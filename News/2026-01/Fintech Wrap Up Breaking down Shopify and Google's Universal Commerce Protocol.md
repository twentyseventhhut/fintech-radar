---
title: "Fintech Wrap Up: Breaking down Shopify and Google's Universal Commerce Protocol"
date: 2026-01-21
tags:
  - company/shopify
  - company/google
  - industry/agentic-commerce
  - region/global
  - type/commentary
sources:
  - https://open.substack.com/pub/samboboev/p/deep-dive-breaking-down-shopify-and
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s641e2c9f
month: 2026-01
enriched: false
---

# Fintech Wrap Up: Breaking down Shopify and Google's Universal Commerce Protocol

> [!info] 2026-01-21 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Breaking Down Shopify and Google’s Universal Commerce Protocol

## Первоисточники

### open.substack.com
<https://open.substack.com/pub/samboboev/p/deep-dive-breaking-down-shopify-and>
*796 слов · direct*

Deep Dive: Breaking Down Shopify and Google’s Universal Commerce Protocol
Commerce is messy and complex. The Universal Commerce Protocol (UCP) tackles that complexity head-on by defining a common language for any AI agent to transact with any merchant. Co-developed by Shopify and Google (with backing from 20+ retailers and platforms), UCP is an open standard built to make integrations fast and flexible. In this deep dive, I break down UCP’s architecture, how agents and merchants negotiate capabilities, Shopify’s embedded checkout approach, and how this protocol is powering AI-native commerce across ChatGPT, Google’s Gemini, Microsoft Copilot, and beyond. I also examine how Shopify’s Agentic Catalog opens this ecosystem to every merchant. Let’s get into it.
Fintech Wrap Up is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Protocol architecture 
UCP’s design is layered and modular by intent. A monolithic all-in-one API would be too rigid and slow to evolve, so UCP cleanly separates concerns. Key layers include:
 Base Shopping Service – Defines core commerce primitives (think checkout session, line items, totals, status messages) that every transaction needs. This is the foundation (dev.ucp.shopping schema) on which everything builds. 
 Capabilities – Self-contained functional modules that sit atop the base service. Capabilities are the major “verbs” of commerce, for example, Checkout, Order, Catalog (product discovery/cart), Identity Linking, etc. Each capability is versioned and evolves independently, so new features in one area don’t break others. 
 Extensions – Optional, domain-specific add-ons that extend a capability’s schema. Extensions plug in things like loyalty points, discounts, subscriptions, or specialized fulfillment options. For instance, there’s a standard dev.ucp.shopping.fulfillment extension that adds shipping groups, delivery windows, pickup options and so on to the core checkout schema. If a merchant has a unique requirement beyond the standard, they can even define their own extension (e.g. com.merchant.loyalty) without waiting for a committee. Extensions compose with the core model; they add fields if both sides support them, and version independently so the core stays stable. 
This layering lets UCP accommodate the wild diversity of commerce. Merchants implement only the capabilities (and extensions) they need, and agents negotiate only what they can handle. The result is a flexible system that can expand without collapsing under the weight of new features.
Under the hood, UCP is transport-agnostic. The protocol defines multiple ways to carry its messages, and the merchant’s profile advertises which transports it supports. The primary binding is simple HTTPS+JSON (REST), a classic REST API approach for universal compatibility. But UCP also maps neatly onto more AI-centric channels. There’s a Model Context Protocol (MCP) binding, which lets an LLM-based agent invoke UCP “tools” (actions like create_checkout or update_checkout) directly within a conversational context. There’s an Agent-to-Agent (A2A) option, which envisions a direct agent communication channel exchanging structured UCP data without a traditional HTTP request/response overhead. UCP even supports an Embedded Protocol (EP) for cases where a merchant provides a web-based interface to be embedded in a host (more on that in a bit). In practice, this means UCP can ride over whatever channel makes sense, be it a REST call from a plugin, an AI’s internal tool-call mechanism, or an iframe/SDK for an embedded checkout.
 Finally, UCP leverages the Agent Payment Protocol (AP2) to handle payments in truly autonomous scenarios. AP2 is an open protocol designed for AI agents to complete payments securely and autonomously. In UCP, AP2 comes into play via the AP2 Mandates extension on Checkout: if negotiated, the agent can present a cryptographic mandate (essentially a signed proof of the user’s authorization for the transaction) and the merchant can cryptographically verify it. This adds a layer of trust when an AI agent is running the entire checkout without user intervention, ensuring there’s non-repudiable proof the user approved the order. In short, UCP’s architecture covers all the bases: a clean separation of concerns, an open extension model, and multiple transport protocols (REST, MCP, AP2, A2A) to plug into any stack. 
Discovery, matching, and handoff 
 UCP flips the typical integration burden by making capabilities discoverable and negotiable in real-time. Here’s how it works: each merchant publishes a profile of what it supports, basically a JSON document (usually hosted at a standard URL like https://merchant.com/.well-known/ucp) declaring its capabilities, supported extensions, and transport endpoints. Similarly, each agent (platform) has its own profile describing what features it can work with. When an agent wants to initiate a transaction (say the user asked it to buy something), it first discovers the merchant’s profile (via the known URL or other discovery service) and then includes a reference to the agent’s own profile in the request. 
Keep reading with a 7-day free trial
Subscribe to Fintech Wrap Up to keep reading this post and get 7 days of free access to the full post archives.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
