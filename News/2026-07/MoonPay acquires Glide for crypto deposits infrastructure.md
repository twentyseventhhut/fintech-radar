---
title: "MoonPay acquires Glide for crypto deposits infrastructure"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - company/moonpay
  - company/glide
  - industry/crypto
  - industry/infrastructure
  - region/us
  - type/m-and-a
sources:
  - https://www.connectingthedotsinfin.tech/r/cbbf3980
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s8554456b
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# MoonPay acquires Glide for crypto deposits infrastructure

> [!info] 2026-07-17 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 MoonPay acquires Glide in an all-equity deal to expand crypto deposits infrastructure. Glide’s specialty is crypto deposits infrastructure, the plumbing that helps users and businesses move fiat currency into crypto wallets. By folding Glide into its stack, MoonPay gains deeper capabilities in bank and fiat integrations.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/cbbf3980>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MoonPay acquires Glide for crypto deposits infrastructure
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
MoonPay acquired **Glide**, a Y-Combinator-backed crypto-deposits startup, in an **all-equity (all-stock) deal** (terms undisclosed; announced 2026-07-16). The founders — **Tushar Soni (CEO)** and **Qinyu Tong** — previously led the team that built **Robinhood's crypto wallet**; Glide was founded in **2023**, backed by YC and Titan Fund.
- **What Glide actually does:** an internal routing layer that lets any app accept crypto deposits "from any token, wallet, exchange or card" **without the user manually bridging/swapping**. It picks between an instant relayer and bridge-and-swap routes based on speed/cost. Supports **100+ tokens across 30+ blockchains**.
- **Traction (real, but modest):** **>$100M annualized transaction volume**. This is small — for scale, MoonPay's own Meso-era US banking push and Helio ($1.5B+ processed) dwarf it. Glide is a **team + tech ("acqui-hire with volume") buy, not a scaled business**.
- **Where it lands:** Glide's tech folds into **MoonPay Deposits** — an existing product (launched **Feb 2026**, [[MoonPay launches Deposits for wallet transfers in Telegram]]) already live in Wallet in Telegram, Moonshot and Paysafe. So MoonPay is **buying to deepen a product it already shipped**, not entering a new category.
- **Why structured as all-equity:** classic early-stage acqui-hire — no cash out, founders/investors ride MoonPay's pre-IPO equity, aligns retention through the IPO window. Signals MoonPay is conserving cash while its stock is the deal currency (same pattern as DFlow/Sodot $100M all-stock deals).

## [1] Competitors / peers
The deposits/on-ramp infra layer is crowded and consolidating:
- **Transak** — >$2B processed, ~30% stablecoin; Oct-2025 Cross River deal added ACH/wire/RTP/FedNow US rails.
- **Ramp Network** — Open-Banking-led, ~0.49% SEPA (cheapest widget), 150+ countries.
- **Stripe Crypto (+ Bridge)** — US-strong, low fee + KYC reuse; Bridge gives infra-level control.
- **Coinbase Onramp** — free ACH for existing users, distribution moat.
- **Zero Hash / Bridge** — infra providers offering better economics if you bring your own compliance.
Position: MoonPay is **ahead on breadth** (coverage + now cross-chain deposit routing) but the specific "cross-chain deposit without manual bridging" job is **not unique** — Decent.xyz (which MoonPay ALSO acquired in 2026) did cross-chain routing/liquidity. **Second-order:** MoonPay is buying overlapping capabilities (Decent + Glide + native Deposits) — consolidation of the *same* routing problem, suggesting it wants to own the deposit-routing stack outright rather than any single differentiated tech.

## [2] Company history / fit
This is MoonPay's **6th acquisition announcement of 2026** and ~7th in 18 months. The spree:
- **2025:** Helio (~$175M, Solana payments), Iron (German stablecoin API infra), Meso (US banking rails — [[MoonPay to acquire payments startup Meso Network]]).
- **2026:** Sodot (~$100M all-stock, key mgmt → MoonPay Institutional under ex-CFTC chair Caroline Pham — [[MoonPay acquires crypto security startup Sodot for $100 million]]), DFlow (~$100M → MoonPay Trade — [[MoonPay acquires DFlow for on-chain trading infrastructure]]), Decent.xyz (cross-chain routing), Entendre (AI finance ops — [[MoonPay acquires Entendre for on-chain finance operations]]), Dawn Labs (AI trading — [[MoonPay acquires Dawn Labs and launches AI trading agent Dawn CLI]]).
- **Structural logic:** MoonPay's core on-ramp is a **commodity take-rate business (1–3% + float)**. To justify an infrastructure multiple and prep an **IPO**, it's stitching every gap in the payments-to-institutional stack via stock deals. Glide = plugging the "frictionless funding/deposit" gap so partners never send users elsewhere. Fits the [[MoonPay launches Headless Onramps for one-tap crypto checkout]] embedded/white-label thesis.

