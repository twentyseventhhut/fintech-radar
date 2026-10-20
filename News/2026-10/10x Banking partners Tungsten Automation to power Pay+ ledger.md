---
title: "10x Banking partners Tungsten Automation to power Pay+ ledger"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/10x-banking
  - company/tungsten
  - industry/banking
  - region/uk
  - type/partnership
sources:
  - https://www.10xbanking.com/news/powers-tungsten-pay-plus-embedded-payments-platform
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s565c7b85
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# 10x Banking partners Tungsten Automation to power Pay+ ledger

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 10x Banking partners with Tungsten Automation to power its Pay+ ledger. It marks 10x's first deployment outside a regulated financial institution. Pay+ is expected to be generally available in the UK and US in Q1 2027.

## Первоисточники

### 10xbanking.com
<https://www.10xbanking.com/news/powers-tungsten-pay-plus-embedded-payments-platform>
*520 слов · direct*

Key facts
10x Banking powers the real-time transaction ledger behind Tungsten Automation's new Pay+ platform.
Pay+ extends Tungsten's market-leading accounts payable capabilities into embedded payments.
Deployment and API integration were completed in under three months using an AI-led delivery approach.
Pay+ is expected to be generally available in the UK and US in Q1 2027.
 LONDON, UK  – 10x Banking, the 4th-generation core banking platform that powers some of the world’s largest financial institutions including Westpac and Chase UK , today announces a partnership with Tungsten Automation , the global leader in intelligent document and accounts payable automation, to provide the core ledger behind Pay+, Tungsten’s new embedded payments proposition. Embedded payments extends Tungsten’s market-leading AP capabilities into a full invoice-to-pay solution.  This partnership is a deliberate expansion of 10x’s technology beyond traditional banks and building societies into embedded finance . It marks a specific first for 10x: its first deployment inside a platform that is not a regulated financial institution, with the ledger embedded at the core of Tungsten’s payments infrastructure.  Pay+ brings the creation, execution, and reconciliation of AP payments into a single workflow, using invoice and supplier data to orchestrate each payment through the right provider or rail across Tungsten’s network of regulated payment partners. Because 10x Banking's core ledger records every transaction across the Pay+ ecosystem in real time, this enables context-aware, streamlined, reconciliation – making end-of-period reconciliation backlogs a problem of the past.  10x’s ability to attach rich payment and commercial data to every transaction is what makes this possible. Each entry can carry the provider, the rail, the payment category and the associated charges, providing a consistent record across any integrated payment modality.  The ledger was deployed within Tungsten’s own infrastructure, meaning its transaction data remains self-hosted, giving Tungsten full control of its payments data and infrastructure. 
 The implementation was a demonstration of AI-led delivery, with a four-person core delivery team. Deploying the 10x environment and building the entire API integration was completed in less than three months, using an AI agent directed by Tungsten engineers.   Olly Richards, SVP, Commercial & Strategy, 10x Banking , said: “Our technology was built for the world’s largest banks and this partnership with Tungsten Automation shows it can do far more than power traditional banks and building societies. Tungsten already owns the invoice and customer relationship, by embedding our ledger into Pay+, it can extend that into payments without becoming a bank itself. That is the promise of embedded finance, and the fact that the whole thing was deployed and integrated by AI shows how quickly it can now be done.”  Andrew Ng, Head of Payments and Embedded Finance, Tungsten Automation , said: “Finance teams trust Tungsten with their invoices, and Pay+ extends that trust to the payments that follow. Tungsten intends to lead embedded payments in invoice-to-pay, bringing automation, orchestration and reconciliation into a single flow.” 
