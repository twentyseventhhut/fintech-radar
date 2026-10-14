---
title: "Reap partners AIR and Pivota on AI agentic commerce"
date: 2026-10-09
retrieved: 2026-10-09
tags:
  - company/reap
  - company/pivota
  - industry/agentic-commerce
  - industry/payments
  - region/global
  - type/partnership
sources:
  - https://www.techinasia.com/news/hong-kong-fintech-firm-reap-test-ai-purchasing-setup
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sfa965c97
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Reap partners AIR and Pivota on AI agentic commerce

> [!info] 2026-10-09 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Reap partnered with AIR, Minds by Animoca Brands, and Palo Alto-based agentic commerce infrastructure startup Pivota to develop and test an AI-driven automated purchasing workflow with pre-approved spending limits, with Reap providing the agentic payment capabilities.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.techinasia.com/news/hong-kong-fintech-firm-reap-test-ai-purchasing-setup>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Reap partners AIR and Pivota on AI agentic commerce
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS: fresh.** Announced 2026-10-09. This is a NEW four-party pilot, distinct from the May-2026 Payward/Kraken acquisition of Reap ([[Kraken parent Payward to acquire Reap for up to $600 million]]) and the 2025 Thredd/Visa stablecoin-card deals ([[Thredd expands Reap partnership for stablecoin cards]]). Note the digest title/tags are slightly misleading: Animoca Brands (via AIR + Minds) is the lead orchestrator and merchant-facing brand, not just a side partner — the primary-source announcement is an Animoca release, and most outlets headline it "Animoca's AIR and Minds partner with Reap and Pivota."

