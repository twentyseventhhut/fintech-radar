---
title: "Chainlink and banks launch Project Pangea for T+0 FX settlement"
date: 2026-06-24
tags:
  - company/chainlink
  - industry/blockchain
  - industry/fx
  - region/global
  - type/partnership
sources:
  - https://newsletter.thepaypers.com/i/zAFigoyMQbie1sL_57UsFYW4zYoGnvguEJt_503QBrK3Yna276OIja8jGcreDSpE-LYBCqasGwqBilFSVEgAuy8kuV25Kw0zzx3lhsgaI1A7UHZS_2TtK7euRX1EPSWUqc2TWiJIiKvWl7iJ7h1icwbsbAWPUnnGbwVRH5IdVQTKRAIUiCGGZNKy_BQBujvFRujqrIDxWNlDHhG0a4JAiomEfw0kLYPT
status: published
n_mentions: 1
channels:
  - "The Paypers"
story_id: s131e17d6
month: 2026-06
enriched: true
importance: 2
---

# Chainlink and banks launch Project Pangea for T+0 FX settlement

> [!info] 2026-06-24 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: The Paypers

## Агрегированный текст (из дайджестов)

[The Paypers] Chainlink and multinational banking consortia launch Project Pangea for T+0 FX settlement

## Первоисточники

### newsletter.thepaypers.com
<https://newsletter.thepaypers.com/i/zAFigoyMQbie1sL_57UsFYW4zYoGnvguEJt_503QBrK3Yna276OIja8jGcreDSpE-LYBCqasGwqBilFSVEgAuy8kuV25Kw0zzx3lhsgaI1A7UHZS_2TtK7euRX1EPSWUqc2TWiJIiKvWl7iJ7h1icwbsbAWPUnnGbwVRH5IdVQTKRAIUiCGGZNKy_BQBujvFRujqrIDxWNlDHhG0a4JAiomEfw0kLYPT>
*694 слов · direct*

Chainlink and multinational banking consortia launch Project Pangea for T+0 FX settlement
Paula Albu
24 Jun 2026 / 5 Min Read
Chainlink and banking consortia from Europe and South Korea have launched Project Pangea to develop real-time stablecoin-based settlement for global FX markets.
Chainlink has announced Project Pangea, a collaborative initiative with two multinational banking consortia aimed at developing real-time, atomic settlement infrastructure for global foreign exchange markets. The initiative brings together UniKA, a Korean coalition comprising Shinhan Bank, JB Bank, Kbank, FairSquareLab, and OBDIA, alongside more than ten participating Korean commercial banks, and Qivalis, a euro stablecoin consortium backed by 37 European banks. The participating institutions collectively represent more than USD 10 trillion in assets under management.
Project Pangea focuses on enabling direct atomic Payment-versus-Payment swaps of regulated EUR and KRW stablecoins, targeting T+0 settlement as an alternative to the T+2 model that currently governs most FX transactions.
Technical architecture
The project is structured across three layers. The banking layer uses Swift and ISO 20022 messaging standards, allowing participating institutions to connect using existing infrastructure. The connectivity layer uses Chainlink's Cross-Chain Interoperability Protocol (CCIP) for secure stablecoin transfers across networks, and Chainlink Data Streams for high-speed FX market data to power an on-chain pricing engine. The settlement layer operates on FairSquareLab's Pangea L1 blockchain - a settlement-dedicated network designed as neutral infrastructure independent of any single country or bank - where FX settlement smart contracts are deployed, and atomic swaps execute.
FairSquareLab's on-chain FX settlement technology anchors price discovery to FX oracle quotes rather than a bonding curve, minimising slippage for large-scale interbank currency conversion. A key design feature of the Pangea L1 is that oracle data updates are guaranteed to execute ahead of every other transaction in a block, ensuring all FX swaps settle against current market prices.
Market context and settlement risk
The global FX market processes more than USD 9.6 trillion in daily trading volume, yet cross-border transactions remain subject to multi-day settlement cycles and reliance on intermediary currencies for conversion. T+2 settlement introduces counterparty and settlement risk across the period between trade execution and final settlement - a structural inefficiency that atomic, real-time settlement would eliminate by completing both legs of a transaction simultaneously.
Project Pangea uses ISO 20022 standards and Swift infrastructure as the entry point for banks, allowing institutions to participate without replacing existing payment messaging systems. Instructions submitted through familiar banking infrastructure are translated into on-chain settlement actions through Chainlink CCIP.
The initiative establishes a scalable multi-currency settlement network beginning with EUR and KRW corridors, with the architecture designed to expand to additional currencies over time.
 News on Crypto, Web3 and CBDC