Our ambition demands infrastructure built to the standard of the world’s largest banks, which is why we chose 10x.
 Pay+, including the 10x ledger, is expected to be generally available in the UK and US in the first quarter of 2027.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: 10x Banking partners Tungsten Automation to power Pay+ ledger
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
10x Banking (London, 4th-gen cloud core-banking vendor; founder/CEO Antony Jenkins, ex-Barclays) is providing its core transaction **ledger** as the record-keeping engine behind **Pay+**, Tungsten Automation's new embedded-payments / invoice-to-pay proposition. Tungsten is the AP-automation vendor formerly called **Kofax** (renamed 2024-01-16; PE-owned, Clearlake Capital + TA Associates since 2022), which already owns the invoice/supplier relationship via its InvoiceAgility capture + e-invoicing network.
- **What is actually new vs PR:** 10x is contributing a *ledger component*, not a full core-banking migration. The ledger records every Pay+ transaction in real time with rich metadata (provider, rail, category, charges) to enable real-time reconciliation. Tungsten remains the orchestrator; it routes each payment "through the right provider or rail across Tungsten's **network of regulated payment partners**" — i.e. 10x does NOT move money or hold the licence. → The deal's weight is a *ledger-as-component* sale into embedded finance, not a core win.
- **Self-hosted, not SaaS:** the ledger was deployed **inside Tungsten's own infrastructure** ("self-hosted," Tungsten keeps full control of payments data/infra). → This is notable: 10x's pitch is cloud-native SaaS, yet here it ships a self-managed deployment. That's a flexibility signal but also dilutes the recurring-SaaS, multi-tenant economics; unit economics of this contract are undisclosed.
- **Status = announced, NOT live.** General availability in UK + US is only **Q1 2027**. No live clients, no GMV, no volume on Pay+. The "under three months" and "four-person AI-led team" claims describe the *build/integration*, not production traction.
- **Why framed this way:** the PR anchors to "first deployment outside a regulated financial institution" and the AI-delivery angle because the raw deal (one ledger component, not yet GA) is modest. The AI-agent-built-the-integration story is the real headline hook — a proof-point for AI-led delivery speed, directed by Tungsten engineers.

## [1] Competitors / peers
- **Core-banking ledger peers:** Thought Machine (Vault — Lloyds, Standard Chartered; crossed ~USD 100M revenue Q2 2026), Mambu (N26, ABN AMRO — SaaS, lending-strong), Temenos, Finacle/Infosys, FIS, Tuum, Finxact. 10x and Thought Machine target Tier-1 enterprise transformation; 10x differentiates on polyglot runtime (no Smart Contract language lock-in like Vault). (analysis: here 10x is competing less against cores and more against generic ledger/subledger infra.)
- **Embedded-payments / ledger-as-a-service peers:** Modern Treasury, Formance, Fragment, Marqeta (issuing), Stripe Treasury, Adyen embedded, plus BaaS players (Unit, Railsr, Solaris, Treasury Prime). → Tungsten could have bought a purpose-built payments ledger (Formance/Modern Treasury) or a BaaS provider. Choosing a Tier-1 *bank-grade* core ledger is a credibility/scale play ("standard of the world's largest banks," per Tungsten). (analysis) Whether bank-grade is actually needed for AP reconciliation — vs over-engineering — is an open question.
- **Position:** For 10x this is a *lateral* move (new buyer type), not a share gain in core banking. For Tungsten it's catch-up to the broader invoice-to-pay convergence (Bill.com, Coupa, SAP Ariba, Tipalti all push AP→payment execution).

