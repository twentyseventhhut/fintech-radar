---
title: "Blueprint: Jupiter's DeFi infrastructure for sovereign payroll"
date: 2026-04-29
tags:
  - company/noah
  - company/jupiter
  - industry/defi
  - industry/payroll
  - region/global
  - type/commentary
sources:
  - https://noah.com/en
  - https://noah.com/blog/noah-solana-jupiter-case-study
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s812ed456
month: 2026-04
enriched: false
---

# Blueprint: Jupiter's DeFi infrastructure for sovereign payroll

> [!info] 2026-04-29 · 1 упоминаний · 2 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] ➡️ Powering Sovereign Payroll; Jupiter's DeFi infrastructure meets the world's workforce by Noah. Noah has built an end-to-end stablecoin payments system using Solana for fast, low-cost settlement, combined with fiat rails for global collections and payouts. By integrating with Jupiter, the solution enables users to instantly access swaps, yield, and off-ramps, creating a compliant, scalable model for payroll, remittances, and cross-border payments.Powering Sovereign Payroll by Noah

## Первоисточники

### noah.com
<https://noah.com/en>
*296 слов · direct*

Powering the New Era of Payments
Trusted by Innovators
Our Solutions
Payin
 Issue named virtual bank accounts across major currencies , supporting both local bank transfer payments and SWIFT. Collect fiat and convert instantly to stablecoins.
Orchestrate
 Trigger automatic payments based on rules you define - like thresholds, timing, recipient type, or currency. Set it once and automate high-volume flows with full compliance and reliability.
Regulated Payments Infrastructure, Engineered for Modern Money
Architected for High-Volume Money Movement
 Precision at scale . Whether you are running mass payroll or high-frequency remittances, our modular infrastructure delivers the flexibility and reliability your platform demands.
Total Visibility, Complete Operational Control.
Developer-First, by Design
This endpoint sets up a workflow which automatically converts fiat currency from bank deposits into cryptocurrency and sends the acquired crypto to the specified wallet address on the specified network.
Backed by the Brightest. Built by Industry Experts
Backed by Felix Capital, FJ Labs, and LocalGlobe, plus a network of strategic investors and operators who believe stablecoins will power the next generation of payments.
Shah Ramezani
Shah Ramezani is the Founder and Board Member of Noah. Shah previously led the Asia division at The Hut Group and has significant experience working in the financial sector at Kingsway Capital, Lazard and UBS.
Thijn Lamers
Thijn Lamers is a founding team member of Adyen and the former Executive Vice President of Global Sales. Adyen grew into the world’s leading global payments platform, with clients including Uber, Facebook & Ebay.
Enterprise Grade Compliance & Security
Risk scoring, anomaly detection, ongoing review.
Pre-existing onboarding data can be shared via API for real-time approval.
Document checks, liveness verification, ID validation. White label or hosted, you decide.
Sanctions, PEP, AML, adverse media checks, travel rule compliance.
Start Building on the Enterprise
Stablecoin Stack.

### noah.com
<https://noah.com/blog/noah-solana-jupiter-case-study>
*1008 слов · direct*

TLDR
Noah has built end-to-end stablecoin payments infrastructure, using Solana as the blockchain settlement layer. Noah leverages Solana’s compliance-first features like token extensions and permissioned environments for regulated payment flows and enterprise use cases. Jupiter's composable DeFi layer transforms settled stablecoins into sovereign financial instruments — enabling workers to swap, earn yield, or off-ramp instantly without custodial intermediaries.
Highlights
 Noah provides regulated Virtual Accounts (USD, EUR, GBP) with collection via ACH, FedWire, SEPA, FPS, SWIFT - and payouts across 60+ countries through local rails including M-Pesa, PIX, and SPEI. 
 Solana’s sub-cent fees and 400ms finality make micro payments as small as $10 economically viable - while Token Extensions and permissioned environments enable compliance ready, enterprise grade settlement. 
 The paying client sends a normal bank transfer with no crypto friction giving the freelancer immediate access to Jupiter's swap, yield, and off-ramp capabilities — with Noah handling the fiat rails. 
 The architecture is replicable: the same fiat collection → blockchain settlement → financial access pattern applies to payroll, remittances, B2B trade, and marketplace payouts. 
