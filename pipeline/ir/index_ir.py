#!/usr/bin/env python3
"""index_ir.py — build a compact LanceDB index of the IR corpus, MIRRORING the news index.

Same table schema as pipeline/semsearch (id, note_path, title, date, month, chunk_type, text,
tags, primary_url, vector) so the existing search.py queries it unchanged — chunks are tagged
`company/<slug>` + `type/earnings` + `doc/<category>`, so `sem search ... --db <irdb> --company stripe`
works out of the box.

Selection = "latest published results": for each (company, category) in the result-bearing set,
keep docs within --since-days OR at least the single latest, capped per category. Everything else
stays cold in the raw corpus. Each row stores a RELATIVE path + the source url + a stable doc_id,
so moving the raw to Google Drive later needs only a different root, never a re-index.

Two phases (so the heavy work is split from the API work and survives the raw moving to Drive):
  python3 index_ir.py --extract-only      # parse raw -> pipeline/state/ir_cache (needs the raw NOW)
  python3 index_ir.py                      # embed from cache -> pipeline/state/irdb (needs no raw)
Resumable/checkpointed like index.py. Reads OPENROUTER_API_KEY/EMBED_* from pipeline/.env.
"""
import os, sys, re, csv, json, hashlib, argparse, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract as ex

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_DS = os.path.expanduser("~/Documents/IR-dataset")
DB = os.environ.get("IRDB", os.path.join(REPO, "pipeline", "state", "irdb"))
TABLE = "notes"

RESULT_CATS = {
    "10-K", "10-Q", "20-F", "6-K", "8-K", "ARS",
    "earnings_release", "quarterly_results", "annual_report",
    "investor_presentation", "transcript", "results", "letter", "press_release",
}
SUPPORTED = (".pdf", ".htm", ".html", ".txt", ".md")
csv.field_size_limit(10_000_000)


def cat_token(cat):
    return re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")


def doc_id(url, rel):
    return hashlib.sha1((url or rel).encode()).hexdigest()[:16]


def chunks(text, maxlen=1500):
    out, buf = [], ""
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if not para:
            continue
        while len(para) > maxlen:                       # hard-split very long paragraphs
            cut = para.rfind(" ", 0, maxlen) or maxlen
            piece, para = para[:cut].strip(), para[cut:].strip()
            if len(piece) >= 40:
                out.append(piece)
        if len(buf) + len(para) + 2 > maxlen:
            if len(buf.strip()) >= 40:
                out.append(buf.strip())
            buf = ""
        buf += para + "\n\n"
    if len(buf.strip()) >= 40:
        out.append(buf.strip())
    return out


def select_all(ds, limit, manifest=None):
    """FULL CORPUS: every supported file in the manifest (one entry per file).
    `manifest` overrides the path — pass a DELTA manifest (only new files) for incremental cloud runs."""
    seen, out = set(), []
    mpath = manifest or os.path.join(ds, "registry", "manifest.csv")
    for r in csv.DictReader(open(mpath, encoding="utf-8")):
        slug = r.get("slug"); lp = r.get("local_path") or ""
        if not slug or os.path.splitext(lp)[1].lower() not in SUPPORTED:
            continue
        rel = os.path.relpath(lp, ds) if lp.startswith(ds) else lp
        if rel in seen:
            continue
        seen.add(rel)
        out.append({"slug": slug, "company": (r.get("company") or slug).strip(),
                    "category": (r.get("category") or r.get("doc_type") or "other").strip(),
                    "date": (r.get("date") or "").strip(), "title": (r.get("title") or "").strip(),
                    "url": (r.get("url") or "").strip(), "rel": rel})
    out.sort(key=lambda d: d["date"], reverse=True)
    return out[:limit] if limit else out


