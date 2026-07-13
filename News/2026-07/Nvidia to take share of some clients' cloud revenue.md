---
title: "Nvidia to take share of some clients' cloud revenue"
date: 2026-07-06
retrieved: 2026-07-06
tags:
  - company/nvidia
  - industry/ai
  - industry/infrastructure
  - region/us
  - type/commentary
sources:
  - https://www.theinformation.com/articles/nvidia-says-will-take-cut-customers-cloud-revenues
status: published
n_mentions: 1
channels:
  - "42 секунды"
story_id: sb997cec5
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# Nvidia to take share of some clients' cloud revenue

> [!info] 2026-07-06 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] The Information: Nvidia заявляет, что будет получать часть облачных доходов некоторых клиентов

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.theinformation.com/articles/nvidia-says-will-take-cut-customers-cloud-revenues>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Nvidia to take share of some clients' cloud revenue
_Analytical notes (not a post). Importance: 4/5._

**FRESHNESS VERDICT: FRESH.** This is a genuinely new development — Nvidia formalizing a revenue-sharing + GPU-backstop *financing vehicle* (announced ~2026-07-01), not a re-run. Distinct from adjacent corpus notes: it is not the [[Kazakhstan and US firm Firebird sign $10B Nvidia-backed AI deal]] (a single sovereign buildout), not [[Amazon raises AWS GPU reservation prices about 20% amid chip shortage]] (hyperscaler pricing), and not [[Meta plans cloud business selling AI compute and models]] (a hyperscaler monetizing its own excess compute). Here the twist is that the *chip vendor itself* takes an ongoing cut of its *customers'* cloud revenue. No prior note covers this mechanism.

## [0] What exactly happened (de-PR'd)
- Nvidia unveiled an **optional financing model** in which it (a) sells GPUs as usual, (b) **backstops** the customer's idle capacity — agreeing to rent/buy back unused GPUs at a pre-set price — and (c) **takes a recurring share of the cloud revenue** the supported capacity generates. Nvidia's framing: "a recurring, usage-linked earnings stream" diversifying it beyond one-time chip sales.
- **First named partners: Sharon AI and Firmus Technologies**, committing to **~210,000 Grace Blackwell GB300 GPUs** across Australia (Sharon AI, 6-yr, 72 MW scaling to ~40k GPUs) and Indonesia (Firmus, Batam campus scaling to 360 MW / up to 170k GPUs), built to Nvidia's DSX "AI factory" design.
- The 42 Секунды digest line ("The Information: Nvidia will take part of some clients' cloud revenues") tracks The Information's report ("Nvidia Will Backstop Customers' GPUs, Take a Cut of Their Cloud Revenues").
- **De-PR'd:** the "recurring revenue" gloss hides that this is **vendor financing** — Nvidia underwrites the residual-value risk lenders won't (GPUs depreciate fast, resale is thin), making otherwise-unbankable neocloud buildouts financeable. **Why structured this way:** capital-constrained neoclouds have demand but can't finance clusters because banks distrust GPU collateral. Nvidia converts its balance sheet + demand visibility into a credit backstop, and prices that risk as a revenue cut → it both *creates* the demand for its chips and *taxes* the downstream cloud. This is the neocloud-scale version of the [[Kazakhstan and US firm Firebird sign $10B Nvidia-backed AI deal]] "Nvidia-backed" pattern, now productized.

