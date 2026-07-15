---
title: "WSJ: AI data centers use far more water than tech giants report"
date: 2026-07-15
retrieved: 2026-07-15
tags:
  - industry/ai
  - region/us
  - type/research-report
sources:
  - https://www.wsj.com/tech/ai/ai-data-centers-water-use-901e2902
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: s0d51c4c1
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# WSJ: AI data centers use far more water than tech giants report

> [!info] 2026-07-15 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] WSJ: Дата-центры для ИИ потребляют гораздо больше воды, чем сообщают большинство IT-гигантов

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.wsj.com/tech/ai/ai-data-centers-water-use-901e2902>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: WSJ — AI data centers use far more water than tech giants report
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS: FRESH.** This is a distinct WSJ investigation on the **water** footprint of AI data centers and the **disclosure gap** — not a duplicate. Internal retrieval surfaces adjacent-but-different notes on the same buildout theme, none covering the water-underreporting angle: [[StrictlyVC AI data-center boom emerges as new inflation driver]] (power capex as a macro/inflation driver, WSJ-sourced), [[Datacentres use 6% of UK and US electricity, says IDCA]] (electricity share, Guardian, May 2026 — mentions water only in passing via Greenpeace), [[Omen AI raises $31M Series A to optimize data-center cooling]] (coolant-loop fluid monitoring). None reports the direct-vs-indirect water accounting gap. No duplicate_of.

## [0] What exactly happened (de-PR'd)
- WSJ investigation (2026-07): most large tech companies **disclose only direct, on-site water** (cooling-tower/humidification evaporation at their own facilities) and **omit the far larger indirect water** consumed off-site by the power plants that electrify the data center. The headline is not "AI uses a lot of water" — it's an **accounting/scope gap**: the reported number is the small half.
- The load-bearing multiplier: a **2024 Lawrence Berkeley National Laboratory** analysis found US data-center **indirect water use (via electricity) has historically run ~12× direct** use (LBNL cited the ratio for 2023). So a company reporting only on-site water can be understating true water impact by ~an order of magnitude.
- Concrete numbers WSJ cites: **Google consumed 10.9bn gallons in 2025, +34% y/y**, almost all data-center cooling; peer-reviewed work suggests Google's **indirect** (power-supply) water is ~3× its direct — true total several times the headline. **Meta's 2024 indirect water = 19bn gallons, >20× its direct** — and Meta is the **exception that discloses power-plant water**; Microsoft, Google, Amazon center disclosures on on-site/operational use. **Amazon** does not publish total water use at all (reports water per unit of power). → **Why structured this way:** WUE (Water Usage Effectiveness, L/kWh) — the metric hyperscalers tout (Amazon ~0.12, Microsoft ~0.27 L/kWh in 2025) — is a **direct, on-site-only** metric by construction. Optimizing the reported number (drive WUE down) can *raise* electricity, which raises **off-site** water that never enters the disclosure. The metric choice is what hides the gap. (analysis)
- **The uncomfortable trade-off (the real story):** cooling method is a water-vs-power dial. Evaporative cooling saves electricity but burns on-site water; closed-loop / zero-water / air cooling cuts on-site water but **increases electricity** — which increases *indirect* water at the power plant. So "we went zero-water on-site" can be net-worse on total water. This is why a single disclosed figure is misleading. (corroborated: EESI, Data Center Frontier, MOST Policy)

## [1] Peers / rival framings
- Not a company deal — "peers" = how the majors compare on disclosure and the rival ESG narratives.
  - **Disclosure spectrum:** Meta (best — includes power-plant water) → Microsoft (total water, no site-level) → Google (total + newly more granular reporting; still not separately breaking out indirect) → **Amazon (worst — no total, only intensity ratio).** So the "who's silent about what" answer: Amazon on absolute water; everyone-but-Meta on indirect/off-site water.
  - **Corporate counter-narrative:** Microsoft's June-2026 blog touts a two-decade water-intensity cut (WUE 2.3 → 0.27 L/kWh) — a real efficiency story, but it is an **intensity** and **on-site** claim, i.e. exactly the frame WSJ challenges (falling L/kWh × exploding kWh can still mean rising absolute water, and says nothing about off-site). (analysis)
  - **Skeptic/quantifier camp:** LBNL (12× multiplier), MSCI (water-scarcity siting risk), arXiv/ScienceDirect scenario forecasts, National Interest ("water is the hidden bottleneck"). Aggregate US DC water ~**264bn gallons / ~1 trillion liters in 2025** (NA), average industry WUE ~1.9 L/kWh — so hyperscaler best-in-class numbers are far below the fleet average, another reason the disclosed leaders flatter the picture. (analysis)

