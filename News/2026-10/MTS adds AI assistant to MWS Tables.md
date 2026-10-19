---
title: "MTS adds AI assistant to MWS Tables"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/mts
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-10-15_mws_tables_zapustil_ii-assistenta
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s709c4aa3
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# MTS adds AI assistant to MWS Tables

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Добавил в MWS Tables AI-ассистента, который по текстовому запросу создает таблицы, канбан-доски, диаграммы Ганта и бизнес-процессы, настраивает формулы и анализирует данные

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-10-15_mws_tables_zapustil_ii-assistenta>
*262 слов · direct*

Эльяс Касми

 MWS Tables запустил ИИ-ассистента для создания бизнес-приложений на базе таблиц
 
 
 МТС Web Services , входит в ПАО «МТС», объявляет о запуске ИИ-ассистента в сервисе для командной работы MWS Tables. Новый инструмент поможет компаниям быстрее запускать рабочие процессы и снижать трудозатраты на настройку таблиц, канбан-досок , диаграмм Ганта , формул и связей между данными. Об этом CNews сообщили представители МТС .
 ИИ-ассистент позволяет описать задачу естественным языком и получить готовую структуру под конкретный бизнес-процесс. Например, пользователь может написать: «Я хочу вести план-факт по продажам, чтобы данные обновлялись автоматически», – после чего ассистент предложит подходящую конфигурацию рабочего пространства .
С помощью ассистента команды могут создавать шаблоны по описанию, настраивать проектные процессы с задачами, ответственными, сроками и статусами, а также связывать таблицы между собой и задавать расчеты для автоматического обновления значений. Инструмент также работает с уже существующими данными: пользователь может открыть таблицу и задать вопрос, например: «Какие проекты просрочены?» или «У какого направления самые большие расходы?». Ассистент проанализирует данные и поможет оперативно принимать управленческие решения и контролировать отклонения от плана.
«Сегодня бизнесу важно быстро превращать данные в управляемые процессы – от планирования продаж и маркетинговых кампаний до проектного управления и операционного контроля. ИИ-ассистент в MWS Tables снижает порог входа в автоматизацию: пользователю больше не нужно вручную собирать структуру таблиц, настраивать связи и формулы – достаточно описать задачу на естественном языке. Это помогает командам быстрее запускать рабочие процессы , сокращать рутинные операции и принимать решения на основе актуальных данных», – сказал Филипп Герм , директор по продукту MWS Tables.
 Первый в России ИТ-маркетплейс CNewsMarket для Вашего бизнеса. С ценами на ИТ-услуги от сотен поставщиков

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MTS adds AI assistant to MWS Tables
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On **2026-10-15** MTS Web Services (MWS, the IT vertical of PJSC MTS) announced an **AI assistant inside MWS Tables**, its collaborative no-code "tables" service (a Russian Airtable analog). The assistant takes a natural-language prompt and generates a ready structure for a business process: tables, kanban boards, Gantt charts, formulas, data relations; it can also query existing data ("which projects are overdue?", "which direction has the biggest expenses?"). Product director quoted: **Filipp Germ** (dir. of product, MWS Tables). Source: single CNews PR-style note (cnews.ru/news/line/2026-10-15), ~262 words, echoed verbatim by TAdviser, Computerra, Content-Review — i.e. **one MWS press release, syndicated**.

De-PR: this is a **feature add to an existing product, not a launch**. MWS Tables itself has a dated trajectory: cloud SaaS version released **2025-07-16** (with Freemium + Unlimited tiers), no-code platform sales opened 2025-05-15, marketer templates Feb 2026. The AI assistant is the natural-language layer bolted on top of that stack in Oct 2026.
- **Why framed this way → what it reveals:** The release carries **zero traction data** — no users, no paying seats, no conversion, no "x% faster" metric for the assistant itself, no model named (own Cotype? third-party LLM? unstated). Claims are pure capability prose ("lowers the barrier to automation," "describe the task in natural language"). The signature of a **catch-up feature announcement**: the global norm (Airtable Omni, Microsoft Copilot in Excel, Notion AI) is "AI generates your tables/app from a prompt," and MWS is matching it for the import-substituted Russian market. The real question is not "is this novel" (it is not) but "does MWS Tables have enough installed base for an AI layer to matter" — and that base is undisclosed.

