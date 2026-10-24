---
title: "Incognia examines Apple's new fraud-prevention features"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/incognia
  - company/apple
  - industry/fraud-risk
  - region/us
  - type/commentary
sources:
  - https://www.incognia.com/blog/apples-new-trust-signals-and-their-role-in-fraud-prevention
  - https://www.incognia.com
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sdef88942
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Incognia examines Apple's new fraud-prevention features

> [!info] 2026-10-23 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Incognia examines Apple’s new fraud-prevention features.Incognia’s Gabriel Falcone, Co-Founder and Head of Software Engineering, explains how Apple’s new trust signals can help flag scams but cannot confirm whether a transaction or identity is legitimate. He highlights why combining them with device, location and transaction data remains important for fraud prevention.

## Первоисточники

### incognia.com
<https://www.incognia.com/blog/apples-new-trust-signals-and-their-role-in-fraud-prevention>
*723 слов · direct*

Apple’s New Trust Signals and Their Role in Fraud Prevention 
Subscribe to Incognia’s content

 Apple’s new security capabilities can help detect when a customer is being manipulated by a scammer or verify what an iPhone camera originally captured. 
 However, neither capability can independently determine whether a payment is legitimate, an identity document belongs to the person submitting it, or a device has been compromised. 
 iOS already provides several layers of security, including application sandboxing and restrictions on access to sensitive capabilities. 
 Apple's new fraud-prevention and image-authenticity features build on these protections, giving applications additional information to assess risk. 
 Understanding what these capabilities can establish, and where their limitations lie, is important when incorporating them into a broader fraud-prevention strategy. 
What Apple is adding
 Impersonation Risk Detection helps applications assess whether a user may be involved in an active social-engineering scam. 
 Starting with iOS and iPadOS 27, an application can request an assessment and receive an Unknown, Medium, or High risk level, provided the user has enabled sharing. 
 This addresses a scenario in which a legitimate customer successfully authenticates while being manipulated into authorizing a payment. The application can use the assessment to introduce a delay, display a warning, or request additional verification. 
 Apple also makes an important distinction: Unknown means that no evidence of suspicious activity was detected, not that the action was confirmed as safe. 
 Apple Reference Image provides a way to verify what an iPhone camera originally captured and identify subsequent modifications to a photograph. 
 On iPhone 18 Pro models, taking a photo in Reference mode captures signed sensor data that is used to create an unalterable reference image. Users can compare that reference with the main image to identify changes. 
 For identity verification, this helps establish the authenticity of an image but does not establish the identity of the person submitting it. 
 An authentic photograph of a genuine identity document, for example, could still be submitted by someone other than its owner. Image authenticity therefore complements identity verification, liveness detection, and an assessment of the device and session involved. 
Experience with existing protections
 Mobile platforms have long provided native security mechanisms designed to protect devices, applications, and sensitive information. 
 When attackers need capabilities restricted by the operating system, they often need to bypass native security protections. We have observed this pattern across different types of device manipulation. 
 Jailbreaks are a good example. 
 iOS restricts applications and users from accessing capabilities beyond those permitted by the operating system. Jailbreak techniques typically exploit vulnerabilities or weaknesses to bypass these restrictions. As platforms introduce stronger protections, attackers can adapt their techniques to circumvent them. 
 Apple itself notes that App Attest cannot definitively identify a device with a compromised operating system. A successful application integrity check therefore does not necessarily establish the integrity of the device or the legitimacy of the activity taking place on it. 
 This is where Incognia complements the native security model, using additional device and environment signals to identify situations in which platform protections may have been bypassed. 
What the new signals leave unresolved
 The practical question is which fraud scenarios Apple's new signals can address, and where complementary detections remain necessary. 
 Their actual contribution will need to be measured in real-world deployments, considering both their effectiveness and coverage. 
 Incognia already incorporates evidence from native platform protections into its fraud decisions and monitors fraud attempts that succeed despite those mechanisms. 
 While this experience does not establish how Apple's newer capabilities will perform, it demonstrates why platform protections should be considered alongside other sources of evidence. 
 Device and location intelligence, session information, account history, transaction context, and connections to previous abuse can provide additional context around what the platform reports. 
 Together, these signals help fraud teams identify risks that fall outside the scope or visibility of individual platform protections. 
