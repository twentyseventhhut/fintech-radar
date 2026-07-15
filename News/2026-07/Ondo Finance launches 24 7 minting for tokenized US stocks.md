---
title: "Ondo Finance launches 24/7 minting for tokenized US stocks"
date: 2026-07-14
retrieved: 2026-07-14
tags:
  - company/ondo-finance
  - industry/defi
  - industry/capital-markets
  - region/us
  - type/product
sources:
  - https://substack.com/redirect/8491fc7e-2c76-461e-96e0-ac55b1c60086
status: published
n_mentions: 1
channels:
  - "lex"
story_id: sa3ea9ec7
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Ondo Finance launches 24/7 minting for tokenized US stocks

> [!info] 2026-07-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: lex

## Агрегированный текст (из дайджестов)

[lex] Ondo Finance Launches 24/7 Minting and Redemption for Tokenized US Stocks and ETFs - Converge

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/8491fc7e-2c76-461e-96e0-ac55b1c60086>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ondo Finance launches 24/7 minting for tokenized US stocks
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
Ondo Finance turned on **round-the-clock primary minting AND redemption** for its tokenized US stocks/ETFs on Ondo Global Markets. This is a **feature upgrade, not a launch**. The product itself launched Sep 2025 (see [[Ondo launches 100+ tokenized US stocks across chains]]), and — per that very note — mint/redeem then ran "24 hours a day, **five days weekly**." The delta here is the missing two days: minting/redeeming against the underlying at prevailing prices now works nights, **weekends and US holidays**, i.e. 24/5 → 24/7 on the *primary* side. Secondary transfers were already 24/7 from day one.

De-PR'd specifics (external, dated):
- Rollout is **chain-staggered**: Ethereum + BNB Chain ~**25 Jun 2026**; Solana ~**8–9 Jul 2026** (this lex item, 14 Jul, is the Solana/latest wave). Any single-date framing is oversimplified.
- **Live but partial**: 24/7 mint/redeem went live on ~**6 high-volume tickers first** (SPYon, QQQon, CRCLon, NVDAon, TSLAon, GOOGLon), "more in coming weeks" — NOT the full 430+ catalog yet. Treat "24/7 for tokenized stocks" as true-but-scoped.
- Zero mint/redeem fees, ~$1 minimum. Powered by Ondo's "Nexus" system; pitch is that pricing draws on deep public-market liquidity rather than thin on-chain pools.

**Why structured this way / what it reveals:** the hard part of "24/7" is not trading (already continuous) but **primary create/redeem when the underlying US cash market is closed**. To mint/redeem at a "prevailing price" on a Saturday, Ondo must internalise a quote and carry basis/hedging risk over the weekend gap. Launching on only 6 mega-cap/most-liquid names first is the tell: those are where Ondo can hedge cheaply and where weekend-gap risk is most manageable. So the real story isn't "more hours" — it's **Ondo taking principal/market-maker risk to remove the last friction of the tokenized wrapper**, betting the always-on UX (vs 24/5 rivals on the primary side) is worth the balance-sheet risk.

## [1] Competitors / peers
- **xStocks (Backed Finance + Kraken, Solana)** — LIVE 22 May 2025, ~60 tickers, 1:1 backed via Swiss prime-broker custody, non-US, 24/7 *secondary* trading on Kraken/Bybit. ~$3.5B cumulative on-chain volume, ~80k holders by 2026. Ondo's most direct comp; **predates Ondo Global Markets by ~4 months**.
- **Robinhood (EU-only)** — tokenized stocks Jun 2025 under a Lithuanian license; 200+ → 2,000+ tokens, €1 min, 24/5, own Arbitrum-Orbit chain live ~2 Jul 2026. Broader catalog, retail distribution, but EU-only.
- **Binance bStocks** (BNB Chain, Jun 2026), **Dinari/dShares** (US TA + broker-dealer), **Backed**, **Securitize**, **Coinbase** (1:1 tokenized stocks announced, pending SEC).

Position: on 24/7 *secondary* trading Ondo is **behind/parity** (xStocks and Robinhood got there in 2025). Ondo's specific "first for the sector" claim is narrowly about **24/7 primary mint+redeem at public-market prices** — plausibly true but a marketing frame, not independently verified. **Why the map looks this way:** rivals optimised distribution first (Kraken CEX, Robinhood app), leaving the wrapper's redemption plumbing as differentiator. Ondo, coming from tokenized Treasuries where 24/7 mint/redeem is table stakes (OUSG), is porting that muscle to equities — competing on **infrastructure depth** rather than reach. Second-order: if primary 24/7 becomes standard, this edge commoditizes within quarters and the fight reverts to distribution/liquidity, where xStocks/Robinhood lead.

