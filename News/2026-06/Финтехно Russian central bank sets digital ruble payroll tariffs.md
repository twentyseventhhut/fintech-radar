---
title: "Финтехно: Russian central bank sets digital ruble payroll tariffs"
date: 2026-06-24
tags:
  - company/cbr
  - industry/payments
  - region/europe
  - type/regulation
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sd451cc5a
month: 2026-06
enriched: true
importance: 3
---

# Финтехно: Russian central bank sets digital ruble payroll tariffs

> [!info] 2026-06-24 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Цифровой рубль сильно повлияет на экономику выплаты зарплат через банки. Совет директоров ЦБ утвердил тарифы по таким операциям, они начнут действовать с 1 января. ⬛️ Юрлица будут платить оператору платформы цифрового рубля 1 рубль за каждое исполненное распоряжение в реестре, но не менее 15 рублей за реестр. Тариф выглядит низким, но чисто технически переход вряд ли будет дешёвым. ⬛️ Банк — точнее участник платформы, от которого на платформу поступило распоряжение о переводе, — будет получать от оператора платформы 67 копеек за каждое исполненное распоряжение в реестре, но не менее 10 рублей за реестр. Относительно ценности зарплатного клиента это очень мало. Как мы поняли, главный мотив ЦБ — снизить сопротивление банков массовым выплатам зарплат в цифровых рублях. Это один из самых чувствительных сценариев, который важен для удержания остатков, регулярного контакта с клиентом, допродаж банковских продуктов — а цифровой рубль ломает часть этой экономики: деньги хранятся на платформ

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Bank of Russia sets digital ruble payroll tariffs
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **19 June 2026** the Bank of Russia Board of Directors approved the tariff schedule for paying salaries (and other labour-contract payments) from legal entities to individuals in digital rubles; the decision takes legal effect **27 June 2026** and the fees themselves are charged only **from 1 January 2027** (free for both sides through 31 Dec 2026). Sources: Interfax, Garant.ru, CBR (cbr.ru), ComNews (2026-06-25).
- **What a company pays the platform operator (the CBR itself):** 1 ruble per executed instruction in the registry, **but not less than 15 rubles per registry**.
- **What the bank receives from the operator:** 67 kopecks per executed instruction, **but not less than 10 rubles per registry**. Note the asymmetry — the bank is *paid* by the CBR for routing the instruction; the corporate is *charged*. The CBR sits in the middle of the cashflow and on a small registry tops the bank's 10-ruble minimum up out of its own pocket (per CoinReporter/cryptonews worked example: 10 staff → 6.7 rubles earned, topped to the 10-ruble floor).
- **Why structured this way (the real story):** the headline tariff is trivially low (1 ruble ≈ $0.012 per payslip). The signal is not the price — it is that the CBR is **subsidising banks to do payroll in digital rubles** rather than charging them. This is a de-PR'd admission that the regulator expects bank *resistance*, not enthusiasm. The whole point of the tariff is to neutralise that resistance on the single most economically sensitive flow — payroll. (analysis)
- **Mechanism delta vs an ordinary salary project:** today a salary "zarplatny proekt" lands money in a bank deposit account the bank controls, earns float on, and uses as the hook for cross-sell. Digital rubles sit on the **CBR platform**, are non-interest-bearing, and have **no holding cap** in Russia (unlike most CBDC designs) — so balances can leave the commercial-bank balance sheet entirely. The 67-kopeck fee is compensation for losing the deposit, and it is laughably small against the value of a payroll client. (analysis)
- **What's vague/PR:** the channel framing ("tariff looks low") obscures the structural transfer of float away from banks. CBR does not quantify expected migration, fraud liability split, or who bears the integration capex (banks estimate up to ~100m rubles each per Association of Russian Banks).

