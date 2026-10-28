---
title: "ACI Worldwide and Circle collaborate on USDC settlement in LatAm"
date: 2026-10-28
retrieved: 2026-10-28
tags:
  - company/aci-worldwide
  - company/circle
  - industry/stablecoins
  - region/latam
  - type/partnership
sources:
  - https://www.businesswire.com/news/home/20261027452148/en/ACI-Worldwide-and-Circle-Collaborate-to-Bring-USDC-Settlement-to-Existing-Payments-Infrastructure-in-Latin-America
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s2647fd69
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# ACI Worldwide and Circle collaborate on USDC settlement in LatAm

> [!info] 2026-10-28 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌎 ACI Worldwide and Circle collaborate on USDC settlement in Latin America. The companies have announced a collaboration designed to connect USDC-based settlement with existing payments infrastructure in the region. The Latin American settlement collaboration targets interoperability between stablecoin and conventional payment systems.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261027452148/en/ACI-Worldwide-and-Circle-Collaborate-to-Bring-USDC-Settlement-to-Existing-Payments-Infrastructure-in-Latin-America>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 2026-10-27 ACI Worldwide (NASDAQ: ACIW) and Circle (NYSE: CRCL) announced a collaboration to bring USDC settlement to *existing* payments infrastructure in Latin America, with the first deployment focused on Colombia. The collaboration pairs Circle's regulated USDC with ACI Connetic — ACI's cloud-native payments orchestration platform — to demonstrate how stablecoin settlement can run *alongside* (not replace) traditional, instant and card rails. The framing is "integration into existing infrastructure," i.e. a settlement/liquidity layer banks can test without ripping out their current rails. (businesswire.com / investor.aciworldwide.com, 2026-10-27.)

**[1] Why Colombia first.** ACI built the core real-time technology for Colombia's national instant-payments scheme, **Bre-B** (addressing directory + real-time clearing + centralised settlement engine), selected by Banco de la República. Bre-B went live Sep 2025 and had already processed 500M+ transactions and registered 100M+ payment keys within ~5 months (by early 2026). This collaboration explores how USDC can complement Bre-B's account-to-account real-time rail and extend connectivity across multiple payment channels. So the "existing infrastructure" is literally infrastructure ACI itself operates — low integration friction, a captive reference deployment. (businesswire.com 2026-03-19; banrep.gov.co.)

**[2] The two players' strategies.**
- *Circle* is aggressively distributing USDC as a cross-border settlement rail through incumbents rather than direct: it launched **CPN Managed Payments** (Apr 2026), a full-stack solution letting banks/PSPs settle in USDC *without holding crypto* (Circle handles minting/burning, orchestration, compliance, chain infra). As of Aug 2026, Circle Payments Network reported 175+ financial institutions enrolled across 25+ blockchains; USDC cumulative on-chain settlement is cited at $70T+. Circle already had a LatAm USDC foothold via Mercado Pago. ACI is another incumbent distribution channel.
- *ACI* positions Connetic as a single cloud-native platform unifying traditional, instant, card AND digital-asset (stablecoin / tokenized-deposit) rails — e.g. consolidating eight US networks (RTP, FedNow, Swift, etc.). Stablecoin support is a feature of its multi-rail orchestration pitch, letting it sell "future-proofing" to bank customers. (pymnts.com, businesswire.com 2026-04-08, 2026-04-23.)

