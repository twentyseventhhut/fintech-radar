---
title: "Russia rewrites payment-blocking rules in digital currency bill"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - industry/crypto
  - industry/regtech
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s1de55299
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Russia rewrites payment-blocking rules in digital currency bill

> [!info] 2026-07-17 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Ещё один апдейт законопроекта «О цифровой валюте и цифровых правах» ко второму чтению. Комитет Госдумы по финансовому рынку существенно переписал механизм блокировки платежей, связанных с нелегальным оборотом криптовалют. В первой редакции предполагалось создать два публичных государственных перечня: нелегальных организаторов оборота криптовалют и иностранных платёжных сервисов, которые их обслуживают. Тем, кто в них попадёт, банки, платёжные агенты, операторы связи, почта и участники платформы цифрового рубля должны были автоматически отказывать в переводах. В новой редакции списки полностью убрали, а круг обязанных участников сузили, оставив только банки. Что изменилось ▶️ Банки будут сами определять, что получатель организует оборот криптовалют без необходимого статуса, признать его неуполномоченным получателем и отказывать в переводе. ▶️ Сведения о неуполномоченных получателях банки будут передавать в ЦБ. ▶️ Регулятор будет сообщать банкам об иностранных платёжных сервисах, об

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Russia rewrites payment-blocking rules in digital currency bill
_Analytical notes (not a post). Importance: 3/5._

FRESHNESS: **fresh** — a DISTINCT second-reading amendment to bill №1194918-8, not a duplicate of the three adjacent RU-crypto notes: [[Russia to allow stablecoins under digital currency bill amendments]] (07-15, qualified-investor foreign-stablecoin access + new legal definitions), [[Russia adds crypto cross-border rules to trade settlement bill]] (07-09, Rosfinmonitoring 10m-RUB auto-feed + 60k travel-rule + BoR veto over banks), [[Russian Duma backs liability rules for crypto violations]] (07-09, criminal-code article + СК/ФСБ jurisdiction). THIS note is the **payment-blocking / "unauthorized recipient" clause** — a different provision of the same bill, same second reading.

## [0] What exactly happened (de-PR'd)

Preparing bill **№1194918-8 "О цифровой валюте и цифровых правах"** for its **second reading**, the State Duma Committee on the Financial Market (chair Anatoly Aksakov) **rewrote the mechanism for blocking payments tied to illegal crypto circulation** (Vedomosti + Interfax, 16.07.2026). The delta vs the first-reading text:

- **First reading:** create TWO public state registries — (1) illegal organizers of crypto circulation and (2) foreign payment services serving them. A broad set of obligated participants — **banks, payment agents, telecom operators, post, and digital-ruble platform participants** — had to **automatically refuse** transfers to listed parties.
- **Second reading (the change):**
  - **Both registries REMOVED entirely.** No more central lists.
  - **Obligated parties NARROWED to banks only** (credit organizations, foreign-bank branches, card issuers). Payment agents, telecoms, post, and the digital-ruble platform are **dropped**.
  - **New concept "неуполномоченный получатель" (unauthorized recipient):** the **bank itself** decides, on its **own suspicion / internal documents**, that a recipient organizes crypto circulation without the required status, deems them unauthorized, and refuses the transfer.
  - **Reporting to CBR:** banks report suspected unauthorized recipients to the Bank of Russia; the **CBR informs banks about foreign payment services** servicing such transfers (a one-way feedback loop, only for foreign services).
  - Carve-outs preserved: transfers under foreign-trade contracts and via legal/authorized market participants remain allowed.

**Why structured this way / what it reveals — the crux.** The headline reads like "Russia softens crypto-blocking," but the real move is a **shift from a central-list regime to bank-side discretion** — and that is the opposite direction from Russia's own anti-fraud plumbing, where banks act on a **CBR-maintained fraud/dropper database** with a mandatory cooling-off freeze (161-ФЗ / 176-ФЗ, 2024–25). Here the statute **sets no criteria and does not even mandate the CBR to set them** (Interfax) — over/under-blocking risk is pushed entirely onto banks. So the de-PR'd reading is not "lighter regulation" but **"unfunded discretion":** the state offloads the hard classification problem (who is an illegal crypto organizer?) onto ~each bank's compliance desk while keeping the CBR reporting feed. `(analysis)`

