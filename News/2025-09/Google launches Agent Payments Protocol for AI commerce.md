---
title: "Google launches Agent Payments Protocol for AI commerce"
date: 2025-09-17
tags:
  - company/google
  - industry/agentic-commerce
  - industry/payments
  - region/global
  - type/product
sources:
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
  - https://ap2-protocol.org
  - https://www.finextra.com/newsarticle/46600/google-unveils-agent-payments-protocol-to-power-ai-commerce
  - https://www.finextra.com/newsarticle/46618/google-and-paypal-agree-multi-year-commerce-collaboration
status: tagged
n_mentions: 6
channels:
  - "Connecting the Dots in Fintech"
  - "Fintech Wrap Up"
  - "The Fintech Blueprint"
  - "This Week in Fintech"
story_id: se9f1c2d4
month: 2025-09
enriched: false
---

# Google launches Agent Payments Protocol for AI commerce

> [!info] 2025-09-17 · 6 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Fintech Wrap Up, The Fintech Blueprint, This Week in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌎 Google announced the Agent Payments Protocol (AP2), powering AI commerce. The protocol can be used as an extension of the Agent2Agent (A2A) protocol and Model Context Protocol (MCP). In concert with industry rules and standards, it establishes a payment-agnostic framework for users, merchants, and payment providers to transact with confidence across all types of payment methods.

[Fintech Wrap Up] The Agent Payments Protocol aims to provide a common language and set of rules so any compliant AI agent can transact with any compliant merchant or payment provider, globally. Think of it as a universal trust layer for payments: an open standard that all parties can agree on to answer those tough questions. By establishing shared methods to authenticate an agent’s actions and record the user’s intent, AP2 prevents the fragmentation of “everyone doing their own thing”]. It’s like setting the rules of the road before letting self-driving cars loose – AP2 sets the rules for self-driving wallets. Google and its partners recognized that without such a protocol, the rise of AI commerce could be stunted by fear and confusion. As one synopsis put it, a new capability (AI agents) broke the old ass

[The Fintech Blueprint] We examine how Google’s re-entry into fintech with the launch of the Agent Payments Protocol (AP2) marks the beginning of a new phase of agentic commerce, where AI agents can safely make payments on behalf of users. Source

