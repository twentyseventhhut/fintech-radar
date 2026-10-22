---
title: "Sierra and Stripe let AI agents take payments during calls"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - company/sierra
  - company/stripe
  - industry/agentic-commerce
  - industry/payments
  - region/global
  - type/partnership
sources:
  - https://sierra.ai/uk/blog/from-conversation-to-payment-sierra-and-stripe
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s0e4433f1
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Sierra and Stripe let AI agents take payments during calls

> [!info] 2026-10-22 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌐 Sierra and Stripe partner to let AI agents take payments during calls. Customers can talk, pay and get a receipt on the same call. Businesses can connect their Sierra agents to Stripe directly through the Stripe App Marketplace, without custom integrations.

## Первоисточники

### sierra.ai
<https://sierra.ai/uk/blog/from-conversation-to-payment-sierra-and-stripe>
*326 слов · direct*

Payments are becoming increasingly important, as agents move from one-and-done support conversations to interactions that can drive revenue. Yet all too often at the moment of purchase, customers are transferred to another system or sent a payment link — bifurcating what should be a seamless process.
Our partnership with Stripe removes this friction so customers can have a conversation, pay, and get their receipt all on the same call.
 Cedar shows how it works 
 Cedar was one of the first companies to take payments over the phone through Sierra’s integration with Stripe. Medical bills can be confusing and stressful to navigate. One visit can produce separate charges or insurance adjustments that are hard to follow. Cedar helps health systems and physician groups make billing and payments easier for patients.
Now patients who call about a bill can get their questions answered and pay in the same conversation. When it’s time to pay, the agent moves into a secure payment mode. The customer then enters their card details on the keypad, which are routed to Stripe to process the payment. Once it’s gone through, the agent comes back on the line to confirm the transaction and help with whatever the patient needs next.
When patients start a payment with Kora, Cedar’s agent, 71.3% of those calls end in a successful payment.
 What’s next 
Sierra is now listed in the Stripe App Marketplace , so any business can connect their agent to their Stripe account without a one-off integration. And payments are just one part of a broader collaboration with Stripe. We’re also working with Stripe and other partners on Personal Agent Protocol , the open standard Meta and Sierra are building to define how personal agents interact with businesses. That includes how payments should work when a personal agent interacts with a business on someone’s behalf.
If your business already uses Stripe, install Sierra from the Stripe App Marketplace or get in touch with our team .

## Контекст

<!-- enrichment:context -->
## [0] What happened (one-paragraph fact base)

