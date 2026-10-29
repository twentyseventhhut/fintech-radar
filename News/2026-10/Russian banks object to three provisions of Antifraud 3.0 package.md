---
title: "Russian banks object to three provisions of Antifraud 3.0 package"
date: 2026-10-28
retrieved: 2026-10-29
tags:
  - industry/fraud-risk
  - industry/regtech
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s450062bd
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Russian banks object to three provisions of Antifraud 3.0 package

> [!info] 2026-10-28 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Банки выступили против трёх положений пакета «Антифрод 3.0», Национальный совет финансового рынка направил Минцифры и Банку России замечания. Банки оспаривают: ⚪️ закрытый перечень целей, для которых клиент сможет разрешать обработку персональных данных; ⚪️ запрет на использование агрегаторов для СМС-рассылок; ⚪️ преимущественное использование ЕСИА для удалённой упрощённой идентификации при выдаче электронных средств платежа. Отказ от агрегаторов заставит банки напрямую интегрироваться с операторами связи либо оплачивать агрегацию через одного из них. Для банка, отправляющего 10 млн сообщений в месяц, потеря объёмной скидки может увеличить расходы на 10–20 млн рублей ежемесячно. Вместо единственной идентификации через ЕСИА банки предлагают разрешить сочетание ID банков и операторов, проверку ИНН и СНИЛС и подтверждение физического владения устройством. Минцифры обещает рассмотреть замечания и уточнило, что проект пока не предполагает полного запрета всех альтернатив ЕСИА. Спор по

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)

The National Financial Market Council (NFMC / НСФР, headed by Andrey Emelin) sent Mincifry and the Bank of Russia a formal comment letter objecting to **three** specific provisions of the draft "Antifraud 3.0" package — the third legislative anti-scam bundle, which Mincifry/MVD put out for discussion in autumn 2026 and plan to introduce into the Duma this fall. This is a lobbying/comment-stage intervention, **not** a regulatory decision or a defeat for the banks. The three contested provisions:

1. **Closed (exhaustive) list of purposes for which a client may consent to personal-data processing.** The bill would enumerate the situations in which a citizen can authorize PD processing. NFMC argues an exhaustive "allow-list" blocks risk scoring, tailoring offers to clients, and launching new products; it counter-proposes an **inverted** design — legislate only the situations where processing is *forbidden*, leaving everything else to the client's discretion (a deny-list, not an allow-list).
2. **Ban on using SMS aggregators for bank messaging.** The bill would force credit institutions to contract directly with each telecom operator. Today banks route transactional/notification SMS through aggregators that fan out across operators and negotiate volume discounts. NFMC proposes keeping aggregators but tightening their regulation instead of banning them.
3. **ESIA (Gosuslugi / Единая система идентификации и аутентификации) as the sole channel for remote simplified identification** when issuing electronic means of payment (cards/e-wallets). Banks call ESIA a "monolithic single point of entry": making it the only channel removes their ability to load-balance and manage graceful degradation during peaks/outages. They propose allowing a **combination** of bank + operator IDs, INN/SNILS checks, and proof of physical possession of the device.

**+ Why framed this way / what it reveals.** Note the asymmetry across the three objections: on PD and aggregators banks fight the *economics* (flexibility to monetize data; a direct cost hit), while on ESIA they fight *operational/systemic risk* (concentration, single-point-of-failure). The single hard number in the record — "a bank sending 10M messages/month could see costs rise 10–20M RUB/month if volume discounts disappear" — is bank-sourced and therefore self-serving; treat as an advocacy figure, not an audited one. Mincifry has already softened: it says it will review the comments and clarified the draft does **not currently** contemplate a *full* ban on all ESIA alternatives — i.e. provision (3) is already partly walked back in public, which lowers the real stakes of the headline.

## [1] Competitors / peers (comparable regimes & actors)

