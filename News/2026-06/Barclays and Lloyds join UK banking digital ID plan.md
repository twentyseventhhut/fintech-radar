---
title: "Barclays and Lloyds join UK banking digital ID plan"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/barclays
  - company/lloyds
  - industry/banking
  - industry/regtech
  - region/uk
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/b0ad89d2
  - https://www.futureofbanking.info/r/f2a1b1f0
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Future of Banking"
story_id: s453ec627
month: 2026-06
enriched: true
importance: 3
---

# Barclays and Lloyds join UK banking digital ID plan

> [!info] 2026-06-26 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Future of Banking

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 Barclays and Lloyds join banking sector plan for digital ID. Led by UK Finance, the initiative aims to make transactions faster and more secure while helping reduce fraud, with a live pilot planned in the coming months. Continue reading

[Future of Banking] 🇬🇧 Barclays and Lloyds join banking sector plan for digital ID. Led by UK Finance, the initiative aims to make transactions faster and more secure while helping reduce fraud, with a live pilot planned in the coming months. Continue reading

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/b0ad89d2>
- <https://www.futureofbanking.info/r/f2a1b1f0>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 25–26 June 2026, UK Finance announced that six major lenders — Barclays, HSBC, Lloyds Banking Group, Nationwide Building Society, NatWest Group and Santander — are jointly developing a voluntary, financial-services-led **digital verification service**. The aggregated digest framing ("Barclays and Lloyds join banking sector plan for digital ID") is accurate but narrow: the participant list is six firms, not two, and the project is industry-coordinated by UK Finance rather than a Barclays/Lloyds initiative. The scheme has completed proof-of-concept work (using synthetic data to test technical, legal and operational requirements) and the next stage is a **live pilot in a controlled real-world environment "in the coming months."**

**[1] How it works.** A customer would verify personal details digitally through their existing banking app; the bank, leveraging its trusted KYC relationship, would then share specific verified attributes — name, age, address — securely with a third party so the customer can complete a transaction or access a service, without handing over physical documents (passport, utility bills). It is **voluntary and consent-based**: the customer controls what is shared and when. Technical design and delivery are led by **Select ID**, a certified Orchestration Service Provider (OSP) under the UK Digital Verification Services (DVS) Trust Framework (holds ISO/IEC 27001). Stated use cases include property transactions, online purchases and opening online accounts.

**[2] Why it matters / strategic logic.** Banks already perform the most expensive identity step (regulated onboarding KYC). A reusable, bank-issued attribute-sharing rail lets them monetise/leverage that trust anchor as relying parties pay for verified attributes — reducing fraud, speeding transactions, and pre-empting fintech/big-tech ID wallets and the government's own GOV.UK One Login / GOV.UK Wallet from owning the identity layer. CFIT estimated a digital company-ID alone could save the UK financial sector ~£1.7bn, indicating the prize banks are chasing.

