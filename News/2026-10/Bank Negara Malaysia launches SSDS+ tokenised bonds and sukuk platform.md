---
title: "Bank Negara Malaysia launches SSDS+ tokenised bonds and sukuk platform"
date: 2026-10-26
retrieved: 2026-10-26
tags:
  - company/bank-negara-malaysia
  - industry/blockchain
  - industry/capital-markets
  - region/asia
  - type/product
sources:
  - https://www.ledgerinsights.com/malaysias-central-bank-launches-depository-for-tokenized-bonds-sukuk
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s3db6ccf8
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Bank Negara Malaysia launches SSDS+ tokenised bonds and sukuk platform

> [!info] 2026-10-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Malayasia's central bank Bank Negara Malaysia, launched SSDS+, a tokenised bonds and sukuk depository platform, integrating with its 24/7 RTGS system.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.ledgerinsights.com/malaysias-central-bank-launches-depository-for-tokenized-bonds-sukuk>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 20 October 2026 Bank Negara Malaysia (BNM) launched **SSDS+**, a next-generation of its Scripless Securities Depository System, to support the issuance, depository and safekeeping of **tokenised bonds and sukuk**. SSDS+ was built in-house using cloud and distributed-ledger technology (DLT), tracks ownership/transfers of tokenised securities, and integrates with **RENTAS+** — the real-time gross settlement (RTGS) rail BNM relaunched in October 2025 — so that cash legs settle in central-bank money on a 24/7 basis. BNM positions it for wholesale issuance but says it is also ready for tokenised government and retail bonds. ([[Bank Negara Malaysia launches SSDS+ tokenised bonds and sukuk platform]]) — https://www.thestar.com.my/business/business-news/2026/10/20/bnm-launches-scripless-securities-depository-system-to-support-tokenised-bond-sukuk-issuance , https://cointelegraph.com/news/malaysia-central-bank-tokenized-bonds-sukuk-dlt-platform

**[1] What SSDS+ actually is (upgrade, not greenfield).** The legacy SSDS is the central securities depository (CSD) for Malaysia's wholesale debt market, operated under BNM's RENTAS infrastructure (which combines the securities depository SSDS with the payment RTGS). SSDS+ bolts a DLT/token layer onto that CSD role: SSDS+ manages the transfer of tokenised securities and maintains digital ownership records, while RENTAS+ moves the corresponding central-bank-money payments — i.e. delivery-versus-payment (DvP) across two linked but distinct systems rather than atomic settlement on one shared ledger. Importantly, BNM named **no first/launch issuance** at go-live, so this is infrastructure availability, not a live bond yet. — https://www.digitalnewsasia.com/digital-economy/bnm-launches-tokenised-bond-and-sukuk-platform-ssds-malaysia-advances-digital-debt , https://www.coindaro.com/bank-negara-malaysia-tokenized-bonds-ssds/

**[2] Why it matters for Malaysia.** Malaysia's bond and sukuk market was ~US$575.6bn (RM2.35tn) at end-June 2026, with sukuk >60% of the market in 2025 — one of the world's deepest Islamic-finance debt pools. A native tokenisation+DvP rail for sukuk is a credible claim to Islamic-finance digital leadership, and the 24/7 central-bank-money settlement via RENTAS+ removes settlement-time and counterparty-cash risk that T+ cycles carry. Retail-bond readiness hints at a longer-term retail-access agenda. — https://themalaysianreserve.com/2026/10/20/bnm-launches-ssds-platform-for-tokenised-bonds-and-sukuk/ , https://www.ledgerinsights.com/malaysias-central-bank-launches-depository-for-tokenized-bonds-sukuk

**[3] Precedents / peer context.** BNM joins a cluster of central banks wiring tokenised securities to central-bank-money settlement, but choosing to build its **own** ledger rather than ride an industry platform:
- **HKMA Project Ensemble** — moved from sandbox (Aug 2024) to **EnsembleTX** real-value pilot (13 Nov 2025) for tokenised deposits settling tokenised MMF/bond trades; Hong Kong has repeatedly set world-record digital-bond issuances.
- **MAS Project Guardian** (Singapore) — 28+ institutions, Fixed Income framework (Nov 2025); MAS is piloting wholesale-CBDC settlement of **tokenised MAS Bills**. See also [[MAS launches BLOOM for tokenised liabilities and stablecoins]].
- **ECB** — dual-track plan: **Pontes** interim bridge linking DLT platforms to TARGET Services, pilot targeted end-Q3 2026, plus a longer-term "Appia" track.
Regionally, BNM also sits inside the cross-border digital-money push with MAS/BoT via [[Bank Negara Malaysia and Bank of Thailand join BLOOM initiative]]. — https://www.info.gov.hk/gia/general/202511/13/P2025111300366.htm , https://www.mas.gov.sg/-/media/mas-media-library/development/fintech/guardian/guardian-fixed-income-framework-v1_1.pdf , https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr250701~f4a98dd9dc.en.html

