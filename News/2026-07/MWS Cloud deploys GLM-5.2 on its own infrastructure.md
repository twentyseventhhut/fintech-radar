---
title: "MWS Cloud deploys GLM-5.2 on its own infrastructure"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - company/mws-cloud
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.kommersant.ru/doc/8816637
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: sf5ebaf17
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# MWS Cloud deploys GLM-5.2 on its own infrastructure

> [!info] 2026-07-17 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Коммерсантъ: MWS Cloud развернула GLM-5.2 на собственной инфраструктуре

## Первоисточники

### kommersant.ru
<https://www.kommersant.ru/doc/8816637>
*430 слов · direct*

Коммерсантъ. Технологии 
 
Облачный провайдер MWS Cloud, входящий в МТС Web Services, расширил каталог больших языковых моделей в сервисе MWS GPT Model Hub почти вдвое — до 17. Одним из новых решений стала разработанная китайской компанией Z.AI модель GLM 5.2.
Фото: Евгений Павленко, Коммерсантъ
По оценке старшего преподавателя факультета компьютерных наук НИУ ВШЭ Ивана Копылова, MWS Cloud первой в России развернула GLM 5.2 на собственной инфраструктуре. В этом случае инференс выполняется внутри российской инфраструктуры. «Запросы не передаются провайдеру модели или сторонним посредникам, а данные остаются в пределах российской юрисдикции»,— поясняет господин Копылов. По его мнению, это также снижает зависимость бизнеса от внешних сервисов и условий доступа зарубежных вендоров.
GLM 5.2 предназначена для анализа текстов, решения многошаговых задач и выполнения запросов с использованием внешних инструментов. Модель работает на инфраструктуре MWS Cloud Platform. Запросы пользователей обрабатываются в России и не передаются разработчику модели или другим зарубежным провайдерам, сообщили в компании.
По результатам внутреннего тестирования MWS AI, GLM 5.2 показала лучший результат среди исследованных компанией моделей в агентских задачах. В мировых рейтингах GLM 5.2 стала лидером среди открытых моделей в рейтинге Artificial Analysis Intelligence Index и продемонстрировала результаты, сопоставимые с GPT-5.5. Также GLM 5.2 заняла первое место в слепом бенчмарке Design Arena, где она опередила даже последнюю модель Anthropic, как Claude Fable 5.
В обновленный каталог также вошли Kimi K2.6 от Moonshot AI, Qwen3.6, Gemma 4 и GPT OSS. Разработчики могут выбирать модели с учетом требований к качеству, скорости работы и стоимости. Доступ к ним организован через единый совместимый с OpenAI API интерфейс, что упрощает переключение между решениями.
«В современной архитектуре агентских решений логично оркестрировать много моделей, каждая из которых лучше всего подходит для своего класса задач. Множество моделей, позволяющих работать с разными модальностями и объединенных с инструментами автоматизации и хранения данных в нашей облачной платформе, — именно то, что нужно бизнесу для оптимального решения прикладных задач», — заявил генеральный директор МТС Web Services Павел Воронин.
Кроме языковых моделей MWS Cloud добавила в сервис решения для распознавания и синтеза речи. В режиме предварительного доступа стали доступны Whisper Large v3, Qwen3 ASR 1.7B и Qwen3 TTS Custom Voice. Их можно использовать для расшифровки аудиозаписей, озвучивания текстов и разработки голосовых помощников.
В GPT Model Hub также появились реранкеры — инструменты, которые повторно сортируют результаты поиска и помогают выбирать наиболее релевантные фрагменты для передачи языковой модели. Такие решения применяются в системах генерации ответов на основе корпоративных документов и баз знаний.
Расширение доступа к открытым моделям может способствовать развитию здоровой конкуренции на рынке ИИ, считает главный инженер «Рокет Контрол» Павел Приходько. «В результате быстрее появляются новые модели и конечные ИИ-продукты, растет выбор для пользователей и бизнеса»,— отмечает он.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MWS Cloud deploys GLM-5.2 on its own infrastructure
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS: FRESH.** The corpus already covers GLM-5.2 the *model* (its release, benchmarks, geopolitics) in [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]], and the broader "firms pick Chinese open models to cut cost/keep control" trend in [[FT More firms pick Chinese AI models to cut costs]] and [[New low-cost Chinese AI model rivals Anthropic and OpenAI]]. But no prior note covers a **Russian cloud actually hosting GLM-5.2 on domestic infra**. This is the *demand/deployment* side inside Russia — a new, distinct event, not a re-report of the model launch. Fresh, but incremental (catalog expansion, not a strategic first).

