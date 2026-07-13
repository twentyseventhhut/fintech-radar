---
title: "Fintech Wrap Up: why Unit21 rebuilt around AI agents"
date: 2026-03-22
tags:
  - company/unit21
  - industry/regtech
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://www.unit21.ai/blog/the-new-unit21-why-we-rebuilt-everything-around-ai-agents
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sce09b127
month: 2026-03
enriched: false
---

# Fintech Wrap Up: why Unit21 rebuilt around AI agents

> [!info] 2026-03-22 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] AI Agents for AML and Fraud: Why Unit21 Rebuilt Everything, accessed March 15, 2026, https://www.unit21.ai/blog/the-new-unit21-why-we-rebuilt-everything-around-ai-agents

## Первоисточники

### unit21.ai
<https://www.unit21.ai/blog/the-new-unit21-why-we-rebuilt-everything-around-ai-agents>
*2296 слов · direct*

The New Unit21: Why We Rebuilt Everything Around AI Agents
Seven years ago, I wrote some of the first lines of code at Unit21. The thesis was simple: risk and compliance teams shouldn't need an engineering degree to build fraud and AML rules. We called it "no-code for risk," and it worked.
‍
Intuit, Chime, Green Dot, and hundreds of other companies used it to ship detection logic in minutes instead of week-long or month-long sprints. We raised $92 million from some of the best in venture capital, Tiger Global, Google's Gradient Ventures, ICONIQ, and others. We achieved product-market fit.
‍
And then the world changed.
‍
 Financial Crime Is Scaling Faster Than Risk and Compliance Teams 
 Financial crime is now a multi-trillion-dollar problem. FinCEN receives nearly 5 million suspicious activity reports a year, up over 70% from five years ago , and that number is accelerating. The average AML team spends four or more days building a single SAR.
‍
They have 30 days to file. The math doesn't work. And it's getting worse: deepfake fraud surged over 1,100% in the past year alone, synthetic identities are flooding onboarding pipelines, and real-time payments have compressed fraud detection windows from days to milliseconds.
‍
Meanwhile, risk and compliance teams are drowning. Up to 95% of AML alerts are false positives , leading to manual reviews that burn analyst hours and budgets, producing nothing. Every bank, every fintech, every payments company is running the same playbook: hire more analysts, pile on more rules, hope the backlog doesn't catch fire before the next exam.
‍
That playbook is broken.
‍
Rules alone can't keep up. Machine learning models adapt, but they need thousands of examples to correlate patterns, they can't explain their decisions to a regulator, and they take months to develop a new model as fraud attacks adapt. The industry has been stuck choosing between speed and safety, between automation and auditability. We spent years building no-code tools to make that tradeoff less painful.
‍
Then we realized the tradeoff itself was the problem.
‍
 Why Rules-Based Fraud Detection Is Reaching Its Limits 
In 2025, we started building something fundamentally different. Not better rules. Not a smarter dashboard. Not an AI "copilot" that helps analysts Google faster. AI Risk Infrastructure. 
‍
We built AI agents that execute the investigation workflow end to end: pull the data, analyze the patterns, check the sanctions lists , review adverse media, write the narrative, produce a recommendation, and document every step for the regulator.
‍
This wasn't incremental. It required rethinking the entire architecture. The founding team, myself included, rebuilt the system from the ground up around agentic AI.
‍
 What Makes AI Agents Different From Other Risk and Compliance AI Tooling 
Here's what I mean by that. Most "AI" in risk and compliance today falls into one of three categories. 
‍
1. AI Summarization Tools
The first is summarization: paste an LLM on top of a legacy system and let it generate a paragraph. It looks impressive in a demo. It doesn't close an alert. 
‍
2. Risk and Compliance Chatbots
The second is chat: give an analyst a chatbot to ask questions, one at a time, one investigation at a time. The analyst still drives every step. The analyst still forms the judgment. The analyst still writes the narrative. If this is what your vendor is offering you, why not use a general-purpose chatbot?
‍
3. Standalone AI Alert Review Tools
And then there's a third category that's even more limited: AI vendors with no platform underneath. No rules engine . No case management . No detection logic. No transaction data. They can review an alert someone else generated, but that's where it ends.
‍
Want to tune a rule based on what the agent learned? Can't. Want to optimize detection thresholds from disposition patterns? Can't. Want the agent to file a SAR or update a risk score ? Can't. Without the underlying infrastructure, the AI has nowhere to act and nothing to act on. It lacks the full data required and capabilities to take meaningful action outside of a paragraph write up.
‍
These three approaches share the same fundamental constraint: the analyst is still the bottleneck. 
‍
 How AI Agents Automate the Financial Crime Investigation Workflow 
