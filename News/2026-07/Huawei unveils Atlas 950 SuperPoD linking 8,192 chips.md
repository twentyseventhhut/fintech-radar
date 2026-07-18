---
title: "Huawei unveils Atlas 950 SuperPoD linking 8,192 chips"
date: 2026-07-18
retrieved: 2026-07-18
tags:
  - company/huawei
  - industry/ai
  - industry/infrastructure
  - region/asia
  - type/product
sources:
  - https://substack.com/redirect/7f0e66f6-1d23-4270-b902-af5eace62870
status: enriched
n_mentions: 1
channels:
  - "MTS"
story_id: s79e8a2ce
month: 2026-07
enriched: true
importance: 2
freshness: stale
---

# Huawei unveils Atlas 950 SuperPoD linking 8,192 chips

> [!info] 2026-07-18 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: MTS

## Агрегированный текст (из дайджестов)

[MTS] Huawei announces the Atlas 950 SuperPoD, capable of connecting up to 8,192 Huawei accelerator chips at 8 EFLOPS (8 × 1018 floating-point operations per second) at FP8 precision, with up to 1,152 TB of memory (in theory). It’s still behind Nvidia’s Vera Rubin.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/7f0e66f6-1d23-4270-b902-af5eace62870>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Huawei unveils Atlas 950 SuperPoD linking 8,192 chips
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS: STALE-ish / RE-SHOWING (leaning stale as a "new event").** The Atlas 950 SuperPoD is **not new**: Huawei first unveiled it at **Huawei Connect 2025 (Sept 2025)** with the exact same headline specs (8,192 Ascend 950DT NPUs, 8 EFLOPS FP8 / 16 EFLOPS FP4, 1,152 TB memory, 160 cabinets, 4Q26 availability). The July-2026 peg (MTS digest, dated 2026-07-18) is a **re-report of the public overseas/domestic showing at the WAIC / Shanghai World Expo hall on 2026-07-16** — the first time the physical unit was displayed publicly — bundled with press around Huawei's **Q4-2026 South Korea market-entry** plan. So the *product announcement* is ~10 months old; what is marginally new in July 2026 is (a) the public display of the hardware and (b) the Korea go-to-market. The MTS one-liner ("still behind Nvidia's Vera Rubin") is a fresh comparative framing but not a new event. Treat the *specs* as a Sept-2025 re-run; the *only* genuinely-2026 news thread is the Korea launch, which itself is still a plan (Q4-2026), not a shipment. No prior corpus note covers the Atlas 950 specifically, so it is not a literal duplicate of an existing note — but it is a re-announcement, not a new development. Related corpus: [[Nvidia halves list of Asia buyers over China chip export curbs]], [[China's LineShine supercomputer declared world's fastest]], [[Huawei Cloud expands Egypt fintech infrastructure presence]].

## [0] What exactly happened (de-PR'd)
De-PR'd: Huawei is **marketing** (not yet shipping) the **Atlas 950 SuperPoD** — a rack-scale AI "supernode" that lashes **up to 8,192 Ascend 950DT accelerators** into one logical pool via Huawei's proprietary **UnifiedBus (SuperPoD Interconnect)** optical fabric. Claimed system specs: **8 EFLOPS FP8, 16 EFLOPS FP4, 1,152 TB total memory, 16.3 PB/s interconnect bandwidth, 160 cabinets (128 compute + 32 comms) over ~1,000 m²**, all-optical interconnect. **Availability: Q4 2026** (announced, not GA; individual Ascend 950 chips also 2026, 960 in 2027).

**What's marketing vs real.** The eye-catching numbers are **system-aggregate, scale-by-brute-force** figures, not per-chip leadership. Huawei's own claim — "6.7x the compute and 15x the memory of Nvidia's NVL144" — is true only because the Atlas packs **~57x more chips** (8,192 vs 144) into a far larger footprint. Per-chip, an Ascend 950DT trails a Nvidia Blackwell part badly: **~780 TFLOPS BF16 vs ~2,500 (GB200), 128–144 GB memory vs 192 GB, 3.2–4 TB/s bandwidth vs 8 TB/s**. The note's own caveat ("still behind Nvidia's Vera Rubin") is correct: at the chip and next-gen level, Nvidia leads; Huawei wins only the "biggest single box" headline. **The 1,152 TB memory is flagged "in theory"** in the source — i.e. full-config, not a delivered benchmark.

