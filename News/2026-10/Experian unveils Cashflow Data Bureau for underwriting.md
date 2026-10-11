---
title: "Experian unveils Cashflow Data Bureau for underwriting"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - company/experian
  - industry/credit
  - industry/lending
  - region/us
  - type/product
sources:
  - https://www.businesswire.com/news/home/20261006880188/en/Experian-Unveils-Cashflow-Data-Bureau-to-Power-the-Next-Generation-of-Underwriting
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s4057bff8
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Experian unveils Cashflow Data Bureau for underwriting

> [!info] 2026-10-08 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Experian unveils Cashflow Data Bureau to power the next generation of underwriting. The new bureau gives lenders access to cash flow data to support credit decisions and strengthen underwriting. It brings together transaction-level cash flow data to give lenders a clearer view of a borrower’s financial health and repayment capacity.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261006880188/en/Experian-Unveils-Cashflow-Data-Bureau-to-Power-the-Next-Generation-of-Underwriting>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Experian unveils Cashflow Data Bureau for underwriting
_Analytical notes (not a post). Importance: 3/5. Freshness: fresh — a NEW structural move (standing up a separate FCRA consumer reporting agency), not a reprint of Experian's 2025 Plaid cash-flow tie-ups ([[Plaid and Experian partner on cash flow underwriting]], [[Experian and Plaid team up on open banking credit decisions]])._

## [0] What exactly happened (de-PR'd)
On **2026-10-06**, at Experian's annual **Vision** conference (San Antonio), Experian unveiled **Experian Cashflow Data Bureau, Inc.** — a **separate, FCRA-regulated consumer reporting agency (CRA)** that turns consumer-permissioned bank-account data (transactions, balances, payroll deposits, digital-wallet activity) into standardized consumer reports lenders can use in underwriting. Exec quote: Jeff Softley, President/CEO Experian North America, frames it as "making it easier for our clients to adopt these insights with confidence and at scale."

**The real "what": this is a legal/structural move, not a new data product.** Experian already *sold* cash-flow inputs — **Cashflow Attributes** and a **Cashflow Score** — and has been running Plaid-powered open-banking credit decisions since mid-2025 ([[Experian and Plaid team up on open banking credit decisions]], 2025-06). What's genuinely new is wrapping that capability into a **standalone CRA entity** that bundles consent management, data aggregation, standardized reporting and analytics under one FCRA roof.

**Why structured this way (the core red-team point):** a CRA is a *regulatory status*, not a technology. By standing up a distinct FCRA bureau, Experian (a) gives lenders FCRA-governed cash-flow **reports** (dispute rights, adverse-action, permissible-purpose plumbing) that de-risk adoption vs. raw aggregator feeds, and (b) positions cash-flow data as a **second bureau rail** it owns — the same "own the regulated reporting layer" play Nova Credit built its whole identity on (a CRA with alt-data). It is a defensive/offensive answer to Plaid moving up-stack into scoring ([[Plaid unveils LendScore Arc transformer credit model]]).

**De-PR'd on the numbers — all Experian-internal, no independent validation, flattering baselines:**
- **"up to 40% lift in predictive performance"** — only *when cash-flow is paired WITH credit data* (i.e. vs bureau-alone; a favorable baseline). This is the **same ~40% figure** Experian already cited for its Nov-2025 "Credit + Cashflow Score" — so the metric is recycled, reinforcing that the data capability is not new.
- **"raise approvals by up to 25% without changing risk tolerance"** — vendor-claimed, no named lender, no live-portfolio loss data.
- Market framing: "~1 in 5 consumers lack access to / have damaged credit"; "60% of denied consumers believe cash-flow would have changed the outcome" — a demand narrative, not adoption.
**Zero named lender customers. US-only (FCRA / North America). Announced, not demonstrably live at scale.**

