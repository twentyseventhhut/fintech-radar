---
title: "Dinari integrates with Para for tokenized US equities access"
date: 2026-10-14
retrieved: 2026-10-16
tags:
  - company/dinari
  - company/para
  - industry/crypto
  - industry/trading
  - region/us
  - type/partnership
sources:
  - https://dinari.com/blog/dinari-and-para-expand-self-custody-wallet-access-to-tokenize-u-s-equities
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s67eb37cd
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Dinari integrates with Para for tokenized US equities access

> [!info] 2026-10-14 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Dinari integrates with Para to expand self custody wallet access to tokenized U.S. equities. Eligible users can buy dShares™ for over 700 U.S. stocks and ETFs with USDC. Purchases settle directly into Para embedded wallets.

## Первоисточники

### dinari.com
<https://dinari.com/blog/dinari-and-para-expand-self-custody-wallet-access-to-tokenize-u-s-equities>
*582 слов · direct*

Dinari and Para Expand Self-Custody Wallet Access to Tokenize U.S. Equities
Dinari
• 
Oct 14, 2026
Integration combines Dinari's tokenized equity infrastructure with Para's embedded wallets, enabling applications to offer access to 700+ U.S. stocks and ETFs through a streamlined user experience.
Dinari has integrated with Para, an embedded wallet infrastructure provider, to make it easier for fintech platforms and developers to offer tokenized U.S. equities directly within their applications.
The integration combines Dinari's infrastructure for the issuance, distribution and trading of tokenized equities with Para's wallet technology, enabling eligible users to purchase dShares™ using USDC.
For platforms, the integration provides a more efficient path to incorporating U.S. equities into existing products without building the underlying tokenization, wallet and transaction infrastructure independently.
Connecting Wallet Infrastructure With U.S. Equity Markets
As stablecoins become increasingly integrated into financial applications, platforms are looking to expand their functionality beyond payments and transfers to include access to investment products.
Historically, incorporating equities into a fintech application has required multiple integrations across brokerage services, custody, identity verification and transaction processing.
Through the Dinari and Para integration, developers can incorporate tokenized equity purchases into existing applications using a coordinated workflow that supports:
 Embedded wallet access: Users can create or access Para wallets through familiar authentication methods, including email and social login.
 Identity verification: Dinari's hosted verification process supports applicable onboarding and eligibility requirements.
 USDC-based purchases: Eligible users can purchase supported tokenized U.S. equities using USDC.
 Direct wallet settlement: Purchased dShares™ are delivered directly to users' Para wallets.
 Gasless transactions: Supported transaction flows can remove the need for users to separately acquire native blockchain tokens to pay network fees.
The result is a more streamlined experience for users and a simplified integration process for platforms seeking to expand access to financial markets.
Preserving Investor Rights Through Tokenization
At the foundation of the integration is Dinari's dShares™ model, which uses a custodial structure in which each token is backed 1:1 by the corresponding underlying U.S. stock or ETF held with licensed custodians.
Unlike synthetic products that provide price exposure without an interest in the underlying security, dShares™ are designed to preserve applicable economic and shareholder rights, including dividends, corporate actions and voting where available.
This approach reflects Dinari's broader mission to modernize financial market infrastructure while maintaining the rights and protections associated with traditional securities.
By integrating with Para, Dinari extends this infrastructure to applications that want to incorporate tokenized equities into their existing wallet experiences.
Expanding Distribution Through Embedded Wallets
Para provides embedded wallet infrastructure to hundreds of teams across fintech, payments and digital assets, supporting more than 15 million wallets.
The integration creates an additional distribution pathway for Dinari's tokenized equities, allowing applications built with Para to incorporate dShares™ without requiring users to leave their existing product experience.
Dinari supports tokenized U.S. equities across multiple blockchain networks, including Ethereum, Arbitrum, Base and Avalanche C-Chain, providing flexibility for platforms building across different ecosystems.
Together, Dinari and Para are making it easier for financial applications to connect stablecoin-based payments, digital wallets and traditional investment products through integrated infrastructure.
Getting Started
Developers building with Para can explore the Dinari integration through Para's technical walkthrough, which covers wallet authentication, identity verification, order submission and token delivery.
 Explore the Para and Dinari integration 
Developers can also access Dinari's Partner Portal to request sandbox credentials and begin integrating tokenized equities into their applications.
© 2026 Dinari, Inc.
Follow us on:
 
 
 
 
 
 Blog 
 Partner Login 
 Privacy Policy 
 Terms & Conditions 
 Documentation 
 Contact us 
Looking to trade dShares™?

## Контекст

