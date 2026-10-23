---
title: "Ondato and Trinsic expand identity verification amid EUDI shift"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/ondato
  - company/trinsic
  - industry/regtech
  - region/europe
  - type/partnership
sources:
  - https://ondato.com/press/ondato-and-trinsic-expand-digital-identity-verification-amid-eudi-transition
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s59fabf58
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Ondato and Trinsic expand identity verification amid EUDI shift

> [!info] 2026-10-23 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇪🇺 Ondato and Trinsic expand digital identity verification amid EUDI transition. Trinsic will provide the infrastructure to verify customers using EUDI wallets and national digital IDs, integrating the capability into Ondato's existing identity verification and risk management platform.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://ondato.com/press/ondato-and-trinsic-expand-digital-identity-verification-amid-eudi-transition>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ondato and Trinsic expand identity verification amid EUDI shift
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On 21–22 Oct 2026, KYC/AML vendor Ondato announced it is integrating Trinsic's digital-identity "gateway" into its compliance platform so clients can (in future) accept EU Digital Identity (EUDI) wallets and national eIDs (e.g. Smart-ID, France/Italy/Denmark/Austria schemes) alongside Ondato's existing document checks and fraud monitoring. Trinsic is the *infrastructure provider*; Ondato is the distribution/compliance front-end.

**De-PR'd reality:** This is an **announced integration, not a live, adopted capability.** Ondato's own framing ("building out capabilities ahead of that shift", "accept wallets *as they launch*") concedes the dependency: EUDI wallets are mostly not yet in production. No pricing, no client names, no go-live date, no volume. The press line "biggest change in a generation to how Europeans prove who they are" (CEO Liudas Kanapienis) is forward-looking marketing, not a shipped product milestone.

**Why structured this way:** Ondato is a small, bootstrapped-ish vendor (~$8.8M ARR, ~80 staff, ~$26.4M last valuation per getlatka/PitchBook — *estimates, analysis*) that cannot build 27 national eID connectors itself. Partnering with Trinsic's gateway is a classic buy-vs-build: outsource the regulatory plumbing, keep the customer relationship. The announcement is timed to the eIDAS 2.0 calendar (see [4]) to position Ondato as "EUDI-ready" before competitors do — i.e. it is **a marketing claim to land ahead of a regulatory deadline**, not evidence of traction.

**Unverified number flag:** one secondary aggregation cited "1.9 billion pre-verified profiles" and "50+ national eID frameworks" for Trinsic; neither primary source (fintech.global, biometricupdate) confirms this and it conflicts with Trinsic's own "~60M pre-verified users" figure elsewhere — treat the billion figure as **unverified PR inflation**.

## [1] Competitors / peers
Trinsic is quietly becoming the **shared pipe** behind multiple IDV vendors, not Ondato's exclusive edge:
- **Jumio** integrated Trinsic in **June 2026** to accept mDLs, eIDs, EUDI credentials across 60+ countries (biometricupdate).
- **Veratad** chose Trinsic (Jan 2026) to expand its IDMax reusable-ID network.
- **authID** partnered Trinsic for biometric-backed digital ID.
Direct IDV incumbents: **Entrust IDV (ex-Onfido** — Entrust closed the acquisition Apr 2024 and retired the Onfido brand), **Jumio, Veriff** (docs in 200+ countries), **iProov, Socure, Sumsub, Persona, Trulioo**. See priors: [[Socure and Docusign embed identity verification in signing]], [[Experian acquires KYC360 to boost fraud and financial crime solutions in the UK]], [[Trulioo posts 134% jump in US verification volume]], [[Persona launches Persona Connect at Money20 20]], [[IDenfy launches AML screening tech]], [[MagicCube raises $10 million to expand into biometrics and IDV]].

**Position: parity / catching-up, not ahead.** Because Jumio (a far larger player) already shipped the *same* Trinsic-EUDI integration in June 2026, Ondato is ~4 months behind a bigger rival **on the identical plumbing**. **Why the lay of the land is this way:** EUDI acceptance is becoming a compliance checkbox, not a differentiator — once the orchestration layer (Trinsic) is shared, the "EUDI-ready" label commoditizes. Second-order: the margin pools at the **gateway/orchestration layer (Trinsic)**, not at the many front-end IDV vendors reselling it.

