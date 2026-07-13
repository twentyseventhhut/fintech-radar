---
title: "Ground raises $3.6M to pipe on-chain yield into fintech apps"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/ground
  - industry/defi
  - industry/infrastructure
  - region/us
  - type/funding
sources:
  - https://www.connectingthedotsinfin.tech/r/2a3445ad
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s570fcca5
month: 2026-06
enriched: true
importance: 2
---

# Ground raises $3.6M to pipe on-chain yield into fintech apps

> [!info] 2026-06-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Ground raises $3.6 million to pipe on-chain yield into FinTech apps. The startup provides API infrastructure that enables FinTechs to integrate regulated on-chain yield products without building blockchain infrastructure, targeting the growing institutional adoption of decentralized finance.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/2a3445ad>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ground raises $3.6M to pipe on-chain yield into fintech apps
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Ground, a San Francisco "money infrastructure" startup, came out of stealth on 2026-06-24 with a **$3.6M pre-seed**, co-led by **Bain Capital Crypto and ParaFi**, with **Nascent, Robot Ventures, Chapter One, Consonant Ventures**. The round was structured as a **SAFE with token warrants**; it actually **opened in Sept 2025 and closed Oct 2025** — i.e. the "news" is a ~8-month-old closed round timed to a public launch, not fresh money. No investors took board seats or observer rights.

What Ground sells: a **modular API** that lets fintechs/neobanks/wealth & asset managers/exchanges plug into on-chain yield (lending protocols, structured products, forthcoming LSTs) **without building blockchain infra**. It currently routes to **Aave, Morpho, Maple, Kamino** across **Ethereum, Solana, L2s**. Revenue = **usage-based fees** (more capital routed → more fee). Team: **3 FT + 1 contractor**, hiring 2-4 more.

**Why framed this way / what it reveals:** The headline number is small and the round is stale, so the PR leans on two flattering anchors instead — (1) the founder's pedigree (Superstate co-founder, ex-Compound Treasury GM) and (2) the "institutional adoption of DeFi" macro narrative. Critically, **no live clients, no AUM/capital-routed numbers, no revenue** were disclosed. The product itself is an aggregation/abstraction layer over four protocols anyone can integrate directly — the moat claimed is "transparency + configurability for TradFi," which is a feature assertion, not demonstrated traction. De-PR'd: this is a **founder-pedigree pre-seed bet on a crowded category at the idea/early-build stage**.

## [1] Competitors / peers
This is a **crowded, well-funded "yield-as-a-service / embedded on-chain yield" lane**, and Ground is *behind on capital and traction* against most named peers:
- **[[OpenTrade secures $17 million for stablecoin yield infrastructure]]** (2026-05, $17M; Circle/a16z-backed) — white-labeled RWA-backed yield, **named live clients** (Belo, BuenBit in LatAm/EU). Far ahead on funding and adoption.
- **[[Veda raises $18M for DeFi vault platform]]** (2025-06, $18M; CoinFund) — vault stack reportedly behind Kraken DeFi Earn and integrated with Privy's 2,000+ dev teams, **$100M+ deposits**. Ahead on both money and live integrations.
- **[[Osero raises $13.5 million for stablecoin yield infrastructure]]** (2026-05, $13.5M; Sky Ecosystem) — direct stablecoin-yield-infra peer, 3.7x Ground's raise.
- **[[Maple Finance brings syrupUSDC yield to Tempo blockchain]]** (2026-06) and **[[Stripe-backed Tempo taps DeFi lender Morpho to expand beyond payments]]** (2026-05) — incumbents (Maple, Morpho, Stripe/Tempo) embedding yield *natively into rails*, which can **disintermediate an aggregator** like Ground.
- Off-corpus: Coinchange (Yield-as-a-Service API), Aegis, Stay Liquid — same plug-and-play pitch.

