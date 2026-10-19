---
title: "VK launches VK Data Catalog with AI-agent access"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/vk
  - industry/infrastructure
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://ai.cnews.ru/news/line/2026-10-13_vk_tech_predstavila_vk_data_catalog
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: se23615fa
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# VK launches VK Data Catalog with AI-agent access

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Представил VK Data Catalog — сервис для каталогизации корпоративных данных, управления их качеством и правами доступа с возможностью подключения AI-агентов через протокол MCP

## Первоисточники

### ai.cnews.ru
<https://ai.cnews.ru/news/line/2026-10-13_vk_tech_predstavila_vk_data_catalog>
*337 слов · direct*

Дмитрий Степанов
VK Tech представила VK Data Catalog для управляемой работы ИИ-агентов с корпоративными данными
VK Tech представила VK Data Catalog для управляемой работы ИИ-агентов с корпоративными данными. Сервис сводит описания корпоративных данных в один каталог, которым компания управляет по общим правилам. Сервис забирает технические и операционные метаданные из систем и связывает их с бизнес-терминами, владельцами, происхождением данных и результатами проверок качества. Об этом CNews сообщил представитель VK Tech .
ИИ-агентам нужен актуальный и управляемый контекст: что означают показатели, откуда они появились, кто за них отвечает, какого они качества и можно ли их использовать в конкретной задаче. Без этой информации агент может выбрать неподходящие или устаревшие данные и неверно их интерпретировать.
 VK Data Catalog объединяет поиск по данным, бизнес-глоссарий, управление владельцами и качеством данных, анализ происхождения данных до уровня колонок и анализ влияния изменений. При совместном использовании с VK Data Platform и ИИ-платформой VK AI Space можно использовать бизнес-контекст из каталога непосредственно при работе с данными и построении аналитических и ИИ-сценариев, включая корпоративных ИИ-агентов . Структурированные, неструктурированные и потоковые данные могут получать бизнес-контекст из каталога и использоваться в сценариях с учетом единых правил доступа и контроля качества .
VK Data Catalog поддерживает подключение ИИ-приложений и агентов по открытому протоколу MCP ( Model Context Protocol ), что позволяет использовать данные каталога как источник структурированного контекста для ИИ-сценариев.
«При внедрении дата-каталогов есть риск получить формальный реестр, который постепенно устаревает и перестает использоваться. Мы создаем инструмент, встроенный в ежедневную работу: каталог будет автоматически собирать и актуализировать метаданные , предлагать описания и связи, а владельцам данных останется проверять и подтверждать изменения. Интеграция с VK Data Platform и AI-платформой VK Tech позволит использовать этот контекст непосредственно при создании агентов. Развитие семантического слоя поможет точнее связывать бизнес-показатели с данными, сокращать объем лишнего контекста и расход токенов, а аудит — отслеживать, какие источники использовал агент. Для нас результат не количество объектов в каталоге, а их реальное использование в аналитических и ИИ-сценария», — сказала директор по продуктам направления « Дата-сервисы » VK Tech Екатерина Канунникова .
 Школа Роста CNews — короткие онлайн-программы по востребованным ИТ-компетенциям

## Контекст

<!-- enrichment:context -->
# Context-enrichment: VK launches VK Data Catalog with AI-agent access
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
VK Tech (the B2B arm of VK) unveiled **VK Data Catalog** on 2026-10-13: a metadata-management / data-governance service that catalogs enterprise data (technical + operational metadata pulled from source systems) and links it to business terms, data owners, lineage (down to column level), and data-quality checks. Feature set as announced: data discovery/search, business glossary, ownership & quality management, column-level lineage, change-impact analysis. The headline hook is that AI apps/agents can connect to the catalog over the **open MCP (Model Context Protocol)** to use it as a source of structured context.

De-PR'd reality: this is a **standard enterprise data-catalog product** (the category pioneered by Alation/Collibra ~2015 and now table-stakes in every major cloud: AWS Glue Data Catalog, Google Dataplex, Databricks Unity Catalog). The genuinely current-year wrapper is the MCP adapter. Everything material is **"announced", not "adopted"**: no customer names, no number of deployed catalogs, no GA/pricing, no benchmark. VK's own product director (Ekaterina Kanunnikova) pre-empts the obvious failure mode — "there's a risk of getting a formal registry that goes stale and stops being used" — and promises auto-collection of metadata and a future **semantic layer** to cut token spend. That hedge is a tell: the hard part (sustained adoption, not shelf-ware) is explicitly deferred to roadmap.

