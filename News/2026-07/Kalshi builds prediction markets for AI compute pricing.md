---
title: "Kalshi builds prediction markets for AI compute pricing"
date: 2026-07-14
retrieved: 2026-07-15
tags:
  - company/kalshi
  - industry/capital-markets
  - industry/ai
  - region/us
  - type/product
sources:
  - https://substack.com/redirect/7befebb1-581f-4da4-af7d-c8f6ca250763
status: enriched
n_mentions: 1
channels:
  - "MTS"
story_id: s9b3389ed
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Kalshi builds prediction markets for AI compute pricing

> [!info] 2026-07-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: MTS

## Агрегированный текст (из дайджестов)

[MTS] Kalshi is building prediction markets for AI compute. These are financial instruments that will help people understand expected future prices in order to make investment decisions, hedge, and keep price discovery. Gold, oil, wheat, and other commodities already have similar markets in traditional finance.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/7befebb1-581f-4da4-af7d-c8f6ca250763>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Kalshi builds prediction markets for AI compute pricing
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
The MTS one-liner ("Kalshi is building prediction markets for AI compute … so people can hedge and get price discovery, like gold/oil/wheat") flattens two different things into one, and the truth is less novel than the "building" framing implies:

- **Live since ~March 2026, NOT new:** Kalshi already lists tradable **binary event contracts on GPU rental prices** (e.g. `KXH100MON`: "H100 SXM compute/hour > $1.47 on Mar 31?"), settled by **Ornn AI's Ornn Compute Price Index (OCPI)**. Our own corpus confirms this predates July: the [[This Week in Fintech Semafor on the rise of an AI futures market]] note (2026-06-02) already reports "speculators on Kalshi assigning a 40% chance that Nvidia's B200 chips rent for at least $5.91 an hour this coming Friday." So the tradable product is ~4 months old.
- **What is genuinely new (2026-07-14):** Kalshi announced **"Compute Forward Curves"** — an *implied forward-price curve* (live for B200, H200, A100; note H100 is in event contracts but not the curve set) **derived from its own weekly/monthly market data**. This is a **benchmark/analytics layer, NOT a new tradable instrument** (per external research; Bloomberg 2026-07-14, news.kalshi.com/p/compute-forward-curves). You still trade the underlying binary contracts.

**Why framed this way / what it reveals:** Kalshi is positioning as "the exchange for the AI economy." The July 14 headline oversells novelty — a marketing-grade repackaging of pre-existing binary markets into a forward curve, timed alongside a ~$40B fundraise ([[Kalshi in talks to raise at $40 billion valuation]]). The "hedge like oil/wheat" analogy is aspirational: there is **zero disclosed liquidity, open interest, or named hedger** on the compute markets.

## [1] Competitors / peers
- **ICE + Ornn / Architect (Brett Harrison):** ICE (NYSE parent) inked a data deal with Ornn; ex-Jane Street/FTX-US Harrison's Architect runs a compute futures venue licensing Ornn data ([[This Week in Fintech Semafor on the rise of an AI futures market]]).
- **CME + Silicon Data (2026-05-12):** cash-settled compute futures on the Silicon Data H100 Rental Index (SDH100RT), "pending regulatory review" — likely **not yet live** vs Kalshi's live binaries. Institutional-grade, aimed away from retail ("not a casino" — Silicon Data CEO Carmen Li).
- **Polymarket:** chief prediction-market rival; ICE invested ~$2B total, targeting ~$15-20B; already uses Silicon Data prices to resolve some compute bets ([[Kalshi and Polymarket eye roughly $20 billion valuations]], [[Over $5 billion bet on World Cup across Polymarket and Kalshi]]).
- **Ornn itself** runs a "Compute Exchange" + indices — simultaneously Kalshi's oracle AND a potential competing venue (dependency + conflict).

**Position / why:** Kalshi is **first-to-live on retail-accessible binary compute contracts** but is the **low-institutional-credibility** entrant vs CME/ICE, who own the commercial-hedger relationships. The Semafor note's structural warning applies directly: compute is an oligopoly (Nvidia + hyperscalers) that "benefit from opaque pricing"; without CoreWeave/Meta/Google as commercial hedgers you get "gambling, not price discovery." Kalshi's edge is distribution/retail, exactly the wrong edge for a real hedging market.

