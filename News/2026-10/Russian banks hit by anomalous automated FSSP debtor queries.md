---
title: "Russian banks hit by anomalous automated FSSP debtor queries"
date: 2026-10-13
retrieved: 2026-10-13
tags:
  - industry/banking
  - industry/regtech
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sda8357af
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Russian banks hit by anomalous automated FSSP debtor queries

> [!info] 2026-10-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] У банков очередная проблема взаимодействия с ФССП. С 18 по 21 сентября банки без предварительного предупреждения получили аномальные массивы автоматизированных запросов ФССП о должниках. Речь идёт об информационных запросах, с помощью которых ФССП устанавливает имущественное положение должника. С декабря 2022 года это взаимодействие переведено в автоматический режим через СМЭВ, на ответ банку даётся три дня. По данным НСФР: ⚪️ Обычная нагрузка была превышена минимум в 10–12 раз, у отдельных банков — до 30 раз. ⚪️ АБР говорит о всплесках до 48 раз относительно обычного среднедневного уровня. ⚪️ Один региональный банк 19 сентября получил 12,8 млн запросов за сутки — примерно столько, сколько обычно получает за месяц. ⚪️ У большинства банков свыше 90% запросов относились к людям, которые вообще не были их клиентами. ⚪️ Запросы шли по всем регионам и категориям клиентов крупными массивами с минимальными интервалами, из-за чего в банковских системах образовывались очереди вызовов. Са

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Russian banks hit by anomalous automated FSSP debtor queries
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
Between **18–21 September 2026**, Russian banks received, with no prior warning, an anomalous flood of automated FSSP (Federal Bailiff Service) debtor-information queries sent over the SMEV state interop bus. These are the standard "establish the debtor's property position" queries that have run in **automatic mode since December 2022**, with a **statutory 3-day** window for the bank to answer.

Confirmed scale (sources: NSFR head Andrey Emelin via Kommersant; ABR):
- Normal daily load exceeded **≥10–12x**, some banks up to **30x**, with single-day peaks up to **48x** (ABR).
- One regional bank got **12.8 million queries on 19 Sept alone** — roughly its usual monthly volume.
- One large bank got **~22 million queries over the four days**.
- **>90% of queries at most banks concerned people who were not their clients** — i.e. blanket fan-out, not targeted lookups.
- Queries arrived across all regions/client categories in large batches at minimal intervals → call queues built up inside bank systems.

Why this matters structurally, and what it reveals: the ">90% non-clients" figure is the tell. A targeted enforcement push would hit the banks where a given debtor actually holds accounts. A blanket cross-bank-cross-region fan-out that is overwhelmingly non-client means the FSSP side is **broadcasting the full debtor registry to every bank** rather than routing. That points to either (a) a technical fault in the AIS FSSP automation (several commentators hypothesize the system lost delivery-acknowledgements and re-sent the entire accumulated/duplicated queue — **(hypothesis, not confirmed by primary NSFR/ABR statements)**), or (b) a deliberate shift to a "portfolio/fan-out" query model that banks fear will become **regular**. The primary sources (Kommersant, Klerk) explicitly do NOT confirm a technical cause; NSFR only calls it an "anomalous flow." So the "glitch" framing is plausible but unverified — treat as open.

## [1] Competitors / peers
Not a competitive-market event; the peers here are the other **banks** (via NSFR / ABR, the two complaining associations) on one side and the **state counterparties** (FSSP, Bank of Russia as arbiter) on the other. The relevant comparison is other state-mandated automated query channels banks must service under SMEV: FNS (tax), Rosfinmonitoring (115-FZ AML), the FSSP travel-ban/restriction feed (cf. [[SberBank Online adds FSSP travel-ban check service]], where the flow goes the other way — bank reads FSSP data for a consumer product). The pattern across all of these is the same structural asymmetry: the state side sets volume unilaterally, the bank side carries a hard statutory SLA plus fine exposure. Why the lay of the land is this way: SMEV automation (since Dec 2022) removed the human throttle on the FSSP side, so there is no natural rate limit — the only governor is the bank's own infrastructure, which is exactly what broke here.

