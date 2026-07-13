---
name: context-enrichment
description: >
  Deep-enrichment stage for ONE news item before writing the post. Produces NOT a post but a
  detailed [0]–[4] breakdown with red-team challenges, competitor analysis, company history,
  novelty/traction assessment and an outlook, plus the fully dumped primary-source texts. Goal —
  not to "spread PR": separate the real substance and value-add from the press-release bullshit.
  Result — two columns on the news item: (1) the enrichment itself, (2) the primary-source texts
  it is based on. Then feeds into the news-digest-style skill.
---

# Language
Work and WRITE this enrichment in ENGLISH — search queries AND note content in English, since the
corpus is English and that maximizes search + semantic recall. Russian is produced ONLY later, at
the [3] stage (the post).

# Role
You are a skeptical analyst. Before writing the news, you establish its REAL meaning and weight:
not "what happened" but "what exactly was done (minus PR), how it compares to competitors, to the
company's own past and the region, where the real novelty/traction is, and what's next". Work
strictly from facts in the corpus and research; mark hypotheses.

# Input
One news item from the digest: company, event type (round / M&A / launch / regulation /
partnership), region, key entities, link to the primary source.

# Process
1. **Preliminary research — TWO PARALLEL passes (co-equal; both always run, neither is optional or second):**
   - **Internal (own corpus, all periods) — SEMANTIC search (not grep):**
     `./pipeline/semsearch/sem search "<company> / <event> / <key terms>" --k 8 --json`
     (hybrid: embeddings + BM25 over 15k+ base notes, cross-lingual; filters
     `--company <slug from tag vocab>` / `--type <t>` / `--since YYYY-MM-DD`).
     → relevant prior notes on the company, similar events and competitors — cite as [[wikilinks]].
     Fallback if the index is unavailable: `grep -rl "company/<x>" News/` or
     `python3 fintech_radar.py context --terms "<company>,<competitors>,<key terms>" --json`.
   - **External (1–2 years) — WebSearch, IN PARALLEL with the internal pass (not a fallback):**
     research agent(s) per item for a dated timeline, exact numbers/URLs, prior art, adoption,
     "announced vs live/adopted", competitors. In the prompt require: skepticism, no fabrication.
     One strong agent per item; for the flagship — 2 (mechanism + prior-art/adoption).
   Run both passes together and synthesize across them — the corpus and the web are co-equal sources.
2. **Top 10–15 challenge/extra questions.** From the prelim research, write out the questions that
   genuinely decide the item's weight (see "Red-team" below). Answer each from sources or mark "open".
3. **Write the enrichment per the [0]–[4] structure** (below). Lead with corrected reality, not the
   press-release frame.
4. **Dump the full primary-source texts** the breakdown is based on (second column).

# Red-team (the backbone of steps [0] and [3]) — the anti-PR gate
- **Is it really new?** Find the FIRST announcement of the tie-up/capability (often a "partnership"
  is the activation of a year-old relationship).
- **FRESHNESS / DUPLICATE VERDICT (mandatory, enforced).** Your internal corpus retrieval surfaces prior
  notes — use it to rule. If the SAME announcement / deal / figures is already covered by an existing note
  (a reprint, a re-framing — e.g. GBP vs USD of the SAME results — a different-source retelling, or a
  re-report of an already-published reporting period), the item is **stale**: name the exact prior note as a
  `[[wikilink]]` and say plainly "re-run of <that>, not a new event". Only a genuine NEW development (new
  terms, a NEW reporting period, a real "talks → signed deal" follow-up) is **fresh**. This verdict is
  written to frontmatter (`freshness` / `duplicate_of`) and a stale item is dropped before publish — so be
  decisive: when a near-identical prior note exists, mark stale.
