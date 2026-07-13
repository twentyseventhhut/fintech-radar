---
title: "Ondo Finance launches custodial tokenized securities with Broadridge"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/ondo
  - company/broadridge
  - industry/blockchain
  - industry/capital-markets
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/2229c4e6
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s06b482b4
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# Ondo Finance launches custodial tokenized securities with Broadridge

> [!info] 2026-07-03 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Ondo Finance launches a custodial tokenized securities product in the U.S. with Broadridge Partners to integrate world-class governance. Broadridge will enable holders of the tokenized securities to participate in proxy voting and receive regulatory disclosures, seamlessly providing token holders with the same protections and rights as holders of traditional securities.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/2229c4e6>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ondo Finance launches custodial tokenized securities with Broadridge
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
On **2026-07-01/02**, Ondo Finance launched the **first-ever "custodial" (third-party) tokenized U.S. securities** — a tokenized **BlackRock iShares Core S&P 500 ETF (IVV)** and **Micron (MU) stock** — on Ethereum, and paired it with **Broadridge** for proxy voting / shareholder communications. The channel one-liner ("launches a custodial tokenized securities product… Broadridge to integrate world-class governance") **understates the real news**: the substance is not the Broadridge tie-up (that was already announced ~April 2026 for Ondo's *synthetic* tokens) but that this is the **first production deployment of the SEC's January-2026 "custodial model"** in the U.S.

- **De-PR'd mechanism**: Under the SEC's Jan-2026 statement, a third party (here Ondo's **registered transfer agent**, obtained via the ~$1.4B **Oasis Pro** acquisition) holds real shares inside the **traditional U.S. regulated custody chain** (shares never leave DTC/broker-dealer/custody rails) and mints tokens **1:1 backed** on Ethereum, held by regulated custodians. Token holders get the **same rights as brokerage holders** — issuer communications, regulatory disclosures, and **on-chain proxy voting via Broadridge's ProxyVote.com**.
- **Why structured this way**: the key design choice is that it **does NOT require the issuer (BlackRock/Micron) to sponsor or tokenize its own shares**, and does **not** route through an offshore SPV. That is the entire point: prior U.S.-accessible tokenized equities were either **offshore** (xStocks/Backed, Kraken SPVs, Robinhood-EU) or needed **issuer-by-issuer sponsorship**. Ondo threads the needle by being the **custodial third party** the SEC explicitly described — so it can tokenize *any* listed security without the issuer's cooperation, on-shore, "within the existing regulatory perimeter."
- **Watch the vagueness**: the PR frames Broadridge governance as the headline (a re-announcement); the genuinely load-bearing claim — "first live U.S. custodial-model product" — is the part to verify. Distribution/eligible-buyer scope for these specific U.S. custodial tokens (retail vs. qualified) is **not clearly stated** in the one-liner (open).

## [1] Competitors / peers
Tokenized-equity landscape is crowded but **structurally segmented** by regulatory posture (dates approx.):
- **Securitize** — deepest regulatory stack (own transfer agent, broker-dealer, fund services); powers **BlackRock BUIDL**; ~19.5% overall RWA share; **went public on NYSE (SECZ) 2026-07-02** via ~$400M SPAC. The most direct on-shore rival by capability.
- **Superstate ("Opening Bell")** — the only **native-issuance** model where the token *is* the SEC-registered share (most legally defensible for equities). Different design than Ondo's custodial wrapper.
- **Dinari** — first **SEC-registered broker-dealer approved to tokenize securities**; the other serious U.S.-native contender.
- **Backed/xStocks (now Kraken-owned)** — most widely distributed tokenized equity product (>$10B volume) but **offshore, non-US** users; SPV-backed.
- **Robinhood** — EU-only "Classic Stock Tokens," self-issued wrapper, 2,000+ tokens.
- **BlackRock BUIDL** — treasuries, not equities; via Securitize. Adjacent, not head-to-head on stocks.
- **Position**: Ondo is **first to production on the specific U.S. custodial model** (a real "first"), and dominates the tokenized-*equity issuer* market (>70%, $1B+ TVL). But on **U.S. on-shore legitimacy** it is **catching up to** Securitize/Superstate/Dinari, who already hold broker-dealer/native-issuance status. (analysis) The moat here is being early + the transfer-agent license, not a unique tech.
- **Why the landscape is this way / second order**: the regulatory perimeter is the battleground, not the chain. Whoever can tokenize **without issuer permission, on-shore** captures the widest catalog fastest → Ondo's custodial model is the most *scalable* catalog-wise, but the *most legally defensible* (Superstate native) may win institutional trust. The gap closes as the SEC formalizes rules.

## [2] Company history / fit
Consistent, aggressive trajectory into regulated tokenized equities:
- **2025-07**: Ondo + Pantera launch **$250M tokenization fund**; agrees to buy **SEC-regulated broker Oasis Pro (~$1.4B)** for broker-dealer/ATS/**transfer-agent** licenses — the exact license powering *this* launch.
- **2025-09**: launches **100+ tokenized U.S. stocks/ETFs** (Ondo Global Markets), initially for **non-US qualified** investors.
- **2025-12**: **SEC ends its 2024 investigation** into Ondo with no charges — clears the runway to operate on-shore.
- **2026-02**: Blockchain.com + Ondo bring tokenized U.S. stocks to Europe ($556M TVL, $8.7B volume then).
- **2026-04**: adds **proxy voting via Broadridge** for its ~$700M *synthetic* tokenized equities (the Broadridge relationship's real origin).
- **2026-05**: Ondo GM tops **$1B TVL** (<8 months, first tokenized-stock platform to do so); completes cross-border tokenized-Treasuries redemption with **J.P. Morgan/Mastercard/Ripple**.
- **Why**: Ondo needs to move from **offshore/synthetic** access to **on-shore, issuer-independent, regulated** rails to win U.S. institutions and defend its >70% share. The Oasis Pro transfer-agent license → SEC clearance → custodial-model launch is a **deliberate, ordered build**, not opportunism. This launch is the logical capstone.

## [3] Novelty / value-add / traction
- **Real novelty (confirmed)**: **First live U.S. custodial-model tokenized securities** where a third party tokenizes listed shares (BlackRock IVV, Micron) **without issuer sponsorship, on-shore, 1:1 backed**, inside DTC/custody rails — validating the SEC's Jan-2026 framework in production. This is a genuine "first," not a reprint.
- **Recycled part**: The **Broadridge proxy-voting governance layer** is NOT new — announced ~April 2026 for synthetic tokens. The PR anchors on it because governance sells; the substance is the custodial model.
- **Traction (numbers, not announcements)**: Ondo GM at **$1B+ → $1.17B TVL**, **~$18–20B cumulative volume**, **>70% of tokenized-equity issuer market**, +3–5% TVL/week. But note: those numbers are for the **broader (mostly offshore/synthetic) GM platform**; this specific **U.S. custodial product just launched** — its own adoption is **$0 → TBD (open)**.
- **Why the value-add is real / where margin sits**: the durable moat is the **transfer-agent + broker-dealer license** + first-mover on a model that scales to *any* listed security. (analysis) Margin accrues to whoever controls **issuance + custody + the compliance rail**, not the chain — Ondo now owns that stack on-shore. Risk: the model is **replicable** by Securitize/Dinari who already have similar licenses, so the "first" premium is **time-limited**, and if the SEC's guidance tightens (e.g., requires native issuance à la Superstate), the custodial wrapper could be reframed as second-best.

## [4] What's next / market sentiment
- **Plans**: Ondo exec **Ian De Bode** guides tokenized-stock TVL to **$2.5–3B by end-2026** at current run-rate. Expect catalog expansion (IVV/Micron are proofs-of-concept) and likely U.S. retail distribution.
- **Sentiment**: broad tailwind — tokenized assets +47% YTD; Securitize's NYSE debut (2026-07-02) and Invesco's tokenized reserve-fund filing (2026-07-01) signal Wall Street racing on-chain the same week.
- **Regulatory backdrop**: the whole thesis rests on the **SEC's Jan-2026 custodial statement** — a *statement*, not a final rule. Second-order risk: if the SEC formalizes rules differently (or a new administration shifts posture), the "first-mover on a statement" edge is fragile.
- **Counterintuitive second-order (analysis)**: being **first on a not-yet-codified model** is both the strength and the exposure — Ondo is building on regulatory interpretation. If the interpretation holds, Ondo has the widest on-shore catalog; if it shifts toward native issuance, Superstate's design wins the legitimacy argument. The central question shifts from "can Ondo tokenize on-shore?" (yes, done) to **"does the SEC's custodial model survive codification, and does Ondo's license-based moat outlast the 6–12-month replication window?"**

## Sources
- PR: Ondo Finance Launches First-Ever Custodial Tokenized Securities in the U.S. (Broadridge) — prnewswire.com/…302816716.html
- CoinDesk (2026-07-01): Ondo debuts SEC-aligned tokenized stock model with BlackRock ETF, Micron
- The Block (2026-07): Ondo tokenizes BlackRock's IVV ETF and Micron under US custodial model
- Finance Magnates / TradingView; CryptoTimes (2026-07-02); Coincentral; crypto.news
- CoinDesk (2026-04-28): Ondo adds proxy voting for $700M tokenized equities (prior Broadridge)
- PRNewswire (2026-05): Ondo GM surpasses $1B TVL; TheStreet: De Bode $3B year-end guide
- Fortune / The Block / The Defiant (2026-07-02): Securitize NYSE debut; competitor set
- Internal: [[Ondo launches 100+ tokenized US stocks across chains]], [[Ondo Finance to buy SEC broker Oasis Pro for $1.4B]], [[SEC ends investigation into tokenization platform Ondo Finance]], [[Blockchain.com and Ondo launch tokenised US stocks in Europe]], [[Ondo, J.P. Morgan, Mastercard, Ripple complete tokenized Treasuries pilot]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Challenge / red-team questions

1. **Is the "first-ever custodial tokenized U.S. securities" claim true, or PR?** — Confirmed across CoinDesk, The Block, Finance Magnates: first production deployment of the SEC's Jan-2026 custodial model on-shore (BlackRock IVV + Micron). Genuine first.
2. **Is Broadridge the news, or a re-announcement?** — Re-announcement. Broadridge proxy voting for Ondo's *synthetic* equities was announced ~2026-04-28 (CoinDesk, PRNewswire 302755024). The custodial product is the new part; PR foregrounds governance.
3. **What legally lets Ondo do this?** — Its **registered transfer agent** license from the ~$1.4B Oasis Pro acquisition + SEC ending its investigation (2025-12). Without those two, this launch is impossible.
4. **Does the issuer (BlackRock/Micron) participate?** — No. The whole design tokenizes listed shares **without issuer sponsorship** — that's the scalability differentiator. Open: any legal risk from tokenizing a name without consent?
5. **Is it truly 1:1 backed and on-shore?** — Claimed: shares stay in DTC/regulated custody, tokens minted 1:1 on Ethereum, held by regulated custodians. Not independently audited yet (open — attestation cadence unstated).
6. **What's the adoption of THIS product (not the broader GM platform)?** — $0 → TBD. Launched 2026-07-02. The $1B+ TVL / $18–20B volume are the broader (mostly offshore/synthetic) platform, NOT the U.S. custodial product. Do not conflate.
7. **Who can replicate this and how fast?** — Securitize (own broker-dealer/transfer agent, NYSE-listed 2026-07-02), Dinari (SEC-registered BD approved to tokenize), Superstate (native issuance). Replication window likely 6–12 months → first-mover premium is time-limited.
8. **Is the custodial model legally durable?** — It rests on a SEC **statement** (Jan-2026), not a codified rule. Regulatory-interpretation risk; a shift toward native issuance would favor Superstate.
9. **Custodial wrapper vs. native issuance — which wins institutional trust?** — Open/analysis. Superstate's token-is-the-share is more defensible; Ondo's is more scalable catalog-wise. Different bets.
10. **Who is eligible to buy the U.S. custodial tokens — retail or qualified only?** — Not stated in the one-liner; GM historically served non-US/qualified investors. Open.
11. **Where does the margin sit in the stack?** — Issuance + custody + compliance rail (which Ondo now owns on-shore), not the chain. Durable only while the license moat + first-mover lead hold.
12. **Does this cannibalize Ondo's offshore/synthetic GM business?** — Possibly complements (U.S. on-shore) vs. non-US GM. Open whether U.S. demand is incremental or migratory.
13. **Is the $2.5–3B year-end TVL guidance credible?** — De Bode (Ondo exec) self-guidance at ~3–5%/week run rate; plausible but self-reported and platform-wide, not custodial-specific.
14. **What's silent?** — Fees/economics of the custodial product, custodian identity, redemption mechanics, and audit/attestation cadence are not disclosed.
15. **Second-order: does being first on an un-codified model help or expose Ondo?** — Both. If the interpretation holds, widest on-shore catalog; if codification favors native issuance, the wrapper is reframed as second-best.

**Importance: 4/5** — A genuine "first" (first live U.S. custodial-model tokenized securities under the SEC's Jan-2026 framework, with a marquee BlackRock ETF), backed by a real license moat (Oasis Pro transfer agent) and category dominance (>70% issuer share, $1B+ TVL). Held below 5 because: the Broadridge governance angle is recycled; the specific U.S. product has zero measured adoption yet; the model rests on an SEC *statement* not a rule; and the moat is replicable within 6–12 months by Securitize/Dinari.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-03]] (2026-07-03).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Onchain RWA (real-world asset) tokenization ex-stablecoins reached ~$31–34bn TVL by May 2026, up from ~$6–6.5bn a year earlier (~+300–400% YoY; per RWA.xyz, via crypto.news / yellow.com, as of May 2026). Tokenized US Treasuries alone crossed ~$15bn AUM by May 2026 (RWA.xyz, via finextra), up from ~$5bn late 2024. Ondo's launch pushes past the Treasuries/MMF wave into the harder, larger prize — tokenized *equities* (IVV ETF, Micron) — the segment gated by shareholder-rights and transfer-agent plumbing, not just yield-bearing wrappers. Structure: still fragmented and early — value is being contested at three chain-of-custody layers: issuance/transfer-agent, custody, and governance/proxy. Barriers are regulatory, not technical: the model rides the SEC's Jan-2026 statement describing a custodial structure where a third party holds the underlying security and issues crypto entitlements. "Why now": that Jan-2026 SEC framing plus the closure (Dec-2025) of the SEC's own confidential probe into Ondo without charges (see [[SEC ends investigation into tokenization platform Ondo Finance]]) removed the overhang that had kept US-domiciled tokenized equities off the table.

**Competitive landscape.** Sector KPIs: onchain AUM/TVL, issuance revenue (fees on AUM), and — newly relevant here — governance completeness (proxy/voting/disclosures). Key players and basis of competition: Securitize (BlackRock-linked, ~$4bn+ AUM Oct-2025, now NYSE-listed "SECZ"), Superstate (issuance layer for SEC-registered equities on ETH/Solana), Franklin Templeton, and BlackRock's BUIDL (>$2.5bn) compete on asset-manager distribution and regulatory standing; Ondo competes on being *first* to a live custodial third-party tokenized-equity model inside the US perimeter, with Broadridge's ProxyVote and Ondo's own SEC-registered transfer agent (Oasis Pro TA) supplying the voting/disclosure layer peers largely lack. Recent peer moves: Superstate $82.5M Series B (Jan-2026, [[Superstate raises $82.5M Series B for tokenization]]); Invesco took over Superstate's ~$900m onchain fund (Mar-2026, [[Invesco takes over Superstate's $900m on-chain fund]]); Coinbase took an equity stake in Centrifuge as tokenization backbone (May-2026, [[Coinbase taps Centrifuge for tokenization and takes equity stake]]); Securitize went public via $1.25bn SPAC (Nov-2025→NYSE Jul-2026, [[Securitize to go public via $1.25B SPAC]], [[Securitize files for SPAC merger after 841% revenue jump]]). Ondo's position: ahead on the *governance-complete US equity* niche (analysis); moat is regulatory/intangible (transfer-agent registration + Broadridge integration), not yet scale — moat is thin and replicable if peers strike similar proxy deals.

**Comps & multiples.** No tradable equity for Ondo; the ONDO token trades at ~$1.6bn market cap / ~$3.1–3.4bn FDV (CoinGecko/Coinbase/Tokenomist, Jul-2026), but token mcap is NOT a claim on issuance revenue and is not comparable to peer equity — treat as sentiment, not valuation. Best external comp is Securitize: $1.25bn pre-money / FY2025 revenue $69m = **~18x** revenue; on projected FY2026 revenue $110m = **~11x**; on projected $9bn 2026 AUM = **~0.14x AUM** (per prnewswire/Blockworks SPAC deck; projections are management guidance, not audited). Ondo's own AUM/issuance-revenue for this new product = no data (not disclosed). Distribution not computed — only one clean revenue comp; qualitative read: RWA-tokenization equity is priced richly (~11–18x revenue) but on triple-digit growth, so not an automatic outlier. `[UNSOURCED]`: Ondo issuance revenue, product AUM, EV/EBITDA.

**Risk flags.**
1. **Announced vs. adopted / thin float.** Live but two instruments (IVV, Micron); no disclosed AUM, holder count, or liquidity — adoption unproven; a governance-complete wrapper with little AUM captures little fee revenue (second-order: revenue follows AUM, not press).
2. **Regulatory dependence on a single SEC interpretive posture.** The whole model rests on the Jan-2026 SEC custodial statement; an interpretive statement is not a rule and can shift with SEC personnel/policy — a reversal would strand the structure (concentration on one regulatory rail).
3. **Disintermediation / value-capture at the wrong layer.** Ondo supplies issuance+transfer-agent, but custody and governance-proxy value accrue to Broadridge and custodians; if asset managers (Securitize/BlackRock) bring proxy in-house or via cheaper vendors, Ondo risks being a thin issuance layer while margin sits elsewhere in the stack.

**What this changes (idea-lens).** (analysis) This is the opening of the *tokenized-equity-with-full-shareholder-rights* front — the credible answer to the "but you don't get voting rights" objection that kept US equities off-chain. Falsifiable thesis: if governance-complete tokenized equities are real demand rather than a compliance box-tick, disclosed AUM in this product line should cross a meaningful threshold within 2–3 quarters and peers (Securitize, Superstate) should announce their own proxy/voting integrations. Trigger to watch: first disclosed AUM/holder figures, and whether a top-tier asset manager (BlackRock, Franklin) adopts a rival proxy stack. What breaks the thesis: product stays at a handful of tickers with no AUM disclosure into 2027 → PR launch, not a market.

Sources: https://www.prnewswire.com/news-releases/ondo-finance-launches-first-ever-custodial-tokenized-securities-in-the-us-broadridge-partners-to-integrate-world-class-governance-302816716.html · https://finadium.com/ondo-launches-first-custodial-tokenized-securities-in-us-with-broadridge/ · https://crypto.news/tokenized-real-world-assets-triple-to-34-billion-as-treasuries-and-ethereum-lead/ · https://www.finextra.com/blogposting/31625/tokenized-real-world-assets-reading-the-2026-numbers-behind-the-headline-growth · https://www.prnewswire.com/news-releases/securitize-the-leading-tokenization-platform-to-become-a-public-company-at-1-25b-valuation-via-business-combination-with-cantor-equity-partners-ii-302596208.html · https://www.coingecko.com/en/coins/ondo
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
