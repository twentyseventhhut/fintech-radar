---
title: "PPRO launches council for local payment standards in agentic commerce"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - company/ppro
  - industry/payments
  - industry/agentic-commerce
  - region/europe
  - type/product
sources:
  - https://www.ppro.com/news/ppro-launches-local-payments-council-for-agentic-commerce
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sc8b0aaac
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# PPRO launches council for local payment standards in agentic commerce

> [!info] 2026-10-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌐 PPRO launches an industry council to develop technical standards for local payments in agentic commerce. Founding members include BLIK, EPI, Bancontact Company and DIAS, focusing on agent identity, authorisation, consent, disputes and refunds. Read more.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.ppro.com/news/ppro-launches-local-payments-council-for-agentic-commerce>

## Контекст

<!-- enrichment:context -->
### [0] What happened
On 2026-10-22, **PPRO** launched the **Local Payments Council for Agentic Commerce**, an industry body to develop common technical standards for how **local payment methods (LPMs)** plug into AI-agent-led checkout. Founding members: PPRO, **BLIK** (Poland), **EPI / Wero** (pan-European), **Bancontact Company** (Belgium) and **DIAS / IRIS** (Greece), with more schemes said to be committed. Stated scope spans five areas: (1) out-of-band authorisation and session hand-off, (2) agent identity and attestation for **non-card rails**, (3) consent, mandates and delegated authority, (4) disputes, refunds and liability, and (5) discoverability and agent-surface eligibility. CTO Alexander Matthey frames it as ensuring the rules for how LPMs work inside agentic protocols exist "from the outset." (Sources: [ppro.com](https://www.ppro.com/news/ppro-launches-local-payments-council-for-agentic-commerce), [Finextra](https://www.finextra.com/pressarticle/111391/ppro-launches-local-payments-council-for-agentic-commerce), [Financial IT](https://financialit.net/news/payments/ppro-launches-local-payments-council-agentic-commerce))

### [1] Who PPRO is / why it matters
PPRO (founded 2006) is a **local-payment-methods infrastructure aggregator** — "the layer behind the layer." A single API exposes 85–160+ LPMs/BNPL across 90+% of global GDP, with lifecycle, reconciliation and risk tooling; it processes ~US$20bn+ annually. Crucially, PPRO is wholesale: **Stripe, PayPal, Worldpay, JPMorgan and Citi resell LPMs through PPRO**, giving it leverage to convene schemes. The council matters because the loud agentic-commerce standards to date are **card- and US-centric**, while ~half of European/LATAM checkout runs on non-card LPMs (BLIK, Wero/EPI, Bancontact, iDEAL, Pix, Boleto). Without an LPM voice, agentic rails risk defaulting to cards. (Sources: [PPRO About](https://www.ppro.com/about-us/), [Fintech Magazine](https://fintechmagazine.com/news/ppro-the-local-payments-layer-behind-global-checkout))

### [2] Competitive / standards landscape
This council enters a crowded, card-dominated field of overlapping agentic-commerce protocols:
- **ACP (Agentic Commerce Protocol)** — OpenAI + Stripe, live in ChatGPT since Sep 2025, Apache-2.0, merchant stays merchant-of-record (see [[Stripe launches tools for German businesses to sell via AI agents]]).
- **AP2 (Agent Payments Protocol)** — Google, Sep 2025, 60+ partners (Mastercard, Amex, PayPal, Adyen, Worldpay, Coinbase), payment-agnostic (cards/stablecoins/bank transfer) (see [[Affirm to support Google's Agent Payments Protocol]]).
- **Visa TAP (Trusted Agent Protocol)** — Visa + Cloudflare, Oct 2025, agent-identity/trust directory (see [[Visa launches Trusted Agent Protocol for AI commerce]], [[Nuvei supports Visa Trusted Agent Protocol]]).
- **Mastercard Agent Pay** — live agent-led card transactions in pilots (see [[Mastercard opens Agent Pay for Machines early access]], [[Mastercard and PayPal partner on agentic commerce]]).
Analysts frame these as **stacking, not purely competing** (MCP/A2A connectivity → ACP/discovery → AP2 consent → TAP/Agent Pay identity). PPRO's council is positioned as the **non-card / LPM-specific standards layer** that none of the above fully address. (Sources: [Orium](https://orium.com/blog/agentic-payments-acp-ap2-x402), [Contra Collective](https://contracollective.com/blog/agentic-payments-protocols-mastercard-visa-stripe-2026))

### [3] Prior context / internal thread
PPRO has been building toward this for months: it named ex-Adyen CTO **Alexander Matthey** as CTO ([[Former Adyen CTO Alexander Matthey joins PPRO]]), then in Aug 2026 announced a **PPRO–BLIK agentic-commerce partnership** billed as one of the world's first LPM implementations for agent-initiated transactions (direct predecessor to this council). PPRO's broader LPM footprint: [[PayPal and PPRO add 30+ local payment methods]], [[PPRO and Coinbase partner on stablecoin payments for US merchants]], [[PPRO launches Buy Now Pay Local BNPL solution in Europe]]. The LPM schemes involved also sit inside Europe's payment-sovereignty push ([[Poland's BLIK joins pan-European cashless payments push]], [[Adyen joins European Payments Initiative as principal member]], [[Nopan and DIAS partner to expand IRIS Commerce internationally]]).

### [4] So what / forward look
A council is **governance, not a shipped standard** — the deliverable is specs, which take time and require schemes to actually implement. Value accrues to PPRO as the convener/distribution layer if LPMs become agent-addressable before card networks lock in defaults. Watch: whether additional big schemes (iDEAL/Currence, Pix/Banco Central, SEPA bodies) join; whether the council's output interoperates with (rather than forks from) AP2/ACP/TAP; and the first live non-card agent transaction at scale. Risk: fragmentation — yet another body in an already protocol-saturated space (see [[Fintech Brainfood the protocols for agentic banking and payments]]).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
1. Is this a **real standards body with deliverables**, or a marketing/PR convening with no published spec, timeline, or governance charter? (As announced it is the latter — scope areas only, no spec.)
2. Does PPRO **control** the council (convener + commercial beneficiary), creating a conflict where "open standard" really means "PPRO-routed LPM rails"?
3. Are the five founding members (PPRO, BLIK, EPI, Bancontact, DIAS) **enough critical mass**? Notably absent: iDEAL/Currence, Pix/Bacen, SEPA scheme owners, Klarna, Swish — without them "local payments" is partial.
4. Does this **duplicate or fork** existing work? AP2 already claims payment-agnostic support for bank transfers; could the council just re-solve what AP2/UCP cover, adding fragmentation?
5. Will card networks (Visa TAP, Mastercard Agent Pay) and OpenAI/Stripe (ACP) simply **ignore or out-run** an LPM council, given their head start and merchant/AI-platform distribution?
6. "Agent identity for non-card rails" — do LPMs even have the **identity/attestation primitives** to support this, or is the council describing a problem it can't yet solve technically?
7. What's the **adoption mechanism**? Standards bodies fail without reference implementations and mandated conformance; is there any?
8. Is the BLIK–PPRO Aug 2026 partnership the **only real implementation**, with the council a repackaging of a single-market pilot as an "industry" effort?
9. Liability/disputes/refunds for agent-initiated LPM payments touch **PSD2/PSD3 and SCA** — can a private council set rules regulators will accept, or does this need EBA/ECB buy-in?
10. How is this **funded and staffed**? No disclosed secretariat, dues, or IP/licensing model (vs ACP's Apache-2.0 openness).
11. Does the **15% of European e-commerce by 2030** agent-spend figure (PPRO's framing) hold up, or is it a vendor projection inflating urgency?
12. Could schemes join **nominally** (logo support) while actually building on AP2/TAP, leaving the council a talking shop?
13. Is there a **first-mover disadvantage** — setting LPM standards before agentic protocols stabilise risks obsolescence once ACP/AP2/TAP converge.
14. Does "discoverability and agent-surface eligibility" risk **gatekeeping** (who decides which LPMs an agent surfaces), inviting antitrust/scheme-neutrality scrutiny?

**Importance: 3/5** — Strategically meaningful: PPRO is a genuine LPM chokepoint and the non-card/LPM angle is a real gap in the card-centric agentic-commerce standards race, with credible European-sovereignty founders (BLIK/EPI/Bancontact/DIAS). But it is a *council announcement*, not a shipped standard — no spec, timeline, funding model, or regulator buy-in disclosed, and it enters an already protocol-saturated field (ACP/AP2/TAP/Agent Pay). Upgradeable to 4/5 if major schemes join and a conformant reference implementation ships; currently governance-stage signalling.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-22]] (2026-10-22).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: cross-border local-payment-method (LPM) aggregation × agentic-commerce standards. PPRO is an infrastructure/orchestration player (not a scheme) convening schemes to define how non-card, local rails plug into AI-agent checkout. Market context: agentic commerce is pre-standardised and card-first — the live protocols (Stripe/OpenAI ACP, Sept 2025; Visa Trusted Agent Protocol, Oct 2025; Mastercard Agent Pay/AP4M, 2026; Google AP2 / Universal Commerce Protocol, NRF Jan 2026) were built around card rails, leaving A2A/LPM schemes (BLIK, EPI/Wero, Bancontact, DIAS, iDEAL, Pix, etc.) without an agreed way to handle agent identity, delegated consent, out-of-band auth and dispute/refund liability (per Finextra/FinancialIT, 2026-10-22). Size: agentic commerce TAM is large but highly dispersed across estimates — Morgan Stanley $190–385bn US e-comm by 2030; Bain $300–500bn US; McKinsey up to ~$5tn global volume by 2030 (attribute: per Morgan Stanley/Bain/McKinsey via secondary citations, as of 2026 — treat as scenario ranges, not a hard TAM). Structure: fragmented on the scheme side (dozens of country-specific LPMs, each with its own governance) but consolidating fast around a few card-network-led agent protocols — the competitive tension this council addresses. Why now: card networks moved first (2025–26) and risk setting the de-facto agent standard; LPMs capture a large share of non-US checkout (PPRO's own prior work: 30+ LPMs added via PayPal, 2026-06; $633bn LATAM map, 2025-11), so schemes have a window to standardise before card-centric protocols entrench.

**Competitive landscape.** Sector KPIs run on: LPM coverage (# methods/markets), authorisation/conversion rate, settlement latency, and — new for agents — attestation/identity success rate and dispute-resolution SLA. Basis of competition: distribution (which schemes/PSPs adopt the standard) and governance legitimacy, not price. Key players by layer: (a) card-network agent protocols — Visa TAP, Mastercard Agent Pay/AP4M, Amex; (b) agent-checkout specs — Stripe/OpenAI ACP, Google AP2/UCP, Stripe+Tempo MPP (2026-03); (c) LPM/A2A schemes — EPI/Wero (57m users, A2A agent demo), BLIK (Poland; also partnered PPRO directly on agentic commerce, 2026-08), Bancontact, DIAS, iDEAL, Pix. Recent moves: Visa Trusted Agent Protocol (2025-10); Nuvei supports Visa TAP (2025-10); PayPal adopts ACP / Mastercard Agent Pay partnership (2025-10); Razorpay Agentic Payments on UPI (2025-10). PPRO's position: niche convener/orchestrator — it does not own a scheme or an agent protocol, so its leverage is as the neutral integration hub between LPMs and whatever protocol wins. Moat: distribution/intangibles — existing LPM connections and scheme relationships (network effects of being the shared rail), plus first-mover on a scheme-side standards body (analysis).

**Comps & multiples.** PPRO is private; no public trading multiples. Last disclosed valuation: unicorn, "over $1bn" per PPRO's own 2021 raise announcement; secondary trackers report a $1–2.5bn range (Dealroom/Tracxn, unverified). Most recent funding: ~€85m / ~$93m in Mar-2024 (PayPal Ventures follow-on, with Eurazeo, HPE Growth, J.P. Morgan, Citi Ventures, BlackRock-managed funds) — total raised ~$463m across 6 rounds per Tracxn (secondary, treat as indicative). Revenue: secondary sources cite UK filings of £50–100m (FY2024) and ~$53.7m (2025) — figures conflict and are not IR-confirmed → treat as "no data / [UNSOURCED]". Transaction volume: >$11bn processed in 2020 (last company-cited figure found); no current TPV disclosed → "no data". EV/Revenue, EV/EBITDA → not computable (private, no verified financials). Internal comps (agentic-commerce / LPM precedents in corpus): [[Visa launches Trusted Agent Protocol for AI commerce]], [[PayPal adopts Agentic Commerce Protocol, expands in ChatGPT]], [[Nuvei supports Visa Trusted Agent Protocol]], [[Razorpay launches Agentic Payments on UPI]], [[PayPal and PPRO add 30+ local payment methods]], [[PPRO maps $633 billion LATAM payments market for US merchants]]. Qualitative comparison only — distribution not computed (private subject, no comparable public peers at the orchestrator layer).

**Risk flags.** (1) Standards fragmentation / card-network pre-emption — the council launches AFTER card protocols are already live and being adopted; if Visa TAP / Mastercard Agent Pay / ACP entrench the agent-identity and consent layer first, an LPM-side standard risks becoming a downstream adapter rather than a peer standard (second-order: PPRO's convening value erodes if schemes individually bolt onto card protocols, as BLIK partly did directly). (2) Governance / adoption — a voluntary council of competing schemes (BLIK/EPI/Bancontact/DIAS) with no regulatory mandate is slow to converge; "launched" ≠ "adopted," and no technical spec, timeline or binding commitment has been published (de-PR: economics, liability allocation and who funds the standard are unstated). (3) Disintermediation of PPRO's own margin — if the council produces an open standard, schemes could integrate agent protocols directly (per the BLIK–PPRO and EPI/Wero agent demos), capturing the orchestration value PPRO monetises; PPRO benefits from the standard existing but not necessarily from owning the rail.

**What this changes (idea-lens).** This is a defensive, scheme-side counter-move to card-network dominance of agentic commerce — a bid to keep non-card LPMs relevant in AI checkout rather than a re-rating event (analysis). Falsifiable thesis: if, within ~12 months, the council ships a published technical spec adopted by ≥2 founding schemes in live agent checkouts, LPMs stay first-class in agentic commerce and PPRO cements a neutral-hub moat; trigger to watch = first interoperable spec + a named agent-protocol (ACP/AP2/TAP) bridge. What breaks the thesis: no spec, members integrating card protocols à la carte, or the council stalling as a PR body — in which case card networks set the agent standard and PPRO reverts to a connectivity vendor.

Sources: https://www.finextra.com/pressarticle/111391/ppro-launches-local-payments-council-for-agentic-commerce · https://financialit.net/news/payments/ppro-launches-local-payments-council-agentic-commerce · https://www.ppro.com/news/ppro-raises-180-million/ · https://fintech.global/2024/03/13/ppro-secures-e85m-in-landmark-funding-to-expand-global-payment-solutions/ · https://dealroom.co/companies/ppro/ · https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook · https://www.bain.com/insights/2030-forecast-how-agentic-ai-will-reshape-us-retail-snap-chart/ · https://www.juniperresearch.com/resources/blog/paying-at-agentic-speed-inside-visa-mastercard-and-stripe-s-agentic-commerce-push/ · https://worldline.com/en/home/main-navigation/resources/blogs/2026/wero-unlocking-pan-european-digital-commerce
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news** — PPRO is a privately held payments-infrastructure company (local payment methods / PSP enablement) and does not publish quarterly earnings; this item is a product/governance announcement (launch of a Local Payments Council for agentic commerce), not a results release. Below is a KPI snapshot from PPRO's own disclosures and public filings, in lieu of formal results.

**Latest disclosed metrics (dated):**
- **Valuation:** Unicorn since Jan-2021 — "over $1 billion" on the $180M round (TechCrunch, 2021-01-19); round later extended to ~$270M in Mar-2021 adding J.P. Morgan and Eldridge. (Note: the task's "~$2.6bn 2021 mark" is not supported by the sourced record — the publicly stated 2021 mark was >$1bn.) Private comps peg a Mar-2024 valuation near €1.4bn on a ~17.7x EV/Revenue multiple (multiples.vc) — [UNSOURCED on magnitude; aggregator estimate, not company-confirmed].
- **Funding:** €85M dual-tranche round announced 2024-03-13 (≈$93M); investors Eurazeo, HPE Growth, Sprints, PayPal Ventures (invested since 2018, follow-on), J.P. Morgan, Citi Ventures, BlackRock-managed funds. Cumulative ~$463M across five rounds since 2018 (aggregator). Primary: ppro.com/news/ppro-announces-85-million-funding/ · PayPal Ventures newsroom (2024-03-13).
- **Revenue:** FY2023 €67.4m (company "record revenue"; fintech.global 2024-03-13, per 2023 accounts); FY2022 ~£56m. Aggregator GetLatka est. ~$53.7m (as of Jul-2025) — [UNSOURCED estimate; conflicts with the €67.4m FY2023 filing figure, treat the €67.4m FY2023 as the firmer number].
- **Transaction / payment volume:** ~€20bn annual transaction volume (company "about us" / profile pages; undated steady-state figure). YoY volume doubled in Q4-2020 (last period-specific growth disclosed). No fresh 2024-2025 TPV growth rate disclosed — **no data**.
- **Profitability:** Not disclosed. At the 2024 round PPRO said it was "firmly on track to reach profitability" — i.e. not yet profitable as of Mar-2024, forward aspiration only. CFO Michelle Eischeid appointed 2025-07-07 "to support its next growth phase" (ppro.com) — consistent with a scale/pre-profitability posture. **No profit/margin figures available.**

**Reach (operating context, undated):** 85+ local payment methods activated across 85+ markets; network spanning 160+ methods and 100+ markets per company pages.

**Read:** N/A (no results) — private company, no beat/miss. Thesis note: the agentic-commerce council is a standards-positioning play, not a monetization event; revenue scale (€67m FY2023) remains small vs the ~€20bn volume it routes, and profitability is still forward-looking (Mar-2024 "on track"), so the near-term financial signal from this announcement is zero.

Sources: https://www.ppro.com/news/ppro-announces-85-million-funding/ · https://newsroom.paypal-corp.com/2024-03-13-PayPal-Ventures-Makes-Follow-on-Investment-in-PPRO · https://techcrunch.com/2021/01/19/ppro-nabs-180m-at-a-1b-valuation-to-bring-together-the-fragmented-world-of-payments/ · https://fintech.global/2024/03/13/ppro-secures-e85m-in-landmark-funding-to-expand-global-payment-solutions/ · https://getlatka.com/companies/ppro.com · https://multiples.vc/private-comps/ppro · https://www.ppro.com/news/ppro-appoints-michelle-eischeid-as-cfo/ — irdb/semsearch unavailable (OpenRouter 402); web fallback used.
<!-- /enrichment:earnings_review -->
