---
title: "Airwallex launches AgentOS AI toolkit for financial workflows"
date: 2026-07-02
retrieved: 2026-07-02
tags:
  - company/airwallex
  - industry/ai
  - industry/payments
  - region/global
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/d2a2dafc
  - https://www.connectingthedotsinfin.tech/r/a0f3f61a
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sb248c5c7
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Airwallex launches AgentOS AI toolkit for financial workflows

> [!info] 2026-07-02 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Airwallex has launched AgentOS, an AI toolkit that enables agents on platforms such as Claude, Cursor, and OpenAI to manage end-to-end financial workflows. The solution helps businesses unify financial data, automate cash management, execute transfers and currency conversions, and use AI to forecast liquidity and future cash flows.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/d2a2dafc>
- <https://www.connectingthedotsinfin.tech/r/a0f3f61a>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Airwallex launches AgentOS AI toolkit for financial workflows
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-07-02 Airwallex announced **AgentOS**, a toolkit that lets AI agents in Claude (Code / Cowork), Cursor and OpenAI Codex operate a business's Airwallex account. Three components: (a) **connectors** — an Airwallex CLI + an **MCP server** (Model Context Protocol) for the production account, plus a separate Developer MCP for docs/sandbox; (b) **Skills** — prebuilt workflows (contract→billing, beneficiary creation, card provisioning, cash management), explicitly labelled **beta** in Airwallex's docs; (c) **Plugins** — one-click install into Claude/Cursor/Codex, or "any MCP-compatible agent". Plugins/connectors are **live to download**; Skills are beta. Auth is OAuth against the live account.

**The de-PR'd core.** The digest line says agents "execute transfers and currency conversions" and "forecast liquidity". Airwallex's own developer docs contradict this: *"AgentOS components do not initiate money-out actions (transfers, FX conversions, or payouts) on your behalf."* So AgentOS today = **reads + non-money-moving writes** (query balances, analyse receivables/payables, create invoices/billing terms, provision cards) — NOT autonomous money movement. → Why framed this way: the scary-but-valuable capability (an LLM autonomously moving corporate cash/FX) is exactly what is withheld, because fraud liability and prompt-injection risk on production credentials are unresolved. The PR anchors to the exciting frame; the docs quietly cap the surface. That gap IS the story.

## [1] Competitors / peers
Agentic-payments tooling has been crowded for a year, and the corpus is dense with MCP launches:
- **Mollie MCP** ([[Mollie introduces Mollie MCP server for AI agents]], 2025-07) — merchant-ops MCP.
- **Coinbase Payments MCP / x402** ([[Coinbase launches Payments MCP for AI agents]], 2025-10) — onchain agent payments.
- **Worldpay MCP** ([[Worldpay launches Model Context Protocol server for agentic commerce]], 2025-11) — publicly available server over Worldpay APIs.
- **Omise MCP, 60+ tools** ([[Omise debuts MCP server for agentic payments with 60+ tools]], 2025-12) — Asia.
- **Nexi agentic commerce MCP** ([[Nexi launches agentic commerce capabilities for AI agents]], 2026-03).
- **Pleo agentic capabilities** ([[Pleo unveils new agentic AI capabilities for financial management]], 2026-06) — closest peer: agent-native spend/finance ops with a Policy Agent (live) + Pleo MCP (next).
- Protocol layer: [[Fintech Wrap Up ACP vs AP2 agentic payments comparison]] (2026-03) frames Stripe/OpenAI **ACP** vs Google **AP2**; add Visa Intelligent Commerce / Mastercard Agent Pay, and PayPal's Agent Toolkit ([[PayPal advances agentic commerce with Perplexity and MCP]], 2025-07).

