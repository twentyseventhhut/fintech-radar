---
title: "Fintech Wrap Up: Ant International's multi-product commerce infrastructure"
date: 2026-05-20
tags:
  - company/ant-international
  - industry/payments
  - industry/infrastructure
  - region/asia
  - type/research-report
sources:
  - https://open.substack.com/pub/samboboev/p/deep-dive-ant-internationals-multi
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s13b72490
month: 2026-05
enriched: false
---

# Fintech Wrap Up: Ant International's multi-product commerce infrastructure

> [!info] 2026-05-20 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Ant International’s Multi-Product Commerce Infrastructure

## Первоисточники

### open.substack.com
<https://open.substack.com/pub/samboboev/p/deep-dive-ant-internationals-multi>
*2007 слов · direct*

Deep Dive: Ant International’s Multi-Product Commerce Infrastructure
In recent years, Ant International has evolved into a unified techfin platform powering global commerce. Its core stack combines cross-border payments (Alipay+ and Antom), digital wallets, global account services (WorldFirst), embedded finance (Bettr), plus an AI-driven layer for compliance and fintech services. As a result, the company now connects 2 billion consumer accounts to over 150 million merchants worldwide through Alipay+, processes 20+ million transactions daily, and spans 300+ payment methods across 220+ markets. WorldFirst and Bettr provide global account services to 1.6 mn SMEs, and over 30 mn underserved businesses and individuals access credit. This article breaks down the technology and product strategy behind Ant International’s platform convergence
 The platform supports 300+ payment methods, all major card schemes, 50+ wallet and bank apps, 10+ national QR systems in 220+ markets. This means consumers can use preferred local payment options, for example, SGQR, DuitNow, PromptPay, QRIS, etc., while merchants connect through one integration. 
 Antom’s merchant gateway serves businesses in 50+ countries, enabling them to accept payments in 100+ currencies and reach customers in over 200 markets. Its services go beyond payments to include digital marketing and store digitization. WorldFirst’s global account and treasury services provide one-stop cross-border accounts, payments, FX conversion, and even supply-chain financing. In combination, WorldFirst and Bettr serve 1.6+ million small businesses and provide credit access to 30+ million underserved MSMEs and consumers. 
Together, these products form a converged infrastructure layer: all facets of commerce transactions, payment acceptance, wallets, corporate accounts, and lending are integrated via APIs and common services. For example, Alipay+ links global bank apps and e-wallets to merchants via SWIFT rails and ISO 20022 messaging. Antom supports card and alternative payments through an enterprise-grade gateway, including APM checkout and digital wallets. Bettr provides embedded finance APIs to accelerate merchant growth, and WorldFirst offers treasury APIs such as a multi-currency account and fund management for cross-border trade. All services share identity, risk, and funds movement flows on Ant’s unified stack.
Fintech Wrap Up is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Payments and Wallets Platform 
At the center are global payment services. Ant International’s payment layer, mainly Alipay+ and Antom, creates a unified acceptance network. Alipay+ is a wallet gateway that “allows consumers to use their preferred payment methods seamlessly and securely, online and offline.” It interoperates digital wallets and apps including 36 e-wallet partners and BNPL apps across borders. Antom is the merchant-facing payment engine, described by the company as providing “unified, vertical-specific digital payment solutions” for businesses of all sizes. Together, they link 2 billion user accounts to 150+ million merchants, enabling one-click checkout in a wide variety of currencies and payment schemes.
This interoperability is supported by extensive APIs and integrations. The platform connects over 10 national QR payment networks and the major card and ACH networks, plus dozens of local wallets, under a single API. For example, through partnerships and standards like ISO 20022, Ant International demonstrated a live bank-to-wallet payment solution: Standard Chartered Bank accounts can send funds to Alipay+-enabled e-wallets globally, leveraging SWIFT infrastructure. In effect, Ant’s payments layer abstracts a complex global network of rails cards, ACH, QR, and wallets into one operating layer for merchants.
On the merchant side, Antom’s SDKs and tools make it simple to onboard new merchants. The Antom Copilot 2.0 is a key example: it automates payment integration, merchant onboarding, risk checks and chargeback resolution in an AI-driven workflow. Within a year, 72% of Antom-onboarded merchants had completed their own payment integration using the Copilot, and it has boosted chargeback handling efficiency by ~46%. These capabilities mean merchants get connected faster and maintain higher transaction success rates on the platform.
Key quantitative highlights of the payments/wallets layer include:
 300+ payment methods supported (cards, 50 mobile wallets/bank apps, 10+ national QR codes). 
 20+ million daily transactions on average across the network. 
 Acceptance in 220+ markets worldwide. 
