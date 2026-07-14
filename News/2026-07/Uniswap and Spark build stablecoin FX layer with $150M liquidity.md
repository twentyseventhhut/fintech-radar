---
title: "Uniswap and Spark build stablecoin FX layer with $150M liquidity"
date: 2026-07-14
retrieved: 2026-07-14
tags:
  - company/uniswap
  - company/spark
  - industry/stablecoins
  - industry/defi
  - region/global
  - type/product
sources:
  - https://substack.com/redirect/64802819-60df-46e1-af22-bbb6301ed3ce
  - https://substack.com/redirect/ad444a4c-7058-43a4-97ba-c328d15f873d
status: enriched
n_mentions: 2
channels:
  - "lex"
story_id: s446c7a8b
month: 2026-07
enriched: true
importance: 2
freshness: stale
duplicate_of: [[Uniswap and Spark aim to build stablecoin FX market]]
---

# Uniswap and Spark build stablecoin FX layer with $150M liquidity

> [!info] 2026-07-14 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: lex

## Агрегированный текст (из дайджестов)

[lex] Uniswap, Spark aim to build stablecoin FX market as banks, fintechs enter the industry - CoinDesk

[lex] Spark, Uniswap build stablecoin ‘FX Layer’ seeded with $150 million liquidity migration - The Block

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/64802819-60df-46e1-af22-bbb6301ed3ce>
- <https://substack.com/redirect/ad444a4c-7058-43a4-97ba-c328d15f873d>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Uniswap and Spark build stablecoin FX layer with $150M liquidity
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS VERDICT: STALE — DUPLICATE of [[Uniswap and Spark aim to build stablecoin FX market]] (2026-06-29, story sc5995f7c).** This July-14 item (CoinDesk + The Block headlines, via lex) is a re-report of the SAME announcement already enriched in the corpus: the **2026-06-25** migration of **~$150M into two Uniswap v4 pools (USDS/USDT and USDS/PYUSD)** seeding a shared "Stablecoin FX Layer" by Spark/Sky. Same $150M, same partners, same "FX Layer" framing — the exact two source outlets (CoinDesk "aim to build...as banks, fintechs enter", The Block "$150M liquidity migration") that already fed the June note. Not a new event. Kept below only as a differential vs the prior note.

## [0] What exactly happened (de-PR'd)
Nothing new here versus the June 29 note. Re-run of the 2026-06-25 launch: Spark (Sky/ex-MakerDAO subDAO) migrated ~$150M into two USDS-paired Uniswap v4 pools (USDS/USDT, USDS/PYUSD) on Ethereum mainnet, branded a "Stablecoin FX Layer." The two headline mechanisms — a **Shared Liquidity Layer** and the **DualPool hook** (idle pool capital routed to approved yield until needed for trades) — remain **future phases** pending a separate security review; unshipped.
- **Only genuinely-newer wrinkle (NOT in this note's text, surfaced only by external research):** on **2026-07-08** Uniswap wired Sky's **LitePSM** (gas-optimized Peg Stability Module) into its routing engine so trades auto-route through fixed-rate PSM swaps (USDS/USDC/DAI/USDT/PYUSD) when cheaper than the pool curve — a real incremental step, plus a Sky governance proposal to raise the USDC PSM buffer $400M→$800M. **But this July-14 note does not report LitePSM** — its aggregated text is verbatim the June 25 CoinDesk/The Block story. So the note itself carries no fresh development.
- **Why it recurs:** the lex newsletter re-surfaced the ~3-week-old story; the ingestion pipeline created a second note off different-source retellings of the identical event. Classic reprint → stale.

## [1] Competitors / peers
Unchanged from the prior note. Onchain stable-pair swap depth is a mature, contested market: **Curve** (StableSwap gold standard; also launched CHF/USD "FXSwap" onchain-FX Dec 2025 and has live EURe pools — i.e. ahead on actual non-USD FX), **Fluid** (overtook Uniswap on stablecoin volume, ~55% share, >$1.4B deposits), **Circle EURC/USDC** (owns the euro-stablecoin supply any real "FX" leg needs), **Stripe/Bridge** (off-chain-orchestrated cross-border FX). Position: Uniswap/Spark are catching up on depth and BEHIND Curve on real non-USD FX; their edge is v4 hooks + the Sky balance sheet.

## [2] Company history / fit
Unchanged. Spark = Sky's capital-allocator subDAO (~$12.6B combined TVL May 2026); this is its stablecoin-bootstrapping playbook one rung up — from scaling a single coin via SparkLend ([[PayPal's PYUSD stablecoin reaches $1B market cap via Spark]], Sep–Oct 2025) to operating a shared multi-stablecoin exchange rail, with USDS as the intended numeraire. Uniswap's institutional/onchain-FX push: [[Anchorage Digital adopts Uniswap API for institutional DeFi access]], [[BlackRock explores DeFi move via Uniswap protocol integration]], [[Uniswap Labs partners Revolut for fast crypto onramp]]. Adjacent DeFi-stablecoin context: [[lex Curve and Maker launch new stablecoin and lending products]].