The problem: Freelancers lost control of their money
A freelance developer in Vietnam invoices a European client €2,000 for a month’s work. In the traditional system, that payment passes through a chain of intermediaries – client → freelancer platform → payment processor → local bank – each extracting fees and introducing delays. By the time the funds arrive, the freelancer has lost 5-10% to FX spreads and lifting fees, waited 2-5 business days, and holds a liability on someone else’s balance sheet that can be frozen at any point in the chain.
This isn’t a niche problem. The global remittance market is $685 billion annually , and cross-border freelance payments are one of its fastest growing segments. The friction is structural” correspondent banking networks were designed for large, infrequent transfers between institutions – not for small. Frequent, multi-currency payments that define the modern gig economy.
Stablecoins offer a better settlement layer. But a stablecoin sitting on a blockchain doesn't pay rent in Ho Chi Minh City. The missing piece is infrastructure that connects the freelancer’s fiat denominated invoice to the blockchain-settled stablecoins – without requiring the paying client to know or care that crypto is involved.
This is what Jupiter built on Solana and Noah.
The solution: Virtual Accounts to Jupiter
Jupiter, the DeFi Superapp and global leader in on-chain finance, powering 90% of trading volume on Solana, partnered with Noah to pioneer a new payment category: Sovereign Payroll: freelancers receive fiat payments through standard banking rails that auto-convert to stablecoins in non-custodial Solana wallets, giving workers instant access to Jupiter's full DeFi ecosystem.
The architecture works in three steps:
"This is a key step in building a better financial system for people around the world. Within seconds, anyone around the world can get paid and then swap, earn yield, or pay across 60+ countries (and counting) through Jupiter. We’ve collapsed the entire financial stack : payroll, trading, savings, FX into a single flow with the help of Noah" - Kash Dhanda, COO, Jupiter
Why this works: Solana’s economics make micro payments viable
The choice of Solana as the settlement rail is not incidental – it is an economic requirement for this use case.
Freelancers receive small, frequent payments: $50 for a logo, $200 for a code review. At median fees of ~$0.001 and sub-second confirmation, Solana makes even $10 micro-payments economically viable: a threshold no legacy settlement network hits.
This distinction matters for product decision makers evaluation infrastructure: Solana is the difference between a payment rail that works for enterprise invoices only and one that scales down to the entire global workforce.
Beyond cost, Solana’s Token Extensions provide compliance capabilities that Noah leverages for regulated payment flows – confidential transfers for privacy preserving amounts, transfer hooks for programmable compliance checks, and memo fields for structured payment data like invoice references. These features, combined with Solana’s permissioned environments for enterprise clients requiring controlled access, create what amounts to a programmable, compliance ready payment rail at a protocol level.
The “Sovereign Payroll” thesis
This architecture introduces a concept that goes beyond faster, cheaper payments.
In the traditional model, a freelancer’s earnings exist as liabilities on intermediary balance sheets – freelance platform → payment processor → local bank – until withdrawn cash. At any point, these intermediaries can freeze access, impose withdrawal limits, or apply unfavourable conversion rates. The worker never truly controls their own income.
In the Sovereign Payroll model, funds become bearer assets the moment they settle to the freelancer’s Solana wallet. The freelancer holds the private keys. No intermediary can freeze, delay, or seize the funds post settlement. And through Jupiter, those funds are immediately composable – swappable, lendable, and deployable – without requiring additional financial institutions.
For workers in regions with banking instability, capital controls, or currency devaluation, this is not an incremental improvement. It is a structural change in economic agency.
Results and Traction
What this means for the market
 For fintechs and payment companies evaluating stablecoin infrastructure: this case study demonstrates a production ready architecture for embedding stablecoin settlement into existing payment flows without exposing end users to crypto complexity. The payin side (Noah’s virtual accounts + fiat rails) abstracts the on ramp entirely – the paying client sends a standard bank transfer, and the recipient gets stablecoins. The pattern is replicable across payroll, remittances, B2B trade settlements, and marketplace payouts.
For fintechs and payment companies evaluating stablecoin infrastructure: Noah's fiat connectivity is live across 60+ countries with SEPA, ACH, Fedwire, FPS, and SWIFT paying rails. Solana provides the settlement layer with sub-cent fees, sub-second confirmation, and compliance-ready features through Token Extensions and permissioned environments. Jupiter provides the composable financial endpoint — where stablecoins don't just sit, they work. Together, they replace correspondent banking for an entire class of cross-border payment.
And for the freelancer in Ho Chi Minh City, the money now arrives in minutes, costs almost nothing to move, and belongs to them the moment it lands.
 Explore Noah’s Develop Docs 
 Learn about Solana for payments 
 Explore DeFi on Jupiter

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
