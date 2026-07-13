---
title: "OpenAI pays Wall Street bankers $500K to train AI"
date: 2026-07-12
retrieved: 2026-07-12
tags:
  - company/openai
  - industry/capital-markets
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://substack.com/app-link/post
status: published
n_mentions: 1
channels:
  - "Linas Newsletter"
story_id: sa9673f3f
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# OpenAI pays Wall Street bankers $500K to train AI

> [!info] 2026-07-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Linas Newsletter

## Агрегированный текст (из дайджестов)

[Linas Newsletter] Cloudflare just made every URL billable 🌐💸; OpenAI is now paying Wall Street bankers $500K to train AI, not close deals 😳🤖

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/app-link/post>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)

The newsletter one-liner ("OpenAI is now paying Wall Street bankers $500K to train AI, not close deals") compresses two distinct, real facts into one punchy claim:

1. **Project Mercury (contractors, since ~Oct 2025).** OpenAI ran a secretive contractor program — internally "Project Mercury" — enlisting **100+ former investment bankers** from JPMorgan, Morgan Stanley, Goldman Sachs, Evercore, KKR, Brookfield, Mubadala (plus some Harvard/MIT MBA candidates) to build **one Excel financial model per week** (DCFs, LBOs, restructurings, IPO pitchbooks) to industry standard, so models learn "hierarchical, error-sensitive spreadsheet reasoning." Pay: **$150/hour**, flexible/remote. Application is itself AI-driven (a ~20-min chatbot interview → modeling test). First reported by Bloomberg on **2025-10-21**.

2. **The "$500K" full-time SME role (2026).** OpenAI opened a full-time **"Subject Matter Expert, Investment Banking"** posting on its Applied AI team (San Francisco, hybrid 3 days). **Caveat on the figure (red-team):** the *publicly listed* comp is **~$185K–$205K base + equity**, requiring only **2+ years** of live deal experience. The **"$500K"** number is a **total-comp (base + equity + benefits) framing** used by some outlets/headlines, not a listed salary — so the headline is directionally true but inflates the cash figure. Treat "$500K" as **all-in comp, not base pay**.

→ **Why framed this way / what it reveals:** OpenAI is not "hiring bankers to do banking" — it is buying **labeled reasoning traces** for the highest-value, hardest-to-synthesize white-collar workflow (audited financial models). The "not to close deals" framing is the point: the labor input *is the training data*. Paying $150/hr for one gold-standard model/week is cheap relative to the RLHF value of thousands of expert-verified models in a domain where errors are catastrophic and verifiable. (Analysis) The story's real weight is **commentary/signal**, not a discrete product launch.

## [1] Competitors / peers

