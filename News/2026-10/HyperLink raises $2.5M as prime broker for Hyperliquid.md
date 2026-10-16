---
title: "HyperLink raises $2.5M as prime broker for Hyperliquid"
date: 2026-10-10
retrieved: 2026-10-10
tags:
  - company/hyperlink
  - industry/crypto
  - industry/trading
  - region/global
  - type/funding
sources:
  - https://cryptorank.io/insights/deals/hyper-link-undisclosed-2026-10-04
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sc03017df
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# HyperLink raises $2.5M as prime broker for Hyperliquid

> [!info] 2026-10-10 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] HyperLink, a prime broker for decentralized trading platform Hyperliquid, raised $2.5 million in funding.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://cryptorank.io/insights/deals/hyper-link-undisclosed-2026-10-04>

## Контекст

<!-- enrichment:context -->
### [0] What exactly happened (de-PR'd)

On ~2026-10-04/05, **HyperLink** (`hyperlink_xyz`) closed a **$2.5M** round — undisclosed structure/valuation — from **Alliance, North Island Ventures, Reverie, Node Capital, Breed, and smartestmoney.hl**. Calling it a "prime broker" is generous: HyperLink is an **order-flow aggregator / broker front-end built on top of Hyperliquid's "builder codes"** (Hyperliquid's native mechanism that lets a third-party app attach a per-order fee and route user orders into the HL order book). HyperLink pools many traders' flow + HYPE staking to unlock **Hyperliquid's own volume-based VIP fee tiers** (Tier 0 →Tier 6, up to −47% fee discount; +40% via HYPE staking) that an individual trader couldn't reach alone, then packages that with "private trade flow" and "optimal execution." It is NOT prime brokerage in the TradFi sense — **no financing, no securities lending, no rehypothecation, no cross-venue custody**. It is single-venue (Hyperliquid only), **invite-only**, and claims **$254M notional routed last month ≈ 0.1% of Hyperliquid volume** (and ~1% of HL "builder" volume), with a stated goal of **10% of Hyperliquid volume**.

**Why structured this way / what it reveals:** the whole product is an **arbitrage of Hyperliquid's fee schedule** — VIP tiers reward aggregate volume, builder codes let a middleman capture 40–100% of HL fees and rebate up to 50% to users. HyperLink is essentially a **GPO/buying-club for taker fees** dressed in prime-broker language. The "$2.5M / 0.1% share" framing flatters: 0.1% of a $200B+/month venue is a real $254M, but the 10% target (≈$20B/month, a ~100x jump) is pure aspiration, not traction.

### [1] Competitors / peers

- **Hyperliquid itself** — the venue HyperLink rides on; also its single point of failure and the party that could change builder-code economics or launch a first-party VIP program.
- **Other Hyperliquid builders / front-ends** — pvp.trade, Dexari, Okto and the broader builder-code cohort (HypeFees/HypeData track them); HyperLink is one of many order-routers, not a category owner.
- **[[CRX Trade debuts Swiss institutional crypto prime brokerage]]** — launched days earlier (2026-10-05); genuinely multi-venue (Binance/Bybit/Gate/Hyperliquid/Deribit + CME/Nasdaq), tri-party custody, tokenised collateral. Same label, far broader product — HyperLink is the seed-stage, single-venue, retail-pro end of the same "crypto prime" theme.
- **[[Standard Chartered prepares crypto prime brokerage service]]**, FalconX, Ripple Prime (ex-Hidden Road, >$3tn/yr cleared), Coinbase Prime — the real balance-sheet primes offering financing/clearing. HyperLink shares the word, not the function.

**Why the landscape is this way (analysis):** "prime broker" has become a marketing label across wildly different models in 2026 — from StanChart's bank-grade financing to a Hyperliquid fee-aggregator. The term's inflation is itself the signal: HyperLink competes with other HL builders on fee-sharing and UX, not with primes on balance sheet.

### [2] Company history / fit

