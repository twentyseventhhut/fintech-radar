---
title: "This Week in Fintech: Blockchains gain speed and wallet infrastructure"
date: 2025-09-09
tags:
  - company/fireblocks
  - industry/blockchain
  - industry/infrastructure
  - region/global
  - type/commentary
sources:
  - https://usa.visa.com/solutions/crypto/deep-dive-on-solana.html
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sbf5ce6bc
month: 2025-09
enriched: false
---

# This Week in Fintech: Blockchains gain speed and wallet infrastructure

> [!info] 2025-09-09 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Blockchains have improved orders of magnitude and are now able to process thousands of transactions per second, with some blockchains like Polygon and Solana having sub-second payment finality for cents — competing on par with established networks like ACH/ Card networks — and making them useful for moving money in real-world use cases. Wallet infrastructure has become significantly easier to access, with advances like multi-party computation lowering barriers for mainstream adoption by making it easier for developers to integrate out-of-the-box custody solutions. Providers like Fireblocks, BitGo and Privy have built solutions which make it easy to custody assets.

## Первоисточники

### usa.visa.com
<https://usa.visa.com/solutions/crypto/deep-dive-on-solana.html>
*1482 слов · direct*

A deep dive on Solana, a high performance blockchain network
 
 Solana's blockchain network has attributes like high transaction throughput and scalability at low cost that help make it a good candidate for payments and Visa’s stablecoin settlement pilot. 
Written by Mustafa Bedawala and Arjuna Wijeyekoon.
Acknowledgement to Cuy Sheffield, Eduardo Lopez, Catherine Gu, Mert Ozbay, and Anuj Sisodiya.
09/11/2023
Blockchain networks have long been proposed as new innovative payment rails. However, for many years they have struggled to scale to support secure, high throughput, low-cost transactions that payment companies require, and consumers expect. Over the past year, our team at Visa has been closely following the technical innovation behind blockchain scalability and are encouraged by the significant progress made with both new “layer 2” networks on top of Ethereum, as well as alternative blockchain networks built from the ground up. Our goal has been to deeply understand the technical properties of blockchain networks and experiment with how we can leverage them to help enhance our existing network as well as build new products for commerce and money movement. 
While we believe that there will likely be multiple blockchain networks that the payments ecosystem will use, we see potential for the Solana blockchain network to become one of the networks that could help power mainstream payment flows.  It holds promise for payments due to its speed, scalability and low transaction costs, helping to make it a good candidate for efficient blockchain settlement rails using stablecoins like USDC. The Solana blockchain network incorporates a number of key features and novel innovations that are worth unpacking for anyone interested in payment technologies.
Transaction throughput at the scale of Visa
 Parallel Transaction Processing: Foundational to its high transaction throughput design, Solana can process transactions in parallel, helping to greatly enhance the network’s efficiency. Transactions impacting separate accounts can be executed simultaneously, enabling Solana to efficiently support payment and settlement scenarios where transactions occur primarily between two distinct parties or where a single party pays out to many other parties. 

In Solana, smart contracts, called programs, can also execute in parallel. Transactions specify the state or accounts they interact with, allowing validators to run non-conflicting transactions simultaneously. Unlike other chains such as Ethereum, which use a single-threaded model, Solana employs a multi-threaded approach to enable parallel transaction execution. In simple terms, while blockchains like Bitcoin and Ethereum process transactions sequentially, Solana's architecture allows for multiple transactions to be processed simultaneously. This design helps prevent congestion in one part of the network from affecting overall network performance.
Low and predictable transaction costs that help drive payment efficiencies
 Figure 1. Average transaction fee in USD 
This image illustrates the average transaction fees, measured in USD, for Bitcoin, Ethereum, and Solana. Notably, it highlights the distinct fee dynamics among these digital assets. Over the past 12 months, as depicted graphically, Bitcoin and Ethereum have experienced significant fee volatility driven by fluctuations in market demand or gas fees within their respective networks. For instance, both Bitcoin and Ethereum witnessed substantial fee spikes, exceeding $15 USD in the case of Bitcoin during May 2023 and surpassing $20 USD for Ethereum. In stark contrast, Solana's fee structure remains stable, consistently below $0.001 USD, thanks to its innovative local fee market system, which ensures predictability and affordability for users. The average transaction fee in the image is based on a 7DMA (7-day moving average).
 Figure 2. Comparing fee markets: Solana vs. Ethereum and other gas-based networks 

