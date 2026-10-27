---
title: "BIS finds Wise, Remitly beat banks and stablecoins on transfer cost"
date: 2026-10-25
retrieved: 2026-10-25
tags:
  - company/wise
  - company/remitly
  - industry/remittances
  - region/global
  - type/research-report
sources:
  - https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: s05a5e8f4
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# BIS finds Wise, Remitly beat banks and stablecoins on transfer cost

> [!info] 2026-10-25 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] BIS сравнил трансграничные переводы через традиционные банки, стейблкойны и финтех-сервисы Wise, Remitly и Western Union. Оказалось, что финтехи существенно дешевле традиционных банков на исследованных направлениях, а стейблкойны пока не демонстрируют устойчивого преимущества по полной стоимости перевода.

## Первоисточники

### bis.org
<https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins>
*BIS Working Paper No. 1385 · Du, Huang, Scharfstein · 2026-10-19*

BIS сравнил трансграничные переводы через традиционные банки, стейблкойны и финтех-сервисы Wise, Remitly и Western Union. Оказалось, что финтехи существенно дешевле традиционных банков на исследованных направлениях, а стейблкойны пока не демонстрируют устойчивого преимущества по полной стоимости перевода.

## Контекст

<!-- enrichment:context -->
**NOTE (source cross-wiring — CORRECTED 2026-10-25):** During ingest the brain step attached the wrong mention_id (a Forbes.ru doctors-and-AI item from "42 секунды") to this story, so the body/`sources` were originally cross-wired. Now repaired: the body, `sources` URL (BIS Working Paper No. 1385) and channel (Финтехно, mention m4c966aa36c) reflect the real BIS cross-border-payments paper. Enrichment below is grounded in that paper.

### [0] What exactly happened (de-PR'd)

On **19 October 2026** the Bank for International Settlements published **Working Paper No. 1385, "Competing rails for cross-border payments: banks, fintechs, and stablecoins"** (authors Wenxin Du, Catherine Huang and David Scharfstein; Du and Scharfstein are academic researchers, the paper is a working paper, not official BIS policy). It builds harmonised, all-in cost measures for sending money across three rails — (1) banks via the correspondent-banking network and SWIFT, (2) non-bank fintech MTOs (Wise, Remitly, and the digital arm of Western Union), and (3) stablecoin transfers over Ethereum / Solana / Tron — across multiple corridors and transfer sizes.

De-PR'd core findings:
- **Fintech MTOs (Wise, Remitly) are the cheapest rail, not stablecoins.** The headline "beats banks AND stablecoins" is accurate to the paper, but note the framing: this is a research paper, not a Wise/Remitly announcement — there is no company PR to de-spin here. The real claim is that fintech MTOs "significantly compressed" cross-border costs, while **stablecoins are "not a panacea."**
- **Banks are the expensive incumbent:** large international banks charge FX margins of roughly **230–470 bps** on retail EUR/USD transfers. (Consistent with World Bank data where bank-channel remittances average ~15% vs ~4.7% for MTOs.)
- **Wise's unit economics, disclosed:** fixed cost of **£0.24 per GBP→EUR transfer**, decomposed as customer support **£0.11**, compliance **£0.06**, and the payment rail itself only **£0.02**. This is the crux of the stablecoin critique: the cheap part (the rail) is already near-free at MTOs; the expensive part (compliance + support) is exactly what stablecoin cost estimates omit.
- **Stablecoins "restructure, don't remove, intermediaries":** a full fiat→stablecoin→fiat trip still needs on-ramp, trading and off-ramp. Centralised exchanges play the correspondent-bank role (on/off-ramps). Exchange trading fees run **0–120 bps** (e.g. Kraken ~100 bps for <$10k/mo volume); a sample USDC-via-Ethereum→Kraken→EUR trip incurred ~$0.19 blockchain fee **plus** a 1% trading fee **plus** a €1 withdrawal fee. On-ramp providers broadly charge 0.5–1.5%.

**Why structured this way / what it reveals:** the paper's real contribution is not "fintechs are cheap" (World Bank already shows that) but **decomposing the fixed-cost stack** to show that the blockchain rail's near-zero marginal cost is a red herring — compliance and customer service dominate and apply to every rail. That reframes the stablecoin-disruption thesis from "cheaper rails win" to "whoever owns compliance + distribution + liquidity wins."

