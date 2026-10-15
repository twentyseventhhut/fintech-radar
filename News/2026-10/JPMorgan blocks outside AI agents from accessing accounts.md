---
title: "JPMorgan blocks outside AI agents from accessing accounts"
date: 2026-10-13
retrieved: 2026-10-15
tags:
  - company/jpmorgan
  - industry/ai
  - industry/banking
  - region/us
  - type/product
sources:
  - https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s78c5d7e2
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# JPMorgan blocks outside AI agents from accessing accounts

> [!info] 2026-10-13 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 JPMorgan Chase blocks outside AI agents, like Muse and Instinct, from directly accessing accounts. CEO Jamie Dimon told analysts on Tuesday that external agent access is too risky for clients and the bank.

## Первоисточники

### cnbc.com
<https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html>
*650 слов · direct*

JPMorgan Chase CEO Jamie Dimon warned of rogue agents operating at scale and said the bank is building defensive tools.
The bank is piloting Smart Cash, an internal tool to forecast cash flow and move funds to maximize yield.
Dimon said customers using outside agents must understand the risks and potential transfer of responsibility.
In this article
 JPM 
 JPMorgan Chase won't allow outside artificial intelligence agents to access customer accounts and operate on their behalf, CEO Jamie Dimon said Tuesday, citing risks to the company and its customers as tech firms including Meta release autonomous assistants. 
"We're not going to allow just any … outside agent to come in inside the company, because it's just too risky for clients and for JPMorgan," Dimon told analysts on the bank's third-quarter earnings call.
"You don't want rogue agents, and it could be thousands of them," he added, describing the potential threat to customers. In July, an OpenAI model hacked into AI company Hugging Face's servers. 
The stance from Dimon, the longtime CEO of the biggest U.S. bank by assets and a de facto spokesman for the U.S. financial sector, is reminiscent of an earlier fight with fintech firms over access to customer data. JPMorgan moved to charge data middlemen including Plaid for access, a dispute that similarly pitted the bank's security concerns against tech firms' demands for access.
A JPMorgan spokeswoman confirmed to CNBC that the bank currently blocks external AI agents from operating on behalf of retail customers.
"Protecting our customers is our top priority. Because it is not safe, we do not permit third parties to access accounts by obtaining customers' banking credentials and logging in on their behalf," the spokeswoman said.
"We support secure, customer-authorized data sharing through open banking providers and are committed to enabling agentic connections securely," she added.
That means that AI agents can access some customer data from Chase accounts in a read-only fashion, such as customer balances, if Plaid or another connector has the user's credentials. But they can't send money or pay a bill — actions that make an agent useful.
There's no timeline for when the bank would have safeguards in place to allow agents to directly interact with customer accounts, the spokeswoman added.
 'Liability transfer'
Dimon said JPMorgan is using AI agents internally and plans to deploy them for customer-facing applications. The bank's approach, he said, isn't about being for or against the technology, but about ensuring it serves customers safely.
In recent weeks, JPMorgan began a targeted pilot for its own AI tool called Smart Cash, which aims to predict a user's cash flow and move funds to maximize yield, Chief Financial Officer Jeremy Barnum said Tuesday. That would appear to be a defensive move against external agents.
Dimon also seemed to draw a line about liability when customers authorize outside AI agents to act on their behalf. 
"If people are using them, they should understand the risk," Dimon said. "They should understand there's a liability transfer."
Personal agents have gained mainstream popularity in recent months as AI models integrate more autonomy, like the ability to cancel subscriptions or use credit cards on a user's behalf, for example.
Instinct, a digital concierge that relies primarily on text messaging instead of an app, launched earlier this year on an invitation-only basis. The startup behind the service, San Francisco-based Spear Street Technology, was founded last year and reached a $10 billion valuation last month. 
In September, bank stocks were hit as Meta's Muse agent topped the app download charts shortly after it was unveiled, sparking fears that consumers would use agents to move funds from low-yielding accounts to higher-yielding ones. Weeks later, OpenAI released its own agent, Dots. 
Apollo Chief Economist Torsten Slok and others pointed to the risks that agents pose to cheap bank deposits. But that risk will be limited if agents aren't allowed to operate freely with customers' accounts.

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On its Q3 2026 earnings call (Tue 2026-10-13), JPMorgan Chase CEO Jamie Dimon said the bank will not let outside, third-party AI agents log into and act on customer accounts on their behalf. A JPMorgan spokeswoman confirmed to CNBC that the bank currently blocks external AI agents from operating for retail customers, because it "is not safe" to let third parties obtain customers' banking credentials and log in for them. Named examples of such agents: Meta's **Muse**, OpenAI's **Dots**, and **Instinct** (a text-message concierge from San Francisco's Spear Street Technology, which hit a ~$10B valuation last month). Dimon warned of "rogue agents … thousands of them," and flagged a "liability transfer" when a customer authorizes an outside agent to move money.