Meta reportedly develops stand-alone prediction markets app
Chainlink and multinational banking consortia launch Project Pangea for T+0 FX settlement
Neo and Triple-A partner on stablecoin treasury integration
Ripple receives preliminary MiCA CASP licence in Luxembourg
OSL Group obtains Australian financial services licence
 Expert views on Crypto, Web3 and CBDC
Digital assets and the future of money movement: where stablecoins and tokenized deposits are creating value today
The quiet revolution: how stablecoins are rewiring the plumbing of global finance
Latvia: the strategic gateway for MiCA compliance – a business case analysis
From speed skating to stablecoins: the race to modernise payment rails
Stablecoin governance risks, fraud vulnerabilities, and monetary sovereignty
 The Paypers is a global hub for market insights, real-time news, expert interviews, and in-depth analyses and resources across payments, fintech, and the digital economy. We deliver reports, webinars, and commentary on key topics, including regulation, real-time payments, cross-border payments and ecommerce, digital identity, payment innovation and infrastructure, Open Banking, Embedded Finance, crypto, fraud and financial crime prevention, and more – all developed in collaboration with industry experts and leaders. 
Categories
 Payments 
 Fraud and Fincrime 
 Fintech 
 Crypto, Web3 and CBDC 
 Regulations 
 M&A and Investments 
Current themes
 A2A Payments 
 Payment Orchestration 
 TradFi and DeFi Convergence 
 KYC, KYB and Digital Identity 
 Scams and Fraud 
 Embedded Finance 
 Real-Time Payments 
The Paypers
 Team 
 Advertise 
 About 
Contact
The Paypers
Prinsengracht 777e 
1017 JZ Amsterdam
P: +31 20 658 0652
No part of this site can be reproduced without explicit permission of The Paypers (v2.7).
 Privacy Policy  / Cookie Statement 
Copyright

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Chainlink and banks launch Project Pangea for T+0 FX settlement
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On **2026-06-23** (Zurich dateline), Chainlink announced **Project Pangea** — explicitly a **"strategic task force," not a live payment network**. CoinDesk: "no production system has launched yet." The aggregated note already over-states it by saying banks "**launch**" the system; the accurate verb is **convene a working group**.

- **Goal:** move **EUR↔KRW** FX from T+2 (~48h) to **T+0** via **atomic Payment-versus-Payment (PvP) swaps**.
- **What settles:** **regulated EUR and KRW stablecoins** — NOT central-bank money and NOT (per sources) tokenized commercial-bank deposits. This is a *stablecoin* design, narrower than the wider tokenized-deposit thesis in [[Kaleido explains tokenized deposit models and infrastructure]] and [[Fintech Wrap Up explainer on the BIS unified ledger]].
- **Organizers:** Chainlink (CCIP + Data Streams + CRE orchestration over Swift/ISO 20022); **FairSquareLab** (operates the dedicated "**Pangea L1**" settlement chain, anchors price to FX oracle quotes not a bonding curve); **Qivalis** (euro-stablecoin consortium, "37 European banks"); **UniKA / Unified Korea Alliance** (10+ Korean banks).
- **Headline metrics — marketing aggregates, not commitments:** "47 banks" (some outlets "50+"), ">$10T AUM," "$150B/yr Europe–Korea trade corridor." None is committed capital or settled volume.

