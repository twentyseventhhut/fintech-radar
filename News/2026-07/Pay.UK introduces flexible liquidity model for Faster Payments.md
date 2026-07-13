---
title: "Pay.UK introduces flexible liquidity model for Faster Payments"
date: 2026-07-07
retrieved: 2026-07-07
tags:
  - company/pay-uk
  - industry/payments
  - industry/infrastructure
  - region/uk
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/4cc32bd6
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s867a83c9
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Pay.UK introduces flexible liquidity model for Faster Payments

> [!info] 2026-07-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 Pay.UK introduces a flexible liquidity model for Faster Payments Net Sender Caps (NSC), reducing pre-funding requirements for payment service providers. The change lowers barriers to direct participation while maintaining liquidity and risk controls through centralized oversight.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/4cc32bd6>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Pay.UK introduces flexible liquidity model for Faster Payments
_Analytical notes (not a post). Importance: 3/5._

**Freshness: FRESH.** No prior corpus note covers this specific Net Sender Cap (NSC) liquidity-model change. Adjacent, non-duplicating context exists: [[Bank of England proposes weekend RTGS and CHAPS settlement]], [[Bank of England confirms CHAPS early-morning extension from 2027]], [[Bank of England sets out plan to deliver National Payments Vision]], [[Corpay joins UK Faster Payments service]], [[Pay.UK appoints Modulr COO Ben Taylor to board]], [[UK Finance Just 4% of Faster Payments via open banking]], [[ACI Worldwide UK payments infrastructure needs a reset]]. This is a NEW operational/access development, not a re-report.

## [0] What exactly happened (de-PR'd)
Pay.UK has **gone live** (announced ~early July 2026, per Finextra/Financial IT) with a *flexible* liquidity model for Faster Payments Service (FPS) **Net Sender Caps (NSC)**.

- The NSC is the maximum net value a direct settling participant can send (sent minus received). Because FPS settles by **deferred net settlement** (currently 3 daily cycles) but pays out in real time, participants must **prefund** in central-bank money: they park cash equal to their NSC in a segregated Bank of England Reserves Collateralisation Account (RCA) within RTGS. That prefunding eliminates settlement risk — the system can always settle a defaulting member's obligation.
- **The old model:** Pay.UK mandated a fixed **Minimum Net Sender Cap (MNSC)** plus a **Peak Contingency Value (PCV)** that a direct settling PSP had to hold in its BoE Pre-Funding Account at all times.
- **The change:** participants can now **propose their own NSC limit** rather than being forced to the prescribed MNSC/PCV floor. Compensating risk controls stay centrally managed by Pay.UK, explicitly modelled on how the existing **Bacs Debit Cap** works. PSPs may still opt to keep the prescribed MNSC/PCV values.
- **Effect:** lower prefunding = less idle cash trapped in RTGS = lower cost of direct participation, aimed squarely at **non-bank / non-traditional PSPs**. Also lets any direct settling PSP better optimise its RTGS balance during non-peak periods.

**Why structured this way / what it reveals:** The reform is a *liquidity-efficiency knob*, not new rails. The real economic cost of FPS direct access has never been the technical connection — it is the **opportunity cost of dead prefunded cash** (remunerated only at Bank Rate, and only against your NSC). By moving from a mandated floor to a participant-set, centrally-governed cap, Pay.UK shifts the design from "one conservative size fits all" to "size it to your actual peak flow, with Pay.UK holding the compensating controls." The Bacs-Debit-Cap analogy signals this is a **proven governance pattern being ported**, not an experiment — which is why it can go live without new regulation.

## [1] Competitors / peers
FPS is a domestic monopoly scheme (owned/operated by Pay.UK alongside Bacs and the Image Clearing System), so "competition" is (a) other access models and (b) international instant-payment schemes.

