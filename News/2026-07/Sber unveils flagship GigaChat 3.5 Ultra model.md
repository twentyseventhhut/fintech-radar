---
title: "Sber unveils flagship GigaChat 3.5 Ultra model"
date: 2026-07-06
retrieved: 2026-07-06
tags:
  - company/sber
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.forbes.ru/tekhnologii/564345-sber-predstavil-novuu-model-gigachat-s-tehnologiej-linejnogo-vnimania
status: published
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sa3938c33
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Sber unveils flagship GigaChat 3.5 Ultra model

> [!info] 2026-07-06 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Представил флагманскую модель GigaChat 3.5 Ultra. Она построена на архитектуре с технологией линейного внимания и MoE (Mixture of Experts), быстрее генерирует текст и код и потребляет меньше ресурсов

## Первоисточники

### forbes.ru
<https://www.forbes.ru/tekhnologii/564345-sber-predstavil-novuu-model-gigachat-s-tehnologiej-linejnogo-vnimania>
*444 слов · direct*

Технологии 
«Сбер» представил новую модель GigaChat с технологией линейного внимания
 Евгения Белкова Редакция Forbes 
 «Сбер» представил новую флагманскую ИИ-модель GigaChat 3.5 Ultra для решения задач, связанных с написанием кода, проведения финансовых расчетов, работы с длинными текстами и автономными агентными сценариями, сообщили Forbes в пресс-службе банка. Новая модель почти вдвое компактнее, потребляет меньше ресурсов, однако при этом генерирует длинный текст до четырех раз быстрее. В основе модели — собственная отечественная архитектура с технологией линейного внимания, разработанная командой «Сбера», пояснили в финансовой организации.  
 «За счет архитектуры линейного внимания она не перечитывает текст заново, а накапливает контекст постепенно, как человек, который помнит суть разговора», — отметили в банке.  
 В «Сбере» также рассказали, что GigaChat 3.5 Ultra увереннее генерирует и проверяет код, а более точные и структурные ответы позволяют встраивать модель в рабочий процесс разработчика, аналитика или инженера. Кроме того, она эффективно анализирует контракты, технические регламенты, отчеты и другие объемные документы, не теряя точности и контекста. ИИ-модели также можно поставить задачу, и она сама найдет данные, напишет и выполнит код, обратится к нужному сервису и представит готовый результат, добавили в организации.  
 «На тестах, которые измеряют способность ИИ решать задачи по программированию, математике, выполнению сложных многошаговых заданий и качество русскоязычного диалога, GigaChat 3.5 Ultra превзошла предыдущую флагманскую модель «Сбера». А по ряду показателей приблизилась к результатам сильных открытых моделей, например к DeepSeek 3.2, при этом будучи почти вдвое компактнее», — подчеркнули в банке. 
 Старший вице-президент, руководитель блока «Развитие генеративного ИИ» Сбербанка Антон Фролов отметил, что количество экспериментов при разработке GigaChat 3.5 Ultra выросло до 1500. При обучении модели акцент был на созданных человеком текстах, прошедших классификацию и фильтрацию, она построена по архитектуре MoE (Mixture of Experts), добавили в «Сбере».  
 Модель работает с применением технологии линейного внимания. В отличие от классического «внимания» ИИ-моделей, где при каждом новом слове она заново сверяет его со всем предыдущим текстом, линейное внимание один раз «запоминает» суть и после дополняет эту память, пояснили в финансовой организации. 
 GigaChat 3.5 Ultra доступна пользователям бесплатно в ИИ-помощнике «ГигаЧат» для решения личных и рабочих задач, а также разработчикам в open-source, которые могут использовать ее для встраивания в свои сервисы и создания ИИ-агентов. Новая модель «Сбера» — одна из самых больших моделей с линейным вниманием среди всех, что выходили в open-source, подчеркнули в организации.  
 В июне 2026 года Совкомбанк спрогнозировал рост затрат и замедление темпов развития российскими игроками ИИ-моделей, если иностранные разработчики существенно ограничат доступ к новым версиям больших языковых моделей. При этом в случае «стратегического разворота» российские игроки могут создать суверенный ИИ мирового класса, подчеркнула организация. В банке также сообщили Forbes, что для обучения и поддержки работы суверенной большой языковой модели уровня китайской DeepSeek V4, вышедшей этой весной, необходимо создать специализированный центр обработки данных (ЦОД) стоимостью 1,2 трлн рублей.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sber unveils flagship GigaChat 3.5 Ultra model
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
Sber released **GigaChat 3.5 Ultra**, its new flagship LLM, with weights genuinely published on HuggingFace (`ai-sage/GigaChat3.5-432B-A28B` + `-base`/`-bf16`/`-GGUF`), MIT license (early July 2026; card "updated ~1h ago" on 2026-07-06 — consistent with a fresh release). Verifiable specs from the primary model card:
- **432B total / 28B active MoE** — i.e. ~40% *smaller* than the prior GigaChat 3.1 Ultra (702B/36B). The Forbes "почти вдвое компактнее" ("almost half as compact") is loose; the precise number is ~40% fewer total params.
- **Hybrid attention: MLA + GatedDeltaNet** — GatedDeltaNet is the real, published "linear-attention" mechanism (NVIDIA-lab origin). Native **FP8** training + **Multi-Token Prediction (2 heads)**. Context window **32,768 tokens** (modest by 2026 frontier standards).
- **"Up to 4x faster text generation" — UNVERIFIED / PR conflation.** The card's actual figures: ~20% throughput gain vs 3.1 Ultra, up to ~2.2x with idealized MTP-2 speculative decoding. The **only "4x" in the source is "~4x less KV-cache per token"** — a *memory* metric, not a speed metric. Treat "4x faster" as marketing.

