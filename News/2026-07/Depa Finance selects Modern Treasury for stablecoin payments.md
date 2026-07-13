---
title: "Depa Finance selects Modern Treasury for stablecoin payments"
date: 2026-07-09
retrieved: 2026-07-09
tags:
  - company/depa-finance
  - company/modern-treasury
  - industry/stablecoins
  - region/us
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/a1a258bb
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: se039be2f
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Depa Finance selects Modern Treasury for stablecoin payments

> [!info] 2026-07-09 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Depa Finance selects Modern Treasury to power its stablecoin-native cross-border payments infrastructure. Through Modern Treasury, Depa is able to automate flows between fiat and stablecoin accounts, manage the full lifecycle of payment orders at scale, and extend Global USD Accounts to clients.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/a1a258bb>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Depa Finance selects Modern Treasury for stablecoin payments
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Depa Finance — a venture-backed cross-border-payments infrastructure startup (founded in Valencia, Spain, presence in Canada/US; self-reported 200+ countries, ~14,000 payments/day, ~$1B annual currency volume) — has adopted **Modern Treasury** as the software/orchestration layer for its stablecoin-native cross-border rails. Per the digest, Depa uses Modern Treasury to (a) automate flows between fiat and stablecoin accounts, (b) manage the full payment-order lifecycle at scale, and (c) extend **Global USD Accounts** to its clients.
- **What this actually is: a vendor-selection/customer win, not a strategic partnership.** Modern Treasury is the API "payment operations" layer; Depa is a customer building on it. The note title ("selects") and body ("power its... infrastructure") confirm buyer→vendor, not a two-way alliance. This is PR for both sides but weighted toward Modern Treasury's logo-collection.
- **Every named capability is a pre-existing Modern Treasury product, not something built for Depa.** "Global USD Accounts" was launched by Modern Treasury on ~2026-05-18 (BusinessWire) as named USD accounts in 90+ countries across ACH/Wire/RTP/FedNow + stablecoin conversion (USDG, PYUSD, USDC on Base/Ethereum/Polygon/Solana/Stellar/Arbitrum). "Payment orders" and "stablecoin orchestration" (pay-in → convert → payout via one API) are core Modern Treasury primitives. So Depa is **consuming** these, not co-developing.
- **Silence / vagueness (red-team):** no contract size, no go-live date, no volume committed, no exclusivity, no economics. "Is able to automate / manage / extend" is capability language, not a live-traction claim → likely **announced, adoption status unproven**. Whether Depa was already live on these rails or is migrating is not stated.
- **Why framed this way:** Modern Treasury spent H1 2026 launching Payments PSP (2026-02-18) and Global USD Accounts (2026-05) and is now harvesting reference customers to prove the new stack has demand; Depa gets validation-by-association with a US infra name. The press frame overstates novelty — the underlying tech shipped months earlier.

## [1] Competitors / peers
Depa's chosen layer (Modern Treasury = payment-operations/orchestration software) sits in a crowded, fast-consolidating stablecoin-orchestration stack:
- **Bridge (acquired by Stripe, 2025)** — custodial B2B stablecoin API for fiat↔stablecoin + bank-rail payouts; the category leader by mindshare. See [[This Week in Fintech Bridge powers money movement for fintechs (2)]], [[This Week in Fintech Shopify and Remitly among Bridge users]].
- **Circle** — CCTP + USDC "Bridge" product (Apr 2026) moving from dev-protocol to consumer-facing orchestration; Modern Treasury is a Circle Alliance member (i.e., partly rides Circle rails).
- **Cross River** — bank-grade unified fiat+stablecoin platform launched 2025-11 ([[Cross River launches unified stablecoin payment platform]]) — a bank competing on the same "one interoperable system" pitch.
- **Brale / Paxos** — regulated issuance/money-transmission partners that Modern Treasury *integrates* (Brale powers its payouts), so they are suppliers-cum-rivals, not head-to-head with Depa.
- **Mastercard+Thunes**, **Conduit, Eco, Across, Relay, LiFi** — payout-network and cross-chain routing peers ([[Mastercard and Thunes bring stablecoin payouts to mainstream]]).
- **Position:** Depa is a mid-tier aggregator ("one integration for stablecoin payments") that chose to *buy* orchestration rather than build it. That is a rational catch-up move, not a lead. Modern Treasury's win here is parity/incremental logo, not a category-defining deal.
**Why the landscape looks like this (2nd order):** the orchestration layer is commoditizing — pay-in/convert/payout over the same 5-6 chains and stablecoins (USDC/USDG/PYUSD) is table stakes. Margin is migrating to (a) the issuer float (Circle/Paxos) and (b) whoever owns the compliant bank/MTL license. A pure software-orchestration layer like Modern Treasury risks being squeezed between issuers above and banks/licensees below — the same disintermediation risk any "dashboard, not the payer" faces.

