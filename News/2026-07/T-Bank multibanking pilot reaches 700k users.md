---
title: "T-Bank multibanking pilot reaches 700k users"
date: 2026-07-03
retrieved: 2026-07-03
tags:
  - company/t-bank
  - industry/neobank
  - region/ru
  - type/product
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sffaec189
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# T-Bank multibanking pilot reaches 700k users

> [!info] 2026-07-03 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Т-Банк отчитался о пилоте мультибанкинга: сервисом уже воспользовались около 700 тыс. клиентов, из них 450 тыс. — в приложении Т-Банка. Самые востребованные сценарии — просмотр баланса в одном окне, переводы и история операций. Сейчас полноценно подключены четыре банка: Т-Банк, Сбер, ВТБ и Альфа-Банк. Т-Банк называет инвестиции банков в мультибанкинг прыжком веры без понятной текущей бизнес-модели. Директор департамента ключевых экосистемных продуктов Т-Банка Сергей Хромов на Финансовом конгрессе Банка России поднял важный вопрос о том, что базовая передача данных в мультибанкинге должна быть бесплатной. Его аргумент — рынок ещё не сформирован, а плата за данные станет барьером для масштабирования. Это важно для всего рынка, потому что мультибанкинг может стать новым способом подтверждения дохода наряду с традиционными документами. Если банк с согласия клиента видит счета, поступления и финансовое поведение в других банках, он может точнее оценивать платёжеспособность при кредитован

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: T-Bank multibanking pilot reaches ~700k users
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
At the Bank of Russia Financial Congress (St. Petersburg, 1–3 July 2026), T-Bank reported a **traction update** on its retail "Мультибанкинг" pilot: ~**700k customers** have used the service, of which **~450k inside the T-Bank app** (the rest via partner-bank interfaces, since the service is reciprocal over the CBR Open API). Most-used scenarios are **read-only**: balance-in-one-window, transfers, and transaction history. Four banks are "fully connected": T-Bank, Sber, VTB, Alfa-Bank.

De-PR'd, two things matter more than the headline number:
1. **It is an update, not a launch.** Retail multibanking went live **9 Oct 2025** (T-Bank claims Russia-first), with Sber-card linking available since **June 2024**. A June 2026 datapoint had it at **350k (up 17x in 6 months)**; ~700k is roughly a further doubling in ~1 month — plausible but a single self-reported figure, no cohort/retention/active-use breakdown. So "700k users" = *cumulative ever-added*, not proven active MAU. (analysis)
2. **The real news is the policy argument, not the metric.** T-Bank's Sergey Khromov (director of key ecosystem products) publicly argued that **base data transfer in multibanking should be free**, on the reasoning that the market is unformed and a data-fee would be a scaling barrier. He framed banks' current multibanking spend as a **"leap of faith without a clear business model."** This is a de-PR'd admission that the product **has no proven monetization yet** — the value is a *bet* that seeing rivals' accounts (with consent) becomes a new **income-verification / scoring input** alongside traditional documents, improving creditworthiness assessment. That is the load-bearing claim, and it is prospective, not live. (analysis)

**Why framed this way / what it reveals:** T-Bank, the *smaller* balance-sheet player vs Sber, benefits most from a symmetric, free data layer — it gets visibility into Sber/VTB/Alfa's much larger deposit and income bases without paying rent for it. Advocating "free base data" at a CBR forum is therefore not neutral: it is the interface-aggregator's interest (maximize inbound data, minimize cost) dressed as market-development principle. The party with the most accounts (Sber) has the opposite incentive. (analysis)

