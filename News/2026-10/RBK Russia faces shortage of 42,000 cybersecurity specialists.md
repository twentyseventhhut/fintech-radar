---
title: "RBK: Russia faces shortage of 42,000 cybersecurity specialists"
date: 2026-10-07
retrieved: 2026-10-08
tags:
  - industry/regtech
  - region/ru
  - type/research-report
sources:
  - https://companies.rbc.ru/news/GggTQivqXh/v-rossii-defitsit-spetsialistov-po-ib-ne-hvataet-42-tyisyachi-chelovek
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: sf5f66a0d
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# RBK: Russia faces shortage of 42,000 cybersecurity specialists

> [!info] 2026-10-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] РБК: В России дефицит ИБ-специалистов – не хватает 42 тыс. чел.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://companies.rbc.ru/news/GggTQivqXh/v-rossii-defitsit-spetsialistov-po-ib-ne-hvataet-42-tyisyachi-chelovek>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: RBK — Russia faces shortage of 42,000 cybersecurity specialists
_Analytical notes (not a post). Importance: 3/5._

**Type:** market-trend / labour-market datapoint (RBC press-aggregator relay), subject = Russia, not a company deal. **Freshness:** FRESH as a corpus note (first coverage of the IB talent-gap angle), BUT the underlying "42,000" number is a recycled 2025 vacancy statistic, not a new 2026 finding — see [0] and the freshness verdict below.

## [0] What exactly happened (de-PR'd)
RBC's `companies.rbc.ru` press feed relayed a one-line claim: "Russia has a deficit of IB (information-security) specialists — short by 42,000 people." The fintech-digest clip ("42 секунды", 2026-10-07) carries only that sentence; no methodology, no source attribution, no date-of-measurement in the note itself.

