---
title: "Trade Republic launches best price execution engine and Direct Price"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/trade-republic
  - industry/trading
  - region/europe
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/a7a9b2ed
  - https://www.futureofbanking.info/r/c73c9ea7
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Future of Banking"
story_id: s7d24c936
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# Trade Republic launches best price execution engine and Direct Price

> [!info] 2026-07-03 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Future of Banking

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇩🇪 Trade Republic launched a new best price execution engine and introduced Direct Price, a paid order type that lets investors choose specific exchanges such as Xetra, Euronext, NYSE, and Nasdaq. The overhaul follows the EU’s ban on payment for order flow and also includes the launch of the company’s first browser-based trading terminal.

[Future of Banking] 🇩🇪 Trade Republic launched a new best price execution engine and introduced Direct Price, a paid order type that lets investors choose specific exchanges such as Xetra, Euronext, NYSE, and Nasdaq. The overhaul follows the EU’s ban on payment for order flow and also includes the launch of the company’s first browser-based trading terminal.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/a7a9b2ed>
- <https://www.futureofbanking.info/r/c73c9ea7>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Trade Republic launches best price execution engine and Direct Price
_Analytical notes (not a post). Importance: 4/5._

**FRESHNESS/DUPLICATE VERDICT: FRESH.** This is a genuinely new product event (announced 2026-07-02, note 2026-07-03). No prior corpus note covers the Best Price engine / Direct Price / Web Terminal. Prior Trade Republic notes cover funding ([[Trade Republic raises EUR1.2B secondary at EUR12.5B valuation]], [[Trade Republic confirms €12.5bn valuation in secondary]], [[Trade Republic nears €12 billion valuation]]), wealth/product expansion ([[Trade Republic expands into wealth management with Apollo and EQT]], [[Trade Republic launches bond ETFs after €2.5 billion interest]]), marketing ([[Trade Republic names Brad Pitt brand ambassador]]) and regulation ([[Italy fines Trade Republic €2.5 million for misleading ads]]) — none overlap this launch. The corpus does NOT contain the Jan-2026 BaFin MTF-license note (the direct precursor), so this event is fresh even against the company's own recent moves.

## [0] What exactly happened (de-PR'd)
On 2026-07-02 Trade Republic shipped a rebuilt execution stack, timed exactly to the EU PFOF ban:
- **Best Price execution engine** — an *aggregated orderbook* that unifies prices across "all relevant liquid exchanges" and routes each order (any size) to the best bid/ask. Marketed as **free** ("no extra cost"). This is smart-order-routing (SOR) — standard institutional plumbing — now defaulted for retail.
- **Direct Price** — a **paid order type: €2 per trade, flat regardless of size**, that lets the customer *pick a specific venue* from ~30 global exchanges (Xetra, Euronext, NYSE, Nasdaq…) for market/limit/stop orders. Note: the aggregated note said "such as Xetra, Euronext, NYSE, Nasdaq"; the press release specifies **30 exchanges**.
- **Web Terminal** — first browser-based terminal (advanced charting, screeners, live market data), **free**.
- **Transparency layer** — in-app real-time aggregated orderbook vs individual-venue orderbooks, free.

**Why structured this way (the red-team core):** PFOF is banned EU-wide from ~30 June 2026 (Art. 39a of MiFIR Reg (EU) 2024/791). PFOF was Trade Republic's model for "€1 / near-free trades" — market makers rebated ~1-3€/order. TR itself says PFOF is **<30% of revenue** (down from ~a third in 2023). So this launch is a **regulatory-forced re-architecture dressed as a customer-benefit upgrade**: the "free Best Price" replaces the rebate economics with (a) still-€1 base commission, (b) a NEW €2 Direct-Price upsell, and (c) — critically — its **own MTF** (BaFin license to a TR subsidiary, 23 Jan 2026) where it can internalise flow/act as market maker and monetise spread instead of PFOF. The PR anchors on "transparency / best execution for retail" precisely because the honest frame ("we lost our rebate revenue and are rebuilding monetization") is unflattering.

