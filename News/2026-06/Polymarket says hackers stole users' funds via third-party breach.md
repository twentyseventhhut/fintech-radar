---
title: "Polymarket says hackers stole users' funds via third-party breach"
date: 2026-06-25
retrieved: 2026-06-26
tags:
  - company/polymarket
  - industry/crypto
  - industry/trading
  - region/us
  - type/outage-security
sources:
  - https://link.techcrunch.com/click/46320801.47777/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA2LzI1L3BvbHltYXJrZXQtc2F5cy1oYWNrZXJzLXN0b2xlLXVzZXJzLWZ1bmRzP3V0bV9jYW1wYWlnbj1kYWlseV9wbQ/6a347703be04c47cab07526aB4a5a6990
status: published
n_mentions: 1
channels:
  - "TechCrunch"
story_id: sdbbafe04
month: 2026-06
enriched: true
importance: 3
---

# Polymarket says hackers stole users' funds via third-party breach

> [!info] 2026-06-25 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: TechCrunch

## Агрегированный текст (из дайджестов)

[TechCrunch] Polymarket says hackers stole users' funds: The prediction market giant Polymarket said it's refunding users who had funds stolen due to a third-party breach. Read More

## Первоисточники

### link.techcrunch.com
<https://link.techcrunch.com/click/46320801.47777/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA2LzI1L3BvbHltYXJrZXQtc2F5cy1oYWNrZXJzLXN0b2xlLXVzZXJzLWZ1bmRzP3V0bV9jYW1wYWlnbj1kYWlseV9wbQ/6a347703be04c47cab07526aB4a5a6990>
*420 слов · direct*

The first StrictlyVC of 2026 hits SF on April 30. Tickets are going fast. Register now. 
 Founder Summit ticket savings of up to $190 end June 26. Join 1,000+ founders and VCs for all-day bootcamp. REGISTER NOW. 
Posted:

 
 
 Lorenzo Franceschi-Bicchierai 
Polymarket says hackers stole users’ funds
Prediction market giant Polymarket confirmed that hackers stole funds from an unspecified number of users after a third-party breach.
 In an X post on Thursday , Polymarket said that a compromise at a third-party vendor allowed hackers to inject malicious code into its website “for some users.” The company said it has “contained” the incident and is now contacting the affected victims and “refunding them in full.”
As of Thursday afternoon, it’s unclear exactly what happened. 
When reached by TechCrunch, Polymarket spokesperson Connor Brandi confirmed that the breach led to users’ funds being stolen but declined to provide more information, and did not respond to specific questions about the incident.
Around the same time as the Polymarket post, blockchain monitoring firm PeckShield reported on X that a phishing campaign was targeting Polymarket users. According to PeckShield, hackers had stolen around $3 million worth of cryptocurrency. 
A blockchain analyst also reported similar losses and claimed that the funds were stolen from more than 11 victims. 
Polymarket offers users the possibility of being paid in cryptocurrency. 
In the last couple of days, two people on social media claimed to have had their Polymarket funds stolen.
The hack is the latest blow for a company that has been in the headlines for the wrong reasons this week. On Sunday, an investigation revealed that Polymarket had paid online creators to post deceptive videos showing they won lucrative bets that were actually fake. In response, the company said it would audit its promotional content.

Topics
 Last chance to save up to $190 on TechCrunch Founder Summit. Join 1,000+ founders and VCs at all stages for real-world scaling insights and connections that move the needle. Savings end June 26, 11:59 p.m. PT .
Newsletters
Subscribe for the industry’s biggest tech news
Related

 

 
 

 
 
 

 
 
 
 
 Security 
 
 
 

 
 Hacked Klue says criminals are deleting stolen customer data, but now other hackers are making threats 
 
 
 
 
 
 Lorenzo Franceschi-Bicchierai 

 

 
 

 
 
 

 
 
 
 
 Apps 
 
 
 

 
 Facebook rolls out an AI companion app for creators 
 
 
 
 
 
 Aisha Malik 