## [1] Competitors / peers
**Global prior art, well ahead (2023–2026):**
- **Microsoft Copilot in Excel / M365** — natural-language PivotTables, formulas, charts, the COPILOT() cell function; GA and widely adopted 2024–2025. The canonical "describe it, AI builds the spreadsheet" incumbent.
- **Airtable** — relaunched AI-native June 2025; **Airtable Omni** (conversational app builder that generates tables, interfaces, automations from a prompt) and **Superagent** (Jan 2026). This is the closest functional twin and the explicit product MWS Tables clones.
- **Notion AI**, **Google (Gemini in Sheets)**, **Softr** — adjacent no-code + NL-to-structure players.

**Russian peers (the actual competitive set, post-2022 import substitution):**
- **Yandex** — DataLens + "Нейроаналитик" (NL analytics), YandexGPT; Yandex Tracker on the task side.
- **Sber** — GigaChat Enterprise / SberCloud AI for B2B analytics.
- **Weeek** ("Вика" AI assistant + Notion/Asana/Trello/Jira import), **Kaiten**, **Bitrix24**, TEAMLY, YouGile — domestic task/collab tools, several now with embedded AI.
- **Position of this item: parity-at-best domestically, far behind globally.** MWS Tables is matching Airtable Omni's prompt-to-structure feature ~16 months after Airtable's AI-native relaunch, into a market where Airtable blocks Russian accounts (regulatory tailwind for local clones).
- **Why the lay of the land is this way → second-order:** the Russian no-code/collab space is fragmented and distribution-led, not feature-led — whoever owns the enterprise channel (telco/bank ecosystems: MTS, Sber, Yandex, VK) wins, not whoever ships the cleverest AI. MWS Tables' edge is **not the AI** (commoditized) but MTS's B2B distribution (now bundled under MTS CorpTech) and co-selling with MWS Cloud/MWS AI.

## [2] Company history / fit
MWS Tables sits inside MTS's "telco → digital ecosystem" pivot:
- **2024-12 / 2025-04:** MTS consolidates IT/cloud/AI assets into **MWS** (>10,000 staff, 100+ services); MTS AI → MWS AI.
- **2025-05-15:** MWS Tables no-code platform sales open; **2025-07-16:** cloud SaaS version (Freemium/Unlimited); **2026-02:** marketer templates; **2026-10-15:** AI assistant.
- Sibling AI moves same month: [[MTS adds dialog-based agent creation to MWS AI Agents Platform]] (2026-10-16 — same "describe in a chat, the system builds it" AI-Force paradigm, applied to agent-building), [[MWS AI opens RESON speech-recognition model evaluation tool]], [[Danila Dyugurov named head of MWS Cloud]] (2026-10-13), all cross-sold under [[MTS bundles enterprise solutions under MTS CorpTech brand]] (2026-10-12).
- MWS FY2025 revenue ₽63.8bn, external +53%; MWS AI external +60–71%; group FY2025 ₽807.2bn (+14.7%), targeting ₽1trn by 2028; MWS is a named IPO candidate.
- **Why MTS acts this way:** low-single-digit telecom growth forces MTS to manufacture a high-growth "software" story to earn a re-rating and float subsidiaries. A productivity-SaaS with an AI layer is a cheap, on-trend way to broaden the MWS SMB/enterprise surface and feed the "AI across the whole stack" narrative — the **same AI-Force/NL-to-structure pattern is being replicated across every MWS product this fortnight** (Tables, AI Agents Platform), which is the real tell: this is a platform-wide AI reskin, not a Tables-specific breakthrough.

## [3] Novelty / value-add / traction
**Not new.** Prompt-to-tables/kanban/Gantt and "ask your data" are standard in Copilot/Excel, Airtable Omni, Notion AI since 2024–2025. For the **Russian** market it is incremental and timely (Airtable blocks RU accounts; local demand for a substitute), but still a **catch-up feature on an existing product**, not a first.
- **Traction = none disclosed.** No user/seat count for MWS Tables, no adoption of the assistant, no model disclosed, no latency/accuracy/time-saved metric. "Announced," not "proven." Everything is capability prose.
- **Why the value-add is thin, deeper:** the AI layer is commoditized — any LLM over a table schema does this, so it confers no durable moat; the margin/value in no-code lives in **data gravity + switching costs of the installed base**, not in the NL feature. MWS does not disclose that base, so we cannot tell whether the assistant sits on a real platform or a thin one. Second-order: if the underlying model is a third-party LLM, unit economics (inference cost per generated workspace) and data-governance (where prompts/data route) are unaddressed — both are the real questions a serious buyer asks, and both are silent.

