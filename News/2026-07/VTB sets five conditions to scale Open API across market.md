---
title: "VTB sets five conditions to scale Open API across market"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/vtb
  - industry/open-banking
  - industry/banking
  - region/ru
  - type/commentary
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: s1f3d7759
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# VTB sets five conditions to scale Open API across market

> [!info] 2026-07-03 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] ВТБ на Финконгрессе сформулировал пять ключевых условий, без которых Open API не получится масштабировать на весь рынок. Речь идет о законодательной базе, расширении стандартов обмена данными для юрлиц, независимом операторе, платформе управления согласиями клиентов и единых процедурах подключения банков. По словам старшего вице-президента банка Сергея Безбогова, именно корпоративный сегмент сегодня остается главным драйвером открытого банкинга. Поэтому сейчас особенно важно ускорить разработку стандартов для юридических лиц и вовлечь в пилоты как можно больше участников рынка. ВТБ уже развивает сервис «Мультибанк», позволяющий компаниям видеть счета разных банков в одном интерфейсе. Дальнейшее развитие Open API должно сделать возможным не только просмотр информации, но и полноценное управление счетами из одного приложения. 💳 Финтехно в Telegram | в MAX

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: VTB sets five conditions to scale Open API across market
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
At the Bank of Russia **Financial Congress** (St. Petersburg, 1–3 July 2026), VTB's Sergey Bezbogov (deputy head of the technology block / senior VP) publicly enumerated **five conditions** he says are prerequisites to scale Open API from bilateral pilots to the whole market. External reporting confirms all five precisely (the Финтехно summary compresses them):

