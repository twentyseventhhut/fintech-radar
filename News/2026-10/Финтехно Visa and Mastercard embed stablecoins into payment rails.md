---
title: "Финтехно: Visa and Mastercard embed stablecoins into payment rails"
date: 2026-10-16
retrieved: 2026-10-16
tags:
  - company/visa
  - company/mastercard
  - industry/stablecoins
  - industry/payments
  - region/global
  - type/commentary
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s8c37774d
month: 2026-10
enriched: true
importance: 2
freshness: stale
duplicate_of: [[Visa Direct moves stablecoin payouts to production with Inyo Global]]
---

# Финтехно: Visa and Mastercard embed stablecoins into payment rails

> [!info] 2026-10-16 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Visa и Mastercard начали встраивать стейблкоины в обычную платёжную инфраструктуру — прежде всего в трансграничные выплаты и управление ликвидностью. Но делают это по-разному. ▶️ Visa перевела в коммерческую эксплуатацию пополнение ликвидности Visa Direct через USDC. До этого платёжной компании, которая отправляет деньги клиентам в разных странах, приходилось заранее держать деньги у банков и партнёров, чтобы выплаты проходили быстро. Это замороженная ликвидность и зависимость от банковских часов. Теперь часть этой задачи можно решить через USDC: платёжная компания круглосуточно переводит стейблкоины оператору Inyo Global, тем самым пополняя средства для будущих выплат через Visa Direct. Дальше получателю деньги приходят уже обычным способом — например, на карту или банковский счёт в местной валюте. То есть клиент может вообще не видеть криптовалюту. USDC используется внутри платёжной цепочки как способ быстро доставить долларовую ликвидность туда, где она нужна. ▶️ Mastercard стро

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Финтехно — Visa and Mastercard embed stablecoins into payment rails
_Analytical notes (not a post). Importance: 2/5. VERDICT: **STALE / duplicate roundup** — both halves already covered by dedicated same-month notes._

## [0] What exactly happened (de-PR'd)
This is a **Финтехно roundup/commentary** (channel aggregation, max.ru/fintexno), not a primary announcement. It bundles two separate, already-reported events and frames them as a theme ("Visa and Mastercard embed stablecoins into payment rails, but do it differently"):
- **Visa half:** Visa moved **USDC prefunding on Visa Direct from pilot to commercial/production**, with **Inyo Global** as the first processor to bring it live. A payment company sends USDC 24/7 to Inyo to prefund future Visa Direct payouts; the end recipient still gets local fiat (card/bank account) — crypto is invisible to them. USDC is used **inside the payout chain** to deliver dollar liquidity around the clock, removing frozen pre-funded balances and bank-hours dependency. Announced ~2026-10-15 (Visa newsroom).
- **Mastercard half:** Mastercard "строит..." (building) a stablecoin money layer — this maps to **Mastercard + BVNK Global Money Platform** (announced 2026-10-17), a single-API multi-currency account holding fiat + stablecoins with real-time conversion, stablecoin-linked cards, and local payouts via Mastercard Move. (Also adjacent same-week: Mastercard "Stablecoin Security" risk intelligence in North America.)
- **Why this framing / what it reveals:** The roundup's value is the *contrast narrative* (Visa = liquidity-prefunding inside its own rail; Mastercard = packaged BVNK platform/accounts). But that contrast is editorial repackaging — it adds **no new fact** beyond the two underlying announcements, which the corpus already holds as dedicated, enriched notes. This is exactly the "reworded roundup of already-covered integrations" pattern the red-team gate flags as stale.

## [1] Competitors / peers
Stablecoin payment-rail land is crowded and the corpus is saturated: Circle/USDC (issuer, Circle Payments Network), Stripe/Bridge + Open USD (Visa+Mastercard+Stripe+140 firms, July 2026), PayPal/PYUSD, Ripple/RLUSD, Paxos (PYUSD/USDG/USDP). On payouts specifically: Nium+Circle, Thunes+CPN, BVNK (now Mastercard-owned), Nuvion+Visa Direct. Visa's own stablecoin settlement run-rate was reported at ~$7bn ([[Visa expands stablecoin settlement network to $7bn run rate]]) and ~200% YoY card-payment growth ([[Visa reports nearly 200% YoY stablecoin card payment growth]]). **Position:** parity/incremental — Visa's Inyo prefunding and Mastercard's BVNK platform are the two networks productizing well-trodden ground, not leapfrogging it.

