---
title: "CJEU rules banks must refund phishing-victim unauthorised payments"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - industry/fraud-risk
  - industry/banking
  - region/europe
  - type/regulation
sources:
  - https://curia.europa.eu/jcms/jcms/Jo2_7052/en
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: se0fc6e32
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# CJEU rules banks must refund phishing-victim unauthorised payments

> [!info] 2026-10-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] The Court of Justice of the European Unionruled in Case C-70/25, brought by a Polish phishing victim who lost about €700, that a bank must refund an unauthorised payment promptly even where it alleges gross negligence — they may recover the money afterwards if it proves the negligence.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://curia.europa.eu/jcms/jcms/Jo2_7052/en>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 15 October 2026 the Court of Justice of the European Union (CJEU) ruled in **Case C-70/25 (Tukowiecka)**, a reference from a Polish court, that a payment service provider (PSP) must immediately refund an unauthorised payment transaction and may NOT withhold that refund on the ground that the customer acted with gross negligence. The underlying facts: a customer of Polish bank **PKO BP** in Koszalin lost ~3,000 zloty (≈ €700) after a fraudster posing as a buyer on an online marketplace sent a fake link spoofing the bank's login page; she entered her credentials, the money was taken, she reported it the next day, and the bank refused to refund, citing gross negligence. (Note: the aggregated digest text said "about €700"; CJEU press materials state 3,000 PLN.) Source: [CJEU judgment C-70/25 press release (cp260147)](https://curia.europa.eu/site/upload/docs/application/pdf/2026-10/cp260147en.pdf).

