---
title: "Stable launches StablePay app for instant USDT payments"
date: 2026-07-16
retrieved: 2026-07-16
tags:
  - company/stable
  - company/tether
  - industry/stablecoins
  - industry/payments
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/b865d6f8
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: seb958762
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Stable launches StablePay app for instant USDT payments

> [!info] 2026-07-16 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Stable launches StablePay, a mobile app built on its Tether-aligned StableChain blockchain that enables free, instant USDT payments worldwide. The app also includes a built-in yield feature, targeting peer-to-peer payments, remittances, and payroll with a simplified stablecoin payment experience.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/b865d6f8>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Stable launches StablePay app for instant USDT payments
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS VERDICT: fresh.** This is a genuine GA product launch (app live on App Store + Google Play, 2026-07-15), not a re-run. The concept was pre-announced at KBW2025 (Sep 2025, waitlist-only), and the parent chain's funding is covered in [[Stable raises $28 million for USDT-optimised blockchain]] (Aug 2025) — but the shipped consumer app is a new event. NOT a duplicate of the KBW tease (that was waitlist; this is public release). NOTE: [[Konga invests $2.7M in stablecoin payments startup Stable]] (Jun 2026) appears to be a DIFFERENT entity — external research indicates Konga backed "Stabyl" (Nigerian FX infra, ex-Konga co-CEO Nnamdi Ekeh), not this Bitfinex/Hack-VC-backed USDT L1. Likely mis-tag in the corpus; treat as unrelated.