- **Anthropic** is the direct co-equal — and arguably ahead on *productization*: on **2026-05-05** it shipped **"Agents for Financial Services"** — 10 ready-to-run Claude agent templates (pitchbook building, earnings review, credit memos, valuation review, KYC, month-end close, statement audit), Microsoft 365 (Excel/PowerPoint) add-ins, and data connectors to **FactSet, S&P Capital IQ, MSCI, PitchBook, Morningstar, LSEG, Moody's, Daloopa**. Anthropic claims **~40% of its top-50 customers are financial institutions** (Citadel: coverage-model building; Walleye Capital: 100% of staff on Claude Code) [[Anthropic is Now Targeting Finance After Revolutionizing Coding]] (external).
- **OpenAI's own prior move:** [[OpenAI unveils Codex plugins for investment, banking and sales]] (2026-06-05, Bloomberg framed it as a "race with Anthropic") — the Mercury data is the training substrate feeding those plugins/tools.
- **Data-labeling infra:** Surge AI (Anthropic's RLHF platform), Fleet/Fleet Fellowship (ex-Anthropic/xAI), Pareto.AI — all now productizing "vetted domain-expert labelers" for finance. So the "pay experts to train the model" pattern is an **industry norm**, not an OpenAI novelty.

→ **Why the lay of the land is this way:** the generic-reasoning frontier has commoditized; the remaining moat is **vertical, error-sensitive expertise** that only sits in practitioners' heads. Whoever assembles the best expert-verified corpus + distribution into the analyst's actual tools (Excel/PowerPoint) wins. (Analysis) On distribution + adoption Anthropic currently looks **ahead**; OpenAI's Mercury is an **input**, its productization lagging visible.

## [2] Company history / fit

OpenAI has spent 2025–2026 pushing hard into finance-adjacent distribution: personal finance in ChatGPT [[OpenAI rolls out personal finance experience in ChatGPT]], Plaid bank-account connections [[OpenAI partners with Plaid to connect bank accounts in ChatGPT]], Fiserv agentOS [[Fiserv partners with OpenAI to build agentOS banking AI platform]], GPT-5.5 to Japanese/UK banks for cyber defense, and Codex plugins for banking. Mercury is the **upstream capability build** that underpins moving from "consumer finance chat" to "automating the analyst desk." It fits logically.

→ **Why OpenAI acts this way:** consumer/chat revenue is commoditizing and its IPO slipped to ~2027, behind Anthropic [[OpenAI IPO delayed to potentially 2027, behind Anthropic]]. Enterprise capital-markets automation is a high-ARPU, defensible seam that justifies a software/enterprise multiple. (Hypothesis) Building the expert-data moat now is a pre-IPO enterprise-revenue story.

## [3] Novelty / value-add / traction

- **Not novel as a technique:** "pay domain experts to generate RLHF/SFT data" is standard (Surge, Scale, Pareto). What's notable is the **target** (top-of-pyramid IB modeling) and the **scale/prestige** of the labor pool (100+ ex-BB/EB bankers).
- **Traction = training input, NOT deployed product.** There is **no evidence** of a live OpenAI tool that autonomously builds bank-grade models in production. Mercury produces *training data*; the payoff is speculative and forward-looking. Anthropic, by contrast, has **named live enterprise adopters**.
- **Constraint (connects to corpus):** even if capability lands, enterprises are entering an **"era of token rationing"** [[TechCrunch Companies ration AI budgets as token spending surges]] — heavy agentic modeling is expensive, capping near-term adoption.

→ **Who captures the margin:** OpenAI/Anthropic capture the *reasoning layer*; but incumbents that own the **proprietary data + distribution** (FactSet, S&P Capital IQ, Moody's, PitchBook, Bloomberg) are being **integrated as data sources**, not disintermediated — Anthropic connects *to* them. (Analysis) The near-term loser is the **junior analyst headcount** (80–100-hr weeks of model-building), not the data incumbents.

## [4] What's next / market sentiment

Expect: (a) OpenAI to convert Mercury data into finance-specific agents/Codex plugins to answer Anthropic; (b) banks to pilot internally over **12–18 months** (per external reporting) rather than adopt OpenAI's tool wholesale, given data-security/compliance; (c) continued erosion of the **entry-level analyst** job as the industry's "training ground." Sentiment: high narrative salience (Bloomberg/Fortune/Quartz), but **announced-capability, not adopted-product**.

→ **Counterintuitive second-order effect (analysis):** if the analyst apprenticeship pyramid is automated away, banks lose the pipeline that produces senior deal-makers — the durable human judgment layer AI still can't replace. Automating the bottom may **hollow the future top**. Also: the more OpenAI/Anthropic depend on human experts to bootstrap the model, the more it concedes the frontier model **cannot yet self-generate** bank-grade financial reasoning — a tell about current limits.

## Sources
- Bloomberg (2025-10-21): "OpenAI Looks to Replace the Drudgery of Junior Bankers' Workload" — https://www.bloomberg.com/news/articles/2025-10-21/openai-looks-to-replace-the-drudgery-of-junior-bankers-workload
- Quartz: "Inside OpenAI's plan to automate Wall Street" — https://qz.com/openai-project-mercury-automate-wall-street-investment-banking
- Fortune (2025-10-22): OpenAI coming for Wall Street's grunt workers — https://fortune.com/2025/10/22/sam-altman-openai-wall-street-junior-bankers-ai-entry-level-jobs/
- Entrepreneur: OpenAI paying ex-bankers $150/hr — https://www.entrepreneur.com/business-news/openai-is-paying-ex-investment-bankers-to-train-its-ai/498585
- OpenAI careers: "Subject Matter Expert, Investment Banking" — https://openai.com/careers/subject-matter-expert-investment-banking-san-francisco/
- Finextra: OpenAI hires Wall Street bankers to train AI — https://www.finextra.com/newsarticle/46795/openai-hires-wall-street-bankers-to-train-ai-in-financial-models
- Anthropic (2026-05-05): Agents for financial services — https://www.anthropic.com/news/finance-agents
- Fortune (2026-05-05): Anthropic deepens Wall Street push, Moody's partnership — https://fortune.com/2026/05/05/anthropic-wall-street-financial-services-agents-jamie-dimon/
- Linas Newsletter (primary trigger) — https://linas.substack.com/p/fintechpulse1098
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5 — rationale:** Real, well-corroborated development (Bloomberg-sourced) with genuine strategic signal about AI encroaching on top-of-pyramid capital-markets work and the "expert-data as moat" race with Anthropic. But it is **commentary on a training INPUT, not a launched/adopted product**; the headline "$500K" overstates the listed cash comp; and the core Project Mercury facts broke in Oct 2025, making the July 2026 newsletter mention a **re-surfacing/re-framing** rather than a new event. Signal-heavy, event-light → 3, not 4.

1. **Is the "$500K" figure accurate?** Partially. The public "Subject Matter Expert, Investment Banking" listing shows **~$185K–$205K base + equity**; "$500K" is a **total-comp (base+equity+benefits)** framing used in headlines. Directionally fair, cash figure inflated.
2. **Is this actually new (July 2026)?** No — **Project Mercury broke via Bloomberg on 2025-10-21**. The newsletter is re-surfacing the theme. The full-time SME posting is a 2026 extension of the same effort. → see freshness verdict.
3. **Is it a product or a training input?** **Training input.** No evidence of a live OpenAI tool autonomously building bank-grade models in production. Open on ship date.
4. **Who else is doing this?** Anthropic (finance agents live 2026-05-05, ahead on productization); data-labeling firms Surge, Fleet, Pareto productizing domain-expert labelers. Pattern is industry norm, not OpenAI-unique.
5. **Which incumbents are threatened?** Junior-analyst headcount (model-building grunt work) is the direct target. Data incumbents (FactSet, S&P Capital IQ, Moody's, PitchBook, Bloomberg) are being **integrated as data sources**, not disintermediated (per Anthropic's connector list).
6. **Adoption evidence for OpenAI?** None named. Anthropic has named adopters (Citadel, Walleye). Open for OpenAI.
7. **Why pay humans at all — doesn't this reveal a limit?** Yes (analysis). Frontier models still **cannot self-generate** audited bank-grade financial reasoning; needing 100+ expert humans is a tell about current capability ceilings.
8. **Unit economics of the training bet?** $150/hr × one model/week × 100+ contractors is cheap vs the enterprise ARPU upside of automating IB workflows. Rational spend. Open on ROI realization.
9. **Timeline to real bank adoption?** External reporting suggests **12–18 months** of internal pilots; compliance/data-security friction slows wholesale adoption of a third-party tool.
10. **Does token rationing cap this?** Yes — heavy agentic modeling is expensive; enterprises now ration AI budgets [[TechCrunch Companies ration AI budgets as token spending surges]]. Near-term brake on adoption.
11. **Who captures the margin in the stack?** Model layer (OpenAI/Anthropic) + data/distribution incumbents both capture value; distribution into Excel/PowerPoint (where Anthropic is investing) may be the decisive lever. Open.
12. **Second-order risk to banks?** Automating the analyst apprenticeship may hollow the pipeline that produces senior deal-makers — the human-judgment layer AI can't yet replace. (Analysis)
13. **Is OpenAI ahead or behind Anthropic here?** On visible productization + named adoption, **behind**; Mercury is an upstream input feeding [[OpenAI unveils Codex plugins for investment, banking and sales]]. Open on the internal model quality gap.
14. **Regulatory/compliance angle?** Bank-grade models carry audit/liability requirements; a black-box AI model faces heavy validation hurdles — a real adoption gate, largely unaddressed in coverage. Open.
15. **Why does this fit OpenAI's strategy now?** Consumer chat commoditizing, IPO slipped to ~2027 behind Anthropic [[OpenAI IPO delayed to potentially 2027, behind Anthropic]]; high-ARPU enterprise capital-markets automation supports a defensible pre-IPO revenue story. (Hypothesis)
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-13]] (2026-07-13).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: AI automation of capital-markets analyst work (DCF, pitchbooks, IPO/restructuring modeling) — the "grunt work" layer of investment banking. Generative AI in banking/financial services/insurance was ~$1.90bn in 2025, projected ~$18.52bn by 2034 at ~27.7% CAGR (per market-report figures via fintech.global/aiautomationglobal coverage, as of 2026; single secondary source — treat as indicative, not audited). This news is not a product launch: it is OpenAI's *data-acquisition* move — "Project Mercury," hiring 100+ ex-bankers from JPMorgan/Morgan Stanley/Goldman to write prompts and build financial models, paid ~$150/hr (the "$500K" headline is a *potential annualized total*, not a salary — de-PR: the $500K framing overstates the per-person economics) (per Bloomberg via Finextra/Fortune/Quartz, Oct 2025–2026). Why now: (1) domain-expert RLHF is the binding constraint — DCF/deal rationale can't be scraped from public data, so labeled expert traces are the moat input; (2) OpenAI is vertically integrating down into a workflow (IB analyst tasks) where specialist startups already have paying customers, i.e. it is buying training data *and* signalling entry into a monetizable vertical.