**Why the landscape is this way / second-order:** The category bifurcates into (a) **RWA/treasury-backed** yield (OpenTrade, Osero) and (b) **DeFi-protocol-routing** yield (Ground, Veda, Coinchange). Ground sits in (b) — the more commoditized half, because aggregating Aave/Morpho/Maple is integration work, not proprietary yield generation. The peers that look strongest (OpenTrade, Veda) win on **named live clients**, not API breadth. So the real competitive axis isn't "who supports more protocols" but **"who already custodies the embedding relationship with a real fintech distributor"** — and on that axis Ground has shown nothing yet.

## [2] Company history / fit
Ground is brand-new (stealth → launch June 2026). The asset is **founder fit**: CEO **Reid Cuming** co-founded **Superstate** (tokenization; ~$82.5M raised through Series B) and was **VP/GM of Compound Treasury**; CTO **Sam Yoon** built stablecoin rails (Braid, HiFi). Cuming remains a board member/advisor at Superstate.

**Why they act this way:** Cuming has lived the exact pain twice — at Compound Treasury and Superstate he sat at the seam between TradFi balance sheets and on-chain yield. Ground is the **"picks-and-shovels" generalization** of that: instead of being one yield product, be the API every fintech uses to reach many. That's a logical, investor-legible thesis, which is why pedigree VCs (Bain Crypto, ParaFi) wrote a *small* check — they're buying the founder and the option, not yet a business. The thin team (3 FT) confirms it's pre-product-market-fit.

## [3] Novelty / value-add / traction
**What's actually new: little.** "API to embed on-chain yield without building blockchain infra" is the *exact* pitch of OpenTrade, Veda, Coinchange and others already in market with money and clients. Ground's differentiation claim — "transparency + configurability that fintechs/TradFi require, which crypto-native aggregators lack" — is **unverified positioning**.

**Traction: none disclosed.** No clients, no capital routed, no revenue, no APY ranges. Compare: Veda cites $100M+ deposits and Kraken/Privy; OpenTrade cites Belo/BuenBit. Ground cites a protocol list (Aave/Morpho/Maple/Kamino) — *capabilities, not adoption*.

**Why value-add is shaky, deeper:** In this stack the **margin accrues to whoever owns yield generation (the protocols: Aave/Morpho/Maple) and whoever owns distribution (the fintech/neobank)**. A pure routing API is the **thin middle** — easy to commoditize, and exactly what payment-rail incumbents (Stripe/Tempo + Morpho/Maple) are now absorbing natively. So Ground risks being disintermediated from *both* sides. Its only durable wedge would be (a) regulatory/compliance abstraction (KYC of yield sources, reporting) and (b) cross-protocol risk underwriting — neither demonstrated. Until a named fintech routes real capital, the value-add is **a hypothesis**, not a fact.

## [4] What's next / market sentiment
Near-term: hire 2-4, land first design-partner fintechs, add liquid staking tokens. Macro tailwind is real — embedded/on-chain yield and stablecoin-yield-as-a-service is one of 2025-26's most-funded fintech-crypto themes (multiple $13-18M rounds in the corpus within ~12 months), and "institutional DeFi adoption" is the consensus narrative.

**Why the market goes this way / counterintuitive second-order:** The *category* tailwind is precisely what makes *Ground* fragile. A hot, well-capitalized lane means the aggregator layer gets **squeezed from above (protocols going direct-to-fintech, e.g. Maple→Tempo) and below (BaaS/embedded-finance incumbents adding yield)**. Capital flooding the space doesn't protect a sub-$4M pre-seed entrant — it **shortens its runway to prove distribution before larger peers or incumbents close the gap**. Regulatory backdrop (yield-bearing-stablecoin scrutiny, who's liable for on-chain yield sold to retail) is an open risk that could *help* (compliance moat) or *hurt* (forces conservative, low-yield products). Net sentiment: **promising founder, commoditized middle, everything-to-prove.**

## Top challenge/extra questions
See challenge column.

