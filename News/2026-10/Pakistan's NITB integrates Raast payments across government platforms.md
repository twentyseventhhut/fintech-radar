---
title: "Pakistan's NITB integrates Raast payments across government platforms"
date: 2026-10-26
retrieved: 2026-10-26
tags:
  - company/nitb
  - industry/payments
  - region/asia
  - type/product
sources:
  - https://www.techjuice.pk/nitb-to-integrate-raast-digital-payments-across-government-platforms
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sd4de8942
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Pakistan's NITB integrates Raast payments across government platforms

> [!info] 2026-10-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] National Information Technology Board (NITB)launched integration of Raast and digital payment services across government platforms, enabling citizens to pay taxes, utility bills, and service fees electronically through multiple channels including cards, QR codes, and interbank transfers.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.techjuice.pk/nitb-to-integrate-raast-digital-payments-across-government-platforms>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** Pakistan's National Information Technology Board (NITB) — the autonomous e-governance agency under the Ministry of IT & Telecommunication that runs government digitization (E-Office, online land records, tourism-service digitization) — has launched an initiative to integrate Raast and digital payment services across government service platforms. The stated goal is to let citizens pay taxes, utility bills, licensing/certificate/application fees and other service charges electronically, through a wide set of channels: debit/credit cards, QR codes, interbank funds transfer (IBFT), branchless-banking agents, the Request-to-Pay (RTP) facility and Raast itself. NITB has reportedly invited banks and fintechs to build a single unified government digital-payment layer with real-time confirmation, automated reconciliation, reporting dashboards, refunds and chargeback/dispute handling, settling into NITB-identified accounts. ([techjuice.pk](https://www.techjuice.pk/nitb-to-integrate-raast-digital-payments-across-government-platforms/), [phoneworld.com.pk](https://www.phoneworld.com.pk/nitb-digital-payment-integration-raast-qr-government-services/))