<!-- enrichment:context -->
### [0] What happened (one-line)
On 2026-10-14 Dinari — an SEC-registered transfer agent / broker-dealer issuer of dShares™ tokenized US equities — integrated with **Para** (embedded-wallet infrastructure, ex-Capsule) so any Para-built app can let eligible users buy 700+ tokenized US stocks/ETFs with USDC, settling dShares directly into the user's Para wallet with gasless transactions.

### [1] Mechanics of the integration
- **Stack combined:** Dinari supplies issuance / distribution / trading of tokenized equities + hosted KYC/identity verification; Para supplies the embedded self-custodial wallet (email/social login auth) and 15M+ existing wallets as distribution.
- **Flow:** Para wallet create/access → Dinari hosted identity & eligibility check → USDC purchase of supported dShares → **direct wallet settlement** of dShares into the Para wallet → **gasless** (no need for the user to hold native gas tokens).
- **Value prop:** platforms avoid separately wiring brokerage, custody, identity and transaction processing — Dinari+Para is a one-integration path to put US equities inside an existing wallet/payments product.
- **Chains:** Ethereum, Arbitrum, Base, Avalanche C-Chain (external sources add Sei/Solana "soon").
- This is an **infrastructure/distribution deal**, not a new regulatory or product category. Para joins Dinari's roster of distribution partners (cf. Bitcoin.com, Circle integrations reported mid-2026 externally).

### [2] The dShares™ model & regulatory wrapper (why it's differentiated)
- Each dShare is **backed 1:1** by the underlying US stock/ETF held with licensed custodians (external: Alpaca Securities LLC, FINRA/SIPC, provides brokerage/custody). Not synthetic price exposure.
- Designed to **preserve shareholder economics** — dividends, corporate actions, voting where available.
- **Regulatory posture (external):** Dinari Inc. is an SEC-registered transfer agent (Sec. 17A(c)); Dinari Securities LLC is a FINRA/SIPC broker-dealer subsidiary. This lets Dinari serve **US investors directly** (Reg A+ for a retail subset; Reg D 506(c) for accredited) — the near-unique US-onshore angle vs peers who gate US retail out under Reg S. Contrast with [[SEC clarifies regulatory framework for tokenized securities]] (Jan 2026): tokenized securities remain securities, carrying registration/disclosure duties — Dinari's licensing is precisely the answer to that posture.

### [3] Internal context — how this fits the tokenized-equity wave (cite prior notes)
- **Model comparison:** dShares (1:1 custodial, rights-preserving) resemble Backed's **xStocks** [[xStocks tokenized equities now supported via Talos]] (1:1 backed, rebasing for corporate actions, open/permissionless) and **Ondo** tokenized US stocks [[Blockchain.com and Ondo launch tokenised US stocks in Europe]] (200+ names via a wallet). Difference: xStocks/Ondo target non-US; Dinari targets eligible US investors.
- **Native vs wrapped:** [[Figure debuts tokenized stock with upsized $150M offering]] = natively-issued onchain stock (FGRD on OPEN), a different architecture from Dinari's custodial wrapper over off-chain shares.
- **Venue/rails momentum this year:** [[SEC approves Nasdaq tokenized securities trading]], [[Nasdaq partners with Kraken for tokenized stock trading]], [[Coinbase and Bybit explore US tokenized stock collaboration]], [[Coinbase launches 24 7 US stock trading with Yahoo Finance]] — the sector is racing to bolt equities onto crypto rails; Dinari+Para attacks the *wallet/embedding* layer rather than the exchange layer.
- **Distribution-via-wallet pattern:** mirrors Ondo-in-Blockchain.com-wallet; Dinari-in-Para is the same "equities inside the wallet users already have" play, now aimed at builders broadly.

### [4] External context — Para & market size
- **Para** = embedded MPC/self-custodial wallet + auth SDK (Capsule Labs, rebranded Capsule→Para Feb 2025); ~100+ dev teams, 15M+ users/wallets; key split across device (passkey/secure enclave) + Para infra; broad EVM + Cosmos/Stellar/institutional chains.
- **Market size (external, 2026):** tokenized equities ~$2.9B onchain by Sep 2026, tripled share YTD. **Ondo (~$837M), Binance bStocks (~$685M), xStocks (~$344M)** lead (~77% combined). Dinari is the US-onshore specialist, not a volume leader — so this deal is about *builder distribution*, a plausible path to close the gap.

