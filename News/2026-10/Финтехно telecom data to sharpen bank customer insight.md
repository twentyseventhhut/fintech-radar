---
title: "Финтехно: telecom data to sharpen bank customer insight"
date: 2026-10-06
retrieved: 2026-10-08
tags:
  - industry/banking
  - industry/ai
  - region/ru
  - type/commentary
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sc50d1f9f
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Финтехно: telecom data to sharpen bank customer insight

> [!info] 2026-10-06 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Телеком-данные могут помочь банкам и другим финансовым компаниям точнее понимать клиента и эффективнее взаимодействовать с ним. Об этом на форуме «ФинТех Х10» рассказала Ирина Лебедева, заместитель директора Т2 по коммерческой деятельности. Т2 предлагает использовать данные операторов для обогащения данных банков, МФО, страховых компаний и маркетплейсов через data clean rooms — доверенные среды для безопасного обмена данными. Т2 совместно с «Ростелекомом» располагает информацией о потребностях пользователей и предпочтительных каналах коммуникации. Это позволит точнее выбирать канал и момент для взаимодействия с клиентом. При этом в Т2 выступают за сокращение числа агрегаторов между финансовыми компаниями и телекомами. По словам Лебедевой, посредники создают «серые зоны», повышают риск злоупотреблений и уязвимости данных, тогда как прямое взаимодействие делает цепочку предоставления сервиса прозрачнее. Ещё один аргумент в пользу консолидации — быстрый рост объёмов данных: строительст

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Финтехно — telecom data to sharpen bank customer insight
_Analytical notes (not a post). Importance: 2.5/5 → rounded **2/5**._

