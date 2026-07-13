---
title: "Worldline, Credit Agricole, Mastercard complete first agentic payment in France"
date: 2026-06-29
retrieved: 2026-06-29
tags:
  - company/worldline
  - company/mastercard
  - industry/payments
  - industry/agentic-commerce
  - region/europe
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/0c03424c
  - https://www.connectingthedotsinfin.tech/r/994748d0
  - https://www.connectingthedotsinpayments.com/r/37f89196
  - https://www.connectingthedotsinpayments.com/r/d5882533
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s6dc9f881
month: 2026-06
enriched: true
importance: 2
freshness: fresh
---

# Worldline, Credit Agricole, Mastercard complete first agentic payment in France

> [!info] 2026-06-29 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇫🇷 Worldline, Crédit Agricole, and Mastercard have completed the first production agentic payment transaction in France, demonstrating secure AI-driven commerce. This first transaction confirms the partners' ability to deploy payment solutions for agentic commerce, from AI discovery to purchase, and support its development on a European scale.

[Connecting the Dots in Payments] 🇫🇷 Worldline, Crédit Agricole, and Mastercard have completed the first production agentic payment transaction in France, demonstrating secure AI-driven commerce. This first transaction confirms the partners' ability to deploy payment solutions for agentic commerce, from AI discovery to purchase, and support its development on a European scale.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/0c03424c>
- <https://www.connectingthedotsinfin.tech/r/994748d0>
- <https://www.connectingthedotsinpayments.com/r/37f89196>
- <https://www.connectingthedotsinpayments.com/r/d5882533>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Worldline, Crédit Agricole, Mastercard complete first agentic payment in France
_Analytical notes (not a post). Importance: 2/5._

**FRESHNESS VERDICT: fresh (but low-weight).** This is a genuinely distinct, dated event (25 Jun 2026, Crédit Agricole as issuer, Weezevent as merchant) — not a reprint of a prior corpus note. BUT it is the THIRD near-identical "first agentic payment" on the SAME Mastercard Agent Pay framework in ~4 months, and Worldline itself did "Europe's first … in production" with ING only ~3 weeks earlier (~2 Jun 2026). So: fresh event, recycled playbook. Related prior note in corpus: [[Worldline adds AI capabilities for agentic commerce]] (15 Jan 2026, the tooling that this transaction runs on).

## [0] What exactly happened (de-PR'd)
- **25 Jun 2026** (Worldline SA press release, carried on GlobeNewswire/Boursorama/Mastercard FR): "première transaction de paiement agentique réalisée **en production** en France."
- **What was actually done:** ONE end-to-end transaction. A Crédit Agricole customer used a "digital agent" to search festivals (budget/type/location); the agent proposed options; the customer chose, confirmed, and asked the agent to start the purchase on **Weezevent**; **payment settled only after explicit human validation**.
- **Not disclosed:** transaction amount, the AI agent/LLM behind the "digital agent", any volume beyond this single transaction, go-live/general-availability date.
- **Protocol:** Mastercard **Agent Pay** defines the purchase pathway; processed end-to-end on Worldline rails over the Mastercard network; Mastercard "specific identifiers" tag it as agentic for traceability. **No** Google AP2 / Visa TAP / Stripe-OpenAI ACP here.
- **Why framed this way → what it reveals:** "in production" = "ran once on production infrastructure", not "live commercial service." The human-in-the-loop ("settlement only after explicit validation") is not a UX nicety — it is the mechanism that keeps the **issuer (Crédit Agricole) in the SCA loop**, preserving PSD2 strong-customer-authentication compliance and the established liability shift. The geo-scoping ("first in **France**") is what makes a "first" claim survivable when the same partners already claimed Europe-firsts. → The real story is regulatory plumbing, not autonomy.

