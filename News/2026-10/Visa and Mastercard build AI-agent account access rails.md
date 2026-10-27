---
title: "Visa and Mastercard build AI-agent account access rails"
date: 2026-10-26
retrieved: 2026-10-26
tags:
  - company/visa
  - company/mastercard
  - industry/agentic-commerce
  - industry/payments
  - region/global
  - type/commentary
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sc05e9609
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Visa and Mastercard build AI-agent account access rails

> [!info] 2026-10-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Пока банки ограничивают сторонним ИИ-агентам доступ к клиентским счетам, Visa и Mastercard создают инфраструктуру, которая позволяет им легально и контролируемо распоряжаться деньгами. Подходы различаются: Visa автоматизирует исполнение уже утверждённых корпоративных платежей, Mastercard даёт агентам возможность самостоятельно покупать цифровые услуги в рамках согласованного бюджета. Главное различие — степень самостоятельности агента. У Visa он исполняет заранее одобренную конкретную операцию. У Mastercard может самостоятельно выбирать и оплачивать услуги в рамках утверждённой задачи. Но глобально платёжные системы решают одну задачу — связать конкретную операцию с проверяемым поручением человека или компании и сделать ИИ-агентов самостоятельными участниками платёжного процесса. Visa + BILL + Billtrust ⚪️ Компания-покупатель утверждает счёт через BILL, платёжный агент получает поручение и платёжные реквизиты в виде защищённого токена. ⚪️ При обращении к платёжному кабинету поставщ

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
**[0] What's new.** Two card networks are, almost simultaneously, shipping infrastructure that lets AI agents move money *out of client accounts* in a legally bounded, auditable way — exactly the access banks have been reluctant to grant third-party agents. The two approaches differ by how much autonomy the agent gets:
- **Visa** automates execution of a *pre-approved, specific* corporate payment. On 2026-10-22 Visa, BILL and Billtrust announced the "first live pilot for trusted AI agent payments between buyer and supplier platforms": a BILL Payment Agent — registered via **Visa Trusted Agent Protocol (TAP)** and listed in Visa's **Agentic Directory** — uses tokenized credentials and buyer-approved controls to pay invoices, and Billtrust (the supplier portal) uses TAP to authenticate and admit that agent. The point is removing the manual human-login step that blocked automation at supplier portals. (https://investor.visa.com/news/news-details/2026/Visa-BILL-and-Billtrust-Launch-First-Live-Pilot-for-Trusted-AI-Agent-Payments-Between-Buyer-and-Supplier-Platforms/default.aspx , https://www.pymnts.com/partnerships/2026/visa-launches-agentic-payments-pilot-with-bill-and-billtrust/)
- **Mastercard** lets an agent *itself choose and pay* for digital services within an approved budget. On 2026-10-20 at Cloudflare Connect, Mastercard opened **early access to Agent Pay for Machines**, built on the open **x402** pay-per-request protocol: a business gives the agent a task + spending limit, the agent mints a digitally-signed payment voucher within that limit, and the provider verifies the voucher before delivering. A demo showed one agent making nine payments to two providers under a single budget. Pilot partners: Cloudflare, Ant International, BVNK, Coinbase/Base. (https://www.pymnts.com/news/artificial-intelligence/2026/mastercard-debuts-tool-to-help-ai-agents-purchase-digital-services/ , https://www.mastercard.com/global/en/news-and-trends/press/2026/october/Mastercard-Agent-Pay-for-Machines-in-action.html)

**[1] The common problem both solve.** Bind a *specific money movement* to a *verifiable mandate* from a human or company, and make the agent a first-class, identifiable participant in the payment flow — not a scraper logging in with stolen-looking credentials. Visa does identity+consent via TAP/Agentic Directory + tokens; Mastercard does it via signed vouchers scoped to a budget on top of x402. The axis of difference is agent *autonomy*: Visa = execute one approved transaction; Mastercard = discretionary spend inside an approved task/budget.

**[2] Prior corpus — this extends a long arc, not a cold start.**
- Visa's consumer/business agentic stack: [[Visa launches Intelligent Commerce Connect for agentic commerce]] (2026-04), [[Crossmint launches Agentic Cards API on Visa Intelligent Commerce]] (2026-06). TAP itself was announced Sept 2025.
- Mastercard's side: [[Mastercard unveils tools for safer agentic commerce]] (2025-09, Agent Pay + Agentic/Insight Tokens), [[Mastercard launches Agent Pay for Machines for machine-speed payments]] (2026-06 — the *machine-to-machine* product this Oct early-access builds on), [[Mastercard: agentic commerce raises new consent and trust questions]] (2026-01).
- Both networks together: [[Mastercard and Visa enlist banks for agentic payment pilots]] (2026-02), [[Fintech Wrap Up: Visa and Mastercard agentic AI tools reference]] (2026-03).
- x402 lineage: [[Stripe introduces machine payments via x402 protocol]] (2026-02).

**[3] Competitive map.** This is a 4-layer race, mostly not mutually exclusive: card networks (Visa TAP + Intelligent Commerce; Mastercard Agent Pay / Agentic Tokens on MDES), open protocols (Google **AP2**), processor/dev-tooling (**Stripe + OpenAI Agentic Commerce Protocol / Shared Payment Tokens**, co-developed w/ OpenAI), and PayPal's own agentic push. Notably Mastercard chose the *open x402* rail for the machine product rather than a proprietary stack — the same rail Stripe and Coinbase back — signalling convergence on x402 for machine-to-machine micropayments. (https://www.crossmint.com/learn/agent-card-payments-compared , https://www.refontelearning.com/blog/agentic-commerce-ai-agent-payment-protocols)

**[4] Why it matters.** This is the networks answering the structural objection that banks won't open accounts to third-party agents: instead of fighting bank gatekeeping, Visa/Mastercard insert themselves as the *trust-and-identity layer* that makes agent-initiated movements admissible — TAP authenticates the agent to the counterparty portal (Visa), signed budget-scoped vouchers bound to a mandate (Mastercard). Visa's B2B angle (AP/AR automation via BILL/Billtrust) targets a huge, friction-heavy invoice-payment market; Mastercard's machine angle targets autonomous software buying APIs/services. Both are still **pilot / early-access**, not GA — live but narrow.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Q1. Are these live or just announced?** Both are explicitly pilot / early-access. Visa+BILL+Billtrust is a "first live pilot" (so live, but limited scope). Mastercard Agent Pay for Machines opened *early access* on 2026-10-20 with a demo and named pilot partners — not GA. Open: production volume, GA date, GA pricing.

**Q2. Is the note's core claim (networks route around bank gatekeeping) accurate?** Directionally yes — TAP authenticates agents to counterparty portals and tokens/vouchers bind movements to a mandate, which is the networks positioning as the trust layer. But the framing "banks restrict agents, so networks build access" is the Russian-digest editorial angle; the primary sources frame it as removing manual-login friction and adding agent identity, not as an adversarial move against banks. Partially supported.

**Q3. Does Visa's agent actually "access the account"?** Not directly — the BILL Payment Agent uses tokenized payment credentials and buyer-approved controls; TAP handles authenticating that agent to the *supplier* (Billtrust) portal. It's authenticated payment execution, not raw bank-account access. The headline "account access rails" is a simplification. Open question.

**Q4. Is Mastercard's Oct 2026 item genuinely new vs the June 2026 Agent Pay for Machines launch?** The June note covered the product launch; this Oct item is the *early-access opening* at Cloudflare Connect with x402 emphasis, named partners (Cloudflare, Ant, BVNK, Coinbase), and the 9-payment demo. Incremental but datedly new — not a duplicate.

**Q5. What exactly is x402's role?** Open HTTP-402-based pay-per-request protocol (Stripe/Coinbase lineage); Mastercard layers network trust/reach on top. So Mastercard is NOT using a proprietary rail for the machine product — an important nuance the note omits.

**Q6. Where does Visa's Trusted Agent Protocol sit?** TAP (announced Sept 2025) provides Verified Agent ID + issuer-signed consent; the Agentic Directory is the registry of authorized agents. The pilot is the first *cross-platform* (buyer-platform ↔ supplier-platform) live use of TAP. Confirmed via Visa IR.

**Q7. Competitive risk — are networks even the winning layer?** Contested. Open protocols (Google AP2) and processor stacks (Stripe/OpenAI ACP + Shared Payment Tokens, with Stripe as merchant-of-record preserver) compete; most real flows touch 2+ layers. Networks' edge is reach + fraud liability + tokenization infra; their risk is commoditization if open protocols (x402, AP2) win the rail. Mastercard adopting x402 is a hedge.

**Q8. Fraud / liability — who eats a bad agent payment?** Unaddressed in sources. Mandate binding + signed vouchers aim to make transactions auditable and attributable, but chargeback/liability allocation for agent errors (wrong vendor, overspend within budget) is unspecified. Open.

**Q9. Consumer vs B2B scope?** Visa BILL/Billtrust = B2B AP/AR invoice payments. Mastercard Agent Pay for Machines = business agents buying digital services/APIs (machine-to-machine). The note conflates them under one "account access" umbrella; they target different buyers. Clarified.

**Q10. Is "autonomy axis" framing (Visa=execute approved, Mastercard=discretionary within budget) correct?** Yes, matches sources: Visa executes a specific approved invoice; Mastercard's agent chooses providers/makes multiple payments within an approved budget (9 payments, 2 providers in demo). Confirmed.

**Q11. Any numbers?** Thin. Only demo figures (9 payments / 2 providers / 1 budget). No TPV, no pilot-partner counts beyond names, no revenue. Open — early stage.

**Q12. Regulatory exposure?** Agent-initiated payments touch consent, SCA/strong-authentication rules, and data-access regimes (open banking). Not covered in these announcements; a live risk for scale-up. Open.

**Q13. Does Mastercard's voucher model need a card at all?** Signed voucher within a budget + x402 — the role of the underlying Mastercard credential vs pure crypto/stablecoin rail (Coinbase/Base, BVNK involvement) is ambiguous. Open — possible stablecoin settlement.

**Q14. Is the Russian source credible / standalone?** It's a single Финтехно commentary post (1 mention, no full source text loaded) that correctly aggregates two real, externally-verified announcements. Content is accurate; depth is editorial, not primary.

**Q15. Durability — is this a one-off or a trend?** Clear trend: this is the Nth step in a ~18-month arc (see context [2]). Both networks, plus Google/Stripe/OpenAI/PayPal, are converging on agent-identity + mandate-bound tokenized payments. High strategic salience.

**Importance: 4/5** — Two tier-1 networks shipping co-equal, dated (Oct 2026) agentic-payment infrastructure addressing the central blocker for agentic commerce (binding agent actions to verifiable mandates), with a notable x402-convergence signal. Capped below 5 because both remain pilot/early-access with no volume data, and the Mastercard piece partly extends prior coverage.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-27]] (2026-10-27).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: agentic commerce / AI-agent payment rails, sitting on top of the card-network value chain. Size estimates are wide and definition-dependent, so treat as directional: Juniper Research pegs 2026 agentic-commerce transaction value at ~$8bn globally, scaling to ~$3.5tn by 2031; IDC projects ~$38.2bn for 2026 and ~$187bn by 2030 (~59% CAGR); eMarketer's narrowest "sales on AI platforms" cut is ~$20bn in 2026 → ~$144bn by 2029 (per Juniper/IDC/eMarketer, via ai-best-practices.com / commercetools summaries, as of Oct 2026). The 35x spread between estimates is itself the signal: nobody yet knows what counts as "agentic" spend. Structure: the card-network layer is a consolidated duopoly (Visa + Mastercard) with deep network effects and regulatory moats; the agentic layer on top is still fragmented and land-grabby (Stripe, PayPal, OpenAI/ACP, Crossmint, Skyfire, protocol consortia). Why now: LLM agents can now transact, but banks are gating third-party agent access to accounts — so the networks are inserting a trust/tokenization layer (verifiable mandate → scoped token) to become the default rail before a protocol standard hardens. Why-ladder: agents need provable authorization → networks already own the authorization/tokenization primitive → whoever owns the mandate-to-token binding captures the new transaction flow → second-order: this defends the networks against being disintermediated by direct bank-to-agent or stablecoin rails.