Our agents are different. They're configured to a customer's specific standard operating procedures, thresholds, and risk appetite . They don't wait for an analyst to ask a question. They execute the workflow the analyst would have executed, step by step, and then they hand over the results for human review. The agent doesn't replace judgment. It performs the work and shows its work.
‍
Since we launched AI Agents in May 2025, it’s been averaging over 100,000 reviews per month and growing. Underdog Fantasy cut its alert volume by 72%. Nexo reduced false positives by 57% and is now targeting 80%. 
‍
Existing customer partnerships are expanding at 2x, and we're winning head-to-head against stand-alone AI agent products thoroughly, because bolt-on solutions can't match what seven years of production infrastructure delivers.
‍
 Why Production Infrastructure Matters for AI  
Today we're relaunching Unit21. New brand. New site. New identity. But this isn't a cosmetic refresh.
‍
We are no longer "no-code transaction monitoring and case management." We are the leader in AI Risk Infrastructure. That's not a tagline. It's a statement based on 100+ customers adopting AI Agents in their risk programs as a core and foundational change to investigations.
‍
It is where the entire industry is headed, and we’re here to ensure your team is the one setting the pace. We aren't just building tools for today; we are defining the AI-driven future of risk so your program remains at the cutting edge. We aim to make the global financial system safer, and we believe agentic AI makes that possible for the first time.
‍
AI Agents Built Across the Full Risk and Compliance Stack
And how are we doing this? Fundamentally, we ship out-of-the-box AI agents across the full risk and compliance stack: AML transaction monitoring , real-time fraud prevention , sanctions screening , KYT, EDD, check fraud, ACH fraud, account takeover, elder abuse, adverse media, case management, Suspicious Activity Report (SAR) filing, device intelligence , and Unit21’s proprietary fraud consortium . 
‍
Not one workflow. The whole thing. Each agent is configured to a customer's SOPs, thresholds, and risk appetite. Each one produces a recommendation tied to evidence, a regulator-ready narrative in the customer's format, and a transparent work log showing every step taken and every data source used. If it's not defensible to a regulator, we don't ship it.
‍
A System That Learns and Improves
But here's what no one else is doing. Our AI doesn't just review alerts. It creates new detection logic for you. AI rule recommendations analyze patterns across your dispositions and suggest smarter rules you didn't know you needed.
‍
And the whole system auto-tunes itself based on your human analysts' approval. Every disposition, every escalation, every confirmed outcome feeds back into the agents and makes them sharper. The more your team uses it, the better it gets. That's not a roadmap item. It’s live today.
‍
No one is even close to where we are. And they're not even close to where our full vision will go.
‍
 The Competitive Landscape is Loud. Production is Quiet. 
I'll be direct about what I see happening in our market right now.
‍
There's a lot of capital chasing AI in financial crime. New entrants are raising large rounds and flooding the market with buzz about "trust infrastructure" and "AI agents." Legacy players are slapping "agentic AI" on their roadmap slides. The press releases are impressive. The category is heating up.
‍
Good. The problem is big enough that it needs more investment and more urgency.
‍
Show Me the Work
But here's what I'd ask any risk and compliance leaders evaluating these vendors: show me the work. Not a demo. The actual work the AI did on a real alert.
‍
Our agents show all of their work. Every recommendation comes with the evidence it's based on, a regulator-ready narrative written in your format, and a transparent log of every step taken, every data source checked, every assumption made. 
‍
That's not a feature. That's the entire architecture. In fact, relying on opaque systems for risk and compliance decisions creates significant institutional risk, as these 'black box' models often fail to meet the rigorous evidentiary standards required by examiners.
‍
Built to Fit Your Process and Scale With It
Our agents are configured to your SOPs. Not a generic workflow you bend your process around. Your thresholds, your risk appetite, your investigation steps, your narrative format. And when your process changes, your team updates the agent in minutes, not via a six-month professional services engagement.
‍
Our agents run in parallel. Thousands of alerts simultaneously, without an analyst initiating each one. A chatbot that helps an analyst research faster is still analyst-constrained. One person, one chat, one investigation. That scales linearly. Our agents scale with your business.
‍
AI That Compounds Over Time
Our agents compound. Every disposition, every escalation, every confirmed outcome feeds back into the system and makes the next decision sharper. Pair that with automating rule tuning that analyzes your patterns and generates detection logic you didn't know you needed, and the system isn't just keeping up with financial crime. It's getting ahead of it.
‍
And our agents go deep. OSINT, adverse media, check image analysis, document verification, entity networks of 400+ connections, across millions of transactions. Try running that through a chatbot.
‍
 Why Leadership Matters in an AI-First Company 
