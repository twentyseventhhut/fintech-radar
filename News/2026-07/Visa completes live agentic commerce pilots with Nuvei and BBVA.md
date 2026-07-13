---
title: "Visa completes live agentic commerce pilots with Nuvei and BBVA"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/visa
  - company/nuvei
  - company/bbva
  - industry/agentic-commerce
  - industry/payments
  - region/global
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/a8bccc93
  - https://www.connectingthedotsinfin.tech/r/f0a2c965
  - https://www.connectingthedotsinpayments.com/r/4e11ea53
  - https://www.connectingthedotsinpayments.com/r/9d391251
  - https://www.connectingthedotsinpayments.com/r/726d2d1c
  - https://www.connectingthedotsinpayments.com/r/0b74bb6c
  - https://www.connectingthedotsinpayments.com/r/fb8fc60e
status: published
n_mentions: 6
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s649ea39b
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Visa completes live agentic commerce pilots with Nuvei and BBVA

> [!info] 2026-07-03 · 6 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇨🇦 Nuvei completes first-party in-agent payment with Visa and unveils a merchant-led agentic payments strategy. Nuvei and Visa completed a live agentic commerce pilot, enabling an AI agent to securely initiate and complete a purchase on a shopper’s behalf using live Visa payment rails and tokenized credentials.

[Connecting the Dots in Fintech] 🌍 BBVA completes its first AI agent-initiated transaction together with Visa, using tokenization, real-time fraud monitoring, and Visa Payment Passkeys to comply with EU Strong Customer Authentication requirements. The pilot demonstrates that agentic payments can operate securely within existing regulatory frameworks.

[Connecting the Dots in Payments] Visa Pushes Agentic Commerce Forward with Nuvei and BBVA

[Connecting the Dots in Payments] Together with Nuvei, it completed a live AI agent purchase on Visa rails, allowing a merchant's AI agent to discover, authorize, and complete a payment without leaving the shopping experience. Separately, BBVA successfully tested its first AI agent-initiated payment using Visa's infrastructure, showing that these transactions can work within today's banking and regulatory frameworks.

[Connecting the Dots in Payments] 🇨🇦 Nuvei completes first-party in-agent payment with Visa and unveils a merchant-led agentic payments strategy. Nuvei and Visa completed a live agentic commerce pilot, enabling an AI agent to securely initiate and complete a purchase on a shopper’s be

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/a8bccc93>
- <https://www.connectingthedotsinfin.tech/r/f0a2c965>
- <https://www.connectingthedotsinpayments.com/r/4e11ea53>
- <https://www.connectingthedotsinpayments.com/r/9d391251>
- <https://www.connectingthedotsinpayments.com/r/726d2d1c>
- <https://www.connectingthedotsinpayments.com/r/0b74bb6c>
- <https://www.connectingthedotsinpayments.com/r/fb8fc60e>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Visa completes live agentic commerce pilots with Nuvei and BBVA
_Analytical notes (not a post). Importance: 3/5._

**Freshness: FRESH.** These are NEW milestone-transaction events (2026-07-02), distinct from the prior *program* announcements in the corpus: [[Visa launches Trusted Agent Protocol for AI commerce]] (2025-10-17, protocol), [[Visa launches Intelligent Commerce Connect for agentic commerce]] (2026-04-10, product), [[Visa expands Agentic Ready program to Canada]] (2026-05-01, program). Nuvei was already named as a TAP feedback partner in Oct 2025 — but hadn't *completed a transaction*. So this is a genuine "framework → first live txn" follow-up, not a reprint.

## [0] What exactly happened (de-PR'd)
Two SEPARATE single-transaction pilots, both dated 2026-07-02, timed around the Visa Payments Forum (Paris):
- **Nuvei + Visa** — a merchant's first-party AI agent initiated and completed a purchase *inside the agent* (no hand-off to a separate checkout), settled on **live Visa rails using a tokenized Visa credential**, within Visa Intelligent Commerce. Named participants: Arvato Systems, brand "Kings and Priests"; issuers Alpha Bank, Piraeus, Bank Leumi, CAL, MAX, Bank of Cyprus. Nuvei (a Canadian *acquirer*) also unveiled a "merchant-led" strategy: a Protocol Compatibility Layer (accept ACP/AP2/MCP, certify against BOTH Visa Intelligent Commerce and Mastercard Agent Pay) and a "Know Your Agent" registry. Commercial availability only "targeting H2 2026."
- **BBVA + Visa** — "first AI agent-initiated transaction" (framed as Europe's first bank agent-initiated payment), using tokenization, real-time fraud monitoring, and **Visa Payment Passkeys** to satisfy **EU SCA under PSD2**. Under the Visa Agentic Ready program (Europe, ~Mar 2026).
- **Why framed this way / what it reveals:** These are engineering proof-of-concepts, not GA. "Completes first" = ONE transaction each. PYMNTS clarifies BBVA's pilots run in "production-grade *testing* environments alongside selected merchants" — real credentials + real merchant systems, but a controlled test, not open commerce. The same-day cluster of near-identical "firsts" (Nuvei, BBVA, and separately Worldline/ING/Visa) is coordinated launch PR around the Forum, not organic independent go-lives. NOT disclosed by anyone: volumes, merchant availability, GA dates (only Nuvei's vague "H2 2026"), **fraud-liability allocation** (the single most important unanswered question), economics/interchange, chargeback/dispute handling.