## [2] Company history / fit
- **Depa Finance:** since 2021 building crypto↔fiat transfer infra; real-time ledger, MPC wallets, KYC/KYB/AML, on/off-ramp, treasury across 200+ countries. Self-reported scale (14k payments/day, $1B/yr) is modest and unaudited. No funding figures disclosed on its site.
- **Fit:** logical. A cross-border aggregator whose value prop is "one integration" naturally outsources the payment-operations/ledger complexity to a specialist rather than maintaining it in-house — lets Depa extend USD-account functionality without building a US banking/orchestration stack. **Why Depa acts this way:** as a small international startup, build-vs-buy on payment ops favors buy; the differentiation it wants to keep is client relationships and country coverage, not ledger plumbing.
- **Modern Treasury fit:** classic land-and-expand — sell the orchestration API + newly launched Global USD Accounts to a fintech that resells to end-clients (platform-of-platforms distribution).

## [3] Novelty / value-add / traction
- **Novelty: low.** Nothing new is built here. Both the product (Global USD Accounts, stablecoin orchestration) and the pattern (fintech adopts Modern Treasury) predate this. It is a customer announcement layered on already-shipped products.
- **Value-add (real):** for Depa, faster time-to-market on USD accounts + unified fiat/stablecoin lifecycle without in-house build; for Modern Treasury, a reference customer for its 2026 product push.
- **Traction (the honest gate):** **unproven from this note.** No live volume through the Modern Treasury integration, no client count on Global USD Accounts via Depa, no go-live date. Depa's own scale numbers are self-reported. Treat as "announced/selected," not "live at scale."
- **Who captures the margin:** not the orchestration layer per se. In this stack the durable economics sit with the **stablecoin issuer float** (Circle/Paxos/USDG) and the **licensed bank/MTL** (Brale, partner banks). Modern Treasury monetizes software/usage fees; Depa monetizes FX/spread + payment fees. Both are thin, competitive take-rates → the deal's *strategic* value is distribution, not defensible margin.