## [2] Company history / fit
Both fit a long, well-documented trajectory in the corpus: Visa Direct stablecoin prefunding was first a **pilot announced at SIBOS 2025** ([[Visa to pilot pre-funded stablecoins via Visa Direct]], [[Visa launches stablecoin prefunding pilot via Visa Direct]], [[Visa Direct taps stablecoins for faster business funding]]), then settlement expansion through 2026. Mastercard's path: Paxos Global Dollar Network (2025-06), acquiring **BVNK for up to $1.8bn** ([[Mastercard to acquire stablecoin firm BVNK for up to $1.8bn]]), Zerohash ~$2bn, settlement expansion ([[Mastercard expands settlement to include stablecoins and weekends]]). The two events in this roundup are the logical next steps of those arcs — structurally unsurprising.

## [3] Novelty / value-add / traction
**Low novelty for THIS note.** The genuine news (pilot→production for Visa; BVNK platform launch for Mastercard) is real but is ALREADY captured in dedicated same-month notes:
- Visa: [[Visa Direct moves stablecoin payouts to production with Inyo Global]] (2026-10-16, status: published, enriched:true) — identical USDC/Inyo/180+ countries facts.
- Mastercard: [[Mastercard and BVNK launch global fiat-stablecoin money platform]] (2026-10-16, published) — identical single-API fiat+stablecoin platform facts.
- Adjacent: [[Mastercard launches Stablecoin Security risk intelligence in North America]].
This roundup adds only editorial juxtaposition, no new terms, numbers, partners, or reporting period. Traction (merchant/GMV adoption) is not quantified here. → **duplicate_of the Visa production note** (lead half); also overlaps the Mastercard BVNK note.

## [4] What's next / market sentiment
Direction is clear and already well-covered: networks keep embedding regulated stablecoins into settlement/payout/liquidity layers (Open USD, BVNK, Inyo, settlement run-rate growth). Counterintuitive second-order point — the more both networks "embed" stablecoins invisibly behind fiat UX, the more the value accrues to the **rail/liquidity layer** (Visa Direct, Mastercard Move/BVNK) rather than to the stablecoin issuers, reinforcing incumbent capture rather than disintermediation. But none of that needs this roundup to be told — the dedicated notes carry it.