## [3] Novelty / value-add / traction
- **Genuinely new?** Marginally. MoonPay Deposits already existed (Feb 2026); Glide **upgrades** it with a mature routing engine + a proven Robinhood-pedigree team. The novelty is **team quality + $100M live volume**, not a new capability.
- **Value-add — real but incremental:** deposit friction (wrong-chain/wrong-token failed transfers) is a genuine conversion killer; owning best-in-class routing improves take-rate durability and partner stickiness.
- **Who captures the margin (analysis):** the risk is that deposit routing becomes **commoditized plumbing** — Decent, Glide, native builds all solve it. Margin sits with **distribution** (who owns the wallet/app the user funds), which is why MoonPay pairs this with Telegram/Moonshot/Paysafe partnerships. If routing commoditizes, the value migrates to whoever controls the front-end, not the router.

## [4] What's next / market sentiment
- **Integration:** Glide tech → MoonPay Deposits; expect faster, broader cross-chain funding across MoonPay partners; founders likely retained through IPO.
- **Sentiment:** framed as another step toward MoonPay as a **full digital-asset infrastructure provider** ahead of a rumored IPO. Market read is neutral-positive — expected continuation of a known M&A machine, not a surprise.
- **Risks / second-order:** (1) **Integration/overlap risk** — Glide + Decent + native Deposits must be rationalized or MoonPay pays twice for one capability. (2) **Regulatory** — cross-chain routing + fiat rails invite MTL/AML scrutiny (mitigated by the NYDFS trust charter, [[MoonPay secures NYDFS limited-purpose trust charter]]). (3) **Counterintuitive:** a rapid all-stock spree inflates the cap table and dilutes — if the IPO slips, the equity currency weakens and the acqui-hire retention thesis frays.

## Sources
- The Block — https://www.theblock.co/post/408603/moonpay-acquires-y-combinator-crypto-glide-all-equity-deal
- Cointelegraph — https://cointelegraph.com/news/moonpay-acquires-glide-strengthen-crypto-deposits
- Crypto Briefing — https://cryptobriefing.com/moonpay-buys-robinhood-wallet-veterans-startup-glide-to-simplify-crypto-deposits/
- FF News — https://ffnews.com/news/moonpay-acquires-glide-to-eliminate-friction-in-cross-chain-crypto-deposits
- Y Combinator (Glide) — https://www.ycombinator.com/companies/glide-2
- Fortune (DFlow $100M spree) — https://fortune.com/2026/05/05/moonpay-acquires-solana-100m-all-stock/
- Competitor landscape — https://tokenmetrics.com/blog/top-on-and-off-ramp-providers-fiat-to-crypto-2026/
- Primary: https://www.connectingthedotsinfin.tech/r/cbbf3980

