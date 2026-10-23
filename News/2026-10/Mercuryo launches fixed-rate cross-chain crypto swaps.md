---
title: "Mercuryo launches fixed-rate cross-chain crypto swaps"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/mercuryo
  - industry/crypto
  - industry/blockchain
  - region/global
  - type/product
sources:
  - https://mercuryo.io/explore/announcements/mercuryo-launches-swaps
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sa9f3de52
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Mercuryo launches fixed-rate cross-chain crypto swaps

> [!info] 2026-10-23 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Mercuryo launches fixed-rate cross-chain crypto swaps. The service supports 38 tokens across 21 blockchains, offering more than 1,400 trading pairs. Users can swap assets at a fixed quoted amount without slippage, with no manual bridging required.

## Первоисточники

### mercuryo.io
<https://mercuryo.io/explore/announcements/mercuryo-launches-swaps>
*404 слов · direct*

Fixed quotes and cross-chain—the new Swap from Mercuryo
No more swapping into “somewhere around what you expected.” Instead of chain hopping and quotes that slip away, swap across chains and get exactly what's promised. Every time.
Most swaps take their time, then take a cut
You get a quote, confirm, and by the time it settles the market has moved—the amount you actually receive is usually a bit less than promised. And that's on top of the hassle of switching between chains and wasting gas doing it.
Mercuryo Swaps fixes both problems at once.
See the number before you commit
A fixed quote is exactly that: the amount shown is the amount you get. Zero slippage, no estimate that shifts with network conditions. Lock it in, confirm, and the swap settles at that number—no slippage, no surprises.
Cross-chain, without the chain-hopping
BTC, ETH, USDT, USDC, POL, TRX, and BNB—swap straight across chains like Bitcoin, Ethereum, BNB Chain, Polygon, Arbitrum, and Tron. No manual bridging, no juggling wallets. Pick what you have and what you need; Mercuryo handles the route in one move.
How it works
Access the Mercuryo Widget here 
Jump to the Swaps tab
Choose the assets you want to Swap
See your fixed quote
Confirm and swap, done!
Questions and answers
What makes a “fixed quote” different from a regular swap quote?
Most swaps—including on DEXs—only give you an estimate. The final amount depends on slippage, and it can shift between the moment you confirm and the moment the transaction settles. Mercuryo locks in your quote before you commit, so there is zero slippage, and the number you see is the number you get.
Which assets and networks can I swap between?
Swaps currently supports 38 tokens (some tokens are present in different networks)—including BTC, ETH, USDT, USDC, POL, TRX, and BNB—across 21 chains, such as Bitcoin, Ethereum, Tron, Base, Arbitrum, BSC, and Polygon, with over 1,400 pairs available and more on the way.
Do I need to complete KYC to swap?
Swaps runs on the same verification as the rest of Mercuryo. If you already buy or sell crypto in the app, you're ready to swap. New users go through Mercuryo's standard identity verification first.
Which countries can I swap in right now?
Mercuryo Swaps is currently available across North America (except USA), Latin America, Asia, Africa, Australia, Middle East. We're constantly working on expanding, so keep an eye on us.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Mercuryo launches fixed-rate cross-chain crypto swaps
_Analytical notes (not a post). Importance: 2/5._

> NB: "Mercuryo" = the crypto on/off-ramp & payments firm (CEO Petr Kozyakov, parent NanduQ), NOT Mercury the US startup-neobank, NOT Mercury Fund the VC.

