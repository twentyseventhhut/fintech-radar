---
title: "Anchorage launches tokenized deposit platform for banks"
date: 2026-06-24
tags:
  - company/anchorage
  - industry/blockchain
  - industry/banking
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/a29efb7e
  - https://www.futureofbanking.info/r/0da94ac3
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Future of Banking"
story_id: s75f5b3c8
month: 2026-06
enriched: true
importance: 3
---

# Anchorage launches tokenized deposit platform for banks

> [!info] 2026-06-24 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Future of Banking

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Anchorage aims to bring banks on-chain with a new tokenized deposit platform. The platform is designed to help financial institutions offer 24/7 payments and settlement services, reflecting growing interest in bringing regulated bank money onto blockchain-based rails without replacing existing core banking systems.

[Future of Banking] 🇺🇸 Anchorage aims to bring banks on-chain with a new tokenized deposit platform. The platform is designed to help financial institutions offer 24/7 payments and settlement services, reflecting growing interest in bringing regulated bank money onto blockchain-based rails without replacing existing core banking systems.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/a29efb7e>
- <https://www.futureofbanking.info/r/0da94ac3>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Anchorage launches tokenized deposit platform for banks
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On ~2026-06-22 Anchorage Digital Bank N.A. announced a **Tokenized Deposits infrastructure product**: turnkey tech that lets a regulated bank issue blockchain tokens representing its own customer deposits, without replacing its core banking system. Mechanically the chain is a **parallel ledger** — customer funds stay in the bank's existing demand-deposit accounts (DDAs); Anchorage provides the wallet/smart-contract layer and reconciles "Blockchain Deposit Accounts" against the DDAs; pitch is "go live in weeks, not a 3–7 year core rip-and-replace," with no customer PII leaving the bank. Pitched explicitly as "a regulated alternative to privately issued stablecoins."