## Sources
- The Defiant — Ground launch / $3.6M: https://thedefiant.io/news/press-releases/ground-launches-onchain-finance-api-3-6m-raise
- The Block — Superstate co-founder raises $3.6M for Ground: https://www.theblock.co/post/406040/superstate-co-founder-ground-funding-crypto-onchain-yield
- Crypto Briefing: https://cryptobriefing.com/ground-raises-preseed-fintech-onchain-yield/
- Cryptopolitan: https://www.cryptopolitan.com/ground-raises-3-6-million-to-pipe-on-chain-yield-into-fintech-apps/
- The Block — Veda/Privy/Kraken: https://www.theblock.co/post/403277/veda-brings-the-vault-stack-behind-kraken-defi-earn-to-privys-2000-plus-developer-teams
- OpenTrade: https://www.opentrade.io/ ; Coinchange YaaS: https://www.coinchange.io/products/yield-as-a-service
- Internal: [[OpenTrade secures $17 million for stablecoin yield infrastructure]], [[Veda raises $18M for DeFi vault platform]], [[Osero raises $13.5 million for stablecoin yield infrastructure]], [[Maple Finance brings syrupUSDC yield to Tempo blockchain]], [[Stripe-backed Tempo taps DeFi lender Morpho to expand beyond payments]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / second-order questions

1. **Is the $3.6M actually fresh news?** No — the round **opened Sept 2025, closed Oct 2025**; the June 2026 "raise" is a stealth-exit PR timing, not new capital (The Block).

2. **Are there any live clients or capital routed?** **Open / negative** — *none disclosed*. No AUM, no design partners named, no APY ranges. This is the single biggest weight-killer.

3. **Is the product genuinely differentiated vs OpenTrade/Veda/Coinchange?** Largely no. Same "embed on-chain yield via API without blockchain infra" pitch. Differentiation ("transparency + configurability for TradFi") is an **unverified assertion**, not a shipped, adopted feature.

4. **Where does the margin sit in this stack?** With **yield generators (Aave/Morpho/Maple)** and **distributors (the fintech/neobank)**. Ground is the **thin routing middle** — structurally the easiest layer to commoditize or disintermediate.

5. **Can incumbents disintermediate Ground?** Yes, and it's already happening: **Maple→Tempo** and **Stripe/Tempo→Morpho** embed yield *natively into rails*, removing the need for a third-party aggregator (corpus notes).

6. **Why so small a check from such strong VCs (Bain Crypto, ParaFi)?** It's a **founder/option bet**, not a business bet. No board seats taken — consistent with a cheap pre-seed pedigree wager, not high conviction on traction.

7. **Does the founder pedigree convert to a moat?** Partially — Cuming (Superstate, Compound Treasury) knows the TradFi↔on-chain seam and likely opens enterprise doors. But pedigree ≠ distribution; peers already have *clients*, Ground has *relationships at best*. **Open.**

8. **What's the real durable wedge if any?** Plausibly **compliance/reporting abstraction + cross-protocol risk underwriting** for regulated fintechs. **Neither demonstrated** — so currently hypothetical.

9. **How crowded/well-funded is the lane?** Very: OpenTrade $17M, Veda $18M, Osero $13.5M all within ~12 months — Ground's $3.6M is the **smallest and latest** entrant, a competitive disadvantage on runway.

10. **Does the macro tailwind protect Ground?** Counterintuitively **no** — a hot lane invites incumbents and better-funded peers, squeezing the aggregator from both ends and **shortening Ground's window** to prove distribution.

11. **Regulatory exposure?** Yield-bearing products sold to retail via fintechs raise liability/registration questions (who's the offeror?). Could become a **moat (compliance)** or a **constraint (forced low-yield/conservative products)**. **Open.**

12. **Smart-contract / counterparty risk concentration?** Routes to Aave/Morpho/Maple/Kamino — Ground inherits those protocols' exploit/depeg/liquidation risks but **who eats the loss** (Ground, the fintech, or the end user) is **unstated**. PR is silent on liability.

13. **Multi-chain breadth (ETH/Solana/L2) — feature or moat?** A feature; competitors span similar surfaces. Breadth without a routing fintech using it is **shelf-ware**.

14. **What single proof point would re-rate this up?** One **named fintech/neobank routing real, disclosed capital** through Ground at a stated fee — converting "API capability" into "live embedded distribution." Absent until then.

15. **Could Ground be an acqui-hire target rather than a standalone?** Plausibly — strong infra-fintech team in a consolidating lane; a larger yield-infra or BaaS player could absorb it. **(hypothesis)**

Importance: 2/5 — A small ($3.6M), stale (closed Oct 2025) pre-seed by a strong-pedigree founder in a crowded, better-funded "embedded on-chain yield" lane, with **zero disclosed traction** and a structurally commoditizable middle-of-stack position facing active disintermediation by protocols and rails. Watchable for the founder and the macro theme, but no demonstrated novelty or adoption to warrant more.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Ground sells into the *yield-bearing-stablecoin / embedded on-chain yield* sub-sector — one of the fastest-growing crypto-fintech lanes. Sizing (sourced): yield-bearing stablecoin supply grew from ~$1bn (2023) to >$19bn (2025), and in Q1 2026 contributed **$4.3bn of an $8bn quarterly stablecoin supply increase — i.e. >half of net growth**, expanding ~22% in the quarter (per CEX.IO / BitKE Q1-2026 stablecoin reports). 21Shares projects the category to exceed **$50bn in 2026** (analysis-grade forecast, not a hard figure). The *underlying* yield generators are scaling fast too: Morpho ~$6.5bn TVL (deposits $5bn→$13bn over 2025-26), Maple ~$2.1bn TVL / >$4bn deposits at 7-8% APY (DefiLlama / press, mid-2026). **Structure:** the value chain is three-layered — (1) yield generation (Aave/Morpho/Maple — capital-intensive, network-effect moats), (2) the embedding/routing API middle (Ground, Veda, Coinchange, OpenTrade), (3) distribution (the fintech/neobank). The middle is **fragmented and low-barrier** — integrating four public protocols is engineering work, not proprietary IP. **Why now / drivers:** (i) idle-balance economics — neobanks want stablecoin yield to replace shrinking FX/interchange revenue (rebelfi, apideck, 2026); (ii) "institutional DeFi adoption" as consensus narrative; (iii) a regulatory overhang on who may offer yield-bearing products to retail, which is the swing factor that could either gate the lane (compliance moat) or force conservative low-yield products.

**Competitive landscape.** Sector KPIs the lane actually runs on: **capital routed / TVL, number of named live fintech distributors, take/usage fee on routed AUM** — none of which Ground discloses. Players and basis of competition (the axis is *distribution relationships*, not protocol breadth):
- **OpenTrade** (Circle/a16z): **>$200M TVL**, >$250M tx volume in 2025, targeting >$1bn in 2026, named clients (Belo, BuenBit), $30M+ total funding (The Block, Tech.eu, May 2026). The clear leader on the RWA-backed half.
- **Veda** (CoinFund): vault stack behind Kraken DeFi Earn + Privy (2,000+ dev teams), **$100M+ deposits** (corpus, 2025-06).
- **Osero** (Sky Ecosystem): $13.5M, RWA/stablecoin-yield half (corpus, 2026-05).
- **Coinchange / Crossmint / Aegis**: same plug-and-play YaaS-API pitch (Coinchange.io, Crossmint, 2026) — off-corpus, confirms low differentiation.
- **Disintermediators (already live):** Maple↔Tempo integration is **live today** (Morningstar/Business Wire, 2026-06-11), embedding syrupUSDC natively into Tempo's fintech rails; Stripe/Tempo↔Morpho similarly. This removes the need for a third-party aggregator for any fintech already on those rails.
**Ground's position:** behind on both capital and traction — smallest ($3.6M) and latest entrant, **zero disclosed clients/AUM/revenue**. Claimed moat ("transparency + configurability for TradFi") is an *unverified feature assertion* `(analysis)`, not a demonstrated switching cost.

**Comps & multiples.** Private, pre-revenue names — **EV/Revenue, EV/EBITDA, P/E = no data** (no public financials for any peer). What is verifiable is funding/valuation scale, which positions Ground as the runt of the lane:
- Ground — **$3.6M** pre-seed (SAFE + token warrants), no valuation disclosed `[UNSOURCED]`.
- [[Osero raises $13.5 million for stablecoin yield infrastructure]] — $13.5M = **3.75x** Ground ($13.5M / $3.6M).
- [[OpenTrade secures $17 million for stablecoin yield infrastructure]] — $17M round, $30M+ total = **~4.7x** Ground's single round; **>$200M TVL** vs Ground's $0 disclosed.
- [[Veda raises $18M for DeFi vault platform]] — $18M = **5.0x** Ground; $100M+ deposits.
- External anchor (not a direct comp — it's the protocol layer Ground routes to): **Morpho** closed $175M at a reported **~$2bn valuation** (Paradigm/a16z/Ribbit, 2026-06-09), on ~$6.5bn TVL → ~**0.31x valuation/TVL** as a crude sanity gauge `(analysis)`. The point: the layer Ground depends on is itself a $2bn, well-capitalized incumbent that can go direct-to-fintech.
Distribution not computed (only 3 comparable raises, all pre-revenue) — **qualitative read: Ground is cheap on raise size but that reflects stage/traction, not a bargain.** Ground sits below the lane's $13-18M funding band by 3.7-5.0x.

**Risk flags.**
1. **Disintermediation from both ends (live, not hypothetical).** Yield generators (Maple→Tempo, Morpho→Stripe/Tempo) and BaaS/embedded-finance incumbents are absorbing the routing middle natively. Second-order: any fintech already on Tempo/Stripe rails has *no reason* to add Ground, shrinking the addressable wedge before Ground can sign one client.
2. **Zero disclosed traction in a lane priced on traction.** Peers compete on named live clients and AUM (OpenTrade $200M TVL, Veda $100M deposits); Ground shows protocol breadth only. With a sub-$4M check and 3 FT, runway to prove distribution is short while peers compound theirs — a self-reinforcing gap.
3. **Liability / regulatory ambiguity on routed yield.** Who is the offeror, and who eats a smart-contract exploit / depeg / liquidation loss across Aave/Morpho/Maple/Kamino is **unstated**. A yield-bearing-stablecoin-to-retail rule could either become Ground's only durable moat (compliance abstraction) or force low-yield products that kill the value prop. Open both ways.

**What this changes (idea-lens).** `(analysis)` This is a *new entry at the bottom of a consolidating lane*, not a re-rating. Falsifiable thesis: **Ground is more likely an acqui-hire (strong infra-fintech team) than a standalone winner**, because the routing middle is being captured natively by protocols and rails. Trigger that would prove the thesis WRONG: one **named neobank/fintech routing real, disclosed capital through Ground at a stated fee** within ~12 months — converting "API capability" into live embedded distribution. Absent that single proof point, the macro tailwind helps the *category*, not this entrant.

Sources: https://blog.cex.io/ecosystem/q1-2026-stablecoin-report-35459 · https://bitcoinke.io/2026/04/stablecoins-in-q1-2026/ · https://www.theblock.co/post/400187/opentrade-raises-17m-to-expand-stablecoin-yield-infrastructure-after-topping-200m-tvl · https://defillama.com/protocol/morpho · https://thedefiant.io/news/defi/morpho-raises-175m-defi-largest-ever-funding-round · https://www.morningstar.com/news/business-wire/20260611228994/maple-finance-brings-institutional-yield-opportunities-to-tempos-fintech-infrastructure · https://www.coinchange.io/products/yield-as-a-service
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