The image contrasts Solana and Ethereum's and other gas-based network fee markets. On the left, Solana's parallel processing depicts multiple threads. When one thread congests, only its account's fees rise, ensuring fee stability elsewhere. On the right, Ethereum's single-threaded design is shown. Global congestion affects the entire network, causing widespread fee spikes.
Transaction finality expected by consumers
Transaction finality measures how quickly users can expect their actions to be confirmed on a blockchain network. For payments, time to transaction confirmation is just as important as network throughput. For instance, Ethereum averages about 12 TPS; however, due to gas limits and smart contract requirements during times of congestion, users can experience minutes of wait time before transactions are confirmed. Solana targets a slot time of 400 milliseconds, though it can range from 500 to 600 milliseconds in practice.²
A vast majority of applications on Solana use “optimistic confirmation” for their finality. Optimistic confirmation is a mechanism used on the Solana blockchain to achieve finality without waiting for all validators — or entities responsible for producing blocks —to vote on a block. With optimistic confirmation, a block can be considered finalized if validators representing more than two-thirds of delegated stake validators have voted on it, and no blocks which have been optimistically confirmed have ever been rolled back or failed to finalize. This mechanism allows Solana to achieve finality in a much shorter time than many other blockchains. The rapid speed of transaction completion can enable better payment experiences.  In comparison, Bitcoin may take up to 60 minutes for six additional blocks to be created before transactions are considered secure and final.
 Table 1: Blockchain confirmation time in blocks and seconds/minutes 
Solana (USDC)
1
~0.4 seconds
Avalance (USDC, EUROC)
1
~2 seconds
Flow (USDC)
1
~2.5 seconds
Algorand (USDC)
1
~5 seconds
Stellar (USDC)
1
~5 seconds
TRON (USDC)
19
~1 minute
Arbitrum (USDC)
300
~3 minutes
Ethereum (USDC, EUROC, ETH)
12
~3 minutes
Polygon PoS (Bridged USDC)
372
~20 minutes
 * The number of blocks you wait before considering a transfer valid is called the "confirmation number", which is typically different for different chains. Circle APIs use the confirmation numbers mentioned in the table for each supported chain. 
 Source: Visa | Data: Circle as of Aug. 31, 2023 
Availability: Large number of nodes and multiple validator clients
A payments network can only be effective if it is always available to initiate and execute a transaction at the very moment a user needs to make a payment.  For blockchain networks, availability is best measured by the number of independent participants or nodes that jointly operate the network to make it available for consumers to initiate transactions. As of July 2023, the Solana network boasts an impressive 1,893 active validators—entities responsible for producing and voting on blocks. Additionally, there are 925 more nodes called RPC nodes, which may not create blocks themselves but maintain a local record of transactions.³ A high number of nodes in a blockchain network enhances its resilience and redundancy. If some nodes encounter issues or go offline, the network can still function without data loss, as long as an adequate number of nodes remain operational. Solana community likewise pays attention to diversity of node geography and infrastructure provider to make the network is more robust against events such as natural disasters or change in access policy by the provider. The Solana network has nodes in over 40 different countries and hundreds of unique hosting arrangements and distinct locations.⁴ This helps ensure a smooth and reliable operation, even in the face of technical challenges.
Validator clients are software tools that enable node operators to act as validators on a proof-of-stake blockchain. The diversity of validator clients boosts a network's resilience. While one client might have bugs or vulnerabilities, another may not. This ultimately reduces the odds of a single software flaw crippling the network.  Solana originally operated with one validator client from Solana Labs. In August 2022, Jito Labs introduced a second one for Mainnet, the Jito-Solana. Soon after, Jump Crypto unveiled Firedancer (in testing stage), an independent C++ validator client. Firedancer stands out for its potential to bring substantial performance enhancements, as evidenced by a live demo that achieved 600k TPS.⁵ The aim of having different validator clients is to keep the network stable. Outside Ethereum, Solana is one of the only chains to have multiple, fully independent validator clients.
Meeting modern demands
Solana's unique technological advantages, including high throughput with parallel processing, low cost with localized fee markets and high resiliency with a significant number of nodes and multiple node clients, work together to create a scalable blockchain platform with a compelling value proposition for payments. These are some of the reasons that we decided to expand our stablecoin settlement pilot to include transactions over the Solana network. As we pilot our stablecoin settlement functionality on Solana, we plan to test whether Solana has the ability to meet the demands of modern corporate treasury operations.
 This article is part of a series on Blockchain ecosystem developments. Head over to Visa Crypto Thought Leadership for more consumer insights, best practices and innovative approaches to the blockchain through our research. To learn more about our involvement in the crypto ecosystem and the products we are currently building, reach out to GDLVisaCryptoResearch@visa.com 
 Footnotes 
 Solana blockchain explorer. Numbers include real TPS, excluding voting TPS. 
 Blockchain explorer, Solana Explorer. 
 Number of node count. 
 Solana Validator Metrics. 
 Firedancer announcement by Jump Crypto.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
