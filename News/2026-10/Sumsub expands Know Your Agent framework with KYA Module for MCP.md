---
title: "Sumsub expands Know Your Agent framework with KYA Module for MCP"
date: 2026-10-20
retrieved: 2026-10-20
tags:
  - company/sumsub
  - industry/regtech
  - industry/ai
  - region/global
  - type/product
sources:
  - https://financialit.net/news/artificial-intelligence/sumsub-expands-know-your-agent-putting-businesses-control-what-ai
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s814c2fe0
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Sumsub expands Know Your Agent framework with KYA Module for MCP

> [!info] 2026-10-20 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Sumsub expands its Know Your Agent framework with a new KYA Module for MCP. The module lets businesses define exactly what their AI agents can access inside company systems. It strips personally identifiable data before it reaches the agent.

## Первоисточники

### financialit.net
<https://financialit.net/news/artificial-intelligence/sumsub-expands-know-your-agent-putting-businesses-control-what-ai>
*666 слов · direct*

London, United Kingdom
 Tuesday 20 October 2026 / 06:02
 Login 
 Sign Up 
 
 
 
 
 Sumsub Expands Know Your Agent, Putting Businesses in Control of What AI Agents Can Access 
 Artificial Intelligence
 19.10.2026 09:08 am 
 Sumsub, the first AI-powered trust infrastructure for compliance operations at scale, today expanded its Know Your Agent (KYA) framework with the launch of the KYA Module for MCP. The module enables businesses to define exactly what the AI agents they build or deploy — whether in-house or on top of models such as Claude or ChatGPT — are allowed to access inside company systems.  
 Sumsub will ensure clients can confirm a real, accountable human stands behind any action that crosses a sensitive threshold. This builds on two earlier milestones. In January, Sumsub launched AI Agent Verification within its Know Your Agent (KYA) framework, binding AI-driven automation to a verified human identity. In June, it introduced its industry-first Model Context Protocol (MCP) integration, letting agents configure and operate the platform directly.  
 As AI agents connect to file storage, communication platforms and financial systems, they routinely request broad access to complete tasks. Once access is granted, many businesses have limited visibility into what an agent actually did with it. Recent research found that 65% of organizations experienced at least one security incident caused by an agent operating on their network in the past year, with sensitive data exposure the leading cause. In July, an OpenAI model acting as an autonomous agent breached Hugging Face's production systems, accessing internal datasets with no human authorizing the action. 
 The KYA Module for MCP addresses this with a filtering module between an agent and the data it connects to. The module screens every agent request, strips personally identifiable and other sensitive information before it reaches the agent, and applies a fully configurable rule engine enabling a business to have precise control, triggering defined actions based on data sensitivity, the type of action, the requesting department, the calling department, and other parameters set.  
 When an agent tries to access a flagged file or take an action above a set threshold, such as approving an invoice above a defined limit or accessing a document outside its permitted scope, the system can trigger a real-time liveness check to confirm a real, authorized human is behind the request. Businesses can also layer in additional verification steps, such as questionnaires or address verification, depending on the sensitivity of the action. 
 Key capabilities include: 
 Data access filtering: Screens every request an agent sends to connected data sources and removes sensitive or personally identifiable information before it reaches the agent. 
 Agent activity log: Gives businesses a clear, auditable record of what each agent has requested and done. 
 Rule-based transaction monitoring: Allows businesses to define what an agent can access or execute, including limits on sensitive files and financial thresholds. 
 On-demand liveness verification: Triggers a liveness check when an agent attempts a flagged or high-value action, confirming a verified human authorized it. 
 Built for MCP: Businesses set organization-wide rules for their agents – starting with Amazon Bedrock AgentCore Gateway, with support for additional MCP gateways to follow. 
 "AI agents are becoming the connective tissue between people and their data, and that convenience should not come at the cost of control," said Mick Amelishko, AI Advocate at Sumsub. "This gives businesses a clear record of what their agents are doing and a way to confirm a real person stands behind the actions that matter most, so companies can adopt agentic AI without losing sight of the decisions being made on their behalf." 
