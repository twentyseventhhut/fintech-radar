---
title: "Russian State Library automates processes with MWS AI platform"
date: 2026-07-08
retrieved: 2026-07-09
tags:
  - company/mws-ai
  - industry/ai
  - region/ru
  - type/partnership
sources:
  - https://www.vedomosti.ru/technologies/trendsrub/news/2026/07/08/1212172-ii-platformi-mws
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: s9f0bdf48
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Russian State Library automates processes with MWS AI platform

> [!info] 2026-07-08 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Ведомости: Российская государственная библиотека автоматизирует процессы с помощью ИИ-платформы от MWS AI

## Первоисточники

### vedomosti.ru
<https://www.vedomosti.ru/technologies/trendsrub/news/2026/07/08/1212172-ii-platformi-mws>
*270 слов · direct*

Российская государственная библиотека (РГБ) и компания MWS AI (входит в МТС Web Services) объявили о технологическом партнерстве. Вместе стороны займутся разработкой ИИ-платформы для автоматизации ключевых процессов в библиотечной сфере, говорится в сообщении компании. В частности, речь идет об интеллектуальном поиске в научных фондах, автоматизации каталогизации и аналитике текстовых корпусов. Уточняется, что в перспективе платформу могут предложить всем библиотекам страны.
В части поиска система научится находить источники по смыслу запроса, а не только по терминам, отмечается в сообщении. Ожидается, что это позволит повысить точность отработки запросов читателей. На этапе эксперимента искусственный интеллект находил подходящие работы как минимум в семи случаях из десяти. Платформа также позволит автоматизировать процесс присвоения библиотечных индексов. ИИ будет формировать предложения по рубрикам, индексам и метаданным.
Исследовательский фонд РГБ насчитывает около 1 млн единиц хранения и продолжает расти. Для работы с уже оцифрованными фондами MWS AI и РГБ разработают два решения: одно позволит проводить ИИ-поиск по полному тексту книг, второе поможет при анализе нарративов и сравнении текстов. Инфраструктура и данные будут размещены на серверах РГБ, а прикладные ИИ-решения будут разрабатываться на базе платформы MWS AI Agents Platform, позволяющей создавать ИИ-агентов и мультиагентные системы без навыков программирования.
По словам генерального директора Российской государственной библиотеки Вадима Дуды, библиотека при помощи искусственного интеллекта начинает работать с фондом как с массивом знаний. «Ценность нашего совместного проекта – не в отдельных технологических решениях, а в том, что мы выстраиваем тиражируемую модель для всей отрасли. То, что будет опробовано в РГБ, смогут использовать другие библиотеки страны», – заявил генеральный директор MWS AI Денис Филиппов. По его словам, сейчас в России насчитывается более 40 000 публичных библиотек с совокупным фондом почти 900 млн единиц хранения.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Russian State Library (RGB) + MWS AI — library-automation AI platform
_Analytical notes (not a post). Importance: 2/5._

