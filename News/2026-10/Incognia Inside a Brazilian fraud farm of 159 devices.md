---
title: "Incognia: Inside a Brazilian fraud farm of 159 devices"
date: 2026-10-16
retrieved: 2026-10-16
tags:
  - company/incognia
  - industry/fraud-risk
  - region/latam
  - type/research-report
sources:
  - https://www.incognia.com/the-signal-finserv-newsletter/fraud-farm-159-devices-11150-accounts-one-apartment
  - https://www.incognia.com
status: enriched
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
story_id: s9c30cb78
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Incognia: Inside a Brazilian fraud farm of 159 devices

> [!info] 2026-10-16 · 2 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] And speaking of financial infrastructure, Incognia uncovered a fraud operation in Brazil that grew to 159 devices accessing more than 11,150 accounts. Its investigation shows how precise location intelligence can expose coordinated fraud that device-level analysis alone might miss.

[Connecting the Dots in Fintech] 💡Incognia:159 Devices, 11,150+ Accounts: Inside a Fraud Farm. Incognia CEO Andre Ferraz reveals how a fraud operation in Brazil grew from 8 devices accessing 153 accounts to 159 devices accessing 11,156 accounts in just a few months. The breakthrough came from apartment-level location analysis, which connected suspicious devices to the same physical operation and exposed its growth over time. The case highlights why analysing device behaviour alone isn't enough, precise location intelligence can uncover coordinated fraud networks while helping avoid false positives against legitimate users. Read the full investigation hereIncognia Uncovers 159 Device Fraud Farm In Brazil

## Первоисточники

### incognia.com
<https://www.incognia.com/the-signal-finserv-newsletter/fraud-farm-159-devices-11150-accounts-one-apartment>
*730 слов · direct*

159 devices. 11,150+ accounts. One apartment. 
Subscribe to The Signal: FinServ

 In just a few months, one fraud farm grew from 8 devices accessing 153 accounts to 159 devices accessing more than 11,150 accounts. 
Several of those devices were already suspicious on their own. They were accessing unusually high numbers of accounts.
But apartment-level location is what showed us that they were connected to the same physical operation.
Once we found that location, we were able to look backward and forward in time and see the farm grow.
Here’s how we found it.
 Note: This particular farm was in Brazil, but this kind of operation isn’t specific to Brazil. We’ve found similar farms in other markets. 
1. It started with a few suspicious devices
In May, our team was analyzing suspicious device activity across one bank’s app.
A few devices immediately stood out. In 30 days, one had accessed 1,181 accounts. Another had accessed 1,108 accounts . And a third had accessed 1,040 accounts .
Those numbers were enough to make each device worth investigating on its own.
The first device (which had accessed 1,181 accounts) was the highest-volume suspicious device in the analysis.
So we started there.
2. Apartment-level location uncovered a much larger cluster
We looked at the physical location associated with that device.
At the same apartment, we found 15 suspicious devices in total .
Together, those devices had accessed 3,353 accounts .
And those accounts weren’t concentrated around that same place. They were spread across the country.
 
Then we noticed something else.
The other two high-volume devices from the May analysis, the ones that had accessed 1,108 and 1,040 accounts, were operating from that same location too.
What looked like a few separate suspicious devices was starting to look like a much larger operation.
3. Looking back showed the cluster was already growing
We compared activity at the same apartment in April with what we had found in May.
In April, there were 8 suspicious devices accessing 153 accounts.
By May, there were 15 suspicious devices accessing 3,353 accounts.
 
4. The team kept following the same apartment
From there, the investigation became simpler.
We had a physical place we could keep watching.
Over the next couple of months, more suspicious devices appeared at that same apartment and the number of accounts they were accessing kept climbing.
From April through July, suspicious devices grew from 8 to 159. Accounts accessed grew from 153 to 11,156 
While the devices changed and volume grew, the apartment stayed the common point connecting them.
5. One device inside the farm showed how much reuse was happening
One device inside that larger cluster became especially active.
In June, it had accessed 1,765 unique accounts .
By July, that number had reached 7,096 .
That’s roughly a 4x increase in one month .
And to be clear, that is one device in the farm, separate from the total for the full location**.**
This gives you a sense of how heavily individual devices inside these operations can be reused.
 
