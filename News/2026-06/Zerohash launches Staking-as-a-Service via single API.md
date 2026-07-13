---
title: "Zerohash launches Staking-as-a-Service via single API"
date: 2026-06-29
retrieved: 2026-06-29
tags:
  - company/zerohash
  - industry/crypto
  - industry/infrastructure
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/3e89f89b
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s338bdbb9
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# Zerohash launches Staking-as-a-Service via single API

> [!info] 2026-06-29 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 zerohash has launched Staking-as-a-Service, enabling banks, brokerages, and FinTech platforms to offer crypto staking through a single API integration. The solution manages blockchain infrastructure, validators, rewards, and compliance, starting with Ethereum support and Solana coming soon. Staking is available across the U.S., outside of California, Maryland, New Jersey and Wisconsin.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/3e89f89b>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Zerohash launches Staking-as-a-Service via single API
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS VERDICT: FRESH.** New product line (staking), distinct from prior Zerohash notes which cover regulation (Trust Company charter [[Zero Hash Trust Company approved to launch]]), funding ([[Zerohash raises $104M from Morgan Stanley, SoFi, Apollo]], [[Zerohash pursues funding above $1.5 billion valuation]]), EU licensing ([[Zerohash receives EMI license from Dutch central bank]]), and stablecoin rails ([[Zerohash integrates Monad for real-time USDC payments]]). No prior note announces a staking product. Primary source PR dated 2026-06-25 (GlobeNewswire); digest picked it up 2026-06-29. Genuine new capability, not a re-run.

## [0] What exactly happened (de-PR'd)
Zerohash added crypto staking to its embedded-infrastructure stack: banks/brokerages/fintechs can offer staking to end-users via a single API, with Zerohash managing validators, blockchain infra, rewards distribution, and compliance. Live with **Ethereum (ETH)** today; **Solana coming soon** (announced, not live). Available across the U.S. **except CA, MD, NJ, WI**. Named launch partners: **Interactive Brokers, Public, BitMart** (per GlobeNewswire/FFNews; the digest text omitted these — material, since partners = real distribution, not a cold launch).
- De-PR'd: this is a **product-line extension on an existing rails business**, not a new venture. The marketing stat "27% of retail crypto investors actively pursue staking" is a demand-side justification, unverified by us — treat as vendor framing.
- **Why structured this way:** Zerohash sells "everything-as-an-API" to regulated institutions that don't want to run blockchain infra or hold a charter. Staking is the obvious next SKU after trading, stablecoins, tokenization, custody — it monetizes the *same* embedded client base (IBKR is both an investor AND a launch partner here, a tell that distribution was pre-wired).

## [1] Competitors / peers
Two distinct competitive layers:
- **Validator / staking-ops specialists:** Figment (50+ networks, non-custodial), Kiln (Paris, ~4% of staked ETH, ~$4B AUM, non-custodial via Fireblocks/BitGo/Coinbase Prime), P2P.org, Coinbase Cloud/Prime, Alluvial (institutional liquid-staking standard, backed by Coinbase+Figment). Fireblocks also offers institutional staking.
- **Embedded-fintech infra:** Zerohash's actual lane. Its edge is NOT best-in-class validator performance — it's the **single-API + regulated stack (Trust charter, EMI, compliance) bundled with trading/stablecoins**. A brokerage adding staking via Zerohash avoids a separate Kiln/Figment integration plus its own compliance build.
- **Position:** parity-to-late on staking *mechanics* (Figment/Kiln have years of validator history and far more chains; Zerohash launches with one). **Ahead on packaging** for non-crypto-native regulated distributors. **+ Second-order:** the value isn't who stakes ETH best; it's who owns the *distribution relationship* with banks/brokerages. Zerohash likely subcontracts/abstracts validator ops while capturing the embedded-integration margin.

## [2] Company history / fit
Founded 2017, Chicago. Trajectory: $104M raise Sept 2025 (~$1B valuation, led by Interactive Brokers; Morgan Stanley, SoFi, Apollo, Jump) → Trust Company charter approved Sept 2025 → Monad/USDC integration Feb 2026 → Amsterdam EU HQ expansion Mar 2026 → Dutch EMI license May 2026 → in talks to raise ~$250M at >$1.5B valuation (after walking away from a Mastercard acquisition reportedly valued up to $2B; Mastercard then bought BVNK instead). Clients cited: IBKR, Stripe, BlackRock BUIDL, Franklin Templeton, DraftKings; 5M+ users, 190 countries.
- **Fit:** logical. **+ Why:** rails/transaction take-rates are commoditized and cyclical; adding fee-bearing, recurring **staking-reward** flow diversifies revenue and supports the software-multiple story it needs to justify a >$1.5B valuation while raising. Staking yield = a sticky, AUM-like revenue base vs one-off transaction fees.

