---
title: "Allica Bank automates SME lending with agentic AI"
date: 2026-05-04
tags:
  - company/allica-bank
  - industry/lending
  - industry/ai
  - region/uk
  - type/product
sources:
  - https://www.allica.bank/blog/scaling-ai-at-allica
  - https://www.finextra.com/newsarticle/47682/allica-introduces-fully-automated-agentic-ai-loan-decisions-in-minutes
status: tagged
n_mentions: 3
channels:
  - "Connecting the Dots in Fintech"
  - "Fintech Brainfood"
  - "This Week in Fintech"
story_id: s1c394bdb
month: 2026-05
enriched: false
---

# Allica Bank automates SME lending with agentic AI

> [!info] 2026-05-04 · 3 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Fintech Brainfood, This Week in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 Allica Bank is testing an agentic AI system that processes SME loan requests from email to credit decision in an average of 12 minutes, with no human input. Live across key brokers, it auto-decided 50% of cases, aiming to speed up complex lending while broader AI adoption expands internally.

[Fintech Brainfood] 1. Alica Bank fully automated SMB lending with AI

[This Week in Fintech] Allica Bankimplemented agentic AI to deliver fully automated loan decisions in minutes, drastically reducing wait times for small and medium-sized enterprises.

## Первоисточники

### allica.bank
<https://www.allica.bank/blog/scaling-ai-at-allica>
*2252 слов · direct*

Allica exists to serve established SMEs (ESMEs) – the roughly one-third of the UK economy made up of businesses with 5 to 250 staff that incumbent banks have structurally underserved.
These businesses are too individually complex for mass-market digital banking and too low value at high diverse volume for traditional corporate banking. The core problem we've been solving for the past six years is how to serve ESMEs at scale while still handling that complexity.
AI matters in that context for a specific reason. We’ve built software specifically to solve that volume x complexity issue – and as the fastest growing company in the UK over the last five years, this has definitely worked. However, ESMEs and their needs are highly diverse, and software alone isn’t fully suited to that challenge. Agentic AI , on the other hand, is perfect for addressing the complex and bespoke parts of the problem.
Twelve months ago, the median Allica colleague used AI on roughly a quarter of their workdays. By March 2026 that had risen to 70%. In product and engineering specifically, daily AI usage is now at 92% (and closer to 100% once you adjust for holidays).
That shift happened because we’ve been working on three different levels of progressing AI:

 Organisation-wide adoption 


 An AI-first rebuild of product and engineering 


 The development of complex agentic systems. 

Each level needed a different playbook.
This is what we did, what worked, and what we got wrong along the way.
1) Org-wide: adoption is a distribution problem, not a technology problem
The temptation with enterprise org-wide AI is to run it top-down: pick a tool, issue a mandate, measure seat occupancy. That’s unlikely to realise real benefits.
We took a different view with three main strands:
 Encourage, don't mandate. 
 We licensed a deliberately wide set of tools – ChatGPT, Codex, Microsoft Copilot, GitHub Copilot, Gemini, Claude, Perplexity, v0, Azure AI Foundry, and others – and let people find what fits their actual work, doubling down where we saw success.  
