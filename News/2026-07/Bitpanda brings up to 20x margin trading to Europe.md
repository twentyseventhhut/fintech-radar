---
title: "Bitpanda brings up to 20x margin trading to Europe"
date: 2026-07-09
retrieved: 2026-07-09
tags:
  - company/bitpanda
  - industry/trading
  - industry/crypto
  - region/europe
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/29f04000
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s0e26e659
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Bitpanda brings up to 20x margin trading to Europe

> [!info] 2026-07-09 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Bitpanda brings Margin Trading with up to 20x to Europe. Customers can now buy on margin and take leveraged positions of up to 20x on Stocks & ETFs, increasing their market exposure beyond their initial capital. This means that customers can open larger positions and react more dynamically to market opportunities, all within the Bitpanda app.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/29f04000>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Bitpanda brings up to 20x margin trading to Europe
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 8 July 2026 Bitpanda enabled **margin trading with up to 20x leverage on REAL stocks, ETFs and ETCs** (875+ securities) inside its app — pitched as "a first for Europe" for leveraged trading on actual underlying securities (not CFDs). Long-only leverage on securities the customer genuinely owns/borrows against.
- **The load-bearing mechanic (why this is even legal):** this is **classic securities margin lending**, NOT a CFD. ESMA's 2018 product-intervention leverage caps (30:1 FX down to **5:1 for single stocks**, 2:1 crypto) apply *only to CFDs* under Art. 40 MiFIR. Real-asset margin loans sit outside that regime → 20x becomes permissible. This is the entire novelty: a regulatory-arbitrage framing more than a product breakthrough. (analysis)
- **Funding structure:** per external reporting, the borrowed leg is funded in Bitpanda's euro stablecoin **EURCV** — customer posts capital, borrows EURCV to fund the levered position. (single-source; treat as reported, not confirmed by primary.)
- **Gating:** requires passing a MiFID/MiFIR **appropriateness test**; Bitpanda flags it as "experienced customers only." So "brings 20x *to Europe*" ≠ "20x for every retail user" — max leverage is liquidity- and eligibility-gated.
- **Economics (de-PR'd):** promo "zero buy fees" only until end-2026 (normally €1), €1 sell fee, **daily degressive funding fee ~0.18% accruing every 4h**, and a **1% liquidation fee**. At 20x a ~5% adverse move wipes the entire stake. The revenue model is funding-fee + liquidation-fee carry on borrowed balances — classic margin-lending net-interest income, dressed as a trading feature.
- **Why framed this way:** Bitpanda is pre-IPO and needs a *software/brokerage* growth story, not a "crypto-only" label. A high-engagement, high-margin lending product on equities directly supports the "universal exchange" narrative ahead of the Frankfurt listing. (analysis)

## [1] Competitors / peers
- **CFD brokers (eToro, Plus500, IG):** capped at **5:1 on single-stock CFDs / 2:1 crypto** for retail under ESMA. eToro's leverage is CFD-based (2x headline). Bitpanda's real-securities-margin route structurally beats these caps — a genuine differentiator *if* the "real asset" claim holds. See [[Bitpanda gears up for Frankfurt IPO in H1 2026]] (stocks/ETFs "universal exchange" push).
- **Crypto-native margin (Kraken up to 10x, Binance ~10x, Coinbase ~3x derivatives):** these are crypto/derivatives leverage, not real-equity margin. Kraken has moved the other way — **tokenized equities as collateral** for crypto derivatives — a different structure (tokenized wrapper vs real share). 
- **Traditional prime/retail brokers (IBKR, Trade Republic, Scalable):** offer securities margin but typically at low multiples (~2–4x Reg-T-style / conservative EU haircuts). Bitpanda's **20x on equities is aggressive** vs incumbents. → The real question isn't "is 20x legal" but **"who bears the gap-risk / negative-balance risk at 20x on a single stock that can gap 10–20% overnight"** — CFD rules mandate negative-balance protection; securities margin outside that regime may not. Silent in PR. (analysis)

## [2] Company history / fit
Bitpanda (Vienna, 2014) has been aggressively de-risking from crypto-only ahead of an IPO: €4.1bn Series C valuation (2021); 2025 adjusted revenue **€371m (+16%)** but adjusted EBITDA **~€13m, down ~75%** on pre-IPO spend ([[Bitpanda 2025 revenue rises 16% to €371 million]]); user base 5.9m→7.4m (+25%). It added 10,000 stocks/ETFs and a €1-flat-fee "universal exchange" in Jan 2026 ([[Bitpanda gears up for Frankfurt IPO in H1 2026]]), targeting a **€4–5bn Frankfurt IPO in H1 2026**. Margin trading is the monetization layer bolted onto that new equities inventory — turns flat-fee, low-margin equity volume into interest-bearing balances. Fits the structural pressure: a commodity brokerage take-rate needs a higher-margin line to justify a software multiple at IPO. (analysis)

## [3] Novelty / value-add / traction
- **Genuinely new (narrow):** first mainstream EU retail app to offer high (20x) leverage on *real* stocks/ETFs by routing around CFD caps via securities margin. That legal/structural framing is the value-add.
- **Not new (broad):** leverage on equities is ancient (prime brokers, CFDs); the innovation is packaging + the ESMA-arbitrage, not a new financial primitive.
- **Traction = zero (announcement only).** No user counts, no volumes, no borrowed-balance figures. "Launched/live" but adoption unproven. Promo fee waivers signal Bitpanda is *buying* early volume.
- **Who captures the margin:** Bitpanda, via funding fees (0.18%/day ≈ high double-digit annualized) + 1% liquidation fees. This is a **high-margin net-interest / carry business** — the real prize and the real reason to launch pre-IPO. But it's also the reputational/regulatory tail-risk: retail wipeouts at 20x invite scrutiny. (analysis)

## [4] What's next / market sentiment
- **Regulatory tail-risk is the central issue.** ESMA/national regulators (BaFin, FMA) have historically clamped down when retail leverage products cause losses (that's why CFD caps exist). A "real securities margin" product marketed to retail at 20x is a plausible next target for intervention or MiCA/MiFID-review scrutiny. If regulators reclassify or extend appropriateness/leverage rules, the headline feature could be capped. (hypothesis)
- **IPO timing:** launching a high-margin lending product weeks before a €4–5bn Frankfurt listing is not coincidental — it props the growth/margin narrative. Second-order: it also raises the litigation/complaint surface right when Bitpanda wants a clean story.
- **Sentiment:** trade press covered it as a genuine "first," but with heavy risk caveats (5% move = liquidation). No independent adoption data yet.

**FRESHNESS VERDICT: FRESH.** No prior note covers this launch. Closest priors are the equities/"universal exchange" push ([[Bitpanda gears up for Frankfurt IPO in H1 2026]]) and 2025 results ([[Bitpanda 2025 revenue rises 16% to €371 million]]) — related context, not the same event. This is a distinct new product (8 Jul 2026).

## Sources
- https://www.connectingthedotsinfin.tech/r/29f04000 (primary digest link)
- https://blog.bitpanda.com/en/bitpanda-brings-margin-trading-real-stocks-europe
- https://cryptoticker.io/en/bitpanda-margin-trading-real-stocks-etfs-20x-launch/
- https://www.tradingview.com/news/financemagnates:a2e575ffc094b:0-bitpanda-brings-leveraged-stock-and-etf-trading-to-european-retail-traders/
- https://fxnewsgroup.com/forex-news/cryptocurrency/bitpanda-launches-20x-leveraged-stocks-and-etfs-trading-in-europe/
- https://www.esma.europa.eu/press-news/esma-news/esma-adopts-final-product-intervention-measures-cfds-and-binary-options
- https://www.financemagnates.com/forex/bitpanda-sheds-crypto-only-label-with-5-billion-frankfurt-ipo-push/
- https://www.theblock.co/post/393233/bitpanda-reports-430-million-adjusted-revenue-in-2025-as-user-base-grows-25
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is "20x on real stocks" genuinely CFD-cap-exempt, or will regulators disagree?** ESMA caps apply to CFDs (Art. 40 MiFIR); securities margin sits outside. But does a synthetic/EURCV-funded position on 875 tickers still count as a "real asset" margin loan, or could BaFin/FMA/ESMA reclassify it? — **Open / core risk.**
2. **Who actually gets 20x?** PR says up to 20x, gated by appropriateness test + asset liquidity. What % of users qualify for the headline number, and what's the typical/default cap? — **Open (not disclosed).**
3. **Is there negative-balance protection?** CFD rules mandate it; securities margin outside the CFD regime may not. Can a retail user at 20x end up owing more than deposited on an overnight gap? — **Open — the single most important unanswered consumer-protection question.**
4. **What is the true funding cost annualized?** 0.18%/day degressive ≈ tens of % APR. Is this a "trading feature" or a high-rate consumer margin loan in disguise? — **Answer: high-margin net-interest business (analysis).**
5. **Is the EURCV-funded borrow leg confirmed?** Only single external sources assert it; primary (Bitpanda blog) not verified in-context. — **Open / single-source.**
6. **Traction?** Any volumes, borrowed balances, active margin accounts? — **None disclosed; announcement-only.**
7. **How does this compare on risk to eToro/Kraken/Coinbase?** Those are 2–10x on CFDs/crypto; is 20x on single equities materially riskier for retail? — **Yes (5% move = wipeout).**
8. **Why launch now, weeks before the Frankfurt IPO?** Growth/margin-narrative timing vs product readiness. — **IPO-narrative-driven (analysis).**
9. **What's the durable revenue share?** Is margin-lending carry recurring, or promo-inflated (fee waivers to end-2026)? — **Promo-boosted early volume; durability unproven.**
10. **Liquidation mechanics:** 1% liquidation fee + 4-hourly funding accrual — how punitive vs peers, and does it create a conflict (Bitpanda profits from liquidations)? — **Potential conflict of interest; open.**
11. **Short-selling?** Is it long-only leverage or two-sided? PR implies leveraged long exposure; shorts unclear. — **Open.**
12. **What breaks the story?** A regulatory intervention extending leverage caps to real-securities retail margin, or a wave of retail losses/complaints during the IPO window. — **Primary downside trigger.**
13. **Does "first in Europe" survive scrutiny?** Prime brokers and some EU brokers already offer securities margin — is 20x-to-retail-in-an-app the actual first, or just marketing? — **Likely first at this leverage/retail-app combo; "first" claim narrow (analysis).**
14. **Cross-collateral/portfolio risk:** can crypto/tokenized assets collateralize equity margin (Kraken-style)? — **Not indicated; open.**
15. **Second-order for the IPO:** does a leverage product raise Bitpanda's regulatory/complaint surface exactly when it wants a clean listing story? — **Yes — counterintuitively fragile, not accretive (hypothesis).**

**Importance: 3/5** — A structurally clever, genuinely first-of-kind EU retail product (20x on real securities via CFD-cap arbitrage) from a soon-to-IPO name, which makes it noteworthy. But: announcement-only (zero traction), the "novelty" is regulatory framing rather than a new primitive, high regulatory tail-risk, and it's fundamentally a high-margin margin-lending line dressed as a feature. Not a 4 (no adoption, single-region, real chance of regulatory pushback); clearly above 2 (real structural differentiation + IPO relevance).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-09]] (2026-07-09).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**IR-primary (Bitpanda reported figures).** 2025 adjusted revenue **€371m (~$430m), +16% YoY** (per Bitpanda FY-results / [[Bitpanda 2025 revenue rises 16% to €371 million]]); **7.4m registered users, +25%** (web, as of 2026). Last priced round: Series C Aug-2021, **$263m at ~$4.1bn** post-money (Valar Ventures; fintechfutures). IPO in prep — Frankfurt listing targeted H1-2026 at **€4–5bn (up to ~$5.5bn) valuation**, banks Goldman/Citi/Deutsche Bank ([[Bitpanda gears up for Frankfurt IPO in H1 2026]]; Bloomberg via Cointelegraph). IR materials on file (ir_latest.json) are product/PR only (Bitpanda Enterprise, Vision, Fusion) — no fresh P&L/margin disclosure; revenue/user figures above are the primary quantitative anchors.

**Sector & drivers.** European retail brokerage/crypto-broker vertical, now pushing into leveraged securities. The move's core is a **regulatory-arbitrage design**: Bitpanda offers up to 20x on **real stocks/ETFs/ETCs (875+ securities)** as *classic securities margin*, not CFDs — so ESMA's product-intervention CFD leverage caps (major FX 30:1 down to crypto 2:1, and the retail equity-CFD cap ~5:1) do not bite (per ESMA product-intervention measures; cryptoticker/FXNewsGroup, 2026-07-08). Economics: **zero buy fee, €1 sell fee, 0.18%/day degressive financing fee, 1% liquidation fee** — i.e. the revenue engine is net-interest/financing on the margin loan plus liquidation fees, not commission `(analysis)`. Why now: crypto trading revenue is cyclical; leverage on equities widens the fee base and deepens engagement pre-IPO, when Bitpanda is explicitly de-labelling from "crypto-only" toward a broad broker (financemagnates).

**Competitive landscape.** Sector KPIs: financing spread / net interest on margin book, ARPU, funded accounts, and (for the leverage product) liquidation-loss rate. Players: **eToro** (public, ETOR), **Robinhood** (US, ~$2.95bn 2024 rev, +58%; Gold/margin ~30% of income; largely absent from EU retail), **Trading 212** ([[Trading 212 offers automatic tax withholding in Germany]]), plus crypto-natives **Kraken** and **Coinbase**. Basis of competition: product breadth + fee/leverage terms + EU regulatory positioning. Recent move: [[Upvest partners with Boerse Stuttgart to bring securitised derivatives trading to financial]] (2026-01) — infra rails for EU leveraged/derivative products. Bitpanda's position: **first-mover in Europe on true leveraged stocks/ETFs** (analysis — a genuine white space vs CFD-capped peers), moat = MiCA/MiFID licensing + broker breadth + pre-IPO scale (7.4m users). Niche today, but the interest-margin economics scale with the book.

**Comps & multiples.** Private/pre-IPO, so revenue multiples only, both numbers publicly verifiable:
- **Bitpanda** — IPO target ~€4.5bn (mid) / €371m 2025 rev → **EV/Rev ≈ 4.5bn/0.371bn ≈ 12x** on last-year revenue (rich, but pre-IPO ask, not a market print). Last round $4.1bn (2021).
- **Kraken** — [[Kraken raises $800m at $20bn valuation]] (2026-01); ~$1.8bn 2025 rev (web) → **≈ 20/1.8 ≈ 11x**.
- **Coinbase (COIN, public)** — slow-growth (~9% 2025 rev, per Motley Fool) vs Robinhood ~52%; internal read: Bitpanda's ~12x on 16% growth is in-line-to-rich vs the private crypto-broker cluster (~11x Kraken), not obviously mispriced given growth `(analysis)`.
- Median not computed (<3 clean, same-model verifiable EV/EBITDA pairs) → qualitative comparison. Clean EV/EBITDA, forward/NTM → `[UNSOURCED]`.

**Risk flags.**
1. **Regulatory reclassification risk (primary).** The whole 20x hinges on ESMA/national regulators accepting this as securities margin rather than de-facto CFD-equivalent leverage; a product-intervention or MiFID reinterpretation could force it to the ~5x CFD cap, gutting the differentiator — and the timing is awkward directly ahead of a Frankfurt IPO/prospectus.
2. **Retail-harm / liquidation risk.** At 20x a 5% adverse move wipes the stake; equities have fixed hours → overnight/weekend gap risk opens positions already underwater. Concentrated liquidation losses or a mis-selling narrative would draw supervisory and reputational scrutiny pre-listing.
3. **Cyclicality + single-market concentration.** Revenue still crypto-cycle-sensitive; the leverage push is EU-retail-concentrated. Financing-fee income depends on sustained margin balances, which shrink fast in a drawdown — pro-cyclical, not diversifying.

**What this changes (idea-lens).** A genuine new EU product category — leveraged *cash* equities via securities-margin, sidestepping the CFD cap — that peers (eToro, Trading 212) can copy fast if regulators tolerate it `(analysis)`. Falsifiable thesis: if ESMA/BaFin stays silent, expect 2–3 EU brokers to launch equivalent leveraged-stock margin within ~2 quarters; **trigger/what breaks it** = any ESMA statement, national warning, or IPO-prospectus risk-disclosure treating it as CFD-equivalent → cap snaps to ~5x and the first-mover edge evaporates.

Sources: https://blog.bitpanda.com/en/bitpanda-brings-margin-trading-real-stocks-europe · https://fxnewsgroup.com/forex-news/cryptocurrency/bitpanda-launches-20x-leveraged-stocks-and-etfs-trading-in-europe/ · https://www.esma.europa.eu/press-news/esma-news/esma-adopts-final-product-intervention-measures-cfds-and-binary-options · https://www.fintechfutures.com/venture-capital-funding/bitpanda-valued-at-4-1bn-after-263m-series-c-raise · https://cointelegraph.com/news/bitpanda-frankfurt-ipo-5-5b-valuation-report · https://www.businessofapps.com/data/robinhood-statistics/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** CONTEXT-ONLY — no earnings in this news; it is a product launch (up to 20x margin trading on real stocks/ETFs). Grounded in Bitpanda's most recent disclosed print (FY2025, private/pre-IPO). FY2025 read: revenue up but profitability sharply down — €371m adjusted revenue (+16% YoY) but adjusted EBITDA €13m (-75% YoY, from €52m in 2024), a self-described "pre-IPO spending push." This margin product is a leverage-monetization / revenue-diversification lever into a compressing-margin, pre-IPO year.

**Key figures (Bitpanda's own disclosed FY results, private company).**
- FY2025 adjusted revenue: €371m (≈$430m), +16% YoY.
- FY2025 adjusted EBITDA: €13m, down from €52m in FY2024 → -75% YoY; EBITDA margin collapsed from ~30% (2024) to ~3.5% (2025) (analysis).
- FY2024 (prior record year): revenue €393m, ≈+100% YoY (roughly doubled); adjusted EBITDA €52m, EBITDA margin >30%; 2024 was the "record profitability" year Bitpanda touted.
- Registered users: 7.4m end-2025, +25% YoY (from 5.9m in 2024).
- B2B institutional partners: grew from 9 to 16 European financial institutions during 2025.
- Note: FY2024 revenue was cited both as €393m and ≈$426m (+162%) across outlets; the €393m / doubling figure is the company's own disclosure.

**By segment / driver.** Revenue growth (+16%) driven by the multi-asset expansion — a unified investing platform (crypto + stocks + ETFs + precious metals, launched 29 Jan 2026), Bitpanda Enterprise/Technology Solutions B2B (partner count 9→16, incl. IG Europe, Lulu Financial, Deutsche Bank fiat rails), and prior crypto-margin trading (>100 cryptos). The EBITDA drop was deliberate: heavier spend on product development, marketing, licensing (MiCA) and international/regulatory expansion ahead of a targeted 2026 Frankfurt IPO — i.e. margin compression is investment-led, not demand-led.

**vs expectations / prior period.** No public sell-side consensus for a private company [UNSOURCED]. vs prior period: revenue decelerated hard — from ~doubling in FY2024 to +16% in FY2025 — while EBITDA fell -75%. So the FY2025 print is a growth-vs-profitability trade-off: top line still growing, bottom line intentionally sacrificed. This 20x margin launch reads as an attempt to re-accelerate high-take-rate trading revenue (margin/leverage fees) to support both the growth and, eventually, the profitability narrative into the IPO.

**Guidance / forward.** No formal guidance (private). Forward frame: targeting a Frankfurt Stock Exchange debut in H1 2026 at a €4–5bn valuation (vs ~$4.1bn in its 2021 raise). Plausibility flag: EBITDA down -75% into an IPO window is a demanding setup — the equity story leans on the multi-asset platform and revenue re-acceleration rather than current profitability.

**Thesis-flags.**
1. Margin/leverage as a margin-recovery lever — this 20x product (zero buy fee, €1 sell fee, 0.18% daily degressive fee, 1% liquidation fee) monetizes trading intensity; fact→ it adds high-take-rate revenue → why it matters: FY2025 EBITDA was only €13m, so incremental high-margin trading fees are exactly what the pre-IPO P&L needs → second-order: also raises retail-risk/liquidation exposure and regulatory attention (ESMA CFD leverage caps don't bind because these are real securities on margin, not CFDs — a genuine structural edge but a novel one).
2. Profitability compression is the key watch-item, not revenue — de-PR: Bitpanda leads with revenue growth and user count, quieter on the -75% EBITDA collapse; sustainability of the +16% top line matters less than whether spend normalizes post-IPO.
3. B2B/institutional (9→16 partners) is a second growth engine diversifying away from retail crypto cyclicality — reduces single-market beta but is lower-take-rate than retail leverage trading.

Sources: https://www.theblock.co/post/393233/bitpanda-reports-430-million-adjusted-revenue-in-2025-as-user-base-grows-25 · https://www.financemagnates.com/cryptocurrency/bitpandas-profit-falls-75-firm-blames-pre-ipo-spending-push/ · https://www.trendingtopics.eu/bitpanda-2025-revenue-grew-16-but-ebitda-has-fallen-75-ahead-of-expected-2026-ipo/ · https://ffnews.com/newsarticle/cryptocurrency/bitpanda-2024-financial-results/ · https://www.theinternational.at/bitpanda-doubles-revenue-in-2024-hits-e393m/ · https://blog.bitpanda.com/en/bitpanda-brings-margin-trading-real-stocks-europe · consensus/guidance: no public consensus for private co [UNSOURCED]. Bitpanda IR annual-review file listed in ir_latest.json but absent on local disk → FY figures taken from web disclosures of the company's own results.
<!-- /enrichment:earnings_review -->
