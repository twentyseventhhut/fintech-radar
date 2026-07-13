---
title: "Sravni helps microlenders embed mandatory biometric verification"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/sravni
  - industry/lending
  - industry/regtech
  - region/europe
  - type/product
sources:
  - https://1prime.ru/20260626/sravni-871067695.html
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sb3c02a24
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# Sravni helps microlenders embed mandatory biometric verification

> [!info] 2026-06-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] «Сравни» поможет МФО встроить в клиентский путь обязательную проверку через Единую биометрическую систему без самостоятельного строительства инфраструктуры. Финансовый маркетплейс разработал SaaS-решение для дистанционного подтверждения личности при оформлении онлайн-займа и запустит его в августе.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://1prime.ru/20260626/sravni-871067695.html>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sravni helps microlenders embed mandatory biometric verification
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
Sravni — a Russian financial marketplace and, crucially, a licensed **operator of a financial platform (OFP)** — built a **SaaS product** that lets microfinance organisations (MFOs) plug the now-**mandatory** Unified Biometric System (UBS / ЕБС) identity check into their online-loan flow **without building their own UBS integration**. Delivery is WhiteLabel / Webview / iFrame, via ~3 API methods; Sravni placed equipment in a dedicated K1-class data centre with a KV2-class security subsystem to connect to the Center for Biometric Technologies (CBT / ЦБТ), the UBS operator. **Launch is scheduled for August 2026 — this is announced, not live.** No client count, no pricing, no signed MFO disclosed.

**+ Why structured this way / what it reveals:** The product is a direct play on a **regulatory pain point, not a market opportunity Sravni invented**. From **1 March 2026** Russian law requires online microloan contracts to be signed only after live biometric matching against the UBS; large MFCs (МФК) must comply from that date, smaller MKCs (МКК) from **1 March 2027**. The catch the PR omits: **as of 26 March 2026 not one of the 27 operating MFCs had connected to UBS** — direct integration costs ~15–30M rubles and the CB itself (Ilya Kochetkov) admitted UBS is "technically not ready" and under-populated. So Sravni is not selling convenience; it is selling a **compliance lifeline / arbitrage of an integration barrier**. Anchoring the pitch to "no need to build infrastructure" is honest framing of a real cost wall (15–30M rubles one-off vs a delegated per-request fee).

## [1] Competitors / peers
This is a delegated-identification (ОФП/bank intermediary) race, explicitly named in the Russian press:
- **T-Bank (Т-Банк)** — its biometric remote-loan system is in **final development**, first MFO integration "imminent" (as of Q1 2026). Most direct competitor.
- **RSHB (Россельхозбанк)** — also building delegated UBS identification for MFOs.
- **Direct integration** (15–30M rubles one-off) — only viable for the largest MFOs; the delegated route charges **~4–19 rubles per request**, the economics that suit small players.
- Vendor solutions exist too (e.g. ID.World "ID.Client" integration package for MFI–UBS).
- **Position:** parity / slightly behind. T-Bank is also pre-launch but signalling a sooner first integration; Sravni's August 2026 date is **5 months after the mandate already bit**, so first-mover advantage in the MFC tier is already partly lost to the regulatory clock.

**+ Why this lay of the land:** Whoever owns the UBS connection sets the per-request tariff for every MFO routed through them — a **toll-booth on a legally compulsory step**. That is why banks (T-Bank, RSHB) and an OFP (Sravni) all rushed in: it is recurring rent on a captive, mandated flow. The winner is decided less by tech (everyone hits the same CBT API) than by **distribution into MFOs and price per call** — and Sravni's edge is that it already sits in the MFO/lending marketplace funnel.

## [2] Company history / fit
Sravni is a **top-5 Russian fintech by revenue** (Smart Ranking, FY2024, +23% YoY), historically a comparison/sales marketplace (it pioneered online OSAGO sales; runs the annual "Sravni" fintech awards across banking, insurance, SME, **microfinance** and edtech). It already aggregates and routes MFO loan demand, and holds OFP status.

**+ Why Sravni acts this way:** A marketplace take-rate on lead generation is a **commodity, low-multiple business** exposed to the same MFOs it now serves. Becoming the **identity gateway** between MFOs and the state UBS converts a per-lead model into a **per-transaction infrastructure toll** on a legally unavoidable step — a stickier, recurring, higher-quality revenue line that deepens lock-in with the same MFO clients. The OFP licence is the structural enabler; the move is logically consistent, not a pivot.

## [3] Novelty / value-add / traction
**Novelty is modest.** Biometric UBS identification is mandated by the state; the UBS, CBT, the matching itself and the "Gosuslugi Biometriya" enrolment app all pre-exist. Sravni's value-add is **packaging + integration speed + capex avoidance**, not new technology. The K1/KV2 security posture is table-stakes for touching UBS, not differentiation.