## [2] Company history / fit
Kalshi's trajectory is a relentless push from retail betting toward "the new Wall Street": $2B (Jun 2025, [[Kalshi raises $185M at $2bn valuation]]) → $11B (Jan 2026, [[Kalshi raises $1bn at $11bn valuation]]) → $22B (May 2026, [[Kalshi raises $1 billion Series F at $22 billion valuation]], institutional volume +800%, annualized volume $52B→$178B) → ~$40B raise in progress ([[Kalshi in talks to raise at $40 billion valuation]]), $2B annualized revenue and early IPO talks ([[Kalshi passes $2 billion annualised revenue, in early IPO talks]]). ~91% US prediction-market share ([[Kalshi holds 91% of US prediction market, BofA data shows]]).

**Why it acts this way (structural logic):** ~90% of volume is sports — a category with regulatory/legal fragility (Arizona criminal charges, adverse MD/MA rulings; [[Minnesota becomes first US state to ban prediction markets]], [[Spain blocks prediction markets Polymarket and Kalshi]]). To justify a $40B valuation and de-risk the IPO story, Kalshi **needs a defensible institutional line that isn't gambling.** Compute contracts are the ideal narrative: a "real commodity," CEA-friendly (see [4]), and adjacent to its explicit institutional courtship ([[Kalshi courts Susquehanna and Jump Trading as prediction market hedging tool]] — Susquehanna, Jump, Greenlight Commodities, FalconX). The July 14 forward curves are a fundraise-timed proof point that the "AI economy exchange" thesis is real.

## [3] Novelty / value-add / traction
- **Genuinely new:** an *implied forward curve* published from live prediction-market prices (a "market-backed" alternative to index-only curves like Silicon Data / Ornn). That framing is a modest differentiator.
- **Not new:** the underlying tradable binary GPU markets (live since ~March 2026 per corpus + external).
- **Traction: unverified.** No published open interest, volume, or named commercial hedger on compute markets. Mansour's claim that compute futures could "dwarf" oil is aspirational.

**Why value-add is thin / who captures the margin (2 levels deep):** The whole edifice settles to **Ornn's OCPI** — a seed-stage startup ($5.7M raised, Oct 2025, 8 employees) whose own risk disclosure concedes data "could be inaccurate" and warns of material **basis risk** (region/quality dispersion). So: (1) **Oracle single point of failure + reflexivity** — Kalshi's forward curves derive from Kalshi markets that resolve to Ornn; the "wisdom of crowds" is really "wisdom of an index built from parsed neocloud invoices." (2) **Basis risk kills the real hedge** — a CoreWeave hedge on OCPI-H100-SXM won't offset its actual fleet economics, and the big-contract prices (Google/Meta) are closed, so the index only sees volatile neocloud spot. (3) **Margin capture:** the durable value in this stack is the **benchmark/index** (Ornn, Silicon Data) and the **commercial-hedger orderflow** (CME/ICE), not the retail binary venue. Kalshi risks being the "casino" wrapper while the index owner and the institutional exchange capture the franchise — the central question shifts from "is Kalshi building the compute futures market?" to "does Kalshi own anything durable here, or is it renting Ornn's index to decorate a fundraise?"

