# Fintech Radar

An automated **market-intelligence pipeline**: it collects news + investor-relations documents into a
searchable knowledge base, enriches the important events with AI analysis, and turns that into a **daily
digest** (auto-posted to Telegram) and an **on-demand research bot**. It runs itself on a schedule in the
cloud — no human in the loop — using **Claude Code on a Claude Max subscription** (flat-rate, no per-token API bill).

This repo is a **reusable template**. Nothing about it is fintech-specific under the hood — swap the sources
and the entity list and you have the same machine for any domain (see [Reuse](#reuse-it-for-your-domain)).

```
  SOURCES                    PROCESS                          OUTPUT
  ┌──────────────┐           ┌───────────────────────┐        ┌────────────────────┐
  │ newsletters  │─┐         │ [1] dedup → notes DB   │        │ daily digest       │
  │ (IMAP)       │ │  ingest │     (AI tags)          │  rank  │ → telegra.ph + TG  │
  ├──────────────┤ ├────────▶│ hybrid semantic index  │───────▶│ channel            │
  │ Telegram     │ │  (python)│    (LanceDB)          │  [2]   ├────────────────────┤
  │ channels     │ │         │ [2] enrich top events  │ enrich │ research bot        │
  ├──────────────┤ │         │     [0]–[4] + red-team │───────▶│ (Telegram → 1-pager)│
  │ IR documents │─┘         │     (Claude sub-agents)│        │                    │
  │ (EDGAR+Drive)│           └───────────────────────┘        └────────────────────┘
  └──────────────┘
     Claude Code (Max)  ·  GitHub Actions (schedule)  ·  self-hosted Fly runner (0 CI minutes)
```

---

## How it works

### 1 · Collect (three sources, full text, incremental)
| Source | What | Scripts / services |
|---|---|---|
| **Newsletters** | Pulls newsletter emails, **splits round-ups into individual stories**, and fetches the **full text of each primary source**. | `mail_ingest.py` (IMAP) → `mail_to_items.py` → `fintech_radar.py expand`; services: IMAP, article fetchers |
| **Telegram channels** | Posts from the channels you follow. | `tg_ingest.py` |
| **IR documents** | SEC/EDGAR filings + investor presentations + private materials for your coverage list; auto-replenished. | `pipeline/ir/` (`ir_discover.py`, `ir_refresh.py`, `collect/edgar_download.py`, `collect/ir_download.py`) + `ir-discovery` skill; services: SEC EDGAR, rclone → Google Drive |

Raw fetching is **plain Python — zero LLM tokens**.

### 2 · Process
| Step | What | Scripts / skills / services |
|---|---|---|
| **Knowledge base** | Every story → a note with **AI tags** (company / industry / region / type) linked to its sources. | `daily_source.py`, `make_notes.py`; skill `daily-fintech` **[1]** |
| **Dedup** | One event spread across many headlines/sources is collapsed by company tag + event match. | `daily_pool.py`, `dedupe.py` + an enforced freshness verdict in enrichment |
| **Index** | **Hybrid semantic search** (dense embeddings + full-text BM25, fused with RRF) over news **and** IR. IR = hot index + cold raw in Drive (link back to the source doc). | `pipeline/semsearch/` (`sem`, `index.py`, `embedder.py`), `ir/index_ir.py`; **LanceDB**, embeddings via **OpenRouter (Qwen3-Embedding-8B)** |
| **Enrich** | Rank the cycle's top events, then a Claude agent writes a **[0]–[4] breakdown** (what actually happened minus the PR → competitors → company history → novelty/traction → what's next) plus a **red-team importance score**, grounded in the corpus + IR figures + web. | skills `daily-fintech` **[2]**, `context-enrichment`; `note_patch.py`; plugin agents **market-researcher / earnings-reviewer**; Claude (Opus) + WebSearch |

### 3 · Output
| Product | What | Scripts / skills / services |
|---|---|---|
| **Daily digest** | Two market sections (top ~70% each) → a **telegra.ph** article + a link posted to your **Telegram channel**. Fully unattended. | skills `daily-fintech` **[3]**, `fintech-news-digest`; `publish_telegraph.py`; telegra.ph + Telegram Bot API |
| **Researcher bot** | DM the bot a company/theme → semantic search (news + IR) + web → a full **1-pager** as a telegra.ph article. **Quick** mode (DB + web) or **deep** mode (vendor plugin agents). | `pipeline/research/research_bot.py`; skill `researcher` + plugins; telegra.ph + Telegram |

---

## Infrastructure
- **Orchestration:** GitHub Actions — 4 workflows: `ingest-enrich` (every 5 h), `publish` (daily),
  `research` (event-driven), `ir-refresh` (monthly). Idempotent + resumable.
- **Compute:** a **self-hosted runner on Fly.io** → **0 GitHub Actions minutes** (only the LLM *inference*
  runs in Anthropic's cloud; the agent loop + tools run on the runner). Setup in [`fly-runner/`](fly-runner/).
- **Instant research:** a tiny always-on Fly webhook ([`fly-webhook/`](fly-webhook/)) turns a Telegram
  message into an immediate run — no poll lag.
- **AI:** Claude Code (`claude -p`) on a **Claude Max** subscription — no per-token API billing.
- **Storage:** git for code + state; **GitHub Releases** for the (large) search indexes; **Google Drive**
  for raw IR documents.

---

## Setup

**Prerequisites:** a GitHub repo (private is fine), a Claude Max subscription, an OpenRouter key (embeddings),
a mailbox for newsletters, a Telegram bot + channel; optional: Google Drive + rclone for IR.

1. **Fork / create your repo** from this template.
2. **Secrets & variables.** Copy `pipeline/.env.example` → `pipeline/.env` for local runs. For the cloud,
   set them in **GitHub → Settings → Secrets and variables → Actions**:

   | GitHub **Secrets** (sensitive) | GitHub **Variables** (config) |
   |---|---|
   | `CLAUDE_CODE_OAUTH_TOKEN` — `claude setup-token` | `IMAP_HOST`, `IMAP_FOLDER` |
   | `OPENROUTER_API_KEY` | `RCLONE_REMOTE` (e.g. `irdrive:`) |
   | `IMAP_USER`, `IMAP_PASS` (app password) | `IR_DUE_CAP` |
   | `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHANNEL` | `RESEARCH_ALLOWED_CHATS` (your chat id) |
   | `TELEGRAPH_TOKEN` (optional) | |
   | `RESEARCH_BOT_TOKEN` (optional) | |
   | `RCLONE_CONFIG` (optional, IR→Drive) | |

3. **Point workflows at your repo:** replace `YOUR_GH_OWNER/YOUR_REPO` in `.github/workflows/*` and
   `fly-*/` with your `owner/repo`.
4. **Compute:** deploy the self-hosted runner — see [`fly-runner/README.md`](fly-runner/README.md). (Or delete
   `runs-on: [self-hosted, fly]` → `ubuntu-latest` to use GitHub-hosted runners and pay per minute.)
5. **First index:** the workflows restore the search index from a GitHub Release; the first `ingest-enrich`
   run builds and uploads it. IR: seed `pipeline/ir/registry/` (see its README) and run `ir-refresh`.
6. **Instant research bot (optional):** [`fly-webhook/README.md`](fly-webhook/README.md).

---

## Reuse it for your domain
The pattern is **domain-independent**. To retarget it (say, biotech, defense, a competitor set):
- **Sources** → point `mail_ingest` at your newsletters, list your Telegram channels in `tg_ingest`, and put
  your entities in `pipeline/ir/registry/` (or drop IR entirely).
- **Tags & framing** → edit the tag vocabulary and the `[0]–[4]` enrichment prompts in
  `.claude/skills/daily-fintech/` and the digest style in `.claude/skills/fintech-news-digest/`.
- **Take one piece or all** — the modules are independent: **collectors** · **semantic index**
  (`pipeline/semsearch/`) · **enrichment skill** · **digest formatter** · **researcher bot**.
- Everything else — the index, dedup, scheduling, publishing, cost model — stays the same.

**Cost:** a Claude Max subscription + ~\$20/mo for the always-on Fly compute. No per-token API bills.

---

## Repo layout
```
pipeline/            collectors, dedup, indexing, IR, publishing, researcher (Python)
  semsearch/         hybrid LanceDB search (the reusable index)
  ir/                investor-relations: discover / download / index / Drive mirror
  research/          the Telegram researcher bot
.claude/skills/      the AI logic: daily-fintech [1][2][3], fintech-news-digest, researcher, ir-discovery
.github/workflows/   the 4 scheduled workflows
fly-runner/          self-hosted CI runner on Fly (0 GitHub minutes)
fly-webhook/         instant-response Telegram webhook on Fly
```

> Built with [Claude Code](https://claude.com/claude-code). Runtime data (notes, digests, raw emails,
> indexes) is gitignored — this template ships the **process**, not one operator's data.
