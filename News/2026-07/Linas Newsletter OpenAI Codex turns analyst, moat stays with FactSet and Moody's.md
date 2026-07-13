---
title: "Linas Newsletter: OpenAI Codex turns analyst, moat stays with FactSet and Moody's"
date: 2026-07-12
retrieved: 2026-07-12
tags:
  - company/openai
  - company/factset
  - industry/capital-markets
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://substack.com/redirect/82332022-2131-42d0-9278-4535bba1f879
  - https://substack.com/redirect/7e9f6f68-305c-4181-9f75-62e8f5d15f45
  - https://substack.com/redirect/d4277a83-c918-41f0-89b9-0c4e2654e4da
status: enriched
n_mentions: 1
channels:
  - "Linas Newsletter"
story_id: s5c26fa7f
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Linas Newsletter: OpenAI Codex turns analyst, moat stays with FactSet and Moody's

> [!info] 2026-07-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Linas Newsletter

## Агрегированный текст (из дайджестов)

[Linas Newsletter] ICYMI: OpenAI’s Codex just became a Wall Street analyst, and the moat belongs to FactSet & Moody’s 🤖📊 [what OpenAI exactly shipped and why it matters, how this hands the durable moat to companies most people aren’t even watching, and the 4 shifts we’d bet on over the next 2 years + bonus deep dives into OpenAI’s Super App strategy & how Anthropic just told AI founders exactly what to build in 2026 inside]

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/82332022-2131-42d0-9278-4535bba1f879>
- <https://substack.com/redirect/7e9f6f68-305c-4181-9f75-62e8f5d15f45>
- <https://substack.com/redirect/d4277a83-c918-41f0-89b9-0c4e2654e4da>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Linas Newsletter — "OpenAI Codex turns analyst, moat stays with FactSet & Moody's"
_Analytical notes (not a post). Importance: 3/5._

**One-line verdict:** Opinion/commentary piece (Linas Beliūnas, Substack, ~2026-07-12) built on a REAL event — OpenAI's 2026-06-02 Codex finance plugins — whose *mechanical* claim is grounded (the AI analysis layer literally runs ON TOP of FactSet/Moody's/S&P licensed data) but whose *conclusion* ("moat intact for both") is exactly the thesis the market is currently rejecting for FactSet (FDS ~-50% off its 2025 high on AI-disintermediation fear). The moat is real but UNEVENLY distributed: durable for Moody's ratings franchise, actively eroding for FactSet's terminal/aggregated-data model. Separate the author's thesis from established fact throughout.

## [0] What exactly happened (de-PR'd)
- **The commentary itself:** Linas Newsletter issue titled "OpenAI's Codex just became a Wall Street analyst, and the moat belongs to FactSet & Moody's" ([linas.substack.com/p/fintechpulse1085]). Free preview confirms the thesis; the "4 shifts over the next 2 years" and "OpenAI Super App strategy" deep-dives are PAYWALLED and NOT retrievable — treat as informed commentary, not primary research.
- **The underlying event (FACT, dated):** On 2026-06-02 OpenAI shipped six role-specific plugins for **Codex**, two of them financial — a **public-equity investing** plugin and an **investment-banking** plugin. Codex is OpenAI's *agent* product (originally a coding agent; desktop app since Feb 2026), NOT a new finance-trained model; the "analyst" comes from wrapping the agent with plugins = integrations + instructions + context. Already covered as a factual product note in the corpus: [[OpenAI unveils Codex plugins for investment, banking and sales]].
- **The crux that supports the thesis (FACT):** OpenAI's own copy says the equity plugin works "using information from Moody's, Daloopa, Datasite, FactSet, LSEG, S&P, PitchBook, and Hebbia." So OpenAI did NOT build a data moat; it built an analysis layer that *consumes the incumbents' licensed data* and names them explicitly. That is genuine support for "the moat belongs to the data vendors."
- **Live vs demo (skeptical flag):** "Rolling out to Codex users in supported regions" — live but STAGED. No disclosed data-access pricing, **no named institutional finance customer**, no finance-specific benchmarks. OpenAI's >5M Codex WAU figure is aggregate Codex, NOT finance-plugin adoption — do not read it as "banks adopted the analyst."
- **Why framed this way:** A paywalled Substack leads with a punchy "just became a Wall Street analyst" hook to sell the deep-dive. The "just became" is a marketing beat, not a technical first (see [2]).