**Competitive landscape.** Sector KPIs: seats/named institutions on platform, workflow integration depth (Excel/PPT/Word/data-warehouse), and task accuracy vs. human analyst. Named specialists building the same "AI IB analyst": Rogo (flagship agent Felix — inside 35,000+ professionals at 250+ firms incl. Rothschild, Jefferies, Lazard, Moelis, Nomura), [[Model ML raises Series A for AI workflow automation]] (AI workflow automation for financial services, SF/NY/London/HK), and Hebbia (document analysis across finance & law). Basis of competition: finance-specific workflow integration + trust/accuracy, not raw model quality. Protagonist position: OpenAI is a *platform-layer entrant* — it owns the frontier model these startups build on, but has no shipped IB product here yet; Mercury is upstream (training) vs. the startups' downstream (deployed, revenue-generating). Moat `(analysis)`: OpenAI's edge is frontier-model scale + capital to buy expert labeling; the startups' moat is switching costs / embedded workflow / firm data-warehouse integration that a horizontal model doesn't automatically capture.

**Comps & multiples.** Private names — round valuations, NOT market caps; revenue undisclosed → revenue multiples = no data.
- **Rogo** — $2.0bn post-money on $160M Series D (Kleiner Perkins), Apr 2026, up from $750M post-Series C (Jan 2026); >$300M raised total. Valuation ~2.7x in ~3 months on seat traction, not disclosed revenue.
- **[[Model ML raises Series A for AI workflow automation]]** — $75M Series A (led by FT Partners), Nov 2025; valuation undisclosed → no data.
- **Hebbia** — ~$161M total funding; last post-money not confirmed here → `[UNSOURCED]`.
- **OpenAI** (protagonist scale, for context): ~$25bn annualized revenue run-rate mid-2026 (~$17bn ChatGPT subs, ~$6.5bn API, ~$1.5bn Sora/licensing); $122bn round at **$852bn** post-money (Mar 31 2026, SoftBank-led); confidential S-1 filed 2026-05-22 targeting a Sept IPO at $852bn–$1tn (per Sacra/ValueAddVC/CNBC; ir_latest.json openai.latest_result=null, older 2025-03 $40bn round on file — newer figures web-sourced). EV/Revenue at $852bn / $25bn ≈ **34x** — far above the ~0.5–20x guide, but this is a horizontal frontier-AI comp, not a fintech comp; not decision-useful for this vertical. Distribution not computed (only 1 comparable disclosed valuation for the *IB-AI* peer set: Rogo).

