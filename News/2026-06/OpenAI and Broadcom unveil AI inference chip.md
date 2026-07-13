---
title: "OpenAI and Broadcom unveil AI inference chip"
date: 2026-06-24
retrieved: 2026-06-26
tags:
  - company/openai
  - company/broadcom
  - industry/ai
  - region/us
  - type/product
sources:
  - https://www.bloomberg.com/news/articles/2026-06-24/openai-and-broadcom-unveil-ai-chip-to-run-models-faster-cheaper
status: published
n_mentions: 1
channels:
  - "42 секунды"
story_id: sa464713b
month: 2026-06
enriched: true
importance: 3
---

# OpenAI and Broadcom unveil AI inference chip

> [!info] 2026-06-24 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Bloomberg: OpenAI и Broadcom представили ИИ-чип, который позволяет быстрее и дешевле запускать модели

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.bloomberg.com/news/articles/2026-06-24/openai-and-broadcom-unveil-ai-chip-to-run-models-faster-cheaper>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: OpenAI and Broadcom unveil AI inference chip ("Jalapeño")
_Analytical notes (not a post). Importance: 3/5._

Skeptical reading. Every unveil-day technical/cost number traces to OpenAI/Broadcom themselves — there are no independent benchmarks yet. Unverified items marked "(open)".

## [0] What exactly happened (de-PR'd)
On 2026-06-24 OpenAI and Broadcom **unveiled "Jalapeño,"** OpenAI's first-ever custom silicon: an **inference-only ASIC** ("Intelligence Processor"), reticle-sized, taped out in a claimed ~9 months ("fastest ever," self-described). Crucially this is **not a shipping product**: on unveil day it was at the **engineering-sample-in-lab stage** (samples running ML workloads incl. "GPT-5.3-Codex-Spark" at production target freq/power). Roadmap: **small prototype deployment late 2026 → production ramp 2027 → expand 2028**, within a **10 GW** envelope through 2029.
- **What "unveil" means here:** tape-out + lab samples, NOT volume shipping. First-silicon programs routinely slip → treat "late-2026 deployment" as a target, not a fact (open).
- **Why framed this way / what it reveals:** This is **the first concrete product of the year-old Oct 13, 2025 Broadcom 10 GW deal**, repackaged as a fresh "unveil." OpenAI does **architecture only**; Broadcom does RTL/physical design, signoff and networking; **TSMC** fabs (reported); **Celestica** integrates. So OpenAI's "own chip" is heavily vendor-built — differentiation is in architecture, not manufacturing.
- **Cost claim:** "~50% cheaper per inference token than Nvidia GPUs" and "on par with Blackwell/Google TPU" are **Hock Tan CEO interview statements (Bloomberg / Reuters)** — not a published benchmark, no disclosed baseline, detailed report "promised in coming months." Discount as directional marketing.

## [1] Competitors / peers
OpenAI is **the latecomer** to the hyperscaler-ASIC playbook:
- **Google TPU** (Ironwood/v7-era): most mature, only one with an external-customer software stack.
- **AWS Trainium**: largest commercial volume (~500k Trainium2 for Anthropic by Oct 2025; Trainium4 announced Dec 2025) → see [[AWS in talks to sell Trainium AI chip racks to outside companies]].
- **Microsoft Maia** (Maia 200, TSMC 3nm) already serves GPT-5.2 for OpenAI; **Meta MTIA** has a 4-gen roadmap.
- China parallel: [[China orders tech giants to halt Nvidia AI chip purchases]] (Alibaba/Baidu on own silicon) and [[ByteDance develops custom CPUs to power AI infrastructure]] — same reduce-Nvidia-dependence logic.
- **+ Second-order:** Custom AI ASIC shipments are projected to outpace GPU growth (TechTimes, 2026-05). But like all these chips, Jalapeño is **captive — inference-only, internal use, not rentable.** It does NOT replace Nvidia for training; OpenAI keeps buying Nvidia/AMD GPUs. The "strike at Nvidia" framing is overstated for now: this dents Nvidia's *inference-margin* thesis at the margin, not its training monopoly.

