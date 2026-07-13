---
title: "lex: Curve and Maker launch new stablecoin and lending products"
date: 2026-06-22
tags:
  - company/curve
  - company/maker
  - industry/defi
  - region/global
  - type/commentary
sources:
  - https://substack.com/redirect/1c5b9700-894b-4c38-9235-595edba887b7
status: enriched
n_mentions: 1
channels:
  - "lex"
story_id: see0d7be6
month: 2026-06
enriched: true
importance: 2
freshness: fresh
---

# lex: Curve and Maker launch new stablecoin and lending products

> [!info] 2026-06-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: lex

## Агрегированный текст (из дайджестов)

[lex] Web3: Curve releases stablecoin, Maker launches lending; ex-Facebook team deploys Sui mainnet, taking on Aptos & 0L

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/1c5b9700-894b-4c38-9235-595edba887b7>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: lex — "Curve releases stablecoin, Maker launches lending"
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS VERDICT: FRESH** (no prior note covers Curve Finance crvUSD / Maker→Sky USDS DeFi products; the only adjacent corpus note is the Sky-ecosystem yield play [[Osero raises $13.5 million for stablecoin yield infrastructure]]). BUT the lex framing is **stale-as-news**: nothing here is a 2026 launch — see [0]. Note the tag `company/curve` in this vault refers to the **Curve digital wallet** (Lloyds acquisition), and `company/sky` to a blockchain-payments startup — NOT Curve Finance / MakerDAO. Different entities; do not cross-link.

## [0] What exactly happened (de-PR'd)
The headline is wrong on both counts; treat it as a lazy re-framing of a multi-year DeFi build-out, not a product drop.
- **Curve's "stablecoin" is not new.** crvUSD (CDP-style, overcollateralized) has been **live since May 2023**. Its real differentiator is **LLAMMA** "soft liquidation" — collateral is spread across AMM price "bands" and swapped gradually crvUSD↔collateral as price moves, allowing partial liquidation *and* de-liquidation (recovery) instead of one hard wipe-out. The genuinely newer wrapper is **scrvUSD** (savings crvUSD, live ~Nov 2024) routing a slice of crvUSD interest to holders. **LlamaLend** isolated lending markets shipped in 2024.
- **Maker's "lending" is not new either.** Maker rebranded to **Sky on 2024-08-27** (Rune Christensen's "Endgame" Phase 1); DAI got a sibling **USDS**, yield via the **Sky Savings Rate (SSR)** on sUSDS. The lending arm is **Spark / SparkLend**, live since **May 2023**, formalized as the first SubDAO in May 2024. The newer 2025-26 pieces are Spark's **Liquidity Layer**, an **SPK token/airdrop (~Jun 2025)**, a push into **off-chain/institutional lending**, and the **forced DAI→USDS exchange migration (Apr 2026)** — billed as the largest stablecoin conversion in crypto history.
- **Why framed this way:** an FT/lex Web3 roundup compresses an ongoing trend (DeFi stablecoins maturing into full money-markets with savings rates) into "two launches." The accurate 2026 angle is **scale/traction, not novelty**: USDS ~$5–9B, Spark ~$9–10B TVL — vs crvUSD still a niche ~$180M. (analysis)

## [1] Competitors / peers
DeFi/stablecoin caps & yields, ~mid-2026 (numbers vary by source/date — flagged):
- **USDT** (Tether, fiat-reserve): ~$186–188B, ~58–60% share, no native yield. Dominant; pressured in EU by MiCA.
- **USDC** (Circle, fiat-reserve): ~$75–78B, outgrew USDT in % terms 2 years running; MiCA beneficiary.
- **USDe** (Ethena, synthetic/delta-hedged): ~$4.5B late-Jun 2026, **down ~40–60% from a ~$14.5B 2025 peak** after the Oct 2025 crash + Aave-Pendle loop unwind. Native sUSDe yield.
- **USDS+DAI** (Sky, CDP): ~$5.4B (early-2026) to ~$9B (mid-2026 framing); SSR ~3.75–4.5% APY. Top-5 stablecoin / "largest decentralized."
- **crvUSD** (Curve, CDP): ~$180M ATH supply; scrvUSD briefly "highest risk-free DeFi rate" (Jul 2025).
- **Reality check:** lumping crvUSD (~$180M) and USDS (~$5–9B) in one headline overstates Curve by ~2 orders of magnitude. They are not the same weight class. (analysis)
- **Why the landscape is this way:** fiat-reserve incumbents (USDC/USDT ≈ 92% of ~$320B total supply) win on liquidity + regulatory fit (GENIUS Act US, MiCA EU); yield/synthetic coins (USDe) are fragile to leverage unwinds; CDP coins (USDS, crvUSD) trade decentralization + on-chain yield for scale. The margin in DeFi stablecoins is captured by whoever controls **distribution + the savings rate as a policy lever**, not by the mint mechanism. (analysis)

