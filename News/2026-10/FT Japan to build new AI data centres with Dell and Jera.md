---
title: "FT: Japan to build new AI data centres with Dell and Jera"
date: 2026-10-21
retrieved: 2026-10-21
tags:
  - company/dell
  - company/jera
  - industry/ai
  - region/asia
  - type/partnership
sources:
  - https://www.ft.com/content/ec55a734-243b-43a2-93ea-8652d6b99309
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: se5bfab26
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# FT: Japan to build new AI data centres with Dell and Jera

> [!info] 2026-10-21 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] FT: Япония планирует построить новые дата-центры для ИИ совместно с Dell и Jera

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.ft.com/content/ec55a734-243b-43a2-93ea-8652d6b99309>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Japan to build new AI data centres with Dell and JERA
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 1 Oct 2026 Japan's largest power producer **JERA**, **Dell**, and UK "sovereign AI cloud" developer **RHAELM Holdings** signed an **MoU** (not a contract/FID) to build a **~400MW, >$15bn hyperscale AI campus in Chiba**, next to JERA's existing Chiba Thermal Power Station (~4,380MW). **Apollo Global Management** is RHAELM's strategic financing partner. First operations in phases **2028**, full capacity **2029**. The parties frame it as a repeatable "standardised model" rollable across JERA power stations, scaling to **multiple GW** and a potential **~$140bn** programme (at a stated ~$35–45bn/GW).
- **The FT/"42 секунды" headline ("Dell and Jera") understates two of the most important parties:** RHAELM (the actual developer/operator and sovereign-cloud brand) and Apollo (the capital). The de-PR'd reality is a **financing + power + hardware stack**, not a Dell-led deal — Dell is the *hardware vendor* supplying rack-scale compute (its server/AI-infra business), one of three named legs.
- **The real innovation is not the data centre — it is "behind-the-meter" power.** The campus draws electricity **directly from JERA's generation asset**, bypassing the conventional grid-connection queue. This is "speed to power": grid-connection waits are the binding constraint on AI buildout globally (cf. [[Datacentres use 6% of UK and US electricity, says IDCA]] — UK grid-connection queue grew 460% in H1 2025, multi-year waits). → **Why structured this way:** the deal is engineered around the scarcest input (power delivery timeline), not compute or land — which is why a *utility* (JERA), not a hyperscaler, is the anchor.
- **PR vagueness flags:** "$140bn potential" and "multiple GW" are aspirational extrapolations off a single 400MW MoU; only the first phase is concretely scoped, and even that is pre-FID.

## [1] Competitors / peers
- **SoftBank/OpenAI Stargate (Japan leg):** SoftBank's **Sakai Data Center** (ex-Sharp factory, ~150MW, 2026 start) is the domestic rival; Stargate is a ~$500bn US-centric JV (SoftBank/OpenAI/Oracle), and SoftBank+OpenAI each put ~$500m–$1bn into **SB Energy** precisely to solve the same power-delivery problem (cf. web). → Japan's two biggest AI-infra bets (JERA and SoftBank) are **both power-first**, confirming power is the real battleground.
- **Mastercard France (€250m, 3 DCs)** ([[Mastercard invests €250 million in three France data centres]]) — but that is *payment-resilience* capacity, a different workload class/scale; not a true peer.
- **Hyperscalers in Japan:** Microsoft, Google, AWS, Oracle all expanding JP capacity, but typically grid-connected and not utility-anchored. JERA's behind-the-meter angle is the differentiator.
- **Position:** Japan is a *catch-up / sovereign* play — it lacks the US's gigawatt-scale campuses and wants domestic sovereign AI compute. This deal is ahead on the *power model*, behind on absolute scale vs US Stargate.

## [2] Company history / fit
- **JERA** is a JV of Tokyo Electric (TEPCO) and Chubu Electric — ~a third of Japan's thermal generation. Fit is **structural**: a thermal utility facing long-term demand erosion (decarbonisation, population decline) is repurposing spare/co-located generation into high-margin "power-as-a-service" for AI. → **Why:** commodity power take-rate → stranded-asset risk → AI compute is the highest-value new offtake JERA can bolt onto existing plants without building new transmission.
- **Dell** — this extends Dell's pivot to being an AI-infrastructure systems integrator (rack-scale, GPU servers); low-margin PC maker chasing the AI-server multiple. Being a *named* partner in a $15bn flagship is marketing capital as much as revenue.
- **Apollo** — part of the broader PE/infra-credit land-grab into data-centre financing (digital infra is the hot private-credit asset class). RHAELM is the new, thinly-documented "sovereign cloud" operator — the weakest-known leg.

