---
title: "Extend introduces Verify document fraud detection API"
date: 2026-10-21
retrieved: 2026-10-21
tags:
  - company/extend
  - industry/fraud-risk
  - industry/infrastructure
  - region/us
  - type/product
sources:
  - https://www.businesswire.com/news/home/20261019356400/en/Extend-Introduces-Verify-a-Document-Fraud-Detection-API-that-Builds-Trust-into-Document-Pipelines
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s3c76977d
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Extend introduces Verify document fraud detection API

> [!info] 2026-10-21 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 2. 🇺🇸 Extend introduces Verify, a document fraud detection API. The new API is designed to build trust into document pipelines. Verify targets fraud within the documents those pipelines handle. Read more

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261019356400/en/Extend-Introduces-Verify-a-Document-Fraud-Detection-API-that-Builds-Trust-into-Document-Pipelines>

## Контекст

<!-- enrichment:context -->
### [0] What happened
On 2026-10-19, at Money20/20 USA, **Extend AI** (extend.ai; NOT the virtual-card fintech paywithextend.com — see [4]) launched **Verify**, a document-fraud-detection API. It is pitched as the first document-fraud API built specifically for developers and AI agents, flagging tampered or AI-generated documents before downstream systems act on them. (BusinessWire/Help Net Security, 2026-10-19/20.)

### [1] What Verify actually does
Three fraud classes, per Extend's own materials:
- **Fully AI-generated synthetic documents** — flags signs of generative fabrication.
- **AI-edited genuine documents** — detects field-level alterations "as small as a single character."
- **Post-signature tampering** — examines digital-signature integrity and revision history.
Self-reported benchmark: **96.3% of fraudulent docs detected at a 4.0% false-positive rate** (vendor-reported, not independently verified). Usable standalone via API or bolted onto Extend's existing parse/split/extract pipelines.

### [2] Who Extend AI is (the real subject)
Extend AI — NYC, founded **2023** by **Kushal Byatnal (CEO)** and **Eli Badgio (CTO)**. Document-processing infrastructure for AI agents / production pipelines. Raised **$17M** seed + Series A (reported ~2025-06), led by **Innovation Endeavors**, with Y Combinator, Homebrew, Character, and angels Scott Belsky and Guillermo Rauch. Verify is an adjacent product extending its core document-processing stack into integrity/fraud.

### [3] Competitive landscape
Verify enters a crowded document-forensics market: **Resistant AI** ($25M Series B, 2025-10 — see [[Resistant AI raises $25M Series B against financial crime]]; runs 500+ checks/doc), **Inscribe** (SF, 2017; added AI-generated-doc detector in 2025), **Ocrolus** ("Detect" tampering layer on extraction), plus Snappt, Fortiro, Klippa. All publish self-reported accuracy (Snappt 99.8%, Resistant AI 99.2–99.92%, Ocrolus 90%+); Verify's 96.3%/4.0%-FPR sits mid-pack and is likewise unaudited. Verify's differentiation is developer/agent-first API packaging and native integration with Extend's own parsing pipeline, not a forensics breakthrough.

### [4] CRITICAL — entity collision
The note carries tag `company/extend` and sits alongside internal notes [[Extend raises $20M and hires PayPal veteran as CFO]], [[Mastercard partners Extend on spend management for issuing banks]], [[Extend and PNC launch virtual card platform for commercial clients]]. Those are a DIFFERENT company: **paywithextend.com** (virtual cards / spend management, CEO Andrew Jamison, founded 2017, ~$88.8M raised). This Verify note is **Extend AI (extend.ai, Byatnal)**. There is no evidence the two are related. Internal cross-links / company tagging for this note are mis-grouped and should NOT be treated as the same company.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
- **Entity integrity:** Is this Extend AI (extend.ai, Byatnal/Badgio, doc-processing, 2023) — NOT the virtual-card Extend (paywithextend.com, Jamison, 2017)? CONFIRMED collision; `company/extend` tag and sibling notes conflate two unrelated firms. Do not inherit funding/partnership facts across them.
- **Accuracy claim:** 96.3% detection at 4.0% FPR is vendor-self-reported on an undisclosed benchmark; no independent validation, no dataset composition disclosed. Competitors quote 90–99.9% on equally unaudited sets — numbers are not comparable.
- **"World's first" framing:** "First document-fraud API for developers/agents" is a marketing qualifier; Resistant AI, Inscribe, Ocrolus already offer API-based tampering/synthetic-doc detection. Novelty is packaging/positioning, not capability.
- **Traction gap:** No customers, pricing, volume, or GA/beta status disclosed. Announcement-stage product at a conference; adoption unproven.
- **Defensibility:** Fraud-detection is an arms race vs improving generative models; a single-char-edit detector degrades as models improve. Recurring model-update cost not addressed.
- **Scale of company:** ~$17M-raised, 2023 seed/Series-A startup entering a field with better-funded incumbents (Resistant AI $25M+ B). Distribution is the open question.

