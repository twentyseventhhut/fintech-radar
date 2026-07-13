---
title: "Kaleido explains tokenized deposit models and infrastructure"
date: 2026-06-14
tags:
  - company/kaleido
  - industry/blockchain
  - industry/banking
  - region/global
  - type/research-report
sources:
  - https://www.kaleido.io/blockchain-blog/tokenized-deposits-models-use-cases-infrastructure
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sa17554a0
month: 2026-06
enriched: false
---

# Kaleido explains tokenized deposit models and infrastructure

> [!info] 2026-06-14 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Tokenized Deposits: Models, Use Cases & Infrastructure - Kaleido, accessed May 10, 2026, https://www.kaleido.io/blockchain-blog/tokenized-deposits-models-use-cases-infrastructure

## Первоисточники

### kaleido.io
<https://www.kaleido.io/blockchain-blog/tokenized-deposits-models-use-cases-infrastructure>
*1998 слов · direct*

Tokenized Deposits: Models, Use Cases, and What Banks Need to Build
Key Takeaways
Tokenized deposits represent commercial bank money on a distributed ledger, preserving the existing two-tier monetary system while adding programmability and atomic settlement.
Two primary models exist: account-based and token-based. Each carries distinct tradeoffs for regulatory treatment, interoperability, and technical architecture.
Tokenized deposits are not a replacement for core banking infrastructure. They connect to it via APIs and event-driven workflows, extending settlement and payment rails into programmable environments.
The primary engineering challenge is not token mechanics. It is policy enforcement, key management, and compliance integration at production scale.
Kaleido's enterprise blockchain platform gives financial institutions the infrastructure to issue and govern tokenized deposits without rebuilding their core systems.
Banks built today's payment rails for batch processing and overnight settlement. Correspondent banking networks, SWIFT messaging, and nostro/vostro account reconciliation all reflect an architecture designed before real-time everything became the baseline expectation. The gap between what those rails deliver and what treasury teams, corporate treasurers, and central banks now want is where tokenized deposits enter.
Kaleido's Enterprise Platform gives financial institutions the infrastructure to issue and govern tokenized deposits without rebuilding their core systems. The sections below cover what tokenized deposits are, how they compare to adjacent forms of money, the two dominant structural models, concrete use cases, and what a bank actually needs to build a production-grade system. Learn more about Kaleido's Tokenized Deposit offerings here .
‍
What Are Tokenized Deposits and How Do They Fit in the Money Stack?
Tokenized deposits are on-chain representations of commercial bank deposits. The underlying liability remains on the issuing bank's balance sheet, subject to the same deposit insurance frameworks and prudential regulation that govern any current account balance. What changes is the settlement layer: instead of a debit instruction traveling through correspondent networks, the deposit itself becomes a programmable token that can settle atomically with other on-chain assets.
This distinction matters for how they sit within the broader money taxonomy:
Stablecoins like USDC and USDT are reserve-backed instruments issued by non-bank entities. They sit outside the regulated deposit guarantee system. CBDCs are central bank liabilities. Tokenized deposits occupy a specific and significant position: they are bank money, issued by a regulated institution, carrying the same credit quality and insurance coverage as a conventional deposit, but able to settle programmatically on a shared ledger.
The BIS Committee on Payments and Market Infrastructures, in its 2023 report on the future of the monetary system, explicitly identified tokenized deposits as a mechanism for preserving the two-tier monetary architecture while adding programmability. The report notes that tokenized deposits allow commercial banks to remain at the center of the payment system rather than ceding that role to stablecoin issuers or non-bank digital currency providers.
For a financial institution evaluating the landscape, that framing is the starting point. Tokenized deposits are not a crypto product. They are the bank's existing liability, replatformed for a programmable settlement environment. For a broader look at how tokenization applies across asset classes, see our guide to tokenization for enterprise architects .
Account-Based vs. Token-Based: The Core Architectural Tradeoff
Two structural models dominate how institutions are approaching tokenized deposit implementation. The choice between them determines regulatory treatment, interoperability constraints, and the technical architecture of the ledger.
 Account-based models maintain the ledger as a record of balances associated with identified account holders. The token on-chain is a claim against a balance entry in the bank's core system. When a payment settles, the core banking ledger updates, and the on-chain token reflects that update. Identity and authorization are embedded in the account relationship, not in the token itself.
 Token-based models represent value directly in the token. Possession or control of the private key gives the holder a claim to the underlying deposit. Settlement occurs when the token transfers between wallets, not when a core banking record changes. This model more closely resembles bearer instruments and requires the bank to think carefully about how deposit insurance attaches, how KYC obligations follow the token, and how reversibility is handled in the event of fraud or error.