**Why framed this way:** the value is pitched entirely as *plumbing for AI agents* rather than as a BI/analyst tool, because the catalog only earns its keep when paired with the rest of the stack — **VK Data Platform** (lakehouse) + **VK AI Space** (agent platform, launched Apr 2026). It is a **lock-in / completeness** play, not a standalone breakthrough.

## [1] Competitors / peers
- **Domestic, direct:** Yandex Cloud / **Yandex B2B Tech** (DataLens BI + data-management services), **Cloud.ru**, Selectel. Yandex has the deeper data-management portfolio and is the AI-startup default. Catalog-specific governance tooling is thin across all Russian clouds (web research found no clearly branded Yandex "data catalog" equivalent), so VK is plausibly early *domestically* on a packaged catalog — but late *globally*.
- **Global prior art (the real benchmark):** Collibra, Alation, Databricks Unity Catalog (with MCP server already shipping), AWS Glue/DataZone, Google Dataplex, Microsoft Purview. MCP-as-context-for-agents is itself a 2025 pattern (Anthropic's MCP; see corpus [[Coinbase launches Payments MCP for AI agents]], [[Bud Financial launches MCP server for AI banking]]). VK is **catching up / at parity on the wrapper, behind on the core**.
- **Position:** domestically ahead on packaging; globally a fast-follow of a 10-year-old category. **Why the lay of the land is this way:** sanctions/import-substitution removed the Western incumbents from the RU market, so a "good-enough" local catalog captures demand that would otherwise go to Collibra/Databricks — the moat is **regulatory/geographic, not technical**.

## [2] Company history / fit
VK Tech has been assembling an end-to-end enterprise-AI stack through 2026: **VK AI Space** agent/multi-agent platform (Apr 30, 2026), **VK WorkSpace** MCP server exposing Mail/Drive/Calendar to agents (Sep 2026), and **VK Data Platform** (lakehouse). The Data Catalog is the governance/context layer that stitches these together — a logical, well-sequenced fit, not a random launch. VK also ships consumer AI (Discovery AI neuro-search, Jul 2026 — [[VK launches Discovery AI neural search across products]]).
**Why VK acts this way:** VK's core ad/social business is pressured and low-multiple; the B2B cloud/AI line is the growth-and-re-rating story. Building the *whole* stack (data → platform → agents → governance) lets VK sell a bundle and defend against a single-point competitor.

## [3] Novelty / value-add / traction
- **Really new?** No, as a category. The only 2026-specific element is native MCP wiring so agents consume governed context (lineage, ownership, quality, access rules) instead of raw tables — a legitimately useful pattern, but **not VK-invented** (Databricks/others already expose catalogs via MCP).
- **Traction:** **zero disclosed.** No clients, no live deployments, no usage metrics. Kanunnikova's own KPI framing ("success is real use, not object count") underscores that use is unproven.
- **Where value/margin sits:** the catalog is a feature that makes **VK Data Platform + VK AI Space stickier**; alone it is commoditizable. Margin accrues to whoever owns the **platform + compute**, not the catalog metadata layer. **Second-order:** the catalog is a retention/attach mechanism — its worth is measured in platform lock-in, not in standalone revenue.

## [4] What's next / market sentiment
Roadmap: auto-collecting/auto-refreshing metadata, suggested descriptions/links, a **semantic layer** (to reduce agent token spend), and audit of which sources an agent used. The decisive backdrop: **Yandex B2B Tech + VK Tech are being merged** (confirmed by Mintsifry early Oct 2026; JV talks started Jul 2026; formalities targeted by **2026-03-31 2027**) into a cloud entity with ~30% market share — Russia's largest. **Why this matters most:** a product launched 5 days before/around a merger confirmation is partly **positioning for integration** — VK's catalog may end up as a line item inside a combined Yandex-VK portfolio, or be rationalized against a Yandex equivalent. Risk: duplicated roadmaps get cut post-merger. Additional backdrop: Yandex data-center outages (Oct 2026, drone attacks) forced emergency client migrations to VK Cloud/Selectel/K2 — a reminder that RU cloud capacity/resilience, not catalog features, is the live constraint. (analysis)

## Sources
- ai.cnews.ru, 2026-10-13 — VK Tech presents VK Data Catalog (primary, in-note).
- seonews.ru / computerra.ru / content-review.com — launch coverage, catalog-as-agent-intermediary, MCP access control.
- lenta.ru, 2026-04-30 — VK AI Space launch; computerra.ru — VK AI Space multi-agent scenarios.
- vibecoding.ru / iz.ru, 2026-09 — VK WorkSpace MCP for agents.
- cloud.vk.ru/data-platform — VK Data Platform (lakehouse, Cloud Trino/S3).
- market.cnews.ru (2026-10-08) / computerra.ru / d-russia.ru — Yandex B2B Tech + VK Tech merger, ~30% share, deadline 2027-03-31.
- meduza.io / www1.ru (2026-10) — Yandex DC outages, emergency migration to VK Cloud/Selectel/K2.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Challenge / red-team questions

1. **Is a "data catalog" new?** No — Alation/Collibra created the category ~2015; every hyperscaler ships one (Glue, Dataplex, Unity Catalog, Purview). VK is a domestic fast-follow. **(closed, answered: not new)**
2. **What is actually 2026-novel here?** Only the native MCP adapter so agents consume governed context. But MCP-over-catalog already exists (Databricks). Marginal novelty. **(closed)**
3. **Any adoption/traction disclosed?** None. Zero named clients, zero deployment counts, no GA date, no pricing. Pure announcement. **(closed: no traction)**
4. **Announced vs live?** Announced 2026-10-13; nothing indicates GA or live production use. **(closed: announced)**
5. **Is VK domestically first with a packaged catalog?** Plausibly early vs Yandex/Cloud.ru, but web research did not confirm a branded Yandex catalog equivalent — so "ahead domestically" is a hypothesis, not proven. **(open)**
6. **Does the catalog stand alone or require the VK stack?** Value is realized mainly with VK Data Platform + VK AI Space — it's an attach/lock-in feature. **(closed)**
7. **Who captures the margin?** The platform+compute owner, not the metadata layer. Catalog is commoditizable. **(closed, analysis)**
8. **How does the Yandex B2B Tech + VK Tech merger change this?** Hugely — the product may be redundant with a Yandex equivalent post-merger; launch timing looks like integration positioning. **(open, decisive)**
9. **What's the real failure mode?** Catalog becoming stale shelf-ware — VK itself names this risk; mitigation (auto-metadata, semantic layer) is roadmap, not shipped. **(closed: unproven mitigation)**
10. **Is the "saves tokens via semantic layer" claim verifiable?** No numbers given; it's a roadmap promise. **(open)**
11. **Does MCP introduce a security/access-control risk?** Catalog is pitched as the control point (permission-gated agent access) — but no audit/pen-test evidence; audit is also roadmap. **(open)**
12. **Who needs whom more — VK's catalog or VK's agents?** The agents (VK AI Space) need governed context to be useful; the catalog needs the platform for distribution. Mutual, but agents drive the demand. **(closed, analysis)**
13. **Is there regulatory tailwind?** Yes — import substitution removed Collibra/Databricks from RU; moat is geographic/regulatory, not technical. **(closed)**
14. **Downside trigger?** Post-merger roadmap rationalization cutting duplicate tooling; or capacity/resilience (Yandex DC outages) dominating customer priorities over governance features. **(open)**
15. **Does this move the fintech needle?** Only indirectly — it's enterprise data infra, fintech-adjacent at best; weight is low. **(closed)**

Importance: 2/5 — A standard, globally-late data-catalog category entry with an MCP wrapper, zero disclosed adoption, and value contingent on the rest of VK's stack. It is a sensible completeness move in VK Tech's AI-stack build-out, and the imminent Yandex B2B Tech / VK Tech merger makes it strategically interesting as positioning — but as a standalone event it is no-novelty + no-traction, hence 2/5.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** VK Data Catalog sits in the enterprise data-catalog / data-governance subvertical of enterprise data infrastructure. Global data-catalog TAM is small and estimated inconsistently: ~$1.4–1.7bn in 2026 across most research houses (per Coherent Market Insights / The Business Research Company, "$1.38bn in 2025 → $1.72bn in 2026"; Persistence Market Research puts 2033 at $3.28bn at ~12.6% CAGR, via einnews, as of 2026) — treat the absolute figures as directional, not precise. Structure: fragmented and vendor-led, sitting one layer above the cloud data estate (warehouse/lakehouse); value is created by automated metadata harvesting + lineage + a business glossary that is actually used rather than a "formal registry that goes stale" — a decay risk VK's own product lead (Kanunnikova) names explicitly. Why now: the secular driver is AI agents needing *governed* context (what a metric means, provenance, owner, quality, usage rights) before they can safely query enterprise data — "governance is table stakes for agents" (per Snowflake/Databricks 2026 summit coverage, via pointfive/atlan). Russian angle: import-substitution + data-localization regulation (AKIT/ФСТЭК) keeps foreign catalogs (Collibra, Alation, Atlan) out and feeds a domestic market VK is entering late.

**Competitive landscape.** Sector KPIs: # of governed data assets is a vanity metric (VK explicitly disavows it — "not the count of objects but real usage"); the KPIs that matter are catalog *adoption/active usage*, metadata freshness (auto-refresh vs manual), and lineage depth (column-level). VK claims column-level lineage + impact analysis + MCP connectivity. Basis of competition: product completeness, deep integration with the vendor's own stack, and security certification. Recent moves: VK Data Catalog launched 2026-10-13, tightly coupled to VK Data Platform + VK AI Space (lock-in play). Key domestic incumbent — **Arenadata Catalog**, which "formed the Data Governance market in Russia," live since late 2021 and ФСТЭК trust-level-4 certified as of June 2025 (via arenadata.tech), clearing it for banks, government and critical infrastructure. Globally, Collibra shipped an MCP Server and Snowflake/Databricks shipped managed MCP servers + AI gateways in 2026 (via collibra.com, snowflake.com) — so MCP support is a parity feature, not a VK differentiator. Protagonist's position: **catching up / niche** — a credible same-stack offering for VK Cloud/AI Space customers, but a late entrant against a certified domestic leader `(analysis)`. Moat: switching costs from stack bundling, not technology.

**Comps & multiples.** No deal/valuation attached to this launch, so no transaction multiple to compute — "no data". Standalone catalog revenue is not broken out. IR anchor for scale (see Risk/IR): VK Tech FY2025 revenue RUB 18.8bn, +38% YoY (per vk.company Q4/FY2025 release); VK Cloud +55% YoY, VK WorkSpace +68% YoY in Q1 2025 — so the catalog is a feature layer on a fast-growing but still sub-RUB-20bn B2B unit, not a material standalone line. Internal comps (base, qualitative — semsearch 402, grep fallback): [[Visiology closes 200M ruble investment round from 342 investors]] (RU BI, ~RUB 200m round — adjacent analytics-stack domestic player); [[MTS bundles enterprise solutions under MTS CorpTech brand]] and [[Danila Dyugurov named head of MWS Cloud]] (MTS enterprise/cloud build-out — rival stack); [[Yandex Cloud helps clients migrate to rival providers after outages]] (competing hyperscaler, reliability stress); [[MyOffice reports nearly 9bn rouble loss]] (RU enterprise-software economics are thin). Distribution not computed; qualitative comparison only.

**Risk flags.**
1. **Late entrant vs a certified incumbent.** Arenadata Catalog is ФСТЭК-level-4 certified (June 2025) and already "forms" the RU Data Governance market; VK's catalog is unlisted on certification, which gates the highest-value bank/government/CII buyers — second-order: VK may be confined to its own-cloud installed base until certified.
2. **MCP/agent framing is parity, not moat.** Collibra, Snowflake and Databricks all shipped governed MCP in 2026; the "AI-agent access" headline is table-stakes, so VK competes on stack integration, not protocol novelty — if a customer isn't on VK Data Platform/AI Space, the value proposition thins.
3. **Catalog-decay execution risk.** The product's whole pitch (auto-collect/refresh metadata so it doesn't become a dead registry) is also its biggest execution risk; adoption, not asset count, is the only proof — and none exists yet (announced, zero disclosed customers/live deployments).