## [2] Company history / fit
Ondo's core is **tokenized US Treasuries** — OUSG (~$692M) and USDY (~$740M); total protocol TVL ~$3.78B (May 2026). It pivoted into equities with **Ondo Global Markets (Sep 2025)**, then scaled aggressively: 100+ → 200+ → 430+ instruments; TVL >$1B; TVL $556M / $8.7B volume already by Feb 2026 ([[Blockchain.com and Ondo launch tokenised US stocks in Europe]]). Distribution expanded via wallets and regional partners — [[Roqqu partners with Ondo Finance to offer tokenized US stocks in Nigeria]] (Africa), Blockchain.com (EEA), MetaMask. It bought SEC broker Oasis Pro (2025, for the transfer-agent rails) and, days before this item, launched **US custodial tokenized securities** with Broadridge/Oasis Pro TA ([[Ondo Finance launches custodial tokenized securities with Broadridge]], 3 Jul 2026) — a separate, US-facing regulatory model, NOT the same product as this Reg-S offshore 24/7 item.

**Why Ondo acts this way:** tokenized Treasuries are a crowded, thin-margin business (yield is the commodity, take-rate compresses). Equities give a larger TAM and a chance to own the **on-chain-equity rails** end-to-end (issuance via Oasis Pro TA, governance via Broadridge, always-on mint/redeem). 24/7 minting is one more brick in "become the default equity-tokenization stack," consistent with the Sep-2025 → Jul-2026 cadence of shipping the missing pieces.

## [3] Novelty / value-add / traction
Genuinely new vs Ondo's own prior state: **primary mint/redeem extended from 24/5 to 24/7** (the Sep-2025 note's own words were "five days weekly"). That is a real, citable delta — this is **fresh**, not a reprint. But the novelty is narrow and partial (6 tickers, chain-staggered).

**Why the value-add is real / where it breaks (deeper):** the economic value of always-on redemption is capturing the **weekend/holiday arbitrage and convenience premium** — users can exit or enter when TradFi is shut. Ondo captures margin via **spread/float**, not the advertised "zero fees" — so "free" is a headline, not the economics. What underpins it: Ondo's willingness/capacity to warehouse basis risk over closed-market gaps. What breaks it: (a) a stress redemption wave on a weekend when the cash market is shut and shares can't be sourced — untested publicly; (b) commoditization once xStocks/Dinari match 24/7 primary; (c) the structure — Global Markets holders own a **BVI-SPV structured note (debt claim)**, not the share, secured 1:1 via Ankura Trust under Reg S. If a rival offers cleaner legal title, Ondo's UX edge doesn't offset the wrapper risk. Traction to watch is redemption volume during closed hours, not the announcement.

## [4] What's next / market sentiment
Ondo says it will extend 24/7 mint/redeem beyond the initial 6 tickers "in coming weeks," and an exec projects tokenized-stock TVL to **$3B by end-2026** (from >$1B). The parallel US custodial track (IVV, Micron via Broadridge/Oasis Pro) rides the SEC's **Jan 2026 staff statement** on third-party custodial tokenization — guidance, not a rule, and **not yet live to US retail**. Sentiment on tokenized equities is hot (xStocks, Robinhood, Binance, Coinbase all in).

**Why the market goes this way / second-order:** tokenized equities are converging on 24/7 as the baseline expectation, so the differentiator migrates from "who's continuous" to **who bears redemption/liquidity risk best and who has distribution**. Counterintuitive risk: aggressive 24/7 minting concentrates **weekend-gap and hedging risk on the issuer's balance sheet** — the feature that looks like pure convenience is actually Ondo absorbing tail risk to buy share. If a weekend dislocation hits during closed US markets, the "always-on" promise is exactly where it could crack. Regulatory overhang (Reg-S offshore structures; unfinished US retail regime) remains the ceiling.

