---
title: "Anthropic accuses Alibaba of stealing Claude"
date: 2026-06-22
retrieved: 2026-06-26
tags:
  - company/anthropic
  - company/alibaba
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id
  - https://substack.com/redirect/d8e71518-d8b2-40cf-bdc8-6d80947c0408
status: enriched
n_mentions: 2
channels:
  - "42 секунды"
  - "MTS"
story_id: sb0fd5237
month: 2026-06
enriched: true
importance: 4
freshness: fresh
---

# Anthropic accuses Alibaba of stealing Claude

> [!info] 2026-06-22 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды, MTS

## Агрегированный текст (из дайджестов)

[42 секунды] TechCrunch: Anthropic заявляет, что Claude может запросить документы пользователя

[MTS] Anthropic accuses Alibaba of stealing Claude. According to a letter sent by Anthropic to multiple US Senators, Alibaba created tens of thousands of fake accounts and collected tens of millions of Claude’s responses in order to distill Claude’s capabilities into its own Qwen models. Anthropic called for tighter export controls on chips and sanctions on foreign labs that engage in distillation attacks.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id>
- <https://substack.com/redirect/d8e71518-d8b2-40cf-bdc8-6d80947c0408>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Anthropic accuses Alibaba of "stealing" Claude via distillation
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
Anthropic sent a **letter dated 2026-06-10** to the **Senate Banking Committee** (Chair Tim Scott R-SC, ranking member Elizabeth Warren D-MA; also shared with White House officials) alleging that operators tied to **Alibaba / its Qwen lab** ran a large-scale **distillation** campaign against Claude. The letter became public only when **Reuters, CNBC and Bloomberg reported on it 2026-06-24/25**, each saying it *reviewed* the letter — i.e. it was **leaked/shared with reporters, not published** by Anthropic.

