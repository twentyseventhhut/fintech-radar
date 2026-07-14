---
title: "Aave advances automated buyback under Aavenomics 3.0"
date: 2026-07-14
retrieved: 2026-07-14
tags:
  - company/aave
  - industry/defi
  - region/global
  - type/product
sources:
  - https://substack.com/redirect/4e74813b-3292-4852-9b02-7d05c456459a
status: enriched
n_mentions: 1
channels:
  - "lex"
story_id: sdafcc844
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Aave advances automated buyback under Aavenomics 3.0

> [!info] 2026-07-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: lex

## Агрегированный текст (из дайджестов)

[lex] Aave Advances Automated AAVE Buyback Overhaul With Aavenomics 3.0 - The Defiant

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/4e74813b-3292-4852-9b02-7d05c456459a>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Aave advances automated buyback under Aavenomics 3.0
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS VERDICT: FRESH.** No prior corpus note covers Aave tokenomics / the AAVE buyback / GHO fee mechanics. The Aave notes in the vault cover adjacent-but-distinct events: [[Aave reaches $50 billion in net deposits]] (TVL milestone, 2025-07), [[Aave Labs launches high-yield savings app]] (product, 2025-11), [[Kraken in talks to buy 15% Aave stake at $385M]] (M&A, 2026-06), [[Mastercard partners with Aave for agentic payments]] (partnership, 2026-06), and the [[KelpDAO exploit drains funds from Aave DeFi vaults]] (security, 2026-04). "Aavenomics 3.0 / automated buyback" is a NEW governance/tokenomics development, not a re-report. NB it directly connects to the Kraken note — Kulechov previewed 3.0 (Jun 26) partly to rebut the "70% discount" framing of the Kraken stake by stressing that ALL protocol revenue accrues to the token, not to Labs equity.

## [0] What exactly happened (de-PR'd)
Aave co-founder Stani Kulechov previewed **"Aavenomics 3.0"** on X (~Jun 26, 2026): an **automated, non-discretionary, "immutable" on-chain mechanism** that routes protocol + GHO revenue to AAVE holders continuously, replacing the *discretionary, committee-approved-per-cycle* buyback that had run since Apr 2025. The lex/Defiant headline says "**Advances**" — and that verb is load-bearing.
- **De-PR'd reality — this is a proposal/direction, not verified codified code.** Sources conflict sharply: The Defiant's own "Advances" piece plus cryptonews.net (Jun 27) and CryptoDaily (Jul 5) describe 3.0 as a **preview/proposal** with "implementation mechanics and governance timeline expected at Aave's next quarterly call" and "a spec, testing, a DAO vote, and staged activation" still pending. A separate camp (some Defiant/aggregator pieces) reports a Jun 27 "activation." **Treat "fully automated on-chain buyback is live and codified" as OPEN/unconfirmed.** What IS DAO-backed: the *direction* — the "Aave Will Win" proposal (passed Apr 2026) already routes 100% of Aave-product + GHO revenue to the DAO treasury.
- **+ Why framed this way / what it reveals:** the "automated/immutable" framing is doing PR work. The real-world pace contradicts the "100% of revenue" implication — reported buybacks run at **~292 AAVE/day (~$28k/day, ~$10M/yr run-rate)**, and the DAO *cut* the buyback budget from **$50M/yr → $30M/yr in Mar 2026** citing a 25% drop in borrow-fee revenue. So "route 100% of ~$400M revenue to buybacks" (aspiration) vs ~$10-30M/yr actual (reality) is a ~10-40x gap that no source reconciles. The word "advances" + a quarterly-call timeline = an announcement being priced as if it were a shipped, revenue-scaled machine.

