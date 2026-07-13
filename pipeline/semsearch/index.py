#!/usr/bin/env python3
"""index.py — build/sync a LanceDB hybrid index (dense OpenRouter/Qwen + BM25) of the News vault.

Incremental + CHECKPOINTED: processes changed notes in groups; embeds + writes to LanceDB and
updates pipeline/state/newsdb/hashes.json after EACH group. Safe to interrupt / re-run — it
resumes from the last checkpoint (already-hashed notes are skipped), so a crash loses at most
one group. Chunks ≤1500 chars on paragraph boundaries, tagged by section; each chunk embedded
as "title\\ntext" so the headline anchors the vector.

Usage:
  python index.py check                              # verify embedder connectivity + dim
  python index.py index [--full] [--limit N] [--group 300] [--vault DIR] [--db DIR]
"""
import os, sys, re, json, hashlib, argparse, glob
import frontmatter
import lancedb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import embedder

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VAULT = os.path.join(ROOT, "News")
DB = os.environ.get("NEWSDB", os.path.join(ROOT, "pipeline", "state", "newsdb"))
TABLE = "notes"

SECTION_TYPE = {"Агрегированный текст": "aggregated", "Первоисточники": "source",
                "Контекст": "context", "Челлендж": "challenge"}
SKIP_PREFIXES = ("> [!", "_(нет", "### Прочие ссылки", "- <http", "<http")


def _clean(body):
    out = []
    for ln in body.splitlines():
        s = ln.rstrip()
        if not s.strip():
            out.append(""); continue
        st = s.lstrip()
        if st.startswith(SKIP_PREFIXES) or st.startswith("<!--"):
            continue
        out.append(s)
    return out


def _chunks(title, body, maxlen=1500):
    cur, buf, chunks = "aggregated", "", []

    def flush():
        nonlocal buf
        t = buf.strip()
        if len(t) >= 40:
            chunks.append((cur, t))
        buf = ""

    for ln in _clean(body):
        h = re.match(r'^#{1,4}\s+(.*)$', ln)
        if h:
            head = h.group(1).strip()
            sec = next((v for k, v in SECTION_TYPE.items() if head.startswith(k)), None)
            if sec:
                flush(); cur = sec
            else:
                if len(buf) + len(head) + 2 > maxlen:
                    flush()
                buf += head + ". "
            continue
        if len(buf) + len(ln) + 1 > maxlen:
            flush()
        buf += ln + "\n"
    flush()
    return chunks


def parse_note(path):
    post = frontmatter.load(path)
    m = post.metadata
    title = str(m.get("title", "")).strip()
    date = str(m.get("date", "")).strip()
    tags = [str(t) for t in (m.get("tags") or [])]
    srcs = m.get("sources") or []
    url = str(srcs[0]) if srcs else ""
    story = str(m.get("story_id", ""))
    relp = os.path.relpath(path, ROOT)
    rows = []
    for i, (ctype, text) in enumerate(_chunks(title, post.content)):
        rows.append({"id": hashlib.sha1(f"{relp}#{i}".encode()).hexdigest()[:16],
                     "note_path": relp, "story_id": story, "title": title, "date": date,
                     "month": date[:7], "chunk_type": ctype, "text": text,
                     "tags": " ".join(tags), "primary_url": url,
                     "_embed": f"{title}\n{text}"[:6000]})
    return rows


def _md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def _esc(s):
    return s.replace("'", "''")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", default="index", choices=["index", "check"])
    ap.add_argument("--vault", default=VAULT)
    ap.add_argument("--db", default=DB)
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--group", type=int, default=300)
    ns = ap.parse_args()

    if ns.cmd == "check":
        v = embedder.embed(["проверка соединения"])
        print(f"embedder OK — dim={len(v[0])}"); return

    os.makedirs(ns.db, exist_ok=True)
    hpath = os.path.join(ns.db, "hashes.json")
    hashes = {} if ns.full else (json.load(open(hpath)) if os.path.exists(hpath) else {})
    old_keys = set(hashes)

    files = sorted(glob.glob(os.path.join(ns.vault, "*", "*.md")))
    if ns.limit:
        files = files[:ns.limit]
    file_md5 = {os.path.relpath(f, ROOT): _md5(f) for f in files}     # one md5 per file
    present = set(file_md5)
    changed = [(f, os.path.relpath(f, ROOT)) for f in files
               if hashes.get(os.path.relpath(f, ROOT)) != file_md5[os.path.relpath(f, ROOT)]]
    deleted = [p for p in old_keys if p not in present]
    print(f"notes={len(files)} changed/new={len(changed)} deleted={len(deleted)}", flush=True)

    con = lancedb.connect(ns.db)
    try:
        tbl = con.open_table(TABLE)
        if ns.full:
            con.drop_table(TABLE); tbl = None
    except Exception:
        tbl = None

    # drop stale chunks for re-indexed (previously-known) + deleted notes
    to_del = {relp for _, relp in changed if relp in old_keys} | set(deleted)
    if tbl is not None and to_del:
        for p in to_del:
            tbl.delete(f"note_path = '{_esc(p)}'")
    for p in deleted:
        hashes.pop(p, None)
    if deleted:
        json.dump(hashes, open(hpath, "w"))

    if not changed:
        print("up to date — nothing to embed", flush=True)
        if tbl is not None:
            try: tbl.create_fts_index("text", use_tantivy=False, replace=True)
            except Exception: pass
        return

    total, done = len(changed), 0
    for gi in range(0, total, ns.group):
        grp = changed[gi:gi + ns.group]
        rows = []
        for f, relp in grp:
            rows.extend(parse_note(f))
        if rows:
            vecs = embedder.embed([r.pop("_embed") for r in rows])
            for r, v in zip(rows, vecs):
                r["vector"] = v
            if tbl is None:
                tbl = con.create_table(TABLE, data=rows)
            else:
                tbl.add(rows)
        for f, relp in grp:
            hashes[relp] = file_md5[relp]
        json.dump(hashes, open(hpath, "w"))                          # checkpoint
        done += len(grp)
        print(f"  checkpoint {done}/{total} notes | rows={tbl.count_rows() if tbl else 0}", flush=True)

    try:
        tbl.create_fts_index("text", use_tantivy=False, replace=True)
    except Exception as e:
        print("fts index warning:", e)
    print(f"done — rows={tbl.count_rows()} notes_indexed={len(hashes)} db={ns.db}", flush=True)


if __name__ == "__main__":
    main()