## Sources
- lex (this item): "Ondo Finance Launches 24/7 Minting and Redemption for Tokenized US Stocks and ETFs - Converge"
- CryptoTimes (Solana 24/7, 2026-07-09); CryptoBriefing (Eth/BNB, 2026-06-25); TheStreet (analysis)
- Ondo docs: Global Markets legal/regulatory (BVI SPV, Ankura, Reg S)
- Yahoo Finance ($1B TVL); Sep-2025 launch coverage (100+ equities, 24/5 mint/redeem)
- Internal: [[Ondo launches 100+ tokenized US stocks across chains]], [[Blockchain.com and Ondo launch tokenised US stocks in Europe]], [[Ondo Finance launches custodial tokenized securities with Broadridge]], [[Roqqu partners with Ondo Finance to offer tokenized US stocks in Nigeria]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Launch or feature update?** Feature update. Ondo Global Markets launched Sep 2025; this is 24/5 → 24/7 *primary* mint/redeem.
2. **Fresh or duplicate of the Sep-2025 note?** FRESH. The Sep-2025 note explicitly says mint/redeem was "24 hours a day, five days weekly." Adding weekends/holidays is a genuine new delta, not a reprint.
3. **Live or announced?** Live but PARTIAL — ~6 tickers first (SPYon, QQQon, CRCLon, NVDAon, TSLAon, GOOGLon); full 430+ catalog "coming weeks."
4. **What is the exact date?** Chain-staggered: ~25 Jun 2026 (Ethereum/BNB), ~8–9 Jul 2026 (Solana). The 14 Jul lex item is the Solana/latest wave.
5. **Was continuous trading already possible?** Yes — 24/7 *secondary* transfers existed from launch. Only *primary* mint/redeem was market-hours-limited. Headlines blur this.
6. **Is "first for the sector" true?** Open/marketing. Plausibly first at 24/7 primary mint+redeem at public prices; xStocks (May 2025) and Robinhood (Jun 2025) beat it to 24/7 secondary. Not independently verified.
7. **Do holders own the actual stock?** No (Global Markets) — a BVI-SPV structured note (debt claim), backed 1:1 with security interest via Ankura Trust, under Reg S. Not direct share title.
8. **Can US investors use it?** No. Global Markets is Reg S / non-US. The separate US custodial product (IVV, Micron; [[Ondo Finance launches custodial tokenized securities with Broadridge]]) is not yet live to US retail.
9. **How is "prevailing price" set on a weekend when US markets are shut?** Open — the key unexplained risk. Ondo likely internalises a quote and carries basis/hedging risk. Mechanism not disclosed.
10. **Does 24/7 minting create redemption/liquidity risk?** Open — a weekend redemption wave means sourcing shares from a closed market. Buffer + public-market liquidity is the claimed mitigant; stress behavior untested.
11. **Are the fees really zero?** 0% mint/redeem reported, but Ondo earns on spread/float. "Zero fee" is a headline, not the full economics.
12. **How many instruments — 200, 260 or 430?** Grew over 2026; 430+ latest. Discrepancies are timeline, not contradiction. 24/7 applies to only ~6 so far.
13. **Is TVL ($1B+/$3.78B total) verifiable?** Issuer/press figures, not independently audited here. Ankura verifies the underlying daily per Ondo's own disclosures.
14. **vs xStocks specifically?** xStocks predates Ondo Global Markets ~4 months; similar 1:1 non-US model (Swiss custody vs BVI-SPV/US custody). Ondo edge = deeper primary liquidity; xStocks edge = Kraken/Bybit CEX distribution + head start.
15. **Regulatory risk?** Open — US retail tokenized-equity regime not finalized (rides Jan 2026 SEC staff statement, guidance not rule); Reg-S offshore structures face ongoing scrutiny.

**Importance: 3/5** — Genuinely fresh (real 24/5→24/7 primary-mint delta, verified against Ondo's own Sep-2025 note), on a fast-scaling ($1B+ TVL) product from a category leader, so not trivial. But it's a narrow, partial feature upgrade (6 tickers, chain-staggered, non-US Reg-S only), the marketing "first" claim is unverified, and always-on secondary trading already existed via rivals since 2025. Solid incremental capital-markets item, not a category-defining event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-15]] (2026-07-15).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Tokenized equities is the fastest-growing RWA sub-vertical: aggregate market cap crossed ~$1bn with 185,000+ holders by March 2026, up from ~$20m and <1,500 users in Dec 2024 — a ~2,800% YoY jump (per CoinDesk, Jan 2026). It sits inside a broader tokenized-RWA base of ~$22bn AUM by May 2026 (Treasuries $10bn, private credit $8bn; per rwa.xyz), where tokenized stocks are still only ~4.4% of on-chain RWA value — early, not yet mainstream. **Why now:** on 18 May 2026 the SEC was reported to be readying an "innovation exemption" — a 12–36-month sandbox letting third parties tokenize stocks (AAPL, TSLA) without issuer sign-off, with volume caps (per Bloomberg via Cointelegraph). That regulatory thaw plus 24/7 crypto-market expectations is the "why now": TradFi equities settle T+1 and trade ~6.5h/day; the pitch is always-on liquidity and atomic settlement. Structure: fragmented and land-grab — multiple issuers (Backed/xStocks, Ondo, Gemini, Robinhood EU, Dinari) mint the *same* underlying tickers across chains, so the sector is racing for holders/distribution, not consolidated.

