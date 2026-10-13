---
title: "Robinhood gives AI agents a trading account and a credit card"
date: 2026-10-13
retrieved: 2026-10-13
tags:
  - company/robinhood
  - industry/trading
  - industry/agentic-commerce
  - region/us
  - type/product
sources:
  - https://finance.yahoo.com/markets/crypto/articles/robinhood-gave-ai-agents-trading-014207554.html
status: enriched
n_mentions: 1
channels:
  - "The Fintech Blueprint"
story_id: s3a3fa83b
month: 2026-10
enriched: true
importance: 2
freshness: stale
duplicate_of: sc9ed16ff
---

# Robinhood gives AI agents a trading account and a credit card

> [!info] 2026-10-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: The Fintech Blueprint

## Агрегированный текст (из дайджестов)

[The Fintech Blueprint] Robinhood Gave AI Agents a Trading Account and a Credit Card - Yahoo Finance

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://finance.yahoo.com/markets/crypto/articles/robinhood-gave-ai-agents-trading-014207554.html>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Robinhood gives AI agents a trading account and a credit card
_Analytical notes (not a post). Importance: 2/5. **FRESHNESS: STALE** — re-run of the May 2026 launch, see [[Robinhood lets AI agents trade stocks and issues agent credit card]] (story sc9ed16ff)._

## [0] What exactly happened (de-PR'd)
This item is **not a new product launch**. The two capabilities in the headline — an AI-agent "trading account" and an AI-agent credit card — were actually launched on **2026-05-27** ("Robinhood is Now Open to Agents") and are already covered in the corpus at [[Robinhood lets AI agents trade stocks and issues agent credit card]].

De-PR'd facts (unchanged since May):
- **Agentic Trading** (beta): a *sandboxed sub-account* funded with a user-set balance; the user connects a third-party AI agent via Robinhood's **MCP (Model Context Protocol) servers**. Agent can read/analyze the full portfolio but can only place orders against the pre-loaded wallet. **Equities only** at launch; options/crypto/event-contracts/futures "planned."
- **Agentic Credit Card**: a virtual card the agent spends on via **Robinhood Banking's MCP server**; **3% cash back**, user-set spending caps.
- Guardrails: isolated account, spend caps, manual-approval option, real-time activity feed, one-tap kill switch.

What is actually *new* in the Oct source (Yahoo/Forkast, **2026-10-02**, analysis piece "The Liability Gap Just Got Wider"), tied to the **2026-09-29 HOOD Summit**:
- A **"Loops"** feature letting agents trade autonomously 24/7 ("while you sleep") — i.e. **removing the human-in-the-loop** entirely, a meaningful escalation over the May beta.
- Post-launch **adoption**: ~**150,000** agentic accounts opened since May; agents hitting Robinhood tools ~**30M interactions/day** (open to all ~27.5M funded accounts).
- A sharpened **liability framing**: Robinhood routes the tech through **Robinhood Labs LLC**, "explicitly not a broker-dealer, investment adviser, or money transmitter… a technology company," and ToS puts all risk on the user ("You assume all risk for trades executed by AI agents and for any use of your data by third-party LLM providers"; Robinhood "does not control, supervise, monitor, recommend, or audit agents").

**Why framed this way / what it reveals:** The Yahoo headline recycles the May product as if new because the *news* is really the governance critique + the "Loops" 24/7 extension, not the account/card themselves. The liability design (segregate the agent tech into a non-regulated LLC, push all risk to the user) is the actual substance — it lets Robinhood ship agent autonomy without taking on broker-dealer suitability duty for machine-initiated trades.

## [1] Competitors / peers
Agentic-finance landscape (corpus):
- **Payments/commerce rails** (not brokerage): [[Revolut is preparing its payment platform for the rise of agentic commerce,]] (AP2/Google, Jan 2026), [[PayPal supports trusted AI checkout with Google]], [[PayPal acquires Cymbio to accelerate agentic commerce]], [[Nuvei supports Visa Trusted Agent Protocol]], Mastercard/Visa Trusted Agent Protocol, [[Fintech Wrap Up How UCP uses AP2 for autonomous payments]], [[Tria raises $12M for self-custodial neobank for humans and AI]].
- **Brokerage-side agentic access**: Robinhood remains one of the **first mainstream retail brokers** to give *outside* agents sanctioned MCP access to a brokerage + credit line (rather than scraping/unofficial APIs). Direct peer launches are thin — this is genuinely ahead on the *brokerage* vertical.