Latest in Security

 

 
 

 
 
 

 
 
 
 
 In Brief 
 
 
 

 
 
 
 Polymarket says hackers stole users’ funds 
 
 
 
 
 
 Lorenzo Franceschi-Bicchierai 

 

 
 

 
 
 

 
 
 
 
 Security 
 
 
 

 
 Hacked Klue says criminals are deleting stolen customer data, but now other hackers are making threats 
 
 
 
 
 
 Lorenzo Franceschi-Bicchierai 

 

 
 

 
 
 

 
 
 
 
 Security 
 
 
 

 
 Cellebrite said it cut off Russia, but Russia used its tools anyway 
 
 
 
 
 
 Lorenzo Franceschi-Bicchierai

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Polymarket says hackers stole users' funds via third-party breach
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **2026-06-25** Polymarket disclosed (via an X post, not a formal incident report) that a **compromised third-party vendor injected a malicious script into its website frontend "for some users."** This is a **supply-chain / frontend attack, not a smart-contract or core-infrastructure exploit** — Polymarket's contracts and backend were untouched; the attack worked by tricking users who loaded the poisoned frontend into **signing/approving fraudulent transactions** from their connected wallets.
- **Scale:** ~**$2.9–3.0M** stolen (PeckShield: ~$3M; crypto.news: ~$2.94M) from a **small number of victims — "11+" / "fewer than 15" wallets.** Funds were held in PUSD/USDC, drained, **bridged from Polygon to Ethereum and swapped to ~1,893 ETH**, consolidated into one attacker address (classic launder pattern).
- **Response:** "contained" the incident, "removed the affected dependency," is "contacting impacted users & **refunding them in full.**" No vendor named, no victim count, no formal post-mortem.
- **De-PR read:** The framing — "third-party breach," "contained," "full refunds" — is **liability-deflecting**: it puts the root cause on a vendor and the small dollar figure makes full reimbursement cheap PR insurance. But the **central question isn't the $3M** (trivial for a company that raised $2B from ICE at a $9B valuation — see [[Polymarket raises $2B from ICE at $9B valuation]]). It's that **a regulated-exchange aspirant shipped unaudited third-party JS that could rewrite transaction prompts for live users** — a frontend supply-chain hole, the same class as the recent [[Hyperbridge processes first fund recovery after hack]] and [[CoinDCX reports $44M theft from operational account]] events. (analysis)

## [1] Competitors / peers
- **Direct prediction-market rival [[Kalshi to require employer disclosures before sensitive trades]]:** Kalshi is the CFTC-regulated, fiat-rails incumbent. Crucially, **Kalshi's custodial/fiat model has no "connect-your-wallet-and-sign" frontend** — so this exact attack vector (malicious JS reaching a self-custody signing flow) **does not exist for Kalshi.** The breach therefore widens, not narrows, the regulatory-trust gap right as both fight for the same US users (see [[Over $5 billion bet on World Cup across Polymarket and Kalshi]]).
- **Exchange/crypto peers:** [[CoinDCX reports $44M theft from operational account]] (treasury covered loss) and [[Hyperbridge processes first fund recovery after hack]] are the playbook: absorb the loss, reimburse, move on. **Why the lay of the land is this way:** for crypto venues, **reimbursement is cheaper than churn**; a few million in refunds buys "your funds are safe" credibility. The second-order point — frontend/supply-chain attacks (poisoned npm-style dependency, injected JS) are now the **dominant** attack surface vs contract bugs, because contracts get audited and frontends don't. (analysis)

## [2] Company history / fit
Polymarket's trajectory is a **regulatory-legitimacy sprint**: $200M at $1B ([[Polymarket nears $200M raise at $1 billion valuation]], Founders Fund) → **$2B from ICE at $9B** ([[Polymarket raises $2B from ICE at $9B valuation]]) → **CFTC application for a US crypto exchange** ([[Polymarket seeks CFTC approval for US crypto exchange]]) → native-USDC settlement with Circle ([[Circle and Polymarket partner to shift to native USDC]]) → distribution land-grab ([[Polymarket integrates with Bitget Wallet's 90 million users]]). **Why this matters:** every one of these moves **expands the self-custody, wallet-connected attack surface** (more integrations, more frontends, more dependencies) at exactly the moment the company is trying to convince the **CFTC and ICE** it is institution-grade. A frontend supply-chain breach is the **structural cost of the growth-via-integration model.** (analysis)