## [2] Company history / fit
Ondato (founded 2018, Lithuania; UK presence) is a single-vendor KYC/KYB/AML/KYT compliance platform serving regulated EU businesses. Recent moves: **AML Ranger** (AI AML-checks assistant, Oct 2025). Adding EUDI acceptance **fits logically** — it is adjacent to its existing onboarding/verification line and defends its EU regulated-business base against larger rivals. **Why it acts this way:** as a sub-$10M-ARR vendor in a market dominated by Entrust/Jumio/Veriff, Ondato must look "complete" and standards-aligned to retain EU clients facing the 2027 mandate; partnering (not building) is the only economically rational path for its scale.

## [3] Novelty / value-add / traction
**Novelty: low.** The capability (accept EUDI/national eIDs via Trinsic) already exists in the market via Jumio (Jun 2026) and others; Ondato is replicating it. The genuine value-add for Ondato's *own* clients is real but narrow: one-platform EUDI acceptance without separate integration — convenience, not innovation.
**Traction: none disclosed** — no clients, volumes, conversion, or go-live. "Announced", firmly not "adopted".
**Where the margin sits (analysis):** Trinsic captures the recurring value as the acceptance network/gateway; Ondato is a reseller/front-end. If EUDI acceptance becomes table-stakes, Ondato's moat is its compliance workflow + client base, not the EUDI feature itself — which any competitor can bolt on via the same Trinsic pipe. That is what breaks the "differentiation" story.

## [4] What's next / market sentiment
Regulatory backdrop (eIDAS 2.0, Reg (EU) 2024/1183, in force 20 May 2024): every member state must offer ≥1 EUDI wallet by **24 Dec 2026**; **regulated businesses (banking, healthcare, telecoms, etc.) must accept the wallet on user request by 24 Dec 2027** (micro/small enterprises exempt). As of Oct 2026 **no wallet is yet fully certified** under the EU scheme and the Commission has doubted all 27 states will meet the Dec-2026 deadline (Italy IT-Wallet, Denmark AltID most advanced; Germany d-you launches 2 Jan 2027). Related corpus signal: [[Bhutan integrates national digital ID with Ethereum]].
**Why the market goes this way:** the 2027 acceptance mandate forces a wave of "EUDI-ready" vendor announcements through 2026–27 — this Ondato note is one of many. **Counterintuitive second-order:** the hard part is not vendor readiness but **wallet availability + certification on the issuer side**, which is slipping; so "EUDI-ready" announcements in 2026 are largely insurance against a deadline whose supply side is behind schedule — real adoption volume is a 2027+ story, gated by states, not by IDV vendors.

