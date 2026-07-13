---
title: "US regulators propose user ID rules for stablecoin issuers"
date: 2026-06-22
tags:
  - industry/stablecoins
  - region/us
  - type/regulation
sources:
  - https://www.connectingthedotsinfin.tech/r/a48362aa
  - https://www.connectingthedotsinpayments.com/r/f4f5447d
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s224d7b46
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# US regulators propose user ID rules for stablecoin issuers

> [!info] 2026-06-22 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 US Regulators propose user ID rules for stablecoin issuers, requiring stablecoin issuers to implement bank-style customer identification programs under the GENIUS Act. The measures would strengthen AML and counter-terrorism controls through identity verification, recordkeeping and customer screening requirements, bringing stablecoin compliance closer to traditional banking standards.

[Connecting the Dots in Payments] 🇺🇸 US Regulators propose user ID rules for stablecoin issuers, requiring stablecoin issuers to implement bank-style customer identification programs under the GENIUS Act. The measures would strengthen AML and counter-terrorism controls through identity verification, recordkeeping and customer screening requirements, bringing stablecoin compliance closer to traditional banking standards.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/a48362aa>
- <https://www.connectingthedotsinpayments.com/r/f4f5447d>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: US regulators propose user ID rules for stablecoin issuers
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **18 June 2026**, FinCEN (Treasury) jointly with the **OCC, Federal Reserve, FDIC and NCUA** issued a Notice of Proposed Rulemaking (NPRM) requiring **Permitted Payment Stablecoin Issuers (PPSIs)** to run a written, risk-based **Customer Identification Program (CIP)** — collect and verify name, address, date of birth and an identification number before opening an "account", keep records, screen against designated government lists, and give customer notice. Published in the **Federal Register on 22 June 2026**; comments due **21 August 2026** (~60 days). This is *not* new primary law — it implements a directive already written into the **GENIUS Act (enacted July 2025)**, which classifies PPSIs as "financial institutions" under the Bank Secrecy Act.

**+ Why structured this way and what it reveals:** The digest framing ("US regulators propose user ID rules… bringing stablecoin compliance closer to banking standards") is accurate but soft. The genuinely hard problem the rule wrestles with — and where the substance is — is **scoping "account" and "customer"**: stablecoins circulate peer-to-peer among holders who never onboard with the issuer. Much of the NPRM is about *when an issuer actually has a CIP-triggering relationship* vs when **secondary-market activity falls outside it**. That is the real fight: a literal "KYC every holder" reading is impossible for a bearer-like token, so the agencies are trying to draw a perimeter at mint/redeem. This is the **second of two rulemakings**, not a standalone event — see [4].

## [1] Competitors / peers (regulatory + issuer landscape)
This sits in a sequence of GENIUS Act implementation rules:
- **April 2026** — FinCEN + OFAC NPRM on the broader **AML/CFT and sanctions-compliance program** for PPSIs (5-pillar program, designated AML officer, sanctions program — comments closed ~9 June 2026). The CIP rule is the narrower follow-on.
- **April 2026** — OCC and FDIC issued their own GENIUS Act NPRMs on requirements/standards for federally- and FDIC-supervised PPSIs.
Issuer peers affected: **Circle (USDC), Tether (USAT — its US arm under Bo Hines)** [[Tether unveils USAT US stablecoin, names Bo Hines CEO]], **Paxos, PayPal (PYUSD)**, Ripple. Industry self-help already pointed this way: **Circle and Paxos piloted "Know Your Issuer"** in Sept 2025 [[Circle and Paxos pilot Know Your Issuer for stablecoins]] — note that KYI authenticates *issuers/coins*, whereas this rule is about *KYC of customers*, so it is complementary, not duplicative.

**+ Why the landscape is this way / second-order:** The GENIUS Act deliberately removed stablecoins from SEC/CFTC jurisdiction and routed oversight through banking + Treasury/BSA channels [[This Week in Fintech: Hong Kong Stablecoins Ordinance overview]]. So compliance convergence with banks is structural, not optional. The competitive implication: bank-grade CIP raises the **fixed compliance floor**, which advantages large/funded issuers (Circle, PayPal, Tether-US) over sub-scale entrants — consistent with the IMF's read that GENIUS compresses the value of payment firms [[IMF GENIUS Act cut payment firms' value by $300 billion]].

## [2] Company / regulator fit
For Treasury/FinCEN this is the logical execution of a mandate Congress already handed them; the agencies have no discretion on *whether* to impose CIP, only *how* to scope it. For issuers, USDC and PYUSD already operate KYC at fiat on/off-ramps, so the marginal burden lands less on the household-name issuers and more on (a) clarifying the *holder-vs-customer* perimeter and (b) firms that relied on permissionless distribution.