Global Accounts and Treasury 
Complementing payments is a cross-border account and treasury layer built on the WorldFirst platform. WorldFirst provides one-stop account services for businesses operating internationally. In practice, this includes multi-currency collection accounts, global payments, currency conversion and hedging, and supply-chain financing options. Small traders can open local accounts in key currencies or regions to receive payments and pay suppliers more cheaply. All currency conversions and transfers happen through WorldFirst’s treasury infrastructure.
 Ant International claims to manage “the largest number of global accounts” for businesses, especially SMEs, in cross-border commerce. This suggests its platform handles vast volumes of multi-currency transactions and holds significant deposit balances. By offering treasury-as-a-service APIs, Ant’s platform enables merchants to automate cash management e.g., API-triggered FX hedges or automated disbursements in the same interface as payments and wallets. This effectively brings corporate finance into the unified stack. 
In Ant’s strategy, the global account function is key to enabling every business to go global from day one. WorldFirst’s technology is layered into the platform: for instance, SMEs paid in one currency can automatically trigger exchange and payouts in another currency via the same dashboard. In sum, the account/treasury layer turns Ant’s infrastructure into a digital bank for merchants, ensuring payments, collections and currency management flow through one system.
Embedded Finance and Credit 
The third pillar is inclusive finance and credit, delivered mainly by Bettr. Bettr’s API-driven platform provides loans, credit lines, and other financial services to SMEs and individuals who lack traditional access. It embeds credit offers at the point of sale or online checkout. Through Bettr, Ant International has extended credit access to 30 million+ underserved businesses and consumers. These loans are often financed via partnerships with local lenders or via blockchain-enabled capital pools.
Bettr is tightly integrated with Alipay+ and Antom. For example, when a merchant onboards via Antom, the same backend can check SME creditworthiness using Ant’s data and AI models, and offer them financing through Bettr. Similarly, consumers in emerging markets can get microloans at checkout via mobile wallets powered by Alipay+. The strategy here is “strategic value boosters”: Ant International explicitly positions embedded financing, credit and treasury as growth enablers for merchants. By offering credit as a service, Ant International can increase transaction volume and lock in customer relationships.
On the tech side, Ant is applying advanced tech to lending. Its sustainability report notes that credit services are integrating new AI and blockchain capabilities. While details are sparse, this could mean using distributed ledgers for credit risk or identity, or AI for loan approval. The combination of global payments and embedded credit creates a tight feedback loop: payments data helps underwrite loans, and credit expands purchasing power on the platform.
AI-Driven Product Layer 
Underpinning all products is an AI/FinTech layer. Ant International has been keen to brand itself as an “AI commerce” pioneer. It has opened up several AI frameworks and tools for partners and internal use:
 Agentic Payment Solutions: Antom launched an agentic payment solution that lets AI agents conduct payments on behalf of users. It supports APMs and cards in one checkout flow, effectively enabling conversational or automated purchasing. Relatedly, at MoMents 2026 Ant introduced an Agentic Mobile Protocol (AMP) – an open-source framework for mobile-based agentic payments. AMP allows AI-driven apps and even wearables to transact by calling standardized payment APIs, enhancing interoperability. 
 GenAI Cockpit (FinAI-as-a-Service): A cloud platform that provides large language model toolkits and APIs for fintech use cases. For example, Malaysia’s TNG eWallet and Pakistan’s Easypaisa use it to build AI agents on top of their payment apps. Ant’s strategy is to “democratize FinAI” by giving emerging markets plug-and-play AI platforms without huge investment. 
 EPOS360: An AI-powered SME app that integrates point-of-sale (POS) checkout, banking, and financing into one interface. EPOS360 bundles merchant tools such as sales reporting, customer engagement, etc. with access to working capital and cross-border payments. It’s currently piloted in Southeast Asia onboarding via wallet mini-programs like TNG. 
 Antom Copilot (AI Merchant Assistant): Beyond onboarding, Antom’s Copilot uses machine learning on real transaction data to help merchants optimize billing, handle chargebacks, and manage disputes. In practice it “learns from real-world cases” to automate routine tasks. 
 AI SHIELD (Fraud and Risk Engine) : A 3-in-1 risk model with 7+ billion parameters that fuses graph, sequence and tabular data to flag high-risk transactions. It achieves over 95% precision in fraud detection and boosts payment success by ~13.5%. Ant shares parts of this risk technology via a Digital Wallet Guardian Partnership , enabling wallets and banks on its platform to access anti-fraud and fund-protection tools. 
 Falcon TST (AI FX Model): A mixture-of-experts AI model 8.5+ billion parameters used internally to forecast foreign exchange moves. It achieves ~93% accuracy on month-ahead FX forecasts and has cut Ant International’s FX hedging costs by up to 60%. Notably, Ant open-sourced this model in 2025 to encourage community adoption. 
 AI-as-a-Service Partnerships: Ant is working with Visa, Mastercard and others on protocols e.g. Model Context Protocol for AI commerce. It pilots tokenized, agentic card payments with Visa Intelligent Commerce and Mastercard Agent Pay, embedding Visa’s trust into AI apps. 