→ Position: on the *consumer-checkout* axis (agent buys goods for a person — Stripe/Visa/Mastercard/Google/PayPal) Airwallex is **not competing** and is behind by design. On the *B2B treasury / cross-border FX / back-office finance-ops* axis (agent operating a business's financial stack), it is **at parity or slightly ahead** vs an emptier field — Pleo is the only tight comp, and Pleo is spend-management, not cross-border FX/treasury. Why the field is empty there: incumbents chased the shiny consumer-checkout narrative; the boring back-office CFO workflow is where Airwallex's existing API surface (multi-currency accounts, cards, billing, Yield, Leapfin data) is uniquely broad.

## [2] Company history / fit
Airwallex is a well-capitalised, profitable cross-border infra incumbent, and AgentOS fits its 2026 "AI-native finance" push exactly. Trajectory: $330M Series G at $8B ([[Airwallex raises $330M Series G at $8B valuation]], 2025-12) → EBITDA-profitable while crossing $1B annualised revenue ([[Airwallex crosses $1B annualized revenue]], 2025-11; [[Connecting the Dots how Airwallex reached $1B ARR profitably]]) → $200B+ then $266B+ annualised TPV ([[Airwallex hits $200 billion in annual transaction volume]], 2025-08) → **$320M Series H at $11B valuation** ([[Airwallex raises $320M Series H at $11 billion valuation]], 2026-06), raised explicitly "to accelerate autonomous finance and agentic commerce". In the same June window it shipped the **Airi** consumer wallet ([[Airwallex launches Airi one-click consumer checkout wallet]], 2026-06-29) and teased T:0 (an AI-agent-run finance platform, private beta). It has been assembling the pieces AgentOS exposes: **Airwallex Billing** ([[Airwallex launches modular Airwallex Billing platform for global businesses]]), **OpenPay** billing acquisition, **Leapfin** financial-data acquisition ([[Airwallex acquires financial data platform Leapfin]], 2026-06), Yield. → Why: a cross-border take-rate is a commoditising business; Airwallex needs a software/"platform" multiple, so it wraps its broad API in an agent-native control plane to become the surface agents build finance ops on. AgentOS is the developer/agent-tooling layer beneath Airi (consumer) and T:0 (autonomous) — the three are distinct, and AgentOS is the first of the three to actually go live for install.

## [3] Novelty / value-add / traction
Genuinely new: little — it is largely an **MCP + CLI wrapper plus prebuilt prompt "Skills" over the existing Airwallex API**, distributed via Claude/Cursor/Codex plugin directories. MCP-over-payments-API is a 12-month-old pattern (Mollie, Worldpay, Omise, Nexi, Coinbase above). The real, modest novelty is being **early with a production-account MCP specifically for cross-border business *treasury* ops** (balances, cards, invoicing, cash management) rather than consumer checkout — a whitespace vs the checkout crowd. Traction: **zero named customers, no usage/volume, no pricing** disclosed; Skills in beta. → Who captures the margin: value accrues to whoever becomes the *system of action* an agent calls to run a company's money. Airwallex's edge is breadth of underlying rails; the risk is that agent platforms (Anthropic/OpenAI) and card networks (Visa/Mastercard agent rails) sit above and commoditise the MCP layer, leaving Airwallex a "connector" not "the one who pays" — precisely mirrored by AgentOS *disabling money-out*, which for now keeps it a read/analytics surface, not the payer.

## [4] What's next / market sentiment
Expect money-out execution (transfers/FX/payouts) with per-agent spend limits and delegated authorization to arrive next — Airwallex has promised delegated agent payments/spend limits for **Airi "in coming months"** and positions T:0 (beta) as the autonomous-finance endgame; AgentOS would inherit those controls. Sentiment: the $11B/June raise and EBITDA profitability give it runway to fund a multi-year agent bet without needing near-term monetisation. Regulatory/risk backdrop is the gating factor: an LLM holding production OAuth credentials on full financial data is a **prompt-injection / data-exfiltration** surface even before money moves; and note Airwallex already faces AML scrutiny ([[AUSTRAC orders external audit of Airwallex over AML]], 2026-01), so autonomous money movement will be conservative by necessity. → Second-order: the winner of B2B agentic finance is likely decided not by who ships the first MCP but by who solves **agent authorization + liability** credibly at enterprise scale — a governance problem, not a demo. AgentOS is a credible early land-grab on that surface, not a category-defining launch.

## Freshness verdict
**FRESH.** AgentOS is a distinct new product — the developer/agent-tooling layer — not a reprint of the Airi consumer-wallet launch ([[Airwallex launches Airi one-click consumer checkout wallet]]) nor the Series H raise ([[Airwallex raises $320M Series H at $11 billion valuation]]). No prior note covers AgentOS or an Airwallex MCP. New capability + new date.

## Sources
- Airwallex AgentOS blog: https://www.airwallex.com/global/blog/introducing-airwallex-agentos-manage-your-financial-operations-in-your-preferred-agent-environment
- Airwallex AgentOS docs (money-out disclaimer): https://www.airwallex.com/docs/developer-tools/ai/agentos
- Airwallex AgentOS landing: https://www.airwallex.com/agentos
- Series H / scale: https://www.businesswire.com/news/home/20260625434997/en/Airwallex-Secures-$320-Million-in-Series-H-Funding-Valuation-Hits-$11-Billion ; https://sacra.com/c/airwallex/
- Competitor protocols: https://stripe.com/newsroom/news/stripe-openai-instant-checkout ; https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol ; https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- Digest primaries: https://www.connectingthedotsinfin.tech/r/d2a2dafc ; https://www.connectingthedotsinfin.tech/r/a0f3f61a
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Can AgentOS actually move money?** No — Airwallex docs state components "do not initiate money-out actions (transfers, FX conversions, or payouts)". So the digest claim that agents "execute transfers and currency conversions" is **contradicted by the primary source**. Today it is reads + non-money-moving writes.
2. **Is this really new, or an MCP wrapper over the existing API?** Largely the latter — an MCP server + CLI + prebuilt "Skills" over Airwallex's existing API. The pattern (payments-API-over-MCP) is ~12 months old (Mollie, Worldpay, Omise, Nexi, Coinbase). Novelty = being early on *cross-border business treasury* ops specifically.
3. **Announced or live?** Plugins/connectors live to install; **Skills are beta** ("behavior may change before GA"). Mixed.
4. **Any named customers or usage numbers?** None disclosed — zero reference clients, no volume, no adoption metrics. Open.
5. **Pricing?** Not disclosed. Open.
6. **How is an agent authorized / spend-limited?** No documented per-agent spend limits or granular permissions beyond OAuth credential scope. The delegated-payments/spend-limit story is promised for Airi "in coming months", not shipped in AgentOS.
7. **Fraud / liability for autonomous actions?** Silent. Unresolved — and plausibly why money-out is disabled.
8. **Security of an LLM holding production OAuth creds?** Prompt-injection → data-exfiltration risk exists even on read-only access to full financial data. Not addressed publicly. Open.
9. **How does this differ from Airi and T:0?** AgentOS = developer/agent-tooling layer (B2B ops); Airi = consumer one-click wallet (2026-06-29); T:0 = AI-agent-run finance platform (private beta). Distinct products — confirms this note is fresh, not a duplicate.
10. **Who's the real competitor?** Not Stripe/Visa/Mastercard/Google (consumer checkout, different game); the tight comp is Pleo (agentic spend/finance ops), and even Pleo lacks cross-border FX/treasury breadth.
11. **Where does the margin accrue?** To whoever becomes the "system of action" agents call to run company money. Risk: agent platforms + card networks sit above and commoditise the MCP layer → Airwallex stays a "connector", not the payer — mirrored by money-out being disabled.
12. **Does it fit the strategy?** Yes — commoditising cross-border take-rate needs a software multiple; wrapping a broad API (Billing, Yield, cards, Leapfin data) in an agent control plane is a coherent land-grab, funded by the $11B Series H.
13. **What would upgrade importance?** Money-out execution + granular authorization + named enterprise adopters going live. Absent those, it's positioning.
14. **Regulatory overhang?** Airwallex is under AUSTRAC AML audit (2026-01); autonomous money movement will be conservative by necessity.
15. **Is the whitespace real or will incumbents fill it fast?** Whitespace in B2B treasury-ops MCP is real today, but the win is decided by solving agent authorization + liability at enterprise scale (governance), not by shipping the first MCP.

Importance: 3/5 — A well-capitalised ($11B, EBITDA-profitable, ~$266B TPV) incumbent making a credible, early land-grab on agent-native B2B *treasury* tooling — a genuine whitespace vs the consumer-checkout crowd — and shipping now via major agent platforms. But near-term substance is thin: money movement disabled, Skills beta, no customers, no pricing, and the autonomous vision lives in still-beta Airi/T:0. Worth tracking, not category-defining. Not a 4/5 until money-out + named adopters land; not a 2/5 because the strategic positioning and distribution are real.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-04]] (2026-07-04).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** AgentOS drops Airwallex into the agentic-payments / AI-agent financial-infrastructure race — one of the hottest fintech subverticals of 2025–26. Market-size claims are wide and unverifiable (extract, don't endorse): Juniper Research projects agentic-commerce transaction value rising from ~$8bn in 2026 to $1.5tn by 2030 (per Juniper via Stellagent, as of 2026); McKinsey QuantumBlack estimates $3–5tn of retail spend orchestrated by agents by 2030 (Oct 2025); Bain ~$300–500bn US and Morgan Stanley ~$190–385bn US by 2030 — a >10x spread that itself is the signal: TAM is a guess, direction agreed. Structure: value is bifurcating. The **network/token rail layer** is consolidating fast around incumbents — Mastercard Agent Pay (announced 2025-04-29, Agentic Tokens on MDES), Visa Intelligent Commerce / Trusted Agent Protocol (Sep 2025), Stripe provisioning agentic network tokens with Visa/Mastercard (2026). The **enterprise-workflow / treasury-execution layer** — where AgentOS plays — is still fragmented and un-owned. Why now: MCP/agent platforms (Claude, Cursor, OpenAI) became a distribution surface in 2025, and Airwallex has explicitly bet the company on this — Series H (2026-06-25) funds "autonomous finance and agentic commerce."

**Competitive landscape.** Sector KPIs for Airwallex's core: annualized revenue, annualized transaction/payment volume, multi-product attach; for the agent layer: agent-authorized TPV and workflow adoption (Airwallex discloses none for AgentOS — `[UNSOURCED]`). Basis of competition here is **distribution + trust/controls**, not price. Key players by layer: rails/tokens — Visa, Mastercard, Stripe (network-led, consumer-checkout skew); AI-native crypto rails — [[Coinbase launches Agentic Wallets via x402 protocol]], [[Skyfire raises... payments network]] (~$9.5m total funding), Payman (~$3m pre-seed, Visa/Coinbase Ventures backed) — tiny vs Airwallex; agent-execution suites — [[Fireblocks launches Agentic Payments Suite for AI agents]], [[Rain releases Agent Control Layer for AI agent spending]], [[Mastercard launches Agent Pay for Machines for machine-speed payments]], [[PhotonPay completes first live agentic payment with Mastercard]]. Recent moves: [[Pay3 launches agentic payments platform]], [[MoonPay unveils AI-driven fiat onramp for autonomous agents]]. Airwallex's position: **niche-but-defensible** on B2B treasury execution — it is not building a competing consumer-checkout token standard; it is exposing its existing production account (balances, beneficiaries, card issuance, FX, cashflow) to agents via CLI/MCP. Moat `(analysis)`: switching costs from being the system-of-record for cross-border money movement + a genuine multi-product money-movement licence stack (90%+ of revenue from multi-product customers, per IR) — harder to replicate than a wrapper.

**Comps & multiples.** No new valuation in this pick (product launch). External anchor (IR-grounded, below): Series H closed 2026-06-25 at **$11bn post-money** on **$1.3bn annualized revenue (Mar 2026)** → implied **P/Rev ≈ $11bn / $1.3bn = 8.5x** (round valuation, private, not market cap). vs Stripe — [[Stripe reaches $159 billion valuation in employee tender offer]] at ~$1.5tn 2025 TPV; on Airwallex's $287bn annualized volume, Airwallex's implied EV/volume ≈ $11bn/$287bn ≈ 0.038x is not directly comparable to Stripe's take-rate-driven model. Internal round comps: [[San Francisco Giants name Airwallex official jersey patch sponsor]] context aside, Airwallex's own ladder — $6.2bn (2025-05) → $8bn (2025-12) → $11bn (2026-06), ~78% up in 13 months, tracks ~74% YoY revenue growth, so **8.5x P/Rev is in-line-to-rich but growth-justified**, not an outlier flag on its own (comps-analysis: check multiple vs growth, which here holds). Clean EV/EBITDA `[UNSOURCED]` (private; cash-flow-positive claim from 2024 IR is stale). Pure agentic-payments comps (Skyfire/Payman) are pre-revenue seed names — distribution not computed, qualitative only.

**Risk flags.**
1. **Disintermediation by the rail layer.** Visa/Mastercard/Stripe own the agentic-token standard and the consumer relationship; if enterprise agents standardize on network tokens, Airwallex risks being a connector into someone else's rails rather than the rail — margin capture moves up-stack. Second-order: AgentOS may deepen lock-in for existing Airwallex customers but is unlikely to win the standard.
2. **Announced ≠ adopted / fiduciary risk.** AgentOS lets agents act on a *production* account (issue cards, execute transfers/FX). No disclosed limits framework, fraud-liability split, or agent-error controls; a single agentic mis-transfer at treasury scale is a reputational/regulatory event. Who's silent on liability = the PR.
3. **Valuation-vs-narrative risk.** The 38% mark-up to $11bn in six months rides the agentic-finance narrative; if agentic-treasury adoption lags the TAM hype (10x forecast spread), the multiple compresses faster than revenue.

**What this changes (idea-lens).** `(analysis)` AgentOS is a defensive distribution play, not a new profit pool: Airwallex is meeting agents where they already live (Claude/Cursor/OpenAI) to keep its account as the money-movement system-of-record rather than cede treasury execution to a rail-native agent stack. Falsifiable thesis: if within ~2–3 quarters Airwallex discloses agent-authorized TPV or workflow-adoption metrics, the bet is working; if the next disclosures stay generic ("launched," "available") with no usage numbers — as this PR is — treat it as marketing, not a re-rating. Trigger to watch: whether Visa/Mastercard's B2B agentic tokens extend into treasury/FX (Airwallex's turf) vs stay consumer-checkout.

