---
title: "FT: More firms pick Chinese AI models to cut costs"
date: 2026-07-13
retrieved: 2026-07-13
tags:
  - industry/ai
  - region/global
  - type/commentary
sources:
  - https://www.ft.com/content/9c8ff45b-7c20-4c2e-93c9-c52339ffdcee
status: published
n_mentions: 1
channels:
  - "42 секунды"
story_id: s0c4751be
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# FT: More firms pick Chinese AI models to cut costs

> [!info] 2026-07-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] FT: Все больше компаний выбирают китайские модели, чтобы сократить расходы на ИИ

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.ft.com/content/9c8ff45b-7c20-4c2e-93c9-c52339ffdcee>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: FT — More firms pick Chinese AI models to cut costs
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS: FRESH — but incremental.** This is an FT trend/commentary piece (2026-07-13). The corpus already covers the *supply side* of the Chinese open-weight surge — the model releases and the geopolitics: [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]], [[Asian AI startups launch Mythos-like models amid Anthropic export ban]], [[DeepSeek raises over $7 billion in debut funding round]], [[OpenAI, Google models reach Chinese firms via Singapore units]]. What is *new* here is the **demand-side** framing: named Western enterprises (DoorDash, Airbnb, Siemens) switching production workloads to Chinese models to cut inference bills. No prior note documents that adoption angle, so not a duplicate. But the underlying "Chinese models are cheap and good enough" narrative is the ~5-month-old post-DeepSeek-R1 story, so weight is moderate, not high.