These AI and tech innovations do not stand alone; they are integrated into the product stack. For instance, SHIELD’s risk scores feed into Antom and Alipay+ to reduce fraud platform-wide. The GenAI and agentic frameworks are available to partners building on Alipay+. The overall approach is to use AI to automate and scale key flows such as payment onboarding, risk assessment, and customer service in the commerce stack.
Compliance, Security, and Trust 
Behind the scenes, Ant International invests heavily in compliance and security as part of its infrastructure. The company holds licenses in 60+ markets and has built a multi-layered AML and KYC framework. The AI-driven SHIELD model above is one layer of fraud prevention. There is also a 3-layer anti-money-laundering program anchored on global control standards. Ant promotes a “Privacy Enhancing Technology” program to enable cross-border wallet use without exposing user PII.
On the payments rails side, Ant is extending standards like ISO 20022 to more corridors. The SWIFT partnership to enable bank-to-wallet transfers is a prime example. By bridging SWIFT with mobile wallets, Ant’s stack creates a single settlement layer that spans traditional banking and new fintech rails. Similarly, Ant has forged alliances with national banks and networks (e.g. Saudi SAMA, Vietnam’s NAPAS) to embed its stack in local systems. In effect, the platform is designed for interoperability and compliance – every new market or payment network is another plug-in, rather than a silo.
Strategic Architecture and Integration 
 Strategically, Ant International positions itself as an end-to-end platform provider for merchants and fintech partners. Its leadership emphasizes a “layered solutions” approach: combining the four pillars Alipay+, Antom, Bettr, and WorldFirst to deliver comprehensive growth solutions. In practice, this means a single sign-on/API key can unlock payment acceptance, wallet access, account treasury functions, and financing altogether. Data flows seamlessly: a merchant’s sales data from Alipay+ can inform credit underwriting in Bettr, or a flagged fraudulent payment in Antom can trigger an AML check. The components share a common identity and data bus. 
 Ant International’s marketing calls this a “unified techfin platform” enabling inclusive growth. Indeed, its press materials describe “layered partnerships” linking 2 billion accounts and 150 million merchants. This suggests a modular architecture: each new partner wallet, bank, or gov’t network plugs into the Ant stack’s APIs. The whole stack is cloud-hosted and microservices-based (implied by scale and open-source initiatives), allowing rapid deployment of new features like agentic payments or Islamic finance programs without rebuilding core systems. 
Go-to-market, Ant bundles these services by use case. For example, an ecommerce platform could integrate Antom’s API to accept global payments, then use WorldFirst’s APIs to handle multi-currency payouts and Bettr’s API to offer installment loans at checkout. Or a mobile wallet app could adopt Alipay+ gateway for international receipts, connect to SHIELD for fraud monitoring, and tap GenAI Cockpit to build a travel-booking assistant. The end result is a converged layer: behind the scenes, all payments, wallets, accounts, credit, and security services operate as one platform.
Key Metrics 
Ant

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
