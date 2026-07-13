---
title: "Linas Newsletter: deployment playbook for Claude Fable 5"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - industry/ai
  - region/global
  - type/commentary
sources:
  - https://substack.com/app-link/post
  - https://substack.com/redirect/78d7afa2-6e8a-4a3a-a68b-81711552085a
status: enriched
n_mentions: 3
channels:
  - "Linas Newsletter"
story_id: s6350171d
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Linas Newsletter: deployment playbook for Claude Fable 5

> [!info] 2026-07-03 · 3 упоминаний · 0 источника(ов) с текстом
> Каналы: Linas Newsletter

## Агрегированный текст (из дайджестов)

[Linas Newsletter] Claude Fable 5 Is Back. Here's Exactly What to Build Before the Free Window Closes ⌛

[Linas Newsletter] Claude Fable 5 is included at no extra cost on Pro, Max, Team, and select Enterprise plans through July 7, capped at 50% of weekly usage limits, after which every prompt moves to metered usage credits.

[Linas Newsletter] Below is the full deployment playbook for doing exactly that. Not how to prompt Fable 5, but what to point it at and how to turn it into real returns before the meter starts.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/app-link/post>
- <https://substack.com/redirect/78d7afa2-6e8a-4a3a-a68b-81711552085a>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Linas Newsletter — deployment playbook for Claude Fable 5
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS VERDICT: FRESH (distinct angle), but SOFT.** The underlying EVENT — Anthropic redeploying Claude Fable 5 on 2026-07-01 after the US lifted the export order on 2026-06-30, with the "free through July 7 at 50% of weekly limits, then metered credits" terms — is already covered in the corpus as [[US drops export restrictions on Anthropic's Mythos and Fable]] (2026-07-01, importance 3, published) and previewed in [[MTS Anthropic's Claude Fable 5 may return after export thaw]]. This Linas piece is NOT a re-report of that regulatory event: its distinct lens is a **"deployment playbook"** — an editorial how-to telling founders/builders/fintechs *what to point Fable 5 at* to build durable, reusable assets before the free window closes and the meter starts. That angle is not covered elsewhere in the corpus, so it is **fresh, not a duplicate**. But it is monetised newsletter commentary (a partly-paywalled prompts/workflows guide with a CTA), not a new fact or development — so marginal informational content is modest. Not marked `duplicate_of` because the primary event note carries the export-lift; this note would only be a duplicate if it merely re-reported that.

## [0] What exactly happened (de-PR'd)
- **The event this rests on (sourced):** After a **19-day suspension** (order 2026-06-12; the US Commerce Dept invoked an export-control directive after **Amazon researchers found a jailbreak** that got Fable 5 to identify software vulnerabilities and, in one case, produce exploit code — TechCrunch/CNBC), the **US lifted export controls on 2026-06-30**, and Anthropic **redeployed Fable 5 on 2026-07-01** globally on the Claude Platform, Claude.ai, Claude Code and Claude Cowork. Anthropic added a **new safety classifier** that blocks the specific jailbreak in **>99% of cases**; blocked requests are **routed to Claude Opus 4.8** rather than refused (Anthropic "Redeploying Claude Fable 5"; MarkTechPost; Hacker News).
- **The commercial terms Linas anchors to (verbatim-accurate):** Fable 5 is **included at no extra cost on Pro, Max, Team, and select Enterprise plans through 2026-07-07, capped at 50% of weekly usage limits, after which every prompt moves to metered usage credits.** API list price is **$10 / 1M input tokens, $50 / 1M output tokens** (Anthropic; VentureBeat; MarkTechPost). This matches the note's aggregated text exactly.
- **What the Linas piece actually IS:** a **"Claude Fable 5 Playbook: Prompts, Workflows, Use Cases"** (linas.substack.com/p/claude-fable-5-playbook) for a stated audience of "395k+ FinTech and AI leaders." Thesis: **most users will burn the free July 1–7 window on casual experimentation; strategic operators should instead build durable, reusable assets** that keep paying off after the meter starts. Named asset categories (from the free excerpt): (a) reusable prompting **skills/techniques**, (b) **agent scaffolds** (multi-step workflow architectures), (c) **due-diligence templates** (its only explicit fintech-flavoured item), (d) tested code and operating manuals. Companion pieces: "The Practical Guide" (8 techniques + Anthropic's prompting rules + a free installable Claude Skill) and "How to Prompt Fable 5" (Anthropic's own note that prior-model prompts are "too prescriptive" and *degrade* Fable 5 output).
- **Why structured this way / what it reveals:** the framing is **scarcity marketing** — a hard July-7 deadline + "the meter is coming" converts a routine model re-release into urgency, and the full playbook sits behind a paywall with a subscribe CTA. Fact → the free window is real → why it matters: for a heavy user the economics are genuinely lopsided (see [3]) → second order: the *durable* value is not the free tokens but the **reusable skills/scaffolds** you build during the window, which is a legitimate point dressed in growth-hack urgency. The "not how to prompt it, but what to point it at" line is the honest core; the deadline drama is the packaging.