## [4] What's next / market sentiment
- **Next:** watch for a follow-up with actual numbers (volume live on Modern Treasury, # of Global USD Accounts opened via Depa). Absent that, this stays a logo slide. Modern Treasury will keep stacking such customer wins to validate its Feb/May 2026 launches.
- **Backdrop:** stablecoin cross-border is the hottest 2025-26 infra theme (GENIUS/regulatory tailwinds in the US; Circle IPO-era momentum; Stripe/Bridge, Cross River, Mastercard/Thunes all crowding in). Demand is real; differentiation is thin.
- **Risk / counterintuitive 2nd order:** the commoditization that makes it *easy* for Depa to plug in is the same force that erodes pricing power for everyone in the orchestration middle — the more "one API for fiat+stablecoin" becomes standard, the less any single vendor selection matters. A vendor win today is a switching-cost bet tomorrow, and switching costs in orchestration are low.

## Sources
- Note digest text (Connecting the Dots in Fintech), source URL: https://www.connectingthedotsinfin.tech/r/a1a258bb
- Depa Finance — https://depa.finance/ , https://depa.finance/about-us
- Modern Treasury — Global USD Accounts launch (BusinessWire, 2026-05-18): https://www.businesswire.com/news/home/20260518787777/en/Modern-Treasury-Launches-Global-USD-Accounts-Enabling-Platforms-to-Serve-Users-in-90-Countries ; https://www.moderntreasury.com/solutions/global-usd-accounts
- Modern Treasury Payments PSP (2026-02-18): https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-launches-payments
- Modern Treasury Stablecoin Orchestration: https://www.moderntreasury.com/solutions/stablecoin-orchestration
- Brale × Modern Treasury payouts: https://brale.xyz/blog/modern-treasury-stablecoin-payouts
- Internal: [[Cross River launches unified stablecoin payment platform]], [[Mastercard and Thunes bring stablecoin payouts to mainstream]], [[This Week in Fintech Bridge powers money movement for fintechs (2)]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions.** Importance: 2/5.

1. Is this a partnership or a vendor selection? → **Vendor/customer win** ("Depa selects Modern Treasury to power its infrastructure"). Not a two-way strategic alliance. Weighted as Modern Treasury logo-collection.
2. Was anything built for Depa, or is it off-the-shelf? → **Off-the-shelf.** Global USD Accounts (launched ~2026-05-18) and stablecoin orchestration/payment orders are pre-existing Modern Treasury products. Nothing new engineered here.
3. Live or announced? → **Announced/selected.** No go-live date, no live volume on the integration, no client count. "Is able to" = capability, not traction. Open.
4. Deal size / economics / exclusivity? → **All undisclosed.** No contract value, no volume commitment, no exclusivity. Silence is telling.
5. Are Depa's scale numbers verified? → **No.** 200+ countries, 14k payments/day, $1B/yr are self-reported on its own site; unaudited.
6. Is this a duplicate of a prior corpus note? → **No.** Grep surfaced only thematic stablecoin peers (Cross River, Mastercard/Thunes, Bridge); no prior note on Depa Finance or Modern Treasury. → **FRESH.**
7. Who captures the margin in this stack? → Issuer float (Circle/Paxos/USDG) + licensed bank/MTL (Brale/partner banks). Orchestration software (Modern Treasury) earns thin usage fees; Depa earns thin FX/payment spread. Not a defensible-margin deal.
8. What is Modern Treasury's real differentiator vs Bridge/Circle/Cross River? → Payment-operations/ledger depth + multi-rail (ACH/Wire/RTP/FedNow + stablecoin) in one API. But this is converging to table stakes → commoditizing. Open whether it holds.
9. Why now? → Modern Treasury shipped Payments PSP (2026-02) and Global USD Accounts (2026-05) and is harvesting reference customers to prove demand. Depa gets US-infra validation. Timing is PR-driven.
10. Does Depa gain a defensible advantage? → No. Orchestration switching costs are low; buying a commoditizing layer is catch-up, not a moat.
11. Which stablecoins/chains are actually in scope for Depa? → Unstated in the note. Modern Treasury supports USDG/PYUSD/USDC across Base/Ethereum/Polygon/Solana/Stellar/Arbitrum — but Depa's specific usage isn't disclosed. Open.
12. Regulatory exposure? → US GENIUS-era tailwinds help; but neither party's licensing posture for these flows is detailed. Compliance is outsourced (Brale MTL etc.). Open.
13. Counterintuitive 2nd-order? → The commoditization that makes Depa's plug-in easy also erodes pricing power across the orchestration middle → a vendor win today = a low-switching-cost bet tomorrow.
14. Does this move any market? → No. Micro-cap customer announcement in a crowded theme. Not market-moving.
15. What would upgrade importance? → A follow-up with live volume, named end-clients on Global USD Accounts via Depa, or disclosed economics/exclusivity. Absent that, it stays a logo slide.

**Verdict:** FRESH (no prior corpus coverage of either party), but LOW weight — off-the-shelf products, no disclosed traction/economics, small self-reported customer, crowded commoditizing category.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Depa Finance sits in stablecoin-native cross-border payment orchestration — using stablecoin rails plus last-mile fiat payout to replace correspondent banking; Modern Treasury is the payment-ops layer underneath. Sizing: per Mordor Intelligence (via mordorintelligence.com), the stablecoin market is ~$0.33tn in 2026, projected to ~$1.16tn by 2031 at ~28.8% CAGR. Cross-border/remittance use is the fastest sub-segment (~36.5% CAGR through 2031 per the same report); Juniper Research projects B2B cross-border stablecoin payments reaching $5tn by 2035 from ~$13.4bn in 2026 (per coindesk.com, 2026-04-27). Reality check: stablecoins are still ~1% of global payment flows, unchanged since 2023–24 despite 60x growth in absolute B2B volume (per FXC Intelligence / fxcintel.com) — i.e. explosive on a tiny base. Structure: the value chain is fragmenting into (a) issuers/reserves (Circle, Paxos), (b) corridor/offramp providers (Bridge, BVNK, Conduit), and (c) an orchestration/payment-ops layer that routes across rails (Modern Treasury, Eco Routes). Entry barriers are regulatory (money-transmission / MiCA / EMI licensing) and network (banking + liquidity partners), not code. Why now: GENIUS Act + MiCA gave stablecoins a compliance wrapper, and incumbents (Stripe, Mastercard, Visa) validated the category via M&A in 2025–26, pulling B2B treasury flows on-chain.

**Competitive landscape.** Sector KPIs: TPV/processing volume, take rate per transaction, corridor coverage (# countries), and rail breadth (ACH/wire/RTP/FedNow + stablecoin). Modern Treasury's own moves (PRIMARY, IR): launched Global USD Accounts serving 90+ countries via a single API across ACH/wire/RTP/FedNow + stablecoin rails (moderntreasury.com); launched "Payments," an integrated PSP for fiat AND stablecoins, 2026-02-18 (IR product_update); acquired Beam to build instant stablecoin payments, 2025-10-22 (IR press_release); partnered Paxos to move money with stablecoins, 2025-12-18 (IR press_release, latest_result); and won Anchorage Digital as a money-movement customer, 2025-11-10 (IR press_release). So Depa is one more crypto-native platform in Modern Treasury's stablecoin-orchestration pipeline. Basis of competition: distribution + rail breadth + compliance, not price. Peer moves: Mastercard agreed to acquire BVNK for up to $1.8bn (2026-03) [[Mastercard to acquire stablecoin firm BVNK for up to $1.8bn]]; Stripe's Bridge powers Shopify/Remitly; BVNK surpassed $20bn processing volume [[BVNK surpasses $20bn in processing volume]]; Cross River launched a unified stablecoin platform [[Cross River launches unified stablecoin payment platform]]. Protagonist positioning: Depa = niche/early cross-border challenger that outsources its money-ops backbone; Modern Treasury = established payment-ops incumbent moving into stablecoins from strength (enterprise reconciliation/compliance = switching-cost moat), catching up to pure crypto-native rails (Bridge/BVNK) on corridor depth (analysis).

**Comps & multiples.** No valuation/round/metrics disclosed in this Depa–Modern Treasury deal → deal-level multiples = no data. Anchor comps (payment-ops / stablecoin infra):
- Modern Treasury — last post-money ~$2bn (Series C, Mar 2022; $183M raised total, per Crunchbase/Tracxn); no revenue disclosed → EV/Rev = no data. Valuation is stale (3+ yrs) and pre-stablecoin-pivot.
- BVNK — Mastercard acquisition up to $1.8bn (2026-03); >$20bn annual processing volume → price/TPV ≈ $1.8bn / $20bn = ~0.09x TPV (analysis; TPV ≠ revenue, illustrative only).
- Bridge — Stripe acquired for ~$1.1bn (2024, per press).
Distribution not computed (mixed metrics, only 3 comparable and heterogeneous); qualitative read: the category is being re-rated via strategic M&A at $1–2bn tickets, so Modern Treasury's stale $2bn mark looks in-line-to-conservative given its stablecoin traction (analysis). Forward multiples / clean revenue → [UNSOURCED].

**Risk flags.**
1. Rails dependence / disintermediation — Depa's entire cross-border backbone runs on Modern Treasury; if Modern Treasury raises take rate, changes terms, or is acquired (its acquirers/partners include Stripe-adjacent players), Depa's unit economics and roadmap are hostage to someone else's stack (second-order: margin captured upstream).
2. Regulatory concentration — stablecoin cross-border payouts touch money-transmission/MiCA/AML across 90–200 countries; a single-corridor licensing setback or de-pegging/reserve event hits settlement reliability, the whole pitch.
3. Adoption gap vs hype — stablecoins stuck at ~1% of payment flows; TAM is huge but penetration flat, so Depa competes for a still-thin real-volume pool against better-funded, incumbent-backed rails (Bridge/Stripe, BVNK/Mastercard).

**What this changes (idea-lens).** Confirms Modern Treasury's positioning as the neutral payment-ops/orchestration layer that crypto-native fintechs plug into rather than build — a "picks-and-shovels" re-rating for the sector, not a new entrant story (analysis). Falsifiable thesis: if Modern Treasury discloses stablecoin TPV or a fresh raise above its 2022 $2bn mark within ~12 months, the orchestration layer is capturing the volume; watch/trigger — a Depa live-volume or Global USD Accounts client-count metric (currently "announced," not proven live) would confirm real adoption; its absence would flag PR-over-traction.

Sources: https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-launches-global-usd-accounts-enabling-platforms-to-serve-users-in-90-countries · https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-launches-payments · https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-and-paxos-make-it-easier-for-businesses-to-move-money-with-stablecoins · https://www.moderntreasury.com/newsroom/press-releases/anchorage-digital-selects-modern-treasury-to-power-money-movement-infrastructure · https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-acquires-beam · https://depa.finance/ · https://www.mordorintelligence.com/industry-reports/stablecoin-market · https://www.coindesk.com/business/2026/04/27/cross-border-b2b-stablecoin-payments-to-rise-by-over-37-000-to-usd5t-by-2035 · https://www.fxcintel.com/research/reports/how-big-is-the-b2b-cross-border-payments-market · https://mpost.io/top-10-platforms-competing-to-become-the-stripe-of-stablecoin-payments-in-2026/ · https://tracxn.com/d/companies/moderntreasury/__GTF1HXt7G0YKtaQq2j8EhjTl_ORqjAdqch2Rv9MyD3Y/funding-and-investors
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news.** Modern Treasury is a **private company** (Series C, founded 2018, San Francisco) — no public 10-Q/10-K/earnings release, so there are NO reported revenue / profit / margin / EPS figures. The Depa Finance item is a **partnership/customer-win press item**, not a financial result. Its own IR feed (`ir_latest.json`) carries only product updates, partnership press releases, one shareholder letter (a Jul-2025 CEO-transition note), and one survey — no results filing.

**Disclosed operating metrics (not audited financials, from company materials / web):**
- Cumulative volume: infrastructure has processed **"more than $400 billion"** for customers (e.g. Anchorage Digital, Float, Gusto, Navan, Procore, Sling Money); highlighted in the Feb-2026 "Modern Treasury Launches Payments" announcement. `(company-disclosed cumulative figure, no YoY given)`
- Instant payments: **~$1 billion annual run-rate** on the platform. `(company-disclosed, no YoY)`

**Private-market context (third-party, not company results):** last valuation ~**$2.2bn** (unicorn); ~**$183m** raised across rounds; last public revenue datapoint was **$9m (2022)** per CB Insights — stale and [UNSOURCED] beyond that. No newer revenue disclosed.

**Strategic direction (from IR, relevant to the Depa deal, not financials):** heavy 2025–26 push into **stablecoin money movement** — Beam acquisition (Oct-2025) for instant payments, Paxos partnership (Dec-2025), Anchorage Digital win (Nov-2025), and the unified fiat+stablecoin **Payments PSP** launch (Feb-2026). The Depa Finance stablecoin-native cross-border win fits this thesis line. `(analysis)`

**Verdict: NO RESULTS** — private company, no reported financials; only cumulative-volume and run-rate KPIs disclosed. Do not infer beat/miss.

Sources: https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-launches-payments · https://pitchbook.com/profiles/company/232149-34 · https://www.cbinsights.com/company/modern-treasury/financials · https://www.fintechfutures.com/venture-capital-funding/modern-treasury-lands-50m-in-series-c-extension
<!-- /enrichment:earnings_review -->