- **Access-model peers within the UK:** directly-connected *non-settling* participants (avoid an RTGS settlement account entirely, but forgo settlement control); aggregator/sponsor-bank indirect access. This reform makes *direct settling* access relatively cheaper, nudging larger fintechs toward it.
- **Non-bank direct access history:** Wise (TransferWise) became the first non-bank direct FPS participant on 13 Apr 2018 after BoE opened RTGS to non-banks in 2017. Onboarding still takes ~9–12 months plus an FCA s166 assessment — so liquidity cost is one barrier among several. [[Corpay joins UK Faster Payments service]] (Oct 2025) shows the ongoing trickle of new direct joiners.
- **International instant schemes:** EU SEPA Instant, India UPI, Brazil Pix, US FedNow/RTP. Many newer schemes were designed prefunding-light or with liquidity-saving mechanisms from day one; the UK is retrofitting flexibility onto a 2008-era scheme.

**Why the lay of the land is this way / second-order:** FPS launched in 2008 with a rigid prefunding regime precisely because it was pioneering real-time retail settlement — conservatism was the price of safety. Newer schemes learned from that and baked in liquidity efficiency. So this reform is best read as the UK **catching up to parity** on liquidity mechanics, not leaping ahead. The second-order effect: cheaper direct access widens the *supply* of direct PSPs, which matters for the National Payments Vision's competition goals — but demand-side pull for account-to-account payments remains weak (only ~4% of the 5.6bn FPS payments are open-banking-initiated, per [[UK Finance Just 4% of Faster Payments via open banking]]).

## [2] Company history / fit
Pay.UK is the not-for-profit retail payment system operator formed from the 2018 consolidation of the old scheme bodies. Its recent trajectory is defined by the **collapse of the New Payments Architecture (NPA)**: after years of delay and cost, the PSR cut NPA scope and Pay.UK ultimately **cancelled the NPA procurement**, pivoting to a modular, phased "alternative technology strategy" now steered under the National Payments Vision (Nov 2024 gov paper) and the Retail Payments Infrastructure Board (which launched a next-gen infrastructure consultation in June 2026). Governance is being refreshed — e.g., appointing Modulr's COO to the board ([[Pay.UK appoints Modulr COO Ben Taylor to board]]).

**Why the company acts this way:** After the NPA reputational hit, Pay.UK's credible near-term wins are **incremental, low-risk operational improvements to the live FPS** rather than big-bang rebuilds. A liquidity-model tweak that (a) needs no new tech, (b) reuses the proven Bacs Debit Cap governance, and (c) directly serves the National Payments Vision's "widen access / boost competition" mandate is exactly the kind of quick, defensible deliverable Pay.UK needs to show momentum while the future infrastructure is still in consultation.

## [3] Novelty / value-add / traction
**What is genuinely new:** the *mechanism* — participant-proposed NSC with centrally-managed compensating controls, replacing a mandated MNSC/PCV floor. That is a real, if narrow, change to how much central-bank money a direct FPS member must lock up.

**What is NOT new:** prefunding itself, RCAs, the NSC concept, and non-bank direct access (all pre-existing since 2017–2018). The Bacs Debit Cap control model already existed — this ports it to FPS.

**Traction — mostly unproven (announcement, not adoption):** the model is "live," but there are **no disclosed numbers** on how many PSPs have adopted a self-set NSC, how much prefunding is actually freed up, or any named early adopter. So the value-add is *structurally plausible* but *empirically unconfirmed*.

**Why the value-add is real or not (deeper):** The saving is real only to the extent a participant's mandated MNSC/PCV floor exceeded its true peak net exposure — i.e., the reform captures the "over-collateralisation gap." For a small non-bank PSP running below the old floor, that gap (and the freed cash) could be material to unit economics; for a large bank whose flows already dwarf the floor, it changes little. **Who captures the value:** directly the PSPs (lower trapped-cash cost); indirectly Pay.UK/BoE (a more efficient, more contestable scheme). What breaks the thesis: if compensating controls prove costly or if FPS's underlying deferred-net-settlement, thrice-daily cycle (the real liquidity driver) is untouched — which it is here — the headline saving may be modest.