## [0] What exactly happened (de-PR'd)
Mercuryo added a **Swaps** tab to its existing widget/app: swap one token for another, including across chains, at a **fixed quote** (the amount shown = the amount received, zero slippage, no manual bridging). Scope: **38 tokens across 21 chains, ~1,400 pairs** (BTC, ETH, USDT, USDC, POL, TRX, BNB; chains incl. Bitcoin, Ethereum, Base, Arbitrum, BSC, Polygon, Tron, Solana). Runs on Mercuryo's standard KYC. Geography is restricted: **not available in US, UK, or the EEA** — live in LatAm, most of Asia, Africa, Australia, Middle East, and "North America except USA."
- **What it actually is (de-PR'd):** this is a **CEX-style custodial/intent swap wrapped in a widget**, not a new on-chain protocol. The "fixed quote" is a **quoted price that Mercuryo guarantees** — per the Swaps terms, a quote is valid ~6 hours and liquidity is "sourced through a leading cryptocurrency exchange" with AML controls. So "zero slippage" ≠ some novel MEV/routing breakthrough; it means **Mercuryo (or its backing exchange) is the counterparty and eats the execution risk**, pricing a spread into the quote. Fees accrue in stablecoin terms regardless of assets swapped (illustratively ~$6 on a $1,000 swap ≈ ~0.6% spread). (analysis)
- **Why framed this way:** Mercuryo is an **on/off-ramp** whose core job is fiat↔crypto. Swaps lets it capture the *next* step — users moving between tokens/chains — **inside the same KYC'd session**, so value doesn't leak out to a DEX/bridge. The PR anchors on "slippage + bridging pain," the real framing is **retention + wallet-share of its existing on-ramp funnel**.
- **Live, not just announced:** the feature is shipped in the widget — but there are **no disclosed Swaps volumes, user counts, or pair-level liquidity depth**, so adoption is unproven.

## [1] Competitors / peers
Two distinct arenas, and Mercuryo sits awkwardly between them:
- **On-ramp / fiat-crypto peers who also route cross-chain:** [[MoonPay launches MoonPay Trade digital asset platform]] (single API across 200+ chains, cross-chain routing + settlement), [[Bitget Wallet launches APAC crypto card]], MoonPay/Transak/Ramp. These are the true comp set — ramps extending into swap/routing.
- **Pure cross-chain swap/bridge aggregators:** Li.Fi/Jumper, [[Squid raises $6 million for cross-chain consumer infrastructure]] ($6B+ routed, 100+ chains, 1M+ users), deBridge, Rango (70–85+ chains, single-signature BTC↔EVM), THORChain (trustless native-asset L1 via RUNE pools), Rubic, Bungee/Socket, CoW Swap (intent-based near-zero slippage on stables). These are **broader (30–85+ chains vs 21) and mostly non-custodial**.
- **Position: catching up / parity-at-best on tech, differentiated on distribution.** 21 chains / 38 tokens is **modest** vs Rango's 70–85 or Squid's 100+. Mercuryo's edge is NOT route coverage — it is the **captive KYC'd user base and widget embedded in Ledger/MetaMask/Trust Wallet/Revolut**. (analysis)
- **Second-order:** aggregators compete on *route optimality and chain breadth*; Mercuryo competes on *custody + compliance + one-session UX*. "Fixed quote / zero slippage" is a **UX/marketing claim, not a moat** — CoW Swap and intent-based venues already deliver near-zero slippage, and any custodial venue can quote a fixed price by pricing in a spread. So the differentiation is **who the user already is (an on-ramp customer) rather than a better engine.**

## [2] Company history / fit
Mercuryo is a crypto payments/on-ramp infrastructure firm: per 2025 data, **148 countries, ~12.5M registered users (~1.3M green-KYC wallets), ~300 staff, ~$2B total volume, ~$15M revenue generated for partners**; integrations with Ledger, MetaMask, Trust Wallet, Revolut (Revolut Pay rolled out Feb 2025), and exchange partners (Binance, Bybit historically). Parent entity NanduQ (per PitchBook, early-2026). (public funding trackers show only early 2020–21 rounds — likely stale.)
- **Why this move fits:** an on-ramp is a **commodity, thin-take-rate** business fighting MoonPay/Transak/Ramp on fee. The structural pressure is to **widen wallet-share per KYC'd user** — if a user already verified to buy crypto, letting them *swap* without leaving is pure incremental take-rate at near-zero CAC. Swaps is the logical adjacency after on-ramp + card + off-ramp. (analysis)
- Consistent with its 2025 stablecoin-payments push ("stablecoins moving beyond crypto") — Swaps keeps users and stablecoin balances **inside Mercuryo's rails** rather than bleeding to external DEXs/bridges.

## [3] Novelty / value-add / traction
- **Novelty: low.** Fixed-quote custodial cross-chain swaps are **not new** — SimpleSwap/ChangeNOW/Changelly have offered fixed-rate quoted cross-asset swaps for years; aggregators solve bridge+swap atomically; intent venues already minimize slippage. Mercuryo's version is **narrower in coverage** than the aggregators and **custodial** vs their non-custodial.
- **Real value-add = distribution + compliance, not mechanism.** For a *non-crypto-native user inside the Mercuryo/Revolut/MetaMask funnel*, a one-tap KYC'd fixed-price swap genuinely removes friction (no bridge UX, no gas juggling, no slippage anxiety). That is real but **incremental UX**, not category-defining.
- **Traction: unproven.** Zero disclosed Swaps-specific metrics. The 12.5M user base is a *ceiling of reach*, not evidence of swap adoption.
- **Who captures the margin:** Mercuryo earns the **spread** (fees accrued in stablecoin terms); the **execution/liquidity is outsourced to a backing exchange**, so Mercuryo is a **distribution + compliance wrapper on someone else's liquidity**. That caps the economics — it's a reseller spread, not protocol/liquidity rent — and leaves Mercuryo dependent on its liquidity partner's pricing. (analysis)

## [4] What's next / market sentiment
- Expect expanded token/chain coverage ("more on the way") and possible geo-expansion, but **US/UK/EEA exclusion** (the richest, most regulated markets) signals this is a **licensing/regulatory-gated** product — a structural ceiling on near-term TAM.
- **Sentiment:** neutral. This is a sensible, defensive **retention/monetization feature** by a scaled on-ramp, not an innovation event. Cross-chain swap UX is converging toward "invisible infrastructure" (Squid's thesis) — ramps bolting on swap is now **table stakes** (MoonPay Trade did the broader version in May 2026).
- **Risks / counterintuitive:** (1) custodial + "quote valid 6h" + exchange-sourced liquidity means **Mercuryo bears market-move and settlement risk** on the fixed quote — profitable in calm markets, loss-exposed in volatility unless the spread/hedging is tight; (2) competing on "zero slippage" invites a **fee/spread race** against both non-custodial aggregators (which can be cheaper) and regulated rivals; (3) narrow chain coverage means power users still leave for Li.Fi/Rango — so Swaps mainly defends the *casual* on-ramp user, a lower-value cohort. (analysis)

## Top challenge/extra questions (10–15, second-order) — see challenge file.

## Sources
- Mercuryo announcement (primary, dumped in note): https://mercuryo.io/explore/announcements/mercuryo-launches-swaps
- Mercuryo Swaps product & terms: https://mercuryo.io/swaps ; https://mercuryo.io/legal/terms-swaps/
- PRNewswire launch release: https://www.prnewswire.com/news-releases/mercuryo-launches-swaps-for-seamless-movement-between-digital-tokens-302916736.html
- Global Fintech Series coverage: https://globalfintechseries.com/banking/digital-payments/mercuryo-launches-swaps-for-seamless-movement-between-digital-tokens/
- TRON/KuCoin coverage (21 networks): https://www.cointrust.com/market-news/tron-adds-mercuryo-support-for-cross-chain-swaps-across-21-networks
- Mercuryo scale/2025: https://en.cryptonomist.ch/2025/12/15/mercuryo-2025/ ; https://www.prnewswire.com/news-releases/mercuryo-data-shows-stablecoins-moving-beyond-crypto-to-power-digital-payments-302833743.html
- Revolut Pay integration (Feb 2025): https://mercuryo.io/press/mercuryo-launches-revolut-pay-on-ledger-metamask-trust-wallet
- Company profile/parent: https://pitchbook.com/profiles/company/438799-15
- Competitor landscape: https://coingape.com/best-cross-chain-swap-platforms/ ; https://debridge.com/learn/guides/cheapest-crypto-swap/ ; https://stablecoininsider.org/best-cross-chain-aggregators-for-2026/
- Corpus priors: [[MoonPay launches MoonPay Trade digital asset platform]], [[Squid raises $6 million for cross-chain consumer infrastructure]], [[Bitget Wallet launches APAC crypto card]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is "fixed quote / zero slippage" actually novel?** No. Custodial fixed-rate swap shops (SimpleSwap, ChangeNOW, Changelly) have quoted guaranteed cross-asset rates for years, and intent venues (CoW Swap) deliver near-zero slippage non-custodially. It's a UX/marketing frame, not a mechanism breakthrough. **Weight: lowers novelty.**

2. **Who is the counterparty to the "fixed" price?** Mercuryo / its backing exchange. The quote is guaranteed because liquidity is "sourced through a leading cryptocurrency exchange," so Mercuryo prices a spread and absorbs execution/market risk — this is a custodial quoted swap, not an on-chain atomic route. (open on which exchange)

3. **Is this live or announced?** Live — the Swaps tab is shipped in the widget. But **no Swaps-specific volume/user/pair-depth metrics disclosed**, so adoption is unproven.

4. **How does coverage compare to real cross-chain aggregators?** Weak: 21 chains / 38 tokens / 1,400 pairs vs Rango 70–85+ chains, Squid 100+ chains ($6B+ routed), Li.Fi 30+. Mercuryo is narrow; power users still have reason to leave.

5. **So what is the real edge?** Distribution + compliance: 12.5M KYC'd users embedded in Ledger/MetaMask/Trust Wallet/Revolut. The moat is the captive on-ramp funnel, not the swap engine.

6. **Who captures the margin in the stack?** Mercuryo earns a **reseller spread** (fees accrued in stablecoin terms, ~0.6% illustrative); liquidity/execution is outsourced. Spread rent, not protocol/liquidity rent → capped economics, dependent on the liquidity partner.

7. **Why exclude US / UK / EEA?** Almost certainly licensing/regulatory gating. These are the highest-value markets, so the addressable base for Swaps is structurally capped near-term. **Weight: caps importance.**

8. **What does Mercuryo stay silent about?** Swaps volume, take-rate/spread size, liquidity partner identity, pair-level depth, and how it hedges the 6-hour fixed-quote window. Silence on economics + adoption = PR-forward.

9. **Does a 6-hour fixed quote create risk?** Yes — in volatile markets a guaranteed quote exposes Mercuryo (or its liquidity partner) to adverse moves. Fine in calm markets; a loss vector if hedging/spread is loose. (analysis)

10. **Is this just following MoonPay?** Largely. [[MoonPay launches MoonPay Trade digital asset platform]] (May 2026) shipped the broader single-API cross-chain routing/execution version. Ramps bolting on swap is now table stakes, not a first-mover event.

11. **Does it fit Mercuryo's strategy?** Yes, tightly — a thin-take-rate on-ramp widening wallet-share per already-KYC'd user at near-zero CAC; keeps tokens/stablecoins inside its rails instead of leaking to DEXs/bridges.

12. **Is there a duplicate in the corpus?** No. No prior Mercuryo note; no prior note covers this Swaps launch. MoonPay/Squid are peers, not the same event. **Verdict: fresh.**

13. **Could "no manual bridging" mislead?** It's accurate as UX (Mercuryo handles routing), but it's achieved via custody/intermediation, not trustless bridging — the user trusts Mercuryo, not a bridge protocol. Risk profile shifts from smart-contract risk to counterparty risk.

14. **What's the second-order competitive effect?** Competing on "zero slippage / low fee" invites a spread race against cheaper non-custodial aggregators and regulated rivals; Swaps mainly defends the *casual* user cohort — a lower-value, more price-elastic segment.

15. **Why does this matter at all, if novelty is low?** Only as a marginal monetization/retention signal from a scaled ramp and a data point in the "ramps becoming invisible cross-chain infra" trend — not a standalone meaningful event.

---
**Importance: 2/5** — Shipped, real, strategically sensible retention/monetization feature from a genuinely scaled on-ramp (~12.5M users), but **low novelty** (fixed-rate custodial swaps and slippage-minimizing routing long exist), **narrower coverage** than real aggregators, **custodial reseller-spread economics**, **no disclosed traction**, and a **US/UK/EEA-excluded** addressable base. Follows MoonPay Trade rather than leading. Fresh, but minor.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Mercuryo sits at the intersection of two crypto-infra subverticals: fiat on/off-ramps and cross-chain swap/bridge aggregation. On-ramps: sized at ~$8.4bn in 2025 heading to ~$34.6bn by 2034 at ~17% CAGR per DataIntelo/Spark-cited figures (via web, as of 2026) — but estimates diverge sharply (a second source puts it at $10.2bn→$17.7bn / 6.3% CAGR), so treat any single TAM as soft; use the direction (secular growth) not the level. Structure: the on-ramp layer is fragmented and commoditising — MoonPay, Transak, Ramp Network, Coinbase Onramp, Paybis and now Mercuryo all compete on fee, country/token coverage and conversion, with low switching costs for the end user and the real moat living in B2B distribution (wallet/exchange integrations) and licensing. The cross-chain swap/bridge layer is a separate, aggregator-dominated market (LI.FI, Jumper, Squid, deBridge, Rango, Bungee) that routes across underlying bridges. Why now: Mercuryo is extending from pure fiat-crypto ramping into token-to-token movement, i.e. moving up the stack into the swap/bridge value chain rather than defending a shrinking ramp take-rate — a defensive-offensive land-grab as ramp economics compress.

**Competitive landscape.** Sector KPIs: ramp conversion rate, take rate / spread per transaction, country+token coverage, and (for swaps) effective slippage + route success rate. Basis of competition: coverage breadth, price/spread transparency, and B2B distribution. Mercuryo's Swaps: 38 tokens / 21 chains / 1,400+ pairs, pitched on fixed quotes + zero slippage + no manual bridging (mercuryo.io / PRNewswire, 2026-10). Peer moves: MoonPay (30M+ users, 500+ B2B customers) has been aggressively consolidating — six acquisitions since early 2025 incl. Helio (~$175M), Iron (~$100M), Sodot (~$100M), DFlow, Dawn Labs — and pushing Headless Onramps and AI-agent/ChatGPT rails (2026-05). On the DeFi-native side, Rango quotes BTC↔EVM in one sign across 85+ chains; LI.FI spans 60+ chains / 20+ bridges. Position: Mercuryo is a mid-tier ramp player (Series A, acquired by NanduQ Jan 2026 per PitchBook/Tracxn) extending into swaps — niche/catching-up versus MoonPay's scale and versus pure-play aggregators' chain breadth. Moat (analysis): the one genuine edge is the shared-KYC rail — Swaps reuses existing Mercuryo verification, so its on-ramp userbase can swap with zero extra onboarding (switching cost / distribution), not technical routing superiority.

**Comps & multiples.** Mercuryo is private, Series A-scale with only ~$10.5M lifetime funding disclosed (Tracxn) and no revenue/valuation public → EV/Revenue, P/S, price-per-user all **no data / [UNSOURCED]**; the Jan-2026 NanduQ acquisition price is undisclosed. Peer financials are mostly private too: MoonPay raised $643M+ (last known ~$3.4bn round valuation, 2021 — likely stale, mark as round valuation not current mark), Ramp Network ~$120M raised, Transak ~$40M (Tether-backed). With no verifiable numerator/denominator pair on any of these, **distribution not computed — qualitative comparison only**: Mercuryo is an order of magnitude smaller by funding than MoonPay and roughly Transak-scale. Internal comps (same sub-vertical, base): [[MoonPay launches Headless Onramps for one-tap crypto checkout]], [[MoonPay launches MoonPay Trade digital asset platform]], [[MoonPay acquires crypto security startup Sodot for $100 million]], [[dLocal and Alchemy Pay partner on crypto-fiat in LatAm]], [[BloFin partners with Checkout.com for crypto fiat on-ramp]].

**Risk flags.**
- *"Fixed quote / zero slippage" is a spread, not a free lunch.* A guaranteed output price means Mercuryo (or its liquidity provider) absorbs execution + bridge risk and prices it into an upfront spread. The PR is silent on fee/spread economics — the de-PR question is whether "zero slippage" is cheaper than a DEX aggregator's slippage, or just repackages the cost. Watch for an opaque or wide spread as the actual revenue line.
- *Disintermediation / stack-layer capture.* Mercuryo doesn't appear to run its own bridges; "handles the route in one move" implies reliance on third-party bridge/aggregator rails. If true, margin and reliability (bridge exploits are the single largest loss category in crypto) sit with a layer it doesn't control — a dependence-on-someone-else's-rails risk, and bridge-hack headline risk it inherits without owning the security.
- *Regulatory + geo concentration.* Swaps is explicitly unavailable in the US, UK and EEA — i.e. all the highest-value, best-regulated markets are excluded, leaving LatAm/Asia/Africa/MENA. That caps the addressable base and signals unresolved licensing/MiCA/token-listing exposure; ownership change (NanduQ) adds integration/strategic-uncertainty on top.

**What this changes (idea-lens).** (analysis) This is a ramp provider trying to re-rate itself as swap infrastructure — the tell that on-ramp take rates are compressing hard enough that incumbents must move up-stack to defend revenue. Falsifiable thesis: if Mercuryo later discloses swap volume/spread that materially beats its ramp economics, the "ramp → swap" pivot is real; if Swaps stays a retention feature with no disclosed volume, it's defensive feature-matching against MoonPay. Trigger to watch: any spread/fee disclosure, a B2B widget distribution deal for Swaps, or expansion into US/EEA (which would require the licensing it currently lacks). What breaks the thesis: a major third-party bridge exploit hitting routed Swaps flow.

Sources: https://mercuryo.io/explore/announcements/mercuryo-launches-swaps · https://www.prnewswire.co.uk/news-releases/mercuryo-launches-swaps-for-seamless-movement-between-digital-tokens-302916738.html · https://pitchbook.com/profiles/company/438799-15 · https://tracxn.com/d/companies/mercuryo · https://dataintelo.com/report/crypto-on-ramp-market · https://www.spark.money/research/crypto-on-off-ramp-market-landscape · https://transak.com/blog/best-white-label-crypto-on-off-ramp-providers · https://eco.com/support/en/articles/14800720-best-bridge-aggregators-2026-cost-speed
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