## [0] What exactly happened (de-PR'd)
On 2026-07-15, **Stable** — the USDT-as-gas Layer-1 ("StableChain") incubated by Bitfinex and seeded by Bitfinex + Hack VC ($28M, Jul 2025) — publicly launched **StablePay**, a non-custodial mobile wallet for "free, instant, global" USDT send/receive. Features (per PR): send by phone/email/QR + "Stable Name" identifiers, email/Google/Apple login with no seed phrase, protocol-level gas-free USDT transfers (USDT is the chain's native gas), a built-in **Earn** yield feature, and fiat conversion. Targets P2P, remittances, payroll.
- **De-PR'd reality:** the app is genuinely LIVE (verifiable app-store listings), but almost all traction claims are unquantified. No user count, no transaction/GMV numbers at launch — the only figure that ever existed is a *pre-launch* "100k+ Korea waitlist" from KBW2025. "Already powering live payment flows across multiple regions" is PR with no regions named.
- **Why structured this way:** Stable's entire thesis is "USDT as native gas → gas-free UX." StablePay is the consumer front-end that makes that thesis tangible (a chain nobody touches directly is worthless; the app is the distribution play). But this also means StablePay is competing for the *same* users its own advisor/investor Tether is now courting directly.
- **Silent on:** custody/recovery mechanism ("non-custodial" + "no seed phrase" implies MPC/social-login, undisclosed); where Earn **yield** comes from (counterparty/security risk); whether on/off-ramp + FX conversion are actually free (they almost never are); US availability.

## [1] Competitors / peers
Gas-free instant USDT is now **table stakes, not a moat**:
- **Tether tether.wallet** (launched 2026-04-14) — Tether's OWN first-party self-custodial gas-free wallet (USDT/BTC/XAUT/USAT), human-readable addresses, riding ~570M USDT users. The single biggest threat: Stable's own investor/advisor (Ardoino) is now a direct competitor with vastly better distribution.
- **Plasma / Plasma One** — the *other* Bitfinex/Tether-adjacent USDT L1 (also Founders Fund/Thiel), mainnet Sep 2025, neobank "Plasma One" (Visa card, cashback, 10%+ yield) launched Jun 2026 ([[Plasma launches Plasma One stablecoin banking product]], [[Thiel-backed Plasma debuts $373M stablecoin neobank]]). Far ahead on TVL/traction and already has a card.
- **Tron** — still the dominant USDT settlement rail by volume; cheap USDT transfers already normal there.
- **Circle/USDC** (Arc L1, consumer rails), **Coinbase**, exchange wallets, gasless-USDT wallets (TokenPocket). Also emerging: **Tempo** (USDT0/USDC.e, [[Kraken supports Tempo blockchain for USDT0 and USDC.e]]).
- **Position: catching up / parity at best.** StablePay ships a near-identical pitch to tether.wallet and Plasma One but *later* and with *less* distribution.
- **Why the landscape is this way (2nd order):** Tether/Bitfinex hedged across multiple USDT-L1 bets (Stable, Plasma) plus its own wallet. That means the ecosystem sponsor is simultaneously Stable's backer AND its competitor — value likely accrues to whoever controls USDT issuance (Tether), not to the app layer.

## [2] Company history / fit
Stable emerged from stealth mid-2025; $28M seed (Bitfinex + Hack VC + Franklin Templeton, Susquehanna, Castle Island, etc.; advisors Ardoino/Tether, McCauley/Anchorage), founder/CEO **Joshua Harding** ([[Stable raises $28 million for USDT-optimised blockchain]]). StableChain mainnet + STABLE token + Stable Foundation launched 2025-12-08 (pre-deposit campaign ~$2B / 24k+ wallets — a deposit figure, not usage). StablePay was the promised consumer app (KBW2025 tease → Dec mainnet → Jul 2026 GA). Fits logically: a purpose-built payments L1 needs a flagship consumer app to bootstrap demand.
- **Why this way:** an L1 with no killer app is dead weight; shipping StablePay is the mandatory step to convert "$2B pre-deposited" into actual payment volume. (The launch quote attributes CEO to "Brian Mehler" in one PR vs founder Joshua Harding — name discrepancy is open.)

## [3] Novelty / value-add / traction
- **Newly live, but not conceptually novel.** The app is a real ship (2026-07-15); the mechanism (USDT-as-gas, gasless UX) was already the chain's Aug-2025 thesis, and rivals (tether.wallet, Plasma One) already offer gas-free instant USDT.
- **Traction: essentially unproven at launch.** No user/tx numbers; only a pre-launch waitlist. Earn/yield went from "roadmap" (Sep 2025 blog) to "built-in" (Jul 2026) — verify it actually shipped vs wording creep (open).
- **Who captures the margin (2nd order):** in a gas-free USDT app, the app operator earns little on transfers; economics must come from FX/on-off-ramp spreads and the Earn yield spread. That pushes StablePay toward the same monetization as any neobank — where Plasma One (card + yield) and Tether (issuer float) are structurally better positioned. The value-add is a UX skin unless Stable owns a distribution channel others lack (none disclosed).

## [4] What's next / market sentiment
- Watch for: real usage metrics (none yet), US availability decision, fiat ramp partners, how/where Earn yield is sourced, and STABLE token unlock (1-yr cliff from Dec 2025 → ~Dec 2026 = forward supply risk).
- **Regulatory backdrop:** GENIUS Act (signed 2025-07-18) is the tailwind for stablecoin payments but a specific risk here — USDT's US status under GENIUS (Treasury foreign-issuer comparability determination) is unresolved, so a USDT-only consumer app's US availability is legally uncertain. GENIUS also restricts issuer-paid yield, putting the Earn feature under potential SEC/compliance scrutiny.
- **Why the market goes this way (counterintuitive):** the flood of near-identical USDT payment apps from the Bitfinex/Tether orbit signals the *chain/app* layer is commoditizing while Tether keeps the float economics. Being close to Tether looks like a strength but is fragile — the sponsor can (and did, via tether.wallet) compete with its own investees.

## Sources
See challenge column + agent brief. Key: chainwire/PR Newswire StablePay launch (2026-07-15); Stable $28M seed PRNewswire/Medium (2025-07-31); StableChain mainnet TheBlock (2025-12-08); tether.wallet CoinDesk (2026-04-14); Plasma One Blockworks (2026-06). Internal: [[Stable raises $28 million for USDT-optimised blockchain]], [[Plasma launches Plasma One stablecoin banking product]], [[Thiel-backed Plasma debuts $373M stablecoin neobank]], [[Kraken supports Tempo blockchain for USDT0 and USDC.e]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_Importance: 3/5._ (Real, verifiable GA launch of a Bitfinex/Tether-orbit product — but conceptually me-too, no disclosed traction, and squeezed between Tether's own wallet and Plasma. Newsworthy as ecosystem signal, not as a breakout.)

## Top challenge / red-team questions

1. **Is StablePay actually live, or announced?** LIVE — on App Store + Google Play (`to.stablepay.app`) as of 2026-07-15. Confirmed by multiple wires.
2. **Same "Stable" as [[Konga invests $2.7M in stablecoin payments startup Stable]]?** No — external research says Konga backed "Stabyl" (Nigerian FX infra), a different entity. Corpus note likely mis-tagged. This item = the Bitfinex/Hack-VC USDT L1.
3. **Truly zero-fee end-to-end?** Gas-free USDT transfers: yes (protocol-level, USDT-as-gas). But whether fiat on/off-ramp + FX conversion are free is **open** — ramps almost never are; that's where the real cost sits.
4. **Any real user / transaction / GMV numbers at launch?** No. Only a pre-launch "100k+ Korea waitlist" (Sep 2025). Traction is **open/unproven**.
5. **What's genuinely new vs the Aug-2025 chain thesis?** Only the shipped consumer app; the gas-free mechanism is old. Rivals already do it.
6. **How is it non-custodial with no seed phrase?** Undisclosed — implies MPC/social-login key mgmt. Custody & recovery model **open**; a real due-diligence gap.
7. **Where does the built-in Earn yield come from?** Unspecified. Counterparty risk + securities/GENIUS-yield-restriction exposure = **open red flag**.
8. **Available in the US?** Unstated and doubtful — USDT's US status under GENIUS (Treasury comparability determination) is unresolved. **Open.**
9. **Only USDT / only StableChain at launch?** Yes; multi-stablecoin / cross-chain (Tron/Ethereum USDT interop) is roadmap, not launch. **Open.**
10. **How does it differ from Tether's own tether.wallet (Apr 2026) or Plasma One (Jun 2026)?** Materially little on the pitch. Tether has brand + 570M users; Plasma has TVL + a Visa card. StablePay's edge is **unclear/open**.
11. **Cannibalization by its own backer?** High — Tether (advisor Ardoino) shipped a first-party gas-free wallet that undercuts StablePay's identical value prop. Structural tension is real.
12. **Is Tether officially behind StablePay?** No — Bitfinex is a lead investor, Ardoino an advisor. tether.wallet is Tether's own product; StablePay is not a Tether product.
13. **Founder/CEO name discrepancy?** Corpus/Medium: Joshua Harding (founder/CEO). One launch PR quotes "Brian Mehler." Reconcile — **open**.
14. **Which "multiple regions" are live?** Unspecified in PR. **Open.**
15. **Downside trigger?** Token unlock cliff (~Dec 2026), no usage traction materializing, US regulatory shutout of USDT apps, or Tether/Plasma out-distributing it — any turns StablePay into an also-ran wallet.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** StablePay sits in the stablecoin-native payments/remittance layer — an app on Stable's own "StableChain" L1, not a wallet on a general chain. Sector size (per Mordor Intelligence, via mordorintelligence.com, as of 2026): total stablecoin market ~$0.33tn in 2026, CAGR ~28.8% to ~$1.16tn by 2031; total supply ~$316bn as of 12 Jun 2026 with USDT ~59% share (per Transak, via transak.com). The relevant sub-segment is payments, not float: McKinsey/Artemis put *actual* stablecoin payment volume at ~$390bn annualized on Dec-2025 activity — an order of magnitude below headline transfer volume, the key de-PR distinction here (per chainalysis.com / bancoli.com). P2P remittance is the stated use case: Juniper sees P2P stablecoin remittances growing from ~$860mn (2026) to ~$155bn by 2035, ~78% CAGR (per juniperresearch.com). Structure: fragmenting fast — a wave of "stablechains" (Plasma, Tempo, Codex, Stable, plus Tron/Avalanche as incumbents) raised >$548mn disclosed in 2025 (per across.to / eco.com). Barriers are distribution + regulatory (MiCA), NOT tech — zero-fee USDT transfer is now table stakes. **Why now:** USDT is being pushed off European venues (see [[Tether abandons Europe as MiCA ban wipes USDT from exchanges]]), redirecting Tether-aligned volume toward emerging-market P2P/remittance/payroll rails where StablePay is aimed — a regulatory-arbitrage tailwind, not organic EU demand.

**Competitive landscape.** Sector KPIs: on-chain payment volume (not raw transfer volume), monthly active senders, remittance corridors live, and for the underlying chain — TVL and USDT-as-gas throughput. Key players: Plasma (Tether/Bitfinex orbit, ~$18.7bn TVL Q2-2026), Stripe+Paradigm's Tempo, Coinbase-backed Codex (an L2, not sovereign L1), plus Tron and Avalanche as USDT-volume incumbents (see [[Hyundai pilots USDT treasury transfers on Avalanche]]). Basis of competition is distribution, not product: send-by-phone-number/QR, in-app fiat off-ramp, and a yield/"Earn" feature are common to nearly all of these. Recent moves: Stable launched StableChain mainnet + StablePay 15 Jul 2026 (App/Play Store), claiming live flows across P2P/remittance/payroll (per chainwire.org); Tether's own tether.wallet designated Plasma a core chain on 14 Apr 2026 with access to Tether's claimed 570M users (per eco.com). **Protagonist's position: catching-up niche `(analysis)`** — Stable ships an app on its own chain but is later and thinner than Plasma on TVL/liquidity, and directly overlaps Tether's own wallet distribution. Moat is weak/unproven: no disclosed network effects or switching costs yet, and "zero-fee USDT" is commoditized `(analysis)`.

**Comps & multiples.** Stable is a private, pre-token/early-token entity with **no disclosed valuation or revenue → EV/Revenue, P/S = no data**. Peer reference points (round valuations, NOT market caps):
- Plasma — raised ~$373mn public token sale (7x the $50mn target), ~$18.7bn TVL Q2-2026 (per btcc.com / defillama).
- Tempo (Stripe+Paradigm) — raised ~$500mn at a ~$5.0bn valuation, Oct 2025 → implied ~10.0x on money-raised ($5.0bn / $0.5bn) `(analysis)`, a pre-revenue narrative multiple, not an operating one.
- Codex — Coinbase Ventures / Dragonfly backed; disclosed valuation `[UNSOURCED]`.
- Internal comps: [[Tether abandons Europe as MiCA ban wipes USDT from exchanges]] · [[Stablecoin market cap shrinks $10B since May]] · [[The Paypers Stablecoins move from trading tool to infrastructure]] · [[RedotPay picks OpenPayd for stablecoin payment infrastructure]].
Distribution not computed (only 1 usable valuation datapoint, Tempo) → qualitative only. Read: stablechain valuations are being set on TVL/narrative and Tether affiliation, not payment revenue — Stable has neither a disclosed number nor Plasma-scale liquidity, so it is **unproven vs peers**, not cheap or rich.

**Risk flags.**
1. **Disintermediation by its own sponsor.** Tether's own tether.wallet + Plasma cover the same USDT send/receive/yield use case for the same 570M-user base — StablePay risks being squeezed by the ecosystem it's aligned to (margin/distribution captured one layer up).
2. **Regulatory / MiCA concentration.** The "why now" is USDT being expelled from EU venues; StablePay's addressable growth leans on emerging-market corridors where AML/remittance licensing and de-listing risk are highest — a policy-dependent TAM, not a durable one.
3. **De-PR gap: "live flows" unquantified.** "Already powering live payment flows" carries no volume, MAU, or corridor count; with real payment volume (~$390bn) an order of magnitude below headline transfer figures, adoption claims are unverifiable → treat as announced, not proven.

**What this changes (idea-lens).** `(analysis)` This is a *new-entry* move in an over-crowding stablechain field, not a re-rating — the marginal stablechain now bundles app + yield + zero-fee as standard, so differentiation shifts entirely to distribution and licensed corridors. Falsifiable thesis: StablePay fails to differentiate from tether.wallet/Plasma and stalls. **Trigger to watch:** disclosed StablePay MAU / monthly payment volume or a named remittance-corridor licensing win within ~2 quarters — absent that, treat as PR-stage. Thesis breaks if Stable posts Plasma-scale TVL or an independent (non-Tether) distribution deal.

Sources: https://chainwire.org/2026/07/15/stable-launches-stablepay-instant-zero-fee-global-payments-app-built-on-stablecoin-rails/ · https://blog.stable.xyz/introducing-stable-pay-the-stablecoin-payment-wallet-on-stablechain · https://transak.com/blog/stablecoin-market-cap-2026 · https://www.mordorintelligence.com/industry-reports/stablecoin-market · https://www.juniperresearch.com/press/stablecoin-p2p-remittances-to-cross-10bn-in-2030/ · https://www.chainalysis.com/blog/stablecoin-utility-future-of-payments/ · https://across.to/blog/stablechains · https://eco.com/support/en/articles/15010646-best-stablecoin-l1-chains-in-2026-the-new-wave-of-dollar-native-blockchains · https://www.btcc.com/en-CA/academy/crypto-wiki/altcoin/plasma-crypto
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