## [3] Novelty / value-add / traction
No new value-add or traction data versus the June note. The differentiating piece (DualPool yield-on-idle-capital hook) is still unshipped; no published volume/fee/TVL-utilization for the two pools. $150M is ~1% of Spark's own TVL and modest vs Curve/Fluid depth. As a NEWS item this July-14 note adds zero incremental substance — it is the same seed, re-headlined.

## [4] What's next / market sentiment
Same watch-items as the prior note (DualPool + Shared Liquidity Layer shipping; non-USD legs actually onboarding; sustained pool volume vs Curve). Additional external tell: the Sky USDC-PSM buffer vote ($400M→$800M) and whether LitePSM routing (Jul 8) measurably improves slippage. Central question is unchanged: can Spark make USDS the neutral numeraire vs the entrenched USDC/Curve Schelling point — which $150M alone does not settle.

## Sources
- **PRIMARY (duplicate target):** [[Uniswap and Spark aim to build stablecoin FX market]] — full [0]–[4] enrichment of the same 2026-06-25 event.
- CoinDesk, 2026-06-25: https://www.coindesk.com/business/2026/06/25/uniswap-spark-aim-to-build-stablecoin-fx-market-as-banks-fintechs-enter-the-industry
- The Block: https://www.theblock.co/post/406154/spark-uniswap-build-stablecoin-fx-layer-seeded-with-150-million-liquidity-migration
- The Defiant: https://thedefiant.io/news/defi/spark-uniswap-sky-150m-usds-uniswap-v4-stablecoin-fx-layer
- Official Spark post: https://paragraph.com/@spark-11/spark-uniswap-and-sky-building-the-fx-layer-for-stablecoins
- LitePSM routing (2026-07-08, external only, not in this note): https://cryptobriefing.com/litepsm-uniswap-stablecoin-fx-layer/
- Curve FXSwap CHF/USD (Dec 2025): https://news.curve.finance/curve-2025-year-in-review/
- Internal: [[PayPal's PYUSD stablecoin reaches $1B market cap via Spark]], [[lex Curve and Maker launch new stablecoin and lending products]], [[Anchorage Digital adopts Uniswap API for institutional DeFi access]], [[BlackRock explores DeFi move via Uniswap protocol integration]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **Is this a new event or a duplicate?** DUPLICATE. Same 2026-06-25 launch already enriched as [[Uniswap and Spark aim to build stablecoin FX market]] (sc5995f7c). Same $150M, same USDS/USDT + USDS/PYUSD v4 pools, same partners. Stale.
2. **Does the July-14 note carry any development the June note lacks?** No. Its aggregated text is verbatim the June 25 CoinDesk/The Block headlines. The only genuinely newer item (LitePSM routing, 2026-07-08) is NOT reported in this note — surfaced only by external research.
3. **Is it really "FX"?** Mostly no. All three live assets (USDS, USDT, PYUSD) are USD stablecoins; "FX" is aspirational until a non-USD leg (EUR/GBP) onboards. Answered: overstated.
4. **Announced or launched?** The $150M migration + two pools are LIVE (since 2026-06-25). The differentiating DualPool hook + Shared Liquidity Layer are future phases, pending separate audit. Unshipped.
5. **Is the $150M third-party money or Spark's own?** Almost certainly Spark/Sky reserve / Liquidity-Layer capital (protocol-owned, deployed), not independent market makers. Exact plumbing unconfirmed.
6. **Any committed non-USD stablecoin issuer?** No — euro consortium, RLUSD, etc. are prospects only. Answered: none.
7. **How does it beat Curve, which shipped CHF/USD "FXSwap" Dec 2025 and has live EURe pools?** It doesn't yet on real non-USD FX; Uniswap's bet is v4 hooks + Sky balance sheet. Currently behind on actual FX. Answered.
8. **Traction numbers (pool volume, TVL retention, fees, slippage)?** None published. Open.
9. **Who captures the margin?** Stable-pair fees ~1 bp → swap fees alone don't pay; economics ride the unshipped yield-on-idle-capital layer (Spark/Sky). Uniswap gets TVL + fee optics. Answered.
10. **Uniswap Labs or Foundation?** Coverage says "Uniswap"; no clean Labs-vs-Foundation attribution. Practically a v4 protocol deployment by Spark with Uniswap co-marketing. Partly open.
11. **New partnership or activation of an old relationship?** New branding on a long-standing Maker/Sky-on-Uniswap relationship; no prior formal structured Uniswap–Spark deal found. Answered.
12. **Why USDS as the hub, not USDC?** Both pools USDS-paired → Spark wants USDS as numeraire; risk that USDC/Curve are the incumbent Schelling point issuers resist. Open.
13. **Real motive?** Yield + peg support + distribution for USDS, plus a Uniswap v4/hooks flagship — under a neutral "infrastructure" label. Answered.
14. **Is the $56.6T-by-2030 cross-border TAM credible?** Promotional forecast, uncited to a rigorous source. Treat as marketing. Skeptical.
15. **Given the duplicate, should this publish?** No — mark stale, drop before publish; the June 29 note is the canonical record. If anything is worth a fresh note it is the 2026-07-08 LitePSM routing integration, which this note does not actually cover.

Importance: 2/5 — Real underlying event but STALE: an exact re-report of the 2026-06-25 Spark/Uniswap $150M FX-Layer launch already fully enriched as [[Uniswap and Spark aim to build stablecoin FX market]]. No new terms, no new reporting period, no new figures in this note's text; the differentiating yield hook is still unshipped and the newer LitePSM step is absent here. Duplicate, not a standalone story.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Note:** this is the same event ([lex] re-report) as the June pick [[Uniswap and Spark aim to build stablecoin FX market]] (story sc5995f7c, already enriched [0]–[4]). That note has the de-PR'd facts, competitor map and company-fit. Below = a sector/comps LAYER only, plus 3 weeks of fresh traction unavailable in June.

**Sector & drivers.** Onchain stablecoin FX is the conversion of one fiat-denominated stablecoin into another via smart-contract AMM/RFQ, settling in seconds vs correspondent-banking T+2. Sizing anchors: total stablecoin supply ~$315.3bn (DeFiLlama, per web, 5-Jun-2026; USDT ~$187bn, USDC ~$76bn); stablecoins settled ~$7.2tn in Feb-2026, first time above US ACH — but only ~$350–550bn of 2025's $28–62tn throughput was real-economy payments, the rest exchange/wallet routing (per OpenFX/Plasma via web). Reference: traditional FX turns ~$7.5tn/day (BIS 2022) — so onchain FX is a rounding error today but structurally the fastest-growing routing layer. **Structure:** the swap curve itself is commoditized — stable-pair spreads run ~1–3 bps on deep venues (per eco.com), fees compressed toward ~1 bp; value has migrated OFF the curve to (a) which asset is the hub/numeraire and (b) capturing yield on idle pool capital. **Why now:** GENIUS Act-era US momentum is pulling banks/fintechs/payment firms into stablecoin issuance (corpus: [[Circle unveils Arc, a Layer 1 blockchain built for stablecoins]], [[MetaMask launches mUSD stablecoin with M0 and Bridge]], [[Western Union to launch Solana-based stablecoin]]), so a neutral "route between hundreds of stablecoins" rail has a real, growing addressable base.

**Competitive landscape.** Sector KPIs: pool depth / slippage-on-size, fee (bps), and — the differentiator here — idle-capital yield capture. Key players: **Curve** (StableSwap incumbent; still handles the majority of onchain stable volume in 2026 despite TVL slipping to ~$2.2bn, per web); **Fluid** (surpassed Uniswap on stablecoin volume across ETH/Base/Arbitrum/Polygon, ~55% share, >$1.4bn deposits, per DL News via web — the direct threat to this exact niche); **1inch / Eco Routes** (SME/cross-chain aggregation); RFQ aggregators + OTC desks for institutional size. Basis of competition = depth/price for the marginal trader, NOT brand. **Recent move (fresh, post-June):** in the first 30 days after the 25-Jun launch Spark ran ~$1.5bn of stablecoin volume through the two Uniswap v4 pools (Cryptobriefing, via web) — and the **DualPool** yield hook (idle pool capital → short-rate strategies) has now moved from roadmap to launched (Crypto-Economy, via web), i.e. the "unshipped" piece flagged in June is now live. **Protagonist position:** catching up on raw depth (Curve/Fluid deeper), but ahead on design if DualPool holds — moat = Sky's captive multi-billion balance sheet to seed depth cheaply + USDS as numeraire; but it is a *rented* moat (marginal flow follows best price), not owned.

**Comps & multiples.** No round/valuation attached to this news — both are protocols, not equity events; classic EV/Revenue-style trading comps = **no data / N/A**. Comparability is on protocol traction, not multiples:
- FX Layer: ~$150M seed → ~$1.5bn volume / 30d (~10x monthly turn) — real, but modest vs Curve/Fluid depth and trivial vs Spark's own ~$12bn+ TVL (June enrichment).
- Fluid: ~55% stablecoin DEX share, >$1.4bn deposits (per web).
- Curve: ~$2.2bn TVL, still majority of onchain stable volume (per web).
- Internal comps: [[PayPal's PYUSD stablecoin reaches $1B market cap via Spark]] (Spark's stablecoin-bootstrapping playbook precedent); [[Anchorage Digital adopts Uniswap API for institutional DeFi access]], [[BlackRock explores DeFi move via Uniswap protocol integration]], [[Uniswap Labs partners Revolut for fast crypto onramp]] (Uniswap institutional-FX positioning). Note the current pools are USD-only (USDS/USDT/USDS/PYUSD) — the non-USD "FX" (EUR stablecoins like [[Euro stablecoin consortium Qivalis expands to 37 banks]], [[Bancomat announces EUR-BANK euro stablecoin in Italy]]) is thesis, not yet in the pools. Distribution not computed (metrics not comparable). Flag: traction *in-line to encouraging* for a 30-day-old venue; not yet a threat to incumbent depth.

**Risk flags.**
1. **Competitive disintermediation** — Curve (incumbent depth) and Fluid (~55% share, capital-efficient smart-collateral) already own the niche; stable-pair fees ~1 bp mean the swap layer alone can't earn its keep, so the whole thesis rests on DualPool yield holding traders/LPs. Second-order: if depth stays behind, flow routes to Curve/Fluid and the $150M seed is stranded optics.
2. **Yield-hook attack surface / run dynamic** — now that DualPool is LIVE, idle pool capital is deployed to external yield strategies; a strategy impairment or de-peg during a trade spike is a new smart-contract + liquidity-withdrawal risk that a plain AMM doesn't carry. Second-order: a single bad strategy could turn a "capital-efficient" pool into a run.
3. **USDS-centric numeraire vs USDC Schelling point** — both live pools are USDS-paired; issuers preferring USDC neutrality (the current default hub) may not route through USDS, capping the "shared layer" to Sky's own orbit. Regulatory treatment of an onchain "FX market" is also untested.

**What this changes (idea-lens) (analysis).** The bet is not "is onchain stable-FX real" (it is) but "can Spark make USDS the neutral numeraire when USDC/Curve are already the Schelling point." Falsifiable thesis: watch whether a *third-party* (non-Sky) issuer plugs a new pair into the FX Layer, and whether monthly volume compounds past the ~$1.5bn/30d run-rate toward Curve/Fluid territory — that would confirm a genuine shared rail vs a Sky-captive treasury deployment. Trigger to watch: DualPool yield performance through the next stress/de-peg event; a strategy loss would break the thesis outright.

Sources: https://cryptobriefing.com/spark-stablecoin-volume-uniswap-v4/ · https://crypto-economy.com/spark-and-uniswap-launch-dualpool-a-yield-generating-stablecoin-fx-layer/ · https://www.theblock.co/post/406154/spark-uniswap-build-stablecoin-fx-layer-seeded-with-150-million-liquidity-migration · https://eco.com/support/en/articles/15483234-what-is-onchain-fx-stablecoin-currency-conversion · https://www.openfx.com/stablecoins-cross-border-payments-report-2026 · https://defillama.com/stablecoins · https://baltex.io/blog/ecosystem/curve-finance-review-best-stablecoin-swaps-2026
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
