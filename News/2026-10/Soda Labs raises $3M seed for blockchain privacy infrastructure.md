---
title: "Soda Labs raises $3M seed for blockchain privacy infrastructure"
date: 2026-10-17
retrieved: 2026-10-17
tags:
  - company/soda-labs
  - industry/blockchain
  - industry/infrastructure
  - region/global
  - type/funding
sources:
  - https://thenextweb.com/news/nextblock-soda-labs-3m-seed-privacy-public-blockchains
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sea59e313
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Soda Labs raises $3M seed for blockchain privacy infrastructure

> [!info] 2026-10-17 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Soda Labs, a provider of privacy infrastructure for blockchain-based finance, raised $3 million in seed funding.

## Первоисточники

### thenextweb.com
<https://thenextweb.com/news/nextblock-soda-labs-3m-seed-privacy-public-blockchains>
*748 слов · direct*

NextBlock is putting $3 million behind an increasingly important challenge for public blockchains: how to give financial institutions privacy without forcing them to move their activity onto separate, purpose-built networks.
The Luxembourg-based venture capital firm has funded Soda Labs’ entire seed round. It is backing the company’s programmable privacy infrastructure for financial activity on public blockchains.
Soda Labs has spent the past two and a half years developing a cryptographic privacy system. It combines garbled circuits with multiparty computation, or GC-MPC. It relies on established cryptography including AES and SHA256 and runs on ordinary cloud CPUs rather than specialized hardware.
The technology is designed to enable private computation while applications remain connected to existing public blockchain infrastructure. That addresses a fundamental problem for banks, payment companies and other financial institutions. Public blockchains may offer liquidity and users, but financial data cannot always be visible to everyone.
 “What attracted us to Soda was not only the underlying cryptography, but the practicality of the technology for the financial workloads we believe will matter most onchain,” said Pieter van Poecke, Founder and General Partner of NextBlock. “Soda already had a working product and paying customers. We believe its differentiated technical IP, deeply technical founding team and strong commercial instincts give the company a compelling foundation for its next phase.” 
Soda’s technology has already processed more than 100 million transactions on the COTI network. There, it supports applications including tokenization platform Zoniqx and perpetuals exchange PriveX. PriveX has processed more than $20 billion in trading volume. Zoniqx is onboarding issuers across multiple asset classes and jurisdictions.
Keeping private finance on public chains
Soda is now extending its architecture beyond gcEVM, its Ethereum Layer 2 privacy layer that remains live on COTI. The next step is Soda Bubble, a chain-agnostic coprocessor for programmable privacy.
Bubble is designed to process developer-defined workloads originating from different blockchains. It does so without exposing the underlying private data publicly or to Soda Labs itself.
The company is expanding the system across major EVM ecosystems including Ethereum, Polygon, Arbitrum and Base. Expansion to non-EVM networks, including Solana, is also underway.
Its Bubble Validator Network enables participants to mathematically verify that computations involving private data have been performed faithfully.
For NextBlock, the investment reflects a focus on infrastructure that could make privacy-preserving computation practical for real financial applications. It does so without removing that activity from existing public blockchain ecosystems.
Making privacy faster and cheaper
Soda Labs expects to publish updated performance benchmarks in the coming weeks based on testing conducted on Arbitrum.
The company says the tests measure the complete transaction lifecycle on the live network. That includes encryption, MPC computation, consensus and settlement. They do not measure the cryptographic operation in isolation.
According to Soda, the results represent a five- to tenfold improvement over its previously published benchmark.
The company also reports that its garbled-circuit MPC architecture can deliver approximately 10 to 100 times greater throughput and 100 to 1,000 times lower cost per transaction. That is compared with currently available alternatives, while operating on standard cloud CPUs. Soda has not yet publicly released the new benchmark results.
 “Public blockchains already have the liquidity, users and financial applications. What they lack is a way for regulated money to move without showing everyone everything,” said Avishay Yanai, Co-Founder and CEO of Soda Labs. “Bubble gives banks, payment companies and tokenization platforms privacy with controlled disclosure, on the chains they already use. This round lets us take it from pilots to production.” 
From pilots to production
The $3 million will support Soda Labs’ go-to-market strategy, expansion of its validator network and blockchain coverage, and team growth. It will also fund integrations with banks, payment companies, tokenization platforms and other financial infrastructure providers.
Soda is also working with financial and infrastructure organizations on several undisclosed pilots, with the objective of converting them into production deployments.
Avishay Yanai, CEO and PhD in cryptography, and Meital Levy, CTO and PhD in algorithms, founded the company. Together they bring more than 20 years of experience in security.
For NextBlock, the investment puts capital behind a simple thesis: public blockchains already have the financial activity. The next challenge is making that activity private enough for regulated finance.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
Contributed article. Not produced by the TNW newsroom and does not reflect the editorial stance of TNW.
Get the TNW newsletter
Get the most important tech news in your inbox each week.