## [2] Company history / fit
Not a single-company story; it is a **sector-infrastructure incident**. Fit with the corpus: FSSP–bank integration is an active, recurring theme — Sber shipped a consumer-facing FSSP travel-restriction check in July 2026 ([[SberBank Online adds FSSP travel-ban check service]]), showing banks are deepening FSSP data ties voluntarily on the product side even as the mandatory back-end (debtor queries) becomes a load/compliance liability. The actors driving the response are the two banking lobbies: **NSFR** (National Council of the Financial Market, Emelin) and **ABR** (Association of Russian Banks). Why they act this way: both face a classic regulated-utility squeeze — obligation (3-day answer) + penalty (₽50k–₽100k per violation under KoAP) but zero control over inbound volume, so the only lever is to escalate to the Bank of Russia for relief.

## [3] Novelty / value-add / traction
What is genuinely new here is not a product but an **operational-risk and governance gap exposed**: the Dec-2022 automation created a channel with no volume ceiling, and Sept 2026 is the first time it visibly overran bank capacity at scale. The "traction" that matters is the concrete ask the banks filed with the CBR:
- Instruct FSSP to **stop abusing the right to send unlimited queries**.
- Issue a memo **relieving banks of liability for missed 3-day deadlines on the 18–21 Sept batch**.
- Require FSSP to give **≥10 days' advance notice** of future query surges.
Why the value/risk is real: the fine is per-violation and the 3-day clock is statutory, so a 12.8M-in-a-day spike mechanically generates mass technical non-compliance the bank cannot avoid — the liability is detached from fault. Who "captures the cost" in the stack: entirely the banks (infra + fine exposure); the FSSP bears none. That asymmetry is the live issue the CBR must now arbitrate.

## [4] What's next / market sentiment
Immediate: banks await a Bank of Russia ruling on the liability-relief request; FSSP's public line is unyielding — "we exercise our powers within current enforcement-proceedings law." Banks warn that **fan-out/portfolio query broadcasts like 18–21 Sept are expected to recur on a regular basis** (per Klerk), which is why the ask includes a standing 10-day-notice rule, not just one-off amnesty. Why the market will go this way (analysis): absent a rate-limit or notice mechanism baked into SMEV, this is a recurring tail-risk — each surge is a mass-fine event for banks and a free externality for FSSP, so the structural fix has to be regulatory (CBR mediating an SLA/throttle), not technical on the bank side. Counterintuitive second-order effect: heavier FSSP automation, sold as efficiency, **raises systemic operational risk** for the banking sector because it concentrates an uncapped, non-client-filtered load onto a hard SLA — more automation = more fragility here, not less.

