---
title: "Linas Newsletter: Plaid's AI sees what no single bank can"
date: 2026-06-28
retrieved: 2026-06-28
tags:
  - company/plaid
  - company/stripe
  - industry/ai
  - industry/open-banking
  - region/us
  - type/commentary
sources:
  - https://substack.com/app-link/post
  - https://substack.com/redirect/76bc4091-f9a5-4b08-95fa-2e42f959de9b
  - https://substack.com/redirect/80150e40-81a1-4ebb-9da7-44b2e8c83133
status: enriched
n_mentions: 2
channels:
  - "Linas Newsletter"
story_id: s084ae393
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# Linas Newsletter: Plaid's AI sees what no single bank can

> [!info] 2026-06-28 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Linas Newsletter

## Агрегированный текст (из дайджестов)

[Linas Newsletter] Plaid’s AI now sees what no single bank can 👀🏦; Santander just open-sourced its AI governance stack. No other major bank has 🤖🏦; Meta wants to clone Polymarket & Kalshi 🤷‍♂️🏦

[Linas Newsletter] Zoom out 🔎 Of course, Plaid isn’t alone here. Stripe trained its Payments Foundation Model on tens of billions of transactions and claims a 64% cut in card-testing fraud. Revolut’s PRAGMA, trained on up to 40 billion events from ~26 million users, reported a 130% lift in credit-scoring precision. Nubank built nuFormer on 100 billion+ transactions across 100 million+ customers.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/app-link/post>
- <https://substack.com/redirect/76bc4091-f9a5-4b08-95fa-2e42f959de9b>
- <https://substack.com/redirect/80150e40-81a1-4ebb-9da7-44b2e8c83133>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 3/5. This is a Linas Newsletter thesis essay, not a discrete event — enrich as a themed read and de-hype the vendor framing._

## [0] What exactly happened (de-PR'd)
Not an event — a Linas Newsletter commentary built on Plaid's own slogan "Plaid's AI now sees what no single bank can," tied to its Effects 2026 product push (see [[Plaid unveils AI financial intelligence tools at Effects 2026]], 2026-05-22). The essay's correct insight: Plaid's edge is **cross-institution breadth** — one fintech sees only its own fraud/return history, Plaid sees the same identity/account across thousands of apps (the genuine logic behind Beacon and Signal). 
**But the tagline inverts the actual power balance (analysis).** "No single bank can" is true only for breadth, not depth: JPMorgan sees every transaction in its own accounts in full fidelity; Plaid sees a permissioned, bank-mediated snapshot. → The biggest banks have deeper data AND, since late 2025, control the pipe and now charge for it. So the vendor frame ("Plaid's AI is uniquely all-seeing") is half marketing — the data is bank-owned, contestable, and increasingly metered.
Linas's own "Zoom out" already de-hypes it: Plaid is one of many running network-scale transaction models — Stripe's Payments Foundation Model (tens of billions of txns, claimed 64% card-testing-fraud cut), Revolut PRAGMA (~40B events / 26M users), Nubank nuFormer (100B+ txns / 100M+ customers). Network-scale ML is table stakes, not a Plaid moat.

## [1] Competitors / peers
- **MX, Yodlee (Envestnet), Finicity (Mastercard, acq. 2020):** direct aggregators. Finicity is the dangerous one — owned by a network giant, competes squarely on cash-flow underwriting (Plaid's CRA / Lendscore turf) and can bundle data + card rails.
- **Akoya (bank-owned: Fidelity + ~11 banks incl. JPMorgan, BofA, Capital One, Citi, Wells):** the strategic threat — banks push fintechs onto Akoya; Wells/PNC actively steering away from Plaid (per CNBC, 2025-11-14).
- **Stripe Financial Connections / Trustly (A2A) / MoneyLion:** narrower, bundled or payments-led.
**+ Why this lay of the land matters (analysis):** the two most dangerous rivals are not independents — they're **Mastercard (Finicity)** and **the banks themselves (Akoya)**, both controlling either distribution or the data source Plaid depends on. The "AI story" peers (Stripe/Revolut/Nubank from Linas's own text) show the model is replicable; the moat question is data access, not algorithms.

