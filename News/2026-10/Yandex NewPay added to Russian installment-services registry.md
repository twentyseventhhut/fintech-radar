---
title: "Yandex NewPay added to Russian installment-services registry"
date: 2026-10-06
retrieved: 2026-10-08
tags:
  - company/yandex
  - industry/bnpl
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: sfcae7ef5
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Yandex NewPay added to Russian installment-services registry

> [!info] 2026-10-06 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] ЦБ внёс принадлежащее Яндексу ООО «НьюПэй» в реестр операторов сервисов рассрочки. Это уже второе юрлицо группы с таким статусом: действующий «Яндекс Сплит» предоставляет ООО «Финансовые и платёжные технологии», которое находится в реестре с апреля. Для «НьюПэй» в реестре указан отдельный сайт splitpay․yandex․ru, который пока находится в разработке, тогда как действующий «Сплит» работает через ФПТ и splitbnpl․yandex․ru. Поэтому регистрация выглядит скорее как подготовка отдельного BNPL-контура или продукта — но официально о его назначении Яндекс пока не сообщил. ⬛️ Первая гипотеза — Яндекс разделяет BNPL на два операционных контура: классический «Сплит» останется на ФПТ, а через NewPay группа будет развивать отдельное направление рассрочки для внешних продавцов, QR/POS или white-label-инфраструктуру. ⬛️ Вторая — отдельное юрлицо нужно, чтобы изолировать портфель, риски, расчёты с мерчантами и регуляторную отчётность BNPL. С этого года продукт стал отдельным регулируемым финансовым б

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Yandex NewPay added to Russian installment-services registry
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On 2 Oct 2026 the Bank of Russia entered **OOO "NewPay"** (owned by Yandex) into the **register of installment-service (rassrochka/BNPL) operators** — publicly reported 5 Oct. This is Yandex's **second** legal entity with that status: the live **Yandex Split** is operated by **OOO "Finansovye i platyozhnye tekhnologii" (FPT)**, in the register since 1 Apr 2026 (the law's effective date). Registry shows NewPay a **separate site splitpay.yandex.ru, "under development"**; live Split runs on splitbnpl.yandex.ru.

Crucial de-PR fact the original note missed: **NewPay is not a greenfield entity.** Yandex **acquired NewPay on 28 Nov 2024** — at the time it was a service for accepting payments for goods/services via **SBP QR codes** (Fast Payment System). NewPay's operations were **suspended on 10 Feb 2026**, but the legal entity was kept alive "for developing other financial services of the group." So this is a **repurposing of a dormant QR-acquiring shell into a registered BNPL operator**, not a brand-new product launch.

→ Why structured this way: registration ≠ product. It is a **regulatory permission** (under 283-FZ, operating a rassrochka service without being in the register is prohibited). The site being "under development" means **nothing is live** — this is *announced/permitted*, not *launched*. The event's real content is "Yandex has secured a second BNPL licence slot," which it cannot do silently because the register is public.

