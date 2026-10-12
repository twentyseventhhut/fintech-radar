---
title: "ClearToken and Consensys bring 24/7 settlement to wholesale markets"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/cleartoken
  - company/consensys
  - industry/blockchain
  - industry/capital-markets
  - region/global
  - type/partnership
sources:
  - https://www.finextra.com/pressarticle/111198/cleartoken-and-consensys-bring-247-settlement-infrastructure-to-wholesale-markets
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s352dd12d
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# ClearToken and Consensys bring 24/7 settlement to wholesale markets

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌏 ClearToken and Consensys bring 24/7 settlement infrastructure to wholesale markets. The two companies are offering settlement infrastructure that runs around the clock for wholesale market participants. The collaboration was announced through a press release published on Finextra.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.finextra.com/pressarticle/111198/cleartoken-and-consensys-bring-247-settlement-infrastructure-to-wholesale-markets>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: ClearToken and Consensys bring 24/7 settlement to wholesale markets
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
ClearToken (London, FCA-authorised digital FMI; founded 2022; backed by XTX, Nasdaq, Nomura's Laser Digital) and **Consensys** (the Ethereum/Linea + MetaMask Institutional infrastructure firm) announced a **strategic partnership** to build 24/7/365 clearing-and-settlement infrastructure for tokenised securities and cash in wholesale markets. Announced early/mid-Oct 2026 (Finextra PR 2026-10-12; Finadium dates it 2026-10-08; MarketsMedia says 2026-09-10 — **date is reported inconsistently across outlets**; treat as a ~Oct-2026 announcement, analysis).
- **Division of labour (the actual substance):** Consensys supplies "**cryptographic finality**" (on-chain immutability) + tokenisation tech, cross-chain interoperability, wallets and institutional distribution/client reach. ClearToken supplies "**settlement finality**" — the *legal* certainty that a transfer is final and irrevocable within a UK-supervised perimeter. The PR's framing (crypto-finality vs legal-finality) is the one genuinely informative line: it concedes that an on-chain confirmation is **not** legally final, which is exactly the gap a regulated FMI is needed to close.
- **Regulatory anchor:** **ClearToken CSD Limited** holds **Gate 2 approval** in the Bank of England's Digital Securities Sandbox (DSS) — designed to let eligible securities held at different banks be tokenised and recognised as a single fungible instrument. Settlement is DvP against cash (fiat, tokenised deposits, stablecoins) via **ClearToken Depository Limited** (FCA-authorised payment institution). ClearToken is *still pursuing* BoE clearing authorisation (CT Clear / CCP).
- **Live vs announced:** This specific tie-up is **"being built"/"aiming to"** — planned, NOT live. No named banks, no launch date, no volume target, no commercial terms disclosed. The only genuinely *live* component underneath is **CT Settle** (launched Dec 2025). **+ Why structured this way:** ClearToken is deliberately multi-chain — it already deployed on **Canton** (March 2026, [[ClearToken launches CT Settle multi-currency settlement solution]]); now it adds the Ethereum/Consensys stack. The "neutral FMI across chosen networks" posture is a bet that no single institutional chain wins → ClearToken wants to be the regulated settlement layer *regardless* of which ledger banks pick.

## [1] Competitors / peers
- **Fnality** — Sterling Fnality Payment System live since Dec 2023 via a BoE omnibus account with settlement-finality designation; raised $136m Series C (Sep 2025). Closest UK peer and arguably **ahead on regulatory status** (actual RTGS-backed settlement asset live), though still waiting on BoE intraday-repo permission and a Fed decision for USD.
- **Partior** (DBS/JPM/Temasek, + Standard Chartered, Deutsche Bank) — live multi-currency (USD/EUR/SGD); Deutsche Bank's first euro payment Sept 2025. Settles in **commercial-bank money** (bank credit risk remains) — a mechanism difference vs ClearToken's DvP/PvP ambition.
- **Canton Network / Digital Asset** — the institutional-blockchain heavyweight (DTCC, Goldman, BNP Paribas, BNY Mellon; HSBC tokenised-deposit service; Broadridge repo billions/day). ClearToken is a *participant* on Canton, so Canton is **both a venue and a rival settlement narrative**.
- Adjacent: Nasdaq/Boerse Stuttgart tokenised settlement ([[Nasdaq and Boerse Stuttgart partner on tokenized settlement in Europe]]), JPMorgan Kinexys ([[Qatar National Bank taps JPMorgan Kinexys for dollar settlements]]).
**+ Why the landscape looks this way:** incumbents split into (a) bank-money rails (Partior, Kinexys) carrying issuer credit risk, and (b) central-bank/omnibus rails (Fnality) with true finality but narrow currency/scope. ClearToken's pitch is a **neutral, FCA/BoE-supervised DvP+PvP layer that spans fiat, tokenised deposits, stablecoins AND crypto across multiple chains** — broader than any single incumbent, but it is the **least live** of the group. Position: catching up on traction, ahead on breadth-of-scope ambition.

## [2] Company history / fit
- Oct 2025: FCA authorisation for CT Settle (DvP for crypto/stablecoin/fiat) — [[ClearToken wins FCA approval]].
- Dec 2025: CT Settle **launched**; multi-currency DvP/net settlement live.
- March 2026: strategic partnership + deployment on **Canton Network** (CT Register/CT Pay/CT Settle as Daml DAPs) — [[ClearToken launches CT Settle multi-currency settlement solution]].
- Oct 2026: Consensys partnership (this item) — extends the same horizontally-integrated FMI roadmap (tokenise → pay PvP → settle DvP → clear) onto the Ethereum/Linea ecosystem.
**+ Why ClearToken acts this way:** its moat is the **FCA licence + BoE DSS/CCP pipeline**, not a chain. So the logical play is to be chain-agnostic and sign every major institutional ledger (Canton, now Ethereum/Consensys) → each partnership is distribution, not a pivot. Structural pressure: a settlement utility needs *network reach* to matter, and reach comes from being on whatever rail the banks already chose.

## [3] Novelty / value-add / traction
- **Genuinely new here:** the specific ClearToken↔Consensys relationship and the Ethereum/Linea distribution channel + MetaMask Institutional wallet reach. The *concept* (regulated 24/7 DvP for tokenised assets/cash) is **not** new — it is ClearToken's existing roadmap, already announced for Canton in March 2026.
- **Traction = thin.** No banks, no live transactions on this stack, no dates, no volume. CT Settle (live Dec 2025) is the only shipped piece; adoption numbers undisclosed. Everything about *this* partnership is "aiming to."
**+ Where the margin sits:** value accrues to whoever owns **legal settlement finality + the regulated cash leg** — that is ClearToken's claim. Consensys is the tech/distribution layer. The risk: if banks settle in central-bank money via Fnality or stick to Canton's atomic settlement, ClearToken's separate "legal-finality" layer may be bypassed. The multi-chain neutrality that is its strength is also its weakness — it has **no exclusivity** with any chain or bank.

## [4] What's next / market sentiment
- Watch for: BoE clearing/CCP authorisation (CT Clear) — the real unlock; DSS Gate 2 → Gate 3 progression; first *named* bank and first *live* transaction on the Consensys stack.
- Regulatory backdrop favourable: UK DSS, BoE weekend-RTGS consultation ([[Bank of England proposes weekend RTGS and CHAPS settlement]]), MiCA in the EU — the "always-on wholesale settlement" thesis is well-supported structurally.
**+ Counterintuitive second-order:** the more chains and FMIs that launch, the more a **neutral legal-finality layer** matters (fragmentation creates demand for an interoperable settlement backstop) — but that same fragmentation means ClearToken must win on *every* chain to be relevant, and any one chain achieving its own credible finality (e.g. Canton + central-bank cash) erodes the need for a separate layer. The central question is less "is 24/7 tokenised settlement coming" (yes) than "**does the regulated legal-finality layer get captured by an independent FMI (ClearToken) or absorbed by the chains/CSDs themselves**."

## Sources
- Finextra PR: https://www.finextra.com/pressarticle/111198/cleartoken-and-consensys-bring-247-settlement-infrastructure-to-wholesale-markets
- Finadium: https://finadium.com/cleartoken-and-consensys-team-up-for-24-7-wholesale-settlement/
- MarketsMedia: https://www.marketsmedia.com/cleartoken-consensys-bring-24-7-wholesale-settlement-infrastructure/
- Crypto Briefing: https://cryptobriefing.com/consensys-cleartoken-24-7-settlement-partnership/
- Prior: CoinDesk FCA approval https://www.coindesk.com/policy/2025/11/11/cleartoken-wins-uk-regulator-approval-for-digital-asset-settlement-service
- Prior: ClearToken/Canton PR https://cleartoken.io/news/press-releases/cleartoken-launches-regulated-stablecoin-fx-and-tokenised-settlement-on-canton-network/
- Competitors: Fnality Series C https://www.theblock.co/post/371889/fnality-raises-136-million-series-c-to-expand-settlement-rails-for-tokenized-markets

### Related internal notes
- [[ClearToken wins FCA approval]]
- [[ClearToken launches CT Settle multi-currency settlement solution]]
- [[Nasdaq and Boerse Stuttgart partner on tokenized settlement in Europe]]
- [[Bank of England proposes weekend RTGS and CHAPS settlement]]
- [[UK names six banks for first digital gilt issuance]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is this actually new vs the March 2026 Canton deployment?** Partly — same FMI roadmap and same DvP-against-cash model, but a genuinely new partner (Consensys/Ethereum-Linea) and distribution channel. Fresh, not a reprint. (answered)
2. **What is live vs announced?** Only CT Settle (live Dec 2025). The Consensys stack is "being built / aiming to" — no live transactions. (answered)
3. **Which exact date?** Reported inconsistently: MarketsMedia 2026-09-10, Finadium 2026-10-08, Finextra PR carried 2026-10-12. Open — treat as ~early-Oct 2026 announcement.
4. **Is Linea specifically named?** Finadium/MarketsMedia describe Consensys generically (tokenisation tech, interop, wallets); Linea is the implied Consensys L2 but not explicitly the settlement chain in the cited coverage. Open.
5. **Any named participating banks?** No. None disclosed by any outlet. (answered — none)
6. **Volume/revenue targets or commercial terms?** None disclosed. (answered — none)
7. **What does ClearToken actually own that Consensys doesn't?** The FCA licence + BoE DSS Gate 2 (CSD) + CCP pipeline = legal settlement finality + regulated cash leg. That is the defensible asset. (answered)
8. **Is "cryptographic finality vs settlement finality" real or PR?** Real distinction — on-chain confirmation is not legally final; it is the actual reason a regulated FMI is needed. The one substantive line in the PR. (answered)
9. **How does this beat Fnality?** It may not on finality — Fnality has a live BoE omnibus-account settlement asset (true central-bank money finality) since Dec 2023. ClearToken claims broader scope (crypto/stablecoin/tokenised deposits, multi-chain) but less live traction. Open on who wins.
10. **Does Partior/Kinexys (bank-money rails) make this redundant?** No — those carry settlement-bank credit risk; ClearToken targets DvP/PvP with finality. Different mechanism. (answered)
11. **Exclusivity?** None with Consensys or with any chain — ClearToken is deliberately multi-chain (Canton + now Consensys). Strength and weakness. (answered)
12. **What could kill the value-add?** A chain achieving credible atomic settlement with central-bank/tokenised-deposit cash (e.g. Canton + HSBC TDS) could absorb the "legal-finality layer" and bypass an independent FMI. (analysis)
13. **Is CT Clear (the real unlock) approved?** No — still pursuing BoE CCP authorisation/Recognised Clearing House status. The highest-value piece is not yet granted. (answered)
14. **Who needs whom more?** Consensys needs a regulated settlement/cash leg to sell institutional tokenisation; ClearToken needs chains + distribution to matter. Roughly symmetric, but Consensys has many other institutional plays (MetaMask Institutional, Linea). Open.
15. **MiCA relevance?** One search result mentioned MiCA standards for the stablecoin cash leg; not confirmed in primary coverage. Open.

Importance: 3/5 — Credible, well-regulated player (FCA-authorised, BoE DSS Gate 2) extending its FMI onto a second major institutional chain (Consensys/Ethereum after Canton), in a structurally important and crowded wholesale-settlement race. But it is a strategic partnership with zero disclosed traction: no banks, no dates, no volumes, no commercial terms, and the highest-value component (CCP/CT Clear) is still unapproved. Real but incremental; the "news" is distribution reach, not a shipped product.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-12]] (2026-10-12).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Tokenised wholesale settlement / digital-asset clearing & settlement. Size: tracked tokenised real-world assets (ex-stablecoins) ~$27–38bn on-chain as of mid-2026, underlying ~$305bn; tokenised US Treasuries the largest single bucket at ~$15.7bn (~40%), tokenised private credit ~$8bn (per Pantera Q1 2026 / RWA.xyz data, via Forbes 2026-07-02 and InvestaX). Cumulative wholesale settlement is further along than stock: J.P. Morgan's Kinexys has settled >$1.5tn cumulatively (via Forbes 2026-07-02). Structure: concentrated at the infrastructure layer (a handful of ledgers — Canton, Kinexys, Fnality, Partior — plus CSDs/CCPs), with high regulatory + capital barriers; value sits in being the legally-recognised settlement venue, not in the chain itself. "Why now": (1) the Bank of England Digital Securities Sandbox (DSS) is handing out live-operation approvals — ClearToken passed "Gate 2" in Sept 2026 as the second firm and first non-bank through, cleared to settle FTSE 350 equities, GBP gilts and corporate bonds (via Crowdfund Insider / A-Team, 2026-09); (2) the market's own complaint is that ~$60bn of tokenised assets mostly isn't moving (Forbes 2026-07-02) — a settlement/liquidity problem this deal targets directly.