Sources: https://www.airwallex.com/global/blog/introducing-airwallex-agentos-manage-your-financial-operations-in-your-preferred-agent-environment · https://www.airwallex.com/global/newsroom/airwallex-secures-320-million-in-series-h-funding-valuation-hits-11-billion · https://www.cnbc.com/2026/06/26/airwallex-series-h-funding-11-billion-valuation-ai-finance.html · https://stellagent.ai/insights/agentic-commerce-1-5-trillion-forecast-2030 · https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants · https://stripe.com/blog/supporting-additional-payment-methods-for-agentic-commerce · IR: https://drive.google.com/file/d/1U03h0wsb6Wm5wvIKzqMzd5-MpGaXjX-I/view (Series F, $720m ARR / $130bn volume, 2025-05)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news** — Airwallex is a private company and does not file GAAP results; the AgentOS launch (2026-07-02) is a product announcement with no financials. This section is context-only, with the latest DISCLOSED metrics from IR press releases and funding announcements.

**Verdict (context-only, private).** No formal earnings. Latest self-disclosed print: ARR ~$1.3bn annualized (Mar 2026, +74% YoY), $287bn annualized transaction volume (+120% YoY), valued at $11bn after the June 2026 Series H — a growth-stage, cash-flow-positive fintech scaling toward IPO-readiness.

