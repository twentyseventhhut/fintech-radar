---
title: "Colombia's Bre-B instant payments turns one with 36M clients"
date: 2026-10-07
retrieved: 2026-10-08
tags:
  - company/bre-b
  - industry/payments
  - region/latam
  - type/research-report
sources:
  - https://www.elcolombiano.com/negocios/bre-b-primer-ano-pagos-inmediatos-colombia-KI41948471
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: se5f892eb
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Colombia's Bre-B instant payments turns one with 36M clients

> [!info] 2026-10-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] 🇨🇴Bre-B, Colombia's instant payment system, turned one with 36 million clients, about 67% of the population, who have registered 115.4 million keys and made 1.7 billion transactions worth about $75.8 billion.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.elcolombiano.com/negocios/bre-b-primer-ano-pagos-inmediatos-colombia-KI41948471>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Colombia's Bre-B instant payments turns one with 36M clients
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
On 2026-10-06, Banco de la República (Colombia's central bank) published official first-anniversary figures for Bre-B, the country's mandatory-interoperable instant-payment rail that went fully live 2025-10-06. The headline, corroborated banrep.gov.co + EBANX + Colombian press:
- **36M+ users** with at least one registered key (~32M of them individuals), vs a country of ~40M adults / ~53.7M population.
- **116M keys** registered ("llaves" = phone/ID/email/alphanumeric alias); **only ~45M keys have actually received ≥1 payment** — a real activation gap the PR headline buries.
- **1.7B+ transactions** cumulative; **262T+ pesos** moved (~USD 75.8-80B; note's $75.8B is the FX-of-the-day figure, banrep quotes pesos only).
- **~10M transactions/day** now, vs ~60M/month (~2M/day) at launch — roughly 3-5x daily growth.
- **245 entities connected** (vs ~25 pre-Bre-B), incl. 172+ cooperatives and 6 payment systems.
- **62% of operations under COP 50,000** (~USD 12) — confirming it is a low-value, cash-displacing P2P rail, not large-ticket.

**Why framed this way:** banrep anchors to "clients with ≥1 key" (a registration count) and headline transaction totals, not active-payer counts — 36M registered but only ~45M of 116M keys ever received a payment implies a meaningful dormant share. The real traction story is daily velocity (3-5x) and institutional breadth (245 entities), which is harder to game than a one-time key sign-up.

## [1] Competitors / peers
Bre-B is explicitly benchmarked against **Brazil's Pix** (BCB, 2020), the LatAm reference rail. Per EBANX (using BCB + banrep + UN/IBGE adult-population data): Bre-B reached **83% of Colombian adults in year 1 vs Pix's 65%** — an 18pp lead; Pix took ~3x longer to hit 83% penetration. Mechanism delta in one sentence: **Pix built a single new centralized rail operated by the central bank itself; Bre-B overlaid a central interoperability layer (built with ACI Worldwide under contract) on top of ~25 pre-existing private wallets/schemes, preserving incumbents' investment.** Regional peers: Mexico CoDi/DiMo (sluggish adoption), Argentina Transferencias 3.0, India UPI (the global volume benchmark). Prior corpus: [[Colombia's Bre-B surpasses 600 million transactions in six months]], [[Instant transfers driving real-time payments in Latin America]].

**Why the lead over Pix:** (analysis) two structural reasons. (1) Colombia copied Pix's single best lesson — **mandatory interoperability for every institution from day one** — removing the chicken-and-egg problem. (2) By connecting existing wallets rather than rebuilding, Bre-B inherited an installed base of already-digitized users, front-loading adoption. The flip side (analysis): a connected-overlay architecture is only as resilient as its weakest node — which the February 2026 Bancolombia multi-day outage exposed (see [4]).

## [2] Company history / fit
Not a company — a central-bank public-good project. Timeline: origin 2022 (fragmented, non-interoperable wallets); legal basis Art. 104 of the 2023 National Development Plan gave banrep power to mandate low-value-payment interoperability; ACI Worldwide contracted to build core; key registration opened 2025-07-14; launch delayed twice then live 2025-10-06 (3M keys day one). Milestones in-corpus: 20M users (Aug 2025), 34.4M users / 503M tx (Mar 2026), 34.6M clients / 638.6M tx / 600M+ (Apr 2026, 6-month mark). March 2026: banrep + ACI won Central Banking Awards. The year-one print is a logical, on-trajectory continuation — not a discontinuity.

**Why banrep acts this way:** (analysis) a central bank running the rail directly (vs leaving it to card networks) captures the public-good framing — low/zero cost to individuals, cash displacement, formalization/bancarization of the informal economy — which is the policy payoff, not a profit motive. The overlay-not-rebuild choice was political economy: it avoided fighting entrenched banks/wallets by letting them keep their rails.