## [1] Competitors / peers
- **Mastercard Agent Pay + Agentic Tokens** — announced 2025-04-29 (one day *before* Visa Intelligent Commerce); "Agent Pay for Machines" (A2A/micropayments) added 2026-06-10. Effectively at parity with Visa on the card-scheme axis; Nuvei explicitly plans to certify against Mastercard too, underscoring the two schemes are co-standards here.
- **Stripe + OpenAI — Agentic Commerce Protocol (ACP)** — 2025-09-29, powers ChatGPT Instant Checkout with real consumers buying from Etsy/Shopify brands. **This is the strongest genuinely-LIVE, at-scale, consumer-facing claim in the space.** Card-based too — so Visa's incremental proof isn't "cards work," it's the *issuer-side SCA/Passkey* (BBVA) and *acquirer-side in-agent first-party* (Nuvei) paths.
- **Google Agent Payments Protocol (AP2)** — 2025-09-16, 60+ partners, card + stablecoin mandates; **Coinbase x402** extension (stablecoin A2A). **PayPal Agentic Commerce Services** — 2025-10-28 (Agent Ready GA "early 2026").
- **Position:** Visa is ahead on *regulated-EU-issuer* proof (SCA via Passkeys is a real differentiator vs the lighter-touch US path Stripe/OpenAI took) but *behind* Stripe/OpenAI on live consumer traction. Position = parity on infrastructure, catching-up on real usage.
- **Why the landscape is this way (analysis):** The US has no SCA equivalent, so Stripe/OpenAI could ship to consumers fast; the EU's PSD2 SCA is the hard problem, which is precisely why Visa stages *issuer pilots (BBVA) in Europe* — the value of the announcement is regulatory viability, not throughput.

## [2] Company history / fit
Consistent trajectory: [[Visa launches Trusted Agent Protocol for AI commerce]] (Oct 2025, agent-verification protocol w/ Cloudflare; Nuvei a feedback partner) → [[Visa works with 100 partners on agentic shopping]] / [[Visa and Partners Complete Secure AI Transactions]] (Dec 2025–Jan 2026, "100+ partners," pilots anticipated early 2026 in APAC/Europe) → [[Visa launches Europe digital-wallet push, joins AWS on agentic commerce]] (Dec 2025) → [[Visa launches Intelligent Commerce Connect for agentic commerce]] (Apr 2026) → [[Visa expands Agentic Ready program to Canada]] (May 2026) → these first live txns (Jul 2026). Fits logically: Visa flagged "pilots to kick off early 2026" back in Dec-2025/Jan-2026, and these are the delivery. **Why (analysis):** as a network, Visa's play is to embed its rails/tokens/identity as the default trust layer *before* agent frameworks route around cards to stablecoins (x402) or closed loops — defending the interchange base against disintermediation.

## [3] Novelty / value-add / traction
- **Genuinely new:** an agent-initiated payment on *existing live card rails with tokenized credentials while satisfying EU SCA via Passkeys* (BBVA), and a *first-party in-agent* flow with no checkout hand-off (Nuvei). The SCA-under-PSD2 proof is the real substance — it's the hard regulatory gate the US players sidestepped.
- **Traction reality check:** ZERO adoption numbers. Each is ONE transaction. "Live in the narrow technical sense" ≠ "in market." Compare to Stripe/OpenAI's actual consumer purchases. So value-add is a de-risking milestone, not a commercial signal.
- **Who captures the margin (analysis):** the central question isn't "does agentic payment work" (it does) but *who owns the agent-identity + mandate layer*. Nuvei's Protocol Compatibility Layer + "Know Your Agent" is a bid to be the merchant-side router/registry — but the trusted-agent protocol and tokens sit with Visa/Mastercard. So an acquirer like Nuvei risks staying a "compatibility shim" while the schemes capture the trust rent. Visa's risk: AP2/x402 stablecoin rails route around interchange entirely.

