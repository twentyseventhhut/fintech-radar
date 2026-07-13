---
title: "Russia advances plan to add cooling-off period on crypto transfers"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - industry/crypto
  - industry/fraud-risk
  - region/ru
  - type/regulation
sources:
  - https://www.interfax.ru/russia/1092437
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sa553fd67
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Russia advances plan to add cooling-off period on crypto transfers

> [!info] 2026-07-03 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Идея охлаждения криптопереводов, которую ещё в мае озвучил представитель Минфина Дмитрий Фролов, стала конкретнее.

## Первоисточники

### interfax.ru
<https://www.interfax.ru/russia/1092437>
*362 слов · direct*

В РФ введут период охлаждения при выводе средств с криптокошельков цифровых депозитариев
Минфин рассчитывает, что законопроект о криптовалютах пройдет второе чтение в начале июня и третье - до июля
Москва. 28 мая. INTERFAX.RU - Законопроект о регулировании криптовалют предусматривает период охлаждения при выводе средств с адресов-идентификаторов на площадке цифрового депозитария, заявил на круглом столе в Совете Федерации заместитель директора департамента финансовой политики Минфина Дмитрий Фролов.
"Ко второму чтению у нас достаточно четко регулируются правоотношения между органами власти. Например, Счетная палата у нас получает также полномочия при реализации своих функций обращаться к участникам регулируемого оборота криптовалют из числа поднадзорных организаций. Например, у нас изменилась немного модель хранения данных Федеральной налоговой службы об адресах-идентификаторах граждан, снижая тем самым некоторые возможные риски информационной безопасности", - сказал он.
"Предусмотрен период охлаждения при выводе средств с адресов-идентификаторов на площадке цифрового депозитария. На самом деле, действительно, охватить все те точечные изменения, которые сделаны, достаточно сложно. Мы надеемся и целимся вместе с коллегами, что в начале июня мы выйдем на второе чтение в Государственной думе, и до конца июня этот законопроект у нас будет в Государственной думе уже принят", - добавил Фролов.
По его словам, Минфин надеется, что законопроект о налогообложении криптовалют Госдума рассмотрит примерно в такой же срок. При этом проекты законов об административной и уголовной ответственности за незаконный оборот цифровых валют, возможно, будут приняты уже в осеннюю сессию.
Период охлаждения - это мера, направленная на борьбу с мошенничеством. В финансовой сфере она применяется при подозрительных переводах денежных средств, а также в кредитовании. Так, например, банки обязаны выдержать паузу в 4 часа при кредитовании на сумму от 50 тысяч до 200 тысяч рублей и паузу в 48 часов, если сумма кредита превышает 200 тысяч рублей.
Законопроект № 1194918-8 , который устанавливает правовую основу для обращения в России цифровых валют (криптовалют), был принят в первом чтении 21 апреля. Согласно документу, с 1 июля 2026 года граждане и компании смогут легально покупать криптовалюту через лицензированных посредников - обменники из реестра ЦБ, брокеров и доверительных управляющих. Ожидается, что квалифицированные инвесторы смогут приобретать криптоактивы без ограничений, кроме анонимных, а для неквалифицированных инвесторов покупка будет разрешена в пределах 300 тысяч рублей в год через одного посредника. Рассчитываться криптовалютой внутри страны по-прежнему будет запрещено.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Russia advances plan to add cooling-off period on crypto transfers
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
De-PR'd: This is NOT a new law or even a new provision — it is a Minfin official (Dmitry Frolov, deputy head of the Financial Policy Department) confirming, at a Federation Council round table on 28 May 2026, that draft bill No. 1194918-8 ("On Digital Currency / regulating crypto circulation") will contain a **cooling-off period on withdrawals from address-identifiers on the digital-depository platform**. Frolov himself framed it as making "more concrete" an idea he floated back in May — so the [Финтехно] channel's own framing ("became more concrete") is accurate: this is an incremental confirmation of a design detail, not an event.

