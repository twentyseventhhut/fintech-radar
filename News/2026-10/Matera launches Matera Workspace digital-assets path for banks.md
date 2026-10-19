---
title: "Matera launches Matera Workspace digital-assets path for banks"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/matera
  - industry/crypto
  - region/us
  - type/product
sources:
  - https://www.businesswire.com/news/home/20261016469184/en/Matera-Launches-Matera-Workspace-Giving-Banks-and-Credit-Unions-the-Shortest-Path-to-Offer-Digital-Assets-Alongside-Fiat
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: se1757037
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Matera launches Matera Workspace digital-assets path for banks

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Matera launches Matera Workspace, giving banks and credit unions a path to digital assets. Matera says Workspace is the shortest path to offer digital assets alongside fiat. Institutions can provide digital assets next to their existing fiat services.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261016469184/en/Matera-Launches-Matera-Workspace-Giving-Banks-and-Credit-Unions-the-Shortest-Path-to-Offer-Digital-Assets-Alongside-Fiat>

## Контекст

<!-- enrichment:context -->
## [0] What exactly happened (de-PR'd)
On 2026-10-16 Matera launched **Matera Workspace**, an "application platform" that lets banks and credit unions offer stablecoins, crypto and tokenized instruments alongside fiat **without replacing the core**. Concretely it bundles three things Matera already sells/ships into one extension: (a) **Digital Twin**, Matera's real-time ledger (already in production for instant payments) that holds USD, EUR, stablecoins, crypto and tokenized assets as balances "with equal standing"; (b) its **X9.150 Secure Payment QR** software (shipped July 2026, open-sourced Aug 2026); and (c) pre-built **custody integrations** with third-party custodians. Marketing claims: a pilot can "go live in about one hour", "nothing to remove" if a project dies, and a built-in **trade engine where the customer transacts directly with the bank** (not a marketplace), keeping trades inside the institution's existing regulatory posture. "Available now."
→ **Why framed this way:** the entire pitch is engineered around the incumbent-bank buying objection — core migrations are multi-year and risky, and compliance teams fear crypto marketplaces. So Matera sells a *side-car* (ledger extension) + a *principal-model* trade engine (bank is counterparty, not a venue) to neutralize both the IT and the regulatory veto. That is a sales-architecture choice, not a technology breakthrough.
→ **What it reveals / what's missing:** this is an **announcement, not adoption**. No named launch customer, no AUC, no volume, no pricing, no custodian named. "Go live in an hour" describes a sandbox/pilot, not a regulated production rollout (KYC/AML, state money-transmission/BitLicense, GENIUS/CLARITY-era posture all unaddressed). It's a repackaging of existing components (Digital Twin + X9.150 + custody) under a product SKU.

