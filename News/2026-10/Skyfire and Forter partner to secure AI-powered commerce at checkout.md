---
title: "Skyfire and Forter partner to secure AI-powered commerce at checkout"
date: 2026-10-20
retrieved: 2026-10-20
tags:
  - company/skyfire
  - company/forter
  - industry/agentic-commerce
  - industry/fraud-risk
  - region/us
  - type/partnership
sources:
  - https://www.businesswire.com/news/home/20261019685711/en/Skyfire-and-Forter-Enrich-Trusted-Agentic-Commerce-Decisions-at-Checkout
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s55c58006
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Skyfire and Forter partner to secure AI-powered commerce at checkout

> [!info] 2026-10-20 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Skyfire and Forter partner to strengthen trust in AI-powered commerce at checkout. The collaboration combines Skyfire’s infrastructure for AI agent payments with Forter’s fraud prevention and decisioning technology to help merchants identify trusted AI-driven transactions. Read more.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261019685711/en/Skyfire-and-Forter-Enrich-Trusted-Agentic-Commerce-Decisions-at-Checkout>

## Контекст

<!-- enrichment:context -->
### [0] What happened
On 2026-10-19 (businesswire), **Skyfire** — an identity-and-payments infrastructure startup for AI agents — and **Forter** — a $3B-valued digital-commerce fraud/trust-intelligence platform — announced an integration that feeds Skyfire's **Know Your Agent (KYA)** token/identity signals into Forter's **Fraud Management for Agentic Commerce** product. Goal: let merchants *approve* legitimate agent-driven purchases at checkout instead of blanket-blocking them as bots, while still catching fraud disguised as "trusted agent" traffic. The identity signals slot into Forter's existing real-time risk decisioning — no merchant checkout-UI changes or extra verification steps. Piloted with **Jomashop** (online luxury watches/jewellery retailer). Quotes from Craig DeWitt (Skyfire co-founder/Head of Product), Eran Vanounou (Forter CTO), Osher Karnowsky (Jomashop GM).

### [1] Why it matters
Legacy bot-management is binary: it blocks automation. But consumer AI agents (Meta Muse, ChatGPT checkout, Grok shopping) now shop *on behalf of* real buyers and trip the same anti-bot signals → false declines on genuine orders, while fraudsters mimic agent traffic. KYA-as-fraud-signal reframes agent identity from "block/allow bot" to "whose authorized agent is this + what's their provenance," which is the missing input Forter's risk engine lacked. It is the fraud/decisioning layer of the broader agentic-commerce stack (identity → authorization → payment).

### [2] Key numbers / scope
- Agentic order volume on Forter's network: **>4x (quadrupled) since August 2026**; automated fraud reportedly **doubled** over the preceding ~2 months.
- Forter: ~**$525M raised** (Bessemer, Sequoia), **~$3B** last valuation, **400k–500k+** business network, **>2 billion** digital identities, **>$2T** historical transaction volume processed.
- Skyfire products: KYA (agent identity/provenance verification, "KYC for agents"), **KYAPay** open protocol (launched 2025-06), agentic wallet, "Buy for Me," USDC instant settlement / micropayments.
- Status: **announced 2026-10-19**; Jomashop cited as an active pilot/customer — live-GA language is NOT explicit (treat as early/pilot, not proven at scale).

### [3] Dated timeline
- **2025-06-26** — Skyfire launches open KYAPay protocol with Agent Checkout.
- **2025-12-18** — Skyfire demos agentic purchase via KYAPay + **Visa Intelligent Commerce**.
- **2026-10-01** — **Mastercard** adds trust/probability signals to its **Agent Pay** framework, built *in partnership with Skyfire* (and Cloudflare) — a major prior validation of Skyfire's KYA.
- **2026-10-19** — Skyfire × Forter integration announced; Money20/20 week (Las Vegas, Oct 18–21).