Enabling MCP (Model Context Protocol) integrations so that the LLM can draw on Allica Jira, Figma, Confluence, Hubspot, Miro, etc significantly increases the usefulness. We paired the tool enablement with lunch-and-learn sessions and peer champions in each function to share best practice and help people get up to speed. AI literacy spreads in all directions, through colleagues people already trust, and through use cases that add value to your day to day, much more than a central directive. 
Bottom-up use cases beat top-down ones.
The CEO or a central team being the sole driver of generating use cases will always be less inventive than the hundreds of people actually at the coalface of the work. 
We’ve run a monthly AI Spotlight competition with Amazon voucher prizes, which sounds trivial but delivered disproportionate results, particularly as it highlights use cases across the organisation: colleagues building structured feedback extraction across our customer call and email universe; copywriting assistants aligned to our tone of voice; rapid root-cause agents for production bugs. 
None of these were executive ideas (though we have these too!). They emerged because we gave frontline people permission and a focus.
Bake it into objectives – but last, not first.
Now for 2026, every member of our executive committee (ExCo) has OKRs covering both personal AI usage and the development of use cases within their function. The sequencing matters.
You can't meaningfully hold an ExCo accountable for AI adoption before the bottom-up signal is in place, because you don't yet know what good looks like, and you likely end up with people just gaming the KPI. 
Measurement matters throughout. An initial "has anyone in department X used an AI tool this month" metric was useful early on, but saturated quickly. The sharper number is intensity of daily active usage across all colleagues (and sub cuts by department). That figure climbed from 25% of workdays in April 2025 to 70% in March 2026, and with steep acceleration in Q1 2026.
2) Product engineering: AI-first, not AI-assisted
Engineering is where we've seen the sharpest compounding, and it's also where we've had to make the most structural changes – because the frontier tools are changing the production function itself.
The framing matters. 'AI-assisted engineering' is a team that writes code the way it always did but with the help of a coding agent. 'AI-first' is a team where AI is the default mode of work – how you do discovery, planning, design, coding, test generation and review – and where the team's structure, stack and rituals have been rebuilt around that assumption. They are different operating models. The gap between them is rapidly getting wider, as the tools improve.
We’ve looked at merged pull requests and release velocity as key indicators of the output of this shift, and as we go through 2026, we will widen this to positive product increments shipped per month - though that needs a clear definition we are working on so we know its genuinely moved the product forward, rather than just gaming a KPI! Fortunately having comprehensive AI synthesised live customer feedback is a pretty good validator.
We’ve made four moves along this path, in rough order below:
Transition to T-shaped roles
The classic specialisation of software teams – product, designer, web, mobile, back-end, data, QA – was already under pressure before AI. With agentic coding tools in the loop, it becomes an active liability: a front-end engineer who only does front-end now leaves 40–60% of a typical feature to someone else; a product owner or designer who can't ship code waits. 
We've consolidated backend, frontend and QA engineering into a single full-stack engineer, supporting individuals through six-month development plans. Our designers are on the same path – using agents to write and modify UI code, building components in our new design system, raising pull requests and running tests. A growing number are already taking well-scoped interface changes from design to production without a handoff. 
The vertical bar of the T stays sharp – depth still matters, arguably more than ever to ensure quality of the end code – but the horizontal bar is now an expectation, and the bar itself doesn't move down to match the pace of adoption.
Optimise the stack for AI – Allica Alchemy
We rebuilt our design system (only originally built in 2023, showing how quickly things become out of date currently!) on Tailwind and Radix, specifically because those primitives are what AI coding tools handle best. We’ve called this design system ‘Alchemy’.  
While this took an investment of time, the payoff once live was immediate and, frankly, larger than we expected: an 89% reduction in page build times. That isn't a marginal productivity bump.
Alongside this, we’ve been building out a shared skills library – reusable agent skills hosted in our GitHub that everyone can use and improve. This is the shift from individual AI experimentation to company capability. One person's clever prompt becomes a versioned, tested, organisation-wide tool.
Squads to squadlets
With T-shaped engineers on an AI-optimised stack, the same output can be delivered by materially smaller cross-functional units, enabling a lot more Single Thread Teams . Our target configurations are deliberately wide ranging: a minimum squadlet is one product engineer plus one full-stack engineer; standard is one product representative, one designer and up to three full-stack engineers; maximum adds a mobile engineer. 
Typical squad size is down roughly 25%. Ownership goes up because there are fewer hand-offs; quality goes up because we back squadlets with staff full-stack engineers whose job is to encode their judgment into shared, reusable artefacts – skills, lint rules, test contracts – so that senior expertise scales beyond their own hours.
Build the engineering harness
AI-generated code is only safe to ship at speed if the surrounding system – test suites, lint rules, security scans, CI/CD gates and encoded team standards – is robust enough that any change, from any author, gets caught before it reaches production.
The harness is what makes agent-driven development work in a regulated environment. It's also what makes it safe for non-engineers to contribute code changes, because the same automated checks apply regardless of who wrote the change. 
Without a strong harness, AI-first engineering for a regulated institution is reckless; with one, it compounds.
The results have compounded. Quarterly merged pull requests rose from roughly 1,900 in Q1 2025 to roughly 7,150 in Q1 2026 – a 3.8x increase year on year.
 
