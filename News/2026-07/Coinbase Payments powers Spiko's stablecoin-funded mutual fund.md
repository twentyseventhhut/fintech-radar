---
title: "Coinbase Payments powers Spiko's stablecoin-funded mutual fund"
date: 2026-07-01
retrieved: 2026-07-01
tags:
  - company/coinbase
  - company/spiko
  - industry/stablecoins
  - region/europe
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/b808dd9d
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s9ab71645
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Coinbase Payments powers Spiko's stablecoin-funded mutual fund

> [!info] 2026-07-01 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇫🇷 Coinbase powers Spiko’s mutual fund with stablecoin funding. By leveraging Coinbase Payments, Spiko has eliminated the traditional multi-day settlement gap, allowing institutional investors to move seamlessly between USDC and T-bills 24/7.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/b808dd9d>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Coinbase Payments powers Spiko's stablecoin-funded mutual fund
_Analytical notes (not a post). Importance: 3/5._

**Freshness: FRESH.** New event (30 Jun 2026): stablecoin subscribe/redeem now LIVE for Spiko's UCITS T-bill funds via Coinbase Payments. Prior corpus notes cover an adjacent-but-distinct fact — Spiko's July-2025 $22M Series A ([[Index Ventures and Revolut founder back Spiko in $22M raise]]) — not this integration. Not a re-run.

## [0] What exactly happened (de-PR'd)
- On ~**30 Jun 2026**, Coinbase and Spiko announced that investors can now **subscribe to and redeem from Spiko's two UCITS-regulated tokenized money-market funds (EU T-Bills / EUTBL and US T-Bills / USTBL) using USDC/EURC**, settled via **Coinbase Payments** — Coinbase's stablecoin commerce rail running on **Base** (its L2). Marketed as the first EU **UCITS** funds to accept stablecoin subscriptions.
- De-PR'd mechanism: Coinbase Payments is the **on/off-ramp + settlement leg on Base** (Commerce Payments Protocol, USDC/EURC). An investor deposits USDC/EURC to buy fund shares and redeems back to their wallet "within minutes," replacing SEPA/SWIFT wires (T+1–T+3). **No x402** involved despite the "onchain" framing.
- **Why this framing matters (analysis):** the "eliminated the multi-day settlement gap / 24-7 USDC↔T-bills" claim is a **UX/liquidity claim at the stablecoin boundary**, NOT instant T-bill settlement. Fund NAV striking and the underlying T-bill market still run on TradFi rails; what is genuinely instant is the stablecoin deposit/redeem leg, backed by Spiko's own liquidity. Fair to say "no wire lag," misleading to read as "T-bills settle instantly."
- **What's silent:** no named end-clients, no volumes, no fresh AUM tied to the integration, no exclusivity terms, no executive quotes in accessible coverage. Primary Coinbase/Spiko pages were bot-blocked; several mechanics rest on secondary reporting.

## [1] Competitors / peers
Tokenized-MMF field, ~May 2026 AUM (directional; moves fast): USYC/Circle-Hashnote ~$2.9B; BUIDL/BlackRock ~$2.6B; USDY/Ondo ~$2.1B; BENJI-FOBXX/Franklin Templeton ~$2.0B; JTRSY/Centrifuge ~$1.2B; **Spiko EUTBL+USTBL ~$1.03B (Feb 2026)**; USTB/Superstate ~$0.7B. Category ~$7B onchain in early 2026 (from ~$850M two years prior).
- **Position:** Spiko is roughly **top-5/6 globally and the only EU/UCITS-regulated issuer at that scale**. On the *distribution* angle, Coinbase itself competes via Coinbase Asset Management ([[Coinbase Asset Management launches tokenized credit strategy via Superstate]]) and its ProShares GENIUS MMF ETF stake ([[Coinbase invests in ProShares GENIUS stablecoin reserve ETF IQMM]]) — so Coinbase is simultaneously a rail for Spiko AND a would-be product competitor.
- **Why (analysis):** US incumbents (BlackRock/Circle/Ondo) won on brand + USD depth; Spiko's moat is the **UCITS wrapper + EURC leg**, a regulated European niche the US majors don't hold. This partnership is Coinbase renting distribution to Spiko rather than building an EU UCITS product itself.

