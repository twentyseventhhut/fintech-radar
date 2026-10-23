---
title: "Ecommpay partners Dolphin Dynamics to simplify travel payments"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/ecommpay
  - company/dolphin-dynamics
  - industry/payments
  - region/global
  - type/partnership
sources:
  - https://ecommpay.com/press-room/ecommpay-dolphin-dynamics-partnership-travel-payments
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s2628d834
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Ecommpay partners Dolphin Dynamics to simplify travel payments

> [!info] 2026-10-23 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Ecommpay partners with Dolphin Dynamics to simplify travel payments. The integration gives travel agencies and tour operators access to multi-currency payments, local payment methods and fraud-prevention tools

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://ecommpay.com/press-room/ecommpay-dolphin-dynamics-partnership-travel-payments>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Ecommpay (London-based payment service provider and direct card acquirer, founded 2012) signed a strategic partnership with Dolphin Dynamics (London travel-tech vendor, founded 1994; reservations/CRM/mid-and-back-office software for travel agents, tour operators and TMCs, ~850 client sites / ~13,000 users across 26 countries). The partnership integrates Ecommpay's payment gateway into Dolphin's platform: a customer paying for a booking is redirected to Ecommpay's hosted payment page (so card data stays in Ecommpay's PCI environment), Dolphin then calls Ecommpay's API to retrieve payment status, update the booking and register the payment. Dolphin's travel clients gain multi-currency acceptance (Ecommpay quotes 100+ payment methods, 130-160+ currencies, local acquiring across 150+ countries), local/alternative payment methods, and Ecommpay's risk/authorisation and fraud tooling. Announced 2026-10-22.

**Why structured this way / what it reveals:** This is a channel/distribution deal, not a product launch. Ecommpay is NOT building anything new — it is embedding its existing gateway inside a vertical software vendor to reach travel agents it cannot sell to directly. The "hosted payment page + API status callback" is a standard, years-old PSP integration pattern; the de-PR'd substance is "Dolphin picks Ecommpay as a payments option for its booking software." The PR frames it as "simplifying travel payments," but the concrete win is reconciliation automation (fewer manual tasks) and access to Ecommpay's APM/currency breadth — real but incremental, not novel. No deal value, no exclusivity, no client/volume commitments disclosed.

