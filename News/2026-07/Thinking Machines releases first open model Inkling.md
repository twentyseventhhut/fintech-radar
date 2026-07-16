---
title: "Thinking Machines releases first open model Inkling"
date: 2026-07-16
retrieved: 2026-07-16
tags:
  - company/thinking-machines
  - industry/ai
  - region/us
  - type/product
sources:
  - https://link.techcrunch.com/click/46590558.42765/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA3LzE1L3RoaW5raW5nLW1hY2hpbmVzLWFtcHMtdXAtaXRzLWJldC1hZ2FpbnN0LW9uZS1zaXplLWZpdHMtYWxsLWFpLXdpdGgtaXRzLWZpcnN0LW9wZW4tbW9kZWwtaW5rbGluZz91dG1fY2FtcGFpZ249ZGFpbHlfcG0/6a347703be04c47cab07526aC2fad5893
  - https://substack.com/redirect/1bddeba9-f06c-41b8-9037-f63b30f77e4f
  - https://substack.com/redirect/3885cb80-3dff-4399-b807-36d3b8a1009e
  - https://substack.com/redirect/f5531b72-81d5-479c-b6f3-df1a95bd2ea0
  - https://substack.com/redirect/0f03433b-8da7-4aef-8b6f-7f465e2cc155
  - https://substack.com/redirect/fbda5683-8726-47ae-a419-0961e99b1bf1
status: enriched
n_mentions: 6
channels:
  - "MTS"
  - "TechCrunch"
story_id: sb6814bb7
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Thinking Machines releases first open model Inkling

> [!info] 2026-07-16 · 6 упоминаний · 1 источника(ов) с текстом
> Каналы: MTS, TechCrunch

## Агрегированный текст (из дайджестов)

[MTS] Thinking Machines, one of the very first neolabs, has finally released its first model, Inkling.

[MTS] Thinky’s founder, Mira Murati, started her career at Tesla and Leap Motion before joining OpenAI in 2018 and eventually becoming CTO. In 2024, she left to found her own startup, along with a number of top AI researchers¹. Thinking Machines came out of stealth in February 2025, and five months later, announced a massive $2 billion seed round at a $12 billion valuation, led by Andreessen Horowitz.

[MTS] Inkling is a 975B model with 41B active parameters, supporting up to a 1M context window, pretrained on 45T multimodal tokens. Inkling-Small is a 276B model with 12B active parameters that performs similarly to its larger sibling on most benchmarks. The model is named after the Inklings, a 1930s/40s reading group including J.R.R. Tolkien and C.S. Lewis, based out of Oxford.

[MTS] On preliminary impressions, it’s a very solid model. It’s behind the frontier, but it’s the best American open-source model currently available. It’s also easily fine-tuneable on Tinker. On benchmarks, it underperforms top models (Fable, Sol, GLM-5.2) on agentic coding, but performs quite well on multimodal and on IFBench, which measures precise instruction-following.

[MTS] TL;DR it’s already the best American open-source model, and with some more iterations it might become a true frontier model, or at least power a much better consumer product.

[TechCrunch] Thinking Machines amps up its bet

## Первоисточники

### link.techcrunch.com
<https://link.techcrunch.com/click/46590558.42765/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA3LzE1L3RoaW5raW5nLW1hY2hpbmVzLWFtcHMtdXAtaXRzLWJldC1hZ2FpbnN0LW9uZS1zaXplLWZpdHMtYWxsLWFpLXdpdGgtaXRzLWZpcnN0LW9wZW4tbW9kZWwtaW5rbGluZz91dG1fY2FtcGFpZ249ZGFpbHlfcG0/6a347703be04c47cab07526aC2fad5893>
*1289 слов · direct*