6. The bank blocked the devices from the suspicious location
By following the same physical location over time, the team was able to identify the larger device farm operation.
The bank ultimately blocked the devices associated with that location.
For this to work, you have to have apartment-level location.
If the location signal is too broad, you risk catching legitimate users who live in the same apartment building or nearby buildings. That creates a false-positive problem very quickly.
Apartment-level location lets you isolate the suspicious location closely enough to act on it without pulling nearby legitimate users into the same decision.
The pattern you may be missing is physical
The team could already see that individual devices were behaving suspiciously.
What they couldn’t see from those device-level signals alone was that several of the highest-volume devices were operating from the same apartment.
Apartment-level location connected those devices to the same physical place.
That changed the investigation from a series of suspicious devices into a view of the larger operation behind them.
That physical connection allowed the team to see the farm, follow its growth over time, and block the devices without affecting legitimate users nearby.
 We see fraud farms like this a lot. If this is the kind of visibility you’re missing, we can show you how it works. 
 Book a call → 
André Ferraz

### Прочие ссылки (без извлечённого текста)

- <https://www.incognia.com>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Incognia — Inside a Brazilian fraud farm of 159 devices
_Analytical notes (not a post). Importance: 2/5._

**Freshness: FRESH** — this is a new, specific case-study/investigation write-up (The Signal: FinServ newsletter, Oct 2026), not a re-run. It is thematically adjacent to Incognia's earlier mule/ATO content ([[Incognia the state of mule account handovers in 2026]], [[Incognia podcast on large-scale account fraud at MRC 2026]], [[Incognia's Andre Ferraz on the AI-enabled fraud landscape]]) but the specific Brazil farm (8→159 devices, 153→11,156 accounts, Apr–Jul) has not been covered before. Content-marketing, not a corporate event.

## [0] What exactly happened (de-PR'd)
- Incognia published a first-person investigation of a single fraud farm it detected inside **one bank's app in Brazil**. Timeline: May analysis flagged three high-volume devices (1,181 / 1,108 / 1,040 accounts touched in 30 days). Tracing the top device to its physical location ("apartment-level") revealed 15 co-located suspicious devices (3,353 accounts). Looking back to April: 8 devices / 153 accounts. Following the apartment through July: **159 devices / 11,156 accounts**. One device alone scaled 1,765→7,096 unique accounts June→July (~4x). The bank ultimately blocked the devices tied to that location.
- **What it actually is:** a thought-leadership / demand-gen piece ("Book a call →"), not a product launch, funding, deal, or disclosed customer win. No bank is named; no loss figure ($/R$) or prevented-loss figure is given; "accounts accessed" ≠ accounts drained — the economic impact is left unquantified.
- **Why framed this way:** the narrative is engineered to sell the ONE differentiator Incognia owns vs. device-only rivals — precise, apartment-level location. The de-PR'd claim is narrow and defensible: *device-level signals flagged the devices individually; location was what connected them into one operation and let the team track growth over time without false-positiving neighbors.* The farm was "found" and "blocked" — but note the lag: Incognia says it could look "backward" to April, i.e. the farm ran ~3 months and scaled 70x before being shut, which is as much an argument about detection latency as about detection power.

