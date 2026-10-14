---
title: "Nigeria launches open-source National Payment Stack"
date: 2026-10-14
retrieved: 2026-10-14
tags:
  - company/nibss
  - industry/payments
  - industry/infrastructure
  - region/africa
  - type/product
sources:
  - https://www.arise.tv/nibss-launches-open-source-payment-stack-for-instant-transfers-qr-codes-phone-payments
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sb4e4181e
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Nigeria launches open-source National Payment Stack

> [!info] 2026-10-14 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇳🇬 Nigeria Inter-Bank Settlement System has launched a National Payment Stack, built on open source technology. The platform supports A2A instant transfers, QR code merchant payments and phone number payments, as well as bulk payments. It runs on Transactility's jPTS switching platform and ISO 20022, and NIBSS keeps access to the source code and control of its development roadmap.

## Первоисточники

### arise.tv
<https://www.arise.tv/nibss-launches-open-source-payment-stack-for-instant-transfers-qr-codes-phone-payments>
*649 слов · direct*

Nigeria’s interbank settlement operator deploys a platform designed to expand payment services and give it greater control over upgrades. 
"> 
 
 


Nigeria Inter-Bank Settlement System (NIBSS) has deployed a new national payments platform built on open-source technology, giving the operator greater control over the development and expansion of critical digital payment infrastructure as transaction volumes and service demands evolve.
The National Payment Stack (NPS), designed and developed by NIBSS, uses technology supplied by United States-based Transactility, including its jPTSswitching platform, to support instant payments based on the ISO 20022 messaging standard.
The arrangement allows NIBSS to retain access to the platform’s source code and control its architecture, development roadmap, and locally developed intellectual property, potentially reducing dependence on proprietary technology vendors for future upgrades and modifications.
NIBSS Managing Director/Chief Executive, Premier Oiwoh, said the platform was designed to meet the scale and requirements of the Nigerian market.
In a statement, Oiwoh said, “The NPS was designed and built for the scale and demands of the Nigerian payments market. The jPOS ecosystem gives us the flexibility to continue developing the platform as the ecosystem evolves.”

 Cardoso Unveils Ambitious Payments Vision, Targets 95% Financial Inclusion, Near-Instant… 
 INEC To Issue Candidate Nomination Portal Access Codes To Parties June 26 
 NIMC, NIBSS, Stakeholders to Roll Out Digital Cards to Boost Financial Inclusion in Nigeria 
 Platform Targets Wider Payment Services 
NPS supports account-to-account instant transfers, QR-code merchant payments, alias-based transactions using identifiers, such as phone numbers, and bulk payments.
Its architecture is designed to deliver the processing performance and availability required for national payment infrastructure while providing room for additional services as the market develops.
A key feature is its adoption of ISO 20022, an international financial messaging standard that enables more structured and detailed information to accompany payment transactions.
Its use provides a foundation for developing payment services around richer transaction data and greater interoperability, subject to implementation and integration requirements.
NIBSS built the platform using a modular architecture that combines its own engineering capabilities with selected open-source and enterprise technologies.
The company has used jPOS, an open-source framework for payment transaction processing, for years, particularly in systems based on the ISO 8583 messaging standard.
For NPS, it adopted jPTS and its ISO 20022 capabilities to develop a switching platform suited to the demands of Nigeria’s payments market.
The arrangement gives NIBSS access to the underlying technology while allowing it to customise and extend the system as operational needs and regulatory requirements change, rather than relying solely on a proprietary vendor’s product-development timetable.
The extent to which the new platform improves transaction costs, processing speeds, and service reliability will depend on its operational performance and adoption across the payments ecosystem.

 Partnership Combines Local Engineering with Established Technology 
Transactility, which develops and supports products within the jPOSecosystem, says the deployment demonstrates how open technology can be combined with local engineering to build payment infrastructure at national scale.
The company’s founder and Chief Technology Officer, Alejandro Revilla, described the selection of its technology for NPS as a milestone for the company and the wider payments community.
Revilla said the deployment illustrated the role open-source technology could play in supporting large-scale payment systems.
Transactility’s products include jPTS, jCard and ISO/Bridge, while its jPOSframework has been used for more than 25 years to develop payment gateways, switching systems, and transaction-processing infrastructure.
NIBSS, incorporated in 1993, is owned by Central Bank of Nigeria (CBN) and all licensed deposit money banks in the country.
It operates critical infrastructure for interbank clearing and settlement, alongside services supporting identity verification through the Bank Verification Number system and electronic payments.
The rollout of NPS adds another layer to the country’s digital payments infrastructure as its longer-term significance will rest on the platform’s ability to sustain reliable transaction processing, accommodate new services, and give NIBSS the flexibility to respond to the changing needs of banks, businesses, consumers, and regulators.
James Emejo
Follow us on:

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Nigeria launches open-source National Payment Stack
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **13 Oct 2026**, NIBSS and US vendor **Transactility** issued a joint announcement publicizing that Nigeria's **National Payment Stack (NPS)** — a next-gen, **ISO 20022** instant-payments platform — runs on Transactility's **jPTS** switch inside the open-source **jPOS** ecosystem. NPS supports A2A instant transfers, QR-code merchant payments, alias (phone-number) addressing and bulk payments; NIBSS keeps source-code access, roadmap control and locally-developed IP.