## [1] Competitors / peers (the "first" claims pile up)
- **Mastercard Agent Pay** unveiled **29 Apr 2025** (Microsoft, IBM, Braintree); US issuer enablement ~Nov 2025 (Citi, US Bank). France is a *deployment*, not new tech.
- **Mastercard + Santander + PayOS** — "Europe's first **live** end-to-end AI-agent payment", **~2-3 Mar 2026**; Agent Pay; explicitly a pilot, "not a commercial rollout."
- **Worldline + ING** — "Europe's first end-to-end agentic payment **in production**", **~2 Jun 2026** (Money20/20), NL/BE, concert tickets, Agent Pay. Near-identical ticket-buying script — same playbook three weeks before France.
- **Visa Trusted Agent Protocol (TAP)** — Oct 2025, w/ Cloudflare; "hundreds of agent-initiated transactions" claimed; part of Visa Intelligent Commerce (Anthropic, Microsoft, Mistral, Perplexity, Stripe).
- **Google AP2** — 16 Sep 2025, 60+ partners (Mastercard, Amex, PayPal, Adyen, Coinbase; not Visa at launch); donated to FIDO Alliance ~28 Apr 2026.
- **Stripe + OpenAI ACP / ChatGPT Instant Checkout** — Stripe Agentic Commerce Suite 11 Dec 2025; OpenAI reportedly scaled back in-chat checkout early 2026.
- **PayPal × Perplexity** — live US merchants since 2025; see corpus [[Mastercard and PayPal partner on agentic commerce]], [[PayPal integrates Mastercard Agent Pay into wallet]], [[Checkout.com adopts Agentic Commerce Protocol]].
- **+ Why the landscape looks like this:** US players ship in-chat checkout fast because there's no SCA gate; EU players must showcase market-by-market issuer-in-the-loop "firsts" because each national bank/regulator relationship is a separate unlock. None of the European "firsts" has disclosed GMV/merchant counts — they remain inaugural, not scaled.

## [2] Company history / fit
- [[Worldline adds AI capabilities for agentic commerce]] (15 Jan 2026, Paris): capability/tooling — MCP servers bridging LLMs to payment APIs, a "ConnectAI" hub for merchants/devs, stated support for AP2/UCP and EU rules, cited McKinsey $3-5T-by-2030.
- Trajectory: **Jan 2026 tooling → 2 Jun 2026 ING "Europe's first" → 25 Jun 2026 Crédit Agricole "first in France."**
- **+ Why Worldline acts this way:** Worldline is under heavy strategic/financial pressure (commodity acquiring economics, depressed equity) and needs an innovation narrative. Racking up "agent-ready" market firsts with bank + Mastercard partners is a cheap, high-visibility way to signal leadership without disclosing economics. (analysis)

## [3] Novelty / value-add / traction
- **Novelty: modest, jurisdictional.** Same Agent Pay framework, same human-in-the-loop pattern as Santander (Mar) and ING (Jun 2). The only delta is *France + the specific Crédit Agricole/Weezevent trio* — not a new protocol or autonomous capability.
- **Traction: absent from sources.** No volumes, GMV, merchant counts, go-live dates, or consumer availability for ANY of these European firsts. By Forrester's stricter definition this is *human-in-the-loop AI-assisted payment*, not autonomous "agentic." Forrester: only 24% of US adults trusted AI for routine purchases (Mar 2025).
- **+ Who captures the margin:** the network (Mastercard) owns the framework and the agentic transaction identifier — i.e., the rails and the rule-making. Worldline supplies processing (commodity-ish); the bank supplies authentication. → If agent payments scale, value concentrates with the **network**, not the acquirer doing the "first." Worldline risks being the visible demo partner while Mastercard captures the durable rail economics. (analysis)

## [4] What's next / market sentiment
- McKinsey: agentic commerce could orchestrate ~$1T US / $3-5T global retail by 2030 — a TAM forecast vendors (incl. Worldline) repeat as marketing, not booked revenue.
- Expect: more country "firsts", extended pilots, protocol consolidation (AP2 → FIDO; Mastercard "Agent Pay for Machines" for M2M, Jun 2026), and a standards fight (Agent Pay vs Visa TAP vs AP2 vs ACP).
- **Risks:** fraud/liability for agent-initiated transactions is unresolved. Under PSD2 SCA, liability sits with the issuer once SCA completes, but shifts to whoever applies an exemption (often merchant/acquirer). Agent flows complicate "cardholder intent" and dispute evidence — the EU issuer+acquirer+network trio is partly a workaround to keep SCA satisfied and liability allocatable.
- **+ Counterintuitive second-order:** the very "human validates before settlement" design that makes these compliant also makes them *not actually agentic* — so the EU is structurally slower to reach autonomous agent commerce than the US, regardless of how many "firsts" get announced.

