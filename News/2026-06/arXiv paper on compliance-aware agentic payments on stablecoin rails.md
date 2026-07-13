---
title: "arXiv paper on compliance-aware agentic payments on stablecoin rails"
date: 2026-06-14
tags:
  - industry/stablecoins
  - industry/agentic-commerce
  - region/global
  - type/research-report
sources:
  - https://arxiv.org/html/2605.00071v1
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sa72b2006
month: 2026-06
enriched: false
---

# arXiv paper on compliance-aware agentic payments on stablecoin rails

> [!info] 2026-06-14 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Compliance-Aware Agentic Payments on Stablecoin Rails - arXiv, accessed May 10, 2026, https://arxiv.org/html/2605.00071v1

## Первоисточники

### arxiv.org
<https://arxiv.org/html/2605.00071v1>
*1909 слов · direct*

Compliance-Aware Agentic Payments on Stablecoin Rails
Agentic payment systems extend delegated action to financial transfers, but scaling them on stablecoin rails in regulated settings requires safeguards that remain effective when humans are not continuously in the loop. We present a compliance-aware architecture that combines x402-style, signature-based payment authorisation and relayed execution with programmable compliance embedded as an on-chain guardrail via a policy wrapper and policy manager coordinating modular checks. By enforcing compliance at the point of execution, rather than as a separate off-chain workflow, the approach preserves low-friction settlement when conditions are satisfied, records transaction-linked on-chain attestations, and supports structured resolution when requirements are pending.

 1 Introduction