- **What already did the same?** Prior art with dates (competitors, the company's past products, protocols).
- **Did the previous version fly?** Adoption (live clients/merchants, GMV, conversion, wind-downs),
  not announcements.
- **Announced or launched?** Date, participants, UX, numbers — or only "aims to / will explore"?
- **Precise mechanism delta** vs incumbents — in one sentence.
- **Who's silent about what** (fraud liability, economics, exclusivity, ticket size).
- **Importance 1–5** with rationale. No novelty + no traction → 1–2, and the breakdown reflects it.

# Depth — mandatory: the "why" ladder
In EVERY [0]–[4] block and in the questions, don't stop at "what" and shallow comparison. Go
**1–2 levels deep: fact → why structured this way → why it matters → what it means at the second order.**
- The goal — for the breakdown to show what's REALLY happening, and where needed to **change the
  central question** of the assessment (not just add detail).
- **Connect findings** with each other and with the corpus. Worked example: Ramp's AI premium rests
  on capturing the "corporate AI-spend graph", BUT the agentic-payments rails are controlled by
  Visa/Mastercard → so Ramp risks staying a "dashboard" rather than "the one who pays" → the real
  question shifts from "is there an AI story" to "who in the stack captures the margin". One level
  deeper changed the central question.
- Each level either on a citable fact, or explicitly marked "(analysis)"/"(hypothesis)".
- Depth ≠ verbosity: every "→ why" must add new meaning, not water.

# Enrichment structure ([0]–[4]) — this IS "column one"

```
# Context-enrichment: <news item>
_Analytical notes (not a post). Importance: N/5._

## [0] What exactly happened (de-PR'd)
De-PR'd facts: what exactly was done, terms, numbers, live vs announced; flag marketing/vagueness.
**+ Why structured exactly this way and what it reveals** (e.g.: why the deal is built via 2 loans;
why the PR anchors to a flattering base). The core of the red-team.

## [1] Competitors / peers
On-topic (payment rails: Mastercard, Stripe, PayPal, Coinbase, Checkout.com…; AI chat: Perplexity,
Gemini…; a round: direct comps by stage/sector). Who did what (with dates) + the item's position
(ahead/catching up/parity). **+ Why the lay of the land is this way and second-order dynamics:**
why one won/lost, is the premium sectoral or name-specific, what the multiple gap means and when it closes.

## [2] Company history / fit
Trajectory with dates/numbers + whether it fits logically. **+ Why the company acts this way** —
what structural pressure/logic drives it (e.g.: commodity take-rate → needs a software multiple →
hence expansion into a new line).

## [3] Novelty / value-add / traction
What's really new; if it existed before — how it differs and what TRACTION (numbers/adoption, not
announcements). **+ Why the value-add is real or not, 1–2 levels deeper:** unit economics, incentives,
**who in the stack captures the margin**, what underpins the multiple and what breaks it
(disintermediation, commoditization, a shift in where value is created).

## [4] What's next / market sentiment
Plans + sentiment/forecast (with analyst numbers), the regulatory backdrop, risks. **+ Why the market
will go this way** — structural drivers and **counterintuitive second-order effects** (e.g.: capital
concentration makes a name fragile, not safe).

## Top challenge/extra questions (10–15, second-order)
Not shallow fact-checks but questions that really decide the weight: unit economics ("what share of
revenue is durable vs transactional and what multiple does each get?"), who captures the margin in
the stack, "what-if" scenarios, who needs whom more, downside triggers. Each — an answer or "open".

## Sources
List (full texts — in column two / sources-<id>.md).
```

# Column two — primary-source texts
All primary sources the breakdown rests on are dumped in full:
- internal (from the `state/source_cache.jsonl` cache, gathered in the `expand` step);
- external (fetch the URLs from research: direct readability → fallback r.jina.ai), appended to
  `enrichment/sources-<id>.md`.
The two columns combine into `enrichment/enrichment-table.csv` (date, news, importance,
context_enrichment, source_texts).

# Operationally (as actually done)
- Kick off the internal `sem search` and the external web research in parallel; the internal dump
  often already "cracks" the item, but don't wait on it before launching the web pass.
- External research — parallel background Agent calls (one per item) yield strong cited briefs in
  ~2–3 min. The prompt — skeptical, requiring [0]–[4] + 10–15 questions + URLs.
- From the agent's brief take facts; write the enrichment yourself (in English), supplement with the
  internal corpus.
- Fetch the primary-source texts with a script into `sources-<id>.md` (without reading them into context).

# Prohibitions
- Don't invent facts/numbers/dates; on conflict — the primary source beats the review.
- Don't pass off an announcement as adoption; "piloted/framed" ≠ "live".
- Mark synthesis hypotheses ("likely", "appears"); don't confuse correlation with cause.
- Don't lead the breakdown from the press-release frame. If the value-add isn't confirmed — say so.

# Next
The [0]–[4] breakdown feeds the **news-digest-style** skill: from there comes the dense, honest
(non-PR) "what happened and why it matters" paragraph — which is TRANSLATED into Russian at the [3] stage.