**Crucial de-PR: this is NOT a launch.** The note's title "Nigeria launches…" and the ARISE/arise.tv framing ("has deployed / launched") are misleading. NPS's **first live transaction was 7 Nov 2025** (PalmPay↔Wema); by Aug 2026 it had processed **26.55m transactions worth ~N1.4trn across 48 institutions** (First Bank leads volume, Fidelity value; GTBank, Sterling, Access, Moniepoint among early adopters). The 13 Oct 2026 event is a **vendor-attribution / partnership PR** — the new *fact* is who supplied the switch (Transactility/jPTS) and the "open-source + sovereign control" narrative, not a system going live. (analysis) NIBSS/Transactility structure it this way to (a) sell the sovereignty angle — "we own the code, not the vendor" — ahead of decommissioning the **15-year-old NIP** rail, and (b) give Transactility a marquee reference for jPTS at national scale. "Open-source" here means NPS is *built on* jPOS/jPTS (an open framework NIBSS has used for years for ISO 8583); it does **not** mean NIBSS open-sourced the NPS itself for others to reuse. Whether NPS actually improves cost/speed/reliability is explicitly left as "will depend on operational performance and adoption."

## [1] Competitors / peers
Category = **public DPI / national instant-payment rails**. Benchmarks: **India UPI** (A2A + QR + alias/VPA, ~Rs 94,000cr/day in Oct, 84% of India's digital payments, 500m users/65m merchants — see [[UPI accounts for 84% of India's digital payments in FY25]], [[UPI reaches 500 million consumers and 65 million merchants]]); **Brazil Pix** (alias-keyed, central-bank-run); African peers **Rwanda eKash/RSwitch** ([[Rwanda launches full interoperability on eKash payment system]], Mojaloop-based), Ethiopia EthSwitch, Ghana GhIPSS. Nigeria's NIP already handled **11.3bn txns (2024)** — it is one of the largest real-time rails on the continent, so NPS is a **platform modernization of an incumbent-scale rail**, not a greenfield catch-up. Position vs UPI/Pix: **feature parity on capabilities** (A2A/QR/alias), but NPS's distinguishing claim is the **governance/tech model** (sovereign source-code control via open framework), not product novelty. (analysis) UPI/Pix are mandate-and-scale stories; NPS's pitch is vendor-independence — a procurement/roadmap-control story, a different axis of value.

## [2] Company history / fit
**NIBSS** (inc. 1993; owned by **CBN** + all licensed deposit money banks) operates Nigeria's interbank clearing/settlement, NIP, and BVN identity rails. NPS fits a clear trajectory: NIP is 15 years old; CBN's **Payments System Vision (PSV) 2028** (launched 1 Jun 2026, Gov. Cardoso) targets **95% financial inclusion**, fraud <0.001% of digital value, and positioning Nigeria as a regional/cross-border hub — NPS is the rail that is supposed to carry PSV 2028. (analysis) Structural logic: a systemically-critical operator locked into a 15-year proprietary-era stack faces vendor-release-cycle risk and ISO 20022 migration pressure; building on jPOS/jPTS (which it already knew from ISO 8583) lets it migrate to ISO 20022 while keeping customization control — hence the "sovereignty" framing is genuine procurement logic, not just PR.

## [3] Novelty / value-add / traction
**Not new as a launch** — see [0]. The genuinely new, citable information in this item is narrow: the **Transactility/jPTS attribution** and the **ISO 20022 + open-framework** architecture detail. **Traction is real and already measurable** (unusually, for an "infrastructure launch" story): N1.4trn / 26.55m txns / 48 institutions by Aug 2026, with a **phased cut-over toward NIP decommissioning** (no firm decommission date disclosed). (analysis) Where value accrues: NPS is public infrastructure, not an investable equity — the margin question is downstream. Lower switching/vendor costs and ISO 20022's richer data *could* lower per-txn cost and enable overlay services (richer reconciliation, fraud data), benefiting banks/fintechs building on top. What breaks the thesis: NPS does nothing by itself for inclusion (it re-plumbs existing flows); "open-source control" cuts vendor lock-in but concentrates **operational/execution risk on NIBSS**, which now owns the roadmap it used to outsource.

