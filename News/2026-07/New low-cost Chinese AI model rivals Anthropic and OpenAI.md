---
title: "New low-cost Chinese AI model rivals Anthropic and OpenAI"
date: 2026-07-15
retrieved: 2026-07-15
tags:
  - company/anthropic
  - company/openai
  - industry/ai
  - region/asia
  - type/product
sources:
  - https://www.reuters.com/world/china/a-new-inexpensive-chinese-ai-model-is-catching-up-with-anthropic-openai-their-2026-07-02
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: sa7d49c59
month: 2026-07
enriched: true
importance: 2
freshness: stale
duplicate_of: [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]
---

# New low-cost Chinese AI model rivals Anthropic and OpenAI

> [!info] 2026-07-15 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Reuters: Новая недорогая китайская модель догоняет Anthropic и OpenAI на их поле

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.reuters.com/world/china/a-new-inexpensive-chinese-ai-model-is-catching-up-with-anthropic-openai-their-2026-07-02>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Reuters — "New low-cost Chinese AI model rivals Anthropic and OpenAI"
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS: STALE — duplicate_of [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]].** The model in the Reuters headline (2026-07-02, "a new, inexpensive Chinese AI model is catching up with Anthropic, OpenAI on their home turf") is **GLM-5.2 from Z.ai (Zhipu AI), Beijing** — confirmed across the syndicated Reuters wire (Japan Times, BusinessWorld, US News, Zawya, Express Tribune) and CNBC's 2026-06-26 Zhipu/Z.ai piece. That is the SAME model release, with the SAME core claims (coding/agentic parity with OpenAI/Anthropic at ~1/6 the cost; a "mini-DeepSeek moment"), already fully enriched in the corpus at importance 4/5 on 2026-06-22. Reuters is a **mainstream-outlet retelling** of the June GLM-5.2 open-weight launch, arriving ~2–3 weeks after the substack that broke it — a reprint/re-framing, not a new event. Per the freshness gate: same model, same figures, different source → **stale**. Enriched here at reduced weight purely for record; the analytical substance lives in the prior note and in [[FT More firms pick Chinese AI models to cut costs]] (the demand-side companion).

## [0] What exactly happened (de-PR'd)
- **The model is GLM-5.2 (Z.ai / Zhipu AI).** Shipped to GLM Coding Plan subscribers 2026-06-13; full open weights under MIT released 2026-06-16. MoE, ~744–753B total / ~40B active params. Reuters' "new, inexpensive" model = this June release, covered ~2 weeks late by the wire. (venturebeat.com; simonwillison.net)
- **Reuters' claim: "catching up with Anthropic/OpenAI on their home turf" at low cost.** De-PR'd, the specific benchmark reality (now with more July data than the June note had):
  - **SWE-bench Pro: GLM-5.2 62.1 vs GPT-5.5 58.6** — a real beat on this one long-horizon coding benchmark. (venturebeat.com; groundy.com)
  - **FrontierSWE: 74.4% vs GPT-5.5 72.6%, near-tie with Claude Opus 4.8 75.1%.** (venturebeat.com)
  - **MCP-Atlas tool-use: 77.0 vs GPT-5.5 75.3, just shy of Opus 4.8 77.8.** (venturebeat.com)
  - **Cost: $1.40 in / $4.40 out per 1M tok ≈ ~1/6 of GPT-5.5-class blended cost** — the "cheap" hook, consistent with the June note. (benchlm.ai)
  - **Endorsement cited by Reuters:** David Sacks (former White House AI czar) called it "as good as the currently available models from OpenAI and Anthropic," just below Opus 4.8, ~level with GPT-5.5.
- **Why framed this way:** Reuters anchors to a "China catches up on the US's home turf" narrative because GLM-5.2 posts genuine wins on *specific coding/agentic* benchmarks. But this is the same selective-parity story the corpus already dissected: parity is **task-specific** (coding/math/agentic), not general-frontier, and the leaderboard crown for GLM-5.2 as "world's #1 available" was partly a **usability artifact** (Claude Fable 5 pulled by the export ban), not a clean benchmark sweep — see prior note [2].

## [1] Competitors / peers
Unchanged from the prior GLM-5.2 note; nothing new added by the Reuters retelling. The honest peer set is the Chinese open-weight cohort — DeepSeek V4, Alibaba Qwen3.7-Max (closed, 1M), Moonshot Kimi K2.6 (open, 262K) — plus the US frontier (Opus 4.8, GPT-5.5) that GLM-5.2 trails at the very top of the leaderboard and on general/long-horizon agentic reliability. GLM-5.2's genuine edge remains **open-weight (MIT) + 1M sparse context + frontier-coding ELO + ~1/6 cost together.** Second-order: the crown turns over monthly across DeepSeek/Qwen/Zhipu/Moonshot — a "new leader" claim (Reuters' framing) has a short half-life. See [[FT More firms pick Chinese AI models to cut costs]], [[Asian AI startups launch Mythos-like models amid Anthropic export ban]], [[DeepSeek raises over $7 billion in debut funding round]].

