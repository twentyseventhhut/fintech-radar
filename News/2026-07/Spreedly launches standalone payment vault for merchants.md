---
title: "Spreedly launches standalone payment vault for merchants"
date: 2026-07-16
retrieved: 2026-07-16
tags:
  - company/spreedly
  - industry/payments
  - industry/infrastructure
  - region/us
  - type/product
sources:
  - https://newsletter.thepaypers.com/i/pA8cKuEoHRTl2th5vb4bsOijLpai2SiuHCwnwUHHARONMIqW5d73k5ZL6N5ER2JSEqbpxugOIMRsm_y_kHQ7_ChX1PZY5981uBjDhxilk6zkFmm8M6EsA2169W6q_uqLez7u1STmsJTadTujxrnjOPpcaBXwkruA
status: enriched
n_mentions: 1
channels:
  - "The Paypers"
story_id: sb5613f41
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Spreedly launches standalone payment vault for merchants

> [!info] 2026-07-16 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: The Paypers

## Агрегированный текст (из дайджестов)

[The Paypers] Spreedly launches standalone payment vault for merchants

## Первоисточники

### newsletter.thepaypers.com
<https://newsletter.thepaypers.com/i/pA8cKuEoHRTl2th5vb4bsOijLpai2SiuHCwnwUHHARONMIqW5d73k5ZL6N5ER2JSEqbpxugOIMRsm_y_kHQ7_ChX1PZY5981uBjDhxilk6zkFmm8M6EsA2169W6q_uqLez7u1STmsJTadTujxrnjOPpcaBXwkruA>
*663 слов · direct*

Spreedly launches standalone payment vault for merchants
Claudia Pincovski
16 Jul 2026 / 4 Min Read
Spreedly has launched a standalone payment vault that allows merchants to store and manage payment credentials independently.
The US-based payments infrastructure provider has made available a version of its vault technology as a stand-alone product, decoupled from its broader payments orchestration platform. The offering is aimed at merchants seeking to secure and control their own payment credentials without committing to a full orchestration setup from the outset.
Credential control as a competitive factor
According to Spreedly, the role of the payment vault has expanded beyond passive credential storage. Capabilities such as network tokenisation, account updater services, and stored-credential optimisation increasingly influence authorisation rates and overall payment performance. This has made control over payment credentials a factor in how merchants manage provider relationships and payment outcomes.
The company noted that payment providers, which have traditionally kept credentials tied to their own systems, are increasingly supporting merchant-controlled vaults and credential portability. Spreedly said this shift removes a longstanding barrier for merchants looking to add or switch payment providers without re-establishing stored credentials each time.
Vault capabilities and platform structure
Spreedly's standalone vault includes PCI DSS Level 1 tokenisation, designed to keep raw payment data out of merchant systems. The vault supports credential portability across more than 100 payment providers, according to the company, without requiring merchants to commit to a single processor. It also incorporates network tokenisation and account updater functions intended to help keep stored credentials current and support authorisation performance.
Spreedly said merchants can adopt the vault while continuing to operate a single payment provider per region. As requirements evolve, merchants can then build their own routing and orchestration layer on top of the portable credentials, or adopt Spreedly's existing orchestration platform, without needing to migrate or re-vault payment credentials.
Spreedly has offered payment vault functionality as part of its orchestration platform for several years. The standalone product allows merchants to begin with credential storage alone and expand into additional platform capabilities later, on the same underlying infrastructure.
Market context
Spreedly reported that stored-credential transactions now represent 40% of transaction volume across its platform, an increase from 34% in 2022. The company linked this trend to growing merchant interest in payment strategies built around portable, merchant-controlled credentials rather than reliance on a single processor.
The launch also comes as merchants and platforms consider how payment infrastructure will need to adapt to AI-driven purchasing, an area in which Spreedly said portable, merchant-controlled credentials could play a role in supporting transactions initiated by AI agents.
 News on Payments
Spreedly launches standalone payment vault for merchants
ID Finance launches Turrón BNPL card via Plazo
Remitly secures UAE Stored Value Facilities licence from Central Bank
Paymentology, T2P partner on card issuing in Thailand
Triple-A secures VARA in-principle approval in Dubai
 Explainers on Payments