The past several years have witnessed the emergence of what is increasingly termed agentic artificial intelligence (AI), where systems are able to plan, reason, and execute multi-step actions rather than merely respond to isolated prompts. While such systems remain far from fully mature, recent industry evidence suggests a rapid rise in experimentation and early deployment. A global survey reports that more than one-third of organizations have already implemented agentic AI systems in some form, with a further large share actively planning adoption Ransbotham et al. ( 2025 ) . This accelerating interest is beginning to extend beyond productivity support toward delegated action in digital markets and financial operations. In emerging “agentic commerce” journeys, agents can search for products, negotiate terms, and execute purchases on behalf of users, while related exploratory work highlights their potential to support real-time treasury and cashflow decision processes in payment systems, together suggesting opportunities to improve conversion and reduce operational overhead for merchants and financial operators Visa ( 2025 ); Aldasoro and Desai ( 2025 ) . Together, these developments motivate growing interest in agentic payments, where machines initiate and complete value transfers under user-specified constraints and at the speed and granularity expected of modern digital services.
However, scaling agentic payments requires confronting distinct risks introduced by autonomy, delegation, and multi-step tool use. First, agents can drift into technological paternalism, subtly substituting the agent’s optimization for the user’s autonomy, especially in decision support contexts where “helpfulness” is ill-defined Mihale-Wilson ( 2025 ) . Second, agents are vulnerable to manipulation and hijacking in environments that contain untrusted content or tools. Surveyed threat classes include prompt and tool injection, environment tampering, and exfiltration pathways that can induce agents to reveal sensitive information or execute unintended actions Deng et al. ( 2025 ) . Third, even without adversaries, autonomy can lead to actions that deviate from a user’s intent due to goal mis-specification, context loss, or brittle orchestration across tools and APIs Leo et al. ( 2026 ) . Consequently, responsible adoption requires safeguards that support governance, transparency, and regulation in ways that remain effective even when humans are not continuously in the loop Murugesan ( 2025 ) .
A second trend relevant to agentic payments is the growing adoption of stablecoins. Stablecoins are digital tokens designed to maintain a relatively stable value, typically through linkage to a fiat currency or reserve assets, and are commonly issued and transferred on blockchain networks that support smart contracts and programmable settlement Higginson and Spanz ( 2025 ) . For certain payment flows, stablecoins can offer faster settlement, broader availability across borders and time zones, and potentially lower operational friction than legacy rails, especially where intermediated reconciliation and batch settlement dominate Higginson and Spanz ( 2025 ) . These properties make stablecoins a plausible substrate for agentic payments, where agents may need to transact frequently, automatically, and in near real time Reppel et al. ( 2025 ) .
Yet, payments remain a highly regulated activity, and compliance does not disappear simply because payment rails change. Conventional requirements include sanctions screening, customer due diligence controls, recordkeeping, and information-sharing obligations such as the FATF “travel rule” (Recommendation 16) as applied to virtual assets and VASPs Financial Action Task Force ( 2023 ) . Regulators also emphasize that faster or instant payment schemes can intensify sanctions-compliance challenges by compressing the time available to interdict prohibited transfers, and therefore should incorporate sanctions controls by design U.S. Office of Foreign Assets Control ( 2022 ) . More broadly, introducing distributed ledger infrastructure can reconfigure how trust is preserved and evidenced across participants, but it does not eliminate the need to demonstrate compliance and accountability See and Li ( 2025 ) . If compliance remains primarily manual, slow, or externally mediated, the purported benefits of real-time agentic payments and stablecoin-based settlement are unlikely to materialize at scale.
This motivates interest in programmable compliance, which leverages smart-contract affordances to encode compliance requirements as enforceable conditions for transfers. Prior work has highlighted how “conditional payments” and policies attached to money or transfers can be represented and enforced on-chain Weber and Staples ( 2022 ) . In practice, multiple industry efforts are converging on architectures for regulated digital assets that embed identity, permissions, and policy checks into token transfer logic or associated rails, including permissioned token standards (e.g., ERC-3643) Lebrun et al. ( 2023 ) , payment-token design proposals for safety and integrity Toh et al. ( 2025 ) , and emerging reference architectures for programmable compliance that distinguish non-interactive checks from interactive, evidence-producing workflows Global Layer One ( 2025 ) . Complementarily, x402 proposes an HTTP-native payment flow that allows software clients, including agents, to programmatically pay for services using stablecoins, commonly leveraging EIP-3009 transferWithAuthorization to support relayed execution via signatures Kim et al. ( 2020 ); Reppel et al. ( 2025 ) .
In this paper, we demonstrate how programmable compliance integrated into stablecoin payment rails can support agentic payment systems that are both seamless and regulated. Concretely, we demonstrate an agentic workflow in which a compliance mediator coordinates buyer and seller agents, executes on-chain policy evaluation, and supports interactive resolution when evidence (e.g., source-of-funds attestation) is missing. The design preserves a machine-native execution path for transfers while preventing unauthorized or non-compliant settlement, thereby reducing compliance-related friction that would otherwise block real-time agentic payments. Our results provide a practical pathway for scaling agentic payments by making regulatory safeguards enforceable, inspectable, and automatable, without requiring the user experience to revert to manual, out-of-band compliance checks.

 2 Architecture and Implementation
Our system is a modular, hybrid architecture that couples agentic decision-making with deterministic on-chain enforcement (Figure  1 ). We assume a simple commerce transaction in which a buyer agent expresses purchase intent, a seller agent provides inventory and pricing, and a compliance agent mediates payment execution under a programmable compliance regime 2 2 2 Implementation code can be found at https://github.com/Chen-XueWen/agentic_compliance_payment .
At a high level, the system comprises (i) a lightweight user interface for issuing intents and observing execution, (ii) an agent orchestration layer that coordinates the buyer, seller, and compliance agents, and (iii) an on-chain enforcement layer realized through the Global Layer One (GL1) Programmable Compliance architecture. The agents interact with the on-chain layer via an x402-style gateway: the buyer produces a signed payment authorization, and the compliance agent compiles and submits the corresponding payment instruction to the GL1 policy wrapper for evaluation and settlement.
Compliance outcomes are returned as transaction-linked attestations ( PASS / FAIL / PENDING ). When checks pass, settlement proceeds immediately; when requirements are pending, the compliance agent can negotiate a structured alternative (e.g., staged settlement) and complete payment once the required evidence is provided. This design embeds compliance as a guardrail at the point of execution, avoiding the need to treat agentic workflows and payment compliance as separate, friction-inducing processes.

 3 Demo
