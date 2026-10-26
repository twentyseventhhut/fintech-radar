---
title: "Allium and FXC find APAC stablecoin B2C payments lead globally"
date: 2026-10-26
retrieved: 2026-10-26
tags:
  - company/allium
  - company/fxc-intelligence
  - industry/stablecoins
  - region/asia
  - type/research-report
sources:
  - https://asianbusinessreview.com/in-focus/apac-stablecoin-use-skews-53x-towards-b2c-payments
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s85e783fd
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Allium and FXC find APAC stablecoin B2C payments lead globally

> [!info] 2026-10-26 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Allium and FXC Intelligencereported stablecoin cross-border B2C payments in Asia-Pacific reached 5.3x traditional currency share, highest globally.

## Первоисточники

### asianbusinessreview.com
<https://asianbusinessreview.com/in-focus/apac-stablecoin-use-skews-53x-towards-b2c-payments>
*354 слов · direct*

APAC stablecoin use skews 5.3x towards B2C payments
 
 Allium and FXC Intelligence found that business transfers held a smaller relative share than conventional currency flows. 
 Asia-Pacific (APAC) recorded the highest relative use of stablecoins for business-to-consumer (B2C) cross-border payments, at 5.3 times the share of equivalent payments made through traditional currencies, according to data from Allium and FXC Intelligence.
