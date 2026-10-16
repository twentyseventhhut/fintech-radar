---
title: "Vipps MobilePay reaches more merchants via Rootline PSP API"
date: 2026-10-13
retrieved: 2026-10-14
tags:
  - company/vipps-mobilepay
  - company/rootline
  - industry/payments
  - region/europe
  - type/partnership
sources:
  - https://rootline.com/blog/vipps-mobilepay-reach-more-merchants-through-rootline
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s1f6bc202
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Vipps MobilePay reaches more merchants via Rootline PSP API

> [!info] 2026-10-13 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Vipps MobilePay reaches more merchants through Rootline, which integrated the wallet using Vipps MobilePay's new PSP API. Platforms using Rootline can now offer Vipps MobilePay to all their merchants without each merchant needing its own agreement. Event platform Preo processed 20,000 MobilePay payments through Rootline during Copenhagen's Kulturnatten.

## Первоисточники

### rootline.com
<https://rootline.com/blog/vipps-mobilepay-reach-more-merchants-through-rootline>
*397 слов · direct*

Back to articles 
Vipps MobilePay reach more merchants through Rootline
Emilie Brink Korsled 
Fintech Specialist 
 Oct 13, 2026 
 Oct 13, 2026 
At a festival, in an online store or somewhere completely different: Vipps MobilePay should be there when people pay. Now, a new partnership with Rootline is making payments available to even more businesses.
Rootline provides payment infrastructure to platforms that, in turn, serve many merchants. Many PSPs are built for one-to-one transactions between a business and its customers. Rootline is built specifically for platform payments, where one platform can provide payment services to hundreds or thousands of merchants. The company has now integrated Vipps/MobilePay directly into its platform setup, using Vipps MobilePay’s new PSP API.
This means that platforms using Rootline can now offer Vipps MobilePay to all their merchants, without each merchant needing its own agreement. 
"Our ambition is very, very simple: people should be able to use Vipps/MobilePay in as many places and payment situations as possible. This means we need to be available through the platforms and payment providers that businesses already use. Rootline allows us to reach many merchants through a single integration," says Vegar Heir, Chief Commercial Officer at Vipps.
Preo is one of the platforms using Rootline. It provides commerce solutions for festivals and events including Copenhagen’s Kulturnatten, where 20,000 MobilePay payments were processed through Rootline during last weekend. Preo also works with festivals such as  Smukfest, Pinkpop and Lowlands. 
"The partnership has been very smooth, and we got Vipps MobilePay live in less than a month, says Thimo Bosma," Head of Product at Rootline. Want to learn more about the integration and Rootline? Book a meeting with us here 
TAKE CONTROL
Talk to our team about routing, fees, reconciliation, and payouts on Rootline. 
TAKE CONTROL
Talk to our team about routing, fees, reconciliation, and payouts on Rootline. 
TAKE CONTROL
Talk to our team about routing, fees, reconciliation, and payouts on Rootline. 
 Product 
 Online Payments 
 In-Person Payments 
 Cross-Channel Payments 
 Money Management 
 Ops & Insights 
 Developers 
 Documentation 
 Get Started 
 API Reference 
 Company 
 About us 
 Case studies 
 Blog 
 Careers 
 Legal 
 Product 
 Online Payments 
 In-Person Payments 
 Cross-Channel Payments 
 Money Management 
 Ops & Insights 
 Developers 
 Documentation 
 Get Started 
 API Reference 
 Company 
 About us 
 Case studies 
 Blog 
 Careers 
 Legal 
 Product 
 Online Payments 
 In-Person Payments 
 Cross-Channel Payments 
 Money Management 
 Ops & Insights 
 Developers 
 Documentation 
 Get Started 
 API Reference 
 Company 
 About us 
 Case studies 
 Blog 
 Careers 
 Legal

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Vipps MobilePay reaches more merchants via Rootline PSP API
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
De-PR'd: Rootline — an Amsterdam platform-payments infrastructure provider (founded 2021, ~$6.1M raised; Coatue, Firstminute, Pretiosum) — integrated the Vipps MobilePay wallet into its stack via Vipps MobilePay's **existing, documented PSP API** (`developer.vippsmobilepay.com/docs/APIs/psp-api`). The net effect: any platform/marketplace already on Rootline can now offer Vipps MobilePay to its sub-merchants under **one agreement** instead of each merchant signing its own Vipps deal. Named proof-point: event platform **Preo** (Smukfest, Pinkpop, Lowlands) ran **20,000 MobilePay payments** through Rootline at Copenhagen's Kulturnatten "last weekend"; Rootline says it went live "in less than a month".
- **Why framed as a "new partnership":** the PSP API itself is NOT new — Vipps has published a PSP API for years and already lets third parties (e.g. Adyen) offer Vipps. The genuinely new thing is a **platform-economy distributor** (Rootline) consuming that API to fan Vipps out to hundreds/thousands of sub-merchants via sub-merchant onboarding — i.e. distribution reach, not a protocol. The PR leads with "reach more merchants" precisely because the delta is reach, not capability.
- **What the numbers hide:** "20,000 payments at one festival" is a single-event volume, not GMV, not recurring run-rate, not merchant count onboarded. No disclosed economics (take-rate split Vipps↔Rootline↔platform), no fraud-liability or exclusivity terms. "Live in under a month" measures integration speed, not adoption.