### [1] Competitors / peers

- **Banks (correspondent/SWIFT):** the costly incumbent rail (230–470 bps FX margin; ~15% blended in World Bank data). The paper's "losers" on price.
- **Fintech MTOs — Wise, Remitly, Western Union digital:** the price-setters. Wise's take rate has trended down for years (cross-border "price" ~0.5–0.6% range disclosed in its own reporting); Remitly competes on corridor coverage and payout breadth.
- **Stablecoin/crypto remitters:** Zepz's Sendwave Wallet ([[Zepz launches stablecoin-powered Sendwave Wallet for digital dollars]]), Remitly's own stablecoin wallet ([[Remitly launches stablecoin-powered cross-border wallet]]), MAJORITY, RedotPay, TerraPay/Fipto, Western Union's planned USDPT on Solana. The paper's finding is a direct reality-check on these product narratives.

**Why the lay of the land is this way (second order):** incumbents that own compliance, licences and local payout networks (Wise's own licences across Nigeria, Thailand, UAE; Remitly's cash-pickup partners) capture the durable margin. Stablecoin entrants that still rely on third-party exchanges for on/off-ramp are, per the paper, re-paying for a correspondent-bank-equivalent — they don't escape the cost base they claim to disrupt. This is why even Remitly is building a stablecoin *wallet on top of its own rails* rather than outsourcing to an exchange.

### [2] Company history / fit

Wise and Remitly are the natural "heroes" of this paper because both have spent a decade compressing FX margins and publishing unusually granular cost data (Wise in particular discloses its mission to drive price to zero; it moved its primary listing to the US in 2026 and served ~11M customers on ~£47bn volume). Remitly reported Q4/FY2025 above outlook and is expanding licences (UAE SVF, UK). Both fit the paper's thesis because their edge is operational (compliance automation, payout networks), not a novel "rail" — which is precisely why a blockchain rail doesn't threaten them on cost.

**Why they act this way:** commodity-like transfer margins force scale + software leverage; the only way to a durable moat is lowering the fixed compliance/support cost per transfer, which rewards volume leaders and punishes sub-scale crypto entrants.

### [3] Novelty / value-add / traction

**What's genuinely new:** the first-order contribution is a **harmonised, apples-to-apples cost dataset** across all three rails (intraday MTO pricing + World Bank data + bank-wire transactions + crypto market data) and the **fixed-cost decomposition** showing compliance/support >> rail cost. That is a real analytical advance over the World Bank's provider-level averages.

**Traction/impact (analysis):** the paper is already shaping the stablecoin-vs-incumbents debate (covered by Payment Expert, Crowdfund Insider, Genfinity, etc.) and lands amid heavy GENIUS-Act stablecoin momentum — it's a credibility counterweight to "stablecoins will gut remittances." Value-add is real because it's falsifiable (numbers, not vibes) and from a central-bank-adjacent source.

**Who captures the margin:** per the paper, the MTO that owns compliance + distribution — not the blockchain. Stablecoins shift the toll from correspondent banks to exchanges, so exchanges/liquidity venues capture the on/off-ramp margin, not end-users.

### [4] What's next / market sentiment