On ~20 Oct 2026 Sierra — the enterprise conversational-AI-agent company co-founded by Bret Taylor (OpenAI board chair, ex-Salesforce co-CEO) — announced a payments partnership with Stripe that lets a Sierra voice/chat agent collect a card payment and issue a receipt within the same customer conversation, removing the usual hand-off to a payment link or a human. At the moment of payment the agent switches into a "secure payment mode": the customer keys their card digits into the phone keypad (DTMF), which are routed directly to Stripe to create a PaymentMethod and process the charge; the agent (and the underlying LLM) never sees the raw PAN, only the payment status and the last four digits. Sierra is now listed in the Stripe App Marketplace, so any business already on Stripe can connect its agent without a one-off integration. Launch customer: healthcare-billing company Cedar, whose agent "Kora" reports 71.3% of calls where a patient starts a payment ending in a successful payment. Source: [Sierra blog "From conversation to payment"](https://sierra.ai/blog/from-conversation-to-payment-sierra-and-stripe); corroborated by [unite.ai](https://www.unite.ai/sierra-partners-with-stripe-to-bring-payments-into-ai-agent-calls/), [The Next Web](https://thenextweb.com/news/sierra-stripe-payments-ai-agent-calls), [Forkast](https://forkast.news/sierra-and-stripe-let-agents-take-card-payments-inside-phone-calls-the-agent-never-sees-the-card/).

## [1] Who the players are

- **Sierra** — enterprise AI-agent platform (customer service, now revenue-generating agents), founded 2023 by Bret Taylor and Clay Bavor. Raised a $950M Series E in May 2026 at a **$15.8B post-money valuation** (GV, Tiger Global, Benchmark, Sequoia, Greenoaks); ~$200M ARR per Sacra, >$1.4B raised total, >40% of the Fortune 50 as customers. (web: techstartups.com, sacra.com). Outcome-based pricing model.
- **Stripe** — payments infra giant, aggressively building the "economic infrastructure for AI." Context in [[Stripe unveils 288 launches for AI economic infrastructure]] (Sessions 2026, 29 Apr), [[Stripe enables payments in ChatGPT with OpenAI]] (Agentic Commerce Protocol, Oct 2025), [[Stripe launches tools to monetize AI usage costs]].
- **Cedar** — patient healthcare-billing/payments company; first production deployment via its agent "Kora."

## [2] Why it matters / what's new

The novel part is **form factor + security model**, not the card rail itself. Rather than agentic *web* checkout (carts, order intents), this is a **voice/phone** payment taken inline during a live support call, with a PCI-conscious design where keypad digits bypass the model. It moves Sierra's agents from cost-center "support" to **revenue-driving** interactions, and gives Stripe another distribution surface (the App Marketplace) for agent-initiated money movement. Sierra frames payments as one piece of a broader Stripe collaboration tied to the [[Meta and Sierra introduce Personal Agent Protocol standard]] (Personal Agent Protocol), where payment handling is explicitly a *future extension* — so this call-payments feature is a card-not-present rail available **today**, separate from that still-forming protocol.

## [3] Market context / competitive landscape

Agentic-commerce is a crowded land-grab, mostly oriented around *web/checkout* flows, which makes Sierra-Stripe's *voice* angle differentiated:
- **OpenAI + Stripe** — Agentic Commerce Protocol (ACP) + Instant Checkout in ChatGPT, plus the Order Intents API (hand an agent a URL + budget) — [[Stripe enables payments in ChatGPT with OpenAI]].
- **Visa** — Intelligent Commerce + [[Visa launches Trusted Agent Protocol for AI commerce]] / [[Nuvei supports Visa Trusted Agent Protocol]]; tokenized credentials + agent identity.
- **Mastercard** — Agent Pay / Agentic Tokens (bind a token to a specific agent + merchant scope + consent).
- **PayPal** — adopting ACP to expose its wallet network inside ChatGPT (Oct 2025).
- **AWS + Coinbase + Stripe** — [[AWS launches AgentCore Payments with Coinbase and Stripe]] (x402, stablecoins).
- **Stablecoin bets** — [[Stablecoin firms bet on nascent AI agent payments]] (Circle, Stripe/Tempo Machine Payments Protocol).
- Protocol-landscape commentary: [[Fintech Brainfood the protocols for agentic banking and payments]], [[Sumsub expands Know Your Agent framework with KYA Module for MCP]] (agent identity/KYA).

## [4] Open questions / what to watch

Does keypad-DTMF-to-Stripe actually clear PCI DSS scope the way marketing implies? Adoption beyond Cedar and whether the 71.3% completion stat generalizes outside healthcare billing. How this card rail reconciles with the Personal Agent Protocol payments extension and with ACP/Order Intents (one stack or parallel). Fraud/consent controls for agent-taken payments. Whether "agent never sees the card" holds under adversarial prompt attacks. Revenue split / Marketplace economics for Sierra.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
Red-team / skeptic's questions:

1. **Is this genuinely new, or a rebrand of phone payments?** Partly rebrand — DTMF-to-processor "secure phone payment" has existed for years (e.g. Paytia). NEW element: the surrounding *AI agent* orchestrating the call + the no-integration Stripe Marketplace install. Answered.

2. **Does the agent really never see the card?** Vendor claim: keypad digits route directly to Stripe; model sees only status + last four. Plausible and consistent across Forkast/unite.ai, but it's Sierra's own framing — not independently audited. OPEN on exact PCI scope.

3. **Is the 71.3% completion rate meaningful?** It's a single-customer (Cedar), single-vertical (healthcare billing — high-intent, inbound, obligated payers) figure supplied by the vendor. Not a general conversion benchmark. OPEN / treat as marketing.

4. **Does this require the Personal Agent Protocol?** No. PAP payments are an explicit *future extension*; this card rail ships now and is independent. Answered — don't conflate (separate note: Meta and Sierra Personal Agent Protocol).

5. **Is this card-present or card-not-present?** Card-not-present (customer keys digits remotely). Carries standard CNP fraud/chargeback risk. Answered.

6. **Who bears fraud/chargeback liability for an agent-taken payment?** Unspecified in sources; consumer keys their own card so it resembles standard CNP, but agent-mediated consent is legally untested. OPEN.

7. **How large is the addressable surface vs web agentic checkout?** Voice/phone support payments are a narrower slice than the ChatGPT/ACP web-checkout battleground. Differentiated but smaller TAM. Partially answered.

8. **Is Stripe exclusive here?** Sierra lists Stripe via the App Marketplace; no stated exclusivity. Sierra also works with Visa/Mastercard-adjacent protocols via PAP partners. OPEN on whether other PSPs follow.

9. **What's the competitive moat vs OpenAI/Stripe, Visa, Mastercard?** Moat is Sierra's enterprise agent footprint (>40% Fortune 50) + outcome pricing, not the payment rail (which is Stripe's). Thin on the payments layer itself. Answered-ish.

10. **Does "no custom integration" overstate it?** Marketplace install removes bespoke dev, but businesses still need an existing Stripe account, a Sierra deployment, and call-flow config. "Without custom integrations" is directional, not literal zero-work. Answered.

11. **Security: prompt-injection to exfiltrate payment state?** Server-validated, predetermined prompt sequence is claimed to constrain the model. Untested against adversarial attacks. OPEN.

12. **Any regulatory angle (healthcare/HIPAA via Cedar)?** Cedar handles patient billing — HIPAA + payments overlap; sources don't address compliance detail. OPEN.

13. **Is there real revenue impact for Sierra/Stripe, or is this a demo?** Cedar is in production, so beyond demo, but scale/GMV undisclosed. Partially answered.

14. **Does this deepen Stripe-vs-Adyen/Braintree competition for agent payments?** Yes directionally — gives Stripe an agent-voice distribution edge rivals lack a named equivalent for. Answered.

15. **Timeline consistency?** Blog/press cluster ~20 Oct 2026; note date 2026-10-22; PAP announced ~6 Oct 2026. Consistent. Answered.

Importance: 3/5 — Credible, well-sourced, production (Cedar) launch from a top-tier AI-agent company (Sierra, $15.8B) + Stripe, extending agentic commerce into the voice/phone channel with a thoughtful "agent-never-sees-the-card" design. Docked from higher because: the payment rail itself is standard CNP/DTMF (not a new rail), single launch customer, and it's one incremental node in an already-saturated agentic-payments narrative rather than a category-defining move. Above-average for a well-known, strategically-relevant partnership.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-22]] (2026-10-22).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: agentic commerce / AI-agent payments — agents that not only converse but transact on a user's behalf. Market-size figures diverge wildly by definition: Juniper Research puts 2026 agentic-commerce transaction value at ~$8bn rising to ~$3.5T by 2031; Bain forecasts the US agentic market at $300–500bn and 15–25% of e-commerce by 2030; McKinsey sizes a $3–5T global opportunity by 2030 (per Juniper/Bain/McKinsey via secondary analyst aggregations, as of 2026) — treat these as directional, not settled TAM. Structure: a nascent, layered and still-fragmenting stack, not yet consolidated — a commerce/checkout layer (ACP, maintained by OpenAI + Stripe), an authorization/trust layer (Google's AP2, Visa Trusted Agent Protocol, Mastercard Agent Pay), a settlement layer (Coinbase x402 for stablecoins), and an identity/authentication layer (Personal Agent Protocol, Meta + Sierra, launched 2026-10-06, built on OAuth). "Why now": the standards land-grab of late-2025/2026 — Google, Visa, Mastercard and OpenAI/Stripe shipped competing protocols almost simultaneously — is pulling agent payments from demo to production; this Sierra-Stripe tie is the live, revenue-generating end of that wave.

**Competitive landscape.** Sector KPIs: for the payments layer — TPV and take rate; for the agent layer — ARR, conversion/completion rate. Players by layer: Stripe owns the checkout/processing economics (ACP co-author, Link Wallet, Order Intents); card networks (Visa Intelligent Commerce, Mastercard Agent Pay) sit above as protocol-agnostic authorization; agent builders (Sierra, OpenAI/ChatGPT, Perplexity, Glance/PayPal, Symphony by Wix) own the conversation surface. Basis of competition: distribution (whose rails/marketplace the agent plugs into) and trust/fraud liability, not price. Recent moves: Personal Agent Protocol announced 2026-10-06 with Walmart, Shopify, Stripe, Rocket, Genesys, Instinct — notably identity/auth first, payments explicitly deferred to "future work" (per The Paypers / thenextweb, 2026-10). Sierra's position: ahead on enterprise voice-to-pay specifically — distribution via Stripe App Marketplace removes custom-integration friction, and Cedar reports 71.3% of Kora-initiated payment calls complete (per sierra.ai, 2026-10-22). Moat (analysis): switching costs from deep enterprise workflow embedding + co-authorship of the PAP standard; thin on the payments economics, which Stripe captures.

**Comps & multiples.** Protagonists are private; use last-round valuations (not market caps). Sierra: $15.8bn post-money on a $950M round (GV/Tiger Global, May 2026), up from $10bn (Sep 2025) — ~2.7x revaluation in ~8 months, tracking ARR ramp $100M (Nov 2025) → ~$150M+ (per sacra.com / CNBC / TechCrunch, 2025–26). Implied P/S on ~$150M ARR ≈ $15.8bn / $0.15bn ≈ ~105x — extreme even for hyper-growth AI, so (analysis) only justified by triple-digit ARR growth and strategic-platform optionality; revenue multiple is a weak anchor here. Stripe: $1.9T TPV in 2025 (+34% YoY vs $1.4T in 2024), $159bn tender valuation (Feb 2026, +74% vs prior tender) — P/TPV ≈ $159bn / $1,900bn ≈ ~0.084x; robustly profitable per 2025 annual letter. Internal comps (same agent-payments wave): [[Symphony by Wix integrates Stripe-built Link Wallet for AI agents]], [[Glance partners PayPal for AI-powered shopping and checkout]], [[Freehand launches Freehand Pay for AI-agent supplier payments]], [[Musk proposes shopping via credit card photos on Grok]], [[JPMorgan blocks outside AI agents from accessing accounts]]. Distribution not computed (mixed stages/models) — qualitative: Sierra rich-but-growth-backed, Stripe in-line for a profitable scaled processor.

**Risk flags.** (1) Margin capture / disintermediation — Sierra owns the customer conversation but Stripe takes the payment economics; as agent rails commoditize, the conversation layer risks becoming a low-margin front-end on someone else's settlement stack. (2) Standards fragmentation / fraud liability — ACP/AP2/TAP/Agent Pay/PAP are overlapping and unsettled; PAP itself ships identity first and defers payments, and no party has publicly owned who eats fraud/chargeback liability when an agent transacts — a real adoption and regulatory overhang (cf. [[JPMorgan blocks outside AI agents from accessing accounts]], where an incumbent is actively gating agent access). (3) Narrow proof-point — the headline 71.3% completion is a single customer (Cedar/healthcare billing, high-intent inbound payers); not yet evidence of broad agentic-checkout conversion.

**What this changes (idea-lens).** (analysis) This is the de-PR'd signal that agent payments are moving from protocol announcements to live revenue — but value is accruing to the payments rail (Stripe), not automatically to the agent builder. Falsifiable thesis: Stripe becomes the default settlement layer for enterprise voice/chat agents via the App Marketplace. Watch for the trigger — PAP's deferred payments extension and whether fraud-liability terms get published; if card networks' authorization layers (Visa/Mastercard) or a bank-gated model (JPMorgan-style) win the trust layer, the thesis that Stripe owns agent-payment economics weakens.

Sources: https://sierra.ai/uk/blog/from-conversation-to-payment-sierra-and-stripe · https://www.juniperresearch.com/research/fintech-payments/ecommerce/agentic-commerce-research-report/ · https://stripe.com/newsroom/news/stripe-2025-update · https://assets.stripeassets.com/fzn2n1nzq965/3LlGw839Q6kUwxZlLZDtH6/75ddcbada4aa7743dd8ec7d0f9ca497e/Stripe-annual-letter-2025-desktop.pdf · https://techcrunch.com/2025/09/04/bret-taylors-sierra-raises-350m-at-a-10b-valuation · https://techstartups.com/2026/05/04/bret-taylors-ai-startup-sierra-raises-950m-at-15-8b-valuation-as-demand-for-ai-agents-surges/ · https://thepaypers.com/payments/news/meta-and-sierra-develop-personal-agent-protocol-for-ai-agents · https://wetheflywheel.com/en/agentic-commerce/acp-vs-ap2/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** NO FORMAL EARNINGS — this is a product/partnership announcement (Sierra × Stripe agentic payments), not a results print. Stripe is a private company with no quarterly reporting; its most recent self-disclosed financials come from its **2025 annual letter (published 2026-02-24)**: total payment volume **$1.9T (+34% YoY)**, "remained strongly profitable," at a **$159B** employee-tender valuation. These are context figures, not a reported quarter, so no beat/miss can be assessed. Formal/audited earnings are not available.

**Key figures (Stripe's most recent disclosures, from its own 2025 annual letter, 2026-02-24).**
- Total payment volume (TPV): **$1.9T in 2025, +34% YoY** (vs $1.4T in 2024) — ≈1.6% of global GDP. TPV is gross processed volume, NOT Stripe revenue.
- Profitability: "**remained strongly profitable**" in 2025 (first profitable year was 2024). No revenue or margin dollar figure disclosed.
- Revenue products (Billing, Invoicing, Tax, etc.): on track to reach **~$1B annual run-rate revenue** in 2026 (this is the Revenue-suite line, not total company revenue).
- Scale: powers **5M+ businesses** directly or via platforms, including "all of the top AI companies," 90% of the Dow and 80% of the Nasdaq 100.
- Valuation: **$159B** employee tender (2026-02-24), up from **$106.7B** a year earlier (+49%); prior points: $91.5B tender (2025-02), Series I $694M at ~$65B (2024-04).

**By segment / driver.** Growth narrative is AI-adjacent: TPV +34% and the Revenue suite nearing a $1B run-rate; the 2025 business cohort grew ~50% faster than the 2024 cohort, with 2x as many companies reaching $10M ARR within 3 months of launch. The Sierra tie-in sits inside Stripe's agentic-commerce push (Agentic Commerce Suite launched 2025-12-11; ChatGPT instant checkout with OpenAI 2025-09-29). Stripe's own letter frames agentic commerce at the Level 1–2 boundary of a five-stage framework, with **bot/agent payments still under 1% of total volume** — i.e. the Sierra partnership addresses a real but today-immaterial slice.

**vs expectations / prior period.** No consensus or prior-quarter comparison applies — Stripe is private with no quarterly cadence. YoY trajectory on TPV: $1.4T (2024) → $1.9T (2025), i.e. acceleration in absolute dollars while the growth rate holds in the mid-30s%. [UNSOURCED] for any quarterly revenue/EPS — none exists publicly.

**Guidance / forward.** No formal guidance (private, annual-letter only). Forward signals from the letter: Revenue suite guided toward a ~$1B run-rate in 2026; management tone confident on profitability and AI-infrastructure positioning. Notably silent on absolute company revenue, net margin, and any IPO timeline (press speculation exists but Stripe has not guided it). Agentic-payment revenue is not quantified — the Sierra deal is pre-monetization scale (one named client, Cedar, with 71.3% of started payments completing on-call).

**Thesis-flags.**
1. TPV +34% to $1.9T with sustained profitability → Stripe keeps compounding at scale without burning for growth; second-order: strengthens its hand as the default payments rail for AI/agent platforms, which is exactly what the Sierra integration monetizes long-term.
2. Agent/bot payments <1% of volume (Stripe's own number) → the Sierra news is strategically on-trend but financially immaterial today; flag against over-reading any single agentic-commerce partnership as a near-term revenue driver.
3. Revenue suite nearing $1B run-rate → the higher-margin software layer (not just processing) is scaling, which matters more for eventual public-market valuation than raw TPV. Stripe stays silent on total-company revenue, so margin quality remains partly opaque.
4. Valuation stepped $106.7B → $159B in one year (+49%) on steady ~34% volume growth → multiple expansion is being driven by the AI/agentic narrative; a risk flag if agent-payment adoption stays sub-1% longer than the market prices in.

Sources (Stripe self-disclosed is PRIMARY; aggregators for cross-check): Stripe 2025 annual letter / tender announcement 2026-02-24 <https://stripe.com/newsroom/news/stripe-2025-update> (drive: assets.stripeassets.com Stripe-annual-letter-2025-desktop.pdf) · Stripe annual update web <https://stripe.com/annual-updates/2025> · Sierra partnership post <https://sierra.ai/uk/blog/from-conversation-to-payment-sierra-and-stripe> · cross-check CNBC 2026-02-24 <https://www.cnbc.com/2026/02/24/stripe-value-stock-sale-tender-offer.html> · Yahoo Finance <https://finance.yahoo.com/news/stripe-reaches-159-billion-valuation-195143711.html>. No formal/audited earnings, no quarterly revenue, no consensus — Stripe is private: those are "no data"/[UNSOURCED] by nature.
<!-- /enrichment:earnings_review -->
