---
title: "Walmart launches Agent Gateway for AI shopping agents"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/walmart
  - industry/agentic-commerce
  - industry/ai
  - region/us
  - type/product
sources:
  - https://www.theverge.com/ai-artificial-intelligence/1015715/walmart-ai-shopping-agents
status: published
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sfe6ba5a1
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Walmart launches Agent Gateway for AI shopping agents

> [!info] 2026-10-23 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Walmart представил платформу Agent Gateway, которая позволит AI-агентам, включая ChatGPT, Gemini и Muse, искать товары и оформлять заказы в Walmart и Sam’s Club. Платформа уже доступна в бета-версии и использует протокол MCP для прямого подключения AI-агентов к системам ритейлера. В ноябре компания запустит Agent Profiles — отдельные профили для агентов, позволяющие отслеживать их покупки независимо от заказов пользователя. Покупатель сможет подтверждать каждую транзакцию или разрешить агенту самостоятельно тратить деньги в пределах установленного лимита, а также в любой момент отзывать доступ. AI-агенты не получат доступ к данным банковских карт и не смогут менять способы оплаты, а пользоваться новыми функциями можно будет без подписки Walmart+

## Первоисточники

### theverge.com
<https://www.theverge.com/ai-artificial-intelligence/1015715/walmart-ai-shopping-agents>
*454 слов · direct*

AI 
 News 
 Tech 
Walmart is inviting AI agents to shop for you
While Amazon shuts out AI agents, Walmart is letting them in.
While Amazon shuts out AI agents, Walmart is letting them in.
 Link 
 Share 
 Gift 
If you buy something from a link, The Verge may earn a commission. See our ethics statement. 
Walmart will soon let AI agents shop on its website for you. Next month, the retail giant will allow you to use an AI agent on the site, with systems in place to let you approve and review purchases and set spending limits.
The embrace of AI agents stands in stark contrast to Amazon, which blocked Perplexity’s shopping agent and Meta’s Muse AI assistant . But Walmart is opening its doors to AI shoppers — as long as they follow the retailer’s rules. It has outlined a set of terms for agents, saying that “agents must not take actions beyond what the shopper intends” and cannot change a customer’s payment method. Agents also can only access information needed to complete their task. Walmart says it will block agents that don’t follow these terms.
Related
 Websites are closing their doors to AI agents 
Agents will connect to new “Agent Profiles” within Walmart. By default, Walmart will require approval for all AI agent purchases, but you can also let it shop within a certain budget, such as up to $100. You’ll also be able to review your agent’s purchases separately from your own in Agent Profiles, as well as turn off the agent at any time.
The retailer has built an “Agent Gateway,” currently available in beta , that connects AI agents through the Model Context Protocol, an open standard that allows AI agents to plug into different services on the web. Walmart says this not only enables AI agents to shop without running into hiccups that they might encounter when navigating a browser, but also prevents them from accessing your shopping history and personal information.
“For example, if a customer tends to buy sourdough bread or a particular brand of milk, Walmart will help the agent find those usual items for the customer without sharing the customer’s broader shopping history with the agent,” Walmart says. The company will let users shop with AI agents on Sam’s Club as well.



 Emma Roth 
 AI 
 News 
 Online Shopping 
 Tech 
Most Popular
 Trump says Sundar Pichai talked him out of renaming the Atlantic Ocean 
 Tesla driver using Full Self-Driving struck and killed a man crossing I-80 
 Bill Gates says to prepare for 20 years of ‘tumultuous’ AI disruption Video 
 The iPhone Duo is a messy, expensive, good time 
 Sure, let’s smoosh SpaceX and Tesla together, who cares 