## [3] Novelty / value-add / traction
Nothing novel in the **attack** — frontend supply-chain compromises are well-trodden. The notable signal is **frequency and timing**: this is reportedly Polymarket's **second incident in ~a month** (≈late-May: a compromised internal operations key drained ~$600K from the UMA CTF Adapter contract on Polygon; user funds said to be safe, permissions revoked). DefiLlama reportedly logged this as the **89th crypto breach of Q2 2026 — the highest quarterly count on record.** Traction read: **full, fast reimbursement is the real value-add to users** and likely contains reputational damage given the small dollar size — **but two breaches in a month points to a process/op-sec deficit, not bad luck.** Who captures the cost: Polymarket eats ~$3M; the durable cost is **trust with regulators**, not the cash. (analysis)

## [4] What's next / market sentiment
- **Reputational stacking:** the hack landed the same week as a **paid-influencer scandal** (Polymarket reportedly paid creators to post fake "winning bet" videos; it said it would audit promotional content) and amid **Senators urging the CFTC to investigate Polymarket's advertising.** Geographic friction is also rising ([[Spain blocks prediction markets Polymarket and Kalshi]], [[Indonesia bans Polymarket after Prabouw ouster bets]]).
- **Why the market will likely shrug on the dollars but not on the narrative:** $3M is immaterial to a $9B company, and full refunds neutralize user anger. **The counterintuitive second-order risk:** the breach feeds the **"Polymarket isn't institution-grade" narrative** precisely while the **CFTC application** ([[Polymarket seeks CFTC approval for US crypto exchange]]) and the **ICE relationship** are pending — a security/marketing credibility wobble during a regulatory review is **more expensive than the loss itself.** Expect: no vendor disclosure unless forced, a quiet frontend-dependency hardening pass, and continued external pressure (CFTC, EU/Asia bans). (hypothesis)