**What this changes (idea-lens).** `(analysis)` This is a defensive stack-completion move: VK is closing a governance gap so AI Space agents have governed context, protecting its cloud installed base rather than opening a new market. Falsifiable thesis — VK Data Catalog stays an own-stack add-on, not a standalone governance winner; it's wrong if VK (a) obtains ФСТЭК certification and (b) lands a named external (non-VK-cloud) customer within ~12 months. Trigger to watch: a certification announcement or a reference bank/government deployment.

Sources: https://ai.cnews.ru/news/line/2026-10-13_vk_tech_predstavila_vk_data_catalog · https://vk.company/en/press/releases/12255/ · https://www.coherentmarketinsights.com/market-insight/data-catalog-market-5142 · https://www.einnews.com/pr_news/901813237/data-catalog-market-set-to-reach-us-3-28-bn-by-2033 · https://arenadata.tech/about/blog/kogda-dannye-govoryat-na-yazyke-biznesa-arenadata-catalog-formiruet-rynok-data-governance-v-rossii/ · https://www.collibra.com/products/mcp-server · https://www.snowflake.com/en/blog/managed-mcp-servers-secure-data-agents/ · https://www.pointfive.co/blog/snowflake-and-databricks-summits-2026-what-actually-matters
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> **Note:** This is a product launch (VK Data Catalog), not an earnings event. No results are in the news itself. The figures below are VK's own most-recent audited filing as **financial context** for the segment that owns this product (VK Tech), not a report on the announcement.