## [0] What exactly happened (de-PR'd)
MWS Cloud (part of MTS Web Services, MTS's cloud arm) added **Z.AI/Zhipu's GLM-5.2** to its **MWS GPT Model Hub**, nearly doubling the catalog to **17 LLMs**. Same batch also added Kimi K2.6 (Moonshot), Qwen3.6, Gemma 4, GPT-OSS, plus speech (Whisper Large v3, Qwen3 ASR/TTS in preview) and rerankers. Access is via a **single OpenAI-compatible API** (source: Kommersant/kommersant.ru/doc/8816637; CNews 2026-07-17). Live, not just announced.
- **The real claim = data residency, not the model.** Inference runs inside MWS Cloud Platform in Russia; requests are not forwarded to Z.AI or foreign providers, data stays in Russian jurisdiction (quoted HSE lecturer I. Kopylov, who also calls MWS "first in Russia to deploy GLM-5.2 on own infra"). That "first in Russia for *this specific model*" is plausible but self-serving and unverifiable — Cloud.ru/Yandex have hosted GLM-family/DeepSeek/Qwen open models since 2025, so it is catalog catch-up dressed as a first.
- **What is NOT disclosed** (why it matters): no GPUs named, no quantization, no param variant, no per-token price. GLM-5.2 is a ~740B-param MoE (~40B active); serving it fully needs multi-H100/H200 FP8 — the un-named GPU provenance is the crux under Nvidia's export ban (analysis).
- The "best in agentic tasks / beats Claude Fable 5 on Design Arena / on par with GPT-5.5" lines are marketing lifted from the model's own positioning — true only **within the open-weight tier** (AA Intelligence Index #1 open-weight), not vs closed frontier.

## [1] Competitors / peers
Russian AI-cloud model hubs, all OpenAI-compatible, all commoditizing:
- **Cloud.ru (Evolution Foundation Models):** 20+ generative models incl. DeepSeek, Qwen, gpt-oss, Qwen3-Coder-480B; open-LLM hosting live since **2025** (free-access promo through 31 Oct 2025).
- **Yandex Cloud AI Studio:** ~24 models (Qwen, DeepSeek, Gemma + own YandexGPT); priced from ~0.5 ₽/1k tokens.
- **VK Cloud / Selectel:** GPU + open-model inference; Selectel a common H100/A100 rental venue.
- **Position:** MWS's Model Hub only launched **Mar 2026** (Inference Valve platform); rivals were earlier and broader. MWS is **at parity / slightly behind on catalog**; its edge is the **MTS telco/enterprise channel + in-country residency**, not being first. **Why this way (analysis):** model catalogs are now table stakes — differentiation has shifted to price, GPU availability, residency and enterprise integration, so MWS competes on distribution not model.

## [2] Company history / fit
MTS Web Services is MTS's bid to turn telco capex into a cloud/AI-platform business. Adjacent corpus: [[MTS Early Sol capability impressions and Cerebras serving path]] (MTS-branded AI commentary channel), and MWS AI already ships its own LLM (Cotype/Cotype Pro line, Apr 2026). **Fit (analysis):** hosting a strong Chinese open model *alongside* its own Cotype is a one-stop-shop / "orchestrate many models" play (CEO Voronin's quote), not an admission Cotype is weak — the margin is in the platform (compute + tools + data), so more models = more reasons to buy the platform.

## [3] Novelty / value-add / traction
- **What is genuinely new:** GLM-5.2 running on Russian soil with residency guarantees — useful for regulated RU enterprises that cannot send data abroad. The **model** is old news (corpus: [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]).
- **Traction: open.** No customer names, usage, or volume disclosed — announcement-ware until proven.
- **Where the margin sits (analysis):** the weights are free (MIT); MWS captures margin on **inference compute + platform lock-in (OpenAI-compatible API, tools, storage, rerankers)**. The fragility: that value rests on **scarce, sanctioned GPUs** MWS can't reliably source, and on a Chinese release cadence Russia can't influence.

