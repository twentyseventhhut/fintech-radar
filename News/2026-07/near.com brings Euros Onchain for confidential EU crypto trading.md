---
title: "near.com brings Euros Onchain for confidential EU crypto trading"
date: 2026-07-02
retrieved: 2026-07-02
tags:
  - company/near
  - industry/crypto
  - region/europe
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/3b4b60da
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s6370ab1e
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# near.com brings Euros Onchain for confidential EU crypto trading

> [!info] 2026-07-02 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇪🇺 near.com brings Euros Onchain, enabling EU users to trade across crypto markets confidentially using their own wallets. Users can deposit euros into a crypto wallet via SEPA Instant, the EU's real-time payment rail, and receive EURe stablecoins against those euros.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/3b4b60da>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: near.com brings Euros Onchain for confidential EU crypto trading
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **2026-07-01**, near.com (the NEAR Protocol consumer app) added a **euro on-ramp**: EU users deposit euros via **SEPA Instant** and receive **EURe** — the MiCA-regulated euro e-money token issued by **Monerium** (the PR itself does not name Monerium; EURe = Monerium's EMT is established from external sources). From EURe they can trade across **30+ chains, 180+ assets, RWAs and perps**, self-custodied, with **NEAR Intents** routing liquidity. The privacy angle — **Confidential Mode / Confidential Intents**, executed in a **NEAR private shard** run by permissioned validators in TEEs — hides trade details (amounts, routes, pairs).
- **De-PR'd delta:** the confidential-execution machinery is **not new** — Confidential Intents went live **2026-02-25** (see [4]). What launched 2026-07-01 is narrowly the **EUR fiat rail (SEPA Instant → EURe mint)** bolted onto that existing stack. So the headline "brings Euros Onchain … confidentially" bundles a genuinely-new fiat on-ramp with a four-month-old privacy feature. → Why framed this way: NEAR is timing the announcement to the **MiCA transition-period close (2026-07-01)**, dressing an on-ramp integration as a regulatory-moment product.
- **What's actually thin:** near.com issues nothing and custodies nothing on the euro side — it **resells Monerium's EURe + SEPA rails**. No disclosed fees, spreads, volume caps, or launch traction numbers. "Confidential" ≠ anonymous: EURe mint/burn runs through a regulated EMI (KYC at the fiat edge); privacy is on-chain trade obfuscation, not AML-free trading.

## [1] Competitors / peers
- **Euro-stablecoin issuers** (whom near.com depends on, not competes with): **EURC/Circle** — ~$427M cap, ~41–50% of the ~€450M euro-stablecoin market (Jan 2026, up from €50M two years prior); **EURe/Monerium** — >€6B 2025 volume, native IBAN; **EURI/Banking Circle** — only bank-issued; **EUROe/Membrane**; **Qivalis** — 9-bank consortium, Dutch EMI, H2-2026 target. Corpus peers: [[ODDO BHF launches euro-backed stablecoin EUROD]], [[Deutsche Börse and Circle collaborate on stablecoins in Europe]], [[Bancomat announces EUR-BANK euro stablecoin in Italy]], [[Alipay bets on EU stablecoin via Luxembourg license]], [[Societe Generale launches dollar stablecoin on Ethereum and Solana]].
- **On the actual product (confidential self-custody EUR trading):** direct comps are CEXs (Binance, Kraken, Coinbase EU) offering EUR SEPA on-ramps but **custodial and non-private**, and DEX aggregators (1inch, CoWSwap) that are self-custodial but **fully public** and lack a fiat rail. → near.com's position: it is one of the few to combine **fiat EUR in + self-custody + on-chain privacy**; that combination is the real differentiator, not the euro on-ramp alone (a commodity).
- Why the landscape is this way: euro stablecoins are a **fraction of the ~$300B USD market**; MiCA compliance (not product) determines who wins issuance, so the value-add for an app like near.com is **distribution/UX + privacy**, not the token.

## [2] Company / fit
NEAR pivoted from an L1 smart-contract chain to an **"intents"/chain-abstraction** thesis: NEAR Intents cumulative **>$10B swap volume, 15.7M txns, 1.6M users**. The euro rail extends the existing playbook (abstract chains → now abstract fiat entry) into the EU. → Why: NEAR needs consumer volume through near.com to monetize its intents layer; a **regulated EUR on-ramp at the MiCA milestone** is a low-cost way to unlock a compliant EU user base without becoming an issuer/EMI itself.

## [3] Novelty / value-add / traction
- **Genuinely new:** a self-custodial EU app pairing SEPA-Instant EURe minting with on-chain **confidential** trading across 30+ chains. The novelty is **the bundle**, not any component.
- **Weak on traction:** the EUR launch ships with **no adoption numbers**. The adjacent Confidential Intents does have traction (~$26.65M TVL mid-June 2026, ~$541M weekly volume, ~$950K weekly fees early March, 35+ chains) — but that predates and is distinct from the euro rail. → Who captures margin: **Monerium** earns float on EURe reserves; **near.com/NEAR** captures routing/intents fees + potential spread. If EURe stays sub-scale (euro stablecoins are tiny), near.com's euro TAM is structurally capped regardless of UX.

## [4] What's next / sentiment
Timed to **MiCA transition close (2026-07-01)**; expect NEAR to push confidential + EUR as a compliance-friendly EU narrative. Sentiment on Confidential Intents was strong (NEAR token +17% on the Feb launch). Risks: (a) **regulatory** — "confidential" trading rails invite AML scrutiny even with KYC at the edge; (b) **demand** — euro-stablecoin liquidity is thin, so perps/RWA trading in EURe may route back into USD anyway; (c) **dependence** — the euro side is entirely Monerium's; near.com has no issuer moat. → Second-order: the durable asset is NEAR's **intents/private-shard infrastructure**, not the euro on-ramp; the EUR launch is a distribution wedge, and its weight depends on whether confidential execution becomes a category rather than a feature.

## Sources
- PR Newswire (primary): https://www.prnewswire.com/news-releases/nearcom-brings-euros-onchain-enabling-eu-users-to-trade-across-crypto-markets-confidentially-using-their-own-wallets-302815862.html
- near.org blog — Confidential Intents (2026-02-25); CoinDesk (NEAR +17%); Cryptobriefing/Bitget (Confidential Intents TVL $26.65M); Monerium.com / monerium.com/eure (EURe issuer, €6B 2025 vol); Forbes (euro-stablecoin scaling, €450M mkt); CoinGecko/CMC EUR-stablecoin rankings.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. Is the "confidential trading" tech actually new, or repackaged? — **Answered: repackaged.** Confidential Intents went live 2026-02-25; only the SEPA/EURe euro on-ramp is new as of 2026-07-01.
2. Who issues EURe and bears the reserve/redemption risk? — Monerium (MiCA EMT, 1:1 safeguarded euros); near.com is a distributor, issues nothing.
3. Any launch traction on the euro rail (deposits, EUR volume, users)? — **Open / none disclosed.** All cited traction ($26.65M TVL, $541M weekly vol) belongs to Confidential Intents, not the EUR path.
4. Does "confidential" mean AML-free? — No. KYC applies at the SEPA/EURe mint edge; privacy is on-chain trade obfuscation only. Regulatory exposure remains.
5. What fees/spreads does near.com take on the euro flow? — Open; undisclosed. Margin split between Monerium (reserve float) and NEAR (intents/routing fees) unclear.
6. Is euro-stablecoin liquidity deep enough to trade perps/RWAs in EURe? — Doubtful; total euro-stablecoin market ~€450M vs ~$300B USD. Trades likely route via USD, diluting the "euro-native" claim.
7. How does this differ from a CEX EUR on-ramp (Kraken/Coinbase EU)? — Self-custody + on-chain privacy; CEXs are custodial and public. That bundle is the only real differentiator.
8. Is the MiCA-close framing substance or marketing? — Marketing timing; the integration is not contingent on the transition date. (analysis)
9. Which euro stablecoin is used, and is near.com locked to Monerium? — EURe/Monerium only, per external sources; single-issuer dependency = no near.com moat on the euro side.
10. What breaks the thesis? — Thin EURe liquidity, AML crackdown on confidential rails, or Monerium switching partners/pricing.
11. Is there disclosed geographic coverage beyond "EU"? — Only "EU users"; no country list or rollout cadence given. (open)
12. Does near.com custody funds at any point? — No; self-custodial per PR. Custody sits with the user wallet; EURe with Monerium's safeguarding.
13. Freshness vs corpus — is this a duplicate? — **Fresh.** No prior note on near.com/NEAR euro rail or EURe/Monerium; corpus euro-stablecoin notes are different issuers/events.
14. Second-order: what is the durable asset here? — NEAR's intents + private-shard infra, not the euro on-ramp; the EUR launch is a distribution wedge.
15. Would this move markets / matter to a fintech reader? — Modest: a credible but incremental EU on-ramp + privacy bundle from a mid-tier L1, no numbers, single-issuer dependency.

**Importance: 3/5** — A genuine, credibly-built new capability (self-custodial SEPA→EURe on-ramp + on-chain confidential trading) landing squarely on the MiCA-transition moment, from an ecosystem with real intents traction (>$10B cumulative). Capped below 4 because: the privacy tech is four months old (only the euro rail is new), zero launch-traction numbers, the euro side is a resold Monerium/EURe dependency with no near.com moat, and euro-stablecoin liquidity is structurally thin. Fresh, not a duplicate.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-07]] (2026-07-07).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Euro-denominated stablecoins are a tiny but fast-growing slice of the ~$300bn global stablecoin market — euro EMTs reached ~€450m market cap in Jan 2026, up from ~€50m two years earlier (per Forbes/DefiLlama-cited data, via forbes.com, 2026-06-04); euro tokens still hold <1% of global supply but ~80% of the non-USD stablecoin segment (via bitcoinworld.co.in, 2026). Structure: fragmented and issuer-led — 27 stablecoins from 17 entities registered under MiCA across 10 countries (per Bancomat note context, 2025-11). Value in euro-crypto sits in three separable layers — issuance (EMI-licensed token), fiat on/off-ramp (SEPA Instant), and the trading/settlement venue — and near.com is playing the venue/ramp layer, not issuance. "Why now": MiCA's CASP transition window closed 1 July 2026 [[MiCA transitional window for crypto service providers closes 1 July]], forcing every EU-serving venue to be licensed and creating a compliance moat for those inside — near.com timed the launch to that date. Barrier to entry = regulation (EMI/CASP licensing) + SEPA Instant access, not technology.