**Why the lay of the land is this way:** the agentic-commerce race (Visa/MC/PayPal/Google AP2) is about **who owns the payment rail** for agent purchases; Robinhood's twist is applying the MCP-agent pattern to *investing*, where the regulatory bar (suitability, best-execution, fiduciary) is far higher than for checkout — so being "first" here is as much a liability bet as a product edge.

## [2] Company history / fit
Robinhood's 2024-26 arc: acquired AI research platform **Pluto (2024)**, added an AI investing assistant (2025), then **Cortex** AI, the **super-app / family-finance** pivot ([[Robinhood pivots to super app for family finance]]), the **$695 Platinum card** ([[Robinhood debuts $695 Platinum card to rival Amex]]), RIA tools ([[Robinhood launches Advisor Network and RIA AI tools with TradePMR]]), and aggressive risk products — **10x crypto leverage** ([[Robinhood launches 10x leverage on Bitcoin and Ether]]), prediction markets, futures. Agentic trading fits the pattern: maximize engagement/velocity on a transaction-take-rate model.

**Why it acts this way:** Robinhood monetizes order flow + activity, so a product that generates ~30M agent interactions/day and 24/7 autonomous trading is directly accretive to its core PFOF/transaction economics — the structural pressure is to push *more trading velocity*, and agents are a velocity multiplier.

## [3] Novelty / value-add / traction
- **Not new as a product** (May launch). **New** vs the May note: the **"Loops" 24/7 no-human-in-loop** escalation + the first hard **traction numbers** (150k accounts, 30M daily calls) and the sharpened **liability-gap** analysis.
- Traction is real but should be read skeptically: "accounts opened" and "tool interactions" are activation metrics, not evidence of profitable agent trading or sticky AUM; a single MCP handshake per poll inflates the 30M/day figure.

**Why the value-add is contestable (deeper):** The margin in agentic *investing* sits with whoever controls the rail the agent must traverse — here Robinhood *is* the rail (its own MCP servers), so unlike Ramp-vs-Visa it captures the transaction. BUT the durable risk is **regulatory**: by design Robinhood disclaims supervision/suitability and shunts liability to the retail user. That is the fragile load-bearing assumption — if a regulator reclassifies agent-initiated trades as requiring broker suitability/human validation, the whole "tech company, not a broker" firewall (Robinhood Labs LLC) is what breaks.

## [4] What's next / market sentiment
- Roadmap: extend beyond equities to options/crypto/event-contracts/futures; "Loops" generalization; deeper Cortex integration.
- Regulatory backdrop: **FINRA's 2026 Annual Regulatory Oversight Report** addressed AI agents for the first time — flagged "autonomy without human validation, scope creep, auditability, misaligned reward functions." No **SEC/CFTC/FINRA rule specific to agentic trading** yet; FINRA calls existing rules "technologically neutral." Pointed asymmetry: **RIAs cannot delegate client management to AI agents, yet retail users can grant full autonomous authority** with no equivalent guardrail.

**Why the market goes this way / second-order:** the open legal question — *when an agent makes a trade the user did not intend, who is liable?* — is unresolved. Counterintuitive effect: Robinhood's first-mover "openness" concentrates **regulatory + reputational tail risk** on Robinhood even as the ToS shifts dollar liability to users; a single high-profile agent-driven blowup (amplified by 24/7 "Loops" + 10x leverage) could trigger exactly the rulemaking that guts the model. Being first here is fragile, not safe.

