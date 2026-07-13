---
title: "Linas Newsletter: Brokerages race to give AI agents trading control"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/sofi
  - company/robinhood
  - industry/trading
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://substack.com/app-link/post
  - https://substack.com/redirect/b5a3ed2c-4949-43b0-a10f-4db7b681c2ed
  - https://substack.com/redirect/e607a64d-1cb3-4683-a362-e62445d00f94
  - https://substack.com/redirect/05c616fc-ce93-4f2e-b89f-12092e88c223
status: published
n_mentions: 3
channels:
  - "Linas Newsletter"
story_id: se13e1c79
month: 2026-06
enriched: true
importance: 3
---

# Linas Newsletter: Brokerages race to give AI agents trading control

> [!info] 2026-06-26 · 3 упоминаний · 0 источника(ов) с текстом
> Каналы: Linas Newsletter

## Агрегированный текст (из дайджестов)

[Linas Newsletter] SoFi acquired Composer and bet against the Agentic AI trading rush 🤖💸; Plaid’s AI now sees what no single bank can 👀🏦

[Linas Newsletter] Following the money 💸 Every major brokerage is now racing to let AI make investment decisions for its customers. FinTech giant SoFi $SOFI thinks most investors would rather build their own strategy.

[Linas Newsletter] In the span of just four weeks, Robinhood shipped Agentic Trading, letting users connect external AI agents to isolated brokerage accounts for autonomous stock trades. Meanwhile, Coinbase followed with a 21-product blitz that included Coinbase Advisor, one of the first SEC-registered AI investment advisors, alongside Coinbase for Agents, a platform enabling third-party AI to trade crypto within user-set limits.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/app-link/post>
- <https://substack.com/redirect/b5a3ed2c-4949-43b0-a10f-4db7b681c2ed>
- <https://substack.com/redirect/e607a64d-1cb3-4683-a362-e62445d00f94>
- <https://substack.com/redirect/05c616fc-ce93-4f2e-b89f-12092e88c223>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Brokerages race to give AI agents trading control (Lina's Newsletter)
_Analytical notes (not a post). Importance: 3/5._
_Nature: third-party analysis/essay, not a primary event. Its value is the SYNTHESIS — "every brokerage is racing to let AI trade, and SoFi is the contrarian bet" — not new facts. The underlying events each have their own notes (see [[wikilinks]]); this note's job is to judge whether the framing adds incremental insight._

## [0] What exactly happened (de-PR'd)
Lina's Newsletter is an opinion essay built on a real, dated cluster of mid-2026 launches, plus one contrarian read:
- **Robinhood Agentic Trading** (2026-05-27): external AI agents connect via an **MCP server** to an isolated, dedicated brokerage sub-account; broad *read* access, trading scoped to that one account; stocks only at launch; beta. Plus an "agentic" virtual credit card. → [[Robinhood lets AI agents trade stocks and issues agent credit card]].
- **Coinbase blitz** (2026-06-11/12): "Coinbase for Agents" (third-party AI trades crypto + pays within user-set limits, MCP/CLI) → [[Coinbase launches Coinbase for Agents to connect AI agents to accounts]]; and **Coinbase Advisor**, an SEC-registered RIA AI advisor → [[Fintech Blueprint Coinbase AI advisor registers as SEC RIA; Mercury launches Command]].
- **SoFi's counter-bet** (2026-06-23): SoFi acquired **Composer** to let users *build/backtest/execute their own* plain-language strategies — framed by Lina as betting AGAINST full autonomous agentic trading, on the thesis that most investors want to author their own strategy, not hand the keys over → [[SoFi acquires Composer for AI-powered investing]].

**Why the essay is framed this way (and the de-PR caveat):** The "every major brokerage is racing" line is directionally true (Robinhood, Coinbase, eToro 2026-03-26, Public.com 2026-03-31, IBKR 2026-06, Alpaca MCP) but flattens a critical distinction the essay underplays: almost all of these are **self-directed accounts where the USER keeps all liability** (legally closer to API trading than to a fiduciary robo-advisor). The "race" is a race to ship *plumbing* (MCP servers, scoped keys, OAuth connectors) — not a race to take discretionary fiduciary responsibility. The SoFi/Composer "contrarian" framing is also partly a face-saving narrative: SoFi was *late* to agentic execution, and "users want to build their own" conveniently matches what it just bought.

