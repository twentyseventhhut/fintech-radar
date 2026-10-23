---
title: "Finom launches Finom MCP for Claude and ChatGPT"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/finom
  - industry/agentic-commerce
  - region/europe
  - type/product
sources:
  - https://finom.co/en-de/news/finom-mcp-ask-questions-inside-claude-chatgpt
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s638be210
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Finom launches Finom MCP for Claude and ChatGPT

> [!info] 2026-10-23 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌐 Finom launches Finom MCP, letting users ask questions inside Claude and ChatGPT. The MCP integration brings Finom into both AI assistants. Users can ask questions in either assistant without switching apps. Read more

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://finom.co/en-de/news/finom-mcp-ask-questions-inside-claude-chatgpt>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Finom launches Finom MCP for Claude and ChatGPT
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Finom (Dutch/European SME finance platform) released **Finom MCP**, a Model Context Protocol connector that lets a customer query their own Finom business account from inside Claude or ChatGPT in natural language (e.g. "list transactions over €500 last month", "analyse my 2026 spend", a morning briefing). Announced ~2026-10-22; covered by Finextra 2026-10-23.

De-PR'd reality — two things the press bullet hides:
- **It is READ-ONLY.** Finextra's own headline says so: "Finom launches read-only MCP connection." It can consult balances/transactions/wallets/invoices/cards/accounting and answer questions, but it **does not move money, issue cards, change the account, or give financial/tax/legal advice.** So it is a conversational query layer over account data, not an agentic-banking capability. The "ask inside Claude/ChatGPT without switching apps" framing is accurate but the agentic/"your AI can act" implication is absent.
- **The customer still controls scope** — connected with the user's own Finom login, access scoped to the existing role, disconnectable anytime. That is a sensible security posture but also underscores there is no delegated-agent execution here.

**Why structured this way / what it reveals:** shipping read-only first is the low-risk path (no payment-authorization, fraud-liability, or write-side audit problems), and it is bundled into every Finom plan across Europe at no extra charge — i.e. a retention/feature-parity play, not a new revenue line. Read-only also means Finom avoids the hard part (write auth + confirmation + audit) that the lead competitor already solved. See prior art below.

## [1] Competitors / peers
Direct European SME-banking peer: **Qonto** — launched its official MCP server in **June 2026** across 8 markets to 600k+ customers, and crucially it is **read + WRITE** (banking data, card management, invoicing, payment-requests), each write gated by explicit confirmation + audit log. **Revolut Business** also exposes an MCP server (read balances/transactions, counterparties, FX, initiate transfers); Revolut shipped consumer "AIR" assistant to 13M UK users in April 2026.
Infra/adjacent prior art: [[Bud Financial launches MCP server for AI banking]] (Oct 2025, bank-data intelligence), [[Coinbase launches Payments MCP for AI agents]], [[BitGo launches MCP Server to bring crypto infrastructure to AI agents]], [[Prometeo launches Agentic Banking solution]], plus Finix, Financial Cents, Qount MCP connectors.

**Position: catching up, and with a weaker SKU.** Finom is ~4 months behind Qonto and ships only the read half of what Qonto shipped. **Why the lay of the land is this way (analysis):** the MCP-for-SME-banking wave is now table stakes among European neobanks — being absent would be a feature gap in RFPs/reviews — so Finom's launch reads as parity-defense rather than differentiation. Second-order: because Qonto already owns the write/execution surface (the valuable, sticky part), Finom's read-only entrant risks being a commodity "ask your statements" chatbot while the margin-bearing "let the AI do the banking" layer sits with the first mover.

