---
title: "Proof launches x401 protocol to verify AI agents online"
date: 2026-10-20
retrieved: 2026-10-20
tags:
  - company/proof
  - industry/agentic-commerce
  - industry/infrastructure
  - region/us
  - type/product
sources:
  - https://www.proof.com/blog/proof-launches-x401-giving-ai-agents-a-way-to-prove-who-they-represent---and-what-theyre-authorized-to-do
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s665d436e
month: 2026-10
enriched: false
---

# Proof launches x401 protocol to verify AI agents online

> [!info] 2026-10-20 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Proof launches x401, an open protocol letting websites verify who AI agents represent. Consumers can authorize wire transfers, purchases and payment mandates through Proof's agent identity wallet. Its MCP server works with Grok and Claude.

## Первоисточники

### proof.com
<https://www.proof.com/blog/proof-launches-x401-giving-ai-agents-a-way-to-prove-who-they-represent---and-what-theyre-authorized-to-do>
*2095 слов · direct*

Today, Proof became the first company to put verified legal identity and transaction authorization for AI agents into production with the launch of x401, an open protocol that lets any website ask an AI agent to prove who it's acting for and what that person approved. Proof works with Meta's Muse, ChatGPT dots, Grok, Claude and other assistants that support the Model Context Protocol (MCP).
The launch comes weeks after Amazon blocked Muse from its marketplace, exposing a problem every business on the agentic web now faces: There is no reliable way to know who an AI agent is acting on behalf of, or whether that person authorized what it is doing. It also follows September guidance from FinCEN and federal banking regulators recognizing digital certificates and verifiable credentials, under certain conditions, as a permissible way for banks to verify customer identity.
With Proof, a consumer can authorize a wire transfer, approve an itemized purchase or sign a payment mandate through an AI agent. At the center of the launch is Proof’s agent identity wallet. It holds a person’s verified legal identity and lets them approve, on their own device, exactly what their AI agent can do. The agent carries the request; the person’s wallet signs it.The business receiving the request can independently confirm the consumer's verified legal identity and check the cryptographic signature on the transaction itself. If the agent changes the amount, recipient or other signed terms, the signature no longer validates.
Three capabilities are live today: 
Proof's agent identity wallet, which shows the information and transaction terms being requested
x401, an open HTTP protocol for requesting and verifying that evidence 
A production Model Context Protocol (MCP) server that works with AI assistants, including Meta's Muse, ChatGPT dots, Grok and Claude.
Websites can request verified identity claims without a sales process or a negotiated agreement, with the option to pay per claim over x402.
Developers can deploy x401 today using the protocol, identity scheme, implementation guides and reference implementation at proof.com/x401 .
 The problem Amazon exposed: Access is not authority 
On September 8, Meta released Muse, an AI agent capable of completing purchases. It reached No. 1 on the U.S. App Store, and Shopify connected Shop Pay. On September 21, Amazon blocked Muse, citing concerns that the agent did not identify itself, appeared to collect customer credentials, and moved through accounts and transactions without Amazon's knowledge or consent.
An agent may possess a valid password, OAuth token, API key or payment card. None establishes that the person behind it authorized a particular action.
Proof calls this the Agent Evidentiary Gap: the distance between what an AI agent can technically do and what a business can verify the person behind it authorized.
For merchants, that gap creates fraud and dispute risk. For banks, lenders and insurers, it raises questions about legal identity, consent and enforceability. Consumers are wary too: in a survey of 1,000 U.S. consumers by Exploding Topics, 31% said they would not let an AI agent spend any money on its own, and more than half (51%) were uncomfortable with AI tools storing their card details.
 "The agentic web needs a trust layer backed by evidence, and Proof is putting this into production," said Pat Kinsel, founder and chief executive officer of Proof. "Businesses are being asked to accept instructions from software acting for a customer, but they cannot reliably prove who that customer is or what the customer approved. Blocking agents is understandable, but it's not sustainable. We are making verified legal identity and authorization available as open web infrastructure, to anyone, without a sales call." 
 How x401 works: Verify the person. Sign the action. 
