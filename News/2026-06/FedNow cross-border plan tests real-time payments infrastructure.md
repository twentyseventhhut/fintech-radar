---
title: "FedNow cross-border plan tests real-time payments infrastructure"
date: 2026-06-22
tags:
  - industry/payments
  - region/us
  - type/regulation
sources:
  - https://www.connectingthedotsinfin.tech/r/7b97d837
  - https://www.connectingthedotsinpayments.com/r/87c25949
status: enriched
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s6dee2e88
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# FedNow cross-border plan tests real-time payments infrastructure

> [!info] 2026-06-22 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 FedNow cross-border plan tests real-time payments infrastructure. The Federal Reserve has proposed changes to allow FedNow participants to use intermediary banks for cross-border payments, extending the instant payment network beyond domestic transactions. FinTechs support the move, while banks have raised concerns around sanctions screening and compliance requirements.

[Connecting the Dots in Payments] 🇺🇸 FedNow cross-border plan tests real-time payments infrastructure. The Federal Reserve has proposed changes to allow FedNow participants to use intermediary banks for cross-border payments, extending the instant payment network beyond domestic transactions. FinTechs support the move, while banks have raised concerns around sanctions screening and compliance requirements.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/7b97d837>
- <https://www.connectingthedotsinpayments.com/r/87c25949>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: FedNow cross-border plan tests real-time payments infrastructure
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-04-08 the Federal Reserve Board issued a **notice of proposed rulemaking** (not a launch, not a live capability) to amend subpart C of **Regulation J**. The change would let FedNow participants use **intermediaries other than Reserve Banks** to send funds transfers through FedNow. Comment period ran ~60 days after Federal Register publication (published 2026-04-10), i.e. roughly through **2026-06-09** (sources put the close near June 9). The digest item (2026-06-22) is a **secondary recap** of the comment-period debate, not new Fed action.

What it actually does, de-PR'd: it does **not** make FedNow a cross-border rail. Today a FedNow transfer can include only **two U.S. banks** plus a Reserve Bank — both originator and beneficiary must be U.S.-bank customers. The proposal would let a sending or receiving U.S. bank act as a **correspondent for a non-U.S. bank**, so FedNow settles the **domestic U.S. leg in real time** while the **international leg still rides conventional correspondent rails** (no real-time settlement beyond U.S. borders).
- **+ Why structured this way / what it reveals:** the Fed is doing the minimum legal change (remove the "no intermediaries" restriction in Reg J) rather than building a cross-border scheme, FX layer, or messaging interlink. → The headline "cross-border plan" overstates it: this is a **regulatory enablement of correspondent banking on top of FedNow**, not an instant cross-border network. The real-time benefit is confined to the U.S. domestic settlement leg; once funds hit the overseas correspondent, the transaction follows the same slow/opaque process as today. → The central question is therefore NOT "will FedNow rival SWIFT/Nexus" but "does removing a domestic settlement-leg friction meaningfully improve end-to-end cross-border, given the international leg is unchanged?"

## [1] Competitors / peers
- **The Clearing House RTP network** (bank-owned): also pursuing cross-border/international settlement; reportedly targeting a **September 2026** go-live for expanded capabilities — ahead of FedNow on this front. See [[Federal Reserve launches FedNow network intelligence API for fraud]] for FedNow's domestic posture.
- **BIS Project Nexus**: the genuinely cross-border-native effort — multilateral **interlinking of domestic instant-payment systems** (India, Malaysia, Philippines, Singapore, Thailand founding members; Indonesia joined). Nexus Scheme Organisation incorporated 2025 in Singapore; live implementation work through 2026; targets <60-second end-to-end. This is **architecturally different**: Nexus connects IPSes so the whole payment is instant, vs. FedNow's proposal which only makes the U.S. leg instant.
- **SWIFT**: rolling out a new retail payments framework + blockchain shared-ledger; still the default international leg the FedNow proposal would feed into. See [[Deutsche Bank goes live on Swift consumer payments initiative]].
- **Mastercard / TIPS**: cross-currency instant pilot (euro↔Danish krone via Mastercard Move) — see [[Mastercard joins TIPS cross-currency instant payments pilot]] — closer to true cross-currency instant than FedNow's domestic-leg-only approach.
- **Bank of America** cross-border real-time service via Swift/CashPro — see [[Bank of America to launch cross-border real-time payments service]] — a bank-level product, complementary not competitive.
- **+ Why the lay of the land is this way:** the U.S. is **behind** on cross-border instant because its domestic rail (FedNow, live 2023) was deliberately domestic-only; the rest of the world (Nexus, TIPS, India UPI links) built interlinking-first. → The Fed's move is **catch-up via the path of least resistance** (Reg J tweak) rather than joining a multilateral scheme like Nexus, which would require FX, governance, and foreign-IPS integration the Fed has not signaled.