**+ Why the value-add is real (with a caveat):** It is **genuinely useful** because the alternative (15–30M rubles direct build) is uneconomic for most of the ~27 MFCs and the ~hundreds of smaller MKCs facing the 2027 deadline, and ~25% of MFOs reportedly risk closure over compliance. So demand is real and regulator-created. **But traction is zero so far** — the product launches August 2026, no client is named, and the binding constraint may not be Sravni at all: **UBS itself is admitted not ready and under-populated**, the CB has floated **deferring fines**, and per-request economics (4–19 rubles) are set in part by whoever controls the pipe. **Who captures the margin:** the CBT/UBS owns the rail; intermediaries (Sravni/T-Bank/RSHB) capture a thin per-call toll; MFOs bear the cost. Sravni is the **toll collector, not the rail owner** — margin is real but capped and contestable.

## [4] What's next / market sentiment
Expect the August 2026 launch to land into a still-immature UBS, with first integrations and named MFO clients as the real signal to watch (vs the announcement). 2027 brings the MKC deadline — a much larger, more price-sensitive cohort where the cheap delegated route should dominate, favouring whoever has the lowest per-request tariff and broadest MFO distribution. Risks/sentiment: regulator may soften enforcement (fine deferral already floated), squeezing near-term urgency; UBS technical readiness and database coverage (~50M Russians enrollable today) cap addressable matching; sector consolidation (~25% MFO closure risk, MFC→MKC reclassification to buy a year) shrinks the client base.

**+ Why the market goes this way / second-order:** The mandate manufactures demand but the **state both owns the rail (CBT) and can throttle the deadline** — so intermediaries live on a margin the regulator can compress at will. Counterintuitively, the bigger the compliance pain, the more likely the CB defers enforcement, which **delays the very revenue** Sravni is building toward. The durable question is not "did Sravni launch a biometric product" but **"who wins MFO distribution and the per-call price war on a toll the state can re-price or postpone"** — Sravni's marketplace funnel is its best card; its weakness is that it owns none of the underlying rail.

## Sources
- 1prime.ru — Sravni biometric identity solution announcement: https://1prime.ru/20260626/sravni-871067695.html
- Rambler (reprint of the same announcement): https://finance.rambler.ru/business/56665719-sravni-predstavil-reshenie-dlya-podtverzhdeniya-lichnosti-po-biometrii/
- finance.mail.ru — "Not one MFC has connected to UBS yet" (26 Mar 2026): https://finance.mail.ru/article/biometrom-zajmyi-ne-izmerit-69203066/
- finance.mail.ru — how MFOs configure UBS connection (T-Bank, RSHB, Sravni named; 4–19 rub/request): https://finance.mail.ru/article/smi-uznali-kak-mfo-nastraivayut-podklyuchenie-k-ebs-69215025/
- Finmarket — most MFOs configuring two connection methods: https://www.finmarket.ru/main/article/6651263
- Vedomosti — ~25% of MFOs may close over biometrics: https://www.vedomosti.ru/finance/news/2026/02/19/1177636-mfo-mogut-zakritsya
- Banki.ru — CB proposed deferring fines for MFOs: https://www.vbr.ru/help/novosti/mfo-osvobodyat-ot-strafov-72250/
- Rossiyskaya Gazeta — biometrics required for microloans from 2026: https://rg.ru/2026/01/02/s-2026-goda-dlia-oformleniia-mikrozajmov-potrebuetsia-biometriia.html
- vc.ru — mandatory biometrics for online microloans from 1 March 2026: https://vc.ru/marketing/2810938-obiazatelnaia-biometriia-dlia-onlain-mikrozaiemov
- RBC Companies — Sravni in top-5 Russian fintechs 2024/2025 (+23% YoY): https://companies.rbc.ru/news/jglHKzvDss/sravni-voshel-v-pyaterku-krupnejshih-finteh-kompanij-rossii-2025/

