---
title: "emerchantpay and LoopingOne enable Motorhome Depot digital payments"
date: 2026-10-16
retrieved: 2026-10-16
tags:
  - company/emerchantpay
  - company/loopingone
  - industry/payments
  - region/uk
  - type/partnership
sources:
  - https://www.emerchantpay.com/insights/emerchantpay-and-loopingone-enable-digital-transactions-for-motorhome-depot-in-the-uk
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s22e4b4e9
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# emerchantpay and LoopingOne enable Motorhome Depot digital payments

> [!info] 2026-10-16 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 emerchantpay and LoopingOne enable digital transactions for Motorhome Depot in the UK. The setup gives Motorhome Depot seamless digital transactions and same day seller payouts. emerchantpay published the project as an online payments success story.

## Первоисточники

### emerchantpay.com
<https://www.emerchantpay.com/insights/emerchantpay-and-loopingone-enable-digital-transactions-for-motorhome-depot-in-the-uk>
*427 слов · jina*

Motorhome Depot becomes the first merchant to benefit from the joint offering, enabling a seamless digital transaction journey and same-day pay-out to sellers in the UK.

emerchantpay, a leading global payment service provider and acquirer, has partnered with LoopingOne, a deal flow platform for high-value transactions, to enable a fully digital transaction journey for Motorhome Depot, Europe’s largest motorhome marketplace.

The collaboration combines LoopingOne’s streamlined marketplace deal flow capabilities with emerchantpay’s payment infrastructure, bringing KYC verification, payment processing and funds settlement into a single digital transaction workflow for Motorhome Depot in the UK.

Motorhome Depot is the first merchant to benefit from the joint offering by emerchantpay and LoopingOne, which is available to businesses and marketplaces in the UK and Europe.

## Simplifying high-value transactions through a digital workflow

Motorhome Depot connects motorhome sellers with prospective buyers through its nationwide network of brokers. Once a sale has been agreed, brokers can use the LoopingOne platform to manage the transaction digitally, replacing a previous manual payment process with an integrated workflow.

emerchantpay provides payment processing services within the LoopingOne platform, while the solution enables funds to be paid out to the seller on the same day following a successful transaction.

Sigurdur Gudmundsson, Chief Commercial Officer at emerchantpay, said:

> “High-value transactions require payment infrastructure that gives every participant confidence while keeping the experience straightforward. Working with Looping One and Motorhome Depot demonstrates how a complex deal can be simplified within one digital journey. This solution is an important milestone and establishes a strong foundation for further shared success. We look forward to extending these capabilities to more businesses with complex, high-value transaction requirements.”

Mark van der Suis, Director and Co-founder at LoopingOne, said:

> “LoopingOne brings the different steps of a high-value transaction together in one digital workflow. By integrating emerchantpay’s payment capabilities into the platform, we can provide Motorhome Depot’s brokers and their customers with a straightforward way to manage the transaction from verification and payment through settlement, while enabling sellers to receive their funds quickly.”

Lucy Garbett, Financial Operations Manager at Motorhome Depot, said:

> “Buying or selling a motorhome is a significant transaction and we want the process to be as straightforward as possible. Our collaboration with LoopingOne and emerchantpay gives our broker network a single digital environment for transactions and the ability to receive their funds promptly.”

## Simplify your payment processes with emerchantpay

Looking to streamline complex transactions and deliver seamless payment experiences for your customers? Discover how emerchantpay’s payment solutions can support your business.

_Contact our team to discuss your payment needs._

## Контекст

<!-- enrichment:context -->
# Context-enrichment: emerchantpay + LoopingOne digitise Motorhome Depot transactions (UK)
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
emerchantpay (London-based PSP + Visa/Mastercard principal-member acquirer) and LoopingOne
(Amsterdam deal-flow / multi-party-payments platform) announced that **Motorhome Depot** — a UK
motorhome marketplace running a broker network — is the **first merchant** on their joint offering.
What is actually delivered: LoopingOne's platform now orchestrates the post-agreement steps of a
sale (KYC/KYB verification → payment processing via emerchantpay → settlement), replacing a
**previously manual payment process** with one digital workflow, and pays the seller out **same-day**
after a successful transaction. Available to businesses/marketplaces in the UK and Europe.

- **De-PR'd:** this is a **single-customer go-live of an integration**, not a new product or a
  licence/rail. The substance = "one marketplace moved its deal-closing from manual (phone/transfer
  into a holding account) to a KYC+pay+payout workflow." emerchantpay's role is the acquiring/payment
  leg inside LoopingOne's orchestration; LoopingOne is the actual platform the merchant touches.
