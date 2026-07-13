---
title: "Visa launches Payment Passkey in India with IDFC FIRST Bank"
date: 2026-07-07
retrieved: 2026-07-07
tags:
  - company/visa
  - company/idfc-first-bank
  - industry/payments
  - region/india
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/7ffd8727
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sb67ce6bf
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Visa launches Payment Passkey in India with IDFC FIRST Bank

> [!info] 2026-07-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇮🇳 Visa launches Payment Passkey in India with IDFC FIRST Bank. Visa has said the solution is expected to improve payment success rates while reducing the number of steps required to complete online transactions. Read more

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/7ffd8727>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Visa launches Payment Passkey in India with IDFC FIRST Bank
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
- On **2 July 2026** Visa announced its **Payment Passkey** went **live in India**, with **IDFC FIRST Bank as the first (and so far only) Visa issuer** to enable it for cardholders. The passkey lets a Visa cardholder authenticate an online card transaction with the phone's native unlock — fingerprint, face, PIN, password or pattern — instead of an SMS OTP. Biometric data is device-bound (FIDO2/WebAuthn), never shared with Visa/merchant.
- De-PR'd: the headline "Visa launches Payment Passkey in India" reads like a country-first debut. It is not. What is actually new is narrow: **the first Visa *issuer* going live**. Passkeys as a capability in India predate this by ~2 years and were pioneered by the **rival**: Mastercard **chose India for the *global* launch of its Payment Passkey Service in August 2024** (`[[Mastercard targets password-free APAC checkout by 2030]]` explicitly says "Building on Mastercard's global launch of its Payment Passkey Service in India"). By Feb 2026, Business Standard already reported **both Visa and Mastercard** rolling out passkeys for card transactions in India via processors like Razorpay (with a Razorpay–Mastercard live PoC dating to 2024). So Visa is **catching up on Mastercard's home turf**, dressed as a launch.
- What Visa actually assembled: a live issuer (IDFC FIRST) + a **broad merchant list** (Myntra, Paytm, MakeMyTrip, Tata Starbucks, Reliance Digital, EatSure/Rebel Foods) + a **fintech/gateway stack** (Juspay, Wibmo, Razorpay, PayU, Pine Labs, BillDesk, M2P, Paytm Payments Services). Note Wibmo is Visa-owned — so part of the "ecosystem" is Visa's own rails.
- Claimed benefit: "improve payment success rates and reduce steps." Trade press quantifies it as a **~2–3% transaction-success uplift** from removing SMS-OTP friction, plus lower social-engineering fraud — but this is a projected figure, not IDFC-measured live data. **No disclosed live volumes, active-passkey counts or actual conversion delta** at launch. → "Launched" is true at the issuer/merchant-enablement level; "adopted at scale" is not yet evidenced.
- **Why framed as a launch, not a catch-up:** Visa is behind Mastercard on the specific "passkey in India" story, so the PR anchors on the country + the merchant roster (impressive breadth) rather than on being second. → the real signal is not novelty but that a **regulatory deadline is forcing the whole card rail off SMS-OTP**, and both networks are racing to have issuers compliant.

