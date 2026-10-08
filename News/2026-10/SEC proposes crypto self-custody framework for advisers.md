---
title: "SEC proposes crypto self-custody framework for advisers"
date: 2026-10-05
retrieved: 2026-10-08
tags:
  - company/sec
  - industry/crypto
  - industry/regtech
  - region/us
  - type/regulation
sources:
  - https://u.today/sec-proposes-new-crypto-custody-framework
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s513c5a6d
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# SEC proposes crypto self-custody framework for advisers

> [!info] 2026-10-05 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 SEC proposes a new crypto custody framework that would let registered investment advisers self-custody certain crypto assets when no suitable outside custodian is available. The proposal amends rules under the Investment Advisers Act and the Investment Company Act, and opens a pathway for state-chartered trust companies to serve as crypto custodians. Chairman Paul Atkins called existing rules "crafted for a bygone era."

## Первоисточники

### u.today
<https://u.today/sec-proposes-new-crypto-custody-framework>
*412 слов · direct*

Home 
 
 
 

 News 
 

 SEC 
 
SEC Proposes New Crypto Custody Framework
 The U.S. Securities and Exchange Commission has proposed a new regulatory framework for crypto.  
 The aforementioned framework would make it easier for registered investment advisers and regulated funds to get exposure to the novel asset class on behalf of clients, including, in some cases, through self-custody. 
 The proposal would amend custody requirements under the Investment Advisers Act of 1940 and the Investment Company Act of 1940.  
 The SEC would permit advisers to self-custody certain crypto assets when an appropriate outside custodian is unavailable. State-chartered trust companies would also receive a pathway to be crypto custodians.  
 SEC Chairman Paul Atkins has stated that existing custody rules were built around a financial system that looked very different from today's.  
 Bitcoin did not exist when much of the framework was developed. Since then, crypto has become a multi-trillion-dollar asset class sought by investors. 

 Atkins said the proposal is intended to replace the regulatory uncertainty surrounding crypto custody with a defined compliance framework for investment advisers and funds. In his words, the existing rules had been "crafted for a bygone era." 
 It is worth noting that these are only proposed rules. Their final form could change following public feedback. 
 The proposal does not simply give investment advisers unrestricted permission to hold private keys themselves. 
 An adviser would first have to determine that a permitted custodian is unavailable for the particular crypto asset. This would have to be done before the adviser takes custody and then repeated at least once every quarter.  
 Self-custody would function as a conditional alternative. The adviser would also need to show that it has the necessary expertise to safeguard the specific crypto asset.  
 Specific tech requirements  
 Custodians would have to address private-key management and joint authorization by at least two people.  Advisers would also have to maintain each client's crypto in one or more blockchain addresses containing only that client's assets.  
 They would also have to take into account the risks associated with keeping client crypto directly.  
 An adviser would need to prepare a report that would examine controls connected to custodial services, including necessary safeguards.  
 Clients would receive account statements at least quarterly. Those statements would identify the blockchain address holding the client's crypto and the network on which the address operates.  
 For now, the proposal remains just a proposal. The public will have 60 days to submit comments in the Federal Register.  
Related articles
Recommended articles
Subscribe to daily newsletter
Successful!

## Контекст

<!-- enrichment:context -->
# Context-enrichment: SEC proposes crypto self-custody framework for advisers
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
On **2026-10-01** the SEC voted **4–1** to propose a tailored crypto-custody framework (Press Release **2026-100**, proposing release **IA-7023**, file no. **S7-2026-35**) amending the custody/"safeguarding" requirements under the **Investment Advisers Act of 1940** and the **Investment Company Act of 1940** (covering RIAs, registered funds and BDCs). The u.today source note dates it 2026-10-05; the actual Commission action was Oct 1 — the note is a few-days-late retelling, not a new event.

