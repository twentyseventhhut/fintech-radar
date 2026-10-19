---
title: "Symphony by Wix integrates Stripe-built Link Wallet for AI agents"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/wix
  - company/stripe
  - industry/agentic-commerce
  - region/global
  - type/partnership
sources:
  - https://www.wix.com/press-room/home/post/symphony-by-wix-integrates-link-s-wallet-for-agents-built-by-stripe-enabling-ai-agents-to-make-pay
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s2a29a82b
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Symphony by Wix integrates Stripe-built Link Wallet for AI agents

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌐 Symphony by Wix integrates Link's Wallet for Agents, built by Stripe. The integration enables AI agents to make payments on behalf of small businesses. Wix announced the integration on October 15, 2026.

## Первоисточники

### wix.com
<https://www.wix.com/press-room/home/post/symphony-by-wix-integrates-link-s-wallet-for-agents-built-by-stripe-enabling-ai-agents-to-make-pay>
*614 слов · direct*

With Link’s wallet for agents,  Symphony's AI agents go from flagging what needs attention to handling it, keeping inventory stocked, bills paid, and deadlines met on the owner's behalf, with every purchase approved first 
 
 Symphony by Wix , the standalone multi-agent system for small and medium-sized businesses and solopreneurs, now connects to Link, Stripe’s  digital wallet. The integration allows Symphony's team of AI agents to make payments on the business owner's behalf, taking execution one step further. Symphony's agents already know how a business operates and work as a coordinated team across it, executing tasks and surfacing growth opportunities. With Link connected, they can now carry that work through to payments, so a task is finished rather than handed back to the owner. 
 
 Most AI tools for business stop at insight. They find the problem, draft the email, or flag the risk, and then hand the final step back to the owner. With Link connected, Symphony's agents can carry tasks through to payment, with business owners approving each purchase before it is made. For small business owners, that means stock is reordered before it runs out, invoices are paid before they fall overdue, and entry fees are covered before a deadline passes, none of it landing back on the owner's to-do list.  
 
 Every payment runs inside a system the owner controls. With Link's wallet for agents, buyers review and approve each spend request, while Stripe uses a secure payment token or one-time virtual card for the transaction.  In practice, it can play out across the whole life of a business: 
 
 A new owner is setting up their business. Symphony identifies the required registration fees and pays them, so the business is registered before the first sale. 
 A candle shop's best-selling scent drops below five units. Symphony reorders from the usual supplier and pays overnight, so the owner wakes up to "reordered" rather than "almost out." 
 A supplier invoice lands on a Friday afternoon. Symphony confirms the amount matches the purchase order and pays it that day, instead of it sitting until the owner has a free hour. 
 A local farmer’s market closes applications in three days. Symphony pays the entry fee right away, so the opportunity is secured rather than left on a list that expires. 
 A customer leaves a two-star review over a late delivery. Symphony sends a complimentary gift card the same day to make good. 
 
 Symphony's agents never see the owner's underlying payment details, and each card is capped at the approved amount. Approval can be given within a 10-minute window from any device, by WhatsApp or SMS.  
 
 "Since launch, Symphony has been built to act on behalf of business owners, not just advise them," said Ronny Elkayam, COO of Wix. "Connecting Link is the last mile of that promise. An agent that can find an overdue invoice or an expiring grant deadline is useful. An agent that can get it paid, with the owner's approval and inside clear limits, is a teammate. That is the difference between knowing what to do and having it handled." 
 
 “People start businesses to solve problems and serve customers. Routine tasks like ordering supplies and paying bills take valuable time away from that work,” said Jay Shah, business lead for Link at Stripe. “With Link’s wallet for agents, Symphony can handle more of those tasks, giving business owners more time to focus on what matters most to them." 
 
 The Link integration follows Symphony's August launch and extends the platform's expansion into the operational layer of how SMBs manage, automate, and grow. The connection is rolling out to Symphony users with a US-based Link account, with payments made in US dollars. 
 
 Find out more here .

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Symphony by Wix integrates Stripe-built Link Wallet for AI agents
_Analytical notes (not a post). Importance: 2/5._