## [4] What's next / market sentiment
Next: full-industry cut-over and eventual **NIP decommissioning**; NPS as the PSV-2028 backbone (95% inclusion by 2028, +50m banked Nigerians). Sentiment is positive/sovereignty-flavored in Nigerian press; Transactility frames it as proof open tech can run national-scale rails. Risks: (a) single-rail concentration — decommissioning NIP removes the fallback; NPS outages would be systemic; (b) migration execution risk now sits with NIBSS, not a vendor SLA; (c) "open-source" ≠ cost savings until adoption and operational data confirm it; (d) inclusion goals depend on last-mile distribution (agents, USSD, fintechs), not the switch. (analysis) Counterintuitive second-order: owning the code makes NIBSS *more* exposed, not less — vendor independence trades procurement risk for in-house capability risk.

## Top challenge/extra questions
See challenge section.

## Sources
- arise.tv (primary, in note): https://www.arise.tv/nibss-launches-open-source-payment-stack-for-instant-transfers-qr-codes-phone-payments
- Transactility/NIBSS partnership: https://www.fintechfutures.com/paytech/nibss-and-transactility-partnership-delivers-national-payment-stack
- Nairametrics (jPOS adoption, 13 Oct 2026): https://nairametrics.com/2026/10/13/nibss-adopts-ransactilitys-jpos-technology-for-national-payment-stack/
- First live txn (7 Nov 2025): https://nairametrics.com/2025/11/09/palmpay-wema-bank-complete-first-live-transaction-on-nibss-national-payment-stack/
- N1.4trn / 26.55m / 48 institutions (Aug 2026): https://nibss-plc.com.ng/nibss-new-payment-system-records-26-5m-transactions-worth-n1-4trn
- CBN PSV 2028 / 95% inclusion: https://nairametrics.com/2026/06/01/cbn-targets-95-financial-inclusion-by-2028-under-new-payment-system-roadmap/
- techpoint explainer: https://techpoint.africa/insight/how-the-nps-works/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **Is this actually a "launch"?** No. NPS's first live transaction was **7 Nov 2025**; by Aug 2026 it had done 26.55m txns / ~N1.4trn across 48 institutions. The note's title and arise.tv framing are inaccurate. The 13 Oct 2026 event is a **vendor-partnership PR** (NIBSS + Transactility), not a system going live.

2. **So what IS the news on 13 Oct 2026?** The **attribution** — that NPS runs on Transactility's jPTS switch / jPOS open-source ecosystem on ISO 20022 — plus the "sovereign source-code control" narrative. Narrow, real, but not a market event.

3. **What does "open-source" mean here — is NPS itself open-source?** No. NPS is **built on** open-source jPOS/jPTS; NIBSS did **not** release NPS's code publicly. "Open-source" = vendor-independence / source-code access for NIBSS, not a public commons. Easy to misread.

4. **Is it fresh or a duplicate?** **Fresh** — no prior KB note covers NPS or Transactility (grep-confirmed; only this note hits). But the underlying "launch" is stale (Nov 2025); treat the headline as a re-framing of an in-progress rollout.

5. **Does NPS replace NIP, and is NIP gone?** NPS is designed to **succeed the 15-year-old NIP** via phased cut-over; **no firm decommission date** is disclosed. NIP still runs in parallel. "Decommission" is a plan, not an event.

6. **Precise mechanism delta vs UPI/Pix?** Capability parity (A2A, QR, alias/phone, bulk). The delta is **governance**: sovereign source-code control via an open framework + ISO 20022 migration — not a new consumer feature. Open: any UX or cost delta vs old NIP.

7. **Is traction real or announced?** **Real and measured** (unusual for a "launch" story): N1.4trn / 26.55m / 48 institutions by Aug 2026, with named early adopters (First Bank, Fidelity, GTBank, Sterling, Access, Moniepoint).

8. **Does NPS move financial inclusion?** Not by itself — it re-plumbs existing interbank flows. Inclusion (CBN PSV 2028: 95% by 2028, +50m banked) depends on last-mile (agents, USSD, fintechs), not the switch. Open causal claim.

9. **Who bears cost / does it lower transaction cost?** Open. Sources explicitly say cost/speed/reliability gains "will depend on operational performance and adoption." No fee or unit-economics data disclosed.