## [2] Company history / fit
Trajectory fits logically: account-linking utility (2010s) → since 2022 a deliberate climb up the value stack to escape commodity API pricing. Cognito acq. (~$250M, Jan 2022) → IDV; Signal GA (Nov 2022, ML ACH-return scoring, cited ~$1.5B/month protected); Beacon (Jun 2023, fraud consortium); Plaid Check CRA → Consumer Report (Jun 2024, FCRA cash-flow underwriting); Layer (2024 onboarding); Plaid Protect / Trust Index (2025). Corpus confirms the partnership flywheel: Experian ([[Experian and Plaid team up on open banking credit decisions]]), FICO UltraFICO ([[FICO partners with Plaid on cash flow score]]), Truist data-access ([[Plaid and Truist announce open banking data-access agreement]]), Protect launch ([[Plaid introduces Plaid Protect anti-fraud engine]]).
**+ Why (analysis):** commodity account-linking take-rate → needs a software/AI multiple → hence the relentless expansion into fraud, identity, underwriting. The AI-network narrative is structurally required to justify the valuation, which is itself a reason to discount it.

## [3] Novelty / value-add / traction
What's genuinely real: cross-institution fraud visibility (Beacon/Signal) is something no single fintech replicates; scale is real (12,000+ institutions, 7,000+ customers, ~half of US bank-account holders linked at least once, ~750k connections/day). 
What's overstated: (1) **Beacon's consortium is shallow** — disclosed members are a handful of fintechs/credit unions, not top-10 banks, so the largest fraud-relevant institutions sit outside the network. (2) **Efficacy stats are first-party and undated** — "47% more fraud caught," "25% better predictive performance," "+25% conversion" are unaudited marketing claims. (3) **Live vs announced is murky** — Effects 2026 models, Lendscore (LS1), Layer Extended Autofill: paid GA-at-scale vs beta is undisclosed.
**+ Who captures the margin (analysis):** the moat rests on data Plaid does **not own and now must pay for**. The Sep 2025 JPMorgan settlement converted a previously-free input into a recurring per-pull cost — banks captured pricing leverage over the very signal feeding Plaid's AI. → The central question shifts from "does Plaid have an AI story" to "does the network's value exceed its now-metered data-access cost, or does the bank capture the surplus?"

## [4] What's next / market sentiment
Financials (corpus-confirmed): $575M raise at $6.1B (Apr 2025, down ~55% from $13.4B 2021 peak); ARR climbed ~40% to >$500M ([[Plaid ARR climbs 40% to over $500m as IPO weighed]]); $8B employee tender Feb 2026 ([[Plaid completes tender offer at $8 billion valuation]], still ~40% below peak). No S-1 filed; IPO "on our path." Note both 2025 and 2026 rounds were **secondary/tender (employee liquidity), not primary growth capital** — a delayed public-market test, not expansion funding.
Regulatory backdrop is the key risk: CFPB Section 1033 (effective Jan 2025) was gutted in 2025 — the CFPB asked the court to vacate its own rule (May 2025), enforcement enjoined (Oct 2025, Judge Reeves), now under rewrite that may explicitly **bless bank data-access fees**. The free-mandated-access tailwind Plaid counted on is becoming a headwind. JPMorgan signed fee deals covering >95% of its data pulls by Nov 2025 ([[JPMorgan says fintech middlemen overload its systems]]).
**+ Counterintuitive second-order (analysis):** the more Plaid leans on the "AI sees what no bank can" pitch, the more it advertises a dependency on bank-controlled data — strengthening banks' incentive to meter, price, or route fintechs to bank-owned Akoya. Capital/data concentration makes the network fragile at the access layer, not safe.