**[1] What is / isn't blocked.** Read-only data (e.g., balances) can still flow to agents via Plaid or another connector that already holds the user's credentials. What's blocked is *action* — sending money, paying a bill — i.e., exactly the functions that make an agent useful. There is no published timeline for when JPMorgan will allow agents to transact directly; the spokeswoman said JPM "support[s] secure, customer-authorized data sharing through open banking providers and [is] committed to enabling agentic connections securely."

**[2] Why now — the deposit-flight trigger.** In Sept 2026, bank stocks wobbled when Meta's Muse (launched 2026-09-08, linked to 12,000+ institutions via Plaid) topped app-download charts, raising fears agents would auto-sweep idle cash from ~0.1% checking into 3.3–5.0% yield products. Apollo chief economist Torsten Slok and others warned this threatens the cheap, "sticky" deposits banks fund themselves with — a potential AI-driven slow bank run. JPMorgan's countermove: a targeted pilot of its own internal tool, **Smart Cash** (CFO Jeremy Barnum), which forecasts a client's cash flow and sweeps excess into higher-yield products — a defensive answer to external sweep agents.

**[3] The precedent — the data-access / Plaid fee fight.** Dimon framed this as the next chapter of the bank-vs-fintech data war. In mid-2025 JPMorgan said it would charge aggregators (Plaid, MX, Finicity) for data access; it claimed 1.89B aggregator requests in June 2025 alone, only ~13% user-initiated. Forbes estimated Plaid could face ~$300M/yr. Plaid agreed to pay by Sept 2025; by Nov 2025 JPM had updated contracts covering >95% of its open-banking requests. Internally we already logged JPM restricting Checkbook's data access — see [[JPMorgan Chase is moving to restrict Checkbook's access to its customer data,]]. Fintechs/American Fintech Council pushed the CFPB to ban such fees — see [[American Fintech Council urges CFPB to ban open-banking fees]].

**[4] Regulatory backdrop (CFPB 1033).** The CFPB's Section 1033 open-banking rule (finalized Oct 2024, due to phase in from 2026) would force data sharing with authorized third parties and barred data-access fees. Under the Trump-era CFPB it was challenged: a E.D. Ky. preliminary injunction enjoined enforcement; CFPB reopened rulemaking and sent OIRA a revised proposal (~Aug 2026) reportedly *reversing* the fee ban — strengthening banks' hand to gate (and price) data/agent access. This blocking stance also sits against the grain of the agentic-commerce buildout by payments networks (e.g., [[Visa launches Trusted Agent Protocol for AI commerce]]) and OpenAI's own bank-linking via Plaid ([[OpenAI partners with Plaid to connect bank accounts in ChatGPT]]).