## [4] What's next / market sentiment
Expect MWS to keep replicating the NL-to-structure / "AI-Force" pattern across the MWS suite and cross-sell via MTS CorpTech + MWS Cloud/AI; the import-substitution tailwind (foreign SaaS exit, Airtable RU blocks, data-localization FZ-242) remains the main structural driver. Regulatory backdrop favors domestic no-code; competitive pressure comes from Yandex, Sber, VK and nimble locals (Weeek/Kaiten) shipping comparable AI helpers.
- **Why / counterintuitive:** the tailwind that makes this easy (foreign-SaaS vacuum) also makes the feature undifferentiated — **everyone ships the same AI assistant**, so the market consolidates on distribution and ecosystem lock-in, not features. For MTS the second-order payoff is narrative (feeding the MWS IPO/"tech company" re-rating), not near-term P&L — this single feature moves no needle on its own; its weight is as one data point in a platform-wide AI push.

## Sources
Primary (note): cnews.ru/news/line/2026-10-15_mws_tables_zapustil_ii-assistenta. MWS Tables timeline: mws.ru/news (cloud version 2025-07-16; Freemium/Unlimited), cnews.ru 2025-05-15 (sales open), mws.ru 2026-02 (marketer templates), mws.ru/blog "MWS Tables — гид по российскому аналогу Airtable". Prior art: airtable.com/platform/ai (Omni, AI-native June 2025; Superagent Jan 2026), techcommunity.microsoft.com (COPILOT in Excel), datacamp.com Excel Copilot tutorial. RU peers: habr.com (map of RU AI analytics platforms), weeek.net (Вика AI), corpblog.ostrovok.ru (RU task-trackers 2026). Internal: [[MTS adds dialog-based agent creation to MWS AI Agents Platform]], [[MWS AI opens RESON speech-recognition model evaluation tool]], [[Danila Dyugurov named head of MWS Cloud]], [[MTS bundles enterprise solutions under MTS CorpTech brand]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_Red-team / challenge questions — answered from sources or marked "open". English._

1. **Is this a product launch or a feature add?** Feature add. MWS Tables already existed (cloud SaaS since 2025-07-16; sales since 2025-05-15); this is only the NL/AI layer on top (2026-10-15).

2. **Is the capability new anywhere?** No — prompt-to-tables/kanban/Gantt and "ask your data" are standard in Microsoft Copilot in Excel (2024–25), Airtable Omni (AI-native June 2025), Notion AI, Gemini in Sheets. Global prior art is ~1.5 years ahead.

3. **Is it new for the Russian market?** Partly — a timely domestic substitute as Airtable blocks RU accounts and foreign SaaS exits, but Yandex (DataLens/Нейроаналитик), Sber (GigaChat), Weeek ("Вика"), Kaiten offer comparable local AI helpers. Parity at best, not a first.

4. **What traction is disclosed?** None. No user/seat count, no paying customers, no assistant-adoption figure, no "x% faster" metric. Announced, not proven. (open)

5. **Which model powers the assistant — own or third-party?** Not stated in the release. MWS AI has an own model (Cotype), but the note doesn't confirm it drives Tables. (open)

6. **What are the unit economics (inference cost per generated workspace)?** Silent. If a third-party/large LLM, per-prompt cost vs Freemium (free up to 3 users) is unaddressed. (open)

7. **Where do prompts and business data route (data governance)?** Not stated — material for enterprise buyers given data-localization rules. (open)

8. **How big is the MWS Tables installed base the AI sits on?** Undisclosed. MWS Tables' absolute revenue/users are not broken out; can't tell if the AI sits on a real platform or a thin one. (open)

9. **Single-source risk?** Yes — one CNews PR note syndicated verbatim by TAdviser/Computerra/Content-Review; all trace to one MWS press release.

10. **Does it move MTS/MWS P&L?** Negligibly on its own. MWS FY2025 ₽63.8bn; this is one feature in a multi-product suite. Weight is narrative, not revenue.

11. **Is accuracy/quality of generated structures verified?** No independent test; no accuracy/error metric. Prompt-to-structure quality is the actual make-or-break and is unaddressed. (open)

12. **Is this part of a broader pattern?** Yes — same fortnight, the MWS AI Agents Platform got the same "describe it in a chat, AI builds it" paradigm (AI-Force, 2026-10-16). This is a platform-wide AI reskin, not Tables-specific.

13. **Does it duplicate any existing corpus note?** No. No prior note covers MWS Tables or its AI assistant. Nearest siblings (MWS AI Agents Platform, MWS Cloud, CorpTech) are distinct products/events. → FRESH.

14. **Where is the real moat?** Not the AI (commoditized) — it's MTS's B2B distribution (MTS CorpTech bundling) + data gravity/switching costs of the Tables base. The feature itself confers no durable edge.

15. **What would make this matter more?** Disclosed adoption of Tables + the assistant, a named model with governance, and measurable time-saved — none present.

**Freshness / duplicate verdict:** FRESH. Genuine new development (AI assistant shipped into MWS Tables, 2026-10-15); not a reprint or re-framing of any existing corpus note. But low-substance: a catch-up feature on an existing product, globally common since 2024–25, with zero disclosed traction, no model/economics, single-source PR.

**Importance: 2/5 — rationale.** A real, dated product-feature announcement from a top-3 Russian telecom's IT arm, strategically coherent (import-substitution + the MWS "AI across the stack" / IPO narrative). But: no novelty (standard since Copilot/Airtable Omni), no disclosed traction/users/economics, no model named, single syndicated PR source, and it moves no P&L on its own. One data point in a platform-wide AI reskin, not a standalone event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** MWS Tables sits in the Russian cloud-collaboration / low-code "work-OS" subvertical (airtable-style tables + kanban + Gantt + formulas), now bolting on a natural-language AI assistant that generates structures from a prompt. No clean TAM figure for this niche is publicly verifiable — "no data"; what is sourced is the parent cloud/AI engine: MWS (MTS Web Services) group revenue was ₽63.8bn for FY2025 (external revenue +53%, MWS Cloud +40%, MWS AI +60%, per MWS/tbank-invest reposts), and Q2 2026 revenue ₽15bn with external revenue +18% and MWS Cloud +20% (per AKM / CNews, 2026-08-25). Structure: fragmented and crowded — the collaboration layer competes with Yandex 360, VK WorkSpace, Bitrix24, R7-Office, plus pure-play work-OS tools Kaiten and Weeek, most of which already ship their own AI copilots (BitrixGPT/CoPilot, Kaiten AI). Entry barriers are low on the app surface (many lookalikes) but high underneath: the real moat is owning the cloud + proprietary LLM stack, which MWS does via MWS Cloud + MWS AI (Cotype models, GPT Model Hub). Why now: (i) import-substitution vacuum after Western SaaS exits (note that Miro blocked Russian users in Oct 2026 — see internal comp), pulling demand to domestic collaboration tools; (ii) generative-AI shift making NL→structure a cheap feature to differentiate on. (analysis)

**Competitive landscape.** Sector KPIs for a SaaS collaboration suite: paying organizations/seats, ARPU, NRR, attach of AI feature to base — none disclosed for MWS Tables specifically → [UNSOURCED]. Players & basis of competition: Yandex 360 (H1 2026 revenue ₽11.6bn, +42% YoY; >185k organizations; 117m MAU, per Yandex 360 blog / AKM) competes on ecosystem breadth and distribution; Bitrix24 on all-in-one CRM+portal+AI; Kaiten/Weeek on focused project-management UX; R7-Office (FY revenue ~₽3.3bn, per TAdviser) and the struggling MyOffice (see internal comp — near-₽9bn loss) compete on document editing and the state-procurement mandate (P7-Office ~61.6% of government software purchases vs MyOffice ~19.2%, per TAdviser gov data). Recent peer moves: R7-Office embedded into Yandex 360 and VK WorkSpace (2025 partnership); MTS itself bundled connectivity+cloud+AI+IIoT under "MTS CorpTech" (2026-10-12, internal comp). MWS Tables' position: catching up / niche feature-parity play — the AI assistant matches, not leapfrogs, incumbents' copilots. Moat is not the Tables UI but the vertically-integrated MWS cloud+own-LLM stack and MTS's B2B distribution (CorpTech). (analysis)

**Comps & multiples.** No valuation, round, or standalone revenue is attached to MWS Tables → product launch, not a deal; EV/Revenue, EV/EBITDA, P/E all "no data" at the product level. Parent-level anchor (sourced): MTS Group Q2 2026 revenue ₽213.5bn (+9.2% YoY), OIBDA ₽84.6bn (+16.3%), per Telecompaper — MWS's ~₽15bn quarterly revenue is roughly 7% of group revenue (₽15bn / ₽213.5bn ≈ 7.0%), i.e. still a small, high-growth segment inside a telco. Growth-vs-multiple cross-check not applicable (no public segment multiple). Internal comps (grep fallback, semsearch 402): [[MyOffice reports nearly 9bn rouble loss]] (domestic office-software economics are ugly — a cautionary peer on monetization), [[MTS bundles enterprise solutions under MTS CorpTech brand]] (the B2B distribution wrapper this product rides), [[MWS Cloud launches fastest S3 storage for ML workloads]] and [[MWS AI opens RESON speech-recognition model evaluation tool]] (the cloud+AI engine underneath), [[Miro blocks Russian users' access to accounts and site]] (the demand-side import-substitution catalyst). Distribution not computed (no ≥3 comparable multiples) — qualitative comparison only.

