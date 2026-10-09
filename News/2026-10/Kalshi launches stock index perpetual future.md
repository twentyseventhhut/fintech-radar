---
title: "Kalshi launches stock index perpetual future"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - company/kalshi
  - industry/trading
  - industry/capital-markets
  - region/us
  - type/product
sources:
  - https://www.reuters.com/business/kalshi-launches-stock-index-perpetual-future-expand-product-suite-2026-10-06
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s92a044a5
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Kalshi launches stock index perpetual future

> [!info] 2026-10-08 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Kalshi launches a stock index perpetual future to expand its product suite. The new contract adds a stock index perpetual future to the range of products available on the prediction market platform. Reuters reported on October 6 that the launch will broaden Kalshi's offering beyond its existing event contracts.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.reuters.com/business/kalshi-launches-stock-index-perpetual-future-expand-product-suite-2026-10-06>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Kalshi launches stock index perpetual future
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **2026-10-06** Kalshi went live with **US500PERP** — a **cash-settled perpetual future** referencing the **MerQube US Large Cap Index** (the 500 largest US-listed/US-domiciled companies by float-adjusted market cap), settled at **$1 per index point**, with **no expiry/no delivery** and a **daily funding payment** between longs and shorts to keep price anchored to the index. Max leverage displayed on day one was **~15.3x**. Kalshi **self-certified / filed the contract with the CFTC on 2026-08-18**; the CFTC path cleared and the product launched ~7 weeks later (live 10-06). (Reuters; FinanceMagnates/TradingView; Finimize; LeapRate.)

**Why structured exactly this way / what it reveals.** This is the Reuters headline's de-PR core: the vague "expand its product suite" framing hides a **category jump** — from *event contracts* (binary yes/no outcomes) to a **continuous, leveraged, index-linked derivative**. Two structural tells:
1. **It references MerQube's "US Large Cap Index," NOT the S&P 500.** Some secondaries loosely call it "S&P 500 perps," but the actual underlying is a MerQube-built 500-large-cap index — i.e. Kalshi avoids S&P DJI licensing and keeps its own/MerQube IP. This is a deliberate legal/economic choice: it sidesteps the index-licensing toll CME pays S&P and lets Kalshi frame it as a *Kalshi index product*. → why it matters: the moat/economics shift from "we license the benchmark" to "we own distribution of a near-identical benchmark." (analysis)
2. **The "perpetual + 15x leverage + no roll" design is the crypto-exchange playbook ported onto US equities.** Perps are the dominant crypto instrument precisely because retail hates rolling contracts; porting that UX to equity-index exposure is the actual product bet — not a new asset, a new *wrapper* on a 100-year-old asset. The novelty is the structure and the regulatory venue, not the exposure.

## [1] Competitors / peers
- **CME Group / Cboe** — the incumbents for US equity-index futures (E-mini, Micro E-mini S&P 500; Cboe index options). Kalshi is now a *direct* challenger on the instrument, but CME has deep liquidity, portfolio-margining and institutional entrenchment; Kalshi's edge is UX (no roll, fractional $1/point, retail-friendly, 24/7-ish) not depth. Position: **new entrant, UX-differentiated, liquidity-disadvantaged**.
- **Coinbase** — ported perps to US crypto (and pre-IPO perps offshore) in the same regulatory wave; a philosophical peer, not a direct index competitor yet, but the obvious next mover into index perps.
- **Robinhood** — has publicly lobbied the CFTC for **24/7 trading and perpetual derivatives** (comment letter on file) and runs its own prediction-market/event-contract push; the most likely retail competitor to copy US500PERP.
- **Polymarket / Hyperliquid** — Polymarket is offshore/crypto-native and event-focused; Hyperliquid already runs equity-like perps offshore (SpaceX perp flash-crash, Jun-2026). Kalshi's pitch is explicitly "**onshore, CFTC-regulated alternative to offshore perps**."

**Why the lay of the land is this way / second-order.** Kalshi is racing to **plant the first CFTC-blessed equity-index-perp flag** so that when CME/Cboe/Robinhood arrive, Kalshi already owns the "regulated US perps venue" brand. But perps are a **liquidity-network-effect** product: the venue with the deepest order book wins because funding-rate stability and tight spreads compound. A 15x-leverage retail product with thin early liquidity is **flash-crash-prone** (cf. Hyperliquid SPACEX-USDH wiping $1.5m in 30 min, Jun-2026). So first-mover brand value is real but fragile until liquidity is proven. (analysis)