## [2] Fit — why this surfaces now
Logical follow-on to the 2025→2026 capex step-change ([[StrictlyVC AI data-center boom emerges as new inflation driver]]: ~$741bn hyperscaler capex 2026). As the physical footprint doubles, **water shifts from footnote to siting constraint**: the US Southwest/Texas/Southeast have cheap power but are water-stressed, so a credible cooling-water plan is now a **screening gate** for a site. Water is becoming the *binding* constraint where power isn't. The disclosure story rides an April-2026 wave of shareholder resolutions (below), so the WSJ piece lands into an already-hot ESG cycle rather than opening it. (analysis)

## [3] Novelty / value-add
- **Real novelty:** quantifying the *disclosure gap* per-company (Google 10.9bn/+34%, Meta 19bn indirect, Amazon no-total) and anchoring it to the LBNL 12× multiplier — turning a diffuse "AI is thirsty" complaint into named, auditable numbers. That's reporting value, not PR.
- **Fintech/investor value-add (why this is in the corpus):** the transmission is (a) **utilities/water utilities** as a demand beneficiary and a scarcity chokepoint; (b) **cooling/siting** vendors (direct-to-chip liquid, immersion, dry cooling — see [[Omen AI raises $31M Series A to optimize data-center cooling]]); (c) an **ESG/regulatory** re-rating risk on the megacap AI names whose reported water understates true use. → **Who captures the margin / who bears the risk:** hyperscalers capture AI upside; **local ratepayers/water systems bear the externality**, and the *disclosure* gap is the mechanism that has let the externality stay off-balance-sheet — which is exactly what investors and the EU EED are now closing. (analysis)

