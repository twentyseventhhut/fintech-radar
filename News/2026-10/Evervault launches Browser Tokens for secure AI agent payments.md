---
title: "Evervault launches Browser Tokens for secure AI agent payments"
date: 2026-10-21
retrieved: 2026-10-21
tags:
  - company/evervault
  - industry/agentic-commerce
  - industry/payments
  - region/europe
  - type/product
sources:
  - https://www.businesswire.com/news/home/20261020664529/en/Evervault-Launches-Browser-Tokens-Enabling-Secure-Agentic-Payments
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sfde6924b
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Evervault launches Browser Tokens for secure AI agent payments

> [!info] 2026-10-21 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 4. 🇮🇪 Evervault launches Browser Tokens to enable secure payments by AI agents. The solution replaces sensitive card details and login credentials with short-lived tokens, allowing AI agents to complete purchases on existing merchant websites without exposing personal data.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261020664529/en/Evervault-Launches-Browser-Tokens-Enabling-Secure-Agentic-Payments>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 2026-10-20, at Money20/20, Dublin/New York encryption-infra startup Evervault launched **Browser Tokens**, a product that lets AI agents check out on any existing merchant website or log in to accounts without ever touching the underlying card number, CVV or password. Sensitive values are swapped for short-lived, **format-preserving** tokens; the agent and browser platform only ever see the token, and the real value is injected only at allowlisted merchant hosts — keeping the agent (and its operator) outside PCI-DSS scope. Launch users named are **Ramp** (an existing Evervault customer) and **Natural**. Pricing is usage-based: **$0.25 per card session, $0.05 per credential session** (BusinessWire / Finextra / Digital Transactions, 2026-10-20/21).

**[1] Why it matters / the positioning.** Evervault's pitch is "zero adoption required": unlike [[Visa launches Trusted Agent Protocol for AI commerce|Visa Intelligent Commerce]], Mastercard Agent Pay/AP4M, Stripe's Machine Payments Protocol (MPP) and OpenAI/Stripe's Agentic Commerce Protocol (ACP), Browser Tokens need **no merchant or bank integration** — they operate at the browser layer on top of the existing web. That makes it a protocol-agnostic workaround to the chicken-and-egg problem plaguing the networks' schemes, which require both sides to adopt new rails. It leans on Evervault's core tokenization/secure-enclave stack (the company reports >$5B in transaction volume processed last year and 4x+ YoY revenue growth).

**[2] Company / funding context.** Evervault was founded in 2019 by Shane Curran (Ireland), and has raised ~$46M total, most recently a **$25M Series B in March 2026 led by Ribbit Capital** (with Index, Sequoia, Kleiner Perkins, Operator Partners). It sells encryption, tokenization, secure enclaves and payment-optimization APIs to the likes of Ramp, Sling and Stitch. Browser Tokens is a net-new product extending that base into the agentic-commerce race rather than a new fundraise.

**[3] Competitive / internal landscape.** This sits in a crowded 2026 agentic-payments field already in the vault: the card networks ([[Visa launches Trusted Agent Protocol for AI commerce]], Mastercard Agent Pay), big PSPs/wallets ([[Stripe enables payments in ChatGPT with OpenAI]], [[PayPal launches Agentic Commerce Services for AI checkout]], [[PayPal integrates Mastercard Agent Pay into wallet]]), tokenization/vault specialists ([[Basis Theory raises $33 million for agentic commerce]]), crypto/stablecoin rails ([[Fireblocks launches Agentic Payments Suite for AI agents]], [[Coinbase launches Payments MCP for AI agents]]), and consumer-facing agent checkout ([[Vivi Money launches Vivi Shop & Pay for AI purchases]]). Evervault's differentiator vs most of these is the no-integration, browser-layer tokenization angle rather than a new protocol or wallet.