## [3] Novelty / value-add / traction
The event itself is a milestone report, not a new capability — but the **traction is real and unusually strong**: 3-5x daily-volume growth in year one, 245 connected entities, and an evidenced (not self-reported) edge over Pix via third-party EBANX analysis on central-bank data. The value-add that's genuinely new vs the 6-month note: a full first-year dataset + the hard Pix comparison. Caveats the PR omits: the 45M/116M key-activation gap (many keys dormant); 62%-sub-COP-50k skews small-ticket, so the 262T-peso headline is volume-driven, not high-value; "36M clients" conflates registration with active use.

**Who captures value / what breaks it:** (analysis) because individuals pay nothing and banrep runs the core, the margin does NOT accrue to a single operator — it diffuses to the economy (lower cash friction, formalization) and to the 245 connected fintechs/banks who now compete on UX, not on owning a rail. Disintermediation risk: Bre-B commoditizes the "transfer" layer, squeezing card interchange and standalone-wallet moats — which is exactly why incumbents (Bancolombia, Davivienda) both lead volume AND feel the squeeze (see draft decree leveling card vs Bre-B costs in-corpus).

## [4] What's next / market sentiment
Next: QR for individuals (rolled out 1H2026), recurring/B2B payments, merchant acceptance deepening, cross-border links (Bre-B appears in regional roaming initiatives, e.g. PagBrasil RoamingPay). Risk 1 — **resilience/SLA**: the Feb-2026 multi-day Bancolombia outage took down Bre-B flows for its users; Nu Colombia's GM publicly demanded uniform SLAs with enforceable penalties ([[Nubank manager criticizes Bancolombia outage, urges Bre-B rules]]). On an overlay architecture one big node failing degrades the whole rail — a structural fragility, not a one-off. Risk 2 — fraud: as volume scales, fraud-liability rules and consumer protection (Banco de Bogotá already launched Bre-B fraud insurance in-corpus) become the contested frontier. Risk 3 — the dormant-key gap: sustained growth depends on converting registrations into habitual payers.

**Why the market goes this way:** (analysis) the counterintuitive second-order effect — Bre-B's very success concentrates systemic risk. The more the economy depends on one instant rail stitched across many operators, the more a single large bank's downtime becomes a national-payments event, which is why the policy fight is shifting from "adoption" to "SLAs, fraud liability, and resilience." The central question moves from "is adoption real?" (yes, demonstrably) to "can an overlay rail be made as resilient as a rebuilt-from-scratch one like Pix?"

