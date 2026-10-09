---
title: "Ledger launches Bitcoin-backed Crypto Loan at TOKEN2049"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - company/ledger
  - industry/crypto
  - industry/lending
  - region/asia
  - type/product
sources:
  - https://decrypt.co/380224/ledger-bitcoin-loans-holders-borrow-without-selling
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s52d0ffe6
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Ledger launches Bitcoin-backed Crypto Loan at TOKEN2049

> [!info] 2026-10-08 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇸🇬 Ledger launches Bitcoin loans, letting holders borrow without selling their coins. Unveiled at TOKEN2049 in Singapore, Crypto Loan lets eligible users pledge cbBTC or wBTC as collateral to borrow USDC or USDT. Morpho powers the feature via Yield.xyz, and key actions are approved on the user's Ledger device.

## Первоисточники

### decrypt.co
<https://decrypt.co/380224/ledger-bitcoin-loans-holders-borrow-without-selling>
*413 слов · direct*

In brief
Ledger launched Crypto Loan, a self-custodial feature in its wallet app letting eligible users pledge wrapped Bitcoin to borrow USDC or USDT..
Powered by Morpho via Yield.xyz, it pairs with a new direct-access integration letting Ledger devices connect to Morpho without browser extensions.
The move deepens Ledger's push into financial services, joining a Bitcoin-lending wave from Coinbase and JPMorgan.
Ledger is giving Bitcoin holders a way to tap cash without parting with their coins, launching a self-custodial lending feature inside its wallet app that keeps final approval on the user's hardware device.
Unveiled Wednesday at the TOKEN2049 conference in Singapore, the new Crypto Loan feature lets eligible users pledge wrapped Bitcoin, in the form of cbBTC or wBTC, as collateral to borrow the stablecoins USDC or USDT.
The pitch is access to liquidity without moving funds onto a centralized lending platform or selling the underlying asset. Users can open and manage loans directly in Ledger Wallet, track their loan-to-value ratio, add collateral, repay or borrow more, with key actions physically approved on a Ledger signer before they execute.
The feature is powered by Morpho, the decentralized credit network, through technical provider Yield.xyz. It’s the same provider Coinbase relies on for its own Bitcoin-backed loans.
Ledger separately announced direct access for its signers to Morpho, letting users connect their hardware device to the protocol without routing through browser extensions or software wallets. Morpho co-founder Paul Frambot said the integration creates "a powerful liquidity flywheel," with stablecoins deposited through Ledger's existing Earn product able to fund the very loans Bitcoin holders now take out.
The move pushes Ledger, best known for its hardware wallets, deeper into financial services, and lands it in a fast-growing corner of crypto.
 Coinbase recently rolled out fixed-rate Bitcoin-backed loans after expanding the product to U.K. users, while JPMorgan has explored lending against Bitcoin and Ethereum.
The appeal is consistent across them: holders who expect their crypto to appreciate can borrow against it rather than trigger a taxable sale. The risk is equally familiar, since a sharp price drop can force liquidation of the collateral.
Ledger, which says it secures nearly 30% of all Bitcoin held by retail investors, also used the Singapore stage to unveil a limited-edition Nano Gen5 signer made with the NBA's San Antonio Spurs, a 250-unit run that extends a marketing deal with the Spurs announced last year.
Crypto Loan begins rolling out to eligible users immediately, with availability expanding over time.
Daily Debrief Newsletter

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ledger launches Bitcoin-backed Crypto Loan at TOKEN2049
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS: FRESH.** This is Ledger's OWN product launch (announced Wed 7 Oct 2026 at TOKEN2049 Singapore), the first Ledger lending note in the corpus — no prior Ledger loan note exists (grep over `company/ledger` returns only breach/IPO/CFO items). It is NOT a re-run. BUT the UNDERLYING rail is heavily precedented: it is the same Morpho-via-Yield.xyz stack Coinbase has run since Jan 2025 — see [[Coinbase's Bitcoin-backed loans surpass $1 billion]]. So: fresh event, incremental substance.