**Verdict (context-only read; closest prior print = FY2025, reported 2026-03-19).** VK Data Catalog has no standalone financials disclosed. Its home segment, **VK Tech**, is VK's fastest-growing and highest-margin unit: FY2025 revenue RUB 18.8bn (+38% YoY), segment EBITDA RUB 4.8bn (+22% YoY) — materially outpacing the group (revenue +8%). At group level FY2025 was a modest **BEAT vs public consensus** — revenue RUB 160bn vs Interfax consensus RUB 158.9bn, adj. EBITDA RUB 22.6bn vs RUB 21.6bn — with the EBITDA line swinging from a RUB 4.9bn loss in 2024 to positive.

**Key figures (VK FY2025, IFRS audited; 12 months to 2026-03-19 release).**
- Group revenue: **RUB 160bn, +8% YoY**.
- Adjusted EBITDA: **RUB 22.6bn**, vs **negative RUB 4.9bn** in 2024 (full turnaround to positive).
- Net loss: **RUB 25.4bn**, narrowed sharply from a **RUB 95.49bn loss** in 2024 (~73% narrower; lower finance/impairment burden, operating leverage).
- No 2025 dividend (confirmed by management).

**By segment / driver (FY2025).**
- **VK Tech (B2B cloud/SaaS — the segment that ships VK Data Catalog, VK Data Platform, VK AI Space):** revenue **RUB 18.8bn (+38% YoY)**, EBITDA **RUB 4.8bn (+22% YoY)**. Drivers: VK Cloud +82% YoY, business applications +95% YoY, VK WorkSpace productivity services +41–63% YoY. Fastest-growing, EBITDA-positive — the data/AI product stack is being built on a segment that already scales profitably, not a cash-burning bet.
- **Social Platforms & Media Content:** revenue **RUB 109.8bn (+5% YoY)**, EBITDA **RUB 21.1bn** (the group's profit engine).
- **EdTech:** revenue **RUB 7.4bn (+19% YoY)**, EBITDA **RUB 0.7bn**.
- **Ecosystem services & other (Mail, Cloud, VK Play, RuStore, VK Pay, YCLIENTS):** revenue **RUB 27.7bn (+13% YoY)**, EBITDA **RUB 0.4bn**.

**vs expectations / prior period.** Group revenue beat Interfax public consensus by RUB ~1.1bn (+0.7%); adj. EBITDA beat by RUB ~1.0bn (+4.6%) — driver is the EBITDA turnaround (cost discipline + VK Tech mix), labelled public consensus, not Street. No pre-earnings preview in the base for this print. YoY: group +8% is a deceleration vs the double-digit era, but VK Tech's +38% is where the thesis lives. No prior VK earnings note in the corpus to wikilink (semsearch down — OpenRouter 402).

**Guidance / forward.** No explicit 2026 numeric guidance located in the FY2025 release. Management's strategic emphasis is monetising VK Tech / the AI-and-data stack — VK Data Catalog (MCP-connected, feeding VK Data Platform + VK AI Space) is a direct expression of that: a product aimed at lifting the +38% segment's take by making enterprise data agent-consumable. (analysis) Plausible that VK Tech stays the growth-and-margin leader; the launch is a feature extension of an already-profitable line, not a new cost centre.

**Thesis-flags.**
1. *VK Tech is the only unambiguously healthy growth-and-margin story in the group* (fact: +38% rev / +22% EBITDA vs group +8%) → why it matters: VK Data Catalog monetises exactly this segment → second-order: incremental SaaS attach on VK Cloud/WorkSpace installed base, not a standalone revenue line to model yet.
2. *Group still loss-making (RUB 25.4bn net loss)* despite EBITDA turnaround → the data/AI product cadence must keep VK Tech compounding to carry group economics → watch whether segment EBITDA margin (FY2025 ~25.5%) holds as R&D on AI/data products scales.
3. *De-PR:* the launch PR touts MCP/agent access and "real usage, not object count"; it is silent on pricing, customer count, and any revenue contribution — treat as capability announcement, zero disclosed financial impact to date.

Sources: VK Q4 & FY 2025 press release 2026-03-19 (corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf · drive_url https://corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf) · Interfax FY2025 results + consensus (interfax.com/newsroom/top-stories/116698/) · AKM net loss (akm.ru/eng/news/vk-s-net-loss-for-2025-under-ifrs-amounted-to-25-4-billion-rubles/) · segment detail via VK press release 12255. 2026 numeric guidance: no data. Corpus semsearch: no data (OpenRouter 402).
<!-- /enrichment:earnings_review -->
