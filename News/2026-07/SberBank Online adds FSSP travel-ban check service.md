---
title: "SberBank Online adds FSSP travel-ban check service"
date: 2026-07-13
retrieved: 2026-07-13
tags:
  - company/sber
  - industry/banking
  - region/ru
  - type/product
sources:
  - https://www.sberbank.ru/ru/sberpress/all/article
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s054047d1
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# SberBank Online adds FSSP travel-ban check service

> [!info] 2026-07-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Внедрил в приложение СберБанк Онлайн интегрированный с базой ФССП сервис проверки ограничений на выезд за границу с функцией автоматических уведомлений

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.sberbank.ru/ru/sberpress/all/article>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: SberBank Online adds FSSP travel-ban check service
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Sber added a feature inside the SberBank Online mobile app that lets a user check whether the FSSP (Federal Bailiff Service / ФССП) has imposed a foreign-travel restriction (запрет на выезд) on them, with automatic re-checking and push/SMS alerts when the status changes (appears or is lifted). It lives in the app's "Госуслуги" section and is also findable via in-app search for "Запрет на выезд" (announced ~2026-07-10).

De-PR'd mechanics:
- **It is a thin front-end over existing government data, not new capability.** To turn it on the user must authorise via the Gosuslugi (ЕСИА) portal and grant Sber consent to query the FSSP registry on their behalf. Sber then polls the FSSP register on a schedule. The same data is already free via Gosuslugi and the FSSP site; Sber's value-add is packaging + proactive notification, not access.
- **Scope is deliberately narrow — and this is the key limitation the PR soft-pedals.** It surfaces ONLY FSSP-set restrictions. Travel bans set by other bodies (e.g. security clearance, court/administrative, conscription-related) are NOT shown, so a "clear" result is not a guarantee of exit. Only ~half the picture.
- **Pilot traction (given, not vague):** during the pilot 30,000+ people used it; 2,700+ of them were found to have an active travel restriction (~9%). Real usage numbers, modest scale.
- Why structured this way: bans are triggered by FSSP at debt thresholds (broadly ≥10,000 ₽ for tax/fines/alimony-type debts held >2 months, ≥30,000 ₽ for other debts — and multiple sub-30k productions can be aggregated). The pain point is that a traveller only discovers the ban at passport control. Sber monetises that anxiety indirectly: engagement + a hook to sell debt-repayment (pay off via the same app, which via ГИС ГМП auto-clears the flag with FSSP) — i.e. the feature is a funnel into Sber's payment/lending surface, not a standalone product.

## [1] Competitors / peers
- **Gosuslugi (the state, the real incumbent):** already offers exactly this via "Исполнительное производство → Электронные сервисы ФССП → узнать об ограничениях на выезд" (result in 10–15 s), free. Sber is a convenience wrapper on top of it.
- **FSSP itself:** free registry lookup by ФИО + DOB, plus third-party apps ("ФССП: проверка долгов") on App Store / Google Play.
- **Other RU banks:** T-Bank, VTB, Alfa all embed government/Gosuslugi-adjacent services and debt-repayment; travel-ban checking is a small, easily-copied add-on with no moat. Sber is at parity-to-slightly-ahead only on the *automatic monitoring + alert* packaging, not on data or access.
- Second-order: because the underlying data is a free public API-style government service, no bank can build a durable advantage here — it commoditises instantly. The real competition is for the *repayment transaction* and *engagement*, not the check.

## [2] Company history / fit
Consistent with Sber's embedded-gov-services and super-app strategy. Recent same-app value-added launches: [[SberBank Online adds remote escrow for secondary property deals]] (2026-07-06, remote аккредитив for P2P property sales) — same pattern of stuffing convenience/gov-linked services into the app. Fits the broader RU thesis that standalone banking apps must become life-scenario platforms ([[Финтехно T-Bank sees standalone banking apps losing relevance]]) and that government data is migrating into private app front-ends. Structural driver: with a saturated banking base, Sber competes on ecosystem stickiness — every embedded gov service is a reason not to leave the app.

## [3] Novelty / value-add / traction
Genuinely new *packaging* (bank-native, with automatic monitoring + alerts) but NOT new capability — the data and manual check already exist free on Gosuslugi/FSSP. Value-add is real but marginal: proactive alerting has some utility (you learn before you buy a ticket), and it plugs into pay-off-in-app. Traction is real but small (30k users / 2.7k flagged in pilot). No moat: instantly copyable, no exclusive data, no economics disclosed. This is a retention/engagement feature, not a revenue line.

## [4] What's next / market sentiment
Expect broad rollout across Sber's base and near-certain copying by T-Bank/VTB/Alfa within months. Regulatory backdrop is favourable: RU state is actively pushing gov services into apps (cf. [[Russian central bank proposes Gosuslugi fraud-victim support service]] — CBR wanting fraud-victim navigation on Gosuslugi). Risk: reliance on Gosuslugi/FSSP consent plumbing; and the "only FSSP data" caveat could create false reassurance and reputational blowback if a user is turned back at the border despite a "clear" check. Sentiment: minor, positive-for-engagement, immaterial to financials.

