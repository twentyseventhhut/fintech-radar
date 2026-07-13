---
title: "TRM Labs: North Korea hackers took 76% of 2026 crypto hack value"
date: 2026-05-05
tags:
  - company/trm-labs
  - industry/crypto
  - industry/fraud-risk
  - region/global
  - type/research-report
sources:
  - https://www.trmlabs.com/resources/blog/north-korea-stole-76-of-all-crypto-hack-value-in-2026-with-just-two-attacks
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s896c6bf7
month: 2026-05
enriched: false
---

# TRM Labs: North Korea hackers took 76% of 2026 crypto hack value

> [!info] 2026-05-05 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] 🌍 TRM Labsfound that North Korea-linked hackers accounted for 76% of all crypto hack value stolen in 2026, across just two attacks.

## Первоисточники

### trmlabs.com
<https://www.trmlabs.com/resources/blog/north-korea-stole-76-of-all-crypto-hack-value-in-2026-with-just-two-attacks>
*2107 слов · direct*

Please be vigilant about TRM impersonation scams, especially those claiming to assist with fund recovery. More info 
North Korea Stole 76% of All Crypto Hack Value in 2026 — With Just Two Attacks
Key takeaways
North Korean hackers, from two distinct groups, stole approximately USD 577 million in 2026 YTD — 76% of all crypto hack losses through April, across just a handful of attributed incidents.
The Drift Protocol hack (USD 285 million, April 1) involved three weeks of pre-attack staging and months of  social engineering to compromise protocol signers, executing the full drain in approximately 12 minutes.
The KelpDAO hack (USD 292 million, April 18) exploited a single-verifier design flaw in a LayerZero bridge, then laundered proceeds through THORChain after USD 75 million was frozen on Arbitrum.
The two attacks show diverging laundering playbooks: Drift, after an initial cross-chain speedrun to Ethereum, is dormant; KelpDAO pivoted to Bitcoin via THORChain after Arbitrum froze a portion of the funds and is now in the midst of a textbook TraderTraitor liquidation process.
THORChain processed the vast majority of proceeds from both the Bybit breach (2025) and the KelpDAO hack (2026), converting hundreds of millions in stolen ETH to Bitcoin with no operator willing to freeze or reject transfers — making it the consistent bridge of choice across North Korea's largest heists.
TRM's Beacon Network — whose 30+ members include both major exchanges and DeFi protocols — enables immediate cross-platform alerts when North Korea-linked funds reach participating institutions, before withdrawals clear.
North Korea's cumulative crypto theft now exceeds USD 6 billion attributed incidents since 2017.
{{horizontal-line}}
North Korean hacking groups accounted for 76% of all crypto hack losses in 2026 through April — not because North Korea launched a wave of attacks, but because two attacks totaling USD 577 million dwarfed everything else. The Drift Protocol breach on April 1 (USD 285 million) and the KelpDAO bridge exploit on April 18 (USD 292 million) represent 3% of 2026 incident count and 76% of stolen value. That ratio — small number of attacks, outsized share of losses — has characterized North Korea's approach across most years since 2017.
North Korea's share of crypto theft has accelerated, not plateaued
North Korea's share of total crypto hack losses has grown from under 10% in 2020 and 2021 to 22% in 2022, 37% in 2023, 39% in 2024, and 64% in 2025. The 2026 figure of 76% through April is the highest sustained share on record.
The 2025 spike was driven almost entirely by the Bybit breach in February — USD 1.46 billion extracted from a cold wallet via a compromised Safe{Wallet} signing interface. Bybit remains the largest single crypto hack in history. Following that, KelpDAO and Drift together now represent one of largest North Korean hauls in any comparable window.
What has not changed is the attack cadence. North Korea's premier hacking teams run a small number of precisely targeted operations each year rather than a sustained high-volume campaign. Two attacks account for 76% of all 2026 hack value to date. The group is not attacking more frequently — it is targeting more precisely, focusing on high-value targets.
What has changed is the sophistication of the attacks themselves. TRM analysts have begun to speculate that North Korean operators are incorporating AI tools into their reconnaissance and social engineering workflows — a development consistent with the increasing precision of attacks like Drift, which required weeks of targeted manipulation of complex blockchain mechanisms, rather than North Korea’s traditional emphasis on simple private key compromises.
Drift Protocol: USD 285 million stolen and still sitting dormant
TRM's initial investigation attributed the Drift Protocol attack to North Korean hackers. TRM analysts assess the threat actor as a North Korean group distinct from TraderTraitor; the specific subgroup attribution remains under investigation. On-chain staging began March 11, with a single 10 ETH withdrawal from Tornado Cash. The campaign against Drift began much earlier, however, and involved in-person meetings between North Korean proxies and employees of Drift over a period of months. These in-person meetings may be unprecedented in North Korea’s lengthy crypto hacking campaign. 
The technical mechanism exploited a Solana-native feature called a durable nonce. Standard Solana transactions expire within roughly 90 seconds if not confirmed on-chain. Durable nonces extend that window indefinitely, allowing a transaction to be pre-signed and held before broadcast — a feature designed for offline hardware signing. Between March 23 and March 30, the attacker created durable nonce accounts and induced Drift's Security Council multisig signers into pre-authorizing transactions using this mechanism. On March 27, Drift migrated its Security Council to a new 2/5 threshold configuration with zero timelock — a change the attacker subsequently exploited. In parallel, the attacker manufactured CarbonVote Token (CVT) — a fictitious asset seeded with a small amount of liquidity and inflated through wash trading — which Drift's oracles treated as legitimate collateral.
On April 1, the pre-signed transactions were deployed: 31 withdrawals executed in approximately 12 minutes, draining real assets including USDC and JLP. Most of the stolen funds were bridged to Ethereum within hours of the theft, see below. The stolen ETH has not moved since the day of the theft. The responsible group — assessed as distinct from TraderTraitor - tends to take a more measured and cautious approach to laundering its heists. TRM anticipates a months or years-long liquidation of the Drift proceeds.  
KelpDAO: USD 292 million moved rapidly through the same infrastructure North Korea used in Bybit 
The KelpDAO breach on April 18 targeted its rsETH LayerZero bridge on Ethereum. The attackers first compromised two internal RPC nodes, swapping out the node software to make them report false blockchain data. They then launched a distributed denial-of-service (DDoS) attack against external, uncompromised RPC nodes, forcing the bridge's verifier to fail over to the two poisoned internal nodes. Those nodes falsely reported that rsETH had been burned on the source chain when no such burn had occurred. The single verifier, reading from the compromised data source, confirmed the fraudulent cross-chain message as legitimate. The attacker drained approximately 116,500 rsETH — worth approximately USD 292 million — from the Ethereum bridge contract.
The single-DVN (Decentralized Verifier Network) configuration is the defining vulnerability. LayerZero's security model supports configuring multiple independent verifiers for cross-chain message validation; KelpDAO's rsETH deployment used only one — the LayerZero Labs DVN. With no second verifier required to agree, a single poisoned data source was sufficient to approve a fraudulent transaction at scale.
TRM Labs’ has attributed this exploit to North Korea based on on-chain analysis of both the pre-funding for the hack and the subsequent laundering . Notably, a portion of the initial funding for the exploit was traceable as far back as 2018 to a Bitcoin wallet controlled by Wu Huihui, a Chinese crypto broker indicted in 2023 for laundering Lazarus crypto thefts. Other funds used to finance the attack were sourced more directly to the BTCTurk hack, another recent TraderTraitor theft.
Two hacks, two laundering strategies
Drift and KelpDAO demonstrate distinct laundering approaches shaped by different operational conditions.
Drift laundering — speed coupled with patience
The stolen tokens were converted to USDC via Jupiter, bridged to Ethereum, and swapped into ETH — distributed across fresh wallets before going dormant. The stolen ETH has not moved since the day of the theft. The responsible group — assessed as distinct from Lazarus Group — follows a well-documented North Korean pattern: hold proceeds for months or years, then execute a structured, multi-phase cashout.
KelpDAO laundering — resilience first
After the theft, the TraderTraitor hackers almost inexplicably left approximately 30,766 ETH on Arbitrum, an L2 with far higher centralization than Ethereum. The Arbitrum Security Council exercised emergency powers to freeze these ETH (worth roughly USD 75 million) — an action that awoke the hackers and triggered a mad laundering scramble. Approximately USD 175 million in ETH — a portion of the unfrozen total —  were swapped to Bitcoin, mostly through THORChain, a cross-chain liquidity protocol with no KYC requirement. Umbra, an Ethereum privacy tool, was also used to obscure some wallet linkages before the conversion to Bitcoin.
So far, the KelpDAO laundering process is unfolding according to the well-worn TraderTraitor playbook. The ongoing laundering phase is handled almost entirely by Chinese intermediaries, not the North Koreans themselves. 
What compliance teams need to monitor
Four monitoring priorities follow from the 2026 pattern.
THORChain flows from KelpDAO-linked addresses
KelpDAO is the latest in a long string of North Korean heists to route proceeds through THORChain. In 2025, the vast majority of stolen Bybit funds were converted from ETH to BTC via THORChain between February 24 and March 2 — an unprecedented surge in cross-chain volume that the protocol processed without intervention. KelpDAO followed the same playbook in April 2026: approximately USD 175 million in ETH moved through THORChain after the Arbitrum Security Council froze a portion of the stolen funds.
THORChain's developers and validators claim it is a decentralized protocol with no central operator and that it cannot reject transactions or centrally disable the platform. Recent statements on X by project members suggest this is not, or has not, always been the case. For North Korea, it functions as a reliable, high-capacity exit ramp: assets enter as ETH and emerge as BTC.
Exchanges receiving BTC inflows from THORChain pools should screen against known KelpDAO and Lazarus Group address clusters. TRM Wallet Screening covers North Korea-attributed addresses across Ethereum, Solana, TRON, and Bitcoin, with updates propagated as attribution is confirmed. Attribution for specific KelpDAO addresses is ongoing — retroactive re-screening in 30 days will capture addresses labeled after the initial response.
Solana multisig and governance contract exposure
The Drift attack targeted governance infrastructure, not application logic. Protocols using Solana Security Council multisig with durable nonce authorization should treat this as a template attack that will be replicated. Exchanges with Solana DeFi deposit exposure should flag inflows from bridge contracts used in the Drift dispersal — including specific Jupiter and Wormhole routes identified in TRM Transaction Monitoring.
Multi-hop bridge deposit screening
Both KelpDAO and Bybit involved bridge or cross-chain infrastructure as the attack surface or laundering route. Bridge-to-exchange flows are a priority monitoring channel for North Korean proceeds. First-hop address screening alone will not catch funds that passed through intermediary wallets before reaching an exchange. Multi-hop analysis across the full transaction chain is required.
Beacon Network enrollment for real-time North Korea alerts
Both of the major 2026 North Korean hacks targeted DeFi protocols — and DeFi protocols are now Beacon Network members alongside major exchanges including Coinbase, Binance, Kraken, OKX, and Crypto.com. When investigators flag attacker-controlled addresses in TRM, Beacon auto-traces funds in real time and sends immediate alerts across all 30+ member platforms. Individual screening catches known addresses; Beacon Network closes the gap between attribution and action — converting a screening lag measured in days into an alert measured in minutes.
{{horizontal-line}}
Frequently asked questions (FAQs)
1. Why does North Korea account for such a disproportionate share of crypto hack losses?
North Korea’s elite hacking teams run a small number of high-precision attacks against large infrastructure targets rather than a high volume of smaller exploits. In 2026 YTD, two incidents accounted for 76% of all tracked hack losses. North Korean hackers also increasingly invest heavily in pre-attack staging — the Drift campaign involved three weeks of on-chain preparation and months of targeted social engineering — and target environments where a single vulnerability produces nine-figure outcomes, such as bridge validator networks and multisig governance contracts.
2. What is a durable nonce, and why did it matter in the Drift attack?
A durable nonce is a Solana feature that extends the validity window of a pre-signed transaction from roughly 90 seconds to an indefinite period. It is designed for scenarios where hardware wallets need to sign transactions offline before broadcasting later. The Drift attacker exploited this by getting authorized signers to pre-authorize transactions that appeared routine at signing time. On March 27, Drift migrated its Security Council to a new configuration with zero timelock — a change that eliminated a safeguard the attacker subsequently exploited. When the pre-signed transactions were broadcast on April 1, the conditions needed to execute the drain were already in place. The signers had approved transactions weeks earlier without knowing the context in which they would be used.
3. How does THORChain factor into North Korean laundering?
THORChain is a nominally decentralized protocol that enables native cross-chain swaps — exchanging ETH for BTC, for example, without a custodian or KYC requirement. Almost unique among large cross-chain protocols, THORChain refuses to consider freezing or “censoring” incoming transactions from known illicit actors, allowing groups like North Korean hackers to

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