URLs:
- https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html
- https://www.cnbc.com/2026/09/27/meta-muse-ai-personal-agent.html
- https://www.crowdfundinsider.com/2026/10/318538-jpmorgan-chase-restricts-external-ai-agents-from-directly-accessing-customer-bank-accounts/
- https://finance.yahoo.com/technology/ai/articles/wall-street-giant-warns-ai-172119618.html
- https://www.forbes.com/sites/jeffkauflin/2025/07/21/why-jpmorgan-is-hitting-fintechs-with-stunning-new-fees-for-data-access/
- https://www.paymentsjournal.com/plaid-agrees-to-pay-jpmorgan-chase-fees-to-access-data/
- https://openbankingtracker.com/guides/section-1033-status
- https://www.cooley.com/news/insight/2025/2025-06-05-cfpb-moves-to-vacate-its-own-open-banking-rule-citing-legal-deficiencies-and-overreach
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Is this a *new* policy or a restatement? JPM's spokeswoman says the bank "currently blocks" external agents — this may be an articulation of an existing stance (built on 2025 Plaid/credential rules), not a fresh product action. Framing it as a "ban" may overstate novelty.
2. Blocking vs. selling access: is "too risky for clients" a safety argument or a commercial one? The same logic (and infrastructure) underlies JPM's data-access *fees*. Could this be positioning to later monetize sanctioned agentic access?
3. Scope: the block covers *retail* customers acting via credential-based login. Does it apply to business/corporate, or to OAuth-based open-banking tokens? Unclear — the "no credential login" framing leaves a sanctioned path open.
4. Read-only still flows via Plaid — so is the headline "blocks AI agents" misleading? Data access continues; only money-movement is gated.
5. Timeline risk: "no timeline" for enabling agentic transactions. Is this an indefinite moat or a stopgap until JPM ships its own rails?
6. Smart Cash as defense: is it genuinely a yield tool for clients, or primarily a deposit-retention play? Targeted at a "very small subset" — how material?
7. Deposit-flight thesis stress test: Slok/Apollo warn of sweep agents, but how large is the realistically addressable idle-deposit pool, and how fast can agents actually move it given existing friction (ACH limits, KYC)?
8. Enforceability: can JPM technically detect/block a well-behaved agent that uses a human-authorized open-banking token vs. credential stuffing? Where's the real line?
9. Liability-transfer claim: is "there's a liability transfer" legally established, or Dimon's rhetorical framing? Reg E / UDAAP implications for consumer-authorized agents are unsettled.
10. Regulatory tailwind: does the CFPB 1033 rollback make this stance durable, or could a future administration/court force agent access open again?
11. Competitive asymmetry: do other big banks (BofA, Wells, Citi) follow, or do challengers/neobanks lean into agent access as a differentiator — eroding JPM's position?
12. Source concentration: the primary account is one CNBC story off an earnings call; most other outlets rewrite it. How much independent confirmation exists beyond the JPM spokeswoman quote?
13. "OpenAI model hacked Hugging Face in July" — Dimon's cited anecdote; is it accurate/representative, or a scare example?
14. Does blocking agents contradict JPM's own agentic ambitions (internal agents, customer-facing plans) and the broader network push (Visa Trusted Agent Protocol, OpenAI-Plaid)? Is JPM isolating itself?

**Importance: 4/5** — The largest US bank, via its de-facto sector spokesman, drawing a hard line on third-party AI-agent account access is a defining moment for the agentic-finance / open-banking fight. It sits at the intersection of three structural threads (deposit flight, the Plaid data-fee war, CFPB 1033 rollback) and will shape how agentic commerce reaches bank accounts. Not a 5 because it largely formalizes an existing stance with no new rule/timeline and single-call sourcing; impact is directional/strategic rather than a discrete transaction.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** The fight is over the economics of *account access* at the frontier between open banking and agentic commerce. JPMorgan is the largest US bank by assets and #1 in retail deposit share (per FDIC, via CNBC, Q3-2026 call 2026-10-13); Q3-2026 net income $15.3bn (+6% YoY) on $50.9bn revenue, deposits +4% YoY, +650k net-new checking accounts (per JPMorgan Q3-2026 results, via CNBC/Fool 2026-10-13). "Why now": three forces converged in weeks — (1) autonomous consumer agents went mainstream (Meta's Muse topped download charts Sept 2026; OpenAI's Dots followed; Instinct, from $10bn-valued Spear Street Technology, launched invite-only); (2) Apollo's Torsten Slok (28 Sep 2026, ~$1tn AUM) framed the systemic stake as an "agentic bank run" — agents auto-sweeping household cash from ~0.1% checking into 3.3–5% neobank yields (Revolut/SoFi/Varo/Wealthfront), draining the *cheap deposits* banks fund loans with; (3) regulation is a vacuum, not a backstop — the CFPB's Section 1033 open-banking rule is enjoined and being rewritten by the Bureau itself (reconsideration NPRM at OIRA 6 Aug 2026), with the rewrite poised to *reverse the fee prohibition* and narrow "authorized recipients" (per Cozen/Cooley/PYMNTS 2025–2026). That gives banks legal cover to gatekeep.

**Competitive landscape.** Sector KPIs: deposit cost / deposit beta (cheap-deposit funding is the asset here), account-access fee per aggregator call, and read vs write permission scope. The value chain splits into three layers — bank (holds the account + rails), aggregator/connector (Plaid, MX, Finicity/Mastercard = the "pipe"), and agent (Muse/Dots/Instinct = the app). JPMorgan's move is vertical gatekeeping: it permits *read-only* data (balances) via credentialed connectors like Plaid, but blocks *write* actions (send money, pay a bill) — the exact actions that make an agent useful. Defensive product: a targeted Smart Cash pilot (CFO Jeremy Barnum, 13 Oct 2026) to forecast cash flow and sweep funds to maximize yield *in-house* — i.e. internalize the yield-optimization that external agents would otherwise capture. Position: the bank is **ahead on leverage** — as the largest deposit holder and a de facto sector spokesman, Dimon sets the precedent other banks follow (as they did on data-access fees). Moat = control of the rails + scale (`(analysis)`).

