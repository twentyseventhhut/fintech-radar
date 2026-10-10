---
title: "Revolut to cover costs for 680 customers hit by data hack"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - company/revolut
  - industry/neobank
  - industry/fraud-risk
  - region/europe
  - type/outage-security
sources:
  - https://www.rte.ie/news/business/2026/1007/1594438-revolut-will-cover-costs-for-customers-hit-by-data-hack
  - https://www.bfmtv.com/economie/replay-emissions/le-grand-entretien/video-beatrice-cossa-dumurgier-revolut-revolut-a-obtenu-une-licence-bancaire-en-france-07-10_VN-202610070203.html
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
story_id: s1f3ec70a
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Revolut to cover costs for 680 customers hit by data hack

> [!info] 2026-10-08 · 2 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Revolut will cover costs for customers hit by a data hack, its Western Europe CEO says. The company sent data on 680 clients to hackers who controlled an Italian government agency email address. Revolut will pay for any identity document changes affected customers need and says it will not pay ransoms.

[Connecting the Dots in Fintech] 🇫🇷 Revolut says government agencies were the weak link in a data incident affecting 680 customers. Western Europe CEO Béatrice Cossa-Dumurgier said Revolut itself was not hacked; attackers compromised an Italian government agency’s domain and used it to request customer files. She said 680 customers were affected, including 55 in France, while no funds, access codes or biometric data were compromised.

## Первоисточники

### rte.ie
<https://www.rte.ie/news/business/2026/1007/1594438-revolut-will-cover-costs-for-customers-hit-by-data-hack>
*289 слов · direct*

Revolut will cover the cost of customers wanting to change their identity documents after the fintech was tricked into giving hackers the data of hundreds of customers, the company's CEO for Western Europe said today.
Revolut, Europe's most valuable startup, said it had sent the customers' personal data to hackers who had taken control of an Italian government agency email address, in an incident first disclosed last month.
Béatrice Cossa-Dumurgier, Revolut's CEO for Western Europe, said that the company would not pay ransoms to hackers, when asked if they had paid one. Revolut previously said it had not received a ransom demand.
Cossa-Dumurgier said Revolut had provided assistance for the 680 affected clients. It is understood that 12 Irish customers of these 680 customers worldwide were affected. 55 of them were in France.
"If they ever have to change their ID documents, we're taking care of the associated costs", she added, without specifying whether this had happened yet or how much it could cost the company.
Financial institutions are required to send customer data to authorities when asked to do so as part of investigations into potential crimes.
Matteo Piantedosi, Italy's interior minister, told lawmakers on September 30 that the email address to which Revolut sent customer data came from the Reggio Calabria police's email system, but was an address that had never been used before.
Revolut could have and should have verified the request by doing minimal due diligence, the minister said.
A spokesperson for Revolut declined to comment on the interior minister's remarks.
Cossa-Dumurgier said that government agencies are sometimes the "weak link" in the system and that Revolut's own systems had not been compromised.
More stories on

 News 
 

 Business 
 

 Revolut 
 

 Your Money 
 

 Béatrice Cossa-Dumurgier 
 
 Source: Reuters

### Прочие ссылки (без извлечённого текста)

