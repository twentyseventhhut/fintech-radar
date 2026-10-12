---
title: "Pakistan FIA uncovers $433M gambling flows via JazzCash, Easypaisa"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/jazzcash
  - company/easypaisa
  - industry/fraud-risk
  - industry/payments
  - region/asia
  - type/regulation
sources:
  - https://www.techjuice.pk/fia-discovers-gambling-transactions-worth-nearly-rs-120-billion-using-jazzcash
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sdbb6ca3a
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Pakistan FIA uncovers $433M gambling flows via JazzCash, Easypaisa

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Federal Investigation Agency (FIA) in Pakistan discovered $433M in gambling transactions routed through payment gateways JazzCash and Easypaisa, forcing JazzCash to shut 100+ merchant accounts.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.techjuice.pk/fia-discovers-gambling-transactions-worth-nearly-rs-120-billion-using-jazzcash>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Pakistan FIA uncovers $433M gambling flows via JazzCash, Easypaisa
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS VERDICT: FRESH.** This is a genuinely new law-enforcement event, not a reprint. The FIR was registered 24 Sep 2026; the story broke in press 8-11 Oct 2026; JazzCash account closures and Easypaisa settlement delays are live operational consequences dated Oct 5-11 2026. No prior corpus note covers this investigation. Related Pakistan AML/fraud notes exist (JeM digital fundraising, 2025) but describe a different case. Not a duplicate.

## [0] What exactly happened (de-PR'd)
The digest line ("FIA discovered $433M in gambling transactions routed through JazzCash and Easypaisa, forcing JazzCash to shut 100+ merchant accounts") is directionally right but compresses and mislabels several things. De-PR'd:
- **The number is a turnover, not "gambling losses" or "laundered profit."** FIA traced Rs119.93bn (~$433.5M at the quoted rate) in combined CREDIT turnover across 11 Single-Member Companies (SMCs), with Rs118.80bn debited out — i.e. money moving THROUGH shell corporates, not Rs120bn of net illicit gain. The headline dollarizes a gross flow figure; the actual gambling-attributable slice is smaller (one documented sub-set: Rs8.586bn across ~10.49M transactions through 5 branchless collection accounts).
- **The wallets are the rails, not the perpetrators (per FIA framing so far).** SMCs fronting as e-commerce / construction / digital-marketing firms collected bettor funds, then layered them through bank transfers and suspected hawala/hundi and crypto channels before reaching 6 overseas betting platforms (U7777, TD777, Game89/89F, EPIWIN, B9, S9). The FIR (8 suspects, registered 24 Sep 2026 under the Foreign Exchange Regulation Act + Pakistan Penal Code) names Muhammad Zeeshan as prime suspect; associate Waqar Rashid Khan allegedly contacted Easypaisa officials directly to arrange payment infrastructure; Muhammad Hamza Sarwar allegedly built fake websites to test/pass Easypaisa payment-integration compliance checks. Two arrests reported.
- **Why this framing matters:** the allegation is INSIDER FACILITATION, not merely wallets being abused by anonymous fraudsters. "Officials contacted directly" + "compliance checks circumvented via test sites" moves this from a KYC-screening failure to a potential insider-collusion / onboarding-integrity failure — a materially worse category for a regulated payment institution (Easypaisa is a licensed digital bank).
- **Operational fallout is the real, confirmed harm so far:** JazzCash shut 100+ (later reported 300+) aggregator accounts following FIA notices + internal review; Easypaisa-linked settlements were delayed across six payment intermediaries (Simpaisa, ajarPay, RapidPay, Zero Technologies, Finza Tech, and global processor dLocal) from ~5 Oct 2026. Core wallet/P2P services stayed up — this is an aggregator/merchant-rail disruption, not a national outage.

## [1] Competitors / peers
- **Direct domestic peers:** JazzCash (Jazz/VEON) and Easypaisa (Telenor Microfinance Bank / Easypaisa Digital Bank) are the two dominant mobile-money rails — together ~70% of branchless-banking agents. Both are implicated as rails here, so this is a sector-wide integrity event, not one firm's scandal. Challengers SadaPay, NayaPay sit outside the named flows (smaller aggregator footprints).
- **Prior art / analogues:** Pakistan's AML enforcement over digital rails is escalating — cf. [[Times Now investigation into Jaish-e-Mohammed digital fundraising]] (Aug 2025, terror financing over fintech) and the broader crypto-regulation push ([[JazzCash signs exploratory crypto MoU with Binance in UAE]], Dec 2025). Globally, mobile-money aggregator abuse for gambling/laundering mirrors M-Pesa (Kenya) and GCash (Philippines) episodes — wallets as laundering conduits is a recurring EMI pattern, not Pakistan-specific.
- **Position:** both wallets are "catching up" on aggregator-layer controls. The incident exposes that merchant-aggregator onboarding (reseller-of-resellers) is the weak link vs. direct-merchant KYC. (analysis)

