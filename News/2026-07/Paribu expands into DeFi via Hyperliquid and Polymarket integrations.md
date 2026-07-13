---
title: "Paribu expands into DeFi via Hyperliquid and Polymarket integrations"
date: 2026-07-02
retrieved: 2026-07-02
tags:
  - company/paribu
  - industry/defi
  - industry/crypto
  - region/europe
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/5702291e
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: se32f379e
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Paribu expands into DeFi via Hyperliquid and Polymarket integrations

> [!info] 2026-07-02 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇹🇷 Türkiye’s leading digital asset platform Paribu has expanded into DeFi by integrating perpetual trading via Hyperliquid and prediction markets via Polymarket, while also opening a waitlist for U.S. and Turkish equity trading. The launch moves Paribu toward a unified platform combining crypto, DeFi, yield, and traditional investing.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/5702291e>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Paribu expands into DeFi via Hyperliquid and Polymarket integrations
_Analytical notes (not a post). Importance: 3/5. Freshness: FRESH (product launch, 2026-07-01/02; no prior note covers this event)._

## [0] What exactly happened (de-PR'd)
On **2026-07-01** Paribu (Türkiye's #1 CEX by the best available hard data — CoinGecko Jun-2023: 50.5% share, now ~3yr stale) announced an in-app **DeFi section**: DEX trading, **perpetuals routed to Hyperliquid**, and **prediction markets routed to Polymarket** — plus a **waitlist** for U.S./Turkish equity trading (NYSE, Nasdaq, Borsa Istanbul) and free real-time market data.

De-PR'd reality:
- **DeFi/prediction products are described as LIVE; equities are WAITLIST-ONLY**, pending an operating license for Paribu's brokerage arm (CMB granted only *establishment authorization*, ~Oct 2025). The most valuable leg (equities) is not live.
- **"Integration" = a self-custodial in-app frontend that routes order flow onchain**, not white-label or custodial CEX matching. Paribu's own wording: perps "route directly to Hyperliquid's blockchain," Paribu "serves as the interface, execution/settlement happen onchain through Polymarket." Assets stay in the user's wallet (no separate app/seed phrase; passkey recovery). → This is consistent with Hyperliquid's **"builder codes"** frontend model, though Paribu never names it — *unverified/open* whether builder codes vs. another path, and *unverified/open* whether "self-custodial" is real vs. passkey-controlled (effectively custodial).
- **The flagship "first regulated exchange to integrate BOTH Hyperliquid and Polymarket" claim is PR-originated and disputed** (see [1]). It is self-reported, no independent verification, and survives only under a narrow reading (excluding wallets like MetaMask, leaning on "regulated" which is itself shaky given the pending license).

**Why framed this way:** the "we're just a self-custodial interface / execution is onchain" language looks **engineered as regulatory-arbitrage cover** — an attempt to argue Paribu is not the CASP responsible for perps/prediction trades, which under Turkish law are legally problematic (see [4]). The "single app for all of finance" frame (CEO Yasin Oral) papers over that the headline products are either legally gray (perps/prediction) or not yet launched (equities).

## [1] Competitors / peers
The premise's implied "CEXes route to Hyperliquid" picture is mostly wrong:
- **No major CEX routes perp flow to Hyperliquid.** Coinbase (own Perpetuals, ~Jul-2025), Kraken (own perps), Binance/MEXC (own), **Robinhood** (perps via **Lighter**, a *rival* DEX) all built or used competitors.
- **Robinhood's prediction markets are Kalshi-powered, not Polymarket; Binance's are via Predict.fun.**
- **Who actually routes to Hyperliquid (builder-code frontends):** Phantom (Jul-2025), **MetaMask** (Oct-2025), pvp.trade, Axiom, Dexari, Okto.
- **Strongest counter to the "first...both" claim: MetaMask integrated BOTH first** — Hyperliquid perps (Oct-2025) and Polymarket (Dec-2025).
- **Turkish rivals (BTCTurk, Bitci, Icrypex, BinanceTR):** no evidence any integrated Hyperliquid/Polymarket (*open*).
- On the protocol side, the two rails Paribu bolts on are themselves converging/competing: Hyperliquid launched **HIP-4 offchain event contracts** aimed at Polymarket ([[Hyperliquid expands event contracts to macro events]], 2026-05); Polymarket bought DeFi infra ([[Polymarket acquires DeFi infrastructure startup Brahma]], 2026-03) and moved to native USDC ([[Circle and Polymarket partner to shift to native USDC]], 2026-02); perps DEX consolidation is live ([[Polygon-incubated Katana acquires IDEX, launches perps platform]], 2026-03).

**Why the landscape is this way / 2nd order:** builder-code frontends are now *commonplace plumbing*, so Paribu's move is **parity, not lead** — the differentiator it claims ("regulated CEX doing both self-custodially") is a narrow slice, and precisely the slice where Turkish law is most hostile. The real question shifts from "who integrated first" to **"can a *regulated* venue legally surface these onchain products to retail in its home market"** — which is where the value and the risk both sit.

## [2] Company history / fit
Trajectory (dates): founded **2017** (Yasin Oral); overtook BTCTurk as Türkiye's #1 CEX by ~**Apr-2023**; prior products — staking, Galatasaray (GAL) fan token, Paribu Custody/ColdShield (2024), Ventures/Art/Pass, acquired self-custody app Clave (2026); **CMB establishment authorization for a brokerage arm (~Oct-2025)**; acquired **CoinMENA up to $240M** (Dec-2025, [[Paribu acquires crypto exchange CoinMENA for $240M]]).

**Why Paribu acts this way:** a domestic-Turkey CEX faces a **commoditizing spot take-rate + tightening licensure** (CMP CASP regime), so it needs a **software/super-app multiple**: bolt DeFi yield, perps, prediction markets, and equities onto one app to widen the wallet-share and justify a re-rate. The CoinMENA (MENA) and equities pushes are the same logic — expand the surface beyond commodity spot. This launch fits that trajectory; the self-custodial framing is the mechanism that lets a *regulated* entity reach for products it may not be licensed to offer directly.

## [3] Novelty / value-add / traction
What is genuinely new: **not** the tech (builder-code routing exists; MetaMask did "both" earlier), but the **actor** — a *regulated Turkish CEX* surfacing onchain perps + prediction markets in-app, in a top-5 global retail-crypto market. That combination is a real convergence data point.

**Traction reality:** zero disclosed. No user/volume numbers for the DeFi section; equities are a **waitlist** (a marketing signup, no license in hand); no independent (non-PR) confirmation the features work for Turkish users today. Best hard market-position data is **3 years stale**.

**Who captures the margin / what breaks it:** if Paribu uses builder codes, it earns a **fee cut on routed flow (≤10bps perps)** — i.e., this is plausibly a **revenue play dressed as "access."** But the value-add is fragile: (a) the products may be **unlawful** for Turkish retail (perps banned, prediction ≈ gambling) → enforcement/blocking risk; (b) counterparty risk sits **offchain of Paribu's control** (Hyperliquid's JELLY delist precedent; Polymarket UMA oracle mis-resolution) yet is surfaced under Paribu's brand; (c) Hyperliquid's own HIP-4 now competes with Polymarket, so routing to "both" may not be durable.