- <https://www.bfmtv.com/economie/replay-emissions/le-grand-entretien/video-beatrice-cossa-dumurgier-revolut-revolut-a-obtenu-une-licence-bancaire-en-france-07-10_VN-202610070203.html>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Revolut to cover costs for 680 customers hit by data hack
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
De-PR'd: Revolut was **socially engineered**, not technically breached. Attackers took control of a never-before-used certified-email (PEC) address on an Italian government domain — specifically the **Reggio Calabria police/Prefecture email system** — and, posing as law enforcement over several months, sent Revolut what looked like legitimate official data requests. Revolut handed over personal files on **680 customers worldwide** (Italy's govt says 8 Italian; CEO's framing cites 55 France, 12 Ireland — note the Italian-count discrepancy, see Q below). Data that went out, per external reporting: identity/contact details, **passport/ID-document scans, verification selfies, IBANs, account statements, and Bitcoin transaction histories** — i.e. a KYC-grade dossier. Hackers reportedly claimed ~147GB and specifically targeted **"crypto whales."**
- Timeline: first disclosed **2026-09-12** (Revolut confirmation; Irish Times/TechCrunch 15–16 Sept); Italy interior minister **Matteo Piantedosi** told the Chamber of Deputies on **2026-09-30** the request came from a Reggio Calabria police address never previously used, and that "Revolut could and should have verified the request by doing minimal due diligence." This **2026-10-07** item is the **CEO-interview follow-on** (Béatrice Cossa-Dumurgier, Western Europe CEO, on BFM TV): Revolut will **cover ID-document replacement costs**, will **not pay ransoms** (says none demanded), and insists "government agencies are the weak link," its own systems were not compromised.
- **Why framed this way:** the "we weren't hacked, the government was the weak link" line shifts liability narrative onto the Italian state; but the minister's "minimal due diligence" rebuke is the counter-frame — the real failure is Revolut's **request-verification controls** for law-enforcement data demands. The compensation offer (ID replacement) is cheap and deflects from the harder, uncosted exposure: passports + selfies + Bitcoin histories enable durable identity-theft and targeted extortion that an ID reissue does not fix. CEO declined to quantify cost or say whether anyone has yet needed a new ID — vagueness flag.