### Related corpus notes
- [[Philippine central bank mandates server-side biometric authentication]] — analogous state-mandated biometric re-verification creating compliance-driven adoption (and ghost-account shutdowns).
- [[NPCI introduces biometric authentication for UPI]] — state/utility-driven biometric onboarding at scale (India), contrast in maturity.
- [[Australian bank introduces ID verification with selfie biometrics to fight fraud]] — market-driven (not mandated) biometric onboarding, useful counterpoint on adoption.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
1. **Is it live or announced?** Announced — launch scheduled for **August 2026**; no MFO client, no volume, no pricing disclosed.
2. **Is the underlying capability new?** No. Mandatory UBS biometric identification is state-imposed (law in force 1 Mar 2026); UBS, CBT and "Gosuslugi Biometriya" enrolment all pre-exist. Sravni packages integration, not new tech.
3. **What is the real differentiator?** Capex avoidance + integration speed for MFOs that can't justify a 15–30M-ruble direct UBS build. (analysis) Distribution via Sravni's existing MFO marketplace funnel, not technology.
4. **Who are the direct competitors and where do they stand?** T-Bank (final development, first MFO integration imminent), RSHB (building delegated identification), plus vendor packages (ID.World). Sravni is at parity / slightly behind on timing.
5. **Who captures the margin in the stack?** The CBT/UBS owns the rail; intermediaries (Sravni/T-Bank/RSHB) collect a thin per-request toll (4–19 rubles); MFOs pay. Sravni is toll collector, not rail owner — margin capped and contestable.
6. **Is demand real?** Yes, regulator-created: ~25% of MFOs reportedly risk closure over compliance, and as of 26 Mar 2026 **zero of 27 MFCs** had connected — a real, urgent gap.
7. **What's the binding constraint — Sravni or UBS?** UBS itself: CB (Kochetkov) admits it is "technically not ready" and under-populated (~50M Russians enrollable). Sravni's product can't outrun an immature rail.
8. **Could the regulator blunt the urgency?** Yes — the CB has floated **deferring fines** for non-compliant MFOs, which would delay the very revenue Sravni is building toward. (downside trigger)
9. **What's the TAM and timing?** MFCs from 1 Mar 2026 (small cohort, ~27); MKCs from 1 Mar 2027 (large, price-sensitive cohort) — the bigger, cheaper-route prize is a year out.
10. **Pricing power?** Weak — per-request tariff (4–19 rubles) is commoditised across intermediaries; competition is on price + distribution, not tech. Open on Sravni's exact tariff.
11. **Fraud-liability / accuracy risk — who eats a false match?** Open. PR is silent on who bears liability for biometric false accept/reject in a loan signed on Sravni's pipe.
12. **Exclusivity?** Open. MFOs are reportedly configuring **two** connection methods (direct + delegated), so Sravni faces non-exclusive, multi-homing clients.
13. **Does it fit Sravni strategically?** Yes — converts a commodity per-lead marketplace take-rate into a recurring per-transaction infrastructure toll on a mandated step, deepening lock-in with the same MFO clients. OFP licence is the enabler.
14. **Is this fresh vs the corpus?** Yes — no prior Sravni note and no prior Russian MFO/UBS biometric note exist in the corpus; the announcement and figures are new.
15. **What would change the verdict to higher importance?** A named first MFO integration live + disclosed volume/tariff + evidence Sravni out-distributes T-Bank in the 2027 MKC wave. Until then it's an announced compliance product.

Importance: 3/5 — A real, regulator-created demand wall (zero of 27 MFCs connected; ~25% closure risk) gives this genuine business logic and ties a top-5 Russian fintech into a mandated identity toll. But novelty is low (state-mandated, pre-existing UBS), the product is announced not live (Aug 2026), economics are a thin contestable per-call toll Sravni doesn't own the rail for, competitors (T-Bank, RSHB) are at parity or ahead, and the regulator can compress or defer the opportunity. Solid niche regulatory story, not a structural shift.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-28]] (2026-06-28).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russia's MFO lending market is large and growing: issuance reached ~1.5 trillion rubles in 2024 (per Expert RA, via TAdviser/AKM, Apr 2025), up >50% YoY (per Bank of Russia). Growth is bank-driven: MFOs affiliated with banks doubled volumes and lifted their share from 38% to 52% in 2024 (per CBR) — the top-3 issuers are bank/marketplace satellites (T-Finance 59.2bn, MoneyMan 55.87bn, Seimer 46.5bn rubles, 2024). Structurally the **registered base is consolidating at a historical low**: 10,273 register entries as of 5 Jun 2026 (incl. excluded), with 149 MFOs struck off in 2025 and 45 (all small MKCs) in 2026 YTD (per Brobank, citing CBR register). **Why now:** the binding driver is regulation, not the cycle — from 1 Mar 2026 online microloan contracts must be signed only after live UBS biometric matching (MFCs now, smaller MKCs from 1 Mar 2027). The second-order effect: a legally compulsory identity step sits in front of every online loan, so whoever owns the UBS connection collects rent on a mandated flow — the value is captured at the identity-rail layer, not in lending itself.

