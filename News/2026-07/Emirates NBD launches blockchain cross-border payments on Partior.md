---
title: "Emirates NBD launches blockchain cross-border payments on Partior"
date: 2026-07-15
retrieved: 2026-07-15
tags:
  - company/emirates-nbd
  - company/partior
  - industry/blockchain
  - region/mea
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/6ed45431
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sb3abb496
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Emirates NBD launches blockchain cross-border payments on Partior

> [!info] 2026-07-15 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Emirates NBD launches real-time blockchain cross-border payments on the Partior Network. The launch marks the first phase of a broader roadmap to expand the capability across additional currencies, settlement corridors, and more participating banks globally as the Partior network scales.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/6ed45431>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Emirates NBD launches blockchain cross-border payments on Partior
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On ~14 Jul 2026 Emirates NBD went **live** on the [[company/partior|Partior]] network for real-time, blockchain-based cross-border **USD** payments. The de-PR'd facts:
- **One currency (USD), one counterparty corridor.** The go-live rests on a single completed live USD transaction where **J.P. Morgan acted as both settlement and beneficiary bank**. So today the capability = Emirates NBD corporate/institutional clients can send real-time USD to beneficiaries **holding accounts at J.P. Morgan**. Not yet a multi-bank, multi-currency network for ENBD.
- **"First in the region" (MENAT)** — the genuinely new bit. ENBD is the first MENAT bank to move real-time USD on Partior.
- The PR's "first phase of a broader roadmap… additional currencies, settlement corridors and more participating banks" is **forward-looking / aspirational** — flag as roadmap, not shipped.

**Why framed this way / what it reveals:** the announcement leans on "real-time blockchain" and "region's first" because the *actual* live scope is narrow (USD, JPM-to-JPM beneficiary). Anchoring to "first phase of a roadmap" is the standard bank-blockchain move: launch a thin production slice, bank the PR, then expand. The load-bearing fact — JPM on both settlement and beneficiary legs — reveals this is Partior's founding-shareholder network doing what it's built for (JPM is a Partior co-founder), not ENBD plugging into a broad liquid network. Real value only materializes as more banks/currencies join.

## [1] Competitors / peers
- **JPMorgan Kinexys** (ex-Onyx) — the 800-lb gorilla: >$3T cumulative, ~$5B/day, live USD/EUR FX settlement ([[News/2026-06/Why JPMorgan built Kinexys for institutional blockchain settlements|Kinexys]], [[News/2025-11/JPMorgan Kinexys launches blockchain fund-flows tool|Kinexys fund-flows]], [[News/2026-05/Kasikornbank, Ant International launch 24 7 USD payments on Kinexys|KBank/Ant on Kinexys]]). Note the irony: JPM is both a Partior co-founder AND runs Kinexys — it hedges across both rails.
- **Fnality** — raised $136M Series C (Sep 2025); differentiates on **central-bank money** (no credit/settlement risk) vs Partior/Kinexys commercial-bank money.
- **Chainlink Project Pangea** for T+0 FX ([[News/2026-06/Chainlink and banks launch Project Pangea for T+0 FX settlement|Pangea]]); big-bank **shared tokenized-deposit network for 2027** (JPM/BofA/Citi) ([[News/2026-06/JPMorgan, BofA, Citi plan shared tokenized deposit network by 2027|shared TD network]]).
- **Partior itself**: live for USD/EUR/SGD; ~40+ institutions in MVP; roadmap USD/SGD/GBP/EUR/AUD/JPY/CNH/HKD. Prior go-lives: [[News/2025-10/Deutsche Bank completes euro cross-border payment on Partior|Deutsche Bank EUR (Oct 2025)]], Nium (first fintech PSP), NongHyup pilot ([[News/2025-12/NH NongHyup Bank pilots blockchain cross-border payments|NongHyup]]), [[News/2025-09/Partior, Finteum and Adhara enable 24 7 FX swap settlement|24/7 FX swaps]].

