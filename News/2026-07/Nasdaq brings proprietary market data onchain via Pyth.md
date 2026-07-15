---
title: "Nasdaq brings proprietary market data onchain via Pyth"
date: 2026-07-14
retrieved: 2026-07-14
tags:
  - company/nasdaq
  - company/pyth
  - industry/blockchain
  - industry/capital-markets
  - region/us
  - type/product
sources:
  - https://substack.com/redirect/295da160-c5a4-4cc9-adec-e1c0176cf5a6
status: published
n_mentions: 1
channels:
  - "lex"
story_id: s449e9400
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Nasdaq brings proprietary market data onchain via Pyth

> [!info] 2026-07-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: lex

## Агрегированный текст (из дайджестов)

[lex] Nasdaq brings proprietary market data onchain through Pyth - CoinTelegraph

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/295da160-c5a4-4cc9-adec-e1c0176cf5a6>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Nasdaq brings proprietary market data onchain via Pyth
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **2026-06-30** (the 2026-07-14 digest item is a re-report), **Nasdaq selected Pyth Network** to distribute its flagship **TotalView** feed — full depth-of-book (every displayed order at every price level across Nasdaq-, NYSE- and regional-listed US equities) plus the **Net Order Imbalance Indicator (NOII)** — onto **Pyth's Data Marketplace**. Framed as the first time Nasdaq's proprietary depth-of-book feed reaches a blockchain distribution network, and Pyth as "the first onchain network to distribute Nasdaq data directly from the exchange." PYTH token popped ~6–8%.

**De-PR'd:** this is **announced, not confirmed live** — the load-bearing blanks are conspicuous: no launch date, **no chain list**, **no latency/update-frequency spec**, and **no commercial terms/pricing** disclosed. "Publishers retain control over data, attribution and commercial terms while Pyth handles distribution" (Mike Cahill, Douro Labs/Pyth) — i.e. Nasdaq is simply **one more publisher** slotting into the pre-existing **Pyth Data Marketplace** (launched 2026-04-09 with Euronext, Fidelity, Tradeweb, OTC Markets, SGX FX, EDI). This is an extension of an existing product, not a bespoke Nasdaq–Pyth alliance.

**+ Why structured this way:** Nasdaq gets a **new, zero-marginal-cost distribution channel** for its highest-margin asset (market data) without building oracle infra; Pyth gets a **marquee logo** to validate its Bloomberg/Refinitiv-disruption pitch. The "direct from the exchange" claim is the genuinely new/defensible part; "Wall Street order book on blockchain" is the PR overlay until the feed is demonstrably live and priced.

## [1] Competitors / peers
- **Chainlink** — the entrenched leader and, on exchange/institutional data, arguably **ahead**: **Deutsche Börse** (DataLink, Oct 2025, Eurex/Tradegate), **ICE** (FX + precious metals), **S&P Global**, WisdomTree; 2,400+ protocols, 40+ chains; also on the same US Commerce Dept economic-data deal. See [[Chainlink partners with Commerce Department to bring data on-chain]] (Sept 2025 — direct precedent: authoritative data onchain via oracle) and [[Robinhood Chain launches and adopts Chainlink for onchain access]] (July 2026).
- **Pyth** — pull-oracle, first-party publisher model, 120+ publishers; wins on **speed/authoritative first-party depth**. Nasdaq is Pyth **matching** Chainlink's exchange relationships, not leapfrogging.
- Smaller: RedStone, Chronicle, Edge.

**+ Why the lay of the land:** many teams use **both** (Pyth for low-latency price, Chainlink for conservative fallback/CCIP). The competitive prize is not a single price feed but becoming the **default authoritative-data rail for tokenized RWAs/equities** — a land-grab of exchange logos, which is exactly why both are racing to sign them.

## [2] Company history / fit
Nasdaq's market-data business is a high-margin, recurring-revenue jewel, and it has been **aggressively multiplying distribution channels** for it: [[Sahm Capital partners with Nasdaq for TotalView and investor education]] (Nov 2025, same TotalView feed into MENA retail), [[ZA Bank partners with Nasdaq to embed US stock data]] (Mar 2026, HK), [[Polymarket launches private-company prediction markets with Nasdaq data]] (May 2026, Nasdaq Private Market as resolution source). Parallel tokenization push: SEC-approved tokenized securities, Boerse Stuttgart, Kraken/Talos partnerships (Mar 2026).