**[1] What Raast is.** Raast is Pakistan's first national instant-payment system, operated by the State Bank of Pakistan (SBP), launched 11 Jan 2021. It settles funds in seconds via aliases ("Raast IDs", typically a mobile number) over central infrastructure connecting all banks. It is the local analogue of India's UPI or Brazil's Pix. By end-2025 Raast had ~48M registered users and processed close to 2 billion transactions worth ~Rs 50 trillion (per SBP's Financial Stability Review); in 2026 Raast Person-to-Merchant (P2M) volume crossed ~1M transactions/day, aided by a Rs 3.5bn merchant-onboarding subsidy. See [[Pakistan reports 96 million digital banking users]] (46M Raast ID transactions, 120M online-banking-user target by Jun 2026). ([en.wikipedia.org/wiki/Raast](https://en.wikipedia.org/wiki/Raast), [propakistani.pk](https://propakistani.pk/2026/05/05/raast-transactions-hit-rs-50-trillion-as-pakistanis-switch-to-online-payments/))

**[2] Why "across government platforms" matters — the G2P/P2G angle.** This is about government-to-person (G2P) and person-to-government (P2G) flows: subsidies, pensions, salaries, social-welfare disbursements on the outbound side, and tax/utility/fee collection on the inbound side. SBP has a parallel, broader plan to route ALL federal government payments through Raast by the end of fiscal year 2025-26, and the federal government set up a dedicated Government Payments & Receipts Transformation Unit (GPRTU) to drive it. NITB's move is the e-government front-end / integration execution of that policy: wiring Raast into the actual citizen-facing portals. ([dawn.com](https://www.dawn.com/news/1943042), [brecorder.com](https://www.brecorder.com/news/40385692/pakistans-digital-transformation-sbp-plans-to-route-govt-payments-through-raast))

**[3] Pakistan digital-payments backdrop.** Rails are maturing fast: PRISM+ (the ISO 20022 RTGS upgrade, see [[Pakistan launches PRISM+ payment and settlement system upgrade]]), QR-merchant acceptance up 245% to 3.8M merchants in FY26 processing 297M transactions ([[State Bank of Pakistan reports QR merchants up 245% in FY26]]), and card-scheme expansion via Mastercard tie-ups ([[Mastercard and BankIslami to expand card offerings in Pakistan]], [[Mastercard and Bank of Punjab expand Pakistan digital economy deal]]). G2P/P2G digitization is the next leg of a documented "war on cash."

**[4] So what / read-through.** Government rails are the single biggest lever for instant-payment adoption anywhere (cf. UPI's growth once the state leaned in). Mandating Raast across government portals converts millions of recurring, previously-cash/over-the-counter payments into digital flows, deepens Raast's network effects, and squeezes cash out of tax and fee collection (a transparency/revenue win for a fiscally-stressed state). For banks/fintechs, NITB's "single unified system" RFP is both an opportunity (a large captive payment-ops contract) and a concentration risk (one integrator/aggregator layer). Watch for: which banks/fintechs win the integration mandate, whether real-time reconciliation + chargeback handling actually ships, and interchange/fee economics on government QR/card flows.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
1. Is this an actual signed/launched integration, or an announcement/RFP/invitation-to-banks? The sourcing ("invites banks and fintechs to build") suggests early-stage procurement, not live rollout — the note title's "integrates" may overstate maturity.
2. What is the concrete scope of "government platforms" today — which ministries/portals are actually wired, versus aspirational? Any named live service (e.g., a specific tax or utility portal)?
3. Is NITB's initiative distinct from, or just the execution arm of, SBP's broader "all government payments via Raast by FY26" plan and the GPRTU unit? Risk of conflating three overlapping programs.
4. No timeline committed in the primary source — is there a go-live date, phased rollout, or pilot scope? "By June 2026" is SBP's target, not necessarily NITB's.
5. No adoption/volume numbers specific to this NITB initiative — the Rs 50tn / 48M users figures are system-wide Raast, not G2P-via-NITB.
6. Single source is techjuice.pk (a tech-news outlet), corroborated by phoneworld.pk — is there an official NITB/MoITT press release or notification? Primary-document gap.
7. Who bears the cost of card/QR interchange on government payments? If MDR is zero-rated for government, who subsidizes acquirers — is the model economically sustainable for participating banks?
8. Vendor-concentration / single-point-of-failure risk: a "single unified digital payment system" for all government services is a large availability and security target. What are the uptime/SLA and cybersecurity provisions?
9. Chargeback/dispute/refund handling for government fees is operationally hard (irreversibility norms differ for tax/fee payments) — is "chargeback handling" realistic here or boilerplate RFP language?
10. Financial-inclusion caveat: G2P digitization can exclude the unbanked/elderly if cash rails are withdrawn too fast — is there a cash fallback, and what share of the target population lacks a Raast ID?
11. Execution track record: how do Pakistan's prior e-government/payment digitization efforts rate on delivery vs announcement? Base rate for such mandates slipping is high.
12. Does routing government flows through a single aggregator layer create data-privacy/surveillance concerns over citizens' payment data held by NITB?
13. Competitive dynamics: does mandating Raast crowd out card schemes (Mastercard/Visa) and private wallets from government payment volume, and is that a deliberate policy or incidental?

Importance: 3/5 — Government-rail mandates are among the strongest adoption levers for instant payments, and this plugs Raast into high-frequency citizen flows, meaningfully advancing Pakistan's cash-displacement agenda. But it reads as an early-stage integration/procurement announcement (single trade-press source, no firm timeline, no NITB-specific adoption numbers, likely a sub-component of SBP's broader FY26 plan), so near-term, verifiable impact is limited. Nationally significant, globally minor.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Public instant-payment rails + G2P/P2G digitisation. Raast is Pakistan's central-bank-owned instant rail: it carried 2,755.2m payments worth PKR 80,050.8tn in the year to June 2026, more than double FY25's 1,276.0m (value +171% YoY), with ~48m registered users and >2.1m P2M merchants (per SBP Quarterly Payment Systems Review / Business Recorder, via brecorder.com, as of Q3 FY26). This NITB move is the government-rails layer on top: integrating Raast + cards + QR + IBFT + Request-to-Pay into federal service platforms so citizens pay taxes/utilities/fees digitally. Structure — a public-utility, state-owned rail (SBP builds/owns it, banks and EMIs distribute), so value accrues to the state operator, not a private incumbent; barriers are regulatory/mandate-driven, not network-effect moats held by any one firm. "Why now": the Cashless Pakistan agenda targets 100% G2P/P2G digitisation by December 2026; the Finance Division stood up a Government Payments & Receipts Transformation Unit (GPRTU) to force federal bodies onto Raast, and Raast is already being wired into gas/electricity billing for ~12m consumers (per profit.pakistantoday.com.pk, phoneworld.com.pk, as of Oct 2025–2026). The template is explicit: follow India's UPI (24.51bn transactions in Aug 2026) and Brazil's Pix (single-day record ~318m on 4 Sep 2026) — state-backed rails that leapfrogged cards (per medianama.com, fxcintel.com, 2026).

**Competitive landscape.** Sector KPIs: transaction volume/value, registered users, P2M merchant count, G2P/P2G digitisation rate, cash displacement. This is not a private-market contest — the "competitor" to Raast in G2P is cash and legacy over-the-counter/branch collection, not another rail. NITB's own PAK (Pakistan Asaan Khidmat) App collected Rs 3.27bn in government payments in July 2026 alone (per propakistani.pk, 2026-08), showing live traction of the citizen-facing front end. The supporting ecosystem is building fast: QR-enabled merchants grew 245% to 3.8m in FY26 ([[State Bank of Pakistan reports QR merchants up 245% in FY26]]); Pakistan reported 96m digital-banking users and 46m Raast ID transactions, targeting 120m by June 2026 ([[Pakistan reports 96 million digital banking users]]). Position: Pakistan is an early-stage follower — roughly where India's UPI was in its first few years — with top-down government mandate as the accelerant rather than organic consumer pull. The "moat" is a state mandate + the single national rail, not a defensible private franchise (analysis).

**Comps & multiples.** No valuation/round/deal attached — NITB and SBP are government bodies, so EV/Revenue, P/E etc. are not applicable (no data). Comparison is operational, not financial:
- Raast FY26: 2,755.2m txns / 48m users ≈ 57 txns per user per year (per SBP, via brecorder.com).
- Scale gap vs peers: UPI ~24.51bn txns in a single month (Aug 2026) dwarfs Raast's ~2.76bn for a full year — Raast is ~1–2 orders of magnitude below UPI maturity; Pix similarly far ahead (~318m/day peak).
Internal comps (base): [[State Bank of Pakistan reports QR merchants up 245% in FY26]], [[Pakistan reports 96 million digital banking users]], [[UPI accounts for 84% of India's digital payments in FY25]], [[Pix adds dispute button against fraud in Brazil]]. In-line read: Raast's growth trajectory (volume >2x YoY) is consistent with the early UPI/Pix S-curve; multiples "not computed — qualitative comparison" given no financials.

**Risk flags.**
1. **Execution / deadline risk** — the 100% G2P/P2G-by-Dec-2026 target is aggressive; a dedicated GPRTU exists precisely because federal institutions are hard to migrate, so "announced integration across government platforms" is far from "live and ubiquitous." Watch for slippage (analysis).
2. **Fraud / leakage into informal rails** — reporting already flags hawala operators exploiting Raast flows (per munaeem.org, 2026-09); forcing high G2P volume onto a young rail before fraud/dispute controls mature is a second-order risk to trust and to the anti-cash thesis.
3. **Registry-before-rails gap** — the UPI/Pix lesson is that identity/registry quality (Aadhaar, Brazil's family registry) matters more than the payment channel; a G2P account that can't also receive bills or merchant payments is a dead end (per orfonline.org, insights.muffinpay.com). Pakistan's financial-inclusion base and KYC coverage are the binding constraint, not the rail itself.

**What this changes (idea-lens).** This is a mandate-driven adoption catalyst, not a re-rating of any listed name — the beneficiaries are the banks/EMIs and QR-acquirers riding Raast distribution (Mastercard-linked expansions, QR merchants), not a single equity (analysis). Falsifiable thesis: if Raast's government-rail integration sticks, FY27 should show a step-change in P2G/G2P transaction share and continued >50% volume growth; it would be wrong if Dec-2026 digitisation stalls well below target or fraud forces a rollback. Trigger to watch: the next SBP Quarterly Payment Systems Review and the GPRTU's federal-onboarding progress.

Sources: https://www.techjuice.pk/nitb-to-integrate-raast-digital-payments-across-government-platforms · https://www.brecorder.com/news/40358567/raast-processes-over-892m-transactions · https://profit.pakistantoday.com.pk/2025/10/03/sbp-to-route-all-government-payments-through-raast-by-end-of-fy26/ · https://www.phoneworld.com.pk/government-payments-receipts-transformation-unit-raast-integration/ · https://propakistani.pk/2026/08/04/pak-app-collects-rs-3-27-billion-in-govt-payments-in-july/ · https://www.medianama.com/2026/09/223-brics-2026-dpi-payments-multipolar-financial-system/ · https://www.orfonline.org/research/digital-public-infrastructure-and-the-future-of-digital-payments-lessons-from-pix-and-upi · https://www.munaeem.org/2026/09/raast-digital-hawala-formal-payment-rails.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