## [1] Competitors / peers
The "banks-offer-crypto-via-your-existing-core" lane is crowded: **Fireblocks** and **Fidelity Digital Assets**/**BNY** (custody-led), **IBM Digital Asset Haven** (Oct 2025, [[IBM launches Digital Asset Haven platform]]), **Coinbase** (institutional/prime + stablecoin tooling, [[Coinbase launches Coinbase Business stablecoin payment tools]]), **Zero Hash/Fortress/Paxos** (embedded crypto-as-a-service for fintechs), and core vendors **FIS/Fiserv/Jack Henry/Temenos** who can bolt crypto modules onto the cores Matera is trying to extend. On the stablecoin-into-core-rails angle its closest analog is its own **Circle/USDC** tie-up ([[Matera partners Circle to expand stablecoin payments in Latin America]], June 2025) and bank tokenized-deposit efforts ([[BNY explores tokenized deposits for payments network]]).
→ **Position:** catching-up to parity on capability; Matera's genuine edge is **distribution into the core** (it already runs instant payments at ~1/3 of Brazilian banks and claims 2 of top-3 global banks / 3 of top-10 US banks). The embedded-crypto BaaS players own the rails and compliance stack; Matera owns the ledger seat. The real question is whether "equal-standing balance in the ledger I already run" beats "a clean API from Zero Hash/Paxos" for a cautious bank. Second-order: as core vendors (Fiserv/FIS) add native stablecoin modules, Matera's side-car thesis weakens where a bank's incumbent core vendor offers the same.

## [2] Company history / fit
Matera (founded 1987, Brazil; ~1,000+ staff) is the infra behind Brazil's Pix/instant-payments wave and has pushed into the US (FedNow/RTP). Trajectory into digital assets is consistent: June 2025 Circle/USDC integration (first regional native TradFi–stablecoin link, [[Matera partners Circle to expand stablecoin payments in Latin America]]); March 2026 hire of a CSO for capital markets/IR/M&A ([[Matera appoints Roberto Otero Chief Strategy Officer]]) signaling a scale/possible-liquidity posture; July–Aug 2026 X9.150 QR software + open-sourcing. Workspace bundles all of it.
→ **Why Matera acts this way:** core-banking/payments licensing is a low-multiple, slow-growth commodity business. To earn a software-growth multiple (and justify the CSO/capital-markets build-out) Matera needs a new, higher-margin attach on top of its installed base — digital assets is that attach, and the Digital Twin ledger is the wedge it can sell without displacing itself. The US focus (region/us tag, BusinessWire) reflects where the regulatory tailwind + bank willingness-to-pay is largest post-2025.

## [3] Novelty / value-add / traction
Genuinely novel-ish: **unifying fiat + stablecoins + crypto + tokenized assets as peer balances in one production real-time ledger**, plus a **principal (bank-is-counterparty) trade engine** rather than routing to an exchange — that is a cleaner regulatory story than most CaaS. But little here is net-new tech: Digital Twin, X9.150 QR and custody are pre-existing; Workspace is the packaging + trade engine.
→ **Why the value-add may be thinner than it reads:** who captures the margin? The **custodian** (unnamed) and the **stablecoin issuer** (Circle) take economics; the **trade engine** monetizes spread/fees but a bank-principal model loads the bank with inventory/market/settlement risk it may not want. "Go live in an hour" is a demo metric; the binding constraint is legal/compliance sign-off, which Matera can't collapse. **Traction = zero disclosed** (no clients, volumes, custodian). Until a named regulated bank runs real customer flow, this is prior-art-repackaged-as-SKU, not proven value-add.

## [4] What's next / market sentiment
Watch for: first **named bank/CU** on Workspace in production; which **custodian(s)** (Fireblocks/BitGo/Anchorage/Coinbase) are integrated; whether the **trade engine** is principal or just routing; stablecoin coverage beyond USDC. Backdrop: US stablecoin/crypto rules firming (GENIUS Act; CLARITY Act stalled per [[Noah CEO weighs crypto regulation path after CLARITY Act fails]]) is pulling banks toward compliant crypto offerings — tailwind for exactly this product. Brazil's Drex/stablecoin-as-e-money proposals ([[Brazil central bank proposes regulating stablecoins as e-money]]) give Matera a second home-market vector.
→ **Why the market tilts this way / second-order:** regulatory clarity turns "offer crypto" from a reputational risk into a competitive must-have for mid-size US banks/CUs that can't build it — favoring packaged, core-adjacent vendors. **Counterintuitive risk:** the same clarity invites the big core vendors (Fiserv/FIS/Jack Henry) and the exchanges (Coinbase) to offer turnkey crypto, which could commoditize Matera's bundle and compress it back toward a low-margin core attach — i.e., the clarity that opens the door also lets bigger incumbents walk through it.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
1. **Any named launch customer?** Open — PR names no bank, CU or fintech live on Workspace. Until one runs real customer flow this is announced, not adopted.
2. **Which custodian(s) are integrated?** Open — "ready-made custody integrations" / "market-leading providers" but none named (Fireblocks? BitGo? Anchorage? Coinbase?). Material, since the custodian takes economics and sets the risk model.
3. **Is the trade engine principal or agency?** PR says customers "transact directly with the bank rather than a marketplace" — implies **principal** (bank is counterparty), which loads the bank with inventory/market/settlement risk. Not clarified how risk is hedged/offloaded.
4. **"Go live in an hour" — pilot or production?** Clearly a sandbox/pilot metric; it cannot collapse KYC/AML, state money-transmission/BitLicense and board/compliance sign-off. Marketing vagueness flagged.
5. **Is any component actually new?** Mostly no — Digital Twin (prod since before 2025), X9.150 QR (July 2026), custody integrations all pre-existed. Workspace = packaging + trade engine. Net-new = the unified-balance SKU + principal trade engine.
6. **Why "us" region for a Brazilian firm?** Launch is BusinessWire/US-targeted at US banks & CUs; US regulatory tailwind + willingness-to-pay is the target market. Brazil/Drex is a secondary vector.
7. **How is this different from the June-2025 Circle deal?** That was a stablecoin-payments (USDC into core rails) integration; Workspace is a broader digital-assets product (crypto + tokenized + a trade engine + custody), so **fresh**, not a reprint of s9170981d.
8. **What volumes/AUC/pricing?** Open — none disclosed. No way to size traction.
9. **Who captures the margin?** Custodian + stablecoin issuer (Circle) + trade-engine spread; Matera's durable take is the ledger/software attach. Risk: margin leaks to custodian/issuer, leaving Matera a thin platform fee.
10. **Does the side-car thesis survive core-vendor entry?** Open/risk — if Fiserv/FIS/Jack Henry/Temenos ship native stablecoin modules, a bank may not need Matera's extension on top of their incumbent core.
11. **Regulatory posture of the "bank as counterparty" model?** Claimed to keep trades "inside the institution's existing regulatory posture" — unverified; principal crypto trading can itself trigger new licensing/capital treatment.
12. **Which stablecoins/chains?** Open — USDC implied (Circle history); no mention of EURC, other issuers, or chains (Solana appears in the related X9.150 demos, not confirmed here).
13. **Is "equal-standing balance" real settlement or just display?** Claim that all assets are peer balances in one ledger — unverified whether that means atomic settlement or a unified view over siloed custody.
14. **Does the CSO/capital-markets hire signal an M&A/exit motive behind the SKU?** Analysis — March 2026 CSO for capital markets/IR/M&A suggests Matera is dressing up a growth narrative; Workspace supports a software-multiple story.
15. **Freshness verdict:** **FRESH** — distinct new product (2026-10-16), not a re-run of the June-2025 Circle note or the March-2026 leadership note.

Importance: 3/5 — Real, differentiated product (non-core-replacement unified ledger + bank-principal trade engine) from a vendor with genuine core-banking distribution and a strong regulatory tailwind, which lifts it above a routine launch. But it is an announcement with zero disclosed customers, custodians, volumes or pricing, and most components are pre-existing — repackaging, not a breakthrough. Caps it at mid.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Bank digital-asset enablement — infrastructure that lets regulated banks/credit unions offer stablecoins, crypto and tokenized assets alongside fiat without ripping out the core. The cited structural fact Matera leans on: Pix accounts for more than 40% of all electronic transactions in Brazil and Matera processes 5bn+ transactions/year for 250+ institutions (per Matera/PYMNTS, 2024, pre-Workspace — background, not a Workspace metric). No sourced TAM for the "banks-offering-crypto" sub-segment — no data; qualitatively the market is early and supplier-fragmented. Why now: a cluster of 2026 launches turning crypto-at-your-bank from pilot to product — Fiserv's Digital Asset Platform went **live 2026-10-01** (first use case Roughrider Coin, Bank of North Dakota's stablecoin; custody via VersaBank, chain Solana, infra Fireblocks, per GlobeNewswire/Yahoo Finance) — signals the demand Matera is chasing is real and already contested. Driver: regulatory thaw plus incumbent-core vendors (Fiserv) moving first forces independents to answer.

**Competitive landscape.** KPIs the layer runs on: institutions live in production, assets/chains supported, and whether custody+ledger+rails are bundled vs assembled (`[UNSOURCED]` for Matera's Workspace client count — none disclosed at launch, a de-PR flag). Basis of competition: distribution into existing cores + regulatory cover + single-pane UX (showing USDC next to USD in one account view via Matera's "Digital Twin" ledger). Players: (1) **core-incumbent** Fiserv — white-label, live, bundles VersaBank (OCC-chartered) + Fireblocks; (2) **embedded-infra APIs** Zero Hash (powers E*TRADE/Stripe/BlackRock crypto) and Fireblocks (80+ banks in live production, per Fireblocks, 2026); (3) **partner-pair routes** [[SaaScada and Zumo give UK banks regulated crypto route]] (2026-10-13, same week — Zumo custody/KYC + SaaScada cash accounts). Matera's position: niche/differentiated **(analysis)** — real-time-ledger-native (Digital Twin treats USDC and USD as equal-standing balances) and distributed through its existing Pix/core footprint, vs assembling a custody vendor on top; moat is switching costs/distribution into cores it already runs, not proprietary crypto tech (custody is integrated, i.e. partnered).

**Comps & multiples.** No deal/round/valuation in this news — it's a product launch, so no transaction multiple to compute (no data). Matera financials, for scale context not a multiple: 2023 revenue ~$77m, 4x growth since 2020; $100m from Warburg Pincus (majority stake) July 2024; $120m raised total (per fintechfutures/seedtable/PYMNTS, 2024). No post-money valuation disclosed → `[UNSOURCED]`; EV/Revenue, EV/EBITDA, P/E all = no data (private, no public comps aligned). Internal comps (`[[wikilink]]`): [[Matera partners Circle to expand stablecoin payments in Latin America]] (2025-06, the USDC/Digital Twin groundwork Workspace productizes); [[SaaScada and Zumo give UK banks regulated crypto route]] (bundled bank-crypto route, Europe); [[Deutsche Bank prepares crypto custody launch in Germany]], [[Citi details stablecoin checkout with Coinbase]] (incumbent demand side). Distribution not computed — no comparable multiples; qualitative comparison only.

**Risk flags.**
1. **Incumbent-core disintermediation** — Fiserv's platform is already live (2026-10-01) and sits inside the US core-banking stack Matera is trying to extend; for the many institutions on Fiserv, the crypto add-on is an upsell from their existing vendor, squeezing Matera's land-and-expand into US cores it doesn't own.
2. **Dependence on someone else's rails** — Workspace bundles "custody integrations," i.e. custody is partnered not owned (Matera is a ledger/rails layer); whoever holds the keys (and the Circle/USDC relationship) captures the regulated-custody economics and the fraud/reserve liability, leaving Matera on thinner middleware margin.
3. **Announced vs adopted** — zero named live clients, pricing, or volumes at launch ("available now" ≠ in production); classic de-PR gap for a platform whose whole pitch is "shortest path," which is unprovable without an adoption count.

**What this changes (idea-lens).** The bank-crypto layer is consolidating from pilots into shelf-ready product in a single 2026 quarter (Fiserv live, Matera launching, SaaScada/Zumo pairing) — this is a land-grab for who becomes the default "crypto tab" vendor inside the core, not a re-rating of any one name. Falsifiable thesis **(analysis)**: Matera's edge is real-time-ledger-native unification, so it should win where the buyer already runs Matera's core/Pix stack (Brazil, LatAm) and lose US core accounts to Fiserv. Trigger to watch: first named Workspace production client + whether it's a Matera-core bank (thesis holds) or a greenfield US win (thesis stronger) vs none by 2027 (thesis wrong — PR without pull).

Sources: https://www.businesswire.com/news/home/20261016469184/en/Matera-Launches-Matera-Workspace · https://www.pymnts.com/real-time-payments/2024/exclusive-matera-builds-on-pix-success-with-digital-twins-and-qr-codes-in-us-expansion/ · https://www.fintechfutures.com/venture-capital-funding/brazil-s-matera-lands-100m-investment-from-warburg-pincus · https://finance.yahoo.com/markets/crypto/articles/fiserv-digital-asset-platform-live-210019596.html · https://stablecoininsider.org/zero-hash-review-2026-the-regulated-infrastructure-platform-behind-wall-streets-crypto-ambitions/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
