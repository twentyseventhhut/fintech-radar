---
title: "Toss and Gwangju Bank complete stablecoin QR payment PoC"
date: 2026-10-09
retrieved: 2026-10-09
tags:
  - company/toss
  - company/gwangju-bank
  - industry/stablecoins
  - industry/payments
  - region/asia
  - type/partnership
sources:
  - https://en.bloomingbit.io/feed/news/121830
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s1945caa8
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Toss and Gwangju Bank complete stablecoin QR payment PoC

> [!info] 2026-10-09 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇰🇷 Toss and Gwangju Bank complete a proof of concept for stablecoin QR payments. The test verified Gwangju Bank customers paying with stablecoins at offline stores through the linked Toss app with a QR code. Payment and settlement are confirmed at the same moment, with funds going directly to the merchant. The companies are now preparing a second round of verification with actual merchants.

## Первоисточники

### en.bloomingbit.io
<https://en.bloomingbit.io/feed/news/121830>
*299 слов · direct*

Toss, Gwangju Bank Complete Proof of Concept for Stablecoin QR Payments
Summary
Toss and Gwangju Bank said they completed a proof of concept for stablecoin -based QR code payments .
The companies said the payment structure links the Toss app and the Gwangju Bank app , allowing customers to pay with stablecoins at offline stores while settlement is completed at the same time.
The two companies said they plan to prepare a second round of verification involving actual merchants based on the latest results.
Forecast Trend Report by Period
Toss said on October 8 that it had completed a proof of concept for stablecoin-based QR code payments with Gwangju Bank.
The test was designed to verify a payment scenario in which a Gwangju Bank customer uses stablecoins at an offline store through the Toss app. When a user of the Gwangju Bank app selects the stablecoin payment option, the linked Toss app opens automatically and the payment proceeds by scanning a QR code.
Settlement is structured so the payment amount is delivered directly to the merchant. The transfer is processed without an intermediary step, and payment and settlement are confirmed at the same time the transfer is completed. That means no separate settlement procedure is required after the payment is made.
The verification was conducted in an environment separate from commercial services. The companies set up a virtual merchant and implemented the payment flow without using customer information or real assets. The exercise focused on confirming that payment and settlement worked as designed.
Based on the results, the two companies are preparing a second round of verification. They plan to streamline the payment process to reduce the number of steps for customers and discuss the scope of a test involving actual merchants.
Bae Tae-woong, Hankyung.com reporter, btu104@hankyung.com
Uk Jin

## Контекст

<!-- enrichment:context -->
**What happened (2026-10-08).** Toss (operated by Viva Republica) and Gwangju Bank — a regional lender inside JB Financial Group — announced they completed a proof of concept (PoC) for stablecoin-based QR-code payments. In the tested flow, a Gwangju Bank app user selects "stablecoin payment," which auto-opens the linked Toss app; the user scans a QR code shown on a merchant terminal (Toss Place POS), and payment plus settlement are confirmed in the same instant, with funds routed directly to the merchant's wallet — no separate post-payment settlement step. The PoC ran in a sandbox separate from live services: a virtual merchant, no real customer data, no real assets. A second PoC is planned with actual merchants in the Gwangju/Jeonnam region, aiming to cut the number of user steps.

**Why it matters.** This is a payments-architecture test more than a product launch. The headline claim — atomic payment-and-settlement with direct-to-merchant transfer — would, if productionized, collapse the card-network authorize/clear/settle cycle (T+1/T+2) into a single on-chain event, removing acquirers/settlement intermediaries. That is the standard stablecoin pitch; the novelty here is wiring it into an existing Korean superapp (Toss) + its physical merchant terminal footprint (Toss Place), rather than a crypto-native rail.