## [4] What's next / market sentiment
- **Regulatory:** Kalshi is the only CFTC-registered DCM; compute-price contracts self-certify cleanly under CEA Rule 40 (commodity-price format) — **the low-risk part of Kalshi's book**, unlike its sports/politics fights (Arizona 20-count criminal information Mar 2026; adverse Maryland/Massachusetts rulings; but 3rd Circuit affirmed injunction Apr 2026). CFTC issued a revised Rule 40.11 event-contracts proposal (Jun 2026).
- **Sentiment:** BlackRock's Fink called compute "a new asset class"; DRW's Don Wilson bullish. But the sober counter (Semafor's Liz Hoffman, [[This Week in Fintech Semafor on the rise of an AI futures market]]): without oligopolist commercial users, no price discovery — just financialized betting. Lex debates whether the valuations are even justified ([[Lex Are prediction-market valuations for Kalshi and Polymarket justified]]).
- **Counterintuitive second-order effect:** the more Kalshi leans on "compute futures = trillion-dollar market" to justify $40B, the more fragile it becomes if the market stays a thin retail casino — the valuation narrative is doing more work than the product. Also: GPU prices are volatile in BOTH directions (H100 up 63% in a month per Ornn, yet down 60-75% from peak), so there IS real two-sided risk — the question is whether commercial hedgers ever show up, and CoreWeave *not* having a compute-trading desk suggests slow takeup.

## Sources
- Note (target): News/2026-07/Kalshi builds prediction markets for AI compute pricing.md (MTS, 2026-07-14)
- Kalshi Compute Forward Curves: https://news.kalshi.com/p/compute-forward-curves
- Bloomberg (2026-07-14): https://www.bloomberg.com/news/articles/2026-07-14/kalshi-ramps-up-effort-to-build-markets-for-ai-computing-power
- Live H100 market: https://kalshi.com/markets/kxh100mon
- DataCenterDynamics (Ornn/March launch): https://www.datacenterdynamics.com/en/news/kalshi-users-able-to-gamble-on-nvidia-gpu-compute-prices-based-on-ornns-compute-derivatives-platform/
- CME + Silicon Data: https://www.cmegroup.com/media-room/press-releases/2026/5/12/cme_group_and_silicondatapartnertolaunchfirstcomputefutures.html
- Ornn Index / risk disclosure: https://www.ornnai.com/research/the-ornn-index-s-p-500-for-accelerated-compute ; https://www.ornnai.com/risk-disclosure-statement
- CoinDesk $40B target: https://www.coindesk.com/business/2026/06/24/kalshi-targets-a-massive-usd40-billion-valuation-widening-lead-over-rival-polymarket
- Semafor (theme): https://www.semafor.com/article/05/26/2026/the-future-of-ai-is-an-ai-futures-market
- Internal: [[This Week in Fintech Semafor on the rise of an AI futures market]], [[Kalshi courts Susquehanna and Jump Trading as prediction market hedging tool]], [[Kalshi raises $1 billion Series F at $22 billion valuation]], [[Kalshi in talks to raise at $40 billion valuation]], [[Lex Are prediction-market valuations for Kalshi and Polymarket justified]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5** — Real, live product tied to a hot theme (AI compute financialization) and to Kalshi's $40B fundraise narrative, giving it genuine weight. But docked because: (a) the core tradable contracts already existed since ~March 2026 (the June 2 Semafor theme note already flagged live Kalshi compute bets), so the July 14 "forward curves" is an analytics/marketing layer, not a new venue; (b) zero disclosed liquidity, OI, or named hedger — traction unverified; (c) it settles entirely to a seed-stage startup's index. Notable but not a 4/5 structural shift.

**Freshness: fresh** — This is Kalshi's OWN, company-specific July 14 product announcement (Compute Forward Curves + ongoing GPU event contracts), distinct from the June 2 thematic overview [[This Week in Fintech Semafor on the rise of an AI futures market]], which was a market-wide piece (ICE/CME/Ornn/Silicon Data/Architect) that merely mentioned Kalshi in passing. Not a reprint of the same event or figures → fresh, but heavily thematically overlapping (cite the Semafor note as predecessor). No duplicate_of.

**Red-team questions:**
1. Is the July 14 product actually new? — **Partly.** The Compute Forward Curves benchmark is new (2026-07-14); the underlying tradable binary GPU markets are ~4 months old (live since ~March 2026, corpus-confirmed via the B200 bet in the Semafor note).
2. Are the forward curves tradable? — **No.** Benchmark derived from existing binary markets; you trade the underlying weekly/monthly contracts. Headline oversells.
3. What settles the contracts? — **Ornn's OCPI** (H100 SXM = ORNNH100), Asian-style VWAP of parsed transactions.
4. Any disclosed volume/OI/liquidity on compute markets? — **Open / none disclosed.** Major red flag for a "hedging" claim.
5. Any named commercial hedger (CoreWeave, Lambda, Crusoe, Nebius)? — **Open / none named.** Semafor notes CoreWeave lacks a compute-trading desk → slow takeup.
6. Who is live first vs CME/ICE? — **Kalshi (binaries since March).** CME+Silicon Data "pending regulatory review"; likely not yet live mid-July.
7. Does the oracle create single-point-of-failure/reflexivity? — **Yes.** Ornn is seed-stage (8 staff, $5.7M); Kalshi curves derive from Kalshi markets resolving to Ornn — circular.
8. Basis risk for a real hedger? — **Material.** Ornn's own disclosure concedes region/quality dispersion; index only sees volatile neocloud spot, not closed Google/Meta contracts.
9. CFTC pushback risk on compute contracts specifically? — **Low.** Commodity-price format self-certifies cleanly; the legal heat is on sports/politics (Arizona criminal charges, MD/MA losses).
10. Is this token/inference pricing too? — **Not on Kalshi yet.** Ornn launched token indices; Kalshi's live markets are GPU-hour. Token markets = plausible next step, open.
11. Manipulation risk on thin markets? — **Yes.** Low-OI binaries + a startup index from parsed invoices are gameable at both layers.
12. Is the fundraise timing coincidental? — **(analysis) No.** Announced alongside the ~$40B raise; serves the "AI-economy exchange, not a casino" IPO narrative.
13. Who captures the durable margin in the stack? — **(analysis)** The index (Ornn/Silicon Data) and the institutional exchange (CME/ICE) — Kalshi risks being the retail wrapper. Central question shifts from "is Kalshi building this market" to "does Kalshi own anything durable here."
14. Does real two-sided price risk exist to justify a market? — **Yes.** H100 +63% in a month yet -60-75% from peak; genuine volatility. But volatility ≠ commercial-hedger demand.
15. Is "compute dwarfs oil futures" credible? — **Unsubstantiated / aspirational.** No volume evidence; hinges on oligopolists (Meta/Google) participating, which they have incentives NOT to (they benefit from opaque bundled pricing).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Two adjacent markets meet here: (a) prediction / event-contract exchanges (Kalshi's core), and (b) an emerging **compute-as-a-commodity** derivatives layer. On the event-contract side the category is a US-centred duopoly (Kalshi + Polymarket) whose demand engine in 2026 has been sports (World Cup, NBA) — no credible sized TAM, so treat "size" as run-rate volume (Kalshi annualized trading volume rose $52bn→$178bn in six months to early May-2026; per corpus [[Kalshi passes $2 billion annualised revenue, in early IPO talks]]). On the compute side, the "why now" is a genuinely new commodity: the cost to rent Nvidia's top chips is volatile enough to sustain a two-sided market — Ornn's data shows the H100 up ~63% in one month, and B200 hourly rental peaked ~$6.11 (2026-05-30) then fell ~30% to ~$4.22 by 2026-06-21 (per Semafor 2026-05-26, [[This Week in Fintech Semafor on the rise of an AI futures market]]; CNBC 2026-06-22). BlackRock's Fink has called compute "a new asset class"; boosters analogise it to the ~$6tn energy market and to WTI/Brent oil becoming benchmarks. Structure of the compute layer is **contested and unbuilt**: the natural hedgers (hyperscalers Google/Meta) benefit from opaque bundled pricing and are absent, so without commercial users it risks being "price discovery you have… or gambling" (Don Wilson/DRW, Semafor). Entry barriers: regulation (CFTC registration) + a credible, manipulation-resistant settlement index + liquidity network effects.

**Competitive landscape.** Sector KPIs: notional volume, taker-fee/take-rate (~1.1% at Kalshi), annualized-revenue run-rate, and — for compute — **index credibility** (who owns the settlement price). On compute pricing specifically, this is a **land-grab of the pricing benchmark, not just a listing**:
- **Kalshi** — already runs LIVE event contracts on hourly GPU rental prices (H100/H200/B200/RTX 5090), resolving on **Ornn AI's** compute index; on 2026-07-14 it added "compute forward curves" (B200/H200/A100) built from its own market trades — a benchmark, not itself a new tradeable (per Kalshi/Businesswire 2026-07-14; DataCenterDynamics 2026-03-04). CEO framing: "compute is the new oil."
- **CME Group + Silicon Data** — announced 2026-05-12, GPU-rental-index futures "later this year, pending regulatory review." ANNOUNCED, not live.
- **ICE + Ornn** — announced GPU compute futures on the Ornn Compute Price Index (OCPI), power-style Asian settlement. ANNOUNCED. (Note: ICE also holds ~23% of Polymarket.)
- **Architect** (Brett Harrison, ex-FTX US) + Ornn — planned exchange-traded **perpetuals** on GPU/DRAM prices (2026-01). ANNOUNCED.
- **MNX** — $6.4m pre-seed at $40m val (Village Global), decentralized AI-economy perps (compute, AI-lab valuations, electricity) on MegaETH, private beta ([[MNX raises $6.4 million pre-seed for AI-economy futures exchange]]).

Position: Kalshi is **first-live** with a working retail compute-price market while CME/ICE/Architect's institutional futures are all still "announced/pending." That is a real head-start on liquidity and mindshare `(analysis)`, but Kalshi's product is retail event contracts, not the commercial hedging instrument (CoreWeave-style desks) that would confer a durable moat — and it depends on **Ornn's** third-party index, not a proprietary one.

**Comps & multiples.** No standalone valuation attaches to the compute product; comps are the parent/peer set (private, round valuations, not market cap):
- [[Kalshi in talks to raise at $40 billion valuation]] (2026-06) — at ~$2bn run-rate revenue: EV/Rev = `$40bn / $2bn = 20x`.
- [[Kalshi raises $1 billion Series F at $22 billion valuation]] (2026-05) — at ~$1.5bn est. revenue then: EV/Rev = `$22bn / $1.5bn ≈ 14.7x`.
- [[Polymarket annualized revenue tops $1 billion]] (2026-07) + ~$15bn round talks: EV/Rev = `$15bn / $1bn = 15x`.
- Trajectory: [[Kalshi raises $185M at $2bn valuation]] (2025-06) → [[Kalshi raises $1bn at $11bn valuation]] (2026-01) → $22bn (May-26) → $40bn talks — an 20x valuation step in ~12 months.
- Sports-betting reference: DraftKings/Flutter trade ~3–5x sales — the ~15–20x prediction-market multiple only holds if these are "exchanges," not "regulated gambling." P/E, EV/EBITDA `[UNSOURCED]` (private, no margins). Verdict: **in-line within the duopoly (~15–20x) but rich in absolute terms**, on unseasoned, World-Cup-flattered run-rate revenue; the compute product adds optionality but no near-term revenue you can size ("no data").

**Risk flags.**
1. **Compute market may not clear (product-specific, highest for this pick).** The natural hedgers (hyperscalers) benefit from opaque bundled pricing and are absent; without commercial users, compute contracts stay a retail casino rather than a price-discovery venue — so the "next oil" thesis may not materialise into durable volume. Second-order: Kalshi's first-mover lead is on retail flow, the least defensible slice if institutional futures (CME/ICE) capture the commercial hedgers.
2. **Settlement-index dependence & manipulation.** Contracts resolve on **Ornn's** third-party index, itself built from volatile "neocloud" spot prices (Crusoe/Nscale) with no access to the big Google/Meta contracts. Thin/opaque underlying data is both a data-quality risk and a manipulation/resolution-dispute vector on a CFTC-registered venue.
3. **Regulatory binary on the parent (still the dominant swing factor).** ~85–90% of Kalshi revenue is sports; CEA-preemption is favorable (3rd Cir. 2026-04) but unsettled — Minnesota's outright ban is a state felony from 2026-08-01 (CFTC/DOJ suing), 40-state amicus and tribes opposing, and ex-CFTC chair Gensler filed an amicus against CFTC preemption (2026-06-12). A reversal would gut the revenue base that funds the compute R&D and the ~20x multiple.

**What this changes (idea-lens).** `(analysis)` This is Kalshi trying to move from "regulated sports gambling" toward "financial-infrastructure / new asset class" — a re-rating narrative that justifies its exchange-like multiple. Falsifiable thesis: if compute becomes a real commodity market, expect (i) a commercial hedger (a CoreWeave/neocloud) to actually trade Kalshi/CME/ICE compute contracts, and (ii) CME or ICE to launch LIVE GPU futures in 2026. What breaks it: no hyperscaler/commercial participation by end-2026 and compute volume staying purely retail/speculative — then this is a marketing lane, not a market. Triggers to watch: first live institutional GPU future (CME/ICE), any hyperscaler or neocloud hedging desk, and Q3-2026 post-World-Cup volume prints on the core book.

Sources: https://news.kalshi.com/p/compute-forward-curves · https://www.semafor.com/article/05/26/2026/the-future-of-ai-is-an-ai-futures-market · https://www.datacenterdynamics.com/en/news/kalshi-users-able-to-gamble-on-nvidia-gpu-compute-prices-based-on-ornns-compute-derivatives-platform/ · https://www.cmegroup.com/media-room/press-releases/2026/5/12/cme_group_and_silicondatapartnertolaunchfirstcomputefutures.html · https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Announces-New-600-Million-Investment-in-Polymarket/default.aspx · https://www.coindesk.com/business/2026/06/24/kalshi-targets-a-massive-usd40-billion-valuation-widening-lead-over-rival-polymarket · https://www.coindesk.com/policy/2026/06/12/former-sec-cftc-chair-gary-gensler-argues-that-prediction-markets-don-t-overrule-state-regulations
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
