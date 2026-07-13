---
title: "RedotPay picks OpenPayd for stablecoin payment infrastructure"
date: 2026-07-01
retrieved: 2026-07-01
tags:
  - company/redotpay
  - company/openpayd
  - industry/stablecoins
  - region/global
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/bbea469c
  - https://www.connectingthedotsinpayments.com/r/faa321ab
status: enriched
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s3e850457
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# RedotPay picks OpenPayd for stablecoin payment infrastructure

> [!info] 2026-07-01 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 RedotPay selects OpenPayd to strengthen global stablecoin payment infrastructure for millions of customers. The collaboration strengthens RedotPay’s payment infrastructure, enabling a more seamless experience for global fund movement so users can navigate between local and digital currencies effortlessly.

[Connecting the Dots in Payments] 🇬🇧 RedotPay selects OpenPayd to strengthen global stablecoin payment infrastructure for millions of customers. The collaboration strengthens RedotPay’s payment infrastructure, enabling a more seamless experience for global fund movement so users can navigate between local and digital currencies effortlessly.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/bbea469c>
- <https://www.connectingthedotsinpayments.com/r/faa321ab>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: RedotPay picks OpenPayd for stablecoin payment infrastructure
_Analytical notes (not a post). Importance: 2/5._

**Freshness: FRESH.** Announced 30 Jun 2026 (Chainwire wire). This is a distinct, new tie-up — not covered by prior corpus notes. Nearest prior notes are different events: [[RedotPay raises $107M Series B for stablecoin payments]] (funding, Dec-2025, which earmarked capital for infra/M&A), [[OpenPayd and Ripple partner on stablecoin payments infrastructure]] (Jul-2025, OpenPayd's supply-side deal), [[OpenPayd to power Altify's multi-currency on off ramps]] (Dec-2025, analogous client win). So fresh, but structurally a routine BaaS supplier win of a familiar type.

## [0] What exactly happened (de-PR'd)
- RedotPay (global stablecoin card/payments fintech, 6M+ registered users, 100+ countries, ~$10B annualized volume, unicorn) **selected OpenPayd** (UK embedded-finance/BaaS provider) as an infrastructure supplier for **treasury operations, multi-currency payments and cross-border remittances** (Chainwire, 30 Jun 2026).
- De-PR'd: OpenPayd supplies the plumbing RedotPay does not want to build/license itself — **virtual IBANs, multi-currency named accounts, FX, domestic/international payment rails and fiat↔stablecoin on/off-ramps** via a single API. RedotPay keeps the consumer-facing card/app; OpenPayd sits underneath as the licensed fiat-money-movement layer.
- What is NOT disclosed: no contract value, no volume commitment, no exclusivity, no go-live date/geographies, no "live vs signed" status. The wording ("selects... to strengthen") is a signed-supplier announcement, not proof of production traffic. Treat as **announced, not yet demonstrably live at scale**.
- **Why structured this way:** RedotPay's edge is card issuance (Visa, 130M+ merchants) + a crypto-native user base; the hard, jurisdiction-by-jurisdiction part is regulated fiat banking access (IBANs, local rails, FX). Rather than chase a patchwork of bank/EMI licenses everywhere (it is doing that in parallel — MSB Canada/US, VASP Argentina/Mexico, per [[RedotPay secures Mexico virtual asset service provider registration]]), it rents OpenPayd's ~30-market banking network. The PR anchors to "millions of customers" to imply scale the deal itself doesn't guarantee.

## [1] Competitors / peers
- **Supply side (who else could RedotPay have picked):** BVNK (Mastercard agreed to acquire for up to $1.8B, 17 Mar 2026 — now inside a network, a reason a Visa-centric fintech like RedotPay might avoid it), Bridge (Stripe-owned), Zero Hash, Circle (already a RedotPay partner for USDC/Mexico payouts — see [[RedotPay adds crypto-to-MXN payouts via Circle in Mexico]]), StraitsX, Fireblocks. OpenPayd's differentiator vs pure stablecoin-rail players (Bridge/BVNK) is its **fiat banking network + virtual IBANs**, i.e. the fiat leg, not the crypto leg.
- **RedotPay's own peers (demand side):** Bybit Card, KAST, Bleap — same crypto-card category. RedotPay is a scale leader among them (6M users).
- **Position:** Parity/catching-up, not ahead. OpenPayd is simultaneously powering Ripple (supply deal) and clients like Altify/Hercle — RedotPay is one more logo in a repeatable BaaS pipeline, not a strategic exclusive.
- **Why the landscape looks this way + second order:** The stablecoin-infra stack has bifurcated — **crypto rails** (Bridge, BVNK, Zero Hash) vs **fiat access/BaaS** (OpenPayd, Clearbank-style). With Mastercard buying BVNK and Stripe owning Bridge, the neutral independent fiat-BaaS layer (OpenPayd) becomes more valuable to card-fintechs that don't want to route their banking through a card network competitor. That is the real (analysis) subtext of this pick.

