---
title: "WSJ: Companies find it nearly impossible to plan AI spending"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: s6a852fcd
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# WSJ: Companies find it nearly impossible to plan AI spending

> [!info] 2026-10-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] WSJ: Компаниям становится практически невозможно планировать расходы на ИИ

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: WSJ — "Companies find it nearly impossible to plan AI spending"
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
This is a WSJ feature/visual explainer (wsj.com/tech, ~2026-10-05 publication; re-shared by the "42 секунды" TG channel on 2026-10-22), not a deal or launch. Thesis: enterprises cannot budget AI reliably because the unit of consumption — **tokens** — is intrinsically non-deterministic.
- Core datapoint (WSJ): running the **same task twice**, token consumption can differ **by up to ~30x**. AI "behaves more like a human worker" — it takes variable numbers of steps, retries, and reasoning depth, so cost is not a fixed function of the task.
- Survey figure cited by WSJ: only **~11% of ~400 surveyed businesses** could accurately project their AI costs. (Corroborated by secondary coverage citing ~60% of enterprises reporting unpredictable AI costs and ~73% of AI projects overshooting budget; treat the exact percentages as reporter/vendor-sourced, not audited.)
- Real-world symptom (WSJ, via Uber/Meta/Microsoft/Salesforce/DoorDash execs): some firms burned an **annual AI budget in ~3 months**; bills **doubled or tripled**; enterprises now **ration token access**.
- **Why structured this way / what it reveals:** the budgeting problem is not "AI is expensive" (prices are actually falling, see [1]) — it's that cost is **decoupled from value and from the task spec**. A cheaper model asked to do something beyond its design can *run up* more tokens than an expensive one; a single agentic coding session can silently burn thousands of dollars because "the meter runs whether or not the output is useful." The second-order point: AI spend migrates from a *capex/license* mental model (predictable) to a *variable usage* model (cloud-like, but worse — because consumption is stochastic, not just elastic).

