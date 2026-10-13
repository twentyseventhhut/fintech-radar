---
title: "Stripe challenges Circle with bank-backed Open USD stablecoin"
date: 2026-10-13
retrieved: 2026-10-13
tags:
  - company/stripe
  - company/circle
  - industry/stablecoins
  - industry/crypto
  - region/us
  - type/product
sources:
  - https://www.thebanker.com/content/38e1c371-ca68-4a84-a540-8bdc0fb431e2
status: enriched
n_mentions: 1
channels:
  - "The Fintech Blueprint"
story_id: sa763635f
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Stripe challenges Circle with bank-backed Open USD stablecoin

> [!info] 2026-10-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: The Fintech Blueprint

## Агрегированный текст (из дайджестов)

[The Fintech Blueprint] ⭐ Stripe challenges Circle with bank-backed Open USD stablecoin - The Banker

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.thebanker.com/content/38e1c371-ca68-4a84-a540-8bdc0fb431e2>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Stripe & partners launch Open USD (OUSD) — a consortium stablecoin aimed at Circle's economics
_Analytical notes (not a post). Importance: 4/5._

> NB on the headline: The Banker's "Stripe challenges Circle with bank-backed Open USD stablecoin" **mis-frames the event twice.** (1) It is not Stripe's coin — it is issued by **Bridge** (Stripe's 2024 acquisition, ~$1.1B) and governed by **Open Standard**, an independent consortium with **five equal founding partners: Stripe, Visa, Mastercard, Coinbase, Shopify** (BlackRock also founding-tier). Stripe is one of five, not the owner. (2) "Bank-backed" is loose: banks (Lead Bank, BNY Mellon) are **reserve custodians**, not sponsors/issuers. The real story is a **card-network + fintech + exchange cartel attacking the reserve-interest economics of USDC/USDT**, not a Stripe product launch.

## [0] What exactly happened (de-PR'd)
- **OUSD went live 30 Sep 2026** on Ethereum, Solana, Base and **Tempo** (Stripe's own L1 — see [[Stripe-backed Tempo launches stablecoin transaction framework]]). First reported 3 Jun 2026; consortium formally unveiled **30 Jun 2026**.
- **Issuer:** Bridge (Stripe subsidiary; CEO Zach Abrams, ex-Bridge). **Governance:** Open Standard, an independent company — "shared among members rather than controlled by a single issuer."
- **Founding partners (equal initial equity):** Coinbase, Mastercard, Shopify, Stripe, Visa; BlackRock founding-tier. Network grew **140+ (Jun) → 200+ (Sep/Oct)**, incl. UBS, SBI Holdings, Standard Chartered, Google, IBM, Aave, Jeeves.
- **$1B+ liquidity** committed by the five founders "over the coming months" (individual sizes undisclosed — vague, watch this).
- **Reserves:** held at **BlackRock, Lead Bank, BNY Mellon**; Bridge commits to **monthly attestations**. GENIUS-ready compliance.
- **The mechanism (the actual point):** zero mint/redeem fees + **reserve interest (Treasury yield) distributed back to distributing partners** by supply generated & transaction activity, minus a management fee. This directly inverts Circle's model (Circle keeps most reserve interest, pays select distributors like Coinbase a revenue share).
- **Why structured this way:** a consortium with equal equity + yield pass-through is engineered to **recruit distribution, not sell a coin.** The scarce input in stablecoins is not tech — it's distribution (wallets, merchants, card rails). By handing distributors the float economics they're denied on USDC, the consortium turns Circle's own distributors (Coinbase!) into its rivals' recruiters. → second order: Coinbase sits on **both** sides (it earns ~half of Circle's USDC reserve income today AND is an OUSD founder), so its presence is a hedge/threat against its own USDC cash cow.

## [1] Competitors / peers
- **Circle / USDC** (direct target): $74–75B cap, grew 73% in 2025, outpacing USDT growth for a 2nd year ([[Circle's USDC outpaces USDT growth for second year]]). Circle's whole P&L is reserve interest it retains. On the OUSD unveil (30 Jun), **CRCL fell >17%**, closing below $63 — weakest since Feb, down ~55% from mid-May. Jefferies reportedly warned against buying the dip; CoinShares called OUSD "the biggest threat yet" to USDC's model (per headlines).
- **Tether / USDT:** ~$143–186B, unregulated in US/EU — less exposed to a "regulated + yield-sharing" pitch but still the volume leader.
- **Stripe's own prior stablecoin stack:** **Open Issuance** (Oct 2025, [[Stripe launches Open Issuance and stablecoin products]]) is a *white-label self-issuance* toolkit (Phantom CASH, mUSD, USDH). OUSD is the opposite bet — one *shared* coin with network liquidity rather than a thousand bespoke coins. **Tempo** ([[Stripe-backed Tempo launches stablecoin transaction framework]]) is the settlement chain; **Arc** is Circle's competing L1. So the fight is now **full-stack**: issuer vs issuer, chain vs chain.
- **Why the lay of the land:** post-GENIUS ([[Connecting the Dots Stablecoin competition heats up post-GENIUS]]), regulated USD stablecoins are table stakes; differentiation moved from "is it compliant" to "who keeps the float." Card networks (Visa/MC) entering as *issuers* (not just rails) is the structural shock — they bring merchant + issuing distribution Circle can't match.

## [2] Company history / fit
- Stripe's arc: acquired **Bridge (2024, ~$1.1B)** and **Privy (2025)**; launched stablecoin subscriptions, Open Issuance + Tempo. OUSD is the logical capstone: Stripe already owns the issuer (Bridge), the chain (Tempo) and the merchant distribution.
- **Why Stripe acts this way:** payments is a commodity take-rate business; owning the money itself (float + issuance) captures a *new* margin pool (reserve yield on ~$300B+ TAM) that a per-transaction fee never could. For Visa/MC the logic is defensive — stablecoins threaten interchange, so co-owning the coin keeps them in the value chain rather than disintermediated.

## [3] Novelty / value-add / traction
- **Genuinely new** (not a reprint of Open Issuance/Tempo): a *multi-issuer-governed single coin* with yield pass-through and $1B seeded liquidity and the card networks as equity founders. That combination is new.
- **Traction is still mostly commitment, not adoption:** "live" since 30 Sep but no disclosed OUSD circulating supply / on-chain cap vs USDC's $74B. $1B is a *pledge* "over coming months," not deployed float. 200+ signatories ≠ 200+ integrations. **Announced ≫ adopted** for now.
- **Who captures the margin (the real question):** OUSD redistributes reserve yield to distributors — so the *issuer* (Bridge/Stripe) deliberately gives up the fat margin Circle keeps. Stripe's payoff is strategic (own the rails/chain, drive volume to Tempo), not the float itself. → so the durable question isn't "will OUSD beat USDC on size" but **"can Stripe monetize owning the settlement stack once the coin itself is a loss-leader?"** If not, OUSD is a weapon to depress Circle's margins more than a profit center.

## [4] What's next / market sentiment
- Watch: disclosed OUSD circulating supply + first monthly reserve attestation; whether Coinbase actually shifts USDC distribution economics toward OUSD (the swing factor); interoperability/swaps with Open Issuance coins.
- Sentiment: clearly negative for Circle (equity -17% on unveil, -55% from May highs). Bull case for the consortium = GENIUS-era regulated demand + unmatched distribution. Bear case = coordination risk among five rivals with equal equity, antitrust optics of Visa+MC+Coinbase co-owning a dollar instrument, and that the whole thesis rests on *compressing* an industry's economics (a race to zero on float yield that could hurt all issuers, consortium included).
- **Counterintuitive second order:** by commoditizing stablecoin float, the consortium may win share yet shrink the *total* profit pool it's fighting over — a Pyrrhic win where the value migrates to whoever owns distribution and settlement (Visa/MC/Stripe), not to "the coin."

## Sources
- The Banker (primary headline, title only). CoinDesk 24 Sep & 30 Jun 2026; American Banker; Unchained; Forbes (OUSD live). See challenge file for URLs.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is it really Stripe's coin?** No — issued by **Bridge** (Stripe subsidiary) and governed by **Open Standard**, 5 equal founding partners (Stripe, Visa, Mastercard, Coinbase, Shopify). The Banker headline overstates Stripe's role. Answered.
2. **Is "bank-backed" accurate?** Loosely. Banks (Lead Bank, BNY Mellon) are **reserve custodians**; BlackRock holds Treasuries. No bank "issues" it. Reframe to "consortium-issued, bank-custodied." Answered.
3. **New event or reprint of Open Issuance/Tempo?** **New.** Open Issuance (Oct 2025) = white-label self-issuance toolkit; Tempo = settlement L1; OUSD = a single consortium coin launched 30 Sep 2026. Distinct. **Fresh.** Answered.
4. **Announced vs live vs adopted?** Live on-chain 30 Sep 2026, but **no disclosed circulating supply / cap**; $1B is a pledge "over coming months." Adoption unproven. Open.
5. **How exactly does it attack Circle?** By returning reserve (Treasury) interest to distributing partners + zero mint/redeem fees — inverting Circle's keep-the-float model. Answered.
6. **Did the market believe the threat?** Yes — CRCL fell **>17%** on 30 Jun 2026 unveil, down ~55% from mid-May highs. Answered (market signal, not fundamentals yet).
7. **Who captures the margin if float yield is given away?** Not the issuer — Stripe/Visa/MC monetize distribution + settlement (Tempo rails, interchange retention). OUSD is plausibly a loss-leader/weapon. (analysis) Open on durability.
8. **Why would Coinbase join when it earns ~half of Circle's USDC reserve income?** Hedge + optionality; it sits on both sides. A genuine shift of Coinbase distribution to OUSD is the single biggest swing factor. Open.
9. **What's the coordination/governance risk?** Five rival equal-equity owners (two card networks, an exchange, two platforms) must cooperate on a dollar instrument — fragile, plus antitrust optics. (hypothesis) Open.
10. **Does yield pass-through survive regulation?** GENIUS Act restricts paying *yield to holders*; paying *distributors* rewards is the workaround — legally live but a regulatory soft spot. Open.
11. **Is the $1B liquidity real or vaporware?** Committed, sizes undisclosed, "over coming months." Treat as soft until on-chain supply confirms. Open.
12. **Does this fragment Stripe's own stablecoin strategy?** Open Issuance (many coins) vs OUSD (one shared coin) could cannibalize — unless OUSD becomes the default liquidity hub for Open Issuance swaps. (analysis) Open.
13. **Second-order market effect?** Commoditizing float yield may shrink the total profit pool even for winners — value migrates to distribution/settlement owners, not the coin. (hypothesis)
14. **Who's silent?** Exact OUSD supply, per-partner $ commitments, Circle's distributor contract terms, whether merchants actually settle in OUSD. Open.
15. **Freshness verdict:** FRESH — genuine new event (consortium coin, new partners, live date), not a re-run of [[Stripe launches Open Issuance and stablecoin products]] or [[Stripe-backed Tempo launches stablecoin transaction framework]].

**Importance: 4/5** — Rationale: a real, dated, live event with material market impact (CRCL -17%), card networks entering as stablecoin *issuers*, and a structural attack on the dominant USDC economics. Not a 5 because OUSD traction is still commitment-stage (no disclosed circulating supply) and the thesis — that giving away float yield wins — is unproven; the headline also over-attributes it to Stripe.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** US stablecoins is a ~$300bn market long duopolised by Tether (USDT) and Circle (USDC) (per CoinDesk/The Information, via [[Connecting the Dots Stablecoin competition heats up post-GENIUS]], as of 2025-10). The economics are a reserve-income model: issuers hold 1:1 reserves in cash + short-dated US Treasuries and keep the interest. Circle's own IR shows the scale and the margin pressure: USDC in circulation reached **$77.0bn** at Q1'26 (+28% y/y), Reserve Income **$653m** (+17% y/y) was 94% of **$694m** total revenue, and the reserve return rate fell **-66bps** y/y even as circulation grew (Circle Q1'26, businesswire 2026-05-11). Why now: the GENIUS Act (P.L. 119-27) gave the first US federal regime — full 1:1 high-quality-liquid-asset backing, monthly attestations, qualified-custody segregation — legitimising bank/consortium entry. The structural catch: GENIUS **§4(a)(11) prohibits issuers paying yield/interest to holders** (Federal Register, 2026). Open USD routes reserve income to *distributors* (banks/fintechs), not holders — the same arbitrage every challenger is now chasing.

**Competitive landscape.** Sector KPIs: stablecoin float (circulation), reserve-return rate (× float = revenue), and distribution reach (chains, wallets, merchants). Open USD (OUSD) launched **2026-09-30** via Open Standard, issued by Stripe-owned **Bridge**, reserves custodied at BNY, Lead Bank and BlackRock, with >$1bn committed liquidity and 140+ partners incl. Visa, Mastercard, Coinbase, Shopify, BlackRock (Forbes/CoinDesk, 2026-09/10). Basis of competition shifts from brand/float to **distribution + economics-sharing**: Open USD's edge is it pays reserve income back to the distributor and is natively plumbed into Stripe/Bridge rails and card networks. Circle's moat was first-mover regulated float + the Circle Payments Network ([[ClearBank to join Circle Payments Network for USDC and EURC]], [[Deutsche Börse and Circle collaborate on stablecoins in Europe]]) and the Arc institutional chain ([[Circle raises $222 million in Arc token presale at $3 billion valuation]]). Position: Circle is the incumbent being *disintermediated at the distribution layer* — it owns the token, but Stripe/Bridge owns the merchant rails (analysis). Related Stripe moves: [[Stripe to expand stablecoin cards to 100+ countries]].

**Comps & multiples.** Circle (CRCL): price ~$81.49, market cap **~$21.4bn**, TTM revenue **~$2.91bn** → P/S = $21.4bn / $2.91bn = **~7.3x**; P/E (normalised) ~64x (Morningstar/companiesmarketcap, 2026-10-13). CRCL is off its 52-wk high ($147) to near the low ($49.90) — the stock fell ~8% on the Open USD consortium news (CoinDesk, 2026-06-30). Internal round comp: Circle's Arc platform priced at a **$3bn** presale valuation (round, not market cap — [[Circle raises $222 million in Arc token presale at $3 billion valuation]]). Peer floats for context: Tether USDT and Circle USDC dominate; PayPal PYUSD only crossed **$1bn** market cap ([[PayPal's PYUSD stablecoin reaches $1B market cap via Spark]]) — i.e. PYUSD is ~1.3% of USDC's $77bn, showing how hard float is to build. Rich/cheap: CRCL's ~7.3x P/S and ~64x P/E are rich for a single-product issuer whose revenue is ~94% rate-sensitive reserve income with a declining return rate — the multiple prices sustained float growth that Open USD directly threatens. Stripe is private; last reference valuation **$159bn** (2026 tender, Stripe 2025 letter) on **$1.9T** total volume — not a stablecoin pure-play, so not a float comp.

**Risk flags.**
1. **Regulatory (GENIUS §4(a)(11)).** The whole "share interest income" pitch skirts the yield ban by paying *distributors* not holders — an untested distinction regulators (OCC/FDIC/Fed rules still being finalised, 2026) could reclassify, collapsing Open USD's core differentiator.
2. **Disintermediation of Circle's economics.** Circle's revenue is ~94% reserve income from float; if Stripe/Bridge pulls distribution, USDC float — hence Circle's rate-sensitive income — erodes even without a depeg (the -66bps return-rate decline already shows how thin the cushion is).
3. **Adoption vs announcement.** $1bn committed liquidity and 140 partners are *announced*; de-PR'd, OUSD must build float from near-zero against USDC's $77bn — PYUSD's two-year grind to $1bn is the base rate for how slow this is.
4. **Reserve/depeg & concentration.** A new coin with concentrated bank custodians (BNY, Lead Bank) and consortium governance carries depeg and single-custodian operational risk until circulation and attestation history prove the 1:1 holds under redemption stress.

**What this changes (idea-lens).** Open USD reframes stablecoins from a token-brand race to a *distribution-and-economics-sharing* race — the value is migrating from the issuer to whoever owns the merchant/card rails (analysis). Falsifiable thesis: if OUSD circulation clears ~$5–10bn within 12 months while USDC float stalls, CRCL's ~7.3x P/S re-rates down. Trigger to watch: next Circle 10-Q USDC-in-circulation print and any OCC/Fed guidance on whether distributor reward-sharing counts as prohibited "yield." Thesis breaks if regulators ban distributor income-sharing, neutering Open USD's edge and re-entrenching Circle.

Sources: https://www.businesswire.com/news/home/20260511188445/en/Circle-Reports-First-Quarter-2026-Results · https://www.sec.gov/Archives/edgar/data/1876042/000187604226000148/final_05x11q1epr30.htm · https://assets.stripeassets.com/fzn2n1nzq965/3LlGw839Q6kUwxZlLZDtH6/75ddcbada4aa7743dd8ec7d0f9ca497e/Stripe-annual-letter-2025-desktop.pdf · https://www.forbes.com/sites/gabrielalinzainescu/2026/09/30/ousd-stablecoin-goes-live-with-visa-mastercard-and-stripe-behind-it/ · https://www.coindesk.com/business/2026/06/30/circle-slides-8-as-stripe-coinbase-and-blackrock-back-rival-stablecoin-network · https://www.federalregister.gov/documents/2026/04/10/2026-06974/genius-act-requirements-and-standards-for-fdic-supervised-permitted-payment-stablecoin-issuers-and · https://companiesmarketcap.com/circle-internet-group/marketcap/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** MIXED — EPS beat, revenue miss. Latest reported period is **Q1 2026** (ended 2026-03-31, released 2026-05-11): total revenue and reserve income **$694.1M (+20% YoY)**, vs public consensus ~$715M → **miss of ~$21M (-2.9%)**; diluted EPS **$0.21** vs Zacks consensus **$0.15** → **beat +36.7%**; net income from continuing operations **$55M (-15% YoY)**. Guidance: prior KPI guidance affirmed (excluding future ARC Token / Arc revenue). The earnings are the thesis: Circle's P&L is ~94% reserve interest income, the exact economics a bank-backed, yield-sharing Open USD entrant is built to undercut.

**Key figures (Q1 2026, YoY).**
- Total revenue & reserve income: **$694.1M (+20%)**.
- Reserve income: **$652.5M (+17%)** = **94.0% of total revenue** — the dominant and nearly sole profit engine.
- Other revenue: **$42M (≈2x YoY)** — subscription & services $34.9M (blockchain partnerships) + transaction revenue $6.7M; still immaterial vs reserves.
- Net income (continuing ops): **$55M (-15%)** — profit fell despite +20% revenue.
- Adjusted EBITDA: **$151M (+24%)**, adj. EBITDA margin **53%**.
- Distribution, transaction & other costs: **$407M (+17%)**; operating expenses **$242M (+76%)**; adjusted opex **$136M (+32%)**.
- USDC in circulation (period-end): **$77.0B (+28% YoY)**; average USDC in circulation **+39% YoY**; onchain transaction volume **$21.5T (+263% YoY)**.
- **Reserve return rate: 3.5%, down 66 bps YoY** — the first-order driver of the revenue miss and net-income decline (lower SOFR).

**By segment / driver.** Reserve income (94% of revenue) is Circle's whole story; "other revenue" doubling to $42M is directionally healthy but far too small to diversify away from rate sensitivity. The margin problem is visible two ways: (1) reserve rate compression (-66 bps to 3.5%) means circulation growth of +28% only partly offsets a falling yield, hence revenue decelerating relative to volume; (2) operating expenses +76% YoY compressed GAAP net income to -15% even as adjusted EBITDA grew +24% — the gap is the de-PR'd signal (they lead with EBITDA, not with the net-income decline).

**vs expectations / prior period.** Revenue **missed** public consensus (Zacks ~$715.05M; moomoo aggregate ~$722.4M) by roughly **-2.9% / -$21M**, driven by the rate-return decline, not volume. EPS **beat** ($0.21 vs $0.15, +36.7%) on cost discipline/below-the-line items. YoY momentum: revenue +20%, USDC +28%, but net income -15% — growth is top-line/volume, not bottom-line. Prior-period corpus reference: [[Circle raises $222 million in Arc token presale at $3 billion valuation]] (2026-05, same print window — Circle is pivoting toward Arc/token and agentic-AI revenue precisely because reserve economics are rate- and competition-exposed). Market reaction to the print: CRCL fell ~3% on the revenue miss despite record USDC growth.

**Guidance / forward.** Management **affirmed** prior KPI guidance, explicitly *excluding* future ARC Token impacts and Arc revenue — i.e. the guided base case does not yet credit the new-revenue pivot, and says nothing about defending reserve-income share against Open USD. Management tone (CEO Jeremy Allaire): forward-looking toward "AI platforms and economic operating systems," steering the narrative to agentic/onchain volume ($21.5T, +263%) and away from the rate-sensitive reserve line. What they left out: no framing of reserve-rate sensitivity to further SOFR cuts, and no guidance on the Coinbase revenue-share renewal — both central to the Open USD threat.

**Thesis-flags (how exposed is Circle's reserve-income model to a bank-backed Stripe Open USD entrant?).**
1. **Single-revenue-stream concentration.** Reserve income = **94% of revenue**; the entire P&L rests on earning (and keeping) the yield on USDC reserves. Open USD's model, per CoinShares analyst Luke Nolan, is to **distribute reserve yield to participating businesses, keeping only a management fee** — a direct attack on the one line that is 94% of Circle's revenue. Second-order: if USDC distributors demand yield-sharing to match Open USD, Circle's take on each reserve dollar falls, compressing margin even if USDC circulation holds.
2. **Rate compression is already live, before competition.** Reserve rate fell **-66 bps to 3.5%** on lower SOFR, which already turned +28% circulation growth into a -15% net-income decline. A yield-sharing competitor stacks a *structural* margin headwind on top of a *cyclical* (rate) one. Second-order: in a falling-rate + yield-competition regime, Circle must grow circulation faster just to stand still.
3. **Distribution economics already heavily shared — ~50% to Coinbase.** CoinShares notes Coinbase takes **~half of USDC's reserve income** under the revenue-share agreement (renewal flagged around Aug 18). Open USD "strengthens Coinbase's hand" at renewal. Second-order: Circle is squeezed on both sides — a yield-sharing rival raising the price of distribution partners, while its largest partner already captures half the reserve income.
4. **Scale/moat as the counter-thesis.** USDC's $77.0B circulation (+28%), $21.5T onchain volume (+263%), deep liquidity and years of integrations are real switching costs; Open USD launched 2026-09-30 at only **~$468M in circulation** (announced vs adopted: ~160x smaller than USDC today). The near-term risk is to *pricing/margin* (forced yield-sharing) more than to *volume*; Circle's defense is the Arc/agentic pivot (not yet in guidance) to add non-reserve revenue before reserve economics erode.

Sources (primary + consensus/threat): Circle Q1 2026 press release (primary) https://www.circle.com/pressroom/circle-reports-first-quarter-2026-results · Q1 2026 Earnings Press Release PDF https://s206.q4cdn.com/265218871/files/doc_financials/2026/q1/FINAL_9_42-p-m-Q1-2026-EPR_May-2026-docx-2.pdf · 10-Q (period 2026-03-31) https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm · consensus/variance (as of 2026-05-11, public consensus — Zacks rev ~$715.05M, EPS $0.15) https://finance.yahoo.com/markets/stocks/articles/circle-q1-earnings-beat-estimates-144100086.html · thesis/threat framing CoinShares via CoinDesk (2026-07-15) https://www.coindesk.com/business/2026/07/15/open-usd-poses-biggest-threat-yet-to-circle-s-usdc-coinshares-says · Open USD launch (2026-09-30, ~$468M) https://ambcrypto.com/openusd-joins-the-stablecoin-race-goes-live-with-coinbase-mastercard-and-stripe/ · irdb semsearch DOWN (OpenRouter 402) — figures read from Circle IR release directly. Stripe (private) files no quarterly earnings; no reserve-income figures to review on its side.
<!-- /enrichment:earnings_review -->