In the absence of programmable compliance safeguards, naïve agentic payment flows can lead to ethically and institutionally problematic outcomes. Transactions may settle despite violating regulatory constraints, exposing counterparties to compliance risk, while informal, off-chain compliance handling can incentivize excessive disclosure of identity data, undermining privacy and data-minimization principles Salmon et al. ( 2025 ) . These risks illustrate how unstructured agentic payments can erode both regulatory trust and user autonomy.
The following subsections present two demo scenarios that illustrate how embedding programmable compliance into the payment substrate reshapes these flows. The first scenario shows a compliance-aware payment that settles immediately when regulatory conditions are satisfied, while the second demonstrates how pending compliance requirements are surfaced and resolved through agent-mediated tranching and escrow.

 3.1 Scenario I: Compliance-Aware Agentic Payment Flow
This scenario illustrates a compliance-aware agentic payment in which regulatory requirements are already satisfied, allowing settlement to proceed seamlessly while producing on-chain compliance attestations. The buyer agent initiates the transaction by generating a signed payment authorization, which is submitted on-chain by a compliance agent acting as a mediator. Rather than executing a direct transfer, the authorization is routed through the PolicyWrapper , which serves as the x402-compatible entry point to the programmable compliance framework.
The PolicyWrapper evaluates the transaction against the relevant sanctions and source-of-funds policies. In this case, all policy checks return a PASS result, triggering immediate settlement without additional interaction or delay (Figure  2 ). A compliance attestation linked to a unique transaction identifier is recorded on-chain, together with updated account balances, demonstrating how compliance enforcement can be embedded into agentic payment flows without introducing additional friction.

 3.2 Scenario II: Pending Compliance and Escrow-Mediated Settlement
This scenario demonstrates how the system handles transactions that cannot be immediately approved. When a payment exceeds the source-of-funds threshold, on-chain policy evaluation returns a PENDING result. No funds are settled; instead, a compliance attestation is recorded on-chain indicating that additional evidence is required.
The compliance agent retrieves the pending result and proposes an alternative arrangement in which the payment is split into two tranches (Figure  3 ). An initial tranche that satisfies existing conditions is settled, while the remaining amount is locked in an escrow contract pending resolution. The buyer subsequently submits a source-of-funds attestation, which is recorded on-chain and linked to the buyer’s identity. Once the requirement is satisfied, the compliance agent releases the escrowed funds, completing settlement. This scenario highlights how incomplete compliance conditions can be resolved through agent-mediated workflows without reverting to manual or off-chain intervention.

 4 Conclusion
We present an agentic payment system that integrates programmable compliance directly into stablecoin payment rails, demonstrating how regulatory safeguards can be enforced without undermining the seamless execution expected of agentic systems. Through compliance-aware and escrow-mediated scenarios, we showed how on-chain policy evaluation enables immediate settlement when requirements are satisfied, while supporting structured resolution when regulatory conditions remain pending. By embedding compliance logic into the payment substrate and aligning it with x402-style authorization flows, our approach illustrates a practical pathway to realizing the benefits of agentic payments—automation, speed, and machine-native interaction—while preserving regulatory trust and minimizing friction.
Contribution Statement
All authors contributed equally to the conception, design, analysis, and writing of this paper.
References

 I. Aldasoro and A. Desai (2025) 
 AI agents for cash management in payment systems .
 
 BIS Working Papers 
 
 Technical Report 1310 , Bank for International Settlements .
 
 External Links: Link 
 
 Cited by: §1 .
 


 Z. Deng, Y. Guo, C. Han, W. Ma, J. Xiong, S. Wen, and Y. Xiang (2025) 
 AI agents under threat: a survey of key security challenges and future pathways .
 
 ACM Computing Surveys .
 
 External Links: Document ,
 Link 
 
 Cited by: §1 .
 


 Financial Action Task Force (2023) 
 Virtual assets: targeted update on implementation of the FATF standards on virtual assets and virtual asset service providers .
 
 Report 
 
 External Links: Link 
 
 Cited by: §1 .
 


 Global Layer One (2025) 
 Programmable compliance toolkit .
 
 Note: Online Documentationhttps://doc.global-layer-one.org, Accessed 2026-01-27 
 
 External Links: Link 
 
 Cited by: §1 .
 


 M. Higginson and G.

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
