---
title: "Payments Fanatic: what Checkout.com and Agoda build behind bookings"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/checkout-com
  - company/agoda
  - industry/payments
  - region/global
  - type/commentary
sources:
  - https://www.connectingthedotsinpayments.com/r/58b025cb
  - https://www.connectingthedotsinpayments.com/r/fee85f51
status: enriched
n_mentions: 2
channels:
  - "Connecting the Dots in Payments"
story_id: se0e7e533
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Payments Fanatic: what Checkout.com and Agoda build behind bookings

> [!info] 2026-07-03 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Payments] What Checkout.com & Agoda Are Building Behind Your Next Booking…

[Connecting the Dots in Payments] Hey Payments Fanatic! You know it’s summer when “I’ll just check prices” turns into a fully mapped-out trip. Or at lea…

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinpayments.com/r/58b025cb>
- <https://www.connectingthedotsinpayments.com/r/fee85f51>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Checkout.com × Agoda — AI-powered travel payments
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On 2026-07-03 Checkout.com and **Agoda** (a Booking Holdings OTA, Nasdaq: BKNG) announced a payments partnership. De-PR'd, this is Agoda naming Checkout.com as (a/the) **acquirer/processor** on two flows:
1. **Consumer processing** — card acceptance for bookings across hotels, holiday homes, flights, activities (6M+ properties cited).
2. **Virtual card issuing** — Checkout.com issues VCCs Agoda uses to **pay its suppliers** (the merchant-of-record model where the OTA collects from the traveller, then settles the hotel/airline via a single-use virtual card).
The stated "value-add" is **Intelligent Acceptance** (Checkout.com's proprietary AI auth-optimisation), plus **Network Tokens** and **Real-Time Account Updater** to cut false declines in cross-border/multi-currency/high-volume flows. "0% downtime" is claimed on supplier payments.
**Why framed this way:** the PR anchors on "AI" and headline reach (6M properties) but discloses **no numbers** — no auth-rate uplift %, no volume/GMV, no exclusivity, no contract term. Note the phrasing "a key driver of Agoda's **increased** performance **has been**" — past tense implies Checkout.com is **already live** at Agoda, so this is a **publicity release on an existing relationship**, not a new go-live. That is the single most important de-PR fact.

## [1] Competitors / peers
Travel-payments acquiring is contested: **Adyen** (long the reference acquirer for Booking.com / large OTAs and a leader in issuing VCCs for supplier settlement), **Stripe**, **Nuvei**, **Worldpay/FIS**. Checkout.com's own travel wins: **Rail Europe** (Sep-2025, "8% acceptance uplift") and **Travelsoft Pay** (Jun-2026, cross-border travel). Position: Checkout.com is **catching up / winning share** in an Adyen-anchored vertical; landing an Agoda (Booking Holdings) logo is a credibility marker vs Adyen's incumbency. **+ Why:** OTAs multi-source acquirers by geography/currency to maximise auth rates and hedge concentration — so "partners with X" rarely means displacing an incumbent; it usually means adding a rail. The competitive delta here is auth-rate optimisation, a commoditising race where every large PSP now sells an "AI acceptance" product.

## [2] Company history / fit
Checkout.com trajectory: $1B+/day volume (Sep-2025), returned to profitability + $300B+ annual volume (Feb-2026), 30%+ net-revenue growth 2 years running, heavy pivot into **agentic commerce** (ACP adoption Nov/Dec-2025, Forrester leader Mar-2026) and **stablecoins** (Blue EMI acquisition Feb-2026, Coinbase acceptance Jun-2026). Travel is a natural enterprise vertical for a full-stack acquirer chasing large, cross-border, high-AOV merchants. **+ Why:** processing is a **commodity take-rate** business, so Checkout.com competes on (a) big-logo enterprise wins and (b) software features (Intelligent Acceptance, Flow, issuing) that justify a stickier relationship — Agoda is exactly the trophy-logo + feature-attach play.

## [3] Novelty / value-add / traction
**Genuine novelty: low.** VCC-based supplier settlement and AI auth-optimisation are established products (Adyen, Nuvei have shipped these for years). Real value-add would be a **quantified auth-rate uplift** on Agoda's actual traffic — and that number is **withheld**. Traction: the past-tense language suggests real live volume, which is more than an "aims to" announcement, but there is **no disclosed metric** to size it. **+ Who captures the margin:** the OTA captures the FX/merchant-of-record spread; the PSP captures a thin bps take-rate plus issuing interchange share on VCCs. Checkout.com's leverage is only as durable as its auth-rate edge, which competitors are actively eroding — i.e. this is transactional revenue at a low multiple, not a defensible moat.

## [4] What's next / market sentiment
Expect Checkout.com to keep stacking travel logos (Rail Europe → Travelsoft → Agoda) to position travel as a vertical alongside its agentic-commerce/stablecoin narratives ahead of any liquidity event. **Risks/silence:** no fraud-liability or chargeback economics disclosed (travel is high-chargeback); no exclusivity (Agoda likely keeps other acquirers); "0% downtime" is unverifiable marketing. **+ Second-order:** as **AI travel agents** begin booking (a theme flagged in the corpus — "AI agents threaten OTAs"), the payment layer that wins agentic checkout could matter more than acceptance %; Checkout.com's ACP/agentic bets are the real strategic story, of which Agoda is a supporting logo, not the headline.

## Sources
- Checkout.com/Agoda PR (2026-07-03), PR Newswire APAC / Agoda press room.
- The Paypers, Financial IT, Insider Monkey (BKNG), IndexBox, ChannelLife coverage.
- Internal corpus: [[Travelsoft Pay partners with Checkout.com for travel payments]], [[Checkout.com powers Rail Europe to 8% acceptance uplift]], [[Checkout.com returns to profitability, passes $300B volume]], [[News & Trends AI agents threaten OTAs like Booking and Expedia]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this new, or a re-announcement of a live relationship?** The PR says performance "**has been**" driven by Intelligent Acceptance — past tense → Checkout.com appears **already live** at Agoda. This is a publicity release, not a go-live. (mostly answered: existing relationship)
2. **What is the actual auth-rate uplift on Agoda's traffic?** Undisclosed. The one metric that would prove value-add is withheld. (open)
3. **Is Checkout.com replacing Adyen, or adding a rail?** OTAs multi-source acquirers; no displacement claimed. Likely additive. (open — no exclusivity disclosed)
4. **What volume/GMV/share of Agoda's payments does this cover?** Not disclosed; "6M+ properties" is Agoda's inventory, not payment volume through Checkout.com. (open)
5. **Who bears fraud/chargeback liability?** Travel is high-chargeback; not addressed in the PR. (open)
6. **How differentiated is Intelligent Acceptance vs Adyen/Stripe/Nuvei AI acceptance?** Every large PSP ships an "AI acceptance" product — likely parity, not moat. (analysis: commoditising)
7. **On the VCC supplier-settlement side, does Checkout.com displace Adyen Issuing / Nuvei?** Unclear; issuing is where Adyen is strong in OTA supplier pay. (open)
8. **Is "0% downtime" verifiable?** No; marketing claim. (open)
9. **What is the contract term / exclusivity / minimums?** None disclosed. (open)
10. **Does this move Checkout.com's revenue needle at $300B+ annual volume?** Almost certainly immaterial financially; value is the trophy logo. (analysis)
11. **Does the corpus already cover this exact deal?** No — prior travel notes are Rail Europe (Sep-2025) and Travelsoft (Jun-2026), different merchants. This is a distinct new logo. → **fresh**. (answered)
12. **How does this connect to agentic commerce?** Agoda faces AI-agent disintermediation; Checkout.com's ACP/agentic bets are the strategic story — Agoda is a supporting logo. (analysis)
13. **Who captures margin?** OTA keeps FX/MoR spread; PSP earns thin bps + issuing interchange share — transactional, low-multiple. (analysis)
14. **What breaks the value-add?** Competitors closing the auth-rate gap; Agoda re-tendering; agentic checkout shifting the value layer. (analysis)
15. **Is this analyst/investor-relevant for BKNG?** Marginal — Insider Monkey picked it up but it's a supplier-cost optimisation, not a thesis mover. (answered: no)

**Importance: 2/5** — Real live relationship (better than a pure "aims-to" PR) and a credible trophy logo (Booking Holdings' Agoda) for Checkout.com in an Adyen-anchored vertical. But zero disclosed metrics, no exclusivity, commodity AI-acceptance/VCC products, and immaterial to either party's financials. It is a re-publicity release on an existing tie-up, not a new capability or a market-moving event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Travel/OTA payments sit inside two markets: the online-travel demand side (global OTA market ~$664bn in 2025, per Grand View Research/Statista secondary citations, as of 2025 — treat as order-of-magnitude, sources vary widely) and the merchant-acquiring supply side that monetises it. Structure is two-sided and unusually complex vs generic e-commerce: (a) high-value, cross-border, multi-currency tickets with heavy FX and local-payment-method fragmentation across 27+ markets; (b) a B2B payout leg where OTAs pay ~millions of hotels/suppliers, increasingly via single-use virtual cards. Barriers = acquiring licences, cross-border scheme relationships, fraud/chargeback tooling (CNP fraud is ~74% of card fraud losses; 79% of orgs hit by payment-fraud attempts in 2024, per AFP citations). "Why now": (1) travel recovery — Booking Holdings gross bookings hit $186.1bn in 2025 (+12% YoY), flights +37% (Booking Q4 2025, via PYMNTS/Phocuswire); (2) the "agentic commerce" narrative — Checkout.com explicitly frames its FY2025 results around it, and virtual-card issuing is the plumbing acquirers are racing to own.

**Competitive landscape.** Sector KPIs: TPV/processed volume, blended take rate (bps), authorization/acceptance uplift, and — on the payout leg — virtual-card issuing volume + interchange share. Key players: Adyen and Stripe (scale incumbents), Checkout.com (enterprise/cross-border challenger), Nuvei/Worldline (specialist acquirers), plus scheme-owned rails (Visa/Mastercard) one layer down. Basis of competition = acceptance/authorization performance + issuing economics, not headline price. Recent dated moves: Nuvei+WEX virtual-card partnership (Jan 2026, [[Nuvei and WEX partner to expand virtual card payments for the global]]); Agoda+Mastercard travel-rewards/redemption tie-up (Jan 2026, [[Agoda and Mastercard collaborate on flexible travel rewards]]); Trip.com enabling USDT/USDC stablecoin payments (Jan 2026, [[Trip.com enables stablecoin payments with USDT and USDC]]); Adyen+Uber global expansion (Feb 2026, [[Connecting the Dots Uber and Adyen expand global partnership]]). Checkout.com's position vs Agoda: catching up on scale (Adyen processed €1,394bn in 2025) but landing a marquee travel logo. The pitch bundles acceptance ("Intelligent Acceptance") on the pay-in leg with single-use virtual-card issuing on the pay-out leg (Checkout.com issuing launched with Visa in 2025) — a two-sided moat few pure acquirers offer (analysis). Deal scope per PR: 6M+ hotels/homes, 39 languages, 27 markets; "0% downtime" on supplier payouts (announced Jul 1 2026 — announced, not independently verified).

**Comps & multiples.** Comparable acquirers with public figures:
- Adyen (FY2025): net revenue €2,364m on €1,394bn processed → implied blended take rate ≈ €2,364m/€1,394,300m = **~17bps**; grows revenue (+18–21% cc) faster than volume (Adyen H2 2025 results).
- Stripe: >$900bn US volume in 2025, +45% YoY, targeting >$1tn in 2026 (TSG/Digital Transactions) — private, no clean multiple.
- Checkout.com: last round-implied valuation **$12bn** (Sep 2025 employee buyback, down from $40bn in 2022, per CNBC); >$300bn e-comm TPV in 2025; core net-revenue growth guided >30%; historic revenue $297m (2024)/$212m (2023) (Sacra/IR). Rough EV/Rev on ~$297m 2024 revenue at $12bn ≈ **~40x** — optically rich, but that is a stale/pre-growth denominator and a private-round mark, not a market cap: **treat as [UNSOURCED] for a true multiple**; the $40bn→$12bn re-rate (−70%) is the load-bearing fact, not the ratio. Distribution not computed (only 1 clean public take-rate comp). Internal deal comps: [[Checkout.com acquires euro stablecoin issuer Blue EMI]], [[Checkout.com powers digital payments behind Freenow by Lyft’s journeys across Europe]].

**Risk flags.**
1. **Client concentration / dependence on someone else's rails.** Agoda is owned by Booking Holdings, which has scale to in-source or dual-source payments; a single marquee logo can be re-competed at renewal. Checkout.com is also dependent on Visa/Mastercard scheme rails for the issuing leg — margin can be captured a layer down. Why: revenue quality of a headline win is only as durable as the contract and the schemes' terms.
2. **Unverified performance claims = execution risk.** "0% downtime," "AI-powered acceptance uplift" and the agentic-commerce framing are PR, not disclosed metrics; no take rate, no volume committed, no fraud-liability split disclosed. Why: if uplift underdelivers, a large travel merchant churns fast and publicly.
3. **Valuation credibility overhang.** The $40bn→$12bn re-rate signals the market already repriced Checkout.com's growth story; big-logo PR is partly a re-rating tool. Why: needs volume/revenue proof, not logos, to defend even $12bn.

**What this changes (idea-lens).** The battleground in travel payments is shifting from pay-in acceptance to owning BOTH legs — acceptance + single-use virtual-card issuing for supplier payouts — where interchange economics live (analysis). Falsifiable thesis: if Checkout.com discloses travel/issuing TPV in FY2026 results (next catalyst ~Feb 2027) showing material Agoda-driven volume, the win is real; if the partnership stays a logo with no disclosed volume, it's marketing. Watch: whether Adyen/Stripe counter with their own OTA issuing pushes.

Sources: https://www.prnewswire.com/apac/news-releases/checkoutcom-partners-with-agoda-to-deliver-ai-powered-payment-performance-for-global-travel-302816814.html · https://www.checkout.com/newsroom/checkout-com-returns-to-full-year-profitability-and-surpasses-300b-in-volume-as-it-positions-for-the-era-of-agentic-commerce · https://www.checkout.com/newsroom/checkout-com-accelerates-towards-full-year-profitability-and-announces-employee-share-buy-back-and-a-new-12bn-valuation · https://www.cnbc.com/2025/09/26/fintech-checkoutcoms-valuation-falls-to-12-billion.html · https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2 · https://www.digitaltransactions.net/stripe-adyen-and-toast-gain-among-top-acquirers-tsg-finds/ · https://www.pymnts.com/earnings/2025/booking-holdings-defies-travel-slump-with-7percent-surge-in-gross-bookings/ · https://sacra.com/c/checkout-com/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
