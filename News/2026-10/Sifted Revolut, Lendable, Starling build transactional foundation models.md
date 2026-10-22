---
title: "Sifted: Revolut, Lendable, Starling build transactional foundation models"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - company/revolut
  - company/starling-bank
  - industry/ai
  - industry/banking
  - region/uk
  - type/research-report
sources:
  - https://sifted.eu/articles/transactional-foundation-models
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s7a4d2c32
month: 2026-10
enriched: true
importance: 2
freshness: stale
duplicate_of: [[Starling Bank builds AI model on UK sovereign cloud]]
---

# Sifted: Revolut, Lendable, Starling build transactional foundation models

> [!info] 2026-10-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Siftedreported that Revolut, Lendable and Starling are each building their own "transactional foundation models" trained on payments data.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://sifted.eu/articles/transactional-foundation-models>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sifted — Revolut, Lendable, Starling build transactional foundation models
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS: STALE (re-report).** This is a *This Week in Fintech* one-line retelling of a **Sifted analytical round-up** ("'The true barrier to entry is scale': Inside the new frontier of European fintech's AI arms race", Damisola Sulaiman, Sifted, **20 Oct 2026**). It carries **no new primary event**. Its two named "builds" are already in the corpus: the **Starling TFM announcement is covered in full by the published note [[Starling Bank builds AI model on UK sovereign cloud]]** (14–15 Oct 2026, importance 3, with the same 15bn-transaction figure, NVIDIA + Civo, early-2027 timeline), and **Revolut's PRAGMA** is prior art the corpus already treats as the benchmark (see that note's [1]/Market Research). The only incremental content Sifted adds is (a) naming **Lendable** as a third builder and (b) the "scale-is-the-moat" framing — neither delivered here as new, dated, quantified fact. So this is a re-framing/aggregation of already-covered material → **stale; duplicate_of [[Starling Bank builds AI model on UK sovereign cloud]]** (the live-event anchor).

## [0] What exactly happened (de-PR'd)
- A **secondary-source report**, not a company event. Sifted (20 Oct 2026) argues European fintechs are in a transactional-foundation-model (TFM) "arms race" and names **Revolut, Lendable and Starling** as the UK front-runners. The This Week in Fintech digest compressed this to "each building their own TFM trained on payments data."
- De-PR'd per builder, from corpus + web:
  - **Starling** — *announced* (14 Oct 2026) a TFM "Starling Intelligence" on >15bn anonymised transactions, NVIDIA "Transaction Foundation Model" blueprint (CUDA-X, NeMo AutoModel), hosted on **Civo** UK sovereign cloud; production **early 2027**; first use fraud detection. **Pre-production, no benchmarks.** Already fully enriched → [[Starling Bank builds AI model on UK sovereign cloud]].
  - **Revolut — PRAGMA** ("PRe-trained bAnking foundation Model"): encoder-style family 10M→1B params, ~24bn events / 26M user histories / 207bn tokens / 100+ countries, built with NVIDIA; treats transactions as part of a **multi-source sequence** (app navigation, comms, profile state) not isolated events; arXiv paper Apr 2026; published lifts +130% PR-AUC credit, ~+65% fraud recall. **The only one of the three with published evidence.**
  - **Lendable** — the *least substantiated* claim. Lendable is a UK consumer lender (plus a separate emerging-markets debt arm) whose data-science team builds proprietary underwriting models (historically CatBoost/GBDTs + neural nets; "Maestro" risk platform). **No public, dated "foundation model" announcement with numbers was found** — Sifted's inclusion of Lendable appears to be analyst framing of their in-house credit-ML, not a confirmed TFM launch. **(open / likely over-framed)**
- **Why framed this way:** Sifted needs a *trend story* ("arms race"), so it brackets three very different states — a published model (Revolut), a pre-production announcement (Starling), and ordinary in-house underwriting ML (Lendable) — under one headline. The digest then flattens all three to "building TFMs," which **overstates Lendable and erases the announced-vs-live gap**. The real, citable new event in this cluster already happened a week earlier (Starling) and is already a note.

