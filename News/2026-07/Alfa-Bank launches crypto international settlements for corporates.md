---
title: "Alfa-Bank launches crypto international settlements for corporates"
date: 2026-07-10
retrieved: 2026-07-10
tags:
  - company/alfa-bank
  - industry/crypto
  - industry/b2b-payments
  - region/ru
  - type/product
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: s85db7f93
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# Alfa-Bank launches crypto international settlements for corporates

> [!info] 2026-07-10 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Альфа-Банк вывел в публичный контур сервис международных расчётов в криптовалюте для корпоративных клиентов. Банк обещает проводить платежи по внешнеторговым контрактам без ограничений по минимальной и максимальной сумме, доставлять деньги контрагенту за две минуты и сопровождать операцию в соответствии с валютным законодательством. «Коммерсантъ» указывает комиссию от 0,16% с последующим повышением до 0,3% с 1 сентября. По понятным причинам Альфа-Банк не раскрывает публично участников цепочки, используемые токены и зарубежную инфраструктуру. Запуск очень интересный: в банковском контуре наконец-то появился сервис, который обещает бизнесу мгновенные и дешёвые криптоплатежи за рубеж. Выглядит так, что продукт встроен в привычный контур ВЭД наряду с валютным контролем, документами и расчётным счётом. Клиенту продают не токен и не криптокошелёк, а результат: контрагент должен получить деньги по контракту. Это сильный конкурент А7 — не только по стоимости, скорости или другим характерист

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Alfa-Bank launches crypto international settlements for corporates
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
Alfa-Bank — Russia's largest **private** bank — moved a **crypto international-settlements service for corporate (ВЭД/foreign-trade) clients into public availability**, listing it on its own site (alfabank.ru/corporate/ved/cryptocurrency/). This is **DISTINCT** from the [[Alfa-Bank plans own crypto depositary after peers]] story (that is *retail investment/custody* under the ~Sept-2026 law); this is a **B2B cross-border-payments** product settling foreign-trade contracts in crypto. (fact)

De-PR'd concrete terms (Kommersant 2026-07-08/10, Финтехно, Alfa site):
- **No minimum or maximum ticket** on payments under external-trade contracts. (bank claim — unverified in practice)
- **~2-minute delivery** to the counterparty. (bank claim)
- **Full currency-control wrap**: payment executed "in accordance with currency legislation" — i.e. sits inside the normal ВЭД contour (settlement account, documents, currency control). (fact/claim)
- **Fee from 0.16%**, rising to **0.3% from 1 Sept 2026** (reduced rate reportedly effective to 30 June per site fine print — treat exact cutoff as **open**). Kommersant flags the 0.16% as a **marketing hook** to undercut the incumbent A7 (which charges from 0.3%). (fact + analyst read)
- Alfa **does not disclose** the chain participants, the tokens used, or the foreign infrastructure "for obvious reasons" (sanctions). (fact — deliberate opacity)
- Alfa reportedly **plans to apply to join the CBR's cross-border experimental legal regime (ЭПР/ФЗ №223-ФЗ)** pilot. (analysis/reported — implies the current offer may run partly outside the formal ЭПР today)

**Why structured this way / what it reveals:** The pitch is **"we sell the outcome, not the token"** — the client is not sold a wallet or a coin, but *"your counterparty receives the money under the contract."* Crypto is hidden middleware inside a familiar ВЭД wrapper (currency control + documents + settlement account). This is the key delta vs standalone crypto-OTC/A7: Alfa bundles the sanctions-evasion rail into a **licensed bank's** compliance perimeter, so a corporate treasurer gets a bank invoice and currency-control paperwork, not a grey-market P2P headache. Second-order: pinning the mechanism to currency legislation is also how Alfa keeps the CBR/Rosfinmonitoring visibility that the [[Russia adds crypto cross-border rules to trade settlement bill]] amendments now *require* (auto-reporting ≥10m₽; travel-rule from 60k₽) — the product is being built to fit the surveillance perimeter that is being legislated in parallel.

