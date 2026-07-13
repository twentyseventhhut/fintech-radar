---
title: "Worldpay outage leaves UK pubs and shops cash-only during England match"
date: 2026-06-25
tags:
  - company/worldpay
  - industry/payments
  - industry/cards
  - region/uk
  - type/outage-security
sources:
  - https://www.connectingthedotsinfin.tech/r/2bea15c6
  - https://www.connectingthedotsinfin.tech/r/3a5df0bb
  - https://www.connectingthedotsinfin.tech/r/cb18f4a7
  - https://www.connectingthedotsinpayments.com/r/787d8f73
  - https://elink22c.strictlyvc.com/ss/c/u001.Lk2l_GQ_9y3_OeVsl2E52hugD7aQjoXn8AIz0S04U3ir_nzXiPl1AhclafZEo0LJXZx2OwN1Hb1RfJ3P_RSoGMQq5z9hZooudBFOR_-xmQkn5KV1fkw_g82p-ktF6zZEXcmYTuO_nKHqjw49J4v0N_Nszu1SX29bk7_K31urJsRqDJGGPtwgzSJOGiCPaI1f-mzKXVRPCqIIYZ8UpgCBFf-_F9Zxjkyo5sQz4ThoU1OMDaaJ8lg0dAQC4Qf2mKYW717oU7eWGmC4fe7JDrlfuDJbBvfAhpeGCFrK-cZrH4I/4rs/Dne9DnxCRcWUf-S6CANuLQ/h63/h001.4UX89x51T7SLRqWL-GYmgsnElXwn_X0JHWWaPg5856o
status: published
n_mentions: 5
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
  - "StrictlyVC"
story_id: s48b81827
month: 2026-06
enriched: true
importance: 3
---

# Worldpay outage leaves UK pubs and shops cash-only during England match

> [!info] 2026-06-25 · 5 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments, StrictlyVC

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] Cash Only. Worldpay's Outage Hits Pubs Mid-Match in England

[Connecting the Dots in Fintech] Worldpay attributed the fault to a third-party power problem rather than any failure of its own platforms.

[Connecting the Dots in Fintech] 🇬🇧 Worldpay outage leaves pubs and shops scrambling for cash during England match. The outage disrupted contactless payments across parts of the UK before services were restored, highlighting the growing dependence of consumers and businesses on digital payment infrastructure.

[Connecting the Dots in Payments] 🇬🇧 Worldpay outage leaves pubs and shops scrambling for cash during England match. The outage disrupted contactless payments across parts of the UK before services were restored, highlighting the growing dependence of consumers and businesses on digital payment infrastructure.

[StrictlyVC] The World Cup’s three-minute hydration breaks have become high-speed beer runs for fans, turning a safety measure FIFA says is needed for summer heat into a “very American” sprint for the concession stand.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/2bea15c6>
- <https://www.connectingthedotsinfin.tech/r/3a5df0bb>
- <https://www.connectingthedotsinfin.tech/r/cb18f4a7>
- <https://www.connectingthedotsinpayments.com/r/787d8f73>
- <https://elink22c.strictlyvc.com/ss/c/u001.Lk2l_GQ_9y3_OeVsl2E52hugD7aQjoXn8AIz0S04U3ir_nzXiPl1AhclafZEo0LJXZx2OwN1Hb1RfJ3P_RSoGMQq5z9hZooudBFOR_-xmQkn5KV1fkw_g82p-ktF6zZEXcmYTuO_nKHqjw49J4v0N_Nszu1SX29bk7_K31urJsRqDJGGPtwgzSJOGiCPaI1f-mzKXVRPCqIIYZ8UpgCBFf-_F9Zxjkyo5sQz4ThoU1OMDaaJ8lg0dAQC4Qf2mKYW717oU7eWGmC4fe7JDrlfuDJbBvfAhpeGCFrK-cZrH4I/4rs/Dne9DnxCRcWUf-S6CANuLQ/h63/h001.4UX89x51T7SLRqWL-GYmgsnElXwn_X0JHWWaPg5856o>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Worldpay outage leaves UK pubs and shops cash-only during England match
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **23 June 2026** (evening, BST), Worldpay's UK card-acquiring/authorisation suffered a multi-hour outage that hit just as fans settled in for **England 0-0 Ghana** (FIFA World Cup, Group L) — one of the busiest trading nights of the year for pubs. Tills and contactless terminals failed at branches of **Tesco** and **Morrisons** and across hospitality; many venues posted "cash only" notices; Downdetector spiked to ~1,000+ reports clustered at Tesco. Service was "restored to some platforms within hours" with engineers working on the rest.
- **Stated cause (vendor framing — treat skeptically):** Worldpay blamed a **third-party "power grid disruption"**, *not* its own platform — "intermittent transaction authorisation issues and tokenisation request errors on some Worldpay platforms." 
- **Second, narrower issue:** Worldpay separately disclosed a **one-day funding/settlement delay** for "a small subset of merchants on the Worldpay Total platform" (24 June → 25 June). Distinct from the authorisation outage; don't conflate.
- **Why the framing matters → de-PR:** "External power problem" is Worldpay's own characterization with **no independent National Grid / UK Power Networks confirmation cited**. Even if a grid event was the trigger, a multi-hour merchant-facing authorisation failure implies a **failover/resilience gap inside Worldpay's own estate** — a power blip should be absorbed by redundant data centres. The PR anchors blame outward; the resilience question is internal. **(analysis)**
- **Open/unconfirmed:** exact end time (StatusGator logged only a ~28-min component "warning", far short of merchant-reported "several hours"); transaction/revenue-loss counts; exact kickoff/outage clock time (8pm vs 9pm BST reported).

