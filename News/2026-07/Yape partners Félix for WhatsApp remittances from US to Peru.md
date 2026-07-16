---
title: "Yape partners Félix for WhatsApp remittances from US to Peru"
date: 2026-07-16
retrieved: 2026-07-16
tags:
  - company/yape
  - company/felix
  - industry/remittances
  - region/latam
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/ff5162a7
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s60a53f0c
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Yape partners Félix for WhatsApp remittances from US to Peru

> [!info] 2026-07-16 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Yape partners with FinTech Félix to facilitate sending remittances from the United States via WhatsApp to Peru. Thanks to this integration, users will be able to receive transfers directly into their digital wallet in soles or dollars through a simple process that combines the Yape app with the messaging platform.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/ff5162a7>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **2026-07-08**, Yape (Credicorp/BCP's Peruvian super-app) added **Félix** (US-based, WhatsApp remittance fintech) as an **inbound US→Peru receive rail**. A Yape user opens Remesas → "Quiero recibir" → "Félix vía WhatsApp", generates a link, and shares it with a relative in the US. The **sender pays entirely inside WhatsApp — no app to install**; funds land in the recipient's Yape wallet **in soles or dollars within minutes** (La República, Gestión, Peru-Retail, 2026-07-08).

- **Direction is the whole point (de-PR'd):** This is **INBOUND** (Yape = payout endpoint), NOT Yape's outbound-corridor expansion. It is distinct from [[Yape enables remittances from Peru to Bolivia]] (outbound, intra-group) and [[Peru's Yape expands remittances to Argentina and Chile]] (outbound). It DOES overlap the receive-side of [[Peru's Yape partners with Western Union on remittances]] (Aug/Sep 2025) — but via a different rail (Félix's WhatsApp/stablecoin flow vs WU's agent+digital network).
- **Limits:** up to **US$999 (S/3,000) per transfer, US$3,200 (S/12,000)/month**; only for Yape users with a BCP account or DNI-registered (La República/Gestión, 2026-07-08). Standard small-ticket retail family-remittance profile.
- **Mechanism (analysis, from Félix's known stack):** Félix funds transfers in **USDC** (Circle Mint), moves value over low-cost chains (Stellar), and converts to local currency via a payout partner — here landing directly in Yape. FX margin / who bears conversion cost is **undisclosed** in the Peru launch coverage. Whether payout is via dLocal (Félix's LatAm partner, see [[dLocal and Félix launch WhatsApp remittances to Central America]]) or direct is **unstated**.
- **Why structured this way:** Yape gets a US-origination front-end it does not own (WhatsApp senders in the US) without building US KYC/licensing; Félix gets instant access to Yape's ~16M-user distribution on the payout side. It is a **distribution swap**, each side plugging its weak end.

## [1] Competitors / peers
- **US→Peru receive rail into Yape:** direct overlap with **Western Union** ([[Peru's Yape partners with Western Union on remittances]], Aug 2025 — "first superapp WU offers receive in Peru", 550k users, usage tripled YoY, top sources US/Chile/Spain/Italy). Yape now has **two inbound US rails** (WU agent-network + Félix WhatsApp/stablecoin).
- **US→LatAm MTOs:** ~10 firms (Western Union, PayPal/Xoom, Remitly, MoneyGram, Ria, Intermex, Viamericas) run ~80% of US→LAC flows. **Remitly** is the digital-native benchmark on cost/UX; Félix's differentiator is the **WhatsApp conversational flow + stablecoin backend** (no app), targeting Latino senders where WhatsApp is default.
- **Félix's own footprint:** already live US→Mexico/Guatemala/Honduras/El Salvador ([[dLocal and Félix launch WhatsApp remittances to Central America]]), US→Ecuador (Peigo), plus a Mastercard tie-up ([[Felix and Mastercard accelerate US-to-LatAm remittances]]) and Nubank/Mexico deal. **Peru is a new corridor for Félix**, and Yape is its Peru payout anchor.
- **Position:** Yape is **catching up / adding optionality** on inbound US rails (WU already there); Félix is **expanding a proven WhatsApp-remittance model into a new country**. Neither party is doing anything mechanically novel vs its own past — the novelty is the *pairing* on the Peru corridor.

## [2] Company history / fit
- **Yape:** 2017 launch; ~19.4M users, ~16.4M MAU, +101% YoY revenue, profitable (Credicorp Q1 2026). Remittance cadence in 2026: Colombia (Feb), Argentina/Chile/Mexico/Italy (May), Bolivia (Jun), Venezuela fee-free after earthquakes (2026-07-15, Infobae) — roughly one corridor/month. This Félix deal is the **inbound-US complement** to that outbound push.
- **Félix:** founded 2020 (Manuel Godoy, Bernardo García); **$15.5M Series A (2024), $75M Series B (QED-led)**; ~**$7bn processed since inception** (Peru coverage cites this; Stripe case study cited $3bn earlier — figure has grown); Circle/USDC + Stellar rails, NPS >90. Peru extends its "WhatsApp + stablecoin" playbook to a **new high-value corridor**.
- **Fit:** logical for both. Yape's structural driver — it monetizes a two-sided super-app graph and wants to own the *receive* moment for the large US→Peru flow; partnering (vs building US ops) is capital-light. Félix's driver — corridor expansion is its growth engine, and Yape is the single best payout distribution in Peru.

## [3] Novelty / value-add / traction
- **Genuinely new:** first **WhatsApp-native, stablecoin-backed** inbound rail into Yape for US→Peru; Félix's Peru market entry. This is NOT a re-run of the WU note (different rail, sender UX, and backend) nor of any outbound Yape note.
- **But value-add is incremental, not structural:** Yape already had a US receive rail (WU). The delta is a *second, cheaper/faster-claimed* rail and a better sender UX (no app). **Traction = zero at announcement** — no disclosed volume, users, or fee/FX terms for the Peru corridor. "Within minutes / no app" is the standard Félix marketing claim, not a Peru-specific metric.
- **Who captures the margin (analysis):** in the stack, the FX spread + payout fee is split between Félix (USDC funding, orchestration) and Yape (payout distribution). Circle earns on USDC; the chain (Stellar) is near-zero cost. The real economic question is whether the stablecoin backend actually undercuts WU's fee to the end user, or whether the saving is captured by the operators — **undisclosed**.

## [4] What's next / market sentiment
- **Corridor size is the reason this matters:** Peru received **~US$5.37bn in remittances in 2025** (BCRP), the **US the #1 source**; central bank projects ~US$5.75bn by 2027. Even a small share of the US→Peru slice is a meaningful pool — bigger than the Peru→Bolivia lane in [[Yape enables remittances from Peru to Bolivia]].
- **Expect:** Félix to add more Yape-adjacent features; Yape to keep stacking inbound rails (WU + Félix + possibly TerraPay/stablecoin) and outbound corridors on its monthly cadence.
- **Risks / silence:** no disclosed FX margin or fee (the anti-PR gate — "no app, minutes" hides the *price*); no volume commitment; US remittance-tax / immigration-policy headwinds on Latino senders (a 2025–26 US theme) could dampen the whole US→LatAm pool; regulatory/AML on a stablecoin-backed cross-border flow into a bank-owned wallet.
- **Central question (analysis):** for Yape this is **rail redundancy + engagement lock-in on the receive side of Peru's largest remittance flow**, not a step-change; for Félix it is **corridor #N of a repeatable expansion**. Weight comes from the corridor size (US→Peru $5.4bn) and Yape's dominance, not from mechanical novelty.

## Freshness verdict
**FRESH.** New corridor (US→Peru), new rail (Félix WhatsApp/stablecoin), new market entry for Félix. Overlaps the *receive-side theme* of [[Peru's Yape partners with Western Union on remittances]] but is a **different partner, rail, and sender UX** — not a reprint. Distinct from all outbound Yape notes.

## Sources
- La República 2026-07-08 — https://larepublica.pe/economia/2026/07/08/yape-se-asocia-con-felix-para-facilitar-el-envio-de-remesas-desde-estados-unidos-via-whatsapp-hnews-546640
- Gestión (Godoy interview) — https://gestion.pe/g-de-gestion/reportaje/felix-y-yape-la-fintech-de-remesas-de-eeuu-ingresa-a-peru-manuel-godoy-habla-de-sus-planes-noticia/
- Peru-Retail — https://www.peru-retail.com/yape-incorpora-envio-de-remesas-desde-ee-uu-mediante-whatsapp-como-funciona-el-servicio/
- Rio Times — https://www.riotimesonline.com/yape-felix-whatsapp-us-remittances-peru-bcp-wallet-2026/
- Félix Series B ($75M) — https://www.finextra.com/newsarticle/45791/flix-raises-75-million-for-whatsapp-based-stablecoin-remittance-platform
- Félix/Circle case study — https://www.circle.com/case-studies/felix
- Inter-American Dialogue remittance outlook 2025 — https://thedialogue.org/blogs/2025/04/the-state-of-the-remittance-industry-and-an-outlook-for-2025
- Digest original — https://www.connectingthedotsinfin.tech/r/ff5162a7
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
1. **Is it really new, or a re-run of the WU deal?** → Different partner (Félix vs WU), different rail (WhatsApp/stablecoin vs agent+digital), different sender UX (no app). **Fresh** — a second inbound US rail, not a reprint.
2. **What is the actual fee and FX margin to the end user?** → **Open/undisclosed.** "No app, minutes" hides the price. The anti-PR gate: without the fee we can't say it beats WU/Remitly.
3. **Is the stablecoin cost saving passed to users or captured by Félix/Yape?** → **Open.** Circle earns on USDC, chain cost ~0; split of the spread undisclosed.
4. **Who does US payout via — dLocal, direct, or Yape's own rails?** → **Open.** Coverage doesn't name the payout partner for Peru.
5. **How big is the US→Peru corridor specifically (vs the $5.37bn total)?** → US is the #1 source but the exact US→Peru USD figure is **open**; total Peru inbound ~$5.37bn (2025, BCRP).
6. **Is it live for all Yape users or phased?** → Live for BCP-account or DNI-registered Yape users; broader gating **open**.
7. **What traction at launch?** → **Zero disclosed** — no volume/users/GMV for the Peru corridor. Announcement, not adoption.
8. **Does Félix's $7bn-processed figure hold up?** → Peru coverage cites ~$7bn cumulative; earlier Stripe case study said $3bn. Figure has grown over time; treat as company-reported, **directionally credible but unaudited**.
9. **How does this compete with WU (already on Yape) on cost/speed?** → Claims minutes + no app; cost comparison **open** without fee disclosure.
10. **US policy risk:** could a US remittance tax / immigration crackdown shrink the Latino-sender base? → Material macro headwind on the whole US→LatAm pool; **open** on magnitude.
11. **AML/sanctions posture** on a stablecoin-backed inbound rail into a bank-owned wallet? → **Open**; Félix runs KYC/AML in-flow per its dLocal deals, but Peru-specific reporting unstated.
12. **Who needs whom more?** → Roughly symmetric: Félix needs Yape's Peru distribution; Yape wants a US-origination front-end it doesn't have to build/license. Neither is dependent.
13. **Is this rail redundant given WU already delivers US→Yape?** → Partly — it's a second rail; value is a better sender UX + potential cost edge, not a new capability for Yape.
14. **Exclusivity?** → **Open.** No indication Félix is exclusive to Yape in Peru or Yape exclusive to Félix on WhatsApp.
15. **Second-order:** does stacking multiple inbound rails (WU + Félix) commoditize the corridor and compress everyone's take rate? → (analysis) Likely — more rails into the same wallet pressures fees; Yape wins on engagement even if per-transfer economics thin.

**Importance: 3/5** — Above the Bolivia note (2/5) because the corridor is materially larger and more strategic: US→Peru is Peru's #1 remittance source within a ~$5.37bn (2025) inbound pool, and the deal marks a credible, well-funded fintech (Félix, $75M Series B, ~$7bn processed) entering Peru via the country's dominant wallet (~19.4M users). But it is held to 3, not higher, because: (a) Yape already had a US receive rail (Western Union), so this is rail redundancy/optionality, not a new capability; (b) zero disclosed traction, fee, or FX terms at launch — pure announcement; (c) mechanically neither party does anything novel vs its own prior deals. Weight is corridor size + distribution, not novelty.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** US→Peru remittances is a sub-corridor of the ~$100bn US→LatAm flow. Peru received ~$5.37bn in total remittances in 2025, with the US the main source (per Rio Times, citing the deal briefing, as of 2026-07); LAC-wide remittances hit a record $173.7bn in 2025, +7.3% y/y (per IDB, as of 2025). Structure is fragmented at the send side (Western Union, Remitly, MoneyGram, Xoom, plus crypto-rail entrants like Félix/dLocal) but the Peru receive side is concentrating fast onto Yape — a BCP/Credicorp-owned superapp with 16m+ active users (per Rio Times, 2026-07; 15m in 2025 per Western Union PR). Why now: (1) migrant-remittance policy risk in the US is pushing senders toward digital/instant channels; (2) stablecoin/crypto rails (USDC) compress correspondent-banking cost and settlement time — the same USDC-funded model Félix runs elsewhere; (3) WhatsApp-native UX removes the app-download barrier for both sides. World Bank pegs the average cost to send $200 at ~6.4%, the cost pool these rails attack (per dLocal/Félix PR, 2025).

**Competitive landscape.** Sector KPIs: send volume / TPV, take rate (revenue/volume), cost-to-send %, active users, settlement time. Send side into Peru: Western Union (already integrated into Yape since 2025-08, S/3,500 per tx / S/12,000 monthly caps — [[Peru's Yape partners with Western Union on remittances]]), Remitly, MoneyGram/Xoom, and now Félix. Félix's basis of competition is distribution (WhatsApp, ~400k–500k Latino migrant users in the US) + crypto-rail speed (USDC funding, sub-2-min delivery, ~99% success in prior corridors); it has processed ~$7bn since launch (per Rio Times, 2026-07). Recent Félix moves: US→Central America w/ dLocal (2025-11 — [[dLocal and Félix launch WhatsApp remittances to Central America]]), Mastercard tie-up (2025-11 — [[Felix and Mastercard accelerate US-to-LatAm remittances]]), Colombia (2025-09), Dominican Republic (2026-04), now Peru (2026-07). Yape's own outbound remittance push (Argentina/Chile/Mexico/Italy, 8 destinations — [[Peru's Yape expands remittances to Argentina and Chile]]; Bolivia [[Yape enables remittances from Peru to Bolivia]]) shows it wants to own both send and receive legs regionally. Position: on the Peru *receive* side Yape is ahead/dominant (network effects + BCP account rails = switching-cost moat, `(analysis)`); Félix is a *new entrant* to Peru layering onto Yape's installed base rather than competing with it. Transfer caps here: $999/tx, $3,200/month (per Rio Times, 2026-07).

**Comps & multiples.** Public send-side peers (market caps as of Jan 2026):
- Remitly (RELY): revenue $1.635bn (+29%), send volume $74.9bn (+37%), 9.3m active users, adj. EBITDA $272m, mkt cap ~$2.87bn → P/S = $2.87bn / $1.635bn = **1.8x**; price-per-user = $2.87bn / 9.3m = **~$309/user** (per companiesmarketcap/Remitly IR, FY2025).
- dLocal (DLO), the crypto-rail payout peer to Félix's model: revenue >$1.1bn (+60% TPV to $40.8bn), net income $197m, mkt cap ~$4.38bn (Q3 2025) → P/S = $4.38bn / $1.1bn = **~4.0x** (per StockTitan/dLocal IR, FY2025). Richer than Remitly, justified by faster growth + stablecoin-rail margin story (growth-multiple correlation).
- Western Union (WU): revenue $4.05bn (−3.8% y/y, declining) — legacy incumbent, the disintermediation target; EV/multiples not computed (mkt cap not sourced), but flat-to-shrinking revenue anchors the low-growth end of the peer range.
Félix and Yape are private → no market cap; last-round valuations `[UNSOURCED]`. Internal comps above as `[[wikilinks]]`. Distribution: RELY 1.8x vs DLO ~4.0x P/S — the rail/growth premium is the read-across, not the absolute level. In-line-to-cheap for the growth cohort; WU is the cheap/declining outlier by design.

**Risk flags.**
1. **Dependence on someone else's rails / disintermediation of Félix.** Félix is one of at least three US→Peru pipes into Yape (WU, Remitly, itself); Yape owns the receive relationship and the 16m users, so Félix captures thin send-side economics and can be substituted. The value accrues to the wallet, not the corridor operator — second-order: Félix's Peru unit economics are hostage to Yape's willingness to keep the integration non-exclusive.
2. **Regulatory / de-risking exposure.** USDC-funded cross-border flows plus tightening US migrant-remittance scrutiny (potential remittance taxes/KYC load) could raise cost-to-send and compress the very margin advantage the crypto rail creates.
3. **Concentration on a single receive counterparty (Yape/BCP).** Caps ($999/tx, $3,200/mo) and reliance on one wallet mean any BCP compliance/outage/policy change is a single point of failure for the corridor.

**What this changes (idea-lens).** `(analysis)` This is a *new-entry*, not a re-rating: it deepens the thesis that receive-side LatAm wallets (Yape, Nequi, Mercado Pago) are becoming the remittance chokepoint, relegating send-side brands (WU, even Remitly) to interchangeable pipes. Falsifiable thesis: if Yape keeps signing multiple non-exclusive US senders (WU, Félix, +more), the wallet — not the transfer operator — captures the corridor's pricing power. Trigger to watch: whether Yape moves to exclusive send partnerships or launches its own US-side send app (it already runs outbound remittances to 8 countries); that would be the tell that it intends to own the full stack and squeeze Félix out. Thesis breaks if Félix's WhatsApp distribution proves stickier than the wallet and it retains the sender relationship across corridors.

Sources: https://www.riotimesonline.com/yape-felix-whatsapp-us-remittances-peru-bcp-wallet-2026/ · https://www.iadb.org/en/blog/migration/remittances-latin-america-and-caribbean-ease-after-2025-surge · https://companiesmarketcap.com/remitly/revenue/ · https://ir.remitly.com/news-releases/news-release-details/remitly-reports-fourth-quarter-and-full-year-2025-results-above · https://www.stocktitan.net/news/DLO/d-local-reports-2025-fourth-quarter-financial-m11toka2fiil.html · https://www.kenresearch.com/us-latam-remittance-corridors-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