Two pathways, de-PR'd:
1. **State-chartered trust companies** get an explicit path to qualify as **qualified custodians** for crypto.
2. **Conditional self-custody** — and this is the headline, but it is NOT "advisers can just hold keys." Hard gating:
   - Adviser must first **document that no permitted/qualified custodian will hold that specific asset**, and **re-test that determination at least quarterly**. Self-custody is a *fallback of last resort*, not a default.
   - Adviser must **demonstrate expertise** to safeguard the specific asset.
   - Technical controls: **private-key management** + **joint authorization of any transaction by ≥2 people**.
   - **Segregation**: each client's crypto in blockchain address(es) holding **only that client's** assets.
   - **Independent public accountant** must report on control objectives within **6 months** of taking self-custody, then annually.
   - **Quarterly client statements** naming the **blockchain address** and the **network**.
   - **No transition period** for the modernized traditional-custody rules (note: aggressive, operationally).
   - **60-day comment period** from Federal Register publication. Proposal only — final form can change.

**Why structured this way / what it reveals:** this is a near-180° reversal of posture. The 2023 "Safeguarding Rule" (Rule 223-1, proposed 4–1 on 2023-02-15 under Gensler) *expanded* the asset scope to crypto while *shrinking* who could custody it — leaving advisers "on the wrong side of the law" with nowhere compliant to put client crypto. That proposal was formally **withdrawn 2025-06-12**. The 2026 Atkins SEC inverts the logic: instead of forcing crypto into a custodian universe that doesn't exist, it (a) widens who counts as a qualified custodian (state trust cos) and (b) creates a conditional escape hatch (self-custody) precisely for assets with no custodian. The "bygone era" quote is the political framing for the reversal. The real tell is the quarterly re-test + accountant report + segregation stack: the SEC is trying to make self-custody *so procedurally expensive* that it stays a genuine edge case, not a loophole — a defensible design against the "endangering investors" critique.

## [1] Competitors / peers (regulatory + custody-infra landscape)
- **Prior SEC posture (2023):** Gensler-era Safeguarding Rule — opposite direction (see [0]); withdrawn 2025. The single most important comp: *same agency, reversed stance in ~3 years.*
- **SEC Division of Trading & Markets (2025-12):** stated **broker-dealers must hold crypto private keys** themselves to satisfy Rule 15c3-3 "possession or control" (Peirce "No Longer Special" statement) — see [[SEC says broker-dealers must hold crypto private keys]]. Parallel track: BD custody via self-holding of keys already being normalized; the adviser side now catches up.
- **OCC / banking chartering race:** [[Crypto.com gets OCC conditional approval for trust bank charter]] (2026-02) and [[Crypto.com files for OCC National Trust Bank charter]] (2025-10) — crypto-natives buying their way into *federal* qualified-custodian status. [[US Bank to custody reserves for Anchorage Digital stablecoins]] (2025-10) — Anchorage is the only OCC-chartered crypto-native bank/qualified custodian. The SEC's "state trust company" path is a *parallel, lighter* route that competes with the OCC federal charter route.
- **Infra custodians:** [[Bakkt, Galaxy and FalconX select Fireblocks for custody]] (2025-10) — Fireblocks Trust Co. positioning as qualified custodian. These incumbents benefit if the rule *keeps* custodians central; they are structurally threatened by the self-custody carve-out.
- **UK/EU contrast:** [[The Financial Conduct Authority (FCA) set out how its rules will apply]] (2026-01) — FCA requires firms holding client crypto to hold on trust, plain-language disclosures, strict third-party rules. The UK leans *custodian-mandatory*; the US 2026 proposal is comparatively *permissive*.