## Контекст

<!-- enrichment:context -->
## [0] What exactly happened (de-PR'd)
Soda Labs closed a **$3M seed round, funded in its entirety by a single investor** — Luxembourg-based VC NextBlock (founder/GP Pieter van Poecke). Framed by TNW/the wire (chainwire) as "NextBlock leads," but every outlet confirms NextBlock funded the *whole* round — so "leads" is PR dressing; there is no syndicate. $3M is a *small* seed for infra, and for a company already ~2.5 years old with a live product and paying customers — signalling this is less a "first bet" than a top-up to convert existing pilots to production.

What Soda actually sells: **GC-MPC** (garbled circuits + multiparty computation) that computes directly on encrypted data, split across independent nodes, on commodity cloud CPUs (AES/SHA256, no specialized hardware). Live artifact today = **gcEVM**, the privacy engine inside the **COTI** L2 (live on COTI mainnet since ~March 2025, 100M–125M+ transactions). The new product being funded is **Soda Bubble** — a chain-agnostic "privacy coprocessor" meant to run on Ethereum, Polygon, Arbitrum, Base (and later Solana), plus a **Bubble Validator Network** to attest computations.

**+ Why structured this way / what it reveals:** The deal is a re-labelling of an existing relationship. Soda was the cryptography team *behind* COTI's garbled-circuits stack and was the **inaugural recipient of COTI's $25M ecosystem fund in 2024** (per COTI). So the "startup raises seed" frame undersells a 2.5-year-old, revenue-generating infra team spinning out from one chain (COTI) to become **chain-agnostic** (Bubble). The real story is de-risking single-chain dependency, not a greenfield seed. The money is explicitly earmarked for go-to-market, validator-network/chain expansion, team, and bank/payment/tokenization integrations — i.e. commercialization, not R&D.

## [1] Competitors / peers
The on-chain privacy field in 2026 splits by cryptographic primitive — ZK vs FHE vs TEE vs MPC:
- **Zama** (FHE) — the category leader and first "FHE unicorn" (>$1B valuation, >$150M raised); fhEVM mainnet live since Dec 2025, confidential USDT on Ethereum (~$121M shielded USDT reported). Both **Fhenix** and **Inco** build on Zama's TFHE-rs/fhEVM, so Zama captures licensing regardless of who wins among FHE chains.
- **Fhenix** (FHE) — CoFHE coprocessor on Base/Arbitrum Sepolia; closest on the "coprocessor" architecture.
- **Inco** (FHE + TEE) — Inco Lightning (TEE) and Inco Atlas (FHE, WIP).
- **Aztec** (ZK) — $100M Series B (a16z); proves correctness but cannot compute over *multi-party* encrypted inputs — a structural gap Soda targets.
- **Hinkal** ([[Hinkal joins Mastercard Crypto Partner Program]]) — FHE-adjacent institutional privacy, now inside Mastercard's Crypto Partner Program.
- Privacy-chain incumbents: **Zcash** ([[Zcash developers target January for quantum-resistant payments]]) — but that's a shielded-currency, not programmable-compute-over-encrypted-data.

**+ Why the landscape is this way / second-order:** Everyone else (Zama/Fhenix/Inco) is clustered on **FHE**; Aztec on **ZK**. Soda's bet is **MPC via garbled circuits** — the contrarian primitive. MPC's historical knock was performance/latency; Soda's pitch is that GC-MPC on ordinary CPUs is *cheaper and faster* than FHE/ZK in practice (claims 10–100x throughput, 100–1,000x lower cost/txn vs alternatives). If true, it attacks the exact weakness that keeps FHE out of production. BUT those benchmarks are **not yet published** (promised "in coming weeks," tested on Arbitrum, claimed 5–10x over Soda's own prior benchmark) — so today it's a differentiated *claim*, not a verified advantage. The $3M vs Zama's $150M+ tells you Soda is competing on capital efficiency + a live reference deployment, not war-chest.

## [2] Company history / fit
Founded by **Avishay Yanai** (CEO, PhD cryptography) and **Meital Levy** (CTO, PhD algorithms); ~20 years combined security experience; ~2.5 years building GC-MPC. Trajectory: cryptography partner to **COTI** → built the first production garbled-circuits-on-chain implementation (gcEVM, live since ~Mar 2025) → inaugural recipient of COTI's $25M ecosystem fund (2024) → now **Soda Bubble**, generalizing beyond COTI to a chain-agnostic coprocessor → this $3M to go pilots→production.