## Sources
- Yahoo Finance / Forkast, 2026-10-02 — "Robinhood Gave AI Agents a Trading Account and a Credit Card. The Liability Gap Just Got Wider." (primary link in note)
- Robinhood Newsroom — "Robinhood is Now Open to Agents" (2026-05-27 launch)
- TechCrunch / Bloomberg / Decrypt / SiliconANGLE, 2026-05-27 (launch coverage)
- Coindesk, 2026-09-30 — "Robinhood is giving customers an AI agent that trades for them, plus 10x crypto bets" (HOOD Summit / Loops)
- FINRA 2026 Annual Regulatory Oversight Report (AI agents section)
- Corpus: [[Robinhood lets AI agents trade stocks and issues agent credit card]] (duplicate source event)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 2/5** — The underlying products (agentic trading account + AI agent credit card) are a **re-run of the 2026-05-27 launch** already in the corpus ([[Robinhood lets AI agents trade stocks and issues agent credit card]], sc9ed16ff). The Oct source is an analysis/re-report (Yahoo/Forkast, 2026-10-02) whose only new content is the Sept-29 HOOD Summit "Loops" 24/7 extension + first adoption stats + a liability-gap critique — incremental, not a new event. Marked **stale** (duplicate_of sc9ed16ff). Weight comes from the governance angle, not novelty.

## Red-team / challenge questions

