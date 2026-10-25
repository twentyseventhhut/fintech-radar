---
title: "Yandex nearly fully restores Yandex Cloud client data access"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/yandex
  - industry/infrastructure
  - region/ru
  - type/outage-security
sources:
  - https://www.vedomosti.ru/technology/news/2026/10/23/1239733-yandeks-vosstanovil
status: published
n_mentions: 1
channels:
  - "42 секунды"
story_id: s5ea44677
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Yandex nearly fully restores Yandex Cloud client data access

> [!info] 2026-10-23 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Ведомости: Яндекс почти полностью восстановил доступ к данным клиентов Yandex Cloud

## Первоисточники

### vedomosti.ru
<https://www.vedomosti.ru/technology/news/2026/10/23/1239733-yandeks-vosstanovil>
*230 слов · direct*

Выбор редакции 
 Выборы в Госдуму: каким был и будет российский парламент 
 Лига Ставок Media Basket: что важно знать о восьмом сезоне 
 Ситуация на топливном рынке: меры, динамика, прогнозы 
 Война на Ближнем Востоке: операция Израиля и США против Ирана 
Инженеры Yandex Cloud восстановили доступ к 90,47% данных клиентов, хранившихся на облачной платформе, после атак на дата-центры «Яндекса». Об этом сообщили в компании.
Часть данных и связанных с ними сервисов перенесли в новую локацию, которая заработала 23 октября. Доступ к ним будет открываться поэтапно в ближайшие дни. О восстановлении доступа клиентов уведомят через рассылку.
Пользователям Yandex Cloud уже доступны основные возможности платформы. Они могут создавать виртуальные машины и базы данных, управлять кластерами Kubernetes, пользоваться инструментами бизнес-аналитики и сервисами защиты от киберугроз. Также возобновлена возможность применять инструменты Yandex AI Studio для работы с искусственным интеллектом.
14 октября Yandex Cloud сообщила о восстановлении работы части корпоративных ИИ-сервисов. Тогда отдельные функции платформы оставались недоступными или работали с ограничениями.
13 октября «Яндекс» отменил плату за использование Yandex Cloud и «Яндекс 360» для действующих клиентов на фоне масштабных сбоев. В компании объяснили, что часть функций была намеренно ограничена для поддержания работоспособности основных сервисов.
Сбои произошли после атак беспилотников на три дата-центра «Яндекса». 8 октября пострадал объект в Сасове Рязанской области, 9 октября – в Калуге. 11 октября БПЛА атаковали дата-центр во Владимире, в результате чего его работа была полностью остановлена. Платформа Yandex Cloud перешла в аварийный режим.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Yandex nearly fully restores Yandex Cloud client data access
_Analytical notes (not a post). Importance: 2/5._

> **Freshness note:** This is the latest recovery-status milestone in the Oct 2026 Yandex data-center drone-strike saga already enriched across [[Yandex Cloud helps clients migrate to rival providers after outages]] (2026-10-09, imp. 4), [[Yandex Pay still down after Yandex data-center outages]] (2026-10-12, imp. 3) and [[RBK Yandex keeps AI plans despite data-center attacks]] (2026-10-20, imp. 3). FRESH — but narrowly: the only genuinely NEW, dated facts are the **90.47% data-access figure**, a **newly-launched replacement location live 23 Oct**, and Yandex AI Studio being back. The root event, cause, DC list and competitor-migration pact are all already booked. See challenge for the verdict.

## [0] What exactly happened (de-PR'd)
On 23 Oct 2026 Yandex said engineers restored access to **90.47% of client data** that sat on Yandex Cloud before the drone strikes, and launched **a new location** (a replacement availability zone) that went live the same day; access will reopen **gradually "in the coming days,"** with clients notified by email (Vedomosti, ixbt, Habr, 1prime, comss — all 23 Oct).