I want to say something that might sound self-serving, but I believe it's critical.
‍
I recently started shipping code again. After years in leadership, I'm back in the codebase, building AI agent configurations, pushing commits, and working directly with our engineering team on the systems that power our product. It's invigorating. And it matters more than most people realize.
‍
I wrote some of the first lines of code at this company. I led our AI team before becoming COO. I know how every layer of this system works because I helped build it. That combination, deep technical understanding of how the AI actually works, paired with seven years of seeing how risk and compliance teams actually operate, is what drives our product decisions.
‍
This extends beyond me. Product managers, designers, sales engineers, and implementation managers are shipping code. Our engineering teams are able to ship things in days that would have otherwise taken months. Across the entire organization, people are scaling their output by multiples of what it was a year ago. That's not a tagline. That's what happens when you have AI-native leadership that can actually drive it.
‍
 What I Actually Believe About AI in Financial Crime 
I'll lay out my convictions plainly, because I think clarity matters more than hedging in a moment like this.
‍
AI Agents Will Not Replace Fraud and Compliance Analysts
They will replace the primary work of the analyst. The job description is changing to one of empowerment, decision-making, and strategic work. The job isn't disappearing. You will be correcting AI decisions and workflows, rather than having to do the same repetitive tasks yourself. You’ll be preventing more financial crime than ever before, and your expertise is more important now than in the past; it’s now your role to help monitor and guide the AI systems to ensure high-quality outcomes.
‍
Explainability and Agentic AI Are Not Opposites
The common objection is that AI can't be trusted in regulated environments because you can't explain how it works. That's an engineering problem, not a fundamental limitation. We built our governance around the frameworks examiners actually use: OCC 2011-12, SR 11-7, NIST AI RMF. 
‍
We don't train models on customer data. Every output is logged, versioned, and traceable. We run evaluations against real cases before deployment and continuous scoring with quality control checks built in. Human-in-the-loop isn't a checkbox; it's architectural. We present this to regulators regularly. We solved it.
‍
Efficiency Is Table Stakes. Effectiveness Is the Real Prize.
Every vendor in this space can promise you'll close alerts faster. Fewer of them can promise you'll catch more actual financial crime. A human eye can only catch so much when consumed with false positives, but AI doesn’t get alert fatigue.
‍
We’ve found AI actually catching fraud that humans had missed. We are bullish on betting that it will not only save time but also save you money in losses. Speed without quality is just faster failure. We're building for both.
‍
The Convergence of Fraud and AML Is Inevitable
Siloed teams running separate systems for fraud detection and AML monitoring are an institutional liability. The data is shared. The criminals don't care about your org chart. The systems (and data) must be unified.
‍
This Is Not Just a Product Problem. It's a Societal One.
Financial crime funds trafficking, cartels, terrorism financing, and exploitation. When compliance teams drown in false positives , the real threats slip through. Every alert an AI agent closes accurately is capacity returned to the analysts who are working the cases that actually matter. I've spent 7 years on this because the work we're enabling actually stops harm. We are on a mission to make the financial system safer and we finally have the technology to make a meaningful dent in the problem.
‍
We're Equipping Our Own Team the Same Way We Equip Our Clients
We believe people and processes are a competitive edge in the age of AI, not a liability. Every team at Unit21, engineering, sales, customer success, leg

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
