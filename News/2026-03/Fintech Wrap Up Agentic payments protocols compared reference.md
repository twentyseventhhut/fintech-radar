---
title: "Fintech Wrap Up: Agentic payments protocols compared reference"
date: 2026-03-29
tags:
  - company/crossmint
  - industry/agentic-commerce
  - industry/payments
  - region/global
  - type/research-report
sources:
  - https://www.crossmint.com/learn/agentic-payments-protocols-compared
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sae1e7198
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Agentic payments protocols compared reference

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Agentic payments protocols compared: Which is best for your AI agents? (ACP vs AP2 vs x402) - Crossmint, accessed March 22, 2026, https://www.crossmint.com/learn/agentic-payments-protocols-compared

## Первоисточники

### crossmint.com
<https://www.crossmint.com/learn/agentic-payments-protocols-compared>
*1983 слов · direct*

Agentic payments protocols compared: Which is best for your AI agents? (MPP, ACP, AP2, x402)
Key takeaways
ACP (Agentic Commerce Protocol), co-developed by OpenAI and Stripe, standardizes checkout flows between AI agents and merchants - first deployed in ChatGPT's Instant Checkout, now evolving toward an app-based model with Shopify and PayPal integration.
AP2 (Agent Payments Protocol), developed by Google with 60+ partners, defines the trust and authorization layer for agent-led payments using cryptographically signed mandates - supporting both traditional card payments and crypto via its x402 extension.
x402, created by Coinbase, enables instant stablecoin payments over HTTP by reviving the 402 status code - purpose-built for machine-to-machine microtransactions and API monetization.
MPP (Machine Payments Protocol), co-developed by Stripe and Tempo, launched March 18, 2026 with a "sessions" model that lets agents pre-authorize a spending limit and stream micropayments in both stablecoins and fiat.
 Crossmint provides agent payments and wallets through a single API surface so agentic products and platforms can easily support every AI payment protocol and agentic commerce infrastructure as the landscape evolves.
Introduction
You're building AI agents that need to transact in the real world. Maybe your agents are purchasing cloud resources on behalf of users, paying for API calls from other agents, or completing e-commerce checkouts autonomously. You need a payment layer that works for machines and not just humans.
Three protocols have emerged to solve this problem, each backed by a major tech company: ACP from OpenAI and Stripe, AP2 from Google, and x402 from Coinbase. They approach agent payments from different angles. Checkout flows, authorization frameworks, and on-chain settlement. They're more complementary than competitive. But choosing which to support (and how to integrate them) is a real engineering decision with long-term consequences.
This guide compares all three on architecture, use cases, and production readiness. We'll also show you why teams building agentic products are choosing Crossmint for agent payments and wallets.
What is ACP (Agentic Commerce Protocol)?
 ACP is an open-source specification co-developed by OpenAI and Stripe, first released in September 2025 under the Apache 2.0 license. It defines how AI agents interact with merchants to complete purchases through four RESTful endpoints: Create Checkout, Update Checkout, Complete Checkout, and Cancel Checkout. Payment is handled via SharedPaymentTokens - single-use, time-bound, amount-restricted tokens that give users control while letting agents transact programmatically.
ACP's first major deployment was OpenAI's Instant Checkout in ChatGPT, which launched in February 2026 with US Etsy sellers. However, OpenAI scaled back in-chat purchasing in early March 2026, shifting toward an app-based model. The protocol remains an open standard with support from Stripe, Salesforce, Shopify, and PayPal (which is building its own ACP server). The pivot highlights that ACP's long-term value is as an open protocol for agent-merchant communication, not a single-platform feature.
ACP's strength is standardizing how agents interact with merchant catalogs and checkout flows. The trade-off is that it's designed for human-present commerce. It doesn't natively address machine-to-machine payments, micropayments, or stablecoin-native settlement.
What is AP2 (Agent Payments Protocol)?
 AP2 is an open protocol developed by Google with more than 60 organizations, including Adyen, American Express, Mastercard, PayPal, Coinbase, Revolut, and Worldpay. It works as an extension of Google's Agent2Agent (A2A) protocol and the Model Context Protocol (MCP).
