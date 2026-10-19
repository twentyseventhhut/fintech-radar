---
title: "Marqeta and Coinbase collaborate on stablecoin-backed card payments"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/marqeta
  - company/coinbase
  - industry/stablecoins
  - region/us
  - type/partnership
sources:
  - https://www.businesswire.com/news/home/20261016304815/en/Marqeta-and-Coinbase-Collaborate-to-Enable-Stablecoin-Backed-Card-Payments
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sc6fa7acf
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Marqeta and Coinbase collaborate on stablecoin-backed card payments

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Marqeta and Coinbase collaborate to enable stablecoin backed card payments. The two companies are teaming up so that stablecoins can back payments made with cards. The collaboration links both firms around card spending funded by stablecoins.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261016304815/en/Marqeta-and-Coinbase-Collaborate-to-Enable-Stablecoin-Backed-Card-Payments>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Marqeta and Coinbase collaborate on stablecoin-backed card payments
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **16 Oct 2026** Marqeta (NASDAQ: MQ) and Coinbase announced an **expansion of their existing (multi-year) relationship** into **stablecoin-backed card issuing for enterprises**. The division of labor is the whole story:
- **Coinbase** = custody of the stablecoin balances + the on/off conversion between stablecoin and fiat; **Base** (Coinbase's L2) provides the on-chain settlement rail.
- **Marqeta** = card issuing + payment processing + the **bank and card-network relationships** (the regulated plumbing that lets the card run on Visa/Mastercard rails at "millions of merchants").
- **Capability promised:** a business can issue cards that **spend directly from a stablecoin balance** at any card-accepting merchant, and can **fund card programs 24/7** (no bank-hours cutoff) — the stablecoin is converted to fiat at authorization so the merchant is paid in normal money.
- **De-PR'd / what's vague (the real point):** the 16 Oct release names **no first customer, no availability/GA date, no supported jurisdictions, no production milestone, no volumes, no take-rate, and does not name the stablecoin(s)/chains** beyond "Base." So this is **announced, not demonstrably live** — a capability/go-to-market announcement, not shipped adoption. (Contrast: the same partners' consumer product, the Coinbase One Card, is already live and *already runs on Marqeta* — see [[Coinbase expands Coinbase One Card to all US users]].)
- **Why structured exactly this way:** the design cleanly **quarantines crypto risk inside Coinbase** (custody + conversion) while Marqeta keeps the **regulated card-issuing / BIN-sponsor / network leg** — the same "crypto-native does the tokens, regulated party does the money/rails" pattern seen in [[Citi details stablecoin checkout with Coinbase]]. It lets Marqeta offer "stablecoin cards" to its enterprise base **without taking custody or token exposure**, and lets Coinbase monetize custody + conversion + Base settlement as reusable B2B infrastructure. The second-order read: Marqeta is **renting Coinbase's stablecoin rail** the same way Citi is — Coinbase accretes the horizontal infra it can resell, while each partner contributes distribution. (analysis)

## [1] Competitors / peers
Stablecoin card **issuing/enablement** is already a crowded, faster-moving field than this announcement implies:
- **Rain** (valued ~$1.95bn) — the clear leader in enterprise "spend-from-stablecoin-treasury" cards; settles with **Visa 7 days/week in USDC**, issues with both Visa and **Mastercard** ([[Rain launches embedded stablecoin wallets for partners]], Fortune 2026-05). Directly overlaps Marqeta+Coinbase's enterprise pitch and is **already live with named programs**.
- **Baanx** — pioneered the **self-custody** card (spend from the user's own wallet until point of spend); a structurally different, more crypto-native model than Marqeta/Coinbase's **custodial** design.
- **Stripe (Bridge + Privy)** — expanding stablecoin **cards to 100+ countries by year-end**, customers include Kraken/Ramp/Morse; ~$1.2bn/mo stablecoin card spend, 3x YoY ([[Stripe to expand stablecoin cards to 100+ countries]]). Stripe owns issuing + Bridge infra end-to-end — the most vertically integrated competitor.
- **The networks themselves:** Visa passed a **~$20bn annualized stablecoin settlement run-rate (Sep 2026, ~15x YoY) across 160+ stablecoin-linked card programs**; Mastercard pushing hard too ([[Финтехно Visa and Mastercard embed stablecoins into payment rails]]). The rails are commoditizing the capability from above.
- **Position:** Marqeta+Coinbase are **catching up / at parity on capability, behind on traction.** The capability (spend stablecoin → auto-convert → card rails) is shipping at Rain, Stripe, Baanx and 160+ Visa programs. What's differentiated is the **combination of Coinbase's custody/Base + Marqeta's enterprise issuing book** — but that is a packaging edge, not a first-mover edge. (analysis)
- **Why the landscape is this way / second order:** the durable margin sits with whoever owns **conversion + settlement float + the BIN/network relationship**, not the "stablecoin card" brand. Coinbase is becoming the custody/conversion layer behind many front-ends (Citi, Marqeta, Yuno, Samsung); Marqeta is the issuing layer behind many brands. Their deal fuses two horizontals — but it also means **neither owns the full stack**, and Rain/Stripe (who do) can undercut on economics. (hypothesis)

## [2] Company history / fit
- **Marqeta's logic:** Marqeta is a **commodity card-issuing processor** whose revenue is heavily concentrated in Block/Cash App and under take-rate pressure — it has spent 2025-26 explicitly **diversifying** ([[Marqeta turns to BNPL to diversify revenue beyond Block]], [[Marqeta completes TransactPay acquisition]] for EU issuing, [[Marqeta expands account and money movement offering in Europe]], [[Marqeta delivers AI-driven risk decisioning for fraud prevention]]). Bolting a **stablecoin funding source** onto its issuing stack is a logical new program type to sell into its enterprise base and defend against Rain/Stripe eating the "crypto-native issuing" segment. Structural pressure: **commodity take-rate → must add differentiated program types** to protect volume. (analysis)
- **Coinbase's logic:** Coinbase is pivoting toward **Subscription & Services** revenue as transaction/trading revenue craters (stablecoin ~25% of total net revenue, ~52% of S&S in 2026; USDC balances at ATH). Every custody/conversion/Base deal (Citi, Marqeta, etc.) feeds the **durable S&S engine** and extends Base as the default settlement chain — see the earnings detail in [[Citi details stablecoin checkout with Coinbase]]. (analysis)
- **Fit:** genuinely logical for both — and notably the two **already work together** (Coinbase One Card is issued on Marqeta), so this is an **expansion of a real, operating relationship**, not a cold new tie-up. That lowers execution risk but also means the "new partnership" framing oversells the novelty.

## [3] Novelty / value-add / traction
- **What's actually new:** combining **Coinbase custody + Base settlement** with **Marqeta's regulated enterprise issuing** into a single enterprise offering — i.e., Marqeta's existing customers can now spin up stablecoin-funded card programs without picking a separate crypto issuer. Incrementally useful for firms already on Marqeta.
- **Not new / overstated:** the **underlying capability** (spend from a stablecoin balance via card rails, auto-converted) is **already live** at Rain, Stripe, Baanx, and 160+ Visa programs. "Mainstream" framing (per PYMNTS) is PR; this is a late-ish entrant packaging existing primitives.
- **Traction: essentially zero disclosed.** No first customer, no GA date, no jurisdictions, no volumes. By contrast Rain/Stripe cite real programs and spend figures. Treat this as **intent, not adoption.**
- **Who captures the margin / what breaks it:** Coinbase captures **custody + conversion spread + Base settlement fees** (reusable across partners); Marqeta captures **issuing/processing fees + the network/BIN relationship**. But because **neither owns the full stack**, the economics are split two ways and exposed to vertically integrated rivals (Rain, Stripe) who keep the whole spread. Conversion economics are also **interest-rate / USDC-float sensitive** on Coinbase's side. The value-add is real as a **defensive product-line extension**, not a step-change moat. (analysis)

## [4] What's next / market sentiment
- **Watch for:** a **named first enterprise customer**, a GA/pilot date, supported jurisdictions, and any program volume — all absent today. Also whether it runs USDC-only or multi-stablecoin, and whether it's Visa, Mastercard, or both.
- **Sentiment:** framed bullishly for **COIN** (Yahoo/Seeking Alpha flagged "Coinbase stock in focus / payments reach expands"); the narrative is the 2026 convergence of regulated payments incumbents onto crypto-native stablecoin rails under GENIUS-era US clarity.
- **Counterintuitive second-order:** each incremental "issuer/bank picks Coinbase + Base as the stablecoin rail" **commoditizes the individual partnership** and entrenches Coinbase/Base (and Visa/MC on the network leg) as the strategic winners — the more such deals exist, the **less differentiating any single one is**, and the more value concentrates in the shared rails rather than in Marqeta's or any issuer's brand. Marqeta's defensive move could deepen its dependence on the very intermediary (Coinbase) that commoditizes issuing. (hypothesis)

## Sources
- Marqeta IR / BusinessWire release (16 Oct 2026): https://www.businesswire.com/news/home/20261016304815/en/Marqeta-and-Coinbase-Collaborate-to-Enable-Stablecoin-Backed-Card-Payments
- Marqeta investor relations: https://investors.marqeta.com/news-releases/news-release-details/marqeta-and-coinbase-collaborate-enable-stablecoin-backed-card
- The Block (16 Oct 2026): https://www.theblock.co/news/business/2026-10-16-coinbase-to-power-stablecoin-backed-cards-for-marqeta-customers-418833
- Crypto Briefing: https://cryptobriefing.com/coinbase-marqeta-stablecoin-payment-cards/
- PYMNTS: https://www.pymnts.com/blockchain/2026/marqeta-and-coinbase-take-stablecoin-spending-mainstream/
- Seeking Alpha (MQ): https://seekingalpha.com/news/4653795-marqeta-and-coinbase-team-up-for-stablecoin-backed-card-payments
- Rain / Visa landscape: https://fortune.com/2026/05/04/mastercard-rain-stablecoin-startup-institutional-customers-partnership/ ; https://insights4.vc/blog/the-state-of-stablecoin-cards-2026/
- Internal: [[Coinbase expands Coinbase One Card to all US users]], [[Citi details stablecoin checkout with Coinbase]], [[Stripe to expand stablecoin cards to 100+ countries]], [[Rain launches embedded stablecoin wallets for partners]], [[Marqeta turns to BNPL to diversify revenue beyond Block]], [[Финтехно Visa and Mastercard embed stablecoins into payment rails]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is it live or just announced?** → **Announced, not demonstrably live.** The 16 Oct release gives no first customer, no GA/pilot date, no jurisdictions, no production milestone. Treat as intent, not adoption.
2. **Is this actually new, or the activation of an old relationship?** → Expansion of a **pre-existing, operating** tie-up: the consumer Coinbase One Card already runs on Marqeta ([[Coinbase expands Coinbase One Card to all US users]]). The "new partnership" framing oversells it — this is a new *product line* on an old relationship.
3. **Is this a duplicate of the Citi+Coinbase stablecoin deal?** → **No.** [[Citi details stablecoin checkout with Coinbase]] is **merchant acceptance / checkout, Citi as bank of record**. This is **card issuing / spend-from-stablecoin-balance, Marqeta as issuer/processor on Base**. Different side of the transaction, different regulated partner → **fresh**, not stale.
4. **Which stablecoin(s) and chains?** → **Only "Base" named.** Specific stablecoin(s) (USDC? others?) and whether multi-chain is **undisclosed**.
5. **Who captures the margin?** → Split: Coinbase = custody + conversion spread + Base settlement fees; Marqeta = issuing/processing + network/BIN relationship. **Neither owns the full stack** → economics shared two ways, exposed to vertically integrated rivals. Take-rate undisclosed.
6. **How does it differ from Rain / Stripe / Baanx?** → Same core capability, which is **already live** at Rain (Visa 7-day USDC settlement), Stripe (Bridge, 100+ countries), Baanx (self-custody). Marqeta+Coinbase are **catching up on a packaging edge**, not first movers.
7. **Custodial or self-custody?** → **Custodial** (Coinbase holds the balances) — the opposite of Baanx's self-custody model; relevant for crypto-native customers who want to keep keys.
8. **Who bears fraud / chargeback / settlement-risk liability?** → **Open.** PR silent. Structure implies Coinbase holds crypto/conversion risk and Marqeta handles card-network dispute flows, but terms undisclosed.
9. **Any exclusivity?** → **No evidence.** Coinbase simultaneously powers Citi, Samsung, Yuno, etc.; Marqeta serves many issuers. Non-exclusive on both sides.
10. **Any traction numbers?** → **None.** No program count, no volume, no committed enterprise logo — vs. Rain's named programs and Stripe's ~$1.2bn/mo stablecoin card spend.
11. **Is the capability itself commoditizing?** → Yes — Visa alone has **160+ stablecoin-linked card programs** at a ~$20bn annualized settlement run-rate (Sep 2026, ~15x YoY). The networks are absorbing the function from above.
12. **Why does Marqeta need this?** → Defensive diversification: commodity issuing processor, Block-concentrated revenue, under take-rate pressure ([[Marqeta turns to BNPL to diversify revenue beyond Block]]) → needs differentiated program types to defend against Rain/Stripe.
13. **Why does Coinbase need this?** → Feeds its S&S/stablecoin revenue pivot (stablecoin ~25% of net revenue, ~52% of S&S in 2026) and entrenches **Base** as default settlement chain. Another reusable B2B infra deal.
14. **Second-order risk to Marqeta?** → Each such deal **deepens dependence on Coinbase** and entrenches the intermediary that commoditizes issuing; concentrates strategic value in shared rails (Coinbase/Base, Visa/MC), not Marqeta's brand. (hypothesis)
15. **What would raise the verdict?** → A named enterprise customer + GA date + jurisdictions + any disclosed program volume. Absent those, it is a credible-but-early capability announcement.

**Importance: 3/5** — rationale: A logical, on-thesis expansion of a real operating relationship (Coinbase One Card already runs on Marqeta), fusing Coinbase custody/Base with Marqeta's regulated enterprise issuing — genuine signal that stablecoin card issuing is mainstreaming, and strategically meaningful for both (Marqeta diversification, Coinbase S&S/Base). But it is **announced with zero disclosed traction** (no customer, date, jurisdiction, volume, or named stablecoin beyond Base), the **core capability is already live** at Rain/Stripe/Baanx and across 160+ Visa programs, and neither party owns the full stack. Not 2 (it's a real product line on a real relationship, not a rumor/explore); not 4 (no traction, not clearly live, late-ish entrant). Fresh, distinct from the Citi+Coinbase checkout deal.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Stablecoin-linked card issuing has gone from crypto perk to a fast-scaling rail in 2026. Per Visa (via pymnts/onebullex, Sep 2026), Visa's stablecoin settlement hit a ~$20bn annualized run-rate, ~15x a year earlier, across 130+ crypto/stablecoin card programs; crypto-funded card spend is running at roughly ~$18bn annualized and could approach ~$30bn by year-end 2026 (per insights4vc/spark.money, 2026). Structure: the value chain splits into custody/FX (Coinbase, Circle), on-chain settlement (Base, other L2s), card issuing/processing (Marqeta, Rain, Reap, Baanx, Immersve), and the scheme rails (Visa >90% of on-chain card volume; Mastercard largely in pilot). Barriers are regulatory (money-transmission, BIN sponsorship) and distribution (merchant acceptance) — not the tech. "Why now": the US GENIUS Act gave stablecoins a federal framework, and on 2026-10-02 Stripe/Visa/Mastercard/Coinbase/Shopify launched Open USD (OUSD, issued by Stripe's Bridge) — so the incumbents are actively building the rails this deal plugs into (per techtimes/forbes, Oct 2026).

**Competitive landscape.** Sector KPIs: TPV/card spend volume, take rate, and reserve/float economics (who earns the yield on stablecoin balances). Players and basis of competition: Stripe/Bridge competes on distribution + bundling (expanding Visa stablecoin cards from 18 to 100+ countries by end-2026, per onebullex Oct 2026); Coinbase competes on custody + USDC economics (it captures ~50% of all USDC economics and held a record ~$20bn avg USDC in Q2 2026, per Coinbase Q2'26); Marqeta competes on modern card issuing/processing. Recent moves: 2026-10-16 Marqeta×Coinbase (this note) — Coinbase handles custody/FX, Base provides settlement, Marqeta issues/processes; crucially merchants do NOT settle on Base or hold stablecoin — the balance converts to fiat inside the card flow using existing acceptance (per theblock/pymnts). This extends a six-year Marqeta–Coinbase relationship (Coinbase One Card already runs on Marqeta). Protagonist position: Marqeta is the issuing layer — a credible, catching-up specialist rather than a rails owner; its moat is switching costs on embedded issuing programs and scale (analysis). Coinbase is ahead on custody/USDC distribution.

**Comps & multiples.** Reported figures as PRIMARY evidence:
- **Marqeta (MQ, EDGAR 8-K/IR):** Q1 2026 TPV $112bn (+33% YoY), net revenue $166m (+19%), gross profit $118m (+19%), first-ever GAAP net income $8m, adj. EBITDA $33m (per IR 2026-05-05, EDGAR filing). High-volume, thin-take-rate processor (net revenue ≈ 0.15% of TPV).
- **Coinbase (COIN, EDGAR 8-K):** Q2 2026 total revenue $1.2bn (down from $1.5bn YoY), transaction rev $599m, subscription & services $555m (record 48% of net rev), net LOSS $359.5m, adj. EBITDA $208m (14th straight positive); stablecoin revenue $292m (−$17m YoY, missed ~$327m est); avg USDC held record ~$20bn, >30% of USDC in circulation (per Coinbase Q2'26, EDGAR).
- **Internal comps:** [[Coinbase expands Coinbase One Card to all US users]]; [[Coinbase launches Coinbase Business stablecoin payment tools]]; [[Marqeta powers Klarna debit card expansion in Europe]]; [[Visa to pilot pre-funded stablecoins via Visa Direct]]; [[Coinbase and Mastercard in talks to buy stablecoin firm BVNK]].
- EV/Revenue, EV/EBITDA, P/E: distribution not computed — market caps/EV not sourced here, so trading multiples = `[UNSOURCED]`. Qualitative: Marqeta just turned GAAP-profitable at scale; Coinbase remains revenue-cyclical (trading-driven) and posted a net loss despite record USDC float.

**Risk flags.**
1. **Disintermediation by the rails owners.** The exact economics this deal targets — convert-at-point-of-spend stablecoin cards — are being standardized by Stripe/Bridge + Visa/Mastercard + Coinbase themselves via Open USD (2026-10-02). Coinbase is on both sides; a Marqeta issuing partner is more substitutable than a scheme or a custodian, risking margin capture above Marqeta's layer.
2. **Reserve/float economics undisclosed.** Neither firm's PR states who earns the yield on the stablecoin balances or the card take-rate split — and Coinbase's stablecoin revenue just FELL YoY, so the economics backing "24/7 funded card programs" are unproven (de-PR: "announced," not "live/adopted").
3. **Regulatory/concentration.** Stablecoin card programs depend on GENIUS-era rules staying favorable and on Visa acceptance (>90% of on-chain card volume) — a scheme or regulatory shift would hit the whole convert-to-fiat model; Marqeta also carries known client-concentration history (Block).

**What this changes (idea-lens).** This is an incumbent-led mainstreaming, not a disruption: by converting stablecoin to fiat inside the existing card flow, Marqeta/Coinbase expand stablecoin spend WITHOUT forcing merchants onto Base — the rails win either way (analysis). Falsifiable thesis: stablecoin card volume keeps compounding toward ~$30bn annualized into 2027 and Marqeta books measurable new issuing TPV from crypto-funded programs. Trigger/what breaks it: watch Marqeta's next 10-Q for any disclosed stablecoin/Coinbase program TPV; if Open USD / Bridge-issued cards capture the issuing economics, Marqeta stays a commoditized processor and the thesis weakens.

Sources: https://www.businesswire.com/news/home/20261016304815/en/Marqeta-and-Coinbase-Collaborate-to-Enable-Stablecoin-Backed-Card-Payments · https://www.theblock.co/news/business/2026-10-16-coinbase-to-power-stablecoin-backed-cards-for-marqeta-customers-418833 · https://www.pymnts.com/blockchain/2026/marqeta-and-coinbase-take-stablecoin-spending-mainstream/ · https://www.sec.gov/Archives/edgar/data/1522540/000152254026000043/mq-20260610.htm · https://investors.marqeta.com/news-releases/news-release-details/marqeta-reports-first-quarter-2026-financial-results/ · https://www.sec.gov/Archives/edgar/data/0001679788/000167978826000087/q226earningsdeck_sec.htm · https://insights4vc.substack.com/p/the-state-of-stablecoin-cards · https://www.techtimes.com/articles/328383/20261002/open-usd-goes-live-stripe-visa-mastercard-deploy-business-stablecoin-infrastructure.htm · https://www.onebullex.com/news/articles/stripe-bridge-visa-stablecoin-cards-expand-from-18-to-100-plus-countries-in-2026
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (financial backdrop).** This is a partnership announcement, not a results release — no deal-specific economics were disclosed (volumes, revenue share, launch geographies all "no data"). As backdrop to the two partners' latest standalone prints (both Q2 2026, quarter ended 2026-06-30): **Marqeta = BEAT / inflecting** (net revenue $176M, +17% YoY; second straight quarter of GAAP profit) while **Coinbase = MISS / cyclically soft** (total revenue $1.22bn, −18.5% YoY; swung to a $359.5M net loss). The collaboration pairs Marqeta's profitable, accelerating card-issuing rails with Coinbase's stablecoin/USDC franchise — which is itself under pressure, with stablecoin revenue actually *down* YoY.

**Marqeta — Q2 2026 (reported 2026-08-03), the issuer side.**
- TPV: $120bn, +32% YoY — volume growth running ~2x net-revenue growth, consistent with pricing/mix drag from large-customer renewals.
- Net revenue: $176M, +17% YoY.
- Gross profit: $122M, +17% YoY; gross margin 69%.
- GAAP net income: $8M (vs −$1M in Q2 2025) — second consecutive quarter of GAAP profitability; diluted EPS $0.07 (vs −$0.01), vs ~$0.01 public consensus → a clear beat (StockAnalysis/MarketBeat aggregators).
- Adjusted EBITDA: $37M, +31% YoY; 21% margin.
- FY2026 guidance (from the release): net-revenue growth 12–13%, gross-profit growth 11–12%, adjusted-EBITDA growth low-30s % — i.e. Q2's +17% net revenue is tracking *above* the full-year guide, implying either conservatism or expected H2 deceleration (de-PR flag: the guide bakes in a slowdown Marqeta did not dwell on).

**Coinbase — Q2 2026 (reported 2026-07-30), the stablecoin/USDC side.**
- Total revenue: $1,220.1M, −18.5% YoY (vs $1,497.2M in Q2 2025); total net revenue $1,154.3M (vs $1,396.5M).
- Transaction revenue: $599.2M, −21.6% YoY (vs $764.3M) — the swing factor; CFO Alesia Haas cited industry spot volumes down >20% and a double-digit crypto-market-cap contraction, a −14% sequential revenue drop.
- Subscription & services revenue: $555.1M, −12.2% YoY (vs $632.2M) — the "stable" leg also declined.
- Stablecoin revenue (USDC): $292.1M, −5.4% YoY (vs $308.9M) — notably *down*, pressured by rate/mix despite USDC-balance narratives.
- Net loss: $(359.5)M, vs +$1,428.9M net income in Q2 2025 (prior-year figure flattered by large crypto-asset mark-to-market gains); loss per share $1.36 vs ~$0.17 loss expected → a clear miss.

**By driver / read-across to the deal.** Marqeta brings the healthier P&L and the regulated card-issuing/program-management layer; Coinbase brings USDC distribution but is monetizing it less, not more, QoQ and YoY. A stablecoin-backed card ties card spend to USDC balances — strategically it is a *distribution* play for Coinbase (grow USDC usage/float) more than a near-term revenue line, and for Marqeta a new fundable-source TAM on top of +32% TPV. Neither print contains partnership-attributable numbers.

**vs expectations / prior period.** Marqeta: beat on EPS ($0.07 vs ~$0.01 public consensus) and inflected to GAAP profit — sustainable-looking (operating leverage, EBITDA +31%), not a one-off. Coinbase: double miss (revenue $1.22bn vs ~$1.3bn expected; EPS −$1.36 vs ~−$0.17 expected), company-specific only insofar as it is leveraged to a sector-wide volume downturn. Compare prior Coinbase coverage on stablecoin-rail expansion: [[Coinbase launches Coinbase Business stablecoin payment tools]], [[Citi taps Coinbase to explore stablecoin payments]].

**Guidance / forward.** Marqeta gave explicit FY2026 guidance (above); Coinbase gives no single revenue guide — tone was defensive (Haas: "difficult operating environment"), leaning on subscription & services and USDC as the through-cycle story even as both fell. Thesis flag: Coinbase is pitching stablecoins as the structural offset to transaction-revenue cyclicality, yet stablecoin revenue itself just declined — this partnership is part of that distribution push, and its payoff is a multi-year float-and-usage bet, not a 2026 earnings driver.

**Thesis-flags.** (1) Asymmetric financial health — Marqeta profitable & accelerating vs Coinbase loss-making & contracting; the deal de-risks more for Marqeta (new volume source) than it immediately helps Coinbase's P&L. (2) Stablecoin monetization is the quiet weak spot — USDC revenue −5.4% YoY contradicts the "stablecoins to the rescue" narrative; a spend-backed card is a demand-generation lever Coinbase needs. (3) Rate sensitivity — USDC economics hinge on interest on reserves; any 2026 rate cuts compress the float revenue this card is meant to grow (second-order risk to the deal's economics). (4) No disclosed deal terms → all partnership figures [UNSOURCED]; treat as strategic optionality, not modeled revenue.

Sources: Marqeta Q2 2026 8-K earnings release (SEC) https://www.sec.gov/Archives/edgar/data/0001522540/000152254026000061/mqearningsrelease-q2x2026.htm · Coinbase Q2 2026 10-Q (SEC) https://www.sec.gov/Archives/edgar/data/0001679788/000167978826000088/coin-20260630.htm · consensus/EPS reactions via public aggregators (MarketBeat, Yahoo Finance, CNBC 2026-07-30); adjusted EBITDA for Coinbase not in 10-Q (reported ~$207.8M per press coverage) — [UNSOURCED] here. Partnership source: businesswire release in note frontmatter; no deal economics disclosed → "no data".
<!-- /enrichment:earnings_review -->