HyperLink is new and small; little public history beyond this round. Backers are crypto-native seed funds (Alliance accelerator, North Island, Reverie, Node Capital, Breed) plus an HL-native angel (smartestmoney.hl) — a syndicate signalling "bet on the Hyperliquid app layer," not institutional validation. **Why this bet:** Hyperliquid's dominance (see [3]) created a land-grab for its order flow — builder codes turned routing into a monetisable layer, and VCs are funding pick-and-shovel plays on top of the single fastest-growing perps venue. [[Trading startup Liquid raises $18 million seed round]] and [[TownSquare raises $16.25 million for Monad DeFi money market]] are adjacent "fund the DeFi-trading app layer" seed bets.

### [3] Novelty / value-add / traction

**Novelty:** low. Order-flow aggregation to unlock volume-tier discounts is an old TradFi idea (introducing brokers, GPOs); on Hyperliquid it's natively enabled by builder codes and already done by several builders. HyperLink's differentiator is execution/UX and a broker-style account, not a new primitive.

**Value-add — is it real? 1–2 levels deep:**
- Real, but thin and borrowed. The savings (VIP tiers + staking rebates) are **Hyperliquid's economics that HyperLink re-packages** — it captures margin only as the spread between HL's builder rebate and what it passes to users.
- **Who captures the margin:** Hyperliquid keeps the venue economics and controls the fee schedule; HyperLink is a disintermediable middle layer. If HL tightens builder-code terms, launches first-party aggregation, or a rival builder undercuts the fee split, HyperLink's edge evaporates. Classic **thin-moat distribution layer on someone else's rails** — the same structural risk as a card "dashboard" that doesn't own the payment.
- **Traction:** $254M/month routed = ~0.1% share. Invite-only. The 10% target is a ~100x leap with no disclosed path. Treat as aspiration, not adoption.

### [4] What's next / market sentiment

Near-term: scale invite-only flow, court larger/active traders, possibly layer financing/margin later to earn the "prime broker" label. Sentiment around the Hyperliquid app layer is hot — HYPE buybacks consume ~97% of protocol fees, and HL commands ~32% of all on-chain perps volume (up to ~44% of perp-DEX volume), ~$9B+ open interest, $200B+/month. **Why the market goes this way / second-order:** capital is flooding Hyperliquid-adjacent apps precisely because HL won the perp-DEX war — but that concentration makes every builder **a bet on one venue's goodwill**. The counterintuitive risk: HyperLink's fortunes are inversely hedged to Hyperliquid's incentive to keep builder economics generous; the stronger HL gets, the more it can squeeze its builders. Also regulatory: "prime broker" for a no-KYC offshore perps venue invites scrutiny if HyperLink onboards institutional/US flow.

### Sources
- https://www.gate.com/en-us/news/detail/hyperlink-completes-25m-funding-round-targets-10-of-hyperliquid-trading-17890770
- https://panews.io/articles/01a10745-d368-734a-b79c-237c9acc8862
- https://www.tokenpost.com/news/business/26670
- https://phemex.com/news/article/hyperliquid-broker-hyperlink-raises-25m-to-unlock-vip-fee-rates-98751
- https://cryptonews.net/news/market/33541037/
- https://hyperliquid-co.gitbook.io/wiki/architecture/hypercore/dex/clearinghouse/fees-builder-codes
- https://coinlaw.io/hyperliquid-statistics/
- https://cryptobriefing.com/hyperliquid-rwa-perps-44-percent-volume/
- https://cryptorank.io/insights/deals/hyper-link-undisclosed-2026-10-04
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions

