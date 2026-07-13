#!/usr/bin/env python3
"""ir_refresh.py — weekly IR replenishment orchestrator.

Flow (exits cleanly when nothing new, so the weekly run is cheap):
  1. discover  — ir_discover.py: new EDGAR filings (vs edgar_seen.json) + private "due" list (cadence).
  2. EDGAR     — collect/edgar_download.py: fetch new periodic forms + EX-99 exhibits (presentations,
                 releases, letters) into the work dir. Resumable (skips already-collected via the seeded manifest).
  3. PRIVATE   — if there are "due" companies (capped IR_DUE_CAP) AND CLAUDE_CODE_OAUTH_TOKEN is set:
                 run the heavy discovery (`claude -p` + the ir-discovery skill) to refresh their
                 ir_sources/<slug>.json with the new period's materials, then collect/ir_download.py fetches them.
  4. delta     — unified rows for everything newly landed under the work dir -> append registry/manifest.csv.
  5. index     — index_ir.py --manifest <delta>: embed ONLY the new files into irdb (never touches the 13GB).
  6. drive     — rclone mirror the new raw files to Drive + rebuild drive_map (link redirect).
  7. refresh   — build_manifest.py (coverage/latest) + carry back updated ir_sources + edgar_seen.
The workflow does checkout / restore irindex / commit registry+state / upload irindex.

Canonical registry = pipeline/ir/registry (in repo); raw lives in Google Drive (cold).
Env: IR_WORK, RCLONE_REMOTE, CLAUDE_CODE_OAUTH_TOKEN, ANTHROPIC_MODEL, IR_DUE_CAP, OPENROUTER_API_KEY/EMBED_*.
"""
import csv, json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
REG = os.path.join(HERE, "registry")
SEEN = os.path.join(HERE, "edgar_seen.json")
WORK = os.environ.get("IR_WORK", os.path.join(REPO, "pipeline", "state", "ir_work"))
DUE_CAP = int(os.environ.get("IR_DUE_CAP", "15"))
DISC_TIMEOUT = int(os.environ.get("IR_DISC_TIMEOUT", "3000"))   # per-subprocess cap for private discovery
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8[1m]")
PY = sys.executable
csv.field_size_limit(10_000_000)
UNIFIED = ["source", "company", "slug", "category", "doc_type", "date", "title", "bytes", "url", "local_path"]


def run(cmd, timeout=None, **env):
    print("  $", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True, timeout=timeout, env={**os.environ, **{k: str(v) for k, v in env.items()}})


def _acc(s):
    return (s or "").replace("-", "").strip()


def seed_work():
    """Copy the canonical registry into WORK so the downloaders SKIP already-collected files
    (they decide 'done' from the seeded manifests); only genuinely-new files land under WORK/data."""
    os.makedirs(WORK, exist_ok=True)
    wreg = os.path.join(WORK, "registry")
    if os.path.exists(wreg):
        shutil.rmtree(wreg)
    shutil.copytree(REG, wreg)


def _rel(lp):
    """normalize any local_path to a 'data/<slug>/...' relative key."""
    lp = (lp or "").replace("\\", "/")
    i = lp.find("/data/")
    if i >= 0:
        return lp[i + 1:]
    return lp[len(WORK) + 1:] if lp.startswith(WORK) else lp


def delta_from_work():
    """Everything newly downloaded this run (its local_path is under WORK) -> unified delta rows.
    Writes WORK/manifest_delta.csv (relative local_paths) and appends to canonical registry/manifest.csv."""
    delta = []
    me = os.path.join(WORK, "registry", "manifest_edgar.csv")
    if os.path.exists(me):
        for r in csv.DictReader(open(me, encoding="utf-8")):
            lp = r.get("local_path", "")
            if lp.startswith(WORK):
                delta.append({"source": "edgar", "company": r.get("company", ""), "slug": r.get("slug", ""),
                              "category": r.get("form", ""), "doc_type": r.get("doc_type", r.get("form", "")),
                              "date": r.get("filing_date", ""), "title": r.get("filename", ""),
                              "bytes": r.get("bytes", "0"), "url": r.get("url", ""), "local_path": _rel(lp)})
    mi = os.path.join(WORK, "registry", "manifest_ir.csv")
    if os.path.exists(mi):
        for r in csv.DictReader(open(mi, encoding="utf-8")):
            lp = r.get("local_path", "")
            if lp.startswith(WORK) and (r.get("status") == "ok"):
                delta.append({"source": "ir", "company": r.get("company", ""), "slug": r.get("slug", ""),
                              "category": r.get("doc_type", ""), "doc_type": r.get("doc_type", ""),
                              "date": r.get("date", ""), "title": r.get("title", r.get("filename", "")),
                              "bytes": r.get("bytes", "0"), "url": r.get("url", ""), "local_path": _rel(lp)})
    if not delta:
        return None
    dpath = os.path.join(WORK, "manifest_delta.csv")
    with open(dpath, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=UNIFIED); w.writeheader(); w.writerows(delta)
    canon = os.path.join(REG, "manifest.csv")
    with open(canon, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=UNIFIED)
        if os.path.getsize(canon) == 0:
            w.writeheader()
        w.writerows(delta)
    print(f"  delta: {len(delta)} new files -> {dpath} (+ appended to manifest.csv)")
    return dpath


