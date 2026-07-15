---
title: "Kraken supports Tempo blockchain for USDT0 and USDC.e"
date: 2026-07-14
retrieved: 2026-07-14
tags:
  - company/kraken
  - industry/stablecoins
  - industry/crypto
  - region/us
  - type/partnership
sources:
  - https://www.connectingthedotsinfin.tech/r/222bf3e1
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sb1d9e6d7
month: 2026-07
enriched: true
importance: 2
freshness: stale
duplicate_of: [[Kraken and Tempo partner on liquidity and custody for payment firms]]
---

# Kraken supports Tempo blockchain for USDT0 and USDC.e

> [!info] 2026-07-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Kraken supports the Tempo blockchain, enabling native deposits and withdrawals of USDT0 and USDC.e. The integration gives FinTechs, payment companies and stablecoin issuers access to Tempo's sub-second settlement and stablecoin-based transaction fees through Kraken's platform.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/222bf3e1>

## Контекст

<!-- enrichment:context -->
### [0] What happened (one-liner)
Kraken enabled native deposits and withdrawals of **USDT0** (omnichain USDT) and **USDC.e** (bridged USDC) on **Tempo**, the Stripe/Paradigm payments-first Layer 1 — going live ~2026-07-10, making Kraken the first major US exchange to natively support the chain. This is the retail/product go-live of the institutional partnership announced 2026-06-08.

### [1] Timeline (dated)
- **2025-09-04** — Stripe and Paradigm incubate Tempo, a payments-first L1 for stablecoins.
- **2025-11** — Klarna launches KlarnaUSD stablecoin on Tempo; Stripe-backed Tempo leads $25M Commonware raise (see [[Klarna launches KlarnaUSD stablecoin on Tempo blockchain]], [[Stripe-backed Tempo leads $25 million Commonware raise]]).
- **2026-03** — Tempo mainnet goes live (with AI-agent / Machine Payments Protocol); USDT0 integrates with Tempo (~23+ chains).
- **2026-06-03** — Kraken adds native **USDT0** support on Tempo; "first US exchange" claim (see [[Kraken adds native USDT0 support on Tempo for sub-second transfers]]).
- **2026-06-08** — Kraken + Tempo announce full institutional partnership (liquidity, custody, on/off-ramps, listings). Kraken named Tempo's **first US CEX partner**; blog states "USDT0 and **USDC.e** deposits and withdrawals are live on Kraken via Tempo" (see [[Kraken and Tempo partner on liquidity and custody for payment firms]]).
- **2026-07-10** — USDT0 **and USDC.e** funding via Tempo confirmed live on Kraken (this note; retrieved 2026-07-14).

### [2] What the pieces are
- **Tempo** — payments-first L1 incubated by Stripe + Paradigm; ~0.6s deterministic finality, no re-orgs, stablecoin-native fees (no separate gas token), dedicated payment lanes. Raised $500M Series A at ~$5B (Thrive, Greenoaks). Design partners: Visa, Mastercard, Deutsche Bank, Standard Chartered, Revolut, Nubank, Shopify, OpenAI, Anthropic.
- **USDT0** — LayerZero OFT (omnichain) representation of USDT; burn-on-source / mint-on-destination, 1:1 backed by USDT in an Ethereum lockbox. Trust path = Tether + LayerZero.
- **USDC.e** — bridged (wrapped) USDC, not issuer-native CCTP USDC; secondary-market liquidity/redeemability must be verified.
- **Kraken's support** = deposits/withdrawals (funding rail) only; on-app trading of USDT0/USDC.e is contingent on liquidity, and geographic restrictions apply.

### [3] Why it matters / competitive frame
Confirms Kraken as the institutional settlement venue anchoring Tempo's ecosystem (custody via Wyoming SPDI Kraken Financial, OTC, on/off-ramps, listings — "one relationship, not five vendors"). Part of the 2026 **stablechain arms race** for a combined ~$268B+ stablecoin float:
- **Tempo** (Stripe/Paradigm) — mainnet live Mar 2026.
- **Arc** (Circle/USDC) — public testnet; mainnet expected 2026 (see [[Circle launches Arc public testnet]]).
- **Plasma** (Tether/Bitfinex orbit) — mainnet live, EVM-compatible, Bitcoin-anchored.
- **Codex** — OP-stack L2 stablecoin rollup (Coinbase Ventures, Dragonfly), USDC gas, B2B focus.
Kraken's exclusive early CEX alignment with Tempo is a bet on the Stripe-backed chain in this race.