**[3] Context — adjacent prior coverage (internal):**
- [[Visa white paper links digital ID wallets to payments]] — commercial digital ID wallets converging with payments; same "verified attributes as a service" thesis (2026-03).
- [[iDenfy adds Smart-ID to identity verification for Baltic markets]] — note explicitly lists "UK OneID" among bank-grade electronic-identity systems; signals an existing UK bank-ID verification market this scheme would consolidate (2026-06).
- [[Banca Transilvania and BPC deliver Romania's EU digital identity payment]] — EU eIDAS/EUDI-wallet model of bank-rail identity (2025-11); useful contrast to the UK's separate, private-sector DVS path.
- [[Lloyds Banking Group to acquire digital wallet Curve]] — Lloyds' broader wallet/identity ambitions (2025-11).

**[4] Open / unresolved.** No named launch date, no go-live commitment (POC + pilot only), no commercial/pricing model, no list of relying-party adopters, and explicitly **separate from the government's digital ID programme** — leaving an unresolved question of duplication/interoperability with GOV.UK One Login and the planned mandatory government Digital ID. Property-sector bodies have reportedly cooled on the parallel government scheme, a demand-side risk.

Sources:
- UK Finance press release — https://www.ukfinance.org.uk/news-and-insight/press-release/banks-and-uk-finance-working-voluntary-digital-verification-service
- Finextra — https://www.finextra.com/newsarticle/47990/top-uk-banks-go-to-work-on-digital-verification-service
- Open Banking Expo — https://www.openbankingexpo.com/news/uk-finance-backs-major-banks-to-launch-digital-verification-service/
- Mortgage Solutions (property use case) — https://www.mortgagesolutions.co.uk/mortgage-news/2026/06/25/uk-finance-and-banks-work-on-digital-verification-for-possible-property-transaction-use/
- City AM — https://www.cityam.com/barclays-and-lloyds-join-banking-sector-plan-for-digital-id/
- Biometric Update (CFIT £1.7bn) — https://www.biometricupdate.com/202606/digital-company-id-could-save-uk-financial-sector-1-7b-cfit
- Biometric Update (property sector backs away) — https://www.biometricupdate.com/202606/property-sector-backs-away-from-uk-digital-id-scheme
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. **Stage inflation.** The project has only completed a *synthetic-data proof of concept*; the pilot is merely "scheduled in the coming months." Is the "join banking sector plan" headline overstating maturity for what is still pre-pilot?
2. **Participant count.** The digest names only Barclays and Lloyds, but the scheme has six firms (incl. HSBC, NatWest, Nationwide, Santander). Does over-indexing on two names misrepresent who is driving this?
3. **Commercial model unknown.** Who pays — relying parties, customers, or banks? Without a pricing/revenue model, is this a viable business or a defensive standards play?
4. **Government overlap.** It is explicitly separate from GOV.UK One Login / the government Digital ID. Why a parallel private scheme, and does fragmentation (two competing UK identity rails) help or hurt adoption?
5. **Interoperability.** Is the bank scheme interoperable with DIATF/DVS-certified providers and the GOV.UK Wallet, or does it risk a walled garden of bank-only attributes?
6. **Relying-party demand.** No relying parties named. Property-sector bodies have reportedly cooled on the government scheme — what evidence is there of actual third-party demand to consume bank-verified attributes?
7. **Competition / data concentration.** Six incumbents controlling the identity layer — does this entrench Big-Bank dominance and raise CMA/competition concerns versus fintech ID providers (OneID, Yoti, Experian)?
8. **Liability.** If a bank-asserted attribute is wrong or a fraud slips through, who bears liability — issuing bank, Select ID (OSP), or relying party? Unresolved.
9. **Single point of failure / privacy.** Routing identity through Select ID's orchestration platform concentrates sensitive PII; what is the breach blast radius and data-minimisation guarantee beyond "consent"?
10. **Coverage gaps.** Reliance on existing bank relationships excludes the unbanked/thin-file population — does it widen the financial-inclusion gap that government Digital ID aims to close?
11. **AML/KYC legal standing.** Government MLR guidance on digital ID was still pending at announcement. Can relying parties legally rely on these attributes for regulated checks yet?
12. **Vendor lock / single supplier.** Select ID is the sole named technical partner. Concentration and switching-cost risk if it underperforms or is acquired.
13. **Timeline credibility.** "Coming months" for a live pilot is vague; six-bank coordination + regulatory alignment historically slips. What is the realistic go-live horizon?
14. **Differentiation.** UK OneID, Smart-ID, BankID already provide bank-electronic-ID verification (see iDenfy note). What does this add beyond rebranding existing capability under UK Finance?
15. **Confirmation bias of sources.** Most detail traces to a single UK Finance press release amplified by trade press — limited independent scrutiny; treat upbeat framing skeptically.

**Importance: 3/5** — Strategically significant (six systemic UK lenders + UK Finance building a reusable identity rail that could reshape KYC economics and pre-empt government/big-tech ID), and it directly touches fraud, payments and open-banking adjacencies. But it is materially discounted: still pre-pilot (synthetic-data POC only), no launch date, no commercial model, no named relying parties, and explicitly parallel to — not integrated with — the government scheme. High potential, low present certainty.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-26]] (2026-06-26).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector context.** The story sits in the **reusable digital identity / verified-attribute-sharing** segment intersecting RegTech, fraud prevention, open banking and payments. The global thesis — captured in [[Visa white paper links digital ID wallets to payments]] — is that verified identity attributes become a payable, reusable service rather than a per-transaction document check. The UK's distinctive feature here is **incumbent-bank issuance**: rather than a fintech or government owning the wallet, six systemic lenders (Barclays, HSBC, Lloyds, Nationwide, NatWest, Santander) coordinate through UK Finance to leverage their existing KYC trust anchor, with Select ID as the certified Orchestration Service Provider under the UK DVS Trust Framework (DIATF lineage). CFIT has put the prize at roughly £1.7bn of annual savings for the UK financial sector from digital company ID alone.

**Comparables / competitive map.**
- **Government rail (substitute/overlap):** GOV.UK One Login + GOV.UK Wallet and the planned mandatory government Digital ID — explicitly *separate* from this scheme; the key strategic tension.
- **Bank-ID models abroad (precedent):** BankID (Sweden/Norway), Smart-ID, and UK OneID — see [[iDenfy adds Smart-ID to identity verification for Baltic markets]], which lists UK OneID as an existing bank-electronic-ID rail. These prove demand but also show the UK is *late* to bank-issued reusable ID.
- **EU eIDAS / EUDI wallet (regulatory contrast):** [[Banca Transilvania and BPC deliver Romania's EU digital identity payment]] — a state-standardised wallet route, opposite the UK's private-sector path.
- **Pure-play IDV / KYC vendors (potential disintermediation targets or partners):** OneID, Yoti, Experian (see [[Experian bolsters verification capabilities with Konfir acquisition]]), Alloy, IDnow, Regula/Indicio, ID.me ([[ID.me hits $2 billion valuation after raising $340 million]]) — a well-funded incumbent vendor field this bank scheme could either commoditise or co-opt.
- **Adjacent UK open-banking rails:** [[UK Payments Initiative launches new open banking scheme]] — same incumbent-coordination pattern, signalling a broader push to own shared UK infrastructure.

**Risk flags (5):**
1. **Execution/stage risk** — synthetic-data POC only; live pilot unscheduled beyond "coming months"; six-party coordination historically slips.
2. **Regulatory/legal-standing risk** — government MLR guidance on digital-ID use for AML/KYC still pending; relying parties' ability to lawfully rely on attributes unconfirmed.
3. **Competition/concentration risk** — six incumbents owning the identity layer invites CMA scrutiny and threatens fintech IDV players; data concentrated at Select ID is a single point of failure (privacy/breach blast radius).
4. **Adoption/demand risk** — no named relying parties; property-sector bodies have reportedly cooled on the parallel government scheme; no commercial/pricing model disclosed.
5. **Fragmentation/interoperability risk** — running parallel to GOV.UK One Login risks two competing UK identity rails, duplicated cost, and user confusion unless interoperability is engineered.

**Net read.** Credible, strategically important infrastructure play by systemic UK banks, but early-stage and commercially unproven; value hinges on the pilot converting to a live service with real relying-party demand and clean coexistence with the government rail.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