AP2 solves the trust and authorization problem for agent payments. Its core mechanism is the Mandate - a tamper-proof, cryptographically signed (ECDSA) JSON-LD object that serves as verifiable proof of a user's payment instructions. AP2 defines three mandate types: Intent Mandates (conditions under which an agent can purchase), Cart Mandates (explicit user authorization for specific items and prices), and Payment Mandates (shared with payment networks to signal agent involvement).
AP2 supports two transaction modes: real-time purchases where the human approves a Cart Mandate with a cryptographic signature, and delegated tasks where the human signs an Intent Mandate upfront and the agent acts autonomously later. In collaboration with Coinbase and MetaMask, Google launched the A2A x402 extension for agent-based crypto payments.
AP2's strength is its comprehensive authorization and audit framework. The trade-off is that AP2 is a framework, not a payment rail - it defines how agents get permission to pay, not how the money moves.
What is x402?
 x402 is an open payment protocol created by Coinbase that enables instant stablecoin payments over HTTP by reviving the 402 status code. When a client requests a paid resource, the server responds with HTTP 402 and payment instructions (amount, currency, destination wallet). The client signs a payment, attaches it to the request header, and gets the resource. No accounts, no sessions, no API keys.
x402 V2 launched in December 2025 with wallet-based identity, dynamic payment recipients, and multi-chain support. The x402 Foundation, co-governed with Cloudflare, was launched in September 2025. Stripe integrated x402 for USDC payments on Base in February 2026. The protocol supports Base, Ethereum, Polygon, Solana, Avalanche, Sui, and other chains, with zero processing fees beyond on-chain gas.
x402 is ideal for machine-to-machine payments like API calls, data feeds, compute resources, agent-to-agent services. The trade-off is that it's stablecoin-only and doesn't handle physical goods commerce.
What is MPP (Machine Payments Protocol)?
MPP is an open-source payment protocol co-developed by Stripe and Tempo that launched March 18, 2026 alongside Tempo's mainnet.
MPP's core primitive is the "session": an agent pre-authorizes a spending limit upfront and streams granular micropayments continuously within that session, without an on-chain transaction per interaction. Stablecoin payments settle on Tempo's EVM-compatible blockchain (fees paid in any major stablecoin via an integrated AMM; no native gas token required). Fiat payments are handled via Stripe's Shared Payment Tokens (SPTs). Visa extended MPP to card-based payments; Lightspark extended it to Bitcoin Lightning. At launch, 100+ services are integrated.
MPP's strength is bridging stablecoin and fiat rails in one protocol with Stripe's full distribution behind it. The trade-off is infrastructure dependency on Stripe and Tempo's chain and a production track record still being established.
ACP vs AP2 vs x402 vs MPP: a head-to-head comparison
Protocol type and layer
 ACP: Checkout and merchant integration layer - defines how agents browse, select, and purchase from merchants
 AP2: Authorization and trust layer - defines how agents get cryptographically verified permission to transact
 x402: Execution and settlement layer - defines how payments are made instantly over HTTP using stablecoins
 MPP: Settlement and session layer - defines how agents pre-authorize a spending budget and stream micropayments continuously across both stablecoin and fiat rails, on a dedicated blockchain
 Crossmint: Unified platform supports major agentic payment protocols through a single API, alongside agent wallets, virtual cards, and stablecoin infrastructure
Payment methods supported
 ACP: Traditional payments via Stripe (cards, bank transfers, digital wallets); PayPal integration coming; fiat-only today
 AP2: Framework supports cards, bank transfers, real-time payments, and stablecoins (via A2A x402 extension); payment-rail agnostic
 x402: Stablecoin-native (USDC primary); supports Base, Ethereum, Polygon, Solana, Avalanche, Sui, and other chains; zero processing fees (only onchain gas)
 MPP: Stablecoins natively on Tempo chain; fiat via Stripe SPTs (cards, BNPL); card network payments via Visa extension; Bitcoin via Lightspark extension
 Crossmint: Fiat and major stablecoin payments; supports 50+ blockchain networks; bridges fiat and crypto in a single agent transaction
Transaction model
 ACP: Human-present conversational checkout - agent helps user complete a purchase inside a chat interface (e.g., ChatGPT)
 AP2: Both human-present (Cart Mandate with real-time approval) and human-not-present (delegated Intent Mandate for autonomous agent action)
 x402: Fully autonomous machine-to-machine - agent sends HTTP request, receives 402 response with payment terms, signs and pays, receives resource
 MPP: Sessions-based — agent pre-authorizes a spending limit once, then streams granular micropayments within the session without per-transaction on-chain overhead
 Crossmint: All of the above. Agents can transact autonomously (via x402/stablecoins), with user approval (via AP2-style mandates), or through conversational checkout, using Crossmint's agent wallets with programmable guardrails