**[4] What to watch.** (a) First actual tokenised sukuk/bond issuance on SSDS+ and its size — until then this is plumbing, not proof. (b) Whether primary dealers / issuers adopt it vs. the incumbent SSDS, and whether BNM runs both in parallel for years. (c) Whether retail bonds actually go live and how (direct retail depository access is a big operational/regulatory step). (d) Interoperability: is SSDS+ cross-border-ready (linking to MAS/HKMA tokenised rails and the BLOOM cross-border digital-money work) or a domestic island? (e) Resilience/governance of an in-house DLT built by a central bank. Timeline: SSDS legacy (long-standing CSD) → **RENTAS+ 24/7 RTGS (Oct 2025)** → **SSDS+ tokenised depository (20 Oct 2026)**.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
1. Is any tokenised bond or sukuk actually live on SSDS+, or did BNM only launch empty infrastructure with **no named first issuance**? (Sources say no first issuance was named — this is capability, not adoption.)
2. Is settlement truly **atomic DvP on one ledger**, or two linked systems (SSDS+ for securities, RENTAS+ for cash) coordinating DvP? The latter still carries operational/coordination risk.
3. The aggregated note says SSDS+ integrates with a "24/7 RTGS system" — confirm that is **RENTAS+** (launched Oct 2025) and not plain RENTAS; mixing them overstates novelty.
4. "Tokenised" vs genuinely "on DLT": is the bond a native token on a distributed ledger, or a conventional scripless entry relabelled? BNM says DLT-built, but validate it isn't marketing gloss over the existing CSD.
5. Will issuers/primary dealers migrate from the incumbent SSDS, or will SSDS+ sit idle? Central-bank-built rails often launch years before real volume.
6. Retail-bond "readiness" — is retail depository access a real near-term plan with a legal/KYC framework, or an aspirational line? Direct retail CSD access is a major undertaking.
7. Is SSDS+ **cross-border interoperable** (with MAS/HKMA tokenised rails, BLOOM) or a domestic silo? A standalone national ledger risks fragmentation vs. shared-platform peers.
8. Governance/resilience risk: an in-house central-bank DLT concentrates both issuance infrastructure and settlement — single point of failure and no external audit track record yet.
9. Does "central-bank money settlement" imply a wholesale CBDC, or just RTGS balances? (Likely RTGS, not a CBDC — avoid overclaiming a CBDC launch.)
10. Does this actually lower issuance cost/time, or just digitise an already-efficient scripless system? Malaysia's bond market is already dematerialised — marginal benefit unclear.
11. Sukuk-specific: does tokenisation respect Shariah structuring (asset-backing, ownership transfer semantics)? Tokenised sukuk raise novel Shariah-compliance questions not addressed at launch.
12. Timeline integrity: SSDS (legacy CSD) → RENTAS+ (Oct 2025) → SSDS+ (20 Oct 2026) — is any date conflated with the earlier BLOOM/cross-border announcements (distinct stories)?
13. Vendor/tech stack: "cloud + DLT built in-house" — which DLT, permissioned/permissionless, and is the claim verifiable or vague?
14. Does single-channel sourcing (one digest mention + Ledger Insights) risk missing caveats BNM stated in its own release? Cross-check the primary BNM media statement.

**Importance: 3/5** — rationale: A credible, concrete central-bank infrastructure upgrade in one of the world's largest sukuk markets, adding 24/7 central-bank-money settlement for tokenised debt — meaningful for Islamic-finance digital-market leadership and consistent with a global wholesale-tokenisation wave (HKMA, MAS, ECB). But it is infrastructure availability with **no named first issuance** and uncertain adoption, built as a domestic in-house ledger rather than a shared/cross-border platform, so near-term real-world impact is unproven. Not a 4/5 until a live tokenised sukuk issues and dealers adopt it.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** The news sits in central-bank-operated DLT securities settlement — a CSD/RTGS modernisation layer, distinct from the private-RWA tokenisation stack. Malaysia's bond and sukuk market stood at ~US$575.6bn (RM2.35tn) as at end-June 2026, with sukuk >60% of outstanding (~RM1.2tn), making this the natural home for a state-run tokenised-debt rail (per The Asian Banker / cbonds, via digitalnewsasia & themalaysianreserve, as of 2026-10-20). Structure: a central CSD is a natural monopoly — BNM already runs the legacy SSDS and RENTAS RTGS, so SSDS+ extends an incumbent, not a greenfield entrant; barriers are regulatory and operational (central-bank-money settlement), not capital. Drivers / "why now": (i) the global shift to DvP-on-ledger with central-bank money as the settlement asset — mirrored by the ECB (Eurosystem accepting DLT-issued CSD collateral from 2026-03-30) and MAS's tokenised-bills/wholesale-CBDC pilots in 2026; (ii) Malaysia's ambition to retain Islamic-finance leadership, where a tokenised-sukuk standard is a differentiator; (iii) prior domestic proof point — Khazanah priced Malaysia's first tokenised sukuk (RM100m, 1yr, Wakalah) on 2026-04-28 with the SC, so SSDS+ productionises a validated pilot `(analysis)`.