## [2] Company history / fit
OpenAI has **never shipped a chip** — this is its first vertical-integration move into silicon. It fits a 2025-2026 spree of ~$1T+ in compute commitments (Nvidia ~$100B equity/10 GW; AMD 6 GW + warrants for ~160M shares @ $0.01; Oracle/Stargate >$300B; Broadcom 10 GW ~$350B reported; Microsoft ~$250B Azure; CoreWeave ~$22B) — context in [[Seven European fintech deals raise EUR 95 million in a week]] (notes the 10 GW Broadcom order, $350-500B).
- **+ Why:** Inference now eats the AI cost base ("the year inference eats the industry" — see [[Baseten reportedly raising at $400 million valuation for AI model infrastructure]]). Owning inference silicon attacks the "Nvidia tax" on OpenAI's largest and growing cost line, and encodes model-specific knowledge into hardware for better perf/watt. Structural pressure: ~$1T+ committed vs ~$20B 2025 ARR and >$17B/yr burn → unit economics on inference are existential.

## [3] Novelty / value-add / traction
**Genuinely new** (first OpenAI silicon, fast tape-out) **but unproven**: zero independent benchmarks, lab samples not volume, vendor-only cost claims, no disclosed node/HBM/TFLOPs or per-GW unit figure (open).
- **+ Why value-add is real-but-fragile:** Real *if* perf/watt and the ~50% cost edge hold at scale — that would meaningfully cut OpenAI's inference COGS and reduce Nvidia dependence. But OpenAI outsources the hard parts (Broadcom/TSMC/Celestica), so margin capture in the silicon stack is shared, not captured. **Where margin sits:** if the chip works, value accrues to OpenAI (lower COGS) AND to Broadcom (recurring ASIC + networking revenue — AVGO popped ~3-9% on the news) — Nvidia loses inference share, not the whole pie.