## Sources
- https://www.cnews.ru/news/line/2026-07-10_sberbank_pomozhet_zaranee
- https://finance.mail.ru/article/sber-zapustil-v-prilozhenii-servis-proverki-ogranichenij-na-vyiezd-za-granitsu-69217128/
- https://hi-tech.mail.ru/news/151081-v-prilozhenii-sbera-teper-mozhno-uznat-zapresheno-li-vam-vyezzhat-za-granicu/
- https://www.vesti.ru/ns/servis-sberbanka-proverit-ne-pomeshayut-li-dolgi-poezdke-za-granicu
- FSSP thresholds / how it works: https://fpa.ru/info/kak-uznat-est-li-zapret-na-vyezd-za-granicu-7-sposobov-proverki/ , https://oooeos.ru/customers/faq/za-kakie-dolgi-ne-vypuskayut-za-granicu/
- Gosuslugi lookup path: https://gogov.ru/check/debts
- Internal: [[SberBank Online adds remote escrow for secondary property deals]], [[Финтехно T-Bank sees standalone banking apps losing relevance]], [[Russian central bank proposes Gosuslugi fraud-victim support service]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this new capability or a wrapper?** — Wrapper. Same check is already free on Gosuslugi and the FSSP site; Sber only re-packages it with monitoring + alerts. (answered)
2. **What does Sber actually add over Gosuslugi?** — Automatic periodic re-checking and push/SMS on status change, plus in-app repayment. Not data or access. (answered)
3. **How complete is the check?** — Only FSSP-imposed restrictions. Other agencies' bans are invisible, so a "clear" result is NOT a guarantee of exit. Material caveat. (answered)
4. **Real traction or announcement?** — Real pilot: 30,000+ users, 2,700+ (~9%) flagged with an active ban. Modest but concrete. (answered)
5. **Is there a moat?** — No. Public government data, no exclusivity, instantly copyable by any bank. (answered)
6. **What are the FSSP ban thresholds?** — Broadly ≥10,000 ₽ (tax/fines/alimony-type, >2 months) or ≥30,000 ₽ for other debts; multiple sub-30k productions can aggregate. Ban is a right, not an obligation, of the bailiff. (answered)
7. **Why does Sber build this?** — Ecosystem stickiness + funnel into in-app debt repayment (which auto-clears the FSSP flag via ГИС ГМП). Engagement play. (answered)
8. **Does it require anything from the user?** — Yes: Gosuslugi/ЕСИА auth + consent for Sber to query FSSP on their behalf. Adds friction; consent dependency is a risk. (answered)
9. **Any economics / revenue disclosed?** — No. Immaterial to financials; a retention feature. (answered)
10. **False-reassurance / liability risk?** — Yes: user cleared by Sber but banned by a non-FSSP body could be turned back at the border → reputational risk. (open — unquantified)
11. **Do competitors already do this?** — Not identified as launched at T-Bank/VTB/Alfa specifically, but all embed gov services; copying is near-certain and trivial. (partly open)
12. **Duplicate of another note?** — No. Distinct from [[SberBank Online adds remote escrow for secondary property deals]] (different service, same app). Fresh event dated ~2026-07-10. (answered)
13. **Does it change any thesis?** — No. Confirms the embedded-gov-services / super-app trend already captured in the corpus. (answered)
14. **What breaks it?** — Loss of Gosuslugi/FSSP data plumbing or consent changes; also state could restrict private-app resale of the service. (open)
15. **Bottom line weight?** — Minor convenience feature, no moat, small traction, no economics. (answered)

Importance: 2/5 — Real, live feature with concrete (if modest) pilot numbers, but it is a thin wrapper over free government data with no moat, no disclosed economics, and a narrow scope (FSSP-only). Materially immaterial to Sber; purely an engagement/retention add-on. Fresh (not a duplicate).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is the Russian banking **super-app engagement layer**: incumbents bolt non-banking and government/data services onto the mobile app to drive recurring opens (DAU) and retention, not to earn a fee. Structure is a **consolidated oligopoly** (Sber, T-Bank, VTB, Alfa) racing on product velocity; the barrier here is not the FSSP check itself but **distribution + the Gosuslugi/ЕСИА consent rail** every bank must ride. "Why now": Nov-2025 sector commentary explicitly frames banks "turning apps into super-services" (вовлечение/удержание) — T-Bank adding food/tickets/telemedicine/multibanking, Alfa+VTB scaling open-banking, VTB relaunching a "universal app" in Q1 2026 (per top68.ru, 2025-11-27). Government data (debts, bans, benefits) is the cheapest such hook because it forces habitual re-checking. Gosuslugi itself is huge: **120mn registered, ~14mn daily audience (+40% YoY in 2025)** (per RIA/TASS, Dec 2025). (facts)

**Competitive landscape.** Sector KPIs that matter here: **MAU/DAU, DAU/MAU stickiness, and monetizable in-app action rate** (here: debt paid in-app). Sber's scale anchor: **SberBank Online MAU 84.7mn** (H1 2026, per Sber press service, 2026-07-09; IR baseline 111.2mn retail clients, FY2025 IFRS net profit RUB 1,707.4bn — [[Финтехно Sber plans full crypto operations under new law]]); a separate RAS-series snapshot gives DAU ~44.9mn, DAU/MAU ~53% (single-month figure, treat as indicative). Basis of competition = **distribution + speed to embed**, not the service's economics. Recent moves: T-Bank's flagship gov/data play is **multibanking** (aggregating Sber/VTB/Alfa accounts; Sovcombank added 2026-06-04, per tbank.ru), i.e. *account aggregation*, not a bailiff checker; VTB's super-app relaunch is planned Q1 2026. **No T-Bank/VTB in-app FSSP travel-ban monitor was found in sources** — so Sber looks **first among the majors on this specific feature** (inferred from absence of peer examples, NOT verified exclusivity). Pilot traction de-PR'd: **30,000+ users, 2,700+ found to have restrictions, 1,800+ paid off debts in-app** to lift the ban (per CNews, 2026-07-10) — small absolute numbers, but it proves the payments-conversion loop works. Sber's position: **ahead** on this feature and on reach; moat `(analysis)` = engagement/distribution scale, **not** lock-in (switching cost is ~zero; the same FSSP data is free on Gosuslugi).

**Comps & multiples.** Not a valuation/deal event — no round, no take-rate, no standalone revenue: **standard multiples n/a for this feature**. Franchise anchor for scale only (not attributable to this launch): Sber H1 2026 RAS net profit **RUB 995.3bn, +20.4% YoY, ROE ~23%**, C/I ~25.7% ([[Sberbank H1 2026 net profit rises 20.4% to RUB 995bn]]); peers for reference — T-Bank FY2025 ROE ~29.1% but ~1/6 of Sber's scale, VTB the laggard (ROE ~17.5%, shrinking earnings). Internal comps for the "government-data-in-app" theme: [[SberBank Online adds remote escrow for secondary property deals]] (same funnel-defence logic), [[Russian central bank proposes Gosuslugi fraud-victim support service]] (state pushing services onto Gosuslugi rail). Per-user or engagement-uplift multiple for this feature = **no data** (Sber discloses no incremental MAU/DAU attribution).

**Risk flags.**
1. **Zero differentiation / commoditized data.** The FSSP travel-ban and debt check is **already free on Gosuslugi** (120mn users; from Feb 2026 even lets you check *third parties*). Sber only re-packages a public service with alerts + one-tap pay. Second order: no moat — any peer can replicate via the same ЕСИА rail, so the "first-mover" edge is measured in months, and the retention benefit erodes as VTB/T-Bank copy it.
2. **Dependence on someone else's rails (Gosuslugi/ЕСИА + FSSP).** The feature works only through **Gosuslugi/ЕСИА consent + FSSP electronic services / СМЭВ**; Sber does not own the data or a private FSSP API. Second order: pricing, availability and scope are controlled by the state — a tariff, consent-scope or СМЭВ-access change can degrade or kill the feature unilaterally.
3. **Data-access / privacy optics.** Russian legal/anti-debt commentary already flags a bank requesting Gosuslugi access as a "тревожный сигнал" (warning sign); consent must be *informed* and data-minimized (per bancrotim/banki.ru). Second order: reputational/regulatory exposure if consent scope is read as over-broad — the risk sits on Sber even though the underlying data is the state's.

**What this changes (idea-lens) `(analysis)`.** A minor **fast-follow feature**, not a re-rating: it confirms the RU super-app race has moved to *scraping every free government dataset into the app* as a DAU lever. Falsifiable thesis: if government-data hooks genuinely move stickiness, expect **VTB (Q1-2026 relaunch) and T-Bank to ship an equivalent FSSP/travel-ban checker within ~2-3 quarters** — trigger to watch. Thesis breaks if Sber discloses a *material* MAU/DAU/payment-conversion uplift attributable to the feature (would imply a real engagement edge, not just parity noise); so far it hasn't.

Sources: https://banks.cnews.ru/news/line/2026-07-10_sberbank_pomozhet_zaranee · https://ria.ru/20251215/chislo-2062075017.html · https://top68.ru/news/economy/2025-11-27/banki-prevraschayut-prilozheniya-v-superservisy-307153 · https://www.tbank.ru/about/news/09102025-multibanking-t-bank-has-consolidated-information-about-clients-accounts-with-alfa-bank-vtb-and-sberbank-in-its-mobile-app/ · https://bancrotim.ru/pravo-banka-prosit-dostup-k-gosuslugam-pochemu-eto-trevozhnyy-signal/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