def select(ds, since_days, cats, cap, limit):
    """Return [doc] to index: latest results per (slug, category)."""
    since = (dt.date.today() - dt.timedelta(days=since_days)).isoformat()
    by = {}
    for r in csv.DictReader(open(os.path.join(ds, "registry", "manifest.csv"), encoding="utf-8")):
        slug = r.get("slug"); cat = (r.get("category") or r.get("doc_type") or "").strip()
        if not slug or cat not in cats:
            continue
        lp = r.get("local_path") or ""
        if os.path.splitext(lp)[1].lower() not in SUPPORTED:
            continue
        rel = os.path.relpath(lp, ds) if lp.startswith(ds) else lp
        by.setdefault((slug, cat), []).append({
            "slug": slug, "company": (r.get("company") or slug).strip(), "category": cat,
            "date": (r.get("date") or "").strip(), "title": (r.get("title") or "").strip(),
            "url": (r.get("url") or "").strip(), "rel": rel})
    selected = []
    for (slug, cat), docs in by.items():
        docs.sort(key=lambda d: d["date"], reverse=True)
        keep = [d for d in docs if d["date"] >= since][:cap] or docs[:1]
        selected.extend(keep)
    selected.sort(key=lambda d: d["date"], reverse=True)
    return selected[:limit] if limit else selected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=os.environ.get("IR_DATASET", DEFAULT_DS))
    ap.add_argument("--db", default=DB)
    ap.add_argument("--since-days", type=int, default=365)
    ap.add_argument("--cap-per-cat", type=int, default=6)
    ap.add_argument("--all-cats", action="store_true", help="index every category, not just result-bearing")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--group", type=int, default=200)
    ap.add_argument("--extract-only", action="store_true", help="parse raw -> text cache, no embedding")
    ap.add_argument("--full-corpus", action="store_true", help="index EVERY supported file (not just latest results)")
    ap.add_argument("--manifest", help="override manifest path — pass a DELTA manifest for incremental runs")
    ns = ap.parse_args()
    ds = os.path.abspath(ns.dataset)

    if ns.full_corpus:
        docs = select_all(ds, ns.limit, ns.manifest)
        print(f"selected {len(docs)} docs (FULL CORPUS — all supported files)", flush=True)
    else:
        cats = RESULT_CATS
        docs = select(ds, ns.since_days, cats, ns.cap_per_cat, ns.limit)
        print(f"selected {len(docs)} docs (latest results, since-days={ns.since_days}, cap/cat={ns.cap_per_cat})", flush=True)

    # ---- extract-only: just populate the text cache from the raw (needs the raw NOW) ----
    if ns.extract_only:
        done = chars = empty = 0
        for d in docs:
            t = ex.extract(os.path.join(ds, d["rel"]), cache_key=doc_id(d["url"], d["rel"]), url=d["url"])
            done += 1; chars += len(t); empty += (len(t) < 100)
            if done % 200 == 0:
                print(f"  extracted {done}/{len(docs)} ({empty} empty so far)", flush=True)
        print(f"extract-only done: {done} docs, {empty} empty/failed, {chars/1e6:.1f}M chars cached", flush=True)
        return

    # ---- embed + index (reads the cache; raw not required if already extracted) ----
    sys.path.insert(0, os.path.join(REPO, "pipeline", "semsearch"))
    import lancedb, embedder

    os.makedirs(ns.db, exist_ok=True)
    hpath = os.path.join(ns.db, "hashes.json")
    hashes = json.load(open(hpath)) if os.path.exists(hpath) else {}
    con = lancedb.connect(ns.db)
    try:
        tbl = con.open_table(TABLE)
    except Exception:
        tbl = None

    todo = [d for d in docs if hashes.get(d["rel"]) != d["date"]]   # cheap key: rel -> date (no raw read)
    print(f"to index: {len(todo)}/{len(docs)} (skipping {len(docs)-len(todo)} already indexed)", flush=True)
    if not todo:
        if tbl is not None:
            try: tbl.create_fts_index("text", use_tantivy=False, replace=True)
            except Exception: pass
        print("up to date"); return

    done = 0
    for gi in range(0, len(todo), ns.group):
        grp = todo[gi:gi + ns.group]
        rows = []
        for d in grp:
            did = doc_id(d["url"], d["rel"])
            text = ex.extract(os.path.join(ds, d["rel"]), cache_key=did, url=d["url"])
            if len(text) < 100:
                continue
            title = f"{d['company']} {d['category']} {d['date']}".strip()
            tags = f"company/{d['slug']} type/earnings doc/{cat_token(d['category'])}"
            for i, ch in enumerate(chunks(text)):
                rows.append({
                    "id": hashlib.sha1(f"{d['rel']}#{i}".encode()).hexdigest()[:16],
                    "note_path": d["rel"], "doc_id": did, "slug": d["slug"],
                    "story_id": d["slug"], "title": title, "date": d["date"], "month": d["date"][:7],
                    "chunk_type": d["category"], "text": ch, "tags": tags,
                    "primary_url": d["url"], "_embed": f"{title}\n{ch}"[:6000]})
        if rows:
            vecs = embedder.embed([r.pop("_embed") for r in rows])
            for r, v in zip(rows, vecs):
                r["vector"] = v
            # drop any stale chunks for re-indexed docs, then add
            if tbl is not None:
                for d in {r["note_path"] for r in rows}:
                    try: tbl.delete(f"note_path = '{d.replace(chr(39), chr(39)*2)}'")
                    except Exception: pass
                tbl.add(rows)
            else:
                tbl = con.create_table(TABLE, data=rows)
        for d in grp:
            hashes[d["rel"]] = d["date"]
        json.dump(hashes, open(hpath, "w"))
        done += len(grp)
        print(f"  checkpoint {done}/{len(todo)} docs | rows={tbl.count_rows() if tbl else 0}", flush=True)

    try:
        tbl.create_fts_index("text", use_tantivy=False, replace=True)
    except Exception as e:
        print("fts warning:", e)
    print(f"done — rows={tbl.count_rows()} db={ns.db}", flush=True)


if __name__ == "__main__":
    main()
