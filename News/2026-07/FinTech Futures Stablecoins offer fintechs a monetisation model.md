---
title: "FinTech Futures: Stablecoins offer fintechs a monetisation model"
date: 2026-07-13
retrieved: 2026-07-13
tags:
  - industry/stablecoins
  - industry/payments
  - region/global
  - type/commentary
sources:
  - https://app.go.informamail01.com/e/er
status: enriched
n_mentions: 1
channels:
  - "FinTech Futures"
story_id: se6e10f5f
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# FinTech Futures: Stablecoins offer fintechs a monetisation model

> [!info] 2026-07-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: FinTech Futures

## Агрегированный текст (из дайджестов)

[FinTech Futures] Fintechs cracked customer acquisition, now stablecoins are handing them a monetisation model – if they ask the right questions

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://app.go.informamail01.com/e/er>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: FinTech Futures — "Stablecoins offer fintechs a monetisation model"
_Analytical notes (not a post). Importance: 2/5._

Thought-leadership commentary (FinTech Futures, 2026-07-13): fintechs "cracked customer acquisition," and stablecoins now hand them a monetisation model — reserve yield, payments take-rate, embedded stablecoin rails — "if they ask the right questions." The single sharp, correct frame worth extracting is the **"who captures the yield"** question created by regulation. Most of the rest is generic adoption-wave narrative.

## [0] What exactly happened (de-PR'd)
No event, no numbers — it is an opinion piece. The one non-obvious, load-bearing claim is regulatory: **stablecoin ISSUERS are barred from paying interest/yield to holders**, so the reserve float yield must be captured elsewhere in the stack. That is real: GENIUS Act §4(a)(11) (signed 2025-07-18) prohibits a permitted issuer from paying "any form of interest or yield… solely in connection with holding" the coin; EU MiCA Art. 22(4) is stricter still. → Why it matters: the ban doesn't destroy the ~$300B float's yield (~$10-11B/yr gross at a 3.63% effective fed-funds rate) — it **relocates** it to whoever owns distribution. That relocation is the entire "monetisation model" the piece is selling. The vagueness ("ask the right questions") is the tell that it stops before the hard part: who *durably* keeps the margin.

## [1] Competitors / peers
The models the piece bundles together are captured by different players:
- **Issuer float (proven):** Tether >$10B net profit 2025 (~$122B direct US Treasuries); Circle ~$2.64B reserve income of ~$2.75B total revenue+reserve FY2025. Pure float monetisation, not a "fintech" play.
- **Distributor rewards (the GENIUS loophole):** PayPal pays 3.7%→~4% on PYUSD holdings — PayPal (distributor), NOT issuer Paxos, funds it. Coinbase keeps 100% of USDC reserve income on-platform + 50% elsewhere (Circle paid Coinbase $907.9M in 2024).
- **Embedded rails / orchestration:** Stripe/Bridge ($1.1B, closed 2025-02-04), Circle's platform, [[Cross River launches unified stablecoin payment platform]], [[This Week in Fintech Bridge powers money movement for fintechs (2)]].
→ Why the landscape is this way: the issuer earns the yield but **cedes most of it to whoever touches the customer** to buy distribution. Second-order: a fintech that merely resells stablecoin rails captures little; only distribution ownership captures margin.

## [2] Company history / fit
N/A — no company. The piece fits the broader 2025-26 wave already in the corpus: [[a16z report stablecoin supply tops $300 billion]] (~87% concentrated in top issuers), [[Stablecoin payments jump 70% since the GENIUS Act]] ($10B+/month, two-thirds B2B, ~$250k avg transfer), yield products like [[Figment, OpenTrade and Crypto.com partner on stablecoin yield]] (15%). The commentary adds framing, not facts, on top of these.

## [3] Novelty / value-add / traction
Genuine incremental insight is thin. The "who captures the yield" lens is correct and useful, but the piece under-delivers on the follow-through:
- **Reserve-yield capture** is durable only at the TOP of the stack (Tether, Circle, Coinbase) and is **compressing** as the Fed cuts (3.63% vs ~5% in 2024). (analysis)
- **The distributor-rewards route is under active regulatory attack** — the fact the piece appears to miss. OCC NPRM (2026-02-25) and FDIC rules (2026-04-10) create a rebuttable presumption that coordinated issuer↔affiliate yield arrangements are themselves prohibited. So the "monetisation model" rests on a loophole regulators are moving to close. (well-supported)
- **Traction check:** paying yield ≠ winning users — PYUSD market cap ~$873M, BELOW its 2024 ~$1B peak despite the 3.7% reward. The customer-acquisition premise the piece leans on is not demonstrably solved by stablecoins.
→ Who captures the margin: only the party owning distribution; pure resellers get squeezed. That reframes the piece's optimistic "fintechs get a monetisation model" into "a few distribution-owning fintechs might, if the loophole survives and rates hold."