1. Is this really "prime brokerage"? No financing, lending, rehypothecation or custody disclosed — it's a builder-code order-flow aggregator unlocking VIP fee tiers. The label is PR inflation. (answered: yes, mislabeled)
2. Where does the margin actually accrue? Hyperliquid controls the fee schedule and builder-code terms; HyperLink earns only the rebate spread it doesn't pass through → disintermediable middle layer. (open on durability)
3. Single-venue concentration: 100% dependent on Hyperliquid. What happens if HL changes builder economics, launches first-party aggregation, or de-prioritises builders as it scales? (open — existential)
4. Traction reality: $254M/month = ~0.1% of HL volume, invite-only. The 10% target is ~100x with no disclosed path. Is any of it durable or just a pitch number? (traction thin)
5. Round structure/valuation undisclosed — SAFE? priced? What dilution/terms behind the $2.5M headline? (open)
6. Who are the backers really betting on — HyperLink, or just "exposure to the Hyperliquid app layer"? Syndicate is crypto-native seed + an HL angel, not institutional validation. (analysis)
7. Competitive density among HL builders (pvp.trade, Dexari, Okto, etc.) — what stops a rival undercutting the fee split? Moat looks like UX only. (open)
8. Fee-split economics: HL builders can take 40–100% of HL fees and rebate ≤50% to users — what split does HyperLink run, and is the user saving real net of HyperLink's cut? (open)
9. "Private trade flow" — does aggregating/internalising order flow create conflicts (front-running, PFOF-style incentives) on a no-KYC venue? (open — governance risk)
10. Regulatory exposure: marketing "prime broker" to active/institutional traders on an offshore, no-KYC perps DEX — sanctions/market-access risk if it onboards US/EU flow. (open)
11. Is the savings proposition structurally stable, or does it compress as more flow concentrates and HL's own VIP tiers/first-party tools improve? (open)
12. Vs [[CRX Trade debuts Swiss institutional crypto prime brokerage]] and real primes (FalconX, Ripple Prime, StanChart): HyperLink shares the word, not the function — is it even the same market? (answered: different category)
13. HYPE-staking dependency: part of the pitch leans on HYPE staking discounts — how exposed is the model to HYPE price/tokenomics changes? (open)
14. Freshness: is this the same event as any prior note? No — distinct company and round; [[CRX Trade debuts Swiss institutional crypto prime brokerage]] is a different firm covered separately. (fresh)

**Importance: 2/5 — rationale:** A sub-$3M seed for an invite-only, single-venue (Hyperliquid-only) order-flow aggregator mislabeled as a "prime broker," routing ~0.1% of venue volume with no disclosed terms. Low novelty (builder-code fee-tier arbitrage already done by several HL builders), thin borrowed value-add, and a thin, disintermediable moat sitting on one venue's goodwill. Mildly interesting only as a signal of capital flooding the Hyperliquid app layer and of "prime broker" label inflation across crypto in 2026. Not market-moving.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto prime brokerage layered on a single perps-DEX venue. Hyperliquid is the dominant onchain perp venue — ~56% of all onchain perpetual-futures open interest and a record ~9.3% share of *global* perp OI (up from ~6.9% in May 2026), ~$7bn TVL, and cumulative protocol revenue crossing ~$1.4bn in early Oct 2026, ~$1.26bn of which was routed into HYPE buybacks (per DefiLlama / CryptoBriefing / coinlaw, as of Oct 2026). Structure: the "builder code" primitive lets third parties route user flow on top of Hyperliquid's shared liquidity and keep a cut of fees — builders had reportedly earned >$70m since Oct 2024 (per hypewatch, Mar 2026). This makes the broker layer a thin, permissionless toll-booth on someone else's order book rather than a venue in its own right — low capital barrier, but also low defensibility. Why now: Hyperliquid's OI/revenue scale has reached a point where fee-tiering and execution routing for pro traders is economically worth building; HyperLink is monetising the gap between retail builder apps and institutional prime brokers.