**Freshness: FRESH** — first coverage of this specific RGB × MWS AI partnership in the corpus. The vault has two adjacent MTS/MWS threads but neither is this deal: [[MWS Cloud launches fastest S3 storage for ML workloads]] (2026-07-02, the cloud/storage arm) and [[MTS sells 49.9% stake in its tower company]] (2026-06-26, the parent's balance-sheet engineering). No prior mws-ai-tagged note exists. Not a duplicate.

## [0] What exactly happened (de-PR'd)
On **2026-07-08** the **Russian State Library (RGB / РГБ)** and **MWS AI** (the AI arm of MTS Web Services / МТС) announced a **technology partnership** to build an AI platform automating core library processes, in three directions: (1) **intelligent/semantic search** over scientific collections (find sources "by meaning of the query, not just terms"); (2) **cataloguing automation** — AI proposes rubrics, library indices and metadata; (3) **text-corpus analytics** — full-text AI search across digitised books plus a narrative-comparison tool. Applied solutions are to be built on the **MWS AI Agents Platform** (a low-code / no-code agent + multi-agent builder). **Infrastructure and data stay on RGB's own servers** (on-prem, not MWS cloud). Stated scope figures: RGB's research fund ≈ **1 mn storage units**; per other pickups (RG/CNews) the semantic-search target is the repository of **~3.7 mn abstracts/dissertations**, and RGB receives **~100k mandatory-copy publications/year** with a cataloguing entry today taking a specialist **>30 min**. Russia has **>40,000 public libraries** with a combined ~**900 mn** storage units — the stated long-term TAM if the model is offered to all of them. Quotes: RGB director-general **Vadim Duda** ("the library begins to work with its fund as a body of knowledge"); MWS AI CEO **Denis Filippov** (the value is "a replicable model for the whole industry", not point solutions).

**+ Why framed this way / what it reveals (core red-team):**
- **This is an announcement, not a deployed system.** The one hard evidence point — AI found the right work **"in at least 7 of 10 cases"** — is described as an **experiment/pilot** stage, i.e. **~70% recall on an internal test**, which is *below* production-grade for a discovery tool and is self-reported by the vendor. No accuracy for cataloguing/metadata generation is given, no go-live date, no contract value, no named budget. (analysis)
- **"On-prem, on RGB servers" is the strategically interesting bit, not the AI.** It means MWS monetises the **platform/agent layer + services**, not compute — a land-grab for a reference logo in the state/GLAM sector rather than a cloud-consumption deal. The RGB win is a **template/showcase** ("replicable for all 40k libraries") — classic public-sector flagship positioning to seed a much larger public-procurement pipeline. (analysis)
- **No financial or fintech content.** This is an AI-platform / public-sector-digitisation story about MTS's non-telecom monetisation, adjacent to the vault's MWS/MTS thread; it is *not* a payments/banking event. Relevance here is as a data point on **MTS Web Services' B2B/B2G AI commercialisation**, not on financial services. (analysis)

## [1] Competitors / peers
- **Sber (GigaChat / GigaChat Enterprise, GigaCowork)** — the dominant domestic rival: Sber opened GigaChat Enterprise (corporate AI-agent platform) in **Mar 2026** and pushes GigaChat into public-sector/GLAM use; comparative library studies benchmark **GigaChat vs YaGPT** for query deconstruction, handwritten-card recognition and text-error correction. Sber is the natural incumbent MWS is racing for these state accounts.
- **Yandex (YaGPT / Yandex Cloud)** — the other national LLM/cloud champion; competes on the same semantic-search + document-AI axis.
- **Separate RGB AI track (do not conflate):** RGB also announced (~**Apr 2026**) a large-scale collection-digitisation effort framed around domestic software (press mentions an "ANSIS"-type reference system and GigaChat-based manuscript recognition, and an RGB×BEAC agreement). That is a **different initiative** from this MWS AI Agents Platform deal; press aggregators blur them.
- **Global prior art (this is not novel as a category):** **Ex Libris** (AI + linked-open-data / BIBFRAME metadata generation), **OCLC**, the **Library of Congress PCC AI/ML task group**, and the **Royal Library of Belgium** retrospective-cataloguing AI demo (May 2025); academic RAG-for-catalogue and AI-MARC21-agent work (CILIP, Manchester Met, 2025). AI-assisted cataloguing/semantic discovery in GLAM is an active, **globally established 2024–2026 pattern**, not a Russian first.

**+ Second-order:** MWS's edge is not the technology (LLM RAG over a catalogue is now commodity) but **import-substitution + on-prem sovereignty + a state anchor tenant**. In a sanctions-fenced market where Ex Libris/OCLC are effectively unavailable, the contest collapses to **Sber vs Yandex vs MWS** for domestic public-sector logos, decided by ecosystem, price and political access — not model quality. (analysis)

## [2] Company history / fit
MWS AI (formerly MTS AI) is MTS Web Services' AI unit (LLM family **Cotype / Cotype Nano**, corporate document-AI assistants, and the **MWS AI Agents Platform** launched Dec 2025 with a reported **~RUB 4bn** investment). MWS AI **2025 revenue ≈ RUB 6.9bn, +60% YoY**, of which generative-AI products >RUB 3.3bn (per TAdviser). It sits inside MTS Web Services (2025 revenue RUB 63.8bn, +9.6%; cloud +40%), whose corporate goal is **>RUB 200bn capitalisation by end-2028** and a **~13% share of the domestic AI-software market by 2028**. → Fit: this RGB deal is exactly the **B2G reference-account strategy** that underpins that 2028 target — a marquee state logo to anchor an "AI for all 40k libraries" procurement funnel and to validate the Agents Platform on a real, large corpus. (analysis)

## [3] Novelty / value-add / traction
- **Novelty: low.** RAG semantic search + AI cataloguing/metadata over a library corpus is **standard 2025–2026 GLAM practice** globally (Ex Libris, LoC/PCC, RGB's own parallel track). MWS's genuine contribution is a **domestic, on-prem, sovereign** implementation on its own agent platform — parity/import-substitution, not invention.
- **Value-add (where real / where not):** real value = a **replicable, ruble-priced, on-prem** stack that lets Russian state libraries automate cataloguing (a genuine labour bottleneck: >30 min/record × ~100k/yr) and offer semantic discovery without foreign vendors. Not-yet-real = **accuracy and adoption**: the only metric (~70% search recall, experimental) is mediocre and unaudited; no cataloguing-accuracy figure, no go-live, no contract value, no second library signed.
- **Traction: minimal.** One flagship partner, pilot-stage, aspirational "could be offered to all libraries." Capability + intent announcement, not a proven rollout. (analysis)

## [4] What's next / market sentiment
Watch: (a) a **production go-live / accuracy disclosure** for cataloguing and search (does ~70% improve, and is metadata quality good enough for librarians to accept?); (b) whether a **second library or a federal library-network contract** actually signs (the real proof the "replicable model" is bankable); (c) **Sber/Yandex counter-bids** for the same state accounts. → Second-order: RGB is a **prestige loss-leader** — the economic question is not this deal's (undisclosed, likely small) value but whether it converts into a **standardised public-procurement template** across a fragmented 40k-library market that buys on price and political access. If it does, it's a durable B2G annuity for MWS AI; if it stays a one-off showcase, it's PR. (analysis/hypothesis)

## Sources
- Primary (note): vedomosti.ru — https://www.vedomosti.ru/technologies/trendsrub/news/2026/07/08/1212172-ii-platformi-mws
- RG (RGB detail: 3.7mn abstracts, 100k/yr, >30min/record): https://rg.ru/2026/07/08/ii-platforma-mws-ai-avtomatiziruet-rabotu-rgb.html
- CNews (partnership scope): https://www.cnews.ru/news/line/2026-07-09_mws_ai_stala_partnerom_rossijskoj
- MWS AI Agents Platform: https://mts.ai/product/ai-agents-platform/ ; https://www.tadviser.ru/index.php/Продукт:MWS_AI_Agents_Platform
- MWS AI revenue RUB 6.9bn +60% / gen-AI >3.3bn: https://tadviser.com/index.php/Company:MWS_AI,_MVS_AI_(formerly_MTS_AI,_MTS_AI)_Center_for_Artificial_Intelligence_MVS
- MTS Web Services RUB 63.8bn / 2028 targets: https://kod.ru/mts-web-services-plans-growth ; Agents Platform ~RUB 4bn: https://fork-tech.ru/actual/mts-invests-4bn-rubles-in-ai-agents-platform/
- Sber GigaChat Enterprise (Mar 2026, rival): https://moika78.ru/news/2026-03-03/1270763-sber-otkryl-dostup-k-gigachat-enterprise-platforme-dlya-sozdaniya-korporativnyh-ii-agentov/
- Global GLAM AI prior art: https://exlibrisgroup.com/blog/artificial-intelligence-blog-series-transforming-the-library-experience-with-linked-open-data-and-ai/ ; https://www.loc.gov/aba/pcc/taskgroup/AI-and-Machine-Learning-TG-final-report.pdf ; https://journals.cilip.org.uk/catalogue-and-index/article/view/750
- Internal: [[MWS Cloud launches fastest S3 storage for ML workloads]] ; [[MTS sells 49.9% stake in its tower company]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. Is this a deployed system or an announcement? Announcement + pilot only; no go-live date, no production accuracy beyond an experimental ~70% search recall. — *answered: announcement.*
2. Is the "7 of 10" figure independently verified? No — vendor-reported, experimental stage; ~70% recall is mediocre for discovery and unaudited. — *answered.*
3. Is any contract value / budget disclosed? No. No deal size, no revenue figure attached. — *open (likely small).*
4. Whose platform / whose compute? Applied AI on MWS AI Agents Platform, but **data + infra on RGB's own servers** — MWS sells the platform/service layer, not cloud consumption. — *answered.*
5. Is the "replicable for all 40k libraries / 900mn units" a signed pipeline or aspiration? Aspiration ("could be offered") — a TAM sizing, not booked contracts. — *answered: aspirational.*
6. Is the technology novel? No — RAG semantic search + AI cataloguing/metadata is standard 2025–26 GLAM practice (Ex Libris, LoC/PCC, Royal Library of Belgium). Novelty = import-substitution/on-prem, not category. — *answered.*
7. Who are the real competitors for these state accounts? Sber (GigaChat Enterprise, Mar 2026) and Yandex (YaGPT); library studies already benchmark GigaChat vs YaGPT. MWS is not obviously ahead. — *answered.*
8. Is this the same as RGB's other AI/digitisation announcement? No — a separate ~Apr 2026 RGB digitisation track (domestic reference system + GigaChat manuscript recognition, RGB×BEAC) is distinct; aggregators conflate them. — *answered: distinct.*
9. Is Filippov's "replicable model" quote correctly attributed? Primary source attributes the industry-model quote to MWS AI CEO Denis Filippov (Duda gives the "body of knowledge" quote); phrasing is slightly cross-wired in the source but that is what it states. — *noted; low materiality.*
10. Any fintech/financial-services angle? None. This is public-sector AI/digitisation; relevance is only as an MTS non-telecom monetisation data point. — *answered: not fintech.*
11. What accuracy is claimed for cataloguing/metadata (the bigger labour saving)? None disclosed — only search recall is quoted; metadata-generation quality is the real acceptance risk and is unstated. — *open; material.*
12. Will librarians accept AI-proposed indices/metadata? Unaddressed; human-in-the-loop review likely still needed, capping the >30min/record saving. — *open.*
13. Does on-prem-only limit MWS's economics? Yes — no compute annuity; value is platform licence + integration services, so per-deal revenue is likely modest unless it scales across many libraries. — *analysis.*
14. Is there sanctions/political dependency? Yes — the whole thesis rests on import substitution (Ex Libris/OCLC unavailable) and B2G access; demand is policy/state-procurement-driven, concentrated in one regulatory regime. — *analysis.*
15. What would make this actually matter? A federal library-network contract or a second signed library + a disclosed production accuracy — converting a prestige showcase into a repeatable B2G annuity. — *analysis/trigger.*

**Importance: 2/5** — A real, dated flagship B2G partnership at Russia's national library, and a clean data point on MTS Web Services / MWS AI's non-telecom AI commercialisation. But it is a pilot-stage announcement with no contract value, a single mediocre unaudited metric (~70% search recall), no novelty (standard GLAM AI, import-substitution flavour), a strong incumbent (Sber/Yandex) in the same lane, and **no fintech/financial-services relevance**. Genuine but incremental showcase, not a sector-mover.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits at the intersection of **Russian enterprise/B2G generative-AI platforms** and **GLAM (galleries/libraries/archives/museums) digitisation** — not fintech. Global GLAM-AI (RAG semantic discovery, AI cataloguing/metadata, OCR/HTR) is an established 2024–2026 pattern (Ex Libris BIBFRAME/linked-open-data automation, OCLC, LoC PCC AI/ML task group, Royal Library of Belgium retro-cataloguing demo, CILIP AI-MARC21 work). The Russian slice is smaller and policy-driven: the **Russian AI-software / corporate-AI market** is where the money is — MTS targets a **~13% share of the domestic AI-software market by 2028**. **Why now (Russia-specific):** (1) **import substitution** — Ex Libris/OCLC and Western LLM tooling are effectively unavailable, so state institutions must buy domestic (Sber/Yandex/MWS); (2) **data-sovereignty/on-prem** mandates for state data (here infra + data stay on RGB's own servers); (3) a genuine **labour bottleneck** — cataloguing a mandatory-copy record takes a specialist **>30 min** and RGB ingests **~100k/yr**, against a research fund of ~**1 mn** units and ~**3.7 mn** abstracts/dissertations to make searchable; national TAM framing is **>40,000 public libraries / ~900 mn** storage units (per the primary source). This is a **procurement-and-substitution tailwind, not organic competitiveness** (analysis).

**Competitive landscape.** Sector KPIs for enterprise-AI-platform players: platform/agent revenue and its growth, number of production (not pilot) deployments, model quality/accuracy on the target task, and B2G reference logos. Field: **Sber (GigaChat / GigaChat Enterprise agent platform, launched Mar 2026; GigaCowork)** is the dominant incumbent and pushes into public-sector/GLAM (comparative library studies already benchmark **GigaChat vs YaGPT** for query deconstruction, handwritten-card recognition, text-error correction); **Yandex (YaGPT / Yandex Cloud)** is the other national champion; **MWS AI (Cotype LLMs + MWS AI Agents Platform)** is the challenger here. Protagonist position: **MWS AI is a fast-growing but sub-scale challenger** relative to Sber/Yandex — the RGB deal is a **B2G reference/land-grab**, and the win is prestige more than economics (on-prem-only ⇒ no cloud-consumption annuity; value is platform licence + integration services). Moat is thin and non-technical: the AI (RAG over a catalogue) is commoditised; the durable edge, if any, is **import-substitution + on-prem sovereignty + state access + a replicable procurement template**, not switching costs (de-PR: pilot-stage, single mediocre metric ~70% search recall, no cataloguing-accuracy figure, no contract value).

**Comps & multiples.** Parent **MTS is IR-covered** (`mts`; latest on file: **Q1 2026 press release, dated 2026-05-20**, https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf) — but MTS trades as a telecom/ecosystem group on MOEX and gives **no clean segment multiple** for the MWS AI unit. Unit financials (company/press-stated, unaudited): **MWS AI 2025 revenue ≈ RUB 6.9bn, +60% YoY**, generative-AI products **>RUB 3.3bn**; MWS AI Agents Platform build reportedly **~RUB 4bn** invested. Parent layer: **MTS Web Services 2025 revenue RUB 63.8bn** (+9.6%; cloud +40%), corporate goal **>RUB 200bn capitalisation by end-2028** and **~13%** domestic AI-software share by 2028. **EV/Revenue and EV/EBITDA are not computable** for MWS AI — no standalone valuation, round, or disclosed EBITDA; MWS unit is not separately listed → any segment multiple is `[UNSOURCED]`. No public deal value for the RGB partnership → revenue contribution not computable. Internal comps are only adjacent MTS/MWS thread notes, not GLAM-AI or valuation comps: [[MWS Cloud launches fastest S3 storage for ML workloads]] (same MTS Web Services parent, product-capability announcement), [[MTS sells 49.9% stake in its tower company]] (parent balance-sheet context). Distribution not computed; qualitative only.

**Risk flags.**
1. **Pilot-to-production / accuracy risk.** The only hard metric is an **experimental ~70% search recall**, self-reported and mediocre for discovery; **no cataloguing/metadata-accuracy figure, no go-live, no contract value** are disclosed. Second-order: if librarians reject AI-proposed indices/metadata (human-in-the-loop review still required), the headline **>30 min/record** labour saving is capped and the "automation" thesis softens to assistance.
2. **Incumbent competition for the same B2G accounts.** **Sber (GigaChat Enterprise)** and **Yandex (YaGPT)** are larger, better-capitalised national champions targeting identical state/GLAM deals; MWS AI is not demonstrably ahead on model quality, so the "replicable model for 40k libraries" pipeline is contestable and price/political-access-driven, not locked.
3. **Policy-concentration + economics risk.** Demand rests almost entirely on **import substitution and state procurement** (a single regulatory regime), and the **on-prem-only** structure gives MWS no compute annuity — so unless the template scales across many libraries via federal contracts, per-deal revenue is small and the win stays a prestige loss-leader.

**What this changes (idea-lens).** For MTS's equity story this is a **small, supportive data point** on the non-telecom AI-monetisation leg (a flagship B2G logo feeding the 2028 AI-software-share target), **not a re-rating** and **not a fintech event** (analysis). Falsifiable thesis: if MWS AI signs a **second library or a federal library-network contract within ~12 months AND discloses a production accuracy** for cataloguing/search, the "replicable model" is bankable and becomes a durable B2G annuity; **what breaks it** — the deal stays a one-off showcase, Sber/Yandex win the follow-on state accounts, or accuracy/adoption never clears librarian acceptance, leaving it PR rather than platform revenue.

Sources: https://www.vedomosti.ru/technologies/trendsrub/news/2026/07/08/1212172-ii-platformi-mws · https://rg.ru/2026/07/08/ii-platforma-mws-ai-avtomatiziruet-rabotu-rgb.html · https://www.cnews.ru/news/line/2026-07-09_mws_ai_stala_partnerom_rossijskoj · https://mts.ai/product/ai-agents-platform/ · https://tadviser.com/index.php/Company:MWS_AI,_MVS_AI_(formerly_MTS_AI,_MTS_AI)_Center_for_Artificial_Intelligence_MVS · https://kod.ru/mts-web-services-plans-growth · https://fork-tech.ru/actual/mts-invests-4bn-rubles-in-ai-agents-platform/ · https://moika78.ru/news/2026-03-03/1270763-sber-otkryl-dostup-k-gigachat-enterprise-platforme-dlya-sozdaniya-korporativnyh-ii-agentov/ · https://exlibrisgroup.com/blog/artificial-intelligence-blog-series-transforming-the-library-experience-with-linked-open-data-and-ai/ · MTS IR (Q1 2026): https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