**Why structured this way / what it reveals.** Huawei can't win on **node** (blocked from EUV / leading-edge TSMC, stuck on SMIC N+2 ~7nm, limited domestic HBM), so it competes on **system scale + interconnect + price** — throw many weaker chips at the problem and connect them tightly. The whole SuperPoD design is a **direct architectural answer to being node-constrained**: if you can't make each chip faster, make the box bigger and the fabric fatter. That is the real story, not the EFLOPS headline.

## [1] Competitors / peers
- **Nvidia GB200 NVL72 / NVL144 (GB300):** the reference point. NVL72 = 72 Blackwell GPUs/rack, already **shipping**; NVL144 (Rubin-gen) is the near comp Huawei benchmarks against. Nvidia wins per-chip and on software (CUDA); Huawei wins single-domain scale. Nvidia's next gen ("Vera Rubin") is what the note says Huawei is "still behind."
- **AMD Instinct "MegaPod":** planned **2027** — a year behind even Huawei's Q4-26 target.
- **China domestic stack:** Cambricon, Biren, Moore Threads (chip-level); on the compute-independence theme, [[China's LineShine supercomputer declared world's fastest]] (Jun 2026) is the CPU-supercomputer analogue of the same "self-sufficiency via scale, not leading-edge nodes" playbook.
- **Position:** Huawei is **catching up via scale**, still behind on node/per-chip/software, but **ahead of AMD on supernode timing** and uniquely positioned inside China by mandate + price (~1/4 the cost / ~2.87x H20 inference, per Huawei).

**Why the landscape is this way (2nd order).** US export controls ([[Nvidia halves list of Asia buyers over China chip export curbs]]) **created the demand** the Atlas 950 fills: with Nvidia's China channel shrinking and Beijing mandating domestic chips, Huawei has a captive, government-backed market regardless of per-chip inferiority. The controls meant to starve Chinese compute are **subsidizing the domestic substitute's scale** — the same paradox flagged in the Nvidia-buyer-list note.

## [2] Company history / fit
Trajectory: Ascend 910B/910C (mass shipments 2025, ~SMIC N+2 7nm) → **Atlas 900 A3 SuperPoD** → **Atlas 950 SuperPoD unveiled Huawei Connect Sept 2025** (20x the NPUs of the 900 A3) → **Mar 2026** first overseas showcase → **Jul 16 2026** public physical display at WAIC/Shanghai + Korea-entry press → **Q4 2026** planned availability + Korea launch (distributors Hansol PNS, SK Shieldus). Fits Huawei's post-sanctions pivot: build a **vertically-integrated, US-independent AI stack** (own NPU, own HBM "HiZQ 2.0" 144 GB, own interconnect, own cloud).

**Why the company acts this way.** Structural pressure: cut off from Nvidia, EUV, and (increasingly) foreign HBM, Huawei's only path to relevance in AI compute is **self-sufficiency by any node it can get** — hence in-house HBM (bypassing memory export curbs), proprietary UnifiedBus (no reliance on NVLink/InfiniBand), and scale-out to mask weaker silicon. The Korea push is the first attempt to **monetize that stack outside the protected home market** — a test of whether "cheap + big" beats "fast + CUDA" where buyers have a choice.

## [3] Novelty / value-add / traction
**What's genuinely new (little):** The Atlas 950 SuperPoD itself is a **Sept-2025 announcement re-surfaced**; the July-2026 increment is a public hardware showing + a *plan* to sell in Korea. **No shipping product, no named customer, no deployed benchmark** as of the news date. The "1,152 TB" is explicitly theoretical. This is **announced, not adopted**.

