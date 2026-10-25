---
title: "Beltic launches agent identity and permissions for businesses"
date: 2026-10-25
retrieved: 2026-10-25
tags:
  - company/beltic
  - industry/ai
  - industry/infrastructure
  - region/us
  - type/product
sources:
  - https://www.beltic.com
  - https://blog.cloudflare.com/agent-registry
status: enriched
n_mentions: 3
channels:
  - "Fintech Brainfood"
story_id: sbc7bc7e3
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Beltic launches agent identity and permissions for businesses

> [!info] 2026-10-25 · 3 упоминаний · 0 источника(ов) с текстом
> Каналы: Fintech Brainfood

## Агрегированный текст (из дайджестов)

[Fintech Brainfood] Beltic — Agent identity and permissions for businesses

[Fintech Brainfood] 1. Beltic — Agent identity and permissions for businesses

[Fintech Brainfood] 🧠 Most companies can’t tell genuine agent traffic from bad bots; that's partly why they’re blocking them. Cloudflare already verifies bot and agent traffic, Beltic adds the ability to decide what they can do. If you stick this with the recently announced Personal Agent Protocol (PAP), which is a way for agents to formally request what they want, and you have something fairly complete. I feel like this should be a feature in every major commerce platform (Shopify, Woo, BigCommerce, etc.).

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.beltic.com>
- <https://blog.cloudflare.com/agent-registry>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 2/5._

### [0] What exactly happened (de-PR'd)
This item is a one-line callout in a Fintech Brainfood roundup (2026-10-25), not a standalone product announcement. Beltic — a San Francisco startup founded in early 2025 — is building "agent identity and permissions for businesses": infrastructure that lets a business verify the person/company behind an incoming AI agent and then decide what that agent is allowed to do (allow / block / step-up confirmation per action). The pitch framing is "Know Your Agent" (KYA), explicitly the agentic analogue of KYC.

The roundup editor's own read is the honest part: most companies can't distinguish genuine agent traffic from bad bots, so they just block agents. Cloudflare already verifies that traffic exists; Beltic's claimed delta is deciding what verified agents can *do* (authorization/permissions layer on top of identity). The editor notes that combined with the recently announced Personal Agent Protocol (PAP) — a way for agents to formally request what they want — "you have something fairly complete," and muses it "should be a feature in every major commerce platform (Shopify, Woo, BigCommerce)."

Why this framing matters: the note's two cited sources are beltic.com and a Cloudflare agent-registry blog post, i.e. it is substantially a positioning/commentary item, not a disclosure of new terms, customers, or metrics. The real corporate event behind Beltic is its stealth exit with a ~$7.3M seed (led by Norwest; Restive Ventures, Oxford Seed Fund, Collide Capital; angels from Coinbase/Ramp/Legora) on top of ~$1.5M pre-seed — ~$8.8M total — announced around 2026-09-30 (external press). That funding is NOT a new event as of this note; the Oct 25 roundup is a product/capability framing of an already-funded, already-out-of-stealth company. Founders: Isha Bhatnagar (ex-Coinbase regulatory/identity) and Mike Allan (Brazil banking infra); Beltic acquired Verifiet, whose co-founder Farhan Afsahi became CTO.

### [1] Competitors / peers
The agent-identity/authorization layer is crowded and standards-fragmented. Direct/adjacent players: Skyfire (KYA + KYAPay, signed JWTs, OAuth2/HTTP-compatible; F5 bot-defense integration shipped ~Apr 2026), Nekuda (agentic payments SDK: secure agent wallet + mandates), Proof (x401 open protocol to prove who an agent represents — [[Proof launches x401 protocol to verify AI agents online]]), Cloudflare (agent/bot verification + registry, cited in this very note), and the card networks' own agentic trust frameworks (Mastercard agentic token / Visa Trusted Agent Protocol, Ant/Mastercard/Visa AI-commerce work). On the protocol side: PAP from Meta/Sierra ([[Meta and Sierra introduce Personal Agent Protocol standard]]), plus the broader agentic-rails fight surveyed in [[Fintech Brainfood the protocols for agentic banking and payments]].

