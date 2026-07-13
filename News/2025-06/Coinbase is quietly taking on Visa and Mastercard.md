---
title: "Coinbase is quietly taking on Visa and Mastercard"
date: 2025-06-29
tags:
  - company/coinbase
  - industry/crypto
  - industry/payments
  - region/us
  - type/commentary
sources:
  - https://www.popularfintech.com/p/coinbase-is-quietly-taking-on-visa-and-mastercard-a85f4594920b297f
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sa6f16ab4
month: 2025-06
enriched: false
---

# Coinbase is quietly taking on Visa and Mastercard

> [!info] 2025-06-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Coinbase is quietly taking on Visa and Mastercard

## Первоисточники

### popularfintech.com
<https://www.popularfintech.com/p/coinbase-is-quietly-taking-on-visa-and-mastercard-a85f4594920b297f>
*1970 слов · direct*

Home 
 Posts 
 Coinbase is quietly taking on Visa and Mastercard 
 Coinbase is quietly taking on Visa and Mastercard 
 The company's new protocol brings stablecoins closer to everyday commerce 
 Jun 21, 2025 
 Hey! 
 On Tuesday, the U.S. Senate passed the GENIUS Act, a new law that sets clear rules for stablecoins in the U.S. It allows not just banks and Fintech companies, but also retailers to issue their own stablecoins . The market reacted quickly: Visa and Mastercard shares dropped about 3%, while Coinbase and Circle jumped more than 10%. 
 The message was clear: investors now see stablecoins as a serious challenge to Visa and Mastercard's dominance in payments. At first, I was skeptical. Even in the most optimistic scenario, stablecoins seemed far from replacing cards, which offer strong rewards, global acceptance, and solid consumer protections. 
 But later that day, I came across the Coinbase Commerce Payments Protocol , and it made me rethink my thesis. The protocol doesn’t just bring key card features into stablecoin payments. It also lays the foundation for an ecosystem of players who are financially motivated to drive stablecoin adoption in commerce . 
 Maybe stablecoin payments will go mainstream faster than I thought. 
 Let’s dive in! 
 Jevgenijs p.s. if you have feedback, just reply to this email or ping me on X/Twitter 
 On Tuesday, the U.S. Senate passed the GENIUS Act, establishing a legal framework for stablecoin issuance in the U.S. The Act enables banks, Fintech companies, and even retailers to issue stablecoins . The next day, Visa $V ( ▲ 1.05% ) and Mastercard $MA ( ▲ 0.71% ) were down about 3%, while Coinbase $COIN ( ▼ 0.41% ) and Circle $CRCL ( ▼ 5.8% ) booked double-digit gains. 
 The market reaction signalled that stablecoins threaten Visa and Mastercard, and my first reaction was to tweet , “There is still a long way before stablecoins start hurting Visa and Mastercard, even if the most bullish thesis plays out.” While stablecoins hold promise as an alternative payment rail for commerce, cards are considered superior due to well-established incentive structures and robust consumer protection frameworks. 
 However, later in the day, I discovered the Coinbase Commerce Payments Protocol , which made me think that perhaps the adoption of stablecoins in commerce might come faster than I thought . 
 The Coinbase Commerce Payments Protocol introduced several mechanisms that replicate key card functionality and paved the way for the emergence of critical ecosystem participants, such as issuers and merchant acquirers (or rather their onchain equivalents). 
 Image source: Coinbase 
 “Onchain payments work well for peer-to-peer transactions, but not for more complex commerce purchases, which require features like refunds, delayed capture, and tax finalization . For example, in commerce, merchants can run out of inventory and need to cancel a purchase, buyers can request refunds, orders may be completed in multiple deliveries, and more. The Commerce Payments Protocol enables onchain payments for commerce at scale by bridging this gap .” 
 Let’s break down how the protocol works and why it represents a major step towards the adoption of stablecoins in commerce. 
 The Commerce Protocol implements “ authorization ” (placement of a hold on buyer funds) and “ capture ” (distribution of payment to the merchant) by introducing an “ Escrow ” smart contract. At “authorization”, funds move from the buyer to the Escrow, and at “capture”, funds move from the Escrow to the merchant. 
 Image source: Base Engineering Blog 
 “The Commerce Payments Protocol brings Auth+Capture onchain through an Escrow smart contract . To authorize, funds move from buyer to Escrow, guaranteeing the ability to pay merchants. To capture, funds move from Escrow to merchant, finalizing payment. This simple 2-step process unlocks onchain payments for commerce at scale.” 
 The protocol also introduces a concept of an “Operator” , a smart contract that “facilitates movement of funds between the transacting parties and drives payment movement through the Escrow.” In card terms: the blockchain acts as the scheme, the protocol defines the scheme rules, the “Operator” functions like a merchant acquirer , and the “Escrow” serves as the merchant processor. 
 Image source: Base Engineering Blog 
 “…the protocol is not concerned with how the operator is implemented and just recognizes it as an address. Operators could be simple externally-owned accounts or advanced smart contracts. Operators could also be controlled via API to easily integrate with existing commerce workflows.” 
 This setup allows the protocol to implement six payment functions: authorization, capture, charge, void (reversal), reclaim, and refund. 
 Image source: Coinbase 
 “ Each operation updates payment accounting in the protocol, tracking authorized payments available for capture and captured payments available for refund . The protocol enforces that payment transitions only occur in the valid time window defined by the payment’s various expiries.” 
 There is no separate settlement function as in traditional card transactions. Instead, funds are transferred at each stage, first from the buyer to the Escrow, and then from the Escrow to the merchant. 
 There are no chargebacks , representment (merchant dispute of a chargeback), incremental authorization, and MITs (merchant-initiated transactions enabling subscriptions). 
 However, some card functions used in the card world may not be necessary, or may work differently, onchain . 
 For instance, the protocol also includes a “reclaim” function, which returns funds from the Escrow to the buyer if the merchant fails to capture them before the authorization expires. In contrast, with card payments, the authorization hold simply expires, and the reserved funds are automatically released. 
 Another example is subscription payments. Per my understanding, subscriptions (where merchants can regularly pull funds after an initial authorization) could be implemented through mechanisms like “ Token Collectors ”, which are “ pluggable payment modules that handle different authorization methods .” 
 Image source: Coinbase 
 “One of the biggest challenges in building onchain payment infrastructure is the fragmented landscape of token authorization methods. When payers need to authorize spending without directly initiating transactions themselves (enabling gasless, asynchronous, operator-driven experiences) there are multiple competing standards , each with distinct tradeoffs.” 
 Token Collectors implement the logic of collecting buyer authorization, and the protocol doesn’t care how they work as long as the authorization is collected. Coinbase designed the protocol to be “ completely agnostic about token authorization methods ”, which enables innovation in payment instruments without the need for protocol changes. 
 Image source: Coinbase 
 “ ERC-3009, implemented by USDC and several major stablecoins, offers elegant single-signature UX with non-sequential nonces, but isn't widely adopted by most ERC-20 tokens. Permit2 provides universal compatibility with any ERC-20 token but requires an initial setup step per token, creating friction on first use. Spend Limits deliver optimal experiences for specific smart wallet implementations like Coinbase Smart Wallet , but with limited compatibility.” 
 Token Collectors are, in many ways, the onchain equivalent of cards . But in the card world, only the schemes define how cards function and even how they look, as issuers must certify every card product before launch. 
 For example, the Visa Flexible Credential, which supports both debit and credit transactions on a single credential, could only have been developed by Visa. In contrast, the Coinbase Commerce Payments Protocol opens up the development of new payment credentials to third parties. 
 This effectively enables the emergence of onchain equivalents to issuers . Coinbase already plays this role through Coinbase Wallet. Third-party developers can build their own wallets using Coinbase’s Smart Wallet technology. Even fully independent players, like Affirm, Amex, or Chase, could become issuers by creating their own Token Collector . 
 Image source: Coinbase 
 “This abstraction makes the system future-proof and universally compatible. As new authorization standards emerge or wallet technology evolves, developers can simply implement new collectors without modifying the core protocol. ” 
 Finally, the protocol includes a Fee System that allows Operators to charge merchant fees similar to the Merchant Discount Rate in the card world. Merchant Discount Rate is a critical incentive mechanism for merchant acquirers. 
 The Fee System is generic and flexible enough to enable equivalents of interchange (the fee would go to the provider of the Token Collector), and cashback (part of the fee charged to the merchant would be returned to the buyer. 
 The success of Visa and Mastercard is built on strong incentive mechanisms for issuers and acquirers, while also allowing room for consumer incentives. Creators of the Coinbase Commerce Payments Protocol clearly took that into account. 
 Image source: Coinbase 
 Let’s put it all together? 
 Stablecoins solved the volatility problem . They turned crypto from a speculative asset into a usable digital dollar. You can hold them, send them, and now spend them. 
 Base, Coinbase’s Layer 2 chain, solved the speed and cost problem. Transactions on Base are fast and cheap. 
 Finally, the Coinbase Commerce Payments Protocol extended onchain payments beyond simple peer-to-peer transfers, making them viable for complex commerce use cases . 
 More importantly, though, the Commerce Payments Protocol introduced the foundation needed to create an ecosystem of players who are financially incentivized to drive stablecoin payment adoption in commerce. 
 This design mirrors how card networks operate, but it’s permissionless . Merchants, acquirers, and payment instrument issuers are welcome to participate in this ecosystem. That’s the difference. 
 However, adoption still requires a few things: 
 Acceptance 
 Convenience 
 Incentives for consumers 
 …let’s take them one by one. 
 First, merchants need a reason to accept stablecoins. They already have one: lower fees, faster settlement, fewer intermediaries . Especially in cross-border commerce, where cards are painfully expensive. The Commerce Payments Protocol enables merchants to become acquirers (Operators) and define their own rules. 
 Coinbase just announced a partnership with Shopify, and the Wall Street Journal reported that Amazon and Walmart are exploring issuing their own stablecoins . If you take Shopify and Amazon, that’s already over 50% of the commerce volume in the U.S . 
 Image source: eMarketer 
 Second, the payment method has to be convenient for consumers . We are still missing a credit card-like wallet that doesn’t require funding each transaction. But the Commerce Payments Protocol lays the foundation for new types of payment instruments through Token Collectors. 
 I would not be surprised to see a new wave of VC-funded companies pursuing this opportunity. Someone will definitely attempt to become the onchain version of Amex . 
 Store and co-branded cards could also get a second life , as retailers may choose to go beyond just being Operators and become issuers of Token Collector credentials themselves. The Commerce Protocol enables merchants to control the flow end-to-end. 
 Image source: Amazon 
 Third, people need a reason to switch from credit cards . That means rewards, and rewards need funding. In card payments, rewards are funded through interchange, lending (“revolvers” funding rewards for “transactors”), annual fees, affiliate commissions and merchant discounts, as well as marketing budgets. 
 The same applies here. Operators can choose to pass the merchant discount rate (or transaction fee savings) directly to consumers, or partner with wallet issuers to drive adoption, effectively creating a new form of interchange . They can also fund rewards through lending, annual fees, and affiliate commissions. 
 But there is one addition…stablecoins earn yield on reserves. That yield is an additional source of funding for cashback, points, or discounts . 
 Image source: Coinbase 
 Visa and Mastercard aren’t going anywhere. But for the first time, a serious alternative is taking shape. There is, of course, a scenario where Visa and Mastercard become the dominant Operators, and Chase and Amex become the largest issuers of wallets . 
 But would you bet on this? 
 Cover image source: Coinbase 
 Disclaimer: The views expressed here are my own and do not represent the views of my employer. The information contained in this newsletter is intended for educational and informational purposes only and should not be considered financial advice. You should do your own research or seek professional advice before making any investment decisions. Read the full disclaimer here . 
 Keep Reading 
 Popular Fintech 
 Become a smarter Fintech founder, operator, and investor

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
