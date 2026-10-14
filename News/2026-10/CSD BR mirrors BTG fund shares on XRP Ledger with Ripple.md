---
title: "CSD BR mirrors BTG fund shares on XRP Ledger with Ripple"
date: 2026-10-07
retrieved: 2026-10-08
tags:
  - company/csd-br
  - company/ripple
  - industry/blockchain
  - industry/capital-markets
  - region/latam
  - type/product
sources:
  - https://www.letsmoney.com.br/cripto/csd-br-ripple-fundos-btg-blockchain
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sfab0cab4
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# CSD BR mirrors BTG fund shares on XRP Ledger with Ripple

> [!info] 2026-10-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] 🇧🇷CSD BR, a Brazilian securities depository, began mirroring ownership records of BTG Pactual fund shares on the public XRP Ledger with Ripple, so authorized participants can check the blockchain copy against the official record in near real time.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.letsmoney.com.br/cripto/csd-br-ripple-fundos-btg-blockchain>

## Контекст

<!-- enrichment:context -->
**[0] TL;DR.** CSD BR — a Brazilian central securities depository (CSD) and would-be B3 rival — has gone live mirroring ownership records of selected BTG Pactual investment-fund shares onto the public XRP Ledger (XRPL) using Ripple's custody stack and XRPL's Multi-Purpose Token (MPT) standard. CSD BR's own systems remain the legally official registry for registration, deposit and settlement; the XRPL copy is an additional, near-real-time verification/audit layer that authorized participants can reconcile against the official record. Ripple frames it as the first time a licensed CSD records securities ownership on a *public* blockchain.

**[1] Who / what.**
- **CSD BR** (Central de Serviços de Registro e Depósito aos Mercados Financeiro e de Capitais), founded 2018, licensed by Brazil's central bank (BCB), securities regulator CVM and insurance regulator Susep for registration, deposit and settlement. It markets itself as a challenger to the B3 exchange monopoly (it filed the 2022 CADE antitrust complaint against B3) and holds licenses to eventually operate a competing exchange. Reported >BRL 22 trillion in *registered* assets and ~R$100bn in 2026 settlements. In 2025 Citi, Morgan Stanley and UBS invested ~R$100m as strategic backers.
- **BTG Pactual** — large Brazilian investment bank; the pilot mirrors a subset of its fund shares (not the full BRL 22T book).
- **Ripple** — provides digital-asset custody infrastructure; XRPL provides the public ledger and the MPT token standard (supports KYC/AML/transfer controls, authorized-only access).

**[2] Dated timeline.**
- 2022 — CSD BR complaint triggers CADE probe of B3 (positions CSD BR as the challenger).
- 2025 — Citi/Morgan Stanley/UBS invest ~R$100m in CSD BR.
- 2026-03-18 — Ripple "goes all-in on Brazil," expanding payments/custody/prime/treasury (see [[Ripple deepens Brazil commitment with expanded payments offering]]).
- 2026-09-29 — Ripple + CSD BR announce the BTG fund-share mirroring on XRPL (MPT + Ripple custody); Ripple's account amplifies 2026-09-30 as the first licensed CSD recording securities ownership on a public chain.
- 2026-10-07 — date on this note (digest pickup via This Week in Fintech / letsmoney.com.br).

**[3] Why it matters.**
- Makes Brazil the single largest reported RWA concentration on XRPL (~US$2.7bn), part of XRPL crossing ~US$3bn tokenized RWA in 2026 — strategic proof-point for Ripple's institutional/RWA narrative beyond RLUSD payments.
- A *licensed* CSD using a *public* L1 (vs. the permissioned-DLT path favored by DTCC/Euroclear/Clearstream under CSDR) is a notable divergence in market-infrastructure design. Contrast: DTCC is routing its 2026 tokenization service to Stellar (public), while Clearstream sticks to permissioned Besu.
- For CSD BR specifically, the public-chain differentiation is a competitive wedge against incumbent B3.

**[4] Open questions / what to watch.** Whether phase 2 (native issuance + on-chain trading of CRI/CRA receivables) actually ships; regulatory comfort (CVM/BCB) with ownership mirrored on a permissionless chain; how "near real-time reconciliation" is enforced if the official record and the mirror diverge; whether BTG expands beyond the pilot funds; adoption by the "authorized participants."

