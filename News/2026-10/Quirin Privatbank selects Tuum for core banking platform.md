---
title: "Quirin Privatbank selects Tuum for core banking platform"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/quirin-privatbank
  - company/tuum
  - industry/banking
  - region/europe
  - type/partnership
sources:
  - https://tuum.com
  - https://tuum.com/news/quirin-privatbank-selects-tuum-core-banking
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s3c94183b
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Quirin Privatbank selects Tuum for core banking platform

> [!info] 2026-10-23 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇩🇪 Quirin Privatbank selects Tuum as its new core banking platform. The Berlin bank will run Tuum's Accounts, Deposits, Payments and Loans modules. The move targets client onboarding in minutes and SEPA Instant payments.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://tuum.com>
- <https://tuum.com/news/quirin-privatbank-selects-tuum-core-banking>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Quirin Privatbank selects Tuum for core banking platform
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-10-22 Quirin Privatbank (Berlin-headquartered German private bank, fee-only model) announced it has **selected Tuum** (Estonian cloud-native core-banking vendor) as its new core banking platform. It will run Tuum's **Accounts, Deposits, Payments and Loans** modules, targeting account onboarding "in minutes", instant payments (incl. SEPA Instant), real-time transaction data for staff, and faster regulatory reporting. The PR frames this as building "Germany's most modern private bank." (Sources: https://natlawreview.com/press-releases/quirin-privatbank-selects-tuum-build-germanys-most-modern-private-bank ; https://globalfintechseries.com/banking/quirin-privatbank-selects-tuum-to-build-germanys-most-modern-private-bank/)

**De-PR reality — this is a core REPLACEMENT, not a greenfield.** The press release omits the incumbent, but it is public record: Quirin ran **Avaloq** (Swiss core + BPaaS back-office, used since 2016) and in **March 2022 extended that Avaloq contract until 2028** (https://www.avaloq.com/insights/news/quirin-privatbank-extends-its-long-term-contract-with-avaloq). So within ~4 years of re-committing to Avaloq-to-2028, Quirin is switching cores to Tuum — a rip-and-replace, which is exactly why the announcement is a "selection" (signed decision), **not a go-live**. Everything stated ("onboarding in minutes", "SEPA Instant") is a target/aspiration of the future build, not a live metric. This is "announced," not "adopted."

**Why structured this way / what it reveals (analysis).** The deal is one leg of a **broader, multi-vendor stack rebuild**. In parallel Quirin + its robo-advisor quirion are migrating the **entire investment/securities infrastructure to Upvest** (API-based), a multi-step program beginning early-2027 and running to ~2028, a reported ~€20M program (https://upvest.co/blog/quirin-privatbank-and-quirion-migrate-to-upvest ; https://www.it-finanzmagazin.de/die-quirin-privatbank-und-quirion-migrieren-die-gesamte-it-auf-upvest-252375/). So Quirin is deliberately **unbundling a single monolithic incumbent (Avaloq) into best-of-breed composable components** (Tuum = core banking, Upvest = investment execution). Tuum's API-first architecture is the enabler of that component-swap strategy. The real story is not "a bank picked a vendor" but "an established €11.1bn-AUM private bank is decommissioning a monolith it re-signed to 2028, in favour of a composable multi-vendor stack."

## [1] Competitors / peers
Tuum's "buy" competitors in the modern-core field (all cloud-native / API-first):
- **Thought Machine** (Vault Core) — tier-1 deployments (Lloyds, Standard Chartered); FY2025 revenue >$100M (+57% YoY), ARR >$100M; raised £30M/£45M in 2025–26 ([[Thought Machine secures GBP 30m funding from new investor]], [[Thought Machine tops $100m revenue for FY2025, up 57%]]). The category revenue leader.
- **Mambu** — composable SaaS, ~$5.5bn 2021 mark, broad BaaS footprint; recent core wins e.g. Nyla ([[Mambu selected as core banking provider by Nyla]]).
- **10x Banking** — polyglot runtime + migration tooling aimed at moving legacy books ([[10x Banking partners Tungsten Automation to power Pay+ ledger]]).
- **Temenos** — incumbent at scale (~950 banks) retrofitting AI into its core ([[Temenos launches embedded AI agents across core and digital banking]]).
- **Avaloq** — the DISPLACED incumbent here; Swiss, strong in private banking/wealth (HSBC Private Bank, others). The loss of a long-standing, recently-re-signed Avaloq client to Tuum is the competitively notable fact.
Tuum's own live/reference base: Banking Circle, LHV UK, Nets, Multitude Bank ([[Tuum secures strategic partnership extension with Multitude Bank to power long-term growth and innovation]]), maib, Bondora, Uptex Bank/OBD Holding in Oman ([[Oman's OBD Holding selects Tuum to launch Uptex Bank]]).