**Risk flags.**
1. Commoditized feature, not a moat — NL-to-structure AND kanban/Gantt/formulas already ship in Bitrix24, Kaiten, Weeek and (adjacent) Yandex 360; MWS Tables is reaching parity, so the "assistant" alone is unlikely to shift share. Second-order: differentiation has to come from price/bundling, compressing margin.
2. Weak domestic-office-software economics — MyOffice's near-₽9bn loss and MyOffice/R7 layoffs/restructuring signal that even a protected, Western-vacated market struggles to monetize productivity software; MWS Tables risks the same low willingness-to-pay outside mandated buyers.
3. Dependence on the MWS AI/cloud stack and MTS distribution — the product's value is captured mostly by the underlying LLM+cloud layer and CorpTech sales motion, not the Tables app; standalone it has little pricing power, and any slowdown in MWS Cloud/AI growth (Cloud decelerated from +40% FY25 to +20% in Q2 2026, per AKM/CNews) pressures the whole workspace story.

**What this changes (idea-lens).** Incremental, not a re-rating: this is MWS stitching a horizontal AI copilot across its growing collaboration surface to deepen the CorpTech bundle and raise switching costs, riding the post-Miro/post-Western-SaaS substitution wave. Falsifiable thesis: if MWS Tables (and MWS collaboration tools broadly) are genuinely winning share, MTS should start disclosing paying-organization or seat counts and segment ARPU within 2–3 quarters, the way Yandex 360 discloses >185k orgs / ₽11.6bn. Thesis breaks if the AI assistant stays a checkbox feature with no disclosed adoption metric and MWS revenue growth keeps decelerating. Watch: MWS Q3 2026 release and any Tables/collaboration usage metric. (analysis)