- **Why framed this way (why it matters):** emerchantpay published it as an "online payments success
  story" on its own insights blog → this is marketing collateral, not a materially new capability. The
  anchor word "first merchant" signals there is **no track record yet** (0 prior live clients on this
  specific joint stack). "Same-day payout" is real and the concrete win, but Motorhome Depot already
  ran an FSCS-protected client/holding account that disbursed to sellers "promptly" — so the delta is
  **speed + digitisation of an existing flow**, not a new payment primitive. (analysis)
- **Silent on:** transaction volumes, ticket size, fees/take-rate, who carries fraud/chargeback
  liability on high-value (£20k–£100k+) vehicle sales, and whether funds are held in escrow vs merely
  processed. For "high-value transactions" the escrow/hold-release mechanics are the whole point and
  are unstated here.

## [1] Competitors / peers
Marketplace payment-orchestration with split payouts / staged (escrow-like) release is a crowded
UK/EU field: **Mangopay** (FCA EMI, wallet/escrow model, strong for held-funds + staged release),
**Lemonway** (ACPR, wallet marketplace flows), **Stripe Connect** and **Adyen for Platforms**
(sophisticated orchestration), **Ryft** (FCA-licensed, "unlimited escrow" + real-time splits, UK
marketplace-native), plus PayPal. LoopingOne's pitch is "connect your preferred payment + KYC
solutions via one platform" — i.e. an orchestration layer that is **payment-partner-agnostic**, which
is exactly how it can bolt emerchantpay underneath.
- **Position:** catching-up / niche. The capabilities on display (KYC/B + split/same-day payout +
  escrow-style flow) are table-stakes at Mangopay/Ryft/Stripe Connect. The differentiation claim is
  the **high-value, broker-mediated, vertical** (motorhomes), not the tech. (analysis)
- **Why the lay of the land (2nd order):** generic marketplace PSPs win horizontal breadth; the only
  durable edge in high-value verticals is domain-specific deal flow (broker commission splits, title
  handover, KYC on both legs). LoopingOne is trying to own that vertical workflow and treat the
  acquirer as a swappable commodity — which structurally **caps emerchantpay's value capture** to the
  interchange/processing leg. (hypothesis)

## [2] Company history / fit
**emerchantpay** (founded 2002; FCA Payments Institution 2011; Visa/Mastercard principal member 2012;
acquiring launched 2014; ~358 staff, 19 offices) is a mid-size global PSP+acquirer, strong in iGaming
and cross-channel acquiring. It has a pattern of **partnership/integration announcements** to show
expansion beyond commodity acquiring — cf. [[Emerchantpay and Visa offer instalment payments for UK merchants]]
(May 2026, Visa Instalments at UK checkout). This Motorhome Depot item fits the same playbook:
commodity acquiring → needs differentiated, embedded, higher-stickiness use cases (instalments,
marketplace deal flow) to defend take-rate. (analysis)
**LoopingOne** (Amsterdam, founded 2021 by Bob Voermans/Freek Dix/Mark van der Sluis, ex-Mastercard/
Ingenico/PayU) raised **€2M** and took an **€800K strategic investment from Ebury** (plus an Ebury
partnership) to advance its KYC/B + multi-party-payment solution. So this deal is LoopingOne landing a
named reference customer and an acquiring partner — meaningful for a small 2021 startup, minor for
emerchantpay.

## [3] Novelty / value-add / traction
- **New?** Not technologically. The genuine novelty is narrow: a specific UK high-value vertical
  (motorhome brokerage) moving from manual to digital deal flow with same-day seller payout. The
  underlying primitives (orchestration, KYC/B, split/same-day payout, escrow) all predate this.
- **Traction:** **one merchant, go-live, no numbers.** "First merchant," no GMV, no volume, no fee
  data. This is announcement-level, not adoption-level.
- **Who captures the margin (2nd order):** LoopingOne owns the merchant relationship and the workflow;
  emerchantpay is the interchangeable processing rail. For emerchantpay this is a small acquiring
  volume stream dressed as strategic; the real strategic value accrues to LoopingOne (reference logo +
  acquiring partner it can replicate). The value-add to Motorhome Depot (speed, single environment) is
  real but incremental. (analysis)

## [4] What's next / market sentiment
Both sides signal intent to extend the joint offering to "more businesses/marketplaces with complex,
high-value transaction requirements" in UK/Europe — i.e. a template deal they want to replicate. Watch
for a **second named merchant and any volume disclosure**; absent that, treat this as a pilot logo.
- **Risks / silences:** fraud & chargeback liability on five-figure vehicle sales; escrow/hold-release
  mechanics (unstated); competition from Mangopay/Ryft/Stripe Connect who can serve the same flow;
  LoopingOne's small scale and dependence on swappable acquirers (including non-emerchantpay via Ebury).
- **Sentiment:** neutral/low. Routine PSP partnership PR, no market-moving figures. (analysis)

