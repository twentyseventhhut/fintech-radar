---
title: "Chile's CMF launches ATENA open-finance sandbox with IDB"
date: 2026-10-07
retrieved: 2026-10-08
tags:
  - company/cmf
  - company/idb
  - industry/open-banking
  - industry/regtech
  - region/latam
  - type/regulation
sources:
  - https://www.cmfchile.cl/portal/principal/623/w4-article-113974.html
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sf6e612e7
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Chile's CMF launches ATENA open-finance sandbox with IDB

> [!info] 2026-10-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] 🇨🇱CMF, Chile's financial market regulator, launched ATENA with the IDB, a technology sandbox where institutions can test integrations before joining Chile's Open Finance System.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.cmfchile.cl/portal/principal/623/w4-article-113974.html>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Chile's CMF launches ATENA open-finance sandbox with IDB
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Chile's regulator **CMF (Comisión para el Mercado Financiero)** presented **ATENA** — *Ambiente Tecnológico de Experimentación y Nuevas Aplicaciones* — on **2026-09-30** (press release art. 113897); the 2026-10-07 beat (art. 113974, the note's source) is the **"now available, go use it"** availability milestone, not a first reveal. ATENA is an **isolated test/staging sandbox with fictitious (mock) data** that mirrors the future production environment of Chile's **Open Finance System (SFA, Sistema de Finanzas Abiertas)**. Institutions use it to (a) verify conformance to CMF technical standards (NCG 514 as amended by **NCG 569**), (b) run interoperability tests against the future **Participant Directory**, and (c) validate developments/business models early. **Participation is voluntary.**

De-PR'd reality — two things the PR frame hides:
- **Chile did not build this.** ATENA is Chile's national instance of the **IDB's "APIBox"** — an open-source regional open-finance sandbox built by **Minsait/Indra**, co-financed under the IDB's **BIDPago** program with support from Luxembourg, unveiled by the IDB on **2025-06-11** at FinnLAC. Chile is the **first** country to deploy APIBox. So the engineering novelty is the IDB's, not CMF's; "launches with IDB" = adopting an off-the-shelf regional public good. → Why it matters: the real story is the IDB's standardization play across LatAm, with Chile as pilot adopter.
- **The system it serves isn't live.** The SFA production start is **2027-07-03**, already slipped a full year from the original July 2026 target after industry pushback (see [[Chile's CMF weighs extending fintech law open finance deadline]], 2025-10). ATENA is therefore a ~9-month pre-season warm-up for a regime that doesn't operate for another ~9 months. → Second order: a sandbox launch is a signal of *progress on a delayed timeline*, not of open finance going live.

## [1] Competitors / peers (other LatAm open-finance regimes)
- **Brazil (Open Finance Brasil)** — the benchmark: regulator-mandated (BCB), 4 phases complete, **live since 2021**, **800+ institutions**, **~125M active consents (2026)** — world #1 by consents. Already minting new participant classes (ITPs — see [[Klavi, Trio and WePayOut approved as Brazil ITPs]], 2025-10). Chile is **years behind** on both time and traction (0 live participants pre-2027).
- **Mexico (Ley Fintech 2018)** — law-first but **stalled**: the secondary rules for aggregated/transactional data were never issued (years overdue). Chile has deliberately avoided Mexico's fate by prescribing a single standard.
- **Colombia** — mandatory via Decree 0368/2026 (April 2026); the nearest mandatory peer to compare standards against.
- **Chile's position:** regulated / single prescribed standard (REST + OpenAPI + mTLS + ISO 20022), like Brazil rather than Mexico's market-led drift — but behind Brazil by years and having slipped its own deadline. Its one distinguishing move: buying standardization off-the-shelf from the IDB instead of building bespoke. → Why: a small market can't justify Brazil-scale bespoke infra, so leasing the IDB's shared rails is the rational (cheaper, interoperable) path.