Position: Beltic is a well-funded but early entrant in a layer where the biggest leverage sits with whoever sits in the traffic path (Cloudflare) or owns the payment rail (Visa/Mastercard). Its differentiation claim — permissions/authorization on top of identity — is defensible only if it is protocol-agnostic and adopted across rails; otherwise identity+permissions get absorbed by the gateway (Cloudflare) or the network (card schemes) that already see the traffic.

### [2] Company history / fit
Short trajectory: founded early 2025, built by a founder pair that each worked the "let good transactions through, block fraud" problem (Coinbase identity side; Brazil banking-infra side), tuck-in acquisition of Verifiet for the CTO/tech, out of stealth ~Sep 2026 with ~$8.8M total. The company is positioning KYA as a new compliance primitive — logical given both founders' KYC/fraud backgrounds. This Oct 25 roundup mention fits the pattern of a newly-unstealthed startup getting repeated newsletter pickups as the agentic-commerce narrative runs hot.

### [3] Novelty / value-add / traction
Genuinely-new vs prior art: thin. "Agent identity" is already contested by Skyfire/Proof/Cloudflare/card networks; Beltic's specific claim is the *permissions/authorization* decision layer ("what can this verified agent do") rather than mere identity attestation. That is a real conceptual gap — identity ≠ authorization — but no public adoption metrics, named merchant customers, GMV, or live integrations appear in this note. Everything here is "capability exists / should be everywhere," i.e. announced/positioned, not demonstrated traction. Who captures the margin is the open question: if authorization rides on top of someone else's identity + rails, Beltic risks being a feature, not a platform — which is exactly what the roundup editor hints ("should be a feature in every major commerce platform").

### [4] What's next / market sentiment
Backdrop is very hot and anxious: banks warning customers about linking accounts to agents ([[RBC and BMO CEOs warn customers over linking accounts to AI agents]]), bank-agent liability debates, Walmart/Robinhood giving agents gateways/accounts ([[Walmart launches Agent Gateway for AI shopping agents]]). That tailwind funds companies like Beltic but also invites the networks and gateways to build KYA in-house. Watch for: named design partners/merchants, which protocols Beltic interoperates with (ACP/AP2/PAP/x401), and whether Cloudflare/Visa/Mastercard partner with vs. subsume the authorization layer. Risk: commoditization of agent identity + absorption of permissions into the rail/gateway.

### Sources
- Fintech Brainfood roundup (2026-10-25) — note aggregated text
- https://www.beltic.com ; https://www.beltic.com/blog/out-of-stealth
- https://blog.cloudflare.com/agent-registry
- thisweekinfintech.com, prnewswire.com, optim.vc, notesfromtheterminal.com — Beltic $7.3M seed / stealth exit (~2026-09-30)
- skyfire.xyz, rye.com, stellagent.ai, bex.co (KYA/competitor landscape)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Freshness/duplicate verdict: FRESH (but thin/early).** No prior Beltic note exists in the corpus; this is the first mention. It is NOT a duplicate. Caveat: the underlying corporate event (the ~$7.3M seed / stealth exit, ~2026-09-30) predates this note — this Oct 25 item is a product/capability *framing* in a Fintech Brainfood roundup, not a new funding or launch disclosure. Treat as a fresh but low-weight positioning item.

**Importance: 2/5** — well-funded founder team in a hot category, but a one-line newsletter callout with zero traction metrics, no named customers, and heavy overlap with better-positioned incumbents (Cloudflare, card networks, Skyfire, Proof).

