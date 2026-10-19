---
title: "MTS adds dialog-based agent creation to MWS AI Agents Platform"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/mts
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://ai.cnews.ru/news/line/2026-10-16_mws_ai_nauchila_platformu_ii-agentov
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sbddeaaaf
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# MTS adds dialog-based agent creation to MWS AI Agents Platform

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Внедрил в платформу MWS AI Agents Platform создание AI-агентов через диалог, поиск информации в сканах документов и изображениях, общую память корпоративных правил, конструктор чат-виджетов для сайтов и инструменты анализа работы агентов

## Первоисточники

### ai.cnews.ru
<https://ai.cnews.ru/news/line/2026-10-16_mws_ai_nauchila_platformu_ii-agentov>
*416 слов · direct*

Дмитрий Степанов
MWS AI научила платформу ИИ-агентов читать сканы, запоминать правила компании и помогать в создании агентов
 MWS AI (входит в « МТС Web Services ») обновила MWS AI Agents Platform — платформу, на которой компании могут создавать и запускать собственных корпоративных ИИ-агентов. Ключевые обновления затрагивают проектирование , запуск и контроль работы созданных решений на базе платформы. В версии 4.0 обновлен модуль «ИИ-команда» (AI Force), который помогает создавать агентов в режиме диалога с пользователем, а также реализованы инструменты для создания интерфейсов с ИИ-агентами на сайтах компаний, просмотра логов пользовательских сессий и поиска информации по отсканированным документам и изображениям. 
