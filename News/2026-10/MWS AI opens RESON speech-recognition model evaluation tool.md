---
title: "MWS AI opens RESON speech-recognition model evaluation tool"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/mts
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-10-06_mws_ai_otkryla_svoj_instrument
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s4b4cbe35
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# MWS AI opens RESON speech-recognition model evaluation tool

> [!info] 2026-10-12 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Открыл доступ к RESON — инструменту MWS AI для оценки моделей распознавания речи по более чем 10 метрикам

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-10-06_mws_ai_otkryla_svoj_instrument>
*663 слов · direct*

Эльяс Касми

 MWS AI открыла свой инструмент для оценки моделей распознавания речи
 
 
 MWS AI (входит в МТС Web Services ) выложила в открытый доступ RESON (Research Engine for Speech Observation & Notes) — инструмент для комплексной оценки качества моделей автоматического распознавания речи (ASR). Он позволяет сравнивать модели по более чем 10 метрикам и автоматически формирует интерактивный HTML-отчет с результатами анализа. RESON стал первой открытой разработкой MWS AI в области распознавания речи. Об этом CNews сообщили представители MWS AI .
Чтобы проанализировать качество модели с помощью RESON, пользователю необходимо загрузить результаты распознавания модели и эталонные расшифровки. Инструмент позволяет привести тексты к единым правилам, чтобы некритичные различия в написании слов не влияли на итоговую оценку качества, а также проводит анализ по выбранным метрикам и сравнивает результаты. На выходе формируется интерактивный отчет, который открывается в формате веб-страницы. Его можно использовать для технического анализа и для наглядного представления результатов бизнес-команде.
RESON поддерживает более 10 метрик, которые можно настраивать под свои задачи. В числе доступных, например: WER (Word Error Rate) — показывает количество ошибок при распознавании слов; CER (Character Error Rate) — рассчитывает ошибки на уровне отдельных символов; MWA (Mean Word Accuracy) — дает каждому уникальному слову одинаковый вес и помогает заметить ошибки на словах, которые редко встречаются в данных, например названиях компаний, продуктов или сервисов.
WIS ( Word Importance Score) — разработанный MWS AI показатель, который помогает находить слова, которые почти не влияют на общий результат, но важны для конкретного сценария — например название брендов и продуктов, англицизмы. Он учитывает, как часто встречается слово, насколько плохо оно распознается, какие ошибки возникают и на какие варианты модель его заменяет. Это позволяет, в частности, приоритизировать улучшения модели в отраслевых сценариях.
RESON доступен в формате открытой Python -библиотеки. Его можно встроить в существующие процессы разработки через командную строку или Python API и развернуть в собственной инфраструктуре компании, в том числе в закрытом контуре. Инструмент рассчитан на команды, которые сравнивают разные версии моделей и на компании, выбирающие между решениями разных разработчиков.
 Новый открытый бенчмарк для оценки моделей MWS RESON ASR OSD 
