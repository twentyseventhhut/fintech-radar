---
title: "MTS Pay adds separate charitable-donation transactions"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/mts
  - industry/payments
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-10-12_mts_predstavila_novyj_instrument
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s061ec39d
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# MTS Pay adds separate charitable-donation transactions

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Добавил в МТС Pay возможность перечислять благотворительные пожертвования отдельной транзакцией при оплате покупок

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-10-12_mts_predstavila_novyj_instrument>
*370 слов · direct*

Анна Любавина

 МТС представила новый инструмент для фандрайзинга на базе сервиса «МТС Pay»
 
 
ПАО «МТС» сообщает о внедрении функционала по сбору средств на благотворительность в сервис приема платежей « МТС Pay ». Теперь бизнес может открыть фандрайзинговый сбор для реализации социальных инициатив, а пользователи – перечислить деньги на благотворительность прямо на платежном экране сервиса. Первые благотворительные транзакции с помощью «МТС Pay» были проведены на помощь детям из социальных учреждений в пяти регионах страны. Об этом CNews сообщили представители МТС .
Инициатива на базе « МТС Pay » дополняет линейку технологичных решений МТС, направленных на развитие ежедневной благотворительности. «МТС Pay» – сервис для оплаты покупок в Интернете у эквайринговых партнеров, который поддерживает платежи с карт российских банков , со счета мобильного номера, через СБП или Sberpay . В частности, «МТС Pay» доступен для оплаты сервисов МТС, включая платформы « Кион », « Юрент » и интернет-магазин МТС. Пожертвовать средства НКО можно на сайте МТС и в приложении « Мой МТС », а в дальнейшем – и у партнеров сервиса «МТС Pay». При выборе этого способа автоматически откроется экран с опцией «Сбор средств». В свободном поле можно ввести желаемую сумму на благотворительность и нажать кнопку «Отправить помощь». После этого средства направляются в фонд-организатор сбора, а клиент перенаправляется обратно на экран оплаты. Пожертвование оформляется как отдельная транзакция и не включается в общую сумму покупки.
Первым партнером фандрайзинговой платформы «МТС Pay» стал благотворительный фонд «Система» . МТС планирует расширение пула некоммерческих организаций, которые могут воспользоваться площадкой благотворительного фандрайзинга на базе «МТС Pay» – возможность партнерства открыта для проверенных НКО с разной специализацией в различных регионах страны независимо от масштаба.
«Мы хотим, чтобы помогать было так же просто, как оплачивать покупки. Именно поэтому мы встроили возможность пожертвований в привычный сценарий оплаты в «МТС Pay». Теперь, совершая платёж, пользователь может буквально в пару кликов поддержать социальный проект – без дополнительных шагов и отвлечений. Первые несколько сотен транзакций в пользу фонда "Система“ показывают, что людям важно иметь удобный и прозрачный инструмент ежедневной благотворительности . Для нас это подтверждение, что мы движемся в правильном направлении: технологии должны служить не только удобству, но и добру», – сказал бизнес-лидер стрима «МТС Pay» Алексей Калина . 
 Почём сегодня объектное хранилище на 2 000 Гб? Предложения десятков поставщиков ― на ИТ-маркетплейсе CNewsMarket

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MTS Pay adds separate charitable-donation transactions
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
MTS added a **fundraising/donation capability** to its acquiring service **MTS Pay**: an NKO (charity) can open a collection, and at the payment screen a user can tap a "Сбор средств" (Fundraising) option, enter a free-form amount, and hit "Отправить помощь". The donation is a **separate transaction**, not rolled into the purchase total, and the user is returned to the checkout screen. First (and so far only) partner: **фонд «Система»** (the AFK Sistema group's own foundation — MTS's parent/affiliate, so this is an **in-group pilot**, not an arm's-length NKO win). First donations funded school-prep help for children in social institutions across **five regions**. Entry points today: the **MTS website and the «Мой МТС» app**; partner-merchant checkouts are "в дальнейшем" (future/announced, not live).
- **Why structured this way / what it reveals:** The PR frames a "new fundraising instrument", but what's actually live is narrow — a donation widget inside MTS's own first-party surfaces, with a single affiliated foundation. The "у партнёров сервиса — в дальнейшем" wording is the tell: the valuable part (donations surfaced at *third-party* merchant checkouts, where MTS Pay's acquiring volume sits) is **not yet shipped**. The anchor metric — "первые несколько сотен транзакций" — is deliberately small-sample and avoids ruble totals.

## [1] Competitors / peers
- **MTS Bank «Добро Пэй»** (launched Apr 2025; itself MTS's closest comparable) — a **round-up** micro-donation on card purchases; ~2M RUB raised in ~1 year; expanded Sep 2026 to let users pick among 5 funds (incl. фонд «Система»). Different mechanism (automatic rounding vs. explicit separate donation), different rail (MTS Bank cards vs. MTS Pay acquiring).
- **Сбер «СберВместе»** — mature donation platform with hundreds of funds, embedded in SberPay/SberBank Online; the scale benchmark in RU.
- **Тинькофф/Т-Банк "Cashback to Give Back"** — cashback-to-charity, 300+ partner funds, cap ~9,000 RUB/mo.
- **Currys × Stripe × Pennies (UK, Jan 2026)** — [[Currys partners with Stripe and Pennies on checkout micro-donations]] — point-of-sale micro-donations via an acquirer+charity-platform (Pennies); the Western archetype MTS is echoing (charity as a checkout add-on on top of an acquiring stack).
- **Position:** catching-up / parity-at-best. Sber and T-Bank already have multi-fund donation infrastructure at far larger scale; MTS Pay launches with one affiliated fund and first-party-only surfaces. **Why the lay of the land is this way:** donation-at-checkout is cheap to build but valuable only with (a) merchant distribution and (b) many funds — exactly what MTS lacks on day one and incumbents already have.

## [2] Company history / fit
MTS has been assembling a "daily charity" product line: «Добро Пэй» (MTS Bank, 2025), «Недели добра» campaigns (>5M RUB over two editions), and now the MTS Pay fundraising widget. **Why MTS acts this way:** MTS Pay is a late, sub-scale entrant in RU acquiring vs Sber/T-Bank; bolting a social/ESG feature onto checkout is a low-cost differentiator and a reason for NKOs and ESG-minded merchants to touch the rail. It also keeps donation flow inside AFK Sistema's orbit (фонд «Система» as launch partner = captive first customer). Fits the pattern of MTS wrapping commodity payment rails in brand/social value rather than competing on price.

## [3] Novelty / value-add / traction
- **Really new?** Not conceptually — separate/explicit donation at checkout and round-up donations both pre-date this (Добро Пэй, Currys/Pennies, СберВместе). The marginal novelty is doing it as a **distinct acquiring-side transaction** on MTS Pay's payment screen (vs card-round-up), which lets third-party merchants eventually surface a charity CTA.
- **Traction:** thin and honestly disclosed — "первые несколько сотен транзакций", 1 fund, 5 regions, first-party surfaces only. No GMV, no merchant count, no conversion.
- **Why value-add is weak (for now):** the economics and moat live in **merchant distribution** (donations at partner checkouts) and **fund breadth**, neither of which exists yet. On MTS's own website/app the feature competes with «Добро Пэй» for the same donor — potential cannibalization inside MTS's own line. The margin in this stack sits with whoever owns merchant distribution; MTS Pay doesn't yet, so the capability is a feature, not a franchise.

## [4] What's next / market sentiment
MTS says it will **expand the NKO pool** (open to vetted funds of any size/region) and roll the donation option out **to MTS Pay partner merchants** — that merchant rollout is the real test and is not yet live. Regulatory backdrop: donations in RU are governed by **135-ФЗ (11.08.1995)** on charitable activity; a пожертвование is a gift (no quid pro quo), funds restricted to charitable purposes — standard, low friction for a payments add-on. **Why the market goes this way:** Russian banks/telcos are commoditizing payments and differentiating on embedded social/ESG and ecosystem lock-in; donation-at-checkout is a cheap loyalty/brand lever. **Counterintuitive second-order:** launching with an affiliated fund and first-party-only surfaces signals this is still a **marketing/pilot** move, not a distribution win — weight stays low until independent funds and real merchant checkouts go live with disclosed volumes.

## Sources
- cnews.ru (primary, 2026-10-12) — https://www.cnews.ru/news/line/2026-10-12_mts_predstavila_novyj_instrument
- ixbt.com (2026-10-12) — https://www.ixbt.com/news/2026/10/12/mts-vstroil-sbor-pozertvovanii-v-plateznyi-servis-mts-pay.html
- ASI on «Добро Пэй» launch (2025-04-29) and 2026 expansion (2026-09-24) — https://asi.org.ru/news/2025/04/29/... , https://asi.org.ru/news/2026/09/24/mts-bank-rasshiril-vozmozhnosti-servisa-dobro-pej/
- Rambler: «Добро Пэй» 1-year results (~2M RUB) — https://finance.rambler.ru/business/56643065-mts-bank-podvel-itogi-raboty-servisa-mikrodonatsiy-dobro-pey-za-god/
- Internal: [[Currys partners with Stripe and Pennies on checkout micro-donations]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is this actually live at third-party merchant checkouts?** No — PR says donations are available on the MTS site and «Мой МТС» app now; at MTS Pay partner merchants only "в дальнейшем". The valuable part is announced, not shipped. (answered: first-party only)
2. **Is фонд «Система» an arm's-length NKO win?** No — it is AFK Sistema's own foundation, i.e. MTS's affiliated/parent-group fund. The "first partner" is effectively captive. (answered)
3. **How big is traction really?** "Первые несколько сотен транзакций", 1 fund, 5 regions. No ruble total, no GMV, no merchant count, no conversion. (answered: thin)
4. **How does this differ from MTS Bank «Добро Пэй»?** Добро Пэй = automatic round-up on MTS Bank card purchases (live since Apr 2025, ~2M RUB/yr, 5 funds as of Sep 2026). This = explicit, free-amount separate transaction on MTS Pay's acquiring checkout. Different rail + mechanism. (answered)
5. **Cannibalization risk within MTS's own charity line?** On MTS's own website/app, the new widget competes with Добро Пэй for the same donor wallet. Open — no disclosure on positioning.
6. **What is MTS Pay's acquiring scale vs Sber/T-Bank?** Not disclosed here; MTS Pay is a sub-scale late entrant. Without merchant volume the donation feature has no reach. Open.
7. **Economics: who bears the acquiring fee / commission on a donation?** Unstated — is the NKO charged a merchant fee, or is it waived? Material for NKO adoption. Open.
8. **Is the donation a true separate settlement to the fund, or does MTS intermediate the float?** PR says funds "направляются в фонд-организатор"; settlement timing/float not disclosed. Open.
9. **Prior art — is "separate donation at checkout" novel?** No. Currys×Stripe×Pennies (UK, Jan 2026), СберВместе, Тинькофф cashback-to-charity all predate it. Marginal novelty only. (answered)
10. **Why separate transaction rather than round-up?** A separate transaction lets a third-party merchant surface a charity CTA at checkout (round-up needs issuer control); this is the strategic rationale for the design. (analysis)
11. **Regulatory exposure?** Standard 135-ФЗ donation framework (gift, no quid pro quo, restricted use); low friction. No special barrier. (answered)
12. **Any disclosed take-rate or revenue to MTS?** None — framed purely as social/ESG, implying no direct monetization yet. Open.
13. **What would move importance up?** Independent (non-Sistema) funds live + donation option on real partner-merchant checkouts + disclosed volume/GMV. None present. (answered)
14. **Freshness vs prior corpus notes?** No prior note covers an MTS *Pay* charity/fundraising feature; [[Currys partners with Stripe and Pennies on checkout micro-donations]] is prior art, not the same event. FRESH. (answered)
15. **Is this strategically a franchise or a feature?** A feature/marketing pilot — the moat (merchant distribution, fund breadth) is not yet built. (analysis)

Importance: 2/5 — A low-cost checkout donation widget launched narrow: one affiliated fund (фонд «Система»), first-party surfaces only, a few hundred transactions, no GMV. The genuinely valuable piece (donations at third-party MTS Pay merchant checkouts) is announced, not live. Fresh (no prior corpus coverage of this specific feature) but low weight versus incumbent RU donation platforms (СберВместе, Тинькофф) and even MTS's own «Добро Пэй».
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** MTS Pay sits in Russian digital-wallet / embedded-payments, with this move targeting the embedded-giving ("daily charity") niche. Market context: e-wallet transaction volume in Russia reached RUB 13.3tn in 2025, up ~1.6x YoY, across 8.8bn operations (+1.4x) — per aggregated figures via Statista/tadviser, as of 2025. The broader cards-and-payments market is ~$0.78tn (2025), projected to a ~13.7% CAGR to 2033 per MarketDataForecast — a large, fast-growing but heavily domestic/consolidated pool dominated by Sber, T-Bank and SBP rails. Structure: payments value in RU is captured by a few bank/ecosystem super-apps; entry barriers are distribution (installed base) and rails access (SBP, SberPay), not technology — MTS Pay itself rides card/SBP/SberPay rails rather than owning them. Why now: (1) embedded "round-up / donate-at-checkout" is a mature pattern abroad (Give.org, NPR coverage of US checkout round-ups) now being localised; (2) ecosystem players are racing to add low-friction social features to deepen engagement and keep users inside the wallet. The charity hook is more an engagement/ESG feature than a revenue line — no take-rate or fee on donations is disclosed.

**Competitive landscape.** Wallet/payments KPIs that matter here: TPV through the wallet, active users, take rate on acquiring, and attach/engagement (donations are a stickiness lever, not a monetised stream). Key players and basis of competition: Sber/SberPay + YooMoney (Sber-owned; YooMoney already runs a standing charity catalogue/directory for NKO donations), T-Bank, and SBP (regulator rails) — competition is on distribution and ecosystem breadth, not price. Recent peer moves: MTS Bank integrated charitable giving directly into online checkout (itrussia, 2026-06-14) — i.e. the MTS group was already doing checkout-embedded charity ~4 months before this MTS Pay acquiring-side launch, so this is group-level extension more than a first mover vs Sber. MTS Pay's position: niche / catching-up — it is a late, small entrant in embedded giving relative to YooMoney's established charity directory and Sber's reach. Moat: none specific to charity; the only edge is MTS's own ecosystem funnel (Kion, Yurent, MTS store, "Мой МТС" app) where it can route donation flow (analysis). First NKO partner is the affiliated Sistema charitable foundation — an intra-group anchor, not external validation.

**Comps & multiples.** No deal, round or valuation in this news — MTS Pay is an internal product line of listed PJSC MTS, so no standalone multiple exists; "distribution not computed, qualitative comparison." Internal comps (RU wallet/payments & MTS product cadence) from the base: [[MTS enables local QR payments in Colombia and Argentina]] (same MTS Pay rails, cross-border expansion, 2026-10), [[Bank of Russia introduces quality rating system for e-money operators]] (RU e-money regulatory frame, 2026-10), [[MTS bundles enterprise solutions under MTS CorpTech brand]] (MTS group product-launch cadence, 2026-10). All are product/feature or regulatory items, not valuation events — confirming there is no comparable priced transaction to multiple against. External peer multiples not computed: YooMoney and SberPay are embedded in Sber, and MTS Bank in PJSC MTS, so no clean standalone revenue/EBITDA figure for the charity/wallet line is publicly disclosed → `[UNSOURCED]`.

**Risk flags.** (1) Traction is negligible: the company itself cites only "first several hundred transactions" to the Sistema fund — a pilot, not a live at-scale product; donation volume and any economics are undisclosed, so materiality to MTS fintech revenue is effectively zero. (2) Related-party optics: the sole launch partner is the affiliated Sistema foundation (AFK Sistema is MTS's controlling shareholder's group), so adoption so far is intra-group, not independent-NKO demand — second-order risk that "proven NKO" onboarding stalls without a captive flow. (3) Disintermediation / me-too: donate-at-checkout is easily replicated and already offered by larger-reach Sber/YooMoney and by MTS's own bank; MTS Pay risks being a late, undifferentiated feature with no pricing power, since it does not own the rails (SBP/SberPay) it depends on.

**What this changes (idea-lens).** For the sector this is a small signal that RU wallets are competing on engagement/ESG features rather than price, extending the "embedded giving" pattern already live abroad (analysis). Falsifiable thesis: MTS Pay charity is an engagement/brand feature, not a growth driver — it will not be broken out in MTS fintech reporting and will stay sub-material. Trigger that would falsify it: MTS disclosing donation TPV, a monetised take rate, or a sizeable roster of unaffiliated NKO partners (beyond Sistema) within ~2–3 quarters.

**IR grounding (company/mts, IR-covered).** Latest result: MTS Q1 2026 press release (earnings_release, dated 2026-05-20). Group figures: consolidated revenue RUB 201.3bn (+14.7% YoY); Group OIBDA RUB 74.7bn (+18.0% YoY); net profit RUB 7.2bn (+46.4% YoY); net debt / LTM OIBDA 1.6x. MTS cites FinTech (alongside Telecom and FunTech) as a primary growth contributor — but no standalone charity/MTS Pay line is disclosed, underlining that this feature is immaterial to the reported fintech segment. Source: https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf (drive_url).

Sources: https://www.cnews.ru/news/line/2026-10-12_mts_predstavila_novyj_instrument · https://www.telecompaper.com/news/mts-adds-charitable-donations-to-mts-pay--1585544 · https://itrussia.media/en/article/mts-bank-integrates-charitable-giving-into-online-14-06-2026 · https://yoomoney.ru/catalogue/charity/all?lang=en · https://www.statista.com/outlook/dmo/fintech/digital-payments/russia · https://www.marketdataforecast.com/market-reports/russia-cards-and-payments-market · https://ir.mts.ru/en/news_and_events/corporate_releases/details/742412 · https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (context-only).** No earnings in the news itself — this is an MTS Pay product/fundraising launch, not a results release. But MTS (parent) IS IR-covered, so here is the financial backdrop from MTS's latest print: **Q2 2026 (reported 2026-08-25)** — group revenue RUB 213.5bn (+9.2% YoY), OIBDA RUB 84.6bn (+16.3% YoY), OIBDA margin 39.6% (vs 37.2% a year ago), net profit RUB 66.9bn (boosted by the tower-business divestment and lower finance costs). Against this, the FinTech segment — where MTS Pay sits — is the group's one soft spot: segment revenue fell -6.1% YoY, the only major segment in decline.

**Key figures (MTS, latest filing period).**
- Group revenue RUB 213.5bn, +9.2% YoY.
- OIBDA RUB 84.6bn, +16.3% YoY; margin 39.6% (+2.4pp YoY).
- Group net profit RUB 66.9bn (lifted by one-off asset sale; not organic).
- Net debt RUB 474.1bn.
- Dividends approved RUB 70bn.

**By segment / driver (where MTS Pay lives).**
- **FinTech (incl. MTS Bank, MTS Pay): revenue RUB 40.5bn, -6.1% YoY** — attributed to falling interest rates compressing lending income. This is the only declining major segment.
- Telecom RUB 136.8bn, +12% YoY; Media (ON Media) RUB 6.9bn, +12.6%; AdTech cluster RUB 19.3bn, +16% (adtech component itself -14.3% to RUB 5.7bn; martech +36.4% to RUB 13.6bn).
- Underneath the soft segment-revenue line, **MTS Bank's own profitability inflected sharply**: Q2 2026 net profit RUB 4.7bn, +89.7% YoY; 1H 2026 net profit RUB 7.2bn, 2.1x YoY (mtsbank.ru). Net interest income pre-provision +34.8% to RUB 14.4bn, post-provision +64% to RUB 8.2bn; ROE 14.9% (vs 8.8% in Q2 2025 and 7.9% in Q1 2026). So the fintech top-line shrinks on rates while bank bottom-line recovers on lower provisioning.

**vs expectations / prior period.** No MTS Pay- or fintech-specific consensus for a product launch. Group Q2: revenue broadly in line with public consensus, OIBDA ahead of expectations (mondiara/Vedomosti coverage). Fintech revenue -6.1% YoY continues the pressure flagged in Q1 2026; MTS Bank net profit nearly doubling is the counter-trend. No prior MTS note in the base to wikilink.

**Guidance / forward.** No fresh fintech guidance tied to this launch. The charitable-donation feature carries no disclosed revenue model, volume target, or take-rate — MTS cites only "first several hundred transactions" to the Sistema foundation (qualitative, not financial). It is a daily-engagement / ecosystem-stickiness play for MTS Pay, not a near-term revenue line; no material P&L impact expected.

**Thesis-flags.**
1. Fintech is MTS's only shrinking segment (-6.1% YoY) on rate-driven lending compression — so MTS Pay engagement features (donations, embedded checkout across Kion/Urent/MTS store) read as an effort to defend transaction volume and payment frequency while the credit side de-risks. Second-order: non-interest/payment income matters more as rates fall.
2. The segment revenue decline masks a real MTS Bank turnaround (net profit +89.7% YoY, ROE 14.9%) driven by lower provisions and NII recovery — the fintech "weakness" is top-line optics, not a franchise problem.
3. The donation feature is announced, not monetized — no take-rate, no volume guidance; treat as ecosystem/brand, not revenue (de-PR: management touts "simplicity" and transaction counts, stays silent on any fee economics).

Sources: MTS Q2 2026 IR release <https://ir.mts.ru/news_and_events/corporate_releases/details/742437> · IR PDF <https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf> (Q1 2026, in irdb) · cnews.ru segment breakdown <https://www.cnews.ru/news/top/2026-08-26_dohody_mts_ot_telekoma_i> · Kommersant <https://www.kommersant.ru/doc/8907646> · MTS Bank 1H 2026 <https://www.mtsbank.ru/o-banke/novosti/detail/1151435/> · Semsearch irdb 402 (OpenRouter credits) — used WebSearch + IR filing list.
<!-- /enrichment:earnings_review -->
