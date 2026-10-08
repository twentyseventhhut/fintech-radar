---
title: "Plaid unveils LendScore Arc transformer credit model"
date: 2026-10-07
retrieved: 2026-10-08
tags:
  - company/plaid
  - industry/ai
  - industry/credit
  - region/us
  - type/product
sources:
  - https://plaid.com/whats-new/fall-2026
  - https://plaid.com
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s7d055d3e
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Plaid unveils LendScore Arc transformer credit model

> [!info] 2026-10-07 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Plaid unveils its Fall 2026 release for intelligent finance, including LendScore Arc, its first transformer model for credit risk. In early testing, Arc, which learns from transaction sequences, increased approvals by 20% for subprime borrowers.

## Первоисточники

### plaid.com
<https://plaid.com/whats-new/fall-2026>
*719 слов · direct*

Meet the new models

 20% approval lift for subprime borrowers with LendScore Arc 
 26% more risky ACH dollars caught over previous payment risk model 
 10% fewer dollars lost with the latest Cash Advance Index 
Introducing Instant Link & LendScore 2

INSTANT LINK
Cash flow insights at application, not after
Instant Link brings cash flow data straight into the application, without asking eligible users to re-connect their bank accounts. More insight. Less waiting.

INSTANT LINK
Cash flow insights at application, not after
Instant Link brings cash flow data straight into the application, without asking eligible users to re-connect their bank accounts. More insight. Less waiting.

LENDSCORE
There’s a LendScore for that
LendScore is now a family of specialized scores for different types of lending, all built on consumer-permissioned cash flow and network insights.

LendScore 2 
Ls2, our next-generation core model, delivers 42% greater predictive power than traditional cashflow data alone.
LendScore Arc
Arc, our first transformer-based credit risk model, learns from transaction sequences. In early testing, Arc increased approvals by 20% for subprime borrowers.
Scores for Auto, Home Lending, and Short Term
New Ls2 Auto, Home Lending, and Short Term models are tuned to the risk dynamics of each type of lending.
Signal
Sharper risk signals for every payment
Signal 4 now reads payment history in broader context, using Plaid's Sequential Foundation Model, with deeper cash flow, income, and spending pattern insights. In early testing, it caught 126% more risky dollars than the previous model.

Signal
Sharper risk signals for every payment
Signal 4 now reads payment history in broader context, using Plaid's Sequential Foundation Model, with deeper cash flow, income, and spending pattern insights. In early testing, it caught 126% more risky dollars than the previous model.

Guaranteed Payments
More configurability over what gets guaranteed
Guaranteed Payments now factors in your own trust indicators, like account tenure and wallet balance, and refreshes fraud signals with every transaction. 
New controls, like delayed release and partial guarantees, help businesses approve with more confidence.

Guaranteed Payments
More configurability over what gets guaranteed
Guaranteed Payments now factors in your own trust indicators, like account tenure and wallet balance, and refreshes fraud signals with every transaction. 
New controls, like delayed release and partial guarantees, help businesses approve with more confidence.

Explore the new fraud foundation model

FRAUD FOUNDATION MODEL
From snapshots to storylines
Our new Fraud Foundation Model learns richer patterns across the network—transactions, devices, identities, and more—powering Plaid’s fraud solutions.
In internal evaluations, it shows up to 40% relative improvement over previous models.

FRAUD FOUNDATION MODEL
From snapshots to storylines
Our new Fraud Foundation Model learns richer patterns across the network—transactions, devices, identities, and more—powering Plaid’s fraud solutions.
In internal evaluations, it shows up to 40% relative improvement over previous models.

CASH ADVANCE INDEX
Better signals, clearer views
Cash Advance Index 2 now runs on Plaid's Sequential Foundation Model, helping you see risk more clearly with a new dashboard and income insights for every repayment decision.

CASH ADVANCE INDEX
Better signals, clearer views
Cash Advance Index 2 now runs on Plaid's Sequential Foundation Model, helping you see risk more clearly with a new dashboard and income insights for every repayment decision.

Transactions, Liabilities & Investments
Accuracy and coverage keep climbing