Thinking Machines amps up its bet against one-size-fits-all AI with its first open model, Inkling
Thinking Machines Lab, the AI startup founded by former OpenAI CTO Mira Murati, released its first in-house AI model Wednesday morning, called Inkling . And unlike the flagship models from OpenAI, Anthropic, or Google, it’s open-weight, meaning outside developers and companies can download it and modify it directly.
Inkling is a mixture-of-experts system with 975 billion total parameters, though it only draws on a fraction of that — about 41 billion — for any given task, a common design that keeps very large models faster and cheaper to run. It was trained on 45 trillion tokens of text, image, audio, and video, and reasons natively across all four, according to the company’s own release materials. For now, though, its outputs are limited to text, including code, styled artifacts, and structured data.
The model is Thinking Machines Labs’ first public proof point after a year and a half spent building AI infrastructure largely out of public view. Some of that work had already surfaced in a May research preview of “interaction models” — AI designed to listen and speak (and even interrupt) instead of stop and wait as with typical chatbots. It’s also a test of the central bet behind the startup, which is that AI that organizations can adapt for themselves will outperform the one-size-fits-all models the biggest labs currently sell.
Inkling is designed to give calibrated answers, including flagging uncertainty rather than guessing, and lets users dial “thinking effort” up or down when they want to trade for speed. On one benchmark, the company says, Inkling uses a third as many tokens as Nvidia’s Nemotron 3 Ultra — its latest generation open-weight model — to hit the same coding performance.
Thinking Machines doesn’t claim Inkling is best-in-class. Its newest blog post states explicitly that Inkling is “not the strongest overall model available today, open or closed.” What it’s evidently going for instead is well-rounded performance.
That raises the question of who, within the enterprise market it’s targeting, this product is really for. Thinking Machines is, for now, marketing Inkling less as a finished product than as a starting point, something for organizations to fine-tune themselves through Tinker, the company’s model-customization platform. This also means customers, not Thinking Machines, are responsible for making sure their customizations are safe, for example. (Fine-tuning requires serious machine-earning talent.)
OpenAI, Anthropic, and Google have all taken a very different approach with ChatGPT, Claude, and Gemini, respectively, which were all built to compete as general-purpose chatbots first, with agentic, autonomous features layered on top.
A post published by Thinking Machines last week was clearly meant as the backdrop for this release. AI that’s trained centrally by one company and then set in stone, the company argued in that post, underperforms AI that organizations shape themselves because so much expertise is specific to the people who hold it. 
Other arguments against closed models are gaining steam. In a blog post published Sunday, Microsoft CEO Satya Nadella — whose company has invested billions in both OpenAI and Anthropic — warned that enterprises using proprietary AI models effectively pay twice : once in subscription costs, and again by handing over business knowledge embedded in their prompts and corrections, which can be absorbed into future model versions.
Hugging Face CEO Clem Delangue made a similar prediction in conversation with TechCrunch last week. Frontier models, he said, will increasingly be reserved for experimentation and high-value tasks, while most production AI work shifts to private or open-source alternatives — the exact split Thinking Machines is building around.
The clearest argument for Thinking Machines’ approach came from a recent project with Bridgewater Associates, the world’s largest hedge fund (which is not, for what it’s worth, a Thinking Machines investor). Researchers from both companies took an existing open-source model and trained it further on Bridgewater’s own financial expertise. The result was said to score 84.7% on financial reasoning tests, beating top proprietary AI models, while costing roughly a fourteenth as much to run — though those results come from the two companies’ own evaluation, not an independent one.
Either way, Thinking Machines is emphasizing how quickly it got here. OpenAI took roughly five years to bring its tech to market and show revenue, and Anthropic roughly three. Thinking Machines says it did the same in about nine months.
Some will wonder whether Inkling was trained on outputs from competitors’ models, a practice known as “ distillation ” that has drawn scrutiny across the industry. The short answer, per the company’s own materials, is partly. Thinking Machines pre-trained Inkling from scratch, but it says it used other open-weight models — including Moonshot AI’s Kimi K2.5 — to help generate some of its early post-training data before large-scale reinforcement learning took over. The next model, the company insists, will use fully self-contained post-training instead.
On the cost side, Thinking Machines has been more guarded. It struck a partnership with Nvidia in March to deploy a gigawatt of Vera Rubin computing capacity and trained Inkling entirely on Nvidia’s GB300 NVL72 systems — but hasn’t said how it plans to cover those costs, and revenue, by most accounts, hasn’t been a priority. (A reported $50 billion fundraising round was said to be coming together last November but had stalled by January; the company has declined to talk about its funding picture since.)
A related question is whether Thinking Machines’ spending will ever reach the scale of OpenAI’s or Anthropic’s, or whether its efficiency-driven approach means the economics look different. Put another way, the company’s bet may be less that it will eventually spend like its larger rivals than that it won’t need to at all — because once weights are public, nothing obligates anyone who downloads them to pay Thinking Machines to run them, unlike the metered access OpenAI and Anthropic sell. It’s Tinker, not the model itself, where the company’s revenue has to come from, via training, fine-tuning, and, now, a cut of the hosting ecosystem built around it. 
Headcount, at least, looks more settled. Thinking Machines now employs roughly 200 people, up from levels reported after a wave of departures earlier this year, including two co-founders who left for OpenAI in January.
Thinking Machines, for its part, doesn’t seem interested in playing up individual moves the way much of the industry does. According to a source inside the company, its culture, by design, favors continuity over reliance on any one personality. It makes sense: it’s less of a setback when people change teams if they were never put on a pedestal to begin with. It’s also a remarkable thing for a company to insist on, given how much of its own story is still associated with the name of its now-famous co-founder, whether she planned it or not.
Topics
 When you purchase through links in our articles, we may earn a small commission . This doesn’t affect our editorial independence. 

 Editor in Chief & General Manager 
 
 Last chance to save up to $190 on TechCrunch Founder Summit. Join 1,000+ founders and VCs at all stages for real-world scaling insights and connections that move the needle. Savings end June 26, 11:59 p.m. PT .