Обновленный модуль «ИИ-команда» ( AI Force) берет на себя часть работы по созданию ИИ-агентов. Пользователю достаточно описать в свободной форме во встроенном чате платформы, что должен уметь агент, а «ИИ-команда» задаст уточняющие вопросы, поможет сформулировать требования и предложит cпособ реализации, который можно скорректировать вручную. Кроме того, на платформе появился раздел «Интерактивное обучение» с тренажёром по работе с конструктором бизнес-сценариев — его можно использовать параллельно с работой над агентом в формате второго окна. Обновления помогают пользователям быстро приступить к созданию агента, осваивая возможности платформы по ходу работы.
На платформе также появился конструктор чат-виджетов, с помощью которых компании могут размещать на своих сайтах окно диалога с ИИ-агентом . Через виджет посетители сайта могут взаимодействовать с агентом — например, задать ему вопрос о продуктах и услугах организации или получить помощь с их выбором. Пользователь настраивает внешний вид чат - виджета в платформе и получает готовый фрагмент кода для его размещения на странице.
В новом разделе « Логи » теперь можно просматривать диалоги пользователей с агентом. Сессии можно фильтровать по периоду, версии, каналу, длительности и наличию ошибок. Внутри каждой сессии видны шаги диалога и причина сбоя. Это помогает владельцу продукта или сервиса найти этап, на котором агент прерывает обработку запроса.
Поиск по подключенной базе знаний компании теперь учитывает текст в отсканированных PDF-документах и изображениях. Для распознавания платформа использует собственную модель Cotype , которая работает с текстом и изображениями ( VLM ). Благодаря этому теперь можно находить информацию в сканах инструкций, актов и технических документов и использовать ее в ответах на вопросы пользователей. Возможности работы с другими моделями также сохранены.
Изменения коснулись и памяти агента на двух уровнях: личный профиль пользователя дополнен общим профилем организации. Регламенты, правила и актуальные договоренности вносятся в профиль организации один раз и учитываются в ответах любому сотруднику.
Платформа MWS AI Agents Platform доступна для развертывания на серверах заказчика и в частном облаке .
 Почём сегодня объектное хранилище на 2 000 Гб? Предложения десятков поставщиков ― на ИТ-маркетплейсе CNewsMarket

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MTS/MWS AI adds dialog-based agent creation to MWS AI Agents Platform (v4.0)
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
MWS AI (the AI arm of MTS Web Services) shipped **v4.0** of its MWS AI Agents Platform — the corporate platform companies use to build/run their own AI agents, deployable on-prem or in a private cloud. This is an **incremental feature release, not a new product**. The de-PR'd deltas:
- **AI Force ("ИИ-команда") now builds agents conversationally:** the user describes in free text what the agent should do; the module asks clarifying questions, drafts requirements and proposes an implementation the user can hand-edit. Plus an "Interactive learning" trainer (a sandbox tutorial for the business-scenario builder running in a second window).
- **Chat-widget builder:** configure a chat window in-platform, get a code snippet to embed the agent on a company website.
- **Session logs:** filter dialog sessions by period/version/channel/duration/errors; see dialog steps and failure cause.
- **Knowledge-base search now reads scanned PDFs and images** via MWS AI's own **Cotype VLM** (OCR/vision); other models still usable.
- **Two-level memory:** per-user profile now joined by an **org-wide profile** (regulations/rules/agreements entered once, applied to all employees' answers).

**Why framed this way / what it reveals:** the headline MTS/ai.cnews framing is "taught the platform to read scans, remember rules, help create agents" — a bundle of QoL features dressed as a milestone. The real center of gravity is **AI Force conversational authoring**, which is the catch-up move to global agent-builders (see [1]). No pricing, no client count, no adoption metric is disclosed — classic "capability announced, traction withheld." This is lowering the skill floor for a no-code tool that already existed, not a step-change in what agents can do.

## [1] Competitors / peers
Conversational/no-code agent authoring is **late-mover territory**, not novel:
- **Global:** OpenAI **AgentKit / Agent Builder** (Oct 2025, drag-and-drop + chat), **Microsoft Copilot Studio** (low-code topics, 1,000+ connectors, enterprise governance), **Google Gemini Enterprise Agent Platform**, **Salesforce Agentforce**, **ServiceNow AI Agents**. Describe-in-plain-language agent creation is table stakes in these by 2025–26.
- **Russian direct peers (the relevant battlefield, given on-prem/sovereignty needs):**
  - **Sber GigaChat Enterprise** (March 2026, local/cloud/hybrid, access control + moderation) and, crucially, **Sber GigaPlatform AI Studio** — a **free** no-code agent builder launched ~Oct 14, 2026, days before this MTS release.
  - **Yandex** (YandexGPT / AI Studio) as the third sovereign-cloud contender.

**Position:** MTS is **at parity / catching up** on features, not ahead. **Why the lay of the land is this way:** the Russian enterprise-AI race is a three-way sovereign-cloud fight (MTS/MWS vs Sber vs Yandex) where the moat is **data residency + on-prem deployment + own models** (Cotype here), not the authoring UX itself. Second-order: with Sber offering a **free** no-code studio the same week, MTS's differentiation can't be "easier to build" — it has to be deep enterprise deployment (private cloud, own VLM, org memory), which is exactly what v4.0 leans into.

## [2] Company history / fit
MWS AI Agents Platform timeline: **launched Dec 2025**; **March 2026** added any-LLM support (GigaChat, YandexGPT, ChatGPT, Claude, DeepSeek); **Sept 2026** added code-execution sandbox, scheduled/autonomous runs, cross-session memory; **Oct 2026 = v4.0** (this release). MTS reportedly invested **~₽4bn** into the platform. It sits inside a broader MWS/MTS enterprise push: MTS CorpTech brand consolidation (Oct 2026), MWS Tables AI assistant (Oct 2026), RESON ASR-eval tool (Oct 2026), MWS Cloud leadership change (Oct 2026). See [[MTS bundles enterprise solutions under MTS CorpTech brand]], [[MTS adds AI assistant to MWS Tables]], [[MWS AI opens RESON speech-recognition model evaluation tool]], [[Danila Dyugurov named head of MWS Cloud]].

**Why MTS acts this way:** telco core (connectivity) is a commodity take-rate business; MTS is pushing into B2B cloud + AI to earn a software/platform multiple and defend enterprise accounts via a one-vendor stack (CorpTech). The cadence of near-monthly updates signals a land-grab for corporate AI budgets before Sber/Yandex lock in defaults.

## [3] Novelty / value-add / traction
**Genuinely new?** No — conversational agent authoring, embeddable chat widgets, session logs and VLM-based doc search all exist elsewhere. The one plausibly distinctive element is **Cotype as an in-house VLM** doing scan/image search inside a sovereign, on-prem-deployable stack (vs relying on a foreign model). **Org-level shared memory** is a sensible but not unique enterprise feature.

**Is the value-add real? (deeper):** the value is **real but marginal** — it lowers the no-code floor and adds enterprise plumbing. **Who captures the margin:** the margin sits with whoever owns the **deployment + model + data** layer, not the authoring UI, which is commoditizing fast (Sber giving it away free). So MTS's defensible value is private-cloud/on-prem + Cotype, not AI Force. **Traction: unverified — zero disclosed clients, agent counts, or revenue.** Per the anti-PR gate, "announced ≠ adopted." Treat as capability, not proof of uptake.

## [4] What's next / market sentiment
Expect continued near-monthly feature cadence (orchestration, multi-agent, deeper CorpTech bundling) as MTS races Sber's GigaChat Enterprise/GigaPlatform and Yandex for sovereign enterprise-AI share. **Why the market goes this way:** Russian regulation + sanctions make **data-sovereign, on-prem, own-model** stacks the durable requirement; foreign agent-builders (OpenAI/Microsoft/Google) are largely off the table for regulated RU enterprises, so the real contest is MTS vs Sber vs Yandex. **Counterintuitive second-order:** commoditization of the no-code authoring layer (Sber free) means feature releases like this **won't move competitive position** — the fight will be decided by deployment economics, model quality (Cotype vs GigaChat), and ecosystem lock-in, not by who adds "describe your agent in chat." Risk: feature parity with no traction disclosure suggests the platform is still pre-scale.

## Sources
- ai.cnews.ru, 2026-10-16 — primary (note body).
- mts.ai; tadviser.ru / tadviser.com (MWS AI Agents Platform product page, ₽4bn, timeline); ict.moscow (Dec 2025 launch); bytemag.ru; www1.ru (2026-10-17).
- OpenAI AgentKit/Agent Builder, Microsoft Copilot Studio, Google Gemini Enterprise (external comparisons).
- Sber GigaChat Enterprise (ixbt.pro, March 2026); Sber GigaPlatform AI Studio free no-code (www1.ru, 2026-10-14).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is conversational agent creation actually new?** No — OpenAI Agent Builder (Oct 2025), Copilot Studio, Gemini Enterprise all do "describe your agent in plain language." MTS is a late mover. (answered)
2. **Is it new within Russia?** Sber GigaPlatform AI Studio (free no-code agent builder) launched ~Oct 14, 2026 — days before this; Sber GigaChat Enterprise since March 2026. MTS is at parity, not first. (answered)
3. **Is v4.0 a new product or an incremental release?** Incremental — platform launched Dec 2025; this is a feature bundle on an existing product. Not a milestone. (answered)
4. **Any adoption/traction numbers?** None disclosed — no client count, no agents built, no revenue. "Announced ≠ adopted." (open — the decisive gap)
5. **What is genuinely differentiated?** The in-house **Cotype VLM** for scan/image KB search inside an on-prem/private-cloud sovereign stack; org-level shared memory. Everything else is parity. (answered)
6. **Who captures the margin in this stack?** The deployment+model+data layer, not the authoring UI — which Sber is giving away free. Authoring is commoditizing. (analysis)
7. **Does lowering the no-code floor change competitive position?** Likely no — if authoring is free/ubiquitous, the fight shifts to deployment economics and model quality. (hypothesis)
8. **Is the ₽4bn investment figure corroborated?** Reported via tadviser/axioma-ai (June 2026 context), not in the primary note; treat as secondary. (open)
9. **How good is Cotype as a VLM vs GigaChat/foreign VLMs?** No benchmark disclosed. Unverifiable. (open)
10. **Is "org-wide memory" a security/governance risk?** Shared regulations applied to all employees' answers — raises access-control/leakage questions not addressed in PR. (open)
11. **Does any-LLM support (incl. Claude/ChatGPT) actually work on-prem for RU clients?** Foreign models are typically API-gated/sanctions-exposed; sovereign clients likely confined to Cotype/GigaChat. (analysis)
12. **Why the near-monthly feature cadence?** Land-grab for corporate AI budgets before Sber/Yandex set defaults; signals pre-scale product racing for mindshare. (analysis)
13. **Is this a duplicate of other MWS Oct-2026 notes?** No — distinct product vs RESON (ASR eval), MWS Tables (spreadsheet assistant), CorpTech (brand bundle). Fresh. (answered)
14. **What's the realistic ceiling?** Capped by RU enterprise-AI TAM split three ways; differentiation must be deployment/model, not UX. (hypothesis)
15. **Does the headline overstate?** Yes — "taught the platform to read scans / help create agents" dresses QoL features as a breakthrough; real delta is modest. (answered)

Importance: 2/5 — Incremental v4.0 feature bundle on an existing (Dec 2025) platform; conversational/no-code agent authoring is global and even Russian prior art (Sber, days earlier). No traction disclosed. Mildly notable only as a data point in the three-way MTS/Sber/Yandex sovereign enterprise-AI race and for the in-house Cotype VLM angle. Fresh (not a duplicate), but low weight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** MWS AI Agents Platform v4.0 sits in the enterprise agentic-AI / no-code-agent-builder subvertical. Sizing is analyst-dependent and should be read as a range, not a point: the global agentic-AI market is put at ~$19.3bn for 2026 at ~40% growth, the enterprise-specific agentic-platform slice at ~$5.4–9.9bn, and the no-code AI-platform segment at ~$4.7–8.6bn for 2026 (per MarketsandMarkets, Grand View, Fortune Business Insights, via secondary citations, as of Oct 2026; wide variance = definitional, so no single TAM is reliable — treat as "high-growth, poorly-bounded"). Structure: fragmented and early, two layers of value capture — global hyperscaler suites (Microsoft Copilot Studio, Salesforce Agentforce) vs. local/sovereign stacks; in RU the barrier is less technology than data-residency + import-substitution, which is exactly the moat MWS leans on (on-prem + private-cloud deployment, own Cotype VLM). Why now: the shift from "chatbots" to "describe-it-and-it-builds-the-agent" (natural-language agent authoring) is the 2026 product frontier — Copilot Studio ships the same "describe what you need in NL" pattern MWS just added as AI Force v4.0, so MWS is tracking the global roadmap on a lag, not leading it.

**Competitive landscape.** Sector runs on: active-agents / agents-built, seats or consumption (token/credit) billing, and attach to the underlying cloud/LLM spend. Key players: globally Microsoft Copilot Studio (160k orgs, >400k custom agents in its first 90 days — a scale MWS cannot approach) and Salesforce Agentforce ($800M ARR, +169% YoY); domestically the direct RU peers are [[Sber adds BPMN generation to Giga Agentic RPA platform]] (text-to-BPMN agentic RPA) and [[VK launches VK Data Catalog with AI-agent access]] (MCP-based agent access to a data catalog), both shipped the same week (Oct 13–19 2026). Basis of competition in RU: not price but distribution (bundling into existing MTS/Sber/VK enterprise relationships — cf. [[MTS bundles enterprise solutions under MTS CorpTech brand]]) and sovereignty/compliance. MWS position: a fast follower on features, ahead domestically on vertical integration (own VLM Cotype for scanned-doc search, own cloud, on-prem option). Moat = switching costs + distribution inside the MTS B2B stack, not product uniqueness `(analysis)`.

**Comps & multiples.** No deal/round/valuation attached to this product news, so trading multiples are not computable here. External revenue anchors for the two global comps: Agentforce ~$800M ARR (+169% YoY) — a standalone growth line, no clean public EV/Rev at the product level, so "no data" on multiple; Copilot Studio revenue not separately disclosed inside Microsoft, so `[UNSOURCED]`. Internal RU comps are product launches, not priced deals — comparison is qualitative only (distribution not computed). **In-house IR grounding for the parent/segment:** MWS (MTS Web Services, the unit housing MWS AI) posted FY2025 revenue of 63.8bn RUB with external revenue +53% and MWS AI +60% YoY; Q1 2026 MWS revenue ~14bn RUB and Q2 2026 ~15bn RUB, with MWS AI external revenue +71% in Q2 2026 (per MWS/AKM releases + MTS IR; MTS Q1 2026 results published 2026-05-20, https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf). Arithmetic caveat: 71% external growth on a sub-segment off a small base is not yet a market-cap-moving number for group MTS — the AI line is strategically loud, financially small.

**Risk flags.**
1. Feature parity, not differentiation — NL agent authoring, chat-widget builder, session logs are table-stakes that Copilot Studio/Agentforce already ship; MWS competes on sovereignty/distribution, so the moat erodes the moment a global peer is re-admitted or a local peer (Sber/VK/Yandex) bundles harder. Second-order: pricing power stays weak, revenue rides on cloud attach not the agent product itself.
2. Reliance on own-model quality (Cotype VLM for scanned-doc understanding) — if OCR/VLM accuracy lags, the headline "read scans + remember company rules" claim degrades silently; the release is silent on accuracy benchmarks (de-PR: announced capability ≠ measured quality).
3. Monetization opacity — MWS AI's +60–71% growth is off an undisclosed small base; the news discloses no seats, no priced SKUs, no customer count for the platform, so traction is unverifiable and the segment remains a strategic cost center risk for group OIBDA.

**What this changes (idea-lens).** Incremental, not a re-rating: this is the RU agentic-platform field converging on the global "describe-to-build" UX in a single week (MWS, Sber, VK) `(analysis)` — a land-grab for enterprise distribution ahead of consolidation, not a new economic model. Watch for the first disclosed platform KPI (paying orgs / agents-in-production) or Cotype VLM benchmark — that would be the trigger separating a real franchise from a feature checklist; absence of any such metric through the next MTS IR cycle would falsify the "emerging franchise" thesis.

Sources: https://ai.cnews.ru/news/line/2026-10-16_mws_ai_nauchila_platformu_ii-agentov · https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf · https://mws.ru/news/mts-web-services-uvelichila-vneshnyuyu-vyruchku-na-18-vo-vtorom-kvartale-2026-goda/ · https://www.akm.ru/eng/news/mts-web-services-external-revenue-increased-by-18-in-the-second-quarter/ · https://www.marketsandmarkets.com/Market-Reports/agentic-ai-market-208190735.html · https://www.fortunebusinessinsights.com/no-code-ai-platform-market-110382 · https://smartbridge.com/salesforce-agentforce-vs-microsoft-copilot-studio-2026-comparison/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (CONTEXT-ONLY — no earnings in this news).** The item is a product release (MWS AI Agents Platform v4.0 — dialog-based agent creation, scanned-doc search, org-level memory, chat-widget builder), not a financial report. Parent MTS is IR-covered, so for financial context: MTS Group most recent print is **Q2 2026** (reported 2026-08-25) — **BEAT / strong**: revenue RUB 213.5bn (+9.2% YoY), OIBDA RUB 84.6bn (+16.3% YoY), net profit RUB 66.9bn (+23.9x YoY, flattered by a tower-business disposal gain). The platform sits inside **MTS Web Services (MWS)**, the group's fastest-growing unit.

**Key figures — MTS Group Q2 2026 (reported 2026-08-25).**
- Revenue: **RUB 213.5bn, +9.2% YoY**. Telecom service revenue +12.2% YoY to RUB 136.8bn; RU subscriber base 84.1mn.
- OIBDA: **RUB 84.6bn, +16.3% YoY**; OIBDA margin ~39.6% (margin expanded as OIBDA outgrew revenue — operating leverage).
- Net profit: **RUB 66.9bn, +23.9x YoY** — magnified by the gain on the tower-business sale plus lower finance costs; not an organic run-rate.
- Net debt: **RUB 474.1bn**; net debt / LTM OIBDA **1.6x**, down 0.1x vs Q2 2025 (deleveraging, partly disposal-funded).

**By segment / driver — MWS (the unit that ships this product).** MWS Q2 2026 revenue **RUB 15bn**, external revenue **+18% YoY**. Division momentum: **MWS AI external revenue +71% YoY** (the MWS AI Agents Platform is this unit's flagship; Cotype VLM powers the new scanned-doc search), **MWS Cloud +20% YoY**, **cybersecurity external revenue +53% YoY** (source: MWS, 2026-08-25). AI is the single fastest-growing line, which is why the group keeps shipping AI-platform features — this release is a product-velocity signal for the highest-growth, highest-multiple segment, not a revenue event on its own.

**vs expectations / prior period.** No public consensus pulled for this product item [UNSOURCED on Street estimates]. YoY/sequential trend for MWS AI is decelerating off a hot base: external revenue +46% group-MWS in Q1 2026 (MWS AI revenue ×2.2 / ~+120%) vs +18% MWS-external / +71% MWS AI in Q2 2026 — still triple-digit-ish for the AI sub-unit but off Q1's pace. Group Q1 2026 MWS revenue was RUB 14bn, so RUB 15bn in Q2 is modest sequential growth on a small absolute base. The AI platform remains a sub-RUB-15bn-unit story — immaterial to the RUB 213.5bn group top line today, material as an option on mix shift.

**Guidance / forward.** No FY2026 group guidance given at Q2; management flagged a **new dividend policy to be finalized in autumn 2026**. No segment-level MWS guidance disclosed [UNSOURCED]. Forward read (analysis): continued double-digit MWS external growth with AI as the lead driver is plausible given the product cadence here, but the base is too small to move group numbers near-term.

**Thesis-flags.**
1. AI is MTS's growth narrative, not its earnings engine — fact: MWS AI +71% YoY external but MWS is RUB 15bn vs RUB 213.5bn group; why it matters: the agents-platform release de-risks the "MTS as tech holding" re-rating story more than it moves 2026 EPS; second-order: value accrues only if MWS is eventually carved out/IPO'd at a tech multiple.
2. Net-profit optics are distorted — the +23.9x print is largely the tower-disposal gain; who's silent on what: management leads with the headline profit and deleveraging, less on organic earnings quality. Underlying OIBDA +16.3% is the cleaner signal.
3. Deceleration watch — MWS AI pace eased Q1→Q2 (×2.2 → +71%); if the agents-platform features don't convert to external revenue, the AI growth premium compresses.

Sources: MTS Group Q2 2026 corporate release (reported 2026-08-25) https://ir.mts.ru/news_and_events/corporate_releases/details/742437 · MWS Q2 2026 segment release (2026-08-25) https://mws.ru/news/mts-web-services-uvelichila-vneshnyuyu-vyruchku-na-18-vo-vtorom-kvartale-2026-goda/ · MTS Q1 2026 press release https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf · product item: ai.cnews.ru 2026-10-16. Public Street consensus: no data / [UNSOURCED].
<!-- /enrichment:earnings_review -->
