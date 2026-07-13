---
name: ir-discovery
description: >
  Discover NEW investor-relations materials for a given list of "due" private/non-EDGAR companies and
  write each company's updated ir_sources/<slug>.json (materials: presentations, results, press releases,
  shareholder letters). Used by the weekly ir_refresh flow when companies are flagged due by cadence.
  Invoke with an explicit list of company slugs.
---

# IR discovery — new materials for due companies

You refresh investor-relations catalogues for a SPECIFIC, SHORT list of company slugs (passed in the
prompt). Do NOT touch any company not in that list. Per company, find materials published AFTER its
latest known period and append them — never invent URLs.

## For each slug
1. Read its current catalogue `pipeline/ir/registry/ir_sources/<slug>.json`
   (fields: `company`, `current_ir_site`, `cadence`, `periods_found`, `periods_missing`, `materials`).
2. Find its **current** official IR / investor-relations page (handle rebrands/migrations) — WebSearch
   `"<company> investor relations"`, then WebFetch the IR / "financial results" / "presentations" pages.
3. Identify the reporting periods published **after** the latest in `periods_found` (respect `cadence`:
   quarterly → next Qn; annual → next FY; etc.). For each NEW period collect the actual documents:
   earnings/investor **presentation**, **results**/financial statements, **press release**, shareholder
   **letter**, **annual report**. Get the DIRECT file URL (PDF/PPTX/XLSX), not the landing page.
4. Skepticism: only real, dated, downloadable documents; `date` (YYYY-MM-DD) must be ≥ the new period and
   not already present in `materials` (dedupe by url). If nothing new is actually out yet, add nothing.

## Output (MANDATORY) — write to the WORK registry, not the repo
Write the merged catalogue to `$IR_WORK/registry/ir_sources/<slug>.json` (the prompt gives the path;
default `pipeline/state/ir_work/registry/ir_sources/<slug>.json`), SAME schema as the input:
```json
{ "slug":"...", "company":"...", "found":true, "current_ir_site":"https://...",
  "ir_pages":["..."], "cadence":"quarterly",
  "periods_found":[...,"<new period>"], "periods_missing":[...],
  "materials":[ {"title":"...","doc_type":"investor_presentation|earnings_release|quarterly_results|annual_report|press_release|letter","period":"Q_ YYYY","date":"YYYY-MM-DD","url":"https://direct-file"} , ... ] }
```
Keep ALL existing `materials` and ADD the new ones (the downloader fetches only URLs it hasn't seen).
Report one line per slug: `<slug>: +N new materials (<periods>)` or `<slug>: nothing new`.
```
(`ir_download.py <slug…>` then fetches the new URLs into the work dir; ir_refresh indexes + mirrors them.)
```