## [4] What's next / market sentiment
- **Immediate:** watch for adoption disclosure — number of PSPs opting for self-set NSCs and any quantified prefunding reduction. Absent that, this stays a "framework improvement," importance-capped.
- **Adjacent settlement reforms compound this:** BoE is extending RTGS/CHAPS hours (early-morning open from Sep 2027, weekend settlement proposed no earlier than 2029 — [[Bank of England confirms CHAPS early-morning extension from 2027]], [[Bank of England proposes weekend RTGS and CHAPS settlement]]) toward near-24/7 settlement. Longer settlement windows plus more flexible prefunding together improve intraday liquidity management and cross-border reach.
- **Strategic backdrop:** National Payments Vision + the June 2026 Retail Payments Infrastructure Board consultation on next-gen infrastructure; RTGS renewal already live. Regulators (PSR/FCA) are pushing access, competition and A2A/commercial VRP (UK Payments Initiative).

**Why the market goes this way / counterintuitive second-order:** Cheaper direct access is *supply-side* stimulus. But the binding constraint on UK A2A payments is **demand** — merchants have some incentive to escape card fees, payers largely do not care (see the 4%-open-banking figure). So making it cheaper for a fintech to *become* a direct FPS participant does not by itself create A2A volume; it mostly redistributes who sits in the stack. The counterintuitive risk: a wave of thinly-capitalised non-bank direct participants with self-set NSCs concentrates more of the "size-your-own-risk" judgement on Pay.UK's centralised compensating controls — efficiency gained, but the systemic-risk-management burden shifts inward rather than disappearing.

## Sources
- Finextra — "Pay.UK launches liquidity model for faster payments" (Jul 2026): https://www.finextra.com/pressarticle/110304/payuk-launches-liquidity-model-for-faster-payments
- Financial IT — "Pay.UK Introduces Flexible Liquidity Model for Faster Payments": https://financialit.net/news/payments/payuk-introduces-flexible-liquidity-model-faster-payments
- Primary channel: Connecting the Dots in Fintech — https://www.connectingthedotsinfin.tech/r/4cc32bd6
- Pay.UK — FPS System Principles v11 (Jan 2026): https://www.wearepay.uk/wp-content/uploads/2026/02/Pay.UK-Faster-Payments-System-Principles-v-11-Jan-2026.pdf
- BoE — Access to UK payment systems for non-bank PSPs: https://www.bankofengland.co.uk/payment-and-settlement/access-to-uk-payment-systems-for-non-bank-payment-service-providers
- Faster Payments — first non-bank PSP direct connection / access & BoE settlement: https://www.fasterpayments.org.uk/access-payments/faster-payments-bank-england-settlement
- Pay.UK FPS statistics (volume/value): https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/faster-payment-system-statistics/
- BoE — Extending RTGS and CHAPS settlement hours (consultation): https://www.bankofengland.co.uk/paper/2026/cp/extending-rtgs-and-chaps-settlement-hours-next-steps
- Gov.UK — National Payments Vision: https://www.gov.uk/government/publications/national-payments-vision/national-payments-vision
- BoE — RPIB next-generation retail payments infrastructure consultation (Jun 2026): https://www.bankofengland.co.uk/news/2026/june/rpib-launches-consultation-on-next-generation-uk-payments-infrastructure
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is it live or announced?** Live — Finextra/Financial IT say Pay.UK "has gone live" with the model (early July 2026). But "live framework" ≠ "adopted": no participant is named as having switched to a self-set NSC. **Open** on adoption.

2. **How much prefunding does this actually free up?** Undisclosed. The saving equals the gap between the old mandated MNSC/PCV floor and a participant's true peak net exposure. No aggregate or per-PSP figure published. **Open — the load-bearing number is missing.**

3. **Who benefits most — small non-banks or large banks?** Structurally, small/non-bank PSPs whose mandated floor exceeded their real flow. Large banks' flows dwarf the floor, so little changes for them. This is a targeted access-cost reform, not a system-wide liquidity release.

4. **Does it touch the real liquidity driver — deferred net settlement across ~3 daily cycles?** No. The settlement cadence and DNS design are untouched; only the cap-setting rule changed. So the headline "improves liquidity efficiency" is bounded by an unchanged settlement architecture.

5. **What exactly are the "compensating controls" and do they add cost?** Modelled on the Bacs Debit Cap and centrally managed by Pay.UK. Details/costs to participants not disclosed. If controls are onerous, net saving shrinks. **Open.**

