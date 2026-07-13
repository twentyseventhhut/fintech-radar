---
title: "Apple Hide My Email bug exposes real email addresses, researcher claims"
date: 2026-07-01
retrieved: 2026-07-02
tags:
  - company/apple
  - industry/fraud-risk
  - region/us
  - type/outage-security
sources:
  - https://link.techcrunch.com/click/46393856.45418/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA3LzAxL2FwcGxlcy1oaWRlLW15LWVtYWlsLWZlYXR1cmUtaGFzLWEtYnVnLXRoYXRzLWJlZW4tZXhwb3NpbmctcmVhbC1lbWFpbC1hZGRyZXNzZXMtcmVzZWFyY2hlci1jbGFpbXM_dXRtX2NhbXBhaWduPWRhaWx5X3Bt/6a347703be04c47cab07526aB3c65fe9c
status: enriched
n_mentions: 1
channels:
  - "TechCrunch"
story_id: s247b8e3e
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Apple Hide My Email bug exposes real email addresses, researcher claims

> [!info] 2026-07-01 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: TechCrunch

## Агрегированный текст (из дайджестов)

[TechCrunch] Apple's Hide My Email feature has a bug that's been exposing real email addresses, researcher claims: Research appears to reveal a bug that could render the feature effectively useless. Read More

## Первоисточники

### link.techcrunch.com
<https://link.techcrunch.com/click/46393856.45418/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA3LzAxL2FwcGxlcy1oaWRlLW15LWVtYWlsLWZlYXR1cmUtaGFzLWEtYnVnLXRoYXRzLWJlZW4tZXhwb3NpbmctcmVhbC1lbWFpbC1hZGRyZXNzZXMtcmVzZWFyY2hlci1jbGFpbXM_dXRtX2NhbXBhaWduPWRhaWx5X3Bt/6a347703be04c47cab07526aB3c65fe9c>
*567 слов · direct*

Apple’s Hide My Email feature has a bug that’s been exposing real email addresses, researcher claims
Apple’s Hide My Email feature is a convenient privacy tool that uses disposable addresses to hide a user’s true email for the sake of online anonymity. Unfortunately, new research appears to show that a bug in the feature allows users’ real email addresses to be unmasked.
The bug was reported by 404 Media , which says that it has tested and verified that the vulnerability exists. Tyler Murphy, the researcher who found the bug, said that he warned Apple about the problem over a year ago and that it was unclear why the company had yet to remedy the problem. All of the attempts to exploit the bug have been successful, Murphy added.
“We don’t know the full scope of the issue, but in our limited tests with volunteers, 100% of Hide My Email addresses were exploitable,” Murphy told the outlet. Details of the vulnerability haven’t been publicly disclosed, for fear that it will be exploited. 
Murphy is the co-founder of EasyOptOuts, which offers a paid data-removal service that takes your information off of data broker sites. He told 404 Media that “publicly accessible people-search sites make it easy to link an email address to other personal details, so people relying on Hide My Email for safety may be at risk.”
TechCrunch reached out to Apple for more information and will update this story if it responds. 
When it comes to the tech world, privacy tools are hard to come by and, unfortunately, even when they do exist, they don’t always work. Apple has been accused of this sort of thing before. 
Case in point: The company was sued in 2022 after it was reported that iPhone apps continued to send analytics data to Apple even when the iPhone Analytics privacy setting was turned on.
Similarly, in 2023, researchers found another one of Apple’s privacy features to be  effectively “useless.” The research claimed that a tool that was supposed to anonymize mobile users’ Wi-Fi connections by providing randomized MAC addresses (an easily trackable identifier) was simply exposing the user’s real MAC address.
Apple has built a large part of its reputation and branding on user privacy, so hopefully it manages to address the apparent Hide My Email bug with some expedience. If it can learn to better stand behind its privacy promises, that wouldn’t be the worst thing in the world either. 