**+ Why the company acts this way:** Structural pressure = **single-chain concentration risk.** All 100M+ transactions and the flagship apps (Zoniqx, PriveX) sit on COTI. A privacy-infra vendor locked to one small L2 has a capped TAM and is hostage to that chain's health. Going chain-agnostic (Bubble across Ethereum/Polygon/Arbitrum/Base/Solana) is the only path to a durable infra business — it moves Soda from "COTI's privacy module" to "the privacy layer any chain/app can call." The raise funds exactly that migration + the validator network needed to make it trust-minimized off-COTI.

## [3] Novelty / value-add / traction
Genuinely differentiated primitive (GC-MPC on commodity CPUs) and, unusually for this field, **real traction, not just a testnet**: 100M+ txns on COTI; perpetuals DEX **PriveX** reports **>$20B** cumulative trading volume; tokenization platform **Zoniqx** onboarding issuers; public figures cite ~500 confidential TPS on Arbitrum and 15k+ transfers in July 2026 at ~$0.14 per million transfers. That's materially more adoption evidence than most privacy-infra seeds.

**+ Why the value-add is real-or-not, deeper:** The durable value is **"programmable privacy with controlled disclosure on chains banks already use"** — i.e. you don't force regulated flows onto a separate privacy chain (the Zcash/standalone-L1 failure mode) or accept the latency tax of FHE. If Bubble delivers the CPU-cost claims, Soda captures margin as a **per-computation coprocessor toll** across many chains. What breaks it: (a) benchmarks unpublished — the 10–100x claim is unverified and self-referential; (b) MPC requires a **set of independent, honest-majority validators** — the Bubble Validator Network is new and its security/liveness/economics are unproven; (c) **the $20B PriveX figure is cumulative trading volume, not Soda revenue** — classic PR anchoring to a flattering, orthogonal number; (d) competitors (Zama) have far more capital, mindshare, and a live mainnet moving real USDT. So the value-add is *plausible and better-evidenced than peers*, but the production-scale, multi-chain, benchmark-verified version does not yet exist.

## [4] What's next / market sentiment
Near-term: publish Arbitrum benchmarks (claimed 5–10x over prior); expand Bubble across EVM chains then Solana; grow the validator network; convert "several undisclosed pilots" with financial/infra orgs into production; integrate with banks/payment cos/tokenization platforms. NextBlock's thesis: public chains already have liquidity + apps; the missing piece is privacy for *regulated* money — so infra that keeps activity on public chains (not siloed privacy networks) is the wedge.