**+ Why:** the structural logic is **channel maximization on a commodity-of-scale data asset** — every incremental venue (retail app, prediction market, DeFi protocol) is pure incremental margin on data Nasdaq already produces. Onchain is just the newest, lowest-friction distribution surface; TotalView specifically because it's the premium product tokenized-equity/perp venues actually need.

## [3] Novelty / value-add / traction
**What's genuinely new:** first exchange-native depth-of-book (TotalView + NOII) directly from Nasdaq onto an oracle network — not just last-sale/reference prices but **order-book microstructure**, which is what execution/liquidation modeling for tokenized equities and perps needs.
**Traction:** **zero disclosed** — announcement only, no live symbols, no consuming protocols named, no volume. Contrast with real precedent adoption where Pyth's US Commerce GDP data went live across ~9 chains (Aug 2025).

**+ Why value-add is real-but-unproven:** on Pyth's economics, **publishers keep commercial terms** and Pyth handles distribution, tying institutional revenue to the PYTH Reserve. So **where the margin sits is the open question**: if Nasdaq keeps pricing/attribution, Pyth risks being a low-margin **pipe** (a "dashboard, not the one who gets paid"); if consumers pay Pyth Pro subscriptions, Pyth captures the data-vendor margin. The Nasdaq-specific onchain revenue split is **undisclosed** — that blank, not the headline, decides whether this is material.

## [4] What's next / market sentiment
Watch for: (a) **go-live** with an actual chain list + latency spec; (b) named **consuming protocols** (tokenized-equity DEXs, perps, prediction markets); (c) whether scope **expands** beyond TotalView (Nasdaq Basic, indices, Nordic). Pyth continues its **$50B+ market-data TAM** assault (Pyth Pro $10k/mo tier, >$1M ARR reported; Data Marketplace). Sentiment: PYTH-positive; crypto media breathless.

**+ Second-order:** the tokenization/RWA tailwind means authoritative US-equity data onchain has **real structural demand** — but the counterintuitive risk is that **exchanges signing every oracle** (Nasdaq→Pyth, Deutsche Börse/ICE→Chainlink) **commoditizes the oracle layer itself**: if data is available everywhere, the durable margin flows back to the **data owners (exchanges)**, not the pipes. That reframes the central question from "which oracle wins" to "does the oracle ever capture more than pipe economics."