## Sources
Internal: [[Plaid unveils AI financial intelligence tools at Effects 2026]], [[Plaid introduces Plaid Protect anti-fraud engine]], [[Experian and Plaid team up on open banking credit decisions]], [[FICO partners with Plaid on cash flow score]], [[Plaid and Truist announce open banking data-access agreement]], [[JPMorgan says fintech middlemen overload its systems]], [[Plaid ARR climbs 40% to over $500m as IPO weighed]], [[Plaid completes tender offer at $8 billion valuation]]
External:
- https://plaid.com/blog/fall-release-25/ , https://plaid.com/blog/2025-year-in-review/ , https://plaid.com/blog/plaid-signal-unlock-ach/ , https://plaid.com/blog/introducing-plaid-check-cra-consumer-report/ , https://plaid.com/blog/ten-years-plaid-link/
- https://www.cnbc.com/2025/04/03/plaid-raises-575-million-funding-round-at-6-billion-valuation.html , https://techcrunch.com/2026/02/26/plaid-valued-at-8b-in-employee-share-sale/ , https://sacra.com/c/plaid/
- https://www.cnbc.com/2025/07/28/jpmorgan-fintech-middlemen-plaid-data-requests-taxing-systems.html , https://www.pymnts.com/data/2025/plaid-and-jpmorgan-reach-customer-data-sharing-agreement/ , https://www.cnbc.com/2025/11/14/jpmorgan-chase-fintech-fees.html
- https://www.openbankingtracker.com/guides/section-1033-status , https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration
- https://www.americanbanker.com/payments/news/plaid-leans-on-banks-fintechs-to-create-a-stolen-identity-database , https://www.fintegrationfs.com/post/plaid-vs-mx-vs-finicity-which-us-open-banking-api-should-you-integrate
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions (second-order; each answered from sources or marked open):**

1. **Margin pass-through:** What does the Sep-2025 JPMorgan fee deal actually cost Plaid per data pull, and can it pass that to customers? — *Open; terms undisclosed. The entire thesis hinges on a number Plaid won't reveal.*
2. **Who captures the surplus:** If banks now charge for data AND want Plaid's fraud signals, does the network's value exceed its data-access cost, or does the bank capture it? — *Open; structurally the leverage has shifted to banks.*
3. **Beacon depth:** How many institutions feed Beacon, and do any top-10 banks participate? — *Disclosed members are a handful of fintechs/credit unions; big banks largely absent → consortium shallower than framed.*
4. **Efficacy validation:** Are "47% more fraud," "25% better predictive," "+25% conversion" independently audited? — *No; all first-party, undated, undisclosed methodology. Treat as marketing.*
5. **Live vs announced:** Which Effects-2026 / Lendscore / Layer Extended Autofill products are paid GA-at-scale vs beta, and what revenue does each contribute? — *Open; not disclosed.*
6. **Akoya substitution:** If Wells/PNC route fintechs to bank-owned Akoya, how much of Plaid's coverage is structurally at risk? — *Open; directional risk confirmed (CNBC 2025-11-14).*
7. **Mastercard/Finicity threat:** Can a network owner undercut Plaid on cash-flow underwriting by bundling data + card rails? — *Plausible; Finicity is Mastercard-owned and on the same turf.*
8. **CFPB 1033 rewrite:** Will the revised rule permit data-provider fees? — *Open; rule enjoined Oct 2025, ANPR reopened the fee question — likely tailwind for banks, headwind for Plaid.*
9. **Customer concentration:** What share of revenue rides on a few large customers (Coinbase, Robinhood, Venmo-type apps) that could in-source or switch aggregators? — *Open.*
10. **Privacy/FCRA exposure:** Does the expanded CRA + fraud-database footprint raise new litigation risk (cf. the $58M 2021–22 privacy settlement)? — *Open; plausible given broader data handling.*
11. **Cross-sell reality:** Is the "network → AI cross-sell" flywheel showing in net revenue retention, or is growth still mostly core Link? — *Open; ARR +40% to >$500M reported but mix undisclosed.*
12. **IPO signal:** Why two consecutive secondary/tender rounds (2025, 2026) instead of a primary raise — confidence or a delayed public-market test? — *Reads as morale/retention management while delaying a public test.*
13. **Low-value polling:** JPMorgan said ~87% of pulls were non-customer-initiated background refreshes — how much of Plaid's "network" is low-value polling banks will now meter or block? — *Material; this is the bank's core complaint and the metering rationale.*
14. **AI commoditization:** If foundation models + the FDX standard commoditize enrichment/categorization, what's left of the data-cleaning moat? — *Open; Linas's own peer list (Stripe/Revolut/Nubank) shows network-scale ML is widespread.*
15. **Bank-as-competitor:** As banks build permissioned-data + fraud-scoring on data they own in full fidelity, why does a fintech need Plaid's mediated snapshot? — *Cross-institution breadth is the only durable answer; depth and price favor the bank.*