## [0] What exactly happened (de-PR'd)
At the **"ФинТех Х10"** forum (FinTech Association's 10th-anniversary event, **6 Oct 2026, Moscow**, MIA "Rossiya Segodnya" press centre — the forum is real and the date matches this note), **Irina Lebedeva** — VP for mass-segment products at Rostelecom AND deputy GD for commercial activity at **Т2** (Tele2 Russia / T2 RTK Holding, a 100% Rostelecom subsidiary) — made a **commentary/positioning pitch**, not a product announcement:
- Telecom-operator data can help banks, MFOs, insurers and marketplaces understand customers better and pick the right **channel and moment** for outreach.
- Vehicle = **"data clean rooms"**: trusted environments where parties match on an **encrypted phone number** and compute joint results without exposing raw data. Т2 + Rostelecom hold data on user needs and preferred communication channels.
- She argued to **reduce the number of aggregators/intermediaries** between financial companies and telecoms: intermediaries create "grey zones", raise data-abuse/vulnerability risk; **direct interaction makes the service chain more transparent**. A second argument for consolidation: rapid growth of data volumes.

**+ Why framed this way / what it reveals.** This is a **vendor positioning argument disguised as a market-hygiene argument**. Т2 is Russia's #3–4 operator — a thinner data panel than MTS/MegaFon — so a *clean room that pools everyone's data* and *direct access that cuts out brokers* is exactly the structure that benefits a laggard trying to sell data directly rather than feed existing aggregators. The "grey zones / transparency" framing is genuine (it rides the 152-FZ tightening, see [4]) but also conveniently reroutes margin from intermediaries to Т2/Rostelecom. De-PR'd: **this is forum commentary restating a 2025–26 recurring Т2 message**; the actual Т2 clean-room product does **not launch until end-2027** (per the May-2026 CIPR roadmap below) and monetizes only from ~2030.

## [1] Competitors / peers
Telecom-data-for-banks in Russia is a **~10-year-old crowded market**; Т2 is the laggard, not the pioneer:
- **MTS** — clear leader. "MTS Big Data" / "МТС Скоринг" (scoring + anti-fraud, ~80M de-identified subscribers, 10k+ parameters). **MWS Confidential** (MTS Bank + MWS) already does joint scoring/anti-fraud via **SMPC** confidential computing — functionally a data clean room, claiming +5–20% scoring-model quality (date disputed across sources: ~2025 vs 2026; treat as unconfirmed but pre-dates/coincides with Т2's plan).
- **MegaFon** — longest pedigree via **oneFactor** (spun out 2015, risk/fraud scoring to Top-100 banks from ~2016; MegaFon bought it back 100% in 2022).
- **Beeline (VimpelCom)** — "Beeline Big Data & AI": scoring, thin-file verification, anti-fraud notifications, adtech; doubled big-data revenue back in 2018.
- **Rostelecom** (Т2's parent) — RT.DataVision/TData, DC assets; Т2's clean room extends the group's data play.
- **Non-telco clean rooms already live:** **VK Data Clean Room** (first client RIV GOSH / Rive Gauche, announced **17 May 2024**).

**+ Why the landscape is this way.** The scoring-data business commoditized (every operator sells the same mobile-usage features). An independent academic benchmark (Zenodo) actually found **credit-history data outperforms telecom data** for scoring — so standalone telco scoring is a weak moat. The differentiation has moved to the **trust/compute layer** (clean rooms, confidential computing), which is why MTS/VK already built it and Т2 is now scrambling to. Т2's only distinct angle: a *neutral Rostelecom-group* environment vs. MTS (which owns a competing bank and so is conflicted as a neutral data hub).

## [2] Company history / fit
- Tele2 Russia (2003) → sold to VTB 2013 → merged with Rostelecom mobile into **T2 RTK Holding (2014)** → **Rostelecom 100% (Mar 2020)** → rebranded **"Т2" (2023)**.
- #3–4 by subscribers; **no mature named scoring product** comparable to МТС Скоринг / oneFactor. Data business is **nascent / under construction** — consistent with the 2027-launch roadmap.
- Context tension: in 2026 Т2 and the "big four" were publicly feuding with banks over **mandatory call-marking/robocalls** — so Т2 is simultaneously a would-be data *partner* and an *adversary* of banks.

**+ Why Т2 acts this way.** A smaller panel means weaker standalone analytics → the only way for Т2 to play in data is to **pool** (clean room) and to **own the direct channel** (cut aggregators). The pitch is structurally forced by its #3 position, not visionary leadership.

## [3] Novelty / value-add / traction
**Low novelty, unproven traction.**
- Not new as a concept: telecom scoring dates to ~2015–16 (oneFactor); clean rooms live in Russia since VK/2024 and MTS/MWS 2025–26. Т2's own product launches end-2027.
- The one new-ish element: **Т2 as a direct seller building its own trusted environment + the explicit "cut out intermediaries" argument** — but this is a *roadmap*, not shipped.
- Traction is soft: Т2 (per May-2026 CIPR) claims cooperation with **"six leading banks"** — unnamed, framed as co-building, not revenue. The forum's value claims (telecom analytics lift scoring accuracy ~1–3%, churn prediction ~1–5%) are **vendor-supplied, unaudited** figures.

**+ Who captures the margin.** The real fight is **who owns the identity/match layer** (the encrypted phone number) that joins telco + bank data. Whoever runs the clean room captures a rent on every match. MTS already runs one (and owns a bank). Т2's bid is to become the *neutral* match layer — but neutrality is only credible if banks trust Rostelecom (a state-group) more than MTS, which is unproven. If they don't, Т2 stays a **data supplier into someone else's clean room**, capturing commodity data-feed economics, not the match rent.

## [4] What's next / market sentiment
- **Regulatory tailwind is the real story.** Russia's **152-FZ** tightened sharply in 2024–25: 233-FZ (Aug 2024) depersonalization provisions; **420-FZ turnover fines effective 30 May 2025** (repeat leaks up to 3% of revenue, min 15M₽; large one-off fines); new depersonalization rules from 1 Sep 2025; a contested Mintsifry bill to force businesses to hand **depersonalized data to a state GIS**. Turnover fines make **raw-data brokering legally dangerous** → the market pivots to **compute-on-encrypted / clean rooms**. Т2's pitch rides this wave.
- Also pending: a ЦБ **bank–telecom fraud-verification bill** (revived from 2018) — operators wary, banks (VTB) supportive.
- Market frame: Russian Big Data + AI market ~433B₽ (2024) → ~520B₽ (2025 est.), ~20% CAGR; the market norm is selling **depersonalized analytics, not raw data** — aligning with clean rooms. No clean standalone "telecom data monetization" figure found (open).

**+ Second-order.** The regulatory squeeze doesn't create new value — it **concentrates** it into whoever owns a compliant match layer. So the counterintuitive effect: tighter privacy law **advantages the incumbents** (MTS, VK) who already built confidential-compute infra, and pressures laggards like Т2 to either build fast or cede the margin. The "fewer aggregators" pitch is Т2 trying to legislate/argue its way up the stack before the window closes.

## FRESHNESS / DUPLICATE VERDICT
**FRESH.** No prior internal note covers this Т2 ФинТех-Х10 statement (grep for Т2/Lebedeva/clean-room/data-exchange across `News/` found no match; the only adjacent same-day note, [[Vedomosti AI adoption lifts demand for corporate data protection]], is a different story — AI-driven corporate data-protection demand, not telco-bank data sharing). The ФинТех Х10 forum (6 Oct 2026) is a genuine, dated new appearance. BUT note it **restates a recurring 2025–26 Т2 positioning** (Finopolis Oct-2025 "commercial data exchange"; CIPR May-2026 clean-room roadmap) — fresh *event*, low *novelty*.

## Sources
- Финтехно (Telegram) aggregated text (primary channel); https://max.ru/fintexno
- ФинТех Х10 forum (6 Oct 2026, Moscow): vbr.ru; ict2go.ru/events/72521; bosfera.ru/event_banner/finteh-h10
- Т2 clean-room roadmap (CIPR, May 2026): cnews.ru 2026-05-19; fonar.tv 2026-05-20; vedomosti.ru press_release 2026-05-19; forbes.ru/547528 (commercial data-exchange)
- Finopolis-2025 statement (9 Oct 2025): vedomosti.ru press_release 2025-10-09
- Competitors: MTS Скоринг (tadviser); MWS Confidential (kommersant/doc/8830638; mtsbank.ru); oneFactor/MegaFon (tadviser/megafon.ru); Beeline Big Data (bigdata.beeline.ru); VK Data Clean Room / RIV GOSH (tadviser, 17 May 2024)
- 152-FZ turnover fines (420-FZ, 30 May 2025): consultant.ru/legalnews/27142; garant.ru/article/1746375
- Market size 433→520B₽: kommersant.ru/doc/8195580
- Scoring benchmark (credit-history > telecom): zenodo.org/records/21901758
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is "ФинТех Х10" a real event and does the date fit?** — YES. FinTech Association's 10th-anniversary forum, 6 Oct 2026, Moscow; matches the note date 2026-10-06. (Earlier research confusion with Finopolis-2025 resolved.)
2. **Is this an announcement or commentary?** — **Commentary/positioning.** No product shipped; it restates Т2's recurring "commercial, direct, clean-room" message.
3. **Is Т2's data clean room live?** — **No.** Per the May-2026 CIPR roadmap: build legal+tech base and launch by **end-2027**; AI-agent interfaces 2028–29; Data-as-a-Service monetization from ~2030.
4. **Is a telecom clean room novel in Russia?** — **No.** MTS/MWS Confidential (SMPC) and VK Data Clean Room (RIV GOSH, 17 May 2024) already operate; telecom scoring dates to ~2015–16 (oneFactor).
5. **Who are the unnamed "six leading banks"?** — **Open.** Framed as co-building, not revenue; no names, no contract values.
6. **Are the value claims (scoring +1–3%, churn +1–5%) verified?** — **No.** Vendor-supplied; an academic benchmark suggests credit-history data outperforms telecom data for scoring.
7. **Who exactly are the "aggregators/intermediaries" Т2 wants to cut out?** — **Partly open.** Data brokers / scoring intermediaries reselling operator data to lenders (oneFactor, scoring bureaus, etc.); Т2 did not name specific firms in accessible sources.
8. **Is the "grey zones / transparency" argument genuine or self-serving?** — **Both.** Real (rides 152-FZ risk), but conveniently reroutes margin from brokers to Т2/Rostelecom.
9. **Why does Т2 specifically need a clean room?** — It's #3–4 by subscribers; a thinner data panel makes standalone analytics weak, so pooling + direct access is structurally forced.
10. **Who captures the margin in this stack?** — Whoever owns the identity/match layer (encrypted phone number). MTS already runs one and owns a bank; Т2 bids to be the *neutral* Rostelecom-group layer — neutrality unproven.
11. **Does the regulatory tightening help or hurt Т2?** — Net it **concentrates** value into incumbents with compliant compute infra (MTS/VK); it pressures laggard Т2 to build fast or cede the rent.
12. **Any conflict of interest between Т2 and banks?** — **Yes.** Simultaneous 2026 feud over mandatory call-marking/robocalls — Т2 is partner and adversary at once.
13. **Is there a hard market-size number for telecom data monetization?** — **Open.** Only whole-market Big Data+AI figures (~433→520B₽, ~20% CAGR).
14. **Is this a duplicate of a prior internal note?** — **No.** No prior Т2/Lebedeva/clean-room note in `News/`; the same-day [[Vedomosti AI adoption lifts demand for corporate data protection]] is a different story.
15. **What would raise the importance?** — If the "cut out aggregators" line became a concrete regulatory/commercial move (e.g., an ЦБ rule or a signed multi-bank clean-room contract) rather than forum commentary.

Importance: **2/5** — A real, dated forum appearance but fundamentally **commentary restating a 2025–26 positioning** from the #3 operator in a space MTS, MegaFon and VK already occupy; the actual product launches end-2027, "six banks" and value-lift claims are unverified vendor figures. The underlying theme (clean rooms / confidential computing for scoring under a tightening 152-FZ) is genuinely important (~4/5), but Т2's specific contribution here is a weak company scoop with no new traction.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-09]] (2026-10-09).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Protagonist is T2 (Tele2, a Rostelecom mobile asset) pitching telco-data enrichment for banks/MFOs/insurers/marketplaces via data clean rooms (DCRs) — a telco big-data / alternative-data monetization play, not a telecom-connectivity story. Market size: the *global* "data monetization in telecom" market is ~$6.31bn (2025) rising to ~$7.82bn (2026), cited ~24% CAGR (per The Business Research Company, via giiresearch/openpr, as of 2026); a separate "data monetization for telcos" read is $14.63bn (2026)→$28.37bn (2032), ~11.5% CAGR (per Research and Markets, 2026). RU-specific size for telco→bank data: **no data** — do not infer from the global figure. Structure: supply side is consolidated (MTS/MegaFon/Beeline/T2 are the only owners of nationwide mobile behavioral data; RU mobile-MNO market ~$17.0bn 2026, per Mordor Intelligence); the data-enrichment layer between telcos and banks is fragmented with aggregators/intermediaries — exactly what T2 wants to compress. Entry barrier is the data asset + regulatory licence to process it, not capital. Why now: (a) AI scoring raises the marginal value of alt-data features; (b) telcos chase non-telecom income (MTS targets ~50% of group income from non-telecom by 2026; MTS Web Services incl. Big Data = RUB 63.8bn, per MTS, as of 2025); (c) DCRs make cross-party enrichment possible without raw-PII transfer, lowering 152-FZ friction.

**Competitive landscape.** Sector KPIs: data-as-a-service ARR / revenue per partner, number of connected data-consumers (banks), scoring-lift / Gini uplift vs bureau-only, and match rate in the clean room — T2 discloses none of these `[UNSOURCED]`. Key players: MTS (own scoring + Big Data unit, bank captive = MTS Bank), MegaFon (service revenue RUB 445.4bn +9.6%, 2025, per ComNews), Beeline, and T2/Rostelecom; basis of competition = breadth/freshness of data, legal cleanliness of consent, and distribution into banks. Recent moves (dated): T2 announced its DCR / secure-data-exchange build-out on 2026-05-19/20 (per Vedomosti press release / Content-Review), roadmap: unify data to a standard + launch DCR by end-2027, then DaaS subscription (verified audience profiles), then AI-agent data-access interface in 2028-29; T2 says it already works with "six leading banks" (per Content-Review, 2026). At the ФинТех Х10 forum (news 2026-10-06), T2's Irina Lebedeva argued for cutting out aggregators as "grey zones." Protagonist position: **catching up / niche** `(analysis)` — T2 is #4 by scale (mobile revenue RUB 306.4bn +10.3%, 42.9m subs, 2025, per ComNews) and lacks a captive bank, unlike MTS; its moat is the Rostelecom fixed+mobile data combination and a push for "direct" (disintermediated) rails, but this is announced, not yet a live DaaS product.

**Comps & multiples.** No deal/valuation/round attaches to this commentary item → trading multiples **not computed** (qualitative only). Internal comps (grep fallback, `sem search` = HTTP 402): [[FinTech Omnisient raises $12.5m to empower lenders with privacy-safe data insights for underserved consumers]] — privacy-safe DCR for lenders scoring thin-file consumers, $12.5m raise (2025-11; round size, not market cap); [[TransUnion invests in SA FinTech Omnisient to power data-driven financial inclusion]] — incumbent-bureau + alt-data tie-up (the global analogue of T2's pitch); [[Nova Credit raises $35M Series D for cash-flow underwriting]] and [[Belvo passes 6 million verifications for Banco Azteca]] as alt-data-for-underwriting precedents; [[Vedomosti AI adoption lifts demand for corporate data protection]] on the privacy-cost side. Scale context for the RU telco subject: T2 mobile revenue RUB 306.4bn vs MTS RUB 807.2bn group — data-enrichment is a small, undisclosed slice of either; revenue contribution of telco→bank data = **no data**. Rich/cheap: n/a (no multiple).

**Risk flags.**
1. **Regulatory / 152-FZ consent.** The whole model rests on lawful consent chains; a scoring *score* may count as "technical information" rather than PII (per krediman, 2026), but raw enrichment does not — a tightening of consent rules or Roskomnadzor enforcement would gut the DaaS thesis. Second-order: T2 already lost subscribers "due to regulatory requirements" (per CNews, 2026-02), showing RU telco is regulation-exposed.
2. **Execution / announced-not-live.** DCR is a *roadmap to end-2027*, DaaS and AI-agent layers 2028-29 — revenue is years out and the "six banks" relationship is unquantified; MTS can monetize faster via its captive MTS Bank.
3. **Disintermediation cuts both ways.** T2 argues to remove aggregators, but banks could equally build direct links to larger MTS/MegaFon data, leaving #4-scale T2 as the marginal supplier — margin and share risk if it is not the default rail.

**What this changes (idea-lens).** `(analysis)` The signal is RU telcos racing to turn behavioral exhaust into a regulated DaaS layer for bank scoring — consolidation of the enrichment middle, not a re-rating. Falsifiable thesis: if T2's DCR launches on schedule (end-2027) with a disclosed bank count and priced DaaS, telco-data becomes a standard scoring input; trigger to watch = first named bank deploying T2 clean-room scoring at scale or a Roskomnadzor/CBR ruling on clean-room lawfulness. What breaks it: a consent-rule tightening or banks standardizing on MTS/MegaFon instead.

Sources: https://www.thebusinessresearchcompany.com/report/data-monetization-in-telecom-global-market-report · https://www.researchandmarkets.com/reports/5532748/data-monetization-for-telcos-market-by-service · https://www.mordorintelligence.com/industry-reports/russia-telecom-market · https://www.comnews.ru/content/244174/2026-03-12/2026-w11/1008/itogi-telekoma-2025-g-mts-megafon-bilayn-i-t2-glavnye-cifry · https://www.content-review.com/articles/74121/ · https://www.vedomosti.ru/press_releases/2026/05/19/t2-sozdast-bezopasnuyu-infrastrukturu-dlya-obmena-dannimi · https://storage.ir.mts.ru/mts-ir/images/documents/MTS_4kv_i_2025_prezentaciya.pdf · https://krediman.ru/advices/Chto_mobilniy_operator_rasskajet_o_vas_banku_mobilniy_skoring · https://www.cnews.ru/news/top/2026-02-26_sotovyj_operator_t2_poteryal
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