## [4] What's next / market sentiment
- Nuvei targets "initial availability H2 2026"; BBVA gives no GA date; PYMNTS hedges practical agent commerce is "within three years." Expect more same-shape issuer/acquirer "firsts" from Visa's Agentic Ready cohort.
- Vendor-cited market (McKinsey, via Nuvei release, treat as marketing): agentic commerce ~$1T global volume by 2030, $3–5T by 2035.
- **Risks / second-order (analysis):** (1) fraud-liability allocation is undisclosed and is the make-or-break for scale — who eats a fraudulent agent-initiated txn? (2) EU regulators may treat autonomous agents' mandates as needing fresh SCA per session, capping "autonomy." (3) counterintuitively, the flood of coordinated "firsts" signals the schemes are racing to set defaults *before* open protocols (AP2/x402/ACP) commoditize the payment step — the PR intensity is a tell of competitive anxiety, not settled dominance.

## Sources
- Internal corpus (see wikilinks above). External: Nuvei PRNewswire (2026-07-02), BBVA.com (2026-07-02), PYMNTS "Visa and BBVA prove today's rails can handle agentic payments" (2026-07-02), Worldline/ING GlobeNewswire (2026-07-02), Visa Intelligent Commerce PR (2025-04-30), Visa TAP investor PR (2025-10-14), Mastercard Agent Pay (2025-04-29), Stripe/OpenAI ACP (2025-09-29), Google AP2 (2025-09-16), PayPal Agentic Commerce Services (2025-10-28).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **One transaction ≠ a product.** Each pilot is a single completed txn. What volume/merchant count would make this "live commerce" vs a demo? — Open; nobody disclosed volumes or merchant rosters beyond one brand each.
2. **Who eats agent-initiated fraud?** Liability allocation between issuer/acquirer/merchant/agent operator is undisclosed — arguably the single gating question for scale. — Open.
3. **Is this actually "live money moved"?** BBVA PR says "real credentials/active merchant," but PYMNTS says "production-grade *testing* environments." Did an irreversible consumer purchase settle, or a test? — Unresolved; treat as live-rails pilot, not GA.
4. **Was Nuvei already "in"?** Nuvei was a TAP feedback partner (Oct 2025). So is "first-party in-agent payment" a genuine first, or the activation of an existing relationship? — Partly the latter; the *completed txn* is new, the tie-up isn't.
5. **Why the same-day cluster?** Nuvei, BBVA, and Worldline/ING all posted near-identical "firsts" on 2026-07-02 around the Visa Payments Forum. Coordinated PR vs organic go-lives? — Coordinated launch marketing.
6. **Does the SCA/Passkey proof durably solve PSD2 for autonomous agents,** or only for a single consented session? Could regulators require fresh SCA per agent action, capping autonomy? — Open.
7. **Who captures margin?** Does Nuvei's "Know Your Agent" / Protocol Compatibility Layer make it the router, or a shim beneath Visa/Mastercard's trusted-agent + token layer? — Structurally at risk of being a shim (analysis).
8. **Disintermediation risk:** AP2 + Coinbase x402 (stablecoin A2A) route around card interchange. How much of this Visa push is defense of the interchange base vs a growth story? — Largely defensive (analysis).
9. **Live-usage gap vs Stripe/OpenAI:** ACP/ChatGPT Instant Checkout has real consumers buying (Etsy/Shopify) since Sept 2025. Is Visa catching up on traction while claiming infrastructure leadership? — Yes; parity on rails, behind on usage.
10. **GA timeline:** Only Nuvei gives vague "H2 2026"; BBVA none. What's the real path from pilot to merchant availability? — Open.
11. **Economics:** interchange/pricing for agent-initiated txns, chargeback/dispute/refund handling — none disclosed. Does the unit economics even change? — Open.
12. **Nuvei geography mismatch:** Nuvei is a Canadian acquirer but the pilot's issuers are EU/Israel/Cyprus. Is the "merchant-led" claim tested in Nuvei's actual core markets? — Open / worth flagging.
13. **Standards fragmentation:** Visa TAP vs Mastercard Agent Pay vs ACP vs AP2 vs MCP — Nuvei certifies against several. Does multi-protocol support signal no winner yet, and does that delay real adoption? — Yes, no settled standard.
14. **Is Passkey-SCA a real moat** or table stakes Mastercard/others will match within months? — Likely table stakes (analysis).
15. **Second-order:** does the intensity of coordinated "firsts" reveal competitive anxiety rather than dominance? — Yes (analysis).

