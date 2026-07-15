---
title: "Russia's Mincifry drafts scam-victim compensation rules"
date: 2026-07-15
retrieved: 2026-07-15
tags:
  - industry/fraud-risk
  - industry/banking
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s93a7a940
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Russia's Mincifry drafts scam-victim compensation rules

> [!info] 2026-07-15 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Минцифры разработало порядок компенсации жертвам мошенников — и он заметно ближе к позиции банковского сообщества, чем операторов связи. При этом документ в целом защищает обе отрасли от автоматической ответственности: клиент получит деньги только если удастся установить конкретный сбой банка или оператора. Схема выглядит так: клиент обращается в полицию → получает талон-уведомление → подаёт заявление в свой банк → банк проверяет собственные действия → если банк считает, что всё сделал правильно, передаёт дело оператору → оператор проверяет себя → при несогласии материалы могут пройти контрольную сверку через ГИС «Антифрод». При положительном решении деньги должны вернуть за 30 дней, при трансграничном переводе — за 60. Если обе организации формально выполнили требования — ущерб остаётся на клиенте. Похожую по смыслу модель год назад предлагал Национальный совет финансового рынка, и операторы выступали против. ▶️ По процедуре банк занимает более сильную позицию: становится входной т

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Russia's Mincifry drafts scam-victim compensation rules
_Analytical notes (not a post). Importance: 3/5._

**FRESHNESS / DUPLICATE VERDICT: FRESH.** This is the actual draft government decree ("постановление правительства", dubbed "Antifraud 2.0"), published by Mincifry ~2026-07-15 for public consultation (regulation.gov.ru, until ~2026-07-29; effect 1 Mar 2027 if adopted). It implements framework law **No. 210-ФЗ** (Duma 9 Jun 2026; signed 26 Jun 2026). This is NOT a duplicate but the concrete follow-up to the corpus's [[Russian central bank proposes Gosuslugi fraud-victim support service]] (s6f735ffd, 2026-06-25) — there the CBR *proposed a victim-navigation portal and forwarded the idea to Mincifry*; here Mincifry publishes the *actual liability-allocation rules*. Proposal → drafted rules is a genuine new development. Related but distinct corpus items: [[Brazil judiciary expands bank and fintech fraud liability]] (comparable liability-expansion, other jurisdiction) and [[Forbes Russian SMBs lose over 2bn rubles yearly on missed calls]] (adjacent telecom-loss theme).