10. **What's the second-order risk of owning the code?** Owning the roadmap shifts **execution/operational risk from vendor SLA to NIBSS in-house capability**. Vendor independence is not free — it trades procurement risk for capability risk.

11. **Single-rail concentration risk?** High. Decommissioning NIP removes the fallback; an NPS outage would be systemic for Nigerian retail payments. Resilience/failover posture not disclosed.

12. **Is Transactility a credible national-scale vendor?** jPOS has 25+ yrs of payment-switch deployments; jPTS/ISO 20022 support is newer. Open: NPS appears to be jPTS's flagship national-scale reference — track record at this scale is thin.

13. **Does ISO 20022 deliver here or is it box-ticking?** ISO 20022 enables richer data/interoperability **subject to implementation** — sources hedge it. Overlay value (fraud data, reconciliation) is potential, not demonstrated.

14. **Read-through to covered public names?** Minimal. NIBSS is CBN+bank-owned public infrastructure, not investable. Indirect beneficiaries = Nigerian banks/fintechs on the rail (Moniepoint, OPay, PalmPay); no direct equity impact.

15. **Any contradiction between sources?** The arise.tv "launch/deployed" framing vs the Nov-2025 first-txn and Aug-2026 volume reports. Primary-source reality (phased rollout since Nov 2025) beats the review's "launch" framing.