## [1] Competitors / peers
Two visible camps by mid-2026 (analysis):
- **Hand the agent the wheel (self-directed, user liable):** Robinhood (MCP, optional confirm), Coinbase (limits-based), **eToro** Agent Portfolios (scoped API key, $200 min, 2026-03-26), **Public.com** ("world's first Agentic Brokerage," 2026-03-31, but waitlisted) → [[Public deploys AI agents for retail investor portfolios]], [[Public launches AI-powered brokerage with custom indexes]]. Infra layer: **Alpaca** open-source MCP server → [[Alpaca raises $150M Series D at $1.15B valuation]], [[Alpaca partners with Composer, ZAD and Manzil to expand access]].
- **Human-in-the-loop / cautious:** **Interactive Brokers** (no key sharing; *mandatory per-instruction client approval* before any order — the safest design); **Charles Schwab** (2026-05 AI launch is *read-only insights, no trading at all*); **SoFi** (give users tools to author strategies, not autonomy).

**Why the lay of the land is this way / second-order:** The "first agentic brokerage" claims (Public vs eToro vs Robinhood, all within ~60 days) are competitive positioning, not technical firsts — the real first-mover is **Alpaca's API/MCP infra**, which has quietly powered this for developers for years. Second-order: the marketing battle is over *autonomy*, but the defensible moat is *distribution + the dedicated-account safety wrapper*, not the agent itself (any off-the-shelf LLM plugs in). That commoditizes the "agent" and shifts value back to whoever owns the account and the order flow.

## [2] Company history / fit (SoFi, as the essay's protagonist)
SoFi has been bolting AI/crypto onto a bank charter at speed: Agentic AI ETF (2025-09) → [[SoFi announces Agentic AI ETF]], SoFi Crypto (2025-11), SoFiUSD stablecoin (2026-05), PrimaryBid (2026-05). Composer (2026-06) fits as the *investing-tools* piece. **Why SoFi acts this way (analysis):** as a chartered bank with a brokerage, fiduciary/Reg BI exposure is more dangerous to SoFi than to a pure-play app; a "build-your-own-strategy" product keeps the user the decision-maker and SoFi out of the discretionary-advice liability seat — the same structural logic that makes the whole sector prefer self-directed framing.

## [3] Novelty / value-add / traction
**Genuinely new (mid-2026):** the *plumbing* — standardized agent-access rails (MCP servers at Robinhood/Alpaca/Coinbase, scoped-key sub-accounts at eToro, no-key OAuth + per-trade approval at IBKR) that let an off-the-shelf Claude/ChatGPT/Grok place *real* orders in *retail* accounts. That capability did not exist a year ago.
**What it is NOT:** a robo-advisor 2.0. Robo-advisors (Betterment 2010, Wealthfront 2011) are discretionary, fiduciary, rule-based. The new wave is a non-deterministic LLM driving a *self-directed* account where the retail user holds all liability — closer to "API trading with an LLM at the wheel."
**Traction = thin / PR-grade:** no platform disclosed agent-specific AUM or order volume. eToro's "46% jump in AI usage" conflates broad AI tools with the new Agent Portfolios. Public's "billions in assets" is total platform, not agent-managed. (analysis) **Where the margin sits:** because any LLM plugs in, the agent layer commoditizes; durable value accrues to whoever holds the account + order flow + the safety wrapper — i.e., the brokerage, not the AI vendor. This is the essay's strongest implicit insight, even if it doesn't state it crisply.

