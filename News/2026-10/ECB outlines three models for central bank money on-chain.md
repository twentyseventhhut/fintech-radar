---
title: "ECB outlines three models for central bank money on-chain"
date: 2026-10-05
retrieved: 2026-10-08
tags:
  - company/ecb
  - industry/blockchain
  - industry/stablecoins
  - region/europe
  - type/research-report
sources:
  - https://en.bloomingbit.io/feed/news/121477
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sc31edfba
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# ECB outlines three models for central bank money on-chain

> [!info] 2026-10-05 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇪🇺 ECB outlines three models for bringing central bank money on-chain, covering direct issuance of tokenized reserves, bridging existing payment systems with DLT platforms, and tokenizing reserves through private intermediaries. The approaches could enable DLT-based transactions in tokenized securities, deposits, and stablecoins to be settled in central bank money. Each model assigns a different role to the central bank and private sector.

## Первоисточники

### en.bloomingbit.io
<https://en.bloomingbit.io/feed/news/121477>
*239 слов · direct*

ECB Outlines Three Models for Bringing Central Bank Money On-Chain
Summary
The European Central Bank, or ECB, said it has outlined three models to introduce central bank money into blockchain -based financial markets.
The models are direct issuance of tokenized central bank reserves , bridging and synchronizing existing payment systems with DLT platforms , and tokenizing reserves through private intermediaries .
The ECB said the approach could allow DLT-based asset transactions, including tokenized securities , deposits , and stablecoins , to be settled in central bank money.
Forecast Trend Report by Period
The European Central Bank has outlined three models for introducing central bank money into blockchain-based financial markets.
According to The Block on October 2, the ECB presented three ways to use central bank money in distributed ledger technology, or DLT, environments: direct issuance of tokenized central bank reserves, bridging and synchronizing existing payment systems with DLT platforms, and tokenizing reserves through private intermediaries.
Under the first model, the central bank would issue reserves directly as tokens on a programmable ledger. The second would keep central bank money in existing systems while linking them to DLT platforms to settle transactions. The third would have private intermediaries deposit reserves at the central bank and issue tokens on DLT networks backed one-to-one by those reserves.
The ECB said the approaches could enable DLT-based asset transactions, including tokenized securities, deposits and stablecoins, to be settled in central bank money.
Uk Jin

## Контекст

<!-- enrichment:context -->
# Context-enrichment: ECB outlines three models for central bank money on-chain
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **1 Oct 2026**, ECB Executive Board member **Isabel Schnabel** gave a speech at the **Bank of England "Future of Money" conference** in London laying out **three architectural options** for putting central-bank money onto DLT. The item's framing ("ECB outlines three models") overstates finality: these are **options for discussion, not decided policy** — the ECB is explicitly "testing hybrid infrastructure rather than committing to one architecture."

The three models, precisely:
1. **Direct issuance (native tokenization):** central bank operates a programmable platform; reserves are *natively tokenized* on-ledger. Maximal CB control, maximal CB operational footprint.
2. **Bridging / interoperability layer:** reserves stay in the existing RTGS (TARGET), connected to a DLT platform via an interoperability layer using **triggers / hash-linked mechanisms**. Reserves remain *non-tokenized*. This is the lowest-change, incumbent-preserving option.
3. **Private intermediation:** a private entity deposits reserves at the CB and issues settlement tokens *1:1 backed* by those reserves — i.e. a tokenized-deposit / regulated-stablecoin-like layer sitting between users and CB money.

**Why structured this way:** the three models are deliberately a spectrum along **"who holds the ledger and who bears operational risk"** — from CB-operated (Model 1) to market-operated with CB only as backstop (Model 3). All three **preserve the two-tier monetary system** (CB money at the top, commercial/private money below). That is the real tell: the ECB is not choosing disintermediation; it is mapping how to keep central-bank-money finality while letting private DLT markets develop. The benefits emphasized — **programmability** and **atomicity** (atomic DvP) — are the same ones every tokenized-settlement pitch uses; the ECB's contribution is sequencing them against institutional risk, not a technical breakthrough.