## [0] What exactly happened (de-PR'd)
The FT reports a *behavioral* shift: a growing set of Western/global firms route inference to Chinese open-weight models (DeepSeek, Alibaba **Qwen**, Moonshot **Kimi**, Zhipu/**GLM**) to cut costs, not to US frontier labs. De-PR'd core:
- **Named adopters (via FT + citing coverage):** DoorDash (cofounder Andy Fang: uses Moonshot/Kimi for "lower-level work" to save money); Airbnb (Qwen + Kimi in AI infra); Siemens; SF startup Lindy (switched Anthropic → DeepSeek V4, founder says it "saved millions"). Note the hedge in Fang's own words — **"lower-level work,"** not customer-facing frontier tasks.
- **The cost gap is real and structural, not a promo:** headline figure across coverage is **"60–90% cheaper"** than leading Anthropic/OpenAI models (CSET/Georgetown). At list, the gap is far wider — DeepSeek V4 Flash ≈ **$0.09/$0.18 per 1M tokens** in/out vs GPT-5.5 ≈ **$5/$30** (~100x on output). It rests on sparse-MoE (activating ~2% of params/token), smaller KV caches, cheaper GPU-hours — i.e. an architectural cost advantage, not only a subsidy war (though DeepSeek did run a 75% promo → "permanent" 75% cut in June 2026).
- **Why framed this way / what it reveals:** the FT anchors the story to a **cost/CFO** lens, which is the strongest version of the argument — the geopolitics (bans, distillation) is a headwind the piece treats as secondary to the economics. → The load-bearing question the framing *skips*: token share ≠ dollar share. Chinese models being ~100x cheaper means high usage share is exactly what you'd see even at trivial spend — so "everyone is switching" can be true in tokens and near-meaningless in revenue displacement (see [3]).

## [1] Competitors / peers
- **The Chinese open-weight cohort (supply side, already in corpus):** GLM-5.2 (1M-token context, topped open-weight leaderboards once Fable excluded — [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]); DeepSeek V4 (well-funded, $7B round — [[DeepSeek raises over $7 billion in debut funding round]], [[DeepSeek to double headcount as it races AGI labs]]); Sakana Fugu / 360 Tulongfeng ([[Asian AI startups launch Mythos-like models amid Anthropic export ban]]). Benchmark parity is genuine on **coding/math/agentic** tasks (DeepSeek V4 Pro ~83.7% SWE-bench Verified vs Claude Opus 4.7 ~87.6%; Kimi K2 Thinking strong AIME/GPQA at $0.60/M) but US frontier still leads the very top of leaderboards. "Generally workable for a lot of workloads" ≠ frontier parity.
- **US frontier response (the peer reaction):** OpenAI released open-weight **gpt-oss** (2025, Altman: "on the wrong side of history"); Google ships Gemma + cheap **Gemini Flash** ($0.50/$3.00); OpenAI has been cutting cost aggressively — corpus: [[OpenAI cuts guest ChatGPT inference costs over 50%]] (software efficiency), [[Anthropic launches cheaper Claude Sonnet 5 for agents]] (price tiering for exactly this pressure). **Anthropic ships no open weights** — a genuine strategic gap the FT can legitimately highlight.
- **Why the landscape is this way (2nd order):** the US export/distillation posture is *pushing* demand toward Chinese substitutes. When Commerce forced Anthropic to suspend global Claude Fable/Mythos access, GLM-5.2 stepped straight into the gap ([[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]); Asian labs advertise "frontier capability without export-control risk" ([[Asian AI startups launch Mythos-like models amid Anthropic export ban]]). → US policy is simultaneously trying to *contain* Chinese AI and *handing it the enterprise market* — the same contradiction flagged in [[OpenAI, Google models reach Chinese firms via Singapore units]].

## [2] Company history / fit (the buyers' logic)
- Not a single company but a *pattern* the corpus already documents from the buy-side: [[Base44 launches own AI model to seek defensibility]] captured the exact enterprise complaint — CFOs "don't see ROI using the latest models for all use cases," so an "orchestration/optimization" layer selects the cheapest adequate model per task. Chinese open-weight models are the extreme low-cost end of that routing menu.
- **Why firms act this way:** inference is now the dominant AI cost line (Deloitte: ~2/3 of AI compute in 2026). At scale, a ~90% per-token saving on the 80–90% of tasks that don't need frontier quality is a direct margin lever. Self-hosting open weights (on the firm's own/US-cloud GPUs) also neutralizes much of the data-residency objection — which is precisely why bans are hard to enforce against *open-weight* (vs API/app) use.

## [3] Novelty / value-add / traction — the skeptic's core
- **Novelty of the piece: modest.** The "Chinese models are cheap and competitive" thesis is the post-DeepSeek-R1 story (Jan–Feb 2026). The incremental value is the **named-enterprise demand evidence** — moving the story from "models exist" to "Western firms deploy them in production."
- **Traction reality check — this is the whole game:** the hard data hook is usage share. **OpenRouter: Chinese-origin models ≈ 46.4% of routed tokens vs 35.7% US-origin (June 2026)**, up from ~4.5% in H1-2025. BUT the load-bearing counter-fact: **on Vercel, DeepSeek went from <1% to ~17% of tokens while revenue stayed near ~1%** — because Chinese models are ~100x cheaper, token share massively overstates commercial displacement of US labs. OpenRouter/Vercel are also developer/hobbyist-skewed, not Fortune-500 production spend. → **The central question is not "are Chinese models winning share?" (yes, in tokens) but "are they capturing dollars / displacing US-lab revenue?" (barely, so far).** A commentary piece adds value only if it foregrounds that gap.
- **Who captures the margin:** if the trend deepens, the winner is the *enterprise buyer* (lower COGS) and the model-routing/orchestration layer — not necessarily the Chinese labs (thin monetization) nor US labs (share erosion at the cheap tier). Value migrates to whoever owns the routing decision.

## [4] What's next / market sentiment
- **US price/open-weight response accelerates** (gpt-oss, Gemini Flash, Sonnet 5, OpenAI's >50% inference-cost cut) — the price gap is closing from above even as it stays wide at list. A commentary piece that assumes static US pricing is already dated.
- **Regulatory tail risk is the real downside trigger:** NDAA FY2026 directs DoD/DNI to exclude DeepSeek-developed AI; a pending bill would bar all federal agencies from Chinese/Russian/Iranian/NK models; House committees sent compliance letters to **Airbnb and Cursor** over Chinese-AI exposure (April 2026). → For a CFO, the "savings" must be netted against compliance/legal review and rip-and-replace risk. Censorship baked into outputs "pursuant to Chinese law" persists even when self-hosted — an integrity risk for regulated/financial use.
- **Counterintuitive 2nd-order effect:** aggressive US export controls are the *strongest driver* of Chinese enterprise-model adoption, not a brake — every ban (Claude Fable/Mythos) vacates a slot GLM/DeepSeek fills, and cheap open weights make the substitution sticky. The policy meant to preserve US AI dominance is helping commoditize the very layer US labs monetize.

## Sources
- FT (paywalled): https://www.ft.com/content/9c8ff45b-7c20-4c2e-93c9-c52339ffdcee
- Reconstructed via secondary coverage citing the FT: CSET/Georgetown https://cset.georgetown.edu/article/companies-turn-to-chinese-ai-models-to-cut-costs/ · Rest of World https://restofworld.org/2026/when-americans-choose-chinese-ai/ · Futurism https://futurism.com/artificial-intelligence/us-realizing-chinese-ai-models-way-cheaper
- Usage share (token vs revenue): OpenRouter DeepSeek V4 adoption https://openrouter.ai/blog/insights/deepseek-v4-adoption/ · Yahoo/Finance https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html
- Pricing/benchmarks: https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard
- Regulatory: NDAA/DeepSeek exclusion https://www.techtimes.com/articles/320171/20260711/washington-wants-chinese-ai-out-corporate-america-open-weights-block-ban.htm · federal-ban bill https://cybernews.com/security/us-lawmakers-bill-bans-chinese-ai-models-across-federal-agencies/ · lawmaker probe https://www.cnbc.com/2026/07/08/chinese-ai-models-probe-us-lawmakers.html
- Internal: [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]], [[Asian AI startups launch Mythos-like models amid Anthropic export ban]], [[DeepSeek raises over $7 billion in debut funding round]], [[OpenAI, Google models reach Chinese firms via Singapore units]], [[Base44 launches own AI model to seek defensibility]], [[OpenAI cuts guest ChatGPT inference costs over 50%]], [[Anthropic launches cheaper Claude Sonnet 5 for agents]], [[DeepSeek to double headcount as it races AGI labs]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Token share vs dollar share — the decisive question.** OpenRouter shows Chinese models at ~46% of *tokens* (June 2026), but on Vercel DeepSeek hit ~17% of tokens while revenue stayed ~1%. Since Chinese models are ~100x cheaper, high token share is expected even at trivial spend. Does the FT distinguish usage from revenue displacement, or launder token share as "US labs losing the market"? — **This separates insight from hype.**

2. **Are the data sources representative of enterprise?** OpenRouter/Vercel are developer/hobbyist-skewed routers. What share of *Fortune-500 production* AI spend runs Chinese models? No enterprise-spend survey confirms the "firms are switching" headline at scale. — Open.

3. **Production vs pilot vs "lower-level work."** DoorDash's Fang explicitly says Kimi is for "lower-level work." Of DoorDash/Airbnb/Siemens, which run Chinese models in *customer-facing production* vs internal low-stakes tasks? — Mostly the latter, on the evidence.

4. **Self-hosted vs Chinese-hosted API.** Self-hosting open weights keeps data in-network and defeats the exfiltration objection; calling Chinese-hosted APIs does not. How much adoption is which? The distinction changes the entire risk story. — Open in the piece.

5. **Is this news, or a 5-month-old recap?** The "Chinese models cheap and good enough" thesis is the post-DeepSeek-R1 (Jan–Feb 2026) story. Does the FT add the named-enterprise demand evidence (new) or just restate the trend? — Adds the demand angle; otherwise incremental.

6. **Benchmark parity vs frontier parity.** "Generally workable" is doing heavy lifting. Chinese models match US frontier on coding/math/agentic benchmarks (DeepSeek V4 Pro ~83.7% SWE-bench vs Claude ~87.6%) but trail at the top and on long-horizon agentic reliability/safety/multimodal. — Parity is task-specific, not general.

7. **Promo pricing vs structural cost.** DeepSeek −75%, Alibaba Qwen-Long −97%, ByteDance −63% — is the arbitrage a subsidized land-grab that reverses once share is won, or structural (sparse-MoE, cheap GPU-hours)? — Both; the architecture is genuine but list prices are promo-inflated downward.

8. **Regulatory tail risk vs "savings."** NDAA FY2026 excludes DeepSeek from DoD; a bill would bar federal agencies; House probed Airbnb/Cursor. Net of compliance, legal review, and forced rip-and-replace risk, is the CFO saving real? — For regulated buyers, materially discounted.

9. **Hidden total cost of ownership.** Do the "saved millions" claims net out self-hosting GPU capex/opex, fine-tuning, eval overhead, and dual-vendor routing complexity — or only compare sticker per-token prices? — Likely sticker-only.

10. **Selection/anecdote bias.** DoorDash/Airbnb/Siemens/Lindy — curated handful or a denominator? What fraction tried Chinese models and *reverted* to US frontier? — No denominator given.

11. **Censorship/output integrity.** Self-hosting fixes data residency but not model-baked censorship/bias "pursuant to Chinese law." Does the piece address output-integrity risk for financial/regulated use? — Usually unaddressed.

12. **Geographic scope.** "More firms" — how much of the 46% token share is US enterprises vs Asia/RoW developers where Chinese models are the default? RoW adoption ≠ the US-enterprise thesis. — Likely conflated.

13. **US counter-move already underway.** gpt-oss, Gemini Flash, cheaper Sonnet 5 ([[Anthropic launches cheaper Claude Sonnet 5 for agents]]), OpenAI's >50% inference-cost cut ([[OpenAI cuts guest ChatGPT inference costs over 50%]]) — does the piece account for the closing price gap, or assume static US pricing? — If static, dated.

14. **Who actually captures the margin?** If the trend holds, the winner is the enterprise buyer + the model-routing/orchestration layer ([[Base44 launches own AI model to seek defensibility]]), not necessarily thin-monetizing Chinese labs nor share-losing US labs. — Value migrates to the router.

15. **The policy paradox.** Is US export control the brake or the accelerant? Every Claude Fable/Mythos ban vacates a slot GLM/DeepSeek fills ([[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]], [[Asian AI startups launch Mythos-like models amid Anthropic export ban]]). — Controls are accelerating Chinese enterprise adoption, the opposite of intent.

**Importance: 3/5 — rationale.** A well-sourced FT trend piece from a credible outlet on a real, corpus-relevant shift (open-weight cost arbitrage; genuine coding/math parity; hard OpenRouter data), and it adds a *new* demand-side angle — named Western enterprises deploying Chinese models — that the corpus (which covered only the supply/geopolitics side) lacked. Held to 3, not 4: it is commentary re-framing a ~5-month-old post-DeepSeek-R1 trend, the single decisive qualifier (token share ≠ revenue share; Vercel 17% tokens / ~1% revenue) is what determines whether it is insight or hype, adoption is largely "lower-level work" / hobbyist-skewed routers rather than proven Fortune-500 production, and the US price/open-weight counter-move plus the regulatory tail risk (NDAA, Airbnb/Cursor probes) cut against a simple "US labs are losing" read. Directionally important for fintech AI cost structure, but not a hard new event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-14]] (2026-07-14).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: LLM inference economics — Chinese open-weight / low-cost models vs US closed frontier labs, read through to enterprise (incl. fintech) AI cost structures. No clean public TAM for "LLM inference spend" → "no data" (don't invent). Structure: bifurcated into (a) US closed frontier labs (OpenAI, Anthropic, Google) monetising via metered API at premium $/token, and (b) Chinese labs (DeepSeek, Alibaba Qwen, Moonshot/Kimi, Zhipu/GLM, MiniMax) competing on price + open weights. Value in the stack is migrating from the *model* to the *routing/agent layer* that lets buyers swap a cheap model into "good-enough" tasks. Entry barriers = compute/talent (several Chinese labs are US Entity-Listed, chip-constrained), NOT distribution — open weights + OpenAI-compatible endpoints collapse switching cost to a config change. **Why now (dated):** frontier US API prices stayed high (GPT-5.5 $5/$30 per 1M tok) while Chinese models closed the quality gap to ~1 pt on agentic benchmarks at 60–90% lower cost; per UBS, select Chinese models are up to ~50x cheaper per token (via cryptobriefing, 2026). OpenRouter usage: Chinese-model token share for US firms held >30% every week since 2026-02-08, peaking ~46% vs an ~11% prior-12-mo average (CNBC, 2026-07-07). **Second-order:** a real inference cost war — Chinese pricing pressures US frontier-lab gross margins on commodity tasks, pushing US labs toward premium/"hardest-work-only" positioning rather than volume.

**Competitive landscape.** Sector KPIs the race runs on: benchmark score (SWE-bench Verified, Code/Agentic Arena ELO), $/1M tokens (in/out), token-efficiency (output tok/task — a hidden cost multiplier), context window, and license permissiveness. Recent dated enterprise moves (de-PR'd — "adopted/routed," not just "announced"): DoorDash routes lower-tier work to Kimi K2.6, reserves Claude for hardest work (FT); Coinbase cut AI spend ~50% routing ~1,200 agents to Chinese models, experimenting with GLM-5.2 / Kimi as defaults (FT, Armstrong, ~2026-06-28); Lindy migrated 100% of traffic off Claude to DeepSeek; Airbnb / Uber / Siemens / others cited. **Protagonist** (the "firms" in the headline) sit as *cost-optimising adopters*, not a single company — the tradable shift is buyers hybridising: cheap Chinese model for volume/"good-enough," US frontier reserved for high-stakes. Moat note: for the Chinese models themselves the moat is thin — open weights are non-exclusive and the price/perf crown turns over monthly across DeepSeek/Qwen/Kimi/GLM (analysis).

**Comps & multiples.** The relevant "multiple" here is $/1M tokens (in / out), not an equity comp — no clean public revenue multiple for the private Chinese labs (→ EV/Revenue "no data"). Pricing table (per BenchLM / pricepertoken / DeepSeek docs, Jul 2026):
- DeepSeek V4: **$0.30 / $0.50**; V4 Flash **$0.14 / $0.28** (cheapest production-grade; one source cites $0.09/$0.18)
- Kimi K2.6 (Moonshot): **$0.95 / $4.00**, 256K ctx, 80.2% SWE-bench Verified
- GLM-5.2 (Zhipu): **$1.40 / $4.40**, ~$18/mo coding plan (per in-base note)
- OpenAI GPT-5.5: **$5.00 / $30.00**; GPT-5.2 $1.75 / $14.00
- Anthropic Claude Opus 4.8: **$5.00 / $25.00**; Sonnet 4.6 $3/$15; Haiku 4.5 $1/$5
- Arithmetic (output-cost ratio, the dominant driver for agentic/coding): GPT-5.5 vs DeepSeek V4 = `$30 / $0.50 = 60x`; Kimi K2.6 = `$30 / $4.00 = 7.5x`. UBS's "up to 50x" is directionally consistent at the cheap end. **Flag:** headline cheapness is partly eroded by token-efficiency — e.g. GLM-5.2 burns ~43K output tok/task vs 24–37K peers (per in-base note), so token-adjusted cost < headline gap. In-line-to-cheap on sticker; less so per completed task.
Internal comps: [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]] (open-weight substitution + pricing precedent), [[Linas Newsletter JPMorgan, Goldman pull Claude from employee toolkits]], [[Anthropic launches cheaper Claude Sonnet 5 for agents]] (US-lab price response), [[Base44 launches own AI model to seek defensibility]]. EV/EBITDA, P/E, forward consensus → [UNSOURCED].

**Risk flags.**
1. **Data-sovereignty / security & export-control friction (esp. fintech).** China-origin models — several on the US Entity List — carry procurement, sanctions and model-governance scrutiny for regulated Western financial institutions; routing customer/transaction data through Chinese *API* endpoints is a hard compliance blocker (open-weight self-host mitigates but is heavy — 700B-class MoE needs ~8×H200). Why it matters: the cost saving is largely unavailable to the most regulated fintech buyers via API; adoption skews to open-weight on-prem or non-regulated workloads (cf. banks keeping closed models internally).
2. **Model-reliability / eval risk.** "~1 pt off frontier on benchmarks" ≠ equivalent in production; buyers report hybridising (cheap model for low-tier, frontier for hard tasks) precisely because quality is task-dependent. Silent regressions on edge cases are a real cost if under-tested.
3. **Vendor concentration + geopolitical single-point risk.** Standardising on one Chinese lab exposes the stack to a future US import/data restriction or an Entity-List escalation; the price/perf leader also rotates monthly, so "lock-in to the cheapest" is unstable. Mitigant: model-agnostic routing (OpenAI-compatible endpoints) — which is itself where the durable margin now sits.

**What this changes (idea-lens).** Falsifiable thesis: the Chinese price/perf disruption structurally caps US frontier-lab pricing power on *commodity* inference and re-rates the value chain toward the routing/agent layer — a one-way ratchet while open weights stay non-recallable (analysis). Watch / triggers: (a) a *named* regulated financial institution running a Chinese model in production (not just experimenting) — confirms fintech read-through; currently only crypto/consumer names (Coinbase, DoorDash) disclosed; (b) US labs' response — cheaper tiers ([[Anthropic launches cheaper Claude Sonnet 5 for agents]]) or usage-based margin compression in results; (c) an export/data restriction on Chinese-model API access — would invalidate the API-adoption path and push everything on-prem. For fintech specifically the near-term change is to the *build-vs-buy / model-portfolio* decision, not yet to core regulated bank stacks.

Sources: cnbc.com/2026/07/07 (OpenRouter 46%, cost war) · techstartups.com 2026/06/29 (Western firms switching) · cryptobriefing.com (UBS 50x; FT US-companies) · techtimes.com 2026/06/28 (Coinbase ~50% cut) · benchlm.ai/llm-pricing · pricepertoken.com/deepseek · api-docs.deepseek.com · restofworld.org 2026 (DeepSeek US traction)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