## [1] Competitors / peers
- **The model itself vs peers (verified, not from memory):** Fable 5 is the **first "Mythos-class" model** Anthropic cleared for general use — a tier Anthropic positions **above the Opus family** (not within it). It is **state-of-the-art across benchmarks**: ~**95% SWE-bench Verified** (vs Opus 4.8 ~88.6%), **80.3% SWE-Bench Pro** (~11 pts ahead of #2), plus leads on FrontierCode Diamond, Humanity's Last Exam (64.5% w/ tools), OSWorld, GDPval, Terminal-Bench 2.1 (Anthropic; morphllm; Vellum; TrueFoundry). **Mythos 5** is the same base model with safeguards lifted (78.0% ExploitBench, 46.1% BioMysteryBench) — gated to vetted **Project Glasswing** partners; NOT self-serve. So the model is real and genuinely frontier; the *newsletter's* value-add is packaging, not the model.
- **Competing "how to use the new model" content:** this is a crowded genre — digitalapplied.com ("Fable 5 Before July 7: Six-Day Window Playbook"), and every vendor benchmark blog (Vellum, TrueFoundry, Finout, CodingFleet, DataCamp) shipped Fable 5 guides in the same week. Linas's edge is **distribution** (a large fintech-leaning list), not unique analysis. Position: **parity-to-behind** on substance vs the technical guides; **ahead on audience** for a fintech framing.
- **Substitutes for the workload:** for non-US developers who were locked out during the ban, the corpus already documented the substitute — [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]] (open-weight Chinese coding model that took the "best available" slot while Fable 5 was offline). With Fable 5 back, that "best available" window closes — the playbook's urgency is partly *because* Fable 5 has reclaimed the top slot. **Why the field looks this way:** the free window is a customer-acquisition move by Anthropic (get builders to embed Fable 5 into agent scaffolds/Claude Skills before pricing bites) — Linas's playbook is, in effect, aligned with Anthropic's funnel.