**Competitive landscape.** Sector KPIs for this delegated-identification play: **per-request tariff** (price per UBS check), **MFO distribution reach**, and **direct vs delegated capex** (15–30M-ruble build vs a per-call fee). The delegated tariff has already collapsed to **4–19 rubles per request, cut 3–6x since the start of 2026** (per finance.mail.ru) — a clear signal of price competition before the product even ships. Key players: **T-Bank** (system in final development, first MFO integration "imminent" per Q1 2026), **RSHB** (building delegated UBS identification), and vendor packages (ID.World "ID.Client"); MFOs are reportedly configuring **two** connection methods (direct + delegated), i.e. multi-homing. Sravni's position is **parity / slightly behind**: its Aug 2026 launch lands ~5 months after the MFC mandate bit, so first-mover advantage in the small MFC tier is partly lost to the regulatory clock. Its moat is **distribution, not technology** (analysis) — it already routes MFO loan demand through its marketplace funnel and holds OFP status; everyone hits the same CBT API, so the contest is price + reach.

**Comps & multiples.** No trading-comp multiples are computable here: Sravni is **private** (a financial marketplace / OFP, top-5 RU fintech FY2024, +23% YoY per Smart Ranking/RBC; the broader top-100 fintech cohort did 231bn rubles of revenue, +14% YoY, in 2024), and the biometric product carries **no disclosed client count, pricing, or volume** — so EV/Revenue, P/S and price-per-user = **no data**. The rivals are units inside larger groups (T-Bank, RSHB), not separately quoted on this line — multiples = **no data / [UNSOURCED]**. The only hard "multiple" is the build-vs-delegate arithmetic: direct UBS integration ≈ **15–30M rubles one-off** vs a delegated **4–19 rubles per request** — at, say, 10 rubles/check a 30M-ruble build equals ~3M checks before delegation is dearer, which is why the route fits small, low-volume MKCs and the largest MFCs build their own. Distribution not computed (fewer than 3 comparable public figures); qualitative comparison only. Internal corpus comps (state-mandated / utility-driven biometric onboarding, none Russian or MFO-specific): [[Philippine central bank mandates server-side biometric authentication]], [[NPCI introduces biometric authentication for UPI]], [[Australian bank introduces ID verification with selfie biometrics to fight fraud]] (market-driven counterpoint), plus the identity-layer-on-payments analogue [[Zimpler introduces ID+ identification layer for payments]].

**Risk flags.**
1. **Margin is a thin, contestable toll Sravni doesn't own.** The CBT/UBS owns the rail; intermediaries collect 4–19 rubles/request already cut 3–6x in months — a commoditised, price-war revenue line the rail owner can re-price. Second-order: even if Sravni wins distribution, unit economics compress toward the floor.
2. **Regulator can throttle the demand it created.** The CB has floated deferring fines for non-compliant MFOs, and UBS is admitted "technically not ready" / under-populated — a deferral delays the very revenue Sravni is building toward, making near-term TAM hostage to enforcement timing.
3. **Shrinking, multi-homing client base.** The register is consolidating (149 struck off in 2025, 45 in 2026 YTD; ~25% of MFOs reportedly at closure risk) and clients configure two connection methods — so Sravni faces fewer, non-exclusive customers and no lock-in on the identity call itself.

**What this changes (idea-lens).** This is a niche, regulator-manufactured re-rating of Sravni's revenue *quality* (per-lead take-rate → recurring per-transaction toll), not a structural sector shift (analysis). Falsifiable thesis: Sravni's edge is winning the larger, price-sensitive **MKC cohort that mandates from 1 Mar 2027**, where the cheap delegated route should dominate. **Trigger to watch:** a named first MFO integration live with disclosed volume/tariff after the Aug 2026 launch, and evidence Sravni out-distributes T-Bank into the 2027 MKC wave. **What breaks it:** a CB fine deferral or a T-Bank/RSHB tariff undercut — either would gut the near-term economics before scale arrives.

Sources: https://tadviser.com/index.php/Article:Microfinance_organizations_(MFIs)_in_Russia · https://www.akm.ru/eng/news/the-mfo-market-in-the-russian-federation-increased-by-50-in-2024/ · https://www.cbr.ru/eng/microfinance/ · https://brobank.ru/zakrytye-mfo-2026/ · https://finance.mail.ru/article/smi-uznali-kak-mfo-nastraivayut-podklyuchenie-k-ebs-69215025/ · https://finance.mail.ru/article/biometrom-zajmyi-ne-izmerit-69203066/ · https://companies.rbc.ru/news/jglHKzvDss/sravni-voshel-v-pyaterku-krupnejshih-finteh-kompanij-rossii-2025/ · https://smartranking.ru/ru/ranking/fintech/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