## [2] Company history / fit
Kalshi's 2025–26 arc is a deliberate **"prediction-market leader → next-gen derivatives exchange"** repositioning (CEO Mansour's own words at the May-2026 BTCPERP approval). Dated ladder from the corpus: event contracts → **BTCPERP** (first US crypto perp, CFTC-approved ~2026-05-28/29, [[Coinbase and Kalshi bring perpetual crypto futures to US]]) → **Pro product for HFT** ([[Kalshi launches Pro product for high-frequency traders]]) → institutional margin license ([[Kalshi secures license for institutional margin trading]]) → **US500PERP** (this note). Valuation: $2bn (Jun-2025) → $11bn → $22bn Series F (May-2026) → **~$40bn target in talks** ([[Kalshi in talks to raise at $40 billion valuation]]); ~$2bn+ annualized revenue run-rate ([[Kalshi passes $2 billion annualised revenue, in early IPO talks]]); ~91% US prediction-market share ([[Kalshi holds 91% of US prediction market, BofA data shows]]).

**Why the company acts this way.** Kalshi's prediction-market revenue is ~90% **sports** — a high-beta, seasonally-flattered, regulation-fragile base (12+ state suits). To defend a ~$40bn / ~20x-revenue mark it **must prove it is an "exchange," not a sports casino** ([[Lex Are prediction-market valuations for Kalshi and Polymarket justified]]). Equity-index perps are a textbook move to **diversify away from sports concentration** into a vastly larger, more legitimate TAM (US equity derivatives) and to buttress the exchange-infrastructure narrative underpinning the raise. → The launch is as much a **fundraise/IPO-narrative instrument** as a product.

## [3] Novelty / value-add / traction
**Genuinely new:** first **CFTC-cleared stock-index perpetual future offered to US retail** — the instrument (equity-index perp) previously existed only offshore (crypto venues). That regulatory first is real. **Not new:** the underlying exposure (large-cap US equity beta) is the most commoditized exposure on earth; CME E-minis, SPY, countless ETFs already deliver it. The value-add is **(a) no-roll UX + (b) onshore regulated venue for a leveraged perp**, nothing about the economic exposure itself.

**Traction: zero confirmed.** This is **announced/live Day-1, NOT adopted.** No volume, open-interest, or user numbers exist yet (note says 1 mention, 1 source). Treat all "could enhance liquidity/attract traders" language as PR aspiration.

**Why the value-add is real-or-not, deeper.** (analysis) Who captures the margin? Kalshi earns a **take-rate/funding-spread** on volume. For this to matter it needs **liquidity depth** that rivals CME — unlikely near-term — OR it monetizes **retail leverage demand** that CME/ETFs underserve (no 15x no-roll retail equity perp onshore). The durable question isn't "is index exposure valuable" (no, it's commoditized) but "**can a thin new venue sustain tight funding rates at 15x retail leverage without a liquidation-driven blowup**" — if not, the product is a brand liability, not an asset. The MerQube (not S&P) choice also means Kalshi avoids benchmark-licensing cost but offers a **slightly-off-benchmark** product that sophisticated hedgers may distrust vs the real S&P contract.

## [4] What's next / market sentiment
Expect **copycats** (Robinhood already lobbying for perps; Coinbase the obvious next index-perp issuer) and **more Kalshi perp listings** (sector/single-name indices, other asset classes) to keep feeding the exchange narrative into the ~$40bn round / late-2027–2028 IPO talks. Regulatory backdrop is the swing factor: the CFTC under Chair Selig has been **actively pro-perps** ("onshore, safe, regulated"), but this stance rests on **no-action letters / self-certification + preliminary court wins**, not durable rule or statute — reversible by a future CFTC composition. 15x retail leverage on equities invites **investor-protection scrutiny** (the same critique leveled at crypto perps: 50x leverage, cascade liquidations, ~$19bn wiped in minutes in prior crypto episodes).

**Why the market goes this way / counterintuitive second order.** (analysis) The pro-perps regulatory window is a **political artifact** (Trump-era "crypto capital of the world" push) — so the moat Kalshi is capitalizing is **borrowed, not owned**, and could close with an administration or chair change. Counterintuitively, **success amplifies the risk**: if US500PERP gets real retail volume at 15x, a single sharp equity drawdown could produce a visible retail-liquidation event on a CFTC-regulated venue — exactly the headline that invites the clampdown. Kalshi's index-perp first-mover status is therefore both its best diversification story and its largest new tail risk.

