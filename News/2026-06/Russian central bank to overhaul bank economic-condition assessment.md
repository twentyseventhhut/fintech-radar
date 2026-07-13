---
title: "Russian central bank to overhaul bank economic-condition assessment"
date: 2026-06-25
retrieved: 2026-06-26
tags:
  - industry/banking
  - industry/regtech
  - region/europe
  - type/regulation
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: s5bc5ecca
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# Russian central bank to overhaul bank economic-condition assessment

> [!info] 2026-06-25 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] ЦБ хочет заменить старую почти двадцатилетнюю методику оценки экономического положения банков на более риск-чувствительную модель. Новая методика должна быть оформлена нормативным актом в 2028 году, а с 2029 года банки планируют оценивать уже по новым правилам. Действующая методика плохо различает банки по уровню устойчивости: большинство попадает в одну классификационную группу, хотя их пять. В новой логике регулятор будет оценивать банки не по набору усреднённых баллов, а по тому, сколько капитала и ликвидности он реально потеряет при реализации ключевых рисков. Раньше банк мог получить плохой балл за один риск, хороший — за другой, и итоговая оценка выглядела приемлемо. Теперь ЦБ будет смотреть, насколько каждый риск снижает норматив достаточности капитала. Если кредитный риск может снизить Н1 на 3 п.п., а запас капитала у банка всего 1 п.п., проблема становится очевидной. Новая методика в перспективе поможет ЦБ связать риск банка с ценой страхования вкладов. По предварительным р

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Bank of Russia to overhaul bank economic-condition assessment (ОЭП)
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
The Bank of Russia (CBR) is replacing its ~20-year-old methodology for the "economic-position assessment" of banks (оценка экономического положения банков, ОЭП) — a core supervisory rating that drives inspection intensity and (in future) deposit-insurance premiums — with a more risk-sensitive model. De-PR'd:
- **This is NOT a brand-new announcement.** CBR first published the proposal as a consultation paper on **25 June 2025** (`consultation_paper_25062025.pdf`, event id 24731), then spent ~a year discussing it with banks. The June 2026 item (Финтехно; mirrors Interfax/Kommersant "ЦБ доработал/пересмотрел") is the **refined concept** after public consultation, NOT a first proposal. → The corpus has no prior note on this thread, so within OUR base it is new, but the underlying initiative is a year old; the "freshness" sits in the refinement, not the idea.
- **Mechanism delta (the real substance):** today banks get averaged sub-scores per risk; a bad score on one risk can be offset by a good score on another, so the blended rating looks acceptable. Result: the existing 5-group classification doesn't discriminate — most banks bunch into one group. The new logic measures **how much capital/liquidity a bank would actually lose if a given risk materialises**, and **assigns the final score by the WORST block** (no offsetting). If credit risk could cut the H1 capital-adequacy ratio by 3 pp but the buffer is only 1 pp, the problem becomes visible.
- **Structural redesign (from the refined version):** the quantitative score is cut **from five blocks to two** — "Capital" and "Liquidity" — with the final quantitative score taken by the worst of the two; plus a separate "quality of bank management" block. CBR **dropped the high-risk-assets (ВРА, высокорискованные активы) indicator** and trimmed the indicator set to the most material ones. Profitability is to be judged across the economic cycle, not a single year.
- **Why structured this way:** the explicit goal is to break score-offsetting and surface the binding constraint (worst risk vs thinnest buffer). The second-order purpose is to make the rating fine-grained enough to **price deposit insurance by risk** (the worse the ОЭП, the higher the premium into the ФОСВ/АСВ fund).