## [4] What's next / market sentiment
Plans: launch equities once the brokerage license clears; deepen the "single app for all of finance." Backdrop is the 2025–26 **CEX↔onchain convergence** (Polymarket's CFTC path + ICE's up-to-$2B stake at ~$8B; Hyperliquid dominance of onchain perps).

**Turkish regulatory backdrop (the biggest under-covered risk):**
- CASP regime: Law 7518 (in force 2-Jul-2024); Communiqués III-35/B.1 & B.2 (13-Mar-2025); licensing conditions from 30-Jun-2025. MASAK travel rule effective 25-Feb-2025.
- **Perpetuals: prohibited** on licensed platforms — the Mar-2025 Communiqués bar leveraged trading/derivatives/margin/short-selling.
- **Prediction markets: likely illegal gambling** (state İddaa monopoly; Law 7258 + Penal Code Art. 228; enabling access to foreign betting → 4–6yr; 84k+ betting sites blocked in 2025). No documented enforcement naming Polymarket yet (*open*) — the classification is a strong inference, not a cited ruling.
- Foreign-platform blocking (CMB Art. 99/A) already hit exchanges and DEXes ([[Turkey blocks PancakeSwap and 45 crypto websites]], 2025-07).

**Why the market/legal picture cuts against the PR:** offering Hyperliquid perps to Turkish retail is **directly at odds** with the derivatives ban, and Polymarket is exposed under **both** crypto-blocking and anti-gambling law. **2nd-order:** the very self-custody framing meant to *reduce* legal exposure could instead **jeopardize Paribu's pending operating license or invite BTK blocking** — i.e., a super-app land-grab that raises regulatory fragility rather than lowering it. Sentiment: notable strategic signal, not category-defining.