Вместе с RESON MWS AI опубликовала MWS RESON ASR OSD — открытый бенчмарк (набор данных и правил для сравнения моделей в одинаковых условиях) с готовыми русскоязычными аудиоданными для оценки качества моделей распознавания речи. Он включает более 12 тыс. размеченных аудиозаписей общей длительностью около 38 часов и ориентирован в том числе на сценарии голосовой связи и контакт-центров .
В бенчмарке представлены два типа данных: разговорная речь и фразы с числами и числовыми последовательностями. В него входят обращения в поддержку, автоматические уведомления и бытовые звонки, а также телефонные номера, счета, даты, суммы и другие данные. Записи представлены как без выраженных помех, так и с акустическим шумом и фоновой речью — например, звуками телевизора или посторонними голосами. В данных также встречаются англицизмы и названия компаний, банков , операторов связи , цифровых сервисов, устройств и приложений.
В рамках публикации бенчмарка MWS AI провела замеры качества открытых моделей Сбербанка, Alpha Cephei, Nvidia и OpenAI . Модели сравнивали по WER — показателю, который отражает количество ошибок при распознавании слов. Среди моделей, протестированных на всех четырех наборах данных, лучший средний результат показала GigaAM v3 от Сбера : средний WER составил 7,42%. У Vosk показатель составил 11,07%, у Nvidia Parakeet — 15,83%, у Nvidia Nemotron — 25,52%. GigaAM допускала более чем вдвое меньше ошибок, чем Nvidia Parakeet, и более чем втрое меньше, чем Nvidia Nemotron. На втором месте по точности другая российская разработка – Vosk от Alpha Cephei.
«RESON изначально создавался для внутренних задач команды. Раньше оценка качества фактически собиралась из нескольких инструментов: отдельно считались метрики, отдельно разбирались ошибки, а результаты приходилось сводить вручную. RESON объединил этот процесс в одной системе — от подготовки данных до сравнения моделей и разбора конкретных ошибок. Анализ, который раньше мог занимать несколько часов, сократился до 10–15 минут. Сейчас мы открываем этот подход индустрии — это наш вклад в формирование общего подхода к оценке ASR-моделей, как минимум на русскоязычных данных», — сказал руководитель команды распознавания речи MWS AI Александр Шевченко . 
 10 функций Telegram, о которых вы не знали: наводим порядок в чатах

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MWS AI opens RESON speech-recognition model evaluation tool
_Analytical notes (not a post). Importance: 2/5._