**+ Why the market goes this way / counterintuitive second-order:** The tokenization/RWA wave (Ondo, BNY, Citi Token Services, tokenized funds across the [[European firms launch Eurøpe Consortium for onchain finance]] cohort) creates demand for *confidential* on-chain finance — banks won't put positions on a fully transparent ledger. That's a real tailwind. Counterintuitively, being **fully funded by one small VC** is a fragility, not a vote of confidence: no syndicate means no second check-writer to backstop a down-round, and a $3M runway for a go-to-market + multi-chain + validator-network + integrations roadmap is thin — Soda is betting the benchmark publication + pilot conversions re-rate it fast enough to raise a real Series A. Regulatory backdrop (MiCA, controlled-disclosure/"private but auditable" demands) favors MPC's selective-decryption ACL model over opaque privacy coins. Primary risk: the privacy-primitive war consolidates around FHE (Zama's gravity) before Soda proves MPC's production edge.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. Is "NextBlock leads" accurate? No — NextBlock funded the **entire** $3M round; "leads" is PR framing. There is no syndicate (a fragility, not strength).
2. Is this a new company or a spin-out? Soda is ~2.5 years old, was the cryptography team behind COTI's gcEVM, and was the **inaugural recipient of COTI's $25M ecosystem fund (2024)**. So "seed" undersells a revenue-generating infra team — this is a commercialization/de-risking round, not a first bet. (Prior COTI funding is distinct from this NextBlock seed, so NOT a duplicate announcement.)
3. Is the $3M for product or go-to-market? Explicitly GTM, validator/chain expansion, team, and integrations — i.e. pilots→production, not core R&D. Supports "differentiated tech already exists."
4. Are the performance claims verified? No. 10–100x throughput / 100–1,000x lower cost and the "5–10x over prior benchmark" (Arbitrum) are **unpublished**; "in coming weeks." Treat as claims, not facts.
5. Is the $20B PriveX number Soda's metric? No — it's **cumulative trading volume** of a customer app, orthogonal to Soda revenue. Classic flattering-base anchoring.
6. How concentrated is traction? Essentially **100% on COTI** (one small L2). All flagship apps (Zoniqx, PriveX) and the 100M+ txns live there. Single-chain dependency = capped TAM → hence the chain-agnostic Bubble pivot.
7. Does Bubble exist in production? Not yet off-COTI. gcEVM is live (COTI, since ~Mar 2025); Bubble + the Bubble Validator Network are the funded next step — announced, not yet multi-chain-live. Open.
8. Why MPC vs the FHE/ZK field? Soda is contrarian: everyone else (Zama/Fhenix/Inco = FHE; Aztec = ZK). MPC-GC's pitch is CPU-cheap/fast, attacking FHE's latency weakness — IF benchmarks hold. Aztec can't compute over multi-party encrypted inputs; Soda can.
9. Who is the real competitive threat? **Zama** — $1B+ val, >$150M raised, fhEVM mainnet live moving real USDT (~$121M shielded), and Fhenix/Inco build on its tech → Zama earns regardless. Soda is out-capitalized ~50x.
10. What's the margin-capture mechanism? Per-computation coprocessor toll across many chains + validator-network economics. Durable only if Bubble is genuinely chain-agnostic and the validator set is secure/honest-majority — both unproven.
11. Trust model / disclosure? MPC splits data across independent nodes; on-chain access list (ACL) grants scoped decryption. "Private but auditable" fits MiCA/regulated-disclosure demand — a real regulatory tailwind vs opaque privacy coins (Zcash).
12. Is the runway credible? $3M for GTM + multi-chain + validator network + bank integrations is thin. Soda is betting benchmark publication + pilot conversions re-rate it into a real Series A. Downside: no syndicate to backstop a down-round.
13. Are the "several undisclosed pilots" real deployments? Undisclosed and unconverted — "pilots → production" is the stated goal, i.e. not yet production revenue. Open.
14. Freshness vs corpus? Single, first-time announcement (NextBlock $3M seed, 2026-10). No prior corpus note covers this round; adjacent notes ([[Hinkal joins Mastercard Crypto Partner Program]], [[Zcash developers target January for quantum-resistant payments]]) are different companies/primitives. **Fresh.**
15. What would raise importance to 4? Published benchmarks confirming the cost/throughput edge + at least one named off-COTI production bank/tokenization integration + a syndicated Series A.