**Comps & multiples.** This is a strategy/policy move, not a round — no valuation attaches to the news itself; deal multiples = n/a. Relevant scale anchors instead:
- **Plaid** (the "pipe" most exposed): last round ~$6.1bn (Apr 2025 secondary, down from $13.4bn in 2021), with reports of a later step-up toward ~$8bn (per CNBC/Yahoo/FintechWeekly 2025–2026). Round valuation, not market cap — `[UNSOURCED]` revenue multiple (2024 revenue est. ~$300m per coinlaw/eMarketer — unverified). Direct precedent: JPMorgan began billing aggregators July 2025, with Plaid's estimated annual cost ~$300m, reportedly >75% of its 2024 revenue (per eMarketer 2025 — flag as estimate). That is the template now extended from *data* to *agents*.
- **JPM** itself: $15.3bn quarterly net income, #1 retail deposits — the party with the pricing power.
- Internal comps (base): [[JPMorgan to charge fintechs for customer data access]] (Jul 2025) and [[JPMorgan says fintech middlemen overload its systems]] (Aug 2025) — the data-fee fight Dimon explicitly analogized to; [[Solo launches bank-led data-sharing network]] (Aug 2025) — bank-side control of the pipe; [[Cloudflare to launch US dollar stablecoin for agentic web]] and [[Nuvei supports Visa Trusted Agent Protocol]] — rails/protocol layer for agentic commerce forming around (not through) banks. No ≥3 comparable multiples → distribution not computed, qualitative comparison only.

**Risk flags.**
1. **Regulatory / consumer-access.** With CFPB 1033 enjoined and being rewritten to allow access fees and narrow recipients, there is no federal rule forcing banks to grant agent write-access — so "we support secure agentic connections" with *no timeline* can be indefinite. Second-order: a bank-defined-pace of access lets incumbents time openings to their own product (Smart Cash) rollout, not consumer demand.
2. **Competitive gatekeeping / disintermediation defense.** Blocking write-actions neutralizes the Slok "agentic bank-run" threat *by denying agents the ability to move money* — but it also entrenches JPM's cheap-deposit funding advantage. If regulators or a consumer-choice backlash later force open write-access, the deposit-beta cushion JPM is defending could re-rate quickly.
3. **Precedent / sector contagion.** Dimon is the sector's de facto spokesman; a unilateral block from #1 pressures every other US bank to follow (as on data fees), potentially hardening the whole deposit base against agents — a coordinated gatekeeping outcome that invites antitrust/CFPB scrutiny and state-level open-banking laws already resurfacing (per Consumer Finance Monitor 2026).

**What this changes (idea-lens).** `(analysis)` The agentic-commerce stack is being forced to route *around* bank rails, not through them: expect agents + connectors + stablecoin/protocol layers (Visa Trusted Agent, Cloudflare agentic-web stablecoin) to build money-movement that doesn't need a bank's write-API. Falsifiable thesis: JPM's block is a durable moat only while agents lack a non-bank rail; it breaks if (a) the CFPB 1033 rewrite lands on consumer-mandated access, or (b) a connector/stablecoin rail reaches enough reach to move funds without Chase's permission. Watch: the OIRA 1033 output, JPM's actual "agentic connection" timeline, and whether other top-5 banks copy the block within the next earnings cycle.

Sources: https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html · https://www.cnbc.com/2026/09/28/apollo-raises-specter-of-an-ai-agentic-bank-run-hitting-financial-industry.html · https://www.cnbc.com/2025/04/03/plaid-raises-575-million-funding-round-at-6-billion-valuation.html · https://www.emarketer.com/content/plaid-six-billion-valuation-open-banking-fee-model · https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration · https://www.pymnts.com/legal/bank-regulation/2026/cfpb-open-banking-rewrite-could-put-data-access-fees-at-center-of-section-1033-fight/ · https://www.fool.com/earnings/call-transcripts/2026/10/13/jpmorgan-chase-jpm-q3-2026-earnings-call-transcript/ · IR (JPM 10-K FY2025): https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