Explainer: understanding cross-border FX mechanisms in card payments
Explainer: understanding 3DS authentication
Advocate General opinion on FX hedging by payment institutions under PSD2 and MiFID II
The merchant's guide to chargebacks: from reason codes to dispute strategy
Understanding the G20 cross-border payments targets
 The Paypers is a global hub for market insights, real-time news, expert interviews, and in-depth analyses and resources across payments, fintech, and the digital economy. We deliver reports, webinars, and commentary on key topics, including regulation, real-time payments, cross-border payments and ecommerce, digital identity, payment innovation and infrastructure, Open Banking, Embedded Finance, crypto, fraud and financial crime prevention, and more – all developed in collaboration with industry experts and leaders. 
Categories
 Payments 
 Fraud and Fincrime 
 Fintech 
 Crypto, Web3 and CBDC 
 Regulations 
 M&A and Investments 
Current themes
 A2A Payments 
 Payment Orchestration 
 TradFi and DeFi Convergence 
 KYC, KYB and Digital Identity 
 Scams and Fraud 
 Embedded Finance 
 Real-Time Payments 
The Paypers
 Team 
 Advertise 
 About 
Contact
The Paypers
Prinsengracht 777e 
1017 JZ Amsterdam
P: +31 20 658 0652
No part of this site can be reproduced without explicit permission of The Paypers (v2.7).
 Privacy Policy  / Cookie Statement 
Copyright

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Spreedly launches standalone payment vault for merchants
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On 16 Jul 2026 Spreedly (Durham, NC; payments infrastructure/orchestration, founded 2007) unbundled its **payment vault into a standalone product**, decoupled from its full orchestration platform. Feature set: PCI DSS Level 1 tokenisation, network tokenisation, Account Updater, stored-credential optimisation, and credential portability across "100+ payment providers." Merchants can start with vault-only, keep a single processor per region, then "graduate" into routing/orchestration later without re-vaulting.

De-PR'd read: **this is a packaging / go-to-market move, not new technology.** Spreedly has offered a vault since inception and shipped "Advanced Vault" (network tokens + Account Updater + lifecycle) back in **Jun 2023** — the same capability set is now sold as a discrete, lower-commitment SKU. No launch customers, no pricing, no SLA disclosed → "available" reads as GA-in-name, adoption unproven (analysis). The one hard number — **stored-credential transactions = 40% of platform volume, up from 34% in 2022** — is Spreedly's own unaudited platform metric measuring the *existing* base, not the new standalone product; it's directional support for the "vault-as-control-point" thesis, self-serving as adoption evidence.

**Why structured this way:** the standalone SKU lets Spreedly attack the pure-play merchant-vault buyer (Basis Theory / VGS turf) without an orchestration commitment, then funnel them upstack ("graduate into Spreedly orchestration without re-vaulting"). Portability is the pitch; the funnel design is a retention play → the second-order question is whether "portable across 100+ providers" is genuine mobility or lock-in with a wider door.