This is the title for the native ad

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Walmart launches Agent Gateway for AI shopping agents
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
Walmart (Oct 21, 2026) shipped three things for third-party AI agents shopping on Walmart.com / Sam's Club: (a) **Agent Gateway** — a technical connector exposing Walmart's catalog/checkout to agents via **MCP** (Model Context Protocol, the Anthropic-created open standard), now in **beta for developers/companies**; (b) **Agent Profiles** — launching "next month" (Nov 2026), a dedicated sub-profile per authorized agent that segregates agent purchases from the user's own order history and carries guardrails; (c) **terms of use for agents** (agents "must not act beyond shopper intent," cannot change payment method, can only access task-necessary data, non-compliant agents get blocked).
- **Guardrails, de-PR'd:** default = approve every basket; optional autonomous spend caps ($50/$100/$200 per sources, "up to $100" per The Verge). Agents never see card data or full shopping history — Walmart brokers "find the usual sourdough" without exposing the history. No Walmart+ subscription required.
- **Why this way — and the real story the PR buries:** this is **not Walmart opening a door; it's Walmart taking the door back.** In Oct 2025 Walmart partnered OpenAI so customers checked out *inside ChatGPT* via **Instant Checkout** ([[Walmart partners OpenAI for ChatGPT checkout]]). That rail converted ~3x *worse* than Walmart.com and couldn't see real-time inventory, coupons, loyalty, or store pickup — so OpenAI killed Instant Checkout and pivoted to a discovery-first ACP ([[OpenAI scales back ChatGPT shopping plans]]). Agent Gateway inverts the topology: the **agent discovers inside ChatGPT/Gemini, but checkout and fulfillment stay inside Walmart's own stack** (Walmart is also pushing its proprietary **Sparky** assistant into ChatGPT and Gemini). So the frame isn't "AI-friendly retailer" vs "Amazon the blocker" — it's "retailer refusing to be disintermediated at checkout while still appearing in the agent's answer."