## [4] What's next / sentiment
- **Regulatory:** EU Energy Efficiency Directive now **mandates annual reporting of total water input + WUE** for data centers above a power threshold (first reports filed 2026) — no mandatory WUE *thresholds* yet, but disclosure is no longer voluntary in the EU. US remains voluntary/patchy → the gap persists domestically.
- **Investor:** April 2026 — **>a dozen investors filed shareholder resolutions** at **Amazon, Microsoft, Alphabet** demanding **site-specific** water and power disclosure (Trillium's Alphabet resolution notes emissions *rose 51%* vs a 2030 halving pledge). This is the live pressure vector; expect more site-level disclosure and possibly WUE-Source (grid-inclusive) metrics.
- **Counterintuitive 2nd-order:** the more the industry "solves" on-site water (closed-loop, air cooling), the **more electricity** it needs → **more off-site (indirect) water** *and* more power-price/inflation pressure ([[StrictlyVC AI data-center boom emerges as new inflation driver]]). The water and power constraints are coupled, so "fixing" one can worsen the other — and can worsen the *unreported* half. The genuine relief valves are grid decarbonization (less water-intensive generation) and siting away from water-stressed basins, both slow. (analysis)
- **Risk to the thesis's weight:** it's an investigative/ESG story, not a deal — no direct near-term fintech P&L. Weight comes from siting/capex constraint + regulatory disclosure risk, not a transaction.

## Sources
- WSJ, "AI Data Centers Use Far More Water Than Most Tech Giants Report," 2026-07 (primary; no full text cached): https://www.wsj.com/tech/ai/ai-data-centers-water-use-901e2902
- LBNL 2024 US data-center report (indirect ≈12× direct water, 2023).
- Google 2025 sustainability report (10.9bn gal, +34%); Meta 2024 (19bn gal indirect); Amazon 2025 (intensity-only). Microsoft blog, 2026-06-24 (WUE 2.3→0.27 L/kWh).
- Investor pressure: Tom's Hardware / ESG News / News-Tribune, 2026-04-07 (>a dozen resolutions at Amazon/Microsoft/Alphabet; Trillium/Alphabet, Dec 2025).
- Context: EESI; Data Center Frontier; MOST Policy; MSCI (water-scarcity siting); National Interest (water bottleneck); Axis Intelligence (~264bn gal / ~1T L 2025 NA).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Challenge / red-team — WSJ: AI data centers use far more water than tech giants report

1. **Is the story new, or a re-run of the earlier water reporting?** Fresh as a corpus item (no prior water-specific note), but the *underlying* finding (companies rarely disclose true water use; direct-vs-indirect gap) has circulated since **Aug 2025** (The Current, Fast Company, GIJN). So novelty = the updated 2025 figures (Google 10.9bn/+34%) and per-company framing, not the core claim. Low-to-mid novelty.
2. **Is the LBNL "12×" multiplier load-bearing and current?** It's the whole story's fulcrum; LBNL cited it for **2023**, and it varies enormously by **grid mix** — WUE-Source is ~5 L/kWh on a coal/gas-heavy grid but near-zero on hydro/solar. Applying one national 12× to every company overstates uniformity. **Open / caveat.**
3. **Does falling WUE actually mean falling water?** No — WUE is intensity (L/kWh); with kWh exploding, absolute water can rise even as WUE falls (Google +34% while efficiency "improved"). Microsoft's 2.3→0.27 L/kWh claim is real but is exactly the misleading frame. Central point.
4. **Who's silent about what?** Amazon = no total water (intensity only); Microsoft/Google = no site-level and no separate indirect line; only **Meta** discloses power-plant (indirect) water. That asymmetry is the actual scandal, not the gallons themselves.
5. **Is "zero-water cooling" genuinely greener?** Not necessarily — closed-loop/air cooling cuts on-site water but **raises electricity → raises off-site water** at the plant. A single disclosed figure can flip sign depending on scope. This is the real trap.
6. **Is water or power the binding constraint?** Region-dependent: in the water-stressed SW/TX/SE, water availability is the siting gate; elsewhere power/grid-queue dominates ([[Datacentres use 6% of UK and US electricity, says IDCA]]: UK grid-connection queue +460%). Don't over-generalize "water is THE bottleneck."
7. **What's the measured fintech/investor P&L, vs inference?** Measured = shareholder resolutions filed (Apr 2026), EU EED mandatory reporting live. Inferred = re-rating risk on megacaps, water-utility upside, cooling-vendor TAM — all directional, no quantified earnings hit. Weight is ESG/siting, not a transaction.
8. **Are the shareholder resolutions material or symbolic?** >a dozen filed at Amazon/Microsoft/Alphabet demanding site-specific disclosure; Trillium flags Alphabet emissions +51% vs a 2030-halving pledge. Governance signal, but such resolutions rarely pass — pressure is reputational/disclosure, not binding (yet). **Open on outcome.**
9. **Does the EU EED actually bite?** It mandates reporting total water + WUE above a power threshold (first reports 2026) but sets **no mandatory WUE thresholds** — transparency, not a cap. US stays voluntary. So near-term effect is disclosure, not curtailment.
10. **Could the numbers be cherry-picked to the worst names?** Google +34% and Meta 20× are attention-grabbing; the fleet-average WUE (~1.9 L/kWh) is far worse than hyperscaler best-in-class — so if anything the *named leaders* flatter the industry. The investigation's frame is defensible, not a strawman.
11. **Who benefits (investor angle) and is it durable?** Water utilities (demand + scarcity pricing), dry/liquid-cooling and immersion vendors ([[Omen AI raises $31M Series A to optimize data-center cooling]]), siting/permitting advisors. Durable only if water genuinely gates siting at scale — plausible in specific basins, not economy-wide. (hypothesis)
12. **Second-order coupling with the power/inflation story?** Solving on-site water pushes electricity up → feeds the [[StrictlyVC AI data-center boom emerges as new inflation driver]] power-price thesis and *increases indirect (unreported) water*. Water, power and inflation are one coupled constraint, not three. This is the strongest analytical point.
13. **Is community/regulatory backlash the real transmission?** [[Datacentres use 6% of UK and US electricity, says IDCA]] flagged pushback past a 5% grid-share threshold; water scarcity accelerates local opposition and permitting friction — the practical near-term risk is *delayed/blocked sites*, which is a capex-timing risk, not a disclosure fine.
14. **Data vintage mixing?** Google is 2025 actual, Meta indirect is 2024, LBNL ratio is 2023 — mixing vintages across companies flatters comparability; true apples-to-apples per-company totals still don't exist, which is itself the point.
15. **Falsifiable watch-items:** (a) do Amazon/MSFT/Google begin publishing site-level or WUE-Source (grid-inclusive) water in FY26 reports? (b) does any US jurisdiction move from disclosure to a water cap/moratorium on DC permits? (c) do the Apr-2026 resolutions gain >20% support? Any "yes" upgrades this from ESG-noise to a real siting/capex constraint.

**Importance: 3/5 — rationale:** A well-sourced, quantified investigative piece that reframes AI-datacenter water from "footnote" to a **disclosure gap + siting constraint** with named per-company numbers (Google 10.9bn/+34%, Meta 19bn indirect/20×, Amazon no-total) anchored to LBNL's 12× multiplier, landing amid live shareholder resolutions (Apr 2026) and new EU EED reporting. Above a 2 because it is corroborated, decision-relevant to siting/capex and megacap ESG risk, and couples directly to the power/inflation thesis already in the corpus. Capped at 3 (not 4) because it is investigative/ESG commentary with **no direct fintech transaction or near-term P&L**, the core "companies under-report water" claim predates this piece (since Aug 2025), and the investor transmission (utilities/cooling upside, re-rating risk) is directional inference rather than a measured earnings impact.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: AI-datacenter physical infrastructure — the water/power/cooling constraint layer under the compute buildout. The WSJ story sits inside a bigger theme: AI capacity is now bottlenecked by physical resources (water, grid interconnect, land), not chips alone. Sourced facts: (1) US datacenters consumed ~264bn gallons of water/year by 2025 and could reach up to ~600bn gallons by 2030 (per Tom's Hardware citing industry study, 2026); >40% of planned/existing US datacenters sit in high or extremely-high water-scarcity zones (per Capacity, 2026). (2) EPRI's Powering Intelligence 2026 projects US datacenters at 9–17% of national electricity by 2030 vs ~4–5% today — a range 60% above prior scenarios (per EPRI, 2026); Virginia's datacenter share could hit 41–59% of state load by 2030. (3) Liquid-cooling market projected ~$4.07bn (2026) → ~$27.65bn (2033), ~31.5% CAGR (per MarketsandMarkets, 2026). Structure: fragmented at the supply end (thermal/power gear vendors, utilities, water utilities) but concentrated demand (a handful of hyperscalers + neoclouds). Barriers are capital and permitting, not tech. Why now: water/grid permitting has moved onto the critical path — >300 datacenter bills across 30 US states in the first six weeks of 2026, pivoting from tax incentives toward mandatory water disclosure, cooling-permit rules and cumulative environmental-impact assessments (per Capacity/MultiState, 2026); NY passed a bill for a 12-month permit freeze (would be first statewide moratorium if signed).