**Freshness: FRESH** — this is a NEW *application* (Symphony/SMB-operations use case) of Stripe's Link "wallet for agents" rail, announced 2026-10-15. It is NOT a reprint of the rail's own launch (Sessions, 2026-04-29) covered elsewhere. No prior note covers the Wix-Symphony-Link tie-up. But note the weight is modest: the hard payments plumbing is Stripe's, pre-existing since April; Wix is a design-partner/distribution win, not a new mechanism.

## [0] What exactly happened (de-PR'd)
- Wix connected **Symphony by Wix** (its standalone multi-agent system for SMBs/solopreneurs, launched 2026-08-11) to **Link's "wallet for agents," built by Stripe**. Announced 2026-10-15 via Wix press room.
- De-PR'd mechanism: Symphony's agents can now *execute payments* (reorder inventory, pay supplier invoices, pay registration/entry fees, send gift cards) — but **every spend is human-approved first**. Approval window is 10 minutes, via WhatsApp or SMS, from any device.
- Under the hood this is **exactly Stripe's existing Link-for-agents primitive** (launched at Stripe Sessions 2026-04-29): user grants the agent access to Link via OAuth; agent raises a scoped spend request; on approval Stripe issues either a **one-time virtual card** or a **Shared Payment Token (SPT)** scoped to the approved amount. The agent never sees the underlying payment credentials; each card is capped at the approved amount. This sits on Stripe's "Issuing for agents" developer layer (single-use cards, transaction-level controls, real-time auth, audit trails).
- **Live vs announced:** the capability is "rolling out" — gated to Symphony users **with a US-based Link account, USD only**. So availability is real but narrow; no user/GMV/transaction numbers were disclosed.
- **Why framed this way:** the PR leans on the emotive "last mile / teammate not advisor" narrative (Ronny Elkayam, COO Wix) because the *actual* technical delta is small — Wix is wiring an off-the-shelf Stripe rail into its agent orchestration. The substance is **distribution + an approved-spend UX for SMB back-office ops**, not new payment infrastructure. (analysis)

## [1] Competitors / peers
- **The rail itself is Stripe's and is being distributed widely** — Link for agents is already wired into Meta's "Muse" personal agent, xAI's Grok, the "Instinct" SMS assistant, plus Claude/OpenAI/custom agents as supported clients at launch. So Wix joins a *queue* of Link-for-agents adopters; it is not ahead.
- Peers on *agentic SMB/back-office payments*: [[Ramp annualized revenue crosses $2 billion]] (agentic cards / spend-management, agents.ramp.com) is the closest on the "agent that pays for a business" axis and is far larger. On the broader agentic-payments rail wave: [[AWS launches AgentCore Payments with Coinbase and Stripe]], [[Klarna and Stripe bring BNPL to AI agents]], [[Oobit lets AI assistants pay with crypto and stablecoins]], [[Stripe enables payments in ChatGPT with OpenAI]], and the protocol layer [[This Week in Fintech Agentic Commerce Protocol underpins Stripe flow]].
- **Position: catching up / parity.** Wix's distinct angle is *SMB operations* (pay the supplier/registration/entry-fee) vs the consumer-shopping framing of most Link-for-agents demos. But the moat is Wix's SMB base + Symphony orchestration, not the payment mechanism — which any Symphony competitor can replicate by calling the same Stripe API. **Why:** Stripe deliberately made the rail a widely-available primitive → adopters compete on distribution and agent quality, not on the payment capability. (analysis)

## [2] Company history / fit
- Trajectory: Wix launched an embedded **financial services suite (Wix Checking + Wix Capital)** 2025-08-08 ([[Wix launches financial services suite with checking and capital]]) and has a PayPal unified-payments tie-up from 2025-07. Symphony (the multi-agent OS) launched 2026-08-11; this Link integration is its first payments-execution feature, ~2 months post-launch.
- **Fit: logical.** Wix's strategic push is from "website builder" → "operational layer for SMBs." An agent that only *advises* has weak willingness-to-pay; an agent that *acts* (incl. pays) justifies a subscription tier. **Why structured this way:** Wix needs Symphony to graduate from novelty to a billable "teammate," and payment-execution is the most visceral proof of agency — hence partnering with Stripe to borrow the compliance/liability-heavy payments plumbing rather than build issuing itself. (analysis)