**Key disclosed figures (self-reported, unaudited).**
- **ARR / revenue run-rate:** ~$1.3bn annualized as of Mar 2026, **+74% YoY** (company). Trajectory: ~$500m ARR (Aug 2024) → $1.0bn (Nov 2025, +90% YoY) → $1.1bn (end-2025) → $1.3bn (Mar/Apr 2026). Deceleration in the YoY growth rate (90% → 74%) as the base grows, but the absolute run-rate still ~2.6x'd in ~19 months.
- **Processing volume:** $287bn annualized transaction volume (Mar 2026), **+120% YoY**; ~$266bn cited as of Apr 2026. Trajectory: >$100bn annualized (Aug 2024) → $287bn (Mar 2026) — volume growing faster than revenue, implying take-rate compression as scale/volume mix shifts (analysis: run-rate revenue ÷ volume ≈ ~0.45% "monetization rate" on $1.3bn/$287bn, vs ~0.5% on $500m/$100bn — broadly stable, not a red flag).
- **Valuation:** **$11bn** post-Series H ($320m raised, 25 Jun 2026, led by Addition; Baillie Gifford, QED, T. Rowe Price, Hedosophia, Amex Ventures et al.), up from **$8bn** post-Series G ($330m, Dec 2025, ~30% step-up from Series F) and **$6.2bn** at Series F ($300m, May 2025). Valuation ~+78% in ~13 months.
- **Customers:** 200,000+ businesses; **>90% of revenue** from customers using more than one Airwallex product (cross-sell / land-and-expand — supports NRR durability).
- **Profitability:** management disclosed the group reached **cash-flow positive** operations (first stated Aug 2024); no GAAP net-income / margin figures disclosed (private). "IPO-ready by 2026" ambition cited by management (Aug 2024).
- **Regional (self-reported):** APAC revenue +83% YoY (Dec 2024); Southeast Asia revenue +108% YoY; Singapore triple-digit revenue growth two consecutive years (Mar 2026).