## [1] Competitors / peers — the DeFi buyback/fee-switch wave
This is the central "why it matters" frame: 2025-26 is the year DeFi majors turned on value accrual. Dated peers:
- **Hyperliquid (HYPE):** Assistance Fund buys ~97% of fees, genuinely automated, **~$2M/day**; fund holds ~45.6M HYPE (~$3.19B). The benchmark. (cf. [[Paxos proposes USDH stablecoin for Hyperliquid with HYPE buybacks]], [[Hyperliquid expands event contracts to macro events]]).
- **Sky (ex-Maker, SKY):** Smart Burn Engine, ~$1M/day burn, $102M in 2025 (burn, not distribute).
- **Uniswap (UNI):** "UNIfication" fee switch passed Dec 2025, 100M UNI (~$596M) burned upfront — yet UNI still hit a cycle low.
- **Jupiter (JUP):** ~$70M spent 2025, covered only ~6% of unlocks; JUP -89% from peak — the cautionary case.
- **Pump.fun (PUMP):** burned ~$370M — price still failed to lift.
- **+ Why the lay of the land / second-order:** the empirical lesson from JUP/UNI/PUMP is that **buybacks alone don't hold price** when they're small vs sell pressure/unlocks. Aave's ~$10-30M/yr on a ~$1.5B mcap is **~1-2%/yr** — an order of magnitude below Hyperliquid's ~$2M/day. So Aave is **catching up on the mechanism but sub-scale on the magnitude**. The differentiator it can credibly claim is not size but that its revenue is *real lending/GHO cash flow* (~$400M annualized DefiLlama, all-time fees >$2.2B), not speculative trading fees like a perp DEX or launchpad.

## [2] Company history / fit
Trajectory: Aavenomics **TEMP CHECK Jul 2024** → approved Aug 2024 ("fee switch on steroids") → "Part one" ARFC Mar 2025 authorizes **$1M/week** → **first buyback Apr 2025** → ACI proposes permanent $50M/yr adaptive $250k-$1.75M/week (Oct 2025) → "Aave Will Win" 100%-revenue-to-DAO (Apr 2026) → 3.0 preview (Jun 2026). Staking overhaul in parallel: **Umbrella** Safety Module (Jun 2025), **Anti-GHO** (>50% of GHO revenue, 80% stkAAVE / 20% stkBPT), **sGHO** migration.
- **+ Why the company acts this way:** Aave is a mature, cash-generative protocol (~$12.5B TVL, ~$50B deposits historically) whose token had **no direct claim on that cash** for years — a classic DeFi value-accrual gap. The buyback + Anti-GHO exist to convert protocol earnings into token-holder value, i.e. give AAVE a "software-multiple" narrative rather than a pure governance token. The Kraken episode sharpened this: Kulechov needed to publicly assert that value lives in the TOKEN (all protocol revenue → AAVE) to reject the Labs-equity "discount," so 3.0 doubles as a positioning move.

## [3] Novelty / value-add / traction
- **What's genuinely new:** moving from *discretionary committee* buybacks to a *formulaic/automated* one — removes human timing discretion and signals credibility. Cumulative traction to date: **>205,000 AAVE bought back (~1.28% of supply)** since Apr 2025 — real, but modest.
- **+ Why the value-add is real-but-thin, one level deeper:** (a) it's a **distribution, not a burn** — value accrues disproportionately to **stakers (stkAAVE/stkBPT via Anti-GHO)** over passive holders; it may partly *offset emissions* rather than net-shrink supply. (b) It's **pro-cyclical** — buys most when fees (and price) are high, least in drawdowns, so it's weakest exactly when support is most needed. (c) Materiality is marginal: ~1-2%/yr of mcap. (d) **Execution/override risk:** the prior buyback was **suspended Apr 19 2026** after the KelpDAO exploit left bad debt — direct evidence the "automated/immutable/continuous" claim has a manual-halt precedent. Who captures the margin: stakers who lock AAVE, at the cost of the Safety Module if 100%-to-buyback starves reserves.

## [4] What's next / market sentiment
Next hard checkpoint: the **quarterly call** where 3.0's mechanics, spec, DAO vote and staged activation are due. Until then the market is pricing "a commitment in writing but not codified to the last clause" (CryptoDaily). GHO ~$598M circulating; DAO simultaneously *raised* opex ($142M 2025 → $190M 2026 budget) while cutting buyback ($50M→$30M) — preserving ~$20M/yr reserves.
- **+ Why / counterintuitive second-order:** routing 100% of revenue to buybacks could **starve the Safety Module (Umbrella)** and raise tail risk right as Aave rebuilds trust post-KelpDAO — a "value accrual" move that quietly increases fragility. And because it's pro-cyclical and sub-scale, the buyback is unlikely to be the swing factor for AAVE price; the real drivers remain TVL recovery, GHO growth, and whether the Kraken/strategic-investor overhang resolves. The honest read: 3.0 is a credible *governance-maturity* signal, not a price catalyst.