## [2] Company history / fit
- Spiko: founded **2023** (Paul-Adrien Hyppolite, ex-French Treasury; Antoine Michon, ex-Palantir), AMF-regulated SICAV, funds launched mid-2024 (billed "first tokenized UCITS MMFs"), ~0.25%/yr fee.
- **$22M Series A, Jul 2025**, Index Ventures + White Star, Frst, Bpifrance, angels (Storonsky/Revolut, Sinha/Wise, Abrams/Bridge) — see [[Index Ventures and Revolut founder back Spiko in $22M raise]]. AUM ~$400M then → **$1.03B Feb 2026**, 3,300+ clients, ~92% B2B.
- **Fit:** consistent. Spiko sells idle-cash yield to corporate treasuries; a USDC/EURC on-ramp removes the wire-lag friction that most blocks treasury adoption. Logical next step, not a pivot.

## [3] Novelty / value-add / traction
- **Genuinely new:** first **UCITS**-regulated fund to accept stablecoin subscriptions — a real regulatory/plumbing first, not just another BUIDL clone. The novelty is the **EU-regulated wrapper + stablecoin rail** combination.
- **Traction — thin:** the integration is **live** (not just announced), but **zero adoption metrics disclosed** — no clients, no volume, no AUM uplift attributed to it. So the "value-add" is proven mechanically but **unproven commercially**.
- **Margin/stack (analysis):** Spiko captures the fund fee (~25bps); Coinbase captures rail/settlement economics + USDC float via Base. Second-order risk for Spiko: it is **dependent on Coinbase's rail and USDC/EURC** for its headline UX, while Coinbase runs competing tokenized products — the classic "your distributor is your competitor" exposure. The real question is less "is stablecoin-funded UCITS possible" (yes) than **"can Spiko convert this rail into net-new B2B AUM before Coinbase/BlackRock offer an equivalent EU wrapper."**

## [4] What's next / market sentiment
- Backdrop: tokenized treasuries ~$7B and climbing; GENIUS Act reserve rules pushing stablecoin issuers toward MMF-style reserves (Coinbase already positioning via IQMM). Regulatory tailwind for compliant onchain cash.
- Watch: named enterprise clients, EURC/USDC subscription volumes, and whether AUM meaningfully steps up post-launch. Absent those, this stays a well-executed plumbing milestone rather than a category shift.
- **Counterintuitive (hypothesis):** the more successful stablecoin-funded MMFs become, the more attractive it is for Coinbase/BlackRock to internalize EU distribution — success could invite disintermediation of the very partner (Spiko) that proved the model.

