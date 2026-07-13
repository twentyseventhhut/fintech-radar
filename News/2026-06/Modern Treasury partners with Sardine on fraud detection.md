---
title: "Modern Treasury partners with Sardine on fraud detection"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/modern-treasury
  - company/sardine
  - industry/fraud-risk
  - region/us
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/c9f49e1e
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s55730682
month: 2026-06
enriched: true
importance: 2
---

# Modern Treasury partners with Sardine on fraud detection

> [!info] 2026-06-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Modern Treasury partners with Sardine to help businesses detect fraud earlier and reduce risk at scale. By integrating Sardine’s real-time monitoring and risk infrastructure, Modern Treasury enhances its ability to help customers identify and stop fraudulent activity more effectively.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/c9f49e1e>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Modern Treasury partners with Sardine on fraud detection
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On **2026-06-24** Modern Treasury (MT) announced it is **embedding Sardine's real-time transaction-monitoring / fraud engine into its payment-operations platform**, so MT customers get fraud scoring "without an additional integration." Claimed rail coverage is the bank/instant set, not cards: **ACH, Wire, RTP, FedNow, Push-to-Card and stablecoins**, plus wallet screening and "automated risk checks within stablecoin orchestration workflows," all via MT's single API (MT/Businesswire 2026-06-24; Finextra/fintech.global 2026-06-25).

De-PR'd reality: this is an **announcement, not a launch**. No GA date, **no named launch customer, no pricing, no rollout timeline** — the language is capability/future framing ("able to help," "real-time risk infrastructure"). Treat as roadmap/distribution deal until live volume is shown.

**Why framed this way →** The PR leads with "real-time risk infrastructure" because MT's structural bet is **multi-rail money movement incl. stablecoins** (see [[Modern Treasury launches PSP for fiat and stablecoins]], [[Modern Treasury acquires stablecoin startup Beam]]). Adding a brand-name fraud engine lets MT sell "fast AND safe" on irreversible rails (ACH/wire/FedNow can't easily be clawed back), where "real-time" detection is the actual sales hook. **Second order:** the vagueness on whether this is **inline blocking (decline before send)** vs **post-hoc alerting** matters — on irreversible rails, alerting after settlement captures far less value than the PR implies (analysis).

## [1] Competitors / peers
The targeted segment is **embedded fraud on bank/instant rails**, distinct from card fraud:
- **Plaid Signal** — ACH-specific risk scoring on the Plaid network (claims ~40% return-rate reduction).
- **Stripe Radar** — card-origin, now **extended to ACH/SEPA**, but tied to Stripe's own processing, not a neutral ops platform.
- **GrailPay** — explicitly building "the risk/intelligence layer for bank payments" ([[GrailPay raises $6.7M for remedial ACH platform]]).
- **Unit21 / Alloy / Socure / Feedzai / Sift / Mastercard** — adjacent: post-transaction monitoring (Unit21), identity/onboarding (Alloy, Socure), card/enterprise fraud (Sift, Mastercard, Feedzai).
- **Sardine itself** runs inline (~50–150ms) across ACH/Wire/SEPA/RTP/FedNow/Zelle.

Position: **catching up to parity**, not leading. MT is **buying a capability rather than building deeper**; differentiation is rails-agnostic + stablecoin coverage **inside MT's ledger/ops workflow**, not the fraud model itself. **Why the lay of the land →** card fraud got decades of tooling; bank rails are the under-tooled frontier now opening because RTP/FedNow/stablecoins make money irreversible and instant — hence a cluster of entrants (Sardine, Plaid Signal, GrailPay, Stripe ACH) all racing the same gap.

## [2] Company history / fit
**Modern Treasury** — payment-ops infra, valuation **>$2B** since 2022 Series C, reported **~$2.1B (Oct 2025)**. Already shipped **native fraud/AML tooling**: Compliance product (KYC + transaction monitoring) in **May 2022**, and **incoming-ACH/Wire risk scoring + business verification** in **June 2023**. So Sardine **augments, not creates**, MT's risk stack. Recent pivot: acquired stablecoin startup **Beam (~$40M, Oct 2025)**, integrated **Paxos (Dec 2025)** — explains stablecoin emphasis here.

**Sardine** — fraud+AML platform, founded 2020 (ex-Revolut). ~$145M+ raised, **~$660M valuation** (Series C $70M, Feb 2025). Recently very partnership-active: see [[Sardine partners with Modulr for AI-enabled fraud detection]] (2026-05), [[Sardine and Helix team up on fraud monitoring for sponsor banks]] (2025-12), [[Sardine raises $25 million as National Bank of Canada partners on fraud]] (2026-05).

