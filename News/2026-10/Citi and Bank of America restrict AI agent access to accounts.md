---
title: "Citi and Bank of America restrict AI agent access to accounts"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/citi
  - company/bankofamerica
  - industry/banking
  - region/us
  - type/regulation
sources:
  - https://tradersunion.com/news/institutions/show/3849745-us-banks-limit-ai-agent-access
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sc034e15d
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Citi and Bank of America restrict AI agent access to accounts

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Citi and Bank of America restrict AI agent access to customer accounts. Citi bars third party AI agents from transacting on its digital banking platforms. Both cite liability concerns as AI tools could shift deposits to higher yields.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://tradersunion.com/news/institutions/show/3849745-us-banks-limit-ai-agent-access>

## Контекст

<!-- enrichment:context -->
**[0] What exactly happened (de-PR'd).** Over a ~72h window in mid-October 2026, the big US banks moved, one after another, to bar *third-party* AI agents from logging into and *moving money* in customer accounts. Citi told the Financial Times (2026-10-16) it will not permit third-party AI agents or assistants to log into a customer's account or transact directly within its digital banking platforms — but customers may still authorize limited, *read-only* access to account data via certain open-banking providers. Bank of America CEO Brian Moynihan said it on BofA's Q3 earnings call (2026-10-14): "We feel very strongly that there should be a human involved in authorizing before money moves out of your account," and the limits stay until *liability* for AI-approved payments is settled. **What this reveals:** this is not one event but a *coordinated sector line* — the exact same split (agents may *read*, not *write*) that JPMorgan's Jamie Dimon drew the day before (2026-10-13 — see [[JPMorgan blocks outside AI agents from accessing accounts]]), that Charles Schwab's Rick Wurster confirmed the same day as Citi (2026-10-16, blocking "tens to twenties" of agent attempts/week, steering clients to its own read-only "Charley"), and that Wells Fargo scheduled to take effect 2026-11-24. The "liability" framing is real but also convenient cover for the deposit-economics motive below.

**[1] Competitors / peers (same wave).** The cohort as of mid-Oct 2026: JPMorgan (Dimon, 10-13), Bank of America (Moynihan, 10-14), Citi + Charles Schwab (10-16), Wells Fargo (effective 11-24). All converge on *read-only via connector, no autonomous money movement*. Schwab is the most operationally explicit (weekly block reports; MCP servers for partner LLMs giving read-only balance/research access only). The agents being walled out are the consumer frontier: Meta's **Muse** (topped app charts Sept 2026), OpenAI's **Dots**, and **Instinct** (Spear Street Technology, ~$10B valuation). **Position:** Citi/BofA are *catching up to / ratifying* the line Dimon set first; none is ahead on a distinct mechanism — the novelty is breadth (now 5 of the largest US banks aligned), not a new technical control. **Second-order:** once the #1 bank (JPM) set the precedent, the cost of *not* following rose (a bank that stayed open would invite exactly the deposit-sweep it fears), so this looks like fast tacit coordination — which also raises antitrust/consumer-access questions (analysis).

**[2] Company history / fit.** Citi and BofA sit on the asset being defended: cheap, "sticky," non-interest-bearing deposits. JPMorgan, BofA and Wells Fargo together hold ~$1.6tn in non-interest-bearing deposits; press math says paying ~3% on that pool would add ~$47bn/yr in cost and cut roughly half their combined annual earnings. BofA's own Q3-2026 results underpin why Moynihan is defensive about deposit funding. The fit is logical: these banks fund lending with ~0.1% checking balances; any tool that auto-sweeps idle cash into 3.3–5% neobank/brokerage yields (Revolut/SoFi/Wealthfront-type) attacks the core liability franchise. **Why act this way:** gating *write* access while allowing *read* lets them say "we support open banking / agentic connections" (regulatory optics, CFPB 1033 posture) while denying agents the one function — moving money — that would trigger deposit flight.

**[3] Novelty / value-add / traction.** Genuinely new vs. the JPM note: *new actors with distinct on-record positions* — Moynihan's explicit "human-in-the-loop before funds move" standard, Citi's FT confirmation, Schwab's concrete block volumes, Wells's dated effective rule. This is the "sector hardens" follow-on, not a reprint of the JPM call. **Traction is in the blocking, not a product:** Schwab is the only one quantifying (tens–twenties of agent attempts/week blocked); Citi/BofA give policy, not metrics. The defensive *product* analog (JPM's in-house Smart Cash sweep tool) is the real tell — banks want to *internalize* yield-optimization rather than let third-party agents capture it. **Who captures the margin:** if the line holds, banks keep cheap-deposit funding + any future *sanctioned/priced* agentic access (echoing the Plaid data-fee playbook); agents and connectors get read-only and must route money movement *around* bank rails (stablecoin/protocol layers — see [[Visa launches Trusted Agent Protocol for AI commerce]], [[OpenAI partners with Plaid to connect bank accounts in ChatGPT]], [[Oobit lets AI assistants pay with crypto and stablecoins]]).

**[4] What's next / market sentiment.** Expect the remaining top banks to fall in line (coordinated gatekeeping). Regulators have reportedly *welcomed* the restrictive stance but flag that legislation is still needed to define authorization + liability for AI-executed payments — i.e., no federal rule currently forces banks to grant agent *write*-access, and the CFPB's Section 1033 rewrite (fee ban reportedly being reversed, recipients narrowed) strengthens banks' hand to gate and price access. **Counterintuitive second-order:** the block is a durable moat *only while agents lack a non-bank money-movement rail*. If (a) a stablecoin/connector rail reaches enough reach to move funds without the bank's write-API, or (b) a future CFPB/court mandates consumer-authorized agent access, the deposit-beta cushion these banks are defending could re-rate fast. Watch: Wells's 11-24 effective date, whether liability legislation materializes, and whether agentic-commerce value migrates to Visa/stablecoin rails that bypass banks entirely. Related AI-risk plumbing forming around this: [[Harbor raises $10M seed to insure AI agent risks]], [[Incognia launches MCP Server for AI-driven fraud investigations]].

URLs:
- https://tradersunion.com/news/institutions/show/3849745-us-banks-limit-ai-agent-access/
- https://www.bloomberg.com/news/articles/2026-10-16/us-banks-block-ai-agents-attempting-to-move-money-for-customers
- https://finance.yahoo.com/technology/ai/articles/schwab-jpmorgan-block-unauthorized-ai-211121084.html
- https://thenextweb.com/news/schwab-blocks-ai-agents-meta-muse
- https://techstrong.ai/agentic-ai/u-s-banking-giants-block-ai-agents-over-security-rate-sweeping-threats/
- https://cellcog.ai/blog/us-banks-block-ai-agents/
- https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html
- https://www.cnbc.com/2026/09/28/apollo-raises-specter-of-an-ai-agentic-bank-run-hitting-financial-industry.html
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Is this a *new* event or a re-report of the JPMorgan ban ([[JPMorgan blocks outside AI agents from accessing accounts]])? Same wave, same read/write split — but *distinct new actors* (Citi FT statement 10-16; Moynihan on BofA's 10-14 call; Schwab 10-16; Wells effective 11-24) with their own on-record quotes. Verdict: fresh follow-on (sector hardens), not a duplicate reprint. Open: does the digest risk double-counting the theme across both notes?
2. "Restrict" vs. "restate": do Citi/BofA actually have *new* controls, or are they articulating pre-existing credential/anti-screen-scraping policy under media pressure? Likely largely articulation — flag novelty as *breadth of alignment*, not new tech.
3. Safety vs. commerce: is "human-in-the-loop / liability" the real driver, or cover for protecting ~$1.6tn cheap deposits? Both; the deposit-economics motive (~$47bn/yr cost, ~half of earnings) is the stronger structural one.
4. Scope: does the block cover *corporate/wealth* clients and OAuth open-banking tokens, or only retail credential logins? Sources emphasize retail + credential login; sanctioned-token path left open. Open.
5. Is the headline misleading? Read-only data still flows via connectors; only *money movement* is blocked. "Restrict AI agent access" overstates — it's a write-block, not an access-block.
6. Enforceability: can banks technically distinguish a well-behaved human-authorized agent token from credential stuffing? Schwab claims it blocks "tens–twenties/week" — but what's the false-negative rate? Open.
7. Liability-transfer / "human authorization" standard: is Moynihan's standard legally grounded (Reg E / UDAAP) or rhetorical pre-positioning ahead of legislation? Unsettled — regulators say law is still needed.
8. Deposit-flight magnitude: how large is the *realistically addressable* idle-deposit pool and how fast can agents move it given ACH limits/KYC/friction? The $47bn figure assumes full 3% repricing — a worst case, not a base case.
9. Coordination risk: 5 top banks aligning in 72h — tacit coordination or independent convergence? Either way, invites antitrust/CFPB/state open-banking scrutiny. Open.
10. Durability: with CFPB 1033 enjoined + rewrite reversing the fee ban, is "no timeline for agent write-access" an indefinite moat? Durable only while agents lack a non-bank money rail.
11. Disintermediation second-order: does blocking push agentic money-movement onto stablecoin/Visa Trusted Agent rails that bypass banks entirely — i.e., banks win deposits now but cede the agentic-payments layer? (analysis)
12. Does this contradict the banks' own agentic ambitions (internal agents, Smart Cash-type sweep tools)? They want to *internalize* yield-optimization, not kill agents — so the block is selective, not principled.
13. Source quality: Citi via a single FT statement; much of the rest is earnings-call quotes + aggregator rewrites. How much independent confirmation beyond the FT/Bloomberg originals? Moderate; primaries exist (FT, Bloomberg, CNBC) but the target note's own source (tradersunion) is a rewrite.
14. What breaks the thesis? A CFPB/court mandate for consumer-authorized agent access, or a connector/stablecoin rail reaching enough scale to move funds without a bank's write-API.

**Importance: 4/5** — The sector-wide hardening (Citi, BofA, Schwab, Wells joining JPM within 72h) turns one bank's stance into an industry line and is a defining moment for the agentic-finance / open-banking / deposit-flight fight. It adds genuinely new actors and on-record standards (Moynihan's human-authorization bar; Schwab's block metrics; Wells's dated rule) beyond the JPM note. Not 5 because it largely formalizes an existing posture with no new rule/timeline, and it overlaps heavily with [[JPMorgan blocks outside AI agents from accessing accounts]] (watch for digest double-counting); impact is directional/strategic, not a discrete transaction.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-19]] (2026-10-19).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a strategy/policy move on the economics of *account access* at the open-banking / agentic-commerce frontier — and the second domino: JPMorgan drew the same line 3 days earlier (2026-10-13), so by 2026-10-16 the top-3 US banks by deposits have converged on the same stance. Scale anchors (Q3-2026 results, 13 Oct 2026): Bank of America — net income $6.9bn (after a $1.2bn regulatory-settlement charge), revenue $30.0bn, deposits ~$2.0tn (+2% YoY) (per BofA Q3-2026 8-K/earnings, via Benzinga/Fool/SEC); Citigroup — net income $5.2bn, EPS $2.85, ROTCE 11.5%, revenue +8% YoY, average deposits ~$1.5tn (+11% YoY, Services-led) (per Citi Q3-2026 results, via Fool/Benzinga/Citi IR). "Why now" — three forces converged in weeks: (1) autonomous consumer agents went mainstream (Meta's **Muse** topped download charts Sept 2026; OpenAI's **Dots** followed; OpenAI's **Operator**/Instant-Checkout agentic-commerce stack is explicitly trained to *refuse* bank-account management today, per OpenAI — the gating is as much self-imposed as bank-imposed); (2) Apollo's **Torsten Slok** (27–28 Sep 2026, ~$1tn AUM) framed the systemic stake as an "agentic bank run" — agents auto-sweeping household cash from ~0.1% checking into 3.3–5.0% fintech yields, draining the *cheap deposits* banks fund loans with (per CoinDesk/OECD.AI); (3) regulation is a vacuum — regulators have *privately welcomed* the blocking, and say future legislation may be needed to clarify how customers authorize autonomous agents and *who bears liability* when a transaction goes wrong (per TradersUnion/gurufocus 2026-10-16). CFPB Section 1033 remains enjoined and under reconsideration, giving banks legal cover to gatekeep `(analysis)`.

**Competitive landscape.** Sector KPIs: deposit cost / deposit beta (cheap-deposit funding is the asset being defended), read-vs-write permission scope, and access-fee per aggregator call. Value chain splits three ways — bank (holds account + rails), aggregator/connector (Plaid, MX, Finicity = the "pipe"), agent (Muse/Dots/Operator = the app). Citi's wording mirrors JPM's almost verbatim: it will not permit "third-party AI agents or assistants to log into a customer's account or transact directly within our digital banking platforms," while still allowing customer-authorized *read-only* data access via certain open-banking providers (per Citi statement, via TradersUnion 2026-10-16). So the block is on *write* actions (move money, shift deposits to higher yields) — the exact function that makes an agent useful and the exact mechanism of Slok's bank-run thesis. Both banks explicitly cite **liability** as the stated rationale. Position: Citi and BofA are **following JPM's precedent** rather than setting it — as on the 2025 Plaid data-fee fight, #1 (JPM/Dimon) moved first and peers aligned within days; this is coordinated gatekeeping by the largest deposit holders. Moat = control of the rails + deposit scale `(analysis)`. Unlike JPM (which paired its block with the in-house **Smart Cash** yield-sweep pilot), no offsetting Citi/BofA consumer yield-tool is disclosed here — flag: who's silent about building the sanctioned path.

**Comps & multiples.** A policy move, not a round — no valuation attaches; deal multiples = n/a. Scale/precedent anchors:
- **Plaid** (the exposed "pipe"): last round ~$6.1bn (Apr 2025 secondary, down from $13.4bn in 2021). The direct template is the data-fee war now extended from *data* to *agents*; `[UNSOURCED]` revenue multiple.
- **Deposit scale of the three gatekeepers:** JPM (#1), BofA ~$2.0tn deposits, Citi ~$1.5tn average deposits — together they gate a large share of US retail/commercial cheap deposits, which is the structural leverage.
- Internal comps (base): [[JPMorgan blocks outside AI agents from accessing accounts]] (2026-10-13, near-identical move + liability-transfer framing — the direct precedent); [[Visa launches Trusted Agent Protocol for AI commerce]] and [[OpenAI partners with Plaid to connect bank accounts in ChatGPT]] — the agentic-access rails forming *around* banks; [[Mollie offers €50M equity to build banking for AI agents]] — the counter-bet that agent-native banking is a greenfield; [[Musk proposes shopping via credit card photos on Grok]] / [[Oobit lets AI assistants pay with crypto and stablecoins]] — non-bank agentic-payment rails. No ≥3 comparable multiples → distribution not computed, qualitative comparison only.

**Risk flags.**
1. **Liability vacuum / regulatory.** Both banks cite liability, and regulators admit no rule yet settles who is liable when a customer-authorized agent errs — so "secure agentic connections" with no timeline can stay indefinite. Second-order: banks set the pace of access to suit their own defensive products, not consumer demand, and the undefined liability is itself the justification for the moat.
2. **Deposit-flight defense = cheap-funding entrenchment.** Blocking write-actions neutralizes the Slok "agentic bank run" by denying agents the ability to move money, protecting Citi/BofA's low-cost deposit base. If a CFPB 1033 rewrite or consumer backlash later forces write-access open, the deposit-beta cushion they are defending could re-rate quickly.
3. **Coordinated gatekeeping / antitrust optics.** Three largest US banks converging on the same restriction within 3 days — with regulators "privately welcoming" it — hardens the whole deposit base against agents; a de-facto industry-wide lockout invites antitrust/consumer-choice scrutiny and state open-banking laws, and risks pushing agentic money-movement entirely onto non-bank (stablecoin/protocol) rails the banks don't control.

**What this changes (idea-lens).** `(analysis)` JPM was a signal; Citi + BofA make it a sector norm — the agentic-commerce stack is being forced to route *around* bank write-APIs (connectors + stablecoin/protocol rails) rather than through them. Falsifiable thesis: the block holds as a durable moat only while (a) CFPB 1033 stays enjoined/rewritten bank-favorably and (b) no non-bank rail reaches the scale to move funds without the banks' permission; it breaks if the 1033 rewrite mandates consumer agent-access or a stablecoin/connector rail achieves reach. Watch: whether a 4th/5th top bank copies within this earnings cycle, any disclosed liability-safe "sanctioned agent" timeline, and the OIRA 1033 output.

Sources: https://tradersunion.com/news/institutions/show/3849745-us-banks-limit-ai-agent-access · https://www.gurufocus.com/news/9128089/major-banks-limit-ai-access-to-customer-accounts-amid-concerns · https://www.fool.com/earnings/call-transcripts/2026/10/13/citi-c-q3-2026-earnings-call-transcript/ · https://www.benzinga.com/news/26/10/62333152/citigroup-q3-2026-earnings-call-complete-transcript · https://www.sec.gov/Archives/edgar/data/0000070858/000007085826000481/bac-09302026ex993.htm · https://www.coindesk.com/markets/2026/09/28/ai-agents-could-drain-cheap-bank-deposits-apollo-s-torsten-slok-warns · https://www.americanbanker.com/payments/news/openai-moves-ai-checkout-to-third-parties · https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
