#!/usr/bin/env python3
"""search.py — hybrid search over the News index: dense (OpenRouter) + BM25 (LanceDB FTS),
fused with Reciprocal Rank Fusion, deduped to notes. Importable + CLI.

  search(query, k=20, type=None, region=None, company=None, since=None) -> list[dict]
  CLI: python search.py "запрос" --k 20 [--type earnings] [--region us]
       [--company stripe] [--since 2026-01-01] [--json]

Each result: {note_path, title, date, url, tags, chunk_type, snippet, score}.
"""
import os, sys, json, argparse
import lancedb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import embedder

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB = os.environ.get("NEWSDB", os.path.join(ROOT, "pipeline", "state", "newsdb"))
TABLE = "notes"
K0 = 60  # RRF constant
DRIVE_MAP = os.path.join(ROOT, "pipeline", "ir", "drive_map.json")
_DM = None


def _drive_map():
    """rel_path -> Drive link, for IR results (empty for News). Lazily loaded once."""
    global _DM
    if _DM is None:
        _DM = json.load(open(DRIVE_MAP)) if os.path.exists(DRIVE_MAP) else {}
    return _DM


def _esc(s):
    return str(s).replace("'", "''")


def _where(type=None, region=None, company=None, since=None, doc=None, until=None):
    cl = []
    if type:    cl.append(f"tags LIKE '%type/{_esc(type)}%'")
    if region:  cl.append(f"tags LIKE '%region/{_esc(region)}%'")
    if company: cl.append(f"tags LIKE '%company/{_esc(company)}%'")
    if doc:     cl.append(f"tags LIKE '%doc/{_esc(doc)}%'")   # IR report form: 10-q, 10-k, earnings_release, …
    if since:   cl.append(f"date >= '{_esc(since)}'")
    if until:   cl.append(f"date <= '{_esc(until)}'")          # period upper bound
    return " AND ".join(cl) if cl else None


def search(query, k=20, type=None, region=None, company=None, since=None, pool=60, db=DB, doc=None, until=None):
    where = _where(type, region, company, since, doc, until)
    tbl = lancedb.connect(db).open_table(TABLE)

    qv = embedder.embed([query], kind="query")[0]
    vq = tbl.search(qv).metric("cosine").limit(pool)
    if where:
        vq = vq.where(where, prefilter=True)
    vres = vq.to_list()

    try:
        fq = tbl.search(query, query_type="fts").limit(pool)
        if where:
            fq = fq.where(where, prefilter=True)
        fres = fq.to_list()
    except Exception as e:
        print(f"(fts unavailable: {e})", file=sys.stderr)
        fres = []

    scores, meta = {}, {}
    for rank, row in enumerate(vres):
        scores[row["id"]] = scores.get(row["id"], 0) + 1 / (K0 + rank); meta[row["id"]] = row
    for rank, row in enumerate(fres):
        scores[row["id"]] = scores.get(row["id"], 0) + 1 / (K0 + rank); meta[row["id"]] = row

    best = {}
    for cid, sc in sorted(scores.items(), key=lambda x: -x[1]):
        r = meta[cid]; p = r["note_path"]
        if p not in best:
            best[p] = {"note_path": p, "title": r.get("title", ""), "date": r.get("date", ""),
                       "url": r.get("primary_url", ""),
                       "drive_url": _drive_map().get(p, {}).get("webViewLink", ""),  # IR redirect to the file in Drive
                       "tags": r.get("tags", ""),
                       "chunk_type": r.get("chunk_type", ""), "snippet": r.get("text", "")[:300],
                       "score": round(sc, 5)}
        if len(best) >= k:
            break
    return list(best.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--k", type=int, default=20)
    ap.add_argument("--type"); ap.add_argument("--region")
    ap.add_argument("--company"); ap.add_argument("--since")
    ap.add_argument("--doc", help="IR report form filter: 10-q, 10-k, 20-f, earnings_release, …")
    ap.add_argument("--until", help="upper bound on note date (YYYY-MM-DD) — pick a period")
    ap.add_argument("--db", default=DB)
    ap.add_argument("--json", action="store_true")
    ns = ap.parse_args()
    res = search(ns.query, k=ns.k, type=ns.type, region=ns.region,
                 company=ns.company, since=ns.since, db=ns.db, doc=ns.doc, until=ns.until)
    if ns.json:
        print(json.dumps(res, ensure_ascii=False, indent=1)); return
    for r in res:
        print(f"[{r['score']}] {r['date']}  {r['title']}  ({r['chunk_type']})")
        print(f"    {r['note_path']}")
        if r["url"]:
            print(f"    {r['url']}")
    print(f"\n{len(res)} notes")


if __name__ == "__main__":
    main()