**Why the landscape is this way / second-order:** the US now has *three competing routes to legitimately custody client crypto* — (1) federal OCC trust charter (Anchorage, Crypto.com pending), (2) NEW state trust-company qualification, (3) NEW adviser self-custody fallback. The state-trust path is the quiet winner: it legitimizes the dozens of **state-chartered (esp. NH, Wyoming, SD) non-depository trust companies** already operating (Crypto.com's NH-regulated custody entity, etc.) without forcing the slow OCC queue. Second-order: this *undercuts* the OCC federal-charter moat — why pay for a national charter if a state trust charter + SEC qualification gets you adviser business? The incumbents who invested in heavy federal/qualified-custodian status (Anchorage, Fireblocks Trust, Coinbase Custody) lose relative moat.

## [2] Company history / fit (the SEC under Atkins)
Trajectory: Gensler SEC (enforcement-first, "regulation by enforcement," 2023 Safeguarding Rule expanding crypto scope) → Atkins confirmed 2025 → Project Crypto / "crypto-clarity" agenda → 2025-06 withdrawal of the Safeguarding Rule → 2025-12 Trading & Markets BD-custody statement → **2026-10 this proposal**. Signals of *more to come*: SEC has flagged additional crypto rulemakings.

**Why the SEC acts this way:** structural pressure — crypto became a multi-trillion-dollar asset class with ETPs/funds live, but the custody rulebook predates Bitcoin, so advisers/funds faced legal limbo offering crypto exposure. The agency's political mandate shifted to "provide a compliant path." The 4–1 vote with Atkins/Peirce/Uyeda in favor (Peirce's resignation took effect right after; Crenshaw, the lone recurring dissenter, had already resigned Jan 2026) shows a **depleted, ideologically aligned Commission** — low internal friction, which is *why* a reversal this large passed quickly. (Note: with the Commission down to ~2 members post-resignations, quorum/legitimacy of aggressive rulemaking is itself a live question — analysis.)

## [3] Novelty / value-add / traction
**Genuinely new:** (a) an SEC-sanctioned **self-custody pathway for RIAs** — the first time the federal adviser custody regime contemplates the adviser *itself* holding keys for client assets; (b) explicit **state trust company** qualification for crypto. Neither existed in US adviser law before.

**Traction = ZERO (and must be flagged):** this is a **proposal**, 60-day comment window not yet closed, no final rule, no effective date, no adviser self-custodying under it. "Announced," emphatically not "live." Treat every "would/could" as conditional.

**Why the value-add is real but bounded:** the real unlock is *optionality for assets with no custodian* (long-tail tokens, newly-launched assets, certain DeFi positions) — exactly where the 2023 rule created a dead-end. But the gating stack (quarterly no-custodian test + ≥2-person auth + per-client address segregation + annual accountant report) is deliberately heavy, so in practice **mainstream BTC/ETH exposure will still flow through qualified custodians** (Coinbase, Anchorage, Fidelity, BNY) — those keep the margin. Self-custody is an edge-case release valve, not a disintermediation of custodians. **Who captures margin:** state trust companies (new addressable adviser business) and large RIAs with in-house crypto ops; incumbents custodians lose only the long-tail they never served anyway. The investor-protection risk (Better Markets: "very high risk of loss the SEC exists to prevent") is the genuine downside — self-custody failure (key loss, hack, insider) has no SIPC/FDIC backstop.

## [4] What's next / market sentiment
- **Timeline:** 60-day comment period from Federal Register publication → likely re-proposal or final rule in 2027; "no transition period" on modernized traditional custody is the most-contested operational item and may soften.
- **Sentiment — sharply divided:** adviser/industry groups praise the "positive framework" and crypto-access unlock; **investor-protection groups (Better Markets) and dissenting commissioner Crenshaw ("Poking Holes")** warn it dilutes protections and that custodianship of this magnitude needs formal rulemaking, not staff relief. Crypto-market reaction broadly positive (easier fund/ETP access).
- **Regulatory backdrop:** part of a broader Atkins-SEC crypto-clarity push; interacts with OCC chartering race and stablecoin/GENIUS-era framework.
- **Risks:** (1) litigation/APA challenge given the 180° reversal and thin Commission; (2) a high-profile self-custody loss during comment period could kill the self-custody prong; (3) quorum questions if the Commission stays depleted.

**Why the market goes this way / counterintuitive second-order:** the headline "self-custody" is a red herring for weight — the *durable* structural change is **legitimizing state trust companies as qualified custodians**, which reroutes the custody-infra competitive map away from the OCC federal-charter moat. Counterintuitive: a rule *marketed* as empowering advisers to self-custody will, because of its cost stack, mostly *entrench a new tier of state-chartered custodians* — the opposite of disintermediation. The fragility is political, not technical: a reversal this sharp on a 2-member Commission is legally brittle, so the single biggest variable is whether it survives comment + courts intact.