## Sources
- Paribu GlobeNewswire release (2026-07-01), mirrors: manilatimes.net, finsmes, fxstreet.
- crypto.news (2026-07-02); crypto-economy.com; cryptonomist.ch; Wu Blockchain (X).
- Primary in-corpus link: https://www.connectingthedotsinfin.tech/r/5702291e
- CMB Communiqués III-35/B.1 & B.2 (mondaq summary); MASAK travel-rule; CoinGecko Türkiye research (Jun-2023).
- Hyperliquid builder-codes docs; MetaMask prediction-markets launch (Dec-2025).
- Internal: [[Paribu acquires crypto exchange CoinMENA for $240M]], [[Hyperliquid expands event contracts to macro events]], [[Polymarket acquires DeFi infrastructure startup Brahma]], [[Polygon-incubated Katana acquires IDEX, launches perps platform]], [[Circle and Polymarket partner to shift to native USDC]], [[Turkey blocks PancakeSwap and 45 crypto websites]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions (open unless answered):**

1. If Turkish rules **ban crypto derivatives** on licensed platforms, how is offering Hyperliquid **perps** to Turkish retail lawful — is the "self-custodial interface" framing a tested CMB position or unlitigated regulatory arbitrage? — *open; likely arbitrage.*
2. Do **prediction markets** trip Turkey's **anti-gambling** monopoly (İddaa, Law 7258, PC Art. 228)? Any legal opinion / no-action letter? — *open; strong inference they do.*
3. Does Paribu use Hyperliquid **builder codes**, and what fee does it take — is this a **revenue** play dressed as "access"? — *open; plausibly yes.*
4. Is "self-custodial, assets stay in the user's wallet" real, or does Paribu control passkeys/keys so it is **effectively custodial**? — *open.*
5. Who bears counterparty/settlement risk when Hyperliquid (cf. JELLY delist) or Polymarket's **UMA oracle mis-resolves** a market shown inside Paribu's app? — *open.*
6. The "**first regulated exchange to integrate both**" claim excludes MetaMask (Hyperliquid Oct-2025, Polymarket Dec-2025) — is the superlative just carefully worded marketing? — *yes, disputed.*
7. "**Regulated**" — is Paribu's *crypto CASP* license actually granted, or only its brokerage *establishment authorization* with operating license **pending**? What exactly is licensed today? — *equities license pending.*
8. What are the **real current** user/volume/market-share numbers? Best hard data (CoinGecko) is Jun-2023; is "Türkiye's leading" still true post-licensing consolidation? — *open, ~3yr stale.*
9. Could offering unlicensed onchain products **jeopardize** the pending CMB operating license or invite **BTK blocking**? — *open, material risk.*
10. On the equity **waitlist**: is there any credible license timeline, or is it a marketing signup with no license in hand? — *waitlist only.*
11. Are Turkish users **KYC-geofenced** for Polymarket? Does routing Turkish flow onchain create **MASAK/travel-rule** exposure? — *open.*
12. Which markets are in Polymarket's "**curated**" set — does Paribu filter politically sensitive ones (Turkish speech/gambling law)? — *open.*
13. Is the timing tied to the **CoinMENA** deal, a raise, or pre-license positioning — i.e., narrative more than product? — *open.*
14. Given Hyperliquid's own **HIP-4 prediction markets** now compete with Polymarket, why route to both — durable integration or headline? — *open.*
15. Any **independent** (non-PR) confirmation the DeFi features are actually **live and functioning** for Turkish users today vs. merely announced? — *none found.*

**Importance: 3/5** — A regulated Turkish CEX surfacing onchain perps + prediction markets self-custodially, in a top-5 retail crypto market, is a genuine CEX↔onchain convergence signal and a smart (if risky) super-app move. But it is not novel globally (MetaMask did "both" first; builder-code frontends are commonplace), the "first regulated" flagship claim is PR spin, the highest-value leg (equities) is only a waitlist, there is zero disclosed traction, and the perps/prediction products sit on shaky-to-illegal Turkish legal ground. Incremental, not category-defining. Would be 4/5 if the "first regulated" framing held or equities were live.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Paribu's move sits at the CEX-to-DeFi convergence front, where regulated centralized exchanges front-end onchain venues rather than build derivatives in-house. Two sub-markets underpin it: (1) onchain perpetuals — per DefiLlama via various trackers, ~$540bn/30d total perp-DEX volume with Hyperliquid the clear leader (share cited anywhere from ~32% on a strict DefiLlama snapshot to 44%/70%+ on narrower cuts, as of mid-2026; treat the exact number as disputed, but "category leader" is robust), Hyperliquid's own cumulative volume >$4tn and open interest >$9bn (per crypto.news/blockeden, 2026); (2) prediction markets — monthly volume rose from $1.2bn (early 2025) to >$20bn (Jan 2026) with 800k+ monthly wallets, and Bernstein projects ~$240bn full-year 2026, ~3.7x YoY, $1tn by 2030 (per Bernstein via tradingkey/coindesk). **Why now:** perp-DEX infra now matches CEX latency/UX (24/7, self-custodial settlement), and a regulated exchange can wrap it while keeping custody with the user — the "everything exchange" pattern Coinbase pioneered (`[[Coinbase launches 24 7 stock perpetual futures]]`, `[[Coinbase and Kalshi bring perpetual crypto futures to US]]`). Structure: perp-DEX layer is winner-take-most (Hyperliquid dominant); the CEX-aggregator layer above it is fragmented and low-barrier — the moat is regulatory license + local distribution, not the DeFi tech (which is rented).

**Competitive landscape.** Sector KPIs: perp/prediction volume routed, take rate on routed flow (undisclosed by Paribu → `[UNSOURCED]`), MAU/funded accounts, and — critically — whether flow is *live* vs *waitlisted* (US/Turkish equities are waitlist-only per the PR). Basis of competition = distribution + regulatory standing, not product novelty. Key players wrapping onchain venues into a front-end: Coinbase (Kalshi prediction markets, 24/7 stock perps, "everything exchange"), OKX (in-wallet DEX trading on Base/Solana, Nov 2025 — `[[OKX launches in-wallet DEX trading on Base, Solana, X Layer]]`), MoonPay (bought DFlow for onchain routing, May 2026 — `[[MoonPay acquires DFlow for on-chain trading infrastructure]]`). Recent moves: Hyperliquid itself is launching prediction markets (Apr–May 2026, per coindesk/cryptotimes), i.e. the venue Paribu routes to for perps is moving into the venue it routes to for predictions — future channel conflict. Paribu's position: **first-mover among regulated exchanges to bundle *both* Hyperliquid perps and Polymarket in one CEX interface** (per crypto-economy), and first Turkish access to prediction markets — a genuine niche-first, but a distribution advantage in one geography, not a defensible tech moat (analysis). Recent Paribu context: acquired MENA's CoinMENA for up to $240M (Dec 2025 — `[[Paribu acquires crypto exchange CoinMENA for $240M]]`), so this is part of a broader "unified multi-asset platform" build-out, not a one-off.

**Comps & multiples.** Paribu is private and discloses no revenue/valuation → own EV/Rev, P/E = no data. The two routed venues, as sizing anchors (not Paribu's economics): Polymarket — targeting ~$15bn valuation on a ~$400M raise (per Bloomberg/PYMNTS, Apr 2026), up >66% from ~$9bn prior; still below Kalshi's ~$22bn; ICE has put ~$600M+ in (coindesk). Hyperliquid — no clean equity valuation cited; sized on flow (>$4tn cumulative volume, >$9bn OI). Internal deal comp: Paribu/CoinMENA at up to $240M (`[[Paribu acquires crypto exchange CoinMENA for $240M]]`); adjacent perp-DEX M&A: Katana/IDEX (`[[Polygon-incubated Katana acquires IDEX, launches perps platform]]`, Mar 2026), Coinbase/The Clearing Company for prediction-market clearing (`[[Coinbase to acquire The Clearing Company]]`). Distribution not computed — <3 comparable revenue figures exist for Paribu; qualitative comparison only. No multiple is computable here; arithmetic omitted deliberately rather than invented.

**Risk flags.**
1. **Regulatory disintermediation in the home market.** Turkey's CMB blocked PancakeSwap + 45 DeFi/DEX sites in a July 2025 crackdown (`[[Turkey blocks PancakeSwap and 45 crypto websites]]`); the CMB/MASAK regime now licenses CASPs and caps stablecoin transfers ($3k/day, $50k/month, MASAK Circular 29, 2025). Paribu routing licensed users into onchain DeFi/prediction markets is exactly the activity the regulator has been fencing off — the core second-order risk is that its regulated status (its only real moat) becomes the liability if the CMB deems DeFi/prediction-market routing out-of-perimeter.
2. **Dependence on someone else's rails + channel conflict.** Perps run through Hyperliquid, predictions through Polymarket; Paribu captures interface/curation only, and both partners can (and Hyperliquid is) expanding up the stack — Hyperliquid launching its own prediction markets (2026) means Paribu could be routing to a venue that competes with its other routed venue. Margin sits with the protocol layer, not the wrapper.
3. **Announced vs live.** Equities (US + Turkish) are waitlist-only; the PR bundles live DeFi with not-yet-live equities into one "unified platform" narrative. The economics (take rate, who bears settlement/fraud liability onchain) are undisclosed — de-PR: treat "unified platform" as roadmap, not run-rate.

**What this changes (idea-lens).** (analysis) Signals that the CEX-to-DeFi wrapper model is going regional: emerging-market regulated exchanges with strong local distribution (Turkey #5 globally, ~$40bn Q1-2026 retail volume, per TRM Labs) can bolt on Hyperliquid/Polymarket rails without building derivatives infra — a distribution play, not a tech play. Falsifiable thesis: this is *additive niche entry*, not a re-rating, and it only compounds if the CMB tolerates DeFi routing. **Watch/trigger:** a CMB statement or enforcement action on onchain perp/prediction routing by licensed CASPs — that single regulatory signal would validate or break the thesis; a Hyperliquid-native or Binance/BtcTurk copycat wrapper in Turkey would confirm the model is generalizable.

Sources: https://crypto-economy.com/paribu-becomes-first-regulated-exchange-to-integrate-both-hyperliquid-and-polymarket/ · https://www.paribu.com/blog/en/news/paribu-integrates-polymarket-opening-turkiyes-first-access-to-prediction-markets/ · https://crypto.news/paribu-adds-defi-polymarket-and-stock-waitlist-to-its-app/ · https://www.bloomberg.com/news/articles/2026-04-20/polymarket-in-talks-for-new-investment-at-15-billion-valuation · https://www.coindesk.com/business/2026/04/29/hyperliquid-is-preparing-to-take-on-polymarket-with-a-new-way-to-trade-real-world-events · https://www.trmlabs.com/resources/blog/q1-2026-global-crypto-adoption-index · https://cryptoslate.com/turkey-blocks-access-to-pancakeswap-45-crypto-websites-in-regulatory-crackdown/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