## [1] Competitors / peers
Peer set = other state-issued CBDCs running real disbursement use-cases, plus the bank-deposit incumbency the digital ruble displaces.
- **India (RBI / NPCI):** RBI is piloting **e-rupee welfare payments** across ~10 experiments targeting a ₹65,000cr ($6.8bn) welfare system (2026-05, [[RBI pilots e-rupee welfare payments to boost CBDC adoption]]); NPCI announced **live programmable CBDC** for targeted subsidies (2025-12, [[NPCI announces live programmable CBDC for targeted subsidies]]); RBI also shipped **offline CBDC** (2025-10, [[RBI introduces offline CBDC payments]]). India leads on *programmability and government-disbursement* fit — the same "push state money to citizens" use-case Russia is now monetising via payroll.
- **China (e-CNY / mBridge):** e-CNY ~230m wallets and ¥16.7tn (~$2.3tn) cumulative by late 2025 — the largest pilot — yet still low *organic retail* share. China is also pushing the wholesale, cross-border angle ([[China advances mBridge digital payments system to rival the dollar]], [[China-led mBridge CBDC platform tops $55 billion in payments]]).
- **Norway (Norges Bank):** the counter-case — **declined to recommend a CBDC** (2025-12, [[Norway's central bank declines to recommend a CBDC]]) because existing rails are already cheap/efficient. Highlights that Russia's motive is *not* payments efficiency (SBP/Faster Payments already do that) but control + sanctions-resilience + programmability.
- **The real competitor = the commercial-bank salary project itself.** Russia's design (no holding cap, no interest) is unusually aggressive at disintermediating banks; most CBDCs cap holdings precisely to protect bank deposits.
- **Position:** Russia is *mid-pack* globally on retail CBDC, but **first-mover on a mandatory, tariff-backed payroll rail** at national scale. The payroll-tariff move is more concrete than most peers' pilots. **Second-order:** by subsidising banks rather than capping holdings, Russia is choosing adoption speed over banking-sector protection — the opposite trade-off to the EU/most BIS designs. (analysis)

## [2] Company history / fit
- The digital ruble's mass rollout was repeatedly delayed: from **1 July 2025** → pushed → now **mass launch 1 September 2026** for systemically important banks and large retailers (revenue >120m rubles); universal-licence banks + retailers >30m rubles on **1 Sep 2027**; the rest on **1 Sep 2028**; outlets <5m rubles exempt (CBR, Interfax, Ledger Insights). Government/budget payments started **1 Jan 2026**, and budget payments are fee-free through 2027.
- The CBR has consistently designed the digital ruble for **sanctions-resilience and state control** post-2022 (Carnegie), alongside parallel crypto moves it tolerates only for cross-border trade ([[Russia to legalize crypto for cross-border trade payments]], [[Russia's Sberbank plans crypto-backed loans for corporate clients]]).
- **Why the CBR acts this way:** it must hit the Sep-2026 mandatory deadline, but the banks it is forcing to integrate are the same banks that lose deposit float to the platform. The payroll tariff is the **carrot bolted onto the stick** — the regulator paying banks 67 kopecks to swallow a structural threat to their funding model. Fits the broader pattern: CBR mandates first, then engineers incentives to reduce friction (cf. its caution on MAX transaction approval, [[Russia's central bank calls MAX transaction approval premature]]). (analysis)

## [3] Novelty / value-add / traction
- **What's genuinely new:** an explicit *per-instruction tariff for B2C payroll* on a CBDC, with the central bank **paying the commercial bank** — a fee architecture few CBDCs have formalised. Most peers are still in pilot/airdrop mode (eNaira, Jam-Dex saw weak organic uptake; adoption concentrated in government cash transfers). Russia is wiring the *economics* of routine payroll, which is the highest-frequency retail flow.
- **Traction = essentially zero so far.** The first salary in digital rubles was a symbolic single payment; mass payroll is not live and the tariff is pre-emptive (effective 2027). This is an *announced economic framework*, not adoption. De-PR: "tariff set" ≠ "salaries flowing".
- **Who captures the margin / where value moves:** the CBR captures the rail and the data; commercial banks lose the deposit float and the cross-sell hook but get a token 67-kopeck routing fee. **The structural value transfer is from bank balance sheets to the central-bank platform.** Because there is no holding cap and no interest, the digital ruble is unattractive for *saving* but fine for *spending* — so the migration risk is concentrated in transactional balances, exactly what salary accounts are. (analysis)
- **What breaks the value-add:** if employees immediately sweep digital-ruble salaries back into interest-bearing bank deposits or cash, the disintermediation never materialises and the whole exercise is symbolic — the eNaira/Jam-Dex pattern. The tariff cannot create demand; it only removes a supply-side (bank) blocker. (hypothesis)

## [4] What's next / market sentiment
- **Timeline:** free through 2026 → tariffs bite 1 Jan 2027 → mass-rollout obligation 1 Sep 2026 (big banks/retailers), cascading to 2027/2028. Government payments already running since Jan 2026.
- **Sentiment:** banks (Association of Russian Banks) have publicly pushed back on **deposit outflow risk** and **integration cost** (up to ~100m rubles/bank cited; some small banks have only ~$3m capital) — which is precisely why the CBR is now paying them. Russia's deliberate choice of **no holding limits** (vs caps elsewhere) maximises both adoption and disintermediation risk.
- **Why the market goes this way:** mandatory deadlines + a subsidised tariff make bank participation a fait accompli, but **demand-side adoption is the open variable** — every comparable retail CBDC (eNaira, Jam-Dex) under-delivered vs launch projections; even e-CNY's huge wallet count masks thin organic use. (analysis)
- **Counterintuitive second-order effect:** subsidising banks to move payroll onto a non-interest, uncapped CBDC could, at scale, **erode the cheap retail-deposit funding base of the banking system** — the regulator is paying banks a few kopecks to help dismantle part of their own funding model. If take-up is high, the systemic-funding question becomes the real story, not the tariff. (hypothesis)

## Sources
- Interfax — https://www.interfax.ru/business/1097827
- Garant.ru — https://www.garant.ru/news/2141462/
- ComNews (2026-06-25) — https://www.comnews.ru/content/246002/2026-06-25/2026-w26/1008/cb-vvedet-tarify-zarplatnye-perevody-cifrovykh-rublyakh
- Plusworld — https://plusworld.ru/articles/72722/
- CoinReporter — https://www.coinreporter.io/2026/06/russias-central-bank-will-pay-banks-to-process-salaries-in-digital-rubles-accelerating-the-cbdc-race/
- CBR rollout — https://cbr.ru/eng/press/event/?id=25774
- Ledger Insights (dates) — https://www.ledgerinsights.com/russia-confirms-digital-ruble-cbdc-delayed-dates/
- Ledger Insights (Jan 2026 gov use) — https://www.ledgerinsights.com/russia-clears-digital-ruble-for-government-usage-starting-january-2026/
- Ledger Insights (bank pushback / no holding limit) — https://www.ledgerinsights.com/russia-shares-cbdc-business-model-as-banks-push-back/
- Carnegie (sanctions motive) — https://carnegieendowment.org/research/2024/10/russia-digital-ruble-development
- CBDC adoption stats — https://coinlaw.io/central-bank-digital-currency-statistics/
- Internal: [[RBI pilots e-rupee welfare payments to boost CBDC adoption]] · [[NPCI announces live programmable CBDC for targeted subsidies]] · [[RBI introduces offline CBDC payments]] · [[Norway's central bank declines to recommend a CBDC]] · [[China advances mBridge digital payments system to rival the dollar]] · [[Russia to legalize crypto for cross-border trade payments]] · [[Russia's Sberbank plans crypto-backed loans for corporate clients]] · [[Russia's central bank calls MAX transaction approval premature]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_Red-team / second-order questions. Each answered from sources or marked "open"._

1. **Is the tariff actually new, or a re-announcement?** New. The Board decision is dated 19 June 2026, effective 27 June 2026; prior digital-ruble news covered budget/government use (Jan 2026) and rollout dates, not B2C payroll tariffs. The payroll fee schedule is the genuinely new artefact.

2. **When do fees actually bite?** Not "1 January" generically (the channel text is ambiguous) — **1 January 2027**. Service is free for both corporates and banks through 31 Dec 2026. The draft note should not imply 2026.

3. **Is payroll in digital rubles live?** No. Only a symbolic first salary was paid. Mass payroll is not operational; the mandatory rollout for big banks/retailers is 1 Sep 2026. This is a pre-emptive economic framework, not adoption.

4. **Why is the CBR PAYING banks rather than charging them?** Because it expects resistance: digital rubles bypass bank deposits (no interest, no holding cap), destroying the float and cross-sell economics of salary projects. The 67-kopeck fee is a subsidy to neutralise that resistance. (analysis — confirmed by ABR pushback reporting)

5. **Is 67 kopecks remotely adequate compensation for losing a payroll client?** No — it is token. A salary client is worth far more via float, balances, and product cross-sell. The fee is symbolic cover, not real compensation. This is the core de-PR point. (analysis)

6. **Who bears integration capex?** Banks. Association of Russian Banks cited up to ~100m rubles per bank; some small banks have only ~$3m capital. The tariff does not offset this. (sourced: Ledger Insights)

7. **Does Russia cap digital-ruble holdings?** No — unusually, no holding limit, unlike most CBDC designs that cap precisely to protect bank deposits. This makes Russian disintermediation risk structurally higher. (sourced)

8. **Who is silent about what?** The CBR is silent on fraud-liability allocation, expected migration volumes, and the systemic-funding impact of float leaving bank balance sheets. The channel frames "low tariff"; the unsaid story is deposit disintermediation.

9. **Will employees actually keep salaries in digital rubles?** Open. Likely they sweep into interest-bearing deposits or cash (eNaira/Jam-Dex pattern), in which case disintermediation is muted and the exercise is symbolic. Demand-side adoption is the key unknown. (hypothesis)

10. **What did the same thing first?** India's e-rupee welfare/subsidy disbursement (RBI ~10 pilots; NPCI live programmable CBDC) is the closest "push state-linked money to citizens" precedent. Russia is first to formalise a *payroll per-instruction tariff* with the CB paying the bank. (sourced + corpus)

11. **Is this about payments efficiency?** No. Russia's existing SBP rails are already fast/cheap (cf. Norway declining a CBDC because rails are efficient). The motive is control, programmability, and sanctions-resilience. (sourced: Carnegie, Norges Bank corpus note)

12. **Could high uptake backfire on the banking system?** Yes (second-order). At scale, payroll on a non-interest, uncapped CBDC erodes the cheap retail-deposit funding base — the CBR would be paying banks to help dismantle part of their own funding model. Becomes the real story if adoption is high. (hypothesis)

13. **Is the registry minimum (15 rub corp / 10 rub bank) material?** Minor but telling: on small registries the CBR tops the bank's fee up to 10 rubles out of its own funds — confirming the regulator is willing to spend to drive adoption, not extract rent. (sourced, worked example)

14. **Does the tariff change the central question of the assessment?** Yes. The press frame is "CBR sets a (low) tariff". One level deeper: the CBR is *subsidising* banks because the digital ruble threatens their deposit base — so the real question is not "how much is the fee" but "will payroll migration drain bank deposit funding, and who absorbs that". (analysis)

15. **Any sanctions/geopolitical angle worth flagging?** Yes — the digital ruble is also a sanctions-resilience play; EU has weighed extending crypto bans to CBDC infrastructure ([[EU weighs crypto ban on Russia as Gemini exits UK market]]). External-facing usability is constrained, so this remains a domestic control/adoption story for now. (sourced)

Importance: 3/5 — A concrete, first-of-kind payroll-tariff framework for a national CBDC with the central bank subsidising banks (genuinely novel mechanism and a clean window into deposit-disintermediation dynamics), but it is regulatory plumbing, pre-adoption (fees only 2027, no live mass payroll), domestic and partly sanctions-driven — high analytical interest, modest near-term market impact.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-25]] (2026-06-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
_Market layer on top of [0]–[4]. Skeptical; numbers sourced or "no data". (analysis)/(hypothesis) marked._

**Sector & drivers.**
- **Subvertical:** retail CBDC / state payment rails — specifically B2C payroll disbursement on a central-bank platform.
- **Addressable base (the thing being disrupted):** Russian household bank deposits totalled **62.7 trillion rubles (~$771bn) as of Sep 2025**, growing ~4.9tn rubles YTD (per Bank of Russia, via The Moscow Times, 2025-10-21). Salary inflows are a core feeder of this base. No public figure isolates the "salary-project float" subset — "no data" — but payroll is the highest-frequency channel into deposits, so it is the most economically loaded flow to migrate.
- **Structure:** highly **consolidated** — 11 systemically important banks (Sberbank, VTB, Alfa, T-Bank, Gazprombank, Sovcombank, PSB, Rosselkhozbank, MKB, Raiffeisen, UniCredit) dominate; Sberbank + VTB alone anchor retail. Entry barriers are regulatory/scale, and the CBR controls the rail — so this is a regulator-driven, not market-driven, structural change.
- **Drivers + "why now":** (1) mandatory rollout deadline — big banks/large retailers must support digital rubles from **1 Sep 2026**, cascading to 2027/2028; (2) **de-dollarisation / sanctions-resilience** (Carnegie); (3) the tariff is the carrot that makes the mandate workable. Why-ladder: high deposit rates → deposit float is unusually valuable now → banks resist a non-interest CBDC harder → CBR must subsidise to hit its deadline → second-order: the subsidy is tiny vs the float at stake, so resistance is muted but not bought off. (analysis)

**Competitive landscape.**
- **Sector KPIs:** for a CBDC rail — number of platform participant banks, corporate/retail wallets, transaction count/volume, smart-contract executions; for the displaced bank product — deposit float, cost of funding, salary-client cross-sell/ARPU.
- **Platform traction (live):** ~**15 banks**, ~**2,500 legal-entity wallets**, **~100,000 transactions** cumulative (>63,000 transfers, ~13,000 goods/services payments by end-May), **~17,000 smart contracts** (TAdviser / ainvest, 2025). This is pilot-scale, not mass adoption.
- **Recent peer/participant moves:** **VTB** was first to announce live digital-ruble transactions; **Sberbank** lobbied to *postpone* the launch to 2026 (Bitget News) — confirming incumbent resistance. Government/budget payments live since **1 Jan 2026** (budget fee-free through 2027).
- **Cross-border / global peers:** India e-rupee welfare pilots ([[RBI pilots e-rupee welfare payments to boost CBDC adoption]]), NPCI live programmable CBDC ([[NPCI announces live programmable CBDC for targeted subsidies]]); China e-CNY ~230m wallets / ¥16.7tn cumulative; Norway *declined* a CBDC ([[Norway's central bank declines to recommend a CBDC]]).
- **Protagonist position:** the CBR is **ahead** on formalising payroll economics (first to pay banks a per-instruction fee) but **behind** on demand-side adoption (pilot-scale, no live mass payroll). Moat = state mandate + control of the rail (regulatory, not competitive). (analysis)

**Comps & multiples.**
- This is a regulatory tariff, not a valuation/round/earnings event → **no equity multiples to compute ("no data")**. Comparison is on tariff/economics terms.
- **Tariff arithmetic:** corporate pays 1 rub/instruction, min 15 rub/registry; bank receives 0.67 rub/instruction, min 10 rub/registry. Worked example (10-staff payroll): bank earns 10 × 0.67 = **6.7 rubles**, topped by the CBR to the **10-ruble** floor. Per payslip the bank gets **~$0.008**. Against a salary client whose deposit float at ~15% deposit rates is worth meaningfully more, the fee is **token** — rich for the CBR's intent (cheap to subsidise), trivially cheap as compensation to banks. (analysis)
- **Internal comps (CBDC disbursement precedents in corpus):** [[RBI pilots e-rupee welfare payments to boost CBDC adoption]] · [[NPCI announces live programmable CBDC for targeted subsidies]] · [[RBI introduces offline CBDC payments]] · [[Norway's central bank declines to recommend a CBDC]] · [[China advances mBridge digital payments system to rival the dollar]]. None has published a payroll per-instruction tariff — Russia's fee architecture is the outlier.

**Risk flags.**
1. **Deposit disintermediation / funding-base erosion** — no holding cap + no interest means salary balances can leave bank balance sheets; with household deposits at 62.7tn rubles and deposit rates ~15%, even modest migration is materially costly to bank funding. Why: the CBR is subsidising the very channel that drains cheap retail funding. (analysis)
- 2. **Demand-side adoption risk** — every comparable retail CBDC (eNaira, Jam-Dex) under-delivered; if employees sweep digital-ruble salaries back to deposits/cash, the whole framework is symbolic. The tariff removes a bank blocker but cannot create demand. (hypothesis)
3. **Cannibalisation of existing rails** — analysts warn the digital ruble could **undercut Russia's own card/SBP system** (Yahoo Finance), shifting interchange/fee economics among incumbents. (sourced, analyst view)

**What this changes (idea-lens).**
- This is a **regulator-engineered re-plumbing of payroll**, not a re-rating event: watch the **2026→2027 transition** (free → fees bite 1 Jan 2027) and the **1 Sep 2026 mandate** as the real adoption test. Falsifiable thesis: *if* live digital-ruble payroll volumes stay pilot-scale (sub-1% of salary flows) through 2027, the disintermediation fear is overblown and this stays symbolic; *trigger that proves it wrong* = visible deposit-float migration at a major bank (Sberbank/VTB) disclosed in 2027 reporting. (analysis)

Sources: https://www.themoscowtimes.com/2025/10/21/russias-household-deposits-growth-slows-to-3-year-low-central-bank-a90877 · https://tradingeconomics.com/russia/deposit-interest-rate · https://tadviser.com/index.php/Product:Digital_ruble · https://www.ainvest.com/news/digital-ruble-transactions-surpass-100-000-russia-expands-cbdc-pilot-2507/ · https://finance.yahoo.com/news/russia-digital-ruble-undercut-own-160723723.html · https://cbr.ru/eng/press/event/?id=25774 · https://www.interfax.ru/business/1097827
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
no full earnings report in the news (tag type/regulation; the item is a central-bank tariff schedule for digital-ruble payroll, not financial results).
<!-- /enrichment:earnings_review -->