## [2] Company history / fit
- JazzCash (2012; VEON/Jazz) is market leader — ~21M MAU, >Rs10.7tn processed in the year to Mar 2025. Easypaisa (Telenor) got Pakistan's first digital-bank licence (Jan 2025), posted Rs5.65bn profit ([[Easypaisa Digital Bank posts Rs 5.65 billion profit, up 45.6%]]) and processed ~Rs9.5tn / 2.7bn txns in 2024 (~9% of GDP). Both have been in expansion/partnership mode: [[Visa and easypaisa partner to scale card payments in Pakistan]] (Jan 2026); Easypaisa's strong growth is exactly why Telenor is monetizing it — [[Telenor explores sale of 55% stake in Pakistan's Easypaisa Bank]] (Jun 2026).
- **Why it fits / why it bites:** these are the rails for Pakistan's state-pushed cashless agenda (PM target: 2M digital merchants, 120M banking users, 15bn txns/yr). Aggressive merchant-acquisition growth and aggregator (reseller) networks are precisely what let fronted SMCs slip in. Structural pressure (land-grab for merchants) → relaxed aggregator onboarding → integrity gap. The timing is awkward for Easypaisa: an insider-collusion allegation lands mid-stake-sale process, directly affecting valuation/diligence. (analysis)

## [3] Novelty / value-add / traction
- **What's genuinely new:** scale + the insider angle. Rs119.93bn traced and a formal FIR with named PSP-insider collusion is a step-change from prior one-off wallet-fraud notices. The confirmed "traction" here is enforcement traction (arrests, account closures, cross-firm settlement freezes), not a product.
- **Who captures the harm in the stack:** the aggregator layer. Wallets earn fees on merchant throughput, so shutting 100-300+ aggregator accounts is self-inflicted revenue loss now to avoid regulatory/licence risk later — a classic compliance-vs-growth trade. For Easypaisa the second-order risk is reputational/licence (digital-bank licence <1yr old) and deal risk (Telenor exit). (analysis)

## [4] What's next / market sentiment
- **Near term:** more arrests/FIRs likely; FIA explicitly "intensifying" the crackdown across wallets, banks and crypto channels. Expect tighter SBP scrutiny of aggregator/reseller onboarding and possibly new branchless-banking merchant KYC rules. Easypaisa must publicly ring-fence the insider allegation from core operations to protect its stake-sale.
- **Counterintuitive second-order:** the cashless-economy push (more merchants, faster onboarding) is in direct tension with AML integrity — the faster Pakistan digitizes merchant payments, the larger the aggregator attack surface. Enforcement wins (freezing settlements) also hit legitimate merchants on those six intermediaries, so over-tightening risks pushing flows back to cash/informal hawala — the opposite of policy intent. (hypothesis)
- **Risk flags / who's silent:** neither wallet has disclosed the fee/revenue hit from closures; liability allocation (wallet vs aggregator vs SMC) is unstated; whether Easypaisa's named "officials" were employees or contractors is unconfirmed; the $433.5M FX conversion of a gross turnover figure risks headline inflation.

## Sources
See /tmp/chl_fia.md question block for issues; URLs:
- https://en.dailypakistan.com.pk/11-Oct-2026/fia-probes-rs120-billion-betting-network-linked-to-easypaisa-jazzcash-accounts
- https://www.techjuice.pk/fia-discovers-gambling-transactions-worth-nearly-rs-120-billion-using-jazzcash/
- https://www.techjuice.pk/jazzcash-closes-aggregator-accounts-fia-crackdown/
- https://pakobserver.net/fia-uncovers-rs119bn-online-gambling-network-allegedly-involving-easypaisa-insider/
- https://dailyausaf.com/en/pakistan/fia-probes-rs119-93-billion-online-gambling-network-eight-suspects-named-in-fir/
- https://www.phoneworld.com.pk/easypaisa-insiders-allegedly-linked-to-rs119-93-billion-digital-gambling-network/
- https://www.techjuice.pk/easypaisa-linked-transactions-face-delays-across-six-payment-firms/
- https://propakistani.pk/2026/10/08/fia-intensifies-crackdown-on-online-gambling-and-digital-payments/
- https://www.dawn.com/news/1931181 (market context)

Internal: [[Times Now investigation into Jaish-e-Mohammed digital fundraising]], [[JazzCash signs exploratory crypto MoU with Binance in UAE]], [[Visa and easypaisa partner to scale card payments in Pakistan]], [[Telenor explores sale of 55% stake in Pakistan's Easypaisa Bank]], [[Easypaisa Digital Bank posts Rs 5.65 billion profit, up 45.6%]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team questions

1. **Is Rs119.93bn ($433.5M) illicit gambling money, or gross corporate turnover?** — It is combined CREDIT turnover across 11 SMCs (Rs118.80bn debited out). The gambling-attributable, documented sub-set is Rs8.586bn / ~10.49M txns through 5 branchless accounts. The headline dollarizes a GROSS flow; the "$433M gambling" framing overstates. (answered — figure is turnover, not net illicit gain)

2. **Were the wallets perpetrators or rails?** — Per FIA framing, rails abused by fronted SMCs — BUT with alleged insider facilitation at Easypaisa (officials contacted directly; compliance test-sites). This straddles "abused rail" and "insider failure." (answered — mixed; insider allegation is the sharpest point)

3. **Employees or contractors? How senior?** — "Easypaisa officials" is unspecified; not confirmed whether staff, agents, or aggregator intermediaries. Materially changes corporate liability. (open)

4. **What is the actual revenue hit to JazzCash/Easypaisa from closing 100-300+ aggregator accounts?** — Reported as "significant" / could dent next-year earnings; no quantified figure disclosed. (open)

5. **Does this threaten Easypaisa's digital-bank licence (granted Jan 2025)?** — No regulator action on the licence reported yet; risk exists given insider allegation <1yr into licence. (open)

6. **Does it derail Telenor's 55% Easypaisa stake sale?** — Plausible diligence/valuation drag; no confirmation buyers have reacted. (open — second-order, high-impact)

7. **Is JazzCash's closure count 100+ or 300+?** — Sources diverge (100+ FIA-directed; up to 300+ including internal-review suspensions). Reconcile before publishing a hard number. (answered — use "100+ (some reports 300+)")

8. **Are the six delayed payment firms (Simpaisa, ajarPay, RapidPay, Zero Technologies, Finza Tech, dLocal) implicated, or collateral?** — Reported as settlement delays / collateral disruption from Oct 5, not as accused parties. (answered — collateral, so far)

9. **Is this a one-off case or a pattern?** — FIA says it is "intensifying" a broader crackdown across wallets, banks and crypto. Likely more FIRs. (answered — pattern)

10. **Prior art — has FIA done this to fintech rails before?** — Yes, adjacent AML/terror-finance scrutiny (cf. JeM digital-fundraising, 2025). This is the largest gambling-specific wallet case to date. (answered)

11. **How did SMCs pass KYC/onboarding?** — Fake business profiles (e-commerce/construction/marketing) + alleged compliance circumvention via test websites. Points to aggregator/reseller onboarding weakness, not direct-merchant KYC. (answered — aggregator layer)

12. **Is the $433M FX conversion stable?** — Rs119.93bn at ~Rs277/USD ≈ $433M; converting a gross turnover to USD inflates headline perception. Flag. (answered — methodological caveat)

13. **Crypto channel — how much flowed via crypto vs hawala vs banks?** — "Suspected" crypto/hawala layering mentioned; no breakdown. (open)

14. **What's the read-through for Pakistan's cashless-economy push?** — Direct tension: faster merchant onboarding enlarges aggregator attack surface; over-tightening pushes flows back to cash/hawala. (answered — structural trade-off)

15. **Could this reprice sector M&A / investor appetite for Pakistani wallets?** — Plausible near-term caution on diligence of aggregator networks; no confirmed deal impact yet. (open — hypothesis)

Importance: 3/5 — Large, confirmed, dated law-enforcement event hitting both dominant Pakistani wallets simultaneously, with a credible insider-collusion angle and real operational fallout (account closures, cross-firm settlement freezes) — more than a routine fraud blurb. Capped below 4 because: (a) the headline $433M is a gross-turnover figure, not net illicit value; (b) allegations are unproven (FIR stage, 2 arrests); (c) impact is regional (Pakistan) with limited global rail/market read-through; (d) no disclosed financial quantification of damage to either operator yet.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Pakistan mobile-money is a scale, low-margin branchless-banking market: JazzCash hit ~60M registered / 29.2M active users and processed ~PKR 16.8tn (~$59.7bn) GTV for the 12 months to Mar-2026, +56% YoY (per Dealroom, as of Mar-2026); Easypaisa crossed ~59M registered / ~20M monthly-active by Dec-2025 (per web search, as of Dec-2025). These two dominate a market where card penetration is below 5%, so wallets are the de-facto rails. Context: 96M digital-banking users, SBP targeting 120M by Jun-2026 (see [[Pakistan reports 96 million digital banking users]]). "Why now": the SBP's biometric-verification mandate under BPRD Circular No.1 of 2026 forces all banks/EMIs/branchless providers onto biometric KYC as the primary ID, with unverified accounts facing debit blocks from 25-Oct-2026 (per web search) — this FIA case lands days before that deadline and reads as the enforcement backdrop to it.

**Competitive landscape.** Sector KPIs: active users, GTV/TPV, and — critically here — aggregator/merchant-account integrity (the fraud-liability surface). Both protagonists are telco-owned wallets: JazzCash sits under VEON's Jazz (Mobilink); Easypaisa under Telenor Microfinance Bank, which Telenor is exploring to exit (see [[Telenor explores sale of 55% stake in Pakistan's Easypaisa Bank]]). The duopoly competes on distribution (telco SIM base) and merchant acceptance, not price. Recent moves: Easypaisa Digital Bank PBT PKR 5.65bn (~$20M), +45.6% YoY for 9M-2025 (see [[Easypaisa Digital Bank posts Rs 5.65 billion profit, up 45.6%]]); Visa–Easypaisa card tie-up (Jan-2026); JazzCash–Binance crypto MoU (Dec-2025). Protagonists' position: both are category leaders (ahead), moat = telco-distribution network effects + branchless agent scale. Here the moat is also the liability: the FIA found ~PKR 119.93bn (~$433M) of gambling/hawala flows routed through 11 single-member shell companies and ~5 collection accounts (~10.5M transactions), forcing JazzCash to shut 100+ (reportedly 300+) aggregator accounts and delaying Easypaisa merchant settlements; an Easypaisa insider was allegedly approached directly (per TechJuice / Pakistan Observer, 11-Oct-2026).

**Comps & multiples.** Internal comps: [[Easypaisa Digital Bank posts Rs 5.65 billion profit, up 45.6%]] (PBT ~$20M, 9M-2025), [[Telenor explores sale of 55% stake in Pakistan's Easypaisa Bank]] (pending M&A — no disclosed price), [[Pakistan reports 96 million digital banking users]], [[Pakistan fintech raises $391M in venture capital, Forbes says]] (sector funding context). Trading multiples: not computable — JazzCash (VEON-owned) and Easypaisa Bank (Telenor, unlisted) do not disclose standalone revenue/EV; the only valuation reference is the in-progress Telenor 55% stake sale with no public price. **No data / [UNSOURCED]** on EV/Revenue, price-per-user and any clean multiple; distribution not computed — qualitative comparison only.

**Risk flags.**
1. **Regulatory/liability concentration on aggregator accounts** — the fraud rode the merchant-aggregator layer, not retail KYC; forced account closures and settlement delays hit legitimate merchant TPV and acceptance, the wallets' growth engine. Second-order: SBP can tighten merchant onboarding/aggregator rules sector-wide, raising compliance cost for every EMI.
2. **Insider/governance exposure** — an Easypaisa official was allegedly approached to arrange the flows; if substantiated this is an internal-controls failure, not just external fraud, and is the costliest kind of AML finding for a regulated bank (fit-and-proper, licence risk).
3. **Deal-timing risk for Easypaisa** — an active, named AML/hawala case during Telenor's exploration of a 55% stake sale is a direct overhang on diligence, price and timeline; a live FIR is exactly what a buyer re-prices.

**What this changes (idea-lens).** (analysis) This is a sector-wide trust/compliance re-rating, not a two-company event: in a sub-5%-card market, wallet rails ARE the payment system, so AML failures here are systemic. Falsifiable thesis — the FIA case + the 25-Oct-2026 biometric mandate mark a shift from growth-at-all-costs onboarding to compliance-gated growth, slowing merchant/aggregator account additions across EMIs over the next 2–3 quarters. Trigger/watch: SBP penalty or new merchant-aggregator circular, and whether Telenor's Easypaisa stake sale re-prices or stalls. Thesis breaks if the case stays contained to a handful of shell companies with no SBP rule change and wallet GTV growth holds.

Sources: https://www.techjuice.pk/fia-uncovers-online-gambling-transactions-worth-rs-120-billion-using-jazzcash/ · https://pakobserver.net/over-100-jazzcash-accounts-shut-down-as-fia-targets-gambling-digital-hundi-hawala-network/ · https://focusgn.com/asia-pacific/pakistan-probes-eight-suspects-over-us433m-online-gambling-funds · https://app.dealroom.co/news/feed/jazzcash-hits-60m-users-processes-59-7b-in-transactions-as-pakistan-goes-cashless · https://ccit.pk/mobile-wallets-and-digital-bank-accounts-without-biometric-verification/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