## Sources
- Kommersant — "Банки не успевают отвечать на обращения ФССП по информации о должниках" https://www.kommersant.ru/doc/9025091
- Klerk.ru — "ФССП направила банкам до 30 раз больше запросов о должниках, чем обычно" https://www.klerk.ru/buh/news/713497/
- Novaya Gazeta https://novayagazeta.ru/articles/2026/10/13/banki-pozhalovalis-na-desiatki-millionov-zaprosov-sudebnykh-pristavov-o-dolzhnikakh-news
- Meduza https://meduza.io/news/2026/10/13/banki-v-rossii-za-tri-dnya-poluchili-desyatki-millionov-zaprosov-sudebnyh-pristavov-o-dolzhnikah
- BFM https://www.bfm.ru/news/620718
- Primary channel: Финтехно https://max.ru/fintexno
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Glitch or policy?** Was the 18–21 Sept flood a technical fault in AIS FSSP (lost delivery-acks → re-sent/duplicated queue) or a deliberate new fan-out model? — **Open.** Primary sources (Kommersant, Klerk) do NOT confirm a technical cause; the duplication theory is commentator hypothesis. Banks' fear that it "will become regular" implies they suspect policy, not a one-off bug.
2. **Why >90% non-clients?** This is the key signal — a blanket registry broadcast, not routing. Confirmed by NSFR. Points to no targeting logic on the FSSP side.
3. **Is the scale verified or lobby-sourced?** The 12.8M/day and 48x figures come from NSFR/ABR (banking lobbies escalating to CBR) — self-interested sources. No independent FSSP-side confirmation of volumes. — partially open.
4. **What is the actual legal exposure?** ₽50k–₽100k per violation (KoAP) × potentially thousands of missed 3-day deadlines = material but hard to size without a per-query vs per-batch fine interpretation. — open on how fines are counted.
5. **Did any bank actually get fined?** No — the story is pre-emptive liability-relief lobbying; no reported penalties yet. "Threatened with fines," not "fined."
6. **Why Dec 2022 as the inflection?** SMEV automation removed the human throttle — the structural root cause. Confirmed in primary text.
7. **What exactly did banks ask the CBR for?** (a) stop FSSP "abuse of unlimited queries", (b) amnesty for 18–21 Sept deadline misses, (c) ≥10-day advance notice of surges. Confirmed (Kommersant/Klerk).
8. **Has the CBR responded or ruled?** Not reported as of 13 Oct 2026. — open.
9. **Is FSSP legally wrong?** FSSP says it acts "within current enforcement law" — likely legally entitled; the gap is SLA/volume governance, not legality. The fix is regulatory, not a violation finding.
10. **Could banks be at fault (capacity under-provisioned)?** The 3-day SLA presumes normal volume; a 30–48x spike is not something SLAs were sized for. Fault attaches to the uncapped channel design, not bank provisioning. — analysis.
11. **Systemic-risk angle:** Does an uncapped FSSP channel threaten core banking ops (queue build-up blocking other calls)? Note says call queues formed inside bank systems — a real availability risk, not just compliance. 
12. **Who bears the cost in the stack?** Banks carry infra + fine risk; FSSP bears zero. Asymmetry is the core governance issue.
13. **Is this new vs recurring?** First time it overran capacity at scale since 2022 automation — new as an incident, but banks warn of recurrence. Fresh event.
14. **Freshness/duplicate check:** No prior corpus note covers FSSP debtor-query floods; [[SberBank Online adds FSSP travel-ban check service]] is a different (consumer-facing, bank-reads-FSSP) flow. Not a duplicate.
15. **What would change the weight?** If CBR mandates a throttle/notice rule → precedent for all SMEV state-query channels (FNS, AML), raising importance sector-wide. — open.

**Importance: 3/5 — rationale.** A confirmed, large-scale, dated sector-infrastructure incident with concrete numbers (12.8M/day, 48x, 3-day SLA, ₽50–100k fines) and an active CBR escalation — materially above a routine product note. Capped at 3 because: single-country, back-office/operational (not a market-moving deal or new business model), no actual fines levied yet, no CBR ruling, and the root cause (glitch vs policy) remains unconfirmed. Could rise to 4 if the CBR ruling sets a lasting SMEV-wide governance precedent.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-14]] (2026-10-14).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits in Russian bank↔government-systems integration (regtech / operational-resilience sub-vertical), not a product market — so no TAM/multiples apply (no data; this is infrastructure load, not a revenue line). Structure: the bank↔FSSP (Federal Bailiff Service) debtor-asset-inquiry channel has been **fully automated via SMEV since December 2022**, with a hard **3-day statutory response window** per inquiry (per note; corroborated by Kommersant/Meduza, 2026-10-13). "Why now": (i) from 1 September 2026 banks and MFOs were put under new FSSP debt-collection reporting obligations (Izvestia, 2026-08-31), raising baseline integration load; (ii) the 18–21 Sep spike — normal volume exceeded **10–12x, up to 30x** (NSFR/Emelin), **up to 48x** (ABR), one regional bank taking **12.8M inquiries on 19 Sep ≈ a full month's volume** in one day, >90% about non-clients (per note; Lenta/Klerk/Habr, 2026-10-13). Experts attribute it to a probable technical fault in FSSP's automated side, not a deliberate load (Kommersant). The second-order point: a monopoly government counterparty on a mandatory, time-bound, non-rate-limited rail can inject unbounded load into every bank's back-office at once — the banks bear the cost, the deadline, and the fine risk, with no throttling contract on the other side.