[The Fintech B

## Первоисточники

### cloud.google.com
<https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol>
*2073 слов · direct*

Powering AI commerce with the new Agent Payments Protocol (AP2) 
 
 
 
 
VP/GM, Payments, Google
VP/GM, Business Applications Platform, Google Cloud
The front door to AI in the workplace
 Today, Google announced the Agent Payments Protocol (AP2), an open protocol developed with leading payments and technology companies to securely initiate and transact agent-led payments across platforms. The protocol can be used as an extension of the Agent2Agent (A2A) protocol and Model Context Protocol (MCP). In concert with industry rules and standards, it establishes a payment-agnostic framework for users, merchants, and payments providers to transact with confidence across all types of payment methods. 
 We’re collaborating with a diverse group of more than 60 organizations to help shape the future of agentic payments, including Adyen, American Express, Ant International, Coinbase, Etsy, Forter, Intuit, JCB, Mastercard, Mysten Labs, Paypal, Revolut, Salesforce, ServiceNow, UnionPay International, Worldpay, and more. 
 Why is a protocol needed? 
 AI agents are capable of transacting on behalf of users, which creates a need to establish a common foundation to securely authenticate, validate, and convey an agent’s authority to transact. While today’s payment systems generally assume a human is directly clicking "buy" on a trusted surface, the rise of autonomous agents and their ability to initiate a payment breaks this fundamental assumption and raises critical questions that AP2 helps to address, including: 

 Authorization : Proving that a user gave an agent the specific authority to make a particular purchase. 


 Authenticity : Enabling a merchant to be sure that an agent's request accurately reflects the user's true intent.  


 Accountability : Determining accountability if a fraudulent or incorrect transaction occurs.  

 AP2 is an open, shared protocol that provides a common language for secure, compliant transactions between agents and merchants, helping to prevent a fragmented ecosystem. It also supports different payment types–from credit and debit cards to stablecoins and real-time bank transfers. This helps ensure a consistent, secure, and scalable experience for users and merchants, while also providing financial institutions with the clarity they need to effectively manage risk. 
 How it works: Establishing trust via mandates and verifiable credentials 
 AP2 builds trust by using Mandates—tamper-proof, cryptographically-signed digital contracts that serve as verifiable proof of a user's instructions. These mandates are signed by verifiable credentials (VCs) and act as the foundational evidence for every transaction. 
 Mandates address the two primary ways a user will shop with an agent: 

 Real-time purchases (human present ): When you ask an agent, “Find me new white running shoes,” your request is captured in an initial Intent Mandate . This provides the auditable context for the entire interaction in a transaction process. After the agent presents a cart with the shoes you want, your approval signs a Cart Mandate . This is a critical step that creates a secure, unchangeable record of the exact items and price, ensuring what you see is what you pay for. 


 Delegated tasks (human not present) : When you delegate a task like, “Buy concert tickets the moment they go on sale,” you sign a detailed Intent Mandate upfront. This mandate specifies the rules of engagement—price limits, timing, and other conditions. It serves as verifiable, pre-authorized proof that can allow the agent to automatically generate a Cart Mandate on your behalf once your precise conditions are met. 

 In both scenarios, this chain of evidence culminates in securely linking your payment method to the verified contents of the Cart Mandate. This complete sequence—from intent, to cart, to payment—creates a non-repudiable audit trail that answers the critical questions of authorization and authenticity, providing a clear foundation for accountability. 
 Unlocking new commerce experiences 
 AP2’s flexible design provides a foundation to support both simple and entirely new commercial models. Let’s consider a few examples below, which all assume Intent Mandates have been signed on behalf of a user:  

 Smarter shopping : A customer discovers a winter jacket they want is unavailable in a specific color, so they tell their agent: "I really want this jacket in green, and I'm willing to pay up to 20% more for it." The agent then monitors prices and availability and automatically executes a secure purchase the moment that specific variant is found, capturing a high-intent sale that would have otherwise been lost. 


 Personalized offers : A shopper tells their agent they want a new bicycle for an upcoming trip from a specific merchant. Their agent communicates this information—which includes the trip's date—to the merchant, whose own agent can respond by creating a custom, time-sensitive bundle offer that includes the bike, a helmet, and a travel rack at a 15% discount, turning a simple query into a more valuable sale. 


 Coordinated tasks : A user is planning a weekend trip and tells their agent: "Book me a round-trip flight and a hotel in Palm Springs for the first weekend of November, with a total budget of $700." The agent can then interact with both airline and hotel agents, as well as online travel agencies and booking platforms, and once it finds a combination that fits the budget, it can execute both cryptographically-signed bookings simultaneously. 

 Support for emerging payments systems 
 AP2 is designed as a universal protocol, providing security and trust for a variety of payments like stablecoins and cryptocurrencies. To accelerate support for the web3 ecosystem, in collaboration with Coinbase, Ethereum Foundation, MetaMask and other leading organizations, we have extended the core constructs of AP2 and launched the A2A x402 extension , a production-ready solution for agent-based crypto payments. Extensions like these will help shape the evolution of cryptocurrency integrations within the core AP2 protocol.  
 What’s next: A call for collaboration  
 AP2 provides a trusted foundation to fuel a new era of AI-driven commerce. It establishes the core building blocks for secure transactions, creating clear opportunities for the industry–including networks, issuers, merchants, technology providers, and end users–to innovate on adjacent areas like seamless agent authorization and decentralized identity. We are committed to evolving this protocol in an open, collaborative process, including through standards bodies, and  invite the entire payments and technology community to build this future with us.  
 Many of the partners building A2A agents have extended their support to AP2. This growing ecosystem will continue to make their agents available in our AI Agent Marketplace, including new, transactable experiences enabled by AP2. For example, enterprise companies could use AP2 for B2B applications, such as enabling autonomous procurement of partner-built solutions via Google Cloud Marketplace or the automatic scaling of software licenses based upon real-time needs. 
 To get started, visit our public GitHub repository to review the complete technical specification, documentation, and reference implementations. Moving forward, this repository will be updated regularly with additional reference implementations from Google and innovations from the community to demonstrate the power and scalability of AP2. 
 Support from our ecosystem 
 Accenture: “Google Cloud's Agent Payments Protocol (AP2) complements the Agent2Agent protocol and Model Context Protocol to provide a unified framework for agents to transact. Innovations like this will enable many of the agentic solutions that reinvent payments for clients – not only for today’s needs, but for the evolving models of future commerce.” – Scott Alfieri, Google Business lead at Accenture 
 Adobe: “Adobe is proud to work with Google to advance secure and authenticated agentic commerce - our role in the Agent Payments Protocol (AP2) underscores our commitment to trusted, AI-driven experiences. With Adobe Commerce and AI agents powering customer journeys, we are focused on delivering secure, reliable, and authentic transactions for businesses and consumers."  - Loni Stark, VP of Strategy and Product at Adobe 
 Adyen: "Agentic commerce is not just about a consumer-facing chatbot, but about the underlying infrastructure that powers it all. Adyen’s collaboration on Google’s Agent Payments Protocol (AP2) is a natural extension of our mission to provide the merchants with the payments building blocks for tomorrow’s commerce. We're excited to help establish a common rulebook that ensures security and interoperability for everyone involved in the payments ecosystem." - Ingo Uytdehaage, Co-CEO at Adyen 
 Airwallex: "Airwallex is thrilled to support Google’s Agent Payments Protocol (AP2) . This is a critical step forward in building a secure, interoperable ecosystem for agentic AI payments. This protocol gives businesses and consumers the confidence to delegate tasks to AI agents, aligning with our mission to build the future of finance by empowering businesses globally.” - Jacob Dai, Co-Founder & CTO at Airwallex 
 American Express: “With the rise of AI-driven commerce, trust and accountability are more important than ever. American Express is excited to contribute to the creation of AP2 as a protocol intended to protect customers and enable participation in the next generation of digital payments.” - Luke Gebb, EVP, Amex Digital Labs, American Express 
 Ant International: "Ant International is excited to partner with Google on protocol-setting for practical AI applications in agentic commerce to unlock new merchant growth and elevate consumer experience, by leveraging our expertise in alternative payment methods and trusted AI innovations." - Jiangming Yang, Chief Innovation Officer at Ant International 
 BHN: “As a trusted partner processing billions of transactions globally, BHN is excited to help shape emerging protocols like AP2 that will enable both merchants and consumers to leverage the power of stored value in secure, autonomous commerce, enabled by AI Agents.” - Nik Sathe, CPTO at BHN 
 BVNK: "Stablecoins provide an obvious solution to the scaling challenges agentic systems are already facing with legacy financial infrastructure. We at BVNK were extremely excited to hear that Google has been working on solving this problem and couldn't wait to contribute" - Donald Jackson, CTO at BVNK 
 Checkout.com: "Agentic commerce is reshaping the checkout moment, and Google’s Agent Payments Protocol (AP2) is a pivotal step forward. At Checkout.com, we’re proud to support open protocols that strengthen trust and give merchants the flexibility to meet their customers where they are, however they want to shop.” – Meron Colbeci, Chief Product Officer, Checkout.com 
 Coinbase: "x402 and AP2 show that agent-to-agent payments aren’t just an experiment anymore, they’re becoming part of how developers actually build. Bringing x402 into AP2 to power stablecoin payments made sense - it’s a natural playground for agents to start transacting with each other and testing out crypto rails. And it’s exciting to see the idea of agents paying each other resonate with the broader AI community." – Erik Reppel, Head of Engineering at Coinbase Developer Platform 
 Crossmint: “With Crossmint’s tools, developers can let agents buy anything using both credit cards or stablecoins. Our goal is to unlock instantaneous, global commerce, giving agent builders the greatest flexibility. Our partnership with Google on AP2 represents our commitment that agentic commerce wins everyone’s trust as a secure, reliable, and seamless way to transact. Time to accelerate!” – Alfonso Gomez, Co-founder at Crossmint 
 Confluent: "Confluent is excited to support Google in this effort to build an open, secure, and high-trust payments protocol. Agent Payments Protocol (AP2) aligns perfectly with our vision of a real-time data-driven world, and we believe our expertise in data streaming with Apache Kafka will be critical in creating a resilient and scalable payments ecosystem for the agentic web." – Pascal Vantrepote, Partner CTO at Confluent  
 Dell: “At Dell Technologies, we’re dedicated to making agentic AI a reality for businesses worldwide . The transformative potential of agentic automation hinges on trust, security and standardization, especially for customer-facing eCommerce platforms. By supporting the Agent Payments Protocol (AP2) with Google, we’re laying the groundwork for a future where AI-driven commerce is reliable, accessible, and trusted by all." – Satish Iyer, Vice President, Innovation & Ecosystems, Office of the CTO, Dell Technologies 
 Deloitte: “As Agentic Commerce rapidly emerges as a transformative force, the industry will need robust standards to empower AI agents to transact payments securely and effectively. These standards must address critical areas such as security, identity, frictionless commerce, trust, and privacy, all while providing compatibility with the existing global payments infrastructure. Deloitte is proud to help shape this evolving industry alongside Google, extending the widely adopted A2A protocol to enable agent-driven payments and commerce.” – Gopal Srinivasan, Alphabet Google Alliance Global AI & Data Leader at Deloitte Consulting LLP 
 DLocal: "Payment agents are no longer an idea, they’re rapidly becoming a reality. In the dynamic emerging markets we serve, payments are fragmented and complex, from cards to local payment methods, to wallets and stablecoin.Agent Payments Protocol (AP2) turns that complexity into a single, interoperable framework, enabling agent-initiated payments that are safe, seamless, and designed to boost merchant conversion while keeping users in control." - Pedro Arnt, CEO at DLocal 
 Ebanx: "Agent Payments Prot

### Прочие ссылки (без извлечённого текста)

- <https://ap2-protocol.org>
- <https://www.finextra.com/newsarticle/46600/google-unveils-agent-payments-protocol-to-power-ai-commerce>
- <https://www.finextra.com/newsarticle/46618/google-and-paypal-agree-multi-year-commerce-collaboration>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