**[4] The skeptical read (key caveat).** A pointed Yahoo Finance analysis argues Browser Tokens may solve the *wrong* problem: banks' current worry is **agent identity, intent and liability**, not credential theft. Between 2026-10-13 and 10-16, JPMorgan, Schwab, BofA and Citi hard-blocked third-party agents; Jamie Dimon warned of "thousands" of rogue agents and liability transfer. Browser Tokens reportedly ship with **anti-detection features (residential IPs, standard Chrome fingerprints, bot-avoidance)** to bypass fraud checks — which directly cuts against what banks are reinforcing, and *masks* agent identity rather than establishing it. Governance (spend caps, human-approval thresholds, merchant-category/kill-switch controls) is on the roadmap, **not available at launch**.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

- **Does it solve a problem banks actually have?** The sharpest critique (Yahoo Finance) is that tokenization addresses credential theft, while banks' Oct-2026 agent blocks (JPMorgan, Schwab, BofA, Citi) were about *identity, intent and liability* — which Browser Tokens do not establish. If anything, the bot-avoidance features (residential IPs, Chrome fingerprinting) *mask* agent identity, potentially putting Evervault/its customers on a collision course with the networks' Trusted-Agent direction.
- **Launch vs reality.** This is announced at Money20/20 with only two named users (Ramp, Natural); Ramp is a pre-existing customer, so adoption breadth is unproven. "No merchant/bank adoption required" is the headline claim — verify it survives contact with merchant fraud systems and acceptable-use/ToS enforcement.
- **Governance gap.** Spend caps, approval thresholds, merchant-category blocks and kill switches are roadmap, not shipped — so the "secure" framing covers data-at-rest/in-transit, not agent behavior control. Buyers should not read "secure agentic payments" as "governed agentic payments."
- **Unit economics / durability.** $0.25/card-session pricing is attractive at low volume, but a browser-layer workaround is vulnerable to being obsoleted if Visa/Mastercard protocols or OpenAI ACP win merchant adoption and bake tokenization in natively. Is this a durable platform or a bridge product for the pre-standard interregnum?
- **Sourcing.** Only one primary source (BusinessWire release) is in the note; transaction-volume/growth figures are company-stated and unaudited.

**Importance: 3/5** — A credible, well-funded (Ribbit-backed) entrant with a genuinely differentiated "no-integration" angle in the hot agentic-payments theme, and real launch partners. But it is an announcement (not GA metrics), narrowly adopted so far, missing governance at launch, and arguably mis-aimed at the credential-theft problem rather than the identity/liability problem that is actually gating bank acceptance. Notable, not pivotal.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Evervault sits in the data-tokenization / payment-vault layer of agentic commerce — the plumbing that lets AI agents transact without being handed raw card data or credentials. Market framing (take as scenario estimates, not firm TAM): per McKinsey (via Juniper Research, Apr 2026) global agentic transaction volume could reach $3–5tn by 2030; per Morgan Stanley (same, 2026) agents could capture ~$385bn of US e-commerce by 2030. Actual live volume is tiny today — per Tiger Research / Forbes (2026), Coinbase/Cloudflare x402 has cleared only ~$15m, and Stripe's agentic payment token settled ~$25k in its first weeks — so the sector is pre-revenue hype vs. adoption. Structure: fragmented and protocol-stratified. Rails/protocols are being set at the top by Visa (Trusted Agent Protocol), Mastercard (Agent Pay / AP4M, launched Jun 2026) and Stripe/OpenAI (Agentic Commerce Protocol with Shared Payment Tokens); the vault/tokenization layer below is contested by VGS, Skyflow, Basis Theory, Spreedly, TokenEx and Evervault. Why now: merchants and banks are blocking agent traffic over fraud/credential-theft fear, and whoever supplies the "safe hand-off" primitive becomes default infrastructure — a land-grab window while standards are unsettled.