## [3] Novelty / value-add / traction
- **Genuinely new for Zerohash; not new for the market.** Staking-as-a-service is a crowded vertical (Figment/Kiln/Coinbase predate this by years). Novelty = bundling staking into a *single regulated embedded API* alongside trading/stablecoins for non-crypto-native institutions.
- **Traction:** stronger than a typical launch — three named partners (IBKR, Public, BitMart) at GA, not "exploring." But still **announcement-stage on volumes**: no staked-asset figures, no AUM, no take-rate disclosed. Solana is roadmap only.
- **+ Who captures the margin:** the staking reward is generated by the protocol; the spread is split among validator operator, Zerohash, and the distributing institution. Zerohash's durable margin depends on whether it runs validators itself (higher margin, higher ops/slashing risk) or resells (thinner, but asset-light). Undisclosed — a key open question. **What breaks it:** validator commoditization compresses fees; large brokerages (IBKR) could in-house staking once volume justifies it, disintermediating Zerohash — exactly the risk of being the "plumbing."

## [4] What's next / market sentiment
- **Regulatory tailwind is the real story.** SEC Div. of Corp Fin (May 2025, "Providing Security is not a 'Security'") + Aug 2025 statements held that **protocol staking on permissionless PoS networks is not a securities transaction** (covering self/custodial/liquid staking and ancillary services like slashing coverage). The Mar 17, 2026 **joint SEC-CFTC interpretation** reinforced this. That clarity is precisely what lets regulated banks/brokerages offer staking — Zerohash's launch is timed to ride it.
- **Remaining risk:** SEC carved out **guaranteed rewards, discretionary management, and restaking** as still uncertain. Zerohash's "no minimum, stake/unstake any amount" framing must stay clear of guaranteed-yield characterization. State-level gaps (CA/MD/NJ/WI excluded) signal money-transmitter/securities friction persists sub-federally.
- **Sentiment:** positive; fits the 2025–26 institutional-crypto-infra thesis. **+ Counterintuitive second-order:** regulatory clarity *lowers the moat* — once staking is plainly legal, more providers (and the brokerages themselves) enter, so Zerohash's window to lock in embedded distribution before commoditization is narrow. The valuation raise depends on this land-grab.