Combining platform and application-level defenses
 Responding quickly to emerging attacks is also essential to fraud prevention. 
 Operating-system protections evolve according to platform-wide priorities and release schedules, while a new fraud technique can begin affecting a specific business immediately. 
 In practice, application-level detections often need to be updated before a platform-level mitigation is available. 
 Incognia can adapt its detections as new bypasses and attack patterns emerge, while continuing to incorporate the platform's protections. 
 Apple's new capabilities become additional inputs in this process, complementing the signals Incognia already uses to detect fraud. 
Gabriel Falcone

### Прочие ссылки (без извлечённого текста)

- <https://www.incognia.com>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Incognia examines Apple's new fraud-prevention features
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
This is a **vendor blog / thought-leadership post**, not an event. Incognia's Gabriel Falcone (Co-Founder, Head of Software Engineering) analyzes two newly-shipped Apple capabilities and argues they are complements to — not replacements for — Incognia's own device/location signals:
- **Impersonation Risk Detection** (a.k.a. the "Trust Insights" framework, shown at WWDC 2026): shipped in **iOS 27 / iPadOS 27 (Sept 2026)**. An on-device, opt-in signal. A supported app can request an assessment at a sensitive action (payment, security-setting change) and receives one of three tiers — **Unknown / Medium / High**. It targets the exact gap device-auth can't close: a *legitimate, correctly-authenticated* user being social-engineered into authorizing a payment. Off by default; the user must enable "Share with App Developers" in Settings → Privacy & Security. Apple explicitly cautions that **Unknown ≠ safe** ("no evidence detected," not "confirmed legitimate"). (source: 9to5Mac, Engadget, Apple Support)
- **Apple Reference Image**: **iPhone 18 Pro / 18 Pro Max only** (announced Sept 2026). The Main-camera sensor cryptographically signs pixel data at capture; Private Cloud Compute develops it into an "unalterable reference image" (a "digital negative") so later edits can be detected. Still photos only, main camera only — telephoto/ultrawide and video are **not** covered. (source: MacRumors, AppleInsider, Help Net Security)

**Why framed this way (the real tell):** Incognia is NOT reporting news — it is **defensive content marketing**. Two Apple-native signals land squarely on territory Incognia sells (device integrity + identity/liveness), so the post pre-empts the "do I still need a third-party vendor?" question. Its thesis — "Apple's signals establish *capability*, not *legitimacy*; Reference Image proves the image is authentic but not that the submitter owns the ID; App Attest (Apple's own admission) can't prove a device is uncompromised" — is accurate, but it is self-serving. The genuine analytical point: Apple ships on **platform-wide schedules**, whereas a new fraud technique hits one business immediately, so app-layer detections must patch faster than OS mitigations. That is a real, durable argument, independent of Incognia.