**+ Why framed this way:** the efficiency pitch (smaller, FP8, linear attention, less KV-cache) is not a flex but a **compute-constrained necessity** — Russia lacks frontier GPU access (sanctions), so the only viable path is "do more with fewer chips per token." The PR conflating a memory metric into a speed claim is the tell that substance is being stretched.

## [1] Competitors / peers
- **Yandex (YandexGPT 5/5.1 Pro):** closest domestic rival, ~128K context, trained on ~2tn RU tokens; broadly a peer, sometimes ahead on general quality. **Not directly comparable on MERA** (YandexGPT excluded for licensing) — so no clean head-to-head exists.
- **T-Bank (T-Pro 1.0/2.0):** efficient open Russian models; **T-Pro 1.0 hit SOTA on MERA among open RU models** (arXiv 2512.10430) — a serious rival to Sber's open-weights strategy.
- **Global open reference:** DeepSeek V3.2 (685B/37B) and **V4 (1.6T/49B, Apr 2026, ~1M context)** are the capability yardstick; Qwen3, Llama, Kimi K2.5 the others.

**+ Why the landscape is this way:** competition here is **on distribution + data-residency, not frontier capability** — independent reviews place both RU flagships in the lower tier vs DeepSeek/Qwen/Kimi. Sber's real edge is compactness (fewer GPUs/token under scarcity) + MIT open-weights distribution, not algorithmic superiority.

## [2] Company history / fit
GigaChat trajectory: closed launch **Apr 2023**; GigaCode Dec 2023; GigaChat MAX Oct 2024; GigaChat 2.0 (2025); **GigaChat 3 Ultra Preview 702B/36B open-sourced MIT, Nov 2025**; **GigaChat 3.1 Ultra + GigaChat Ultra assistant, Mar 2026** (long-term memory, autonomous web search, code execution); now **3.5 Ultra (432B/28B), Jul 2026**. Strategy stack: SberDevices/Sber AI (models), AIRI (research), Kandinsky (image/video), GigaCode (coding), GigaChat Enterprise (agents).

**+ Why Sber acts this way:** open-weights MIT releases are a deliberate ecosystem play — lock Russian developers into a home-grown stack and reduce dependence on foreign models, precisely as those foreign models may become harder to access.

## [3] Novelty / value-add / traction
Genuinely new: a **432B-total MoE using GatedDeltaNet linear attention released under MIT** is plausibly "one of the largest linear-attention models in open source" (most large open MoEs use full/MLA attention, not linear). That claim is **plausible but unverified** (not in the model card I read; likely in the Habr blog). Benchmarks are **all vendor-reported, hours old, zero independent replication** — the "approaches DeepSeek 3.2 at half the size" line is **defensible on SWE-bench (42.6 vs 44.8) / Arena Hard (tie) but cherry-picked** (trails on MMLU 85.3 vs 87.5, MATH-500 86 vs 91.4); suspiciously large base-model HumanEval/MMLU-Pro leads are likely eval-harness artifacts. **Adoption is a data gap** — last concrete figure is 2.5M users (Feb 2024); GigaChat did appear on a16z's Top-100 Gen-AI consumer apps (Mar 2026), but no recent DAU/MAU.