## [2] Company history / fit
Finom trajectory: €50M Series B (Feb 2024) → €115M Series C (June 2025, led by AVP; General Catalyst, Northzone, Headline, Cogito) + ~€92.7M growth from General Catalyst's Customer Value Fund → **>€300M total raised**, valuation ~2× the 2024 Series B, 125k+ customers (local IBANs in DE/FR/IT/ES/NL), 500+ staff, target 1M business customers by end-2026. Explicitly flagged "AI-powered financial intelligence" as a Series C investment area.
Product line into AI: [[Finom launches Interest Account for European businesses]] (Mar 2026), [[Finom launches standalone AI accounting software in Germany]] (May 2026, unbundled AI bookkeeping/tax, €14/mo). MCP fits that AI-accounting push logically.

**Why Finom acts this way (analysis):** as a sub-scale challenger chasing a 1M-customer goal, Finom needs to look AI-forward to defend its "smart business finance" positioning against Qonto/Revolut; a free, every-plan MCP connector is cheap PR + retention signalling that it is keeping pace. It extends the same "AI assistant answers plain-language finance questions" pattern already in its accounting product — low marginal cost, on-brand.

## [3] Novelty / value-add / traction
**Not novel as a category** — it is the Nth MCP-for-banking launch (Bud Oct 2025; Qonto/Revolut mid-2026). Novelty for Finom specifically: first time a Finom customer can read account data from a third-party AI assistant. **Traction: zero disclosed** — announcement only, no usage/adoption numbers, launched 2026-10-22. "Included in every plan" is availability, not adoption.
**Why the value-add is thin (analysis):** read-only means the AI can summarize but not transact, so the economic value to the user is modest (saves a dashboard trip) and there is no new monetization. **Who captures the margin:** none shifts — Finom gives this away free; the assistant vendors (Anthropic/OpenAI) capture the engagement. The durable value in agentic banking is the write/execution + confirmation layer (Qonto), which Finom has not built. What breaks the thesis: if write-capable agents become the norm, a read-only connector is a transitional half-step that gets superseded by Finom's own future write version (likely roadmap) — so today's launch is more a marker than a moat.

## [4] What's next / market sentiment
Expect Finom to follow with write/action capabilities (payments, invoicing via MCP) to match Qonto; the read-only "in every plan" rollout de-risks that path. Broader market: MCP has become the default standard for "connect your business account to an AI assistant," with 10+ banks/fintechs live or in beta per open-banking trackers. Regulatory/risk backdrop: PSD2/strong-customer-authentication, data-consent scoping, and the unresolved question of liability when an AI agent acts on finances — which is precisely why most players (Finom included) start read-only.
**Why the market goes this way (analysis):** standardization on MCP commoditizes the connector itself, so differentiation migrates to (a) write/execution safety and (b) proprietary financial intelligence on top. **Counterintuitive second-order:** the "AI can see your account anywhere" convenience erodes the neobank's own app as the primary surface — Finom risks training its users to live inside Claude/ChatGPT rather than Finom, ceding the customer relationship/engagement to the assistant layer while still bearing the cost and compliance.

## Top challenge/extra questions
(see challenge column)