**+ Why this logic:** GENIUS gave issuers something they wanted (a federal "yes, you may exist" framework + SEC/CFTC exemption) in exchange for accepting bank-style obligations — the AML/CIP rules are the *price* of that legitimacy. The White House framed GENIUS as boosting Treasury's power to seize/freeze/burn illicit coins [[FT analyzes GENIUS Act's implications for US dollar regulation]]; CIP is the front-end that makes attribution possible.

## [3] Novelty / value-add / traction
Genuinely new: the **federal mandate that a stablecoin issuer must run a bank-style CIP** is a first, and (per the April companion rule) the first time US law explicitly mandates a sanctions-compliance program for a specific class of private issuer. But "traction" here = a *proposed* rule in a 60-day comment window — **announced, not in force**. No final rule, no effective date, no enforcement yet. The on-chain reality (privacy in commerce, identity surfacing only at KYC endpoints) already approximates this at off-ramps [[Noah essay: money evolves toward programmable dollars]]; the rule formalizes and federalizes it.

**+ Why the value-add is real or not:** The durable value is **legal certainty** — a defined perimeter lets compliant issuers scale into regulated US distribution. The risk that breaks it: if the final "account/customer" definition is drawn too broadly, it could push privacy-sensitive or non-US issuers (Tether's offshore USDT) further outside the US perimeter rather than into it — a disintermediation, not capture, outcome.

## [4] What's next / market sentiment
Comment period runs to **21 Aug 2026**; expect heavy industry comment on the account/customer scoping and on reliance provisions (limited reliance on other federally-regulated FIs is permitted). A final rule likely later in 2026/2027, then a compliance runway. Regulatory backdrop is reinforcing: Senate's four-year **Fed CBDC ban** [[US Senate passes housing bill with four-year Fed CBDC ban]] signals the US is betting on *private* regulated stablecoins over a CBDC — making this rulemaking the load-bearing AML layer of that bet.

**+ Counterintuitive second-order:** Tighter US KYC could *strengthen* USDC/PYUSD onshore while pushing USDT's offshore liquidity to remain offshore — bifurcating the dollar-stablecoin market into a "regulated onshore" and "grey offshore" tier rather than unifying it.

## Sources
- FinCEN news release: https://www.fincen.gov/news/news-releases/fincen-agencies-propose-rule-implement-genius-act-customer-identification
- Federal Register (CIP NPRM, 2026-06-22): https://www.federalregister.gov/documents/2026/06/22/2026-12460/permitted-payment-stablecoin-issuer-customer-identification-program
- FinCEN CIP NPRM fact sheet: https://www.fincen.gov/system/files/2026-06/GENIUS-CIP-NPRM-FactSheet.pdf
- Sullivan & Cromwell memo: https://www.sullcrom.com/insights/memo/2026/June/Agencies-Propose-Customer-Identification-Program-Requirements-Stablecoin-Issuers
- NCUA release: https://ncua.gov/newsroom/press-release/2026/agencies-request-comment-customer-identification-program-requirements-permitted-payment-stablecoin
- April AML/CFT+sanctions NPRM (Federal Register): https://www.federalregister.gov/documents/2026/04/10/2026-06963/permitted-payment-stablecoin-issuer-anti-money-launderingcountering-the-financing-of-terrorism
- Covington (April NPRM analysis): https://www.cov.com/en/news-and-insights/insights/2026/04/fincen-and-ofac-propose-aml-cft-and-sanctions-framework-for-permitted-payment-stablecoin-issuers-five-things-to-know
- Original digest links: https://www.connectingthedotsinfin.tech/r/a48362aa , https://www.connectingthedotsinpayments.com/r/f4f5447d
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team questions

1. **Proposed vs in force?** This is an NPRM (issued 18 Jun 2026, FR 22 Jun 2026), comments due 21 Aug 2026. There is no final rule, effective date, or enforcement. Treating it as "new rules now in effect" would overstate it. → confirmed: *proposed only*.
2. **Is it actually new law?** No. The CIP mandate is written into the GENIUS Act (July 2025); agencies are implementing a pre-existing directive, not creating new authority. → confirmed.
3. **Which regulators, exactly?** FinCEN (Treasury) jointly with OCC, Federal Reserve, FDIC, NCUA. Some press said "Fed proposes" — misleading; it is a multi-agency joint NPRM led by FinCEN. → confirmed.
4. **Is this the only GENIUS stablecoin AML rule?** No — it is the *narrower CIP follow-on* to the broader April 2026 FinCEN+OFAC AML/CFT + sanctions-program NPRM. Conflating the two would double-count. → confirmed.
5. **The real hard problem — who is a "customer"?** Stablecoins circulate to holders who never onboard with the issuer. The genuine substance is the account/customer scoping and the secondary-market carve-out, not "KYC everyone." → confirmed as central.
6. **Which issuers are named?** The rule applies to all PPSIs; FinCEN docs do NOT name Circle/Tether/Paxos/PayPal specifically. Naming them as "targeted" is analyst inference, not in the primary source. → mark as inference.
7. **Marginal burden — how big?** USDC and PYUSD already KYC at fiat ramps, so incremental cost is moderate for incumbents; heavier for permissionless/offshore models. Open: no cost estimates extracted from the NPRM.
8. **Does this duplicate "Know Your Issuer"?** No. KYI (Circle/Paxos, Sept 2025) authenticates coins/issuers; this rule is customer KYC. Complementary, distinct layers. → confirmed.
9. **Comment-period date precision?** Two figures appear: "~60 days from 18 Jun" and explicit "21 Aug 2026" / "comments due Aug 21 2026". Use 21 Aug 2026 (FR-published). One source said "Aug 21"; reconcilable. → confirmed.
10. **SEC/CFTC angle?** GENIUS removed stablecoins from SEC/CFTC jurisdiction; oversight runs through banking + BSA. Any claim of SEC involvement here would be wrong. → confirmed absent.
11. **Reliance provisions?** Rule permits limited reliance on other federally-regulated FIs — material for distribution partners; easy to omit. → flagged.
12. **Second-order risk — onshoring or offshoring?** Could bifurcate market: onshore-regulated (USDC/PYUSD) vs offshore-grey (USDT). This is hypothesis, not stated by regulators. → mark (hypothesis).
13. **Does the CBDC ban change the read?** The four-year Fed CBDC ban makes private regulated stablecoins the US policy vehicle, raising this rule's importance as the AML backbone — but that linkage is analytical. → mark (analysis).
14. **Any traction/adoption to cite?** None — purely a proposed rule; no live compliance, no enforcement actions. Do not present as adoption.
15. **Source quality?** Primary sources are strong (FinCEN, Federal Register, NCUA, FDIC) plus top-tier law-firm memos (S&C, Covington, Mayer Brown). High confidence on facts; low on speculative market effects.

**Importance: 3/5 — rationale:** A genuine regulatory first (federal bank-style CIP mandate on stablecoin issuers) with real structural consequence — it sets the AML perimeter for the US private-stablecoin bet and the account/customer scoping is substantive. BUT it is a *proposed* rule in a comment window, not in force, with no adoption/enforcement yet, and it implements a mandate already known since GENIUS (July 2025). Incremental, expected, and not a surprise to the market → solidly mid: above commodity regulation noise, below a market-moving final rule or enforcement action.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-28]] (2026-06-28).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** US payment-stablecoins, the AML/compliance layer of a ~$321–322bn dollar-stablecoin market (per DefiLlama / multiple trackers, via bitcoinfoundation.org & kucoin.com, May 2026). Structure is highly concentrated: top-5 issuers controlled ~89% of supply in Q1 2026; Tether/USDT ~$188–190bn (~59% share) and Circle/USDC ~$79bn are the two load-bearing names (per market trackers, May–Jun 2026). The "why now": this NPRM is one rung in a fast GENIUS Act (enacted Jul 2025) implementation ladder — FinCEN/OFAC AML/CFT + sanctions NPRM (Apr 2026), OCC/FDIC supervisory NPRMs (Apr 2026), now the FinCEN-led joint CIP NPRM (issued 18 Jun, Federal Register 22 Jun 2026, comments due 21 Aug 2026). The structural driver is regulatory: GENIUS routed stablecoin oversight through banking + Treasury/BSA channels (not SEC/CFTC), so convergence with bank-grade KYC/CIP is mandated, not optional (analysis). Entry barrier here is regulation itself — a rising fixed compliance floor.

