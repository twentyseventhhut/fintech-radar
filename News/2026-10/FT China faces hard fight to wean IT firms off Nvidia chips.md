---
title: "FT: China faces hard fight to wean IT firms off Nvidia chips"
date: 2026-10-27
retrieved: 2026-10-27
tags:
  - company/nvidia
  - industry/ai
  - region/asia
  - type/commentary
sources:
  - https://www.ft.com/content/9dbd99db-6b0c-43bd-b7be-849f129df098
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: seedbd55e
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# FT: China faces hard fight to wean IT firms off Nvidia chips

> [!info] 2026-10-27 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] FT: Китаю предстоит нелегкая борьба, чтобы отучить IT-компании от использования чипов Nvidia

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.ft.com/content/9dbd99db-6b0c-43bd-b7be-849f129df098>

## Контекст

<!-- enrichment:context -->
**[0] What this is.** An FT commentary/analysis piece (2026-10-27) arguing that despite Beijing's directives, China faces a *hard fight* weaning its IT firms off Nvidia. The gap is structural, not political: Nvidia still leads on raw performance (the Huawei Ascend 910C trails the H200, and Huawei is not expected to match H200-class performance until ~end of 2027), and Nvidia's CUDA software moat keeps top labs (DeepSeek and others) on its stack for frontier training. Beijing's answer is a two-track squeeze — restrict/approve foreign chips narrowly while forcing domestic adoption — but the "wean" is friction-heavy.

**[1] Policy timeline (dated).**
- Sep 2025 — China's internet regulator ordered major tech firms (Alibaba, Baidu, ByteDance) to halt Nvidia AI-chip purchases and pivot to domestic silicon (see [[China orders tech giants to halt Nvidia AI chip purchases]]).
- Nov 2025 — Beijing banned foreign AI chips in *state-funded* data centers, requiring domestic-only hardware in government-backed compute.
- Jan 2026 — Chinese customs told agents H200 chips were "not permitted" to enter despite US BIS export licenses; Beijing told firms to halt H200 orders (see [[This Week in Fintech The cost of US tech export controls]]).
- Feb 2026 — US granted Nvidia a license to ship H200 to China, but subject to a 25% US import tariff; Beijing then allowed narrow re-entry, restricting approved H200 to *training only* and steering firms to domestic chips (chiefly Huawei Ascend) for routine inference.
- Sep 2026 — MIIT's 15th Five-Year Plan: target 9,800 exaflops of AI compute by 2030 (~5x current), backed by ~$300–530B, with a reported ≥80% domestic-hardware threshold that would leave Nvidia/AMD little room.

