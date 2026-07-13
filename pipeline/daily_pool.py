#!/usr/bin/env python3
"""Build the [2] ranking pool / [3] publish pool — WITH deterministic dedup surfacing.

  daily_pool.py --date YYYY-MM-DD --days N --out pool.json [--enriched]

Why this exists: the same real-world event often spawns SEVERAL notes across ingest
cycles (different source, reworded title, a later "stage" of the story). Title-only
dedup by the LLM misses them. The semantic index is too coarse for this (RRF scores
top out ~0.03) AND it is rebuilt only AFTER publish, so it is blind to same-day twins
at decision time. The reliable, deterministic signal available right now is the
`company/*` tag overlap.

So every pool entry carries `dup_candidates`: recently-published notes AND the other
candidates in THIS batch that share a company/* tag — a short, focused list the ranker
/ digest agent uses to catch the SAME event even when titles or sources differ.

In --enriched (publish) mode we ALSO enforce the enricher's own verdict: a note whose
[2] enrichment concluded `freshness: stale` or set `duplicate_of:` is dropped outright
(the enricher's internal retrieval already found the prior coverage — e.g. it can write
"GBP re-framing of the SAME FY2025 results already in-base" — but that finding was
previously advisory; now it is enforced here).
"""
import argparse, glob, json, os, re, datetime as dt

NEWS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "News")


def fm_get(text, key):
    m = re.search(rf'^{re.escape(key)}:\s*(.*)$', text, re.M)
    return m.group(1).strip().strip('"') if m else ""


def tags_of(text):
    m = re.search(r'^tags:\n((?:  - .*\n)+)', text, re.M)
    return [l.strip()[2:] for l in m.group(1).splitlines()] if m else []


def companies(tags):
    return {t for t in tags if t.startswith("company/")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--out", required=True)
    ap.add_argument("--enriched", action="store_true",
                    help="[3] publish mode: select ENRICHED-but-not-yet-published notes "
                         "(digest candidates) instead of the un-enriched [2] pool")
    ap.add_argument("--dup-window", type=int, default=30,
                    help="days of already-published history surfaced for company-tag dedup")
    ap.add_argument("--dup-cap", type=int, default=8, help="max dup_candidates per entry")
    a = ap.parse_args()

    cutoff = (dt.date.fromisoformat(a.date) - dt.timedelta(days=a.days)).isoformat()
    # wider window of ALREADY-PUBLISHED stories surfaced for dedup (keyed on EVENT date),
    # so a story published recently but dated a few days earlier is still caught.
    pub_cutoff = (dt.date.fromisoformat(a.date) - dt.timedelta(days=max(a.days, a.dup_window))).isoformat()

    notes = []
    for f in glob.glob(os.path.join(NEWS, "*", "*.md")):
        with open(f) as fh:
            head = fh.read(2500)
        date = fm_get(head, "date")
        if not date or date < pub_cutoff:
            continue
        notes.append({
            "story_id": fm_get(head, "story_id"),
            "date": date,
            "title": fm_get(head, "title"),
            "tags": tags_of(head),
            "status": fm_get(head, "status"),
            "enriched": fm_get(head, "enriched").lower() == "true",
            "freshness": fm_get(head, "freshness").lower(),
            "duplicate_of": fm_get(head, "duplicate_of"),
            "note": os.path.relpath(f, NEWS),
        })

    published = [n for n in notes if n["status"] == "published"]

    # candidate set
    dropped_stale = []
    if a.enriched:
        cands = []
        for n in notes:
            if n["status"] == "published" or not n["enriched"] or n["date"] < cutoff:
                continue
            if n["freshness"] == "stale" or n["duplicate_of"]:
                dropped_stale.append(n)          # ENFORCE the enricher's freshness/dup verdict
                continue
            cands.append(n)
    else:
        cands = [n for n in notes
                 if n["status"] != "published" and not n["enriched"] and n["date"] >= cutoff]

    # deterministic dedup surfacing: per candidate, same-company published notes + intra-batch peers
    surface = published + cands
    for c in cands:
        cc = companies(c["tags"])
        dups = []
        if cc:
            for o in surface:
                if o["note"] == c["note"]:
                    continue
                if cc & companies(o["tags"]):
                    dups.append({"story_id": o["story_id"], "date": o["date"],
                                 "title": o["title"], "status": o["status"], "note": o["note"]})
            dups.sort(key=lambda x: x["date"], reverse=True)
        c["dup_candidates"] = dups[:a.dup_cap]

    pool = [{"story_id": c["story_id"], "date": c["date"], "title": c["title"],
             "tags": c["tags"], "note": c["note"], "dup_candidates": c["dup_candidates"]}
            for c in sorted(cands, key=lambda x: x["date"], reverse=True)]

    json.dump(pool, open(a.out, "w"), ensure_ascii=False)
    pub_path = os.path.join(os.path.dirname(a.out) or ".", "recent_published.json")
    rp = [{"story_id": n["story_id"], "date": n["date"], "title": n["title"], "tags": n["tags"]}
          for n in sorted(published, key=lambda x: x["date"], reverse=True)]
    json.dump(rp, open(pub_path, "w"), ensure_ascii=False)

    kind = "enriched publish-candidates" if a.enriched else "un-enriched"
    n_surf = sum(1 for c in pool if c["dup_candidates"])
    extra = f"; DROPPED {len(dropped_stale)} stale/duplicate" if dropped_stale else ""
    print(f"pool: {len(pool)} {kind} since {cutoff} ({n_surf} with dup_candidates){extra}; "
          f"{len(rp)} already-published since {pub_cutoff} -> {a.out}, {pub_path}")
    for n in dropped_stale:
        print(f"  drop {n['freshness'] or 'dup'}: {n['title'][:70]}"
              + (f" (dup_of {n['duplicate_of'][:40]})" if n['duplicate_of'] else ""))


if __name__ == "__main__":
    main()