## [1] Competitors / peers
- **FactSet (FDS) — the thesis's weak leg (FACT):** FY2025 rev $2.32B, adj op margin 36.3%, 45-yr revenue-growth streak; FY2026 guide ASV +4-6%, margin *compression* to 34.0-35.5%. Stock ~$247 (2026-07-10), **~-49% below its June-2025 high (~$450)**, YTD down double digits. A wall of sell-side (UBS, BMO, Stifel, Morgan Stanley, Goldman, RBC, Deutsche, Barclays, Wells Fargo) cut targets; Rothschild Redburn downgraded on "terminal risks." Key structural exposure: terminals ~51% of revenue, ~25% is aggregated NON-proprietary data — the exact slice AI commoditizes. AI response: FactSet Mercury (LLM knowledge agent, beta Dec 2023, GA early 2025), Conversational API, and it was "first to announce an MCP server sans intermediary" (Explorer beta: 45 firms / 800+ users). So FactSet is leaning INTO disaggregation, but the market is pricing moat *erosion*, not intactness.
- **Moody's (MCO) — the thesis's strong leg (FACT):** FY2025 rev $7.7B (+9%), adj op margin 51.1%; MIS ratings $4.1B, Moody's Analytics $3.6B (~97% recurring). Trades near highs. **Regulatory/franchise moat: no LLM can mint a Moody's rating** (NRSRO status, issuer-pays). Via MCP, customers query Moody's data inside Claude/OpenAI but never receive a copy — data stays in governed infra, outputs generated on demand; 170+ exclusive/semi-exclusive data relationships. This is where "moat intact" cleanly holds.
- **Anthropic (the buried lede):** Claude for Financial Services launched **Jul 2025**, expanded to a 10-agent suite **May 2026** with FactSet, S&P/Kensho, Moody's, LSEG, Morningstar, PitchBook, Daloopa, MSCI. Bloomberg framed OpenAI's June move as "a direct race with Anthropic." Corpus: [[Anthropic launches financial services plugins for Claude Cowork]]. So OpenAI is *catching up* to a pattern Anthropic set — "just became" overstated.
- **+ Why the landscape is this way (analysis):** The market is already pricing the split the headline conflates — punishing the *terminal/aggregated-data* model (FDS) while rewarding the *regulated-franchise* model (MCO). Differentiation is collapsing FROM the analysis layer (commoditized across OpenAI/Anthropic/AlphaSense/Rogo/Hebbia) TO data access + workflow lock-in + regulatory franchise.