**[2] Domestic alternatives — live vs announced.**
- *Huawei Ascend* is the flagship. Ascend revenue reportedly grew ~6x in three years (~$2B 2023 → ~$12.1B 2026), almost entirely inside China; by volume Ascend is now claimed to have surpassed Nvidia *within China* — but volume masks a per-chip performance deficit (910C < H200). Related: [[China's Huawei hypes up chip and computing power plans]] signals.
- *Hyperscaler self-silicon*: Alibaba + China Telecom stood up a data center with ~10,000 Alibaba "Zhenwu" chips (Apr 2026); ByteDance is building custom CPUs for AI infra (see [[ByteDance develops custom CPUs to power AI infrastructure]]) and a CUDA-compat agent.
- *Software moat erosion*: DeepSeek released open tooling for Ascend built around a language it calls simpler than CUDA; DeepSeek is also designing its own inference chip (targeted 2027, likely 2028). This directly attacks the CUDA lock-in the FT piece flags as Nvidia's real moat.
- *Supply-chain context*: the squeeze runs both ways — US fears ASML EUV tooling leaked into China (see [[US fears ASML's top chip tool ended up in China]]); China is simultaneously anti-dumping-probing US analog chipmakers (TI, Analog Devices).

**[3] Nvidia exposure (numbers).** Pre-controls, China was ~20–25% of Nvidia data-center revenue (~$10–15B/yr at FY25 run-rate). The H20 ban (Apr 2025) drove a ~$4.5B inventory charge and cost ~$8B of H20 revenue in Q2 FY26 guidance; Nvidia now assumes *zero* China data-center compute revenue in its outlook. Its China training-GPU share fell from ~95% toward ~zero. So the "hard fight" cuts both ways: China struggles to replace Nvidia at the frontier, while Nvidia has already written China out of its model — a mutual decoupling.

**[4] Fintech / infrastructure relevance.** This is an infrastructure-sovereignty story with direct fintech read-through. Chinese financial institutions (banks, securities, insurers) are a prime domestic-compute customer: at the 2026 China International Financial Expo, domestic high-compute firms (Hygon, Muxi, Zhaoxin, Phytium) led, and Hygon reportedly covers compute for >90% of financial scenarios. State-owned banks are reportedly tying vendor pay to latency/throughput SLAs — i.e., the chip shift is becoming a procurement/SLA question for core banking and fraud/risk inference. China's generative-AI-in-fintech market is sized ~$4.7B (2026). The broader signal for Western fintech infra: custom AI silicon (AWS Trainium — see [[AWS in talks to sell Trainium AI chip racks to outside companies]]) is eroding Nvidia's grip globally, so "sovereign/alternative compute" is now a cost and resilience theme well beyond China.

Sources: https://www.ft.com/content/9dbd99db-6b0c-43bd-b7be-849f129df098 · https://thediplomat.com/2026/02/nvidias-h200-chips-re-enter-china-but-beijing-isnt-giving-up-on-huawei/ · https://www.notebookcheck.net/Ascend-AI-chips-surpass-Nvidia-in-China-as-Huawei-weans-off-American-tech.1418406.0.html · https://www.cnbc.com/2026/04/08/china-alibaba-data-center-ai-chips-zhenwu.html · https://www.fdd.org/analysis/2025/11/10/signaling-confidence-in-its-domestic-industry-china-bans-foreign-ai-chips-in-state-funded-data-centers/ · https://easternherald.com/2026/09/08/china-miit-ai-infrastructure-plan-us-chip-restrictions-2030/ · https://finance.biggo.com/news/c02374dc-a764-4829-bfd9-72915e6798ff · https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000052/nvda-20260426.htm · https://news.futunn.com/en/post/74688082/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team the FT thesis ("China faces a hard fight to wean IT firms off Nvidia").**

1. *Is the "hard fight" framing accurate, or is weaning already succeeding?* Partly already succeeding on **volume/inference** (Ascend reportedly outsells Nvidia in-China by unit; state data centers mandated domestic) but the fight is real at the **frontier/training** tier where CUDA + H200-class performance still dominate. Both can be true. — answered.
2. *Does Ascend actually match Nvidia?* No. 910C trails H200; Huawei not expected to reach H200-class until ~end-2027. Volume leadership ≠ performance parity. — answered.
3. *Is the CUDA moat really breaking?* Being *attacked*, not yet broken: DeepSeek's open Ascend tooling + ByteDance's CUDA agent target the scarce-talent cost of porting, but top labs still train on Nvidia. Trajectory uncertain. — open/answered-partial.
4. *How reliable are the Ascend revenue figures (~$2B→$12.1B)?* Third-party estimates (press/analyst), not audited Huawei disclosure; treat as directional. — open.
5. *Could Beijing reverse and re-admit Nvidia?* It already did a narrow H200 re-admission (Feb 2026, training-only, 25% US tariff). Policy is oscillating, not monotonic — "wean" is deliberately partial to keep frontier access. — answered.
6. *What's Nvidia's real China exposure?* Pre-ban ~20–25% of data-center rev (~$10–15B/yr); now guided to ~zero China DC compute. So Nvidia has largely pre-absorbed the loss — the narrative risk is already priced. — answered.
7. *Is this a duplicate of prior notes?* The *theme* is covered ([[China orders tech giants to halt Nvidia AI chip purchases]], [[This Week in Fintech The cost of US tech export controls]], [[ByteDance develops custom CPUs to power AI infrastructure]]), but this is a fresh dated FT synthesis of the current state (Oct 2026), not a re-report of one event. → fresh. — answered.
8. *Fintech relevance — is it a stretch?* Not for China: financial institutions are a named domestic-compute customer (Hygon >90% of financial scenarios; bank SLA-linked procurement). For Western fintech it's an analogy to the Trainium/custom-silicon cost theme. — answered.
9. *Counter-view: does export control actually accelerate Chinese self-sufficiency (backfire)?* Strong case yes — controls created the forced market that funds Huawei/SMIC/Alibaba silicon; multiple analysts argue controls are an industrial-policy own-goal. — answered.
10. *Manufacturing bottleneck ignored?* Yes — the binding constraint is advanced fab/EUV (SMIC yields, ASML tooling access, HBM supply), not chip *design*. Design catch-up ≠ volume at leading nodes. Under-covered in the headline framing. — open.
11. *Is "IT firms" the right frame vs "AI labs"?* The pain concentrates in frontier AI training (a handful of labs), not all IT firms; most inference/enterprise workloads can already run domestic. The headline over-generalizes. — answered.
12. *Second-order: does this threaten Nvidia globally or just China?* Mostly China-contained near-term, but the self-sufficiency playbook + custom silicon (AWS Trainium, hyperscaler ASICs) is a global margin threat to Nvidia over time. — answered.
13. *Any direct named fintech company impact here?* No single fintech is named in the FT piece; relevance is infrastructure/sovereign-compute and Chinese bank procurement — thematic, not company-specific. — answered.
14. *Data freshness risk?* Fast-moving policy; H200 terms, tariffs, and Ascend numbers can shift within weeks — figures are as-of Oct 2026. — flagged.

**Importance: 3/5 — a well-sourced, decision-relevant macro/infrastructure theme (AI-chip sovereignty, export-control decoupling, CUDA moat) with real fintech read-through (Chinese bank/insurer domestic compute; global custom-silicon cost pressure), but it is FT commentary with no new hard event, no named fintech actor, and the core facts are already captured across several prior notes — so informative context rather than a market-moving item.**
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits in AI-compute infrastructure — the silicon/datacenter layer that fintech AI ultimately rents, not builds. Size: global AI-datacenter capex is running near ~$800bn–$1trn in 2026 (PwC Global Data Centre Outlook sees ~$800bn/yr in 2026 rising to ~$1.1trn by 2030; Goldman/BofA peg 2026 AI spend near $1trn), with PwC's central scenario at $31.6trn cumulative through 2050 (per PwC/Goldman/BofA, via press, as of Oct 2026). Structure: highly consolidated at the accelerator layer — Nvidia has historically dominated training compute, with the moat in CUDA software + supply allocation, not just the die. Why now: this is a geopolitically-forced de-consolidation of the China slice. US export controls restrict which Nvidia parts can legally ship, and in Sep 2025 Beijing told domestic tech giants to cancel outstanding H20 orders on "security" grounds, then (per the corpus) treated even licensed H200s as "not permitted" at customs in early 2026 — a two-sided wall closing the China workaround.

**Competitive landscape.** KPIs the segment runs on: accelerator units shipped, in-country market share, datacenter revenue, and software-ecosystem lock-in (CUDA vs Huawei CANN). Key players: Nvidia (incumbent), Huawei Ascend (domestic champion), with Alibaba/Baidu building in-house silicon (per corpus [[China orders tech giants to halt Nvidia AI chip purchases]]); the US-side custom-ASIC wave (AWS Trainium, Broadcom co-design) is the parallel non-China disintermediation vector [[AWS in talks to sell Trainium AI chip racks to outside companies]]. Recent moves with dates: Nvidia's China datacenter-AI share fell to ~34% in H1 2026, with Bernstein forecasting a collapse from ~40% to ~8% by end-2026 (per Bernstein, via Reuters/US News, 12 Oct 2026). Huawei shipped 572,000 AI accelerators in H1 2026 for ~28% share, with Ascend revenue projected ~$12bn in 2026, +60% from $7.5bn in 2025 (per reports via Benzinga/US News, Oct 2026). Protagonist's position inside China: losing — incumbent abroad, structurally shut out at home; moat (CUDA + allocation) is being bypassed by state fiat, not out-competed on merit (analysis).

**Comps & multiples.** Not a valuation event — no deal/round/metric in the note; it's FT commentary. Nvidia market-cap/forward multiples not re-derived here (no clean free EV/EBITDA figure in-source → [UNSOURCED]). The load-bearing arithmetic is exposure, not multiples: China H200 sales were <1% of datacenter revenue in the Jul-2026 quarter, and management reiterated ~zero China datacenter-compute in the outlook (per Nvidia 10-Q / earnings commentary, SEC, Jul–Oct 2026), against record total datacenter revenue of $51.2bn in Q3 FY2026, +66% YoY (per Nvidia / Futurum, 2026). So the directly-at-risk China slice ≈ <$0.5bn/qtr vs $51.2bn total = the ban removes a slice Nvidia has largely already written to zero. Internal comps (corpus): [[China orders tech giants to halt Nvidia AI chip purchases]], [[This Week in Fintech The cost of US tech export controls]], [[US fears ASML's top chip tool ended up in China]], [[Stanford HAI 2026 AI Index shows capability outpacing governance]]. Distribution not computed — qualitative. Flag: in-line with a story already priced out of Nvidia's China number; the open question is second-order (ecosystem), not Nvidia's near-term China revenue.

**Risk flags.**
- Bifurcated compute stack: a CUDA-world vs a CANN/Ascend-world split means any fintech AI serving China users may face a separate, non-portable model/inference supply chain — a hidden compliance + re-engineering cost, not a one-off (why: software lock-in doesn't travel across the chip wall).
- "Hard fight" = demand-side friction, not just supply: the FT framing (and the corpus H200-at-customs detail) implies Chinese firms still prefer Nvidia on performance/software, so domestic substitution risks a capability gap — China-based AI-compute could run slower/costlier than the global frontier, a drag on any fintech-AI built on it (second-order: higher cost-per-inference onshore).
- Concentration cuts both ways: outside China, Nvidia's dominance + the custom-ASIC push (Trainium/Broadcom) means fintech-compute buyers face either single-vendor pricing power or a fragmenting accelerator field with portability risk — margin and roadmap exposure sit with whoever controls the stack layer, not the app.

**What this changes (idea-lens).** For AI-infrastructure: the China AI-compute market is de-coupling into a protected domestic pool (Huawei to ~50% share by end-2026 per Bernstein) — a durable second ecosystem, not a temporary outage (analysis). Falsifiable thesis: if Huawei Ascend revenue clears ~$12bn in 2026 and share holds >40% through 2027, the split is structural and fintechs serving both markets must dual-source AI compute; trigger to watch — Chinese cloud/fintech capex disclosures naming Ascend vs Nvidia, and any relaxation of the H200 customs block. What breaks the thesis: a US-China chip détente that reopens licensed Nvidia flow at scale, which would re-collapse the domestic premium (analysis).

Sources: https://www.ft.com/content/9dbd99db-6b0c-43bd-b7be-849f129df098 · https://money.usnews.com/investing/news/articles/2026-10-12/nvidias-china-ai-chip-share-falls-as-huawei-closes-gap-report-finds · https://www.benzinga.com/markets/tech/26/10/62319484/nvidia-loses-ground-in-china-as-huaweis-ai-chip-shipments-nearly-double-capturing-28-market-share-report · https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm · https://futurumgroup.com/insights/nvidia-q3-fy-2026-record-data-center-revenue-higher-q4-guide/ · https://www.pwc.com/gx/en/news-room/press-releases/2026/global-investment-in-ai-infrastructure.html · https://www.kucoin.com/news/flash/nvidia-s-h200-chip-sales-to-china-account-for-less-than-1-of-data-center-revenue
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