**Why they dropped the registries (1 level deeper):** two public state lists of "illegal crypto organizers + the foreign services serving them" would have been (a) slow to maintain, (b) a published sanctions-evasion map (naming the exact foreign rails that work), and (c) legally fragile (blacklisting foreign entities by decree). Bank-side "unauthorized recipient" judgment avoids all three — no published list to game, no due-process target, and the surveillance still flows to the CBR. `(analysis/hypothesis)`

**Legislative status (skeptical flag):** NOT law. As of 16.07.2026 this is second-reading committee text; the plenary vote was tentatively **21.07.2026** and the session must close by ~27.07. Russian digital-asset dates routinely slip (the whole bill effective 01.09.2026; the blocking provision reportedly phased to ~01.07.2027 — per-provision date table unverified). Treat as an in-progress step.

## [1] Competitors / peers (comparable blocking regimes)

The relevant comparison is **transfer-blocking mechanism design**, not crypto policy per se:
- **Russia's OWN anti-fraud regime (161-ФЗ / 176-ФЗ, 2024–25):** banks block/freeze transfers to recipients on the **CBR fraud database**, with a 2-day cooling-off and bank liability for refund if they ignore the list; droppers on the list are capped at ₽100k/mo. This is **list-driven** — the exact opposite of the new crypto clause's **discretion-driven** model. The state runs *both* patterns simultaneously. `(analysis)`
- **EU / FATF travel-rule model:** obligated VASPs/PSPs screen against **sanctions lists** and file SARs — again list-anchored, with the state supplying the list. Russia's "you figure out who's an illegal crypto organizer" has no clean Western parallel.
- **US §1960 / OFAC SDN:** blocking is against a **published designation list**; discretion sits with the regulator, not the transmitting bank.

**Why the lay of the land is this way (2nd-order):** most jurisdictions centralize the *classification* (the state names who to block) and decentralize only *execution*. Russia here decentralizes **classification itself** to banks. The likely second-order effect is **defensive over-blocking**: with criminal liability for illegal crypto circulation arriving 01.07.2027 ([[Russian Duma backs liability rules for crypto violations]]) and no safe-harbor criteria, banks will rationally refuse anything ambiguous, pushing grey flow toward P2P/OTC and non-bank rails — which were **just exempted** from the obligation. That is a structural gap: narrowing the duty to banks only means the phased-out non-bank channels are precisely where blocked flow can migrate. `(analysis)`

## [2] Company/institution history / fit

Fits the CBR/MinFin "legalise → license → surveil → penalise" arc the corpus tracks:
- **09.2024** crypto EPR for cross-border trade; **11.2024** mining legalized.
- **01.2026** digital ruble live for federal budget; retail mass rollout also slated **01.09.2026** ([[Bank of Russia tests digital ruble for deposits and credit]], [[Финтехно Digital ruble could add 423bn rubles to economy]]).
- **21.04.2026** umbrella bill №1194918-8 first reading (327–13).
- **09.07.2026** cross-border AML thresholds ([[Russia adds crypto cross-border rules to trade settlement bill]]) + criminal-liability package ([[Russian Duma backs liability rules for crypto violations]]).
- **15.07.2026** qualified-investor foreign-stablecoin clause ([[Russia to allow stablecoins under digital currency bill amendments]]).
- **16.07.2026** THIS payment-blocking rewrite.

**Why the state acts this way.** A monetary-sovereignty hawk building a **licensed, monitorable, state-bank-centric** crypto perimeter. Every second-reading tweak concentrates control and flow into the CBR-registered banks (Sber/VTB/T-Bank/Alfa — see [[Финтехно Sber plans full crypto operations under new law]], [[Alfa-Bank plans own crypto depositary after peers]]). Narrowing the blocking duty to **banks only** is consistent: banks are the entities the state already licenses and can hold liable, so making them the sole gatekeepers keeps enforcement inside the controllable perimeter. **Notably, the digital-ruble platform was in the first-reading obligated list and got DROPPED** — the CBDC and the crypto-blocking regime now run on separate tracks, worth flagging since they were briefly coupled. `(analysis)`

## [3] Novelty / value-add / traction

**Genuinely new vs corpus:** YES. The three adjacent July notes cover *different clauses* of the same bill (stablecoin definitions, Rosfinmon thresholds/travel rule/BoR veto, criminal liability). The **payment-blocking mechanism** — registries → bank-discretion "unauthorized recipient" — is a **distinct provision**, first reported 16.07.2026. Not a reprint.