**Competitive landscape.** Sector KPIs: stablecoin circulating supply (issuer), on/off-ramp volume + SEPA settlement, and for a venue — trading volume / take rate (near.com discloses none of these `[UNSOURCED]`). Two distinct competitor sets:
- *Euro stablecoin issuers* (the token near.com resells): near.com uses **EURe**, issued by **Monerium** (EU-licensed EMI, ~€6bn 2025 transaction volume, per monerium.com). Rivals: **Circle EURC** — largest MiCA euro token, ~€460m cap / ~390m supply Mar 2026, ~41–50%+ euro-market share (per stablecoininsider/coinmarketcap, 2026); **Membrane EUROe** (first EMT post-MiCA, smallest); SocGen **EURCV**, Deutsche/Galaxy **EURAU** [[Deutsche Bank, Galaxy, Flow Traders launch euro stablecoin EURAU]], Bancomat **EUR.bank**. near.com does NOT issue — it distributes someone else's token.
- *Euro on/off-ramp & settlement venues*: ClearBank Europe (EURC in/out via SEPA Instant, "Digital Asset Rails") [[ClearBank Europe launches Digital Asset Rails for settlement]]; centralized exchanges (Kraken, Bitstamp, Coinbase) with SEPA euro rails. near.com's differentiator is **confidential execution** ("Confidential Mode" via a NEAR Protocol private shard) + non-custodial multi-chain (30+ chains, NEAR Intents) — a privacy-first, self-custody positioning vs CEX competitors. Recent peer moves: ClearBank Digital Asset Rails (2026-06); Circle France MiCA EURC/USDC approval (2026). Position: niche entrant `(analysis)` — differentiated on privacy + self-custody, but dependent on Monerium (issuance) and SEPA (rails); moat is thin (the privacy tech is the only proprietary layer; the ramp and token are commodity/partner-supplied).