## [1] Competitors / peers
Third-party / social-engineering data exposures at fintechs are a recurring 2026 pattern — Revolut is squarely in the cluster, not an outlier:
- [[Ledger says payments partner leaked customer data in new breach]] (2026-01) — vendor (Global-e) leaked names/contacts; fuels phishing.
- [[Betterment confirms data breach via fake crypto notification]] (2026-01).
- [[SoFi confirms third-party data breach at Hong Kong subsidiary]] (2026-06) — scope undetermined.
- [[Polymarket says hackers stole users' funds via third-party breach]] (2026-06) — refunds users; direct analog to "we'll cover costs" posture.
- [[Klue breach exposes data at multiple cybersecurity firms]] / [[LastPass says hackers stole support data in Klue breach]] (2026-06) — supply-chain exposure even at security vendors.
- [[TWIF FCA and ICO probe Lloyds app data exposure]] (2026-03) — same UK regulators (FCA + ICO) now engaged on Revolut.
- **Position:** mechanism is distinctive — most peers are breached *via a vendor's systems*; Revolut *voluntarily shipped* data to a spoofed authority, i.e. a **process/authentication failure in its law-enforcement-request pipeline**, closer to an "EDR (emergency-data-request) fraud" than a classic exfiltration. **Why it matters:** this attack class scales across every regulated fintech that must answer govt data demands; the delta vs peers is that no system was "hacked," so patching code doesn't fix it — only verification policy does.

## [2] Company history / fit
Fits an accumulating Revolut risk-controls theme, not an isolated slip:
- [[Revolut tops UK bank fraud complaints for third year]] (2025-10) — 3,208 FOS fraud complaints, worst UK firm 3 years running.
- [[Revolut suspends inbound PayTo top-ups in Australia after security incident]] (2026-05) — ~250 mule accounts, up to A$3M misdirected.
- [[Revolut's UK banking licence bid hits risk-control setback]] / [[Revolut's full UK banking licence held up by risk concerns]] (2025-10) — regulators repeatedly flagged **risk-control maturity**.
- Scale context: raising at [[Revolut plans secondary share sale at $100-120 billion valuation]] (2026-05), expanding aggressively ([[Revolut plans second EU bank in Paris with French licence]]). **Why:** hyper-growth across dozens of jurisdictions (the note's neighbours: Philippines, Israel, Hungary licences same month) multiplies the surface for jurisdiction-specific authority-request fraud while central control maturity lags — the same "growth outpaces controls" gap regulators cited on the UK licence. This incident is that structural tension surfacing operationally.

## [3] Novelty / value-add / traction
- **Not a new event for the world** (disclosed Sept 12), but a **new development**: first corpus coverage + the CEO's explicit compensation commitment and ransom stance + Piantedosi's parliamentary testimony are genuinely new beyond the initial September confirmation.
- "Value-add" here is reputational/regulatory, not product: Revolut's ID-cost reimbursement mirrors Polymarket's refund playbook — a **limited, optics-driven remediation**. **Why it's thin:** reissuing a passport does not remediate exposed selfies, bank statements, or Bitcoin transaction graphs; those feed long-tail extortion/identity fraud, which no announced remedy addresses. The durable question is **control reform** (how Revolut authenticates govt/LEO data requests going forward), on which there is **no disclosed change** — open.
- Traction/liability real-world: UK **FCA** engaged; UK **ICO** assessing the report; **Lithuania's State Data Protection Inspectorate** (Revolut's EU GDPR lead supervisor via its Lithuanian bank licence) assessing — GDPR fines can reach 4% of global turnover, so the tail risk is non-trivial even if base case is a reprimand.

## [4] What's next / market sentiment
- Watch: (1) Lithuanian SDPI / ICO outcome — a formal GDPR finding vs closure; (2) whether Italy's criminal probe (Reggio Calabria prosecutors, Postal Police, DNA anti-mafia directorate) attributes/charges anyone; (3) whether Revolut publishes a **request-verification control change** — the only fix that matters; (4) spillover to the still-pending **UK banking licence** and the French second-bank push, where risk-controls are the gating issue.
- **Second-order (analysis):** the counterintuitive risk is reputational not financial — 680 customers is tiny, ID-cost is immaterial to a ~$100B+ company, but the *framing* ("blame the government") plus a minister publicly saying "minimal due diligence would have caught it" hands regulators a live example precisely while Revolut is asking those same regulators (FCA) for a full banking licence. The breach's weight is as **leverage in the licence negotiation**, not as a standalone loss. **Why fresh-but-mid-weight:** real regulatory hooks (3 authorities) and a sensitive data set, but small customer count, no funds lost, and no disclosed control reform cap it below a systemic event.

## Sources
- Note primary: rte.ie (Reuters), 2026-10-07 — <https://www.rte.ie/news/business/2026/1007/1594438-revolut-will-cover-costs-for-customers-hit-by-data-hack/>
- BFM TV interview (Cossa-Dumurgier) — <https://www.bfmtv.com/economie/replay-emissions/le-grand-entretien/video-beatrice-cossa-dumurgier-revolut-revolut-a-obtenu-une-licence-bancaire-en-france-07-10_VN-202610070203.html>
- Irish Times (crypto-whale targeting, 147GB claim), 2026-09-16 — <https://www.irishtimes.com/business/2026/09/16/hackers-say-they-breached-italian-state-email-to-target-revolut-crypto-whales/>
- TechCrunch confirmation, 2026-09-12 — <https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/>
- MLex (FCA + Lithuanian SDPI; ICO assessing) — <https://www.mlex.com/mlex/data-privacy-security/articles/2527689/revolut-breach-on-desks-of-uk-finance-regulator-lithuanian-privacy-watchdog> ; <https://www.mlex.com/mlex/data-privacy-security/articles/2525511>
- Piantedosi testimony / Reggio Calabria PEC — <https://pasqualepillitteri.it/en/news/19815/revolut-piantedosi-ghost-pec-reggio-calabria>
- CybelAngel / thecybersecguru (data types: passports, selfies, statements, BTC history) — <https://cybelangel.com/blog/revolut-data-breach-what-we-know/> ; <https://thecybersecguru.com/news/revolut-data-breach-2026/>
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Was this a hack of Revolut at all?** No — social engineering of Revolut's law-enforcement-request process via a spoofed Italian govt PEC address. Revolut's systems were not breached. The honest framing is a **control/verification failure**, not an intrusion. (answered)
2. **How many customers, and why do the numbers conflict?** 680 worldwide (Revolut + Italy govt agree). CEO cites 55 France, 12 Ireland; Italy says 8 Italian. The "8 Italian" vs the Italian-govt origin of the attack is the discrepancy to watch — the bulk of the 680 are non-Italian despite an Italian-govt vector. (mostly answered; national split incomplete — open)
3. **What data actually leaked?** Per external reporting: ID/contact details, passport & ID-document scans, verification selfies, IBANs, bank statements, Bitcoin transaction histories. Revolut has not itemized this publicly in the note's source. (answered externally; Revolut disclosure vague)
4. **Does "cover ID-replacement costs" remediate the harm?** No. Reissuing a passport does nothing for leaked selfies, statements, or BTC transaction graphs, which enable durable identity theft/extortion. The remedy is optics-sized, not harm-sized. (answered — analysis)
5. **Has anyone actually needed/claimed a new ID yet, and what's the cost cap?** CEO explicitly declined to say. (open)
6. **Is this a NEW event or a re-run of the September disclosure?** New *development* (CEO compensation commitment + ransom stance + Piantedosi testimony) on an event first disclosed 2026-09-12. No prior corpus note on the breach exists. → **fresh**. (answered)
7. **Did Revolut pay a ransom?** CEO says no, and says none was demanded. Unverifiable externally; take at face value but flag. (answered, low confidence)
8. **Which regulators are live and what's the max exposure?** UK FCA (engaging), UK ICO (assessing), Lithuania SDPI (EU lead supervisor via Lithuanian licence). GDPR tail = up to 4% global turnover; base case likely reprimand. (answered)
9. **Is the Italian criminal angle material to Revolut?** Reggio Calabria prosecutors + Postal Police + DNA (anti-mafia) investigating the compromised PEC — but focus is the attacker/govt account, not Revolut liability directly. Minister's "minimal due diligence" line is the reputational hit. (answered)
10. **Is this idiosyncratic or a sector-wide attack class?** Sector-wide: emergency/law-enforcement-data-request (EDR) fraud threatens every regulated fintech obliged to answer authority demands. Peers hit via different vectors in 2026 (Ledger, SoFi, Polymarket, Betterment, Klue). (answered)
11. **Does it connect to Revolut's prior risk-control flags?** Yes — pattern with fraud-complaints #1 (3 yrs), Australian PayTo mule incident, and UK-licence risk-control setbacks. Growth-outpaces-controls thesis. (answered)
12. **What control change has Revolut announced to prevent recurrence?** None disclosed. This is the single most important open item — the only fix that addresses root cause. (open)
13. **What's the real downside trigger?** Not the £-cost (immaterial at ~$100B valuation) but leverage this hands FCA while Revolut seeks a full UK banking licence and pushes its French/EU bank. (answered — analysis)
14. **Were the targets random or selected?** Hackers reportedly targeted "crypto whales" and obtained BTC transaction histories — suggesting curated, high-value targeting, raising extortion/physical-risk tail for affected customers. (answered externally)
15. **Could this recur across other jurisdictions Revolut just entered?** Structurally yes — same month the note's neighbours show Philippines/Israel/Hungary activity; each new regulator relationship is a new authority-request attack surface. (open — analysis)

Importance: 3/5 — Genuinely fresh development with real regulatory hooks (three authorities incl. GDPR lead supervisor), sensitive data set (passports/selfies/BTC histories), a ministerial rebuke, and tight fit to Revolut's recurring risk-control narrative at the exact moment it seeks a UK banking licence. Capped below systemic: only 680 customers, no funds/access/biometric loss claimed, remediation is optics-sized, and no root-cause control reform disclosed.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-10]] (2026-10-10).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Neobanking/KYC-data risk. Revolut is Europe's most valuable startup: FY2025 revenue £4.5bn (~$6.0bn, +~50% YoY), profit before tax £1.7bn (~$2.3bn, ~38% PBT margin), 68.3m retail + 767k business customers, 5th consecutive profitable year (per Revolut Annual Report 2025, assets.revolut.com/pdf/annualreport2025.pdf, as of 2025-12-31). The structural driver here is not growth but **regulatory data-handling liability**: neobanks sit on dense KYC stacks (passports, selfies, IBANs, full transaction + crypto history) and are legally obliged to disclose customer data to authorities on request (per rte.ie 2026-10-07) — making the "government request" the soft underbelly of the compliance perimeter. Why now: EU GDPR enforcement is accelerating (>€7.1bn cumulative fines since 2018, ~€1.2bn in 2025 alone, per Kiteworks 2026); a breach of 680 high-profile accounts via a compromised Italian Interior Ministry email (Reggio Calabria police domain, per Italy's interior minister 2026-09-30) lands into a hostile enforcement climate.

**Competitive landscape.** Neobank KPIs: customers/ARPU, deposit balances (£50.2bn / ~$67.5bn FY2025), PBT margin, and — increasingly — **trust/incident record**. Basis of competition is distribution + product breadth + regulatory footprint (Revolut holds UK, Lithuania, Mexico, Colombia licences; filed US charter). Recent moves: $115bn secondary share sale Jul 2026 (Bloomberg 2026-07-22); UK full banking licence; reiterated no IPO before 2028. Position: **category leader by scale and valuation**, but a serial laggard on operational-integrity metrics — worst UK firm for fraud complaints for a third year (3,208 complaints to the FOS in 2025 YTD, per Which?, see [[Revolut tops UK bank fraud complaints for third year]]); Bank of Lithuania £3m AML fine; Italy €11.5m+€1.5m misleading-fees penalty (fintech.global 2026-04). Moat is scale + network/switching costs `(analysis)`, not process rigour.

**Comps & multiples.** Private — no public market cap; use last-round/secondary valuations (round valuations, NOT market cap).
- Revolut, $115bn (Jul 2026 secondary): EV/Rev ≈ `$115bn / $6.0bn = ~19x`; value-per-user ≈ `$115bn / 68.3m = ~$1,684/user`.
- Revolut prior round, $75bn (Nov 2025, see [[Revolut raises $3B at $75 billion valuation]]): `$75bn / $6.0bn = ~12.5x` — i.e. valuation re-rated +53% in ~8 months on broadly the same revenue base, so most of the uplift is multiple expansion, not fundamentals (hypothesis).
- Internal private-neobank comps (lower scale, revenue not comparably disclosed → multiples "no data"): [[Gulf Startup Tabby nabs $4.5 billion valuation in secondary sale]] ($4.5bn), [[Mexico's Plata raises $250M at $3.1B valuation]] ($3.1bn).
- Distribution not computed (only 1 revenue-backed multiple available). Flag: at ~19x revenue Revolut is **rich for a bank-like entity** (incumbent banks trade ~1–3x revenue / ~8–12x P/E), but in line with hyper-growth fintech given ~50% growth and 38% PBT margin — not an automatic over-valuation flag. P/E on the $115bn round = `$115bn / $1.7bn PBT ≈ ~68x` [UNSOURCED net-income basis] — stretched even for the growth rate.

**Risk flags.**
1. **Process/due-diligence risk** — the minister said Revolut "could and should have verified the request by doing minimal due diligence" (rte.ie 2026-10-07). The breach was social-engineering, not a systems hack; the second-order read is that Revolut's manual compliance-response controls scale worse than its user base, and this compounds its already worst-in-class fraud-complaint record.
2. **Regulatory/GDPR tail** — no sanction announced as of 2026-10-06, but a 680-record KYC breach (passports, selfies, crypto history) during peak EU enforcement is a latent fine + heightened-scrutiny risk precisely as the US charter and 2028 IPO ambitions require a clean regulatory sheet.
3. **Valuation sensitivity to trust** — a $115bn private mark (~19x revenue) resting on growth and brand is exposed to re-rating if trust erosion (fraud complaints + breach) slows customer adds; cost of covering ID-document replacement is disclosed as open-ended ("without specifying... how much it could cost").

**What this changes (idea-lens).** `(analysis)` The incident reframes neobank risk from fund security to **data-custody / third-party-request integrity** — a vector no neobank has underwritten well. Falsifiable thesis: this becomes a sector-wide control-tightening catalyst (verified-request protocols for gov/LE data demands) rather than a Revolut-specific event. Watch: whether an EU DPA opens a formal probe or levies a fine within 6–12 months (trigger confirming regulatory tail); absence of any enforcement by mid-2027 would weaken the thesis.

Sources: https://www.rte.ie/news/business/2026/1007/1594438-revolut-will-cover-costs-for-customers-hit-by-data-hack · https://assets.revolut.com/pdf/annualreport2025.pdf · https://www.bloomberg.com/news/articles/2026-07-22/revolut-confirms-115-billion-valuation-in-secondary-share-sale · https://fintech.global/2026/04/07/revolut-faces-e11-5m-penalty-over-fee-claims/ · https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (context, not an earnings print).** This pick is a security/breach event (Revolut to cover ID-document costs for 680 customers after data was handed to hackers who spoofed an Italian government email), not a quarterly result. Framing: Revolut's financial scale makes the direct cost trivially immaterial. Latest reported results = FY2025 (year ended 31 Dec 2025, Revolut Group Holdings Ltd Annual Report, published 2026-04-29). Record year: revenue £4.5bn (+46% YoY), pre-tax profit £1.7bn (+57% YoY), net profit £1.3bn (+65% YoY). The incident touches ~0.001% of a 68.3m retail base; the ID-reissue cost it has committed to is not quantified by the company and is negligible vs a near-£2bn annual PBT.

**Key figures (FY2025, reported in GBP in the Annual Report; USD equivalents are Revolut's own press-release conversions).**
- Revenue: £4.5bn, +46% YoY (Revolut press release reports this as $6.0bn, up from $4.0bn).
- Pre-tax profit: £1.7bn, +57% YoY ($2.3bn). PBT margin 38%, up from 35% in 2024.
- Net profit: £1.3bn, +65% YoY (2024: £0.8bn). Fifth consecutive year of net profitability.
- Gross profit margin: 78%.
- Retail customers: 68.3m, +30% YoY (16m added in-year). Business customers: 767k, +33% YoY.
- Total customer balances / deposits: $67.5bn, +66% YoY.
- Revenue mix: fee-based ~76% of turnover; interest income ~21.6%. 11 product lines each >£100m revenue. Transaction volume £1.3tn, +65% YoY.

**Materiality of the breach vs the financials.** 680 customers affected worldwide (55 in France, ~12 in Ireland) = ~0.001% of the 68.3m retail base. No funds, access codes or biometric data compromised; the firm's own systems were not breached (attackers compromised an Italian government agency domain and requested files; financial institutions are legally obliged to hand customer data to authorities on request). Revolut has committed to cover ID-document reissue costs — unquantified, "without specifying... how much it could cost" — and states it will not pay ransoms (no ransom demand received). Against a £1.7bn annual PBT and £1.3bn net profit, any plausible per-customer ID-reissue bill for 680 people is immaterial to earnings. The residual risk is reputational/regulatory (Italy's interior minister said Revolut "could have and should have" done minimal due diligence), not financial.

**vs expectations / prior period.** No consensus applies (Revolut is private, reports annually, not quarterly). vs prior year: revenue +46%, PBT +57%, net profit +65% — margin expansion (PBT margin 35%→38%) on top of top-line acceleration. No internal prior-period note found in the corpus for this company (Revolut reports annually, so no quarterly trend line).

**Guidance / forward.** None given in the usual earnings-guidance sense (private company). Management framing emphasised the US push and continued scaling; no numeric forward guidance is in the public domain [UNSOURCED].

**Thesis-flags.**
1. Scale = shock-absorber. A breach touching 0.001% of customers with a self-funded, unquantified remediation is a rounding error against £1.7bn PBT → the thesis-relevant risk is reputational/regulatory trust, not a P&L hit. Second-order: as Revolut pursues a US banking push and deeper EU licensing, repeated data-handling lapses (even third-party-triggered) raise supervisory scrutiny more than they dent earnings.
2. Growth still accelerating with margin expansion (PBT margin 35%→38%, net profit +65% > PBT +57% > revenue +46%) — operating leverage intact; a one-off breach does not change the earnings trajectory.
3. Currency presentation gap to note for de-PR: Revolut's own press release headlines USD ($6.0bn / $2.3bn) while the statutory Annual Report is in GBP (£4.5bn / £1.7bn) — same results, larger-sounding USD figures in the PR.

Sources: Revolut Group Holdings Ltd Annual Report 2025 (year ended 31 Dec 2025), https://assets.revolut.com/pdf/annualreport2025.pdf · Revolut press release "record profit of $2.3bn for 2025 as revenue surges to $6bn", https://www.revolut.com/en-US/news/revolut_reports_record_profit_of_2_3bn_for_2025_as_revenue_surges_to_6bn/ · CNBC, https://www.cnbc.com/2026/03/24/revolut-2025-earnings-record-profit.html · FinTech Futures, https://www.fintechfutures.com/challenger-banks/revolut-profit-jumps-57-to-1-7bn-for-2025 · breach details from the note (RTE/Reuters, 2026-10-07). Per-customer ID-reissue cost: not disclosed by company [UNSOURCED].
<!-- /enrichment:earnings_review -->