**[1] The "refund first, argue later" rule.** Under **PSD2 Article 73(1)**, a PSP must refund the amount of an unauthorised transaction immediately (by the next business day after notification). The CJEU held gross negligence does NOT suspend that obligation. The ONLY front-end exception: the PSP has reasonable grounds to suspect fraud BY the customer AND notifies the competent national authority in writing. The refund is not final — under **PSD2 Article 74**, the PSP may afterwards sue to recover the money if it PROVES the customer acted fraudulently or, through gross negligence, failed to protect personalised security credentials (Art. 69 obligations). The burden and the litigation cost thus shift from victim to bank. Sources: [CMS analysis](https://cms.law/en/pol/legal-updates/CJEU-opinion-of-Advocate-General-victims-of-online-fraud-must-receive-immediate-refunds-from-service-providers), [Skarbiec](https://kancelaria-skarbiec.pl/en/cjeu-c-70-25-unauthorised-payment-refund/).

**[2] Unauthorised vs authorised-push-payment (APP) — the scope limit.** This ruling concerns **UNAUTHORISED** transactions: the victim never approved the specific transfer (fraudster used stolen credentials). It does NOT cover **APP / authorised-push-payment** scams, where the victim is tricked into authorising the payment themselves — those sit outside Art. 73 PSD2 and remain a gap in EU law. The UK addresses the APP gap separately via the **PSR mandatory reimbursement scheme** (in force 7 Oct 2024): mandatory reimbursement within 5 business days, cost split 50/50 between sending and receiving PSPs, cap £85,000; PSR dashboard reported 88% of covered claim value (£173m) reimbursed Oct-2024–Sep-2025. The EU has no equivalent harmonised APP regime. Sources: [AO Shearman on UK APP scheme](https://www.aoshearman.com/en/insights/ao-shearman-on-fintech-and-digital-assets/the-uks-authorised-push-payment-app-fraud-reimbursement-scheme), [PSR](https://www.psr.org.uk/news-and-updates/latest-news/news/psr-confirms-new-requirements-for-app-fraud-reimbursement/).

**[3] Why it matters / forward link to PSD3 & PSR.** The ruling pre-empts the incoming **PSD3 / Payment Services Regulation (PSR)**. Draft **PSR Article 56** keeps the immediate-refund rule but lets a PSP suspend it where it has "objectively justified reasons" to suspect intentional or grossly negligent conduct (communicated in writing; 15-business-day decision window) — precisely the front-end withholding the CJEU just said is unlawful under current PSD2. So banks cannot lean on the PSR draft to keep withholding refunds today, and consumer groups argue the PSR drafting could weaken the protection the CJEU just affirmed. National transposition is already moving (e.g. Belgium's 15-day investigation window). Sources: [Chambers "Refund first, argue later"](https://chambers.com/articles/refund-first-argue-later-case-c-70-25-and-its-implications-for-the-upcoming-psd3-psr-framework), [EFRI on PSR Art. 56](https://efri.io/psr-article-56-phishing-refunds-gross-negligence/).

**[4] Internal context (prior notes).** Fraud-liability and scam-prevention pressure is a recurring thread in the DB: [[Starling Bank launches AI tool for customers to spot purchase scams]] (banks building front-line scam detection as liability tightens), [[Incognia report only 16% of firms catch mule-account fraud early]] (receiving-side / mule-account detection gap that reimbursement regimes penalise), [[The Financial Brand Frictionless payments as a fraud factory]] (frictionless UX vs fraud trade-off), and [[Suits Me partners with tell.money for PSD2 compliance]] (PSD2 operational compliance). This ruling raises the cost of weak controls by removing gross-negligence as a reason to delay refunds.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge**

1. **Is the ruling date right?** Yes — CJEU delivered judgment on 15 October 2026 in C-70/25 (confirmed by curia.europa.eu press release cp260147 and multiple legal commentaries). The note's digest text is undated for the ruling but consistent.

2. **Is "€700" accurate?** PARTLY. CJEU materials state the loss was ~3,000 zloty; at 2026 rates that is ≈ €700, so the digest figure is a reasonable conversion, not an official EUR figure. Noted in context.

3. **Is the party identification correct?** The claimant is a Polish consumer; the bank is PKO BP; the forum was a Polish national court referring to the CJEU. The digest's "Polish phishing victim" is correct.

4. **Does it really mean banks must ALWAYS refund?** NO — overstated if read that way. Banks must refund IMMEDIATELY and may NOT withhold on gross-negligence grounds, but can (a) refuse where they have reasonable grounds to suspect customer fraud and notify the authority in writing, and (b) claw back afterwards via court if they PROVE gross negligence/fraud. Headline is directionally right but loses this nuance.

5. **Does this cover APP (authorised push payment) scams?** NO — only UNAUTHORISED transactions (stolen credentials). APP scams where the victim authorises the payment are NOT covered by Art. 73 PSD2. Critical scope limit; the headline "phishing-victim" is correct because this phishing stole credentials to make an unauthorised transfer.

6. **Is the PSD2 article citation correct?** Yes — immediate refund = Art. 73(1); payer liability / gross-negligence clawback = Art. 74 (with Art. 69 credential-protection duties). Confirmed via betterregulation and BEUC/EBF guidance.

7. **Is it binding across the whole EU?** Yes — a CJEU preliminary ruling interprets PSD2 for all member states; national courts must apply this reading. Several jurisdictions (Belgium, Spain, Italy commentary) already reacting.

8. **Does the incoming PSR/PSD3 override it?** NO (yet). PSR is still draft; draft Art. 56 arguably conflicts with this ruling by allowing suspension on "objectively justified" negligence grounds. Until PSR is law, PSD2 as interpreted by C-70/25 governs. Open question: will the final PSR text be reconciled with the ruling?

9. **Is the UK APP comparison apples-to-apples?** NO, and the context flags it: UK PSR scheme covers APP scams (different fraud type) and is a reimbursement regime split across PSPs; C-70/25 covers unauthorised transactions under PSD2. They address adjacent but distinct gaps.

10. **Who bears the financial hit?** Sending bank (the PSP) refunds first. Receiving-side / mule-account detection failures raise exposure (see [[Incognia report only 16% of firms catch mule-account fraud early]]). No automatic inter-PSP split like UK's 50/50 for unauthorised transactions under PSD2.

11. **Is there any carve-out that lets banks stall indefinitely?** Only the fraud-suspicion + written notification to national authority route; otherwise the next-business-day deadline applies. A bank cannot simply assert "gross negligence" to delay.

12. **Novelty vs prior CJEU case law?** This sharpens the "refund first, argue later" principle and removes gross negligence as a front-end defence — a meaningfully pro-consumer clarification, not merely restating prior law. No earlier note in the DB covers this ruling, so it is fresh, not a duplicate.

13. **Could the digest conflate AG Opinion with final judgment?** Risk flagged — earlier 2026 coverage was AG Rantos' Opinion; the 15 Oct 2026 item is the FINAL judgment, which followed the AG. Context uses the final-judgment framing.

14. **Open: quantified bank cost impact?** Not disclosed — commentaries note "immediate and significant" operational/litigation cost shift but no EU-wide figure. Open.

15. **Open: enforcement / penalties for non-compliant banks?** PSD2 refund duty is enforced via national competent authorities and private claims; specific sanctions vary by member state. Open.

**Importance: 4/5** — a binding, EU-wide CJEU interpretation of PSD2 that shifts fraud-refund liability and litigation burden from consumers to banks, directly pre-empts the PSD3/PSR drafting debate, and materially raises the cost of weak fraud controls for every EU PSP. Not a 5 because it is confined to unauthorised (not APP) transactions and largely reaffirms/clarifies existing PSD2 obligations rather than creating new ones.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-23]] (2026-10-23).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a payment-fraud-liability / fraud-prevention story, not a company deal — the protagonist is the regulatory regime (EU PSD2, feeding into PSD3/PSR) and its cost-bearers (banks/PSPs). Scale of the problem: EU/EEA payment fraud reached €4.2bn in 2024, up 17% from €3.5bn in 2023; credit transfers alone were €2.20bn (+16% YoY), cards €1.33bn (+29% YoY) (per EBA-ECB 2025 Report on Payment Fraud, Dec 2025). The UK (post-Brexit, own regime but a leading comparator) lost £1.28bn to payment fraud in 2025, of which unauthorised fraud was £703.4m (−5%) and APP fraud £576.4m (+19%) (per UK Finance Annual Fraud Report 2026). Structure: liability is highly fragmented across issuing/acquiring banks, PSPs and payment schemes; the value-chain pressure point is who eats the loss. Crucially, in 2024 payment users already bore ~85% of credit-transfer losses (vs ~38% of card losses) across the EEA (EBA-ECB) — the ruling attacks exactly that user-borne share. **Why now:** CJEU C-70/25 (judgment 15 Oct 2026) interprets PSD2 Arts. 73/74 to require a bank to refund an *unauthorised* payment by end of the next business day even where it alleges the customer's gross negligence; the bank must refund first and claw back later, bearing the burden of proving negligence in court. This front-runs PSD3/PSR, which already shifts the burden of proof onto the PSP and (PSR Art. 59) narrows the authorised/unauthorised distinction in impersonation fraud.

**Competitive landscape.** The KPIs that matter here are not company multiples but liability KPIs: reimbursement rate, user-vs-PSP loss split, and cost-of-fraud as a share of transaction value. "Players" are the loss-bearers and the vendors selling them a way out: (a) banks/PSPs now facing earlier, larger refund outflows; (b) fraud-prevention fintechs that monetise the compliance squeeze — in-base comps include [[Experian acquires KYC360 to boost fraud and financial crime solutions in the UK]] (Oct 2025, consolidation into fincrime tooling), [[Moniepoint partners tell.money on UK Confirmation of Payee]] (May 2026, VoP/CoP rails) and scam-detection moves like [[Starling Bank launches AI tool for customers to spot purchase scams]]. Basis of competition for vendors: detection accuracy + regulatory coverage (VoP/CoP, real-time monitoring), not price. Recent regime moves: PSR mandatory reimbursement (UK) live since Oct 2024 — in its first year banks reimbursed 88% of covered-claim value (£173m); EU-wide VoP mandatory from Oct 2025. Position: the ruling tilts the field decisively toward consumers and toward fraud-prevention vendors (demand tailwind), and against banks/PSPs that previously used "gross negligence" as a refund shield. [[Revolut tops UK bank fraud complaints for third year]] flags which issuers are most exposed.

**Comps & multiples.** No company valuation/round/metrics in this news → trading multiples not applicable; "no data" by design. The relevant sizing is the fraud-prevention software TAM, where estimates diverge widely by scope: 2025 market cited at $17.6bn, $19.45bn, $24.8bn and up to $43.4bn across vendors, with CAGRs of ~10–20% (per multiple secondary market-research firms — treat as indicative, not verified; wide dispersion signals weak comparability). Arithmetic not computable (no consistent numerator/denominator). Internal comps above are qualitative, not valuation comps.

**Risk flags.**
1. **Bank/PSP cash-flow & liability drag (regulation).** "Refund-first, prove-later" forces banks to advance funds before adjudicating fault; the burden of proving gross negligence now sits with the bank and must be won in court — second-order effect: higher provisioning, slower recovery, and incentive to over-reimburse to avoid litigation cost. Exposure concentrates in high-volume neobanks/PSPs (see Revolut complaint note).
2. **Moral-hazard / fraud-cost inflation.** Guaranteed fast refunds without strong prevention can raise claim volumes (UK unauthorised-fraud *cases* rose 11% to 3.81m in 2025 even as value fell) — if refund mandates outpace detection, scheme-wide fraud losses and mule activity can climb, pushing cost back into fees/interchange.
3. **Scope ambiguity → legal risk.** Ruling covers *unauthorised* payments under PSD2 Arts. 73/74; APP/impersonation ("authorised" but deceived) sits in a separate, evolving PSR Art. 59 track — misclassification risk between the two regimes creates litigation and reserving uncertainty for PSPs operating cross-border.

**What this changes (idea-lens).** This is a structural re-rating of consumer-fraud liability across the EU single market: the loss that users bore (~85% of credit-transfer fraud) is being pushed back onto PSPs, making fraud-*prevention* spend a defensive necessity rather than a cost center — a demand tailwind for VoP/CoP, real-time monitoring and KYB/fincrime vendors `(analysis)`. Falsifiable thesis: EU PSP fraud-prevention tooling spend accelerates into 2027 as banks internalise refund-first exposure; trigger/catalyst = PSD3/PSR final text + national transpositions; what breaks the thesis = PSR carve-outs that re-widen the gross-negligence defence or shift APP losses back toward users. `(hypothesis)`

Sources: https://curia.europa.eu/site/upload/docs/application/pdf/2026-10/cp260147en.pdf · https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr251215~e133d9d683.en.html · https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds · https://www.mondaq.com/white-collar-crime-anti-corruption-fraud/1745300/psd3-and-the-psr-rewriting-fraud-liability-in-eu-payments-law · https://www.grandviewresearch.com/industry-analysis/fraud-detection-prevention-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