**Why both act this way →** MT sells commodity-ish payment-ops plumbing and needs a **safety/trust differentiator** to defend take rate as it expands into stablecoins; Sardine needs **distribution** and runs a repeatable "embed into a banking-infra platform" play — it did the **identical move with Treasury Prime (a MT competitor) in June 2023**. So for Sardine this is incremental, not strategic exclusivity.

## [3] Novelty / value-add / traction
**Real novelty is low.** The capability (fraud scoring on bank rails) pre-existed both at MT (2022–2023) and as a Sardine OEM pattern (Treasury Prime 2023, Modulr 2026, Helix 2025). **Traction = zero disclosed**: no launch customers, no volume, no GA, no economics. This is a **press-release-stage distribution partnership**.

**Why the value-add is/isn't real →** The genuine value would be **native bundling reducing integration friction** for MT customers moving onto instant/stablecoin rails — but that only converts to value if it ships as **inline pre-send blocking** and gets adopted. **Who captures the margin:** unclear — no rev-share disclosed; likely Sardine gets a per-screen/transaction fee, MT gets a stickier platform and a trust story. The **disintermediation risk for MT**: if fraud scoring becomes the differentiator, the value migrates toward the fraud-engine layer (Sardine), making MT more of a "ledger/orchestrator" than the owner of the risk relationship (hypothesis).

## [4] What's next / market sentiment
Watch for: GA date, named design partners, whether it's inline-blocking, and how it reconciles with MT's pre-existing 2023 risk scoring (replace/layer/overlap — PR is silent). Regulatory backdrop: rising APP/authorized-push-payment and instant-rail fraud pressure (FedNow/RTP/Zelle) is the structural tailwind making bank-rail fraud tooling a real growth lane.

**Counterintuitive second order →** The flurry of Sardine partnerships (Modulr, Helix, NBC, now MT) signals Sardine winning the **"fraud layer for everyone's rails"** position — which is good for Sardine but means MT's deal is **non-exclusive and commoditized**: every MT competitor can buy the same engine. So this nudges the central question from "does MT now have fraud detection?" (yes, trivially) to **"can MT turn a non-exclusive OEM into durable differentiation, or is it just table stakes for the stablecoin/instant-rail era?"** — likely the latter until proven otherwise.

