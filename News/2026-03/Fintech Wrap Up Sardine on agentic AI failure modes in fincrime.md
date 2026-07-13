---
title: "Fintech Wrap Up: Sardine on agentic AI failure modes in fincrime"
date: 2026-03-22
tags:
  - company/sardine
  - industry/fraud-risk
  - industry/ai
  - region/global
  - type/research-report
sources:
  - https://www.sardine.ai/blog/agentic-ai-financial-crime-failure-modes
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s6632e7ca
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Sardine on agentic AI failure modes in fincrime

> [!info] 2026-03-22 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] The 3 Failure Modes of Agentic AI in Financial Crime (and How to ..., accessed March 15, 2026, https://www.sardine.ai/blog/agentic-ai-financial-crime-failure-modes

## Первоисточники

### sardine.ai
<https://www.sardine.ai/blog/agentic-ai-financial-crime-failure-modes>
*2210 слов · direct*

Financial crime teams are at a breaking point.
Not because fraud is new or because money laundering is suddenly harder to detect. But because the scale of financial crime is now fundamentally mismatched with the way most institutions are staffed and operated.
A typical financial services company has an enormous percentage of its workforce tied up in investigation-heavy workflows: fraud operations, transaction monitoring, sanctions review, onboarding compliance, disputes, and customer support.
Fraud isn’t just increasing, it’s accelerating faster than any human team can respond.
Scammers are using AI. Deepfakes are getting cheaper and more convincing. Attack cycles are shrinking.
And yet inside most institutions, the day-to-day reality looks the same: alert queues dominated by false positives, customers locked out for no clear reason, legitimate businesses stuck in review limbo.
Just two years ago, the only lever banks and fintechs could pull to address it was to throw even more warm bodies at it.
But it’s 2026, and the industry is doing what it always does when manual work becomes unscalable: it’s turning to automation. Only this time, it actually has the means to do so with Agentic AI.
Specifically, AI systems that can gather evidence, interpret context, produce investigation-ready conclusions, and in some cases, even take action autonomously.
And yet, despite all the excitement, most early deployments of AI agents in financial crime fail.
Not because the models are weak, but because how they are deployed is wrong.
How so?
In regulated environments, an agent that produces confident narratives without guardrails doesn’t reduce risk, it creates a new one.
And risk teams, surprisingly, don’t like risk. 
These teams quickly realize they end up spending their time on validating, correcting, and hand-holding AI agents.
They aren’t more efficient. They aren’t spending their time on more important tasks. Frustration builds, and the project gets bogged down, or in the worst case scenario - it gets completely sidelined.
But if you deploy it correctly?
When we A/B tested on Sardine’s own on-ramp platform, we found that flows supported by AI agents didn’t just reduce labor. They also showed 49% faster time-to-revenue. That’s a quantifiable impact on business growth, not just efficiency savings.
Why fincrime teams fail with Agentic AI
After building and deploying AI agents in real-world fraud and AML workflows, we’ve seen three predictable failure modes show up again and again.
If you’re considering AI agents for fraud, AML, or transaction monitoring, understanding these failure modes is the difference between building a force multiplier and building a liability.
The 3 failure modes of AI Agents
Failure mode #1: The Hallucinating Investigator
The most common mistake teams make is deploying AI agents with too much context and capabilities. 
The thinking is understandable: “ We have a lot of data. Let’s feed the model everything. It will figure it out. ”
In practice, this is the fastest path to hallucination.
The problem isn’t that modern models are incapable. The problem is that fincrime investigations are fundamentally adversarial and evidence-driven, and large, open-ended prompts increase the chance that the model fills gaps with assumptions.
If you ask an agent to “review this customer’s entire profile and determine if this is suspicious,” you’ve given it a task that is too vague, too broad, and too interpretive.
And the model will do what models do best: it will generate a plausible narrative.
Even if that narrative is wrong.
This gets worse by the fact that hallucinations in fraud and AML are often subtle. The agent might infer a business category incorrectly, assume a relationship between two counterparties, or claim that a transaction is unusual when it is completely normal for that industry.
This is why agentic AI in fincrime must be built on a principle that feels almost counterintuitive: Less context often produces more reliable conclusions.
In other words, avoid deploying a “super-agent” that knows everything. Instead, implement a set of narrow agents that each know how to do one thing extremely well.
This is one of the reasons why Sardine is focused on developing what we call “atomic agents”, or AI agents designed around specific investigation primitives. For example:
A Data Analyst agent that can interpret transactional data
An OSINT agent that can perform external research and summarize findings
A KYB agent that can validate business identity and ownership relationships
A Graph Analyst agent that can interpret entity networks and shared identifiers
The fundamental design philosophy is that agents do not replace humans, but instead replace a specific skill. Since today’s fraud investigations require a variety of skills, and each step in the process demands a dedicated AI agent.
This approach reduces hallucination risk dramatically because each agent operates inside a smaller decision boundary. Instead of “guessing” what matters, it is asked to retrieve, interpret, and summarize specific data in a specific context.
 That’s how you build systems that are not just intelligent, but reliable. 
Failure mode #2: The Over-Suspicious Agent
The second failure mode is more operational than technical. Even when AI agents don’t hallucinate, they often suffer from a different flaw: they are too quick to assume something is nefarious.
This isn’t because models are “paranoid.” Fraud detection is inherently pattern-driven, and models are trained to recognize signals. But in financial crime, signal recognition without contextual grounding produces a predictable outcome: over-escalation.
The agent sees a high-value payment to a foreign counterparty and flags it.
The agent sees multiple entities connected through shared addresses and assumes it’s a shell network.
The agent sees circular flows and suggests layering.
To a human reviewer, the output sounds intelligent. It uses the right vocabulary and “sounds” like an experienced investigator. But it often misses the most important reality of fincrime operations: most alerts are false positives.
This is where many AI deployments accidentally create a new bottleneck by increasing workloads, not reducing them. Because now your analysts are not just reviewing alerts, they’re reviewing the agent’s reasoning too, which is often overly suspicious.
This failure mode shows up most clearly in transaction monitoring, where a huge percentage of flagged behavior is not criminal at all.
A good example is self-dealing.
Self-dealing is one of the most common patterns that triggers alerts, especially for high-volume businesses. It can look like suspicious circular movement, but in reality it is often just money moving across related accounts, subsidiaries, or internal entities.
To an AI agent trained on “fraud signals,” these can look like suspicious anomalies. To a real investigator, they are normal business operations.
Why does this happen?
We tend to think that training AI on large datasets can teach it all it needs to know. But in reality, true domain expertise is the insights we have on that data . And these insights are by default outside of the dataset.
Tinkering with the dataset or with prompts can only get you so far. To inject real-life domain expertise we need to design agents that are explicitly trained and constrained to ask the right questions:
Does this counterparty category make sense for this business?
Is this transaction self-dealing or third party?
Are the entities connected through ownership, shared identifiers, or operational structure?
Is this pattern consistent with the industry’s normal flows?
When agents are forced to reason in these frameworks, they become far less likely to “jump to fraud” as the default conclusion.
Failure mode #3: The Black Box Agent
Even if your AI agent avoids hallucination and over-suspicion, it can still fail in the most important way:
It can produce conclusions that are not defensible.
In financial crime, accuracy is not enough. If an agent flags a business as suspicious, a compliance team still has to answer:
What evidence did the agent use?
What data sources did it rely on?
Can the decision be reproduced?
Would an auditor accept this reasoning?
Would a regulator accept it?
This is where many AI tools break down.
They output a narrative, but they don’t show the chain of evidence. They cite external information vaguely without clear sourcing. They provide a recommendation without documenting why.
But in regulated environments, AI cannot be a black box. It has to be an evidence machine. A good AI agent should behave less like a chatbot and more like a structured investigator:
It should pull data deterministically (e.g., from defined queries)
It should summarize findings in consistent formats
It should explain why a counterparty is relevant
It should highlight uncertainty instead of masking it
This changes our definition of what “black box AI” means. It’s no longer about whether I understand the decision or reasoning of a model.
When agents operate inside investigation workflows, such as alert queues, case management, analyst escalation, they need to produce outputs that humans can approve, defend, and audit.
 This is why one of the most important agentic capabilities is not reasoning. It’s documentation. 
How to deploy AI agents for optimized ROI
If hallucination, over-suspicion, and black-box outputs are the predictable failure modes, then the solution isn’t incremental tuning. It’s structural.
You don’t fix these problems by asking the model to “be more careful.” You fix them by redesigning how investigation work is decomposed, executed, and documented. That’s the foundation behind how we built Sardine’s AI Agent Garden , a set of atomic agents, each one replacing a specific investigation skill, not a whole investigator.
Our goal isn’t to create a single omniscient “fraud brain” that can do everything. Instead, we’re creating a system that behaves like a seasoned investigation team: specialists that do their piece of the work, leave a clean trail, and hand off to the next step.
Let’s look at some examples.
The Data Analyst Agent: “What happened?” 
Most investigations start with the same problem: the raw data is unreadable at human speed. Transaction monitoring is the clearest example. 
You’re staring at hundreds or thousands of transfers and trying to answer questions that are simple to ask but painful to answer: Who are the top counterparties? What’s the distribution of risk? What’s outward versus inward flow? Is the “weird” behavior a pattern or a one-off? 
The Data Analyst Agent is designed to do that first pass, fast. It produces a structured view of activity, including sessions and transactions in the recent time window, ranked counterparties, high-value and high-risk items surfaced first, and context like directionality and timing. 
In our Transaction Monitoring setup, that starts from deterministic retrieval, or pulling a defined set of transactions within a defined time range so the agent isn’t improvising what it analyzes.
This is where the most practical value shows up: when the agent compresses data querying and analysis into a single brief that a human can scan and immediately know where to look next.
The OSINT Agent: “What’s the context?”
Once you can see what happened, the next bottleneck is interpretation. Most compliance teams aren’t short on data, they’re short on context . A counterparty name by itself rarely tells you whether a transaction makes sense. And in transaction monitoring, “makes sense” is the whole game.
The OSINT Agent is built for the simplest but most time-consuming task in investigations: turning an entity string into an intelligible business category and a credibility check. Is this a real business? What do they do? Are they plausibly connected to the customer’s line of business? Do they have signals that indicate mismatch, shell behavior, or outright fabrication? 
Crucially, this isn’t done for every counterparty. It’s done for the ones that matter: the highest-risk and highest-value counterparties surfaced earlier. That’s how you keep OSINT from becoming an endless rabbit hole (and token sink) and turn it into a repeatable investigative step.
A good example is when a human investigator is looking at a business connection graph and sees a high-risk entity tied to an address in Geneva. On paper, the address looks “legit,” but it could just as easily be a virtual office, a PO box, or a shared services location used by dozens of unrelated businesses.
Instead of forcing an analyst to manually research the address across multiple sources, the OSINT Agent runs directly from the address node in the graph and produces a structured summary of what that location actually represents.
In this case, the agent finds plenty of data that positions the address as an exclusive office building located in a prestigious area of Geneva. But it also highlights the fact that it’s likely being used as a PO Box hub that can potentially harbor illicit activity.
That last point is critical. In fincrime, investigators don’t just need more data, they need to know which data is misleading .
The Graph Analyst Agent: “What’s connected that shouldn’t be?”
If the OSINT Agent tells you what an address is, then the Graph Analyst Agent tells you who else is using it.
In the example above, once the OSINT Agent clarified the Genevan address context and highlighted the possibility of shared usage and data inconsistencies, the next logical question wasn’t “is this address prestigious?” It was: how many other businesses are actually tied to it? 
That’s where the Graph Analyst Agent takes over.
Instead of forcing an investigator to manually investigate all related entities one by one, the agent runs a full Connections Graph search on the business and surfaces every linked entity through shared identifiers. 
In the case shown, the graph immediately surfaced multiple businesses

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