De-PR'd specifics:
- **Mechanism is API output-harvesting (distillation), NOT model-weight or source-code theft.** The Telegram aggregator framing "stealing Claude" overstates a **ToS/distillation dispute**. Distillation = querying Claude at industrial scale via fraudulent accounts, harvesting responses, and using them as training targets for a cheaper rival (Qwen).
- **Numbers (all from Anthropic's letter, single-source):** ~**25,000 fraudulent accounts**, **>28.8M Claude exchanges**, window **2026-04-22 → 2026-06-05**, targeting Claude's software-engineering / agentic / cyber capabilities in the frontier "Mythos Preview" model.
- **Reuters explicitly notes the figures "have not been independently verified."** The forensic basis for attributing the accounts to Alibaba is **not public** — reporters saw the letter, not the evidence.
- **Why structured this way:** The letter is a **policy instrument, not a court filing**. Anthropic is an interested party packaging an unverifiable allegation into a Senate ask (treat distillation as IP theft, "close the API loophole," sanction offending labs, keep chip export controls). The 28.8M figure is deliberately framed as **larger than DeepSeek+Moonshot+MiniMax combined** (~16M, per Anthropic's own Feb-2026 disclosure) → built to justify escalation from "ToS enforcement" to "national-security sanctions."

## [1] Competitors / peers
**Precedent — OpenAI vs DeepSeek (the central comparison):**
- Jan 2025: Microsoft/OpenAI probed a DeepSeek-linked group for exfiltrating data via OpenAI's API (fall 2024); David Sacks cited "substantial evidence" DeepSeek distilled OpenAI's models. Feb 2026: OpenAI told the House Select Committee on China that DeepSeek used "new, obfuscated methods" to free-ride.
- **Outcome: no lawsuit, no successful enforcement.** Legal experts call distillation enforcement an uphill battle (IP gray area, China jurisdiction, no ToS-distillation precedent). → This is the realistic base rate for the Alibaba case: **accusation + policy pressure, not litigation.**

**Anthropic's own enforcement track record (ToS cut-off, not courts):**
- Aug 2025: Anthropic cut off OpenAI's Claude API access for allegedly testing GPT-5 against Claude in violation of terms.
- See internal: [[Anthropic suspends 60+ Claude accounts, disrupting fintech Belo]] — Anthropic acts via **account suspension**, not law, and even suspends paying fintech customers over alleged policy violations. The lever here is the same (kill accounts), not a courtroom.

**Why the landscape is this way (analysis):** Frontier labs cannot stop API distillation technically (any served output can be harvested), and cannot easily litigate it across borders → so the only live lever is **regulatory** (export controls, sanctions). That is exactly why the dispute surfaces as a Senate letter rather than a complaint.

## [2] Company history / fit
This fits a clear 2026 Anthropic pattern of **wrapping itself in US-China national-security framing** while itself under Washington scrutiny:
- [[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]] (2026-06-19) and [[Trump walks back calling Anthropic a national security threat]] (2026-06-20) — Anthropic was simultaneously **a target** of US export/security pressure (foreign-national access curbs on its top models reported ~mid-June).
- [[JPMorgan Chase blocks Anthropic AI access for Hong Kong staff]] (2026-06-19) — US banks pulling Claude in Asia while local banks lean on Alibaba/Baidu Cloud → Anthropic is **structurally losing the Asian enterprise market** to Alibaba.
- [[This Week in Fintech Anthropic long-read on how AI trains AI]] (2026-06-17) — Anthropic publicly theorizing about AI-trains-AI / recursive self-improvement.

**Why Anthropic acts this way (analysis):** It is squeezed on two sides — regulated *as* a security risk at home, and out-competed by Alibaba in Asia. Reframing Alibaba as the *thief* and itself as the *victim* of a "distillation attack" flips the narrative and converts a commercial loss into a national-security argument for protection. The accusation is as much **positioning** as grievance.

## [3] Novelty / value-add / traction
- **Not novel as a phenomenon:** API distillation accusations are 18 months old (OpenAI-DeepSeek). What's new is **scale claimed (28.8M)** and the **explicit policy ask** to criminalize/sanction distillation and "close the API loophole."
- **Traction of the claim = thin.** Single interested-party source; numbers unverified by Reuters; **no released forensic evidence**; **no on-record detailed Alibaba rebuttal** (Reuters reports Alibaba *denies*; other outlets report "no comment"). A purported Alibaba spokesperson quote / Global Times dismissal appears only in secondary aggregators — **unconfirmed**.
- **Traction of the policy = the real story.** Senators Bill Hagerty (R-TN) and Andy Kim (D-NJ) reportedly moving a **defense-bill amendment** to sanction/blacklist entities running such campaigns. That is concrete legislative motion, regardless of whether the 28.8M number holds.
- **Who captures value (analysis):** If "API distillation = IP theft" becomes US policy, the moat shifts from *model quality* to *legal/regulatory protection of API outputs* — which advantages incumbent US labs and disadvantages Chinese fast-followers. That is the actual prize Anthropic is playing for.

## [4] What's next / market sentiment
- Watch for: (a) an **on-record Alibaba response**; (b) any **released forensic attribution evidence** (none public yet); (c) the **Hagerty/Kim amendment** progress; (d) whether BIS treats API-extracted capability the same as exported weights.
- **Regulatory backdrop:** AI Diffusion Rule (Jan 2025), H20/H200 license + revenue-share regime (2025 → formalized Jan 2026), case-by-case review of H200/MI325X (Jan 2026). The "distillation loophole" is the gap Anthropic wants closed: controls cover hardware + weights, not capability siphoned through a public API.
- **Counterintuitive second-order effect (analysis):** Anthropic is invoking national-security protection at the very moment it is *itself* restricted by BIS (foreign-national access curbs). Casting Alibaba as the adversary may **harden the very export regime that also constrains Anthropic** in Asia — protection and self-harm in one move.
- **Sentiment:** Live US-China AI-IP flashpoint; high media salience but legally inert (precedent = no enforcement). Treat as **allegation + lobbying**, not adjudicated fact.

## Top challenge/extra questions
(in challenge file)

## Sources
- CNBC, Anthropic-Alibaba distillation campaign (2026-06-24) — https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html
- TheNextWeb — https://thenextweb.com/news/anthropic-accuses-alibaba-distillation-claude-qwen
- Tom's Hardware (25k accounts / 28.8M exchanges / Apr-Jun 2026) — https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude
- Benzinga (Reuters: figures unverified; Alibaba denies) — https://www.benzinga.com/markets/tech/26/06/60088712/anthropic-accuses-alibaba-of-ai-model-theft-says-28-8-million-claude-conversations-were-harvested
- Crypto Briefing (policy ask: export controls) — https://cryptobriefing.com/anthropic-congress-ai-export-controls-alibaba/
- Bloomberg, DeepSeek/OpenAI precedent (2025-01-28/29) — https://www.bloomberg.com/news/articles/2025-01-29/microsoft-probing-if-deepseek-linked-group-improperly-obtained-openai-data
- Bloomberg, OpenAI vs DeepSeek (2026-02-12) — https://www.bloomberg.com/news/articles/2026-02-12/openai-accuses-deepseek-of-distilling-us-models-to-gain-an-edge
- Law.asia, OpenAI-DeepSeek enforcement difficulty — https://law.asia/openai-deepseek-ai-distillation/
- Anthropic ToS (Outputs not for training competing models) — https://support.claude.com/en/articles/12326764-can-i-use-my-outputs-to-train-an-ai-model
- VentureBeat, Anthropic cut off OpenAI API (Aug 2025) — https://venturebeat.com/technology/anthropic-cracks-down-on-unauthorized-claude-usage-by-third-party-harnesses
- Internal: [[Trump walks back calling Anthropic a national security threat]], [[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]], [[Anthropic suspends 60+ Claude accounts, disrupting fintech Belo]], [[JPMorgan Chase blocks Anthropic AI access for Hong Kong staff]], [[This Week in Fintech Anthropic long-read on how AI trains AI]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is it weight theft or API distillation?** ANSWERED: API output-harvesting via fraudulent accounts — NOT model-weight/source-code theft. The "stealing Claude" framing (Telegram "MTS") overstates a ToS/distillation dispute.
2. **Is the event itself real or a Telegram artifact?** ANSWERED: Real. Reuters, CNBC, Bloomberg each reviewed the letter (2026-06-24/25). Not a rumor.
3. **Are the numbers (25k accounts / 28.8M exchanges) verified?** OPEN — single-source (Anthropic's letter). Reuters explicitly states the figures "have not been independently verified." Treat as allegation.
4. **What is the forensic basis for attributing the accounts to Alibaba?** OPEN — no evidence public; reporters saw the letter, not the attribution data. Attribution = unconfirmed.
5. **Did Alibaba respond?** PARTIAL: Reuters reports Alibaba *denies*; other outlets report "no comment." A specific Alibaba/Global Times denial quote appears only in secondary aggregators → unconfirmed.
6. **What is the realistic enforcement outcome?** ANSWERED via precedent: OpenAI-DeepSeek (Jan 2025–Feb 2026) produced accusations + congressional testimony but NO lawsuit and no successful enforcement. Base rate for Alibaba = lobbying, not litigation.
7. **Why a Senate letter and not a lawsuit/ToS cut-off?** ANSWERED: Distillation is technically unstoppable (any served output is harvestable) and hard to litigate cross-border → the only live lever is regulatory (export controls/sanctions). Hence a policy instrument.
8. **What does Anthropic's own ToS actually say?** ANSWERED: "Our Terms do not allow the use of Outputs to train models that are competitive with Anthropic's own." So this is a contract-violation theory dressed as national-security theft.
9. **Is Anthropic an interested party with a non-IP motive?** ANSWERED (analysis): Yes — it is losing the Asian enterprise market to Alibaba/Baidu Cloud ([[JPMorgan Chase blocks Anthropic AI access for Hong Kong staff]]) and is itself under US export/security pressure ([[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]]). The accusation doubles as positioning.
10. **What is the actual policy prize?** ANSWERED: Reclassify "API-extracted capability" as IP theft and "close the API loophole" (controls cover hardware+weights, not API output siphoning). Hagerty (R-TN) / Kim (D-NJ) defense-bill amendment is the concrete vehicle.
11. **Does the 28.8M figure inflate the threat by design?** ANSWERED (analysis): Framed as bigger than DeepSeek+Moonshot+MiniMax combined (~16M, Anthropic's Feb-2026 numbers) → engineered to justify escalation from ToS to sanctions.
12. **Counterintuitive risk to Anthropic?** OPEN/analysis: Hardening export controls against Alibaba may reinforce the same BIS regime that restricts Anthropic's own foreign-national access — self-harm wrapped in protectionism.
13. **Is the "BIS restricted Anthropic's top models ~mid-June" twist confirmed?** OPEN — reported but not anchored to a clean primary source; medium confidence.
14. **Could Qwen have reached its capability without Claude distillation?** OPEN — no independent technical analysis shows Qwen gains are attributable to Claude outputs vs Qwen's own large-scale training. Causation unproven.
15. **What concretely changes if the claim is true vs false?** ANSWERED: Either way the legislative motion (sanctions amendment) proceeds on the *narrative*; the verified facts barely move the policy. The story's weight is in the lobbying, not the forensics.

Importance: 4/5 — Live US-China AI-IP / export-control flashpoint with concrete pending legislation (Hagerty/Kim) and a clear precedent chain (OpenAI-DeepSeek). Confirmed by three primary outlets, so the event is solid. Capped below 5 because the core technical claims (25k/28.8M, Alibaba attribution) are single-source and unverified, there is no legal action, and precedent shows distillation accusations have never been successfully enforced — this is allegation + lobbying, not adjudicated fact.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is not a fintech deal but a frontier-AI / model-IP policy flashpoint; the relevant "market" is the closed-frontier-LLM API business and the emerging legal regime around output-distillation. Size/growth: Anthropic run-rate revenue crossed ~$47bn in late May 2026, up from ~$30bn earlier in 2026 and ~$10bn FY2025; it raised a $65bn Series H at a $965bn post-money valuation (5/2026) and confidentially filed for IPO (per CNBC/TechCrunch/Fortune, as of 2026-05/06). Alibaba's Cloud Intelligence Group did US$6.19bn revenue in the Dec-2025 quarter (+36% YoY) with AI-product revenue at RMB8.97bn and eleven straight quarters of triple-digit AI growth; Qwen is one of the most-deployed open-weight families globally (per Alibaba FY2026 6-K / CIW, as of 2026). Structure: the frontier-API layer is consolidated (a handful of US labs: Anthropic, OpenAI; Chinese fast-followers: Alibaba/Qwen, DeepSeek). Entry barrier was historically compute + talent; the news is about a NEW barrier being legislated — legal protection of API outputs. **Why now:** the policy machinery already exists independently of this letter — a White House OSTP memo on "Adversarial Distillation of American AI Models" (2026-04-23) and the "Deterring American AI Model Theft Act of 2026" (introduced 2026-04-15, routing enforcement through export controls/sanctions, not civil suits) (per IAPS / Center for Data Innovation, 2026). Anthropic's letter is one input into a pre-loaded pipeline, not a standalone trigger.

**Competitive landscape.** Sector KPIs: run-rate revenue, frontier-capability lead (Stanford HAI 2026: top US model led by ~2.7% as of 3/2026 — see [[Stanford HAI 2026 AI Index shows capability outpacing governance]]), cost-per-token, and cloud attach (AI usage pulling cloud compute). Players & basis of competition: Anthropic/OpenAI compete on model quality + enterprise distribution and price-protected closed weights; Alibaba/Qwen and DeepSeek compete on cost and open weights (per Alibaba 6-K). Recent moves: OSTP memo (4/23/2026); Model Theft Act (4/15/2026); Beijing added ten US firms to its export-control list 2026-06-22 in retaliation; Hagerty(R-TN)/Kim(D-NJ) defense-bill amendment reportedly in motion (per note + Crypto Briefing). Protagonist's position: Anthropic is ahead on frontier quality but **structurally losing the Asian enterprise market** to Alibaba/Baidu Cloud (see [[JPMorgan Chase blocks Anthropic AI access for Hong Kong staff]]) and is itself under BIS scrutiny (see [[Trump walks back calling Anthropic a national security threat]]). Moat: shifting from *model quality* (eroding, 2.7% lead) toward *regulatory protection of API outputs* — an intangible, policy-conferred moat `(analysis)`.

**Comps & multiples.** Anthropic: $965bn post-money / ~$47bn run-rate revenue = **~20.5x** P/S on run-rate (private round valuation, not market cap; per CNBC/TechCrunch 5/2026). That is rich even for hyper-growth, but run-rate grew ~4.7x YoY ($10bn→$47bn), so the multiple tracks growth rather than being unsupported `(analysis)`. Alibaba (public, BABA): traded ~$130–140 in early 3/2026, >50% below ATH; Investing.com framed the valuation as "cheap" relative to its ~$56bn AI bet — i.e. the market is **discounting**, not paying up for, the Qwen/cloud story. A clean EV/Revenue or EV/EBITDA for Alibaba's AI segment vs Anthropic is not comparable (Alibaba is a diversified conglomerate; segment-level EV not isolable) → distribution not computed, qualitative comparison. Internal comps (distillation/IP-theft and the US-China AI-IP thread): [[BondIT sues JPMorgan over AI technology theft]] (2025-10, the *litigation* route — opposite of the policy route here), [[Tencent and Alibaba in talks to invest in DeepSeek above $20B]] (2026-04, Alibaba backing Chinese fast-followers), [[This Week in Fintech The cost of US tech export controls]] (2025-10), [[Anthropic launches Claude for Financial Services]] (2025-07, the enterprise revenue base being defended), [[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]]. Outlier flag: Anthropic ~20.5x P/S is at the top of the sane range but defensible on growth; Alibaba is cheap/discounted — the two are valued on opposite sides of the same US-China AI thesis.

**Risk flags.**
1. **Single-source, unverified core facts → narrative risk.** The 25k accounts / 28.8M exchanges and the Alibaba attribution are from Anthropic's own letter; Reuters states the figures "have not been independently verified" and no forensic evidence is public. Second-order: a later retraction or weak attribution would not stop the legislation (which predates the letter) but would dent Anthropic's credibility as the "victim" framing it is monetizing.
2. **Enforcement base rate is ~zero (disintermediation of the legal lever).** OpenAI-DeepSeek (Jan 2025–Feb 2026) produced accusations + testimony but no lawsuit and no successful enforcement; distillation is technically unstoppable (any served output is harvestable) and hard to litigate cross-border. The realistic outcome is lobbying, not litigation — so the "moat" Anthropic seeks depends entirely on Congress, an execution risk outside its control.
3. **Self-harm / reflexive export-control risk.** Anthropic is invoking national-security protection while itself restricted by BIS (foreign-national access curbs) and already losing Asia to Alibaba/Baidu. Hardening the export/sanction regime against Chinese labs may reinforce the same regime that constrains Anthropic in Asia, plus Beijing's 6/22 retaliatory listing shows tit-for-tat escalation that can cut both ways.

**What this changes (idea-lens).** `(analysis)` If "API-extracted capability = IP theft" becomes US statute (OSTP memo + Model Theft Act + Hagerty/Kim amendment), the frontier-AI moat re-rates from *model quality* (a 2.7% lead that keeps narrowing) to *legal/regulatory protection of API outputs* — advantaging incumbent US labs and disadvantaging Chinese fast-followers like Qwen/DeepSeek. Falsifiable thesis: watch whether BIS/Commerce treats API-siphoned capability the same as exported weights AND whether the Hagerty/Kim amendment survives into a passed defense bill. Thesis breaks if (a) no statute lands and enforcement stays at zero (the OpenAI-DeepSeek base rate), or (b) Alibaba puts a credible on-record technical rebuttal / Qwen's gains are shown attributable to its own training — collapsing the "theft" narrative into a commercial-positioning move.

Sources: https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html · https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/ · https://www.sec.gov/Archives/edgar/data/0001577552/000119312526274928/d133513dex991.pdf · https://www.investing.com/analysis/alibabas-cheap-valuation-reflects-doubt-over-its-56-billion-ai-bet-200682576 · https://www.iaps.ai/research/ai-distillation-attacks-executive-and-congressional-action-can-go-further · https://datainnovation.org/2026/06/the-united-states-needs-a-strategic-response-to-adversarial-ai-distillation/ · https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