## [2] Company history / fit
FedNow launched July 2023 as a domestic-only instant rail; adoption has grown via certifications — [[Intuit completes FedNow certification for instant payments]] (2026-04) — and fraud tooling — [[Federal Reserve launches FedNow network intelligence API for fraud]] (2026-05). The cross-border proposal fits a **logical maturation arc**: get domestic reach + fraud controls first, then loosen the intermediary restriction. **+ Why the Fed acts this way:** as operator AND regulator, it moves conservatively and via rulemaking with public comment — hence a *proposal* with a debate, not a product. The structural pressure is competitive (RTP, Nexus, stablecoins eating cross-border — see [[Payment trends and insights for 2026 by Deloitte]], remittance fees still >6%) pushing the Fed to at least not block FedNow from the cross-border value chain.

## [3] Novelty / value-add / traction
**Novelty is modest and legal, not technical.** Nothing new is built; a restriction is proposed to be lifted. **Traction = zero live** — it is a comment-stage proposal; banks broadly support the *direction* but split on timeline and risk allocation; FinTechs more enthusiastic.
- **+ Why value-add is limited (one level deeper):** the binding constraints on cross-border instant are **real-time sanctions screening, AML, FX, and foreign-regulatory differences** — none solved by this rule. Instant settlement is **irrevocable in seconds**, but receiving institutions get only seconds to screen against sanctions lists. The Clearing House / Bank Policy Institute flagged exactly this and recommended a **dedicated cross-border message code** + **two-phase opt-in rollout**. → So even if the rule passes, the **margin/value still sits with whoever handles the international leg + compliance** (correspondents, SWIFT, FX providers), not FedNow. FedNow captures the commoditized domestic settlement leg only.

## [4] What's next / market sentiment
Next: Fed reviews comments (closed ~June 9, 2026), then a final rule (timing open). RTP's ~Sept 2026 target may put it ahead. Sentiment: cautiously positive on direction; banks (ABA, BPI, TCH) warn that **compliance/sanctions and U.S.–foreign procedural mismatches could delay transfers** and want phased, opt-in implementation. Regulatory backdrop: GENIUS-era stablecoin momentum and Nexus pressure the Fed to keep FedNow relevant cross-border.
- **+ Why the market goes this way / second-order:** even a passed rule yields **incremental** improvement — a faster U.S. leg bolted onto an unchanged international leg. The counterintuitive effect: by enabling correspondent use, the Fed may **entrench correspondent banking** (and SWIFT) inside FedNow rather than displace it, the opposite of the "FedNow vs SWIFT" framing. The bigger cross-border disruption is more likely from **interlinking (Nexus)** or **stablecoins**, not from this Reg J amendment. Threat-to-SWIFT framing is overblown for now.