**Freshness verdict: FRESH.** No prior note covers RESON or an MWS ASR benchmark. Related MTS/MWS speech items exist ([[MTS Link adds Chinese speech recognition and 19-language subtitles]], [[MTS Secretary learns to answer calls in subscriber's voice]], [[Russian State Library automates processes with MWS AI platform]], [[MWS Cloud deploys GLM-5.2 on its own infrastructure]]) but none is the same announcement — this is MWS AI's first open-source release in speech recognition.

## [0] What exactly happened (de-PR'd)
MWS AI (AI arm of MTS Web Services / telecom MTS) open-sourced two linked artifacts under MIT:
1. **RESON** (Research Engine for Speech Observation & Notes) — a runnable Python eval harness: ingests ASR hypotheses + reference transcripts, normalizes text, computes 10+ metrics (WER, CER, MWA + their proprietary **WIS** Word Importance Score), runs significance tests, emits a self-contained HTML report. Pitched as cutting internal eval from "hours → 10–15 min".
2. **MWS RESON ASR OSD** — an open benchmark: **12,114 recordings / ~37h52m**, 8 kHz mono telephone audio, conversational + numeric domains × quiet/noisy conditions, gender-balanced, Russian call-center focus.

Published benchmark run (avg WER): **Sber GigaAM v3 7.42%** (best), Vosk/Alpha Cephei 11.07%, Nvidia Parakeet 15.83%, Nvidia Nemotron 25.52% (Whisper Large v3 Turbo shown per-domain, no avg; collapses to 62% noisy).

**Why structured this way / what it reveals:** The single defining tell is that MWS AI's OWN commercial ASR stack (Audiogram) is ABSENT from the results — they benchmarked five competitors and omitted themselves. Scoping to "open models" conveniently excludes both the strongest proprietary Russian rivals (Yandex SpeechKit, Tinkoff VoiceKit, Sber's paid SaluteSpeech) AND MWS's own paid product, letting MWS pose as a neutral referee rather than a scored entrant. Crowning a Russian model (Sber) over OpenAI/Nvidia also serves an import-substitution PR frame (Lenta.ru ran "Russian neural net beat OpenAI and Nvidia"). The repo carried an MIT license tagged ~2026-06-24, months before the 2026-10-06 coordinated PR launch — a staged launch event, not first publication.

## [1] Competitors / peers
Russian ASR landscape: **Sber (GigaAM v3 / SaluteSpeech)** is the clear open leader (GigaAM v3, MIT, ~700k hrs incl. call-center) — MWS's own benchmark confirms it on top; **Yandex SpeechKit** and **Tinkoff VoiceKit** (proprietary, excluded here); **Alpha Cephei Vosk** (open lightweight baseline, 11%); **Nvidia Parakeet/Nemotron** and **OpenAI Whisper** (not tuned for 8 kHz Russian telephone, so they underperform — a home-turf matchup, not apples-to-apples). On the benchmark-tooling axis the peers are HuggingFace Open ASR Leaderboard (arXiv 2510.06961, 86 models/12 datasets), Nvidia NeMo, jiwer, SpeechBrain, Mozilla Common Voice, Sber Golos.

**Why the landscape is this way:** A telecom releasing its own eval dataset/leaderboard is common and well-precedented — motive is standard-setting on home turf (Russian 8 kHz telephone, where MWS holds proprietary data others lack), cheap credibility/recruiting, and steering the metric (WIS reframes "quality" toward call-center error criticality, the dimension MWS's own Audiogram competes on). Second order: whoever authors the accepted benchmark shapes what "good ASR" means for the Russian call-center market.

## [2] Company history / fit
MWS AI = AI center under MTS Web Services (cloud/AI arm of MTS). Portfolio: **Cotype** LLM family (Cotype Pro 2 / Pro 2.5, claimed #1 Russian on MERA), an AI Agents Platform across ~7 verticals, and **Audiogram** (its commercial ASR/TTS call-center stack). MTS Web Services announced ~1 bn RUB into AI services; MTS AI claims >1 bn RUB saved by moving training/inference to MWS cloud. This RESON release is MWS AI's FIRST open-source move in speech — a toe-in-water from an otherwise closed/commercial ASR business.

**Why MWS acts this way:** A commercial ASR vendor gains more from owning the yardstick than from winning a public leaderboard it doesn't control. Open-sourcing a benchmark (not its model) plants MWS's flag + metric (WIS) on Russian-telephone ASR evaluation at near-zero cost, drives recruiting/credibility, and sidesteps the risk of being directly outscored by GigaAM. Fits the broader MTS AI/cloud import-substitution narrative.

## [3] Novelty / value-add / traction
Novelty is **moderate**. The tool is a competent-but-not-unique harness (NeMo/jiwer/SpeechBrain/HF leaderboard all do similar). Genuine value sits in two places: (a) the benchmark's niche — 8 kHz noisy Russian telephone + numeric-sequence domains, a real gap vs clean read-speech corpora (LibriSpeech, Golos, Common Voice); (b) the **WIS metric** (criticality-weighted errors: freq 25% / F1 severity 35% / error-type 25% / substitution diversity 15%) — original and call-center-relevant, but a bespoke composite with arbitrary weights and no external validation.

**Traction: near-zero.** GitHub ~6 stars / 0 forks; HF dataset ~837 downloads/month, 1 discussion. All Oct-6 coverage traces to one press release (churnalism) — no independent reproduction. **ANNOUNCED, not ADOPTED.** Who captures value in the stack: if RESON/OSD becomes the cited Russian-telephone ASR standard, MWS owns the definition of "quality" — but that depends on third-party adoption that has not materialized.

## [4] What's next / market sentiment
Watch for: (a) will MWS ever publish Audiogram's own RESON score, or keep it private (the silence is the story); (b) third-party adoption/citation of RESON/OSD; (c) whether Sber/Yandex engage or ignore; (d) whether this is a precursor to open-sourcing an MWS ASR model or a one-off marketing artifact. Sentiment: credible, genuinely runnable standard-setting/credibility play — but with zero independent validation and near-zero adoption, and wrapped in an overstated nationalist frame. Low near-term market impact.

## Sources
- cnews.ru 2026-10-06 (primary, in note): https://www.cnews.ru/news/line/2026-10-06_mws_ai_otkryla_svoj_instrument
- HuggingFace dataset MTSAIR/mws-reson-asr-osd; GitHub mts-ai/RESON; Habr mts_ai/1088946
- Lenta.ru 2026-10-06 (note: mislabels Nemotron's 25.52% as "OpenAI" — press error, do not propagate)
- GigaAM v3 (developers.sber.ru; github salute-developers/GigaAM); HF Open ASR Leaderboard (arXiv 2510.06961)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Challenge / red-team (second-order)

1. **Is RESON actually open and runnable, or just announced?** — Real & runnable. MIT-licensed, pip-installable, live GitHub repo + HF dataset. Confirmed.
2. **Any independent reproduction of the numbers?** — NO / open. All Oct-6 coverage (CNews, Lenta, Computerra, Content-Review) traces to one MWS press release. Nobody has re-run it.
3. **Why is MWS's own Audiogram model absent from results?** — Unstated. Likely (a) it's not an "open model," letting MWS pose as neutral referee; and/or (b) it would underperform Sber GigaAM on MWS's own benchmark. The silence is the story.
4. **Would Audiogram beat 7.42% on this set?** — Open. No published figure. Suspicious that a call-center ASR specialist omits itself from a call-center benchmark it designed.
5. **Is the benchmark gamed toward a vendor?** — No favoritism evident (a competitor, Sber, wins). But MWS controls data selection + WIS weighting — standard benchmark-authorship bias risk. Open.
6. **Why only OPEN models (no Yandex SpeechKit, Tinkoff VoiceKit, paid SaluteSpeech)?** — Reproducibility is a defensible reason, but it conveniently excludes the strongest proprietary Russian rivals AND MWS's own paid stack. Partly PR-convenient.
7. **Is the "beat OpenAI/Nvidia" narrative sound?** — Only partially. Russian-tuned GigaAM beating Whisper/Parakeet/Nemotron on 8 kHz noisy Russian telephone is a home-turf matchup; foreign models aren't built for it. Nationalist framing (esp. Lenta) overstates it.
8. **Is 12k recordings / ~38h a large benchmark?** — Modest. Enough for a focused telephone benchmark; small vs LibriSpeech (~1000h) or Golos (~1000h). Niche depth over breadth.
9. **Is WIS a real advance or marketing?** — Useful idea (weight errors by criticality for call-center QA), but a bespoke composite with arbitrary weights (25/35/25/15) and no external validation. Open whether anyone adopts it.
10. **Credibility/recruiting, standard-setting, or genuine contribution?** — All three, weighted to standard-setting + credibility. Genuine (real code/data, fills a niche) but strategically self-serving: plants MWS's flag + metric on Russian-telephone ASR eval without exposing its own model.
11. **Is adoption real?** — NO. ~6 GitHub stars / 0 forks / ~837 HF downloads. Announced, not adopted.
12. **Why the ~June-2026 repo date vs Oct-6 announcement?** — Code/tag predates the PR push by ~3.5 months; a staged launch event, not first publication. Benign but notable. Open.
13. **Did the press get the numbers right?** — No — Lenta.ru mislabels Nemotron's 25.52% as "OpenAI." Trust the HF dataset card, not the headlines.
14. **Does this signal MWS will open-source its ASR model next?** — Open. First speech open-source move; could be precursor or one-off. Watch Audiogram.
15. **What is MWS silent about?** — Its own model's score; any proprietary/paid competitor comparison; any independent validation; concrete adoption numbers. Four silences, all in MWS's favor.

**Importance: 2/5 — rationale:** Real, MIT-licensed, runnable tool + a genuinely niche-useful Russian telephone-ASR benchmark, and MWS AI's first speech open-source move — but with zero independent validation, near-zero adoption (~6 stars / ~837 downloads), and an overstated nationalist PR frame. The defining tell: MWS built a call-center ASR benchmark and left its own call-center ASR model out of the results. A credibility/standard-setting play, not yet an adopted standard. Low near-term fintech/market weight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian ASR/speech-tech is a subvertical of the domestic AI-infra stack, structurally driven by import-substitution: Western ASR (Google, Nvidia, OpenAI) is either sanction-constrained or runs off-shore, so Russian contact-centres, telecoms and the public sector need locally-hosted, closed-loop models and on-prem deployability — exactly the "within Russian jurisdiction, inference stays in-country" logic MWS itself stressed for GLM-5.2 ([[MWS Cloud deploys GLM-5.2 on its own infrastructure]], 2026-07-17, via kommersant.ru). No defensible TAM figure surfaced — market-sizing claims are paywalled/absent → no data. Secular driver + "why now": contact-centre/voicebot automation is the volume use-case (per ai-sage GigaAM-v3 trained on 700k hrs incl. call-centre audio), and the Russian outsourced contact-centre market itself *stalled* in 2025 ([[Forbes Russian outsourced contact-center market stalled in 2025]]) — so growth has to come from automation/AI densification, not seat growth. That is the pull RESON is positioned into: cheaper/faster model-selection for ASR buyers.

**Competitive landscape.** Sector KPIs: WER (Word Error Rate) is the headline metric; CER, and domain-robustness (noise, numerics, named entities/англицизмы) the secondary ones. Basis of competition is model *accuracy on Russian* + on-prem/closed-contour deployability + price. Key ASR players: Sber (GigaAM / SaluteSpeech), Yandex (SpeechKit), Alpha Cephei (Vosk, open), plus foreign open models (Nvidia Parakeet/Nemotron, OpenAI Whisper). Per MWS's own RESON ASR OSD benchmark, Sber's GigaAM v3 won on avg WER 7.42%, Vosk 11.07%, Nvidia Parakeet 15.83%, Nvidia Nemotron 25.52% (via cnews.ru, 2026-10-06). Protagonist's position: MWS AI is here an *evaluation-tool/benchmark* vendor, NOT (in this release) a competing ASR-model vendor — a tooling/standards play adjacent to the model race. Moat `(analysis)`: thin and open by design — RESON is an open Python library + public HF dataset (huggingface.co/datasets/MTSAIR/mws-reson-asr-osd); the strategy is category-shaping ("common approach to evaluating ASR on Russian data", per team lead A. Shevchenko) and lead-gen into the MWS AI Agents Platform / MWS GPT Model Hub, not a licensable product.

**Comps & multiples.** No valuation, round or revenue attaches to this specific release → EV/Revenue, P/S, price-per-user all = no data; multiples not computed. For scale of the parent segment (PRIMARY, IR + press): MTS Web Services external revenue grew 46% YoY in Q1 2026 with MWS AI revenue up ~2.2x YoY and MWS Cloud +44% (via tbank.ru social citing the Q1-2026 release; MTS Q1 2026 Press Release, https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf, dated 2026-05-20 per ir_latest.json), and MWS Q2 2026 external revenue +18% QoQ-basis (akm.ru). Adjacent monetised segment: MTS AdTech FY2025 revenue +27.4% to RUB 70bn (tadviser.com). Internal comps (base precedents of MWS AI go-to-market): [[MWS Cloud deploys GLM-5.2 on its own infrastructure]] (open catalogue / Model Hub), [[Russian State Library automates processes with MWS AI platform]] (AI Agents Platform enterprise land-and-expand), [[MTS Link adds Chinese speech recognition and 19-language subtitles]] (same-group speech-tech, product side), [[MTS bundles enterprise solutions under MTS CorpTech brand]] (B2B packaging). No comparable multiple exists in-base → qualitative comparison only.

**Risk flags.**
1. Benchmark self-interest / credibility: MWS AI publishes the eval tool AND the dataset AND runs the comparison — and its own ASR model does not appear among the ranked results, while a *rival* (Sber GigaAM) tops the table. Either MWS has no competitive ASR model to show (ceding the actual product layer to Sber/Yandex), or it withheld it; either reading undercuts the "neutral standard" framing. Second-order: a vendor-controlled benchmark is only an industry standard if peers adopt it — adoption, not the release, is the real test.
2. Monetisation gap / value capture by another layer: an open, free tool + open dataset generates no direct revenue; value accrues only if it funnels into paid MWS AI/Cloud platform spend. The margin/economics of that funnel are undisclosed → `[UNSOURCED]`. Classic "give away the ruler, sell the model-hosting" bet that may never convert.
3. Protagonist not winning the metric that matters: on MWS's own WER table the Russian ASR leader is Sber, not MTS. In a telecom-adjacent, contact-centre-driven market where the stalled outsourcing market forces automation, being the measurer rather than the best model is a weak position if buyers pick on WER.

**What this changes (idea-lens).** `(analysis)` This is a standards/distribution move, not a re-rating event — MWS is trying to own the *evaluation layer* of Russian ASR to pull enterprise buyers toward its platform while Sber owns the accuracy crown. Falsifiable thesis: RESON becomes relevant only if third-party Russian ASR buyers/vendors actually cite MWS RESON ASR OSD as the reference benchmark within ~6–12 months; what breaks it — Sber/Yandex ship or endorse their own competing Russian ASR benchmarks, fragmenting the "standard" and leaving RESON as internal MWS tooling with a PR wrapper. Watch: whether MWS AI subsequently fields a first-party ASR model to enter the ranking it created.

Sources: https://www.cnews.ru/news/line/2026-10-06_mws_ai_otkryla_svoj_instrument · https://huggingface.co/datasets/MTSAIR/mws-reson-asr-osd · https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf · https://www.akm.ru/eng/news/mts-web-services-external-revenue-increased-by-18-in-the-second-quarter/ · https://tadviser.com/index.php/Company:MTS_AdTech,_MTS_Ads_(MTS_Advertising_Technologies) · https://github.com/salute-developers/GigaAM
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Issuer-scale context (not an earnings event). RESON is a free/open-source ASR-evaluation tool from MWS AI (part of MTS Web Services), a product launch with no financials of its own. Below: the latest reported results of the parent issuer, PJSC MTS (MOEX: MTSS), framed as the scale and trajectory behind the MWS AI business unit. Figures from the MTS Q1 2026 press release (published 2026-05-22); semantic IR search was unavailable (OpenRouter 402), so figures are read directly from the filing.

**Verdict (issuer context, not a reaction to this news).** IN-LINE / solid top-line beat on momentum — MTS Group Q1 2026 revenue 201.3bn RUB (+14.7% YoY) · OIBDA 74.7bn RUB (+18.0% YoY, margin ~37.1% vs ~36.1% a year ago) · net profit 7.2bn RUB (+46.4% YoY). Double-digit growth led by Telecom, Fintech and "Funtech"; dividend of 35.0 RUB/share recommended. **But the unit that built RESON — MWS — is the one soft spot: MWS revenue fell 5.1% YoY to 14.0bn RUB**, even as its external (third-party) revenue grew ~46%.

**Key figures (Group, Q1 2026 vs Q1 2025, RUB bn).**
- Revenue: 201.3 vs 175.5 — **+14.7%** YoY.
- OIBDA: 74.7 vs 63.3 — **+18.0%** YoY (OIBDA growing faster than revenue → ~1pp margin expansion to ~37.1%).
- Operating profit: 41.0 vs 31.9 — **+28.7%** YoY.
- Net profit (attributable to shareholders): 7.2 vs 4.9 — **+46.4%** YoY; management frames the recovery as the hard-money-policy period being overcome.
- Capex: 44.3 vs 34.3 — **+29.1%** YoY (heavier investment in the quarter; 5G prep on domestic tech).
- Net debt: 451.5 vs 456.4 — **-1.1%** YoY; Net debt / LTM OIBDA 1.6x (down 0.2x YoY) — third straight quarter at the lowest level since 2021.
- Dividend recommended: 35.0 RUB/share (~69.9bn RUB total), record date proposed 2026-07-09.

**By segment / driver (Q1 2026 revenue, RUB bn; YoY).**
- Telecom: 130.3 (**+14.7%**) — B2C mobile+fixed +10.3%, B2B/G base & digital +15.8%, interoperator (B2O) +33.7% (the fastest line).
- Fintech: 42.0 (**+18.4%**) — driven by the high key rate and securities-portfolio income; bank net profit 2.5bn RUB (x2.6 YoY); retail loan book 325.7bn RUB.
- AdTech (MTS Ad): 15.3 (**+2.3%**) — advertising tech itself -10.7% to 5.2, marketing tech +10.7% to 10.1.
- Retail & equipment sales: 12.0 (**+11.9%**).
- Media holding: 7.0 (**+3.8%**) — OTT users 10.9m (+9.1%), pay-TV 16.3m (+9.8%).
- **MWS (MTS Web Services — the cloud/AI arm that houses MWS AI, maker of RESON): 14.0 (-5.1%)** — the only reported segment in decline. The issuer calls out that **external MWS revenue rose ~46%**, i.e. the drop is on the internal/intra-group book; the external pivot is the growth story but it is small-base and not yet enough to offset.

**vs expectations / prior period.** No pre-earnings preview or public consensus retrieved (semsearch down; no free RU-telecom consensus pulled). Beat/miss stated qualitatively vs prior year only: Group revenue and OIBDA both accelerated into mid/high-teens with margin expansion and a sharp net-profit rebound (+46.4%) — a clean YoY beat on the parent. No prior MTS earnings note exists in the corpus to wikilink. Any street estimate: [UNSOURCED].

**Guidance / forward.** No explicit numeric FY2026 guidance in the Q1 press release (standard for MTS quarterly releases). Forward signals given instead: continued deleveraging (ND/OIBDA held at ~1.6x), sustained dividend policy (35.0 RUB/share), elevated capex for domestic-tech 5G prep, and a strategic China Mobile partnership (AI-driven autonomous network infrastructure + joint B2B solutions) announced in March 2026. Management tone: confident on Telecom/Fintech/Funtech; conspicuously no segment profitability or standalone guidance for MWS despite flagging the -5.1% — they emphasize the +46% external line and stay silent on MWS margins/path to scale.

**Thesis-flags for this product (why-ladder).**
1. **RESON / MWS AI sit inside a sub-scale, shrinking reported segment.** Fact: MWS revenue 14.0bn RUB (-5.1% YoY), ~7% of Group revenue and the only line down. Why: the growth is external (+46%) but off a small base. Why it matters: an open-source ASR tool is a go-to-market / credibility play (seed the RU ASR ecosystem, win external cloud/AI customers) rather than a near-term revenue driver. Second-order: RESON's open benchmark — where Sber's GigaAM v3 (WER 7.42%) beat MWS-tested Nvidia/OpenAI models — is a bid to position MWS AI as the neutral arbiter of RU ASR while it fights Sber/Yandex for external cloud share.
2. **Issuer has the balance sheet to subsidize the AI land-grab.** Fact: ND/OIBDA 1.6x (record-low since 2021), OIBDA +18.0%, capex +29.1%. Why it matters: MTS can fund loss-leading open-source/AI bets out of Telecom+Fintech cash flow; RESON's "free library" model is affordable at Group scale even while MWS itself declines.
3. **Watch the MWS external line, not the headline Group number.** The relevant KPI for whether products like RESON convert is MWS external revenue (+46% in Q1 2026), which is small-base and not yet disclosed in absolute RUB — [UNSOURCED] for the exact external figure. If it keeps compounding, MWS flips from drag to driver; if not, RESON remains a marketing asset.

Sources: MTS Q1 2026 Financial & Operating Results press release (PJSC MTS, published 2026-05-22) — https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf (latest MTS report in ir_latest.json; ~5 months old as of 2026-10-12 — slightly outside the <~3-month freshness window but the most recent available; Q2 2026 not yet in the IR index). Semantic IR search unavailable (OpenRouter 402). Public consensus / street estimates: not retrieved — [UNSOURCED]. MWS external revenue absolute RUB: not disclosed in release — [UNSOURCED].
<!-- /enrichment:earnings_review -->