## [4] What's next / market sentiment
Adoption momentum is real (bank entrants — sofiUSD launched 2025-12-18, JPMorgan JPMD deposit token live 2025-11-12 on Base, [[JPMorgan launches JPMD deposit token on Base]]; consortia forming). But two structural drivers cut against the thesis: (1) **falling rates** shrink the float economics; (2) **regulatory closure** of affiliate-paid yield (US) and outright stricter MiCA (EU CASP transition ends 2026-07-01). Counterintuitive second-order effect: tighter yield rules could actually *strengthen* the biggest incumbents (who monetise scale/float directly) and squeeze the mid-tier fintechs this piece is addressed to.

## Sources
- GENIUS Act §4(a)(11): https://clsbluesky.law.columbia.edu/2025/12/11/circle-coinbase-and-the-prohibition-on-interest-under-the-genius-act/ ; https://www.sidley.com/en/insights/newsupdates/2025/07/the-genius-act-a-framework-for-us-stablecoin-issuance
- OCC NPRM (2026-02-25) / FDIC (2026-04-10): https://perkinscoie.com/insights/update/stablecoin-interest-yield-and-rewards-occ-proposes-sweeping-regulations-under ; https://www.federalregister.gov/documents/2026/04/10/2026-06974/genius-act-requirements-and-standards-for-fdic-supervised-permitted-payment-stablecoin-issuers-and
- "Coinbase-shaped hole": https://www.forbes.com/sites/digital-assets/2026/05/20/the-genius-act-stablecoin-yield-ban-has-a-coinbase-shaped-hole/
- Market size / rates: https://coinlaw.io/stablecoin-market-cap-statistics/ ; https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
- Circle FY2025 / Coinbase split: https://cryptobriefing.com/circle-pays-coinbase-908m-usdc-distribution/
- Tether 2025 profit: https://tether.io/news/tether-delivers-10b-profits-in-2025-6-3b-in-excess-reserves-and-record-141-billion-exposure-in-u-s-treasury-holdings/
- PYUSD rewards: https://www.coindesk.com/markets/2025/04/23/paypal-to-pay-3-7-annual-yield-on-stablecoin-pyusd-to-encourage-broader-use
- Stripe/Bridge: https://www.cnbc.com/2025/02/04/stripe-closes-1point1-billion-bridge-deal-prepares-for-stablecoin-push-.html
- MiCA: https://blogs.law.ox.ac.uk/oblb/blog-post/2026/03/stablecoin-interest-crossroads-micas-prohibition-and-us-regulatory-maze
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is it new?** No — it is a commentary reframing of an adoption wave already in the corpus (a16z $300B supply, GENIUS-driven 70% payments jump, Bridge/Cross River rails). The "who captures the yield" frame is the only genuinely useful addition. → Fresh as a distinct analytical piece, but low incremental value.
2. **Does the piece grapple with the GENIUS yield ban's fragility?** Apparently not. It sells distributor-captured yield as "the model" while OCC (NPRM 2026-02-25) + FDIC (2026-04-10) are moving to treat coordinated issuer↔affiliate yield as itself prohibited. The model rests on a closing loophole. → open how the author treats this.
3. **Does "fintechs cracked customer acquisition" hold?** Weakly. PYUSD cap ~$873M (below 2024 ~$1B peak) despite a 3.7% reward shows paying yield does not automatically win/retain users.
4. **Reserve-yield economics — durable?** Only at issuer/top-distributor level (Tether $10B, Circle $2.64B). Compressing with rates (3.63% vs ~5% in 2024). For mid-tier fintechs: fragile.
5. **Who actually captures the margin?** The party owning distribution. Pure resellers of stablecoin-as-a-service get squeezed by orchestration layers (Stripe/Bridge, Circle).
6. **Payments take-rate thesis — evidenced?** Directionally strong (cheaper corridors) but Stripe/Bridge live volume/revenue is undisclosed. open.
7. **Embedded stablecoin-as-a-service — who wins?** Margin accrues to the orchestration/issuance layer, not to fintechs merely reselling. Bank entrants (sofiUSD, JPMD) mostly announcements vs disclosed revenue.
8. **Counterintuitive second-order effect?** Tighter yield rules may STRENGTHEN large incumbents (direct float monetisers) and squeeze the mid-tier fintechs the piece addresses.
9. **EU vs US divergence?** MiCA (Art. 22(4)) is stricter and harder to route around than GENIUS — the "distributor captures yield" model is largely a US-only phenomenon. open on whether piece is US-centric.
10. **Any exact data/thesis unique to this piece?** None surfaced beyond the generic frame; exact title/date of the FinTech Futures article could not be independently confirmed (mailer link only). open.
11. **Duplicate risk?** Substantial thematic overlap with prior notes but no identical event/figures → fresh, not a reprint.
12. **Downside trigger?** A final OCC/FDIC rule banning affiliate-paid rewards would gut the piece's central "monetisation model" overnight.
13. **Why does this matter for a reader?** Mainly as a lens ("who captures the yield") to apply to concrete deals — the piece itself carries no new facts.