**Thesis-flags (context for the AgentOS news).**
1. **Agentic finance is now the funding narrative, not a side product.** Airwallex explicitly earmarked the Series H for "autonomous finance and agentic commerce" and "AI-native financial software" — AgentOS (agents on Claude, Cursor, OpenAI executing end-to-end financial workflows) is the productization of that thesis, launched days after the raise. Second-order: positions Airwallex as infrastructure for the agentic-payments wave rather than a commoditized cross-border FX player.
2. **Growth is real but decelerating off a bigger base** (ARR YoY 90% → 74%); volume still +120% YoY. Watch whether monetization (take-rate) holds as volume outpaces revenue.
3. **Cross-sell depth (>90% multi-product revenue)** is the durable moat signal — AgentOS + the June 2026 Leapfin acquisition (revenue recognition/reconciliation) extend the platform up the finance stack, reinforcing multi-product stickiness.
4. **Private, unaudited, self-selected metrics** — all figures are company-disclosed marketing/IR numbers, not GAAP; no net income, no gross margin, no churn/NRR disclosed. Treat growth rates as directional.

Sources: semsearch irdb (drive_url) — Series G $8bn ([drive](https://drive.google.com/file/d/1wQRKaV_W590thr8cQspWgt-mhh6f9pOL/view)), $100bn volume / ~$500m ARR / cash-flow-positive ([drive](https://drive.google.com/file/d/1plcP6FtjzipMlF7FUok6J4UHJN8IpdQD/view)), APAC +83% quarterly ([drive](https://drive.google.com/file/d/1CC0FyT0UsLkOc5iJEd2rNCEaUgwdlPU-/view)), SEA +108% ([drive](https://drive.google.com/file/d/1ZMR3FdGyhUzDCck28pXnakOUIUeTGwQI/view)) · web: Airwallex Series H $320m/$11bn, $1.3bn ARR +74% / $287bn volume +120% (businesswire.com 2026-06-25; fintechfutures.com) · Sacra (sacra.com/c/airwallex) $1.3bn ARR Apr 2026, $266bn volume, 200k+ businesses · CNBC 2024-08-15 (~$500m ARR, IPO-ready 2026). Not disclosed (private): GAAP net income, gross/operating margin, NRR, churn — "no data".
<!-- /enrichment:earnings_review -->