## Sources
- Visa Direct USDC prefunding live via Inyo Global: https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-direct-moves-stablecoin-pilots-production.html ; https://financefeeds.com/visa-direct-stablecoin-for-cross-border-payments/ ; https://coingape.com/visa-advances-stablecoin-strategy-as-usdc-prefunding-hits-live-operations-on-visa-direct/
- Mastercard + BVNK Global Money Platform (2026-10-17); Mastercard CEO on stablecoins for cross-border (2026-10-09, Bloomberg/PYMNTS); Mastercard Stablecoin Security risk intelligence: https://www.mastercard.com/us/en/news-and-trends/press/2026/october/Mastercard-brings-risk-intelligence-to-stablecoin-payments.html
- Internal: [[Visa Direct moves stablecoin payouts to production with Inyo Global]], [[Mastercard and BVNK launch global fiat-stablecoin money platform]], [[Mastercard launches Stablecoin Security risk intelligence in North America]], [[Visa to pilot pre-funded stablecoins via Visa Direct]], [[Visa reports nearly 200% YoY stablecoin card payment growth]], [[Mastercard to acquire stablecoin firm BVNK for up to $1.8bn]]
- Roundup primary: https://max.ru/fintexno (Финтехно)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is any fact here new vs the corpus?** No — the Visa USDC/Inyo production launch and the Mastercard BVNK platform are each already in dedicated 2026-10 notes. Only the juxtaposition is new. (stale)
2. **Is this a primary announcement or a roundup?** A Финтехно channel roundup/commentary (max.ru/fintexno), explicitly aggregating two events. Not primary.
3. **Visa half — pilot or production?** Production/commercial, first processor Inyo Global, ~2026-10-15. Already captured in [[Visa Direct moves stablecoin payouts to production with Inyo Global]].
4. **Mastercard half — what exactly?** The truncated "Mastercard строит..." maps to the Mastercard+BVNK Global Money Platform (single-API fiat+stablecoin), 2026-10-17 — already in [[Mastercard and BVNK launch global fiat-stablecoin money platform]]. Could also partly reference Stablecoin Security risk intelligence.
5. **Which prior note is the primary duplicate?** The Visa production note (lead + most detailed half of the roundup). Mastercard BVNK note is a secondary overlap.
6. **Any NEW terms, numbers, partners, or reporting period?** None found. No volumes, no new counterparties beyond Inyo/BVNK already named elsewhere.
7. **Does the end user touch crypto?** No — USDC is internal liquidity; recipient gets local fiat. (Confirmed, but not novel.)
8. **Traction / adoption quantified?** No merchant/GMV/live-client numbers in this item. Open.
9. **Could the Mastercard half be a genuinely different event than the BVNK platform?** Possible it blends BVNK platform + Stablecoin Security, but both are already covered same-month; either way → stale.
10. **Does the "they do it differently" contrast change the central question?** No — it's editorial framing; the substance (both networks embedding regulated stablecoins into rails) is thoroughly covered.
11. **Who captures the margin?** Rail/liquidity layer (Visa Direct, Mastercard Move/BVNK), not issuers — reinforces incumbents. (analysis; already derivable from dedicated notes.)
12. **Any regulatory/competitive delta disclosed?** No. Silent on economics, fraud liability, exclusivity.
13. **Would publishing this duplicate degrade the digest?** Yes — it would re-tell two items the reader already got as standalone notes.
14. **Verdict confidence?** High — exact entity/figure overlap (Inyo Global, USDC prefunding, 180+ countries; BVNK single-API fiat+stablecoin).

**Importance: 2/5 — rationale:** The underlying moves are strategically meaningful, but THIS item is a reworded roundup with zero new development; both halves are already covered by dedicated, published, enriched same-month notes. Mark STALE, duplicate_of the Visa production note.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Stablecoin settlement/cross-border is the fastest-growing adjacent rail to card networks. Stablecoins are on pace to process ~$40–46tn in raw on-chain volume in 2026, with real-world payment volume ~$400bn in 2025 (~60% B2B); FXC Intelligence sizes the B2B stablecoin cross-border TAM at ~$14.7tn base / ~$20.4tn upside (per FXC Intelligence / KuCoin recap, as of 2026). By comparison Visa + Mastercard move ~$16tn in combined annual payments volume — i.e. stablecoins are a credible parallel rail for the funding/settlement leg, not (yet) the acceptance leg. **Structure:** the acceptance/authorization layer stays a consolidated duopoly (Visa + Mastercard), but the stablecoin *liquidity/settlement* layer is fragmenting fast (Circle/USDC, Tether/USDT, PayPal PYUSD, bank consortia). **Why now:** post-GENIUS-Act regulatory clarity + a 24/7 always-on liquidity demand that correspondent banking (banking-hours, pre-funded nostro) can't meet. Both networks are defending the *funding/settlement* flow before a stablecoin-native stack disintermediates it.

