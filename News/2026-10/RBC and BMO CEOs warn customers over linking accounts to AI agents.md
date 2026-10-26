---
title: "RBC and BMO CEOs warn customers over linking accounts to AI agents"
date: 2026-10-25
retrieved: 2026-10-25
tags:
  - company/rbc
  - company/bmo
  - industry/banking
  - industry/ai
  - region/canada
  - type/commentary
sources:
  - https://news.crunchbase.com/venture/q3-2026-fintech-startup-funding-deal-count-fell-ai
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s2a1750c7
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# RBC and BMO CEOs warn customers over linking accounts to AI agents

> [!info] 2026-10-25 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] The CEOs of Canada's RBC and BMO are the latest bank chiefs to warn customers about the dangers of linking their accounts to AI agents.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://news.crunchbase.com/venture/q3-2026-fintech-startup-funding-deal-count-fell-ai>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 3/5._

**[0] What exactly happened (de-PR'd).** Two of Canada's Big Five bank chiefs publicly warned retail customers not to hand their accounts over to third-party AI agents. **BMO CEO Darryl White** (speaking around the Toronto Global Forum, reported ~2026-10-21/22 by CBC) told Canadians never to give an AI agent their banking username/password, credit card numbers, SIN or PIN, warning the agents can't safeguard that data from bad actors, and that AI is advancing faster than regulation and safeguards. **RBC CEO Dave McKay** told Bloomberg (~2026-10-20) that RBC is *considering blocking* Meta's new **Muse** agent from accessing client account information — "You have to protect that consumer and then we're liable for that as an organization." RBC's head of AI **Bruce Ross** (to The Logic) said RBC won't let agents like Muse connect to its systems without sufficient safeguards, and flagged the open question of *who bears legal responsibility* when an agent acts for a customer and something goes wrong.

The de-PR'd read: this is **verbal/strategic positioning (commentary), not a product action or a rule**. No agent was technically blocked by RBC yet ("considering"/"weighs"); BMO's is a consumer-advisory. The substance is a **liability-shifting message** — the banks are pre-emptively telling customers that credential-sharing with an agent likely breaches the account agreement, which can void fraud reimbursement and leave the customer liable (money.ca). That is the same "liability transfer" framing Jamie Dimon used two weeks earlier. → Why framed this way: banks can't yet technically distinguish an authorized agent from a rogue one (see the Axios reporting), so the cheapest defensive lever is a public credential-sharing ban that moves the loss to the consumer and buys time.

**[1] Competitors / peers (who said the same, with dates).** This is the Canadian echo of a fast-moving US bank chorus, not a first mover:
- **JPMorgan / Jamie Dimon — 2026-10-13** (Q3 call): will not let outside agents (Muse, OpenAI's Dots, Instinct) act on accounts; "you don't want rogue agents… thousands of them"; explicit "liability transfer." See [[JPMorgan blocks outside AI agents from accessing accounts]].
- **Morgan Stanley, Bank of America, Citi, Wells Fargo — by 2026-10-22** (Axios): Morgan Stanley *blocking* third-party agents; others *restricting*; industry moving to read-only access. See [[This Week in Fin AI agents open new bank security threats]].
- RBC/BMO are therefore **~1–2 weeks behind** the US majors and saying essentially the same thing, with a Canadian consumer-protection/fraud-reimbursement twist (OSFI/FSB oversight pressure).
→ Why the lay of the land is this way: the trigger is common — Meta's Muse topping app charts (Sept 2026) and the "agentic bank run" deposit-flight fear (Apollo's Torsten Slok, 28 Sep) — so every large deposit-holder is reflexively gating the same vector. The second-order dynamic: a coordinated incumbent block across US+Canada hardens the whole North American deposit base against agents, which is exactly the outcome agentic-commerce builders (Visa/Mastercard/Google/OpenAI) are trying to route around.

**[2] Company history / fit.** RBC and BMO are #1 and (roughly) #4 of Canada's Big Five by assets; both have leaned hard into AI (RBC via Borealis AI; Bruce Ross is a senior AI lead). It fits logically: Canadian banking is a tight oligopoly with very sticky, low-cost retail deposits and a strong consumer-protection/fraud-reimbursement regime — exactly the deposit franchise most exposed if agents can auto-sweep cash or trigger unreimbursed fraud. → Why they act this way: as oligopolists with pricing power and no CFPB-1033-style open-access mandate forcing them open, the rational move is to gate first and negotiate the rules later; the "we're liable as an organization" line (McKay) is the structural tell — Canadian banks eat more fraud loss than a liability-shifted US model, so they have a sharper incentive to pre-empt credential-sharing.

**[3] Novelty / value-add / traction.** Low novelty, real signal. Novelty is **geographic, not conceptual** — the first on-record Canadian Big-Five warnings, naming Meta's Muse specifically as the thing RBC might block. There is **no traction to measure**: RBC has not actually blocked Muse (it "weighs"/"considers"); BMO issued advice, not a control. So "announced vs live" = this is still *announced/rhetorical*. The durable value-add is the explicit, public linkage **credential-sharing → breach of account agreement → loss of fraud reimbursement** (money.ca), which is the sharpest consumer-facing articulation of the liability question Ross raises. → Who captures the margin / what breaks it: banks hold the account + rails and, absent a Canadian open-banking mandate, can set the pace; the thesis breaks if (a) Canada's long-delayed open-banking/consumer-driven-banking framework lands with an access mandate, or (b) a non-bank rail (stablecoin/agent protocol) lets agents move money without the bank's write-API.

**[4] What's next / market sentiment.** Expect convergence on **read-only-by-default + credential-sharing bans**, with banks steering agents through sanctioned connectors (Plaid-style) while they build agent-authentication. Regulatory backdrop: the **FSB**, backed by Canada's **OSFI**, has urged lenders to tighten AI oversight — verify agents' identities and limit their exposure to sensitive data (per CBC/money.ca) — but there is still **no liability framework** for a user-authorized agent gone wrong, the exact gap Ross names. Counterintuitive second-order effect: the louder banks warn, the more they *accelerate* the agentic-commerce stack's incentive to build money-movement that bypasses bank rails entirely (Visa Trusted Agent Protocol, Google AP2, OpenAI/Anthropic agent checkout, stablecoin rails) — so blanket "no" risks disintermediation rather than control. Note the contrast with Russia, where [[Финтехно Russian banks to open accounts to third-party AI agents]] shows Tochka/T-Bank/Sber *opening* accounts to external agents via MCP (with signature still required to send money) — the opposite posture to the North American block.

**Sources:**
- https://www.cbc.ca/news/business/bmo-ai-warning-9.7390171
- https://money.ca/banking/bmo-ceo-warning-banking-info-ai-agents
- https://www.bloomberg.com/news/videos/2026-10-20/rbc-weighs-blocking-meta-s-ai-agent-muse-ceo-mckay-video
- https://thelogic.co/news/rbc-artificial-intelligence-meta-muse/
- https://www.finextra.com/newsarticle/48634/banks-move-to-limit-agents-access-to-customer-accounts
- https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html
- https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **Is this a new event or an echo?** Mostly an echo. Dimon said essentially the same thing on 2026-10-13; Morgan Stanley/BofA/Citi/Wells by 2026-10-22 (Axios). RBC/BMO are the *Canadian* restatement ~1–2 weeks later. Fresh as a distinct, newly-sourced statement, but low novelty.

2. **Did RBC actually block Muse?** No. McKay said RBC is *considering*/"weighs" blocking Meta's Muse — rhetoric, not a technical control. BMO issued consumer advice, not a block. "Announced," not "live."

3. **Commentary vs product action?** This is commentary/positioning (type/commentary). No API change, no rule, no disclosed timeline. Framing it as "banks block agents" over-reads it.

4. **What exactly did BMO's White warn against?** Handing an agent your username/password, credit-card details, SIN, PIN — i.e. credential-sharing — because agents can't protect that data from bad actors, and AI is outpacing safeguards. Specific and on record.

5. **Is the fraud-reimbursement claim real or scare framing?** Plausible and sourced (money.ca): credential-sharing can breach the account agreement, which banks may use to deny fraud reimbursement, shifting loss to the customer — the same "liability transfer" logic as Dimon. But whether a bank would actually deny a claim is untested; regulators/courts haven't ruled. — partly open.

6. **Who bears liability when a user-authorized agent errs?** Unresolved — Bruce Ross explicitly flags the gap; no Canadian (or US) liability framework exists. This is the real substantive question, and it's open.

7. **Is "rogue agents" an evidenced threat in Canada?** No confirmed Canadian losses cited. Axios documented no confirmed US losses either — the alarm is inability to distinguish authorized vs rogue agent traffic, not a breach wave. "Rogue" is rhetorically loaded.

8. **Could the security framing mask a commercial/deposit-defense motive?** Likely partly. The same block neutralizes the "agentic bank run" deposit-flight threat (Slok/Apollo) that would drain cheap Canadian deposits — so "protect the consumer" and "protect our funding" coincide. Banks are silent on the deposit-economics motive.

9. **Does read-only actually solve it?** It stops fund movement but not data profiling/exfiltration, and not agents escalating via call centers (Axios). Mitigation, not a fix.

10. **Can banks even technically enforce this?** Hard — they struggle to parse human vs authorized-agent vs rogue-agent traffic (Axios). A credential-sharing ban is enforceable mainly by denying liability after the fact, not by real-time blocking.

11. **Is there an agent-auth standard banks could use instead of blocking?** Not for bank-account access. Commerce has Visa TAP, Google AP2, Mastercard Agent Pay; account-access has no equivalent — hence blunt bans. This gap is the actual story.

12. **Why Canada specifically / why now?** Big-Five oligopoly, sticky low-cost deposits, strong consumer fraud-reimbursement norms, and no open-banking access mandate yet → strong incentive + legal room to gate first. Trigger = Meta Muse (Sept 2026) + the US bank chorus.

13. **Regulatory tailwind or headwind?** Tailwind for the banks: FSB (backed by OSFI) urged lenders to tighten AI oversight, verify agent identity, limit data exposure. No rule forces banks open — so "we support secure agentic access" can be indefinite.

14. **Does this contradict the global direction?** Yes, regionally. [[Финтехно Russian banks to open accounts to third-party AI agents]] shows Tochka/T-Bank/Sber *opening* accounts to external agents via MCP (signature still required to send money). North America blocks; Russia opens. Divergent regulatory/market regimes.

15. **Net reliability / weight.** Statements are solidly sourced (CBC, Bloomberg, The Logic, money.ca, Finextra) and correctly attributed. But it's commentary echoing a two-week-old US stance, with no action, no losses, no rule — directional signal, not a scoop.

**Importance: 3/5** — Canada's two of the largest banks publicly joining the agent-account-access gatekeeping chorus is a genuine, correctly-sourced data point that the "banks say no to agentic account access" posture is now cross-border (US + Canada), and it sharpens the consumer-liability/fraud-reimbursement angle better than most. Capped at 3 because it is commentary (no block executed, no rule, no timeline, no confirmed losses) that largely restates the JPMorgan/Axios cluster ([[JPMorgan blocks outside AI agents from accessing accounts]], [[This Week in Fin AI agents open new bank security threats]]) from ~1–2 weeks earlier.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-26]] (2026-10-26).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits at the collision of agentic commerce and open banking / account-data access. Market sizing is for the agentic layer itself, not these banks: Juniper Research puts agentic commerce at ~$1.5tn in global transaction value by 2030; McKinsey frames $3–5tn in orchestrated revenue by end-decade; IDC is far more conservative at $18.4bn (2025) → $187bn (2030) (per Juniper/McKinsey/IDC, via secondary citations, as of 2026 — treat the trillions as TAM boosterism, the IDC path as the base case). Structure: the retail-banking side is consolidated oligopoly (RBC + BMO = ~2 of Canada's Big Six; the US cohort below is the top tier by deposits), with high regulatory + trust barriers; the agent/aggregation side is fragmented and racing to standardize. "Why now": consumer agents hit retail scale fast — Meta's Muse reported >10m downloads ~1 month post-launch (per The Logic, 2026-10) — forcing banks to rule on access before a fraud incident sets precedent. The unresolved primitive is liability allocation: when an agent moves money and it goes wrong, who pays — customer, agent vendor, merchant, or bank? McKay's framing: "we're liable for that as an organization," so banks will not cede the authorization step (per Bloomberg, 2026-10-20).