**Importance: 3/5** — A substantive modernization of a continent-scale rail (NIP → NPS, ISO 20022, sovereign/open-framework control) backed by **real measured traction** (N1.4trn, 48 institutions) and tied to CBN's PSV 2028. Weighted up by Nigeria's scale and the credible vendor-independence/DPI angle; weighted down because the 13 Oct item is a **vendor-attribution PR of an already-live rollout** (not a launch), there is no listed-equity read-through, and the claimed cost/inclusion benefits remain unproven.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-14]] (2026-10-14).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits in the global **public digital-payment-infrastructure (DPI)** wave — central-bank/operator-owned instant A2A rails displacing cards for domestic retail. Reference scale: India's **UPI ≈ 23.2bn transactions/month** (May 2026), ~46% of global real-time volume; Brazil's **Pix ≈ 80bn transactions in 2025**, ~15% of global instant payments (per Ebanx, via [heyfuturenexus](https://www.heyfuturenexus.com/posts/brazil-india-instant-payments-growth-worldwide-pix-upi)). Nigeria is already a DPI heavyweight, not a greenfield: **NIP processed ~11.2bn transactions in 2024 (≈N1.07 quadrillion / ~USD 702bn–1tn), +120% vs 2022**, powering >90% of interbank transfers ([NIBSS](https://nibss-plc.com.ng/nigerias-digital-payments-surge-to-n1-07-quadrillion-as-nibss-defines-future); [TC Insights](https://insights.techcabal.com/nigeria-fintech-financial-inclusion-cbn-infrastructure-gap/)). **Structure:** consolidated monopoly rail — NIBSS (owned by CBN + all licensed banks) is the single switch; barriers are regulatory/network-effect, not capital. **Why now:** (a) CBN's **Payments System Vision 2028 target of 95% financial inclusion** (from 64% in 2024; 26% of adults — 47% in the north — still excluded) ([Guardian](https://guardian.ng/news/cbn-targets-95-financial-inclusion-with-digital-payments/); [Channels](https://www.channelstv.com/2026/06/02/financial-inclusion-to-hit-95-by-2028-cbn/)); (b) legacy ISO-8583 rails hitting ceilings on volume, richer data and fraud controls → migration to **ISO 20022**; (c) a sovereignty push to own source code rather than lease a proprietary vendor stack.

**De-PR / what actually happened.** The 13 Oct 2026 item is the **NIBSS–Transactility partnership announcement**, not a cold launch: the **first live NPS transaction ran 7 Nov 2025 (PalmPay ↔ Wema Bank)**, and NPS had already cleared **26.55m transactions / N1.4trn across 48 institutions** by the announcement ([Nairametrics](https://nairametrics.com/2026/10/13/nibss-adopts-jpos-technology-for-national-payment-stack/); [Leadership](https://leadership.ng/nibss-payment-stack-processes-n1-4trn-in-26-5m-transactions/)). So this is an incumbent re-platforming its own monopoly rail onto open-source jPTS/ISO 20022 — **not a new entrant disrupting anyone**. The 26.55m vs 11.2bn/yr NIP base shows NPS is still an early-stage parallel rail, not a full cut-over (analysis).

**Competitive landscape.** Sector KPIs: transaction volume/value, settlement latency (sub-second), institutions connected, per-transaction cost/fraud rate. NIBSS has **no domestic competitor** on the clearing rail — it IS the national switch. The real "competition" is architectural: proprietary vendor stacks vs the open-source jPOS/jPTS route NIBSS chose (vendor: US-based **Transactility**, CTO Alejandro Revilla; 48 institutions live). Peer DPI programs — none are NIBSS's rivals but all are comparators: India UPI (NPCI), Brazil Pix (BCB), Rwanda eKash/RSwitch (Mojaloop, RWF 20 fee cap, cut-over Jul 2026), Ethiopia EthSwitch, Kenya PesaLink/national-switch, Ghana GhIPSS. Protagonist position: **mature incumbent, ahead on absolute scale in Africa** (AfricaNenda rates NIP Africa's first "mature" IPS) but **catching up on modern messaging/data** — ISO 20022 and QR/alias features that UPI/Pix shipped years earlier (analysis). Moat: regulatory mandate + ownership by the entire banking system = near-insurmountable network-effect/switching-cost moat.

**Comps & multiples.** National infrastructure program, not an issuer — **no valuation, no multiple ("no data")**. Internal base comps (DPI / national-switch analogs):
- [[Rwanda launches full interoperability on eKash payment system]] — central-bank-mandated, open-source (Mojaloop) national switch; closest African analog, incl. the "launch ≠ launch" phased-rollout pattern.
- [[Nigeria mandates dual PoS routing through NIBSS and UPSL]] — same operator, CBN forcing traffic onto NIBSS rails (Dec 2025); shows the mandate lever.
- [[Rwanda launches national instant payment system]] / Ethiopia EthSwitch analogs; [[UPI reaches 500 million consumers and 65 million merchants]] and [[Instant transfers driving real-time payments in Latin America]] as the UPI/Pix benchmark.
- [[OPay secures $185M private placement with Standard Bank]] — a NIP/NIBSS-dependent Nigerian fintech, i.e. a downstream beneficiary of this rail.

**Risk flags.**
1. **Execution/migration risk, not announcement risk.** 26.55m NPS transactions vs ~11.2bn/yr on legacy NIP means the hard, multi-year, dual-running cut-over is ahead; any instability on a monopoly rail is a systemic single-point-of-failure (cf. CBN's own dual-PoS-routing fragility concerns). "Open-source + own the code" shifts maintenance/security burden onto NIBSS.
2. **Vendor/sovereignty paradox.** The sovereignty pitch (own the source, escape proprietary vendors) still leaves NPS dependent on **one US vendor (Transactility) and the jPOS/jPTS ecosystem** for the switch core — concentration risk dressed as independence.
3. **Displacement of card economics / fintech margin.** Richer ISO-20022 data + free-ish A2A/QR/alias rails compress what acquirers, card networks and PSPs can charge (the UPI/Pix playbook already hollowed card interchange); downstream fintechs (OPay, PalmPay, Moniepoint) gain reach but cede pricing power to the central rail (analysis).

**What this changes (idea-lens).** NPS is Nigeria's bid to run the **UPI/Pix DPI playbook at Africa's largest-economy scale** — if the ISO-20022/QR/alias layer drives merchant acceptance, it accelerates the card-to-A2A shift and pulls the still-excluded 26% onto rails, re-rating fintech distribution over card economics (analysis). **Falsifiable thesis:** NPS is live-and-adopted (not just announced) only once volumes on the new stack approach legacy NIP's billions and QR merchant acceptance is published; **what breaks it** — NPS stays a thin parallel pilot while the bulk of traffic lingers on legacy ISO-8583 NIP, or a vendor/outage incident forces rollback. **Watch:** published NPS-vs-NIP volume split, QR/merchant onboarding numbers, and whether CBN mandates migration the way it did dual-PoS routing.

Sources: https://nairametrics.com/2026/10/13/nibss-adopts-jpos-technology-for-national-payment-stack/ · https://nibss-plc.com.ng/nigerias-digital-payments-surge-to-n1-07-quadrillion-as-nibss-defines-future · https://leadership.ng/nibss-payment-stack-processes-n1-4trn-in-26-5m-transactions/ · https://insights.techcabal.com/nigeria-fintech-financial-inclusion-cbn-infrastructure-gap/ · https://guardian.ng/news/cbn-targets-95-financial-inclusion-with-digital-payments/ · https://www.heyfuturenexus.com/posts/brazil-india-instant-payments-growth-worldwide-pix-upi
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