**Competitive landscape.** Not a competitive market — FSSP is a single mandatory counterparty and every licensed bank is a forced participant; there is no "winning" here, only resilience differentials. The relevant KPIs are operational, not commercial: inbound SMEV request rate vs. provisioned throughput, queue depth/latency, and % of requests answerable within the 3-day SLA. Banks with elastic/cloud back-office capacity and request-queue buffering absorb a 30–48x spike; those on fixed on-prem capacity form call queues (explicitly described in the note) and risk breaching the window. Positioning is a capacity question, not a moat: large banks (Sber, VTB) with heavy SMEV/gov-integration estates are better provisioned; small regional banks — the ones that took 12.8M/day — are structurally exposed because the load is undifferentiated by bank size (requests span all regions/client categories, >90% non-clients). The sector response was collective lobbying: NSFR and ABR escalated to the CBR/FSSP asking for clarification and fine relief (BFM/Rambler, 2026-10-13) — the signal that no single bank can engineer its way out.

**Comps & multiples.** No valuation/round/deal — multiples = no data (operational-incident, not a transaction). Internal comparables (bank/MFO ↔ government-systems integration, RU):
- [[SberBank Online adds FSSP travel-ban check service]] — same FSSP↔bank rail, opposite direction (bank *pulls* FSSP data as a consumer product); shows the integration is two-way and productized, which makes the inbound-overload exposure structural, not incidental.
- [[Russian microfinance firms can connect to biometric system cheaply]] / [[Sravni helps microlenders embed mandatory biometric verification]] — same pattern of a mandatory state system (biometric EBS) imposing integration cost on regulated lenders; same regtech/operational-burden lens.
- [[Bank app adds Dom service for household bill payments]] — adjacent bank-as-integration-hub to state/utility systems (weaker comp).
Distribution not computed — qualitative only; no ≥3 comparable financial figures exist for this type.

**Risk flags.**
1. **Compliance / fine cascade.** Each missed 3-day response carries an administrative fine (~50,000–100,000 RUB per the RU press). Applied per-inquiry against millions of requests, NSFR warns the aggregate "genuinely threatens the financial stability of some banks" — a per-unit penalty designed for normal volumes becomes existential under a 30–48x fault-driven spike. Watch whether CBR/FSSP grant retroactive relief.
2. **Operational resilience / single-counterparty concentration.** The rail has no apparent rate-limiting, back-pressure, or advance-notice contract on the FSSP side ("без предварительного предупреждения"); a fault in one government system simultaneously overloaded the entire sector. This is textbook critical-third-party concentration risk — the exact exposure global operational-resilience regimes (FCA/PRA, OSFI E-21) are built to govern, with no analogous binding regime on the state counterparty here.
3. **Asymmetric cost allocation / disintermediation of control.** Banks hold the SLA, the capacity cost, and the liability; FSSP holds the send button with no reciprocal obligation. Smaller banks are disproportionately hit because load is undifferentiated by institution size — a structural fairness/concentration problem, not a one-off.

**What this changes (idea-lens).** (analysis) This is a resilience/regulatory stress event, not a re-rating — but it is a falsifiable trigger for change on the government-integration rail: thesis — the CBR/FSSP will have to add either rate-limiting/advance-notice on the FSSP side or a fine-safe-harbour for load anomalies, because the current design externalizes unbounded operational risk onto regulated banks. Watch for: a CBR/FSSP response to the NSFR/ABR escalation, and whether fines for the 18–21 Sep window are waived. What would make the thesis wrong: regulators treat it as a one-off technical glitch, levy no fines, and change nothing — leaving the structural exposure intact for the next fault.

Sources: https://www.kommersant.ru/doc/9025091 · https://meduza.io/news/2026/10/13/banki-v-rossii-za-tri-dnya-poluchili-desyatki-millionov-zaprosov-sudebnyh-pristavov-o-dolzhnikah · https://lenta.ru/news/2026/10/13/spam/ · https://www.klerk.ru/buh/news/713497/ · https://habr.com/ru/news/1093674/ · https://www.bfm.ru/news/620718 · https://iz.ru/2158004/2026-08-31/banki-i-mfo-budut-otchityvatsia-pered-pristavami-o-vzyskanii-dolgov-s-1-sentiabria
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