Proof's x401 protocol extends HTTP 401, the web's standard unauthorized-response mechanism, allowing a website to specify the evidence an AI agent must provide before proceeding.
A website can request verified identity claims, such as legal name, age or nationality, from trusted issuers at a required level of assurance. It can also request that the consumer cryptographically sign the terms of a specific transaction.
The agent presents that request to the consumer, who authenticates with a biometric on their own device. Proof's wallet shows the information and transaction terms being requested. When the consumer approves, their hardware-protected key signs the presentation, binding their verified legal identity to the specific terms they authorized.
The website verifies the issuer, credential, signature and transaction terms before proceeding. It can retain the signed evidence and independently validate it later if the transaction is disputed.
The distinction is consequential: Proof doesn't merely establish who someone is. It creates verifiable evidence of exactly what they agreed to.
Consider an AI agent instructed to transfer $25,000 from a consumer's bank account. The bank can issue an x401 challenge requiring both verified legal identity and a signature on the wire instructions, including the amount, recipient and source account. The consumer reviews and approves those details on their own device. The bank then verifies the signed instructions, alongside its own existing requirements, before executing the transfer. If any signed detail changes, the evidence fails verification.
Proof supports transaction signing for wire instructions, payment mandates, itemized purchases and developer-defined transaction data, enabling the same infrastructure to protect financial transactions, contracts, account changes and other high-consequence actions.
Proof works with Meta’s Muse, ChatGPT dots, Grok, Claude and other MCP-compatible assistants. Consumers can connect Proof to their assistant and enroll for a credential when one is first requested.
Websites can deploy x401 through a reference implementation for Cloudflare Workers, with guides for Node, Python, Go and other environments. Basic identity claims, including verified age, country of residence and email, can be requested without a sales process or a negotiated agreement.
 x401 meets x402: Identity, authorization and payment over open protocols 
As AI agents increasingly transact across the internet, businesses need to establish three things: who is behind the agent, what that person authorized, and how the transaction gets paid.
Proof designed x401 to work alongside x402, the HTTP-native payment protocol now stewarded by the Linux Foundation, which had more than 40 member organizations as of July 2026, including Visa, Mastercard, Stripe, Google, AWS, Circle and Coinbase.
x401 establishes who is behind a request and can carry cryptographically signed evidence of what they approved. x402 enables the payment.
Together, the protocols give developers a way to combine verified legal identity, signed transaction authorization and payment without requiring either protocol to replace the other.
Proof is also using x402 to transform the economics of identity verification itself.
Historically, identity providers relied on enterprise agreements and billing relationships because collecting payment for a single verification costing cents was impractical. With x402, a website can pay Proof per claim, with no purchase order, invoice or minimum commitment.
A developer can deploy x401 and begin buying verified identity within minutes, so identity can now be metered like bandwidth or compute: one API request, one agent purchase or one machine-signed document at a time.
Payments can now move between machines in seconds. Proving that a verified person approved the underlying transaction is the missing step, and early adopters like Superfluid are already putting it into production.
Superfluid operates the infrastructure that powers continuous settlement for tokenized markets. In September, they announced the first live implementation of x401 with Proof as part of the Superfluid Wallet launch, making them among the first organizations to run it in production.
  “Superfluid Wallet is built for a world where people and their agents act together, where users can understand what they’re authorizing and control exactly what their agent can do. With x401 and Proof, users now have portable, verifiable identities that let the services their agents interact with verify who that agent represents. That’s the foundation agentic commerce needs: agents act for people and people stay in charge, verifiably.” 
  — ZhiCheng Miao, Founder and CEO, Superfluid 
The opportunity is expanding rapidly. In June, Cloudflare data found that bots accounted for 57% of web-page requests on its network, surpassing human traffic online for the first time. HUMAN Security found that AI-agent traffic grew 7,851% in 2025.
 How verified legal identity fits existing law 