### [4] Internal links & ecosystem
Related notes: [[Crossmint launches Agent Commerce Toolkit for AI payments]], [[Proof launches x401 protocol to verify AI agents online]], [[Glance partners PayPal for AI-powered shopping and checkout]], [[Musk proposes shopping via credit card photos on Grok]].
Competitive/standards landscape: Visa **Trusted Agent Protocol (TAP)** + Intelligent Commerce (w/ Cloudflare), **Mastercard Agent Pay** / Agentic Tokens (also uses Skyfire), **Google/Mastercard AP2**, **Stripe** Agent Toolkit + Issuing, Cloudflare CDN-layer agent ID. NOTE: Skyfire is the identity/payment layer; Forter is the fraud-decisioning layer — complementary, not head-to-head with the card networks.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
1. Is the Forter integration actually GA, or just a single-pilot (Jomashop) with marketing gloss? No explicit "generally available" language was found.
2. Does "agentic orders quadrupled since August" and "fraud doubled" come from Forter's own PR? Both metrics are vendor-sourced and unaudited — off a tiny base?
3. Is this a *new* partnership or an *expansion*? Some coverage says Skyfire "widens/expands" existing Forter checks — how much is genuinely new vs re-announced for Money20/20?
4. What's the exclusivity? Forter can ingest other agent-identity signals (Visa TAP, Cloudflare, Mastercard) — is Skyfire's KYA preferred, default, or one of many?
5. Does KYA actually prove *consumer authorization* (what the human approved), or only agent *provenance/identity*? Proof's x401 explicitly targets the "did the person authorize this" gap — KYA may not.
6. Conflict/overlap: Skyfire also powers Mastercard Agent Pay trust signals (2026-10-01). Do Mastercard and Forter become competing consumers of the same KYA data, and does that create channel conflict?
7. Adoption breadth: only one named merchant. How many of Forter's 400k+ businesses have turned this on? Likely near-zero at announcement.
8. Revenue model: who pays — merchant, Forter, or the agent? No pricing disclosed; unclear if this is monetized or land-grab.
9. Standards risk: if Visa TAP / Mastercard Agentic Tokens / Google AP2 win as the identity standard, does Skyfire's proprietary KYA get commoditized or bypassed?
10. Fraud-signal reliability: can a sophisticated fraudster obtain/forge a KYA token or replay a legitimate agent's identity? What's the revocation/assurance level vs Proof's NIST IAL2 approach?
11. Measurement: any disclosed lift in approval rate or drop in false declines from the Jomashop pilot? None found — claims are directional, not quantified.
12. Dependency: Forter's value is its own 2B-identity network; is KYA additive signal or does it risk over-weighting a thin, new agent-identity dataset?
13. Timing/hype: announced Money20/20 week alongside many agentic-commerce launches (Proof x401, Crossmint, Glance/PayPal) — is this differentiated or me-too?
14. Durability: card networks could build native agent-identity-to-fraud signals (Mastercard already did Oct 1), potentially disintermediating a standalone KYA-to-fraud integration.