## Sources
- SEC Press Release 2026-100 — https://www.sec.gov/newsroom/press-releases/2026-100-sec-proposal-would-address-how-investment-advisers-funds-can-custody-crypto-assets-under-federal
- SEC IA-7023 Fact Sheet — https://www.sec.gov/files/ia-7023-fact-sheet.pdf
- u.today (note primary source) — https://u.today/sec-proposes-new-crypto-custody-framework
- The Block — https://www.theblock.co/news/regulation/2026-10-01-sec-proposes-crypto-custody-rule-investment-advisers-funds-417498
- Crowdfund Insider — https://www.crowdfundinsider.com/2026/10/315828-sec-proposes-conditional-crypto-custody-framework-for-advisers-and-funds/
- CNBC — https://www.cnbc.com/2026/10/02/sec-bitcoin-crypto-proposal.html
- Wealthmanagement.com (divisive reactions / Crenshaw, Better Markets) — https://www.wealthmanagement.com/regulation-compliance/sec-proposes-self-custody-rules-for-crypto-assets
- cryptonews.net (2023 reversal context) — https://cryptonews.net/news/legal/33527718/
- DWT / Perkins Coie (2023 Safeguarding Rule background) — https://perkinscoie.com/insights/update/sec-spotlights-crypto-new-safeguarding-rule-proposal
- Internal: [[SEC says broker-dealers must hold crypto private keys]], [[Crypto.com gets OCC conditional approval for trust bank charter]], [[Crypto.com files for OCC National Trust Bank charter]], [[US Bank to custody reserves for Anchorage Digital stablecoins]], [[Bakkt, Galaxy and FalconX select Fireblocks for custody]], [[The Financial Conduct Authority (FCA) set out how its rules will apply]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Proposal vs rule — what's actually in force?** Nothing. It's a proposed rule (IA-7023, S7-2026-35), 4–1 vote on 2026-10-01, 60-day comment window from Federal Register publication. No final rule, no effective date, no adviser self-custodying. Every "would/could" is conditional. *(answered)*

2. **Is "self-custody" the real story, or marketing bait?** Largely bait. The gating stack (quarterly no-custodian re-test, ≥2-person auth, per-client address segregation, annual independent-accountant control report) makes self-custody a last-resort edge case. The *durable* change is state-trust-company qualification. *(answered — analysis)*

3. **Why did the SEC reverse itself in ~3 years?** 2023 Safeguarding Rule (Gensler, 4–1) expanded crypto scope while shrinking eligible custodians → dead-end; withdrawn 2025-06-12. Atkins SEC inverts: widen custodians + conditional self-custody. Political framing = "crafted for a bygone era." *(answered)*

4. **Who actually captures the margin?** State trust companies (new adviser addressable market) + large RIAs with in-house crypto ops. Incumbent qualified custodians (Coinbase, Anchorage, Fidelity, BNY) keep mainstream BTC/ETH flow; lose only the long-tail they never served. *(answered — analysis)*

5. **Does this disintermediate custodians?** No — counterintuitively it entrenches a *new tier* (state trust cos) and undercuts the OCC federal-charter moat, not the custodian model itself. *(answered — analysis)*

6. **How legally durable is this on a 2-member Commission?** Weak. Peirce resigned right after the vote; Crenshaw resigned Jan 2026. A sharp reversal on a depleted Commission invites APA/quorum challenges. Biggest single risk variable. *(open — litigation outcome unknown)*

7. **What's the investor-protection downside, concretely?** Self-custody failure (key loss, hack, insider theft) has no SIPC/FDIC backstop; Better Markets: "very high risk of loss the SEC exists to prevent." Crenshaw's "Poking Holes" dissent: dilutes protections, needs formal rulemaking. *(answered)*

8. **Is the note itself fresh or a late retell?** Note dated 2026-10-05 (u.today); the Commission action was 2026-10-01. The item is a few-days-late single-source retelling but of a genuine NEW event. *(answered)*

9. **Does any prior corpus note cover THIS proposal?** No. Nearest: [[SEC says broker-dealers must hold crypto private keys]] (2025-12, broker-dealer track, different rule 15c3-3), FCA (UK, 2026-01), OCC charters (Crypto.com). None is this adviser-side Advisers-Act/Investment-Company-Act proposal. → **fresh.** *(answered)*

10. **What exactly is new vs the 2023 proposal?** 2023: mandatory qualified custodian, scope expansion, no self-custody. 2026: adds (a) self-custody fallback, (b) state-trust-company qualification, (c) no transition period. Direction reversed. *(answered)*

11. **Who's silent about what?** The SEC is light on *economics of enforcement* — who audits the quarterly "no custodian available" determination, and how a self-custody loss is remedied for clients. Liability allocation on key loss is underspecified. *(open)*

12. **Mechanism delta in one sentence?** Unlike the 2023 rule (crypto must sit with a shrinking set of qualified custodians), the 2026 proposal lets advisers self-custody as a conditional last resort AND promotes state trust companies to qualified-custodian status. *(answered)*

13. **"No transition period" — realistic?** Operationally aggressive for the modernized traditional-custody rules; likely the most-contested comment item and a candidate to soften in any final rule. *(open — depends on comments)*

14. **Second-order effect on the OCC chartering race?** If a state trust charter + SEC qualification unlocks adviser business, the value of a slow OCC national trust charter (Crypto.com pending, Anchorage holder) erodes — a quiet competitive repricing. *(answered — hypothesis)*

15. **What would move importance up or down?** UP: final rule adopted / a marquee adviser announces self-custody plans. DOWN: proposal withdrawn, struck down on quorum/APA grounds, or a self-custody loss kills the prong. *(open)*

**Importance: 4/5** — A sitting-SEC, Commission-voted (4–1) proposed rule that materially reverses the prior crypto-custody posture, reshapes who can be a qualified custodian in the US, and opens a (heavily conditioned) self-custody path — with a 60-day comment window now running. High policy weight and clear second-order effects on the custody-infra competitive map. Held below 5 because it is a *proposal* with zero traction, legally brittle on a depleted Commission, and the self-custody headline is narrower in practice than the framing implies.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto custody / institutional digital-asset infrastructure. Size estimates vary widely and are vendor-report driven: per Stratistics MRC (via marketresearch.com) the broader "crypto custody & institutional digital-asset management" market is ~$8.4bn in 2026 → ~$48.7bn by 2034 (~24.6% CAGR); the narrower "crypto custody provider" slice is pegged far smaller (~$3.69bn in 2026, ~13% CAGR, per Research and Markets). The spread (~2–5x across firms, as of Oct 2026) means no reliable single TAM — treat as "order-of-magnitude, not precise." Structure: historically regulation-gated — the SEC custody rule (Rule 206(4)-2 / Advisers Act) requires client assets at a "qualified custodian" (bank or trust company), which until recently left crypto in a grey zone. Barriers = regulation + trust charters, not capital. Why now: the proposed framework (SEC, 2026-10-01; 60-day comment window) is the first *dedicated* crypto custody rule for RIAs/funds and codifies state-chartered trust companies as qualified custodians — turning a 2025 no-action posture into proposed ruletext. Second-order effect: a defined compliance path lowers the main friction keeping advised/fund money out of crypto, i.e. demand-side unlock rather than a new supply technology.

**Competitive landscape.** Sector KPIs: assets-under-custody (AUC), number of chartered entities acting as qualified custodian, # of RIA/fund mandates. Industry AUC reportedly surpassed ~$400bn in 2024 (per snsinsider report) — directional, not auditable. Key players as qualified/permitted custodians for US regulated money: Coinbase Custody (NYDFS trust charter + OCC conditional federal trust approval, Apr 2026 — see internal comp below), Anchorage Digital (OCC national trust bank, the only federally-chartered crypto bank), BitGo (SD + NY trust charters), Fireblocks Trust Company (NYDFS limited-purpose trust), plus Crypto.com Custody Trust and Zero Hash Trust. Basis of competition: regulatory status (charter) + security/key-management tech + distribution into asset managers. Recent moves: Coinbase OCC conditional approval (2026-04); Crypto.com OCC conditional approval (2026-02); BitGo×InvestiFi bank-distribution deal (2026-02); Bakkt/Galaxy/FalconX picking Fireblocks (2025-10). Protagonist: the SEC is the regulator, not a competitor — its "position" is that of rule-setter. The proposal's own novelty is the *self-custody* carve-out (adviser may hold keys only if no qualified custodian is available, re-tested quarterly, with 2-person authorization and per-client blockchain addresses) `(analysis)`: this is a narrow fallback, not an invitation for advisers to become their own custodians.

**Comps & multiples.** No valuation/round/deal in the note — it is a rule proposal, so trading multiples are **not applicable / no data** (no issuer, no transaction). Internal comps (regulatory + charter precedents in base that this proposal directly builds on):
- [[Coinbase wins conditional approval for national trust charter]] (2026-04)
- [[Crypto.com gets OCC conditional approval for trust bank charter]] (2026-02)
- [[Zero Hash Trust Company approved to launch]] (2025-09, explicitly cites "qualified custodian for RIAs")
- [[US Bank to custody reserves for Anchorage Digital stablecoins]] (2025-10)
- [[Bakkt, Galaxy and FalconX select Fireblocks for custody]] (2025-10)

Private-custodian valuations (round, not market cap): not disclosed in base; `[UNSOURCED]` here — avoid attaching peer post-money figures to a rule proposal where they'd be misleading.

**Risk flags.**
1. **Proposal, not law.** Only proposed ruletext with a 60-day comment period; final form can change materially after industry/consumer feedback. Why it matters: custody providers and advisers cannot yet build compliance on it, so near-term commercial impact is signaling, not revenue.
2. **Self-custody = operational/fiduciary risk shifted to advisers.** The carve-out puts private-key safekeeping, quarterly re-testing and 2-person controls on RIAs that may lack custody expertise. Why: key loss/theft at an under-equipped adviser becomes a client-loss and liability event the old bank-custodian model was designed to prevent.
3. **Charter-arbitrage / fragmentation.** Blessing state-chartered trust companies as qualified custodians favors incumbents already holding charters (Coinbase, BitGo, Fireblocks, Crypto.com) and could invite a race of state charters with uneven supervision. Why: regulatory standard-shopping can erode the very safeguard the rule intends.

**What this changes (idea-lens).** `(analysis)` This reads as a demand-unlock for the *established, chartered* custodians rather than a leveling event: the biggest winners are entities already positioned as qualified custodians (Coinbase/Anchorage/BitGo/Fireblocks), who gain SEC-blessed access to RIA/fund flows; the self-custody path is a narrow safety valve, not a disintermediation of custodians. Falsifiable thesis: if finalized broadly, expect a step-up in RIA/fund crypto mandates routed to the top handful of chartered custodians within ~12 months of a final rule. Trigger to watch: the final rule (post-comment) and how many advisers actually invoke self-custody — heavy self-custody uptake would *falsify* the "custodians win" thesis and signal custodian capacity/pricing gaps.

Sources: https://u.today/sec-proposes-new-crypto-custody-framework · https://www.theblock.co/news/regulation/2026-10-01-sec-proposes-crypto-custody-rule-investment-advisers-funds-417498 · https://www.coindesk.com/policy/2026/10/01/u-s-sec-maps-out-crypto-custody-in-new-proposal-that-furthers-its-digital-assets-agenda · https://www.marketresearch.com/Stratistics-Market-Research-Consulting-v4058/Crypto-Custody-Institutional-Digital-Asset-45264891/ · https://www.researchandmarkets.com/report/crypto-custody-provider · https://www.snsinsider.com/reports/digital-asset-custody-market-10886
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
