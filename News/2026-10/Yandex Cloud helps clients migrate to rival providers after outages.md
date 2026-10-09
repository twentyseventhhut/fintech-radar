---
title: "Yandex Cloud helps clients migrate to rival providers after outages"
date: 2026-10-09
retrieved: 2026-10-09
tags:
  - company/yandex
  - industry/infrastructure
  - region/ru
  - type/product
sources:
  - https://vc.ru/services/3185215-yandeks-soglashenie-s-oblachnymi-provaiderami
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s3aee928e
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Yandex Cloud helps clients migrate to rival providers after outages

> [!info] 2026-10-09 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Yandex Cloud организовал для своих клиентов ускоренный переезд к другим облачным провайдерам, включая прямых конкурентов. Помощь — для тех, чьи сервисы пострадали после инцидентов в дата-центрах компании и кому нужен переезд.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://vc.ru/services/3185215-yandeks-soglashenie-s-oblachnymi-provaiderami>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Yandex Cloud helps clients migrate to rival providers after outages
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
The source note frames this as Yandex Cloud "organising an accelerated migration" for affected clients — a seemingly magnanimous customer-service gesture. The de-PR'd reality is far sharper: **this is disaster recovery after a physical war attack, not a product initiative.**

- On the night of 7–8 Oct 2026, a Ukrainian drone strike set fire to Yandex's data center in Sasovo (Ryazan Oblast); the site stopped operating entirely and the `ru-central1-b` availability zone went offline (comss.ru, vbr.ru, Lenta.ru). Yandex initially softened the public framing as "a power outage at a data center" before acknowledging the attack.
- On 9 Oct 2026 a **second** facility, in Kaluga, was hit; part of its infrastructure failed, and reporting flagged possible damage to AI-training supercomputers (The Moscow Times, The Register, CNBC, GIGAZINE).
- Impact: 1,200–1,300+ complaints; Yandex Cloud, Yandex Documents, Yandex Tables disrupted; major media (Vedomosti, RIA, Kommersant, Interfax, RBC) had loading problems. Creation of new cloud resources was limited; Yandex would not commit to restoration timelines and could not confirm whether the Sasovo equipment is recoverable.
- The "migration to rivals": Yandex signed agreements with **VK Cloud, Selectel and K2Cloud** to host affected clients' infrastructure on their sites — extra specialist teams, simplified onboarding, "flexible financial terms" (ixbt, anti-malware.ru, vz.ru, abn.agency, profile.ru).

**Why structured this way / what it reveals:** You do not voluntarily hand your paying customers to three direct competitors unless you physically cannot serve them yourself. This is an admission that Yandex's own remaining capacity could not absorb the failed zones fast enough — i.e. the damage is severe and (at least short-term) irreversible for Sasovo. The "helping clients" PR frame inverts a forced capitulation into goodwill. The real signal is **concentration risk in Russian critical infrastructure now has a kinetic-war dimension** that cloud SLAs never priced.

## [1] Competitors / peers
The "rivals" are the recipients, which makes the competitive read unusual:
- **Cloud.ru** (ex-SberCloud) — IaaS market leader (~29.7% IaaS share 2025; 32.5% combined IaaS+PaaS) (tadviser). Notably NOT named among the three rescuers — possibly a coordination/trust gap, or simply not approached.
- **VK Cloud** (VK Tech) — ~9bn RUB H1 2026 revenue, +35% YoY; a recipient here.
- **Selectel, K2Cloud** — mid-tier IaaS/colocation players, recipients.
- **MWS Cloud** (MTS) — growing ML-storage player ([[MWS Cloud launches fastest S3 storage for ML workloads]]), not involved.
- Western AWS/GCP/Azure — irrelevant in RU (foreign share ~1%).

**Why the lay of the land is this way / second-order:** Rivals accepting Yandex's refugees get a rare, low-CAC land-grab of enterprise workloads under duress — but also inherit the same target profile. The counterintuitive dynamic: cooperation here is self-interested **systemic-risk insurance** (any RU provider could be hit next; a reciprocal mutual-aid norm benefits all) more than altruism. It also hints the regulator/Mintsifry likely coordinated it.

## [2] Company history / fit
Yandex Cloud sits inside Yandex B2B Tech (H1 2026 revenue 28.9bn RUB, +32% YoY) and is the broad-market cloud leader (~24%), targeting half the Russian enterprise-AI market (Vedomosti, 22 Sep 2026). Crucially, on **8 Oct 2026 — the same day as the first strike — Mintsifry confirmed Yandex and VK are forming a cloud "giant" expected to capture ~a third of the market** (cnews). So handing clients specifically to VK Cloud is not purely emergency improvisation; it rides on an already-forming alliance.