## [2] Company/regulator history & fit
CMF created the SFA under **Ley Fintech 21.521 (enacted Jan 2023)** with a ~24-month mandate pointing at July 2026. Technical regulation **NCG 514** came July 2024; by Nov 2025 CMF opened a consultation to delay; **NCG 569 (2026-06-01)** formally pushed the start to **2027-07-03**, extended data history to 24 months, set a 5-minute data-serving latency rule, added a "simplified participation" regime for entities with **<50,000 clients**, and formalized the pilot/sandbox. Leadership changed mid-rollout: Catherine Tornel became CMF president in March 2026 (see [[Chile's CMF names Catherine Tornel as new president]]). ATENA fits logically as the implementation tooling CMF owed the industry after granting the delay — a concession that lets institutions prepare while the clock runs to 2027.

## [3] Novelty / value-add / traction
What's genuinely new: a **live, usable test harness** (vs the earlier abstract rule-making) — institutions can actually integrate and conformance-test now. What's NOT new: the underlying tech (IDB APIBox, a year old) and the SFA itself (not live till 2027). **Traction is unmeasured**: CMF discloses **no count** of institutions using ATENA (piloted with "industry representatives" in H1 2026, voluntary). No real-world interoperability or the 5-minute latency rule is proven until production. → Where value is captured: the IDB captures regional influence/standardization (co-owns the sandbox, reusable code); Chile's institutions get a cheaper on-ramp; the margin/value question ("who runs the rails") only becomes real at 2027 go-live.

## [4] What's next / sentiment
- **2026 → early 2027:** voluntary ATENA testing, updated versions, Participant Directory dry-runs.
- **2027-07-03:** SFA enters force; phased API obligations begin (banks/card issuers first, then cooperatives/insurers/fund managers over a 20–30-month tail).
- **Regional:** watch other APIBox adopters — the IDB positions it as a reusable public good; Colombia (Decree 0368/2026) is the nearest mandatory peer.
- **Risk:** the 2026→2027 slip already happened once; a second slip is plausible (open). Consent-rule ambiguity in NCG 569 is a live debate.

## Sources
- Primary: CMF art. 113974 (note source); CMF press release art. 113897 (2026-09-30).
- IDB APIBox announcement (2025-06-11); IDB publication "APIBox: A Technology Sandbox for Open Finance" (Nov 2025).
- NCG 569 (2026-06-01); df.cl on the 2026→2027 delay; Cuatrecasas/Carey/Fiskil advisories.
- Brazil/Colombia/Mexico comparisons: tiinside, Fiskil tracker, EBANX, OpenBankingTracker, Latinia LatAm 2026 map.
- Internal priors: [[Chile's CMF weighs extending fintech law open finance deadline]], [[Chile's CMF names Catherine Tornel as new president]], [[Klavi, Trio and WePayOut approved as Brazil ITPs]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is ATENA live and usable, or vaporware?** Launched 2026-09-30, available for voluntary testing from Oct; piloted with industry in H1 2026. Appears genuinely available, though CMF flagged a "new version" to come — maturity partly open.
2. **Does it use real customer data?** No — fictitious/mock data in an isolated environment mirroring production. Confirmed.
3. **Did Chile build this?** No. It's a national instance of the IDB's APIBox (built by Minsait/Indra, BIDPago-financed, Luxembourg-supported). Low original engineering content. Confirmed.
4. **Is the SFA itself live?** No — 2027-07-03, already slipped from July 2026. Confirmed.
5. **How many institutions are actually testing in ATENA?** Open — no count published.
6. **What did the IDB cooperation cost / who paid?** Open — "co-financed by BID," no dollar figure disclosed.
7. **Is ATENA mandatory?** No — voluntary prep tool. Confirmed.
8. **Is "first to implement APIBox" substance or marketing?** Both — genuinely first adopter, but APIBox is built for multi-country reuse, so "first" is time-ordering, not exclusivity.
9. **Single prescribed API standard or market-led?** Prescribed single standard (REST/OpenAPI/mTLS/ISO 20022). Confirmed.
10. **How far behind Brazil is Chile?** Years — Brazil live since 2021, 800+ institutions, ~125M consents; Chile 0 live pre-2027. Confirmed.
11. **Could July 2027 slip again?** Open — already slipped once after industry pushback; a second slip is plausible but unconfirmed.
12. **Is the 2026-10-07 beat new vs the 2026-09-30 launch?** Largely the same event — Oct is the availability/consent-rules follow-on, not a second launch. So the item is a FRESH event (new tool now usable) but a thin, incremental one.
13. **Any consent/security controversy?** NCG 569 reworked consent rules (tech-neutral evidence, dropped mandatory hash); advisories flag terminological ambiguity. Live debate — partly open.
14. **Does ATENA guarantee interoperability at go-live?** No — it tests conformance to standards + the Participant Directory, but real-world interoperability and the 5-minute latency rule are unproven until production. Open.
15. **Does APIBox lock Chile into Minsait/Indra or the IDB?** Open — code is described as open-source and co-owned (cuts against lock-in), but operational dependency on the IDB stack is a real question.

Importance: 2/5 — Regulatory plumbing, not a market event. A pre-production test harness for a system that isn't live until July 2027, built on an off-the-shelf year-old IDB tool, with no disclosed participant count or budget. Nudged above 1 because Chile is the first APIBox adopter (regional replication signal) and it marks concrete progress on a previously delayed open-finance timeline; well short of 3 given zero traction and no original novelty.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Open finance infrastructure/regtech in LatAm — a regulator-driven data-sharing regime, not a company round. ATENA (Ambiente Tecnológico de Experimentación y Nuevas Aplicaciones) is a CMF+IDB testing sandbox launched 30 Sep 2026 (per CMF prensa; the digest item is dated 2026-10-07, i.e. a few days after the primary launch), letting institutions verify technical-standard compliance, run interoperability tests against the Participants Directory, and manage digital credentials before joining Chile's Open Finance System (SFA). "Why now": the SFA — established by Ley Fintech No. 21,521 (2023) — had its entry into force pushed from the original July 2026 to **July 2027** (CMF amendment published 2 Jun 2026, Annex No. 3 + Developers' Portal), with progressive rollout through 2029 (per Latinia/CMF). Size/growth: no clean Chile open-finance TAM — "no data"; the broader LatAm fintech market is cited at ~$17.5bn (2026) → ~$54bn (2034), ~15% CAGR per IMARC [UNSOURCED beyond secondary market-research PR, treat as directional]. Structure: regulation-gated, network-effects business (value accrues once a critical mass of banks + fintechs connect); the sandbox lowers the integration/compliance entry barrier (analysis).

**Competitive landscape.** The relevant "KPIs" here are regime-level, not corporate: # participating institutions, # active consents, API call volume, and time-to-go-live. Benchmark against the regional frontier — **Brazil** (BCB): 800+ institutions, 100m+ customers, ~128m active consents (Jan 2026), world's most engaged open-finance ecosystem; full open finance since Apr 2024 (per BCB/thepaypers). **Colombia** moved open finance to mandatory for banks (2026-05, [[Colombia makes open finance mandatory for banks]]). **Mexico** is the laggard — passed LatAm's first open-banking law (2018) but transactional-layer secondary rules still unpublished in 2026, with an amparo filed against CNBV (per FintechFutures/OpenBankingTracker). Chile sits mid-pack: law done, technical annex done, but live system still ~9 months out. Basis of competition for data-aggregator vendors (Belvo, Prometeo, Klavi): local bank-coverage breadth and reliability. Chile's position: catching up to Brazil/Colombia, ahead of Mexico; moat is regulatory infrastructure (the CMF Directory itself), not a private firm (analysis).

**Comps & multiples.** No valuation/round/financials attach to CMF or IDB (public bodies) → trading multiples not applicable, "no data". Comparison is qualitative, across regional open-finance regimes and the in-base precedent trail:
- [[Chile's CMF weighs extending fintech law open finance deadline]] (2025-10) — the deadline-slip that this launch now operationalizes; direct prior chapter.
- [[Colombia makes open finance mandatory for banks]] (2026-05) — mandatory-for-banks model, a stricter path than Chile's.
- [[Belvo and Banco Plata launch open finance credit in Mexico]] (2026-05) — commercial use-case (real-time income verification + direct debit) that a working directory enables downstream.
- [[Klavi, Trio and WePayOut approved as Brazil ITPs]] (2025-10) — Brazil's participant-licensing mechanics (ITP), the mature-market analogue of ATENA onboarding.

**Risk flags.**
1. **Slippage risk / execution** — the July 2026 → July 2027 postponement is already the second signal of timeline pressure (the 2025-10 "weighs extending" note foreshadowed it); a sandbox launch is "test-ready," not "system live," and progressive rollout runs to 2029 — adoption could lag the headline date.
2. **Low initial network value** — open finance is a two-sided network; a directory with few connected institutions delivers little until banks AND fintechs onboard at scale, so early-phase economics are thin (cf. Mexico's 8-year stall despite having a law first).
3. **Donor-dependency / sustainability** — build co-financed by the IDB; a one-off externally-funded launch leaves open questions on who funds ongoing operation, API maintenance and incident liability once the grant ends (no disclosure — [UNSOURCED]).

**What this changes (idea-lens).** Incremental, not a re-rating: ATENA de-risks the technical onboarding path and makes the July 2027 go-live more credible, improving the setup for LatAm aggregators (Belvo, Prometeo) and Chilean fintechs to monetize once live (analysis). Falsifiable thesis: if, by mid-2027, a meaningful count of banks has certified through ATENA and the SFA launches on time, Chile converges toward the Brazil/Colombia tier; trigger to watch — CMF's published participant-certification numbers. What breaks it — a third deadline extension past July 2027, which would signal Chile is drifting toward Mexico's stalled trajectory.

Sources: https://www.cmfchile.cl/portal/prensa/625/w4-article-113897.html · https://www.cmfchile.cl/portal/principal/623/w4-article-110883.html · https://latinia.com/en/resources/open-finance-in-latam-regulatory-map-2026 · https://www.bcb.gov.br/en/pressdetail/2462/nota · https://www.fintechfutures.com/regulatory-actions/mexico-s-cnbv-reportedly-facing-legal-action-over-delays-publishing-open-finance-rules · https://www.imarcgroup.com/latin-america-fintech-market

_IR grounding: no ir_latest.json entry for company/cmf or company/idb (both public bodies) — IR step skipped._
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