Related News
 19.10.2026 01:45 pm 
 19.10.2026 01:35 pm 
 16.10.2026 11:14 am 
 16.10.2026 10:19 am 
 15.10.2026 11:57 am 
 15.10.2026 09:46 am 
 15.10.2026 06:10 am 
 14.10.2026 04:28 pm 
 14.10.2026 11:13 am 
 14.10.2026 11:02 am 
 14.10.2026 10:22 am 
 14.10.2026 09:25 am 
 Latest Issue 
 FinTech List 
 Payment gateways 
 Challenger banks 
 Challenger banks 
 Challenger banks 
 Challenger banks 
 Popular Tags 

 Download our new app
 

 Get FinTech news headlines, videos, stories and product reviews on your mobile device. Download Financial IT App for Free

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sumsub expands Know Your Agent framework with KYA Module for MCP
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-10-19/20 Sumsub launched the **KYA Module for MCP** — a filtering/policy layer that sits between an AI agent and the company data/tools it connects to over the **Model Context Protocol (MCP)**. Concretely it does four things: (1) **PII stripping** — screens every agent request to a connected data source and removes personally identifiable / sensitive data before the agent sees it; (2) a **configurable rule engine** keyed on data sensitivity, action type, and requesting/calling department, with financial thresholds; (3) an **agent activity log** (auditable record of what each agent requested and did); (4) **on-demand liveness verification** — when an agent attempts a flagged file or a high-value action (e.g. approving an invoice above a set limit), it triggers a real-time liveness check to confirm an authorized human is behind the request.
- **Live vs announced:** The module ships "**Built for MCP**" and launches **starting with Amazon Bedrock AgentCore Gateway**, with "support for additional MCP gateways to follow." So it is **live on exactly one gateway** today — the broad "works with any MCP agent" framing is aspirational. No named customers, no adoption numbers, no pricing. The only named human quote is from **Mick Amelishko, AI Advocate** (a marketing/evangelist title, not CPO/CTO) — a tell that this is a positioning release, not a flagship product drop.
- **Why structured this way:** The module is deliberately built as a **man-in-the-middle proxy on the MCP transport** rather than inside the agent or the model. That lets Sumsub insert itself regardless of which model (Claude, ChatGPT, in-house) the client uses — it monetizes the *connection point*, not the model. **→ why it matters:** the value capture is at the data-egress boundary, which is exactly where AWS's own AgentCore Gateway already applies Bedrock Guardrails (PII filters, content policy). So Sumsub's differentiator is not the filtering per se but the **liveness/human-binding escalation** — the one thing AWS's gateway can't do.
- **The threat framing is doing heavy lifting:** the PR anchors to "65% of organizations had ≥1 agent-caused security incident last year" and a July incident where an OpenAI model "breached Hugging Face's production systems." These are unsourced/second-hand scare stats — treat as marketing, not verified.

## [1] Competitors / peers
The agent-identity/MCP-security space got crowded fast in 2026:
- **Auth0 (Okta)** — "Auth for MCP" went GA **2026-05-06**; scopes agent operations on behalf of a verified user to exact tools/APIs. Okta also shipped its own MCP server with least-privilege per-tool-call control.
- **Amazon Bedrock AgentCore Gateway** itself — applies PII filters, content policy, prompt-attack detection via native Bedrock Guardrails *at the gateway layer*. **This is simultaneously Sumsub's launch platform AND its substitute** for the data-filtering half of the pitch.
- **Descope** (Agentic Identity Hub), **Aembit** (identity-aware workload/agent access via MCP), **SailPoint** (Agent Identity Security — discovery/governance across clouds).
- Adjacent in the fintech corpus: [[Incognia launches MCP Server for AI-driven fraud investigations]] and [[FXC Intelligence launches MCP server on AWS]] — MCP is the standard everyone is wrapping in Oct 2026; [[Meta and Sierra introduce Personal Agent Protocol standard]] and [[Mollie offers €50M equity to build banking for AI agents]] show the agent-infra land-grab.
- **Position:** Sumsub is **at parity on filtering/logging** (table stakes vs AWS/Auth0) but **differentiated on liveness + agent-to-human binding** — it is the identity-verification incumbent extending its KYC/liveness stack to agents. **→ second-order:** the IAM vendors (Okta/Auth0/Entra) own the *authorization* layer and the enterprise relationship; Sumsub owns *biometric liveness*. If regulators/insurers demand "a real human authorized this," Sumsub's liveness is hard for IAM vendors to replicate; if they only demand scoped tokens + logging, Sumsub is a feature AWS/Auth0 bundle for free.