- **Domestic lineage:** This sits inside a dense RU anti-fraud stack. See [[Russia's Mincifry drafts scam-victim compensation rules]] (Jul 2026 — the compensation procedure, where NFMC's position again prevailed over telecoms), [[Bank antifraud signals to be shared with digital platforms]] (Oct 2026 — cross-industry signal sharing), and [[Russian Supreme Court tightens rules on scam-linked loan disputes]] (Oct 2026 — courts raising the bar on SMS-code consent). The through-line: who bears liability and who bears the compliance cost of scam prevention — banks vs telecoms vs platforms vs the client.
- **ESIA-as-sole-channel precedent:** NFMC has run this play before — see [[Russia's central bank calls MAX transaction approval premature]] (Mar 2026), where NFMC lobbied CBR *against* mandatory transaction confirmation via MAX and the regulator sided with "premature." NFMC's single-point-of-failure argument against ESIA is the same institutional reflex against state-mandated monochannels.
- **Cross-border comparison (liability vs identity):** Other jurisdictions are pushing the liability lever — [[RBI issues draft directions on bank fraud liability and compensation]] and [[RBI proposes ₹25,000 compensation for small digital fraud losses]] (India), [[Brazil broadens bank and fintech liability for digital fraud]] (judiciary-led). The RU "Antifraud 3.0" package is notable for pushing *identity/data/channel* controls (ESIA, SIM regulation, PD minimization) more than pure loss-reimbursement, so banks' objections here are about input controls, not payout rules.

**+ Why the lay of the land is this way.** Russia's anti-scam policy is being built input-first (control the identity rail, the SIM, the messaging channel) rather than output-first (compensate losses), because the state can mandate state infrastructure (ESIA/Gosuslugi) and telecom rules directly. That is precisely what makes it collide with bank economics: input controls route everyone through state/monopoly chokepoints, which is where banks lose both margin and resilience.

## [2] Company / actor history & fit

NFMC is the standing industry lobby that files exactly this kind of comment letter; doing so is on-mission, not surprising. Its recent track record is mixed-to-favorable: it shaped the scam-victim compensation procedure toward the banks (Jul 2026) and successfully slowed MAX transaction-confirmation (Mar 2026). So this letter is best read as the opening move of a negotiation NFMC has a real chance of winning on points (2) and (3), given Mincifry's conciliatory public response.

**+ Why NFMC acts this way.** Banks' structural interest is to keep identity/data/messaging as *competitive, multi-vendor* surfaces they can optimize. Every provision that routes a function through a single state or monopoly node (ESIA, direct-operator SMS, exhaustive PD-purpose lists) converts a bank cost-and-capability center into a dependency — hence they fight all three on the same underlying principle: preserve optionality and redundancy.

## [3] Novelty / value-add / traction

Genuinely a **new** event: it is the first surfacing of banks' *specific* objections to Antifraud 3.0 (the prior Antifraud 3.0 coverage was about the bill's *contents* — SIM subdealer bans, hosting-provider rules — being readied for the Duma). It is not a reprint of the compensation-rules, signal-sharing, Supreme-Court, or MAX stories, which are different instruments. **Traction = zero on outcomes:** this is a comment letter on a draft that is *not yet introduced* to the Duma; nothing is adopted. The value is as a leading indicator of where the fight lines are (data monetization, SMS cost, identity resilience).

**+ Where the real value / risk sits.** The economically material item is (2) SMS aggregators — a concrete, recurring opex hit banks can quantify (hence the 10–20M RUB/month figure they chose to publicize). (1) PD-purpose list is the strategically material item — an exhaustive allow-list could structurally constrain data-driven product and risk models, which is a far bigger long-run lever than SMS cost, but it is harder to quantify so it gets less headline weight. (3) ESIA is already the least live, given Mincifry's walk-back.

## [4] What's next / sentiment

Status: draft at the **public-discussion / comment stage**; Mincifry/MVD plan to introduce Antifraud 3.0 to the State Duma in autumn 2026. No law number, no effective date, and the text can still change. Mincifry has publicly promised to consider NFMC's comments and has already narrowed the ESIA claim. Expect iterative softening on (2) and (3) and a harder fight on (1).

**+ Second-order read.** The real contest is not "banks vs anti-fraud" (banks support the goal) but **who absorbs the cost and the systemic risk of state-mandated chokepoints.** If ESIA becomes a true monochannel, a single Gosuslugi outage could freeze card issuance sector-wide — an operational-resilience risk the state is implicitly asking banks to underwrite. That reframes the question from "are banks obstructing fraud prevention?" to "is concentrating identity/messaging on state infrastructure trading retail-scam risk for systemic-outage risk?"

## Sources
- Kommersant — НСФР раскритиковал пакет мер по борьбе с мошенничеством «Антифрод 3.0» (kommersant.ru/doc/9062356; /doc/9062106)
- CNews — «Банки восстали против антифрода» (cnews.ru, 2026-10-28)
- Habr news 1100440; RB.ru; cisoclub.ru; www1.ru (2026-10-28); telesputnik.ru
- Comnews / Profile / Parlamentskaya Gazeta (2026-09) — Antifraud 3.0 Duma-introduction timeline & contents
- Primary channel: Финтехно (max.ru/fintexno)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions.** Importance: 3/5.

1. **Is this a real regulatory event or just lobbying noise?** It is a comment letter on a draft bill **not yet introduced** to the Duma. No adoption, no effective date. Weight comes from being a leading indicator, not from any decision. (open outcome)

2. **Is it a duplicate of prior RU anti-fraud notes?** No. Distinct from the Jul-2026 scam-victim compensation procedure, the Oct-2026 cross-industry signal sharing, the Oct-2026 Supreme Court SMS-consent ruling, and the Mar-2026 MAX-confirmation story. Those are different instruments; this is NFMC's first specific objection set to Antifraud 3.0. **Fresh.**

3. **Are the three provisions correctly stated?** Yes, corroborated across Kommersant/CNews/Habr: (1) exhaustive PD-purpose allow-list, (2) ban on SMS aggregators forcing direct operator contracts, (3) ESIA as sole remote simplified-ID channel for issuing electronic means of payment.

4. **Is the "10–20M RUB/month" cost figure independent?** No — it is bank/NFMC-sourced advocacy, scenario-specific (a bank sending 10M SMS/month losing volume discounts). Not audited. Treat as illustrative, directional only.

5. **Which objection is economically largest vs strategically largest?** SMS (2) is the quantifiable recurring opex hit; PD-purpose list (1) is the bigger long-run strategic lever (constrains data-driven risk/product models) but harder to quantify, so under-headlined. ESIA (3) is already the least live.

6. **Has Mincifry actually conceded anything?** Partially — it publicly clarified the draft does **not currently** contemplate a *full* ban on all ESIA alternatives, and promised to review comments. So provision (3)'s headline stakes are already lower than the note's framing suggests.

7. **What is the genuine systemic risk in ESIA-as-monochannel?** Single point of failure: a Gosuslugi/ESIA outage could stall card/e-wallet issuance sector-wide. Banks frame it as resilience/load-balancing, not just cost — a credible argument, not pure self-interest. (analysis)

8. **Does NFMC usually win these fights?** Mixed-to-favorable recent record: shaped the compensation procedure toward banks (Jul 2026); slowed MAX transaction confirmation (Mar 2026). So (2) and (3) have real odds of softening; (1) likely the hardest.

9. **Is the inverted PD proposal (deny-list vs allow-list) material or cosmetic?** Material. An exhaustive allow-list fundamentally limits future data uses; a deny-list preserves default flexibility. This is the structurally important ask even if it gets less press.

10. **Who are the real counterparties with opposing interests?** Telecom operators (SMS routing, who gain if aggregators are banned and banks contract direct), the state identity stack (ESIA/Gosuslugi, which gains mandated traffic), and data-privacy advocates (who favor the exhaustive allow-list). Banks are not fighting "fraud prevention" per se.

11. **Does the package's overall thrust differ from peer jurisdictions?** Yes — RU "Antifraud 3.0" leans on input controls (identity, SIM, messaging, PD minimization) vs India/Brazil's output/liability levers (compensation, broadened bank liability). That is why bank objections here are about inputs, not payout rules.

12. **What's missing / silent?** No law number, no effective date, no clause text in the public record; no independent quantification of consumer-protection benefit vs bank compliance cost; unclear how aggregators would be "regulated more tightly" under NFMC's counter-proposal in peak-load conditions.

13. **What would make this genuinely high-importance?** Duma introduction with provision (1) intact (allow-list), or a firm ESIA-only mandate surviving comment — either would move it from 3/5 toward 4/5. A quiet softening before introduction would confirm it was mostly lobbying theater.

14. **Downside trigger for banks?** If adopted as drafted: recurring SMS opex increase + constrained data models + concentration risk on ESIA. Cumulative, not catastrophic — hence 3/5, not higher.

**Importance: 3/5** — a credible, well-corroborated leading indicator of RU anti-fraud policy fault lines (data monetization, SMS economics, identity resilience), but draft-stage with zero adopted outcomes and Mincifry already conceding on the ESIA point.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is RU payments-security / regtech regulation, not a single issuer. The backdrop: scam/APP fraud in Russia remains large and growing even after two prior anti-fraud packages — fraudsters stole RUB 6.3bn from Russians in Q2 2025, up RUB 1.5bn YoY vs Q2 2024, with the voluntary refund share at only ~5% (per Bank of Russia, via iz.ru, as of 2025). The CBR's July-2024 regime ("Antifraud" wave 1) already forces banks to (i) screen payees against the CBR fraud database, (ii) impose a two-day cooling-off suspension, and (iii) refund within 30 calendar days if they fail to suspend a flagged transfer (per cbr.ru, effective 2024-07-25). Antifraud 3.0 is the third iteration, now pushing into identity (ESIA), personal-data consent scope, and messaging rails. Structure: the compliance burden sits almost entirely on banks (liability + cost), while the state controls the mandated rails (ESIA for identity, direct telco contracts for SMS) — a regulation-driven value-chain shift that concentrates dependence on state/telco infrastructure. "Why now": fraud losses keep rising despite waves 1–2, so the regulator is tightening the perimeter (identity + data + channels) rather than just the transaction layer.

**Competitive landscape.** The "KPIs" here are regulatory-cost KPIs, not market multiples: (i) incremental SMS/notification cost, (ii) remote-onboarding conversion, (iii) refund/liability exposure. Banks (via the NSFR / National Financial Market Council) object to three provisions: a closed list of purposes for which a client can consent to personal-data processing; a ban on SMS aggregators (forcing direct integration with each telco or paying one operator for aggregation); and ESIA as the privileged channel for simplified remote identification when issuing electronic payment instruments (per Kommersant / CNews / Habr, 2026-10-28). Banks counter-propose a combination of bank+operator IDs, INN/SNILS checks, and device-possession proof instead of ESIA-only (per note text, 2026-10-28). Mintsifry says it will review the comments and clarified there is no "total ban" on non-ESIA methods — only a reduction of allowed methods (per rb.ru / CNews, 2026-10-28). Context on the messaging economics: Russia's FAS has previously ordered the four major MNOs (MTS, Beeline, MegaFon, t2) to cut bulk-SMS rates for banks (per Telecompaper), so banks already treat A2P pricing as a regulated cost line — losing aggregator volume discounts directly hits it.

**Comps & multiples.** No valuation/multiple is applicable — this is sector regulation with no deal, round, or traded issuer. Cost arithmetic from the note: a bank sending ~10mn messages/month could see monthly costs rise RUB 10–20mn from losing aggregator volume discounts (per note text) — i.e. roughly RUB 1–2 per message of incremental cost at the margin, consistent with the ~RUB 1–2/message domestic SMS pricing range (per sent.dm, 2025); annualized that is ~RUB 120–240mn per large sender, before any onboarding-conversion loss. Internal comps (regulatory precedents, de-PR'd): [[Russia's central bank calls MAX transaction approval premature]] (CBR cautious on new state-mandated rails, 2026-03), [[Russia orders carriers to disable Apple account payments]] (state tightening payment channels, 2026-03), [[RBI issues draft directions on bank fraud liability and compensation]] (India, bank-borne fraud liability, 2026-03), [[Pix adds tool to recover funds for fraud victims]] (Brazil mandatory refund from Feb-2026, 2025-11), [[Monzo wrongly denied refunds to thousands of fraud victims]] (UK mandatory-reimbursement friction, 2026-02). Cross-jurisdiction pattern: regulators worldwide are shifting scam liability onto banks (UK PSR 50/50 reimbursement, India RBI draft, Brazil Pix MED) — RU's Antifraud track fits this, but is distinctive in also mandating state identity (ESIA) and messaging rails.

**Risk flags.**
- **Single-point-of-failure on state rails.** ESIA-only simplified identification concentrates onboarding on one state system; if ESIA is slow/unavailable (cf. [[Russia's VPN crackdown reportedly triggered major banking outage]], 2026-04), banks lose the ability to issue payment instruments at all — an availability/concentration risk the note's counter-proposal (multi-factor alternatives) is explicitly trying to hedge.
- **Opex step-up with no revenue offset.** Dropping SMS aggregators raises notification cost (RUB 10–20mn/month per large sender per note) — a pure margin hit that smaller banks absorb worse than top-tier ones, widening the cost gap between large incumbents (Sber et al.) and mid/small banks.
- **Data-consent perimeter shrinks model inputs.** A closed list of permitted personal-data-processing purposes can starve banks' own anti-fraud/scoring models of inputs — a second-order risk where an anti-fraud law could degrade banks' own fraud detection and cross-sell, pushing more fraud losses (and refund liability) back onto them.

**What this changes (idea-lens).** (analysis) Antifraud 3.0 marks the shift of RU fraud regulation from the transaction layer (cooling-off, refunds) to the identity + channel layer (who you are, how you're reached). Thesis: the economics move value from bank-chosen vendors (SMS aggregators, alt-ID providers) toward state/telco rails, compressing bank opex flexibility; watch whether Mintsifry softens the ESIA-only and aggregator provisions in the final text (the stated willingness to "review" is the near-term catalyst). Falsifier: if the final law keeps multi-method identification and only bans the transaction-level loopholes, the sector-cost thesis is wrong and this is a routine tightening, not a structural rail shift.

Sources: https://www.cbr.ru/eng/press/event/?id=18866 · https://iz.ru/en/node/1951087 · https://www.kommersant.ru/doc/9062106 · https://www.cnews.ru/news/top/2026-10-28_banki_poshli_protiv_antifroda · https://habr.com/ru/news/1100440/ · https://rb.ru/news/banki-raskritikovali-antifrod-30-popravki-ogranichat-ispolzovanie-personalnyh-dannyh-rassylki-stanut-dorozhe/ · https://www.telecompaper.com/news/russian-operators-ordered-to-cut-bulk-sms-rates-for-banks--1249369 · https://www.sent.dm/resources/russia-sms-pricing
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
