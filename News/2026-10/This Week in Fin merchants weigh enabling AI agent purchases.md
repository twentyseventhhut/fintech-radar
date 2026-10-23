---
title: "This Week in Fin: merchants weigh enabling AI agent purchases"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - company/openai
  - industry/agentic-commerce
  - industry/ai
  - region/us
  - type/commentary
sources:
  - http://firmly.ai
  - https://unsplash.com/@egorkomarov
  - https://www.removepaywall.com/search
status: enriched
n_mentions: 3
channels:
  - "This Week in Fintech"
story_id: sea6447ae
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# This Week in Fin: merchants weigh enabling AI agent purchases

> [!info] 2026-10-22 · 3 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] The company said it had not received prior warning for the agent crawling its site, and Muse didn’t identify itself when it did.

[This Week in Fintech] Still, merchant collaborations with tech are anything but a sure thing. Last year, OpenAI partnered with Walmart. The initial plan allowed consumers to make purchases directly through ChatGPT. That eventually fell apart just months later after sales weren’t as high as anticipated, and Walmart instead installed Sparky, its own chatbot, into Google Gemini and ChatGPT, WIRED reported at the time.

[This Week in Fintech] “It creates a dichotomy for the merchants, saying, ‘OK, where do I enable? Where do I stop? It's hard for them to figure out,” said Kumar N Senthil, the CEO of Firmly.AI. His company helps connect merchants to AI agents.

## Первоисточники

### firmly.ai
<http://firmly.ai>
*158 слов · direct*

firmly launches firmly Connect — sell through any AI agent with zero code
Buy now—anywhere.
The agentic commerce platform for instant, inspired purchases.
Introducing firmly Connect 
The first platform that connects merchants to any AI agent with zero engineering effort. One connection. Every agentic channel. Go live in hours, not months.
 Self-onboard through a guided flow — no dev resources needed 
 One integration covers every agentic protocol — UCP, ACP, MCP, AP2, TAP, and more 
 Future-proof — new protocols and channels are added automatically 
Buy wherever discovery occurs.
Discover.
Decide.
Checkout.
In one step.
firmly transforms product discovery into instant purchasing. From questions to conversions, our agentic platform embeds commerce at the point of intent, wherever customers are exploring.
 We make AI chatbots shoppable 
 We make social media shoppable 
 We make content shoppable 
 We make ads shoppable 
 We make messaging shoppable 
 We make CTV and livestream shoppable 
Contact us to learn more about our "buy now, anywhere" solutions

### Прочие ссылки (без извлечённого текста)

- <https://unsplash.com/@egorkomarov>
- <https://www.removepaywall.com/search>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: This Week in Fin — merchants weigh enabling AI-agent purchases
_Analytical notes (not a post). Importance: 3/5._

This is a weekly roundup/essay, not a single deal. Treat the core theme as the question every merchant now faces: **should I let autonomous AI agents transact on my site — and if so, where do I enable vs. block?** The note's own aggregated text already names the two live data points that define the debate right now (Oct 2026): Amazon blocking Meta's "Muse" agent, and Walmart's OpenAI ChatGPT-checkout tie-up that "fell apart" on weak conversion.