Europe, the Middle East and Africa (EMEA) followed at 3.5 times, whilst the Americas recorded 1.4 times.
Consumer-to-consumer (C2C) payments also accounted for a larger share of stablecoin transactions than traditional cross-border payments across all three regions.
The ratio stood at 3.7 times in APAC, 2.9 times in EMEA and 2.5 times in the Americas.
For consumer-to-business (C2B) payments, the ratio was 2.0 times in both APAC and EMEA, compared with 1.9 times in the Americas.
Business-to-business (B2B) payments showed the opposite pattern, accounting for a smaller share of stablecoin transactions than traditional cross-border payments.
The ratio was 0.6 times in APAC and EMEA and 0.8 times in the Americas.
The report estimated that B2B transactions accounted for 46% to 57% of cross-border stablecoin flows across the three regions, compared with approximately 76% to 81% of traditional cross-border payment flows.
At the country level, Taiwan, Turkey and Indonesia were amongst the leading markets for stablecoin payments in 2025.
Three payment routes — Taiwan to Turkey, Taiwan to Indonesia and Turkey to Indonesia — accounted for approximately 13% of all cross-border stablecoin payments.
Mexico, Ukraine and South Korea also ranked amongst the leading markets for outbound stablecoin payments.
The report linked increased adoption in Turkey, Ukraine, Mexico and Indonesia to currency volatility, inflation and restrictions on moving capital.
In Taiwan and South Korea, established cryptocurrency trading markets were identified as possible drivers of adoption.
The findings also showed differences between stablecoin transfers and traditional remittances.
In the Mexico-US payment route, for example, stablecoin transfers primarily moved from Mexico to the US, reversing the usual direction of remittances.
According to the report, this suggests some users may be moving funds into US dollar-denominated stablecoins to save, hold or settle payments rather than using them for conventional remittances.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Allium & FXC Intelligence — APAC leads stablecoin B2C cross-border payments
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
Allium (on-chain data platform) and FXC Intelligence (cross-border payments market-sizer) published a joint report (Oct 2026) measuring stablecoin penetration of cross-border payments by region and use-case. The headline stat — "APAC B2C stablecoin use is 5.3x the equivalent fiat share" — is a **relative ratio, not a volume claim**. It means: in APAC, B2C's share of stablecoin cross-border flow is 5.3x larger than B2C's share of traditional cross-border flow. It does NOT mean stablecoins dominate payments in APAC; the absolute base is tiny.
- Absolute size (the de-PR'd anchor the headline omits): stablecoins moved **~$135B of a $44.3T retail cross-border market in 2025 = 0.31%** (up from 0.2% in 2024). By use-case: C2C 0.95%, B2C 0.89%, B2B just 0.19%. So the "5.3x skew" sits on top of a sub-1% absolute base — impressive growth rate (64% YoY vs 9% for fiat), still a rounding error in dollar terms.
- **Why the ratios are structured this way**: the report explicitly normalizes against fiat use-case mix. Traditional cross-border flow is overwhelmingly B2B (~76-81%); stablecoins invert this (B2B only 46-57% of stablecoin flow). So B2B shows 0.6x (under-indexed) while consumer legs (B2C 5.3x, C2C 3.7x, C2B 2.0x in APAC) over-index. The "5.3x" is as much a statement about how UN-B2B stablecoins are as about APAC being special.
- Methodology (the credibility core): FXC's market-sizing + Allium's Real-World Payments layer (~2.1B txns 2024–2026 YTD across Ethereum, Polygon, Base, Solana, Tron), filtering out exchange deposits/non-payment activity, geotagged. This is a serious de-noising attempt — most "stablecoins did $33T, more than Visa+MC" headlines (Artemis) do NOT strip bots/DeFi/exchange legs; this report's whole value-add is isolating *genuine payment* activity, which is why its number ($135B) is ~250x smaller than the raw $33T figure.
- Country detail: Taiwan, Turkey, Indonesia are top 2025 markets; the three corridors Taiwan↔Turkey, Taiwan↔Indonesia, Turkey↔Indonesia = ~13% of all cross-border stablecoin payments. Mexico→US stablecoin flow *reverses* the normal remittance direction (report reads this as USD-stablecoin *savings/store-of-value*, not remittance).

## [1] Competitors / peers (the data producers, not the payments)
This is a research-report item, so "competitors" = rival on-chain analytics shops racing to be the authoritative stablecoin-payments scorekeeper:
- **Artemis** (with Castle Island / Dragonfly): "Stablecoin Payments From The Ground Up" — the most-cited prior-art; B2B ~$36B annual run-rate, 30x growth since 2023. Artemis is trusted by Visa, Circle, Tether. Its headline numbers run *larger* and looser than FXC/Allium's.
- **Visa Onchain Analytics / Dune**, **BCG** ("Truth Behind the Numbers", Jan 2026), **Alvarez & Marsal** monthly reports — all publishing competing stablecoin-payment sizings.
- Position: FXC+Allium is **catching up on brand but ahead on rigor** — the explicit fiat-normalized ratio framing and aggressive exchange-leg filtering are a differentiator vs Artemis's larger raw totals. **Why the lay of the land is this way (analysis)**: whoever's number the press/regulators quote wins mindshare and lead-gen; the market is fragmenting into "big scary number" shops (Artemis $33T) vs "conservative real-payment" shops (FXC/Allium $135B). Second-order: as stablecoin regulation (GENIUS Act era) tightens, *conservative* methodologies become the policy-grade citation — advantage FXC/Allium.

## [2] Company history / fit
- **FXC Intelligence**: established cross-border payments data/benchmarking firm (used by banks, PSPs, investors for market-sizing). Stablecoins are a natural adjacency to its core fiat cross-border dataset — this report literally bolts stablecoins onto its existing $44.3T market map.
- **Allium**: on-chain data infra for institutions (Visa, Stripe, Grayscale type customers). Its edge is the "Real-World Payments" labeled dataset. **Why they partnered (analysis)**: neither can size the market alone — FXC has the fiat denominator and payments credibility but no chain data; Allium has the chain data but no fiat baseline. The report is a textbook complementary-asset JV. For both, the report is top-of-funnel marketing for paid data products, not a revenue event.
- Related internal corpus thread: dLocal/BVNK, Remitly's stablecoin wallet, JPYC yen-stablecoin — see [1]/[4]; this report is the measurement layer under those product launches.

## [3] Novelty / value-add / traction
- **Really new?** The *partnership/dataset* isn't brand-new (FXC+Allium have run prior drops, e.g. "stablecoins close to cracking 1% of C2C"); this is a **fresh regional/use-case cut** with 2025 full-year data, not a reprint of identical prior figures — hence fresh, not stale.
- **Value-add is real (analysis)**: the genuine contribution is the *fiat-normalized use-case ratio* + hard corridor data (Taiwan/Turkey/Indonesia, Mexico→US reversal). That reframes the central question from "are stablecoins big in payments?" (no — 0.31%) to "*where* and *for whom* are they structurally displacing fiat first?" Answer: consumer-side, emerging-market, high-FX-volatility corridors — NOT the G10 B2B treasury story the industry PR emphasizes.
- **Who captures value (analysis)**: the corridors flagged (Turkey, Ukraine, Mexico, Indonesia = inflation/capital-control economies) show adoption is driven by **dollar access / store-of-value**, not payment UX. Mexico→US reversal confirms "stablecoin = synthetic USD savings." This is a dollarization story wearing a payments costume — the real beneficiary is USD/USDT dominance, not local PSPs.
- Traction caveat: these are *measured flows* (real), but a sub-1% share means the "disruption" narrative is still forward-looking; the honest read is high growth off a tiny base.

## [4] What's next / market sentiment
- Trajectory: C2C (0.95%) and B2C (0.89%) on track to cross **1% of cross-border in 2026**; B2B (0.19%) lags far behind despite being the segment the industry hypes most.
- **Why the market goes this way (analysis)**: consumer corridors lead because the pain (FX volatility, capital controls, remittance cost) is acute and the counterparties are retail/informal — low compliance friction. B2B lags because enterprises need bank-grade compliance, reconciliation, and don't suffer the dollar-access pain. So the industry's B2B-treasury thesis is **structurally behind** the actual consumer-led adoption curve.
- **Counterintuitive second-order effect**: because adoption concentrates in a few volatile-currency corridors, stablecoin cross-border growth is **fragile to local regulation** (a Turkey/Indonesia crackdown could dent a big slice of the 13% corridor cluster) — concentration looks like momentum but is a single-point-of-failure risk.
- Regulatory backdrop: GENIUS Act (US) + MiCA + APAC licensing regimes legitimize issuers; conservative measurement (this report) becomes the policy-citation standard. Sentiment: constructive but the credible shops are actively deflating the "$33T, bigger than Visa" hype.

## Sources
- Asian Business Review: <https://asianbusinessreview.com/in-focus/apac-stablecoin-use-skews-53x-towards-b2c-payments>
- Allium report page: <https://www.allium.so/reports/stablecoins-cross-border-payments-2026>
- Allium blog (methodology): <https://www.allium.so/blog/how-big-is-stablecoins-share-of-cross-border-payments-a-new-fxc-intelligence-allium-report-2/>
- FXC Intelligence press release (C2C ~1%): <https://www.fxcintel.com/research/press-releases/stablecoins-close-to-cracking-1-of-global-c2c-cross-border-payments-fxc-intelligence-and-allium-partnership-data>
- CoinGeek ($135B / $44.3T): <https://coingeek.com/stablecoins-hit-135b-in-non-wholesale-cross-border-payments/>
- Artemis (prior art): <https://reports.artemisanalytics.com/stablecoins/artemis-stablecoin-payments-from-the-ground-up-2025.pdf>
- Internal: [[Remitly launches stablecoin-powered cross-border wallet]], [[dLocal unlocks trapped funds and speeds payouts with BVNK]], [[JPYC secures approval for Japan's first yen-backed stablecoin]], [[dLocal and Damisa partner on APAC cross-border settlement]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is "5.3x" a volume or a ratio?** Answered: a *relative* ratio — B2C's share of stablecoin flow ÷ B2C's share of fiat flow in APAC. Not a volume dominance claim. The absolute stablecoin share of cross-border is 0.31%.

2. **What's the absolute base the headline hides?** Answered: ~$135B stablecoin of $44.3T retail cross-border = 0.31% in 2025 (up from 0.2% in 2024). The "5.3x" sits on a sub-1% base.

3. **Is this a fresh report or a reprint of prior FXC/Allium figures?** Answered: fresh — a new regional/use-case cut on 2025 full-year data. A prior drop ("close to cracking 1% of C2C") exists but is not identical figures. No internal note covers these numbers → fresh.

4. **Why does APAC lead?** Answered (report + analysis): leading markets (Taiwan, Turkey, Indonesia) driven by FX volatility, inflation, capital controls, and established crypto-trading markets (Taiwan, South Korea) — i.e. dollar-access, not payment UX.

5. **Does "5.3x" prove APAC adoption or just that stablecoins are un-B2B?** Open/analysis: largely the latter — fiat cross-border is ~76-81% B2B; stablecoins are only 46-57% B2B, so all consumer legs mechanically over-index. The ratio partly reflects the global use-case inversion, not APAC exceptionalism alone.

6. **How credible is the methodology vs hype numbers?** Answered: strong — Allium's Real-World Payments layer (~2.1B txns, 5 chains), exchange-deposit/non-payment filtering, geotagging. This is why its $135B is ~250x below the raw $33T "bigger than Visa" headlines.

7. **Is the Mexico→US reversal a remittance story?** Answered: no — report reads it as moving funds INTO USD-stablecoins to save/hold, reversing normal US→Mexico remittance direction. A dollarization/savings signal, not payment.

8. **How concentrated is the flow?** Answered: 3 corridors (Taiwan↔Turkey, Taiwan↔Indonesia, Turkey↔Indonesia) = ~13% of all cross-border stablecoin payments → concentration risk.

9. **What does concentration imply for durability?** Analysis: fragile — a single-jurisdiction crackdown (Turkey/Indonesia) could dent a large slice; momentum is single-point-of-failure exposed.

10. **Why is B2B lagging despite industry hype?** Answered: B2B only 0.19% share vs C2C 0.95%/B2C 0.89%. Enterprises need compliance/reconciliation and lack the acute dollar-access pain; consumer corridors have sharper pain + lower friction.

11. **Who actually profits from this report?** Answered: FXC + Allium monetize paid data products; report is top-of-funnel marketing, not a revenue event. Downstream value accrues to USD/USDT dominance, not local PSPs.

12. **Any conflict in the data?** Open: report figures (0.31%, $135B) are internally consistent across FXC/Allium/CoinGeek citations; differ sharply from Artemis's larger totals due to methodology (filtering), not error.

13. **What would change the thesis?** Analysis: B2B crossing ~1% (would validate the enterprise/treasury narrative) or a regulatory shock in a top corridor (would expose concentration fragility).

14. **Is there genuine traction or just measured-but-tiny flow?** Answered: real measured flows, high growth (64% YoY vs 9% fiat), but sub-1% absolute — "disruption" remains forward-looking.

15. **Does this move markets / warrant prominence?** Analysis: it's a credible data point, not an event; useful as the measurement layer under product stories (Remitly, dLocal/BVNK, JPYC), but no new deal/terms. Moderate weight.

Importance: 3/5 — rigorous, well-sourced data drop that usefully reframes stablecoin adoption as consumer/emerging-market-led (not the B2B-treasury hype) and surfaces hard corridor data, but it's a research report on a sub-1% market, not a market-moving event or new deal.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Cross-border stablecoin payments are still a sliver of the total but growing far faster than fiat rails. Per Allium + FXC Intelligence (report dated ~2026-10-20), stablecoins moved ~$135bn of the ~$44.3tn retail cross-border market in 2025 (≈0.31% of volume, up from ~0.2% in 2024), while stablecoin cross-border volume grew ~64% YoY vs ~9% for fiat. Actual stablecoin payment activity (ex-trading/automated transfers) was estimated at ~$390bn in 2025, roughly double 2024 (per Allium/FXC via crypto.news/blindpay). Structure: the broader stablecoin market is highly concentrated at the issuer layer (USDT/USDC dominate; combined ~$260bn cap per IMF, Dec-2025 — see [[IMF top two stablecoins reach combined $260bn market cap]]), but the cross-border payments layer on top is fragmented across orchestrators, on/off-ramps and regional PSPs. "Why now": emerging-market FX stress and capital controls (Turkey, Ukraine, Mexico, Indonesia) plus deep crypto-trading ecosystems (Taiwan, South Korea) are the stated adoption drivers, not enterprise B2B efficiency — a demand-side, not infrastructure-side, pull (analysis).

**Competitive landscape.** This is a research-report, not a company move — "players" here are the data vendors (Allium = on-chain data; FXC Intelligence = cross-border payments pricing/benchmarking) and the companies whose rails the flows run on. Sector KPIs that matter: payment vs total on-chain volume split, segment penetration (B2C/C2C/C2B/B2B share vs fiat), and corridor concentration. The report's own finding is the key datapoint: APAC B2C skews 5.3x the fiat share (highest globally), EMEA 3.5x, Americas 1.4x; C2C 3.7x/2.9x/2.5x; B2B *under*-indexes at 0.6x in APAC/EMEA, 0.8x Americas. Allium/FXC position: Allium is the incumbent reference for on-chain stablecoin supply/flow data (its $303bn Aug-2026 supply print is widely cited); pairing with FXC's fiat-corridor pricing data is what makes the B2C/B2B relative-share framing possible — a methodological moat (combining two otherwise-separate datasets) rather than a payments moat (analysis). Recent related moves in base: Visa stablecoin settlement at ~$4.5bn annualized run-rate (2026-02), dLocal anchoring APAC in Singapore (2026-06), HitPay/Triple-A stablecoin merchant payments in SEA (2025-10).

**Comps & multiples.** No valuation/round/revenue in this news — it is a free research report from two data vendors, so trading multiples are **not applicable / no data**. Internal comps (data points, not deals): [[OpenFX report stablecoins still just 1% of global payment flows]] (2026-03) corroborates the "<1% of flows" framing from an independent vendor; [[Stablecoin volumes grew 91% to $10.9 trillion last year]] (2026-05) shows why total on-chain volume (~$10.9tn) massively overstates genuine payment activity (~$390bn), i.e. the same trading-vs-payment distinction Allium/FXC make; [[IMF top two stablecoins reach combined $260bn market cap]] (2025-12) anchors the supply side. Distribution not computed (no comparable valuation figures) — qualitative comparison only. Cross-vendor numbers roughly reconcile (sub-1% penetration, ~60–90% YoY growth), which is a sanity-check positive.

**Risk flags.**
1. Measurement/definitional fragility — headline ratios depend entirely on how "payment" is isolated from trading, treasury and automated transfers. Different vendors already quote wildly different denominators ($135bn vs $390bn vs $10.9tn), so the 5.3x figure is a ratio of two noisy estimates; second-order: policy and investment narratives built on it inherit that fragility.
2. Driver = currency distress, not product-market fit — APAC/EMEA B2C lead is concentrated in high-inflation/capital-control corridors (Turkey, Indonesia, Ukraine). If local FX stabilizes or regulators clamp capital flight, the B2C skew could reverse faster than durable B2B adoption would (disintermediation of the very use case driving the "lead").
3. B2B under-indexing (0.6x) undercuts the bull case — the segment carrying ~76–81% of fiat cross-border value is where stablecoins are *weakest*, so headline "APAC leads globally" masks that the economically largest flow pool is barely penetrated; enterprise fraud liability, reversibility and compliance remain unresolved (de-PR'd gap the report is quiet on).

**What this changes (idea-lens).** The report reframes stablecoin cross-border adoption as consumer-led in stressed-FX corridors rather than enterprise-led efficiency — a bottoms-up adoption curve (analysis). Falsifiable thesis: if the next Allium/FXC update shows B2B rising toward ~1x fiat share (from 0.6x) without a corresponding fall in the B2C skew, stablecoins are broadening into a genuine rail; if instead the B2C skew decays as EM currencies stabilize, the "APAC leads" story was cyclical FX arbitrage, not structural. Trigger to watch: regulatory clarity (US GENIUS-style / HK / Singapore frameworks) that would pull regulated B2B volume on-chain.

Sources: https://www.allium.so/reports/stablecoins-cross-border-payments-2026 · https://www.allium.so/blog/how-big-is-stablecoins-share-of-cross-border-payments-a-new-fxc-intelligence-allium-report-2/ · https://crypto.news/stablecoins-move-billions-across-borders-how-much-is-payment-activity/ · https://blindpay.com/resources/more/stablecoin-payments-statistics-2026 · https://www.fxcintel.com/research
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
