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
status: tagged
n_mentions: 6
channels:
  - "MTS"
  - "TechCrunch"
story_id: sb6814bb7
month: 2026-07
enriched: false
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
_(пусто — заполняется при обогащении)_
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_(пусто)_
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
_(пусто)_
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