**Timeline caveat (the note vs CBR's own dates):** the note says the normative act lands in **2028** and banks are assessed under new rules from **2029**. Some 2025-era coverage cited a **2027–2028** transition. The 2028-act / 2029-application framing is what the latest (refined) coverage carries, so treat 2028/2029 as the current plan and 2027–2028 as the earlier, now-superseded estimate — but flag this as an open, slippable date.

## [1] Competitors / peers (regulatory peers)
ОЭП is a supervisory-rating regime, so "peers" are other regulators' bank-rating frameworks, not companies.
- **US: CAMELS** (Fed/OCC/FDIC) — composite supervisory rating; FDIC already runs **risk-based, differentiated deposit-insurance premiums** keyed to CAMELS + financial ratios. CBR is, in effect, catching up to a 1990s-vintage US design.
- **EU: SREP** (ECB/EBA Supervisory Review and Evaluation Process) — a scored, risk-based supervisory assessment feeding Pillar-2 capital add-ons.
- **Brazil:** see corpus — [[Brazil's central bank to apply uniform rules to banks and nonbanks]] (Nov 2025): same regulatory direction (evolving risk-based supervision, extending to non-banks).
- **Position:** CBR is **catching up / parity-seeking**, not pioneering. Risk-sensitive supervisory scoring tied to differentiated DI premiums is established practice abroad; the novelty is domestic (replacing a 2008-era указание).

## [2] Company history / fit (CBR's supervisory arc)
- The legacy ОЭП rests on указание 2005-У (2008), later 4336-У (2017) — hence "almost twenty-year-old" framing.
- CBR has been steadily moving to risk-based regulation: standardised credit-risk approach revisions (2019), risk-weight buffers/add-ons, and a countercyclical buffer turned positive (0.25%→0.5% in 2025).
- The corpus shows CBR active on multiple supervisory/fintech fronts in 2026: [[Russia's central bank calls MAX transaction approval premature]] (Mar 2026), [[Bank of Russia to explore feasibility of a national stablecoin]] (Feb 2026). ОЭП reform fits the same "tighten and modernise supervision" logic.
- **Why now:** the legacy tool failed its primary job (discrimination — everyone in one group). A supervisor that can't rank-order resilience can't triage inspections or price insurance — so the reform is a structural fix, not cosmetic.

## [3] Novelty / value-add / traction
- **Real novelty (domestic):** moving from additive/averaged sub-scores to a **worst-block, loss-given-stress** logic that ties each risk directly to its hit on the H1 ratio. That is a genuine methodological shift, not relabelling.
- **Traction = near zero (by design, it's early).** This is a **refined consultation concept**, internally tested at CBR in H2 2025; the binding normative act is years out (2028), application 2029. No bank is rated under it yet. Per anti-PR gate: this is "framed/consulted", emphatically **not live**.
- **Where the value is real:** if the worst-block rule survives lobbying, it removes the offsetting that let weak banks hide — a real supervisory upgrade. **What could break it:** banks (e.g. Sber publicly assessed the methodology in mid-2025) will push to soften it; the worst-block rule is harsh and politically contestable, so the final act may reintroduce smoothing. The 2028/2029 horizon also means design can drift substantially before it binds.

## [4] What's next / market sentiment
- **Path:** refined concept (2026) → normative act (2028, per latest coverage) → banks assessed under new ОЭП from 2029 → differentiated ФОСВ/АСВ deposit-insurance premiums linked to ОЭП thereafter. An interim step (2027–2028) introduces criteria for an elevated additional insurance rate before full differentiation.
- **Second-order effects:** risk-priced DI premiums create a real incentive gradient — weak banks pay more, which either strengthens them or accelerates exits/consolidation. For a sector where most banks currently cluster in one group, sharper discrimination could **re-rank** institutions and surface previously masked fragility (counterintuitive: better measurement can look like "more weak banks appearing" without anything having actually worsened).
- **Risks/uncertainty:** long runway (a 2029 binding date is highly slippable); lobbying could dilute the worst-block rule; cross-border verification of CBR specifics is constrained (sanctions-era reduced English-language primary coverage).

## Sources
- CBR consultation paper, 25 Jun 2025: https://www.cbr.ru/content/document/file/177312/consultation_paper_25062025.pdf ; press event id 24731: https://www.cbr.ru/press/event/?id=24731
- Interfax (refined approach): https://www.interfax.ru/business/1098278 ; earlier test: https://www.interfax.ru/business/1034589
- Kommersant: https://www.kommersant.ru/doc/8765250 ; Forbes: https://www.forbes.ru/finansy/540483 ; Expert: https://expert.ru/news/tsb-predlozhil-izmenit-sposob-otsenki-ekonomicheskogo-polozheniya-bankov/
- profbanking (2027–2028 framing): https://www.profbanking.com/only-news/5200-oep ; Финансы Mail (25 Jun 2025): https://finance.mail.ru/amp/2025-06-25/cb-peresmotrit-metodiku-ocenki-ekonomicheskogo-polozheniya-bankov-66737286/
- Internal corpus: [[Brazil's central bank to apply uniform rules to banks and nonbanks]], [[Russia's central bank calls MAX transaction approval premature]], [[Bank of Russia to explore feasibility of a national stablecoin]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5 — rationale.** A genuine, structural overhaul of a core Russian bank-supervision instrument (worst-block, loss-given-stress logic replacing offsetting averages) with a real downstream consequence: risk-differentiated deposit-insurance premiums. That matters for the RU banking sector and regtech. But it is capped: (a) it is a *refined consultation concept*, not law — binding act ~2028, application 2029, so zero current traction and a highly slippable horizon; (b) the design mirrors long-established foreign frameworks (FDIC risk-based premiums, CAMELS, ECB SREP) — domestic catch-up, not global novelty; (c) single-channel sourcing (one RU channel) and sanctions-limited cross-verification. New within our corpus, but the initiative itself dates to June 2025.

## Red-team questions
1. Is this actually new? — Partly. The proposal was published as a CBR consultation paper on 25 Jun 2025; June 2026 is the *refined* version after a year of market consultation. New within our base, but a year-old initiative. (answered)
2. Duplicate of a prior corpus note? — No. Semantic search surfaced no prior note on the ОЭП methodology; closest are thematic, not the same event. Verdict: fresh. (answered)
3. Which timeline is correct — 2027–2028 or 2028-act/2029-application? — Both appear in coverage; 2025-era said 2027–2028, latest refined coverage says act 2028 / apply 2029. Treat 2028/2029 as current, 2027–2028 as superseded. **Open** (date will likely slip).
4. Does the "worst-block, no-offsetting" rule survive into the final act, or get smoothed back under bank lobbying? — **Open** — this is the load-bearing design choice and the most contestable.
5. How many blocks in the final quantitative score — confirmed two ("Capital", "Liquidity")? — Yes, per refined version, cut from five to two, worst-of taken. (answered)
6. Was the high-risk-assets (ВРА) indicator really dropped, and what does its removal change? — Reported dropped in the refined version; reduces complexity but also removes a forward-looking risk flag. (answered, second-order open)
7. How exactly are premiums differentiated, and by how much? — Direction known (worse ОЭП → higher ФОСВ premium); magnitudes/brackets not specified. **Open**.
8. Will sharper discrimination *re-rank* banks and expose masked fragility without anything worsening? — Plausible second-order effect; (analysis), unquantified. **Open**.
9. Could risk-priced premiums accelerate exits/consolidation among weak banks? — Likely directional effect; depends on premium steepness. **Open**.
10. How does this compare to FDIC/CAMELS and ECB SREP — is CBR pioneering or catching up? — Catching up; risk-based DI premiums are decades-old abroad. (answered)
11. What's the legacy regime being replaced? — указание 2005-У (2008) → 4336-У (2017); hence "~20-year-old". (answered)
12. Is any of this live today? — No. Internally tested at CBR (H2 2025); no bank rated under it; act not issued. (answered)
13. How will "quality of management" be scored objectively vs the quantitative blocks, and how are the two combined? — CBR flags this as an open design question (e.g. balancing capital deficit vs consumer-rights violations). **Open**.
14. Source robustness? — Single RU channel (Финтехно) in our base; corroborated by CBR primary PDF + Interfax/Kommersant/Forbes externally. Adequate. (answered)
15. Does profitability-across-the-cycle (vs single-year) materially change ratings? — Intended to reduce point-in-time noise; effect depends on cycle calibration. **Open**.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-28]] (2026-06-28).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is bank-supervision / regtech, not a company market — the relevant "market" is risk-based deposit-insurance (DI) pricing, where CBR is a late mover. Sizing anchors: US DIF reached **$145.3bn with a 1.36% reserve ratio in Q2 2025**, rising to **1.42% by Q4 2025** vs a statutory 1.35% minimum and a 2% designated target (per FDIC, as of those quarters); the EU DGSD mandates each scheme fund **≥0.8% of covered deposits** ex-ante (per EBA). Both already run risk-differentiated premiums. Structure of the RU side: **highly consolidated and state-dominated** — Sberbank alone is ~1/3 of system assets (per Statista/Sber, FY2025 Sber ROE 22.7%, ~110.7m retail clients), and CBR's 2013-onward "clean-up" closed ~550 banks by 2021 (per Statista). Driver / "why now": the legacy ОЭП fails its one job — discrimination (most banks bunch in one of five groups), so a supervisor that can't rank-order resilience can't price DI by risk; the worst-block / loss-given-stress redesign is the structural fix (per Interfax 1098278, Kommersant 8765250). Second-order: in a sector already concentrating, risk-priced premiums steepen the cost gradient on the long tail of small banks → accelerant to further consolidation (analysis).

**Competitive landscape.** "Players" here are peer regulators' DI-pricing regimes (this note has no company protagonist). The KPIs the regime runs on: (1) DI fund reserve ratio vs target, (2) premium dispersion across rating bands, (3) discriminatory power of the supervisory score. Comparison vs CBR's design:
- **US / FDIC + CAMELS** — small-bank initial base rates **3–30 bps** keyed to CAMELS composite (1–2: 3–16 bps; 3: 6–30; 4–5: 16–30), large banks on a scorecard; CAMELS weights Capital + Management 25% each (per FDIC). Mature, decades-old; CBR is catching up to a 1990s design.
- **EU / EBA + SREP** — risk-based DGS contributions adjusted to each institution's profile, explicitly to curb moral hazard, feeding off SREP/Pillar-2 risk assessment (per EBA / ECB banking supervision).
- **India / RBI–DICGC** — closest live analogue in our corpus: RBI proposed risk-based DI premiums Oct 2025 and **DICGC launched its risk-based framework Feb 2026** (per corpus notes) — an EM peer moving on the same axis only months ahead of CBR.
- **Protagonist position:** CBR is **catching up / parity-seeking**, not pioneering — the novelty is purely domestic (replacing a 2008-era указание). Distinctive design choice: a harsh **worst-of-two-blocks (Capital/Liquidity), no-offsetting** rule, more aggressive than FDIC's weighted CAMELS composite (analysis).

**Comps & multiples.** No valuation/round/deal/metrics in this regulatory item → trading-comp multiples are **not applicable** (no EV/Revenue, P/E etc. to compute). Comparison is qualitative across DI-pricing regimes. Internal corpus comps (same risk-based-DI / risk-based-supervision theme): [[RBI proposes risk-based deposit insurance and Basel III revisions]] (Oct 2025), [[DICGC launches risk-based deposit insurance premium framework]] (Feb 2026), [[Brazil's central bank to apply uniform rules to banks and nonbanks]] (Nov 2025), and US DI-context [[FDIC approves Thiel-backed Erebor Bank for deposit insurance]] (Dec 2025). External quant anchors: FDIC DIF 1.42% reserve ratio / 3–30 bps CAMELS band; EU ≥0.8% covered-deposits target — all `[as cited above]`; CBR's own premium brackets/magnitudes are **not specified** ("no data" — direction only: worse ОЭП → higher ФОСВ premium).

**Risk flags.**
1. **Consultation, not binding law.** This is a *refined concept* after ~1yr of consultation, not a normative act — act ~2028, application 2029, zero banks rated under it today. The load-bearing worst-block / no-offsetting rule is the most contestable element; bank lobbying (Sber publicly assessed it in 2025) could reintroduce smoothing before it binds → the headline "harshness" may not survive (why: design can drift before enactment).
2. **~2029 horizon is highly slippable + already slipped once.** Earlier coverage cited a 2027–2028 transition, now 2028-act/2029-application — the date has already moved out, so further drift is the base case (why: a 3-yr-plus runway in a politically negotiated rulemaking compounds execution risk).
3. **Domestic catch-up, not frontier.** The whole design (risk-based DI tied to a supervisory score) mirrors FDIC/CAMELS, EBA/SREP and even EM peer RBI/DICGC — so the "market"/regtech upside is bounded; it removes a domestic distortion rather than creating a new capability (why: limited read-through beyond RU; single-channel RU sourcing + sanctions-era thin cross-verification add an information-quality discount).

**What this changes (idea-lens).** If the worst-block rule survives intact, it re-ranks a system that currently can't be ranked — surfacing previously masked fragility in the small-bank tail and, via risk-priced ФОСВ premiums, accelerating exits/consolidation in an already Sber-dominated sector (analysis). Falsifiable thesis: the final 2028 act will *dilute* the no-offsetting rule (reintroduce smoothing). Trigger/catalyst to watch: the draft normative act text and the specific premium brackets — if magnitudes and the worst-of rule appear intact, thesis is wrong; if a blend/offset reappears, confirmed.

Sources: https://www.fdic.gov/news/speeches/2026/fdic-quarterly-banking-profile-fourth-quarter-2025 · https://www.fdic.gov/deposit-insurance-assessments/risk-based-assessments · https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/depositor-protection/guidelines-methods · https://www.interfax.ru/business/1098278 · https://www.kommersant.ru/doc/8765250 · https://www.statista.com/statistics/1116407/russia-top-10-largest-banks-by-assets/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