## [0] What exactly happened (de-PR'd)
The piece crystallizes a split that went from theoretical to concrete in Oct 2026:
- **Enable camp:** Walmart launched an **Agent Gateway** (cf. [[Walmart launches Agent Gateway for AI shopping agents]]) letting third-party agents buy on a customer's behalf within user-set limits (e.g. $50/$100 caps, transaction approvals). Walmart also pivoted from OpenAI's native Instant Checkout to embedding its own **Sparky** assistant inside ChatGPT and Gemini. TikTok shipped an agentic shopping assistant + checkout (cf. [[TikTok launches agentic AI shopping assistant and checkout]]).
- **Block camp:** Amazon broadly locks agents out via robots.txt + Conditions-of-Use enforcement; on ~Sep 20, 2026 it began blocking Meta's **Muse** agent (the note: Muse "didn't identify itself," no prior warning). Amazon earlier won — then lost on appeal (9th Cir. vacated, Aug 2026) — an injunction against Perplexity's Comet browser. eBay, Delta, JPMorgan, Schwab, Yelp also gate or license agent access.
- **Enabler layer:** Firmly.AI (the note's primary source) sells "connect to any agent with zero code," one integration spanning UCP/ACP/MCP/AP2/TAP. CEO Kumar N. Senthil frames the merchant's dilemma: "where do I enable? where do I stop?"

**Why structured this way / what it reveals:** The PR framing (from firmly.ai) is "frictionless omni-agent commerce is inevitable — plug in now." The de-PR'd reality is that the *merchant incentive is genuinely ambiguous*. Enabling agents risks (a) losing the customer relationship, first-party data and ad revenue to the agent/platform; (b) commoditizing your catalog into an agent's price-comparison feed; (c) weak conversion economics (see [3]). Blocking risks ceding discovery as agent traffic scales. So the essay's real subject is not a product but **who controls the shopper** once an LLM sits between buyer and store.

## [1] Competitors / peers — the two strategies and the rail owners
- **Rails/standards (the toll-collectors):** Visa **Trusted Agent Protocol** (cf. [[Visa launches Trusted Agent Protocol for AI commerce]]), Mastercard + PayPal agentic tie-up (cf. [[Mastercard and PayPal partner on agentic commerce]]), Google's **AP2** (cf. [[Affirm to support Google's Agent Payments Protocol]]), OpenAI/Stripe **Agentic Commerce Protocol / Instant Checkout** (cf. [[Stripe enables payments in ChatGPT with OpenAI]]), Coinbase x402. These define *how* an agent pays; they are largely merchant-neutral and sit upstream of the enable/block choice.
- **Enablers / middleware:** Firmly.AI, PayPal Agentic Commerce Services, Stripe. Their pitch assumes merchants *will* enable; their TAM depends on the enable camp winning.
- **Merchant archetypes:** Walmart (enable, but on *its own* terms via Sparky/Gateway — keep the account, the data, the checkout) vs. Amazon (block — protect the walled garden, ads, Prime flywheel). 

**Why the lay of the land is this way / second-order:** Amazon and Walmart block/enable for the *same* reason — protecting the customer graph — but reach opposite conclusions because of asymmetric exposure. Amazon *is* the discovery surface (its own search + ads = ~$50B+ ad business), so an external agent is pure cannibalization. Walmart is a distant #2 in e-commerce discovery, so agent traffic is incremental reach it can't get otherwise — hence "welcome mat." The telling detail: even Walmart's "enable" is defensive — Sparky keeps authentication and checkout *inside Walmart*, not in OpenAI's layer. Nobody wants to be the dumb inventory behind someone else's agent.

## [2] Company/theme history / fit
The agentic-commerce wave is ~12 months old as a *commercial* story: Stripe×OpenAI Instant Checkout (Oct 2025), Walmart×OpenAI (Oct 2025), Visa TAP (Oct 2025), Mastercard/PayPal (Oct 2025), PayPal's suite, Coinbase x402 — an entire 2025-10 cohort of announcements (see the dense cluster of News/2025-10 agentic notes). 2026 is the **reckoning year**: announcements meet adoption data, and the first failures surface (Walmart dropping OpenAI checkout after ~5 months on conversion roughly 1/3 of Walmart.com).

