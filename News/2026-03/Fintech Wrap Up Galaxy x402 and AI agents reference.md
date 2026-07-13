---
title: "Fintech Wrap Up: Galaxy x402 and AI agents reference"
date: 2026-03-29
tags:
  - company/galaxy
  - industry/agentic-commerce
  - industry/crypto
  - region/global
  - type/research-report
sources:
  - https://www.galaxy.com/insights/research/x402-ai-agents-crypto-payments
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s0159a99e
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Galaxy x402 and AI agents reference

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Agentic Payments: x402 and AI Agents in the AI Economy - Galaxy, accessed March 22, 2026, https://www.galaxy.com/insights/research/x402-ai-agents-crypto-payments

## Первоисточники

### galaxy.com
<https://www.galaxy.com/insights/research/x402-ai-agents-crypto-payments>
*2060 слов · jina*

## Introduction

AI agents promise to transform the internet landscape. Already, continuous improvements in artificial intelligence have enabled agents to serve as coding assistants, shopping concierges, planning tools, and all other manner of subject-matter experts. They represent a powerful new primitive for how humans interact with the internet, mainly because they remove much of the need for humans themselves to directly engage with browsers and search engines.

In Galaxy Research’s 2024 report, _Understanding the Intersection of Crypto and AI_, we identified agents as one of the most promising growth verticals, noting that they are “well suited for crypto where users (or agents themselves) can create wallets for transacting with other services, agents, or people.” At the time, the agent space was nascent – limited by the intelligence of the underlying AI models, the infrastructure that enabled them to perform complex tasks, and the regulatory clarity needed for adoption beyond Web3-native contexts.

In just over a year since then, the progress on all three of the fronts has been astounding:

*   AI intelligence has progressed rapidly, enabling agents to “reason” over long horizons and autonomously execute complex tasks with increasing reliability.

*   Agent tooling has taken a leap forward with the release of foundational primitives including the Model Context Protocol (MCP), Agent-to-Agent (A2A) Protocol, Agent Payments Protocol (AP2), and the x402 standard.

*   Regulatory clarity, especially on the stablecoin front, has accelerated the integration of crypto payment rails.

Together, these developments have opened the door for the mass adoption of AI agents that leverage blockchain-based payments. One of the most promising advancements driving this trend is the emergence of x402 and related payment standards, which allow agents to pay for services and data directly using stablecoins or other crypto assets. For simplicity, we refer to this family of protocols collectively as agentic payment standards (APS) throughout this paper.

Simply put, APS give agents access to the internet’s full economic surface area. They can become smarter (by ingesting external data), more capable (by paying for resources), and more collaborative (by transacting with other agents). Beyond functionality, APS act as a bridge between the onchain and offchain economies, allowing any business to sell to the fastest emerging class of internet users – namely, agents – and accelerating the adoption of stablecoins for payments. APS also have the potential to improve the capital efficiency of an otherwise ignored economic engine by refactoring the business model for application programming interfaces (APIs, the standardized ways software requests data or services). Beyond economics, APS also bring forward fundamental changes to programming UX with respect to API key management. These changes make developing new applications easier.

This paper examines x402, one of the leading emerging onchain agentic payment standards. We situate x402 within the broader APS landscape and discuss its early adoption, use cases, and the tailwinds and headwinds that will determine whether blockchains can serve as the financial backbone of the emerging agentic economy.

## The x402 Standard

### Background

In May, Coinbase launched the x402 standard, a protocol that uses HTTP, the basic language servers use to communicate with each other, to enable crypto transactions in web interactions. Whereas previously transacting on the web depended on traditional payment rails (Visa, Mastercard, etc.), x402 opens the door for agentic payments that can access digital services using stablecoins and crypto.

x402 refers to a status code, “HTTP 402 Payment Required,” that was included in the original specification (spec) for the internet web protocol. Despite its inclusion at the onset of HTTP, 402 has largely sat dormant due to a lack of supporting infrastructure. Instead, a complementary payments infrastructure emerged, built by companies like Paypal and Stripe and reliant on traditional payment rails. While this infrastructure enabled the growth of e-commerce and significantly reduced payment frictions, it sat outside the inherent network capabilities of the internet.

_Source: x402 Whitepaper_

The key unlock from x402 is that it is now much simpler for anyone (human or agent) to pay for online services. The standard aims to “enable value to move across the internet as seamlessly as information, whether the actor is a human, an app, or an agent,” according to the team that developed it. This is most frequently exemplified through the streamlining of API requests. As Coinbase’s own teams have succinctly put it, “Let’s kill the API key.”

### Payment Flows

The payment flow for x402 is simple to understand. There are four primary components:

*   Client: The agent (or user’s software) that initiates the service request.

*   Server: The service provider that returns a 402 request and eventually delivers the paid resource.

*   Facilitator: Executes and/or verifies the payment.

*   Blockchain: The settlement layer where the actual stablecoin/crypto transfer happens.

_Source: x402 Whitepaper_

Agents send a request to a server for some product or service (say, a streaming subscription or an ebook), which returns a “payment required” request (HTTP 402). This request includes fields such as the amount required, types of tokens accepted, wallet address to send the payment to, and blockchain to pay on.

_Fields required for a 402 payment_

The agent then responds to the payment request with all the required information and a cryptographic signature authorizing the payment. Finally, a facilitator handles the actual payment for the service on the blockchain and confirms it to the server, which then returns the requested service to the agent.