- Core platform functions are back: create VMs and databases, manage Kubernetes clusters, use BI tools and cyber-threat-protection services, and — newly re-enabled — **Yandex AI Studio** for AI work.
- This continues the published recovery ladder: **14 Oct** — part of corporate AI services restored (prior note confirms Alice AI / smart-speaker / YaOS functions on the same date); **13 Oct** — Yandex waived Cloud + Yandex 360 fees for existing clients during the outage (the note dates the fee-waiver to 13 Oct; [[RBK Yandex keeps AI plans despite data-center attacks]] cited an 8–31 Oct waiver window — minor framing difference, not a conflict).
- Cause (re-stated, not new): drone strikes on three DCs — **Sasovo (Ryazan), night of 7–8 Oct** (fire, site stopped); **Kaluga, 9 Oct** (modules disabled); **Vladimir, 11 Oct** (full shutdown, Yandex Cloud entered emergency mode).

**Why framed this way / what it reveals:** The headline metric is the tell. A **90.47%** figure is precise enough to sound like an engineering readout, but it is really a **de-PR'd admission that ~9.53% of client data is NOT yet accessible** (status of the remainder — recoverable, delayed, or lost — is unstated). "A new location went live" is the substantive news under the reassurance: Yandex did not restore the destroyed Vladimir/Sasovo zones, it **stood up fresh replacement capacity and is re-homing data onto it** — confirming the prior-note read that the struck sites were a (partial) write-off and that recovery = rebuild, not repair. The "90.47% + core functions back + AI Studio" bundle is confidence-signalling two weeks into a war-damage incident, consistent with the Masyuk "AI plans unchanged" messaging of 20 Oct ([[RBK Yandex keeps AI plans despite data-center attacks]]).

## [1] Competitors / peers
Unchanged from the sibling notes. The relevant peers remain **Cloud.ru (ex-SberCloud)** — RU IaaS leader (~29.7% IaaS share), conspicuously still absent from Yandex's rescue pact; and **VK Cloud, Selectel, K2Cloud** — the three providers that took Yandex's refugee workloads on 9 Oct ([[Yandex Cloud helps clients migrate to rival providers after outages]]). **MWS Cloud (MTS)** is the fourth scaled peer. Western hyperscalers are irrelevant in RU (~1% share).

**Why it matters / second-order:** The 90.47%-restored message is partly a **re-capture play** against exactly those three partners. Having pushed clients onto VK/Selectel/K2Cloud under duress, Yandex now needs to prove the home platform is safe again before switching costs calcify elsewhere — the strike broke lock-in, and every day of degraded service lets a migrated enterprise decide to stay put. The new-location launch is the earliest credible "come back, we're resilient now" signal. Open question: does 90.47% + a single new zone actually restore the geographic redundancy enterprises will now demand, or is it the same clustered-DC risk re-concentrated?

## [2] Company history / fit
Yandex Cloud sits in **Yandex B2B Tech** (H1 2026 segment revenue RUB 28.9bn, +32% YoY; Cloud revenue RUB 16.7bn, +30% YoY; ~64k cloud accounts; ~83% of consumption from banking/fintech, retail and IT) — the franchise's fastest-scaling, most downtime-sensitive customer base. The group's stated strategy is AI/enterprise-cloud scale, reaffirmed mid-crisis ([[RBK Yandex keeps AI plans despite data-center attacks]]).

**Why the company acts this way:** Enterprise cloud sells trust and always-on availability. A precise public recovery metric + fresh replacement capacity is pure retention engineering: Yandex must convert a war-damage narrative ("железное сердце" hit) back into a reliability narrative fast, because its ~24% public-cloud lead and the pending Yandex–VK cloud consolidation both rest on enterprises believing the platform is durable. Restoring AI Studio specifically protects the AI-monetization story (AI Studio token consumption was the headline growth proof in the Q2 2026 print).

## [3] Novelty / value-add / traction
Low novelty. This is an **incident-recovery status update**, not a product or a new development. Its only informational value-add over the three prior enriched notes: (a) the **quantified 90.47%** data-access figure; (b) a **new replacement location live 23 Oct**; (c) **AI Studio** explicitly back. Traction is real/live (not announced) — these are operational facts, not promises — but the "value-add" is defensive recovery, not a capability.