## [4] What's next / market sentiment
Late-2026 prototype → 2027 ramp → 2028 expand; gigawatt-scale with Microsoft and others. Sentiment: bullish for **Broadcom/AVGO** (now the pure-play custom-ASIC winner), bearish-at-the-margin for **Nvidia** inference moat.
- **+ Why / counterintuitive second-order:** The bigger live question is **financing, not silicon.** ~$1T+ commitments vs ~$20B ARR, with documented **circular/vendor financing** (Nvidia invests in OpenAI which buys Nvidia; AMD warrants tied to OpenAI's own purchases — see Bloomberg "AI circular deals"). OpenAI's CFO has publicly flagged pay-ability. So capital concentration makes the AI-capex web **fragile, not safe** — a Jalapeño slip or demand wobble propagates across Broadcom/Oracle/AMD/TSMC/Celestica. Whether this is unsustainable is contested (open).
- **Fintech relevance — honest:** **Largely tangential.** Not a fintech product. Matters only as (1) macro AI-capex / "bubble vs real demand" debate that moves equities; (2) public-equity input for Nvidia/Broadcom/AMD/Oracle/TSMC valuations and the Nvidia-margin thesis; (3) a credit/balance-sheet (circular-financing) story. Frame as a markets/macro item, explicitly adjacent to fintech.

## Sources
- OpenAI release: https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
- Broadcom IR: https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor
- Oct 2025 deal: https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/
- Bloomberg (unveil): https://www.bloomberg.com/news/articles/2026-06-24/openai-and-broadcom-unveil-ai-chip-to-run-models-faster-cheaper
- CNBC (unveil): https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html
- Tom's Hardware: https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle
- TechCrunch: https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
- VentureBeat: https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models
- $1T deal guide: https://www.cnbc.com/2025/10/15/a-guide-to-1-trillion-worth-of-ai-deals-between-openai-nvidia.html
- Circular financing: https://www.bloomberg.com/graphics/2026-ai-circular-deals/ ; https://blogs.cfainstitute.org/investor/2025/12/08/the-two-ai-stories-measurable-gains-and-hidden-balance-sheet-pressure/
- OpenAI ARR/compute: https://www.datacenterdynamics.com/en/news/openai-cfo-says-company-ended-2025-with-19gw-of-compute-scaled-revenue-at-same-speed/
- Competitive landscape: https://www.cnbc.com/2025/11/21/nvidia-gpus-google-tpus-aws-trainium-comparing-the-top-ai-chips.html
- Internal: [[Seven European fintech deals raise EUR 95 million in a week]], [[AWS in talks to sell Trainium AI chip racks to outside companies]], [[China orders tech giants to halt Nvidia AI chip purchases]], [[ByteDance develops custom CPUs to power AI infrastructure]], [[Baseten reportedly raising at $400 million valuation for AI model infrastructure]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **New deal or old one?** → Activation/first-product of the **Oct 13, 2025** Broadcom 10 GW deal. Not a new relationship.
2. **Is Jalapeño shipping?** → No. **Engineering samples in lab** on unveil day; small prototype deployment *targeted* late-2026, ramp 2027.
3. **First OpenAI chip ever?** → Yes — first silicon, start of a multi-generation program. Execution risk unproven.
4. **Source of "~50% cheaper than Nvidia"?** → **Hock Tan, Bloomberg interview** — CEO claim, not a benchmark, no baseline disclosed. Directional only.
5. **Source of "on par with Blackwell/TPU"?** → **Hock Tan, Reuters.** Vendor claim, no published benchmark.
6. **Independent benchmarks?** → None. Detailed report "promised in coming months." Open.
7. **Who actually builds it?** → Broadcom (RTL/physical/signoff/networking), **TSMC** (fab, reported), Celestica (systems). OpenAI does architecture only — "custom chip" is heavily vendor-dependent.
8. **9-month tape-out — verifiable?** → Self-described "fastest ever"; plausible via Broadcom IP reuse, but unverified superlative. Open.
9. **Does it replace Nvidia?** → No — **inference-only**; OpenAI still buys Nvidia/AMD for training. "Strike at Nvidia" overstated.
10. **Node / HBM / TFLOPs / per-GW units?** → Not disclosed beyond "reticle-sized ASIC." Open.
11. **Will late-2026 deployment hit on time?** → Open — it's a target; first-silicon slips are common.
12. **Total OpenAI compute commitments?** → ~$1.0-1.5T order-of-magnitude solid; exact figure overlaps/double-counts → open. (Nvidia ~$100B, AMD ~$90B, Oracle >$300B, Broadcom ~$350B, MSFT ~$250B, CoreWeave ~$22B, AWS ~$38B.)
13. **Is the financing circular?** → Partly yes (Nvidia equity-in/chips-out; AMD warrants tied to OpenAI purchases). Sustainability contested; CFO flagged pay-ability vs ~$20B ARR. Open.
14. **Rank vs hyperscaler ASICs?** → Behind Google TPU, AWS Trainium, MSFT Maia, Meta MTIA on maturity/volume; same playbook, faster, but captive/inference-only.
15. **Who captures the margin if it works?** → OpenAI (lower inference COGS) + Broadcom (recurring ASIC/networking revenue); Nvidia loses inference share, not the whole pie. TSMC/Celestica take fab/integration cut.
16. **Is this fintech?** → No — adjacent. Relevant only as AI-capex macro, Nvidia/AVGO valuation input, and circular-financing/credit story.

Importance: 3/5 — Genuine novelty (OpenAI's first custom silicon, fast tape-out) and a material data point in the $1T+ AI-capex / Nvidia-margin narrative that moves AVGO/NVDA equities. But discounted because: lab-stage not shipping, vendor-only unverified cost/perf claims, heavily outsourced execution, and only tangential (macro/markets) fintech relevance.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-27]] (2026-06-27).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: custom AI silicon (ASIC accelerators), the layer of AI-infra now growing fastest within the broader AI-accelerator market. Size/growth: per Bloomberg Intelligence (company press release, 2026), the total AI-accelerator market grows ~16% CAGR to ~$604bn by 2033 (from $116bn in 2024); within it, custom ASICs grow ~27% CAGR to ~$118bn by 2033, rising from ~8% to ~19% of the accelerator mix — i.e. ASIC is the share-gainer, GPUs the share-donor (per Bloomberg Intelligence, via Bloomberg LP press, 2026). JPMorgan separately projects custom AI ASIC shipments may surpass GPUs around 2027 (per JPMorgan, via Bitget/indmoney summaries, 2026 — treat the exact crossover date as an analyst call, not fact). Structure: highly **consolidated on the design-services side** — Broadcom holds a reported ~70%+ of custom AI-accelerator design (older estimates 80-85%), Marvell second at ~10-12% (per indmoney/Tom's Hardware, 2026). Entry barriers are extreme: advanced-node IP (SerDes, HBM controllers, networking), TSMC leading-edge capacity, and multi-year hyperscaler relationships. Why now: inference is becoming the dominant AI cost line ("the year inference eats the industry"), and every large model owner (Google/AWS/Microsoft/Meta, now OpenAI) is verticalizing silicon to cut the "Nvidia tax" on per-token COGS. The OpenAI move is the **first product** of the Oct-2025 Broadcom 10 GW deal (~$350-500bn reported), not a new relationship.

**Competitive landscape.** Sector KPIs: AI-accelerator design share, AI-semiconductor revenue growth, gross/operating margin (ASIC design vs merchant GPU), and per-token inference cost. Key players & basis of competition: **Nvidia** (merchant GPU, competes on full-stack CUDA software + ecosystem lock-in; ~74% inference share, up from ~66%, per cryptobriefing/The Information, 2026 — note its inference share is reportedly *rising*, not falling); **Broadcom** and **Marvell** (custom-ASIC design + networking, compete on co-design + interconnect); captive in-house programs — Google TPU (most mature, only external software stack), AWS Trainium (largest commercial volume), Microsoft Maia, Meta MTIA. Recent moves: Broadcom Q2-FY2026 (ended 2026-05-03) AI-semi revenue $10.8bn, +143% y/y, with Q3 guided to ~$16.0bn (>200% y/y) and full-year FY2026 AI revenue ~$56bn, +~180% y/y (per Broadcom IR / PRNewswire, 2026); Google reported in talks to add Marvell to its TPU/inference program alongside Broadcom (per The Next Web, 2026). Protagonist's position: OpenAI is the **latecomer** to the hyperscaler-ASIC playbook — behind Google/AWS/Microsoft/Meta on maturity and volume; Jalapeño is at lab/engineering-sample stage, inference-only, captive (not rentable). Moat for OpenAI = model-specific architecture knowledge encoded in hardware `(analysis)`; but the durable economic moat sits with **Broadcom** (design IP + recurring ASIC/networking revenue), since OpenAI outsources RTL/physical/signoff (Broadcom), fab (TSMC) and integration (Celestica).

**Comps & multiples.** The cleanest comparison is the two listed pure-play ASIC-design beneficiaries (Broadcom, Marvell) vs merchant-GPU Nvidia. Multiples as of ~2026-06-26 (third-party aggregators — stockanalysis/Yahoo/gurufocus — so treat as directional, not filings-grade):
- **Broadcom (AVGO):** mkt cap ~$1.80T, EV ~$1.85T. EV / FY26 AI-revenue = `$1.85T / $56bn ≈ 33x` (AI-only — rich, but AI is a fraction of group revenue). EV / annualized group revenue ≈ `$1.85T / (~$22.2bn x 4 ≈ $89bn) ≈ 21x` (analysis; annualizing Q2 is crude). Forward P/E reported in a wide ~24-38x band across sources → use ~35x as a rough mid `[range, not a single sourced figure]`.
- **Marvell (MRVL):** mkt cap ~$242bn; FY26 (ended Jan-2026) revenue $8.2bn, +42%; data-center ~$6bn. P/S ≈ `$242bn / $8.2bn ≈ 30x`; forward P/E reported ~85-92x — the richest of the three, consistent with smaller-base hyper-growth.
- **Nvidia (NVDA):** forward P/E reported ~18-25x in 2026 (one outlier source ~42x); EV/Rev far lower than the ASIC names relative to growth. The **cheapest** of the three on forward earnings despite ~74% inference share and DC revenue ~$60bn/qtr (Q1-FY27).
Internal comps (in-base precedent for the dis-intermediate-Nvidia / custom-silicon thesis): [[AWS in talks to sell Trainium AI chip racks to outside companies]], [[China orders tech giants to halt Nvidia AI chip purchases]], [[ByteDance develops custom CPUs to power AI infrastructure]], [[Baseten reportedly raising at $400 million valuation for AI model infrastructure]], [[Seven European fintech deals raise EUR 95 million in a week]] (which logged the 10 GW Broadcom order). Read-across: ASIC-design names (AVGO/MRVL) carry **richer multiples than NVDA** — the market is paying up for the share-shift narrative; this is defensible only if the ASIC ramp (and OpenAI's Jalapeño) actually ships at scale. EV/EBITDA, clean forward consensus and NTM figures `[UNSOURCED]` (no free filings-grade source).

**Risk flags.**
1. **Customer/financing concentration (the dominant flag).** OpenAI carries reported ~$1.4T of multi-year compute commitments against ~$20B ARR and ~$14-27B 2026 burn (per Fortune/valueaddvc/Sacra, 2026). A meaningful slice of the ASIC bull case (and Broadcom's $56bn FY26 AI number) rests on a handful of capital-hungry customers; a Jalapeño slip or OpenAI funding wobble would propagate to Broadcom/TSMC/Celestica revenue. Second-order: AVGO's AI growth is increasingly single-customer-cohort-sensitive.
2. **Circular / vendor financing fragility.** Documented loops (Nvidia equity into OpenAI which buys Nvidia; AMD warrants tied to OpenAI purchases; Nvidia–CoreWeave–OpenAI) mean demand signals may be partly self-referential, inflating perceived end-demand for all silicon vendors. If one node de-rates, the web tightens fast.
3. **Execution / "announced vs shipping" gap.** Jalapeño is lab samples, not volume; cost/perf claims (~50% cheaper, on par with Blackwell) are vendor CEO statements (Hock Tan), no independent benchmark. Valuation multiples on AVGO/MRVL already price a smooth ASIC ramp; first-silicon slips are routine. Also note Nvidia's inference share is reportedly *rising* — the "ASICs are eating inference" thesis is not yet visible in NVDA's share data.

**What this changes (idea-lens).** `(analysis)` This is a re-rating story, not a near-term Nvidia displacement: it cements Broadcom as the listed pure-play custom-ASIC winner and extends the inference-cost-war to OpenAI, but it does not dent Nvidia's training monopoly and (per current data) not yet its inference share. Falsifiable thesis: if Jalapeño hits its late-2026 prototype / 2027 ramp and the ~50% cost claim survives an independent benchmark, Broadcom's AI-revenue trajectory and AVGO's premium are validated and Nvidia's inference-margin thesis erodes. What breaks it: a Jalapeño slip, a withdrawn/under-funded OpenAI commitment, or Nvidia inference share continuing to climb — any would expose the rich ASIC-name multiples. Fintech tie is **tangential** (not a fintech product): relevant only as AI-capex/"bubble vs real demand" macro, a public-equity input for NVDA/AVGO/MRVL/Oracle/TSMC, and a credit/balance-sheet (circular-financing) story.

Sources: https://www.bloomberg.com/company/press/ai-accelerator-market-looks-set-to-exceed-600-billion-by-2033-driven-by-hyperscale-spending-and-asic-adoption-according-to-bloomberg-intelligence/ · https://www.indmoney.com/blog/us-stocks/ai-chip-war-broadcom-avgo-marvell-mrvl-asic · https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia · https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial · https://stockanalysis.com/stocks/avgo/statistics/ · https://www.macroaxis.com/stock/MRVL/Marvell-Technology-Group · https://cryptobriefing.com/nvidia-ai-inference-chip-market-share-74-percent/ · https://fortune.com/2025/11/12/openai-cash-burn-rate-annual-losses-2028-profitable-2030-financial-documents/ · https://www.bloomberg.com/graphics/2026-ai-circular-deals/ · https://thenextweb.com/news/google-marvell-ai-chips-inference-tpu-broadcom
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
