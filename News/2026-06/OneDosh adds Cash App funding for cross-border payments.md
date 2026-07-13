---
title: "OneDosh adds Cash App funding for cross-border payments"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/onedosh
  - company/cash-app
  - industry/remittances
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/1d1f580b
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s5e3c2acf
month: 2026-06
enriched: true
importance: 2
freshness: fresh
---

# OneDosh adds Cash App funding for cross-border payments

> [!info] 2026-06-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 OneDosh adds Cash App funding to streamline cross-border payments. The new feature allows eligible U.S. users to fund their OneDosh wallets directly through Cash App, enabling them to transfer value more efficiently across the U.S.–Nigeria corridor.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/1d1f580b>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: OneDosh adds Cash App funding for cross-border payments
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS VERDICT: FRESH.** This is a distinct, dated product event (Cash App funding rail, announced ~2026-06-23/26), not a re-report of the OneDosh capital raises. Internal corpus has two prior OneDosh *funding* notes — [[OneDosh raises $3M pre-seed for stablecoin payments]] (2026-01-22) and [[OneDosh adds $1 million for stablecoin payments infrastructure]] (2026-06-12, total $4M) — but neither covers this Cash App integration. Not a duplicate; it is a thin product/distribution tweak by the same tiny issuer.

## [0] What exactly happened (de-PR'd)
OneDosh — a ~16-month-old (founded Feb 2025, NYC) stablecoin remittance startup, $4M total pre-seed, self-claimed "200k+ users" — added **Cash App as a funding rail** for its USD wallet on the US→Nigeria corridor. Eligible US users top up the OneDosh USD wallet from Cash App; USD then converts to NGN for payout. Promo: **zero OneDosh fees through 2026-08-31** (per BusinessDay coverage). Marketed as "first platform to enable instant fiat funding from Cash App convertible into naira," pitching access to "60M+ Cash App users."
- **Why this framing reveals the real substance:** the company credits "Cash App, **Lightspark**, and other technology partners" (TechAfrica, 2026-06-25). That strongly implies the rail is **Lightspark UMA / Bitcoin-Lightning**, riding Block's 2026 rollout of Lightning in Cash App — i.e. value likely leaves Cash App as a Lightning/UMA payment OneDosh receives and settles to USD/stablecoin, **not** a native "Cash App Pay" or ACH integration. This matters because Cash App itself does not do international transfers (US/UK only). So "first Cash App→naira" is plausibly literally true but is a marketing wrapper over a thin, replicable Lightning-bridge feature (analysis).
- **What's silent (the anti-PR gate):** no Block/Cash App press release or endorsement — "support of Cash App" is OneDosh's wording only. No post-promo fee schedule, **no FX spread disclosed** (the real cost in remittances lives in the FX margin — exactly what's hidden). No MSB/MTL license disclosure anywhere in coverage. Much coverage is brandpress/wire echoing one release.

## [1] Competitors / peers
US–Nigeria / US–Africa remittance field, dated:
- **LemFi** — ~$87M raised; Series B $53M (2025-01, Highland Europe) + a 2026-05 round; **2M+ customers, >30 markets, claims >$1B/month volume**; Tether strategic investment ([[Tether invests in LemFi to expand stablecoin remittances]], 2026-05-14). Unofficial secondary ref ~$5B.
- **Remitly (RELY)** — market cap ~$3.6B (Feb 2026); FY2025 revenue $1.6B, send volume $74.9B (+37%); Remitly One membership ([[Remitly launches Remitly One membership tier]], 2025-09).
- **Wise (WISE.L)** — ~$10.5B mcap (Jun 2026); FY26 cross-border volume £181.7B (+25%), 18.9M active.
- **Zepz (WorldRemit/Sendwave)** — $5B (2021); repeated layoffs through Feb 2025; 11M+ users.
- **Flutterwave Send** ([[Flutterwave's Send app returns to Europe for diaspora remittances]], 2025-07), **NALA** ($40M Series A, Jul 2024), **Afriex** (stablecoin, $10M Series A), **Aspora** ([[Aspora raises $90M+ for Indian diaspora remittances]], $500M val — India corridor analogue).
- **Position: far behind / sub-scale.** OneDosh (200k users, $4M raised) is orders of magnitude smaller than every named peer. **Why none of the majors bother with "Cash App funding":** they already have direct ACH/debit/bank funding at scale and Visa/MC + bank rails; a Lightning bridge to a closed P2P wallet is an acquisition gimmick for a long-tail player, not a moat (analysis).

## [2] Company history / fit
Trajectory: Feb 2025 founded (team ex-Zero Hash/Plaid/Amazon) → Dec 2025 US+Nigeria launch (USD wallet, USD↔NGN, Visa USD card on Apple/Google Pay) → Jan 2026 $3M pre-seed → Jun 2026 +$1M ($4M total), claims 29 European countries + Canada → Jun 2026 Cash App funding. **Why it acts this way:** as a sub-scale stablecoin remittance issuer with no brand and a commodity corridor, its binding constraint is **US-side user acquisition and funding friction**. Bolting onto an app 60M+ Americans already hold is the cheapest distribution wedge available — consistent with the funding-led "infrastructure" narrative, but it is distribution plumbing, not new product capability.

## [3] Novelty / value-add / traction
Genuinely new: a Lightning/UMA bridge from Cash App into a naira-payout wallet — narrowly "first." But the value-add is thin: the underlying capability (Cash App ACH/Visa debit card; Lightspark Lightning↔USD bridges) already existed; OneDosh stitched them. **Traction = unproven.** Every scale claim (200k users) is self-reported; **no transaction volume, no adoption figures** for the Cash App rail. **Who captures the margin:** the durable economics are the FX spread (undisclosed) and any Lightspark/network take — OneDosh is a thin layer on someone else's rails (Block's Cash App + Lightspark's Lightning), which it does not control. A zero-fee promo to Aug 31 confirms it is buying volume, not earning it.

## [4] What's next / market sentiment
Plan: extend beyond US→Nigeria to wider SSA, UK, LatAm, UAE, Asia (announced, not live). **Market backdrop (the real opportunity):** US→Nigeria corridor ~$7.5–8.5B (2025); Nigeria total remittances ~$20.9B (2024, CBN) → ~$23B (2025e); SSA is the **costliest** region globally at ~8.45–8.78% to send $200 (World Bank RPW) vs ~6.5% global avg. **Why the structural pull is real but the OneDosh wedge is fragile:** high corridor cost is exactly what stablecoin/Lightning rails attack — but the same disintermediation that helps OneDosh also lets LemFi (Tether-backed), Afriex, and incumbents undercut it; being "first to Cash App→naira" is trivially copyable, and depends on Block tolerating third-party Lightning bridges out of Cash App. Counterintuitive second-order: reliance on Cash App rails makes OneDosh **dependent on Block's permission**, not safer for being attached to a big name.

## Sources
- techeconomy.ng/onedosh-launches-cash-app-funding (2026-06-24)
- dailypost.ng/2026/06/23/onedosh-launches-cash-app-funding (2026-06-23)
- techafricanews.com/2026/06/25/onedosh-adds-cash-app-funding (2026-06-25 — "Cash App, Lightspark, and other technology partners")
- nairametrics.com/2025/12/22/onedosh-launches-in-the-united-states-and-nigeria (launch)
- World Bank RPW Q1'24/Q1'25; Nairametrics 2025-07-26 (Nigeria $20.93B 2024); World Bank migration blog (SSA $56B 2024)
- Remitly IR Q4'25; companiesmarketcap (Wise); TechCrunch 2025-01-13 (LemFi)
- Internal: [[OneDosh raises $3M pre-seed for stablecoin payments]], [[OneDosh adds $1 million for stablecoin payments infrastructure]], [[Tether invests in LemFi to expand stablecoin remittances]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is there an official Block/Cash App partnership?** No — open. Coverage only quotes OneDosh "acknowledging the support of Cash App." No Block press release. "First Cash App→naira" is self-asserted.
2. **What is the actual mechanism?** Likely Lightspark UMA / Bitcoin-Lightning bridge (OneDosh credits "Cash App, Lightspark, and other technology partners"), not Cash App Pay or ACH. Cash App has no native international transfer (US/UK only). (analysis)
3. **Is the feature live or announced?** Described as live for eligible US users; but no adoption/volume data — treat as "shipped, adoption unproven."
4. **What are the economics after Aug 31, 2026?** Open. Post-promo fees and FX spread undisclosed — the real margin (FX) is silent.
5. **Is the "200k+ users" claim verifiable?** No — self-reported, no third-party data; no transaction volume disclosed at all.
6. **Does OneDosh hold MSB/MTL licenses?** Open — no FinCEN MSB / state MTL disclosure in any coverage; likely relies on a regulated partner's rails. Notable silence for a US USD-wallet operator.
7. **Is "first to enable Cash App→naira" actually novel?** Narrowly yes, but the components (Cash App debit/ACH, Lightspark Lightning↔USD) pre-existed; it is a stitch, trivially replicable by peers.
8. **Who captures the margin in the stack?** Block (Cash App) owns the user + funding endpoint; Lightspark owns the Lightning rail; OneDosh is a thin FX/payout layer it doesn't control. Margin durability is weak.
9. **How does this compare to LemFi/Remitly scale?** OneDosh is 1–3 orders of magnitude smaller (200k vs LemFi 2M / $1B-month; Remitly $74.9B/yr). Won't move the corridor.
10. **Does this depend on Block tolerating third-party Lightning bridges out of Cash App?** Yes (hypothesis) — a platform-policy single point of failure; Block could restrict it.
11. **Is the corridor opportunity real?** Yes — US→Nigeria ~$7.5–8.5B (2025); SSA costliest globally (~8.5–8.8% to send $200, World Bank). Genuine pain point.
12. **Why a zero-fee promo?** Buying volume, not earning it — signals acquisition push, not proven product-market fit.
13. **Is this a fresh event or a re-run of the OneDosh raises?** Fresh — distinct dated product launch, not the Jan $3M / Jun $1M funding notes. Not a duplicate.
14. **What would make this matter (5/5)?** Official Block endorsement + disclosed competitive FX + real volume. None present.
15. **Counterintuitive risk?** Attachment to Cash App's big-name rail makes OneDosh *more* dependent (Block's permission, Lightspark's pricing), not safer.

**Importance: 2/5 — rationale:** A sensible but minor distribution tweak (Lightning/UMA bridge from Cash App into a naira wallet) by a sub-scale ($4M, ~200k-user) early-stage player, marketed as a "first." No new corridor, license, capital event, or Block endorsement; economics (FX, post-promo fees) undisclosed; adoption unproven. Real corridor opportunity (US→Nigeria ~$8B, costliest region) is the only thing lifting it above a 1.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: US–Africa diaspora remittances / stablecoin cross-border payments. Size: remittances to Nigeria ~$20.93bn in 2024 (CBN, +8.9% YoY, via Nairametrics 2025-07-26) → ~$23bn 2025e; the US–Nigeria corridor is the single largest source at ~$7.5–8.5bn in 2025 (US+UK ≈ 60% of inflows, via Arbiterz). Sub-Saharan Africa total ~$56bn 2024 (World Bank). Structure: fragmented and contested — incumbents (MoneyGram, WorldRemit/Zepz), digital scalers (Remitly, Wise), African-diaspora specialists (LemFi, NALA, Afriex, Flutterwave Send) and a long tail of micro-issuers like OneDosh. Entry barriers are real on the capital/regulation side (MSB/MTL, banking partners, FX liquidity) but low on the feature side — funding rails are easily copied. Drivers + "why now": SSA is the **costliest** remittance region globally — ~8.45% (Q3 2024) rising to ~8.78% (Q1 2025) to send $200, vs ~6.5% global avg (World Bank RPW). That cost gap is precisely what stablecoin/Lightning rails (Tether→LemFi, Lightspark UMA) are attacking in 2025–26 → second-order: the same disintermediation that lets OneDosh ride Cash App also lets better-capitalized peers undercut it (analysis).

**Competitive landscape.** Sector KPIs: monthly/annual send volume (TPV), take rate, FX spread, funded-user count, cost-to-send %. Key players + recent dated moves: **LemFi** — ~$87m raised, 2M+ customers, claims >$1bn/month, Tether strategic investment ([[Tether invests in LemFi to expand stablecoin remittances]], 2026-05-14); **Remitly (RELY)** — FY2025 revenue $1.6bn, send volume $74.9bn (+37%) ([[Remitly launches Remitly One membership tier]]); **Wise** — FY26 cross-border volume £181.7bn; **Flutterwave Send** ([[Flutterwave's Send app returns to Europe for diaspora remittances]]). Basis of competition: price (FX spread + fees), payout speed/reach, and US-side distribution. OneDosh's position: **niche / sub-scale** — $4m raised, self-claimed ~200k users; the Cash App funding rail is a distribution wedge, not a moat. Moat: weak — thin layer on Block (Cash App) + Lightspark rails it does not control (analysis).

**Comps & multiples.** Public peers, market cap basis: **Remitly (RELY)** ~$3.6bn mcap (Feb 2026) on FY2025 revenue $1.6bn → P/S ≈ $3.6bn / $1.6bn = **2.3x**. **Wise (WISE.L)** ~$10.5bn mcap (Jun 2026); FY revenue not cleanly sourced here → EV/Rev = no data. Private peers (round valuations, not market cap): **LemFi** unofficial secondary ref ~$5bn [UNSOURCED — secondary, not a priced round]; **Aspora** $500m post-money (2025, India analogue, [[Aspora raises $90M+ for Indian diaspora remittances]]). OneDosh: $4m pre-seed, no public valuation/revenue → multiples **not computable**. With only one cleanly-comparable public figure (Remitly 2.3x P/S), distribution not computed — qualitative: OneDosh is pre-revenue-scale, valued on round size, not multiples. Flag: in-line for an early-stage issuer; nothing rich/cheap to assess.

**Risk flags.**
1. **Platform dependence / disintermediation (single point of failure):** the rail rides Cash App (Block) + Lightspark Lightning bridges OneDosh does not own; Block can restrict third-party Lightning bridges, and there is no confirmed Block partnership — "support of Cash App" is OneDosh's wording only. Attachment to a big name = more dependent, not safer.
2. **Margin captured elsewhere / opaque economics:** zero-fee promo only to 2026-08-31; post-promo fees and FX spread undisclosed — the durable margin (FX) is silent, and Block/Lightspark capture the funding + rail layers.
3. **Regulatory / scale risk:** no MSB/MTL license disclosure for a US USD-wallet operator; sub-scale ($4m, ~200k self-reported users) vs LemFi (2M, $1bn/mo) and Remitly ($74.9bn/yr) — execution/survival risk is high.

**What this changes (idea-lens).** For the sector: nothing structural — a long-tail issuer adding a copyable funding rail. Falsifiable thesis: if "Cash App→naira" mattered, expect (a) a Block/Cash App co-announcement and (b) larger peers (LemFi, Afriex) shipping the same Lightning-funding feature within ~6–12 months; trigger to watch = OneDosh disclosing actual Cash-App-funded volume or competitive FX. Absent those, this is noise, not a re-rating (analysis).

Sources: techeconomy.ng/onedosh-launches-cash-app-funding (2026-06-24) · techafricanews.com/2026/06/25/onedosh-adds-cash-app-funding · nairametrics.com 2025-07-26 (Nigeria $20.93bn 2024) · World Bank RPW Q1'25 (SSA ~8.78%) · arbiterz.com (US–Nigeria corridor) · Remitly IR Q4'25 · companiesmarketcap (Wise) · TechCrunch 2025-01-13 (LemFi)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