## Sources
- GlobeNewswire (primary PR, 2026-06-25): https://www.globenewswire.com/news-release/2026/06/25/3317514/0/en/zerohash-expands-consumer-digital-asset-functionality-with-launch-of-staking-infrastructure-for-financial-institutions.html
- FFNews: https://ffnews.com/news/zero-hash-launches-staking-infrastructure-for-banks-and-brokerages-to-meet-rising-crypto-demand
- FinanceFeeds: https://financefeeds.com/zero-hash-brings-crypto-staking-to-banks-and-brokers-as-competition-for-digital-asset-clients-intensifies/
- Zerohash staking product/docs: https://zerohash.com/products/staking , https://docs.zerohash.com/docs/staking
- Funding/valuation: https://www.coindesk.com/business/2026/05/19/zerohash-pursues-new-funding-at-more-than-usd1-5-billion-valuation-after-mastercard-drops-investment-plans ; https://www.coindesk.com/business/2026/01/26/zerohash-is-in-talks-to-raise-usd250-million-at-usd1-5-billion-valuation-after-walking-away-from-mastercard-takeover
- Competitors: https://www.kiln.fi/ ; https://www.theblock.co/post/147385/coinbase-figment-alluvial-institutional-liquid-staking-protocol ; https://ambcrypto.com/top-11-staking-platforms-in-june-2026/
- SEC staking stance: https://www.sec.gov/newsroom/speeches-statements/peirce-statement-protocol-staking-052925 ; https://www.sidley.com/en/insights/newsupdates/2026/03/sec-releases-landmark-interpretation-on-application-of-us-securities-laws-to-crypto-assets
- Internal: [[Zero Hash Trust Company approved to launch]], [[Zerohash raises $104M from Morgan Stanley, SoFi, Apollo]], [[Zerohash pursues funding above $1.5 billion valuation]], [[Zerohash receives EMI license from Dutch central bank]], [[Zerohash integrates Monad for real-time USDC payments]], [[Zerohash expands European headquarters in Amsterdam]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Does Zerohash run its own validators or resell?** This determines whether margins are fat-and-risky (slashing exposure) or thin-and-asset-light. PR is silent. **Open** — central to the value-add.
2. **What is the take-rate / fee split on staking rewards** among protocol → validator → Zerohash → distributing institution? Undisclosed. **Open.**
3. **Is the IBKR relationship a customer or an investor placement?** IBKR led the $104M round AND is a launch partner — distribution may be pre-wired insider, not arm's-length market validation. **Partly answered: yes, IBKR is an investor; treat "partner" with that caveat.**
4. **Why ETH-only at launch, Solana "soon"?** Single-chain GA suggests limited validator footprint vs Figment (50+) / Kiln (10+). Is this a thin MVP dressed as a platform? **Likely yes (analysis).**
5. **What share of Zerohash revenue is durable (recurring staking/AUM yield) vs transactional (trading/on-ramp fees)?** Staking's strategic point is multiple-expansion via recurring revenue, but no numbers given. **Open** — decides the >$1.5B valuation case.
6. **What stops IBKR/Public from in-housing staking once volume scales,** disintermediating Zerohash as mere plumbing? This is the structural downside trigger. **Open / unmitigated.**
7. **Does the offering risk SEC's carve-out for "guaranteed rewards / discretionary management / restaking"?** "No minimum, stake/unstake any amount" sounds clean, but reward-smoothing or pooled validation could drift toward the uncertain zone. **Open.**
8. **Why are CA, MD, NJ, WI excluded?** State money-transmitter or securities-law friction — what's the path to lifting it, and does it limit the addressable brokerage base? **Open.**
9. **Is the "27% of retail crypto investors stake" stat sourced or vendor PR?** No citation surfaced. **Treat as marketing.**
10. **How does Zerohash differentiate from Fireblocks,** which already gives institutions staking + custody and is the custody backbone for Kiln? Is Zerohash competing or could it sit atop Fireblocks? **Open.**
11. **What's the slashing-liability allocation** between Zerohash and the institution / end-user? A live operational/financial risk the PR omits. **Open.**
12. **Did the previous infra SKUs (Monad/USDC, tokenization) actually drive volume,** or is this another announced-not-adopted layer? Pattern check on Zerohash's launch-to-traction conversion. **Open.**
13. **How does this launch interact with the funding raise** — is staking a revenue-narrative prop timed to the >$1.5B round, more than a deployed business? **Likely a contributing factor (analysis).**
14. **What happens to the embedded-staking moat as SEC clarity invites more entrants?** Regulatory clarity is a tailwind for the launch but erodes the moat — net effect on Zerohash's pricing power? **Open / structurally negative.**
15. **Cross-corpus:** does owning crypto + stablecoin + tokenization + staking under one regulated API actually create lock-in (switching costs) for distributors, or just a longer SKU list a competitor can match? **Open** — the real bull/bear pivot.

**Importance: 3/5.** Rationale: genuine new product line from a well-capitalized, regulated infra player with three named GA partners and a clean regulatory tailwind (SEC PoS-staking clarity) — above a routine launch. Capped at 3 because the underlying capability is years-old market-wide (Figment/Kiln/Coinbase), it launches single-chain with no disclosed volumes/economics, and Zerohash faces real disintermediation risk as the "plumbing." Notable as part of the Zerohash valuation-and-expansion arc, not a market-moving novelty.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-29]] (2026-06-29).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto/stablecoin embedded-infrastructure, sub-vertical = institutional Staking-as-a-Service (SaaS) delivered via API to banks/brokers/fintechs (a B2B2C "rails" layer, not retail staking). Size: per Coinlaw, institutional staking services were ~$5.8bn in 2024, projected ~$33.3bn by 2033; per MarketIntelo the broader crypto-staking-platform market was ~$3.8bn (2025) at ~21.9% CAGR to ~$22.6bn by 2034 (third-party research-house figures, definitions vary, treat as order-of-magnitude, not precise TAM). Demand driver "why now": ETH staked has climbed to ~30–31% of supply / >36m ETH in 2026, and institutions are entering via vehicles like BlackRock's staked-ETH trust (~$254m AUM in week one) — per CoinDesk/ainvest, 2026. Structure: the *embedding* layer (custody + validator orchestration + compliance + tax/rewards reporting behind one API) is consolidating around a handful of infra players; entry barriers are regulatory (state-by-state money-transmission, qualified-custody status) and operational (validator uptime/slashing risk), not capital-light — Zerohash itself can only offer staking in 47 states (excludes CA, MD, NJ, WI), which directly illustrates the regulatory-fragmentation barrier in the US.

**Competitive landscape.** Sector KPIs: total assets staked / AuS, validator uptime (SLA, typically 99.9%+), take/commission rate on rewards, and number of institutional clients; per-client API integration time is the go-to-market metric vendors compete on. Basis of competition = distribution (who already sits in the bank/broker stack) + compliance breadth + reliability, less on price. Key players & recent moves: Figment (the institutional validator standard, >1,500 institutional clients) powers staking *for* custodians — Fireblocks Trust Company + Figment launched institutional NEAR staking under qualified custody (Jun 2026, per Figment/PRNewswire); [[Crypto Finance Group launches staking service in Europe]] also runs on Figment (Oct 2025); BitGo built out crypto-as-a-service / digital-asset operating model for banks (May 2026, [[BitGo unveils modular digital asset operating model for banks]]); [[Anchorage launches Starknet staking for institutions]] (Sep 2025); Coinbase/Kraken offer staking inside their own stacks. Protagonist's position: Zerohash is *catching up* in staking specifically (Figment/Fireblocks/BitGo were there earlier) but enters from a position of strength on distribution — its embedded fiat/crypto/stablecoin API already sits inside Morgan Stanley, Stripe, Interactive Brokers and BlackRock's BUIDL (per CoinDesk/PYMNTS, 2026). Moat = distribution + switching costs of an already-embedded multi-product API and a multi-state regulatory footprint (analysis); validator economics themselves are likely outsourced/commoditized, so the moat is the integration layer, not the staking tech.

