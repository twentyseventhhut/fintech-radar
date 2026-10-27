---
title: "Yandex and ShAD students build MTGBench reasoning benchmark"
date: 2026-10-27
retrieved: 2026-10-27
tags:
  - company/yandex
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.forbes.ru/tekhnologii/571040-kontrol-nyj-organ-v-andekse-pridumali-testy-dla-ocenki-rassuzdenij-nejrosetej
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: s59027853
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Yandex and ShAD students build MTGBench reasoning benchmark

> [!info] 2026-10-27 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Forbes: Исследователи Яндекса и студенты ШАД разработали MTGBench – набор тестов для оценки способности нейросетей рассуждать

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.forbes.ru/tekhnologii/571040-kontrol-nyj-organ-v-andekse-pridumali-testy-dla-ocenki-rassuzdenij-nejrosetej>

## Контекст

<!-- enrichment:context -->
### [0] What happened
On 2026-10-27, Yandex engineers together with students of the Yandex School of Data Analysis (ShAD / ШАД) released **MTGBench** — an open-source benchmark for evaluating the *reasoning* ability of large language models. Despite the MTG abbreviation (and the convenient "Magic: The Gathering" framing), MTG here stands for **"Multi-Turn Game"** — a research paper describing it was accepted to **Findings of EMNLP 2026** (Budapest). Source note is a Forbes.ru item relayed via the "42 секунды" channel; primary company source is Yandex IR.

### [1] What it is / what it measures
MTGBench is a suite of **seven text-based, multi-turn games**: Wordle, Word Chain, Situation Puzzles, 20 Questions, Wheel of Fortune, 20 Features, and Alias. The games span several reasoning modes — deductive logic, using newly revealed information, multi-step planning, consistency with prior answers, lateral/clue interpretation, and knowledge retrieval. It scores not only task success but, where meaningful, **how many turns/steps** a model needs to reach the solution. Four games are checked algorithmically; the other three rely on an **LLM-as-judge** whose accuracy was validated against human annotators. All seven games ship in **both English and Russian**, with tasks generated separately per language (a bilingual angle relatively rare in Western reasoning benchmarks).

### [2] Key findings reported
The team ran **16 models**, from smaller Qwen variants up to larger Gemini and GPT models. Headline result: the *benefit of explicit step-by-step reasoning is task-dependent* — it helps most on letter/symbol games, clue interpretation, and option-elimination, but is inconsistent on knowledge-retrieval and semantic tasks, varying by model. This is a methodological finding (reasoning is not a monotonic good) rather than a product/revenue event.

### [3] Why it matters / connection to Yandex
Fits Yandex's broader 2026 AI research push — cf. [[TASS Yandex research aids Anthropic on AI self-propagation]] (Yandex work cited by Anthropic) and [[Yandex open-sources YTsaurus Flow real-time stream processing]] (open-sourcing posture). ShAD is Yandex's long-standing ML talent pipeline; an open benchmark is cheap reputational/recruiting capital and a positioning move against saturated Western benchmarks (SWE-bench style saturation discussed in [[This Week in Fintech Anthropic long-read on how AI trains AI]]). Fintech relevance is indirect: tooling for choosing reasoning models, not a financial product.

### [4] Comparables / landscape
Crowded field of game-based LLM reasoning benchmarks: TMGBench (strategic games), DSGBench (strategic agents), GameArena (live games), TurnBench-MS (multi-turn multi-step). MTGBench's differentiators are the puzzle-game mix, the step-count metric, and explicit EN/RU bilinguality. Contrast with capability-model releases like [[Ant Group releases Ling-1T AI model]] (a model claiming reasoning superiority) — MTGBench is the *measuring stick*, not the model.

Sources:
- Forbes.ru (note source): https://www.forbes.ru/tekhnologii/571040-kontrol-nyj-organ-v-andekse-pridumali-testy-dla-ocenki-rassuzdenij-nejrosetej
- Yandex IR press release (2026-10-27): https://ir.yandex/press-releases?year=2026&id=2026-10-27
- MTGBench, Findings of EMNLP 2026 (ACL Anthology): https://aclanthology.org/2026.findings-emnlp.1333/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
1. **Acronym trap.** The note title and upstream framing flirt with "Magic: The Gathering," but the EMNLP paper defines MTG as **"Multi-Turn Game."** Does any downstream digest copy still carry the MTG=Magic reading? (A separate arXiv paper on *Causal RL for Magic: The Gathering* exists and is a genuine confound.)
2. Is "ShAD students" accurate, or were students a minor contributor to a Yandex-led effort? The IR headline credits "Yandex and School of Data Analysis."
3. Is this genuinely *new* on 2026-10-27, or a re-announcement of an EMNLP paper accepted earlier in 2026? (Conference acceptance can predate the open-source/PR release by months.)
4. Open-source to what degree — code, data generators, leaderboard, and license? "Open-source" in a PR can mean data only.
5. The three LLM-judge games: how was judge accuracy "validated by human annotators" — agreement rate, sample size? LLM-as-judge is a known weak point.
6. 16 models tested — were Yandex's own models (Alice/YandexGPT) included, and did they look favorable? Benchmark-author conflict-of-interest risk.
7. Russian-language tasks "generated separately" — generated by what? If by an LLM, contamination/quality risk for the RU split.
8. Is the "reasoning helps on symbol games, not on knowledge tasks" finding novel, or a restatement of known chain-of-thought literature?
9. Any fintech angle at all, or is this pure AI-research PR with zero payments/banking relevance? (Leaning: zero direct fintech relevance.)
10. Could this be sanctions/geopolitics-colored — a Russian benchmark whose adoption outside RU is limited regardless of merit?
11. Benchmark saturation / gameability: text games like Wordle have known optimal strategies; can a model hard-code rather than "reason"? Contamination from training data?
12. Does the single-source (Forbes via one Telegram channel, 1 mention) justify any prominence, or is this a minor research note?
13. Is "MTGBench" a unique name, or does it collide with other benchmarks (naming overlap with TMGBench/DSGBench etc.)?