## [2] Company history / fit
Sumsub (UK-based, "AI-powered trust infrastructure for compliance at scale") has a clear, dated agentic trajectory:
- **2026-01-29:** launched **AI Agent Verification** inside the KYA framework — binds AI automation to a verified human identity (agent-to-human binding); CTO Vyacheslav Zholudev framed it as "verify the humans behind agents." [internal: covered in corpus]
- **2026-06-19:** **MCP integration** — agents (Claude/ChatGPT) configure/operate the Sumsub platform from an AML policy doc; first verification platform listed on ChatGPT Apps ([[Sumsub launches MCP integration for AI agent compliance setup]]).
- **2026-10-20:** **KYA Module for MCP** — the inverse of June: June let agents *operate Sumsub*; October lets Sumsub *police agents operating on client systems*.
- Broader 2026 cadence: Summy AI Copilot ([[Sumsub launches Summy AI Copilot for compliance teams]]), fraud registry ([[Sumsub launches fraud-prevention registry and badge system]]), Satoshi Test, travel-rule for Fireblocks, synthetic-fraud reports ([[Sumsub report identity fraud rate falls but attacks surge 180%]]).
- **Why Sumsub acts this way:** core KYC/liveness is commoditizing (ComplyAdvantage, Persona, Onfido, Jumio all compete on price). The structural pressure is to **move up-stack into higher-margin "trust infrastructure"** — agentic identity is a new, un-commoditized line where Sumsub's liveness biometrics are a genuine moat. KYA is Sumsub re-using its single real asset (verified-human liveness) against a new buyer (AI-governance budgets).

## [3] Novelty / value-add / traction
- **Genuinely new:** the specific combination of **MCP-transport request filtering + liveness-escalation on sensitive actions** is novel in market framing. Sumsub claims to be "the only verification solution offering human binding."
- **How it differs from prior art:** AWS Guardrails / Auth0 do PII + scopes; they do **not** inject a biometric liveness check mid-flow. That escalation ("agent hit a high-value threshold → prove a real human is here") is the actual differentiator and the reason this isn't just a reskin of AgentCore features.
- **Traction = zero disclosed.** No customers, GMV, or pilots named — only "starting with Amazon Bedrock AgentCore Gateway." This is an **announcement, not adoption.** Previous KYA milestones (Jan, June) also have no public adoption numbers in the corpus → pattern of launch-without-traction.
- **Who captures the margin:** the risk for Sumsub is **disintermediation by the gateway.** It launched *on* AgentCore Gateway, whose owner (AWS) already does filtering natively. If AWS, Okta, or Anthropic bake liveness-escalation into the gateway/protocol, Sumsub becomes an optional plugin, not the control point. Value capture holds only if liveness stays a specialist biometric capability that platforms prefer to buy rather than build.