## [3] Novelty / value-add / traction
- **Genuinely new?** The *rail* is not new (April 2026). What's new is the **packaging for SMB operational spend with a tight WhatsApp/SMS approval loop** — a credible UX fit for owners who live in messaging apps, not dashboards. Modest but real product novelty.
- **Traction: none disclosed.** No user counts, no volume, no live-client metrics — "rolling out" to US/USD Link accounts only. This is an announcement, not adoption. By contrast the underlying Link rail reportedly saw agentic purchases surge ~38x in a month to late-Sept 2026 (Stripe figure, unverified independently) and ~1M merchants / ~300M Link users.
- **Who captures the margin?** Stripe does — it owns issuing, the token/virtual-card economics, and the merchant-side acceptance. Wix captures subscription/engagement and keeps the customer relationship, but **does not own the payment moment**; it is a distribution channel feeding volume into Stripe's rail. This is the same "who pays vs who dashboards" tension seen with Ramp. **What breaks the value-add:** if Stripe (or Visa/Mastercard, who ultimately clear the one-time cards) commoditize the agent-wallet, Wix's edge collapses to its SMB base and agent quality. (analysis)

## [4] What's next / market sentiment
- Expect Wix to broaden beyond US/USD and add more agent actions; watch for any disclosed transaction/attach metrics as the real signal of whether SMB owners trust agents to pay.
- Sentiment: part of the broad 2026 agentic-commerce land-grab (Stripe, Meta, Walmart, Shopify, Google all building agent-shopping infra). Regulatory/risk backdrop: fraud liability and dispute handling for agent-initiated spend are unsettled — PR is silent on who eats losses if an agent mis-pays within the approved window. [[JPMorgan blocks outside AI agents from accessing accounts]] shows incumbents pushing back on third-party agent access, a structural headwind.
- **Second-order:** the more Wix routes SMB spend through Stripe's wallet, the more it entrenches Stripe (not Wix) as the agentic-payments toll-collector for SMBs — a classic "distribution partner strengthens the platform it depends on" dynamic. (hypothesis)