**Competitive landscape.** Sector KPIs: PUE/WUE (water-usage effectiveness), GW of contracted/connected power, permit-to-power lead time, and cooling backlog. Exposed players by layer:
- **Hyperscalers (demand / disclosure-risk):** Google 6.4bn gal water (2024), Microsoft 1.7bn gal (FY23), Meta ~870m gal (2023) — the WSJ thesis is that reported figures understate true (incl. off-site/power-generation) water. Investor pressure mounting: April-2026 shareholder campaigns pressing Amazon/Google/Microsoft for site-level power+water disclosure. Mitigation underway: Microsoft's zero-water closed-loop chip-cooling design (Phoenix, Mt. Pleasant pilots, online late-2027).
- **Cooling/power vendors (supply / beneficiaries):** Vertiv (VRT) — Q1'26 revenue $2.65bn (+30.1% YoY, Americas +53%), FY26 guide raised to $13.5–14.0bn, backlog >$15bn; bought Strategic Thermal Labs to deepen liquid cooling. Schneider Electric — co-leader in liquid cooling; note its [[Schneider Electric acquires industrial AI firm Cognite]] deal targets grid/datacenter operations software.
- **Utilities:** incremental supply under reference policy is dominated by natural gas (EPRI), with carbon-free commitments shifting some investment to storage — utilities in VA/AZ/TX/IA are the load-growth winners but also carry ratepayer-backlash risk.
Basis of competition (vendors): thermal density leadership + integrated power-thermal packaging, not price. Position: liquid cooling is a structural share-gainer as racks get hotter — WUE/closed-loop is becoming a competitive and regulatory necessity, not a nice-to-have.

