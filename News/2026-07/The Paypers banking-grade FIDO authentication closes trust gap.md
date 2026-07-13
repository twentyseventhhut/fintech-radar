---
title: "The Paypers: banking-grade FIDO authentication closes trust gap"
date: 2026-07-06
retrieved: 2026-07-06
tags:
  - industry/regtech
  - industry/fraud-risk
  - region/global
  - type/commentary
sources:
  - https://newsletter.thepaypers.com/i/2uv6ff3m2HbW1CQ6dVEvHg3052KXRGGOd7drmtBO74Ap18UeyjOU5763rvVwBt-93zRijJ2YDHVnxaU-R1iSalUULEj2Lcgz-QZjk8r0ns8kmdS7p9txjr-krfszykzOSsNCQgtmrd_L1euEOKgbVb1gEGVvxSzT7Dfl4taAEKWOO4LfGQMbso_2tMAVqqt-6fqPt-lqMJk
status: enriched
n_mentions: 1
channels:
  - "The Paypers"
story_id: sf821952d
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# The Paypers: banking-grade FIDO authentication closes trust gap

> [!info] 2026-07-06 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: The Paypers

## Агрегированный текст (из дайджестов)

[The Paypers] The Rise of Banking-Grade FIDO Authentication: Closing the Trust Gap

## Первоисточники

### newsletter.thepaypers.com
<https://newsletter.thepaypers.com/i/2uv6ff3m2HbW1CQ6dVEvHg3052KXRGGOd7drmtBO74Ap18UeyjOU5763rvVwBt-93zRijJ2YDHVnxaU-R1iSalUULEj2Lcgz-QZjk8r0ns8kmdS7p9txjr-krfszykzOSsNCQgtmrd_L1euEOKgbVb1gEGVvxSzT7Dfl4taAEKWOO4LfGQMbso_2tMAVqqt-6fqPt-lqMJk>
*348 слов · direct*

The Rise of Banking-Grade FIDO Authentication: Closing the Trust Gap
Takes place on 14 Jul 2026 07:00 AM PDT / 10:00 AM EDT / 04:00 PM CET
Daniela Ceobanu
01 Jul 2026 / 5 Min Read
Strong authentication is no longer enough. Financial institutions are under pressure to reduce friction and improve customer experience, combat increasingly sophisticated fraud, and move away from vulnerable SMS OTPs. Yet authentication success doesn’t always mean legitimate activity. FIDO passkeys are transforming authentication, but banks, issuers and payment processors need more than strong authentication alone. Join us to explore how leading financial institutions are building banking-grade FIDO authentication by combining passkeys with fraud intelligence, behavioral biometrics, device intelligence and adaptive risk assessment.
 
Agenda
The benefits of FIDO passkeys for banks, issuers, and payment processors
Why authentication success does not necessarily mean legitimate activity
The limitations of FIDO authentication alone in financial services
The additional measures that transform FIDO authentication into banking grade fraud protection
How banking-grade FIDO supports regulatory requirements, including PSD3
Presenters
Gagan Bhatia
Chief Information Security Officer (CISO) at Outseer
Dr. Ruth Wandhöfer [Moderator]
Experienced Chair, Author, Speaker, Adviser, Visiting Prof. Bayes Business School. Blackwired Cybersecurity
Susann Gäbler
Head of Risk Steering Fraud at Santander Deutschland
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
## [0] What exactly happened (de-PR'd)
Not an event, a deal, or a stat — this is a **webinar promo** from The Paypers (registration piece by Daniela Ceobanu, 01 Jul 2026; event 14 Jul 2026) fronted by **Outseer** (CISO Gagan Bhatia) and **Santander Deutschland** (Susann Gäbler, Head of Risk Steering Fraud), moderated by Dr. Ruth Wandhöfer. Treat it as **marketing, not adoption evidence**.

The de-PR'd argument (which is technically sound): (a) FIDO passkeys are now mainstream and defeat *credential phishing and adversary-in-the-middle (AiTM)* because the private key is domain-bound; (b) BUT "authentication success ≠ legitimate activity" — passkeys answer "who is this?", not "is this transaction safe?"; (c) therefore banks must bolt fraud intelligence + behavioral biometrics + device intelligence + adaptive risk onto passkeys = "**banking-grade FIDO**".