Topics
 When you purchase through links in our articles, we may earn a small commission . This doesn’t affect our editorial independence. 

 Senior Writer, TechCrunch 
 
 Last chance to save up to $190 on TechCrunch Founder Summit. Join 1,000+ founders and VCs at all stages for real-world scaling insights and connections that move the needle. Savings end June 26, 11:59 p.m. PT .
Most Popular

 
 
 
 
 Flipper Device’s new Busy Bar is a customizable display for productivity 
 
 
 
 Ivan Mehta 

 
 
 
 
 Ford rehires ‘gray beard’ engineers after AI falls short 
 
 
 
 Anthony Ha 

 
 
 
 
 Govee’s smart nugget ice maker makes every iced drink feel like a luxury 
 
 
 
 Aisha Malik 

 
 
 
 
 Instagram is testing more ways to customize ‘Your Algorithm’ 
 
 
 
 Anthony Ha 

 
 
 
 
 Asian AI startups launch Mythos-like models as Anthropic’s export ban drags on 
 
 
 
 Kate Park 

 
 
 
 
 FTC gives Musk the OK to acquire SpaceX alumni startup Mesh 
 
 
 
 Marina Temkin 

 
 
 
 
 Corgi, the buzzy Y Combinator-backed insurance tech startup, says it didn’t steal an open source product 
 
 
 
 Julie Bort

## Контекст

<!-- enrichment:context -->
**What happened.** On 2026-07-01, 404 Media (reporter Joseph Cox) and TechCrunch reported that Apple's **Hide My Email** — the iCloud+ feature that issues disposable `@icloud.com` aliases to mask a user's real address — contains a bug that lets an attacker de-anonymize an alias and recover the real forwarding inbox behind it. Researcher **Tyler Murphy**, co-founder of data-removal service **EasyOptOuts**, found the flaw and says he disclosed it to Apple in **June 2025** with reproduction steps. In limited tests with volunteers, **100% of Hide My Email aliases were exploitable**; Murphy demonstrated it by unmasking a freshly generated alias belonging to the 404 Media reporter within minutes. Technical specifics are being withheld because the flaw remains live.

**Timeline (dated).**
- Jun 2025 — Murphy/EasyOptOuts responsibly discloses to Apple with repro instructions.
- Mar 2026 — Apple tells Murphy it "addressed the reported issue in a recent system change"; Murphy verifies it is NOT fixed.
- May 2026 — Apple says the issue is still under investigation, asks for continued non-disclosure; later says a fix is "expected in the coming weeks."
- 2026-07-01 — 404 Media publishes, having independently reproduced the bug; TechCrunch/MacRumors/9to5Mac amplify.
- Announced remediation — Apple plans to migrate future aliases from `@icloud.com` to `@private.icloud.com` plus other changes, expected later in summer 2026.

**Why it matters (fintech/risk angle).** Hide My Email is a signup/anti-spam privacy tool used across account creation, marketing, and third-party services. Murphy's point: publicly accessible people-search / data-broker sites make it trivial to pivot from an email to a full identity profile, so users relying on the alias for safety (e.g., domestic-abuse, activism, KYC-sensitive contexts) are exposed. The reputational hit is amplified because Apple markets privacy as a core brand differentiator and has twice claimed a fix that did not hold.

**Pattern of prior Apple privacy criticism (context).**
- 2022–2023: ~12 class-action suits alleged iPhone apps kept sending analytics (tied to DSID → iCloud identity) even with "iPhone Analytics" off (Mysk research). Apple largely defeated the California claims (ruling reported Jan 2026).
- 2023: researchers found Apple's Wi‑Fi **MAC-address randomization** effectively "useless," leaking the real MAC.
- Jan 2026: Apple began distributing payments in the **Siri privacy settlement** [[Apple begins distributing Siri privacy settlement payments]] (no admission of guilt).

**Internal cross-references (prior notes in vault).**
- [[Apple begins distributing Siri privacy settlement payments]] — most relevant prior privacy-reputation incident (2026-01).
- [[Apple introduces Digital ID in Apple Wallet]] — Apple's privacy-branded identity push, the reputation this bug undercuts (2025-11).
- [[Apple Pay GBP1.5bn class action launched in UK over fees]] — parallel example of Apple facing consumer/legal pressure over platform conduct (2026-01).

