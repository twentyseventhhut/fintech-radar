---
title: "Kalshi launches Pro product for high-frequency traders"
date: 2026-07-14
retrieved: 2026-07-14
tags:
  - company/kalshi
  - industry/trading
  - industry/capital-markets
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/1b417643
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s5719f622
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Kalshi launches Pro product for high-frequency traders

> [!info] 2026-07-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Kalshi launches ‘Pro’ product for users trading multiple markets. Kalshi Pro is designed for speculators who trade multiple markets at the same time and move with speed during live events. The platform is also designed to support those who run resting orders, trades that don’t execute until certain prices are met.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/1b417643>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Kalshi launches 'Pro' product for high-frequency traders
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 13 Jul 2026 Kalshi launched **Kalshi Pro** (pro.kalshi.com) — a browser-based "advanced trading terminal", **free and in public beta**. It is NOT a new asset class or a new market; it is a **desk-grade front-end + workflow layer** on top of the existing CFTC-regulated exchange, aimed at users who trade many markets at once and move fast during live events.
De-PR'd feature list (CNBC / Kalshi newsroom / Yahoo / QZ):
- **Canvas**: multiple markets side-by-side, each with own order book/chart/order panel, saved as layouts.
- **Resting-order management** desk-style: sortable/filterable order tables, inline amends, batch cancel, bulk edits, drag-to-reprice a resting order directly on the book.
- **Active-markets screener** across ~2,000 markets ranked by price/spread/depth/rolling 5-min volume; a continuous **trade tape**.
- **Perps tooling**: "terminal-grade" charting + risk management for the crypto perpetual-futures product (which crossed $1B volume within a week of its June launch; >$100M in first 24h).
- **Why structured this way**: this is the retail→exchange pivot made visible. Kalshi already courts Susquehanna/Jump/FalconX [[Kalshi courts Susquehanna and Jump Trading as prediction market hedging tool]]; a "Bloomberg-terminal-for-prediction-markets" (CNBC first flagged the build 4 Jun 2026) is the retention/upsell layer that keeps high-frequency taker flow — the volume that drives its revenue — inside Kalshi rather than routed via third-party API tooling. Note: **the API/FIX 4.4 rails already existed**; Pro is the GUI, not new connectivity. → the real question is not "new capability" but "does a free terminal defend the pro/HFT wallet share that underwrites the $22–40B valuation".

## [1] Competitors / peers
- **Polymarket** — the direct rival. Kalshi overtook it on US taker volume in Apr 2026 ($5.42B vs $1.99B) [[Kalshi holds 91% of US prediction market, BofA data shows]]; combined two-platform monthly volume hit ~$44.8B in Jun 2026 (The Block). Polymarket is crypto/offshore-rooted, bought CFTC-licensed QCX+QC Clearing ($112M, Jul 2025) to re-enter the US as "Polymarket US" — but it has no comparable pro-terminal announced.
- **Robinhood** — distributes prediction-market contracts (via a JV / futures exchange) and hit 9B contracts / 1M users [[Robinhood prediction market hits 9 billion contracts, 1M users]]; a distribution rival, not a terminal rival.
- **Incumbent analogue = Bloomberg/CQG/Trading Technologies** in real derivatives. Pro is Kalshi importing that UX. Position: **ahead within prediction markets** (first mover on a pro terminal), **catching up** vs mature futures-terminal ecosystems.
- **+ Second-order**: Kalshi's ~91% US share (BofA) means the terminal's job is less to win share than to **deepen monetisation per pro user** and lock liquidity providers in. The moat is the order book's liquidity, not the GUI — a competitor could clone the UI; it cannot clone 91% of the flow.

## [2] Company history / fit
Trajectory: $185M @ $2B (Jun 2025) → $1B @ $11B (Jan 2026) → $1B @ $22B Series F (Apr–May 2026) → reportedly in talks at **~$40B** (Jun 2026) [[Kalshi in talks to raise at $40 billion valuation]], with **>$2B annualised revenue** and early IPO talk (late 2027/2028) [[Kalshi passes $2 billion annualised revenue, in early IPO talks]]. Expansion into sports (~80% of volume since Jul 2024), crypto perps (with Coinbase), and institutional margin/hedging. **+ Why**: a take-rate business on contract volume needs a durable, defensible flywheel to justify a software-like multiple; building exchange infrastructure (terminal, FIX, perps, institutional onboarding) is how it argues it is "an exchange", not "a betting app" — the framing that supports a $22–40B mark.