**Why framed this way / what it reveals:** "banking-grade FIDO" is **not a standard or certification** — it is **Outseer's coinage** (see Outseer blog, 2026-06-10, "FIDO passkeys & 3DS authentication for issuers"). The rhetorical move — "passkeys alone aren't enough" — is exactly the argument that preserves the revenue of the *risk/fraud layer Outseer sells* on top of the (open, commoditizing) FIDO2 primitive. The real driver named in the agenda is regulatory (PSD3), not a product breakthrough. So the honest read: value is migrating **from the auth primitive to the fraud-orchestration layer**, and this piece is a vendor staking a claim to that layer.

## [1] Competitors / peers
Two layers compete, and "banking-grade FIDO" is the pitch to sell the *combination*:
- **FIDO/credential layer** (commoditizing, open FIDO2/WebAuthn): Nok Nok Labs (FIDO server), Daon, Transmit Security, Ping Identity, Entrust, HID, Thales/OneSpan.
- **Risk / behavioral / device layer** (where the margin sits): **Outseer** (RSA spinout; EMV 3-D Secure ACS + all-cause fraud scoring), **BioCatch** (behavioral intent; $35M Series E, Sept 2025), **Feedzai** & **Featurespace** (now Visa-owned), **Callsign**, **Incognia** (device/location; cf. [[Webull Brazil hits 92.5% frictionless onboarding with Incognia]], which surfaced RAT/ATO risk — the same "legit-user-coerced" gap this webinar leans on).

Recent dated moves in-corpus: [[Ping Identity to acquire Keyless for biometric authentication]] (Nov 2025) — a credential-layer player buying privacy-preserving biometrics; and behavioral/device-intelligence fraud detection recurring across fraud-risk notes.

**Why the landscape is this way (2nd order):** the FIDO primitive is a free, open cryptographic standard → it cannot carry a durable multiple. So every vendor here has a **structural incentive** to argue "passkeys alone are insufficient" (analysis) — because the defensible, data-network-moated revenue is in the risk layer, not the auth primitive. The competitive question is not "who has passkeys" (everyone will) but "who owns the cross-bank fraud-signal graph."

## [2] Company history / fit
Outseer = the former RSA Anti-Fraud/Adaptive Authentication business, spun out under the Outseer brand; its heritage is issuer-side EMV 3-D Secure and risk scoring, not passwordless login. Fronting a "banking-grade FIDO" webinar is a logical **repositioning**: as passkeys eat the authentication step Outseer never owned, it reframes itself as the *fraud-intelligence layer that makes passkeys safe for money movement*. Santander Deutschland's presence is credibility signalling (a real issuer risk lead); note Germany's BSI issued **draft passkey-server guidelines TR-03188 v0.9 (2025-09-30)**, a regulatory tailwind in Santander DE's home market. **[SOFT]** No first-party Santander DE passkey adoption %/dates were verifiable — treat any on-air specifics as unconfirmed.

**Why the company acts this way:** commodity auth primitive → Outseer needs a software/data multiple → hence it must anchor to the risk-and-liability layer that regulation (PSR) is actively expanding.

## [3] Novelty / value-add / traction
**Novelty: low.** "Layer risk analysis on top of authentication" is old (RSA Adaptive Auth predates FIDO by a decade; TRA exemptions under PSD2 already reward real-time risk scoring). The genuinely current fact is that **passkeys are now at banking scale** — FIDO Alliance World Passkey Day (2026-05-06): ~5bn passkeys in use (a *modeled estimate*), 75% of consumers have enabled ≥1, 49% use regularly; **but no banking/payments-specific figure**. Named live bank rollouts (Chase, U.S. Bank, CBA, CIBC, Chinabank PH) are overwhelmingly **login, not transaction authorization**; EU retail-banking passkey use for *payment signing* is still thin.

**Why the value-add is real but the branding is inflated (deeper):** the technical premise holds — the fraud category that is *growing* is **authorized push payment (APP) / social-engineering scams**, where the *legitimate user authenticates under deception*, so passkeys pass every check. UK APP losses £450.7M in 2024; **H1 2025 £257.5M = 41% of all UK fraud losses** (UK Finance). Passkeys structurally cannot stop this. BUT: the honest industry response to APP has been **liability shifts + Verification of Payee**, not "better authentication." So "banking-grade FIDO" is less a product category than **repackaging the existing risk stack as a compliance necessity**. The margin-capture question: whoever owns the cross-bank behavioral/device **signal graph** wins; the passkey itself captures nothing.

