---
title: "Yandex Pro couriers flood chats with payout complaints"
date: 2026-10-21
retrieved: 2026-10-21
tags:
  - company/yandex
  - industry/payments
  - region/ru
  - type/commentary
sources:
  - https://vk.ru/yandex_drivers
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s6153e8d0
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Yandex Pro couriers flood chats with payout complaints

> [!info] 2026-10-21 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] 19 октября издание «Рахмат» опубликовало обзор жалоб исполнителей из профессиональных чатов, и их поток не останавливается до сих пор. В частности, в сообществе «Яндекс Про» в VK. Проблемы возникают на разных этапах расчётов:

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://vk.ru/yandex_drivers>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 19 Oct 2026 the outlet «Рахмат» published a round-up of courier/driver complaints pulled from professional chats (notably the VK community «Яндекс Про»), and per Финтехно the flood of complaints has not stopped since. The grievances cluster around the *payout/settlement mechanics* of the Yandex Pro gig app: opaque "corrections" (корректировки — minus lines for late/undelivered orders), "stop-payments" (temporary pauses in transfers for partner-fleet couriers who skip slots), referral-bonus cuts applied mid-work, automatic НПД self-employment tax withholding, and reduced payment visibility on the in-app "Карта Про" vs an external bank card. This is a *structural/chronic* complaint cluster about how couriers get paid — the single listed source is the VK group (<https://vk.ru/yandex_drivers>), no primary-source full text was ingested.

**[1] Why it matters (fintech lens).** Yandex Delivery/Eda is one of Russia's largest gig-payment payers: ~33k couriers executed Eda+Lavka orders in Dec 2025 (34k a year earlier). Couriers are not employees — they contract as self-employed (НПД, 4% on income from individuals / 6% from legal entities) or ИП under civil-law contracts, so Yandex operates a high-volume mass-payout rail: daily settlement (same-day for Alfa/Sber/T-Bank/VTB/Tochka cards, weekday-only for others), automatic tax computation/withholding, weekly income reports, and the proprietary «Карта Про» wallet. Payout trust is the labour-supply moat in gig delivery; chat-driven complaint contagion about opaque deductions directly threatens courier retention and the platform's float/withholding model.

**[2] Prior / adjacent coverage (internal).** This is a *different episode* from the Oct 12–13 infrastructure story: [[Yandex Pay still down after Yandex data-center outages]] (s2b8b85a4) covered payout *delays* caused by drone attacks on Yandex data centres (Yandex Taxi/Pro drivers unable to withdraw; ~7k complaints in a day; Yandex later resumed payouts). The present item is about *recurring, structural* settlement grievances, not the outage. Adjacent Yandex-fintech context: [[Yandex NewPay added to Russian installment-services registry]] (sfcae7ef5 — Yandex building out its BNPL/payment stack) and the broader delivery operation in [[Yandex Lavka expands robotic delivery to 130 dark stores]] (sced95f30). Yandex's fintech leader Dmitry Pirogov is named in the outage note.

**[3] Numbers / mechanics.** Scale: ~33k Eda+Lavka couriers (Dec 2025). Tax: НПД 4%/6% auto-withheld. Payout cadence: daily (ex-weekends for non-partner-bank cards); weekly income report issued Tuesdays. Deduction types flagged: корректировки (per-violation minus lines, disputable within 30 days via support chat), стоп-выплата (transfer pause for partner-fleet couriers inactive several days; does not apply to directly-onboarded self-employed), referral-bonus reductions (reportedly >2x cuts post-registration). Complaint channel: in-app Yandex Pro support chat is the only working support route. No disclosed episode-specific complaint count for the Рахмат round-up.