## [1] Competitors / peers
On-topic = Russian sanctions-driven crypto/stablecoin B2B cross-border rails, NOT global stablecoin settlement (Circle/Visa etc. are walled off from RU).
- **A7 (Promsvyazbank-linked)** — the incumbent Alfa is explicitly attacking. A7 launched late-2024, ran **>₽7.5T in H1-2025**, and now reportedly handles **~19% of all Russian foreign-trade operations** (was "every 5th payment" per Feb-2026). Uses the **A7A5 ruble-pegged token** (first token to get ЦФА status, Sept-2025); issued bills/векселя reportedly **₽6.1T** (TASS). Commission **0.3%** (import; 0% export). A7A5 was **US/UK-sanctioned** in 2025 — a live example of the secondary-sanctions risk (analysis). (dates/figures: www1.ru, tass.ru, a7-agent.ru)
- **Standalone crypto-OTC / P2P agents & vc.ru "оплата инвойса криптой"** schemes — fragmented grey market Alfa is trying to formalize into a bank contour.
- **Sberbank / T-Bank / VTB** — announced *retail* crypto (custody/depository), not (yet) a public B2B cross-border-settlement product — so on THIS use-case Alfa is arguably **ahead of the other big banks**, behind only the specialist A7. ([[Sberbank plans crypto wallet and custody service by December]], [[Russian app to add crypto buy, sell and storage in 2026]])
- Digital ruble (CBR) — the *state's* preferred long-run cross-border rail, still in test ([[Bank of Russia tests digital ruble for deposits and credit]]); Alfa's crypto product is a market-led stopgap while the digital ruble and ЭПР mature.

**Position:** Alfa is a **credible fast-follower to A7 but the first Tier-1 universal bank** to put a public crypto-ВЭД product on its site. **Why the landscape looks this way (analysis):** A7 proved the demand (₽7.5T+) and the model (ruble-pegged token + currency-control wrap); Alfa's edge is *brand + banking licence + an existing ВЭД client base* — it can cross-sell to corporates who already bank with it and who distrust a semi-opaque payment agent. The 0.16% loss-leader signals Alfa is buying share, not margin, in the opening window — classic incumbent-disruption via a trusted balance sheet.

## [2] Company history / fit
Alfa has deep DLT/tokenization prior art, so this is an incremental extension, not a cold start:
- **2018** — joined R3 Corda consortium; first in Russia on the Contour blockchain trade-finance network. (grokipedia/coin-turk — treat as background)
- **2023-05** — CBR-licensed **ЦФА/DFA issuance operator** (A-Token platform, ~60% of RU DFA trading volume). (see [[Alfa-Bank plans own crypto depositary after peers]] market research)
- **2026-05-29** — launched **BTC/ETH-linked ЦФА** for qualified investors.
- **2026-07-08** — public crypto **B2B cross-border-settlements** product (this note) + separately the retail depository plan.

**Why Alfa acts this way (analysis):** Alfa is a top ВЭД bank whose corporate franchise is being strangled by SWIFT/correspondent-banking exclusion (OFAC/EU/UK-sanctioned). Crypto cross-border settlement is a **defensive retention play** — keep ВЭD clients from defecting to A7 or to DIY crypto agents — more than a growth play. Structural pressure: without a working cross-border rail, Alfa's corporate deposit/FX/trade-finance revenue erodes; a bundled crypto rail is how it defends that book.

## [3] Novelty / value-add / traction
**Novelty:** the *category* (crypto B2B cross-border) is NOT new (A7 has run it at scale since 2024). The genuine increment is **a Tier-1 bank productizing it publicly inside a licensed currency-control contour** — turning a grey/agent-mediated flow into a bank product with an invoice and compliance. Novelty is **jurisdictional + distribution/packaging**, not technical.

**Traction:** essentially **unproven** — this is a **just-launched product page** with bank *claims* (no min/max, 2-min delivery). **No disclosed volumes, no client counts, no named corridors, no tokens/chains disclosed.** Contrast A7's hard ₽7.5T/₽6.1T figures — Alfa has zero comparable traction data yet. So: **announced-and-listed, not proven-at-scale.**