## [1] Competitors / peers
- Direct TFM builders with *shipped/published* work: **Revolut (PRAGMA)**, **Mastercard (Large Transaction Model, LTM)**, **Stripe** (payments foundation model; cites blocking ~$112bn fraud, avg ~38% fraud-rate reduction), **Plaid** (sequential/transaction foundation model powering LendScore Arc + Plaid Protect; cites +48% income-classification, +14% loan-payment-detection, +22% bank-fee-classification). **JPMorgan / BNY** run governance/orchestration layers over external models, not TFMs.
- **NVIDIA is the common arms-dealer** — the TFM "developer blueprint" Starling (and others) use is a *productised NVIDIA offering*, so the model layer is converging, not differentiating.
- **Position of this item:** it is *commentary about* that field, not a new entrant. Among the three named, Revolut is clearly ahead (published lifts), Starling is a fast-follower (announced), Lendable is not demonstrably a TFM builder at all.
- **Why / second order:** Sifted's own thesis — "the true barrier to entry is **scale**" — is the right lens: if NVIDIA sells the blueprint to everyone, the moat collapses to proprietary data volume + distribution, which favours scaled neobanks (Revolut >> Starling >> a consumer lender like Lendable). The article thus implicitly undercuts its own "three equal builders" framing.

## [2] Company history / fit (of the *report*)
- Sifted (owned by the FT) runs recurring "AI-native or you're not getting funded" European-fintech-AI coverage; a TFM arms-race piece fits that editorial arc. Fine as journalism, but it is **tertiary** by the time it reaches a This Week in Fintech one-liner: company PR → Sifted analysis → curator digest → this note.
- Corpus fit: this sits squarely on an arc the vault already holds — [[Starling Bank builds AI model on UK sovereign cloud]], plus the broader AI-in-banking cluster (Feedzai RiskFM, Plaid AI intelligence tools, Lloyds agentic AI roles, Huawei financial AI). It adds a label ("arms race"), not a fact.

## [3] Novelty / value-add / traction
- **Novelty of THIS note: ~none.** The underlying builds (Starling, Revolut PRAGMA) are already covered; the TFM concept is prior art. The sole net-new item — Lendable as a TFM builder — is unverified and likely an over-reading of standard credit-ML.
- **Traction:** only Revolut shows published numbers; Starling is pre-production; Lendable shows nothing TFM-specific. A trend headline that averages these three hides that two of the three have zero demonstrated TFM traction.
- **Who captures the margin:** NVIDIA (blueprint + GPUs) and the most data-rich player (Revolut among these). A Sifted round-up captures *attention*, not economics — and for the vault it is duplicative of a richer, event-anchored note.