## Sources
- Modern Treasury press release, 2026-06-24 — https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-partners-with-sardine-to-help-businesses-detect-fraud-earlier-and-reduce-risk-at
- Businesswire, 2026-06-24 — https://www.businesswire.com/news/home/20260624533063/en/
- Finextra, 2026-06-25 — https://www.finextra.com/pressarticle/110245/modern-treasury-partners-sardine-to-help-businesses-detect-fraud-earlier
- fintech.global, 2026-06-25 — https://fintech.global/2026/06/25/sardine-integration-arms-modern-treasury-against-fraud/
- Digest source — https://www.connectingthedotsinfin.tech/r/c9f49e1e
- MT Compliance launch, 2022-05-02 — https://www.businesswire.com/news/home/20220502005258/en/
- MT June 2023 risk-scoring changelog — https://www.moderntreasury.com/journal/june-changelog-2023
- Treasury Prime x Sardine, 2023-06 — https://www.prnewswire.com/news-releases/treasury-prime-announces-partnership-with-sardine-to-strengthen-fraud-detection-capabilities-for-enterprises-and-banks-on-the-platform-301865303.html
- Sardine Series C, 2025-02-11 — https://www.businesswire.com/news/home/20250211169372/en/
- MT acquires Beam, 2025-10-22 — https://fortune.com/crypto/2025/10/22/modern-treasury-beam-stablecoin-startup-acquisition-40-million-all-stock/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is it actually live, or just announced?** → **Announced only** (2026-06-24). No GA date, no rollout language. PR-stage.
2. **Are there named launch customers / committed volume?** → **None disclosed.** No design partner, no GMV.
3. **Is the fraud check inline (pre-send block) or post-hoc alerting?** → **Open / vague.** PR says "real-time monitoring" but doesn't specify blocking-before-send vs alerting-after-settlement — decisive on irreversible rails (ACH/wire/FedNow).
4. **Did MT already have fraud/risk tooling?** → **Yes.** Compliance product (May 2022), incoming-ACH/Wire risk scoring + business verification (June 2023). So this **augments**, not creates — novelty is low.
5. **Does this replace, layer on, or overlap MT's existing 2023 risk scoring?** → **Open.** PR silent; reconciliation unknown.
6. **Is the partnership exclusive?** → **Open, but almost certainly not.** Sardine ran the identical embed play with Treasury Prime (June 2023, a MT competitor), Modulr (2026-05), Helix (2025-12) — non-exclusive OEM pattern.
7. **Who eats fraud losses that slip through?** → **Not disclosed.** Industry default: liability stays with customer/merchant; Sardine provides scoring, not a guarantee. Unconfirmed here.
8. **What are the economics / rev-share / ticket size?** → **Not disclosed.** No pricing, per-transaction fee, or minimums.
9. **Who captures the margin in the stack?** → **Open / analysis.** Likely Sardine takes a per-screen fee; MT gets stickiness + a trust narrative. Risk: value migrates to the fraud-engine layer, leaving MT as ledger/orchestrator.
10. **Is the stablecoin angle real or PR garnish?** → **Plausibly real.** MT acquired Beam (Oct 2025) and integrated Paxos (Dec 2025); fraud screening on stablecoin orchestration is a logical extension — but unproven without a live customer.
11. **How does this compare to direct competitors?** → **Parity/catch-up.** Plaid Signal (ACH), Stripe Radar (now ACH/SEPA), GrailPay (bank-payment risk layer) all target the same gap; MT differentiates only via rails-agnostic + in-platform bundling.
12. **Is bank-rail fraud tooling a real growth lane or a fad?** → **Real tailwind.** Instant/irreversible rails (RTP/FedNow/Zelle/stablecoins) + APP fraud pressure make this a genuine, under-tooled frontier (card fraud got decades; bank rails didn't).
13. **What would re-rate this upward?** → Evidence of **GA, named customers, disclosed economics, or inline-blocking** confirmation. None present yet.
14. **Who needs whom more?** → **Sardine needs distribution; MT needs a trust differentiator.** Roughly symmetric, but Sardine's multi-partner spree suggests it holds the stronger, repeatable position.
15. **Does this change the central question?** → **Yes.** Not "does MT now have fraud detection?" (trivially yes) but **"can a non-exclusive OEM become durable differentiation, or is it just table stakes for the stablecoin/instant-rail era?"** — likely table stakes until proven.

Importance: 2/5 — Distribution/OEM-style announcement, not a product launch with proof: no GA, no customers, no economics, no liability terms. MT already shipped native fraud scoring in 2022–2023 and Sardine has run this identical embed play repeatedly, so it is incremental for both. Nudged to 2 (not 1) because embedded fraud on instant + stablecoin rails is a genuine, well-timed growth lane — but value is unconfirmed until it converts to live volume.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Fraud detection & prevention is a large, fast-growing software category, though analyst estimates diverge widely on the absolute number: ~$40.4bn (Grand View, 2026) to ~$70–82bn (Mordor / Straits, 2026), CAGR ~16–24% to 2030–2034 (per Grand View / Coherent / Mordor / Straits, all market-research-firm estimates, as of late 2025 / 2026; treat the spread as a sign the "TAM" is loosely defined, not a precise figure). The relevant *subsegment* here is narrower — embedded fraud/AML on bank & instant rails, distinct from card fraud, which the note already frames well. **Why now:** the demand driver is irreversibility + speed of new rails. Deloitte estimates US authorized-push-payment (APP) fraud losses could reach ~$15bn by 2028 (Deloitte, via deloitte.com); FedNow is live across all 50 states at 1,000+ FIs and RTP raised per-transaction limits to $10M in 2025 (Federal Reserve / The Clearing House, via Wolters Kluwer / FICO). On these rails the *only* prevention window is the seconds before authorization — which is exactly the "real-time / inline" claim MT is buying. Internal base corroboration: [[Javelin report instant payment rails outpace fraud detection]] (2026-02) — the structural thesis that rail rollout is outpacing fraud tooling, i.e. the gap MT/Sardine are selling into. **Structure:** fragmented and consolidating — many point vendors (identity, AML monitoring, ACH-specific, card-origin) racing to become the embedded layer; barriers are data network effects + model accuracy, not capital. Recent consolidation signal: [[AdvanThink acquires Paris-based AML firm Heptalytics]] (2026-01).

**Competitive landscape.** Sector KPIs: protected payment volume, fraud-loss-prevented, detection latency (ms), false-positive/return-rate reduction, ARR growth. Key players & basis of competition (product accuracy + distribution, not price): the note's competitor list ([0]–[1]) is solid; the market-layer addition is the embedding-into-someone-else's-platform race. Recent dated moves the note doesn't fully capture: [[Sardine partners with Modulr for AI-enabled fraud detection]] (2026-05-01), [[Finastra and Fraudaverse deploy real-time fraud prevention]] (2026-03), [[ACI Worldwide launches ACI Connetic multi-rail payments platform]] (2026-04) — note ACI explicitly markets fraud "built directly into transaction workflows … rather than requiring separate bolt-on systems," i.e. a *vertically-integrated multi-rail-plus-fraud platform competing with the MT+Sardine bolt-together approach*. MT's position: **catching up to parity via OEM**, consistent with the note — the market-layer point is that MT is *assembling* (ledger + bought-in fraud engine) while ACI/Finastra ship native-embedded, so MT's bundle is only differentiated if integration friction genuinely falls and it owns the stablecoin niche.

**Comps & multiples.** No deal/valuation/round attaches to *this* news (it is a partnership, not a financing) — so no transaction multiple to compute for the event itself. Reference comps for the two protagonists and the segment (private, so post-money round valuations, NOT market cap):
- **Sardine** — ~$660M post-money, Series C $70M, May 2026; ARR +130% YoY, customers ~2x (per sardine.ai / Crunchbase). Revenue undisclosed → EV/Revenue = **no data**; growth is the justification narrative, multiple `[UNSOURCED]`.
- **Feedzai** — ~$2.0bn, $75M Series E, Oct 2025; protects >$70bn annual payment volume, prevents >$2bn losses/yr (per Feedzai / fintech.global). [[Feedzai raises $75M at $2B+ valuation for fraud platform]]. Revenue undisclosed → multiple **no data**.
- **Unit21** — ~$92M total raised, $45M Series C, Jun 2023; no fresh valuation (PitchBook/Tracxn). Stale → excluded from any range.
- **SEON** — $80M Series C, Sept 2025, $187M total raised ([[SEON raises $80M Series C led by Sixth Street]]) — adjacent fraud/AML, valuation undisclosed.
Distribution not computed (fewer than 3 verifiable like-for-like multiples; all revenue figures private). Qualitative read: Feedzai (~$2.0bn) sits ~3x Sardine (~$660M) on headline valuation, plausibly reflecting Feedzai's larger protected-volume base and longer enterprise/bank footprint vs Sardine's faster growth — **in-line-to-cheap for Sardine on growth (analysis)**, but unverifiable without revenue. No outlier flag warranted on data this thin.

**Risk flags.**
1. **Disintermediation of MT toward the fraud layer** — the note raises this; the market-layer sharpening is that Sardine's valuation/growth is rising *on the back of multi-partner distribution* (Modulr, Helix, NBC, MT), so the franchise value accrues to Sardine, while MT's deal is one non-exclusive node. Second order: MT risks renting, not owning, its key trust differentiator on irreversible rails.
2. **Native-embedded competitors close the "bolt-on" gap** — ACI Connetic (2026-04) and Finastra/Fraudaverse (2026-03) market fraud built *into* the rail rather than integrated alongside it. If buyers prefer single-vendor native fraud, MT's "augment via OEM" loses its friction-reduction selling point; second order: pressure on MT take rate as the bundle commoditizes.
3. **"TAM tailwind" is real but the value-capture is unproven for MT specifically** — the APP/instant-fraud loss curve is a genuine demand driver, but a large sector TAM does not translate to MT margin when MT neither owns the model nor (per PR) has disclosed inline-blocking, customers, or economics. Second order: the growth lane mostly re-rates the *fraud-engine* vendors (Sardine/Feedzai), not the orchestrator buying their engine.

**What this changes (idea-lens).** This is not a re-rating event for MT — it's table-stakes catch-up in a sector where the durable franchise is forming at the *fraud-engine* layer (Sardine's serial-OEM model + 130% ARR growth) (analysis). Falsifiable thesis: *the embedded-fraud value chain consolidates around a few neutral engines (Sardine, Feedzai) that every payment-ops/banking-infra platform OEMs, leaving orchestrators competing on rails/UX, not fraud.* Trigger to confirm: another major MT-competitor signs the same Sardine/Feedzai engine within ~12 months (Treasury Prime already did, 2023). What would break it: a payment-ops platform builds proprietary, demonstrably-better inline fraud and wins on it — or MT discloses GA + named customers + inline-blocking that turn this OEM into real differentiation.

Sources: https://www.grandviewresearch.com/industry-analysis/fraud-detection-prevention-market · https://www.mordorintelligence.com/industry-reports/global-fraud-detection-and-prevention-fdp-market-industry · https://www.deloitte.com/us/en/insights/industry/financial-services/authorized-push-payment-fraud.html · https://www.fico.com/blogs/real-time-payments-rails-fednow-need-enhanced-fraud-protection · https://news.crunchbase.com/cybersecurity/fraud-detection-startup-sardine-ai-fundraise/ · https://fintech.global/2025/10/06/ai-regtech-feedzai-bags-75m-at-2bn-valuation/ · https://www.fintechfutures.com/regulations-compliance/risk-and-compliance-fintech-unit21-bags-45m-series-c · https://investor.aciworldwide.com/news-releases/news-release-details/multi-rail-complexity-grows-aci-worldwide-delivers-one-cloud
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