**Traction = zero, by construction.** Second-reading committee text only; no vote confirmed, effective date pushed to ~2027 for this provision, no bank has implemented anything. The value is **signal + mechanism design**, not adoption.

**Who captures the value / what breaks it (1 level deeper).** By removing lists and loading discretion onto banks, the state (a) avoids maintaining/publishing a blacklist, (b) keeps the CBR reporting feed, and (c) offloads legal/operational risk to banks. Banks capture the *burden*, not value; the CBR captures *visibility*. What breaks the design: the **absence of statutory or CBR criteria** — without a safe harbor, banks either over-block (killing legitimate ambiguous transfers, e.g. borderline OTC) or under-block (liability exposure from 2027), and there is no clean equilibrium. The economically meaningful crypto flows (the ~$11bn/yr foreign-trade channel documented in [[Russia adds crypto cross-border rules to trade settlement bill]]) are explicitly **exempted**, so this clause targets the *domestic illegal-organizer* fringe, not the big sanctioned-trade rail. `(analysis)`

## [4] What's next / market sentiment

- **Path:** 2nd reading (target ~21.07.2026, session ends ~27.07) → 3rd → Federation Council → signature. Whole law effective 01.09.2026; blocking provision reportedly phased to ~01.07.2027 (per-provision date table **open**).
- **Watch:** (1) whether the vote happened and the bank-discretion language survived unchanged; (2) whether the CBR issues *any* classification guidance despite the statute not requiring it (the key soft spot); (3) whether the digital-ruble platform stays out of the obligated set; (4) interaction with the 2027 criminal liability, which raises banks' incentive to over-block.
- **Risks / silence:** no criteria, no safe harbor, no due-process route for a wrongly-flagged "unauthorized recipient," no stated appeal path.

**Why the market goes this way / counterintuitive 2nd-order.** The intuitive read — "Russia softened crypto-blocking by scrapping the blacklists" — is misleading. The sharper read: replacing a **published, contestable list** with **unreviewable bank discretion + CBR reporting** is *harder* on ambiguous recipients, not softer, because banks facing 2027 criminal liability and zero safe-harbor will **default to refusal**. Counterintuitively, deregulating the *mechanism* (no lists) can tighten the *outcome* (more defensive blocking) — while the non-bank rails just exempted become the leakage path. `(analysis)`