**De-PR'd reality — this is a go-to-market announcement of infrastructure banks can buy, NOT a live network moving deposit volume:**
- **No named bank client or pilot disclosed.** Coverage (PYMNTS: "pilot and deploy"; CoinDesk quotes CEO Nathan McCauley on banks "we're starting to work with") is forward-looking. Source: [Anchorage PR](https://www.anchorage.com/insights/anchorage-digital-launches-tokenized-deposit-infrastructure-for-banks-delivering-24-7-settlement-without-replacing-core-systems), [CoinDesk](https://www.coindesk.com/business/2026/06/19/anchorage-aims-to-bring-banks-onchain-with-new-tokenized-deposit-platform), [PYMNTS](https://www.pymnts.com/blockchain/2026/anchorage-digital-introduces-tokenized-deposit-platform-for-banks/).
- **Chain not disclosed** (public vs permissioned, named L1/L2) — a material omission given JPM (Canton/Base) and ZKsync Prividium (regionals) are the two emerging camps.
- **Zero product metrics** (no TVL, no tx volume). The only numbers attached are corporate: $4.2B valuation, "tens of billions" assets under custody.
- → **Why framed this way:** Anchorage anchors to the bank's *own balance sheet preservation* fear (deposit flight to stablecoins) — the strongest sales hook to a CFO — and to the "no rip-and-replace" speed claim, because it has no live client to point to. The press-release weight rests on capability claims, not adoption.
- → **Second-order tension (analysis):** Anchorage simultaneously issues stablecoins (USDtb, Tether's USAT) *and* now sells deposit tokens as the "regulated alternative" to stablecoins. It is hedging both rails, so its "deposits-are-better" framing is self-interested in both directions.

## [1] Competitors / peers
Anchorage's lane is **infrastructure vendor selling to banks** — not a bank building its own coin in-house. Comparison must split those two groups.

**In-house bank builders (the volume leaders, not Anchorage's customers):**
- **JPMorgan Kinexys (ex-Onyx) / JPMD deposit token** — the only proven production scale: Kinexys >$3T cumulative, >$5B/day (caveat: that is all-Kinexys, JPMD-specific volume is undisclosed). JPMD went live on Base (public L2); native issuance on Canton announced Jan 2026. [JPM Kinexys](https://www.jpmorgan.com/kinexys/digital-payments/jpm-coin).
- **Citi Token Services** — live since 2023 pilot, permissioned, 24/7 cross-border; limited scope.
- **Consortia:** The Clearing House network (JPM/Citi/BofA/Wells) targeting H1 2027; five regionals (First Horizon, Huntington, KeyCorp, M&T, Old National) on ZKsync Prividium via Cari Network, pilot Q3 2026 / launch Q4 2026; HSBC piloted on Canton.

**Direct infra-vendor rivals (Anchorage's real fight):**
- **BitGo + ZKsync (Prividium), announced Mar 2026** — the closest analog and the key threat: also an OCC-chartered custody bank selling a turnkey "Bank Stack," and it **already has 5 named regional banks** ($600B+ deposits) committed. [CoinDesk](https://www.coindesk.com/business/2026/03/25/bitgo-teams-with-zksync-to-build-tokenized-deposit-infrastructure-to-bring-banks-onchain).
- **Fnality** (central-bank-reserve settlement, not commercial deposits), **Partior** (Singapore interbank), **Ownera/Broadridge** (interop/DLT settlement).
- → **Position: catching up, not first-mover.** BitGo/ZKsync preceded Anchorage by ~3 months *with named banks*; Anchorage launches with none. → **Why it matters (analysis):** in B2B infra, the first vendor with named reference banks usually wins the next cohort (procurement herds toward proven peers). Anchorage's credibility gap here is concrete, not cosmetic.

## [2] Company history / fit
Founded 2017 by Diogo Mónica and Nathan McCauley (ex-Docker security; McCauley CEO). Jan 2021: first OCC-chartered national crypto trust bank. Dec 2021: Series D $350M led by KKR, ~$3B valuation. 2024–25 stablecoin pivot: helped launch Ethena's USDtb (Dec 2024), became first GENIUS-pathway federally regulated stablecoin issuer one week after the GENIUS Act (signed 2025-07-18), and issuing bank for Tether's USAT. Feb 2026: Tether invested $100M at a $4.2B valuation (first employee tender; IPO chatter).
- This launch fits the trajectory tightly. Internal corpus confirms the build-up: [[Anchorage Digital Bank becomes first chartered stablecoin issuer]] (2025-08), [[Anchorage Digital to issue Tether's US stablecoin USAT]] (2025-09), and especially [[Anchorage Digital launches stablecoin settlement for banks]] (2026-02) — the bank-facing settlement product is the direct predecessor of this deposit-token product. Reserve/custody plumbing in [[US Bank to custody reserves for Anchorage Digital stablecoins]] (2025-10).
- → **Why Anchorage acts this way (analysis):** custody is a commoditizing, fee-compressing base. To earn a software multiple (and support a $4.2B mark / IPO narrative) Anchorage must move up-stack into recurring infrastructure that banks license. Deposit tokens are the natural next SKU after stablecoin-issuance and stablecoin-settlement — same buyer (banks), same regulated-bank credibility, higher stickiness.

## [3] Novelty / value-add / traction
What is genuinely new: not the concept (JPM/Citi have run deposit tokens for years) but **packaging it as turnkey infra for any regulated bank, balance-sheet-preserving and core-system-sparing.** That is a real product idea.
- **But traction = zero disclosed.** No live bank, no chain, no volume. Tokenized deposits broadly are still mostly pilots; JPM Kinexys is the lone proven volume. → "available/launched" here ≠ adopted.
- **Mechanism delta vs stablecoins (the real substance):** a tokenized deposit is an *on-balance-sheet bank liability* — the same insured deposit, just tokenized; it can bear interest and stays on the bank's books. A stablecoin is a *separate issuer's liability* backed by segregated reserves and, under the GENIUS Act, **cannot pay yield**. → **Why banks prefer deposit tokens:** no deposit flight (funding base preserved), interest-bearing, fits existing deposit/insurance law (FDIC 2026 NPRM proposes insurance "regardless of technology") rather than a new regime, keeps the customer relationship.
- → **Who captures the margin (analysis):** Anchorage wants to be the "AWS/Stripe for deposit tokens." But the big banks (JPM, Citi, the Clearing House consortium) build in-house and won't be customers; the addressable market is mid/regional banks — exactly the cohort BitGo/ZKsync already locked reference clients in. So the real question is not "is tokenized-deposit infra valuable" but "is there room for a *second* chartered-bank infra vendor once the first has named regionals" — Anchorage's value-add is unproven until it shows one live bank.

## [4] What's next / market sentiment
Watch for (a) Anchorage naming a first live bank — the single biggest credibility gap; (b) chain disclosure (Canton vs ZKsync-Prividium vs unnamed); (c) FDIC finalizing the "insurance regardless of technology" rule (de-risks adoption); (d) Anchorage IPO chatter post-Tether; (e) the dates that prove pilot→production: regional launches Q3/Q4 2026, Clearing House mega-network H1 2027.
Regulatory backdrop is favorable: GENIUS Act covers payment stablecoins only and deliberately leaves tokenized deposits under existing deposit law; OCC interpretive letters 1183/1184/1186/1188 (2025) broadly permit bank crypto activity — but these are interpretive letters, reversible by future leadership.
- → **Counterintuitive second-order effect (analysis):** the same favorable regime that lets Anchorage launch also lets every chartered bank and every rival vendor launch — so the moat is *speed-to-named-reference-banks*, not regulation. A crowded, fragmented field (Base vs Canton vs Prividium vs unnamed chains) raises an interoperability risk that no vendor, including Anchorage, has addressed. The structural winner is whoever achieves cross-network settlement, not whoever ships first.

## Sources
- [Anchorage tokenized-deposit PR](https://www.anchorage.com/insights/anchorage-digital-launches-tokenized-deposit-infrastructure-for-banks-delivering-24-7-settlement-without-replacing-core-systems)
- [CoinDesk — Anchorage tokenized deposit platform](https://www.coindesk.com/business/2026/06/19/anchorage-aims-to-bring-banks-onchain-with-new-tokenized-deposit-platform)
- [PYMNTS — Anchorage tokenized deposit platform](https://www.pymnts.com/blockchain/2026/anchorage-digital-introduces-tokenized-deposit-platform-for-banks/)
- [JPMorgan Kinexys / JPMD](https://www.jpmorgan.com/kinexys/digital-payments/jpm-coin)
- [BitGo + ZKsync tokenized-deposit infra](https://www.coindesk.com/business/2026/03/25/bitgo-teams-with-zksync-to-build-tokenized-deposit-infrastructure-to-bring-banks-onchain)
- [Anchorage + Ethena USDtb (GENIUS)](https://www.anchorage.com/insights/anchorage-digital-partners-with-ethena-labs-to-launch-first-genius-compliant-federally-regulated-stablecoin)
- [Tether $100M into Anchorage, $4.2B valuation](https://www.anchorage.com/insights/anchorage-digital-announces-100-million-strategic-investment-from-tether-first-ever-employee-tender-offer-4-2-billion-valuation)
- Internal: [[Anchorage Digital launches stablecoin settlement for banks]], [[Anchorage Digital Bank becomes first chartered stablecoin issuer]], [[Anchorage Digital to issue Tether's US stablecoin USAT]], [[US Bank to custody reserves for Anchorage Digital stablecoins]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5 — rationale:** A logical, credible product extension from a first-mover regulated crypto bank in a genuinely hot category (tokenized deposits). But it is an *announcement of infrastructure*, not adoption: no named bank client, no chain disclosed, zero volume — and a near-identical rival (BitGo + ZKsync, Mar 2026) already launched with five named regional banks. Real mechanism substance (deposit-token vs stablecoin distinction) and a strong company backstory keep it above a 2; absence of any traction and not-first-mover status keep it below a 4.

1. **Is the platform live with a paying bank?** — Open. No client disclosed; coverage says "pilot and deploy." Likely pre-production.
2. **Which blockchain — public or permissioned, named?** — Open. Not disclosed anywhere. Material omission.
3. **Any TVL or transaction volume for the product?** — No. Zero. Only corporate metrics ($4.2B valuation, "tens of billions" AUC).
4. **Are the deposit tokens FDIC-insured?** — Conditionally: FDIC's 2026 NPRM proposes insurance "regardless of technology," and Anchorage keeps funds in DDAs to preserve it — but final rule pending, so open in law.
5. **Does the GENIUS Act govern this product?** — No (verified). GENIUS covers payment stablecoins only; tokenized deposits fall under existing deposit law. This is precisely why banks like the structure (can bear interest, no new regime).
6. **Is Anchorage first to sell deposit-token infra to banks?** — No. BitGo + ZKsync (Mar 2026) preceded it with 5 named regionals. Anchorage is a fast-follower.
7. **Is "24/7 settlement" demonstrated or just a feature claim?** — Feature claim only. No live settlement evidence.
8. **Conflict: Anchorage sells both stablecoins and deposit tokens?** — Yes, confirmed. Issues USDtb/USAT yet pitches deposit tokens as "the regulated alternative to stablecoins." Treat its framing as two-sided self-interest.
9. **Did Tether's $100M (Feb 2026) drive this launch?** — Open. Tether is now a strategic investor and Anchorage issues USAT, but no disclosure ties Tether to the deposit-token product.
10. **Who actually has real tokenized-deposit volume today?** — JPMorgan Kinexys (>$3T cumulative, >$5B/day, though that is all-Kinexys not JPMD alone). Everyone else pilot/limited. JPMD-specific volume: open.
11. **Does "go live in weeks" hold up?** — Open. Unverified vendor claim; no bank has corroborated a timeline.
12. **Does it interoperate with JPMD/Canton/ZKsync networks?** — Open. Interoperability unaddressed; fragmentation (Base vs Canton vs Prividium vs unnamed) is a real risk and arguably the category's decisive battleground.
13. **Is the favorable OCC posture durable?** — Pro-crypto-bank via 2025 interpretive letters (1183/1184/1186/1188), but these are reversible by future leadership — favorable, not permanent.
14. **Did any outlet independently confirm a bank using it (vs reprinting the PR)?** — No. CoinDesk, PYMNTS et al. all trace to Anchorage's release; no independent bank confirmation. Open.
15. **What is the realistic addressable market?** — Mid/regional banks (big banks build in-house: JPM, Citi, Clearing House consortium). That cohort is exactly where BitGo/ZKsync already has reference clients, so Anchorage is competing for the *second-vendor* slot in a market it did not open. Real question shifts from "is the infra valuable" to "is there room for a second chartered-bank infra vendor without a single named live bank."
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Включено в дайджест [[Posts/2026-06-24]] (2026-06-24).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: tokenized deposits / on-chain regulated bank money — an infrastructure layer distinct from stablecoins (deposits stay inside the regulated bank as the underlying; the token is a representation). One paywalled secondary report (Dataintelo via WebSearch) sizes "tokenized deposits" at $4.8bn (2025) → $38.6bn by 2034, ~26% CAGR — treat as indicative only, single unverifiable source, not a TAM anchor. Better-attributed adjacent figure: Citi projects tokenized real-world assets growing from ~$17bn today to ~$5.5trn by 2030 (per Citi, via CoinDesk, 2026-06-01) — a different, broader pool. **Why now:** the demand driver is defensive — banks face deposit flight to yield-bearing stablecoins if the Clarity/GENIUS Act lets stablecoins pay returns (per WSJ via CoinDesk, 2026-06-05). Tokenized deposits are the banks' counter: keep money inside the regulated perimeter while matching stablecoins' 24/7, programmable, cross-border capabilities. **Structure:** the deposit-token rail itself is consolidating around the largest banks' own consortium ([[JPMorgan, BofA, Citi plan shared tokenized deposit network by 2027]]), but the *infrastructure* layer that smaller/regional banks need (wallets, smart contracts, settlement) is fragmenting across specialist vendors. Barrier to entry for the vendor layer is regulatory: Anchorage's OCC federal trust-bank charter ([[Anchorage Digital Bank becomes first chartered stablecoin issuer]]) is a genuine moat vs pure-software rivals.

**Competitive landscape.** Sector KPIs (mostly undisclosed here): AUC (assets under custody), settlement volume/TPV on rail, number of bank clients live, take rate on settlement — Anchorage disclosed none for this product [UNSOURCED]. Key players & basis of competition: (1) the big-bank consortium via The Clearing House, mid-2027 target ([[JPMorgan, Citi plan tokenized deposit network via Clearing House in 2027]]) — competes on owning both rail and deposits; (2) JPMorgan Kinexys / JPMD deposit token, already live and multi-chain ([[Why JPMorgan built Kinexys for institutional blockchain settlements]], [[JPMorgan expands JPM Coin to multiple blockchains]]) — the incumbent benchmark; (3) BitGo (with ZKsync) building bank-focused tokenized-deposit infra (per PYMNTS via WebSearch) — Anchorage's closest vendor-layer rival, both now OCC-chartered; (4) Fireblocks — chain-breadth infra. Basis of competition = regulatory perimeter + integration ("no core replacement") + chain coverage, not price. **Protagonist's position:** catching up / niche on the deposit-token product specifically — JPMorgan's deposit token is live, the bank consortium owns the deposits, whereas Anchorage targets the long tail of banks that lack their own chain. Anchorage's edge is sequencing: it already shipped stablecoin settlement for banks four months earlier ([[Anchorage Digital launches stablecoin settlement for banks]], 2026-02), so deposit tokens extend an existing bank-facing rail rather than a cold start (analysis). Moat = OCC charter + 8-yr custody track record (intangibles/regulatory), not network effects — it does not own the deposits.

**Comps & multiples.** Anchorage is private; no public multiple computable for it. Last marked round: $4.2bn post-money on Tether's $100M strategic investment ([[Tether invests $100M in Anchorage Digital at $4.2B value]], 2026-02) — round valuation, not market cap; revenue undisclosed, so EV/Revenue = no data. IPO speculation with a $200–400M raise ([[Anchorage Digital eyes $400M raise ahead of IPO]], 2026-01).
- **Anchorage** — $4.2bn last round (Feb 2026); rev [UNSOURCED] → multiple = no data.
- **BitGo** (closest vendor comp, OCC trust charter) — IPO Jan 2026 at $18/sh, ~$2.0bn valuation (per WebSearch). Closest public read-across; rev not captured → multiple = no data.
- **Fireblocks** — ~$8bn at 2022 Series E (per WebSearch); stale 2022 mark, private, no current multiple → no data.
- **Circle** (stablecoin issuer, adjacent not same model) — mkt cap ~$78bn area; FY2025 rev $2.75bn → P/S ~28x ($78bn / $2.75bn ≈ 28x), reported as trading ~32x revenue / 152x EBITDA (per Yahoo/coinmetrics via WebSearch). Cited only as a sector valuation-temperature gauge — Circle monetizes reserve float, a different model from Anchorage's custody/infra fees; NOT a clean comp.
Distribution not computed (≥3 comparable revenue figures unavailable) — qualitative only. Read: the crypto-infra/custody peer set (BitGo $2bn, Fireblocks $8bn-2022) brackets Anchorage's $4.2bn as plausibly in-line for a chartered, revenue-bearing custodian, but unverifiable without Anchorage revenue.

**Risk flags.**
1. **Disintermediation by its own customers.** The largest banks are building their own deposit-token rail via The Clearing House (mid-2027); they don't need Anchorage. Anchorage's addressable market is the smaller/regional banks left out of the consortium — a structurally lower-value tail, and one that may simply join the consortium's network later. Second-order: TAM for the vendor layer could compress as the bank-owned rail standardizes.
2. **Announced ≠ adopted.** No initial clients disclosed; product is in "pilot and deploy" stage (per WebSearch). Tokenized deposits are still pre-revenue at scale industry-wide; the launch is a positioning move, not proven traction.
3. **Regulatory/legislative dependency.** The entire "why now" rests on GENIUS/Clarity Act outcomes; the same legislation that pressures bank deposits could also let stablecoins out-compete tokenized deposits on yield, undercutting bank demand for Anchorage's rail. Concentration risk also: Tether is now both a strategic shareholder and a stablecoin issuer on Anchorage's platform — potential conflict if Anchorage's bank clients want stablecoin-agnostic neutrality.

**What this changes (idea-lens).** This is a land-grab for the *non-consortium* bank long tail, not a challenge to JPMorgan/Kinexys (analysis). Falsifiable thesis: if tokenized deposits standardize on the big-bank Clearing House network, independent infra vendors (Anchorage, BitGo) get squeezed into integration-plumbing for banks too small to matter — watch for whether any named, sizeable bank goes live on Anchorage's rail before mid-2027. Trigger that would break the bear case: a top-20 bank adopting Anchorage's deposit-token infra rather than waiting for the consortium. Catalyst to watch: Anchorage IPO timing — a filing would force first real revenue/AUC disclosure and let the $4.2bn mark be tested (analysis).

Sources: https://www.anchorage.com/insights/anchorage-digital-launches-tokenized-deposit-infrastructure-for-banks-delivering-24-7-settlement-without-replacing-core-systems · https://www.coindesk.com/business/2026/06/19/anchorage-aims-to-bring-banks-onchain-with-new-tokenized-deposit-platform · https://www.pymnts.com/blockchain/2026/anchorage-digital-introduces-tokenized-deposit-platform-for-banks/ · https://www.coindesk.com/markets/2026/06/05/jpmorgan-bank-of-america-and-citi-are-going-on-the-blockchain-offensive-with-a-shared-tokenized-network · https://www.coindesk.com/markets/2026/06/01/citi-predicts-the-tokenized-securities-market-will-grow-to-usd5-5-trillion-by-2030 · https://finance.yahoo.com/news/circle-hits-record-market-cap-210210106.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
