---
title: "Stripe-backed Tempo launches stablecoin transaction framework"
date: 2026-01-05
tags:
  - company/tempo
  - company/stripe
  - industry/stablecoins
  - region/global
  - type/product
sources:
  - https://www.fintechwrapup.com/p/deep-dive-stripe-and-circle-are-launching
  - https://www.bitget.com/news/detail/12560605116570
  - https://fortune.com/crypto/2025/10/17/stripe-paradigm-tempo-series-a-5-billion-thrive-capital-greenoaks-joshua-kushner
status: tagged
n_mentions: 3
channels:
  - "The Fintech Blueprint"
  - "This Week in Fintech"
story_id: se1b56896
month: 2026-01
enriched: false
---

# Stripe-backed Tempo launches stablecoin transaction framework

> [!info] 2026-01-05 · 3 упоминаний · 2 источника(ов) с текстом
> Каналы: The Fintech Blueprint, This Week in Fintech

## Агрегированный текст (из дайджестов)

[The Fintech Blueprint] The crypto payments space has two other massive, integrated models vying for control: Stripe’s Tempo and Circle’s Arc. But all three players have their own core focuses, at least for now.Source - Fintech Wrap Up

[This Week in Fintech] Tempo raised $500 million at $5 billion valuation.

[This Week in Fintech] 🌍 Stripe-backed Tempolaunched a blockchain-native transaction framework designed specifically for stablecoins

## Первоисточники

### fintechwrapup.com
<https://www.fintechwrapup.com/p/deep-dive-stripe-and-circle-are-launching>
*1335 слов · direct*

Deep Dive: The Great Stablecoin Chain Grab: Circle’s Arc vs. Stripe’s Rumored “Tempo”
The payments world is watching. If Circle and Stripe prove custom blockchains can meaningfully reduce costs and speed settlement, expect others to follow. MastercardNet? PayPalChain? 
 Imagine sipping coffee with a fellow fintech nerd when they drop this bombshell, “Did you hear Stripe and Circle are both building their own Layer-1 blockchains?” It sounds crazy, but it’s true. In the past few months, payments giant Stripe (yes, that Stripe) and stablecoin issuer Circle have each unveiled plans for custom L1 blockchains – Stripe’s project reportedly called “Tempo” and Circle’s chain known as “Arc.” This is like Visa and PayPal each deciding to build their own version of Ethereum. What’s going on here, and why now? Let’s break it down. 
 Fintech Wrap Up is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber. 