## Sources
- GlobeNewswire / Mastercard FR press release, 25 Jun 2026 (France transaction).
- Galitt/adnews independent write-up; Boursorama; Zonebourse.
- Worldline ING release ~2 Jun 2026; Worldline "AI capabilities" 15 Jan 2026.
- Santander/Mastercard 2-3 Mar 2026; Mastercard Agent Pay 29 Apr 2025; Agent Pay for Machines Jun 2026.
- Google AP2 (16 Sep 2025); Visa TAP (Oct 2025); Stripe ACP (11 Dec 2025); Forrester agentic-payments blog; McKinsey agentic-commerce report.
- Corpus: [[Worldline adds AI capabilities for agentic commerce]], [[Mastercard and PayPal partner on agentic commerce]], [[PayPal integrates Mastercard Agent Pay into wallet]], [[Checkout.com adopts Agentic Commerce Protocol]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 2/5.** A real, dated national-first event, but a single inaugural transaction on a recycled framework (3rd Mastercard Agent Pay European "first" in 4 months; Worldline+ING did "Europe's first in production" 3 weeks earlier). Newsworthy as a marker of EU agentic-commerce rollout; thin on substance and traction.

## Top challenge / red-team questions

1. **"In production" or a one-off showcase?** — Largely a one-off: wire says "réalisée en production" but no volume/GA/availability. Galitt frames it as a first "concretization." Production rails, single transaction.
2. **Volume/GMV since launch?** — Open. Not disclosed.
3. **Transaction amount?** — Open. Not disclosed.
4. **Which AI agent/LLM powered the "digital agent"?** — Open. Not named in any source.
5. **A new protocol?** — No. Mastercard Agent Pay, same as Santander (Mar) and ING (Jun 2) events.
6. **Truly autonomous (agentic)?** — No. Human explicitly validates before settlement → human-in-the-loop AI-assisted payment (Forrester's strict definition would not call this agentic).
7. **Is "first in France" defensible?** — Plausibly as a narrow national-first, but it's the 3rd near-identical Agent Pay European "first" in ~4 months. "First" is geo-scoped marketing.
8. **Did anyone do agentic payments earlier globally?** — Yes: Agent Pay since Apr 2025; Visa TAP "hundreds of transactions" Oct 2025; US ChatGPT/Stripe ACP and PayPal×Perplexity live in 2025.
9. **Who bears fraud liability if an agent buys wrongly?** — PSD2 SCA: issuer once SCA completes; shifts to whoever applies an exemption. Agent-specific rules: open/unsettled.
10. **How is SCA satisfied for an agent-initiated payment?** — Crédit Agricole (issuer) retains authentication/authorization; Mastercard identifiers tag it agentic. Exact SCA mechanics/exemptions: open.
11. **Is Weezevent live for all customers or a pilot integration?** — Open. Sources describe one demonstrated purchase, not general availability.
12. **Does it use Google AP2 / Visa TAP / Stripe-OpenAI ACP?** — No. Mastercard Agent Pay. (Worldline separately supports AP2/UCP per its Jan 2026 release.)
13. **Is consumer demand real?** — Weak signal: Forrester, only 24% of US adults trusted AI for routine purchases (Mar 2025).
14. **Are the McKinsey $3-5T figures credible?** — They are TAM forecasts, not realized revenue; repeated by vendors (incl. Worldline) as marketing. Treat as scenario.
15. **What's genuinely differentiated vs the ING deal 3 weeks earlier?** — Mainly jurisdiction + the specific issuer (Crédit Agricole) and merchant (Weezevent). Same Worldline+Mastercard tech and human-in-loop UX. Differentiation is thin.
16. **Who captures the durable margin?** — Mastercard (owns Agent Pay framework + the agentic transaction identifier/rail). Worldline risks being the demo partner while the network keeps the rail economics. (analysis)
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-29]] (2026-06-29).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic payments = AI agents executing card-rail transactions end-to-end (discovery → checkout) under explicit consumer consent. This is a production "first" in France (announced 2026-06-25), not a commercial rollout — one Crédit Agricole customer buying a festival ticket on Weezevent, with the issuer retaining authentication/authorization (per Mastercard/Worldline press release, 2026-06-25). No TAM disclosed for agentic commerce — "no data"; treat any vendor "$X trillion agentic" figure as PR, not sourced. The real driver is the 2025-26 protocol land-grab: Mastercard Agent Pay (Apr-2025) and "Agent Pay for Machines"/AP4M (Jun-2026), Visa Intelligent Commerce + Trusted Agent Protocol (Sep-2025), Google AP2 (Sep-2025, 60+ partners incl. Mastercard/Amex/PayPal/Coinbase) — all settlement-agnostic (card / bank / stablecoin). Why now: LLM agents are crossing into transaction initiation, and the networks are racing to insert tokenized, scoped credentials before stablecoin/open protocols capture the machine-to-machine layer. Structure: highly consolidated at the network tier (Visa/Mastercard duopoly), fragmented and capital-intensive at the acquirer/processor tier (Worldline's layer).

**Competitive landscape.** Sector KPIs: networks run on GDV/switched transactions and net-revenue yield; acquirers/processors on TPV, take rate, per-transaction margin. Mastercard Q3-2025: net revenue $8.60bn (+17% y/y), GDV $2,747bn (+9% LC), 45.4bn switched transactions (per MA 8-K / earnings release, 2025-10-30). Worldline FY2025: revenue €4,030m (-2.7% y/y), adj. EBITDA €737m (18.3% margin) (per Worldline FY2025 release, 2026-02-25). Basis of competition: at the network layer — protocol/standard control and trust/tokenization; at Worldline's layer — distribution via bank partners and processing scale. Recent moves: Mastercard AP4M (Jun-2026); Worldline "AI for agentic commerce" (2026-01-16, see internal comp); FIS bank-enablement offering (2026-01-13); PayPal on Agentic Commerce Protocol / ChatGPT (2025-10-29); Stripe AI-payments acquisitions (2025-08-03). Position: Mastercard is *ahead* — it owns the rail, the token standard (MDES-based Agentic Tokens) and the moat (network effects + scale). Worldline is a *participant/integrator*, not the standard-setter — it contributes processing and a bank relationship (Crédit Agricole), capturing acquirer economics on a network-controlled flow (analysis).

**Comps & multiples.** Same-model test fails Worldline vs Mastercard (network vs processor, opposite scale/trajectory) — compare qualitatively, not on one multiple.
- Worldline (EPA:WLN): EV ~€4.7bn, net debt ~€2.2bn, market cap ~€0.7bn USD (per stockanalysis/companiesmarketcap, May-Jun 2026). EV/Revenue = €4.7bn / €4.03bn = **~1.2x**; EV/EBITDA = €4.7bn / €0.74bn = **~6.4x** (third-party quotes ~6.7x). Equity has collapsed -94% over 52wks after a €4.7bn FY2025 goodwill impairment and a Jun-2026 reverse split — *deep-distress / cheap*, value sits in debt, not equity.
- Mastercard (MA): trades at premium network multiples (high-teens revenue growth, ~50%+ EBIT margins) — *rich, justified by growth + moat*; precise EV/Rev and EV/EBITDA = `[UNSOURCED]` (no free current market-cap figure in results).
- Distribution not computed (only one comparable EV pair; 2 names, opposite categories) — qualitative comparison only.
Internal comps: [[Worldline adds AI capabilities for agentic commerce]] · [[Worldline completes divestments as revenues beat expectations]] · [[Worldline buys remaining Eurobank Greek merchant stake for €72 million]] · [[PayPal adopts Agentic Commerce Protocol, expands in ChatGPT]] · [[Stripe buys three firms to build AI-powered payments]] · [[FIS launches offering to scale banks in agentic commerce]].

**Risk flags.**
1. **Disintermediation / value capture by another stack layer (Worldline).** The token standard and trust layer sit with Mastercard; Worldline supplies commoditizable processing. If agentic flows route through network-owned tokens + bank issuers, the acquirer/processor's per-transaction economics stay thin while the network captures the premium — second-order: a "first" headline does not move Worldline's earnings.
2. **Balance-sheet / going-concern overhang (Worldline).** €2.2bn net debt, €4.7bn impairment, -94% equity, reverse split — innovation PR is competing against a solvency narrative; agentic upside is a multi-year option, the debt is near-term.
3. **Regulation & fraud-liability silence.** Press release is explicit on consent/authentication but silent on who bears fraud liability for agent-initiated purchases and on PSD2/SCA treatment of an AI-initiated transaction — unresolved liability could stall the move from "production demo" to scaled deployment.

**What this changes (idea-lens).** This is a demo/standards milestone, not a re-rating event (analysis) — the falsifiable thesis: agentic commerce accrues to the *network* (Mastercard) and *issuer* (Crédit Agricole), not the processor (Worldline), so watch for the first disclosed agentic *volume/take-rate* metric rather than more "first transaction" PR. Trigger that would flip it: Worldline disclosing agentic-commerce revenue or an exclusive processing standard; what makes the thesis wrong: open protocols (Google AP2) commoditizing the network token and shifting value back to processors/banks.

Sources: https://www.mastercard.com/news/europe/fr-fr/salle-de-presse/communiques-de-presse/fr-fr/2026/worldline-le-credit-agricole-et-mastercard-realisent-la-premiere-transaction-de-paiement-agentique-en-france/ · https://investors.worldline.com/en/home/news-events/financial-press-releases/2026/pr-2026_02_25_02 · https://www.sec.gov/Archives/edgar/data/0001141391/000114139125000191/ma09302025-exx991xearnings.htm · https://stockanalysis.com/quote/epa/WLN/statistics/ · https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html · IR(MA): https://www.sec.gov/Archives/edgar/data/1141391/000114139125000191/ma09302025-exx991xearnings.htm (drive: https://drive.google.com/file/d/1JBOcO6r0BKuvnugiO5lUR3g2bEFPbKVF/view)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** BEAT (Mastercard, the IR-covered + most material partner here — Worldline is not IR-covered in this pipeline; Crédit Agricole is private to this story). Latest print = **Q1 2026** (period ended 2026-03-31, released 2026-04-30; fresh, ~2 months pre-news). Net revenue **$8.4bn (+16% YoY; +12% currency-neutral)** vs public consensus ~$8.25bn → modest beat. Adjusted diluted EPS **$4.60 (+23% YoY)** vs public consensus ~$4.41 → ~4% beat. Driver: value-added services & solutions (+22% reported). Full-year 2026 net-revenue guidance reaffirmed (high end of low-double-digit, currency-neutral). NB: this earnings layer is general context — the news itself (first production agentic-payment transaction in France with Worldline + Crédit Agricole) is a product milestone, NOT a results event; no agentic-commerce revenue is disclosed in any filing.

**Key figures (Q1 2026, with growth).**
- Net revenue **$8,398m / $8.4bn — +16% reported, +12% currency-neutral** (vs $7,250m / $7.3bn Q1 2025).
- Payment network revenue **$4,948m (+12% reported)**; value-added services & solutions **$3,450m (+22% reported; +18% currency-neutral)** — VAS again the faster-growing leg.
- Operating income **$4.9bn (+18% reported, +13% c-n)**; operating expenses **$3.5bn (+13% reported)**.
- Operating margin **58.4%** (+1.2 ppt YoY; +0.6 ppt c-n); adjusted operating margin in the ~66% area (adj. opex $3.3bn, +11%). Effective tax rate 19.3% (vs 18.6%).
- Net income **$3.9bn (+18% reported, +13% c-n)**; diluted EPS **$4.35 (+21% reported, +16% c-n)**. Adjusted net income **$4.1bn**; adjusted diluted EPS **$4.60 (+23%)**.
- Key business drivers (local-currency basis, YoY): gross dollar volume **+7%**, cross-border volume **+13%**, switched transactions **+9%** — cross-border the standout, consistent with travel/e-commerce strength.
- Capital return: repurchased 7.8m shares for $4.0bn and paid $777m dividends in Q1; a further 3.3m shares for $1.7bn through Apr 27, ~$11.7bn remaining on authorization.

**By segment / driver.** Growth is two-engine: the core network (payment-network +12% reported) plus the higher-multiple VAS leg (+22% reported / +18% c-n), which keeps lifting blended take-economics and is the structural growth story this agentic-payment news plugs into (cyber/identity/agentic rails are VAS-adjacent). Cross-border +13% (local FX) outpaced domestic GDV +7%, the usual high-margin mix tailwind.

**vs expectations / prior period.** Net revenue $8.4bn vs public consensus ~$8.25bn = small beat (~+1.8%); some trackers cite a higher whisper (~$8.49bn), so the top-line beat is modest, not blowout. Adjusted EPS $4.60 vs ~$4.41 public consensus = ~+4.3% beat, the cleaner surprise. Versus prior year: revenue +16%, adj. EPS +23% — acceleration vs the +13–14% revenue cadence seen across 2024–2025 quarters in the corpus (Q3'25 net revenue $8.6bn; Q2'25; Q3'24 $7.4bn), helped by FX turning to a tailwind. (Public consensus figures from aggregators "as of" the 2026-04-30 print; marked public consensus, not paid Street.)

**Guidance / forward.** Reaffirmed, not raised. Full-year 2026 net revenue guided at the **high end of a low-double-digit range (currency-neutral)**, with an additional **~1.5 ppt FX tailwind**. **Q2 2026** flagged at the **low end of a low-double-digit range** due to Middle East conflict-related pressure; ex-conflict, management said Q2 growth would be "generally in line with the first quarter." Tone: confident — CEO Michael Miebach: "Building on 2025 momentum, '26 is off to an excellent start." De-PR flag: the only soft spot management volunteered is the geopolitical/Q2 trims and "April trends soften" commentary — they led with VAS and cross-border, said less about the GDV deceleration to +7%.

**Thesis-flags.**
1. VAS +22% (reported) keeps outgrowing the network → why it matters: it is the higher-margin, less-regulated growth engine, and agentic-commerce security/identity rails (this France milestone) sit inside that engine → second-order: a credible new VAS volume vector if agentic payments scale on a European basis.
2. Cross-border +13% vs GDV +7% → high-margin mix still expanding margins (58.4%, +1.2 ppt) → matters because it cushions the Q2 conflict trim → but watch the "April trends soften" comment for early consumer-spend deceleration.
3. Guidance reaffirmed (not raised) despite the EPS beat + a Q2 trim → management is banking the beat, not extrapolating it → sandbag-vs-caution read: prudent given Middle East exposure, low downgrade risk.
4. Story-specific: the agentic-payment "first" is a product/standards milestone with **no disclosed revenue, volume, or economics** in any Mastercard filing — treat as optionality, not a numbers catalyst (analysis).

Sources: Q1 2026 8-K/EX-99.1 earnings release (primary) https://www.sec.gov/Archives/edgar/data/1141391/000114139126000029/ma03312026-exx991xearnings.htm (drive: https://drive.google.com/file/d/1PfMtcgFCMGzKj_oMVYlLz045VyiiHKMb/view) · Q1 2026 earnings release PDF https://s25.q4cdn.com/479285134/files/doc_financials/2026/q1/1Q26-Mastercard-Earnings-Release.pdf (drive: https://drive.google.com/file/d/1neT4u3dNKpZc5-MnUustCIvl24cqjH1Z/view) · Q1 2026 10-Q https://www.sec.gov/Archives/edgar/data/1141391/000114139126000031/ma-20260331.htm (drive: https://drive.google.com/file/d/1f5KQEcbgSHoIieSGWbhRgfCm8ToSKpiO/view) · Q1 2026 earnings presentation drive: https://drive.google.com/file/d/1O2gXHXO3ajFlWu16e2STOu59GSBUvMUb/view · public consensus + guidance/transcript color (aggregators, "as of" 2026-04-30): MLQ News, TIKR, Investing.com Q1 2026 earnings-call transcript · Worldline & Crédit Agricole results: no data (Worldline not IR-covered in this pipeline; not material to verdict).
<!-- /enrichment:earnings_review -->