**Competitive landscape.** Sector KPIs: payments/gross-dollar volume, cross-border volume growth, processed/switched transactions, settlement run-rate. Two distinct plays here: Visa keeps the stablecoin *inside* its own rail (USDC prefunds Visa Direct liquidity; recipient still gets fiat on card/account), whereas Mastercard is buying a stablecoin-native settlement stack to sit *alongside* cards.
- **Visa** — Visa Direct USDC prefunding moved from pilot to commercial production on 2026-10-15, Inyo Global first enabler (Visa Direct reaches 180+ countries). Visa's own stablecoin *settlement* run-rate scaled from ~$7bn annualized (reported 2026-04-29) to >$20bn annualized by Sept 2026 (per web recap) — still a rounding error vs ~$4tn quarterly payments volume.
- **Mastercard** — completed the ~$1.8bn BVNK acquisition on 2026-08-03, adding ~$30bn annualized stablecoin payment volume across 130 markets / 25+ licenses; BVNK added Stellar in Sept 2026. See [[Coinbase and Mastercard in talks to buy stablecoin firm BVNK]] (bidding war, 2025-10) and [[Rain reaches $1.95 billion valuation and to launch Mastercard cards]].
- **Peers / disruptors:** Circle (USDC issuer, the actual rail Visa rides), PayPal (PYUSD), Stripe/Bridge, Citi+Coinbase ([[Citi details stablecoin checkout with Coinbase]]), Euronet+Fireblocks ([[Euronet and Fireblocks extend partnership to bring stablecoins into card issuing]]).
- **Position:** both networks are incumbents *co-opting* the rail from a position of strength (distribution, compliance, 180+ country reach) — moat is network effects + regulatory licensing, not the stablecoin tech itself `(analysis)`.

**Comps & multiples.** Both protagonists are IR-covered; folding their own filed results as primary evidence:
- **Visa** — Q3 FY2026 (qtr ended 2026-06-30, 8-K filed, earnings release): net revenue $11.6bn (+14%); payments volume crossed $4tn for the first time (+10% cc); total cross-border volume +13% cc; 71.7bn processed transactions (+10%); non-GAAP EPS $3.32 (+11%). Market cap ~$790bn, trailing P/E ~29.9x (per macrotrends/companiesmarketcap, Oct 2026). EV/Revenue sanity: ~$790bn / ~$40bn FY-run-rate net revenue ≈ **~19.8x** — top of the EV/Rev range, justified by ~40bn-revenue scale + mid-teens growth + ~65%+ operating margin `(analysis)`.
- **Mastercard** — Q2 2026 (qtr ended 2026-06-30, 8-K earnings release): net revenue $9.28bn (+14%, +12% cc); gross dollar volume $2.9tn (+8% lc); cross-border volume +12% lc; switched transactions +9%; adjusted EPS $5.04 (+21%). Market cap ~$541bn, trailing P/E ~33.9x, fwd P/E ~28.3x (Oct 2026). Mastercard trades *richer* on P/E (33.9x vs 29.9x) — in-line-to-rich, consistent with faster VAS/EPS growth `(analysis)`.
- **Stablecoin-rail comp:** Mastercard paid ~$1.8bn for BVNK's ~$30bn annualized volume ≈ **~6.0% of annualized volume** as a price-to-volume proxy (not a revenue multiple — BVNK take-rate not disclosed → actual EV/Rev `[UNSOURCED]`).
- Full EV/EBITDA, clean EV, forward consensus → `[UNSOURCED]` (no free source). Both are rich-but-in-line vs each other; cheap/rich verdict: **in-line**, growth-justified.

**Risk flags.**
1. **Disintermediation of the settlement leg.** Stablecoins already move ~2–3x the combined V+MA volume on-chain; if merchants/PSPs adopt stablecoin acceptance end-to-end, the networks' interchange/cross-border premium (their richest revenue) is bypassed. Embedding USDC into *their own* rail is a defensive moat-preservation move, not pure upside.
2. **Dependence on someone else's rails/issuer.** Visa's flow rides Circle's USDC — a third-party issuer whose depeg, reserve, or regulatory event would hit Visa's advertised liquidity product; Visa captures the flow but not the float economics. Mastercard mitigates by *owning* BVNK, but inherits 25+ licenses of compliance/regulatory exposure.
3. **Economics still undisclosed / small base.** Visa's stablecoin settlement >$20bn annualized is <1% of ~$16tn volume; neither network discloses take-rate or margin on the stablecoin leg — "announced/live" ≠ "material to revenue". Fraud-liability and chargeback treatment on stablecoin payouts is unaddressed in PR.