## [2] Company history / fit
Unchanged: Zhipu/Z.ai — Tsinghua spinout, on the US Entity List since Jan 2025 (chip-constrained), IPO'd on HKEX (2513.HK) 2026-01-08. Open-weight + ultra-low pricing is a deliberate distribution/mindshare play — one of the few growth levers not gated by US compute access. Fully covered in the prior note.

## [3] Novelty / value-add / traction — why this is stale
- **Novelty of the Reuters piece: ~zero.** It is a wire retelling of a June release the corpus already rated 4/5. The only *incremental* facts vs the June note are (a) firmer July benchmark numbers (SWE-bench Pro 62.1, FrontierSWE 74.4, MCP-Atlas 77.0) and (b) a **Vercel adoption data point**: GLM-5.2 saw the fastest adoption of any 2026 model Vercel tracks — daily token volume ~27x and customers ~80x in its first full week. That traction is real and notable, but token-volume adoption ≠ revenue displacement (the [[FT More firms pick Chinese AI models to cut costs]] caveat: Vercel is developer-skewed; token share massively overstates dollar share for a model ~100x cheaper on output).
- **Who captures the margin:** unchanged — the deployment/agent layer (coding harness), not the non-exclusive open weights.

## [4] What's next / market sentiment
No new forward-looking content vs the prior note. The structural read stands: US export controls handed open-weight Chinese labs a distribution gift; the "China catching up" narrative is now mainstream (Reuters/CNBC picking up what substacks flagged in June), which is itself the story — but a *sentiment* signal, not a *new event*. Risk/regulatory backdrop (NDAA DeepSeek exclusion, Airbnb/Cursor probes, Entity-List friction for Western finance) is covered in [[FT More firms pick Chinese AI models to cut costs]].

