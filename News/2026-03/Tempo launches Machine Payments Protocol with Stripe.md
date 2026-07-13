---
title: "Tempo launches Machine Payments Protocol with Stripe"
date: 2026-03-18
tags:
  - company/tempo
  - company/stripe
  - industry/agentic-commerce
  - industry/stablecoins
  - region/us
  - type/product
sources:
  - https://open.substack.com/pub/samboboev/p/deep-dive-mastercard-verifiable-intent
  - https://tempo.xyz
  - https://fortune.com/2026/03/18/stripe-tempo-paradigm-mpp-ai-payments-protocol
  - https://www.ledgerinsights.com/stripe-paradigm-launch-tempo-blockchain-alongside-machine-payments-standard
status: tagged
n_mentions: 4
channels:
  - "Connecting the Dots in Fintech"
  - "Fintech Wrap Up"
  - "This Week in Fintech"
story_id: s021dc9e5
month: 2026-03
enriched: false
---

# Tempo launches Machine Payments Protocol with Stripe

> [!info] 2026-03-18 · 4 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Fintech Wrap Up, This Week in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] Stripe-backed start-up Tempo has launched a new Machine Payments Protocol, designed to let AI agents send and receive money across both fiat and crypto rails.

[Connecting the Dots in Fintech] 🇺🇸 Stripe-backed crypto startup Tempo releases AI payments protocol, launches blockchain. Dubbed the “Machine Payments Protocol,” the open-source network supports payments in both fiat and cryptocurrency. The protocol is also compatible with Stripe’s existing AI payments infrastructure.

[Fintech Wrap Up] Mastercard Verifiable Intent vs Visa Trusted Agent Protocol

[This Week in Fintech] 🌍 Paradigm and Stripelaunched a new Payment Standard for AI Agents — known as MPP, short for “Machine Payments Protocol”

## Первоисточники

### open.substack.com
<https://open.substack.com/pub/samboboev/p/deep-dive-mastercard-verifiable-intent>
*565 слов · direct*

Deep Dive: Mastercard Verifiable Intent vs Visa Trusted Agent Protocol
Agentic commerce breaks a core assumption of online payments, that a human is directly clicking “buy” on a trusted surface. Once software can browse, decide, and transact, merchants and networks lose the simplest security primitive: “the customer was here.”
That creates three concrete trust failures that show up as operational costs:
Merchants need a way to distinguish a legitimate, user-authorized agent from malicious automation and bot traffic, without rewriting their stack or blocking valuable sessions by accident.
Payment networks and issuers need a deterministic audit trail of what the user authorized, what the agent did, and what the merchant charged, so disputes and fraud decisions can anchor to evidence rather than inference.
Agents need a portable way to carry proof of authority across merchants, devices, and protocols, in both human-present and human-not-present execution modes.
Both proposals are “trust layers,” but they sit in different parts of the stack and they optimize for different verifiers.
Fintech Wrap Up is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Mastercard Verifiable Intent as a credential chain for authorization proof 
Verifiable Intent (VI) is built as a layered credential format: a cryptographic delegation chain that binds identity, intent, and action using SD-JWT and key binding, with role-scoped selective disclosure.
 The spec frames two execution modes: 
 Immediate mode is human-present. The user signs final checkout and payment values. The specification treats this as a two-layer flow, with short-lived Layer 2 credentials. 
 Autonomous mode is delegated. The user signs constraints up front, binds an agent key, and the agent later produces fulfillment credentials within those bounds. The spec treats this as a three-layer flow and makes constraints normative in that path. 
The mechanics matter because Verifiable Intent is not just an “agent header.” It is a composable evidence object that multiple parties can verify independently.
 Layer 1 is an SD-JWT issued by an issuer and provisioned into a credential provider wallet, binding user identity to a public key via cnf.jwk. The normative format specifies ES256 and a long lifetime on the order of a year, plus issuer key discovery through JWKS. 
 Layer 2 is created and signed by the user key bound in Layer 1. It expresses purchase intent either as final values (Immediate) or as constraint-bearing mandates and an agent key binding (Autonomous). Layer 2 also binds to Layer 1 via sd_hash. 
 Layer 3 exists only in Autonomous mode. The agent signs short-lived, key-bound SD-JWTs that present fulfillment details. The format splits L3 into a network-facing payment mandate (L3a) and a merchant-facing checkout mandate (L3b). The split is not aesthetic; it enforces a privacy boundary by construction. 
Constraints are treated as first-class authorization limits. The constraints spec defines eight registered constraint types and requires verifiers to support them. It also defines how unknown constraint types behave under strictness modes, and it explicitly calls out that unknown types in open mandates must be rejected because they can silently unbound authority.
This is where Verifiable Intent is opinionated: it tries to turn “intent” into machine-checkable bounds, and it makes the verifier do explicit constraint validation against fulfillment artifacts like the merchant-signed checkout object.
Keep reading with a 7-day free trial
Subscribe to Fintech Wrap Up to keep reading this post and get 7 days of free access to the full post archives.

### Прочие ссылки (без извлечённого текста)

- <https://tempo.xyz>
- <https://fortune.com/2026/03/18/stripe-tempo-paradigm-mpp-ai-payments-protocol>
- <https://www.ledgerinsights.com/stripe-paradigm-launch-tempo-blockchain-alongside-machine-payments-standard>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