**Competitive landscape.** Sector KPIs for networks: payments/gross-dollar volume (PV/GDV), cross-border volume, processed/switched transactions, net revenue growth; for the agentic layer specifically, # of agent transactions, tokens issued, merchant/partner coverage — none disclosed yet for agentic (too early). Key players & basis of competition (product + distribution + network, not price): Visa Intelligent Commerce / Trusted Agent Protocol (executes pre-approved, scoped payments; integrated into OpenAI since ~Jun 2026) vs Mastercard Agent Pay / Agentic Tokens (lets an agent choose and pay within an approved budget; unveiled Apr 2025). Recent dated moves: Mastercard + Santander completed Europe's first live end-to-end AI-agent payment in a regulated framework (Mar 2026); Mastercard "Agent Pay for Machines" for M2M payments (Jun 2026, early access in Oct 2026 per [[Mastercard opens Agent Pay for Machines early access]]); Mastercard added trust/intelligence services (Sep 2026); the Visa+BILL+Billtrust corporate pilot that anchors this very story ([[Visa, BILL and Billtrust pilot trusted AI agent payments]]). Protagonists' position: both ahead on distribution and trust primitives, but the design split is the story — Visa = constrained executor (lower autonomy, lower fraud surface), Mastercard = autonomous spender within budget (higher autonomy, higher liability question). Moat (analysis): network effects + tokenization/authorization infrastructure already embedded in issuers and merchants — a switching-cost and scale moat the pure-agentic startups can't replicate.