**Why the landscape is this way (2nd order):** Kinexys wins on volume because it's single-bank (JPM controls both ends → no coordination cost). Partior's pitch is the opposite — a **neutral, multi-bank** utility — but that same neutrality is its curse: value is fully network-effect-dependent and today most live corridors still route through JPM. The competitive question shifts from "is blockchain settlement real" (it is, at Kinexys scale) to **"can a neutral consortium rail reach critical mass before single-bank rails and the 2027 shared-deposit network eat the corridor economics."**

## [2] Company history / fit
- Emirates NBD (Dubai, ~largest UAE bank by assets) signed with Partior on **22 Oct 2024**, becoming the **first regional bank + first AED/SAR/INR settlement bank** slated for the network. July 2026 = the **go-live** of that ~21-month-old agreement (signed → live).
- Parallel track: deep [[company/nium|Nium]] tie-up (May 2024, expanded Oct 2025) for real-time MENAT payouts — ENBD is pursuing both a fintech-PSP rail (Nium) and a bank-utility rail (Partior).

**Why ENBD acts this way:** as the dominant UAE bank it wants to be the **regional settlement hub** — being the AED/SAR/INR settlement bank on a global rail is a strategic land-grab (own the corridor into the Gulf/India remittance and trade flows, one of the world's largest). Blockchain here is a means to lock in correspondent-banking relevance before stablecoins/fintech rails disintermediate it.

## [3] Novelty / value-add / traction
- **Genuinely new:** first MENAT bank live on Partior; first real-time blockchain USD out of the region. Not new: Partior go-lives themselves (DB EUR 2025, etc.) — the *mechanism* is proven.
- **Traction reality check:** what's live is thin — one currency, beneficiaries at one bank (JPM). "Programmable liquidity management" and multi-currency are **roadmap**. No ticket size, volume, or client-count disclosed → treat as production-pilot scale, not scaled adoption.

**Why value-add is real-but-limited (deeper):** the real economic value of Partior for ENBD is **intraday liquidity / trapped-cash reduction** (24/7 atomic settlement kills nostro pre-funding). But that value only compounds as *counterparties* join — with only JPM live, ENBD mostly gets a faster JPM corridor, not network liquidity. **Who captures the margin:** Partior (network fees) and the settlement banks; ENBD captures client-retention/treasury-efficiency value, not a new revenue line. The moat is the AED/SAR/INR settlement-bank role — durable **only if** ENBD onboards other banks onto those corridors before a rival (or Kinexys/stablecoins) does.

## [4] What's next / market sentiment
- **Plans:** add currencies, corridors, participating banks; ENBD to connect with other Partior banks; programmable liquidity management.
- **Sentiment:** bank-blockchain settlement is in a clear 2025-26 adoption wave (Kinexys scale, Fnality raise, 2027 shared-deposit network, Pangea). ENBD's move is directionally with the market.
- **Risks / 2nd order:** (a) **network-effect trap** — stuck as "faster JPM corridor" if peers don't join; (b) **rail fragmentation** — Kinexys, Fnality, Pangea, tokenized-deposit consortium and stablecoins all compete for the same flows, so Partior may not win the standard; (c) **JPM dual-role concentration** — JPM co-founds Partior and runs the rival Kinexys, so Partior's largest live corridor depends on a firm building the competitor. Counterintuitive: ENBD's "first-mover" edge is fragile precisely because it's currently one-corridor and single-counterparty.

## Top challenge/extra questions
See challenge file.

## Sources
- Emirates NBD press release: https://www.emiratesnbd.com/en/media-center/emirates-nbd-takes-the-lead-in-redefining-cross-border-payments-in-partnership-with-partior
- Partior: https://partior.com/news-and-insights/emirates-nbd-takes-the-lead-in-redefining-cross-border-payments-in-partnership-with-partior
- Finextra: https://www.finextra.com/newsarticle/48087/emirates-nbd-enables-blockchain-based-cross-border-payments-on-partior-network
- TechAfrica News: https://techafricanews.com/2026/07/14/emirates-nbd-launches-real-time-blockchain-cross-border-payments-on-partior-network/
- Ledger Insights (2024 partnership, AED/SAR/INR settlement bank): https://www.ledgerinsights.com/dlt-settlement-network-partior-partners-emirates-nbd-nium/
- Partior backers/currencies: https://partior.com/about-us/our-story ; https://www.coindesk.com/business/2024/07/12/partior-blockchain-payment-network-backed-by-jpmorgan-and-dbs-raises-60m-series-b
- Kinexys scale: https://www.jpmorgan.com/insights/payments/blockchain-digital-assets/introducing-kinexys
- Fnality $136M: https://www.coindesk.com/business/2025/09/23/fnality-raises-usd136m-to-expand-blockchain-payment-systems-for-banks
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **Is it really new, or activation of an old deal?** ENBD signed with Partior on **22 Oct 2024**; this July 2026 item is the **go-live** of that agreement. Fresh (a real "signed → live" milestone), NOT a duplicate of the 2024 announcement or of other Partior go-lives.

2. **What is actually LIVE vs roadmap?** Live: real-time USD, one completed transaction, JPM as settlement+beneficiary bank. Roadmap: more currencies, corridors, banks, programmable liquidity. Most of the PR is forward-looking.

3. **Is it a network or a single corridor today?** Effectively a single corridor — beneficiaries at J.P. Morgan. Not yet multi-bank liquidity for ENBD. **(open on when other counterparties go live)**

4. **Any volume / ticket size / client count?** None disclosed → assume production-pilot scale. **(open)**

5. **Why JPM on both legs?** JPM is a Partior co-founder; easiest first counterparty. Reveals reliance on founding-shareholder liquidity, not broad network.

6. **What does ENBD actually gain economically?** Intraday-liquidity / nostro-prefunding reduction + client retention — but only compounds as counterparties join. No new revenue line evident.

7. **What's the durable moat?** ENBD's role as first **AED/SAR/INR settlement bank** on Partior — durable only if it onboards other banks on those corridors before rivals/Kinexys/stablecoins.

8. **Biggest competitive threat?** JPMorgan **Kinexys** (>$3T cumulative, ~$5B/day) — and JPM co-founds Partior AND runs Kinexys (dual role = concentration risk for Partior).

9. **Partior vs Fnality mechanism delta?** Partior/Kinexys settle in **commercial-bank money** (credit/settlement risk); Fnality settles in **central-bank money** (risk-free). One sentence: Partior trades away risk-freeness for faster network onboarding.

10. **Does the 2027 shared tokenized-deposit network (JPM/BofA/Citi) undercut Partior?** Plausibly — big-bank consortium rail could capture the same interbank flows. **(open)**

11. **Who is silent about what?** No fraud-liability, fees, FX-spread, or exclusivity terms disclosed. Standard PR omissions.

12. **Did prior Partior go-lives fly?** DB completed EUR (Oct 2025), Nium onboarded, NongHyup piloted — all announced, little public volume data → adoption still early-stage.

13. **Is "region's first real-time USD via blockchain" defensible?** Likely accurate for MENAT on Partior specifically; other regional stablecoin/rail claims exist, so scope the claim to Partior. **(open on absolute-first)**

14. **Second-order fragility?** ENBD's "first-mover" edge is fragile precisely because it's one-corridor/single-counterparty; value hinges on network growth ENBD doesn't fully control.

15. **What would move importance up?** Multiple non-JPM banks live, AED/SAR/INR corridors active with disclosed volumes → then it becomes a genuine regional settlement hub (4-5/5).

**Importance: 3/5** — A genuine, verified "signed → live" milestone and a real regional first (MENAT bank, AED/SAR/INR settlement-bank role) on a serious consortium rail, which lifts it above routine PR. But the live scope is thin (one currency, JPM-to-JPM beneficiary), no volumes disclosed, and value is fully network-effect-dependent amid heavy competition (Kinexys at scale, Fnality, 2027 tokenized-deposit consortium). Directionally important, not yet material.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: blockchain-based interbank clearing/settlement rails for cross-border payments (a "shared-network" layer that sits under correspondent banking). Sizing: cross-border B2B flows are projected to exceed **$42.7tn in 2026** (from ~$34tn in 2021), and total cross-border payment flows are put at **$194tn (2024) → ~$320tn by 2032** (per Mordor/Grand View-type estimates, via aggregated 2026 sector guides — directional, secondary sources, not a single audited TAM). The value captured by rails/software is far smaller: the cross-border *payments revenue* market is ~**$238bn in 2026 → ~$336bn by 2031, ~7.2% CAGR** (per Mordor Intelligence, via cross-border-payments guides, as of 2026). Structure: fragmented at the front end (banks, PSPs) but the settlement layer is *consolidating* around a few shared DLT networks — Partior (DBS/JPM/Standard Chartered/Temasek-founded), JPMorgan's Kinexys, Fnality, plus a bank-consortium tokenized-deposit network (JPMorgan/BofA/Citi via The Clearing House, targeted mid-2027, see [[JPMorgan, BofA, Citi plan shared tokenized deposit network by 2027]]). Barriers = network effects (a settlement rail is only useful once counterparties join), bank-grade regulation, and integration cost. "Why now": stablecoins processed a claimed ~$33tn in 2025 (+72% y/y), pressuring banks to offer 24/7 real-time settlement inside the regulated perimeter rather than cede deposits to stablecoin issuers — a defensive driver behind both Kinexys and Partior adoption. `(analysis)` on the causal link.

**Competitive landscape.** Sector KPIs: on-network settlement volume (USD/day), number of participating banks, currencies/corridors live, and time-to-settle (T+0/atomic vs T+2). Key players & basis of competition (network reach + which currencies settle in central/commercial-bank money, not price):
- **Partior** (protagonist's rail) — multi-currency atomic settlement; supports USD, EUR, SGD; founded by DBS, J.P. Morgan, Standard Chartered, Temasek; strategic investors incl. Peak XV, Deutsche Bank; had processed >$1bn cumulative (as of Deutsche Bank onboarding, 2024–25, per Partior/Kapronasia). Recent moves: Deutsche Bank live EUR cross-border payment (2025-10, [[Deutsche Bank completes euro cross-border payment on Partior]]); OSTTRA/Baton FX PvP link (2025-06, [[Partior joins OSTTRA-Baton FX settlement network]]); Finteum/Adhara 24/7 FX-swap PvP (2025-09, [[Partior, Finteum and Adhara enable 24 7 FX swap settlement]]).
- **JPMorgan Kinexys** — the scale leader: >$4tn cumulative processed, **avg >$7bn/day** (per J.P. Morgan, 2026); expanding currencies + JPMD deposit token on Base ([[Why JPMorgan built Kinexys for institutional blockchain settlements]], [[JPMorgan launches JPMD deposit token on Base]]).
- **Fnality** — wholesale settlement in central-bank-backed money; raised $136M (2025-09, [[Fnality raises $136M for blockchain bank settlement]]).
- Adjacent: bank tokenized-deposit consortium ([[JPMorgan, BofA, Citi plan shared tokenized deposit network by 2027]]), stablecoin rails (Circle/Ripple).

Protagonist position: Emirates NBD is a **participant/adopter, not the rail owner** — first bank in MENAT to go live on Partior, launching real-time USD payments (per Emirates NBD/Finextra/Ledger Insights, 2026-07-14). Its first live USD transaction had **J.P. Morgan as both settlement and beneficiary bank** — i.e. today the "network" is effectively ENBD⇄JPM, single-corridor, single-currency. Emirates NBD's moat here is distribution/first-mover in the MENAT corridor, not the technology (which is Partior's). `(analysis)`

**Comps & multiples.** Private network, no public multiples; comparison is qualitative + last-round valuation:
- **Partior** — Series B raised **$80M** (led by Peak XV Jul-2024, second close w/ Deutsche Bank ~$20M, Nov-2024); **~$111M total funding**; a cited **pre-money ~$109.8M** (per PitchBook/Kapronasia — treat as round valuation, not market cap; `[UNSOURCED]` on post-money). No EV/Revenue computable — Partior does not disclose revenue; multiple = **no data**.
- **Fnality** — $136M raised (2025-09, internal comp above); valuation not disclosed → no data.
- **Kinexys** — inside JPMorgan (JPM CIK 0001652044 in IR base as `jp-morgan`, but the 8-K set carries no Kinexys segment figures → IR skipped); not separately valued.
- Distribution not computed (fewer than 3 comparable valuations disclosed; qualitative only). Read: the settlement-rail layer is still venture-stage and *capital-light relative to the flows it touches* — Partior's ~$100M-scale funding vs Kinexys' $7bn/day shows the winner-take-most network dynamic; being sub-scale vs Kinexys is the key competitive gap, not a valuation outlier.

**Risk flags.**
1. **Single-corridor / counterparty concentration (execution).** "Launch" today = real-time USD to J.P. Morgan beneficiary accounts, with JPM as settlement bank — one currency, effectively one counterparty. The de-PR'd reality is a pilot-scale go-live; the "additional currencies/corridors/banks" roadmap is unfunded promise. Second-order: value only materializes if ENBD onboards non-JPM counterparties.
2. **Dependence on someone else's rails (disintermediation of the rail choice).** Emirates NBD is a tenant on Partior, and Partior is itself sub-scale vs JPMorgan's own Kinexys (which some of the same banks use). If Kinexys or the JPM/BofA/Citi tokenized-deposit network (2027) becomes the default, ENBD's Partior bet could strand; the bank captures corridor economics, not rail economics.
3. **Regulatory / settlement-asset ambiguity.** What settles on Partior — tokenized commercial-bank deposits — carries different credit/legal treatment than central-bank money (Fnality's pitch). PR is silent on fraud liability, ticket size, and whether MENAT regulators (CBUAE) treat these as final settlement. Second-order: regulatory reclassification could cap eligible flows.

**What this changes (idea-lens).** `(analysis)` This is a *new-entry* signal, not a re-rating: MENAT's largest banks are wiring into global DLT settlement, extending the shared-rail consolidation from US/EU/SEA into the Gulf corridor. Falsifiable thesis: if Partior adds a second MENAT-outbound currency (EUR/AED) and a non-JPM counterparty within ~12 months, the corridor is real; trigger to watch = next participating-bank announcement. What breaks it: if 6–12 months on it's still USD-to-JPM only, the "launch" was a marketing pilot and the tokenized-deposit consortium / Kinexys will have out-scaled it.

Sources: https://www.emiratesnbd.com/en/media-center/emirates-nbd-takes-the-lead-in-redefining-cross-border-payments-in-partnership-with-partior · https://www.finextra.com/newsarticle/48087/emirates-nbd-enables-blockchain-based-cross-border-payments-on-partior-network · https://www.ledgerinsights.com/dlt-settlement-network-partior-partners-emirates-nbd-nium/ · https://kapronasia.com/insight/blogs/blockchain-research/asia-blockchain-research/partior-closes-its-series-b-round-having-raised-us-80-million · https://pitchbook.com/profiles/company/466428-52 · https://www.jpmorgan.com/payments/newsroom/kinexys-milestones-2026 · https://www.mordorintelligence.com/industry-reports/cross-border-payments-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