## [2] Company history / fit
- RedotPay trajectory: Series A $40M (Mar-2025) → unicorn $47M strategic (Sep-2025, [[RedotPay reaches unicorn status with $47M round]]) → **$107M Series B (Dec-2025)** explicitly to fund "acquisitions to deepen product/infrastructure capabilities" and licensing/compliance ([[RedotPay raises $107M Series B for stablecoin payments]]). It launched UK/EU fiat-to-stablecoin onramps (Aug-2025) and a Solana card.
- OpenPayd: founded 2018 (Dr Ozan Ozerk), rails-agnostic BaaS, ~$180B annualized volume, 1,000+ clients, added ex-ClearBank COO Yasemin Swanson (Oct-2025, [[OpenPayd appoints Yasemin Swanson as COO]]); Ripple partnership Jul-2025.
- **Fit / why RedotPay acts this way:** logically consistent with the Series B thesis — build/buy infra. This is the "buy/rent" side of that thesis: OpenPayd's IBANs plug the fiat gap while RedotPay's own VASP/MSB licensing plugs the crypto gap. Structural pressure: a crypto-card business earns thin interchange/FX; to serve remittances/treasury it needs cheap, broad fiat account access it can't profitably build in 30+ markets. Renting is rational.

## [3] Novelty / value-add / traction
- **Novelty: low.** "Card fintech rents BaaS/IBAN provider" is a standard integration; OpenPayd runs this playbook repeatedly (Altify, Hercle, Ripple). No new mechanism, no disclosed volumes, no live proof-point.
- **Real value-add (if it goes live):** broader multi-currency IBAN coverage → better cross-border remittance UX and treasury for RedotPay's users, converting stablecoin holdings to local fiat via named accounts rather than P2P. That is genuinely useful for RedotPay's EM/remittance users — but it is capability parity with what onramps + Circle already partly provided.
- **Who captures the margin (analysis):** OpenPayd takes a per-transaction/account BaaS fee off RedotPay's fiat flows; RedotPay keeps the customer relationship + card interchange. Because OpenPayd holds the regulated banking relationships, **RedotPay is renting, not owning, the fiat leg** — a dependency and a margin leak. If RedotPay later acquires/licenses its own banking (Series B intent), OpenPayd is replaceable. So the deal's durability for OpenPayd is weak; for RedotPay it's a speed play, not a moat.
- **Traction: none disclosed.** Announcement only.

## [4] What's next / market sentiment
- Watch for: go-live confirmation, named geographies, and whether OpenPayd IBANs actually front RedotPay remittance corridors (vs staying a press release). Also whether RedotPay's own licensing (Mexico/Argentina VASP, US/Canada MSB) eventually in-sources what it's renting.
- **Market backdrop:** stablecoin-payment infra is consolidating fast (Mastercard→BVNK $1.8B, Stripe→Bridge). Independent BaaS/IBAN providers like OpenPayd benefit as neutral suppliers to fintechs wary of network-owned rails.
- **Counterintuitive second-order (analysis):** consolidation makes OpenPayd more attractive as the last big neutral fiat-BaaS layer, but also makes it an acquisition target — if a network buys OpenPayd, RedotPay's rented rails become a competitor's rails, reprising the exact BVNK-under-Mastercard risk. RedotPay's parallel own-licensing is the hedge.
- **Risk:** vendor lock-in / single-supplier dependency for fiat leg; regulatory exposure inherited from OpenPayd's coverage; no exclusivity means OpenPayd can serve RedotPay rivals with the same rails.

## Sources
- Chainwire / TradingView / CryptoPotato / IBS Intelligence / cfotech.asia — RedotPay selects OpenPayd (30 Jun 2026)
- Corpus: RedotPay Series B, unicorn round, Circle-MXN payouts, UK/EU onramps, Mexico VASP; OpenPayd-Ripple, OpenPayd-Altify, OpenPayd COO
- BVNK/Bridge landscape: Mastercard–BVNK ($1.8B, Mar-2026), Stripe–Bridge; openbankingtracker / eco.com comparisons
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team questions (second-order)