**Sources:**
- https://dinari.com/blog/dinari-and-para-expand-self-custody-wallet-access-to-tokenize-u-s-equities
- https://www.getpara.com/ · https://blog.getpara.com/how-embedded-wallets-work/
- https://eco.com/support/en/articles/15254023-tokenized-equities-2026-backed-dinari-robinhood
- https://www.theblock.co/news/defi/2026-08-17-tokenized-equities-triple-market-share-ondo-binance-xstocks-dominate-411996
- https://www.tokenpost.com/news/investing/29088
- https://cryptobriefing.com/dinari-circle-tokenized-stocks-us-investors/ · https://cryptobriefing.com/dinari-tzero-tokenized-stock-framework/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
1. **Is this a real product launch or a dev-preview?** The blog describes a "technical walkthrough" + sandbox credentials via Partner Portal — i.e. an SDK integration available to *builders*, not a live consumer feature with named apps shipping it yet. How many Para apps have actually enabled dShares?
2. **Who is "eligible"?** All US-investor claims hinge on Dinari's KYC gate (Reg A+ retail subset vs Reg D 506(c) accredited). The note's "over 700 stocks" figure may not all be available to a given user class. What's the retail-accessible subset?
3. **Self-custody vs custodial reality.** Dinari holds the *underlying* shares with licensed custodians; the "self-custody" is only of the token. Does the holder actually have an enforceable claim on the underlying in a Dinari insolvency, or just a contractual IOU?
4. **"Gasless" subsidized by whom?** Gasless flows need a paymaster — is Dinari/Para/the app footing gas, and is that sustainable at scale?
5. **Dividend/voting mechanics unverified.** "Rights preserved where available" is hedged. How are dividends actually distributed to on-chain holders, and is voting ever practically exercisable?
6. **Para's 15M "wallets/users" number** conflates attendees-provisioned (e.g. Devconnect 10k) with active users. How many are economically active and would plausibly buy equities?
7. **Revenue/economics undisclosed.** No fee split, no spread/markup, no volume commitment disclosed. Is this a press-release partnership with little near-term P&L?
8. **Regulatory fragility.** [[SEC clarifies regulatory framework for tokenized securities]] keeps these as securities; a shift in SEC posture or a Reg A+ qualification lapse could restrict the US-retail angle that is Dinari's whole differentiator.
9. **Liquidity/redemption at NBBO** — external sources claim redemption at NBBO, but who market-makes dShares and what are spreads/slippage in thin names outside mega-caps?
10. **Competitive moat.** Ondo/Binance/xStocks dominate volume (~77%); Backed also distributes via wallets. What stops a Para app from integrating Ondo instead? Is Dinari's US-license the only durable edge?
11. **Source is first-party.** Only source is Dinari's own blog; no independent coverage, adoption metrics, or Para co-statement in the note. Single-source risk.
12. **Settlement/custody counterparty (Alpaca).** Underlying custody reportedly via Alpaca — concentration/counterparty risk not disclosed in the note.
13. **Cross-chain fragmentation.** dShares across Ethereum/Arbitrum/Base/Avalanche — does liquidity fragment per chain, hurting pricing?
14. **"700+ stocks" overlap with S&P 500 claim** (external says 724 incl. full S&P 500) — is the number in the DB note stale/understated or is availability conditional?

**Importance: 3/5** — Credible, well-structured infrastructure deal from a genuinely differentiated US-onshore issuer, plugging into a large wallet network at the fast-growing tokenized-equity layer; strategically sensible distribution play. But it is a builder-facing SDK integration (no named live apps, no disclosed economics, single first-party source), and Dinari is a small player vs Ondo/Binance/xStocks who hold ~77% of a still-small (~$2.9B) market. Infrastructure enabler, not a market-moving event — mid importance.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Tokenized equities are the fastest-growing slice of on-chain RWAs: total tokenized-stock value reached ~$3.8bn in Oct 2026, up ~483% YTD (per cryptotimes/CoinGecko-cited data, as of 2026-10-16), a sub-segment of the broader ~$38–60bn RWA market (excl. stablecoins) (per BeInCrypto/rwa.xyz, mid-2026). Structure is fast-consolidating around a handful of issuers while distribution fragments across wallets/exchanges/chains — value is splitting between the issuance/custody layer (Dinari, Backed, Ondo) and the distribution layer (wallets, CEXs). Entry barriers are regulatory (broker-dealer/transfer-agent status, custody, KYC) more than technical. Why now: the 2026 US regulatory thaw (SEC moves on tokenized securities) plus stablecoin ubiquity let apps bolt equities onto existing USDC rails — exactly the gap Dinari+Para target. The news is an *infra integration* (announced developer path), not demonstrated end-user adoption — de-PR: no volume or wallet-activation numbers disclosed.