## Sources
- banrep.gov.co — official 1-year release (2026-10-06): https://www.banrep.gov.co/es/noticias/bre-b-cumple-un-anio-en-colombia
- EBANX analysis (globenewswire, 2026-10-06): https://www.globenewswire.com/news-release/2026/10/06/3375461/0/en/colombia-s-bre-b-marks-one-year-with-faster-adoption-than-brazil-s-pix-ebanx-analysis-finds.html
- El Universal (262B pesos): https://www.eluniversal.com.co/economica/2026/10/06/primer-aniversario-de-bre-b-262-billones-de-pesos-en-transferencias/
- Vanguardia (~264B pesos): https://www.vanguardia.com/economia/2026/10/06/bre-b-mueve-casi-264-billones-en-un-ano-asi-cambio-la-forma-de-transferir-dinero-en-colombia/
- Note primary source: https://www.elcolombiano.com/negocios/bre-b-primer-ano-pagos-inmediatos-colombia-KI41948471
- Corpus: [[Colombia's Bre-B surpasses 600 million transactions in six months]], [[Colombia's Bre-B reaches 34.4 million users]], [[Colombia's Bre-B instant payment system launches]], [[Nubank manager criticizes Bancolombia outage, urges Bre-B rules]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **"36M clients" — active payers or registrations?** Registrations: 36M users with ≥1 key, but only ~45M of 116M keys have ever received a payment → a meaningful dormant share. The headline overstates active use. (answered, caveat stands)
2. **Is this a NEW event or a reprint of the 6-month note?** Fresh: this is the FULL first-year print (Oct 2025–Oct 2026, 1.7B tx / 262T pesos) vs the April 6-month note (638.6M tx / 100.3T pesos). New reporting period + new EBANX Pix comparison. (fresh)
3. **Is the "faster than Pix" claim independent or PR?** EBANX (a payments vendor with commercial interest in LatAm rails) produced it, BUT on central-bank + UN/IBGE data: 83% adult penetration yr1 vs Pix 65%. Directionally credible, source has an incentive to boost the rail. (answered, flag source interest)
4. **Does 262T pesos = big money or just volume?** Volume-driven: 62% of operations are under COP 50,000 (~USD 12); avg ticket ~COP 146,872. Low-value P2P rail, not high-value. (answered)
5. **USD figure — which FX?** $75.8B (note) / ~$80B (EBANX) differ by spot FX of the quote date; banrep quotes pesos only. Not a contradiction. (answered)
6. **Is the overlay architecture a hidden weakness?** Yes — Feb-2026 Bancolombia multi-day outage degraded Bre-B for its users; Nu Colombia demanded enforceable SLAs. One big node failing hits the whole rail. (answered, key risk)
7. **Who actually operates the core?** ACI Worldwide under contract to banrep — not banrep in-house (unlike Pix/BCB). Vendor dependency is a structural difference. (answered)
8. **Daily-volume growth — real or base-effect?** ~10M tx/day now vs ~2M/day at launch (~3-5x). Growth is real but off a low launch base. (answered)
9. **Penetration denominator games?** 83% is of ADULTS (~40M); 36M of ~53.7M population. Comparisons vs Pix use consistent adult bases per EBANX. (answered)
10. **Where's the margin / who monetizes?** Free to individuals, banrep runs core → no single operator captures rail margin; value diffuses to economy + 245 connected entities competing on UX. Disintermediates card interchange. (answered)
11. **Fraud and consumer-protection exposure?** Rising with scale; fraud-liability rules unsettled; Banco de Bogotá already launched Bre-B fraud insurance. Open frontier. (open/partial)
12. **Cooperatives/financial-inclusion claim verifiable?** 172+ cooperatives of 245 entities connected — supports the formalization narrative, but actual rural/unbanked usage not broken out. (partial)
13. **Did banrep pick a flattering base?** It anchors to key registrations and cumulative totals (both monotonically rising) rather than active-payer or retention metrics. (answered — PR framing flagged)
14. **Cross-border / next-leg traction?** QR-for-individuals live 1H2026; appears in regional roaming (PagBrasil RoamingPay); B2B/recurring expanding — plans, not yet major numbers. (open)
15. **Could it be downgraded to stale later?** No — distinct annual reporting period + official banrep milestone + new third-party analysis. Decisively fresh. (answered)

Importance: 4/5 — Flagship LatAm instant-payments story with demonstrable, third-party-validated traction (83% adult reach, 245 entities, 3-5x daily growth) and a meaningful structural read (overlay-vs-rebuild, concentrated resilience risk, card disintermediation). Not a 5 because it's a milestone report on an already-covered rail, not a new capability, and headline figures lean on registration/volume framing with a real key-activation gap.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-11]] (2026-10-11).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Bre-B is Colombia's central-bank-operated instant A2A payment rail (Banco de la República, launched 6 Oct 2025), not a company — so this is infrastructure/real-time-payments, adjacent to the Pix-style "public-good rail" category rather than a fundable asset. One-year scorecard: 36M clients (~32M individuals in a country of ~40M adults), 110M+ registered keys, and the system now runs >8M transactions/day — ~3x its first-month daily volume; accumulated value since launch ≈ USD 80bn (per EBANX analysis, via GlobeNewswire/FinancialContent, as of 2026-10-06). Note's own figures (1.7bn transactions, $75.8bn) are consistent with the lower-bound/earlier cut; the newer EBANX cut (~USD 80bn) is the fresher read. "Why now": the driver is a huge cash base — cash is still ~77.8% of Colombian transactions per Banco de la República (via EBANX), so instant-payment growth is a cash-displacement land-grab, not card-displacement (unlike Brazil, where Pix already overtook cards). Structure: the rail itself is a mandated monopoly utility (central bank owns it; barrier = regulation, not capital/network), while value accrues to the private layer riding on top — banks, wallets, acquirers, orchestrators (Movii, Plenti, dLocal, EBANX, Thunes, Mono, TumiPay all in-base integrating Bre-B).

**Competitive landscape.** Sector KPIs for rails/enablers: transaction count/day, value (TPV), % population reached, keys registered; for the private enablers — take rate and attach. Bre-B's position vs the regional benchmark: EBANX claims first-year adoption *faster than Pix* — 83% of Colombian adults using it after year 1 vs ~65% for Pix after its year 1 (per EBANX, via GlobeNewswire, 2026-10-06) `(analysis: vendor-adjacent framing — EBANX is a Bre-B commercial beneficiary, treat the "faster than Pix" claim as interested data)`. Pix benchmark for scale calibration: ~200M monthly active users (~80% of Brazil population) and 79.8bn transactions / BRL 35.36tn in 2025 (per Banco Central do Brasil, via ClearingPost / EBANX) — Pix moves ~8.6x the value of cards combined, i.e. the end-state is card-volume displacement, which Colombia has NOT yet reached. The actual competitive battleground is the enabler layer: who captures merchant acquiring, cross-border, and QR on top of the free rail. Moat for the protagonist (the rail): regulatory mandate + interoperability by law = strong, durable `(analysis)`; moat for the enablers: thin — the rail commoditizes basic transfers.

**Comps & multiples.** Bre-B itself has no equity/valuation — central-bank utility, so a trading multiple is not applicable ("no data" by design). Closest public comp is the build vendor: **ACI Worldwide (ACIW)** — built Bre-B with Banrep. FY2025: revenue $1.76bn (+10%), adj. EBITDA $506M (+9%), net income $227M; market cap ≈ $5.14bn (as of 2026-10). EV/Revenue ≈ 3.0–3.5x (Q1–Q2 2026); EV/EBITDA ≈ 14.3x (per stockanalysis.com / saasdb, 2026). Arithmetic sanity on EBITDA multiple: a ~$5.1bn cap company at ~14x EBITDA on $506M EBITDA implies EV ≈ $7.2bn ⇒ ~$2.1bn net debt `(analysis, EV not independently sourced — [UNSOURCED] net debt)`. In-line to cheap for a ~10%-grower payments-software name (EV/Rev 3x against ~10% growth is reasonable, not stretched). Internal comps (context, not valuations — these are adoption/launch datapoints, not deals):
- [[Colombia's Bre-B instant payment system launches]] — launch: 32M users / 17M txns in week 1
- [[Colombia's instant payments grow 3,300% in 2025]] — ACI Worldwide as the named rail builder
- [[Instant transfers driving real-time payments in Latin America]] — regional RTP context
- [[BBVA Colombia launches first real-time payroll payments via Bre-B]] — enabler/use-case expansion
No private-round or deal valuation surfaced for any pure Bre-B enabler ⇒ distribution not computed, qualitative comparison only.

**Risk flags.**
1. **Interested-source adoption claims.** The headline "faster than Pix" / 83% figures come from EBANX, a commercial beneficiary of Bre-B flows — adoption metrics (active vs merely registered keys) are not from an independent audit; "36M clients" may conflate registered with active. Why it matters: overstated penetration feeds overbuilt enabler capex.
2. **Cash, not cards, is the incumbent — ceiling risk.** With ~77.8% of transactions still cash, headline growth is off a low base; the hard part (sticky, recurring everyday spend and merchant acceptance) is unproven, and Pix's own card-displacement took years. Why: year-2 growth could decelerate sharply once the easy P2P cohort is captured.
3. **Rail commoditizes the enabler economics.** A free, central-bank mandated A2A rail compresses interchange/transfer fees to ~zero for the private layer (banks, wallets, acquirers). Why: disintermediation of card interchange hits issuer/acquirer revenue (ACI's clients) and squeezes the fintech integrators monetizing Bre-B — margin captured by the public rail, not the stack.

**What this changes (idea-lens).** Bre-B confirms the LatAm "public-rail-as-default" thesis Pix proved: central-bank instant rails become the dominant A2A method and re-route value away from card networks toward account-to-account `(analysis)`. Falsifiable thesis: within 12–24 months Bre-B's *value* mix shifts from P2P toward merchant/C2B, pressuring Colombian card interchange the way Pix did in Brazil. Trigger/catalyst to watch: Banrep's next moves (credit/installments on Bre-B, like Pix's roadmap) and merchant-QR rollout for individuals (slated H1 2026). Thesis breaks if cash share stays stuck >70% and C2B fails to scale — i.e. Bre-B stays a P2P-only rail.

Sources: https://business.ebanx.com/en/press-room/press-releases/colombias-bre-b-marks-one-year-with-faster-adoption-than-brazils-pix-ebanx-analysis-finds · https://www.globenewswire.com/news-release/2026/10/06/3375461/0/en/colombia-s-bre-b-marks-one-year-with-faster-adoption-than-brazil-s-pix-ebanx-analysis-finds.html · https://www.banrep.gov.co/en/news/six-months-operation-bre-b-34-million-registered-users · https://clearingpost.com/insights/pix-breaks-all-records-in-2025-798-billion-transactions-move-r-3536-trillion/ · https://en.wikipedia.org/wiki/Pix_(payment_system) · https://investor.aciworldwide.com/news-releases/news-release-details/aci-worldwide-inc-reports-double-digit-revenue-growth-full-year · https://stockanalysis.com/stocks/aciw/statistics/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