**Why the theme moves this way:** 2025 was protocol land-grab (everyone shipped a "rails" announcement to be in the conversation). 2026 forces the question announcements dodged — *does it convert, and who captures the value?* The structural pressure on merchants: agents compress the funnel (discover→decide→checkout in one step, per firmly's own copy), which is great for the agent/consumer but strips the merchant of the upsell, the retargeting pixel, and the brand touchpoint that justify their margin.

## [3] Novelty / value-add / traction — the hard numbers
Real novelty = we now have *adoption data*, not just protocols:
- Consumer pull is real: ~39% AI-shopping adoption cited; AI-referral traffic up ~800% YoY; AI-recommended products reportedly ~4.4x higher conversion *when the merchant is set up for it*.
- BUT raw agent checkout converts badly: ChatGPT/Instant-Checkout referrals convert ~86% worse than affiliate links; Walmart's OpenAI checkout converted ~3x worse than clicking through to Walmart.com. Walmart's own Sparky-in-ChatGPT reportedly recovers to ~70% of Walmart.com conversion — i.e. owning the experience beats renting it.
- Transaction execution still lags discovery: Regulation E doesn't cleanly say agent authorization = consumer consent; fraud liability, identity, chargebacks unresolved. Several analysts peg mainstream agent *purchasing* (vs back-office) as a 2027–2028 story.

**Why the value-add is real-but-contested / who captures the margin:** The durable value in agentic commerce is being captured *upstream* (payment rails: Visa/MC/Stripe) and *at the agent* (OpenAI, Google, Perplexity, TikTok), NOT at the merchant — unless the merchant forces the agent to transact inside its own authenticated environment (the Walmart/Sparky move). This flips the central question from "will agentic commerce happen?" (yes, discovery already is) to **"can a merchant enable agents without being disintermediated into a commodity feed?"** The firmly.AI "zero-code, every-protocol" pitch quietly concedes the merchant's weak hand: if you need a middleman to reach five fragmented protocols (UCP/ACP/MCP/AP2/TAP), you have no leverage in any of them.

## [4] What's next / market sentiment
- **Standards war continues** across UCP/ACP/MCP/AP2/TAP + Visa/MC/Google rails; expect consolidation, and payment networks positioned to be the neutral trust/identity layer (TAP) regardless of who wins the agent war.
- **Legal/regulatory:** the Amazon–Perplexity appeal ("the *user*, not the developer, does the accessing") weakens pure technical blocking; expect merchants to shift from "block" to "license/authenticate" (Yelp/Delta model). Reg E / consent, fraud-liability allocation are the gating unknowns.
- **Merchant playbook consensus forming:** enable *selectively* — authenticated, spend-capped, inside your own checkout — rather than open or closed. "Where do I enable, where do I stop" (Senthil) is the operative question for 2027.

**Why the market goes this way / counterintuitive second-order:** The intuitive read is "agents will route around blockers, so blocking is futile." The counterintuitive read: the *biggest* merchants (Amazon) can afford to block precisely because they ARE a discovery destination, while mid-tail merchants are forced to enable via middleware and thereby accelerate their own commoditization. Agentic commerce may therefore *widen* the gap between scaled destinations and everyone else, not flatten it — the opposite of the "democratized discovery" pitch.

## Sources
- firmly.ai (note primary source).
- TechCrunch, "While Amazon blocks AI agents, Walmart rolls out the welcome mat" (Oct 21, 2026).
- ThePaypers / TheStreet / mlq.ai — Walmart drops OpenAI checkout, deploys Sparky (conversion ~1/3 of Walmart.com; Sparky ~70%).
- CNBC / Seeking Alpha — Amazon v. Perplexity injunction (Mar 2026) vacated by 9th Cir. (Aug 2026).
- Forrester, "Agentic Payments in B2C Commerce: Where We Are Now"; FintechFutures, "Agentic commerce in 2026."
- Chargeflow — agentic-commerce regulation / Reg E; Yahoo Finance / MetaRouter — adoption + conversion stats.
- Internal corpus: [[Walmart launches Agent Gateway for AI shopping agents]], [[TikTok launches agentic AI shopping assistant and checkout]], [[Walmart partners OpenAI for ChatGPT checkout]], [[Stripe enables payments in ChatGPT with OpenAI]], [[Visa launches Trusted Agent Protocol for AI commerce]], [[Mastercard and PayPal partner on agentic commerce]], [[Affirm to support Google's Agent Payments Protocol]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is the theme actually new, or a 2025 re-run?** The *protocols* are 2025; the novelty is 2026 *adoption + failure data* (Walmart dropping OpenAI checkout, Amazon blocking Muse, conversion numbers). Fresh as an essay on the block-vs-enable reckoning, not a re-report of a single prior deal. **Fresh.**

2. **Does enabling agents actually convert?** Mostly no, yet: raw ChatGPT/Instant-Checkout referrals convert ~86% worse than affiliate links; Walmart's OpenAI checkout ~3x worse than Walmart.com. Only merchant-owned flows (Sparky ~70% of Walmart.com) hold up. So "enable" ≠ "revenue."

3. **Who captures the margin once an agent mediates?** Upstream rails (Visa/MC/Stripe) and the agent platforms (OpenAI/Google/TikTok) — not the merchant, unless it forces checkout into its own authenticated environment. This is the load-bearing point.

4. **Why does Amazon block while Walmart enables — same incentive, opposite call?** Both protect the customer graph. Amazon IS the discovery/ad surface (cannibalization), Walmart is #2 (incremental reach). Asymmetric exposure, not disagreement on principle.

5. **Is blocking even legally durable?** Weak: 9th Cir. (Aug 2026) vacated Amazon's injunction against Perplexity — "the *user* accesses, not the developer." Expect a shift from block → license/authenticate (Delta/Yelp model). Open: how courts treat robots.txt + CoU going forward.

6. **Does Reg E / consent law resolve agent authorization = consumer consent?** No — explicitly unsettled. Fraud-liability allocation and chargeback responsibility for agent-initiated buys are the real gating unknowns. Open.

7. **Is firmly.AI's "zero-code, every-protocol" pitch a signal of merchant strength or weakness?** Weakness: needing a middleman across five fragmented protocols (UCP/ACP/MCP/AP2/TAP) means no leverage in any one. The enabler TAM exists *because* merchants have a poor hand.

8. **Is consumer demand real or hype?** Demand/discovery is real (~39% adoption, ~800% AI-referral traffic growth, ~4.4x conversion on AI-recommended products *when set up*). Execution/purchasing is the lagging half — plausibly a 2027-2028 mainstream story.

9. **Could agentic commerce widen, not flatten, the retail gap?** Yes (counterintuitive): scaled destinations can afford to block; mid-tail merchants must enable via middleware and accelerate their own commoditization into price-comparison feeds.

10. **What's silent in the enabler PR?** First-party data loss, ad-revenue loss, brand/upsell loss, and conversion economics — all absent from firmly's "buy now, anywhere" framing.

11. **Which standard wins, and does it matter to the merchant?** Unclear; likely multi-protocol coexistence with payment networks (Visa TAP) as neutral trust/identity layer. For merchants the standard matters less than *where checkout happens* (their env vs the agent's).

12. **Is "merchant collaborations with tech are anything but a sure thing" overstated?** No — the Walmart/OpenAI unwind after ~5 months is direct evidence. One-off pilots fail on economics even when the tech works.

13. **What would change the verdict to "enable aggressively"?** Conversion parity with first-party web + a clean liability/consent framework + agents that preserve merchant branding. None present as of Oct 2026.

14. **Is this note a duplicate of the Walmart Agent Gateway or TikTok notes?** No — those are single-deal product launches; this is a cross-cutting commentary synthesizing the merchant dilemma. Complementary, not duplicative.

15. **Downside trigger for the whole theme?** A high-profile fraud/liability case on an agent-initiated purchase, or a wave of merchant blocks, could freeze enablement into 2027+.

**Importance: 3/5** — a well-framed, timely synthesis of the single most important structural question in payments right now (who controls the shopper when an LLM mediates), anchored to concrete Oct-2026 data points (Walmart/OpenAI unwind, Amazon/Muse block, conversion figures). Docked from 4 because it is commentary, not a new event or a deal with its own numbers — its weight is derivative of the underlying stories it aggregates.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce — AI agents that discover, decide and pay on a shopper's behalf — sits between two layers every player wants to own: *discovery* (the LLM/chatbot surface) and *checkout* (the payment rail + merchant of record). TAM estimates are wide and definition-dependent, so treat them as directional, not sourced truth: Juniper Research pegs global agentic-commerce transaction value at ~$8bn in 2026 rising to ~$3.5tn by 2031; McKinsey projects agentic channels could *mediate* $3–5tn of consumer commerce by 2030; Gartner expects 20% of digital-commerce transactions to run through AI platforms (on-platform or via agents) by 2030 (per Juniper/McKinsey/Gartner, via secondary analyst citations, as of 2026; narrower "autonomous checkout" numbers are far smaller, ~$17–20bn US retail in 2026). "Why now": the protocol land-grab of late-2025/2026 — OpenAI+Stripe's ACP, Google's AP2, Visa's Trusted Agent Protocol (TAP, Oct-2025), Mastercard Agent Pay / Agent Pay for Machines (Jun-2026), PayPal's ACP adoption — means the *plumbing* now exists, so the binding constraint has shifted to merchant willingness to expose catalog + checkout to third-party agents. Structure: the rail/protocol layer is consolidating fast around Visa/Mastercard/Stripe/PayPal (network effects + existing merchant relationships = high barriers), while the merchant-connector layer (Firmly, Basis Theory, DEUNA, Nuvei, Splitit) is fragmented and VC-funded.

**Competitive landscape.** Sector KPIs: for connectors — merchants onboarded, agentic channels covered, time-to-live, take rate per agentic transaction; for merchants — agentic conversion rate vs. own-site click-through, fraud/chargeback liability, incremental vs. cannibalized GMV. Players by layer: *discovery/agent surface* — OpenAI (ChatGPT), Google (Gemini), Perplexity, Anthropic (ran "Project Deal" commerce experiment, [[Anthropic runs agentic commerce experiment Project Deal]]); *rails/protocols* — Visa TAP ([[Visa launches Trusted Agent Protocol for AI commerce]]), Mastercard Agent Pay ([[Mastercard and PayPal partner on agentic commerce]]), Stripe/ACP ([[Stripe enables payments in ChatGPT with OpenAI]]), PayPal ([[PayPal adopts Agentic Commerce Protocol, expands in ChatGPT]]); *merchant connectors* — Firmly (the protagonist), Basis Theory ([[Basis Theory raises $33 million for agentic commerce]]), DEUNA, Splitit ([[Splitit launches partner program for agentic commerce]]). Firmly's position (analysis): niche but strategically placed — a multi-protocol abstraction layer (UCP/ACP/MCP/AP2/TAP) that lets merchants "go live in hours, zero code." Its moat is a thin switching-cost/aggregation play, not a network — it is a toll-collector *on top of* rails it doesn't control. Recent credibility signal: selected into Mastercard's Start Path Emerging Fintech cohort (Sep-2026) and an Aurus gateway partnership (per GlobeNewswire/PYMNTS).

**Comps & multiples.** Firmly's round size/valuation is not disclosed in the note or in public sources found — valuation multiples = no data / `[UNSOURCED]`. Internal funding comp: [[Basis Theory raises $33 million for agentic commerce]] (same subvertical — merchant/agentic payment infra, $33M raise, Oct-2025); directionally this bounds the connector-layer at tens-of-millions rounds, not the billions commanded by the rail incumbents. Public-market anchors for the rail layer (Visa, Mastercard, PayPal, Stripe-private) are not comparable to an early-stage connector (different model/scale/stage) — comparison is qualitative only; distribution not computed (only 1 comparable in-base figure). Takeaway: connector valuations hinge entirely on unproven take-rate durability, not on current GMV.

**Risk flags.**
1. **Disintermediation — the core existential risk.** The Walmart/OpenAI episode is the de-PR'd evidence: Walmart's ChatGPT Instant Checkout reportedly converted ~3x *lower* than click-through to its own site, so Walmart killed native checkout and embedded its own assistant (Sparky) into ChatGPT/Gemini, keeping checkout on its own stack (per RetailDive/ThePaypers, 2026). If large merchants retain checkout and only expose *discovery*, the connector layer that sells "sell *through* any agent" loses its highest-value function.
2. **Rails squeeze the middle.** Visa/Mastercard/Stripe/PayPal are shipping their own low-/zero-code agent toolkits (MCP servers, Agent Toolkit, SPTs). A connector sitting between merchants and these rails risks being bypassed as the networks extend direct merchant onboarding — margin captured by the layer below.
3. **Trust/fraud + "uninvited agent" liability (unresolved).** The note itself flags an agent ("Muse") crawling a site without identifying itself and without warning — the fraud-liability and consent model for agent traffic is unsettled, and no one in the stack is loudly owning chargeback liability. Regulatory/liability ambiguity is a direct headwind to merchant adoption.

**What this changes (idea-lens).** (analysis) The strategic question is not "will agents shop" but "who owns checkout" — and the Walmart reversal tilts the answer toward merchants-keep-checkout, agents-own-discovery. Falsifiable thesis: if the merchant-keeps-checkout pattern generalizes, pure "sell-through-any-agent" connectors re-rate down toward discovery/affiliate plumbing, while rail incumbents and merchants capture the economics. Trigger to watch: whether any top-20 retailer sustains *native* in-agent checkout past a full holiday season with conversion at parity to own-site — absence of that is the signal connectors are structurally pinched. What would break the thesis: a rail/protocol settling fraud liability cleanly enough that merchants reopen native agent checkout at scale.

Sources: https://www.retaildive.com/news/walmart-sparky-chatgpt-instant-checkout/815647/ · https://thepaypers.com/payments/news/walmart-drops-openai-checkout-and-deploys-sparky-on-ai-platforms · https://www.juniperresearch.com/resources/blog/paying-at-agentic-speed-inside-visa-mastercard-and-stripe-s-agentic-commerce-push/ · https://www.pymnts.com/news/artificial-intelligence/2025/firmly-launches-platform-that-eases-merchant-adoption-of-agentic-commerce/ · https://stellagent.ai/insights/agentic-commerce-market-size-forecast-2030
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