**Freshness / duplicate verdict:** **FRESH.** Semantic search (company=apple, k=8) surfaced only tangential Apple items — Siri settlement, Apple Pay/Visa, Digital ID, NFC/antitrust, RICO suit — none covering Hide My Email or this vulnerability. No duplicate note exists.

*Sources:* [TechCrunch](https://techcrunch.com/2026/07/01/apples-hide-my-email-feature-has-a-bug-thats-been-exposing-real-email-addresses-researcher-claims/), [MacRumors](https://www.macrumors.com/2026/07/01/hide-my-email-vulnerability-exposes-real-addresses/), [9to5Mac](https://9to5mac.com/2026/07/01/apple-hide-my-email-bug-seemingly-allows-100-of-real-email-addresses-to-be-discovered/), [Cult of Mac](https://www.cultofmac.com/news/apple-icloud-hide-my-email-exploit), [EasyOptOuts guide](https://easyoptouts.com/guides/apple-hide-my-email-is-leaking-email-addresses), [Gizmodo (analytics suits)](https://gizmodo.com/apple-iphone-privacy-analytics-12-lawsuits-statement-1850077715).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. **Single-source origin?** The core claim traces to one researcher (Tyler Murphy) with a commercial interest (EasyOptOuts sells data removal). 404 Media independently reproduced it — but has anyone outside those two parties verified the mechanism?
2. **"100% exploitable" — on what N?** The figure comes from "limited tests with volunteers." How many aliases? Self-selected? Not a statistical population claim.
3. **What is the actual mechanism?** Technical details are withheld. Is this a true cryptographic/leakage flaw, a metadata side-channel, or a correlation attack via people-search sites (which would shift blame partly off Apple)?
4. **Does the attack need prior knowledge?** Can an attacker unmask a *random* alias cold, or only when they already interact with the target (e.g., receive mail from the alias)? That distinction changes severity by orders of magnitude.
5. **Scope of exposure.** How many of the ~hundreds of millions of iCloud+ users actually rely on Hide My Email for safety-critical anonymity vs. mere spam reduction?
6. **Any evidence of real-world exploitation?** Reports describe *capability*, not confirmed abuse. Is there any indication threat actors have used it at scale?
7. **Apple's "twice fixed" claim.** Did Apple's Mar/May changes partially mitigate (e.g., new aliases safer, old ones not)? Or was it never addressed at all? The reporting conflates these.
8. **Does the `@private.icloud.com` domain migration actually fix the root cause,** or just cosmetically change the alias format while the underlying leak persists?
9. **Disclosure-window fairness.** Murphy says he warned Apple 12+ months ago; is that timeline corroborated by Apple, or only the researcher's account?
10. **Conflict of interest in framing.** EasyOptOuts benefits commercially from "your email can be linked to your identity" narratives. How much of the alarm is marketing-adjacent?
11. **Regulatory exposure.** Could this trigger GDPR/CCPA scrutiny (privacy feature that fails to deliver advertised protection)? Any DPA or FTC signal yet? (None found as of report date.)
12. **Comparison base rate.** Every alias/relay service (Firefox Relay, DuckDuckGo, SimpleLogin) can leak via forwarding metadata. Is this uniquely bad or an inherent limitation being framed as an Apple-specific failure?
13. **Fintech relevance test.** Does this materially affect payments, KYC, or financial-account security, or is it a general consumer-privacy story tagged into a fintech feed?
14. **Reputational vs. material impact.** Is the real story "Apple's privacy brand is dented" rather than any quantifiable user harm or financial loss?

**Importance: 3/5** — Credible, independently reproduced privacy failure in a widely-deployed Apple feature, with a damaging "reported over a year ago / twice claimed fixed" narrative and 100% exploit rate in tests. Downgraded from higher because: no confirmed real-world exploitation, technical scope undisclosed, source has a commercial interest, and the fintech/financial-risk linkage is indirect (identity-linkage risk, not payments/KYC breach). Notable as a reputational blow to Apple's privacy branding rather than a systemic financial-sector event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Privacy-as-a-feature inside Apple's iCloud+ subscription bundle (Hide My Email, Private Relay, custom email domains), which sits within the Services segment. Services hit an all-time high of ~$30.98bn in Apple's fiscal Q2'26 (quarter ended 2026-03-28), +16.3% YoY, beating the ~$30.4bn consensus (per Variety/9to5Mac, as of 2026-04-30); segment covers App Store, Music, TV+, Apple Pay, AppleCare, iCloud and ads. Structure: this is not a standalone market — it is a retention/differentiation lever bundled into a consolidated, single-vendor ecosystem where the moat is device lock-in, not a priced privacy product. "Why now": the value of "privacy" here is reputational, not directly monetized, so a credible failure of the promise is a brand/trust liability rather than a revenue line at risk (analysis). Consumer data-removal/anti-broker tooling is a real adjacent niche — the researcher who found the bug (Tyler Murphy) co-founded EasyOptOuts, a paid data-removal service, which is a conflict-of-interest flag to note when weighing the "100% exploitable" claim.

**Competitive landscape.** KPIs that actually matter here: Services revenue (~$31bn/qtr), iCloud+ / paid-subscription attach and churn — Apple does NOT break out iCloud+ subs or Hide My Email usage, so adoption is `[UNSOURCED]`. Basis of competition for "privacy" is trust/brand + default-on integration, not price. Peers on the privacy-tool axis: Proton (Proton Mail / SimpleLogin aliasing), Firefox Relay (Mozilla), DuckDuckGo Email Protection, 1Password/Fastmail masked email — all offer email-aliasing that competes functionally with Hide My Email but lacks Apple's OS-level distribution. Recent move: bug publicly disclosed by 404 Media 2026-07-01; researcher says he reported it to Apple in June 2025, Apple claimed a March 2026 fix that didn't hold, promised a security update "in coming weeks" by end-May, and as of publication had not shipped a specific fix or public guidance (per 404 Media / TechCrunch, 2026-07-01). Apple's position: dominant on distribution, but this is the third documented "privacy feature that doesn't work as advertised" episode (2022 iPhone Analytics suit; 2023 randomized-MAC research), which erodes the credibility differentiation vs. purpose-built privacy vendors (analysis).

**Comps & multiples.** No deal/valuation/round attaches to this news — it is a security-defect story, not a financing event, so trading multiples are not the right lens (Apple is a ~$3T mega-cap where a single feature bug is immaterial to EV/Revenue). Multiple = "no data / not applicable." Internal comps are the relevant benchmark — recent fintech/consumer privacy & exposure incidents in the corpus: [[Klarna confirms customer data leak]] (2025-11), [[Wealthsimple discloses third-party-linked customer data breach]] (2025-09), [[Betterment confirms data breach via fake crypto notification]] (2026-01), [[Figure data breach exposes nearly 1 million accounts]] (2026-02), [[IDMerit exposes one billion identity records in data leak]] (2026-03), [[47 million Pix keys exposed in Brazil security incidents]] (2026-03). Pattern vs. those: this is NOT a breach/exfiltration (no attacker, no stolen records) but a *design/implementation flaw* that defeats a privacy guarantee — closer to a mis-sold-safety issue than a hack, which changes the liability profile (regulatory/reputational, not incident-response/notification).

**Risk flags.**
1. Regulatory/legal — a privacy feature marketed as protective but demonstrably leaking the protected attribute invites consumer-protection and false-advertising exposure (cf. the 2022 iPhone Analytics suit); second-order: raises the bar for how Apple can market "privacy" and could draw FTC/EU DPA attention given Apple's explicit privacy branding.
2. Trust/brand disintermediation — privacy is Apple's stated differentiator; repeated "feature doesn't work" episodes let purpose-built rivals (Proton, DuckDuckGo, Firefox Relay) argue Apple's privacy is theater, chipping at the one intangible moat Services leans on (analysis).
3. Source credibility / disclosure conflict — the "100% exploitable" figure comes from a small-sample volunteer test by a researcher who sells a competing paid data-removal product, and full technical details are withheld; the claim is directionally serious but not independently quantified, so treat the magnitude as unverified.

**What this changes (idea-lens).** (analysis) Financially immaterial to Apple — Services is ~$31bn/qtr and this bug moves no revenue line near-term. The real signal is thesis-level: it's a data point that Apple's "privacy as product" narrative is thinner in execution than in marketing, which matters if/when Apple tries to *monetize* privacy directly or defend Services multiples on a "trust premium." Falsifiable trigger to watch: whether Apple ships a specific, dated fix and public acknowledgment within weeks (promised "coming weeks" since late May and already slipped) — continued silence, or a consumer/regulator suit citing the marketing gap, would confirm the thesis; a fast, transparent patch would break it.

Sources: https://techcrunch.com/2026/07/01/apples-hide-my-email-feature-has-a-bug-thats-been-exposing-real-email-addresses-researcher-claims/ · https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/ · https://9to5mac.com/2026/07/01/apple-hide-my-email-bug-seemingly-allows-100-of-real-email-addresses-to-be-discovered/ · https://variety.com/2026/digital/news/apple-earnings-march-2026-quarter-services-revenue-1236734606/ · IR (Apple 8-K Q2'26, 2026-04-30): https://drive.google.com/file/d/1_uvUD6knhjPswOU-v6sDiV64CVW9L0Sj/view (EDGAR: https://www.sec.gov/Archives/edgar/data/320193/000032019326000011/a8-kex991q2202603282026.htm)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** BEAT · Q2 FY2026 (three months ended 2026-03-28) revenue $111.18bn (+16.6% YoY; vs public consensus ~$109.66bn → beat by ~$1.5bn / +1.4%) · diluted EPS $2.01 (+22% YoY; vs consensus $1.95 → +$0.06 / +3.1%) · net income $29.6bn · drivers: iPhone 17 super-cycle + Services all-time high + Greater China re-acceleration; margin expansion. Guidance action: Apple gives no formal numeric guidance, but raised the dividend +4% to $0.27/share and authorized an additional $100bn buyback. Note: this earnings context is offered only as a scale check on the Hide My Email privacy story — the bug is not itself a reported financial item and has zero visible impact on these results.

**Key figures (with growth) — reported in Apple's own 10-Q / 8-K press release.**
- Total net sales: $111.184bn vs $95.359bn → **+16.6% YoY** (March-quarter record).
- Products: $80.208bn vs $68.714bn → +16.7%. Services: $30.976bn vs $26.645bn → **+16.3%** (new all-time high).
- iPhone: $56.994bn vs $46.841bn → **+21.7%** (March-quarter record, driven by iPhone 17).
- Mac $8.399bn (+5.7%) · iPad $6.914bn (+8.0%) · Wearables/Home/Accessories $7.901bn (+5.0%).
- Total gross margin $54.78bn → **49.3% vs 47.1%** prior year (+2.2pp). Products GM 38.7% (vs 35.9%); Services GM 76.7% (vs 75.7%).
- Opex: R&D $11.419bn **+33.6%** (10% of sales, up from 9%); SG&A $7.477bn +11.1% — R&D growing far faster than revenue (AI/silicon spend).
- Diluted EPS $2.01 (+22% YoY); net income $29.6bn. Operating cash flow >$28bn (March-quarter record).
- Capital return: quarterly dividend raised to $0.27/share (+4%); additional $100bn repurchase authorization.

**By segment / driver.** All five geographies grew double digits: Americas $45.093bn (+11.9%), Europe $28.055bn (+14.7%), **Greater China $20.497bn (+28.1%)** — the standout re-acceleration after multiple soft China quarters, Japan $8.401bn (+15.1%), Rest of Asia Pacific $9.138bn (+25.3%). Growth is broad-based, not one region. iPhone (+21.7%) is the single largest driver; Services (+16.3%) is the quality driver — 76.7% gross margin, recurring, and the segment most exposed to the privacy-brand narrative in this note.

**vs expectations / prior period.** Beat on the two headline lines: revenue $111.18bn vs public consensus (LSEG) ~$109.66bn (+$1.52bn / +1.4%); EPS $2.01 vs $1.95 (+3.1%); gross margin 49.3% vs ~48.4% expected. Category beats: Mac ($8.4bn vs ~$8.02bn), iPad ($6.91bn vs ~$6.66bn), Services ($30.98bn vs ~$30.39bn). The one soft spot: **iPhone $56.99bn came in marginally below the ~$57.21bn consensus** — a beat carried by everything except the flagship, which merely met the record bar rather than crushing it. No prior Apple earnings-review note exists in the corpus to wikilink; adjacent Apple-Pay/regulatory items are context-only. (Consensus figures are public aggregator consensus as of the 2026-04-30 print, labeled as such — not paid Street feeds.)

**Guidance / forward.** Apple issued no formal numeric revenue/margin guidance (consistent with its practice of qualitative color on the call). Management tone (CEO Tim Cook, CFO Kevan Parekh) was confident: Cook cited "extraordinary demand for the iPhone 17 lineup" and a March-quarter iPhone record; Parekh flagged a new all-time high for the active installed base across all major categories. What they emphasize: installed base, Services momentum, capital return. What is not addressed in the release: nothing on the Hide My Email vulnerability or privacy-feature reliability — expected, as it is a security-research claim, not a financial disclosure item.

**Thesis-flags.**
1. **Services is the profit engine and the brand at risk.** Services grew +16.3% at 76.7% gross margin — the highest-quality, most recurring revenue. Why it matters: the Hide My Email bug (404 Media / researcher Tyler Murphy claim, reportedly 100% of tested aliases exploitable, unpatched >1yr) attacks the privacy value-proposition that underpins iCloud+/Services stickiness and Apple's premium positioning. Second-order: no near-term revenue impact visible in this print, but repeated "privacy feature is effectively useless" episodes (2022 analytics suit, 2023 MAC-randomization) erode the differentiator that justifies Services pricing power over the long run.
2. **Greater China +28.1% is the biggest positive surprise.** Fact → China re-accelerated hard after years of soft/negative prints → why it matters: removes a standing bear pillar → second-order: privacy/security controversies carry outsized regulatory and brand risk precisely in markets where Apple sells on trust; a China-specific privacy scandal would be more thesis-relevant than a US researcher claim.
3. **Margin quality is expanding, not just revenue.** Gross margin 49.3% (+2.2pp) with Products GM up on mix despite tariff costs. Why it matters: beat is margin- and mix-driven (sustainable) more than a one-off. Second-order: gives Apple room to absorb any remediation/compliance cost from privacy issues without denting the model.
4. **R&D +33.6% (opex outpacing revenue).** The one line to watch — spend is ramping well ahead of the +16.6% top line (AI/silicon). Not a red flag at these margins, but it is where the "who's silent about the payoff" question sits: heavy invest-ahead with the return still qualitative.

Sources: Apple 10-Q Q2 FY2026 (period ended 2026-03-28, filed 2026-05-01) — reported net sales / category / segment / gross-margin / opex figures · Apple Q2 FY2026 earnings press release / 8-K Ex-99.1 (filed 2026-04-30), primary: https://drive.google.com/file/d/1_uvUD6knhjPswOU-v6sDiV64CVW9L0Sj/view (url fallback https://www.sec.gov/Archives/edgar/data/320193/000032019326000011/a8-kex991q2202603282026.htm) · Apple Newsroom press release (EPS $2.01 +22%, rev +17%, dividend $0.27 +4%, $100bn buyback): https://www.apple.com/newsroom/2026/04/apple-reports-second-quarter-results/ · public consensus & net income $29.6bn: https://www.cnbc.com/2026/04/30/apple-aapl-q2-2026-earnings-report.html · https://www.macrumors.com/2026/04/30/apple-2q-2026-earnings/ · source news (Hide My Email bug): TechCrunch/404 Media, 2026-07-01.
<!-- /enrichment:earnings_review -->