**+ Where the value is real:** the durable value-add is efficiency-under-scarcity (real engineering) + permissive open-weights distribution (real ecosystem lever), NOT benchmark leadership. The margin isn't captured by GigaChat as a product line — Sber monetizes it as an ecosystem/superapp retention and enterprise-agent enabler.

## [4] What's next / market sentiment
The bigger story is **sovereign-AI economics.** Sovcombank (note "ЦОДы", 21 Jun 2026, analysts Troshin/Legostaev): if Chinese labs (DeepSeek) restrict open releases, RU players face rising costs/slower progress; a DeepSeek-V4-class sovereign LLM needs a ≥300 MW data center at **~RUB 1.2tn** capex — and Russia currently lacks the compute. A draft MinDigital law codifying "sovereign/national/trusted" AI (RU-soil training) would make data-residency the primary moat over raw capability. Gref reportedly explored buying Chinese silicon (May 2026); Sber is marketing GigaChat to Global-South states (Reuters, 3 Jun 2026).

**+ Second-order:** the release confirms Russia's frontier strategy is **efficiency + regulation-fenced distribution, not scale** — a rational response to GPU scarcity, but it caps ambition to "competitive laggard" rather than "frontier." Sovereignty here is as much a compute/capex problem as an algorithmic one.

## Sources
- PRIMARY (weights): https://huggingface.co/ai-sage/GigaChat3.5-432B-A28B (+ `-base`/`-bf16`/`-GGUF`); org https://huggingface.co/ai-sage ; GitHub https://github.com/salute-developers/gigachat3
- Sber/Habr: https://habr.com/ru/companies/sberdevices/articles/968904/ ; 3.1: https://habr.com/ru/companies/sberbank/articles/1014146/
- Forbes (note source): https://www.forbes.ru/tekhnologii/564345-sber-predstavil-novuu-model-gigachat-s-tehnologiej-linejnogo-vnimania
- Sovcombank/sovereign AI (Forbes, 21 Jun 2026): https://www.forbes.ru/tekhnologii/563277-ostorozno-kody-zakryvautsa-analitiki-ocenili-perspektivy-sozdania-suverennogo-ii
- DeepSeek V4: https://www.securitylab.ru/news/571988.php
- Independent skeptical review: https://mysummit.school/blog/en/gigachat-sber-review-2026/
- T-Pro 2.0: https://arxiv.org/html/2512.10430v1 ; GigaChat paper: https://arxiv.org/html/2506.09440v1
- Prior corpus notes: [[VK launches Discovery AI neural search across products]], [[Yandex begins developing new wearable AI devices]], [[2GIS founder Sysoev on investors and the sale to Sber]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is "up to 4x faster" real?** No — vendor card shows ~20% throughput, up to ~2.2x with idealized MTP-2. The "4x" is a *KV-cache memory* figure PR-conflated into a speed claim. **Answer: PR overstatement.**
2. **Does it really "approach DeepSeek 3.2"?** Partly — ties/leads on SWE-bench (42.6 vs 44.8) and Arena Hard, but trails on MMLU (85.3 vs 87.5) and MATH-500 (86 vs 91.4). Cherry-picked. **Open on independent eval.**
3. **Are any benchmarks independently verified?** No — all self-reported, model hours old. Zero third-party replication. **Open.**
4. **Are the base-model HumanEval/MMLU-Pro leads (80.5 vs 64; 74.5 vs 62) credible?** Suspicious — base evals are highly sensitive to prompt/harness formatting; competitor base evals often under-optimized. Treat as **likely inflated**.
5. **Is "half the size" accurate?** ~True on total params (432B vs 685B DeepSeek V3.2) but weaker on active (28B vs 37B). **Partly true.**
6. **Are the weights genuinely open?** Yes — on HuggingFace under **MIT** (commercial use). More permissive than most Western frontier models. **Verified.**
7. **Is "one of the largest linear-attention open-source models" true?** Plausible (large open MoEs mostly use full/MLA, not linear attention) but **not found in the model card — unverified vendor claim.**
8. **What's actual adoption?** Data gap — last concrete figure 2.5M users (Feb 2024); a16z Top-100 (Mar 2026) but no recent DAU/MAU. **Open.**
9. **Is this fresh or a re-run?** Fresh — a distinct new version (3.5, 432B) vs prior 3/3.1 Ultra (702B). No prior corpus note covers 3.5. **Fresh.**
10. **What is the real value-add?** Efficiency-under-compute-scarcity + open-weights distribution — NOT benchmark leadership. Genuine but narrow. **Answered.**
11. **Where is the margin captured?** Not in GigaChat as a P&L line — Sber monetizes via ecosystem/superapp retention + enterprise-agent enablement. **Answered (analysis).**
12. **Does the sovereign-AI subtext matter more than the model?** Arguably yes — Sovcombank's RUB 1.2tn / ≥300 MW DC estimate + compute shortfall reframes the whole story as capex/compute-bound. **Answered.**
13. **Is context length competitive?** No — 32K tokens is modest vs DeepSeek V4's ~1M. **A real limitation.**
14. **How does it stand vs YandexGPT / T-Pro?** No clean head-to-head (YandexGPT excluded from MERA; 3.5 too new); T-Pro 1.0 is SOTA among open RU models — Sber not clearly ahead. **Open.**
15. **What is Sber silent about?** Training-cost/compute source, real DAU, context-window limits, and any neutral benchmark rank. **Noted silences.**

**Importance: 3/5** — A real, MIT-open, efficiency-focused flagship from Russia's dominant AI player with a legitimate architectural angle (GatedDeltaNet linear attention) and a meaningful sovereign-AI/compute-scarcity backstory. But: incremental (3.5 vs 3.1), all-vendor benchmarks with a stretched "4x faster" claim, modest 32K context, no independent verification, and thin adoption data. Regionally notable, globally a laggard — solid mid-tier, not a headline.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-06]] (2026-07-06).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian foundation-model race, a two-horse contest inside a walled-off "sovereign AI" market. Sber's GigaChat 3.5 Ultra (linear-attention + MoE, "almost half as compact", up to 4x faster long-text generation, benchmarked near DeepSeek 3.2) is the flagship vs Yandex's YandexGPT 5 Pro (trained on 2tn RU tokens, ~128K context; per appleinsider.ru / albato.ru, 2026). "Why now": (1) sanctions cut off NVIDIA/AMD H100/B200 supply, pushing Russian players to Chinese chips — Gref reportedly discussed buying Chinese-made silicon in China in May 2026 to power GigaChat (per cloudnews.tech); (2) a draft MinDigital law codifies "sovereign / national / trusted" AI models requiring RU-soil training (per Reuters via US News, 2026-06), turning compliance/data-residency into the primary moat rather than raw capability. Compute is the binding constraint: Sovcombank estimated a DeepSeek-V4-class sovereign LLM needs a dedicated data center costing ~RUB 1.2tn (per note text); separately Sber reportedly requested RUB 450bn for a DC and was turned down (per search, unverified primary). No independent TAM for the RU LLM market — no data.

**Competitive landscape.** Sector KPIs: MAU / query volume, benchmark rank (coding/math/RU dialog), context window, active-vs-total params (MoE efficiency), and — uniquely here — economic effect captured inside the owner's ecosystem (Sber doesn't sell GigaChat as a standalone P&L line). Players: Sber (GigaChat) and Yandex (YandexGPT/Alice) as the two scaled incumbents; open Chinese models (DeepSeek) as the de-facto capability benchmark and a substitute for RU enterprises. Basis of competition: ecosystem lock-in + data residency, NOT frontier capability — both RU models sit in the lower tier of independent rankings and "regularly make factual errors" (per mysummit.school, 2026). Recent moves: Sber launched a reasoning-mode GigaChat Ultra in Mar 2026; Sber is marketing GigaChat to Global South states (Reuters, 2026-06-03). Protagonist position: **domestic leader, global laggard** (analysis) — GigaChat 3.5 Ultra's edge is compactness/efficiency (fewer GPUs per token, matters acutely under compute scarcity) and open-source distribution ("one of the largest linear-attention models released open-source", per note). Moat = distribution/switching costs inside the Sber superapp + regulatory data-residency, not algorithmic superiority (intangibles moat is thin).

