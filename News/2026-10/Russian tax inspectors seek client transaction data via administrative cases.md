---
title: "Russian tax inspectors seek client transaction data via administrative cases"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - industry/banking
  - industry/regtech
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: sb4916fc7
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Russian tax inspectors seek client transaction data via administrative cases

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Налоговые инспекторы пытаются получать сведения об операциях клиентов через административные дела, минуя специальную процедуру налогового контроля, — хотя ещё в прошлом году Верховный суд уже разбирал аналогичный случай и поддержал позицию банка, отказавшегося раскрывать данные. Это был РСХБ. Ассоциация российских банков заявляет о росте числа нестандартных запросов с лета этого года, называет практику «атакующей позицией» ФНС и уже направила обращения в налоговую службу и Банк России. ЦБ обещает изучить ситуацию. Публичной позиции ФНС по претензиям банков пока нет. В чём принципиальная разница двух процедур ⬛️ Статья 86 НК, обычная процедура: налоговая получает банковские данные по предусмотренным законом основаниям: например, при налоговой проверке или истребовании документов по статье 93.1 НК. Для получения выписок по счетам обычных физлиц, как правило, необходимо согласование руководителя вышестоящего налогового органа или уполномоченного руководства ФНС. ⬛️ Статья 26.10 КоАП,

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Russian tax inspectors seek client transaction data via administrative cases
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
The Association of Russian Banks (ARB/АРБ) has formally complained to the Federal Tax Service (FNS/ФНС) and the Bank of Russia that, since summer 2026, tax inspectors are increasingly demanding bank-secrecy-protected client transaction data (account statements, operation details) via **administrative-offence proceedings under Art. 26.10 of the Administrative Code (КоАП)**, instead of the dedicated tax-control route under **Art. 86 / 93.1 of the Tax Code (НК)**. (Reported by Kommersant 2026-10-18, Fontanka 2026-10-18; ARB sent letters to FNS and CBR.)

**Why this matters — the mechanism delta (the core red-team point):**
- **Art. 86 НК (the lawful channel)** is gated: the bank data request must rest on a predicate (an ongoing tax audit, or a document demand under Art. 93.1 tied to a specific taxpayer/transaction). Crucially, for statements on **ordinary individuals'** accounts it typically requires sign-off from the head of a *superior* tax body or authorised FNS leadership. Narrow scope, named subject, paper trail.
- **Art. 26.10 КоАП** (demand for evidence in an administrative case) has **no such predicate or escalation gate** — any official conducting an administrative matter can request "evidence." Tax inspectors are allegedly using it as a side-door to pull client transaction data that Art. 86 would restrict.
- So the story is not "FNS got new powers." It is **FNS re-routing an existing data appetite through a weaker-gated statute** to bypass the Art. 86 safeguards. The ARB calls it an "attacking stance" (атакующая позиция). That reframes the central question from "can the tax authority see bank data" (yes, long-settled) to **"which procedure governs — one with judicial/internal checks, or one without."**

**What is NOT confirmed (anti-PR):** FNS has issued no public response to the banks' claims; CBR only "promises to study" the situation. No stated number of requests, no named sanctioned bank beyond the precedent case. "Growth since summer 2026" is the ARB's characterisation, not an audited figure.