## Sources
- Wix press room (primary, in-note): symphony-by-wix-integrates-link-s-wallet-for-agents-built-by-stripe
- Finextra: https://www.finextra.com/pressarticle/111293/symphony-by-wix-connects-to-stripes-link-digital-wallet
- Manila Times / GlobeNewswire (2026-10-15): https://www.manilatimes.net/2026/10/15/tmt-newswire/globenewswire/symphony-by-wix-integrates-links-wallet-for-agents-built-by-stripe-enabling-ai-agents-to-make-payments-on-behalf-of-small-businesses/2446659
- StockTitan: https://www.stocktitan.net/news/WIX/symphony-by-wix-integrates-link-s-wallet-for-agents-built-by-stripe-vb033wjqxbng.html
- Symphony launch (2026-08-11): https://www.globenewswire.com/news-release/2026/08/11/3342741/0/en/wix-launches-symphony-by-wix-a-new-standalone-multi-agent-system-built-for-smbs.html
- Stripe Link for agents launch (2026-04-30): https://techcrunch.com/2026/04/30/stripe-link-digital-wallet-ai-agents-shopping/
- Stripe Sessions 2026 announcements: https://stripe.com/blog/everything-we-announced-at-sessions-2026
- Payments Dive (Link embraces AI bots / Meta Muse): https://www.paymentsdive.com/news/stripes-digital-wallet-paypal-embraces-ai-bots-agentic-commerce/830753/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is the payment mechanism actually Wix's, or just a re-skin of Stripe's April rail?** — It's Stripe's. Link for agents (one-time card / SPT, OAuth, approval loop) launched 2026-04-29. Wix added orchestration + a WhatsApp/SMS approval UX. The novelty is packaging, not plumbing.
2. **Any disclosed traction (users, GMV, transactions)?** — Open/None. "Rolling out" to US-based Link accounts, USD only. Zero adoption numbers → announcement, not proof.
3. **Who captures the economics?** — Stripe (issuing, token economics, merchant acceptance) and ultimately the card networks that clear the one-time cards. Wix gets subscription/engagement and the customer relationship, not the payment take-rate.
4. **Who needs whom more?** — Stripe is distributing Link-for-agents to many surfaces (Meta Muse, Grok, Instinct, Claude/OpenAI). Wix is one of a queue; Stripe can lose Wix more easily than Wix can replace Stripe's compliant issuing rail.
5. **Can competitors replicate this trivially?** — Yes. Any agent platform (incl. Symphony rivals) can call the same Stripe Issuing-for-agents API. The defensible asset is Wix's SMB base + agent quality, not the payment capability.
6. **What's the fraud/dispute liability split?** — Open. PR silent on who eats losses if an agent mis-pays within the 10-min approved window, or on chargeback/dispute handling for agent-initiated spend.
7. **Is "approval required for every purchase" friction that kills the value prop?** — Tension: the pitch is "task is handled, not handed back," yet every spend needs human approval. If owners must approve each payment, how much "last-mile autonomy" is really delivered? (open — depends on batching/limits UX)
8. **How narrow is the rollout?** — Very: US-only, USD-only, requires an existing US Link account. Materially limits near-term reach vs the global SMB framing.
9. **Does this meaningfully move Wix's P&L?** — Unlikely near-term. No pricing disclosed; it's a feature to defend/justify Symphony subscriptions, not a direct revenue line. Weight is strategic/narrative.
10. **Is the "38x agentic purchase surge" figure Wix-relevant?** — No. That's Stripe's aggregate Link figure (late-Sept 2026), not Symphony-specific; don't attribute it to Wix.
11. **Structural risk: is Wix strengthening its own dependency?** — Yes. Routing SMB spend through Stripe's wallet entrenches Stripe as the SMB agentic-payments toll-collector; Wix becomes a distribution channel for a rail it doesn't control.
12. **Incumbent pushback risk?** — Real. [[JPMorgan blocks outside AI agents from accessing accounts]] signals banks resisting third-party agent access — a headwind to agent-initiated payments broadly.
13. **First-mover vs late-mover on SMB agentic payments?** — Ramp ([[Ramp annualized revenue crosses $2 billion]]) is ahead on "agent that pays for a business." Wix's edge is its SMB website/commerce base, not timing.
14. **Is the approval channel (WhatsApp/SMS) a security weak point?** — Open. SMS/WhatsApp approval could be a phishing/SIM-swap surface; mitigated by the agent never seeing credentials and per-card caps, but worth flagging.
15. **What would make this a 4–5 story instead of a 2?** — Disclosed adoption at scale, international/multi-currency expansion, exclusive terms with Stripe, or evidence SMBs trust unattended (not per-spend-approved) payments. None present.

**Importance: 2/5** — Fresh as a new SMB-operations application of Stripe's Link-for-agents rail, with a credible WhatsApp/SMS approval UX, but the hard payment infrastructure is Stripe's pre-existing primitive, the rollout is narrow (US/USD/existing-Link-account), there is zero disclosed traction, and the economics/margin accrue to Stripe, not Wix. Strategic signal for Wix's SMB-OS ambition and another data point in the agentic-commerce land-grab — but not a heavyweight, mechanism-changing event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce — AI agents transacting on a user's behalf — went from protocol announcements to live rails across 2026. Stripe + OpenAI shipped the open-source Agentic Commerce Protocol (ACP, Apache-2.0) and "Instant Checkout in ChatGPT" on 2026-02-16, with the Shared Payment Token (SPT) primitive; Stripe then announced the Link wallet for agents at Sessions on 2026-04-29 (per Stripe newsroom, as of 2026-04). The networks moved in parallel: Mastercard Agent Pay (agentic tokens over MDES) and Visa Intelligent Commerce launched end-Apr 2025, Visa's Trusted Agent Protocol on 2025-10-14, and both joined Google's AP2 in Sep 2025 (per eco.com/Forbes, as of 2026-06). Size/TAM of agentic-commerce payment flow — no data (no verifiable TAM; PR TAMs excluded). Structure: the value chain is layering — identity/trust (Visa TAP, agent IDs) → authorization token (SPT, agentic tokens, one-time VCNs) → wallet/credential holder (Link, PayPal) → platform orchestration (Symphony, ChatGPT). Barriers are high at the token/network layer (scheme rules, fraud liability, regulation) and low at the orchestration layer, where Wix sits. Why now: the surface for autonomous spend only becomes bankable once scheme-grade controls (scoped tokens, per-tx caps, buyer approval) exist — 2026 is the first year they do, which is exactly what this integration consumes.