## [2] Company history / fit
- **Curve Finance** — AMM since 2020 (Michael Egorov); crvUSD May 2023; LlamaLend 2024; scrvUSD Nov 2024. Carries real dents: a ~$700k LlamaLend CRV-long bad-debt shortfall after the Oct 2025 crash → soft-liquidation is not loss-proof.
- **MakerDAO → Sky** — DAI live since 2017; SparkLend May 2023; Spark first SubDAO May 2024; Sky rebrand Aug 2024; USDS Sep 2024; forced DAI→USDS migration Apr 2026. The Sky ecosystem is actively funding distribution — it led the **$13.5M round into Osero** to embed the Sky Savings Rate into wallets/neobanks ([[Osero raises $13.5 million for stablecoin yield infrastructure]]).
- **Why they act this way:** both face commoditized mint mechanisms, so value migrates to **savings-rate distribution and lending integrations** — hence the savings wrappers (scrvUSD, sUSDS) and the Spark/Osero distribution push. (analysis)

## [3] Novelty / value-add / traction
- **Genuinely novel (but old):** LLAMMA soft/de-liquidation (~3 yrs old). **Newer:** scrvUSD (Nov 2024), Spark Liquidity Layer + SPK + institutional lending (2025-26), forced DAI→USDS migration (Apr 2026).
- **Traction split:** winners are USDS (~$5–9B) and Spark (~$9–10B TVL); crvUSD stays niche (~$180M). The article's "two launches" premise is better read as DeFi stablecoins maturing into money-markets.
- **Where margin is captured / what breaks it:** yields are partly **subsidized** (fee-switch redirection, token incentives) — sustainability is the open question. Soft-liquidation's safety claim was dented by Oct-2025 bad debt. Without scaled integrations crvUSD supply stays small; USDS scale depends on distribution deals (Osero/Spark) holding. (analysis)

## [4] What's next / market sentiment
- **Sky:** finish DAI→USDS migration; Spark deeper into RWA/institutional lending; SSR as a rate lever vs USDC/USDT.
- **Curve:** scrvUSD growth + bad-debt remediation; crvUSD likely stays niche absent integrations.
- **Ethena:** fee-switch/ENA buybacks targeted Q3 2026; rebuilding from ~$4.5B.
- **Macro:** GENIUS Act (US) + MiCA (EU) favor regulated fiat coins (USDC) for off-chain scale; synthetic/CDP coins stay DeFi-native rails. **Counterintuitive:** the "largest decentralized stablecoin" crown (USDS) is a small slice of a ~$320B market dominated by exactly the centralized issuers DeFi set out to displace. (analysis)

## Sources
See /tmp/chl_curve-maker.md for red-team questions and full URL list. Key URLs:
- crvUSD / LLAMMA: https://www.curve.finance/crvusd · https://docs.curve.finance/developer/crvusd/llamma-explainer
- scrvUSD: https://news.curve.finance/introducing-scrvusd/ · https://cointelegraph.com/news/curve-finance-launches-savings-crv-usd-yield-bearing-stablecoin
- crvUSD mainnet (May 2023): https://www.coindesk.com/tech/2023/05/03/curve-finance-deploys-native-stablecoin-on-mainnet
- Maker→Sky: https://blockworks.com/news/maker-rebrands-as-sky-dai-will-be-changed-to-usds · https://www.theblock.co/post/313235/makerdao-mkr-sky-dai-stablecoin-usds
- DAI→USDS migration (Apr 2026): https://blockeden.xyz/blog/2026/04/03/dai-usds-migration-makerdao-sky-protocol-stablecoin-rebrand/
- Spark TVL: https://defillama.com/protocol/spark · https://thedefiant.io/news/defi/spark-launches-institutional-lending-products-in-off-chain-expansion
- USDC > USDT growth: https://www.coindesk.com/markets/2026/01/06/circle-s-usdc-outpaces-growth-of-tether-s-usdt-for-second-year-running
- USDe post-crash: https://www.coingecko.com/en/coins/ethena-usde