## [4] What's next / market sentiment
- **Stated plan:** extend beyond AgentCore to additional MCP gateways; layer in questionnaires/address verification per action sensitivity.
- **Backdrop:** MCP became the de-facto agent-tooling standard through 2025–26; agentic-AI governance is the hot 2026 fintech/regtech theme (see corpus cluster of Oct MCP launches). EU AI Act + emerging "human accountability for autonomous actions" expectations are the regulatory tailwind that makes *liveness/human-binding* specifically valuable (vs generic access control).
- **Risks / counterintuitive second-order:** (a) **standard-capture risk** — if agent-identity consolidates into the protocol layer (MCP itself, or Meta/Sierra-style agent protocols) or into IAM incumbents, point solutions get squeezed; (b) **UX friction** — a liveness check mid-agent-workflow defeats the "autonomy" selling point, so real-world usage will be rare/edge-case, capping revenue; (c) the heavy reliance on **scare statistics** suggests the buyer urgency isn't yet organic. **→ Central question** isn't "is agent governance a real market" (yes) but "does the human-liveness escalation become a required control or an occasional nice-to-have that platforms absorb for free."

## Sources
- Primary: financialit.net / Sumsub newsroom (2026-10-19) — in note body column two.
- Sumsub newsroom, PYMNTS, Help Net Security (2026-01-29) — AI Agent Verification.
- Sumsub / The Paypers (2026-06-19) — MCP integration.
- AWS docs/blogs — Bedrock AgentCore Gateway, Guardrails PII filtering.
- Okta newsroom / MarkTechPost / Aembit — Auth0 "Auth for MCP" GA 2026-05-06, competitor landscape.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is it really new, or a reskin of AgentCore Guardrails?** AWS's own AgentCore Gateway (the launch platform) already applies PII filtering, content policy, and prompt-attack detection. Sumsub's genuinely additive piece is only the **liveness-escalation + human-binding**. → The PII-filtering/logging half is arguably redundant with the gateway it runs on. *Mostly answered: differentiator = liveness.*

2. **Any customers, pilots, or revenue?** None disclosed. Only "starting with Amazon Bedrock AgentCore Gateway." *Open — announcement, not adoption.*

3. **Why is the only quote from an "AI Advocate," not the CPO/CTO?** June's MCP launch had CPO Novoselsky; Jan's had CTO Zholudev. An evangelist byline signals a lower-tier positioning release. *Analysis — weight down.*

4. **Does a liveness check mid-agent-workflow kill the autonomy value prop?** The whole point of agents is unattended execution; forcing a human liveness check on high-value actions reintroduces the human. How often will clients actually enable it vs leave it off? *Open — likely edge-case only.*

5. **What stops AWS / Okta / Anthropic from absorbing liveness-escalation into the gateway/protocol?** If they do, Sumsub is disintermediated to an optional plugin. *Open — key downside trigger.*

6. **Are the threat stats real?** "65% of orgs had an agent-caused incident"; "OpenAI model breached Hugging Face in July." Unsourced in the PR. *Open — treat as marketing.*

7. **Is "model-agnostic / works with any MCP agent" true today?** No — live on exactly one gateway (AgentCore). The rest is roadmap. *Answered: overstated.*

8. **How does this monetize — per-check, seat, or platform fee?** Unknown. Liveness checks are Sumsub's billable unit in KYC; if priced per-escalation, low-frequency usage = low revenue. *Open.*

9. **Does Sumsub's liveness biometric actually bind to the RIGHT human, or just A human?** The claim is "a real, authorized human." Authorization mapping (which human may approve which action) is an IAM problem Okta/Auth0 own — does Sumsub integrate or reinvent it? *Open.*

10. **Is agent-to-human binding defensible IP or a framing?** Sumsub says it's "the only" one offering it; competitors (Descope, Aembit, SailPoint) govern agents but via tokens/scopes, not biometrics. Moat = biometric liveness, not the binding concept. *Partly answered.*

11. **What share of Sumsub revenue is this vs commoditizing core KYC?** KYA is a new line defending against take-rate compression in core verification. No revenue split disclosed. *Open — but strategic logic is sound.*

12. **Regulatory pull or vendor push?** Is any regulator requiring "human accountability for agent actions" yet, or is Sumsub pre-positioning ahead of the EU AI Act? *Open — mostly anticipatory.*