## [1] Competitors / peers
- **Mastercard** — the reference point. Made **India the global launch market for Payment Passkey (Aug 2024)**; `[[Mastercard targets password-free APAC checkout by 2030]]` (Nov 2025) frames India as the proof point for extending passkeys to Singapore/Malaysia/Vietnam by 2027. First Mastercard *issuer* worldwide to go live was **xMoney (Portugal, Jun 2026)** — `[[xMoney becomes first Mastercard issuer to launch Payment Passkey]]` — so Visa's "first issuer" milestone (IDFC, India) roughly parallels Mastercard's issuer-activation phase in the same quarter. Networks are in lockstep, ~weeks apart.
- **Domestic India substitutes already live:** `[[Flipkart, Axis Bank, PayU launch biometric card authentication]]` (May 2026) shipped issuer-level face-ID authentication for Axis cardholders on Flipkart — same OTP-replacement job, without the "passkey/FIDO" branding. `[[Samsung Wallet to enable biometric UPI payments from December]]` and Aadhaar-based biometrics cover the UPI side. So Indian consumers can already do OTP-less biometric checkout on several rails; Visa's passkey is one more entrant, not a category creator.
- **Standards layer:** `[[Google and Mastercard back FIDO Alliance on agentic commerce standards]]` (May 2026) shows the same FIDO passkey plumbing is being positioned as the base layer for **agentic commerce** — the strategic prize behind the mundane OTP-replacement story.
- Position: **parity/catching-up**, not ahead. On its home network Visa is credible, but on the "India passkey" narrative specifically it is the follower.
- **Why the landscape is this way (2nd order):** the passkey race in India is **regulator-driven, not demand-driven** — whoever gets issuers compliant with RBI's dynamic-factor rule first captures merchant integrations and default status. Because the tech (FIDO2) is a shared standard, neither network has a durable moat from the passkey itself; the moat is **issuer relationships + merchant/gateway distribution**, which is why Visa's PR leads with the partner roster.