## Sources
- TechCrunch (primary, in note): Polymarket says hackers stole users' funds — https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/
- BleepingComputer: Polymarket customers lose $3 million in supply-chain attack — https://www.bleepingcomputer.com/news/security/polymarket-customers-lose-3-million-in-supply-chain-attack/
- crypto.news: Polymarket to refund users after $2.94M frontend phishing attack — https://crypto.news/polymarket-to-refund-users-after-2-94m-frontend-phishing-attack/
- The Next Web — https://thenextweb.com/news/polymarket-hack-3-million-stolen-third-party-breach
- Cybernews — https://cybernews.com/security/polymarket-hit-by-cyberattack-via-third-party-dependency/
- Internal: [[Polymarket raises $2B from ICE at $9B valuation]], [[Polymarket seeks CFTC approval for US crypto exchange]], [[Circle and Polymarket partner to shift to native USDC]], [[Polymarket integrates with Bitget Wallet's 90 million users]], [[Kalshi to require employer disclosures before sensitive trades]], [[CoinDCX reports $44M theft from operational account]], [[Hyperbridge processes first fund recovery after hack]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Which third-party vendor was actually breached?** Open — never named (no oracle/wallet/relayer identified). The opacity is itself a red flag for a CFTC-applicant.
2. **Was this truly "third-party," or a Polymarket dependency-management failure?** Partly open — the vendor's code ran on Polymarket's frontend because Polymarket chose to load it without integrity checks (SRI/pinning). Root cause is shared. (analysis)
3. **Exact loss and victim count?** ~$2.9–3.0M (PeckShield ~$3M; ~$2.94M reported), "11+" to "fewer than 15" wallets. Small and consistent across sources.
4. **Is "refunding in full" verified or just a promise?** Open — only an X statement; no on-chain proof of reimbursements seen at disclosure.
5. **Smart contracts untouched — confirmed?** Yes — multiple sources agree it was a frontend/supply-chain (signing-prompt) attack, not a contract exploit. Mitigates systemic-risk framing.
6. **Is this really the second incident in a month?** Reported yes — ≈late-May compromised internal ops key drained ~$600K from the UMA CTF Adapter on Polygon. If true, signals an op-sec pattern, not bad luck. (verify)
7. **Does the small dollar size make the story immaterial?** No — the weight is reputational/regulatory, not financial; $3M is trivial vs $9B valuation.
8. **Could a malicious frontend have stolen far more if higher-balance wallets had connected?** Likely yes — the cap was attacker reach/timing, not a built-in limit. Downside was luck-bounded. (hypothesis)
9. **Does Kalshi share this attack surface?** No — custodial/fiat model has no wallet-sign frontend flow; the breach widens Kalshi's trust edge.
10. **Regulatory trigger?** Indirect — Senators already pushing CFTC on Polymarket advertising; a breach during the pending CFTC exchange application compounds scrutiny. No formal investigation tied to the hack yet. (open)
11. **Why disclose via X and not a formal post-mortem?** Controls narrative, limits liability, avoids naming the vendor. Standard but weak for an institution-grade aspirant. (analysis)
12. **How exposed is the integration-led growth model (Bitget, Circle, Nasdaq data)?** More integrations = larger frontend/dependency attack surface. Structural, recurring risk. (analysis)
13. **Is the timing with the fake-influencer scandal coincidental?** Yes (independent events), but they stack into one "Polymarket credibility" narrative the same week.
14. **Did attackers fully launder the funds (Polygon→ETH→1,893 ETH, one address)?** Reported yes — consolidation suggests low recovery odds absent exchange freezes.
15. **What changes the importance upward?** Naming of a widely-used vendor (blast radius beyond Polymarket), proof refunds didn't happen, or a CFTC action citing the breach.

Importance: 3/5 — Real, confirmed user losses and a credible supply-chain attack with a clear laundering trail, but small dollar size ($3M), narrow blast radius (<15 wallets), no contract/systemic compromise, and prompt full-refund commitment cap the severity. Weight comes from the reputational/regulatory timing (pending CFTC application, ICE backing, second incident in a month, concurrent ad scandal) rather than the money — hence above "noise" but not a top-tier event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-27]] (2026-06-27).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Prediction markets are now a real, fast-scaling vertical, not a fringe. Combined Kalshi+Polymarket monthly volume rose from <$5bn (Sep 2025) to a ~$25.7bn peak (Mar 2026), then cooled to ~$8.6bn taker volume in Apr 2026 (per The Block / news.bitcoin.com, as of Apr 2026) — i.e. volume is large but cyclical/event-driven (elections, sports, crypto), not a smooth ramp. The two leaders control ~85–95% of industry volume (per quantvps/defirate citations) — a **duopoly with a long tail**. Sports/politics/crypto = ~90% of volume on both. **Why now for the security angle:** the sector's growth is integration-led (wallets, oracles, settlement partners), and the dominant crypto attack surface in 2026 has shifted from smart-contract bugs to **frontend/supply-chain + private-key compromise** — private-key compromise alone = 43% of exploit losses over the trailing 30 days (per crypto-security trackers via MetaMask/CCN). The Polymarket breach is a textbook case: vendor-injected JS, contracts untouched. (analysis)

**Competitive landscape.** Sector KPIs: monthly notional volume, taker volume, take rate (fees), and — uniquely relevant here — **custody model** (custodial/fiat vs self-custody/wallet-sign), which is the single variable that determines exposure to this attack class. Recent dated moves: Kalshi raised ~$1bn at $22bn (May 2026, Coatue/Sequoia/a16z/Morgan Stanley) and is now reportedly chasing ~$40bn (per CoinDesk, 2026-06-24); Polymarket is reportedly seeking ~$15bn off its Oct-2025 $9bn ICE post-money (per DeFi Rate / TFN). Kalshi overtook Polymarket on US-relevant taker volume for the first time in Apr 2026 ($5.42bn vs $1.99bn). **Protagonist's position:** Polymarket is the international/crypto-native volume leader but is **catching up and trading at a discount** to Kalshi on the regulatory-trust axis — and Fortune (2026-04-21) explicitly ties Polymarket's valuation discount to its crypto ties. This breach sharpens exactly that discount. Moat: network/liquidity effects + the pending CFTC/ICE legitimacy path — but the breach is a direct hit to the legitimacy leg, not the liquidity leg. (analysis)

