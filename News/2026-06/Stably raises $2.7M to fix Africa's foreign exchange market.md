---
title: "Stably raises $2.7M to fix Africa's foreign exchange market"
date: 2026-06-30
retrieved: 2026-06-30
tags:
  - company/stably
  - industry/fx
  - region/africa
  - type/funding
sources:
  - https://www.connectingthedotsinfin.tech/r/27605c35
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s4e56fa38
month: 2026-06
enriched: true
importance: 2
freshness: fresh
---

# Stably raises $2.7M to fix Africa's foreign exchange market

> [!info] 2026-06-30 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇳🇬 Konga-backed stably raises $2.7m to fix Africa's broken foreign exchange market. The funding aims to eliminate the friction, slow clearing times, and fragmented counterparty reliance that currently plague cross-border African currency corridors.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/27605c35>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Konga-backed Stabyl raises $2.7M for African FX infrastructure
_Analytical notes (not a post). Importance: 2/5._

> **Name correction (load-bearing):** the newsletter says **"Stably"** — this is wrong. The company is **Stabyl** (S-T-A-B-Y-L), a new Nigerian FX-infrastructure startup. It is **NOT** the US Seattle stablecoin-as-a-service issuer **Stably (stably.io, USDS, 2018)**. Every primary source (TechCabal, BusinessDay, TechEconomy, Guardian NG, Tekedia) uses "Stabyl." The digest conflated the two names.

## [0] What exactly happened (de-PR'd)
- **The fact:** Stabyl left stealth ~2026-06-26 with a **$2.7M pre-seed led by Konga** (Nigerian e-commerce group; Zinox/Leo Stan Ekeh). Round stage = pre-seed. **Other investors, valuation, team size, HQ city — all undisclosed** (open).
- **The product (as described):** a **central limit order book (CLOB)** that matches FX orders — i.e. a shared exchange-style book replacing bilateral, bank-by-bank rate negotiation. Uses **USDT + USDC**, blockchain-agnostic; settlement via **KongaPay** (naira leg) and **DFNS** (MPC custody). Revenue = a deliberately low per-transaction take-rate; the company says it does **not** hold inventory or earn a spread (rate undisclosed).
- **Live vs announced:** only **one corridor is live — NGN/USD** — and the only named customer is **Konga**. Everything else (multi-currency expansion, more markets, licensing) is "planned." **Zero traction numbers disclosed** — no volume, no external clients, no transaction counts. This is a stealth-exit press moment, not an adoption story.
- **Why structured this way — the core red-team:** Konga is simultaneously **lead investor + first/only customer + settlement partner (KongaPay)**, and co-founder **Prince Nnamdi Ekeh is ex-Co-CEO of Konga Group** (Ekeh/Zinox family). So the raise validates a **captive, in-house anchor deal**, not open-market demand. → Why it matters: a round anchored by your own strategic backer/customer is a **low-signal** market datapoint — it de-risks distribution but tells you nothing about whether third parties will pay. → Second order: the "fix Africa's FX" framing is doing PR work over what is currently a one-corridor, one-client deployment.