## [2] Company history / fit
- Fits Visa's global passkey push: Visa introduced its Payment Passkey Service at its Payments Forum, and has been rolling it out region by region (Noon Payments = first PSP globally in the Middle East; Thales as APAC VDRP partner). India is a logical, high-volume node.
- Consistent with Visa's broader India/biometric moves in the corpus: `[[Visa unveils Tap to Confirm ID technology with Fidelity Bank Bahamas]]` (biometric identity), `[[ICICI Bank and Visa launch India's first USD debit card from GIFT City]]` (India partnerships). Visa also owns **Wibmo** (an India-centric payment-security/token firm), which appears in this launch's stack — so Visa has in-country authentication infrastructure to leverage.
- **Why Visa acts now:** the forcing function is **RBI's "Authentication Mechanisms for Digital Payment Transactions Directions, 2025"** (issued 25 Sep 2025, compliance from 1 Apr 2026), which requires ≥2 factors with at least one **dynamic** and explicitly blesses biometrics/passkeys as alternatives to SMS-OTP. SMS-OTP alone is being phased out. → Visa isn't innovating into a vacuum; it's meeting a compliance deadline in a market where fraud is acute (`[[Indian bank fraud losses surge 46% to ₹48,021 crore in FY26]]`; RBI cites card-fraud spikes). The structural pressure: on a network where a rival owns the "we launched passkeys here first" story and a hard regulatory clock is ticking, Visa must show issuer traction fast or cede default-authentication share.

## [3] Novelty / value-add / traction
- **Novelty: low-to-moderate.** The passkey capability, FIDO2 mechanism, India market and even the "OTP-less" pitch are all pre-existing (Mastercard 2024; Razorpay PoCs 2024; Visa/MC dual rollout reported Feb 2026). The genuinely new datum is **narrow and incremental: IDFC FIRST is the first live Visa issuer, plus a named merchant/gateway roster**.
- **Value-add (real but bounded):** removing SMS-OTP is a real UX/fraud win — trade estimates cite up to ~50% lower auth abandonment and ~2.5× lower fraud vs OTP (FIDO Alliance figures, quoted in the xMoney case), and a **2–3% success-rate uplift** cited for India. In a market with India's OTP-fraud problem, that is material *if* adoption scales.
- **Traction: unproven at launch.** "First issuer live + select users of select merchants" = enablement, not volume. No cardholder counts, no measured conversion delta from IDFC, no share of IDFC's book enrolled. "Select users" is a soft phrase implying a limited cohort. → Treat as **piloted-at-scale-of-one-issuer**, not adopted.
- **Who captures the margin (2nd order):** the passkey is a **standardized, free-to-consumer authentication layer** — it earns Visa no direct fee. Its value to Visa is **defensive/volume**: higher approval rates = more transactions on Visa rails = more interchange/network-fee volume, and staying the default authenticator keeps Visa in the flow. The deeper prize is **agentic commerce**: whoever owns the trusted device-bound credential (passkey) owns the authentication step when AI agents pay — which is exactly why FIDO/Mastercard/Google are standardizing it (`[[Google and Mastercard back FIDO Alliance on agentic commerce standards]]`). → The central question shifts from "did Visa launch a passkey" (yes, incrementally) to **"who becomes the default authentication credential in India as SMS-OTP dies — and can that be parlayed into owning agent-initiated payment authorization."** On that question Visa is currently trailing Mastercard's head start.

## [4] What's next / market sentiment
- **Near term:** Visa says more banks will roll out passkeys "this year." Watch for (a) additional Visa issuers going live, (b) any **measured** success-rate/fraud numbers from IDFC (vs today's projected 2–3%), (c) expansion beyond "select users." RBI's dynamic-factor compliance (1 Apr 2026; cross-border CNP 2FA by 1 Oct 2026) guarantees continued issuer migration off SMS-OTP regardless of network marketing.
- **Sentiment:** positive but not differentiating — Indian press frames it as part of the broader "OTP-less era," with Visa and Mastercard treated as parallel movers. No new pricing/economics disclosed.
- **Risks:** device/UX fragmentation (older Android, shared devices), consumer trust/education, uneven merchant enablement, and that "select users" never broadens. Regulatory risk is low (this *is* the regulator's preferred direction).
- **Why the market goes this way (counterintuitive 2nd order):** because passkeys are a **shared FIDO standard**, the more both networks and processors (Razorpay, Juspay) push them, the more the authentication layer **commoditizes** — the winner is decided by distribution and default-issuer status, not the tech. And the same commoditized passkey layer becomes the **control point for agentic payments**, so a "boring" compliance rollout in India is quietly laying the rails for who authorizes AI-agent purchases later. The under-appreciated effect: India, a fraud-plagued OTP market, is functioning as the **global proving ground** for passkey-based checkout for *both* networks — a lead that Mastercard, not Visa, currently holds.

## Sources
- Note primary source: Connecting the Dots in Fintech (2026-07-07 digest) — https://www.connectingthedotsinfin.tech/r/7ffd8727
- Visa press release: https://www.visa.co.in/about-visa/newsroom/press-releases/visa-launches-payment-passkey-in-india-reducing-friction-in-digital-payments.html
- Business Standard, "Visa passkeys go live in India as IDFC First Bank becomes first issuer" (2026-07-03): https://www.business-standard.com/industry/banking/visa-payment-passkeys-india-idfc-first-bank-otp-less-authentication-126070300284_1.html
- BusinessToday, Visa passkey (2026-07-02): https://www.businesstoday.in/personal-finance/news/story/waiting-for-otp-to-make-a-card-payment-visa-will-now-allow-payment-authentication-via-passkey-540500-2026-07-02
- Biometric Update, "Visa expands payment passkeys, from issuer rollout to AI agent commerce" (2026-07): https://www.biometricupdate.com/202607/visa-expands-payment-passkeys-from-issuer-rollout-to-ai-agent-commerce
- Mastercard press, "India selected for global launch of Payment Passkey Service" (Aug 2024): https://www.mastercard.com/global/en/news-and-trends/press/2024/august/mastercard-selects-india-for-the-global-launch-of-its-payment-passkey-service-accelerating-secure-online-checkout-for-millions-of-shoppers.html
- Business Standard, "Going OTP-less: Mastercard, Visa rolling out passkeys" (2026-02-16): https://www.business-standard.com/finance/news/going-otp-less-mastercard-visa-rolling-out-passkeys-for-card-transactions-126021601202_1.html
- Razorpay blog on biometric passkey auth with Mastercard & Visa: https://razorpay.com/blog/razorpay-biometric-card-authentication-passkey-with-mastercard-visa/
- RBI Authentication Directions 2025 coverage (IBM / Business Standard): https://www.ibm.com/think/perspectives/strengthening-digital-payment-security-with-rbi-new-authentication-directions
- Internal: [[Mastercard targets password-free APAC checkout by 2030]], [[xMoney becomes first Mastercard issuer to launch Payment Passkey]], [[Google and Mastercard back FIDO Alliance on agentic commerce standards]], [[Flipkart, Axis Bank, PayU launch biometric card authentication]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is this actually a "launch" or a catch-up?** Catch-up. Mastercard made India the *global* launch market for Payment Passkey in **Aug 2024**; Visa+Mastercard passkey rollouts in India were reported Feb 2026. The new fact is only "first Visa **issuer** (IDFC) live." → *answered.*

2. **What's the FIRST Visa passkey activity in India?** Passkey/FIDO card-auth capability existed via processors (Razorpay–Mastercard PoC 2024; Visa/MC reported Feb 2026). IDFC = first live Visa *issuer*, Jul 2026. → *answered.*

3. **Launched or announced?** Launched at issuer/merchant-enablement level (IDFC live, named merchants/gateways). But only "select users" — no live volumes, enrolled-card counts, or measured conversion. → *live-but-unquantified.*

4. **Is the 2–3% success-rate uplift real or projected?** Projected/industry-cited, **not** an IDFC-measured live figure. FIDO's 50%-lower-abandonment / 2.5×-lower-fraud numbers are Mastercard/FIDO stats, not this deployment's. → *open (unproven for IDFC).*

5. **Who is silent about what?** Visa/IDFC disclose no adoption numbers, no share of IDFC's book, no exclusivity terms, no timeline for more issuers beyond "this year." "Select users" is doing a lot of work. → *gaps flagged.*

6. **Precise mechanism delta vs Mastercard's passkey?** Effectively none — both are FIDO2/WebAuthn device-bound passkeys replacing SMS-OTP. Delta is distribution (issuer/merchant roster), not tech. → *answered.*

7. **Is there a durable moat?** No — passkey is a shared standard; moat is issuer relationships + merchant/gateway distribution + default-authenticator status. → *answered (analysis).*

8. **What's the real driver — demand or regulation?** Regulation: RBI Authentication Directions 2025 (issued 25 Sep 2025, compliance 1 Apr 2026; cross-border CNP 2FA by 1 Oct 2026) phases out SMS-OTP-only. Both networks are racing to compliance. → *answered.*

9. **Does Visa own part of its own "ecosystem"?** Yes — **Wibmo** (in the partner stack) is Visa-owned, so the breadth of "partners" is partly Visa's own rails. → *answered.*

10. **Is India uniquely important here?** Yes — high OTP-fraud, huge CNP volume, and it's the **global proving ground** for passkey checkout for BOTH networks. But Mastercard, not Visa, holds the first-mover story here. → *answered.*

11. **Where's the second-order prize?** Agentic commerce — passkey = the trusted device-bound credential for AI-agent payment authorization (FIDO/Mastercard/Google standardizing it). Whoever is default authenticator now is positioned for agent-pay later. → *answered (strategic).*

12. **Does Visa monetize the passkey directly?** No direct fee. Value is defensive/volume (higher approval → more on-Visa transactions → interchange/network volume) + staying in the auth flow. → *answered.*

13. **Are there already OTP-less substitutes live in India?** Yes — Flipkart/Axis/PayU face-ID (May 2026), Samsung Wallet biometric UPI, Aadhaar biometrics. Consumers already have OTP-less options. → *answered.*

14. **Duplicate of an existing corpus note?** No note covers Visa+IDFC specifically. Closest analogs (Mastercard India passkey, xMoney first MC issuer, Flipkart/Axis biometric) are distinct events. → *fresh.*

15. **What would change the verdict / downside triggers?** If "select users" never scales, or if a later note shows this is a re-report of the Feb-2026 Visa/MC India passkey story, downgrade. Upside trigger: IDFC publishes measured live conversion/fraud gains, or multiple issuers go live fast. → *open.*

---

Importance: 3/5 — A real, verifiable NEW step (first live Visa issuer in India + concrete merchant/gateway roster) on a regulator-forced migration off SMS-OTP in a huge, fraud-heavy market, with a genuine second-order stake in agentic-commerce authentication. But it is incremental and a catch-up: Mastercard globally launched passkeys *in India* two years earlier, the tech is a shared FIDO standard with no Visa-specific moat, OTP-less substitutes already exist, and there is zero disclosed live-adoption data — only projected uplift. Not novelty, not proven traction; weight comes from market size + strategic optionality, capped at mid.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-07]] (2026-07-07).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Payments authentication / online card acceptance in India. Market frame: India credit-card market ~$20.1bn (2025) → ~$38.3bn by 2034, ~7.4% CAGR (per IMARC, via imarcgroup.com, as of 2026). Context, not TAM for this feature: UPI processed ~23.2bn txns worth ~₹29.9tn in May 2026 (per NPCI data cited via coinlaw.io) — i.e. cards compete for online checkout against a dominant, near-free real-time rail, which is the structural backdrop pressuring card networks to cut checkout friction. Why now: RBI's push for tokenization (per RBI, ~98% of e-commerce txns now token-based, via coingeek.com) plus a mandate (effective ~2026) requiring at least one dynamic/additional authentication factor for digital payments — passkeys (FIDO/biometric) satisfy this while replacing the SMS-OTP that causes drop-off. Visa frames the benefit as higher success rates + fewer steps (note); press cites a claimed +2–3% success-rate uplift from removing SMS friction (per Business Standard, as of 2026-07-03) — a vendor figure, treat as `(analysis)` not verified economics.

**Competitive landscape.** Sector KPIs: online payment success/authorization rate, checkout conversion, fraud/chargeback rate, processed-transaction volume. Basis of competition: distribution (which issuers/merchants go live) and standards ownership (FIDO passkey + 3DS + tokenization + Click to Pay), not price. Key players & recent moves:
- Mastercard launched its Payment Passkey Service in India in Aug 2024 and went "OTP-free" across APAC (per Mastercard/PRNewswire, biometricupdate.com Nov 2024) — a clear head start.
- Razorpay enabled biometric card authentication via passkeys with BOTH Mastercard and Visa in India (per razorpay.com) — the network is one input; the aggregator/PSP owns the merchant integration.
- Visa: first issuer live is IDFC FIRST Bank (2026-07-02), select users at Myntra, Paytm, MakeMyTrip, Tata Starbucks, Reliance Digital, EatSure; "more banks expected this year" (per Business Standard).
Protagonist position: **catching up / fast-follower** on the India passkey rollout — Mastercard was ~2 years earlier — but Visa runs the same play globally (see agentic-commerce passkey moves below). Moat = network/standards + issuer relationships (`(analysis)`; single-issuer launch is early traction, not scale).

**Comps & multiples.** Internal comps (in-base, same authentication/Click-to-Pay theme):
- [[Juspay joins Mastercard Engage network for Click to Pay]] — PSP-side Click to Pay, ~300m txns/day globally (2026-06).
- [[ZEN.COM and Mastercard introduce Click to Pay checkout]] — Mastercard checkout rollout (2026-06).
- [[Mastercard launches Agent Pay for Machines for machine-speed payments]] — adjacent auth/agentic direction (2026-06).
No round/valuation attaches to this pick (product launch, no deal), so no deal-multiple table. Public trading comps (network scale, not this feature): Visa FY-Q2'26 (ended 2026-03-31) net revenue $11.2bn (+17% YoY); payments volume $3.7tn (+9% cc); cross-border ex-Europe +11% cc; 66.1bn processed txns (+9%) (per Visa 8-K / earnings release, sec.gov 000140316126000077, 2026-04-29). EV/Revenue, EV/EBITDA, P/E → **no data** (no free clean EV/consensus source here; do not estimate). Read: this is a product/adoption story, not a re-rating event; multiples "not computed, qualitative only."

**Risk flags.**
1. **Fast-follower / not first** — Mastercard shipped India passkeys ~2 years earlier (Aug 2024) and Razorpay already spans both networks; second-mover means Visa competes on issuer/merchant execution, and the standard is commoditizing (both networks + PSPs converge on FIDO passkeys), so any conversion edge is likely temporary.
2. **Disintermediation by the domestic rail** — UPI dominates Indian retail digital payments and card-linked UPI blurs the card use case; friction-reduction on cards defends share but doesn't reverse the mix shift; second-order: card-network India volume growth stays capped regardless of passkey UX.
3. **Adoption/economics unverified** — one issuer live, "select users," and the +2–3% success-rate uplift is a vendor claim; note is silent on fraud-liability shift, merchant fees and rollout timeline — "announced," not yet "adopted at scale."

**What this changes (idea-lens).** `(analysis)` Passkey/OTP-free auth is becoming table stakes in India, not a differentiator — the RBI dynamic-auth mandate turns it into a compliance floor both networks must meet. Watch: pace of additional issuers going live (Visa said "more this year") and whether success-rate/conversion gains show up in merchant data. Falsifiable thesis: if Visa passkeys stay stuck at one issuer / "select users" into H2-2026 while Mastercard + PSPs (Razorpay/Juspay) scale, this is a defensive catch-up, not a share gain — the trigger to disprove it is a multi-issuer, full-rollout announcement with disclosed conversion uplift.

Sources: https://www.business-standard.com/industry/banking/visa-payment-passkeys-india-idfc-first-bank-otp-less-authentication-126070300284_1.html · https://razorpay.com/blog/razorpay-biometric-card-authentication-passkey-with-mastercard-visa/ · https://www.biometricupdate.com/202411/mastercard-replacement-of-otps-with-passkeys-and-click-to-pay-reaches-apac · https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000077/q22026earningsrelease.htm · https://www.imarcgroup.com/insight/india-credit-card-market-analysis-forecast · https://coinlaw.io/upi-statistics/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings layer — context, not in the news. The passkey/IDFC item is a product announcement (`type/product`, no financials). Below: Visa's latest reported quarter as material backdrop. Primary source = Visa's own fiscal Q2 2026 release (quarter ended March 31, 2026; Visa FY ends September), reported April 28, 2026.

**Verdict (headline read).** BEAT · net revenue $11.2B (+17% YoY; +16% constant-dollar) vs public consensus ~$10.75B (beat ~+$0.45B / ~+4%) · non-GAAP EPS $3.31 (+20% YoY) vs consensus ~$3.10 (beat ~+$0.21) · GAAP EPS $3.14 (+36% YoY) · drivers: resilient consumer spend + value-added services + lower litigation provision · capital: new $20.0B buyback authorized. This is broad-based strength — revenue growth was the highest since 2022.

**Key figures (with growth).**
- Net revenue: **$11.2B, +17% YoY** (+16% constant-dollar).
- GAAP net income: **$6.0B, +32% YoY**; GAAP diluted EPS **$3.14, +36% YoY** (~35% constant-dollar). Note: GAAP EPS growth outran revenue mostly on a smaller litigation special item YoY ($311M this year vs $992M prior).
- Non-GAAP net income: **$6.3B, +17% YoY**; non-GAAP diluted EPS **$3.31, +20% YoY** (~20% constant-dollar). Non-GAAP EPS > net income growth reflects buyback (share count 1.92B; ~25M class A repurchased in-quarter).
- GAAP operating expense: $4.0B, **-4% YoY** (litigation provision down); ex-items non-GAAP opex **+17% YoY** (personnel + marketing) — real cost growth is running hot, masked at the GAAP line.
- GAAP effective tax rate 16.1%; cash & investments $14.2B.

**By segment / driver.**
- Data processing revenue **$5.5B, +18% YoY** — fastest revenue line.
- Service revenue **$5.0B, +13% YoY** (recognized on prior-quarter payments volume).
- International transaction revenue **$3.6B, +10% YoY** (cross-border driven).
- Other revenue **$1.3B, +41% YoY** — small base, includes value-added services momentum (VAS revenue +27% YoY constant-dollar to ~$3.3B per management).
- Client incentives **$4.2B, +14% YoY** (contra-revenue; growing broadly in line with volume).

**Key business drivers (constant-dollar YoY).**
- Payments volume **+9%** (quarter ended Mar 31, 2026; +8% for the Dec-quarter that feeds service revenue).
- Total cross-border volume **+12%**; excluding intra-Europe **+11%**.
- Processed transactions **+9%** to **66.1B**.
Read-through to the passkey story: cross-border and processed-transaction growth stayed strong; Visa's e-commerce authentication push (Payment Passkey in India w/ IDFC FIRST) is a lever on the "improve success rates / reduce fraud friction" side of that processed-transaction / cross-border franchise, not yet a reported revenue line.

**vs expectations / prior period.**
- Public consensus (per StockTitan / IndexBox / Investing.com coverage, as of the Apr 28, 2026 print): revenue ~$10.75B, adj. EPS ~$3.10. Reported $11.2B / $3.31 → **beat on both** (~+$0.45B revenue, ~+$0.21 EPS). [Consensus figures are public aggregators, not FactSet/Street — labeled as such.]
- YoY momentum: +17% revenue is an acceleration vs Visa's mid-teens run-rate and the strongest since 2022 (per CEO). No prior Visa earnings note exists in the corpus to wikilink against.

**Guidance / forward.** Full-year FY2026 outlook figures were not disclosed in the press release (given on the earnings call; magnitude [UNSOURCED] here). Management tone confident: CEO McInerney framed continued "resilient" consumer spending and positioned Visa as "the leading hyperscaler of payments," explicitly citing agentic and stablecoin capabilities in the "Visa as a Service" stack. New $20.0B multi-year buyback + $0.670/sh dividend signal balance-sheet confidence. What management did NOT foreground in the release: the +17% non-GAAP opex growth (personnel/marketing) and the ongoing MDL interchange litigation ($311M provision this quarter, $125M escrow deposit) — the de-PR read is that GAAP EPS +36% flatters underlying operating trends that are closer to the +20% non-GAAP EPS.

**Thesis-flags.**
1. **Growth acceleration is real and broad** (revenue +17%, cross-border +12%, VAS +27% cd). Fact → why: volume + data-processing + VAS all firing → why it matters: supports the pricing-power / network-scale thesis → second-order: funds the aggressive product roadmap (passkeys, agentic, stablecoin) that defends the network against account-to-account / stablecoin disintermediation.
2. **Opex running +17% (non-GAAP)** vs revenue +17% — operating leverage is flat this quarter as Visa invests. Watch whether marketing/personnel spend converts to VAS/new-flows revenue or compresses margin if volume growth normalizes.
3. **Capital return at record pace** ($9.2B returned; $7.9B buyback, largest ever; new $20B authorization) — a lever that props EPS growth above net-income growth; a tailwind but also a signal management sees limited larger M&A (Prisma/Newpay in Argentina are bolt-ons).
4. **Litigation overhang persists** (MDL interchange provision + escrow) — recurring GAAP noise; not a numbers surprise but keeps GAAP vs non-GAAP divergence structural.

Sources: Visa fiscal Q2 2026 earnings release (primary), https://www.sec.gov/Archives/edgar/data/1403161/000140316126000077/v-20260428.htm · Visa IR PDF, https://s1.q4cdn.com/050606653/files/doc_financials/2026/q2/Q2-2026-Earnings-Release_vF.pdf · public consensus via StockTitan/IndexBox/Investing.com (as of 2026-04-28) · FY2026 full-year guidance magnitude [UNSOURCED] (call only). No prior Visa earnings note in the base to wikilink.
<!-- /enrichment:earnings_review -->