## [3] Novelty / value-add / traction
Genuinely new **for prediction markets** (first pro terminal in the category), but **not novel in trading tech** — Canvas/screener/tape/drag-to-reprice are table stakes on any real derivatives terminal. Traction caveat: it is **beta and free** — zero disclosed adoption, no pro-user count, no revenue attribution. The value-add is **retention + monetisation of existing HFT/market-maker flow**, not new-user acquisition. **+ Who captures the margin**: Kalshi keeps taker fees (0.07·p·(1−p), ~1.75% peak at 50¢) and can steer maker rebates/volume tiers to designated market makers — the terminal is a lever to keep those makers quoting on Kalshi's book. Margin stays with Kalshi only as long as it owns the liquidity; the GUI itself is commoditisable and given away free.

## [4] What's next / market sentiment
Expect: paid/institutional tiers layered on the free beta, tighter FIX/perps integration, and use as an IPO-narrative asset ("full-service financial exchange"). Sentiment is bullish on Kalshi's volume lead and valuation ramp. **Regulatory backdrop is the real swing factor**: Kalshi is CFTC-regulated (DCM since 2021), but the **CFTC has proposed rules limiting sports/event contracts**, multiple states (Minnesota ban; Massachusetts, tribal suits) and countries (Brazil, Spain, India) have moved against it. Since ~80% of volume is sports, a pro terminal is exposed to the same regulatory tail as the underlying markets. **+ Counterintuitive**: the more Kalshi looks like a "real exchange" (terminal, perps, institutions), the more it invites exchange-grade scrutiny — professionalisation is both the valuation story and a regulatory magnet.