**Importance: 3/5** — A well-argued thesis essay on a genuinely important structural question (cross-institution data-network advantage), anchored to a real, traction-bearing incumbent and a live regulatory/commercial fight (JPMorgan fees, CFPB 1033). Not higher because: it's commentary, not a discrete new event; the headline claim is half vendor framing that the essay's own "zoom out" partly dismantles (network-scale ML is table stakes — Stripe/Revolut/Nubank); and the de-hyped reality (banks own and now price the data) cuts against the bullish frame. Fresh as an analytical read — no prior note packages this specific "AI sees what no bank can" thesis with the de-hype angle.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Open-banking / financial-data networks. Market size estimates are vendor-research and dispersed: per Precedence Research (via web), global open banking ~$35.7bn (2025) → ~$43bn (2026), ~21% CAGR to ~$240bn by 2035 — treat as order-of-magnitude only, these third-party TAMs are not independently verifiable. Structure: consolidating at the aggregator layer — of the three large US data aggregators, two are now owned (Visa attempted Plaid in 2020, blocked; Mastercard bought Finicity for $825M in 2020, per ffnews/Banking Dive), leaving Plaid and MX as the main independent/quasi-independent players. Barriers are network effects + bank-connection coverage + permissioned-data scale, not capital. "Why now": the moat is shifting from *connectivity* (commoditizing) to *intelligence* — Plaid, Stripe, Revolut and Nubank are each training transaction foundation models on network-scale data, so the defensibility argument moves to proprietary cross-bank data that no single institution holds (analysis).

**Competitive landscape.** Sector KPIs: bank-connection coverage, accounts/consumers reached, % of revenue from newer products (payments/anti-fraud/credit), ARR growth. Per Plaid IR/press: >1 in 2 US bank-account holders have used Plaid; newer lines (payments, anti-fraud, underwriting) now >20% of ARR; full-year 2025 adjusted-EBITDA profitable (per web/Sacra/getlatka). Key players & basis of competition: Plaid (independent, developer distribution), MX (~$1.9bn valuation, bank-side aggregation, per Tracxn), Mastercard-Finicity and Visa (rails incumbents bundling data), plus vertically-integrated data-model owners (Stripe Payments Foundation Model, Revolut PRAGMA, Nubank nuFormer) who do NOT sell the model — they keep it in-house, which is a competitive *threat* to a data-network selling-to-third-parties model. Recent dated moves: Plaid Effects 2026 (2026-05-21) launched a transaction foundation model claiming +26.5% return-value caught at fixed 1% ACH action rate and 13.6% lower default risk at 70% approval (per Plaid blog effects-2026-recap — vendor self-report, un-audited); FICO+Plaid cash-flow UltraFICO (2025-11-20); Plaid–Truist data-access deal (2026-03-16); JPMorgan–Plaid paid data-access agreement (2025-09-15). Position: leader on the independent-aggregator axis, *catching up* as a model vendor vs in-house builders. Moat: network effects + cross-bank data breadth ("sees what no single bank can"); durability `[UNSOURCED]` — depends on whether banks keep granting access at viable prices.

**Comps & multiples.** Private; multiples are round-valuation (post-money), NOT market cap.
- Plaid: ~$8.0bn valuation (Feb-2026 secondary, per TechCrunch/Sacra) ÷ ~$546M ARR (2025, +40% YoY per Sacra) = **14.6x EV/ARR**. Prior round: $6.1bn (Apr-2025) ÷ ~$390M (2024) ≈ 15.6x — i.e. valuation re-rated UP but ARR multiple roughly flat/slightly compressed; both well below the $13.4bn 2021 peak (per Cobalt/TechCrunch).
- MX: ~$1.9bn valuation (per Tracxn) — ARR not public, multiple = no data.
- Mastercard/Finicity: $825M acquisition (2020, +up to $160M earn-out) — pre-AI-era, not a clean current comp.
- Internal comps: [[Plaid and Truist announce open banking data-access agreement]], [[Plaid agrees to pay JPMorgan for data access]], [[FICO partners with Plaid on cash flow score]], [[Plaid unveils AI financial intelligence tools at Effects 2026]].
Flag: ~15x ARR is rich in absolute terms but in-line/justifiable for ~40% growth + EBITDA-positive (analysis); distribution not computed — only one clean revenue-multiple comp available, so qualitative comparison.

