#!/usr/bin/env python3
"""ir_discover.py — lightweight weekly "is there a new report?" check (no downloads).

EDGAR (deterministic): for every CIK in registry/edgar_map.csv, reuse the collector's
collect_filings() to list periodic filings since cutoff, and diff against pipeline/ir/edgar_seen.json
(cik -> [accessions already collected]) → NEW filings.
Private/non-EDGAR (heuristic): from registry/ir_sources/<slug>.json use `cadence` + the newest
`periods_found` to flag companies likely DUE for a fresh period (a quarterly reporter whose latest
known period is older than ~110 days).

Writes pipeline/ir/ir_discovery.json {generated, new_edgar:[...], due_private:[...]}. If both empty,
there is nothing to replenish. First run seeds edgar_seen.json from the existing manifest_edgar.csv.

Usage: python3 pipeline/ir/ir_discover.py [--limit N] [--seed-from <manifest_edgar.csv>]
"""
import argparse, csv, json, os, sys, datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
REG = os.path.join(HERE, "registry")
SEEN = os.path.join(HERE, "edgar_seen.json")
OUT = os.path.join(HERE, "ir_discovery.json")
sys.path.insert(0, os.path.join(HERE, "collect"))
import edgar_download as ed

csv.field_size_limit(10_000_000)
PERIODS = {"Q1": (1, 1), "Q2": (4, 1), "Q3": (7, 1), "Q4": (10, 1), "FY": (1, 1)}


def _acc(s):
    return (s or "").replace("-", "").strip()          # normalize accession (dashes vary by source)


def seed_seen(manifest_edgar):
    seen = {}
    if os.path.exists(manifest_edgar):
        for r in csv.DictReader(open(manifest_edgar, encoding="utf-8")):
            cik, acc = (r.get("cik") or "").strip(), _acc(r.get("accession"))
            if cik and acc:
                seen.setdefault(cik, [])
                if acc not in seen[cik]:
                    seen[cik].append(acc)
    return seen


def private_due(today):
    due = []
    src = os.path.join(REG, "ir_sources")
    for fn in os.listdir(src) if os.path.isdir(src) else []:
        if not fn.endswith(".json"):
            continue
        d = json.load(open(os.path.join(src, fn), encoding="utf-8"))
        cad = (d.get("cadence") or "").lower()
        found = d.get("periods_found") or []
        if cad != "quarterly" or not found:
            continue
        # newest period end-date implied by the latest "Qn YYYY" / "FYYYYY"
        latest = found[-1]
        yr = "".join(c for c in latest if c.isdigit())[-4:]
        q = next((k for k in PERIODS if latest.upper().startswith(k)), "Q?")
        try:
            mon = PERIODS.get(q, (1, 1))[0]
            approx = dt.date(int(yr), mon, 1)
        except Exception:
            continue
        if (today - approx).days > 110:          # a new quarter is likely out
            due.append({"slug": d.get("slug", fn[:-5]), "cadence": cad,
                        "latest_period": latest, "ir_site": d.get("current_ir_site", "")})
    return due


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="limit CIKs (testing)")
    ap.add_argument("--seed-from", help="manifest_edgar.csv to seed edgar_seen.json on first run")
    a = ap.parse_args()
    today = dt.date.today()

    seen = json.load(open(SEEN)) if os.path.exists(SEEN) else {}
    if not seen:
        src = a.seed_from or os.path.join(os.environ.get("IR_DATASET",
              os.path.expanduser("~/Documents/IR-dataset")), "registry", "manifest_edgar.csv")
        seen = seed_seen(src)
        json.dump(seen, open(SEEN, "w"))
        print(f"seeded edgar_seen.json from {src}: {sum(len(v) for v in seen.values())} accessions", flush=True)

    rows = list(csv.DictReader(open(os.path.join(REG, "edgar_map.csv"), encoding="utf-8")))
    if a.limit:
        rows = rows[:a.limit]
    new = []
    for r in rows:
        cik, slug = (r.get("cik") or "").strip(), (r.get("slug") or "").strip()
        if not cik:
            continue
        try:
            _name, fils = ed.collect_filings(cik)
        except Exception as e:
            print(f"  {slug}: SEC fetch failed ({e})", flush=True); continue
        known = set(seen.get(cik, []))
        for f in fils:
            acc = _acc(f.get("accession"))
            if acc and acc not in known:
                new.append({"slug": slug, "cik": cik, "form": f.get("form"),
                            "date": f.get("date"), "accession": f.get("accession")})
    due = private_due(today)
    out = {"generated": today.isoformat(), "new_edgar": new, "due_private": due}
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"discovery: {len(new)} new EDGAR filings, {len(due)} private companies likely due -> {OUT}")
    for n in new[:20]:
        print(f"  NEW {n['slug']:18} {n['form']:7} {n['date']}  {n['accession']}")


if __name__ == "__main__":
    main()
