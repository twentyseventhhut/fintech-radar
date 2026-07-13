---
title: "Circle launches Nanopayments on testnet for agentic economy"
date: 2026-03-12
tags:
  - company/circle
  - industry/stablecoins
  - industry/agentic-commerce
  - region/us
  - type/product
sources:
  - https://www.circle.com/blog/circle-nanopayments-launches-on-testnet-as-the-core-primitive-for-agentic-economic-activity
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s5410535e
month: 2026-03
enriched: false
---

# Circle launches Nanopayments on testnet for agentic economy

> [!info] 2026-03-12 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Circle Nanopayments launches on Testnet as the core primitive for agentic economic activity. Nanopayments provides the financial rail for the emerging agentic economy. It lets developers power pay-per-call, pay-per-use, and machine-to-machine flows where agents can send fractions of a cent in USDC nearly instantly, without paying gas fees per individual payment.

## Первоисточники

### circle.com
<https://www.circle.com/blog/circle-nanopayments-launches-on-testnet-as-the-core-primitive-for-agentic-economic-activity>
*651 слов · direct*

Home
 Solutions 
 
 
 
 Back 
 Partners 
 
 
 
 Back 
 Developer 
 
 
 
 Back 
 Company 
 
 
 
 Back 
 Transparency 
 More 
 
 
 
 Back 
Mar 10, 2026
May 14, 2026
Circle Nanopayments is the financial rail for agentic economic activity, enabling gas-free USDC transfers as small as $0.000001, powered by Circle Gateway.
Circle Nanopayments enables agents to make gas-free USDC transfers as small as $0.000001. Nanopayments, built on Circle Gateway, provides the financial infrastructure for the agentic economy.
 Circle Nanopayments , a core payments primitive that enables gas-free USDC transfers as small as $0.000001, is now live on testnet. Powered by Circle Gateway , Nanopayments provides the financial rail for the emerging agentic economy. It lets developers power pay-per-call, pay-per-use, and machine-to-machine flows where agents can send fractions of a cent in USDC nearly instantly — without paying gas fees per individual payment.
Traditional payment rails, established decades ago, weren’t designed for the high frequency and ultra-fine granularity required for agents making countless sub-cent payments. Fixed fees and operational overhead drive up the cost of these transactions, rendering ultra-small payments uneconomical.
Standard onchain transactions, while meaningfully more efficient than legacy systems, still face economic realities that hinder high-frequency, sub-cent payments. When settled individually, a typical onchain transaction fee can overshadow the payment value itself. Even on low-cost blockchains, fees for a $0.0001 transfer can represent 1,000% to 5,000% of the total amount.
To flourish, the emerging agentic economy requires infrastructure purpose built for this new way of transacting.
Built for agentic scale
Circle Nanopayments addresses these bottlenecks through offchain aggregation and delayed, batched onchain settlement. By bundling thousands of transactions into a single onchain settlement, Nanopayments slashes the gas fee to zero for the developer, with onchain costs covered by Circle at the batch settlement layer. This delayed settlement approach makes agentic payments economically viable at scale, allowing developers to build applications that transfer value nearly instantly without paying gas fee for individual transactions.
By eliminating per-transaction gas, Nanopayments enables business models built around true sub-cent value exchange. Developers can confidently implement pay-per-call APIs, real-time compute billing, pay-per-crawl search, and autonomous service marketplaces where every interaction carries programmable value.
Nanopayments works on any Gateway-supported EVM chain. It does so while following the x402 standard , which allows any agent to pay any merchant without creating an account or adding a credit card. Here’s how it works:
When an agent initiates a payment, it signs an EIP-3009 authorization (a signed token transfer authorization message) that is forwarded to the Circle Nanopayments API. 
Nanopayments validates the signature, adjusts the agent’s internal ledger balance, and provides instant confirmation to the merchant. 
The merchant can then release the good or service immediately.
The actual onchain settlement occurs periodically in the background.
Agentic economic activity in action
Nanopayments is already being validated in practice. In Circle’s recent collaboration with open-source robotics software developer OpenMind , an autonomous robot dog used Nanopayments to complete transactions in USDC to recharge itself. This demonstrates an agent-driven payment loop where autonomous software can initiate payment, receive near-instant confirmation, and continue a workflow (like recharging) while settlement is handled later via batching.
This collaboration illustrates some of the early stages of the agentic economy, and it signals a near future where robots and agents increasingly exist as fully independent economic actors.
Available on testnet for builders
Circle Nanopayments is currently available on testnet for developers building applications that incorporate sub-cent payments. As of February 2026, Nanopayments is supported on the testnet of the following chains: Arbitrum, Arc , Avalanche, Base, Ethereum, HyperEVM, Optimism, Polygon PoS, Sei, Sonic, Unichain, and World Chain. For the most up-to-date supported chain list, refer to the Nanopayments documentation.
Whether it is pay-per-crawl search, usage-based billing, or machine-to-machine marketplaces, the infrastructure for the agentic economy is here with Nanopayments. START BUILDING 
Related posts
Navigate what’s next in the new internet financial system
How Kura Is Using USDC to Reach Haiti's Last Mile
Circle Expands Support for USDC on Hyperliquid

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
