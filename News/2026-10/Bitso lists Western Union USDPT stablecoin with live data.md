---
title: "Bitso lists Western Union USDPT stablecoin with live data"
date: 2026-10-15
retrieved: 2026-10-15
tags:
  - company/bitso
  - company/western-union
  - industry/stablecoins
  - region/latam
  - type/product
sources:
  - https://bitso.com/prices/usdpt
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s21c41804
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Bitso lists Western Union USDPT stablecoin with live data

> [!info] 2026-10-15 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌐 Bitso lists the Western Union USDPT Stablecoin with live price and chart data. The page also offers a USDPT calculator alongside the live chart. Bitso states its platform is not authorized to provide crypto services in Spain.

## Первоисточники

### bitso.com
<https://bitso.com/prices/usdpt>
*177 слов · direct*

Bitso
Western Union USDPT Stablecoin (USDPT) live price and calculator
Western Union USDPT Stablecoin statistics
#1175
5,916,998
46,373
5,922,444
1.3851
About Western Union USDPT Stablecoin
 USDPT is a GENIUS Act-compliant U.S. dollar stablecoin built on the Solana blockchain and issued by Anchorage Digital Bank, N.A., a federally regulated U.S... Read more 
USDPT calculator
Type an amount, check the price, and buy USDPT quickly.
*This calculator tool provides informative data of conversions between any of the crypto listed on Bitso and your preferred fiat currency. This calculator uses estimated rates from the Bitso exchange.
*Conditions of an effective conversion may vary from shown due to then-current market prices, volatility and/or other reasons. Fees and other conditions apply on conversions. To know more visit our fees or terms websites.
Crypto trends
Check some of the most popular assets on our platform.
pepe
PEPE
-0.00000015
pepe
-3.57 %
pepe
PEPE
-0.00000015
PEPE
-3.57 %
ada
Cardano
-0.0101
ada
-4.25 %
ada
Cardano
-0.0101
ADA
-4.25 %
link
ChainLink Token
-0.6028
link
-4.66 %
link
ChainLink Token
-0.6028
LINK
-4.66 %

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Bitso lists Western Union USDPT stablecoin with live data
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS VERDICT: FRESH (but thin).** This is a genuinely new event — the *first exchange listing of USDPT in a LatAm retail market (Mexico)* with a direct MXN⇄USDPT route and a Bitso Business agent-conversion channel — announced ~13 Oct 2026. It is NOT a re-run of the issuance story ([[Western Union launches USDPT stablecoin with Fireblocks]], May 2026) nor of the first-exchange-integration story ([[Bybit first major exchange to integrate Western Union's USDPT stablecoin]], Jun 2026). However, the *source we actually captured* is only Bitso's `bitso.com/prices/usdpt` price/calculator page — a data-listing artefact, not the announcement — so the note frame ("lists … with live data") understates the real event (a Mexico retail + agent on/off-ramp). Fresh, but the item is low-weight: a single-corridor distribution step for a sub-$20M stablecoin.

## [0] What exactly happened (de-PR'd)
- **De-PR'd fact:** Bitso added Western Union's **USDPT** (USD Payment Token) to its app for **Mexico** users (~13 Oct 2026). Two mechanisms: (1) **retail** — eligible MX users buy/sell USDPT **directly against MXN** (no USD leg); (2) **Bitso Business** — Western Union **agents** can convert USDPT ⇄ other supported currencies, i.e. a local **off-ramp / liquidity** point for payout shops. The captured page is just the live price/calculator widget (price ~1.00 vs the "1.3851" and "#1175" figures on the scraped page, which are page-scrape artefacts/other fields, not a depeg — treat as noise).
- **USDPT itself** (from [[Western Union launches USDPT stablecoin with Fireblocks]]): GENIUS-Act-compliant USD stablecoin, **Solana**, issued by **Anchorage Digital Bank, N.A.** (OCC-chartered), wallet/ops via **Fireblocks**; launched May 2026 live in **Philippines + Bolivia**, consumer-facing "Stable by Western Union" planned across 40+ countries through 2026.
- **Why structured this way:** WU built USDPT primarily as an **internal settlement rail** (replace correspondent-bank/SWIFT batch settlement with 24/7 on-chain settlement across its ~500k-agent network — see [[Western Union plans USDPT stablecoin on Solana]]). A listing on **Bitso** — the dominant US–Mexico remittance crypto rail — is the logical **distribution** step: it gives USDPT a real retail on/off-ramp and MXN liquidity exactly where WU's biggest corridor is. The "Bitso states its platform is not authorized to provide crypto services in Spain" line is a generic Bitso compliance disclaimer, not USDPT-specific.
- **Second-order read:** the *agent* conversion channel (Bitso Business) matters more than retail buy/sell — it's the piece that lets USDPT actually clear last-mile cash payout in MXN, which is what a stablecoin remittance rail needs to be useful rather than ornamental.

## [1] Competitors / peers
- **MoneyGram MGUSD** (Jun 2026): dollar-pegged stablecoin via **Stripe-owned Bridge** on **Stellar** (smart contracts M0, security Fireblocks), live **in the MoneyGram app** across ~500k locations — a near-identical "legacy remittance brand issues own stablecoin" play, but MGUSD is distributed **in-house** rather than via a third-party exchange. (See [[MoneyGram becomes Solana validator, expands blockchain strategy]].)
- **Circle USDC:** ~$72.7B market cap (Oct 2026) vs USDPT's ~$17–18M — USDPT is **~4,000x smaller**; USDC is the incumbent dollar unit most LatAm crypto remittance already uses (e.g. [[RedotPay adds crypto-to-MXN payouts via Circle in Mexico]], [[MAJORITY launches Latin America stablecoin transfers with Privy]]).
- **Bitso's own book:** Bitso already runs **MXNB** (peso stablecoin via subsidiary **Juno**, on Arbitrum, SPEI-integrated) and settles with **Ripple RLUSD/XRP** ([[Ripple and Bitso expand stablecoin settlement in Latin America]], [[Bitso uses Ripple RLUSD and XRP for US-LatAm settlements]]) and **USDT on Solana** ([[Bitso integrates USDT on Solana for Latin America]]). So USDPT is **one more SKU** on a shelf that already holds the peso-native and the enterprise-USD options.
- **Position: catching-up / parity at best.** USDPT is a late, tiny entrant; its only edge is being WU's *captive* settlement token. The listing is parity-with-Bybit plus a first LatAm-retail foothold.
- **Why the lay of the land is this way:** remittance incumbents (WU, MoneyGram) are issuing proprietary stablecoins to (a) cut correspondent-bank settlement cost/float and (b) avoid ceding the "digital dollar" layer to Circle/Tether. But distribution, not issuance, is the bottleneck — hence needing Bitso/Bybit. The second-order risk: by routing through an exchange that also sells USDC/USDT/MXNB, WU gives users a shelf where USDPT has **no reason to win** on its own merits.

## [2] Company history / fit
- **Bitso** is the LatAm crypto/remittance super-app: claims it now moves **~14.7–15% of US→Mexico remittances** (2026), processed **~$6.5B to Mexico in 2024**; Bitso Business crossed **~$80B annualized TPV** (2025), largest stablecoin payments platform in the region. History: MXNB/Juno launch (2025), MXNB El Salvador issuance approval ([[Bitso gains El Salvador approval to issue MXNB stablecoin]]), SPEI-for-business, fractional shares/ETFs, CIBanco brokerage bid.
- **Western Union** trajectory: 2025 "crypto arms race" entry ([[Western Union plans USDPT stablecoin on Solana]]) → Fireblocks/Anchorage launch May 2026 → Bybit integration Jun 2026 → now Bitso/Mexico. In parallel WU is consolidating physical remittance (Intermex/Dash/Lanapay/GMT acquisitions — see [[Western Union-Intermex deal faces new 30-day antitrust wait]]).
- **Why they act this way:** Bitso wants to be the **neutral liquidity layer** for every stablecoin flowing through the US–Mexico corridor — listing USDPT (even a rival-ish WU token) grows its rail-toll business regardless of which coin wins. WU, a commodity take-rate remittance firm under margin pressure, needs on-chain settlement to defend economics and a software/network story for investors (cf. Forbes: "Western Union's stablecoin automates the end of its own margin"). The structural logic: WU must disintermediate its own correspondent-bank costs *before* a pure-crypto rail disintermediates WU.

## [3] Novelty / value-add / traction
- **What's genuinely new:** first **retail MXN⇄USDPT** route and first **LatAm agent off-ramp** for USDPT — i.e. the first time USDPT touches the US–Mexico corridor, WU's single most important market, through a major local exchange.
- **Traction (hard numbers, skeptical):** USDPT supply **~17.8M tokens across ~326 wallets** (14 Oct 2026); market cap **~$17M**; 30-day transfer volume **~$114.9M** (per RWA.xyz, as of 13 Oct). That 30-day volume >> market cap suggests the token is **circulating as a settlement/working-capital instrument** (mint→settle→burn), consistent with WU's internal-rails design, not sitting as retail savings. But 326 wallets = essentially **no retail adoption**; this is plumbing, not a consumer product yet.
- **Why the value-add is thin:** on Bitso's shelf USDPT competes with USDC, USDT-on-Solana, MXNB and RLUSD — all deeper, more liquid, and already corridor-integrated. USDPT's only durable edge is **WU-captive volume** (agent settlement). **Who captures the margin:** the issuer (Anchorage) earns reserve yield; Bitso earns the spread/conversion toll; WU saves correspondent-bank float. The consumer sees little reason to hold USDPT over USDC. So the listing adds a distribution node but **not a reason-to-win** — value accrues to the rail (Bitso) and the float-saver (WU), not to the token's competitive position.

## [4] What's next / market sentiment
- **Plans:** WU's "Stable by Western Union" consumer app across 40+ countries through 2026; more exchange listings/corridors likely (Bybit → Bitso pattern). Expect additional LatAm corridors (Bolivia already live on the issuance side).
- **Sentiment:** analysts frame USDPT as potentially reshaping WU's **settlement cost base** (CoinDesk, May 2026) while cautioning it also **compresses WU's own transfer margin** (Forbes). Equity view is mixed — upside is cost/float, downside is self-cannibalization.
- **Regulatory backdrop:** GENIUS Act gives USDPT a compliant US framework; Mexico's Ley Fintech + SPEI integration make the corridor workable; Bitso's Spain disclaimer flags EU MiCA perimeter limits.
- **Risks / counterintuitive second-order:** the bigger WU's own stablecoin succeeds at 24/7 settlement, the faster it **erodes the FX spread and float income** that fund the agent network — success could hollow the very distribution it depends on. And by distributing via multi-coin exchanges, WU trains its corridor to treat "digital dollar" as fungible, which favors the liquid incumbent (USDC/USDT), not USDPT. Net: a sensible distribution step, but low standalone weight.

## Sources
- Internal: [[Western Union launches USDPT stablecoin with Fireblocks]]; [[Western Union plans USDPT stablecoin on Solana]]; [[Bybit first major exchange to integrate Western Union's USDPT stablecoin]]; [[Ripple and Bitso expand stablecoin settlement in Latin America]]; [[Bitso uses Ripple RLUSD and XRP for US-LatAm settlements]]; [[Bitso integrates USDT on Solana for Latin America]]; [[Bitso gains El Salvador approval to issue MXNB stablecoin]]; [[MoneyGram becomes Solana validator, expands blockchain strategy]]; [[RedotPay adds crypto-to-MXN payouts via Circle in Mexico]]; [[Western Union-Intermex deal faces new 30-day antitrust wait]]
- External:
  - https://bitso.com/prices/usdpt (primary — live data page)
  - https://cryptobriefing.com/bitso-lists-western-union-usdpt-stablecoin-mexico/
  - https://solanacompass.com/news/bitso-lists-western-unions-solana-stablecoin-usdpt-in-mexico
  - https://coinfomania.com/bitso-lists-western-unions-usdpt-stablecoin-in-mexico/
  - https://app.rwa.xyz/assets/USDPT (supply/wallets/volume)
  - https://www.coingecko.com/en/coins/usdpt-western-union
  - https://www.coindesk.com/business/2026/05/05/western-union-s-solana-based-stablecoin-could-reshape-its-payment-model-analyst-says
  - https://www.forbes.com/sites/digital-assets/2026/05/29/western-unions-stablecoin-automates-the-end-of-its-own-margin/
  - https://www.prnewswire.com/news-releases/moneygram-launches-mgusd-a-stablecoin-to-power-its-own-global-network-302787799.html
  - https://www.coingecko.com (USDC market cap reference) / https://messari.io/project/circle-usdc
  - https://www.coindesk.com/business/2025/03/26/crypto-exchange-bitso-launches-stablecoin-business-eyeing-latam-cross-border-payments (Juno/MXNB)
  - https://www.prnewswire.com/news-releases/bitso-processes-15-of-usmexico-remittances-302897489.html
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Top challenge / red-team questions (second-order). Importance: 2/5 — a genuinely new but low-weight distribution step: first retail MXN⇄USDPT route + first LatAm agent off-ramp for USDPT, but on a ~$17M, ~326-wallet token with essentially no retail adoption, listed on a shelf where USDC/USDT/MXNB already win. Fresh, not a dup of the May launch or Jun Bybit integration.**

1. **Is it really new?** Yes — first USDPT retail listing in Mexico (~13 Oct 2026) with a direct MXN route; distinct from issuance (May, Fireblocks/Anchorage) and Bybit integration (Jun). *Not* a reprint. (answered)
2. **Announced or live?** Live — the `bitso.com/prices/usdpt` page shows an active price/calculator; cryptobriefing confirms buy/sell + Bitso Business agent conversion are available. (answered)
3. **What's the real traction?** ~17.8M supply, ~326 wallets (14 Oct), ~$17M mcap, ~$114.9M 30-day volume (RWA.xyz). Volume >> mcap ⇒ settlement churn, not holdings. 326 wallets ⇒ ~zero retail. (answered)
4. **Does the Bitso retail route actually drive remittances, or is it a vanity listing?** Likely mostly vanity for *retail* today; the load-bearing piece is the **agent off-ramp** via Bitso Business. (open — no agent-usage numbers disclosed)
5. **Why would a Mexican user pick USDPT over USDC/USDT/MXNB on the same app?** No stated reason — no lower fee, deeper liquidity, or unique utility disclosed. USDPT's only edge is WU-captive settlement, invisible to retail. (answered: no reason-to-win)
6. **Who captures the margin?** Anchorage (reserve yield), Bitso (conversion spread/toll), WU (correspondent-bank float savings). Token holder captures ~nothing. (answered)
7. **Does this cannibalize WU's own transfer margin?** Plausibly yes over time (Forbes thesis); 24/7 on-chain settlement erodes FX spread/float that funds the agent network. (open — depends on rollout scale)
8. **Is the "1.3851 / #1175" on the scraped page a depeg?** No — treat as page-scrape noise/other field; USDPT is USD-pegged ~1.00 per CoinGecko/RWA.xyz. (answered)
9. **How does this compare to MoneyGram MGUSD?** MGUSD (Stripe/Bridge, Stellar) is distributed *in-app*; USDPT leans on third-party exchanges (Bybit, Bitso). WU's model is more open but cedes the shelf. (answered)
10. **Does Bitso listing a quasi-rival token signal anything?** Yes — Bitso is positioning as neutral corridor liquidity layer; it tolls every coin, so listing USDPT grows its rail business regardless of coin winner. (answered)
11. **What's the Spain disclaimer about?** Generic Bitso MiCA/EU-perimeter compliance notice, not USDPT-specific; irrelevant to the Mexico event. (answered)
12. **Is USDPT GENIUS-Act-compliant and who holds reserves?** Yes — Anchorage Digital Bank, N.A. (OCC-chartered) issues/custodies; fully USD-backed. (answered)
13. **Could Bitso's MXNB make USDPT redundant in-corridor?** For US→MX, MXNB (peso-native, SPEI) + USDC often beat a thin USD token; USDPT's role is narrow (WU agent settlement). (open — depends whether WU routes real volume through Bitso)
14. **What would move importance up?** Disclosed WU agent-conversion volume via Bitso, a fee/UX advantage, or multi-corridor retail expansion — none present yet. (answered)
15. **Downside trigger?** USDPT stays sub-$20M plumbing while USDC/USDT absorb LatAm retail dollar demand ⇒ listing is a checkbox, not a channel. (open)
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** LatAm stablecoin remittance rails. Size: Mexico is the ~$42.8bn remittance market, #4 globally; the US–Mexico corridor was ~$61.8bn in 2025, down ~4.5% YoY (per secondary citations via cointelegraph/cryptoninjas, as of 2026). Mexico stablecoin cross-border activity quadrupled since early-2024 to ~$1.8bn/month by Jun-2026; Q2-2026 stablecoin service inflows ~$8.4bn (secondary, chainalysis-cited). Drivers / "why now": (1) GENIUS Act gives US-regulated issuance a legal frame — USDPT is issued by Anchorage Digital Bank N.A., a federally regulated bank (per note's own source text), which is what lets an incumbent like Western Union put a dollar token on retail rails; (2) incumbent money-transfer firms are being disintermediated by on-chain settlement and are now issuing their own tokens to keep the float/economics in-house (WU USDPT on Solana, MoneyGram MGUSD on Stellar). Structure: fragmented at the wallet/exchange layer, consolidating at the issuance layer — value is migrating to whoever controls (a) the regulated issuer + reserve float and (b) distribution. Barriers: licensing per jurisdiction, banking/reserve relationships, and liquidity/network effects.

**Competitive landscape.** Sector KPIs: TPV/settlement volume, float/reserve AUM (interest income), take rate on FX conversion, and active users / listed-asset liquidity. This news is Bitso the *venue* listing someone else's token — Bitso earns on buy/sell spread + FX, not on USDPT issuance economics (those accrue to WU/Anchorage). Key players & basis of competition: issuers (Circle USDC, Tether USDT, WU USDPT, MoneyGram MGUSD) compete on distribution + regulatory standing + chain; venues/rails (Bitso, Bybit, Ripple) compete on liquidity and corridor reach. Recent dated moves: WU launched USDPT on Solana ~May-2026 via Fireblocks/Anchorage (Bolivia + Philippines first, 40+ countries planned); Bybit integrated USDPT Jun-2026; MoneyGram launched MGUSD on Stellar via Bridge Jun-2026 (60m customers); Ripple–Bitso expanded MXNB/RLUSD enterprise settlement on the US–Mexico corridor Jun-2026 ([[Ripple and Bitso expand stablecoin settlement in Latin America]]). Bitso's position: *ahead* as the dominant LatAm distribution venue — >10m retail users and >2,000 institutional clients (per Bitso IR, "9 Million Users" PR Jan-2025 + later disclosures); Bitso Business surpassed **$80bn annualized stablecoin TPV** by end-2025 ([[Bitso Business Becomes Latin America's First Stablecoin Payments Platform to Surpass $80 Billion in Annual TPV]], Bitso PR 2025-12-18, https://www.prnewswire.com/news-releases/bitso-business-becomes-latin-americas-first-stablecoin-payments-platform-to-surpass-80-billion-in-annual-tpv-302646241.html — PRIMARY IR). Moat: regulated multi-country LatAm licensing + corridor liquidity + its own MXNB peso stablecoin (switching costs / network effects) `(analysis)`.

**Comps & multiples.** Bitso is private → last disclosed valuation ~$2.2bn (Series C 2021, Tiger/Coatue; secondary via dealroom/tracxn), i.e. a *round* valuation, not current market cap; 2026 revenue reported ~$305m (secondary, unverified) → implied ~7.2x P/S = $2,200m / $305m `(analysis, both numbers single-source → treat as indicative only)`. External public comp — **Circle (CRCL):** mkt cap ~$20bn, LTM revenue ~$2.9bn → EV/Revenue ≈ $20bn / $2.9bn ≈ **6.9x** (multiples.vc cites 6.4x on a tighter EV); EV/EBITDA ~27.9x; USDC ~$75bn supply, ~24% share (as of mid/Sep-2026, secondary). Comparability caveat: Circle is an *issuer* (float/interest-income model), Bitso is primarily a *venue/payments* operator — different economics, so the Circle multiple is context not a direct comp. MoneyGram / WU are the closest *strategic* comps (incumbents issuing tokens) but no clean public token-level multiple → "no data". Distribution not computed (<3 comparable figures); qualitative only. In-line/rich flag: Circle's ~6.9x EV/Rev sits mid-range for the sector but has compressed hard (reportedly down ~67% from peak) — the re-rate is the story, not the level.

**Risk flags.**
1. **Disintermediation of Bitso's own economics** — on USDPT, issuance float + reserve interest accrue to WU/Anchorage; Bitso captures only spread/FX. If incumbents push users to self-custodial issuer wallets (WU "Stablecard", MoneyGram app wallet), the venue layer risks being squeezed to a thin-margin on-ramp.
2. **Regulatory / jurisdiction fragmentation** — the note's source explicitly states Bitso is *not authorized to provide crypto services in Spain*; per-country licensing gaps cap the cross-border network effect and add compliance drag.
3. **Concentration on US–Mexico corridor + remittance cyclicality** — the headline corridor was *down ~4.5% YoY* in 2025; volume tied to one declining corridor plus migration/policy risk is a demand-side exposure.

**What this changes (idea-lens).** `(analysis)` This is incremental, not a re-rating: a venue listing a token already live since May-2026. The real signal is incumbents (WU, MoneyGram) choosing *distribution partners* (Bitso, Bybit) rather than building wallets alone — pointing to a two-sided market where regulated LatAm venues like Bitso become default on/off-ramps for incumbent tokens. Falsifiable thesis: if USDPT gains real retail traction, it shows up as rising Bitso Business TPV above the $80bn-2025 base in the next IR update. Trigger to watch: USDPT on-chain volume / Bitso TPV disclosures. Thesis breaks if WU routes users to its own wallet and USDPT liquidity on Bitso stays thin.

Sources: https://bitso.com/prices/usdpt · https://www.prnewswire.com/news-releases/bitso-business-becomes-latin-americas-first-stablecoin-payments-platform-to-surpass-80-billion-in-annual-tpv-302646241.html · https://www.crowdfundinsider.com/2025/01/234785-latam-based-bitso-retail-division-surpasses-9-million-users/ · https://cryptobriefing.com/bitso-lists-western-union-usdpt-stablecoin-mexico/ · https://multiples.vc/public-comps/circle-valuation-multiples · https://cointelegraph.com/news/moneygram-mgusd-stablecoin-remittance-onchain-rails · https://www.cryptoninjas.net/news/stablecoin-boom-hits-174b-latam-flows-as-fintechs-miss-112b-hidden-corridors/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No formal earnings — private company.** Bitso is privately held (last priced at a ~$2.2bn valuation in its 2021 Series C) and does not report formal earnings — no revenue, margin, EPS or audited income statement is disclosed. What follows reviews the operating metrics Bitso does publish (TPV, users, stablecoin flows) with growth, plus funding/valuation context. No P&L exists, so beat/miss is N/A.

**Disclosed operating metrics (with growth).**
- **Bitso Business TPV:** crossed **$80bn+ annual TPV** (first LatAm stablecoin payments platform to do so; Dec-2025 release), and is cited as on track to reach **~$82bn annualized TPV**. Mexico local real-time rails enabled transactions reaching **$15.6bn annualized volume**.
- **Stablecoin TPV (B2B):** **+81% YoY** in H1 2026 for Bitso Business B2B clients (second edition Stablecoin Landscape Report, presented at Stablecoin Conference 2026, Jun-2026).
- **Institutional base:** **over 1,900 institutional clients** in H1 2026; **>60% of new clients onboarded in 2026 were banks/financial institutions** — a mix shift toward regulated TradFi counterparties.
- **Retail users:** **9mn retail users** (Jan-2025 milestone, +12% YoY, ~3x in three years); total registered users reported "almost 10mn" by 2025. Mexico = **>70%** of the 9mn base. Fastest-growing markets by transaction volume: Argentina (~4x), Mexico (+80%+), Colombia (+70%), Brazil (+44%).
- **Market context:** stablecoins became the most-purchased digital asset class in LatAm, **40% of all digital-asset acquisitions**, surpassing Bitcoin for the first time — the tailwind behind Bitso's B2B TPV growth and directly relevant to the USDPT listing in this note.

**Funding / valuation history.** Series C of **$250mn (May-2021)** made Bitso LatAm's first crypto unicorn; **~$2.2bn** valuation; cumulative funding reported at **~$331mn** across ~8 rounds (investors incl. QED, Tiger Global, Ripple). No new priced round or valuation update disclosed in 2026 — the $2.2bn mark is stale (2021) and predates the B2B/stablecoin scale-up; current fair value is **[UNSOURCED]**.

**Thesis-flags.**
1. **B2B is the growth engine, not retail.** TPV scaling to ~$82bn with +81% YoY stablecoin B2B growth shows the center of gravity has moved from the 9mn retail app to institutional stablecoin payment rails — exactly the surface where listing Western Union's USDPT adds inventory. Second-order: revenue quality likely shifting from volatile retail trading fees toward payment/FX spread on flow (direction only; economics undisclosed → **no data**).
2. **Mix shift to banks (>60% of new clients).** De-risks the client base and validates the "hybrid finance" pitch, but concentrates Bitso in a regulated, compliance-heavy segment where margins and counterparty terms are undisclosed — and the note itself flags Bitso "is not authorized to provide crypto services in Spain," a reminder that regulatory perimeter is a live constraint.
3. **No P&L visibility = valuation risk.** All disclosure is volume/user vanity-adjacent; no profitability, take-rate or burn is public. A 2021-vintage $2.2bn mark against a materially larger 2026 business could be stale in either direction; absent a new round, any valuation claim is a hypothesis **(analysis)**.
4. **Transparency is selective (de-PR).** Bitso publishes TPV, user counts and landscape-report flow data generously but stays silent on revenue, margins, net flows and unit economics — standard for a private company, but it means these metrics cannot be stress-tested against a bottom line.

Sources: https://www.prnewswire.com/news-releases/bitso-business-becomes-latin-americas-first-stablecoin-payments-platform-to-surpass-80-billion-in-annual-tpv-302646241.html · https://www.crowdfundinsider.com/2026/06/285824-bitso-reports-stablecoin-usage-volume-up-by-81/ · https://www.coindesk.com/press-release/2026/06/23/bitso-unveils-the-hybrid-finance-era-as-stablecoins-reshape-global-payments · https://www.crowdfundinsider.com/2025/01/234785-latam-based-bitso-retail-division-surpasses-9-million-users/ · https://teampcn.com/crypto-exchange-bitso-hits-2-2bn-valuation/ · valuation/funding history: $2.2bn / ~$331mn / Series C $250mn 2021 · current fair value [UNSOURCED]
<!-- /enrichment:earnings_review -->