Concrete facts:
- Mechanism: a mandatory pause before crypto can be withdrawn from the regulated digital-depository custody layer. No exact duration published for crypto; the source only offers an analogy to the existing **consumer-loan cooling-off** (4h for RUB 50k-200k, 48h above RUB 200k, live since 1 Sept 2025).
- It is an **anti-fraud** measure, explicitly modeled on the same social-engineering-scam logic used for loans and suspicious money transfers.
- Timeline claimed by Minfin at the time: 2nd reading "early June", passage "by end of June", with tax bill on a similar track; criminal/administrative-liability bills possibly pushed to the autumn session.
- Base law context: passed 1st reading 21 April 2026; from 1 July 2026, individuals/firms can legally buy crypto via **licensed intermediaries** (CBR-registry exchangers, brokers, trust managers). Qualified investors: no cap except anonymous assets; non-qualified: **RUB 300k/year per intermediary**. Domestic settlement in crypto stays **banned**; cross-border trade use allowed.

**Why structured this way / what it reveals:** The cooling-off period only bites at the **digital-depository → personal-wallet** boundary. That is the entire architectural point of the bill — Russia is deliberately building a **securities-account-style custody chokepoint** (address-identifiers recorded with FNS, Schetnaya Palata oversight) so that the state can see, delay and block flows. The cooling-off is not really a consumer-protection add-on; it is the **enforcement handle** that makes the custodial regime governable (block suspicious withdrawals, freeze scam proceeds, and — second order — deter people from moving assets out of the regulated perimeter into self-custody at all). Frolov's own admission that "it's hard to cover all the point changes" signals the 2nd-reading text is still fluid.

**CRITICAL correction vs the note's implicit "advances" framing:** By early July 2026 the July-1 target had **slipped**. Alexey Yakovlev (director of the same Minfin department) told Interfax the bill is "largely ready" but would **not** be adopted by 1 July; the Duma Financial Market Committee still had to review it "in coming weeks." So the correct read on 2026-07-03 is: cooling-off is a confirmed *design intent*, but the whole bill (and this provision) is **behind schedule**, not "advancing" on time. (fact)

## [1] Competitors / peers (comparable regimes)
This is a regulatory-design item, so "competitors" = other jurisdictions' anti-fraud transaction delays:
- **India / RBI** — [[RBI proposes one-hour delay on high-value digital transfers]] (Apr 2026): 1-hour provisional hold on push payments >RUB-equivalent ~RUB 10k, with whitelist/bypass-after-verification. The closest live analogue in the corpus.
- **UK**: banks may delay suspicious outbound payments up to 72h.
- **Singapore**: 12h cooling-off on high-risk account actions. **Sweden**: bank-led cooling-off/confirmation.
- **Russia's own precedent**: consumer-loan cooling-off (live 1 Sept 2025) and suspicious-transfer pauses under the "Antifraud" package — the direct template Frolov cites.

**Position:** Russia is **catching up / parity**, not leading. Cooling-off periods for fraud are a 2025-26 global wave; Russia is porting a domestic-finance tool onto crypto. **Why the lay of the land is this way (analysis):** every jurisdiction is reacting to the same shift — fraud is now **authorised-push-payment social engineering**, not system breach, so the only lever left is *time* (give the victim a window to cancel). Russia's twist is that it applies this **inside a state-run custody layer** rather than at the bank/PSP edge — a structurally heavier, more surveillance-oriented implementation than India's or the UK's.

## [2] Company / regime history & fit
Russia's crypto trajectory (dated): experimental legal regime & mining legalization 2024 → CBR treats crypto as FX assets → cross-border trade payments legalized in principle ([[Russia to legalize crypto for cross-border trade payments]], Oct 2025) → Sberbank crypto-backed loans ([[Russia's Sberbank plans crypto-backed loans for corporate clients]], Feb 2026) → bill 1st reading Apr 2026 → cooling-off confirmation May 2026 → target July 2026 (now slipping).

**Fit / why the state acts this way (analysis):** Two structural pressures. (1) **Sanctions**: Russia needs crypto rails for cross-border trade but fears domestic capital flight and dollarized shadow settlement — hence "cross-border yes, domestic settlement no" + a custody chokepoint. (2) **Fraud epidemic**: the same dropper/social-engineering wave that produced the loan cooling-off and the [[T-Bank and CBR flag new crypto-based bank antifraud scheme]] detection. The cooling-off is the intersection of both: it makes the *legal* crypto perimeter both governable and fraud-resistant, which is the precondition for the state to allow retail crypto at all.