### Importance: 2/5
New-product launch from a small (~$17M) Series-A startup into an already-served document-fraud market, with only self-reported accuracy and no disclosed traction. Noteworthy mainly as an AI-agent-era fraud-tooling signal and because the note is mis-tagged against an unrelated same-name fintech. Low standalone market-moving weight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Entity note:** This "Extend" is Extend (CrowdView Inc.), the NYC AI document-processing startup (extend.ai), NOT Extend the extended-warranty/product-protection firm (extend.com) nor the Extend virtual-card/spend-management fintech (paywithextend.com). Extend was founded in 2023 (Eli Badgio, Kushal Byatnal), backed by Innovation Endeavors, Y Combinator and Character VC, having raised ~$17M across seed + Series A (2025). Its document-processing cloud converts complex PDFs/scans into validated data at >95% accuracy; customers include Brex, Square, Checkr and Flatiron Health. Verify extends that pipeline from extraction into integrity-checking.

**Sector context — document fraud / AI-fraud infrastructure.** Verify lands in the document-fraud-detection segment, a fast-growing slice of the broader fraud-detection stack. Estimates put the document fraud detection market near $3.58B in 2026, growing ~20.7% CAGR to ~$9.16B by 2031 (Mordor Intelligence). The wider fraud detection & prevention market is far larger (~$35.7B in 2026, MarketsandMarkets). The specific tailwind is AI-generated document fraud, reportedly scaling "from virtually zero to an $8.9B problem in ~18 months," with ~72% of business leaders expecting AI-generated fraud/deepfakes to be a major 2026 challenge. Adjacent identity-verification software (~$16–17B in 2026, ~15–16% CAGR) overlaps on buyers but Verify is positioned below IDV/KYC: it inspects the document artifact (tampering, AI edits, post-signature changes) rather than the identity behind it.

**The product (grounded).** Launched 2026-10-19 at Money20/20 USA, Verify is an API that examines visual content, file structure and revision history, combining specialized models, forensic checks and agentic analysis. It flags AI-generated documents, localized AI-tampering (edits as small as a single character to an amount or account number), conventional digital editing (patched text, image overlays) and post-signature changes. It returns detected signals, risk scores, explanations and traceable evidence. Benchmark: 96.3% of fraudulent documents detected at a 4.0% false-positive rate. Framed as trust infrastructure for AI agents acting on documents (e.g. flag altered income docs before a credit decision, or a doctored invoice before payment).

**Comps / competitive set.** The document-forensics specialists most comparable to Verify are Resistant AI (forensic layer, 500+ checks on tampering/metadata/serial-fraud patterns), Inscribe (agentic, case-level cross-referencing of all docs in an application; strong in fintech lending), plus Fortiro and Attestiv. Document-heavy IDV/KYC platforms (Sumsub, Jumio, Mitek, Onfido/Entrust, Regula) are adjacent but anchored on identity rather than pure document integrity. Within the news vault, nearby comps on the fraud-infra theme: Feedzai ($75M raise at $2B+ valuation), Trulioo, Experian/KYC360, Themis/Pasabi, Thredd+Featurespace, Plaid's AI-fraud reports. Extend's wedge vs these: it already sits inside document pipelines (extraction), so Verify bolts integrity-checking onto workflows its models already read — a distribution advantage over standalone forensics vendors.

**Risk flags.**
1. **Entity/tagging risk.** The note is tagged `company/extend` and the IR key `extend` maps to a different company (extend.com, warranty/product-protection). Any IR grounding or de-dup keyed on the slug risks cross-wiring; IR skipped here as wrong-entity.
2. **Benchmark is self-reported.** 96.3% detection / 4.0% FPR comes from Extend's own "challenging benchmark" with no disclosed dataset, adversary model or third-party validation — vendor-defined benchmarks rarely transfer to production fraud distributions.
3. **Adversarial / fast-moving threat.** AI-generated fraud evolves faster than detectors; a static model that scores 96.3% today can degrade sharply as generators improve, forcing continuous retraining.
4. **Crowded, well-funded field.** Resistant AI, Inscribe, Fortiro plus IDV incumbents already sell document-tampering detection; Extend is a late, small (~$17M raised) entrant differentiating mainly via its existing document-cloud distribution.
5. **False-positive cost at scale.** A 4.0% FPR means ~1-in-25 legitimate documents flagged; in high-volume lending/payments that is meaningful manual-review load and customer friction.
6. **Scope confined to the artifact.** Verify checks document integrity, not identity, synthetic applicants or account takeover — buyers still need separate KYC/IDV, so it is a feature layer rather than a full fraud stack.

**IR grounding:** skipped — the `extend` IR entry (extend.com warranty/retail-returns firm; e.g. "Mattress Firm Launches FirmCare Powered by Extend") is a DIFFERENT entity from this note's Extend (extend.ai AI document processing). No matching IR figures to fold in.

_Sources: Extend/BusinessWire press release (2026-10-19); Help Net Security (2026-10-20); extend.ai; SiliconANGLE/BuiltInNYC on the $17M raise; Mordor Intelligence (document fraud detection market); MarketsandMarkets (fraud detection & prevention / identity verification); Klippa, Microblink, verifypdf (competitive set). Figures as reported; not independently verified._
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
No earnings/results data. This item is a product launch (Extend's "Verify" document-fraud-detection API), not an earnings event, and Extend is a privately held company with no public financial filings. The IR entry under `extend` is a different entity — Extend.com, the e-commerce product-protection / extended-warranty / shipping-protection company (Shopper Operations, Mattress Firm/Beyond partnerships), not the document-fraud-detection / document-pipeline API fintech in this note. No revenue, guidance, or results figures are available.
<!-- /enrichment:earnings_review -->