**Competitive landscape.** Sector KPIs: cumulative/annual value settled, assets eligible (securities classes live), settlement finality latency (T+0 / 24-7 vs T+1), and connected institutions. Players & basis of competition: Fnality (central-bank-money sterling settlement, $136M Series C Sep 2025 from BofA/Citi/WisdomTree/Temasek/Tradeweb — see internal comps), Digital Asset/Canton (regulated capital-markets ledger), J.P. Morgan Kinexys (bank-captive, >$1.5tn cumulative), Partior (cross-border bank payments), plus incumbent CSDs (Euroclear, DTCC piloting tokenisation). Competition is on legal recognition + institutional distribution, not price. Recent move: ClearToken + Consensys announced 2026-10-08 — pairs Consensys' cryptographic finality (Linea/Ethereum stack) with ClearToken's settlement (legal) finality, aiming for 24/7 DvP against fiat, tokenised deposits and stablecoins (via Markets Media / Finadium, 2026-10). ClearToken's position: niche but structurally advantaged — it is a regulated CSD (ClearToken CSD Ltd) with a pending CCP application at the BoE, i.e. moving toward the full clearing+settlement stack most rivals lack; moat = regulatory licence + central-bank sandbox status (switching/regulatory barrier) `(analysis)`.

**Comps & multiples.** No public multiples: ClearToken, Consensys, Fnality, Digital Asset and Partior are all private; no revenue/EBITDA disclosed → EV/Revenue, EV/EBITDA, P/E = no data. Round-valuation reference points only (not market caps):
- [[DRW-backed Digital Asset raising funds at $2 billion valuation]] — Canton operator, reported ~$2bn round valuation (2026-05).
- [[Digital Asset raises $355 million led by a16z crypto for Canton]] — $355M round, backers incl. HSBC, BNP Paribas, Citadel Securities, Apollo, CME Ventures, S&P Global (2026-06).
- [[Fnality raises $136M for blockchain bank settlement]] — $136M Series C (2025-09), prior $95M (2023); bank/asset-manager syndicate.
- ClearToken itself: only a ~$10M seed (2024, Nomura Laser Digital, Zodia/SC Ventures, Flow Traders, LMAX Digital, GSR) is on record (via CoinDesk / Ledger Insights 2024) — an order of magnitude below Digital Asset/Fnality.
Internal precedent on the DvP/settlement theme: [[Lloyds completes UK's first tokenized-deposit gilt purchase]], [[DTCC pilots asset tokenisation with JPMorgan, Goldman, BlackRock]]. Distribution not computed (no comparable $ figures); qualitative only — ClearToken is capital-light vs peers, which is a risk, not a valuation.

**Risk flags.**
1. Sandbox-bound, not production — "Gate 2" DSS approval carries operational limits and the CCP licence is still pending; this is "approved to settle in a sandbox," not an at-scale live utility. Second-order: timeline/regulatory slippage could let better-funded rivals (Fnality, Digital Asset) reach scale first.
2. Capital/distribution gap — ClearToken's ~$10M seed is tiny next to Digital Asset (~$2bn val) and Fnality ($136M C) and it lacks their bank-equity syndicates; a settlement utility lives or dies on connected institutions, where it is behind. Second-order: may be forced to partner/sell rather than win independently.
3. Economics + liability silent — the PR discloses no fees, revenue split with Consensys, or who bears settlement-failure/finality-dispute liability; "settlement finality" is asserted via sandbox rules, not yet battle-tested in a default. Second-order: legal finality untested in court = the core selling point is still a claim.

**What this changes (idea-lens).** `(analysis)` Signals the tokenised-settlement race is shifting from "can we tokenise?" to "who is the regulated settlement rail" — ClearToken is positioning as the neutral, non-bank CSD/CCP alternative to bank-captive rails (Kinexys) and consortium ledgers (Canton/Fnality). Falsifiable thesis: if ClearToken converts the DSS approval into a live, bank-connected 24/7 DvP service with named institutional flow within ~12 months, it re-rates as credible infrastructure; trigger to watch = BoE CCP authorisation + first live production settlements with named banks. What breaks the thesis: CCP application stalls, or a better-capitalised rail (Fnality/Canton) wins the same banks first, leaving ClearToken a sub-scale niche.

Sources: https://www.forbes.com/sites/astanley/2026/07/02/the-tokenized-asset-market-is-60-billion-most-of-it-isnt-moving/ · https://investax.io/blog/q1-2026-real-world-asset-tokenization-market-report · https://www.marketsmedia.com/cleartoken-consensys-bring-24-7-wholesale-settlement-infrastructure/ · https://finadium.com/cleartoken-and-consensys-team-up-for-24-7-wholesale-settlement/ · https://www.crowdfundinsider.com/2026/09/312066-cleartoken-joins-bank-of-england-digital-securities-sandbox/ · https://a-teaminsight.com/blog/cleartoken-gains-uk-regulatory-approval-to-operate-digital-securities-depository/ · https://www.ledgerinsights.com/cleartoken-raises-10m-for-digital-assets-central-clearing-from-nomura-stanchart-subsidiaries/ · IR: https://consensys.io/blog/how-consensys-and-ethereum-made-2025-cryptos-most-important-year
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news** — this is a partnership/product announcement (24/7 wholesale settlement infrastructure), not a results release. Consensys is a private company and files no quarterly financials; the IR corpus (`ir/ir_latest.json["consensys"]`) carries only blog posts, press releases and surveys (latest: annual review 2025-12-18 "How Consensys and Ethereum made 2025 crypto's most important year"), with **no revenue / profit / EPS disclosures**. The figures below are third-party / public reporting, cited only as strategic weight — not audited or IR-filed.

**Strategic-weight context (public estimates, not reported results).**
- Valuation: ~$7bn as of the $450m Series D in early 2022; total raised ~$725m across 6 rounds. Press reports a targeted IPO (JPMorgan / Goldman Sachs) now pushed to H2 2027 at ~$8bn (delayed from a fall-2026 plan on weak market conditions). A fresh, undisclosed-size investment from NYSE-listed C1 Fund was announced 2025-12-15. `(all third-party — [UNSOURCED] vs IR)`
- Revenue: ~$91m est. ARR reported (getlatka, Sept 2025); no official figure, no YoY growth disclosed. [UNSOURCED]
- Operating scale: MetaMask ~30m+ MAU (~80% of the Web3-wallet market per reporting); Infura ~10bn daily requests; Linea zkEVM. Headcount ~766.
- Structure: Consensys has announced a split — MetaMask spinning out as an independent consumer-wallet company, with Consensys retained as protocols + **institutional infrastructure** (directly the ClearToken partnership's lane). `(context for strategic fit)`

**Why it matters for this partnership.** The 24/7 wholesale-settlement tie-up with ClearToken sits squarely in the "institutional infrastructure" half of Consensys post-split, and bolsters the Linea/enterprise narrative that Wall Street is being asked to underwrite for the 2027 IPO — i.e. a credibility/revenue-diversification signal ahead of a listing, more than a near-term P&L event. Second-order: no disclosed economics (fees, volume commitments) for the deal, and no Consensys margin/segment data exists to size it — so the strategic read stays qualitative. De-PR flag: "settlement infrastructure for wholesale markets" is announced, not yet evidenced as live production volume; no counterparties, go-live date, or throughput numbers were given.

Sources: IR `ir/ir_latest.json["consensys"]` (no financials) · https://consensys.io/blog/how-consensys-and-ethereum-made-2025-cryptos-most-important-year · https://getlatka.com/companies/consensys.io · https://en.wikipedia.org/wiki/Consensys · https://www.coindesk.com/business/2026/05/13/ethereum-app-builder-consensys-has-delayed-its-potential-ipo-until-fall · https://ventureburn.com/consensys-ipo-jpmorgan-goldman/ — revenue/valuation/round-size [UNSOURCED] (no IR-filed results; Consensys is private).
<!-- /enrichment:earnings_review -->