**Risk flags.**
1. **Data-access pricing / dependence on someone else's rails.** Plaid pays JPMorgan for data (2025-09) and JPM publicly called aggregators a system load — banks can raise data costs or throttle access, compressing the very margin the AI story rests on. Second-order: if access economics worsen, the foundation-model edge degrades as coverage thins.
2. **Regulatory whiplash on 1033.** The CFPB Section 1033 open-banking rule is currently *enjoined and being rewritten* (not vacated) as of mid-2026, with fee/data-security provisions reopened (per Cozen/Cooley). Removal of a free statutory data-access right shifts leverage to banks and legitimizes per-request fees — directly negative for aggregators.
3. **Disintermediation by in-house model owners.** Stripe/Revolut/Nubank build comparable models on their own data and keep them captive; large customers may internalize rather than buy Plaid's intelligence layer, capping the >20%-of-ARR new-product flywheel.

**What this changes (idea-lens).** Thesis (analysis): the open-banking moat is migrating from connectivity to proprietary cross-bank *intelligence*, and Plaid is best-positioned among independents to sell that as a layer — re-rating, not new entry. Falsifiable: watch whether the next funding/IPO mark holds ≥15x ARR AND whether bank data-access fees stay flat; the thesis breaks if a major bank materially raises data pricing or 1033's rewrite hands banks fee/throttling power, or if a flagship customer publicly swaps Plaid's model for an in-house one.

Sources: https://techcrunch.com/2025/04/03/fintech-plaid-raises-575m-at-6-1b-valuation-says-it-will-not-go-public-in-2025/ · https://sacra.com/c/plaid/ · https://plaid.com/blog/effects-2026-recap/ · https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration · https://www.consumerfinancemonitor.com/2025/06/05/cfpb-states-the-section-1033-open-banking-rule-exceeds-its-authority/ · https://tracxn.com/d/companies/mx/__8OA-JNy34P3z6jCWbHiU0_EtlxcGR33OimAOM129Ppw · https://ffnews.com/newsarticle/mastercard-acquires-finicity-for-825-million-to-advance-in-open-banking/ · https://www.precedenceresearch.com/open-banking-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!warning] Private company — no public earnings release. This is a private-market financial-signals read (last funding/tender valuation, disclosed revenue growth, profitability commentary) as backdrop to the AI/open-banking news. Plaid files no audited income statement; hard P&L line items are not in the public domain → marked [UNSOURCED] where so.

**Verdict (private-market read).** No earnings print — but the freshest hard signal is a step-UP: Plaid completed a secondary tender at an **$8.0bn valuation on 2026-02-26, +31% vs the $6.1bn April-2025 round** (still ~40% below the 2021 peak of $13.4bn). Management framed the markup on "momentum from the past year" and "increasing relevance in the age of AI" — directly the angle of this Linas note. Direction: improving, AI-led; this is a liquidity event for employees, not a primary growth-capital raise.

**Key figures (with growth).**
- **Valuation:** $8.0bn (2026-02-26 tender) vs $6.1bn (2025-04-03 Series E) = +31%; peak $13.4bn (2021), so still ~−40% from peak. Total lifetime funding ~$1.3bn across 6 rounds.
- **April-2025 round:** ~$575M led by Franklin Templeton (with Fidelity, NEA, Ribbit), proceeds for RSU-conversion tax withholding + employee liquidity — not growth capex.
- **Revenue growth (last disclosed by management):** ">25% YoY in 2024", described as a "record-setting year on revenue." Plaid does not publish a revenue figure; third-party estimates (Sacra) put 2024 ARR ~$390M and 2025 ARR ~$546M (+40%) — both **(third-party estimate, not company-disclosed)**, treat as directional only.
- **Profitability:** management cited a "return to positive operating margins" (2024) and approaching "sustained profitability"; third-party reporting flags adjusted-EBITDA profitability in 2025 — **(unverified, no audited figure)** [UNSOURCED on the actual margin %].