**Regulatory backdrop (load-bearing caveat).** South Korea still has NO stablecoin legal framework in force. Phase 2 of the Digital Asset Basic Act — which would institutionalize a won-denominated stablecoin — is stalled, delayed ~1 year amid a turf fight between the Bank of Korea (BOK) and the Financial Services Commission (FSC). The government targets passage by end-2026, with issuer licensing possibly Q4 2026–early 2027. BOK has pushed a bank-centered model (banks holding ≥51% of any issuing consortium) citing AML/capital supervision; see [[Bank of Korea urges banks to lead won stablecoin issuance]]. Korea also paused its CBDC/deposit-token work in favor of bank-led stablecoins. So this PoC uses an unspecified "stablecoin" with no legal issuance basis yet — banks are building rails ahead of the rulebook.

**Internal comps / the broader Korean race.**
- [[Danal and BNK Busan Bank validate Korean Won stablecoin]] (Jun 2026): full-lifecycle technical validation on Danal's IEUM infra, cutting payment processing from ~2s to 0.3s — a direct domestic comp for another regional-bank + fintech pairing.
- [[SBI tests stablecoin QR payments for Japan-Korea travel]] (Oct 2026): SBI DigiTrust + NICE + DSRV testing cross-border tourist QR payments at ~1.2M Korean merchants, targeting Dec 2026 — adjacent (inbound/cross-border) vs. Toss/Gwangju's domestic case.
- [[Samsung affiliates buy Dunamu stake amid won stablecoin push]] (May 2026) and [[Hana Financial Group bets on stablecoins, says chair]] signal that incumbents and chaebol are positioning around won-stablecoin infrastructure.
- Large-bank consortium (KB Kookmin, Shinhan, Woori, NongHyup, IBK, Suhyup, SC Korea) is separately forming to issue a 1:1 won-pegged stablecoin; KB has filed tickers like KBKRW. Gwangju Bank (regional, JB Financial) is NOT a top-tier consortium member — this PoC is a smaller player moving early via a fintech partner.

**Who Toss is.** Viva Republica's Toss is a leading Korean fintech superapp (payments, banking via Toss Bank, brokerage). Prior notes: [[Toss plans domestic listing after US IPO]], [[South Korea's Toss FacePay surpasses 5 million users]], [[Toss Bank pursues global remittance PoC with Solana]] — Toss has an active crypto/rails experimentation track and distribution (app + Toss Place terminals) that makes it a natural payments front-end for bank-issued stablecoins.

**Source quality.** Single underlying event, reported by multiple crypto/trade outlets (bloomingbit, crypto.news, parameter.io, digitaltoday, tokenpost, blockonomi) all tracing to the Oct 8 company announcement via Korean press (Hankyung). No independent verification of performance claims; no named stablecoin, blockchain, volume, or launch date.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Which stablecoin was actually used? The announcement names none — was it a won-pegged token, a dollar stablecoin, or a mock token in a sandbox? Without this, "stablecoin payment" is marketing.
2. Which blockchain / ledger ran the PoC? Permissioned vs. public? "Atomic settlement" claims mean nothing without knowing the settlement layer.
3. "Payment and settlement confirmed at the same moment, funds direct to merchant" — in a sandbox with a virtual merchant and no real assets, is this an engineering demo or a claim about production behavior under load, disputes, and refunds?
4. There is NO legal basis to issue a won stablecoin in Korea yet (Digital Asset Basic Act Phase 2 stalled). On what regulatory footing could this ever go live, and when?
5. How is this materially different from the Jun 2026 Danal/BNK Busan PoC, which already claimed full-lifecycle validation at 0.3s? Is Gwangju/Toss behind, not ahead?
6. Gwangju Bank is a small regional lender (JB Financial), not in the big-bank won-stablecoin consortium (KB/Shinhan/Woori/etc.). Is this a minnow trying to leapfrog, and will any eventual standard freeze it out?
7. Who bears FX/peg/reserve risk and redemption guarantees in a real deployment? A PoC with virtual assets dodges the hardest part.
8. What is the merchant economics case? If it merely replicates existing Korean QR rails (Toss already has instant account-to-account payments domestically), what does a stablecoin add for Korean consumers — and does it add cost?
9. AML/KYC and reversibility: direct-to-merchant, irreversible on-chain settlement is a consumer-protection and fraud liability problem. How are chargebacks/disputes handled?
10. No volume, no date, no second-PoC timeline specifics beyond "actual merchants in Gwangju/Jeonnam." Is this a press-cycle milestone timed to the Digital Asset Basic Act debate rather than a commercial signal?
11. BOK wants banks (≥51%) to control issuance; Toss is a fintech, not a bank. Does the Toss front-end / Gwangju-issuer split survive the likely bank-centric legal model?
12. Is "settlement at the same instant" actually true, or is there off-chain pre-funding/escrow that makes it look atomic to the user while a bank balance-sheet step happens behind the scenes?
13. Could this be a defensive move — Toss hedging against the large-bank consortium owning the rail — rather than genuine conviction in stablecoin payments?
14. Cross-border comp: SBI's Japan-Korea tourist PoC (Oct 2026) targets a concrete use case (inbound travelers, 1.2M merchants). Domestic won-for-won stablecoin payments lack an obvious pain point vs. existing instant transfers — what's the real demand?