6. **Is this genuinely new or a re-report of an older reform?** New — no prior corpus note covers the NSC flexible model; the Bacs Debit Cap it copies is pre-existing but its application to FPS NSC is the novelty. **Fresh.**

7. **Does cheaper direct access create A2A payment volume?** No — it is supply-side. Demand is the binding constraint: only ~4% of 5.6bn FPS payments are open-banking-initiated. Reform redistributes stack position more than it grows volume.

8. **Does it need new regulation or BoE approval?** Appears not — it reuses existing prefunding/RTGS mechanics and a proven governance pattern, which is why it could go live now while bigger infrastructure remains in consultation.

9. **How does it interact with RTGS/CHAPS hour extensions and RTGS renewal?** Complementary: longer settlement windows (2027 early-morning, 2029 weekend proposal) plus flexible prefunding jointly improve intraday liquidity management. But these are separate, later-dated programmes — don't conflate.

10. **Is this a distraction from the NPA failure?** Partly — after cancelling NPA procurement, Pay.UK needs visible, low-risk wins. This is a credible incremental deliverable but should not be read as core infrastructure renewal (that sits in the June 2026 RPIB consultation).

11. **Does self-set NSC raise systemic risk?** It concentrates "size-your-own-cap" judgement on Pay.UK's central controls. Efficiency up, but risk-management burden shifts inward rather than vanishing. Prefunding still eliminates settlement risk per member — the question is calibration discipline at scale. **Open (analysis).**

12. **What is FPS's scale (does the reform matter at system level)?** Large: FPS processed ~1.3bn payments / ~£1.1tn in a single recent quarter (Q4 2024), ~5.6bn payments annually. So even modest per-PSP liquidity efficiency across many direct participants could aggregate — but that depends on adoption breadth, which is unknown.

13. **Who is silent about what?** No named early adopters, no quantified prefunding reduction, no fee/economics detail on compensating controls, no timeline for further NSC-cycle reform. The PR leads with "flexibility" and "lower barriers" but omits magnitudes.

14. **Could this backfire competitively?** A wave of thinly-capitalised non-bank direct participants with aggressive self-set caps would test Pay.UK's central controls; a single default event that stresses the model would reverse the "lower barriers" narrative fast.

15. **Precise mechanism delta vs the old regime (one sentence):** Participants now propose their own Net Sender Cap with Pay.UK-managed compensating controls (Bacs-Debit-Cap style), instead of holding a Pay.UK-mandated fixed MNSC + Peak Contingency Value floor in their BoE prefunding account.

**Importance: 3/5** — A real, sensible liquidity-efficiency reform to a systemically important live scheme (FPS: ~5.6bn payments/yr) that materially lowers the cost of direct access for non-bank PSPs and fits the National Payments Vision agenda. Capped at 3 because: mechanism is incremental (not new rails), the core deferred-net-settlement design is untouched, no adoption or freed-liquidity numbers are disclosed, and the binding constraint on UK A2A (demand) is unaffected. Upgrade if adoption/quantified liquidity savings are later reported; downgrade toward 2 if it proves a framework with few takers.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-07]] (2026-07-07).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** UK real-time retail payments infrastructure. Faster Payments (FPS) is the UK's instant-payment rail, operated by Pay.UK (the not-for-profit scheme operator). Scale: ~4.9bn FPS transactions in the 12 months to Sept 2024, +14% YoY; Q4 2024 alone processed >1.3bn payments worth >£1.1tn, +18.1% vs Q4 2023 (per UK Finance / Pay.UK QSR, via search, as of 2024–2025). FPS became the most-used method for business payments (~50% share in 2024), overtaking Bacs Direct Credit. Structure: a single centrally-governed scheme (natural monopoly at the rail layer), settled across the Bank of England's RTGS (RT2 core went live 28 Apr 2025); the competitive layer is *participation* — direct settling PSPs vs indirect access via bank sponsors. Barrier being lowered here: pre-funding. Direct settling PSPs must hold liquidity in a BoE Pre-Funding Account sized to a Net Sender Cap (NSC); until now a fixed Minimum NSC (MNSC) + Peak Contingency Value (PCV) was mandated. Why now: this is the latest step in an access-widening programme running since 2018 — direct FPS participation has grown from 26 to 47 organisations, and non-bank PSPs have been able to hold BoE settlement accounts since 2017/2018 (per Pay.UK / BoE, via search).