## Sources
- Reuters (syndicated), 2026-07-02: https://www.reuters.com/world/china/a-new-inexpensive-chinese-ai-model-is-catching-up-with-anthropic-openai-their-2026-07-02 · Japan Times https://www.japantimes.co.jp/business/2026/07/03/tech/china-ai-catch-up/ · US News https://money.usnews.com/investing/news/articles/2026-07-02/ · BusinessWorld https://bworldonline.com/technology/2026/07/02/760688/
- Model = GLM-5.2 / Z.ai confirmation: CNBC 2026-06-26 https://www.cnbc.com/2026/06/26/china-zhipu-z-ai-open-source-anthropic-openai.html
- July benchmarks/pricing: VentureBeat https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost · BenchLM https://benchlm.ai/models/glm-5-2 · Groundy https://groundy.com/articles/glm-5-2-benchmarks-what-62-1-swe-bench-pro-and-99-2-aime-actually-mean/
- Internal (duplicate + companions): [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]] (duplicate_of — the primary enrichment), [[FT More firms pick Chinese AI models to cut costs]], [[Asian AI startups launch Mythos-like models amid Anthropic export ban]], [[DeepSeek raises over $7 billion in debut funding round]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

_Freshness gate first: this is a stale duplicate of [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]. Questions below establish that and probe the residual substance._

1. **Which model is the Reuters "new, inexpensive Chinese AI model"?** GLM-5.2 from Z.ai (Zhipu AI), Beijing — confirmed via CNBC (2026-06-26) and the syndicated Reuters wire. Not DeepSeek/Kimi/Qwen.

2. **Is this a new event or a retelling?** Retelling. GLM-5.2 shipped 2026-06-13/16; Reuters ran the wire 2026-07-02, ~2–3 weeks later. The corpus enriched the same release on 2026-06-22 at 4/5. → **STALE, duplicate_of** the June note.

3. **Do the figures match the prior note?** Yes — same ~1/6-cost hook ($1.40/$4.40 per 1M tok), same coding/agentic-parity claim, same "mini-DeepSeek moment" framing. A different-source re-report of identical substance.

4. **Anything genuinely incremental?** Two things only: (a) firmer July benchmarks (SWE-bench Pro 62.1 > GPT-5.5 58.6; FrontierSWE 74.4; MCP-Atlas 77.0); (b) a Vercel adoption stat (~27x daily tokens, ~80x customers in week one). Neither is a new *event* — refinement + traction data on the same release.

5. **Is "catching up with Anthropic/OpenAI" verified or selective?** Selective. Real beats on specific coding/agentic benchmarks (SWE-bench Pro, some tool-use), near-tie on FrontierSWE — but trails Opus 4.8 at the top and on general long-horizon reliability. Parity is task-specific, not general-frontier.

6. **Was GLM-5.2 ever "the world's #1"?** No — it was #2 on Code Arena Frontend behind Claude Fable 5; it became top *available* only because Fable 5 was pulled by the export ban. A usability artifact, dissected in the prior note.

7. **Does the David Sacks endorsement add weight?** It is a notable political/credibility signal ("as good as currently available OpenAI/Anthropic models") but not an independent benchmark — a quote, not a measurement.

8. **Does the Vercel ~80x adoption prove displacement of US labs?** No. Vercel is developer-skewed; for a model ~100x cheaper on output, token/customer growth overstates revenue displacement (the [[FT More firms pick Chinese AI models to cut costs]] token-share≠dollar-share caveat).

9. **Is the 1M context real / dense?** Sparse (DeepSeek Sparse Attention), extended not dense; independent recall quality at ~1M depth unverified at launch. Unchanged from prior note.

10. **Can a Western financial institution actually use it?** Blocked in practice — Zhipu is US Entity-Listed; China-origin governance/sanctions friction persists despite the MIT license. Adoption skews to non-aligned/Asian buyers or non-regulated workloads.

11. **Is the "cheap" story durable?** Partly eroded — high token-per-task burn (~43K output tok/task vs 24–37K peers) raises effective cost-per-task above the sticker 1/6 gap.

12. **Why did a mainstream wire (Reuters) pick this up now?** The "China catches up" narrative went mainstream 2–3 weeks after substacks/CNBC — a *sentiment* signal (the story reaching general finance readers) but not a new development. Relevant for the digest only as confirmation the theme is now consensus.

13. **Does publishing this add anything over the June note + FT note?** No. The June GLM-5.2 note owns the supply-side analysis; the FT note owns the demand-side. This Reuters item sits between them with no unique event. → drop before publish.

14. **What would have made it fresh?** A genuinely new GLM-5.3 release, a new reporting period, a named Western-bank production deployment, or a materially different figure. None present.

15. **Central question (de-PR):** Not "did a new Chinese model appear?" (no — it is June's GLM-5.2) but "does the Reuters wire add any event or number the corpus lacks?" (no — only a Vercel adoption stat and firmer benchmarks, both incremental). → stale.

**Importance: 2/5 — rationale.** The underlying subject (GLM-5.2 posting real coding/agentic parity at ~1/6 cost, amid the Anthropic export ban) is genuinely important — but the corpus already captured it at 4/5 in [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]] and framed the demand side at 3/5 in [[FT More firms pick Chinese AI models to cut costs]]. This Reuters item is a mainstream retelling of the same June release with only incremental additions (firmer benchmarks, a Vercel adoption stat). Per the freshness gate it is a **duplicate** and should be dropped before publish; scored 2/5 to reflect real but fully-covered substance with near-zero net-new event value.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** The frontier-model layer splits into three cohorts: US closed-weight incumbents (OpenAI, Anthropic, Google), Chinese open-weight labs (Z.ai/Zhipu, DeepSeek, Alibaba Qwen, Moonshot Kimi), and infra/serving. TAM: no clean sourced figure — treat as "no data" rather than cite a vendor deck. The dated facts that matter here: the model in question is **GLM-5.2**, launched June 2026 by Beijing's Z.ai (Zhipu), 5th on Artificial Analysis' intelligence leaderboard and within ~1pt of Claude Opus 4.8 on a watched agentic benchmark at roughly a fifth-to-a-sixth of the cost (per Reuters/CNBC, 2026-07-02). **"Why now" is two-sided:** (1) an API price war — Chinese open models run 60–90% cheaper than US flagships; (2) a US export/policy shock — the Commerce Dept ordered Anthropic to suspend global access to Claude Fable 5 / Mythos 5, leaving non-US developers without the top closed coding models (see [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]). Structure: the *model* layer is commoditizing (open weights + MIT license erode pricing power), while value migrates to distribution (ChatGPT), inference scale, and enterprise trust — a classic disintermediation setup for pure model licensing.

**Competitive landscape.** KPIs the sector runs on: API price/1M tokens (in/out), a capability benchmark (SWE-bench Verified, agentic-coding rank), and third-party usage share (OpenRouter token routing). Players & basis of competition: US incumbents compete on frontier capability + distribution + safety/trust; Chinese labs compete on **price and open weights**. Recent dated moves: on OpenRouter, combined US-model share fell from ~70% to ~30% YoY; **Anthropic's Claude slid from 29.1% to 13.3%**, now behind six Chinese models (CNBC, 2026-06/07); US firms routed 30%+ of weekly OpenRouter tokens to Chinese models, peaking ~46% (vs ~11% 12-mo avg). Protagonist (GLM-5.2 / Z.ai) position: **fast-follower catching up on price-adjusted capability**, not the frontier leader — its moat is cost + open-weight ecosystem lock-in, not a capability lead. US incumbents' moat (distribution, inference scale, brand) is intact on revenue but eroding on developer mindshare. Proprietary unit economics (per-token gross margin) → `[UNSOURCED]`.

**Comps & multiples.**
- **OpenAI (US incumbent benchmark, private):** $122bn raise → **$852bn post-money** (2026-03-31, closed round — round valuation, not market cap). Revenue ~**$25bn annualized run-rate** mid-2026 (~$17bn ChatGPT, ~$6.5bn API, ~$1.5bn Sora/licensing). EV/Rev ≈ `$852bn / $25bn = 34.1x` on a round valuation — rich, but the label is post-money round pricing, and it still loses ≈$1.22 per $1 of revenue. IR: OpenAI is private, no filings; `ir_latest.json` carries only the March round PR. Confidentially filed a draft S-1 (2026-06-08); 2027 IPO likelier than 2026.
- **Z.ai / Zhipu (protagonist, public):** listed HKEX Jan 2026 at **~$6.55bn** valuation (retail oversubscribed >1,000x). Revenue not cleanly disclosed → EV/Rev = **"no data."**
- **DeepSeek (open-weight peer, private):** debut raise **$7bn+** (see [[DeepSeek raises over $7 billion in debut funding round]]); prior talks reportedly above ~$20bn ([[Tencent and Alibaba in talks to invest in DeepSeek above $20B]]). Funded by a hedge fund — explicitly does not need API revenue to be profitable.
- **Price arithmetic (the actual competitive lever):** GLM-5.2 **$1.40 / $4.40** vs Claude Opus 4.8 **$5.00 / $25.00** per 1M tokens → input `5.00/1.40 = 3.6x` cheaper, output `25.00/4.40 = 5.7x` cheaper; blended ≈ 5–6x cheaper, consistent with the "fifth-to-a-sixth" claim. GPT-5.5 sits at $5/$30; DeepSeek V4 Flash undercuts all at $0.14/$0.28.
- Distribution not computed as a formal median (mixed round-valuation vs market-cap bases, only one public comp) → qualitative comparison only.

**Risk flags.**
1. **Margin capture by an upstream layer / disintermediation of the US API business** — when an open-weight model at ~1/6 the price sits within 1pt of the frontier on agentic coding, the closed-model API's pricing power compresses; Anthropic's OpenRouter share halving (29.1%→13.3%) is the leading indicator. Second-order: erodes the API revenue line US labs need to fund R&D, while the Chinese loss-leaders don't.
2. **Policy/regulatory whipsaw cuts both ways** — the export ban that *created* GLM-5.2's opening (Claude pulled abroad) is a US policy lever that could reverse; conversely, US restrictions on *deploying* Chinese weights, or Anthropic's IP claim against Alibaba ([[Anthropic accuses Alibaba of stealing Claude]]), could throttle the open-weight cohort. Concentration on a single policy variable is itself the risk.
3. **Benchmark-vs-production gap** — leaderboard rank and OpenRouter token share measure developer experimentation, not durable enterprise adoption or reliability at scale; "as good as" on a benchmark ≠ substitutable in regulated/production workloads where trust, safety, and support still favor incumbents.

**What this changes (idea-lens).** This is a **commoditization/re-rating signal for the model layer, not (yet) for the leaders' revenue** `(analysis)`: developer mindshare is repricing toward open weights while ChatGPT-style distribution keeps incumbent *revenue* growing. Falsifiable thesis — if Chinese open-model OpenRouter share holds above ~40% and enterprises (not just hobbyist tokens) migrate, US pure-API pricing compresses and value concentrates in distribution + inference scale. Trigger to watch: the next US-model release closing the price-adjusted gap, or a reversal of the Claude export ban — either would break the thesis by restoring incumbent price/mindshare.

Sources: https://www.reuters.com/world/china/a-new-inexpensive-chinese-ai-model-is-catching-up-with-anthropic-openai-their-2026-07-02 · https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html · https://www.cnbc.com/2026/06/26/china-zhipu-z-ai-open-source-anthropic-openai.html · https://openrouter.ai/z-ai/glm-5.2 · https://sacra.com/c/openai/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