### Importance: 3/5
Credible, well-positioned deal between two real players (Forter $3B; Skyfire already tied to Visa + Mastercard) that fills the fraud-decisioning gap in agentic commerce — a hot, fast-growing theme. Capped at 3/5: single-pilot adoption, vendor-sourced metrics, no pricing/GA confirmation, and heavy competition from card-network-native approaches. Strategically notable, not yet materially proven.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic-commerce infrastructure (AI agents that discover, decide and pay at checkout) + the fraud/trust layer bolted onto it. Market-size estimates diverge wildly by definition: Juniper Research ~$8bn global in 2026 and ~$3.5tn transaction value by 2031; IDC $38.2bn (2026); Grand View $7.7bn (2026) — per secondary citations, as of Oct 2026 (treat as directional, not a clean TAM). Structure: early-stage and fragmented — rail/protocol players (Skyfire KYA/KYAPay, Visa Trusted Agent/Intelligent Commerce, Google AP2/UCP, OpenAI/Stripe ACP, Mastercard Agent Pay), discovery/catalog layers, and a thin but fast-growing agent-fraud/identity layer (Forter, incumbents like Visa/Mastercard security stacks). Entry barriers: merchant distribution and network data (Forter's ~$2tn processed history), not capital. "Why now": agent traffic looks like bots to legacy fraud models, so merchants either reject legitimate agent orders or wave through disguised fraud — a trust gap that has to be closed before agentic checkout scales. 78% of financial institutions expect AI-agent fraud (per survey citation, 2026).

**Competitive landscape.** Sector KPIs: for the fraud layer — authorization/approval rate, chargeback/fraud-loss rate, false-decline rate; for the rail — agent transaction volume, take rate. Basis of competition: data/network effects and merchant distribution, not price. Agentic orders on Forter's network jumped >4x since August 2026 (per PR/press, as of Oct 2026) — the demand signal the deal rides. Recent peer moves: Visa Trusted Agent Protocol (Oct 2025, [[Visa launches Trusted Agent Protocol for AI commerce]]); Nuvei adopted it ([[Nuvei supports Visa Trusted Agent Protocol]]); Worldpay flagged consumer fraud wariness ([[Worldpay report consumers wary of agentic AI shopping fraud]]). Position: Skyfire is a niche rail/identity specialist (founded 2023, ~$9.5M raised — a16z CSX, Coinbase Ventures, Neuberger Berman) that gains distribution by feeding KYA identity signals into Forter's installed base; Forter is the established incumbent ($3bn valuation 2025, ~$103M ARR 2024) extending its moat into agents. Moat: Forter's network/decisioning data (switching costs + scale); Skyfire's is the KYA identity standard IF it becomes default — otherwise it is one of several competing protocols (analysis).

**Comps & multiples.** Forter: last round $300M Series F (2021), ~$525M total raised, $3bn valuation (2025) — round/private mark, not market cap; implied P/S ≈ $3.0bn / $0.103bn ≈ 29x on 2024 ARR (high, but a 2025 mark on 2024 revenue and the usual private-growth premium — not an outlier flag on its own). Skyfire: ~$9.5M total raised, no disclosed valuation → multiples = no data. Internal comps (private agentic-commerce rounds): [[Basis Theory raises $33 million for agentic commerce]], [[Paygentic raises $2M pre-seed for AI payments infrastructure]], [[Coinbase launches Payments MCP for AI agents]]. Peer fraud multiples (public): no data / [UNSOURCED] — closest public comp would be fraud/identity vendors, none cleanly comparable here, so distribution not computed, qualitative comparison only.

**Risk flags.**
1. Rail disintermediation — Visa, Mastercard, Google and OpenAI/Stripe are all pushing their own agent-identity/trust protocols; if a card-network or Big Tech standard wins, Skyfire's KYA could be bypassed and the value accrues to Forter (the data layer), not the thin rail (second-order: Skyfire's distribution gain may not convert to durable economics).
2. "Announced vs live" — this is a signal-enrichment integration with one named pilot (Jomashop); no disclosed revenue split, pricing or exclusivity, and the >4x agentic-order growth is off a tiny base. Adoption breadth unproven.
3. Concentration/early-base — agent fraud models are being trained on thin, fast-changing data; a mis-tuned model raises false declines (killing the merchant's authorization-rate pitch) or lets disguised fraud through (chargeback exposure) — the exact failure mode the deal claims to fix.

**What this changes (idea-lens).** (analysis) This is the agentic-commerce stack bifurcating into a "trust/identity" layer: whoever owns agent-identity signals (KYA-style) becomes a tollgate on agent checkout, and fraud incumbents are racing to absorb it before networks standardize it away. Falsifiable thesis: if Forter publishes measurable authorization-rate / chargeback improvements from KYA signals within ~2 quarters, the identity-enrichment model is real and other fraud vendors copy it; trigger to watch — a competing card-network protocol becoming the merchant default (Visa Trusted Agent / Google AP2), which would make KYA redundant and break the thesis.

Sources: https://www.businesswire.com/news/home/20261019685711/en/Skyfire-and-Forter-Enrich-Trusted-Agentic-Commerce-Decisions-at-Checkout · https://www.pymnts.com/partnerships/2026/skyfire-and-forter-team-to-strengthen-agentic-commerce-decisioning/ · https://fintech.global/2026/10/19/skyfire-and-forter-target-fraud-in-ai-agent-checkout/ · https://sacra.com/c/forter/ · https://getlatka.com/companies/forter · https://tracxn.com/d/companies/skyfire/__-gSNwLdAbLR2EH3jQO5ja24BZ2dqjmKWC_BS3-4pf1s · https://www.juniperresearch.com/research/fintech-payments/ecommerce/agentic-commerce-research-report/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