## Sources
- https://ffnews.com/news/coinbase-and-spiko-launch-europes-first-stablecoin-funded-ucits-mutual-funds
- https://cryptoadventure.com/coinbase-and-spiko-open-stablecoin-access-to-tokenized-ucits-money-market-funds/
- https://bitcoinworld.co.in/coinbase-spiko-stablecoin-bond-fund-payments/
- https://www.spiko.io/blog/1-billion-aum-numbers
- https://www.spiko.io/blog/spiko-raises-22m-led-by-index-ventures
- https://www.coinbase.com/blog/coinbase-and-shopify-bring-usdc-payments-on-base-to-millions-of-merchants-worldwide
- Internal: [[Index Ventures and Revolut founder back Spiko in $22M raise]], [[Coinbase Asset Management launches tokenized credit strategy via Superstate]], [[Coinbase invests in ProShares GENIUS stablecoin reserve ETF IQMM]], [[Shopify enables USDC payments on Coinbase Base via Stripe]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is it really new?** Yes — first UCITS-regulated fund to accept stablecoin subscriptions (30 Jun 2026); Coinbase Payments itself dates to Jun 2025. Not a re-announcement.
2. **Is the "no multi-day settlement gap" claim real?** Partly. Instant applies to the **stablecoin deposit/redeem leg only**, backed by Spiko liquidity — NOT to underlying T-bill settlement. UX claim, not market-structure claim. (analysis)
3. **Live or just announced?** Live per coverage — but zero adoption metrics. "Live" ≠ "adopted."
4. **Who are the actual clients?** OPEN — none named. Spiko is ~92% B2B (corporate treasuries), but no user tied to this integration was disclosed.
5. **How much net-new AUM has the integration driven?** OPEN — no figure disclosed; Feb-2026 $1.03B AUM predates the integration.
6. **What exactly is Coinbase Payments doing here — rail, custody, or product?** Settlement/on-off-ramp on Base (USDC/EURC via Commerce Payments Protocol). Not x402, not custody of fund shares.
7. **Who captures the margin?** Spiko ~25bps fund fee; Coinbase gets rail/settlement + USDC float. Split favors the rail owner at scale. (analysis)
8. **Conflict of interest — is Coinbase a competitor?** YES. Coinbase Asset Management (Superstate credit fund) + ProShares IQMM stake put Coinbase in the same tokenized-cash space it's now distributing for Spiko.
9. **Where does Spiko rank vs BUIDL/USYC/Ondo?** ~top-5/6 globally (~$1B), #1 in EU/UCITS. Mid-tier by AUM, niche leader by regulation.
10. **What's the exclusivity / can Spiko use other rails?** OPEN — no exclusivity terms disclosed.
11. **Does EURC vs USDC matter?** Yes — EURC support is the EU differentiator US incumbents lack; central to why this is a UCITS/EU-specific first.
12. **Regulatory exposure?** UCITS + AMF give it a compliance edge; GENIUS Act tailwind for compliant onchain cash. Low near-term regulatory risk vs unregulated peers.
13. **Downside trigger?** Coinbase/BlackRock launching an equivalent EU UCITS wrapper → disintermediates Spiko's rail-dependent moat.
14. **Source reliability?** Medium — primary Coinbase/Spiko pages bot-blocked; mechanics from secondary crypto press. One source misdated Coinbase Payments to "2026" (correct: Jun 2025).
15. **Does the corpus already cover this?** No — closest is Spiko's Jul-2025 raise [[Index Ventures and Revolut founder back Spiko in $22M raise]], a different event. FRESH.

**Importance: 3/5 — genuine regulatory first (first stablecoin-funded UCITS MMF) and a clean TradFi↔onchain bridge on a hot ~$7B theme where Spiko leads Europe; but capped by mid-tier AUM, zero disclosed adoption/volume/clients, a UX-overstated "instant settlement" claim, and a partner (Coinbase) that is also a competitor.**
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-04]] (2026-07-04).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Tokenized RWAs (ex-stablecoins) reached ~$31.4bn by mid-May 2026, up from ~$6bn at start of 2025, with tokenized US Treasuries the dominant subcategory at ~$15.3bn (~45% of the RWA market) — per RWA.xyz/DeFiLlama, via Yellow.com and finextra, as of May 2026. Money-market/T-bill funds lead the onchain wave: BlackRock BUIDL ~$2.8bn AUM (Q2 2026, per rwa.xyz), and JPMorgan launched JLTXX in May 2026 explicitly as a GENIUS-Act-compliant reserve asset. Structure: still small and fragmented — a land-grab where asset managers (BlackRock, Franklin, WisdomTree, JPMorgan, Goldman/BNY) supply the fund and crypto-native rails (Coinbase/Base, Securitize, Superstate, Centrifuge) supply settlement. Barriers are regulatory (UCITS/SEC exemptive relief, MiCA) and distribution, not tech. Why now: (1) the 2022–24 rate cycle made ~4–5% T-bill yield the product; (2) GENIUS Act (US) + MiCA (EU) legitimize stablecoins as the on/off-ramp; (3) the pitch here is settlement — Spiko/Coinbase collapse the multi-day fund subscription/redemption gap into 24/7 USDC/EURC flow on Base (analysis).

**Competitive landscape.** Sector KPIs: fund AUM, net yield vs benchmark, settlement latency, and for the rails provider — TPV / stablecoin float / take on flow. Key players: incumbent asset managers own the fund (BlackRock BUIDL, Franklin BENJI, WisdomTree, Goldman/BNY, JPMorgan JLTXX); crypto rails compete to be the settlement backbone (Coinbase Payments/Base here; Securitize powers BUIDL; Superstate, Centrifuge). Recent moves: WisdomTree launched 24/7 trading + instant settlement for a tokenized MMF (2026-02-27, via SEC exemptive relief); JPMorgan launched a tokenized MMF on Ethereum (Dec 2025); Coinbase took an equity stake in Centrifuge as "preferred tokenization backbone" (2026-05-05) and is issuing its own CUSHY credit fund and a Bitcoin Yield Fund share class on Base. Protagonist position: Spiko is a niche but first-mover — the funds are pitched as the first UCITS to subscribe/redeem in stablecoins (USDC for the US T-bill fund, EURC for the EU fund), an EU-regulatory first (per Cointelegraph, ffnews, 2026-06-30). Spiko's moat is regulatory (UCITS wrapper + EU distribution) and being early in EURC; Coinbase's moat is the Base/USDC network + payments API. Note: it is Coinbase, not Spiko, that captures the durable economics here (rails + stablecoin float) — Spiko is the distribution front-end (analysis).