## [4] What's next / market sentiment
**Regulatory backdrop is the real story:** PSD3/PSR reached provisional political agreement (2025-11-27); OJ publication expected ~Q2 2026, then ~18-month application → first hard deadlines ~early 2028. Crucially PSR **expands SCA triggers** (tokenization, limit/contact-detail changes) and **shifts liability for spoofing/impersonation scams onto PSPs** — i.e. regulation forces banks to detect fraud *beyond* successful auth (Norton Rose Fulbright; Flagright). Verification of Payee already mandatory for euro-area PSPs since 2025-10-09. SMS-OTP deprecation is broad (NIST de-recommended; UAE mandated removal by Mar 2026). eIDAS 2.0 EUDI wallets due in all 27 member states by Dec 2026 (specs still incomplete — slippage risk).

**Sentiment / risks (2nd order):** (1) account **recovery/fallback is the real weak link** — phishing-resistance is only as strong as the SMS/password reset path behind it; a documented Mar 2026 case took 3 weeks of manual proofing after device loss. (2) **Synced vs device-bound** passkeys trade device-binding for cloud-breach exposure — a genuine assurance bind for banking. (3) FIDO's own 2026 survey: 57% of orgs still rely on phishable primary auth — intent outruns adoption. Counterintuitive takeaway: the winning move for banks is **not** stronger authentication (they'll all have passkeys) but owning the risk/liability layer — which is precisely why vendors are racing to define "banking-grade" on their own terms.

**Freshness:** FRESH — thematic commentary; no prior corpus note covers "banking-grade FIDO / passkeys + layered fraud." Adjacent but distinct: [[Ping Identity to acquire Keyless for biometric authentication]], [[Webull Brazil hits 92.5% frictionless onboarding with Incognia]].

## Sources
- The Paypers webinar promo (01 Jul 2026), primary text in note above.
- FIDO Alliance, World Passkey Day 2026 (2026-05-06): fidoalliance.org
- UK Finance Annual Fraud Report 2025 / H1 2025: ukfinance.org.uk
- Outseer blog, "FIDO passkeys & 3DS for issuers" (2026-06-10): outseer.com
- Norton Rose Fulbright / Arthur Cox — PSD3/PSR status 2026; BSI TR-03188 v0.9 (2025-09-30).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Top challenge / red-team questions (second-order)**

1. Is "banking-grade FIDO" an industry standard or a certification? — **No.** It is Outseer's coinage (Outseer blog, 2026-06-10); the webinar title reuses the vendor's own framing. Treat as marketing scaffolding around a valid technical point.

2. Does the piece report any actual adoption, deal, or metric? — **No.** It is a webinar registration promo (event 14 Jul 2026). Zero traction data; the "leading financial institutions are building..." claim is unquantified.

3. Do passkeys actually stop the fraud that is growing? — **No.** APP / social-engineering scams have the *legitimate user authenticate under deception* — passkeys pass every check. UK APP H1 2025 = £257.5M, 41% of all UK fraud losses (UK Finance). This is the honest core of the "trust gap."

4. What do passkeys genuinely defend against? — Credential phishing and adversary-in-the-middle (domain-bound private key). Real, but a *different* threat from scams.