## [1] Competitors / peers
- **Vendor-finance analogues:** classic Cisco/Lucent late-1990s vendor financing (which ended badly when demand was partly financially engineered). No direct chip-peer offers this; AMD/Broadcom compete on silicon, not on underwriting customer clouds — so this is a **moat move** as much as a finance move.
- **Circular-financing cluster:** Nvidia's $2B stake in CoreWeave, its $6.3B deal to buy CoreWeave's unused capacity through 2032, and OpenAI/Nebius arrangements are the same flywheel. This note *generalizes* that to any neocloud. Cf. [[Linas Newsletter Coatue's $12 trillion AI bet report]] and [[This Week in Fintech Semafor on the rise of an AI futures market]] for the capex-concentration backdrop.
- **Position:** Nvidia is *ahead* — no competitor can match a backstop underwritten by the dominant chip supplier. **Why:** only the monopoly supplier both controls allocation and has the demand data to price residual risk. Second-order: this deepens dependence, raising antitrust/tying scrutiny risk.

## [2] Company history / fit
- Fits Nvidia's 2025–26 arc of moving up the stack from chips → systems (DSX AI factories) → ecosystem financing (CoreWeave stake, Firebird, Inception program). **Why:** as chip gross margins face eventual normalization and demand-durability doubts, Nvidia wants *annuity* revenue and wants to remove financing as the bottleneck throttling its own unit sales. Take-rate on downstream cloud = software-like multiple on top of hardware.

## [3] Novelty / value-add / traction
- **New:** yes — a chip vendor taking equity-like exposure to its customers' *operating* revenue is novel at this scale. **Traction:** thin so far — one announcement, two partners (Sharon AI, Firmus), 210k GPUs *committed* not yet live. Terms (the exact revenue % and buyback prices) are **undisclosed** — the key economics are the silence.
- **Value-add real?** For neoclouds: real (unlocks financing). For Nvidia: real *only if* the usage-royalty exceeds the working-capital cost of buyback guarantees. **Who captures the margin:** Nvidia captures hardware margin + a cloud-revenue tax + optionality; the neocloud bears operating risk but offloads residual-value risk. Breaks if GPU utilization disappoints (Nvidia then owns idle depreciating assets it must rent back).

## [4] What's next / market sentiment
- **Skepticism is the story.** Analysts (e.g., Wedbush's Matthew Bryson) flag **circular financing** — Nvidia backstops buyers who buy Nvidia chips, making demand look organic when it's financially engineered. Bull case: a "flywheel" underwriting the AI buildout. Bear case: "vendor-finance risk" concentrating credit risk on Nvidia's balance sheet at the top of a capex cycle.
- **Why the market goes this way (analysis):** the model quietly moves demand-risk from customers to Nvidia. Counterintuitive second-order effect — this makes Nvidia's reported growth look *safer* while actually making it *more fragile*, because a neocloud/utilization downturn now hits Nvidia twice (lost sales + buyback obligations). Central question shifts from "is AI demand real?" to **"how much of Nvidia's growth is self-funded, and who eats the residual-value risk when GPUs commoditize?"**

## Sources
- The Information (primary): https://www.theinformation.com/briefings/nvidia-will-backstop-customers-gpus-take-cut-cloud-revenues ; https://www.theinformation.com/articles/nvidia-says-will-take-cut-customers-cloud-revenues
- Tom's Hardware: https://www.tomshardware.com/tech-industry/nvidia-to-take-a-cut-of-ai-cloud-revenue-on-top-of-hardware-sales
- DataCenterDynamics: https://www.datacenterdynamics.com/en/news/nvidia-acts-as-backstop-for-customer-gpus-in-return-for-cut-of-cloud-revenue/
- TechTimes (210k GPUs, Sharon AI/Firmus): https://www.techtimes.com/articles/319704/20260704/nvidia-revenue-sharing-ai-cloud-debuts-210000-gpus-flywheel-vendor-finance-risk.htm
- MLQ News: https://mlq.ai/news/nvidia-launches-gpu-backstop-financing-model-takes-cut-of-cloud-revenue-from-neocloud-partners/
- io-fund (circular financing, CoreWeave/Nebius): https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 4/5** — Nvidia, the single most systemically important AI-cycle company, is productizing vendor financing with a downstream cloud-revenue tax. The mechanism materially reframes how to read Nvidia's revenue durability and concentrates AI-capex credit risk on its balance sheet — high signal for anyone tracking the AI infrastructure bubble question. Held below 5 because traction is one announcement + two sub-scale partners, and the load-bearing economics (revenue %, buyback prices) are undisclosed.

## Top challenge / red-team questions (second-order)
1. What is the actual **revenue-share percentage** and the **buyback/rent-back price** on idle GPUs? Undisclosed — the entire risk-transfer economics hinge on this. **Open.**
2. Is the usage-royalty **recognized as revenue or netted against COGS/financing cost**? Determines whether this flatters Nvidia's growth optics vs. genuinely diversifies it. **Open.**
3. How much of Nvidia's forward revenue is now **self-funded** (Nvidia-backstopped or Nvidia-invested buyers buying Nvidia chips)? Circular-financing scale is the core bear thesis. **Partly open** (analysts flag it; magnitude undisclosed).
4. Who eats **residual-value risk** if GB300 GPUs commoditize faster than expected (AMD/ASIC pressure, next-gen cannibalization)? Nvidia, via buyback obligations — a working-capital and impairment exposure. **Analysis.**
5. Is this **tying/antitrust**-exposed — does financing steer allocation and lock out non-Nvidia silicon? **Open.**
6. Why **Sharon AI and Firmus** (small, APAC) first rather than CoreWeave/Nebius? Signals the tool targets the *un*bankable long tail, not the flagships. **Analysis.**
7. Are the 210k GPUs **committed vs. deployed vs. financed**? Announcement ≠ live capacity. **Committed only.**
8. What happens to Nvidia's balance sheet in a **utilization downturn** — does it simultaneously lose sales AND owe buybacks? Double-exposure fragility. **Analysis.**
9. Does the backstop make GPU clusters genuinely **bankable to third-party lenders**, or does Nvidia just become the lender of last resort? **Open.**
10. How does this interact with **hyperscaler self-supply** ([[Meta plans cloud business selling AI compute and models]], AWS GPU pricing power) — is Nvidia financing the neocloud tail precisely because hyperscalers are pulling in-house? **Analysis.**
11. Is the "recurring, usage-linked earnings stream" a **software multiple** the market will re-rate, or a leverage/credit line the market should *discount*? **Open — the valuation crux.**
12. What's the **contract term and exit** — can a neocloud refinance out of the revenue share once bankable, leaving Nvidia only the downside? **Open.**
13. Does this accelerate or paper over a **demand air-pocket** — i.e., is Nvidia underwriting demand that wouldn't clear at market financing rates? Cf. Cisco/Lucent vendor-finance precedent. **Analysis.**
14. How large could the program scale, and at what point does **concentration of AI credit risk** in one vendor become a systemic (not just Nvidia-specific) concern? **Open.**
15. Duplicate check: is this the same event as [[Kazakhstan and US firm Firebird sign $10B Nvidia-backed AI deal]]? **No** — Firebird is a sovereign buildout; this is a repeatable financing product. **Fresh.**
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-06]] (2026-07-06).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** AI-infra / GPU compute + "neocloud" vendor financing. On 2026-07-01 Nvidia unveiled a revenue-sharing + credit-support model: participating "AI clouds" buy Nvidia infrastructure and Nvidia earns *both* standard product revenue *and* a share of the cloud revenue that supported capacity generates (per Nvidia via Tom's Hardware / DCD / The Information, 2026-07-01..05). First partners Sharon AI and Firmus committed to ~210,000 Grace Blackwell GB300 GPUs across Australia/Indonesia; Sharon AI's contract is 6 years / 72 MW (per DCD, 2026-07). Structure: the GPU-cloud value chain is capital-intensive and consolidating around a single supplier (Nvidia) at the chip layer while the "rental" layer (CoreWeave, Nebius, IREN, Sharon AI, Firmus) is fragmented and thinly capitalized. Why now: neocloud buildouts are increasingly *vendor-financed* — operators layer Nvidia backstop/credit on top of debt + equity to fund GPU purchases they can't otherwise afford, and Nvidia gains a recurring revenue layer that smooths its GPU-refresh-cycle volatility (per Forbes, 24/7 Wall St, 2026-07). Analysts compare the structure to GE Capital equipment financing and to late-1990s telecom vendor financing (per Tech Times / Seeking Alpha, 2026-07).

**Competitive landscape.** Neocloud KPIs: GPU count / MW capacity, utilization, contract backlog, and revenue run-rate vs. lease obligations. Nvidia's position: dominant / effectively the platform — it now captures value twice in one transaction (hardware sale + monthly token revenue share) `(analysis)`. Moat: intangibles (CUDA lock-in) + scale + now financial gatekeeping — Nvidia decides which neoclouds get backstopped, deepening dependence on its rails `(analysis)`. This extends a pattern already visible in the base: Nvidia owns ~7% of CoreWeave and invested $2bn in Jan 2026 to help the debt-laden operator add 5GW (per TechCrunch, 2026-01), the "circular financing" that EU competition staff flagged in Mar 2026 (per Seeking Alpha). Related base signals: [[Amazon raises AWS GPU reservation prices about 20% amid chip shortage]] (hyperscalers ration GPUs — demand backdrop), [[SpaceX signs $150M month compute deal with Reflection AI]], [[Groq raises $650M after Nvidia not-acquihire deal]] and [[OpenAI and Broadcom unveil AI inference chip]] (custom-silicon threat to Nvidia's monopoly), [[Cerebras stock plunges after first earnings on margin outlook]] (AI-hardware margin fragility).

**Comps & multiples.** Pure-play neoclouds (the entities being financed), latest web figures:
- CoreWeave (CRWV): mkt cap ~$59bn; 2026 rev guide $3.0–3.4bn; ~$18.5bn annualized run-rate exit-2026; trades ~3.7x this-year revenue / ~6x NTM revenue / ~10x NTM EBITDA (per Yahoo/Seeking Alpha/Clouded Judgement, 2026). Arithmetic sanity: $59bn / $3.2bn ≈ 18x current-year rev, compressing to ~6x on NTM as run-rate scales — i.e. the multiple is *forward*-justified only if the run-rate ramp is delivered.
- Nebius (NBIS): mkt cap ~$58bn; trades ~18x current-year rev midpoint / ~10x NTM rev / ~20x NTM EBITDA (per Motley Fool / Seeking Alpha, 2026) — richer than CRWV, priced on faster growth.
Internal comp: [[Etched exits stealth at $5B valuation with $1B AI-chip sales]] ($5bn / $1bn = 5x on stated sales). Nvidia itself: valuation multiples not sourced here → `[UNSOURCED]`; the news doesn't quantify the size of the revenue-share cut → "no data" on incremental Nvidia revenue. Read: neocloud names sit *above* mature-hardware ranges (EV/Rev ~0.5–20x) but that is normal for triple-digit growth — flag only if run-rate ramps disappoint.

**Risk flags.**
1. *Circular financing / demand-masking* — Nvidia funds the customers who buy its chips (CoreWeave $2bn stake, now a backstop program), so reported GPU demand may be partly self-generated; if end-user AI demand softens the loop reverses (EU already flagged it Mar 2026). Second-order: a Nvidia revenue miss and neocloud distress would hit simultaneously, not independently.
2. *Counterparty concentration on thin balance sheets* — the revenue-share income depends on under-capitalized neoclouds staying solvent; a neocloud stacking vendor finance on debt has "narrowed its margin for error before serving its first token" (per Tech Times). If utilization falls, Nvidia's cut falls *and* its backstop liability rises at the same moment.
3. *Disintermediation of Nvidia's own monopoly* — custom inference silicon ([[OpenAI and Broadcom unveil AI inference chip]], Groq, Etched) plus hyperscaler self-builds (Microsoft's ~$80bn buildout) could erode the token volumes the revenue share is levered to.