## [1] Competitors / peers
- **Scalable Capital** — furthest ahead structurally: launched **EIX (European Investor Exchange)** with Hannover Stock Exchange on **10 Dec 2024**, operating as a market maker earning the spread; already runs a **subscription** (€2.99/mo tier) that can absorb the PFOF loss without raising per-trade cost. Scalable restructured for post-PFOF in 2024 — ~18 months before TR's public product.
- **Trade Republic** — catching up on the venue/MTF piece (license Jan 2026, product Jul 2026), but its Best-Price/SOR + free Web Terminal + transparency UX is arguably a **stronger consumer proposition** than a bare exchange.
- **Robinhood EU / eToro** — no directly comparable PFOF-ban response surfaced; PFOF is effectively a **German-specific story** (France, NL, Sweden, Italy, Spain already banned/never adopted it), so non-German-flow neobrokers are less exposed.

**Why the landscape looks this way (second-order):** the ban converts a *rebate* business into a *venue/spread + subscription/upsell* business. Whoever owns an execution venue captures the internalisation margin PFOF used to pay out. Scalable chose "own an exchange"; TR chose "own an MTF + SOR + paid venue-choice." The multiple question shifts from "how cheap are trades" to **"who controls the venue where retail flow clears."**

## [2] Company history / fit
Trajectory: 10M+ customers, 18 markets, €150B+ AuM (2025-2026); €12.5B valuation secondary (Dec 2025 / Jan 2026, Thiel/Wellington/GIC/Fidelity); expansion beyond brokerage into wealth (Apollo/EQT private markets, Sep 2025), bond ETFs (Oct 2025), child savings (Oct 2025), interest-on-cash. **Fit: strong and structural.** TR has spent 18 months diversifying revenue *away* from transactional PFOF toward AuM/interest/wealth — this launch closes the last gap (execution/venue) with the same logic: replace a commodity, regulation-exposed rebate line with owned infrastructure it controls.

**Why (structural pressure):** a neobroker on €1/PFOF trades has a fragile, regulation-dependent take-rate. To justify a €12.5B (software-like) valuation post-PFOF, TR must convert transactional revenue into durable, owned-margin revenue (venue spread, subscription-adjacent upsells, interest, wealth fees). Hence the vertical integration into an MTF + paid order types.

## [3] Novelty / value-add / traction
- **Genuinely new for TR / European retail-at-this-scale:** free aggregated-SOR best execution + free advanced Web Terminal + in-app orderbook transparency. SOR itself is not new (institutional standard; brokers like IBKR have long done multi-venue routing) — the novelty is **offering it free to 10M+ mass-retail customers with a transparency UI**, and the €2-flat "choose your venue" order type.
- **Traction: NONE yet — this is a launch, not adoption.** No numbers on Direct-Price uptake, Web Terminal usage, or MTF internalisation volume. Zero data on how much of the lost PFOF revenue the €2 upsell + MTF spread actually recovers.

**Why the value-add is real / where it breaks (deeper):** For the *customer*, best execution + transparency is a real, verifiable upgrade over opaque single-venue PFOF routing. For TR's *unit economics*, the value-add depends entirely on the unproven part: can MTF internalisation + €2 upsells replace <30%-of-revenue PFOF at similar margin? If "Best Price is free," TR must monetise via (a) internalising flow on its own MTF (capturing spread that used to go to Citadel-style market makers — TR moves UP the stack from PFOF-recipient to venue-operator), and (b) Direct-Price €2. The margin-capture question: **does TR now become the market maker (best case, higher owned margin) or just eat the PFOF revenue loss (worst case)?** That is the whole story and it is unanswered.

## [4] What's next / market sentiment
- Watch: Direct-Price attach rate, MTF internalisation volume, whether TR raises the €1 base or adds a subscription (Scalable-style) later, and H2-2026 revenue disclosure showing PFOF replacement.
- Regulatory backdrop: ban live from ~30 Jun 2026; Germany's temporary exemption expired at the deadline. Investor-facing framing (regulators, press) is "good for investors — more transparency, better prices."
- Risk: PFOF <30% of revenue means the P&L hit is survivable, but the *repricing risk* is that best-execution + transparency commoditises the very thing TR competed on; differentiation moves to product breadth (wealth, terminal) and brand.