**Competitive landscape.** Sector KPIs: sessions/tokens issued, attach to transaction volume, per-session price, merchant/host coverage. Evervault's pricing is disclosed: $0.25 per card session, $0.05 per credential session (per Finextra/BusinessWire, 20 Oct 2026), with Ramp and Natural as launch users. Basis of competition is protocol-neutrality + developer integration, not price. Differentiator `(analysis)`: Browser Tokens are protocol-agnostic (Luhn-valid, BIN-preserving short-lived values swapped in only at allowlisted hosts) so they work on any merchant web page regardless of ACP/AP4M/TAP — positioning Evervault as neutral middleware under all three network stacks rather than betting on one. Recent peer moves: Mastercard AP4M (Jun 2026); Visa TAP + >100 partners (2026); Stripe/OpenAI ACP (Mar 2026). Protagonist position: niche but well-placed — ahead on the narrow credential/card hand-off problem, behind on agent governance. Moat: thin — mostly intangibles/dev mindshare and host-allowlist integration; low switching costs vs. the network schemes' tokenization, which can disintermediate it.

**Comps & multiples.** Private, no public EV/Revenue possible — multiples = no data. Last-round funding for tokenization peers (per PitchBook/Crunchbase via WebSearch, 2026): VGS ~$105m raised (Series C $60m, 2021); Skyflow ~$101m raised; Basis Theory ~$17m disclosed (note: our corpus has a later $33m Series B). Internal comps: [[Basis Theory raises $33 million for agentic commerce]] (Series B led by Costanoa, 2025 — closest direct comp, programmable payment vault for agentic commerce); [[Paygentic raises $2M pre-seed for AI payments infrastructure]] (pre-seed, 2025); rails-layer context [[Visa launches Trusted Agent Protocol for AI commerce]], [[Stripe enables payments in ChatGPT with OpenAI]], [[Mastercard and PayPal partner on agentic commerce]]. Evervault's own valuation/round not disclosed → `[UNSOURCED]`. Qualitative: well-capitalized peers ($100m+) are the scaling set; Evervault appears earlier-stage/narrower — distribution, not capital, is the constraint.

**Risk flags.**
1. **Governance gap vs. what banks actually demand.** Spend caps, human-approval thresholds, kill switch and merchant-category blocks are roadmap-only, not at launch (per Yahoo Finance/Forkast, 2026). The product solves credential theft — a problem banks were *not* primarily worried about — while leaving the control surface banks require unshipped; adoption by regulated issuers stalls until guardrails land.
2. **Fraud-evasion optics / bank lockout risk.** Marketed features (residential IPs, standard Chrome fingerprints, anti-bot avoidance) are exactly the behaviors that triggered recent bank agent-lockouts — Evervault risks being read as helping agents *evade* fraud checks, inviting issuer and scheme pushback.
3. **Disintermediation by the network stacks.** Visa/Mastercard/Stripe tokenization is being baked into the protocols themselves; if the schemes' native tokens become the default hand-off, a neutral third-party vault layer gets squeezed — margin captured one layer up.

**What this changes (idea-lens).** `(analysis)` Signals the agentic-commerce fight is moving from "who sets the protocol" to "who owns the safe credential/card hand-off" — a new entry point below the schemes. Falsifiable thesis: protocol-neutral vaults like Evervault only survive if merchants/agents refuse to standardize on one scheme's tokens; watch whether Evervault ships the governance roadmap (spend caps/kill switch) and signs regulated issuers — if the networks' native tokenization wins first, the neutral layer collapses into a feature.

Sources: https://www.finextra.com/pressarticle/111376/evervault-launches-browser-tokens-enabling-secure-agentic-payments · https://finance.yahoo.com/technology/ai/articles/evervault-browser-tokens-solve-credential-211827798.html · https://www.juniperresearch.com/resources/blog/paying-at-agentic-speed-inside-visa-mastercard-and-stripe-s-agentic-commerce-push/ · https://reports.tiger-research.com/p/payments-30-the-ai-agent-payments-eng · https://pitchbook.com/profiles/company/342948-79
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