## [0] What exactly happened (de-PR'd)
Ledger added a **self-custodial borrow feature inside Ledger Wallet** (ex–"Ledger Live"). You pledge **wrapped BTC (cbBTC or wBTC)** into **Morpho** lending markets and borrow **USDC or USDT**. The novelty is UX/custody, not credit: the Ledger hardware signer connects **directly to Morpho** (no browser extension / software wallet), and every action — open, add collateral, repay, borrow more — is **physically approved on the device**. Collateral lives in Morpho's on-chain smart contracts; **Ledger neither lends nor custodies** — it is a signing front-end.
- Rail = **Morpho** (decentralized credit network); integration/tx-construction/LTV-tracking = **Yield.xyz** — *the exact provider Coinbase uses*. Ledger is, functionally, a self-custody skin on infrastructure a CEX already productized ~20 months earlier.
- → **Why structured this way:** Ledger has no balance sheet and no lending licence, and its whole brand is "not your keys / not on an exchange." Building on Morpho lets it ship a loan product with zero credit risk, zero custody, zero licensing — the only thing Ledger owns is the hardware-approval UX. The press frame ("Ledger launches Bitcoin loans") overstates Ledger's role: Morpho launches the loan, Ledger launches the button.
- **Terms (CAUTION — mostly secondary-sourced):** default LTV ~50%, liquidation threshold ~86%, ~1% fee on borrowed amount, **variable** rate (set by each isolated Morpho market's utilization). These figures come from secondary outlets (coinlaw.io); **Ledger's own blog does not publish LTV/fee** — treat as unconfirmed. Markets are four isolated Morpho markets **on Ethereum** (Coinbase's equivalent runs on **Base** — note the chain difference).
- **Status: announced + rolling out to "eligible users," country-gated — NOT globally live; jurisdictions undisclosed.**

## [1] Competitors / peers
Ledger lands into a crowded 2025–26 BTC-backed-lending wave:
- **Coinbase** — BTC→USDC via Morpho on Base since **Jan 2025**; **$1.4B active loans / ~$3B collateral** by Sep 2026; added **fixed-rate** loans (Morpho Midnight, up to $5M) + UK in Sep 2026. See [[Coinbase's Bitcoin-backed loans surpass $1 billion]]. **Same Morpho/Yield.xyz backend as Ledger.**
- **Kraken** — Flexline crypto-backed loans, 10–25% APR, also Morpho-powered — [[Kraken launches Flexline crypto-backed loans at 10-25% APR]].
- **Nexo** — CeFi credit lines; 0%-APR promo — [[Nexo unveils zero-interest credit at 0% APR]].
- **Sygnum** (Swiss bank) BTC-backed loans — [[Swiss bank Sygnum launches bitcoin-backed loan platform]]; **Xapo Bank** (custodial, up to $1M, Mar 2025); **JPMorgan** institutional BTC/ETH collateral (~Mar 2026); **Ledn** ($1.4B originated 2025, $188M ABS rated S&P BBB Feb 2026); **Aave** (DeFi money market, TVL ~$40B peak).
- **Position: catching up, differentiated on custody.** Ledger is the *only* offering that is self-custody + hardware-signed end-to-end; everyone else is custodial (Coinbase/Nexo/Xapo) or third-party-custody (JPMorgan). → **Why this matters (analysis):** in CeFi lending the lender captures the spread and bears rehypothecation risk; in Ledger's model the *protocol* (Morpho) and stablecoin suppliers capture the yield, and the borrower eats raw DeFi liquidation + variable-rate risk with **no CeFi backstop**. Ledger's differentiator is real but narrow — it trades convenience/rate-certainty for sovereignty.

## [2] Company history / fit
Fits Ledger's multi-year pivot from hardware to **financial services inside the wallet**: Stablecoin Yield / "Ledger Earn" (live May 2025 via Kiln, routing into Aave/Compound/Morpho), the **Ledger Live → Ledger Wallet rebrand (Jun 2026)**, and the stalled US listing — [[Ledger puts $4 billion US IPO plans on hold]] (also [[Ledger names John Andrews CFO, opens NYC office for US expansion]]). → **Why Ledger acts this way:** hardware is a one-time, saturating, commoditizing sale; to justify a >$4B valuation Ledger needs recurring software/financial-services revenue (fees on Earn + the new ~1% loan fee). Loan + Earn are two sides of one stablecoin flywheel (Frambot's quote): Earn suppliers' stablecoins fund Loan borrowers — both inside Ledger's app, both fee-bearing. The product exists to turn an installed hardware base into an annuity.

## [3] Novelty / value-add / traction
**Novelty is modest.** The credit product is not new — it is Coinbase's Jan-2025 rail with a self-custody front-end bolted on ~20 months later. The genuine delta: keys never leave the Secure Element, collateral is on-chain (not on anyone's balance sheet), and the device signs directly to Morpho without an intermediary wallet. → **Who captures the margin:** Morpho/Yield.xyz own the rail and most of the economics; Ledger clips a thin (~1%, unconfirmed) borrow fee and the Earn-side yield spread. The "liquidity flywheel" is mechanically plausible but **unverified** — Morpho pools are protocol-wide, not necessarily Ledger-internal, so the claim that Earn deposits specifically fund Ledger loans is marketing until shown. **Traction: NONE disclosed** — no Ledger loan volume or TVL; only the announcement + a staged rollout. Ledger's "secures ~30% of retail BTC / 8M signers" is self-reported and unverified (and don't conflate with Ledn's separate ~30%-of-consumer-lending claim).

## [4] What's next / market sentiment
Expect broader country rollout, more collateral/stablecoin pairs, and tighter Earn↔Loan coupling. Backdrop: crypto-backed lending reached ~$73.6B outstanding in Q3 2025; the sector is the hot post-ETF crypto-credit theme, with CeFi (Coinbase, Nexo, Ledn) and TradFi (JPMorgan, Cantor) both entering. → **Second-order (analysis):** the real test is conversion, not novelty. Ledger owns distribution (large installed base) but the hardware-signing friction that is its differentiator is also a UX tax vs Coinbase's one-tap custodial loan. If variable rates + on-chain liquidation prove too sharp for retail (a 2025-style drawdown forces cascading liquidations on self-custody users with no human support desk), the self-custody pitch could backfire reputationally. The central question is not "is BTC lending real" (it is) but "can a hardware vendor out-convert a CEX on its own rail when it gives up rate certainty and a safety net?"

## Sources
- decrypt.co — Ledger Bitcoin loans, holders borrow without selling (primary, in note)
- crypto.news — Ledger adds BTC-backed loans through Morpho (7 Oct 2026)
- coinlaw.io — Ledger/Morpho wrapped BTC loans, LTV/fee detail (Oct 2026, secondary — flag)
- The Block — Coinbase fixed-rate BTC loans via Morpho Midnight (22 Sep 2026)
- Morpho blog — Coinbase launches crypto-backed loans (Jan 2025)
- Internal priors: [[Coinbase's Bitcoin-backed loans surpass $1 billion]], [[Kraken launches Flexline crypto-backed loans at 10-25% APR]], [[Ledger puts $4 billion US IPO plans on hold]], [[Nexo unveils zero-interest credit at 0% APR]], [[Swiss bank Sygnum launches bitcoin-backed loan platform]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **Is it actually live?** Partially — rolling out to "eligible users," country-gated, not global; jurisdictions undisclosed. (confirmed)
2. **Does Ledger lend or custody anything?** No. Markets are Morpho's; collateral sits in Morpho smart contracts; Ledger only provides the hardware-signing UX. The PR headline overstates Ledger's role. (confirmed)
3. **Is this the same backend as Coinbase?** Yes — Morpho via Yield.xyz, the exact provider Coinbase has used since Jan 2025. So the rail is ~20 months old. (confirmed)
4. **Are the 50% LTV / 86% liquidation / 1% fee numbers official?** OPEN — secondary-sourced (coinlaw.io); Ledger's own blog does not publish them. Do not quote as fact.
5. **Fixed or variable rate?** Variable (Morpho market utilization). Unlike Coinbase's newer fixed-rate Midnight product — a disadvantage for retail wanting certainty. (confirmed)
6. **What is the real novelty vs Coinbase?** Self-custody + hardware signing + direct device-to-Morpho — a UX/custody delta, not a new credit product. (confirmed)
7. **Is the "liquidity flywheel" real or marketing?** OPEN — mechanically plausible (Earn supplies stablecoins ↔ Loan borrows them) but Morpho pools are protocol-wide; no data that Earn deposits specifically fund Ledger loans. Frambot quote is reported, not on Ledger's blog.
8. **Any Ledger-specific traction (TVL / loan volume)?** None disclosed. Only Coinbase's $1.4B/$3B and market-wide ~$73.6B exist. OPEN.
9. **Which chain?** Ethereum (four isolated Morpho markets) vs Coinbase's Base — a liquidity/fee difference worth noting. (confirmed)
10. **Who captures the margin in the stack?** Morpho/Yield.xyz own the rail and most economics; Ledger clips a thin borrow fee + Earn spread. Ledger is the front-end, not the lender. (analysis)
11. **Is "~30% of retail BTC / 8M signers" verifiable?** No — Ledger self-claim, independently unverified; don't conflate with Ledn's separate ~30%-of-consumer-*lending* claim. FLAGGED.
12. **Why would Ledger do this now?** Hardware sales are a saturating one-off; it needs recurring financial-services revenue to justify a >$4B IPO valuation (now on hold). (analysis)
13. **Is the self-custody differentiator a feature or a liability?** Double-edged — no custodian risk, but no human support desk or CeFi backstop; a sharp BTC drawdown forces on-chain liquidations on retail with variable rates. OPEN risk.
14. **Is it fresh or stale?** FRESH — Ledger's own first lending launch at TOKEN2049; no prior Ledger loan note. But substance is incremental (precedented rail).

Importance: 3/5 — A genuinely new, well-distributed product launch from a major brand in a hot sector (self-custody is a real differentiator), so above baseline. But capped: the credit rail is ~20-month-old Coinbase infrastructure, Ledger is only the signing UX, no traction is disclosed, and key terms are secondary-sourced. Fresh event, modest substance — not a market-mover.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-09]] (2026-10-09).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto-collateralised lending has re-inflated past the last cycle's highs: outstanding crypto-collateralised loans hit ~$73.6bn by Q3 2025 and loan origination volume across all crypto ran ~$67bn in Q1 2026, up ~50% YoY (per Galaxy Research, via AMINA Bank, as of 2026). The platform-service market is smaller — ~$10.7bn in 2025 → ~$12.7bn 2026, ~18.8% CAGR (per Research and Markets, as of 2026). The consumer *bitcoin*-backed slice is tiny by contrast — Ledn pegs it at ~$3bn today vs. a multi-trillion asset base (per Ledn, via Yahoo Finance, 2026), i.e. the structural pitch is penetration of long-term holders who want liquidity without a taxable sale. Structure: increasingly DeFi-rail-dominated — DeFi protocols are ~62.7% of outstanding loans vs. ~37.3% CeFi (per AMINA, 2026); value is migrating from the lender's balance sheet to on-chain credit protocols plus a front-end/distribution layer. Why now: post-BlockFi/Celsius collapse, the market has re-formed around non-custodial / on-chain collateral models that avoid rehypothecation; hardware-signer + DeFi-protocol pairing (this launch) is the self-custody-native expression of that shift.

**Competitive landscape.** Sector KPIs: loan originations / outstanding book, LTV ceiling + liquidation threshold, borrow APR, average loan size. Ledger's own disclosed KPI: it says it secures ~30% of all retail-held Bitcoin — a large captive collateral base, which is the actual asset here, not a lending book. Players & basis of competition (price = APR/LTV, distribution, custody model):
- **Coinbase** (same Morpho/Yield.xyz rail): >$1bn BTC-loan originations since Jan 2025, avg loan ~$54k, cap raised $1m→$5m; opened loans at ≥133% collateral (~75% max LTV, liquidation ~86%), rates from ~4–5% APR, added fixed-rate via Morpho Midnight Sep 2026 (per The Block / CoinDesk, 2025–26). Direct functional twin.
- **Nexo** (CeFi, custodial): 1.9–18.9% APR tiered on NEXO holdings, up to 90% LTV, $50–$2m (per Benzinga/Bitcompare, 2026) — cheaper headline rate but custodial.
- **Kraken Flexline**: fixed 10–25% APR, crypto collateral, builder/working-capital focus (2026-05).
- **Sygnum/Debifi MultiSYG**: bank-backed multi-sig, institutional/HNW, non-custodial angle (2025-10).
- **Aave**: DeFi lending #1, ~$17.7bn TVL — the open-protocol substrate others sit beside.

Protagonist position: **niche / fast-follower, differentiated on custody.** Ledger is not building a lending book; it is a distribution + hardware-signing front-end on top of Morpho — identical plumbing to Coinbase, but final approval stays on the user's device and collateral stays on-chain. Moat = intangible/installed-base (its ~30% retail-BTC custody footprint + hardware trust brand) and switching costs of the device ecosystem; NOT a lending/credit moat. `(analysis)`

**Comps & multiples.** Ledger is private; no lending-book or revenue figure disclosed for this feature → per-loan / origination economics = **no data / [UNSOURCED]**. Equity reference points: Ledger targeted a >$4bn NY IPO valuation Jan 2026 (plans later put on hold May 2026) — see [[Ledger plans New York IPO at over $4B valuation]] and [[Ledger puts $4 billion US IPO plans on hold]]; a $50m secondary (2026-03) gives a liquidity datapoint but no clean post-money multiple → distribution not computed, qualitative only. The rail provider, **Morpho**, is the comparable worth sizing: ~$11.2bn TVL, ~$5.7bn active loans, #2 DeFi lender behind Aave's ~$17.7bn (per DefiLlama/TheDefiant, Oct 2026). Internal comps: [[Coinbase's Bitcoin-backed loans surpass $1 billion]], [[Kraken launches Flexline crypto-backed loans at 10-25% APR]], [[Swiss bank Sygnum launches bitcoin-backed loan platform]], [[Stripe-backed Tempo taps DeFi lender Morpho to expand beyond payments]]. Arithmetic multiple (EV/Rev, EV/EBITDA) = **no data** — no public denominator for either Ledger's lending revenue or a clean Morpho revenue figure here. Qualitative read: Coinbase's ~$54k avg loan × a growing book shows the per-ticket economics are thin and volume-driven; Ledger enters at a structurally lower rate ceiling than Nexo's custodial top tier but inherits Morpho's variable on-chain borrow rate.

**Risk flags.**
1. **Rail dependence / disintermediation.** The entire product is Morpho + Yield.xyz — the exact stack Coinbase uses. Ledger owns the collateral relationship and the signer UX but not the credit protocol; the economics (borrow rate, liquidation logic, oracle) are captured one layer down. If Morpho repriced, failed, or on-boarded Ledger's rivals (it already powers Coinbase and Tempo), Ledger's differentiation collapses to "nicer signing flow."
2. **Liquidation / collateral-cycle risk.** Wrapped-BTC collateral with an on-chain liquidation threshold means a sharp BTC drawdown force-liquidates retail borrowers — the same mechanism that burned prior-cycle lenders, now pushed onto a retail hardware-wallet base rather than sophisticated desks. Reputational blast radius is larger given Ledger's security-brand positioning.
3. **Wrapped-asset + smart-contract surface.** cbBTC/wBTC introduce bridge/issuer trust (Coinbase-custodied cbBTC, BitGo-model wBTC) plus Morpho contract risk — new attack/counterparty surface for a firm whose core promise is self-custody safety, and which has prior customer-data-breach history ([[Ledger says payments partner leaked customer data in new breach]]).

**What this changes (idea-lens).** `(analysis)` This is a hardware-wallet maker converting a custody footprint into a financial-services distribution funnel — the same monetisation pivot neobanks ran, applied to self-custody. Falsifiable thesis: the durable winners in BTC-backed lending will be *distribution owners sitting on Morpho-class rails* (Coinbase, Ledger), not the protocols themselves, because the protocol is commoditised and fungible. Trigger to watch: whether Ledger discloses an outstanding loan book / origination number within 2–3 quarters (proof it's real volume, not a TOKEN2049 banner) and whether Morpho strikes further exclusive front-end deals. Thesis breaks if Morpho (or a rival protocol) launches its own retail front-end and captures the borrower directly.

Sources: https://aminagroup.com/research/crypto-lending-in-2026-how-borrowing-against-bitcoin-is-reshaping-global-credit/ · https://www.researchandmarkets.com/reports/6103510/crypto-lending-platform-market-report · https://finance.yahoo.com/markets/crypto/articles/ledn-sees-1-trillion-market-204900335.html · https://www.theblock.co/news/defi/2026-09-22-coinbase-fixed-rate-bitcoin-loans-morpho-midnight-416050 · https://bitcompare.net/platforms/nexo/loan-rates · https://defillama.com/protocol/morpho · https://decrypt.co/380224/ledger-bitcoin-loans-holders-borrow-without-selling
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news.** Ledger is a private company (hardware-wallet / self-custody; Paris) and publishes **no financial statements, no earnings release, and no formal results** — IR DB (`ir_latest.json[ledger]`) holds only blog posts, product updates and press releases (latest "result": "New CFO & Opening of NYC Office", 2026-03-23), never P&L figures. The TOKEN2049 item is a product launch (Crypto Loan), not a print. **Verdict: no-data.**

Disclosed operating proxies (not audited financials):
- **~30% of all Bitcoin held by retail investors secured** — per the Decrypt source note, 2026-10-08. Prior company figure: **~20% of crypto value secured** (Ledger "10 Years" blog, 2024-11-14, `ir_latest.json[ledger]`).
- **Devices: 7M+** cumulative (Ledger blog, 2024-11-14, IR); press reports ~**8M** more recently, with hardware-wallet sales **+~31% in 2025 vs 2024** — third-party reporting, not an IR disclosure (analysis).
- **Funding / valuation:** last priced round **$380M Series C at ~$1.5bn valuation (2021)**; ~$109M extension reported 2023 (Bloomberg/CoinDesk). Press (2025–26) reports Ledger is **weighing a NYC listing / new raise**, with one report floating a **~$4bn IPO** frame — a target/plan, not a completed deal (hypothesis). Figures via PitchBook/Tracxn/getLatka are **third-party estimates**, not company-reported.
- **Revenue:** no figure is company-disclosed. Third-party estimate (getLatka): **$70.9M (2024) vs $36.7M (2023)**, with 2025 reported as a record "triple-digit-millions" year — **[UNSOURCED / third-party estimate, not audited]**; do not treat as official.

Thesis note: the Crypto Loan launch (Morpho via Yield.xyz, hardware-signed) is a financial-services revenue-mix push on top of hardware sales, but with no reported unit economics (take-rate, loan book, revenue split) it cannot be sized here — no data.

Sources: `ir_latest.json[ledger]` (ledger.com blogs) · https://decrypt.co/380224/ledger-bitcoin-loans-holders-borrow-without-selling · https://finance.yahoo.com/news/ledger-plans-fundraise-weighs-york-070200670.html · https://finance.yahoo.com/news/ledger-turn-crypto-security-wall-095313890.html · https://www.coindesk.com/business/2023/03/30/crypto-hardware-wallet-maker-ledger-raises-most-of-109m-round-bloomberg · https://getlatka.com/companies/ledger (third-party revenue estimate) · https://pitchbook.com/profiles/company/109108-81 · No company-reported financial results exist — all figures are disclosed proxies or third-party estimates.
<!-- /enrichment:earnings_review -->