**Why the landscape is this way / second-order (analysis).** The modern-core field is crowded and now competes on **AI-native functionality and migration tooling**, not just deployment speed. Tuum is a **mid-size challenger** (FY2023 revenue ~€3.68M off a tiny base, ~$49.8M total raised) — well below Thought Machine/Mambu by revenue and raise. What makes Quirin material for Tuum is not size but **category: it is a marquee DACH private-banking reference win**, precisely the market Tuum's €25M Series B (led by CommerzVentures, a Commerzbank vehicle) was raised to penetrate. Displacing Avaloq — a private-banking specialist — in its home-turf wealth segment is a credibility signal disproportionate to the single logo.

## [2] Company history / fit
**Quirin Privatbank** (Berlin): founded on a notable premise — in 2006 it became the first German bank to abandon commission-based advice for a fee-only model. It owns/operates the digital robo-advisor **quirion** (founded 2013). As of 30 June 2026 the Quirin group managed **€11.1bn AUM for ~118,000 clients** (https://www.quirinprivatbank.de/pm/6-mrd-aum ; quirion AUM +~20–25% in 2025) — an established, growing mid-market wealth player, not a startup.
**Tuum** (Tallinn, founded 2019 as Modularbank): cloud-native, API-first, modular core; ~$49.8M raised over 5 rounds; €25M Series B led by CommerzVentures + Speedinvest, earmarked for **DACH, Southern Europe and Middle East** expansion. 2026 leadership build-out: ex-Vocalink CEO Gregor Dobbie as CEO ([[Tuum names Vocalink veteran Gregor Dobbie as CEO]]), James Bushby as CRO ([[Tuum names James Bushby as Chief Revenue Officer]]), Renato Cassinelli head of marketing ([[Tuum appoints Renato Cassinelli as head of marketing]]).

**Why both act this way (analysis).** For Quirin: a digital-first, fee-only wealth manager scaling AUM needs cheap, fast product iteration and straight-through processing; a decades-old monolith (even Avaloq's BPaaS with ~100% STP) is a time-to-market bottleneck — exactly the "TCO vs time-to-market" trade-off Tuum has been publicly campaigning on ([[Tuum Should banks build their own core]]). For Tuum: landing an €11.1bn-AUM German private bank directly executes the DACH thesis its Series B (CommerzVentures = Commerzbank-linked) funded. The fit is logical on both sides.

## [3] Novelty / value-add / traction
**What's genuinely new:** a signed decision by an established, recently-Avaloq-committed private bank to replace its core with a challenger vendor — a real "incumbent displacement," which is rarer and harder than a greenfield neobank win. For Tuum this is arguably its highest-profile DACH reference to date.
**What is NOT yet proven:** zero live traction. No go-live date, no migrated-client/account numbers, no reporting of actual onboarding/SEPA-Instant performance. Core migrations are the sector's chronic failure mode (big-bang risk, legacy-data mess, failure to decommission the old core; ~94% of core-modernization projects reportedly overrun timelines). Until Quirin is live on Tuum, the "modern private bank" claim is a plan.
**Who captures the margin / what underpins the value (analysis).** Tuum's value-add is real only if the migration lands and sticks: switching costs then become Tuum's moat (multi-year lock-in, reference pull in DACH). But the composable/unbundled strategy Quirin is pursuing cuts both ways — the same API-first modularity that let Quirin swap Avaloq out for Tuum **also lets Quirin swap Tuum out later** without disturbing the rest of the stack. Modularity lowers the vendor's own lock-in. So the durable question is whether Tuum becomes the sticky system-of-record or just one replaceable component among Upvest et al.

## [4] What's next / market sentiment
Watch for: (1) a **go-live date and phased migration plan** (the only thing that converts "selection" into traction); (2) whether Quirin's parallel **Upvest** investment-infra migration (early-2027 start, to ~2028) stays on schedule, since the two programs together define the real stack rebuild; (3) further Tuum DACH wins that would confirm Quirin was a beachhead not a one-off. Regulatory backdrop: PSD3/instant-payments mandates and DORA operational-resilience rules are structural tailwinds for cloud-native cores in Europe.
**Why the market goes this way / second-order (analysis).** The secular shift from monolithic incumbents (Avaloq, Temenos, FIS) to composable challengers favours "buy/hybrid" for most mid-market banks — but the counterintuitive effect is that **composability erodes the very lock-in that makes core vendors valuable**: as banks learn to unbundle (Avaloq → Tuum + Upvest), each vendor's share of wallet and switching-cost moat shrinks, pushing core vendors to compete on continuous AI/feature velocity rather than one-time capture. The win is a credibility milestone for Tuum; the risk is that migration slippage or a public failure would damage the challenger thesis more than it helps.

## Sources
- Tuum/Quirin PR: https://natlawreview.com/press-releases/quirin-privatbank-selects-tuum-build-germanys-most-modern-private-bank ; https://globalfintechseries.com/banking/quirin-privatbank-selects-tuum-to-build-germanys-most-modern-private-bank/ ; https://tuum.com/news/quirin-privatbank-selects-tuum-core-banking
- Incumbent (Avaloq) contract to 2028: https://www.avaloq.com/insights/news/quirin-privatbank-extends-its-long-term-contract-with-avaloq
- Parallel Upvest investment-infra migration: https://upvest.co/blog/quirin-privatbank-and-quirion-migrate-to-upvest ; https://www.it-finanzmagazin.de/die-quirin-privatbank-und-quirion-migrieren-die-gesamte-it-auf-upvest-252375/ ; https://thepaypers.com/fintech/news/quirin-privatbank-and-quirion-move-investment-infrastructure-to-upvest
- Quirin AUM / profile: https://www.quirinprivatbank.de/pm/6-mrd-aum
- Tuum funding/clients: https://www.fintechfutures.com/core-banking-technology/core-banking-tech-challenger-tuum-secures-25m-series-b-to-tap-new-territories ; https://tracxn.com/d/companies/tuum
- Core-banking field: https://www.10xbanking.com/core-banking-platforms-compared
- Internal priors: [[Tuum Should banks build their own core]] · [[Tuum names Vocalink veteran Gregor Dobbie as CEO]] · [[Tuum secures strategic partnership extension with Multitude Bank to power long-term growth and innovation]] · [[Thought Machine tops $100m revenue for FY2025, up 57%]] · [[Mambu selected as core banking provider by Nyla]] · [[Oman's OBD Holding selects Tuum to launch Uptex Bank]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge**

1. Is this news or PR? — Real news: a signed core-vendor selection by an established €11.1bn-AUM bank. But "Germany's most modern private bank" is pure PR; the substance is the vendor decision, not the superlative.
2. Selection or go-live? — **Selection only.** No go-live date, no phased plan, no migrated accounts. All stated benefits (onboarding in minutes, SEPA Instant, real-time data) are future targets, not live metrics. Announced ≠ adopted.
3. Who is the displaced incumbent? — **Avaloq** (used since 2016). Not in the PR but on record; this is a rip-and-replace, not greenfield.
4. Isn't this odd given Avaloq was re-signed to 2028? — Yes, and that's the interesting bit: Quirin extended Avaloq to 2028 in March 2022, then ~4 years later switched cores. Signals genuine dissatisfaction / strategic pivot to composability, not routine renewal.
5. Is this a single deal or part of a bigger rebuild? — Bigger rebuild. In parallel Quirin + quirion are migrating investment/securities infra to **Upvest** (early-2027 → ~2028, ~€20M program). Tuum is one leg of an unbundling of Avaloq into best-of-breed components.
6. How material is this for Tuum? — High relative to its size: Tuum is a mid-size challenger (FY2023 rev ~€3.68M, ~$49.8M raised). A marquee DACH private-banking reference directly executes its CommerzVentures-funded DACH thesis. Logo value > revenue value.
7. Any disclosed contract value / term / TCV? — Open. No deal size, duration or revenue to Tuum disclosed.
8. Is the migration risk being downplayed? — Yes (by omission). Core migrations overrun ~94% of the time; big-bang/legacy-data risk is the sector's chronic failure mode. The "modern bank" claim is contingent on a migration that hasn't started.
9. Does Quirin's own composability strategy undercut Tuum's lock-in? — Yes (analysis). The same API-first modularity that let Quirin drop Avaloq lets it later drop Tuum. Modularity lowers the vendor's switching-cost moat.
10. Is this a duplicate of an existing note? — No. Closest prior is [[Tuum Should banks build their own core]] (2026-10-08) — a vendor opinion piece, NOT this deal. This is a distinct, new event (a concrete client win). Fresh.
11. Is Tuum credible vs the field? — Credible but sub-scale: below Thought Machine (>$100M rev) and Mambu by revenue/raise. Competes on composability/speed, not scale.
12. What's the second-order read? — Composability consolidates core spend toward a few challengers yet erodes each one's lock-in; vendors must win on continuous feature/AI velocity, not one-time capture.
13. Regulatory catalyst? — Structural tailwinds (PSD3, SEPA Instant mandate, DORA) favour cloud-native cores in the EU; no single named trigger for this deal.
14. Would omitting it lose anything? — Some. It's a genuine incumbent-displacement datapoint in a theme the DB tracks heavily; but with no numbers and no go-live, its standalone weight is moderate.
15. Date/recency confirmed? — Announced 2026-10-22; note dated 2026-10-23. Current. Fresh.

**Importance: 3/5** — A real, dated event (signed core-vendor selection) with genuine competitive significance: an established German private bank displacing a recently-re-signed Avaloq monolith in favour of a composable multi-vendor stack (Tuum core + Upvest investment infra), and a marquee DACH reference win for a sub-scale challenger. Downgraded from higher because it is a selection with zero live traction (no go-live, no account/migration numbers, no contract value), execution risk is high, and the headline superlative is PR. Fresh — not a duplicate of the existing Tuum commentary note.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Quirin Privatbank, a Berlin private bank, is replacing its core on a cloud-native, modular platform (Tuum) — a core-replacement deal in the DACH market. Market sizing varies by definition and should be read as order-of-magnitude only: core-banking-software estimates cluster around $13–19bn for 2025 with ~10–17% CAGR (Grand View ~$13.3bn 2025, 10.2% CAGR; Fortune Business Insights ~$19.3bn 2025, 17.4% CAGR — per vendor-commissioned research firms, as of 2025), while cloud/SaaS sub-segments are pegged higher-growth (~20% CAGR per Precedence Research). These are third-party research-firm figures, not audited — treat as directional. Structure: concentrated at the top — Temenos holds ~15% of the global core market and claims 950+ bank customers (per Temenos FY2025 annual report / 6sense, as of early 2026); the legacy tier (Temenos, Avaloq/NEC, FIS, Finastra) still dominates installed base, with cloud-native challengers (Tuum, Mambu, Thought Machine, 10x) competing for new/replacement deals. Barriers are high: regulation, migration risk, and multi-year switching costs. Why now: cloud-native re-platforming to cut onboarding/settlement latency; Quirin also cites Germany's state-subsidized Altersvorsorgedepot retirement account launching 2027-01-01 as an expected inflow catalyst (analysis — forward-looking, bank's own claim).

**Competitive landscape.** Sector KPIs: for core vendors — ARR/revenue growth, bank logos won, migration throughput; for the bank — onboarding time, settlement latency (SEPA Instant), reg-reporting cycle time. Players & basis of competition: legacy incumbents (Temenos ARR ~$860m, +12% YoY; revenue ~$1.15bn FY2025 est.) compete on breadth/installed base; challengers compete on cloud-native, API-first, modular architecture and migration ease. Tiering (per CB Insights): Thought Machine and 10x target large banks; Mambu, Tuum and SDK.finance serve digital players and mid-tier. Recent peer moves: Thought Machine raised £45m (2025-10, losses widening) and reported crossing $100m revenue for FY2025; 10x hired a senior ex-Temenos exec (2025-10) to push global growth; Mambu kept winning emerging-market logos (Wio Bank UAE, Krom Bank Indonesia, 2025). Protagonist (Tuum) position: niche/catching-up challenger — a win against incumbent Avaloq (which Quirin had a long-term contract with per Avaloq's own prior release) is a credible displacement reference. Moat: switching costs + architectural lock-in once live; still small-scale vs incumbents (analysis).

**Comps & multiples.** Tuum is private; no public multiple. Last round: €25m Series B led by CommerzVentures (2024-02); total raised ~$46m (per CB Insights); valuation not disclosed → EV/Revenue, P/S = no data. Peer references:
- Thought Machine — £45m round (2025-10), ~$100m revenue FY2025; round valuation not disclosed in corpus → multiple = no data. [[Thought Machine lands GBP 45M funding as losses widen]]
- Mambu — private, recent round valuation not sourced here → no data. [[Wio Bank leverages Mambu for composable banking]]
- 10x Banking — private, no public multiple. [[Philip Barnett named executive vice chair at 10x Banking]]
- Temenos (public, SIX: TEMN) — ARR ~$860m, revenue ~$1.15bn FY2025; the only listed comp but far larger/broader, not a like-for-like scale comp for Tuum.
With all challengers private and valuations undisclosed, no median/distribution computed — qualitative comparison only. [UNSOURCED]: Tuum/Mambu/Thought Machine post-money valuations and revenue multiples.

**Risk flags.**
1. Execution/migration risk — a full core replacement plus a "wider rebuild of the technology stack" is multi-year; delivery slips or a botched cutover would hit Quirin ops and dent Tuum's displacement reference. Why: core migrations are where challengers historically stumble.
2. Scale/survival risk around Tuum — a ~$46m-total-raised vendor with peers (Thought Machine) openly "widening losses" signals the cloud-core cohort is still cash-burning and unconsolidated; vendor viability over a 5–10yr core lifespan is a real procurement risk. Why: a stressed or acquired vendor mid-migration transfers risk to the bank.
3. Catalyst-dependence / unproven volumes — the Altersvorsorgedepot inflow thesis (2027) is a forward bank claim, not realized AUM; if the scheme underdelivers, the ROI case for the re-platform weakens. Why: the deal's economics partly rest on an external, policy-driven demand event.

**What this changes (idea-lens).** One more incumbent-displacement (Avaloq → Tuum) in DACH is a data point that cloud-native cores are now winning in the conservative German private-banking segment, not just neobanks (analysis). Falsifiable thesis: if 2–3 more DACH/private-bank core wins land for the challenger cohort within ~12 months, it signals a genuine re-platforming wave; trigger to watch — reference go-lives (not just signings) and whether incumbents respond with cloud-native rewrites vs defending installed base. Thesis breaks if the Quirin migration stalls publicly.

Sources: https://natlawreview.com/press-releases/quirin-privatbank-selects-tuum-build-germanys-most-modern-private-bank · https://www.avaloq.com/insights/news/quirin-privatbank-extends-its-long-term-contract-with-avaloq · https://www.cbinsights.com/company/tuum · https://ibsintelligence.com/ibsi-news/tuum-raises-e25m-series-b-financing-led-by-commerzventures/ · https://www.temenos.com/wp-content/uploads/2026/02/temenos-q4-2025-results-presentation-22tw4tk10.pdf · https://6sense.com/tech/banking/temenos-core-market-share · https://www.grandviewresearch.com/industry-analysis/core-banking-software-market · https://www.fortunebusinessinsights.com/core-banking-software-market-104392
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
