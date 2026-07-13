---
title: "Circle introduces open-source Arc Fintech Starter for USDC treasury"
date: 2026-04-13
tags:
  - company/circle
  - industry/stablecoins
  - industry/infrastructure
  - region/us
  - type/product
sources:
  - https://www.circle.com/es-la/blog/build-a-multichain-treasury-system-on-arc
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sfbdd85a9
month: 2026-04
enriched: false
---

# Circle introduces open-source Arc Fintech Starter for USDC treasury

> [!info] 2026-04-13 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Circle has introduced the Arc Fintech Starter, an open-source app that demonstrates how to build multichain treasury systems with USDC, helping teams manage wallets, move funds across chains, and execute payouts. Read more

## Первоисточники

### circle.com
<https://www.circle.com/es-la/blog/build-a-multichain-treasury-system-on-arc>
*860 слов · direct*

Inicio
 Soluciones 
 
 
 
 Atrás 
 Socios 
 
 
 
 Atrás 
 Desarrollador 
 
 
 
 Atrás 
 Empresa 
 
 
 
 Atrás 
 Transparencia 
 Más 
 
 
 
 Atrás 
Apr 10, 2026
Apr 23, 2026
Learn how to build a multichain treasury system on Arc with USDC, Circle Wallets, Bridge Kit + Forwarding Service and Circle Gateway using the Arc Fintech Starter.
Moving your treasury onchain can be straightforward in some cases. Managing funds across multiple wallets and chains is where operational complexity shows up.
 USDC balances quickly become fragmented across networks. Users, vendors, and employees expect to get paid on different chains. Teams end up moving funds constantly just to stay operational.
Onchain treasury management is essentially the set of tools and processes to: 
Create and manage operational wallets
Move USDC between chains when needed 
Consolidate balances so they’re usable for day-to-day operations 
Execute payouts with logging and basic controls
To make these workflows easier to understand end-to-end, we built the Arc Fintech Starter , an open-source sample app that demonstrates how a multichain treasury system can be built on Arc.
 Who this is for 
This starter is designed for builders working on:
Fintech apps (wallets, neobanks, payment platforms)
Marketplaces with cross-chain payouts
Payroll or remittance systems
AI agents that need to move and manage money
If your product needs to hold, move, or pay USDC across chains , this is a practical place to start.
 What you’ll get in ~15 minutes 
By running this app locally and following the guided flow, you’ll:
Create and manage wallets across multiple chains
Move USDC between chains using Bridge Kit and Gateway 
Consolidate balances into a unified Gateway balance
Execute a real payout across chains
 Get started 
Clone the repo
Run the app locally
Follow the “create → fund → rebalance → unify → pay” flow
 What the starter app demonstrates 
This is a minimal fintech dashboard that acts like a treasury operations console .
It uses:
 Circle Developer-Controlled Wallets Create and manage wallets programmatically
 Circle Bridge Kit + Forwarding Service Rebalance funds across chains
 Circle Gateway Consolidate balances into a unified, spendable pool
This is not meant to be a finished product. It’s a reference architecture you can run, inspect, and extend.
 The core workflow 
The app follows a simple but realistic flow:
 Create → Fund → Rebalance → Unify → Pay 
 1) Create wallets on multiple chains 
Start by creating a few Developer Controlled Wallets across different supported testnets (for example, Arc Testnet plus one or more other chains). 
This sets up the basic “multichain treasury” state.
 app/api/wallet/route.ts 
 2) Fund your primary wallet 
Deposit testnet USDC into your Arc wallet using the Circle Testnet Faucet . 
This becomes your initial treasury balance.
 3) Rebalance from Arc to other chains 
Use the Rebalance feature to distribute USDC from the Arc wallet to wallets on other chains.
Under the hood, this uses Bridge Kit + Forwarding Service .
 app/api/bridge/rebalance/route.ts 
 4) Consolidate into Gateway 
Use Add Funds to deposit USDC from multiple wallets into Gateway , creating a single consolidated gateway balance.
This is what enables simplified spending across chains.
 app/api/gateway/deposit/route.ts 
 5) Execute a payout from the Gateway balance 
Once funds are consolidated, you can use Payout to send USDC to recipients on different chains using the Gateway balance.
This is useful for cases like paying vendors or employees with wallets on various networks.
 app/api/payout/route.ts 
 What you can build from this 
You can extend this into:
 Cross-border payroll systems 
 Stablecoin neobank backends 
 Marketplace payout engines 
 AI-native financial agents 
 Treasury automation tools for startups 
 From demo → production 
As you extend this, think in terms of:
 Reliability (retry logic, monitoring)
 Security (permissions, approvals)
 Observability (logs, audit trails)
 Build something with it 
If you end up building on top of this starter, we’d love to see it.
This repo is meant to be forked, modified, and turned into real products.
👉 Get started building with the repo 
‍
 Sample apps provided for demonstration and educational purposes only, is intended for testnet use only, and is not production-ready. 
 Arc testnet is offered by Circle Technology Services, LLC (“CTS”). CTS is a software provider and does not provide regulated financial or advisory services. You are solely responsible for services you provide to users, including obtaining any necessary licenses or approvals and otherwise complying with applicable laws. 
 Arc has not been reviewed or approved by the New York State Department of Financial Services. 
 The product features described in these materials are for informational purposes only. All product features may be modified, delayed, or cancelled without prior notice, at any time and at the sole discretion of Circle Technology Services, LLC. Nothing herein constitutes a commitment, warranty, guarantee or investment advice. 
 USDC is issued by regulated affiliates of Circle. See Circle’s list of regulatory authorizations . 
 Circle Technology Services, LLC (“CTS”) is a software provider and does not provide regulated financial or advisory services. You are solely responsible for services you provide to users, including obtaining any necessary licenses or approvals and otherwise complying with applicable laws. For additional details, refer to the Circle Developer terms of service . 
Related posts
AMP: Rethinking Block Building with Multi-Proposer Consensus
ChainBench: An LLM Benchmark for Multichain Code Generation
How Kura Is Using USDC to Reach Haiti's Last Mile

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
