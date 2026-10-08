---
title: "Visa reports nearly 200% YoY stablecoin card payment growth"
date: 2026-10-05
retrieved: 2026-10-08
tags:
  - company/visa
  - industry/stablecoins
  - industry/cards
  - region/global
  - type/earnings
sources:
  - https://fintechnews.sg/138434/digitalassets/visa-stablecoin-business-payments
status: enriched
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "This Week in Fintech"
story_id: s820a1f72
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Visa reports nearly 200% YoY stablecoin card payment growth

> [!info] 2026-10-05 · 2 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, This Week in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌏 Visa reports nearly 200% annual growth in stablecoin card payments, now supporting over 160 stablecoin-linked card programmes globally. Business and commercial cards account for roughly 17% of volume, while research cited by Visa estimates annual stablecoin payment volume at between $401 billion and $527 billion. Payments are now the fastest-growing stablecoin use case.

[This Week in Fintech] Visareported nearly 200% YoY growth in stablecoin-linked card payments, with business and commercial programmes accounting for 17% of volume in FY2026 to date.

## Первоисточники

### fintechnews.sg
<https://fintechnews.sg/138434/digitalassets/visa-stablecoin-business-payments>
*243 слов · direct*

Get the hottest Fintech Singapore News once a month in your Inbox
Business and commercial card programmes accounted for approximately 17% of Visa ’s stablecoin-linked card volume in fiscal 2026 to date.
Visa released the figures as businesses, financial institutions and payment providers explore stablecoins for moving and managing money.
The network supports more than 160 stablecoin-linked card programmes across consumer, business and commercial activity.
Payment volume across these programmes has grown nearly 200% year on year.
 “Businesses aren’t looking for new payment technologies for the sake of innovation. They’re looking for trusted, reliable ways to move money. What’s changing is that stablecoins are increasingly becoming part of the conversation around real business applications, from supplier payments and treasury operations to cross-border commerce.” 