## Top challenge/extra questions (10-15, second-order)
1. Is 3.0 **live and codified**, or a founder preview pending a quarterly-call vote? — **OPEN; sources conflict.** Headline verb "advances" + "next quarterly call" timeline lean toward *proposal*.
2. How is "100% of ~$400M revenue → buyback" reconciled with the reported **~292 AAVE/day (~$10M/yr)** pace? — **OPEN, ~10-40x gap unexplained.**
3. Is the $400M revenue figure real? — DefiLlama 7-day annualized, volatile, not audited; all-time fees >$2.2B is more solid.
4. Is the buyback **material** vs mcap? — No: ~1-2%/yr of ~$1.5B mcap; below Hyperliquid/Sky by an order of magnitude.
5. Burn or distribute? — **Distribute** (buy-and-distribute to stakers via Anti-GHO), so supply reduction is weaker than a burn.
6. Who benefits — stakers or passive holders? — Stakers (stkAAVE/stkBPT); passive holders benefit less.
7. Does it offset emissions or net-reduce supply? — Likely partial offset; net effect unconfirmed (analysis).
8. Pro-cyclicality risk? — Yes, buys least in drawdowns; "won't offset heavy selling" (CryptoDaily).
9. Does 100%-to-buyback **starve the Safety Module**? — Flagged as a real tail-risk tradeoff.
10. Is "automated/immutable" contradicted by precedent? — Yes: buyback **suspended Apr 19 2026** post-KelpDAO — manual override exists.
11. Is this a Kraken-stake defensive move? — Plausibly: Kulechov used 3.0 to rebut the "70% discount" on the Labs stake (all revenue → token). (analysis)
12. How does it compare to peers' outcomes? — JUP/UNI/PUMP show buybacks alone don't hold price when sub-scale.
13. What's the GHO contribution to the revenue backing? — ~$598M circulating supply; incremental, not dominant.
14. Does the DAO budget support it? — Mixed: opex UP ($142M→$190M), buyback DOWN ($50M→$30M); reserves ~$20M/yr.
15. What's the real catalyst for AAVE? — TVL/GHO recovery + strategic-investor resolution, not the buyback itself.