Most Popular

 
 
 
 
 Anthropic’s newest ad is creeping people out 
 
 
 
 Lucas Ropek 

 
 
 
 
 Satya Nadella has issued a shocking warning to companies using AI 
 
 
 
 Julie Bort 

 
 
 
 
 The wildest allegations in Apple’s trade secrets lawsuit against OpenAI 
 
 
 
 Sarah Perez 

 
 
 
 
 Anthropic starts localizing Claude pricing for India, its biggest market after the US 
 
 
 
 Jagmeet Singh 

 
 
 
 
 Meta removes controversial AI feature on Instagram after backlash 
 
 
 
 Lucas Ropek 

 
 
 
 
 Apple sues OpenAI over alleged trade secret theft 
 
 
 
 Sarah Perez 

 
 
 
 
 Instagram users: Here’s how to stop Meta’s AI from using your photos 
 
 
 
 Lauren Forristal

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/1bddeba9-f06c-41b8-9037-f63b30f77e4f>
- <https://substack.com/redirect/3885cb80-3dff-4399-b807-36d3b8a1009e>
- <https://substack.com/redirect/f5531b72-81d5-479c-b6f3-df1a95bd2ea0>
- <https://substack.com/redirect/0f03433b-8da7-4aef-8b6f-7f465e2cc155>
- <https://substack.com/redirect/fbda5683-8726-47ae-a419-0961e99b1bf1>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Thinking Machines releases first open model Inkling
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS/DUPLICATE VERDICT: fresh.** This is a distinct NEW event — the first shipped model from Thinking Machines Lab (Inkling, released 2026-07-15). The internal corpus surfaces TML only as (a) a *mission-statement* item four days earlier ([[Thinking Machines publishes human-centered AI mission statement]], 2026-07-11, a values credo — no product) and (b) a *talent* item ([[Barret Zoph rejoins OpenAI as VP after Thinking Machines exit]], same day, a departure). Neither covers this product launch. Note the mission-statement note already flagged (correctly) that TML had "no shipped flagship model" as of 2026-07-11 — Inkling is the very thing whose absence it noted. So this is the **product proof-point** those prior notes were waiting on, not a reprint. FRESH.