**Importance: 3/5** — Genuinely fresh milestone (first live agent-initiated txns on Visa rails with EU SCA satisfied via Passkeys is a real regulatory-viability proof, and BBVA is framed as a European bank first), but it's single-transaction pilot PR with zero adoption numbers, no GA, no economics, and no fraud-liability disclosure. Meaningful as a de-risking signal in a fast-moving, well-covered Visa agentic thread — not a market-moving event on its own. Bumped above 2 by the SCA/PSD2 substance and the Nuvei strategy detail; capped at 3 by demo-not-product reality.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-03]] (2026-07-03).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce = AI agents that discover, authorize and settle purchases on a user's behalf. Third-party sizing is early and dispersed: Juniper Research projects agentic-commerce transaction value rising from ~$8bn in 2026 to ~$1.5tn by 2030 (per Juniper, via juniperresearch.com/stellagent, as of 2026); McKinsey frames a wider $3–5tn global opportunity and Morgan Stanley a narrower US $190–385bn (10–20% of online retail) by 2030 — the spread itself signals these are directional scenarios, not settled TAM (treat as `(analysis)`, not a hard number). Structure: the underlying card-network layer is a duopoly (Visa + Mastercard) with entrenched network effects; the *agentic* layer sits on top and is currently fragmented across networks, acquirers (Nuvei/Stripe), issuers (BBVA), and agent-identity startups (Crossmint, Alchemy). Why now: the constraint isn't payment capacity but trust/authentication — an agent must prove it's authorized and the transaction must satisfy fraud and regulatory rules (EU SCA). Visa's pitch is that its rails + tokenized credentials + Payment Passkeys let agent transactions clear inside existing frameworks rather than on a new rail — de-PR'd, that's the load-bearing claim here.

**Competitive landscape.** Card-network KPIs: payments volume (TPV), processed transactions, cross-border volume, net revenue yield. Visa scale (Q2 FY26, see IR below): $3.7tn quarterly payments volume, 66bn processed transactions — dwarfing any agentic pilot, so agentic is optionality on the existing base, not a near-term needle-mover. Basis of competition in agentic: standards ownership + issuer/acquirer distribution, not price. Recent moves (dated): Visa Intelligent Commerce Connect launched 2026-04-10 [[Visa launches Intelligent Commerce Connect for agentic commerce]]; Visa Europe agentic programme 2026-03-18 (Revolut named) [[Visa launches agentic payments programme in Europe]]; Visa + Mastercard bank pilots 2026-02-20 [[Mastercard and Visa enlist banks for agentic payment pilots]]; Mastercard Agent Pay for Machines 2026-06-12 [[Mastercard launches Agent Pay for Machines for machine-speed payments]]; Crossmint Agentic Cards API on Visa 2026-06-03; Alchemy AgentCard on Visa 2026-06-19. This 2026-07-03 item moves BBVA/Nuvei from "enlisted" (Feb) to "completed live transaction" — incremental proof-of-life, not GA. Position: Visa is *ahead* on breadth (both its own Intelligent Commerce APIs and interop with non-Visa rails) with a moat from network effects + issuer relationships `(analysis)`; Mastercard is at parity on messaging.

**Comps & multiples.** Public duopoly peer (per stockanalysis/yahoo/companiesmarketcap, as of ~June 2026):
- **Mastercard**: market cap ~$428bn; fwd P/E ~27.7x.
- **Visa** (protagonist): market cap ~$639bn; fwd P/E ~24.4x; EV/EBITDA ~20.8x; LTM revenue ~$43.0bn, net income ~$22.0bn → implied P/S = $639bn / $43.0bn ≈ **14.9x**; P/E (LTM) = $639bn / $22.0bn ≈ **29x**. Visa trades at a modest *discount* to Mastercard on fwd P/E despite larger scale — in-line-to-slightly-cheap within the duopoly, both rich vs a broad market but justified by ~mid-teens revenue growth and ~65%+ operating margins (growth-multiple consistent, not an outlier flag).
- Private acquirer comp: **Nuvei** taken private by Advent for EV ~$6.3bn ($34.00/sh, ~56% premium) closing early 2025 (mark as take-private EV, not current market cap) — orders of magnitude below the networks; the acquirer's economics per agentic transaction are undisclosed → `[UNSOURCED]`.
- Distribution not computed (only 2 comparable public figures); qualitative comparison used.