## Sources
- CNBC, 13 Jul 2026 — Kalshi launches 'Pro' product / perpetual futures: https://www.cnbc.com/2026/07/13/kalshi-launches-pro-product-for-users-trading-multiple-markets-at-same-time-perpetual-futures.html
- Kalshi newsroom — Advanced Trading Terminal: https://news.kalshi.com/p/kalshi-pro-trading-terminal
- Yahoo Finance / QZ — pro trading terminal launch: https://finance.yahoo.com/markets/options/articles/kalshi-launches-pro-trading-terminal-121813373.html | https://qz.com/kalshi-pro-trading-terminal-prediction-markets-071326
- CNBC, 4 Jun 2026 — "Bloomberg Terminal for prediction markets" (earlier report of the build): https://www.cnbc.com/2026/06/04/kalshi-is-building-a-bloomberg-terminal-for-prediction-markets.html
- Fee schedule / market-maker program: https://kalshi.com/docs/kalshi-fee-schedule.pdf | https://help.kalshi.com/en/articles/13823819-how-to-become-a-market-maker-on-kalshi
- Volume/share: https://news.bitcoin.com/prediction-market-traders-push-april-2026-volume-to-8-6b-kalshi-takes-the-lead/ | https://www.pewresearch.org/short-reads/2026/05/27/trading-volume-on-prediction-markets-has-soared-in-recent-months/
- CFTC proposed limits: https://www.espn.com/espn/betting/story/_/id/49019930/cftc-proposes-rules-limiting-prediction-markets-kalshi-sports
- Internal: [[Kalshi in talks to raise at $40 billion valuation]] · [[Kalshi passes $2 billion annualised revenue, in early IPO talks]] · [[Kalshi holds 91% of US prediction market, BofA data shows]] · [[Kalshi courts Susquehanna and Jump Trading as prediction market hedging tool]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is it really new?** As a *product for prediction markets* — yes (first pro terminal). As *trading technology* — no: Canvas, screener, trade tape, drag-to-reprice are standard on any real derivatives terminal. Answer: incremental, not category-defining.
2. **Announced or launched?** Launched and public — but **beta and free** (pro.kalshi.com). No GA, no paid tier disclosed. → "live-in-beta", not "monetised".
3. **Duplicate of the June "Bloomberg-terminal" report?** No — CNBC on 4 Jun 2026 reported Kalshi was *building* it (unnamed source, rumor); this is the *actual launch* on 13 Jul. Genuine "build → ship" follow-up = fresh, not a re-run. (Not in corpus as a separate note.)
4. **What traction is disclosed?** None. No pro-user count, no share of volume from Pro, no revenue lift. Open.
5. **Who captures the margin?** Kalshi keeps taker fees (~1.75% peak at 50¢) + steers maker rebates/volume tiers. The GUI is free and clonable; the moat is the ~91%-share order book, not the terminal. Terminal ≠ moat.
6. **Does a free terminal add value or defend a wallet?** Almost certainly a **retention/defence** play for existing HFT + market-maker flow, not a new-user funnel. Open whether it converts to paid revenue.
7. **What's silent?** Pricing/monetisation of Pro, latency/co-location specifics, whether FIX/perps risk tools are gated to institutions, adoption numbers. All open.
8. **Regulatory tail?** Large: CFTC proposed limits on sports/event contracts; ~80% of Kalshi volume is sports; state bans (Minnesota) and country blocks (Brazil, Spain, India). Professionalising the front-end doesn't reduce this — arguably raises scrutiny.
9. **Mechanism delta vs a real futures terminal (one sentence)?** Same UX primitives, applied to CFTC event contracts + crypto perps instead of listed futures — a UI port, not a new mechanism.
10. **Does this move the valuation ($22–40B) thesis?** Marginally — it supports the "full-service exchange, not a betting app" narrative that underwrites the multiple, but it adds no disclosed revenue yet.
11. **Polymarket counter?** No comparable pro terminal announced; Polymarket is rebuilding US access (QCX/QC Clearing). Kalshi is ahead on pro tooling and US volume lead (Apr 2026).
12. **What breaks it?** (a) CFTC/state restrictions shrinking the tradable sports book; (b) makers not needing the GUI (they use FIX/API directly) → terminal underused; (c) a rival matching UX once liquidity fragments.
13. **Why free?** To maximise adoption/lock-in before an IPO narrative; monetisation deferred to institutional tiers. Hypothesis.
14. **Second-order:** the more Kalshi looks like a real exchange, the more it invites exchange-grade regulation — professionalisation is both the bull case and a risk magnet.
15. **Net weight?** A meaningful-but-incremental step in a well-covered high-momentum story; not a standalone thesis-changer.

**Importance: 3/5** — a real, dated, shipped product from a category leader in a hot sector, and a clean "build→launch" follow-up to the June report; but it is a free beta GUI over pre-existing API/FIX rails, with zero disclosed traction and no direct revenue impact, so it is a supporting data point in the Kalshi story rather than a top-tier event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-14]] (2026-07-14).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Prediction / event-contract markets are mid-transition from retail political-betting curiosity to a partly-institutionalised derivatives venue. Kalshi Pro (public beta 2026-07-13) is the "professionalization" layer: a desktop workstation with multi-market view, live screener, contract-level order books, resting/limit orders and a TradingView-charted perpetuals interface — built explicitly for high-frequency, multi-market speculators (CNBC, Yahoo Finance, 2026-07-13). "Why now": three drivers converge — (i) an institutional-liquidity ramp (Susquehanna, Jump Trading, FalconX exploring hedging trades; institutional volume +800% over six months to early May-2026, per [[Kalshi courts Susquehanna and Jump Trading as prediction market hedging tool]]); (ii) a fresh perpetual-futures product line (first US-regulated crypto perps, BTCPERP live 2026-06-03; ~$16.1bn cumulative volume by early July, Kalshi seeking to extend to FX/metals/energy — Reuters/DeFi Rate); (iii) a firming CFTC framework (267-page NPRM issued 2026-06-10 that would *allow* most sports event contracts; comments due 2026-07-27). No standalone TAM for prediction markets is verifiable — "no data"; sized instead by volume run-rate (below).

**Competitive landscape.** Sector KPIs: monthly notional volume, take rate (~1.1% implied), institutional-volume share, and now (for Pro/perps) order-book depth & API/latency. Two-player US structure: **Kalshi** (CFTC-registered DCM, US-regulated leader — 91% US prediction-market share per BofA, [[Kalshi holds 91% of US prediction market, BofA data shows]]) vs **Polymarket** (crypto-native, offshore + rebuilding US access). Recent dated moves: Kalshi June-2026 volume $31.5bn (+87.4% MoM) vs Polymarket ~$10.26bn — combined ~$44.8bn, +75% MoM on World Cup (The Block, 2026-06); crypto perps live June-3; Pro terminal live July-13. Protagonist position: **ahead** on regulation, US share and now product surface. Moat = regulatory status (CFTC DCM) + network-effect liquidity (deepest US order books) + switching costs once HFTs/market-makers wire up to Pro's API — the Pro launch deliberately deepens the last two `(analysis)`.