## [1] Competitors / peers
- **Device/behavioral-intelligence incumbents:** Sift (e-commerce/marketplace account+payment fraud), BioCatch (behavioral biometrics — typing/mouse/session; strong on ATO, scams, mules in banking), Sardine (device + behavior "DIBB" signals + 40+ enrichment sources; money-movement fraud), plus SEON, Feedzai, Unit21, Fingerprint, Bureau. Most lead with *device fingerprint + behavioral biometrics + network/velocity* signals.
- **Incognia's position (differentiated, not ahead on everything):** it is the one leaning on **first-party GPS/sensor location → "apartment-level"** resolution. The case is implicitly a swipe at device-only approaches ("device behaviour alone isn't enough"). BioCatch/Sardine would catch the same velocity anomaly (1,000+ accounts/device) on behavior/velocity; the genuinely harder thing they can't do is *physically co-locate* the devices to one apartment and track the cluster over months.
- **Why the lay of the land is this way:** location is a hard moat (needs an SDK embedded in the bank's own app + user consent to GPS/sensors) but also a limitation — it only works in-app, on mobile, with location permission, and is useless for web-only or spoofed-GPS flows. So the competitive story is "complementary layer," not "replacement." Second-order: velocity alone (1,181 accounts in 30 days) was *already* a screaming red flag — the honest read is that location's real value here was reducing false positives and enabling a durable "watch this apartment" anchor, not first-detection.

## [2] Company history / fit
- Incognia: founded ~2010 by André Ferraz + Alan Gomes out of Recife, Brazil (pivoted from In Loco ad-tech, acquired by Magalu); refocused on fraud prevention ~2020. Funding ~$46.5M total (incl. $15.5M Series A, $31M Series B led by Bessemer). Claims presence on hundreds of millions of devices.
- Fit: Brazil is Incognia's home turf and the most intense real-time-payments fraud market globally — natural place to source a flagship case. Consistent with a steady 2026 content cadence: mule-account handover research, MRC talks on large-scale account fraud, Webull Brazil onboarding win ([[Webull Brazil hits 92.5% frictionless onboarding with Incognia]]), AI Rule Builder, AI Agent Detection ([[Incognia launches AI Agent Detection for financial institutions]]).
- **Why it acts this way:** a location-SDK vendor must constantly prove location beats pure device/behavior analytics (its whole premium rests on that), so publishing vivid "location cracked the case" investigations is core go-to-market, not incidental PR.

## [3] Novelty / value-add / traction
- **Novelty:** low. The *technique* (location clustering to find fraud farms) is long-standing Incognia messaging — the company has blogged for years about "fraud farms" and location spoofing. What's new is only the specific, numeric case study. No new product, metric methodology, or customer disclosed.
- **Value-add (real, but narrow):** the defensible insight is physical co-location as a graph edge device-only tools lack, plus low false positives from apartment-level precision. Traction here is anecdotal (one unnamed bank, one farm) — not a fleet metric, not a prevented-loss number, not a named reference. "Accounts accessed" is a deliberately soft denominator.
- **Who captures the margin:** Incognia sells a signal layer into the bank's fraud stack; the bank owns the block decision and the liability. The case quietly concedes the bank did the blocking — Incognia's value is detection/attribution, which is valuable but commoditizing as every rival adds ML on velocity/network signals.

## [4] What's next / market sentiment
- Backdrop strongly tailwinds the pitch: Brazil Pix fraud ~R$6.5B (2025), ~28M Pix fraud cases in 9 months; BCB Resolution 506/2025 made behavioral monitoring mandatory for SPI participants + a fraud-marking system; Law 15,397/2026 criminalizes knowingly lending accounts. Regulators are forcing banks to buy more fraud tooling — demand tailwind for Incognia and all peers.
- **Why the market goes this way / second-order:** mandatory monitoring commoditizes the baseline and rewards differentiated signals, which helps Incognia's location angle — but also invites every incumbent to add "device graph / co-location" features, eroding the moat. Counterintuitive risk: as fraudsters learn location is the tripwire, farms distribute across many apartments / spoof GPS / move to web, degrading exactly the signal this case celebrates. The investigation is best read as marketing of a known capability into a hot regulatory moment, not a new development.

## Sources
- Primary: Incognia, "159 devices. 11,150+ accounts. One apartment." The Signal: FinServ newsletter — https://www.incognia.com/the-signal-finserv-newsletter/fraud-farm-159-devices-11150-accounts-one-apartment
- Incognia background/funding: https://www.incognia.com/newsroom/incognia-raises-15m-series-a-to-combat-increased-identity-fraud ; https://fintechmagazine.com/fraud-id-verification/incognia-series-b-funding
- Competitors: https://bureau.id/resources/blog/sardine-competitors ; https://cside.com/blog/best-device-intelligence-for-fraud-prevention
- Brazil fraud/Pix backdrop: https://seon.io/resources/lessons-from-brazil-pix-incident/ ; https://www.biocatch.com/blog/new-legislation-raises-stakes-for-mules-in-brazil ; https://www.riotimesonline.com/pix-rules-central-bank-brazil-fraud-exemption-2026/
- Internal: [[Incognia the state of mule account handovers in 2026]], [[Incognia podcast on large-scale account fraud at MRC 2026]], [[Webull Brazil hits 92.5% frictionless onboarding with Incognia]], [[Incognia launches AI Agent Detection for financial institutions]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **"Accessed" vs. "defrauded"** — 11,156 accounts were *accessed*; how many were actually drained, and what R$/$ was stolen or prevented? Open — no loss figure given; the big number is deliberately the softer "accounts accessed" denominator.
2. **Who was first to detect?** Velocity alone (1,181 accounts/device in 30 days) already flagged the devices. So was location *detection* or merely *attribution + false-positive reduction*? Per the text, location connected and tracked them — i.e. attribution, not first-detection. Dilutes the "device-alone isn't enough" claim.
3. **Detection latency.** The farm ran April→July (~3 months) and scaled ~70x before the bank blocked it. Is a 3-month dwell a success story or an indictment of the pipeline? Open — framed as success; arguably exposes lag.
4. **Named customer / reference?** No bank is named, no case approved for attribution. Reduces evidentiary weight to anecdote.
5. **Is the technique new?** No — Incognia has blogged about "fraud farms" and location clustering for years. Novelty is the specific numbers only.
6. **Spoofing counter.** What stops the farm from spoofing GPS or distributing across many apartments once they learn location is the tripwire? Open — not addressed; this is the core durability risk.
7. **Coverage limits.** Location only works in-app, on mobile, with GPS/sensor permission granted. What share of the bank's fraud surface (web, no-permission users) does it even see? Open.
8. **False-positive claim.** "Apartment-level avoids catching neighbors" — any quantified FP rate for this case, or just assertion? Assertion only.
9. **Why only one bank, one farm?** If "we see fraud farms like this a lot," why not a portfolio stat (farms detected / accounts protected across clients)? Suggests the vivid single case is the strongest available proof point.
10. **Competitive delta durability.** BioCatch (behavioral), Sardine/Sift (device+velocity), SEON would all flag the velocity anomaly. The only thing they can't do is physical co-location — how defensible is that once rivals add device-graph features? Open; moat is narrow.
11. **Regulatory pull-through.** Does BCB Res. 506/2025 (mandatory behavioral monitoring) + Law 15,397/2026 actually force banks to buy *location* specifically, or just "monitoring"? Likely the latter — tailwind is generic, not Incognia-specific.
12. **Economic incentive of the piece.** Ends in "Book a call →" — this is demand-gen content, so every framing choice favors location. Weight accordingly.
13. **Second-order on the bank's action.** The bank blocked devices by location; does that create a disintermediation risk where the bank operationalizes co-location internally and churns the vendor? Open.
14. **Attribution to Incognia vs. bank's own team.** The narrative says "our team" analyzed, but the bank blocked — how much of the win is Incognia's signal vs. the bank's fraud ops? Shared; unquantified.

**Importance: 2/5** — Well-told, concrete investigation that credibly illustrates a real (narrow) differentiator (apartment-level co-location), and lands into a hot Brazil/Pix fraud-regulation moment. But it is demand-gen content marketing, not a product/funding/deal event: no named customer, no loss/prevented figure, zero new capability, a known technique, and a soft "accounts accessed" metric. Fresh (new specific case) but low weight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Device-intelligence / location-intelligence fraud prevention sits inside the broader fraud-detection market, sized at ~$34.6bn in 2025 growing to ~$40.9bn in 2026 (~18.1% CAGR) and ~$80.2bn by 2030 (~18.3% CAGR) (per Research and Markets, via researchandmarkets.com, as of 2026). Structure: fragmented across behavioral biometrics (BioCatch), orchestration/ML (Sardine, SEON), identity verification (Socure) and device+location signals (Incognia) — value accrues to whoever supplies the lowest-false-positive risk signal to the bank's decision layer, with network effects (devices/places mapped) and switching costs (embedded SDK) as the main moats. "Why now": the farm Incognia describes (8→159 devices, 153→11,156 accounts, Apr–Jul) illustrates industrialized mule/ATO operations at scale, the same driver behind Visa's Aug 2026 BioCatch buy — fraud is moving upstream of the payment, and incumbents are paying up to own pre-transaction signals.

**Competitive landscape.** Sector KPIs: devices/users covered, false-positive rate, detection precision, net revenue retention (SDK stickiness). Key players & basis of competition — **BioCatch** (behavioral biometrics, 1.8bn devices / 760M users / 350+ FIs / 21 countries); **SEON** (ML + digital-footprint, AML); **Sardine** (fraud + AML orchestration); **Socure** (identity verification); **Incognia** (device + apartment-level location fusion). Recent moves: Visa to acquire BioCatch for $2.4bn (announced 2026-08-03, largest Visa deal); SEON raised $80M Series C (2026-09); Sardine raised $70M Series C (2025-02, total $145M). Incognia's own 2026 cadence is product-led — AI Agent Detection, AI Rule Builder, Browser ID, Location 2FA (see [[Incognia launches AI Agent Detection for financial institutions]], [[Incognia launches AI Rule Builder for fraud detection]]). Position: **niche/differentiated** — Incognia protects ~1bn devices and maps 500M+ places monthly, and this case is a credible proof point that apartment-level location resolves clusters device-level signals alone miss (analysis). Moat: proprietary location graph (network effect) + embedded SDK (switching cost).

**Comps & multiples.**
- **BioCatch** — EV/ARR = $2.4bn / $160M ARR (Jun 2025) = **15.0x** (Visa acquisition, 2026-08; ARR per Sacra). Prior Permira buyout was ~$1.3bn (May 2024), so the mark roughly doubled in ~2 years.
- **SEON** — $80M Series C (2026-09); post-money not disclosed → round valuation "no data".
- **Sardine** — $70M Series C (2025-02), total raised $145M; post-money not disclosed → "no data".
- **Socure** — $4.5bn post-money at Series E (Nov 2021); no revenue disclosed → EV/Revenue "no data" (and a stale 2021 private mark).
- **Incognia** — last raise $31M Series B (Jan 2024, led by Bessemer); PitchBook valuation band ~$100–250M; revenue not disclosed → EV/Revenue `[UNSOURCED]`. Internal comps: [[SEON partners Yuno to expand global fraud prevention]], [[Alkami customers prevent over $263M fraud with BioCatch]].
- Distribution not computed (only 1 verifiable revenue multiple, BioCatch 15.0x). Qualitative read: BioCatch's 15.0x EV/ARR on 350+ FI scale sets a rich strategic-buyer benchmark; Incognia at a sub-$250M private band is an order of magnitude smaller and would re-rate only on a comparable M&A event (analysis).

**Risk flags.**
1. **Scale gap vs. acquired peers.** Incognia (~1bn devices, ~$100–250M band) is materially sub-scale vs BioCatch (1.8bn devices, $160M ARR, $2.4bn exit); as Visa/strategics internalize fraud signals, standalone niche vendors risk disintermediation — a bank-owned or network-owned signal can displace a point tool.
2. **Geographic/segment concentration.** The flagship evidence (this farm, Webull Brazil, Cabify) skews LatAm and app-based onboarding; location-signal quality and the mule-farm pattern may not generalize to other markets, concentrating revenue in a few verticals/regions.
3. **Signal-dependency / false-positive liability.** The method hinges on apartment-level precision — the note itself concedes a too-broad signal "catches legitimate users"; degraded location accuracy (OS privacy changes, VPN/GPS spoofing) erodes the core differentiator and shifts liability to the bank.

**What this changes (idea-lens).** This is a marketing-grade proof point, not a financial event — it reinforces the thesis that pre-transaction fraud signal is being consolidated by payment networks (Visa→BioCatch) (analysis). Falsifiable thesis: Incognia's next step is a strategic acquisition or deep network/FI partnership rather than a large growth round; trigger to watch — a network (Visa/Mastercard) or a core banking/orchestration player (vs SEON/Sardine) moving on device+location signals. What breaks it: Incognia raising a large independent growth round and scaling solo, signaling the location moat is defensible standalone.

Sources: https://www.researchandmarkets.com/reports/6255238/fraud-detection-market-report · https://www.incognia.com/newsroom/incognia-secures-31mm-series-b-funding-for-proactive-approach-to-fraud-prevention · https://pitchbook.com/profiles/company/152413-12 · https://finovate.com/visa-acquires-behavioral-biometrics-innovator-biocatch-for-2-4-billion/ · https://sacra.com/c/biocatch/ · https://www.biometricupdate.com/202509/seon-gets-80m-to-for-global-expansion-of-aml-fraud-prevention-platform · https://www.biometricupdate.com/202502/sardine-nets-70m-in-series-c-funding-for-automated-fraud-prevention-platform
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