**Risk flags.**
1. **Disintermediation of its own customers.** By buying IB-analyst labels and eyeing the vertical, OpenAI competes with model-consumers (Rogo/Model ML/Hebbia) it also supplies — platform-vs-app tension; second-order: those startups accelerate multi-model / fine-tuning strategies to reduce OpenAI dependence.
2. **Data-acquisition ≠ product.** 100+ contractors at $150/hr yields expert traces, but IB modeling is judgment-, liability- and confidentiality-heavy; DCF hallucination or a mispriced deal rationale is a legal/reputational event, not a UX bug — adoption gate is trust, and banks are structurally slow to let a general model touch live deals.
3. **Headline/economics gap.** The "$500K to train AI" framing is a max-earnings artifact ($150/hr), not evidence of a large committed spend — signals intent, not scale of investment; weak basis for sizing the bet.

**What this changes (idea-lens).** `(analysis)` Signals the AI-IB-analyst vertical is real enough that the frontier-model owner wants to enter it directly, not just supply it — a re-rating catalyst for specialists (owning the workflow/data-integration layer, not the model, is the defensible position). Falsifiable thesis: if OpenAI ships a native IB/finance-modeling product within ~12 months, Rogo/Model ML/Hebbia valuations compress OR they pivot to model-agnostic + proprietary-data moats. What breaks it: Mercury stays purely internal training data with no shipped vertical product — then it's a capability-improvement story, not a competitive-entry story.