**Competitive landscape.** Sector KPIs: cumulative transaction volume, on-chain AUM/TVL, unique holders, chains/venues covered. Basis of competition = distribution (wallet/exchange integrations) + breadth of tickers + settlement UX, not price. Key players & recent moves:
- **Backed Finance / xStocks** (now Kraken-owned) — the leader: >$25bn cumulative volume in <8 months since Jun-2025 launch, ~$225m AUM, 80,000+ holders; held 8 of top-11 tokenized equities by holders (mid-Feb 2026) (per Kraken blog).
- **Ondo (Ondo Global Markets, rebranding to "Ondo Stocks")** — >$500m TVL and >$9bn cumulative volume by Feb 2026 (Ondo's own claim of "largest platform"); TVL doubled since Jan and cumulative volume >$18bn by May 2026; 200–260+ tokenized US stocks/ETFs across Solana, Ethereum, BNB Chain, bridgeable to HyperEVM (per Solana.com, MetaMask, Yahoo Finance).
- Others: Gemini (14 EU listings), Robinhood (EU tokens, under EU scrutiny), Dinari, Bybit/Kraken via Backed.
**This news specifically:** extends minting/redemption to **24/7** — prior state was mint/redeem 24h × *5 days/week* with only P2P transfers round-the-clock. So the incremental change is closing the weekend/off-hours primary-market gap, not launching a new product. **Protagonist position:** clear #2 by disclosed volume/AUM, catching up to xStocks; multi-chain breadth + the Oasis Pro broker-dealer and Broadridge custody rails (see comps) are its differentiators. Moat = distribution + regulatory rails (analysis); thin vs xStocks' holder lead.

**Comps & multiples.** No public equity multiples — Ondo Global Markets is a protocol, not a filer; ONDO token FDV would not be a clean equity comp, so **valuation multiples = no data / [UNSOURCED]**. Operating comps (volume/AUM) above. Internal base comps (tokenized-equity precedent):
- [[Ondo launches 100+ tokenized US stocks across chains]] — the original OGM launch.
- [[Ondo Finance launches custodial tokenized securities with Broadridge]] — custody rail, same month.
- [[Blockchain.com and Ondo launch tokenised US stocks in Europe]] · [[Roqqu partners with Ondo Finance to offer tokenized US stocks in Nigeria]] — distribution.
- [[Backed Finance's xStocks pass $2 billion in trading volume]] · [[Kraken acquires Backed Finance for tokenization]] — the leader.
- [[Coinbase seeks SEC approval for tokenized equities]] · [[Kraken seeks SEC blessing for 24 7 tokenized stock trading platform]] — regulatory race.
Sanity check: xStocks $225m AUM on $25bn cumulative volume implies AUM turns over ~100x+ — i.e. volume is overwhelmingly secondary/CEX churn, not sticky holdings. Ondo's $18bn cumulative on ~$500m+ TVL shows the same volume-to-AUM gap; treat "cumulative volume" as a marketing metric, not stock of assets (in-line with peer, not an outlier).

**Risk flags.**
1. **Volume ≠ adoption / thin AUM.** Cumulative-volume headlines (Ondo $18bn, xStocks $25bn) dwarf actual AUM (~$0.5bn / ~$0.23bn) — most flow is short-hold trading. 24/7 minting adds convenience but doesn't create end-holders; risk that TVL plateaus while announcements accelerate.
2. **Liquidity fragmentation.** Same tickers minted by multiple issuers across chains disperse order flow that would concentrate on NYSE/Nasdaq → price discrepancies and slippage on size (per Cointelegraph research). 24/7 primary minting deepens the primary/secondary basis-risk when the underlying US market is closed — weekend mints price against a stale last-trade.
3. **Regulatory dependence.** The whole US expansion hinges on the SEC's unconfirmed "innovation exemption" (volume caps, 12–36-month sandbox). If the exemption narrows or lapses, US distribution and issuer-consent questions reopen — dependence on a policy that is not yet law.

**What this changes (idea-lens).** Incremental, not re-rating: 24/7 minting is table-stakes catch-up toward always-on parity with crypto rails, narrowing Ondo's UX gap to xStocks but not its holder gap (analysis). Watch the holder-count and AUM split (not cumulative volume) and whether the SEC exemption is formalized — that, plus which wallets/exchanges Ondo signs, is the real catalyst. Falsifiable thesis: if Ondo's on-chain AUM/holders don't close on xStocks within 2–3 quarters despite 24/7 minting, distribution — not settlement hours — is the binding constraint.

Sources: https://www.coindesk.com/business/2026/01/30/the-market-for-tokenized-equities-has-exploded-by-almost-3-000-in-a-single-year · https://blog.kraken.com/product/xstocks/25-billion-in-total-transaction-volume · https://solana.com/news/ondo-global-markets-tokenized-stocks-etfs-solana · https://finance.yahoo.com/markets/crypto/articles/ondo-global-markets-tops-1b-103215556.html · https://metamask.io/news/metamask-adds-tokenized-us-stocks-etfs-and-commodities-via-ondo-global · https://cointelegraph.com/news/tokenized-stocks-risk-liquidity-and-revenue-fragmentation-research · https://eco.com/support/en/articles/15254020-tokenized-rwa-market-size-2026-20b-aum-growth-trajectory
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
