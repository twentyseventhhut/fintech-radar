---
title: "Unit launches Real-Time Payments on its platform"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/unit
  - industry/payments
  - region/us
  - type/product
sources:
  - https://www.unit.co/blog/real-time-payments
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s74fc35d0
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Unit launches Real-Time Payments on its platform

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Unit launches Real-Time Payments on its platform. Clients can send and receive RTP in seconds, 24/7/365, including weekends and holidays. Unit connects directly to The Clearing House with no intermediary processor.

## Первоисточники

### unit.co
<https://www.unit.co/blog/real-time-payments>
*677 слов · direct*

Real-Time Payments are now live on Unit
Money in the U.S. still moves on a banking calendar. ACH settles on business days and wires stop at the end of them. In 2026, that leaves 114 days when neither settles at all: 104 weekend days and 10 Federal Reserve holidays. That's nearly one day in three.
Your customers don't keep that calendar. A business remembers a supplier invoice at 7pm on a Friday, and on ACH that payment won't land until the next business day. A customer pays them on Saturday, and the funds won't be usable until the next business day either. Seven times this year, a holiday stretches that wait across a three-day weekend.
Starting today, you can send and receive Real-Time Payments (RTP) on Unit in seconds, 24/7/365, including weekends and holidays. The supplier is paid Friday night. The Saturday payment arrives in seconds and can be used right away. 
We connect directly to The Clearing House, with no intermediary processor. RTP runs on the same Payments API, native ledger, and dashboard as ACH, wire, check, and international payments. If you're already on Unit, you can access this new rail from the same Platform you use today.
Real-Time Payments on Unit includes:
Send and receive into the accounts your customers already hold with you. Incoming credits are final under network rules*, so funds are usable on arrival.
A pre-send check that the recipient's bank can receive RTP, so your code can choose the rail itself 
The network's rejection codes and transaction ID on every payment 
A TimedOut status for payments that don't resolve
tags to carry your order or invoice ID onto the transaction, and idempotent retries that never create a duplicate payment
Sender account details on incoming payments
 Every rail, one ledger 
Because RTP sits alongside every other rail on Unit, you can combine them in a single build:
Pay a seller over RTP the moment an order is confirmed, with the order ID already on the ledger entry
Check whether a recipient's bank is on RTP and fall back to ACH automatically when it isn't
Receive an RTP payment into a customer's account on a Sunday and let them spend it on their Unit card minutes later 
Take funding by RTP on Saturday and pay a vendor by wire on Monday, from one balance
 Read the docs to learn more, or talk to our team .
‍
 Unit is a financial technology company and not a bank. Banking services are provided by Unit's bank partners, Members FDIC. 
 *As with other payment rails, received RTP payments can be returned after settlement in limited circumstances. See Unit’s docs for more information. 
Subscribe to our Newsletter
Build financial products on battle-tested infrastructure
Platform
 The Unit Platform 
 Managed Solutions 
Developers
 Sandbox 
 API Documentation 
 API Status 
 Technical Guides 
Use Cases
 Accounts & Wallets 
 Money Movement 
 Card Issuing 
 Capital 
Resources
 Resource Hub 
 Case Studies 
 Architecture 
 Program Management 
 Configure your Build 
Company
 About 
 Careers 
 Security 
Products
 For Businesses 
 For Consumers 
 For Independent Workers 
 For Vertical Software 
Find us on social
Certified and tested
 Privacy Policy 
 Terms of Use 
 Code of Conduct 
1. Unit is a financial technology company and not a bank. Banking services are provided by Unit's bank partners, Members FDIC. Deposit volume disbursed through Unit's partner bank ecosystem. Visa® debit cards are issued by Unit's bank partners pursuant to a license from Visa U.S.A. Inc. and may be used everywhere Visa debit cards are accepted.
Accounts are eligible for pass-through deposit insurance only to the extent pass-through insurance is permitted by the rules and regulations of the FDIC, and if the requirements for pass-through insurance are satisfied. There may be a risk that pass-through deposit insurance is not available because conditions have not been satisfied. In such cases, funds may not be fully insured in the event the insured depository institution where the funds have been deposited were to fail.
2. Deposit sweep networks may be offered through select Unit bank partners, Members FDIC. Please refer to the applicable bank partner’s deposit sweep network disclosures for more information.

