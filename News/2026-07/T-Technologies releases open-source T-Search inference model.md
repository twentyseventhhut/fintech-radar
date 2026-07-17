---
title: "T-Technologies releases open-source T-Search inference model"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - company/t-technologies
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.forbes.ru/tekhnologii/564945-t-tehnologii-vypustili-ii-model-t-search-dla-korporativnogo-mnogosagovogo-poiska
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s12eb2555
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# T-Technologies releases open-source T-Search inference model

> [!info] 2026-07-17 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Группа «Т-Технологии» представила открытую модель T-Search, позволяющую сократить инференс модели без дополнительных затрат на железо. Модель берет на себя самую дорогую и плохо стандартизированную часть Agentic RAG — управляет серией поисковых запросов к уже существующей базе, отслеживает, каких доказательств не хватает, сохраняет релевантные фрагменты и ранжирует их для последующей генерации ответа любой LLM.

## Первоисточники

### forbes.ru
<https://www.forbes.ru/tekhnologii/564945-t-tehnologii-vypustili-ii-model-t-search-dla-korporativnogo-mnogosagovogo-poiska>
*476 слов · direct*

Технологии 
 Бизнес 
«Т-Технологии» выпустили ИИ-модель T-Search для корпоративного многошагового поиска
 София Плетнева Редакция Forbes 
 Группа «Т-Технологии» выложила в открытый доступ T-Search — первую русскоязычную модель для Agentic RAG, технологии, которая позволяет ИИ-агентам самостоятельно выполнять многошаговый поиск информации в корпоративных документах, сообщили Forbes в пресс-службе компании.  
 Модель T-Search опубликована на платформе Hugging Face вместе с кодом, необходимым для ее интеграции в ИИ-агентов. 
 Компании могут скачивать ее, адаптировать под свои задачи и интегрировать в корпоративные продукты и сервисы. На разработку T-Search, включая вычислительные мощности для исследований и финального дообучения модели, а также зарплаты сотрудников, было потрачено 70 млн рублей. 
 В отличие от традиционных RAG-систем (Retrieval-Augmented Generation — технологии, при которой ИИ ищет информацию в документах и использует ее для подготовки ответа), T-Search сосредоточен не на генерации ответа, а на многошаговом поиске и сборе релевантного контекста из внутренних баз знаний, говорится в релизе. Затем этот контекст может использовать любая языковая модель. 
 Решение рассчитано на компании, которым приходится обрабатывать большое количество запросов ко внутренним данным и при этом соблюдать строгие требования к безопасности и затратам, указано в релизе. Среди них — телеком-операторы, маркетплейсы и e-commerce, страховые компании, медицинские и фармдистрибьюторы, логистические компании и сервисы доставки, следует из релиза. 
 По оценке разработчиков, использование T-Search в агентских ИИ-системах позволяет сократить затраты на инференс — то есть выполнение запросов языковыми моделями — на 20–50% в зависимости от сценария. Кроме того, T-Search можно запускать на собственной инфраструктуре компании. Это помогает снизить стоимость обработки запросов и справляться с пиковыми нагрузками без расширения  GPU-кластера. При этом решение помогает соблюдать требования по защите персональных и других чувствительных данных, поскольку информация не передается во внешние облачные сервисы. 
 T-Search построена на базе Qwen3.6-35B-A3B и работает как специализированный агент-ретривер (ИИ для поиска и отбора релевантной информации). Благодаря архитектуре с 35 млрд параметров, из которых одновременно используются только 3 млрд, модель можно запускать на одном графическом процессоре Nvidia H100. По данным разработчиков, это позволяет обрабатывать запросы до трех раз быстрее и снижать затраты на их обработку до пяти раз по сравнению с открытыми моделями сопоставимого качества. Кроме того, архитектура поддерживает параллельную работу нескольких поисковых агентов, что повышает качество поиска до 15%. 
 Директор центра искусственного интеллекта Т-Банка Дмитрий Ушанов, слова которого приводятся в релизе, отметил, что T-Search решает одну из ключевых задач корпоративных ИИ-агентов — поиск полного и достоверного контекста. По его словам, открытая публикация модели поможет компаниям быстрее внедрять такие решения и адаптировать их под свои задачи. При этом компактная архитектура позволяет до двух раз сократить требования к вычислительным ресурсам без потери качества многошагового поиска, делая технологию более доступной для организаций, которым важно локальное развертывание, добавил он. 
 Годом ранее, в июле 2025-го, «Т-Технологии» выпустили первую языковую модель с гибридным режимом рассуждений для ответов на запросы пользователей — T-Pro 2.0. Стоимость ее создания составила более чем 120 млн рублей. До этого, в 2024-м, компания выпустила первые большие языковые модели на 32 млрд параметров и на 7 млрд параметров — T-Pro и T-Lite.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: T-Technologies open-sources T-Search agentic-retrieval model
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-07-17 T-Technologies (the tech group behind Russia's T-Bank, ex-Tinkoff) published on Hugging Face (`t-tech/T-Search`, + FP8/NVFP4 quantized variants) an **agentic multi-step retrieval model** under **Apache 2.0**, with integration/reproduction code. De-PR'd, this is NOT a general chat LLM, NOT an embedding model, NOT a standalone reranker: it is a **search sub-agent** that plans and runs multi-round retrieval over an *existing* corporate index, tracks which evidence is still missing, keeps relevant snippets, and returns a ranked evidence set that any downstream LLM then uses to generate the answer. It owns "the most expensive and least standardized part of Agentic RAG" (its own framing).
- **Base / size:** a fine-tune of **Qwen3.6-35B-A3B** (Alibaba MoE) — ~35B total / **3B active** → runs on a **single Nvidia H100**. So it is built on a Chinese open base, not from scratch, and not on their own T-pro/T-lite (which are also Qwen-derived).
- **Training recipe:** SFT on ~11K synthetic search examples/language, then RL (GSPO with recall-based rewards), language-specific EN/RU experts.
- **Cost:** stated **RUB 70m** (compute + fine-tuning + salaries) — cf. T-Pro 2.0 a year earlier at >RUB 120m.
- **Vendor claims (all unverified):** up to 3× faster / up to 5× cheaper in tokens vs comparable open models; 20–50% inference-cost savings in agent scenarios; +15% search quality via parallel sub-agents; runs on-prem so data never leaves RU jurisdiction.
- **Why framed this way:** the "first Russian-language Agentic RAG model" + "open source" framing is a positioning claim, not a technical moat. The real, de-PR'd substance is a **task-specific fine-tune + a custom multi-round tool-use harness + an RU expert**, released free. → Why open-source it? Same playbook as T-Lite/T-Pro: seed ecosystem adoption, recruiting/brand in the AI-talent race, and lower the on-prem-deployment barrier so integrators standardize on T-stack (analysis).

## [1] Competitors / peers
Domestic RU foundation-model race is crowded and the same week is dense with it:
- **Sber — GigaChat 3.5 Ultra** ([[Sber unveils flagship GigaChat 3.5 Ultra model]], 2026-07-06): flagship MoE + linear-attention chat model. A full-stack proprietary LLM play — the opposite pole to T-Bank's "we release a narrow open component" strategy.
- **Yandex — YandexGPT 5 / wearables** ([[Yandex begins developing new wearable AI devices]]): the other big domestic foundation-model owner; T-Search publishes **no** head-to-head vs YandexGPT or GigaChat despite the "first in Russian" claim — a notable gap.
- **MWS Cloud — GLM-5.2 on-prem** ([[MWS Cloud deploys GLM-5.2 on its own infrastructure]], 2026-07-17, same day): MTS deploying a Chinese Z.AI model inside RU infra. Same underlying driver — data-residency / 152-FZ, inference kept in RU jurisdiction — but MWS *hosts a foreign model*, T-Bank *releases its own weights*.
- **VK — Discovery neuro-search** ([[VK launches Discovery AI neural search across products]], 2026-07-01): consumer neuro-search; adjacent "AI search" theme, different (B2C) target.
- Global open peers benchmarked by the vendor: Qwen3.6-27B, GLM-5.1, DeepSeek-V4-Flash. No Llama comparison.
→ Why the landscape looks this way: Sber/Yandex can amortize full-stack LLMs across huge platforms; T-Bank, smaller in AI headcount, gets more leverage from **owning one hard, reusable RAG primitive** and giving it away than from a me-too flagship chat model (analysis). Second-order: if integrators adopt T-Search as the retrieval layer, T-Bank captures mindshare *underneath* whatever LLM (GigaChat, Qwen, GLM) the customer runs on top — a wedge that is model-agnostic.

## [2] Company history / fit
T-Technologies has a consistent, dated open-source trajectory, all Apache 2.0 and all Qwen-derived:
- **2024:** first LLMs **T-Lite** (~7–8B) and **T-Pro** (~32B), on Qwen-2.5.
- **Jul 2025:** **T-Pro 2.0**, hybrid-reasoning, rebased on Qwen3 (>RUB 120m).
- Plus T-One (ASR/speech), RU eval sets (ru-mt-bench, ru-arena-hard), libraries (ETNA, Turbo Alignment).
- **2026-07-17:** T-Search continues the exact same pattern — adapt a Chinese open base, add RU expertise, release free.
Fit: logical and in-character. → Why: as a **bank**, not a hyperscaler, T-Bank's structural pressure is to deploy AI internally at low cost and on-prem (regulated PII), not to sell tokens. Open-sourcing narrow components is cheap marketing + recruiting in a talent-scarce, sanctions-isolated market where hiring signal matters (analysis). The AI-center head (Dmitry Ushanov) frames it as compute-cost reduction for corporate agents — consistent with a cost-center, not a product line.

## [3] Novelty / value-add / traction
- **Real novelty:** modest and specific — an RL-with-recall-reward training recipe + a bespoke multi-round agent harness + a Russian-language expert, packaged as a small (3B-active) drop-in retriever. That is legitimate engineering.
- **Not novel:** the base architecture (Qwen MoE) and the Agentic-RAG concept itself. "First Russian-language" is a scoping claim.
- **Benchmarks (vendor, single-rollout Recall@10, per press over RAGBench + FRAMES):** T-Search 55.96 vs GLM-5.1 53.96, Qwen3.6-27B 48.34, DeepSeek-V4-Flash 48.19, own Qwen3.6-35B-A3B base 41.54; with N=3 parallel rollouts → 61.33. **Caveat:** the biggest margin (+14.4) is over its *own* base — expected for a task fine-tune; the margin over the strongest external model (GLM-5.1) is just **+2.0**, and N=3 uses 3× compute. No domestic-model comparison. No independent verification.
- **Traction:** effectively **zero external** at launch — HF shows ~18 downloads/month, no third-party integrations, no external case studies. Internal use (support agent, B2B/corporate search) is *asserted*, not verified. → Where the value/margin sits: because it's model-agnostic and free, T-Search does not itself capture margin; the value to T-Bank is **ecosystem lock-in of the retrieval layer + talent brand**, not licensing revenue (analysis). What breaks it: if the retrieval quality is bottlenecked by the customer's underlying index (BM25/vector store) rather than the model, the "up to 5× cheaper" claim collapses to index-tuning, not the model.

## [4] What's next / market sentiment
- Marketed at telecoms, marketplaces/e-commerce, insurance, pharma/med-distributors, logistics — i.e. large RU enterprises with big internal corpora and strict PII/152-FZ constraints. Plans: swap the retrieval module of T-Bank's own AI support agent.
- **Structural driver:** RU sanctions + data-residency law make **on-prem, RU-hosted inference** the dominant enterprise constraint — the through-line linking T-Search, MWS/GLM-5.2, and GigaChat. Open weights you can run on one H100 fit that constraint far better than a foreign API.
- **Counterintuitive second-order:** a well-adopted *free* retrieval primitive could commoditize the "RAG integrator" layer that RU system-integrators sell today — good for T-Bank's mindshare, bad for those integrators' margins. And because it rides a Chinese base (Qwen), the whole domestic "sovereign AI" narrative quietly depends on continued access to Chinese open weights — a fragility, not a moat.
- Sentiment: same-day, Russian-only press cycle (Forbes.ru, CNews, bosfera, hi-tech.mail.ru); no independent/English coverage or third-party benchmark verification yet.

**Freshness: FRESH.** Genuine new product release with live Apache-2.0 weights on Hugging Face on 2026-07-17. No prior vault note covers T-Search or any T-Technologies open-source model; the Sber/MWS/VK/Yandex notes are adjacent peers, not the same event.

## Sources
- Forbes.ru (primary, in-note): https://www.forbes.ru/tekhnologii/564945-t-tehnologii-vypustili-ii-model-t-search-dla-korporativnogo-mnogosagovogo-poiska
- Hugging Face `t-tech/T-Search` (weights, Apache 2.0, benchmark card): https://huggingface.co/t-tech/T-Search — org: https://huggingface.co/t-tech
- CNews (2026-07-17): https://www.cnews.ru/news/line/2026-07-17_gruppa_t-tehnologii_predstavila
- bosfera press release: https://bosfera.ru/press-release/t-tehnologii-otkryli-dostup-k-modeli-dlya-agentnogo-poiska-t-search
- T-Bank open-source hub: https://ai.tbank.ru/opensource/
- Prior releases (Habr): T-Lite/T-Pro https://habr.com/ru/companies/tbank/articles/865582/ · T-Pro 2.0 https://habr.com/ru/companies/tbank/articles/928956/
- Internal: [[Sber unveils flagship GigaChat 3.5 Ultra model]], [[MWS Cloud deploys GLM-5.2 on its own infrastructure]], [[VK launches Discovery AI neural search across products]], [[Yandex begins developing new wearable AI devices]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. Can the RAGBench + FRAMES Recall@10 numbers be **independently reproduced** with the published harness, and specifically on Russian-language corpora? — Open; vendor-only, no third-party verification as of 2026-07-17.
2. Why is there **no benchmark vs YandexGPT 5, GigaChat 3.5, or their own T-Pro** — does T-Search actually beat a well-prompted domestic LLM at retrieval, or only foreign open models? — Open; conspicuous gap for a "first Russian" claim.
3. Is the N=3 → 61.33 gain a fair comparison given it uses **3× the compute** of the single-rollout baselines? What is the cost-normalized ranking? — Open.
4. The headline win is largest over its **own base** (Qwen3.6-35B-A3B, +14.4); margin over the strongest external model (GLM-5.1) is only +2.0. Is this a general advance or expected task-fine-tune overfitting to 8K synthetic questions? — Analysis: mostly the latter.
5. Does hitting these numbers **require the T-Technologies harness**? How portable is T-Search into an existing LangChain/LlamaIndex stack without it? — Open; portability = adoption ceiling.
6. Is retrieval quality bottlenecked by the customer's **underlying index** (BM25/vector store) rather than the model? If so, "up to 5× cheaper" is index-tuning, not the model. — Open.
7. What are the **real per-query economics** (H100 amortization + MLOps) behind "20–50% savings," and at what query volume does self-hosting beat an API? — Open; savings are scenario-dependent by the vendor's own wording.
8. Are the claimed **internal deployments** (support agent, B2B/corporate search) actually in production with a measured lift, or roadmap? — Open; asserted, not verified.
9. With ~18 HF downloads at launch and no external integrations, is there **any real developer traction** at 30/60/90 days, or is this primarily a recruiting/PR release? — Traction currently ≈ zero externally.
10. Does the **Qwen license/lineage** permit Apache-2.0 relicensing of the fine-tune, and what exactly is upstream "Qwen3.6-35B-A3B"? — Open; should be confirmed against Qwen repos.
11. What is the **EN vs RU performance split**? Is the "first Russian" framing masking that EN performance is unremarkable vs GLM/DeepSeek? — Open.
12. Strategic: since T-Search is **model-agnostic and free, capturing no direct margin**, what is the actual payoff for T-Bank — ecosystem lock-in of the retrieval layer, talent brand, or internal cost reduction? — Analysis: brand/recruiting + internal cost, not revenue.
13. Second-order dependency: the whole "sovereign RU AI" framing rests on a **Chinese (Qwen) base**. Does continued access to Chinese open weights make this a fragility rather than a moat? — Analysis: yes.
14. Does the RUB 70m stated cost include a full comparison-model eval suite, or only the T-Search training run? — Open; cost is a marketing figure.

Importance: 3/5 — a genuine, live Apache-2.0 open-source release from a credible RU AI group (fresh), fitting a consistent T-Lite/T-Pro playbook and a real market driver (on-prem/152-FZ data residency). But it is a narrow retrieval fine-tune of a Chinese base with only vendor benchmarks, near-zero launch traction, no domestic-model comparison, and no independent verification — solidly notable for the RU-fintech-AI beat, not a breakthrough. Not higher because there is no proven adoption and no verified performance edge; not lower because it is a real shipped open artifact with a clear strategic and cost rationale.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian enterprise LLM/AI is a three-to-four-horse race dominated by bank/tech incumbents, not independent labs: GigaChat (Sber), YandexGPT 5 / Alice AI LLM (Yandex), Cotype (MTS AI), and T-Tech's T-Pro/T-Lite/T-Search family. Structure is consolidated and captive — the models are built by the same balance sheets that own the largest distribution (banking, search, telco), so value accrues to the platform, not to a standalone-model market. "Why now": (1) sanctions cut Russian firms off from OpenAI/Anthropic/Google APIs and complicate frontier-GPU access, so import-substitution + locally-hosted models are a regulatory-and-necessity driver, not just a cost one; (2) the frontier has shifted from raw foundation models to *agentic* systems (Agentic RAG, tool-use), where inference cost per query — not one-off training — is the binding constraint, exactly the layer T-Search targets. Note that T-Search is not a from-scratch foundation model: it is built on Qwen3.6-35B-A3B (a Chinese open base), so the "first Russian-language Agentic RAG model" claim is about the fine-tune/retriever specialization, not the base weights (analysis).

**Competitive landscape.** Sector KPIs: inference cost/query, GPU footprint (models-per-H100), latency/throughput, and Russian-language benchmark quality vs global open models. Basis of competition = distribution + cost-efficiency on scarce local GPUs, less so raw capability. Recent moves: Sber open-sourced **GigaChat 3.5 Ultra** on 2026-07-06 (432B-param MoE, MIT licence on HuggingFace/GitVerse, positioned "close to DeepSeek 3.2"); Yandex rolled out the Alice AI model family (Feb 2026); T-Tech shipped T-Pro 2.0/2.1 (hybrid-reasoning, on HuggingFace) through 2025-26. T-Search (2026-07-17, HuggingFace, RUB 70m dev cost) claims 20-50% inference savings, up to 3x throughput / 5x cheaper vs comparable open models, +15% search quality via parallel retriever agents, one-H100 deployment (35B total / 3B active MoE). **Position:** niche/differentiated rather than head-to-head — instead of chasing Sber/Yandex on flagship model size, T-Tech targets the retriever sub-layer of the agent stack and open-sources it to seed adoption. Moat is weak on the model itself (open weights, Qwen-derived, replicable) but real on distribution and applied-AI talent inside a RUB 1.4tn ecosystem (analysis).

**Comps & multiples.** No in-vault Russian-LLM comps exist (fintech-weighted corpus; GigaChat/Yandex/MTS AI model releases are not held as notes). Nearest internal AI reference: [[Russian AI startup Mymeet.ai raises 16.5m roubles]] (RU applied-AI, not a comp on scale). External scale anchor (parent, MOEX:T / TCSG): FY2025 revenue **RUB 1.4tn (+49% YoY)**, operating net profit **RUB 174.4bn (+43%)**, **54.1m** customers, 34.3m MAU, ~17% of Russian retail turnover (per T-Technologies FY2025 IFRS, via bne IntelliNews). Model-economics arithmetic from the note: T-Search dev cost RUB 70m vs T-Pro 2.0 RUB 120m — i.e. this release is ~0.6x the cost of the prior flagship and a rounding error (~0.04%) against FY2025 net profit; AI R&D here is trivially funded, so cost is not the risk. Trading multiples: not computed — T-Technologies is a diversified bank, not a comparable AI pure-play, so EV/Rev vs Sber/Yandex would be apples-to-oranges; `[UNSOURCED]` on any AI-segment valuation.

**Risk flags.** (1) **Base-model dependence** — T-Search sits on Qwen3.6 (Chinese open weights); a licence change, an export/geopolitical restriction, or Qwen stagnation removes the foundation, and "Russian sovereignty" framing is undercut by a foreign base (second-order: sovereignty pitch is marketing, not architecture). (2) **Quality gap vs frontier** — independent reviews (2026) find Russian models still trail global leaders even on Russia-specific tasks; a specialized retriever inherits its base's ceiling, so the 20-50% cost claim is vendor self-reported and unverified `[UNSOURCED]`. (3) **Commoditization / no moat on the artifact** — open-sourcing a Qwen-derived retriever means Sber (GigaChat 3.5 Ultra, MIT) or any peer can match or absorb it; the giveaway is a distribution/ecosystem play, and monetization of the model itself is near-zero (why: value must be captured in downstream products, not the weights).

**What this changes (idea-lens).** (analysis) Signals the Russian AI contest is moving from "biggest model" to "cheapest agentic inference on constrained local GPUs" — a re-framing that favors incumbents with capital + distribution and squeezes independent labs. Falsifiable thesis: if T-Search sees real third-party enterprise adoption (telco/e-com/insurance named as targets) within ~2-3 quarters, T-Tech's open-source-to-seed strategy is working; trigger to watch — external deployment case studies or HuggingFace download/fork traction. What breaks it: if adoption stays internal-only, this is PR/talent-branding, not a market move.

Sources: https://www.intellinews.com/t-technologies-announces-ifrs-financial-results-for-4q25-and-fy-2025-432551/ · https://itbrief.co.uk/story/sber-launches-gigachat-3-5-ultra-as-open-source-ai · https://huggingface.co/t-tech · https://mysummit.school/blog/en/yandexgpt-review-2026/ · https://arxiv.org/html/2506.09440v1
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