## Sources
- Fed press release (2026-04-08): https://www.federalreserve.gov/newsevents/pressreleases/other20260408a.htm
- Fed proposal details: https://www.federalreserve.gov/apps/proposals/FR-2026-0011-01/details
- Federal Register (2026-04-10), Reg J: https://www.federalregister.gov/documents/2026/04/10/2026-06996/collection-of-checks-and-other-items-by-federal-reserve-banks-and-funds-transfers-through-the
- Sullivan & Cromwell memo: https://www.sullcrom.com/insights/memo/2026/April/Federal-Reserve-Proposes-Expansion-Would-Permit-Use-FedNow-Cross-Border-Payments
- ABA Banking Journal: https://bankingjournal.aba.com/2026/04/fed-proposes-opening-fednow-to-cross-border-payments/
- BPI / The Clearing House comment: https://bpi.com/bpi-and-tch-comment-on-fednow-cross-border-payments-rule/
- PYMNTS: https://www.pymnts.com/real-time-payments/2026/fednow-cross-border-plan-tests-real-time-payments-infrastructure/
- American Banker: https://www.americanbanker.com/payments/news/fednow-proposes-support-for-cross-border-payments
- BIS Project Nexus: https://www.bis.org/about/bisih/topics/fmis/nexus.htm
- Internal: [[Federal Reserve launches FedNow network intelligence API for fraud]], [[Intuit completes FedNow certification for instant payments]], [[Bank of America to launch cross-border real-time payments service]], [[Mastercard joins TIPS cross-currency instant payments pilot]], [[Deutsche Bank goes live on Swift consumer payments initiative]], [[Payment trends and insights for 2026 by Deloitte]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Announced or launched?** This is a **proposal (NPRM)**, not a live capability — comment period closed ~2026-06-09; no final rule yet, no live cross-border FedNow flow. (answered)
2. **Does it make FedNow a cross-border rail?** No. FedNow would still settle only the **domestic U.S. leg** in real time; the international leg rides conventional correspondent banking. End-to-end is **not** instant. (answered)
3. **What's the precise mechanism delta vs today?** It only removes the Reg J "no intermediaries other than Reserve Banks" restriction, letting a U.S. bank act as correspondent for a non-U.S. bank. Purely legal/structural, no new tech. (answered)
4. **How does real-time sanctions screening work when settlement is irrevocable in seconds?** Open / unresolved — TCH and BPI flagged that receiving institutions have only seconds to screen; this is the core unsolved constraint. (open)
5. **Who is silent / split on what?** FinTechs enthusiastic; banks support direction but disagree on **timeline, risk allocation, and compliance procedures**. ABA fears U.S.–foreign procedural mismatches delay transfers. (answered)
6. **Is RTP ahead?** The Clearing House RTP reportedly targets ~**September 2026** for expanded/international capability — potentially ahead of FedNow's still-open rulemaking. (answered, monitor)
7. **How does this compare to BIS Nexus architecturally?** Nexus **interlinks domestic IPSes** for true end-to-end instant cross-border; FedNow proposal does not interlink and is not a Nexus member — fundamentally less ambitious. (answered)
8. **Does this threaten SWIFT?** Counterintuitively, it may **entrench** SWIFT/correspondent banking inside FedNow rather than displace it, since the international leg is unchanged. "Threat to SWIFT" framing is overstated. (answered)
9. **Who captures the margin?** The international-leg handlers (correspondents, FX, SWIFT, compliance) keep the value; FedNow captures only the commoditized domestic settlement leg. (analysis)
10. **What's the FX layer?** None provided by FedNow; FX still handled off-rail by correspondents. Open question whether this materially lowers cost vs current cross-border. (open)
11. **Will a final rule actually pass, and when?** Open — only the comment period has closed; final-rule timing and content unannounced. (open)
12. **What real traction/adoption exists?** Zero live cross-border traction; FedNow's traction is domestic (certifications, fraud API). (answered)
13. **Did the Fed signal joining a multilateral scheme (e.g. Nexus)?** No signal — chose the path-of-least-resistance Reg J tweak instead. (answered)
14. **Recommended implementation path?** TCH/BPI recommend a **dedicated cross-border message code** + **two-phase opt-in** rollout to manage compliance risk. (answered)
15. **Is the digest item even new news?** No — it's a 2026-06-22 recap of an April proposal + the comment-period debate; risk of overstating novelty. (answered)

Importance: 3/5 — Real and structurally relevant (the Fed loosening Reg J to let FedNow touch the cross-border value chain is a genuine policy direction with competitive stakes vs RTP/Nexus/SWIFT). But discounted because it is a **proposal, not live**, the **real-time benefit is confined to the domestic leg only**, the **hard constraints (sanctions/AML/FX) are unsolved**, and the digest item is a recap rather than fresh action. Not a 4 (no launch, no traction, incremental); not a 2 (it materially shapes U.S. cross-border instant-payments strategy and competitive positioning).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.**
Subvertical: cross-border instant payments / interlinking of domestic real-time payment systems (RTGS-adjacent rails). Note: this is a Fed NPRM (Reg J amendment), not a deal/round — no valuation, take-rate, or volume metric attaches to the protagonist, so the comps/multiples block is largely "no data" by design.
- **Size/growth:** cross-border payments market estimates diverge widely by methodology — ~$193.5bn (2026) at ~7.1% CAGR to 2033 per Grand View; ~$238bn (2026) at ~7.16% CAGR to 2031 per Mordor Intelligence; ~$397bn (2026) at ~7.9% CAGR per Fortune Business Insights (via the respective firm reports, as of 2026). The spread (~2x between low and high) means TAM here is a soft signal, not a precise figure — treat as "low-double-digit-billions revenue pool growing high-single-digit %." [partly UNSOURCED — paywalled report bodies; only headline figures cited]
- **Why-now / driver (de-PR'd):** remittance cost remains the binding pain point — global average **6.36%** in Q3 2025 (digital **4.59%**, non-digital **7.30%**), still >2x the **3% SDG/G20-by-2030 target** (per World Bank Remittance Prices Worldwide, Q3 2025). This is the structural pressure pushing every domestic rail toward cross-border. But the FedNow proposal does **not** touch the cost driver: it makes only the U.S. domestic settlement leg instant; FX, correspondent fees and AML/sanctions — where the 6%+ actually sits — are unchanged. → The "why now" is competitive (Nexus, RTP, stablecoins) far more than it is cost-reduction for the end user.
- **Structure:** the international leg is concentrated around SWIFT messaging + a shrinking correspondent-banking network (de-risking has cut correspondent relationships for a decade), with high entry barriers (regulation, liquidity, network). Value in cross-border is captured at the FX + compliance + correspondent layers, not at the domestic settlement rail. (analysis)

**Competitive landscape.**
Sector KPIs (no protagonist disclosure here, so qualitative): end-to-end speed (Nexus target <60s), all-in cost % (the remittance metric above), reachability (# of linked IPSes / corridors), and compliance latency (seconds-to-screen on irrevocable settlement). FedNow scores on none of the cross-border KPIs yet — it improves only the U.S. leg.
- **Key players / basis of competition (architecture, not price):**
  - **BIS Project Nexus** — the genuinely cross-border-native model: multilateral interlinking of domestic IPSes (UPI, FAST, PromptPay, PESONet, DuitNow), Nexus Scheme Organisation home-jurisdictioned in Singapore (MAS oversight), targeting go-live across the five founding countries (India, Malaysia, Philippines, Singapore, Thailand; Indonesia joined) in 2026, <60s end-to-end (per BIS / MAS, 2024 blueprint; 2026 live-implementation work). Architecturally ahead of FedNow's proposal.
  - **The Clearing House RTP** — building cross-border; **domestic-correspondent-bank capability targeted ~September 2026** as the foundation for international RTP "later this year" (per American Banker / ClearingPost, 2026). Notably, TCH's earlier SWIFT IXB cross-border pilot was **paused in 2023** over policy/regulatory hurdles — a direct precedent for the sanctions/AML friction now flagged on FedNow.
  - **Mastercard / TIPS cross-currency** — euro↔Danish krone instant settled via Mastercard Move (2026-06) — closer to true cross-currency-instant than FedNow.
  - **SWIFT** — incumbent international leg; the FedNow proposal feeds it rather than displaces it.
- **Protagonist position:** **catching up / niche**, via path-of-least-resistance (a Reg J tweak, not joining a multilateral scheme). Moat: none cross-border; FedNow's moat is domestic (Fed operator+regulator, fraud API, certifications) and does not extend across the border. (analysis)

**Comps & multiples.**
No valuation/round/TPV attaches to a Fed rulemaking → **trading multiples: no data / not applicable.** Comparison is policy/architecture, not financial.
Internal comps (in-base precedents on cross-border instant interlinking):
- [[Mastercard joins TIPS cross-currency instant payments pilot]] — cross-currency instant, live pilot.
- [[Bank of America to launch cross-border real-time payments service]] — bank-level real-time cross-border via SWIFT/CashPro.
- [[ECB advances cross-border payments link with India and Asia]] — TIPS↔foreign-IPS interlinking under the G20 roadmap (the Nexus-style model FedNow declined).
- [[Mastercard joins TIPS cross-currency instant payments pilot]] / [[Deutsche Bank goes live on Swift consumer payments initiative]] — SWIFT-leg modernization.
Distribution not computed (no comparable financial figures); qualitative comparison only.

**Risk flags.**
1. **Compliance/sanctions on irrevocable settlement (execution + regulatory).** Instant settlement is final in seconds, but receiving institutions get seconds to screen against sanctions/AML lists — the exact reason TCH paused IXB in 2023. → If unresolved, the final rule could be narrow, opt-in, and slow to adopt, blunting any competitive benefit. (Why: irreversibility + speed structurally conflict with screening; this is the sector's hardest constraint, not a FedNow-specific one.)
2. **Disintermediation of the value the Fed touches (margin capture by another layer).** FedNow captures only the commoditized domestic settlement leg; FX + correspondent + compliance keep the ~6% economics. → Even a passed rule may **entrench** SWIFT/correspondent banking inside FedNow rather than displace it — the opposite of the "threat to SWIFT" framing. (Why: value sits at the international leg, which the proposal leaves untouched.)
3. **Competitive timing / falling behind interlinking (strategic).** RTP targets correspondent capability ~Sept 2026 and Nexus targets 2026 go-live, while FedNow is still at comment-stage with no final-rule date. → The U.S. risks remaining the domestic-only outlier as the rest of the world standardizes on interlinking. (Why: path-of-least-resistance Reg J tweak is structurally less ambitious than a multilateral scheme.)

**What this changes (idea-lens).**
Incremental, not a re-rating: the Fed is signaling it won't *block* FedNow from the cross-border value chain, but it is not building a cross-border network — so the disruptive cross-border story stays with **interlinking (Nexus) and stablecoins**, not this rule. (analysis) Falsifiable thesis: if a final FedNow rule passes without a dedicated cross-border message code + phased sanctions-screening framework, adoption will stay near-zero and SWIFT/correspondent banking will be entrenched, not displaced. Trigger to watch: final-rule timing/scope vs. RTP's ~Sept 2026 correspondent go-live and Nexus 2026 live date — whichever ships a working cross-border flow first sets the U.S. competitive baseline.

Sources: https://www.grandviewresearch.com/industry-analysis/cross-border-payments-market-report · https://www.mordorintelligence.com/industry-reports/cross-border-payments-market · https://www.fortunebusinessinsights.com/cross-border-payments-market-110223 · https://remittanceprices.worldbank.org/sites/default/files/2026-04/RPW_main_report_and_annex_Q325.pdf · https://www.bis.org/about/bisih/topics/fmis/nexus.htm · https://www.mas.gov.sg/news/media-releases/2024/project-nexus-completes-comprehensive-blueprint-for-connecting-domestic-ipses-globally · https://www.americanbanker.com/payments/news/rtp-rail-pushes-international-cross-border-real-time-payments · https://www.paymentsdive.com/news/how-one-cross-border-payments-pilot-failed-real-time-stablecoins-rtp/804358/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