**Traction reality.** Domestically Ascend has real pull (Beijing procurement mandates, DeepSeek reportedly stress-testing on Ascend 950), but the **Atlas 950 SuperPoD as a delivered system has zero disclosed external deployments**. Korea faces stated headwinds: security/geopolitical sensitivity to Chinese silicon, power/heat overhead of dense sub-leading-edge chips, and proprietary-stack lock-in.

**Who captures the value / what breaks it (2nd order).** Huawei's bet is that **at the system/TCO level, "many cheap NPUs + own HBM + own fabric" undercuts Nvidia on $/useful-FLOP inside China and in price-sensitive third markets** — even if each chip is worse. What breaks it: (a) **software** — CUDA lock-in and CANN's immaturity make porting costly, so the price advantage is partly eaten by migration/engineering cost; (b) **power/space** — 160 cabinets / 1,000 m² / all-optical is a massive TCO and siting burden that only makes sense where power is cheap and Nvidia is unavailable; (c) **HBM/yield ceiling** — domestic HBM (CXMT ~2M stacks/2026) and SMIC N+2 (~750K Ascend 950/yr) **cap how many of these SuperPoDs Huawei can actually build**, so scale-headline ≠ volume.

## [4] What's next / market sentiment
- **Plans:** Q4-2026 GA of Atlas 950 + Ascend 950DT (cloud from ~Aug 2026); Korea commercialization via Hansol PNS / SK Shieldus; roadmap to Atlas 960 / Ascend 960 (2027) and larger "SuperCluster" (Huawei touts an Atlas 950 SuperCluster at ~1 ZettaFLOPS FP4 from hundreds of thousands of NPUs).
- **Sentiment:** in the West, read as a **scale-flex with real per-chip caveats**; the note's "still behind Nvidia's Vera Rubin" is the consensus. In China, read as a compute-sovereignty milestone.
- **Risks:** production ceiling (SMIC/HBM), software ecosystem gap, power/heat/footprint, and **geopolitical resistance abroad** (Korea security sensitivity) — plus the risk that "announced Q4-26" slips.

**Why the market goes this way / counterintuitive.** The instinctive read ("8,192 chips, 8 EFLOPS — China caught up") is **misleading**: the headline is a scale artifact, not a node/per-chip breakthrough, and the binding constraint is **manufacturing volume (HBM + N+2 wafers), not design.** Counterintuitively, the more Nvidia is walled out of China, the more the Atlas 950's *weakness* (needs huge chip counts) becomes a *strength of narrative* — but the same walls (no EUV, limited HBM) that create the demand also **cap Huawei's ability to supply at scale.** The story that matters is not the EFLOPS number; it's **whether Huawei can build enough SuperPoDs, and whether anyone outside the mandated home market actually buys one.**