Related corpus notes (different entities/adjacent themes): [[Osero raises $13.5 million for stablecoin yield infrastructure]], [[MetaMask launches mUSD stablecoin with M0 and Bridge]], [[Coinbase explores native Base token, partners with Google]] (USDC onchain lending), [[Paxos proposes USDH stablecoin for Hyperliquid with HYPE buybacks]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. Is anything here *actually* a 2026 launch? — No. crvUSD (May 2023), LlamaLend (2024), scrvUSD (Nov 2024), SparkLend (May 2023), USDS (Sep 2024) all predate the article. Only *scale* is new. The headline is evergreen framing, not news.
2. Does the 2026-06-22 date map to a real event, or is it a roundup blurb? — Appears to be a lex Web3 roundup line, not a discrete launch. (open / likely evergreen)
3. USDS market cap: ~$5.4B (early-2026) or ~$9B (mid-2026)? — Range across sources; lock to one DefiLlama figure for the date before quoting. (open)
4. Is "USDS = largest decentralized / 3rd-largest overall" true given USDe ~$4.5B? — Plausibly the largest *decentralized* coin, but "3rd overall" is marketing-adjacent; rank-check DefiLlama. (open)
5. USDe cap on the exact date — sources span $4.47B–$14B by date. Use ~$4.5–6B for mid-2026. (open)
6. crvUSD "$181M ATH supply" vs "$69M from minting markets" — different metrics (total supply vs mint-only); do not conflate. Answered.
7. Does scrvUSD's "highest risk-free DeFi rate" (Jul 2025) still hold in Jun 2026? — Likely stale; rates move. (open)
8. SparkLend protocol launch (May 2023) vs Spark SubDAO formalization (May 2024) — distinct. Answered.
9. Is "Spark $9.74B total" double-counting savings + SparkLend + SLL? — Verify no overlap before quoting a single TVL number. (open)
10. Does the item mention Curve's ~$700k LlamaLend bad debt (Oct 2025 crash)? — Almost certainly not; omitting it is PR. Soft-liquidation is not loss-proof. Answered (counterweight).
11. Was the DAI→USDS migration voluntary or forced/exchange-driven (Apr 2026)? — Reported as forced on exchanges; "largest conversion in history" is partly mechanical, not organic adoption. (open)
12. What is the SSR APY *as of Jun 2026* (vs 3.75–4.5% early 2026)? — (open)
13. Are crvUSD/USDS yields sustainable or subsidized (fee-switch + token incentives)? — Partly subsidized; this is the durability question. (open)
14. Do USDS/crvUSD/USDe qualify under GENIUS Act / MiCA for US/EU off-chain distribution, or are they confined to DeFi rails? — Likely DeFi-confined; limits scale vs USDC. (open)
15. Sourcing hygiene: several figures came from SEO/aggregator pages (Fool, Ticker Report). Replace with DefiLlama / Sky / Curve official / Messari before any number is published. Answered (caveat).

Importance: 2/5 — No genuine new event: every "launch" is 2023–2024, only scale changed; coverage is a one-line roundup blurb with 1 mention. crvUSD is a tiny niche (~$180M) and Sky/USDS, while a real top-5 stablecoin, was not the subject of a fresh development here. Marked fresh (no duplicate in corpus) but low-weight: a trend-marker for "DeFi stablecoins become money-markets," not a standalone story.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** DeFi/CDP stablecoins sit inside a ~$321bn total stablecoin market (per DefiLlama dashboard, Apr 2026), but fiat-reserve USDC+USDT capture ~90% of supply; crypto-collateralized/algorithmic coins are only ~6–8% of supply (per DefiLlama via eco.com, 2026) — i.e. the entire CDP/synthetic category the protagonists compete in is a ~$20–25bn slice. Structure is **two-tier**: a consolidated reserve-coin oligopoly (liquidity + regulatory fit) above a fragmented decentralized tail (Sky USDS, crvUSD, Aave GHO, Ethena USDe) competing on on-chain yield and composability. **Why now:** the GENIUS Act (enacted 2025-07-18) bars *payment-stablecoin issuers* from paying interest/yield directly — pushing yield off the coin and into wrapper/savings tokens (sUSDS, scrvUSD, sGHO) and DeFi lending rails (per cryptobriefing/CRS, 2026). Second-order effect: this *entrenches* the savings-rate-via-wrapper model these DeFi protocols already use, while denying USDC/USDT a yield response — a structural tailwind for the decentralized tail's yield narrative even as it stays small in supply.

**Competitive landscape.** Sector KPIs: stablecoin **supply/market cap**, **savings-rate (APY)** as the policy lever, and lending-arm **TVL**. Basis of competition = distribution + yield, not the mint mechanism (which is commoditized). Lending-protocol TVL ranking (DefiLlama via eco.com, Apr 2026): **Aave V3 ~$19.4bn > Spark ~$6.8bn > Morpho Blue ~$4.9bn**. Recent moves: Spark closed May 2026 with ~$6.4bn Savings + ~$3.6bn SparkLend + ~$2.6bn Liquidity Layer ≈ $12.6bn combined (cryptobriefing, May 2026); Aave passed Aavenomics 3.0 / a landmark revenue-control vote (CoinDesk, 2026-04-13) and Grayscale issued a fair-value note (2026-06-17). **Positioning:** Sky/USDS is the scaled leader of the decentralized tail (DAI+USDS ~$8.6bn, Apr 2026); **crvUSD is niche** (~$250–293m mkt cap, Apr 2026 per CoinMarketCap/DefiLlama) — ~30x smaller than USDS and trailing even Aave's GHO (~$580–584m, Mar–May 2026). Moat: Sky = distribution + SSR-as-rate-lever (Osero/Spark integrations); Curve = LLAMMA soft-liquidation + DEX-liquidity flywheel, but no distribution scale (analysis).

**Comps & multiples.** No tradable equity for Curve/Sky; the only publicly-priced lending-protocol comp is **Aave**:
- **Aave** — mkt cap ~$1.47bn (16m AAVE × ~$95.48), FDV ~$1.52bn; protocol revenue ~$134–140m run-rate. **P/S (mkt-cap / revenue) = $1.47bn / ~$134m ≈ 11x** (CoinGecko/TokenTerminal, 2026). Grayscale fair value $80–100 on ~$60m projected 2026 net income at a 20–25x earnings multiple (2026-06-17). In-line-to-cheap for a DeFi token vs the ~15.8x category P/F median cited (TokenTerminal). Token P/S ≠ equity P/S — value accrues to token, not a company (TechTimes, 2026-06-27); treat as indicative only `[UNSOURCED]` for clean EV/EBITDA.
- **crvUSD / USDS:** no token-economic multiple is publicly verifiable for the stablecoins themselves (CRV/SKY governance tokens are separate); revenue/fee-take not cleanly disclosed → multiple = "no data". Compare on supply scale only: USDS ~$8.6bn vs crvUSD ~$0.25–0.29bn.
- Internal comps (corpus): [[Osero raises $13.5 million for stablecoin yield infrastructure]] (Sky-led SSR distribution), [[PayPal's PYUSD stablecoin reaches $1B market cap via Spark]], [[Revolut chooses Morpho for new DeFi yield product]], [[Aave and MetaMask bring DeFi to payments with Mastercard]]. Distribution not computed (<3 comparable equity multiples) → qualitative.

**Risk flags.**
1. **Yield is subsidized / rate-sensitive, not structural.** Savings rates (SSR ~3.75–4.5%, scrvUSD) lean on fee-switch redirection + token incentives and track external rates; a cut or incentive wind-down can reverse the inflows that justify the "money-market" framing — Sky's own stUSDS pool outflows on incentive changes are visible (Curve metrics, 2026). Why: the moat is a rate lever, and a lever can be pulled both ways.
2. **GENIUS-Act distribution ceiling.** USDS/crvUSD/USDe stay confined to DeFi rails because the yield must live in non-payment wrappers; off-chain/institutional scale flows to compliant USDC. Why: caps the addressable market for the decentralized tail to a ~$20bn category, not the $321bn whole.
3. **Disintermediation by the lending layer.** Margin in DeFi stablecoins migrates to whoever owns distribution + the lending venue (Aave $19.4bn, Spark, Morpho) — a CDP issuer with no integrations (crvUSD) risks being a price-taker on someone else's rails. Soft-liquidation's safety claim was already dented by the ~$700k LlamaLend bad debt (Oct 2025).

**What this changes (idea-lens).** Read as **maturation, not a launch** — DeFi stablecoins are consolidating into wrapper-yield money-markets, with the GENIUS yield-ban accidentally moating the model (analysis). Falsifiable thesis: the decentralized tail re-rates on *distribution wins* (neobank/wallet SSR embeds via Osero, Spark institutional lending), NOT on supply growth of the coin itself. Trigger to watch: whether crvUSD breaks out of its ~$0.25bn niche via integrations, or stays a DEX-liquidity utility while USDS/Sky compounds via distribution. What breaks the thesis: a GENIUS amendment or exchange-reward crackdown that closes the wrapper-yield workaround.

Sources: https://defillama.com/stablecoins · https://defillama.com/token/crvusd · https://coinmarketcap.com/currencies/crvusd/ · https://defillama.com/protocol/spark · https://cryptobriefing.com/spark-may-savings-sparklend-tvl/ · https://thedefiant.io/news/defi/aave-gho-stablecoin-market-cap-breaks-usd500-million · https://www.coingecko.com/en/coins/aave · https://tokenterminal.com/explorer/projects/aave/metrics/market-cap-fully-diluted · https://www.coindesk.com/tech/2026/04/13/aave-passes-landmark-vote-ending-months-long-fight-over-who-controls-protocol-revenue · https://cryptobriefing.com/genius-act-yield-stablecoin-rules/ · https://www.congress.gov/crs-product/IF13174 · https://www.techtimes.com/articles/319156/20260627/kraken-aave-stake-talks-expose-defi-pricing-paradox-revenue-flows-token-not-equity.htm
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