1. **Live or announced?** Is any RedotPay traffic actually flowing over OpenPayd IBANs, or is this a signed-supplier PR? — **Open.** Only a 30-Jun-2026 announcement; no go-live date, geographies, or volumes disclosed.
2. **Contract terms?** Value, minimum volume, tenure, exclusivity? — **Open.** None disclosed; wording implies non-exclusive supplier.
3. **Which corridors/geographies?** Where do OpenPayd's IBANs actually front RedotPay flows? — **Open.** Not specified; OpenPayd network is ~UK/EU-heavy (~30 markets).
4. **Is it new?** Does this duplicate RedotPay's existing fiat access via Circle (MXN payouts) or its UK/EU onramps? — Partly overlapping; adds multi-currency IBAN breadth, but capability parity, not a leap.
5. **Who captures the margin?** OpenPayd takes BaaS fees on fiat flows; RedotPay keeps interchange + customer. RedotPay rents, doesn't own, the fiat leg — a margin leak and dependency.
6. **Replaceability?** RedotPay's Series B explicitly funds own infra/licensing (VASP/MSB). Does that make OpenPayd a stopgap it later in-sources? — Likely; low durability for OpenPayd.
7. **Why not BVNK/Bridge?** Both now sit inside Mastercard/Stripe. A Visa-centric RedotPay plausibly avoids routing banking through a card-network rival — OpenPayd's neutrality is the (analysis) selling point.
8. **Single-supplier risk?** Does one BaaS provider become a concentration/regulatory single point of failure for RedotPay's fiat leg? — Yes, unmitigated absent multi-sourcing.
9. **Acquisition risk on the rails?** If a network buys OpenPayd (as with BVNK), RedotPay's rented rails flip to a competitor. Is RedotPay hedged? — Partly, via own licensing.
10. **What's OpenPayd silent on?** FX spread economics, uptime SLAs to RedotPay, who bears fraud/AML liability on IBAN-fronted flows. — **Open.**
11. **Scale claim vs reality:** "millions of customers" — how many will actually use IBAN/remittance features vs card spend? — **Open;** RedotPay is card-first.
12. **Strategic exclusivity to RedotPay?** OpenPayd also powers Ripple, Altify, Hercle — is RedotPay just one more logo? — Yes; repeatable BaaS pipeline, not strategic.
13. **Regulatory inheritance:** Which licenses underpin the IBANs and in which jurisdictions is RedotPay relying on OpenPayd's permissions vs its own? — **Open.**
14. **Second-order:** Does consolidation (MC-BVNK, Stripe-Bridge) make independent OpenPayd more valuable — and therefore a target, reintroducing the very risk RedotPay is avoiding? — Yes (analysis).
15. **Net weight:** Absent volumes/exclusivity/go-live, is this materially more than a routine supplier win? — No.

Importance: 2/5 — a fresh but low-novelty, announced-not-live BaaS/IBAN supplier win. Standard "crypto-card fintech rents fiat rails" integration with no disclosed terms, volumes, exclusivity, or go-live. Notable only as another data point in stablecoin-infra bifurcation (fiat-BaaS vs crypto rails) amid MC-BVNK/Stripe-Bridge consolidation; low strategic durability for OpenPayd, a speed play for RedotPay.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a wiring deal in the stablecoin cross-border-payments / embedded-finance rails layer: RedotPay (crypto-card + wallet, the consumer front-end) plugging into OpenPayd (fiat/digital-asset banking rails — virtual IBANs, multi-currency accounts, treasury). Sizing: real-world stablecoin payments volume roughly doubled in 2025 to ~$400bn, ~60% B2B (per BVP/OpenFX-cited data, via web, as of 2026); fiat-backed stablecoin supply exceeded ~$273bn in March 2026 (per BVP, as of 2026-03); Juniper projects cross-border B2B stablecoin payments reaching ~$5tn by 2035 from ~$13.4bn in 2026 (per Juniper Research, via CoinDesk, 2026-04-27) — a long-dated forecast, treat as directional, not a near-term TAM. Structure: fragmented and layered — issuers (Circle/Tether), orchestration/rails (OpenPayd, Clear Junction, Sokin, BVNK), and consumer wallets/cards (RedotPay, Wirex) each capture a slice; the value question is who owns the fiat on/off-ramp + IBAN licensing (the regulated, capital-heavy layer) vs. who owns the end user. "Why now": stablecoin supply +40x since 2020 and a maturing regulatory frame (GENIUS-type US legislation, EU MiCA) are pulling wallets to bolt on compliant fiat rails rather than build them — buy-vs-build tilting to buy `(analysis)`.