**Competitive landscape.** Sector KPIs: circulating supply / market cap, share of supply, reserve composition + reserve yield (the dominant revenue line for issuers). Players: incumbents Tether (USDT; USAT US arm under Bo Hines) and Circle (USDC); challengers Paxos, PayPal (PYUSD), Ripple (RLUSD). Basis of competition: distribution + regulatory legitimacy + reserve scale, not price. Recent moves: Circle & Paxos piloted "Know Your Issuer" (Sept 2025) — note KYI authenticates *coins/issuers*, whereas this rule is customer KYC, so complementary not duplicative [[Circle and Paxos pilot Know Your Issuer for stablecoins]]; FDIC proposed its first GENIUS rules Dec 2025 [[FDIC proposes first stablecoin rules under GENIUS Act]]. Per the NPRM (via FinCEN/Sullivan & Cromwell), CIP triggers on a *direct* PPSI relationship (issue, redeem, convert, repurchase, burn, reissue, custody); *mere ownership* and *secondary-market activity that touches the PPSI only via smart contract* do NOT create a CIP-triggering account — the perimeter is drawn at mint/redeem, not at every holder. Protagonist (the rule itself, as policy): the agencies have no discretion on *whether* to impose CIP, only *how* to scope "account/customer". Marginal burden falls lighter on incumbents that already KYC at fiat ramps (USDC, PYUSD), heavier on permissionless/offshore models (USDT) (analysis).