## [0] What exactly happened (de-PR'd)
- Mincifry published a **draft decree** setting a **fault-based** ("whoever erred, pays") procedure to compensate victims of phone/online fraud. Confirmed mechanism: victim → police report + **notification slip (талон-уведомление)** → files claim **with own bank within 10 working days** → **bank self-checks (~5 wd)**; if the bank could have blocked the suspicious op and didn't → **bank pays**. If the bank finds no fault → case **forwarded to the telecom operator** (~3 wd to identify the number, then reviews calls/SMS in the ~4h before the transfer); if the operator let a blacklisted/fraud number through → **operator pays**. Victim must supply the **criminal-case initiation order** within 30 days. On a positive decision: **refund in 30 days (60 cross-border)**. If **both institutions formally complied → the loss stays with the client**.
- **Why structured this way / what it reveals.** The decree is **liability-by-fault, not automatic reimbursement**. That design does two things: (1) it protects *both* industries from blanket payout obligations (the news's own framing) — the burden of proving a specific bank or operator "failure" is front-loaded onto the already-robbed victim (police slip + criminal case + 10-day deadline + document set); (2) despite the "neutral" framing, the substance resolves the year-long dispute **against telecom operators** — see [1]. The "both complied → client eats it" outcome is the real quiet part: it preserves the status-quo escape hatch, so the practical refund uplift is uncertain.
- **Anchor numbers (CBR, why weight is moderate).** 2025: fraudsters stole **₽29.3bn** (+6.4% YoY); banks reimbursed only **₽1.73bn = 5.9%** — *down* from ₽2.7bn / **9.9%** in 2024. (analysis) A fault-based scheme that keeps the "both complied" loophole layered on a system where the statutory refund trigger already almost never fires (369-ФЗ payouts were trivial) is unlikely to move that 5.9% dramatically — the novelty is *who* can be on the hook, not a guarantee of payout.

## [1] Competitors / peers (comparable liability regimes)
- **UK APP-fraud mandatory reimbursement (PSR), live 7 Oct 2024:** cost **split 50/50 between sending and receiving PSP**, hard cap **£85k**, refund in **5 working days**, *automatic* (fault-agnostic). Structurally the opposite of Russia: UK allocates between **two payment firms only** (no telecom), pays fast, caps exposure, and does not require the victim to prove institutional fault or file a criminal case.
- **Russia's own back-end:** the existing **369-ФЗ** (in force 25 Jul 2024) already imposes bank refund liability if a transfer went to a **CBR fraud-DB-flagged account** or a mandated **2-day cooling-off** was ignored — but that is *bank-only* and DB-triggered.
- **Australia (Scam Prevention Framework) / Singapore (shared-responsibility):** directionally similar in spreading liability across **banks + telecoms** (unverified on details here) — Russia is not first to pull telecoms in, but is doing so in a large market.
- **Position: catching up on structure, distinctive on scope.** Russia lags the UK on speed/automaticity but is **ahead of the UK on breadth** by making *telecom operators* co-liable for account fraud enabled by missed fraudulent calls/SMS. (analysis) The second-order effect: it shifts anti-fraud incentives onto the *carrier layer* (the SS7/call-origination and SIM-fraud vector), which the payments-only UK model ignores.

## [2] Country / policy fit
- Fits a multi-year Russian anti-fraud build-out: **369-ФЗ** (2024, cooling-off + fraud DB via FinCERT, >1m drop-account records), **loan self-ban** (самозапрет via Gosuslugi, 1 Mar 2025), **mandatory in-app fraud reporting** (1 Oct 2025, which drove reported cases +31%), the **CBR Gosuslugi victim-navigation proposal** (Jun 2026, [[Russian central bank proposes Gosuslugi fraud-victim support service]]), now **210-ФЗ + this decree** (2026–27).
- **Why the state acts this way.** The prevention/blocking stack works (₽13.9tn / 134m ops blocked in 2025), yet **realised losses keep rising and the reimbursement rate is *falling*** (5.9%). That gap is politically toxic (mass retail victims). (analysis) Rather than force banks to pay more automatically (which the bank lobby resists), the state redistributes *blame* — adding telecoms as a second defendant — which is cheaper for banks and lets the government show action without a UK-style unconditional payout mandate.

## [3] Novelty / value-add / traction
- **Genuinely new:** explicit, **fault-based liability on telecom operators** for *bank-account* fraud losses enabled by missed fraudulent calls/SMS — extending beyond the prior rule that limited operator liability to **subscriber-balance (лицевой счёт)** losses. This is the substantive shift and it **tracks the banking-community / НСФР position** (proposed ~12 May 2025, reiterated 27 Jan 2026; operators opposed).
- **Not new:** the bank-side refund duty (already in 369-ФЗ) and the victim-navigation layer (CBR's Gosuslugi idea).
- **Traction: none yet — it is a *draft* in consultation**, effect date 1 Mar 2027. No adoption, no first payouts. (analysis) Value-add is real *only if* the operator-fault test is enforceable in practice; if operators can routinely show "formal compliance," the new liability is nominal and the 5.9% barely moves.

## [4] What's next / market sentiment
- Public consultation to ~29 Jul 2026; potential effect 1 Mar 2027. Expect **telecom-operator pushback** (MTS, MegaFon, VimpelCom/Beeline, T2 were conspicuously silent in the 15 Jul coverage) and lobbying to narrow the "operator fault" definition. Bank lobby broadly wins on structure.
- **Second-order risks/effects.** (analysis) (1) Front-loading friction (police + criminal case + deadlines) plus the "both complied" loophole means the *headline* refund rate may stay near 5.9% — the reform could be more optics than money. (2) Making carriers co-liable creates a real incentive to invest in call-origination / anti-spoofing / SIM-fraud controls — the durable value-add is upstream at the telecom layer, not in the compensation mechanics. (3) Watch whether a **monetary cap** appears (none reported — appears uncapped, unlike UK's £85k) and whether GIS «Антифрод» actually adjudicates bank-vs-operator disputes (the "control cross-check" step is plausible but partly **unverified** in coverage).

## Sources
- Финтехно (primary, aggregated) — https://max.ru/fintexno
- Kommersant, 15 Jul 2026 — https://www.kommersant.ru/doc/8815350
- Vedomosti, 15 Jul 2026 — https://www.vedomosti.ru/society/news/2026/07/15/1213784-poryadok-kompensatsii
- CNews, 15 Jul 2026 — https://www.cnews.ru/news/top/2026-07-15_rossiyane_smogut_kompensirovat
- Izvestia, 15 Jul 2026 — https://iz.ru/2132758/2026-07-15/
- Parlamentskaya Gazeta — https://www.pnp.ru/economics/bank-ili-operator-kto-vernet-dengi-esli-vas-obmanuli-telefonnye-moshenniki.html
- НСФР proposal: RIA 27 Jan 2026 — https://ria.ru/20260127/moshenniki-2070457035.html ; 1prime 12 May 2025 — https://1prime.ru/20250512/moshenniki-857486109.html
- Bank-vs-telecom dispute: RBC 14 Aug 2025 — https://www.rbc.ru/technology_and_media/14/08/2025/689b53bc9a794770fecf20f2
- 210-ФЗ signed 26 Jun 2026 — https://www.klerk.ru/buh/news/697533/
- 369-ФЗ / CBR fraud DB / cooling-off — https://cbr.ru/press/event/?id=18865
- CBR 2025 fraud statistics — https://www.cbr.ru/analytics/ib/operations_survey/2025/
- UK PSR APP reimbursement (7 Oct 2024, £85k) — https://www.psr.org.uk/news-and-updates/latest-news/news/psr-confirms-new-requirements-for-app-fraud-reimbursement/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is this actually new vs 369-ФЗ?** Partly. Bank-side refund duty already exists (369-ФЗ, 2024, DB-triggered). The real novelty is **fault-based liability on *telecom operators* for bank-account losses**, beyond the old subscriber-balance-only rule. — mostly answered.
2. **Does it move the reimbursement rate?** Open/skeptical. Rate *fell* to **5.9% in 2025** (from 9.9%); a fault-based scheme with a "both complied → client eats it" loophole may not lift it materially.
3. **The "both formally complied" loophole — how wide?** Open. This is the escape hatch that preserves the status quo; if operators can routinely demonstrate formal compliance, their new liability is nominal.
4. **Automatic or friction-loaded?** Answered: NOT automatic (unlike UK). Victim must file a police report + notification slip + criminal-case initiation order + meet a 10-day deadline — friction front-loaded onto the robbed party.
5. **Is there a monetary cap?** Open — none reported; **appears uncapped** (vs UK £85k). If uncapped, tail-risk exposure for banks/telecoms is large; worth confirming in final text.
6. **Does GIS «Антифрод» really adjudicate bank-vs-operator disputes?** Partly unverified — the "control cross-check" step is plausible and consistent with the law but not explicitly confirmed in 15 Jul coverage.
7. **Who wins the bank-vs-telecom fight?** Answered: **banks / НСФР** — the fault split extends operator liability to account fraud (missed-call route), the position operators opposed since May 2025.
8. **Why are telecoms silent?** Answered (inference): MTS/MegaFon/VimpelCom/T2 absent from coverage; the "neutral fault-based" framing papers over a resolution *against* them. Expect consultation pushback to narrow "operator fault."
9. **Timeline reality?** Answered: draft in consultation to ~29 Jul 2026; potential effect **1 Mar 2027**; implements 210-ФЗ (signed 26 Jun 2026). No payouts yet — zero traction.
10. **How does it compare internationally?** Answered: UK APP (7 Oct 2024) = 50/50 PSP split, £85k cap, 5-day auto-refund, no telecom. Russia is slower/conditional but broader (pulls in carriers). AU/SG spread liability to telecoms too (details unverified).
11. **Second-order incentive effect?** (analysis) Carrier co-liability could push real investment in anti-spoofing / call-origination / SIM-fraud controls — the durable value-add is upstream at the telecom layer, not the compensation mechanics.
12. **Does it fill a demand-side gap?** Linked to s6f735ffd: CBR admitted victims often don't know they can claim from the bank. This decree + the Gosuslugi navigator address awareness AND liability — but neither guarantees payout.
13. **Downside trigger?** If, a year post-effect, the reimbursement rate stays ~6%, the reform reads as optics; if it jumps, telecoms bore real cost. Watch first-year CBR stats.
14. **Is the 30/60-day refund window enforceable?** Open — depends on how fast criminal-case orders are issued (a known bottleneck); the victim's clock (criminal-case doc in 30 days) may be the binding constraint.
15. **Cross-border (60-day) carve-out — why?** (analysis) Reflects harder recovery/attribution for cross-border transfers; also a likely high-loss, low-recovery segment where neither bank nor operator wants exposure.

**Importance: 3/5 — rationale.** A concrete, market-wide draft decree (not a mere proposal) in a large market, resolving a year-long bank-vs-telecom liability dispute and introducing a genuinely new element (fault-based telecom co-liability for account fraud). Weight is capped below 4 because: it is still a *draft* (effect 1 Mar 2027, zero traction), it is *fault-based not automatic* with a "both complied" loophole layered on a system where the reimbursement rate is a falling 5.9%, and the bank-side duty already existed under 369-ФЗ — so the practical impact on victims is uncertain and the structural novelty (telecom co-liability) is the main reason it clears a 2.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: anti-fraud / scam-liability regulation — the question of *who bears the loss* when a customer is socially-engineered into an authorised transfer. Scale (per CBR, via iz.ru/Interfax/cbr.ru, as of 2025): fraudsters stole ₽27bn from Russians in 2024 (+74% in unauthorised-transfer volume vs 2023) and ₽29.3bn in 2025 (+6.4%), with fraudulent-transaction *count* up ~31% — i.e. losses per case are falling but incidents are exploding, driven by cash-courier and phone/SMS social-engineering schemes (which roughly doubled in 2025). Card-specific fraud was ~₽8.5bn / 822k transactions in 2024. Banks blocked ₽3.5tn of attempted theft in 2025 Q3 alone (per cbr.ru) — the prevention layer is large, but the residual leakage is what this draft re-allocates. Structure: this is a *cost-allocation* rule sitting on top of the existing "Antifraud 2.0" package (amendments to laws On Communications / On Information / On the National Payment System; first reading Feb 2026), with the substantive reimbursement obligations phased to Mar 1 2027 → 2028 (per akm.ru, sostav.ru). Why now: cyberfraud has become a *political* issue in Russia (per Carnegie, Jan 2026), forcing the state to move from "prevention only" to "someone must repay."

**Competitive landscape.** The "players" here are two liability-bearing industries, not product rivals. **Banks** — Sber, T-Bank, VTB, Alfa: they already carry the CBR-mandated block infrastructure and reimburse a slice today (~₽870m returned in an earlier CBR-cited period), so being the *entry point* for claims is procedurally costly but familiar. **Telecoms** — MTS, MegaFon, Beeline (VimpelCom): the call/SMS delivery layer where the social-engineering originates. The draft's key move: the customer files at the *bank* first, the bank self-checks, then hands to the *operator* — so banks win the framing (bank as gatekeeper) but a "no-fault-found by either → loss stays with the customer" carve-out shields *both* industries from automatic liability. This is materially closer to the banking lobby's position than the telecoms', and the National Financial Market Council (NSFR) floated a similar model a year ago that operators opposed. Position: banks ahead on procedure; telecoms exposed on origination but protected by the fault-establishment burden.

**Comps & multiples.** No valuation/multiple event here (regulatory draft, no covered issuer) — comps are *regime/precedent* comps, not trading comps. Internal: [[Russian banks oppose shifting Pochta Rossii rescue costs]] — the closest Russian precedent of the state migrating a cost onto banks via mandated cross-subsidy, and NSFR again arguing for non-mandatory / free anti-fraud messaging; [[Brazil judiciary expands bank and fintech fraud liability]] — a harsher foreign model where courts push liability onto banks/fintechs *even when the customer voluntarily shared credentials* (contrast: Russia's draft explicitly keeps that residual on the customer); [[Hang Seng Bank launches Money Safe fund-locking feature]] — a prevention-side product response to the same scam wave under HKMA guidance. External regime comp: **UK PSR APP-fraud scheme** (live 7 Oct 2024) — mandatory reimbursement up to £85k, cost split **50/50 between sending and receiving PSPs**, refund within 5 business days (per psr.org.uk, Freshfields). Contrast arithmetic: UK = automatic reimbursement, liability split *within* the payments industry (bank↔bank); Russia's draft = *conditional* reimbursement (fault must be proven), liability split *across* industries (bank↔telecom), pay-out in 30 days (60 cross-border). Russia is thus structurally *lighter* on the payer than the UK — no strict-liability, and the customer can end up uncompensated. "no data" on a modelled cost per bank — the fault-test design makes aggregate payouts unforecastable.

**Risk flags.**
1. **Compliance/process cost, not just payout.** Even with the "no automatic liability" shield, banks become the mandatory intake and self-audit point for every claim; at ~460k fraud transactions/quarter the operational load (talon verification, GIS "Antifrod" reconciliation, 30-day SLA) is the real cost — second-order: pass-through into fees/pricing, echoing the Pochta cross-subsidy pattern.
2. **Moral hazard / enforcement gap.** Because reimbursement hinges on proving a *specific* bank or operator failure, both sides are incentivised to document formal compliance rather than actually reduce fraud, and the customer bears the loss when neither is found at fault — weaker deterrent than the UK's strict-liability model, and hard to adjudicate at scale.
3. **Telecom pushback / legislative dilution.** Operators (MTS/MegaFon/Beeline) opposed the earlier NSFR version and are the losers under the bank-as-gatekeeper framing; watch for the origination-liability language to soften at second reading — the Pochta note shows Russian second readings do grant lobby carve-outs.

**What this changes (idea-lens).** `(analysis)` This normalises fraud-loss reimbursement as a *shared* bank+telecom obligation in Russia, but the fault-test design blunts its bite — it is a lighter regime than UK APP or Brazil's court-driven liability. Falsifiable thesis: if the final text keeps the "no-fault-found → customer bears loss" carve-out, the P&L hit to Sber/VTB/Alfa/T-Bank and to MTS/MegaFon/Beeline is modest (process cost, not open-ended payout); the thesis breaks if the Duma strips the fault test toward strict liability (UK-style) at later readings, which would materially re-rate anti-fraud compliance spend across both sectors. Trigger to watch: State Duma second/third reading of the Antifraud 2.0 reimbursement package and the Mar 2027 commencement text.

Sources: https://www.cbr.ru/eng/analytics/ib/operations_survey/2024/ · https://en.iz.ru/en/1841157/2025-02-18/fraudsters-stole-27-billion-rubles-russians-2024 · https://www.cbr.ru/eng/press/event/?id=28094 · https://interfax.com/newsroom/top-stories/110666/ · https://carnegieendowment.org/russia-eurasia/politika/2026/01/russia-cybersecurity-problems?lang=en · https://www.akm.ru/eng/press/from-2026-banks-will-expand-the-list-of-signs-of-fraudulent-transfers/ · https://www.sostav.ru/publication/mintsifry-obyasnilo-kak-budut-kompensirovat-ushcherb-ot-telefonnykh-moshennikov-85274.html · https://www.psr.org.uk/news-and-updates/latest-news/news/psr-confirms-new-requirements-for-app-fraud-reimbursement/ · https://www.freshfields.com/en/our-thinking/briefings/2024/09/authorised-push-payment-fraud-a-new-mandatory-reimbursement-regime-for-uk-psps
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
