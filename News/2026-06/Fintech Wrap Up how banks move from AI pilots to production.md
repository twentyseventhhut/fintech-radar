---
title: "Fintech Wrap Up: how banks move from AI pilots to production"
date: 2026-06-14
tags:
  - company/oscilar
  - industry/banking
  - industry/ai
  - region/global
  - type/research-report
sources:
  - https://oscilar.com/blog/aibank
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sb7eb6c68
month: 2026-06
enriched: false
---

# Fintech Wrap Up: how banks move from AI pilots to production

> [!info] 2026-06-14 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] From Pilots to Production: How Banks Are Building With AI - Oscilar, accessed May 10, 2026, https://oscilar.com/blog/aibank

## Первоисточники

### oscilar.com
<https://oscilar.com/blog/aibank>
*2062 слов · direct*

Introducing the Oscilar Agent Hub
/
Read the story
->
Platform
Solutions
Industries
Resources
Company
Get a Demo
->
Introducing the Oscilar Agent Hub
/
Read the story
->
Get a Demo
->
Introducing the Agent Hub
Read the story
Introducing the Oscilar Agent Hub
/
Read the story
->
Platform
Solutions
Industries
Resources
Company
Get a Demo
->
Introducing the Oscilar Agent Hub
/
Read the story
->
Platform
Solutions
Industries
Resources
Company
Get a Demo
->
From Pilots to Production: How Banks Are Building With AI
Posted
Posted
 January 30, 2026 
 January 30, 2026 
Read time:
Read time:
13 minutes
13 minutes
Share this article
 Last updated: January 2026 
Bank technology leaders find themselves in a familiar bind: McKinsey estimates that AI could add $200 billion to $340 billion in annual value to the global banking sector, equivalent to 9 to 15 percent of operating profits. The consulting firm's vision of an AI Bank of the Future is compelling: real-time decisioning, autonomous agents, hyper-personalized service. Yet according to an MIT study from August 2025, 95% of enterprise AI pilots fail to deliver any measurable financial impact . Most banks are stuck in what the industry has come to call "pilot purgatory," running dozens of isolated experiments that never scale.
The conventional wisdom says the only way out is "rip and replace" transformation: tear out the legacy core, rebuild from scratch, accept 18-month procurement cycles and eight-figure budgets. But this narrative is both paralyzing and wrong.
A different path exists. Banks can capture 70-80 percent of AI’s potential value by focusing on a small number of high-impact subdomains and deploying modern AI infrastructure alongside legacy systems — rather than attempting multi-year core replacements.
This piece examines that path. It builds on McKinsey & Company’s AI Bank of the Future framework, which positions AI as horizontal infrastructure spanning customer engagement, decisioning, core technology, and operating models. Taking that blueprint as a given, the focus here is execution: how banks can operationalize this vision under real regulatory scrutiny, legacy-system constraints, and risk-management requirements.
Practitioners with deep experience building real-time data systems inside large financial institutions consistently observe the same gap: while banks invested heavily in moving data faster, they failed to modernize how risk decisions are made once that data arrives. The result is a proliferation of siloed tools, brittle pipelines, and slow human workflows — at precisely the moment fraudsters are coordinating attacks across the entire customer journey.
TL;DR
 Banks are stuck in “pilot purgatory.” AI adoption stalls because risk decisioning remains siloed, procurement is slow, and governance models were built for deterministic (not agentic) systems. 
 Core replacement isn’t required. Banks can capture 70–80% of the value of AI by layering a unified, real-time decisioning platform on top of legacy systems. 
 The fastest ROI is in the decision layer. Fraud, AML, credit, and compliance use cases—especially shadow mode, analyst-assist agents, and AML overlays—deliver quick, low-risk gains. 
 Progress comes from “tractable wedges.” Small, contained deployments running alongside existing systems let banks prove value, satisfy model risk management, and scale safely. 
 Governance accelerates adoption. Explainability, human-in-the-loop controls, audit trails, and AI control towers enable faster deployment while staying compliant. 
