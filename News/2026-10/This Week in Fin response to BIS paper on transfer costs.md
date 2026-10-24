---
title: "This Week in Fin: response to BIS paper on transfer costs"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - industry/remittances
  - industry/stablecoins
  - region/global
  - type/commentary
sources:
  - https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sef14dd9f
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# This Week in Fin: response to BIS paper on transfer costs

> [!info] 2026-10-23 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] A good response to the recent BIS workingpaper evaluating the cost differences in international transfers between fintech, stablecoins, and banks.

## Первоисточники

### bis.org
<https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins>
*499 слов · direct*

Competing rails for crossborder payments: banks, fintechs, and stablecoins
Focus
 We focus on the costs of cross-border payments across three payment channels: traditional banks, fintech money transfer operators (MTOs) and stablecoin-based transfers. Despite improvements in domestic payment systems, sending money internationally remains expensive, particularly for small transfers. We examine how payment architecture, foreign exchange (FX) pricing and intermediary fees shape these costs. It also studies whether stablecoins can overcome the frictions associated with existing payment channels. 
Contribution
 Combining intraday pricing from fintech MTOs, World Bank remittance data, bank wire transactions and crypto market data, we construct comparable measures of cross-border payment costs across currencies and transfer sizes. We distinguish FX markups from explicit fees, including exchange trading charges, blockchain transaction fees and fiat withdrawal costs. We examine both transfers using a single dollar-linked stablecoin and those involving on-chain exchanges between stablecoins denominated in different currencies.  
Findings
 There are three sets of findings. First, fintech money transfer operators (MTOs) substantially reduce cross-border payment costs relative to traditional retail bank wires. In our small sample of bank transactions, FX markups range from approximately 2 to 4.7%, even for highly liquid currencies and before accounting for explicit wire fees. By contrast, fintech transfer costs are considerably lower and decline substantially as a share of the amount sent as transfer size increases. For $10,000 transfers from the United States, median costs across developed market currency groups are around $40–$60, although some currency destinations remain considerably more expensive.  
 Second, using stablecoins to transfer funds across borders requires conversions between fiat currencies and stablecoins. These conversions still rely on crypto exchanges and other intermediaries, whose trading, conversion and withdrawal fees can substantially increase the total cost. Recipients may also have to wait for stablecoin conversion and bank processing before they can access the funds in their bank accounts. Moreover, liquidity between US dollar stablecoins and non-US currencies is generally very thin. 
 Third, stablecoins can offer favourable FX pricing for transfers from developed markets to some emerging market economies. However, this advantage reflects distortions associated with capital controls rather than the underlying technology. Limited market depth and volatile pricing also constrain the scale of such transfers. Ultimately, the competitiveness of stablecoins as cross-border payment rails depends not only on blockchain technology but also on market liquidity, reliable access to fiat currencies, regulatory compliance and trust in intermediaries. 
 Abstract 
 Cross-border payments remain slow and expensive despite significant improvements in digital financial infrastructure over the past several decades. This paper compares the cost of sending cross-border payments across three payment rails: traditional banks operating through the correspondent banking system and SWIFT, fintech money trans fer operators (MTOs) such as Wise, Remitly, and the digital arm of Western Union, and stablecoin-based transfers. We construct harmonized all-in costs measures across these three rails for different corridors and payment values. We find that fintech MTOs have significantly compressed the costs of cross-border payments, and demonstrate that stablecoins are not a panacea for frictions in cross-border payments.  
 Discussion  by Tobias Adrian 
Authors

## Контекст

<!-- enrichment:context -->
# Context-enrichment: This Week in Fin — response to BIS paper on transfer costs
_Analytical notes (not a post). Importance: 3/5._

This is a **thematic commentary item**, not a company event: "This Week in Fintech" (TWIF) flagged and endorsed "a good response" to BIS Working Paper No. 1385, _Competing rails for cross-border payments: banks, fintechs, and stablecoins_ (published 2026-10-19). Enriched here as analysis of the underlying debate.