**What the 42,000 actually is (de-PR'd, the core correction):**
- The "42,000" traces to **HeadHunter** data first circulated via Vedomosti / GardInfo in **July 2025**: ~42,000 IB **vacancies were OPENED in the first ~4 months of 2025** — ~half of all IB vacancies posted in the whole of 2024. It is a **vacancy FLOW (demand/hiring activity)**, NOT a measured net shortfall of unfilled specialist positions. **(cited)**
- The RBC headline reframes "42k vacancies opened" into "shortage of 42,000 people" — a category error. A vacancy count ≠ an unmet-headcount deficit (one open req can be filled and reopened; many vacancies compete for the same candidates). → The number is real but mislabelled.
- The more authoritative **deficit** figure comes from a separate study — **Positive Technologies + CSR North-West ("Рынок труда в ИБ 2024–2027")**: the current gap is **~50,000 specialists (~45% of those employed)**, and is projected to reach **~52,000–65,000 (headline ~60,000) by 2027**, even as the share falls to ~29–33% as the employed base grows. Employed IB specialists ~**110,000 in 2023** (doubled since 2016) → **181,000–196,000 by 2027**. **(cited)**
- **Why framed this way:** RBC's companies-feed is a low-friction press-release channel; a round, alarming "42,000" headline travels. The de-PR reality: demand is genuinely surging, but the specific "42,000 shortage" conflates a 2025 vacancy flow with a structural deficit that credible analysts put nearer 50,000–60,000. → Treat "42,000" as directional evidence of a hot IB labour market, not as a precise deficit.

## [1] Competitors / peers (the data-points measuring the same gap)
"Peers" here = the other estimates of the RU IB/IT talent gap, which bracket the RBC figure:
- **Positive Technologies / CSR-NW:** IB-specific deficit ~50,000 now → ~52–65k by 2027; +19,000 architects/engineers needed 2024–2027 specifically for building domestic IB products (import-substitution-driven). The credible IB-specific anchor. **(cited)**
- **HeadHunter:** the ~42,000 vacancies / early-2025 flow; 7 candidates per IB opening in 2025 vs 3:1 in 2021 — but employers reject many as under-qualified ("junk" juniors, "сырые" vuz graduates). → the gap is a QUALITY gap at mid/senior level, not raw bodies. **(cited)**
- **Ministry of Digital Development:** broad IT deficit of **500,000–700,000** specialists (all IT, not IB) — the macro backdrop. **(cited)**
- **Position of the item:** the RBC "42,000" sits at the low end / is the least rigorous of the bracket; the PT/CSR ~50–60k is the number an analyst should cite. Second-order: because employers filter hard for quality, the binding constraint is experienced architects/DevSecOps, not entrants — raw "shortage" counts overstate how many hires would actually clear the bar. **(analysis)**

## [2] Fit / why this appears now (structural drivers)
Not a company, so "history" = the drivers of the gap:
- **Brain drain / emigration:** ~80,000–100,000 IT professionals net-emigrated 2022–2024 (RANEPA, via research), Moscow ~60% of departures; 15–20k to Armenia alone (40% still on remote Moscow contracts). This thinned the senior pool precisely as demand spiked. **(cited)**
- **Import substitution:** Dec-2024 decree + exit of Western security vendors (CrowdStrike, Palo Alto, Fortinet) forces migration to domestic stacks → net-new demand for engineers to BUILD and operate Russian IB products (the +19k architects/engineers in the PT/CSR study). Directly links to [[Vedomosti AI adoption lifts demand for corporate data protection]] (the SW-market side of the same tailwind) and [[Alfa-Bank starts selling its cybersecurity system externally]] (banks monetizing scarce in-house IB competence). **(cited)**
- **Regulatory load (the bank/fintech channel):** new **FSB GosSOPKA rules effective 30 Jan 2026** require 24/7 continuous attack-detection/SOC operation and live exchange with NKTsKI — "practically impossible to comply without full on-call shifts or an outsourced SOC." The Bank of Russia's 2025–2027 priorities explicitly include cybersecurity/regtech. → Regulation manufactures demand for IB headcount that the labour market cannot supply, pushing banks toward outsourced SOCs and automation. **(cited)**
- **Rising attack volume** on Russian targets (incl. 2024 Ukrainian cyberattacks) raises the operational need. **(cited)**
→ Why now: the gap is the intersection of SUPPLY destruction (emigration) and DEMAND inflation (import substitution + GosSOPKA + attacks) — a structural, multi-year squeeze, not a 2026 spike.

## [3] Novelty / value-add / traction
- **Novelty of the EVENT:** low. It is a recycled 2025 vacancy statistic re-surfaced via an RBC press feed; the underlying trend is well-documented since 2022. No new study, no new period, no new methodology disclosed in the note.
- **What is OBSERVED vs asserted:** observed/credible — ~110k employed (2023), ~42k vacancies opened H1-2025 (HH), ~50k current deficit and ~45% gap (PT/CSR), 7:1 candidates-per-opening. Asserted/soft — the exact "42,000 shortage" framing. **(cited vs analysis)**
- **Value-add reality for a fintech reader:** the gap is the **binding execution constraint** on the RU infosec growth story — it caps how fast the forecast IB-software spend ([[Vedomosti AI adoption lifts demand for corporate data protection]]) can actually be deployed and operated. Who captures the margin from scarcity: (a) incumbent IB vendors / MSSPs selling outsourced SOC to banks that cannot staff GosSOPKA in-house (→ [[Alfa-Bank starts selling its cybersecurity system externally]] is the bank-side mirror of this), and (b) the scarce senior engineers themselves via wage inflation (cyber is one of the few roles still seeing double-digit pay rises while general IT wages stagnated at ~183k RUB/mo median, flat y/y, H2-2025). **(cited + analysis)**

## [4] What's next / market sentiment
- **Direction:** all sources agree the gap persists through 2027; the % deficit may ease (45% → ~29–33%) as universities add IB masters' programmes and vendors run training, but the ABSOLUTE deficit RISES (to ~52–65k) because demand outruns supply. New training/master's tracks are the stated response (PT/CSR). **(cited)**
- **Counterintuitive second-order:** the shortage is self-mitigating in a perverse way — it FORCES automation (AI-assisted scanning, e.g. Alfa-Scanner) and SOC outsourcing, which structurally benefits the scaled IB vendors (Positive, BI.ZONE, Solar) at the expense of in-house bank teams. So the "talent crisis" is simultaneously the demand engine for the IB-vendor sector. The real question shifts from "can Russia train enough people?" to "how much of IB gets consolidated into a few vendor/MSSP platforms because clients can't staff it themselves?" **(hypothesis)**
- **Risks to the number:** single-line, unsourced-in-note; "42,000" is a 2025 vacancy flow masquerading as a 2026 deficit. Macro labour backdrop (Nabiullina's "unprecedented labour shortage" warning, Apr-2026) means wage inflation, not headcount growth, is the near-term adjustment.

## Sources
- RBC (primary, in note): companies.rbc.ru/news/GggTQivqXh/ (2026-10-07 relay).
- Vedomosti / GardInfo (Jul-2025): ~42,000 IB vacancies opened H1-2025 (HeadHunter), 7:1 candidates-per-opening.
- Positive Technologies + CSR North-West, "Рынок труда в ИБ 2024–2027": deficit ~50k (~45%) → 52–65k by 2027; employed 110k (2023) → 181–196k (2027); +19k architects/engineers. (ptsecurity.com; csr-nw.ru PDF)
- CNews (2025-02 / 2025-06): acute IB deficit, low-quality candidate glut, 7:1 ratio.
- RANEPA via research: 80–100k IT net emigration 2022–2024.
- Min. Digital Development: 500–700k broad IT deficit.
- FSB GosSOPKA rules eff. 30 Jan 2026 (cisoclub.ru; isslab.ru); Bank of Russia 2025–2027 priorities.
- Moscow Times (2026-02, 2026-04): IT wages flat ~183k RUB/mo; Nabiullina labour-shortage warning.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **What is the "42,000" actually measuring?** NOT a net deficit of unfilled posts. It is HeadHunter's count of IB VACANCIES OPENED in ~the first 4 months of 2025 (~half of all 2024 postings), circulated via Vedomosti/GardInfo in Jul-2025. RBC reframed a vacancy FLOW as a "shortage of 42,000 people." ANSWERED — mislabelled.

2. **Is there a more credible deficit figure?** Yes — Positive Technologies + CSR North-West put the current IB-specific deficit at ~50,000 (~45% of employed), rising to ~52–65k (headline ~60k) by 2027. That is the number to cite, not 42,000. ANSWERED.

3. **Is this a fresh event or a recycled statistic?** The NOTE is a first-coverage of the talent angle (fresh as a corpus entry), but the "42,000" is a 2025 number re-surfaced on an RBC press feed — no new study/period/method. Borderline; fresh as subject, stale as data. ANSWERED.

4. **Is it a duplicate of the Vedomosti companion note?** No. [[Vedomosti AI adoption lifts demand for corporate data protection]] is a market-SIZE forecast (₽198bn SW by 2031); this is the labour-SUPPLY gap. Complementary (supply vs demand of the same IB boom), not duplicate. ANSWERED.

5. **What is OBSERVED vs asserted?** Observed: ~110k employed (2023), ~42k vacancies H1-2025, ~50k/45% deficit (PT/CSR), 7:1 candidates per opening. Asserted/soft: the exact "42,000 shortage" framing. ANSWERED.

6. **If there are 7 candidates per opening, is it really a shortage?** It is a QUALITY/seniority gap, not a raw-body gap — employers reject under-qualified juniors and "сырые" graduates; the bind is experienced architects/DevSecOps. ANSWERED — mid/senior gap.

7. **What are the real drivers?** Supply destruction (80–100k IT net emigration 2022–24, RANEPA) + demand inflation (import substitution needing +19k engineers, GosSOPKA 24/7 SOC rules from 30-Jan-2026, rising attacks). ANSWERED.

8. **Who captures the value from the scarcity?** Scaled IB vendors / MSSPs selling outsourced SOC to banks that cannot staff GosSOPKA in-house (mirror of [[Alfa-Bank starts selling its cybersecurity system externally]]), and scarce senior engineers via wage inflation (cyber is a rare double-digit-raise role). ANSWERED (analysis).

9. **How does this hit RU banks/fintech specifically?** New FSB GosSOPKA rules (eff. 30-Jan-2026) require 24/7 attack-detection + live NKTsKI exchange — near-impossible to staff internally → forces SOC outsourcing/automation; Bank of Russia lists cybersecurity/regtech as a 2025–2027 priority. ANSWERED.

10. **Does the macro labour backdrop corroborate?** Yes — Nabiullina (Apr-2026) warned of an "unprecedented" economy-wide labour shortage; broad IT deficit 500–700k (MinDigital). IB is a sharp instance of a general squeeze. ANSWERED.

11. **Will training/universities close the gap?** Partially — PT/CSR expect the % deficit to fall (45%→29–33%) via new IB master's tracks/vendor training, BUT the ABSOLUTE deficit rises (to ~52–65k) because demand outruns supply through 2027. ANSWERED.

12. **Is the primary source rigorous?** No — the note carries one unsourced sentence from an RBC companies-feed (a press-aggregator); methodology/date/author absent. Figure recovered and corrected via HH/PT/CSR externally. ANSWERED — weak primary.

13. **What is the second-order effect of the shortage?** Perverse self-mitigation: it forces AI-assisted automation and SOC consolidation into a few vendors — so the "talent crisis" is itself the demand engine for the IB-vendor sector. Central question shifts from "can Russia train enough people?" to "how much IB consolidates into vendor/MSSP platforms?" (hypothesis)

14. **Direct fintech relevance for the digest?** Indirect but real: banks/fintechs are heavy IB employers and the parties most exposed to GosSOPKA staffing rules; the gap caps how fast the RU infosec spend can be operationalized. Lowers lead-worthiness, raises context value. OPEN/judgment.

15. **What would change the assessment?** A NEW dated 2026 study with a measured net deficit (vs recycled vacancy flow), or a concrete government/vendor training-output number — either would upgrade this from a recycled alarm stat to a trackable supply metric. OPEN.

**Importance: 3/5** — A structurally important, well-corroborated RU labour-market signal: IB talent is the binding execution constraint on the whole import-substitution/infosec-spend story, and it directly pressures banks via new GosSOPKA 24/7 staffing rules. But the specific "42,000" is a mislabelled 2025 vacancy flow (the credible deficit is PT/CSR's ~50–60k), the primary source is a one-line unsourced RBC press-feed relay, and the event is a recycled statistic rather than a new finding. Valuable as context/backdrop (complements the Vedomosti demand-side and Alfa-Bank vendor-side notes), not a lead story.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a labour-market datapoint, not a company story: RBK (2026-10-07) reports Russian firms are short ~42,000 information-security (IS) specialists. The sector the gap constrains is the RU infosec industry, which is booming on policy, not organic demand.
- The deficit is observed, not projected: by end-April 2025 RU companies were advertising for ~42,000 IS roles; IS-specialist vacancies rose **+18% y/y to ~90,000**, and IS is the single most-understaffed IT sub-field — lacking at **~52%** of IT companies, with sector unemployment **<1.2%** (RBK/HeadHunter-class labour data, via tproger/getgrade, 2026). That is a structurally tight market, not a cyclical gap.
- The demand it meets is the RU infosec boom: whole RU cybersecurity market **~₽364bn in 2025 (+16.1%)** heading to **~₽968bn–₽1trn by 2030–31, ~+21%/yr** (CSR, Nov-2025, via Kommersant/TASS); IS-software specifically **+13.1%/yr** to 2031 (iKS-Consulting via Vedomosti, see [[Vedomosti AI adoption lifts demand for corporate data protection]]). Western trackers are tamer (Mordor: ~USD 7.75bn 2026, CAGR ~8–11%) — read the direction, not the single number.
- "Why now": (1) **turnover-fine regime** (152-FZ / FZ-420, live 30 May 2025: repeat leaks 1–3% of revenue, ₽20–500m) makes security a mandated, board-level spend; (2) **import substitution** — exit of CrowdStrike/Palo Alto/Fortinet handed the whole domestic install base to RU vendors, forcing re-implementation on local stacks. Both are labour-intensive migrations → the demand shock lands on engineers, not just licences. Second-order: a supply-constrained industry whose growth is policy-mandated will see the gap resolved through **wage inflation and price pass-through**, not output, until the training pipeline catches up.

**Competitive landscape.** The KPIs the talent squeeze bites on: R&D/engineering headcount, revenue-per-engineer, and shipments growth vs the market. The "competition" here is for scarce engineers among the scaled RU vendors — **Positive Technologies** (FY2025 revenue ₽30.9bn, +26%; net profit ~₽7.3bn — ~2x the market rate), **Kaspersky, GC Solar (Rostelecom), BI.ZONE, Group-IB/F.A.C.C.T., InfoWatch** (DLP leader but sub-scale, FY ~₽3.77bn and shrinking) — plus banks/fintechs building in-house SOCs under 152-FZ. Basis of competition for talent: comp + brand + security-clearance fit, not pure salary.
- Wage signal (sourced): average cybersecurity pay in RU rose **~+40% to ~₽115,600/mo** on one tracker (techora, 2026-08), with industry wage-growth guidance of **+8–15% for 2026** for experienced staff; junior-glut / senior-scarcity polarisation means the +40% is concentrated at mid/senior level. Expat-grade annual figures (₽2.2–2.4m/yr, ERI/SalaryExpert) corroborate the upward trend `(analysis)`.
- Bank/fintech posture: banks are the heaviest regulated IS buyers (152-FZ + CBII/GOSSOPKA reporting), so the 42k gap directly raises the cost and lengthens the timeline of their security build-out — the constraint is felt as outsourced-SOC price and slower in-house hiring, not as a published metric `(analysis)`.
- Training pipeline (recent, dated): RU universities graduate **~120,000 IT specialists/yr across all specialties** vs a **>200,000** all-IT vacancy gap, and IS forecasts suggest only **~45% of need met by 2035** (iz.ru/edstellar, 2026) — i.e. formal education cannot close a 42k IS gap this decade. Private capital is trying to backfill: see [[FRII and Metascan launch 300M-ruble cybersecurity fund]] (2026-07), whose co-investor Metascan also took 24.5% of IS-training platform **defbox.io** (Jan-2026) — capital rotating into both IS product AND the training layer.

**Comps & multiples.** Internal comps (grep fallback; `sem search` returns HTTP 402):
- [[Vedomosti AI adoption lifts demand for corporate data protection]] (2026-10) — the demand-side companion: IS-SW +13.1%/yr, whole market → ~₽1trn by 2030-31. Confirms the booming industry this labour gap throttles.
- [[FRII and Metascan launch 300M-ruble cybersecurity fund]] (2026-07) — ₽300m IS-startup fund, ₽5–100m/project for 10% (implied ~₽50m–₽1bn pre-money band). Relevant twice: it funds the sector AND (via defbox.io) the training pipeline for the exact specialists in shortage.
- No in-base RU-IS labour-cost or listed-vendor valuation comp beyond these surfaced.
This is a labour datapoint, so there is no round/valuation to multiply; a trading multiple is **n/a**. For reference the only listed name, Positive Technologies, has sourced growth (+26%) and profit (₽7.3bn) but no free, dated EV/market-cap → EV/Revenue, P/E, EV/EBITDA are **[UNSOURCED] / no data**. Distribution not computed — qualitative only.

**Risk flags.**
1. **Supply-constraint caps the forecast** — a +13–21%/yr industry growth story assumes engineers exist to deliver it; a 42k gap with <1.2% unemployment and a pipeline covering only ~45% of IS need by 2035 means growth may show up as **wage/price inflation rather than delivered capability** — margin compression for integrators, timeline slippage for bank/fintech security build-outs.
2. **Policy-dependence of the underlying demand** — the gap is severe because demand is compelled (fines + forced import substitution). If either eased (unlikely near-term) the urgency and the wage premium would soften; if they persist, the labour cost structurally re-rates the whole sector's opex.
3. **Single-tracker salary/figures fragility** — the headline ₽115.6k/+40% wage number and the 90k-vacancy / 52%-of-firms stats come from individual recruiters/trackers, not audited data; the exact 42k is RBK's own and dated to spring-2025 demand, so treat magnitudes as directional, not precise.

**What this changes (idea-lens).** `(analysis)` The signal is that RU infosec's binding constraint has shifted from *regulatory willingness-to-spend* (solved by 152-FZ fines) to *human capacity to deliver* — i.e. the sector is moving from a demand story to a **supply/labour-cost story**. Falsifiable thesis: if the gap is real and structural, scaled vendors that can internalise training (Positive's cyber-range, defbox-style platforms) and arbitrage automation/AI-SOC should out-grow sub-scale peers, and IS wage growth should keep outrunning general-IT wage growth. Trigger / what breaks it: a sharp fall in IS vacancies or a convergence of IS pay back toward general-IT pay would signal the gap is closing (bearish for the labour-scarcity thesis, bullish for delivery); continued +40%-type wage prints alongside flat graduate output would confirm the bottleneck is here to stay.

Sources: https://companies.rbc.ru/news/GggTQivqXh/v-rossii-defitsit-spetsialistov-po-ib-ne-hvataet-42-tyisyachi-chelovek · https://techora.ru/news/zarplaty-v-kiberbezopasnosti-rossii-vyrosli-na-2026-08-20 · https://tproger.ru/articles/kogo-vozmut-na-rabotu-v-2026--razbor-it-rynka-posle-sokrashhenij · https://getgrade.ru/zarplaty-informacionnaya-bezopasnost · https://www.csr.ru/ru/news/k-2030-godu-rynok-kiberbezopasnosti-mozhet-dostich-pochti-trilliona-rubley/ · https://en.iz.ru/en/2169454/liubov-lezhneva/cadres-decide-everything-how-deal-shortage-specialists-russia · https://www.edstellar.com/blog/skills-in-demand-in-russia · https://www.mordorintelligence.com/industry-reports/russia-cybersecurity-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