## [0] What exactly happened (de-PR'd)
On **2026-07-15** (Wed AM) Thinking Machines Lab released **Inkling**, its first in-house model, **open-weight** (per multiple outlets, **Apache 2.0**). De-PR'd facts:
- **Architecture:** mixture-of-experts, **975B total / ~41B active** parameters; a smaller **Inkling-Small (276B total / 12B active)** said to match the big model on most benchmarks. **1M context** window. Pretrained on **45T multimodal tokens** (text/image/audio/video), reasons natively across all four, **but outputs text only** (code, structured data, styled artifacts) for now.
- **Controllable "thinking effort":** a tunable effort parameter (reported range ~0.2–0.99) trading tokens for speed; calibrated answers that flag uncertainty.
- **Honest self-assessment (rare):** the company's own blog states Inkling is **"not the strongest overall model available today, open or closed."** It is positioned as **well-rounded + a fine-tuning starting point**, not a frontier chatbot.
- **+ Why structured this way / what it reveals:** The release is deliberately **not** a ChatGPT-style consumer product — it is a **substrate for Tinker** (TML's fine-tuning/customization platform). That is the whole business logic: once weights are public (Apache 2.0), *nothing obligates a downloader to pay TML to run the model* — so revenue cannot come from metered inference the way it does for OpenAI/Anthropic. It must come from **Tinker** (training/fine-tuning + a cut of the hosting ecosystem). The open-weight choice is therefore not idealism but the **only monetization path consistent with the "organizations adapt their own models" thesis.** The "distillation" admission (below) and the "not the best" candor are also strategic: they inoculate against the two attacks TML most fears (copycat/derivative, and overclaiming).

## [1] Competitors / peers
The relevant field is **open-weight frontier-class models**, and here the standout finding is that **TML is racing largely Chinese labs, not American ones:**
- **GLM-5.2 (Zhipu/Z.ai, MIT, Jun 2026):** ~744B/40B active, top open-weight on SWE-bench Pro (62.1%), 1M context via IndexShare. The current all-round open-weight leader.
- **Kimi K2.5 / K2.6 / K2.7-Code (Moonshot AI):** ~1T/32B active, multimodal, strong agentic coding. **TML admits it used Moonshot's Kimi K2.5 to help generate early post-training data** — i.e. its nearest peer is also partly its teacher.
- **Nemotron 3 Ultra (Nvidia):** the open-weight baseline TML benchmarks against — Inkling reportedly matches it on Terminal-Bench 2.1 at **~1/3 the tokens** and leads heavily on MCP Atlas agentic (74.1% vs 44.7%).
- **DeepSeek V4 Pro:** another Chinese open-weight peer in the safety/benchmark tables.
- **Closed frontier (OpenAI/Anthropic/Google — Fable, Sol, etc.):** ahead on agentic coding; TML doesn't try to match them and says so.
- **Position:** Inkling is credibly **"the best American open-source model"** on the aggregated read — but that title is narrow: it is *behind the frontier*, and the genuinely strong open-weight models (GLM, Kimi, DeepSeek) are **Chinese**. So the real claim is "best open-weight model *not* subject to a China-origin trust/compliance objection" — which for regulated buyers (US enterprise, government, **finance**) is exactly the axis that matters.
- **+ Why the landscape is this way / second-order:** Open-weight leadership migrated to China in 2025–26 because Chinese labs use open weights as **distribution + soft-power** while US frontier labs kept weights closed to protect metered revenue. TML's opening is precisely this **US-origin + open-weight** white space — but it is a *fragile* moat: the benchmark deltas are small, and if OpenAI/Meta/Google ship a competitive open model, TML's differentiation collapses to "Murati + Tinker."

## [2] Company history / fit
Trajectory (dated): founded / out of stealth **Feb 2025** (Murati + ex-OpenAI researchers) → **Jul 2025 $2B seed at $12B** (a16z-led) → **Oct 2025 Tinker** (fine-tuning API) → **Nov 2025** rumored **$50B** up-round, **stalled by Jan 2026** → **Jan 2026** co-founders Zoph & Metz + researchers defect to OpenAI (see [[Barret Zoph rejoins OpenAI as VP after Thinking Machines exit]]) → **Mar 2026** Nvidia partnership (1 GW Vera Rubin; Inkling trained entirely on **GB300 NVL72**) → **May 2026** Interaction Models research preview → **Jul-11 2026** mission credo ([[Thinking Machines publishes human-centered AI mission statement]]) → **Jul-15 2026** Inkling. Headcount now **~200**, up from post-exodus lows.
- **+ Why the company acts this way:** TML raised on **pedigree, not product**, then took a **valuation-reset + talent-exodus** hit. Inkling is the **overdue proof-of-life** that must convert story into a shippable, benchmarkable asset before the next raise — hence the emphasis that it got here in **~9 months** vs OpenAI's ~5 years / Anthropic's ~3. The open-weight + Tinker structure fits a lab that (a) can't outspend OpenAI/Anthropic and is **betting it won't need to**, and (b) needs a monetization story that doesn't depend on winning the consumer race it has already conceded.

## [3] Novelty / value-add / traction
- **What's genuinely new:** (1) a **US-origin, open-weight, frontier-*adjacent* multimodal MoE** — a real capability, not an announcement; weights are downloadable. (2) **Controllable thinking-effort** as a first-class dial. (3) **Token efficiency** (1/3 of Nemotron's tokens for equal Terminal-Bench) — economically meaningful.
- **Distillation caveat (anti-PR):** TML admits it used **other open models (incl. Kimi K2.5)** to generate *some* early post-training data before RL — so "trained from scratch" is only *partly* true; the next model is promised to be fully self-contained. Take the "all our own work" framing with skepticism.
- **Traction — thin, and mostly self-reported:** all benchmark numbers (AIME 97.1%, SWEBench-V 77.6%, IFBench 79.8% vs Kimi 76%, FORTRESS safety 78%) are **from TML's own release**, not independent. The strongest *use-case* proof — the **Bridgewater** collaboration (84.7% on financial reasoning, ~1/14th the run cost, beating proprietary models) — is likewise a **joint self-evaluation, not independent**, and Bridgewater is **not** an investor. No disclosed external adoption, revenue, or download counts yet.
- **+ Why the value-add is/isn't real, deeper:** In this stack the model itself captures **no margin once open-weight** — anyone can host it free. Margin has to accrue to **Tinker** (fine-tuning + a cut of the hosting ecosystem). So the central question is **not** "is Inkling a good model" (it is decent) but **"will enterprises fine-tune *on Tinker* rather than on the many rival open weights + commodity fine-tuning tooling?"** Fine-tuning "requires serious ML talent," which shrinks the addressable buyer to sophisticated shops (hedge funds, big enterprises) — the exact **Bridgewater** profile. That is a **real but narrow** wedge, and it is contestable: HuggingFace, cloud providers, and the Chinese open-weight labs all sit in that value-capture layer too.