## [0] What exactly happened (de-PR'd)
The BIS put out a working paper (No. 1385, 2026-10-19) by **Wenxin Du, Catherine Huang and David Scharfstein** (Harvard Business School) that builds **harmonized, all-in cost measures** across three cross-border rails — correspondent banks (SWIFT), fintech MTOs (Wise, Remitly, digital Western Union), and stablecoins — using intraday MTO pricing, World Bank remittance data, bank wire transactions and crypto-market data. TWIF's item is a one-line endorsement of a third-party response piece agreeing with the paper's skeptical read of stablecoins.
- **The paper's headline claim, de-hyped:** "fintech MTOs have significantly compressed the cost of cross-border payments, and stablecoins are **not a panacea**." Two distinct findings often conflated in crypto marketing:
  1. **Banks are expensive, fintechs are cheap.** Retail bank-wire **FX markups ≈ 200–470 bps** (2–4.7%) even on liquid USD/EUR, before explicit wire fees — vs a wholesale interbank bid-ask spread of **<6 bps**. That ~2 orders-of-magnitude retail-vs-wholesale gap is the real indictment. Fintech MTOs collapse it: **median all-in cost on a $10,000 US-outbound transfer to developed-market currencies ≈ $40–$60** (~0.4–0.6%), declining as a share as ticket size rises.
  2. **Stablecoins don't remove intermediaries — they relocate them.** On-chain transfer fees are tiny and stablecoin FX can approach wholesale rates, BUT fiat↔stablecoin conversion still runs through crypto exchanges, which **"act like correspondent banks"**: trading, conversion and withdrawal fees plus settlement/processing delays push all-in cost **as high as or higher than a bank wire**. USD-stablecoin↔non-USD liquidity is **"generally very thin."**
- **Why framed this way (the anti-PR core):** the paper deliberately separates the **on-chain leg** (cheap, where crypto marketing anchors) from the **off/on-ramp legs** (expensive, where compliance + customer service are the largest fixed costs). The widely-cited "stablecoins cost pennies" figure measures only the cheap middle leg. The honest comparison is **all-in, door-to-door**, and on that basis fintech MTOs — not stablecoins — are today's cost leader. **(analysis)** The item's value is precisely this de-PR'ing; TWIF is amplifying the BIS line against the "stablecoins disintermediate everything" narrative.
- **One genuine pro-stablecoin finding:** stablecoins **can** offer favorable FX into some **emerging markets** — but the paper attributes this to **distortions from capital controls**, not the technology (you are arbitraging a parallel FX rate, not a cheaper rail), and thin depth + volatile pricing cap the size.

