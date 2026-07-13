---
title: "Fintech Wrap Up: Visa Trusted Agent Protocol GitHub"
date: 2026-03-29
tags:
  - company/visa
  - industry/agentic-commerce
  - industry/infrastructure
  - region/global
  - type/research-report
sources:
  - https://github.com/visa/trusted-agent-protocol
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s9d8974ba
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Visa Trusted Agent Protocol GitHub

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] GitHub - visa/trusted-agent-protocol: Establishing a universal standard of trust between AI agents and merchants for the next phase of agentic commerce., accessed March 22, 2026, https://github.com/visa/trusted-agent-protocol

## Первоисточники

### github.com
<https://github.com/visa/trusted-agent-protocol>
*749 слов · direct*

Trusted Agent Protocol
 Establishing a universal standard of trust between AI agents and merchants for the next phase of agentic commerce. 
The Challenge
AI agents are becoming part of everyday commerce, capable of executing complex tasks like booking travel or managing subscriptions. As agent capabilities evolve, merchants need visibility into their identities and actions more than ever.
 For an agent to make a purchase, merchants must answer: 
Is this a legitimate, trusted, and recognized AI agent?
Is it acting on behalf of a specific, authenticated user?
Does the agent carry valid instructions from the user to make this purchase?
 Without a standard, merchants face an impossible choice: 
Block potentially valuable agent-driven commerce
Accept significant operational and security risks from unverified agents
The Solution
Visa's Trusted Agent Protocol provides a standardized, cryptographic method for an AI agent to prove its identity and associated authorization directly to merchants. By presenting a secure digital signature with every interaction, a merchant can verify that an agent is legitimate and has the user's permission to act.
For merchants, the Trusted Agent Protocol describes a standardized set of mechanisms enabling merchants to:

 Cryptographically Verify Agent Intent: Instantly distinguish a legitimate, credentialed agent from an anonymous bot. The agent presents a secure signature that includes timestamps, a unique session identifier, key identifier, and algorithm identifier, allowing you to verify that the signature is current and prevent relays or replays. 


 Confirm Transaction-Specific Authorization: Ensure the agent is authorized for the specific action it is taking (browsing or payment) as the signature is bound to your domain and the specific operation being performed. 


 Receive Trusted User & Payment Identifiers: Securely receive key information needed for checkout via query parameters. This can include, as consented by the consumer, verifiable consumer identifiers, Payment Account References (PARs) for cards on file, or other identifiers like loyalty numbers, emails and phone numbers, allowing you to streamline or pre-fill the customer experience. 


 Reduce Fraud: By trusting the agent's identity and intentions, merchants can create a more seamless path to purchase for customers using agents. This cryptographic proof of identity and intent provides a powerful new tool to reduce fraud and minimize chargebacks from unauthorized transactions. 

Key Benefits

 Differentiate from Malicious Actors: The Trusted Agent Protocol provides a definitive way for you to distinguish legitimate, authorized AI agents from other automated traffic. This allows you to confidently welcome agent-driven commerce while protecting your site from harmful bots. 


 Context-Bound Security: Every request from a trusted agent is cryptographically locked to a merchant's specific website and the exact page with which the agent is interacting . This ensures that an agent's authorization cannot be misused elsewhere. 


 Protection Against Replay Attacks: The protocol is designed to prevent bad actors from capturing and reusing old requests. Each signature includes unique, time-sensitive elements that ensure every request is fresh and valid only for a single use. 


 Securely Receive Customer & Payment Identifiers: The protocol defines a standardized way for a verified agent to pass essential customer information directly to merchants. This allows merchants to streamline the checkout process by receiving trusted data to pre-fill forms or identify the customer. 

Example Agent Verification for Payments
 
Quick Start
This repository contains a complete sample implementation demonstrating the Trusted Agent Protocol across multiple components:
🚀 Running the Sample 

 Install Dependencies (from root directory): 
 pip install -r requirements.txt 


 Start All Services : 
 # Terminal 1: Agent Registry (port 8001) 
 cd agent-registry && python main.py

 # Terminal 2: Merchant Backend (port 8000) 
 cd merchant-backend && python -m uvicorn app.main:app --reload

 # Terminal 3: CDN Proxy (port 3002) 
 cd cdn-proxy && npm install && npm start

 # Terminal 4: Merchant Frontend (port 3001) 
 cd merchant-frontend && npm install && npm run dev

 # Terminal 5: TAP Agent (port 8501) 
 cd tap-agent && streamlit run agent_app.py 


 Try the Demo : 
 
 Open the TAP Agent at http://localhost:8501 
Configure merchant URL: http://localhost:3001 
Generate signatures and interact with the sample merchant
📚 Component Documentation 
Each component has detailed setup instructions:
 TAP Agent - Streamlit app demonstrating agent signature generation
 Merchant Frontend - React e-commerce sample with TAP integration
 Merchant Backend - FastAPI backend with signature verification
 CDN Proxy - Node.js proxy implementing RFC 9421 signature verification
 Agent Registry - Public key registry service for agent verification
🏗️ Architecture Overview 
The sample demonstrates a complete TAP ecosystem:
 TAP Agent generates RFC 9421 compliant signatures
 Merchant Frontend provides the e-commerce interface
 CDN Proxy intercepts and verifies agent signatures
 Merchant Backend processes verified requests
 Agent Registry manages agent public keys and metadata

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
