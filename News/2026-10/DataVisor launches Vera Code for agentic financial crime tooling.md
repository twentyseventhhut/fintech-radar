---
title: "DataVisor launches Vera Code for agentic financial crime tooling"
date: 2026-10-21
retrieved: 2026-10-21
tags:
  - company/datavisor
  - industry/fraud-risk
  - industry/ai
  - region/us
  - type/product
sources:
  - https://www.businesswire.com/news/home/20261020005356/en/DataVisor-Cuts-Financial-Crime-Solution-Deployment-from-Months-to-Days-with-Agentic-AI
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s1dfd1b9b
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# DataVisor launches Vera Code for agentic financial crime tooling

> [!info] 2026-10-21 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 5. 🇺🇸 DataVisor launches Vera Code to accelerate financial crime solution deployment with agentic AI. The tooluses AI agents to build, test and update fraud and AML programs, with human oversight. DataVisor claims up to 100 times faster deployment.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261020005356/en/DataVisor-Cuts-Financial-Crime-Solution-Deployment-from-Months-to-Days-with-Agentic-AI>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 2026-10-20, at Money20/20 USA (Breaking News stage), Santa Clara-based DataVisor launched **Vera Code**, an agentic-AI capability that builds, tests, and updates fraud and AML programs from natural-language requirements, with a human-in-the-loop. Through a conversational flow, Vera Code takes customer requirements and generates a complete solution or any component — event schemas, aggregated signals, rules, scorecards, alert queues, review workflows, and test data — then tests it before go-live and adapts it as threats/requirements evolve. DataVisor claims up to **100x faster** builds for new end-to-end solutions and up to **25x faster** updates to existing ones, citing a real-time fraud solution delivered for a Fortune 500 insurer in **four days** vs. an industry norm of 3–6 months ([businesswire via source](https://www.businesswire.com/news/home/20261020005356/en/DataVisor-Cuts-Financial-Crime-Solution-Deployment-from-Months-to-Days-with-Agentic-AI); [thepaypers](https://thepaypers.com/fraud-and-fincrime/news/datavisor-launches-vera-code-agentic-ai-for-fraud-and-aml-deployment); [globalfintechseries](https://globalfintechseries.com/finance/datavisor-cuts-financial-crime-solution-deployment-from-months-to-days-with-agentic-ai/)).

**[1] The company.** DataVisor (founded 2013 by CEO Yinglian Xie; Santa Clara, CA) is an AI-native fraud and financial-crime-prevention platform (unsupervised ML "RiskOps"/decisioning). It has raised ~$94.5M over ~6 rounds (Series D; investors incl. NEA, Brighton Park Capital). Vera Code is not a standalone debut but an extension of **Vera**, the "first conversational AI agents for financial crime prevention" that DataVisor launched 2026-04-14 — Vera is the conversational interface + execution agents across the detection→investigation→reporting lifecycle; **Vera Code** adds the "requirements → configured, verified solution" build/deploy layer, targeting time-to-value rather than runtime investigation ([helpnetsecurity Vera, Apr 2026](https://www.helpnetsecurity.com/2026/04/14/datavisor-vera/); [businesswire Vera, Apr 2026](https://www.businesswire.com/news/home/20260414155827/en/DataVisor-Launches-the-First-Conversational-AI-Agents-for-Financial-Crime-Prevention)).

**[2] Why it matters / so-what.** The binding constraint in bank fraud/AML tooling is not model accuracy but **implementation time** — standing up or re-tuning rules, scorecards, and queues historically takes months of vendor + internal engineering. Vera Code attacks that config/deployment bottleneck directly, which is DataVisor's wedge against larger platform rivals. It also moves "agentic AI" in fincrime from the hot runtime use case (agents triaging alerts / drafting SARs) toward the **solution-engineering** step — closer to no-code/low-code program building.

**[3] Competitive landscape.** Agentic fincrime tooling is crowded in 2026: [[Feedzai raises $75M at $2B+ valuation for fraud platform]] (Feedzai also won the [[ECB selects Feedzai for digital euro fraud detection]] mandate), Hawk (AML Investigative Agent — info-gathering, case summaries, SAR prep), Sardine (agentic fraud/AML investigation on one risk platform), and Unit21 (end-to-end detection→investigation agents; cites customers cutting alert volume ~72% / false positives ~57%). Most rivals target the **investigation/alert** loop; Vera Code's differentiator is the **build/configure** loop. Adjacent agentic-AI-in-finance moves: [[Broadridge invests in DeepSee for agentic post-trade AI]], [[Experian acquires KYC360 to boost fraud and financial crime solutions in the UK]] ([amlwatcher](https://amlwatcher.com/blog/top-agentic-ai-in-aml-compliance-providers/); [fintech.global Hawk](https://fintech.global/2026/03/25/hawks-ai-agent-automates-aml-investigations/)).

**[4] What to watch.** (a) Independent validation of the 100x/25x and "4 days vs. 3–6 months" claims — these are vendor-stated, single-anecdote (Fortune 500 insurer) figures; (b) named GA customers / adoption beyond pilots; (c) how regulators/model-risk-management treat AI-*generated* fraud/AML rules and scorecards (auditability, explainability of agent-built logic); (d) whether "human-in-the-loop" is genuine control or a thin review step; (e) pricing/packaging vs. Vera, and whether Vera Code is GA or preview.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / skeptical review**

1. **Is this a brand-new product or a repackage?** Partly repackage — Vera Code extends the April 2026 **Vera** launch. Vera = conversational agents across the fincrime lifecycle; Vera Code = the requirements→configured/verified-solution build layer. Genuinely new capability, same product family. (answered)
2. **Are the 100x / 25x speedup claims credible?** Unverified vendor claims. "Up to 100x" is a ceiling, not typical. No methodology, baseline, or third-party audit disclosed. Treat as marketing. (open)
3. **The "4 days vs 3–6 months, Fortune 500 insurer" proof point — how strong?** Single anonymized anecdote, no named customer, no independent confirmation. n=1. (open)
4. **Is there real revenue/customer traction?** No GA customer names, no ARR, no deal count disclosed. Launch is an announcement at Money20/20, not evidence of adoption. (open)
5. **Does AI generating fraud/AML *rules and scorecards* create model-risk/compliance exposure?** Likely — AI-authored detection logic raises auditability, explainability, and MRM-governance questions for regulated FIs; "human oversight" may be a thin gate. Material risk. (open)
6. **Is "agentic" substantive or a buzzword?** The build→test→deploy→adapt loop with execution agents is more than a chatbot, but how autonomous vs. templated is undisclosed. Partly answered.
7. **How defensible vs. Feedzai/Hawk/Sardine/Unit21?** Rivals mostly target the investigation/alert loop; DataVisor's config/deployment wedge is differentiated but copyable by well-funded peers (Feedzai ~$2B val). Moderate moat. (answered/open)
8. **Any funding/valuation signal here?** No — not a funding event; DataVisor last known at ~$94.5M total raised (Series D). (answered)
9. **Regional scope?** US-centric (Money20/20 USA, Santa Clara HQ); no stated international rollout. (answered)
10. **Does this duplicate an existing vault note?** No internal note on the April 2026 Vera launch or any prior Vera Code item. Not a duplicate. **Fresh.** (answered)
11. **Is the only source a vendor press release?** Yes — primary source is BusinessWire (DataVisor-issued); trade pickups (thepaypers, globalfintechseries) echo the PR. No independent reporting. Source quality low. (open)
12. **Could AI-built programs introduce fraud-detection blind spots?** Plausible — speed-to-deploy could trade off against adversarial robustness / coverage gaps if agent-built rules aren't stress-tested. (open)
13. **Is Vera Code GA or preview?** Not clearly stated; "launched/unveiled" at a conference stage ≠ confirmed GA. (open)
14. **Macro trend confirmation?** Yes — consistent with broad 2026 agentic-fincrime wave (Hawk, Sardine, Unit21 investigative agents; Broadridge/DeepSee post-trade). (answered)

**Importance: 2/5** — Incremental product extension (of April's Vera) from a mid-size ($94.5M-raised) vendor, announced via its own press release with unverified "up to 100x" claims and a single anecdotal proof point. Thematically on-trend (agentic fincrime tooling, config-automation angle is a fresh wrinkle) and worth a mention, but no funding, named customers, or independent validation to lift it higher.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** AML/fincrime software is a mid-single-digit-billion market growing fast: estimates for 2026 cluster at ~$3.8bn–$5.8bn (Global Growth Insights ~$3.82bn; 360 Research Reports ~$4.49bn; Knowledge Sourcing ~$5.77bn) with ~15–19% CAGR through the early 2030s (per secondary market-research firms, via vendor-report aggregators, as of 2026 — figures are directional, methodologies differ, treat as "no single authoritative TAM"). Structure: fragmented, with legacy rules-based transaction-monitoring/screening incumbents (Nice Actimize, SAS, Oracle) under attack from a wave of AI-native disruptors (Feedzai, Hawk, Sardine, Unit21, DataVisor). Value sits in model accuracy (false-positive reduction) and, increasingly, in time-to-deploy and time-to-adapt — the pain Vera Code targets. Why now: the 2025–2026 cohort has pivoted hard to "agentic" framing (Unit21 rebuilt around AI agents in Mar-2026; Sardine publicly warns on agentic-fraud failure modes; Feedzai shipped RiskFM) — the differentiation is shifting from detection quality to autonomy + deployment speed, and the announcement rode the Money20/20 USA 2026 stage.

**Competitive landscape.** Sector KPIs: detection rate / false-positive reduction, number of Tier-1 FI logos, and — the new axis DataVisor is pushing — deployment/adaptation cycle time. Players and basis of competition: Feedzai (scale + enterprise FI distribution), Hawk (Tier-1 bank AML/screening), Sardine (device intelligence + real-time risk, agentic framing), Unit21 (case-ops/analyst workflow, rebuilt around agents), DataVisor (unsupervised ML heritage, now agentic build/test tooling). DataVisor's position: a mid-size, mature player (founded 2013) using Vera Code to claim a speed moat — "up to 100x faster to build, 25x faster to update," one cited 4-day deploy vs a typical 3–6 months for a Fortune 500 insurer (vendor PR, single case, un-audited). Moat is weak-to-moderate `(analysis)`: deployment speed is copyable — rivals already ship agentic tooling — so the real switching cost remains the data/model estate, not the config agent.

**Comps & multiples.** DataVisor is private; no revenue disclosed → EV/Revenue, EV/EBITDA, P/E all "no data." Last primary round: Series D $40.2M at ~$226M post-money (Feb-2018); total raised ~$119M (per Caplight/Forge secondary-market data — secondary-market valuation marks are `[UNSOURCED]`/unreliable, not a primary round). Peer markers:
- [[Feedzai raises $75M at $2B+ valuation for fraud platform]] — $75M round, **$2.0bn+** post-money (Oct-2025). Richest comp; multiple not computable (revenue undisclosed).
- Hawk — $56M Series C (Apr-2025), **valuation undisclosed**.
- [[Sardine raises $25 million as National Bank of Canada partners on fraud]] — $25M Series C extension (May-2026), valuation undisclosed.
- [[Fintech Wrap Up Unit21 relaunches as AI risk infrastructure leader]] — rebuilt around AI agents (Mar-2026), private, no mark.
Distribution not computed (zero comparable revenue multiples). Qualitative read: Feedzai at $2bn+ is the valuation outlier of the cohort; DataVisor's ~$226M (2018) mark is ~8 years stale and almost certainly not representative today — flag as a large information gap, not a cheap/rich signal.

**Risk flags.**
1. Un-adopted / vendor-claim risk: "100x faster," "25x faster," "4 days" are single-source PR with one anonymized case; no named FI, no false-positive or precision/recall disclosure — classic "announced, not proven at scale" gap. Faster deployment of a weaker model is a liability, not an asset.
2. Commoditization / disintermediation: agentic build-and-adapt tooling is now table stakes (Unit21, Sardine, Feedzai all pushing agents) — DataVisor's speed claim is easily matched, so pricing power on "speed" alone is thin.
3. Scale / staleness gap vs Feedzai+Hawk: DataVisor's last primary mark (~$226M, 2018) and modest ~$119M raised sit far below Feedzai's $2bn+ and Hawk's fresh $56M — raising funding/competitive-intensity risk if the agentic race is capital-driven.

**What this changes (idea-lens).** Thesis `(analysis)`: fincrime tooling's competitive axis is migrating from detection accuracy to autonomy + time-to-deploy, which structurally favors AI-native vendors and pressures legacy rules-based incumbents (SAS/Actimize/Oracle) — watch for incumbent agentic launches or M&A as the catalyst. Falsifier: if named Tier-1 FIs publicly adopt Vera Code with disclosed false-positive/precision gains (not just speed), the moat thesis strengthens; absent that within ~2–3 quarters, treat Vera Code as a marketing re-brand of config tooling.

Sources: https://www.businesswire.com/news/home/20261020005356/en/DataVisor-Cuts-Financial-Crime-Solution-Deployment-from-Months-to-Days-with-Agentic-AI · https://thepaypers.com/fraud-and-fincrime/news/datavisor-launches-vera-code-agentic-ai-for-fraud-and-aml-deployment · https://www.globalgrowthinsights.com/market-reports/anti-money-laundering-aml-software-market-110697 · https://www.360researchreports.com/market-reports/anti-money-laundering-aml-software-market-206397 · https://fintech.global/2025/10/03/ai-fraud-platform-feedzai-hits-2bn-valuation · https://fintech.global/2025/04/08/hawks-ai-solutions-attract-56m-for-global-aml-efforts/ · https://www.caplight.com/company/datavisor
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