**Competitive landscape.** This is not a company deal but a sector-wide posture shift. The relevant axis is *who controls the authorization/authentication layer*. Key moves, all 2026-10: BMO CEO Darryl White — don't share username/password, card, SIN or PIN with agents ("these are not protected," i.e. sharing credentials voids fraud-loss protection); RBC's Dave McKay weighing blocking Meta's Muse, AI chief Bruce Ross saying Muse won't connect without safeguards; in the US, JPMorgan (Dimon's "rogue agents… liability transfer" on the Q3 call), Citi, Bank of America (Moynihan wants a human to approve money leaving accounts), Wells Fargo, Morgan Stanley and Charles Schwab all restricting third-party agents (per Finextra/PYMNTS/Axios, 2026-10). The emerging compromise is *view-only via sanctioned rails* (e.g. Plaid/open-banking providers) while blocking fund movement and direct credential login / screen-scraping. Basis of competition shifts from product to trusted-rails gatekeeping + agent-identity: API consent converts ~81% vs ~50% for scraping (per secondary citation), so banks have both a security and a UX reason to force agents onto permissioned APIs they police. RBC/BMO position: fast followers of the US majors, not first movers — the Canadian Big Six's concentration lets them coordinate a near-industry-wide default of "no autonomous agent access."

**Comps & multiples.** No valuation, round or deal in this item (it is CEO commentary), so no trading multiple applies — distribution not computed, qualitative comparison only. Internal comps from the base show this is one beat in a dense 2026-10 cluster of the same debate and the counter-build of sanctioned agent rails: [[Citi and Bank of America restrict AI agent access to accounts]], [[JPMorgan blocks outside AI agents from accessing accounts]] (the policy comps on the bank side); and on the infrastructure/offense side [[American Express publishes Intent Intelligence agentic commerce framework]], [[Mastercard opens Agent Pay for Machines early access]], [[Visa, BILL and Billtrust pilot trusted AI agent payments]], [[Backbase launches Conversational Banking for agentic AI]]. Read together: incumbents block *unsanctioned* access while networks (Visa/MA/Amex) race to supply the *sanctioned* agent-payment rails — the economics of the agentic layer are being captured by the rail owners, not the deposit holders.

**Risk flags.**
1. Liability ambiguity (regulatory/legal) — no settled rule on who eats losses when an agent misacts; until regulators or a landmark case decide, every bank sets its own policy, and a single large agent-driven fraud could force rushed, costly rules. Why it matters: unresolved liability is the real reason for the blanket "no," not UX.
2. Disintermediation of the bank relationship — if consumer agents (Muse, and future OpenAI/Google equivalents) become the front door to money movement, banks risk sliding to a dumb-pipe deposit utility while networks/agent vendors own the intent and the take-rate. Blocking buys time but doesn't solve the demand.
3. Credential-sharing / screen-scraping fraud (security) — millions already hand passwords to agents; the warning is an admission that fraud-loss protection is being voided at scale, shifting loss onto consumers and reputational/regulatory risk onto banks.

**What this changes (idea-lens).** This is the opening of a standards fight, not a one-off warning: expect convergence on bank-sanctioned, read-only-then-permissioned agent APIs with explicit liability terms, with networks (Visa/Mastercard/Amex) positioned to own the authenticated agent-payment rail (analysis). Falsifiable thesis: within ~6–12 months the major banks move from blanket blocking to a *tokenized agent-access standard* (agent identity + scoped permissions + liability waiver) rather than outright bans. Trigger/catalyst to watch: whether RBC actually blocks Muse (a real block = banks still choosing walls over rails), a regulator (OSFI/CFPB/Section 1033-style open-banking rule) assigning agent-transaction liability, or a network signing a bank to a sanctioned agent-pay pilot. What breaks the thesis: a high-profile agent fraud loss that hardens blocking into permanent policy.

Sources: https://www.bloomberg.com/news/videos/2026-10-20/rbc-weighs-blocking-meta-s-ai-agent-muse-ceo-mckay-video · https://thelogic.co/news/rbc-artificial-intelligence-meta-muse/ · https://www.cbc.ca/news/business/bmo-ai-warning-9.7390171 · https://www.finextra.com/newsarticle/48634/banks-move-to-limit-agents-access-to-customer-accounts · https://www.pymnts.com/news/banking/2026/banks-crack-down-on-unauthorized-ai-agents-operating-inside-customer-accounts/ · https://www.juniperresearch.com/press/agentic-commerce-set-to-generate-15-trillion-globally-by-2030-as-payments-infrastructure-leaders-revealed/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