The right choice depends on a few considerations:
 Choose account-based when: 
Your regulatory environment requires account-holder identity to attach to every balance and transaction at the core banking layer.
You are operating within a closed consortium where counterparties are known and permissioned at the network level.
You need full compatibility with existing core banking reconciliation and reporting infrastructure without a parallel ledger.
 Choose token-based when: 
You need atomic Delivery versus Payment (DvP) settlement with securities or other tokenized assets where a counterparty's core banking system is not on the same network.
You are building toward interoperability across multiple institutions or chains where a shared account ledger is not feasible.
Your jurisdiction's regulatory framework has explicit provisions for bearer digital instruments, as some jurisdictions governed by eWpRV (Germany's electronic securities registry law) already do.
In our work deploying tokenized asset infrastructure at Tier 1 and Tier 2 financial institutions, we find that most institutions start with an account-based model for regulatory simplicity and evolve toward token-based settlement for specific use cases like cross-border DvP. The architecture needs to accommodate both, because a bank that locks into one model in year one will face a costly rebuild when the second use case arrives.
Tokenized Deposit Use Cases: Where the Model Creates Real Value
The case for tokenized deposits is clearest in contexts where today's payment rails create measurable friction. Three use cases consistently surface across the institutions we work with.
 Cross-Border and Cross-Currency Settlement 
Correspondent banking chains introduce latency and cost that are well documented. A SWIFT cross-border payment can take one to five business days and pass through two or three correspondent banks, each adding fees and creating reconciliation obligations. The BIS has reported that correspondent banking fees on some corridors exceed 6% of transaction value, with settlement times stretching beyond 24 hours for emerging market currencies.
Tokenized deposits on a shared permissioned ledger or connected public chain allow two banks to settle directly in central bank money equivalents without a correspondent intermediary. Payment netting, FX conversion, and settlement confirmation all happen within a single atomic transaction. For a corporate treasury moving $50 million in payroll across eight jurisdictions, the difference between T+3 and T+0 settlement is a material working capital question.
 24/7 Liquidity and Repo Markets 
Traditional repo markets operate within fixed settlement windows. Tokenized deposits enable intraday repo: a bank can post tokenized deposits as collateral, receive tokenized securities, and unwind the position within hours rather than days. This is not theoretical. The European Central Bank's trials of wholesale CBDC settlement and the Banque de France's DL3S system have demonstrated atomic settlement of repo-style transactions between central bank accounts and commercial bank instruments, with settlement confirmed in seconds rather than overnight.
 Programmable Payments and Supply Chain Finance 
When payment is conditional on an event, tokenized deposits enable the condition to be enforced at the smart contract layer without a payment instruction traveling through a separate rail. A supplier receives payment at the moment a logistics oracle confirms goods delivery. An escrow releases at contract execution. A coupon payment on a tokenized bond triggers against a verified rate index. Each of these patterns removes a manual confirmation step and the operational risk that comes with it. 
How Tokenized Deposits Are Represented On-Chain
At the technical layer, a tokenized deposit can be represented under several token standards, and the choice has downstream consequences for compliance and interoperability.
 ERC-20 is the baseline fungible token standard. It works for simple transfer and settlement but carries no native compliance enforcement. A bank issuing deposits under ERC-20 needs to enforce KYC and transfer restrictions at the contract level through custom extensions, because the standard itself does not require identity checks on sender or receiver.
 ERC-1400 and its sub-standards were designed for security tokens and carry partitioned balances, forced transfer capabilities for regulatory intervention, and document attachment. They are a closer fit for deposit instruments that need built-in operator control.
 ERC-3643 (T-REX) combines on-chain identity registries with transfer rules. Every transfer validates the receiver's identity claim before the token moves. For a bank that needs to ensure deposits only settle to counterparties who have passed KYC and sanctions screening, this standard enforces that check at the protocol layer rather than relying on a manual off-chain gate.
