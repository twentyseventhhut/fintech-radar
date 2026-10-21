---
title: "Tether leads $15M Series A for Mural"
date: 2026-10-20
retrieved: 2026-10-21
tags:
  - company/tether
  - company/mural
  - industry/stablecoins
  - industry/payments
  - region/us
  - type/funding
sources:
  - https://fortune.com/2026/10/20/mural-startup-former-palantir-engineers-15-million-bid-banks-bot-economy
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s302b1cd7
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Tether leads $15M Series A for Mural

> [!info] 2026-10-20 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Tether leads $15M Series A for Mural, bringing total funding to $28M. The proceeds will fund global expansion and regulatory and payments infrastructure. Mural has processed $2.1B in payment volume since launching its API in 2025.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://fortune.com/2026/10/20/mural-startup-former-palantir-engineers-15-million-bid-banks-bot-economy>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Tether leads $15M Series A for Mural
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS: FRESH.** This is a new primary funding event (announced 2026-10-20, Fortune + PRNewswire). The only prior Mural note in the corpus is a 2025 commercial partnership ([[Taxbit partners Mural Pay to enable stablecoin payments]]) — a different event, not this round. Not a duplicate. "Mural" here = "Mural Pay" (same company; the brand now goes by "Mural").

## [0] What exactly happened (de-PR'd)
- **The facts:** Mural (NYC, cross-border stablecoin-payments API; the company formerly styled "Mural Pay") closed a **$15M Series A led by Tether**, with **North Island Ventures** participating. Total raised to date **$28M** (so ~$13M prior across a 2022 seed of ~$5–5.6M plus pre-seed/bridge). Founded 2022 by **ex-Palantir engineers Sinclair Toffa (CEO) and Chris Fernandes (CTO)**.
- **Use of proceeds (de-PR'd):** The note's "global expansion + regulatory/payments infrastructure" is generic. The press's actual frame is sharper: Mural is positioning its existing control layer (spending limits, counterparty approvals, audit trails, compliance) as the rails for **AI-agent ("bot economy") payments** — Tether CEO Paolo Ardoino explicitly called it a bet on "AI + crypto". So the money is less about geography and more about owning the **agentic-payments compliance/settlement layer**.
- **Traction stated:** **$2.1B processed since the API launched in 2025**, across **128 countries**; 2026 YTD volume ~6x all of 2025. Clients cited include **Deel** and **Opera**. (These are vendor-supplied figures — not independently audited; treat as directional.)
- **Why framed this way:** A $15M Series A is modest. Anchoring the raise to "agentic payments" (the hottest 2026 narrative) and to brand-name clients (Deel/Opera) does the lifting that the dollar figure can't. The "$28M total" phrasing flatters a company that is still sub-scale vs peers.

## [1] Competitors / peers
Stablecoin cross-border / payments-API peers, by rough annualized volume:
- **Bridge (Stripe-owned):** acquired Feb 2025 for ~$1.1B; $10B+ annualized; powers Stripe stablecoin accounts in 100+ countries.
- **BVNK:** Mastercard agreed to acquire for **up to $1.8B** (announced Mar 2026, its largest digital-asset deal); ~$30B annualized.
- **Conduit:** ~$53M raised (Circle, Dragonfly, Altos); $10B+ annualized; deepest Africa rails.
- **Sphere** (~$15M, Coinbase/Kraken Ventures, $3.5B+ annualized), **Noah** (~$22M seed, ex-Adyen/Visa founders, $1B+ processed).
- **Position: catching up / sub-scale.** Mural's lifetime $2.1B processed is a fraction of peers' *annualized* run-rates. The two biggest comps (Bridge, BVNK) have already been absorbed by Stripe and Mastercard — i.e. the category's winners are being bought by the incumbents that control the rails.
- **Why this matters (analysis):** With Bridge→Stripe and BVNK→Mastercard, the independent-API lane is thinning fast. Mural's defensible edge is NOT raw volume but the **agentic control layer** (approvals/limits/audit) — a bet that "who signs off on an AI agent's payment" is a distinct, ownable primitive the payment giants haven't locked down.

## [2] Company history / fit
- 2022 founding by Palantir alumni → compliance/ops-heavy DNA (audit trails, controls) rather than a consumer-crypto wallet. 2025 API launch → 2025 Taxbit partnership (invoicing/tax module, see [[Taxbit partners Mural Pay to enable stablecoin payments]]) → 2026 Series A.
- **Fit (logical):** The pivot from "stablecoin payments API for the Americas" (2025 framing) to "control layer for AI-agent payments" (2026 framing) is opportunistic but coherent — the same primitives (counterparty approval, spend limits, audit) that enterprises need are exactly what autonomous agents need before anyone will let a bot move money. The Palantir heritage (governance/audit) is the one credible differentiator.
- **Why Tether leads (structural):** Tether has been running a wide "invest in anything that moves USDT volume" strategy — see [[Argentina's Belo raises $14 million Series A led by Tether]], [[Tether invests in Axiym for global payment infrastructure]], [[Tether invests in LemFi to expand stablecoin remittances]], [[UAE's Utexo closes $7.5 million seed led by Tether]], [[Bit2Me raises $34.9M led by Tether]]. Backing distribution/settlement rails drives USDT demand; Mural is one more such node, now with an agentic-AI gloss.

## [3] Novelty / value-add / traction
- **Genuinely new?** The *funding* is new; the *product* is iterative. Stablecoin cross-border APIs are a crowded 2025–26 category (Bridge, BVNK, Conduit, Sphere, Noah). What's differentiated is the **agentic-payments positioning** — but that is still mostly narrative: the note cites no AI-agent transaction volume, only that the controls *could* serve agents.
- **Traction reality:** $2.1B lifetime and Deel/Opera as clients are real signals of product-market fit on the *human* payments side. On the *agentic* side it is "positioned for," not "live at scale" — classic announced-vs-adopted gap.
- **Who captures the margin (analysis):** In agentic payments the scarce asset is the authorization/compliance gate, not the rail itself. If Visa/Mastercard/Stripe (which own the rails and are buying the volume leaders) bolt approvals onto their stacks, Mural risks being a feature, not the layer. Its multiple rests on staying the neutral, cross-rail control plane — disintermediation by an acquirer-incumbent is the key break risk.

## [4] What's next / market sentiment
- **Market:** Stablecoin payment volume ~**$400B in the first 8 months of 2026** (Alvarez & Marsal); cross-border stablecoin flows ~**$220B Jul-2025→Jun-2026, +78% YoY**. The tailwind is real and large — which is exactly why incumbents are consolidating the category.
- **Plans:** Multi-asset single-account (USD + local + stablecoins), expansion, and the agentic push. Proceeds are small, so expect targeted build, not land-grab.
- **Risks / second-order:** (1) Category consolidation (Stripe/Mastercard) squeezes independents on both pricing and distribution. (2) "Agentic payments" is unproven revenue — if agent spend doesn't materialize in 12–18 months, the narrative premium evaporates and Mural reverts to a sub-scale payments API. (3) Tether lead-investor dependence ties Mural's fate to USDT regulatory standing (GENIUS-era US stablecoin scrutiny).
- **Sentiment:** Modestly positive/narrative-driven; the raise's weight comes from the agentic story and the Tether halo, not the dollars or standalone scale.

## Sources
See challenge file + URLs: Fortune (2026-10-20), PRNewswire (Mural Raises $28M), Citybiz, CryptoBriefing, Dealroom, BigGo Finance, Causeartist; competitor data from opendue / fintechspecs / trio.dev 2026 roundups.
- https://fortune.com/2026/10/20/mural-startup-former-palantir-engineers-15-million-bid-banks-bot-economy
- https://www.prnewswire.com/news-releases/mural-raises-28-million-total-to-power-fintechs-and-agentic-finance-302914128.html
- https://cryptobriefing.com/mural-raises-28m-tether-series-a/
- https://www.citybiz.co/article/921792/mural-raises-15-million-series-a-led-by-tether-bringing-funding-to-28-million/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5 — rationale.** A genuinely new (fresh) Series A in a hot, large category (stablecoin cross-border payments, ~$400B 2026 volume) with a credible team (ex-Palantir) and real human-payments traction ($2.1B, Deel/Opera). But the dollar amount is small ($15M), the company is sub-scale vs Bridge/BVNK/Conduit, and the headline differentiator (agentic/"bot economy" payments) is narrative, not yet revenue. Notable mainly as another Tether distribution-investment + an early marker of the agentic-payments theme — hence mid, not high.

## Red-team / challenge questions
1. Is this the same event as any prior note? No — the only prior Mural note is the 2025 Taxbit *partnership* ([[Taxbit partners Mural Pay to enable stablecoin payments]]); this is a 2026 funding round. FRESH.
2. Is "Mural" the same entity as "Mural Pay"? Yes — same NYC company (founders Toffa/Fernandes), rebranded/shortened to "Mural." Confirmed via Fernandes being CTO in both the 2025 Taxbit note and 2026 coverage.
3. How much was raised before? Total is now $28M with a $15M Series A → ~$13M prior (2022 seed ~$5–5.6M + pre-seed/bridge). Open: exact prior breakdown not fully disclosed.
4. Is the $2.1B volume audited or vendor-supplied? Vendor-supplied (company PR). Treat as directional, not verified.
5. Is the agentic-payments use case live or positioned? Positioned. No AI-agent transaction volume disclosed — only that existing controls *could* serve agents. Announced ≠ adopted.
6. Are Deel and Opera really clients, and at what scale? Cited as clients in coverage; scale/revenue contribution undisclosed. Open.
7. How does Mural compare to peers by scale? Sub-scale: $2.1B lifetime vs Bridge ~$10B+/yr, BVNK ~$30B/yr, Conduit ~$10B+/yr annualized. It is catching up, not leading.
8. Why is the category consolidating into incumbents? Stripe bought Bridge (~$1.1B, 2025); Mastercard buying BVNK (up to $1.8B, 2026). The rails owners are absorbing the volume leaders — structurally bad for independents.
9. Who captures the margin in agentic payments? Likely whoever owns the authorization/compliance gate across rails. Mural's bet. Risk: incumbents bolt approvals onto their own stacks and reduce Mural to a feature.
10. Why did Tether lead? Consistent with Tether's broad "fund USDT-distribution rails" strategy (Belo, Axiym, LemFi, Utexo, Bit2Me). Drives stablecoin demand; agentic-AI framing is the new wrapper.
11. What's the downside trigger? If agent-driven payment volume doesn't materialize in 12–18 months, the narrative premium collapses and Mural is a small payments API in a consolidating market.
12. Regulatory exposure? Tied to USDT's US standing (GENIUS-era scrutiny) via lead investor; also money-transmission/compliance across 128 countries.
13. Does the use-of-proceeds in the source note ("global expansion + regulatory/payments infra") match the press? Partly — the press emphasizes the agentic pivot more than geography; the note's framing is the generic PR version.
14. Is $15M enough to win this category? No — it's a build/survive round, not a land-grab. Expect targeted product (agentic controls) rather than broad expansion.
15. What would raise importance to 4/5? Disclosed, independently-verifiable agentic-payment volume, a marquee rails/bank partnership, or a materially larger follow-on — none present yet.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Stablecoin-rail B2B / cross-border payments infrastructure. Market sizing (via WebSearch, treat as secondary analyst estimates, not primary): B2B now represents ~60% of all stablecoin payment volume, with B2B stablecoin flows cited at ~$226bn of ~$390bn total 2026 payment activity (per hinkal.io/reap.global compilations); the stablecoin infrastructure & cross-border platform market is pegged at ~$7.43bn (2025) → ~$9.19bn (2026), ~23.8% CAGR (openpr/market-research syndication) — directional only, methodology unverifiable. Longer-dated TAM claims ($5tn B2B stablecoin payments by 2035; FXC Intelligence base TAM $14.7tn) are far-horizon and should be read as upside framing, not base case [treat as hypothesis]. Structure: still-fragmented, API-first infra layer sitting between fiat on/off-ramps, stablecoin issuers (USDT/USDC) and local payout rails; barriers are regulatory (money-transmission/VASP licensing per corridor), compliance/KYC-AML, and banking/liquidity partnerships rather than capital. Why now: GENIUS-era US stablecoin regime + incumbents buying (not building) the rail (see comps) + Mural's explicit "agentic finance" wager (24/7 machine-initiated payments, per Tether CEO Ardoino) — the forward thesis is AI agents as a new payer class, which is unproven demand (analysis).

**Competitive landscape.** Sector KPIs: total payment volume (TPV) processed, corridors/countries live, take rate on FX+settlement, and stablecoin↔fiat conversion spread. Mural disclosed metrics: $2.1bn cumulative TPV since 2025 API launch, 128 countries, $28M total raised. Take rate / net revenue / per-corridor margin — [UNSOURCED], not disclosed. Key players & basis of competition (product + distribution + licensing, not price): Bridge (Stripe-owned), BVNK (Mastercard-owned), Conduit, plus payout-API peers. Recent moves: Stripe closed Bridge for ~$1.1bn (Feb 2025); Mastercard completed BVNK for up to $1.8bn (Aug 3 2026); Conduit has raised ~$53M (Circle/Dragonfly/Altos), reportedly $10bn+ annualized volume. Mural's position: sub-scale niche entrant — its $2.1bn cumulative TPV is small vs Conduit's cited $10bn+ annualized run-rate, and it lacks the distribution of a Stripe/Mastercard parent. Moat is thin and early: at best a product/onboarding edge for fintech/payroll customers wanting unified fiat+stablecoin accounts, no evident network-effect or scale moat yet (analysis).

**Comps & multiples.** No revenue disclosed for Mural → revenue multiples not computable; comparison is on round size / scale, not EV/Rev.
- Internal (Tether strategic-venture cluster — direct read-across for deal shape, not valuation): [[Argentina's Belo raises $14 million Series A led by Tether]] ($14M Series A, LatAm stablecoin wallet — nearly identical ticket to Mural's $15M), [[Tether invests in LemFi to expand stablecoin remittances]] (remittances, €30M Series B extension), [[Tether invests in Axiym for global payment infrastructure]] (settlement infra), [[UAE's Utexo closes $7.5 million seed led by Tether]], [[Tether invests in Kenya's Kotani Pay]]. Pattern: Tether writes small (<$20M) early-stage checks into USDT-distribution plays across LatAm/EMEA/Africa — Mural fits the template, not a standout.
- External scale/valuation benchmarks: Bridge ~$1.1bn exit (Stripe, Feb 2025); BVNK up to $1.8bn (Mastercard, Aug 2026); Conduit ~$53M raised. Mural at $28M total / $15M Series A is 1–2 funding stages behind these.
- Multiple arithmetic: not computed — no public revenue/EBITDA for Mural or the private peers (last-round valuations for Bridge/BVNK are acquisition prices, not market caps; "distribution not computed, qualitative comparison").

**Risk flags.**
1. **Tether-dependence / single-sponsor concentration.** Lead investor is also the issuer of the primary settlement asset (USDT) — Mural's distribution thesis and liquidity are tied to one counterparty whose own excess-reserve buffer halved in a single quarter ($8.23bn→$4.11bn, Q1→Q2 2026 BDO attestation on ~$184.6bn USDT in circulation). Strategic alignment cuts both ways: exposure to USDT regulatory/de-peg/attestation events and to Tether's capital-allocation whims.
2. **Sub-scale vs consolidating incumbents (disintermediation).** With Stripe (Bridge) and Mastercard (BVNK) having bought the rail, Mural competes against distribution it cannot match; the value could be captured by the issuer layer (Tether) and the acquirer-distribution layer, squeezing an independent middleware startup's take rate.
3. **Unproven "agentic finance" demand + early-stage execution.** The forward narrative (AI agents as payers) is a bet, not revenue; $2.1bn cumulative TPV is modest, no revenue/margin disclosed, and global/LatAm expansion adds per-corridor licensing and compliance execution risk.

**What this changes (idea-lens).** Reads less as a re-rating and more as Tether extending USDT distribution into the B2B/agentic-payments stack via a cheap option-like stake — consistent with its Belo/LemFi/Axiym/Utexo pattern (analysis). Falsifiable thesis: if "agentic" payments are real demand, Mural's TPV should inflect well above its $2.1bn cumulative base within 12 months; watch for a disclosed run-rate (annualized TPV) and whether a Stripe/Mastercard-class player responds with an agent-payments product — absence of TPV disclosure or acquisition by a larger rail would signal the independent thesis is breaking. (analysis)

Sources: https://www.prnewswire.com/news-releases/mural-raises-28-million-total-to-power-fintechs-and-agentic-finance-302914128.html · https://cryptobriefing.com/mural-raises-28m-tether-series-a/ · https://techcrunch.com/2025/02/05/stripe-makes-1-1-billion-crypto-bet-as-it-closes-on-bridge-acquisition/ · https://cryptobriefing.com/stripe-mastercard-circle-stablecoin-acquisitions/ · https://decrypt.co/374796/tether-reports-1-5b-q2-profit-usdt-supply-grows · https://hinkal.io/blog/b2b-stablecoin-statistics · https://www.openpr.com/news/4629032/the-stablecoin-infrastructure-and-cross-border-payment
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