**Why the company acts this way:** Yandex's structural bet is AI/enterprise cloud scale. A multi-day unrecoverable outage directly threatens the trust that enterprise cloud sells. Routing clients to partners (especially its prospective merger partner VK) is damage-control to prevent churn to Cloud.ru and to preserve the "we keep you running no matter what" narrative underpinning the AI land-grab.

## [3] Novelty / value-add / traction
Genuinely novel: **a provider orchestrating customer exodus to direct competitors as a formalized, multi-party program** is rare globally and effectively unprecedented in the RU market at this scale. Traction is real and live (not announced-only): the agreements are operational, with named partners and active teams. But the "value-add" is defensive, not a new capability — it is DR-as-necessity.

**Why it matters, deeper:** The margin question inverts. Normally the cloud captures lock-in margin. Here the strike **broke lock-in**: once a client's stack is live on Selectel/VK, switching cost to return is a reason to stay. So Yandex's gesture risks permanent share leakage. Whoever absorbs the workloads captures the recurring margin. Second order: this reprices "sovereign cloud" — domestic concentration (99% local) was framed as resilience against sanctions, but it created physical single-points-of-failure now exposed to drones.

## [4] What's next / market sentiment
- Watch Sasovo recoverability (possibly a total write-off) and whether Kaluga's AI supercomputers were damaged — material to Yandex's AI roadmap.
- Expect a push toward **geographic/zone redundancy, hardened/underground DCs, and cross-provider mutual-aid frameworks** across RU cloud; likely regulatory pressure (Mintsifry) for it.
- The Yandex–VK cloud consolidation (announced 8 Oct) will be read partly through this lens: scale + redundancy as war-resilience.
- Sentiment risk: enterprise buyers may diversify multi-cloud domestically, eroding any single leader's ~24–30% share.

**Counterintuitive second order:** The "sovereign, all-domestic" cloud posture that looked like strength is now a concentration liability — making the market's resilience story fragile precisely because it is self-contained and geographically clustered in strike range.