## Sources
- Finom press release: https://finom.co/en-de/news/finom-mcp-ask-questions-inside-claude-chatgpt
- Finextra (read-only framing): https://www.finextra.com/pressarticle/111410/finom-launches-read-only-mcp-connection-for-claude-and-chatgpt
- Qonto MCP (June 2026, read+write): https://docs.qonto.com/mcp/overview ; https://qonto.com/en/ai
- Revolut Business MCP / AIR: https://www.tapix.io/resources/post/ai-assistants-in-banking-compared
- Finom Series C €115M: https://fintech.global/2025/06/23/finom-secures-e115m-to-expand-financial-tools-for-smes/ ; https://avpcap.com/finom-raises-e115-million-series-c-to-fuel-european-expansion/
- Agentic banking / banks-with-MCP tracker: https://www.openbankingtracker.com/banks-with-mcp-servers
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
1. **Read-only or write-capable?** Read-only (confirmed by Finextra headline + press release: consults data, does not move money / issue cards / change account). Not agentic.
2. **Is it novel?** No. MCP-for-banking is the Nth such launch: Bud (Oct 2025), Qonto & Revolut (mid-2026), BitGo, Coinbase Payments MCP, Finix, Financial Cents. Finom's novelty is only "first time for Finom customers."
3. **Who did it first / better among direct peers?** Qonto — June 2026, 600k+ customers, 8 markets, and read+WRITE (invoicing, cards, payment-requests) with per-write confirmation + audit. Finom is ~4 months later and read-only. Open.
4. **Any adoption/traction numbers?** None disclosed. Announcement only (2026-10-22). "Included in every plan" = availability, not usage.
5. **Does it make money?** No new revenue — bundled free into every plan. Retention/parity play, not monetization.
6. **What's the real user value beyond a dashboard trip?** Modest: summarize/query account data inside an assistant the user already uses. No ability to act, so low on the value ladder. Open whether this materially changes behaviour.
7. **Who captures the margin?** Not Finom (gives it away). Engagement/margin accrues to Anthropic/OpenAI (the assistant surface). The durable, margin-bearing layer (write/execution) sits with Qonto, not Finom.
8. **Does it cannibalize Finom's own app/relationship?** Risk (analysis): trains users to live in Claude/ChatGPT rather than Finom, ceding the engagement surface while Finom keeps cost + compliance. Second-order downside.
9. **Security/liability posture?** Read-only + user's own login + role-scoped + disconnectable. Sensible, but also the reason value is capped — no delegated execution, so no write fraud-liability to solve (yet).
10. **Is it fresh or a dupe?** FRESH. Distinct product (MCP connector) and distinct company vs the same-period MCP priors (Bud is bank-data infra; Qonto/Revolut are separate companies; Finom's own prior notes are Interest Account and standalone AI accounting — different products). Not a re-run.
11. **Does it fit Finom's strategy?** Yes — extends the Series-C "AI financial intelligence" thesis and the May-2026 standalone AI-accounting product; cheap, on-brand AI signalling for a 1M-by-2026 challenger.
12. **What's the likely next step?** Write/action MCP (payments, invoicing) to reach Qonto parity; today's read-only rollout de-risks that path. Open (no roadmap confirmed).
13. **Why read-only first?** Avoids payment-authorization, SCA, write-audit, and AI-acts-on-money liability — the hard, unsolved parts. Low-risk MVP.
14. **Does Finom's scale justify weight?** Sub-scale vs Qonto (125k vs 600k+ customers); €300M+ raised but a feature-parity launch from a smaller challenger carries limited market significance.
15. **What would raise importance?** Real adoption data, write/agentic capability, or a monetized SKU. None present today.

Importance: 2/5 — a free, read-only MCP connector from a sub-scale European SME challenger, launched ~4 months after Qonto shipped a superior read+write version. Correct strategic hygiene (feature parity in a now-table-stakes category) but no novelty, no disclosed traction, no new revenue, and the weaker half of the product. Fresh event, modest weight.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** European SME/SMB business-banking (neobanks: Qonto, Revolut Business, Tide, Finom, Shine) sits inside the fast-moving "agentic finance" wave — exposing banking data to LLM assistants via protocols (MCP, ACP, UCP). Qonto pegs its European SME TAM at ~€52bn across 17.4m SMEs in its 8 markets (per Qonto/Contrary research, as of Dec 2024) — large and still underpenetrated. Structure: fragmented (many country-level incumbents + a handful of pan-EU challengers), high regulatory/capital barriers (e-money/banking licences, PSD2), and moats built on local IBANs, accounting integrations and distribution rather than rate. Why now: three protocol stacks matured in 2025–26 — MCP (Anthropic, data/connectivity), ACP (OpenAI+Stripe, checkout, live since Sep 2025), UCP (Google+Shopify). By 2026 most major PSPs (Stripe, PayPal, Adyen) and data providers shipped MCP servers (per Fin.ai / PaymentBrief, 2026), so a neobank exposing its account data to Claude/ChatGPT is now a table-stakes move, not a first.

**Competitive landscape.** SME-neobank KPIs: active business customers, TPV, ARR/ARPA, EBITDA margin. Players & basis of competition: Qonto (~600k business customers, ~€350m ARR, ~€8.2bn TPV, €4.4bn Series-D valuation from Jan 2022 — per Contrary/stockanalysis, dated/stale) and Revolut Business compete on product breadth + scale; Tide (2m+ members, India push) on SMB distribution; Finom on local-IBAN coverage (DE/FR/IT/ES/NL) + accounting. Recent agentic moves — [[Bud Financial launches MCP server for AI banking]] (MCP for bank data, Oct 2025); [[Prometeo launches Agentic Banking solution]] (LLMs executing payments, Oct 2025); [[Anthropic expands Claude for Financial Services with Excel add-in]]; broad PSP MCP/ACP rollout (Stripe, PayPal, 2025–26). Finom's position: fast-follower / in-line, not pioneer — Bud shipped a banking MCP server a year earlier. Its MCP is explicitly read-only (no money movement, no card issuance, no advice; included in every plan, user-scoped). Moat (analysis): switching costs from embedded accounting/IBAN, not from the MCP feature, which is easily replicable.

**Comps & multiples.** Finom: ~$50.9m ARR (2025, per getlatka); raised €115m Series C (Jun 2025, led by AVP; +General Catalyst CVF ~€92m); 300k+ businesses (Finom PR) / 125k+ with local IBANs (secondary). EBITDA-/EBITDAM-profitable in all key markets (Finom, 2024). Valuation: no verifiable post-money (getlatka's "$152.8m valuation" looks stale/implausible vs a €115m round — treat as [UNSOURCED]); revenue/ARR multiple = no data (no reliable valuation numerator). Internal comps: [[Bud Financial launches MCP server for AI banking]], [[Prometeo launches Agentic Banking solution]] — qualitative agentic-banking peers, no disclosed multiples. External comp Qonto: €4.4bn / ~€350m ARR = ~12.6x EV/Rev (analysis; Jan-2022 round vs later ARR, cross-period mismatch so treat as indicative only, not clean). Distribution not computed (only one usable multiple, cross-dated) — qualitative comparison: Finom is the smaller, capital-efficient, profitable challenger vs Qonto's scale-and-spend model.

**Risk flags.** (1) Disintermediation / commoditisation — the MCP layer is read-only and trivially replicable (Bud, PSPs already shipped servers); the feature adds little durable moat and risks the assistant (Claude/ChatGPT) owning the customer interface while Finom becomes a data backend. (2) Execution vs the 1m-customers-by-end-2026 target (Finom) — from a ~125k-local-IBAN base that is a steep ramp; agentic features don't move that needle. (3) Data-security/consent + regulatory surface — piping business banking data into third-party LLMs invites GDPR/data-residency and prompt-exfiltration scrutiny; read-only now, but any later write-access (payments) would pull in PSD2/fraud-liability exposure.

**What this changes (idea-lens).** For the sector: exposing account data to assistants is becoming table stakes for EU business banking, shifting differentiation toward whoever owns write-access (initiating payments/invoices) rather than read-only Q&A (analysis). Watch: whether Finom (or Qonto/Revolut Business) ships an ACP-style transactional/payment-initiation agent next — that would be the real re-rating trigger; a thesis that "MCP read-only is a moat" is falsified by how quickly peers match it.

Sources: https://finom.co/en-de/news/finom-mcp-ask-questions-inside-claude-chatgpt · https://www.finextra.com/pressarticle/111410/finom-launches-read-only-mcp-connection-for-claude-and-chatgpt · https://getlatka.com/companies/finom.co · https://sifted.eu/articles/dutch-fintech-finom-raises-e115m-and-eyes-ma · https://research.contrary.com/company/qonto · https://fin.ai/learn/what-is-agentic-commerce · https://paymentbrief.com/articles/ai-agents-payment-apis-mcp-stripe-toolkit/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