→ What it reveals: NewPay's QR/SBP acquiring heritage makes the note's **first hypothesis (separate BNPL contour for external merchants / QR-POS / white-label infrastructure) materially more plausible** than framed — the entity already had merchant-acquiring DNA. The "splitpay" naming (vs Split's "splitbnpl") hints at a **pay/checkout-rail positioning** distinct from the consumer Split brand.

## [1] Competitors / peers
Russian register (per CB RF) held **14 operators on 1 Apr 2026** and **~21 by early Oct 2026** — including structures of **T-Bank (Tinkoff)**, **Alfa-Bank**, and **Sovcombank**; Sber (Podeli) is the other large BNPL. Globally the BNPL-into-regulation arc mirrors the EU (Klarna, PayPal under consumer-credit rules) and the UK FCA regime. Internally the corpus is rich on BNPL regulation elsewhere: [[Pix installment rules to be released by Brazil Central Bank]], [[Klarna and Worldpay bring installment payments to Italy's pagoPA]], [[Tamara secures UAE Central Bank regulatory approval]], [[Mastercard and Citi expand Flex Pay installments at checkout]].

→ Why the lay of the land is this way: 283-FZ turned BNPL from a "semi-marketing tool" into **regulated financial activity** (register, 5M RUB min capital, ₽50k limit, ≤6-month term, no hidden fees, BKI credit-bureau reporting above limit, ≤20%/yr penalty). Second-order: regulation **favors the incumbents with balance sheets** (banks T/Alfa/Sovcom, and Yandex via FPT). Yandex adding a *second* slot is defensive positioning in a market that is now a licensing game, not a growth-hack game.

## [2] Company history / fit
Yandex's fintech push: Yandex Pay, Yandex Split (consumer BNPL at checkout across Yandex ecosystem + external merchants), and the 2024 NewPay (QR/SBP acquiring) buy. Trajectory fits: Yandex is assembling a **merchant-acquiring + consumer-credit stack** around its marketplace/Lavka/Eats/Market commerce flywheel (cf. [[Yandex Lavka expands robotic delivery to 130 dark stores]] for the commerce scale it serves).

→ Why the company acts this way (analysis): a single entity (FPT) carrying both the live Split book **and** a new external-merchant/white-label line would **commingle portfolio risk, merchant settlement, and regulatory reporting**. Splitting entities lets Yandex **ring-fence the Split consumer book** from a new B2B/infrastructure contour — exactly the note's second hypothesis. The structural driver: under 283-FZ every operator reports to the CB (financial reporting from 2027), so **entity separation = cleaner supervisory boundaries** per product line.

## [3] Novelty / value-add / traction
Novelty is **low**. Nothing launched: splitpay.yandex.ru is "under development"; NewPay's prior QR business is *suspended*. No disclosed GMV, merchants, terms, pricing, or launch date. The only hard new fact is the **register entry** (a permission). Yandex has **not stated the entity's purpose** — both the note's hypotheses (external-merchant/QR/POS/white-label vs. risk/portfolio isolation) remain open and are not mutually exclusive.

→ Why value-add is unconfirmed: in BNPL the margin sits with **whoever holds the receivable and the merchant relationship**. A registered-but-dormant entity captures **zero** until a product ships. The *potential* value-add — reusing NewPay's SBP/QR acquiring rails to offer **installments at external-merchant POS** rather than only inside Yandex checkout — is credible given the entity's origin, but **entirely prospective (hypothesis)**.

## [4] What's next / market sentiment
Watch for: (a) splitpay.yandex.ru going live and its branding (consumer vs merchant-infra); (b) whether Yandex migrates any Split volume or keeps books separate; (c) terms vs the 283-FZ caps (₽50k, ≤6mo until 2028 then ≤4mo). Regulatory backdrop: CB RF supervision tightening, mandatory financial reporting from 2027, BKI reporting of defaults — raising compliance cost and **consolidating the market toward well-capitalized operators**.

→ Second-order (analysis): the register is public, so a competitor-watcher sees Yandex's intent before any product exists — this is a **telegraphed move**, limiting surprise. Counterintuitive effect: heavier regulation **entrenches Yandex/banks** and squeezes small/retailer-captive BNPL schemes, so a second Yandex slot is less "new product" and more "land-grab of regulated capacity."

## Top challenge/extra questions (10–15, second-order) — see /tmp/chl_yandex-newpay.md

## Sources
- Interfax: https://www.interfax.ru/business/1120380
- 1Prime (05.10.2026): https://1prime.ru/20261005/bank-873942391.html
- TKS: https://www.tks.ru/politics/2026/10/05/0014/kompaniya-yandeksa-voshla-v-reestr-operatorov-rassrochki-tsb/
- www1.ru (second operator framing): https://www1.ru/news/2026/10/05/u-iandeksa-poiavilsia-eshhe-odin-operator-rassrocki-split-uze-rabotaet-cerez-druguiu-kompaniiu.html
- NewPay acquisition (28.11.2024), 1Prime: https://1prime.ru/20241129/yandeks-853190834.html
- TAdviser NewPay (acquisition + suspension 10.02.2026): https://www.tadviser.ru/index.php/Компания:NewPay
- 283-FZ / register rules, Kontur: https://kontur.ru/articles/513
- CB RF register of installment operators: https://www.cbr.ru/admissionfinmarket/register/
- CB RF "new installment rules in force 01.04.2026", Garant: https://www.garant.ru/products/ipo/prime/doc/413891324/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is it really new?** Partially. The register *entry* (2 Oct 2026) is new, but NewPay is a 2024-acquired, Feb-2026-*suspended* QR/SBP entity being repurposed — not a greenfield launch. → mostly a regulatory permission.
2. **Announced or launched?** Announced/permitted only. splitpay.yandex.ru is "under development"; no live product, no date. → *not launched*.
3. **Freshness/duplicate?** Fresh. No prior corpus note covers Yandex Split/NewPay or this registry event (only tangential Yandex notes: Lavka, wearables, Moscow space). Not a re-run.
4. **What already did the same?** Yandex Split via FPT (register since 1 Apr 2026); Sber Podeli, T-Bank, Alfa, Sovcombank operators (~21 in register by Oct 2026). Yandex is at parity/incumbent, not pioneering.
5. **Did the prior version fly?** Split is live and real; NewPay's *own* QR business did NOT — suspended 10 Feb 2026. The shell is being reused, which is a negative signal on the original NewPay product.
6. **What is the entity actually for?** OPEN. Yandex has not stated purpose. Two live hypotheses: (a) external-merchant / QR-POS / white-label BNPL contour; (b) risk/portfolio/reporting isolation from Split. NewPay's QR-acquiring origin tilts toward (a).
7. **Precise mechanism delta vs Split?** Unknown — no product terms. Only signal: "splitpay" naming + QR/SBP heritage suggests a checkout/merchant-rail angle vs Split's in-ecosystem consumer BNPL. (hypothesis)
8. **Who's silent about what?** Everyone silent on: GMV, merchants, launch date, pricing, which book carries receivables, fraud/credit liability split between FPT and NewPay.
9. **Any numbers that matter?** None disclosed for NewPay. Context numbers: ₽50k limit, ≤6mo term, ₽5M min capital, ≤20%/yr penalty, financial reporting to CB from 2027.
10. **Why two entities and not one?** (analysis) 283-FZ makes each operator a supervised reporting entity; splitting ring-fences Split's consumer book from a new contour's risk/settlement/reporting. Structurally logical.
11. **Does regulation help or hurt Yandex?** Helps — favors well-capitalized incumbents; a second registered slot is a defensive land-grab of regulated capacity, squeezing small retailer-captive BNPL.
12. **Who captures the margin?** Whoever holds the receivable + merchant relationship. Dormant registered entity captures zero until a product ships. → value is prospective.
13. **Downside triggers?** Product never ships (shell stays dormant like the QR business did); CB tightens capital/reporting; cannibalization of Split.
14. **What-if it's just housekeeping?** Plausible mild case: Yandex simply had to register a kept-alive entity it intends to use, with no near-term launch — would make this a 1/5 non-event.
15. **Does this change the central question?** Yes slightly: from "new BNPL product?" to "is Yandex building a *merchant-facing/white-label* BNPL rail separate from consumer Split?" — unresolved but the better question.

**Importance: 2/5 — rationale:** Only a public register entry (permission), no live product, no numbers, undisclosed purpose, and the underlying entity's prior product was suspended. It is a real, correctly-reported, non-duplicate signal about Yandex's BNPL ambition under the new 283-FZ regime, which keeps it above 1/5, but there is no traction or confirmed novelty to justify more.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russia's installment/BNPL ("рассрочка") market roughly tripled to ~RUB 940bn turnover in 2025 (per T-Bank's "Shares"/Доли service data aggregating Доли, Yandex Split, Alfa's Podeli, Wildberries' Части et al., published 2026-02-03; up from ~RUB 300bn in 2024) — per T-Bank, via Interfax/TAdviser citations. "Why now": the market just shifted from unregulated commercial deferral to a licensed financial product. Federal Law No. 283-FZ took effect 2026-04-01: non-bank/non-MFO installment operators must hold ≥RUB 5m capital and sit in the Bank of Russia's operator registry; must report debt >RUB 50k to credit bureaus (БКИ); cannot charge contract/schedule-servicing fees; price in installments cannot exceed cash price; penalties capped at 20% p.a. of the overdue amount (per Kontur/Vedomosti, as of 2026-04). Structure: fragmented at the edges but anchored by a handful of ecosystem incumbents (T-Bank, Yandex, Alfa, Wildberries, Sber); barriers are now regulatory (registry + capital) plus distribution/network effects from captive marketplaces. As of 2026-10, 21 operators sit in the CBR registry (per 1prime/Interfax, 2026-10-05).

**Competitive landscape.** Sector KPIs: BNPL GMV/turnover, take rate, fintech penetration in marketplace GMV, loss rate, share of external (off-ecosystem) turnover. Players & basis of competition: distribution (captive marketplace checkout) and funding cost, not price — Yandex Split (via ООО ФПТ, in registry since Apr 2026), T-Bank Доли, Alfa Podeli, Wildberries Части, Sber. Recent moves: the pick itself — CBR entered Yandex's ООО «НьюПэй» into the registry (decision dated 2026-10-02, reported 2026-10-05), a second Yandex operator alongside Split/ФПТ, listing a separate in-development site splitpay.yandex.ru. De-PR: NewPay was acquired by Yandex in 2024 and its operations were paused on 2026-02-10 (per Interfax/1prime) — so this is a dormant shell being re-registered under the new law, NOT a live launch; Yandex has not stated NewPay's purpose. Protagonist position: ahead on distribution — ahead `(analysis)`, leveraging Yandex Pay/Split rails and marketplace reach; moat = network effects + ecosystem switching costs rather than balance sheet. Proprietary BNPL economics (NewPay ticket size, loss rate, merchant take) → `[UNSOURCED]`.

**Comps & multiples.** Parent Yandex (MOEX: YDEX) reported FY2025 group revenue RUB 1,441.1bn (+32% YoY) and adjusted EBITDA RUB 280.8bn (+49%, 19.5% margin); Q4'25 revenue RUB 436.0bn (+28%); 2026 guidance ~20% revenue growth — all from the official Q4/FY2025 ENG press release (yastatic.net IR, 2026-02-17). The fintech/Financial Services segment is in investment phase and is NOT separately profitable at the group level; fintech penetration in GMV reached ~25% in Q1'25 with external-turnover share rising (per TASS/Interfax secondary, 2025). FY2025 fintech GMV is reported around RUB 1.1trn / ~+80% in some press, but this conflicts with other data (RUB 1.1trn = 2024 group revenue) → treat as "no data / unverified". Internal comps (Russia installment/regulation precedent): [[Russian government backs installment-market bill with delay]] (2026-07, govt backed FZ with deferred commencement), [[Russia's central bank targets real estate instalment plans]] (2026-07, CBR tightening rassrochka pricing/disclosure), [[Buyer to close 5% stake deal in Wildberries bank by October]] (2026-10, marketplace-bank consolidation). EV/Revenue, EV/EBITDA, P/E not computed — NewPay is an unconsolidated internal shell with no standalone financials; distribution not computed, qualitative comparison only. `[UNSOURCED]` for NewPay-level multiples.

**Risk flags.** (1) Regulatory/execution overhang — the whole re-registration is a compliance artifact of FZ 283-FZ; second-order effect: capital, bureau-reporting and fee bans compress BNPL unit economics sector-wide, and credit-bureau visibility will surface previously-hidden borrower leverage (the same concern CBR raised on real-estate rassrochka), potentially slowing GMV growth. (2) Fragmentation/cannibalisation inside Yandex — running two operators (Split/ФПТ + NewPay) signals a deliberate split of contours (captive Split vs. external/white-label NewPay) but also raises reporting/governance complexity and the risk NewPay never actually launches (it was already paused once, Feb 2026). (3) Concentration/disintermediation — BNPL value sits with whoever owns checkout distribution; Yandex's edge is ecosystem-captive, so growth in external (off-Yandex) turnover depends on winning merchants away from T-Bank/Wildberries rails where it has no distribution moat.

**What this changes (idea-lens).** `(analysis)` The registry entry is regulatory plumbing, not a re-rating event — but it is a tell that Yandex intends to run a separate externally-facing BNPL/white-label contour (splitpay.yandex.ru) distinct from captive Split, isolating merchant risk and reporting under the new law. Falsifiable thesis: NewPay goes live as a merchant-facing/POS or white-label installment product for non-Yandex sellers within ~6–12 months. Trigger to watch: splitpay.yandex.ru leaving "in development" + first external-merchant onboarding; what breaks the thesis — NewPay stays dormant and the registration was purely defensive compliance to protect the licence.

Sources: https://www.interfax.ru/business/1120380 · https://1prime.ru/20261005/bank-873942391.html · https://kontur.ru/articles/513 · https://yastatic.net/s3/ir-docs/docs/2025/q4/fc756ee95baa6fa171ee77ac733d52be/4Q25_YDEX_Press_Release_ENG_short_6ee9.pdf · https://tadviser.com/index.php/Article:Installment_Services_(BNPL)_in_Russia · https://tass.com/economy/1964377 · https://www.cbr.ru/admissionfinmarket/register/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings layer. This note is a regulatory/registry item (NewPay added to the CBR installment-services registry), not an earnings release — "no full earnings report in the news." But Yandex is IR-covered, so this adds the reported financials of the segment the news touches: **Financial Services** (Финансовые сервисы — Yandex Pay, Split, Saves), which is where a NewPay/Split BNPL loop would book. Figures are from Yandex's own filings; the BNPL product line itself is **not** separately disclosed.

**Verdict (headline read).** BEAT / accelerating. Latest print = **Q2 2026 (reported 2026-07-29)**. Group revenue RUB 386bn (+16% YoY); adj. EBITDA RUB 89bn (+35% YoY, 23% margin); adj. net income RUB 48bn (+56% YoY); FY2026 guidance reaffirmed (revenue ~+20%, adj. EBITDA ~RUB 350bn). The segment relevant to this note — **Financial Services** — is Yandex's fastest-growing business: revenue **RUB 29.5bn (+51% YoY)** in Q2 2026, GMV **RUB 351bn (+39% YoY)**, and it is now **adj.-EBITDA-positive** (RUB 1.9bn, 6.5% margin, vs ≈ RUB −0.2bn a year ago). Note: Yandex's IR manifest still lists Q1 2026 as "latest_result"; the Q2 2026 release is live but not yet re-indexed, so Q2 figures below are sourced from Yandex's own newsroom + Russian press, with Q1 2026 quoted directly from the IR PDF.

**Key figures (with growth).**
- _Group, Q2 2026:_ revenue RUB 386bn (+16% YoY); adj. EBITDA RUB 89bn (+35% YoY), margin 23.0%; adj. net income RUB 48bn (+56% YoY). H1 2026: revenue RUB 759bn (+19% YoY), adj. EBITDA RUB 162bn (+41% YoY).
- _Group, Q1 2026 (IR PDF):_ revenue RUB 372.7bn (+22% YoY); operating profit RUB 46.0bn (+135%); adj. EBITDA RUB 73.3bn (+50%, 19.7% margin, +3.7pp YoY); net profit RUB 28.9bn (vs RUB −10.8bn); adj. net profit RUB 34.7bn (+171%). Net-cash position: cash + short-term deposits RUB 245.1bn; adj. net-debt/EBITDA 0.1x.
- _Financial Services segment (the news-relevant line):_
  - Q2 2026: revenue RUB 29.5bn (+51% YoY); GMV RUB 351bn (+39% YoY); off-ecosystem turnover now 59% of GMV (+19pp YoY); adj. EBITDA RUB 1.9bn (margin 6.5%).
  - Q1 2026 (IR PDF): revenue RUB 29.4bn (+83% YoY); GMV RUB 314bn (+30% YoY); off-ecosystem turnover +73% YoY; adj. EBITDA RUB 1.2bn (margin 4.0%, vs −14.5% a year ago, i.e. first profitable quarter).
- _No separate BNPL/Split disclosure:_ Yandex does not break out Split, NewPay, loan book, take-rate, reserves, or installment GMV. Financial Services GMV is defined (IR footnote 17) as "total volume of all user purchases via Yandex Pay products" — a payments-wide metric, not a credit book. So there are **no data** on the BNPL unit economics that the NewPay registry move actually concerns.

**By segment / driver.** Financial Services is the standout growth engine inside the Personal Services block (Personal Services total Q2 2026 revenue RUB 64.9bn, +32% YoY; the other leg, Plus & entertainment, grew only +8% in Q1 / with Plus subscription revenue RUB 28bn +27% in Q2). Within Financial Services the two drivers management names are (a) off-ecosystem expansion — external-merchant turnover rising from a 40% to a 59% share of GMV YoY, i.e. the business is increasingly pulled by third-party merchants, exactly the "external sellers / white-label" surface the NewPay hypotheses in this note point to; and (b) operating leverage flipping the segment from structurally loss-making (−14.5% margin a year ago) to profitable (4.0% → 6.5% margin), which management attributes to "scale + product quality + operating efficiency."

**vs expectations / prior period.** No sell-side consensus is published for Yandex's internal segments, so the beat is assessed vs prior periods, not vs Street [public consensus: none for this segment]. Financial Services revenue growth decelerated optically from +83% YoY (Q1) to +51% YoY (Q2), but that is a base effect — Q1 2025 was a depressed comp; on GMV the trend is clean acceleration (RUB 314bn/+30% → RUB 351bn/+39%). Crucially the segment holds and extends EBITDA-positivity (RUB 1.2bn → RUB 1.9bn; 4.0% → 6.5% margin) for a second straight quarter, so the Q1 profitability inflection was not a one-off. Group-level: revenue growth did soften (+22% Q1 → +16% Q2), consistent with the ~+20% FY guide. See prior Yandex items in base: [[Yandex Lavka expands robotic delivery to 130 dark stores]], [[Yandex to open flagship space in Moscow in November]].

**Guidance / forward.** FY2026 guidance **reaffirmed at both Q1 and Q2**: group revenue ~+20% YoY and adj. EBITDA ~RUB 350bn; capex 10–12% of revenue (≈ 5-yr average of 11%). No segment-level guidance for Financial Services or any BNPL/Split target is given — so the strategic intent behind the NewPay registration (separate BNPL loop / external-merchant / white-label) has **no quantified management guide**; treat the note's two hypotheses as `(analysis)`, unconfirmed by filings. Management tone on Financial Services is confident (repeatedly flags it as "the fastest-growing business"); what they stay silent on is credit quality — no loan-book size, no overdue/reserve ratios, no installment take-rate — which is the exact risk axis a newly CBR-regulated BNPL entity introduces. De-PR flag: they tout GMV and the EBITDA turn, not credit risk.

**Thesis-flags.**
1. _Financial Services is now a self-funding growth engine, not a cash sink._ Fact: segment adj. EBITDA went RUB −2.3bn (Q1'25) → +1.2bn (Q1'26) → +1.9bn (Q2'26). Why it matters: a profitable fintech arm can absorb a second regulated entity (NewPay) and a separate BNPL build-out without dragging group EBITDA — lowering the execution risk of the registry move this note describes. Second-order: supports the "separate operational loop / white-label infra" hypothesis, since Yandex can fund it internally.
2. _Growth is migrating off-ecosystem (external merchants 40%→59% of GMV YoY)._ Why it matters: this is precisely the external-seller / QR-POS / third-party surface that a dedicated NewPay/splitpay.yandex.ru contour would serve; the financials corroborate that strategic direction even though the product is undisclosed. Second-order: a regulated standalone BNPL operator is the natural legal wrapper for an external-merchant installment book.
3. _Opacity on credit metrics is the key unquantified risk._ Yandex discloses payments GMV but no BNPL loan book, reserves, or delinquency. Why it matters: CBR entry into the installment registry (this note's event) means NewPay becomes a regulated financial entity with reporting/capital obligations — yet investors have zero visibility into the credit exposure being regulated. Second-order: if a separate NewPay portfolio is being carved out (hypothesis 2 in this note), isolation of risk/reporting is plausible, but the figures to confirm it do not yet exist — `(analysis)`, watch Q3 2026 disclosure.

Sources: Yandex Q1 2026 press release (RUS, IR primary) https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf · Yandex Q2 2026 newsroom (official) https://yandex.ru/company/news/29-07-2026 · Interfax (Q2 group figures) https://www.interfax.ru/amp/1106242 · Bosfera (Q2 Financial Services +51%) https://bosfera.ru/press-release/vyruchka-finansovyh-servisov-yandeksa-vo-ii-kvartale-vyrosla-na-51 · Reuters/MarketScreener (Q2 +16%, dividend, guidance) https://www.marketscreener.com/news/yandex-reports-16-increase-in-q2-revenue-recommends-h1-dividend-at-110-rbls-share-ce7f51d2dc8af125 · semantic search over irdb: UNAVAILABLE this run (embedding-credit 402). BNPL/Split unit economics (loan book, take-rate, reserves): no data — not disclosed by Yandex.
<!-- /enrichment:earnings_review -->
