---
title: "MDPI paper on payment rails in smart-contract-as-a-service"
date: 2026-06-14
tags:
  - industry/blockchain
  - industry/payments
  - region/global
  - type/research-report
sources:
  - https://www.mdpi.com/1999-5903/18/2/110
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sb74f5ee9
month: 2026-06
enriched: false
---

# MDPI paper on payment rails in smart-contract-as-a-service

> [!info] 2026-06-14 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Payment Rails in Smart Contract as a Service (SCaaS) Solutions from BPMN Models - MDPI, accessed May 10, 2026, https://www.mdpi.com/1999-5903/18/2/110

## Первоисточники

### mdpi.com
<https://www.mdpi.com/1999-5903/18/2/110>
*1865 слов · jina*

## 1. Introduction

Blockchains and their programmable smart contracts have gained significant interest due to their potential to automate agreements among distrusting parties without intermediaries, forming a cornerstone of Web3 ecosystems. Classic work on blockchain technology highlights both its trust guarantees and its challenges in real-world application domains involving multiple stakeholders and complex business logic. The development of robust, secure, and maintainable smart contracts remains a barrier to adoption, especially for business applications that include payment coordination across heterogeneous rails.

Writing smart contracts is difficult not only because of blockchain platform intricacies (e.g., gas, storage costs, and consensus), but also due to distributed coordination among participants—a longstanding challenge in distributed systems. For applications involving multiple actors, coordination, synchronization, and transactional guarantees increase development complexity significantly.

To reduce developer burden, the Model-Driven Engineering (MDE) paradigm has been applied whereby application requirements are first modeled at a high level of abstraction and then automatically transformed into executable artifacts. Early works used finite state machines (FSMs) to model contract logic (e.g., [1]) and Petri nets to capture concurrency and synchronization before contract synthesis. However, FSMs often lack the expressiveness needed for complex multi-actor processes, and Petri net models—though powerful—are not widely adopted by business practitioners due to their perceived complexity.

For this reason, many researchers have turned to Business Process Model and Notation (BPMN) for representing application requirements and control flow, because BPMN is understood by business analysts, managers, and software developers alike. BPMN naturally expresses conditional flows, parallelism, and collaboration, and it integrates with Decision Model and Notation (DMN) to capture business logic decisions (e.g., tariff choices, eligibility rules). DMN’s Friendly Enough Expression Language (FEEL) allows business logic to be expressed in a readable and structured form that can be transformed into target implementation code.

Despite these advances, payment integration remains a challenge: it is unreasonable to expect a business analyst (**BA**) to specify low-level payment implementation details in the target programming language (e.g., Solidity on Ethereum). Different trade applications may require disparate payment methods (bank rails, crypto tokens, escrow, cross-chain bridges), each with distinct semantics and compliance constraints. Furthermore, modern systems increasingly hybridize on-chain and off-chain components, demanding orchestration logic that ensures atomicity and correct sequencing across disparate execution contexts.

Across all payment categories, two properties are especially relevant to the BPMN-to-smart contract transformation problem:

1.
Semantic richness—Payments involve amounts, assets (currencies or tokens), participants, timing constraints, and compliance conditions, all of which must be respected by execution logic.

2.
Implementation diversity—The actual execution semantics vary widely depending on the payment rail (traditional banking, DeFi protocols, escrow logic, wrapped assets, or cross-chain protocols), even though BAs typically model payments as abstract tasks.

This motivates the central abstraction of the smart contract-as-a-service (SCaaS) approach to payment services: BAs model payments generically, while developers produce concrete payment smart contract services that can be pre-deployed and invoked by an automatically generated orchestration of process execution from BPMN models.

In our previous work, we established a foundation for the automated generation of smart contracts from BPMN models using multi-modal modeling, comprised of discrete event (DE) and hierarchical state machine (HSM) modeling and referred to as DE-HSM modeling, that is used to capture process semantics, participant interactions, and execution ordering. We subsequently extended this pipeline to support nested and multi-step transactions. More recently, we introduced TABS+R, a mechanism that enables the repair and upgrade of generated smart contracts when real-world conditions diverge from modeled assumptions by isolating the affected BPMN fragments, modifying them, and regenerating consistent contract logic [2].

A key benefit of DE-HSM modeling within the SCaaS framework is its explicit separation of concerns. Collaborative interactions among participants, such as task sequencing and message exchanges, are modeled using discrete-event (DE) semantics, while the internal functionality of BPMN task elements is represented using Hierarchical State Machines (HSMs). Decision points in BPMN models are represented by gateways whose conditions are typically expressed as relatively simple Boolean expressions. These expressions, such as checking whether a payment amount exceeds a threshold value, can be naturally specified by BAs using DMN and FEEL, which are designed to be accessible to both technical and non-technical stakeholders.

Our modeling approach supports a clear division of responsibilities: BAs focus on modeling trade activities and decision logic, while developers provide specialized services when the functionality of a BPMN task exceeds the BA’s scope—most notably in the case of payment execution. However, existing BPMN-to-smart contract transformation approaches do not provide a systematic mechanism for abstracting payment rails, separating payment implementation from process logic, or reusing pre-deployed payment services across multiple trade applications.

### 1.1. Objectives

The focus of our project is to simplify the creation of smart contracts for blockchain applications that support the trade of goods and services. Our primary objective is to automate smart contract generation by allowing business analysts (BAs) to model trade workflows in BPMN, while software developers implement code for BPMN task elements as methods with well-defined inputs, outputs, and objectives.

The transformation process automatically synchronizes process flows and message exchanges among system components using DE-FSM modeling. This approach enables developers to focus on well-defined tasks without managing complex process synchronization, reducing errors and developer effort. It also supports a clear separation of concerns between BAs and developers, simplifying collaboration.

