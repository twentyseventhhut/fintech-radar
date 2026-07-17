---
title: "Wollette and Yapily partner for automated wallet top-ups"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - company/yapily
  - company/wollette
  - industry/open-banking
  - industry/payments
  - region/uk
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/2f2bf40a
  - https://www.connectingthedotsinfin.tech/r/8ba440f2
  - https://www.connectingthedotsinfin.tech/r/76686c48
  - https://www.connectingthedotsinfin.tech/r/5bdcc3b0
status: enriched
n_mentions: 3
channels:
  - "Connecting the Dots in Fintech"
story_id: s43b22ed6
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Wollette and Yapily partner for automated wallet top-ups

> [!info] 2026-07-17 · 3 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] Yapily and Wollette Want to Make Wallet Top-Ups Disappear

[Connecting the Dots in Fintech] That's why the partnership between Wollette and Yapily caught my attention.

[Connecting the Dots in Fintech] 🇬🇧 Wollette and Yapily partner to power automated wallet funding through open banking. The integration enables customers to automatically fund their wallets from their bank accounts, supporting seamless account-to-account payments for online and in-store purchases while reducing payment friction for merchants.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/2f2bf40a>
- <https://www.connectingthedotsinfin.tech/r/8ba440f2>
- <https://www.connectingthedotsinfin.tech/r/76686c48>
- <https://www.connectingthedotsinfin.tech/r/5bdcc3b0>

## Контекст