Across 2025 as a whole, our in-house product and engineering teams shipped over 3,700 production releases at platform uptime above 99.5% – sustained operational throughput that matters more than any single adoption headline. Benchmarked against Jellyfish's study of over 700 companies and 200,000 engineers – the most comprehensive dataset we're aware of – we sit well into the top decile on AI engineering adoption and productivity.
3) Complex agents: the real unlock for ESMEs, but where accuracy is everything
The first two layers are, in a sense, the straightforward part. Diffusive, intense adoption and AI-first engineering are now increasingly table stakes among high quality tech driven scale ups. Complex proprietary agentic systems – the kind that deliver specific, skilled knowledge work on bespoke processes – in a regulated bank are an entirely different category of work, and where we see the true final unlock of the complexity x volume problem for our ESME segment.
The strategic reason to build complex agents at Allica specifically – beyond the general capability argument – follows directly from our segment mission. 
Six years of proprietary software development gets us a long way, but software alone hits a ceiling in solving for ESMEs. 
For example in ESME credit – the quality of a management team, the specifics of a particular sector, assessing guarantor security nets and the multitude of collateral types are all genuinely bespoke, and hard to encode exhaustively in traditional software.
Agents are not simply a productivity layer on top of that software. We believe on most bespoke dimensions they do the job better than software alone ever could. Complex agents, for us, are the final piece of our thesis as to how we fully solve for this segment’s needs. But it is much easier said than done.
We started on this in late 2023, specifically aiming at a couple of complex credit analysis tasks. The initial excitement at what was achieved in a few weeks gave way to a frustrating 2024, when we found it impossible to get accuracy to sufficiently high levels to use in production. We found the models could easily get us to 85-90% accuracy, but if you needed high 90s – essential to be of the same quality as humans – that was a different story entirely. 
Mid-2025 we finally deployed agents in production, including financial statement analysis and the handling of unstructured inbound email loan applications. One of these was recognised at the FSTech Awards in March 2026 as the best use of technology in commercial finance across EMEA, which was gratifying – but the more honest framing is that we learned a lot the hard way, and those lessons are what we would share with anyone starting now.
The single most important question, which we didn't ask sharply enough early on, is: what accuracy do you actually need?
Getting a complex credit agent to 85–90% accuracy turns out to be relatively easy. This is great for the demo and the press release. But it is not sufficient for any high value or regulated process. 
To move into the very high 90s requires an order of magnitude more work, including iterative development testing using core data science principles on high quality test samples, dual-LLM validation where independent models have to agree before an output is accepted (and enabling human referral whenever they don't), ongoing validation of results in life, and explicability of what is happening. This model risk management isn't the glamour of quickly knocking out a demo that works on the happy path, but it is essential for any high value or regulated use case.
Beyond accuracy, five things matter in roughly this order:

 The ability to use a range of LLMs , because no single model is best across different tasks and models progress every few weeks 


 Data quality and readiness (where we’ve been running a cross company programme for 18 months now), because proprietary data is the future moat 


 Workflow/software integration , because an agent that works perfectly but sits outside the end-to-end process delivers close to zero value. 


 Model risk , because complex agents fall squarely inside existing model risk frameworks 


 Security , with particular attention to prompt injection, particularly where the agent will be externally facing to avoid the ‘lethal trifecta’. 

We've crystallised all of this into a three-stage process: develop accuracy (diverse model testing, modular prompts, strict JSON outputs, dual-LLM validation, document-type-specific handling), test and monitor (ground-truth validation and shadow deployment pre-launch; automated monitoring and drift detection post-launch), and govern in production (security review, model risk review, and cross-functional review with the actual user functions alongside the second line). 
The pay-off is worth the discipline – to give just one example:
We recently put live what we believe is a market-first for commercial lending: an end-to-end agent that ingests an unstructured email loan request, checks it is complete (and if not sends an email back explaining the gaps), extracts and analyses the content, calls our decisioning engine, and returns a decision, which is then sent back by email. Start to finish, no human in the loop. 
This is

### Прочие ссылки (без извлечённого текста)

- <https://www.finextra.com/newsarticle/47682/allica-introduces-fully-automated-agentic-ai-loan-decisions-in-minutes>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