U.S. law has recognized transactions formed by electronic agents for more than 25 years. As Proof uses the term, a verified legal identity is a person's identity established from government-issued identity evidence through NIST IAL2 identity proofing and bound to a certificate issued to that person. Under the federal ESIGN Act and Uniform Electronic Transactions Act (UETA), electronic-agent transactions can have legal effect when the agent's actions are legally attributable to the person to be bound.
Proof's signed, tamper-evident evidence of the issuer, assurance level, verified person and authorized action is the kind of evidence that cryptographic attribution enables.
Each verified person holds an X.509 certificate issued by Proof's WebTrust-audited certificate authority following Kantara-certified NIST IAL2 identity proofing, bound to a hardware-protected key. The resulting credential belongs to the person, not an institution, and can be reused across relationships.
When a consumer signs transaction terms, the resulting evidence binds their verified legal identity to those terms. The relying party can verify the cryptographic signatures and certificate chain, and check that the signed instructions match the transaction it was asked to perform.
Selective disclosure allows consumers to share specific identity attributes without exposing their entire identity document. x401 is designed to interoperate with AP2 and Verifiable Intent, the specifications developed by Google and Mastercard and now stewarded by the FIDO Alliance, for recording what a person authorized an agent to do.
On September 8, FinCEN, together with staff from the Federal Reserve, FDIC, NCUA and OCC, updated Customer Identification Program guidance to expressly recognize digital certificates and verifiable credentials—including those issued by nongovernment third parties—as permissible methods of customer identity verification, provided the institution ensures the issuer applies the same level of authentication the institution itself would use. Existing Bank Secrecy Act requirements remain unchanged.
The implications extend beyond commerce. Whether an agent is opening a bank account, authorizing a payment, changing a beneficiary or accepting contractual terms, businesses can request evidence of the verified person and the specific action being authorized, subject to their own Customer Identification Program, onboarding and other regulatory requirements.
 An open protocol for the agentic web 
Proof has published the x401 protocol and identity scheme at proof.com/x401 , including credential formats, issuance, custody, presentation, transaction signing, agent delegation, settlement, claims, offline verification and implementation guides.
The specifications provide the information needed for independent implementations, audits and competing credential issuers.
Proof first published x401 in June 2026 with technical contributors from payments, identity and AI organizations, including Visa, Circle, Okta and others. It intends to place the protocol under neutral, independent governance and publish additional proposals addressing operating rules and liability.
 "We have specified the whole scheme, not just the part that touches our product," Kinsel said. "How identity is proofed, how it is issued, how it is held, how it is presented, how it travels into an agent’s transaction and how it gets paid for — all of it is written down and open. If this is going to be infrastructure, other people have to be able to build it, check our work and disagree with us in public." 
As AI agents take on increasingly consequential tasks, businesses will need more than a valid login or a successful payment. They will need verifiable evidence of the person behind the transaction—and what that person authorized.
Proof is making that evidence available as open internet infrastructure.
Developers can begin at proof.com/x401 . Consumers can set up their agent identity wallet at proof.com/digital-credential . Organizations requiring higher assurance, signed authorization evidence or credential issuance can register with Proof.
Proof will demonstrate the end-to-end experience at Money20/20 in Las Vegas, October 18–21, Booth #5069, and host developer sessions for organizations implementing x401.
Subscribe to our newsletter
Related Articles
Title lorem ipsum
Title lorem ipsum
Title lorem ipsum
Proof and Circle Show How AI Agents Can Prove Who They Act For and Pay in USDC
Proof Launches x401, Giving AI Agents A Way to Prove Who They Represent - and What They're Authorized To Do
The Fraud Files: When Fraud Went Corporate | October 2026
Anatomy of a Fraud Attempt: The Password Reset That Was the Attack
How Businesses Reduce Help Desk Social Engineering Attacks
Candidate Fraud and the Continuity Gap in Remote Hiring
Proof Appoints Jeremiah Glodoveza as Chief Marketing Officer
An AI Just Passed the Video Turing Test. Who's on Your Next Call?
What Makes ID Checks Fail
Anatomy of a Fraud Attempt: the Photograph of a Building Nobody Owned
Can AI Deepfakes Bypass Identity V

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

## Market Research

<!-- enrichment:market_research -->
_(пусто)_
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