**Importance: 3/5** — Genuinely differentiated primitive (GC-MPC on commodity CPUs) and, rare for privacy-infra seeds, real adoption evidence (100M+ txns, live gcEVM). But: tiny $3M round, single investor, 100%-COTI concentration, headline benchmarks unpublished, and the flagship $20B figure is a customer's volume, not Soda's. A credible contrarian bet against FHE incumbents, not yet a proven multi-chain winner.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: on-chain privacy / confidential-compute infrastructure for public blockchains — a crowded, rapidly-funded niche within blockchain infra. The thesis that regulated finance needs "privacy with selective disclosure" on public chains (not separate permissioned networks) is now consensus across the field. Market sizing is PR-grade and not independently verifiable: a widely-cited confidential-computing forecast of "$24bn (2025) → $350bn (2032)" and "$500bn institutional capital on the sidelines" circulates via vendor/secondary blogs (e.g. BlockEden, bex.co, 2026) — treat as marketing, not sourced TAM; **no verifiable TAM**. Structure: still pre-standardisation — three competing cryptographic stacks (ZK, FHE, TEE, plus Soda's GC-MPC) are racing to become the default, so the real barrier is technical IP + chain integrations + a credible benchmark, not capital. Why now: ECB/Bank of Israel CBDC pilots and the 2026 tokenisation wave (RWA, tokenised deposits/treasuries — see the dense Oct-2026 tokenisation cluster below) create demand for "compliant privacy" exactly as banks move activity on-chain.

**Competitive landscape.** Sector KPIs run on throughput (tx/sec), cost-per-private-tx, chains supported, and production (not pilot) deployments; Soda discloses >100M tx processed on COTI and a hosted app (PriveX) with >$20bn cumulative trading volume. Technology camps and the basis of competition (performance/cost + EVM compatibility + compliance tooling):
- **FHE camp:** Zama — FHE "unicorn," >$150M raised, >$1bn valuation, mainnet Dec-2025 (per secondary press); Fhenix — ~$22M raised, FHE coprocessor (CoFHE) **live on Arbitrum** — the most direct architectural analogue to Soda's planned "Bubble" coprocessor, also targeting Arbitrum; Inco — ~$10M total (a16z CSX-led), universal confidentiality layer on Ethereum/Base.
- **ZK camp:** Aztec — privacy-first L2, >$170M total funding; Zcash — privacy L1 ([[Zcash developers target January for quantum-resistant payments]]).
- **GC-MPC camp:** COTI — the L2 Soda's tech already powers; COTI markets garbled-circuits as faster than FHE and is pursuing the same bank/RWA/CBDC buyers. Soda's relationship to COTI is ambiguous (supplier vs competitor) — see risk flags.
Position: Soda is a **niche, early-stage challenger** — live product + paying customers + real tx volume are genuine differentiators at seed, but it is one to two orders of magnitude behind FHE/ZK peers on capital. Moat `(analysis)`: differentiated GC-MPC IP + a PhD cryptography founding team + existing COTI deployment (intangibles + a small installed base); no network-effect or switching-cost moat yet.

**Comps & multiples.** Private seed; **no valuation disclosed** → EV/Revenue, P/S etc. = **no data** (post-money not reported by NextBlock). Funding-scale comparison instead:
- Soda Labs — **$3M seed** (this round, fully funded by NextBlock, 2026-10).
- Fhenix — ~$22M (FHE coprocessor, Arbitrum) → ~7x Soda's raise.
- Inco — ~$10M total (confidentiality layer) → ~3x.
- Zama — >$150M / >$1bn valuation (FHE) → ~50x on capital.
- Aztec — >$170M total (ZK L2).
Internal comps (same-month funding rounds in the tokenisation/infra cluster that create Soda's demand): [[Fission raises $10M Series A led by Pantera for tokenized funds]], [[Multiliquid closes Polychain-led seed for tokenized asset liquidity]], [[Sui Foundation invests $30M in DATA Network]]. Read: at $3M fully from a single Luxembourg VC, Soda is **cheaply/thinly capitalised vs the privacy-infra field** — a seed-stage bet, not a scaled contender; the multiple distribution is not computable (one private round, no valuation).

**Risk flags.**
1. **COTI concentration / dual-use ambiguity.** Essentially all disclosed traction (>100M tx, PriveX, Zoniqx) sits on one network, COTI — which itself markets garbled-circuits privacy to the same institutional buyers. If COTI is a competitor rather than a channel, Soda's "chain-agnostic Bubble" pivot is partly a de-risking from a single host; if a dependency, it is single-point concentration. Either way, traction is not yet chain-diversified. Why: revenue and benchmark credibility hinge on one ecosystem's health.
2. **Unverified performance claims.** The headline "10–100x throughput / 100–1,000x lower cost" and "5–10x vs prior benchmark" are **self-reported and not yet published** ("Soda has not yet publicly released the new benchmark results"). Why: the entire GC-MPC-vs-FHE/ZK pitch rests on numbers no third party has validated — classic de-PR gap between "announced" and "verified."
3. **Capital & commoditisation risk.** $3M against peers holding $10M–$170M+ in a stack-wars race where the winning cryptography is undecided; a well-funded FHE/ZK/TEE rival (or COTI itself) could capture the "private RWA on public chains" layer first, leaving Soda's IP stranded. Why: in infra land-grabs, under-capitalised challengers get disintermediated by whoever ships production integrations and standards first.

**What this changes (idea-lens).** `(analysis)` Confirms privacy/confidential-compute is moving from a crypto-native curiosity to a contested institutional-infra category funded as a race, not a product. Soda is a small new entry, not a re-rating. Falsifiable thesis: GC-MPC earns a defensible seat only if (a) the independent Arbitrum benchmark lands near the claimed 5–10x gain AND (b) at least one of the undisclosed bank/payments pilots converts to production off COTI. Trigger to watch: the promised Arbitrum benchmark publication "in coming weeks" and first non-COTI production deployment. What breaks it: benchmark slips or underwhelms, or an FHE/ZK peer wins the first regulated-RWA mandate.

Sources: https://thenextweb.com/news/nextblock-soda-labs-3m-seed-privacy-public-blockchains · https://www.theblock.co/post/278316/inco-raise-testnet · https://www.fhenix.io/blog/privacy-in-defi-2025-landscape-recap · https://blockeden.xyz/blog/2026/01/27/privacy-infrastructure-zk-fhe-tee-mpc-comparison-benchmarks/ · https://cotinetwork.medium.com/the-institutional-checklist-for-privacy-why-banks-and-hedge-funds-will-choose-coti-ca9ef8899b10
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