Transactions
Transactions has improved merchant name accuracy by over 19%.
Liabilities
Liabilities adds coverage for more auto loans, HELOCs, personal loans, and lines of credit.
Investments
95% of Investments holdings now have at least two identifiers for easier reconciliation.
Layer
More ways to build your flow
Customize onboarding with the new Layer. Collect identity and bank data together or separately. Let returning users share saved identity documents in one tap. Easier, faster, and flexible to what you need. 

Layer
More ways to build your flow
Customize onboarding with the new Layer. Collect identity and bank data together or separately. Let returning users share saved identity documents in one tap. Easier, faster, and flexible to what you need. 

Link
Faster connections, ready to customize
Link has been rebuilt from the ground up: modernized UI, smoother connections, and a shared component library for quicker shipping.

Link
Faster connections, ready to customize
Link has been rebuilt from the ground up: modernized UI, smoother connections, and a shared component library for quicker shipping.

Product deep dives drop Oct 27

Get on the list for a first look.

### Прочие ссылки (без извлечённого текста)

- <https://plaid.com>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Plaid unveils LendScore Arc transformer credit model
_Analytical notes (not a post). Importance: 3/5. Freshness: fresh (builds on but materially advances [[Plaid launches LendScore credit risk score]], Oct 2025)._

## [0] What exactly happened (de-PR'd)
On **2026-10-06** (businesswire dateline; Plaid's social push 10-07) Plaid shipped its annual **Fall 2026 release**. The headline item is **LendScore Arc** — Plaid's *first transformer-based credit risk model*, powered by a new **Sequential Foundation Model** that reads the *order, timing, cadence and interactions* of a borrower's transactions (e.g. a Friday direct deposit followed by Monday bill payments), then fuses those signals with the existing tabular LendScore underwriting features. Arc sits inside a broader **LendScore 2 (Ls2)** family: an upgraded core model plus specialized Auto / Home Lending / Short Term variants. The same foundation model also powers **Signal 4** (ACH risk), a new **Fraud Foundation Model** (Plaid Protect) and **Cash Advance Index 2**.

**De-PR'd reality — this is a preview, not a product you can buy today.** Every number is **Plaid-internal, "early testing"**, with no independent validation and inconsistent baselines:
- Arc **"+20% approvals for subprime"** — measured vs Plaid's *own* prior core LendScore model (blogs also cite 20% deep-subprime / 24% superprime lift). Not vs the bureau.
- Ls2 core **"42% greater predictive power"** — vs **"traditional credit data alone"** (i.e. a flattering bureau-only baseline), *not* vs LS1.
- Signal 4 **"126% more risky dollars caught"** — *relative* vs Signal v3 at a 5% decline rate; the "26% more risky ACH dollars" is a different cut (1% decline rate).
- Fraud Foundation Model **"40% relative improvement"** — vs prior Trust Index; internal only, contact-sales (not GA).
- Cash Advance Index **"10% fewer dollars lost"** — appears **only on the landing page**; Plaid's own blog/Effects recap instead cite "-8 pp delinquency in an A/B test with *a leading provider*" (unnamed). **Possibly a different metric — treat as unconfirmed.**

**Why framed this way:** anchoring Ls2 to "traditional credit data alone" maximizes the lift headline while quietly conceding the honest comparison (Arc vs the prior LendScore) is the smaller, truer 20-24% number. The "Product deep dives drop Oct 27" line on the page is the tell: Arc is **early-testing / preview, not GA**, and there are **zero named customers** for LendScore or Arc in any source.

## [1] Competitors / peers
- **FICO — Cash Flow UltraFICO** (with Plaid itself, 2025-11-20) and **Experian Credit + Cashflow Score** (2025-11-10, claims >40% lift): both use Plaid/open-banking cash-flow data but are **not** transformer/sequence models. See [[FICO partners with Plaid on cash flow score]], [[FICO and Plaid launch UltraFICO Score adding cashflow data]], [[Experian and Plaid team up on open banking credit decisions]].
- **Nova Credit / Prism Data / Pinwheel / MX / Ocrolus / Zest AI / Upstart / Scienaptic**: cash-flow or ML underwriting; **no public evidence any has shipped a transformer/sequence credit model** (searches found none — "not found", not "confirmed absent"). See [[Nova Credit integrates cash-flow analytics into Imprint underwriting]].
- **Closest technical prior art is NOT a US credit vendor:** **Nubank's nuFormer** (arXiv 2507.23267, Jul 2025) and **Revolut's PRAGMA** are genuine GPT/transformer-style foundation models over ~100B transactions. So "first transformer credit model" is Plaid's *first* and likely a **US-cash-flow-vendor first**, but the technique predates it — treat the "industry-first" frame as marketing.
- **Position:** ahead of its direct US cash-flow peers on *technique*, at parity-or-behind the global neobanks on the underlying foundation-model science.

**Second-order:** the awkward fact is Plaid partners with FICO/Experian (distribution) while simultaneously building Arc (a competing standalone score via its Plaid Check CRA). It is both the pipe and, increasingly, the scorer — a channel-conflict that gets sharper the better Arc performs.

## [2] Company history / fit
Trajectory: open-banking connectivity core → **LendScore (LS1)** launched ~Oct 2025 "in beta" ([[Plaid launches LendScore credit risk score]]) → FICO/Experian cash-flow tie-ups through 2025-26 → **Fall 2026** foundation-model push. Valuation **~$8B** (Feb 2026 employee tender, up ~31% from the $6.1B April-2025 primary round; peak $13.4B in 2021); Sacra est. ~$546M ARR 2025 (+40% YoY); preliminary IPO talks reported mid-2026, no S-1.

**Why it acts this way (analysis):** connectivity/data-transit is a commoditizing, price-pressured take-rate business. To justify a software multiple ahead of an IPO, Plaid must climb the stack into **higher-margin intelligence/risk products** (LendScore via its CRA, Protect, Signal) that monetize the one asset rivals can't copy cheaply — the transaction graph across ~1M daily connections. Arc is the clearest expression of that "connectivity → intelligence" pivot.

## [3] Novelty / value-add / traction
**Genuinely new:** applying a pretrained sequence transformer (attention over transaction order/timing) to consumer credit, with Integrated-Gradients reason codes for adverse-action compliance, is a real technical step up from static cash-flow aggregates — *for a US credit vendor*. **What's NOT new:** the transformer-over-transactions idea (Nubank/Revolut already published it) and cash-flow underwriting itself (Plaid has sold this since 2025).

**Traction = essentially none proven.** All lift figures are internal/early-testing; no GA, no named lenders, deep dives deferred to Oct 27. "Announced," not "adopted."

**Who captures the margin (analysis):** the value-add is real *only if* the lift survives (a) out-of-sample on live portfolios and (b) regulatory explainability. The data moat is Plaid's, but the lender captures the loss-reduction economics, and FICO/Experian still own the distribution rails into most underwriting stacks — so Arc risks being a better *ingredient* sold through others' scores rather than the score lenders actually pull. The central question is less "is the model better" (plausibly yes) than **"can Plaid get lenders to underwrite on *its* score rather than a bureau's, given channel conflict and fair-lending risk."**

## [4] What's next / market sentiment
Oct 27 product deep dives; Signal 4 broad rollout "early Q4 2026"; IPO overhang. **Regulatory backdrop is the real swing factor:** ECOA/Reg B require adverse-action notices with up to 4 *specific, accurate* reasons, and a transformer is a black box. CFPB Circular **2022-03** (AI models get no "algorithm said so" pass) was **withdrawn May 2025** under the current administration — reducing *near-term federal-guidance* pressure, but the **statute and state/ litigation exposure remain**. (A supposed "Circular 2026-03" reinstating this surfaced in one secondary source and could **not** be verified — flagged.)

**Counterintuitive second-order:** the guidance rollback is a short-term tailwind that could become a trap — if Plaid leans into black-box scoring now and enforcement swings back, the most "predictive" model becomes the hardest to defend. Explainability (Integrated Gradients reason codes), not raw lift, is the durability test.

## Sources
- https://plaid.com/whats-new/fall-2026
- https://plaid.com/blog/instant-link-next-generation-lendscore/
- https://plaid.com/blog/foundation-models-power-plaid-intelligence-products/
- https://plaid.com/blog/signal-v4-launch-ach-risk-model/
- https://www.businesswire.com/news/home/20261006091265/en/
- https://plaid.com/blog/plaid-lendscore-credit-risk-scoring/ (LS1, Oct 2025)
- https://arxiv.org/abs/2507.23267 (Nubank nuFormer, prior art)
- https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/ (CFPB Circular 2022-03 withdrawal, May 2025)
- Internal corpus: [[Plaid launches LendScore credit risk score]], [[FICO partners with Plaid on cash flow score]], [[FICO and Plaid launch UltraFICO Score adding cashflow data]], [[Experian and Plaid team up on open banking credit decisions]], [[Nova Credit integrates cash-flow analytics into Imprint underwriting]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is Arc actually live?** No — "early testing," deep dives deferred to Oct 27, no GA language, zero named customers. **(answered: preview, not GA.)**
2. **Vs what baseline is the +20%?** Plaid's own prior core LendScore, *not* the bureau; the flashier "42%" is vs "traditional credit data alone." The honest Arc-vs-LendScore delta is the smaller 20-24%. **(answered.)**
3. **Any independent validation of any number?** None found. 100% company-internal. **(answered: unverified.)**
4. **Is "first transformer credit model" true?** Plaid's first and plausibly a US-cash-flow-vendor first, but Nubank (nuFormer, Jul 2025) and Revolut (PRAGMA) published comparable transformer-over-transaction models earlier. **(answered: marketing framing.)**
5. **Does "10% fewer dollars lost" (Cash Advance Index) reconcile with the blog's "-8 pp delinquency"?** No — different metrics/sources; the landing-page figure is uncorroborated. **(open — wait for Oct 27.)**
6. **Who are the named lenders using LendScore or Arc?** None disclosed anywhere. **(open.)**
7. **Fair-lending/ECOA exposure of a black-box transformer?** High in principle; Plaid's mitigation is Integrated-Gradients reason codes — untested against examiner "specific and accurate" standard. **(open.)**
8. **Did CFPB Circular 2022-03 get reinstated in 2026?** Could not verify a "2026-03" reinstatement; only the May-2025 withdrawal is confirmed. **(open/unverified.)**
9. **Channel conflict:** Plaid supplies cash-flow data to FICO/Experian *and* sells a rival standalone score (Arc via its CRA). Who does the lender ultimately pull? **(open — strategic risk.)**
10. **Does lift survive out-of-sample on live portfolios?** Unknown; early-testing lift routinely decays live. **(open.)**
11. **Who captures the economics?** Lender gets loss reduction; FICO/Experian own distribution; Plaid owns the data. Arc may remain an ingredient, not the score. **(analysis.)**
12. **Is this a duplicate of the Oct 2025 LendScore launch?** No — new model class (transformer/Arc), new core (Ls2), new testing numbers; builds on [[Plaid launches LendScore credit risk score]] but is a distinct event. **(answered: fresh.)**
13. **Why the IPO-timed push up-stack?** Commodity connectivity take-rate needs a software multiple; intelligence products monetize the transaction graph ahead of a listing. **(hypothesis.)**
14. **What breaks the thesis?** Regulatory swing-back on black-box scoring, failure to win direct lender adoption vs bureaus, or lift not surviving live. **(analysis.)**
15. **Exact announce date?** 2026-10-06 (businesswire), not 10-07; note frontmatter says 10-07 (social push). Minor. **(answered.)**

**Importance: 3/5** — Genuinely new technique for a US credit vendor and a clean read on Plaid's pre-IPO "connectivity → intelligence" strategy, which lifts it above a routine feature release. But capped at 3: all metrics are internal/early-testing, no GA, no named adopters, the transformer-over-transactions idea is prior art (Nubank/Revolut), and the hardest questions (live lift, fair-lending defensibility, channel conflict) are all unresolved. A promising preview, not a proven, adopted product.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-08]] (2026-10-08).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: alternative credit data / cash-flow underwriting on top of open-banking rails. Market size: per Mordor Intelligence, the alternative credit scoring market was ~$4.22bn in 2026, growing ~21% CAGR toward ~$11.07bn by 2031 (secondary analyst estimate, treat as order-of-magnitude, not audited). Structure: the value chain is consolidating into three layers — (1) bank-data connectivity (Plaid, MX, Finicity/Mastercard), (2) scoring/decisioning models built on that data (LendScore, FICO, Experian, Nova Credit), (3) the lenders. Plaid historically sat in layer (1) and is now pushing up into layer (2) — selling the score, not just the pipe. Entry barriers: data-network scale (Plaid says >1 in 2 US bank-account holders have used it, per 2024 shareholder letter) and consumer-permissioned coverage. "Why now": (a) GSE adoption of cash-flow/alt-data (FICO 10T, VantageScore 4.0) legitimizes bank-statement data for mortgage; (b) FICO's Oct-2025 direct-licensing move that bypasses the bureaus (per Forbes, 2025-10-04) is unbundling the bureau stack, opening room for new scores; (c) the transformer/"foundation-model" tech shift lets sequence models read transaction order/timing, not just snapshots.

**Competitive landscape.** Sector KPIs: predictive lift / Gini-KS vs incumbent score, approval-rate lift at fixed loss (or loss reduction at fixed approval), thin-file/subprime coverage, and lender attach/adoption. Plaid's claimed numbers for Arc: +20% approvals for (deep) subprime, +24% superprime lift, LendScore 2 core +42% predictive power vs traditional cash-flow data; Signal 4 catches +126% more risky dollars (all Plaid internal/early-testing figures — vendor-reported, not independently validated; de-PR: "early testing" ≠ live book performance). Key players & basis of competition: FICO (incumbent score, now unbundling from bureaus — and notably a Plaid *partner* via the Nov-2025 FICO x Plaid cash-flow score [[FICO partners with Plaid on cash flow score]], so Plaid is simultaneously partner and emerging competitor); Experian (open-banking credit decisions, incl. a 2025 Plaid tie-up [[Experian and Plaid team up on open banking credit decisions]]); Nova Credit (cash-flow analytics, Chase win Sep-2025 [[Chase taps Nova Credit for underwriting]], $35M Series D Oct-2025 [[Nova Credit raises $35M Series D for cash-flow underwriting]]); Dave (CashAI v5.5, in-house cash-flow risk [[Dave introduces CashAI v5.5]]). Basis of competition = model accuracy + distribution (already-integrated data pipe) rather than price. Plaid's position: ahead on distribution/data-network reach, catching up on being a *scoring* vendor (FICO/VantageScore own lender mindshare and regulatory acceptance). Moat: network effects + switching costs from embedded Link integration (analysis). Proprietary unit economics (CAC, model licensing price) → [UNSOURCED].

**Comps & multiples.** Plaid is private; no public EV. Last marks: ~$575M primary round at ~$6.1bn (Apr-2025, per CNBC); employee tender at ~$8bn (Feb-2026) [[Plaid completes tender offer at $8 billion valuation]], up ~31% but still ~40% below the 2021 peak of ~$13.4bn (per thepaypers/GL Insight). ARR: ~$546M in 2025, +40% YoY from ~$390M (per Sacra/getlatka; corpus: [[Plaid ARR climbs 40% to over $500m as IPO weighed]]). Implied price/ARR (round valuation, NOT market cap): $8bn / ~$0.546bn ≈ **14.6x** (also $6.1bn / ~$0.39bn ≈ **15.6x** at the Apr-2025 mark). Sanity: ~15x revenue is rich on an absolute basis but defensible for a ~40%-growth data-infrastructure name — in-line with the growth, so not an automatic flag. External comps: FICO is public (NYSE: FICO) but its revenue mix/scale isn't cleanly comparable to a private data-network — EV/Revenue not computed here ("no data" on a like-for-like basis). Internal comps as wikilinks above; distribution not computed (fewer than 3 truly comparable post-money figures).

**Risk flags.** (1) *Vendor-reported lift, unvalidated* — every Arc/LendScore2 number is Plaid "early testing"; no independent out-of-sample or through-the-cycle loss data. A +20% subprime-approval lift that isn't matched by holding losses flat would simply mean looser credit, which looks great until a downturn. (2) *Fair-lending / model-risk regulation* — a transformer on raw transaction sequences is a black box; adverse-action reason codes and disparate-impact testing (ECOA/Reg B) are the gating constraint, and "approve more subprime" is exactly the segment regulators scrutinize. (3) *Channel conflict / disintermediation* — Plaid moving from data pipe into the scoring layer competes with its own partners (FICO, Experian), who could route around Plaid or build native connectivity; conversely Plaid remains dependent on bank data-access rails that incumbents and 1033-rule shifts can tighten.

**What this changes (idea-lens).** This is Plaid attempting a re-rating from "connectivity utility" to "decisioning/IP vendor" — higher-margin, stickier, and a better IPO story (CFO has said IPO can wait while ARR compounds [[Plaid ARR climbs 40% to over $500m as IPO weighed]]) (analysis). Falsifiable thesis: if, within ~12 months, a named Tier-1 lender publicly adopts LendScore Arc for live underwriting (not pilot) with disclosed loss performance, the move up-stack is working; trigger to watch = the Oct-27 product deep-dives and any FICO/Experian response (do they deepen the Plaid partnership or compete head-on?). What breaks the thesis: lenders keep Plaid as the pipe but buy the *score* from FICO/VantageScore, leaving Plaid stuck in the low-margin connectivity layer.

**IR grounding (plaid, IR-covered).** Apr-2025 ~$575M raise led by Franklin Templeton (~$6.1bn) — https://drive.google.com/file/d/1uxJ7wNzVgwvtCUyrKs1b132RgxaE4kvB/view · 2025 annual shareholder letter: record adoption, AI fraud prevention, expansion of bank payments + alternative credit data — https://drive.google.com/file/d/1gDZVVbBKve-zY5UusvR4NLZsy-LtTYAF/view · 2024 shareholder letter: >1 in 2 US bank-account holders have used Plaid — https://drive.google.com/file/d/191AN9VObvvAaM94i7oTbsekmNiCO8w9U/view · Fall-2025 product release (prior release — same credit/fraud/payments model cadence) — https://drive.google.com/file/d/1KbIO-krJpkqKRrWCx23TPHIBoeZ60rJL/view · 2025 Year-in-Review (AI categorization +10–20% accuracy) — https://drive.google.com/file/d/1tF5pGDc1weTlCg_D9_eOQL_-4WIvOLQ0/view

Sources: https://plaid.com/whats-new/fall-2026 · https://www.businesswire.com/news/home/20261006091265/en/Plaid-Releases-New-AI-Models-to-Improve-Decisions-Across-Credit-Fraud-and-Payments · https://www.pymnts.com/consumer-finance/2026/plaid-launches-credit-and-fraud-models-fueled-by-cash-flow-data/ · https://www.mordorintelligence.com/industry-reports/alternative-credit-scoring-market · https://www.forbes.com/sites/christerholloman/2025/10/04/how-ficos-new-license-disrupts-the-credit-bureaus/ · https://www.cnbc.com/2025/04/03/plaid-raises-575-million-funding-round-at-6-billion-valuation.html · https://thepaypers.com/payments/news/plaid-reaches-usd-8-billion-valuation-in-new-funding-round · https://sacra.com/c/plaid/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**no full earnings report in the news.** This is Plaid's Fall 2026 product release (LendScore Arc transformer credit model, LendScore 2, Signal 4, Fraud Foundation Model), not a results print. It carries only product-efficacy metrics in early/internal testing — +20% approvals for subprime borrowers (Arc), +42% predictive power vs cashflow data alone (Ls2), +126% risky dollars caught (Signal 4), up to +40% relative improvement (Fraud Foundation Model), +19% merchant-name accuracy (Transactions) — with no revenue, margin, EPS, or guidance. Plaid is a private company with no reported financials: `ir_latest.json[plaid].latest_result` is `None`, and its entire IR corpus is a funding announcement (~$575M led by Franklin Templeton, ~$6.1B valuation, Apr 2025), annual shareholder letters, year-in-review posts, and product updates — none an earnings report. No earnings analysis possible. Sources: https://plaid.com/whats-new/fall-2026 · pipeline/ir/ir_latest.json[plaid] (latest_result: null).
<!-- /enrichment:earnings_review -->