## Sources
- The Defiant — "Aave Advances Automated AAVE Buyback Overhaul With Aavenomics 3.0" (primary, via lex).
- The Defiant — "Aave Confirms Aavenomics 3.0 Live: Buybacks, DAO Spending Cut" (conflicting status).
- CryptoDaily (2026-07), cryptonews.net (2026-06-27), Blockonomi/BanklessTimes (2026-06-26 Kulechov X preview).
- governance.aave.com (Aavenomics ARFC), The Block, Cryptopolitan/Cryptorank (Apr 2025 first buyback), CoinDesk/DLNews (Oct 2025 $50M proposal).
- Peers: DexTools/Tokenomics.com (Hyperliquid), Tokenomics.com (Sky), The Defiant/KuCoin (Uniswap UNIfication), crypto.news (Jupiter), CoinMarketCap (Pump.fun).
- Internal: [[Kraken in talks to buy 15% Aave stake at $385M]], [[KelpDAO exploit drains funds from Aave DeFi vaults]], [[Mastercard partners with Aave for agentic payments]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team challenge questions

1. **Is 3.0 live or just proposed?** OPEN — sources conflict. The headline verb "advances" plus "mechanics/timeline expected at next quarterly call" (CryptoDaily, cryptonews.net) point to a founder PREVIEW/proposal, not codified live code. Treat "automated on-chain buyback is live" as unconfirmed.
2. **Does "100% of ~$400M revenue → buyback" match reality?** No. Reported pace is ~292 AAVE/day (~$10M/yr) and the DAO cut the budget $50M→$30M/yr in Mar 2026. A ~10-40x gap between framing and execution, unreconciled by any source.
3. **Is the $400M revenue figure trustworthy?** It's DefiLlama 7-day-annualized — volatile, not audited. All-time fees >$2.2B is the sturdier number.
4. **Is the buyback material vs market cap?** No — ~1-2%/yr of ~$1.5B mcap; roughly an order of magnitude smaller than Hyperliquid (~$2M/day) and Sky (~$1M/day).
5. **Burn or distribute?** Distribute (buy-and-distribute to stakers via Anti-GHO), so supply reduction is weaker than an outright burn.
6. **Who actually benefits?** Stakers (stkAAVE / stkBPT), not passive holders — value accrual is conditional on locking.
7. **Does it net-reduce supply or just offset emissions?** Likely partial offset; net-deflationary effect is unconfirmed (analysis).
8. **Pro-cyclicality?** Yes — buys most when fees/price are high, least in drawdowns; "won't offset heavy selling."
9. **Does routing 100% to buybacks starve the Safety Module (Umbrella)?** Flagged as a genuine tail-risk tradeoff, especially post-KelpDAO.
10. **Is "automated/immutable" contradicted by precedent?** Yes — the buyback was suspended Apr 19 2026 after the KelpDAO exploit; manual override exists.
11. **Is this partly a defensive move around the Kraken stake?** Plausible — Kulechov used 3.0 (Jun 26) to rebut the "70% discount" framing by asserting all protocol revenue accrues to the token, not Labs equity. Connects to [[Kraken in talks to buy 15% Aave stake at $385M]].
12. **What do peer outcomes teach?** JUP (-89%), UNI (cycle low despite $596M burn), PUMP — buybacks alone don't hold price when sub-scale vs sell pressure/unlocks.
13. **How big is the GHO contribution to the revenue backing?** ~$598M circulating supply; incremental, not the dominant driver.
14. **Does the DAO budget actually support this?** Mixed signal — opex raised ($142M→$190M) while buyback cut ($50M→$30M); ~$20M/yr reserves preserved.
15. **What's the real catalyst for AAVE?** TVL/GHO recovery and resolution of the strategic-investor overhang — not the buyback itself.

Importance: 3/5 — A real, DAO-backed governance/tokenomics maturation by DeFi's largest lender, riding the 2025-26 buyback/fee-switch wave (Hyperliquid, Sky, Uniswap). But it is a "advances/preview" (status contested), sub-scale (~1-2%/yr of mcap), pro-cyclical, and a distribution rather than a burn — a credibility signal more than a price catalyst. Above a routine PR item (novelty + real cash-flow backing + trend relevance), below a market-moving event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** DeFi lending / tokenomics ("real-yield" value accrual). Aave is DeFi's largest lending protocol: TVL ~$12.5bn (down from a ~$30bn peak six months earlier, i.e. −52%; per DefiLlama via search, as of ~Jun 2026), annualized protocol revenue ~$402m on a trailing-7-day basis at launch (per DefiLlama via The Defiant, Jul 2026); FY2025 revenue $907m, YTD-2026 $333m (per Standard Chartered coverage via Cryptobriefing). GHO stablecoin supply ~$580–600m (per search, mid-2026). Structure: the value-accrual layer is *consolidating* toward automated, revenue-funded buybacks — the dominant 2026 tokenomics meme. "Why now": Aavenomics 3.0 (confirmed live Jul 2026) replaces the discretionary ~$1m/week pilot buyback (running since Apr 2025, ~205k AAVE / ~1.28% of supply bought) with an *immutable, non-discretionary* on-chain mechanism routing 100% of Aave + GHO + Aave-branded-product revenue to AAVE holders — the culmination of the "Aave Will Win" (AWW) framework that passed governance Apr 2026. Second-order: DeFi is porting TradFi's buyback playbook (Uniswap flipped its fee switch Dec 2025, routing 17% of swap fees to UNI buyback+burn) — token "earnings yield" replaces TVL as the headline KPI.

**Competitive landscape.** Sector KPIs: protocol revenue, revenue→holders payout ratio, buyback $ / month vs annualized fees, TVL, stablecoin (GHO) supply. Peers on automated/revenue buybacks: **Hyperliquid** — most aggressive, ~97% of platform fees into an automated Assistance Fund (~29.8m HYPE, >$1.5bn, per tokenomist/search, Q3 2025); **Uniswap** — 17% fee-switch buyback+burn since Dec 2025; **Ethena/Sky** — real-yield stablecoin models (sUSDe funding-rate carry; Sky's savings rate) but not classic buyback. Basis of competition: credibility/immutability of the revenue→holder link, and whether fees actually cover it. Aave's position: **ahead / category leader** in lending and among the first blue-chips to make buybacks *immutable* rather than committee-gated (analysis) — moat = scale + brand + the largest DeFi deposit base and GHO as a native fee source (network effects + switching costs). Recent moves: Kraken in talks (Jun 2026) to buy a 15% stake at a $385m valuation ([[Kraken in talks to buy 15% Aave stake at $385M]]); Mastercard/MetaMask payments push (2026) ([[Aave and MetaMask bring DeFi to payments with Mastercard]], [[Mastercard partners with Aave for agentic payments]]).

**Comps & multiples.** Buyback intensity (annualized buyback $ vs annualized revenue), not equity multiples, is the comparable here.
- **Aave:** ~$402m annualized revenue now routes ~100% to holders (Aavenomics 3.0). Prior pilot: ~$1m/week ≈ $52m/yr → roughly $52m / $402m ≈ **13% of revenue** was being bought back before; 3.0 lifts the payout ratio materially higher. Earlier snapshot: ~$96m monthly fees / ~$13.2m monthly protocol revenue on ~$42bn TVL (per Cryptodaily, ~May 2026) — TVL has since fallen sharply, so revenue is cyclical.
- **Hyperliquid:** ~97% of fees to buyback (rich end of the range).
- **Uniswap:** 17% of swap fees (low end).
- Internal comps (base): [[Kraken in talks to buy 15% Aave stake at $385M]] (equity-stake valuation, not token mcap — mark as private-round valuation of the operating entity, NOT AAVE market cap); [[Aave reaches $50 billion in net deposits]] (Jul 2025 deposit scale, since roughly halved); [[KelpDAO exploit drains funds from Aave DeFi vaults]] (Apr 2026 — triggered billions in withdrawals though Aave's own contracts weren't compromised). Equity/EV multiples on AAVE = **no data** (need free, verifiable AAVE market cap + revenue snapshot as-of same date; not sourced). In-line-to-rich vs peers on payout ratio, but justified by genuine recurring fee revenue (analysis).

**Risk flags.**
1. **Buyback sustainability / procyclicality.** Fee revenue is cyclical and correlated with token prices and TVL — Aave's own TVL is down ~52% off peak and governance flagged a ~25% drop in borrow-fee revenue from its peak (per search). An immutable, revenue-funded buyback shrinks in a downturn exactly when support is most wanted; if 3.0 ever taps treasury rather than live fees, it becomes redistribution of reserves, not earnings (why: undermines the "real-yield" thesis).
2. **Immutability = governance/optionality risk.** Making buybacks non-discretionary removes committee flexibility to redirect capital (security incidents, GHO backstop, R&D) — post the Apr-2026 KelpDAO episode, hard-coding 100% revenue out to holders could starve safety-module / bad-debt coverage (why: a future exploit or GHO depeg needs treasury dry powder).
3. **"DeFi turning into CeFi" / centralization critique.** Concentrating value accrual in token buybacks (cited across Uniswap/Lido/Aave) prioritizes price support over ecosystem reinvestment and can entrench large holders (e.g. an incoming 15% strategic holder like Kraken) (why: governance capture + the dYdX cautionary tale — ~a quarter of revenue to buybacks, token still −90% from ATH).

**What this changes (idea-lens).** Re-rating of AAVE from a "TVL story" to a "protocol-earnings / real-yield" story — the first blue-chip lender to hard-wire ~100% revenue → holders (analysis). Falsifiable thesis: if Aavenomics 3.0 durably lifts AAVE's buyback-funded holder yield without draining treasury, AAVE should trade on an earnings-yield basis and lead peers; it breaks if a fee-revenue downturn (TVL/borrow-fee decline continuing) or a GHO/security event forces governance to halt or reverse the immutable buyback. Trigger to watch: monthly on-chain buyback $ vs annualized revenue post-launch, GHO supply trajectory, and whether the Kraken stake closes (institutional validation vs governance-concentration risk). (analysis)

Sources: https://thedefiant.io/news/defi/aave-confirms-aavenomics-3-0-live-buybacks-dao-spending-cut · https://thedefiant.io/news/defi/aave-advances-automated-aave-buyback-overhaul-aavenomics-3-0 · https://defillama.com/protocol/aave · https://cryptobriefing.com/aave-907m-revenue-2025-standard-chartered-coverage/ · https://cryptoslate.com/uniswap-lido-aave-how-token-buybacks-are-quietly-centralizing-defi/ · https://cryptodaily.co.uk/2026/05/aave-buybacks-protocol-revenue-defi-tokens · https://tokenomist.ai/hyperliquid/buyback
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