## [1] Competitors / peers (analogous legal conflicts, not market competitors)
This is a regulation story; "peers" = prior state-vs-bank-secrecy standoffs and analogous data-access grabs:
- **Precedent cited in the item — Supreme Court sided with the bank (RSHB / Rosselkhozbank).** The item states that "last year" (≈2025) the Supreme Court already examined an analogous case and **upheld the bank's refusal to disclose data**, and that bank was RSHB. This is the banks' strongest card: a controlling-court precedent that the KoAP route cannot override Tax Code limits. (External search confirmed the Art. 26.10 framing but could not independently confirm the specific RSHB ruling — treat the RSHB attribution as the primary source's claim, unverified externally.)
- **VS/ФАС precedent (analysis):** In 2019 the Supreme Court **blocked the Federal Antimonopoly Service (ФАС) from compelling bank-secrecy data**, ruling banking-secrecy law enumerates an exhaustive list of who may receive client data (Vedomosti/RG/Pravo.ru, 2019). Same logic transplants directly: a state body cannot invent an access channel outside the enumerated list. This strengthens the banks' position — the KoAP gambit looks like a repeat of a fight the agencies already lost.
- **Position:** Banks are **ahead on case law** (two court wins on the principle) but **behind on operational reality** — they must answer or risk administrative fines, so they are litigating/escalating defensively while the practice spreads.

## [2] Company / institutional fit — why FNS is doing this now
FNS under its digitisation drive has been steadily widening its data reach: 2021 Tax Code amendments already force banks to hand over account documents (passports, beneficial-owner data, signature cards) within 3 days in audit/collection contexts (Bellerage). Structural pressure:
- **From Nov 2025, FNS can collect undisputed individual tax debt out-of-court** (see [[Russia's FNS can intercept loan-repayment funds under new tax collection]]) — an aggressive extrajudicial collection regime whose side-effects (seizing funds meant to repay credit cards) already generated complaints. The Art. 26.10 data-pull fits the same trajectory: **FNS is being pushed toward population-scale, automated enforcement and wants the underlying transaction data to feed it.**
- **Revenue pressure:** aggressive VAT/tax enforcement against fintech lenders is live — see [[FNS hits Lime-zaim with 630M ruble tax claim over payment VAT]]. Harvesting granular client transaction data is the raw material for finding under-reported income (cross-referencing bank flows vs declared income). A pending bill to force banks to share payment data would industrialise this (UNITED24 Media). The KoAP route is the interim workaround while that broader data-sharing regime is not yet law.

## [3] Novelty / value-add / traction (what is really new)
- **New:** the *procedural vehicle* (Art. 26.10 КоАП for client-data fishing) and the *organised banking-sector pushback* (ARB letters to FNS + CBR). Not new: FNS's general right to bank data under Art. 86.
- **Traction of the practice:** per ARB, "non-standard requests" are rising since summer 2026 — a trend, not a one-off. But hard numbers are absent. Traction of the *resistance*: two Supreme Court precedents on the principle (ФАС 2019; the claimed RSHB 2025) give banks real leverage, so the practice may be **legally fragile** even as it spreads operationally.
- **Who captures what:** if the KoAP channel sticks, banking secrecy for ordinary clients is effectively hollowed out — the Art. 86 escalation gate (superior-body sign-off for individuals' statements) becomes bypassable. Second-order: **fintech/neobank clients and SMEs are most exposed**, because their income is transaction-visible (QR/SBP/card acquiring) and they are the natural targets of income-cross-referencing. Banks absorb compliance/legal cost either way.

## [4] What's next / sentiment / risks
- **Next:** CBR "will study"; FNS silent. Likely path — either FNS issues internal guidance walking the practice back (to avoid another Supreme Court loss), or a bank litigates a KoAP refusal to the top court, where the ФАS/RSHB precedents favour the bank. A legislative fix forcing bank payment-data sharing (bill reported by UNITED24) could make the KoAP fight moot by granting the access directly.
- **Counterintuitive second-order (analysis):** the banks are not defending clients out of principle — they are defending against **liability and administrative fines** for either disclosing (breach of secrecy) or refusing (KoAP penalty). They are caught between two sanctions, which is exactly why they escalated to the regulator rather than just complying. The real risk to the system: if tax authorities normalise KoAP as a data door, **every administrative body gains a template** to bypass banking secrecy — the same slippery slope the 2019 ФАС ruling tried to close.
- **Risks to the "fresh/important" read:** no FNS confirmation, no quantified scale, single-source (Финтехно/Kommersant/Fontanka chain). Weight rests on the regulatory-precedent significance, not on a confirmed mass event.

## Sources
- Финтехно (Telegram/MAX): <https://max.ru/fintexno> (aggregated item)
- Kommersant, "ФНС активнее запрашивает банковские данные клиентов по статье 26.10": <https://www.kommersant.ru/doc/9041388>
- Fontanka, 2026-10-18, "Налоговые органы запрашивают у банков данные о клиентах: изменения в процедуре раскрытия": <https://www.fontanka.ru/2026/10/18/76708887/>
- Realnoe Vremya, "Банки пожаловались на рост числа запросов ФНС данных с банковской тайной": <https://realnoevremya.ru/news/408943-banki-pozhalovalis-na-rost-chisla-zaprosov-fns-dannyh-s-bankovskoy-taynoy>
- Vedomosti/RG/Pravo.ru (2019, ФАС precedent): <https://www.vedomosti.ru/finance/articles/2019/01/30/792875-zaschitil-bankovskuyu> ; <https://rg.ru/2019/01/30/verhovnyj-sud-otkazal-fas-v-dostupe-k-bankovskoj-tajne.html> ; <https://pravo.ru/story/208639/>
- Bellerage (2021 FNS bank-data powers): <https://www.bellerage.com/news/russia-s-federal-tax-service-fns-given-access-to-bank-secrecy/>
- UNITED24 Media (bill to force banks to share payment data with FNS): <https://united24media.com/latest-news/russias-new-bill-could-force-banks-to-share-payment-data-with-federal-tax-service-17494>
- Internal: [[Russia's FNS can intercept loan-repayment funds under new tax collection]], [[FNS hits Lime-zaim with 630M ruble tax claim over payment VAT]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is this a new FNS power?** No — FNS has had Art. 86 НК bank-data rights for years (expanded 2021). What's new is the *procedural vehicle* (Art. 26.10 КоАП) and the organised ARB pushback. (answered)
2. **What exactly is the procedural delta?** Art. 86 НК is predicate-gated (audit/Art. 93.1 demand) and, for individuals' statements, needs superior-tax-body sign-off; Art. 26.10 КоАП has no such predicate or escalation gate. KoAP is the weaker-checked side-door. (answered)
3. **Is "growth since summer 2026" a fact or a claim?** ARB's characterisation; no quantified figure disclosed. (open — scale unverified)
4. **Did FNS confirm or deny?** No public FNS position; CBR only "promises to study." Single-direction sourcing. (answered — FNS silent)
5. **Is the RSHB Supreme Court precedent real?** The primary item (Финтехно) asserts a ~2025 Supreme Court ruling upholding RSHB's refusal. External search confirmed the Art. 26.10 framing and a 2019 ФАС precedent but could NOT independently confirm the RSHB ruling. (partly open — treat RSHB as primary-source claim)
6. **Is there a controlling precedent against the agencies?** Yes — 2019 Supreme Court blocked ФАС from compelling bank-secrecy data (exhaustive-list logic). Transplants directly to the FNS/KoAP fight. (answered — strengthens banks)
7. **Who is actually harmed?** Ordinary individuals and SMEs/fintech clients whose transaction flows become visible without the Art. 86 gate; banks face dual-sanction exposure (breach of secrecy vs KoAP fine for refusing). (answered)
8. **Why would FNS route through KoAP rather than fix the law?** The direct bank-payment-data-sharing bill (UNITED24) is not yet law; KoAP is the interim workaround while the data appetite (income cross-referencing, out-of-court collection from Nov 2025) is already live. (answered — analysis)
9. **Does this connect to other FNS enforcement moves?** Yes — same trajectory as out-of-court individual tax collection intercepting loan-repayment funds ([[Russia's FNS can intercept loan-repayment funds under new tax collection]]) and aggressive VAT claims on fintech lenders ([[FNS hits Lime-zaim with 630M ruble tax claim over payment VAT]]). (answered)
10. **Is it a duplicate of those prior FNS notes?** No — different mechanism (data-access procedure vs fund interception vs VAT claim) and a new actor/event (ARB formal complaint, Art. 26.10). Fresh. (answered)
11. **What's the second-order systemic risk?** If KoAP normalises as a banking-secrecy bypass, every administrative body gets a template — reopening the slope the 2019 ФАС ruling tried to close. (open — scenario)
12. **What breaks the banks' position?** A legislative fix (direct data-sharing bill) would grant the access outright and moot the KoAP fight. (answered — analysis)
13. **Is banking secrecy "already dead" as some commentary claims?** Overstated — the legal gate under Art. 86 and two court precedents still stand; the item is about an *attempt* to bypass, not a settled defeat of secrecy. (answered)
14. **Why important despite thin numbers?** It targets the integrity of banking-secrecy procedure for the whole retail/SME client base and tests a precedent with system-wide replication risk — regulatory weight, not event scale. (answered)
15. **Single-source risk?** Chain is Финтехно → Kommersant/Fontanka (2026-10-18); credible but one storyline, FNS side absent. Discount accordingly. (answered)

**Importance: 4/5 — rationale:** High structural significance — a tax authority attempting to hollow out the Art. 86 banking-secrecy gate via a weaker KoAP channel, with system-wide replication risk and an active regulator/association escalation, backed by directly analogous Supreme Court precedent. Docked from 5 because scale is unquantified, FNS has not responded, the RSHB precedent is primary-source-only (externally unconfirmed), and nothing is legally settled yet — it is a live dispute, not a decided outcome.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian bank-secrecy is already heavily eroded for tax purposes: since the March 2021 Tax Code amendments the FNS can demand account documents (passport copies, beneficial-owner data, signature cards) within 3 days, and banks notify the FNS of every account open/close under Art. 86 §1.1 (per Bellerage; per ejournals.eu). The news here is procedural arbitrage, not a new power: inspectors are reportedly using KoAP Art. 26.10 (evidence-gathering in administrative cases) to obtain client-transaction data while bypassing the stricter Art. 86 / Art. 93.1 tax-control safeguards (which, for ordinary individuals' statements, normally require sign-off from a senior tax official). Structure: the Russian banking-data regime is a one-way ratchet toward disclosure — multiple state channels (FNS tax control, FSB, Rosfinmonitoring) can reach the same data under different legal bases, so the compliance barrier for banks/fintechs is not whether to disclose but adjudicating which requests are lawful. Why now: the Association of Russian Banks (ARB) reports a rise in non-standard requests since summer 2026 and calls it an FNS "attacking posture"; it has escalated to both the FNS and the Bank of Russia, and the CB has promised to study the matter (per note; FNS has no public position). This follows a 2025 Supreme Court case where the court backed a bank (RSHB) that refused to disclose (per note).

**Competitive landscape.** The relevant "KPIs" here are compliance, not revenue: request-volume growth, legal-basis dispute rate, and response-SLA exposure (3-day window under Art. 86). Affected set = all Russian credit institutions, with systemically important banks (RSHB, and by extension Sber, VTB, Alfa, T-Bank) the natural test cases given request volume. Basis of "competition" is legal posture: comply-broadly vs challenge-and-refuse. RSHB's 2025 win established that a bank refusing an out-of-procedure request can prevail — a precedent that lowers the cost of pushback and is likely why ARB is now litigating the channel question collectively rather than per-bank (analysis). Position: banks are on the defensive/reactive side; the FNS holds process initiative, but the Supreme Court precedent plus ARB+CB escalation shifts leverage back toward banks on this specific KoAP channel.

**Comps & multiples.** No valuation/deal in this item — it is a regulatory-process story, so trading multiples are N/A ("no data"). Internal comps (direction of the Russian state-data-access trend):
- [[Russia rewrites payment-blocking rules in digital currency bill]] — state widening of payment/data-control levers.
- [[Russian Duma backs liability rules for crypto violations]] — parallel tightening of enforcement reach over financial activity.
Distribution not computed — qualitative comparison only. All three (this item + the two above) point the same way: expanding state access/enforcement surface, higher compliance overhead, no offsetting monetisation for banks.

**Risk flags.**
1. Compliance cost / legal-uncertainty burden: banks must now triage each request's legal basis (Art. 86 vs KoAP 26.10) under a 3-day SLA, raising legal/ops cost and wrong-call liability — scales with request volume ARB says is already rising. Second-order: larger legal teams, slower responses, friction with the FNS.
2. Client-privacy / de-banking erosion: if the KoAP channel is accepted, effective bank-secrecy protection for ordinary clients narrows further (bypassing the senior-official sign-off safeguard), weakening the deposit-trust proposition; second-order: marginal push toward cash / informal rails.
3. Precedent/arbitration risk: the dispute is unresolved (FNS silent, CB only "studying"); an adverse ruling or FNS doubling-down would institutionalise a lower-friction data-extraction path for the whole sector — a systemic, not single-bank, exposure.

**What this changes (idea-lens).** This is a boundary fight over which legal door the state uses to reach bank data, not whether it can (analysis). Falsifiable thesis: the CB/ARB escalation plus the 2025 Supreme Court precedent will force the FNS back to the Art. 86 procedure or an explicit rule, re-closing the KoAP gap. Trigger to watch: a public FNS position, a CB methodological letter, or a fresh court ruling on a KoAP-26.10 bank request — any of these resolves the channel; continued FNS silence amid rising requests would falsify the thesis and signal the workaround is becoming entrenched.

Sources: https://www.bellerage.com/news/russia-s-federal-tax-service-fns-given-access-to-bank-secrecy/ · https://ejournals.eu/en/journal/financial-law-review/article/permissible-restrictions-of-bank-secrecy-for-tax-control-purposes-in-the-legal-system-of-the-russian-federation · https://www.kucoin.com/blog/russians-tax-service-to-receive-device-data-for-digital-ruble-transactions-what-will-change-from-july-1-2027 · https://max.ru/fintexno
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