## [4] What's next / market sentiment
- Watch (tracked already in the Starling note): a **2027 Starling production milestone with published lift**; whether Lendable ever ships an actual TFM with numbers (the falsifiable test of Sifted's framing); whether Plaid/Mastercard/Stripe network-scale TFMs out-compete single-bank models on the "scale is the moat" logic.
- Sentiment: TFM is a genuine 2026 banking theme, but trade press treats single-bank builds as "claims" pending benchmarks. **Second-order:** convergence on NVIDIA's blueprint means "we built a TFM" is becoming table-stakes marketing; the signal shifts to *published downstream uplift* and *data scale*, which is exactly why a generic "three fintechs are building TFMs" report carries little incremental weight once the flagship (Starling) is already enriched.

## Sources
- Sifted report (primary for this note): https://sifted.eu/articles/transactional-foundation-models ("The true barrier to entry is scale", Damisola Sulaiman, 20 Oct 2026)
- Corpus duplicate/anchor: [[Starling Bank builds AI model on UK sovereign cloud]] (14–15 Oct 2026)
- Revolut PRAGMA: https://www.nvidia.com/en-us/case-studies/revolut/ ; arXiv Apr 2026
- NVIDIA TFM blueprint: https://developer.nvidia.com/blog/build-your-own-transaction-foundation-model-for-financial-intelligence/ ; https://blogs.nvidia.com/blog/financial-institutions-transaction-foundation-models/
- Stripe / Plaid TFM figures: https://cfotech.in/story/plaid-unveils-foundation-model-for-transaction-data ; https://www.openbankingexpo.com/news/plaid-unveils-new-ai-models-to-improve-lending-decisions-and-reduce-payment-risk/
- Lendable data science (context, not a TFM announcement): https://careers.lendable.com/blog/articles/datascience-at-lendable
- Thoughtworks "TFM unified intelligence layer for payments": https://www.thoughtworks.com/insights/articles/power-of-transaction-foundation-models-building-the-unified-intelligence-layer-for-payments
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is this a new event or a re-report?** Re-report. It is a This Week in Fintech one-liner summarising a **Sifted analysis** (20 Oct 2026). No company action originates here. **(answered — stale)**
2. **Duplicate of a prior note?** Yes — the only live, dated event in the cluster (Starling's TFM) is already published and fully enriched as [[Starling Bank builds AI model on UK sovereign cloud]] (14–15 Oct 2026). **duplicate_of that note.** **(answered)**
3. **Does Sifted add any new primary fact vs the Starling note?** Only the *label* ("arms race" / "scale is the moat") and naming **Lendable**. No new numbers, dates, or shipped capability. **(answered — negligible)**
4. **Is Lendable actually building a TFM?** Not verifiably. Lendable runs in-house underwriting ML (CatBoost/GBDT/NN, "Maestro"); no public dated TFM announcement with numbers was found. Sifted's inclusion looks like framing. **(open — likely over-stated)**
5. **Announced vs live for each named builder?** Revolut = published (PRAGMA, arXiv, lifts); Starling = announced/pre-production (early 2027); Lendable = no TFM shipped. The digest flattens all three to "building." **(answered)**
6. **Whose numbers are real?** Only Revolut's (+130% PR-AUC credit, ~+65% fraud recall). Starling: none. Lendable: none TFM-specific. **(answered)**
7. **What is a "transactional foundation model"?** A model pre-trained on large volumes of transaction/event sequences to learn the "language of money movement," reusable across fraud, credit, personalisation, recommendation. **(answered)**
8. **Prior art?** Mastercard LTM, Stripe (payments FM, ~$112bn fraud blocked, ~38% fraud-rate cut), Plaid (sequential FM; +48% income class., +14% loan-payment detect., +22% fee class.), NVIDIA blueprint supplying all. **(answered)**
9. **Who captures the margin?** NVIDIA (blueprint + GPUs) and the most data-rich bank. A press round-up captures attention, not economics. **(answered)**
10. **Does the "scale is the moat" thesis hold?** Yes and it undercuts the article's own framing — if the model layer converges on NVIDIA's blueprint, data scale decides, which ranks Revolut >> Starling >> Lendable, not "three equals." **(analysis)**
11. **Is there any UK/region novelty here not in the Starling note?** No — the sovereign-cloud/Civo angle and policy backdrop are already captured in the Starling note's enrichment. **(answered)**
12. **Could this be kept as a standalone "trend" note?** Weak case: it is tertiary (PR → Sifted → curator) and duplicative. The flagship event is better served by the existing enriched note. **(answered — drop)**
13. **What would make it fresh?** A genuinely new, dated, quantified Lendable TFM launch, or a Sifted-exclusive datum not in the Starling note (e.g., Revolut/Lendable production metrics). Not present. **(answered)**
14. **Any risk of under-rating a real theme?** The TFM theme is real and important — but it is already represented in the corpus by a richer, event-anchored note; this item's marginal information is near zero. **(answered)**
15. **Second-order signal?** "We built a TFM" is becoming table-stakes marketing on a shared NVIDIA stack; the durable signal is published downstream uplift + data scale, neither of which this report supplies. **(analysis)**

Importance: 2/5 — A secondary Sifted trend round-up with no new primary event; the only live build it names (Starling) is already published and fully enriched ([[Starling Bank builds AI model on UK sovereign cloud]]), Revolut PRAGMA is established prior art, and the third name (Lendable) is an unverified over-reading of ordinary credit-ML. Stale / duplicate. The underlying theme matters, but this specific item adds a label, not information.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** "Transactional foundation models" (TFMs) — transformer models that treat a payment/transaction as a token and a customer's event-stream as the context window, trained self-supervised on billions of raw transactions — are emerging as a distinct AI sub-vertical inside banking/payments, separate from text LLMs. Stripe set the template: it shipped a payments foundation model in May 2025 trained on "tens of billions" of transactions, lifting card-testing fraud detection for large merchants from 59% to 97% (per Stripe/AI-Street, via ai-street.co, as of 2025-05). Starling's own project (the sibling in-base note) is a TFM trained on ~15bn anonymised transactions on Civo's UK sovereign cloud with Nvidia, production targeted early-2027, first use fraud then its "Starling Assistant" agent (per Computer Weekly / futureofbanking.info, 2026-10). Structure: this is a scale game, not a licence game — the barrier is proprietary, labelled-by-reality transaction history + GPU capex, which favours incumbents with large, long-tenured customer bases. "Why now": (1) transformer self-supervision now extracts signal from raw event sequences without hand-labelling; (2) sovereign-cloud + Nvidia availability lowers the infra hurdle for a single bank; (3) competitive pressure after Stripe and Plaid (LendScore Arc transformer credit model, in-base) demonstrated step-changes in fraud/credit accuracy.

**Competitive landscape.** Sector KPIs for this layer: fraud-detection precision/recall, false-decline recovery ($ saved), model-driven lending loss rates, and — upstream — the raw asset, transaction count and customer tenure. Players: payments rails (Stripe — live since 2025) and data networks (Plaid — LendScore Arc, in-base) building horizontally across many merchants/banks; versus single-institution builders (Revolut, Starling, Lendable per Sifted) building vertically on their own book. Basis of competition = data scale + vertical integration of the model into product (fraud, underwriting, assistant). Protagonists' position: catching up to Stripe/Plaid on the TFM concept but each sits on genuinely large proprietary datasets — Revolut reports ~68.3M retail customers and £1.3tn FY2025 transaction volume (per CNBC/FintechFutures, 2026-03); Starling 6.2M accounts and the cited 15bn transactions. Moat (analysis): proprietary transaction data + switching costs of a primary account — strong for Revolut/Starling, thinner for Lendable (lending-only, narrower event stream).

**Comps & multiples.** No market-cap/EV for these private names, so trading multiples = no data; use scale/funding context instead. External reported figures: Revolut FY2025 revenue £4.5bn (+46%), pre-tax profit £1.7bn (+57%), ~68.3M retail customers, £1.3tn volume; a $13bn five-year investment plan (per CNBC/FintechFutures/Revolut AR2025, 2026-03/04, https://assets.revolut.com/pdf/annualreport2025.pdf). Starling FY2026 (y/e Mar) revenue £887.4m (−6% on £940.0m, rate-driven), PBT £217.1m, ROCE 34.6%, 6.2M accounts, >£500m capital surplus (per Starling release / Bloomberg, 2026-05, https://www.starlingbank.com/news/starling-delivers-fifth-year-of-profitability-and-accelerates-global-growth-strategy/). Read-through: both are solidly profitable and cash-generative — they can self-fund a TFM from operating profit without a raise, which is the key "can they afford it" test; Revolut's £1.7bn profit and $13bn plan dwarf any single-model GPU bill, Starling's £217m PBT is ample for a sovereign-cloud pilot. Internal comps (grep fallback; semsearch 402-down): [[Starling Bank builds AI model on UK sovereign cloud]] (the same TFM project, de-duplicate at digest stage), [[Plaid unveils LendScore Arc transformer credit model]], [[Linas Newsletter Plaid's AI sees what no single bank can]], [[Revolut aims to become global tech company beyond finance]]. Distribution not computed — qualitative only.

**Risk flags.**
1. Concept-vs-production gap (execution). Starling/Revolut/Lendable TFMs are largely announced/in-training — Starling's is a pilot to early-2027; the only proven live TFM is Stripe's. Risk that single-bank datasets (even 15bn txns) underperform a network model spanning many institutions on rare-fraud recall.
2. Horizontal disintermediation. Stripe (rails) and Plaid (data network) see cross-institution patterns no single bank can (see in-base Plaid note); a single-book model may be structurally blind to cross-bank fraud rings, so banks may still have to buy network intelligence — margin/value captured upstream.
3. Data-moat is narrower for Lendable. A monoline lender's event stream is thin vs a primary-account bank's; its TFM may generalise worse. Also model/AI governance: sovereign-cloud framing (Starling/Civo) signals regulators will scrutinise transaction-data training for privacy/consent — a compliance drag not yet priced.

**What this changes (idea-lens).** (analysis) This is the opening of a data-scale arms race in European fintech where the asset isn't the model but proprietary transaction volume — re-rating potential for whoever converts data into measurably lower fraud/credit losses. Falsifiable thesis: by end-2027 at least one of Revolut/Starling publishes a quantified fraud or false-decline improvement comparable to Stripe's 59%→97%; trigger to watch = Starling's early-2027 production deployment and any disclosed fraud-loss delta. What breaks it: if single-bank TFMs fail to beat bought network models and these three quietly revert to vendor AI, the "build" thesis is wrong.

Sources: https://sifted.eu/articles/transactional-foundation-models · https://www.computerweekly.com/news/366651839/Starling-Bank-claims-first-banking-AI-trained-on-UK-sovereign-cloud · https://www.ai-street.co/p/stripe-built-a-payments-llm-to-fight-fraud · https://www.cnbc.com/2026/03/24/revolut-2025-earnings-record-profit.html · https://www.starlingbank.com/news/starling-delivers-fifth-year-of-profitability-and-accelerates-global-growth-strategy/ · https://assets.revolut.com/pdf/annualreport2025.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Earnings angle — can neobank profitability fund sustained AI/compute investment?** This story (Sifted) is about Revolut, Lendable and Starling building transactional foundation models; the question for the thesis is whether these firms throw off enough profit to self-fund the compute and data-engineering such models require. The two IR-covered names here both do — but at very different scales.

**Revolut — FY2025 (year ended 31 December 2025), from Revolut Group Holdings annual report filed 2026-04-29:**
- Revenue: **£4.5bn (€5.2bn), +46% YoY** (from £3.1bn in FY2024).
- Pre-tax profit: **£1.7bn (€2bn), +57% YoY** (vs £1.1bn FY2024) — a **38% pre-tax margin**.
- Retail customers: **68.3m, +30% YoY**; business customers **767,000, +33% YoY**.
- Total customer balances: **£50.2bn, +66% YoY**.
- Source (filing): https://assets.revolut.com/pdf/annualreport2025.pdf

**Starling (Starling Group) — FY2026 (year ended 31 March 2026), from FY2026 results announcement 2026-05-21:**
- Revenue: **£887.4m, down from £940.0m in FY2025** (decline attributed to the softening interest-rate environment).
- Pre-tax profit: **£217.1m (FY2025: £223.4m)** — its fifth consecutive year of profitability; pre-tax return on capital employed **34.6%**.
- Platform accounts: **6.2m, +0.9m YoY** (from 5.3m); customer deposits **£12.7bn** (from £12.1bn); ARPAU **£275**.
- Notably Starling already monetises its own tech: "Engine by Starling" SaaS revenue **+25% YoY**, client base doubled, with £70m of committed ARR; and it has shipped AI features (Spending Intelligence, Scam Intelligence, and the "Starling Assistant," billed as the first agentic AI financial assistant from a UK bank).
- Source (release): https://www.starlingbank.com/news/starling-delivers-fifth-year-of-profitability-and-accelerates-global-growth-strategy/
- Source (annual report): https://www.starlingbank.com/docs/annual-reports/Starling-Group-Annual-Report-2026.pdf

**Read-through for the AI thesis:**
- **Supportive:** Both are solidly, recurringly profitable, so AI/compute spend is funded from operating cash rather than fresh raises. Revolut's £1.7bn pre-tax profit and 68m-customer transaction stream give it both the budget and the proprietary data volume a "transactional foundation model" needs — by far the strongest position of the two. Starling is a proven builder/seller of banking tech (Engine) and already has agentic AI shipped, so model investment extends an existing, monetised capability rather than being a speculative bet.
- **Caution flags:** Starling's top line and pre-tax profit both *declined* YoY (rate-driven), so its AI budget is being carved out of a flat-to-shrinking P&L — less headroom than Revolut. Lendable, the third name in the story, is not IR-covered here, so no filings-grounded profitability read is available for it. Treat any claim that all three can equally sustain heavy compute spend with care: on filed numbers, Revolut's scale (~5x Starling's revenue, ~8x its pre-tax profit, and a far larger transaction dataset) is in a different league for training foundation models.
<!-- /enrichment:earnings_review -->