**Importance: 2/5** — A sandbox PoC by a small regional bank + a fintech front-end, with no named token, no chain, no volume, no launch date, and no legal basis for issuance in Korea yet. It is one data point in a crowded, pre-regulatory Korean won-stablecoin race (Danal/BNK Busan already did a similar validation in June; the big-bank consortium is the real story). Signal value is as a marker of continued bank-led experimentation ahead of the Digital Asset Basic Act, not as a commercial milestone. Toss's distribution (app + Toss Place terminals) is the one genuinely interesting ingredient; otherwise low materiality.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: **KRW (won) stablecoin — merchant QR *acceptance* rail, Korea** (distinct from the *issuance-infra* angle of [[Toss and Optimism explore won-pegged stablecoin for Korea]]). No credible free TAM for a KRW-stablecoin segment — issuance is **not yet legal**, so "no data" on size; context anchor: ~99% of global stablecoin supply is USD-denominated (per BoK governor, via [[Bank of Korea wants gradual, bank-led stablecoin rollout]]), making a won coin a sovereignty-driven greenfield, not a sized market. Structure: **pre-launch, fragmented on issuers / concentrating on distribution** — value accrues to whoever owns the consumer wallet + the licensed bank rail; the chain and the acceptance terminal are commoditizing layers beneath. Barriers are **regulatory + licence**, not tech. **Why now:** the government's **won-stablecoin bill is targeted for submission ~October 2026** with a goal of passage by end-2026 (per Cointelegraph / BitMarkets, Oct 2026); a **bank-centred model** (bank consortium holding **≥50%+1 share**) is the leading structure under discussion, down from BoK's earlier hard 51% line but still bank-anchored (per Bloomingbit/CoinDesk, 2026). So every super-app and bank is planting PoC flags *before* the rules lock issuance economics in. Second-order: a bank-anchored rule pushes fintechs toward acceptance/distribution roles — exactly the layer this Toss×Gwangju PoC occupies.

**Competitive landscape.** Sector KPIs (pre-volume, proxies): merchant-acceptance footprint (POS terminals), distribution reach (MAU / population penetration), settlement latency/finality, and reserve/float economics (accrues to the *issuer*). Mechanics of this PoC (per crypto.news / digitaltoday, 2026-10-08): links **Gwangju Bank app → Toss app → Toss Place terminals**; QR scan, with payment *and* settlement confirmed simultaneously and funds routed directly to the merchant (no separate clearing step). Tested in a ring-fenced environment with a virtual merchant, no real assets/customer data — **a lab PoC, not live**; a second round with *actual* merchants is "being prepared," no date. Key players & basis of competition (distribution + licence eligibility, not tech): [[Danal and BNK Busan Bank validate Korean Won stablecoin]] (acceptance-rail tech, 2s→0.3s); BDACS+Woori (KRW1 on Avalanche, chain-side ahead); Naver–Hana–Dunamu axis and Kakao/KakaoBank consortium (distribution); the 8-bank commercial consortium (licence/reserves). Recent moves: [[SBI tests stablecoin QR payments for Japan-Korea travel]] and [[Samsung brings USDC to Samsung Wallet with Solana and Coinbase]] (both 2026-10) — QR/wallet stablecoin acceptance is now a *crowded Oct-2026 theme*. **Protagonist's position:** Toss is **ahead on distribution** (IR/Q2-2025 release: 30M+ registered users, ~60% of Korea's population; Toss Place offline terminals) and now demonstrating the *acceptance* leg — but it is **catching up / niche on issuance**: it cannot issue a won coin today, and the PoC settles whatever token Gwangju Bank's side supplies. Moat = super-app network effects + 500k-merchant Toss Place base + banking/FX/AML licences (switching costs, scale) `(analysis)`. Notably, the partner is a *regional* bank (Gwangju Bank, JB Financial subsidiary) — smaller than the Naver-Hana / 8-bank camps, so this is a flag-plant with a willing mid-tier bank, not a top-consortium alliance.