## Sources
- Tom's Hardware (Korea entry, 8,192 Ascend 950, 2.87x H20 @ 1/4 cost): https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment-reportedly-challenges-nvidia-dominance-with-tripled-inference-performance-of-h20-at-one-quarter-the-cost
- Tom's Hardware (Atlas 950 SuperCluster / 1 ZettaFLOPS FP4): https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-unveils-atlas-950-supercluster-touting-1-fp4-zettaflops-performance-for-ai-inference-and-524-fp8-exaflops-for-ai-training-features-hundreds-of-thousands-of-950dt-apus
- Huawei Central (6.7x compute vs NVL144, specs, 160 cabinets, Q4-26): https://www.huaweicentral.com/huawei-atlas-950-superpod/
- Huawei (Sept 2025 keynote, SuperPoD interconnect): https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech
- TechRadar (Atlas 950 vs Nvidia DGX vs AMD MegaPod, availability late-2026 / 2027): https://www.techradar.com/pro/huawei-atlas-950-superpod-vs-nvidia-dgx-superpod-vs-amd-instinct-mega-pod-how-do-they-compare
- TechRadar (MWC 2026 debut): https://www.techradar.com/pro/huawei-debuts-its-atlas-950-ai-superpod-at-mwc-2026-taking-the-ai-data-center-fight-to-nvidia-and-amd
- Seoul Economic Daily (Jul 17 2026 public showing / WAIC): https://en.sedaily.com/international/2026/07/17/huawei-unveils-atlas-950-superpod-linking-thousands-of-ai
- TrendForce (Q4-26 Korea launch plan): https://www.trendforce.com/news/2026/07/02/news-huawei-reportedly-plans-4q26-korea-launch-of-ascend-ai-chips-and-atlas-950-superpod-as-nvidia-alternative/
- SemiAnalysis (HBM bottleneck, production ramp): https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp
- abit.ee (Ascend 950DT 144GB HiZQ 2.0 HBM, 4 TB/s, cloud Aug 2026): https://abit.ee/en/processors/huawei-ascend-950dt-ai-chip-ai-accelerator-huawei-cloud-machine-learning-ascend-950-en
- Spheron (Ascend 950 vs Nvidia B300/B200 per-chip): https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/
- Internal: [[Nvidia halves list of Asia buyers over China chip export curbs]], [[China's LineShine supercomputer declared world's fastest]], [[Huawei Cloud expands Egypt fintech infrastructure presence]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions (second-order)

1. **Is this even a new event?** No — the Atlas 950 SuperPoD (same 8,192 chips / 8 EFLOPS FP8 / 16 EFLOPS FP4 / 1,152 TB specs) was **unveiled at Huawei Connect in Sept 2025**, showcased overseas at MWC/Mar 2026, and only *physically displayed* at WAIC Shanghai on 2026-07-16. — **Answered: the specs are a ~10-month-old re-announcement; only the public hardware showing + Korea-entry plan are 2026-new. Leans STALE as a "new event."**

2. **System EFLOPS vs per-chip — where's the trick?** The 8 EFLOPS FP8 / "6.7x Nvidia" is a **scale artifact**: 8,192 chips vs Nvidia's 144 (~57x more). Per-chip, Ascend 950DT trails Blackwell badly (~780 vs ~2,500 TFLOPS BF16; 144 vs 192 GB; 3.2–4 vs 8 TB/s). — **Answered: no per-chip leadership.**

3. **Announced or shipping?** Announced. **Availability Q4 2026; zero disclosed external deployments; no named customer for a delivered SuperPoD.** — **Answered: not GA, not adopted.**

4. **Is the 1,152 TB memory real?** The source itself flags it "in theory" (full-config). — **Answered: theoretical max, not a delivered benchmark.**

5. **What actually caps this — design or manufacturing?** Manufacturing. SMIC N+2 (~7nm) ≈ 750K Ascend 950/yr; domestic HBM (CXMT) ≈ 2M stacks/2026. **Volume, not design, is the binding constraint.** — **Answered.**

6. **Does the price claim (~1/4 Nvidia, ~2.87x H20 inference) survive software cost?** Partly eaten by **CUDA lock-in / CANN immaturity** — porting/engineering cost offsets sticker savings. — **Open (analysis): $/useful-FLOP net of migration is undisclosed.**

7. **Is there any real traction, even domestically?** Ascend has mandate-driven pull (Beijing procurement, DeepSeek reportedly testing on Ascend 950), but **the Atlas 950 SuperPoD system has no disclosed live external deployment.** — **Answered: chip yes-ish, SuperPoD no.**

8. **Will the Korea push work?** Q4-2026 *plan* via Hansol PNS / SK Shieldus; faces security sensitivity to Chinese silicon, power/heat overhead, proprietary-stack lock-in. — **Open: unproven, and still a plan not a sale.**

9. **What's the TCO reality of 160 cabinets / 1,000 m² / all-optical?** Massive power + siting burden; only rational where power is cheap and Nvidia unavailable. — **Open (analysis): TCO likely only competitive inside China.**

10. **Does this duplicate a corpus note?** No literal duplicate exists (no prior Atlas 950 note), but it re-runs the "China compute self-sufficiency via scale" theme of [[China's LineShine supercomputer declared world's fastest]] and is the supply-side mirror of [[Nvidia halves list of Asia buyers over China chip export curbs]]. — **Answered: adjacent, not duplicate; but a re-announcement.**

11. **Who is Huawei silent about?** Delivered benchmarks (vs theoretical peaks), real yield/production volume, power draw, software-porting cost, and any actual customer. — **Open.**

12. **Does the "still behind Vera Rubin" caveat hold?** Yes — Nvidia's next-gen leads per-chip and on the fabric+software stack; Huawei leads only single-box scale on a footprint/power penalty. — **Answered.**

13. **Second-order: do export controls help or hurt Huawei here?** Both — they **create captive mandated demand** (helps narrative/scale) but **the same walls (no EUV, limited HBM) cap supply** (hurts volume). — **Answered (analysis).**

14. **What would move importance up?** A named external Atlas 950 deployment, a delivered third-party benchmark, or a firm Korea/overseas sale — none present. — **Open.**

15. **Does it change the central question?** Yes — from "did China catch up on AI compute?" (headline says yes) to **"can Huawei actually build enough SuperPoDs (HBM/wafer-limited), and will anyone outside the mandated home market buy one?"** — that's where the real weight sits, and both are unanswered.

**Importance: 2/5 — rationale.** The underlying product is a **Sept-2025 re-announcement** re-surfaced on a July-2026 public-showing / Korea-plan peg; there is **no shipping system, no named customer, no delivered benchmark**, the flagship numbers are **scale artifacts** (8,192 chips) rather than per-chip advances, and the "1,152 TB" is explicitly theoretical. It matters as a **compute-sovereignty signal** (real, mandate-backed domestic demand; in-house HBM bypassing memory curbs) and pairs cleanly with the Nvidia-export-curb note, but as a discrete news event it is announced-not-adopted and largely a re-run. Would rise to 3–4/5 only on a delivered deployment, a real third-party benchmark, or a confirmed overseas sale.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Data-center AI accelerator market, sized (definitions vary widely) at ~$25bn (IDC "data-center accelerator") to ~$48.9bn ("AI accelerator chips") for 2026 per secondary market-research citations (via straitsresearch / coherentmarketinsights, as of 2026) — treat as directional, not precise. Nvidia's Feb-2026 quarterly Data Center revenue alone was $62.3bn (+75% YoY, per Nvidia earnings via siliconanalysts), which dwarfs most "market size" figures and shows how definition-dependent TAM is here → [UNSOURCED] single clean TAM. Structure: heavily consolidated globally — Nvidia holds ~80–85% of data-center AI accelerators by revenue in 2026, down from ~92% in 2023 (per Silicon Analysts). But the market is *bifurcating* along the US-China decoupling line: inside China Nvidia's share fell from ~95% to ~55% over 2024–25 (IDC via Reuters/Medium) and is projected toward ~$12–14bn / declining as domestic silicon absorbs demand. Barriers = capital (fabs/HBM), software lock-in (CUDA), and — for Chinese entrants — export controls on EUV/HBM/advanced tooling. Why now: the Apr-2025 H20 export ban plus a Sep-2025 directive for Chinese firms to stop buying Nvidia GPUs created a *captive* domestic market for Huawei Ascend that does not require performance parity to win (per SemiconductorX / CFR).

**Competitive landscape.** Sector KPIs: system-level FLOPS (FP8/FP4), memory capacity & bandwidth (HBM GB, TB/s), interconnect bandwidth, perf-per-watt, and — critically for China — units shippable given HBM supply. Key players: Nvidia (incumbent, NVL144 / Vera Rubin roadmap H2-2026), AMD, and China's Huawei Ascend as the domestic disruptor; basis of competition globally = per-chip performance + software ecosystem; inside China = availability + cost + "good-enough at cluster scale." Recent moves: Atlas 950 SuperPoD debuted at MWC 2026 (Mar 2026), reportedly going overseas (Korea launch planned 4Q26, per TrendForce). Huawei's play is *scale-out over per-chip parity*: the note's own spec — 8,192 chips, 8 EFLOPS FP8, up to 1,152 TB memory — is Huawei's claimed answer to a weaker single chip (Ascend 950PR ~1.56 PFLOPS FP4, 112GB HBM-class memory at 1.4 TB/s vs Nvidia B200's ~20 PFLOPS NVFP4 and 8 TB/s, per Tom's Hardware / Spheron). Huawei claims the SuperPoD fields ~56.8× more NPUs and ~6.7× the aggregate compute of Nvidia's H2-2026 rack, and ~2.87× H20 inference per chip (vendor claims — de-PR: brute-force node count, not efficiency). Position: **catching up / niche-by-mandate** — a distant #2 on technology but structurally advantaged inside China. Moat = policy-protected domestic demand + CUDA-compatible stack lowering migration friction (analysis); NOT a technology moat.

**Comps & multiples.** Huawei is a private, unlisted conglomerate — no market cap, no segment financials disclosed → EV/Revenue, EV/EBITDA, P/E all **no data / [UNSOURCED]**. Demand-side sizing (unaudited, secondary): Chinese hyperscaler Ascend demand ~$12–15bn for 2026; ByteDance reportedly committed $5.6bn in orders; ~600k–750k Ascend units targeted for 2026 (SemiAnalysis / FourWeekMBA / TrendForce) — figures are analyst estimates, not company-confirmed. Internal comps from base (adjacent, not valuation-comparable): [[Micron quarterly profit jumps 15-fold]] (memory-cycle read-through — AI HBM demand), [[Fireworks AI raises $1.5B at $17.5B valuation]] (US inference-layer megaround, $1bn+ ARR — the demand side Ascend serves), [[MTS Early Sol capability impressions and Cerebras serving path]] (alt-accelerator co-design), [[Xi Jinping endorses open-source AI at World AI Conference]] (China compute-sovereignty policy backdrop), [[Huawei Cloud expands Egypt fintech infrastructure presence]] (Huawei's own downstream distribution). Multiples: distribution not computed — no comparable public valuation figures.

**Risk flags.**
1. **HBM supply is the binding constraint, not compute.** Domestic CXMT HBM output is projected at ~2M stacks in 2026 — enough for only ~250–300k advanced Ascend packages, well below the 600k–1.6M die-level ambition (SemiAnalysis / Tom's Hardware). SMIC 7nm-class yields on large NPU die reportedly ~20–40%. Second-order: the 8,192-chip "8 EFLOPS" headline is largely *theoretical* (the note itself says "in theory") — real deployable clusters are gated by HBM and yield, so announced capability ≠ shipped capacity.
2. **Policy-dependent demand = policy-reversible demand.** Ascend's share gain is driven by the H20 ban and the Sep-2025 no-Nvidia directive, not by winning on merit. Any easing of US export policy or Chinese re-authorization of Nvidia would re-expose Huawei to a superior product (per CFR/CSIS). Concentration risk on a handful of state-aligned hyperscalers (ByteDance, Alibaba, Tencent).
3. **Power/TCO penalty at scale.** Winning via 56.8× more NPUs means far higher power draw, footprint and interconnect complexity per unit of useful compute — a real cost/energy disadvantage that the "6.7× total compute" framing hides (analysis).

**What this changes (idea-lens).** Confirms a durable *bifurcation* of the accelerator market: a Nvidia-led global stack and a policy-walled Chinese domestic stack where Huawei is the default winner regardless of parity (analysis). Falsifiable thesis: Huawei's real 2026 constraint is HBM/yield, not design — so Ascend shipments will materially undershoot the die-level targets. Watch: CXMT HBM output disclosures, the 4Q26 Ascend 950DT / Korea launch (first real export test), and any US–China chip-policy thaw — the latter would be the clearest catalyst to break the "captive demand" moat.

Sources: https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment · https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/ · https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026 · https://www.trendforce.com/news/2026/07/02/news-huawei-reportedly-plans-4q26-korea-launch-of-ascend-ai-chips-and-atlas-950-superpod-as-nvidia-alternative/ · https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp · https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-chip-champions-ramp-up-production-of-ai-accelerators-at-domestic-fabs-but-hbm-and-fab-production-capacity-are-towering-bottlenecks · https://www.cfr.org/articles/chinas-ai-chip-deficit-why-huawei-cant-catch-nvidia-and-u.s.-export-controls-should-remain · https://fourweekmba.com/ai-nvidia-huawei-ascend-china-ai-chip-demand-decoupling/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