## Sources
- Финтехно (max.ru/fintexno), 17.07.2026 — source note.
- Vedomosti, 16.07.2026: vedomosti.ru/finance/articles/2026/07/16/1214389-zakona-o-kriptovalyutah
- Interfax, 16.07.2026 (blocking rewrite): interfax.ru/business/1103769
- Interfax, 15.07.2026 (stablecoin amendment, distinct): interfax.ru/business/1103384
- Draft law №1194918-8: sozd.duma.gov.ru/bill/1194918-8; RIA first reading 21.04.2026: ria.ru/20260421/gosduma-2088173297.html
- CBR digital-ruble mass rollout 01.09.2026: cbr.ru/press/event/?id=25772
- Anti-fraud/dropper precedent (161-ФЗ/176-ФЗ): rbc.ru/finances/15/05/2025/68247f309a79479d76c3a5ec
- Internal: [[Russia to allow stablecoins under digital currency bill amendments]], [[Russia adds crypto cross-border rules to trade settlement bill]], [[Russian Duma backs liability rules for crypto violations]], [[Bank of Russia tests digital ruble for deposits and credit]], [[Финтехно Digital ruble could add 423bn rubles to economy]], [[Финтехно Sber plans full crypto operations under new law]], [[Alfa-Bank plans own crypto depositary after peers]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team questions

1. **Is this a DUPLICATE of the 07-15 stablecoin note?** No — **fresh**. [[Russia to allow stablecoins under digital currency bill amendments]] (Interfax 15.07) covers the *qualified-investor foreign-stablecoin access + two new legal definitions* clause. THIS (Vedomosti/Interfax 16.07) is the *payment-blocking / "unauthorized recipient"* clause. Same bill №1194918-8, same second reading, **different amendment**. (confirmed)

2. **Duplicate of the 07-09 cross-border note?** No. [[Russia adds crypto cross-border rules to trade settlement bill]] covers Rosfinmonitoring 10m-RUB auto-feed, the 100k→60k travel-rule cut, and BoR veto extended to banks — a *different provision*. Related, not same event. (confirmed)

3. **Duplicate of the 07-09 liability note?** No. [[Russian Duma backs liability rules for crypto violations]] is the criminal-code article + СК/ФСБ jurisdiction. Distinct clause. (confirmed)

4. **Is it law?** No — second-reading committee text as of 16.07.2026; plenary vote tentatively 21.07, session ends ~27.07. Not enacted. (confirmed)

5. **What exactly changed in the blocking mechanism?** Two public registries removed; obligated parties narrowed from {banks, payment agents, telecoms, post, digital-ruble platform} to **banks only**; new "unauthorized recipient" concept decided by the bank's own suspicion; banks report to CBR; CBR informs banks of foreign payment services. (confirmed via Vedomosti + Interfax, two independent outlets)

6. **Is this "softer" regulation, as the headline implies?** Ambiguous → likely **harder in outcome**. Removing a published, contestable blacklist and substituting unreviewable bank discretion, with no statutory criteria and 2027 criminal liability looming, incentivizes **defensive over-blocking**. De-PR: not a liberalization. (analysis)

7. **Does the statute set blocking criteria?** No — and it does **not even task the CBR** to set them (Interfax). Classification risk sits entirely on banks. This is the single most important soft spot. (confirmed)

8. **Why remove the registries?** Hypothesis: two published state lists would be a sanctions-evasion map (naming working foreign rails), slow to maintain, and legally fragile. Bank-side discretion avoids all three while keeping the CBR feed. (hypothesis)

9. **Prior art / what already did the same?** Russia's own anti-fraud regime (161-ФЗ/176-ФЗ, 2024–25) blocks transfers to recipients on a **CBR fraud/dropper database** with cooling-off + bank refund liability. That is **list-driven** — the opposite pattern. So this is NOT an extension of prior art; it's a deliberately different design. (confirmed)

10. **Who is exempted, and does that create leakage?** Payment agents, telecoms, post, and the digital-ruble platform are dropped from the duty. Since only banks must block, grey flow can migrate to the exempted non-bank rails / P2P/OTC — a structural gap. (analysis)

11. **Why was the digital-ruble platform dropped from the obligated list?** It was in the first-reading version and removed. Effect: the CBDC rollout (mass launch 01.09.2026) and the crypto-blocking regime now run on separate tracks. Rationale not stated in sources. (open)

12. **Does this touch the big sanctioned-trade flow?** No — foreign-trade-contract transfers and authorized market participants are explicitly carved out. This clause targets the *domestic illegal-organizer* fringe, not the ~$11bn/yr cross-border channel. (confirmed)

13. **Any traction/adoption?** None — bill stage, blocking provision phased to ~01.07.2027, no bank implementation. Signal, not action. (confirmed)

14. **Did the 21.07 second-reading vote actually happen and survive unchanged?** Reporting is pre-vote (16.07). Not confirmed. (open)

15. **Exact per-provision effective-date table?** Whole law 01.09.2026; blocking provision cited ~01.07.2027 by two sources but the full per-clause table is unverified against final text. (open)

Importance: 3/5 — A genuinely fresh, distinct second-reading amendment to the most-watched RU crypto bill, with a real mechanism-design story (central-list regime → bank-discretion "unauthorized recipient" + CBR reporting) whose de-PR'd read is *tighter*, not looser. Capped below 4 because: (a) not law — second-reading committee text, vote/effective date unconfirmed and slippage-prone; (b) the economically meaningful cross-border flow is explicitly exempted, so this targets a domestic fringe; (c) it is one clause in a fast-moving arc already covered by three adjacent notes, so incremental. It would rise to 4/5 if the vote passes with the bank-discretion language intact and the CBR declines to issue classification criteria (making defensive over-blocking the operative outcome).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: Russia crypto-payment regulation / AML rails, layered on the mandatory digital-ruble rollout. Structure is state-consolidated: the Bank of Russia sits at the top as licensor, blacklist-distributor and transaction-veto holder, with commercial banks as the compliance choke-point. The core bill "On Digital Currency and Digital Rights" passed first reading 21 Apr 2026, and its Financial-Market Committee approved the second-reading text; entry into force was pushed from 1 Jul to 1 Sep 2026, with the harshest norms (mandatory licensed intermediaries, criminal liability) deferred to 1 Jul 2027 (per Vedomosti/Interfax, via cryptonomist/cryptopolitan, as of Jul 2026). "Why now": the September deadline forces a settled text, and the same window mandates digital-ruble support for 12 systemically important banks plus retailers with revenue above ₽120m (per Bank of Russia, via cbr.ru/tftc, as of Jul 2026) — so blocking rules and the CBDC platform go live together. Domestic crypto payments stay banned; the rouble remains the sole legal tender.

**Competitive landscape.** No commercial protagonist here — this is a rulemaking event whose "customers" are the obligated intermediaries. What changed at second reading: the two public state registries (illegal crypto-circulation organisers + foreign payment services serving them) were scrapped; the circle of obligated parties narrowed from banks + payment agents + telecoms + post + digital-ruble platform participants down to banks only. Banks must now self-identify an "unauthorised recipient" organising crypto turnover without licence, refuse the transfer, and report to the CBR; the CBR feeds banks data on foreign payment services. Sector KPI that matters: false-positive/refusal rate and per-transfer compliance cost, now pushed onto banks. In-base regulatory comps clustering into the same July second-reading package: [[Russia adds crypto cross-border rules to trade settlement bill]] (Rosfinmonitoring auto-reporting ≥₽10m; data-transfer threshold cut ₽100k→₽60k; CBR veto extended to credit institutions), [[Russian Duma backs liability rules for crypto violations]] (admin + criminal track, Investigative Committee/FSB, deferred to 1 Jul 2027), [[Russia advances plan to add cooling-off period on crypto transfers]] (withdrawal cooling-off on depositary wallets), [[Russia to allow stablecoins under digital currency bill amendments]] (USDT/USDC for qualified investors from 1 Sep 2026), [[Bank of Russia tests digital ruble for deposits and credit]], [[Sberbank plans crypto wallet and custody service by December]].

**Comps & multiples.** No valuation/round/deal and no traded security — this is a regulatory note. Trading-comp multiples: not applicable. Internal comparison is qualitative across the wikilinks above: the pattern is a move from centralised state blacklists toward decentralised, bank-executed determination + CBR data-feed, mirroring the shift in the cross-border bill from NFO-only to credit-institution CBR veto. Distribution not computed (no numeric comps).

**Risk flags.**
1. Compliance-liability transfer onto banks — removing the state registries shifts the legal judgment ("is this recipient an unlicensed crypto organiser?") to each bank, with no safe-harbour list. Second-order: over-blocking of legitimate transfers, higher false-positive/dispute cost, and litigation exposure when a bank misclassifies a payee.
2. Rails dependence + circumvention — banks are the sole choke-point now (agents/telecoms/post/CBDC-platform dropped), so refused flows migrate to P2P, cash, foreign services and stablecoins that quals may legally buy from 1 Sep ([[Russia to allow stablecoins under digital currency bill amendments]]); enforcement narrows to one layer that users can route around.
3. Regulatory-timeline / discretion risk — text still mutating at second reading with a hard 1 Sep in-force date and criminal norms deferred to 2027; the CBR's discretionary transaction-veto (extended to credit institutions in the sister bill) concentrates unpriced regulatory power over specific counterparties.

**What this changes (idea-lens).** For the sector, this de-centralises AML enforcement onto banks while the CBR keeps the data-feed and veto — cheaper for the state to run, costlier and riskier for banks to operate (analysis). Falsifiable thesis: if the final 1 Sep text keeps banks as sole determiner without a safe-harbour registry, expect rising refusal/dispute volumes and continued crypto-flow migration to stablecoins/foreign rails within 2-3 quarters. What breaks it: reinstatement of an official list or a CBR safe-harbour at third reading, which would move liability back to the state.

Sources: https://www.vedomosti.ru/finance/articles/2026/07/16/1214389-zakona-o-kriptovalyutah · https://en.cryptonomist.ch/2026/05/22/russia-crypto-regulation-bill-trading-payments-ban/ · https://www.cryptopolitan.com/russia-to-ease-crypto-payments-ban/ · https://cbr.ru/eng/press/event/?id=25774 · https://www.tftc.io/russia-digital-ruble-mandatory-rollout-september-2026 · https://www.interfax.ru/russia/1092437
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
