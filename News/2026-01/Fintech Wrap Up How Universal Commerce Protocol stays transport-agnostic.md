---
title: "Fintech Wrap Up: How Universal Commerce Protocol stays transport-agnostic"
date: 2026-01-18
tags:
  - industry/agentic-commerce
  - industry/ai
  - region/global
  - type/commentary
sources:
  - https://open.substack.com/pub/samboboev/p/deep-dive-googles-ap2-explained-the
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s76983304
month: 2026-01
enriched: false
---

# Fintech Wrap Up: How Universal Commerce Protocol stays transport-agnostic

> [!info] 2026-01-18 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Under the hood, UCP is transport-agnostic. The protocol defines multiple ways to carry its messages, and the merchant’s profile advertises which transports it supports. The primary binding is simple HTTPS+JSON (REST), a classic REST API approach for universal compatibility. But UCP also maps neatly onto more AI-centric channels. There’s a Model Context Protocol (MCP) binding, which lets an LLM-based agent invoke UCP “tools” (actions like create_checkout or update_checkout) directly within a conversational context. There’s an Agent-to-Agent (A2A) option, which envisions a direct agent communication channel exchanging structured UCP data without a traditional HTTP request/response overhead. UCP even supports an Embedded Protocol (EP) for cases where a merchant provides a web-based interface

## Первоисточники

### open.substack.com
<https://open.substack.com/pub/samboboev/p/deep-dive-googles-ap2-explained-the>
*960 слов · direct*

Deep Dive: Google’s AP2 Explained - The Rulebook for Agent-Led Payments
Imagine telling your AI assistant to “just buy it for me” and having it actually go through with the purchase – safely, securely, and without you clicking any “Buy Now” button. Google’s new Agent Payments Protocol (AP2) is betting on exactly that future. Announced in September 2025, AP2 is an open standard designed so AI agents can initiate payments on our behalf across different platforms. In other words, it’s a common rulebook that lets your autonomous digital sidekicks not only talk a big game, but also transact – whether that means paying a merchant, subscribing to a service, or even paying another agent. And it’s not just a Google pet project; over 60 organizations (from Mastercard and American Express to Coinbase and PayPal) are collaborating to shape this standard. Why? Because as AI assistants evolve from simple chatbots into full-fledged shopping and task-doing agents, the last missing piece is giving them a wallet – and making sure they don’t run off with it.
 But enabling AI-driven payments isn’t as simple as handing your credit card to a robot. It raises a million questions around trust: How do you prove an AI had permission to make a purchase? How can a merchant be sure the request isn’t some AI hallucination or fraud? And if something goes wrong, who’s liable – you, the agent’s creator, the bank? These are exactly the trust issues AP2 tackles head-on, with a blend of cryptography, digital “contracts,” and industry-wide guardrails. In this deep dive, we’ll break down why AP2 exists, how it works (in plain English, promise!), and what it means for banks, payment networks, stablecoins, and the whole fintech world. Grab your favorite fintech beverage (kombucha? coffee?) and let’s explore this new protocol that has AI agents doing more and more – and might just change how we think about payments. Would you let your chatbot pick up the tab? Let’s see if AP2 can make that a reality. 
 Subscribe or Support by Upgrading 
Why Was AP2 Needed? 
Today’s payment systems assume a human is behind every purchase – clicking “Buy” on a website or tapping a phone at checkout. Enter autonomous agents, and that assumption flies out the window. If an AI agent tries to pay for something on your behalf, it opens a can of trust questions that current systems can’t answer:
 Authorization: How do we verify you actually gave your agent permission to make this specific purchase? In other words, prove the AI isn’t going rogue on a shopping spree with your money. 
 Authenticity: How can a merchant be sure the agent’s order reflects your true intent and not a misunderstanding (or an AI hallucination)? Did you really want the 100 pairs of sneakers it put in the cart, or did it misinterpret your request? 
 Accountability: If a transaction turns out fraudulent or wrong, who’s on the hook for it – you (the user), the agent’s developer, the merchant, or your bank (issuer)? In other words, when your AI messes up, who pays for the damages? 
 This triad of issues – authorization, authenticity, accountability – creates what Google calls a potential “crisis of trust” in agent-led payments ] . Without a solution, people (and institutions) simply won’t feel comfortable letting bots handle money. Moreover, every player might invent their own proprietary way to solve it, leading to a fragmented mess of one-off integrations. Imagine dozens of incompatible “AI payment” systems – nightmare. 
 The Agent Payments Protocol aims to provide a common language and set of rules so any compliant AI agent can transact with any compliant merchant or payment provider, globally. Think of it as a universal trust layer for payments: an open standard that all parties can agree on to answer those tough questions. By establishing shared methods to authenticate an agent’s actions and record the user’s intent, AP2 prevents the fragmentation of “everyone doing their own thing” ] . It’s like setting the rules of the road before letting self-driving cars loose – AP2 sets the rules for self-driving wallets. Google and its partners recognized that without such a protocol, the rise of AI commerce could be stunted by fear and confusion. As one synopsis put it, a new capability (AI agents) broke the old assumptions of payments, so “you need a new foundational layer” – an open protocol so everyone can innovate on a common standard. 
 Crucially, AP2 is open and non-proprietary. It’s built as an extension of existing open protocols in the “agentic” ecosystem – namely the Agent-2-Agent (A2A) protocol for agent communication and the Model Context Protocol (MCP) for connecting AI to external tools. You don’t need to memorize those acronyms, but the point is AP2 isn’t a closed Google toy; it’s meant to slot into a broader open framework. The design philosophy is “competitive but collaborative”: any developer, bank, or fintech can implement AP2 and participate, ensuring broad interoperability and avoiding any single company controlling agent payments. In an industry where walled gardens have often been the norm, this openness is a deliberate strategy to get everyone – banks, networks, crypto players, you name it – on the same page. (After all, nothing unites fintech folks like the prospect of a trillion-dollar new market, and nothing scares them like not having a standard to tap into it.) 
What Exactly Is AP2? 
So, what is AP2 in plain terms? At its core, AP2 is a protocol – essentially a set of standards and message formats – that lets an AI agent prove it has the user’s approval 
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