**Why structured this way / what it reveals:** Pangea is sold as a *standards-compatible overlay* — banks keep Swift + ISO 20022 messaging while CCIP/CRE translate instructions into on-chain settlement. That choice minimizes bank integration cost (good adoption design) **but also means Chainlink stays middleware**: it neither holds the money nor operates the settlement venue (that is FairSquareLab's L1 + the two consortia). The PR anchors to a $9.6T/day FX TAM and $10T AUM to make an *aspirational* task force look like infrastructure. Chainlink VP Niki Ariyasinghe pre-empted the vaporware charge: "This is not just a POC… target is live transactions within a legal/regulatory framework within the next 12 months" — i.e. **nothing is live today** (analysis).
- URLs: https://www.prnewswire.com/news-releases/chainlink-and-multinational-banking-consortia-launch-project-pangea-to-develop-t0-settlement-framework-for-international-fx-markets-302807910.html · https://www.coindesk.com/markets/2026/06/23/chainlink-teams-up-with-47-south-korean-european-banks-to-speed-up-international-money-transfers · https://thefullfx.com/working-group-plans-onchain-fx-settlement-project/

## [1] Competitors / peers
On the **atomic-PvP / tokenized FX-settlement** thesis, Pangea is a **laggard, not a leader**. Live, real-volume rails already exist (dates/status, external):
- **JPMorgan Kinexys** (ex-Onyx): live in prod since 2020; on-chain FX live; ~$3T cumulative, ~$5B/day avg (Kinexys 2026 Milestones, 2026-04-28). Already used for client FX in our corpus — see [[Corpay Cross-Border uses Kinexys blockchain for FX conversions]] (settles "within minutes" after hours) and [[Ondo, J.P. Morgan, Mastercard, Ripple complete tokenized Treasuries pilot]].
- **Broadridge DLR on Canton:** ~$8T processed in March 2026 (~$354B/day), +392% YoY.
- **Partior** (DBS/JPM/StanChart/Temasek): live commercial USD/EUR/SGD; first EUR via Deutsche Bank Sep 2025.
- **Fnality** (Sterling FnPS): live (controlled) since Dec 2023; BoE finality designation Dec 2024.
- **SWIFT shared ledger:** real-value MVP planned 2026 — note Chainlink ALSO partnered Swift earlier, [[Swift partners Chainlink for multi-bank digital asset settlement]] (2026-01).
- **BIS Project Agorá:** 8 central banks + 40+ firms, advancing to real-value testing (report 2026-05-27) — the closest *consortium* analogue, with far stronger counterparties (central-bank money).

**Why the lay of the land is this way (second-order):** the credible settlement layer is being captured by **bank-owned ledgers (Kinexys, Partior, Fnality) and central-bank consortia (Agorá)** — entities that already hold the money and the regulatory standing. Pangea's neutral-L1 + stablecoin route is differentiated on *neutrality* and the *specific EUR↔KRW corridor*, but on volume and credibility it is years behind (analysis). URLs: https://www.jpmorgan.com/payments/newsroom/kinexys-milestones-2026 · https://www.bis.org/press/p260527.htm

## [2] Company history / fit
Genuine strength: **CCIP is real and in production** (mainnet 2023→GA 2024, disclosed multi-chain volume); **CRE** went live Nov 2025. The orchestration story Pangea leans on therefore rests on shipped infrastructure. **But the fit risk is structural:** Chainlink is **oracle/messaging middleware**, not a bank or a settlement venue. Its institutional history is a logo-wall of *pilots* with few production conversions and almost no disclosed volume — Swift/UBS pilot (2024), DTCC Smart NAV pilot (2024), one "first" live uMINT tx (Nov 2025), a $50M Sygnum/Fidelity NAV position.

**Why Chainlink acts this way:** as middleware it cannot generate revenue without consortia doing real settlement, so it manufactures demand via high-profile bank task forces that supply counterparties and regulatory cover (analysis). Pangea is the **earliest, least-committed stage** of exactly this pattern. URL: https://www.swift.com/news-events/press-releases/swift-ubs-asset-management-and-chainlink-successfully-complete-innovative-pilot-bridge-tokenized-assets-existing-payment-systems

## [3] Novelty / value-add / traction
**Novelty: modest.** Atomic PvP stablecoin FX is already pursued by Partior, Fnality, Kinexys, Swift's MVP, ISDA/Ant under MAS Guardian, and BIS Agorá. Pangea's distinct angle = **EUR↔KRW corridor + neutral L1 + Chainlink orchestration over Swift/ISO 20022** (oracle updates guaranteed first-in-block to settle at current price).

**Traction: near zero today.** No live transactions, no named European banks, no named regulator, no economics. The market verdict: **LINK flat-to-down** on the news (FXStreet 2026-06-24, "partnership fails to lift sentiment," LINK ~$8, ~82% below ATH; analysts cite "no near-term fee generation").

**Why the value-add is unconfirmed (deeper):** even if it ships, the **margin in the stack** likely accrues to whoever issues the EUR/KRW stablecoins and operates the settlement L1 (FairSquareLab + consortia), with Chainlink earning thin messaging/oracle fees — undisclosed. The thing that would make this matter is **a first executed transaction + a named European bank**, neither of which exists (analysis). URL: https://www.fxstreet.com/cryptocurrencies/news/chainlink-price-forecast-global-fx-infrastructure-partnership-fails-to-lift-sentiment-202606240757

## [4] What's next / market sentiment
Watch-fors: (1) a **first executed Pangea L1 transaction** (testnet or live) — none yet; (2) **named European banks** / actual roster (currently aggregate "37" only); (3) **regulatory sign-off** for EUR (MiCA) and KRW (FSC) wholesale stablecoin settlement; (4) a first-party chain.link post or Reuters/Bloomberg confirmation (absent — all coverage traces to one 2026-06-23 release); (5) LINK fee/value-accrual mechanics (undisclosed); (6) whether Pangea **converges with or is eclipsed by** Swift's 2026 MVP and BIS Agorá real-value testing.

**Why the market shrugged (second-order):** with credible live rails already moving $5B–$350B/day, a counterparty-light, regulator-light EUR↔KRW *task force* adds little marginal information — hence the non-reaction. The aggregate "$10T AUM / 47 banks" framing, ironically, signals *weakness*: real commitments are named bilaterally; aggregates are named when individual commitments are thin (analysis).

## Sources
- The Paypers (primary, in note): https://newsletter.thepaypers.com/i/... "Chainlink and multinational banking consortia launch Project Pangea for T+0 FX settlement" (2026-06-24)
- PR Newswire / CoinDesk / The Full FX / Markets Media / FXStreet (URLs above)
- Internal: [[Swift partners Chainlink for multi-bank digital asset settlement]], [[Fintech Wrap Up explainer on the BIS unified ledger]], [[Ondo, J.P. Morgan, Mastercard, Ripple complete tokenized Treasuries pilot]], [[Corpay Cross-Border uses Kinexys blockchain for FX conversions]], [[Kaleido explains tokenized deposit models and infrastructure]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Did banks actually "launch" anything?** No — it is a **task force / framework** announced 2026-06-23. "No production system has launched yet" (CoinDesk). The note title's verb "launch" overstates it.
2. **Is it live in production?** No. Aspirational target: "live transactions within ~12 months."
3. **Is it even a running pilot or testnet?** **Open/unconfirmed** — sources describe planning, not a launched pilot. No testnet tx cited.
4. **What settles T+0 — real money?** No. **Regulated EUR/KRW stablecoins.** Not central-bank money; not (per sources) tokenized deposits.
5. **Which European banks are committed?** **Open** — only "37 European banks via Qivalis" in aggregate; none individually named. That aggregation is a red flag for thin individual commitment.
6. **Which Korean banks?** Confirmed steering committee: **Shinhan, JB Bank, Kbank** (+FairSquareLab, OBDIA infra); "10+" total, rest unnamed.
7. **Any transaction volume or live counterparties?** None disclosed. The only $ figure is the **$150B/yr corridor size** — not settled volume.
8. **Hard go-live date or regulatory approval?** No date; **no regulator named** as approving (MiCA EUR issuer? Korean FSC?). "Open."
9. **Is this Chainlink's first FX/settlement bank tie-up?** No — it follows Swift/Chainlink (2026-01, see corpus), Swift/UBS pilot (2024), DTCC Smart NAV (2024). Pattern of pilots, few production conversions.
10. **Precise mechanism delta vs incumbents?** Neutral L1 + oracle quotes guaranteed first-in-block so swaps settle at live mid — vs Kinexys/Partior/Fnality which are bank-operated and already live. Differentiation is *neutrality + EUR↔KRW corridor*, not a settlement breakthrough.
11. **Who captures the margin?** Likely stablecoin issuers + FairSquareLab's L1 + consortia; Chainlink earns thin messaging/oracle fees — undisclosed. Analysts: "no near-term fee generation."
12. **Did the market believe it?** No — **LINK flat-to-down** (FXStreet 2026-06-24). Clearest skeptical signal given sparse critical coverage.
13. **Is the "$10T AUM / 47 banks" meaningful?** Marketing aggregate; "47" vs "50+" inconsistent across outlets. Not committed capital.
14. **Independent confirmation?** Weak — all coverage derives from one 2026-06-23 release; no first-party chain.link post, no Reuters/Bloomberg.
15. **Who's silent about what?** Economics, go-live date, named EU banks, regulatory status, LINK fee accrual — all undisclosed.

### Importance: 2/5 — rationale
The *theme* (atomic PvP FX settlement, tokenized cross-border payments) is genuinely important, but **on that theme Pangea is a laggard**: live, real-volume rails already exist (Kinexys ~$5B/day on-chain FX; Broadridge DLR ~$354B/day; Partior/Fnality live PvP), and the strongest consortium effort (BIS Agorá, 8 central banks) has far better counterparties. Pangea today is a framework with **no live system, no named European banks, no regulator, no volume, no economics**, riding Chainlink's pilot-heavy/production-light pattern — and the market priced it as a non-event (flat LINK). It rates **2** not **1** only because it is real and first-party-documented, Chainlink's underlying CCIP/CRE rails are genuinely in production, and the EUR↔KRW corridor is a plausible niche. Re-rate up on a first executed transaction + named EU banks + regulatory sign-off.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Включено в дайджест [[Posts/2026-06-25]] (2026-06-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** FX is the world's largest market: OTC turnover hit **USD 9.6tn/day in April 2025** (net-net, all instruments), up 28% from $7.5tn three years earlier (per BIS Triennial Survey 2025, via cls-group.com). The structural problem Pangea targets is settlement risk in the cross-border leg: per the same survey, only ~36% of daily settlement (~$5tn) runs through PvP (CLS) that eliminates settlement risk, ~54% ($7.6tn) uses risk-mitigating netting, and ~10% (**$1.4tn/day**) still settles gross-bilateral, fully exposed to Herstatt risk (via cls-group.com). The legacy rail is T+2 + correspondent chains (1–5 business days, 2–3 intermediaries each adding fees — see [[Kaleido explains tokenized deposit models and infrastructure]]). Structure: settlement is concentrated (CLS is the dominant PvP utility, $2.54tn/day in Apr 2025, +37% vs 2022) but the long tail of currency pairs CLS doesn't cover — incl. KRW, a non-CLS currency — is where atomic on-chain PvP has the clearest opening. "Why now": MiCA (2023) pushed EU banks to build a regulated euro stablecoin answer to USD-stablecoin dominance, and Korea's won-stablecoin debate is heating into H2 2026 — Pangea rides both regulatory openings (via cryptobriefing.com, en.sedaily.com).

**Competitive landscape.** Sector KPIs: settlement value/day, PvP coverage %, settlement-risk exposure ($ gross-bilateral), settlement latency (T+2 → T+0). Basis of competition here is **distribution + neutrality of the settlement rail**, not price. Players splitting into camps: (1) incumbent utility — **CLS** (PvP standard, but not 24/7, excludes many EM currencies); (2) bank-led tokenized-deposit/clearing rails — **Citi** 24/7 USD clearing + Citi Token Services ([[Citi and Swift conclude fiat-to-digital asset settlement trial]], Nov 2025), **HSBC** TDS ([[HSBC launches tokenized deposit service with Ant International]], Sep 2025), **JPMorgan Kinexys** ([[Ondo, J.P. Morgan, Mastercard, Ripple complete tokenized Treasuries pilot]], May 2026); (3) infra/oracle layer — **Chainlink** (CCIP + Data Streams) and **Canton**-based **ClearToken CT Settle** ([[ClearToken launches CT Settle multi-currency settlement solution]], Dec 2025), Circle×Finastra ([[Circle partners with Finastra on cross-border stablecoin payments]], Sep 2025). Recent move: Swift flipped on blockchain wallet-address attachment for its 11,500 members in Nov 2025, with Chainlink as the connectivity layer (via blog.chain.link). Chainlink's position: **infrastructure-layer, not a competing settlement venue** — it provides CCIP messaging + FX oracle data, while settlement sits on FairSquareLab's Pangea L1 and the value (stablecoins) sits with the banks. Moat (analysis): incumbency in the Swift-adjacent oracle slot + 50+ bank distribution; weak point is that the economically valuable layer (the stablecoins, the float) is captured by the bank consortia, not Chainlink.

**Comps & multiples.** No revenue/EV figures are disclosed for Pangea, UniKA or Qivalis (private consortia) → deal multiple = **no data**. The only listed/liquid comparable is the LINK token: market cap **~$5.2bn** at ~$7.21 (84% below ATH), but token cap ≠ protocol revenue and Chainlink does not publish audited fee revenue, so EV/Revenue, P/E, etc. = **[UNSOURCED]** — a price-per-unit multiple cannot be computed honestly. Operational comp instead of valuation comp: CCIP did **$7.77bn transfers in 2025 (+1,972%)** and ~$18bn/month volume, connecting 60+ chains (via blockeden.xyz) — non-trivial but ~3 orders of magnitude below FX's $9.6tn/day, so Pangea is a pilot footprint vs the TAM, not a captured share. Internal comps above (Citi, HSBC, JPM, ClearToken, Circle) are all 2025–26 pilots/launches in the same tokenized-settlement wave — none has published settled-volume economics either, so **distribution not computed, qualitative comparison only**: this is a crowded, pre-revenue field of announcements.

**Risk flags.**
1. **Announced ≠ live (execution/de-PR).** The consortia state live transactions are ~12 months out; the euro stablecoin (Qivalis) is only "anticipated H2 2026" and KRW stablecoin issuance is still a legislative debate in Korea — i.e. two of the two settlement assets do not yet legally/operationally exist. Second-order: timeline slip or regulatory rejection of a won stablecoin would strand the KRW corridor entirely.
2. **Disintermediation / value capture by another layer.** Chainlink supplies messaging + oracles but the economics (stablecoin float, FX spread) accrue to the 50+ banks and to FairSquareLab's Pangea L1; the oracle layer is the most commoditizable / substitutable slot. If a bank consortium standardizes on a rival oracle or builds in-house, Chainlink's role is thin.
3. **Concentration & neutrality claims unproven.** The "neutral, country-independent L1" runs on FairSquareLab's chain with oracle data privileged to execute first in every block — a single-vendor dependency and a single point of trust/failure dressed as neutrality; regulators and banks will scrutinize who controls the L1 and the oracle.

**What this changes (idea-lens).** (analysis) Pangea is a **new-entry attack on CLS's non-PvP long tail** (EM/Asia corridors CLS doesn't serve), not a frontal assault on the cleared majors — that's the falsifiable thesis: if 12 months out there is real EUR↔KRW atomic settlement volume on regulated stablecoins, it signals on-chain PvP can eat the $1.4tn/day gross-bilateral exposure CLS leaves open. Trigger to watch: (a) Qivalis euro stablecoin actually launching in H2 2026 and (b) a Korean won-stablecoin legal framework passing. Thesis breaks if, by mid-2027, Pangea is still a press-release task force with no settled volume — the base case for most entrants in this crowded tokenized-settlement field.

Sources: https://www.prnewswire.com/news-releases/chainlink-and-multinational-banking-consortia-launch-project-pangea-to-develop-t0-settlement-framework-for-international-fx-markets-302807910.html · https://www.cls-group.com/insights/policy/fx-policy-04-bis-triennial-survey-2025-fx-settlement-risk-you-can-t-fix-what-you-can-t-measure-shapingfx-series/ · https://www.bis.org/statistics/rpfx25_fx.htm · https://cryptobriefing.com/chainlink-korean-and-european-banks-launch-project-pangea/ · https://en.sedaily.com/finance/2026/06/25/shinhan-woori-launch-coin-experiment-with-european-banks · https://blog.chain.link/the-swift-and-chainlink-partnership/ · https://blockeden.xyz/blog/2026/01/12/chainlink-ccip-cross-chain-interoperability-tradfi-bridge/ · https://coinmarketcap.com/cmc-ai/chainlink/latest-updates/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