<!-- enrichment:context -->
**[0] What exactly happened (de-PR'd, ~2026-07-15).** Wollette — a UK "integrated commerce" startup — integrated **Yapily**'s open-banking infrastructure to automate funding of the WollettePay wallet. The mechanism is specifically **sweeping VRP** (Variable Recurring Payments): a customer authorises a standing consent so that when the wallet balance falls below a **customer-defined threshold**, funds are swept automatically from their own bank account into the WollettePay wallet — no manual top-up per transaction. The same flow extends online via Wollette's **pay-by-link**, giving merchants one A2A rail across in-store + online. Wollette's wallet is pitched as interest-bearing (save + spend). Source: Open Banking Expo, FF News (Jul 2026); Yapily is an Event Partner of Open Banking Expo UK & Europe 2026 (13–14 Oct, London) — i.e. this is partly event-timed PR.
**Why structured this way / what it reveals:** the choice of **sweeping VRP is load-bearing and under-reported**. Sweeping VRP is the FREE, "me-to-me" flavour of open banking (moving your own money between your own accounts) — it sits OUTSIDE the new commercial-VRP (cVRP) / UKPI pricing scheme that went live 2 Jun 2026 (see [[Connecting the Dots on variable recurring payments and open banking]]). So Wollette funds the WALLET via free sweeping, then the actual merchant PURCHASE happens from the pre-funded wallet balance — sidestepping cVRP per-transaction scheme fees. This is the real trick: it recreates a "card-on-file / stored-value" UX on rails that are currently zero-marginal-cost to the consumer, rather than paying to initiate an A2A payment at each checkout.

**[1] Competitors / peers.** Same wallet-top-up-via-open-banking pattern already showcased by Yapily with **Pleo** (expense wallets funded by open banking — Yapily's own case study). Direct A2A / pay-by-bank checkout rivals: **Volt** (see [[Volt launches stablecoin checkout for Profee transfers]]), **TrueLayer**, **GoCardless** (Pay by Bank + Direct Debit; see [[Sage and GoCardless add Pay by Bank for small businesses]]), **Token.io**, **Tink** (Visa). On the wallet-issuer side Wollette competes with any stored-value/BNPL-style wallet and ultimately with card-on-file (Visa/Mastercard). Position: **catching up / parity** on plumbing — nothing here is technically novel; sweeping VRP + PIS have existed for 2+ years. Wollette's edge is packaging (one-tap biometric UX + interest-bearing wallet), not infrastructure.
**Why the landscape is this way (2nd-order):** because merchant-facing cVRP still carries scheme fees and thin bank coverage in Wave 1, the fastest way to get "free A2A checkout" live TODAY is to fund a wallet with free sweeping and settle purchases off the balance. Expect more wallet issuers to adopt this arbitrage until cVRP e-commerce (Wave 2, H2 2026) makes direct-at-checkout A2A economically competitive — at which point the pre-funded-wallet detour loses its rationale.

**[2] Company history / fit.** Wollette launched **WollettePay** in June 2025 ("one-tap A2A / open banking", BusinessWire 12 Jun 2025), scheduled UK GA Q4 2025 and Europe Q1 2026. In **June 2025 it partnered Ordo** to power that exact wallet-funding journey (see [[Wollette partners Ordo to optimise account-to-account payments]]). This Yapily deal is therefore **another open-banking supplier for the same top-up function** — a swap or dual-sourcing away from / alongside Ordo, likely to gain Yapily's 2,000+-bank coverage and VRP tooling. Fits Wollette's need: a small issuer must ride a licensed PISP/AISP's rails rather than build its own.
**Why:** Wollette is not itself the FCA-regulated payment initiator; it needs an AISP/PISP partner. Trading up to Yapily (bigger bank coverage, first-mover on VRP) is the logical move for a startup trying to scale merchant acceptance.

**[3] Novelty / value-add / traction.** **Low genuine novelty.** Yapily has publicly demoed the identical "instant wallet top-ups via open banking" pattern (Pleo case study/webinar) before this. What's new is only the specific Wollette integration. **Traction: none disclosed** — no live merchant count, no wallet users, no top-up volumes, no GMV, no go-live date confirmed as production. It is a capability/partnership announcement.
**Why the value-add is thin (deeper):** the consumer benefit (auto-refill, no manual top-up) is real UX but the economic value hinges on avoiding fees — and that advantage is **regulatory-timing-dependent**: it works because sweeping VRP is free and cVRP e-commerce isn't live yet. Who captures margin? Yapily takes an infra fee; Wollette earns on wallet float/interest spread + merchant acceptance; the banks provide free sweeping today but could see that change. It is a clever fee-arbitrage wrapper, not a durable moat.

**[4] What's next / market sentiment.** UK open-banking payments are scaling (~36M tx/month, Juniper; 17.5M+ active connections, OBL — per [[Yapily brings bank account verification to Google Cloud in Europe]]). cVRP/UKPI went live 2 Jun 2026 with Wave 2 (e-commerce) expected H2 2026. Regulatory backdrop favours A2A. Risk: if/when cVRP e-commerce matures and prices sensibly, direct-at-checkout A2A may make the "pre-fund a wallet" step redundant; also sweeping VRP economics for banks could be revisited. Sentiment: incremental positive for open-banking-at-POS momentum, immaterial at market level.
**Why (2nd-order):** the counterintuitive read is that this deal is a symptom of cVRP NOT yet being cheap/broad enough for e-commerce — issuers route around the toll via free sweeping. As Wave 2 lands, the same partnerships may re-plumb to direct cVRP, and stored-value wallets become one option among many rather than the workaround of necessity.

_Internal DB note: `sem search` unavailable (LanceDB 'notes' table not built — known issue); grep fallback over News/ used. Cited priors: [[Wollette partners Ordo to optimise account-to-account payments]] (same wallet-funding function, June 2025, Ordo), [[Connecting the Dots on variable recurring payments and open banking]] (sweeping vs commercial VRP, UKPI), [[Yapily brings bank account verification to Google Cloud in Europe]] (Yapily scale/coverage, Jul 2026), [[Volt launches stablecoin checkout for Profee transfers]] / [[Sage and GoCardless add Pay by Bank for small businesses]] (A2A-checkout peers)._
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Is it really new? Only partly. Wollette already had an open-banking wallet-funding partner — **Ordo (June 2025)**. This is a swap/addition to Yapily for the SAME WollettePay top-up function, not a first-of-kind. Fresh as a distinct partner+mechanism story, but not a new capability.
2. What exactly is the mechanism? **Sweeping VRP** — me-to-me auto-transfer from the user's bank account to their wallet when balance drops below a threshold. This is the FREE flavour of VRP, outside the cVRP/UKPI priced scheme. Don't conflate with commercial VRP.
3. Why sweeping and not cVRP at checkout? Because sweeping is zero-marginal-cost to the consumer and cVRP e-commerce isn't live yet (Wave 2, H2 2026). The deal is effectively a **fee-arbitrage** — fund a wallet for free, spend from balance. That's the real story.
4. Is it live? Unknown — no go-live date, no production confirmation. Treat as announced, not live.
5. Any adoption metrics? None. No merchant count, wallet users, top-up volumes, GMV, or conversion figures. Pure capability PR.
6. Is Ordo dropped or dual-sourced? Not stated. Open whether Yapily replaces or supplements Ordo.
7. Who is Wollette, really? A small UK "integrated commerce" startup; WollettePay launched Jun 2025 (BusinessWire), UK GA targeted Q4 2025, Europe Q1 2026. Not FCA-regulated as the initiator — rides Yapily's PISP/AISP rails.
8. Economics / who captures margin? Undisclosed. Yapily earns infra fees; Wollette earns on wallet float/interest + merchant acceptance. No pricing shared.
9. Is the "interest-bearing wallet" claim substantiated? Stated by Wollette in coverage; rate, provider of yield, and regulatory status of the interest are not detailed. Open.
10. Novelty vs Yapily's own prior work? Low — Yapily has publicly demoed identical "instant wallet top-ups via open banking" with **Pleo**. Wollette is another logo on an existing pattern.
11. Bank coverage / reliability? Depends on Yapily's ~2,000-bank / 19-market estimate and sweeping-VRP support per bank; uneven coverage can undercut the "always funded" promise. Open.
12. Fraud / liability? A2A pull via sweeping shifts UX to biometric auth (Wollette claim); liability model for mis-sweeps or APP-fraud on funded wallets not addressed.
13. Durability of the advantage? Timing-dependent: if cVRP e-commerce (Wave 2) prices competitively, the pre-funded-wallet detour may lose its rationale. The moat is a regulatory window, not tech.
14. Source quality? Vendor/event PR (Open Banking Expo, FF News), Yapily is an Open Banking Expo 2026 Event Partner — event-timed. Single-origin press-release framing.
15. Is this a duplicate of the Ordo note? No — different partner (Yapily), added specificity (sweeping VRP + pay-by-link). Fresh, but explicitly a continuation of the [[Wollette partners Ordo to optimise account-to-account payments]] thread.

**Importance: 2/5 — rationale.** A real but small partnership: no disclosed traction, no economics, capability already demoed by Yapily with Pleo, and Wollette already had an equivalent Ordo deal a year prior. The one genuinely interesting angle is the **sweeping-VRP fee-arbitrage** (fund wallet free, sidestep cVRP checkout fees) — a useful signal about how open-banking-at-POS is routing around unfinished cVRP economics — but the deal itself is a minor logo swap with no proven adoption. Notable for open-banking watchers, low broad-market weight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** UK open-banking A2A payments, VRP subsegment. VRP now ~16% of open-banking transactions and ~5.5m payments/month in the UK, "much of the growth through sweeping VRPs" (per The Payments Association, state of UK open banking 2026). Cards still dominate: ~84% of UK retail spend by turnover, ~£1.5bn/yr in fees via the Visa/Mastercard near-duopoly (per GoCardless, 2 Jun 2026 — [[GoCardless launches Recurring Pay by Bank on UKPI rails]]). Structure: infrastructure layer (aggregators: Yapily, TrueLayer, Tink, Token.io) is consolidating around a few players; the merchant-facing layer (Wollette, Pleo) is fragmented and rides on top. "Why now": the crucial nuance — this deal uses **sweeping VRPs** (me-to-me: a consumer topping up their OWN Wollette wallet from their OWN bank account), which have been live and fee-free since 2022, NOT the new commercial VRP (cVRP) that only went live 2 Jun 2026 under the UK Payments Initiative (UKPI) scheme (Wave 1 regulated sectors; Wave 2 general e-commerce H2-2026, per FCA/Lewis Silkin). So Wollette gets automated funding today without waiting on cVRP economics — a pragmatic architecture, not a cVRP land-grab.

**Competitive landscape.** Sector KPIs: A2A payment volume/TPV, conversion/auth rate, cost-per-transaction vs cards, bank coverage (Yapily cites 2,000+ banks across 19 countries). Two distinct competitive planes:
- Infra/aggregator (Yapily's plane): TrueLayer (Europe's largest Pay-by-Bank network, 20m users, +1m/month, VRP growth 12% vs 10% market in Oct-2025 — [[TrueLayer hits 20 million users as Pay by Bank adoption grows]]), Tink (Visa-owned), Token.io, GoCardless, Plaid. Basis of competition: bank coverage, reliability/auth rate, price. Yapily is a mid-scale challenger here (raised $51m Series B, $69m total, ~140 staff — per FintechFutures/CB Insights), positioned catching-up vs TrueLayer's scale; recent momentum from the Google bank-account-verification win ([[Yapily signs Google for bank account verification]]).
- Merchant checkout (Wollette's plane): Wollette is a small UK commerce/wallet startup (WollettePay launched Q4-2025). Notably it earlier chose **Ordo** to power WollettePay A2A (per Open Banking Expo/Finextra, Jun 2025); this Yapily deal is specifically for the sweeping-VRP wallet-funding leg — so Wollette is multi-rail, and Yapily's win here is a component mandate, not the whole payment stack. `(analysis)`

Recent peer moves: TrueLayer Bank on File recurring Pay-by-Bank live Jun-2026 with Trading 212/IG/InvestEngine ([[TrueLayer launches Bank on File recurring Pay by Bank at Money20 20]]); Modulr commercial VRP Jun-2026 ([[Modulr launches commercial Variable Recurring Payments]]); GoCardless Recurring Pay-by-Bank on UKPI. Protagonist position: Yapily = niche/catching-up challenger; moat is thin (switching costs + bank-integration coverage), not scale.

**Comps & multiples.** No valuation/round/metrics attached to THIS partnership → deal multiples "no data". Peer funding context (round valuations, not market caps): Yapily — $69m total raised, last disclosed Series B $51m (Sapphire Ventures); post-money valuation not publicly disclosed → `[UNSOURCED]`. TrueLayer — larger, private, latest valuation not verified here → `[UNSOURCED]`. Tink — acquired by Visa (2021/2022) for ~$2.1bn `[UNSOURCED for current]`. No revenue/ARR disclosed for Yapily or Wollette → EV/Rev, P/S not computable, distribution not computed. Internal comps (A2A/VRP, UK): [[TrueLayer hits 20 million users as Pay by Bank adoption grows]], [[GoCardless launches Recurring Pay by Bank on UKPI rails]], [[TrueLayer launches Bank on File recurring Pay by Bank at Money20 20]], [[Modulr launches commercial Variable Recurring Payments]].

**Risk flags.**
1. **Aggregator disintermediation / commoditisation.** Yapily supplies only the funding rail; Wollette already uses Ordo for other legs and could swap providers cheaply. Open-banking infra is increasingly a low-margin, coverage-and-price game where TrueLayer's scale (20m users, +1m/mo) compounds — Yapily risks being the interchangeable pipe. Why: value migrates to whoever owns the merchant/consumer relationship, not the API layer.
2. **Adoption/economics unproven for the merchant.** Announced integration, not disclosed live volume, auth rates or cost savings. Sweeping VRP is free today, but the consumer-facing top-up UX (bank-selection + biometric consent, friction, failed-payment fallback) determines whether it actually displaces cards. Why: A2A's card-displacement thesis dies on conversion, not on rail cost.
3. **Regulatory/scheme dependence for the NEXT step.** The wallet model works on sweeping VRP now, but scaling to true merchant checkout depends on cVRP/UKPI economics (access-fee pricing still being finalised; FCA/PSR declined a CA98 probe "at this stage"). Why: if cVRP pricing lands high, the card-cost advantage that justifies A2A narrows.

**What this changes (idea-lens).** `(analysis)` Small, incremental proof-point that sweeping VRP is being productised for wallet top-ups ahead of cVRP maturity — an interim architecture, not a re-rating. Watch: (a) whether Wollette discloses live top-up volume / card-displacement %, (b) whether Yapily converts point wins (Google, Wollette) into a durable VRP share vs TrueLayer, (c) Wave 2 cVRP go-live (H2-2026) as the real catalyst for A2A e-commerce. Thesis breaks if TrueLayer/GoCardless bundle sweeping+commercial VRP and squeeze mid-scale aggregators like Yapily on price and coverage.

Sources: https://www.openbankingexpo.com/news/wollette-partners-with-yapily-to-enable-sweeping-vrps-for-wallet-funding/ · https://thepaymentsassociation.org/article/the-state-of-open-banking-payments-in-the-uk-in-2026/ · https://www.fca.org.uk/news/statements/open-banking-launch-uk-payments-initiative-scheme · https://www.fintechfutures.com/open-banking/open-banking-fintech-yapily-lands-51m-series-b-funding · https://www.cbinsights.com/company/yapily · https://www.openbankingexpo.com/news/wollette-partners-with-ordo-to-power-wollettepay/ · https://truelayer.com/blog/recurring-payments/what-does-2026-hold-for-vrp/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