## [1] Competitors / peers
The "merchant-controlled portable vault" category is already contested:
- **Basis Theory** — purest developer-first PCI-L1 vault pure-play; raised **$33M Series B (Costanoa), Oct 2025**, explicitly for agentic commerce. **Independent, NOT acquired** (correcting a task premise that it was bought by Adyen — no supporting source; contradicted by the Oct 2025 raise).
- **VGS (Very Good Security)** — "leader in payment tokenisation," 5B+ tokens, composable vault + network tokens + Account Updater; more established pure-play with a dedicated agentic push (2025).
- **Gr4vy** — orchestration + standalone GCP vault; launched its standalone vault Jun 2023 (a day before Spreedly's Advanced Vault) and pushed a new 2026 vault alongside this Spreedly launch.
- **Adyen** — "Universal Token Vault," 7.6B+ active tokens (Oct 2025), agentic-framed — but processor-tied, the portability adversary.
- **Cybersource/Visa TMS, Stripe, Checkout.com, Recurly, Paddle** — vault-as-part-of-processor; **Stripe** is the key portability adversary (vault-migration friction is its moat).

Position: **fast-follower at parity, matching table stakes.** Spreedly's edge is not vault maturity (VGS/Basis Theory are ahead) but its ~$50B GMV orchestration install base and the upsell path. **Why the map looks this way:** merchant-controlled vaults commoditise the tokenisation layer; the durable value migrates up to routing/optimisation/fraud — which is exactly why every orchestrator (Spreedly, Gr4vy) now also sells a vault as the top-of-funnel wedge.

## [2] Company history / fit
Founded 2007 (Nathaniel Talbott); ~$50B+ GMV/yr, 100+ countries, 140+ gateway connections, customers incl. Priceline/Hopper/Lemonade. Last major raise: **$75M growth round from Spectrum Equity, Nov 2019** — **no fresh capital in ~6 years.** Recent moves: acquired **Dodgeball (fraud orchestration), Sep 2025** ([[Spreedly acquires Dodgeball for fraud orchestration]]); integrated Paysafe as acquirer, Feb 2026 ([[Paysafe announces partnership with Spreedly]]). CEO Justin Benson stable.

**Why the company acts this way:** an orchestrator's core take-rate is thin and commoditising; growth needs new monetisable entry points. Unbundling the vault (this launch) + adding fraud (Dodgeball) both widen the funnel and the wallet-share of existing infra — a monetisation/land-grab lever consistent with a firm that hasn't raised since 2019 (analysis).

## [3] Novelty / value-add / traction
Novelty **low-to-moderate**: the tech shipped in 2023; the new thing is the SKU and lower entry point. Traction **unproven** — zero named logos or pricing at launch. The substantive economic hook is real but not Spreedly-specific: **network tokens genuinely lift auth rates** (Visa cites ~4.6%, Mastercard ~2.1% uplift via pre-validation, per-txn cryptograms, auto credential refresh) and PCI-L1 tokenisation removes PAN from merchant systems. **Who captures the margin:** the vault layer is being commoditised by three-plus credible providers → the value-add sits in *portability that actually reduces switching costs across processors* and in the up-stack optimisation. If portability is real, merchants win negotiating leverage over processors; if it's a funnel, Spreedly wins retention. That tension, not the tokenisation itself, is where the weight lies.

## [4] What's next / market sentiment
Market backdrop is real: payment-orchestration TAM ~$3–4B in 2026, ~18–26% CAGR (soft, estimate-dependent). The **AI-agent-commerce angle in the announcement is aspirational** — Spreedly ships no agentic product/protocol here, only asserts that merchants controlling portable credentials "will be best positioned." The genuine wave is moving faster than the mention implies: Mastercard Agent Pay (first live agentic txn Sep 2025), Visa Intelligent Commerce / Trusted Agent Protocol (Oct 2025), Google AP2, PayPal x ChatGPT/Perplexity — see corpus [[Visa expands agentic commerce access for merchants in Europe]], [[Stripe unveils AI and commerce tools at Stripe Tour Berlin]]. **Why it may matter second-order:** if agent-initiated purchases scale, a merchant-owned, processor-portable credential store becomes strategically valuable (the agent needs a stable token independent of any one processor's roadmap). Watch: standalone-vault pricing, named logos, and actual AP2 / agent-token support. Competitors (Basis Theory, VGS) are ahead on the agentic narrative with fresh capital.

## Sources
- The Paypers (primary), 16 Jul 2026 — note body.
- ITDigest, 16 Jul 2026 (launch, Benson/Rivers quotes).
- PYMNTS 2023 (Advanced Vault); Digital Transactions (Gr4vy + Spreedly vaults).
- PR Newswire, 17 Sep 2025 (Dodgeball); Spreedly blog Nov 2019 ($75M Spectrum Equity).
- fintech.global, 15 Oct 2025 (Basis Theory $33M, independent).
- Solidgate / pci-proxy (network-token auth uplift); Mordor/Vantage (orchestration TAM).
- Digital Commerce 360, 16 Oct 2025 (Visa/Mastercard agentic).
- Internal: [[Spreedly acquires Dodgeball for fraud orchestration]], [[Paysafe announces partnership with Spreedly]], [[Visa expands agentic commerce access for merchants in Europe]], [[Stripe unveils AI and commerce tools at Stripe Tour Berlin]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Freshness: FRESH.** New product launch (standalone vault SKU, 16 Jul 2026) — distinct from the Sep 2025 Dodgeball M&A ([[Spreedly acquires Dodgeball for fraud orchestration]]) and Feb 2026 Paysafe partnership ([[Paysafe announces partnership with Spreedly]]). Not a reprint of a prior note. Weight is low, but it is a genuine new event.

**Importance: 2/5** — Incremental repackaging of an existing capability (Advanced Vault, Jun 2023) from a mid-size (~$50B GMV) orchestrator, no named customers, no pricing, agentic angle is aspirational. A legible signal of the "vault-as-control-point / unbundling" trend — digest one-liner, not a standalone story. Bumps to 3 only if launch logos or agentic-protocol support materialise.

## Red-team / challenge questions
1. **GA or PR?** Announced "available" 16 Jul 2026, but no customers/pricing/SLA → GA-in-name; adoption **open**.
2. **What's new vs Advanced Vault (Jun 2023)?** Technically little — it's a discrete SKU with a lower entry point. Packaging/GTM, confirmed.
3. **Was Basis Theory acquired by Adyen?** No — contradicted by BT's $33M independent Series B (Costanoa, Oct 2025). Task premise **wrong**.
4. **Portable credentials or lock-in in disguise?** Portability across 100+ providers is the pitch; "graduate into Spreedly orchestration without re-vaulting" is a retention funnel. Genuine cross-processor mobility **open**.
5. **Is the 40%-of-volume stat credible?** Spreedly's own unaudited platform metric (up from 34% in 2022); measures the existing base, not the new SKU. Directional, not verified.
6. **Does it actually cut merchant PCI scope?** Yes in principle (PCI-L1 tokenisation removes PAN) — but not unique to Spreedly; any third-party vault does this.
7. **How does it compare to VGS / Basis Theory on vault maturity?** VGS (5B+ tokens) and Basis Theory are more established pure-plays; Spreedly's edge is its orchestration install base, not vault depth.
8. **Is the network-token auth uplift real?** Yes — Visa ~4.6%, Mastercard ~2.1%, mechanism-backed. The substantive economic hook, but industry-wide.
9. **Is the agentic-commerce claim substantive?** No shipped agentic feature or protocol — positioning only. The broader wave (Mastercard/Visa/PayPal/AP2) is real and moving faster than the mention implies.
10. **Financial/strategic health?** No fresh capital since Nov 2019 ($75M Spectrum Equity); ~$50B GMV; Dodgeball buy Sep 2025. This unbundling looks like a monetisation/land lever. New funding status **open**.
11. **Who needs whom more — merchant or Spreedly?** Merchants gain processor leverage IF portability is real; Spreedly needs the top-of-funnel wedge to defend a commoditising take-rate. Balance hinges on real switching-cost reduction.
12. **What breaks the value-add?** Processors (Stripe, Adyen) keeping vault-migration friction high, or Visa/MC network-token services being consumed directly — disintermediating the independent vault layer.
13. **Second-order: why does a merchant-owned portable vault matter for AI agents?** An agent needs a stable credential independent of any single processor's roadmap; a portable vault could become the control point for agent-initiated purchases — if agent commerce scales (open).
14. **Is Gr4vy's simultaneous 2026 vault a coincidence?** No — every orchestrator is racing to sell the vault as a wedge, confirming this is a category move, not a one-off.
15. **Does this change the central question?** From "is Spreedly's vault new?" (no) to "will processor-portable credentials meaningfully lower merchant switching costs, and who captures the up-stack margin once the vault is commoditised?"
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Card vaulting / tokenization sits inside the payments-orchestration stack. No clean TAM figure is publicly verifiable → no data on market size; structurally it is a fragmented, fast-consolidating infra layer where value accrues to whoever holds the token (the "system of record" for card credentials). Two live drivers: (1) network tokenization measurably lifts auth rates — Visa reports ~4.6% CNP uplift, Mastercard ~2.1%, with ~26% fraud reduction (per VisaNet, via pci-proxy/juspay, as of 2026); (2) PCI-DSS scope reduction — routing raw PAN out of merchant systems drops a merchant from SAQ-D to SAQ-A and can cut PCI assessment cost ~40–60% (via pci-proxy, 2026). "Why now": credential portability is the wedge — Spreedly reports stored-credential transactions rose to 40% of platform volume from 34% in 2022, i.e. the vault is shifting from passive storage to an auth-rate/optionality lever (analysis).

**Competitive landscape.** Sector KPIs: GMV/TPV routed, tokens under management, auth-rate uplift, provider connections (portability breadth). Players & basis of competition:
- **Dedicated vault/tokenization:** VGS (Very Good Security) — self-described "world leader in payment tokenization", 4bn+ tokens, ~$104.9M raised, backers incl. a16z, GS Growth, Visa Ventures (via Crunchbase/press); Basis Theory — challenger competing on non-per-API-call pricing (via basistheory.com); TokenEx. Basis competition = pricing + composability + no processor lock-in.
- **Orchestration bundling a vault:** Primer (raised $100M Series C May 2026, $170M total; [[Primer raises $100 million Series C for payments orchestration]]), Gr4vy ([[Gr4vy and Worldline strengthen global payments partnership]], [[Airwallex and Gr4vy partner on enterprise payment optimization]]), Payrails, Yuno, IXOPAY.
- **Rails-level:** Visa/Mastercard network tokens + PSPs (Adyen, Stripe, Checkout.com) embedding their own vaults.
Protagonist's position: Spreedly is a scaled incumbent orchestrator — ~$60bn GMV/yr, 100+ countries, 100+ provider connections (via Spreedly/press). The standalone vault is a land-and-expand move: sell the credential store first, upsell orchestration later with "no re-vaulting". Moat = switching costs (once a merchant's tokens live in your vault, moving is painful) + breadth of provider integrations (analysis).

**Comps & multiples.** Spreedly is private; no valuation disclosed (last named round: $75M growth from Spectrum Equity, Nov 2019; total ~$82.8M — via Finovate/Crunchbase). No revenue disclosed → EV/Rev, P/S = no data; multiples not computable. Internal comps are venture rounds, not trading comps: Primer $100M Series C / $170M total ([[Primer raises $100 million Series C for payments orchestration]]); VGS ~$105M total raised (external). Distribution not computed — qualitative only: this is a private growth-infra set valued on GMV/TPV and token volume, not public EBITDA multiples. `[UNSOURCED]`: any Spreedly post-money, revenue, take rate.

**Risk flags.**
1. **Network-token disintermediation.** Visa/Mastercard push network tokens directly to merchants/PSPs; if the schemes and large PSPs make merchant-owned network tokens frictionless, the independent vault's value (auth uplift, portability) is captured at the rails layer — the vault risks becoming a thin, commoditized store.
2. **Commoditization + pricing pressure.** PCI-compliant tokenization is now table stakes offered by VGS, Basis Theory, every orchestrator and PSP; Basis Theory explicitly attacks on price. A decoupled vault sold standalone competes closer to a utility, compressing margin unless the orchestration upsell converts.
3. **Land-and-expand execution / switching-cost dependence.** The thesis rests on merchants adopting vault-only and later buying Spreedly orchestration; if they instead build their own routing on the portable credentials (which the product explicitly enables), Spreedly monetizes only the low-margin vault while handing away the stickier orchestration layer — the portability pitch cuts both ways.

**What this changes (idea-lens).** Unbundling the vault is a bet that "credential ownership" becomes the merchant's control point and the entry wedge for orchestration — a defensive land-grab against VGS/Basis Theory and against PSP lock-in, dressed as a pro-merchant portability story (analysis). Falsifiable: if stored-credential share keeps climbing and standalone-vault logos convert into orchestration seats, the wedge works; it breaks if scheme network tokens + PSP vaults commoditize the layer and standalone vault stays a stranded, low-margin SKU. Watch for named enterprise adoption and any disclosed vault→orchestration conversion. Note: prompt's "CVC-backed" ownership is unverified — disclosed lead investor is Spectrum Equity, not CVC Capital Partners `[UNSOURCED for CVC]`.

Sources: https://itdigest.com/fintech/spreedly-launches-standalone-payment-vault-as-merchants-move-to-control-their-own-payment-credentials/ · https://www.spreedly.com/blog/spreedly-receives-75-million-growth-investment-from-spectrum-equity · https://www.crunchbase.com/organization/spreedly · https://www.verygoodsecurity.com/press-releases/very-good-security-vgs-announces-usd35-million-series-b · https://go.basistheory.com/compare/very-good-security · https://www.pci-proxy.com/blog-posts/how-network-tokenization-helps-improve-payment-authorization-rates · https://juspay.io/blog/network-tokenization-vs-pci-tokenization-differences-architecture-and-which-one-lifts · https://www.payrails.com/blog/merchant-owned-payment-vault
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