## Freshness / duplicate verdict
**FRESH.** This is a **distinct new product** (US500PERP, equity-index perpetual, live 2026-10-06, CFTC-cleared 2026-10-03), not a reprint. It is **related to but NOT a duplicate of** [[Coinbase and Kalshi bring perpetual crypto futures to US]] (that was *crypto* BTCPERP, May-2026) — different underlying asset class, different contract, five months later. No prior note covers an equity-index perp. Net-new event.

## Sources
- Reuters (primary, 2026-10-06): https://www.reuters.com/business/kalshi-launches-stock-index-perpetual-future-expand-product-suite-2026-10-06
- FinanceMagnates / TradingView (CFTC filing 08-18, approval 10-03, MerQube, 15.3x): https://www.financemagnates.com/fintech/kalshi-takes-perpetual-futures-into-us-equities-after-cftc-approval/
- Finimize (mechanism, $1/point, US500): https://finimize.com/content/kalshi-brings-perpetual-futures-to-a-us-500-stock-index
- LeapRate (CFTC filing detail): https://www.leaprate.com/regulation/kalshi-launches-us500-perpetual-future/
- CryptoBriefing / CoinGape (competitor framing vs CME/Cboe, offshore rivals): https://cryptobriefing.com/kalshi-expands-into-stock-market-derivatives-with-us-500-perpetual/
- Robinhood CFTC comment letter (24/7 trading & perpetual derivatives): https://cdn.robinhood.com/assets/robinhood/legal/Robinhood%20Comment%20Letter%20-%2024_7%20Trading%20and%20Perpetual%20Derivatives.pdf
- Internal: [[Coinbase and Kalshi bring perpetual crypto futures to US]], [[Kalshi passes $2 billion annualised revenue, in early IPO talks]], [[Lex Are prediction-market valuations for Kalshi and Polymarket justified]], [[Kalshi holds 91% of US prediction market, BofA data shows]], [[Kalshi in talks to raise at $40 billion valuation]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team Q&A

1. **Is it really new, or a re-run of the May crypto-perps story?** New. May-2026 was **BTCPERP** (crypto); this is **US500PERP** (equity index), a different asset class and contract, 5 months later. Not a duplicate. *Answered.*
2. **Is the underlying actually the S&P 500?** No — it references the **MerQube US Large Cap Index**, a 500-large-cap index Kalshi brands "US 500." Secondaries loosely say "S&P 500," but that is imprecise; the choice avoids S&P DJI licensing. *Answered.*
3. **Announced or adopted?** Live but **zero traction data** — no volume, OI, or user numbers. Day-1 launch only. Treat all "enhances liquidity" claims as PR. *Answered: announced/live, not proven.*
4. **What is the precise mechanism delta vs a CME E-mini?** No expiry/no roll + daily funding-rate alignment + $1/point + ~15.3x retail leverage, on a CFTC-regulated US venue. The exposure is identical; only the wrapper and venue differ. *Answered.*
5. **What regulatory basis cleared it, and how durable?** Filed 08-18, cleared ~10-03 via the CFTC's pro-perps posture (self-certification / no-action-style framework under Chair Selig). **Not a durable rule or statute** — reversible by future CFTC composition. *Answered: fragile basis.*
6. **Does this diversify Kalshi away from its ~90%-sports revenue concentration?** That is the strategic intent, but **no revenue from it yet** — diversification is aspirational, not realized. *Open on traction.*
7. **Who captures the margin in the stack?** Kalshi earns take-rate/funding-spread on volume; value depends on **liquidity depth** it does not yet have vs CME. Commoditized exposure means margin is thin unless it owns retail-leverage demand CME underserves. *Answered (analysis).*
8. **What is the flash-crash / liquidation tail risk?** High. 15x leverage on a thin new book invites cascade liquidations (cf. Hyperliquid SPACEX perp, $1.5m wiped in 30 min, Jun-2026; prior crypto episodes ~$19bn). A retail-blowup headline on a CFTC venue could trigger clampdown. *Answered.*
9. **Is "15.3x" leverage fixed or a launch-day display?** Reported as the **max leverage shown on launch day**; may vary by margining. *Open on exact ongoing terms.*
10. **Who's silent about what?** No disclosed fee/take-rate, no funding-rate cap mechanics, no liquidation-engine detail, no market-maker arrangements, no day-1 volume. PR anchors to "expand product suite," not economics. *Answered: economics undisclosed.*
11. **Is the launch timed to the ~$40bn fundraise / IPO narrative?** Very plausibly — it directly buttresses the "exchange infrastructure, not sports casino" thesis underpinning the raise ([[Lex Are prediction-market valuations for Kalshi and Polymarket justified]]). *Answered (hypothesis, strong).*
12. **Does the MerQube-vs-S&P choice weaken the product for hedgers?** Possibly — a near-benchmark index may introduce basis/tracking distrust vs the real S&P contract for sophisticated users, while saving Kalshi licensing cost. *Open (analysis).*
13. **Who copies this and how fast?** Robinhood (already lobbying CFTC for perps) and Coinbase are the obvious fast-followers; perps are a liquidity-network-effect product, so Kalshi's first-mover brand is valuable but not defensible on depth. *Answered.*
14. **Is it tradeable for readers?** No — Kalshi is private; read-through only to CME/Cboe (incumbent index-futures), ICE, and the retail-leverage regulatory debate. *Answered.*
15. **Does this change Kalshi's central valuation question?** It reinforces the "exchange" framing but changes nothing until it shows **volume/OI**; the binary regulatory question (sports reclassification + reversible CFTC posture) still dominates the ~20x mark. *Answered.*

Importance: 3/5 — rationale: a genuine **first** (first CFTC-cleared US-retail equity-index perpetual future) and a strategically significant move diversifying Kalshi beyond sports and feeding the ~$40bn exchange-infrastructure narrative — more than a routine listing. But marked down from 4 because there is **zero traction data** (Day-1 launch), the economic exposure is fully commoditized (large-cap beta already available via E-minis/ETFs), the novelty is a UX/venue wrapper rather than new value, and the regulatory basis enabling it is a reversible political posture. Material as a signal, unproven as a business.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-09]] (2026-10-09).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Kalshi operates CFTC-regulated event contracts / retail derivatives — a sub-vertical of "prediction markets" that is converging with retail futures brokerage. Size (volume, not TAM): per Pew Research via its 23-Sep-2026 note, prediction-market volume roughly doubled May→Jul 2026, largely driven by sports; per CCN, prediction markets hit $188bn of volume in Q3 2026, with Kalshi the main driver (sports ~40% of its Q3 volume). Kalshi-specific: per DeFiRate, Kalshi traded ~$66.7bn of contracts over 7-Sep–6-Oct 2026 (~78% of prediction-market volume, +58% vs prior 30 days) and set a 2026 weekly high of $15.27bn with a first $3bn day. **Structure:** concentrating fast — one regulated DCM (Kalshi) now ~three-quarters of volume; the real moat is the CFTC Designated Contract Market license + FCM status (`[[Kalshi secures license for institutional margin trading]]`), a regulatory barrier crypto-native venues (Polymarket) lack onshore. **Why now:** a May-2026 CFTC policy shift — Chairman Michael Selig let DCMs self-certify perpetual futures under §40.2 on one business day's notice (per Dechert/CoinDesk) — opened "perps" to regulated US venues; Kalshi filed the US 500 perp in Aug 2026 and was approved before the 6-Oct launch (per Reuters). Second-order: this is Kalshi explicitly pivoting from "event contracts" to "full-service financial exchange" (CEO Mansour), colliding head-on with Coinbase, Robinhood and the incumbent CME.