## [3] Novelty / value-add / traction
- **New:** the utility-anchored, behind-the-meter *template* designed to be franchised across a fleet of power stations. That franchising intent (not one site) is the genuinely novel bit.
- **Not new / not yet traction:** it is an **MoU, pre-FID, zero megawatts live**. No customer/offtake named for the compute (who rents the 400MW?). "Announced ≠ built." Compare [[This Week in Fintech IMF warns of AI investment bubble]]: IMF/BoE flagged exactly this pattern of circular, announcement-driven AI capex in late 2025.
- **Who captures the margin (analysis):** power scarcity means **JERA (the power owner) captures the durable rent**; Dell gets one-off hardware revenue; RHAELM/Apollo carry build + financing risk; the compute-demand risk (will AI offtake fill 400MW+?) sits with whoever signs the compute leases — currently unnamed. The margin accrues to whoever controls the scarcest input = power.

## Sources
See frontmatter FT link + Nikkei Asia, FT (via TheNextWeb), Japan Times/Bloomberg (Apollo), HPCwire/AIwire (JERA-Dell-RHAELM MoU), datacentremagazine, TechRadar. All dated 1–2 Oct 2026.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## [4] What's next / market sentiment
_Importance: 3/5._

- **Near term:** MoU → feasibility/FID on the 400MW Chiba phase; first power/compute in phases 2028, full 2029. Watch for (a) a named **compute offtaker/customer** for the capacity, (b) FID + final financing structure (Apollo/private credit), (c) whether the "standardised model" actually gets signed at a *second* JERA site — the $140bn/4GW figure is meaningless until it does.
- **Sentiment / backdrop:** rides the Japan sovereign-AI + "speed-to-power" narrative, but lands amid explicit AI-bubble warnings from IMF/BoE and growing public pushback on datacentre power/water use ([[Datacentres use 6% of UK and US electricity, says IDCA]]). Behind-the-meter sidesteps the *grid-queue* problem but not the *fossil-fuel* optics — drawing from a thermal plant invites decarbonisation criticism.
- **Second-order (analysis):** if behind-the-meter utility anchoring becomes the standard template, the AI-infra bottleneck shifts from land/GPUs to **who owns dispatchable generation** — repricing incumbent thermal utilities (JERA, and SoftBank via SB Energy) as AI-infra platforms, not commodity power sellers. Counterintuitively, that concentrates fragility: a 400MW+ load behind one power station couples compute uptime to a single generation asset.

## Top challenge/extra questions (second-order)
1. Who is the **compute customer** for the 400MW? No offtaker named → biggest open risk. **(open)**
2. Is this an MoU or an FID? **MoU, pre-FID** — no capital committed yet, no megawatts live.
3. Is "Dell and JERA" accurate? **No** — RHAELM (developer/operator) and Apollo (financing) are co-equal legs the headline drops; Dell is the hardware vendor.
4. What is RHAELM's track record as a sovereign-cloud operator? **(open — thinly documented, newest/weakest-known party.)**
5. Does behind-the-meter actually clear faster? Claim = "years ahead of grid-connected"; plausible given grid queues, but unproven at this scale. **(open)**
6. Who captures the durable margin? **Power owner (JERA)**; Dell = one-off hardware; compute-demand risk unassigned.
7. Is $140bn / multiple-GW real or PR? **Extrapolation** off one MoU; treat as aspiration.
8. Fossil-fuel exposure? Thermal-plant power → decarbonisation/ESG risk vs SoftBank's SB Energy (renewables-leaning). **(open)**
9. Vs SoftBank/OpenAI Stargate Japan (Sakai ~150MW)? This is larger (400MW) and utility-anchored vs factory-conversion. **Different model, both power-first.**
10. Fintech relevance? **Marginal/indirect** — it is AI-infra/power, not a financial-services product; matters as macro AI-capex + Apollo private-credit signal, hence importance 3 not higher.
11. Downside trigger? AI-demand softening (bubble) leaves 400MW+ stranded; or FID slips. **(open)**
12. Why a utility anchor vs hyperscaler? JERA monetises stranded thermal assets + owns the scarce input (power). **Structural.**
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is an AI-infrastructure (compute capex + behind-the-meter power) story, not a payments one. De-PR'd scope: the FT headline names "Dell and Jera," but the signed MoU is a three-party deal — JERA (Japan's largest power producer / world's largest LNG trader), Dell Technologies (rack-scale AI hardware), and UK-based AI-cloud provider RHAELM (per DCD/Nikkei, 1 Oct 2026). First node: a ~$15bn, up-to-400MW data centre at JERA's Chiba Thermal Power Station, targeting operation ~2028, powered directly off the adjacent gas plant *without* public-grid connection (Nikkei Asia). Broader framing: Japan eyes ~$140bn across 3–4GW of AI DC capacity within ~5yr (~$35–45bn/GW incl. gas power), aiming to be the largest AI compute hub outside the US/China (FT, via thenextweb/dealroom). Sector size (analysis): PwC projects global DC capex rising from ~$800bn (2026) toward ~$1.8tn by 2050, ~100GW of new capacity 2026–2030 — i.e. a genuine capex supercycle. "Why now": the binding constraint has shifted from chips to *power + grid interconnect* — PwC flags 30–50% of 2026-planned DC capacity slipping to 2028+ on power/supply-chain limits; inner-Tokyo grid waits can run 5–10yr. Behind-the-meter gas co-location is the structural answer to that bottleneck.