**Comps & multiples.** Best public read-through is the USDC economics, since Coinbase — not Spiko — is the value capture point.
- **Circle (CRCL)** — mkt cap ~$15.4bn, TTM revenue ~$2.86bn (as of 2026-07-01, per stockanalysis/Yahoo) → P/S = $15.4bn / $2.86bn ≈ **5.4x**. Reserve income ~$653m of $694m Q1-2026 revenue; USDC circulation ~$77bn (+28% YoY). In-line-to-rich for a rate-sensitive float business whose growth (~20% YoY Q1) doesn't obviously justify a 5x sales multiple → watch rate direction (analysis).
- **Coinbase (COIN)** — IR PRIMARY: FY2025 stablecoin revenue **$1,348,821K = $1.35bn, +48% YoY**; total subscription & services **$2,828,048K = $2.83bn, ~41% of net revenue** (10-K, coin-20251231, 2026-02-12). Coinbase keeps 100% of interest on USDC held on its platform + 50% of net reserve income on the rest; in 2024 Coinbase earned more from USDC than Circle did. This is the "who captures the economics" answer for the Spiko deal — flow settled via Coinbase Payments/Base feeds Coinbase's stablecoin + Base/"other transaction" lines, not a fee to Spiko (analysis).
- **Spiko (private)** — Series A $22m led by Index Ventures (2025-07-17); ~$400m AUM in year one, targeting $1bn by end-2025; >$900m working capital from >1,000 businesses. No post-money valuation disclosed → **[UNSOURCED]**; treat as a round, not a market cap. EV/Revenue/AUM multiple: **no data** (Spiko take rate not disclosed).
- Internal comps: [[JPMorgan launches tokenized money market fund on Ethereum]], [[WisdomTree launches 24 7 trading for tokenized money market fund]], [[Goldman Sachs and BNY launch tokenized money market funds]], [[Coinbase taps Centrifuge for tokenization and takes equity stake]].
- Distribution not computed (only 2 clean public multiples, different models) → qualitative comparison only.

**Risk flags.**
1. **Value capture sits with the rails, not the fund.** Spiko is disintermediated on the durable economics — settlement float and stablecoin interest accrue to Coinbase/Circle. If a fund can plug into Base/USDC directly, Spiko's differentiation narrows to the UCITS wrapper (analysis).
2. **Dependence on someone else's rails + stablecoin concentration.** The 24/7 promise is built on Coinbase Payments, Base, and USDC/EURC. Single-network / single-stablecoin dependence means Spiko inherits Coinbase's and Circle's platform, de-peg and regulatory risk (analysis).
3. **Yield/rate cyclicality + governance overhang.** The whole product is a rate trade — the "yield" is T-bill rates; a cutting cycle compresses the appeal. Separately, on 2026-06-30 Coinbase (with Stripe and BlackRock) backed a *rival* stablecoin network, and CRCL fell ~8% (per CoinDesk) — a signal Coinbase's USDC alignment is not permanent, which matters for anyone building on Coinbase's stablecoin rails.

**What this changes (idea-lens).** This is a rails/distribution unbundling story, not a re-rating: tokenized MMFs are commoditizing on the fund side while competition concentrates on who owns settlement (Base vs Securitize vs Superstate) (analysis). Falsifiable thesis: if stablecoin-settled subscription/redemption becomes table stakes, standalone tokenization front-ends like Spiko compress into thin distribution unless they own proprietary AUM/EURC scale — watch whether Spiko's AUM materially breaks past $1bn and whether it stays single-stablecoin/single-chain. Trigger to revisit: Coinbase pushing its own CUSHY/Base MMF products would put it in direct competition with the very partners (like Spiko) it settles for.