**[4] Open threads / what to watch.** (a) Is this a genuine spike or ambient background noise amplified by the Рахмат article? (b) Any regulatory/labour angle — self-employed courier payment protections, ЦБ/ФНС scrutiny of НПД withholding, platform-liability debate? (c) Does it overlap in time with the data-center outage aftermath (couriers conflating outage delays with structural corrections)? (d) Yandex official response / any payout-policy change. (e) Whether «Карта Про» visibility gap pushes couriers to external bank cards (deposit-flight from Yandex's wallet).

Sources: [[Yandex Pay still down after Yandex data-center outages]]; [[Yandex NewPay added to Russian installment-services registry]]; [[Yandex Lavka expands robotic delivery to 130 dark stores]]; <https://vk.ru/yandex_drivers>; <https://kurerhub.ru/ru/blog/stop-vyplata-kurera>; <https://kyrieros.ru/blog/skolko-kurerov-v-iandeks-ede/>; <https://pro.yandex.ru/ru-ru/moskva/knowledge-base/courier/dohod/avtouplata-nalogov>; <https://vc.ru/claim/3032385-yandeks-pro-i-referalnye-bonusy-dlya-kuryerov>; <https://ru.themoscowtimes.com/2026/10/13/iz-za-atak-bpla-nadata-tsentri-yandeks-taksi-zaderzhal-viplati-voditelyam-a208522>.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge**

1. *Is this the same story as the Oct 12–13 Yandex Pay outage?* — No (answered). The outage note (s2b8b85a4) is drone-attack-driven payout *delays*; this is chronic *structural* settlement complaints (corrections, stop-payments, referral cuts). Fresh, but temporal overlap risks reader conflation — must disambiguate.
2. *Is there any hard number for "the flood of complaints"?* — Open. No episode-specific count. The ~7k/day figure belongs to the outage, not here; do not transplant it.
3. *Who/what is «Рахмат»?* — A publication/outlet (per Финтехно framing) that compiled the complaints; not a primary regulator or Yandex. Single-sourced via a VK group link. Low source authority.
4. *Is the complaint volume real or amplified by one article?* — Open. Chat-aggregation + a single round-up could manufacture the appearance of a surge.
5. *Does "Yandex Pro couriers" conflate drivers and couriers?* — Yandex Pro is the unified app for taxi drivers AND Eda/Lavka/Delivery couriers; the headline says couriers but grievances may span both cohorts.
6. *НПД tax withholding — is this a Yandex fault or statutory?* — Partly statutory: auto-computed НПД is by design. Framing it as a "complaint" conflates legal withholding with discretionary deductions (корректировки/стоп-выплата), which are the real grievance.
7. *Is "стоп-выплата" even a cut?* — No; it is a transfer pause for inactive partner-fleet couriers, not a deduction, and does not touch directly-onboarded self-employed. Easy to overstate.
8. *Scale check — ~33k couriers?* — That counts Eda+Lavka together (Dec 2025); Delivery/Taxi not included, so total Yandex Pro payees are larger. Use as a floor, not a ceiling.
9. *Any regulatory/ЦБ/ФНС action?* — Open / none found. No evidence of a formal probe into courier payout practices tied to this episode.
10. *Fintech relevance vs labour-dispute?* — Borderline. The payment-rail/float/withholding angle is genuinely fintech; the headline reads as a labour-grievance story. Importance hinges on the settlement-mechanics framing.
11. *Did Yandex respond officially?* — Open. No disclosed company statement on the structural complaints (distinct from Pirogov's outage comments).
12. *Deposit-flight signal?* — Hypothesis only: couriers advised to use external bank cards over «Карта Про» for payment visibility; no data on actual wallet-abandonment.
13. *Could this be seasonal/recurring?* — Likely; courier payout complaints recur on vc.ru/forums year-round. Novelty is marginal.
14. *Primary-source gap.* — Zero ingested full text; everything rests on secondary blogs + a VK community link. Verification is weak.
15. *Market impact on Yandex (MOEX: YDEX)?* — Negligible; a courier-chat complaint round-up is not a market-moving event.

Importance: 2/5 — A recurring, single-sourced (VK group + «Рахмат» round-up) structural-complaints story with no hard numbers, no regulatory action, and no company response. Fintech hook (mass gig-payout rail, НПД auto-withholding, «Карта Про» wallet trust, retention float) is real and distinguishes it from the Oct outage note, but novelty and verifiability are thin.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a RU gig-economy delivery/ride-hailing payout story, not a product launch — couriers on Yandex Pro (the unified driver/courier app for Yandex's O2O services — taxi, Eda food delivery, Lavka quick-commerce, Delivery) report recurring problems being paid out across multiple stages of settlement. Sector size: Russia's online food-delivery market was ~$9.3bn in 2025, projected to ~$15.2bn by 2034 (~5.5% CAGR 2026–34) (per IMARC, via imarcgroup.com, as of 2025). Yandex is the dominant platform — Yandex Eda holds an estimated ~40–50% share of platform-aggregated delivery (per grokipedia/secondary, as of 2024) `(analysis — share figures are secondary, not IR-confirmed)`. Structure: the delivery/ride layer is a two-sided marketplace where value accrues to whoever owns demand aggregation + the payout rail; couriers are overwhelmingly self-employed (samozanyatye), so platforms bear no employment liability but carry the reputational/regulatory risk of being seen as a de-facto employer. Why now: the complaints surfaced via a 19 Oct Rakhmat review of professional chats (incl. the "Yandex Pro" VK community) and are "not stopping" — distinct from, but overlapping with, the Oct 8–11 data-center outages that also froze Yandex Pro withdrawals (drivers/couriers unable to pull earnings) (per Meduza/CNN, as of Oct 2026). Payout-float dynamics: a platform that holds courier earnings for days of "verification" earns float and preserves liquidity, which is precisely the friction couriers are flagging.

**Competitive landscape.** KPIs this subsector runs on: GMV/number-of-orders, take rate, courier payout-per-order, and courier retention/supply (the binding constraint — Yandex itself cites a "courier shortage," pushing its 1,000+ rover fleet, Q2 2026, per CNews). Key players: Yandex Eda/Lavka/Delivery (incumbent, ~40–50% share), Samokat (quick-commerce, VK/Sber-linked), Cooper (ex-SberMarket), plus FoodBand/Elementaree in meal-kits. Basis of competition: supply density (how many couriers you can field) + consumer selection — price/payout to couriers is the lever to keep supply, so cutting payout per order directly threatens the KPI that matters most. Recent moves: historical precedent for exactly this complaint — after Yandex absorbed Delivery Club, couriers protested cuts from ~₽110 to ~₽70/order and struck for labour contracts (per Jacobin, 2023). Position: Yandex is the clear leader in RU delivery/ride, so its payout terms effectively set the market floor — but leadership + self-employed workforce = concentrated reputational exposure. Moat: demand aggregation + the Yandex Pro single-app lock-in across taxi/food/grocery (switching costs for couriers who juggle multiple Yandex gigs) `(analysis)`.

**IR grounding (PRIMARY evidence — MKPAO Yandex, MOEX-listed).** The relevant reporting bucket is Yandex's **E-commerce, Mobility & Delivery (EMD)** segment — the O2O businesses that these couriers deliver for. Group Q1 2026: revenue **₽372.7bn, +22% YoY**; adjusted EBITDA **₽73.3bn, +50%**; adjusted net profit **₽34.7bn** (more than doubled) (per Yandex Q1 2026 press release, as of 2026-04-28, url fallback https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf — segment lines not machine-readable from the PDF; figures cross-checked via secondary press). Segment scale (FY2024 anchor, secondary): EMD earned **~₽592bn in 2024 (~54% of group revenue)**, of which mobility ~₽228bn (per Statista, via statista.com, as of 2024); foodtech+e-commerce revenue grew **+46% YoY to ₽102.8bn in Q2 2025** (per IR/secondary); Yandex Eda alone ₽84.8bn FY revenue +64% YoY with 4.6m active users / 14,000+ restaurants across 112 cities (Q4 2024 cadence, secondary). Read-through: the courier payout line sits inside a segment that is >50% of a group growing group revenue +22% and EBITDA +50% — i.e. the economics being squeezed at the courier level are funding segment profitability, which is the crux of the labour-vs-margin tension.

**Comps & multiples.** Internal comps (same-group/same-sector, via base):
- [[Yandex Lavka expands robotic delivery to 130 dark stores]] — robotisation framed as answer to the "courier shortage"; 2026 rover fleet 1,000+ (Q2). Direct hedge against the exact payout/supply friction here.
- [[Yandex Pay still down after Yandex data-center outages]] — Oct 8–11 outage also froze Yandex Pro withdrawals; overlapping (but separate) payout-availability failure.
- [[Yandex NewPay added to Russian installment-services registry]] — Yandex's fintech/BNPL contour; shows the group owns its own payment/settlement rails (Yandex Pay, Split, NewPay), so courier payout friction is an internal-rail design choice, not a third-party dependency.

Trading multiples: Yandex (MOEX: YDEX) is the listed entity; a clean, free EV/Revenue or EV/EBITDA with publicly verifiable current EV is **not sourceable here → no data / `[UNSOURCED]`**. External gig-economy comps (DoorDash, Delivery Hero, Deliveroo) trade in different geos/currencies and fail the comparability test (sanctions-isolated RU market, ruble, state-adjacent) → **comparison not computed, qualitative only.** No deal/valuation metric attaches to this note, so no multiple arithmetic applies.

**Risk flags.**
1. **Labour/reputational risk** — repeated, unresolved payout complaints from self-employed couriers invite regulatory reclassification pressure (de-facto employment) and union/strike precedent (2023 Delivery Club strikes); a platform at ~40–50% share is the obvious target. Second-order: forced employment terms would raise the EMD segment's cost base that currently drives +50% EBITDA growth.
2. **Payout-rail / platform-float dependence** — couriers depend entirely on Yandex's internal settlement stack (Yandex Pay/Pro) with no alternative; the same stack just failed for >24h in the Oct outage. Multi-stage settlement delays double as a float benefit to the platform, aligning Yandex's incentive against fast payout — a structural, not incidental, friction.
3. **Supply concentration** — courier supply is the binding growth constraint (hence robotisation); sustained payout grievances erode the very supply the segment's GMV depends on, especially amid a cited courier shortage.

**What this changes (idea-lens).** `(analysis)` Not a one-off: this reads as the labour-cost side of Yandex squeezing EMD-segment margins to fund group-level profit growth, with robotisation (Lavka rovers) as the long-run answer to both payout grievances and supply scarcity. Falsifiable thesis: if payout complaints persist into 2027 without resolution, expect (a) regulatory/samozanyatye-reclassification moves in RU and/or (b) accelerated rover deployment as Yandex substitutes capex for contested courier opex. What breaks the thesis: a public Yandex payout-terms fix or faster settlement SLA that quiets the chats. Trigger to watch: Yandex's next EMD segment EBITDA margin vs courier-cost disclosure, and any Bank of Russia / Mintrud signal on gig-worker payout timing.

Sources: https://www.imarcgroup.com/russia-online-food-delivery-market · https://grokipedia.com/page/Yandex_Eda · https://meduza.io/en/feature/2026/10/12/ukraine-knocked-out-key-yandex-data-centers-the-fallout-is-being-felt-across-russia · https://jacobin.com/2023/02/courier-union-strike-food-delivery-russian-tech · https://www.statista.com/statistics/225714/annual-revenue-of-yandex-by-segment/ · https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Earnings read (Yandex / МКПАО «Яндекс», MOEX: YDEX) — Q2 2026, reported 29 Jul 2026.** Verdict: **BEAT** on EBITDA/profit, in-line-to-soft on top-line. Note the gap vs the news angle: the courier-payout complaints sit inside the very unit (Delivery) that is still the group's only loss-making piece, even as the broader E-commerce block hits breakeven.

- **Group:** revenue RUB 386.3bn, +16% YoY (decelerating from the 30%+ pace of 2024–25 and below the FY-2026 ~20% growth guide). Adjusted EBITDA RUB 88.9bn, +35% YoY; margin 23.0%, +3.1pp YoY. Adjusted net profit RUB 47.6bn, +56% YoY. FY-2026 guidance: revenue growth ~20%, adjusted EBITDA ~RUB 350bn, capex 10–12% of revenue.

- **Urban Services block (where Mobility + Delivery sit):** revenue RUB 215.6bn, +18% YoY; adjusted EBITDA RUB 34.4bn, +168% YoY (≈2.7x), margin up ~9pp to ~16% — the single biggest driver of the group EBITDA beat.
  - **Ridetech (Mobility):** revenue RUB 77.6bn (+15%), GMV RUB 439.3bn (+10%), adjusted EBITDA RUB 35.0bn (+39%), margin 8.0% of GMV (+1.6pp). Strongly profitable; the block's cash engine.
  - **E-commerce (Market/Lavka/Eda):** revenue RUB 123.7bn (+20%), GMV RUB 295.7bn (+2% — a sharp GMV-growth slowdown), adjusted EBITDA RUB +0.4bn — **first-ever operational breakeven**, the quarter's headline.
  - **Delivery / O2O logistics:** revenue RUB 21.2bn (+7%, the slowest-growing line), GMV RUB 58.3bn (+21%), adjusted EBITDA **-0.9bn (still loss-making)**; management flagged margin improvement to ~5.8% of GTV (+1.2pp).

- **Tie to the courier-payout-complaints angle (gig-labor cost pressure / delivery-unit margins):** Yandex does not disclose a courier-cost line, but the segment math is the thesis-flag. Delivery is the only sub-segment still printing negative EBITDA (-0.9bn), and its revenue growth (+7%) badly lags its GMV growth (+21%) — i.e. take-rate/revenue per order is compressing even as volumes rise. That is exactly the pressure point where a company squeezes variable gig-labor (courier) payouts to protect a razor-thin delivery margin on its path to breakeven — consistent with the "Яндекс Про" courier complaints about recalculated/cut payouts. The group-level EBITDA beat is being carried by Ridetech and the E-commerce breakeven, which gives management cover to keep tightening Delivery's cost base rather than pass more to couriers. Total workforce -2% YoY (92,060) alongside +3% core staff also signals cost discipline in the lower-skill/operational base. Watch Delivery EBITDA and the revenue-vs-GMV growth spread next quarter: if the payout squeeze is structural, Delivery should inch toward breakeven; if complaints force payouts back up, the -0.9bn drag widens and dents the block's 168% EBITDA story.

_Primary: Yandex Q2 2026 MSFO release (ir.yandex.ru, 29 Jul 2026); figures cross-checked via content-review.com, oborot.ru, rb.ru. ir_latest.json lags at Q1 2026, so Q2 figures taken from the latest MOEX/IR release + press. No courier-specific cost disclosure exists in the filing; the labor-cost read is inferred from segment unit economics._
<!-- /enrichment:earnings_review -->