### [4] Open / to-watch
- Whether USDT0/USDC.e **trading** (not just funding) launches on Kraken — currently liquidity-dependent.
- Kraken's parallel neutrality: also lists tokenised GBP, HashKey tie-ups — not Tempo-exclusive as a business.
- Related prior context: [[Kraken files confidentially for US IPO at $20B]], [[Kraken raises $800M from Citadel and others]].

**Sources:** https://blog.kraken.com/product/new-features/usdt0-and-usdce-now-available-on-tempo · https://blog.kraken.com/product/360/kraken-and-tempo-partnership · https://tempo.xyz/ · https://www.paradigm.xyz/writing/tempo-payments-first-blockchain · https://cryptobriefing.com/kraken-usdc-tempo-network-support/ · https://across.to/blog/stablechains · https://eco.com/support/en/articles/14998914-usdt0-explained-layerzero-s-omnichain-usdt
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team

1. **Is this new vs June?** Largely NO. The 2026-06-08 Kraken partnership blog already stated "USDT0 and USDC.e deposits and withdrawals are **live** on Kraken via Tempo." The July 14 item is the confirmed retail go-live (~Jul 10) — an incremental restatement, not a new deal. **Duplicate of the June partnership note.**
2. **Two prior notes already cover this?** YES — [[Kraken adds native USDT0 support on Tempo for sub-second transfers]] (2026-06-03, USDT0) and [[Kraken and Tempo partner on liquidity and custody for payment firms]] (2026-06-08, full partnership + USDC.e). This note adds nothing material beyond a go-live date.
3. **Any genuinely new fact?** Marginal: USDC.e funding confirmed live 2026-07-10 as a discrete product ship (June note framed it as "live" tied to the partnership announcement). Not enough to be a standalone story.
4. **"First US exchange" — verified?** Yes, consistently claimed across Kraken blog, Crypto Briefing, Crypto Economy. But the claim was already made in June — reused, not new.
5. **Is trading available?** NO — deposits/withdrawals only; on-app trading is liquidity-contingent. Note's implication of broad "access" overstates; it's a funding rail.
6. **USDT0 counterparty/trust risk?** USDT0 = LayerZero OFT + Tether lockbox (two trust layers). USDC.e = bridged/wrapped, not native CCTP USDC — redeemability/liquidity caveats apply. Note glosses this.
7. **Is Kraken Tempo-exclusive?** No — Kraken is Tempo's first US CEX partner, but Kraken also supports many chains/stablecoins. Low strategic lock-in for Kraken.
8. **Volume/adoption metrics?** None disclosed (TVL, transfer volume, # users). No quantitative traction to assess.
9. **Regulatory wrapper solid?** Custody via Payward Financial (Wyoming SPDI / Kraken Financial) — credible; explicitly NOT FDIC-insured. Standard stablecoin de-peg disclaimer present.
10. **Competitive threat real?** Tempo competes with Circle Arc, Plasma, Codex, Stable for stablecoin float. Kraken/Tempo alignment is one data point in an unsettled arms race — outcome uncertain.
11. **Source quality?** Primary = Kraken blog + reposts (promotional, single-sourced press release). No independent/critical coverage. Marketing-grade.
12. **Ranker / freshness leakage?** This pick surfaced despite the underlying event being a ~5-week-old June partnership — a staleness signal.
13. **Any impact on Kraken IPO thesis?** Tangential; too small to move the $20B IPO narrative ([[Kraken files confidentially for US IPO at $20B]]).
14. **Would omitting this lose signal?** No — the June partnership note captures the substance. Digest can reference June coverage.

**Verdict: STALE — duplicate of the June Kraken/Tempo partnership.** Substance already captured 2026-06-08; only a go-live date is incremental.

**Importance: 2/5** — Incremental product go-live restating a known June partnership; single-sourced promo, no metrics, deposits/withdrawals only. Relevant to the Tempo stablechain race but not standalone-worthy.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Market research — Kraken × Tempo (USDT0 / USDC.e native support).** _Skeptical read; dated evidence; nothing invented._

**What actually happened (incremental).** This is the third data point in a rolling Kraken–Tempo integration, not a new deal:
- 2026-06-03 — Kraken becomes first U.S. exchange to natively support USDT0 deposits/withdrawals on Tempo (~0.6s finality, fees in stablecoins, no gas token). [note: "Kraken adds native USDT0 support on Tempo"; src tempo.xyz]
- 2026-06-08 — Broader Kraken–Tempo partnership: Tempo names Kraken its **first US centralized-exchange partner**, bundling liquidity/OTC, on/off-ramps, qualified custody, and listings "through one relationship." [note: "Kraken and Tempo partner…"; src blog.kraken.com]
- 2026-07-14 (this pick) — USDC.e added alongside USDT0; positioned as distribution rail for fintechs/PSPs/issuers building on Tempo.
Net: an extension of an existing partnership (adds USDC.e), not a standalone catalyst. Weight accordingly.

**Sector context.** Tempo is a payments-first Layer-1 incubated by **Stripe + Paradigm**, mainnet-live 2026-03-18, ~0.6s finality, stablecoin-denominated gas, targeting 100k+ TPS. Series A of **$500M at a ~$5B valuation** (Thrive, Greenoaks). Design partners named include Visa, Deutsche Bank, Shopify, Nubank, Revolut, Fifth Third, Howard Hughes. [WebSearch: tempo.xyz, Fortune 2026-04-21, CoinDesk 2026-03-18]. Kraken's role is **distribution/on-ramp** into that ecosystem — the value is being the credible US-regulated fiat/liquidity/custody gateway for Tempo-native flows, not owning the chain. USDT0 is Tether's omnichain USDT (redeemable 1:1 to underlying USDT); USDC.e is a bridged USDC representation — both are wrapped/bridged assets, which carries bridge/redemption-path risk vs. native issuance.

**Kraken IR grounding (PRIMARY — Payward reported figures).**
- **Q1 2026 (2026-05-18):** Adjusted Revenue **$507M (+3% YoY)** in a weak quarter (BTC −22%, crypto mcap −23%, industry spot vol −38%); Platform Transaction Volume **$357B**; spot market-share up from ~3.5% (mid-2025) to peak **5.2% (Mar 2026)**; Futures DARTs **+51% YoY**; funded accounts **6.1M**; platform assets **$40B**; Adjusted EBITDA down to **$18M** (compliance/product spend). [ir_latest: payward.com/press-release/q1-2026-financial-highlights]
- **Prior rounds:** $800M raise at **$20B valuation** (2025-11-18, incl. Citadel Securities $200M, Jane Street, DRW); earlier $500M at $15B (2025-09-26) — pre-IPO capital build. [ir_latest funding_announcement]
- Read-through: Kraken is scaling and diversifying (derivatives, tokenization) but Adj. EBITDA is thin ($18M) and still trading-volume-sensitive. A stablecoin-rails integration is strategically on-trend but immaterial to near-term revenue on its own.

**In-base comps / competitive set (grep on News/2026-06..07).**
- **Coinbase / Base** is the direct competitive threat: Base processed **~62% of global onchain stablecoin volume**; Coinbase holds >25% of USDC in circulation (~$19B). [WebSearch: CoinDesk] Kraken–Tempo is partly a counter to Coinbase's owned-chain distribution advantage.
- **Open USD (OUSD)** consortium (2026-06-30, 140+ firms incl. Visa, Mastercard, Stripe, Coinbase, BlackRock; deploys on Base/Solana) — note "Visa, Stripe, 140 firms launch Open USD stablecoin." Notably **Stripe backs both Tempo and OUSD**, muddying the "Stripe ecosystem" moat narrative.
- MiCA reshaping EU stablecoin access: "Revolut to delist USDT" (2026-07-07), "Tether exits EU market as MiCA blocks USDT" — direct headwind to a USDT0-centric rail in Europe.
- Adjacent monetisation thesis: "FinTech Futures — Stablecoins offer fintechs a monetisation model" (2026-07-13) supports the distribution/fee narrative Kraken is selling.

**Risk flags.**
1. **Incremental / low materiality** — extension of a June partnership (adds USDC.e); no disclosed volumes, revenue, or economics. Not a standalone catalyst.
2. **Distribution role, not moat** — Kraken is a gateway to Tempo, not the chain; value accrues largely to Tempo/Stripe. Coinbase's owned Base gives a rival a structurally deeper distribution position (~62% of onchain stablecoin volume).
3. **Regulatory / MiCA on USDT0** — USDT-linked exposure faces EU delisting pressure (Revolut, Tether EU exit); limits addressable market for a USDT0 rail in Europe.
4. **Bridged-asset risk** — USDT0 (omnichain) and USDC.e (bridged) are wrapped representations; redemption-path/bridge risk and 1:1 backing rely on issuer + bridge integrity.
5. **Ecosystem-alignment ambiguity** — Stripe simultaneously backs the rival Open USD consortium (with Coinbase/BlackRock), weakening the "Stripe-exclusive tailwind" read for Tempo.
6. **Earnings sensitivity** — Kraken Adj. EBITDA thin ($18M Q1'26) and volume-dependent; a rails feature won't move the P&L near-term.

**Bottom line:** Strategically coherent (Kraken as US-regulated on-ramp into the Stripe/Paradigm Tempo stablecoin ecosystem, a distribution counter to Coinbase/Base), and consistent with Kraken's pre-IPO diversification and $507M Q1'26 revenue base. But this specific item is an incremental add to an existing partnership with no disclosed economics, sits against a formidable Coinbase/Base and Open USD competitive backdrop, and carries MiCA/USDT and bridged-asset risks. Importance: low-to-moderate.

_Sources: ir_latest.json (payward.com Q1 2026; blog.kraken.com 2025-11 raise); in-base notes 2026-06-03/06-08, 07-07, 07-13; WebSearch payward.com, coindesk.com, fortune.com, tempo.xyz. IR db (pipeline/state/irdb) not on disk locally — figures via ir_latest.json + web._
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Kraken (Payward) — reported figures (IR-covered; company's own disclosures)**

Kraken/Payward is IPO-prep and discloses adjusted financials directly (no filings on disk locally; figures below are from Kraken's/Payward's own press releases).

**Q1 2026 (latest reported, disclosed 2026-05-18):**
- Adjusted revenue: **$507M, +3% YoY** — growth cooled sharply amid "industry-wide moderation in trading activity."
- Total platform transaction volume: **$357B** in Q1.
- Adjusted EBITDA: **$18M** (down materially vs. prior quarters; framed as a "conscious choice to keep investing through the cycle").
- Funded accounts: **6.1M, +47% YoY**.
- Assets on platform: **$40B** as of 2026-03-31, **+11% YoY** (~48% ex-price effects, i.e. net inflows).
- Source: [Payward Q1 2026 Financial Highlights](https://www.payward.com/press-release/q1-2026-financial-highlights)

**FY2025 (disclosed 2026-02-03):**
- Adjusted revenue: **$2.2B, +33% YoY**.
- Adjusted EBITDA: **$531M, +26% YoY**.
- Total platform transaction volume: **$2.0T, +34% YoY**.
- Assets on platform: **$48.2B, +11% YoY**.
- Funded accounts: **5.7M, +50% vs. 2024**.
- Revenue mix: ~47% trading-based / ~53% asset-based & other — a deliberate diversification away from pure trading fees.
- Q4 2025: **$625M** adjusted revenue, **$84M** adjusted EBITDA.
- Sources: [Kraken 2025 financials](https://blog.kraken.com/news/kraken-2025-financials), [Payward 2025 Financial Highlights](https://www.payward.com/press-release/2025-financial-highlights)

**Read-through to the Tempo / stablecoin-rails support**

- **Scale backdrop:** Kraken runs a $2T/yr volume, $2.2B-revenue platform with 6.1M funded accounts and ~$40B of assets — meaningful distribution for any stablecoin/settlement rail it plugs in. Adding native USDT0/USDC.e deposits/withdrawals on Tempo extends that reach to Tempo's sub-second, stablecoin-fee settlement.
- **Revenue-mix pivot supports the move:** the FY2025 shift to ~53% asset-based & other (non-trading) revenue is the strategic frame. With Q1 2026 revenue nearly flat (+3%) and EBITDA compressed to $18M as trading activity moderated, Kraken is leaning into non-trading, payments/stablecoin rails (Tempo integration, stablecoin transaction fees) to diversify the revenue base — consistent with management's "keep investing through the cycle" stance.
- **Thesis flags:** (1) Q1 2026 deceleration (+3% revenue, $18M EBITDA vs. $84M in Q4 2025) shows the trading-cycle sensitivity that stablecoin/payments rails are meant to offset — but Tempo support is a distribution/plumbing move, not yet a disclosed revenue line, so near-term financial impact is unquantified. (2) IPO-prep context: diversifying into stablecoin settlement strengthens the equity story ahead of a listing. (3) 47% funded-account growth signals user-base momentum even as per-user trading revenue softens.

_Note: Kraken is private/IPO-prep; all figures are company-reported adjusted metrics, not audited GAAP filings. No standalone financials are disclosed for the Tempo integration itself._
<!-- /enrichment:earnings_review -->