Sources: https://www.akm.ru/eng/news/mts-web-services-external-revenue-increased-by-18-in-the-second-quarter/ · https://www.cnews.ru/news/line/2026-08-25_mts_web_services_uvelichila_vneshnyuyu · https://www.telecompaper.com/news/mts-group-revenues-up-9-in-q2--1580761 · https://360.yandex.com/blog/news/bolee-185-tis-organizatsii-yandeks-360-obyavlyaet-finansovie-rezultati-za-pervoe-polugodie/ · https://www.akm.ru/eng/news/revenue-of-yandex-b2b-tech-in-two-key-areas-increased-by-53-in-the-first-half-of-the-year-in-accorda/ · https://tadviser.com/index.php/Company:P7-Office_(formerly_New_Communication_Technologies,_NKT) · https://tadviser.com/index.php/Article:Office_Software_(Russian_Market) · MTS IR Q1 2026 press release (drive_url): https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** CONTEXT-ONLY — no earnings in this news. The item is a product announcement (an AI assistant inside MWS Tables), not a results print, so there is no revenue/EPS to score. But MTS is IR-covered, and MWS Tables is a MTS Web Services (MWS) product, so the relevant financial backdrop is MWS's own segment trajectory: MWS external revenue +18% YoY in Q2 2026, with MWS Tables' external SaaS audience up 4x YoY — this feature ships into an accelerating, AI-led segment.