**Why it matters, deeper:** The durable lesson, already established in [[Yandex Pay still down after Yandex data-center outages]], holds: **data durability (geo-replicated records) survived; service availability did not.** 90.47% restored two weeks on quantifies how long "availability recovery via rebuild" actually takes when the failure mode is a destroyed building rather than a config error — and it validates the ~6-month equipment-replacement estimate circulating in RU press (Kommersant via Moscow Times/UBN): the "new location" is a stopgap, full hardware replacement is a multi-quarter capex overhang. Second order: whoever ends up hosting the un-restored ~9.53% and the migrated workloads captures that recurring margin.

## [4] What's next / market sentiment
- Watch the **tail**: what is the status of the remaining ~9.53% (delayed vs permanently lost), and the actual timeline for full access reopening.
- Watch for a **post-mortem / compensation** and any **CB RF / Mintsifry operational-resilience** follow-up; Mintsifry (Shadaev) already called the attacks "unprecedented" and helped migrate systems, and MinFin said (19 Oct) Yandex had made no support requests ([[RBK Yandex keeps AI plans despite data-center attacks]]).
- Expect the **geo-redundancy / distributed-infra** push to become a concrete, capex-heavy program — the binding constraint is now physical resilience + hardware lead times, not demand.
- Sentiment: the quantified-recovery message is designed to stem churn to VK/Selectel/K2Cloud and Cloud.ru; the falsifiable test is whether Yandex's ~24% public-cloud share holds through Q4 2026.

**Counterintuitive second order:** Publishing a precise 90.47% reassures, but it simultaneously timestamps that a war strike can keep ~10% of a national cloud leader's client data inaccessible for 2+ weeks — permanently repricing "sovereign, all-domestic cloud" from a resilience story into a clustered-physical-single-point-of-failure liability.