**Who captures the margin (analysis):** whoever controls the **off-shore leg / liquidity + the token** captures the real spread; Alfa, by hiding "chain, tokens, foreign infrastructure," is signalling it relies on undisclosed intermediaries (likely USDT/stablecoin OTC), so Alfa may be a **distribution front-end** over someone else's rails — margin could leak to the liquidity provider, exactly the "who pays vs who dashboards" question. The 0.16%→0.3% path implies thin economics; durable value = the ВЭД client relationship + currency-control compliance, not the payment fee.

## [4] What's next / market sentiment / regulatory backdrop
- **Regulatory:** operates against the **ЭПР (ФЗ №223-ФЗ, cross-border crypto since Sept-2024)** and the market bill's second-reading cross-border amendments ([[Russia adds crypto cross-border rules to trade settlement bill]]): auto-reporting to Rosfinmonitoring ≥10m₽; travel-rule threshold cut to 60k₽; CBR veto extended to banks. Alfa says it **will apply to the ЭПР pilot** — watch whether the current public offer is fully inside the regime or ahead of it. Since March-2024, FX-denominated ЦФА/stablecoins are **currency values** under RU currency law.
- **Watch:** first disclosed volumes/corridors; whether A7's ~19% share erodes; whether the CBR admits Alfa to the ЭПР; whether the undisclosed token gets sanctioned (as A7A5 was).
- **Risks:** heavy **secondary-sanctions exposure** — Alfa is OFAC/EU/UK-listed and the EU 20th package bans EU-person dealings with RU crypto providers; the settlement token/venue is a single point of failure (cf. A7A5 designation); opacity ("we don't disclose tokens/infra") is itself a red flag and a compliance risk for counterparties; fee compression to 0.3% + a low-margin race.

**Why the market goes this way / counterintuitive (analysis):** Sanctions are *manufacturing* a domestic crypto-payments industry that Western regulators will keep trying to sever — so the "winner" is whoever can rebuild the plumbing fastest after each designation, not whoever is cheapest. Alfa's bank wrapper is more resilient than a standalone agent (harder to fully sanction a systemic domestic bank's onshore rails), which is the real second-order reason a Tier-1 bank, not just A7, is now in this market.