**Related internal notes:** [[Ripple deepens Brazil commitment with expanded payments offering]] · [[Sygnum brings Fidelity tokenized liquidity fund to Singapore]] · [[Ondo launches Ondo Private Markets for tokenized exposure]] · [[Standard Chartered adds custody support for Ripple's RLUSD]] · [[BNY Mellon reportedly adds XRP to corporate payments roadmap]]

**Sources:**
- https://www.letsmoney.com.br/cripto/csd-br-ripple-fundos-btg-blockchain
- https://usethebitcoin.com/news/xrp-ledger-brazil-csd-br/
- https://cryptoslate.com/ripple-quietly-made-brazil-the-center-of-its-xrpl-tokenization-push/
- https://www.cryptoninjas.net/news/brazils-brl-22t-csd-br-moves-fund-records-to-xrp-ledger-in-live-tokenization-push/amp/
- https://www.seudinheiro.com/2025/bolsa-dolar/outra-rival-para-a-b3-csd-br-recebe-r-100-milhoes-do-citi-morgan-stanley-e-ubs-para-criar-nova-bolsa-no-brasil-paty/
- https://www.ledgerinsights.com/clearstream-dtcc-euroclear-propose-approach-to-tokenization-interoperability/
- https://www.dtcc.com/press-releases/2026/tokenization-service-to-connect-with-stellar-public-blockchain-as-dtc-advances-multi-chain-strategy
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. "Mirroring" vs "tokenization": is this a legally transferable on-chain security, or just a read-only audit copy? The sources say CSD BR keeps the official record and XRPL is an *additional* layer — so what actually moves on-chain, and can anything settle there?
2. Scale framing risk: headlines lead with "BRL 22 trillion CSD" but only a subset of BTG fund shares is in the pilot. How much notional is actually mirrored? (Likely tiny.)
3. "First licensed CSD on a public blockchain" — is this claim verifiable, or Ripple marketing? Does it survive once you account for other public-chain CSD pilots (e.g., SDX, prior XRPL/Stellar institutional trials)?
4. Is this live production or a "live test"/pilot? Yahoo headline says "live XRPL test." Materiality hinges on this distinction.
5. Primary-source gap: the note's only source is a Brazilian crypto outlet (letsmoney). Is there a Ripple press release or CSD BR/BTG official statement? (Ripple amplified Sept 29-30 but a formal PR URL wasn't captured.)
6. Why public XRPL rather than permissioned DLT, when DTCC/Euroclear/Clearstream lean permissioned under CSDR-style rules? What regulatory cover (CVM/BCB) permits ownership data on a permissionless chain?
7. Privacy/confidentiality: fund-share ownership on a public ledger — how is counterparty/holding confidentiality preserved? MPT controls access, but is ownership mapping leaked?
8. Reconciliation failure mode: if the XRPL mirror diverges from the official CSD record, which wins and who bears the risk? "Near real-time" implies lag windows.
9. Ripple-interest bias: much coverage is XRP-price-oriented ("Can XRP catch up?"). Separate infrastructure substance from token-pump narrative.
10. Competitive reality: CSD BR vs B3 — does a blockchain mirror meaningfully erode B3's moat, or is it a PR differentiator with negligible volume?
11. Dependency on Ripple custody: vendor lock-in and what happens to the records if Ripple's custody stack changes or is deprecated.
12. Phase-2 vaporware risk: native issuance + CRI/CRA trading are "planned/explored." Any committed timeline, or aspirational?
13. Date discrepancy: announcement Sept 29-30 vs note date Oct 7 — is the note capturing a fresh event or a re-surfaced one in digests?

**Importance: 3/5** — A licensed CSD putting real (if pilot-scale) securities ownership on a *public* L1 is a genuinely notable market-infrastructure signal and a strong proof-point for Ripple's RWA/institutional thrust in Brazil (now XRPL's biggest RWA hub). Capped below 4/5 because it is an early pilot/mirror (not transferable on-chain settlement), tiny notional relative to the BRL 22T headline, single secondary source, and heavy XRP-token-price framing in coverage.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** RWA / fund-share tokenization. On-chain RWA (ex-stablecoins) crossed ~$30–31bn by mid-2026 (per rwa.xyz/CoinGecko citations, via Unchained/crypto.news, as of Jul 2026), up >400% from early 2025; tokenized Treasuries (~$10bn) and private credit (~$8bn) dominate, fund shares/equities are the long tail. The XRP Ledger specifically held ~$4.18bn of tokenized RWA by Jun 2026 vs ~$147M a year earlier — a ~28x jump, ranking it ~6th among chains (per kucoin/thecryptobasic, via finbold, Jun–Aug 2026). Structure: securities-depository plumbing is a consolidated, utility-like layer (one national CSD per market, high regulatory barriers); value accrues to the record-of-truth operator, not to the chain. **Why now:** a confluence of institutional rails going live in 2026 — DTCC's tokenization program (Ripple Prime alongside BlackRock/JPMorgan, limited live trades Jul 2026, scale Oct 2026) and Ripple's licensing push (MiCA CASP, UK FCA, Luxembourg EMI per ir/ripple) — makes a public-chain "mirror" of a regulated book credible rather than experimental. Note: the deal is a *mirror/audit* layer (XRPL Multi-Purpose Token standard), explicitly **not** a replacement of CSD BR's core systems — "live test," not production settlement.