## [3] Novelty / value-add / traction
**Novelty: low.** The *concept* (cooling-off) is borrowed wholesale from Russian consumer-loan/anti-fraud law and mirrors India/UK/Singapore. The only genuinely new element is **applying it at a state digital-depository withdrawal boundary** for crypto — which is more a consequence of the custody design than an independent innovation.

**Traction: zero (nothing is live).** This is "announced/drafted," not adopted. There are no numbers, no launched depository, no exchanger registry populated, and the enabling law hasn't passed 2nd reading. **Who captures value / who is silent (analysis):** unstated — the **duration** of the crypto cooling-off (loan analogy ≠ binding), whether it applies to all withdrawals or only flagged/suspicious ones, whether there's a whitelist/bypass (India has one; Russia's source doesn't say), and who bears **fraud liability** during the hold. The related fraud-liability shift (exchangers must compensate clients for fraud losses, per web reporting) is the real teeth — the cooling-off is the operational complement. Without those specifics, the provision is directionally clear but operationally hollow.

## [4] What's next / sentiment
Next: 2nd-reading review by the Duma Financial Market Committee (Aksakov's committee), now expected **after** the missed 1 July 2026 date; tax bill on a parallel track; criminal/administrative-liability bills likely autumn 2026 session. Enforcement rules for the market framework are signposted for ~1 July 2027.

**Why the market goes this way / second-order (analysis):** The bill is a **surveillance-first legalization** — the point is not to free crypto but to pull it inside a state-visible custody rail before allowing it. The cooling-off, retail RUB 300k/yr cap, domestic-settlement ban and depository custody together mean the *legal* channel is deliberately less flexible than the existing gray P2P market. **Counterintuitive risk:** friction (cooling-off + caps + custody) may **push sophisticated users back to self-custody/gray P2P** — the exact behavior the regime wants to eliminate — unless the criminal-liability bills (autumn) make the gray market genuinely dangerous. So the cooling-off's real effectiveness depends on a *different* bill that isn't even scheduled yet. Sentiment: measured/skeptical; repeated timeline slippage (July → post-July) is the dominant signal.

## Sources
- interfax.ru (primary, in note): https://www.interfax.ru/russia/1092437
- Forbes.ru, TASS, Expert.ru, kod.ru (RU coverage of Frolov's statement)
- dig.watch — Russia expects delay in crypto bill (Yakovlev): https://dig.watch/updates/russia-delay-in-crypto-market-regulation-bill
- CBR — consumer-loan cooling-off (4-48h, live 1 Sept 2025): https://www.cbr.ru/eng/press/event/?id=26879
- Internal: [[RBI proposes one-hour delay on high-value digital transfers]], [[Russia to legalize crypto for cross-border trade payments]], [[Russia's Sberbank plans crypto-backed loans for corporate clients]], [[T-Bank and CBR flag new crypto-based bank antifraud scheme]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is this even a new event?** No — it is a Minfin official (Frolov, 28 May) *confirming* a design detail he already floated earlier in May. Fresh only in the weak sense that the [Финтехно] restatement on 2026-07-03 adds the "became more concrete" framing; the underlying substance dates to May. (mostly stale-flavored but not a duplicate of an existing note)

2. **Is it a duplicate of [[T-Bank and CBR flag new crypto-based bank antifraud scheme]]?** No. That note is a *detected fraud scheme* (crypto + dropper QR payments) flagged by T-Bank/CBR; this is a *Minfin legislative provision* (cooling-off in the crypto law). Same theme (RU crypto anti-fraud), distinct events. Not duplicate_of.

3. **Announced or launched?** Announced/drafted only. Nothing live; the enabling law hasn't passed 2nd reading. Traction = 0.

4. **What is the actual cooling-off duration for crypto?** OPEN. Source gives only the *loan* analogy (4h / 48h). No published crypto-specific figure — a material gap.

5. **Does it apply to ALL withdrawals or only flagged/suspicious ones?** OPEN. Loan cooling-off is blanket-by-amount; suspicious-transfer pauses are risk-triggered. The note doesn't specify which model crypto uses — determines whether it's routine friction or targeted.

6. **Is there a whitelist / bypass-after-verification?** OPEN. India's RBI version has one; Russia's source is silent. Absence would make it much heavier UX.

7. **Who bears fraud liability during the hold?** OPEN in the note; web reporting says exchangers must compensate clients for fraud losses — that is the real teeth, cooling-off is the operational complement.

8. **Has the July-1 timeline actually held?** NO — this is the biggest correction. Yakovlev (Minfin) told Interfax the bill would NOT be adopted by 1 July 2026; committee review slipped past the deadline. The note's "advances" framing is optimistic vs reality on 2026-07-03. (fact)

9. **Only bites at the depository→wallet boundary — so what?** By design: it presumes assets sit in a state-run custody layer. Self-custodied/gray-market crypto is untouched → effectiveness depends on funneling users into the regulated perimeter first.

10. **Does friction backfire?** Plausible. Cooling-off + RUB 300k/yr retail cap + domestic-settlement ban + custody may push sophisticated users to self-custody/gray P2P — the opposite of the intent. Countered only by the (unscheduled, autumn) criminal-liability bills.

11. **Is Russia leading here?** No — parity/catching up. India (1h), UK (72h), Singapore (12h), Sweden all have live/proposed equivalents; Russia ports its own loan tool onto crypto.

12. **Why a state digital depository at all vs bank-edge delay?** Sanctions + surveillance: Russia wants a visible custody chokepoint (FNS-recorded address-identifiers, Schetnaya Palata access), not just a PSP-level speed bump.

13. **Does the number of mentions (1) reflect weight?** Single channel ([Финтехно]), single source (interfax). Low corpus salience — consistent with an incremental legislative-detail item.

14. **What would make this a 4-5/5?** Publication of the actual cooling-off duration + scope in the 2nd-reading text, or the law actually passing. Neither happened; and the timeline slipped.

15. **Bottom line freshness call:** FRESH (barely) — it is a same-day restatement/consolidation of a distinct regulatory item, not covered by any existing note. Not a duplicate. But low novelty and zero traction, and the headline "advances" is contradicted by the confirmed timeline slippage.

Importance: 3/5 — A real, concrete provision inside Russia's headline crypto-legalization bill, at the intersection of two live macro themes (sanctions-driven crypto regime + fraud epidemic), and comparable to a tracked RBI item. But it is announced-not-live, low-novelty (borrowed from loan law), operationally under-specified (no duration/scope), single-source/single-channel, and the flagship "on-schedule" framing is undercut by the bill's slippage past July 1. Solidly mid — informative context, not a market-mover.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-04]] (2026-07-04).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a *regulatory* item, not a deal — no valuation, no protagonist company. Sector = Russian crypto-market legalization + anti-fraud/RegTech overlay. Bill №1194918-8 ("On Digital Currency and Digital Rights") passed first reading 21 Apr 2026; targeted to legalize crypto purchase by residents from 1 Jul 2026 via licensed intermediaries (CBR-registered exchangers, brokers, trustees), with domestic settlement in crypto still banned (per interfax, note primary). Timeline is the first risk: as of early Jul 2026, the second reading had NOT landed — Minfin's Alexey Yakovlev told Interfax the bill is unlikely to hit the original 1 Jul 2026 date and goes back to committee before second reading (per Interfax/coincentral, as of ~Jun–Jul 2026). "Why now": Russia is racing two agendas at once — (1) sanctions-driven need for a legal cross-border crypto channel (crypto reframed as FX asset for foreign trade), and (2) a domestic fraud epidemic. The cooling-off clause belongs to the second. Fraud scale is the driver: CBR detected 7,000+ fraudulent operations in 2025; Russians sent funds to 4,600+ scam-controlled crypto wallets, ~1,500 firms ran bogus crypto investments (per CCN/Yahoo Finance, 2026). Sberbank's Kuznetsov put total scam theft on track for ~360bn rubles in 2025, up 20%+ from ~295bn in 2024 (per RussiaPI/press, 2025) — [UNSOURCED] as to the crypto-specific share.

**Competitive landscape (regulatory precedent).** No sector KPIs / peers here — the relevant frame is *precedent for cooling-off as an anti-fraud tool*. The clause imports a mechanism already live in Russian banking: since 25 Jul 2024 banks must pause 2 days on transfers to payees flagged in CBR's fraud database, incl. self-transfers/SBP (per CBR/Izvestia). Consumer-lending cooling-off (4h for 50k–200k rub loans, 48h above 200k) is already law — cited verbatim in the note's own primary. So the crypto cooling-off is a copy-paste of an *established* domestic template onto a new rail (withdrawals from address-identifiers on the digital-depository platform), not a novel invention. International comps in-base: India's [[RBI proposes one-hour delay on high-value digital transfers]] (Apr 2026) is the same anti-fraud-delay pattern on a different rail. The distinctive Russian design choice: the depository model caps withdrawals to *licensed* platforms only, excluding transfers to personal/private wallets (per U.Today/ForkLog, 2026) — i.e. the cooling-off is one layer of a broader custody-gating regime, not a standalone friction.

**Comps & multiples.** No data — regulatory event, no traded entity, no valuation. Distribution not computed. Internal comps (regulatory/precedent, as `[[wikilink]]`): [[RBI proposes one-hour delay on high-value digital transfers]] · [[Russia's central bank calls MAX transaction approval premature]] · [[Russia to legalize crypto for cross-border trade payments]] · [[Crypto coin for Russian shadow payments moves $9 billion]] (shadow/sanctions-evasion crypto flows the regime must reconcile with). These situate the note inside a consistent 2025–26 arc: Russia is simultaneously legalizing crypto for cross-border trade and hard-gating retail crypto against fraud.

**Risk flags.**
1. **Legislative-timeline slippage.** Second/third readings had not passed as of early Jul 2026 and Minfin itself concedes the 1 Jul date will slip (per Interfax/coincentral). "Announced" ≠ "live": the cooling-off clause is a provision in a bill that keeps moving between readings — text can still change materially before third reading.
2. **Effectiveness / false-positive risk from the banking precedent.** The 2024 transfer cooling-off already produced excess blocking — CBR's own head flagged rising complaints about unjustified account freezes and "excessive" anti-fraud action (per RealnoeVremya/CBR, late 2025). Banks over-reinsure because CBR/Rosfinmonitoring sanctions hurt more than lost customer loyalty. Transplanted to crypto withdrawals, the same friction likely recurs — legit users delayed, real determined fraud (social-engineering victims who self-confirm) only partly stopped, since confirmation lets the transfer through.
3. **Displacement, not elimination (second-order).** Cooling-off only bites *inside* the licensed digital-depository perimeter. Domestic crypto settlement stays banned and P2P is being squeezed, so scam/sanctions flows plausibly route around the regulated rail into unlicensed exchangers, foreign platforms and shadow stablecoins (cf. [[Crypto coin for Russian shadow payments moves $9 billion]]) — the friction protects the legal channel while illicit volume migrates off it.

**What this changes (idea-lens).** For the sector: this cements Russia's model as *gated legalization* — retail crypto access wrapped in the same fraud-control machinery as bank transfers, with custody centralized in a state-supervised digital depository rather than self-custody. Falsifiable thesis (analysis): if the bill passes with the cooling-off + licensed-withdrawal-only design intact, it structurally favors CBR-registered incumbents (banks, licensed exchangers) over crypto-native/self-custody players — the moat is the license, not the product. Watch/triggers: (a) does the second reading actually land in the autumn session and does the cooling-off clause survive verbatim; (b) whether admin/criminal-liability bills (flagged for the autumn session per Interfax) attach real teeth; (c) early complaint/false-positive data once withdrawals go live — the tell for whether it reduces fraud or just reduces usage.

Sources: https://www.interfax.ru/russia/1092437 · https://coincentral.com/russia-advances-crypto-regulation-bill-to-legalize-foreign-trade-settlements/ · https://www.ccn.com/news/crypto/two-thirds-russian-pyramid-scams-run-on-crypto/ · https://www.cbr.ru/eng/press/event/?id=23263 · https://realnoevremya.com/articles/8904-new-measures-against-fraudsters-and-strict-control-over-money-transfers · https://u.today/opinions/crypto-regulation-2026-what-is-happening-in-russia
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