The paper arms regulators and incumbents against the "stablecoins disrupt remittances" narrative just as US stablecoin issuance accelerates post-GENIUS. Expect it cited in CBDC / cross-border policy debates (BIS's Project mBridge / Nexus lineage) and by MTOs defending their moats. Risk to the thesis: stablecoin on/off-ramp costs could fall sharply if exchanges commoditise or if issuers vertically integrate licensed on/off-ramps (Western Union USDPT, Circle) — the paper measures *today's* cost structure, which is the counterintuitive second-order point: the rail is cheap, the *institutional* layer is not, and that's where future disruption (or not) will actually happen.

### Sources
- BIS WP 1385, "Competing rails for crossborder payments: banks, fintechs, and stablecoins" (19 Oct 2026): https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
- HBS working-paper page (authors Du, Huang, Scharfstein): https://www.hbs.edu/faculty/Pages/item.aspx?num=68673
- Genfinity analysis (exchange fees, on/off-ramp): https://genfinity.io/2026/10/20/bis-stablecoin-cross-border-payments-not-a-panacea/
- Payment Expert / Crowdfund Insider reporting: https://paymentexpert.com/2026/10/23/bis-paper-stablecoins-payment/ ; https://www.crowdfundinsider.com/2026/10/319582-bis-paper-finds-stablecoins-compete-with-cross-border-banking-infrastructure/
- Fintech.garden (Wise £0.24 fixed-cost decomposition): https://fintech.garden/news/2026-10-22-bis-study-puts-fintech-money-transfers-ahead-of-banks-on-cost-but-finds-stableco/
- World Bank Remittance Prices Worldwide (6.36% global avg; banks ~15%, MTOs ~4.7%): https://remittanceprices.worldbank.org/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5** — a genuinely new, well-grounded BIS research paper (WP 1385, 19 Oct 2026) with a non-obvious, falsifiable contribution (fixed-cost decomposition proving the blockchain rail is the cheap part and compliance/support the expensive part). Not a company event and no new product/adoption, so not top-tier, but it meaningfully reframes the stablecoin-vs-incumbents cost debate and is being widely cited — above routine for a research item.

1. Is the headline claim ("beats banks AND stablecoins") the paper's own conclusion or media spin? — Paper's: it explicitly says fintech MTOs "significantly compressed" costs and stablecoins are "not a panacea." Accurate.
2. Is this an official BIS position or a working paper? — Working paper by Du/Huang/Scharfstein; carries the standard "views are the authors'" disclaimer. Don't present as BIS policy.
3. Does it compare like-for-like? — It constructs harmonised all-in costs across corridors/sizes from MTO intraday pricing + World Bank data + bank wires + crypto data. Methodology is explicitly cross-rail; main validity risk is whether the stablecoin sample corridors/fee tiers are representative. Open on exact corridor set.
4. The £0.24 Wise fixed cost — is it marginal or fully-loaded? — Fixed cost per GBP→EUR transfer, split support £0.11 / compliance £0.06 / rail £0.02. It's Wise's own cost, not the price charged to users (separate FX margin). Don't conflate cost with price.
5. Does "stablecoins lose on cost" hold at larger ticket sizes? — Fee structure differs: stablecoin fixed/percentage fees may invert vs MTOs at high value or exotic corridors. The paper varies transfer size; verdict likely corridor/size-dependent — open on where stablecoins actually win.
6. Are the exchange fees (0–120 bps; Kraken 100 bps <$10k) current and representative? — Snapshot of ~six CEXs; fees fall with volume and vary by venue, so the "stablecoins expensive" result is partly an artifact of retail-tier exchange pricing. Real risk to durability of the finding.
7. Does it account for speed/finality value, not just cost? — Appears cost-focused; stablecoins' settlement-speed advantage isn't a cost line, so a pure-cost comparison understates their value proposition. Open.
8. Is the World Bank "banks ~15%" figure consistent with the paper's 230–470 bps bank FX margin? — Different metrics (all-in blended cost vs FX margin component). Both point the same direction (banks costliest) but aren't the same number; don't equate.
9. Could vertical integration flip the result? — Yes: issuers/MTOs owning licensed on/off-ramps (Western Union USDPT, Circle) could collapse the exchange toll the paper measures. The finding is time-stamped to 2026 fee structures. Key second-order caveat.
10. Why did the primary-source body originally show Russian doctors and AI? — Ingest cross-wiring (wrong mention_id attached); CORRECTED 2026-10-25 to the real Финтехно/BIS mention (m4c966aa36c) + BIS WP 1385 URL. Enrichment is grounded in the BIS paper.
11. Is this a duplicate of any prior corpus note? — No. Prior remittance/stablecoin notes (Zepz Sendwave, Remitly stablecoin wallet) are product launches; no prior note covers WP 1385 or this cost-comparison finding. FRESH.
12. Who benefits from amplifying this paper? — Incumbent MTOs and bank/regulator camps resisting the stablecoin-disruption narrative; stablecoin skeptics. Doesn't invalidate the data but note the receptive audience.
13. Does it change adoption behaviour, or just the discourse? — Research only; no measured change in flows/volumes. Impact is narrative/policy, not operational — caps importance.
14. Is Remitly's inclusion as a "winner" accurate given it is also building stablecoin products? — Yes, consistent: Remitly wins on its MTO rail while hedging with a stablecoin wallet on its own infrastructure, reinforcing the "owning compliance/distribution matters more than the rail" thesis.

Duplicate verdict: **FRESH** — new 19 Oct 2026 BIS working paper; no prior corpus coverage of this finding.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-27]] (2026-10-27).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Cross-border consumer payments/remittances. The World Bank's SDG target is to drive the global average cost of sending $200 below 3%; actual averages have stuck well above that (roughly 6%+ for bank channels), which is exactly the wedge fintech MTOs exploit. The BIS working paper 1385 (*Competing rails for cross-border payments: banks, fintechs and stablecoins*, Oct 2026) quantifies the gap: fintech MTOs' all-in cost runs ~40–150bps, vs bank FX markups of ~2.0–4.7% even on liquid pairs *before* explicit wire fees; for a $10k US outbound transfer, median cost via fintechs like Wise/Remitly is ~$40–60 (per BIS, via Finextra/PaymentExpert, 2026-10). Structure: fragmented at the consumer edge (hundreds of MTOs) but the underlying rails are concentrated (correspondent banks, a few network/liquidity providers); value accrues to whoever owns the FX spread + payout network, and barriers are regulatory (money-transmitter/e-money licences per corridor) rather than capital. "Why now": the stablecoin remittance narrative is the live driver — but BIS's headline finding is that stablecoins do *not* disintermediate; fiat⇄stablecoin conversion and exchange withdrawal fees reinsert intermediaries, so crypto exchanges "still act like correspondent banks." Negligible on-chain gas is offset by on/off-ramp friction, so stablecoins price near wholesale FX only on major pairs and lose the cost race on consumer-sized tickets.