**Competitive landscape.** Sector KPIs: for the payment layer — authorized agent-transaction volume, approval/fraud rate, take rate per agentic tx; for Wix as the platform — GPV, transaction take rate, and attach of Symphony. Wix's own payments business is sub-scale: Q2 2026 GPV grew only +3% y/y (dragged by InkFrog wind-down), transaction revenue $71.5m with take rate ~1.96% (per Wix Q2 2026 results, 2026-08-04). Basis of competition at the orchestration layer is distribution (installed SMB base) and workflow depth, not payment economics. Key players: PayPal (Agentic Commerce Services + Mastercard Agent Pay in-wallet, 2025-10 — see internal comps), the ChatGPT/Walmart Instant-Checkout axis, and vertical SMB suites. Recent moves: Symphony launched Aug 2026; Link-for-agents integration announced 2026-10-15 (US-only, USD-only, US Link accounts). Protagonist position: Wix is a **consumer/orchestration-layer adopter, not an infrastructure owner** — it rides Stripe's rails and Link's wallet rather than building a competing stack. Moat is Wix's SMB distribution + Symphony's operational context (switching costs once agents run reorders/AP), `(analysis)`; it owns no payment-network moat here.

**Comps & multiples.** Wix (NASDAQ: WIX) market cap ~$3.1–3.4bn (per stockanalysis/tipranks, as of 2026-10-15/17); revenue TTM $2.13bn → **P/S ≈ $3.3bn / $2.13bn ≈ 1.5x**; EBITDA TTM −$34.45m and P/E −21x, so EV/EBITDA and P/E = not meaningful (EBITDA-negative). That 1.5x sales is at the low end of the software range and well below agentic-commerce high-flyers — a value, not a growth, multiple; stock −63% y/y. Counterparty Stripe is private: $1.9T total payment volume in 2025 (+34% y/y), tender valuation $159bn (2026-02-24 annual letter) — a round/tender mark, not a market cap; no clean public revenue so no EV/Rev computed. Internal comps (same agentic-commerce wave): [[Stripe enables payments in ChatGPT with OpenAI]], [[Visa launches Trusted Agent Protocol for AI commerce]], [[PayPal integrates Mastercard Agent Pay into wallet]], and Wix's prior fintech push [[Wix launches financial services suite with checking and capital]]. Distribution not computed (mixed private/public, different models) — qualitative: Wix trades cheap on fundamentals; the agentic-commerce narrative is not (yet) priced into its multiple.

**Risk flags.**
1. **Dependence on someone else's rails + disintermediation.** Wix consumes Stripe/Link tokens and VCNs; Stripe owns the wallet, the SPT, the fraud layer and the economics. If agentic spend consolidates at the wallet/network layer (Link, Visa/MC tokens), Wix captures orchestration value but little payment margin — the take-rate accrues upstream. Second-order: Wix's payments KPIs (GPV +3%, 1.96% take) suggest it has limited leverage to monetize the flow it originates.
2. **Fraud/liability and authorization scope are under-disclosed.** The PR touts buyer approval, per-card caps, and 10-minute approval windows but is silent on who eats losses on a mis-authorized agent purchase and on ticket-size limits. Autonomous AP/reorder on an SMB's behalf concentrates a new fraud surface; liability allocation between Wix, Stripe and the SMB is the economics that's not being said.
3. **Adoption vs announcement + narrow rollout.** US-only, USD-only, US-Link-account gated, on a Symphony base launched only ~2 months prior (Aug 2026). "Announced" ≠ "adopted at scale"; execution risk is high and the addressable cohort on day one is small.

