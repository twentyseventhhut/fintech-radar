# IR registry — your coverage universe (config, not data)

This folder is the **list of companies whose investor-relations materials the pipeline tracks**.
It ships here with a tiny sample — replace it with your own universe.

- **`edgar_map.csv`** — `slug,company,cik` for SEC/EDGAR filers. EDGAR is public (no key); the
  downloader pulls 10-K/10-Q/20-F/6-K/8-K + EX-99 exhibits for each CIK. Sample rows included.
- **`companies.csv`** — the full company list (slug, name, market, ticker…) used for coverage.
- **`ir_sources/<slug>.json`** — for **non-EDGAR / private** companies: their IR site + the materials
  found so far (presentations, results, press, letters). See `ir_sources/EXAMPLE.json` for the schema.
  The weekly `ir-refresh` flow's `ir-discovery` skill fills these in and the downloader fetches the URLs.
- `manifest*.csv`, `../ir_coverage.json`, `../ir_latest.json`, `../edgar_seen.json`, `../drive_map.json`
  are **generated** at runtime (gitignored) — don't hand-edit.

To adapt: put your tickers in `edgar_map.csv`, your private names in `ir_sources/`, and run `ir-refresh`.