Importance: 2/5 — Correct and useful central frame (regulation relocates, not destroys, reserve yield), but it is opinion with no new data, heavily overlaps existing corpus coverage, and appears to miss the key risk (regulators closing the very loophole it monetises). Fresh as a standalone analytical framing, low incremental insight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Stablecoin circulation is **~$300–320bn (mid-2026)** — trackers vary (~$303bn on 12 Jul 2026; ~$321bn mid-May), so treat the level as directional — up **~+23% YoY** and **~+93% over two years** (~$161bn Jun-2024 → ~$313bn Jun-2026) (per CoinLaw/Reap trackers; a16z pegged supply >$300bn, [[a16z report stablecoin supply tops $300 billion]]). Structure is **concentrated**: Tether (USDT) ~**59%** of supply, USDC second; entry barriers are now regulatory (charter/reserve rules) and network/distribution, not tech. The core economic engine: reserves sit in short-dated T-bills/repos and the **issuer captures the float yield** — the coin itself pays holders nothing. **Why now:** the **GENIUS Act (signed 18 Jul 2025)** made this explicit — permitted issuers **cannot pay interest/yield to holders**, reserves capped to cash/insured deposits/T-bills ≤93 days/overnight repos/govt MMFs, with monthly disclosure + audits. That legal split — issuers keep the yield, holders get none — is precisely what turns distribution into a monetisable asset for fintechs, the article's thesis (per congress.gov IF13174; Perkins Coie; EU MiCA imposes the same interest-prohibition, transitional deadline **1 Jul 2026**).

**Competitive landscape.** Sector KPIs: **circulation (float)**, **reserve yield / return rate**, **distribution cost** (share of yield paid away), on-chain volume. The fintech monetisation model has three live variants, all engineered around the yield ban:
- **Reserve-yield sharing to distributors** — the Circle↔Coinbase template: Coinbase gets **100%** of reserve income on USDC held on its platform and **50%** off-platform (agreement effective 18 Aug 2023; renews **Aug 2026**). Consortium versions — Global Dollar Network / USDG (Paxos, Robinhood, Kraken et al.) and **Open USD** (launched 30 May 2026, zero-fee mint/redeem + shared reserve returns) — formalise partner yield-sharing and directly attack the single-issuer-keeps-all model.
- **Rewards wrappers** — paid by the fintech as a separate program, not "coin interest": PayPal **PYUSD** ~3.7→4% reward (circ. ~$3.5bn May-2026); Robinhood **Earn** (1 Jul 2026) ~7% APY on USDG via Morpho/Spark to 27.7M funded customers. In-base precedents: [[Kast launches stablecoin yield product]], [[Figment, OpenTrade and Crypto.com partner on stablecoin yield]].
- **Payments take-rate & embedded rails** — Stripe/Bridge ($1.1bn, closed 4 Feb 2025); Visa (~$7bn annualised settlement run-rate by Apr-2026); Mastercard expanded stablecoin settlement (Jun-2026, incl. USDC/PYUSD/RLUSD; [[Ripple, Mastercard, WebBank and Gemini bring RLUSD settlement]]); bank/infra plays [[BNY launches stablecoin reserves fund for issuers]], [[Cross River launches unified stablecoin payment platform]], [[Klarna launches KlarnaUSD stablecoin on Tempo blockchain]]. Basis of competition is **distribution + trust/regulatory standing**, not the coin's tech — a fintech with users but no issuer can still monetise as distributor.