## [1] Competitors / peers
Travel-payments is a crowded vertical. Direct/adjacent players: **CellPoint Digital** (travel-specialised payment orchestration — airlines/OTAs, interline settlement, multi-currency; shipped a major orchestration platform release and a PayPal integration in 2026 — see [[CellPoint Digital's OSO platform redefines airline payments]], [[Travelsoft Pay partners with Mastercard on travel payments]]); **Nuvei** (broad orchestration + acquiring, 53 markets, added an Israel direct-acquiring licence Oct 2026); **Trust Payments, Travelpay**; cross-border travel-payment tie-ups like [[Worldline and YeePay partner on China cross-border travel payments]], [[dLocal and XanderPay partner on cross-border hotel payments]], [[RateGain and Juspay partner on global travel payments]]. Ecommpay itself keeps stacking travel partners: [[Ecommpay partners humm for travel and retail finance]] (BNPL for travel/retail, Oct 2025) and [[Ecommpay and BridgerPay partner on payment orchestration]] (May 2026).

**Why the landscape is this way / second-order:** Travel payments are structurally hard (high ticket, long booking-to-travel gap, complex refunds/chargebacks, multi-currency, settlement to suppliers), which is why vertical specialists (CellPoint) and APM/currency-broad PSPs compete for the same agents. Ecommpay's position here is **catching-up / parity via distribution**, not technical leadership: it wins by being the embedded default inside Dolphin's installed base rather than by a differentiated travel-payments mechanism. The real contest is who owns the software layer the agent logs into daily — Dolphin owns that relationship, so Ecommpay is the supplier, not the gatekeeper.

## [2] Company history / fit
Ecommpay has run a steady cadence of UK/travel/e-commerce partnership and product news through 2025-26: humm BNPL for travel (Oct 2025), BridgerPay orchestration (May 2026), open-banking suite, network tokenisation, Visa VAMP prep, plus awards/accessibility items (see priors above). It has a dedicated travel-and-hospitality vertical. Dolphin Dynamics is an old, niche but entrenched travel-software vendor (acquired Travelport's Travelwire brand for Nordic mid/back-office) that periodically adds payment rails (it has prior links to other payment providers).

**Why they act this way:** For a mid-market PSP without card-scheme or scale dominance, embedding in vertical ISVs is the cheapest path to transaction volume — you inherit the ISV's merchant base instead of buying it via direct sales. For Dolphin, adding a multi-currency/APM gateway is table-stakes feature parity to keep agents from churning to competitors. The deal fits both sides' structural logic (volume-for-PSP, feature-for-ISV) — which is exactly why it's low-drama and low-novelty.

## [3] Novelty / value-add / traction
Novelty: low. The capabilities (hosted page, multi-currency, APMs, fraud tooling) are standard PSP features Ecommpay already sells; the only "new" thing is the Dolphin integration/distribution channel. Value-add is real but narrow: for Dolphin's agents, automated reconciliation and broader currency/APM coverage inside their existing booking workflow is a genuine operational improvement over manual card-machine/off-platform flows. **Traction: unproven — zero disclosed metrics** (no number of agents live, no GMV/volume, no go-live date beyond "announced"). Treat as announced, not adopted.

**Why value-add is or isn't real / who captures margin:** The durable value accrues to whoever owns the merchant relationship and the data. Here Dolphin owns the agent login and booking record; Ecommpay is the interchangeable payment rail behind a hosted page — easily swapped for another PSP later. So Ecommpay captures transaction fees but remains a commoditised supplier, not a sticky platform, unless the integration becomes exclusive/deep (not disclosed). The margin economics (take-rate, revenue split with Dolphin) are entirely undisclosed — a classic "who's silent" gap.

## [4] What's next / market sentiment
Expect the usual PSP follow-up: case studies/named agents going live if adoption materialises. Watch for (a) any client count or volume disclosure (its absence now is telling), (b) whether this becomes Dolphin's default/exclusive payments option or just one of several. Backdrop: travel-payments M&A and partnership activity is heavy (CellPoint-PayPal, Nuvei licensing expansion, multiple cross-border travel tie-ups in 2025-26), signalling a land-grab for travel-agent payment volume.

**Why the market goes this way / second-order:** As vertical travel ISVs (Dolphin, Travelsoft, RateGain) become the integration surface, PSPs are forced into ISV-embedding deals to stay in the flow — which commoditises the PSP and shifts pricing power to the software vendor and the card schemes. Counterintuitively, "winning" distribution deals can make a PSP more fragile (dependent on the ISV's goodwill and swap-out risk) rather than more entrenched. For Ecommpay specifically, this is one of many incremental channel wins, not a strategic inflection.

## Sources
- Ecommpay press room: https://ecommpay.com/press-room/ecommpay-dolphin-dynamics-partnership-travel-payments
- Financial IT: https://financialit.net/news/payments/strategic-partnership-ecommpay-gives-dolphin-dynamics-travel-clients-access-global
- CFOtech: https://cfotech.co.uk/story/dolphin-dynamics-partners-ecommpay-on-travel-payments
- Dolphin Dynamics news: https://www.dolphind.com/about-us/news/year/2026/
- Ecommpay travel vertical: https://ecommpay.com/industries/travel-and-hospitality/
- Dolphin/Travelwire acquisition: https://www.phocuswire.com/Dolphin-Dynamics-acquires-Travelwire
- CellPoint travel orchestration: https://www.pymnts.com/transportation/travel-payments/2025/cellpoint-debuts-payments-orchestration-tool-airline-travel-sectors/
- Internal priors: [[Ecommpay partners humm for travel and retail finance]], [[Ecommpay and BridgerPay partner on payment orchestration]], [[CellPoint Digital's OSO platform redefines airline payments]], [[Worldline and YeePay partner on China cross-border travel payments]], [[RateGain and Juspay partner on global travel payments]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this actually new, or the activation of an existing relationship?** Open — PR frames it as a new "strategic partnership" announced 2026-10-22; no evidence of a pre-existing live integration, but Dolphin routinely adds payment providers, so this is likely just one more rail option, not a first.
2. **Announced or live?** Announced only. No go-live date, no named first agents live. Treat as announced.
3. **How many of Dolphin's ~850 client sites will actually enable Ecommpay?** Open — zero disclosed. This is the number that would determine real weight; its absence suggests early-stage.
4. **Any transaction volume / GMV commitment?** None disclosed. No volume = no way to size the deal.
5. **Is Ecommpay exclusive or default within Dolphin, or one of several PSPs?** Open/undisclosed — almost certainly non-exclusive, which caps stickiness and leaves swap-out risk.
6. **What's the revenue split / take-rate between Ecommpay and Dolphin?** Silent. Economics undisclosed — the key "who's silent" gap.
7. **Who owns the merchant relationship?** Dolphin (owns the booking software and agent login). Ecommpay is the interchangeable rail behind a hosted page — commoditised supplier position.
8. **What's the precise mechanism delta vs a generic PSP integration?** Essentially none — hosted payment page + API status callback is a standard PSP pattern. No travel-specific orchestration (interline settlement, refund/change flows) claimed, unlike CellPoint.
9. **Does this differentiate vs travel specialists (CellPoint, Nuvei, Trust Payments, Travelpay)?** No. Ecommpay wins on APM/currency breadth + distribution via Dolphin, not on travel-specific capability.
10. **Who handles fraud/chargeback liability on high-ticket, long-lead travel bookings?** Open — "fraud-prevention tooling" mentioned but liability allocation (a real risk in travel) not addressed.
11. **How does this relate to Ecommpay's prior travel moves (humm BNPL Oct 2025, BridgerPay May 2026)?** Same pattern of incremental travel-channel partnerships; this is additive, not a strategic pivot — reinforces "one of many" reading.
12. **Is the reconciliation-automation benefit material?** Plausibly real operational value for agents doing manual reconciliation today, but unquantified.
13. **Is there any geographic or regulatory angle?** Region tagged global; both parties UK-based. No new licence or market entry — unlike Nuvei's Israel acquiring licence. Low regulatory novelty.
14. **Duplicate of a prior note?** No — distinct event/entity (Dolphin Dynamics) and date (2026-10-22); not the same as the humm or BridgerPay deals. Fresh.
15. **Does it change the central assessment question?** Yes, mildly: from "is Ecommpay winning travel payments?" to "does embedding in vertical ISVs actually entrench a mid-market PSP, or just commoditise it?" — the latter suggests limited strategic upside.

Importance: 2/5 — A standard, non-exclusive PSP-into-travel-ISV distribution deal with no disclosed economics, volume, exclusivity, or go-live metrics; real but incremental operational value for Dolphin's agents, low technical novelty, and a commoditised supplier position for Ecommpay. Notable only as another data point in the heavy 2025-26 travel-payments land-grab.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Travel is a high-fee, high-risk payments vertical sitting inside a very large flow: the global B2B travel payments market was ~$8.63bn in 2025, projected to ~$18.59bn by 2034 (~8.9% CAGR), with OTAs the fastest-growing end-user segment at ~11.6%/yr as they adopt the merchant model (per Growth Market Reports, as of 2025). Card fees of ~2–3% are the norm, and hotels alone spend ~$21bn/yr on processing (per atlasperk, 2026) — smaller operators (tour operators, DMCs, travel agencies) pay the same rates without negotiated discounts, which is exactly the fragmented long-tail Ecommpay/Dolphin target. Structure: fragmented on the merchant side (thousands of agencies/operators on legacy booking software), consolidating on the rails side (acquirers, orchestration layers). Why now: cross-border/multi-currency complexity and alternative-payment-method proliferation make DIY integration uneconomic for small travel firms, so PSPs win distribution by embedding into the travel-tech booking stack rather than selling direct — the structural pattern behind this deal.

**Competitive landscape.** Sector KPIs: processing/transaction volume (TPV), take rate (~bps on 2–3% card economics), authorisation/conversion uplift, chargeback ratio, FX margin. Ecommpay discloses +25% YoY processing volume and +19% transaction volume for 2024 (per ecommercenews.uk) but not TPV in absolute terms or take rate `[UNSOURCED]`. Basis of competition = distribution via travel-tech integrations + risk/fraud tooling + local/alt payment coverage, not headline price. Recent peer moves, all the same "PSP ⨉ travel-tech platform" playbook: Travelsoft Pay ⨉ Checkout.com (2026-06) and ⨉ Mastercard (2026-03); 2C2P ⨉ M-PAY across Asia (2026-03); RateGain ⨉ Juspay (2026-03); CellPoint Digital's OSO airline-payments orchestration (2025-10); Worldline ⨉ YeePay China cross-border (2025-10). Ecommpay's own cadence: ⨉ humm for travel finance (2025-10), Travelopedia (2026), and a UK travel-payments report (2026-06) — so Dolphin Dynamics is an incremental distribution win within an established travel push, not a new strategy. Position: credible mid-tier full-stack PSP/acquirer, catching up to scaled orchestration incumbents (Worldline, Checkout.com); moat is switching cost once embedded in a booking platform's reconciliation flow (analysis), not scale.

**Comps & multiples.** Private, undisclosed economics → no equity multiple computable. Ecommpay revenue estimates diverge wildly across aggregators ($25–50M SimilarWeb vs $360.9M ZoomInfo vs £46.9M UK FY2022 filing) — treat all as unreliable, no valuation disclosed `[UNSOURCED]`; EV/Revenue = no data. Internal comps (same PSP-⨉-travel-platform pattern, not valuation comps): [[Travelsoft Pay partners with Checkout.com for travel payments]], [[Travel payments firm 2C2P partners M-PAY across Asia]], [[CellPoint Digital's OSO platform redefines airline payments]], [[Worldline and YeePay partner on China cross-border travel payments]], [[Ecommpay partners humm for travel and retail finance]]. Distribution not computed, qualitative only: the sector is crowded with near-identical 2025–26 partnership announcements — signalling commoditisation of the "travel PSP" message.

**Risk flags.** (1) Chargeback/settlement exposure — the defining risk of travel acquiring: customers pay weeks-to-months pre-travel and chargeback windows run up to ~12–18 months, so an acquirer sits exposed to supplier/airline failure; rolling reserves (~2 months) typically undershoot ~6 months of forward-inventory exposure (per Envisso/Weavr, 2026). A thin PSP earning bps can absorb outsized losses if an embedded operator collapses — and holdbacks can themselves accelerate the failure (Thomas Cook 2019, Flybe 2020). (2) Distribution-dependence / disintermediation — value flows through Dolphin Dynamics' booking software; Ecommpay owns the rails but not the merchant relationship, so it can be swapped out (Dolphin can integrate another PSP) and margin may be captured by the travel-tech layer. (3) Commoditisation — the near-identical peer announcements above mean this layer competes on price/coverage once novelty fades, compressing take rate.

**What this changes (idea-lens).** Incremental, not re-rating: confirms the land-grab where PSPs/acquirers buy distribution by embedding into travel-tech booking platforms rather than selling to agencies direct (analysis). Falsifiable thesis: the winners will be those who price/underwrite travel chargeback risk, not those with the most integrations — watch for whether Ecommpay discloses who holds fraud/chargeback liability under the Dolphin deal (PR is silent on it) and whether rolling-reserve/holdback terms surface; silence there is the tell that economics, not logos, decide this vertical.

Sources: https://cfotech.co.uk/story/dolphin-dynamics-partners-ecommpay-on-travel-payments · https://growthmarketreports.com/report/b2b-travel-payments-market · https://atlasperk.com/guides/technology-for-travel/payment-processing/ · https://ecommercenews.uk/story/ecommpay-grows-processing-volume-25-with-new-payment-options · https://envisso.com/reports/airline-acquirer-risk-report-2026/ · https://www.weavr.io/blog/why-acquirers-miss-the-free-insurance-already-built-into-airline-payments/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