**Competitive landscape.** Sector KPIs: notional contract volume, dollars-paid (net), take-rate/fees, and leverage offered. Players & basis of competition: (1) **Coinbase** — launched 24/7 single-stock perps (`[[Coinbase launches 24 7 stock perpetual futures]]`, 23-Mar-2026) and a US500 perp with up to 20x leverage (per Cryptonomist, from 17-Aug-2026); filed with CFTC/SEC for single-stock perps (Sep-2026). (2) **Robinhood** — planning US perpetual futures + weekend equity trading, 10x on BTC/ETH, via CFTC-registered Robinhood Derivatives (per Crowdfund Insider, Sep-2026). (3) **CME** — incumbent futures exchange, now an active antagonist (lawsuit below). (4) **Polymarket** — top prediction-market rival but crypto-native, fully collateralized, no margin/perps onshore. Recent peer moves cluster in a ~6-month window (Mar–Oct 2026), i.e. the whole field is racing into retail perps simultaneously. **Kalshi's position: ahead on regulatory status** (sole dominant CFTC DCM, ~78% share) but a late/parallel entrant on the perp product itself vs Coinbase. Moat = license + liquidity network effect (analysis); it is NOT first-mover on index perps.

**Comps & multiples.** Kalshi is private; no public revenue → EV/Rev, EV/EBITDA, P/E = no data. Round-valuation comps (mark as private post-money, not market cap):
- Kalshi Series F — $22bn post-money on $1bn raised (`[[Kalshi raises $1 billion Series F at $22 billion valuation]]`, May-2026).
- Kalshi current round — ~$1bn raise at ~$40bn valuation, led by Sequoia/Wellington, pre-IPO (per CoinDesk 24-Jun-2026 / Bloomberg), i.e. ~1.8x the May mark in ~5 months.
- Polymarket — $21bn post-money (1789-led, per Bloomberg 31-Aug-2026); earlier $9bn post-money on ICE's $2bn (`[[Polymarket raises $2B from ICE at $9B valuation]]`, Oct-2025).
- Prior parity point: `[[Kalshi and Polymarket eye roughly $20 billion valuations]]` (Mar-2026) — the two were level ~7 months ago; Kalshi has since opened a ~2x gap ($40bn vs $21bn).
Arithmetic/multiples not computable without a revenue figure (none disclosed) → `[UNSOURCED]`. Qualitative: Kalshi's ~2x premium to Polymarket is justified narratively by volume share (~78%) and the regulatory moat, but is a private secondary mark, not a liquid price — treat the re-rating as momentum-driven, not earnings-backed.