Red-team / second-order questions:
1. Is this actually a new event, or a re-framing of the Sept 30 stealth exit? (Appears to be re-framing; no new funding/customers disclosed here.)
2. Identity vs authorization: is "deciding what an agent can do" a durable product, or a feature the traffic-path owner (Cloudflare) absorbs? — open, leans feature-risk.
3. Does Beltic interoperate across protocols (ACP, AP2, PAP, x401) or bet on one? Single-protocol lock-in would cap TAM. — open.
4. Any named merchants, design partners, or live integrations? — none in this note; unverified.
5. What stops Visa/Mastercard (who already own rails + agentic trust frameworks) from building KYA permissions in-house? — open; structural threat.
6. Cloudflare is cited as a *complement* here — is Beltic dependent on Cloudflare's agent registry/verification as upstream? If so, who captures margin? — open, dependency risk.
7. How does KYA permissioning handle liability allocation when an authorized agent acts wrongly? (Ties to the bank-agent liability debate.) — open; the hard commercial/legal question is unaddressed.
8. Is "KYA = the new KYC" a real regulatory category or vendor marketing? No regulator has mandated KYA. — marketing framing.
9. Revenue model: per-verification, seat, or transaction take-rate? Unknown — determines whether it scales like infra or like SaaS. — open.
10. Pricing/economics vs just blocking agents: businesses today block agents for free; what's the ROI of permissioning? — open.
11. Does the Verifiet acquisition bring real tech/patents or just a CTO hire? — unclear.
12. Defensibility: identity data is network-effect-driven; is Beltic's verification graph proprietary or riding others' signals? — open.
13. If "should be a feature in every commerce platform" (editor's own words), does Shopify/BigCommerce build it natively and disintermediate standalone KYA vendors? — plausible, downside trigger.
14. How does Beltic differ substantively from Skyfire's KYAPay (JWT-based KYA) beyond the permissions framing? — not demonstrated.
15. Second-order: in a fragmenting standards war (PAP vs x401 vs ACP vs card-network frameworks), does an authorization layer need a winning identity standard first? If so, Beltic's timing is early and its fate is coupled to someone else's standard winning. — key open question.

Importance: 2/5
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Beltic sits in the emerging "agent identity, authorization and trust" layer of agentic commerce — not the payment rail itself, but the policy/verification gate that decides *what* a verified agent is allowed to do. Market sizing is early and analyst-house (treat as directional, not hard): per SNS Insider, the AI-agent identity-and-access-management market was ~$402.5M in 2025, ~$547.8M in 2026, projected ~$8.8bn by 2035 at ~36% CAGR; per market.us, the adjacent AI-agent permission-management market was ~$466M in 2025 at ~37% CAGR (both via secondary market-report sites, as of 2026 — unverifiable primary source, so directional only). Why now: in late-2025/early-2026 the *payment* layer standardized fast and simultaneously — OpenAI/Stripe's Agentic Commerce Protocol (ACP, Shared Payment Tokens), Google's AP2, Visa's Trusted Agent Protocol (TAP), Mastercard Agent Pay (per digitalapplied.com / refontelearning, 2026). Once agents can *pay*, the unsolved problem shifts one layer up: merchants can't distinguish a genuine delegated agent from a bad bot, and legacy fraud tooling was built for humans, not software acting on a customer's behalf. That is the gap Beltic's "Know Your Agent" (KYA) targets — verifying the person/business behind an agent via portable cryptographic credentials, then enforcing per-action policy.

**Competitive landscape.** Sector KPIs (early-stage, mostly undisclosed): verified-agent coverage / credential portability, policy-decision latency (Beltic claims millisecond verification `[UNSOURCED beyond PR]`), protocol-agnostic rail coverage, merchant integrations. Basis of competition = trust primitive + distribution/standards alignment, not price. Players split into (a) rails/standards setters capturing the payment token (Stripe/OpenAI ACP, Visa TAP, Mastercard, Google AP2); (b) traffic-verification incumbents (Cloudflare's agent/bot registry — Beltic positions as complementary, adding "what can they do" on top of Cloudflare's "is this a real agent"); (c) pure-play agent-identity/KYA peers — Skyfire (founded 2022, ~$9.5M raised, a16z CSX / Coinbase Ventures / Brevan Howard Digital; also markets "KYA"), Payman, Natural, Nekuda. Recent demand signals: JPMorgan moved to block outside AI agents from accessing accounts, and RBC/BMO CEOs publicly warned customers over linking accounts to AI agents (both Oct 2026, in-base) — i.e. the enterprise side is defensively gating agents, which is exactly Beltic's buyer. Position: niche new entrant, roughly at parity with Skyfire on the KYA framing but behind on vintage/raise; moat is thin today (intangibles/standards relationships) — `(analysis)`.

**Comps & multiples.** De-PR: the digest frames this as a product "launch," but the underlying event is Beltic's **out-of-stealth $7.3M seed (Sept 30, 2026), led by Norwest** (Restive Ventures, Oxford Seed Fund, Collide Capital), lifting total funding to **$8.8M** (incl. a $1.5M Collide-led pre-seed). No post-money valuation, revenue, or agent-volume disclosed → trading multiples **not computable (no data)**; this is a seed-stage credential-layer bet, not a priced comp. Nearest external comp: **Skyfire** — ~$9.5M total raised for the same KYA/agent-identity thesis (per Tracxn, 2026), i.e. Beltic is raising into an already-funded category at a similar check size, which argues the round is priced to the *category narrative*, not differentiated traction `(analysis)`. Internal comps (grep fallback; sem down, OpenRouter 402): [[Harbor raises $10M seed to insure AI agent risks]] (adjacent agent-trust/risk layer, $10M seed — larger raise, parallel "make agents safe for enterprises" thesis), [[Iridium Credit raises $3M to verify every invoice]] (verification-as-infra, smaller seed), [[JPMorgan blocks outside AI agents from accessing accounts]] and [[RBC and BMO CEOs warn customers over linking accounts to AI agents]] (demand-side driver — incumbents gating agents), [[This Week in Fin AI agents open new bank security threats]] (threat framing). Distribution not computed — <3 comparable priced figures; qualitative only.

**Risk flags.** (1) **Standards/disintermediation risk** — the big economics sit in the payment token (ACP SPTs, Visa TAP, Mastercard, Google AP2); if those standards or Cloudflare's registry absorb identity+authorization natively, Beltic's "permissions" layer can be squeezed between the rail below and the merchant platform above (it even positions as a *feature* for Shopify/Woo/BigCommerce — feature, not platform, is a value-capture trap). (2) **Crowded, undifferentiated early field** — Skyfire ships the same "KYA" language with a 3-year head start and more capital; Beltic's moat is unproven and the category may consolidate before any single credential standard wins (network-effects winner-take-most risk cuts against a sub-$10M seed player). (3) **Adoption/chicken-and-egg + regulatory ambiguity** — value requires both merchants *and* agent issuers to adopt one credential scheme; with banks currently *blocking* rather than onboarding agents and liability/fraud rules for agent transactions unsettled, the buyer timeline may slip well past the funding runway.

**What this changes (idea-lens).** `(analysis)` The agentic-commerce stack is bifurcating: payment-token standards are near-settled, so 2026–27 competition moves up to the *identity/authorization/trust* layer — Beltic is an early entry in that re-rating, not a consolidation event. Falsifiable thesis: this layer is a durable standalone category only if a neutral, portable KYA credential emerges that rails and merchant platforms adopt rather than build; trigger to watch — whether Visa/Mastercard/Stripe/OpenAI embed native agent-authorization (thesis breaks) or instead partner with/acquire credential specialists like Beltic or Skyfire (thesis holds). Near-term tell: Beltic merchant/partner integrations beyond the single Keiki partnership currently cited.

Sources: https://www.thisweekinfintech.com/p/exclusive-beltic-raises-7-3m-to-help-businesses-keep-ai-agents-in-check · https://www.finsmes.com/2026/09/beltic-raises-7-3m-in-seed-funding.html · https://beltic.com/kya · https://blog.cloudflare.com/agent-registry · https://www.digitalapplied.com/blog/agentic-commerce-standards-ucp-acp-ap2-2026-merchant-guide · https://tracxn.com/d/companies/skyfire/ · https://www.snsinsider.com/reports/ai-agent-identity-and-access-management-market-11181 · https://market.us/report/ai-agent-permission-management-market/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
