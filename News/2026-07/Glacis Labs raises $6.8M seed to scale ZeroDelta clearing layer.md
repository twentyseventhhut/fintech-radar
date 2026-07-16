---
title: "Glacis Labs raises $6.8M seed to scale ZeroDelta clearing layer"
date: 2026-07-16
retrieved: 2026-07-16
tags:
  - company/glacis-labs
  - industry/crypto
  - industry/infrastructure
  - region/us
  - type/funding
sources:
  - https://www.connectingthedotsinfin.tech/r/8058eda4
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sbecf179c
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Glacis Labs raises $6.8M seed to scale ZeroDelta clearing layer

> [!info] 2026-07-16 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Glacis Labs raises a $6.8 million seed round to scale ZeroDelta, the clearing layer for digital assets. The company aims to scale infrastructure for institutional stablecoin settlements and future tokenized assets, with ZeroDelta already processing more than $1 billion in transaction volume.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/8058eda4>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Glacis Labs raises $6.8M seed to scale ZeroDelta clearing layer
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
- **The facts:** Glacis Labs (NYC, founded 2024) closed a **$6.8M seed** led by **Lightspeed Faction**, with **Franklin Templeton, Coinbase Ventures, Again (ex-IDC Ventures), Protein Capital, Techni Ventures** (The Block, PRNewswire, 2026-07-15). Proceeds fund hiring / GTM for **ZeroDelta**, its flagship product.
- **ZeroDelta = a multichain non-custodial clearinghouse.** It sits *above* bridges/messaging (Axelar, Wormhole, LayerZero) and **matches, nets, and settles** opposing digital-asset flows so that only the **net remainder** moves on-chain, with atomic delivery + a cryptographic receipt per transfer. Supported assets today: **USDC, USDT, USDe** (stablecoins). Roadmap: tokenized securities, RWAs, FX.
- **Traction claim (de-PR'd):** ">$1B in transaction volume" in the note is **lifetime/cumulative settled volume**, not run-rate; press adds a **$1.5B annualized run-rate across 40+ chains**. So the headline $1B is a *cumulative-to-date* figure — real but flattering framing (cumulative ≠ current throughput). **Customers = market makers/dealers, aggregators/solver networks, stablecoin issuers/tokenization platforms** — i.e. B2B/wholesale rebalancing, not retail.
- **Why framed this way:** a $6.8M seed is small; the story leans on the $1B/$1.5B numbers and the **Franklin Templeton + Coinbase Ventures** logos to signal institutional credibility for the "tokenized securities/RWA" ambition. The de-PR'd reality: this is an **early, stablecoin-rebalancing netting layer** with a big TAM narrative bolted on top.
- **Note tags miss `industry/defi`** — the note carries crypto/infrastructure; the substance is DeFi/settlement infra.

## [1] Competitors / peers
- **Direct peer, already in corpus:** [[Cycles raises $6.4 million to expand digital-asset clearing network]] (2026-05, Toronto, Cosmos co-founder Ethan Buchman; $6.4M led by Blockchange, **also Coinbase Ventures**; "Cycles Prime" nets OTC obligations privately across the network). Near-identical thesis, size, and lead-investor pattern to Glacis — **the "on-chain multilateral clearing" category now has ≥2 funded entrants in one quarter.**
- **Adjacent settlement peers in corpus:** [[Cyclops raises $20M for faster stablecoin settlement]] (2026-07, but that is B2B fiat↔stablecoin payment settlement, different layer), [[Cycles raises $6.4 million to expand digital-asset clearing network]], and broader tokenized-clearing names ([[Citi and DTCC urge regulators to keep pace with tokenized collateral]], [[ClearToken wins FCA approval]], [[Gemini secures US derivatives clearing license for prediction markets]]).
- **The real competitive threat is the transport layer itself:** **Circle CCTP V2** collapses clearing+settlement into burn-and-mint for USDC (live 13+ chains) and is the default settlement leg under most routers; **Chainlink CCIP** has become the institutional interop standard (adopted by BlackRock, Swift, DTCC) and pulled **>$7.2B of assets from LayerZero since May 2026** (CoinDesk, 2026-07-09). **+ Why this matters (analysis):** Glacis's netting value-add shrinks if issuers/routers internalize netting. Position: **catching up on category momentum, but structurally squeezed between commoditizing transport (CCTP/CCIP) below and issuer-native netting above.**

## [2] Company history / fit
- **Trajectory:** Glacis raised **$2M seed in May 2024** (Arrington Capital, Paper Ventures) for a **GMP router/firewall** aggregating Axelar/Wormhole/LayerZero (built with Moonsong Labs). Founders **Jacob Blish** (ex-Lido, motivated by bridge hacks) and **Shyamal Patel** (ex-product lead, Sommelier Finance).
- **Fit (logical):** the pivot from "router/firewall over bridges" → "clearing/netting layer above bridges" is **coherent** — same problem (bridge fragility/cost), moved up the stack from *routing* messages to *netting* value. **+ Why:** routing/messaging is being commoditized by CCTP/CCIP, so the durable margin is in **netting economics** (reducing on-chain moves), not in relaying messages. The pivot is a rational escape from a commoditizing layer.

## [3] Novelty / value-add / traction
- **What's genuinely new:** applying **multilateral netting** (a TradFi clearinghouse primitive) to on-chain, cross-chain flows with **non-custodial, atomic** settlement + cryptographic receipts. The value-add is real *in principle*: if you net opposing flows, you move less on-chain → lower gas/bridge cost + lower counterparty exposure.
- **Traction (skeptical read):** $1B cumulative settled / $1.5B annualized run-rate across 40+ chains is **material for a seed** and better than pure-announcement peers — BUT it's **wholesale rebalancing volume** (market makers moving inventory), which is high-volume/low-value-capture and **not sticky** (users switch on price). No disclosed take-rate, revenue, or named anchor clients (contrast Cycles, which named **Lynq + FalconX**).
- **+ Who captures the margin (analysis):** stablecoin **issuers** (Circle/Tether) and the **transport standard** (CCIP) sit on either side. A netting overlay captures margin only if it stays the **cheapest net-settlement route** and issuers don't internalize it. That's a thin, contestable moat → hence the seed-stage valuation and the "expand into RWA/FX" narrative to justify a bigger prize.

## [4] What's next / market sentiment
- **Plans:** hire, expand GTM, extend from stablecoins to **tokenized securities, RWAs, FX**. The **Franklin Templeton** check is the tell — an asset manager pushing tokenized funds wants cross-chain settlement rails.
- **Sentiment/backdrop:** 2026 is a land-grab for **institutional on-chain settlement** (Citi/DTCC, CCIP institutional adoption, tokenized-collateral push). Tailwind: real institutional demand for 24/7 net settlement.
- **+ Counterintuitive second-order (analysis):** the same institutional tailwind that funds Glacis also **empowers CCIP/CCTP and issuers to absorb netting natively** — so category momentum can validate the thesis while **eroding the independent clearing layer's economics**. The central question is not "is on-chain clearing real" (it is) but **"does an independent netting overlay survive between commoditized transport and issuer-native settlement, or get disintermediated?"**

## Sources
- The Block — "Crypto clearinghouse Glacis Labs raises $6.8M seed" (2026-07-15)
- PRNewswire / Morningstar — Glacis Labs $6.8M seed release (2026-07-15)
- CryptoBriefing, BitcoinWorld — round details, investor list
- Newswire / Yahoo — Glacis $2M seed (May 2024), founders, GMP router/firewall
- CoinDesk — LayerZero→CCIP $7.2B migration (2026-07-09); Eco.com — CCTP V2 / clearing-vs-settlement primers
- Corpus: [[Cycles raises $6.4 million to expand digital-asset clearing network]], [[Cyclops raises $20M for faster stablecoin settlement]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5** — Real, credited traction ($1B cumulative / $1.5B annualized run-rate, 40+ chains) and a strong institutional cap table (Franklin Templeton, Coinbase Ventures, Lightspeed Faction) lift it above a typical seed. But it's a $6.8M seed in a suddenly-crowded "on-chain clearing/netting" niche (direct peer Cycles funded the same quarter), with unproven margin capture and a structural squeeze between commoditizing transport (CCTP/CCIP) and issuer-native netting. Solid, not landscape-moving.

## Top challenge / red-team questions
1. **Cumulative vs run-rate:** ">$1B volume" is lifetime settled; the $1.5B *annualized* run-rate is the honest metric. Is throughput accelerating or flat? — **open** (no time series disclosed).
2. **What is the take-rate / revenue?** No fee, revenue, or unit-economics figure disclosed. Is netting monetized per-transfer, on saved gas, or SaaS? — **open**.
3. **Named clients?** Peer Cycles named Lynq + FalconX as anchors; Glacis names only *categories* (market makers, solvers, issuers). Are there disclosed anchor customers? — **open / likely none public**.
4. **Value = wholesale rebalancing?** If volume is market makers moving inventory, it's high-volume/low-value and price-switchable — how sticky is it? — **analysis: low stickiness**.
5. **Disintermediation by CCTP V2** (burn-and-mint collapses clear+settle for USDC) — does ZeroDelta add net value for pure-USDC flows, or only for cross-stablecoin/mixed flows? — **open, likely only mixed-asset**.
6. **Disintermediation by CCIP** — with $7.2B migrating LayerZero→CCIP and CCIP as institutional standard, does an independent netting overlay survive or get absorbed? — **the central question; open**.
7. **Do issuers internalize netting?** Circle/Tether/Ethena could net natively — what stops them? — **analysis: nothing structural; moat is thin**.
8. **Non-custodial + atomic claims** — verified/audited? Any live incident, or purely marketing? — **open**.
9. **Pivot risk:** $2M→router/firewall (2024) then pivot to clearing (2026). Is the router product dead, or does traction come from it? — **open; appears fully pivoted**.
10. **RWA/securities/FX roadmap** — announced ambition, zero live volume there. Is Franklin Templeton a customer or just an investor? — **investor only, per release; roadmap = aspiration**.
11. **Freshness vs Cycles:** Is this a re-report of the Cycles clearing story? — **No: different company (Glacis/NYC vs Cycles/Toronto), different product, different lead investor. Fresh.**
12. **Regulatory:** a "clearinghouse" for digital assets — does non-custodial atomic design dodge clearing-agency regulation, or is that a latent risk (cf. ClearToken/FCA, Gemini clearing license)? — **open**.
13. **Why so small ($6.8M)?** If $1.5B run-rate is real, why only a seed? — **analysis: low monetization / early revenue; volume ≠ dollars captured**.
14. **Second-order:** does category momentum (Cycles, Cyclops, CCIP) validate or cannibalize Glacis? — **both; cannibalization risk dominates long-run**.
15. **Chain concentration:** 40+ chains supported, but is volume concentrated on 2-3? Breadth may be marketing. — **open**.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Glacis sits in on-chain clearing & settlement infrastructure — the layer between cross-chain bridges/transport and institutional digital-asset flows. Sector backdrop: total stablecoin market cap crossed ~$322bn in June 2026 (per stablecoininsider.org, as of Jun-2026), with ~$1.1tn/month in on-chain stablecoin transactions over the six months to Nov-2025 (per Chainalysis/Thunes citations). Institutional plumbing is scaling fast: Broadridge's DLR repo platform hit ~$7.3tn monthly volume in Jan-2026, +508% YoY (per company data, via chainup/fintechweekly). Structure — fragmented and pre-standard: transport (bridges/messaging: LayerZero, Chainlink CCIP, Wormhole) is separate from clearing/netting, and no dominant multichain clearinghouse exists yet; barriers are technical (atomic settlement across 40+ chains) and trust/institutional (custody, counterparty risk), not capital-heavy. Drivers + "why now": (1) the GENIUS Act's federal stablecoin framework (100% reserves, disclosures) gives banks a rulebook to move settlement on-chain; (2) tokenized RWA/Treasuries expansion pulls institutional flows on-chain and creates demand for netting/clearing that reduces the volume that actually touches the chain. Why-ladder: bridges move gross tokens one-by-one → gross cross-chain flow is capital-inefficient and risky → a netting layer settles only the remainder → second-order: less on-chain volume per unit of economic activity, so clearing captures value the transport layer can't.

**Competitive landscape.** Sector KPIs: settled/cleared volume, annualized run-rate, chains supported, and net-to-gross settlement ratio (netting efficiency) `(analysis)`. Key players & basis of competition: this is an emerging clearing/netting niche distinct from bridges — Glacis (ZeroDelta) competes on netting efficiency + non-custodial atomic settlement + cryptographic receipts rather than raw transport speed; adjacent/competing efforts include Cycles (open clearing network for on-chain finance) and the transport incumbents (Chainlink, LayerZero) that could move up-stack into netting. Recent peer moves: [[Cycles raises $6.4 million to expand digital-asset clearing network]] (May-2026, $6.4M, near-identical positioning); [[AEON raises $8 million to build settlement layer for AI agents]] (May-2026, $8M pre-seed, agent-payment settlement); [[Squid raises $6 million for cross-chain consumer infrastructure]] (May-2026, $6M, cross-chain routing/settlement, consumer-side); [[Kraken replaces LayerZero with Chainlink for cross-chain bridging]] (May-2026, shows transport-layer churn/competition below Glacis). Protagonist position: early leader on disclosed traction — ZeroDelta reports >$1bn settled and a ~$1.5bn annualized run-rate across 40+ chains, ahead of same-vintage peers who are pre-traction. Moat `(analysis)`: netting network effects (more counterparties → deeper offsetting flows → better netting) plus institutional backer distribution (Franklin Templeton, Coinbase Ventures); moat is nascent, not yet defensible.

**Comps & multiples.** Private seed-stage — no market-cap/revenue multiples; post-money not disclosed, so EV/Revenue and price-per-metric = no data / `[UNSOURCED]`. Round-size peer set (all disclosed rounds, same infra/clearing/cross-chain vintage, source channel Connecting the Dots):
- Glacis Labs — $6.8M seed (Lightspeed Faction lead; Franklin Templeton, Coinbase Ventures) — traction: >$1bn settled, ~$1.5bn run-rate, 40+ chains.
- [[Cycles raises $6.4 million to expand digital-asset clearing network]] — $6.4M (closest comp; open clearing network for on-chain finance).
- [[Squid raises $6 million for cross-chain consumer infrastructure]] — $6M (cross-chain routing/settlement).
- [[AEON raises $8 million to build settlement layer for AI agents]] — $8M pre-seed (agent settlement).
- [[Variational raises $50 million to bring liquidity to crypto]] — $50M (larger, derivatives/RWA — different scale/model, excluded from tight comp).
Distribution not computed as valuation multiples (post-monies undisclosed); on round size Glacis's $6.8M is in-line with the $6–8M clearing/cross-chain seed cluster. Note: Glacis previously raised a $2.1M seed (Arrington Capital, Paper Ventures) as a cross-chain messaging protocol per The Block/ChainCatcher — this $6.8M is a re-positioning up-stack from messaging to clearing, worth flagging as a pivot, not pure scale-up.

**Risk flags.**
1. Disintermediation from below — transport incumbents (Chainlink CCIP, LayerZero) already sit on the flows and could add netting/clearing themselves, capturing the layer Glacis targets; Glacis depends on someone else's rails to move the net remainder. Why: margin could be squeezed to the transport layer that owns the endpoints.
2. Traction attribution / de-PR — ">$1bn settled" and "$1.5bn annualized run-rate" are self-reported and mix gross throughput with netting; unclear how much is sustained institutional flow vs. bootstrapped/incentivized volume. Why: run-rate framing can overstate durable adoption for a seed-stage clearinghouse.
3. Regulatory & counterparty — a clearinghouse for institutional stablecoin/tokenized-asset settlement invites the same oversight as ClearToken/regulated CCPs; non-custodial design mitigates custody risk but clearing-member and jurisdictional rules (GENIUS Act + securities regimes for tokenized RWA) are unsettled. Why: compliance cost and licensing could gate the institutional TAM the pitch depends on.

**What this changes (idea-lens).** `(analysis)` Signals a new sub-layer forming — "clearing/netting" as a distinct, fundable category above cross-chain bridges, with two ~$6M+ seeds (Glacis, Cycles) in one quarter suggesting early competition, not consolidation. Falsifiable thesis: if netting genuinely reduces on-chain gross volume, transport/bridge economics compress while clearing captures the spread. Trigger/what breaks it: watch for a named institutional counterparty going live (not just "processing volume"), or a bridge incumbent bundling netting — the latter would invalidate Glacis's standalone-layer thesis.

Sources: https://www.theblock.co/post/408490/crypto-clearinghouse-glacis-labs-zerodelta-funding · https://www.prnewswire.com/news-releases/glacis-labs-raises-6-8-million-seed-round-to-scale-zerodelta-the-clearing-layer-for-digital-assets-302825869.html · https://cryptobriefing.com/glacis-labs-seed-round-zerodelta-clearing/ · https://www.fintechweekly.com/news/stablecoins-2026-onchain-finance-settlement · https://stablecoininsider.org/stablecoin-infrastructure-landscape-2026/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