## Sources
- Kommersant (2026-07-08/10) — «Альфа-банк стал предлагать трансграничные расчёты для бизнеса в крипте»: https://www.kommersant.ru/doc/8800045
- Alfa-Bank product page — «Международные платежи в криптовалюте»: https://alfabank.ru/corporate/ved/cryptocurrency/
- finance.mail.ru (2026-07) — «Альфа-банк запустил международные криптопереводы для бизнеса»: https://finance.mail.ru/article/alfa-bank-zapustil-mezhdunarodnyie-kriptoperevodyi-dlya-biznesa-69217111
- investfuture.ru (2026-07-08) — Alfa tests crypto trading before 2026 launch (context): https://investfuture.ru/articles/alfa-bank-nachinaet-testirovat-torgi-kriptovalyutoy-pered-zapuskom-v-2026-1182779768
- vc.ru — «Криптовалюта в расчётах по ВЭД: что разрешает новый российский закон»: https://vc.ru/crypto/2997401-kriptovaljuta-v-mezhdunarodnoj-torgovle
- A7 scale — www1.ru (2026-02-05, ~every 5th / ₽7.5T H1-2025): https://www1.ru/news/2026/02/05/dengi-iz-monopolii-kazdyi-piatyi-platez-vo-vnesnei-torgovle-rossii-proxodit-cerez-platformu-a7.amp.html
- A7 векселя ₽6.1T — TASS: https://tass.ru/ekonomika/27204711
- A7 Agent (0.3% commission): https://www.a7-agent.ru/
- logirus.ru — «Стейблкоины, крипта и расчётная суета» (ЭПР/USDT/currency-value context): https://logirus.ru/articles/ved/steyblkoiny-_kripta_i_raschetnaya_sueta.html
- Internal: [[Alfa-Bank plans own crypto depositary after peers]], [[Russia adds crypto cross-border rules to trade settlement bill]], [[Sberbank plans crypto wallet and custody service by December]], [[Russian app to add crypto buy, sell and storage in 2026]], [[Bank of Russia tests digital ruble for deposits and credit]], [[Russian central bank open to stablecoins only for external settlements]], [[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Freshness verdict: FRESH (distinct product).** There IS a prior Alfa crypto note — [[Alfa-Bank plans own crypto depositary after peers]] (2026-07-08) — but that is the **retail investment/custody depository** story under the ~Sept-2026 law. THIS note is a **B2B corporate cross-border-settlements product** (foreign-trade contracts, 0.16%→0.3% fee, 2-min delivery) publicly listed on Alfa's site. Different customer (corporates vs qualified retail), different mechanism (payments vs custody), different figures. **Not a duplicate — a genuinely distinct, newly-launched product.** No prior note covers a Russian bank's public crypto-ВЭД payment product.

**Red-team / challenge questions:**
1. Duplicate of the Alfa crypto-depository note? — **No.** That is retail custody/investment; this is corporate cross-border *payments*. Distinct product line, distinct audience. (answered)
2. Announced or live? — **Live-ish**: publicly listed on alfabank.ru with concrete terms and a dated fee schedule (0.16% now → 0.3% from 1 Sept). But **zero disclosed volumes/clients/corridors** → productized-and-listed, not proven-at-scale. (answered/nuanced)
3. Is the 0.16% fee real or bait? — Kommersant/experts call it a **marketing hook** to undercut A7's 0.3%; it auto-rises to 0.3% on 1 Sept 2026. Reduced-rate cutoff date is inconsistent in sources (30 June vs "next two months"). (answered — treat exact cutoff as open)
4. What token/chain is used? — **Undisclosed by design** ("for obvious reasons"). Likely USDT/stablecoin OTC + an undisclosed ruble-pegged instrument (analysis). This opacity is a red flag. (open)
5. Is it inside the ЭПР legal regime? — Alfa reportedly **plans to apply** to the CBR cross-border ЭПР pilot — implying the current offer may run partly outside the formal regime today. (open — flag)
6. Who is the real incumbent/competitor? — **A7** (Promsvyazbank-linked): ~19% of RU foreign-trade ops, ₽7.5T H1-2025, ₽6.1T векселя, A7A5 ruble-pegged token, 0.3% fee. Alfa explicitly targets it. (answered)
7. Does Alfa have real traction? — **No data.** No volumes, clients, corridors disclosed — vs A7's hard billions. (open — the key weakness)
8. Is this technically novel? — No; A7 has run crypto-ВЭД at scale since 2024. Alfa's increment is a **Tier-1 bank packaging it in a licensed currency-control contour**. Jurisdictional/distribution novelty, not technical. (answered)
9. Is Alfa ahead of Sber/T-Bank/VTB here? — On *this* B2B cross-border product, **yes** — the others announced *retail* crypto, not a public ВЭД payment product. Behind only specialist A7. (answered)
10. Where's the margin / who captures it? — Likely the **off-shore liquidity provider / token issuer**, not Alfa; Alfa may be a distribution front-end over someone else's rails. Durable value = ВЭД client relationship + compliance, not the thin fee. (analysis)
11. Sanctions exposure? — High: Alfa is OFAC/EU/UK-sanctioned; EU 20th package bans EU-person dealings with RU crypto providers; the settlement token is a single point of failure — A7A5 was already US/UK-sanctioned. (answered)
12. What's the strategic logic? — **Defensive retention** of ВЭД corporate clients bleeding to A7/DIY agents amid SWIFT exclusion — not primarily growth. (analysis)
13. What is Alfa silent about? — Tokens, chains, foreign infrastructure, volumes, corridors, counterparty-KYC on the foreign leg, fraud/settlement-failure liability. (open — large)
14. What breaks the thesis? — Sanction of the undisclosed token/venue; CBR denying ЭПР admission; A7 defending its ~19% via price; the market bill's tighter reporting (Rosfinmon ≥10m₽, 60k₽ travel rule) raising friction; fee compression to unprofitability. (open — downside triggers)
15. Does the parallel regulation help or hurt? — Both: [[Russia adds crypto cross-border rules to trade settlement bill]] legitimizes the channel but also extends CBR veto to banks and tightens reporting — Alfa is building to fit that perimeter. (answered)

Importance: 4/5 — First **Tier-1 universal bank** to put a **public crypto cross-border-settlements product for corporates** into its licensed ВЭД contour, directly attacking the proven ~₽7.5T A7 channel — materially more significant than the crowded "we plan retail crypto" bank announcements because it targets a **live, sanctions-critical ~$11bn+/yr trade-settlement flow** and a real incumbent. Held below 5/5 by: **zero disclosed traction** (claims only, no volumes/clients), deliberate opacity on tokens/chain/infra, unresolved ЭПР legal status, thin/loss-leader economics, and heavy secondary-sanctions fragility (a single token designation could sever it).
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-10]] (2026-07-10).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Distinct product from Alfa's retail crypto-custody push ([[Alfa-Bank plans own crypto depositary after peers]]): this is **corporate cross-border trade settlement in crypto** for ВЭД clients. Size of the addressable pool: **crypto-facilitated Russian foreign trade reached ~1tn₽ / ~$11bn in 2025** (mostly China, Turkey, India — oil/metals/grain invoices), per secondary coverage of MinFin data (as of 2026); Russia's **total daily crypto turnover ~50bn₽ / ~$650M (~10tn₽ / ~$130bn/yr)** per Deputy FinMin Chebeskov (Feb 2026, via CoinDesk). **Structure:** this is a **sanctions-workaround payment rail**, not an open market — legal only inside the CBR **experimental legal regime (ЭПР)** for select exporters/importers (live since 2024), with domestic crypto payments still banned; any transfer **>100k₽ (~$1,300) must be reported to CBR + Rosfinmonitoring**, and the coming bill №1194918-8 licenses only a handful of venues (reported ~8). Entry barrier is therefore **regulatory access + counterparty/liquidity relationships offshore**, not technology. **Why now:** crypto-for-foreign-trade becomes broadly legal from the bill's entry into force (targeted ~1 Sept 2026, slipped from 1 July); a bank moving the grey-market ЭПР flow into a **licensed banking contour** (currency control + settlement account + documents) is the "why now." 3 dated facts above.