## [1] Competitors / peers (the cost drivers, and the tooling response)
Two opposing forces create the paradox WSJ describes:
- **Per-token prices are collapsing** — GPT-4-class performance fell from ~$20/M tokens (late 2022) toward ~$0.40/M (2026), roughly **10x/year**; frontier floor ~$0.20/M input (GPT-5.6 class, after OpenAI's Jul-2026 cut); frontier-tier (Claude Opus 5) ~$5/$25 per M in/out, down from Opus 4's $15/$75. Analysts expect 3–5x annual compression through 2027.
- **…yet total bills explode**, because **agentic consumption** scales token volume far faster than price falls: reasoning models + multi-step agents + retries. Meta reportedly saw a **~30x rise in agentic queries in six months**; GitHub Copilot users projected jumps from ~$29 to ~$750/mo. So the "pricing collapse" is a trap — it invites more consumption than it saves.
- **Tooling / FinOps response (the fintech angle):** [[Ramp adds AI agents to Bill Pay platform]] and Ramp's 2026 **AI Token Spend Management** — one place to see/control spend across Anthropic, OpenAI, Cursor, Gemini; reconciles invoices, tracks commitments vs utilization. Ramp reports AI token spend across its customers up **~20.7x since Jun-2025** and raised capital at a ~$44bn valuation partly on this "token spend platform" vision. Billing-side peers monetize the same volatility: [[Paid raises $21M seed for AI results-based billing platform]] (outcome-based billing for agents), [[Flexprice raises $1.5 million seed round for billing tools]] (usage-based metering of API calls/token/GPU hours; 20B+ events/mo). Microsoft Foundry's "Agent ROI" preview puts business value next to token cost.
- **+ Why the landscape is this way:** the industry is importing the **cloud-FinOps playbook** (attribution by team/feature, monthly budgets, anomaly alerts) onto a workload that is harder to forecast than cloud compute because token output is *generated*, not provisioned. Whoever owns the **invoice/attribution layer** (Ramp) vs the **metering/billing rail** (Flexprice/Paid/Stripe) captures different margin — see [2].

## [2] Company / topic fit (who this empowers)
The WSJ thesis is the demand-side rationale for a whole emerging fintech category: **AI cost management / Token-FinOps**. It fits the broader corpus arc from the AI-bubble worry ([[This Week in Fintech IMF warns of AI investment bubble]]) to the operational reality — spend is real and large, but ROI/attribution is murky. Spend-management incumbents (Ramp, Brex, Mesh — [[Mesh and Peoples Trust bring AI expense management to Canada]]) are structurally positioned: they already hold the corporate card/invoice graph, so adding AI-token visibility is an adjacency, not a new product category. 
- **+ Why they act this way:** card/spend platforms earn commodity interchange/SaaS fees and need a *software multiple*; "owning the corporate AI-spend graph" is the premium story (same logic flagged for Ramp in prior analysis — it risks being a *dashboard* not *the payer*, since the agentic-payment rails sit with Visa/Mastercard/Stripe/Coinbase — see [[Coinbase launches Payments MCP for AI agents]], [[AWS launches AgentCore Payments with Coinbase and Stripe]]).

## [3] Novelty / value-add / traction
- **What's genuinely new vs recycled:** the *framing* (token non-determinism as a budgeting problem) is now mainstream, but the underlying facts were reported through 2026 (WSJ ran an agentic-token-cost piece earlier in 2026 too). This specific article's value-add is the **quantified volatility** (~30x same-task variance; 11% can forecast). As an *event*, it is commentary, not a development.
- **Traction of the solution side (real, not announced):** Ramp's **20.7x** token-spend growth across its base and a shipped product (not a roadmap) is the strongest live signal; Flexprice's 20B events/mo and 6x quarterly revenue are vendor-reported but concrete. 
- **+ Who captures the margin:** the durable value is in **attribution + control** (recurring SaaS, sticky) rather than in reselling tokens (commoditizing fast, 10x/yr deflation). The risk that breaks the thesis: if frontier labs or hyperscalers bundle native cost-governance (Microsoft Agent ROI, provider dashboards), the independent FinOps layer gets disintermediated — value shifts back to whoever owns the model/compute.

## [4] What's next / market sentiment
- Expect continued **token-rationing**, model-routing (cheap model for easy tasks, escalate only when needed), caching, and per-team token budgets to become standard CFO practice in 2026–27.
- Sentiment is a two-sided story: deflating per-token prices (bullish on adoption) + exploding and unforecastable total spend (bearish on ROI discipline) — the same tension underlying the AI-bubble debate ([[This Week in Fintech IMF warns of AI investment bubble]]).
- **+ Counterintuitive second-order effect:** falling token prices do **not** relieve budget pressure — they *accelerate* agentic consumption (Jevons paradox), so the forecasting problem gets worse, not better, which is exactly why the FinOps/spend-management category grows regardless of the bubble outcome. For fintech, AI-cost management may be one of the few AI plays whose demand is *counter-cyclical* to an AI correction (cost scrutiny rises when ROI is questioned).

## Sources
- WSJ, "Spending on AI Is Becoming Almost Impossible for Businesses to Budget" / "AI token spending businesses" — https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a
- PYMNTS, "Businesses Finding It Harder to Predict AI Spending" (2026) — https://www.pymnts.com/news/artificial-intelligence/2026/businesses-finding-it-harder-to-predict-ai-spending/
- PYMNTS, "FinTech Finds a New Category in AI's Untracked Costs" — https://www.pymnts.com/news/artificial-intelligence/2026/fintech-finds-new-category-ai-untracked-costs/
- SiliconANGLE, "Ramp targets AI's fastest-growing cost with expanded token spend tracking" (2026-07-16) — https://siliconangle.com/2026/07/16/ramp-targets-ais-fastest-growing-cost-expanded-token-spend-tracking/
- Ramp press release, "Ramp Launches AI Token Spend Controls" — https://www.prnewswire.com/news-releases/ramp-launches-ai-token-spend-controls-302827389.html
- unite.ai, "Why Token Costs Are Breaking the CFO Budgets in 2026" — https://www.unite.ai/ai-token-costs-enterprise-budgeting-agentic-spending/
- CloudZero, "LLM API pricing comparison in 2026" — https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- Internal: [[This Week in Fintech IMF warns of AI investment bubble]], [[Ramp adds AI agents to Bill Pay platform]], [[Paid raises $21M seed for AI results-based billing platform]], [[Flexprice raises $1.5 million seed round for billing tools]], [[Mesh and Peoples Trust bring AI expense management to Canada]], [[Coinbase launches Payments MCP for AI agents]], [[AWS launches AgentCore Payments with Coinbase and Stripe]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this a new event or recycled commentary?** It is a WSJ visual explainer (~Oct 2026), re-shared by a TG channel on 2026-10-22 — not a deal/launch. WSJ ran a related agentic-token-cost piece earlier in 2026. Weight comes from the framing + quantified volatility, not novelty. **Mostly recycled thesis; not stale as a corpus duplicate (no prior note covers the same budgeting article).**

2. **Is the ~30x same-task token variance real or a cherry-picked extreme?** WSJ-sourced; plausible given retries/reasoning-depth variance, but "up to 30x" is a worst case, not a median. Median dispersion is unstated → treat as illustrative, not a planning constant. **Open (magnitude).**

3. **The "11% can forecast AI costs" stat — whose survey, what n, what methodology?** WSJ cites ~400 businesses; the sponsor/instrument isn't named in secondary coverage. Likely vendor-adjacent (cost-tooling vendors benefit from the scary number). **Open — handle with caution.**

4. **If per-token prices fell ~10x/yr, why are bills exploding?** Because agentic consumption volume outpaces price deflation (Jevons paradox). This is the real insight — the problem is *volume growth*, not unit price. **Answered.**

5. **Is "impossible to plan" overstated?** Partially. Cost is forecastable at portfolio level with routing, caching, caps and FinOps attribution; it's the *per-task, per-session* variance that's unforecastable. The headline overstates by conflating the two. **Partially overstated.**

6. **Who benefits from amplifying this narrative?** AI cost-management vendors (Ramp, Flexprice, Paid) and FinOps tooling — the "untracked cost" story is their TAM pitch. Read vendor figures (Ramp 20.7x, Flexprice 20B events) as directional, not audited. **Conflict-of-interest flagged.**

7. **Ramp's 20.7x token-spend growth — is that AI cost exploding, or just Ramp onboarding more customers?** Ambiguous; "across Ramp customers" mixes same-store growth with base expansion. Cannot isolate organic per-customer AI inflation. **Open.**

8. **Does the FinOps layer have durable margin, or get disintermediated?** Risk is real: Microsoft Foundry "Agent ROI", provider-native dashboards, and hyperscaler billing could absorb cost-governance. Independent layer's moat = cross-provider attribution + corporate spend graph. **Contested moat.**

9. **Where in the stack is the margin — metering (Flexprice), outcome billing (Paid), or attribution (Ramp)?** Different pools: Ramp owns the invoice/card graph (sticky SaaS); metering/billing rails risk commoditizing. Reselling tokens earns nothing (10x/yr deflation). **Analysis.**

10. **Is AI-cost management counter-cyclical to an AI bubble?** Hypothesis: if ROI gets questioned ([[This Week in Fintech IMF warns of AI investment bubble]]), cost scrutiny *rises*, so this category may grow even in a correction. **Hypothesis — attractive but unproven.**

11. **Can enterprises just cap spend?** They can (rationing, per-team budgets), but caps trade off capability — a hard cap can kill a useful agentic run mid-task. The control problem is value-vs-cost, not just cost. **Answered (structural trade-off).**

12. **Does cheaper ≠ cheaper hold?** Yes per WSJ: a cheaper model asked beyond its design can burn MORE tokens than an expensive one. Model routing must be task-aware, not price-first. **Answered.**

13. **Why does this matter for FINTECH specifically (vs generic IT budgeting)?** Because spend-management/card fintechs (Ramp, Brex, Mesh) already hold the corporate spend graph — AI tokens are the fastest-growing new line item, a natural adjacency and a software-multiple story on a commodity (interchange) base. **Answered.**

14. **What breaks the thesis?** (a) Provider-native cost governance bundled free; (b) agentic adoption stalls (budgets stop exploding); (c) per-token deflation eventually outruns volume growth. **Downside triggers identified.**

15. **Fresh or stale?** No existing corpus note covers this budgeting-forecast article or its thesis; closest neighbors are adjacent (bubble, Ramp agents, billing startups) but not the same story. **Fresh.**

**Importance: 3/5** — High-signal, widely-resonant thesis that cleanly motivates a real, traction-backed fintech category (AI Token-FinOps: Ramp 20.7x, shipped product; Flexprice/Paid). Capped below 4 because it is commentary/an explainer, not a new development; several headline figures are vendor/reporter-sourced and the "impossible to plan" framing overstates (portfolio-level forecasting is tractable via routing + FinOps).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** The WSJ piece is a demand-side signal: enterprises can't forecast AI bills because spend is driven by token consumption, not seats. Per FinOps Foundation's 2026 State of FinOps (via unite.ai, 2026), 73% of enterprises reported AI costs exceeded original projections; average enterprise AI budgets have grown from ~$1.2M/yr (2024) to ~$7M (2026). The paradox: blended token prices fell ~67% YoY (~$18.40 → ~$6.07 per 1M tokens, Q1'25→Q1'26, via unite.ai) yet bills rose — a Jevons-paradox effect where agentic workflows consume ~5–30x more tokens per task than 2024 prompt/response, so cheaper tokens drive higher aggregate spend (analysis). "Why now": the shift from fixed seat-based SaaS to usage-based/agentic billing (e.g. GitHub Copilot moved to token billing June 2026; reported dev bills jumping $29→$750/mo, via unite.ai) breaks the annual-budget planning model and creates demand for a new cost-control layer. Structure: a layered stack — model labs (OpenAI/Anthropic) → inference gateways/aggregators → the FinOps/cost-observability layer sits on top, capturing allocation/governance value without owning the compute.

**Competitive landscape.** Sector KPIs for the cost-observability layer: % spend under allocation/tagging, forecast accuracy vs actual, waste/idle-GPU reduction, net revenue retention as AI spend scales. The emerging "AI FinOps" vendor set: Vantage (aggregates LLM spend across OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, GCP Vertex AI; self-serve + free tier), Finout (ingests OpenAI/Anthropic/Bedrock/SageMaker/Vertex/Azure/Cursor; patented Virtual Tags allocate 100% of token/inference spend without code changes), CloudZero, Amnic; Kubecost for pod-level GPU/training cost. Incumbent cloud-FinOps set — Apptio/Cloudability, Flexera, CloudHealth (Broadcom) — is extending into AI-cost but was built for compute/SaaS, not token streams. Basis of competition: breadth of billing-source ingestion + allocation granularity (per-feature/per-customer) + forecast quality; moat is switching cost once spend is tagged across the org and the integration footprint (analysis). Adjacent: billing/metering infra itself is consolidating — Salesforce moved to acquire usage-based billing platform [[Salesforce moves to acquire usage-based billing platform M3ter]] (2026-06), and Stripe reportedly to acquire AI gateway OpenRouter for ~$7bn (via Fintech Brainfood). For finance-team-facing spend control, [[Ramp launches Applied AI Solutions for finance teams]] and Ramp's broader spend-management franchise sit adjacent but are expense-management, not inference-cost-observability (analysis).

**Comps & multiples.** No protagonist company and no deal/valuation in this note → no trading multiple to compute (no data). Internal comps for the surrounding theme: [[Fintech Brainfood the financialization of AI compute]] (2026-10, the compute-as-asset / AI data-center debt angle), [[Salesforce moves to acquire usage-based billing platform M3ter]] (2026-06, usage-based billing M&A), [[FT Cheap new model could pressure OpenAI and Anthropic]] (2026-10, price-per-token compression), [[Ramp launches Applied AI Solutions for finance teams]] (2026-06, AI in finance ops). FinOps-software market sizing is wide-dispersion and vendor-report sourced (ranging from ~$2.6bn to ~$16–17bn for 2026 depending on scope, via Straits/Fortune/Mordor/FactMR) — too divergent to treat as a reliable TAM → "no data" on a single figure; directionally double-digit CAGR. Private vendor valuations (Vantage/Finout/CloudZero) not publicly verified → [UNSOURCED].

**Risk flags.**
1. Deflation vs volume — the thesis rests on consumption outrunning price cuts. If per-token prices keep falling faster than usage grows for a given firm, the "budgeting pain" eases and willingness to pay for a cost layer softens (second-order: cost-observability TAM is contingent on sustained spend growth, not just adoption count).
2. Platform disintermediation — the control layer can be absorbed by the stack below (cloud providers' native cost tools, model labs' own usage dashboards) or the billing layer above (M3ter/Salesforce, Stripe/OpenRouter), squeezing standalone observability vendors to features rather than platforms.
3. Low switching cost / commoditization — allocation/tagging can become table-stakes; with ~10+ vendors chasing the same ingestion integrations, pricing power is thin unless a vendor owns the forecast/governance workflow finance teams act on.

**What this changes (idea-lens).** This is less a company story than a confirmation that "AI FinOps" is becoming a distinct budget line and buying center — CFO/platform-eng, not just the CIO (analysis). Falsifiable thesis: if usage-based/agentic billing keeps spreading, a cost-observability + forecast vendor reaches escape velocity (independent scale-up round or acquisition by a billing/cloud incumbent) within ~12–18 months; trigger to watch — a named AI-FinOps raise or an Apptio/Flexera/Broadcom (or Stripe/Salesforce) tuck-in acquiring token-level allocation. Thesis breaks if token-price deflation outpaces usage growth enough that AI bills become predictable again, collapsing the pain the WSJ describes.

Sources: https://www.unite.ai/ai-token-costs-enterprise-budgeting-agentic-spending/ · https://www.finout.io/blog/best-ai-cost-forecasting-platforms-top-8-in-2026 · https://www.nops.io/blog/finops-tools-for-ai/ · https://www.lighthousetechnology.ai/insights/apptio-competitors · https://straitsresearch.com/report/cloud-finops-market · https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
