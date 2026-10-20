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
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s665d436e
month: 2026-10
enriched: true
importance: 4
freshness: fresh
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
**[0] What happened.** On 2026-10-15 identity company Proof (CEO Pat Kinsel) launched **x401**, an open protocol that lets any website challenge an AI agent to prove (a) which verified legal person it represents and (b) that the person cryptographically authorized the specific action. Three pieces are live: Proof's agent identity wallet, the x401 HTTP protocol, and a production MCP server working with Meta's Muse, ChatGPT, Grok and Claude. Proof demoed it with [[Proof and Circle demo AI agents paying in USDC at Money20 20]] at Money20/20 Las Vegas (Oct 18–21, Booth #5069).

**[1] What x401 actually is (mechanics).** x401 extends HTTP status 401 (Unauthorized) the same way x402 extends 402 (Payment Required): a server returns a 401-style challenge specifying the evidence it needs — e.g. a verified legal name/age/nationality claim at a required assurance level, plus a signature over the exact transaction terms (amount, recipient, source account). The consumer approves on-device via biometric; a hardware-protected key signs, binding an X.509 credential (issued by Proof's WebTrust-audited CA after Kantara-certified NIST IAL2 proofing) to the terms. If any signed detail changes, verification fails. Proof's framing: it closes the "Agent Evidentiary Gap" — the distance between what an agent *can* do (valid OAuth token / API key / card) and what a business can *prove* the human approved. x401 was first published June 2026 with contributors from Visa, Circle, Okta.

**[2] Where it sits in the agentic stack (relation to x402 and rivals).** x401 = identity + authorization; **x402** = payment. x402 (Coinbase-originated May 2025, HTTP 402, pay-in-USDC-on-Base) was moved to the **Linux Foundation x402 Foundation** on 2026-04-02 with 22+ members (Visa, Mastercard, Stripe, Google, AWS, Circle, Coinbase, Shopify). Proof deliberately designed x401 to *compose* with x402 (identity → authorization → payment) rather than replace it, and uses x402 itself to meter identity "per claim." x401 is also designed to interoperate with **AP2** (Google's Agent Payments Protocol) and Mastercard's **Verifiable Intent**, both donated to the **FIDO Alliance** (Apr 2026, 60+ orgs, new Agentic Auth + Payments working groups). Competitive neighbors: **Skyfire** (KYAPay "Know Your Agent", signed JWTs, $9.5M raised, partnered with **Visa Intelligent Commerce / Trusted Agent Protocol** in Dec 2025 alongside Nekuda/PayOS/Ramp); **Mastercard Agent Pay** (tokenized agent credentials + AI-fraud scoring); **Sumsub KYA**, **Incognia AI Agent Detection**. See internal cluster: [[Sumsub expands Know Your Agent framework with KYA Module for MCP]], [[Skyfire and Forter partner to secure AI-powered commerce at checkout]].

**[3] Why now / the trigger.** Catalyst was the Sep 2026 Meta Muse episode: Muse (an agent that completes purchases) hit #1 on the US App Store, Shopify wired Shop Pay, then on Sep 21 Amazon blocked Muse for not identifying itself and moving through accounts without consent — exposing that nobody can verify on whose behalf an agent acts. Tailwinds: Cloudflare found bots = 57% of web requests (Jun 2026, first time above human traffic); HUMAN Security reported AI-agent traffic +7,851% in 2025. Regulatory opening: Sep 8 2026 FinCEN + Fed/FDIC/NCUA/OCC updated CIP guidance to accept digital certificates / verifiable credentials (incl. from non-government third parties) for customer identity verification — directly legitimizing Proof's model. US ESIGN Act + UETA already attribute electronic-agent transactions to the person bound.

**[4] Adoption: live vs announced.** LIVE: three capabilities in production today; reference implementation for Cloudflare Workers + guides for Node/Python/Go; developers can self-serve basic claims (age/country/email) with no sales process. Named early adopter in production: **Superfluid** (tokenized-market settlement infra) — first live x401 implementation in its Superfluid Wallet, announced Sep 2026. Everything else is announced/roadmap: Proof *intends* to place x401 under neutral independent governance and publish operating-rules/liability proposals (not yet done). The Circle USDC flow is a *demo*, not a shipped integration. Net read: strong spec + one real production user + a marquee demo, versus x402's ~69k active agents / 165M txns / ~$50M volume by Apr 2026 — x401 is early-stage adoption riding a credible, standards-aligned architecture.

**FRESHNESS: fresh.** Launch 2026-10-15; this note dated 2026-10-20 within the launch news cycle. Companion note [[Proof and Circle demo AI agents paying in USDC at Money20 20]] (Oct 19 demo) is a distinct, later event — same vendor, different story, NOT a duplicate. No prior x401-launch note exists in the base.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. "First to put verified identity + authorization for agents into production" — is that an objective milestone or vendor-defined? Skyfire's KYAPay and Visa TAP shipped (beta) in Dec 2025; the claim likely hinges on the narrow phrase "verified *legal* identity + signed authorization."
2. Production adoption is essentially ONE named customer (Superfluid), itself a small tokenized-markets infra firm. Is there any volume, or is this a spec launch dressed as a product launch?
3. "Open protocol" + plan to move to "neutral independent governance" — but governance is not yet established and Proof is the sole CA/issuer today. How open is it really if Proof controls proofing, issuance and the WebTrust CA?
4. x401 depends on MCP + specific assistants (Muse, ChatGPT, Grok, Claude). What happens if those platforms adopt a rival (AP2/Verifiable Intent natively, or Visa TAP)? Is x401 a thin layer easily disintermediated?
5. x402 has Linux Foundation + 22 heavyweight members; x401 has "contributors" (Visa, Circle, Okta) but no foundation. Is Proof trying to ride x402's legitimacy without comparable backing?
6. NIST IAL2 proofing is high-friction (government ID + biometric enrollment). Does mass consumer enrollment realistically happen, or does friction cap this to high-value flows only?
7. Does the FinCEN/banking guidance actually permit reliance on a third-party issuer like Proof, or does it still require the institution to independently assure the issuer applies equivalent authentication (i.e., does Proof remove the bank's work or just add a step)?
8. Business model risk: metering identity "per claim" over x402 assumes claims cost cents and volume is huge. Is the unit economics proven, or aspirational?
9. Interop claims with AP2/Verifiable Intent/FIDO are "designed to" — is there a working, tested integration, or just stated intent? Standards fragmentation risk is real.
10. The Amazon-blocks-Muse framing is Proof's narrative. Did Amazon's block actually stem from identity gaps, or from marketplace/competitive/ToS reasons that x401 wouldn't solve?
11. Liability model is explicitly deferred ("additional proposals addressing operating rules and liability"). Who eats fraud loss if a signed credential is later disputed? Unanswered = adoption blocker for banks.
12. Privacy/selective-disclosure claims vs. a reusable X.509 identity credential tied to one issuer — correlation/tracking risk across relying parties?
13. Is x401 patent-encumbered or royalty-free? "Open" specs can still carry IP claims that deter competing issuers.
14. Can the same outcome be achieved by AP2 mandates alone (Google/Mastercard, FIDO-stewarded, far more backers)? What's x401's durable differentiation beyond "legal identity" vs. "payment intent"?
15. For a daily fintech digest: is this materially different from the companion Circle/USDC demo note, or would covering both double-count one vendor's Money20/20 PR push?

**Importance: 4/5** — Agent identity/authorization is the single hottest unresolved layer of agentic commerce (the whole Oct-2026 Money20/20 news cluster: Visa, Mastercard, Circle, Stripe, Skyfire, Sumsub). Proof's launch is credible, standards-aligned (x402/AP2/FIDO) and regulator-timed (FinCEN CIP). Held below 5 because real adoption is one customer + a demo, governance/liability/economics are unproven, and it competes against far-better-capitalized incumbents (Visa TAP, Mastercard Agent Pay).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Proof's x401 sits in the agentic-commerce *trust/identity* layer — the authorization sub-vertical beneath the payment rails. Market framing (count checkout transactions only, not orchestrated spend): agentic-commerce transaction value is put at ~$8bn in 2026, with Juniper Research projecting ~$3.5tn by 2031 (per Juniper Research, via juniperresearch.com, as of Jun 2026); McKinsey frames the broader orchestrated-spend TAM at $3–5tn of global retail by 2030 (per McKinsey, via stellagent.ai, Oct 2025). Treat these as order-of-magnitude, not comparable bases. **Structure:** fragmented and pre-standard — three competing protocol stacks are forming (payment: x402; authorization: Google/Mastercard AP2 + OpenAI/Stripe ACP), so value is being fought over at the *standards* layer, where the moat is governance neutrality + network adoption rather than product. Entry barriers for the identity piece specifically are high: NIST IAL2 proofing, a WebTrust-audited CA, and X.509 certificate issuance are regulatory/capital-heavy. **Why now:** (1) the Sep 2026 FinCEN + federal banking-regulator CIP guidance expressly recognizing digital certificates/verifiable credentials as a permissible KYC method (per note primary source) — the regulatory unlock that lets banks consume third-party credentials; (2) the "Agent Evidentiary Gap" exposed when Amazon blocked Meta's Muse on Sep 21 2026; (3) bots now exceed human web traffic (57% of Cloudflare page requests, Jun 2026) with AI-agent traffic up 7,851% in 2025 (per HUMAN Security, via note source).

**Competitive landscape.** Sector KPIs: live transactions/volume on the protocol, number of active agents, credential issuances, and ecosystem member count (x402 Foundation: 40+ members at Jul 2026). Proof is positioned not as a payment network but as the *who-authorized-what* evidence layer, explicitly designed to compose with x402 (payment) and to interoperate with AP2/Verifiable Intent (authorization intent). Recent peer/ecosystem moves: Coinbase donated x402 to the Linux Foundation, which launched the x402 Foundation Jul 14 2026 (per linuxfoundation/press, via search); [[Visa launches Trusted Agent Protocol for AI commerce]] (Oct 2025); [[Coinbase x402 protocol logs surge in transactions]]; dedicated agent-identity/wallet startups — Skyfire ("KYA"/KYAPay, ~$9.5m raised; a16z CSX, Coinbase Ventures) and Nekuda ($5m seed; Madrona, Amex & Visa Ventures) — plus [[Basis Theory raises $33 million for agentic commerce]] and [[Paygentic raises $2M pre-seed for AI payments infrastructure]] on the credentials side. Position: Proof is a *first-mover in production* for verified-legal-identity-plus-signed-authorization (claims first-to-production; Superfluid live since Sep 2026) and is materially better capitalized/scaled than the pure-play agent-identity startups. Moat (analysis): switching costs + intangibles — the regulated CA, IAL2 proofing stack, and portable X.509 credential that "belongs to the person, not an institution" and is reusable across relationships; weaker on network effects today (adoption is early).

**Comps & multiples.** Proof (private): last valuation ~$0.9bn, ~$321m total raised (investors incl. Visa, State Farm Ventures); ~425 employees (per PitchBook/Crunchbase, via search). Revenue/ARR not disclosed → EV/Revenue, EV/EBITDA, P/E = no data; price-per-employee ≈ `$0.9bn / 425 ≈ $2.1m/employee` (analysis; a rough scale sanity check, not a valuation multiple). Private-round comps in the same agent-identity/credentials niche (post-money not disclosed; compare on capital raised, not market cap): Skyfire ~$9.5m, Nekuda $5m seed, Basis Theory $33m, Paygentic $2m pre-seed. Relative read: Proof is ~1–2 orders of magnitude larger by capital and the only one carrying a regulated CA — so it is a different class of comp (incumbent identity infra vs. seed-stage rails), **distribution not computed, qualitative comparison**. No public-market peer is a clean comp for the identity-authorization layer specifically.

**Risk flags.**
1. *Standards fragmentation / disintermediation* — x401 is Proof's own proposal and not yet under neutral governance (Proof says it "intends" to hand it off). If the de-facto authorization standard consolidates on AP2 (Google/Mastercard, FIDO-stewarded) or ACP, Proof risks being a credential *issuer plugged into someone else's protocol* rather than owning the layer — margin captured by the protocol/payment stack above it.
2. *Adoption vs. announcement gap* — "live" today = one named production customer (Superfluid) plus demos; x402's own on-chain volume is still tiny (~$28k/day reported), so the surrounding rail is pre-scale. Thin real usage means the network-effects moat is asserted, not yet earned.
3. *Platform/dependence risk* — value depends on websites choosing to *challenge* agents with x401 and on MCP-assistant distribution (Claude, Grok, ChatGPT dots, Muse); if the large platforms (Visa, Mastercard, Google, OpenAI) bundle native identity into their own agent stacks, Proof's open-infra pitch gets squeezed. (Visa is both an investor and a competitor via Trusted Agent Protocol.)

**What this changes (idea-lens).** (analysis) This is a land-grab for the authorization layer of agentic commerce, not a product launch — the thesis is that *payment rails (x402) commoditize first and the scarce, regulated asset becomes verified identity + signed consent*. Falsifiable thesis: if, within ~12 months, x401 is adopted by ≥1 top-tier bank/merchant beyond pilots AND handed to neutral governance, Proof re-rates from "notarization vendor" to "identity infrastructure." Trigger/what breaks it: AP2/ACP absorbing the signed-authorization function natively, or regulators/networks mandating a single credential scheme Proof doesn't control. Watch: who else issues x401-compatible credentials (the spec invites "competing issuers"), and whether Money20/20 (Oct 18–21 2026) converts demos into named production relying parties.

Sources: https://www.proof.com/blog/proof-launches-x401-giving-ai-agents-a-way-to-prove-who-they-represent---and-what-theyre-authorized-to-do · https://pitchbook.com/profiles/company/153145-27 · https://www.crunchbase.com/organization/notarize · https://www.juniperresearch.com/research/fintech-payments/ecommerce/agentic-commerce-research-report/ · https://stellagent.ai/insights/agentic-commerce-market-size-forecast-2030 · https://ecorpit.com/x402-linux-foundation-agent-payments-adopt-decision-2026/ · https://stellagent.ai/insights/agentic-commerce-infra-startups
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