**What this changes (idea-lens).** `(analysis)` This is incumbents absorbing a disruptive rail rather than being disrupted by it — a defensive re-rating of the *funding/settlement* layer, not a new profit pool yet. Watch: (a) whether stablecoin settlement run-rate compounds past ~$50bn and management starts disclosing take-rate — the trigger that would make it financially material; (b) whether Mastercard monetizes BVNK's $30bn volume at a card-like take-rate. Falsifiable: if 12 months out neither network breaks out stablecoin revenue, the thesis "this is a strategic defensive play, not a near-term earnings driver" holds.

Sources: https://s1.q4cdn.com/050606653/files/doc_financials/2026/q3/Q3-2026-Earnings-Release_vF.pdf · https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm · https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000081/ma06302026-exx991xearnings.htm · https://investor.visa.com/news/news-details/2026/Visa-Direct-Launches-Stablecoin-Powered-Money-Movement-as-Pilots-Move-to-Production/default.aspx · https://www.theblock.co/news/business/2026-10-16-visa-direct-moves-usdc-prefunding-into-commercial-production-with-inyo-global-418802 · https://www.mastercard.com/us/en/news-and-trends/press/2026/august/mastercard-completes-acquisition-of-bvnk-to-advance-global-stabl.html · https://www.fxcintel.com/research/analysis/ct-mastercard-q2-2026-earnings · https://companiesmarketcap.com/visa/marketcap/ · https://www.macrotrends.net/stocks/charts/MA/mastercard/market-cap
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_Subject: Visa and Mastercard embed stablecoins into payment rails (stablecoin-rails commentary — grounded in latest filed quarterly results)._

This is a rails/strategy story, not an earnings release — there are no stablecoin-specific P&L figures. Below the two networks' latest **filed** quarterly results frame the thesis: stablecoins are being bolted onto two still-accelerating cross-border franchises, not onto stressed ones. Cross-border — the exact flow (Visa Direct pre-funding, Mastercard settlement) that USDC targets — is the fastest-growing line for both, which is why the embedding matters strategically rather than financially today.

**Verdict (context read).** CONTEXT, not a beat/miss on this news. Both networks are compounding double-digit, cross-border-led, high-margin: Visa fiscal Q3 2026 (qtr ended Jun 30, 2026) net revenue $11.6bn (+14% YoY; +13% constant-dollar); Mastercard Q2 2026 (qtr ended Jun 30, 2026) net revenue $9.3bn (+14%; +12% currency-neutral). Stablecoin rails are additive optionality on top of a franchise that is still growing, not a rescue.

**Key figures (latest filed quarter — both ended Jun 30, 2026).**
- **Visa (fiscal Q3 2026):** net revenue **$11.6bn, +14% YoY** (+13% constant-dollar). GAAP net income **$5.6bn** / EPS **$2.97** (+7% / +10%); non-GAAP net income **$6.3bn** / EPS **$3.32** (+8% / +11%). GAAP operating margin **59.1%**; non-GAAP **66.7%**. Payments volume **+10%** (constant dollars); processed transactions **71.7bn, +10%**; capital returned $6.2bn.
- **Mastercard (Q2 2026):** net revenue **$9.3bn, +14%** (+12% currency-neutral). GAAP net income **$4.4bn** / EPS **$4.97**; adjusted net income **$4.5bn** / adj EPS **$5.04**. GAAP operating margin **60.2%**; adjusted **61.1%**. Gross dollar volume **+8%** (local currency); switched transactions **+9%**. Value-added services & solutions revenue **+20%** (+18% currency-neutral).