Within the context of generating smart contract-as-a-service solutions from BPMN models and the separation of concerns between the roles of the BAs and developers, this paper aims to:

*   Enable software developers to prepare specific smart-contract payment services in advance, targeting various payment rails (on-chain crypto, off-chain bank transfers, cross-chain rails).

*   Allow business analysts to model trade activities for goods and services in BPMN models while allowing them to use generic representation of payment services without requiring knowledge of payment implementation details.

*   Design a transformation process that identifies generic payment tasks in a BA’s BPMN model, matches them to concrete payment services via a BPMN fragment repository, augments the BPMN model accordingly, and generates a smart contract that orchestrates the trade activity while invoking the appropriate payment services.

The scope of the paper concerns how smart contract payment services can be prepared and deployed while minimizing the development effort, rather than the efficiency of the produced software. Reducing the time required for a BA or a developer is more cost-effective than minimizing the execution delays of a smart contract method, unless that smart contract method is executed many times. The execution delays of a smart contract payment method depend on the method’s efficiency and on the efficiency of the underlying infrastructure that executes the method. As the smart contract methods of a payment service are prepared by a software developer, the efficiency of those methods depends on the skill of the software developer and the underlying blockchain. Consequently, the efficiency of the payment services methods prepared by a software developer are outside scope of this paper.

### 1.2. Contributions

This paper extends the capabilities of our TABS+R system and makes the following contributions:

*   Separation of concerns between trade-activity modeling and payment implementation, allowing BAs and developers to work independently at appropriate abstraction levels.

*   Repository-mediated transformation of generic payment tasks, enabling BPMN payment elements prepared by BAs to be mapped to instantiated and deployed payment services prepared by developers.

*   Multi-rail payment support for heterogeneous payment scenarios, including on-chain native payments, third-party cross-chain stablecoin payments, and off-chain conventional banking transfers.

*   Reuse and composition of patterns for extensibility of payment services, enabling the same payment services to be leveraged across multiple trade applications.

*   Shared state management across participants to facilitate sophisticated multi-party settlement patterns.

*   Cross-platform payment service invocation, supporting interaction with heterogeneous blockchain and off-chain systems.

*   Incremental ecosystem growth, allowing new payment services to be added to the repository without disrupting existing applications.

At the end of Section 3 and Section 4, we summarize which of the objectives were reached, while in the last section we review the contributions listed above while also summarizing how they were achieved.

### 1.3. Outline

The remainder of this paper is organized as follows. Section 2 provides a background on conventional and crypto-payment methods, introduces BPMN and DMN modeling and their use in transformation pipelines, and overviews our SCaaS approach from BPMN and DMN models. Section 3 presents our approach to integrating payment services into SCaaS workflows, including repository design and smart contract generation, illustrated through a representative use case covering on-chain, off-chain, and cross-chain payments. Section 4 discusses reuse and extensibility by presenting an additional use case of creating a payment service that utilizes payments with settlement netting while reusing other, already existing, payment services and by showing how the repository supports the integration of services. Section 5 reviews related work, situating our contributions relative to existing BPMN-to-smart contract transformation research. Finally, Section 6 provides a summary, the contributions, and the conclusions with the direction of future work.

## 2. Background

This section surveys the foundational concepts underlying the generation of smart contracts from business process models and motivates the smart contract-as-a-service (SCaaS) paradigm with explicit support for payment rail abstraction. We first characterize payment methods across conventional and blockchain-based ecosystems, then introduce BPMN and DMN as modeling standards for business processes and decisions and finally review our approach to transforming BPMN models into executable smart contracts.

### 2.1. Payment Methods in Conventional and Blockchain Ecosystems

Payments represent the transfer of economic value between parties and differ substantially in semantics, execution guarantees, and compliance obligations depending on the underlying rail. These differences are especially relevant when payment logic is orchestrated by smart contracts generated from abstract process models.

#### 2.1.1. Conventional (Off-Chain) Payments

Conventional payment systems operate over established financial infrastructures such as Automated Clearing House (ACH) transfers, wire payments, card networks, real-time gross settlement (RTGS) systems, and correspondent banking arrangements. These rails rely on intermediaries, including banks, clearing houses, and payment processors, to execute settlement, manage liquidity, and enforce regulatory requirements such as anti-money laundering (AML) and know-your-customer (KYC) checks. Payment instructions and confirmations are commonly exchanged using standardized messaging frameworks, notably SWIFT MT and MX formats [3,4].

Settlement in conventional systems is typically irreversible once completed, and dispute resolution is handled through institutional or legal processes external to the execution infrastructure. While compliance rules and exception-handling logic can be encoded in smart contracts, the determination of compliance and exception conditions typically depends on off-chain data, institutional authority, and human judgment. As a result, compliance evaluation and exception recognition cannot be performed natively on-chain and must be delegated to external services or oracles when integrating conventional payment rails with smart contracts [5].

#### 2.1.2. Blockchain-Based Payments

Blockchain-based payment mechanisms enable programmable value transfer on distributed ledgers. These mechanisms can be classified based on ledger locality and the nature of inter-ledger interaction.

##### On-Mainchain Payments

On-mainchain payments occur when both the requesting smart contract and the payment execution logic reside on the same blockchain. Transfers of native cryptocurrencies or tokenized assets are atomic, transparent, and self-verifying due to blockchain consensus. Such payments support advanced features such as conditional transfers, escrow, and bulk payments with netting, all enforced directly by smart contract logic [6,7]. Regulatory compliance is typically layered via external oracles or application-level controls.

##### Cross-Chain Native Payments

Cross-chain native payments transfe

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
