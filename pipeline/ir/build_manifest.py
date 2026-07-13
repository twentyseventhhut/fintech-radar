#!/usr/bin/env python3
"""build_manifest.py — turn the IR-dataset registry into two compact JSONs the pipeline ships.

Reads the already-collected IR-dataset (default ~/Documents/IR-dataset) registry CSVs and writes:
  pipeline/ir/ir_coverage.json  — slug -> {company, ticker, cik, market, segment, public, n_files, categories}
                                   the COVERAGE CROSSWALK ([2] checks if a news note's company is covered)
  pipeline/ir/ir_latest.json    — slug -> {category -> [recent docs]} + "latest" per result category
                                   the "latest published results" pointer (date, title, rel-path, url)

Both are tiny (<2MB) and committed to the repo. The raw 13GB stays where it is (cold); only these
pointers + the compact vector index (built separately by index_ir.py) travel with the pipeline.

Usage: python3 pipeline/ir/build_manifest.py [--dataset DIR]
"""
import argparse, csv, json, os, sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_DS = os.path.expanduser("~/Documents/IR-dataset")

# result-bearing categories surfaced as "latest results" (governance/proxy excluded from the headline view)
RESULT_CATS = {
    "10-K", "10-Q", "20-F", "6-K", "8-K", "ARS",
    "earnings_release", "quarterly_results", "annual_report",
    "investor_presentation", "transcript", "results", "letter", "press_release",
}
RECENT_PER_CAT = 4    # keep the most recent N docs per category in ir_latest.json


def rows(path):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        yield from csv.DictReader(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=os.environ.get("IR_DATASET", DEFAULT_DS))
    a = ap.parse_args()
    ds = os.path.abspath(a.dataset)
    reg = os.path.join(ds, "registry")
    if not os.path.isdir(reg):
        sys.exit(f"no registry/ under {ds} — set --dataset")

    # crosswalk inputs
    companies = {r["slug"]: r for r in rows(os.path.join(reg, "companies.csv")) if r.get("slug")}
    edgar = {r["slug"]: r for r in rows(os.path.join(reg, "edgar_map.csv")) if r.get("slug")}

    # walk the unified file manifest
    by_slug_cat = defaultdict(lambda: defaultdict(list))   # slug -> cat -> [doc]
    n_files = defaultdict(int)
    cat_counts = defaultdict(lambda: defaultdict(int))
    for r in rows(os.path.join(reg, "manifest.csv")):
        slug = r.get("slug")
        if not slug:
            continue
        cat = (r.get("category") or r.get("doc_type") or "other").strip()
        lp = r.get("local_path") or ""
        rel = os.path.relpath(lp, ds) if lp.startswith(ds) else lp
        doc = {"date": (r.get("date") or "").strip(), "title": (r.get("title") or "").strip(),
               "category": cat, "source": (r.get("source") or "").strip(),
               "path": rel, "url": (r.get("url") or "").strip(),
               "bytes": int(r["bytes"]) if (r.get("bytes") or "").isdigit() else 0}
        by_slug_cat[slug][cat].append(doc)
        n_files[slug] += 1
        cat_counts[slug][cat] += 1

    coverage, latest = {}, {}
    for slug in sorted(set(by_slug_cat) | set(companies)):
        c = companies.get(slug, {})
        e = edgar.get(slug, {})
        coverage[slug] = {
            "company": c.get("company") or e.get("company") or slug,
            "ticker": (e.get("ticker") or "").strip(),
            "cik": (e.get("cik") or "").strip(),
            "public": (c.get("public") or "").strip(),
            "market": (c.get("market") or "").strip(),
            "segment": (c.get("segment") or "").strip(),
            "core_business": (c.get("core_business") or "").strip(),
            "n_files": n_files.get(slug, 0),
            "categories": dict(cat_counts.get(slug, {})),
        }
        # latest.json: per category the most-recent RECENT_PER_CAT docs (date desc)
        lat = {}
        for cat, docs in by_slug_cat.get(slug, {}).items():
            docs.sort(key=lambda d: d["date"], reverse=True)
            lat[cat] = docs[:RECENT_PER_CAT]
        # the single most recent result-bearing doc overall = the headline "latest result"
        results = [d for cat in lat for d in lat[cat] if cat in RESULT_CATS]
        results.sort(key=lambda d: d["date"], reverse=True)
        latest[slug] = {"categories": lat, "latest_result": results[0] if results else None}

    out = os.path.join(REPO, "pipeline", "ir")
    os.makedirs(out, exist_ok=True)
    json.dump(coverage, open(os.path.join(out, "ir_coverage.json"), "w"), ensure_ascii=False, indent=1)
    json.dump(latest, open(os.path.join(out, "ir_latest.json"), "w"), ensure_ascii=False, indent=1)

    covered = sum(1 for v in coverage.values() if v["n_files"])
    print(f"coverage: {len(coverage)} companies ({covered} with files); "
          f"{sum(n_files.values())} files -> pipeline/ir/ir_coverage.json, ir_latest.json")


if __name__ == "__main__":
    main()