Internal corpus: [[MoonPay launches Deposits for wallet transfers in Telegram]], [[MoonPay to acquire payments startup Meso Network]], [[MoonPay acquires DFlow for on-chain trading infrastructure]], [[MoonPay acquires crypto security startup Sodot for $100 million]], [[MoonPay acquires Entendre for on-chain finance operations]], [[MoonPay launches Headless Onramps for one-tap crypto checkout]], [[MoonPay secures NYDFS limited-purpose trust charter]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions (second-order)**

1. Is this fresh or a re-run of MoonPay Deposits (Feb 2026)? — **Fresh.** Deposits was a product LAUNCH ([[MoonPay launches Deposits for wallet transfers in Telegram]]); this is a distinct M&A event (Glide acqui-hire) that *feeds into* Deposits. New entity, new terms.
2. What were the deal terms? — **All-equity/all-stock, undisclosed value.** No cash figure or valuation published. (open on price)
3. How much real traction does Glide have? — **>$100M annualized volume**, 100+ tokens, 30+ chains. Modest — this is a team+tech buy, not a scaled business.
4. Is the tech differentiated, or does MoonPay already own it? — **Overlaps with Decent.xyz** (also acquired 2026, cross-chain routing) and native Deposits. Risk of paying twice for one capability. (analysis)
5. Who captures the margin if deposit routing commoditizes? — **Distribution (wallet/app front-end)**, not the router. Value migrates to whoever owns the funded surface.
6. Why all-stock, not cash? — Conserves cash, uses pre-IPO equity as currency, aligns founder retention through IPO. Same pattern as DFlow/Sodot.
7. Are the founders retained? — Implied (acqui-hire logic); not explicitly time-boxed in sources. (open on lock-up)
8. Does this move the on-ramp competitive needle vs Transak/Ramp/Stripe? — Marginally; improves partner stickiness but the specific job isn't unique. Transak's Cross-River US rails and Ramp's cheap SEPA are stronger single differentiators.
9. What's the count/context of this deal in the spree? — **6th of 2026, ~7th in 18 months.** Signals IPO prep, not organic strategy.
10. Regulatory exposure of cross-chain routing + fiat? — MTL/AML/travel-rule risk; partly mitigated by NYDFS trust charter. (open on jurisdiction specifics)
11. Cap-table / dilution risk from serial all-stock deals? — Real. If IPO slips, equity currency weakens and retention thesis frays. (analysis)
12. Is "any token/wallet/exchange/card" claim live or aspirational? — Live per Glide's stated 100+ tokens/30+ chains and $100M volume; the "card" leg maps to MoonPay's existing on-ramp. Plausible-live.
13. Does this cannibalize third-party on-ramp partners? — Owning the deposit layer could pull volume in-house, straining partner relationships. (hypothesis)
14. Any disclosed synergy metric (conversion uplift, cost)? — **None disclosed.** Pure capability narrative. (open)
15. What breaks the thesis? — Deposit routing commoditizing before MoonPay monetizes it via distribution; integration overhang across Glide+Decent+Deposits.

**Importance: 3/5** — A logical, on-strategy tuck-in acqui-hire with a strong (Robinhood-pedigree) team and real-but-small ($100M) volume, folding into an existing product. Fresh event, but incremental: no new category, undisclosed/all-stock terms, and overlap with prior MoonPay buys cap the weight. Above a 2 for the team quality and clear IPO-narrative signal; below a 4 for lack of scale, price, or novel capability.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto fiat on/off-ramps + "deposits" (cross-chain/cross-token funding) sit inside the on/off-ramp market — est. ~$8bn in 2024, projected >$35bn by 2033 (per Token Metrics/Spark landscape, as of 2026; figure is a secondary analyst estimate, treat as directional, not audited). The adjacent prize MoonPay actually chases is stablecoin payments: total stablecoin mkt-cap ~$313bn (30-Jun-2026), on pace for $40–46tn raw on-chain volume in 2026, but *real-economy* payment volume only ~$390bn annualized (McKinsey/Artemis, Dec-2025 basis) — the TAM is real but far smaller than headline volume implies (per McKinsey, via web, 2026). Structure: **consolidating**. Ramp/deposits is a thin-margin, capital+licensing-gated commodity layer where value accrues to whoever owns the most licenses × distribution × integrations; barriers = money-transmitter licensing (MoonPay: 46+ US jurisdictions + NY BitLicense, all-50-state coverage) and network of embedding apps, not the routing tech itself. Why now: the ramp market has visibly shed independents — Wyre shut (Jan-2023), Banxa bought by OSL for ~C$85.2m (Jan-2026) — so sub-scale ramp/deposit startups face a build-vs-sell fork, and MoonPay is the natural consolidator mid-fundraise.

**Competitive landscape.** Sector KPIs: TPV/annualized transaction volume, take rate, license/geo coverage, # of embedding apps, token/chain coverage. Basis of competition = distribution + licensing + conversion/UX, not price (fees are largely commoditized). Key players: **MoonPay**, **[[Ramp Network rolls out multichain self-custody wallet|Ramp Network]]**, **[[Transak raises $16 million from Tether and IDG Capital|Transak]]**, Banxa (now OSL), plus vertically-integrated incumbents Coinbase/Stripe(Bridge)/Circle that can self-supply ramps. Recent peer moves: Ramp got EU-wide MiCAR authorisation ([[Ramp Network receives EU-wide MiCAR authorisation]], Dec-2025) and shipped a self-custody wallet (Apr-2026); Transak raised $16m from Tether/IDG (Aug-2025). MoonPay's own position: **clear leader / aggressive roll-up** — Glide is its **6th acquisition of 2026** (after Sodot, Decent, DFlow, Entendre, Dawn Labs) on top of 2025's Helio ($175m), Iron, Meso. Moat = licensing scale + ~30m customers + ~500 embedding firms (intangibles + distribution network effects). Glide (founded 2023 by ex-Robinhood-wallet Tushar Soni & Qinyu Tong, YC-backed, 4 employees) folds into **MoonPay Deposits**, already live in Wallet-in-Telegram, Moonshot, Paysafe — so this is a capability tuck-in into an existing product, not a new market entry.

**Comps & multiples.** All-equity deal, **terms undisclosed** — no purchase price → no deal multiple computable ("no data"). Sizing anchors: Glide processes >$100m annualized transaction volume and covers 100+ tokens / 30+ chains (per The Block/company, 2026); as a 4-person acqui-hire, price is almost certainly modest relative to MoonPay's scale (analysis). MoonPay itself (private): ~$3.4bn post-money early-2025, ~$107.6m 2025 revenue per Latka → implied ~32x P/S (`$3.4bn / $107.6m = 31.6x`) — rich, but revenue reportedly grew +112% YoY (2024 net revenue) so the multiple is not obviously unjustified on growth; **caveat: the $3.4bn valuation and $107.6m revenue are third-party/secondary estimates, not audited** → treat as `[UNSOURCED]`-adjacent, not primary. A $5bn round (ICE reportedly in talks, Dec-2025) is a *round valuation*, not market cap. Internal roll-up comps (all MoonPay, showing the pattern): [[MoonPay acquires crypto security startup Sodot for $100 million]] ($100m all-stock), [[MoonPay acquires DFlow for on-chain trading infrastructure]] (~$100m), [[MoonPay acquires Entendre for on-chain finance operations]] (undisclosed acqui-hire), [[MoonPay to acquire payments startup Meso Network]] (undisclosed). Peer-move comp: Banxa → OSL at ~C$85.2m (Jan-2026) frames what a sub-scale ramp is worth. Distribution not computed (only 1 priced peer deal + MoonPay's own P/S) → qualitative.