## [2] Company / theme history & fit
- **AI-as-analyst is NOT new (FACT):** BloombergGPT (2023, 50B params on Bloomberg's corpus) *lagged* GPT-4 on financial reasoning — proprietary *model* wasn't the moat, data+Terminal was. AlphaSense (AI over 10k+ premium sources, live for years); Hebbia ($130M 2024, integrated into LSEG Workspace Sep 2025, and a named source inside OpenAI's own equity plugin); Rogo (IB-workflow AI); Perplexity Finance (early-2026 Bloomberg-like product at ~$200/mo vs ~$32k/yr terminal). Corpus analog: [[BridgeWise acquires Context Analytics for AI investment platform]].
- **OpenAI's actual contribution (analysis):** distribution + generality (an agent millions already use + a plugin marketplace + explicit finance data partnerships in one place), NOT a capability first. Fits OpenAI's broader white-collar/"super-app" agent push; Codex is already used inside finance orgs for dev work ([[Payward accelerates development with OpenAI Codex]]).

## [3] Novelty / value-add / traction
- **Novelty: modest.** Novel = OpenAI's scale + marketplace + named finance data partners in one agent. Not novel = analyst-on-licensed-data (Anthropic May 2026; AlphaSense/Hebbia/Rogo earlier).
- **Traction: live product, UNPROVEN finance adoption.** Staged rollout confirmed; no public buy/sell-side deployment of the finance plugins as of ~2026-07-13. Aggregate Codex WAU ≠ finance traction (do not conflate).
- **Does the thesis hold? Half-confirmed.** Confirmed: the analysis layer is being commoditized/multi-sourced and rides on incumbent data (OpenAI's plugin proves it). Contested: "moat [and value] stays with FactSet" — the tape says FactSet's moat is eroding because a big chunk of revenue is aggregated non-proprietary data + seat-priced terminals, precisely what an AI front-end disintermediates.
- **+ Who captures the margin (the second-order shift):** The real battle is the **pricing model, not the capability**. Incumbents survive IF they convert "per-seat terminal" → "metered data/API/MCP consumption." If AI apps let clients extract the same data with FEWER seats, revenue falls even as the data stays essential. Moody's MCP is *designed* to prevent copying (query-not-copy); FactSet's aggregated layer is more leakable. So moat durability is **dataset-specific, not vendor-wide** — the central question shifts from "is there a data moat" to "can incumbents re-price data as consumption faster than AI compresses seats."

## [4] What's next / market sentiment
- OpenAI flagged more plugins (Corporate Finance, Private Equity, Strategy Consulting, Legal) — white-collar expansion continues.
- Watch **FactSet FY2026 ASV & seat counts** for the first hard read on whether AI compresses seats vs expands data licensing; watch whether Moody's/S&P/FactSet can monetize MCP/API access enough to replace terminal economics.
- Sentiment: divergent — FDS de-rated on AI disintermediation fear; MCO near highs. The counterintuitive second-order effect: the incumbent most exposed (FactSet) is the one whose brand the newsletter uses as the *symbol of safety*.

## Sources
- Linas Newsletter (paywalled): https://linas.substack.com/p/fintechpulse1085
- OpenAI Codex-for-every-role: https://openai.com/index/codex-for-every-role-tool-workflow/ ; TechCrunch 2026-06-02: https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/ ; Bloomberg 2026-06-02: https://www.bloomberg.com/news/articles/2026-06-02/openai-plans-ai-tools-for-finance-legal-in-race-with-anthropic ; Finextra: https://www.finextra.com/newsarticle/47846/openai-launches-codex-plugins-for-finance-pros
- FactSet FY25: https://investor.factset.com/news-releases/news-release-details/factset-reports-results-fourth-quarter-and-fiscal-2025 ; FDS AI/moat: https://www.ainvest.com/news/factset-faces-ai-driven-moat-erosion-49-drop-rating-play-2604/ ; MCP: https://investor.factset.com/news-releases/news-release-details/factset-meets-demand-ai-ready-data-first-announce-mcp-sans
- Moody's FY25: https://www.tipranks.com/news/company-announcements/moodys-reports-record-2025-results-and-growth-outlook ; data moat/AI: https://www.constellationr.com/insights/news/how-moodys-thinking-about-data-moats-ai-strategy-token-costs
- Anthropic finance agents: https://www.anthropic.com/news/finance-agents ; https://www.anthropic.com/news/claude-for-financial-services
- Perplexity Finance: https://finance.yahoo.com/news/perplexity-ai-just-turned-30-153122212.html
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / second-order questions

1. **Is Codex a model or an agent doing analysis?** Answered: an **agent + finance plugins** on GPT-5.x-Codex, not a finance-trained model. The newsletter's "coding tool now does banking" framing is technically accurate — agentic tool-use generalized beyond code.
2. **Did OpenAI ship an "analyst" or a demo?** Answered: LIVE but staged rollout (2026-06-02). No finance-specific benchmarks, no named institutional users disclosed.
3. **Does the plugin actually prove the "data moat" thesis?** Answered — partially yes: OpenAI's own copy names FactSet/Moody's/S&P/LSEG as data sources; the analysis layer is clearly NOT OpenAI's moat.
4. **If data is the moat, why is FDS down ~50%?** Answered: market prices AI disintermediation of terminals + the ~25% aggregated non-proprietary data slice. "Moat intact" is contradicted by the tape for FactSet specifically.
5. **Does the thesis apply equally to FactSet and Moody's?** Answered — NO. Moody's has a regulatory ratings franchise (no LLM can mint a rating); FactSet's terminal/aggregated-data mix is far more exposed. The headline over-couples two very different moats — the single biggest flaw in the piece.
6. **Is this genuinely new, or is Anthropic ahead?** Answered: Anthropic led (Claude for Financial Services Jul 2025; 10-agent suite May 2026). OpenAI is catching up; Bloomberg called it a "race." "Just became" is overstated.
7. **Any evidence buy-side/sell-side actually adopted Codex finance plugins?** Open/negative: none found as of ~2026-07-13. Aggregate Codex WAU (>5M) ≠ finance adoption.
8. **What are the "4 shifts" and "Super App strategy"?** Open: paywalled, not retrievable. "Super App" = OpenAI bundling agents/apps/commerce (inference, unconfirmed for this post).
9. **Does AI compress seat-based/terminal pricing?** Answered — bear case is live: Perplexity Finance ~$200/mo vs ~$32k/yr terminal; analysts cite fee compression + headcount cuts hitting FactSet seats.
10. **Can incumbents recapture value via metered data/MCP consumption?** Open: FactSet (first MCP-sans-intermediary; 45 firms/800 users beta) and Moody's (query-not-copy MCP) are trying; economics not yet proven to offset seat loss. This is the decisive open question.
11. **Can a client extract the underlying data with fewer seats?** Partly answered: Moody's MCP is designed to prevent copying (query-only); FactSet's aggregated non-proprietary layer is more leakable. Moat durability is dataset-specific, not vendor-wide.
12. **Is the "analysis layer commoditized" claim true?** Answered — trending yes: OpenAI, Anthropic, AlphaSense, Rogo, Hebbia, Perplexity all offer overlapping analyst-style output; differentiation collapses to data access + workflow lock-in + regulatory franchise.
13. **Does the BloombergGPT precedent support the thesis?** Answered — yes: a proprietary *model* didn't win (BloombergGPT lagged GPT-4); data + distribution did. Reinforces "moat = data," but also warns terminal distribution itself can be disrupted by AI front-ends.
14. **Regulatory / liability angle?** Open/analysis: AI-generated analyst output raises accuracy/liability/compliance questions; regulated ratings stay human-governed — a structural reason Moody's franchise is safer than generic analysis.
15. **Is the newsletter promotional / paywall-gated?** Answered — yes: thesis-forward hook, key reasoning behind paywall. Treat as informed commentary, NOT primary research.

### Freshness / duplicate verdict
**FRESH.** The corpus contains [[OpenAI unveils Codex plugins for investment, banking and sales]] (2026-06-05), which covers the SAME underlying 2026-06-02 product event — but as a bare factual product note. This Linas item is a distinct *analyst commentary / thesis* about the competitive-moat implications (Codex commoditizes the analysis layer; durable value accrues to FactSet/Moody's data). Different content type, different central claim, ~5 weeks later. The pool's dup_candidates were unrelated OpenAI corporate items (payments, ChatGPT finance, IPO delay), NOT this thesis. No prior note covers THIS commentary. Not a reprint.

### Importance: 3/5
Real, well-sourced event underneath (Codex finance plugins are live) and a genuinely useful analytical frame ("who owns the data moat when the analysis layer commoditizes"). Docked below 4 because: (a) it is paywalled opinion/commentary, not a new hard event; the news beat itself is already captured in the June note; (b) the headline's central conclusion is half-wrong — it lumps FactSet (moat visibly eroding, -50%) with Moody's (moat intact), the exact distinction that decides the weight; (c) no finance-plugin adoption evidence and Anthropic already set the pattern, so novelty is modest. Above 2 because the underlying shift (AI consuming incumbent data → pricing-model battle over seats vs metered consumption) is a real, tradeable second-order dynamic worth surfacing.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Financial-data & analytics + credit ratings — the "picks-and-shovels" layer of capital markets. Structure: a consolidated oligopoly, not fragmented. Two distinct sub-verticals with different economics: (a) ratings (Moody's MCO, S&P Global SPGI ratings) — a regulated near-duopoly with NRSRO barriers, issuer-pays model, ~55–60% operating margins; (b) desktop data/analytics (Bloomberg Terminal ~$30k/seat/yr per [techbuzz], FactSet FDS, S&P Market Intelligence, LSEG, MSCI) — sold on proprietary datasets, integration into workflows and high switching costs. "Why now": OpenAI turned Codex into an equity-analyst / banker tool (public-equity-investing plugin: review earnings, compare companies, assess theses), explicitly wiring in Moody's, FactSet, S&P, LSEG, PitchBook, Daloopa, Hebbia as the data layer (per Finextra/OpenAI, Jul 2026). Codex now >5M weekly users; non-developers (analysts, bankers, investors) ~20% of users and growing >3x faster than developers (per OpenAI/TradingView, Jul 2026). Second-order: the AI vendor competes for the *interface/workflow* but rents the *data* from the incumbents — the moat migrates down the stack to whoever owns proprietary, licensed, real-time data.

**Competitive landscape.** Sector KPIs: recurring/subscription revenue (ASV — annual subscription value), retention/renewal rate, organic ASV growth, ratings issuance volume (cyclical with debt issuance), operating margin. Basis of competition: proprietary data + regulatory licence (ratings) + workflow lock-in, NOT UI. Key players: incumbents FactSet, Bloomberg, S&P Global, Moody's, LSEG, MSCI; AI-native challengers AlphaSense, Hebbia, Perplexity Finance ($200/mo vs Bloomberg's $30k/yr, per techbuzz), BloombergGPT (incumbent's own LLM). Recent moves: Perplexity launched a $200/mo finance research tool aimed at Bloomberg (Mar 2026, per linkstartai); Bloomberg Terminal adding native AI layer (per techbuzz, 2026); Moody's publicly framing "data moats + AI strategy + token costs" (Constellation Research). Protagonist (OpenAI): a new *entrant* at the analyst-workflow layer, ahead on distribution (weekly users) but with NO proprietary financial-data moat — it licenses from the very incumbents the newsletter says keep the moat. Incumbents' position: FactSet/Moody's defensible via intangibles (proprietary/licensed data) + switching costs; but the disruption vector is at the *low end* (independent traders, small funds priced out of Bloomberg) per multiple sources — classic disruption-from-below.

**Comps & multiples.** Peer trading multiples (public equities, mid-2026):
- **Moody's (MCO):** fwd P/E **27.3x** (trailing 32.1x) — richest; ratings duopoly + Moody's Analytics recurring rev (per financecharts/gurufocus, Jun 2026).
- **S&P Global (SPGI):** fwd P/E **20.6x** (per valueinvesting.io, Jul 3 2026).
- **MSCI:** fwd P/E **30.4x** — highest, index/ESG toll-road model (per gurufocus, Jul 6 2026).
- **FactSet (FDS):** fwd P/E **13.2x** — the clear outlier LOW (per gurufocus, Jun 6 2026), ~half the peer set. FDS trades cheapest of the four, consistent with it being seen as *most* exposed to AI/desktop disruption (competes head-on at the analyst-desktop layer that Codex/Perplexity attack), while ratings (MCO) and index (MSCI) toll-roads command a premium.
- Median fwd P/E of the four ≈ (20.6+27.3+30.4+13.2)/4 ≈ **22.9x**; range 13.2x–30.4x — a >2x spread within one "sector," so treat as three different business models, not one comp set.
- OpenAI (private, not comparable to these on P/E — loss-making, no ratings/data licence): last funding = **$40bn round closed Mar 2025** (largest private tech raise on record, SoftBank-led; per CNBC via IR). This is a *round valuation input*, not market cap; no public earnings exist — no revenue multiple computed [UNSOURCED].
- Internal comps (base): [[BridgeWise acquires Context Analytics for AI investment platform]], [[EquiLend acquires Finadium to expand securities-finance research]], [[S&P Global completes sale of EDM and thinkFolio to STG]], [[Broadridge invests in DeepSee for agentic post-trade AI]], [[Finrob closes $3.9M seed for AI financial markets research]], [[Luxembourg Stock Exchange acquires Tetrao ESG data analytics unit]] — incumbents actively *buying/building* AI-analytics and *shedding* commoditizing assets (S&P sold EDM/thinkFolio), consistent with the "moat = data, not tooling" thesis.

**Risk flags.**
1. **Disintermediation of the desktop layer (FactSet-specific).** FDS's 13.2x fwd P/E vs 20–30x peers signals the market already prices AI risk at the analyst-desktop tier; if Codex/Perplexity/AlphaSense capture the query/workflow, FactSet keeps data licence revenue but loses the higher-margin interface — margin captured by another stack layer. Why: value migrates to whoever owns proprietary data OR the agent, and FDS owns less unique data than Bloomberg/S&P.
2. **The moat thesis assumes data stays licensed, not scraped/synthesized.** The newsletter's core bet (moat → data vendors) breaks if LLMs increasingly reconstruct "good-enough" fundamentals from filings/alt-data (Daloopa/Hebbia already extract from primary docs), eroding pricing power at the mid-tier. Why: commoditization historically starts at the low end (priced-out users) and moves up.
3. **Cyclicality + concentration for the "moat" names.** Moody's/S&P ratings revenue is tied to debt-issuance volume (cyclical); MCO/MSCI at 27–30x fwd P/E leave no margin for a ratings-volume downturn or AI-driven ESG/index fee compression. Why: rich multiples on cyclical/regulated tolls re-rate hard on any structural doubt.

**What this changes (idea-lens).** (analysis) Not a re-rating of OpenAI — it's a *relative* signal for the incumbents: the four "data moat" names split into toll-roads (MCO/SPGI-ratings/MSCI, premium, defended by regulation + index network effects) vs contested desktop (FDS, discounted, in the blast radius). Falsifiable thesis: if OpenAI/Perplexity's finance agents keep *licensing* incumbent data (as Codex does today), the moat holds and FDS's discount is overdone; the thesis breaks if a major buy-side client publicly *drops* a FactSet/Bloomberg seat for an AI-native stack, or if OpenAI moves from licensing to building/acquiring its own proprietary data. Watch next: FactSet's next ASV-growth print and any AI-native win of an institutional data contract as the trigger.

Sources: https://linas.substack.com/p/fintechpulse1085 · https://www.finextra.com/newsarticle/47846/openai-launches-codex-plugins-for-finance-pros · https://www.tradingview.com/news/stocktwits:bd2f0c1fa094b:0-openai-launches-new-codex-tools-for-non-developers-sees-110-growth-in-data-analytics/ · https://www.constellationr.com/insights/news/how-moodys-thinking-about-data-moats-ai-strategy-token-costs · https://www.gurufocus.com/term/forward-pe-ratio/FDS · https://www.gurufocus.com/term/forward-pe-ratio/MSCI · https://valueinvesting.io/SPGI/metric/forward-pe · https://www.financecharts.com/stocks/MCO/value/pe-ratio · https://www.techbuzz.ai/articles/the-bloomberg-terminal-is-getting-an-ai-makeover-like-it-or-not · https://www.cnbc.com/2025/03/31/openai-closes-40-billion-in-funding-the-largest-private-fundraise-in-history-softbank-chatgpt.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> Note: OpenAI (the note's headline company) is PRIVATE — no earnings; its only IR item is the $40B round (2025-03-31). This review pivots to the two PUBLIC incumbents the "moat stays with FactSet & Moody's" thesis actually rests on: **FactSet (NYSE: FDS)** and **Moody's (NYSE: MCO)**. FDS/MCO are not in ir_coverage.json and irdb is absent locally → figures via WebSearch, exact numbers only.

**Verdict (headline read).** Both incumbents printed BEAT-to-solid results that SUPPORT the moat thesis, and — crucially — both frame AI as a demand tailwind for their proprietary data, not an erosion of it.
- **FactSet — IN-LINE/modest BEAT** (fiscal Q3 2026, reported ~2026-07-01): revenue $622.9M (+6.4% YoY; organic +7%), adj. EPS $4.53 (+6.1% YoY), organic ASV +7.1% to $2.48bn; FY26 guidance reaffirmed. Shares dipped ~1.8% on the print (already-high expectations).
- **Moody's — BEAT** (most recently REPORTED quarter = Q1 2026, reported 2026-04-22): revenue ~$2.1bn (+8% YoY), adj. diluted EPS $4.33 (+13% YoY) vs ~$4.23 consensus; record quarterly rated issuance >$2 trillion; 2026 adj-EPS guidance raised to $16.40–$17.00. (Moody's Q2 2026 does NOT report until ~2026-07-22, so any "Q2 2026" figures circulating on 2026-07-13 are estimates, not actuals — excluded here.)

**Key figures (with growth).**
- FactSet fiscal Q3 2026: revenue **$622.9M, +6.4% YoY** (organic +7%); **organic ASV +7.1% to $2.48bn**; **adj. EPS $4.53, +6.1% YoY**; GAAP diluted EPS **$3.50** (down from $3.87 YoY — GAAP compressed vs adjusted). FCF +11.1% to $254.0M; $243.4M returned to shareholders in the quarter.
- Moody's Q1 2026: revenue **$2.1bn, +8% YoY**; **adj. diluted EPS $4.33, +13% YoY**; GAAP diluted EPS $3.73, +8%. Operating margin 44.3%; adj. operating margin 53.2%. MIS (ratings) record revenue ~$1.2bn on >$2trn rated issuance, ~67% adj. operating margin.

**By segment / driver.**
- FactSet: growth is subscription/ASV-led; management flagged **>10% of Q3 ASV growth came directly from AI SKUs** — i.e. AI is currently additive to the moat, monetized through new AI products layered on connected data + embedded workflows. Mix is shifting from seat-linked to enterprise/3+ yr agreements (avg contract term +~30%) while broadly preserving pricing — locks clients in.
- Moody's: two engines both up — MIS (ratings) on record issuance incl. **jumbo AI-related financings** (the AI capex buildout is itself feeding ratings volume), and Moody's Analytics on recurring "decision-grade" data demand.

**vs expectations / prior period.**
- FactSet: broadly in-line to slight beat (public aggregators: revenue $622.9M; adj. EPS $4.53); a pre-print preview had EPS est. ~$4.45. Stock fell ~1.8% — a "beat but priced-in" reaction, not a miss. Public consensus, as reported around the 2026-07-01 release.
- Moody's Q1 2026: adj. EPS $4.33 vs ~$4.23 consensus (≈+2.4% beat), revenue ~$2.1bn vs ~$2.07bn expected (≈+0.5%). Beat driven by record issuance + operating leverage; guidance was RAISED, signaling sustainability rather than a one-off. Consensus as of the 2026-04-22 release.

**Guidance / forward.**
- FactSet: FY2026 REAFFIRMED — GAAP revenue $2.45–$2.47bn, adj. operating margin 34.0–35.5%, adj. diluted EPS $17.25–$17.75 (GAAP $14.85–$15.35). Reaffirm (not raise) after a priced-in stock = disciplined, no acceleration signal.
- Moody's: RAISED 2026 adj. diluted EPS to $16.40–$17.00; ~$2.5bn buyback. Management tone confident; MIS visibility hinges on issuance staying elevated (rate/geopolitical risk is the swing factor).

**Thesis-flags (moat stays with FactSet & Moody's?).**
1. **AI reads as tailwind, not threat — supports the thesis.** FactSet: AI SKUs already >10% of ASV growth. Moody's CEO Rob Fauber: "as AI adoption accelerates, it is driving demand for Moody's decision-grade connected intelligence." Why it matters: the note's claim is that generative tools (OpenAI Codex-as-analyst) commoditize the *analysis layer* but not the *proprietary, licensed, decision-grade data layer* underneath — and both incumbents are monetizing exactly that layer. Second-order: they are inserting themselves into the AI stack (FactSet↔Gemini Enterprise / MCP + agents; Moody's embedded in Microsoft 365 Copilot, plus AWS/Anthropic bring-your-own-license) — the LLMs become distribution for their data, reinforcing the moat rather than bypassing it.
2. **Lock-in is deepening (FactSet).** Shift to enterprise/3+ yr agreements (+~30% avg term) with preserved pricing raises switching costs — de-PR: this also front-loads retention risk into fewer, larger renewals, but Q3 renewals skewed to these longer forms, a moat-positive.
3. **Moody's issuance benefits from the AI capex cycle itself.** Record >$2trn rated issuance partly from "jumbo AI-related financings" — the AI buildout that could theoretically disrupt them is currently *funding their ratings volume*. Second-order risk: issuance is cyclical/rate-sensitive, so this tailwind is not structural like the data moat.
4. **What's quieter / de-PR.** FactSet's GAAP EPS fell YoY ($3.87→$3.50) even as adjusted rose — AI/transition investment is a real near-term GAAP margin cost; the stock's ~1.8% dip says the market wants acceleration, not just reaffirmation. Moody's is one quarter stale (Q1) — the Q2 print (2026-07-22) will be the real-time test of whether issuance/AI-demand momentum held.

Net: reported results **support** the note's "moat stays with FactSet & Moody's" thesis — both are growing on proprietary data + embedding into the AI stack, with AI showing up as incremental revenue, not disintermediation. The nuance the headline omits: FactSet's growth is steady-not-accelerating (reaffirm + priced-in dip), and Moody's ratings tailwind is partly cyclical.

Sources: FactSet fiscal Q3 2026 — https://www.stocktitan.net/sec-filings/FDS/8-k-factset-research-systems-inc-reports-material-event-c8dce829df21.html · https://finance.yahoo.com/markets/stocks/articles/factset-research-systems-inc-fds-210048881.html · https://www.investing.com/news/company-news/factset-q3-fy26-slides-ai-adoption-fuels-71-asv-growth-93CH-4770815 · https://www.fool.com/earnings/call-transcripts/2026/07/01/factset-fds-q3-2026-earnings-call-transcript/ · Moody's Q1 2026 (reported 2026-04-22) — https://s203.q4cdn.com/694693571/files/doc_financials/2026/q1/1Q26-Earnings-Release-vFINAL.pdf · https://www.sec.gov/Archives/edgar/data/1059556/000162828026026383/a1q26earningsrelease.htm · https://www.stocktitan.net/sec-filings/MCO/8-k-moodys-corp-de-reports-material-event-ce5b3707785a.html · https://stockstory.org/us/stocks/nyse/mco/news/earnings-call/the-top-5-analyst-questions-from-moodyss-q1-earnings-call · Note: Moody's Q2 2026 reports ~2026-07-22 (not yet reported as of 2026-07-13) — any "Q2 2026 actuals" circulating are estimates and were excluded. FactSet CEO name from one aggregator was inconsistent/unverifiable, so not attributed. [Figures via public aggregators / IR releases; no paid feeds]
<!-- /enrichment:earnings_review -->