## [1] Competitors / peers (the three rails)
- **Fintech MTOs — current cost winners:** Wise, Remitly, Western Union's digital arm. The paper's own data makes them the benchmark the other two rails must beat. Position: **ahead on cost today.**
- **Correspondent banks (SWIFT) — the expensive incumbent:** 200–470 bps FX markup is the baseline everyone undercuts. SWIFT's own counter-moves are live in the corpus — [[Swift launches pay-by-alias cross-border initiative]] — i.e. incumbents fighting on UX/addressing, not price.
- **Stablecoin rails — over-promised vs the data:** corpus shows a wall of 2025–26 stablecoin cross-border launches/pilots that the BIS paper implicitly stress-tests: [[Western Union plans USDPT stablecoin on Solana]], [[Zelle to support international payments via stablecoins]], [[Zepz launches stablecoin-powered Sendwave Wallet for digital dollars]], [[Thunes launches Pay-to-Stablecoin-Wallets solution]], [[TerraPay partners with Fipto for stablecoin flows]], [[Japan's megabanks complete yen stablecoin cross-border pilot]]. Position: **loud on announcements, unproven on all-in cost** — exactly the gap the paper measures.
- **Why the landscape is this way (2nd-order):** the margin in cross-border payments sits at the **fiat on/off-ramp and compliance layer**, not the transport layer. Whoever controls fiat access captures the rent — which is why MTOs (who own both ramps and the licences) beat a stablecoin flow that must rent exchange ramps. Stablecoins only win where they also disintermediate the ramp (self-custody wallet to self-custody wallet, or where a regulated parallel-FX arbitrage exists).

## [2] Where the debate fits (company/theme trajectory)
- The BIS has been consistently skeptical of stablecoins as money (see its 2026 Annual Economic Report chapter "Anchoring trust in money: innovation beyond stablecoins"); No. 1385 is the **empirical, cost-level** version of that institutional stance, not a one-off.
- It lands amid a 12-month stablecoin-remittance land-grab (the corpus cluster above) and a persistently high headline cost: **World Bank global average remittance cost ≈ 6.36% (RPW Issue 54, Apr 2026)**, still ~2× the **UN SDG / G20 3% target** for 2030. That persistent gap is what every rail claims to close.
- **Why this matters now (analysis):** the paper is a counterweight at the exact moment capital and PR are flooding into stablecoin rails (post-GENIUS-Act US environment). It reframes the central question from **"will stablecoins kill SWIFT?"** to **"who already closed the retail-vs-wholesale FX gap — and it's fintech MTOs, not crypto."**

## [3] Novelty / value-add / traction
- **Novelty of the paper:** the de-PR'd **all-in** methodology (FX markup separated from explicit fees; on-chain fee separated from ramp/withdrawal/compliance cost) across all three rails with real transaction/pricing data. That is new and citable; most prior "stablecoins are cheaper" claims measured only the on-chain leg.
- **Novelty of the TWIF item itself:** low — it's an endorsement/amplification, not original analysis. Its weight is as a **signal** that the skeptical, data-grounded framing is gaining traction in fintech discourse against stablecoin hype.
- **Who captures the margin (the real question):** the paper's implicit answer — **the fiat ramp + compliance layer**. Stablecoins shift value from correspondent banks to crypto exchanges; they do not hand it to end users unless the ramp is also removed. That is why "disintermediation" is a misnomer: it's **re-intermediation** at near-parity cost. **(analysis)**

## [4] What's next / sentiment
- **Likely trajectory:** stablecoins compete hardest where they (a) collapse the ramp via embedded wallets/held balances (cf. [[Zepz launches stablecoin-powered Sendwave Wallet for digital dollars]] holding "digital dollars" so no per-transfer off-ramp), or (b) exploit regulated EM corridors with parallel FX. Pure fiat→stablecoin→fiat door-to-door stays at or above MTO cost until exchange liquidity in non-USD pairs deepens.
- **Counter-intuitive 2nd-order effect:** cheap on-chain transport + expensive ramps means the **winners are vertically-integrated players who own the ramp** (Wise, Remitly, Western Union, Zepz) — the same incumbents stablecoins were supposed to disrupt. Crypto risks subsidising the exact intermediaries it set out to kill.
- **Risk to the BIS thesis:** stablecoin-native payroll/held-balance use (recipient keeps the stablecoin, never off-ramps) partly escapes the paper's all-in framing; and deepening EUR/MXN/etc. stablecoin liquidity could narrow the ramp cost over 2026–27. The paper is a snapshot, not a verdict.

## Sources
- BIS WP No. 1385 (2026-10-19), Du, Huang, Scharfstein — https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
- Finextra, "Fintechs top banks and stablecoins for cheap cross-border payment – BIS research" — https://www.finextra.com/newsarticle/48630/fintechs-top-banks-and-stablecoins-for-cheap-cross-border-payment---bis-research
- Payment Expert, "BIS paper: stablecoins don't cut out cross-border middlemen" (2026-10-23) — https://paymentexpert.com/2026/10/23/bis-paper-stablecoins-payment/
- Genfinity, "BIS stablecoin cross-border payments not a panacea" (2026-10-20) — https://genfinity.io/2026/10/20/bis-stablecoin-cross-border-payments-not-a-panacea/
- Harvard Business School faculty working paper page — https://www.hbs.edu/faculty/Pages/item.aspx?num=68673
- World Bank Remittance Prices Worldwide, Issue 54 (Apr 2026), global avg 6.36% vs 3% SDG target — https://remittanceprices.worldbank.org/
- Internal corpus: [[Western Union plans USDPT stablecoin on Solana]], [[Zelle to support international payments via stablecoins]], [[Zepz launches stablecoin-powered Sendwave Wallet for digital dollars]], [[Thunes launches Pay-to-Stablecoin-Wallets solution]], [[Swift launches pay-by-alias cross-border initiative]], [[Japan's megabanks complete yen stablecoin cross-border pilot]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is this a new event or a re-report?** New: it responds to a specific paper (BIS WP 1385, 2026-10-19). No prior corpus note covers this paper. **Fresh.**

2. **Does the TWIF item add original analysis?** No — it endorses a third-party "response." Its weight is as a discourse signal, not new facts. **Answered.**

3. **Headline claim?** "Fintech MTOs compressed cross-border cost; stablecoins are not a panacea." Two separable findings; crypto marketing usually hears only the second half as a challenge. **Answered.**

4. **Hard numbers — banks:** retail FX markups ≈ 200–470 bps (2–4.7%) on liquid USD/EUR, before explicit wire fees; wholesale bid-ask <6 bps. The retail-vs-wholesale gap is the core finding. **Answered.**

5. **Hard numbers — fintechs:** median all-in ≈ $40–$60 on a $10,000 US-outbound transfer to developed-market currencies (~0.4–0.6%); cost share falls as ticket rises. **Answered.**

6. **Hard numbers — stablecoins:** on-chain fee trivial and FX can near wholesale, BUT exchange trading/conversion/withdrawal fees + settlement delay push all-in cost to ≥ a bank wire; USD↔non-USD liquidity "very thin." **Answered.**

7. **Why "not a panacea" specifically?** Stablecoins don't eliminate intermediaries — crypto exchanges "act like correspondent banks." It's re-intermediation at near-parity cost, not disintermediation. **Answered.**

8. **Any genuine stablecoin win?** Yes — favorable FX into some EMs, but driven by capital-control distortions (parallel-rate arbitrage), not the tech; capped by thin depth/volatility. **Answered.**

9. **Methodology credible?** Yes — harmonized all-in measures from intraday MTO pricing + World Bank data + bank wires + crypto data; separates FX markup from explicit fees and on-chain from ramp costs. HBS authors, BIS working paper (not peer-reviewed/final). **Answered.**

10. **Who are the authors / is there bias?** Wenxin Du, Catherine Huang, David Scharfstein (HBS); published via BIS, an institution structurally skeptical of stablecoins (cf. 2026 AER chapter). Institutional prior exists, but findings are data-grounded. **Answered with caveat.**

11. **What's the market backdrop that makes this matter?** World Bank global remittance avg ≈ 6.36% (RPW Issue 54, Apr 2026) vs 3% SDG/G20 2030 target; 12-month stablecoin-remittance launch wave in corpus. **Answered.**

12. **Where do stablecoins actually win on cost?** When the ramp is collapsed (held balances / embedded wallets, e.g. Zepz Sendwave "digital dollars") or regulated EM parallel-FX corridors — not fiat→SC→fiat door-to-door. **Answered.**

13. **Biggest counter-intuitive takeaway?** Cheap transport + expensive ramps means vertically-integrated incumbents who own the ramp (Wise, Remitly, WU, Zepz) are the structural winners — crypto risks subsidising the intermediaries it meant to kill. **Answered (analysis).**

14. **What could invalidate the BIS thesis over 12–24 months?** Deepening non-USD stablecoin liquidity narrowing ramp cost; growth of stablecoin-native/held-balance use that never off-ramps (escapes the all-in frame). Snapshot, not verdict. **Open.**

15. **Does the item change the central question?** Yes — from "will stablecoins kill SWIFT?" to "who already closed the retail-vs-wholesale FX gap" (answer: fintech MTOs), and "who captures the ramp/compliance margin." **Answered.**

16. **Duplicate check:** grep for working-paper-1385 / "Competing rails" / BIS commentary in 2026-10 returns only this note. No twin. **Fresh.**

**Importance: 3/5** — Not a company event and the TWIF line itself is just an endorsement, so no traction/novelty of its own (would be 1–2). But the underlying BIS WP 1385 is a high-quality, widely-cited, de-PR'd empirical rebuttal to the dominant stablecoin-remittance narrative, directly relevant to a large corpus cluster, with concrete figures (200–470 bps banks, $40–60/$10k fintechs, 6.36% World Bank avg). As thematic analysis it is genuinely weight-bearing, lifting it to a 3.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Global remittance flows reached ~$857bn in 2025 (2024: $905bn, of which ~$685bn to low/middle-income countries) — per World Bank, via internationalmoneytransfer.com/ebc.com, as of 2026. The global average cost to send $200 was 6.36% in Q3 2025 (down from 6.49% in Q1), still >2x the UN SDG 3%-by-2030 target; digital averaged 4.59% vs 7.30% non-digital — per World Bank RPW, via remitroutes.com (Apr 2026). The digital-remittance slice is ~$278bn in 2026, forecast ~$342bn by 2031 (CAGR ~4.2%) — per Mordor Intelligence, via mordorintelligence.com. Structure: the rail stack is the real battleground — banks/correspondent+SWIFT at the top of the cost curve, fintech MTOs compressing it, stablecoins restructuring (not removing) the intermediary layer. Barriers are regulatory (money-transmitter licences per corridor) and network/liquidity (payout partners, FX depth), not technology. Why now: the BIS WP 1385 (Du/Huang/Scharfstein, HBS; published 2026-10-19) hands a data-grounded verdict into a market where the "stablecoins kill remittance fees" thesis had been priced as near-inevitable.

**Competitive landscape.** Sector KPIs: all-in cost as % of amount (FX markup + explicit fees), transfer volume/TPV, net-revenue take rate, corridor coverage. Key players by rail: **MTOs/fintech** — Wise, Remitly, Western Union's digital arm (basis of competition: price + corridor breadth + distribution); **incumbent banks** — correspondent+SWIFT (slowest, dearest: BIS finds bank FX markups ~2.0–4.7% even in liquid pairs, before wire fees); **stablecoin rails** — Circle/USDC, Tether/USDT. BIS finding: fintech all-in costs are ~40–150bps and fall as ticket size rises (e.g. $10k US transfers to DM currencies cost ~$40–60 median = ~0.4–0.6%). Recent moves: Circle announced a 40-market USDC push and a Thunes tie-up (140+ countries) on 2026-10-20 to cut prefunding (via onesafe.io/stablecoininsider.org); Western Union agreed to buy Intermex for ~$500m in 2025 (adds ~6m customers). Protagonist here is the BIS thesis itself, not a company — the "position" call: fintech MTOs are the current cost leaders; stablecoins are a contender constrained by on/off-ramp economics, not a done deal (analysis).

**Comps & multiples.** Public peers (comparability caveat: different scale/model, use as directional):
- Remitly: market cap ~$3.65bn / revenue ~$1.64bn (+25.7% YoY) → P/S = $3.65bn / $1.64bn ≈ **2.2x** (via pitchgrade.com, 2026).
- Wise: FY net revenue ~$2.5bn (+19%), cross-border volume ~$243bn (+31%), ~19m customers; market cap not verified in a free source → P/S **[UNSOURCED]** (via granaresearch/mordorintelligence, 2026).
- Western Union: 2024 revenue ~$4.2bn (~90% consumer money transfer); multiple not computed here (no verified current cap) — a declining-incumbent profile, not a growth comp.
- Circle: reportedly keeps ~7 cents of each revenue dollar (reserve-income economics flow mostly to distribution partners) — a structurally thin net-take model (via biggo.com, 2026); explicit multiple **[UNSOURCED]**.
Internal comps (base): [[Wise gets UAE Central Bank approval for products]], [[Western Union launches first digital remittance app in Philippines]], [[Zepz launches stablecoin-powered Sendwave Wallet for digital dollars]], [[Viamericas raises $113.6M for remittance network]]. Median/distribution not computed (<3 verified comparable multiples) — qualitative only. Remitly at ~2.2x P/S looks in-line-to-modest for ~26% growth, not stretched (analysis).

**Risk flags.**
1. Disintermediation is overstated, not absent — BIS shows stablecoins restructure rather than remove intermediaries (exchanges/on-off-ramps behave like correspondent banks); the risk to MTO incumbents is slower than the crypto narrative implies, but the risk to stablecoin-rail business models is that end-to-end cost advantage evaporates once ramp FX spreads, withdrawal fees and thin USD↔non-USD liquidity are counted.
2. "EM advantage" is a regulatory-arbitrage artefact — BIS attributes stablecoins' favourable EM FX pricing to capital-control distortions and dollar demand, not technology; that edge is fragile to a single regulatory move (capital-control enforcement, local stablecoin rules) and non-scalable given thin market depth.
3. Rate/reserve-income dependence for stablecoin issuers — Circle's ~7¢-on-the-dollar net economics make the model sensitive to falling rates and to partners defecting to rival coins, undercutting the capital available to subsidise cheap corridors.

**What this changes (idea-lens).** The BIS paper is a de-rating signal for the "stablecoins = free remittance" thesis and a quiet re-validation of the fintech-MTO cost-leader position — watch whether stablecoin players respond by acquiring/partnering on the fiat ramp (Circle–Thunes is the first tell) to internalise the cost BIS flags (analysis). Falsifiable: if a USDC/USDT corridor posts audited, independently-measured all-in cost at or below the BIS fintech-MTO band (~40–150bps) on a thick liquid pair, the "not a panacea" verdict weakens; absence of such a published number keeps MTOs as the cost benchmark.

Sources: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins · https://remitroutes.com/blog/world-bank-remittance-prices-report-april-2026 · https://www.ebc.com/forex/global-remittances-905-billion-fdi-deportation-tax-risk · https://www.mordorintelligence.com/industry-reports/digital-remittance-market · https://pitchgrade.com/companies/remitly-global-inc · https://www.onesafe.io/blog/stablecoin-regulation-2026-circle-40-markets · https://finance.biggo.com/news/36468326-81f3-4111-b3e6-62aa1515f493
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