This is the standard payment flow that has been adopted with x402, but many different modifications are possible. For example, if an agent controls a wallet itself and can transact on a blockchain, it can submit the payment and verification to the server directly without relying on a facilitator. To date, however, facilitators have been used because they simplify the process by abstracting away the complexity of blockchain interactions like wallet management, gas payments, and network selection. In this respect, facilitators resemble traditional payment service providers, except at no point do they custody the funds or control the private keys of the wallet involved in the transaction. Instead, the agent, which controls the wallet, authorizes the _what_(“send up to X dollars from the payer to payee’s wallet”) and leaves the _how_(which chain, how much gas, etc.) to the facilitator.

### x402 V2

On Dec. 11, Coinbase released x402 V2, a major upgrade based on feedback received over the past six months of usage. V2 begins the transition of x402 from a relatively simple but effective agentic payment specification into a more modular standard designed to adapt to evolving blockchain environments and support a broader range of payment use cases.

At a high level, x402 V2 expands the protocol along three key dimensions. First, it introduces a unified payment interface that supports multiple blockchains and assets through a single format, while enabling integration with legacy payment rails via facilitators. Second, it adds wallet-based identity and reusable access sessions, allowing clients to avoid repeated onchain interactions for subsequent requests—reducing latency and enabling higher-frequency use cases. Third, it enables automatic service discovery, allowing facilitators to index endpoints, pricing, and routing information without manual configuration.

Together, these changes allow x402 to support more sophisticated commercial models, including subscriptions, prepaid access, usage-based billing, and multi-step agent workflows.

## The x402 Agentic Payment Stack

Increasingly, the x402 stack is starting to take shape. The pace at which projects and infrastructure are launching is exponential, but we have tried our best to capture as many projects as possible below.

_All third-party logos are for identification purposes only and are property of their respective owners. Use of these logos and brands does not imply endorsement._

Value flow in the x402 payment stack begins at the agent layer and moves downward through coordination, execution, and settlement before propagating back up as fulfilled service access.

First, an agent or application initiates a task that requires access to a paid service, such as querying an API, retrieving proprietary data, or invoking another agent. The agent determines what it needs and under what _constraints_, including price, latency, preferred chain, or budget.

The coordination layer shapes how agents broadcast intents, discover services, exchange _context_(relevant information needed to complete a task), and coordinate workflows before payment occurs. It embeds additional functionality into agent workflows beyond what payment and settlement protocols alone provide, including mechanisms for service discovery, intent signaling, constraint enforcement (rules or limits such as budget, timing, or permissions), context management, and multi-step or multi-agent coordination.

Once terms are established, the agent initiates payment through the facilitation layer. Facilitators (services operated by third-party providers) handle routing, verification, and execution of the transaction, abstracting away blockchain-specific complexity and, when necessary, interfacing with legacy payment rails.

The currency layer defines what is transferred—typically stablecoins—enabling predictable pricing and programmable settlement suitable for high-frequency, machine-native transactions. USDC has been the dominant form of payment to date, but in theory any crypto can be used.

Finally, the blockchain layer executes and finalizes the transaction, providing cryptographic settlement and an auditable record. Confirmation then propagates back up the stack, allowing the service provider to deliver the requested resource to the agent.

### Emerging Crypto Use Cases

As previously covered by Galaxy Research (here and here), x402 activity had an initial surge in activity in late October and early November after which activity has tapered off.

As is often the case when primitives are introduced in crypto, initial adoption and interest were primarily driven by speculative activities, with the late October spike caused by teams using x402 to mint and purchase memecoins. Since then, however, transaction volume and counts for agent-to-agent services, data as a service, and infrastructure and utilities have begun to account for an increasingly large percentage of transaction market share.

This has been the nature of permissionless offerings within crypto. Initial speculative use cases attract users, which then attract developers, who then begin to experiment with the technology and build beyond speculative use cases. Indeed, filtering across all transactions and volume for gaming (defined by Artemis Analytics as apparent self-dealing or wash trading) shows a drop below 50% since early December.

The most compelling use cases, and those most likely to persist over time, are those that leverage x402 to offer a differentiated product relative to what is possible with legacy payment rails. This primarily includes offerings that would otherwise be cost-prohibitive on traditional rails due to transaction fees, as well as use cases that require internet-native money where legacy systems are constrained by limited programmability, slow settlement times, and reliance on non-native intermediaries.

Today, these offerings are dominated by service providers enabling one-off API calls that would otherwise require subscriptions. Trading agents, for example, can pay for individual API calls to blockchain data provider Nansen or AI analysts to supplement their crypto analysis when needed. Beyond data access, x402 also enables agents to pay programmatically for infrastructure services—such as compute—that are difficult to price or automate using subscription-based or human-mediated payment models. Nous Research, a leading decentralized AI lab, has enabled x402 payments for access to its Hermes 4 model. x402 onchain activity and early use cases have been covered extensively elsewhere, and interested readers can refer to this recent piece by Lucas Shin of Artemis for additional detail.

While promising, these examples largely remain speculative proofs of concept that demonstrate the infrastructure’s capabilities rather than the growth drivers required for x402 adoption at scale. This is not meant to discredit any individual project or its potential, but rather to acknowledge that most onchain product offerings still primarily target crypto-native audiences and represent only a subset of potential applications. The following section explores additional use cases and the broader conditions required for agentic payment standards to scale.

### Context and Data Access

One of the most compelling non-crypto use cases for agentic payment standards is paid access to online context and data. As AI agents increasingly rely on external information to perform tasks, the ability to programmatically purchase access to content on a per-request basis becomes critical.

Cloudflare provides an early example of how this model may emerge. As a major infrastructure provider that hosts and secures a significant portion of the internet, Cloudflare already mediates interactions between websites and automated traffic. In 2024, it introduced Pay-per-Crawl, a mechanism that allows bots and crawlers to pay for access rather than being blocked outright. Cloudflare has since indicated plans to integrate this infrastructure with x402 (the company partnered with Coinbase to launch the x402 Foundation), enabl

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