In our deployments, the standard that fits depends on the counterparty set and the regulatory obligations. A bank-to-bank wholesale deposit network with a closed set of permissioned participants may use a simpler custom standard with role-based access control. A retail-adjacent or multi-institution network where identity needs to follow the token uses ERC-3643 or an equivalent identity-linked pattern.
Regardless of standard, the representation also needs to address how the on-chain balance reconciles with the core banking ledger. The deposit token is not the deposit itself; it is a representation. Every mint event, transfer, and burn needs a corresponding entry in the issuing bank's system of record. That reconciliation loop, driven by event-driven webhooks and idempotency keys to guarantee exactly-once processing, is where most of the integration engineering sits.
What a Financial Institution Needs to Build Tokenized Deposits
A tokenized deposit program is not a smart contract project. It is an integration project. The token mechanics take a fraction of the engineering effort. The rest goes to key management, policy enforcement, compliance integration, and connecting on-chain events back to core banking systems.
The production requirements break down across four areas:
 Key Management and Custody 
Every wallet holding a tokenized deposit balance needs a signing key. At institutional scale, that means hundreds or thousands of wallets, each managed under a governance framework that specifies who can authorize transactions, under what conditions, and with what approval chain. Hardware Security Modules (HSMs) are mandatory for keys holding material balances. In our Key Manager, we support a Remote Signing Module (RSM) that deploys co-located with the HSM and validates policy before any signing operation reaches the hardware. Supported HSM vendors include Thales Luna, Entrust, Fortanix, IBM OSO, and all major cloud HSM providers.
 Policy Enforcement 
Transfer restrictions for tokenized deposits go beyond simple allowlists. A policy engine needs to evaluate source and destination wallet identity, transaction value and velocity limits, asset type, sanctions screening results, and jurisdictional classification before a transaction signs. Kaleido's Policy Manager uses Open Policy Agent (OPA) with Rego policies, evaluated at the RSM before the transaction reaches the HSM. Policy changes themselves require approval before taking effect, which means the governance layer governing the policy is auditable.
 Compliance Integration 
AML screening cannot be an afterthought. A tokenized deposit that settles before sanctions screening completes creates regulatory exposure. The workflow engine needs to gate transaction signing on the result of a screening call to Chainalysis, TRM Labs, or Elliptic, with a configurable hold window if the result is inconclusive. This check needs to happen within the transaction lifecycle, not as a parallel process that might complete after settlement.
 Core Banking Reconciliation 
Every on-chain event must write back to the issuing bank's core system. Mints, transfers, and burns each produce a ledger entry. That event stream, delivered via Apache Kafka or webhook, feeds the bank's general ledger, regulatory reporting system, and treasury management platform. The integration is not optional and it is not simple. In our work with Tier 1 banks, reconciliation architecture consistently takes longer to design and test than the smart contract layer.
How Kaleido Supports Tokenized Deposit Programs
Kaleido's platform covers the infrastructure layer that sits between a bank's existing systems and the blockchain network. We do not replace core banking systems. We connect to them.
A tokenized deposit program built on Kaleido gets:
 Smart Contract Manager for deploying, versioning, and managing the deposit token contract lifecycle, with auto-generated typed REST APIs from any contract ABI.
 Key Manager with HSM integration and the RSM for pre-signing policy enforcement across hot, warm, cold, and air-gapped signing tiers.
 Policy Manager with OPA/Rego-based programmable rules evaluated before any transaction signs, supporting M

## Контекст

<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_(пусто)_
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->