**Competitive landscape.** This is infrastructure, not a P&L — the relevant KPIs are settlement finality/latency (SSDS+ claims 24/7 vs T+ batch), on-platform issuance volume, and number of connected dealers/custodians (none disclosed — `[UNSOURCED]`). "Competitors" are peer central banks / market infrastructures building the same rail, not commercial rivals: MAS ([[MAS launches BLOOM for tokenised liabilities and stablecoins]]), RBI ([[RBI launches certificate of deposit tokenisation pilot]]), BoE/FCA ([[Bank of England and FCA launch tokenized wholesale markets consultation]]), ECB, plus private venues (Canton/Digital Asset, 21X — [[AMINA becomes first regulated bank on 21X DLT venue]]) competing on the opposite philosophy (public/permissionless rails). Basis of competition here is standards-setting and network adoption, not price. BNM's position: ahead on the specific niche of a sovereign-run tokenised-sukuk depository with in-house DLT + central-bank-money settlement; moat is regulatory franchise + network effects of being the mandated domestic CSD (switching cost ≈ absolute). SEBI is pursuing a similar state-sponsored path ([[SEBI weighs easing debt-issuer disclosures, starts bond tokenisation]]).

**Comps & multiples.** No deal/valuation/round attaches to this news — BNM is a central bank, so trading multiples are N/A (distribution not computed; qualitative comparison only). Internal comps as directional precedents for central-bank / infrastructure tokenised-debt moves: [[MAS launches BLOOM for tokenised liabilities and stablecoins]], [[RBI launches certificate of deposit tokenisation pilot]], [[Bank of England and FCA launch tokenized wholesale markets consultation]], [[SEBI weighs easing debt-issuer disclosures, starts bond tokenisation]], [[Brazil's Anbima pilots tokenized financial assets on blockchain]]. The one commercial size marker in-corpus is Khazanah's RM100m first tokenised sukuk — a pilot ticket, i.e. the addressable on-ledger base today is a rounding error vs the RM2.35tn total market. Multiples: no data.

**Risk flags.**
- **Announced vs live / no first issuance named.** BNM launched the platform but has not named a first SSDS+ issuance or go-live issuer (per coindaro, 2026-10-20) — so "launch" is capability, not throughput; the thesis fails if 2027 sees no material on-ledger issuance volume.
- **Proprietary / permissioned ledger = interoperability risk.** SSDS+ is built in-house on BNM's own DLT and settles only in RENTAS+ central-bank money. That maximises control but risks a walled garden: no bridge to the private/public tokenisation stacks (Canton, Ethereum L2s, MAS/ECB rails), limiting cross-border sukuk distribution — the very frictions Malaysia's own cross-border pilots target.
- **Adoption / network risk.** A CSD rail is worthless without issuers, dealers and custodians connecting; incumbent STP flows and the legacy SSDS batch process create inertia, and nothing in the release discloses mandated migration timelines or participant count.

**What this changes (idea-lens).** `(analysis)` SSDS+ moves Malaysia from one-off pilot (Khazanah) toward a standing sovereign rail — if it becomes the default for new GII/sukuk issuance it could make Malaysia the first jurisdiction with routine, production tokenised government sukuk, a credible Islamic-finance moat vs GCC peers. Falsifiable thesis: watch for the first SSDS+-settled primary issuance and a disclosed participant count within ~2-3 quarters; absent that by mid-2027, treat SSDS+ as infrastructure signalling rather than a live market, and the "re-rating of Malaysian debt rails" thesis is wrong.

Sources: https://www.ledgerinsights.com/malaysias-central-bank-launches-depository-for-tokenized-bonds-sukuk/ · https://www.digitalnewsasia.com/digital-economy/bnm-launches-tokenised-bond-and-sukuk-platform-ssds-malaysia-advances-digital-debt · https://www.coindaro.com/bank-negara-malaysia-tokenized-bonds-ssds/ · https://www.theasianbanker.com/updates-and-articles/malaysia-s-tokenisation-pilots-target-cross-border-wholesale-frictions · https://www.khazanah.com.my/newsroom/press-releases/khazanah-leads-malaysias-first-tokenised-sukuk-pilot-in-collaboration-with-the-sc/ · https://www.futureoffinance.biz/the-european-central-bank-will-accept-eligible-collateral-in-tokenised-form-from-30-march-2026
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