**Competitive landscape.** Sector KPIs: routed volume, share of venue volume, VIP/maker-taker fee capture, builder-fee rebate. HyperLink routed ~$254m last month ≈ 0.1% of Hyperliquid volume and ~1% of *builder* volume, and openly targets 10% of total Hyperliquid volume (per gate.com / tokenpost, Oct 2026) — i.e. it is tiny today and the thesis is entirely forward. Basis of competition: fee economics (aggregating flow + staking to unlock VIP tiers), private trade flow, and execution quality; invite-only, aimed at larger active traders. Position: niche new entrant **(analysis)** — a Hyperliquid-native aggregator/broker, not a multi-venue prime broker. Its "moat" is at best an aggregation/flow network effect that only works while it is the preferred builder; switching costs for traders are low. True institutional prime brokers (Hidden Road / Ripple Prime, FalconX, Standard Chartered's planned desk) compete on multi-asset clearing, credit and custody — a different, much larger game HyperLink does not play.

**Comps & multiples.** No valuation disclosed for the $2.5m round, so no entry multiple is computable — **no data** on EV/Revenue or price/volume. Scale framing only:
- HyperLink: ~$2.5m raised (seed/pre-seed; Alliance, North Island, Reverie, Node Capital, Breed), ~$254m/mo routed volume, undisclosed valuation.
- [[Trading startup Liquid raises $18 million seed round]] — leveraged-trading startup, $18m seed (May 2026): same "trading" subvertical, ~7x the raise; a sense of where a priced trading-infra seed can land.
- [[Ripple Prime secures $200 million facility from Neuberger]] — $200m *debt* facility for a multi-asset prime broker (May 2026): two orders of magnitude larger, institutional, multi-venue.
- [[Standard Chartered prepares crypto prime brokerage service]] — bank-grade prime brokerage build (Jan 2026): incumbent-balance-sheet comp.
- External: Ripple acquired prime broker Hidden Road for $1.25bn (closed Oct 2025), clearing >$3tn/yr across 300+ institutions (per CoinDesk/Ripple). FalconX has raised ~$427m across 8 rounds (per Tracxn).
Comparability is weak: HyperLink is a single-venue onchain flow-aggregator, the external names are multi-asset, credit-and-custody prime brokers. Distribution not computed, qualitative comparison only. In-line vs other early trading-infra seeds; dwarfed by every "prime broker" it is named against.

**Risk flags.**
1. **Single-venue dependency.** 100% of the business sits on Hyperliquid — any fee-schedule change, builder-code policy shift, or loss of Hyperliquid share erases HyperLink's entire TAM; it has no venue diversification and no own liquidity.
2. **Platform/governance & concentration risk.** Hyperliquid has a small validator set, an Arbitrum-bridge centralisation vector, and a precedent of discretionary intervention (the Mar-2025 JELLY force-settlement) (per hypewatch/wublockchain). A broker routing client flow inherits counterparty/settlement risk it cannot control.
3. **Regulatory / custody exposure.** Hyperliquid runs no KYC and operates without explicit approval in most jurisdictions; a "prime broker" offering VIP economics and private flow to active traders invites securities/derivatives and AML scrutiny, and the note is silent on custody — whether HyperLink ever controls client assets/keys is undisclosed, a material gap for a "prime broker" label.

**What this changes (idea-lens).** Confirms the builder-code layer is becoming investable as a business, not just a feature — expect more Hyperliquid-native brokers/aggregators chasing VIP-fee arbitrage **(analysis)**. Falsifiable thesis: if HyperLink's share climbs from ~0.1% toward even 2–3% of Hyperliquid volume within ~2 quarters, the "toll-booth on the dominant perp venue" model is real; if it stalls near current share, it is a feature a competing builder (or Hyperliquid itself) can commoditise. Trigger to watch: Hyperliquid builder-fee policy changes and whether a priced follow-on reveals a valuation.

Sources: https://www.gate.com/en-us/news/detail/hyperlink-completes-25m-funding-round-targets-10-of-hyperliquid-trading-17890770 · https://www.tokenpost.com/news/business/26670 · https://defillama.com/protocol/hyperliquid · https://cryptobriefing.com/hyperliquid-record-9-percent-perp-open-interest/ · https://coinlaw.io/hyperliquid-statistics/ · https://www.hypewatch.io/blog/hyperliquid-complete-guide-2026 · https://www.coindesk.com/business/2025/04/08/ripple-to-acquire-prime-broker-hidden-road-for-usd1-25b-expanding-institutional-push · https://tracxn.com/d/companies/falconx/__WtUU61ZGUsBxEgjFVWUawb62jY0KCOrEyb7seLY5_uE/funding-and-investors
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
