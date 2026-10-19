---
title: "Sber adds BPMN generation to Giga Agentic RPA platform"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/sber
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.sberbank.ru/ru/sberpress/all/article
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sd2d1decb
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Sber adds BPMN generation to Giga Agentic RPA platform

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Добавил в платформу Giga Agentic RPA функцию, которая по текстовому описанию формирует BPMN-схемы бизнес-процессов с использованием программных роботов, AI-агентов и модулей распознавания документов

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.sberbank.ru/ru/sberpress/all/article>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sber adds BPMN generation to Giga Agentic RPA platform
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On **2026-10-16**, at Sber's internal **GigaConf** engineering conference (Moscow HQ), Sber added a **"Prompt → Process"** feature to its existing **Giga Agentic RPA (GigaARPA)** platform. The feature turns a **plain-text description** of a business process into a **BPMN schema draft** that wires together software robots (RPA), GigaChat-based AI agents and an IDP (intelligent document processing / document-recognition) module.
- Mechanism (per vendor): user enters a prompt → built-in AI agents split it into semantic blocks → a GigaCode-based code-gen model structures them → the platform's compiler emits a **BPMN template**. Claimed effect: idea-to-first-prototype compressed "from weeks to hours."
- **This is a feature release on a year-old platform, not a new product.** GigaARPA is the rebrand/next generation of Sber's older **SaluteRPA**, unveiled at **AI Journey on 2025-11-20**; the same month it got ecosystem integrations with Digital Q platforms (via SberService / Diasoft). So the news is the next incremental capability on an established stack.
- **Target user / PR frame:** pitched at "business analysts and process owners with minimal IT involvement." The honest read: it generates a **draft/template**, not a production-ready, deployed process — a human still validates, connects systems and hardens it. "From weeks to hours" is a vendor claim about prototyping, not end-to-end delivery.
- **Why framed this way:** Sber is monetizing the GigaChat/GigaCode stack by pushing it into every internal tool (RPA, dev env, analyst agents) and productizing them for external corporate clients. Text-to-BPMN is the current industry "agentic automation" marketing hook, so Sber is matching the category narrative rather than opening a new one.
Related internal corpus items (same Sber AI-productization wave, same day/month): [[Sber unveils free GigaPlatform AI Studio for building AI agents]], [[SberBusiness launches AI agent for small-business cashback selection]], [[Sber teaches AIFA financial analyst to self-plan analysis]], [[Sber fully automates bank guarantees for Federal Customs Service]].