**Why the market goes this way (counterintuitive second-order):** the ban is sold as pro-investor, but its structural effect is **consolidation toward venue-owners**. Neobrokers with their own MTF/exchange (TR, Scalable) can internalise and survive; sub-scale brokers without a venue lose the rebate and have no replacement — so a "transparency" reform quietly **entrenches the two German incumbents** rather than opening the market.

## Sources
- EQS/TradingView press release (2026-07-02): Trade Republic new trading technology — Best Price, Direct Price (30 exchanges), Web Terminal.
- FinanceFeeds; Finance Magnates "Trade Republic Rebuilds Trade Execution as EU PFOF Ban Takes Hold"; BrokerChooser.
- Finance Magnates "PFOF Ban Threatens the Free-Trade Era for Europe's Neobrokers"; Börsen-Zeitung.
- heise / finanz-szene / DAS INVESTMENT: TR BaFin MTF license (2026-01-23).
- Internal corpus: [[Trade Republic raises EUR1.2B secondary at EUR12.5B valuation]], [[Trade Republic expands into wealth management with Apollo and EQT]], [[Trade Republic launches bond ETFs after €2.5 billion interest]], [[Trade Republic names Brad Pitt brand ambassador]], [[Italy fines Trade Republic €2.5 million for misleading ads]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **What share of the lost PFOF revenue does the €2 Direct-Price upsell + MTF internalisation actually recover?** — OPEN. TR says PFOF <30% of revenue; no data on replacement economics.
2. **Does TR now capture the market-maker spread it used to *receive* as PFOF?** — Likely yes via the MTF (BaFin license 23 Jan 2026), but internalisation volume undisclosed → the whole margin story is unproven.
3. **Is "Best Price / SOR" genuinely new, or repackaged institutional plumbing?** — SOR is an institutional standard (IBKR etc.); novelty = free + mass-retail + transparency UI, not the algorithm.
4. **Is Best Price *verifiably* best, or marketing?** — TR shows aggregated vs single-venue orderbooks in-app (a real transparency lever), but no third-party best-execution audit cited. OPEN.
5. **Why is Best Price free while Direct Price costs €2?** — Free default routes flow to TR's own MTF (monetisable); paid Direct Price is the opt-out that costs the customer to bypass internalisation. Follow the incentive.
6. **Does the €1 base commission survive, or is a Scalable-style subscription coming?** — Currently €1/trade held; no subscription announced. OPEN.
7. **How exposed is TR vs peers — is PFOF a German-only problem?** — Yes: FR/NL/SE/IT/ES already banned/never used PFOF; disruption is ~entirely German. TR & Scalable are the two exposed incumbents.
8. **Is Scalable structurally ahead?** — Yes on venue: EIX launched 10 Dec 2024 (~18 mo earlier) + €2.99/mo subscription already absorbs the shortfall. TR's UX (Web Terminal, transparency) may be the stronger consumer answer.
9. **What is Direct Price's attach rate / Web Terminal adoption?** — OPEN. Zero traction numbers; this is a launch, not adoption.
10. **Does this event duplicate any prior corpus note?** — NO. Distinct from all prior TR notes (funding, wealth, bond ETFs, Brad Pitt, Italy fine). FRESH.
11. **Does "transparency/best execution" commoditise TR's own moat?** — Plausibly: if execution quality converges, differentiation shifts to product breadth (wealth, terminal) + brand → repricing risk (analysis).
12. **Counterintuitive: does a pro-investor ban actually entrench incumbents?** — Likely yes — only venue-owners (TR MTF, Scalable EIX) can internalise; sub-scale brokers lose the rebate with no replacement.
13. **How does this fit the €12.5B valuation thesis?** — It converts a commodity, regulation-exposed take-rate into owned venue/spread + upsell revenue — necessary to defend a software-like multiple post-PFOF.
14. **Any conflict between the aggregated-note "such as Xetra/Euronext/NYSE/Nasdaq" and the PR "30 exchanges"?** — PR is authoritative: ~30 global venues; the note's list is illustrative, not exhaustive.
15. **Fraud/best-ex liability & who's silent?** — TR is silent on the economics of MTF internalisation and on independent best-execution verification; watch for regulator scrutiny given the June 2026 Italy misleading-ads fine.

**Importance: 4/5** — A regulation-forced, structurally significant re-architecture of the core execution/monetization model of Europe's largest neobroker (10M+ customers, €150B+ AuM), timed to the EU PFOF ban and building on its own new MTF. Fresh and consequential. Not a 5 because it is a launch with zero traction data and the SOR mechanism itself is not novel — the real weight (does MTF+upsell replace PFOF margin?) is still open.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-03]] (2026-07-03).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** European retail neobroking, ~€0–1/trade "commission-free" model. The structural trigger is regulatory: MiFIR Art. 39a bans payment for order flow (PFOF) EU-wide; Germany's transitional carve-out — the last one — sunset on 30 June 2026, so the model that bankrolled zero-fee trading is now dead in the largest neobroker market (per ESMA, MiFIR Art. 39a; The Industry Spread, 2026). France, NL, Italy, Spain never took the carve-out — PFOF was effectively unlawful for their residents since 2024. Economics of the shift: PFOF rebates (~€1–3/order) were reportedly ~one-third of Trade Republic's revenues per some accounts, though the company frames it as "less than 30%" (Finance Magnates, via TradingView, 2026-07). Why now: the ban forces a revenue-model pivot toward subscriptions, net interest income on client cash, securities lending and running one's own execution venue. Trade Republic received a BaFin MTF (multilateral trading facility) licence in January 2026 — this launch operationalises it: orders now execute against Trade Republic itself, i.e. the firm stands on the other side of the trade rather than routing straight to an exchange (Finance Magnates, 2026-07).

**Competitive landscape.** Sector KPIs: AUM/deposits, funded customers, net interest income on client cash, and (post-PFOF) subscription attach + take on proprietary execution/spreads. Key players & basis of competition: Trade Republic (10M+ customers, €150bn+ AUM per IR, Sep 2025) vs Scalable Capital (BlackRock-backed, €1.5bn/$1.4bn valuation — flat vs its 2021 Series E; ECB banking licence Sep 2025; runs its own European Investor Exchange (EIX) since Dec 2024 with Scalable Bank as market maker; €2.99/mo subscription) vs US-listed Robinhood (FY2025 net revenue $4.5bn, +52% YoY; expanding into UK/EU). Basis of competition is shifting from headline "free" price to execution quality + product breadth (Trade Republic added Private Markets with Apollo/EQT and fixed income in 2025). Recent moves: Trade Republic — Direct Price paid order type (choose Xetra/Euronext/NYSE/Nasdaq), best-price engine across ~30 venues, first browser terminal (2026-07); Scalable — EIX + banking licence (2024–25). Position: Trade Republic is ahead on scale in Europe (largest by customers/AUM per its own IR) and is first to pair an MTF licence with a productised paid order type; moat = scale + regulatory infrastructure (own MTF) + switching costs on a growing multi-asset stack `(analysis)`.

**Comps & multiples.** Trade Republic is private: €12.5bn valuation at the Dec 2025 €1.2bn secondary (IR funding announcement, 2025-12-17). No public revenue disclosure → EV/Revenue **no data**; price-per-customer = €12.5bn / 10m = **~€1,250/customer** (round valuation, not market cap; customer count per IR Sep 2025). External comps: Robinhood — FY2025 net revenue $4.5bn, +52% YoY, ARPU $191 (Robinhood Q4/FY2025 release, 2026-02-10); public, but a US PFOF-driven model, so a weak margin comp for post-PFOF Europe. Scalable Capital — ~€1.5bn round valuation, flat since 2021 (Sifted, 2025-10) → Trade Republic carries a materially richer private mark (~8x Scalable's valuation) on larger scale/AUM, in-line with its lead rather than an outlier `(analysis)`. Internal comps: [[Trade Republic raises EUR1.2B secondary at EUR12.5B valuation]]; [[Scalable Capital eyes European IPO after banking licence]]; [[Scalable Capital receives banking license from ECB]]; [[Trade Republic expands into wealth management with Apollo and EQT]]. Distribution not computed (only 2 comparable private valuations, different scale) — qualitative comparison only.

**Risk flags.**
1. **Revenue-model transition risk.** If PFOF was ~a third of revenue, the pivot to paid order types + spreads on own MTF must backfill a large gap without churning price-sensitive users who joined for "free" trading — execution risk on the core P&L (second-order: pressure to lean harder on net interest income, which is rate-cycle dependent and falls as the ECB cuts).
2. **Conflict-of-interest / execution-quality scrutiny.** Executing orders against itself on its own MTF replaces the PFOF conflict with a principal/internaliser conflict — regulators and press are already framing post-PFOF quote-driven venues as "conflict of interest, worse" (Banker on Wheels, 2026). Best-execution and spread transparency become the new regulatory attack surface.
3. **Monetisation optics.** "Direct Price" as a *paid* add-on to reach named exchanges signals the free tier no longer guarantees venue choice/best routing — reputational/competitive risk if peers (Scalable's EIX) or incumbents undercut on transparent all-in cost.

**What this changes (idea-lens).** The PFOF ban is a sector-wide re-rating of neobroker unit economics from rebate-funded "free" to a stack of subscription + net interest + proprietary-venue spreads; Trade Republic's MTF-plus-paid-order-type is the template European peers will be measured against `(analysis)`. Falsifiable thesis: neobrokers that own an execution venue (Trade Republic MTF, Scalable EIX) preserve margin and consolidate share, while sub-scale, pure-rebate brokers exit or get acquired. Trigger/what breaks it: first full post-ban quarter (H2 2026) showing whether Trade Republic's ARPU/take holds without PFOF and whether best-execution/spread complaints draw a BaFin or ESMA response.

Sources: https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifir/article-39a-prohibition-receiving-payment · https://www.financemagnates.com/forex/brokers/trade-republic-rebuilds-trade-execution-as-eu-payment-for-order-flow-ban-takes-hold/ · https://theindustryspread.com/eu-pfof-ban-mifir-article-39a-june-2026-vs-us-uk/ · https://www.bankeronwheels.com/pfof-and-quote-driven-venues/ · https://assets.traderepublic.com/assets/files/251217_Secondary_PressRelease_DE_EN2.pdf · https://drive.google.com/file/d/11k2OJq0IwsJM5oaxGaciDtYkZDPW20zt/view · https://investors.robinhood.com/node/15161/pdf · https://sifted.eu/articles/scalable-capital-banking-licence
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** NO-DATA on financial results — Trade Republic is a private company (Trade Republic Bank GmbH) and publishes **no quarterly/annual earnings**: no revenue, no profit/margin, no EPS. The current news is a product launch (best-price execution engine + Direct Price), not a report. What IS disclosed via the company's own IR press releases are **operating metrics** (customers, AUM, interest passed through) — trending UP — plus a Dec-2025 secondary round. Verdict on the print: **no earnings report; operating traction positive.**

**Key figures (company-disclosed operating metrics, own IR).**
- **Customers:** >10.0m across 18 European markets (as of 2025-09-15). Trajectory: 4.0m / 17 countries (2024-01-09) → 8.0m (2025-01-09, "doubled in just one year") → >10.0m (2025-09-15). No revenue/margin/EPS disclosed alongside — TR does not report a P&L.
- **Assets under management (AUM):** >€150bn (2025-09-15; reiterated ">150 billion euro" in the 2025-12-17 secondary release) → up from >€100bn (2025-01-09) → ~€35bn (2024-01-09). Roughly +50% AUM in the ~8 months Jan→Sep 2025; ~4.3x over ~20 months from Jan-2024.
- **Interest passed to customers:** >€1.0bn cumulative since Jan-2023 (as of 2024-11-15, "in under 2 years"), via full pass-through of the ECB deposit rate — the deposit economics behind the AUM growth. No net interest income / NIM disclosed.
- **Valuation (proxy, not results):** €1.2bn **secondary** round at **€12.5bn** valuation, led by Founders Fund with existing investors (Sequoia, Accel, TCV, Thrive), new holders Wellington, GIC, Fidelity, Khosla (2025-12-17). Secondary = existing-shareholder liquidity, **no primary capital raised**, no financials disclosed.

**By segment / driver.** Company frames the growth as a shift **from brokerage to wealth management**: three new asset classes rolled out in 2025 — Private Markets (Apollo & EQT, 2025-09-15), Fixed Income (2024-10-15), plus IPO access (2025-06-06) and crypto wallet (2024-11-14). AUM growth is attributed to national IBANs/branches (France, Spain, Italy) and deposit inflows on ECB pass-through, not disclosed by segment (no per-product AUM or revenue split available — no data).

**vs expectations / prior period.** No public consensus exists (private, no analyst estimates, no results). vs prior company disclosures: customers +25% (8m→10m within 2025), AUM +~50% (€100bn→€150bn within 2025) — clear acceleration in AUM per euro of new customer. All quantitative comparisons are company-disclosed operating metrics, not audited results. Revenue/profit vs any prior period: **[UNSOURCED] — not disclosed.**

**Guidance / forward.** None — TR issues no guidance. The Direct Price / best-price execution launch is a **response to the EU ban on payment-for-order-flow (PFOF)**, which removes a TR revenue stream from 2026; Direct Price is a **new paid order type** (revenue partially replacing lost PFOF) — magnitude of PFOF revenue lost or Direct Price economics **not disclosed (no data)**. (analysis) The wealth-management pivot (Private Markets/Fixed Income + deposit spread) is the strategic hedge against PFOF loss.

**Thesis-flags.**
1. **PFOF ban is a structural revenue hit** → Direct Price monetizes execution routing to backfill it → but TR discloses no revenue, so replacement rate is unverifiable → second-order: margin pressure risk that the company is not quantifying (who's-silent flag: touts product, silent on the P&L impact).
2. **AUM (+~50% in 2025) and deposit base compound the interest/spread engine** → but income depends on ECB rates → as the ECB eases, pass-through spread economics compress → second-order: the wealth-management pivot (fees on Private Markets/Fixed Income) is needed to de-risk from rate-sensitive net interest income.
3. **€12.5bn secondary (Dec-2025) with no primary capital** → validates valuation and gives insiders liquidity but adds no growth funding → signals TR is self-funding, consistent with positive operating cash generation (hypothesis) — but unconfirmed absent financials.

Sources (company's own IR, primary): Secondary round €1.2bn/€12.5bn 2025-12-17 — https://drive.google.com/file/d/11k2OJq0IwsJM5oaxGaciDtYkZDPW20zt/view (url: https://assets.traderepublic.com/assets/files/251217_Secondary_PressRelease_DE_EN2.pdf) · Private Markets / >10m customers / >€150bn AUM 2025-09-15 — https://drive.google.com/file/d/1U28xrS1TZ66qte2IJ67IdSiay1nQ7h_Q/view · Birthday / 8m customers / >€100bn AUM 2025-01-09 — https://drive.google.com/file/d/1K7LwtUzDJd-o2E1ZyZGa6MBF0PWQZ9HP/view · >€1bn interest passed through 2024-11-15 — https://drive.google.com/file/d/1CKn0quddUT6YP3pCCj4Jsywr9awIb9Un/view · Card / 4m customers / ~€35bn AUM 2024-01-09 — https://drive.google.com/file/d/1l4LumZ2-ER0zHudRf1RjhYdbrK2ml2Xh/view · Fixed Income / €2.5bn interest 2024-10-15 — https://drive.google.com/file/d/1_Nu7pl58Us44heeC7hdcdIRc_ta4pmZw/view · Revenue / profit / margin / EPS: **no data — Trade Republic is private and does not report a P&L.**
<!-- /enrichment:earnings_review -->