Note: not a speculative framing. These models directly map to the ECB's live two-track program: **Pontes** (near-term bridge, = Model 2) and **Appia** (long-term integrated ecosystem, open on Models 1/3).

## [1] Competitors / peers
- **Bank of England** — host of the very conference; BoE is running its own wholesale RTGS renewal + synchronisation ("DLT via trigger") experiments, i.e. effectively BoE's preferred route is Model 2. Schnabel speaking at the BoE venue signals aligned, incumbent-preserving, synchronisation-first thinking among major CBs.
- **Federal Reserve** — notably absent / no comparable public framework; the Fed under current leadership is hostile to a CBDC and has not published an equivalent wholesale-DLT settlement menu, leaving the EU/UK ahead on wholesale (as opposed to the US private-stablecoin route post-GENIUS-style regime).
- **Other CBs:** [[RBI launches blockchain-based Unified Markets Interface]] (Oct 2025) already uses a **wholesale CBDC as the live settlement leg** for tokenized assets — i.e. India has effectively *shipped* a version of Model 1/2; [[HKMA prioritizes e-HKD for wholesale use over retail]] (Oct 2025) shows the global pivot from retail CBDC to wholesale settlement is the dominant theme.
- **Market infra:** [[Clearstream launches tokenized securities platform]] (Nov 2025, D7 DLT) and other EU CSDs are the demand side — they need a CB-money settlement leg, which is exactly what Pontes/these models supply.

**Why the landscape is this way (2nd order):** CBs have quietly abandoned the retail-CBDC fight (privacy/bank-disintermediation backlash) and converged on **wholesale DLT settlement**, where the political cost is low and the market pull (tokenized bonds/repo) is real. The ECB's "three models" is a late-ish formalization of a consensus BoE/HKMA/RBI already enacted — hence importance is moderate, not high.

## [2] Company (ECB) history / fit
Consistent, incremental trajectory — this is step N of a multi-year program, not a new initiative:
- **Jul 2025** — [[ECB commits to distributed ledger settlement work]] (dual-track decision).
- **Jan/Feb 2026** — [[ECB paves way for DLT assets as Eurosystem collateral]] (DLT-issued CSD assets accepted as collateral).
- **Mar 2026** — [[ECB launches Appia tokenization roadmap]] (long-term integrated-ecosystem track; blueprint due H2 2028).
- **Apr 2026** — [[ECB sets out new strategy for future of European payments]] (umbrella: digital euro + Pontes + Appia + cross-border).
- **Jun 2026** — [[Digital Euro clears key hurdle in EU parliament]].
- **21 Sep 2026** — **Pontes** goes live: bridge of market DLT platforms to TARGET; 13 institutions (Deutsche Bank, Santander, SocGen, EIB...) settling tokenized assets in CB money.
- **1 Oct 2026** — this speech: the conceptual menu behind the above.

**Why ECB acts this way:** structural pressure from (a) losing settlement/securities-infra relevance if tokenized markets settle in stablecoins/commercial money instead of CB money, and (b) euro-sovereignty anxiety vs USD stablecoins (see [[This Week in Fintech Europe urged to back stablecoins]]). Mapping three models = keeping optionality while the market (Pontes pilot) reveals demand.

## [3] Novelty / value-add / traction
- **Genuinely new:** very little. The *three-model taxonomy as a public ECB communication* is new, but each model is already instantiated (Model 2 = live Pontes; Model 1/2 = live RBI UMI; Model 3 = tokenized-deposit concept banks already pilot).
- **Traction (real):** the credible datapoint is **Pontes live since 21 Sep 2026 with 13 named institutions** — that is adoption, not announcement. The *speech itself* has zero independent traction; it is analysis/framing.
- **Value-add, de-PR'd:** the value is **sequencing + institutional legitimation**, not technology. By publicly ranking options, the ECB signals to EU market infra and banks which rails to build to.