## [4] What's next / market sentiment
- **Watch:** (1) **independent** benchmark verification (all current numbers are first-party); (2) real **Tinker** adoption/revenue — the only place TML monetizes; (3) whether the **next model** delivers the promised fully self-contained (no-distillation) post-training; (4) the **next fundraise** and whether Inkling re-rates TML up from $12B after the failed $50B; (5) the **cost question** — TML has been guarded on how it funds the 1 GW Nvidia commitment.
- **Structural tailwind:** the **"pay twice"** argument (Satya Nadella: enterprises using closed models pay in subscriptions *and* by handing over embedded business knowledge) and HuggingFace's Delangue view (frontier = experimentation, production shifts to open/private) both favor exactly TML's split. See [[Prime Intellect raises $130M Series A for enterprise AI agents]] for the adjacent "own-your-AI-stack" thesis.
- **+ Why the market goes this way / counterintuitive second-order:** Open-weight + Tinker makes TML **structurally lower-margin per model but potentially stickier** — if it becomes the default *fine-tuning substrate* for regulated US enterprises wary of Chinese weights. But the same openness that is its distribution advantage is its **margin trap**: it hands the model away and must recapture value one layer up, where incumbents (clouds, HuggingFace) already sit. So capital/talent concentration cuts both ways — Inkling proves TML can ship, but a single competitive US open model (from Meta/OpenAI) would erase the one axis where it currently leads. **Fintech relevance is above the AI-industry baseline** here specifically because of the **Bridgewater financial-reasoning use case** — the clearest signal that domain-fine-tuned open models can beat proprietary ones on cost for finance workloads.

## Top challenge/extra questions
See challenge file.