**Competitive landscape.** Rail-infra KPIs: transaction volume/value, number of direct participants, pre-funding/liquidity cost, settlement finality/uptime. Pay.UK is not a commercial competitor for share — it is the monopoly scheme operator; the "competition" it shapes is *among* PSPs and vs alternative access models (bank sponsorship, and adjacent rails: card networks, A2A overlays). Peer sovereign/utility RTP systems: FedNow (US, Federal Reserve — recently shipped a network-intelligence/fraud API, [[Federal Reserve launches FedNow network intelligence API for fraud]]), Pix (Brazil, central-bank-run, R$15tn in H1 2025, [[Brazil's Pix processes R$15 trillion in first half of 2025]]), UPI (India), TIPS/SEPA Instant (EU). Recent adjacent UK move: [[Visa completes first A2A variable recurring payment in UK]] — card networks pushing into A2A on top of FPS rails. Non-bank direct-access precedent elsewhere: [[Wise becomes first non-bank to go live on Japan's Zengin network]]. Pay.UK's position: incumbent operator, not "ahead/behind" — its moat is regulatory mandate + the network itself (all UK banks/PSPs connect to it). This change is Pay.UK lowering its own access friction to keep the direct-participation funnel growing rather than ceding volume to sponsor-bank intermediation.

**Comps & multiples.** No valuation/round/deal/revenue in the item — Pay.UK is a not-for-profit utility, not a traded/valued entity. Trading multiples not applicable: **no data / not meaningful.** Internal comps are qualitative RTP-infra reference points, not valuation comps: [[Brazil's Pix processes R$15 trillion in first half of 2025]], [[Federal Reserve launches FedNow network intelligence API for fraud]], [[Visa completes first A2A variable recurring payment in UK]], [[Wise becomes first non-bank to go live on Japan's Zengin network]]. Distribution not computed (no comparable financial figures).

**Risk flags.**
- Liquidity-vs-risk trade-off: self-proposed NSC limits shift discipline from a hard prescribed floor to Pay.UK-managed "compensating controls" (framed as analogous to the Bacs Debit Cap). Second-order effect: if a self-set cap is mispriced against a participant's actual settlement risk, the scheme absorbs more counterparty/liquidity risk at the centre — the mitigation is only as strong as Pay.UK's oversight. (analysis)
- Announced vs live/de-risked: the item and PR say the flexible model is "introduced"/"go live," but adoption and real capital savings for non-banks are unproven at the note date — benefit is a projection until PSPs actually opt in and cut pre-funding. `[UNSOURCED]` on the size of the capital saving.
- Concentration/dependence: participants still depend on BoE RTGS (RT2) and Pay.UK's centralised controls — a single-operator rail; any RT2 or scheme incident is systemic. (analysis)

**What this changes (idea-lens).** Lowering pre-funding is a pro-competition lever: it makes *direct* FPS participation cheaper for non-bank PSPs, weakening the economic case for renting access from sponsor banks and feeding the 26→47 (and rising) direct-participant trend. Falsifiable thesis: over the next 12–18 months direct FPS participant count accelerates and new joiners skew non-bank. Trigger/catalyst to watch: Pay.UK/BoE publishing new direct-participant numbers and NSC opt-in rates; what would break the thesis — take-up stalls because Pay.UK's compensating-control terms end up as costly/onerous as the old MNSC/PCV, leaving no net saving. (analysis)

Sources: https://www.finextra.com/pressarticle/110304/payuk-launches-liquidity-model-for-faster-payments · https://financialit.net/news/payments/payuk-introduces-flexible-liquidity-model-faster-payments · https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/faster-payment-system-statistics/ · https://www.ukfinance.org.uk/system/files/2025-10/Payment%20Markets%20Report%20Summary.pdf · https://www.bankofengland.co.uk/payment-and-settlement/access-to-uk-payment-systems-for-non-bank-payment-service-providers
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