**Competitive landscape.** Sector KPIs: **take rate (commission)**, settlement speed/finality, ticket-size limits, corridor/liquidity depth. Basis of competition = **price + speed + compliance packaging**, not product novelty (crypto rails are commoditised). **Recent moves / players:**
- **A7 / A7A5 ecosystem** — the incumbent Alfa's own PR explicitly targets ("сильный конкурент А7"): a Kremlin-backed (state PSB holds ~49% of A7) payment-agent + ruble-pegged stablecoin rail; A7A5 **processed a reported $72bn (TRM) to ~$120bn (issuer claim) in 2025** ([[Russia's A7 cross-border payments firm plans global expansion]], [[Sanctioned Russian crypto network expands across Africa]]). Heavily sanctioned (OFAC, EU 19th/20th packages, UK).
- **B-Crypto + Rosbank** — Moscow fintech settling exporter trade in virtual currency via **OFAC-designated Rosbank** (Elliptic, 2026).
- **CBR/policy backdrop** — regulator open to **stablecoins only for external settlements** ([[Russian central bank open to stablecoins only for external settlements]]).
**Protagonist's position:** Alfa is a **new-entrant challenger** to A7/B-Crypto with a genuine wedge — it bundles crypto settlement **inside a regulated bank** (валютный контроль + расчётный счёт), selling "the counterparty gets paid," not a token/wallet. Commission **0.16% (promo) → 0.3% from 1 Sept 2026**, no min/max ticket, ~2-min delivery (Alfa / Kommersant, Jul 2026). Moat (analysis) = **regulatory-trust + distribution intangibles** (Alfa is a licensed bank inside the ЭПР contour vs. sanctioned standalone agents), not any technical edge. Alfa does **not disclose** the token(s), chain-of-intermediaries, or offshore infrastructure — deliberately opaque.