## [1] Competitors / peers — comparable UK payment/banking outages
This is one in a dense run of UK payment-infrastructure failures, which is what gives an otherwise routine outage its weight:
- **Visa EU/UK, 1 Jun 2018** (~10 hrs): 51.2M tx initiated, **5.2M failed** (~9%); a rare datacentre switch fault that blocked failover — the closest analogue to "single point of failure in a card rail."
- **TSB migration, Apr 2018**: 5.2M customers; **£48.65m fine** (FCA+PRA, Dec 2022). The benchmark for regulator punishment of resilience failure.
- **Visa-network retailer outage, 11 Jul 2024**: Sainsbury's/Asda/M&S/McDonald's hit.
- **Sainsbury's + Tesco, 16 Mar 2024**: faulty overnight software update; deliveries cancelled, contactless down.
- **Barclays, 31 Jan–2 Feb 2025** (~3 days, payday weekend): 56% of online payments failed; **£5m–£12.5m** redress, no FCA fine. Mainframe software fault.
- **AWS us-east-1, 20 Oct 2025** (~15 hrs): hit Lloyds/Halifax/BoS, HMRC, DWP — see [[AWS outage disrupts UK banks' online services]]. The "cloud concentration" cousin of this story.
- **Why the cluster matters → second order:** each incident has a *different* root (grid, mainframe, software update, cloud DNS, card-network switch) but the *same* second-order signal — **UK retail/hospitality has near-zero cash fallback**, so any single processor/rail/cloud failure cascades to "cash only" in minutes. The systemic risk is concentration + cashlessness, not any one vendor's bug. **(analysis)**

## [2] Company history / fit
Worldpay is a UK-rooted acquiring giant with a turbulent ownership history: FIS sold ~55% to **GTCR** (~$18.5bn valuation, closed Jan 2024); then **Global Payments agreed to acquire Worldpay** (~$24.25bn), **UK CMA cleared** it Oct 2025 — see [[Global Payments' $22.7B Worldpay acquisition cleared by UK CMA]] and [[UK CMA opens probe into Global Payments' $24bn Worldpay deal]]. **The deal CLOSED on 9 January 2026** — so at the time of the outage **Worldpay is a Global Payments subsidiary** (GTCR retains ~15% of *Global Payments* equity, not of Worldpay).
- **Why it matters → fit:** the outage lands ~5.5 months into a **post-merger integration** of two mega-acquirers — exactly the window when platform consolidation, migration and cost-out raise operational-resilience risk (cf. TSB). Worldpay has been actively expanding (Santander UK distribution — [[Santander UK to offer Worldpay solutions to clients]]; UnionPay 3DS — [[UnionPay and Worldpay enable ExpressPay and 3DS e-commerce solution]]; embedded finance — [[Worldpay expands platforms offering for embedded finance]]; stablecoin payouts — [[Worldpay to enable stablecoin payouts for global businesses]]). The growth/integration agenda sits in tension with keeping legacy UK rails bulletproof. **(analysis)**

## [3] Novelty / value-add / traction
Low novelty as an *event* — it's a transient outage, not a product, and (per the research) there is **no verified prior major Worldpay UK outage** to call this a "pattern" yet (open). What's genuinely informative:
- The **anti-PR delta**: vendor blames external power; no independent grid confirmation → the substantive story is **internal failover adequacy**, not the trigger.
- The **scale signal**: named tier-1 grocers (Tesco, Morrisons) + nationwide hospitality on the single busiest match-night demonstrates how concentrated UK acquiring is and how thin the cash backstop has become.
- **Who captures the cost:** merchants eat the lost-sales risk; the processor faces reputational and (potentially) regulatory cost but no published redress. The asymmetry — merchants bear downtime, acquirer bears little — is the durable structural point. **(analysis)**

## [4] What's next / market sentiment
- **Regulatory backdrop is the live wire.** UK operational-resilience rules hit full-compliance 31 Mar 2025; the **Critical Third Parties (CTP) regime** went live 1 Jan 2025 (FCA PS24/16; BoE/PRA) but only bites once **HM Treasury designates** a firm — **whether Worldpay/Global Payments is a designated CTP is open/unconfirmed**. New **operational-incident & third-party reporting** Policy Statements landed **March 2026**. The **Treasury Committee** already found (Mar 2025) that nine major banks logged **≥803 hours (~33 days)** of unplanned outages over ~2 years — political appetite to scrutinise payment IT failures is high.
- **No Treasury Committee / FCA statement on the June 2026 Worldpay event has been found** — open.
- **Why the market goes this way → second order:** the steady drumbeat (Visa 2018, TSB, Barclays 2025, AWS 2025, now Worldpay 2026) plus the cashless tipping point makes **CTP designation of large acquirers/processors increasingly likely**, which would push resilience capex onto firms like Worldpay precisely as they're cost-cutting through the Global Payments merger. **(hypothesis)** Counterintuitive effect: consolidation into fewer mega-processors raises *systemic* fragility even as it improves each firm's scale economics.

## Sources
- Internal corpus (wikilinks above): [[Global Payments' $22.7B Worldpay acquisition cleared by UK CMA]], [[UK CMA opens probe into Global Payments' $24bn Worldpay deal]], [[AWS outage disrupts UK banks' online services]], [[Santander UK to offer Worldpay solutions to clients]], [[UnionPay and Worldpay enable ExpressPay and 3DS e-commerce solution]], [[Worldpay expands platforms offering for embedded finance]], [[Worldpay to enable stablecoin payouts for global businesses]].
- https://bmmagazine.co.uk/news/worldpay-outage-uk-card-payments-england-match/
- https://paymentexpert.com/2026/06/24/worldpay-outage-uk-england-ghana
- https://www.americanbanker.com/payments/news/worldpay-suffers-payments-outage-during-world-cup
- https://uk.news.yahoo.com/card-payments-fail-worldpay-goes-214956982.html
- https://statusgator.com/services/worldpay · https://status.worldpay.com/
- Deal close: https://paymentexpert.com/2026/01/12/global-payments-worldpay-deal/ · https://www.prnewswire.com/news-releases/gtcr-completes-sale-of-worldpay-to-global-payments-302658108.html · https://www.sec.gov/Archives/edgar/data/0001123360/000110465926002705/tm262856d1_8k.htm
- Prior outages: https://www.computerweekly.com/news/252443325/Visa-reveals-rare-datacentre-switch-fault-as-root-cause-of-June-2018-outage · https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings · https://www.fintechfutures.com/bankingtech/barclays-set-to-pay-out-millions-in-customer-compensation-after-it-outage · https://paymentexpert.com/2024/07/11/card-outages-uk-retailers/
- Regulatory: https://www.fca.org.uk/publications/policy-statements/ps24-16-operational-resilience-critical-third-parties-uk-financial-sector · https://www.regulationtomorrow.com/2026/03/fca-pra-and-boe-issue-policy-statements-on-operational-resilience/ · https://committees.parliament.uk/committee/158/treasury-committee/news/205611/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Did the outage start 23 or 24 June?** → **23 June 2026** (UK reporting + England v Ghana match date). American Banker's "June 24" is a US-timezone/editorial artifact.
2. **"Third-party power" or Worldpay's own platform?** → Vendor blames an external power grid disruption. **No independent grid-operator (National Grid / UK Power Networks) confirmation cited — open.** Multi-hour merchant impact implies an internal failover gap regardless of trigger.
3. **Which match / result?** → England 0-0 Ghana, World Cup Group L, 23 June 2026. Confirmed.
4. **Exact duration / end time?** → "Several hours" per merchants; StatusGator shows only a ~28-min component "warning". Full end time **open**.
5. **How many merchants / transactions affected?** → No transaction-count or revenue figure published. Named: Tesco, Morrisons branches + pubs/bars; 1,000+ Downdetector reports. **Open.**
6. **Who owns Worldpay now?** → **Global Payments** — acquisition CLOSED **9 Jan 2026**. GTCR retains ~15% of *Global Payments*, not of Worldpay. The pre-2026 "GTCR-owned" framing is stale. Confirmed.
7. **Does post-merger integration explain the fragility?** → Outage is ~5.5 months into Global Payments/Worldpay integration — a classic resilience-risk window (cf. TSB). **(hypothesis — no root-cause link confirmed.)**
8. **Was a separate funding/settlement failure conflated with the outage?** → Yes, two distinct issues: (a) authorisation/tokenisation errors during the match; (b) a one-day funding delay for "a small subset of merchants on Worldpay Total" (24→25 June). The second is narrower. Don't merge them.
9. **Any verified prior major Worldpay UK outage?** → **None verified (2023–25) — open.** So "Worldpay has a pattern" is not yet supported.
10. **Is Worldpay/Global Payments a designated UK Critical Third Party?** → **Open/unconfirmed.** CTP regime live since 1 Jan 2025 but bites only on HM Treasury designation; no Worldpay designation confirmed.
11. **Any regulator / Treasury Committee response to this specific event?** → **None found — open.** But Treasury Committee scrutiny of bank/payment IT outages is active (Mar 2025 finding: ≥803 hrs of outages across 9 banks).
12. **Is this systemically novel, or a routine transient outage?** → Event itself is low-novelty; the durable signal is UK acquiring concentration + near-zero cash fallback, not Worldpay specifically. **(analysis)**
13. **Who bears the cost?** → Merchants eat lost match-night sales; processor faces reputational/regulatory exposure but no published redress. Asymmetry is the structural point.
14. **Does the Global Payments deal change resilience incentives?** → Larger combined estate + cost-out pressure cuts both ways: scale vs integration risk and systemic concentration. **(hypothesis.)**

Importance: 3/5 — A high-visibility, real-world consumer-facing outage hitting tier-1 UK grocers and nationwide hospitality on a marquee match-night, adding to a politically charged run of UK payment IT failures (Barclays, AWS, Visa) with live CTP/operational-resilience regulation in play. But it is a transient outage with no product/structural novelty, no confirmed root cause (vendor blames external power, unconfirmed), no published impact numbers, no regulator response yet, and no verified prior Worldpay pattern — so it is consequential-but-routine, not a 4–5.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Включено в дайджест [[Posts/2026-06-25]] (2026-06-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Worldpay sits in UK/global **merchant acquiring** — the rails that route card auth from POS terminal to scheme to issuer. The UK is the largest, most competitive acquiring market in Europe; incumbents (Worldpay, Barclaycard, Global Payments/Fiserv, Elavon) coexist with digital-native challengers (Stripe, Adyen, Checkout.com, Dojo, SumUp) (per Mordor Intelligence / CMA decision, as of Nov-2025). Structure: **consolidating** — on 17-Apr-2025 Global Payments agreed to buy Worldpay from GTCR (55%) and FIS (45%) for **$24.25bn**; CMA cleared it 20-Oct-2025; close expected H1-2026 (per Global Payments IR / SEC 8-K). Why now: the outage hit during England vs Ghana at the 2026 World Cup — a peak trading night — and lands while UK **FCA operational-resilience rules** are live (firms had to operate "important business services" within set impact tolerances by 31-Mar-2025; per FCA / Sidley). Second-order: every public card outage now reads against a regulatory yardstick, not just brand reputation.

**Competitive landscape.** Sector KPIs: TPV/processed volume, take rate, per-transaction margin, and — increasingly load-bearing — **uptime**. Checkout.com publicly markets "99.999%" uptime as its trust pitch (per [[Connecting the Dots Checkout.com publishes 2025 annual letter]]); reliability is becoming a competitive axis, not table stakes. Recent peer moves: Barclays put **GBP 400m** into modernising Barclaycard's stack (Mar-2025, w/ Brookfield) precisely because legacy tech was bleeding share to Adyen/Stripe/Dojo (per Business of Payments). Worldpay's position: scale incumbent, **catching up** on modernity vs cloud-native peers; moat = installed merchant base + scheme relationships (switching costs), but that base is exactly what an outage exposes. Note: Worldpay blamed a **third-party UK power-grid disruption**, not its own platform — a deflection to watch, since resilience rules judge the *service*, not the root-cause owner (analysis).

**Comps & multiples.** Deal/peer multiples for the acquiring sector:
- **Global Payments / Worldpay deal** — ~**8.5x** adj. EV/EBITDA (incl. some run-rate synergies), on $24.25bn (per Global Payments IR).
- **Global Payments (GPN)** — mkt cap ~**$18.0bn** (19-Jun-2026); EV/EBITDA cited ~9–11x across sources (per stockanalysis / GuruFocus) → range, not a clean figure.
- **Adyen** — mkt cap ~$36bn, EV ~$24bn, **8.1x EV/Revenue**, **15.2x EV/EBITDA** (24-Apr-2026; per multiples.vc) on 2025 net revenue $3.10bn / processed volume €1,394.3bn.
Read: legacy acquirers (GPN, Worldpay deal) trade ~**8.5–11x EV/EBITDA**; cloud-native Adyen carries a clear premium (~15x EBITDA, ~8x revenue) — the market pays up for the modern, higher-uptime stack. In-line, no outlier breach. Worldpay standalone post-2023 financials not separately public → **[UNSOURCED]** for a Worldpay-specific multiple. Internal comps (outage precedents): [[Monzo hit by major outage disrupting payments]] · [[AWS outage disrupts UK banks' online services]] · [[PayPal outage freezes billions in German payments]] · [[ACI Worldwide UK payments infrastructure needs a reset]].

**Risk flags.**
1. **Single-point-of-failure / concentration.** One acquirer's fault froze card payments across many UK merchants (Tesco branches, pubs) — a systemic-looking dependency that is exactly what FCA impact-tolerance rules target; a repeat invites regulatory scrutiny (why: harm now measured against a legal yardstick, not just brand).
2. **Third-party rails dependence + deflection.** Worldpay pinned it on a power-grid issue. Even if true, merchants experienced acquirer downtime; "not our platform" doesn't reset impact-tolerance clocks (why: liability/PR gap between root cause and customer-facing service).
3. **Integration/execution risk into the merger.** Outage lands mid-way through the Global Payments acquisition (H1-2026 close); operational fragility during a mega-integration raises the bar on resilience spend and could surface in regulatory/customer-retention terms (why: stressed systems + transition = elevated failure odds) (analysis).

**What this changes (idea-lens).** Uptime is re-rating from cost line to **competitive moat** in acquiring: cloud-native players (Adyen at ~15x EBITDA) get rewarded, legacy incumbents get punished by both regulators and merchants for downtime. Falsifiable thesis: repeated high-profile acquirer outages accelerate SME/enterprise churn toward Stripe/Adyen/Dojo and pressure Worldpay/Barclaycard share. Trigger to watch: FCA/PSR commentary on this incident, churn data post-merger, and whether Worldpay publishes a root-cause/impact-tolerance breach disclosure (analysis). Thesis breaks if the outage proves purely exogenous (grid) and merchants stay put.

Sources: https://www.americanbanker.com/payments/news/worldpay-suffers-payments-outage-during-world-cup · https://bmmagazine.co.uk/news/worldpay-outage-uk-card-payments-england-match/ · https://paymentexpert.com/2026/06/24/worldpay-outage-uk-england-ghana · https://investors.globalpayments.com/news-events/press-releases/detail/469/global-payments-announces-agreements-to-acquire-worldpay · https://www.fca.org.uk/firms/operational-resilience · https://www.sidley.com/en/insights/newsupdates/2025/01/uk-operational-resilience-rules-are-you-ready-for-31-march-2025 · https://www.mordorintelligence.com/industry-reports/united-kingdom-payment-gateway-market · https://businessofpayments.substack.com/p/business-of-payments-april-2025 · https://multiples.vc/public-comps/adyen-valuation-multiples · https://stockanalysis.com/stocks/gpn/market-cap/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