**By segment / driver.** Growth narrative is the de-PR'd substance behind this note: AI customers made up **20% of newly onboarded customers** in the year preceding the Feb-2026 tender — Plaid positioning its network as data infrastructure for AI agents (Effects 2026, Guaranteed Payments with up-to-90% approval rates). Underlying franchise: ">1 in 2 Americans have used Plaid"; product expansion across Anti-Fraud, Alternative Credit Data, Bank Payments saw "record adoption" (2024/2025 shareholder letters). No segment revenue split is disclosed.

**vs expectations / prior period.** No consensus exists (private). vs prior round: valuation +31% in ~10 months reverses the 2021→2025 down-round trajectory — a positive inflection, though still a secondary (employee liquidity), so it does not inject primary growth capital and is a softer signal than a priced primary raise. Internal trend across the IR corpus is consistent: record adoption + margin recovery 2023→2025 (cf. [[2025-shareholder-letter]], [[2024-shareholder-letter]], [[2025-year-in-review]]).

**Guidance / forward.** None given (private; no guidance regime). Management explicitly said it **will not IPO in 2025**; the rising-valuation + tender pattern reads as staying-private-longer optionality (peers Stripe ~$159bn, Anthropic $350bn+ cited as comps). Independent read (analysis): if the ">25%" 2024 growth and AI-onboarding momentum hold, the $8bn mark looks defensible-to-conservative on a software-infra multiple, but the absence of a disclosed revenue base means any multiple claim is unverifiable.

**Thesis-flags.**
1. **AI-led re-rating (+31%) is the signal, not a number-beat.** Fact: $6.1bn→$8.0bn on "AI relevance" + 20% of new logos = AI firms. Why it matters: validates the note's thesis that Plaid's cross-bank data network is becoming AI training/inference infrastructure (vs Stripe/Revolut/Nubank in-house models). Second-order: data-network breadth ("what no single bank can see") is the moat AI rivals with single-institution data cannot replicate.
2. **Liquidity event ≠ growth inflection (de-PR).** Both 2025 and 2026 events are secondaries/tenders for employee liquidity; Plaid is quiet on absolute revenue, gross margin %, and net-revenue retention. Markup is real but it is not a primary raise — calibrate enthusiasm.
3. **Still ~40% below 2021 peak.** The $8bn mark is a recovery, not a new high; the IPO is explicitly off the table near-term — duration risk for any holder.

Sources: $8bn tender (2026-02-26, +31% vs $6.1bn, peak $13.4bn, 20% AI new-logos): https://news.crunchbase.com/fintech/plaid-completes-tender-offer-8b-valuation/ · April-2025 ~$575M / $6.1bn / Franklin Templeton, ">25%" 2024 growth, "positive operating margins", no-IPO-2025: https://techcrunch.com/2025/04/03/fintech-plaid-raises-575m-at-6-1b-valuation-says-it-will-not-go-public-in-2025/ · https://plaid.com/blog/our-latest-fundraise/ (drive: https://drive.google.com/file/d/1uxJ7wNzVgwvtCUyrKs1b132RgxaE4kvB/view) · revenue/ARR estimates (third-party, unverified): https://sacra.com/c/plaid/ · IR corpus: [[2025-shareholder-letter]] (https://drive.google.com/file/d/1gDZVVbBKve-zY5UusvR4NLZsy-LtTYAF/view), [[2024-shareholder-letter]] (https://drive.google.com/file/d/191AN9VObvvAaM94i7oTbsekmNiCO8w9U/view), [[2025-year-in-review]] (https://drive.google.com/file/d/1tF5pGDc1weTlCg_D9_eOQL_-4WIvOLQ0/view), Effects 2026 recap (https://drive.google.com/file/d/1dzkr5nhpAau8r8CD4WG3kKnBnJQjnIou/view) · No audited P&L; absolute revenue, gross margin %, EBITDA $ = no data / [UNSOURCED].
<!-- /enrichment:earnings_review -->