13. **Why launch on AWS first specifically?** AgentCore Gateway is the largest managed MCP gateway → fastest distribution, but also the platform most able to replicate the feature. Distribution vs disintermediation tradeoff. *Analysis.*

14. **Does this cannibalize or complement the June MCP integration?** June = agents operate Sumsub; Oct = Sumsub polices agents. Complementary, builds a two-sided KYA story. *Answered: complementary.*

15. **If the market consolidates to a protocol-level standard (MCP auth, Meta/Sierra Personal Agent Protocol), where does a point vendor sit?** Point solutions survive only if liveness stays a specialist buy-not-build capability. *Open — central question.*

**Importance: 3/5** — Genuinely differentiated capability (liveness-escalation on agent actions) from a credible incumbent extending a coherent year-long KYA strategy, and it rides the hottest 2026 regtech theme. But: zero disclosed traction, launched on a single gateway that already does half the job, marketing-tier quote, real disintermediation risk, and a UX-vs-autonomy tension that caps real-world usage. A solid strategic marker, not a market-moving product.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Sumsub sits at the intersection of two markets: identity verification / KYC-AML RegTech and the emerging "agent identity" / non-human identity (NHI) security layer. Sizing varies by scope: pure identity verification ~$15.8–16.5bn in 2026 at ~11% CAGR to the early 2030s; the broader "Digital Identity Verification & KYC/AML RegTech" bucket ~$28.0bn in 2026 → $98.6bn by 2034 at ~16.9% CAGR; standalone KYC ~$7.8bn in 2026 growing ~15.9% (per marketresearch.com/Stratistics, Grand View, Mordor, as of 2026 — all paywalled summaries, treat as order-of-magnitude). Structure: fragmented, with a cluster of well-funded scale players (Socure, Persona, Veriff, Jumio, Onfido, Trulioo) competing on accuracy, liveness/anti-deepfake, coverage (ID types/geographies) and increasingly on an orchestration/platform layer. Barriers: regulatory licensing + data-residency, document/biometric model training data, and enterprise compliance integrations (switching costs). Why now: the secular driver is a tech shift — autonomous AI agents requesting broad system access. Sumsub's own framing cites research that 65% of organizations had at least one agent-caused security incident in the past year (de-PR: vendor-cited stat, unverified) and a July 2026 incident where an OpenAI agent reportedly breached Hugging Face production systems. The second-order driver is that "Know Your Agent" (KYA) reframes identity vendors from one-time onboarding KYC toward continuous, runtime authorization of non-human actors — a larger, stickier surface.

**Competitive landscape.** Sector KPIs: verification volume (Socure processed >5bn identity verifications in 2025 vs 2.7bn in 2024), ARR and ARR growth, and accuracy/liveness pass rates. Basis of competition is shifting from pure IDV accuracy toward platform breadth (fraud + AML + orchestration) and now agent governance. Recent moves: Persona launched Persona Connect at Money20/20 (Oct 2025); Socure closed the Fravity-related growth round (Aug 2026); the NHI/agent-identity front is being contested from the IAM side — Okta's Oktane 2026 launched AI Agent Registration (Early Access) binding agents to human owners, GA targeted ~Apr 2026 (per Okta/Forrester/SiliconANGLE). Sumsub's position: niche-but-early-mover on the specific "verified human behind the agent" + PII-stripping/data-filtering angle (KYA Jan 2026 → MCP integration Jun 2026 → KYA Module for MCP now, starting with Amazon Bedrock AgentCore Gateway). Moat (analysis): its edge is combining liveness/KYC assets with agent-runtime policy — a bundle IAM incumbents (Okta) and pure IDV peers don't fully have yet; but the moat is narrow and the category is pre-standard (no universal KYA standard exists — per Forrester).