## [1] Competitors / peers
- **Domestic retail:** T-Bank is first-mover on *retail* multibanking in one app; Sber, VTB, Alfa are simultaneously counterparties and rivals. **Sovkombank** signed at SPIEF to join, with data exchange piloting from **Sept 2026** — i.e. the network is still expanding.
- **Domestic corporate (adjacent, do NOT conflate):** VTB↔Sber (production ~Apr 2026) and VTB↔Alfa (out of pilot, 23 Jun 2026) run a *corporate/treasury* read-only "Мультибанк" — see [[VTB and Alfa-Bank roll out Multibank service for corporates]]. That is the same CBR-Open-API rail but a different product/segment (holdings' treasury visibility). This note is the **retail** track.
- **Same trio, blocked elsewhere:** Sber/Alfa/T-Bank's independent alternative-payment-system bid was rejected by the CBR — [[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]]. Read together: the CBR is channeling big-bank cooperation *into* its Open-API perimeter (multibanking = sanctioned) and away from bespoke rails (rejected). Multibanking is the "approved" cooperation.
- **Global prior art (capability is mature abroad):** account aggregation / "see all banks in one app" has existed for years — [[Valiant adds multibanking for private customers in Switzerland]] (2025-09, retail, near-identical UX), [[Open banking goes live in Switzerland via bLink]], [[SBS adds Wero wallet support to open banking platform]], [[Spare receives in-principle open finance approval from UAE Central Bank]]. So Russia is **catching up on capability**, distinctive only on *delivery model* (banks aggregate each other on a regulator's standard, no neutral TPP) and on the *income-verification* ambition.

**Position:** first-mover *within Russia* on retail; a laggard *globally*. Mechanism delta (one sentence): unlike a neutral third-party aggregator (Plaid/Tink model), here the **largest banks themselves are each other's aggregators** over CBR Open API, so the cockpit relationship — and any future scoring edge — is captured by an incumbent bank, not a fintech.

## [2] Company history / fit
T-Bank (ex-Tinkoff, ~55M clients, 34M active ecosystem) is Russia's largest digital-native bank and a serial "own-the-interface" player. Multibanking fits its consistent strategy of turning its app into the **front door for the client's whole financial life** — the same thesis behind its Auto.ru buy and its "standalone banking apps will lose relevance" commentary ([[Финтехно T-Bank sees standalone banking apps losing relevance]], 2026-07-02). **Why it acts this way (analysis):** with a smaller deposit base than Sber, T-Bank's edge is UX + data/AI, not balance sheet; a free, symmetric multibanking layer lets it *see and score* clients' money held at bigger rivals and cross-sell against it — converting an interface advantage into a lending/pricing advantage. Hence its forceful lobbying for "free base data": the economics only work for the aggregator if the data is cheap.

## [3] Novelty / value-add / traction
**What's genuinely new here:** (a) an *incremental traction disclosure* (~700k cumulative, 450k in-app) on a 9-month-old product, and (b) a public **policy stance** (base data should be free) tied to a concrete **future use-case** — multibanking as a consent-based **income/creditworthiness signal**. The traction number is the softest part: cumulative, self-reported, no active/retention split, and dominated by *read-only* scenarios (balance/history/transfer) — i.e. utility, not yet monetization.
**Value-add reality, deeper (analysis):** the real prize is not the balance-aggregation dashboard (commoditized, low willingness-to-pay) but the **scoring/underwriting data** — seeing a client's true income, deposits and debts across banks. That is where margin sits, and it explains why T-Bank wants the raw data *free*: the value is captured downstream in *lending decisions*, not in the data feed itself. **Who captures the margin:** the bank that best converts cross-bank visibility into pricing/underwriting — favoring the strongest data/AI stack (T-Bank, Sber). Spokes that merely expose accounts risk becoming a commoditized "data feed." **But it's a bet, by T-Bank's own admission** ("leap of faith, no clear business model") — so treat monetization as **unproven**, and the 700k as engagement, not revenue.

## [4] What's next / market sentiment
- **Roadmap:** Sovkombank data exchange from Sept 2026; longer-term T-Bank flags extending data exchange to **MFOs, telecoms and other data-holders** — i.e. open *finance*, not just open banking.
- **Regulatory backdrop (the swing factor):** CBR **Open API** standards are published/updated (recommended, then mandated). The mandate for the largest banks was originally **2026** (others 2027) but was **postponed in Oct 2025** pending a federal law — so current adoption is **voluntary/standard-led ahead of a delayed rule**, not compliance. The CBR + Mindigital are building a **Commercial Consent Management Platform** for individuals/businesses to manage data consents — this is the rail on which "who pays for data" will be decided. Khromov's "free base data" push is a shot in exactly that pricing/policy debate, still open.
- **Why the market goes this way (second-order):** with Western aggregators gone and the CBR blocking independent rails, domestic banks build the visibility layer themselves on the regulator's standard. The unresolved question is **pricing of the data layer** — if the CBR lets data-holders charge, big-deposit banks (Sber) monetize their scale and the aggregation economics tilt against smaller aggregators; if base data is free (T-Bank's ask), it accelerates scaling but concentrates the *scoring* edge with whoever has the best AI, and turns multibanking into a de-facto alternative to the credit bureau for income verification. Counterintuitive risk: "free open banking" could *deepen* the data/AI moat of the top-2 rather than democratize access.

## Top challenge/extra questions
See challenge file.

## Sources
- Финтехно (max.ru/fintexno) — primary aggregated text (2026-07-03). Full text not loaded (no primary source cached).
- CBR Financial Congress 1–3 Jul 2026: https://ifcongress.ru/en
- Retail launch (9 Oct 2025), 4-bank scope: https://tadviser.com/index.php/Product:T-Bank:_Multibanking_(Mobile_application) ; https://rozetked.me/news/42034-t-bank-ob-yavil-o-zapuske-mul-tibankinga
- Prior traction 350k / +17x (Jun 2026) + Sovkombank Sept-2026 pilot: https://bankinform.ru/news/141974 ; https://kod.ru/t-bank-multibanking-sber-sovkombank ; https://www.vedomosti.ru/finance/articles/2026/06/04/1203002-k-multibankingu-t-banka-prisoedinitsya-esche-odin-bank
- Tech (FAPI.SEC / OpenID Connect) + scoring rationale: https://www.iguides.ru/main/os/multibanking_v_prilozhenii_t_banka/
- CBR Open API mandate + postponement + Consent Management Platform: https://www.cbr.ru/eng/press/event/?id=20969 ; https://cbr.ru/eng/press/event/?id=28218
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. **Is "700k" active or cumulative?** Almost certainly *cumulative ever-added* (prior figure 350k in Jun 2026 was framed as growth, not MAU). No active-use, retention or per-scenario split disclosed → engagement, not proven traction. **Open / likely cumulative.**
2. **Is this fresh vs the corporate multibank note?** Yes — [[VTB and Alfa-Bank roll out Multibank service for corporates]] is the *corporate/treasury* track (VTB as hub). This is the *retail* track (T-Bank in-app, ~700k consumers) + a policy argument. Different product, segment, protagonist. **Not a duplicate.**
3. **Is the launch itself old news?** Retail multibanking went live 9 Oct 2025; Sber cards since Jun 2024. So the *product* is not new. The new elements are the traction update and Khromov's "free base data" stance. Note weight rests on those, not the launch.
4. **Read-only or transactional?** The stated top scenarios are balance-in-one-window, transfers, history. Transfers exist, but "full money management" across banks is not claimed. Predominantly **read-only aggregation**.
5. **Does "700k" prove product-market fit, or just curiosity adds?** A one-time "link my other bank" tap inflates cumulative counts; without repeat-use data, can't distinguish habit from novelty. **Open.**
6. **Whose interest is "free base data"?** T-Bank (smaller deposit base) gains most from cheap symmetric data; Sber (largest deposits) has the opposite incentive. Khromov's framing is self-interested principle, not neutral. **Confirmed bias to flag.**
7. **Is multibanking-as-income-verification real or aspirational?** Presented as future potential ("may become a new way to confirm income"). No live underwriting product cited using it. **Aspirational / open.**
8. **What's the business model?** T-Bank's own admission: "leap of faith without a clear business model." Monetization is **unproven** by the protagonist itself — a strong de-PR signal to cap importance.
9. **Regulatory status — mandate or voluntary?** CBR Open API mandate (orig. 2026/2027) was **postponed Oct 2025** pending federal law. Current adoption is voluntary/standard-led. Any "regulation forced it" framing is wrong. **Confirmed.**
10. **Who's silent on liability/consent?** Cross-bank data access under consent: who bears liability for misuse/leak, and does the coming CBR Commercial Consent Management Platform change the pricing/consent flow? **Open — not addressed in source.**
11. **Attribution strength.** Single-channel (Финтехно Telegram) aggregation, no primary source text loaded; the 700k/450k split and Khromov quote are un-cross-checked against a T-Bank primary. **Weak sourcing.**
12. **Does scale help or trap the aggregator?** If base data is free, the *scoring* edge accrues to the best AI/data stack (T-Bank, Sber) → "open banking" could deepen top-2 concentration, not democratize. Second-order risk to the pro-consumer framing.
13. **Prior art dilution.** Account aggregation is a mature global category ([[Valiant adds multibanking for private customers in Switzerland]], Plaid/Tink). Russia's only distinctiveness is bank-as-aggregator delivery + the income-verification ambition. Novelty is regional, not fundamental.
14. **Sovkombank/MFO/telecom expansion — firm or aspiration?** Sovkombank pilot Sept 2026 is dated; MFO/telecom extension is directional. Treat expansion as **plan, not done.**
15. **Materiality of the metric to the market.** Does ~700k cumulative retail users (in a ~55M-client bank, and a ~110M-client Sber ecosystem) actually move anything, or is it early-adopter noise dressed as momentum? **Likely early-stage; low read-across without active-use data.**

**Importance: 3/5 — rationale:** Fresh and genuinely informative on two counts — (a) an incremental traction disclosure on Russia's first retail multibanking product, and (b) a live *policy* argument (base data should be free) that goes to the core open-banking economics debate and to a real future use-case (consent-based income verification / scoring). It also complements, without duplicating, the corporate-multibank and standalone-app-thesis notes, filling the vault's thin T-Bank retail-open-banking coverage. Capped at 3 because: the product is 9 months old (not a launch), the headline number is self-reported/cumulative with no active-use split, monetization is unproven by the protagonist's own admission ("leap of faith, no business model"), the capability is globally mature, the mandate is postponed (voluntary adoption), and sourcing is a single Telegram channel with no primary text. Real, structurally interesting, but early and PR-tinged → 3/5.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-04]] (2026-07-04).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russia's open-banking layer is regulation-driven, not market-pull. The CBR has developed Open API standards since 2020; from **2026** the largest banks, brokers and insurers are **obliged** to expose Open APIs, extending to MFIs/depositories/financial platforms in 2027 (per Bank of Russia, cbr.ru, as of 2026). A **Commercial Consent Management Platform** (CBR + Mindigital) is planned to let clients govern data consents. So the T-Bank pilot rides a mandate wave rather than voluntary rails: the structure is a **concentrated** oligopoly (Sber, VTB, Alfa, T-Bank = the four "fully connected" banks), where the aggregator interface — not the underlying account — is where daily engagement is captured. "Why now": the 2026 compliance deadline plus the CBR Financial Congress (St Petersburg, 1–3 Jul 2026) where T-Bank's Sergei Khromov argued baseline data transfer must be **free** — i.e. the economics are unsettled precisely as the mandate lands. Global frame for scale: UK open banking hit ~16.5m user connections by Dec-2025 (~1/3 of adults) after *six* years and still ~20% adoption (per Open Banking Ltd, openbanking.org.uk, 2025); Brazil >9.8m users. Against that, T-Bank's ~700k pilot users in months is early but not yet mass.

**Competitive landscape.** Sector KPIs for an aggregator: linked-account penetration, DAU/MAU of the aggregator surface, AIS "view" vs PIS "action" mix, and (downstream) whether aggregated data feeds underwriting. Players/basis of competition: **T-Bank** competes on product/UX and first-mover aggregation (launched Multibanking Oct-2025, Sber-linking live since Jun-2024, per tbank.ru/tadviser); **Sber** competes on distribution/scale and its own ecosystem; **VTB + Sber** launched a rival **"Multibank" for business** (Apr-2026, per www1.ru) — signalling the incumbents will build their own hubs rather than concede the interface. Recent moves: T-Bank 700k users / 450k in-app (2026-07); VTB/Sber business multibank (2026-04). Position: T-Bank is **ahead** on the consumer front-door and framing (pushing the "free base data" norm that suits an aggregator), but the moat is thin — the rails are mandated and shared, so the defensibility is UX + engagement + cross-sell, i.e. **switching costs via daily habit**, not proprietary infrastructure `(analysis)`.

**Comps & multiples.** No valuation/round/metrics in this news beyond user counts → trading multiples **not applicable / no data**. Price-per-user for the pilot is not meaningful (free feature, no revenue model — T-Bank itself calls it a "leap of faith without a clear business model"). Internal comps (open-banking / aggregation precedents in-base):
- [[Open banking goes live in Switzerland via bLink]] — regulated multi-bank aggregation, 8 banks + 2 TPPs; direct structural analogue to a mandated hub.
- [[Flutterwave acquires open banking firm Mono]] — consolidation of aggregation *infrastructure*; shows the value pool can sit in the API/data layer, not the app.
- [[New Zealand to extend open banking to SME channels]] — another regulator-led rollout expanding scope.
- [[Revolut launches Dutch mobile network on KPN 5G]] — super-app engagement-consolidation play (adjacent motive: own the daily surface).
Distribution not computed (no comparable financials); comparison is qualitative.

**Risk flags.**
1. **No business model / disputed economics.** T-Bank concedes there is no current model and lobbies for *free* base data. If the CBR mandates paid data transfer, the aggregator economics invert — the party holding the data (large incumbents like Sber) can toll the aggregator, disintermediating T-Bank's margin. Second-order: the interface-owner may not capture the value.
2. **Incumbent counter-build + data asymmetry.** Sber/VTB launching their own multibank hubs (Apr-2026) means T-Bank could aggregate rivals while rivals refuse reciprocity or degrade API quality within the mandate's letter — concentration risk in a 4-bank oligopoly where peers are also competitors.
3. **Regulatory + adoption execution risk.** UK took six years to ~20% adoption; 700k is a pilot, and the CBR Consent Platform, data-liability rules and the multibanking-as-income-proof use case (credit underwriting) are all unbuilt/unproven. Regulatory design (who bears fraud/data liability) is silent in the PR.

**What this changes (idea-lens).** `(analysis)` Multibanking reframes the Russian retail-bank contest from "own the account" to "own the aggregating interface + the underwriting signal" — if aggregated cross-bank data becomes an accepted income/affordability proof, the aggregator gains a lending edge, not just a UX one. Falsifiable thesis: T-Bank's lead holds only if base data transfer stays free and reciprocal; **trigger to watch** — the CBR's ruling on data-transfer pricing and the Consent Management Platform launch. What breaks it: a paid-data regime or incumbents (Sber) locking their data behind their own hub, turning T-Bank's aggregation into a cost centre.

Sources: https://www.cbr.ru/eng/press/event/?id=20969 · https://www.akm.ru/eng/news/the-largest-russian-banks-and-insurance-companies-will-be-required-to-use-open-apis-from-2026/ · https://www.tbank.ru/about/news/09102025-multibanking-t-bank-has-consolidated-information-about-clients-accounts-with-alfa-bank-vtb-and-sberbank-in-its-mobile-app/ · https://tadviser.com/index.php/Product:T-Bank:_Multibanking_(Mobile_application) · https://www1.ru/en/news/2026/04/05/dva-banka-v-odnom-okne-vtb-i-sber-zapustili-multibank-dlia-biznesa.html · https://www.openbanking.org.uk/insights/open-banking-in-2025-now-part-of-the-uks-everyday-financial-life/ · https://www.cbr.ru/eng/press/event/?id=32602
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