**Comps & multiples.** Only one US issuer is public, so this is a qualitative comparison, not a peer distribution.
- **Circle (CRCL):** market cap ~$17.1bn (25 Jun 2026; ranged $18–22bn earlier in Jun), TTM revenue ~$2.86bn → **P/S = $17.1bn / $2.86bn ≈ 6.0x** (per stockanalysis.com / Yahoo Finance / macrotrends, Jun 2026). Q1 2026 revenue $694m, +20% YoY. In-line-to-rich on a ~20% grower; revenue multiple sits inside the normal range, not an outlier.
- **Tether (USDT):** private, no public market cap or audited revenue → **multiples = no data** [UNSOURCED]. Largest issuer by supply (~$188bn) but reserve-income economics undisclosed.
- **PayPal (PYUSD):** PYUSD is a sub-scale line inside PYPL; no standalone stablecoin multiple → no data.
Internal comps (regulatory/economic precedent, not valuation): [[FDIC proposes first stablecoin rules under GENIUS Act]], [[FT analyzes GENIUS Act's implications for US dollar regulation]], [[IMF GENIUS Act cut payment firms' value by $300 billion]], [[SEC eases broker-dealer capital rules for stablecoin holdings]]. The IMF read — GENIUS compressing payment-firm value by ~$300bn — is the relevant valuation signal: the framework cuts disintermediation rent even as it confers legitimacy. EV/EBITDA, P/E for the cohort: not computed (one public name, Tether private).

**Risk flags.**
1. **Account/customer scoping risk.** If the final rule draws the CIP perimeter too broadly (beyond mint/redeem into holder-level), it becomes unworkable for a bearer-like token and pushes privacy-sensitive or non-US issuers (offshore USDT) *further outside* the US perimeter — disintermediation, not capture (hypothesis). The whole substance of the NPRM rides on this definition.
2. **Proposed, not in force.** NPRM only; comments due 21 Aug 2026, no final rule, effective date or enforcement. Treating it as live compliance overstates it; final rule + runway likely 2026/2027 — execution/timing risk on the entire AML backbone.
3. **Compliance-floor concentration.** Bank-grade CIP raises the fixed cost of issuance, advantaging large/funded incumbents (Circle, PYUSD, Tether-US) over sub-scale entrants — reinforcing the already ~89% top-5 concentration and the structural margin compression the IMF flagged.

**What this changes (idea-lens).** This is the load-bearing AML layer of the US bet on *private regulated* stablecoins over a CBDC (reinforced by the four-year Fed CBDC ban) [[US Senate passes housing bill with four-year Fed CBDC ban]] — not a re-rating event, but a consolidation/entrenchment trigger (analysis). Falsifiable thesis: tighter onshore KYC bifurcates the dollar-stablecoin market into a regulated-onshore tier (USDC/PYUSD) and a grey-offshore tier (USDT) rather than unifying it. Trigger to watch: the *final* "account/customer" definition and reliance provisions in the post-comment rule; thesis breaks if Tether's USAT onshores cleanly under the same CIP regime without share loss.

Sources: https://www.federalregister.gov/documents/2026/06/22/2026-12460/permitted-payment-stablecoin-issuer-customer-identification-program · https://www.fincen.gov/news/news-releases/fincen-agencies-propose-rule-implement-genius-act-customer-identification · https://www.sullcrom.com/insights/memo/2026/June/Agencies-Propose-Customer-Identification-Program-Requirements-Stablecoin-Issuers · https://defillama.com/stablecoins · https://bitcoinfoundation.org/news/stablecoin-news/stablecoin-market-cap-tops-321b/ · https://stockanalysis.com/stocks/crcl/ · https://finance.yahoo.com/quote/CRCL/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