## [1] Competitors / peers
- **Amazon (the deliberate foil):** The Verge's hook — "Amazon shuts out AI agents, Walmart lets them in" — maps to real litigation. Amazon sued Perplexity (Comet) under the CFAA; a preliminary injunction (Judge Chesney) blocked Comet, the 9th Cir. briefly reversed on "the *user* accesses, not Perplexity," and as of ~Oct 23 2026 a judge again ordered Comet to stop and delete data. Amazon also blocked Meta's agent. **Why opposite strategies:** Amazon owns demand (Prime) and fears margin/ads/Buy-Box disintermediation, so it litigates for *authorization control*; Walmart, #2 in e-com, uses "agent-open" as a *share-grab wedge* — but with MCP + terms + Agent Profiles it keeps the same control Amazon seeks via courts, just via API design instead of lawsuits.
- **OpenAI/Stripe ACP:** retailer-owns-checkout discovery model (Target, Sephora, Nordstrom, Lowe's, Best Buy, Home Depot, Wayfair integrated). Walmart's Gateway is a **generalized, multi-agent** version of the same insight (works with ChatGPT, Gemini, "Muse").
- **Payment-rail layer (who actually captures the transaction):** Visa **TAP** (crypto-signed agent identity/intent token, Web Bot Auth) [[Visa launches Trusted Agent Protocol for AI commerce]]; Mastercard **Agent Pay** / Agentic Tokens [[Mastercard and PayPal partner on agentic commerce]]; Google **AP2** [[Affirm to support Google's Agent Payments Protocol]]; Coinbase **x402/Payments MCP** [[Coinbase launches Payments MCP for AI agents]]. Walmart's own **OnePay** has positioned as an AP2 *credential provider* — so Walmart potentially owns both the merchant endpoint (Gateway) and the credential layer (OnePay).
- **Position:** ahead of US peers on a *first-party, catalog-wide agent API* (vs per-platform ACP onboarding); parity-or-behind on the payment-authentication primitive, which is being set by Visa/Mastercard, not Walmart.

## [2] Company history / fit
Walmart's agentic/payments arc is dense and internally consistent: ChatGPT checkout (Oct 2025) → OnePay hits $4B valuation (Jan 2026) [[Walmart-backed OnePay hits $4 billion valuation]], Klarna BNPL, Bitcoin/crypto rails for 150m users [[Walmart embraces Bitcoin, opening crypto payments to 150m users]], Tempo stablecoin cross-border, Workday HR. **Why Walmart acts this way:** it is a thin-margin commodity retailer buying itself a software/fintech multiple via OnePay and now an agent-commerce control point. Opening to agents *grows the top of funnel* (every ChatGPT/Gemini shopper becomes reachable) while MCP + Agent Profiles + OnePay keep the *margin-bearing* steps (checkout, credential, data) in-house. Learning from the Instant-Checkout failure, it chose the architecture where the retailer's operational plumbing (inventory, pickup, loyalty, returns) stays authoritative.

## [3] Novelty / value-add / traction
- **Genuinely new vs the 2025 note:** yes — different architecture and different counterparty posture. 2025 = Walmart *inside* OpenAI's checkout; 2026 = agents *inside* Walmart via first-party MCP gateway with agent-specific identity/guardrails. The Agent-Profile construct (per-agent sub-identity + spend caps + revocable access + segregated order history + data minimization) is the most concrete merchant-side agent-governance primitive shipped by a top US retailer.
- **Traction reality check:** Gateway is **beta**; Agent Profiles **not yet live** (Nov). Zero disclosed agent-GMV, zero named integrated agents actually transacting, "Muse" referenced loosely. This is "announced + beta," not adoption. Instant Checkout's flop (~30 Shopify merchants, <200k Walmart SKUs, 3x worse conversion) is the cautionary baseline for how far "announced" is from "works."
- **Who captures the margin (the central question):** discovery is commoditizing toward the agent platforms (ChatGPT/Gemini); the durable value is in *checkout + credential + fulfillment + first-party data*. Walmart's move is precisely an attempt to **keep the margin-bearing layer** while conceding discovery. The risk: if Visa TAP / Mastercard Agent Pay become the mandatory agent-auth rail, the networks re-capture their interchange + an "agent identity" toll, and Walmart's Gateway becomes a compliant endpoint rather than the value sink — unless OnePay rides as the credential provider.

## [4] What's next / market sentiment
- Nov 2026: Agent Profiles go live; watch for *named* agents transacting and any GMV/conversion disclosure (the only metrics that matter given the Instant Checkout flop).
- Structural driver: agentic commerce is consolidating into a **protocol stack** — discovery (ACP), identity/auth (Visa TAP, MC Agent Pay, AP2), merchant endpoint (Walmart Gateway / ACP integrations), credential (OnePay). The 2025 "protocol wars" are resolving into layered coexistence, not a single winner.
- Regulatory/legal backdrop: Amazon v. Perplexity makes *authorization* the live legal question; Walmart's explicit agent terms + blocking rights are its pre-emptive answer, converting a courtroom fight into an API ToS — a model others will copy.
- **Counterintuitive second-order:** "opening to agents" looks like generosity but is a *defensive moat* — by standardizing agent access on its own terms, Walmart denies agent platforms the leverage to dictate checkout, and makes itself the reference implementation other retailers benchmark against. The fragility: it still doesn't own the agent-identity primitive, so a networks-led auth standard could tax every agent transaction regardless of whose gateway it hits.

## Sources
- The Verge, "Walmart is inviting AI agents to shop for you," 2026-10-23 (note primary source)
- unite.ai / thenextweb / chainstoreage / cryptopolitan / theaiinsider — Agent Gateway, Agent Profiles, MCP, $50/$100/$200 caps, Oct 21 2026 announcement
- thepaypers / paymentsdive / enterprisedna / retaildive — Walmart Sparky in ChatGPT & Gemini; OpenAI Instant Checkout retired; ACP pivot; Instant Checkout conversion/traction stats
- finovate — OnePay as AP2 credential provider; useproxy.ai / agenticcommerce.report — Visa TAP, Mastercard Agent Pay, AP2 rails
- geekwire / searchenginejournal / thenextweb — Amazon v. Perplexity Comet CFAA litigation (2026)
- Internal: [[Walmart partners OpenAI for ChatGPT checkout]], [[OpenAI scales back ChatGPT shopping plans]], [[Visa launches Trusted Agent Protocol for AI commerce]], [[Mastercard and PayPal partner on agentic commerce]], [[Affirm to support Google's Agent Payments Protocol]], [[Coinbase launches Payments MCP for AI agents]], [[Walmart-backed OnePay hits $4 billion valuation]], [[Walmart embraces Bitcoin, opening crypto payments to 150m users]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 4/5** — A strategically significant, well-sourced pivot by the #2 US e-commerce player that reframes agentic commerce (merchant reclaims checkout from the AI platform) and sits directly against the Amazon-v-Perplexity legal fight. Not a 5 because it is still beta / pre-launch (Agent Profiles Nov 2026) with zero disclosed agent-GMV, and the previous Walmart agentic checkout (Instant Checkout) materially flopped — announced ambition, unproven adoption.

1. Is this actually new vs the Oct-2025 OpenAI/ChatGPT checkout note? Yes — different architecture (first-party MCP gateway vs checkout-inside-ChatGPT) and a reversal of posture after Instant Checkout's failure. **Fresh.**
2. Live or announced? Agent Gateway = **beta**; Agent Profiles = **not live until Nov 2026**. No agent is confirmed transacting at scale. (mostly announced)
3. What's the hard traction number? None disclosed — no agent-GMV, no conversion, no named integrated agent actually buying. Open.
4. Did Walmart's prior agentic checkout fly? No — Instant Checkout converted ~3x worse than Walmart.com, <200k SKUs exposed, and OpenAI killed it. This is the base rate for "announced." (answered)
5. Precise mechanism delta vs ACP (OpenAI/Stripe)? ACP = discovery-first, retailer-owns-checkout per-platform; Gateway = generalized first-party MCP endpoint usable by any compliant agent (ChatGPT, Gemini, Muse). (answered)
6. Who captures the margin? Discovery commoditizes toward agent platforms; Walmart fights to keep checkout+credential+fulfillment+first-party data. The networks (Visa TAP / MC Agent Pay) threaten to re-capture an "agent identity + interchange" toll. (analysis)
7. Does Walmart own the agent-identity primitive? No — that's being set by Visa TAP / Mastercard Agent Pay / Google AP2. OnePay-as-AP2-credential-provider is Walmart's hedge, but unconfirmed as live in this launch. Open.
8. Is "open to agents" generosity or a moat? A defensive moat — standardizing agent access on Walmart's ToS denies platforms leverage over checkout while mimicking the control Amazon seeks via lawsuits. (analysis)
9. What's the real Amazon contrast? Amazon litigates (CFAA, Perplexity Comet injunction Oct 2026); Walmart codifies the same control in API terms + blocking rights. Different tactic, similar objective: authorization control. (answered)
10. Fraud / liability silence: who eats a misbehaving agent's bad purchase? Walmart says standard returns apply even if an agent misbehaves, but liability allocation between shopper, agent provider, and Walmart on unauthorized/over-limit spend is unstated. Open.
11. What does "agent must not act beyond shopper intent" mean operationally, and who adjudicates intent? Undefined enforcement mechanism beyond blocking non-compliant agents. Open.
12. Spend-cap discrepancy: $50/$100/$200 (trade press) vs "up to $100" (The Verge) — which is the shipping config? Minor, open.
13. Does Sparky-in-ChatGPT/Gemini compete with or complement the Gateway? Complement: Sparky = Walmart's first-party assistant surface; Gateway = the plumbing any agent uses. Both keep checkout in Walmart. (answered)
14. Second-order fragility: if a networks-led auth standard becomes mandatory, does Gateway reduce Walmart to a compliant endpoint rather than the value sink? Plausible downside trigger. (hypothesis)
15. Will other retailers copy the Agent-Profiles-as-ToS model, making it a de facto standard? Likely, given ACP retailers already lean retailer-owns-checkout; watch Target/Best Buy for first-party gateways. (hypothesis)
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-24]] (2026-10-24).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce — AI agents that search, select and transact on a shopper's behalf — is the fastest-moving sub-vertical in retail/payments, but sizing is highly definition-dependent. Forecasts for 2030: Morgan Stanley sees agentic shoppers at $190bn–$385bn of US e-commerce spend (~10% of online retail, up to 20% optimistic); Bain at $300bn–$500bn / 15–25% of US online sales; IDC pegs the (narrower) global agentic-commerce market at $18.4bn in 2025 → $187bn by 2030 (per Morgan Stanley / Bain / IDC via secondary citations, as of 2025–2026). Treat these as directional, not reconciled — the spread reflects "agent-completed" vs "AI-influenced" definitional drift; no single defensible TAM, so (analysis) not a hard figure. Structure: the value chain is consolidating around three contested control points — (1) the agent/model layer (OpenAI, Google Gemini, Perplexity, Microsoft/Muse), (2) the payment/checkout rail (Stripe+OpenAI's Agentic Commerce Protocol, PayPal, Mastercard Agent Pay, Visa), and (3) the merchant/catalog endpoint (Walmart, Amazon). Barriers are high at each end (scale, catalog, fraud liability, payment licensing) but the middle "agent↔merchant interface" is up for grabs — whoever sets the connection standard captures the economics. Why now: MCP has become the de-facto open standard for agent↔service plumbing, and the Amazon-vs-Perplexity litigation (below) forced every large retailer to pick a posture — block or gate — in 2026.

**Competitive landscape.** Sector KPIs: for the retailer, e-commerce GMV growth, advertising (retail-media) revenue, and marketplace take rate; for the agentic layer, agent-driven conversion and attach to existing checkout. Walmart's own run-rate is the backdrop: FY27 Q1 (quarter ended Apr 30, 2026) revenue $177.8bn (+7.3% reported, +5.9% cc), global e-commerce +26% YoY, marketplace ~+50% (best in 10 quarters), and global advertising +37% (Walmart Connect US +44%), with membership income +17.4% — i.e. the fastest-growing, highest-margin parts of Walmart are exactly e-commerce + ads, the two lines an agent channel feeds (per Walmart FY27 Q1 Earnings Release, May 21 2026). Basis of competition is **posture toward agents**, not price: Amazon sued Perplexity (Nov 2025) under the CFAA, won a preliminary injunction (Mar 2026), then had it lifted by the 9th Circuit (Aug 2026) — Amazon = gatekeeper/block. Walmart = controlled-open: Agent Gateway is an invite-only MCP server; by-default per-purchase approval; optional spend caps ($50/$100/$200); agents barred from exceeding user intent, touching payment data or over-collecting; non-compliant agents blocked (per Walmart corporate newsroom + TechCrunch, Oct 21 2026). Recent peer moves: Walmart×OpenAI ChatGPT Instant Checkout [[Walmart partners OpenAI for ChatGPT checkout]] (Oct 14 2025); Stripe/OpenAI ACP [[Stripe enables payments in ChatGPT with OpenAI]] (Oct 1 2025); [[PayPal launches Agentic Commerce Services for AI checkout]] (Oct 28 2025); [[Mastercard and PayPal partner on agentic commerce]] (Oct 27 2025); [[Basis Theory raises $33 million for agentic commerce]]; [[PayPal adopts Agentic Commerce Protocol, expands in ChatGPT]]. Walmart's position: **ahead among merchants** on standing up its own agent interface rather than ceding it to a model or wallet. Moat = scale + first-party catalog/inventory + the Gateway as a switching-cost chokepoint: agents must integrate to Walmart's MCP terms, so Walmart — not the agent — keeps the customer relationship, shopping history and (critically) the ad surface (analysis).

**Comps & multiples.** Walmart (WMT) is a public mega-cap; a trading multiple here would reflect the whole retailer, not this product, so a comp multiple is not meaningful for pricing the Agent Gateway and is not computed. For internal comparability, the right comps are other agentic-commerce plays in-base rather than valuation peers: [[Walmart partners OpenAI for ChatGPT checkout]] (same company, the checkout side vs this connection side), [[PayPal launches Agentic Commerce Services for AI checkout]] and [[Mastercard and PayPal partner on agentic commerce]] (payment-rail contenders for the same transaction), [[Stripe enables payments in ChatGPT with OpenAI]] (the ACP standard Walmart's rail will likely touch), and [[Basis Theory raises $33 million for agentic commerce]] (infra financing signal). Deal/round multiples: no disclosed economics for any of these agent integrations — take rate, agent-referred GMV and ad load are all undisclosed → no data / [UNSOURCED]. Qualitative comparison only; distribution not computed.

**Risk flags.**
1. **Disintermediation of the customer relationship.** If shoppers increasingly start at the agent (ChatGPT/Gemini) rather than walmart.com, the model layer — not Walmart — owns discovery and first-party data; the Gateway is Walmart's bid to keep itself the merchant of record, but it structurally hands the top of the funnel to third-party agents. Second-order: pressure on Walmart Connect ad inventory, the +37%-growing, high-margin line, if impressions move to an agent surface Walmart doesn't monetize.
2. **Standard/platform risk around MCP + ACP.** Walmart is betting on MCP and (via its OpenAI tie-up) effectively ACP; if a rival standard (e.g. a Google/Visa "AP2"-style rail or Mastercard Agent Pay) wins, or if agents fragment across incompatible protocols, integration cost and loss of neutrality rise. Walmart controls the endpoint, not the protocol.
3. **Fraud/liability and consent-flow execution.** Spend caps and per-purchase approval shift but don't remove liability: an agent acting "beyond user intent," erroneous auto-spend within a cap, or a blocked-but-persistent agent creates chargeback, trust and regulatory exposure — exactly the economics (fraud liability, who eats a bad agent order) the announcement is silent on (de-PR flag).

**What this changes (idea-lens).** This is the merchant side drawing a line: rather than block agents (Amazon) or surrender the interface to a model/wallet, Walmart is trying to become the *gateway operator* for agentic retail — commoditize the agent, keep the catalog, data and ad surface (analysis). Falsifiable thesis: if the Gateway sticks, expect Walmart to disclose agent-referred GMV / an "agent ad" product within 2–3 quarters and other big-box retailers (Target, Kroger) to ship MCP endpoints on similar terms. What would break it: agents (or regulators, post-9th-Circuit) refusing invite-only gating and routing around Walmart via general browsers, or OpenAI/Google launching their own checkout that bypasses merchant gateways entirely. Trigger to watch: Agent Profiles GA (late Nov 2026) and the first disclosed agent-channel metric.

Sources: https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers · https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/ · https://www.sec.gov/Archives/edgar/data/104169/000010416926000095/earningsreleasefy27q1.htm · https://stock.walmart.com/_assets/_073745ae8c54e2cd48e8e649fea81965/walmart/db/938/9995/earnings_release/Earnings+Release+(FY27+Q1).pdf · https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook · https://www.digitalcommerce360.com/2025/12/22/bain-agentic-ai-us-ecommerce-sales-2030/ · https://www.cnbc.com/2026/03/10/amazon-wins-court-order-to-block-perplexitys-ai-shopping-agent.html · https://thenextweb.com/news/amazon-loses-perplexity-comet-ai-shopping-ruling
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Note:** This pick is a product announcement (Agent Gateway), not an earnings print. The company is IR-covered, so the most recent reported quarter is added here as material context for the agentic-commerce thesis — Walmart's e-commerce, marketplace and advertising (Walmart Connect) momentum is exactly the engine an agent-shopping channel is meant to feed.

**Verdict (headline read).** BEAT · Q2 FY27 (quarter ended Jul 31, 2026, reported Aug 20, 2026) · total revenue $187.9bn (+5.9% YoY; +5.1% cc) vs public consensus ~$186.6bn (beat ~+$1.3bn / ~+0.7%) · adjusted EPS $0.81 vs consensus ~$0.74 (beat +$0.07 / ~+9%) · GAAP EPS $0.80 · drivers: e-commerce +23% global, advertising +38%, operating leverage · guidance RAISED for FY27.

**Key figures (with growth).**
- Total revenue $187.9bn, +5.9% YoY (+5.1% constant currency). Consolidated net sales $186.1bn, +5.9% (+5.0% cc).
- GAAP operating income $9.383bn, +28.8% YoY; adjusted operating income +17.4% cc (GAAP inflated by one-offs — see thesis-flags). Gross profit rate +96 bps.
- GAAP EPS $0.80; adjusted EPS $0.81.
- Walmart U.S. comp sales (ex-fuel) +2.6%, led by +1.5% transactions, with a ~125 bps drag from health-and-wellness deflation — the slowest U.S. comp in ~six years. Sam's Club U.S. comp (ex-fuel) +4.4%.
- Global e-commerce +23%; Walmart U.S. e-commerce +24%; Sam's Club U.S. e-commerce +26%. Store-fulfilled delivery (Walmart U.S.) +40%. Marketplace net sales +>50%.
- Global advertising +38%; Walmart Connect (U.S., ex-VIZIO) +43%. Membership fee income +17% globally.

**By segment / driver.** Profit is running ahead of the top line: operating income +28.8% GAAP vs revenue +5.9%, on +96 bps gross margin plus the high-margin "flywheel" lines — advertising +38%, marketplace +>50%, membership +17%. Core U.S. store traffic is decelerating (comp +2.6%, transactions +1.5%, a six-year low), so the growth mix is shifting toward digital + monetization rather than same-store volume. That mix shift is the crux for the Agent Gateway story: agentic commerce extends the e-commerce/marketplace/ad engine, not the slowing in-store comp.

**vs expectations / prior period.** Revenue $187.9bn beat public consensus ~$186.6bn by ~$1.3bn (~+0.7%); adjusted EPS $0.81 beat ~$0.74 by $0.07 (~+9%). Beat is broad-based (margin + digital), not a single one-off, and management raised the full-year outlook — a sustainable-beat signal rather than a pull-forward. Momentum check: global e-commerce +23% this quarter is consistent with the high-20s% pace reported in prior FY26/FY27 quarters, i.e. durable double-digit digital growth; U.S. comp, by contrast, decelerated to a multi-year low. Public consensus figures are from free aggregators (see sources) as of the Aug 20, 2026 print.

**Guidance / forward.** RAISED. FY27: net sales +4.0% to +5.0% cc; adjusted operating income +7.0% to +8.5% cc; adjusted EPS $2.80–$2.87. Q3 FY27: net sales +3.0% to +3.75% cc, adjusted operating income +2.0% to +4.0% cc, adjusted EPS $0.62–$0.64. The raise reflects confidence in the digital/advertising mix; Q3 op-income guide (+2–4%) is notably softer than FY27 full-year (+7–8.5%), implying heavier reliance on Q4 holiday — a point management left lightly addressed. Despite the beat-and-raise, the stock fell on the print (slowing U.S. comp + decelerating Q3 op-income guide).

**Thesis-flags (agentic-commerce relevance).**
1. Advertising +38% / Walmart Connect ex-VIZIO +43% → agent-mediated checkout plugs directly into the highest-margin, fastest-growing line → an AI-agent channel that drives incremental transactions is accretive to margin, not just GMV → second-order: more ad inventory and sponsored-placement demand as agents mediate discovery.
2. Marketplace +>50% and e-commerce +23–24% → the Agent Gateway (MCP) is built to scale exactly these digital channels while U.S. store comp cools to a six-year low → why it matters: agentic commerce is a lever to re-accelerate the part of the business that is still compounding, offsetting in-store deceleration.
3. Operating income +28.8% GAAP vs +17.4% adjusted cc → the GAAP figure is flattered by one-offs/FX; read the adjusted/cc line for the true operating trend → flag: don't over-extrapolate the headline op-income jump.
4. Beat-and-raise with a cautious Q3 op-income guide (+2–4%) → management is confident on the full year but conservative near-term → second-order: execution risk concentrated in Q4 holiday, the first season with Agent Gateway in beta.

Sources: Walmart Q2 FY27 earnings release (8-K EX-99.1, EDGAR, filed 2026-08-20) <https://www.sec.gov/Archives/edgar/data/0000104169/000010416926000145/earningsreleasefy27q2.htm> · Walmart corporate newsroom (Q2 FY27) <https://corporate.walmart.com/news/2026/08/20/walmart-releases-q2-fy27-earnings> · public consensus (revenue ~$186.6bn / adj EPS ~$0.74 as of 2026-08-20) via CNBC <https://www.cnbc.com/2026/08/20/walmart-wmt-q2-2027-earnings.html> and MarketBeat <https://www.marketbeat.com/earnings/reports/2026-8-20-walmart-inc-stock/> · comp/ad detail via bit.fan <https://www.bit.fan/en/news/list/walmart-fy2027-q2-earnings-us-comp-sales-msx-rwa-en-ee859f38-en-keyName-aecf583d>
<!-- /enrichment:earnings_review -->
