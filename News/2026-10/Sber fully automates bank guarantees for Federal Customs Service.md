---
title: "Sber fully automates bank guarantees for Federal Customs Service"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/sber
  - industry/banking
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.sberbank.ru/ru/sberpress/all/article
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sbc543279
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Sber fully automates bank guarantees for Federal Customs Service

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Полностью автоматизировал выпуск банковских гарантий для Федеральной таможенной службы: процесс теперь занимает около семи минут вместо нескольких часов и проходит без участия сотрудников банка

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.sberbank.ru/ru/sberpress/all/article>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sber fully automates bank guarantees for Federal Customs Service
_Analytical notes (not a post). Importance: 2/5. Freshness: fresh (no prior corpus note on Sber guarantees / customs / FCS)._

> Primary PR is dated **9 Oct 2026** (bosfera.ru / bankinform.ru), re-reported in the 2026-10-12 digest. Single-source bank PR; no FCS corroboration, no volume/value/error metrics disclosed.

## [0] What exactly happened (de-PR'd)
Sberbank says it moved issuance of **customs bank guarantees (гарантии в пользу ФТС)** into a "fully autonomous" mode: the system generates and e-signs the guarantee (УКЭП), routes it **through the Bank of Russia** to the Federal Customs Service, and processes the returned receipts — removing >10 manual steps, enabling 24/7 issuance in ~7 min vs "several hours," "without bank-employee involvement." First live guarantee issued to "Velikonovgorodsky myasnoy dvor" (Adept Group).
- **Why framed this way / what it reveals:** The PR sells a time metric (7 min, no human), but a customs guarantee is a *credit* product — the bank is on the hook if the importer defaults on duties. "No employee" almost certainly means **autonomous document issuance against a pre-approved client limit**, not autonomous underwriting (analysis; PR phrasing "credit processes autonomous" is ambiguous — red-team Q2). Sber's own public guarantee offer already advertised "рассмотрение до 5 минут" in 2025, so "minutes" is not a marketing step-change; the genuine delta is **end-to-end straight-through processing to FCS with no human in the loop**.
- "Через Банк России" is **not** Sber-proprietary: CBR runs the shared electronic message-exchange rails with FCS for all accredited banks (cbr.ru/development/feddc/cust). So Sber built an STP layer *on top of* existing shared infrastructure, not new rails.

