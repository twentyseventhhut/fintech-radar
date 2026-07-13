# IR source — investor-relations corpus for the peer set

A second big data source: IR / SEC filings for ~360 covered companies (the raw `IR-dataset`,
~13 GB). The pipeline **never ships the raw** — it follows the same hot/cold split as `semsearch`:

| layer | what | where | size |
|---|---|---|---|
| **cold** | raw filings (PDF/HTML/…) | `IR-dataset/data/<slug>/…` (local now → **Google Drive** later) | ~13 GB |
| **hot** | compact vector index | `pipeline/state/irdb` → GitHub Release `irindex` | ~100–300 MB |
| **hot** | coverage crosswalk + latest-results pointers | `pipeline/ir/ir_coverage.json`, `ir_latest.json` (committed) | <2 MB |

Each index row + manifest entry stores a **relative path + source url + stable `doc_id`**, never an
absolute path — so moving the raw to Drive needs only a different root, never a re-index.

## Components
- `build_manifest.py` — reads `IR-dataset/registry/{manifest,companies,edgar_map}.csv` → writes
  `ir_coverage.json` (slug → company/ticker/cik/market/segment/n_files) and `ir_latest.json`
  (slug → latest docs per category + the single `latest_result`). Tiny, committed, refresh anytime.
- `extract.py` — doc → plain text. Resolution order **cache → local path → source url** (best-effort
  download). Cached under `pipeline/state/ir_cache/<doc_id>.txt`, so once extracted the raw is never
  needed again. PDF via PyMuPDF; HTML/htm via a stdlib stripper.
- `index_ir.py` — builds `pipeline/state/irdb` (a LanceDB with the **same schema as `newsdb`**, so the
  existing `search.py` queries it). Chunks are tagged `company/<slug> type/earnings doc/<category>`.
  Selection = "latest published results": per (company, category) keep docs within `--since-days`
  (default 365) or at least the latest, capped `--cap-per-cat` (6). ~2k docs under defaults.

## Build / refresh (one command, resumable)
```bash
PY=pipeline/semsearch/.venv/bin/python            # py3.13 venv (lancedb + pymupdf)
# point at wherever the raw lives (local now, a Drive mount later):
export IR_DATASET="$HOME/Documents/IR-dataset"
$PY pipeline/ir/build_manifest.py                 # refresh the crosswalk + latest pointers
$PY pipeline/ir/index_ir.py                       # extract + embed -> pipeline/state/irdb
# query it (your existing CLI, just point --db at irdb):
./pipeline/semsearch/sem search "segment revenue guidance" --db pipeline/state/irdb --company stripe --json
```
`index_ir.py` reads `OPENROUTER_API_KEY`/`EMBED_*` from `pipeline/.env` (same Qwen-1024 as the news
index → vectors are compatible). Checkpointed: safe to interrupt / re-run.

## Future flow on Google Drive (cold raw in the cloud)
The hot loop is unaffected — only the **raw root** moves. Two ways to refresh/deep-dive against Drive:

1. **Drive mount (simplest)** — Google Drive Desktop / `rclone mount` exposes the corpus as a folder;
   set `IR_DATASET=/path/to/mount/IR-dataset` and run `index_ir.py` as usual. Zero code change.
2. **No mount needed** — `extract.py` falls back to the **source url** per doc, so a refresh/deep-dive
   works even with the raw only in Drive and not synced locally (slower; network-bound). For a future
   Drive-API (file-id) path, add one `doc_id → drive_file_id` map; the index keys on `doc_id` already.

The cloud pipeline (GitHub Actions) **never pulls the 13 GB**: it restores only `irdb` from a Release
`irindex` (mirror the `semindex` restore/upload steps in `ingest-enrich.yml`) plus the committed
`ir_*.json`. Distribute the index like the news one:
```bash
tar -czf /tmp/irdb.tar.gz -C pipeline/state irdb
gh release upload irindex /tmp/irdb.tar.gz --clobber || gh release create irindex /tmp/irdb.tar.gz -t "IR index"
```

## Search by period / form + redirect (point 4)
`search.py` (and `sem search --db pipeline/state/irdb`) filters: `--company <slug>`, `--doc <form>`
(10-q / 10-k / 20-f / earnings_release / …), `--since` / `--until` (period window). Each hit carries the
source `url`; once `drive_map.json` exists it also resolves to the Drive file link for deep processing.

## Enrichment [2] integration (point 5) — DONE
When a pick's `company/<slug>` is in `ir_coverage.json`, `[2] market` (every pick) and `[2] earnings`
(now also triggered by IR-coverage) ALWAYS pull the company's filed results: `ir_latest.json` for the
latest period + doc link, and `sem search --db pipeline/state/irdb --company <slug>` for figures, folded
into `market_research`/`earnings_review` with a redirect link. Cloud `ingest-enrich.yml` restores the
`irindex` Release so [2] has `irdb`.

## Weekly replenishment (point 1+2) — `.github/workflows/ir-refresh.yml`
Mondays (+ manual dispatch): `ir_refresh.py` runs `ir_discover.py` (EDGAR: diff each CIK's SEC submissions
vs `edgar_seen.json`; private: `ir_sources` cadence → "due" list). If new EDGAR filings → `collect/edgar_download.py`
fetches them → delta appended to `registry/manifest.csv` → `index_ir.py --manifest <delta>` embeds ONLY the
new files → Drive mirror + `drive_map` (if creds) → `build_manifest.py` refreshes coverage/latest → commit +
upload `irindex`. Never pulls the 13GB. Private/non-EDGAR "due" companies are reported for the heavier
`wf_*_discovery` collection flow (run separately, as in the IR-dataset `scripts/`).

## Drive redirect (point 4b) + Drive access — rclone OAuth (recommended)
Drive is ID-addressed, so `drive_map.py` enumerates the folder and maps `rel_path -> {file_id, webViewLink}`
(joined to the index by `note_path`; no rebuild). Use **rclone with your own Google account (OAuth)** — it
needs NO service-account key (org policy `iam.disableServiceAccountKeyCreation` blocks those), avoids the
service-account consumer-Drive storage-quota wall, and covers BOTH read (link map) and write (mirror):
1. `brew install rclone` → `rclone config` → new remote `irdrive`, type `drive`, blank client_id/secret,
   scope `drive`, `root_folder_id` = the IR-dataset folder id, auto-config (browser → log in → allow).
2. local one-time link map: `python3 pipeline/ir/drive_map.py --from-rclone irdrive:`
3. for Actions: put `~/.config/rclone/rclone.conf` into GitHub **secret `RCLONE_CONFIG`** and set repo
   **var `RCLONE_REMOTE`** = `irdrive:` (the workflow writes the conf, mirrors new files, refreshes the map).
Until set, new files are still indexed and the redirect falls back to the source url.
(Service-account path via `--folder <id>` + `GDRIVE_SA_KEY` still exists, but requires key creation to be
allowed by org policy and can't write to a personal Drive — prefer rclone.)