**Comps & multiples.** No round, valuation, revenue or volume disclosed for this launch → trading-comp multiples = **no data / `[UNSOURCED]`**; distribution not computed, qualitative comparison only. Issuer scale as a rough size guide: EURC ~€460m supply vs EURe's issuer Monerium ~€6bn annual throughput (different metrics — supply vs flow — not directly comparable). Internal comps for the privacy-crypto adjacency: [[Grvt raises $19M for privacy-focused on-chain finance]] (private capital into privacy-focused on-chain finance, 2025-09); [[Deutsche Bank, Galaxy, Flow Traders launch euro stablecoin EURAU]] and [[ClearBank Europe launches Digital Asset Rails for settlement]] as euro-onchain precedents. No comparable public multiple exists.

**Risk flags.**
1. **Regulatory / privacy-vs-AML tension.** "Confidential" euro trading collides directly with EU AML and MiCA transparency/Travel-Rule expectations; a self-custody privacy venue that closed its licence window on 1 July is exactly the profile supervisors scrutinise — the confidentiality feature is the product's edge AND its biggest regulatory tail risk.
2. **Disintermediation / thin moat — value captured elsewhere.** near.com owns neither issuance (Monerium/EURe) nor the fiat rail (SEPA); it sits in the middle as a UX/venue layer. If Monerium or a CEX adds a privacy/self-custody mode, near.com's only differentiator erodes and the euro-flow economics accrue to the issuer and the ramp, not the venue.
3. **Demand-side risk on the euro leg itself.** Euro stablecoins are <1% of global supply; if EURC "stays where it is" the regulated-EUR thesis "needs revisiting" (per deriq/TWIF, 2026-05) [[TWIF USDC grew $18.6 billion as Africa adoption stays thin]]. A confidential-EUR venue is a leveraged bet on a market that has not yet proven product-market fit at scale.

**What this changes (idea-lens).** `(analysis)` This is a *new entry*, not a re-rating — near.com is testing whether "privacy + self-custody + regulated euro rail" is a durable wedge against CEXs now that MiCA has commoditised the licensed-euro-token layer. Falsifiable thesis: if confidential-mode euro volume is material within ~2–3 quarters it validates a privacy premium in EU crypto; it breaks if (a) regulators force disclosure that neuters Confidential Mode, or (b) EURe/EURC supply stays flat, signalling the euro-onchain TAM isn't there yet. Watch: EURe supply trajectory and any EU AML/MiCA guidance on confidential onchain execution as the trigger.

Sources: https://www.prnewswire.com/news-releases/nearcom-brings-euros-onchain-enabling-eu-users-to-trade-across-crypto-markets-confidentially-using-their-own-wallets-302815862.html · https://www.forbes.com/sites/digital-assets/2026/06/04/euro-stablecoins-are-scaling-while-the-digital-euro-waits-on-brussels/ · https://monerium.com/eure/ · https://www.circle.com/eurc · https://stablecoininsider.org/eurc-q1-2026-stablecoin-report/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