**Comps & multiples.** Public card-network / payments comps (market caps per companiesmarketcap/macrotrends summaries, as of ~Oct 20–26 2026):
- Visa (V): market cap ~$765.8bn. FY2025 Q4 net revenue $10.72bn (+12%); fiscal Q3 FY2026 net revenue $11.6bn (+14%) per Visa 8-K (irdb drive: https://drive.google.com/file/d/1KAwJMvzVrjq8djc0mVZL_7DoN40UcQdN/view for Q4'25; Q3'26 8-K https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm). Street modeled Q4 FY2026 (reported 27 Oct 2026) at ~$12.09bn revenue / $3.44 EPS; actual EPS $3.43 (per MarketBeat/AlphaStreet). Annualizing recent quarterly revenue (~$11.6bn x4 ≈ $46bn): P/S ≈ $765.8bn / $46bn = ~16.6x (analysis; EV≈mkt cap given net-cash-ish balance sheet).
- Mastercard (MA): market cap ~$539.97bn. Q3 2025 net revenue +17% (15% cc); Q1 2026 GDV +7%, cross-border +13%, switched tx +9% per MA earnings release (irdb drive: https://drive.google.com/file/d/1neT4u3dNKpZc5-MnUustCIvl24cqjH1Z/view). Q3 2026 reported 29 Oct 2026, consensus ~$9.66bn revenue / $5.16 EPS (per MarketBeat). Forward P/E cited ~24.9x; trailing P/E ~33x (per Motley Fool / hudson-labs, Oct 2026).
- PayPal (PYPL) — adjacent agentic player, NOT a clean network comp (wallet/processor model): market cap ~$48.9bn, forward P/E ~8x / trailing ~10.8x (per Motley Fool, Jun 2026; macrotrends Oct 2026).
Internal comps (base): [[Visa, BILL and Billtrust pilot trusted AI agent payments]] (same event, corporate-AP angle), [[Mastercard opens Agent Pay for Machines early access]], [[Visa launches Trusted Agent Protocol for AI commerce]] (2025-10), [[Mastercard and PayPal partner on agentic commerce]] (2025-10). Read: both networks are in-line-to-rich on revenue multiples (V ~16-17x P/S, MA mid-20s fwd P/E) — justified by ~double-digit durable revenue growth and ~50%+ operating margins; agentic commerce is optionality not yet in the numbers, so no re-rating is attributable to it. PayPal's ~8x P/E vs the networks' premium quantifies the market's view that wallets/processors sit lower in the value chain than the networks' authorization layer. Distribution of agentic-specific multiples: not computed — no disclosed agentic revenue.

**Risk flags.**
1. Fraud/liability allocation is unresolved — especially Mastercard's higher-autonomy model, where an agent spends within a budget: who eats a bad agent-initiated transaction (issuer, network, merchant, consumer)? Unanswered in the PR → second-order: chargeback/dispute economics could compress the new flow's margin or stall bank adoption.
2. Disintermediation / standards risk — if ACP (OpenAI/Stripe) or a bank-direct / stablecoin rail becomes the agent standard, networks could be relegated to a commodity settlement leg; the whole move is defensive against exactly this.
3. Bank gatekeeping — the premise is that banks are *restricting* third-party agent access; if issuers prefer their own agent rails (cf. [[Финтехно Russian banks to open accounts to third-party AI agents]]), network token adoption could be slower than announced. De-PR: these are "announced/piloted," not "live at scale" — Visa+BILL is a pilot, not GA.

**What this changes (idea-lens).** (analysis) This is a land-grab for the authorization primitive of agentic commerce, not a revenue event — the thesis is that owning the verifiable-mandate-to-token binding lets the networks tax agent flows the way they tax card flows today, defending the duopoly rather than expanding the TAM. Falsifiable test / trigger to watch: look for the first *disclosed* agentic transaction volumes or take-rate in Visa/Mastercard earnings (next prints 27 & 29 Oct 2026) and whether a rival protocol (ACP) wins marquee merchants without a network token in the loop — the latter would break the thesis.

Sources: https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm · https://drive.google.com/file/d/1KAwJMvzVrjq8djc0mVZL_7DoN40UcQdN/view · https://drive.google.com/file/d/1neT4u3dNKpZc5-MnUustCIvl24cqjH1Z/view · https://www.electronicpaymentsinternational.com/analyst-comment/visa-mastercard-bet-agentic-payments/ · https://ai-best-practices.com/news/agentic-commerce-market-forecast-to-reach-300-500-billion-by · https://www.marketbeat.com/earnings/reports/2026-10-27-visa-inc-stock/ · https://www.marketbeat.com/earnings/reports/2026-10-29-mastercard-incorporated-stock/ · https://www.fool.com/coverage/better-buy/2026/06/23/mastercard-vs-paypal-which-financial-stock-is-a-better-buy-in-2026/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_Earnings-grounding context for a strategic (non-earnings) story. The news reports an agentic-payments product move, not a print — so this layer frames BOTH networks' most recently reported quarter (both fiscal periods ended June 30, 2026, released late July 2026) as the balance-sheet backdrop against which the AI-agent rails bet is being made. ir_latest.json lagged (latest filing there = Q1 CY2026, period ended 2026-03-31); figures below are cross-checked against the fresher EDGAR 8-K releases. Note: Visa fiscal Q4 FY2026 (ended Sept 30, 2026) reports 2026-10-27 and Mastercard Q3 2026 reports 2026-10-29 — both still in the future as of this review's 2026-10-26 date, so the June-quarter prints are the latest actuals._

**Verdict (headline read).** Both BEAT and both RAISED full-year guidance on their latest reported quarter — the strongest footing in years for the capex this agentic push implies. **Visa** (fiscal Q3 FY2026, qtr ended Jun 30, 2026): net revenue $11.6bn (+14% YoY; +13% constant-dollar), non-GAAP EPS $3.32 (+11% YoY); payments volume topped $4tn, guidance raised. **Mastercard** (Q2 2026, qtr ended Jun 30, 2026): net revenue $9.3bn (+14% YoY; +12% currency-neutral), adjusted EPS $5.04 (+21% YoY; +19% c/n); full-year outlook narrowed-and-raised to low-teens net-revenue growth.

**Key figures (with growth).**
- **Visa — fiscal Q3 FY2026 (ended Jun 30, 2026; released Jul 28, 2026):** Net revenue $11.6bn, +14% YoY (+13% constant-dollar). GAAP net income $5.6bn, GAAP EPS $2.97 (+10% YoY). Non-GAAP net income $6.3bn (+8% YoY), non-GAAP EPS $3.32 (+11% YoY). Key drivers (constant dollars): payments volume +10%, cross-border volume total +13% (ex-intra-Europe +12%), processed transactions +10%. Payments volume crossed $4tn in the quarter (analysis, per earnings-call slides).
- **Mastercard — Q2 2026 (ended Jun 30, 2026; released Jul 30, 2026):** Net revenue $9.3bn, +14% YoY (+12% currency-neutral). GAAP net income $4.4bn, GAAP diluted EPS $4.97; GAAP operating margin 60.2%. Adjusted net income $4.5bn (+18% YoY; +16% c/n), adjusted diluted EPS $5.04 (+21% YoY; +19% c/n); adjusted operating margin 61.1%. Drivers (local currency): gross dollar volume +8%, cross-border volume +12%, switched transactions +9%.

**By segment / driver.** For both, **cross-border is the margin engine** — Visa cross-border +13% and Mastercard +12% ran well ahead of their domestic volume lines (payments/GDV +10%/+8%), and cross-border carries the richest yield. Mastercard's EPS (+21%) outran revenue (+14%) on operating leverage and value-added services (fraud, data, consulting) — VAS was explicitly cited as the revenue beat's driver (per Q2 slides). Visa's non-GAAP EPS (+11%) grew roughly in line with revenue, with GAAP EPS (+10%) held back partly by a restructuring/headcount action flagged on the call. The relevance to this story: the agentic-rails products (Visa Intelligent Commerce / BILL + Billtrust tokenized B2B flows; Mastercard Agent Pay) sit on top of exactly these cross-border and value-added rails that are already the fastest-growing, highest-yield parts of the P&L.

**vs expectations / prior period.** Both beat public consensus. Visa fiscal Q3: EPS $3.32 vs public consensus near $2.85 (as of Jul 2026) — a beat on revenue and EPS. Mastercard Q2: adjusted EPS $5.04 vs public consensus near $4.90 and revenue $9.3bn ahead of a ~$9.0bn estimate (as of Jul 2026) — a beat "on every line" per analyst recaps [UNSOURCED on exact consensus cents; figures from free aggregators/press]. Momentum vs prior quarters: Visa decelerated modestly off its fiscal Q2 FY2026 print (net revenue had grown ~17%, its strongest since 2022) to +14% here; Mastercard held a steady +14% headline. Both remain in a mid-teens revenue / high-teens-to-low-double-digit EPS cadence — healthy and self-funding.

**Guidance / forward.** The 8-K earnings releases carry no forward guidance (standard disclaimer only); guidance is given on the calls. **Visa** raised full-year FY2026 outlook after this quarter: net-revenue growth to the low end of low-teens, EPS growth to the low end of mid-teens (per Q3 call). **Mastercard** narrowed-and-raised full-year 2026 net-revenue growth to the low-teens (currency-neutral, ex-inorganic), up from prior "high end of low double digits to low teens," with ~1.5pt FX headwind to revenue (per Q2 call). Both management tones were confident; both devoted call time to agentic commerce as a forward growth vector rather than a cost — Visa framing Intelligent Commerce / agent tokenization and Mastercard framing Agent Pay as extensions of their tokenization and credential rails.

**Thesis-flags.**
1. **The agentic bet is being made from strength, not desperation.** Double-digit revenue growth + rising margins + raised guidance at both networks means the AI-agent rails are incremental optionality funded by core cash flow — not a pivot to rescue slowing volumes. Second-order: neither network needs this to work near-term, so they can set standards (tokenized mandates, verifiable human authorization) patiently and defensively, which is exactly the control-layer posture the news describes.
2. **Cross-border strength de-risks the agentic-commerce TAM.** The fastest-growing, highest-yield line at both (cross-border +13%/+12%) is where agent-initiated purchases of digital services and cross-border B2B settlement would land. If agents drive more remote/digital and cross-border transactions, they feed the mix that is already lifting yields — the strategic move leans into, not against, the current revenue tailwind.
3. **Tokenization is the shared moat both are extending.** The de-PR'd reality of the news — "connect a specific transaction to a verifiable human/company mandate" — is tokenization applied to agents. Both already monetize tokenization and value-added security (Mastercard's VAS drove the Q2 beat); extending it to agents defends the authorization layer against banks' instinct to wall off third-party AI access. Second-order: whoever owns the trusted-mandate standard captures the agentic interchange, so this is a land-grab for the next credential primitive.
4. **Watch (de-PR / who's silent): "announced vs live."** The prints are strong, but neither network has disclosed agentic-commerce transaction volume or revenue — it is product announcement, not a reported line. Visa's GAAP EPS lagged non-GAAP on a restructuring charge (cost discipline amid the AI build-out); monitor whether agentic rails become a quantified driver in the fiscal Q4/Q3 prints due 2026-10-27 (Visa) and 2026-10-29 (Mastercard), or stay a narrative.

Sources: Visa fiscal Q3 FY2026 8-K earnings release (EDGAR) https://www.sec.gov/Archives/edgar/data/1403161/000140316126000103/q32026earningsrelease.htm · Mastercard Q2 2026 8-K earnings release (EDGAR) https://www.sec.gov/Archives/edgar/data/1141391/000114139126000081/ma06302026-exx991xearnings.htm · Visa Q3 FY2026 call/guidance (Investing.com transcript & slides) https://www.investing.com/news/transcripts/earnings-call-transcript-visa-tops-q3-2026-estimates-raises-outlook-93CH-4818303 · Mastercard 2026 guidance (Seeking Alpha) https://seekingalpha.com/news/4544503-mastercard-signals-high-end-of-low-double-digit-net-revenue-growth-for-2026-while-advancing · irdb semsearch (Visa/Mastercard 8-K trend, FY2024–FY2026) drive_url e.g. https://drive.google.com/file/d/1VyCFznE7XzphUipbyoNItvBP9GJHcYDQ/view (Visa Q1 FY2026), https://drive.google.com/file/d/1WlQ-3I8AwYCbd6IChgCAz5AeNEnQPJQb/view (Mastercard Q4 2025) · consensus figures from free aggregators (MarketBeat/Yahoo, as of Jul 2026) [exact cents UNSOURCED] · Next prints (both unreported as of 2026-10-26): Visa Q4 FY2026 on 2026-10-27, Mastercard Q3 2026 on 2026-10-29.
<!-- /enrichment:earnings_review -->