## Sources
- Vedomosti (primary): https://www.vedomosti.ru/technology/news/2026/10/23/1239733-yandeks-vosstanovil
- ixbt (new location + 90.47%): https://www.ixbt.com/news/2026/10/23/yandex-cloud-zapustil-novuiu-ploshhadku-i-vosstanovil-dostup-k-9047-dannyx.html
- Habr: https://habr.com/ru/news/1098646/
- 1prime: https://1prime.ru/20261023/jandeks-874574087.html
- comss: https://www.comss.ru/page.php?id=22566
- Fortune (three DCs / AI race, 22 Oct): https://fortune.com/2026/10/22/ukraine-russia-drones-data-centers-ai-race
- UBN (~6-month equipment recovery): https://ubn.news/yandex-faces-six-month-equipment-recovery-after-drone-strikes/
- The Moscow Times (govt helped migrate, 14 Oct): https://www.themoscowtimes.com/2026/10/14/government-says-it-helped-yandex-migrate-systems-after-data-center-attacks-a93979
- Al Jazeera (Vladimir shutdown, 11 Oct): https://www.aljazeera.com/news/2026/10/11/russias-yandex-says-data-centre-in-vladimir-shut-down-after-drone-attack
- Internal: [[Yandex Cloud helps clients migrate to rival providers after outages]]; [[Yandex Pay still down after Yandex data-center outages]]; [[RBK Yandex keeps AI plans despite data-center attacks]]; [[Yandex NewPay added to Russian installment-services registry]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions (second-order)

1. **Is this a new event or a duplicate of the outage chain?** FRESH but narrowly. The root event (Oct 2026 drone strikes on three Yandex DCs) and the competitor-migration pact are already enriched in [[Yandex Cloud helps clients migrate to rival providers after outages]], [[Yandex Pay still down after Yandex data-center outages]] and [[RBK Yandex keeps AI plans despite data-center attacks]]. The only NEW, dated facts here: the **90.47% data-access** figure, a **new replacement location live 23 Oct**, and AI Studio being back. It is the next recovery milestone, not a reprint. (sourced)

2. **What does 90.47% actually mean — restored or lost?** Restored = *accessible again*. The de-PR'd flip side: ~9.53% of client data is still NOT accessible, and Yandex did not state whether it is delayed-but-recoverable or permanently lost. A material silence. (open)

3. **Restore via repair or rebuild?** Rebuild. Yandex launched a NEW location and is re-homing data onto it — it did not resurrect the destroyed Sasovo/Vladimir zones. Confirms the struck sites were a (partial) write-off. (sourced)

4. **Does "new location" restore geographic redundancy?** Open. One new zone could simply re-concentrate the same clustered-DC risk enterprises will now demand be eliminated. No site count/geography disclosed. (open)

5. **Is AI Studio restoration substantive or PR?** Substantive-adjacent but signalling-heavy: re-enabling AI Studio directly protects the AI-monetization narrative (AI Studio token consumption was the Q2 2026 growth proof), landing days after the 20 Oct "AI plans unchanged" message. (analysis + sourced)

6. **Announced or live?** Live/operational — these are recovery facts (functions usable, location running), not promises. The "access reopens gradually in coming days" part is forward-looking. (sourced)

7. **Fee-waiver date conflict?** Minor: this note dates the Cloud/Yandex 360 fee waiver to 13 Oct; [[RBK Yandex keeps AI plans despite data-center attacks]] cited an 8–31 Oct window. Framing difference, not a substantive conflict. (flagged)

8. **Does a quantified-recovery message stem or accelerate churn?** It is a re-capture play against VK Cloud/Selectel/K2Cloud (who took the refugee workloads) and Cloud.ru. But switching costs cut both ways — migrated enterprises now stable elsewhere may not return; 90.47% + one new zone may not beat a rival's running stack. (analysis)

9. **Full-recovery timeline?** None given for the data tail. RU press (Kommersant via Moscow Times/UBN) floats **~6 months** to replace damaged equipment — a multi-quarter capex overhang; the new location is a stopgap. (sourced, external estimate)

10. **Regulator / state follow-up?** Open. Mintsifry (Shadaev) called the attacks "unprecedented" and helped migrate systems; MinFin (19 Oct) said no Yandex support request; no CB RF operational-resilience action on record. (open, prior-note sourced)

11. **Financial impact visible yet?** No — incident post-dates the last print (Q2 2026). Cloud is ~1.9% of group revenue, so this is reputational/retention risk, not a near-term P&L dent; watch Q3/Q4 B2B Tech client count + Cloud growth. (analysis)

12. **Single-source fragility of the note?** The note carries one channel (42 секунды / Vedomosti, 230 words direct) but the 90.47% + new-location facts are independently corroborated by ixbt, Habr, 1prime and comss (all 23 Oct). Well-corroborated. (sourced)

13. **Precise mechanism delta vs a normal outage recovery?** The recovery is a *rebuild onto new capacity after physical destruction of buildings*, not failover/repair — the same unusual, near-unprecedented-at-scale property as the rest of this incident. (analysis)

14. **Does this change the central question?** No — it confirms the already-established one: durability (geo-replicated records) survived, availability did not, and availability recovery via rebuild is slow (90.47% at ~2 weeks). It adds a data point, not a new thesis. (analysis)

15. **What would push importance up?** If the remaining ~9.53% turns out to be permanently lost, or if a record-integrity problem surfaces contradicting the "no record lost" claim, or if CB RF/Mintsifry opens a formal resilience inquiry, or if Q4 share data shows real churn to rivals. (analysis)

## Freshness / duplicate verdict
**FRESH** (with a strong dedup caveat). Same underlying event as three already-published, higher-importance notes. NOT a duplicate because it carries materially new, dated content: the 90.47% data-access figure, the new replacement location live 23 Oct, and AI Studio restored. It is an incremental recovery-milestone update, and if the digest publishes it, it should be framed explicitly as the "recovery progress" slice to avoid reader-level duplication with the earlier outage notes.

**Importance: 2/5 — rationale:** A dated, well-corroborated recovery milestone of Russia's #1 broad-market cloud two weeks after a war strike, with one genuinely useful de-PR'd number (90.47% access = ~9.53% still inaccessible, status unstated) and the substantive detail that recovery = rebuild onto a new location. Held at 2 (not 3+) because the systemic weight — war-concentration risk, competitor-migration pact, payments angle, AI-plans messaging — is already booked across [[Yandex Cloud helps clients migrate to rival providers after outages]] (4), [[Yandex Pay still down after Yandex data-center outages]] (3) and [[RBK Yandex keeps AI plans despite data-center attacks]] (3); this is the fourth touch of the same story with only an incremental status delta, no new entities, deals or figures that reframe anything. Above 1 because the quantified recovery + rebuild-not-repair confirmation is concrete, decision-relevant information.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-25]] (2026-10-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian public-cloud services market ≈ RUB 416.5bn in 2025, +32.8% YoY (per iKS-Consulting, via Mordor/TAdviser citations, as of 2025); 99% of demand now sits with domestic providers after Western hyperscalers (AWS/Azure/GCP) exited post-2022. Why now: sanctions + a data-localisation mandate make import-substituted clouds the only compliant option, so sector growth is policy-driven rather than purely demand-driven (fact → forced domestic sourcing → tight supplier set → systemic concentration risk, see below). Structure: consolidating around a few scaled players with capital/datacentre barriers — Cloud.ru (Sber-owned) led IaaS at ~29.7% share in 2025, with Yandex Cloud, VK Cloud, Selectel, MTS/MWS and MegaFon trailing. The new, war-specific driver: physical datacentre vulnerability — Ukrainian drone strikes on 8–11 Oct 2026 hit three Yandex DCs (Sasovo, Kaluga, Vladimir), knocking the ru-central1-a availability zone offline and dropping Yandex Cloud network connectivity to ~30% of normal (per NetBlocks, via The Register, 2026-10-12).

**Competitive landscape.** Sector KPIs: cloud revenue growth, client count, share of revenue from mid/large enterprise, and — newly salient — availability-zone redundancy / RTO. Players & basis of competition: Cloud.ru (scale + Sber distribution), Yandex Cloud (product breadth: VMs, managed Kubernetes, BI, AI Studio), VK Cloud, Selectel, MTS MWS. Competition historically on product/price; this incident shifts it toward physical resilience and multi-AZ guarantees. Recent dated moves: Yandex Cloud revenue +39% to RUB 27.6bn in FY2025 with ~51,000 clients (+17%), 84% of revenue from mid/large business, 93% from external customers (per Yandex Cloud 2025 report); 1H2026 cloud revenue +30% to RUB 16.7bn, >64,000 clients. Protagonist position: #2–3 by share but growing fast; the 2026-10-23 restoration of 90.47% of client data (with a new location live and phased re-opening) is damage-control, not an advance. Moat `(analysis)`: switching costs + integrated AI stack, but the outage actively erodes it — [[Yandex Cloud helps clients migrate to rival providers after outages]] shows Yandex itself assisting churn to competitors.

**Comps & multiples.** Internal comps (base): [[Sber confirms drone attack on Saratov data center]] — same drone-on-DC risk hitting the #1 cloud rival Cloud.ru's parent days later; [[Yandex Pay still down after Yandex data-center outages]] — the fintech blast radius of the same event; [[Yandex Cloud helps clients migrate to rival providers after outages]] — quantifies churn risk; [[EU regulators question Google over London cloud outage]] — cloud-outage governance precedent in a Western market. External valuation multiple: Yandex (MOEX: YDEX) is public but a clean EV/Revenue is not computable here — EV requires net-debt + share count from the filing, not in-hand → `[UNSOURCED]`; using group revenue only is misleading since cloud is <2% of group revenue. **Arithmetic shown where possible:** Yandex Cloud FY2025 revenue RUB 27.6bn ÷ group FY2025 revenue (Q1'26 run-rate RUB 372.7bn ≈ RUB 1.2–1.3tn annualised) ≈ ~2% of group — i.e. the cloud outage is reputationally large but financially a small direct line for the group. Distribution not computed (no ≥3 comparable public cloud-pure-play multiples in-base); qualitative comparison only.

**Risk flags.**
1. **Physical infrastructure concentration / single-AZ dependence** — a single availability zone (ru-central1-a, Vladimir) being knockable offline shows thin geographic redundancy; second-order effect: enterprise clients demand multi-AZ SLAs Yandex may not yet guarantee, raising capex.
2. **Client churn / trust erosion** — 90.47% data restored still leaves ~9.5% inaccessible days later, and Yandex is actively helping clients migrate to rivals; second-order: permanent share loss to Cloud.ru/VK even after full restoration.
3. **Fintech dependency blast radius** — Yandex Pay and other payment rails went down with the DCs; second-order: regulated fintechs reassess single-provider reliance on Yandex Cloud, a systemic-concentration concern for the whole RU fintech stack.

**What this changes (idea-lens).** `(analysis)` The war has made physical DC resilience a first-order competitive variable in Russian cloud — expect a re-rating of providers toward multi-AZ/geo-redundancy and disaster-recovery as a paid product, and a possible consolidation of mission-critical workloads onto the largest, most-dispersed operator (Cloud.ru). Falsifiable thesis: Yandex Cloud's client count growth decelerates in 2H2026/FY2026 vs the +17–30% trend; trigger to watch — the FY2026 cloud revenue/client disclosure and any churn to Cloud.ru/VK. What breaks the thesis: fee waivers (13 Oct Yandex zeroed Yandex Cloud/360 charges) + fast restoration retain clients and growth holds.

Sources: https://tadviser.com/index.php/Article:Cloud_services_(Russian_market) · https://www.mordorintelligence.com/industry-reports/russia-data-center-market · https://yandex.cloud/en/blog/financial-results-2025 · https://www.telecompaper.com/news/yandex-b2b-tech-revenues-up-48-in-2025--1565113 · https://www.theregister.com/security/2026/10/12/ukrainian-drone-strikes-on-yandex-datacenters-knock-cloud-and-payments-offline/5302577 · https://www.tradingview.com/news/reuters.com,2026:newsml_S8N40B0AJ:0-yandex-reports-22-rise-in-q1-revenue-says-board-to-consider-share-buyback/ · https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** IN-LINE / modestly BEAT — but note this news item is an **outage-recovery report, not an earnings print**; there is no new Q3 2026 release yet (latest reported period is Q2/H1 2026, filed ~Aug 2026). Group H1 2026 revenue RUB 759bn (+19% YoY); Q2 2026 revenue RUB 386bn (~$4.89bn, +16% YoY), adj. EBITDA RUB 89bn (+35% YoY), adj. net profit RUB 48bn (+56% YoY). FY2026 guidance reaffirmed (~+20% revenue, ~RUB 350bn adj. EBITDA). The directly-affected unit — **Yandex B2B Tech / Yandex Cloud** — was a fast-growing but still sub-scale segment going into the outage.

**Key figures (with growth).**
- Group Q1 2026: revenue RUB 372.7bn (+22% YoY); adj. EBITDA RUB 73.3bn (+50% YoY); adj. net profit RUB 34.7bn (+2.7x YoY).
- Group Q2 2026: revenue RUB 386bn (+16% YoY); adj. EBITDA RUB 89bn (+35% YoY); adj. net profit RUB 48bn (+56% YoY).
- Group H1 2026: revenue RUB 759bn (+19% YoY).
- **Yandex B2B Tech (the segment carrying the outage) H1 2026: revenue RUB 28.9bn (+32% YoY); adj. EBITDA RUB 6.4bn (+45% YoY).**
- **Yandex Cloud H1 2026: revenue RUB 16.7bn (+30% YoY); ~64,000 customers (+64%), large enterprises the main users.**

**By segment / driver.** Group growth is still driven by Search/portal and e-commerce; B2B Tech is a small (~RUB 29bn of ~RUB 759bn H1, <4% of group revenue) but high-growth, now EBITDA-positive segment (margin ~22% in H1). Within it, Yandex Cloud (+30%) is the core, with Yandex 360 and AI/cybersecurity services the stated demand drivers. So the drone attacks (8–11 Oct) hit the group's smallest-revenue-but-highest-visibility growth bet, not its profit engine.

**vs expectations / prior period.** Q1 2026 (+22%) decelerated to Q2 (+16%), but EBITDA growth (+35–50%) ran well ahead of revenue — operating leverage intact. Public consensus for Q2 clustered around the reported figures (Reuters/Globalbanking: "16% rise … dividend recommended RUB 110/share") — call it broadly IN-LINE, no large beat/miss [public consensus, as of Q2 2026 release ~Jul/Aug 2026]. No in-base prior Yandex earnings note to wikilink.

**Guidance / forward.** FY2026 guidance **reaffirmed** at ~+20% revenue and ~RUB 350bn adj. EBITDA (set/maintained through Q2). CRITICAL: this guidance predates the October datacenter attacks. The Oct outage — three DCs hit (Sasovo 8 Oct, Kaluga 9 Oct, Vladimir 11 Oct fully halted), fees waived for Cloud + Yandex 360 clients (13 Oct), only 90.47% of client data restored by 23 Oct — is a direct hit to the Cloud/B2B segment that is NOT yet reflected in any guidance. Management has given no updated Cloud outlook; the Q3 2026 print (due ~late Oct/early Nov) will be the first to show outage impact. No data on the revenue/EBITDA cost of the fee waiver or data-loss liability — [UNSOURCED].

**Thesis-flags.**
1. *Resilience / churn risk (new).* 90.47% data restored ≠ 100%; residual ~9.5% loss + phased reopening → fact: enterprise clients (the segment's main users, +64% base) saw multi-week disruption → why it matters: cloud buying is trust-driven and sticky-but-losable → second-order: possible enterprise churn / slower new-logo adds just as Cloud was scaling (+30%), the exact opposite of the growth thesis.
2. *P&L hit is contained.* B2B Tech is <4% of group revenue and RUB 6.4bn H1 EBITDA; even a severe Cloud quarter is immaterial to group adj. EBITDA (~RUB 350bn guide) → the outage is a strategic/reputational risk to the growth story, not a group-level earnings risk.
3. *Fee waiver = margin drag in Q3.* Waiving Cloud + Yandex 360 fees for active clients directly compresses the segment's just-turned-positive EBITDA margin (~22%); watch whether B2B Tech EBITDA growth (+45% H1) stalls or reverses in Q3.
4. *Guidance credibility.* FY2026 reaffirm is now stale vs the Oct event; if management holds guidance at Q3 without addressing Cloud, that is a de-PR flag (touting group strength while silent on segment damage).

Sources: ir_latest.json[yandex] latest filing Yandex Q1 2026 Press Release (RUS), 2026-04-28 (https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf — PDF binary-encoded, figures cross-sourced below) · Reuters/AOL Q2 2026 (https://www.aol.com/articles/yandex-reports-16-increase-q2-060740000.html) · Globalbanking Q1 2026 (https://www.globalbankingandfinance.com/yandex-reports-22-rise-q1-revenue-board-consider-share/) · Telecompaper Yandex B2B Tech H1 2026 (https://www.telecompaper.com/news/yandex-b2b-tech-revenues-rise-32-in-h1--1579958) · T-Investments B2B Tech H1 2026 · outage facts from note (Vedomosti, 2026-10-23). Q3 2026 results: not yet published — no data. Fee-waiver cost / data-loss liability: [UNSOURCED].
<!-- /enrichment:earnings_review -->