**What this changes (idea-lens).** Nvidia is migrating from a chip vendor to a compute-platform *financier* — a re-rating toward recurring, GE-Capital-style revenue if it works, or a bubble tell if it's just vendor finance propping demand `(analysis)`. Falsifiable thesis: if backstopped neocloud utilization/token revenue holds through the next GPU refresh, the recurring layer de-risks Nvidia's cyclicality; watch/trigger — a single backstopped neocloud (Sharon AI, Firmus, or a CoreWeave-scale name) defaulting or breaching lease coverage would validate the vendor-finance-risk read and pressure the whole neocloud comp set.

Sources: https://www.tomshardware.com/tech-industry/nvidia-to-take-a-cut-of-ai-cloud-revenue-on-top-of-hardware-sales · https://www.datacenterdynamics.com/en/news/nvidia-acts-as-backstop-for-customer-gpus-in-return-for-cut-of-cloud-revenue/ · https://www.forbes.com/sites/janakirammsv/2026/07/03/why-the-neocloud-gold-rush-is-now-vendor-financed/ · https://www.techtimes.com/articles/319704/20260704/nvidia-revenue-sharing-ai-cloud-debuts-210000-gpus-flywheel-vendor-finance-risk.htm · https://techcrunch.com/2026/01/26/nvidia-invests-2b-to-help-debt-ridden-coreweave-add-5gw-of-ai-compute/ · https://seekingalpha.com/article/4915653-nvidia-coreweave-and-nebius-inside-the-circular-financing-of-the-gpu-boom · https://www.fool.com/coverage/charts/2026/04/09/nebius-vs-coreweave-accelerating-growth-vs-massive-scale-in-revenue/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