Part I: The Strategic Context
Why legacy systems can't keep pace
The typical Tier 1 bank runs on infrastructure designed for a different era. Customer data sits in fragmented silos: separate databases for credit cards, mortgages, savings, and wealth management. Building a real-time, 360-degree view of any customer requires stitching together systems that were never meant to communicate. Decisioning logic is often hard-coded into mainframes or locked inside vendor "black boxes," making even simple rule changes a multi-week engineering exercise. In practice, this often means a customer can fail identity verification during onboarding and still be approved for credit or instant payments minutes later — simply because those systems never share signals.
This architecture was optimized for stability in a world where fraud moved at human speed. Today, attackers probe onboarding flows, test payment rails, and exploit credit systems in coordinated sequences — often within minutes. The FedNow Service, which now has over 1,400 participating financial institutions , and stablecoin rails demand instant settlement . Fraudsters use generative AI to launch attacks at machine speed . Customers expect the same responsiveness from their bank that they get from their streaming service. A system that updates overnight cannot defend against threats that evolve in minutes.
When risk systems operate independently, each sees only a fragment of the attack. What looks benign in isolation becomes obvious only when signals are evaluated together and in real time.
The McKinsey blueprint
McKinsey’s AI Bank of the Future framework proposes treating AI not as a set of isolated use cases, but as horizontal infrastructure spanning four layers of the organization: Engagement, Decisioning, Core Technology & Data, and Operating Model.
The framework is directionally correct. The challenge banks face is not understanding the destination, but navigating the constraints — regulatory approval, model risk management, legacy integration, and operational safety — required to reach it.
The Engagement Layer handles customer-facing interfaces: multimodal interactions across voice, text, and image, supported by "digital twins" that simulate customer behavior and enable personalized, proactive service. The decision layer is where data becomes action: AI agents and copilots perform real-time reasoning, orchestrate complex workflows , and achieve what McKinsey projects as 20 to 60 percent productivity gains. The Core Tech and Data Layer provides the foundation: unified data architectures that break down silos , vector databases that enable semantic search across unstructured data, and LLM pipelines to manage model lifecycles. The Operating Model Layer organizes the humans: cross-functional teams, AI "control towers" for governance, and accountability structures focused on outcomes rather than project completion.
The framework is coherent. The problem is execution.
Why banks freeze
Bank leaders face three structural barriers when they try to move from vision to implementation. A BCG survey found that only 25% of institutions have woven AI capabilities into their strategic playbook — the other 75% remain stuck in siloed pilots and proofs of concept.
The first barrier is procurement. The phrase “AI infrastructure” often triggers 18-month RFP cycles involving procurement, legal, and compliance. In a technology landscape evolving this quickly, solutions selected at the start of such processes may be obsolete by deployment. Many institutions attempt to compensate by building custom pipelines internally — assembling complex streaming, rules, and analytics stacks that require large engineering teams just to keep running. For most banks, this approach is economically unsustainable.
The second is governance. Model Risk Management frameworks were designed for static, deterministic models. Generative and agentic systems introduce probabilistic behavior that must be governed continuously — through explainability, lineage, and live performance monitoring — rather than through one-time approvals.
The third is control. Banks are rightly skeptical of "transformation" pitches that require outsourcing decisioning logic to third parties. Their risk policies and customer insights are intellectual property. Ceding control of that logic to vendors inverts the value proposition.
These barriers explain the gap between enthusiasm and action. The resolution lies in reframing the task: not as a wholesale transformation, but as a series of contained deployments that prove value and build institutional capability.
The scale of transformation ahead
The stakes are becoming clearer. A Citigroup report found that 54% of jobs across banking have high potential for automation , with an additional 12% that could be augmented by AI. According to Bloomberg Intelligence, global banks will cut as many as 200,000 jobs over the next three to five years as AI encroaches on tasks currently carried out by human workers. Singapore's DBS Bank has already announced plans to reduce its workforce by 4,000 positions over three years as AI takes over roles, while simultaneously deploying over 800 AI models across 350 use cases.
Yet Accenture's research suggests the opportunity outweighs the disruption : productivity could rise by 20 to 30 percent and revenue by 6 percent for banks that implement effectively. The question is not whether to transform, but how to do so without destroying operational stability.
Part II: Five Tractable Wedges
The McKinsey framework defines what an AI-first bank looks like. What it does not prescribe is how regulated institutions can move toward that future incrementally — without exposing customers, regulators, or balance sheets to unacceptable risk. The following “tractable wedges” reflect execution patterns observed in live deployments where banks proved value first, then scaled safely.
The following “tractable wedges” are execution patterns observed in live deployments that allow banks to progress toward the AI Bank of the Future incrementally.
A wedge is a targeted implementation that introduces modern AI infrastructure alongside legacy systems without requiring wholesale replacement. The following five wedges offer varying risk profiles and immediate applicability for risk and compliance leaders.
Wedge 1: Shadow mode decisioning
 The problem: Banks hesitate to deploy new AI models directly into production because the cost of error is high. A false positive blocks a legitimate customer. A false negative allows fraud. Either outcome triggers regulatory scrutiny and customer attrition.
 The solution: Shadow mode runs a new AI decisioning engine in parallel with the legacy system. Both systems receive the same live production data. Both make decisions. Only the legacy system's decisions execute. The AI system's decisions are logged for comparison.
 How it works: Transaction and customer data streams are duplicated, often via API gateways or event streaming platforms like Kafka. One stream feeds the legacy rules engine; the other feeds the AI platform. Risk analysts compare decisions against actual outcomes. When the AI system flags a fraud ring the legacy system missed, that's evidence of "alpha." When the AI system would have blocked a legitimate customer, that's a tuning opportunity.
 Why it works: Shadow mode is effectively backtesting and forward-testing on live data with zero production risk. It builds the empirical record Model Risk Management committees require. Once the AI system consistently outperforms legacy, the bank can flip the switch or gradually ramp traffic via canary deployment. Just as importantly, it enables continuous validation. Risk teams can measure false positives, false negatives, and drift over time — aligning far more closely with how regulators increasingly expect AI systems to be governed.
 Risk Level: Low. No customer impact until the bank chooses to act on the evidence.