## [1] Competitors / peers
- **Plaid** — simultaneously Experian's **data partner AND competitor** (pymnts states this explicitly). Plaid just shipped LendScore/LendScore Arc, a rival standalone cash-flow score via its own CRA ([[Plaid unveils LendScore Arc transformer credit model]], 2026-10). Experian depends on Plaid-type pipes for the raw data yet competes with Plaid's score.
- **Nova Credit** — the clearest structural comp: an alt-data **Consumer Reporting Agency** running Cash Atlas cash-flow underwriting; Chase/PayPal/Yardi wins, $35M Series D ([[Nova Credit raises $35M Series D for cash-flow underwriting]], 2025-10). Experian is essentially doing "Nova Credit, but with the incumbent bureau's distribution."
- **FICO (+ Plaid)** — UltraFICO folds cash-flow into the score; "79% of non-prime applicants see higher scores" ([[FICO and Plaid launch UltraFICO Score adding cashflow data]], [[FICO partners with Plaid on cash flow score]]).
- **Mastercard/Finicity, Prism Data, MX** — aggregators/analytics also named as competitors.
- **Position:** catching up on *concept* (cash-flow underwriting is now table stakes — FICO, Plaid, Nova all shipped in 2025-26), but **ahead on distribution and regulatory packaging** (incumbent bureau already wired into most US lenders' stacks + an FCRA entity).

**Why the landscape is this way (2nd order):** everyone agrees bureau-only data is incomplete for ~1-in-5 thin/damaged files; the fight has moved from "is cash-flow useful" to **"who owns the FCRA-regulated reporting layer for it."** Aggregators (Plaid) have the pipes; Nova built a greenfield CRA; FICO owns the score. Experian is the only player that owns the **incumbent bureau + distribution + brand trust with lenders**, and is now bolting on the regulated cash-flow rail — its structural advantage is channel, not technology.

## [2] Company history / fit
Experian's 2025-26 trajectory is a relentless pivot from static bureau to **data-and-decisioning platform**: Ascend platform + Agent OS ([[Experian launches Agent Operating System on Ascend platform]]), Plaid open-banking tie-ups (2025-06), UK score overhaul adding rental/behavioral data ([[Experian overhauls credit scoring, adds rental payments]], 2025-11), ChatGPT credit/loans apps, and a string of acquisitions (AtData, Konfir, Own Up, KYC360). The Cashflow Data Bureau fits this logic exactly.

**Why Experian acts this way (analysis):** the core bureau is a mature, regulated, low-growth annuity facing disintermediation from open banking — if lenders can pull cash-flow data direct from aggregators, the bureau's monopoly on "the file" erodes. Experian's defense is to **become the regulated reporting layer for the NEW data too**, so that the open-banking shift expands rather than cannibalizes its reporting franchise. Standing up a CRA is the cleanest way to capture that without contaminating the legacy bureau's compliance posture.

## [3] Novelty / value-add / traction
**Genuinely new:** the *structure* — a dedicated FCRA cash-flow bureau with consent/aggregation/reporting/analytics bundled — is a real packaging innovation that lowers lender adoption friction (FCRA cover, dispute/adverse-action plumbing, single vendor).
**NOT new:** the underlying capability. Experian has sold Cashflow Attributes/Score and run Plaid-powered cash-flow decisions since 2025; the 40% lift figure is recycled from the Nov-2025 Credit+Cashflow Score. So this is **repackaging + regulatory wrapper**, not a new analytical breakthrough.
**Traction = none proven.** No named lenders, no live approval/loss data; all figures internal. "Announced," not "adopted at scale."

**Who captures the margin (analysis):** value-add is real only if lenders actually underwrite on Experian's cash-flow *report* rather than cheaper raw aggregator feeds. Experian's leverage is the **existing bureau integration** (already in the underwriting stack) + FCRA trust — a real moat vs. a greenfield CRA like Nova. The risk: cash-flow data is increasingly commoditized (every aggregator has it), so the durable margin sits in the **regulated reporting/compliance layer and the score**, not the data. The central question is less "is cash-flow predictive" (settled: yes, ~40% paired lift) than **"can Experian defend a premium for being the FCRA bureau-of-record for cash-flow when Plaid/Nova/FICO are all racing for the same rail."**

## [4] What's next / market sentiment
Watch for: (1) named Tier-1 lender adoption with disclosed live performance (the only thing that converts this from announcement to fact); (2) how the Plaid relationship evolves — partner vs. competitor tension sharpens as both sell standalone cash-flow scores; (3) GSE/regulatory tailwinds (FICO 10T, VantageScore 4.0 legitimizing bank-statement data) that broaden the TAM.

**Regulatory backdrop / risk:** cash-flow underwriting lives under FCRA + ECOA/Reg B (adverse-action, disparate-impact on "approve more subprime" segments) and the CFPB §1033 open-banking rule (whose fate under the current administration is contested) — the entire premise depends on durable consumer-permissioned data access.

**Counterintuitive 2nd order:** the FCRA-bureau wrapper is both Experian's moat and its tell — standing up a *separate* entity signals the legacy bureau's own monopoly on "the file" is eroding, and that cash-flow is becoming a parallel, contestable rail where the incumbent must re-earn its position rather than inherit it.

## Sources
- https://www.businesswire.com/news/home/20261006880188/en/Experian-Unveils-Cashflow-Data-Bureau-to-Power-the-Next-Generation-of-Underwriting (primary PR)
- https://www.pymnts.com/loans/2026/experian-launches-new-credit-reporting-agency-to-deliver-cash-flow-insights/ (competitors: Plaid partner+competitor, Prism Data, Mastercard/Finicity, Nova Credit)
- https://finovate.com/experian-unveils-new-consumer-reporting-agency-for-cashflow-underwriting/ (built on existing Cashflow Attributes/Score; Softley quote)
- https://receivablesinfo.com/2026/10/08/experian-launches-cashflow-data-bureau/ (FCRA structure)
- Internal corpus: [[Plaid and Experian partner on cash flow underwriting]], [[Experian and Plaid team up on open banking credit decisions]], [[Nova Credit raises $35M Series D for cash-flow underwriting]], [[FICO and Plaid launch UltraFICO Score adding cashflow data]], [[FICO partners with Plaid on cash flow score]], [[Plaid unveils LendScore Arc transformer credit model]], [[Experian overhauls credit scoring, adds rental payments]], [[Experian launches Agent Operating System on Ascend platform]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this actually new, or a reprint of Experian's 2025 cash-flow moves?** New *structure* (a standalone FCRA CRA entity) but the capability is old — Experian has sold Cashflow Attributes/Score and run Plaid cash-flow decisions since mid-2025 ([[Experian and Plaid team up on open banking credit decisions]]). **(answered: fresh as an entity, recycled as a capability.)**
2. **Is the "40% predictive lift" a new finding?** No — it is the SAME ~40% paired-with-credit figure Experian cited for its Nov-2025 Credit+Cashflow Score. Recycled. **(answered.)**
3. **Vs what baseline is the 40% / 25%?** 40% = cash-flow *paired with* credit data vs bureau-alone (flattering baseline); 25% approval lift "without changing risk tolerance" — vendor-claimed. **(answered.)**
4. **Any independent validation of any number?** None. 100% Experian-internal, no live-portfolio loss data. **(open/unverified.)**
5. **Named lender customers?** None disclosed in any source. "Announced," not "adopted." **(open.)**
6. **Is it live at scale or just unveiled at a conference?** Unveiled at Vision 2026-10-06; no evidence of scaled live deployment. **(open.)**
7. **Why a SEPARATE CRA rather than a feature of the core bureau?** FCRA status is a regulatory wrapper — gives lenders dispute/adverse-action/permissible-purpose plumbing and keeps the legacy bureau's compliance posture clean; also stakes a claim to a second reporting rail. **(answered: analysis.)**
8. **How does this differ from Experian's core bureau?** Core bureau = tradeline/payment history; this = consumer-permissioned bank-transaction/income/cash-flow data under a distinct FCRA entity. **(answered.)**
9. **US or UK?** US-only (FCRA / North America framing, Softley = Experian North America). Distinct from the UK score overhaul ([[Experian overhauls credit scoring, adds rental payments]]). **(answered.)**
10. **Who is the closest structural competitor?** Nova Credit — an alt-data CRA running cash-flow underwriting (Cash Atlas) ([[Nova Credit raises $35M Series D for cash-flow underwriting]]). Experian = "Nova Credit with incumbent distribution." **(answered.)**
11. **The Plaid paradox — partner or competitor?** Both (pymnts states explicitly): Experian relies on Plaid-type pipes for raw data yet competes with Plaid's own standalone LendScore/Arc ([[Plaid unveils LendScore Arc transformer credit model]]). Channel conflict sharpens as both sell cash-flow scores. **(open — strategic tension.)**
12. **Does cash-flow underwriting even work?** Consensus yes (FICO's "79% of non-prime see higher scores"; broad analyst agreement) — so the novelty is NOT "does it work" but "who owns the regulated rail." **(answered: concept settled.)**
13. **Who captures the margin?** Data is commoditizing (every aggregator has it); durable margin sits in the FCRA reporting/compliance layer + the score. Experian's edge is existing bureau integration, not the data itself. **(analysis.)**
14. **What breaks the thesis?** (a) lenders pull cheaper raw aggregator feeds instead of Experian's report; (b) §1033 open-banking access tightens, choking the data supply; (c) ECOA/fair-lending scrutiny of "approve more subprime." **(analysis.)**
15. **Is it a duplicate of an existing note?** No — the 2025 notes are partnerships/products; this is the first note on a standalone FCRA bureau entity. Fresh. **(answered.)**

**Importance: 3/5** — A strategically meaningful incumbent move: Experian standing up a regulated cash-flow bureau is the clearest signal yet that open banking is turning cash-flow data into a contestable second reporting rail, and it directly answers Plaid/Nova/FICO's 2025-26 pushes. But capped at 3: the underlying capability and the headline 40% figure are recycled from 2025, there are zero named adopters and no live performance data, every number is vendor-internal, and the hardest questions (Plaid channel conflict, margin capture, §1033 durability) are unresolved. A structurally important repackaging, not a proven new product.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-11]] (2026-10-11).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: alternative / cash-flow credit data inside the US credit-bureau stack. Market size: per Mordor Intelligence, the alternative credit-scoring market is ~$4.22bn in 2026 growing at a ~21.3% CAGR to ~$11.07bn by 2031; cash-flow and bank-transaction data was the single largest data source at ~31.4% share in 2025 (via mordorintelligence.com, as of 2026). Structure: the core US bureau layer is a consolidated oligopoly (Experian / Equifax / TransUnion), with high entry barriers (data scale, FCRA regulation, lender integrations); the cash-flow layer on top is more contested, with data aggregators (Plaid), specialist CRAs (Nova Credit) and scoring vendors (FICO) all entering. "Why now": lenders are pushing to score the ~20% of US consumers who are thin-/no-file (per Experian launch coverage via pymnts.com / americanbanker.com, Oct 2026), and consumer-permissioned open-banking rails have made transaction data cheap to collect — Experian is moving the cash-flow signal from a partner-sourced add-on into a standalone, FCRA-regulated bureau it owns.

**Competitive landscape.** Sector KPIs: organic revenue growth, segment revenue mix (consumer vs B2B), benchmark EBIT margin; for the cash-flow layer specifically — data coverage/aggregator count and FCRA-compliant report status. Experian's own economics (PRIMARY, FY26 YE 31 Mar 2026): group organic revenue growth 8% (9% in Q4), benchmark EBIT margin +90bps at constant currency; North America revenue US$5,587m (~66% of ~$8.45bn group TTM revenue), NA organic growth 10% led by B2B, group B2B organic growth 8% "supported by strong performance across alternative data" (Experian FY26 FY results announcement, 2026-05-20, https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/Experian-fy26-fy-results-announcement.pdf). Key players & moves: Plaid + FICO launched a cash-flow UltraFICO Score (2025-11-20); Nova Credit raised a $35M Series D (2025-10) and runs Cash Atlas as a CRA with Chase/PayPal/Yardi; Plaid operates the largest US consumer-permissioned bank-data network. Protagonist position: Experian is catching up on the product but ahead on distribution — it already partnered with Plaid on cash-flow underwriting (2025-06) and now verticalises by standing up its own FCRA-regulated CRA ("Experian Cashflow Data Bureau Inc.", announced 2026-10-06 at Vision 2026). Moat (analysis): scale + existing lender integrations + regulatory/data-handling intangibles; the new entity bundles cash-flow reports with Experian's incumbent bureau sell, a switching-cost/distribution edge pure-play aggregators lack.

**Comps & multiples.** Listed bureau peers (via companiesmarketcap / multiples.vc / macrotrends, as of 2026):
- Experian (EXPN.L): market cap ~$30.84bn, TTM revenue ~$8.45bn → P/S = 30.84 / 8.45 = ~3.6x (a separate source cites PS ~3.9x). In-line-to-rich on revenue, consistent with highest growth (8% organic) and best scale of the three.
- Equifax (EFX): market cap ~$16bn, revenue ~$6.6bn → P/S = 16 / 6.6 = ~2.4x (source cites ~3.3x EV/Rev — gap = net debt in EV); EBITDA ~$2.1bn → implied EV/EBITDA ~10.5x.
- TransUnion (TRU): market cap ~$15.1bn; EV/Revenue ~3.4x LTM, EV/EBITDA ~9.6x LTM, P/E ~19.75x.
Distribution (3 comps, EV/Rev ~3.3–3.9x; EV/EBITDA ~9.6–10.5x): bureau multiples cluster tightly and sit mid-range vs the EV/Rev ~0.5–20x guide — no outlier; Experian sits at the top on both growth and multiple, which is justified by its faster organic growth, not a red flag. Internal comps: [[Nova Credit raises $35M Series D for cash-flow underwriting]] (private, $35M round, not post-money — valuation "no data"), [[Plaid and Experian partner on cash flow underwriting]], [[Experian and Plaid team up on open banking credit decisions]]. EV/EBITDA and P/E for Experian itself not computed here (clean EV / consensus EPS not free-sourced) → [UNSOURCED].

**Risk flags.**
1. Disintermediation / rail dependence: the cash-flow signal originates from consumer-permissioned bank data largely carried by aggregators (Plaid). If Experian relies on third-party rails for the raw feed, margin and the data relationship can be captured upstream — second-order: owning the FCRA "report" layer is only durable if Experian also controls connectivity.
2. Regulatory/FCRA execution: a brand-new CRA entity ("Experian Cashflow Data Bureau Inc.") inherits full FCRA dispute/accuracy liability; cash-flow categorisation errors feed directly into adverse credit decisions — litigation/CFPB exposure if accuracy claims aren't met. De-PR note: launch is "announced/unveiled" (Oct 2026), not yet evidenced by adopted lender volumes.
3. Crowded, commoditising layer: Plaid+FICO (UltraFICO), Nova Credit (Cash Atlas), plus Equifax/TransUnion are all building the same cash-flow capability — risk the feature becomes table-stakes and compresses pricing before it adds segment-level revenue (B2B is only part of NA's ~$5.6bn; alternative data is one driver among many).

**What this changes (idea-lens).** (analysis) This is a verticalisation / land-grab move, not a re-rating: Experian is converting a partner-dependent cash-flow add-on into an owned, regulated product line, racing Plaid+FICO and Nova Credit for the thin-file ~20% of consumers. Falsifiable thesis: if cash-flow underwriting becomes a durable share-shift, it shows up as accelerating NA B2B "alternative data" revenue in FY27 disclosures; trigger to watch — named lender adoptions of the Cashflow Data Bureau (as Nova Credit secured Chase/PayPal/Yardi) and whether Experian internalises data connectivity vs staying dependent on Plaid. Thesis breaks if the bureau stays a partner-sourced wrapper with no disclosed volume uplift.

Sources: https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/Experian-fy26-fy-results-announcement.pdf · https://www.pymnts.com/loans/2026/experian-launches-new-credit-reporting-agency-to-deliver-cash-flow-insights/ · https://www.americanbanker.com/news/how-experian-scores-thin-file-borrowers-with-cash-flow-data · https://www.mordorintelligence.com/industry-reports/alternative-credit-scoring-market · https://multiples.vc/public-comps/equifax-valuation-multiples · https://companiesmarketcap.com/experian/marketcap/ · https://finovate.com/experian-unveils-new-consumer-reporting-agency-for-cashflow-underwriting/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings backdrop for a product launch (not an earnings item). The Cashflow Data Bureau is a B2B/Data-and-Decisioning product; the relevant financial read is Experian's North America B2B and decisioning/analytics momentum. Latest reported results: **FY26 full-year** (year ended 31 Mar 2026, released 20 May 2026) + **Q1 FY27 trading update** (three months ended 30 Jun 2026, released 16 Jul 2026). No earnings are reported in the news itself.

**Verdict (headline read).** Latest full print = **BEAT / record year.** FY26 revenue **US$8.425bn (+13% actual, +11% cc, +8% organic)**, Benchmark EBIT **US$2,407m, margin 28.6% (+50bps actual)**, Benchmark EPS **179.8c (+15%)** — at the upper end of guidance; new **US$1.0bn buyback**, dividend 69.25c (+11%). North America (~67% of group) grew **+10% organic** in FY26, the single biggest engine the Cashflow Bureau plugs into. Most recent data point (Q1 FY27, 16 Jul 2026): group +7% organic, decelerating but with **B2B +9% organic** still carrying growth.

**Key figures — FY26 (year ended 31 Mar 2026).**
- Total revenue (ongoing): **US$8.425bn**, +13% actual / +11% constant / **+8% organic** (quarterly organic 8/9/8/9%).
- Benchmark EBIT (ongoing): **US$2,407m**, +15% actual; margin **28.6%**, +50bps actual / +60bps cc / +90bps organic — operating leverage ahead of guidance.
- Benchmark EPS: **179.8c, +15%** actual (vs 156.9c FY25); +13% cc.
- Benchmark operating cash flow **US$2.2bn**, **93% cash conversion**; ROCE **17.2%**; dividend **69.25c (+11%)**; **US$1.0bn share buyback** (through 30 Jun 2027).

**By segment / driver — FY26 organic growth.**
- **By region:** North America **+10%**, Latin America +8%, EMEA & Asia Pacific +5%, UK & Ireland +2%. North America is the growth leader and ~2/3 of revenue.
- **By business line:** B2B **+8%** organic — explicitly driven by alternative data, mortgage, fraud prevention and analytics; Consumer Services **+9%** organic (215m free members globally). The Cashflow Data Bureau sits squarely in the B2B / Data-and-Decisioning stack (alternative/transaction data for underwriting).

**Most recent data point — Q1 FY27 (3 months ended 30 Jun 2026, released 16 Jul 2026).**
- Group revenue +10% actual / +8% cc / **+7% organic** (vs +8% organic FY26 — a step down).
- **North America +7% organic, ~67% of group.** Within it, **B2B strong at +11% organic**; NA Consumer Services -2% (data-breach contract wind-down; +3% ex-those).
- Other regions: Latin America +12%, UK&I +5%, EMEA/AP +1%.
- **B2B (group) +9% organic, 73% of revenue** — Financial Services +9%, Verticals +7%; Consumer Services +2%. Ascend analytics / Ascend Platform cited as growth drivers.
- Full-year guidance reaffirmed (below).

**vs expectations / prior period.** FY26 landed at the **top of the guidance range** and ahead on margin/EPS; CEO Brian Cassin called it "a record year … performance at the upper end of our expectations." FY27 organic guidance midpoint (~7%) was flagged by Goldman Sachs as "a touch below consensus" (~8%), but guidance mechanically implied "limited changes to consensus EPS"; shares rose +4.2% on the FY26 print. No corpus history for Experian (semsearch DOWN — OpenRouter 402; no prior Experian note found). Trajectory from the base's own IR index: organic 8% FY26 → 7% Q1 FY27 = modest deceleration off a very strong FY26, with B2B the resilient leg.

**Guidance / forward (FY27, year ending 31 Mar 2027).** **Organic revenue growth 6–8%** (total 8–11% actual); margin expansion "at the higher end of the Medium-Term Framework"; management guided to "another year of double-digit Benchmark EPS growth." Guidance **reaffirmed at Q1 FY27** (16 Jul 2026, "expectations unchanged"). Tone: confident; emphasis on data breadth, decisioning/analytics (Ascend) and North America B2B. What they stay quieter on: the NA Consumer Services drag from data-breach contract roll-off, and that the FY27 organic midpoint sits just under consensus.

**Thesis-flags (tying the Cashflow Data Bureau to data/decisioning growth).**
1. **The Bureau feeds the fastest, highest-quality growth leg.** NA B2B ran **+11% organic in Q1 FY27** vs +7% for NA overall — B2B is what's holding group growth up as Consumer Services softens. A new transaction-level cash-flow dataset directly extends B2B's "alternative data + analytics" driver that management already credits for FY26's +8% B2B. Second-order: it deepens the data moat (proprietary cash-flow signals → stickier decisioning/Ascend attach), supporting the margin-expansion thesis (28.6%, +90bps organic in FY26).
2. **Alternative/cash-flow data is an explicit, management-named growth lever — not a side bet.** FY26 B2B growth was attributed to "alternative data, mortgage, fraud prevention and analytics"; a Cashflow Bureau operationalises the alternative-data piece at scale. Why it matters: it converts a cyclical (mortgage/credit-volume-sensitive) bureau into a thicker-information, higher-value underwriting layer — more defensible organic growth inside the 6–8% framework.
3. **Offsets the deceleration flagged at Q1 FY27.** Group organic slipped 8%→7% and the FY27 midpoint sits just below consensus; new data products in the core NA B2B engine are exactly the type of launch that can defend the top of the 6–8% range. Watch whether cash-flow/Open-Banking-style data shows up as a named driver in H1 FY27 results (expected ~Nov 2026).
4. **Competitive read.** Equifax and TransUnion are pushing the same cash-flow/alternative-data-for-underwriting narrative; a branded "Bureau" framing is Experian's land-grab for the category — a share-of-decisioning play, not incremental reported revenue yet (no figures disclosed for the product; "announced, not yet live/adopted at scale").

Sources: FY26 full-year results, year ended 31 Mar 2026, released 20 May 2026 — experianplc.com press release (https://www.experianplc.com/newsroom/press-releases/2026/full-year-results-fy26) and results announcement PDF (https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/Experian-FY26-FY-results-announcement.pdf) · FY26 figures/buyback/analyst reaction via Investing.com (https://www.investing.com/news/earnings/experian-tops-fy26-forecasts-sets-new-1-bln-share-buyback-4700269) · Q1 FY27 trading update, 3 months ended 30 Jun 2026, released 16 Jul 2026 — Investegate RNS (https://www.investegate.co.uk/announcement/rns/experian--expn/trading-update-first-quarter/9671274) and experianplc.com (https://www.experianplc.com/newsroom/press-releases/2026/trading-update--first-quarter-fy27) · IR index: pipeline/ir/ir_latest.json["experian"] · corpus semsearch DOWN (OpenRouter 402) — no prior Experian note in base.
<!-- /enrichment:earnings_review -->
