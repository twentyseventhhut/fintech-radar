---
title: "Coinbase discloses customer-data exposure via analytics provider"
date: 2026-10-29
retrieved: 2026-10-29
tags:
  - company/coinbase
  - industry/crypto
  - industry/fraud-risk
  - region/global
  - type/outage-security
sources:
  - https://cointelegraph.com/news/coinbase-analytics-provider-customer-data
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s028fe4a4
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Coinbase discloses customer-data exposure via analytics provider

> [!info] 2026-10-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌎 Coinbase discloses customer-data exposure involving analytics provider. Customer information was exposed through a security incident involving third-party analytics provider Amplitude, rather than a breach of Coinbase's own systems. Coinbase said customer funds were not affected.

## Первоисточники

### cointelegraph.com
<https://cointelegraph.com/news/coinbase-analytics-provider-customer-data>
*272 слов · jina*

Coinbase said that an incident at analytics vendor Amplitude exposed some customers’ contact data, but it found no evidence of unauthorized access to its own systems.

Some Coinbase customers’ contact information was exposed in a security incident at analytics vendor Amplitude, the exchange said Wednesday.

The incident impacted a “small subset” of Coinbase customers, along with other Amplitude clients, Coinbase Support said on X.

Coinbase denied that its own systems had been breached and said customer funds were not affected.

The disclosure adds to Wednesday’s reports of cyberattacks affecting both crypto exchanges and traditional financial firms. In South Korea, Bithumb is investigating whether a breach of its internal work platform exposed customer information, while brokerage Daishin Securities reported a leak of personal and credit information belonging to 38,490 customers.

Cointelegraph contacted Coinbase to find out how many customers were affected but had not received a response by publication.

In May 2025, Coinbase disclosed a separate data breach that impacted less than 1% of its monthly transacting users. The exchange estimated reimbursement and remediation costs at up to $400 million.

_**Related:**__**Bloom bot hackers loot $953K faster than you can microwave popcorn**_

### Subscribe to daily byte-sized crypto news from Cointelegraph

Subscribe

Get more of Cointelegraph on Google

Add Cointelegraph as a preferred source for Google Search.

Cointelegraph is committed to independent, transparent journalism. This news article is produced in accordance with Cointelegraph’s Editorial Policy and aims to provide accurate and timely information. Readers are encouraged to verify information independently.

*   Coinbase
*   Cryptocurrency Exchange
*   Data
*   Cybersecurity
*   Hackers
*   Hacks
*   Scams & Cybercrime

## More on the subject