Sources: https://cointelegraph.com/news/spiko-coinbase-stablecoin-payments-treasury-funds · https://ffnews.com/news/coinbase-and-spiko-launch-europes-first-stablecoin-funded-ucits-mutual-funds · https://yellow.com/research/tokenized-rwas-31b-market-growth-real-race-starting · https://www.finextra.com/blogposting/31625/tokenized-real-world-assets-reading-the-2026-numbers-behind-the-headline-growth · https://www.spiko.io/blog/spiko-raises-22m-led-by-index-ventures · https://stockanalysis.com/stocks/crcl/ · https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-filing · https://www.coindesk.com/business/2026/06/30/circle-slides-8-as-stripe-coinbase-and-blackrock-back-rival-stablecoin-network · IR: https://drive.google.com/file/d/1m4rj1PNY67mWczRIGR2nirZ4RsVgZ6U4/view (Coinbase 10-K FY2025) · https://drive.google.com/file/d/1LXwG9VEN-elbVu_X8-kUL66zOa02kE5z/view (Coinbase 2025 ARS)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** **MISS.** Q1 2026 (period ended 2026-03-31, reported 2026-05-07) — Total revenue $1,412.98M (-30.5% YoY; -21% Q/Q) and Net revenue $1,339.35M (-30.9% YoY), below public consensus of ~$1.5–1.56bn (miss of roughly -$90-150M / ~-6%). GAAP diluted EPS $(1.49) vs $0.24 a year ago and vs ~+$0.29 public consensus (surprise ~-146%). Driver: crypto market volumes fell 28% Q/Q and spot volumes 37% Q/Q, dragging transaction revenue down; a $482.4M mark-to-market loss on crypto assets held for investment tipped GAAP to a net loss. Guidance: Q2 2026 outlook given — S&S $565-645M; transaction revenue ~$215M QTD through May 5. **Relevant to the Coinbase Payments + stablecoin story: stablecoin revenue was the standout, $305.4M (+11.5% YoY), the fastest-growing line as trading collapsed.**

**Key figures (with growth).**
- Net revenue **$1,339.35M** (-30.9% YoY vs $1,936.82M). Total revenue **$1,412.98M** (-30.5% YoY vs $2,034.30M; -21% Q/Q).
- Total transaction revenue **$755.83M** (-40.1% YoY vs $1,262.21M); Consumer $566.90M (-48.3% YoY), Institutional $135.73M (+37.3% YoY), Other transaction $53.20M (-21.5% YoY).
- Total subscription & services **$583.52M** (-13.5% YoY vs $674.61M), now **44% of net revenue** — a durable buffer independent of trading.
  - **Stablecoin revenue $305.4M (+11.5% YoY** vs $274.0M), driven by USDC market-cap growth (reached ~$80bn supply in Q1) and ATH average USDC held in Coinbase products. Note a Q1'26 presentation change: revenue on Coinbase's own corporate USDC balances (~$23.5M in the year-ago period) was reclassified out of Stablecoin revenue into Corporate interest/Other revenue, so reported YoY growth is on a like-for-like basis.
  - Blockchain rewards $100.85M (-48.7% YoY); Interest & finance fee income $67.81M (+7.5% YoY); Other S&S $109.43M (-22.3% YoY).
- **Net loss $(394.1)M** vs net income $65.6M a year ago; operating result swung to an operating loss of $(21.4)M vs operating income $705.8M (opex +8.0% YoY to $1,434.4M, incl. Technology & development $525.6M vs $355.4M).
- Non-GAAP: **Adjusted EBITDA $303.3M** (-67% YoY vs $929.9M Q1'25; -46% Q/Q vs $565.9M Q4'25), still positive for a 13th consecutive quarter. **Adjusted net loss $(45.6)M** vs adjusted net income $524.1M a year ago.
- Balance sheet: cash & equivalents $10.2bn; ~$12bn total available resources incl. $1.8bn crypto/marketable investments.

**By segment / driver.** The collapse is entirely transaction-driven (risk-off, low volatility, longer-tail assets hit hardest). S&S — and within it stablecoin — is what held the print together: management explicitly frames S&S at 44% of net revenue as a "durable buffer to volatility," and stablecoin is the growth engine (USDC market cap ~$80bn, Base-chain stablecoin volume up ~10x Y/Y). Institutional transaction revenue actually grew (+37.3% YoY), the one bright spot in transactions. This directly underpins the Spiko/Coinbase Payments story: the stablecoin/USDC franchise is the part of Coinbase compounding while trading is cyclical.

