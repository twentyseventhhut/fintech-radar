---
title: "RBI introduces interoperability among Account Aggregators"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/rbi
  - industry/open-banking
  - region/india
  - type/regulation
sources:
  - https://economictimes.indiatimes.com/industry/banking/finance/rbi-opens-up-account-aggregator-network-making-financial-data-sharing-easier-for-consumers/articleshow/134756457.cms
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sf4d851d8
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# RBI introduces interoperability among Account Aggregators

> [!info] 2026-10-12 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Reserve Bank of India (RBI)introduced inter-operability among Account Aggregators for seamless financial data sharing.

## Первоисточники

### economictimes.indiatimes.com
<https://economictimes.indiatimes.com/industry/banking/finance/rbi-opens-up-account-aggregator-network-making-financial-data-sharing-easier-for-consumers/articleshow/134756457.cms>
*108 слов · direct*

Listen to this article in summarized format
Unlock AI Briefing and Premium Content
What's Included
Exclusive Stories
Daily ePaper Access
Smart Market Tools
Curated Investment Ideas
Ad-lite Experience
 Subscription
 
Live Events

So what does interoperability mean?
Does this mean anyone can access your bank data?
Why is RBI doing this?
(Catch all the Business News , Breaking News and Latest News Updates on The Economic Times .)
Subscribe to The Economic Times Prime and read the ET ePaper online.
(Catch all the Business News , Breaking News and Latest News Updates on The Economic Times .)
Subscribe to The Economic Times Prime and read the ET ePaper online.

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **7 Oct 2026**, as part of the RBI Statement on Developmental and Regulatory Policies (alongside the monetary policy review), Governor **Sanjay Malhotra** announced that the RBI will **mandate interoperability among NBFC-Account Aggregators (NBFC-AAs)**. Today's note is a one-line reprint of that announcement via "This Week in Fintech"; the underlying event is the RBI policy statement, not a bank-specific launch.

De-PR'd substance:
- **The actual change**: a customer registered with *any one* licensed AA app will be able to fetch and share data held across *all* Financial Information Providers (FIPs) on the network, instead of having to onboard separately with multiple AAs. One AA = full reach. (medianama, business-standard, Oct 2026)
- **Second measure bundled in**: SEBI-regulated depositories (NSDL/CDSL) can add **bank deposit information to the Consolidated Account Statement (CAS)** via NBFC-AAs, so a demat holder sees securities + bank deposits in one statement.
- **Status = announced, not live.** Both measures are **"expected to be implemented by 31 Dec 2026."** As of the announcement there is no circular text, no technical interoperability spec, no go-live. Treat as a policy direction, not a shipped feature.
- **Why framed this way**: the AA framework launched in 2021 with 17 operational AAs; fragmentation across AAs is a real friction (a user had to pick the right AA app for the right lender). Mandating interoperability is the RBI closing a known UX gap and nudging the network from "many walled AA apps" toward a single utility layer — consistent with its DEPA/consent-based data-sharing playbook. The CAS measure is a convenience bolt-on that mainly benefits the wealth/demat side (NSDL/CDSL turf).