## Top challenge/extra questions (10–15, second-order)
1. Is it live? No — announced 2026-06-30, **no go-live date**. (open)
2. Which chains? **Undisclosed.** (open)
3. Latency/update frequency for TotalView onchain? **Undisclosed.** (open)
4. Commercial terms / who monetizes / revenue split Nasdaq↔Pyth? **Undisclosed** — the decisive blank. (open)
5. Is this a NEW Nasdaq–Pyth deal or activation of an older one? New; no prior Nasdaq-Pyth relationship. First tie-up.
6. Is it bespoke or just another Marketplace publisher? Latter — Data Marketplace (Apr 2026) framework.
7. Any named consuming protocol / actual demand signal? **None disclosed.** (open)
8. Does Chainlink already have bigger exchange wins? Yes — Deutsche Börse (DataLink) + ICE; Pyth is matching.
9. Scope beyond TotalView (Basic, indices, Nordic)? Not mentioned. (open)
10. Where does the margin sit — Nasdaq keeps terms → is Pyth a low-margin pipe? Likely pipe unless Pyth Pro subs capture it. (analysis)
11. Is "$100B+ TVS" real? Marketing figure; independent estimates far lower (~$6B Q3'25). (unverified)
12. Does depth-of-book (NOII) meaningfully beat last-sale feeds for onchain use? Yes for execution/liquidation modeling — the real value-add if live. (analysis)
13. Regulatory angle on redistributing exchange proprietary data onchain? Nasdaq controls attribution/licensing — likely why it retains commercial terms. (analysis)
14. Duplicate of any existing corpus note? No — no prior Nasdaq-Pyth note; closest is Chainlink-Commerce (different oracle/dataset).
15. What would make this a 4–5/5? Confirmed live across named chains + named consuming venues + disclosed economics. Currently 3/5.

## Sources
- CoinDesk 2026-06-30 "Nasdaq expands distribution of its market data into blockchain infrastructure"
- Cryptobriefing 2026-06-30 "Nasdaq blockchain market data distribution"
- TechTimes 2026-06-30 (TotalView / NOII scope)
- BusinessWire 2026-04-09 (Pyth Data Marketplace launch)
- BusinessWire 2025-09-23 (Pyth Pro launch, $50B TAM)
- CoinDesk / Pyth blog 2025-08-28 (US Commerce Dept GDP onchain)
- Deutsche Börse PR 2025-10 (Chainlink DataLink)
- Internal: [[Sahm Capital partners with Nasdaq for TotalView and investor education]], [[Chainlink partners with Commerce Department to bring data on-chain]], [[Polymarket launches private-company prediction markets with Nasdaq data]], [[ZA Bank partners with Nasdaq to embed US stock data]], [[Robinhood Chain launches and adopts Chainlink for onchain access]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is it live or just announced?** Announced 2026-06-30 only. No go-live date, no live symbols, no consuming protocols named. → treat as announcement, not adoption.
2. **Which blockchains does TotalView go to?** Undisclosed. Pyth's general reach is 50–100+ chains but the TotalView-specific list is open.
3. **What latency / update frequency onchain?** Undisclosed for TotalView. A depth-of-book feed's value hinges on this; the blank is material.
4. **What are the commercial terms and the Nasdaq↔Pyth revenue split?** Undisclosed. Publishers "retain commercial terms" — so who captures the margin is unresolved and decisive.
5. **New deal or re-report/activation?** Genuinely new signing (first Nasdaq–Pyth tie-up), but the digest item is a July re-report of the June 30 announcement.
6. **Bespoke alliance or just another Marketplace publisher?** The latter — Nasdaq slots into the pre-existing April-2026 Pyth Data Marketplace alongside Euronext, Fidelity, Tradeweb, etc.
7. **Has Chainlink already done bigger exchange deals?** Yes — Deutsche Börse (DataLink) and ICE; Pyth is matching, not leapfrogging.
8. **Is the "first onchain network to distribute Nasdaq data directly" claim defensible?** Appears so — no prior Nasdaq oracle-distribution deal found. That's the genuinely novel part.
9. **Any real demand signal / named consuming venue?** None disclosed. Pure supply-side announcement.
10. **Is "$100B+ TVS" credible?** Marketing figure; independent estimates far lower (~$6B, Q3'25). Unverified.
11. **Does depth-of-book (TotalView + NOII) beat last-sale feeds for onchain use?** Yes — for tokenized-equity/perp execution and liquidation modeling, if it goes live.
12. **Where does the durable margin sit — oracle or exchange?** Likely the exchange (data owner); the oracle risks pipe economics as every exchange signs every oracle. (analysis)
13. **Does this duplicate an existing corpus note?** No — closest are Chainlink-Commerce Dept (different oracle/dataset) and Nasdaq-Sahm/Polymarket (different, non-onchain channels).
14. **Regulatory/licensing angle?** Nasdaq controls attribution/licensing of proprietary data — plausibly why it retains commercial terms while Pyth only distributes. (analysis)
15. **What would upgrade this to 4–5/5?** Confirmed live across named chains + named consuming protocols + disclosed economics.

Importance: 3/5 — a marquee first (Nasdaq's proprietary TotalView depth-of-book onto an oracle network, direct from the exchange) with a genuine tokenization/RWA tailwind and clear strategic logic, but discounted because it is announced-not-live with every load-bearing detail undisclosed (chains, latency, economics), it is an extension of an existing Pyth Data Marketplace rather than a bespoke deal, and Chainlink already banked comparable/larger exchange wins (Deutsche Börse, ICE). Not a 4 until it is demonstrably live and priced.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-15]] (2026-07-15).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Blockchain-oracle / onchain-market-data: the layer that pipes off-chain prices and reference data into smart contracts. Two secular drivers converge here: (1) traditional exchanges monetizing proprietary data through a new distribution rail — Nasdaq's Data business sits in the Capital Access Platforms segment and is a high-margin recurring revenue stream (Nasdaq Q3 2025 net revenue ~$1.3bn/qtr, +13% YoY; Solutions ARR crossed $3bn — per Nasdaq IR, as of Q3 2025); (2) DeFi/RWA demand for institutional-grade feeds as perps, prediction markets and tokenized securities scale. "Why now": this follows the Aug 2025 US Commerce Department move to publish GDP/PCE macro data onchain via both Pyth and Chainlink (per CoinDesk/Pyth blog, as of 2025-08-28) — a government stamp that legitimized onchain data distribution and is now pulling private data owners (Nasdaq) onto the same rails. The scope so far: Nasdaq TotalView (full depth-of-book / order-imbalance feed) via Pyth's programmable interface — Pyth is the first onchain network to distribute Nasdaq data directly from the exchange (per CoinTelegraph/CryptoBriefing, 2026-07).

**Competitive landscape.** Oracle-sector KPIs: Total Value Secured (TVS), protocol integrations, chain coverage, feed latency. Two dominant players on different niches: **Chainlink** — ~68.9% oracle market share by TVS, 2,400+ projects, secures $30bn+ (per DefiLlama/CoinLaw, as of Dec 2025); the incumbent for spot/lending/CCIP cross-chain. **Pyth** — ~5.9% TVS share but the oracle-of-choice for perps/derivatives via low-latency first-party feeds, 100+ chains, ~305 protocols, Solana-native heritage (per Messari/RedStone, 2026). Basis of competition: data provenance (first-party publishers vs aggregated node network), latency, and — increasingly — exclusive data partnerships. Nasdaq's position: as a data *supplier* it is picking distribution rails, not competing; the news is Pyth winning an exclusive TotalView distribution deal, narrowing its data-quality gap vs Chainlink at the top of the stack. In-base precedent of the same playbook on the rival: [[Chainlink partners with Commerce Department to bring data on-chain]] and [[Robinhood Chain launches and adopts Chainlink for onchain access]] (2026-07).

**Comps & multiples.** No round/valuation/metrics in this note — it is a product/partnership, not a deal — so trading-comp multiples: **no data / not applicable** (Pyth is a protocol/token, not a disclosed-cap private raise; Nasdaq's data segment is not separately valued). Internal comps (same onchain-data / oracle theme in base, cite as precedent not multiples): [[Chainlink partners with Commerce Department to bring data on-chain]] (Sep 2025, US macro data onchain), [[Robinhood Chain launches and adopts Chainlink for onchain access]] (Jul 2026), [[Chainlink and banks launch Project Pangea for T+0 FX settlement]] (Jun 2026), [[Polymarket launches private-company prediction markets with Nasdaq data]] (May 2026 — Nasdaq data feeding a prediction market, the same demand vector this deal serves). Distribution not computed — qualitative comparison only.

**Risk flags.**
1. **Announcement vs adoption.** The deal is a distribution agreement for TotalView; there is no disclosed onchain integration count, no fee split, and no live consuming protocols named. Exchange-data revenue only materializes if DeFi/prediction-market apps actually license and pay for the feed — de-PR: neither party disclosed economics or exclusivity term length. Second-order: headline may be priced ahead of realized data revenue.
2. **Value captured by the oracle layer, not the exchange.** Pyth sits between Nasdaq and the end app. If onchain distribution scales, the oracle network (and its token holders) can capture the fee stack and disintermediate Nasdaq from the end user, compressing the exchange's take on its own data over time.
3. **Regulatory / data-licensing ambiguity onchain.** Market-data licensing is heavily contractual (per-user, per-terminal, redistribution controls). Programmable/onchain distribution makes usage-based enforcement and audit harder; a licensing or SEC market-data-fee dispute is a live tail risk for exchange data pushed to permissionless chains.

**What this changes (idea-lens).** (analysis) Signals a shift from "exchanges experiment with tokenized securities" to "exchanges monetize their crown-jewel data via onchain rails" — a re-rating vector for exchange data-as-revenue and a validation of first-party oracles closing the quality gap on Chainlink. Falsifiable thesis: within ~12 months Pyth publishes named live protocols consuming TotalView and a disclosed revenue/fee arrangement; trigger to watch — Nasdaq breaking out onchain-data contribution in IR, or Chainlink countering with its own exclusive exchange-data deal. What breaks it: the feed stays a PR pilot with no consuming apps and no disclosed economics through 2026.

Sources: https://www.tradingview.com/news/cointelegraph:543041829094b:0-nasdaq-brings-proprietary-market-data-onchain-through-pyth/ · https://cryptobriefing.com/nasdaq-blockchain-market-data-distribution/ · https://messari.io/compare/chainlink-vs-pyth-network · https://coinlaw.io/chainlink-statistics/ · https://blog.redstone.finance/2026/03/30/blockchain-oracles-comparison-chainlink-vs-pyth-vs-redstone-2026/ · https://www.coindesk.com/business/2025/08/28/chainlink-to-provide-u-s-department-of-commerce-data-on-chain-for-smart-contract-use · https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-reports-first-quarter-2025-results-diversified-business
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