## [0] What exactly happened (de-PR'd)
- A four-party **pilot** (framed, NOT live commerce): a Minds AI agent completes a purchase for a user while (a) proving the user's entitlements/identity via AIR without exposing personal data, (b) picking product/merchant/route via Pivota, and (c) paying via Reap's agentic-payment rails within pre-approved spending limits. Reap supplies the payment capability only.
- Stack roles: **AIR** = privacy-preserving identity credentials on Animoca's Moca Chain (mainnet live; issues KYC/membership credentials portable across apps). **Minds** = Animoca's persistent agentic-AI platform (already running a separate live pilot with Visa). **Reap** = stablecoin-native card issuing + "Agentic Payments" product (tokenized credentials, scoped cards, programmable spend control, Visa authenticates / Reap underwrites against stablecoin collateral / settles on-chain). **Pivota** (Palo Alto; founder/CEO Peng Xu) = "commerce decision + order-execution layer" that indexes beyond the top ~1,000 brands and routes the order through the merchant's existing stack.
- **Reality check on scope:** the "first release is a controlled demonstration with ONE merchant" covering four steps — eligibility proof, an applied offer, a scoped payment credential, and authorisation. So: a single-merchant demo, not GMV, not multi-merchant, no disclosed volumes or conversion. → Why framed as a grand four-logo partnership: each party is small/pre-revenue in agentic commerce and gains credibility by co-branding; the PR anchors to the $3–5T McKinsey 2030 TAM, not to the one-merchant demo actually shipped.
- **Why this architecture:** it decomposes the "can an agent be trusted to spend my money?" problem into identity (AIR) + authorization/spend limits (Reap scoped credential) + catalog/routing (Pivota). → The real differentiator claimed is **identity-led** commerce (prove *who* and *what you're entitled to* without doxxing the user) rather than just "an agent with a card."

## [1] Competitors / peers
The agentic-commerce rails race is crowded and dominated by networks, not startups:
- **Visa** — Trusted Agent Protocol (Oct 2025, [[Visa launches Trusted Agent Protocol for AI commerce]]); Know Your Agent framework with Mastercard + Ant International (Sep 10, 2026). Visa also powers Reap's auth leg AND a separate Minds pilot — i.e. Visa sits underneath this "partnership" too.
- **Mastercard** — Agent Pay, integrated into PayPal wallet ([[PayPal integrates Mastercard Agent Pay into wallet]]); first live agentic ride-booking Mar 2026.
- **PayPal** — agentic commerce w/ NVIDIA Nemotron, Honey ([[PayPal adds Honey to new agentic commerce features]]).
- **Coinbase** — x402 protocol (powers AWS Bedrock AgentCore Payments, May 2026) ([[Coinbase x402 protocol logs surge in transactions]], [[Coinbase launches Payments MCP for AI agents]]).
- **Stripe/Checkout.com/Nuvei** — order-flow + agent protocols ([[Nuvei supports Visa Trusted Agent Protocol]]).
- Startups: Paygentic ($2M pre-seed), Basis Theory ($33M) ([[Paygentic raises $2M pre-seed for AI payments infrastructure]], [[Basis Theory raises $33 million for agentic commerce]]).
- **Position: catching up / parity at best.** → Why the landscape is network-dominated: the authorization/settlement leg is where fraud-liability and interchange economics live, and Visa/Mastercard already control it (Reap's own flow has *Visa* authenticating). The crypto-native angle (stablecoin settlement, Moca Chain identity) is the only place this consortium is genuinely differentiated — but that is also the least-adopted rail.

## [2] Company history / fit
- **Reap** (HK, founded ~2018, >200 staff): stablecoin-native corporate cards + cross-border payouts; MAS MPI license Oct 2025 ([[Hong Kong's Reap secures MAS Major Payment Institution license]]); joined Global Dollar Network Dec 2025 ([[Reap joins Global Dollar Network for stablecoin settlements]]); Visa stablecoin-card expansion to 100+ markets Sep 2026; TerraPay payout deal ([[Hong Kong fintech Reap partners with TerraPay on cross-border payouts]]). **Acquired by Payward (Kraken parent) for up to $600M, closed ~July 2026.** CEO Daren Guo (10/09/2026) said the Payward deal "sped up an existing roadmap, with agentic payments next" — so this pilot is the on-roadmap execution of what Guo flagged at the M&A ("web3, agentic commerce and more").
- → Why Reap acts this way: a commodity stablecoin-card take-rate needs a higher-multiple story; "agentic payments" is the software/platform narrative that justifies the $600M valuation and Payward's $20B equity framing. The pilot is strategically coherent, not a pivot.
- **Animoca Brands**: pivoting Moca Network → AIR (identity/money/loyalty layer); Moca Chain mainnet live; already piloting Minds+Visa commerce. For Animoca this extends its Web3-identity bet into payments.

## [3] Novelty / value-add / traction
- **Genuinely new-ish:** the *identity-led, privacy-preserving entitlement proof* (prove a user's loyalty/eligibility to a merchant without exposing PII) layered onto agent payments — most rivals solve "agent has a token/card," fewer solve "agent proves verified entitlements + applies the right offer." (analysis)
- **Traction: essentially zero.** One-merchant controlled demo, no GMV, no conversion, no named merchant, no live date. "Piloted/framed" ≠ live. → Who captures the margin: the settlement + authorization leg (Visa + Reap collateral/underwriting) captures payment economics; Pivota captures catalog/routing data; AIR/Minds capture identity + agent engagement. But with Visa authenticating every transaction, the network still owns the choke point — the consortium risks being a feature layer on top of Visa rails rather than an independent rail. → What breaks the value-add: if Visa/Mastercard's own Trusted Agent + Know Your Agent frameworks standardize identity-for-agents, AIR's differentiator (portable credentials) gets commoditized.

## [4] What's next / market sentiment
- Plan: expand from one-merchant demo to broader merchant set; Pivota's thesis is indexing the "long tail" beyond the top ~1,000 brands agents can currently reach.
- Sentiment: hot theme (McKinsey $3–5T agentic-commerce sales by 2030; every network + big fintech shipping something weekly). Regulatory backdrop: Visa/MC/Ant "Know Your Agent" (Sep 2026) is the emerging standard — a tailwind for identity layers but also a commoditization threat.
- → Why the market goes this way: the bottleneck is no longer "can an agent transact" but "can a merchant trust an agent's authority + spend limits" — identity/authorization is the real battleground. Counterintuitive second-order effect: the more networks standardize agent identity, the LESS defensible independent identity startups like AIR become; being inside a Visa-authenticated flow is both distribution AND a ceiling.

## Sources
- Animoca (primary): https://www.animocabrands.com/announcement/animoca-brands-air-and-minds-partner-with-reap-and-pivota-to-enable-identity-powered-personalized-agentic-commerce
- The Paypers: https://thepaypers.com/payments/news/air-and-minds-partner-with-reap-and-pivota-on-agentic-commerce
- FinanceFeeds: https://financefeeds.com/animoca-air-minds-reap-pivota-agentic-commerce/
- Tech in Asia (digest source): https://www.techinasia.com/news/hong-kong-fintech-firm-reap-test-ai-purchasing-setup
- Reap Agentic Payments: https://reap.global/products/agentic-payments
- Blockhead (Guo on Payward/roadmap): https://www.blockhead.co/2026/10/09/reaps-daren-guo-says-payward-deal-sped-up-an-existing-roadmap-with-agentic-payments-next/
- Moca Chain mainnet: https://www.kucoin.com/news/flash/moca-chain-mainnet-launches-with-identity-credentials-for-businesses-and-ai-agents
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 2/5** — Rationale: An on-theme (agentic commerce) but low-traction item: a single-merchant controlled DEMO, no GMV/conversion/live date, four small parties co-branding around a huge TAM. Reap contributes only the payment leg and the network choke point (Visa) sits underneath. Strategically coherent (on Reap's post-Payward roadmap) and the identity-led angle is mildly differentiated, but no adoption and a crowded, network-dominated field keep it at 2. Would be 3+ if a named merchant went live with real volumes or exclusivity.

Red-team / challenge questions:
1. Is this live or a demo? → ANSWERED: "controlled demonstration with one merchant" — a demo, not production. Red flag against any "launch" framing.
2. Who is the actual lead — Reap or Animoca? → Animoca (AIR+Minds) is the orchestrator and primary-source issuer; the digest title under-weights Animoca. Does the note's Reap-first framing distort the story? (open/analysis)
3. What exactly does Reap contribute vs the others? → Payment capability only (scoped credential + stablecoin-collateral settlement). The other three legs (identity, agent, catalog) are not Reap's.
4. Does Visa authenticating every transaction make the whole consortium a feature on top of Visa rails rather than an independent rail? → Likely yes (analysis). If so, where is the durable margin?
5. Is the identity-led entitlement proof genuinely novel, or does Visa/MC/Ant "Know Your Agent" (Sep 2026) commoditize it within a year? → open; this is the key value-destruction trigger for AIR.
6. Any named merchant, GMV, conversion, ticket size, or fraud-liability allocation disclosed? → None. Who eats fraud when an agent over-spends within "pre-approved limits"? Silent.
7. Is this just the activation of Reap's already-announced "Agentic Payments" product (on the roadmap Guo flagged at the May M&A) rather than a new capability? → Largely yes — it's roadmap execution, which caps novelty.
8. Does Payward/Kraken ownership matter here, or is this pre-acquisition momentum? → Guo says Payward "sped up an existing roadmap"; the pilot is Reap-driven, Payward incidental so far. (open on whether Payward distribution gets attached)
9. Pivota is pre-revenue/early (Palo Alto, founder Peng Xu) — is its "index the long tail of merchants" thesis proven anywhere? → open; no traction cited.
10. Why four parties instead of two? → Each is sub-scale in agentic commerce; co-branding manufactures credibility and splits the stack. Does the complexity itself signal none can do it alone? (analysis)
11. Stablecoin settlement angle: does any part of this demo actually settle in stablecoins, or is it Visa-rails with stablecoin collateral behind the scenes? → Reap's model = Visa auth + stablecoin collateral netting; the user-facing leg is card. Worth not overselling "stablecoin commerce."
12. Is this a duplicate of the May Payward/Reap M&A note or the Thredd/Visa card notes? → No — distinct event (new pilot, new parties). Fresh.
13. Regulatory exposure: agents spending autonomously + privacy-preserving identity — any consumer-protection / authorized-push-payment-fraud concern once this scales? → open, material at scale.
14. What would make this a 3–4/5 next time? → A named merchant live, disclosed GMV/conversion, multi-merchant rollout, or an exclusivity/distribution tie to Payward/Kraken's base.
15. Second-order: if networks (Visa/MC) win agent-identity standardization, does being "inside a Visa-authenticated flow" become a ceiling rather than distribution for AIR/Reap? → the central question shifts from "is there an AI story" to "who owns the identity+authorization choke point" — and today that is the networks.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce (AI agents transacting on a user's behalf) is a theme, not yet a sized market with reliable figures. Secondary forecasts vary wildly by definition: US agentic commerce $300–500bn and 15–25% of US e-commerce by 2030 (per Bain, via ai-best-practices citing Juniper/Bain, as of 2026); global agentic spend "$3–5tn by 2030" (per McKinsey framing, same source) vs eMarketer's far lower $144bn — the 30x spread is itself the signal: no consensus TAM, treat any single number as marketing (analysis). The narrower, more relevant slice — agentic *payment infrastructure* — is projected to grow from ~$7bn to ~$93bn by 2032 (per Juniper/secondary citation, as of 2026). Structure: fragmented and pre-standard; the stack is splitting into identity (who the agent represents), authorization/credential (how much, where, when), order-execution/merchant-decision, and settlement/rails layers. Value accrues to whoever owns the scarce layer — rails + risk/fraud liability, and merchant-side distribution. Why now: 2025–26 saw the incumbents define the protocol layer — Visa Trusted Agent Protocol, Mastercard Agent Pay, Stripe/OpenAI in ChatGPT, PayPal Agentic Commerce Services (all [[Visa launches Trusted Agent Protocol for AI commerce]], [[Mastercard and PayPal partner on agentic commerce]], [[Stripe enables payments in ChatGPT with OpenAI]]) — so the land-grab for the *authorization* layer around those protocols is the open contest Reap is playing in.

**Competitive landscape.** Sector KPIs for the payment layer: TPV routed through agent credentials, attach/take rate per agentic transaction, authorization-success & fraud/chargeback rate, number of live merchant integrations (vs announced). Reap discloses none of these for this pilot → `[UNSOURCED]`. Players by layer: (a) protocol/network incumbents — Visa, Mastercard, PayPal, Stripe — who set the rules and capture network economics; (b) data/vault & infra — [[Basis Theory raises $33 million for agentic commerce]], [[Paygentic raises $2M pre-seed for AI payments infrastructure]]; (c) crypto/stablecoin agent payers — [[Oobit lets AI assistants pay with crypto and stablecoins]] (near-identical model: single-purpose card issued per approved purchase), Coinbase x402 ([[Coinbase x402 protocol logs surge in transactions]]); (d) this consortium — Reap (payment credential), Pivota (merchant/order-execution), AIR+Minds/Animoca (identity on Moca Chain + agent runtime). Basis of competition: not price but trust/control — who can bound an agent's spend and carry the fraud liability. Reap's position: niche/early — its differentiator is issuing a Visa credential scoped to one merchant, one amount, one time-window (de-PR: this is the same per-purpose-card pattern Oobit already ships, so not uniquely novel). Moat `(analysis)`: Reap's real asset is its licensed card-issuing + stablecoin rails (MAS Major Payment Institution licence, [[Hong Kong's Reap secures MAS Major Payment Institution license]]) and its pending absorption into Kraken/Payward's balance sheet — regulatory + rails scale, not the agentic software itself.

**Comps & multiples.** No valuation attaches to *this* partnership (pilot, one merchant, no economics disclosed) → deal multiple = no data. Reap's own reference point: Payward (Kraken) agreed to acquire Reap for up to $600m in cash+stock, May 2026 ([[Kraken parent Payward to acquire Reap for up to $600 million]]), inside a Payward equity valuation of ~$20bn ([[Kraken parent Payward raises capital at $20 billion valuation]]). Prior Reap funding: $40m Series A (Oct 2022, Acorn Pacific/Arcadia/HashKey), $5m seed (2020) — per Crunchbase/Dealroom, as of 2026. Revenue/TPV undisclosed → EV/Revenue cannot be computed = no data; the $600m is an M&A price for the whole payments franchise, NOT a mark on agentic commerce. Peer financing comps (private, round sizes not multiples): Basis Theory $33m Series B (Oct 2025, Costanoa); Paygentic $2m pre-seed (Oct 2025). Caution: do not confuse Pivota (Palo Alto, agentic-commerce order layer) with "Pivot" (Paris, enterprise-procurement agent, €34.4m/$40m Series B May 2026) — different company, excluded. With <3 comparable multiples, distribution not computed — qualitative only: agentic-payment infra is being funded at seed/Series-A ticket sizes, consistent with a pre-revenue, pre-standard sector.

**Risk flags.**
1. Disintermediation / rails-captured-by-another-layer — Visa/Mastercard/Stripe own the protocol and the card network Reap issues on; if the networks' native agent-authorization (Trusted Agent Protocol, Agent Pay) becomes the default, Reap's scoped-credential feature is commoditized and margin stays with the network, not the issuer.
2. "Announced vs live" execution risk — this is a single-merchant pilot with four parties (Reap, Pivota, AIR, Minds); multi-party consortia with no disclosed economics, fraud-liability split, or ticket size routinely stall before scale (who is silent: everyone, on who eats the chargeback).
3. Ownership/integration overhang — Reap is mid-acquisition by Payward/Kraken (expected close H2 2026); Kraken's own priorities (IPO prep, OCC/trust-charter push) could redirect or deprioritize a speculative agentic pilot, and regulatory approval of the deal is not yet confirmed.

**What this changes (idea-lens).** `(analysis)` The contested prize in agentic commerce isn't checkout — the networks already took that — it's the *authorization/identity* layer that lets an agent spend within hard limits; expect consolidation where issuers/rails pair with identity providers (here Reap×Animoca's Moca Chain). Falsifiable thesis: if, within ~6–12 months, this pilot does not move from one merchant to a multi-merchant live deployment with a disclosed take-rate, it's a marketing collaboration, not a product — watch for a GA announcement with named merchants and transaction volume as the trigger; its absence breaks the thesis.

Sources: https://thepaypers.com/payments/news/air-and-minds-partner-with-reap-and-pivota-on-agentic-commerce · https://financefeeds.com/animoca-air-minds-reap-pivota-agentic-commerce/ · https://www.juniperresearch.com/press/agentic-commerce-set-to-generate-15-trillion-globally-by-2030-as-payments-infrastructure-leaders-revealed/ · https://ai-best-practices.com/news/agentic-commerce-market-forecast-to-reach-300-500-billion-by · https://www.theblock.co/amp/post/400407/kraken-parent-payward-to-acquire-hong-kong-stablecoin-firm-reap-for-600-million · https://sacra.com/c/reap/ · https://www.crunchbase.com/organization/reap
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