5. Is layering risk analysis on authentication actually new? — **No.** RSA Adaptive Auth (Outseer's own lineage) predates FIDO; PSD2 TRA exemptions already reward real-time risk scoring. Novelty is low; the new fact is passkeys reaching banking scale.

6. Are the banking passkey rollouts login or transaction authorization? — **Overwhelmingly login** (Chase, U.S. Bank, CBA, CIBC). Payment-signing passkeys (ABANCA, Chinabank PH, SBI Sumishin) are rarer; EU retail payment-auth adoption is thin. Open for Santander DE specifically.

7. Is Santander Deutschland's passkey adoption verifiable? — **[SOFT / open]** Third-party trackers show WebAuthn support; no first-party Santander DE press release with dates/adoption % surfaced. Do not cite specifics as fact.

8. Who captures the margin in the stack? — Not the passkey (open, free FIDO2 standard). The **cross-bank behavioral/device fraud-signal graph** does. That reframes the central question from "who has passkeys" to "who owns the risk-signal network."

9. What is the real driver — innovation or regulation? — **Regulation.** PSR expands SCA triggers and shifts spoofing/impersonation-scam liability onto PSPs; PSD3/PSR OJ ~Q2 2026, deadlines ~2028. "Add fraud intelligence" is a compliance necessity, not a feature.

10. What is the strongest counter-argument to the whole thesis? — Regulators are answering the growing (APP) fraud category with **liability shifts + Verification of Payee** (mandatory euro-area since 2025-10-09), *not* with better authentication. So "banking-grade FIDO" partly rebrands the existing risk stack.

11. What is the unglamorous weak link the webinar likely underplays? — **Account recovery / fallback.** Phishing-resistance is only as strong as the SMS/password reset path; documented Mar 2026 case: 3 weeks of manual proofing after device loss.

12. Synced vs device-bound passkeys — security tension? — Yes. Synced (iCloud/Google) trade device-binding for cloud-breach exposure; device-bound is stronger but has no automatic recovery. A genuine assurance bind for banking-grade use.

13. Do the vendors have a conflict of interest in this framing? — **Yes (analysis).** Every player (Outseer, BioCatch, Feedzai, Featurespace, Callsign) profits from "passkeys alone are insufficient" because it preserves the risk-layer revenue. Skeptical weight warranted.

14. How reliable is the headline "5bn passkeys" figure? — **[SOFT]** It is a FIDO Alliance *modeled estimate* (public + internal deployment data), not a count. Use with a caveat.

15. Does anything genuinely new happen here that a reader must know? — Marginally: confirmation that passkeys are at banking scale AND that the industry is openly conceding auth ≠ fraud prevention just as PSR codifies scam liability. The *convergence* is the only fresh signal; the "banking-grade FIDO" label is not.

**Importance: 2/5** — A vendor webinar promo, not an event: no deal, no metric, no verifiable adoption. The underlying theme (auth ≠ legitimacy; value migrating to the fraud/risk layer under PSD3/PSR) is real and worth one honest paragraph, which lifts it above a 1, but the piece itself is marketing with low novelty and no traction.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: digital identity / authentication (passwordless, phishing-resistant), sitting between fraud/regtech and payments. This note is not a deal or a metric — it is a webinar promo from The Paypers (14 Jul 2026) with Outseer (CISO Gagan Bhatia) and Santander Deutschland (Head of Risk Steering Fraud); treat the thesis as marketing, not adoption evidence. Market size (sourced, wide dispersion across vendors): passwordless-authentication market ~$22–24bn in 2025 (per Mordor $24.1bn; Coherent MI $22.1bn; Research and Markets $23.6bn, via their 2025/26 reports) growing ~15.7–18.2% CAGR to ~$45–62bn by 2029–2032. Adoption (per FIDO Alliance State of Passkeys 2026, via BusinessWire 06 May 2026): ~5bn passkeys in use; 75% of people have enabled a passkey on ≥1 account, 49% use regularly; 68% of orgs deploying for workforce. Structure: fragmented — platform suites (Microsoft, Okta/Auth0, Ping Identity) bundle SSO+governance+passkey orchestration vs specialists (HYPR, Yubico, 1Kosmos, Transmit Security, Nok Nok) and payment-fraud stacks (Outseer, formerly RSA Adaptive Auth). Why now: (1) regulation — PSD3/PSR (likely in force ~Feb–Apr 2026 per OneSpan) tightens SCA + shifts fraud liability, and SMS-OTP is being deprecated as vulnerable; (2) the note's own de-PR'd point — "authentication success ≠ legitimate activity," i.e. FIDO alone doesn't stop scams/APP fraud/account-takeover, so banks bolt on fraud intelligence + behavioral biometrics + device signals + adaptive risk. Second-order effect: value migrates from the raw auth primitive (commoditizing, cryptographic, open FIDO2 standard) toward the risk/fraud-orchestration layer on top — which is exactly the layer Outseer sells.

**Competitive landscape.** Sector KPIs: for SaaS identity — ARR/subscription revenue growth, NRR, EV/Rev; for the auth primitive itself — auth success rate (~98% for passkeys vs lower for passwords, per HID/Descope 2026), enrollment/opt-in rate (40–45% within months). Key players & basis of competition: incumbents Okta (workforce + Auth0 CIAM), Microsoft, Ping Identity compete on platform breadth + distribution; specialists (HYPR, Yubico, 1Kosmos, Transmit Security) on high-assurance / hardware / dev experience; Outseer competes on payments-native fraud intelligence + EMV 3-D Secure. Recent moves: Ping Identity to acquire Keyless for biometric auth (Nov 2025, in-base); Mastercard targeting password-free APAC checkout by 2030 (Nov 2025); Google+Mastercard backing FIDO Alliance on agentic-commerce standards (May 2026); Okta FY2026 (ended Jan 2026) revenue $2.919bn +12% YoY. Protagonist (Outseer) position: niche — a fraud/risk-intelligence layer, NOT a passkey issuer; positioning "FIDO + fraud intelligence = banking-grade" is a value-migration play `(analysis)`. Moat: switching costs + proprietary cross-bank fraud data network (intangibles), not the FIDO standard itself (open, commoditizing). CAC/LTV/NRR for Outseer — not disclosed `[UNSOURCED]`.

**Comps & multiples.** Only one pure-play public comp is verifiable; Outseer and most specialists are private → no market cap.
| Company | Metric | Multiple (arithmetic) |
|---|---|---|
| Okta (public) | mkt cap ~$24bn, EV ~$19bn, FY26 rev $2.919bn | EV/Rev = $19bn / $2.919bn ≈ 6.5x (companiesmarketcap/gurufocus cite ~6.1x); EV/EBITDA ~22.6x |
| Outseer (private) | — | no data (last round not verifiable) |
| Transmit Security / HYPR / Nok Nok (private) | — | no data |
Internal comps: [[Ping Identity to acquire Keyless for biometric authentication]] · [[Mastercard targets password-free APAC checkout by 2030]] · [[Google and Mastercard back FIDO Alliance on agentic commerce standards]]. Read: Okta ~6.1x EV/Rev on +12% growth is in-line-to-modest for identity SaaS — a rule-of-40-ish name, not richly valued; below the ~0.5–20x sanity band's upper half. Distribution not computed (only 1 comparable figure) — qualitative comparison only.

**Risk flags.** (1) Commoditization of the primitive — FIDO2/passkeys are an open standard pushed by platform owners (Apple/Google/Microsoft) and the FIDO Alliance; the auth step itself trends to zero margin, so specialists must defend the fraud/risk layer or get disintermediated. (2) Disintermediation by rails owners — Mastercard/Visa/Google embedding passkeys + agentic-commerce standards (May 2026) could absorb the "banking-grade" bundle into scheme/platform rails, squeezing standalone fraud vendors. (3) Regulatory double-edge — PSD3/PSR is a tailwind for demand but shifts fraud liability onto PSPs/banks and could mandate baseline controls that erode premium pricing for add-on fraud intelligence.

**What this changes (idea-lens).** Signal, not event: the "FIDO alone isn't enough" framing marks the sector re-centering from authentication to continuous risk/fraud orchestration — a consolidation/attach vector where fraud-intelligence vendors (Outseer, Transmit) get pulled into passkey deployments `(analysis)`. Falsifiable thesis: if passkey enrollment scales but scam/APP-fraud losses keep rising, banks buy the add-on layer and specialists re-rate up; trigger to watch — PSD3/PSR final text on SCA + liability, and whether schemes (Mastercard/Visa) bundle fraud intelligence natively (which would break the thesis by disintermediating specialists).

Sources: https://www.mordorintelligence.com/industry-reports/passwordless-authentication-market · https://www.coherentmi.com/industry-reports/passwordless-authentication-market · https://www.businesswire.com/news/home/20260506926067/en/FIDO-Alliance-Reports-Accelerating-Global-Passkey-Adoption-on-World-Passkey-Day-2026 · https://blog.hidglobal.com/iam-authentication-2026-5-key-predictions-enterprises · https://investor.okta.com/news-and-events/news-releases/news-details/2025/Okta-Announces-Fourth-Quarter-And-Fiscal-Year-2025-Financial-Results/default.aspx · https://companiesmarketcap.com/okta/marketcap/ · https://www.gurufocus.com/term/enterprise-value-to-revenue/OKTA · https://www.outseer.com/ · https://www.onespan.com/blog/psd3-psr-updates-2025
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