**Comps & multiples.** VRT trades at a forward P/E ~53x — more than double the Industrial Products median — with sell-side targets $330–435 (Morgan Stanley/Citi/TD Cowen/RBC etc., 2026). Arithmetic check: premium is set against ~30% organic revenue growth and ~51–66% guided EPS growth, so ~53x on ~55%+ earnings growth ≈ PEG ~1x — rich vs peers but not obviously de-linked from growth (see growth-multiple correlation; flag only if growth stalls). Liquid-cooling TAM growth (~31.5% CAGR) supports the multiple qualitatively. Internal comps: [[Linas Newsletter Coatue's May 2026 report maps the $12T AI bet]] frames "sellers of scarcity" (chips/power/turbines book margin now) vs "buyers of scarcity" (hyperscalers) — cooling/power vendors sit on the seller side; [[Reflection AI signs $1B compute deal with Nebius]] shows the same power-as-bottleneck dynamic (Nebius contracting ~3.5GW). Schneider Electric standalone multiple: no data (not computed here). Distribution not computed — only one clean public pure-play (VRT); qualitative comparison.

**Risk flags.**
1. **Disclosure/regulatory re-rating on demand side.** Mandatory water disclosure + moratoria (NY freeze, 30-state bill wave) lengthen permit-to-power timelines and can strand sited capex; second-order effect — slower datacenter build-out throttles the whole compute-supply chain, hitting neoclouds and hyperscaler capex plans, not just water.
2. **Water scarcity as a hard siting constraint.** >40% of datacenters in high-scarcity zones means water rights, not just power, gate greenfield expansion — a bottleneck that can't be solved with capital alone and pushes builds to farther/costlier locations.
3. **Vendor valuation/concentration.** VRT at ~53x forward is priced for sustained ~30%+ growth tied almost entirely to one AI-capex cycle; any hyperscaler capex pause (the "buyers of scarcity" re-rating risk flagged by Coatue) would compress both order backlog and the multiple — cyclical, not structural, per Coatue's own framing.

**What this changes (idea-lens).** The read-through: water/grid is emerging as the next binding constraint on AI scaling after chips, which (a) hands pricing power to liquid-cooling/closed-loop and power vendors (VRT, Schneider) and (b) adds a regulatory-cost and reputational overhang to hyperscalers who under-disclose (analysis). Falsifiable thesis: if 2026–2027 sees zero-water/liquid-cooling adoption accelerate AND water-disclosure rules bite, cooling vendors keep re-rating while high-scarcity-sited hyperscaler projects slip. Watch: NY moratorium signature, hyperscaler water/WUE disclosures in next sustainability reports, and VRT/Schneider cooling backlog. Thesis breaks if a hyperscaler capex pause cuts the cooling backlog — the seller-side lead would compress with it.

Sources: https://www.tomshardware.com/tech-industry/ai-is-set-to-consume-up-to-600-billion-gallons-of-water-by-2030-rising-energy-consumption-primarily-to-blame-as-data-center-power-demands-rise · https://capacityglobal.com/news/data-centre-water-rights-permitting-risk/ · https://powering-intelligence.epri.com/executive-summary.html · https://www.multistate.us/resources/state-data-center-policy-101 · https://insideclimatenews.org/news/04062026/new-york-data-center-moratorium-bill/ · https://www.marketsandmarkets.com/ResearchInsight/data-center-liquid-cooling-market.asp · https://letsdatascience.com/news/vertiv-reports-q1-2026-revenue-growth-driven-by-ai-data-cent-cfadfe9e · https://seekingalpha.com/article/4890719-vertiv-holdings-the-15-billion-backlog-liquid-cooling-dominance-and-the-ai-infrastructure-trade-wall-street-is-still-underpricing
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