**Who captures the margin (2nd order):** the choice of model decides *where settlement economics sit*. Model 1 keeps everything at the ECB (private settlement-service providers squeezed out); Model 3 hands a fee layer to private intermediaries (stablecoin issuers / tokenized-deposit banks). The unresolved question is therefore **distributional, not technical** — which is why the ECB will not pick yet.

## [4] What's next / market sentiment
- **Timeline:** Pontes operating now; **Appia blueprint H2 2028**; model choice deferred until pilot evidence accumulates. No committed date to adopt any single model.
- **Risks / silences:** the speech is silent on (a) the economics — who pays for and earns from settlement in each model; (b) whether Model 3 effectively blesses regulated stablecoins/tokenized deposits as CB-money proxies (tension with the ECB's defensive stance on USD stablecoins); (c) governance of an ECB-operated programmable ledger (Model 1 concentration/operational-risk).
- **Sentiment:** incremental-positive for EU tokenized-securities infra; low surprise. **Counterintuitive 2nd-order:** the more the ECB preserves the two-tier system via Model 2/3, the more it *empowers* private intermediaries (banks, tokenized-deposit/stablecoin issuers) rather than displacing them — i.e. the "CBDC" fear is inverted; the real fight is over which private layer the ECB legitimizes.

## Sources
- The Block (via en.bloomingbit.io reprint): <https://en.bloomingbit.io/feed/news/121477>
- FinanceFeeds: <https://financefeeds.com/ecb-three-models-central-bank-money-onchain/>
- Crypto-Economy: <https://crypto-economy.com/ecbs-isabel-schnabel-outlines-three-models/>
- Ledger Insights (Appia consultation): <https://www.ledgerinsights.com/ecb-launches-appia-consultation-re-wholesale-dlt-settlement-infrastructure/>
- Cointelegraph (Pontes/Appia two-track): <https://cointelegraph.com/news/ecb-launches-two-track-dlt-settlement-plan-2026>
- FIA ("All roads lead to DLT"): <https://www.fia.org/marketvoice/articles/all-roads-lead-dlt-ecb-advances-pontes-and-appia>
- Internal: [[ECB commits to distributed ledger settlement work]], [[ECB launches Appia tokenization roadmap]], [[ECB sets out new strategy for future of European payments]], [[ECB paves way for DLT assets as Eurosystem collateral]], [[Digital Euro clears key hurdle in EU parliament]], [[RBI launches blockchain-based Unified Markets Interface]], [[HKMA prioritizes e-HKD for wholesale use over retail]], [[Clearstream launches tokenized securities platform]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this a report or a speech?** A **speech** by Isabel Schnabel at the BoE "Future of Money" conference, 1 Oct 2026 — not a new ECB report or policy decision. The note's "outlines three models" overstates finality. (answered)
2. **Are the three models decided policy?** No — explicitly *options under exploration*; ECB is "testing hybrid infrastructure rather than committing." (answered)
3. **Is any of this genuinely new?** The *taxonomy* is a new communication; the mechanisms are not. Model 2 is already live as Pontes (21 Sep 2026); India's RBI UMI already settles tokenized assets in wholesale CBDC. (answered)
4. **What's the hard traction datapoint?** Pontes live since 21 Sep 2026, 13 named institutions (Deutsche Bank, Santander, SocGen, EIB). The speech itself has none. (answered)
5. **Does this duplicate the Mar-2026 Appia note or Apr-2026 strategy note?** No — those cover the Appia roadmap and the umbrella payments strategy; this is a distinct, later conceptual framing. Related, not duplicate. (answered — fresh)
6. **Who captures settlement economics under each model?** Open / silent in sources — Model 1 keeps it at ECB, Model 3 hands a fee layer to private intermediaries. The deferral *is* a distributional fight. (open)
7. **Does Model 3 effectively bless regulated stablecoins/tokenized deposits as CB-money proxies?** Plausibly yes; unaddressed in the speech, and in tension with the ECB's defensive stance on USD stablecoins. (open)
8. **How does this compare to BoE / Fed?** BoE (the host) favors synchronisation/Model 2; Fed has no comparable public framework and is CBDC-hostile. EU/UK ahead on wholesale. (answered)
9. **What's the real driver?** Euro-sovereignty + risk of tokenized markets settling in private money if CB money isn't available on-chain. (answered, analysis)
10. **Timeline to an actual decision?** None committed; Appia blueprint H2 2028, model choice deferred pending pilot evidence. (answered)
11. **Does "programmability/atomicity" represent ECB novelty?** No — generic tokenized-settlement benefits; ECB's value is sequencing/legitimation, not tech. (answered)
12. **Could the ECB run a programmable ledger itself (Model 1) operationally?** Open — concentration and operational-risk governance unaddressed. (open)
13. **Is there a retail-CBDC angle?** No — this is strictly wholesale; consistent with the global pivot away from retail CBDC (HKMA). (answered)
14. **Does the two-tier-preservation framing actually empower private intermediaries?** Yes (2nd-order) — preserving tiers via Model 2/3 strengthens banks/issuers rather than displacing them. (answered, analysis)
15. **Does the headline source (The Block via a reprint) distort anything?** The bloomingbit reprint omits the speaker (Schnabel), venue (BoE conf), and "options not policy" status — primary/secondary coverage restores those. (answered)

**Importance: 3/5** — Credible, well-sourced, and backed by a genuinely live rail (Pontes, 13 institutions). But it is a *framing speech*, not a decision or launch; the mechanisms are already instantiated elsewhere (Pontes, RBI UMI); it is step N in a long, pre-telegraphed ECB program. Matters for EU tokenized-securities infra and euro-sovereignty watchers; not a market-moving surprise.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Theme = wholesale central bank money on DLT / tokenised settlement (not retail CBDC). The ECB's "three models" are a conceptual taxonomy (direct token issuance of reserves; bridging RTGS to DLT; private intermediaries issuing reserve-backed tokens), presented by Isabel Schnabel at the BoE Future of Money conference on 2026-10-01 (per FinanceFeeds/Genfinity, as of 2026-10-02). They map to the Eurosystem's already-launched delivery stack: **Pontes** (launched 2026-09-21), a dual-settlement bridge where the cash leg settles in T2/TARGET or via DLT cash tokens, and **Appia**, the long-term strategic roadmap with full implementation targeted for 2028 (per ECB press release 2026-09-21; FIA). So the "news" is framing/communication layered on top of live infrastructure, not a new product. No TAM is cleanly sourceable for wholesale-CBDC settlement — "no data"; adjacent anchors only: stablecoin market cap ~$307bn in early 2026 (per Quant.network, unverified primary) and India's REC CBDC-settled tokenised bond targeting a ~$624bn debt market (per TechTimes 2026-09-04) — both context, not this market's size. Structure: monopoly issuer (the central bank owns the money leg); value in the securities/cash-leg plumbing is contested between the central bank's own rails (T2/Pontes) and private DLT platforms. **Why now:** tokenised securities/deposits/stablecoins are moving pilot→production, and without a central-bank cash leg they settle in commercial-bank or stablecoin money — the ECB is racing to keep the risk-free settlement asset inside its perimeter before private money (stablecoins, tokenised deposits) becomes the default DLT settlement medium.

**Competitive landscape.** This is a central-bank policy space, not a company market; "KPIs" are adoption of the settlement rail (participants onboarded, settlement volume, operating hours) — none disclosed yet, `[UNSOURCED]`. Players are peer central banks, not firms: **ECB/Eurosystem** (Pontes/Appia), **Bank of England** (host of the conference; its own DLT/RTGS synchronisation work), **RBI** (wholesale e₹ live in the Unified Markets Interface for atomic settlement — see internal comp), **HKMA** (steered e-HKD to wholesale over retail), and the BIS (Project Agora) as the multilateral venue. Basis of competition is standards/interoperability, not price. The three-model framing is deliberately model-agnostic: the ECB leaves open whether it issues tokens directly (model 1) or lets private intermediaries do it (model 3), i.e. it is hedging between owning the token and merely backing it. Protagonist position: **ahead on delivery** vs most peers (Pontes is live, not a whitepaper) but **deliberately conservative on model choice** — Pontes keeps final settlement in T2 rather than issuing native reserve tokens on-chain, which is the cautious bridging option (model 2), not direct issuance (model 1). Moat: the ECB's "moat" is structural — it is the sole issuer of euro central bank money; the open question is whether that moat extends onto DLT rails or is disintermediated by private money `(analysis)`.

**Comps & multiples.** Not a deal/round — no valuation, revenue, GMV or users. EV/Revenue, P/E, price-per-user all **not applicable / no data**; no multiple can be computed. Internal comps (central-bank DLT/wholesale-settlement precedent in-base), as a qualitative ladder of the same theme:
- [[ECB launches Appia tokenization roadmap]] (2026-03-12) — the long-term roadmap this news sits on.
- [[ECB commits to distributed ledger settlement work]] (2025-07-03) — origin of the exploratory wholesale-settlement work (May–Nov 2024 trials).
- [[ECB advances to next phase of digital euro project]] (2025-10-31) — parallel retail track (distinct from this wholesale theme; useful to avoid conflation).
- [[RBI launches blockchain-based Unified Markets Interface]] (2025-10-20) — closest live peer: wholesale CBDC as the settlement leg for tokenised assets, i.e. model-1-style direct use already in production.
- [[HKMA prioritizes e-HKD for wholesale use over retail]] (2025-10-31) — peer central bank choosing wholesale focus.
- [[Deutsche Borse integrates SocGen CoinVertible stablecoins]] (2025-11-21) — private-money settlement filling the gap the ECB is trying to close.
Distribution not computed (no numeric comps); comparison is qualitative only.

**Risk flags.**
1. **Disintermediation of the settlement asset.** If private tokenised deposits/stablecoins (e.g. SocGen FORGE via Deutsche Börse) scale on DLT before Pontes/Appia, the euro risk-free settlement leg migrates to private money — the ECB loses the monetary-policy transmission and financial-stability lever that is its stated reason for acting. Second-order: it would then be forced into the more invasive model 1 (direct token issuance) under time pressure.
2. **Framing vs delivery gap.** The "three models" is communication, not a commitment; Pontes is a cautious bridge (settlement still finalises in T2) and full Appia is a 2028 target. The risk is that the DLT market front-runs the ECB's 2028 timeline and standardises on other rails in the interim.
3. **Fragmentation / standards risk.** Multiple coexisting DLTs (JPMorgan, DTCC, BNP Paribas noted by industry) mean the ECB bridges to a moving multi-chain target; a wrong interoperability bet raises rebuild cost and strands early participants.

**What this changes (idea-lens).** `(analysis)` This signals the ECB is committing to a *bridging-first, optionality-preserving* path rather than native reserve tokens — it keeps the euro inside the settlement leg while deferring the hard choice to 2028. Falsifiable thesis: if Pontes reports material wholesale DLT settlement volume (participants + value) through 2027, the ECB has successfully defended the central-bank money leg against private stablecoins/tokenised deposits. Trigger/what breaks it: a major European tokenised-securities venue defaulting to a private stablecoin (e.g. a SocGen/EURC-type coin) for its cash leg instead of Pontes would show the bridge is too slow and the disintermediation risk is realising.

Sources: https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260921~e754847a7b.en.html · https://financefeeds.com/ecb-three-models-central-bank-money-onchain/ · https://genfinity.io/2026/10/02/ecb-schnabel-three-models-central-bank-money-onchain/ · https://www.fia.org/marketvoice/articles/all-roads-lead-dlt-ecb-advances-pontes-and-appia · https://en.bloomingbit.io/feed/news/121477
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