**By driver — why cross-border is the hinge.** Cross-border is the highest-yield, fastest-growing line for both and the exact flow stablecoins attack. **Visa cross-border volume +13% YoY** (+12% ex-intra-Europe, constant dollars) — outpacing total payments volume (+10%). **Mastercard cross-border volume +12%** (local currency) — outpacing GDV (+8%). The USDC pre-funding thesis (frozen correspondent-banking liquidity, 24/7 settlement outside banking hours) maps directly onto this already-outperforming segment: it defends/extends the most profitable flow rather than opening a new revenue line. Mastercard's value-added services (+20%) is the margin-mix tailwind that stablecoin settlement/MTN tooling would eventually feed into.

**vs expectations / prior period.** No consensus on this commentary item (not an earnings event) → qualitative. Momentum is intact and roughly steady: Visa net revenue +15% (fiscal Q1) → +17% (Q2) → +14% (Q3 2026); Mastercard +16% (Q1) → +14% (Q2 2026). Mastercard management said Q2 "delivered above expectations" at +14% net-revenue growth — i.e. a modest beat on its own frame. [UNSOURCED] precise public consensus $/% not pulled (semsearch/IR embedder down, 402).

**Guidance / forward.** Neither latest release in the IR set carries explicit forward guidance for this period (Mastercard release gave none; Visa release emphasized resilient consumer/business spending, no quantified reaffirm captured). Forward read on the thesis: stablecoin rails are still pre-revenue plumbing — Visa Direct USDC pre-funding only moved to commercial production Oct 15, 2026 (Inyo Global first, 180+ countries); Mastercard announced regulated-stablecoin settlement Jun 3, 2026 (USDC/PYUSD/RLUSD/USDG/USDP/SoFiUSD across Ethereum/Solana/Polygon/Base/Arbitrum/XRPL via Multi-Token Network) and bought stablecoin-infra firm BVNK (closed ~Aug 3, 2026). None of this is yet a disclosed segment or a numbered contributor to the quarters above.

**Thesis-flags.**
1. **Defensive, not dilutive (announced vs live).** Fact: both are inserting stablecoins *inside* their own rails (Visa Direct pre-funding → payout still lands fiat on card/account; Mastercard settlement/MTN). Why: this keeps the network in the value chain rather than letting USDC disintermediate the cross-border leg. Why it matters: protects the +12–13% cross-border engine, the richest yield line. Second-order: competitive moat vs direct on-chain remittance, but also an admission that stablecoins are a real substitute threat to correspondent-banking economics.
2. **Zero financial contribution so far (de-PR: who's silent).** The strong Q2/Q3 2026 prints were driven by conventional volume and cross-border, *not* stablecoins — neither company quantifies stablecoin revenue, volume, or margin. Treat the embedding as strategic optionality; modeling near-term upside from it would be fabrication.
3. **Margin durability is the real anchor.** Visa non-GAAP op margin 66.7%, Mastercard adjusted 61.1% — any stablecoin rail must clear this bar to be accretive. The risk is that cheaper on-chain settlement compresses the very take-rate it's meant to defend; management has not addressed this trade-off in the captured disclosures.

Sources: Visa Reports Fiscal Third Quarter 2026 Results (8-K/EX-99.1, filed ~Jul 2026) https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm · Visa Q3-2026 Earnings Release PDF https://s1.q4cdn.com/050606653/files/doc_financials/2026/q3/Q3-2026-Earnings-Release_vF.pdf · Mastercard Q2 2026 earnings (8-K/EX-99.1) https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000081/ma06302026-exx991xearnings.htm · Visa Direct USDC pre-funding commercial launch (TheBlock, 2026-10-16) https://www.theblock.co/news/business/2026-10-16-visa-direct-moves-usdc-prefunding-into-commercial-production-with-inyo-global-418802 · Mastercard on-chain stablecoin settlement (CoinDesk, 2026-06-03) https://www.coindesk.com/markets/2026/06/03/mastercard-expands-on-chain-settlement-in-bet-on-stablecoins-and-always-on-finance · public consensus $/% [UNSOURCED] (semsearch/IR embedder 402 down).
<!-- /enrichment:earnings_review -->