Wedge 2: Analyst-assist agents (L1 Triage)
 The problem: Risk and compliance teams spend most of their time on mechanical work — gathering data, switching dashboards, and dismissing obvious false positives rather than exercising judgment. Legacy transaction monitoring systems generate false positive rates exceeding 90 to 95 percent . Global AML compliance costs now exceed $274 billion annually, with much of this going toward handling low-quality alerts rather than catching criminals. Human analysts spend most of their time on L1 triage: gathering data, copying between screens, dismissing obvious false alarms.
 The solution: Deploy AI agents to perform the data gathering and preliminary analysis. The agent doesn't replace the analyst; it assembles the case file.
 How it works: When an alert triggers, an "Investigation Agent" automatically queries internal databases, external watchlists, and relevant open sources. It synthesizes findings into a natural language case narrative that explains why the alert fired and recommends a disposition. The analyst reviews the assembled work product rather than starting from a blank screen.
 Why it works: Case studies suggest this approach reduces manual review time by 75% and enables junior analysts to perform at senior levels. The human-in-the-loop remains for final judgment, which maintains governance while unlocking efficiency. The most effective deployments treat AI as an augmentation layer. Agents gather context, rank alerts, and draft narratives — but humans retain decision authority, supported by complete audit trails and explainable rationales.
 Risk level: Low to Medium. Humans retain decision authority; AI handles data aggregation.
Wedge 3: Greenfield products (stablecoins and cryptocurrency)
 The problem: Banks entering stablecoins, tokenized deposits, or crypto custody face a timing mismatch. These assets operate on blockchain rails that run 24/7 with instant settlement. The GENIUS Act, signed into law in July 2025 , established the first federal regulatory framework for payment stablecoins, requiring federal banking agencies to adopt comprehensive rules by July 2026. Traditional banking risk systems designed for T+2 settlement cannot manage risk at blockchain speed.
 The solution: Build an AI-native risk stack specifically for new product lines. Because these are greenfield deployments, there is no legacy system to displace.
 How it works: Implement a platform capable of sub-100m

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