## Контекст

<!-- enrichment:context -->
**[0] What exactly happened (de-PR'd).** On 2026-10-19 Unit (US Banking-as-a-Service / embedded-finance middleware, unit.co — a "financial technology company and not a bank") turned on Real-Time Payments (RTP) for its fintech/software partners: their end-customers can now send and receive RTP in seconds, 24/7/365, including weekends and holidays. The one genuinely load-bearing technical claim is "we connect directly to The Clearing House (TCH), with no intermediary processor" — i.e. Unit is a direct RTP participant/connection rather than routing through a third-party processor/aggregator. RTP sits on the same Payments API, native ledger and dashboard as Unit's existing rails (ACH, wire, check, international). Feature set: pre-send receiver-eligibility check (so code can pick the rail and fall back to ACH), network rejection codes + transaction ID surfaced per payment, a `TimedOut` status, idempotent retries (no duplicate payments), and tags to carry order/invoice IDs. Incoming credits are "final under network rules" (with the standard caveat that received RTP can be returned after settlement in limited circumstances).
— **Why framed this way / what it reveals.** The PR leads with a calendar-gap story ("114 days a year neither ACH nor wires settle") — a real but well-worn instant-payments pitch. The de-PR'd substance is narrow and infra-ish: (a) *direct* TCH connection = fewer hops, better latency, Unit owns the network-level data/return-code plumbing rather than reselling a processor's; (b) one-ledger-many-rails consolidation so partners can orchestrate RTP-with-ACH-fallback in one build. This is the SAME release wave as the sibling note [[Unit launches international payments to 190+ countries]] (2026-10-13) and a revolving-credit launch — Unit's "Fall 2026" product batch. It is NOT a duplicate of the international-payments note (different rail, different mechanism), so it is **fresh** — but it is part of the same batch-expansion story, not an isolated breakthrough.

**[1] Competitors / peers.** RTP-via-BaaS is now table stakes, not novel: the direct-comp is [[Increase adds push-to-card transfers to payments platform]] — Increase explicitly markets "direct connections to the Federal Reserve, Visa, and The Clearing House" and already offers RTP + FedNow + push-to-card, processing "hundreds of billions" for Gusto/Ramp/Stripe. So Unit's "direct, no intermediary" positioning is matching Increase, not leapfrogging it. Other US BaaS/money-movement peers with instant rails: Treasury Prime, Synctera, Column (charter-owning), Lead Bank, Modern Treasury (orchestration) ([[Modern Treasury partners with Sardine on fraud detection]]). Network backdrop: RTP (TCH) processed ~142M txns / ~$576B in Q2 2026, averaging >1.5M payments/day, with the per-txn limit raised to **$10M in Feb 2025**; FedNow had ~1,900 FIs live by Sept 2026 and ~5M customer payments in Q2 2026 — RTP still dwarfs FedNow on volume. Notably Unit's launch is RTP-ONLY (no FedNow mentioned), a gap vs Increase which offers both.
— **Why the landscape is this way / second order.** Instant-rail breadth has commoditized; competition has shifted to compliance/reliability, developer experience and *directness of network access* (own the return codes, latency, idempotency) rather than "do you have RTP at all." A direct TCH connection is a credibility/moat signal in a post-[[Synapse]] world where partners fear flaky intermediaries — but it is a parity move against Increase, not a differentiator.

**[2] Company history / fit.** Unit raised a $100M Series C led by Insight Partners at a **$1.2bn post-money (May 2022)** — the first US BaaS unicorn; that mark is >3 years stale and predates the post-Synapse de-rating. Its consistent strategy is to be the single middleware layer on which non-banks embed accounts, cards and every money-movement rail on partner banks (Members FDIC). Adding RTP, international (SWIFT) and revolving credit in one Fall-2026 wave is a logical "expand revenue-per-customer on infra already built" play as domestic rails commoditize and margins compress.
— **Why it acts this way.** Commoditized per-rail take rates push BaaS platforms to bundle more rails + attach higher-value products (credit, cross-border) onto existing programs to earn a software multiple rather than a thin payments spread.

**[3] Novelty / value-add / traction.** Novelty is modest. RTP itself is years old (TCH live since 2017); BaaS-delivered RTP already exists (Increase, et al.). The only arguably-new wrinkle is "*direct* to TCH, no intermediary processor" for Unit specifically, plus the orchestration niceties (pre-send eligibility check, auto-fallback to ACH, idempotent retries, invoice-ID tags) that are genuinely useful but not unique. **Traction: zero disclosed** — no customers, no volumes, no pricing, no named bank partner for RTP. This is a capability announcement, self-published on Unit's blog (677 words), with no independent press coverage found.
— **Why value-add is real/not, deeper.** Real value is incremental: fewer intermediaries can mean lower cost and better data/latency, and one-ledger orchestration lowers partner build cost (switching-cost moat). But who captures the margin? RTP economics are thin interbank fees; Unit's edge is distribution/orchestration, not the rail. Absent disclosed take-rate or volume, this reads as a feature-parity checkbox that defends revenue-per-customer, not a re-rating event.

**[4] What's next / market sentiment.** US instant payments are structurally rising (RTP $10M limit + record volumes; FedNow expanding reach), and FedNow/RTP interoperability + cross-border RTP experiments ([[FedNow cross-border plan tests real-time payments infrastructure]]) are the frontier. Expect Unit to add FedNow next (to match Increase) and to lean on RTP as a feeder for its card and international products (e.g. "receive RTP Sunday, spend on a Unit card minutes later"). Regulatory backdrop: post-Synapse, sponsor banks bear accountability; a direct-TCH model doesn't remove sponsor-bank/AML/fraud-return surface (RTP push payments are a known APP-fraud vector).
— **Why / counterintuitive.** The direct-TCH framing is as much a trust/credibility signal (post-Synapse "no flaky middleman") as a technical one. But faster, irreversible, final-on-arrival credits raise authorized-push-payment fraud risk — "funds usable on arrival" is the exact property fraudsters exploit; the PR is silent on fraud/return liability split between Unit, provider-less direct connection, and sponsor bank.

Sources: Unit blog (RTP) <https://www.unit.co/blog/real-time-payments> · Unit Fall 2026 releases <https://www.unit.co/blog/fall-2026-product-releases> · Unit RTP insight <https://www.unit.co/more-insights/rtp-real-time-payments> · TCH RTP network <https://www.theclearinghouse.org/payment-systems/rtp> · TCH $10M limit <https://www.paymentsdive.com/news/real-time-payments-network-transacion-limit-increase/734710/> · FedNow vs RTP 2026 <https://www.qubevents.com/post/post-fednow-vs-rtp-next-phase-instant-payments-us-banks> · Insight Partners (Unit $1.2bn) <https://www.insightpartners.com/ideas/banking-as-a-service-platform-unit-announces-100-million-series-c-led-by-insight-partners-valuing-the-company-at-1-2-billion/>
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. Is "direct to The Clearing House, no intermediary processor" actually distinctive, or does Increase (and others) already do the same? Increase explicitly markets "direct connections to … The Clearing House" — so is this parity, not differentiation? (Leans parity.)
2. Is Unit a direct RTP *participant/funding agent* or just a direct technical *connection* on top of a sponsor bank that is the actual RTP participant? The PR says "no intermediary processor" but Unit is not a bank — the sponsor bank is the network participant. (Open — likely sponsor-bank-fronted.)
3. Why RTP only and no FedNow? Increase offers both. Is omitting FedNow a gap, a sequencing choice, or a sponsor-bank limitation? (Open.)
4. Any traction? Zero customers, volumes, pricing, or named bank partner disclosed. Is there evidence of demand or is this purely a capability announcement? (Announcement only.)
5. Single-source, self-published 677-word blog, no independent coverage. How much weight should a self-announcement carry?
6. Who bears authorized-push-payment (APP) fraud liability on irreversible, "final on arrival" RTP credits — Unit, the sponsor bank, or the partner? The PR is silent. (Silent → red flag.)
7. "Incoming credits are final under network rules*" with an asterisk that they CAN be returned after settlement "in limited circumstances." How final is final, really?
8. What does Unit charge for RTP, and what's the take rate vs raw TCH interbank fees? Where is the margin — rail or orchestration? (Undisclosed.)
9. Does the $10M RTP limit (Feb 2025) even apply through Unit's sponsor-bank setup, or are partner limits lower? (Open.)
10. Is this a defensive catch-up to Increase/Treasury Prime rather than an offensive move? (Leans catch-up.)
11. Is this double-counting newsworthiness — is it being treated as a separate story when it's one of three items in the same "Fall 2026" release batch (with international payments and revolving credit)? (Fresh as a distinct rail, but same wave.)
12. Which sponsor bank(s) support RTP on Unit, and is RTP enabled across all partner banks or only some? (Open.)
13. Does the "receive RTP then spend on a Unit card minutes later" flow actually work end-to-end today, or is it illustrative? (Asserted, not demonstrated.)
14. Post-Synapse, does adding a fast, irreversible rail increase reconciliation/fraud surface at a time the sector is under heightened FDIC/OCC/Fed scrutiny? (Material risk.)
15. Is the "114 days nothing settles" calendar framing a real customer pain or a generic instant-payments marketing trope reused across the industry? (Trope.)

**Importance: 2/5 — rationale.** A logical, sensible rail addition by a notable US BaaS player (Unit, 2022's first BaaS unicorn), delivered in its Fall-2026 batch alongside international payments and revolving credit. But novelty is low: RTP is years old, BaaS-delivered RTP already exists, and the one distinctive claim ("direct to TCH, no intermediary") merely matches Increase rather than leapfrogging it. It is a single-source self-announcement with no customers, volumes, pricing, named bank partner, or FedNow support, and it is a feature-parity catch-up that defends revenue-per-customer rather than a market-moving event. Newsworthy as a signal of BaaS middleware bundling more instant rails, not as a re-rating. **Fresh** (a distinct rail/mechanism, not a duplicate of the sibling international-payments note), but same release wave.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** US instant-payments rails are now in a scaling phase, and Unit is adding RTP as middleware on top of a partner bank. TCH's RTP network processed ~150M transactions worth ~$621bn in Q3 2026 (daily average ~$6.9bn as of Sep 2026) and set a single-day record of 2.27M txns / $8.62bn on 1 May 2026; the network averages >1.5M payments/day in 2026 (per The Clearing House / PYMNTS, via pymnts.com and theclearinghouse.org). Reach is now effectively ubiquitous: RTP touches ~1,200–1,378 FIs and FedNow ~1,700, with instant payments collectively reaching >75% of US bank accounts as of 2026 (per paymentsdive/fintechspecs). Structure: the rails themselves are a duopoly (bank-owned TCH RTP vs public FedNow), both credit-push and irreversible; value for a BaaS firm is captured not in the rail but in the orchestration layer (one ledger, rail-selection, idempotency, fallback-to-ACH). Barriers are regulatory (sponsor-bank relationship, fraud liability) more than technical. Why now: with instant rails past the ~75% reach tipping point, "24/7/365 money movement" is becoming table stakes rather than a differentiator — the laggard among infra vendors loses deals, so this is a defensive catch-up as much as an offensive launch (analysis).

**Competitive landscape.** Sector KPIs for BaaS: deposit volume / accounts on platform, interchange + per-transaction take, net revenue/ARR, and program retention. Key players and basis of competition:
- **Charter-owning stack (structural advantage):** Column (own charter; ~$291M revenue per Sacra) and Increase (launched Increase Bank; added RTP/FedNow/push-to-card, and on 1 Jul 2026 launched stablecoin instant payments with Grasshopper) own ACH/wire/FedNow/RTP end-to-end with no middleware dependency.
- **Multi-bank middleware (Unit's own category):** Treasury Prime (multi-bank routing, FedNow+RTP), Synctera, and Unit — these sit between fintechs and sponsor banks.
Recent peer moves: Increase added push-to-card (May 2026, [[Increase adds push-to-card transfers to payments platform]]); Treasury Prime launched Prime Cash with the Green Dot Network (May 2026, [[Treasury Prime launches Prime Cash with Green Dot Network]]); Unit itself launched international/SWIFT payouts days earlier on 13 Oct 2026 ([[Unit launches international payments to 190+ countries]]). Unit's position: **catching up to parity** on rails — RTP is now broadly available across competitors; its differentiation is the unified "every rail, one ledger" developer experience and the direct TCH connection "with no intermediary processor" (per unit.co). Moat is switching costs / developer lock-in on an existing program, not a rail monopoly (analysis).

**Comps & multiples.** Unit is private; last disclosed round was a **$100M Series C at a $1.2bn valuation (May 2022, Insight Partners)** — ~3.5-year-old mark, no refresh found for 2026, so no current multiple is computable (no data on revenue → EV/Rev = no data; valuation is a stale round mark, not market cap). Internal comps (private rounds / own-charter peers):
- [[Mercury raises $200 million at $5.2 billion valuation]] — ~$20bn deposits, ~$650M ARR, GAAP-profitable → ~8.0x ARR (`$5.2bn / $650M`), a startup-banking benchmark but a direct neobank, not a BaaS vendor (comparability: adjacent, not pure).
- Column — ~$291M revenue, own-charter (per Sacra); [[Erebor passes $7bn in deposits eight months after launch]] cites it as a charter-owning comp.
- [[Treasury Prime launches Prime Cash with Green Dot Network]] and [[Increase adds push-to-card transfers to payments platform]] — closest pure BaaS/infra peers; no public revenue/valuation → multiples not computable.
Distribution not computed (<3 clean, comparable valuation+revenue pairs). Qualitative read: at a stale $1.2bn mark Unit looks cheap vs Mercury's $5.2bn, but the two are not the same model and Unit's current revenue is undisclosed — `[UNSOURCED]`.

**Risk flags.**
1. **Disintermediation by charter-owning peers (→ margin squeeze).** Column and Increase own their charter and the full rail stack; as RTP/FedNow commoditize, the value shifts to whoever holds the balance sheet and eliminates the sponsor-bank middle layer — Unit's "no intermediary processor" line mitigates processor fees but not the structural dependence on a partner bank.
2. **Sponsor-bank / BaaS counterparty risk (→ platform continuity).** The US BaaS model has a live fraud-and-reconciliation track record (Synapse collapse; see [[California fines Yotta \$1 million over false FDIC-insurance claims]]) and current litigation over fintech loan losses at partner banks ([[Investors sue Coastal Financial after fintech loan losses]]). Unit depends on partner banks (Members FDIC) for the actual banking; a partner's problems become Unit's program risk.
3. **Irreversible-credit fraud exposure (→ liability silence).** RTP credits are final under network rules; the PR is silent on who eats fraud/mistaken-payment losses. Instant + irreversible is a known APP-fraud vector, and liability allocation across Unit, the partner bank, and the end program is the unstated economics.

**What this changes (idea-lens).** Incremental, not re-rating: RTP going "live on Unit" closes a feature gap rather than opening a new one — with instant rails at >75% reach, this is table stakes catch-up (analysis). Falsifiable thesis: the durable winners in US BaaS will be charter-owning stacks (Column, Increase, chartering Mercury), and pure middleware like Unit will face compressing take rates unless it moves up-stack (international/SWIFT, ledger, fraud tooling) — which the 13 Oct international-payments launch suggests it is already doing. Watch: a fresh Unit funding round / valuation mark (would re-price the sector), and any Unit move toward its own charter. Thesis breaks if middleware proves stickier than charters via developer lock-in and multi-bank optionality.

Sources: https://www.unit.co/blog/real-time-payments · https://www.pymnts.com/real-time-payments/2026/rtp-network-marks-record-2-million-transactions-in-a-day · https://www.paymentsdive.com/news/clearing-house-rtp-real-time-payments-network/721105/ · https://fintechspecs.com/blog/increase-vs-column/ · https://sacra.com/c/column/ · https://www.fintechfutures.com/fintech-start-ups/baas-start-up-unit-raises-100m-series-c-reaches-1-2bn-valuation
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