## Sources
- TechCrunch, "Thinking Machines amps up its bet against one-size-fits-all AI with its first open model, Inkling" (2026-07-15): https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/
- Thinking Machines Lab, "Inkling: Our open-weights model": https://thinkingmachines.ai/news/introducing-inkling/ ; Model card: https://thinkingmachines.ai/model-card/inkling/
- Bloomberg, "Murati's Thinking Machines Releases First AI Model for Broad Use" (2026-07-15): https://www.bloomberg.com/news/articles/2026-07-15/murati-s-thinking-machines-releases-first-ai-model-for-broad-use
- MarkTechPost, "Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal MoE…" (2026-07-15): https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/
- VentureBeat, "Thinking Machines open sources first multimodal language model, Inkling…": https://venturebeat.com/technology/thinking-machines-open-sources-first-multimodal-language-model-inkling-focused-on-low-cost-and-resistance-to-censorship
- OfficeChai, "Thinking Machines Releases Open-Weights Model Named Inkling, Shows Strong Benchmark Results Among Open Models": https://officechai.com/ai/inkling-benchmarks/
- Kingy AI / Composio (open-weight peer context, GLM-5.2 / Kimi / DeepSeek, 2026): https://kingy.ai/news/best-open-weight-ai-models-in-2026-glm-5-2-vs-deepseek-v4-vs-kimi-k2-6-vs-qwen-vs-mistral/ ; https://composio.dev/content/glm-vs-kimi
- Internal: [[Thinking Machines publishes human-centered AI mission statement]], [[Barret Zoph rejoins OpenAI as VP after Thinking Machines exit]], [[Prime Intellect raises $130M Series A for enterprise AI agents]], [[Neolab Mirendil exits stealth with $200M seed at $1B valuation]], [[Menlo Ventures raises record $3 billion fund on Anthropic bet]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is this actually new, or a re-run of the Jul-11 mission note?** New. Jul-11 was a values credo with *no product*; Jul-15 is the first *shipped, downloadable* model. This is the proof-point the prior note explicitly flagged as missing. — **Fresh, distinct event.**
2. **Announced or launched?** Launched — Apache-2.0 open weights are downloadable, with a model card and benchmarks. Not a "will explore." — **Live.**
3. **Are the benchmarks independent?** No — AIME 97.1%, SWEBench-V 77.6%, IFBench 79.8%, FORTRESS 78%, and the Nemotron token-efficiency claim are **all first-party** from TML's release. — **Self-reported; OPEN on independent verification.**
4. **Is "best American open-source model" a real claim or a narrow one?** Narrow. Inkling is *behind the frontier*; the genuinely strongest open-weight models (GLM-5.2, Kimi, DeepSeek) are **Chinese**. The real claim is "best *US-origin* open-weight," which matters mainly to buyers who won't touch Chinese weights. — **True but qualified.**
5. **Was it distilled from competitors?** Partly, by TML's own admission — used **Moonshot's Kimi K2.5** to generate some early post-training data before RL. "From scratch" is only partially true; next model promised to be self-contained. — **Distillation caveat confirmed.**
6. **Where does TML actually make money?** Not the model — open weights mean anyone hosts it free. Revenue must come from **Tinker** (fine-tuning + hosting-ecosystem cut). — **Model = loss-leader; Tinker = the business.**
7. **Who captures the margin in this stack?** Contested. The value-capture layer (fine-tuning tooling, hosting) is also occupied by HuggingFace, cloud providers, and Chinese open-weight labs. TML must win the *fine-tuning substrate* fight, not the model fight. — **Margin trap; OPEN.**
8. **How real is the Bridgewater proof point?** 84.7% financial-reasoning, ~1/14th cost, beating proprietary — but it's a **joint TML+Bridgewater self-evaluation**, not independent, and Bridgewater is **not an investor**. Strong *directional* signal, weak as verified proof. — **Compelling but self-graded.**
9. **Who is the buyer, given fine-tuning "requires serious ML talent"?** Sophisticated shops only (hedge funds, large enterprises) — the Bridgewater profile. Narrows the TAM sharply. — **Niche, high-touch.**
10. **Does this re-rate the $12B valuation?** Unknown. The **$50B up-round died in Jan 2026**; Inkling is the shipping proof that could support the next raise, but no new mark is confirmed. — **OPEN — watch next round.**
11. **How is the 1 GW Nvidia / GB300 compute funded?** TML has been guarded; no cost/revenue disclosure. Open-weight release means no metered-inference revenue to amortize it. — **Financing overhang; OPEN.**
12. **Multimodal in, text out — is "multimodal" overstated?** Somewhat. Trained on text/image/audio/video and reasons across them, but **outputs text only** for now. — **Input-multimodal, not output-multimodal.**
13. **Does Inkling square with the "human-centered" mission (Jul-11)?** Loosely — "organizations adapt their own models / keep expertise in-house" is the operational form of that credo. More coherent than most manifesto→product gaps. — **Reasonably consistent.**
14. **What's the biggest downside trigger?** A competitive **US open-weight model from Meta/OpenAI/Google** — that would erase TML's only current differentiator (US-origin + open) and collapse it to "Murati + Tinker." — **Single-axis fragility.**
15. **Fintech relevance?** Above the AI-industry baseline *specifically* because of the **Bridgewater financial-reasoning** case — evidence that domain-fine-tuned open models can beat proprietary ones on cost for finance. Otherwise an AI-industry story. — **Moderate, via the finance use case.**

**Importance: 3/5** — rationale: This is a **real, shipped, open-weight frontier-adjacent model** (not a manifesto or a hire) from a marquee founder — a genuine proof-of-life after a valuation reset and talent exodus, which lifts it clearly above the Jul-11 mission note (2/5). The **token-efficiency** and **US-origin open-weight** angles are substantive, and the **Bridgewater financial-reasoning** result gives it real (if narrow) fintech relevance. It is **not 4** because: all benchmarks are self-reported, adoption/revenue is zero-to-undisclosed, the "best" claim is narrow (Chinese labs lead open weights), there's a distillation caveat, and the whole business rests on the *unproven* bet that enterprises fine-tune on Tinker rather than rival open weights. A solid, weighable product event — but the value-capture question is wide open.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: foundation-model labs / **open-weight LLMs** — Thinking Machines Lab (TML, founded 2024 by ex-OpenAI CTO Mira Murati) shipping its first model into the open-weight tier, not the closed-API tier. No credible TAM figure is publicly verifiable for "open-weight models" as a stand-alone market — **no data** on size/CAGR; do not invent one. Structure: **capital-intensive and consolidating at the top** — a handful of well-funded labs (OpenAI, Anthropic, Google closed; Meta Llama, Mistral, DeepSeek, Alibaba Qwen, Moonshot Kimi, GLM open) plus a long tail of neo-labs. Entry barriers are extreme (compute + talent): TML trained Inkling on Nvidia GB300 NVL72 and struck a March-2026 deal for **~1 GW of Vera Rubin capacity** (per TechCrunch/note). Drivers / "why now": (1) an emerging **"pay twice" thesis** against closed models — Microsoft CEO Nadella (blog, ~2026-07-12, via TechCrunch) argued enterprises pay in subscription *and* in surrendered proprietary knowledge; (2) HF CEO Delangue's split — frontier closed models for experimentation/high-value tasks, **open/private models for production** (TechCrunch, week of release). Second-order effect: value migrates from the model to the **adaptation + inference layer**, which is exactly where TML is trying to stand (Tinker).

**Competitive landscape.** KPIs the open-weight tier actually competes on (none of which are $-KPIs): **benchmark rank** (agentic coding, IFBench, multimodal), **tokens/task efficiency** (cost proxy — TML claims Inkling hits Nvidia Nemotron-3-Ultra coding parity with ~1/3 the tokens), **license permissiveness** (Inkling is **Apache 2.0**, per MarkTechPost/NewsCord — material for finance/legal/healthcare adoption), and **downloads/derivatives + fine-tune ecosystem**. Basis of competition: product/efficiency/license, not price (weights are free). Recent peer moves: GLM-5.2 shipped 1M context ([[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]]); DeepSeek V4 imminent + raising ([[DeepSeek raises at $71B valuation, prepares 2027 IPO]]); Ollama/HF distribution rails growing ([[Open source AI tool Ollama raises $65M, nears 9M users]]). Day-one distribution: Inkling **live on Databricks** (Databricks blog, 2026-07-15) — a real adoption signal, not just an announcement. TML's position (analysis): **catching up, not frontier** — the company itself states Inkling is "not the strongest overall model available today, open or closed," and the note calls it merely "the best *American* open-source model," behind GLM-5.2/Sol/Fable on agentic coding. Moat (analysis): **not the model** (weights are copyable) but (a) the Murati/researcher brand for fundraising and (b) **Tinker** as the customization/hosting toll-booth — a switching-cost/ecosystem moat that is still unproven (**TML is pre-revenue**, per Contrary Research/TechCrunch).

**Comps & multiples.** TML last marked at **$2bn seed / $12bn post** (Feb–Jul 2025, a16z-led; per note + TechCrunch). A reported ~$50bn round was floated Nov-2025 but **stalled by January** and remains unconfirmed — treat $12bn as the live mark, the $50bn as **[UNSOURCED]** rumor. All figures below are **private round valuations, not market caps**, and revenue is undisclosed for every private peer → **EV/Revenue and P/S not computable** (no data). Qualitative comparison only:
- **Safe Superintelligence** — ~$32bn post, **pre-product, ~20 staff** (TechCrunch/Calcalist) — the purest "team+thesis" comp; TML at $12bn is *cheaper* but is now shipping.
- **Mistral** — in talks ~€20bn (~$23bn) at ~€3bn raise (Bloomberg/TechCrunch, 2026-06-12); prior €11.7bn Series C (Sep-2025). Open-weight incumbent with claimed >€1bn 2026 revenue ambition (Mensch, via search) — a *revenue-bearing* open-weight peer, unlike TML.
- **DeepSeek** — reportedly ~$71bn target, ≥$1.5bn raise, 2027 IPO prep ([[DeepSeek raises at $71B valuation, prepares 2027 IPO]]) — open-weight, but shipping frontier-adjacent models.
- Internal team-bet comps: [[Neolab Mirendil exits stealth with $200M seed at $1B valuation]] ($1bn, pre-product) and [[Nous Research nears $75M+ round at $1.5B valuation]] ($1.5bn, open-source, live product + ~214k GitHub stars).
- **Flag:** $12bn for a pre-revenue lab is *not* an outlier vs SSI ($32bn) or DeepSeek ($71bn) — the tier prices on talent/compute-access, not fundamentals; multiples "not computed, qualitative comparison." The rich-vs-cheap read is unanswerable without revenue → **no data**.

**Risk flags.**
1. **Monetization / free-rider risk (structural).** Open weights mean *nobody who downloads Inkling is obligated to pay TML to run it* (note). Revenue must come from Tinker + a hosting cut, but Tinker is unproven and TML is pre-revenue — the entire thesis rests on capturing the adaptation layer while giving the model away. Second-order: if inference commoditizes on partners (Databricks et al.), TML captures little of its own model's usage.
2. **Compute-cost vs revenue mismatch.** A ~1 GW Vera Rubin commitment and GB300-class training against **no disclosed revenue plan** and a stalled mega-round = a burn/funding-durability risk; efficiency-first strategy only works if TML genuinely *won't* need OpenAI-scale spend (note frames this as the open question).
3. **Not-frontier + distillation dependency.** Inkling is explicitly not best-in-class and used **Moonshot Kimi K2.5 outputs** to bootstrap post-training data (partial distillation, per company materials) — an industry-scrutinized practice; also a reminder that being "best *American* open model" is a narrow, geopolitically-scoped claim, not a global lead.

**What this changes (idea-lens).** (analysis) This is a **layer-shift bet, not a re-rating**: the interesting question isn't Inkling's benchmark rank but whether "give the model away, sell the customization + hosting toll" beats metered-API economics for the enterprise. **Falsifiable thesis:** if TML's next model ships with *fully self-contained* post-training (no competitor-distillation, as promised) AND Tinker shows real paid fine-tuning revenue, the adaptation-layer moat is real. **What breaks it:** if Inkling adoption accrues to hosting partners (Databricks/Ollama/HF) while Tinker stays flat, TML becomes a subsidized upstream commodity funding others' inference margins — watch Tinker paid-usage disclosure and the fate/existence of the rumored next round as the trigger.

Sources: https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/ · https://www.databricks.com/blog/inkling-thinking-machines-lab-now-databricks · https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/ · https://research.contrary.com/company/thinking-machines-lab · https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/ · https://techcrunch.com/2025/04/12/openai-co-founder-ilya-sutskevers-safe-superintelligence-reportedly-valued-at-32b/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