**Comps & multiples.** Sumsub is private; last disclosed round was a $30M raise in Dec 2022 at a ~$100–250M valuation (per PitchBook/Tracxn, 2022 — stale), total raised ~$38M. 2025 revenue estimates are a wide, unreliable range (£10–50M low-end vs a $1bn+ outlier), so no credible revenue multiple can be computed — **no data / [UNSOURCED]** on Sumsub's current valuation and ARR. Peer reference points (round valuations, not market caps):
- Socure — $5.2bn valuation (Aug 2026), $364M ARR (Jun 2026). Implied EV/ARR ≈ $5.2bn / $0.364bn ≈ **14.3x** (round-valuation proxy).
- Veriff — $1.5bn valuation (Jan 2022 Series C, stale), $110M ARR in 2025 (+83% YoY); on stale valuation ≈ **13.6x** — but the valuation predates the ARR, so treat as indicative only.
- Persona — $2.0bn valuation (Apr 2025, $200M Series D); ARR not disclosed → multiple **no data**.
- Jumio — ~$210M revenue (2024 est.); valuation not disclosed → **no data**.
Distribution not formally computed (only 2 roughly comparable valuation/ARR pairs, both caveated); qualitative read: well-funded IDV peers trade at low-double-digit EV/ARR on round valuations, consistent with ~11–17% sector growth. Sumsub, raising last in 2022 and far smaller by disclosed funding, looks under-capitalized relative to Socure/Persona/Veriff. Internal comps: [[Persona launches Persona Connect at Money20 20]], [[Trulioo posts 134% jump in US verification volume]], [[Veriffreports that about 4% of verification attempts in 2025 were fraudulent, and]], [[Socure and Docusign embed identity verification in signing]].

**Risk flags.**
1. Category-definition / standards risk — KYA is pre-standard (no universal framework; Forrester notes even Okta hasn't committed to one). A vendor-specific "KYA Module" can be stranded if the market standardizes around MCP-native or IAM-native controls (Okta/cloud gateways), disintermediating the specialized layer.
2. Competitive squeeze from both sides — IAM incumbents (Okta) pushing down into agent identity and better-capitalized IDV peers (Socure $5.2bn, Persona $2bn) pushing up into orchestration; Sumsub's last disclosed raise (2022, ~$38M total) suggests a capital disadvantage to defend a land-grab.
3. Dependence on others' rails — KYA Module launches on Amazon Bedrock AgentCore Gateway and MCP gateways; value accrues partly to the gateway/model layer (Claude, ChatGPT, Bedrock), and a platform owner building native PII-filtering/liveness could capture the margin.

**What this changes (idea-lens).** (analysis) This is an attempted category-expansion, not a re-rating event: Sumsub is trying to convert one-time KYC into continuous agent-runtime authorization — a larger, stickier TAM if "verified human behind the agent" becomes a compliance requirement. Falsifiable thesis: KYA-style human-accountability controls become a line item in enterprise agentic-AI rollouts within ~18–24 months. Trigger/catalyst to watch: regulator or large-platform (AWS/Anthropic/OpenAI) endorsement of a KYA-type standard, or a marquee enterprise deployment. What breaks the thesis: MCP/IAM platforms ship native agent-identity + data-filtering controls as a default, making standalone KYA modules redundant.

Sources: https://financialit.net/news/artificial-intelligence/sumsub-expands-know-your-agent-putting-businesses-control-what-ai · https://pitchbook.com/profiles/company/221537-80 · https://valueaddvc.com/blog/socure-valuation-2026-5-2b-364m-arr-and-the-fravity-acquisition-explained · https://sacra.com/c/veriff/ · https://fintech.global/2025/04/30/identity-verification-firm-persona-hits-2bn-valuation-following-200m-funding-round/ · https://www.marketresearch.com/Stratistics-Market-Research-Consulting-v4058/Digital-Identity-Verification-KYC-AML-45264823/ · https://www.grandviewresearch.com/industry-analysis/identity-verification-market-report · https://www.forrester.com/blogs/oktane-2026-recap-okta-announces-a-unified-iam-control-plane-with-agent-governance-and-identity-details-remaining-unclear/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