**[3] Prior art in the vault — pattern, not one-off.** This is the latest in a steady run of Circle-via-incumbent USDC settlement deals:
- [[Circle partners with Finastra on cross-border stablecoin payments]] (2025-09) and [[Circle and Finastra weave USDC settlement into bank payments]] (2025-08) — USDC into Finastra GPP ($5T/day cross-border).
- [[FIS partners with Circle for bank stablecoin payments]] (2025-07) — US FIs, domestic + cross-border USDC.
- [[Corpay and Circle to embed USDC across cross-border rails]] (2025-08) — FX/commercial-card rails.
- [[Nium and Circle connect USDC settlement with global payouts]] (2026-05) — last-mile local-currency payout.
- [[dLocal integrates Circle Payments Network for stablecoin payouts]] (2025-11) and [[Circle and LianLian Global explore cross-border payments]] (2025-12) — emerging-markets / LatAm payouts via CPN.
- [[ACI Worldwide's Phil Bruno on stablecoin last-mile challenges]] (2025-08) — ACI's own earlier stablecoin commentary; this collaboration operationalises that stance.
The ACI-Circle deal is distinct from the above: it is the first to attach USDC to a *national real-time A2A scheme that ACI itself runs* (Bre-B/Colombia), rather than a correspondent/payout network.

**[4] Caveats / what this is NOT (yet).** Language is "collaborate / demonstrate / explore," and multiple outlets call Colombia a *pilot*. No disclosed volumes, go-live date, named bank participants, or revenue terms. This is a design/reference-architecture announcement, not a live production settlement product with committed users. Competitors (FIS/Worldpay, Fiserv, Finastra, Worldline, Adyen) all have their own stablecoin-settlement or multi-rail plays, several already partnered with Circle — so ACI's differentiation rests on the Bre-B incumbency, not exclusivity.

Sources:
- https://investor.aciworldwide.com/news-releases/news-release-details/aci-worldwide-and-circle-collaborate-bring-usdc-settlement
- https://www.businesswire.com/news/home/20261027452148/en/ACI-Worldwide-and-Circle-Collaborate-to-Bring-USDC-Settlement-to-Existing-Payments-Infrastructure-in-Latin-America
- https://cryptobriefing.com/circle-aci-usdc-colombia-bre-b-pilot/
- https://decrypt.co/381982/circle-pushes-deeper-latin-america-usdc-settlement-colombia
- https://www.businesswire.com/news/home/20260319965529/en/Colombias-BreB-Hits-More-than-500-Million-Transactions
- https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
- https://www.pymnts.com/cryptocurrency/2026/circle-launches-managed-payments-for-stablecoin-settlement/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
Red-team questions (skeptical; "collaborate/explore/pilot" language warrants discounting):

1. Is this a signed commercial deal or just a demonstration? The press language is "collaborate to bring" and outlets describe a Colombia *pilot* — what, if anything, is contractually committed vs. a joint PR/reference-architecture exercise?
2. Are there ANY named bank, PSP, or merchant participants on the Colombia deployment, or is it currently just ACI + Circle showing a sandbox integration?
3. No volumes, no go-live date, no revenue split disclosed — what concrete metric would let us judge adoption 6–12 months out?
4. Does USDC actually settle *inside* Bre-B, or merely "complement" it? Bre-B is a central-bank A2A scheme settling in COP; where does a USD stablecoin fit without FX conversion at the edges, and who bears that FX?
5. Regulatory: Colombia has no comprehensive stablecoin framework. What is Banco de la República's stance on a USD stablecoin touching its national instant-payments rail — is the central bank even a party here, or just ACI as vendor?
6. Is this cannibalistic or additive for ACI? If banks settle cross-border in USDC, does that reduce ACI's traditional cross-border/correspondent processing revenue?
7. Circle has done near-identical "collaborations" with FIS, Finastra, Corpay, Nium, dLocal, LianLian. How many of those produced measurable production volume vs. staying announcements? What's the base rate of these turning real?
8. Differentiation: every major processor (FIS, Fiserv, Worldline, Adyen) has a stablecoin/multi-rail story and several already partner with Circle. What does ACI uniquely offer beyond operating Bre-B — and is that moat durable if the central bank multi-sources?
9. Demand question: Colombian consumers/merchants transact in COP; who actually needs USDC settlement here — remittance corridors, cross-border merchant payouts, or treasury? The announcement is vague on the end use-case.
10. Depeg / reserve risk: routing settlement through USDC introduces stablecoin reserve and redemption-liquidity risk onto a payments rail. Is that risk acknowledged, and would a regulator accept it on critical national infrastructure?
11. "LatAm" headline vs. Colombia-only reality: is there any committed expansion beyond Colombia, or is "Latin America" aspirational framing off a single-country pilot?
12. Materiality to ACIW/CRCL financials: is this large enough to move either company's numbers, or is it a strategic signaling / option-value play with no near-term P&L impact?
13. Timing: why now? Is this riding the post-GENIUS-Act/stablecoin-regulation momentum and Circle's post-IPO distribution land-grab more than specific LatAm demand?
14. Could Mercado Pago (Circle's existing LatAm USDC partner) make the ACI channel redundant in Circle's largest LatAm market?

Importance: 3/5 — Genuinely interesting because it ties USDC to a *live national real-time scheme that ACI itself operates* (Bre-B), which is a more credible integration path than another generic correspondent-network tie-up, and both names are public and market-relevant. Discounted from higher because it is an exploratory Colombia pilot with no disclosed volumes, participants, go-live, or revenue, and it fits a well-worn "Circle + incumbent announce USDC settlement" pattern where most prior deals have not yet shown production scale. Watch for a named bank going live on Bre-B settlement and any Banco de la República endorsement.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector context — stablecoin cross-border settlement meets LatAm real-time payments.** The ACI Worldwide–Circle collaboration (announced Oct 27, 2026) is less a pure stablecoin play than an attempt to wire USDC *into* existing bank and real-time-payment infrastructure rather than around it. Per press coverage, the initial focus is a Colombia pilot built on Bre-B — the country's interoperable instant-payments ecosystem, whose central infrastructure ACI itself built — pairing Circle's USDC with ACI's payments orchestration (Connetic) so banks can run stablecoin settlement alongside conventional rails. Important caveat: this is a demonstration/pilot, not a confirmed large-scale deployment, and the public note's generic "across Latin America" framing overstates what is so far a single-country test.

The timing sits on top of a genuinely large and fast-growing LatAm stablecoin wave. Industry data put stablecoins at roughly ~32% of cross-border value in Latin America, with the region cited as a global leader in stablecoin cross-border usage; one estimate has stablecoins reaching 18–22% of the LatAm remittance market in 2026 (~$25–31B of transfer volume), driven by cost: traditional remittance fees average ~6%+ vs ~0.5–1.5% for stablecoin rails. Mexico's cross-border stablecoin activity reportedly quadrupled since early 2024 to ~$1.8B/month by mid-2026. (Web figures from trade/market sources — directional, not audited.)

**Circle IR grounding (PRIMARY — filed figures).** Circle's economics are overwhelmingly a reserve-income/float business, which frames the strategic value of this deal (volume and USDC-in-circulation growth, not direct fee revenue from the pilot). From Circle's Q1 2026 10-Q (period ended Mar 31, 2026):
- USDC in circulation: **$77.0B end-of-period**, **$75.2B average** (vs $60.0B / $54.1B a year earlier — ~39% average growth YoY).
- Reserve return rate: **3.5%** (down from 4.2% a year earlier — rate-sensitivity risk).
- Reserve Income **$653M** (+17% YoY), Other Revenue **$42M**, Total Revenue and Reserve Income **$694M** for the quarter.
- Reserve income was **96.0% of total revenue in FY2025** (per 10-K), underscoring how dependent Circle remains on float and interest rates rather than transactional/network revenue.
USDC-on-platform EOP jumped to $13.7B (from $3.9B), signaling Circle's push to capture more of the economics on its own rails — the strategic logic behind infrastructure deals like this one. (Source: Circle 10-Q filed 2026-05-11, https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm; drive copy https://drive.google.com/file/d/1NuyHWOdF_ldCMf4fbqo24_-SLrUMD1Vn/view for 10-K revenue-mix figure.)

**In-base comparables (news DB).** This fits a clear 2025–26 pattern of Circle embedding USDC into incumbent rails rather than building new consumer apps:
- *Circle + Finastra* (Sep 2025) — connect Finastra GPP banks (>$5T/day cross-border) to USDC settlement; the closest structural analog (orchestration layer + USDC).
- *Corpay + Circle* (Aug 2025) — USDC across Corpay's cross-border pay-in/pay-out and commercial-card rails.
- *ACI + Prosa* (Oct 2025) — ACI's existing LatAm payments-infrastructure footprint, showing ACI is the incumbent rail, not a newcomer, in the region.
- Competing stablecoin rails in LatAm: *Bitso + Ripple RLUSD/XRP* for US–LatAm settlement (Feb 2026) and *dLocal + Félix* WhatsApp stablecoin remittances (Nov 2025) — i.e., USDC is not the only settlement token chasing these corridors.

**Risk flags.**
1. **Pilot ≠ production.** Public framing ("USDC settlement in LatAm / across the region") overstates a single Colombia Bre-B test; monetization and regional rollout are unproven.
2. **Reserve-rate dependence.** Circle's revenue is ~96% reserve income; the return rate already fell 420bps-area (4.2%→3.5% YoY). A rate-cut cycle compresses Circle's economics regardless of volume — so growth must come from circulation, which this deal targets only indirectly.
3. **Token competition in-corridor.** USDT dominates LatAm retail stablecoin usage and Ripple's RLUSD/XRP is actively courting the same US–LatAm settlement flows; USDC's incumbency here is far from assured.
4. **Regulatory/FX.** Cross-border stablecoin settlement in Colombia, Argentina, and Mexico faces evolving local FX, capital-control, and stablecoin-regulation regimes; bank adoption depends on supervisory comfort that is not yet settled.
5. **No disclosed economics.** Neither party has disclosed volume commitments, revenue split, or go-live dates; ACI's upside (orchestration licensing) and Circle's (incremental USDC float) are currently unquantified.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
This is a partnership story (ACI Worldwide to connect USDC settlement to its LatAm payments rails), not an earnings print — so the earnings layer here is scale context: how big is the USDC/CPN engine ACI would be plugging into, and whether Circle's economics make a stablecoin settlement rail a credible commercial proposition.

**Latest reported quarter (for scale, not a beat/miss on this news).** Circle's most recent print is **Q2 2026**, reported **2026-08-05** (fresh, within ~3 months of today; note that `ir_latest.json[circle]` lags — its newest earnings doc is the Q1 2026 release of 2026-05-11, and the 2026-06-12 "latest_result" 8-K is a non-earnings filing). The Q2 print was a **MISS vs consensus**: total revenue and reserve income **$701.3M (+7% YoY)** but GAAP **EPS $0.18 vs ~$0.27 public consensus** — a record circulation offset by a falling reserve yield.

**Key figures (Q2 2026, reported).**
- Total revenue + reserve income **$701.3M, +7% YoY**; sequentially roughly flat vs Q1 2026's $694M.
- **Reserve income $668M, +5% YoY** — 96%+ of revenue; growth from +25% average circulation, mostly offset by a **66 bps drop in the reserve return rate to 3.48%**.
- **USDC in circulation $73.3B at period-end (+19% YoY)**; **average circulation $76.5B (+25% YoY), a record** (vs $77.0B EoP in Q1 2026).
- Other revenue (subscription/services/transaction) is the stated growth lever: FY2026 other-revenue guidance **raised to $310–$330M** (from $150–$170M), driven by Arc and a **$242M Arc token presale**.
- Adjusted EBITDA **$143M (+8% YoY)**, ~50% margin; revenue-less-distribution-cost margin **41.2% (+3pp YoY)**. Net income from continuing ops **$48M** (prior-year comparison distorted by IPO stock-comp).

**The metric that matters for this deal — Circle Payments Network (CPN).** CPN is the rail ACI's collaboration actually hooks into. At end-Q2 2026, CPN annualized payment volume was **~$15B** on a trailing-30-day basis (reported ~$14.7B, **+76% QoQ**), with **175 financial institutions enrolled (+29% QoQ)**, and management flagged it had already climbed to **~$23B by July 31, 2026**. This is still a tiny fraction of USDC's ~$73B circulation and $21.5T quarterly onchain volume — CPN is early-stage, which is precisely why an incumbent-rail distributor like ACI Worldwide (connecting USDC settlement to existing LatAm infrastructure) is strategically useful: it is a distribution play on a rail whose volumes are small but compounding fast.

**vs expectations / prior period.** Q2 revenue **$701.3M vs ~$694M in Q1 2026** (near-flat QoQ) and **+7% YoY**; EPS **$0.18 missed ~$0.27 public consensus** (StockAnalysis/Yahoo-type aggregators; consensus "as of" early Aug 2026). The driver is structural, not a one-off: reserve yield is compressing (-66 bps YoY) as the rate cycle turns, so circulation growth (+25% avg) is running just to stand still on reserve income. This is the core thesis flag — Circle's P&L is still ~96% rate-sensitive reserve income.

**Guidance / forward.** FY2026 other-revenue guidance **raised sharply to $310–$330M**; RLDC margin outlook lifted to **41.7%–43.7%**; adjusted opex guided **$570–$585M**. Management tone was growth-forward on **Arc** (public mainnet launched 2026-09-16, 100+ builders, BlackRock/DTCC involvement) and CPN, i.e. pivoting the story toward non-reserve revenue — the de-PR read is they are loud on circulation records and Arc/CPN momentum, and quieter on the reserve-yield headwind squeezing the dominant revenue line.

**Thesis-flags for the ACI partnership.**
1. Fact: CPN volume +76% QoQ to ~$15B (≈$23B by July) off a tiny base → why: real-world settlement adoption is accelerating → why it matters: ACI connecting USDC settlement to LatAm card/real-time rails adds exactly the incumbent distribution CPN lacks → second-order: converts Circle's "stablecoin as settlement asset" thesis from onchain-native into mainstream cross-border rails.
2. Reserve yield -66 bps YoY offsetting +25% circulation → non-reserve revenue (CPN/Arc/subscription) is now the strategic swing factor → a LatAm settlement rail that drives real transactional volume is directly on-thesis for the revenue-diversification Circle needs.
3. Scale proportionality: this collaboration touches a rail that is <1% of USDC circulation today — commercially promising, not yet financially material to the print.

Sources: Circle Q2 2026 press release (NASDAQ/SEC 8-K, 2026-08-05) https://www.nasdaq.com/press-release/circle-reports-second-quarter-2026-results-2026-08-05 · SEC 8-K exhibit https://www.sec.gov/Archives/edgar/data/1876042/000187604226000246/augustepr-circle_q22026f.htm · Q1 2026 release (prior period) https://www.circle.com/pressroom/circle-reports-first-quarter-2026-results · public consensus/EPS miss via aggregators (StockAnalysis/Yahoo, as of early Aug 2026). ir_latest.json[circle] lags Q2 (cross-checked EDGAR/web).
<!-- /enrichment:earnings_review -->