[](https://cointelegraph.com/news/bithumb-discloses-data-leak-after-internal-system-breach-report)[](https://cointelegraph.com/news/bloom-bot-hackers-953k-faster-popcorn)[](https://cointelegraph.com/news/keystone-breach-deepens-hackers-stole-key-used-to-verify-wallets-as-genuine)

[](https://cointelegraph.com/news/bithumb-discloses-data-leak-after-internal-system-breach-report)[](https://cointelegraph.com/news/bloom-bot-hackers-953k-faster-popcorn)[](https://cointelegraph.com/news/keystone-breach-deepens-hackers-stole-key-used-to-verify-wallets-as-genuine)

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Coinbase discloses customer-data exposure via analytics provider
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On Wednesday 2026-10-28/29, Coinbase Support disclosed via X that contact information for a "small subset" of its customers was exposed in a security incident at its third-party analytics vendor **Amplitude** (NASDAQ: AMPL), not through a breach of Coinbase's own systems. Amplitude itself disclosed the incident around 2026-10-28, saying it detected unauthorized access to parts of its internal systems (reportedly ~2026-09-28) affecting a small portion of customer event data across multiple Amplitude clients — Coinbase is one of several affected customers.

De-PR'd facts:
- Data involved = **contact data only** (reports cite email addresses and phone numbers). No claim that passwords, private keys, government IDs, SSNs, balances, transaction history, or funds were touched. Coinbase explicitly: customer funds not affected, no evidence of access to Coinbase systems.
- Coinbase did NOT disclose how many customers were hit, which exact fields, or the Amplitude compromise timeline. SlowMist researcher 23pds (third party, unverified by Coinbase) claimed >70,000 users affected — treat as an external estimate, not confirmed scope.
- **Why framed this way:** Coinbase is aggressively steering the narrative to "vendor incident, not a Coinbase breach, funds safe." That framing is accurate but also self-serving — the reputational point is to avoid this being read as a second Coinbase breach after the painful May 2025 one. The real exposure vector is the classic SaaS-supply-chain problem: a product-analytics tool ingests customer PII (emails/phones) to do its job, so a breach at the vendor is functionally a breach of the customer's users even if Coinbase's perimeter held.
- **Second order:** contact data (email + phone) is low-severity on its own but high-value as **phishing/smishing raw material** targeting a crypto-exchange userbase — the same population already primed by the May 2025 social-engineering campaign. The downstream risk is targeted phishing, not direct asset theft.

## [1] Competitors / peers
Third-party/vendor-linked fintech data exposures are now the dominant breach pattern, not perimeter hacks:
- [[UBS data breach exposes employee details via vendor Chain IQ]] (2025-06) — UBS employee data leaked via procurement vendor Chain IQ; same structural story (vendor, not bank, breached).
- [[Wealthsimple discloses third-party-linked customer data breach]] (2025-09) — client PII (incl. SINs, account numbers) exposed via a compromised software package; heavier data set than Coinbase/Amplitude.
- [[Crypto.com hit by unreported attack leaking user data]] (2025-09) — crypto peer, Scattered Spider; a direct exchange compromise (worse than a vendor contact-data leak).
- [[Betterment data breach exposes 1.4 million accounts]] (2026-02) — far larger exposure at a wealth fintech.

Position: on the severity ladder this Coinbase/Amplitude event is on the **low end** — contact data only, "small subset," no financial/identity data, perimeter intact — materially less serious than Crypto.com's direct exchange breach or Coinbase's own May 2025 insider breach. **Why the landscape looks this way:** fintech attack surface has shifted to the vendor graph (analytics, procurement, support-outsourcing) because the primary targets hardened; the marginal attacker now hits the softest shared dependency, and one vendor breach fans out across all its clients simultaneously.

## [2] Company history / fit
Coinbase's recent security trajectory:
- May 2025: **insider-bribery breach** — external actors bribed overseas support contractors to exfiltrate data on ~69,461 people (names, contacts, last-4 SSN, masked bank details, gov-ID images, balances, tx history), <1% of monthly transacting users. Coinbase refused a $20M ransom, offered a $20M reward, and guided remediation/reimbursement cost of **$180M–$400M**.
- Feb 2026: [[Coinbase confirms insider breach affecting 30 customers]] — small insider-linked incident.
- May 2026: [[Coinbase reports record Q1 trading share, resumes service after outage]] — operational, record volumes.

This Amplitude incident is a **distinct, new event** (different vector: a SaaS analytics vendor, not insiders; different, much lighter data: contact info only; different timeline: Sept–Oct 2026). It is NOT a re-run of the May 2025 breach — the $400M/$20M figures belong to that earlier incident and should not be attached here. **Why it keeps happening to Coinbase:** as the largest, most trusted US exchange it is the highest-value target in crypto and carries a large third-party/outsourced operational footprint (support contractors, analytics vendors) — each dependency is an attackable edge, so the pattern is structural, not a one-off failure.

## [3] Novelty / value-add / traction
Low novelty — it is one more supply-chain data exposure. The only genuinely new facts: (a) Coinbase's analytics stack includes Amplitude and that pipeline carried customer contact PII; (b) a single Amplitude compromise simultaneously hit multiple named clients. Traction/impact so far is modest and unquantified by the company: "small subset," contact data only, no funds, Coinbase notifying affected users and regulators per legal obligation. The >70K figure is an unverified third-party estimate. **Why the real weight is limited:** no asset loss, no sensitive-identity loss, perimeter intact — so the durable cost is reputational and phishing-exposure, not balance-sheet. Unlike May 2025 there is (so far) no disclosed remediation/reimbursement liability.

## [4] What's next / market sentiment
Expect: user notifications, regulator notifications, and a short news cycle framing this as "another Coinbase data issue" even though it is a vendor incident. Amplitude (public, AMPL) carries the primary accountability and some client/reputational risk. **Why the market mostly shrugs on the Coinbase side:** contact-data-only leaks rarely move COIN or usage; the structural signal, however, is that crypto-exchange users remain a concentrated phishing target, and repeated contact-data leakage compounds the social-engineering risk already demonstrated in 2025. Counterintuitive second-order: the "it was only the vendor" framing is comforting but points to a larger unmanaged risk — Coinbase's security is only as strong as the weakest SaaS tool allowed to ingest customer PII. Watch for (open) confirmed scope, exact fields, and any downstream phishing wave.

## Top challenge/extra questions (10–15, second-order)
1. Exact scope — how many Coinbase users, confirmed by Coinbase (not the >70K SlowMist estimate)? **Open** (Coinbase declined to say).
2. Exact fields beyond email/phone — any names, account identifiers? **Open / likely contact-only per statements.**
3. Is this the same incident as May 2025? **No — distinct vendor (Amplitude) vs insider-bribery; distinct data; distinct 2026 timeline.** The $400M/$20M figures are May 2025's, not this event's.
4. Why did Amplitude hold Coinbase customer PII at all — product-analytics ingesting emails/phones. Is minimization possible? **(analysis) Yes; a tightening opportunity.**
5. When did the Amplitude compromise actually start/end? **Open** (detection reported ~2026-09-28; not confirmed by Coinbase).
6. Which other Amplitude clients were affected? **Open** ("other Amplitude customers," unnamed).
7. Real downstream risk — asset theft vs phishing? **Phishing/smishing of exchange users; no direct asset-theft vector from contact data.**
8. Does Coinbase face remediation/reimbursement liability like May 2025? **No disclosed liability yet — much lighter data set.**
9. Is Amplitude or Coinbase legally on the hook for notifications? **Both notifying per obligations; Coinbase confirmed it is notifying users + regulators.**
10. Is the ">70,000 users" and any "$20M extortion" being wrongly carried over from May 2025? **Risk of conflation — the $20M ransom/reward was May 2025; do not attach it to Amplitude.**
11. Does this move COIN or Coinbase usage? **(hypothesis) No — contact-data leaks are not market-moving.**
12. What is the structural lesson? **Vendor/SaaS graph is now the primary fintech breach surface; one vendor breach = fan-out across clients.**
13. Did Coinbase's own systems hold? **Yes per Coinbase — no evidence of access to Coinbase systems; funds unaffected.**
14. Is "small subset" PR minimization? **Possibly — unquantified; third parties suggest tens of thousands.**
15. What would raise importance? **Confirmation of sensitive fields, a large verified count, or a documented phishing wave — none yet.**

Importance: 2/5 — a real but low-severity, low-novelty supply-chain contact-data exposure; no funds, no sensitive identity data, perimeter intact; distinct from (and far lighter than) the May 2025 breach.

## Sources
- cointelegraph.com — Coinbase denies breach, vendor Amplitude exposed customer data (primary, in note).
- cybersecuritynews.com, financefeeds.com, coingape.com, ccn.com, egamers.io — Amplitude incident scope, >70K SlowMist estimate, contact data (email/phone).
- gurufocus.com — Amplitude (AMPL) addresses security breach impacting customer data (vendor disclosure, detection ~2026-09-28).
- cnbc.com / securityinfowatch.com / cointelegraph.com — May 2025 insider-bribery breach (~69,461 users, $20M ransom refused, $180M–$400M cost) — for contrast only.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team challenge questions (second-order) — Importance: 2/5

1. **Confirmed scope?** How many Coinbase users, verified by Coinbase itself? Open — Coinbase said only "small subset" and declined to give a number. The >70,000 figure is a SlowMist (23pds) third-party estimate, unverified.
2. **Which data fields?** Reports cite email addresses and phone numbers (contact data). No claim of passwords, private keys, gov-ID, SSNs, balances, or transaction history. Likely contact-only; exact fields not confirmed.
3. **Same incident as May 2025?** No — this is DISTINCT. May 2025 = insider-bribery (bribed support contractors), ~69,461 users, sensitive PII, $180M–$400M remediation, $20M ransom refused. This = third-party analytics vendor Amplitude, contact data only, Sept–Oct 2026. Fresh event.
4. **Beware conflation:** do NOT attach the $20M extortion/reward or $400M cost to the Amplitude event — those belong to May 2025. Some aggregated coverage blurs the two.
5. **Did Coinbase's perimeter hold?** Yes per Coinbase — no evidence of unauthorized access to Coinbase's own systems; customer funds not affected. The exposure was entirely at the vendor.
6. **Why did Amplitude even hold this PII?** Product analytics ingests customer emails/phones to function; this is the structural SaaS-supply-chain exposure. Data-minimization is the obvious (analysis) remediation lever.
7. **Amplitude timeline?** Vendor reportedly detected unauthorized internal access ~2026-09-28, disclosed ~2026-10-28. Full compromise window not confirmed by Coinbase.
8. **Other victims?** "Other Amplitude customers" affected, unnamed. One vendor breach fans out across all clients — the real systemic signal.
9. **Downstream risk?** Phishing/smishing against crypto-exchange users (the valuable use of leaked contacts), not direct asset theft. Compounds the social-engineering risk already shown in 2025.
10. **Financial/market impact?** No disclosed remediation or reimbursement liability (unlike May 2025). (hypothesis) Not COIN-moving; contact-data leaks rarely are.
11. **Is "small subset" PR minimization?** Possibly — unquantified by Coinbase while third parties cite tens of thousands. Treat as marketing vagueness until confirmed.
12. **Regulatory/legal?** Coinbase notifying affected users and regulators per obligations; Amplitude (public, AMPL) carries primary vendor accountability.
13. **Novelty?** Low — one more vendor/supply-chain data exposure. Only new facts: Amplitude is in Coinbase's stack and carried contact PII.
14. **What would raise importance?** Confirmation of sensitive fields, a large verified user count, or a documented phishing wave traced to this leak — none present yet.
15. **Structural takeaway?** Fintech breach surface has moved to the SaaS/vendor graph; Coinbase's security is only as strong as the weakest third party allowed to ingest customer PII.

**Importance: 2/5** — real but low-severity, low-novelty supply-chain contact-data exposure; no funds, no sensitive identity data, perimeter intact; a genuinely NEW event (vendor Amplitude), distinct from and far lighter than the May 2025 insider breach → freshness: fresh.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto-exchange cybersecurity is a structurally recurring cost, now increasingly *third-party/supply-chain* in origin rather than core-system breaches. This Amplitude incident is one of a cluster disclosed on the same day (27–28 Oct 2026): South Korea's Bithumb (internal groupware access under investigation), brokerage Daishin Securities (38,490 customers' personal + credit data, incl. bank account numbers), and a blocked attempt at Mirae Asset — per CoinDesk / CryptoTimes, 28 Oct 2026. The pattern: as exchanges harden their own custody/key infrastructure, the attack surface migrates to vendors with legitimate data access (analytics, support, KYC processors). Structure: value chain is fragmenting across SaaS vendors (Amplitude = product analytics), so a single vendor compromise fans out across many clients simultaneously — Coinbase explicitly noted "other Amplitude clients" were also hit. "Why now": no financial-account funds are taken in these vendor exposures, but contact-data leaks (email/phone) are the fuel for the phishing/social-engineering economy that previously cost Coinbase up to $400M (see below).

**Competitive landscape.** Sector KPIs that matter here: monthly transacting users (MTU) exposed as % of base; remediation/reimbursement cost; and incident *recurrence*. Named peers in the same-day wave: Bithumb, Daishin Securities, Mirae Asset (Korea). Prior in-base third-party-vendor incidents span the sector and beyond: BigONE ($27M stolen in a third-party attack), Transak (92,000+ users via phishing), Wealthsimple (compromised software package), UBS/Chain IQ (vendor breach), SoFi (third-party at HK subsidiary). Coinbase's position: it is the largest/most-scrutinized US exchange ($7.2bn FY25 revenue — see IR), so each incident draws disproportionate regulatory + press attention regardless of root cause. Moat here is reputational, not technical: Coinbase's fast public denial of a core-systems breach and funds-safe messaging is brand-protection `(analysis)`.

**Comps & multiples — materiality anchored to IR.** Coinbase scale (IR, Q4'25 Shareholder Letter + FY2025 ARS/10-K): **FY2025 total revenue ~$7.18bn** (net revenue $6.88bn + other $0.30bn), up ~9% Y/Y from FY2024's $6.6bn; FY2024 net income $2.6bn, Adjusted EBITDA $3.3bn. Transaction revenue is dominated by Consumer ($3.32bn FY25). Against this, breach economics:
- **May 2025 insider breach (the key in-base comp):** 69,461 people affected (per Maine AG filing), characterized as <1% of MTU; estimated reimbursement + remediation **$180M–$400M**; $20M extortion refused; $20M reward fund. At the $400M high end that is ~5.6% of FY25 revenue — material but absorbable given ~$3.3bn EBITDA. See [[Coinbase confirms insider breach affecting 30 customers]] (Feb 2026, separate 30-customer contractor incident).
- **This Amplitude incident:** "small subset" of customers; SlowMist researcher 23pds claims ~70,000 users (UNCONFIRMED by Coinbase); **$20M extortion demand refused**; no funds affected. Direct cost not yet quantified → "no data" on remediation. Note the eerie symmetry with May 2025 (~70K, $20M extortion) — but this time the root cause is a vendor, so Coinbase's *direct* liability framing differs.
- In-base vendor-breach comps as orientation (no public per-incident cost): [[Crypto exchange BigONE loses $27 million in third-party attack]], [[Wealthsimple discloses third-party-linked customer data breach]], [[UBS data breach exposes employee details via vendor Chain IQ]], [[SoFi confirms third-party data breach at Hong Kong subsidiary]]. Trading multiples not computed — this is an operational/security event, not a valuation event.

**Risk flags.**
1. **Vendor/supply-chain concentration.** Coinbase's data-protection perimeter now extends to SaaS vendors it doesn't control (Amplitude, support contractors in May 2025). Second-order: liability and disclosure obligations attach to Coinbase even when its own systems are clean, so remediation cost is partly exogenous and hard to engineer away.
2. **Recurrence + regulatory accumulation.** Third Coinbase-linked customer-data event in ~18 months (May 2025 insider, Feb 2026 contractor, Oct 2026 vendor). Second-order: a visible pattern invites heavier regulator scrutiny (Coinbase said it is notifying authorities) and strengthens the standing of the open May-2025 class action — reputational drag on the #1 US exchange brand.
3. **Phishing-fuel externality (not funds).** Exposed email/phone is low-severity on its face but is precisely what powered the costly social-engineering attacks after May 2025. Second-order: the real cost tail is future fraud reimbursement, which lags the disclosure by months and is hard to pre-provision.

**What this changes (idea-lens).** The locus of crypto-exchange security risk is shifting from custody/key compromise to third-party data-vendor exposure — a harder problem because it is distributed across the SaaS stack and only partly under the exchange's control `(analysis)`. Falsifiable thesis: vendor-origin incidents will increasingly dominate exchange breach headlines, and the differentiator becomes third-party risk management + speed of disclosure, not just cold-storage hygiene. Trigger/catalyst to watch: whether Coinbase quantifies an Amplitude-related remediation charge in its next 10-Q, and whether the ~70K SlowMist figure is confirmed — confirmation near that scale would make this comparable to May 2025's $180M–$400M band; silence/denial would signal a materially smaller, contact-data-only event. Thesis breaks if the exposure proves immaterial and no fraud tail emerges.

Sources: https://www.coindesk.com/tech/2026/10/28/coinbase-says-customer-funds-are-safe-after-third-party-vendor-exposes-customer-contact-info · https://cointelegraph.com/news/coinbase-analytics-provider-customer-data · https://financefeeds.com/coinbase-denies-direct-data-breach-confirms-customer-information-exposed-through-analytics-vendor/ · https://www.ledgerinsights.com/coinbase-faces-up-to-400m-customer-compensation-costs-after-data-breach/ · https://investor.coinbase.com/files/doc_financials/2025/q4/Q4-25-Shareholder-Letter.pdf · https://www.sec.gov/Archives/edgar/data/1679788/000167978826000015/coin-20251231.htm
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Not an earnings release — scale-context frame only.** This is a third-party security incident (analytics vendor Amplitude exposed some customers' contact data; Coinbase says its own systems were not breached and funds were unaffected). There are no new results to analyze; the figures below exist only to anchor the breach's potential materiality to real, filed numbers. Do NOT read a beat/miss into this.

**Latest reported scale (to size materiality).**
- **FY2025 revenue $7.2B (+9% Y/Y)** — Coinbase operates at multi-billion annual scale, so a contact-data exposure at a vendor is immaterial to the top line unless it triggers large remediation/legal costs or churn (per Q4'25/FY2025 shareholder letter, 2026-02-12).
- **Q1'26 (period ended 2026-03-31, reported 2026-05-07): total revenue $1.41B, down ~21% Q/Q (≈ -31% Y/Y per press), with a net LOSS of $394.1M and Adjusted EBITDA of $303.3M** (13th consecutive quarter of positive adj. EBITDA). Transaction revenue $755.8M; subscription & services $583.5M (≈44% of net revenue); USDC on-platform a record ~$19B. The most recent quarter was already loss-making on a soft crypto market — incremental remediation costs land on an income statement with no margin cushion.
- **Monthly Transacting Users 7.6M in Q2'26 (three months ended 2026-06-30) vs 8.7M a year earlier** (latest 10-Q, period ended 2026-06-30) — a declining active base; reputational data-handling events are a second-order churn risk on top of the macro decline.

**Materiality anchor — the May 2025 precedent (de-PR).** The real cost signal is not in current results but in Coinbase's own prior disclosure: the separate May 2025 insider/support-agent breach hit **<1% of monthly transacting users (~69,461 customers)** and Coinbase estimated **reimbursement + remediation costs of $180M–$400M**. That is the yardstick for how a customer-data event converts into P&L impact at this company. The new Amplitude incident is described as a "small subset" of customers with **contact data only** (no credentials/funds) and, critically, **sits at a third-party vendor, not Coinbase's own systems** — so on current disclosure the expected direct cost is far smaller than the 2025 event, and no remediation-cost figure has been disclosed for it. [UNSOURCED: size of affected cohort and any cost estimate for the Amplitude incident — Coinbase had not responded on numbers as of publication.]

**Bottom line.** No results to review; materiality is low-probability-of-material unless the affected cohort or disclosed remediation cost grows toward the 2025 breach's $180M–$400M range. Watch the next 8-K/10-Q for any accrual or affected-customer count. Vendor-side exposure + contact-data-only scope argues for a sub-material outcome vs the 2025 precedent.

Sources: Q4'25/FY2025 shareholder letter (IR, 2026-02-12) https://investor.coinbase.com/files/doc_financials/2025/q4/Q4-25-Shareholder-Letter.pdf · Q1'26 results 8-K/earnings deck (EDGAR, 2026-05-07) https://www.sec.gov/Archives/edgar/data/1679788/000167978826000053/q126earningsdeck-finalse.htm · Q1'26 10-Q (EDGAR) https://www.sec.gov/Archives/edgar/data/0001679788/000167978826000054/coin-20260331.htm · Q2'26 10-Q, MTU (EDGAR) https://www.sec.gov/Archives/edgar/data/0001679788/000167978826000088/coin-20260630.htm · May 2025 breach $180M–$400M remediation estimate https://cointelegraph.com/news/coinbase-analytics-provider-customer-data · public figures (Yahoo Finance / Motley Fool Q1'26 transcript, as of 2026-05-08). Amplitude-incident affected-count and cost: no data / [UNSOURCED].
<!-- /enrichment:earnings_review -->