**Competitive landscape.** Sector KPIs: assets-under-custody/registered (depository), on-chain RWA value + holder count (chain adoption), settlement latency. CSD BR carries >R$22tn (~$4.2tn) in registered assets (per Unchained, as of Oct 2026) — the scale that makes this notable vs the ~$4bn total currently on XRPL. Key players on the "where do institutional books live on-chain" question: public-chain mirrors/issuance (Ripple/XRPL here; [[Ondo launches Ondo Private Markets for tokenized exposure]]; [[Sygnum brings Fidelity tokenized liquidity fund to Singapore]]) vs incumbent CSDs building private/permissioned rails (Clearstream, DTCC's own program). Basis of competition: regulatory trust + distribution to existing custodians, not chain throughput. Recent dated moves: Standard Chartered added RLUSD custody ([[Standard Chartered adds custody support for Ripple's RLUSD]]); BNY reportedly mapping XRP into corporate payments ([[BNY Mellon reportedly adds XRP to corporate payments roadmap]]); Ripple's Garanti/Turkey push ([[Ripple targets Turkey crypto market with Garanti BBVA]]) — Ripple signed multiple institutional deals the same week (247wallst, 8 Oct 2026). Protagonist position: CSD BR is the *incumbent* taking a cautious first step; Ripple is the infrastructure vendor racing BlackRock/JPMorgan/DTCC for institutional mind-share — ahead on LatAm distribution, catching up on the global tokenization stack (analysis). Moat = CSD BR's regulatory monopoly on the Brazilian record-of-truth; Ripple's is thinner (switchable rails).