**Competitive landscape.** Sector KPIs: IT-load MW (and $/MW build cost), power capacity (GW) and time-to-energize, PUE/utilization, and for the vendor leg AI-server backlog→revenue conversion. Basis of competition here is *speed-to-power* and standardization, not price. Players: hyperscalers (AWS/Azure/Google) and neocloud/GPU-cloud entrants (CoreWeave, Nebius, SuperX — the last took a $38.8m NVIDIA B300 order for Yokohama) on the demand side; on the build side, power-anchored developers. JERA's edge is a genuine moat: 20+ existing power sites and ~35Mt/yr LNG trading, i.e. *proprietary, fast, off-grid power* — the scarce input (analysis). Dell's position: ahead and scaling — ISG FY2026 revenue a record $60.8bn (+40%), AI-optimized server revenue +166%, AI backlog ~$43bn at FY-end with mgmt guiding AI revenue to ~$50bn in FY27 (SEC 10-K / Futurum). This MoU is a template-able channel into Japan's $140bn pipeline, not just one order.

**Comps & multiples.** Dell (public) is the one cleanly-sourced leg: EV/Revenue = $393.3bn / $113.5bn ≈ **3.5x** trailing (EV per gurufocus; FY2026 revenue per Dell 8-K, 26 Feb 2026). For a predominantly hardware/distribution mix that is on the richer side vs legacy-hardware norms (~0.5–2x) but defensible given AI-server growth (+166%) — a classic growth-justified multiple, not an outlier risk. JERA and RHAELM: private/complex — no clean public EV/Rev; the $15bn spend is a *project capex* figure (≈$37.5m/MW at 400MW), NOT a valuation — do not read it as such. Internal comps (grep fallback, semsearch 402-down): [[Mastercard invests €250 million in three France data centres]] (payments-resilience DC, different thesis), [[Datacentres use 6% of UK and US electricity, says IDCA]] (power-draw context), [[Coinbase suffers multi-hour trading outage after AWS failure]] (cloud-concentration fragility). Distribution not computed — only one truly comparable public multiple.

**Risk flags.**
1. **Execution / timeline to 2028** — only an MoU (non-binding), 400MW first node operational ~2028; a DC co-located with a new behind-the-meter gas plant stacks permitting, construction and fuel-logistics risk. Slippage directly erodes the "speed-to-power" thesis that is the whole point.
2. **Fuel & carbon exposure** — behind-the-meter power = LNG-fired. This hard-wires AI load to gas prices and to Japan's decarbonization policy; a carbon levy, fuel-price spike, or green-DC procurement mandate (hyperscaler net-zero pledges) could strand or re-price the capacity.
3. **Demand concentration / build-ahead** — $140bn / 3–4GW is speculative capacity ahead of signed offtake; if AI compute demand or GPU-cloud economics soften (SuperX-style neoclouds are thin-margin), JERA/developers carry utilization risk while the value (and margin) accrues up-stack to NVIDIA and the model labs — classic "who captures the rail" exposure.

**What this changes (idea-lens).** (analysis) Behind-the-meter gas co-location is becoming the credible workaround to grid gridlock — this positions power producers (not just hyperscalers) as the gatekeepers of AI capacity, a potential re-rating vector for utilities with fast dispatchable generation. Falsifiable thesis: if the Chiba node energizes on/near schedule (~2028) and JERA converts ≥1 further site into a binding build, the $140bn "compute hub" framing is real; trigger to watch — conversion of the MoU to a binding EPC/offtake and a named anchor tenant. What breaks it: no firm hyperscaler/neocloud offtake by 2027, or Japanese carbon policy penalizing gas-fired DC load.

Sources: https://asia.nikkei.com/business/technology/artificial-intelligence/japan-s-largest-power-producer-teams-with-dell-on-15bn-data-center · https://www.datacenterdynamics.com/en/news/jera-dell-technologies-and-rhaelm-team-up-for-behind-the-meter-ai-infrastructure-in-japan/ · https://thenextweb.com/news/japan-140bn-ai-data-centre-dell-jera · https://www.sec.gov/Archives/edgar/data/1571996/000157199626000008/dell-20260130.htm · https://www.sec.gov/Archives/edgar/data/1571996/000157199626000003/exhibit991earnings8kq4fy26.htm · https://introl.com/blog/japan-data-center-power-crisis-hyperscaler-investment-2026
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