**MWS segment context (the unit that owns this product).** From the MWS Q2 2026 release (period ended Jun-2026): MWS company revenue RUB 15.0bn; external revenue +18% YoY. Growth led by AI and cloud: MWS AI external revenue +71% YoY, MWS Cloud revenue +20% YoY, cybersecurity external revenue +53% YoY. MWS Tables specifically: external SaaS audience grew 4x (fourfold) YoY — so the AI-assistant launch targets the fastest-adopting SaaS line in the segment. Prior quarter (Q1 2026) for reference: MWS revenue RUB 14.0bn (-5.1% YoY on a reporting-perimeter basis) but external revenue +46% YoY and MWS Cloud +44% YoY — i.e. external monetization was already accelerating before this launch.

**MTS Group context (the IR-covered parent).** Latest group print, Q2 2026 (ended Jun-2026): revenue RUB 213.5bn (+9.2% YoY); OIBDA RUB 84.6bn (+16.3% YoY); net profit RUB 66.9bn vs RUB 2.8bn a year earlier (~24x, flattered by lower financing expense and a stake disposal — a non-operating, largely one-off driver, not core operating leverage). Mobile subscribers 84.1mn; CapEx +21.6% YoY. The near-term earnings quality here is low: the net-profit jump is financing- and disposal-led, not a sign the digital/B2B build-out is yet profit-accretive.

**By segment / driver.** MWS (ex-cloud "digital/B2B tech" cluster) is the strategic growth leg MTS is spinning up, and within it AI (+71%) and cloud (+20%) are the pull. MWS Tables sits in the applied-SaaS layer; the AI assistant (natural-language creation of tables/kanban/Gantt, formula setup, data Q&A) is a feature add aimed at lowering activation friction and lifting the 4x-growing external SaaS base — plausibly ARPU/retention-accretive, but no disclosed MWS Tables revenue line to size it.

**vs expectations / prior period.** Not applicable — no consensus or whisper exists for a product-feature launch, and the news carries no period figures. Segment momentum vs prior quarter: MWS external revenue decelerated from +46% YoY (Q1 2026) to +18% YoY (Q2 2026); MWS Cloud from +44% to +20% — strong but off a fast start and now lapping tougher comps. Group OIBDA growth (+16.3% YoY) still outpaces revenue (+9.2% YoY), i.e. positive operating leverage at the consolidated level. [Consensus for MWS: no public data — private segment of a listed parent.]

**Guidance / forward.** No guidance in this news; none tied to MWS Tables. MTS's broader 2026 posture (per results commentary) leans on the digital/B2B (MWS) and adtech verticals as growth drivers while the core telecom base grows high-single-digit. Independent read (analysis): expect MWS to stay a double-digit external-revenue grower into H2 2026, with AI the headline multiple, but the launch itself is immaterial to group revenue near term — it is a positioning/retention move, not a reported-results event.

**Thesis-flags.**
1. Signal, not scale (analysis): the AI assistant deepens MWS Tables' AI narrative and feeds the 4x-growing external SaaS base → supports the "MTS is a tech/AI company, not just a telco" re-rating thesis → but contributes no disclosed revenue, so it moves sentiment more than near-term numbers.
2. Deceleration to watch: MWS external revenue +46%→+18% and Cloud +44%→+20% QoQ-comparable YoY → decelerating off high bases → if the slide continues, the standalone-MWS/IPO-optionality narrative (a key MTS value lever) loses momentum regardless of product cadence.
3. Earnings quality at the parent: Q2 2026 net profit ~24x YoY is financing/disposal-driven, not operating → investors crediting MTS for "profit inflection" on the back of digital should discount the one-offs; the MWS feature launch does nothing to change that near term.

Sources: MWS Q2 2026 release (https://mws.ru/news/mts-web-services-uvelichila-vneshnyuyu-vyruchku-na-18-vo-vtorom-kvartale-2026-goda/) · MTS Q1 2026 press release, IR drive (https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf) · MTS Q2 2026 group figures via Telecompaper/TelecomLead · CNews MWS Q2 coverage (https://www.cnews.ru/news/line/2026-08-25_mts_web_services_uvelichila_vneshnyuyu). MWS Tables standalone revenue: no data (not disclosed). Public consensus for MWS/MTS digital segment: no data.
<!-- /enrichment:earnings_review -->