**Comps & multiples.** Kalshi is private → market-cap multiples are round valuations, not EV. Arithmetic on the $2bn annualised run-rate ([[Kalshi passes $2 billion annualised revenue, in early IPO talks]]):
- **Kalshi:** ~$40bn target round / ~$2.0bn run-rate revenue = **~20x revenue** (round valuation, not market cap; run-rate annualises a seasonal peak).
- **Polymarket:** ~$15bn round / volume ~half of Kalshi's → the ~$25bn gap is priced on US-regulatory standing, not proportional volume; **revenue not disclosed → multiple = no data**.
- **DraftKings / Flutter (FanDuel):** listed sports-betting comps trade ~**3–5x sales** (per prior enrichment) — a ~4–7x gap to Kalshi's ~20x that only holds if Kalshi is an "exchange," not "sports gambling."
- **Exchange comps (CME/ICE/Coinbase):** the bull frame; unvalidated at this regulatory certainty → qualitative only.
Distribution not computed (only one revenue figure is public). Flag: **~20x run-rate is rich vs the gambling comp set** but defensible *only* if the exchange/derivatives reclassification (which Pro + perps are engineered to support) survives regulation.

**Risk flags.**
1. **Regulatory binary (highest).** ~80–90% of volume is sports contracts (Pew: 80% of Kalshi volume since Jul-2024; CRS ~90% year-to-Feb-2026). The 2026-06-10 NPRM *permits* most sports contracts but would **prohibit** injury/officiating/single-play/sub-collegiate markets — a live rulemaking (comments 2026-07-27) that could trim the very high-velocity, in-play markets Pro is built to serve. Second-order: shrinks the HFT product's addressable volume.
2. **Product-mix / self-cannibalization on take rate.** Pro courts market-makers and HFTs whose rebated/incentivised flow inflates volume but earns thin/negative take — professionalising the book can *lower* blended take rate even as notional rises.
3. **Valuation stretch.** ~20x run-rate + 8x valuation jump in <12 months invites a markdown if growth or regulation disappoints; Pro/perps are partly a narrative underpin for the concurrent ~$40bn raise.
4. **Execution / operational risk.** An HFT-grade terminal + perps raises the bar on latency, matching-engine reliability and market-surveillance; an outage or manipulation episode during a live event is now reputationally costlier.

**What this changes (idea-lens).** `(analysis)` Kalshi Pro + perps is the concrete step in re-rating prediction markets from "regulated sportsbook" toward "new derivatives exchange" — the explicit bet behind the exchange-multiple (~20x) rather than gambling-multiple (~3–5x) valuation. Falsifiable thesis: if the CFTC final rule (post-2026-07-27 comments) preserves in-play/sports contracts AND institutional/perp volume keeps compounding, the ~$40bn round closes and the exchange framing holds; **what breaks it** — a rule that carves out high-velocity in-play markets, or evidence that Pro/perp volume is predominantly incentivised market-maker flow rather than organic demand. Watch: CFTC final rule; Pro/perps volume disclosed *net* of rebates; Polymarket US relaunch compressing take rates.

Sources: https://www.cnbc.com/2026/07/13/kalshi-launches-pro-product-for-users-trading-multiple-markets-at-same-time-perpetual-futures.html · https://finance.yahoo.com/markets/options/articles/kalshi-launches-pro-trading-terminal-121813373.html · https://www.theblock.co/post/406983/kalshi-polymarket-volume-45-billion · https://defirate.com/news/polymarket-eyes-15b-valuation-gap-with-kalshi-widens/ · https://www.ropesgray.com/en/insights/alerts/2026/06/rewriting-the-rulebook-cftc-proposes-rule-changes-for-prediction-market-contracts · https://www.federalregister.gov/documents/2026/06/12/2026-11854/prediction-markets-public-interest-determinations · https://cryptobriefing.com/kalshi-crypto-perpetual-futures-us-launch/ · https://www.investing.com/news/stock-market-news/exclusivekalshi-in-talks-with-regulators-to-expand-neverexpiring-derivatives-to-new-areas-4783252
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