## [4] What's next / market sentiment
- Russia AI-inference-PaaS is a fast-growing, import-substituted market (analyst est. ~high-teens % CAGR); domestic providers dominate by necessity. Expect every RU cloud to keep racking up open Chinese models (DeepSeek/Qwen/GLM/Kimi) as the default frontier-adjacent tier.
- **Why Chinese-open, not GigaChat/YandexGPT:** GigaChat (see [[Sber unveils flagship GigaChat 3.5 Ultra model]]) and YandexGPT are **rivals' closed models** MWS can't resell; MIT-licensed GLM can be run and monetized locally. Sovkombank (June 2026, cited in the Sber note) warned a truly sovereign DeepSeek-V4-class model needs a ~1.2 trillion ₽ datacenter — so leaning on Chinese open weights is the pragmatic near-term substitute.
- **Second-order risk (analysis):** the whole RU-cloud open-model strategy is one export-control tightening (GPUs) or one Chinese licensing shift away from disruption — cheap capability today, structurally fragile supply.

## Sources
- Kommersant (primary): https://www.kommersant.ru/doc/8816637
- CNews 2026-07-17: https://www.cnews.ru/news/line/2026-07-17_mws_cloud_razvernula_glm_52_v_sobstvennom
- MWS Inference Valve: https://mws.ru/ai/inference-valve/
- GLM-5.2 benchmarks: https://kie.ai/blog/glm-5-2-benchmark-deep-dive
- Cloud.ru EFM: https://cloud.ru/products/evolution-foundation-models
- Yandex AI Studio: https://yandex.cloud/en/services/ai-studio
- Internal: [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]], [[FT More firms pick Chinese AI models to cut costs]], [[Sber unveils flagship GigaChat 3.5 Ultra model]], [[MTS Early Sol capability impressions and Cerebras serving path]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is GLM-5.2 served at full ~740B params, or a smaller/quantized variant?** Open — no param/quant detail disclosed; likely FP8 given GPU constraints. Materially changes the "on par with GPT-5.5" claim.
2. **What GPUs power this, and are they sanctioned Nvidia obtained via gray-market?** Open — MWS lists A100/H100/H200 generically but ties none to this deploy. This is the load-bearing unknown.
3. **Is there a published per-token price for GLM-5.2 on MWS?** No public rate found — only generic "~15% cheaper than self-hosting" claims. Open.
4. **"First in Russia to deploy GLM-5.2 on own infra" — verified?** Only via one HSE lecturer's quote. Cloud.ru/Yandex hosted GLM-family/DeepSeek/Qwen since 2025; "first for exactly 5.2" is plausible but self-serving and low-stakes.
5. **Does "all compute stays in Russia" mean local weights, or a proxied Z.AI API?** Claim is local inference (MIT open weights make it credible), but not independently verified. Partly open.
6. **Any real customer traction, or announcement-ware?** Open — zero customer names, usage, or volume figures.
7. **Is "best for agentic tasks / beats Claude Fable 5" independently true?** Only within the open-weight tier (AA index #1 open-weight); marketing framing, not best overall.
8. **Why GLM over MWS's own Cotype?** Catalog/orchestration play, not a Cotype admission — margin is in the platform, not the model.
9. **Why a Chinese model over GigaChat/YandexGPT?** Those are rivals' closed models MWS can't resell; MIT GLM can be run and monetized locally.
10. **What breaks this strategy?** Tighter GPU export controls or a Chinese licensing/access shift — supply is structurally fragile despite cheap capability today.
11. **Is the residency guarantee legally/technically airtight for regulated RU data (152-FZ etc.)?** Open — claimed but no compliance detail.
12. **Does GLM-5.2 (Chinese-trained) carry content/safety-filter or provenance risks for RU enterprise use?** Open — not addressed.
13. **How durable is a 17-model catalog as differentiation?** Low — catalogs are commoditizing table stakes across all RU clouds.
14. **Is the AA Intelligence Index / Design Arena ranking recent and applicable to the served checkpoint?** Rankings are for the reference model; MWS's served variant/quant may differ. Open.

Importance: 3/5 — A real, live deployment with a genuine value proposition (Chinese frontier-adjacent open model with in-Russia data residency), which matters for the RU sovereign-AI/import-substitution theme and MTS's cloud strategy. But it is an incremental catalog expansion, not a strategic first (rivals host open LLMs since 2025), the differentiating facts (GPUs, price, quant, customers) are undisclosed, and the model itself is already covered in the corpus. Above a pure reprint, below a market-moving event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian cloud (IaaS+PaaS) reached ~RUB 226.9bn in 2025, +36.7% YoY; the full IaaS+PaaS+SaaS market ~RUB 416.5bn (+29.2% YoY), of which IaaS ~RUB 183.1bn, PaaS ~RUB 42.7bn (per iKS-Consulting, via CNews/servernews, 2025); forecast to pass RUB 1–1.2tn by 2030 (per TelecomDaily/ComNews, Nov-2025). MWS Cloud sits in the AI-infra sub-segment — cloud + a model-hub layer. Structure: consolidating oligopoly — top-5 providers hold ~72% of the market (2024: 71%, 2026e: 74%; per iKS/CNews); barriers are capital (data-centres, scarce GPUs), regulation (data-residency FZ-242), and distribution via parent telcos/banks. Why now: two forces converge — (1) mandatory data-localisation + Kremlin's "AI sovereignty" push (Putin at AI Journey Nov-2025 called reliance on foreign LLMs "unacceptable"; sovereign-AI bill Jun-2026, per Meduza) makes "inference stays in RF jurisdiction" the core sales pitch of this MWS release; (2) Chinese open-weight models (Qwen/DeepSeek/GLM/Kimi) surged from ~1.2% to ~30% of global open-model usage in 2025 (per Stanford HAI / Yahoo Finance), giving Russian clouds a frontier-adjacent model supply that no US vendor will license to them. GLM-5.2 topping Artificial Analysis' open-model index and matching GPT-5.5 (per note) is exactly what makes self-hosting attractive.

**Competitive landscape.** Sector KPIs: IaaS/PaaS revenue & growth, enterprise-customer count, GPU capacity, and (for a model-hub) number of served models + tokens/inference volume (MWS discloses none of the latter → `[UNSOURCED]`). Key players & shares (IaaS+PaaS combined, 2025, per iKS via CNews): Cloud.ru 32.5% (leader, ex-SberCloud), RTK-TsOD/Rostelecom 13.7%, Yandex Cloud 11%; on pure IaaS MWS is #5 at 6.2% (Cloud.ru 29.7%, RTK 15.7%, Selectel 8.4%, Yandex 7.3%). Basis of competition: price + product breadth + parent-group distribution, not network effects. Recent dated moves: Sber's flagship GigaChat 3.5 Ultra (MoE + linear attention, ~2x more compact) [[Sber unveils flagship GigaChat 3.5 Ultra model]] (2026-07-06); VK's Discovery AI neural search built on fine-tuned open-source weights [[VK launches Discovery AI neural search across products]] (2026-07-01); and MWS's own adjacent pushes — fastest ML S3 storage [[MWS Cloud launches fastest S3 storage for ML workloads]] (2026-07-02) and the RGB library AI-platform deal [[Russian State Library automates processes with MWS AI platform]] (2026-07-08). Protagonist position: catching up / niche — #5 in IaaS, but differentiating on a multi-model "orchestrate many models" hub (17 models, OpenAI-compatible API) rather than a proprietary frontier LLM. Moat is weak-to-moderate `(analysis)`: switching costs (a unified API layer) + MTS-group distribution, but no data/scale/IP moat — the models are third-party open weights any rival can also host.

**Comps & multiples.** MWS Web Services 2025 revenue RUB 63.8bn, +40% YoY, external revenue +53%, OIBDA >2x (per Telecompaper, 2026). No public valuation/EV disclosed → EV/Revenue, EV/EBITDA = **no data** (MWS is an unlisted MTS subsidiary; MTS PJSC on MOEX is not in $IRCOV → skipped per instructions; no free market-cap-for-MWS source → `[UNSOURCED]`). Internal comps (Russian cloud/AI peers in-base, qualitative — not valuation): [[Sber unveils flagship GigaChat 3.5 Ultra model]], [[VK launches Discovery AI neural search across products]], [[MWS Cloud launches fastest S3 storage for ML workloads]], [[Russian State Library automates processes with MWS AI platform]]. With <3 comparable valuation figures, distribution not computed — qualitative comparison only. Sanity note: 40% revenue growth is in line with peers (SberCloud/Yandex/VK each >35% enterprise-customer growth in 2025, per Telecompaper) — the segment is growing fast, so no over-valuation signal can be drawn absent price data.

**Risk flags.**
1. **GPU / hardware dependency (structural, sanctions).** Self-hosting GLM-5.2 needs accelerators Russia cannot legally import; the RF GPU market (~RUB 62.7bn in 2025) runs on smuggled Nvidia/AMD via India/third countries (per Tom's Hardware; TIME Jun-2026: hardware is Russia's "greatest AI weakness"). Second-order: inference capacity and unit economics are hostage to grey-market supply and price — the "our own infrastructure" pitch is only as durable as the smuggling channel.
2. **Commoditised, non-proprietary model layer.** GLM-5.2, Qwen, Kimi, Gemma, GPT-OSS are open weights any competitor (Cloud.ru, Yandex, VK, Selectel) can equally deploy; "first in Russia to host it" (per one HSE lecturer in the note) is a days-to-weeks lead, not a moat. Second-order: differentiation collapses to price + storage/latency, compressing margins in the very segment MWS is only #5 in.
3. **Model-sovereignty / regulatory whipsaw.** The sales pitch leans on "data stays in RF jurisdiction," yet the sovereign-AI bill (Jun-2026) and Kremlin rhetoric could tilt procurement toward *Russian-built* models (GigaChat/YandexGPT), for which a hub built around *Chinese* open weights is off-narrative. Second-order: state/enterprise demand could bifurcate, and a foreign-model-centric hub sits on the wrong side if rules harden.

**What this changes (idea-lens).** `(analysis)` Not a re-rating — a defensive product-catalogue move: MWS is buying frontier-adjacent capability it can't build, betting orchestration + jurisdiction beats owning a model. Falsifiable thesis: if the moat is real, MWS's external cloud revenue and Model-Hub usage should keep outgrowing the market (>36%) and lift its IaaS share above 6.2%; if it's just commoditised hosting, share stays flat while Cloud.ru/Yandex host the same models. Watch/trigger: (a) whether MWS discloses Model-Hub inference/token volumes (silence = weak traction); (b) any state-procurement rule favouring domestic-built LLMs, which would strand the Chinese-model hub; (c) a reported MWS/MTS Web Services IPO — the growth+OIBDA inflection is the setup, but no IPO is confirmed (`[UNSOURCED]`).

Sources: https://www.cnews.ru/reviews/oblachnye_servisy_2025/articles/rossijskij_oblachnyj_rynok_rastet · https://servernews.ru/1130487 · https://www.comnews.ru/content/242275/2025-11-12/2025-w46/1008/obem-rossiyskogo-oblachnogo-rynka-k-2030-g-pereydet-za-1-trln-rub · https://www.telecompaper.com/news/mws-revenues-up-40-in-2025--1564570 · https://tadviser.com/index.php/Article:Video_cards_(Russian_market) · https://www.tomshardware.com/tech-industry/artificial-intelligence/indian-firms-secretly-funneled-amd-nvidia-ai-gpus-to-russia-sanctions-reportedly-skirted-on-hundreds-of-millions-of-dollars-of-hardware · https://time.com/article/2026/06/18/russia-ai-putin-chip-us-china/ · https://meduza.io/en/news/2026/06/22/russia-revises-ai-regulation-bill-sovereign-models-remain-but-can-now-be-trained-on-non-russian-data · https://hai.stanford.edu/assets/files/hai-digichina-issue-brief-beyond-deepseek-chinas-diverse-open-weight-ai-ecosystem-policy-implications.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