## [1] Competitors / peers
Russian guarantee market, portfolio shares @30 Jun 2025 (CBR via Kommersant, 10 Sep 2025): **Sber RUB 2.4 trn (#1, ~22% of the RUB 10.75 trn total)**, Alfa 2.0, Gazprombank 1.5, VTB 1.36, Sovcombank 0.97; top-5 ≈ 75%.
- **VTB** launched electronic customs guarantees for small business in **Apr 2021** (first = RUB 45 m; Q1'21 issuance tripled YoY to >RUB 3 bn) — e-issuance to FCS is ~5 years old at rival banks.
- **Alfa-Bank** relaunched an AI-equipped online guarantee platform in **Mar 2025** (scoring + status monitoring).
- As of Oct 2025 there were **78 customs-guarantee offers across 52 banks** — a crowded, commoditized sub-segment.
- **Position:** Sber may be *first on the narrow claim* of zero-human STP specifically for FCS guarantees, but no dated competitor disclosure confirms or refutes that — treat "first" as unverified (analysis). The lay of the land: electronic customs guarantees are table stakes; automation of the issuance workflow is where the leaders now compete on cost-to-serve.

## [2] Company history / fit
- **Apr 2024:** Sber began transmitting electronic *tax* guarantees directly to ФНС.
- **2025:** Sber moved ФНС (tax-authority) guarantees to the **same** autonomous, ~7-min, >10-steps-removed, CBR-routed pattern.
- **9 Oct 2026:** Sber extends that identical pipeline to **FCS / customs** — the item here. So this is a **template reuse**, the "next phase" of an existing autonomous-guarantee engine, not a from-scratch build.
- **Why Sber acts this way:** Guarantees throw off large, low-risk fee income — system-wide guarantee commission was **RUB 113 bn in H1'25 (>10% of banking net fee income)**, but growth has decelerated to ~+4% YoY and the portfolio *shrank* −2.6% YTD. With volume growth stalling, the #1 player competes on **cost-to-serve and throughput** (automate the human out) rather than volume — a classic margin-defense move in a maturing product line (analysis). Fits Sber's broader 2026 automation push (AI agents across SberBank Online, AIFA analyst, GigaChat tooling).

## [3] Novelty / value-add / traction
**Incremental, genuinely live for ≥1 deal.** (a) FCS e-guarantee technology dates to **Apr 2017** (industry-wide, УКЭП exchange); (b) Sber ran the identical autonomous architecture for tax guarantees in 2025; (c) rivals already offer electronic (VTB 2021) and AI-driven (Alfa 2025) guarantee platforms. The narrow novelty = fully employee-free, 24/7 STP applied to the customs use-case, by the market leader. **Traction:** one named live transaction; **no** volume, value, ticket-size, error-rate or FCS-acceptance-latency data — so "7 min / no employee" is an unverified single-source claim (red-team Q1, Q3, Q13, Q15).
- **Where the value really is:** the economics are internal (lower cost-to-serve, faster time-to-money for importers freeing working capital). The guarantee itself is commoditized; margin is captured by whoever has the cheapest automated pipeline + the pre-approved-limit relationship — Sber's distribution advantage, not the automation per se, is the moat (analysis).

## [4] What's next / market sentiment
Expect Sber to roll the autonomous engine across remaining guarantee types (44-FZ/223-FZ procurement, excise) and push customs volume via pre-approved limits for foreign-trade SMEs. Competitors (VTB, Alfa) will match the STP claim; the differentiator converges back to pricing and limit availability.
- **Structural backdrop:** sanctioned, domestic-only bank; **global fintech relevance ~1/5** (OFAC/EU-sanctioned, unverifiable). Russian relevance ~2–3/5 as a trade-finance automation data-point in a RUB 10.75 trn market whose growth has stalled — automation is a defensive response to that stall, not an expansion story (analysis). Risk: autonomous 24/7 credit issuance with no disclosed fraud/fallback controls is an operational-risk question the PR is silent on.

## Related internal notes
- [[Sberbank H1 2026 net profit rises 20.4% to RUB 995bn]] — scale/financial-strength backdrop of the #1 guarantee issuer.
- [[Sber teaches AIFA financial analyst to self-plan analysis]] — same 2026 "autonomous/agentic" automation theme.
- [[Sber adds car-wash booking and payment to SberBank Online]] — Sber's broader workflow-automation / embedded-service push.
- [[SberInvestments launches GigaChat tool explaining portfolio moves]] — GigaChat/AI productization trajectory.

## Sources
- Sber PR (bosfera.ru, 9 Oct 2026); bankinform.ru №143353 (~9 Oct 2026).
- Kommersant doc/8024556, 10 Sep 2025 (CBR: RUB 10.75 trn portfolio @1 Jul'25; Sber 2.4 trn / ~22%; RUB 113 bn H1'25 fee income).
- logistics.ru, 14 Jun 2017 (FCS e-guarantee tech, Apr 2017). Kommersant doc/4770873, 12 Apr 2021 (VTB first e-customs guarantee RUB 45 m).
- comnews, 15 Apr 2024 (Sber e-tax guarantees to ФНС); comnews, 21 Mar 2025 (Alfa AI guarantee platform).
- FCS bank registry: Order No. 463 (25 May 2020), customs.gov.ru open data; CBR FCS message formats cbr.ru/development/feddc/cust.
- Caveats: 7-min/no-employee and "first fully automated customs guarantee" = single-source Sber PR, no FCS confirmation; +44% customs-growth figure reported but not reconfirmed in the primary source; no customs-specific volume disclosed.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 2/5** — Real, live (≥1 deal) operational improvement and a credibly "first" zero-touch customs-guarantee STP in Russia from the #1 issuer (~22% share). But it is single-source bank PR with no FCS corroboration, no volume/value/error metrics, built on 9-year-old FCS e-guarantee rails and Sber's own 2025 tax-guarantee template. Global fintech relevance ~1/5 (sanctioned, domestic-only, unverifiable); Russian relevance ~2–3/5 as a trade-finance automation data-point.

**Freshness: FRESH** — no prior corpus note covers Sber bank guarantees, customs, or the FCS; this is a genuinely new development (not a reprint/re-framing of an existing note). It is, however, an *incremental* extension of Sber's own un-noted 2025 tax-guarantee automation.

## Red-team questions
1. **Is the 7-min figure independently verified?** Open — Sber-only; no FCS/third-party confirmation.
2. **Does "no employee involvement" mean autonomous credit approval, or just autonomous document issuance against a pre-approved limit?** Mostly open; lean = issuance automated, underwriting pre-done (PR phrasing ambiguous).
3. **Live at scale or a single showcase deal?** One named live deal (Adept/Velikonovgorodsky); scale open.
4. **Is e-issuance to FCS itself new?** No — FCS e-guarantee tech dates to Apr 2017; VTB live since Apr 2021.
5. **Had Sber already done this for tax guarantees?** Yes, in 2025 — same architecture; customs is an extension.
6. **Sber's customs-guarantee volume/value?** Open/undisclosed.
7. **Sber's overall guarantee share?** ~RUB 2.4 trn / 10.75 trn ≈ 22%, #1 (CBR, 30 Jun 2025).
8. **Is the customs sub-market big enough to matter?** Growing fast (+44% reported), 78 offers / 52 banks (Oct '25), but no standalone RUB figure — partly open.
9. **Is "через Банк России" Sber-proprietary?** No — CBR runs the shared FCS message-exchange rails for all banks.
10. **Do competitors have equivalent zero-touch FCS automation?** Open — VTB/Alfa have electronic/AI platforms; no dated competitor claim of fully employee-free FCS STP found, so "first" is plausible but unverified.
11. **Does a distinct customs "Single Resource of Bank Guarantees" exist?** Not confirmed — customs uses FCS registry + CBR exchange (the 44-FZ EIS guarantee registry is a different world; don't conflate).
12. **Any FCS-side quote/endorsement?** No — bank-side PR only.
13. **Does ~7 min include FCS acceptance, or only submission?** Open — PR says "from application to guarantee at FCS"; whether FCS acceptance is within 7 min is unclear.
14. **Global relevance given sanctions?** Low/confirmed — Sber is OFAC/EU-sanctioned, domestic-only.
15. **Fraud/fallback controls for autonomous 24/7 issuance?** Open — no error-rate, fallback, or fraud-control disclosure.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian bank-guarantee / trade-finance digitization. The aggregate Russian bank-guarantees-and-sureties portfolio reportedly grew from ~RUB 10trn to ~RUB 11trn over the last three years (per Bank of Russia, via bankinform.ru/consult-cct.ru, as of 2026) — a large, regulated, paper-heavy segment where the "product" is a legally binding undertaking routed between bank → CBR → the beneficiary state agency (FTS). Structure: concentrated at the top (Sber/VTB and a few large banks dominate because customs authorities require a minimum national-scale credit rating to accept a guarantee — a regulatory entry barrier, per cis-legislation.com). Value in the chain is shifting from manual underwriting/ops toward STP (straight-through processing): Sber says the new flow removes 10+ manual stages, runs 24/7, and cuts issuance to ~7 minutes vs several hours (bosfera.ru / bankinform.ru). "Why now": this is stage two of a credit-process digitization push — Sber moved *tax*-authority guarantees to autonomous mode in 2025, now *customs* (FTS) in 2026 (analysis). Driver = CBR's 2025–2027 Financial Market Development Programme explicitly targeting digitization of foreign-trade settlements and payment infrastructure (cbr.ru).

**Competitive landscape.** Sector KPIs: guarantee portfolio volume (RUB), issuance time / cost-to-serve, and acceptance by state beneficiaries (rating-gated). Key players: Sber (incumbent scale leader), VTB (the main digital-guarantee challenger), plus Alfa and other top-20 banks. Basis of competition = speed + cost-to-serve + distribution to corporates, not price of the guarantee itself. Recent peer move: VTB ran the first Russian *digital* bank guarantee into commercial operation on the Masterchain blockchain platform — a RUB 392m (~$5m) guarantee in favour of MTS, launching industrial issuance of electronic guarantees ([[VTB takes large Ozon share stake as collateral]] is a separate VTB item; the digital-guarantee item is web-sourced, thefintechtimes.com). Globally, Standard Chartered completed the first ICC-Swift-API-standard digital bank guarantee via Komgo in Jan 2026 (see [[Standard Chartered completes ICC-Swift digital bank guarantee via Komgo]]). Protagonist's position: **ahead on the FTS/state-agency rail specifically** — Sber is automating the *full* bank→CBR→FTS loop end-to-end, which is a different moat (switching costs + direct state-agency integration) than VTB's blockchain-issuance play. Moat = scale + entrenched state-channel integration (analysis); no proprietary per-product economics disclosed → `[UNSOURCED]`.

**Comps & multiples (IR grounding — PRIMARY evidence).** No valuation/round attaches to this product news, so trading multiples are not the point; Sber's *own filed results* frame the issuer. Per Sber FY2025 Summary Consolidated IFRS Financial Statements (12M 2025, English, dated 2026-02-26 — PDF: https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf): FY2025 net profit RUB 1,705.9bn (+7.9% YoY), net interest income RUB 3,556bn (+18.5% YoY), EPS RUB 77.8 (+8.0%), ROE 22.7% achieved amid a Russian economic slowdown (figures corroborated via TASS/Investing.com; Q3/9M 2025 presentation dated 2025-10-28: https://www.sberbank.com/common/img/uploaded/files/info/presentation_q3_z2lvsxdf_2025.pdf). Read-through: this automation touches cost-to-serve / operating efficiency and SberBusiness (SME transactional) stickiness, not a new revenue line — too small to move the P&L, so treat as a margin/retention lever, not a growth catalyst. Internal comps (grep fallback — semsearch down, OpenRouter 402): [[Standard Chartered completes ICC-Swift digital bank guarantee via Komgo]] (global interoperability standard, Jan 2026). No directly comparable Russian deal/valuation in base. EV/Revenue, EV/EBITDA, P/E = not computed (no free market-cap source for a sanctioned, delisted-from-Western-venues name) → `[UNSOURCED]`.

**Risk flags.**
1. **Single-beneficiary / regulatory-rail concentration.** The flow depends on the bank→CBR→FTS integration; any change in FTS/CBR acceptance rules, formats, or the rating threshold for accepted guarantees (cis-legislation.com) could force re-engineering. Second-order: the moat is also the dependency.
2. **Sector tightening into 2026.** Press flags tougher bank-guarantee conditions and rising risk for businesses in 2026 (Kommersant/Vedomosti) — if underwriting standards tighten, faster *issuance* doesn't help volumes and could raise claim/fraud exposure on auto-approved guarantees (no human in the loop). Second-order: speed without commensurate risk controls is a liability vector.
3. **Commoditization / no durable lead.** VTB (blockchain issuance) and others are digitizing the same workflow; a 7-minute SLA is a catch-up target, not a lasting moat. Second-order: efficiency gains get competed away into price/service, not retained as margin.

**What this changes (idea-lens).** `(analysis)` This is incremental STP, not a re-rating — it signals Russian trade-finance back-office moving to lights-out processing, with state-agency integration (customs/tax) as the contested terrain rather than the guarantee product itself. Falsifiable thesis: if Sber publishes guarantee-issuance volume/share gains in SberBusiness after rollout, the efficiency play is converting to share; watch the FY2026 corporate/SME segment commentary. What breaks it: no disclosed volume lift → it stays a PR-grade ops improvement with no measurable P&L or share effect.

Sources: https://bosfera.ru/press-release/sberbank-avtomatiziroval-poluchenie-tamozhennyh-bankovskih-garantiy · https://bankinform.ru/news/143353 · https://thefintechtimes.com/vtb-bank-first-in-russia-to-issue-a-digital-bank-guarantee-via-russian-blockchain-platform/ · https://ffnews.com/newsarticle/paytech/standard-chartered-completes-first-icc-swift-api-standards-digital-bank-guarantee-transaction-through-komgo · https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf · https://tass.com/economy/2092243 · https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · http://www.cbr.ru/content/document/file/174775/fm_development_programe_2025-2027.pdf · https://www.kommersant.ru/doc/8360489
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_This is a product story (full automation of bank-guarantee issuance for the Federal Customs Service), not an earnings release. The block below frames Sber's latest reported results as CONTEXT for the issuer's scale and financial health. Source priority: Sber's own IFRS filings (ir_latest.json). Semsearch dense retrieval was down (OpenRouter 402); figures pulled via BM25/FTS over the IR DB from the filing text._

**Verdict (headline read).** IN-LINE / modest BEAT on profit vs the prior year — record FY2025 but decelerating. FY2025 (12M 2025, audited IFRS) net profit **RUB 1,705.9bn (+8.0% YoY)**, attributable to shareholders **RUB 1,707.4bn (+8.0%)**, EPS **RUB 77.81 (+8.0%)**; driven by net interest income **RUB 3,556.0bn (+18.6%)** on balance-sheet growth, partly offset by a sharp rise in credit-loss charges and opex. No forward guidance in the summary statements (new strategy set at the Dec 2025 Investor Day). No public-consensus number is available in the corpus, so beat/miss is stated vs the prior year, not vs Street. The product story itself touches a small fee line: B2B "Guarantees and documentary operations" net fee income was **RUB 61.4bn in 2025 (−4.4% YoY from RUB 64.2bn)** — automation targets throughput/cost in exactly this book.

**Key figures (FY2025 IFRS, with YoY).** All figures from the FY2025 Summary Consolidated Statement of Profit or Loss / Financial Position unless noted; RUB bn.
- Net interest income **3,556.0** vs 2,999.6 — **+18.6%** (gross interest income 8,651.6 +26.2%; interest expense −5,662.4 +35.3% — funding cost rising faster than asset yield under high key-rate conditions).
- Net fee & commission income **833.7** (1,217.1 income − 383.4 expense) vs 842.9 (1,172.1 − 329.2) — **−1.1%**: fee income +3.8% but fee expense +16.5%, so the net line slipped.
- Operating income **3,487.4** vs 3,097.2 — **+12.6%**.
- Staff & administrative expenses **1,237.4** vs 1,062.6 — **+16.5%** (opex outgrew revenue — negative operating-leverage flag).
- Profit before tax **2,250.0** vs 2,034.6 — **+10.6%**.
- Net profit for the year **1,705.9** vs 1,580.3 — **+8.0%**; attributable to shareholders **1,707.4** vs 1,581.6 — **+8.0%**.
- EPS (basic = diluted) **RUB 77.81** vs 72.03 — **+8.0%**.
- Balance sheet: total assets **RUB 68,814.5bn** (vs 60,855.1 — +13.1%); total equity **RUB 8,346.5bn** (vs 7,173.5 — +16.4%); equity attributable to shareholders **8,351.6** vs 7,175.7.
- ROE **≈ 22.0%** `(analysis)` — 1,707.4 / average attributable equity (8,351.6 and 7,175.7); not a figure quoted verbatim in the summary statements. The prior Annual Report 2024 reported FY2024 ROE of 23.3% and net profit RUB 1,509bn (RAS basis in that highlight), so the IFRS ROE level has eased modestly but remains very high.

**By segment / driver.** Earnings are B2B-led: B2B segment profit before tax **RUB 1,698.7bn (+2.8%)** vs B2C **RUB 964.0bn (−1.9%)**. B2C was squeezed by a jump in retail credit-loss charges (**−529.8** vs −368.6, +43.7%) and net insurance expense (−210.1 vs +14.8 income) — i.e., retail provisioning and insurance drag offset solid retail NII (B2C NII +7.5% to 2,252.8). B2B NII +4.2% to 1,638.2 with far lower provisioning (−60.7). Takeaway: profit growth in 2025 came from the corporate book and from NII expansion, not from fees (flat) or retail.

**vs expectations / prior period.** No public consensus in the corpus → stated vs prior year only (exact Street number [UNSOURCED]). YoY momentum is decelerating: FY2024 attributable net profit was RUB 1,581.6bn, so +8.0% in 2025 is a clear slowdown from the double-digit growth Sber had posted into 2024 — consistent with a high-key-rate environment lifting funding costs and credit losses. Prior 9M/Q3 2025 (2025-10-28) and 1H/Q2 2025 (2025-07-29) IFRS prints exist in the IR DB and are the within-year trail into this annual; the Q3 2025 run-rate already implied full-year profit near the RUB 1.7tn level. `[[Sber fully automates bank guarantees for Federal Customs Service]]` is the current note.

**Guidance / forward.** None in the summary financial statements (no quarterly/annual guidance line). Forward direction is set qualitatively by the Sber Investor Day 2025 (2025-12-10) strategy deck rather than numeric guidance here. Dividends: FY2024 dividends of **RUB 786.9bn** were declared at the June 2025 AGM (up from RUB 752.1bn for 2023); the FY2025 payout is not yet declared in this filing. `(hypothesis)` On the 50%-of-IFRS-net-profit policy, FY2025 net profit of RUB 1,705.9bn points to a materially higher absolute dividend, but the exact amount is [UNSOURCED] until the 2026 AGM.

**Thesis-flags.**
1. Margin/funding pressure (fact: NII +18.6% but interest expense +35.3% → why: high Bank-of-Russia key rate repricing deposits faster than assets → why it matters: NIM and net-profit growth decelerated to +8.0% → second-order: further rate moves swing the single largest P&L line). This is the macro backdrop, not something the product story changes.
2. Rising credit cost in retail (fact: net credit-loss charge for debt assets −646.6 vs −442.8, +46.0%; B2C provisions +43.7% → why: retail book seasoning under tight policy → matters: it is the main reason B2C profit fell YoY → second-order: credit quality, not fees, is the swing factor in 2026).
3. Negative operating leverage (fact: opex +16.5% vs operating income +12.6% → why: wage/IT/AI investment → matters: AI-led automation like this guarantees product is precisely the cost lever Sber is pressing to re-invert that ratio → second-order: productivity/automation wins are a credible margin story only if they show up in the cost-to-income trend).
4. Scale/health context for the product (fact: a RUB 68.8tn-asset bank earning RUB 1.7tn net profit → matters: the FCS bank-guarantee automation is a small, process-efficiency improvement inside a large and profitable franchise, de-PR'd as operational optimization of the RUB 61.4bn guarantees/documentary fee book rather than a needle-mover → second-order: directionally supports the opex/CIR self-help thesis, immaterial to group earnings).

De-PR note: the press release frames a record annual profit; the filing shows the net fee line actually dipped (−1.1%), provisions jumped (+46%) and opex outran revenue — the growth was carried by NII and the corporate segment, which management emphasizes less. The guarantees-automation announcement carries no financial figures of its own; its earnings relevance is purely as a cost-efficiency signal.

Sources: Sber FY2025 Summary Consolidated IFRS Financial Statements (12M 2025), filed 2026-02-26 — https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf (latest_result in ir_latest.json; figures read from the statement of profit or loss, financial position, EPS/dividends note and segment analysis) · Sber Annual Report 2024 (FY2024 highlights, ROE 23.3% / net profit RUB 1,509bn RAS) — https://www.banktrack.org/download/annual_report_2024_142/sberbank_ar_esg_2024_eng.pdf · prior within-year trail: 9M/Q3 2025 IFRS (2025-10-28) and 1H/Q2 2025 IFRS (2025-07-29) · Investor Day 2025 strategy (2025-12-10) — https://www.sberbank.com/investorday/en · Public consensus / Street estimates: no data in corpus [UNSOURCED]; semsearch dense retrieval unavailable (OpenRouter 402). ROE ≈22.0% is `(analysis)`, not a verbatim disclosed figure.
<!-- /enrichment:earnings_review -->