1. **Is this a new launch?** No — open. Core products launched 2026-05-27; this is a re-framing. Only "Loops" (24/7, no human-in-loop, Sept 29) is incremental-new.
2. **What exactly is new vs May?** 24/7 autonomous "Loops"; ~150k accounts; ~30M agent tool-calls/day; explicit liability-gap framing via Robinhood Labs LLC. — answered.
3. **Are the adoption numbers meaningful?** Open/skeptical — "accounts opened" and "tool interactions/day" are activation vanity metrics; no disclosed agent-driven AUM, P&L, or retention. 30M/day could be polling, not trades.
4. **Who bears liability for an unintended/erroneous agent trade?** Answered: the **user**, per ToS. Robinhood "does not control, supervise, monitor, recommend, or audit agents." No regulator has blessed this allocation.
5. **Why segregate into Robinhood Labs LLC?** Answered (analysis): to assert "technology company, not broker-dealer/adviser/money transmitter" and dodge suitability/best-execution duty for machine-initiated orders.
6. **Does any rule actually govern agentic retail trading?** Answered: No SEC/CFTC/FINRA-specific rule; FINRA 2026 report flags the risks but calls existing rules "technologically neutral." Open legal question.
7. **Why can RIAs NOT delegate to AI agents but retail users can grant full autonomy?** Answered (source): a real regulatory asymmetry; fiduciary standard blocks advisers, caveat-emptor leaves retail exposed. Key second-order fragility.
8. **Who captures the margin?** Answered (analysis): Robinhood is its own rail (MCP servers) so it captures transaction economics — unlike agentic-commerce players dependent on Visa/MC/AP2.
9. **Does "Loops" + 10x leverage + 24/7 autonomy compound risk?** Open: plausibly yes — autonomous leveraged trading without human validation is a tail-risk amplifier; no data on blowups yet.
10. **Is Robinhood actually ahead of peers?** Answered: yes on the *brokerage* vertical (first mainstream retail broker with sanctioned outside-agent MCP access); agentic-commerce peers (Revolut/PayPal/Visa/MC) are payments-rail, not brokerage.
11. **What breaks the model?** Answered (analysis): a regulator reclassifying agent trades as requiring broker suitability/human validation collapses the "tech, not broker" firewall.
12. **Is the credit-card piece material or a sidecar?** Open — 3% cashback virtual card via Banking MCP is minor vs the trading story; mostly a halo product.
13. **Does the duplicate note warrant a fresh post?** No — the agentic account/card are the same event. Only a standalone "Loops / 24-7 autonomous + FINRA liability gap" angle would be fresh, and that overlaps the existing note's scope.
14. **Any conflict between sources?** Minor: launch described as "beta, equities only" in May vs broadening roadmap by Oct — consistent, incremental.
15. **Second-order sentiment effect?** Answered (analysis): first-mover openness concentrates regulatory/reputational tail risk on Robinhood even while dollar liability is pushed to users — fragile, not safe.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** The story sits in the **agentic-finance / agentic-commerce** race — AI agents getting their own authenticated spending and (here) *trading* rails. 2025–26 the payment networks built parallel standards: Visa launched its **Trusted Agent Protocol** (Oct 2025, per [[Visa launches Trusted Agent Protocol for AI commerce]]) and now "Intelligent Commerce Connect" (single merchant integration); Mastercard's **Agent Pay** went live (first live agentic txns in APAC, Feb–Mar 2026); **PayPal adopted the OpenAI/Stripe Agentic Commerce Protocol (ACP)** to transact inside ChatGPT against its 400M+ wallets ([[PayPal adopts Agentic Commerce Protocol, expands in ChatGPT]]). Robinhood's move is the first time a US retail *broker* lets third-party agents (built on Claude / ChatGPT, via Robinhood's **MCP servers**) place, modify and cancel equity trades 24/7 via standing "Loops," plus an **Agentic Credit Card** (3% cash-back, Gold-linked). Why now: (i) model capability + protocol standardization (MCP/ACP/AP2) make agent-to-rail plumbing cheap; (ii) a permissive 2026 US posture — FINRA's 2026 oversight report only *names* agent risk for the first time; (iii) brokerage economics reward activity, and agents trade more. Note the de-PR point: OpenAI *deprecated* its ChatGPT Instant Checkout in Mar 2026 (only ~a dozen Shopify merchants ever live) — "announced ≠ adopted" is the sector's recurring tell; Robinhood's 150k accounts / ~30m daily tool-calls is one of the few *adoption* datapoints.

**Competitive landscape.** Sector KPIs for a broker: **transaction-based revenue, net deposits, platform assets (AUC), Gold attach rate, ARPU**. Players split into (a) payment rails arming agents to *spend* (Visa, Mastercard, PayPal, Stripe/OpenAI, Coinbase x402) and (b) brokers arming agents to *invest* — where Robinhood is effectively first-mover; Schwab, IBKR, eToro, Webull have not opened autonomous-trade APIs to third-party LLMs. Basis of competition: distribution + product surface, not price. Recent moves: product first shipped **May 2026** ([[Robinhood lets AI agents trade stocks and issues agent credit card]]); the Oct-2026 coverage reframes it around the *liability gap* now that it is live. **Position:** ahead / land-grab, but the moat is thin — the agent logic lives in third-party LLMs; Robinhood supplies rails + the Gold subscription hook (switching cost = funded capital + 17% Gold attach), `(analysis)`.

**IR grounding — PRIMARY evidence (HOOD, Q2 2026, reported 29 Jul 2026).** Net revenues **$1.31bn, +32% YoY**; **transaction-based revenue $776m, +44% YoY** (event contracts, options, equities). Record **net deposits $21.7bn** (+28% annualized); **total platform assets $369bn (AUC)**; Retirement AUC **$34.5bn, +82%**. Record **Gold subscribers 4.8m (17% attach)**. Adj. EBITDA margin **57%**; 13 business lines now >$100m annualized revenue. Read-through: agentic trading directly feeds the fastest-growing, highest-margin line (transaction revenue) and raises Gold stickiness — a revenue flywheel, not a moonshot. (Source: HOOD Q2-2026 release / investors.robinhood.com; latest EDGAR 10-Q filed 2026-06-30 hood-20260630.htm, sec.gov.)

**Comps & multiples.** Verifiable arithmetic from IR: **take-rate proxy** = transaction revenue / platform assets = $776m-qtr / $369bn ≈ **0.21%/qtr** (~0.8% annualized on AUC) — a thin, activity-driven take rate, so agent-driven volume is the lever. **Gold attach** = 4.8m / net-funded ≈ **17%** (per Robinhood). Private/peer agentic-rail comps (round-stage, not market cap): [[Basis Theory raises $33 million for agentic commerce]], [[Paygentic raises $2M pre-seed for AI payments infrastructure]], [[Tria raises $12M for self-custodial neobank for humans and AI]] — early, sub-Series-A, signalling the vertical is pre-consolidation. **HOOD equity multiples (EV/Rev, P/E): no data** — live market cap/EV not sourced this turn, so not computed rather than estimated. Qualitative: HOOD is a hyper-grower (rev +32%, txn +44%), so a rich revenue multiple would be growth-justified, not an automatic flag.

**Risk flags.**
1. **Liability / fiduciary gap (primary).** Robinhood Labs LLC is explicitly *not* a broker-dealer, adviser or money transmitter; the TOS pushes *all* risk onto the user — "You assume all risk for trades executed by AI agents and for any use of your data by third-party LLM providers." RIAs are *barred* from letting agents manage client money (fiduciary standard), yet retail can now hand a model autonomous trade authority. Second-order: a mis-aligned agent or bad "Loop" at scale invites FINRA/SEC action and reputational blowback that could claw the feature back.
2. **Suitability / autonomy.** Standing "Loops" trade 24/7 without per-trade human validation and agents get broad *read* access to all balances/positions — scope-creep and auditability risk flagged by FINRA's 2026 report; retail harm is concentrated in the least sophisticated users.
3. **Thin moat / disintermediation.** The intelligence sits in OpenAI/Anthropic models, not Robinhood; if the networks (Visa/Mastercard) or an LLM platform own the agent-authentication layer, Robinhood risks being commoditized rails while another stack layer captures the economics.

**What this changes (idea-lens).** `(analysis)` This is a *new-entry* land-grab that could re-rate HOOD's transaction line if agentic volume compounds the already-+44% txn revenue — but it is equally a regulatory lightning rod. Falsifiable thesis: agentic accounts become a durable driver only if they survive the first FINRA/SEC scrutiny *without* a forced rollback or liability reversal. Watch: (trigger) FINRA/SEC guidance on retail agent authority, a headline loss-and-dispute case, and whether Q3/Q4-2026 disclosures *quantify* agentic volume/revenue (silence = still PR, not P&L).

Sources: https://finance.yahoo.com/markets/crypto/articles/robinhood-gave-ai-agents-trading-014207554.html · https://robinhood.com/newsroom/robinhood-is-now-open-to-agents/ · https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results · https://www.sec.gov/Archives/edgar/data/0001783879/000178387926000114/hood-20260630.htm · https://forkast.news/robinhood-gave-ai-agents-a-trading-account-and-a-credit-card-the-liability-gap-just-got-wider/ · https://techinformed.com/visa-opens-one-integration-for-ai-agent-payments/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** BEAT. Robinhood's latest print is Q2 2026 (quarter ended 2026-06-30, reported 2026-07-29) — the Q2 2026 10-Q (filed 2026-07-29) and Q2 2026 results release are the primary sources; irdb carries only up to the June 2026 8-Ks, so figures are quoted from Robinhood's own release/10-Q via the IR site. Record total net revenue $1.31bn (+32% YoY) vs. public consensus ~$1.25–1.29bn; GAAP diluted EPS $0.62 (+48% YoY) vs. consensus ~$0.42 — a large headline EPS beat, but ~$0.14 of it is a one-off non-cash gain ($129m from deconsolidation of Robinhood Ventures Fund I/RVI), so the clean operational beat is narrower. Drivers: record transaction revenue and record net deposits; guidance action — 2026 adjusted OpEx + SBC guidance *lowered and tightened* to $2.675–2.775bn.

**Key figures (with growth).**
- Total net revenues: $1.31bn (+32% YoY, +23% QoQ) — record.
- Transaction-based revenues: $776m (+44% YoY). Mix: options $342m (+29%), event contracts/prediction markets $156m (new, scaling fast), equities $129m (+95%), crypto $100m (-38% YoY).
- Net interest revenue: $389m (+9% YoY) — the slowest-growing line (rate-sensitive, decelerating vs. the double-digit transaction lines).
- Other revenues (subscriptions/services): $143m (+54% YoY).
- Net income (GAAP): $573m (+48% YoY); diluted EPS $0.62 (+48%), inflated ~$0.14 by the RVI deconsolidation gain.
- Adjusted EBITDA: $741m (+35% YoY), ~57% quarterly margin (LTM $2.8bn at 56%) — operating leverage intact.

**Operating metrics.**
- Net deposits: record $21.7bn in the quarter (~28% annualized); LTM $76bn (+27%).
- Assets under custody: $369bn (+32% YoY) — equities $266B (+66%), crypto $50B (+17%), RIA $50B. AUC/funded customer ~$13,000 (vs. ~$10,500 a year ago).
- Funded customers: 28.4m (+1.9m / +7% YoY); +940k QoQ (largest sequential add in ~5 years, incl. ~300k from WonderFi).
- Gold subscribers: 4.84m (+1.4m / +39% YoY), 17% adoption (vs. 13.1%).
- ARPU: $187 (+24% YoY).

**By segment / driver.** Growth is broadening off commission-equivalent trading into recurring/durable lines: equities (+95%) and prediction markets ($156m, event-contract volume ~13.6bn, +~10x YoY) are now material, and Robinhood says it runs 13 business lines over $100m annualized (up from 9 in 2024, 1 in 2019). The one clear soft spot is crypto transaction revenue, down 38% YoY — management stayed largely silent on the decline, framing it as volume softness with take-rates holding. Net interest revenue (+9%) is the laggard as rate tailwinds fade; the thesis increasingly rests on fee-based volume, subscriptions and the new banking/card stack rather than NIM.

**vs expectations / prior period.** Revenue beat public consensus by roughly $20–60m (+~1.5–5%) depending on source (StockAnalysis/Yahoo-type aggregators, "expected as of" late July 2026). EPS beat of ~$0.20 (~48%) is flattered by the RVI one-off — adjust for it and the EPS beat is modest. Momentum vs. prior quarters: +32% YoY revenue and +23% QoQ mark re-acceleration and the best quarter since IPO on deposits/customer adds. (No prior Robinhood earnings note found in the corpus to `[[wikilink]]`.)

**Guidance / forward.** Management *lowered and tightened* FY2026 adjusted OpEx+SBC guidance to $2.675–2.775bn (down from prior) while still funding new initiatives — a positive cost-discipline signal that supports the margin story. July trends flagged as "similar area" to record Q2 volumes for equities/options, with net deposits tracking ~$4bn (ex-Trump Accounts), implying some seasonal moderation but no deceleration alarm. Tone: confident/ambitious (Tenev's "make everyone an owner"), with CFO Verma stressing profitability alongside expansion.

**Thesis-flags (how the agent-trading / credit-card product fits the revenue mix).**
1. The agentic-trading account + credit card in the news is an *incremental monetization + new-TAM* extension of a franchise already compounding at +32% revenue / +48% net income — it lands on strength, not as a rescue. Why it matters: it feeds the same two engines the quarter proved out (transaction volume + net deposits/AUC), so the first-order effect is more order flow and more balances, not a wholly new P&L line.
2. Credit card is already a *real, live* driver, not a slide: Gold Card hit 1m cardholders with ~$17bn annualized purchase volume and banking deposits >$3bn since the November launch. Second-order effect: interchange + deposit funding deepen the "primary financial account" wedge and lift net-deposit durability — the exact metric that hit a record this quarter.
3. Agentic/AI-agent trading is early and friction-heavy: management cited only ~100,000 integrated agentic accounts and flagged code-complexity/model-familiarity friction, with a v2.0 to simplify. De-PR: "AI agents get a trading account" is announced/early-adoption, not yet a monetized segment — treat it as optionality on new TAM (agent-driven order flow) rather than near-term revenue; it is not among the 13 $100m+ lines.
4. Quality-of-beat flag: the headline $0.62 EPS and crypto's -38% both argue for caution — strip the RVI one-off and watch whether crypto/NIM stabilize; if the new banking/card/prediction-market lines keep +40–95% growth, the mix shift away from rate-sensitive NIM is a structural positive.

Sources: Robinhood Q2 2026 results release & 10-Q (period ended 2026-06-30, filed 2026-07-29), investors.robinhood.com/news-releases + SEC 10-Q https://www.sec.gov/Archives/edgar/data/0001783879/000178387926000114/hood-20260630.htm · Q2 2026 earnings presentation https://investors.robinhood.com/static-files/f5aa8c24-cd37-4a94-9169-cd04759e02a1 · earnings-call transcript (management tone/guidance) https://www.investing.com/news/transcripts/earnings-call-transcript-robinhood-beats-q2-2026-estimates-as-growth-stays-strong-93CH-4821999 · public consensus (late-Jul-2026) via https://www.tradingview.com/news/tradingview:a628c3b432afe:0-robinhood-reports-q2-2026-revenues-1-31b-net-income-573m-diluted-eps-0-62/ · irdb (ir_latest.json) robinhood entry — latest on-disk filing is the 2026-06 8-K (pre-Q2 print), so Q2 figures sourced from Robinhood's own release. Prior-quarter corpus note: no data (no Robinhood earnings note in base).
<!-- /enrichment:earnings_review -->