**Competitive landscape.** Sector KPIs: TPV / annualized payment volume, number of live IBANs / accounts, take rate on FX + settlement, and licensing/geographic coverage. Rails players: OpenPayd (processes >$240bn/yr for >1,100 businesses, clients incl. eToro, Kraken, OKX, B2C2 — per OpenPayd/web), Clear Junction (virtual IBANs for VASPs, see [[Clear Junction extends virtual IBAN services to VASP businesses]]), Sokin ([[Sokin launches stablecoin capabilities for hybrid finance platform]]), plus Ripple/Rail post-acquisition. Basis of competition: licensing breadth, uptime, and price, not brand. Recent moves: Ripple bought Rail for $200m (2025-08); Wirex+Utorg partnered on stablecoin card rails (2026-04); Flutterwave deployed stablecoin wallets via Turnkey/Nuvion (2026-01). RedotPay's position: a scaled consumer front-end (6M+ users across 100+ markets, >$10bn annualized volume, >$150m annualized revenue, $107m Series B in Dec-2025; Circle Ventures among backers — per RedotPay/CoinDesk) that is renting, not owning, the regulated rails. Moat is distribution/user base (switching costs on the card + wallet); it explicitly lacks the IBAN/licensing moat, which is why it needs OpenPayd `(analysis)`.

**Comps & multiples.** Deal is a commercial partnership — no valuation, no economics disclosed, so no deal multiple. Reference points (private, round/deal valuations, NOT market caps): RedotPay Series B $107m (Dec-2025), $194m raised across 2025; on ~$150m annualized revenue that is a low capital-to-revenue draw (`$194m / $150m ≈ 1.3x` raised-to-revenue — a funding-intensity read, not a valuation) `(analysis)`. OpenPayd: Tracxn shows only ~$25m total funding (Series B, Aug-2024) and a third-party revenue *estimate* of ~$35.9m — unverified, mark `[UNSOURCED]`; no post-money disclosed → no data. Internal deal comp: Ripple/Rail = $200m acquisition price, denominator undisclosed → multiple = no data; [[Ripple to acquire stablecoin platform Rail for $200 million]]. Public rails/issuer comps (Circle CRCL, dLocal DLO) exist in-base but differ in model/scale → excluded from a multiple (qualitative only). Distribution not computed (<3 comparable figures); qualitative read: RedotPay looks capital-efficient for its volume vs. peers, but with no OpenPayd valuation the deal itself can't be marked rich/cheap.

**Risk flags.**
1. **Dependence on someone else's regulated rails.** RedotPay is outsourcing the licensed, capital-heavy IBAN/treasury layer to OpenPayd; that layer is where regulatory value accrues, so RedotPay stays a distribution skin exposed to re-pricing or provider switching, and OpenPayd captures the compliance moat.
2. **"Announced" not "adopted."** Both PR blasts are identical de-PR boilerplate ("seamless," "millions of customers") with zero go-live date, volume commitment, corridor list, or economics — classic silence on the numbers that would prove the integration is live rather than a signed MOU.
3. **Concentration / commoditization of the rails.** OpenPayd's own client list (eToro, Kraken, OKX, RedotPay) shows the same rails serving competing wallets — RedotPay gets no exclusivity or differentiation, and any margin the deal saves is available to rivals on the same stack.

**What this changes (idea-lens).** `(analysis)` Reinforces a barbell forming in stablecoin payments: a few licensed rails aggregators (OpenPayd, Clear Junction, Ripple/Rail) underneath many consumer wallets — value migrating to the regulated middle, not the app. Falsifiable thesis: if this holds, expect further wallet-picks-rails deals and eventually rails consolidation/M&A; it's wrong if a scaled wallet like RedotPay vertically integrates by acquiring an EMI/IBAN license itself (its Series B explicitly earmarks capital for "strategic acquisitions" and licensing — the trigger to watch).

Sources: https://chainwire.org/2026/06/30/redotpay-selects-openpayd-to-strengthen-global-stablecoin-payment-infrastructure-for-millions-of-customers/ · https://ibsintelligence.com/ibsi-news/redotpay-selects-openpayd-for-global-payments/ · https://www.redotpay.com/news/redotpay-raises-us107m-in-series-b-to-drive-stablecoin-payments-adoption-globally · https://www.coindesk.com/markets/2025/12/16/hong-kong-s-redotpay-raises-over-usd100-million-series-b-to-push-stablecoin-payments-globally · https://www.bvp.com/atlas/stablecoins-from-defi-primitive-to-global-financial-infrastructure · https://www.coindesk.com/business/2026/04/27/cross-border-b2b-stablecoin-payments-to-rise-by-over-37-000-to-usd5t-by-2035 · https://tracxn.com/d/companies/openpayd/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
