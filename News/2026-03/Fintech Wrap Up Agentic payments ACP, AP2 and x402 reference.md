---
title: "Fintech Wrap Up: Agentic payments ACP, AP2 and x402 reference"
date: 2026-03-29
tags:
  - industry/agentic-commerce
  - industry/crypto
  - region/global
  - type/research-report
sources:
  - https://orium.com/blog/agentic-payments-acp-ap2-x402
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s39dfc9ff
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Agentic payments ACP, AP2 and x402 reference

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Agentic Payments Explained: ACP, AP2, and x402 | Orium, accessed March 22, 2026, https://orium.com/blog/agentic-payments-acp-ap2-x402

## Первоисточники

### orium.com
<https://orium.com/blog/agentic-payments-acp-ap2-x402>
*1165 слов · jina*

###### 2025-09-29

AI systems are evolving from assistants that respond to prompts into agents that take action. They book travel, manage subscriptions, and increasingly, spend money. For decades, web payments have relied on people filling out forms or tapping buttons to confirm transactions. But agents have no browser window and no fingers to click checkout. The familiar model of redirecting to a hosted payment page simply doesn’t work for agentic commerce at scale.

That gap is driving the emergence of a new generation of payment protocols designed specifically for machine-to-machine and agent-to-business commerce. These protocols define how an AI agent can securely authorize, execute, and record a payment on behalf of a user or an organization. The three most prominent initiatives today are the Agentic Commerce Protocol (ACP) from Stripe and OpenAI, Google’s Agent Payments Protocol (AP2), and x402 from Coinbase. Each comes from a different corner of the technology ecosystem, and each tackles a unique part of the same challenge.

For CIOs, this movement signals an early shift in how digital platforms will transact in an AI-driven economy. The decision isn’t about picking winners yet; it’s about understanding where these standards might intersect with existing systems and what governance will be required when software becomes a spender.

* * *

**_Orium is a launch partner for Stripe and OpenAI's ACP. Whether you need a high-level overview for leadership alignment or a deep-dive strategy session, we can help you understand where you stand today, what to prioritize, and how to compete with confidence in the agentic era. Request your 30-minute executive briefings and 1-day strategic intensives._**

* * *

## The Agentic Commerce Protocol (ACP)

ACP is an open standard developed by OpenAI and Stripe to make online checkouts agent-ready. It allows a business to define how an AI agent can initiate a purchase using the merchant’s existing commerce and payment infrastructure. The merchant remains the merchant of record, and transactions flow through established payment service providers like Stripe.

In practice, ACP creates a secure way for an agent to share credentials, initiate a checkout, and receive confirmation without exposing sensitive payment data. The model supports physical and digital goods, subscriptions, and asynchronous purchases. It also gives merchants the ability to apply custom approval logic, ensuring that transactions initiated by agents comply with their own risk and compliance policies.

ACP is already live within OpenAI’s ChatGPT Instant Checkout, where users can buy products directly inside the chat experience. It’s open source under Apache 2.0 licensing, designed to be adopted by any merchant, AI platform, or payment provider. While Stripe is the first implementation partner, the framework is intended to be platform-agnostic and extensible across the broader agentic commerce ecosystem.

## The Agent Payments Protocol (AP2)

AP2, led by Google, takes a complementary approach by focusing on the authorization and traceability layer of agentic payments. It establishes how agents, users, and payment providers communicate trust and consent. AP2 introduces the concept of mandates, digitally signed statements that define what an agent is allowed to do, such as create a cart, complete a purchase, or manage a subscription.

These mandates are portable, verifiable, and revocable, allowing multiple stakeholders to coordinate safely. A user can delegate spending authority to an agent, and that agent can then execute the payment through any compatible network or provider. The specification supports multiple rails including cards, real-time payments, and digital assets.

Google has released AP2 as an open protocol under Apache 2.0 license and has assembled more than sixty initial partners, including Mastercard, Adyen, PayPal, Coinbase, and major merchants. The protocol aims to create a shared foundation for agent-initiated payments across ecosystems. For CIOs, AP2 represents a potential standard for compliance, auditability, and multi-party governance in agentic transactions.

## x402 and the Web’s Payment Revival

x402, developed by Coinbase, addresses a different piece of the puzzle. It revives the long-unused HTTP 402 status code, “Payment Required,” to enable simple, programmatic payments on the web. Instead of creating accounts or API keys, a client can request a resource, receive a 402 response with payment details, submit payment on-chain, and retry the request to access the content or service.

The design is minimal, chain-agnostic, and especially suited for microtransactions and pay-per-use APIs. For example, a content API could charge a small fee for each request without requiring user registration. This makes x402 attractive for developers, data providers, and AI systems that need to pay for API calls, digital assets, or limited-use services without friction.

x402 does not attempt to handle the full commerce lifecycle or authorization semantics that ACP and AP2 address. Instead, it focuses on embedding payment directly into HTTP in a way that’s open, decentralized, and easy to integrate. The specification and SDKs are public on GitHub, and the first reference implementations use stablecoins like USDC.

## Comparing the Three Protocols

ACP, AP2, and x402 are not direct competitors so much as layers in an emerging agentic commerce stack. ACP focuses on the checkout and merchant integration layer. AP2 defines the trust and authorization model that could underpin transactions across ecosystems. x402 operates at the execution layer, enabling instant, programmable payments for data and APIs.

Their maturity levels also differ. ACP is already in production within ChatGPT’s checkout. AP2 has a broad coalition but remains early in adoption. x402 has working open-source implementations, though real-world usage is still limited to developer experiments.

For CIOs, the key questions are interoperability and timing. None of these protocols are mutually exclusive. A large enterprise might support ACP for agent-based shopping, adopt AP2 for internal governance and audit controls, and experiment with x402 for machine-to-machine data access. The real risk is ignoring them until they become embedded in platforms the enterprise already relies on.

## Implications for CIOs

The arrival of agentic payment standards hints at a broader shift in enterprise architecture. Systems that were once designed around human workflows will increasingly need to accommodate autonomous agents acting on behalf of employees or customers. Governance, risk management, and compliance will need to account for delegated authority, transaction traceability, and non-human user identities.

The right posture for most organizations in 2025 is selective experimentation. Evaluate ACP or AP2 integrations in sandbox environments. Monitor early merchant and PSP adoption to identify where standards are stabilizing. Use these tests to refine internal policies on AI delegation and spending limits. CIOs should also engage procurement and finance teams early to align on accountability when agents initiate transactions.

## Preparing for the Agentic Economy

History shows that standards quietly shape the future long before they become visible. The web’s early protocols built the foundation for modern APIs, cloud services, and digital identity. Agentic payments may play a similar role in enabling the next phase of AI-driven business.

For CIOs, understanding ACP, AP2, and x402 isn’t about betting on a winner. It’s about recognizing the architecture of what comes next. The organizations that experiment early will be better positioned to define how machines transact responsibly, securely, and in alignment with business goals.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
