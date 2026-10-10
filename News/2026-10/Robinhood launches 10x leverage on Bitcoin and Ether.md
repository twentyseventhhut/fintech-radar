---
title: "Robinhood launches 10x leverage on Bitcoin and Ether"
date: 2026-10-06
retrieved: 2026-10-08
tags:
  - company/robinhood
  - industry/crypto
  - industry/trading
  - region/us
  - type/product
sources:
  - https://pluang.com/en/news-feed/robinhood-perkenalkan-leverage-10x-bitcoin-ether-dampak-pasar-liquidasi-478-juta
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sd16bf1d0
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Robinhood launches 10x leverage on Bitcoin and Ether

> [!info] 2026-10-06 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Robinhood has launched 10x leverage on Bitcoin and Ether, introducing new perpetual futures contracts for U.S. traders. The launch follows a $478 million crypto liquidation event and lets traders control larger positions with less capital. Robinhood also plans to offer weekend trading for select stocks and ETFs in early 2027, pending regulatory approval.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://pluang.com/en/news-feed/robinhood-perkenalkan-leverage-10x-bitcoin-ether-dampak-pasar-liquidasi-478-juta>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Robinhood launches 10x leverage on Bitcoin and Ether
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
At its HOOD Summit (Houston, **Sept 29–30, 2026**) Robinhood **announced** US crypto perpetual futures — up to **10x** on BTC/ETH and **3x** on six altcoins (SOL, XRP, DOGE, ADA, LINK, HYPE) — offered via **Robinhood Derivatives LLC** (a CFTC-registered FCM / NFA member) with **Bitstamp supplying the matching/perp engine**. Promo fee: **0.01% (1 bp)** per trade through end-2026 (half Coinbase's 0.02%). Contracts never expire, P&L settles every ~15 minutes, 24/7, with liquidation alerts and stop-loss/take-profit.
- **"Launches" is premature → this is an announcement, not a live launch.** As of the summit the product was "coming months" with **no firm trading date, and no disclosed listing DCM** (an FCM is an intermediary, not an exchange). Flag `open`: has any US customer actually traded a Robinhood perp? → Why it matters: the headline frames a roadmap item as a shipped product; the aggregated digest text inherits that PR frame.
- **The "$478M liquidation event" is NOT caused by Robinhood.** It refers to ~**$487M in long liquidations** (24h total ~$556M) on **Oct 6, 2026** when BTC slid below ~$84k — broad-market deleveraging, not a Robinhood product failure (the product isn't live). → Why it matters: the timing is awkward optics — a 10x-leverage pitch landing days into a retail-long wipeout — but there is no causal link; do not conflate.

## [1] Competitors / peers
- **Coinbase** (Coinbase Financial Markets, CFTC/DCM): shipped US nano BTC/ETH "perpetual-style" perps up to **10x** at 0.02% on **Jul 21, 2025** — **~15 months ahead of Robinhood**. See [[Coinbase says it is building most complete trading platform]].
- **Kalshi (KalshiEX DCM)**: first CFTC-**approved** perp (BTCPERP) on **May 29, 2026** — the regulatory door-opener.
- **Kraken**: bought SmallExchange ($100M, Oct 2025) specifically to get a **DCM licence to run its own US perps** rather than route via others — see [[Kraken acquires exchange in $100M derivatives deal]]. Robinhood's open "which DCM?" question is exactly what Kraken bought its way around.
- **Hyperliquid** (offshore DEX, not US-retail legal): ~9% of global perp OI, ~70–80% of DEX perp volume by mid-2026. Robinhood will list **HYPE** perps — i.e. a perp on a perp-competitor's token.
- **Binance/OKX** (offshore, 50–125x): hold global liquidity; US-regulated 10x is tame by comparison.
→ **Position:** Robinhood is a **late follower, not an innovator** — cloning Coinbase's Jul-2025 model, differentiating on fee (1bp vs 2bp), token breadth (8 assets), and retail UX/distribution. → Why the gap closes slowly: ~90% of global derivatives volume sits offshore; US-regulated 10x competes on compliance/UX, not on leverage.

## [2] Company history / fit
Logical continuation of the Bitstamp-anchored crypto build: acquisition (~$200M, closed Jun 2025) → EU crypto perps **3x** live Jun 30 2025 → EU perps widened to 10x on commodities/FX ~mid-2026 → now the **same engine wrapped in a US FCM for 10x crypto perps**. Related: [[Robinhood hires Bitstamp's Nejc Bizjak for crypto strategy]] (talent to run this). Fits a broader "own-the-rails" push: Robinhood Chain L2, tokenized stocks, staking, prediction markets ([[Robinhood explores launching prediction markets outside US]]), and weekend stock/ETF trading slated early 2027. → Why: Robinhood is converting PFOF-dependent equities economics into higher-margin, 24/7 crypto/derivatives surfaces; leverage + funding + financing are richer take-rate lines than spot.

## [3] Novelty / value-add / traction
- **Real novelty is low.** Mechanism is not new (Coinbase shipped it 15 months earlier). Robinhood adds: lower promo fee, more altcoin perps, Bitstamp engine, retail reach. **Traction = zero so far** (not live; no volumes).
- **Who captures the margin? → open and decisive.** A 1-bp promo fee implies revenue must come from funding-rate spread, leverage financing, and/or Bitstamp fees, not the headline commission — and promo pricing expires Dec 2026. Real durable take-rate is undisclosed.
- **Funding mechanics ambiguity:** "P&L settled every 15 min" reads like an **interval cash-settled continuous future dressed as a perp**, not a classic offshore funding-rate perp — matters for basis/carry and whether arbs engage (analysis).

## [4] What's next / market sentiment
- **Regulatory durability is the swing factor.** **CME sued the CFTC (Jun 18, 2026)** arguing Kalshi-style perps are "swaps"; CFTC moved to dismiss Sep 2, 2026 — **unresolved**. A judicial loss could unsettle the whole onshore-perp framework Robinhood relies on. The CFTC also has a pending **ANPR on retail crypto leverage** that could cap leverage below 10x. → Second-order: Robinhood's 10x may be a headline number regulators force down before/after launch.
- **Jurisdiction tail:** BTC/ETH perps sit with CFTC; if SEC deems any of the six altcoins securities, part of the line could strand (open).
- **Sentiment:** incremental land-grab in a race Coinbase/Kraken already entered; the Oct 6 liquidation cascade underscores the retail-suitability/PR risk of selling 10x into volatile markets.

## Sources
- crypto.news — Robinhood plans 10x crypto perps for US traders: https://crypto.news/robinhood-plans-10x-crypto-perps-for-u-s-traders/
- blockhead.co — Robinhood brings leveraged crypto perps to US, AI agents: https://www.blockhead.co/2026/09/30/robinhood-brings-leveraged-crypto-perpetual-futures-to-us-customers-launches-ai-trading-agents/
- Robinhood newsroom (Jun 30 2025) — stock tokens, L2, EU perps/staking: https://robinhood.com/us/en/newsroom/robinhood-launches-stock-tokens-reveals-layer-2-blockchain-and-expands-crypto-suite-in-eu-and-us-with-perpetual-futures-and-staking
- Coinbase blog — US perpetual-style futures (Jul 21 2025): https://www.coinbase.com/blog/coming-july-21-us-perpetual-style-futures
- Proskauer — CFTC approves US-listed perpetual futures: https://www.proskauer.com/alert/opening-the-door-to-perps-the-cftc-approves-us-listed-perpetual-futures
- theblock.co — CFTC moves to dismiss CME suit (Sep 2 2026): https://www.theblock.co/news/regulation/2026-09-02-cftc-dismiss-cme-413416
- theblock.co — Bitcoin slides, long liquidations surge (Oct 6 2026): https://www.theblock.co/news/markets/2026-10-06-bitcoin-slides-crypto-long-liquidations-surge-417882
- Original item source: https://pluang.com/en/news-feed/robinhood-perkenalkan-leverage-10x-bitcoin-ether-dampak-pasar-liquidasi-478-juta
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is it actually live?** As of Sept 29–30 it was "coming months" with no date — has any US customer traded a Robinhood perp? → **Open; likely not live.** The digest "launches" framing is premature.
2. **Which DCM lists the contracts?** Robinhood Derivatives is an FCM (intermediary), not an exchange. Own DCM, Kalshi, or third party? → **Open, undisclosed** — determines order-book control and economics (Kraken bought SmallExchange precisely for this).
3. **Does the CME v. CFTC suit survive?** If a court reclassifies perps as "swaps," the onshore framework Robinhood depends on could be voided mid-rollout. → **Open; CFTC motion to dismiss pending (Sep 2026).**
4. **Who captures the margin?** 1-bp promo (half Coinbase) ends Dec 2026 — is revenue funding-rate spread, leverage financing, or Bitstamp fees? → **Open; real take-rate undisclosed.**
5. **Is 10x durable?** CFTC's pending retail-leverage ANPR could cap below 10x. → **Open; headline number at regulatory risk.**
6. **Genuine novelty?** Coinbase shipped the same CFTC-regulated perp model Jul 2025. What does Robinhood add beyond fee + more altcoins? → **Answer: little; late follower.**
7. **Adoption vs announcement:** US-regulated perps so far capture a sliver vs ~90% offshore/Hyperliquid volume — does 10x pull volume onshore or stay a rounding error? → **Open; no Robinhood traction yet.**
8. **Retail/PR risk:** 10x pitched days into a ~$487M long-liquidation cascade (Oct 6) — reputational/regulatory exposure if retail gets liquidated? → **Material; timing optics poor.**
9. **Funding mechanics:** True funding-rate perp, or 15-min interval cash-settled future dressed as a perp? → **Open; affects basis/carry and arb participation.**
10. **Cannibalization:** Do perps eat spot-crypto/options PFOF revenue or add incrementally? → **Open.**
11. **Bitstamp dependency:** EU 3x engine scaled to US 10x volume, surveillance, CFTC customer-protection/margin — operationally proven? → **Open.**
12. **Altcoin jurisdiction tail:** If SEC deems SOL/XRP/ADA etc. securities, does part of the line strand and stall the launch? → **Open.**
13. **Is this a duplicate?** No prior note covers Robinhood US crypto perps / 10x; closest are EU-era Bitstamp/prediction-market notes and competitor perps notes — distinct event. → **Fresh.**

**Importance: 3/5** — Materially relevant (large retail broker entering US-legal leveraged crypto derivatives, a structurally new US product category post-CFTC-2026), but discounted: it is an **announcement, not a live launch**, Robinhood is a **late follower to Coinbase (Jul 2025)**, mechanism is **not novel**, **zero traction**, and the whole framework hangs on an **unresolved CME v. CFTC suit** plus a pending leverage-cap rulemaking. Not a 4 (no live product, no differentiation beyond fee/tokens); not a 2 (the US retail-perp category and a top-3 retail broker's entry do matter).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-10]] (2026-10-10).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto perpetual futures ("perps") — leveraged, no-expiry derivatives that are the single largest category of crypto trading. Perps are ~80% of global crypto trading volume (per Coinbase, 2026-05-29); the market did >$60tn notional in 2025 (per Kraken blog, 2026-06-16) and >$300bn moves through perps on a typical day in 2026, with Q1'26 alone at ~$524.8bn (per datawallet.com, 2026). Structure: consolidated offshore-first — Binance ~55.7% share, Hyperliquid ~28.9%, CEXs still ~75–80% of flow but on-chain DEX perps have grown to >$1.2tn monthly (per Coinbase Institutional 2026 Outlook, via datawallet/yellow.com, 2026). Why now: the US has *just* opened onshore: the CFTC cleared the first US perps in late May 2026 (Kalshi's BTCPERP + a Coinbase no-action letter), followed by Kraken launching CFTC-regulated perps via Bitnomial on 2026-06-16 ([[Coinbase and Kalshi bring perpetual crypto futures to US]], [[Kraken launches CFTC-regulated perpetual futures in the US]]). Robinhood's 10x BTC/ETH launch (announced at its HOOD Summit 2026-09-29; 3x on SOL/XRP/DOGE/ADA/LINK/HYPE; 15-min PnL settlement; routed through Bitstamp; 0.01%/trade fee through end-2026 — per coincentral/cryptowisser, 2026-10) is Robinhood joining a land-grab for the newly-legal US retail-perps lane, not inventing a product.

**Competitive landscape.** Sector KPIs: notional derivatives/perp volume, funding-rate + transaction take rate, open interest, and crypto transaction revenue mix. Key players & basis of competition: offshore CEXs (Binance, Bybit) and DEXs (Hyperliquid) compete on liquidity/leverage/asset breadth; the *US-regulated* perps field is narrow and new — Kalshi (BTCPERP), Coinbase (global perps via Deribit/Bermuda FCM), Kraken (Bitnomial), and now Robinhood (via Bitstamp). Basis of competition onshore = distribution + regulatory access + retail UX, since the underlying contract is commoditized. Recent moves (dated): CFTC first approvals 2026-05-29; Kraken US perps 2026-06-16; Coinbase retail perps/options rollout mid-2026; Robinhood 10x BTC/ETH announced 2026-09-29. Position: Robinhood is a FAST FOLLOWER, not first-mover — behind Kalshi/Coinbase/Kraken onshore by ~3–4 months — but it brings the largest retail-brokerage distribution (27.4M funded customers, Q1'26 10-Q) and its Bitstamp acquisition as exchange infrastructure ([[Robinhood completes $200M Bitstamp acquisition]]). Moat = distribution/brand to retail, not product or switching costs (analysis).

**Comps & multiples (IR-grounded; PRIMARY = Robinhood's own filed results).**
- **Robinhood (HOOD) — latest filed quarter Q2'26 (ended 2026-06-30, results 2026-07-29), PREFERRED over the Q1 10-Q as newer:** total net revenues **$1.31bn** (+32% YoY, record), net income **$573M** (+48%), diluted EPS **$0.62**. Crypto transaction revenue **$100M (−38% YoY)** — the company's weakest line; **crypto notional volume $40bn** (of which $18bn on the Robinhood app + $22bn via Bitstamp). Event/prediction-market revenue **$156M** (>10x YoY) OVERTOOK crypto; options $342M (+29%); equities $129M (+95%) on $956bn equity notional. (per Robinhood Q2'26 release, investors.robinhood.com, 2026-07-29.)
- **Prior quarter for context (Q1'26 10-Q, filed 2026-04-29, hood-20260331.htm):** crypto revenue **$134M (−47% YoY** from $252M); total rev $1.067bn (+15%); transaction-based $623M; net income $346M; EPS $0.38.
- **Valuation:** HOOD market cap ~**$99–101bn** (2026-10-07/08, close $109.51 on 10-07; per stockanalysis/companiesmarketcap). P/S on annualized Q2'26 = $100bn / ($1.31bn × 4 = $5.24bn) = **~19x**. Rich vs the ~0.5–20x guide range, consistent with +32% top-line growth and +48% earnings — a growth premium the market is paying for the diversified, *non-crypto* mix (prediction markets + options + NII), NOT for crypto.
- **Internal comps (grep):** [[Coinbase and Kalshi bring perpetual crypto futures to US]], [[Kraken launches CFTC-regulated perpetual futures in the US]], [[Coinbase launches 24 7 stock perpetual futures]], [[The $12B hole in Coinbase and Robinhood's Q126 earnings]] (COIN ~6.9x vs HOOD ~23x P/S on Q1'26 — the gap has since narrowed to ~19x as HOOD revenue grew). Private peers (Binance/Bybit/Hyperliquid/Kraken): no clean public multiple → "no data". Forward/NTM multiples, clean EV/EBITDA → [UNSOURCED] (no free source).

**Risk flags.**
1. **Retail leverage → liquidation/consumer-harm + regulatory tail.** 10x perps on BTC/ETH for retail are among the riskiest instruments; the note's own framing cites a $478M crypto liquidation event as backdrop, and the CoinDesk/pymnts coverage notes ~$19bn of leveraged positions wiped out in minutes in a 2025 flash crash. The CFTC's perps framework is still no-action-letter/guidance, NOT a formal rule — it can be reversed by future agency leaders, and Robinhood is already under a Florida AG probe over crypto promotions ([[Robinhood crypto promotions probed by Florida attorney general]]). Second-order: a liquidation-driven retail blow-up invites exactly the "gambling/predatory leverage" narrative that could claw the framework back.
2. **Launching INTO a crypto downcycle, into its weakest line.** Robinhood's crypto revenue is −38% YoY and only ~$100M/qtr (Q2'26) — now smaller than prediction markets. Adding 10x leverage is a bid to re-stimulate a shrinking line; de-PR: the move signals crypto *volume* weakness as much as ambition, and 0.01% promo pricing through end-2026 means thin take-rate economics even if volumes come.
3. **Dependence on others' rails + fast-follower position.** Perps run through Bitstamp (Robinhood's own, but a bolt-on) and the whole onshore category is derivative of the CFTC's 2026 opening that Kalshi/Coinbase/Kraken reached first. Robinhood captures retail distribution but not the regulated-venue/clearing layer where Coinbase (Deribit/Bermuda) and Kraken (Bitnomial) have built infrastructure — margin risk if the value accrues to the venue layer.

**What this changes (idea-lens).** (analysis) This is a new-entry land-grab, not a re-rating event: the US retail-perps market opened in mid-2026 and Robinhood is racing to convert its 27M-customer funnel before Coinbase/Kraken lock in regulated-perps liquidity. Falsifiable thesis: perps meaningfully *re-accelerate* Robinhood's crypto line (reverse the −38% trend) within 2–3 quarters. Trigger/what to watch: Q3/Q4'26 crypto notional volume and crypto revenue (does $40bn/qtr inflect up?) and whether a leverage-driven liquidation event or CFTC/state regulatory action hits before the product scales — either would break the thesis and re-expose HOOD's ~19x multiple, which is underwritten by the *non-crypto* mix, not by crypto.

Sources: https://investors.robinhood.com/static-files/2f42ce10-59b7-4880-8371-7d52ede7c22e · https://www.sec.gov/Archives/edgar/data/1783879/000178387926000062/hood-20260331.htm · https://coincentral.com/robinhood-to-launch-crypto-perpetual-futures-and-weekend-stock-trading-for-us-users · https://www.cryptowisser.com/news/robinhood-to-offer-10x-leverage-crypto-perpetual-futures-in-us/ · https://www.datawallet.com/crypto/crypto-perpetual-futures-statistics · https://yellow.com/research/who-controls-crypto-300b-perpetuals-market · https://stockanalysis.com/stocks/hood/market-cap/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** BEAT · Q2 2026 (ended 2026-06-30, reported 2026-07-29) total net revenues $1.31bn (+32% YoY; vs public consensus ~$1.26bn, beat +$0.05bn / +3.5%) · GAAP diluted EPS $0.62 (vs ~$0.42 a yr ago; vs Zacks consensus $0.44, +40.9% surprise) — but EPS flattered by ~$0.14 of one-time non-cash gain on deconsolidation of Robinhood Ventures Fund I (underlying ~$0.48) · drivers: record equities/options/prediction-markets volumes, offset by a crypto slump · guidance: FY2026 adj opex+SBC range *lowered* to $2.675–2.775bn (from $2.7–2.825bn).

**Key figures (with growth).**
- Total net revenues $1.31bn, +32% YoY.
- Transaction-based revenues $776m, +44% YoY. Net interest revenues $389m, +9% YoY. Other revenues $143m, +54% YoY (Trump Account service revenues + Gold subscriptions).
- Net income (GAAP) $573m, +48% YoY. Adj EBITDA $741m, +35% YoY, 57% margin.
- Diluted EPS $0.62 GAAP (vs ~$0.42 prior yr); ~$0.14 is a one-off deconsolidation gain → ~$0.48 underlying.

**By segment / driver (transaction revenue mix).**
- Event/prediction-markets contracts $156m, up over 10x YoY — the new growth engine; 13.6bn contracts traded (>10x YoY).
- Options $342m, +29% YoY; 774m contracts, +50% YoY.
- Equities $129m, +95% YoY; equity notional $956bn, +85% YoY.
- **Cryptocurrencies $100m, −38% YoY** — the clear laggard. Robinhood-App crypto notional volume −35% YoY to $18bn (total crypto notional $40bn incl. $22bn Bitstamp). Crypto drag is the de-PR'd backdrop to this note's product news.

**Operating / platform metrics.** Total Platform Assets $369bn, +32% YoY (equity gains + net deposits, partly offset by lower crypto valuations). Net Deposits $21.7bn (28% annualized). Funded Customers 28.4m, +7% YoY; Investment accounts 29.9m, +9% YoY. Gold subscribers record 4.84m, +39% YoY.

**vs expectations / prior period.** Beat on both lines: revenue $1.31bn vs public consensus ~$1.26bn (Zacks; +3.5%); EPS $0.62 vs ~$0.44 (+40.9% surprise) — though the beat quality is diluted by the non-cash Ventures Fund gain, so the "clean" EPS beat is far narrower (~$0.48 vs $0.44). Sequential acceleration vs Q1 2026 (prior 10-Q, qtr ended 2026-03-31): revenue $1.067bn→$1.31bn; transaction revenue $623m→$776m; crypto transaction revenue $134m (Q1, −47% YoY)→$100m (Q2, −38% YoY) — crypto decline is moderating in % terms but still deeply negative. Event contracts $104m (Q1)→$156m (Q2). (No prior earnings note in corpus — irdb semantic search down, HTTP 402; figures taken from filings/IR + public aggregators.)

**Guidance / forward.** No revenue guidance given (not Robinhood's practice); the only hard guide is cost: FY2026 adjusted operating expenses + SBC *lowered* to $2.675–2.775bn (from $2.7–2.825bn) — a modest tightening that reads as cost discipline / operating-leverage confidence while top line runs hot. Management tone confident on diversification (prediction markets, equities, Gold, Trump Accounts); conspicuously quieter on the crypto revenue decline, leaning on Bitstamp/total-notional framing rather than the −35% App volume. HOOD shares sold off post-print despite the beat — market read the one-off gain and crypto softness, not the headline.

**Thesis-flags.**
1. Crypto is shrinking, not growing (−38% YoY rev; App notional −35% YoY) → this is WHY the note's 10x-leverage perps launch matters: it's a revenue-reacceleration lever on a declining segment, not a victory lap → second-order: leverage/perps raise take-rate and engagement but also raise liquidation/credit and regulatory-fraud-liability risk — watch whether crypto rev inflects in H2 2026.
2. Growth has decoupled from crypto → prediction markets (>10x), options (+29%), equities (+95%) now carry the model → de-risks the crypto drag but concentrates on event-contracts regulatory exposure.
3. Earnings quality: ~$0.14 of the $0.62 EPS is a non-cash deconsolidation gain → the real beat is modest; don't extrapolate the headline run-rate.
4. Cost guide lowered + 57% Adj-EBITDA margin → operating leverage intact; the swing factor for the thesis is top-line durability of new segments, not costs.

Sources: Q1 2026 10-Q (qtr ended 2026-03-31) https://www.sec.gov/Archives/edgar/data/1783879/000178387926000062/hood-20260331.htm · Q2 2026 release (2026-07-29) https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results · https://www.nasdaq.com/press-release/robinhood-reports-second-quarter-2026-results-2026-07-29 · consensus (Zacks, as of 2026-07-29) https://finance.yahoo.com/markets/stocks/articles/robinhood-markets-inc-hood-q2-212504312.html · one-off gain https://www.top1markets.com/news/robinhood-q2-2026-earnings-hood-reaction · irdb semsearch unavailable (HTTP 402).
<!-- /enrichment:earnings_review -->