**Risk flags.**
1. **Regulatory/legal — the perp classification itself is contested.** CME sued the CFTC (Jun-2026, per Bloomberg/Law360) arguing perpetuals are swaps, not futures, and that Selig's one-day self-certification circumvented Dodd-Frank; the suit explicitly targets the Kalshi BTCPERP approval mechanism. If courts reclassify perps as swaps, the favorable tax/regulatory basis of the US 500 perp — and the §40.2 fast-track Kalshi relied on — could be pulled, directly hitting the newest product line.
2. **Thin, single-commissioner CFTC + state-gambling overhang.** The approval came from Selig as the CFTC's sole confirmed commissioner; CFTC preemption of state gaming regulators is still being litigated (`[[Minnesota becomes first US state to ban prediction markets]]`, `[[Spain blocks prediction markets Polymarket and Kalshi]]`). A hostile future Commission or an adverse preemption ruling could reverse the regulatory tailwind that is the entire bull case.
3. **Commoditization / disintermediation of the perp.** Coinbase (20x US500) and Robinhood are offering the same leveraged index exposure; the contract is not differentiated, so competition compresses to fees and liquidity. Kalshi's event-contract brand doesn't obviously transfer, and a $40bn mark assumes it wins a category where better-capitalized incumbents are already live.

**What this changes (idea-lens).** This is Kalshi explicitly re-labeling itself from prediction market to retail derivatives exchange — the $40bn pre-IPO mark is being underwritten on "exchange infrastructure," not event-contract novelty (analysis). Falsifiable thesis: if US 500 perp volume is immaterial in Kalshi's next disclosed figures OR the CME v. CFTC suit forces a swaps reclassification, the perp pivot is cosmetic and the valuation gap to Polymarket is unjustified; conversely, the trigger to watch is the CME lawsuit ruling and whether sports+perps push Kalshi's share above ~80% into the IPO.

Sources: https://www.reuters.com/business/kalshi-launches-stock-index-perpetual-future-expand-product-suite-2026-10-06 · https://cryptobriefing.com/kalshi-expands-into-stock-market-derivatives-with-us-500-perpetual/ · https://defirate.com/news/kalshi-2026-volume-record-15b-week/ · https://www.ccn.com/news/crypto/prediction-markets-188-billion-cftc-rules/ · https://www.pewresearch.org/short-reads/2026/09/23/prediction-markets-trading-volume-doubled-between-may-and-july-largely-driven-by-sports/ · https://www.coindesk.com/business/2026/06/24/kalshi-targets-a-massive-usd40-billion-valuation-widening-lead-over-rival-polymarket · https://www.bloomberg.com/news/articles/2026-08-31/polymarket-funding-round-led-by-1789-values-firm-at-21-billion · https://www.bloomberg.com/news/articles/2026-06-18/cme-sues-cftc-as-battle-over-perpetual-futures-trading-heats-up · https://www.dechert.com/knowledge/onpoint/2026/6/addendum-to-perpetual-contracts.html · https://www.crowdfundinsider.com/2026/09/314377-robinhood-markets-plans-perpetual-futures-and-weekend-stock-trading-for-us-customers/ · https://en.cryptonomist.ch/2026/07/31/us500-perpetual-futures-coinbase/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