**IR grounding (PRIMARY, MoonPay newsroom/IR).** MoonPay is private — no filings, but its own IR discloses real figures folded here as primary evidence: 2024 results **cash-flow positive, profitable, +112% YoY net-revenue growth** (funding_announcement, 2025-03-20, https://www.moonpay.com/newsroom/galaxy); Q1-2025 **transaction volume +123% QoQ, net revenue +43% QoQ** (product_update, 2025-04-28, https://www.moonpay.com/newsroom/nyc-office). Latest IR result: **NYDFS trust charter** for custody + OTC (press_release, 2025-11-01, https://www.moonpay.com/newsroom/nytrust) — reinforces the licensing-moat thesis. These confirm MoonPay funds this M&A spree from a profitable, fast-growing base and pays in its own (appreciating) equity — hence the all-equity structure.

**Risk flags.** (1) **Roll-up integration/indigestion risk** — 6 deals in ~7 months (2026) on top of 5+ in 2025; each is a small team + point capability that must be knit into one stack. Second-order: integration debt + culture dilution can stall the platform-synergy thesis that justifies a ~32x P/S. (2) **Disintermediation by vertically-integrated incumbents** — Coinbase, Stripe/Bridge, Circle can self-supply ramps/deposits and bypass MoonPay's rails; deposits routing is thin-margin and copyable, so the moat is licensing+distribution, not this tech. Second-order: if big wallets in-house the deposit layer, MoonPay's per-txn economics compress. (3) **Regulatory/licensing dependence** — the entire moat rests on money-transmitter/trust licenses across 46+ jurisdictions; any adverse licensing/reserve action (esp. as it moves into stablecoin *issuance* and institutional custody) hits the core asset directly.

**What this changes (idea-lens).** (analysis) Confirms MoonPay is executing a *serial-consolidator* play to become the full-stack "money-movement OS" for crypto (issuance → ramps → deposits → swaps → payments → fin-ops), using richly-valued equity as acquisition currency ahead of a rumored $5bn round. Falsifiable thesis: if MoonPay's *organic* net-revenue growth decelerates sharply while deal cadence stays high, the roll-up is masking core stagnation — watch the next disclosed KPI update (transaction volume / net-revenue QoQ) and whether the ICE-led $5bn round actually closes. Trigger to re-rate: a priced primary round + disclosed post-integration TPV.

Sources: https://www.theblock.co/post/408603/moonpay-acquires-y-combinator-crypto-glide-all-equity-deal · https://cointelegraph.com/news/moonpay-acquires-glide-strengthen-crypto-deposits · https://blog.tokenmetrics.com/p/top-on-and-off-ramp-providers-fiat-to-crypto-2026 · https://www.spark.money/research/crypto-on-off-ramp-market-landscape · https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss · https://getlatka.com/companies/moonpay.com · https://www.moonpay.com/newsroom/galaxy · https://www.moonpay.com/newsroom/nyc-office · https://www.moonpay.com/newsroom/nytrust
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No formal earnings report** — MoonPay is a private company and does not publish quarterly/annual financial statements. Below is the best available disclosed financial profile (from MoonPay's own newsroom/IR + press) and what this all-equity deal implies for economics. No P&L, no EPS, no audited results exist.

**Disclosed financial profile (MoonPay-sourced, real figures).**
- FY2024: MoonPay states it was **cash-flow positive and profitable**, with **net revenue +112% YoY** vs 2023 (disclosed in the Galaxy $200M credit-line release, 2025-03-20).
- Q1 2025 KPIs (MoonPay newsroom, 2025-04-28): **transaction volume +123%** and **net revenue +43%** on a quarter-over-quarter basis; growth attributed to higher trading volumes and new merchant partnerships.
- Scale: **6,000+ merchants**, **$1.5bn+ annualized transaction volume** (company/press figures, 2025).
- Capital: total funding ~**$643M** (incl. the $555M Series A closed late-2021); **$200M debt facility** from Galaxy (Mar-2025). Recognition: #21 on 2025 CNBC Disruptor 50.
- Recent build-out (custody/stablecoin rails): **New York Trust Charter** (2025-11-01) for digital-asset custody + OTC; **Virtual Accounts / enterprise stablecoin infrastructure** launched in NY (2025-10 / 2025-11).

**Valuation (third-party press estimates — NOT MoonPay-disclosed).**
- ~**$3.4bn** post-money (early-2025 estimates). ~**$107.6M** revenue for 2025 (getlatka/aggregator estimate — [UNSOURCED] vs primary IR).
- Reported (Dec-2025 press) that **ICE (NYSE parent) is in talks** to invest at a **~$5bn valuation** — a report, not a closed round. Treat as unconfirmed.

**Deal economics implied by the Glide acquisition.**
- Structure: **all-equity**, size **not disclosed** — so no cash outflow and no revenue/EBITDA multiple is observable. This is an acqui-hire + IP tuck-in: Glide is a **4-person team** (ex-Robinhood Wallet founders Tushar Soni & Qinyu Tong, YC-backed, founded 2023).
- Glide scale absorbed: **>$100M annualized transaction volume**, **100+ tokens across 30+ chains** — small relative to MoonPay's $1.5bn+ TPV, so near-term revenue accretion is immaterial; the value is deposit-routing/fiat-onramp plumbing folded into **MoonPay Deposits** (already used by Telegram Wallet, Moonshot, Paysafe).
- Strategic frame: **MoonPay's 6th acquisition of 2026** (after Sodot, Decent, DFlow, Entendre, Dawn Labs) — an equity-funded roll-up building a full digital-asset infrastructure stack. An all-equity, undisclosed-size deal signals MoonPay is spending its (private) shares rather than cash, consistent with preserving the $200M facility and any pending ICE raise.

**Thesis-flags.**
- (1) All-equity + undisclosed size = MoonPay prefers paper over cash for tuck-ins → dilution to existing holders, but conserves the balance sheet ahead of a potential $5bn-valuation raise (second-order: signals confidence its equity is a strong acquisition currency).
- (2) Six deals in ~7 months is an aggressive infra roll-up → integration/execution risk is the real question the (private, unaudited) numbers cannot answer; MoonPay discloses growth % but **stays silent on absolute revenue, margins post-M&A, and share count/dilution**.

Sources: https://www.moonpay.com/newsroom/galaxy · https://www.moonpay.com/newsroom/nyc-office · https://www.moonpay.com/newsroom/nytrust · https://www.theblock.co/post/408603/moonpay-acquires-y-combinator-crypto-glide-all-equity-deal · https://cointelegraph.com/news/moonpay-acquires-glide-strengthen-crypto-deposits · https://pitchbook.com/profiles/company/266376-70 · valuation/revenue estimates are third-party aggregator figures [UNSOURCED vs primary IR].
<!-- /enrichment:earnings_review -->
