---
title: "Intesa Sanpaolo completes core IT migration to Google Cloud"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/intesa-sanpaolo
  - company/google-cloud
  - industry/banking
  - industry/infrastructure
  - region/europe
  - type/partnership
sources:
  - https://app.go.informamail01.com/e/er
status: published
n_mentions: 1
channels:
  - "FinTech Futures"
story_id: s1182577b
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# Intesa Sanpaolo completes core IT migration to Google Cloud

> [!info] 2026-07-03 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: FinTech Futures

## Агрегированный текст (из дайджестов)

[FinTech Futures] Intesa Sanpaolo completes core IT migration to Google Cloud

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://app.go.informamail01.com/e/er>

## Контекст

<!-- enrichment:context -->
### [0] What happened
On 2 July 2026, **Intesa Sanpaolo** (Italy's largest bank, ~€1.4tn customer assets) announced it has **completed the migration of its core IT systems to Google Cloud**, run jointly with **TIM (Telecom Italia)**. More than **800 applications** were moved to Google Cloud and an equal number of on-premise systems were decommissioned, "without major incidents." Workloads run in the two Italian Google Cloud regions (Turin and Milan) hosted inside **TIM's data centres**. The bank says this lays the foundation for **Isytech**, its cloud-native technology platform, and that it retired its legacy mainframe estate. Over 3,000 employees were trained, earning 170+ Google Cloud certifications.
Sources: [FinTech Futures](https://www.fintechfutures.com/cloud-services/intesa-sanpaolo-completes-core-it-migration-to-google-cloud) · [Finextra](https://www.finextra.com/newsarticle/48033/intesa-sanpaolo-migrates-core-it-systems-to-google-cloud-infrastructure) · [Intesa press release](https://group.intesasanpaolo.com/en/newsroom/press-releases/2026/07/intesa-sanpaolo-cloud-core-banking) · [PR Newswire](http://www.prnewswire.com/news-releases/intesa-sanpaolo-brings-its-digital-infrastructure-to-google-cloud-regions-in-italy-hosted-in-tims-data-centers-302816342.html)

### [1] Prior art / timeline
- **21 May 2020** — MoU signed between Intesa Sanpaolo, TIM and Google Cloud.
- **December 2020** — final agreements signed to migrate a large part of the bank's information system to Google Cloud, hosted in TIM's Milan and Turin data centres. [Intesa 2020 release](https://group.intesasanpaolo.com/en/newsroom/press-releases/2020/12/intesa-sanpaolo--tim-and-google-cloud-have-signed-final-agreemen)
- **2023** — Intesa launched **isybank**, a cloud-native digital bank built on **Thought Machine's Vault Core**, migrating millions of retail customers. isybank served as the proving ground / stress test for the cloud stack before the full core moved.
- **2 July 2026** — completion of the core IT migration announced (this story). The migration is framed as delivering the 2022–2025 plan and preparing the 2026–2029 business plan.

### [2] Scope / what actually moved
"Core IT" here = 800+ applications migrated plus 800 legacy systems decommissioned, including the retirement of legacy mainframe technology, over a multi-year program. The digital-bank workload (isybank) already sat on Thought Machine's cloud-native core; this milestone is about the *incumbent group's* core/back-office estate moving to Google Cloud IaaS/PaaS in TIM-hosted Italian regions, not a rip-and-replace of the core banking engine onto a new vendor core.

### [3] Related internal notes ([[wikilinks]])
- [[DXC and Thought Machine partner to accelerate banking modernization]] — explicitly names Intesa Sanpaolo as a Thought Machine Vault Core reference (basis of isybank).
- [[Swiss bank AMINA trials Google Cloud ledger for instant payments]] — another European bank running core-adjacent workloads on Google Cloud.
- [[Commerzbank and Macquarie adopt Google's Gemini Enterprise]] — Google Cloud landing more EU bank workloads.
- [[Akbank's German unit goes live on Mambu core]] — comparable European incumbent moving off legacy core to cloud-native.
- Company context: [[Intesa Sanpaolo launches €30.6B unsolicited bid for Monte dei Paschi]] (M&A, unrelated to IT but same entity).

### [4] Competitors / market context
Intesa joins a small set of European incumbents pursuing large-scale core-to-cloud migration: **Danske Bank, Lloyds, HSBC, Santander, BBVA**. **Deutsche Bank** has a ~10-year, ~$1bn Google Cloud deal and had ~260 apps moved to Google as of its earlier disclosures. Regulatory backdrop: EU **DORA** (in force since 17 Jan 2025) treats cloud as a supervised critical dependency but explicitly permits it. For Google Cloud, a fully-migrated incumbent of Intesa's size (Italy's #1 bank) is a marquee EU reference win; for TIM it monetises sovereign-cloud data-centre capacity.
Sources: [globalbankingandfinance.com](https://www.globalbankingandfinance.com/italys-intesa-shifts-core-banking-systems-googles-cloud/) · [Technobezz](https://www.technobezz.com/news/intesa-sanpaolo-migrates-over-800-applications-to-google-cloud-without-major-incidents) · [TechFinitive – Deutsche Bank](https://www.techfinitive.com/deutsche-banks-lifts-lid-on-cloud-progress-with-260-apps-moved-to-google/)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions

1. **Is this a real, dated milestone?** Yes — completion announced 2 July 2026, corroborated by Intesa's own press release, Finextra, FinTech Futures, Reuters-syndicated wires, and TIM. Not a plan or intent.
2. **Is "core IT migration" = new core banking engine?** No. It is migration of ~800 applications and decommissioning of legacy/mainframe onto Google Cloud IaaS/PaaS in TIM-hosted Italian regions. The cloud-native core (Thought Machine Vault Core) already runs isybank; this is the group's broader estate, not a core-vendor swap. Nuance flagged in [2].
3. **When did the program start?** MoU 21 May 2020; final agreements Dec 2020 — a ~5.5-year program. Not new news that it started; the *completion* is the news.
4. **Are the numbers verified?** "800+ applications migrated / 800 decommissioned," "3,000+ employees trained / 170+ certifications," "€1.4tn customer assets" appear consistently across Intesa's release and multiple outlets. Consistent, though single-sourced from the bank.
5. **Any downtime / incident claims to stress-test?** Bank claims "no major incidents." Unverifiable independently; treat as vendor/issuer claim, not audited fact.
6. **Is Google Cloud or TIM confirming?** Yes — joint announcement; TIM confirmed hosting in Turin/Milan data centres (Telecom Italia release on MarketScreener).
7. **Is it a duplicate of a prior note?** No prior note covers this completion. Closest internal notes are analogous migrations (DXC/Thought Machine naming Intesa, AMINA, Commerzbank, Akbank) — none is the same milestone. → fresh.
8. **Is isybank the same story?** No — isybank (2023, Thought Machine) is prior art/enabler, a distinct event. This 2026 milestone is the group core migration.
9. **Materiality to the market?** High signal: Italy's #1 bank fully migrating incumbent core off mainframe to public cloud is a rare EU proof point and a marquee Google Cloud/TIM reference.
10. **Vendor lock-in / concentration risk angle?** Real but not addressed in source; single-hyperscaler dependency under DORA scrutiny. Open.
11. **Cost / savings figures?** Bank references cost reduction but no hard € savings figure disclosed. Open.
12. **Sovereignty angle solid?** Yes — hosted in Italian regions inside TIM data centres, a deliberate data-sovereignty design. Well-supported.
13. **Competitor framing accurate?** Danske, Lloyds, HSBC, Santander, BBVA cited by wires as comparable; Deutsche Bank has separate ~$1bn Google deal. Directionally correct.
14. **Is the note's source link usable?** The note's own source is an obfuscated Informa mailer link; enrichment relies on named primary/secondary sources above instead. Fine.
15. **Any reason to downweight?** Slightly single-issuer sourced on the operational claims (no incidents, headcount), and "core IT" phrasing risks overstating a core-engine replacement. Otherwise strong.

**Importance: 4/5** — A rare, completed full-core cloud migration by Italy's largest bank (Google Cloud + TIM), a marquee EU reference and a concrete data point for the incumbent core-to-cloud trend; docked one point because it is a completion of a long-known 2020 program and the operational claims are issuer-sourced rather than independently verified.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-04]] (2026-07-04).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Bank core-banking cloud migration. Sizing (attribute carefully): the cloud *core-banking platform* market is a small, fast-growing slice — ~$1.6bn in 2025 → ~$1.9bn 2026, ~21% CAGR to ~$11bn by 2035 (per market.us, as of 2025); the broader retail-banking IT-spend market is ~$176bn in 2025 (per dataintelo, 2025). Treat these as vendor/analyst figures, not audited. Direction of travel is the real signal: Gartner cited as forecasting 90% of banking workloads cloud-based by 2030 (via numberanalytics, as of 2025) `[UNSOURCED — primary Gartner note not seen]`. Structure: consolidated on the hyperscaler layer (Google/AWS/Azure) but fragmented on the core-software layer (Thought Machine, Temenos, Mambu, Finacle, FIS/Fiserv). Value/barriers: for the *bank*, moving core is a multi-year, high-execution-risk programme (regulatory approval, data residency, no-downtime cutover) — barriers are execution and regulatory, not capital. Why now: legacy on-prem core reportedly eats ~64% of bank IT budgets (via numberanalytics, 2025), so migration is framed as freeing spend for product + AI; cloud spend is growing ~2.8x faster than overall bank IT budgets. Second-order: the migration is the pre-condition for AI/data-platform work (Intesa's "Isytech"), which is where the actual differentiation is claimed.

**Competitive landscape.** This is a *vendor-relationship + execution* story, not a product launch — the sector KPI that matters is migration scope/reliability, not TPV/take-rate. Key layers: (a) hyperscalers competing for bank core workloads — Google Cloud (Intesa, Deutsche Bank 2020, Commerzbank 2021), AWS (Experian [[Experian accelerates AWS migration to drive generative AI]]), Azure (Akbank/Mambu [[Akbank's German unit goes live on Mambu core]], Mibanco/Temenos [[Peru's Mibanco selects Temenos SaaS for core banking upgrade]]); (b) core-software vendors (Thought Machine — Intesa's isybank core; Temenos, Mambu, Finacle [[Infosys Finacle completes cloud migration for Uniting Financial]]). Basis of competition: reliability + local data-residency + skills/certification, not price. Recent dated moves: Intesa completion announced 2 Jul 2026 — >800 apps migrated, equal number decommissioned, "no major incidents", using Google Cloud Turin+Milan regions hosted in TIM data centres, 3,000+ staff trained / 170+ Google certs (per Intesa PR / Finextra, 2 Jul 2026). Intesa's position: *ahead of the European incumbent pack* on completeness — it de-risked via a greenfield cloud-native bank (isybank, live 2023 on Thought Machine) before migrating the legacy estate. Moat (analysis): the moat is Intesa's own switching-cost/execution capability, not a defensible tech asset — the underlying stack (Google + TIM + Thought Machine) is available to peers.

**Comps & multiples.** No deal value or migration cost was disclosed — trading multiples are not the right lens for an infra story, and no transaction economics exist to compute EV/Revenue etc. → "no data" for multiples. Relevant comparison is *peer core-cloud programmes* (scope/vendor/status):
- [[Akbank's German unit goes live on Mambu core]] — Mambu core on Azure, Germany, live (Feb 2026). Smaller scope (single unit).
- [[Peru's Mibanco selects Temenos SaaS for core banking upgrade]] — Temenos SaaS on Azure (Feb 2026). *Selected*, not complete.
- [[Infosys Finacle completes cloud migration for Uniting Financial]] — Finacle core migration complete (Aug 2025). Small institution.
- Deutsche Bank (Google Cloud, 2020) and Commerzbank (Google, targeting 85% of apps by 2024) — external, larger European peers, but *multi-year in-progress* rather than a declared core completion (via Computer Weekly / Data Centre Magazine, as of announcement dates).
Read: Intesa is *in-line to ahead* of European incumbents on ambition and notably ahead on declared completeness of a full-estate core migration; most in-base comps are single-unit or "selected", so Intesa is an outlier on scope, not on approach. For context, Intesa itself trades at P/E ~11 / ~€104bn market cap (per companiesmarketcap/Yahoo, mid-2026) — a normal EU-bank multiple; the migration is not (yet) a re-rating event.

**Risk flags.**
1. **Single-hyperscaler concentration / lock-in.** Full core on Google Cloud (with TIM) concentrates operational + regulatory dependence on one provider; ECB/Bank of Italy concentration-risk and DORA (EU operational-resilience regime) scrutiny of critical-ICT-provider dependence is the direct second-order concern — exit/portability becomes a live supervisory question once the *core* runs on one cloud.
2. **"Completed / no major incidents" is management PR, unquantified.** No independent uptime, cost-saving, or run-rate figure was disclosed ("reduced costs", no number). De-PR: "migrated" ≠ proven cheaper/more resilient across a stress cycle; the payoff thesis (AI on Isytech) is prospective.
3. **Value captured up-stack, not by the bank.** The recurring economics of running core in-cloud accrue to Google + TIM + Thought Machine; the bank swaps capex/on-prem for opex/vendor rails, so margin on the infra layer is disintermediated to the stack — savings depend on FinOps discipline holding over years.

**What this changes (idea-lens).** (analysis) Signal for the *hyperscaler-in-banking* thesis: a G-SIB-scale European incumbent declaring a *completed* full core migration is a credibility marker for Google Cloud vs AWS/Azure in regulated EU banking, and a reference-sell for TIM's sovereign-region model. Falsifiable thesis: if Intesa's 2026–2029 plan reports concrete IT-cost-per-asset reduction or faster product velocity attributable to Isytech, expect more EU incumbents to commit full-core (not just app) migrations. What breaks it: a supervisory concentration/DORA intervention forcing multi-cloud/exit plans, or a public incident, would chill full-core single-cloud commitments. Trigger to watch: cost/efficiency disclosure at Intesa's next business-plan update and any Bank of Italy/ECB commentary on cloud concentration.

Sources: https://www.finextra.com/newsarticle/48033/intesa-sanpaolo-migrates-core-it-systems-to-google-cloud-infrastructure · https://group.intesasanpaolo.com/en/newsroom/press-releases/2026/07/intesa-sanpaolo-cloud-core-banking · https://www.fintechfutures.com/cloud-services/intesa-sanpaolo-completes-core-it-migration-to-google-cloud · https://market.us/report/cloud-core-banking-platform-market/ · https://www.numberanalytics.com/blog/cloud-adoption-banking-statistics · https://datacentremagazine.com/automation/deutsche-bank-migrates-core-it-system-google-cloud · https://www.computerweekly.com/news/252498684/Commerzbank-picks-Google-for-cloud-migration · https://companiesmarketcap.com/intesa-sanpaolo/pe-ratio/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