said Mark Nelsen, Global Head of Product, Commercial & Money Movement Solutions, Visa.
Stablecoins have historically been associated with cryptocurrency trading.
Research from Allium cited by Visa found that payments are now their fastest-growing use case, with annual payment volume estimated at between US$401 billion and US$527 billion.
The largest business payment categories included service fees at US$56 billion, payroll at US$43 billion and supplier payments at US$28 billion.
Among the payment flows analysed, business-to-business payments had the highest cross-border share at 43% of volume.
Visa is expanding its stablecoin capabilities across settlement, money movement and payment acceptance, including Visa Direct pre-funding and payouts.
 
 
 Featured image: Edited by Fintech News Singapore, based on image by Who is Danny via Magnific

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Visa reports nearly 200% YoY stablecoin card payment growth
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On ~1 Oct 2026 Visa released a **data/marketing report** (not quarterly earnings — FY2026 ends 30 Sep, so "fiscal 2026 to date" means roughly the full fiscal year) on its stablecoin franchise. The hard numbers:
- Stablecoin-linked **card payment volume up ~200% YoY**.
- **160+ stablecoin-linked card programmes** globally (consumer + business + commercial).
- **Business/commercial cards = ~17%** of stablecoin-linked card volume in FY2026 to date.
- Separately, Visa says its **stablecoin settlement run rate recently passed ~$20bn annualized** (per web sources; cryptobriefing: "up 15x YoY"). Note: the note's own aggregated text does NOT mention $20bn — that figure comes from the external reporting of the same Oct release.
- Market sizing comes from **Allium** (cited by Visa, not Visa's own data): total annual stablecoin **payment** volume est. **$401bn–$527bn**; largest B2B categories — service fees $56bn, payroll $43bn, supplier payments $28bn; B2B had the highest cross-border share at 43%.

**Why framed this way (red-team).** Two things are being conflated in the PR and in secondary coverage: (a) **card payment volume** growth (+200%) and (b) **settlement** run rate ($20bn). They are different rails — card spend is consumer/business purchases; settlement is issuers/acquirers clearing in USDC instead of fiat wires. Visa bundles them to project one "stablecoin momentum" story. The +200% is off a **tiny base** (crypto card spend was ~$18bn annualized industry-wide in Jan 2026 per Artemis/CoinDesk — see [[This Week in Fintech Artemis data shows crypto card spending rising]]), and the headline Allium $401–527bn figure is **third-party market sizing**, not Visa throughput — Visa borrows the big number to anchor the narrative. The genuinely new, Visa-specific disclosures are the **160+ programmes count** and the **17% business/commercial mix** (first time Visa breaks out the business share).

## [1] Competitors / peers
- **Mastercard**: added stablecoin settlement (USDC/PYUSD/RLUSD, intraday/weekend cycles) in **Jun 2026**; **SoFi** began settling card txns in SoFiUSD on Mastercard in **Sep 2026** with an expected **>$25bn annualized** program (theblock.co). So on the settlement metric, Mastercard+partners are quoting a larger single-program number than Visa's whole-network $20bn — though methodologies differ (expected vs run-rate).
- **Stripe/Bridge, Circle, Coinbase**: the settlement layer itself; Visa added **Tempo (Stripe), Arc (Circle), Base (Coinbase), Polygon, Canton** in Apr 2026 ([[Visa expands stablecoin settlement network to $7bn run rate]]).
- Internal corpus: [[Visa and Mastercard accelerate stablecoin and crypto payments]] frames both networks racing to own the settlement/liquidity layer.

**Why the landscape looks this way.** Cards remain the dominant bridge for stablecoin spend because they require **no new merchant integration** — the crypto→fiat conversion happens before network settlement, so the txn is indistinguishable from any card payment (see [[Fintech Wrap Up crypto cards bridge stablecoins and spending]]). That is why "card payment volume" grows fast while true on-chain merchant acceptance stays nascent — the +200% is largely crypto-funded cards riding existing rails, not a new payment network. Second-order: Visa's moat here is **distribution (programmes + acceptance)**, not the blockchain; whoever has the most issuer programmes wins, which is why Visa leads with "160+ programmes."

## [2] Company history / fit
Visa's stablecoin settlement run-rate trajectory (internal corpus):
- **Nov 2025: ~$3.5bn** annualized ([[Visa launches USDC stablecoin settlement for US banks]]).
- **Jan/Feb 2026: ~$4.5bn** ([[Visa stablecoin settlement reaches $4.5bn annualized run rate]]).
- **Apr/May 2026: ~$7bn**, +50% QoQ, expanded to 9 chains ([[Visa expands stablecoin settlement network to $7bn run rate]]).
- **Sep/Oct 2026: ~$20bn** (this release).
So the settlement curve has roughly tripled in ~8 months. The card-payment angle is a newer disclosure dimension layered on top.

**Why Visa pushes this.** Visa's core business is a commodity-ish take-rate on $14.2tn+ annual payments; stablecoins are both an **existential threat** (direct on-chain transfer could disintermediate the network) and an **option** (be the settlement/liquidity layer). By owning programmes + settlement, Visa converts the threat into incremental volume and defends its position as the "common settlement layer." The 17% business-mix disclosure signals Visa wants to move the story from crypto-trading to **treasury/supplier/payroll** — higher-value, stickier flows.

## [3] Novelty / value-add / traction
**What's genuinely new:** the **160+ programmes** count and the **17% business/commercial share** — first explicit business-mix breakout. Real traction signals: settlement run rate 3x'd in 8 months; card volume +200%.
**What is NOT new / is soft:** the "stablecoins are the fastest-growing use case" framing (repeated across 2026), and the $401–527bn Allium number (market sizing, not Visa). The +200% is off a small base.

**Why the value-add is real but bounded.** Durable value accrues to Visa only if stablecoin flows stay **inside its rails** (settlement + card acceptance). The risk: as merchant-direct stablecoin acceptance and native on-chain B2B matures, the crypto→fiat→card bridge gets disintermediated and Visa's take-rate shrinks to a thin settlement fee. So who captures the margin: today Visa (network fee) + issuers; tomorrow, if stablecoin issuers (Circle, Tempo, SoFiUSD) + merchant-acceptance layers cut out the card, the margin migrates on-chain. The $20bn is still **0.1%** of Visa's ~$14tn+ — so this is optionality/defense, not yet a P&L mover.

## [4] What's next / market sentiment
Visa is expanding across settlement, money movement, acceptance (Visa Direct pre-funding/payouts). Sentiment: analysts increasingly see stablecoin settlement as a swing factor for Visa/Mastercard investment cases (Simply Wall St, Yahoo Finance). Regulatory backdrop: GENIUS-style US stablecoin regulation + regulated issuers (USDC, PYUSD, RLUSD) de-risking institutional adoption.

**Why the market goes this way + second-order.** The networks are racing to **become the settlement layer before stablecoins route around them**. Counterintuitive effect: every integration Visa adds (Tempo/Arc/Base) **legitimizes the disintermediating rails** it may later compete with — short-term volume, long-term optionality for rivals. The real question is not "is Visa growing stablecoin volume" (yes, off a tiny base) but **"when flows go native on-chain, does Visa keep the margin or keep only the fee"** — unresolved.

## FRESHNESS / DUPLICATE VERDICT
**FRESH.** This is a NEW Oct-2026 data release with a NEW reporting dimension (card payment volume +200% YoY, 160+ programmes, 17% business mix) and a new settlement milestone (~$20bn). The prior settlement-run-rate notes ($3.5bn / $4.5bn / $7bn) are earlier, lower milestones on a different metric — related, not a reprint of the same disclosure. Not a duplicate.

## Sources
- fintechnews.sg (primary, in note): https://fintechnews.sg/138434/digitalassets/visa-stablecoin-business-payments
- crypto.news: https://crypto.news/visa-stablecoin-card-payments-jump-200-in-a-year/
- cryptobriefing ($20bn / 15x): https://cryptobriefing.com/visa-stablecoin-settlement-20-billion/
- theblock (SoFi/Mastercard $25bn): https://www.theblock.co/news/business/2026-09-22-sofi-begins-stablecoin-settlement-on-mastercard-network-for-program-expected-to-exceed-25-billion-in-annualized-volume-416035
- Related internal: [[Visa stablecoin settlement reaches $4.5bn annualized run rate]], [[Visa expands stablecoin settlement network to $7bn run rate]], [[Visa launches USDC stablecoin settlement for US banks]], [[This Week in Fintech Artemis data shows crypto card spending rising]], [[Fintech Wrap Up crypto cards bridge stablecoins and spending]], [[Visa and Mastercard accelerate stablecoin and crypto payments]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions (second-order)

1. **What is the absolute card volume, not the %?** +200% off what base? Industry crypto-card spend was only ~$18bn annualized in Jan 2026 — Visa gives no $ card-volume figure. **Open / likely small base.**
2. **Card volume vs settlement — are coverage outlets conflating them?** Yes. +200% = card payments; $20bn = settlement run rate. Different rails. The note's own text omits $20bn; it comes from external coverage of the same release. **Confirmed conflation.**
3. **Is the $401–527bn Visa's throughput?** No — it's **Allium** third-party market sizing cited by Visa. Not Visa volume. **Confirmed.**
4. **Is this earnings or a marketing data drop?** A data/PR release (~1 Oct 2026), not the FY2026 earnings call. "Fiscal 2026 to date" ≈ full fiscal year ending 30 Sep. **Confirmed — tagged type/earnings is slightly off; it's a research/data report.**
5. **How much of the +200% is genuine new adoption vs crypto-funded cards riding existing fiat rails?** Cards dominate because no merchant integration needed; conversion happens pre-settlement. Likely mostly bridge volume, not native on-chain. **Open, leaning bridge.**
6. **What is $20bn as a share of Visa's total?** ~0.1% of $14tn+ annual payments. Immaterial to P&L today. **Confirmed — optionality not driver.**
7. **Does Visa lead Mastercard?** On single-program settlement, no — SoFi/Mastercard alone claims >$25bn expected vs Visa's whole-network $20bn, but methodologies differ (expected vs run-rate). **Mixed.**
8. **Is the 17% business-mix disclosure new?** Yes — first explicit business/commercial breakout by Visa. **Genuinely new datapoint.**
9. **Who is silent on economics?** No disclosure of Visa's take-rate on stablecoin card/settlement volume vs traditional interchange — is the margin accretive or dilutive? **Open.**
10. **Disintermediation risk:** if merchant-direct stablecoin acceptance matures, does the card bridge (and Visa's fee) get cut out? **Open — the central long-term question.**
11. **Why integrate rival rails (Tempo/Arc/Base)?** Each integration legitimizes the networks that could later route around Visa. Volume now vs optionality for rivals. **Strategic tension, open.**
12. **Is "fastest-growing use case" new?** No — repeated framing across 2026 Visa/Artemis/Chainalysis commentary. **Not new.**
13. **Durability of business flows (treasury/payroll/supplier)?** These are stickier than crypto-trading flows — if real, they justify a better multiple. But % share, not $ growth, disclosed. **Partially open.**
14. **Could the number be cherry-picked to a flattering base?** +200% off a near-zero FY2025 base inflates optics. **Likely, confirmed concern.**
15. **Does this change the investment case?** Marginally — confirms Visa is defending, not losing, the settlement layer; not yet a revenue mover. **Confirmed — directional, not material.**

Importance: 3/5 — Real, new Visa-specific datapoints (160+ programmes, 17% business mix, ~$20bn run rate, +200%) on a strategically important theme (networks defending against stablecoin disintermediation), and recurring coverage shows sustained momentum. Capped below 4 because: it's a marketing/data drop not earnings, growth is off a tiny base, the headline numbers conflate card volume with settlement and borrow Allium's market sizing, and $20bn is ~0.1% of Visa volume — optionality/defense, not a P&L driver.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Stablecoins are shifting from a trading-settlement instrument to a payments rail. Allium research cited by Visa pegs annual stablecoin *payment* volume at $401bn–$527bn (through Aug 2026, per crypto.news), with largest business categories service fees ($56bn), payroll ($43bn), supplier payments ($28bn); B2B flows carry the highest cross-border share (43%). This is a tiny slice of total stablecoin activity — Chainalysis put adjusted stablecoin volume at ~$28tn in 2025 (via [[Visa and Mastercard accelerate stablecoin and crypto payments]]) — so "payments" is the fast-growing but still-small use case. Structure: the card-network layer is a consolidated duopoly (Visa/Mastercard) sitting ON TOP of a fragmenting issuance/orchestration layer (Bridge, BVNK, dtcpay, Rain, etc.); entry barriers at the network tier are extreme (global acceptance, compliance, settlement licenses). Why now: GENIUS Act / regulatory clarity (2025), plus networks racing to own the stablecoin settlement layer "beneath existing brands" (via [[Visa and Mastercard accelerate stablecoin and crypto payments]]).

**Competitive landscape.** Sector KPIs: payments volume (TPV), settlement run-rate, number of card programmes, cross-border share, take rate. Visa's disclosed figures: **160+ stablecoin-linked card programmes** globally; **~200% YoY** card-payment volume growth; business/commercial = **17%** of stablecoin card volume in FY2026-to-date. Settlement is a separate, faster-climbing metric: $3.5bn annualized run-rate at Nov 2025 (via [[Visa launches USDC stablecoin settlement for US banks]]) → $4.5bn Feb 2026 ([[Visa stablecoin settlement reaches $4.5bn annualized run rate]]) → $7bn Apr/May 2026 ([[Visa expands stablecoin settlement network to $7bn run rate]]) → **~$20bn annualized by Sep 2026** (per wallstreetledger/crypto.news) — a ~4.4x climb in 10 months (analysis). Players & basis of competition: Visa vs **Mastercard** (added USDC/PYUSD/RLUSD intraday+weekend settlement Jun 2026; agreed to acquire BVNK for **$1.8bn** late Sep 2026, per pymnts) competing on rails breadth + partner ecosystem, not price; fintech issuers (dtcpay, Coinbase cards) compete on distribution. Position: Visa is **ahead on card distribution** (Artemis: Visa captures most on-chain card volume via early infra, via [[This Week in Fintech Artemis data shows crypto card spending rising]]); moat = acceptance network effects + switching costs (analysis). Note: the protagonist discloses % growth and programme counts but NOT absolute dollar card-payment volume for the period — only the FY2025 cumulative ($3.7bn, see comps).

**Comps & multiples.** IR-grounded anchor — Visa FY2025 Annual Report (CEO letter): *"We've processed $3.7 billion in payments volume in more than 200 countries"* on stablecoin-linked cards (drive_url: https://drive.google.com/file/d/1naQ0Tn6m695Qp1izlrg4KnynovyRYpqL/view). Against this, ~200% YoY growth implies the trailing-year flow roughly tripled off a small base (analysis). Scale check vs Visa total: Q2 FY2026 net revenue $11.2bn (+17%), FY2025 $40bn (+11%) — 8-K 2026-04-28, drive_url: https://drive.google.com/file/d/11Yn24BCvigbjXDAUjEkAAuQA1HOEr4pz/view; FY2025 8-K 2025-10-28, drive_url: https://drive.google.com/file/d/1KAwJMvzVrjq8djc0mVZL_7DoN40UcQdN/view. So a ~$20bn stablecoin settlement run-rate and ~$3.7bn cumulative card volume are **immaterial** to a company settling trillions annually — this is an option on a new rail, not a current P&L driver. No standalone valuation/multiple is disclosable for the stablecoin unit → **no data**. Peer settlement comp: Mastercard — no standalone stablecoin volume disclosed; BVNK acquisition at $1.8bn is a round/deal valuation (not a market cap, revenue multiple [UNSOURCED]). Internal comp — crypto-card market as a whole: $18bn annualized / 230% YoY in May 2026 (via [[This Week in Fintech Artemis data shows crypto card spending rising]]), i.e. Visa's ~200% is roughly in line with the broader crypto-card market, not outperforming it (analysis).

**Risk flags.**
1. **Disclosure asymmetry / de-PR.** Visa reports flashy % growth and programme counts but withholds the absolute period dollar volume and economics (take rate, fraud liability, fees on stablecoin cards). A ~200% jump off a tiny FY2025 base ($3.7bn cumulative) can look large yet stay immaterial — second-order: headline risks over-signalling adoption.
2. **Disintermediation of the card rail.** If stablecoin payments move to direct on-chain/wallet-to-merchant or pay-by-bank, the economics shift to the issuance/settlement layer (where BVNK/Bridge/Tempo/Arc sit) and Visa's per-transaction card take rate is at risk — the same "whoever controls the settlement layer controls the economics" thesis cuts both ways.
3. **Competitive catch-up.** Mastercard's $1.8bn BVNK buy (Sep 2026) + multi-stablecoin intraday settlement narrows Visa's lead fast; this is a land-grab where a 6-month edge is not a durable moat.

**What this changes (idea-lens).** This is a *new-entry / option-value* story, not a re-rating: stablecoin cards remain <0.1% of Visa volume, so the thesis is about whether Visa defends the acceptance layer as value migrates on-chain, not about near-term revenue (analysis). Falsifiable thesis: if the settlement run-rate keeps ~doubling every ~4-5 months (it went $3.5bn→$20bn in ~10 months) AND Visa starts disclosing absolute stablecoin-card dollar volume, the rail is becoming material — watch the FY2026 10-K (expected ~Nov 2026) for the next cumulative figure. What breaks it: flat/undisclosed volume + Mastercard/BVNK capturing the B2B cross-border flow (the 43%-cross-border, highest-margin slice).

Sources: https://investor.visa.com (FY2025 AR, $3.7bn) · https://www.sec.gov/Archives/edgar/data/1403161/000140316126000077/q22026earningsrelease.htm · https://crypto.news/visa-stablecoin-card-payments-jump-200-in-a-year/ · https://www.pymnts.com/cryptocurrency/2026/mastercard-sofi-bring-stablecoin-settlement-cards-step-one-broader-rollout/ · https://www.wallstreetledger.org/article/visa-mastercard-stablecoin-settlement-2026 · https://fintechnews.sg/138434/digitalassets/visa-stablecoin-business-payments
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** BEAT · the ~200% stablecoin-card growth is a product-marketing stat from an Oct-2026 Visa release, NOT a reported earnings metric — so it is tied here to Visa's latest *actual* print: fiscal **Q2 2026** (quarter ended Mar 31, 2026; released Apr 28, 2026). That quarter: net revenue **$11.2B (+17% YoY; +16% constant-dollar)**, non-GAAP EPS **$3.31 (+20% YoY)**, GAAP EPS **$3.14** — both ahead of public consensus (EPS est. ~$3.09, rev ~$10.7B). Stablecoins remain a thesis/optionality story, not yet a disclosed revenue line.

**Key figures (Q2 FY2026, from Visa earnings release, quarter ended Mar 31, 2026).**
- Net revenue: **$11.2B, +17% YoY** (**+16% constant-dollar**), driven by growth in payments volume, cross-border volume and processed transactions.
- GAAP net income **$6.0B**, GAAP EPS **$3.14**; non-GAAP net income **$6.3B**, non-GAAP EPS **$3.31**.
- Payments volume **+9% YoY** (constant dollars).
- Cross-border volume **total +12% YoY**; **excluding intra-Europe +11% YoY**.
- Processed transactions **66,086M, +9% YoY** (6-month: 135,485M, +9%).
- Capital return: record **~$7.9B** of buybacks in the quarter (per public coverage).

**By segment / driver.** Growth is broad-based across the three Visa engines (consumer payments, cross-border/new flows, value-added services). Cross-border (+12%) continued to out-grow domestic payments volume (+9%) — the higher-yield travel/e-commerce flow remains the margin driver. The **stablecoin-card metric in this news (~200% YoY growth in stablecoin-linked card payments, >160 programmes, business/commercial = ~17% of that volume in FY2026-to-date)** sits inside the cross-border / new-flows narrative but is a *product disclosure (Oct 2026)*, not a segment in the financials; Visa has NOT quantified stablecoin revenue. The CEO's only earnings-call reference was qualitative: enhancing the "Visa as a Service" stack "including with agentic and stablecoin capabilities." (analysis) The Allium-sourced $401–527B annual stablecoin payment-volume TAM is a *third-party estimate cited by Visa*, not Visa volume.

**vs expectations / prior period.** Beat vs public consensus: non-GAAP EPS $3.31 vs ~$3.09 est (**~+7%**, Zacks); net revenue $11.2B vs ~$10.7B est (**~+5%**) — extends the beat streak to ~4 straight quarters (public coverage, as of Apr 28, 2026 print). YoY momentum is intact/accelerating: Q1 FY2026 was net revenue $10.9B (+15%) and EPS $3.17 non-GAAP (`[[Visa Reports Fiscal First Quarter 2026 Results]]`-equiv in IR db); vs Q2 FY2025 ($9.8B-area) the +17% top line is a step-up from the ~10% cadence seen through FY2024. Consensus figures labeled **public consensus** (Zacks), not proprietary Street.

**Guidance / forward.** Q2 release gave **no full-year headline guidance in the press release**; Visa provided its usual **fiscal Q3 2026 outlook** in the investor deck (constant-dollar net revenue growth and EPS framework; exact magnitude **[UNSOURCED]** — not captured verbatim here). Management tone confident (record buyback, broad-based volume). Independent read (analysis): with cross-border >domestic and value-added/new-flows compounding, mid-teens revenue growth looks sustainable near-term; stablecoin is upside optionality, not yet a numbers driver.

**Thesis-flags.**
1. **Stablecoin = narrative, not yet P&L.** ~200% growth is off a tiny base and is *card-rail* volume (Visa still clips interchange/network fees on it) — fact: fastest-growing stablecoin use case is payments → why: it rides Visa's existing rails rather than disintermediating them → why it matters: near-term it is thesis-protective (Visa monetizes crypto-settled spend) not thesis-threatening → 2nd-order: if stablecoins later move to non-card direct rails, that optionality could invert. Watch for Visa to ever *quantify* stablecoin revenue (it has not).
2. **Cross-border +12% is the real engine** — not stablecoins. The high-yield cross-border line continues to out-pace domestic +9%; this, not crypto, explains the +17% revenue beat.
3. **Beat quality is sustainable, not one-off** — volume-driven plus operating leverage (EPS +20% > revenue +17%), reinforced by the record ~$7.9B buyback shrinking the share count.
4. **De-PR:** the news leads with a flashy ~200% crypto stat and a $401–527B third-party TAM, but Visa stays *silent on stablecoin revenue contribution* — treat the metric as adoption signaling, not an earnings driver.

Sources: Visa Q2 FY2026 earnings release / 8-K EX-99.1 (quarter ended Mar 31, 2026), https://drive.google.com/file/d/11Yn24BCvigbjXDAUjEkAAuQA1HOEr4pz/view · https://www.sec.gov/Archives/edgar/data/1403161/000140316126000077/q22026earningsrelease.htm · Q2 FY2026 results presentation https://drive.google.com/file/d/155fXpB4TJH2YbWb88dqXDeCEcDtZO1_V/view · 10-Q (processed transactions) https://drive.google.com/file/d/1BIG6L0iHRnAkPh4Fc2F9Inut06_D6hDG/view · public consensus (Zacks, as of Apr 28, 2026) https://finance.yahoo.com/markets/stocks/articles/visa-v-q2-earnings-revenues-211503876.html · stablecoin-card metric (Oct 2026 product news, fintechnews.sg) https://fintechnews.sg/138434/digitalassets/visa-stablecoin-business-payments · Q3 FY2026 outlook magnitude [UNSOURCED].
<!-- /enrichment:earnings_review -->