Sources: https://www.finextra.com/newsarticle/46795/openai-hires-wall-street-bankers-to-train-ai-in-financial-models · https://fortune.com/2025/10/22/sam-altman-openai-wall-street-junior-bankers-ai-entry-level-jobs/ · https://qz.com/openai-project-mercury-automate-wall-street-investment-banking · https://www.prnewswire.com/news-releases/rogo-raises-160m-series-d-to-scale-the-agentic-platform-for-finance-302756546.html · https://sacra.com/c/rogo/ · https://sacra.com/c/openai/ · https://www.cnbc.com/2025/03/31/openai-closes-40-billion-in-funding-the-largest-private-fundraise-in-history-softbank-chatgpt.html · https://fintech.global/2026/04/29/rogo-raises-160m-series-d-to-scale-finance-ai-platform/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No formal earnings — private company; figures below are best-available run-rate/loss data (not a reported quarter).** This story is product/strategy commentary (OpenAI's "Project Mercury" hiring ex-bankers to train AI on financial modeling), not a financial result. OpenAI files no public quarterly earnings; its own IR corpus carries no `latest_result` (only the Mar-2025 $40bn round). So there is no beat/miss to score — the numbers below are third-party/leaked figures that frame the thesis, not a print.

**Best-available figures (with growth).**
- Annualized revenue run-rate: ~$25bn by end-Feb 2026, +17% vs the ~$21.4bn run-rate exiting 2025; up from ~$3.7bn in 2024. Run-rate mix (mid-2026): ~$17bn ChatGPT subscriptions, ~$6.5bn API, ~$1.5bn Sora/licensing. Enterprise/Team seats grew fastest — from ~$1bn annualized (start-2025) to >$7bn (mid-2026). `(third-party, leaked/attributed — not audited results)`
- FY2025 (reported via FT-verified audited figures): revenue ~$13.07bn vs total costs ~$34bn → operating loss ~$20.9bn; net loss reported at ~$38.5bn. Gross margin ~33%, constrained by inference cost of ~$8.4bn in 2025. `(FT/press, not company release)`
- 2026 outlook (OpenAI's own internal projections): loss widening to ~$14bn on ~$13bn sales; inference cost rising to ~$14.1bn; projected cash burn ~$25–27bn in 2026, ~$57–63bn in 2027; cumulative burn to 2030 ~$218bn; cash-flow-positive not expected until 2030.
- Corporate: confidential draft S-1 filed with the SEC on 8 Jun 2026 (IPO leaning 2027, not 2026); prior round $40bn at [[OpenAI closes $40 billion in funding the largest private fundraise in history]]-scale valuation.

**vs expectations / prior period.** No public consensus exists (private, no guidance regime) → cannot compute a $/% variance. Directionally: revenue run-rate is accelerating (+17% in ~2 months), but losses and burn are widening faster than revenue — 2026 loss (~$14bn) roughly triples the ~$14bn figure vs prior internal plan, and gross margin (~33%) stays thin. [UNSOURCED] for any precise "expected" line — no whisper/preview to calibrate against.

**Guidance / forward.** Not given in any formal sense (private). Internal projections (leaked): sales to ~$100bn by 2029, profitability ~2030 — high-variance, self-reported, not de-risked. Management tone (via press): confident on top-line/automation narrative, quiet on the margin and burn bridge — classic de-PR gap between the growth headline and the cash story.

**Thesis-flags (why-ladder).**
1. **Project Mercury = margin-mix bet, not this story's revenue.** OpenAI is paying ex-bankers ~$150/hr (~$300K/yr full-time; the "$500K" headline is the top of the range) to hand-build IB models → *why*: it's buying proprietary financial-reasoning training data → *why it matters*: targets the highest-value knowledge-work vertical (IB/finance) where API monetization is richest → *second-order*: if it lands, it lifts the ~$6.5bn API/enterprise line (the fastest-growing segment) and pressures incumbent finance-software and junior-banker headcount.
2. **Burn is the real read, not run-rate.** Revenue +17% but 2026 cash burn ~$25–27bn and cumulative ~$218bn to 2030 → *why it matters*: the automation push (Mercury) is a cost, not near-term revenue, and every vertical land requires more inference spend → thesis hinges on whether monetization outruns compute cost, which the ~33% gross margin says it is not yet doing.
3. **S-1 filed (8 Jun 2026) reframes disclosure.** A future IPO forces these figures into audited daylight → second-order: the leaked-figure ambiguity (loss "$14bn" internal vs "$38.5bn" net reported) will have to reconcile, a risk flag for anyone underwriting the growth story.
4. **De-PR:** the news touts a bold Wall-Street-automation move; it stays silent on the fact that OpenAI itself remains deeply loss-making — automating bankers while burning more cash than any private company on record.

Sources: https://sacra.com/c/openai/ · https://futuresearch.ai/openai-revenue-forecast/ · https://fortune.com/2025/11/12/openai-cash-burn-rate-annual-losses-2028-profitable-2030-financial-documents/ · https://stateofsurveillance.org/news/openai-audited-financials-2026-ft-verified-38-billion-net-loss/ · https://www.finextra.com/newsarticle/46795/openai-hires-wall-street-bankers-to-train-ai-in-financial-models · https://qz.com/openai-project-mercury-automate-wall-street-investment-banking · consensus/variance: no data (private, no public consensus) · irdb semsearch: skipped (db absent locally).
<!-- /enrichment:earnings_review -->