## Sources
- vc.ru (primary note link); themoscowtimes.com; theregister.com; cnbc.com; nbcnews.com; united24media.com; gigazine.net
- RU trade press: ixbt.com; anti-malware.ru; vz.ru; abn.agency; profile.ru; kod.ru; comss.ru; vbr.ru; lenta.ru; ura.news; tks.ru; fontanka.ru
- Market: tadviser.com; vedomosti.ru; market.cnews.ru (Yandex+VK consolidation)
- Internal: [[MWS Cloud launches fastest S3 storage for ML workloads]]; [[AWS outage disrupts UK banks' online services]]; [[Yandex NewPay added to Russian installment-services registry]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions (second-order)

1. **Is this a product/goodwill move or forced DR?** Forced. Yandex only hands clients to VK Cloud/Selectel/K2Cloud because two of its DCs (Sasovo, Kaluga) were physically disabled by drone strikes 7–9 Oct 2026 and it cannot serve the affected zones itself. (sourced)

2. **Why did the note's RU framing say "power outage" first?** Yandex initially downplayed it as a power cut before the drone-attack cause surfaced in media (Lenta.ru) — PR softening of a war-damage event. (sourced)

3. **Is Sasovo recoverable?** Open — as of 8 Oct Yandex could not confirm equipment recovery; plausibly a total loss. Material to the story's weight. (open)

4. **Were AI-training supercomputers hit at Kaluga?** Reported as possible (GIGAZINE, united24media), not confirmed by Yandex. If true, raises importance for Yandex's AI roadmap. (open/plausible)

5. **Why these three rivals and not market leader Cloud.ru?** Open — Cloud.ru (29.7% IaaS) is absent. Possible trust/coordination gap or simply not approached; notable because VK is Yandex's prospective merger partner. (open + sourced on VK link)

6. **Does the migration permanently leak share?** Likely. Once workloads are live elsewhere, re-migration cost discourages return — the strike broke Yandex's lock-in. (analysis)

7. **Who captures the recurring margin?** Whoever hosts the refugee workloads (VK/Selectel/K2Cloud). Yandex gives up near-term margin to preserve trust. (analysis)

8. **Was this state-coordinated?** Likely — Mintsifry is active in RU cloud policy and announced a Yandex–VK cloud consolidation the same day (8 Oct). Cross-provider mutual aid under war fits a coordinated response. (hypothesis, sourced on Mintsifry announcement)

9. **Is the "helping clients migrate" framing live or announced?** Live/operational — named partners, dedicated teams, active onboarding, not a press-release aspiration. (sourced)

10. **Does this reprice "sovereign cloud"?** Yes — 99% domestic concentration, geographically clustered in drone range, converts the resilience narrative into a physical single-point-of-failure liability. (analysis)

11. **Fintech relevance?** Indirect but real — RU banks/fintechs run on these domestic clouds; the outage hit online services broadly (RBC etc.). Infrastructure risk is systemic to RU fintech. (sourced)

12. **Precise mechanism delta vs a normal outage response?** A provider formally orchestrating customer exodus TO direct competitors (vs internal failover) is the unusual move — effectively unprecedented at this scale in RU. (analysis)

13. **What are "flexible financial terms"?** Undisclosed — who eats the cost (Yandex, partners, clients)? Silent point. (open)

14. **Duplicate check — is the drone attack itself covered?** No separate note in corpus covers the 7–9 Oct 2026 Yandex DC strikes or this migration agreement; this is the only note on the event. (sourced via grep)

15. **What breaks the bull case for RU cloud?** Repeat kinetic strikes on clustered DCs; share fragmentation as enterprises go multi-domestic-cloud for redundancy. (analysis)

## Freshness / duplicate verdict
**FRESH.** No prior corpus note covers these 7–9 Oct 2026 drone strikes on Yandex DCs or the VK Cloud/Selectel/K2Cloud migration agreement. Adjacent notes are thematically related but distinct events: [[MWS Cloud launches fastest S3 storage for ML workloads]] (different company/product), [[AWS outage disrupts UK banks' online services]] (2025, different provider/region), [[Yandex NewPay added to Russian installment-services registry]] (Yandex but BNPL, unrelated). This is a new, dated, materially distinct development.

Importance: 4/5 — A war-driven, materially damaging, multi-day outage of Russia's #1 broad-market cloud, with the genuinely unusual (near-unprecedented) move of formally migrating clients to direct rivals, landing the same day as a Yandex–VK cloud consolidation. High novelty and real, live traction; systemic infrastructure risk for RU fintech. Not a 5 only because the direct fintech payload is indirect and some key facts (Sasovo recoverability, AI-supercomputer damage, cost-bearer) remain open.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian public-cloud infrastructure (IaaS+PaaS) reached ~RUB 227bn in 2025, +36.7% YoY (per TAdviser, as of end-2025); the pure-IaaS slice is ~RUB 96bn and ~80%+ of volume (per Apple Hills Digital, via Telecompaper). The market is a closed, import-substituted system: domestic providers hold ~99% of revenue after foreign hyperscalers (AWS/Azure/GCP) exited (per TAdviser). "Why now": the triggering event is not a routine ops glitch but a **Ukrainian drone strike** that hit Yandex's Sasovo data center (Oct 7-8) and a Kaluga facility (Oct 9), knocking out tens of thousands of servers incl. two A100 supercomputers (per Tom's Hardware, CNBC, Kyiv Independent) — the note's neutral phrase "incidents in data centers" de-PRs to a wartime physical-infrastructure attack. Secular driver underneath: AI-load growth (>80% of firms cite AI's effect on consumption) plus mandatory data-residency pushing workloads onto RU rails. Structure: fragmented at the top (5+ scaled players) but each is captive to domestic demand with no external competition.

**Competitive landscape.** Sector KPIs: IaaS/PaaS revenue, external-consumption share, enterprise-customer count/growth, EBITDA margin. Key players and basis of competition (scale + data residency + breadth of managed/PaaS/AI services, not price): **Cloud.ru** (ex-SberCloud) is the largest provider — IaaS share 29.7%, PaaS 44.6%, FY2025 revenue RUB 76.5bn (+50%), EBITDA RUB 58bn (76% margin), net profit RUB 14.7bn (+86%), AI/infra now 54% of revenue (per cloud.ru, Vedomosti). **Yandex Cloud** leads overall public-cloud share at ~24% but is #2 in PaaS at 26.8% behind Cloud.ru's 44.6% (per TAdviser); FY2025 revenue RUB 27.6bn (+39%), ~93% external consumption. **VK Cloud, Selectel, K2Cloud** are the three peers Yandex routed affected clients to (per www1.ru, Oct 9). Recent move: Yandex's own outage-driven migration pact (Oct 9, 2026). Protagonist position: revenue leader by public-cloud share but materially smaller in absolute cloud revenue than Cloud.ru (RUB 27.6bn vs 76.5bn), and now demonstrably exposed on physical resilience — catching-up on durability, not ahead `(analysis)`. Moat: scale + integrated AI stack + switching costs, but this event shows the moat does not cover single-site physical risk.

**Comps & multiples.** Internal comps (RU cloud infra, in-base): [[MWS Cloud launches fastest S3 storage for ML workloads]], [[MWS Cloud deploys GLM-5.2 on its own infrastructure]], [[Russian State Library automates processes with MWS AI platform]] — MWS (MTS) is a fourth scaled RU-cloud peer; corpus notes cite RU corporate cloud-penetration of only ~15-20% (runway, not maturity). External comps (private; no public market caps — IPO valuations "no data"):
- Cloud.ru: FY2025 rev RUB 76.5bn, EBITDA RUB 58bn → EBITDA margin = 58 / 76.5 = 75.8% (per cloud.ru).
- Yandex Cloud: FY2025 rev RUB 27.6bn (+39%); standalone EBITDA not disclosed. Parent B2B Tech segment (Yandex Cloud + Yandex 360): rev RUB 48.2bn (+48%), adj EBITDA RUB 9.4bn → segment adj-EBITDA margin = 9.4 / 48.2 = 19.5% (per akm.ru/Telecompaper). Note Yandex Cloud ≈57% of the B2B Tech segment (27.6 / 48.2).
- Parent Yandex FY2025: rev RUB 1.44tn (+32%), adj EBITDA RUB 280.8bn → cloud is ~1.9% of group revenue (27.6 / 1440), so an outage is reputationally/strategically bad but not financially material to the parent.
EV/Revenue and EV/EBITDA for the cloud units = **no data** (all private, no verifiable EV). Qualitative flag: Cloud.ru's ~76% EBITDA margin vs the B2B Tech blended ~20% suggests Cloud.ru is the profitability outlier of the RU cloud set — distribution not computed (fewer than 3 comparable EBITDA figures).

**Risk flags.**
1. **Single-site / physical-war risk (concentration).** The outage was a kinetic strike, not a config error; one lost site (Sasovo) cascaded across Mail, Disk, Pay, Market plus enterprise clients (RZD, Cian, 1C). Second-order: war-risk becomes a permanent discount on RU cloud reliability and may force costly geo-redundancy that compresses margins.
2. **Disintermediation / self-inflicted churn.** By actively migrating clients to VK Cloud, Selectel and K2Cloud, Yandex hands competitors warm, qualified enterprise leads with simplified onboarding and flexible terms. Second-order: switching costs cut both ways — once migrated and stable on a rival, many clients may not return, permanently shifting the ~24% share.
3. **Resilience-trust re-rating across the sector.** Buyers now price physical-security and multi-region failover into provider selection, favoring players marketing redundancy; providers unable to prove it risk losing regulated/critical-infra accounts. Second-order: potential consolidation toward the best-capitalized (Cloud.ru/Sber, MTS/MWS) who can fund more sites.

**What this changes (idea-lens).** `(analysis)` This is a durability shock that can trigger a share re-shuffle, not a one-day blip: watch whether Yandex's public-cloud share erodes below ~24% in the next 1-2 quarters as migrated clients stick with VK/Selectel/K2 — that is the falsifiable trigger. Thesis: the RU cloud market re-rates on physical resilience, advantaging multi-site, well-capitalized players (Cloud.ru, MWS) and accelerating multi-cloud adoption by RU enterprises. What would break it: Yandex fully restores Sasovo quickly and recaptures migrated clients, proving switching friction still favors the incumbent.

Sources: https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russias-yandex-data-centers-housing-two-top-supercomputers-major-outage-follows-retaliatory-strike · https://www1.ru/en/news/2026/10/09/posle-atak-na-data-centry-iandeks-dogovorilsia-s-konkurentami-o-perenose-servisov-klientov.html · https://www.cnbc.com/2026/10/08/russia-yandex-ukraine-drone-strike-data-center.html · https://tadviser.com/index.php/Article:Cloud_services_(Russian_market) · https://www.telecompaper.com/news/russian-public-cloud-infrastructure-market-forecast-to-triple-by-2030--1578982 · https://cloud.ru/blog/vyruchka-cloud-ru-2025-prevysila-76-mlrd-rubley · https://www.akm.ru/eng/news/revenue-of-yandex-b2b-tech-according-to-ifrs-in-2025-in-two-key-areas-increased-by-48/ · IR: Yandex Q4 2025 & FY2025 Press Release (ENG) https://yastatic.net/s3/ir-docs/docs/2025/q4/fc756ee95baa6fa171ee77ac733d52be/4Q25_YDEX_Press_Release_ENG_short_6ee9.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** NO EARNINGS EVENT in this news — it's an operational/reputational story (Yandex Cloud arranging accelerated migrations, including to direct competitors, for clients hit by its own datacenter incidents). No results were reported with the item. Financial context comes from Yandex's most recent *reported* print: **Yandex B2B Tech H1 2026** (reported 2026-08-12), the segment that houses Yandex Cloud. On those numbers the business is still scaling fast — segment revenue RUB 28.9bn (+32% YoY), Cloud revenue RUB 16.7bn (+30% YoY) — so the outage episode is a reputational/retention risk layered on top of a still-growing franchise, not a visible revenue dent yet (the incident post-dates the last report).

**Key figures (Yandex B2B Tech, H1 2026, reported 2026-08-12).**
- Group (B2B Tech) revenue: **RUB 28.9bn, +32% YoY**.
- Adjusted EBITDA: **RUB 6.4bn, +45% YoY** — EBITDA growing faster than revenue → operating leverage / margin expansion (adj. EBITDA margin ~22%).
- **Yandex Cloud revenue: RUB 16.7bn, +30% YoY** — the larger of the two sub-units; growth cited as ~1.6x the Russian corporate-IT market.
- Yandex 360 (virtual office) revenue: **RUB 11.6bn, +42% YoY**; MAU >117mn (+26% YoY).

**By segment / driver.** Cloud (~58% of B2B Tech revenue) is the slower grower of the two (+30% vs 360's +42%) but the bigger absolute base. Cloud client base reached **64,000 accounts** (growth cited at +64% YoY in the H1 release; an earlier figure of +36% appears in other coverage — [UNSOURCED] discrepancy, use with caution). Stated growth drivers: information-security services and AI services — AI MRR cited up ~1.8x YoY by June 2026, with Q2 2026 enterprise AI-token consumption exceeding all of FY2025. Mix skews enterprise: large enterprises ~50% of cloud consumption, mid-market ~29%, SMB/mass ~21%; ~83% of consumption from banking/fintech, retail and IT clients — i.e. the very clients most sensitive to downtime, which is what makes this outage/migration story thesis-relevant.

**vs expectations / prior period.** No public sell-side consensus for Yandex B2B Tech (unlisted sub-group; reports stand-alone) → beat/miss assessed qualitatively vs prior year only. H1 revenue +32% and EBITDA +45% are both strong vs the prior-year base; no sign of deceleration in the last report. The migration episode itself contributes **no reported figures** — any revenue/churn impact would first surface in H2 2026 results (not yet published).

**Guidance / forward.** No formal quantitative guidance is given for the B2B Tech sub-group; management framing is qualitative ("growing 1.6x the Russian corporate-IT market", AI as the key accelerator). Independent read (analysis): if the migration/outage episode drives measurable enterprise churn — and enterprises are ~50% of consumption — H2 2026 Cloud growth could decelerate from the +30% H1 pace; watch the client-count line and Cloud revenue growth in the next B2B Tech release as the first hard read on retention.

**Thesis-flags.**
1. *Reputation vs. retention (de-PR).* Helping clients migrate to rivals is PR-positive ("we did right by customers") but signals real service-reliability damage after datacenter incidents → second-order: enterprise clients (~50% of consumption, heavily banking/fintech) are exactly the cohort with the lowest tolerance for downtime and the resources to multi-cloud away.
2. *Growth still intact as of last print.* +30% Cloud / +32% B2B Tech with +45% EBITDA means the franchise entered this episode from strength; the outage is a risk to the *forward* curve, not something visible in reported numbers yet.
3. *AI as the offsetting engine.* Security + AI services are the stated growth drivers (AI MRR ~1.8x YoY); if these keep compounding they can mask churn at the infra layer — watch whether Cloud revenue growth holds while client count softens.
4. *Opacity flag.* B2B Tech reports semi-annually and without external consensus; limited visibility means the migration impact won't be independently verifiable until the next H2/FY release.

Sources: Yandex B2B Tech H1 2026 results (reported 2026-08-12) · https://www.telecompaper.com/news/yandex-b2b-tech-revenues-rise-32-in-h1--1579958 · https://rb.ru/news/yandex-b2b-tech-raskryl-finansovye-itogi-za-i-polugodie-2026-goda-vyruchka-gruppy-dostigla-289-mlrd/ · https://www.cnews.ru/news/line/2026-08-12_yandex_b2b_tech_obyavlyaet_finansovye · noah-news.com (AI-token usage, Q2 2026) · IR latest filing: Yandex Q1 2026 press release https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf (group-level only; Cloud not broken out — PDF not machine-readable). No public consensus for B2B Tech sub-group → beat/miss qualitative vs prior year. Client-growth figure +64% vs +36% — [UNSOURCED] discrepancy across coverage.
<!-- /enrichment:earnings_review -->