def update_seen(new):
    seen = json.load(open(SEEN)) if os.path.exists(SEEN) else {}
    for n in new:
        seen.setdefault(n["cik"], [])
        if _acc(n["accession"]) not in seen[n["cik"]]:
            seen[n["cik"]].append(_acc(n["accession"]))
    json.dump(seen, open(SEEN, "w"))


def carry_back_ir_sources(slugs):
    """Discovery wrote updated ir_sources into WORK; copy the touched ones back to the committed registry."""
    for s in slugs:
        src = os.path.join(WORK, "registry", "ir_sources", f"{s}.json")
        if os.path.exists(src):
            shutil.copy(src, os.path.join(REG, "ir_sources", f"{s}.json"))


def drive_sync():
    remote = os.environ.get("RCLONE_REMOTE")
    if not remote:
        print("  RCLONE_REMOTE unset — new raw NOT pushed to Drive (index still updated)"); return
    run(["rclone", "copy", os.path.join(WORK, "data"), f"{remote}data", "--transfers", "8"])
    run([PY, os.path.join(HERE, "drive_map.py"), "--from-rclone", remote])   # rebuild link map


def _emit_delta(has):
    gho = os.environ.get("GITHUB_OUTPUT")
    if gho:
        open(gho, "a").write(f"has_delta={'true' if has else 'false'}\n")


def main(argv):
    skip_index = "--skip-index" in argv      # collect job: discover + download + drive, leave indexing to a separate job
    run([PY, os.path.join(HERE, "ir_discover.py")])
    disc = json.load(open(os.path.join(HERE, "ir_discovery.json")))
    new = disc.get("new_edgar", [])
    due = [d["slug"] for d in disc.get("due_private", [])][:DUE_CAP]
    n_due_total = len(disc.get("due_private", []))
    print(f"discovery: {len(new)} new EDGAR | {n_due_total} private due (taking {len(due)} this run)", flush=True)
    if n_due_total > len(due):
        print(f"  NOTE: {n_due_total - len(due)} due companies deferred (IR_DUE_CAP={DUE_CAP})", flush=True)
    if not new and not due:
        print("nothing new — done"); _emit_delta(False); return 0

    seed_work()
    if new:
        run([PY, os.path.join(HERE, "collect", "edgar_download.py")], IR_DATASET=WORK)

    # PRIVATE: heavy discovery for due companies, then download what it found
    if due and os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
        prompt = (f"Use the ir-discovery skill to refresh investor-relations materials for ONLY these "
                  f"due companies: {', '.join(due)}. For each, read its current "
                  f"pipeline/ir/registry/ir_sources/<slug>.json (current_ir_site, periods_found), find the "
                  f"NEW reporting period's materials (presentations/results/press/letters) published after "
                  f"its latest periods_found, and write the updated JSON to {WORK}/registry/ir_sources/<slug>.json "
                  f"in the SAME schema (materials:[{{title,doc_type,period,date,url}}]). Add only genuinely new items.")
        try:                                            # private discovery is best-effort: never abort the whole refresh
            cap = os.path.join(WORK, "claude_discovery.jsonl")
            with open(cap, "w", encoding="utf-8") as out:
                subprocess.run(["claude", "-p", prompt, "--model", MODEL, "--dangerously-skip-permissions",
                                "--output-format", "stream-json", "--verbose"], check=True, timeout=DISC_TIMEOUT, stdout=out, env={**os.environ})
            subprocess.run([PY, os.path.join(REPO, "pipeline", "token_trace.py"), cap, "ir-refresh-discovery"])
            run([PY, os.path.join(HERE, "collect", "ir_download.py"), *due], IR_DATASET=WORK, timeout=DISC_TIMEOUT)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            print(f"  private discovery failed/timed out (continuing with EDGAR delta): {e}", flush=True)
    elif due:
        print("  due companies present but CLAUDE_CODE_OAUTH_TOKEN unset — skipping private discovery", flush=True)

    delta = delta_from_work()
    if delta:
        if not skip_index:                          # single-job mode: index inline
            run([PY, os.path.join(HERE, "index_ir.py"), "--full-corpus",
                 "--manifest", delta, "--dataset", WORK, "--group", "200"])
        else:                                       # split mode: the separate index job embeds WORK/data via the artifact
            print(f"  --skip-index: {os.path.basename(delta)} + WORK/data handed to the index job", flush=True)
        drive_sync()
    carry_back_ir_sources(due)
    run([PY, os.path.join(HERE, "build_manifest.py")], IR_DATASET=os.path.join(REPO, "pipeline", "ir"))
    update_seen(new)
    _emit_delta(bool(delta))
    print("ir_refresh: done")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