**Comps & multiples.** No deal/valuation/round attaches — Alfa is **private, OFAC/EU/UK-sanctioned, and gives no segment financials**, so EV/Revenue, EV/EBITDA, P/E, price-per-transaction = **no data / [UNSOURCED]** (no numerator, no denominator). No clean listed pure-play comp exists (A7 is a private sanctioned entity; Rosbank/PSB are state-linked conglomerates). **Distribution not computed — qualitative only.** The one hard, comparable sourceable metric is the **take rate**: Alfa **0.16%→0.3%** vs. the opaque, higher-friction sanctioned-agent spreads A7/B-Crypto embed — i.e. Alfa is priced **cheap-to-undercut** as a share-grab, consistent with experts flagging 0.16% as a **marketing loss-leader** (Kommersant). Internal comps (all RU sanctions-era cross-border rails, `[[wikilink]]`): [[Russia's A7 cross-border payments firm plans global expansion]], [[Sanctioned Russian crypto network expands across Africa]], [[Russian central bank open to stablecoins only for external settlements]], [[Alfa-Bank plans own crypto depositary after peers]].

**Risk flags.**
1. **Secondary-sanctions / correspondent risk (structural, severe).** Alfa is OFAC/EU/UK-listed; the **EU 20th package (crypto measures from 24 May 2026) bans EU-person transactions with Russia-established crypto/payment-agent rails** and explicitly targets agents settling trade in tokens like A7A5. Second-order: any offshore exchange/custodian/counterparty in Alfa's undisclosed chain risks designation, so the rail's durability depends entirely on **non-Western liquidity providers continuing to take the sanctions risk** — a single OFAC action on a node can sever a corridor (cf. Grinex halting after a 2026 cyberattack).
2. **Opacity = un-auditable execution + AML exposure (structural).** Alfa hides tokens, intermediaries, and foreign infrastructure "по понятным причинам." Second-order: clients cannot assess counterparty/settlement-finality risk, and every >100k₽ leg is reportable to CBR/Rosfinmonitoring — a compliance/AML surface that can be tightened or frozen by the regulator at will, and that makes the "2-minute, unlimited" promise fragile under stress.
3. **Margin / commoditisation (competitive).** 0.16% is a flagged loss-leader; at 0.3% Alfa competes on price against A7's entrenched corridors. Second-order: because the value is **corridor liquidity + compliance packaging, not tech**, whoever holds the deepest offshore counterparty network keeps the margin — Alfa must win liquidity relationships it does not disclose it has, or the take rate compresses toward zero in a price war.

**What this changes (idea-lens).** This is a **legitimisation / consolidation** event, not a re-rating (analysis): a top-tier *licensed bank* stepping into a niche previously served by sanctioned standalone agents (A7, B-Crypto) signals the state wants ВЭД crypto settlement pulled into the **regulated, monitorable banking contour** ahead of the ~Sept-2026 law — exactly the "additional, not alternative" pattern seen when the CBR blocked the banks' private payment system ([[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]]). **Falsifiable thesis:** if Alfa's bank-wrapped rail wins corporate ВЭД flow from A7 on price + compliance comfort, expect Sber/T-Bank/VTB to launch mirror corporate-settlement products within ~2 quarters. **What breaks it:** an OFAC/EU designation of Alfa's specific crypto-settlement node, a CBR tightening of the ЭПР, or A7's entrenched corridor liquidity proving un-dislodgeable at 0.3%. **Trigger to watch:** first disclosed transaction volumes, or a competitor bank matching the 0.16%/2-min offer.

Sources: https://alfabank.ru/corporate/ved/cryptocurrency/ · https://www.kommersant.ru/doc/8800045 · https://www.coindesk.com/business/2026/02/16/russia-s-daily-crypto-turnover-is-over-usd650-million-ministry-of-finance-says · https://beincrypto.com/russia-crypto-payments-foreign-trade-july/ · https://www.theblock.co/post/398402/russias-crypto-bill-first-reading · https://www.elliptic.co/blog/eu-20th-sanctions-package-targets-the-architecture-of-crypto-sanctions-evasion · https://foreignpolicy.com/2026/03/31/russia-sanctions-evasion-cryptocurrency-a7a5-kyrgyzstan-exports-dual-use-technology/ · https://www.coindesk.com/business/2026/07/03/this-sanctioned-russian-stablecoin-claims-it-processes-billions-but-blockchain-analysts-disagree
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