## [2] Company history / fit
- 10x founded 2016 by Antony Jenkins (ex-Barclays CEO). Clients: Westpac, Chase UK, Old Mutual, NZ Co-operative Bank. Metrics (self-reported, LTM to ~mid-2026): >10M live accounts, ARR +30% YoY, EBITDA-positive Q4 2025, 100th release (v10.0, March 2026), >10 new clients, raised **£40M from AshGrove Capital** (Aug 2026; debt-style growth capital per AshGrove's profile). ~10k TPS, 99.99% uptime (self-reported).
- **Why 10x is doing this:** structural pressure. Core-banking is a slow, lumpy, multi-year sales cycle; 10x is newly EBITDA-positive and under pressure to show growth beyond a handful of Tier-1 banks. Embedded finance / ledger-as-component is a way to expand TAM into non-bank platforms (a recurring 2026 theme — cf. [[10x Banking and audax partner to speed bank upgrades]], [[10x Banking and HassemPrag partner on core banking across Africa]]: a partnership-led channel expansion strategy). This Tungsten deal is the logical next step: sell the ledger as a standalone component, not just a full core.
- Fits the "continuous delivery / modular platform" narrative from [[10x Banking marks 100th release with version 10.0]].

## [3] Novelty / value-add / traction
- **Real novelty:** modest but genuine — first time 10x's ledger is embedded in a **non-regulated platform**, proving the ledger can be sold decoupled from a full core-banking migration. The second-order value: rich per-transaction metadata (rail/provider/category/charge) enabling real-time reconciliation — a real AP pain point ("end-of-period reconciliation backlogs"). (analysis) This is a plausible, non-trivial technical fit.
- **Traction: zero so far.** GA Q1 2027; no users, no volume, no revenue disclosed. "Under three months to integrate" is a delivery stat, not adoption.
- **Who captures the margin (analysis):** Tungsten owns the customer, the invoice data, and the orchestration; the *regulated payment partners* move the money and likely take the payment economics. 10x is a software/infra supplier paid (presumably) a licence/usage fee for the ledger. → 10x risks being the low-margin "plumbing" while Tungsten captures the embedded-finance value. Durability of 10x's revenue here depends on usage-based pricing tied to Pay+ volume — undisclosed. Self-hosted deployment further weakens 10x's lock-in vs multi-tenant SaaS.
- **The AI-delivery claim** (one AI agent + 4-person team, <3 months) is the most strategically interesting part: if real and repeatable, it slashes 10x's integration cost/time — the single biggest friction in core-banking sales. (hypothesis) If generalizable, that matters more to 10x's economics than the Tungsten contract itself.

## [4] What's next / market sentiment
- Near-term: GA UK + US Q1 2027 is the real proof point — watch for named Pay+ customers and payment volume then. Until then this is an announcement.
- Market backdrop: strong tailwind for invoice-to-pay convergence and embedded B2B payments (AP automation + payment execution merging). 10x's lateral move into embedded finance is on-trend; the risk is commoditization of the "ledger" layer (Formance/Modern Treasury/Fragment are cheaper, purpose-built).
- **Counterintuitive second-order (analysis):** success here could *reposition* 10x from "core-banking challenger to Thought Machine" to "ledger-infra supplier to any platform" — a bigger TAM but a lower-margin, more contested market where it loses its Tier-1-bank moat. The central question shifts from "can 10x win core-banking deals?" to "is 10x's ledger differentiated enough to earn a premium outside regulated banking, or does it get commoditized?"
- Risks: deal is pre-GA; self-hosted model limits recurring economics; 10x doesn't control the money movement or the customer; PE-owned Tungsten (cost-focused) may squeeze supplier pricing.

## Sources
- 10xbanking.com press release (primary, in-note): https://www.10xbanking.com/news/powers-tungsten-pay-plus-embedded-payments-platform
- thepaypers.com; ibsintelligence.com; enterprisetimes.co.uk (2026-10-16); financialit.net — deal reprints
- techtimes.com (2026-08-04, £40M/$54M AshGrove raise, EBITDA-positive, 10M accounts, ARR +30%); Fortune (2026-09); Crunchbase; Finovate — 10x background
- Wikipedia/Finovate/wirthconsulting — Tungsten=Kofax rename 2024, Clearlake+TA ownership, InvoiceAgility
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions — Importance: 3/5**

1. **Is it live or just announced?** Announced only. GA is Q1 2027 (UK + US). No live clients, volume, or revenue. "Under three months to integrate" is a build stat, not adoption. → weight capped.
2. **What did 10x actually sell — a core-banking win or a component?** A ledger *component*, not a full core migration. 10x records transactions; it does not orchestrate routing or move money. Materially smaller than a core win.
3. **Is this recurring SaaS revenue?** Unclear — and the ledger is **self-hosted inside Tungsten's infra**, which dilutes 10x's usual multi-tenant SaaS economics. Pricing undisclosed (licence vs usage-based?). Open.
4. **Who captures the margin in the stack?** Tungsten owns customer + invoice data + orchestration; regulated payment partners take payment economics; 10x is the infra supplier. 10x risks being low-margin plumbing. (analysis)
5. **Why not a purpose-built payments ledger (Formance, Modern Treasury, Fragment)?** Those are cheaper/purpose-built. Tungsten chose "bank-grade" for credibility/scale, but is bank-grade actually required for AP reconciliation, or is it over-spec marketing? Open.
6. **Does 10x have lock-in here?** Weak. Self-hosted deployment + a replaceable ledger layer = low switching cost vs a full core migration. Open.
7. **How real is the AI-led-delivery claim?** One AI agent + 4-person team, full API integration <3 months, directed by Tungsten engineers. Per primary source only; unverified independently. If real and repeatable it's more strategically important than the contract itself. (hypothesis)
8. **Is this a duplicate of a prior 10x note?** No. Prior notes cover audax, HassemPrag, Validata, v10.0, exec hires, Constantinople, Co-operative Bank — all distinct events. FRESH.
9. **How big is Tungsten / is Pay+ a credible launch?** Tungsten = ex-Kofax (renamed Jan 2024), PE-owned (Clearlake + TA Associates), established AP/e-invoicing base (InvoiceAgility network). Credible distribution, but Pay+ is a brand-new product line — execution risk.
10. **What's 10x's financial health underwriting this move?** EBITDA-positive Q4 2025, ARR +30% YoY, >10M live accounts, £40M AshGrove raise (Aug 2026). Healthy but pressured to show TAM expansion beyond Tier-1 banks. (context explains the strategic motive.)
11. **Does moving "beyond regulated banks" dilute 10x's moat?** Second-order risk: repositions 10x from Thought-Machine-class core challenger to a commoditizable ledger-infra supplier in a more contested market. (analysis)
12. **What does 10x stay silent on?** Contract value, pricing model, exclusivity, any volume commitment, whether Tungsten considered rivals. All undisclosed.
13. **What does Tungsten stay silent on?** Which regulated payment partners move the money, fraud/liability allocation, and whether Pay+ has any committed customers for Q1 2027.
14. **Is there prior art for "core ledger in a non-bank platform"?** Yes — Modern Treasury, Formance, Stripe Treasury, Fragment all do embedded ledgers. 10x's novelty is narrower: *its* Tier-1 core ledger, decoupled, in a non-regulated host. Incremental, not category-defining.
15. **What's the single thing to watch?** Q1 2027 GA: named Pay+ customers + actual payment volume. Until then, importance stays mid (announcement, pre-traction, component sale).

**Importance: 3/5** — genuinely fresh and strategically interesting (new buyer type + AI-delivery proof-point), but pre-GA, no traction, a ledger component not a core win, self-hosted with unclear/likely-thin economics, and 10x sits in a margin-weak position in the stack.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This deal straddles two markets: (1) cloud-native core banking — valued ~$12.4bn in 2025, projected ~$47.8bn by 2034 at ~16.2% CAGR (per Dataintelo, as of 2026); the broader SaaS-based core banking segment is cited at ~$14.3bn in 2026 growing ~20.7% (per Persistence Market Research) — and (2) accounts-payable / invoice-to-pay automation moving into embedded payment execution. Structure: core banking is consolidating around a handful of 4th-gen cloud-native vendors (10x, Thought Machine, Mambu) displacing legacy on-prem stacks (FIS, Temenos); barriers are high (regulatory trust, data-migration risk, multi-year switching costs). "Why now": AP automation platforms are pushing beyond approval workflows into payment execution as the next monetization layer (per Future Market Insights / MHC, 2026) — e.g. Medius launched Medius Payments in June 2025 — and 10x's own pitch is that the AI-led build cut deployment to "under three months," collapsing the integration-cost barrier that historically gated embedded-finance entrants. Second-order effect: if ledger deployment compresses from quarters to weeks, core-banking vendors can address non-bank platforms (software firms, marketplaces) at the volume end, expanding TAM beyond the finite pool of licensed banks.

**Competitive landscape.** Sector KPIs: ARR, NRR, live accounts/deployments, EBITDA margin (core-banking SaaS); for the AP side, per-invoice cost and straight-through-processing rate. Key players & basis of competition — 10x vs Thought Machine and Mambu (product depth, cloud-native architecture, reference logos), vs legacy incumbents (price/inertia). Recent in-base peer moves: Thought Machine topped $100m revenue for FY2025, up 57% ([[Thought Machine tops $100m revenue for FY2025, up 57%]]), and raised GBP 30m in Jul-2026 ([[Thought Machine secures GBP 30m funding from new investor]]); Mambu teamed with Mastercard on cross-border payments in Sep-2026 ([[Mambu teams with Mastercard on cross-border payment integration]]). 10x's own recent cadence: Validata AI data-migration partnership ([[10x Banking partners with Validata on AI data migration]]), 100th release / v10.0 ([[10x Banking marks 100th release with version 10.0]]), audax tie-up ([[10x Banking and audax partner to speed bank upgrades]]). Protagonist position: 10x is a credible top-3 cloud-native core vendor (Westpac, Chase UK references) and reached EBITDA-positive with 10m+ live accounts and ARR +30% YoY in its Aug-2026 GBP 40m raise (per Enterprise Times). This Tungsten deal is its first deployment outside a regulated FI (analysis) — a genuine new vertical, not just another bank logo. Moat: switching costs + regulatory-grade reliability (intangible trust); network effects are weak (per-client ledgers, self-hosted inside Tungsten).

**Comps & multiples.** Private names, no live market caps — qualitative comparison, distribution not computed.
- 10x Banking: last disclosed valuation ~$700m (Series C, Jun-2021) on ~$118m revenue → EV/Rev ≈ $700m / $118m = 5.9x (per multiples.vc, stale 2021 figure — treat as historical, not current). Aug-2026 GBP 40m raise (equity+debt) disclosed no valuation. [UNSOURCED] current multiple.
- Thought Machine (closest comp): >$100m revenue FY2025 (+57%); last reported unicorn-tier private valuation [UNSOURCED] current; losses still widening per [[Thought Machine lands GBP 45M funding as losses widen]] — 10x's EBITDA-positive status is the differentiator.
- Tungsten Automation (customer, not 10x comp): CEO cited $500m–$1bn revenue, ~90% recurring, low-double-digit ARR growth (per Mergermarket, Jun-2026); eyeing a 2027 exit. Backed by Clearlake/TA Associates. The $500m–$1bn range is unusually wide and self-reported — treat skeptically (a third-party tracker, GetLatka, estimates only ~$159m, a large divergence flagging unverifiable financials).
Flag: no deal economics disclosed — revenue/fee split between 10x and Tungsten, contract value, or volume commitments are all silent.

**Risk flags.**
1. Zero disclosed economics + pre-revenue timeline — Pay+ is only GA in UK/US Q1 2027, so this is an "announced," not "live/adopted," deployment; no ledger is processing production AP volume yet, and no fee split is public. Execution/adoption risk dominates.
2. Disintermediation / stack-layer capture — 10x supplies the ledger but Tungsten owns the customer, invoice relationship and the "network of regulated payment partners" that actually move money; 10x risks being a commoditized infrastructure layer whose margin is capped while Tungsten (and its rail partners) capture the payment economics.
3. Reference-concentration / novelty risk — first non-regulated-FICE deployment means no proven playbook for this vertical; the "<3 months, AI-led, 4-person team" claim is a PR differentiator that cuts both ways (fast = thin, less-battle-tested integration).

**What this changes (idea-lens).** (analysis) Thesis: embedded core-banking-as-ledger lets core vendors escape the finite bank-customer pool and sell into software/AP platforms, re-rating the TAM — but value accrues to whoever owns the end customer and the rails, not the ledger. Watch: Q1-2027 GA and whether 10x discloses a per-transaction or usage-based economic model (vs flat platform fee); if it stays flat-fee, the disintermediation risk is real. Falsifier: 10x signing 2+ more non-bank embedded-finance deals at disclosed usage-based economics within 12 months would prove the vertical and the moat.

Sources: https://dataintelo.com/report/cloud-native-core-banking-platforms-market · https://www.persistencemarketresearch.com/market-research/saas-based-core-banking-software-market.asp · https://www.futuremarketinsights.com/reports/accounts-payable-automation-market · https://www.enterprisetimes.co.uk/2026/08/04/10x-banking-secures-40m-to-power-the-ai-first-future-of-banking/ · https://multiples.vc/private-comps/10x-banking · https://ionanalytics.com/insights/mergermarket/tungsten-automation-exit-possible-in-2027-as-buyer-appetite-builds-ceo/ · https://getlatka.com/companies/tungstenautomation.com
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