## [1] Competitors / peers
Every device-intelligence / behavioral-biometrics vendor faces the same "Apple is eating my lower layer" question:
- **Sardine** — device intelligence + behavioral biometrics, money-movement/ACH/scam focus.
- **Sift**, **BioCatch** (DeviceIQ, Mar 2026), **Feedzai**, **Fingerprint**, **Approov/Guardsquare** (who have long published on App Attest/DeviceCheck's limits — 2-bit storage, no jailbreak detection, no user identity).
- Incognia's own differentiator = **apartment-level location + Physical Social Graph** behavioral history, which Apple's signals do not provide.

**Why the landscape is this way (2nd order):** Apple's move actually *validates* the behavioral-scam-detection category and raises the floor for everyone — but it also **commoditizes the on-device risk tier**. The vendors most exposed are the ones whose moat WAS device/app integrity (classic fingerprinting); the ones better insulated sit on signals Apple structurally can't see (cross-app location history, cross-device graphs, server-side account/transaction context). Incognia is arguing it is in the second camp — see [[TWIF Device fingerprinting alone insufficient against fraud]] (its standing thesis) and [[Incognia launches Real-Time Scam Prevention for banks]] (its 2026-10-21 scam-prevention product launch that this blog implicitly cross-sells).

## [2] Company history / fit
Incognia (Brazil-rooted, device + location fraud intelligence; ~$46.5M raised, $31M Series B led by Bessemer, Jan 2024; claims ~1B devices protected). 2026 cadence has been heavy on AI-fraud content + launches: AI Rule Builder, Browser ID, Verified IP Location, AI Agent Detection, MCP Server, and Real-Time Scam Prevention (2026-10-21). This blog fits the pattern exactly: react to a macro platform shift (Apple iOS 27) with a "we complement it" narrative days after launching a directly-adjacent scam product. See [[Incognia's Andre Ferraz on the AI-enabled fraud landscape]] and [[Incognia launches Real-Time Scam Prevention for banks]].

**Why it acts this way:** its product line is a commodity-risk-signal business that needs to defend a software/platform premium; when the OS vendor ships an overlapping signal for free, the rational play is to reframe the native feature as an *input* to its platform, not a substitute. The blog does exactly that ("Apple's new capabilities become additional inputs").

## [3] Novelty / value-add / traction
**Novelty of the NEWS: low.** No product, no numbers, no customers, no deal — it is commentary on someone else's launch. The *underlying Apple features* are genuinely new (Sept 2026); Incognia's take is not.
**Value-add of the post: moderate-but-honest.** The strongest, non-PR point — Apple itself concedes App Attest can't confirm a device is uncompromised, and Unknown ≠ safe — is a correct caution against over-trusting the native signal. **Traction: none cited** (no clients using Apple's signal + Incognia, no measured lift). Falcone explicitly says the real-world contribution "will need to be measured in real-world deployments" — i.e. nothing is proven yet.

**Why the value is real or not (2nd order):** The margin question for Incognia isn't "is Apple a threat?" but **"who captures the fraud-decision layer?"** Apple owns the device and can give the Unknown/Medium/High tier for free to every app; that pushes value capture *up* to whoever combines it with cross-app/location/account context into a decision. If banks find Apple's tier "good enough" for scam nudges, Incognia's upsell shrinks; if fraud keeps slipping past OS-schedule patches (Incognia's bet), the orchestration layer keeps the margin. The blog is Incognia staking the claim to that orchestration layer.

## [4] What's next / market sentiment
Expect every device-intel vendor to publish similar "we complement Apple" positioning; expect iOS 27's Impersonation Risk Detection adoption to be gated by (a) opt-in friction (off by default) and (b) the short, undisclosed list of supported apps. Reference Image's reach is capped by iPhone 18 Pro hardware. Regulatory tailwind for scam/APP-fraud liability (UK, Brazil Pix) keeps demand for *any* scam-detection signal high.

**Why the market goes this way (counterintuitive 2nd order):** Apple commoditizing the base signal is usually read as bad for vendors, but it can *expand* the market — it legitimizes behavioral-scam detection with every bank's risk team, and the on-device tier is deliberately coarse (3 buckets, no explanation), so it *creates* demand for a richer layer on top rather than removing it. Net: tailwind for orchestration/context vendors, headwind for pure device-fingerprint commodities.

## Sources
- Incognia blog (primary): https://www.incognia.com/blog/apples-new-trust-signals-and-their-role-in-fraud-prevention
- Apple Support — Impersonation Risk Detection: https://support.apple.com/guide/iphone/use-impersonation-risk-detection-je2kvy9nls19/ios
- 9to5Mac (iOS 27 scam feature): https://9to5mac.com/2026/10/20/ios-27-adds-scam-prevention-feature-to-iphone-heres-how-to-enable-it/
- 9to5Mac Security Bite (developer API detail): https://9to5mac.com/2026/09/21/security-bite-ios-27-now-lets-apps-ask-your-iphone-if-youre-being-scammed/
- Engadget (Impersonation Risk Detection): https://www.engadget.com/2271157/apple-iphone-ipad-impersonator-risk-detection-new-security-feature/
- MacRumors (Apple Reference Image): https://www.macrumors.com/2026/09/09/apple-reference-image/
- AppleInsider (Apple Reference Image): https://appleinsider.com/articles/26/09/09/apple-reference-image-is-a-new-way-to-authenticate-iphone-photography
- Approov (App Attest / DeviceCheck limits): https://approov.io/blog/limitations-of-apple-devicecheck-and-apple-app-attest
- Incognia Series B: https://www.incognia.com/newsroom/incognia-secures-31mm-series-b-funding-for-proactive-approach-to-fraud-prevention
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is this a news event at all?** No — it is a vendor thought-leadership blog commenting on Apple's Sept 2026 iOS 27 / iPhone 18 Pro features. No product, deal, round, or number. (answered)
2. **Is it genuinely fresh vs prior Apple notes?** Yes. Prior published Apple items are Apple Pay *launches/fees* (Uzbekistan, UK tap-to-pay, India/Axis, $1B fraud-cut) — different events. No prior note covers iOS 27 Impersonation Risk Detection or Apple Reference Image, and none carries Incognia's commentary. **Fresh.** (answered)
3. **Is there a true twin among Incognia's own notes?** No. [[Incognia launches Real-Time Scam Prevention for banks]] (2026-10-21) is a product launch, not Apple commentary; [[TWIF Device fingerprinting alone insufficient against fraud]] is a general thesis. This is a distinct artifact, though low-value. (answered)
4. **What is Apple's feature actually called / what's the API?** "Impersonation Risk Detection," built on the WWDC-shown "Trust Insights" framework; on-device, returns Unknown/Medium/High. (answered)
5. **Is Reference Image broadly available?** No — **iPhone 18 Pro / 18 Pro Max only, main camera only, still photos only.** Narrow reach limits its fraud-fighting footprint near-term. (answered)
6. **Does Incognia show any traction linking its product to Apple's signal?** No — zero clients, zero measured lift; Falcone concedes real-world contribution "will need to be measured." (answered)
7. **Is the "Unknown ≠ safe" caution legitimate or FUD?** Legitimate — it mirrors Apple's own documentation; not fabricated. (answered)
8. **Does Apple commoditize Incognia's core signal?** Partly — it commoditizes the on-device *risk tier*; it does NOT provide cross-app location history / Physical Social Graph, Incognia's actual moat. Net exposure is on classic device-fingerprint commodities, less on context/orchestration. (analysis)
9. **Who captures the fraud-decision margin after this?** Shifts toward whoever fuses Apple's coarse tier with account/transaction/location context into a decision; Apple keeps the device layer, banks decide the consequence. (analysis)
10. **Is the opt-in design a real adoption cap?** Yes — off by default + undisclosed supported-app list means low initial coverage, so apps can't rely on it alone soon. (answered)
11. **Could Apple extend this to Apple Pay directly and disintermediate vendors?** Open — no evidence Apple plans to turn the tier into a payment-authorization gate; currently it only hands apps a score. (open)
12. **Does this help or hurt the device-intel category commercially?** Likely helps near-term (validates behavioral-scam detection with bank risk teams; coarse signal invites a richer layer on top) — counterintuitive but plausible. (hypothesis)
13. **Any conflict of interest in the analysis?** Yes — it is Incognia arguing you still need Incognia; accurate but self-interested. Weight accordingly. (answered)
14. **Does it name specific competitors or benchmarks?** No — no comparison to Sardine/Sift/BioCatch, no metrics; purely conceptual. (answered)
15. **What would raise importance?** A bank case study showing measured lift from Apple-tier + Incognia, or Apple extending the tier into payment auth. Neither present. (open)

**Importance: 2/5** — fresh but low-weight: an opinion blog, not an event; no product/numbers/customers/traction. The one durable insight (OS-schedule patches lag per-business attacks; Apple's own App Attest caveat) is real but modest, and the framing is self-promotional. Tracks a genuinely new Apple shift, which keeps it above a 1.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Device-fraud / behavioral-biometrics / mobile anti-fraud sits inside a fast-growing market: behavioral biometrics is put at ~$3.45–3.85bn in 2026 growing ~24–27% CAGR toward ~$11–16bn by 2031–2033 (per Mordor Intelligence / The Business Research Company / Coherent Market Insights, via secondary citations, as of 2026 — figures vary by definition, so treat as order-of-magnitude, not a single verified TAM). The adjacent fraud-detection-and-prevention-in-BFSI market is sized ~$11.6bn for 2026 (per Grand View / Precedence, as of 2026). Structure: fragmented, with value split across (a) platform-native OS controls (Apple, Google), (b) risk-signal vendors (device/location/behavioral), and (c) orchestration/decisioning layers at the bank/merchant. Barriers are data network effects (devices/abuse graphs seen) and integration switching costs, not capital. Why now: iOS 27 / iPadOS 27 ships Impersonation Risk Detection (on-device Unknown/Medium/High scam signals, off by default, requires app opt-in and developer support) and Apple Reference Image (signed sensor data on iPhone 18 Pro) — announced Sep 2026 (per Help Net Security / Engadget, 2026-09). This is the trigger for the note: a platform owner moving into the fraud-signal layer where third-party vendors operate.

**Competitive landscape.** Sector KPIs: devices/accounts protected, detection precision/recall and false-positive (friction) rate, annualized payment volume protected, net revenue retention. Key players: platform-native (Apple, Google); device/location/behavioral specialists (Incognia, BioCatch, Prove, NuData); decisioning/RiskOps (Feedzai, Sift, Forter, Featurespace, FICO). Basis of competition: breadth/quality of signal, false-positive economics, and speed of adapting to new attack patterns — not price. Recent moves: Visa agreed to acquire BioCatch for ~$2.4bn (Aug 2026, per secondary citations); Feedzai raised $75m at a ~$2bn valuation and won the ECB digital-euro fraud role (Oct 2025, per Fintech Global / SiliconANGLE). Incognia's position: a device+location-intelligence specialist (device fingerprinting + exact-location + tamper detection as "Incognia ID"), ~1bn devices protected, used by gig/delivery/ride-hailing/fintech; last round $31m Series B led by Bessemer in 2024, total ~$46.5m raised, founded 2014 by Andre Ferraz (per PitchBook / PYMNTS / Crunchbase). It is a well-funded niche leader, not a scaled incumbent — ahead on device+location signal depth, behind the RiskOps platforms on balance-sheet and breadth. Moat: the cross-device/location abuse graph (data network effects) and the ability to recognize a device post factory-reset `(analysis)`.

**Comps & multiples.** Internal comps from the base: [[Apple Pay cuts $1 billion fraud, expands to 89 markets]] (platform-native fraud scale), [[Resistant AI raises $25M Series B against financial crime]], [[Experian acquires KYC360 to boost fraud and financial crime solutions in the UK]], [[Thredd launches fraud solution with Featurespace]], and the Incognia family [[Incognia launches Real-Time Scam Prevention for banks]] / [[Incognia behavioral biometrics strengthen web risk decisions]] / [[Incognia the state of mule account handovers in 2026]]. External valuation markers: Feedzai ~$2bn post-money on $75m Series E (Oct 2025); BioCatch ~$2.4bn acquisition price by Visa (Aug 2026); Incognia ~$46.5m total raised, Series B 2024 (no disclosed post-money). Trading multiples (EV/Revenue, EV/EBITDA): no data — Incognia, Feedzai and BioCatch are private and do not disclose revenue, so numerator/denominator are both unavailable `[UNSOURCED]`; distribution not computed, qualitative comparison only. Note the scale gap: Incognia's ~$46.5m lifetime raise vs Feedzai's ~$2bn valuation and BioCatch's ~$2.4bn exit — Incognia competes on signal quality, not balance sheet. IR grounding (Apple, EDGAR): Apple's latest filing is the 10-Q for the quarter ended 2026-03-28 (filed 2026-05-01) — https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm ; relevant only as context — Apple Pay/Services scale is what gives Apple's new on-device fraud signals distribution, but no specific fraud-prevention revenue line is broken out, so no quarterly number is forced here.

**Risk flags.**
1. Platform disintermediation. Apple moving fraud signals on-device (Impersonation Risk Detection) partially overlaps the "is this user being socially engineered?" question vendors sell — if Apple/Google widen native coverage, the third-party signal layer can get commoditized at the edges. Second-order: pricing pressure on device-level signals, pushing vendors toward decisioning/orchestration where they still add value.
2. Dependence on someone else's rails. Incognia's value partly rests on reading around platform protections (jailbreak/tamper detection); each OS hardening cycle both helps (fewer bypasses) and threatens (less residual signal to sell), and Apple's opt-in/off-by-default design means real-world coverage is uncertain and outside Incognia's control.
3. Scale/funding asymmetry. At ~$46.5m raised vs $2bn-class peers, Incognia is under-capitalized relative to Feedzai/BioCatch (now Visa-backed); a distribution-rich acquirer bundling fraud signals (cf. Visa–BioCatch) could out-distribute a standalone specialist. Second-order: consolidation/acquisition pressure on sub-scale independents.

**What this changes (idea-lens).** Apple entering the fraud-signal layer reframes the vendor pitch from "we detect scams" to "we detect what the platform can't, and we adapt faster than OS release cycles" — exactly the positioning in Incognia's post `(analysis)`. Falsifiable thesis: native OS signals stay complementary (Unknown ≠ safe; off-by-default; no device-compromise guarantee per App Attest), so vendors keep the decisioning/liability layer. Watch: adoption rate of iOS 27 Impersonation Risk Detection by banks/apps, and whether Visa (post-BioCatch) or Apple starts bundling fraud signals into rails — either would compress the standalone device-signal niche. Thesis breaks if a platform owner ships a turnkey, default-on fraud API that banks accept as sufficient.

Sources: https://www.incognia.com/blog/apples-new-trust-signals-and-their-role-in-fraud-prevention · https://www.helpnetsecurity.com/2026/09/24/apple-ios-27-impersonation-risk-detection/ · https://www.engadget.com/2271157/apple-iphone-ipad-impersonator-risk-detection-new-security-feature/ · https://www.mordorintelligence.com/industry-reports/behavioral-biometrics-market · https://www.grandviewresearch.com/industry-analysis/fraud-detection-prevention-bfsi-market-report · https://fintech.global/2025/10/03/ai-fraud-platform-feedzai-hits-2bn-valuation/ · https://pitchbook.com/profiles/company/152413-12 · https://www.pymnts.com/authentication/biometrics/2024/biometrics-startup-incognia-raises-31-million-for-anti-fraud-tools/ · https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news.** This story is Incognia's commentary on Apple's new iOS 27 fraud-prevention features (Impersonation Risk Detection, Apple Reference Image) — Apple's quarterly financials are not the subject, so there is no beat/miss to review here.

Relevant scale context (why Apple's fraud-prevention reach matters): Apple's latest reported period is FY2026 Q2 (quarter ended Mar 28, 2026), reported 2026-04-30 — total revenue $111.2bn (+17% YoY), diluted EPS $2.01 (+22% YoY). Services set an all-time record at $31.0bn (+16% YoY), and the installed base exceeded 2.5bn active devices with transacting and paid accounts at all-time highs. That installed base is the distribution channel through which Apple's new OS-level trust signals (and Apple Pay / Tap to Pay) reach end users — i.e. the reason Incognia frames these signals as a material new input to complement rather than replace device/location/transaction intelligence. Apple does not break out Apple Pay revenue separately (it sits within Services).

Sources: https://www.apple.com/newsroom/2026/04/apple-reports-second-quarter-results/ · https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000011/a8-kex991q2202603282026.htm (FY2026 Q2 8-K, filed 2026-04-30) · https://www.macrumors.com/2026/04/30/apple-2q-2026-earnings/
<!-- /enrichment:earnings_review -->