**Comps & multiples.** *(issuer economics, since the article is about the money model)*
- **Circle (CRCL)** Q1'26: revenue+reserve income **$694.1M (+20% YoY)**, of which **reserve income $652.5M = 94%** — i.e. issuer economics are almost entirely reserve yield; reserve **return rate 3.5%** (down YoY); USDC circulation **$77.0bn (+28% YoY)**. Market cap **$16.44bn (10 Jul 2026)**, TTM revenue **$2.86bn** → **P/S ≈ $16.44bn / $2.86bn = 5.7x** (net loss, so no P/E; margin −2.8%). EV/Rev ~5.2x. Distribution cost is the swing factor: in 2024 Circle paid Coinbase **$908M** of ~$1.01bn distribution costs. (per circle.com pressroom; SEC 8-K May-2026; stockanalysis.com)
- **Tether (USDT)** Q1'26 (BDO attestation): **net profit ~$1.04bn**, total assets **$191.8bn**, **excess reserve buffer $8.23bn (record)**; T-bill exposure ~$141bn plus ~$20bn gold + ~$7bn BTC. Private, no market cap — **valuation multiple not computed**; profitability dwarfs Circle on a fraction of the cost base (no large distribution partner). In-base: [[Circle explores native token for Arc as Q3 profit surges]], [[Circle's USDC outpaces USDT growth for second year]], [[S&P downgrades Tether's USDT stablecoin to weak]].
- **Multiple flag:** Circle P/S ~5.7x is **in-line** for a ~20–28% grower with a payments/infra profile, but the multiple rides on the reserve return rate (3.5% and falling) — the P/S is not cheap once you strip rate dependence. Distribution not computed for a peer median: only one public issuer + one private ⇒ **qualitative comparison only**.

**Risk flags.** (4)
1. **Rate-cycle dependence — the dominant risk.** Issuer revenue is ~90%+ reserve/T-bill income (Circle **94%**; return rate already fell to 3.5%). Fed cuts compress this near-linearly, and the same yield is what funds the distributor/reward payments fintechs live on — so a cutting cycle squeezes the whole monetisation stack, not just issuers. *Second-order:* fintech "monetisation model" is really a leveraged bet on the front end of the curve.
2. **Regulatory / the "distributor loophole."** GENIUS bars holder interest but is silent on affiliates/third-party rewards; banks (BPI/Clearing House) are lobbying to close it and OCC has proposed rules — if the wrapper is curtailed, the reward-based fintech model loses its legal footing. EU MiCA is stricter (interest prohibited "regardless of structure"; 1 Jul 2026 deadline).
3. **Disintermediation / margin compression.** Zero-fee, yield-sharing consortia (Open USD, GDN) and rising distributor share (Coinbase's growing USDC balance inflated Circle's distribution cost) push float yield away from issuers toward whoever owns the user — good for distributor-fintechs, corrosive for issuer margins; the **Aug-2026 Coinbase renewal** is a live catalyst.
4. **Depeg / reserve-quality & concentration.** Tether's non-Treasury reserves (~$20bn gold, ~$7bn BTC) and USDT's ~59% share are a systemic single-point risk; Tether's first full independent audit is only *underway*, not complete (S&P already rates USDT "weak", [[S&P downgrades Tether's USDT stablecoin to weak]]).

**What this changes (idea-lens).** The de-PR'd reading: "stablecoins are a monetisation model for fintechs" = fintechs monetise **distribution of someone else's float yield**, legally walled off from holders by GENIUS/MiCA — a rate-sensitive, regulation-contingent revenue line, not a durable moat. *(analysis)* Falsifiable thesis: if the Fed enters a sustained cutting cycle, per-dollar stablecoin distribution economics compress and reward APYs (PYUSD 4%, Robinhood ~7%) get cut — watch the **Aug-2026 Circle–Coinbase renewal terms** and OCC's affiliate-rewards rulemaking as the twin triggers that reprice the whole model. Wrong if payments take-rate/volume growth (Visa/Mastercard rails) grows fast enough to offset yield compression.

Sources: https://www.circle.com/pressroom/circle-reports-first-quarter-2026-results · https://stockanalysis.com/stocks/crcl/market-cap/ · https://clsbluesky.law.columbia.edu/2025/12/11/circle-coinbase-and-the-prohibition-on-interest-under-the-genius-act/ · https://www.congress.gov/crs-product/IF13174 · https://perkinscoie.com/insights/update/stablecoin-interest-yield-and-rewards-occ-proposes-sweeping-regulations-under · https://www.theblock.co/post/399722/tether-posts-over-1-billion-q1-profit-as-reserve-buffer-reaches-record-8-2-billion · https://www.cnbc.com/2025/02/04/stripe-closes-1point1-billion-bridge-deal-prepares-for-stablecoin-push-.html · https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html · https://coinlaw.io/stablecoin-market-cap-statistics/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