## [1] Competitors / peers
The "stablecoins fix African FX" thesis is **crowded and far better capitalized** than Stabyl:
- **HoneyCoin** (Kenya) — $4.9M seed, Aug 2025 (Flourish, TLcom, Stellar Dev Fdn, Visa Ventures). **Profitable, ~$150M/mo TPV, 350 enterprises, 326k+ consumers.** See [[HoneyCoin raises $4.9 million for stablecoin cross-border payments]].
- **Flutterwave** — Ripple strategic investment in Series E at **$3.2B** valuation (Jun 2026), RLUSD/XRPL rails; separate **Tempo** stablecoin-settlement partnership (Jun 2026). See [[Ripple invests in Flutterwave's Series E at $3.2 billion valuation]] and [[Flutterwave partners with Tempo for stablecoin settlement]].
- **dLocal → AZA Finance** — ~$150M acquisition, Jun 2025; AZA billed as "Africa's largest fiat+stablecoin FX trading desk." See [[dLocal acquires AZA Finance in roughly $150M deal]].
- **3S Money founders → Express Minds** (Botswana VASP), Jun 2026 — USD-stablecoin liquidity, cross-border settlement in Southern Africa. See [[3S Money founders invest in Botswana VASP Express Minds]].
- **Conduit** — $36M Series A, May 2025 (Dragonfly, Circle Ventures, DCG), 23 African countries. **Yellow Card** — ~$85M total, Series C led by Blockchain Capital (Oct 2024), Mastercard + Visa partnerships, 20 countries. **Juicyway** — $3M pre-seed 2024.
- **Position:** Stabyl is a **late, sub-scale entrant** ($2.7M vs peers at $30–500M+). Ahead: Yellow Card / Flutterwave (scale + card-network/Ripple deals), HoneyCoin (real volume + profitability), dLocal/AZA (consolidation).
- **Why the landscape is this way (analysis):** the region's structural pain — dollar shortages, naira devaluation, fragmented multi-day corridors — is genuine, so capital and incumbents already flooded in. → The scarce resource is no longer the "idea"; it's **liquidity depth + regulatory reach + distribution**. Stabyl's only edge on those is Konga's distribution — which is captive, not a moat.

## [2] Company history / fit
- Founders Prince Nnamdi Ekeh (ex-Co-CEO Konga), Zachary Schwartzman (Oxford MBA classmate) and Michael Anyi (financial-infra engineer). Concept traced to Oxford (2021–22, founder narrative, unverifiable).
- **Why the company acts this way (analysis):** the Ekeh/Zinox/Konga lineage explains the whole structure — the family owns a large Nigerian e-commerce + payments footprint (KongaPay), which needs cheaper NGN/USD FX. Building an in-house FX exchange and funding it from Konga is a **vertical-integration play** dressed as a market startup. → It fits logically, but the "independent infrastructure for all of Africa" claim is aspirational until non-Konga volume appears.

## [3] Novelty / value-add / traction
- **Potentially novel:** the **CLOB-for-FX** angle (an order book replacing bilateral bank negotiation) is a more institutional/infra framing than the consumer-remittance crowd (Juicyway, HoneyCoin) — conceptually closer to AZA's "trading desk," but exchange-native.
- **Where it breaks (analysis):** an order book is only as useful as the **liquidity on both sides**. With one live corridor and one anchor customer, there is no evidence of a two-sided book yet. → The value-add is **unproven**: the margin in stablecoin FX is captured by whoever holds deep, multi-corridor liquidity and settlement licenses — currently the incumbents, not a pre-seed with $2.7M. → Take-rate-only, no-inventory economics is attractive in theory but implies thin margins that only work at scale Stabyl doesn't have.
- **Traction: effectively zero disclosed.** Announcement ≠ adoption.

## [4] What's next / market sentiment
- Plans: expand corridors/currencies, pursue licensing, add clients beyond Konga. All announced, none live.
- **Sentiment:** the African stablecoin-FX narrative is hot (a16z "new financial stack," multiple "This Week in Fintech: stablecoin era" pieces, Flutterwave/Ripple), so a small raise gets amplified. → **Counterintuitive second-order effect (analysis):** heavy incumbent capital (Yellow Card, Conduit, Flutterwave/Ripple, dLocal/AZA) makes the *market* validated but a *sub-scale new entrant* more fragile, not safer — liquidity and distribution concentrate with the leaders, squeezing thin-margin newcomers. Stabyl's survival likely hinges on Konga volume + the next (larger) round, not on this milestone.
- **Risks:** captive-demand dependency, no proven third-party traction, Nigerian FX/regulatory volatility, crowded field with 10–100x better-funded rivals.

## Sources
See challenge column / research brief for full URLs. Key: TechCabal (2026-06-26 stealth-exit), BusinessDay, TechEconomy (2026-06-29), Guardian NG, Tekedia; Connecting the Dots in Fintech newsletter (the digest item). Internal: [[HoneyCoin raises $4.9 million for stablecoin cross-border payments]], [[Ripple invests in Flutterwave's Series E at $3.2 billion valuation]], [[Flutterwave partners with Tempo for stablecoin settlement]], [[dLocal acquires AZA Finance in roughly $150M deal]], [[3S Money founders invest in Botswana VASP Express Minds]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_Red-team challenge questions. Importance: 2/5._

**FRESHNESS / DUPLICATE VERDICT: FRESH.** This is a genuinely new pre-seed round (Stabyl, Nigeria, ~2026-06-26). No prior corpus note covers Stabyl or this deal — the retrieved notes are *adjacent* African stablecoin-FX peers (HoneyCoin, Flutterwave, dLocal/AZA, Express Minds), not the same event. Not a reprint. Note also the name error: this is **Stabyl**, not the US company **Stably (stably.io)**.

1. **Is it Stably or Stabyl?** Stabyl (Nigerian FX-infra startup), NOT the US Stably.io. The digest headline is a misspelling. **Resolved.**
2. **Is this really new?** Yes — first-ever raise, stealth exit ~2026-06-26. Fresh. **Resolved.**
3. **How captive is the demand?** Very. Konga is lead investor + first/only customer + settlement partner (KongaPay), and co-founder is ex-Konga Co-CEO. Raise validates an in-house deal, not the open market. **Resolved — low-signal.**
4. **Any traction numbers?** None disclosed — no volume, no external clients, no txn counts. Only one live corridor (NGN/USD). **Open (implies pre-revenue).**
5. **What's the actual mechanism delta?** A CLOB (shared FX order book) vs bilateral bank rate negotiation; take-rate only, no inventory/spread. Novel framing, but unproven without two-sided liquidity. **Partially resolved.**
6. **Who else is in the syndicate, at what valuation?** Undisclosed beyond "Konga-led." **Open.**
7. **Is a CLOB useful with one corridor + one client?** No — an order book needs depth on both sides. No evidence of that yet. **Analysis: value-add unproven.**
8. **How does it compare on funding?** $2.7M vs HoneyCoin $4.9M (profitable, $150M/mo), Conduit $36M, Yellow Card ~$85M, Flutterwave $3.2B. Sub-scale entrant. **Resolved.**
9. **Who captures the FX margin in this stack?** Whoever holds deep multi-corridor liquidity + settlement licenses — currently incumbents, not a $2.7M pre-seed. **Analysis.**
10. **Does the "fix Africa's FX" claim match reality?** No — currently one corridor (NGN/USD), one client. The claim is aspirational PR. **Resolved.**
11. **Where's HQ / team size?** Undisclosed (implied Nigeria/Lagos). **Open.**
12. **Is the low-take-rate model sustainable?** Thin margins only work at scale Stabyl lacks; viable long-term only if it wins non-Konga volume. **Open.**
13. **What's the strategic logic?** Vertical integration — the Ekeh/Zinox/Konga group needs cheaper NGN/USD FX; Stabyl is an in-house exchange funded by Konga. **Resolved (analysis).**
14. **What would move this from a 2?** Live non-Konga corridors + disclosed volume + a larger priced round. **Open / watch item.**
15. **Downside triggers?** Captive-demand dependency, Nigerian FX/regulatory volatility, better-funded rivals concentrating liquidity. **Analysis.**

**Importance: 2/5** — small $2.7M pre-seed, pre-revenue, single captive corridor and anchor client (Konga = also lead investor). The thesis is real but the space is crowded and far better capitalized. Notable strategic backer + infra (vs consumer) CLOB positioning lift it from 1 to 2; not a needle-mover — a watch item.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Sub-vertical: African cross-border FX / stablecoin settlement infrastructure — "liquidity exchange" layer, not consumer remittances. Note the naming discrepancy: aggregator wrote "Stably," but the company is **Stabyl** (per TechCabal, BusinessDay, allAfrica); this is a $2.7M **pre-seed** led by Konga, out of stealth, not a priced venture round. Sector facts: global cross-border payments ~$238bn revenue in 2026 (per Mordor Intelligence, via web, as of 2026 — third-party estimate, unverified) and a widely-cited $16.5tn stablecoin cross-border TAM (per Tazapay/industry sources, `[UNSOURCED]` origin — treat as marketing, not a hard number). Real, dated drivers: (1) Sub-Saharan corridors still average >6% remittance fees (World Bank, via web), and correspondent-bank routing forces double FX conversion (naira→USD→cedi), each hop adding spread — this is precisely the friction Stabyl targets `(analysis)`. (2) "Why now": Nigeria's CBN mandated **naira settlement for all diaspora remittances from May 1, 2026** (per Punch/BusinessDay, via web) — a regulatory tailwind for local-currency settlement rails, and the exact corridor (naira↔dollar) Stabyl launches on. Structure: highly fragmented — no direct inter-African rails, USD-intermediary dependence; barriers are regulatory licensing + counterparty liquidity access, not tech.

**Competitive landscape.** Sector KPIs: settlement time (days→seconds), all-in FX spread (traditional 3–5% vs on-chain ~0.5–1%, per web), corridor coverage, and depth of accessible liquidity pools. This is a crowded, well-capitalised field. Key players / recent moves: Flutterwave took Ripple's strategic investment at a **$3.2bn valuation, Series E, 2026-06-16**, embedding RLUSD as a settlement asset [[Ripple invests in Flutterwave's Series E at $3.2 billion valuation]]; Flutterwave also partnered Tempo (2026-06-08) and standardised on Polygon (2025-10). NALA won MoneyGram (2026-04) and Noah (2026-01) settlement deals; Mastercard+Yellow Card (2026-05) covers EEMEA. Basis of competition = liquidity depth + distribution + regulatory reach, not price alone. Stabyl's position: **new entrant, sub-scale, niche** — one corridor (NGN/USD), USDT/USDC only, and its "first major commercial deployment" is captive (KongaPay naira settlement, Konga being the lead investor) `(analysis)`. Moat is thin at pre-seed: any edge is intangibles (Ekeh's Konga distribution + Oxford-founder network) and a licensing head-start, not network effects or scale. CAC/LTV/liquidity-pool depth → `[UNSOURCED]`, undisclosed.

**Comps & multiples.** Stabyl raised $2.7M pre-seed; **no valuation disclosed → post-money multiple = no data**. Comparable early-stage African stablecoin FX rounds (internal): [[HoneyCoin raises $4.9 million for stablecoin cross-border payments]] ($4.9M, 2025-08); [[3S Money founders invest in Botswana VASP Express Minds]] (2026-06, southern-Africa USD-stablecoin liquidity, undisclosed). Scale comp: [[Ripple invests in Flutterwave's Series E at $3.2 billion valuation]] — $3.2bn post-money on >$50bn cumulative TPV and >1bn transactions (per Flutterwave/TechCrunch); a crude price-to-cumulative-TPV = $3.2bn / $50bn = 0.064x, but cumulative (not annualised) TPV makes this **not a usable revenue multiple** — flagged, don't lean on it. Distribution not computed: only one disclosed valuation among comparables; qualitative comparison only. No EV/Revenue or EV/EBITDA computable for any private peer → no data.

**Risk flags.** (1) **Captive-demand / concentration risk:** lead investor Konga is also the first (only named) customer via KongaPay — early "traction" is related-party, not independent market validation; second-order effect: revenue quality overstated until external counterparties sign. (2) **Regulatory / licensing dependency:** proceeds go to "regulatory licensing" across markets Stabyl hasn't entered; the CBN naira-settlement regime is a double-edged sword — tailwind if compliant, existential if the pre-seed runway can't fund multi-jurisdiction VASP/IMTO licensing before larger players (Flutterwave, NALA, Yellow Card) lock corridors. (3) **Disintermediation by better-funded incumbents:** Stabyl sits in the liquidity-exchange layer that Flutterwave+Ripple (RLUSD) and Mastercard+Yellow Card are building in-house with balance-sheet-scale liquidity — a $2.7M entrant risks being out-capitalised on the one dimension that matters (liquidity depth).

**What this changes (idea-lens).** `(analysis)` This is a new-entrant story, not a re-rating: pre-seed capital chasing a corridor incumbents are already fortifying. Falsifiable thesis: Stabyl matters only if it signs ≥1 non-Konga tier-1 PSP/bank on the NGN/USD corridor within ~12 months AND secures a second-market license; absent that, it becomes an acqui-hire or gets crowded out. Trigger to watch: independent customer announcements and the next (priced) round valuation — a flat or down pre-seed-to-seed step would confirm the crowding-out risk.

Sources: https://techcabal.com/2026/06/26/stabyl-emerges-from-stealth-with-2-7-million-for-africas-fx-infrastructure/ · https://businessday.ng/technology/article/konga-backed-stabyl-raises-2-7m-to-fix-africas-broken-foreign-exchange-market/ · https://allafrica.com/stories/202606290026.html · https://techcrunch.com/2026/06/16/payments-startup-flutterwave-hits-3-2b-valuation-backed-by-ripple/ · https://punchng.com/naira-settlement-policy-reshapes-nigerias-remittance-landscape/ · https://www.mordorintelligence.com/industry-reports/cross-border-payments-market · https://tazapay.com/guides/stablecoins-cross-border-payments-emerging-markets
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