Production readiness
 ACP: Launched in ChatGPT Instant Checkout (February 2026); OpenAI pivoted to app-based model in March 2026; protocol remains open standard with Stripe, Shopify, Salesforce, and PayPal support
 AP2: Specification published; industry coalition formed; A2A x402 extension is production-ready for crypto payments; broader card-based implementation still maturing
 x402: V2 launched December 2025; Stripe integrated x402 on Base in February 2026; Cloudflare supports x402 transactions
 MPP: Mainnet launched March 18, 2026; 100+ integrated services at launch; Stripe, Visa, Lightspark, Anthropic, OpenAI, Shopify, Mastercard partnerships confirmed
 Crossmint: Agent wallets, virtual cards, and x402 support live in production; launched lobster.cash as an open payment standard for OpenClaw agents (powered by Visa, Circle, Solana, and Stytch)
Pricing model
 ACP: Stripe processing fees apply (typically 2.9% + $0.30 for cards); merchants remain merchant of record
 AP2: No protocol fees; underlying payment processor fees apply
 x402: Zero protocol fees; users pay only blockchain gas fees (fractions of a cent on L2s like Base) MPP: No native gas token on Tempo; fees paid in any major stablecoin via integrated AMM; Stripe processing fees apply for fiat/card payments via SPTs ‍ 
 Crossmint: Usage-based pricing; contact sales for enterprise terms
Ideal use cases
 Use ACP for shopping agents that interact with merchant catalogs. If your agent helps users discover and purchase physical or digital goods and you want a standardized protocol for agent-merchant communication with Stripe handling payment processing, ACP provides that foundation. OpenAI's early pivot from in-chat checkout to app-based purchasing shows the protocol is still finding its production form, but the merchant ecosystem support from Stripe, Shopify, Salesforce, and PayPal is real.
 Use AP2 for enterprise multi-agent systems that need auditable authorization. If your agents operate across platforms, interact with multiple payment networks, or need to prove that a specific human authorized a specific purchase, AP2's cryptographic mandate system provides the compliance infrastructure. The A2A x402 extension makes AP2 the natural choice for enterprises that want both traditional and crypto payment support under one authorization framework.
 Use x402 for the machine economy. If your agents pay for API calls, data feeds, compute resources, or services from other agents, x402's HTTP-native stablecoin payments are the most efficient path. The zero-fee model (beyond minimal gas costs on L2s) makes x402 uniquely suited for high-frequency, low-value transactions.
 Use MPP when your agents need to stream micropayments in real time without incurring an onchain transaction per interaction. The sessions model makes MPP uniquely efficient for continuous workflows. 
The practical challenge is that production agent systems often need elements of all four. An agent that shops for users needs ACP's checkout flow, AP2-style authorization when acting on delegated authority, x402 or MPP when paying another agent for a data lookup, and the right sessions model for high-frequency micropayments. That's four protocol integrations, multiple wallet infrastructures, and multiple compliance surfaces to manage.
Why platforms choose Crossmint for agentic payments
The protocols above define how agents should pay. Crossmint provides the all-in-one agentic payments infrastructure to make it happen. Rather than picking one protocol and building around it, Crossmint gives your agents everything they need to transact like through a single API:
 Agent wallets - Fiat and stablecoin wallets purpose-built for AI agents. Non-custodial stablecoin wallets with programmable guardrails (spending limits, merchant whitelisting, approval requirements, auditable logs). Virtual card wallets that hold tokenized card details securely without exposing raw card data.
 Agent virtual cards - Derive virtual card numbers from your existing Visa or Mastercard, letting agents pay at any merchant that accepts cards. Scoped permissions and guardrails control spending limits, merchant access, and transaction caps.
 Stablecoin onramps - Fund agent wallets by connecting any major debit or credit card, including Visa and Mastercard. Top up virtual cards or stablecoin wallets directly. Fiat payments supported globally, stablecoin onramps available in 150+ countries.
 Agentic checkout - APIs for agents to purchase physical goods, software, flights, and more. Support for Amazon, Shopify, and other major merchants at retail price. Crossmint acts as Merchant of Record and handles returns and chargebacks - zero operational overhead.
 Agentic credentials - Verifiable credentials built on open-source W3C standards. Agents can prove they act on behalf of a specific user or hold certain affiliations. Any third party can

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
