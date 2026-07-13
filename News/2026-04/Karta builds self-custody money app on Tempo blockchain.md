---
title: "Karta builds self-custody money app on Tempo blockchain"
date: 2026-04-27
tags:
  - company/karta
  - company/tempo
  - industry/blockchain
  - industry/stablecoins
  - region/us
  - type/product
sources:
  - https://tempo.xyz/blog/karta-is-building-its-self-custody-money-app-on-tempo
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s72c1975b
month: 2026-04
enriched: false
---

# Karta builds self-custody money app on Tempo blockchain

> [!info] 2026-04-27 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Karta is building its self-custody money app on Tempo, using its payments-focused blockchain for fast, on-chain settlement. The setup enables real-time transactions, stablecoin-based fees, and scalable card payments, supporting global users and upcoming product launches.

## Первоисточники

### tempo.xyz
<https://tempo.xyz/blog/karta-is-building-its-self-custody-money-app-on-tempo>
*538 слов · direct*

Karta, a self-custody money app with more than 25,000 monthly cardholders and 1,250+ business teams across 150+ countries, is building on Tempo. Karta’s treasury is live on Tempo today, and Karta Personal launches on Tempo soon. Read the full Karta case study → 
Karta is a self-custody money app: a Visa card accepted in 150+ countries, fiat virtual accounts available in the US today with expansion underway globally, and one wallet to earn, spend, and send across currencies.
Karta’s uses Privy for self-custody wallets, Bridge for fiat rails and virtual accounts, and Tempo for settlement. Privy’s embedded wallets manage keys, signing, and authorization policies in the background, so Karta can deliver a seamless self-custodial experience that still meets the reliability requirements of real-time payments.
Building self-custody payments at consumer scale
Onchain card products have historically had to navigate a set of constraints that traditional payment infrastructure does not face. According to Karta, four are material:
 Gas. On a general-purpose chain, every transaction requires a native gas token. Users have to acquire that token before they can move the asset they actually care about.
 Per-transaction signing. In a pure self-custodial model, every transaction requires a live signature from the wallet owner. Asynchronous flows like card authorizations cannot pause while a user opens an app to approve.
 Finality as a fraud surface. Seconds-long finality creates a window for double-spend attempts and race conditions that millisecond-level card authorization flows cannot tolerate.
 Structured metadata. Reconciliation, compliance, and dispute resolution depend on per-transaction context. Rebuilding that from event logs is fragile.
Each of these has been solved individually on different chains. Paymaster contracts abstract gas. Session keys and account abstraction approximate asynchronous signing. Emerging rollups approach sub-second finality. Specialty payment chains expose structured metadata.

 At Karta, self-custody isn’t a feature, it’s the architecture. Every user holds their own stablecoin balance on their own wallet, and every transaction they make settles on-chain. Doing that at consumer scale was only possible on infrastructure built for payments, not retrofitted for them. Tempo is the first chain where we didn’t have to trade self-custody for a product that actually works. 
 — Nik Zimarkov, Co-founder and CEO, Karta 

How Tempo addresses these constraints
Tempo is a payments-purpose-built chain. Each constraint above maps to a native Tempo capability.
 Sub-second deterministic finality. Transactions finalize on-chain in approximately 500ms with no re-orgs, inside standard card authorization windows.
 Stablecoin-native gas. Gas is paid in USD stablecoins at the protocol level. No native gas token, no paymaster contracts, no ERC-4337 retrofits.
 Access Keys. A protocol-level primitive for authorized debits against a wallet without custody transfer. Card authorizations can settle asynchronously against an on-chain balance without a live wallet signature at authorization time.
 Dedicated payment lanes. Payment traffic has guaranteed blockspace at the protocol level, insulated from unrelated network activity.
 Structured memo fields. Native per-transfer metadata, ISO 20022-compatible, supports reconciliation and compliance workflows.
Karta’s treasury is live on Tempo today. Karta Personal launches on Tempo soon, alongside fiat virtual account expansion to new markets. Karta Business migrates onto the same settlement layer shortly after.
Get started
Tempo is incubated by Stripe and Paradigm and built for payment use cases like Karta’s: card issuance, treasury operations, and consumer payments.
 Read the Karta case study →

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