## [1] Competitors / peers
- **Domestic AA operators** (the entities directly affected): 17 operational AAs incl. names like Finvu, OneMoney, CAMS Finserv, NeSL, Perfios/Anumati, PhonePe, plus infra players. Interoperability **commoditizes the "reach" of any single AA** — an AA can no longer differentiate on "which FIPs we connect to," since all become reachable through any AA.
- **AA infrastructure / enablers** in our corpus: [[Ignosis raises $4M for Account Aggregator infrastructure]] (TSP/analytics for 125+ BFSI clients), [[Indian fintech Finarkein raises $1.5M from DSP Group office]], [[Finfactor raises $15M Series A led by WestBridge]] — these TSPs benefit: interoperability raises the value of the data-intelligence layer sitting on top.
- **Global analogues**: this is India's version of **open-banking interoperability** — comparable in spirit to UK Open Banking's common API standard and EU PSD2/FiDA. Contrast with the US fight over screen-scraping/data access ([[JPMorgan Chase is moving to restrict Checkbook's access to its customer data,]]) — India's model is regulator-mandated and consent-first, the opposite of the US bank-gatekeeping posture. Other regional consent-manager moves: [[Turkey authorizes iyzico and Odeal for open banking]], [[Floid launches consent manager for Chile data and debt rules]].
- **Position**: India is **ahead** on scale of a live, consent-based data-sharing rail; interoperability is a maturity step, not a first-mover novelty.

## [2] Company history / fit (RBI + ecosystem)
- RBI issued the AA Master Directions in 2016 and the framework went live in 2021. Trajectory of RBI's 2025–26 digital-rail agenda in our corpus: [[RBI launches four digital payment initiatives]], [[RBI launches blockchain-based Unified Markets Interface]], [[RBI mandates risk-based authentication for digital payments]] — a consistent pattern of RBI building/mandating public digital infrastructure.
- **Direct predecessor note**: [[RBI recognises Sahamati Foundation as Account Aggregator SRO]] (8 Jun 2026) — RBI designated Sahamati as the self-regulatory body for the AA ecosystem. Interoperability is the **logical next move after an SRO exists**: first install governance, then mandate the harder technical/competitive standard. Also [[Account aggregator body Sahamati raises ₹50 crore]] (May 2026, from 30+ FIs) funded that SRO buildout.
- **Why RBI acts this way**: AA is RBI's flagship "public good" data layer (DEPA). A fragmented AA market undermines the whole thesis of consent-portable data; mandating interoperability protects the network-effect value of the rail it built. (analysis)

## [3] Novelty / value-add / traction
- **Ecosystem scale (the real story, FY26 / mid-2026 Sahamati data)**: ~1,117 live entities (1,076 FIUs, 176 FIPs, 17 AAs); the framework has processed on the order of **~45 crore (450M+) cumulative consents and ~500 crore data fetches**, **~3.8 crore financial services facilitated in FY26**, and reportedly enabled **~₹1.6 lakh crore of loans across ~1.8 crore loan accounts**. Daily consents >7 lakh. (Sahamati/newkerala/blitzindia — vendor-sourced; treat as directional, not audited.)
- **Novelty**: the AA rail is not new; interoperability *within* it is the new increment. Value-add is **real but incremental** — it removes onboarding friction and prevents AA-level data silos, which should raise completion rates and widen credit/wealth access. It does **not** add new data types or new use cases by itself.
- **Who captures margin**: AAs earn tiny per-consent fees; interoperability compresses their differentiation and pushes value **up-stack to the data-intelligence/TSP layer (Ignosis, Finarkein, Finfactor) and to the FIUs (lenders, wealth apps)** who get cheaper, fuller data. The AA operators themselves risk becoming thin, commoditized pipes. (analysis)

## [4] What's next / market sentiment
- **Timeline**: implementation by **31 Dec 2026** — watch for the actual RBI circular + Sahamati/ReBIT technical interoperability spec. Until then, announced ≠ live.
- **Drivers**: deepens India's open-finance thesis; positive for lenders and wealth-tech reliant on AA data (e.g. [[Indian FinTech platform Jupiter Money secures $13m funding]], [[Dezerv raises $40 million led by Premji Invest and Accel]]).
- **Risks / open**: (1) technical interoperability standard and liability for failed/partial fetches are unspecified; (2) consent fatigue and data-security remain the headline consumer concerns the ET source flags; (3) commoditization may thin AA-operator economics, raising consolidation risk among the 17 AAs. (analysis)

## Sources
- Economic Times (note primary source), Oct 2026 — https://economictimes.indiatimes.com/industry/banking/finance/rbi-opens-up-account-aggregator-network-making-financial-data-sharing-easier-for-consumers/articleshow/134756457.cms
- MediaNama, "RBI to make account aggregators interoperable," Oct 2026 — https://www.medianama.com/2026/10/223-rbi-account-aggregators-interoperable/
- Business Standard, "RBI allows account aggregator interoperability, enables CAS bank deposits," 7 Oct 2026 — https://www.business-standard.com/finance/news/rbi-account-aggregators-interoperability-cas-bank-deposits-december-2026-126100700369_1.html
- Outlook Money — https://www.outlookmoney.com/invest/rbi-account-aggregator-interoperability-bank-deposits-cas-financial-data
- Sahamati, "AA Framework Crosses 100 million Consents" / FY26 data — https://sahamati.org.in/
- NewKerala, "India's AA ecosystem facilitates ~3.8 crore services in FY26" — https://www.newkerala.com/news/a/indias-account-aggregator-ecosystem-facilitates-nearly-38-crore-263.htm
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5** — A genuine, named structural move on India's flagship open-finance rail (one of the largest live consent-based data-sharing networks globally), announced by the RBI Governor. Weight is capped below 4 because (a) it is **announced, not live** (target 31 Dec 2026), (b) it is an **incremental maturity step** on an existing 2021 rail, not a new capability, and (c) the note itself is a one-line reprint with a paywalled, content-thin source.

## FRESHNESS / DUPLICATE VERDICT: **FRESH**
This is the **interoperability mandate** from the RBI's 7 Oct 2026 Developmental & Regulatory Policies statement. It is **distinct** from the June 2026 SRO designation ([[RBI recognises Sahamati Foundation as Account Aggregator SRO]]) — different action, different date, different mechanism (governance body vs. technical/competitive interoperability standard). No prior note covers this specific rule. Not a duplicate. Verdict: **fresh**.

## Red-team / challenge questions
1. **Announced or live?** Announced 7 Oct 2026; **target implementation 31 Dec 2026**. No circular, no spec, no go-live yet. Do not present as shipped. (confirmed)
2. **Is it really new vs. the SRO recognition?** Yes — separate measure; SRO = who governs, interoperability = how AAs interconnect. (confirmed)
3. **What exactly changes for a user?** One AA app now reaches all FIPs on the network; no need to onboard multiple AAs. (confirmed)
4. **Who is actually affected first?** The 17 operational AAs (differentiation compressed) and the TSP/data-intelligence layer (value accrues up-stack). Consumers get convenience later. (analysis)
5. **Scale — is the rail material?** Yes: ~1,117 live entities, ~450M+ cumulative consents, ~500 crore fetches, ~3.8 crore services in FY26, ~₹1.6 lakh crore loans enabled. **But all figures are Sahamati/vendor-sourced**, not RBI-audited — directional only. (open on independent verification)
6. **Mechanism delta vs. status quo (one sentence):** removes AA-level data silos so any AA = full network reach, turning fragmented AA apps toward a single portable-consent utility.
7. **Who's silent on what?** No detail on the technical interoperability standard, fee/settlement model between AAs, or **liability for failed/partial data fetches** — the hard parts. (open)
8. **Does interoperability help or hurt AA operators?** Likely **hurts** per-operator economics (commoditizes reach), could trigger consolidation among 17 AAs; helps FIUs/lenders and TSPs. (hypothesis)
9. **Consumer risk?** Consent fatigue + data security are the ET source's own flagged questions; mandate doesn't resolve them. (confirmed as open)
10. **What would change the central question?** If the 31 Dec spec includes **cross-AA fee economics**, the question shifts from "convenience" to "who monetizes the unified AA utility" — regulator-as-utility vs. private-AA-margin. (analysis)
11. **Global framing correct?** Yes — India's regulator-mandated, consent-first model is the inverse of the US bank-gatekeeping fight ([[JPMorgan Chase is moving to restrict Checkbook's access to its customer data,]]); closer to UK Open Banking common standards. (analysis)
12. **Downside trigger?** Slipped Dec-2026 deadline or a watered-down circular would make this a PR milestone rather than a real step; also a data-breach on the unified rail would be systemic. (open)
13. **Is the CAS/bank-deposit measure material?** Minor — convenience for demat holders; benefits NSDL/CDSL + wealth-tech, not a structural shift. (analysis)
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-13]] (2026-10-13).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** India's Account Aggregator (AA) framework is the consent-layer of the DEPA (Data Empowerment and Protection Architecture) stack — the data analogue to UPI. As of June 2026 the ecosystem counted ~1,117 live entities (1,076 FIUs, 176 FIPs, 17 operational NBFC-AAs, 2 certifiers), ~493mn consent requests fulfilled and ~295mn monthly data shares, with AA-enabled lending cited at ~₹1.6 lakh crore across ~1.8 crore loan accounts (per Sahamati, via sahamati.org.in / newkerala.com, as of Jun 2026). Structure is a many-sided network split into FIPs (banks/NBFCs holding data), AAs (consent routers that see no plaintext data) and FIUs (lenders/PFM apps consuming it); value accrues to whoever owns distribution and analytics, not to the AA pipe itself. Why now: RBI (Gov. Sanjay Malhotra) announced on 2026-10-07 a mandate making NBFC-AAs interoperable, so a user can reach any FIP through a single AA of choice, with full rollout targeted by 2026-12-31 (per medianama.com / Outlook Money, Oct 2026). This mirrors UPI's switch-interoperability moment: it attacks the core friction that each AA was a siloed gateway requiring separate registrations, and that FIU/FIP onboarding of each new AA took ~3–6 months of legal/ops work (per Sahamati's B.G. Mahesh, via medianama.com).

**Competitive landscape.** Sector KPIs: consents raised/fulfilled, successful data-fetch rate, FIP/FIU coverage, and AA-enabled loan disbursal value. RBI is the rails-setter, not a competitor — the commercial layer is the ~17 licensed NBFC-AAs (e.g. Finvu/Cookiejar, Onemoney, CAMS Finserv, NeSL AA, Perfios/Anumati) plus infra/analytics players like [[Ignosis raises $4M for Account Aggregator infrastructure]] (raised $4M, 2025-10, ~125 BFSI clients). Basis of competition shifts with interoperability: once any AA can reach any FIP, AAs can no longer compete on which FIPs/FIUs they've wired up — differentiation moves to UX, consent-success/fetch reliability, and value-added analytics on top. Protagonist's position: RBI is cementing the ecosystem it already regulates; in June 2026 it recognised Sahamati as the AA SRO (via sahamati.org.in), so interoperability sits inside an established governance frame rather than being greenfield. (analysis)

**Comps & multiples.** No valuation/round/metrics attach to this pick (it is a regulator policy action), so trading multiples are not applicable — "no data". Internal comps for the same sub-sector: [[Ignosis raises $4M for Account Aggregator infrastructure]] (AA infra, $4M, 2025-10); adjacent RBI rails/open-finance actions in-base include [[RBI launches blockchain-based Unified Markets Interface]] and [[RBI launches four digital payment initiatives]]. External peer valuations for AA-native names are not publicly verifiable (most are private, no disclosed post-money) → `[UNSOURCED]`. Distribution not computed; qualitative comparison only.

**Risk flags.**
1. Execution/coordination risk — RBI itself flags that interoperability is "a coordination challenge across technology, standards, testing and operational processes"; a 2026-12-31 hard deadline on ~17 AAs + 1,000+ FIUs makes slippage and uneven data-fetch reliability the base case, which would blunt the consumer benefit.
2. Disintermediation of the AA layer — removing "which FIPs am I wired to" as a differentiator commoditises the consent-router role; margin and defensibility migrate to FIUs/analytics (e.g. Ignosis-type infra), so pure-play AAs risk becoming thin, interchangeable pipes.
3. Privacy / consent-abuse surface — one-door access to all FIPs plus data-fetch volume (~500 crore fetches cited in FY26) raises the stakes on consent clarity and fraud; RBI is simultaneously imposing new consent/UX, 2FA and notification standards (compliance deadline 2026-10-31), and the economics of who bears liability for mis-consented data pulls are not spelled out.

**What this changes (idea-lens).** (analysis) This is a "UPI-ification" of financial data: interoperability should expand FIU reach and compress AA onboarding cost, accelerating AA-based lending and PFM adoption — bullish for FIUs and AA analytics/infra, structurally dilutive for standalone AA toll-takers. Falsifiable thesis: by mid-2027, monthly data-shares and AA-enabled disbursals re-accelerate vs the ~295mn/month June-2026 base once single-AA access is live. Watch triggers: the 2026-12-31 go-live and whether RBI issues pricing/liability rules — if AA pricing stays capped/zero like UPI, expect further consolidation among the ~17 NBFC-AAs.

Sources: https://www.medianama.com/2026/10/223-rbi-account-aggregators-interoperable/ · https://www.medianama.com/2026/10/223-sahamati-bg-mahesh-rbi-account-aggregator-interoperability/ · https://www.outlookmoney.com/invest/rbi-account-aggregator-interoperability-bank-deposits-cas-financial-data · https://sahamati.org.in/ · https://www.newkerala.com/news/a/indias-account-aggregator-ecosystem-facilitates-nearly-38-crore-263.htm · https://vinodkothari.com/2026/10/one-door-many-aggregators-rbis-interoperability-push-for-nbfc-account-aggregators/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