**Comps & multiples.** All comps are PRIVATE — figures are last-round post-money (round valuations, NOT market cap), and several are STALE. No public revenue/EBITDA for any of these names, so EV/Revenue, EV/EBITDA and P/E = **no data**; price-per-staked-asset = `[UNSOURCED]` (AuS not disclosed). Qualitative comparison only — distribution not computed (need ≥3 same-basis revenue figures).
- Zerohash — internal trail: [[Zerohash raises $100M at $1B valuation]] (Jul 2025, $1.0bn) → [[Zerohash raises $104M from Morgan Stanley, SoFi, Apollo]] (Sep 2025, ~$1.0bn) → [[Zerohash in talks to raise $250M after dropping Mastercard deal]] / [[Zerohash pursues funding above $1.5 billion valuation]] (Jan–May 2026, >$1.5bn target). [[Mastercard in talks to buy crypto firm Zerohash]] implied up to ~$2bn (M&A, lapsed). Trajectory: ~$1bn → >$1.5bn target in <1yr.
- Fireblocks — $8.0bn post-money (Series E, Jan 2022, per Fireblocks/CoinDesk) — STALE (2022, peak-cycle); broader custody/infra peer, not a pure staking comp.
- Figment — $1.4bn post-money (Series C, Dec 2021, per Blockworks/CoinDesk) — STALE (2021); the closest *staking-specific* comp.
Read: Zerohash's >$1.5bn target sits between Figment's (stale) $1.4bn and a fraction of Fireblocks' (stale) $8bn, but Zerohash is a broader fiat+crypto+stablecoin+tokenization platform, so it is NOT a like-for-like staking comp — comparison is in-line-to-rich only directionally, and unverifiable absent revenue. No outlier flag possible without denominators.

**Risk flags.**
1. Regulatory fragmentation / disclosure gap — staking is securities-sensitive in the US and the launch is already carved out of 4 states (CA/MD/NJ/WI); the PR is silent on whether rewards are passed to end users net of an undisclosed take, on slashing/loss liability, and on who is the regulated party. Second-order: a single SEC/state reclassification of staking-as-a-security could force withdrawal in more states and strand integrations.
2. Late entrant into a commoditizing layer — Figment, Fireblocks, BitGo and Anchorage already offer this; the validator/rewards economics are largely outsourced and price-competed, so Zerohash captures margin only at the integration/distribution layer. Second-order: thin staking-specific economics, value risks being captured by the underlying validator stack (disintermediation from below).
3. "Announced," not proven at scale — Ethereum live, Solana "coming soon," no client logos, no AuS or take rate disclosed; product traction is unverified. Second-order: hard to underwrite the >$1.5bn raise on staking-driven growth specifically.

**What this changes (idea-lens).** This is a product cross-sell, not a re-rating: Zerohash bolts a yield product onto an already-distributed crypto API, betting that bank/broker partners want one vendor for custody + trading + stablecoins + staking rather than stitching Figment/Fireblocks separately (analysis). Falsifiable thesis: if Zerohash's embedded distribution wins, watch for named bank/brokerage staking clients and the Solana launch landing within ~2 quarters; catalyst = the >$1.5bn round closing with staking cited as a growth driver. What breaks it: partners keep buying staking direct from Figment/Fireblocks (the specialist standard), or US staking regulation tightens — either leaves this as a feature, not a franchise.

Sources: https://coinlaw.io/cryptocurrency-staking-statistics/ · https://marketintelo.com/report/crypto-staking-platform-market · https://www.coindesk.com/markets/2026/01/07/staking-goes-mainstream-what-2026-could-look-like-for-ether-investors · https://www.figment.io/insights/fireblocks-trust-company-launches-institutional-staking-powered-by-figment/ · https://www.coindesk.com/business/2026/05/19/zerohash-pursues-new-funding-at-more-than-usd1-5-billion-valuation-after-mastercard-drops-investment-plans · https://www.fireblocks.com/press/crypto-custodian-fireblocks-raises-550-million-at-8-billion-valuation · https://blockworks.com/news/figment-closes-funding-round-at-1-4b-valuation
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