**Comps & multiples.** Toss/Viva Republica is **private, pre-IPO** — no market cap, no P/E. **IR-grounded PRIMARY figures** (company's own filings): FY2024 consolidated revenue **~KRW 2.0tn, first full-year net profit** (Toss earnings release, 2025-03-28); Q2-2025 revenue **KRW 668bn, +41% YoY** (release, 2025-08-14); latest reported quarter **Q1-2026 operating revenue KRW 805.3bn, +41.8% YoY, net profit ≈KRW 1bn (near break-even, −98% YoY)** — top-line compounding ~40% while opex (+54.5%) outran revenue, partly a Toss Payments refinancing one-off (Viva Republica 분기보고서, DART rcpNo 20260515002034, filed 2026-05-15). IPO frame (press): targeting a US listing >$10bn (up to ~$15bn) → implied **P/S ≈ $10bn / ~$1.4bn FY2024 rev ≈ 7x** `(analysis)` — rich for a bank-adjacent name but defensible against 40%+ growth (growth-multiple link); Korean IB's KRW-10tn / 2tn-rev = **5x** frame is the cheaper read. Listing timing is fluid — corpus has both [[South Korea's Toss postpones US ADR listing plan]] and [[Toss plans domestic listing after US IPO]]. Counterparty **Gwangju Bank**: regional bank, ~KRW 34.4tn total assets at YE2025; parent **JB Financial Group** FY2025 net income **~$499m** (per web) — but no stablecoin-specific revenue exists, so **EV/Revenue, P/E on the stablecoin line = n/a (pre-revenue)**. Internal comps (all PoC/announce-stage, no live volume): [[Danal and BNK Busan Bank validate Korean Won stablecoin]], [[Naver Pay enters South Korea stablecoin race]], [[KakaoBank prepares Korean won stablecoin amid Upbit deal]], [[KB Kookmin Bank files won-stablecoin trademarks KBKRW and KRWST]]. **Distribution not computed** — no ≥3 comparable revenue/EV figures for the KRW-stablecoin line; qualitative comparison only. Clean EV/EBITDA, NTM multiples, sell-side consensus → **[UNSOURCED]** (none public for a private issuer).

**Risk flags.**
1. **Regulation is the binding gate, and it favours banks.** No won coin can be issued until the Digital Asset Basic Act / Oct-2026 won-stablecoin bill passes; the leading bank-anchored (≥50%+1) model could force Toss into a subordinate role where the **licensed bank keeps the reserve float** and Toss earns only thin acceptance/processing fees — its distribution edge is worth less if it doesn't own issuance economics. (second-order: speed/UX demos ≠ rent.)
2. **Acceptance-rail commoditization / saturation.** QR stablecoin acceptance is suddenly a crowded Oct-2026 theme (Danal/BNK, SBI, Samsung-USDC); the "simultaneous payment+settlement" design is replicable, and bank consortiums / Naver-Upbit / Kakao can build or buy acceptance in-house → likely consolidation around 1–2 issuers, with standalone rails relegated to plumbing.
3. **PoC ≠ product, against a soft IPO clock.** A ring-fenced lab test with a *regional* bank, a virtual merchant and no real assets, no second-round date, no disclosed economics/fraud-liability/reserve mechanism — classic pre-regulation signalling that risks being read as IPO narrative rather than shipped revenue.

**What this changes (idea-lens).** `(analysis)` Not a re-rating event — it extends Toss's multi-track hedge from *issuance infra* (Optimism PoC) to the *acceptance/merchant* leg, buying optionality while the law is written. The real catalyst is the Oct-2026 bill + the issuer-eligibility ruling, which decides whether Korea's won coin is **bank-issued / fintech-distributed** (Toss keeps reach, loses float) or **fintech-issuable** (Toss owns the full stack). Falsifiable thesis: *Toss's durable value here is the Toss Place acceptance network + distribution, not this specific Gwangju tie-up, which is cheap flag-planting.* Trigger that would make it material: the "second round with actual merchants" ships with a named issuer + disclosed revenue-share, or Toss is named a lead/co-issuer under the bill. What breaks it: a bank-majority rule plus incumbents building acceptance in-house, commoditizing Toss out of the economics.

Sources: https://en.bloomingbit.io/feed/news/121830 · https://crypto.news/south-koreas-gwangju-bank-and-toss-successfully-test-stablecoin-qr-payments/ · https://www.digitaltoday.co.kr/en/view/112105/toss-completes-stablecoin-qr-payment-technology-test-with-gwangju-bank · https://cointelegraph.com/news/south-korea-won-stablecoin-bill-october-dollar-dependence · https://bitmarkets.com/en/insights/article/south-korea-to-officially-introduce-stablecoin-framework · https://www.coindesk.com/policy/2026/04/08/south-korea-proposes-cryptocurrency-law-with-bank-style-rules-for-stablecoins · https://www.prnewswire.com/news-releases/toss-reports-records-revenue-of-2-trillion-krw-and-first-full-year-net-profit-in-2024-302414439.html · https://www.prnewswire.com/news-releases/toss-surpasses-krw-668-billion-in-consolidated-revenue-for-q2-2025-achieving-41-year-over-year-growth-302530252.html · Viva Republica Q1-2026 분기보고서 (DART rcpNo 20260515002034) https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002034 · https://www.koreaherald.com/article/10488443 · Note: semsearch (news + irdb) down (OpenRouter 402); IR figures grounded via ir_latest.json metadata + filings/IR URLs + grep fallback over the corpus.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings review — Toss / Viva Republica. The Gwangju-Bank stablecoin-QR item is a PoC product announcement with **no financials** of its own ("no full earnings report in the news"). Per IR coverage, this layer reports Viva Republica's own latest filed results. Viva Republica is **private (pre-IPO)**; its period-complete disclosures are mandatory DART filings. Latest print = **Q1 2026** (filed 2026-05-15; DART rcpNo 20260515002034). Q2 2026 not yet published as of 2026-10-10.

**Verdict (headline read): MIXED — top-line BEAT, bottom-line MISS.** Q1 2026 consolidated revenue **KRW 805.3bn (+41.8% YoY)** — growth held in the 40s, accelerating vs FY2025's +38%. But consolidated **net profit collapsed to KRW 0.98bn (−98% YoY)** and **operating profit fell to KRW 37.2bn (−47.5% YoY)** as opex outran revenue. No formal guidance (private co.). The quarter is a profitability air-pocket, not a growth problem.

**Key figures (Q1 2026 consolidated, vs Q1 2025):**
- Revenue: **KRW 805.3bn, +41.8% YoY** (from KRW 567.9bn).
- Operating profit: **KRW 37.2bn, −47.5% YoY** (from KRW 70.8–70.9bn). Operating margin compressed to ~4.6% from ~12.5%.
- Net profit: **KRW 0.98bn (≈KRW 1bn), −98% YoY** (from KRW 48.8–48.9bn). Still positive — "consecutive profitability" technically maintained.
- Operating expenses: **KRW 768bn, +54.5% YoY** (from KRW 497bn) — expenses grew ~13pp faster than revenue, the whole story of the quarter.

**By driver.** Revenue growth "balanced across advertising, financial brokerage, securities and payments" (super-app monetization). The margin hit is explicitly cost-side: (1) tech-infrastructure + headcount investment, (2) sales-linked costs scaling with revenue, and (3) a **one-off early-repayment / refinancing fee at Toss Payments**. Only the first two are structural; the Toss Payments refi fee is a one-off and should not recur.

**vs expectations / prior period.** No public analyst consensus exists (private, no listed stock) → beat/miss is qualitative vs prior periods [consensus UNSOURCED]:
- vs Q1 2025 (KRW 567.9bn / op KRW 70.9bn / net KRW 48.9bn): revenue clearly up, profit sharply down.
- vs FY2025 full year — **revenue KRW 2.7tn (+38% YoY), operating profit ~KRW 336bn, net profit KRW 201.8bn (+~846% YoY)** (BigGo/Korean press, FY2025). Q1 2026 net of ~KRW 1bn annualizes nowhere near the FY2025 KRW 201.8bn run-rate — a steep QoQ/seasonal profitability step-down, flagged.
- vs FY2024 (revenue KRW 1,956bn +43%, op KRW 91bn, first-ever net profit KRW 21.3bn): trajectory confirms revenue deceleration from +43% (FY24) → +38% (FY25) → re-acceleration to +41.8% (Q1'26), with profit now the swing variable.

**Guidance / forward.** None given (private company; DART filings carry no forward guidance, no IPO date). Mgmt framed the quarter defensively: "the key takeaway is we maintained consecutive profitability while achieving revenue growth in the 40% range" — i.e. leading with growth + bare-positive net, quiet on the magnitude of margin compression. Independent read `(analysis)`: strip the one-off Toss Payments refi fee and the quarter is lower-margin-but-growing; the open question is how much of the +54.5% opex surge (infra/headcount) is IPO-prep front-loading vs permanent cost base.

**Thesis-flags:**
1. **Margin durability (highest).** Op margin ~4.6% (from ~12.5%) with opex +54.5% > revenue +41.8%. Fact → investing ahead of an IPO and scaling sales costs → if the one-off is excluded the drop is smaller, but the trend bears watching → second-order: a thin-profit print weeks before a planned 2026/2027 US listing pressures the valuation narrative that rested on FY2025's KRW 201.8bn net.
2. **One-off vs structural split.** The Toss Payments early-repayment fee is explicitly one-off; de-PR flag — mgmt grouped it with structural investment to soften the headline, so normalized profit is better than the KRW 1bn suggests, but the exact one-off size was not disclosed [UNSOURCED].
3. **Growth re-acceleration intact.** +41.8% revenue (vs FY25 +38%) says the monetization engine (ads/securities/payments/brokerage) is not stalling — the thesis pillar holds; this is a cost quarter, not a demand quarter.
4. **Pre-IPO disclosure gap.** No consensus, no guidance, Korean-only primary filings → figures come from DART-filing-day press (2026-05-15), not a clean English release; verification reliance is on secondary English press.

Sources (primary = Viva Republica's own DART Q1 2026 filing, rcpNo 20260515002034): DART filing https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002034 · Q1 2026 figures (filing-day report) https://www.asiae.co.kr/en/article/finance/2026051517545320591 · Q1 2025 comparatives https://www.koreaherald.com/article/10488443 · FY2024 release (Viva Republica) https://www.prnewswire.com/news-releases/toss-reports-records-revenue-of-2-trillion-krw-and-first-full-year-net-profit-in-2024-302414439.html · Q2 2025 release (Viva Republica) https://www.prnewswire.com/news-releases/toss-surpasses-krw-668-billion-in-consolidated-revenue-for-q2-2025-achieving-41-year-over-year-growth-302530252.html · FY2025 full-year figures https://finance.biggo.com/news/m41mQ50Bh5an-7GhFwpf · irdb semsearch unavailable (OpenRouter 402) — used ir_latest.json + web. Public analyst consensus / forward guidance: none (private, pre-IPO) [UNSOURCED].
<!-- /enrichment:earnings_review -->