**Comps & multiples.** No deal value/round disclosed for this partnership — a product pilot, not a financing → valuation multiples **not computed**. Vendor comp (IR-grounded): Ripple is private, publishes no revenue and stopped disclosing XRP holdings (May 2025) → revenue/EBITDA multiples = **no data**. Reference valuation: $40bn post-money on the $500M Fortress/Citadel round (per ir/ripple funding_announcement, 5 Nov 2025; https://ripple.com/ripple-press/ripple-announces-500-million-strategic-investment-led-by-fortress-citadel-securities-valuing-the-company-at-40-billion-following-record-growth/), reportedly re-marked to ~$50bn via a self-tender buyback (Mar 2026, per unicorn-club — mark as internal buyback price, not a market clearing). RLUSD ~$2.4bn market cap (per rwa.xyz/kucoin, Sep–Oct 2026) frames Ripple's stablecoin scale but is not a comp for a depository mirror. Internal RWA-issuance comps as qualitative reference (no public multiples): [[Ondo launches Ondo Private Markets for tokenized exposure]], [[Sygnum brings Fidelity tokenized liquidity fund to Singapore]]. Distribution not computed — <3 comparable figures; qualitative only.

**Risk flags.**
1. **"Mirror ≠ settlement" — thin economics.** The XRPL copy audits ownership but does not replace CSD BR's core book; until native issuance/trading (receivables certificates are the stated next step), it adds a parallel ledger with limited revenue and real reconciliation/dual-source-of-truth risk if the mirror and the official record diverge.
2. **Single-issuer, single-market concentration.** Phase one is one issuer (BTG Pactual funds) in one jurisdiction on a permissioned (KYC/AML-gated) basis; adoption/regulatory validation by Brazil's CVM/B3 ecosystem is unproven — a pilot that stalls leaves the "first CSD on a public chain" headline unmonetized.
3. **Rail dependence / disintermediation.** CSD BR, as a regulated monopoly, can swap XRPL for a private chain or DTCC's program with low switching cost; Ripple captures distribution now but the moat sits with the depository, and XRPL's ~$4bn RWA base is small vs incumbent post-trade stacks — value could migrate to whoever the CSD ultimately standardizes on.

**What this changes (idea-lens).** If validated, this is the template for emerging-market CSDs to bolt a public-chain audit layer onto legacy books without a core migration — a low-risk on-ramp that could re-rate XRPL as institutional RWA infra and pressure Clearstream/DTCC to match on *public* (not just private) rails (analysis). Falsifiable thesis: watch for progression from "mirror" to **native on-chain issuance of receivables certificates on CSD BR** within ~12 months — if that ships with CVM sign-off, the model is real; if it stays a perpetual "live test" with no second issuer beyond BTG, it's a marketing pilot. Trigger to watch: a named second asset class / second issuer, or regulatory approval for on-chain primary issuance.

Sources: https://ripple.com/ripple-press/csdbr-and-ripple-use-the-xrpl-blockchain-to-expand-brazils-financial-market-infrastructure/ · https://unchainedcrypto.com/brazilian-depository-with-4-2-trillion-in-assets-taps-xrp-ledger-to-mirror-fund-shares/ · https://thepaypers.com/crypto-web3-and-cbdc/news/ripple-and-csd-br-bring-btg-pactual-fund-records-to-xrp-ledger · https://finbold.com/xrp-ledger-tokenization-gains-momentum-as-rwa-value-hits-4-billion/ · https://www.kucoin.com/news/flash/xrp-ledger-s-tokenized-rwa-surpasses-4-18b-28x-growth-in-a-year · https://ripple.com/ripple-press/ripple-announces-500-million-strategic-investment-led-by-fortress-citadel-securities-valuing-the-company-at-40-billion-following-record-growth/ · https://247wallst.com/investing/cryptocurrency/2026/10/08/ripple-signed-three-institutional-deals-in-one-day-which-of-them-actually-needs-xrp/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news** — and Ripple is a PRIVATE company (no ticker/CIK; IR DB `ir/ir_coverage.json` lists only press releases, funding announcements, XRP Markets Reports, a product update and impact reports — no company revenue/earnings filings). No reported financial results are available; figures below are disclosed operational metrics only, not earnings.

**Disclosed operational metrics (RLUSD, the stablecoin relevant to this tokenization story):**
- RLUSD market cap passed **$2.4bn** (up >50% month-on-month). Per Ripple's transparency report, as of 2026-10-01 there was **$2,509.8m** RLUSD in circulation against **$2,633.8m** in reserves (overcollateralized, backed 1:1 by cash, US Treasuries and government money-market funds via an NYDFS-supervised NY trust).
- Network split: ~**$963m** RLUSD circulates on the **XRP Ledger** vs ~**$1.05bn** on Ethereum; daily transaction activity has more than tripled since the start of 2026.
- Context for this note: on 2026-10-12 Standard Chartered announced institutional custody support for RLUSD on the XRP Ledger — a second-order signal that the XRPL is gaining TradFi-grade infrastructure, consistent with CSD BR mirroring BTG fund shares there.
- Corporate (not results): Ripple was valued at **$40bn** in a Nov-2025 $500m strategic round (Fortress/Citadel Securities); recent M&A includes GTreasury ($1bn), Hidden Road, and Rail ($200m) — scale/ambition markers, not reported earnings.

**Verdict: no results data (private).** No revenue/profit/EPS/guidance exist to assess beat/miss. Semantic search over `state/irdb` was unavailable (OpenRouter 402 — embed HTTP 402 / insufficient credits), so the corpus trend pass could not run.

Sources: https://ripple.com/ripple-press/ · https://finance.yahoo.com/markets/crypto/articles/rlusd-hits-2b-market-cap-130101226.html · https://phemex.com/news/article/ripple-stablecoin-rlusd-market-cap-tops-2-billion-with-nearly-1-billion-on-xrp-ledger-94637 · public consensus / earnings: none (private) — [UNSOURCED beyond disclosed metrics above]
<!-- /enrichment:earnings_review -->