**vs expectations / prior period.** MISS on both lines vs public consensus (StockAnalysis/Zacks/Yahoo aggregators, as of the May 7, 2026 report): revenue ~-6% below the ~$1.5-1.56bn expected; EPS $(1.49) vs ~+$0.29 expected — described in the press as the largest single-quarter negative EPS surprise in recent history. However, the miss is market-cycle-driven (crypto volumes down 28% Q/Q), not a structural break, and the GAAP loss is dominated by a non-cash $482.4M crypto-investment mark. Notably, reported **S&S of $584M landed within/at the midpoint of the company's own Feb-2026 outlook of $550-630M**, and transaction-revenue decline (-23% Q/Q on the deck basis) outpaced the market-volume decline — so on management's own guided metrics the quarter was "within outlook (or better)." No prior COIN earnings note exists in the corpus to `[[wikilink]]`.

**Guidance / forward.** Q2 2026 outlook **introduced** (deck, 2026-05-07): Transaction revenue **~$215M QTD through May 5**; S&S revenue **$565-645M**; Transaction expenses low-to-mid teens % of net revenue; Tech+Dev & G&A $820-870M; S&M $200-300M; SBC ~$240M. The Q2 S&S range ($565-645M) sits roughly flat-to-slightly-up vs Q1's $584M, implying management expects the stablecoin/S&S buffer to hold even if trading stays soft — supportive of the Payments/stablecoin thesis. Management tone: confident on fundamentals and market-share gains ("13th consecutive quarter of positive Adjusted EBITDA," "fortress balance sheet"), while cautioning against extrapolating soft Q2-to-date transaction trends. What they lean away from: the GAAP net loss and the sharp transaction decline are contextualized as macro/market-cycle, with focus steered to S&S durability and non-GAAP EBITDA.

**Thesis-flags.**
1. **Stablecoin is now the growth spine.** Fact: stablecoin revenue +11.5% YoY to $305.4M while nearly every other line fell → why: USDC market cap ~$80bn and rising on-platform balances → why it matters: S&S is 44% of net revenue and counter-cyclical to trading → second-order: partnerships like Spiko/Coinbase Payments (USDC↔T-bills 24/7 settlement) monetize exactly this rail, extending the stablecoin franchise from a rate-driven balance business toward payments/settlement volume.
2. **Earnings quality: the GAAP loss is largely optical.** Fact: $(394)M net loss but $303M positive Adjusted EBITDA → the swing is a $482.4M non-cash crypto-investment mark plus depressed volumes → matters: underlying cash generation persists; the "miss" is cyclical, not a deterioration of the core → second-order: reduces read-through risk to the Payments story, which doesn't depend on trading volumes.
3. **Transaction cyclicality remains the dominant risk.** Consumer transaction revenue -48% YoY; Q2 QTD transaction revenue only ~$215M through May 5 → matters: revenue is still volume/volatility-levered → second-order: raises the strategic value of diversifying into fee/float-light stablecoin-payments flows (the Spiko-type integrations) to de-risk the top line.
4. **Presentation/accounting change on stablecoin revenue.** Corporate USDC-balance revenue reclassified out of Stablecoin revenue into Other/Corporate interest income (effective Q1'26; ~$23.5M restated in the year-ago comp) → matters: watch for optical distortions when comparing stablecoin-revenue growth across periods and vs consensus.

Sources: Coinbase Q1'26 10-Q (period ended 2026-03-31, filed 2026-05-07) — https://drive.google.com/file/d/1aywHuDBKFD9A-xJztm61JN3b8sbodrIj/view (url: https://www.sec.gov/Archives/edgar/data/1679788/000167978826000054/coin-20260331.htm) · Q1'26 earnings deck (8-K EX-99.1, 2026-05-07) — https://drive.google.com/file/d/17UsgGkTaRZxkkSBG7diTaVL_zLBdTa-x/view (url: https://www.sec.gov/Archives/edgar/data/1679788/000167978826000053/q126earningsdeck-finalse.htm) · public consensus (Zacks/StockAnalysis/Yahoo aggregators, as of 2026-05-07): revenue ~$1.5-1.56bn, EPS ~+$0.29 · Note: the 2026-06-18 8-K in ir_latest.json is the 2026 annual-meeting vote (Item 5.07), not an earnings release; Q1'26 remains the latest reported quarter.
<!-- /enrichment:earnings_review -->