## [1] Competitors / peers
Platform-payments / PtPP (payment-facilitator-for-platforms) rails that distribute local methods to sub-merchants: **Stripe Connect, Adyen for Platforms, Mollie** (which has aggressively pushed into the Nordics/EEA — see [[Mollie commits €350 million to complete 30-country EEA expansion]]), **PPRO** (local-method aggregation, now exclusive Nordic BNPL partner for Qliro — [[Qliro becomes PPRO's exclusive Nordic BNPL partner]]), Checkout.com. On the wallet-acceptance side Adyen already lists Vipps as a method; Kustom is now Vipps' recommended checkout partner after buying the Checkout merchant contracts ([[Vipps sells MobilePay Checkout merchant contracts to Kustom]]).
- **Position:** Rootline is a small ($6.1M) challenger vs Adyen/Stripe/Mollie; adding Vipps is **table-stakes catch-up**, not a lead — to be credible in the Nordics a platform acquirer MUST carry Vipps MobilePay (dominant wallet). So this is Rootline closing a coverage gap, parity move.
- **Second-order:** the real contest is who owns the **sub-merchant onboarding + reconciliation + payout** layer for platforms. Vipps is method-agnostic about which orchestrator carries it (Adyen, Rootline, Kustom); the margin at the method level accrues to Vipps, the platform-plumbing margin is fought over by orchestrators. Vipps wins reach regardless of which rail wins.

## [2] Company history / fit
Vipps MobilePay: ~12.4M users (end-2025; ~4.7M NO, ~4.7M DK, ~2.9M FI), ~400k merchants, dominant NO/DK/FI wallet. Recent trajectory is a clear **"be everywhere" distribution push**: Tink Pay-by-Bank for P2P in Finland ([[Vipps MobilePay selects Tink for Pay by Bank in Finland]]), Greenland expansion + cross-border P2P ([[Vipps MobilePay expands to Greenland]]), Klarna added inside the app ([[Klarna becomes payment option in Vipps and MobilePay apps]]), co-founding the European Network for Payments for cross-wallet interoperability ([[European wallets form European Network for Payments]]), and the single-brand rebrand to "Vipps" across the Nordics from 12 Jan 2027 ([[Vipps MobilePay rebrands as Vipps across the Nordics]]).
- **Why act this way:** Vipps' moat is the consumer install base, not acquiring. CCO Vegar Heir's quote ("available through the platforms and payment providers businesses already use") is the strategy stated plainly — Vipps monetizes **ubiquity of acceptance**, so it pushes the wallet through every orchestrator rather than fighting to own merchant relationships (which it just exited by selling Checkout contracts to Kustom). Rootline is one more distribution node in a deliberately outsourced acceptance network.

## [3] Novelty / value-add / traction
Genuinely new: a platform-payments orchestrator aggregating Vipps under **one agreement for its whole sub-merchant book** — meaningful for festival/event/marketplace platforms where per-merchant Vipps contracts were friction. NOT new: the PSP API, Vipps-via-third-party acceptance in general.
- **Is the value-add real?** For Rootline, yes but modest: Vipps is a must-have Nordic method, so this is a credibility/coverage unlock that lets Rootline compete for Nordic platform clients. Traction is thin and single-anchor (Preo + 20k Kulturnatten payments); no merchant-count, no GMV, no multi-platform rollout disclosed.
- **Who captures margin:** method economics → Vipps; orchestration/reconciliation/payout margin → Rootline (contested vs Adyen/Stripe/Mollie). Because Vipps is deliberately method-agnostic, Rootline gets no exclusivity — the same wallet is one integration away for every rival orchestrator, so this does not durably differentiate Rootline.

## [4] What's next / market sentiment
Watch for (a) additional Rootline platform clients going live with Vipps beyond Preo, (b) whether Rootline discloses recurring volume/GMV vs one-off event spikes, (c) the 12-Jan-2027 rebrand simplifying "Vipps" acceptance branding across DK/FI. Regulatory backdrop: EU platform-payments sit under PSD2/PSD3 and sub-merchant/agent oversight; Rootline operates without its own full licence by design (its pitch is "run your own stack without a licence"), which raises the standard agent/distributor compliance questions.
- **Why the market goes this way (analysis):** platform/marketplace commerce is the growth segment, and local wallets (Vipps, Bizum, MB WAY, Wero) are consolidating cross-border (ENP). Orchestrators that carry the full local-method set win platform deals. Counterintuitive second-order: the more Vipps makes itself available through every orchestrator, the **less any single orchestrator can differentiate on "we have Vipps"** — commoditizing wallet access and shifting orchestrator competition to price, onboarding UX and payout/reconciliation depth.

## Sources
- rootline.com/blog/vipps-mobilepay-reach-more-merchants-through-rootline (primary)
- rootline.com — product/company; dealroom/pitchbook (founded 2021, ~$6.1M, Coatue/Firstminute/Pretiosum)
- developer.vippsmobilepay.com/docs/APIs/psp-api (PSP API is pre-existing)
- vippsmobilepay.com rebrand release; Wikipedia Vipps/MobilePay (user/merchant figures)
- Internal: [[Vipps MobilePay rebrands as Vipps across the Nordics]], [[Vipps sells MobilePay Checkout merchant contracts to Kustom]], [[Vipps MobilePay selects Tink for Pay by Bank in Finland]], [[European wallets form European Network for Payments]], [[Mollie commits €350 million to complete 30-country EEA expansion]], [[Qliro becomes PPRO's exclusive Nordic BNPL partner]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is the PSP API itself new?** No (answered). Vipps' PSP API is long-published and already used by third parties (Adyen). The news is Rootline distributing it to sub-merchants, not a new capability.
2. **Is this a genuinely new event or a re-run?** Fresh — distinct Rootline integration + Preo/Kulturnatten proof-point; no prior note covers this tie-up. Related but distinct from the Kustom Checkout sale and the rebrand.
3. **What's the real traction?** Open/thin: one named platform (Preo) + 20,000 payments at a single festival. No merchant count onboarded, no GMV, no run-rate, no second platform cited.
4. **What are the economics?** Open: no disclosure of the take-rate split between Vipps, Rootline and the platform, nor whether Rootline marks up Vipps acceptance.
5. **Who carries fraud/chargeback liability** across the Vipps → Rootline → platform → sub-merchant chain? Open — unstated.
6. **Any exclusivity?** No — Vipps is deliberately method-agnostic and available via Adyen/others, so Rootline gets no moat from this.
7. **Does "20,000 payments" mean recurring volume?** No — it is a single-event spike (Kulturnatten); not evidence of durable run-rate.
8. **Why did Vipps exit merchant contracts (Kustom) yet push acceptance via Rootline?** Consistent strategy: Vipps monetizes wallet ubiquity, outsources acquiring/checkout — distribution not ownership.
9. **How material is Rootline?** Small: ~$6.1M raised, founded 2021; a challenger vs Adyen/Stripe/Mollie, not a category leader.
10. **Is this competitively differentiating for Rootline?** Marginally — it's catch-up table-stakes for Nordic platform credibility, not a lead.
11. **Does it move the needle for Vipps?** Barely — one more distribution node among many; immaterial to Vipps' ~400k-merchant, 12.4M-user base.
12. **Compliance/licensing exposure?** Open — Rootline's pitch is running a payment stack without a full licence; raises standard agent/sub-merchant oversight questions under PSD2/PSD3.
13. **Who needs whom more?** Rootline needs Vipps (must-have Nordic method) more than Vipps needs Rootline (one of many orchestrators).
14. **Second-order risk for orchestrators?** Wallet access commoditizes; "we have Vipps" stops differentiating → competition shifts to price/onboarding/payout depth.
15. **What would upgrade importance?** Multiple platforms live + disclosed recurring GMV, or an exclusive/preferred-partner status — none present.

**Importance: 2/5** — real but minor: a small orchestrator closing a must-have-method coverage gap via a pre-existing API; single-anchor, event-spike traction, no economics, no exclusivity. Fits Vipps' known "be everywhere" distribution story without changing it.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Nordic mobile-wallet / acquiring + platform-PSP connectivity. Vipps MobilePay counts ~13m Nordic users (NO ~4.68m, DK ~4.74m, FI ~2.86m, SE ~0.16m as of YE2025) and 400,000+ merchants (per Vipps/Wikipedia, via WebSearch, as of 2026) — effectively the default domestic wallet in NO/DK/FI, but it is NOT a card scheme; it rides local rails and bank distribution. Structure: the acquiring/PSP value chain is fragmenting at the "platform payments" layer — marketplaces/event/SaaS platforms want to onboard thousands of sub-merchants under one integration rather than one contract each. Rootline (Amsterdam B.V., PSD2-licensed PSP, ~$6.1m raised; investors incl. Coatue, firstminute, Pretiosum — per Pitchbook/Tracxn, via WebSearch) targets exactly this niche vs one-to-one PSPs. Why now: (1) Europe's sovereignty push — in Sep-2026 Vipps co-founded the Madrid-based "European Network for Payments" with Bancomat/Bizum/EPI-Wero/SIBS-MB WAY (~130m users, 13 countries, per EPI/KBC, via WebSearch), raising the stakes on wallet distribution reach vs Visa/Mastercard; (2) Vipps' own retreat from running direct acquiring — it sold its Checkout merchant book to Kustom in Mar-2026 [[Vipps sells MobilePay Checkout merchant contracts to Kustom]], signalling a deliberate pivot from owning merchant relationships to being a payment method distributed through partners' rails.

**Competitive landscape.** Sector KPIs: active wallet users, merchant/acceptance reach, TPV, PSP take rate, platform onboarding time. Vipps' distribution competitors as a *payment method* = cards (Visa/Mastercard), Swish (SE), BLIK (PL) and increasingly Wero/EPI across Europe; its *connectivity* partners = PSPs/platforms (Rootline here; Klarna, Kustom, PPRO also integrate Vipps/MobilePay) [[Klarna integrates Vipps MobilePay across Nordics]] [[PPRO brings Swish payments into PayPal for Swedish shoppers]]. Basis of competition for Vipps: ubiquity of acceptance (every checkout where it's offered) rather than price. Recent moves: PSP-API launch enabling single-integration reach (this item, Oct-2026); Vipps rebrand to drop "MobilePay" across Nordics (Oct-2026) [[Vipps MobilePay rebrands as Vipps across the Nordics]]; ENP interoperability entity (Sep-2026) [[European wallets form European Network for Payments]]. Vipps' position: dominant/ahead domestically (near-universal NO/DK/FI consumer penetration = strong network-effect moat), but *catching up / niche on the merchant-distribution layer* — having exited direct acquiring, its acceptance now depends on third parties' integrations. Rootline's own position: sub-scale new entrant (small funding) in a crowded PSP market; its edge is the platform/sub-merchant model, not balance sheet.

**Comps & multiples.** No valuation, round or deal economics disclosed in this item — it is a technical integration partnership, so EV/Rev, P/S and price-per-user are **"no data"** for both parties. Rootline is private (~$6.1m raised, no post-money disclosed → [UNSOURCED]); Vipps is bank-owned (DNB-led consortium), not separately listed → no public multiple. Internal comps are directional, not valuation: [[Vipps sells MobilePay Checkout merchant contracts to Kustom]] (Mar-2026; ~3,000 merchants + >NOK 7bn volume transferred — a size anchor for Vipps' *direct* acquiring book it chose to divest), [[Klarna integrates Vipps MobilePay across Nordics]] and [[Klarna becomes payment option in Vipps and MobilePay apps]] (distribution-via-partner precedent). Distribution not computed — qualitative comparison only; no comparable public multiples exist.

**Risk flags.**
1. **Disintermediation of the merchant relationship.** By distributing through Rootline/Kustom/Klarna, Vipps becomes a payment *method* behind someone else's stack and reconciliation — it keeps consumer reach but cedes the merchant relationship, data and the acquiring take-rate to the PSP layer (second-order: thinner economics, weaker pricing power vs its own former Checkout business).
2. **Partner concentration / counterparty quality.** Rootline is a small, thinly-funded (~$6.1m) PSD2 PSP; leaning on such partners for acceptance reach exposes Vipps to a partner's settlement, solvency and compliance risk for flows it no longer controls end-to-end.
3. **De-PR / evidence gap.** The only live proof-point is one event platform (Preo) processing 20,000 MobilePay payments at Kulturnatten — a single weekend, single use case. "Platforms can now offer it to all their merchants" is *announced capability*, not demonstrated at scale; economics, fees and fraud-liability split are silent in the PR.
4. **Strategic dependence vs card rails & Wero.** Vipps' reach still depends on bank/partner distribution within a market where Visa/Mastercard set the acceptance default and Wero/ENP is the longer-term European play; a wallet without its own acquiring must keep winning integrations to stay ubiquitous (execution risk).

**What this changes (idea-lens).** `(analysis)` This confirms Vipps' deliberate shift from vertically-integrated acquirer to a widely-distributed payment *method* — accept more, own less. Falsifiable thesis: if Vipps is truly out-sourcing acceptance, expect further PSP/platform integrations (and no re-entry into direct merchant acquiring) over the next 2–3 quarters. Watch: whether partner platforms disclose real multi-merchant adoption (not just one Preo-style showcase) and whether Vipps' ENP interoperability role starts to matter more for reach than any single PSP tie-up. Thesis breaks if Vipps re-launches its own checkout/acquiring product.

Sources: https://rootline.com/blog/vipps-mobilepay-reach-more-merchants-through-rootline · https://en.wikipedia.org/wiki/Vipps · https://pitchbook.com/profiles/company/650347-66 · https://epicompany.eu/media-insights/european-network-for-payments/ · https://www.techradar.com/pro/eu-payment-providers-are-building-a-new-network-to-cut-down-on-us-tech-reliance
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