## [1] Competitors / peers
- **UiPath** — ahead. UiPath **Autopilot** already turns natural-language descriptions into **BPMN** process models inside **UiPath Maestro** (BPMN-based agentic orchestration), GA within its 2025.10 / 2026 agentic stack (Maestro Flow/Case, Agent Builder, IXP, ScreenPlay). ~$1.85B ARR scale.
- **Automation Anywhere** — comparable. Added AI agents + "AI + Automation Enterprise System" (mid-2024), acquired **Aisera** (Nov 2025) for agentic depth.
- **Microsoft Power Automate / Blue Prism / ABBYY / Kofax(Tungsten)** — broad RPA incumbents, several with gen-AI copilots.
- **Academic baseline:** multi-stage LLM text→BPMN generation is an active research area (e.g. arXiv work), i.e. the underlying technique is not proprietary novelty.
- **Position: catching up / parity inside Russia.** Globally Sber is a fast follower of UiPath's Autopilot-in-Maestro pattern. **Why the lay of the land is this way:** post-2022 sanctions removed UiPath/Automation Anywhere/Microsoft from the Russian market, so Sber's real competitive frame is **domestic import-substitution** (vs. Russian RPA vendors like PIX Robotics, Primo RPA, Sber's own legacy SaluteRPA) rather than global leaders. The second-order point: Sber's moat here is **distribution + a captive GigaChat stack inside Russia**, not technical lead.

## [2] Company history / fit
- Trajectory: **SaluteRPA → GigaARPA** (AI Journey, 2025-11-20) → Digital Q integrations (2025-11) → **Prompt→Process / text-to-BPMN** (2026-10-16). Consistent, logical roadmap: add GigaChat agents, then lower the authoring barrier.
- Scale/traction anchors (vendor-stated): Sber's automation systems run **~400,000 operations/day**; Sber claims **99.4% of its operations center automated**. IDP module stated throughput ~**20 documents/minute**.
- **Fit: high and structurally driven.** Sber is simultaneously an AI model owner (GigaChat/GigaCode), a cloud/dev-tools vendor and a giant bank with its own vast process-automation needs. Building RPA on its own LLM (a) dogfoods internal automation at huge scale, (b) creates a sovereign, sanction-proof alternative to foreign RPA, and (c) feeds the broader "sell the GigaChat ecosystem to Russian corporates" strategy. **Why:** owning the full stack lets Sber capture the automation budget that would otherwise flow to foreign vendors now locked out of Russia.

## [3] Novelty / value-add / traction
- **Genuinely new vs. the company's own prior notes?** Yes, narrowly: this specific "text → BPMN template" feature was not in prior corpus notes and is dated **2026-10-16**. But it is **not new to the market** — UiPath Autopilot and the academic LLM-to-BPMN literature predate it. So novelty is **regional/incremental**, not global.
- **Value-add reality check:** the output is a **draft BPMN skeleton**. The hard, value-capturing part of process automation — connecting to real corporate systems, exception handling, governance, security — still requires engineers. "Weeks → hours" describes the cheap, early prototyping step; it does not prove the expensive end-to-end step shrank. **No external adoption numbers for this feature** (clients, deployed processes) were disclosed — only platform-wide ops counts that predate the feature.
- **Who captures the margin:** Sber captures it internally (import-substitution + ecosystem lock-in to GigaChat). For external clients the bet is that lowering authoring effort drives seat/consumption growth on the GigaChat stack. The margin risk is **commoditization**: text-to-BPMN is becoming table stakes across RPA vendors, so it is a feature-parity defensive move, not a differentiator.

## [4] What's next / market sentiment
- Expect continued GigaARPA iteration (more connectors, deeper agent autonomy, external productization to Russian corporates), consistent with Sber's 2026 cadence of near-daily AI feature announcements (see corpus cluster above).
- **Market sentiment:** the whole RPA category is converging on "agentic automation" — RPA bots do the baseline, AI agents handle exceptions and changing UIs. Sber is on-trend but not leading it.
- **Risks / counterintuitive second-order:** (1) **Hype vs. deployment gap** — generating a BPMN draft is easy; the industry's recurring failure is the last mile of production hardening, so "weeks→hours" may not translate to realized ROI. (2) **Captive-market trap** — Sber's domestic dominance (no UiPath competition) reduces pressure to match global quality, which could leave the product behind once/if borders reopen. (3) **No disclosed external traction** means this reads as a conference demo / roadmap item until paying clients and deployed-process counts appear.

## Sources
- Lenta.ru, "Сбер научил платформу автоматизации собирать бизнес-процессы по текстовому описанию," 2026-10-16: https://lenta.ru/news/2026/10/16/sber-nauchil-platformu-avtomatizatsii-sobirat-biznes-protsessy-po-tekstovomu-opisaniyu/
- CNews, "Платформа Giga Agentic RPA научилась превращать текстовые запросы в готовые бизнес-процессы," 2026-10-16: https://www.cnews.ru/news/line/2026-10-16_platforma_giga_agentic_rpa_nauchilas
- Kod.ru, "Платформа Сбера Giga Agentic RPA начала собирать бизнес-процессы по текстовому запросу": https://kod.ru/giga-agentic-rpa-prompt-process
- TAdviser, "Сбер: GigaARPA (Agentic RPA)": https://www.tadviser.ru/index.php/Продукт:Сбер:_GigaARPA_(Agentic_RPA)
- Lenta.ru, "На AI Journey представили решение Giga Agentic RPA на основе GigaChat," 2025-11-20: https://lenta.ru/news/2025/11/20/na-ai-journey-predstavili-giga-agentic-rpa/
- CNews, "GigaARPA: Искусственный интеллект расширяет возможности платформы роботизации от Сбербанка," 2025-11-20: https://www.cnews.ru/news/line/2025-11-20_gigaarpa_iskusstvennyj_intellekt
- UiPath, "Orchestrating the agentic enterprise: what's new in UiPath 2025.10": https://www.uipath.com/blog/product-and-updates/orchestrating-the-agentic-enterprise-whats-new-in-uipath-2025-10
- SOAIS, "UiPath Agentic Process Modeling Using BPMN": https://soais.com/blog/uipath-agentic-process-modeling-using-bpmn/
- Sber developers portal, GigaARPA: https://developers.sber.ru/portal/products/gigaarpa
- arXiv, "Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach": https://arxiv.org/pdf/2604.12105
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Challenge / red-team (second-order)

1. **Is this a new product or a feature on an existing one?** A feature. GigaARPA itself launched at AI Journey 2025-11-20 (rebrand of SaluteRPA); this is the "Prompt→Process" text-to-BPMN addition announced 2026-10-16. Incremental.

2. **Is it fresh vs. the corpus?** Fresh (narrowly). No prior corpus note covers this specific feature; dated 2026-10-16. But it is NOT novel to the market (UiPath Autopilot/Maestro, Automation Anywhere already do text/NL→BPMN). Novelty is regional/incremental.

3. **Announced or launched?** Announced at an internal engineering conference (GigaConf, 2026-10-16). It is a live platform feature, but NO external client adoption of THIS feature is disclosed. Reads as demo + roadmap for external productization.

4. **What already did the same, with dates?** UiPath Autopilot → BPMN inside Maestro (GA by 2025.10 / 2026 stack); Automation Anywhere AI agents (2024) + Aisera acquisition (Nov 2025); academic LLM→BPMN (arXiv). Open-category, not proprietary.

5. **Does "weeks to hours" survive scrutiny?** Partially — it describes idea→first prototype (draft BPMN), the cheap step. The expensive last mile (system connectors, exception handling, governance, prod hardening) still needs engineers. ROI not demonstrated. Treat as vendor claim.

6. **Who is the real competitive set?** Inside Russia (post-sanctions): domestic RPA vendors (PIX Robotics, Primo RPA) and Sber's own legacy SaluteRPA — NOT UiPath/AA, which exited Russia. So this is import-substitution, not a global-leadership move.

7. **What traction numbers are real vs. recycled?** ~400k operations/day and "99.4% of operations center automated" are PLATFORM-wide, pre-existing stats, NOT evidence this feature is adopted. ~20 docs/min is the IDP module's throughput, also pre-existing. No feature-specific metric.

8. **Where is the margin captured?** Internally (import-substitution + GigaChat ecosystem lock-in); externally the bet is seat/consumption growth on the GigaChat stack. Risk: text-to-BPMN is commoditizing into table stakes → defensive parity feature, not a differentiator.

9. **What is Sber silent about?** Pricing, external paying clients for this feature, how often generated BPMN is usable without heavy rework, accuracy/error rate of the generation, and any benchmark vs. prior manual authoring beyond "weeks→hours."

10. **Does the strategy fit?** Yes, strongly. Sber owns GigaChat/GigaCode + cloud + a huge bank with massive internal automation needs; building RPA on its own LLM dogfoods internally and productizes a sovereign alternative to foreign RPA. Structural logic is sound.

11. **Second-order risk of domestic dominance?** Captive-market trap: with no UiPath competition in Russia, quality pressure is low; the product could lag global peers, a latent risk if the market reopens. (analysis)

12. **Could this materially move Sber's economics?** No. It is one feature in a near-daily stream of Sber AI announcements (AI Studio, GigaIDE, AIFA, cashback agent, bank guarantees). Non-financial, no disclosed revenue impact.

13. **What-if: external clients adopt at scale?** Then it becomes a consumption driver for the GigaChat stack and a moat via workflow lock-in — but that's a future, unproven scenario; nothing today supports it. Open.

14. **Is the headline accurate?** Yes — "adds BPMN generation to Giga Agentic RPA" fairly describes the Prompt→Process feature; no entity conflation. The only nuance: it generates a draft/template, not a finished process.

15. **Net weight?** Low. Regional feature-parity update on an established platform, no new numbers, no external adoption, no financial impact.

**Importance: 2/5 — A genuine but incremental, Russia-only feature-parity update (text→BPMN draft) on a year-old platform; global prior art (UiPath/AA) exists, no external adoption or financial impact disclosed, traction stats are recycled platform-wide figures. Fresh but minor.**
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Global RPA is a $12–35bn market in 2026 (estimates diverge widely by firm) growing ~24–29% CAGR toward $30–247bn by 2030–2035 (per Precedence/The Business Research Co./GlobeNewswire syndications, as of Dec 2025) — the key signal is the direction of travel: classic RPA is being re-platformed into "agentic automation," a narrower but faster-emerging segment (~$7.4bn in 2026 → ~$55bn by 2036, ~22% CAGR, per Future Market Insights). "Why now": LLM/agent orchestration collapses the authoring step — Sber's "Prompt→Process" turns a plain-text brief into a BPMN schema wiring robots + GigaChat agents + document-recognition (IDP), cutting idea-to-prototype from weeks to hours (per CNews/Kod.ru, GigaConf, 2026-10-16). Structure: BFSI is a top RPA vertical; the stack layers as rails (RPA runtime) → orchestration (BPMN/agents) → authoring (NL→process), with value migrating up to the authoring+orchestration layer, where switching costs and model quality create the moat.

**Competitive landscape.** Sector KPIs: ARR/ARR-growth, net dollar retention, automations-in-production, and realized cost-saving/"financial effect." Key players globally: UiPath (listed, est. ~36% share), Microsoft (Power Automate), ServiceNow, Salesforce (Agentforce), IBM, Automation Anywhere (private). Basis of competition is shifting from bot reliability/price to agent orchestration + authoring UX. Recent peer moves: UiPath's agentic stack is explicitly BPMN-based (Maestro orchestration, Agent Builder, Autopilot, IXP) — i.e. Sber's BPMN-from-prompt is directly comparable to UiPath Maestro + Autopilot authoring, not a novel category. Sber's position: for the Russian market this is a credible catch-up/parity move built on its own GigaChat/GigaCode captive stack; globally it is a fast-follow of the UiPath/Microsoft agentic pattern (analysis). Moat is vertical-integration/distribution inside the Russian BFSI+enterprise base (captive demand) rather than a technology lead (analysis).

**Comps & multiples.** Only one clean public comp exists; Sber itself is not a pure-play automation vendor, so this product doesn't carry a standalone multiple.
- **UiPath (NYSE: PATH)** — FY2026 revenue $1.611bn, ARR $1.853bn (+11% y/y), Q4 revenue $481m (+14% y/y); FY2027 guide ARR $2.051–2.056bn (per UiPath IR). No market cap in a free source here → EV/Rev / EV/ARR = no data (would need a verifiable share count/EV; `[UNSOURCED]`). Growth ~11–14% is modest, so any premium multiple would need scrutiny.
- **Automation Anywhere (private)** — last disclosed post-money ~$6.8bn (2019 Series B, $290m raise); 2026 secondary/pre-IPO marks imply only ~$1.5–2bn (Forge/Hiive composite) — a sharp markdown vs the primary round, flagging private-market re-rating risk for pure-play RPA (round/secondary valuation, not market cap).
- **Internal comps** (grep fallback — semsearch index DOWN, OpenRouter 402): [[Zania raises $18M Series A for agentic AI compliance platform]], [[Bank of Singapore deploys agentic AI tool SOWA]], [[Mashreq pilots IBM Bob for agentic AI integration engineering]], [[Backbase launches Conversational Banking for agentic AI]], plus Sber's own adjacent pushes [[Sber unveils free GigaPlatform AI Studio for building AI agents]], [[Sber teaches AIFA financial analyst to self-plan analysis]]. Distribution not computed (no comparable multiples) → qualitative comparison only.

**IR grounding (Sber, company-level).** Sber does not break out Giga Agentic RPA revenue, but the group monetizes AI at scale and self-funds this R&D: FY2025 record IFRS net profit ~RUB 1.58trn (~$22bn, +7.9% y/y); 9M 2025 net profit RUB 1.307trn (+6.5%), Q3 RUB 448.3bn (+9.0%), ROE 23.7%, 9M net interest income RUB 2.568trn (+18%) (per Sber IFRS results via Interfax/TASS; primary filing: FY2025 Summary Consolidated IFRS, 2026-02-26 — https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf). AI "financial effect" targets: ~RUB 450bn ($5.7bn) in 2025 (RUB 50bn from generative AI; ~RUB 30bn realized H1 2025) rising to a ~RUB 550bn target in 2026 on RUB 350bn planned AI capex (per Interfax/TASS). So this launch is a feature inside a self-financed, high-ROE AI program, not a standalone revenue event.

**Risk flags.**
1. **Not differentiated / fast-follow** — BPMN-from-prompt + agent orchestration mirrors UiPath Maestro/Autopilot and Microsoft Power Automate; second-order, Sber competes on captive distribution, not product lead, so the feature is easily matched by global vendors where they can sell (analysis).
2. **"Announced" vs "live/adopted"** — the PR cites weeks→hours and cites no paying-customer count, production automations, or accuracy/validation metrics for auto-generated BPMN; LLM-authored processes carry correctness/hallucination risk in regulated BFSI workflows, so realized savings are unproven (de-PR).
3. **Concentration / sanctions-bounded TAM** — monetization is effectively confined to the Russian market (captive base is also a ceiling); the global RPA re-rating (Automation Anywhere's private→secondary markdown) shows pure-play automation economics are under pressure even for leaders.

**What this changes (idea-lens).** Agentic authoring (NL→BPMN) is becoming table stakes across the RPA stack, compressing the business-analyst authoring layer and pushing differentiation toward orchestration quality + domain data — this is incremental consolidation of Sber's captive AI stack, not a re-rating (analysis). Watch: a disclosed production-automation count or a quantified RUB "financial effect" attributable to Giga Agentic RPA in Sber's 2026 AI-effect tally (catalyst); absence of any adoption metric by the next results cycle would confirm this stays PR-stage (what breaks the thesis).

Sources: https://www.cnews.ru/news/line/2026-10-16_platforma_giga_agentic_rpa_nauchilas · https://kod.ru/giga-agentic-rpa-prompt-process · https://www.globenewswire.com/news-release/2025/12/16/3206126/0/en/Robotic-Process-Automation-RPA-Market-Size-Expands-from-USD-35-27-Bn-in-2026-to-USD-247-34-Bn-by-2035-Fueled-by-AI-Powered-Automation-and-Digitalization.html · https://www.futuremarketinsights.com/reports/agentic-automation-market · https://ir.uipath.com/news/detail/431/uipath-reports-fourth-quarter-and-full-year-fiscal-2026-financial-results · https://forgeglobal.com/automation-anywhere_stock/ · https://interfax.com/newsroom/top-stories/114559/ · https://tass.com/economy/2092243 · https://interfax.com/newsroom/top-stories/115237/ · https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Context-only** — no earnings in this news (product announcement, `type/product`). Financial context from Sber's own reporting (parent company Sber is IR-covered).

**Verdict (financial context).** CONTEXT-ONLY · the item is a Giga Agentic RPA product feature, not a results print. For backdrop: Sber is running a record year — H1 2026 IFRS net profit RUB 1,019bn (+18.6% YoY), ROE 24.2%, well above the 22% FY guidance; 9M 2026 RAS net profit RUB 1.5trn (+18.2% YoY), ROE 23.0%. IR DB (pipeline/state/irdb) is stale (latest indexed = FY2025, 2026-02-26) and semsearch is DOWN (OpenRouter 402), so 2026 figures are from the press/transcripts below, not the filing.

**Key figures (latest reported, H1 2026 IFRS).**
- Net profit: RUB 1,019bn (+18.6% YoY); Q2 2026 alone RUB 511.2bn.
- Net interest income: RUB 2,051bn (+22.5% YoY); Q2 +26.7% YoY — NIM expanding.
- Net fee & commission income: RUB 419.8bn (+5.4% YoY) — the laggard line; Q2 +10.4% YoY.
- ROE: 24.2% (Q2 24%).
- Cost of risk: total portfolio 1.04% (-0.25pp in Q2); corporate 0.9% (+0.6pp in Q2 — rising).
- 9M 2026 RAS (interim, reported 2026-10-09): net profit RUB 1.5trn (+18.2% YoY), ROE 23.0%, NII RUB 2.8trn (+24.1% YoY); fee & commission RUB 534.6bn (-0.8% YoY); retail loans RUB 20.3trn (+10% YTD), mortgages RUB 13.5trn (+11.3% YTD).

**vs expectations / prior period.** No consensus tied to this product news. YoY momentum is strongly positive (profit +18–19%, NII +22–24%) despite a slowing Russian economy; the H1 beat (24.2% ROE vs 22% FY target) implies management is sandbagging guidance. Fee income is the soft spot (RAS 9M -0.8% YoY) — directly relevant to the RPA/AI thesis, which is about monetizing software and operating leverage, not spread income. [No public analyst consensus pulled for this product item — figures are reported actuals, not estimates.]

**Guidance / forward (FY2026, from H1 call).** ROE ~22% (running ahead of it); NIM revised UP to ~6.2%; corporate loan growth DOWNGRADED to 8–10% (from 10–12%); retail loan growth 5–8%; record dividend payout RUB 850bn. Tone: cautiously optimistic; management flagged ~0.5% Russian GDP growth, inflation 6.5–7%, a ~RUB 2trn sector liquidity deficit, and rising corporate risk in metallurgy/agriculture/real estate.

**Thesis-flags (product × financials).**
- NII (+22–24%) is doing the heavy lifting while fee income stalls (-0.8% RAS 9M). Giga Agentic RPA / BPMN generation is a cost-side and future fee-side play: fact — Sber automates its own back office with agents; why — the earnings are spread-driven and NIM is at/near peak; why it matters — as rates eventually fall, operating leverage from internal AI automation (and selling the platform externally) becomes the swing factor for ROE; second-order — the product is defensive margin insurance more than a near-term revenue line.
- Rising corporate cost of risk (+0.6pp in Q2) sits alongside the "AI efficiency" narrative — watch whether automation claims translate into a falling cost/income ratio in the IFRS prints, not just PR. (de-PR: the release tells a product story and is silent on near-term revenue from this feature.)

Sources: Sber H1 2026 IFRS (investing.com transcript) https://www.investing.com/news/transcripts/earnings-call-transcript-sber-posts-strong-h1-2026-profit-as-macro-risks-rise-93CH-4819283 · Sber RAS 9M 2026 (reported 2026-10-09) https://www.akm.ru/eng/news/sberbank-s-ras-net-profit-for-the-first-nine-months-of-2026-increased-by-18-2-/ · IR DB stale (FY2025, 2026-02-26 https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf) + semsearch DOWN (OpenRouter 402) — 2026 actuals from press/transcripts above · consensus: no data (product item).
<!-- /enrichment:earnings_review -->