1. **Legislative base** — a full legal framework, which VTB expects to form **by 2027** (matches the CBR's own postponed timeline; see below).
2. **Equidistant independent operator** — a neutral arbiter/infrastructure operator to lower connection costs, ensure transparency and enforce common rules (an inter-bank clearing/dispute layer).
3. **Commercial consent-management platform** — a shared mechanism for correctly obtaining and revoking client consents to data access across several banks at once.
4. **Standards for legal entities** — the CBR has issued **14 standards** (Bezbogov's count; the Dec-2025 published complex was reported by Vedomosti as ~10 documents — treat the exact number as disputed), but key **corporate/юрлицо functionality** standards are still missing and must be finished.
5. **Standardised base connection processes** — run either on the CBR itself or an independent venue like the **Fintech Association (АФТ)**.

**This is commentary, not an event.** No new product, deal, number or launch — it is a **position statement / lobbying wishlist** at a regulator's forum. The single Финтехно source (one Telegram channel, no primary text loaded) attributes the "corporate segment is the main driver of open banking" framing and the "Мультибанк" reference to VTB.

**Why framed this way / what it reveals (analysis):** VTB is the sequential **hub-of-record** for corporate multibanking (Sber first → Alfa → Gazprombank next). Four of its five conditions — an "independent operator," a shared consent platform, common connection processes, legal-entity standards — are exactly the **shared public infrastructure** that lets an incumbent hub onboard rivals cheaply and with legal certainty, while a **legislative base** removes the voluntary-adoption ceiling. So the "five conditions" read less as neutral market-development principles than as **VTB's dependency list to convert its early hub lead into a mandated, low-friction, market-wide network**. Notably VTB pushes for a *neutral* operator — the opposite of T-Bank's forum message the same days (see below), where T-Bank argued the biggest banks *themselves* can drive open innovation.

## [1] Competitors / peers
- **T-Bank (same forum, opposing frame):** [[T-Bank showcases bank-led open innovation at Financial Congress]] — Sergey Khromov argued innovation can come *from top-5 banks*, not only ЦБ/НСПК; and in [[T-Bank multibanking pilot reaches 700k users]] he lobbied that **base data transfer should be free**. VTB wants a neutral operator + legal mandate; T-Bank wants free data + bank-led rails. Both are self-interested: VTB (state #2, corporate hub) wants mandated shared infra; T-Bank (smaller deposits, retail aggregator) wants cheap symmetric data.
- **Sber:** the other anchor; VTB↔Sber launched **production** corporate Open-API exchange ~**3 Apr 2026** (per ComNews/bosfera). Sber is both counterparty and the largest-deposit rival with the opposite incentive on "free data."
- **Corporate multibank rail:** [[VTB and Alfa-Bank roll out Multibank service for corporates]] — the read-only treasury-aggregation product these conditions are meant to scale; Gazprombank flagged next.
- **Regulatory storyline:** [[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]] — the CBR blocked the big banks' *independent* payment system, channeling their cooperation *into* its Open-API/НСПК perimeter. Multibanking is the sanctioned outlet; hence the banks now lobby over *its* terms (operator, data pricing, standards). Also [[Bank of Russia to value NSPK ahead of possible stake sale]] shows the same "who controls the shared infra" question across NSPK.
- **Global prior art (the conditions are un-novel):** the EU's PSD2/CMA9 model already has these building blocks — mandated APIs, TPP consent dashboards, standards bodies (OBIE), central directories. Russia is **re-deriving** an open-banking rulebook the UK/EU built 2018–2021.

**Position:** VTB is *ahead* domestically as corporate hub but *behind* globally — everything it asks for (operator, consent platform, standards, mandate) exists in mature open-banking regimes. Mechanism delta (one sentence): unlike PSD2 where neutral TPPs aggregate banks, here the **largest banks aggregate each other** and now lobby for the neutral scaffolding that makes that incumbent-led model durable.

## [2] Company history / fit
VTB (Russia's #2, state-controlled) has consistently positioned its business-bank as a platform and made itself the **orchestrator** of corporate Open-API exchange (Sber→Alfa→Gazprombank). Advocating five system-level conditions fits that trajectory: VTB has the most to gain from turning its bilateral hub into a mandated, standardised network. **Why it acts this way (analysis):** with Western treasury/connectivity vendors gone and independent bank rails rejected by the CBR, the only path to a market-wide corporate-banking cockpit runs through the regulator's Open-API perimeter — so VTB's rational move is to shape *that* perimeter (push for a legal mandate, corporate-entity standards, and a neutral operator that de-risks onboarding rivals) rather than build proprietary rails.

## [3] Novelty / value-add / traction
**Novelty: low.** No new capability, product or metric — a restatement of well-known open-banking prerequisites, all of which exist abroad and most of which the CBR/АФТ are already building (10–14 published standards; a Commercial Consent Management Platform with Mindigital already announced). The one substantive **new signal** is VTB *publicly naming* the missing pieces (esp. corporate-entity standards and a neutral operator) and dating the legal base to **2027** — useful as a checklist of what's blocking scale, not as a development. **Traction: none to report** — this is a wishlist, not adoption. The underlying "Мультибанк" it references is read-only and has no disclosed client/volume numbers ([[VTB and Alfa-Bank roll out Multibank service for corporates]]). **Who captures the margin (analysis):** if VTB's conditions are met via a *neutral* operator and free/cheap base data, the value shifts from infrastructure control toward whoever owns the **corporate cockpit + cross-sell** (financing/FX) — which is precisely VTB's aim. The tell is that VTB wants the plumbing *socialised* (operator, standards, mandate) so the *relationship* it already holds becomes the moat.

## [4] What's next / market sentiment
- **Regulatory backdrop (the swing factor):** the CBR's mandatory Open-API timeline — originally **2026** (largest banks/brokers/insurers) / **2027** (MFOs, depositories, DFA operators, financial platforms) — was **postponed in Oct 2025**, with new deadlines pending a **federal law**; CBR fintech-dept head Ruslan Bulatov has voiced hope for **2027** go-live. So current adoption is **voluntary/standard-led ahead of a delayed mandate**. VTB's "legislative base by 2027" aligns with this. Watch: (a) the federal Open-API law, (b) whether a neutral operator (CBR or АФТ) is designated, (c) the Commercial Consent Management Platform launch, (d) the **data-pricing** ruling (VTB silent on it; T-Bank wants free — a live, unresolved fight).
- **Why the market goes this way (second-order, analysis):** because the regulator blocked independent rails, the big banks now compete *through the design of the shared infrastructure*. VTB lobbying for a neutral operator + mandate is a bid to lock in an incumbent-led, standardised network before smaller/neutral aggregators can contest the cockpit. Counterintuitive risk: a "neutral operator + mandated APIs" could equally **re-open** the corporate cockpit to third-party aggregators (the PSD2 outcome), eroding the very hub advantage VTB is trying to entrench — so VTB's asks are double-edged.

## Top challenge/extra questions
See challenge file.

## Sources
- Финтехно (max.ru/fintexno) — primary aggregated text (2026-07-03). Full text not loaded.
- Five conditions (Bezbogov, CBR Financial Congress): https://volga.news/article/796723.html · https://penzavzglyad.ru/news/204608/ekspert-nazval-klyuchevye-usloviya-dlya-razvitiya-obmena-dannymi-mezhdu-bankami · https://www.interfax.ru/business/1051540 · https://www.tatar-inform.ru/news/vtb-predlozil-mexanizm-reseniya-sporov-mezdu-bankami-pri-obmene-dannymi-6018728
- VTB "Open API creates new rules for banking competition" (May 2026): https://pln-pskov.ru/business/588079.html
- CBR mandate + Oct-2025 postponement + 2027 hope + Dec-2025 standards (10 docs): https://bosfera.ru/press-release/bank-rossii-perenes-sroki-obyazatelnogo-vnedreniya-open-api · https://frankmedia.ru/224334 · https://rtln.ru/blog/otkrytye-api-banka-rossii-itogi-2025-goda-novye-sroki-obnovlenie-standartov/ · https://www.vedomosti.ru/finance/news/2025/12/24/1165941-tsb-obnovil-kompleks
- CBR mandate scope (2026 largest / 2027 others): https://www.akm.ru/eng/news/the-largest-russian-banks-and-insurance-companies-will-be-required-to-use-open-apis-from-2026/ · https://www.cbr.ru/eng/press/event/?id=20969
- VTB+Sber production exchange (~3 Apr 2026): https://www.comnews.ru/digital-economy/content/244586/2026-04-03/2026-w14/1012/sber-i-vtb-zapustili-promyshlennyy-obmen-dannymi-otkrytym-api
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team — VTB's five Open-API conditions

1. **Is this an event or commentary?** Commentary — a position statement at the CBR Financial Congress. No product, deal, number, or launch. Weight rests on signal value, not a development. **Confirmed: commentary.**

2. **Are the "five conditions" accurately reported?** Yes — external Russian reporting (Interfax, Volga News, Penzavzglyad, Tatar-inform) confirms all five: (1) legislative base ~2027, (2) equidistant independent operator, (3) commercial consent platform, (4) legal-entity standards (14 issued, more needed), (5) standardised base connection processes via CBR or АФТ. **Confirmed against the source.**

3. **Is it novel?** No. These are standard open-banking prerequisites already implemented abroad (PSD2/CMA9: mandated APIs, consent dashboards, OBIE standards, central directories) and largely in-flight at the CBR/АФТ (10–14 standards, Commercial Consent Management Platform announced). Russia is re-deriving a known rulebook. **Low novelty.**

4. **How many standards — 14 or 10?** Bezbogov says 14; Vedomosti reported the Dec-2025 published complex as ~10 documents. **Disputed — flag both; don't assert 14 as fact.**

5. **Whose interest do the five conditions serve?** VTB's. As the corporate hub-of-record (Sber→Alfa→Gazprombank), VTB gains most from mandated shared infra + a neutral operator + legal-entity standards that de-risk onboarding rivals. The wishlist is a **dependency list to entrench an incumbent-led network**. **Confirmed bias to flag (analysis).**

6. **Why push for a *neutral* operator if VTB is the hub?** Counterintuitive but rational: a neutral operator socialises connection cost/liability across the market while VTB keeps the *client relationship*. Risk to VTB (see Q13): a truly neutral, mandated rail could also let third-party aggregators contest the cockpit. **Double-edged.**

7. **Mandate or voluntary?** Voluntary/standard-led. CBR's mandatory timeline (2026 largest / 2027 others) was **postponed Oct 2025** pending a federal law; go-live hoped for 2027. Any "regulation is forcing this" framing is wrong today. **Confirmed.**

8. **Does it duplicate the corporate-multibank note?** No — [[VTB and Alfa-Bank roll out Multibank service for corporates]] is the *product* (read-only treasury aggregation, VTB↔Alfa). This is a *policy/commentary* item naming the systemic conditions to scale it market-wide. Different type (commentary vs product), different content (five conditions vs a launch). **Not a duplicate — fresh.**

9. **Does it duplicate the two T-Bank Financial-Congress notes?** No, and it complements them: T-Bank ([[T-Bank showcases bank-led open innovation at Financial Congress]], [[T-Bank multibanking pilot reaches 700k users]]) argues *bank-led* innovation + *free base data*; VTB argues *neutral operator + legal mandate*. Same forum, **opposing frames** — together they map the Russian open-banking policy fight. **Fresh, and adds the VTB/corporate side.**

10. **Is the "corporate segment is the main driver" claim substantiated?** It's VTB's assertion, consistent with its corporate-hub strategy and the CBR's legal-entity Open-API pilot. Plausible but self-serving; no independent volume data. **Partly open.**

11. **What's silent?** VTB says nothing on **data pricing** (the live fight T-Bank opened with "free base data"), nothing on fraud/data-leak liability across banks, and no adoption metrics for its own Мультибанк. **Notable silences.**

12. **Is "legislative base by 2027" credible?** It matches the CBR's own postponed schedule and Bulatov's 2027 hope — so it's an alignment with the regulator's timeline, not an independent forecast. Treat as **directional, dependent on the federal law actually passing.** Open.

13. **Second-order: do the conditions help or hurt VTB's hub?** Ambiguous. Mandated APIs + neutral operator + consent platform lowered PSD2's barriers *for third-party aggregators* in the EU — the same design could re-open Russia's corporate cockpit to fintechs, eroding VTB's incumbency edge. So VTB's asks could backfire. **(analysis) — key uncertainty.**

14. **Sourcing strength?** Weak: single Telegram channel (Финтехно), no primary text loaded. Corroborated on the five conditions by multiple regional Russian outlets, so the *facts* stand; but it's PR-forum commentary. **Facts confirmed, but low-weight channel.**

15. **Does it move anything?** No immediate market impact — it's a checklist of blockers. Its value is as a **signal of what's gating open-banking scale in Russia** (legal base, operator, consent platform, corporate standards, connection processes) and of VTB's positioning vs T-Bank/Sber. Useful for corpus continuity, not a mover.

16. **Prior art / first mention?** VTB has aired the "Open API creates new rules for banking competition" theme since ~May 2026; the "five conditions" framing is the Congress-specific articulation, not a first-ever statement of intent. **Incremental restatement.**

**Importance: 3/5 — rationale:** Fresh (not a duplicate) and genuinely useful as the **VTB/corporate counterpart** to the two T-Bank Financial-Congress notes — together they crisply map Russia's open-banking policy fight (neutral operator + legal mandate vs bank-led rails + free data), and VTB's five conditions are a clean checklist of what actually gates market-wide scale (legal base ~2027, independent operator, consent platform, legal-entity standards, connection processes). But weight is capped: it is **commentary, not an event** — no product/deal/number/traction; the "conditions" are un-novel (all exist in PSD2/CMA9 and are largely in-flight at CBR/АФТ); the mandate is postponed (voluntary adoption); the wishlist is self-serving (entrenches VTB's hub) and silent on data-pricing/liability; and sourcing is a single Telegram channel (facts corroborated by regional outlets, but low-weight). Structurally informative signal, not a mover → 3/5.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-04]] (2026-07-04).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian open banking / Open API — a regulator-driven, standard-first market, not a market-led one. The Bank of Russia has developed Open API standards since 2021 (advisory to date), and mandatory use begins in 2026 for the largest banks, brokers and insurers, extending in 2027 to microfinance orgs, depositories, information-system operators and financial platforms (per Bank of Russia / AKM, as of 2026). No TAM/revenue figure is public for the Russian open-banking layer — no data. Structure: highly concentrated at the top (five pilot players — Sber, T-Bank, Alfa-Bank, Gazprombank, VTB — drive the standard); barriers are regulatory (CBR conformance) plus network effects (value rises with each connected bank). Why now: the 2026 mandate turns a voluntary pilot into a compliance deadline, so incumbents are racing to set the de-facto corporate standard before the rules harden. Why-ladder: mandate forces connectivity → whoever runs the aggregation interface owns the corporate treasury relationship → account-viewing today becomes account-management tomorrow → the "primary bank" for a multi-bank holding can be decided by UX, not by balance-sheet size (a re-ranking risk for smaller incumbents). VTB's five stated conditions (legislation, expanded legal-entity data-exchange standards, an independent operator, a client-consent management platform, unified bank-onboarding procedures) are effectively a de-PR'd checklist of what is *still missing* — i.e. the framework is not yet operational at scale (analysis).

**Competitive landscape.** Sector KPIs for a bank-aggregation play: number of connected banks (network coverage), corporate clients on the aggregator, share of corporate liquidity visible in-app, and progression from read-only (statements/balances) to write access (payments/account management). Key players: Sber and T-Bank were first to pilot a two-bank joint solution (mid-2024, per BFC/AKM); VTB is building "Multibank" for corporates and is sequencing partners — Sber first, then Alfa-Bank (2026-06-23, see [[VTB and Alfa-Bank roll out Multibank service for corporates]]), with Gazprombank named next. Basis of competition: distribution and network coverage, not price — the winner is whoever aggregates the most rival banks into one treasury window. VTB's position: catching-up-to-leading in the *corporate* niche it has chosen as its wedge, where Sergey Bezbogov calls the corporate segment the main open-banking driver; moat is prospective network effects (value grows for a VTB client even when accounts sit at competitors) plus switching costs once treasuries standardize on one interface — but read-only functionality means the moat is thin today (analysis). De-PR: this is aggregated *viewing* only; full money-movement is explicitly not live yet, and the note is a conference statement (Fincongress), not a shipped capability — "announced/advocated," not "adopted."

**Comps & multiples.** This is a product/regulatory-positioning story with no round, deal or valuation attached, so no transaction multiple applies — no data. Internal comps (same market/standard, corporate open-banking): [[VTB and Alfa-Bank roll out Multibank service for corporates]] (2026-06-23) — same protagonist, next network node; [[Ukraine's central bank simplifies open banking payment initiation]] (2026-04-09) — adjacent CIS regulator easing PIS rules; global regulator-led comps for structure only: [[Colombia establishes mandatory Open Finance framework]] (2026-04), [[FCA sets out vision for open finance]] (2026-04), [[Saudi central bank begins licensing open banking fintechs]] (2026-05). IR grounding — VTB's own filed figures (VTB Group FY2025 IFRS, results call 2026-03-03): FY2025 net profit was described as a record in relative terms it fell — ROE 18.3% (−4.6pp YoY); NIM 1.4% (−30bp YoY); net fee & commission income RUB 307bn; N20.0 capital adequacy ~10.0% (up from 9.1% at start of 2025); FY2026 net-profit target RUB 600–650bn; guided RWA growth ~5% with corporate lending +10% and retail −5%, plus continued cost (staff + IT) optimization to normalize CIR below 40% NII. Read-through: VTB's own guidance leans on the corporate segment for growth, which is exactly the segment its Open API "Multibank" wedge serves — the open-banking push is strategically aligned with where the P&L is being steered (analysis). Distribution of multiples not computed — no comparable priced transaction. [Sources: drive.google.com/file/d/1O3Y-j1D6YA4X0wz6AmllxM6OkZUDKMDO/view (FY2025 transcript); drive.google.com/file/d/1q5I8GEraBY63jCZ_LSyE9zXJ1ooS6BZP/view (FY2025 IFRS)]

**Risk flags.**
- *Regulatory dependence / execution outside VTB's control.* Four of VTB's five conditions (legislation, an independent operator, a consent platform, unified onboarding) require the CBR and other parties to act — VTB can advocate but not deliver them; scaling is gated on a regulatory roadmap it doesn't own, so the timeline is soft (second-order: the "record" being touted may stay a pilot).
- *Thin moat while read-only.* Value today is a single-window statement view; until write access (payments/management) is live, switching costs are low and a rival aggregator (Sber/T-Bank, first movers) could capture the treasury relationship first (second-order: mandate-driven parity erodes any first-mover UX edge).
- *Standard commoditizes the incumbents.* A CBR-mandated, interoperable Open API by design lets any bank see into any other — it lowers the barrier that big balance sheets historically provided, so a mandated open standard can compress the very corporate-relationship advantage VTB is trying to build (second-order: the regulator, not VTB, captures the network value).

**What this changes (idea-lens).** For the sector, the 2026 mandate flips Russian open banking from voluntary pilot to compliance race, and the corporate treasury-aggregation window is the contested prize — whoever nodes-in the most rival banks first sets the default (analysis). Falsifiable thesis: VTB's "Multibank" becomes the corporate open-banking hub *only if* it (a) connects Gazprombank and beyond and (b) ships write/payment functionality before the standard is fully mandated. Trigger to watch: Gazprombank go-live and any move from read-only to account-management. What breaks the thesis: CBR designates a neutral "independent operator" (one of VTB's five conditions) that aggregates at the utility layer — in which case the aggregation value accrues to the regulator's rails, not to VTB. (analysis)

Sources: https://www.cbr.ru/eng/press/event/?id=20969 · https://www.akm.ru/eng/news/the-largest-russian-banks-and-insurance-companies-will-be-required-to-use-open-apis-from-2026/ · https://www.akm.ru/eng/news/beber-and-vtb-are-the-first-russian-banks-to-test-an-open-banking-service-for-business/ · https://drive.google.com/file/d/1O3Y-j1D6YA4X0wz6AmllxM6OkZUDKMDO/view · https://drive.google.com/file/d/1q5I8GEraBY63jCZ_LSyE9zXJ1ooS6BZP/view
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Background: VTB's financial health behind its Open API push**

VTB's drive to scale Open API (and its "Multibank" corporate service) is being made from a position of a large but earnings-pressured balance sheet. Its most recent reported results — FY2025 (12M 2025) IFRS, published 2026-02-25 with an analyst call on 2026-03-03 — show profitability declining year-on-year even as the group leans into open-banking and corporate-segment digital services.

**Reported FY2025 figures (IFRS, RUB):**
- Net income: **RUB 502.1bn**, vs RUB 551.4bn in FY2024 — **-8.9% YoY** (though VTB flagged it as the highest net income in its public history on an absolute-scale narrative, the reported group figure is down YoY).
- Net income attributable to parent's shareholders: **RUB 483.7bn** vs RUB 535.3bn (**-9.6% YoY**); non-controlling interests RUB 18.4bn (+14.3%).
- EPS (basic & diluted): **RUB 79.0** vs RUB 94.0 (**-16.0% YoY**) — larger drop than net income, reflecting share issuance/dilution.
- Return on equity (ROE): **18.3%**, down **-4.6 pp** YoY.
- Net interest margin (NIM): **1.4%**, down **-30 bps** YoY — margin compression under high-rate conditions.
- Net fee & commission income: **~RUB 307bn** — the fee line management highlighted as a growth driver (relevant to open-banking/transactional monetisation).

**vs prior / consensus:** No sell-side consensus is available in the IR DB; comparison is vs the prior-year reported base. All headline profitability metrics (net income, EPS, ROE, NIM) are **down YoY**, so on a reported basis FY2025 is a **miss vs the prior year**. Fee income was the relative bright spot.

**Guidance:** For 2026 management targets net income of **RUB 600-650bn** (implying a return to double-digit YoY growth off the RUB 502bn base), with cost-to-income normalising as net fee & commission income (ЧКД) grows fast and net interest income stabilises (NII to remain <40% of the CIR mix per the call). Long-term dividend policy reaffirmed at **50% IFRS payout**.

**Thesis flags relevant to the Open API strategy:**
- Capital is the binding constraint: Basel buffers are stepping up — minimum adequacy was raised to 9.25% for 2025, rises to **10.0% from 1 April 2026** and **10.75% from 1 April 2027**. This makes capital-light, fee-generating channels (corporate Open API, Multibank, consent-management platforms) strategically attractive as VTB seeks ROE-accretive, low-RWA revenue.
- Corporate/юрлица segment is management's stated main driver of open banking, aligning the five Open API conditions (legislation, corporate data-exchange standards, independent operator, client-consent platform, unified bank-onboarding procedures) with where VTB already earns fee income.
- Risk: NIM compression (1.4%) and the YoY profit decline mean the group needs the 2026 rebound and fee growth to materialise; Open API monetisation is a multi-year, standards-dependent bet rather than a near-term earnings lever.

Sources (VTB own filings, redirect to Drive):
- FY2025 IFRS consolidated financial statements (2026-02-25): https://drive.google.com/file/d/1q5I8GEraBY63jCZ_LSyE9zXJ1ooS6BZP/view
- FY2025 IFRS results analyst call transcript (2026-03-03): https://drive.google.com/file/d/1O3Y-j1D6YA4X0wz6AmllxM6OkZUDKMDO/view

_Verdict: **miss vs prior year** (net income, EPS, ROE, NIM all down YoY); 2026 guidance points to recovery (RUB 600-650bn net income)._
<!-- /enrichment:earnings_review -->