**Competitive landscape.** Sector KPIs: cross-border volume (TPV), **take rate** (net revenue / volume), active customers, cost-per-corridor. Players: cost leader **Wise** (infrastructure-led, thinnest take rate); consumer-remittance scaler **Remitly** (emerging-market payout breadth); legacy incumbents **Western Union / MoneyGram** (cash network, highest cost, pivoting to stablecoins — WU's USDPT on Solana, MoneyGram+Plaid); crypto-native entrants (**Zepz/Sendwave** stablecoin wallet, [[Zepz launches stablecoin-powered Sendwave Wallet for digital dollars]]; TerraPay, Thunes pay-to-stablecoin). Basis of competition: price + payout reach, not product. Recent moves: Wise cut blended take rate to 0.52% in FY26 (deliberate price-for-volume), Remitly surpassed 10M active customers in Q2 2026. Position: Wise is *ahead* on raw cost (infra ownership = structural moat via network-effect liquidity + regulatory licence stack); Remitly is the consumer-distribution leader but at a structurally higher take rate because it serves smaller, harder emerging-market tickets. The BIS finding is effectively a third-party validation of both firms' core moat — independent cost leadership — which is reputationally valuable in a sector where cost is the product.

**Comps & multiples.**
- **Wise plc** (LON:WISE / WSE): market cap ~$11.0bn (as of 2026-10-22, per stockanalysis). FY26 net revenue $2,502.8m, cross-border volume $243.5bn → take rate = $2,502.8m-equivalent cross-border portion / $243.5bn; reported blended **take rate = 0.52%** (down 6bps from 0.58%). **P/S ≈ $11.0bn / $2.5bn = 4.4x**. Volume +31%, net revenue +19%, active customers +21% to 19M.
- **Remitly** (NASDAQ:RELY): market cap ~$5.3bn (2026-10-23, per stockanalysis/companiesmarketcap). FY26 revenue guidance $1.978–1.988bn (+21–22%); send volume ~$23.5bn in Q2 alone. **Take rate ≈ 2.05%** (Q1 2026) — ~4x Wise's, reflecting smaller EM tickets. **P/S ≈ $5.3bn / $1.98bn = 2.7x**.
- Internal comps: [[Remitly reports Q4 and full year 2025 results above outlook]] (first full-year GAAP profit; Q4 rev $442.2m, net income $41.2m), [[Wise serves 11 million customers as volumes hit £47 billion]] (Q3 FY26 CB volume £47.4bn, +26%).
- **Flags:** Wise at 4.4x P/S vs Remitly 2.7x — Wise rich vs Remitly, but defensible: Wise is pure-play infra with structurally lower cost and a wider product/holdings mix (card +40%, Wise Assets); Remitly's lower multiple reflects single-product consumer-remittance concentration and US-listing discount. Both inside a reasonable P/S band for profitable, 20–30%-growth payments names — neither is an outlier on a growth-adjusted basis. EV/EBITDA not computed (net cash/float distorts EV; "no data" for a clean figure).

**Risk flags.**
1. **Take-rate compression is strategic, not forced — but it's one-way.** Wise's 6bps/yr cut is a deliberate price-for-share lever; it works only while volume growth (+31%) more than offsets the rate drop (+19% revenue). If volume growth decelerates, the same strategy inverts into revenue stall — the moat (lowest cost) is also the ceiling on pricing power.
2. **Disintermediation risk is low from stablecoins but real from incumbents going cheap.** BIS defuses the stablecoin threat (exchanges reinsert cost), but the second-order risk is incumbents (WU/MoneyGram) and banks adopting stablecoin/real-time rails to close the cost gap, eroding the fintechs' headline advantage over time.
3. **Regulatory/corridor concentration.** Cost leadership depends on a per-corridor licence stack (Wise's Belgian criminal probe over suspicious transactions is a reminder that compliance cost can spike and asymmetrically hit the thin-margin cost leader hardest).

**What this changes (idea-lens).** The BIS paper reframes the stablecoin-remittance hype from "banks and MTOs get disrupted" to "incumbent fintechs (Wise, Remitly) are the current cost frontier, and stablecoins are a rail they can adopt rather than a competitor that replaces them" (analysis). Falsifiable thesis: if on/off-ramp (fiat⇄stablecoin) fees fall sharply — e.g. licensed-bank minting at scale under new stablecoin regimes — the BIS cost-ordering could flip for large-ticket corridors; watch stablecoin all-in cost for sub-$200 consumer tickets as the trigger. Until then, the cost crown and its validation stay with the MTOs.

Sources: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins · https://www.finextra.com/newsarticle/48630/fintechs-top-banks-and-stablecoins-for-cheap-cross-border-payment---bis-research · https://paymentexpert.com/2026/10/23/bis-paper-stablecoins-payment/ · https://owners.wise.com/news-releases/news-release-details/wise-fy26-results · https://www.sec.gov/Archives/edgar/data/0001782170/000162828026053361/rely2q26-earningspr.htm · https://stockanalysis.com/stocks/wse/market-cap/ · https://stockanalysis.com/stocks/rely/market-cap/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** IN-LINE / modest BEAT on growth, with the stock dipping on margin optics. FY2026 (year ended 31 March 2026, reported in USD after the US re-domicile) · net revenue $2,502.8m (+19% YoY) · cross-border volume $243.5bn (+31% YoY, vs FY25 $185.2bn) · income before tax $660.4m (26% margin) · blended cross-border take rate 0.52% (down 6bps from 0.58%). Wise reaffirmed its 15-20% medium-term net-revenue-growth target and guided FY27 growth "around the middle" of that range. Verdict for the BIS cost-leadership thesis: Wise's own filing directly corroborates it — the firm is deliberately cutting price (take rate) to compound volume.

**Key figures (with growth).**
- Cross-border volume: $243.5bn, +31% YoY (FY25 $185.2bn). Volume grew ~12pp faster than net revenue — the mechanical signature of a falling take rate, i.e. customers paying less per dollar moved.
- Net revenue: $2,502.8m, +19% YoY.
- Blended cross-border take rate: 0.52% (52bps), down 6bps from FY25's 0.58%. Management explicitly framed this as a customer benefit: "Customers benefited from our low pricing, with an average take rate of just 52bps."
- Income before tax: $660.4m, margin ~26%.
- Interest income on customer balances: ~$806m for FY26 (the float, not transfer fees — material to margin, see thesis-flag).
- Active customers: up 21% YoY to ~19m (Personal ~10.7m, Business ~0.6m active in Q4).
- Speed: 75% of Q4 payments globally completed in under 20 seconds.

**By segment / driver.** Growth is volume-led, not price-led. The engine is Wise's "scale economies shared" flywheel: lower unit cost → lower price (take rate) → more volume/customers → still lower unit cost. Take-rate compression is therefore the intended output of the model, not a demand problem. Interest income on the ~$806m float is the second income leg that lets Wise keep transfer pricing aggressive while holding a 26% PBT margin — a structural advantage incumbent banks and most stablecoin rails lack.

**vs expectations / prior period.** No internal-corpus prior report available (semsearch/irdb down — see sources). vs prior year (FY25: volume $185.2bn, take rate 0.58%, net revenue ~$2,103m [implied by +19%]): clear acceleration in volume (+31%) alongside deliberate price reduction (take rate -6bps). Public analyst reaction: growth was solid but the stock dipped, with commentary flagging (a) opex growth outpacing revenue and (b) continued take-rate cuts — management signalled a further ~1-2bps quarterly reduction into FY27. So the "miss" read, where it exists, is on margin optics, not on the transfer-cost thesis.

**Guidance / forward.** Reaffirmed, not raised: FY27 net-revenue growth "around the middle" of the 15-20% medium-term range; income-before-tax margin "around the top of the 20-25% range" (above the 15-20% long-run target while Wise is not yet paying out additional interest to customers). Management guided a further ~1-2bps per quarter take-rate reduction — i.e. it is pre-committing to cheaper transfers, the strongest possible endorsement of the BIS cost-leadership finding from the company's own mouth.

**Thesis-flags (for the BIS "cheapest cross-border channel" claim).**
1. SUPPORTS: A 52bps blended take rate, falling ~6bps/year by design, is a hard number backing the BIS claim that Wise beats banks (typically well above 1% all-in) on transfer cost. Fact → Wise cuts price as it scales → the cost gap vs banks widens, not narrows → BIS's finding should strengthen over time, not be a one-off snapshot.
2. SUPPORTS but with nuance vs stablecoins: Wise's edge is not just fee level but delivered FX + speed (75% of payments <20s) with no on/off-ramp or wallet-conversion friction. Against stablecoin rails the relevant cost is all-in (spread + on-ramp + off-ramp), where Wise's single mid-market-rate + flat fee is price-transparent. Second-order: stablecoin cost advantage is concentrated in corridors where Wise lacks local rails; Wise's 31% volume growth suggests it is not losing the mainstream consumer corridor.
3. COMPLICATES (margin, not cost-leadership): the cost leadership is partly funded by ~$806m of interest income on the float. If rates fall, Wise must either accept thinner margins or slow take-rate cuts — the only realistic threat to the "keeps getting cheaper" dynamic. De-PR read: management is loud on the 52bps "low pricing" headline and quieter on the fact that the 20-25% margin leans on interest income it is "not yet" sharing with customers.
4. WATCH: opex growth > revenue growth in FY26 (flagged by analysts, drove the stock dip). This is a profitability flag, not a transfer-cost flag; it does not weaken the BIS finding but caps how aggressively the price-cut flywheel can run if cost discipline slips.

Sources: Wise Group plc FY2026 earnings release (6-K Exhibit 99.1, SEC, FY ended 31 Mar 2026) https://www.sec.gov/Archives/edgar/data/2099039/000119312526282767/d117224dex991.htm · Wise FY26 Annual Report (Form 20-F) https://www.sec.gov/Archives/edgar/data/2099039/000119312526282911/d17323d20f.htm · analyst reaction (public): Investing.com FY2026 earnings-call transcript ("stock dips"), Pursuit of Compounding "Wise FY26 Update: One Basis Point at a Time" · Internal corpus semsearch/irdb unavailable (OpenRouter 402, insufficient credits) — figures taken directly from the SEC primary filing, not consensus feeds. Prior-year and segment-level net-profit detail: [UNSOURCED beyond release summary].
<!-- /enrichment:earnings_review -->
