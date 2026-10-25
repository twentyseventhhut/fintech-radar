---
title: "Kalshi Prime and BitGo launch HODL Margining for crypto"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/kalshi
  - company/bitgo
  - industry/crypto
  - region/us
  - type/product
sources:
  - https://www.businesswire.com/news/home/20261022502407/en/Kalshi-and-BitGo-Allow-Customers-to-Unlock-Crypto-Liquidity-for-Margin
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s21da2446
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Kalshi Prime and BitGo launch HODL Margining for crypto

> [!info] 2026-10-23 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Kalshi Prime and BitGo launch HODL Margining, allowing eligible customers to fund futures margin without selling their crypto. Kalshi Katalyst provides U.S. dollar loans secured by BTC, ETH or eligible stablecoins. BitGo Bank & Trust is the first custodian to join the network.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261022502407/en/Kalshi-and-BitGo-Allow-Customers-to-Unlock-Crypto-Liquidity-for-Margin>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Kalshi Prime and BitGo launch HODL Margining for crypto
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **2026-10-21/22** Kalshi and BitGo (NYSE: BTGO) announced **"HODL Margining"** — a crypto-collateralized **margin-financing network**, not a Kalshi product per se. De-PR'd mechanics (tri-party structure): (1) an eligible **Kalshi Prime** client pledges **BTC, ETH, or GENIUS-Act-compliant stablecoins** held in segregated qualified custody at **BitGo Bank & Trust, N.A.**; (2) **Kalshi Katalyst** — a *lending affiliate* of Kalshi Prime, NOT BitGo — extends a **USD loan** against that collateral; (3) the loan proceeds are credited to the client's **Kalshi Prime** account (Kalshi's US-registered FCM) and used as **margin for perpetual futures and other eligible margin products on KalshiEX**. Pledged assets are **not transferred to the venue or sold** — the client keeps legal ownership subject to Katalyst's security interest. BitGo Bank & Trust is the **first custodian**; the PR frames an open "network" with more custodians to follow. Insurance of **up to $250M** on custodied assets is cited. (BusinessWire/StockTitan primary; Unchained, FinanceFeeds, Bitcoin Magazine, The Paypers.)

**Why structured exactly this way / what it reveals.** The three-way split (borrower / affiliated lender Katalyst / independent custodian BitGo) is the tell. (a) By routing the loan through **Katalyst rather than BitGo**, Kalshi keeps the **credit spread and the client relationship** in-house — BitGo is relegated to custody-agent economics, not lender economics. (b) The "customers can **HODL** rather than sell" framing is the real demand hook: the target is **crypto trading firms and large holders already running perps offshore** (Binance/Bybit/Hyperliquid) who don't want a taxable crypto sale just to fund USD margin onshore. (c) GENIUS-Act-only stablecoins + a federally-chartered trust bank = a deliberately **compliance-forward** packaging that distinguishes it from offshore crypto-margin. The structure is engineered so Kalshi monetizes **leverage + lending** on top of its already-approved perps — adding a second revenue layer (loan spread) to a product (perps) it currently runs at **zero trading fees** as a land-grab. (analysis)

## [1] Competitors / peers
- **BitGo + Susquehanna Crypto (2026-03, [[BitGo and Susquehanna Crypto launch OTC access to prediction markets]])** — the closest prior art, and from the *same custodian*: lets institutions trade listed prediction markets OTC posting BTC/stablecoin collateral held at BitGo, min $100k ticket. HODL Margining is the **on-exchange, perps-margin** sibling of that OTC offering — BitGo is building a repeatable "post crypto collateral, trade event/derivatives markets" rail.
- **Coinbase** — vertically integrated rival; routes US clients into perps via its own CFM/Deribit stack and offers crypto-backed USD loans (Morpho-powered) directly. Coinbase owns both venue and lending; Kalshi+BitGo assemble the same stack across two firms.
- **Offshore perp venues (Binance, Bybit, Hyperliquid)** — where crypto-collateralized perp margin is already standard (cross-margin spot+perps). HODL Margining is explicitly the **onshore, CFTC-regulated** answer to exactly that offshore workflow; Hyperliquid (HIP-4, co-authored by Kalshi's John Wang) is the structural competitor Kalshi is chasing.
- **Crypto-backed lenders (Maple, Aave, Ledn, Coinbase/Morpho)** — provide the "borrow USD against BTC" primitive generally; Katalyst's edge is **captive integration** with a CFTC venue + regulated custodian, not a better rate (LTV/rate undisclosed).

**Why the lay of the land is this way / second-order.** Prediction-market/perp venue economics are a **liquidity network effect** that compounds at the venue (KalshiEX holds ~91% US prediction-market share, [[Kalshi holds 91% of US prediction market, BofA data shows]]). Kalshi is now extending its moat **downward into the capital stack** (lending/collateral), capturing the financing spread that offshore venues or third-party lenders would otherwise take. BitGo's role is replaceable-by-design ("first custodian" of a network), so the durable margin accrues to **Kalshi/Katalyst**, not BitGo. The multiple question: does Kalshi earn a defensible lending spread, or does an open custodian network commoditize the collateral leg while Katalyst competes with Coinbase/Maple on rate? (analysis)

## [2] Company history / fit
Kalshi's trajectory is a **relentless march up the institutional/leverage curve**: fully-collateralized event contracts → **FCM license for institutional margin trading** (2026-03, [[Kalshi secures license for institutional margin trading]], a departure from prediction markets' full-collateral norm) → **crypto perps** (BTCPERP live 2026-06, [[Coinbase and Kalshi bring perpetual crypto futures to US]]) → **equity-index perps** ([[Kalshi launches stock index perpetual future]]) → **Webull distribution** (2026-10, [[Webull partners Kalshi to debut crypto-linked perpetual futures]]) → now **crypto-collateralized margin financing**. Valuation arc: $2bn (Jun-25) → $11bn → $22bn Series F ([[Kalshi raises $1 billion Series F at $22 billion valuation]]) → ~$40bn talks ([[Kalshi in talks to raise at $40 billion valuation]]); ~$2bn+ annualized revenue, early IPO talks ([[Kalshi passes $2 billion annualised revenue, in early IPO talks]]). BitGo: NYSE IPO Jan-2026 ([[BitGo prices IPO near $2B valuation for NYSE listing]]), first federally-chartered digital-asset trust bank, but stock trades well below IPO and it cut 15% of staff ([[BitGo cuts 15% of workforce in strategic refocus]], [[BitGo launches $50 million share buyback as stock trades 65% below IPO]]).

**Why the company acts this way.** Kalshi runs perps at **zero trading fees** to grab liquidity — that starves it of per-contract revenue, so it is **structurally pushed to monetize adjacent layers**: financing (loan spreads via Katalyst), order flow, and institutional services. Offering crypto-collateralized margin both (a) removes friction for the exact whales it wants (offshore perp traders avoiding a taxable sale) and (b) opens a **lending P&L** that doesn't depend on reinstating perp fees. For BitGo — a pressured public custodian seeking recurring custody/AUC revenue — becoming the anchor custodian of Kalshi's financing network is a way to attach to the fastest-growing US derivatives franchise. (analysis)

## [3] Novelty / value-add / traction
**Novelty: moderate, not first-of-kind.** Crypto-as-collateral for trading is standard offshore and BitGo already did the OTC-prediction-market version in March 2026. What's genuinely new: **(1)** crypto collateral funding margin on a **CFTC-regulated FCM/DCM (Kalshi Prime/KalshiEX)** — i.e., the onshore, regulated packaging; **(2)** a **GENIUS-Act-gated** stablecoin collateral set + federally-chartered trust-bank custody; **(3)** an explicit **affiliated-lender (Katalyst)** structure so Kalshi captures the financing spread. **Traction: zero disclosed.** This is an **announcement** — no live loan volume, no LTV, no rate, no client count, no utilization. "Eligible customers," "first custodian," "expected to join over time" are all forward framing.

**Why the value-add is real-or-not, deeper.** Who captures the margin? **Kalshi/Katalyst** take the loan spread + feed their perp liquidity; **BitGo** takes thin, commoditizable custody-agent fees (and is explicitly one of a planned *network* of custodians → little pricing power). The real economic unlock is **capital efficiency for whales**: a crypto fund can keep its BTC/ETH exposure *and* run leveraged onshore perps, avoiding a taxable disposal — that is a concrete, non-PR reason the product could pull offshore volume onshore. The break risk is **credit/liquidation**: a crypto-backed loan funding a *leveraged perp* is **double leverage on correlated collateral** — if BTC craters, both the collateral and the perp position move against the client at once, forcing liquidations that can cascade. So the value-add is real for capital efficiency but introduces a **second-order risk that the PR is silent on**. (analysis)

## [4] What's next / market sentiment
Expect **more custodians** to join the network, **LTV/rate terms** to surface, and this to be bundled with Kalshi's perp expansion (ETH/SOL/XRP, equity-index) and distribution deals (Webull). Sentiment sits squarely in the **"bring offshore crypto leverage onshore under a friendly CFTC (Chair Selig)"** tailwind that also powered the perp approvals — but that posture rests on self-certification/no-action, not durable statute, and faces live litigation (CME suit that perps are swaps, not futures). Regulatory backdrop is otherwise favorable: **GENIUS Act** gives a federal stablecoin framework Kalshi leans on; BitGo's federal trust-bank charter provides the custody credibility.

**Why the market goes this way / counterintuitive second order.** The onshore crypto-derivatives build-out is moving from **venue approval → distribution → now financing/collateral** — each layer deepens Kalshi's capture of the stack. Counterintuitively, **adding leverage-on-leverage makes the franchise more fragile, not stronger**: the more whales fund perps with borrowed-against-crypto dollars, the more a single sharp BTC drawdown can trigger **simultaneous collateral-and-position liquidations**, concentrating tail risk at exactly the regulated venue regulators are watching. A high-profile retail/institutional blow-up (echoing the 2025 ~$19bn liquidation episode) could invite CFTC pushback and a product rollback — so the very feature that pulls offshore volume onshore is also the standing tail risk. (analysis)

## Freshness / duplicate verdict
**FRESH.** This is a **distinct new event** — a crypto-collateralized **margin-financing network** (Katalyst loans + BitGo custody) announced 2026-10-21/22. It is **not a reprint** of [[BitGo and Susquehanna Crypto launch OTC access to prediction markets]] (that is *OTC* prediction-market access via BitGo/Susquehanna; this is *on-exchange perps margin* via Katalyst lending), nor of [[Kalshi secures license for institutional margin trading]] (the FCM license itself, March), nor of the perp-approval notes. No existing note covers HODL Margining. Net-new, with real structural novelty (regulated crypto-collateralized leverage) but zero disclosed traction.

## Sources
- BusinessWire primary (via StockTitan): https://www.stocktitan.net/news/BTGO/kalshi-and-bit-go-allow-customers-to-unlock-crypto-liquidity-for-91hyahps9r48.html
- Unchained (tri-party, Katalyst lender, perps margin): https://unchainedcrypto.com/bitgo-held-bitcoin-and-ether-will-secure-perps-margin-loans-for-some-kalshi-prime-clients/
- FinanceFeeds (borrow USD vs crypto): https://financefeeds.com/kalshi-and-bitgo-launch-crypto-backed-margin-financing-network/
- Bitcoin Magazine (deeper into derivatives): https://bitcoinmagazine.com/news/kalshi-pushes-deeper-bitcoin-derivatives
- The Paypers (crypto margin collateral): https://thepaypers.com/crypto-web3-and-cbdc/news/kalshi-teams-up-with-bitgo-for-crypto-backed-futures-collateral
- CryptoBriefing / Coingape (GENIUS-Act stablecoins, structure): https://cryptobriefing.com/kalshi-bitgo-crypto-backed-loans-futures/ · https://coingape.com/kalshi-and-bitgo-partner-to-offer-bitcoin-and-ethereum-backed-loans-for-futures-trading/
- Internal: [[BitGo and Susquehanna Crypto launch OTC access to prediction markets]], [[Kalshi secures license for institutional margin trading]], [[Coinbase and Kalshi bring perpetual crypto futures to US]], [[Kalshi launches stock index perpetual future]], [[Webull partners Kalshi to debut crypto-linked perpetual futures]], [[Kalshi holds 91% of US prediction market, BofA data shows]], [[Kalshi passes $2 billion annualised revenue, in early IPO talks]], [[BitGo prices IPO near $2B valuation for NYSE listing]], [[BitGo cuts 15% of workforce in strategic refocus]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team Q&A

Importance: 3/5.

1. **Is it really new, or a re-run of the BitGo/Susquehanna prediction-market OTC deal?** New. [[BitGo and Susquehanna Crypto launch OTC access to prediction markets]] (2026-03) is *OTC bilateral* trading of listed prediction markets with crypto collateral; HODL Margining is *on-exchange* USD margin loans (via Katalyst) to fund **perps and margin products on KalshiEX**. Same custodian, different mechanism. *Answered: fresh.*
2. **Who actually lends — BitGo or Kalshi?** **Kalshi Katalyst**, a lending affiliate of Kalshi Prime. BitGo Bank & Trust is only the **collateral custodian/agent**. So Kalshi, not BitGo, owns the loan spread and credit relationship. *Answered.*
3. **Announced or live?** **Announced only.** No live loan volume, utilization, client count, or launch metrics disclosed. *Answered: announced, not adopted.*
4. **What is the LTV and interest rate?** **Undisclosed.** No loan-to-value ratio, rate, margin-call thresholds, or liquidation mechanics published — the core credit terms are silent. *Open: economics undisclosed.*
5. **Precise mechanism delta vs offshore (Binance/Bybit/Hyperliquid cross-margin)?** Offshore venues let you post crypto directly as perp margin on one platform; here it's a **tri-party onshore** structure — crypto stays in regulated custody (BitGo), a separate affiliated lender (Katalyst) issues USD, and that USD margins CFTC-regulated perps. The delta is **regulatory packaging**, not a novel financial primitive. *Answered.*
6. **Why route the loan through Katalyst rather than BitGo?** So Kalshi captures the **financing spread and client relationship**; BitGo gets commoditizable custody-agent fees. It also keeps credit risk inside the Kalshi complex. *Answered (analysis).*
7. **Who captures the margin in the stack?** **Kalshi/Katalyst** (loan spread + perp liquidity); **BitGo** thin custody fees and explicitly "first of a network" of custodians → little pricing power. *Answered (analysis).*
8. **Is this double leverage?** Yes — a **loan against crypto** used to **margin a leveraged perp**, with correlated collateral. A sharp BTC/ETH drawdown hits collateral value *and* the perp position simultaneously → forced liquidations that can cascade. The PR is silent on this. *Answered: key risk.*
9. **Who is the real target customer?** **Crypto trading firms and large holders already running perps offshore** who want to avoid a taxable crypto sale to fund onshore USD margin. Capital efficiency / tax deferral is the genuine pull, not PR. *Answered.*
10. **Why GENIUS-Act-only stablecoins + a federal trust bank?** Deliberate **compliance-forward** packaging to differentiate from offshore crypto-margin and give institutions a regulated-custody, federal-framework story. Narrows eligible stablecoins to the federal regime. *Answered.*
11. **How replaceable is BitGo?** Highly — PR explicitly frames an open "network" with "more custodians expected to join," and BitGo is merely "first." BitGo gains volume but no exclusivity or durable moat. *Answered.*
12. **Does this help Kalshi or BitGo more?** **Kalshi** — it monetizes a lending layer on top of zero-fee perps and pulls offshore whale volume onshore. BitGo (stock below IPO, 15% layoffs) gets incremental AUC/custody revenue but is a swappable node. *Answered (analysis).*
13. **Why would Kalshi do this if perps are zero-fee?** Precisely *because* perps are zero-fee — Kalshi needs a **non-fee revenue layer**; the loan spread via Katalyst is that layer, plus the leverage deepens perp liquidity/network effect. *Answered (analysis).*
14. **What's the regulatory fragility?** Rests on the same friendly-CFTC (Selig) self-certification/no-action posture as the perp approvals — reversible, and the category is litigated (CME suit: perps are swaps not futures). A retail/institutional liquidation blow-up could invite a rollback. *Answered: reversible basis.*
15. **Is it tradeable for readers?** BitGo is public (NYSE: BTGO) — the only listed read-through, though its exposure here is small/commoditizable; Kalshi is private (~$22-40bn rounds). Peers: Coinbase (COIN, integrated lending+perps). *Answered.*
16. **Does it change the central question?** Yes: not "can you post crypto as collateral" (offshore does already) but "**does assembling regulated crypto-collateralized leverage onshore pull offshore perp volume to Kalshi — and does the leverage-on-leverage concentrate tail risk at the one venue regulators watch most?**" *Answered.*

Importance: 3/5 — rationale: a **genuinely new, structurally meaningful** event — the first **CFTC-regulated, crypto-collateralized margin-financing network** funding perps, with a deliberate affiliated-lender (Katalyst) + federal-trust-bank (BitGo) packaging and a GENIUS-Act stablecoin gate. It materially advances Kalshi's march up the capital stack (full-collateral → FCM margin → perps → now financing) and targets a concrete demand (offshore whales avoiding taxable sales). Marked up from 2 because of real structural novelty (regulated leverage-on-crypto), a sizeable franchise (KalshiEX ~91% US share, ~$22-40bn valuation), and a publicly-listed custodian (BTGO). Marked down from 4 because it is **announcement-only with zero disclosed traction** (no LTV, rate, volume, or client data), the collateral-as-margin primitive is standard offshore and BitGo already did an OTC version in March, the economics are undisclosed, and it introduces an unaddressed double-leverage/liquidation-cascade risk.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-25]] (2026-10-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Prediction-market infrastructure crossed into crypto collateral/margining. Kalshi traded ~$81.5bn in contracts ($18.8bn in dollars paid) over Sep 22–Oct 21 2026, ~76% of prediction-market volume, +53% QoQ (per defirate/blockonomi web data, as of Oct 2026); it is now the dominant CFTC-regulated venue (claims ~95% of US prediction-market revenue, ~$4bn annualized, sports-led). Crypto-collateralized credit is the adjacent driver: the broader asset-based lending market was projected at ~$1.3tn by 2030 (per a July 2025 report, via CoinDesk — see internal comp). Structure: Kalshi sits at exchange + clearing + now lending (Katalyst/Klear), capturing value across the stack; BitGo supplies the qualified-custody rail. Barriers are heavily regulatory (CFTC designation as FCM/DCM/DCO; GENIUS Act-compliant stablecoin eligibility; federally chartered trust bank for custody) — not easily replicated by offshore venues. "Why now": Kalshi launched the first US CFTC-regulated crypto perpetual futures on 29 May 2026 (BTC 3 Jun, ETH 4 Jun), so it needs crypto-native margin funding to feed that book, and is pulling offshore perp traders onshore. Note: Kalshi Klear separately applied to the CFTC for margin on event contracts via BTC-backed loans (per predictionnews) — adjacent but distinct from this HODL Margining launch (which funds futures margin).

**Competitive landscape.** Sector KPIs: notional/dollar volume, take rate (fees), AUC (custodian), loan-to-value and interest spread on the credit leg. The tri-party structure here = Kalshi Prime (FCM) + Kalshi Katalyst (lending affiliate, originates USD loans) + BitGo Bank & Trust (first custodian; segregated qualified custody, up to $250m insurance per web reporting). Competing crypto-collateral credit models: Coinbase BTC-backed loans (>$1bn, Oct 2025 — [[Coinbase's Bitcoin-backed loans surpass $1 billion]]); JPMorgan accepting BTC/ETH as collateral via a third-party custodian ([[JPMorgan to accept Bitcoin and Ethereum as collateral]]); OKX/Standard Chartered off-exchange collateral mirroring ([[OKX expands Standard Chartered collateral partnership to EEA]]); US Bank custodying for Anchorage ([[US Bank to custody reserves for Anchorage Digital stablecoins]]). On prediction markets specifically, Polymarket is the main rival (Kalshi ~76% share of combined volume) and Robinhood is expanding prediction markets ([[Robinhood explores launching prediction markets outside US]]). Position: Kalshi is ahead and widening — it is the only one pairing a regulated US perps venue with its own lending affiliate and an open multi-custodian network. Moat: regulatory licence stack + network effects of being the liquidity venue; switching costs for traders once collateral is pledged (analysis).

**Comps & multiples.** Private names — round valuations, not market caps:
- Kalshi: ~$22bn (Series F, Coatue-led, May 2026, $1bn raised); finalizing a new round at ~$40bn ahead of a planned IPO (Bloomberg, Sep 2026). At ~$4bn annualized revenue, $40bn ÷ $4bn ≈ **10x revenue** — rich in absolute terms but paired with +50–70% QoQ volume growth, so revenue-multiple premium tracks the growth rate rather than flagging over-valuation on its own.
- BitGo: IPO'd Jan 2026 at $18/share, ~$2bn valuation; AUC ~$81.6bn (Q4 2025, down 22% from ~$104bn in Q3 on crypto drawdown) (per PYMNTS/CoinDesk/Yahoo, as of Jan 2026). EV/Revenue not computed — revenue not publicly broken out here → no data.
- Internal credit comps: Coinbase BTC loans >$1bn ([[Coinbase's Bitcoin-backed loans surpass $1 billion]]); JPMorgan collateral ([[JPMorgan to accept Bitcoin and Ethereum as collateral]]).
Distribution not computed (mixed models/scale); qualitative: Kalshi carries an exchange-platform multiple, BitGo a lower infrastructure/custody multiple — consistent with where each sits in the stack.

**Risk flags.**
1. **Leverage-on-leverage / liquidation risk.** A trader pledging BTC to margin a BTC perpetual is long the same asset twice: a price drop simultaneously erodes collateral value and raises the margin call, forcing liquidation — the exact failure mode of 2022 crypto lending desks. Recent BTC volatility already triggered large leveraged-long liquidations (per Forbes/oddsshopper, 2026). Second-order: cascading liquidations could feed back into Kalshi's own perp book.
2. **Regulatory / novelty exposure.** This is CFTC-regulated-but-new territory; critics argue US perps were approved without enhanced retail protections, and the separate Kalshi Klear CFTC application (leverage limits, client tiers undisclosed) shows the rulebook is still being written. Second-order: an adverse CFTC ruling or a high-profile retail blowup could freeze the product line.
3. **Custodian/counterparty concentration.** BitGo Bank & Trust is the first and (so far) only custodian; Katalyst is the sole lender. Despite segregation + $250m insurance, a BitGo solvency/operational event or a GENIUS Act stablecoin de-peg among eligible collateral would stress the whole tri-party chain until the "additional custodians" network actually materializes (announced, not yet live).

**What this changes (idea-lens).** This is a re-rating of prediction-market operators from pure event venues toward full derivatives-exchange infrastructure (exchange + clearing + lending), justifying Kalshi's ~$40bn target (analysis). Falsifiable thesis: onboarding ≥2 more custodians and non-trivial loan balances within ~2 quarters would confirm the network model; trigger to watch = CFTC action on the Klear leverage application and the first disclosed HODL Margining loan volumes. What breaks it: a liquidation-driven retail-loss episode prompting a CFTC clampdown before the multi-custodian network scales.

Sources: https://www.businesswire.com/news/home/20261022502407/en/Kalshi-and-BitGo-Allow-Customers-to-Unlock-Crypto-Liquidity-for-Margin · https://financefeeds.com/kalshi-and-bitgo-launch-crypto-backed-margin-financing-network/ · https://www.cryptotimes.io/2026/10/23/kalshi-and-bitgo-launch-crypto-backed-loans-for-futures-margin/ · https://www.bloomberg.com/news/articles/2026-09-30/kalshi-finalizing-new-funding-at-40-billion-value-ahead-of-ipo · https://www.bloomberg.com/news/articles/2026-05-07/kalshi-secures-22-billion-valuation-in-coatue-led-round · https://www.coindesk.com/markets/2026/01/21/bitgo-prices-ipo-at-usd18-pitching-custody-growth-over-crypto-trading-swings · https://predictionnews.com/story/kalshi-to-allow-leveraged-futures-bets-with-bitcoin-backed-loans · https://blockonomi.com/prediction-market-statistics-2026-kalshi-polymarket-and-the-numbers-behind-the-boom
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