Circle lit the fuse 
In August 2025, Circle (the company behind USDC) announced Arc, an open Layer-1 blockchain purpose-built for stablecoins and financial apps. Arc isn’t just another general-purpose chain; it’s explicitly designed as “the home for stablecoin finance”. Key features? Arc will be EVM-compatible but with some big twists:
 USDC as native gas - Arc uses USDC (a $1.00 stablecoin) to pay transaction fees instead of a volatile crypto token. That means fees are low, predictable, dollar-denominated – no more worrying about gas prices spiking 10x overnight. Circle even built a variant of Ethereum’s fee model (EIP-1559) that smooths out volatility by averaging usage over time, so businesses can budget for fees in dollars. 
 Deterministic finality & low latency - Arc’s consensus (code-named Malachite ) achieves sub-second final settlement. In plainer terms, once a transaction is in an Arc block, it’s 100% final and irreversible within <1 second. No probabilistic confirmations, no waiting for 6 blocks. It uses a high-performance BFT (Byzantine Fault Tolerant) engine (informed by Tendermint) instead of Ethereum’s probabilistic approach. This means no chain re-org surprises – a transaction is either unconfirmed or permanently confirmed. For payments, that certainty is gold. 
 Opt-in privacy - Unlike fully-transparent public chains, Arc will offer selective privacy features. Confidential transfers are on the roadmap, letting users shield transaction amounts while keeping parties’ addresses visible. Think of it like a fintech version of “hide the dollar amount, but not who paid whom.” Importantly, it’s opt-in and comes with compliance knobs – e.g. “view keys” that authorized auditors or regulators can use to see the details. Under the hood, Arc starts with Trusted Execution Environments (TEE) to encrypt transactions fast, and leaves room for fancier cryptography (MPC, ZK proofs) as they mature. The goal is privacy with compliance – no more broadcasting your entire balance sheet to the world, but still being able to prove things to those who need to know. 
 MEV mitigation - Arc’s designers are very aware of the scourge of MEV (Maximal Extractable Value), where bots and insiders exploit transaction ordering for profit. The Arc litepaper literally classifies MEV as “constructive” vs. “harmful” – arbitrage that aligns prices is okay, sandwich attacks and front-running your trades? Not so much. Arc’s roadmap includes measures to tame the bad MEV, like encrypted mempools, batch transaction processing, and multi-proposer mechanisms to keep the playing field fair. In non-dev speak, they want to prevent the usual crypto shenanigans that siphon value from regular users, making Arc’s markets more boring (in a good way) and reliable for serious finance. 
 Institutional validators (at least to start) - Here’s the slightly spicy part – Arc is launching with a permissioned Proof-of-Authority validator set. Translation a hand-picked roster of known, reputable institutions (think regulated financial players) will produce blocks, rather than an open, anonymous free-for-all. Circle calls it “a limited number of known, established, and geographically distributed institutions held to high standards” . These validators are likely big firms with reputations to lose (and compliance audits to pass), which Circle argues deters malicious behavior. Over time, they may broaden participation (perhaps moving toward a permissioned PoS model), but don’t expect a fully permissionless, anyone-can-spin-up-a-node vibe here. This setup aligns with Circle’s goal of “institutional-grade” infrastructure – the network is decentralized in the sense of multiple independent institutions globally, but it’s certainly not decentralized like Bitcoin or Ethereum. (Cue the Crypto Twitter debates on whether Arc is an “L1” or just a consortium chain in disguise!) 
 Programmability for FX, assets, and more - Arc isn’t just a vanilla chain that moves USDC around. Circle is baking in a whole suite of financial primitives for developers. For one, Arc plans a built-in FX engine – essentially an on-chain foreign exchange marketplace. Think 24/7 atomic swap of stablecoins with an RFQ (Request-for-Quote) system hooking into market makers. Two businesses could do a payment-versus-payment (PvP) trade of, say, USDC for EURC (Euro stablecoin) instantly on Arc, with the protocol handling price quotes and settlement. Circle will start it off permissioned (only vetted players providing liquidity) for compliance and deep liquidity, but the long-term vision is to open it up once it’s robust. Arc also natively supports multiple stablecoins and tokenized money from day one – not just USDC, but things like EURC (Euro Coin) and even USYC (Circle’s tokenized US Treasury fund shares). This means Arc could be a playground for on-chain treasury management – companies parking cash in a yield-bearing fund (USYC) and using it as collateral or for instant lending on Arc. And speaking of collateral, Circle clearly has Real World Assets (RWAs) in mind. Arc will enable issuance and trading of tokenized securities (think stocks, bonds, funds) in partnership with regulated entities. Essentially, Arc is aiming to be the all-in-one money layer, stablecoins, FX, yield, and tokenized assets all composing together under one roof. 
 In short, Circle looked at today’s blockchains and said, “These aren’t built for serious money. So we built our own.” Arc is currently in development (private testnet in 2025, with public testnet by fall and mainnet beta slated for 2026). It’s an ambitious attempt to create the ideal chain for global payments and finance. 
In Stripe-land 
Meanwhile, in Stripe-land… things are a bit more hush-hush but equally intriguing. Stripe hasn’t officially unveiled “Tempo” in a glossy blog post – the news leaked via job postings and insider reports. According to a (now-deleted) Stripe job listing, Tempo is an Ethereum-compatible, high-performance L1 blockchain focused on payments. It’s reportedly being built in partnership with crypto VC firm Paradigm and was in “stealth mode” with a small team of engineers as of mid-2025. Stripe’s crypto moves so far give us clues that they acquired a stablecoin platform called Bridge in late 2024 (for a whopping $1+ billion) and a crypto wallet startup (Privy) in 2025. They’ve also rolled out support for merchants to accept stablecoin payments (initially using partners like Paxos/Bridge to handle conversion and custody). So why stop there? It appears Stripe wants to own the entire payments stack, right down to the settlement layer. If Arc is the “money network” blockchain, think of Stripe’s Tempo as aiming to be the “commerce network” blockchain – deeply integrated with checkout, merchant accounts, and shopping experiences.
While details are scant until Stripe formally breaks cover, industry chatter paints a picture of what Stripe’s L1 might entail:
 Commerce-first design - Stripe’s DNA is all about making payments dead simple for merchants and developers. So Tempo would likely be invisible to end-users. Analysts speculate Stripe will need to offer things like gasless transactions (so neither shoppers nor merchants touch crypto), guaranteed FX rates at the point of sale, and instant conversion of stablecoins to fiat for merchants. In other words, swipe your card (or scan a QR) and behind the scenes, a stablecoin might travel over Tempo, but the merchant still feels like they got paid in dollars or euros like usual. 