## Sources
- emerchantpay insights (primary, in note body): https://www.emerchantpay.com/insights/emerchantpay-and-loopingone-enable-digital-transactions-for-motorhome-depot-in-the-uk
- The Paypers: https://thepaypers.com/payments/news/emerchantpay-and-loopingone-digitise-transactions-for-motorhome-depot
- Financial IT: https://financialit.net/news/payments/emerchantpay-and-loopingone-enable-digital-transactions-motorhome-depot-uk
- LoopingOne funding (Ebury €800K / €2M): https://siliconcanals.com/loopingone-bags-800k/ ; https://siliconcanals.com/amsterdams-loopingone-raises-2m/ ; https://ebury.com/resources/blog/loopingone-secures-e800-000-strategic-investment-from-ebury-and-forms-partnership-between-companies
- emerchantpay profile/history: https://www.emerchantpay.com/about-us/ ; https://thepaypers.com/payments/company-information/emerchantpay
- Motorhome Depot seller/buyer flow: https://www.motorhomedepot.com/page/sellers-guide
- Marketplace PSP comps (Mangopay/Ryft/Lemonway/Stripe Connect): https://www.ryftpay.com/blog/split-payment-providers-for-uk-marketplaces-2026
- Internal: [[Emerchantpay and Visa offer instalment payments for UK merchants]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **How many live merchants are on this joint offering?** One — Motorhome Depot, explicitly "first
   merchant." Zero track record on this specific stack.
2. **Any transaction volume, GMV, or ticket-size data?** Open / undisclosed. No numbers at all.
3. **Is this a new product or a single-customer integration go-live?** A go-live of an existing
   integration/orchestration capability for one vertical customer — not a new product or rail.
4. **What is the actual delta for Motorhome Depot?** Manual payment process → digital KYC+pay+settle
   workflow with same-day seller payout. Speed + digitisation of a flow they already ran (FSCS client
   account), not a new payment primitive.
5. **Who captures the margin?** LoopingOne owns the merchant/workflow relationship; emerchantpay is the
   swappable acquiring/processing leg (and LoopingOne also partners Ebury). Value capture for
   emerchantpay is capped to processing.
6. **Is "same-day payout" novel?** No — table-stakes across Mangopay, Ryft, Stripe Connect, Lemonway.
   The claimed differentiation is the high-value broker-mediated vertical, not the tech.
7. **Who carries fraud/chargeback liability on five-figure vehicle sales?** Open — unstated. Material
   for high-value transactions.
8. **Escrow vs mere processing — is there hold/release?** Open. "Funds settlement" is mentioned but the
   hold/release/escrow mechanics (the crux for high-value deals) are not specified.
9. **Fees / take-rate / commercial terms?** Open — undisclosed.
10. **Is this the same event as the May 2026 emerchantpay+Visa instalments note?** No — different
    partner (LoopingOne vs Visa), different product (marketplace deal flow vs checkout instalments),
    different merchant. FRESH, not a duplicate.
11. **Is the May note the same deal re-reported?** No; only the shared actor emerchantpay. Confirms fresh.
12. **How exposed is this to competitors?** Highly — Mangopay (FCA EMI, escrow), Ryft (FCA, unlimited
    escrow + real-time splits), Stripe Connect, Adyen for Platforms all serve the same flow.
13. **Why does emerchantpay publish this on its own blog?** Marketing collateral ("success story") to
    show expansion beyond commodity acquiring — consistent with its Visa Instalments PR pattern.
14. **How strategic is this for each party?** Meaningful reference logo + acquiring partner for a small
    2021 startup (LoopingOne, €2M + €800K Ebury); minor incremental acquiring volume for emerchantpay.
15. **What would make this matter more?** A second named merchant plus disclosed volume/GMV; until then
    treat as a pilot logo.

Importance: 2/5.
_(Routine PSP partnership PR; real but incremental value-add; single customer, no numbers, no novel
primitive, fully contested competitive space. Fresh, not a duplicate.)_
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits in UK/EU marketplace payments — specifically payment facilitation (PayFac-as-a-Service) layered under a vertical high-value-goods marketplace. The PayFac-as-a-Service market was ~$8.2bn in 2025, projected to ~$34.6bn by 2034 at ~17.3% CAGR (per dataintelo, as of 2026); a second source puts it at ~$6.9bn (2024) → ~$36.3bn (2033) at ~18.2% (per growthmarketreports). Estimates diverge by source and vendor definition — treat the ~17–18% CAGR as directional, not a hard TAM. Structure: the UK marketplace-payments stack is fragmented and increasingly commoditised at the gateway layer (Stripe Connect, Adyen for Platforms, Mangopay, Ryft, Airwallex all compete for the same split-payment/escrow/KYC-payout feature set). Entry barriers are regulatory (FCA licensing, PSD2 SCA, per-seller KYC) and operational (fraud liability on large tickets), not technical — the features themselves are table stakes. **Why now:** marketplaces for high-ticket physical goods (motorhomes, vehicles, equipment) are migrating off manual bank-transfer/escrow processes onto embedded digital flows; the moat for a PSP is distribution into verticals, not the rails.

**Competitive landscape.** Sector KPIs: TPV/GPV, take rate (per-transaction margin), and attach/settlement speed. None are disclosed in this note. Key players by basis of competition — Adyen/Nuvei/Global Payments compete on scale + single-platform processing; Stripe Connect / Mangopay / Ryft on marketplace-native split-payment + embedded KYC; Escrow.com on single high-value-item escrow (fees from ~0.89% of transaction value, per decipherzone/web). emerchantpay positions as a "global PSP and acquirer" (London-based; "Payment Acquirer of the Year 2025" at the Brit Fintech Awards, per web) supplying the processing rails inside LoopingOne's deal-flow platform — i.e. emerchantpay is the acquiring layer, LoopingOne owns the merchant relationship and workflow. Recent protagonist move: emerchantpay + Visa UK instalments, 2026-05 ([[Emerchantpay and Visa offer instalment payments for UK merchants]]) — same UK-merchant-enablement playbook. Position: **niche / catching-up** in marketplace payments vs Adyen/Stripe platform offerings; the differentiation here is the LoopingOne partnership and same-day seller payout, not a structural moat `(analysis)`.

**Comps & multiples.** No deal size, valuation, TPV or take rate is disclosed for this partnership, and neither emerchantpay nor LoopingOne is public — so no entity-level multiple can be computed; multiple = **no data / [UNSOURCED]**. For sector context on listed/transacted acquiring peers (NOT the protagonist's valuation): Adyen ~5.7x EV/Revenue (Sep 2026, per multiples.vc; ~7.9x on Aug-2026 trailing per another cut — gross-vs-net-revenue sensitive); Nuvei taken private by Advent at $6.3bn = ~5.0x on ~$1.3bn revenue (Apr 2024, per web); Nuvei→Payoneer ~$2.75bn ≈ ~2.0x EV/2026E revenue (Jun 2026, per windsordrake). These are co-equal-scale global acquirers, not comparable to a private vertical-marketplace integration, so: **distribution not computed, qualitative only.** emerchantpay's own revenue is unverifiable (web estimates range $100M–$500M to "$1B–$10B" — too wide to use). Internal comp: [[Emerchantpay and Visa offer instalment payments for UK merchants]].

**Risk flags.**
1. **De-PR / announced vs live:** emerchantpay published this as its own "success story" and Motorhome Depot is explicitly the *first* merchant — single reference customer, no volume. Risk the joint offering doesn't scale beyond one logo. Second-order: PR-led go-to-market with no disclosed pipeline is weak evidence of traction.
2. **Concentration + silence on economics:** no TPV, take rate, fraud-liability split, or ticket-size cap disclosed. On high-value transactions (motorhomes = £10k–£100k+), chargeback/fraud liability and settlement risk sit somewhere in the emerchantpay↔LoopingOne stack and are unaddressed — a material gap for an acquirer carrying same-day payout risk.
3. **Disintermediation / rails commoditisation:** emerchantpay is one layer under LoopingOne, which owns the merchant. If marketplace-native PSPs (Stripe Connect, Mangopay, Adyen for Platforms) offer the same KYC+split+payout natively, the acquiring layer is the most substitutable and lowest-margin part of the stack. Second-order: margin accrues to whoever owns distribution (LoopingOne/Motorhome Depot), not the rails.

**What this changes (idea-lens).** Marginal, not a re-rating: a single vertical integration in UK high-value-goods marketplaces, consistent with embedded/marketplace payments eating manual escrow flows `(analysis)`. Falsifiable thesis: emerchantpay is building a repeatable "high-value transaction" PSP vertical — **watch for a second named high-ticket marketplace merchant (vehicles/equipment/property) on the same LoopingOne stack within ~2 quarters.** If none materialises and it stays a one-logo case study, treat it as PR, not a product line.

Sources: https://www.emerchantpay.com/insights/emerchantpay-and-loopingone-enable-digital-transactions-for-motorhome-depot-in-the-uk · https://dataintelo.com/report/payfac-as-a-service-market · https://growthmarketreports.com/report/payfac-as-a-service-market · https://multiples.vc/public-comps/adyen-valuation-multiples · https://windsordrake.com/payfac-payment-rails-orchestration-valuation/ · https://www.decipherzone.com/blog-detail/escrow-payment-solutions
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