## [4] What's next / market sentiment
**Regulation is notably absent as a constraint:** the one SEC rule that would have bitten — the **Predictive Data Analytics conflicts rule — was formally WITHDRAWN (2025-06-12)**, leaving only technology-neutral **FINRA Notice 24-09** (existing rules apply) and live **AI-washing enforcement** (SEC v. Rimar, 2025). FINRA's 2026 oversight report adds AI-testing/human-in-the-loop emphasis but no binding agent rule. **Second-order risk (IOSCO Mar-2025, FSB Nov-2024):** if many agents act on correlated signals, herding/feedback-loop/concentration risk rises — agentic autonomy called "perhaps the most significant challenge on the horizon." Counterintuitive: the *safety* features brokerages tout (dedicated accounts, optional confirms) protect the *firm's* liability, not necessarily the market's stability, and quietly push downside onto retail users. SoFi's contrarian bet is plausible precisely because the liability math favors keeping the human as author.

## Sources
- Target note + aggregated digest text (Lina's Newsletter, 2026-06-26).
- Internal: [[Robinhood lets AI agents trade stocks and issues agent credit card]], [[Coinbase launches Coinbase for Agents to connect AI agents to accounts]], [[SoFi acquires Composer for AI-powered investing]], [[Fintech Blueprint Coinbase AI advisor registers as SEC RIA; Mercury launches Command]], [[Public deploys AI agents for retail investor portfolios]], [[Alpaca raises $150M Series D at $1.15B valuation]].
- Robinhood Agentic Trading: https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/ ; https://robinhood.com/us/en/support/articles/agentic-trading-overview/
- Coinbase for Agents: https://www.coinbase.com/developer-platform/discover/launches/agentic-wallets ; https://www.cnbc.com/2026/06/11/coinbase-launches-tool-to-let-ai-agents-manage-trading-and-payments.html
- eToro Agent Portfolios: https://www.financemagnates.com/fintech/etoro-lets-investors-delegate-trades-to-ai-agents-as-automation-usage-nearly-doubles/
- Public Agents: https://www.prnewswire.com/news-releases/public-becomes-the-first-brokerage-to-introduce-ai-agents-for-your-portfolio-302729050.html
- IBKR: https://www.businesswire.com/news/home/20260601336232/en/
- Alpaca MCP: https://alpaca.markets/mcp-server ; https://github.com/alpacahq/alpaca-mcp-server
- Schwab (read-only): https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability...
- SEC PDA rule withdrawn: https://www.sec.gov/rules-regulations/2025/06/s7-12-23 ; FINRA 24-09: https://www.finra.org/rules-guidance/notices/24-09 ; IOSCO PD788: https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf ; FSB: https://www.fsb.org/uploads/P14112024.pdf
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Challenge / red-team (second-order) — Brokerages race to give AI agents trading control

1. **Is the "every major brokerage is racing" claim true?** Mostly yes, directionally — Robinhood (2026-05-27), Coinbase (2026-06), eToro (2026-03-26), Public (2026-03-31), IBKR (2026-06), Alpaca (infra). But Schwab's "AI launch" is read-only with NO trading, and SoFi explicitly opts out of autonomy. So "racing to let AI *make decisions*" overstates it; several are racing to ship *rails* with human approval. **Partly open / overstated.**

2. **Is this actually new, or rebranded API/algo trading?** The LLM-in-the-loop + natural-language intent + retail self-directed account is new packaging on old infra (Alpaca API has done programmatic retail orders for years). Novelty is the standardized MCP/OAuth rails, not the concept. **Answered: incrementally new.**

3. **Who holds the liability when the agent loses money?** The USER. Robinhood: "You are ultimately responsible... not responsible for losses from agent-generated decisions." Public: user determines suitability. These are self-directed, not fiduciary. **Answered — and this is the load-bearing fact the essay underweights.**

4. **Does that liability structure let brokerages dodge Reg BI / fiduciary duty?** Plausibly — by framing the agent as the *user's* tool in a self-directed account, firms sidestep recommendation liability. Untested by regulators as of mid-2026. **Open (legal risk).**

5. **Is there any real adoption (AUM / order volume) or just press releases?** No platform disclosed agent-specific AUM or order volume. eToro's usage stats conflate broad AI tools; Public's "billions" is total platform. **Answered: traction is PR-grade, not metrics-grade.**

6. **Who really wins — the brokerage or the AI vendor (OpenAI/Anthropic)?** Any off-the-shelf LLM plugs into the MCP rail, so the agent commoditizes; the account holder + order flow + safety wrapper keeps the margin → brokerage wins the economics, AI vendor supplies the model layer. **Answered (analysis).**

7. **Is SoFi's "contrarian" bet genuine conviction or post-hoc spin for being late?** Both — SoFi was behind on agentic execution, and "users want to build their own" matches the Composer it just bought AND its higher bank-charter liability exposure. **Open / partly spin.**

8. **What's the regulatory backstop if agents misbehave at scale?** Thin. The SEC Predictive Data Analytics conflicts rule was WITHDRAWN (2025-06-12); only technology-neutral FINRA 24-09 + AI-washing enforcement remain. No binding agentic-trading rule. **Answered: regulation absent as a constraint.**

9. **Systemic risk if many agents trade on correlated signals?** IOSCO (Mar-2025) and FSB (Nov-2024) flag herding/feedback-loop/concentration risk; "agentic autonomy" called the biggest horizon challenge. No rules yet. **Answered: real but unregulated tail risk.**

10. **Do the touted safety features (dedicated accounts, optional confirms) protect the user or the firm?** Primarily the firm's liability surface; IBKR's *mandatory* per-trade approval is the only design that meaningfully protects the user from runaway autonomy. **Answered.**

11. **Which "first agentic brokerage" claim is real?** None as a technical first — Public, eToro, Robinhood all claim variants within ~60 days; Alpaca's infra predates all. Marketing, not milestone. **Answered.**

12. **Is the Coinbase Advisor RIA a different (safer) model than agentic trading?** Yes — an SEC-registered RIA carries fiduciary duty, unlike the self-directed agent rails. The essay lumps them together; they are legally opposite structures. **Answered: a meaningful distinction the essay blurs.**

13. **Does this essay add incremental insight beyond the individual event notes?** Modestly. The cross-cutting "race vs SoFi contrarian" frame and the implicit "agent commoditizes, brokerage keeps margin" angle are useful synthesis, but the single most important fact — user-held liability / self-directed framing — is underweighted, and no new primary data is added. **Answered: useful framing, not a must-read.**

14. **What would change the central question?** Shifting from "is everyone racing to agentic trading?" (yes, on rails) to "who absorbs the liability and the systemic risk when autonomous agents err at scale?" — currently the retail user and an unregulated market. That is the real weight of the story. **Answered (analysis).**

15. **Could regulation snap back and kill the model?** Possible but no live rulemaking; the binding rule was withdrawn, leaving enforcement-by-AI-washing as the main lever. **Open.**

Importance: 3/5 — A real, well-timed synthesis of a genuine mid-2026 cluster (Robinhood/Coinbase/eToro/Public agentic rails vs SoFi's build-your-own counter-bet), and the underlying events matter. Capped at 3 because it is third-party commentary that adds framing rather than facts, underweights the load-bearing user-liability/self-directed structure, blurs the RIA-vs-self-directed distinction, and rides a traction narrative with no disclosed AUM/volume.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-27]] (2026-06-27).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
_Market layer on top of context/challenge (those cover the event cluster, liability and regulation — not duplicated here). Skeptical; cite-or-`[UNSOURCED]`._

**Sector & drivers.**
This sits at the intersection of three markets, and the sizing depends heavily on which one you scope to — a key reason the "race" framing is slippery.
- **Robo-advisory (the closest sized adjacent, NOT the same product):** ~$12.9–14.3bn revenue in 2026, ~$2.7tn AUM, with multi-source CAGR estimates of ~22–30%+ to 2034–35 (per Fortune Business Insights / Business Research Insights / Statista, via secondary citations, as of 2026). Treat as an order-of-magnitude reference, not as the agentic-trading TAM: as the note's [3]/[challenge] establish, the new wave is *self-directed*, not discretionary/fiduciary robo — legally a different product, so robo TAM is an upper-bound proxy at best.
- **"Agentic AI in wealth management" sizing exists but is unreliable:** one report puts it at $3.2bn (2025) → $42.8bn (2034), ~37% CAGR, with "$620bn AUM" claims (Market Intelo / CoinLaw, via secondary). `[UNSOURCED]`-grade: these are new-vintage market-research reports with no auditable methodology, and the AUM figures almost certainly conflate broad AI tooling with true agent-managed assets — the same conflation the note flags in eToro's "46% AI usage." No verifiable agentic-trading TAM. **"no data" for a hard number.**
- **Structure:** the brokerage layer is **consolidating around a few scaled order-flow owners** (Robinhood, Coinbase, Schwab, IBKR, SoFi) while the *agent-access layer* is **fragmenting** into commodity MCP/OAuth rails (Robinhood, Coinbase, Alpaca, plus adjacent MCP launches: BitGo 2026-03, Blend 2026-05, Sumsub 2026-06, Coinbase Payments MCP 2025-10). Entry barrier is regulatory + capital (broker-dealer licence, custody, clearing) — NOT the agent, which is off-the-shelf. **Why now:** MCP standardization (2024–2026) + the SEC PDA conflicts rule withdrawn 2025-06-12 (per note) removed the one binding constraint; the cost of letting an LLM place a real order collapsed.

**Competitive landscape.**
Sector KPIs that actually run the economics: **transaction-based revenue, PFOF/order-flow take, equity/options/crypto notional volume, net deposits, platform AUC**. The "agent" is not yet a disclosed KPI at any platform (no agent-specific AUM/volume — see [3]).
- **Robinhood** — Q1 2026 revenue $1.07bn (+15% YoY); transaction revenue $623m (+7%), of which options $260m, equities $82m (+46%), crypto $134m (−47% YoY); platform assets $307bn (+39%); net deposits $18bn (per Robinhood Q1 2026 release). Shipped Agentic Trading 2026-05-27. Also cutting ~10% of staff (2026-06) — so "racing on AI" coincides with a cost reset.
- **Coinbase** — Q1 2026 revenue $1.4bn (−21% QoQ), net loss $394m, adj. EBITDA $303m; transaction revenue $756m, stablecoin revenue $305m (per CNBC/TIKR, Coinbase Q1 2026). Shipped Coinbase for Agents + SEC-registered Advisor RIA (2026-06).
- **SoFi** (protagonist) — Q1 2026 adj. net revenue ~$1.1bn, net income ~$167m, 14.7m members (per SoFi IR / investingintheweb). Contrarian Composer bet (2026-06).
- **Alpaca** — the real infra first-mover (open-source MCP), private, $1.15bn last round → [[Alpaca raises $150M Series D at $1.15B valuation]]. **Public.com / eToro / IBKR** — agent rails too, but Public is waitlisted and IBKR's design is human-in-the-loop (mandatory per-trade approval).
- **Position:** Robinhood is *ahead on distribution + the dedicated-account safety wrapper* (the actual moat, per note [1]); the agent layer is commoditized. SoFi is *catching up / deliberately niche* on a lower-liability framing. Moat lens: durable edge = **switching costs + order-flow scale**, not the LLM (intangible/network advantage accrues to the account holder, not the AI vendor). `(analysis)`

**Comps & multiples.** All on **P/S (annualized last-quarter revenue)** — P/E/EV-EBITDA skipped where loss-making or net cash undisclosed (`[UNSOURCED]`). Market caps are spot, late-June 2026, single-source, treat as ±range:
| Co | Mkt cap | Rev (Q1'26 ann.) | P/S | Flag |
|---|---|---|---|---|
| Robinhood | ~$85–95bn | $1.07bn ×4 = $4.3bn | $90bn / $4.3bn ≈ **21x** | rich — but rev +15% YoY, assets +39%; growth partly justifies |
| Coinbase | ~$37.6bn | $1.4bn ×4 = $5.6bn | $37.6bn / $5.6bn ≈ **6.7x** | optically cheap, but rev −21% QoQ + net loss → de-rated on declining crypto cycle, not a bargain |
| SoFi | ~$22.7bn | $1.1bn ×4 = $4.4bn | $22.7bn / $4.4bn ≈ **5.2x** | in-line for a profitable bank/fintech |

Internal comps (rounds, not market caps): [[Alpaca raises $150M Series D at $1.15B valuation]] (infra layer); [[CoinDCX raises from Coinbase at $2.45B valuation]]; Trade Republic €12.5bn secondary → [[Four European fintech deals raise EUR 45.1m in three weeks]]; sector context [[F-Prime Fintech Index adds over $200B market cap in 2025]], [[Blue Dot and FT Partners report sees fintech liquidity supercycle]] (Wealth & Capital Markets Tech $157bn private value). **Distribution not computed** (3 mixed-model names, annualized off one quarter — directional only). Read: Robinhood's ~21x is the outlier; it is a *growth* multiple, defensible only if growth holds — agentic trading must convert to real volume, not press, for it to stand. None of these multiples is *driven* by the agent product; the agent is currently a $0-attributable-revenue feature.

**Risk flags.**
1. **Multiple-without-monetization (re-rating risk).** Robinhood at ~21x P/S prices in continued growth, yet *zero* agent-specific revenue is disclosed across the sector. If agentic trading stays PR-grade (no AUM/volume) while the crypto/options cycle softens — as Coinbase's −21% QoQ and Robinhood's −47% crypto already show — the growth narrative funding the multiple is exposed. **Why:** the feature carrying the story isn't yet in the P&L.
2. **Liability/regulatory snap-back (tail, but binary).** The binding constraint (SEC PDA rule) is withdrawn, but the *self-directed = user-liable* structure is untested by regulators (note [4]/challenge #4). A single bad-faith or runaway-agent loss event could trigger FINRA/SEC action or a Reg BI reinterpretation that reclassifies the agent rail as a recommendation — instantly raising compliance cost for everyone except the human-in-the-loop designs (IBKR). **Why:** the economics depend on a liability dodge that hasn't been litigated.
3. **Disintermediation / herding (systemic + margin).** Two-sided: (a) margin — if the agent commoditizes, value could leak to whoever owns the *model + UX layer* (OpenAI/Anthropic) rather than the brokerage, should consumers anchor on the agent brand; (b) systemic — correlated agent signals → herding/feedback loops (IOSCO Mar-2025, FSB Nov-2024, per note). **Why:** both the firm's margin and market stability hinge on agents staying diverse and subordinate to the account holder.

**What this changes (idea-lens).** `(analysis)` This is a **plumbing build-out, not yet a re-rating event** — the durable winner is the order-flow + safety-wrapper owner, and the agent is a feature, not a franchise. Falsifiable thesis: *agentic trading will NOT move sector revenue/multiples until a platform discloses agent-specific AUM or order volume.* Trigger to watch: the first quarter any brokerage breaks out an "agent-driven" volume line (bullish confirmation) — or, on the downside, the first agent-loss enforcement action / FINRA agentic-trading rule, which would re-price the whole self-directed model and vindicate SoFi's contrarian, lower-liability bet.

Sources: https://www.globenewswire.com/news-release/2026/04/28/3283181/0/en/Robinhood-Reports-First-Quarter-2026-Results.html · https://www.cnbc.com/2026/05/07/coinbase-coin-earnings-q1-2026.html · https://www.tikr.com/blog/coinbase-q1-2026-earnings-revenue-down-21-but-derivatives-and-stablecoins-are-gaining · https://companiesmarketcap.com/robinhood/marketcap/ · https://finance.yahoo.com/quote/COIN/ · https://investingintheweb.com/digital-banks/sofi-statistics/ · https://www.fortunebusinessinsights.com/robo-advisory-market-109986 · https://www.statista.com/outlook/dmo/fintech/digital-investment/robo-advisors/worldwide · https://marketintelo.com/report/agentic-ai-in-wealth-management-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