Keep reading with a 7-day free trial
Subscribe to Fintech Wrap Up to keep reading this post and get 7 days of free access to the full post archives.

### bitget.com
<https://www.bitget.com/news/detail/12560605116570>
*527 слов · direct*

Tempo Introduces Crypto-Native Transactions to Scale Stablecoin Payments On-chain
 Quick Breakdown  
 Enables enterprise-grade stablecoin payments with batching, concurrency, and scheduled transactions 
 Allows network fees to be paid in supported stablecoins, reducing friction for users and developers 
 Integrates biometrics-based authentication and partner infrastructure to support real-world payment use cases 
 
 Tempo has introduced Tempo Transactions, a blockchain-native transaction framework designed to deliver enterprise-grade payment functionality for stablecoins, addressing structural limitations that have long constrained onchain payment systems. 
 The new transaction type is purpose-built for high-volume stablecoin settlement, enabling lower costs, greater flexibility, and operational efficiency closer to traditional financial infrastructure. Tempo Transactions allow network fees to be paid in supported stablecoins and introduce native capabilities such as batching, concurrent execution, fee sponsorship, scheduled payments, and passkey-based biometric authentication, including FaceID. 
 
 Introducing Tempo Transactions: a native onchain transaction type for real-world payments. 
 Rolling out soon on infrastructure partners including @turnkeyhq , @privy_io , @crossmint , and @FireblocksHQ . 
 Learn more in our blog: # 
 — tempo (@tempo) December 17, 2025 
 

 As stablecoins increasingly underpin 24/7 global settlement, Tempo said the framework is intended to move blockchain payments beyond basic transfers and toward full-scale financial operations, including payroll, subscriptions, mass payouts, and complex enterprise workflows. 
 Protocol-native payments for stablecoins 
 Unlike general-purpose blockchains that rely on external tooling to support enterprise use cases, Tempo embeds payment primitives directly at the protocol level. Structured transaction data, atomic execution, and concurrent workflows are native features that allow developers to coordinate multiple payments within a single transaction flow. 
 According to Tempo, this architecture significantly reduces development overhead by eliminating the need for custom infrastructure layers. The network is optimized for low-latency, high-throughput execution, positioning it for adoption by banks, fintech firms, and enterprises that deploy stablecoins for real-world payments. 
 Partnerships signal enterprise push 
 To support adoption, Tempo is working with infrastructure providers including Privy, Turnkey, Fireblocks, and Crossmint. The partners are integrating Tempo Transactions to enable advanced payment functionality for developers building on the network. 
 Privy CEO Henri Stern said native support for batching, fee sponsorship, and transaction metadata materially improves the developer experience for blockchain payments. Turnkey CEO Bryce Ferguson noted that compatibility with both Ethereum-style transactions and Tempo’s EIP-2718-based format enables existing applications to migrate without re-architecting their systems. 
 The launch follows Tempo’s recent ecosystem expansion , including a strategic partnership with institutional digital asset services firm BitGo, as the network intensifies its focus on enterprise and financial institution adoption. 
 
 

 

Disclaimer: The content of this article solely reflects the author's opinion and does not represent the platform in any capacity. This article is not intended to serve as a reference for making investment decisions.
You may also like
Middle East Conflict Ignites Safe-Haven Frenzy! USD Bulls Hit 16-Month High Amidst Gold's Long-Short Tug-of-War

Warsh’s First Battle! New Fed Chair Caught in the Crossfire of "High Inflation" and "Political Pressure"

New Zealand Dollar gains on easing risk aversion

Trump’s Post Shocks the World! U.S.-Iran Deal in Sight as Oil Plunges and Asian Stocks Rally

Trending news
Akash Network rallies 25% – Can AKT bulls push toward $1?
Middle East Conflict Ignites Safe-Haven Frenzy! USD Bulls Hit 16-Month High Amidst Gold's Long-Short Tug-of-War
Crypto prices

### Прочие ссылки (без извлечённого текста)

- <https://fortune.com/crypto/2025/10/17/stripe-paradigm-tempo-series-a-5-billion-thrive-capital-greenoaks-joshua-kushner>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