**Competitive landscape.** Sector KPIs: tokenized AUM / market cap of issued assets, on-chain holders, trading volume, chain/venue coverage. Four-way issuer race as of Oct 2026: **Ondo** (Global Markets) ~$0.99bn, the largest (~26% share, down from ~56% earlier in 2026 as rivals scaled); **Backed/xStocks** ~$0.97bn (~25%, non-US retail, Liechtenstein FMA prospectus, ~$25bn cumulative volume since Jun-2025, 80k+ holders); **Binance bStocks** ~$0.92bn; **Robinhood** (EU-listed tokens). Basis of competition: regulatory access (who can legally serve US vs EU vs RoW), distribution reach, chain breadth, and investor-rights fidelity. Dinari's position: **niche but differentiated** — it is a Delaware transfer agent + SEC-registered broker-dealer, one of the only issuers legally serving *eligible US investors*, and sells rights-preserving (dividends/voting) 1:1-backed dShares vs synthetic exposure. But it is tiny: ~$42.6m issued market cap (late-Aug 2026, per CoinDesk/cryptonomist) vs Ondo's ~$1bn — well under ~5% of the segment. Moat `(analysis)`: regulatory licensing + rights-preservation, not scale. Recent peer moves: Ondo TVL ATH $1.26bn (Oct 2026); xStocks via Talos (Mar 2026) and Kraken IPO access (Jun 2026); Dinari's own Circle/USDC US launch of 724 tickers incl. full S&P 500 (2026-08-04). The Para deal extends distribution to 15m+ embedded wallets — a channel play, not a product leap.

**Comps & multiples.** Private, pre-revenue-disclosure names → EV/Revenue, P/E = **no data**. Round valuations only: **Dinari** — $12.7m Series A (May 2025, Hack VC/Blockchange, VanEck Ventures, F-Prime, Avalanche Fund), total raised ~$22.65m; current valuation `[UNSOURCED]`. **Para** (ex-Capsule) — a16z-led seed (2023); later valuation `[UNSOURCED]`. A cleaner read-across is AUM, not multiples: Dinari ~$42.6m vs Ondo ~$0.99bn ≈ **~0.04x** of the leader's book — i.e. a long-tail issuer. Internal comps (base): [[Blockchain.com and Ondo launch tokenised US stocks in Europe]], [[xStocks tokenized equities now supported via Talos]], [[Ondo Finance launches 24 7 minting for tokenized US stocks]], [[Securitize launches onchain trading of US stocks on Solana]], [[Bybit opens US stocks trading to global users]], [[BingX launches U.S. stock trading via Alpaca]]. Distribution not computed on multiples (no public revenue); qualitative comparison only. No valuation outlier flag possible — insufficient public figures.

**Risk flags.**
1. **Scale/disintermediation.** At ~$42.6m vs an ~$3.8bn segment, Dinari is sub-scale; its edge is the *infra/compliance* layer, but distributors (Para, exchanges) own the user and could multi-source issuers or vertically integrate — margin risk if Dinari becomes a swappable backend.
2. **Regulatory concentration/single-jurisdiction dependence.** The whole US-investor thesis rests on the 2026 SEC thaw and Dinari's broker-dealer/transfer-agent status; any walk-back of tokenized-securities permissiveness or a licensing issue would hit the one axis where Dinari leads peers.
3. **Announced vs live.** This is a developer integration with gasless USDC flows but zero disclosed activation/volume — adoption via Para's 15m wallets is a claim, not demonstrated traction; the economics (fees, who bears fraud/settlement risk) are undisclosed.

**What this changes (idea-lens).** `(analysis)` The competitive front line is shifting from *issuing* tokenized stocks to *distributing* them inside existing fintech/wallet UX — Dinari is betting it can be the regulated US-equity backend for embedded-wallet apps the way Circle is for stablecoins. Falsifiable thesis: if the Para integration materially lifts Dinari's issued AUM off its ~$42.6m base over the next 1–2 quarters, the "infra-for-apps" model works; if AUM stays flat while Ondo/Backed keep scaling, Dinari stays a licensed niche and the real value accrues to distributors. Trigger to watch: next rwa.xyz/dune AUM + holder prints for dShares post-integration.

Sources: https://www.cryptotimes.io/2026/10/16/tokenized-stocks-reach-3-8b-as-dex-trading-volume-rises-55x/ · https://www.theblock.co/news/defi/2026-08-17-tokenized-equities-triple-market-share-ondo-binance-xstocks-dominate-411996 · https://www.panewslab.com/en/articles/019d2e3f-5893-774f-acb6-5b806c3890e0 · https://www.coindesk.com/business/2026/08/04/dinari-brings-tokenized-u-s-stocks-to-american-investors-as-equity-race-heats-up · https://en.cryptonomist.ch/2026/08/05/tokenized-stock-trading-dinari-usdc/ · https://www.coindesk.com/tech/2025/05/01/dinari-raises-usd12-7m-to-expand-tokenized-stock-access-for-non-u-s-investors · https://blockeden.xyz/blog/2025/10/30/xstocks/ · https://solanacompass.com/projects/para
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