## Sources
- Ondato press (primary): https://ondato.com/press/ondato-and-trinsic-expand-digital-identity-verification-amid-eudi-transition/
- fintech.global (21 Oct 2026): https://fintech.global/2026/10/21/ondato-taps-trinsic-as-eu-digital-identity-wallets-loom/
- biometricupdate (Oct 2026): https://www.biometricupdate.com/202610/ondato-partners-with-trinsic-for-eudi-wallet-verification-as-hopae-expands-testing
- Jumio-Trinsic (Jun 2026): https://www.biometricupdate.com/202606/jumio-integrates-trinsic-to-expand-reach-in-growing-idv-market
- Veratad-Trinsic: https://www.biometricupdate.com/202601/veratad-trinsic-partnership-expands-idmax-reusable-digital-id-network
- eIDAS 2.0 / EUDI timeline: https://www.gataca.io/resources/blog/eIDAS2-timeline/ ; https://en.wikipedia.org/wiki/EU_Digital_Identity_Wallet
- Ondato financials (estimates): https://getlatka.com/companies/ondato.com ; https://pitchbook.com/profiles/company/234258-04
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Live or announced?** Announced only. Ondato says "accept wallets *as they launch*"; no go-live date, no client. → not adoption.
2. **Is it new?** No — Jumio shipped the same Trinsic-powered EUDI/mDL acceptance in Jun 2026, ~4 months earlier; Veratad/authID also use Trinsic. Ondato is replicating, not pioneering.
3. **Who captures the margin?** Trinsic (the acceptance gateway) captures the recurring value; Ondato is a front-end reseller. The feature commoditizes across IDV vendors sharing the same pipe.
4. **Any traction numbers?** None disclosed — no clients, volumes, conversion, revenue impact. Open.
5. **Is the "1.9B profiles / 50 frameworks" figure real?** Unverified; absent from both primary sources and conflicts with Trinsic's own ~60M-user figure. Treat as PR inflation.
6. **What's Ondato's actual scale?** ~$8.8M ARR, ~80 staff, ~$26.4M valuation (third-party estimates) — too small to build 27 eID connectors itself, hence the partnership. Verifies the buy-vs-build read.
7. **Does EUDI acceptance differentiate Ondato?** No — once the 2027 mandate hits it's table-stakes; the moat is Ondato's compliance workflow + EU client base, not the EUDI feature.
8. **Is the deadline even firm?** As of Oct 2026 no wallet is EU-certified; Commission doubts all 27 states hit Dec-2026. Supply side (wallet issuance) is slipping — real volume is 2027+.
9. **Exclusivity?** No evidence Trinsic is exclusive to Ondato; it is explicitly multi-vendor (Jumio, Veratad, authID). So no defensive lock-in.
10. **Who needs whom more?** Ondato needs Trinsic more (it can't build the gateway); Trinsic treats Ondato as one of many distribution channels.
11. **Fraud liability / economics — who's silent?** Both silent on pricing, liability split for wallet-based verification failures, and per-check economics. Open.
12. **Does it fit Ondato's trajectory?** Yes — adjacent to KYC/AML onboarding, follows AML Ranger (Oct 2025); logical defensive move for an EU-regulated-business base.
13. **Second-order risk?** EUDI commoditizes IDV document-checking over time (wallets carry pre-verified credentials), which could erode Ondato's core document-verification revenue even as it resells acceptance. Structural, long-run.
14. **Is "amid EUDI shift" overstated?** The shift is real regulation but adoption is gated by states, not vendors; the announcement is deadline-driven positioning, not a demand signal.
15. **Duplicate?** No prior corpus note covers this specific Ondato-Trinsic deal; the nearest priors are adjacent IDV items, not the same event → fresh.

Importance: 2/5 — Real regulatory tailwind (eIDAS 2.0 2027 mandate) and a logical fit for Ondato, but this is an *announced*, non-exclusive integration of commodity plumbing (Trinsic) that a larger rival (Jumio) already shipped months earlier, with zero disclosed traction. Margin accrues to the gateway, not to Ondato. Notable as a signpost of the EUDI readiness wave, not as a standalone material event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Digital identity verification / IDV is a ~$14–17bn market in 2026 depending on source (e.g. ~$17.3bn at ~17% CAGR, or ~$14.1bn — multiple secondary trackers, figures diverge widely so treat as order-of-magnitude, not precise), with the narrower KYC-specific slice put at ~$6.0bn in 2026 (per aggregated market-research trackers via WebSearch, as of Oct 2026 — all are paid-report summaries, so `[UNSOURCED]` at the primary level). Structure: fragmented — dozens of IDV/KYC vendors (document + biometric + AML screening) competing on verification accuracy, coverage breadth and compliance depth; barriers are regulatory (per-market AML/KYC licensing), data/document coverage and fraud-model quality rather than capital. **Why now:** the catalyst is explicit and dated — eIDAS 2.0 (Reg. EU 2024/1183, in force 20 May 2024) requires every EU member state to make an EUDI Wallet operational by **24 Dec 2026**, and designated private sectors (banking, telecom, energy, transport, healthcare) + large platforms must *accept* it by **24 Dec 2027**. Member-state readiness is uneven (fewer than a third at benchmark), so incumbents face a hard compliance clock while the acceptance layer is still being built — exactly the gap this Ondato–Trinsic deal targets.

**Competitive landscape.** Sector KPIs: verification volume/transactions, auto-approval (pass) rate, fraud catch rate, country/document coverage, and for infra players the size of the reusable-ID network (credentials/wallets reachable). Key players: full-stack IDV/KYC vendors — Veriff, Sumsub, Jumio, Entrust (post-Onfido), Trulioo, Socure, Experian (post-KYC360) — vs the emerging *reusable / orchestration layer*: Trinsic, Persona Connect, Plaid ("verify once, verify everywhere"). Basis of competition is shifting from one-off document checks to **acceptance of pre-verified credentials** (eID apps, mDLs, EUDI wallets). Recent moves: Trinsic divested its SSI/ecosystem assets to Dentity to focus on its Identity Acceptance Network (2024–25), and Digidentity added 25M identities to that network (Oct 2024); Persona launched Persona Connect at Money20/20 (Oct 2025) as reusable KYC "rails"; Trulioo reported +134% US verification volume and >20M US transactions in 2025. Position: Ondato is a mid-size compliance/KYC platform (Lithuania/London, founded 2016, ~150 clients across 24 countries) — a **niche** EU regtech, not a scale incumbent; the moat here is the *combination* — Ondato's existing AML/risk platform + client base plus Trinsic's acceptance-network coverage. Neither party alone has a wide EUDI moat; this is a distribution-plus-rails play `(analysis)`.

**Comps & multiples.** Internal comps (same IDV/KYC subvertical, in-base):
- [[Persona launches Persona Connect at Money20 20]] — closest analog: reusable verified-identity *rails* (same thesis as Trinsic's layer).
- [[Trulioo posts 134% jump in US verification volume]] — scale/volume benchmark for the incumbent IDV model.
- [[Experian acquires KYC360 to boost fraud and financial crime solutions in the UK]] — consolidation of KYC/AML into a data incumbent.
- [[Socure and Docusign embed identity verification in signing]] — IDV-embedded-in-workflow distribution precedent.

External comps (round valuations, NOT market caps — show arithmetic where possible):
- **Ondato**: last disclosed ~€6.6M raised (through 2022); Dealroom estimated enterprise value ~$20M — stale/secondary, so no current multiple → "no data".
- **Trinsic**: ~$9.4M total raised since 2019 ($8.5M seed, 2022); no valuation disclosed → "no data". Both protagonists are small/early — no revenue disclosed, so EV/Revenue not computable.
- **Veriff**: ~$1.5bn valuation at ~$110M ARR (2025) → implied **EV/ARR ≈ $1.5bn / $0.11bn ≈ 13.6x** (round valuation, not market cap; rich but within hyper-growth IDV norms).
- **Socure**: ~$5.2bn valuation on a $156M growth round (Aug 2026); ARR not public → multiple = `[UNSOURCED]`.
- **Onfido**: acquired by Entrust ~$650M (closed Apr 2024) — M&A reference point, no public multiple.
Distribution not computed (only one clean valuation/ARR pair). Qualitative read: the *scale* IDV names (Veriff, Socure) carry billion-dollar valuations; the two deal parties are an order of magnitude smaller — this is a capability partnership, not a valuation event.

**Risk flags.**
1. **Disintermediation / margin captured one layer up** — if EUDI wallets + national eIDs become the universal acceptance layer, the economic value may accrue to the acceptance-network/orchestration owner (Trinsic-type, or the member-state wallet itself), compressing standalone IDV vendors like Ondato into thin integration margin. Ondato is *consuming* Trinsic's rails, not owning them.
2. **Regulatory execution / timeline risk** — the whole thesis rides on the 24 Dec 2026 member-state deadline and 2027 private-sector acceptance; with <1/3 of states at readiness, slippage or fragmented per-state wallet implementations could strand the integration and delay revenue.
3. **"Announced vs live" / scale asymmetry** — this is a partnership announcement (de-PR: no disclosed volumes, pricing, or client commitments), and both firms are sub-scale vs Veriff/Socure/Entrust; execution against far larger, better-funded incumbents racing to the same EUDI acceptance layer is unproven.

**What this changes (idea-lens).** `(analysis)` This is an early marker of IDV's shift from *re-verifying* users to *accepting* portable credentials — the EUDI deadline turns reusable-identity rails from optional to near-mandatory, favoring acceptance-network players (Trinsic, Persona, Plaid) and the vendors who integrate them first. Falsifiable thesis: by end-2027 the value in EU IDV re-rates toward acceptance/orchestration layers rather than per-check document vendors. Trigger to watch: disclosed EUDI-wallet verification volumes or a scale incumbent (Entrust/Veriff) acquiring an acceptance-network player. What breaks it: EUDI member-state rollout slips materially past Dec 2026, keeping classic document-based IDV the default.

Sources: https://ondato.com/press/ondato-and-trinsic-expand-digital-identity-verification-amid-eudi-transition · https://www.fortunebusinessinsights.com/identity-verification-market-106468 · https://www.eadtrust.eu/en/blog/december-2026-deadline-eudi-wallet/ · https://tech.eu/2020/12/31/ondato-seed-funding/ · https://trinsic.id/trinsic-raises-8-5m-for-decentralized-identity-platform/ · https://www.trinsic.id/trinsic-decentralized-identity-assets-acquired-by-dentity-to-accelerate-digital-id-adoption/ · https://www.fintechfutures.com/biometrics-id-verification/entrust-in-exclusive-talks-to-acquire-id-verification-solutions-provider-onfido
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