## [2] Company / actor history & fit
- Not a company story; the protagonist is the **Linas Newsletter** as messenger, on the **Anthropic Fable 5** event. Fit with the corpus arc is tight: this is the **6th+ Linas/Anthropic-export item** in ~3 weeks — [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]] (fresh, 4/5), [[Linas Newsletter EU AI sovereignty push after Anthropic export order]] (fresh, 3/5), [[Linas Newsletter JPMorgan, Goldman pull Claude from employee toolkits]] (stale, 2/5), plus the event notes [[US drops export restrictions on Anthropic's Mythos and Fable]], [[US clears Anthropic to release Mythos to 100+ companies and agencies]], [[Trump walks back calling Anthropic a national security threat]], [[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]].
- **Why the newsletter behaves this way:** the export saga has been the single most-covered AI story of the quarter, and a fintech-audience newsletter monetises it by routing a frontier-AI event back to actionable "build-this-now" content + a paywall/CTA. That is a legitimate content model, but it means each installment leans on the same shared event with declining marginal news value — the pattern the corpus already flagged on the JPMorgan/Goldman re-run.

## [3] Novelty / value-add / traction
- **Novelty of the NOTE: low.** It adds **no new dated hard fact** beyond the already-covered redeploy terms. The genuine value-add is the **framing/asset thesis**: "build reusable skills + agent scaffolds during the free window so the value outlasts July 7." That is a real, non-trivial operating insight (the durable asset is the *scaffold*, not the free tokens) — but it is advice, not news, and much of the substance is paywalled.
- **The one quantifiable hook — the free-window economics (analysis on sourced prices):** at API rates ($10 in / $50 out per 1M tok), a builder who front-loads heavy Fable-5 usage in the free week and captures the output as reusable skills/code gets frontier output effectively free vs metered credits after. For a heavy agentic-coding user this is a real, if bounded, arbitrage — which is exactly why the "build assets now" thesis has teeth. But **there is zero disclosed traction**: no numbers on how many readers acted, what got built, or any fintech deployment outcome. It is prescriptive, not evidenced.
- **Who captures the value / where it breaks:** the durable margin accrues to whoever owns the **deployment surface** (the agent/harness/Claude Skill the scaffold runs in), not to the free tokens — a point consistent with the GLM-5.2 note's "margin accrues to the deployment/agent layer, not the weights." The thesis breaks if (a) post-July-7 metered pricing is cheap enough that front-loading gains little, or (b) Anthropic's own guidance (prior-model prompts *degrade* Fable 5) means hastily-built scaffolds need re-work anyway.

## [4] What's next / market sentiment
- **Likely path:** after 2026-07-07 Fable 5 moves fully to **usage credits** on Pro/Max/Team/Enterprise; expect a wave of "what I built in the free window" follow-ups. The **new safety classifier + Opus-4.8 fallback** is the durable structural change from the saga — Anthropic can now ship a frontier model with a cyber-capability kill switch that reroutes rather than refuses, which is the template for future frontier releases under US-gov scrutiny.
- **Counterintuitive second-order:** the export saga functioned as **free marketing** — Fable 5 got weeks of headlines, then relaunched with a time-boxed free window that pulls builders to embed it before pricing bites. The suspension arguably *strengthened* Fable 5's launch adoption funnel. For fintech specifically, the concrete read-through is thin: the note's only fintech-flavoured asset is "due-diligence templates," and no financial institution deployment is cited — the fintech relevance is audience-framing, not a fintech event.
- **Risk to the narrative:** it is a **partly-paywalled promotional how-to** with a hard-deadline hook; the informational core (free through July 7, then metered; build reusable scaffolds) is fully captured above from primary sources, so the paywalled remainder is unlikely to change the weight.

## Sources
- Internal corpus: [[US drops export restrictions on Anthropic's Mythos and Fable]] (the redeploy EVENT, 2026-07-01), [[MTS Anthropic's Claude Fable 5 may return after export thaw]], [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]], [[Linas Newsletter EU AI sovereignty push after Anthropic export order]], [[Linas Newsletter JPMorgan, Goldman pull Claude from employee toolkits]], [[US clears Anthropic to release Mythos to 100+ companies and agencies]], [[Trump walks back calling Anthropic a national security threat]], [[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]], [[Asian AI startups launch Mythos-like models amid Anthropic export ban]], [[Broadridge joins Anthropic Project Glasswing for frontier AI deployment]].
- Linas Beliūnas / Linas's Newsletter: https://linas.substack.com/p/claude-fable-5-playbook · https://linas.substack.com/p/claude-fable-5-guide · https://linas.substack.com/p/prompting-claude-fable-5-guide
- Anthropic (primary, model facts): "Redeploying Claude Fable 5" — https://www.anthropic.com/news/redeploying-fable-5 · "Claude Fable 5 and Claude Mythos 5" — https://www.anthropic.com/news/claude-fable-5-mythos-5 · platform docs — https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
- External: CNBC (export lift 2026-06-30) — https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html · MarkTechPost (redeploy + classifier) — https://www.marktechpost.com/2026/07/01/anthropic-redeploys-claude-fable-5-on-july-1-after-us-export-controls-lift-adds-new-cybersecurity-classifier/ · VentureBeat (enterprise access) · The Hacker News (jailbreak-linked controls) · Al Jazeera (2026-07-01) · benchmarks: morphllm.com/claude-benchmarks, vellum.ai, truefoundry.com
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team questions (second-order)

1. **Is this a new event or commentary on a covered one?** Commentary. The Fable 5 redeploy (2026-07-01) and its "free-through-July-7 / 50% cap / then metered" terms are already covered as the EVENT in [[US drops export restrictions on Anthropic's Mythos and Fable]]. This adds a distinct **"deployment playbook"** angle not covered elsewhere → **FRESH by angle, SOFT by content.** Not `duplicate_of` (it doesn't re-report the regulatory event), but low marginal news value.

2. **Are the commercial terms accurate?** Yes — verbatim-correct vs Anthropic's primary "Redeploying Claude Fable 5": included at no extra cost on Pro/Max/Team/select Enterprise **through July 7, capped at 50% of weekly usage limits, then metered usage credits.** API list $10/1M in, $50/1M out. Confirmed.

3. **Is "Claude Fable 5" a real Anthropic model, not a codename or newsletter invention?** Real. It is the **first "Mythos-class" model cleared for general use**, positioned by Anthropic *above* the Opus family; SOTA on benchmarks (~95% SWE-bench Verified, 80.3% SWE-Bench Pro). Verified against Anthropic + multiple benchmark sources. Do not confuse with older Claude models.

4. **What was the ban actually about, and does the note's frame acknowledge it?** The 2026-06-12 order followed **Amazon researchers finding a jailbreak** that got Fable 5 to produce exploit code; the redeploy adds a **classifier blocking it >99%** and **routing blocked requests to Opus 4.8**. The Linas note anchors only to pricing/urgency, not the safety mechanics — accurate but partial.

5. **Is the "deployment playbook" genuinely fintech, or a fintech-audience framing?** Framing. The only fintech-flavoured asset named is "due-diligence templates"; the rest (prompting skills, agent scaffolds, tested code) is sector-agnostic. **No named financial-institution deployment.** Fintech relevance = audience, not event.

6. **Is the core thesis sound?** Yes, and it is the real value-add: **the durable asset is the reusable skill/agent scaffold you build during the free window, not the free tokens.** That is a legitimate operating insight (margin accrues to the deployment surface, consistent with the GLM-5.2 note), dressed in scarcity-marketing urgency.

7. **Is the free-window arbitrage economically real?** Bounded-yes (analysis on sourced prices). At $10/$50 per 1M tok, front-loading heavy agentic-coding output in the free week and capturing it as reusable code/skills is a real, if small, arbitrage for heavy users. It breaks if post-July-7 metered pricing is cheap, or if Anthropic's "prior-model prompts degrade Fable 5" guidance forces scaffold re-work.

8. **How much is paywalled, and does that change the weight?** The full playbook is behind a paywall + subscribe CTA. But the informational core (terms + the build-reusable-assets thesis) is fully recoverable from primary sources, so the paywalled remainder is unlikely to raise the weight. → caps importance.

9. **Does this duplicate the other Linas Anthropic-export notes?** No. GLM-5.2 note = a concrete substitute model; EU-sovereignty note = the European policy reaction; JPMorgan/Goldman note = bank access blocks (stale). THIS = a how-to-exploit-the-relaunch playbook. Distinct angle within the same cluster.

10. **Is Anthropic's funnel aligned with the playbook?** Yes (analysis). The free window is a customer-acquisition move — get builders to embed Fable 5 into scaffolds/Claude Skills before pricing bites. Linas's "build assets now" advice is effectively aligned with Anthropic's adoption funnel; the newsletter amplifies the vendor's growth motion.

11. **Did the ban hurt or help Fable 5's launch?** Plausibly helped (analysis, counterintuitive). Weeks of headlines + a time-boxed free relaunch created an adoption pull the model might not have had on a quiet launch. The suspension arguably strengthened the funnel.

12. **Any traction/adoption evidence in the note?** None. No numbers on readers who acted, assets built, or outcomes. Prescriptive advice, not evidenced adoption. → caps importance.

13. **Is Mythos 5 relevant here?** Only as context: same base model, safeguards lifted, **gated to Project Glasswing partners** ([[Broadridge joins Anthropic Project Glasswing for frontier AI deployment]]) — NOT self-serve, so not part of the free-window playbook. Keep distinct from Fable 5.

14. **What would make this fresher / higher-weight?** A named fintech/bank deploying Fable 5 in the window with disclosed use case and outcome; disclosed post-July-7 credit pricing; or evidence readers built durable production assets. None present.

15. **Net: how much does this change the picture?** It repackages a covered event into an actionable "build reusable scaffolds before the meter" thesis for a fintech audience — a real but modest operating insight, partly paywalled, with no new facts or traction. Low-to-mid weight.

---

**Importance: 2/5** — A **fresh-but-soft** editorial "deployment playbook" layered on an already-covered event (the 2026-07-01 Fable 5 redeploy and its free-through-July-7 / 50%-cap / then-metered terms, canonically held in [[US drops export restrictions on Anthropic's Mythos and Fable]], importance 3). Model facts check out (Fable 5 is a real, SOTA Mythos-class model above Opus; terms verbatim-accurate). The genuine value-add — "build reusable skills/agent scaffolds during the free window so value outlasts July 7" — is a legitimate operating insight, but it is monetised, partly-paywalled how-to content with a scarcity-marketing hook, no new dated fact, no disclosed traction, and only audience-level (not event-level) fintech relevance. Above a 1 (the free-window asset thesis is real and the terms are materially correct); below a 3 (no new event, no adoption evidence, promotional framing) — sits alongside the stale/soft end of this Linas Anthropic-export cluster.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: enterprise LLM adoption / model-deployment economics in financial services. Sizing: enterprise LLM API spend roughly doubled from ~$3.5bn to $8.4bn in under a year (per Menlo Ventures, via Yahoo Finance / ai-techpark, as of mid-2026); ~37% of enterprises now spend >$250k/yr and ~73% >$50k/yr on LLMs. Structure: consolidating oligopoly at the frontier-model layer (Anthropic / OpenAI / Google), with value split between the model layer and the application/deployment layer on top — the note is an artifact of the *deployment* layer, not the model layer. Barriers are capital (training compute), distribution (enterprise + coding-tool footprint), and, specific to financial services, the compliance architecture around a model — data handling, explainability, audit — which "often matters more than raw performance" (per a16z framing, via search). Why now: Anthropic overtook OpenAI in enterprise LLM share (~32% Menlo / ~40% other trackers vs OpenAI ~20–27%, Google ~21%) and its run-rate revenue jumped from ~$9bn end-2025 to a reported $47bn by mid-May 2026 (per VentureBeat / simonwillison.net), ~80% of it enterprise. The "Fable 5 free through July 7, then metered" window in the note is a live-monetization funnel: seed usage during the free tier, capture it on paid credits once the meter starts.

**Competitive landscape.** Sector KPIs for a model vendor: token pricing ($/1M in-out), enterprise revenue share, net-new large accounts (>$100k / >$1M annual), and inference gross margin (undisclosed → `[UNSOURCED]`). Key players and basis of competition: Anthropic (Claude Fable 5, Opus 4.8, Sonnet 5, Haiku 4.5) competing on frontier capability + coding/agentic workloads; OpenAI (GPT-5.x) on consumer distribution and agentic-commerce protocol; Google (Gemini) on cloud bundling. Recent dated moves already in-base: Anthropic Finance Agents / FS agent templates (2026-05), FIS × Anthropic financial-crime agent (2026-05), iCapital adopting Claude for adviser tools (2026-05), PayPal × Anthropic (2026-05), US dropping export restrictions on Mythos/Fable (2026-07). On the OpenAI side: Fiserv agentOS (2026-05), Intuit's $100M OpenAI deal (2025-11), MUFG bank build (2025-11). Protagonist position: Anthropic is *ahead* in enterprise/FS by share and by the density of named FS deployments; moat = intangibles (frontier capability + safety/compliance brand) plus switching costs once agents are wired into treasury/back-office stacks. The note itself — a third-party newsletter writing a "deployment playbook" — is evidence of an ecosystem forming around Claude, a network-effects tailwind Anthropic doesn't have to pay for.

**Comps & multiples.** Model-tier price ladder (per Anthropic pricing docs / claude-api reference, as of 2026-07):
- Claude Fable 5 (`claude-fable-5`): **$10.00 / $50.00** per 1M in/out, 1M context — the ceiling tier.
- Claude Opus 4.8 (`claude-opus-4-8`): **$5.00 / $25.00** — Fable is a **2.0x** price premium to Opus (`$10 / $5 = 2.0x` input; `$50 / $25 = 2.0x` output).
- Claude Sonnet 5 (`claude-sonnet-5`): **$3.00 / $15.00** ($2.00 / $10.00 intro through 2026-08-31) — Fable input is **~3.3x** Sonnet standard (`$10 / $3`).
- Claude Haiku 4.5 (`claude-haiku-4-5`): **$1.00 / $5.00** — Fable input is **10x** Haiku.
Rate-trend context: Opus-tier at $5/$25 is ~66.7% cheaper than Opus 4/4.1's old $15/$75, i.e. frontier per-token prices have fallen while a *new, higher* tier (Fable) was added on top — differentiation by tiering, not by cutting. Deployment-cost levers that change the effective multiple: batch API −50%, prompt caching −~90% on cached input (combinable to ~−95%). No public EV/Revenue multiple — Anthropic is private; last reported run-rate ~$47bn (mid-May 2026), valuation `[UNSOURCED]` here. Internal comps: [[Anthropic introduces Claude-powered Finance Agents for enterprises]], [[FIS and Anthropic build AI agent to fight financial crime]], [[iCapital taps Anthropic's Claude for AI adviser tools]], [[Anthropic launches AI agent templates for financial services]], [[Basware launches Governed Autonomy Framework for finance AI]], [[Airwallex launches AgentOS AI toolkit for financial workflows]].

**Risk flags.**
1. *Meter-cliff / adoption-economics risk (the note's own thesis).* The "build before the free window closes" framing means teams that wire Fable 5 into workflows during the free tier face a step-change to $10/$50 metered pricing after July 7 — the most expensive tier in the ladder. Second-order: workloads sized on free-tier assumptions can become uneconomic overnight unless re-tiered to Opus/Sonnet or optimized (caching/batch), so "deployment playbook" enthusiasm can reverse into churn.
2. *Model-layer disintermediation of the newsletter/deployment layer.* Value captured by the deployment-advice layer (what this note is) is thin and non-durable — Anthropic ships FS agent templates and Finance Agents itself (2026-05), pulling the "what to point it at" guidance in-house and capturing the margin at the model layer.
3. *Regulation / compliance concentration in FS.* In financial services the audit/explainability wrapper matters more than raw capability; a single frontier vendor now holding ~32–40% enterprise share concentrates model-risk-management exposure on one stack (cf. [[India tests financial systems against Anthropic's Mythos AI model]], and MAS/Singapore AI-risk guidance in-base).

**What this changes (idea-lens).** `(analysis)` This is a re-rating of the *deployment/enablement* layer, not the model vendor: as frontier providers ship first-party FS agents and templates, third-party "how to deploy" content commoditizes and the durable value migrates to (a) the model layer and (b) integrators wiring agents into regulated back-office stacks. Falsifiable thesis: within ~2 quarters, expect more first-party Anthropic FS tooling and *fewer* independent "playbook" intermediaries capturing standalone economics. Trigger to watch: post-July-7 Fable 5 metered-usage retention — if enterprise FS workloads stay on the $10/$50 tier rather than down-tiering to Opus/Sonnet, it confirms frontier-capability lock-in; heavy down-tiering would falsify the "Fable-first" deployment thesis.

Sources: https://finance.yahoo.com/news/enterprise-llm-spend-reaches-8-130000140.html · https://ai-techpark.com/enterprise-llm-spend-hits-8-4b-as-anthropic-tops-openai/ · https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth · https://simonwillison.net/2026/May/29/anthropic/ · https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-hits-30-billion-run-rate-as-enterprise-demand-accelerates/ · https://a16z.com/leaders-gainers-and-unexpected-winners-in-the-enterprise-ai-arms-race/ · https://www.cloudzero.com/blog/claude-api-pricing/ · https://platform.claude.com/docs/en/about-claude/pricing
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