**Comps & multiples.** GigaChat is not a standalone asset — no valuation/round/multiple to compute; it is an internal capability of Sber. So EV/Rev, P/S = **no data / not applicable**. Disclosed monetization proxies (per Sber/Gref via TASS, Interfax, tadviser, 2025–26): total AI economic effect ~RUB 450bn in 2025 (Gref's broader "AI financial effect" figure of RUB 1.75tn is a wider methodology — treat cautiously); GenAI-specific effect ~RUB 30bn in 1H2025 and >RUB 50bn attributed to GenAI for the year; GigaChat MAU >20mn, >800mn queries/yr; guided AI effect RUB 550bn in 2026 on ~RUB 350bn AI capex (per Interfax). Arithmetic sanity: even RUB 50bn GenAI effect ÷ ~RUB 1.7tn FY2025 net profit ≈ **~3%** of profit — material but not yet a re-rating driver. Internal comps (semsearch notes table unavailable → grep): [[Revolut publishes PRAGMA banking foundation model with NVIDIA]], [[Plaid unveils transactional foundation model for intelligent finance]], [[Base44 launches own AI model to seek defensibility]] (bank/fintech building proprietary foundation models), and [[Linas Newsletter EU AI sovereignty push after Anthropic export order]] / [[Amazon raises AWS GPU reservation prices about 20% amid chip shortage]] (sovereignty + compute-scarcity backdrop).

**IR grounding (Sber FY2025 IFRS, reported 2026-02-26).** Net profit +7.9% to ~RUB 1.7tn (~$22bn); ROE ~22.7% (per Sber 2025 slides via Investing.com); net interest income +18.5% to RUB 3.55tn; net fee & commission income RUB 833.7bn (-1.1% YoY) (figures per TASS/Investing.com press; primary doc: Sber Summary Consolidated IFRS FS 12M 2025, https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf). Reading: a >RUB 1.7tn-profit bank guiding RUB 350bn AI capex for 2026 can bankroll the compute race from balance-sheet strength — GigaChat is a cost-cutting/retention tool funded by the core bank, not a business that must stand alone.

**Risk flags.**
1. **Compute dependency / single point of failure** — training and serving hinge on Chinese GPU supply after Western chip sanctions; any tightening (or Chinese export controls) directly caps model scale and cadence. This is the sector's hardest constraint and it is external to Sber's control.
2. **Capability gap vs cost** — RU models trail DeepSeek/frontier labs and sit low in independent rankings while AI capex rises to RUB 350bn (2026); if the "sovereign premium" (data residency) fails to convert to durable revenue, spend outruns monetization (GenAI effect still ~3% of profit).
3. **Monetization opacity / disclosure quality** — Sber's headline "AI effect" figures (RUB 450bn–1.75tn) mix cost-savings, pricing and credit-risk estimates with revenue and are not audited line items; the real standalone GigaChat P&L is not disclosed — treat effect claims as management estimates, not booked revenue.

**What this changes (idea-lens).** GigaChat 3.5 Ultra reframes the RU race around **compute-efficiency, not capability** — MoE + linear attention is an explicit answer to GPU scarcity, and open-sourcing it is a distribution/soft-power play (Global South) rather than a monetization one (analysis). Falsifiable thesis: if Sber secures Chinese-chip DC capacity (watch for a funded RUB 1.2tn-class DC or a China chip-supply deal) AND GenAI economic effect clears ~RUB 100bn+, GigaChat becomes a genuine efficiency moat for the bank; trigger to watch = the next MinDigital "sovereign AI" law text (mandated procurement) and Sber's 2026 AI-effect disclosure. What breaks the thesis: a Chinese GPU-supply squeeze or DeepSeek/open-model substitution eroding the data-residency premium.

Sources: https://www.forbes.ru/tekhnologii/564345-sber-predstavil-novuu-model-gigachat-s-tehnologiej-linejnogo-vnimania · https://tass.com/economy/2092243 · https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · https://interfax.com/newsroom/top-stories/114913/ · https://tadviser.com/index.php/Article:Artificial_intelligence_in_Sberbank · https://money.usnews.com/investing/news/articles/2026-06-03/russias-sberbank-offers-ai-model-to-global-south-states-keen-to-bridge-digital-divide · https://cloudnews.tech/russia-looks-to-china-to-power-gigachat-its-alternative-to-chatgpt/ · https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Not a results release. GigaChat 3.5 Ultra is a product/AI-model announcement, not an earnings print. This section reframes as **Sber's latest reported financial health** — the balance-sheet capacity behind its AI spend. Latest filing: **Summary Consolidated IFRS Financial Statements 12M 2025 (FY2025)**, published 2026-02-26.

**Verdict (context read).** Sber enters its heaviest AI-investment cycle from a position of strength but *decelerating* returns: FY2025 IFRS net profit **RUB 1,705.9bn (+7.9% YoY)** — a third consecutive record — yet **ROE fell to 22.7% from 23.4% in 2024** as the Russian macro/rate slowdown bit. Fee income turned slightly negative. Capital and NII give ample funding headroom for GigaChat/GenAI capex; profitability momentum is the flag.

**Key figures (FY2025 IFRS, YoY).**
- Net profit: **RUB 1,705.9bn, +7.9% YoY** (2024: ~RUB 1,580bn). Third straight record.
- ROE: **22.7%** vs **23.4%** in 2024 — down ~0.7pp (still well above cost of equity).
- Net interest income: **RUB 3.56tn (RUB 3,556bn), +18.5% YoY** — the main earnings driver; NIM expanded from 6.0% (Q4 2024) to **6.5% (Q4 2025)**.
- Net fee & commission income: **~RUB 833.7bn, -1.1% YoY** (2024 base ~RUB 842.9bn) — the soft spot: fees flat-to-down while NII carried the print.
- Cost of risk (CoR): **1.3%**.
- Capital adequacy (N20.0): **13.7%**, vs regulatory minimum 11.5% — explicitly cited as headroom to grow lending, pay dividends *and* invest in development.

**By driver.** Growth was **rate-driven, not fee-driven**: +18.5% NII (margin expansion in a high-rate environment) offset a -1.1% fee line and a rising cost of risk, netting +7.9% profit. The ROE dip (-0.7pp) reflects earnings growing slower than the equity base — i.e. profitability per ruble of capital is easing even as absolute profit sets records.

**vs expectations / prior period.** No formal sell-side consensus in the corpus [UNSOURCED for a numeric beat/miss]; qualitatively FY2025 landed **in-line-to-modestly-positive** — the ~RUB 1.7tn / +7.9% and ~22.7% ROE tracked pre-print guide (management had guided ROE ≥22% and flagged higher YoY profit; Sber "expects higher profits in annual terms"). Cost-to-income ratio for FY2025: **no data** in the public releases reviewed (not disclosed in the summary results) [UNSOURCED]. Momentum vs 9M 2025 (net profit RUB 1,307bn; Q3 alone RUB 448bn) implies a Q4 in the ~RUB 400bn range — steady, not accelerating.

**Guidance / forward (context for AI spend).** FY2025 print keeps Sber comfortably able to self-fund AI: N20.0 at 13.7% (220bp above the 11.5% floor) and RUB 3.56tn NII underwrite record dividends (~RUB 37.6/share approved, ~8% growth) *and* continued GenAI investment. Note the note's own de-PR anchor: Sovcombank (June 2026) put the price of a sovereign DeepSeek-V4-class LLM data centre at **RUB 1.2tn** — roughly 70% of Sber's *annual* net profit, a useful scale check on how capital-intensive the frontier-model race is even for the sector's most profitable player. Sber's capacity to absorb this is high; the return on it is unproven.

**Thesis-flags.**
1. **ROE deceleration (22.7% ← 23.4%).** Fact: profit up but return on capital down. Why: rate cycle peaking, cost of risk rising, equity base compounding. Why it matters: the margin tailwind (NIM 6.5%) that funded the record is cyclical and reverses as rates fall. Second-order: if NII normalizes, AI/tech spend competes harder with dividends for a shrinking incremental-return pool.
2. **Fee income -1.1%.** The one line that shrank. Sber's AI push (GigaChat embedded in developer/analyst workflows, agentic scenarios) is partly a *strategic answer* to soft fees — monetizing the tech stack. Watching whether GenAI converts to fee/services revenue is the real thesis link between this product news and the P&L.
3. **Self-funding capacity intact.** 13.7% capital + RUB 3.56tn NII = GigaChat capex is affordable without straining dividends today; the RUB 1.2tn sovereign-DC benchmark shows the ceiling if the AI arms race escalates.

Sources: Sber Summary Consolidated IFRS Financial Statements 12M 2025 (FY2025), 2026-02-26 — https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf (primary; binary PDF, figures cross-checked via press) · RBC 2026-02-26 (record profit, ROE 22.7% vs 23.4%) https://www.rbc.ru/finances/26/02/2026/699f2bd79a7947fc6f105946 · TASS (net profit +7.9%, ~RUB 1.7tn) https://tass.com/economy/2092243 · Investing.com Sber 2025 slides (22.7% ROE) https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · Cost-to-income FY2025: no data [UNSOURCED].
<!-- /enrichment:earnings_review -->