Importance: **2/5** — Legitimate, verifiable AI-research release (EMNLP 2026 paper + Yandex IR) with a mild newsworthiness hook (bilingual, step-count metric). But it is academic/reputational, single-sourced (1 mention), and has no direct fintech/payments/revenue relevance; it mainly reinforces Yandex's open-AI-research posture. Not digest-prominent on its own.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector context — LLM reasoning benchmarks.** MTGBench slots into a crowded, fast-saturating evaluation layer. By early 2026 nearly half of the ~60 most-cited LLM benchmarks are considered saturated: frontier models top ~93% on MMLU, ~99% on GSM8K, and GPQA Diamond is approaching the ceiling, forcing evaluators toward fresh, contamination-resistant tasks (e.g. annually-refreshed AIME 2026). Yandex's design choice — 7 multi-turn text games (Wordle, Word Chain, Situation Puzzles, 20 Questions, Wheel of Fortune, 20 Features, Alias) with 4 algorithmically-checked and 3 LLM-judged, human-validated — is a deliberate bet on dynamic, procedurally-generated, multi-turn reasoning that resists the memorization that has hollowed out static Q&A benchmarks. The paper was accepted to Findings of EMNLP 2026, which gives it academic credibility distinct from vendor-marketing leaderboards. Sources: [Yandex IR press release 2026-10-27](https://ir.yandex/press-releases?year=2026&id=2026-10-27); [MTGBench, ACL Anthology / Findings EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.1333/); [LLM benchmark landscape 2026 — saturation & contamination](https://www.digitalapplied.com/blog/llm-benchmark-methodology-2026-contamination-leaderboard-guide).

**Positioning vs global labs.** The reported test set spans 16 models from small Qwen variants to larger Gemini and GPT families — i.e. Yandex is positioning MTGBench as a neutral third-party yardstick for *other* labs' models, not a vehicle to showcase its own YandexGPT/YaLM line (none featured prominently in the write-up). This mirrors a broader pattern of national/regional AI players (Alibaba's Ant with Ling-1T, Chinese open-weight releases) competing on open, citable research artifacts rather than only closed model scores. Benchmark-release is a low-capex way to earn mindshare and recruiting signal (the ShAD student co-authorship is itself a talent-pipeline play) relative to the far costlier race on frontier model training.

**In-base comps (news DB).** No direct benchmark-release comp exists in the vault; nearest adjacents are AI-model/research items rather than evaluation tooling: [[News/2025-10/Ant Group releases Ling-1T AI model]] (large-model release by a fintech-adjacent tech giant), [[News/2026-05/Nof1 raises $15 million for financial market AI models]] (domain-specific model funding), and Yandex's own operational-AI deployments such as [[News/2026-10/Yandex Lavka expands robotic delivery to 130 dark stores]] and [[News/2026-10/Sber adds BPMN generation to Giga Agentic RPA platform]] (RU-tech applied-AI). The absence of close comps underlines this is a research/eval-layer story, not a product or capital event.