**What this changes (idea-lens).** For the sector, this is agentic commerce crossing from checkout (ChatGPT buy-it) into **outbound SMB operations** (AP, reordering, registration fees) — a new entry point rather than a re-rating. Falsifiable thesis `(analysis)`: if agentic spend meaningfully lifts Wix GPV/transaction take-rate, it should show in H1-2027 transaction-revenue growth re-accelerating above the current +12%; trigger to watch — a disclosed Symphony-attributed GPV metric or an expansion beyond US/USD. What breaks the thesis: GPV stays ~flat and the value visibly pools at Stripe/Link, confirming Wix as a thin orchestration skin on someone else's wallet.

Sources: https://www.wix.com/press-room/home/post/wix-reports-second-quarter-2026-results · https://stripe.com/newsroom/news/stripe-openai-instant-checkout · https://stripe.com/newsroom/news/stripe-2025-update · https://finance.yahoo.com/news/stripe-reaches-159-billion-valuation-195143711.html · https://stockanalysis.com/stocks/wix/market-cap/ · https://www.forbes.com/sites/digital-assets/2026/06/07/visa-mastercard-and-coinbase-are-fighting-over-how-ai-agents-pay/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_Not a results release — this is a product-integration story. Below is an IR-grounded financial backdrop for the two parties, as context; no integration-specific economics are disclosed, so none are invented._

**Backdrop (Wix, latest print = Q2 2026, reported 2026-08-04).** Growth steady, cash conversion the thing to watch. Total revenue $563.1M (+15% YoY), ahead of ~$552.6M public consensus; total bookings $569.1M (+12% YoY) — bookings growth trailed revenue, i.e. the leading indicator decelerated below the reported top line. Creative Subscriptions $398.4M (+15% YoY); Business Solutions — the commerce/payments-exposed segment most relevant to a Stripe/Link integration — $164.7M (+14% YoY). Total ARR $1.963bn (+15% YoY). Profitability: non-GAAP operating income $64.8M (12% margin) and non-GAAP net income $68.2M ($1.39/diluted share), but a GAAP operating loss of $(58.8)M and GAAP net loss of $(76.4)M, or $(1.78)/share (SBC/restructuring gap). Free cash flow $52.6M, or $61.2M (11% of revenue) ex-restructuring — well below the full-year high-teens FCF-margin target, a timing/seasonality step-down to flag. FY2026 guidance (reaffirmed): revenue low-to-mid-teens growth, bookings low-teens, FCF margin (ex-acquisition/restructuring) high-teens. Prior quarter for context: Q1 2026 revenue $541M (+14% YoY), bookings $585M (+15% YoY), GPV $3.8bn (+12% YoY, called "soft" on SMB macro pressure), FCF $112M (21% of revenue). GPV was not re-disclosed in the Q2 release.

**Backdrop (Stripe, private — no quarterly filings).** Publicly reported calendar-2025 total payment volume $1.9tn (+34% YoY, ~1.6% of global GDP); last valuation $159bn via a Feb-2026 employee tender (up from $106.7bn prior). Link, the consumer/agent wallet in this integration, is Stripe's own product; Stripe does not break out Link TPV or the "wallet for agents" economics publicly.

**Read.** BACKDROP ONLY — no earnings event. The integration is a go-to-market/agentic-commerce feature, not a reported financial driver; it is US-only, USD-only, and follows Symphony's Aug-2026 launch, so any payments-volume contribution is immaterial to the Q2 numbers above and unquantified by either party. For Wix the relevant monitorables remain Business Solutions growth and GPV re-acceleration (the lines agentic payments would eventually feed) against a soft-SMB macro; for Stripe it is another distribution surface for Link. Thesis-flag: watch whether agent-initiated spend shows up in future Wix GPV/Business Solutions disclosure — until it does, treat the integration as announced, not monetized.

Sources: Wix Q2 2026 results (2026-08-04) <https://www.sec.gov/Archives/edgar/data/0001576789/000162828026052108/secondquarter2026results.htm> · <https://www.stocktitan.net/news/WIX/wix-reports-second-quarter-2026-7v2g2dpy5dtf.html> · Wix Q1 2026 results (2026-05-13) <https://www.sec.gov/Archives/edgar/data/0001576789/000162828026034370/firstquarter2026results.htm> · Stripe TPV/valuation <https://www.cnbc.com/2026/02/24/stripe-value-stock-sale-tender-offer.html> · GPV not re-disclosed in Q2 release = no data.
<!-- /enrichment:earnings_review -->