**Comps & multiples.** No revenue is publicly disclosed for either private name, so EV/Revenue, P/E etc. = **no data / [UNSOURCED]**. Only round valuations are sourceable — mark as round post-money, NOT market cap:
- Polymarket — ~**$9bn** post-money (ICE, Oct 2025); reportedly targeting ~$15bn now.
- Kalshi — ~**$22bn** (May 2026); reportedly targeting ~$40bn.
- Implied valuation gap: $22bn / $9bn = **~2.4x** on last priced rounds, widening to $40bn / $15bn = **~2.7x** on targets — Kalshi is re-rating faster despite Polymarket's larger international volume. A revenue/volume multiple cannot be computed (fees undisclosed), so this is a **qualitative comparison, distribution not computed**.
- Internal comps (in-base): the reimburse-and-move-on playbook is consistent — [[CoinDCX reports $44M theft from operational account]] (treasury-covered, $44M, far larger), [[Hyperbridge processes first fund recovery after hack]], [[Crypto.com hit by unreported attack leaking user data]], and the systemic frame in [[TRM Labs North Korea hackers took 76% of 2026 crypto hack value]] and [[Circle faces class action over Drift Protocol USDC hack]] (the latter shows refunds don't always pre-empt litigation). Defensive-side comp: [[Hypernative raises $40M for crypto threat detection]] (threat-detection demand is the second-order beneficiary).

**Risk flags.**
1. **Regulatory-timing risk.** A self-custody frontend breach during a *pending CFTC exchange application* and active ICE backing is the expensive part, not the ~$3M. Second-order: it hands Senators/CFTC a concrete "not institution-grade" data point right as the regulatory case is being decided. (analysis)
2. **Structural attack-surface risk from the growth model.** Polymarket's edge — integrations (Bitget, Circle, oracles) — is the same thing that enlarges its frontend/dependency attack surface. This is recurring, not one-off; the $3M cap was attacker reach/luck, not a built-in limit (a higher-balance wallet connecting could have made it far larger). (hypothesis)
3. **Disclosure/opacity risk.** Disclosed via X, no vendor named, no formal post-mortem, "full refunds" unverified on-chain at disclosure. For a regulated-exchange aspirant, opacity is itself a credibility cost — and as [[Circle faces class action over Drift Protocol USDC hack]] shows, a refund promise does not foreclose legal/regulatory follow-through.

**What this changes (idea-lens).** Not a re-rating of the *sector's* size — the duopoly TAM thesis is intact and Kalshi is unaffected. It is a **relative re-rating between the two leaders**: the breach widens Kalshi's existing trust/valuation premium (custodial-fiat model has no wallet-sign vector to exploit) right as it raises at ~$40bn. Falsifiable thesis: *Polymarket's crypto/self-custody model is a structural valuation drag that no amount of volume leadership offsets while the CFTC decision is pending.* Trigger/what would break it: CFTC approval of Polymarket's exchange with no breach-citing condition (thesis wrong); conversely, a CFTC action referencing security, a named widely-used vendor (blast radius beyond Polymarket), or a second integration-driven breach would confirm it. (analysis)

Sources: https://www.theblock.co/data/decentralized-finance/prediction-markets/polymarket-and-kalshi-volume-monthly · https://news.bitcoin.com/prediction-market-traders-push-april-2026-volume-to-8-6b-kalshi-takes-the-lead/ · https://www.coindesk.com/business/2026/06/24/kalshi-targets-a-massive-usd40-billion-valuation-widening-lead-over-rival-polymarket · https://defirate.com/news/polymarket-eyes-15b-valuation-gap-with-kalshi-widens/ · https://fortune.com/2026/04/21/polymarket-valuation-discount-kalshi-crypto/ · https://crypto.news/polymarket-to-refund-users-after-2-94m-frontend-phishing-attack/ · https://metamask.io/news/crypto-security-report-2026
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