**IR backdrop (real figures — Yandex scale & AI-investment capacity).** Yandex is a large, profitable platform, not an AI-research pure-play: Q3 2025 revenue was RUB 366.1bn, +32% YoY, with adjusted EBITDA RUB 78.1bn (21.3% margin, +1.5pp YoY); Search & portal remains the largest segment (~33% of total revenue, +30% in 2024) and Yandex updated its segment structure in Q3 2025. This scale and cash generation is what funds discretionary AI research like MTGBench; the benchmark itself is financially immaterial but is a credibility/recruiting asset for a company whose advertising and search franchise is explicitly AI-driven. Sources: [Yandex Q3 2025 press release (ENG)](https://yastatic.net/s3/ir-docs/docs/2025/q3/25b90c11d0060d861ec0957dbbb96eeb/3Q25_YDEX_Press_Release_ENG_short_25b9.pdf) · [drive](https://drive.google.com/file/d/1p3HWYet_XGjj9NQPqmp0mwWKprwPtg-k/view); [Yandex AR2024](https://yastatic.net/s3/ir-docs/prospectus/reports/2024/ENG_YANDEX_AR2024.pdf) · [drive](https://drive.google.com/file/d/1YNiBUYsHBo0y7LxPwNpGsMxJDmdkH3ud/view).

**Risk flags.**
1. **No commercial revenue** — MTGBench is open-source and non-monetized; impact on Yandex financials is zero. Its value is reputational/recruiting, which is hard to measure and easy to overstate.
2. **Benchmark adoption risk / crowded field** — multiple near-identically-named game/multi-turn reasoning benchmarks already exist (TMGBench, TTT-Bench, MTR-Bench). MTGBench must win community adoption to matter; most academic benchmarks see little uptake beyond their own paper.
3. **LLM-judge reliability** — 3 of 7 games depend on an AI judge; despite human-validation claims, LLM-as-judge introduces its own bias/non-determinism, a known weakness that can undercut the benchmark's credibility as it ages.
4. **Saturation/short shelf-life** — like all static benchmarks, procedurally-generated games can still be gamed or contaminated once the method is public; usefulness decays as models are tuned against it.
5. **Geopolitical/access constraint** — a Russia-headquartered lab's benchmark may face limited integration into Western leaderboards and model-eval pipelines regardless of technical merit, capping its reach as a global standard.
6. **Source thinness** — the vault note rests on a single secondary Forbes mention with no primary text loaded; methodology/scoring details here derive from the vendor press release and the EMNLP paper, not independent replication.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Backdrop context — not an earnings event.** This story (Yandex/ShAD's MTGBench LLM-reasoning benchmark) is a research/product item, not a financial release. The figures below frame Yandex's overall scale and the size of the "Search and AI services" engine funding this AI work. Latest reported period: **Q4 2025 & FY2025** (announced Feb 17, 2026; all figures IFRS/non-IFRS as reported, RUB).

**FY2025 headline (vs FY2024):**
- Revenue **RUB 1,441.1bn, +32% YoY** (FY2024: 1,094.6bn).
- Adjusted EBITDA **RUB 280.8bn, +49% YoY**, margin **19.5%** (+2.3 p.p.).
- Adjusted Net Income **RUB 141.4bn, +40% YoY**.

**Q4 2025 (vs Q4 2024):**
- Revenue **RUB 436.0bn, +28% YoY** (Q4 2024: 340.1bn).
- Adjusted EBITDA **RUB 87.8bn, +80% YoY**, margin **20.1%** (+5.8 p.p.).
- Adjusted Net Income **RUB 53.5bn, +70% YoY**.

**"Search and AI services" segment (the unit behind this benchmark work):**
- FY2025 revenue **RUB 551.2bn, +10% YoY** (FY2024: 499.8bn); segment adj. EBITDA **RUB 245.5bn, +12%**, margin **44.5%** — the group's profit engine funding AI R&D.
- Q4 2025 revenue **RUB 163.0bn, +4% YoY**; adj. EBITDA **RUB 69.2bn (flat)**, margin **42.5%** (−1.6 p.p.).
- FY2025 advertising revenue **RUB 449.1bn, +13.5%**; subscription revenue **RUB 89.8bn, +44.9%**.

**AI investment signal:** the press release does not quote a standalone AI capex/R&D number. Yandex flags AI integration into Search and Alisa AI (Q1 2026 RUS release notes **1,600+ API applications** from retailers/brands for transactional scenarios inside AI interfaces) — directional only, not a FY2025 AI spend figure.

**Guidance (2026):** revenue growth **~20% YoY** and adjusted EBITDA **~RUB 350bn**. Management to recommend **RUB 110/share** dividend for 2025 (+37.5% vs prior).

**Thesis flags:** group growth strong and broadening (City Services FY adj. EBITDA RUB 62.8bn vs 17.6bn; B2B Tech +48% revenue), but the Search & AI services segment itself is maturing — single-digit Q4 revenue growth (+4%) and flat segment EBITDA with a slight margin dip (42.5%), consistent with heavier AI investment weighing on the core cash cow even as it stays the main profit driver. 2026 guidance implies deceleration (~20% vs 32% in 2025).

**Verdict: in-line** — FY2025 revenue +32% matched the ">30%" 2025 outlook and FY adj. EBITDA RUB 280.8bn beat the "at least RUB 250bn" target. (This is backdrop, not a reaction to the MTGBench story.)

Source: Yandex Q4 2025 & FY2025 results, Feb 17, 2026 (ENG press release). drive_url: https://drive.google.com/file/d/1tL34dVaR0rJUa_1IB4AhYuJUGBGHXHS8/view · url: https://yastatic.net/s3/ir-docs/docs/2025/q4/fc756ee95baa6fa171ee77ac733d52be/4Q25_YDEX_Press_Release_ENG_short_6ee9.pdf
<!-- /enrichment:earnings_review -->