**Risk flags.**
1. **Disintermediation cuts both ways.** Agentic commerce is being sold by the networks as a defensive moat, but the same shift lets agent-layer players (Crossmint, Alchemy, agent-wallets) or stablecoin rails (cf. Mastercard's Coinbase tie-up) insert themselves — if value migrates to whoever owns agent *identity/authorization*, the network could be relegated to a commodity settlement rail. Second-order: pressure on take rate.
2. **Pilot ≠ economics.** "Completed a live transaction" says nothing about interchange treatment, fraud-liability allocation for agent-initiated payments, or ticket size — precisely the disputed items. Who's silent: no party has disclosed the economics or SCA liability split. Regulatory ambiguity (who is liable when an autonomous agent misfires under EU SCA) is unresolved.
3. **Announcement cadence risk.** This is the ~5th Visa agentic headline in 5 months with overlapping partners; a stream of pilots can outrun measurable volume, making it hard to distinguish real adoption from PR positioning.

**What this changes (idea-lens).** `(analysis)` Not a re-rating event on its own — agentic volume is immaterial to Visa's $3.7tn/quarter base today; the stock trades on card volume, not agents. The real question is defensive: does Visa keep the payment leg as agents commoditize the shopping leg? Falsifiable thesis — if by FY27 Visa quantifies agentic transactions/volume in an earnings release (as it does Visa Direct), the duopoly has successfully annexed the new layer; if the disclosure never comes while startups/stablecoin rails scale, that's the disintermediation flag playing out. Trigger to watch: first network to report agentic TPV, and the first published interchange/liability standard for agent payments.

Sources: IR — Visa Q2 FY26 earnings release (2026-04-28) https://drive.google.com/file/d/1X9YkQAcH51_U9lg1phhxEHmDvWhOE2Bu/view (filing: https://s1.q4cdn.com/050606653/files/doc_financials/2026/q2/Q2-2026-Earnings-Release_vF.pdf) · https://stockanalysis.com/stocks/v/statistics/ · https://finance.yahoo.com/news/visa-vs-mastercard-payments-giant-185000325.html · https://www.juniperresearch.com/press/agentic-commerce-set-to-generate-15-trillion-globally-by-2030-as-payments-infrastructure-leaders-revealed/ · https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook · https://www.nuvei.com/posts/nuvei-announces-completion-of-going-private-transaction
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> **Note:** the target news is a product announcement (agentic-commerce pilots with Nuvei/BBVA), not an earnings print. Visa is IR-covered, so this layer reviews Visa's own most recent reported quarter — **fiscal Q2 2026** (quarter ended 2026-03-31, released 2026-04-28) — as material context for the equity.

**Verdict (headline read).** **BEAT** · Net revenue $11.2B (+17% nominal, +16% constant-dollar; vs public consensus ~$10.69B → beat ~$0.5B / +5%) · non-GAAP EPS $3.31 (+20% YoY; vs consensus ~$3.09 → beat ~$0.22 / +7%) · driven by resilient payments volume and outsized data-processing + value-added-services growth · guidance reaffirmed (FY26 net-revenue growth low-double-digit to low-teens). Stock had run +8.4% into the print, so the beat drew a muted price reaction (analyst estimates revised up).

**Key figures (with growth, fiscal Q2 2026 vs Q2 2025).**
- Net revenue **$11.2B, +17%** nominal / **+16%** constant-dollar (prior-year Q2 FY25: $9.6B, +9%).
- GAAP net income **$6.0B (+32%)**, GAAP EPS **$3.14** (vs $2.32; ~+35%).
- Non-GAAP net income **$6.3B**, non-GAAP EPS **$3.31 (+20%)** (vs $2.76).
- GAAP operating expenses: **−4% YoY**, primarily a lower litigation provision (one-off tailwind to GAAP margin — de-PR flag, not operating leverage).
- Revenue lines (nominal YoY): Service **$5.0B, +13%** (recognized on prior-quarter volume); Data processing **$5.5B, +18%**; International transaction **+10%**; Other revenue **+41%** (value-added services); Client incentives (contra-revenue) **+14%**.

**Key business drivers (YoY, constant dollars).** Payments volume **+9%**; Cross-border volume total **+12%**, excluding intra-Europe **+11%**; Processed transactions **+9%** (66.1B, up from 60.7B). Service revenue is recognized on the prior quarter's payments volume, which grew **+8%** constant-dollar.

**By segment / driver.** Growth is led by (1) data processing +18% (processed-transaction volume + pricing/VAS), and (2) Other revenue +41% — value-added services is now the fastest-growing line and the strategic thrust behind moves like the agentic-commerce pilots in the target note. Cross-border +12% remains the highest-margin engine but is the slowest-accelerating of the volume metrics; international transaction revenue +10% trails data processing, worth watching. GAAP EPS (+35%) outran non-GAAP EPS (+20%) mainly because of the lower litigation provision (GAAP opex −4%), so the "clean" growth rate is the ~20% non-GAAP figure.

**vs expectations / prior period.** Beat on both lines vs public consensus (StockAnalysis/Zacks/Yahoo aggregators, as of the 2026-04-28 print): net revenue $11.23B vs ~$10.69B consensus (+5.0%); non-GAAP EPS $3.31 vs ~$3.09 (+7.1%). YoY momentum accelerated: net revenue growth stepped up to +17% from +9% in Q2 FY25 (`[[Visa Reports Fiscal First Quarter 2026 Results]]` prior print: $10.9B, +15%), i.e. sequential acceleration Q1→Q2 FY26 (+15%→+17%). Post-print, ~16 analysts revised estimates up; Zacks FY26 EPS moved to ~$13.01 (+13.4% implied).

**Guidance / forward (reaffirmed / consistent).**
- **Q3 FY2026:** net-revenue growth **low-double-digit**; operating-expense growth **low-teens**; diluted EPS growth **mid-to-high-single-digit**.
- **Full-year FY2026:** net-revenue growth **low-double-digit to low-teens**; operating-expense growth **low-double-digit to low-teens**; diluted EPS growth **low-teens**.
The Q3 EPS-growth guide (mid-to-high single digits) decelerates sharply from Q2's +20% actual — driven by rising opex (low-teens guide) for marketing, technology and strategic initiatives (incl. agentic commerce). This is a spend-up / margin-normalization signal management flagged, not a demand-weakness signal. Management tone: confident ("hyperscaler of payments globally," strong cash generation).

**Capital return.** Q2 FY26: **$9.2B returned** ($7.9B buybacks + $1.3B dividends); FY26 YTD **$14.3B** ($11.7B buybacks + $2.6B dividends) — supports EPS via shrinking share count.

**Thesis-flags.**
1. **Value-added services (+41% Other revenue) is the growth engine** → the Nuvei/BBVA agentic-commerce pilots in the target note sit inside this VAS/new-flows thrust → if agentic payments convert from pilot to live volume on Visa rails + tokens/Payment Passkeys, it defends Visa's role as the settlement layer as commerce shifts to AI agents (second-order: protects the network from disintermediation risk).
2. **Opex ramp / EPS-growth deceleration** → Q3 EPS-growth guide of mid-to-high single digits vs Q2's +20% actual, with opex guided low-teens → margin normalization as Visa invests; watch whether VAS/agentic revenue scales fast enough to justify the spend (second-order: near-term EPS-growth compression even as top-line stays strong).
3. **GAAP beat flattered by litigation provision** (GAAP opex −4%, GAAP EPS +35% vs non-GAAP +20%) → the durable growth rate is ~20% non-GAAP, not the GAAP headline (de-PR: don't extrapolate +32% net-income growth).
4. **Cross-border is the slowest-accelerating volume line (+12%)** and international transaction revenue (+10%) trails data processing (+18%) → the high-margin travel/cross-border engine is steady but not accelerating; a macro/travel slowdown would hit the richest revenue mix first.

Sources: Visa fiscal Q2 2026 earnings release (2026-04-28), 8-K & investor presentation — https://drive.google.com/file/d/1X9YkQAcH51_U9lg1phhxEHmDvWhOE2Bu/view (url fallback: https://s1.q4cdn.com/050606653/files/doc_financials/2026/q2/Q2-2026-Earnings-Release_vF.pdf) · prior-year Q2 FY2025 release (2025-04-29) · Q1 FY2026 release (2026-01-29) · public consensus / guidance / analyst reaction: Zacks/StockAnalysis/Yahoo & investing.com Q2 FY26 slides recap (as of 2026-04-28/30). International transaction & Other revenue $-levels not separately quoted in retrieved chunks (growth %: +10% / +41% from investor presentation) — [$-level UNSOURCED].
<!-- /enrichment:earnings_review -->
