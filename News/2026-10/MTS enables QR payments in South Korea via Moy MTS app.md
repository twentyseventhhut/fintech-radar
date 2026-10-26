---
title: "MTS enables QR payments in South Korea via Moy MTS app"
date: 2026-10-26
retrieved: 2026-10-26
tags:
  - company/mts
  - industry/payments
  - region/ru
  - type/product
sources:
  - https://www.rbc.ru/rbcfreenews/6adb77165ea18da5a7ad8fb9
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sd905168e
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# MTS enables QR payments in South Korea via Moy MTS app

> [!info] 2026-10-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Запустил оплату товаров и услуг в Южной Корее по местным QR-кодам через приложение Мой МТС

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.rbc.ru/rbcfreenews/6adb77165ea18da5a7ad8fb9>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MTS enables QR payments in South Korea via Moy MTS app
_Analytical notes (not a post). Importance: 2/5._

## [0] What happened
On 2026-10-26 Russian telecom/fintech group MTS (ПАО «МТС») launched in-store payment for goods and services in South Korea via local QR codes through its consumer super-app **"Мой МТС" (Moy MTS)**. MTS says it is the **first Russian company** to enable this capability in South Korea. Users open Moy MTS → "Деньги" (Money) tab → "Оплата по QR-коду" (Pay by QR) → scan the merchant QR at checkout. Funds can be drawn from the MTS **mobile account balance** or from **cards of Russian banks** added to the app; operations are **commission-free, charged in Russian rubles with conversion to South Korean won**. (Reported single-transaction cap cited by press: ~400,000 RUB.)

## [1] How it works technically — the rails
This is the load-bearing detail. The South Korea payment flows through **GME**, a South Korean fintech platform built for foreigners, riding the **national Zero Pay QR infrastructure** (a government-backed, low/zero-fee merchant QR scheme). Acceptance is anywhere the **Zero Pay logo** appears on the till/terminal — covering large, mid-size and small retail. The design goal: let Russian tourists scan *local domestic* QR codes directly, without installing a separate Korean app and without a local bank card/account. This matters because, under sanctions, Russian-issued Visa/Mastercard do not work abroad and UnionPay acceptance is patchy; MTS instead bridges a Russian funding source to a *local domestic* QR rail via a foreigner-facing intermediary (GME), settling the FX internally.

## [2] Part of a broader cross-border QR campaign
This is one more market in MTS's steadily expanding "оплата за границей по QR-коду" program, not a one-off. The same Moy MTS QR mechanism has been rolled out across popular destinations for Russian travelers. Prior installment in this vault: [[MTS enables local QR payments in Colombia and Argentina]] (2026-10-19) — same app, same funding model (mobile balance or Russian bank cards). MTS marketing lists ~11 countries live (China, Turkey, Egypt, Thailand, Vietnam, Cambodia, Kyrgyzstan, Tajikistan, Uzbekistan, Azerbaijan, Armenia), and earlier launches named Brazil (via Pix), Mongolia, Belarus, India, Philippines. Each market rides a *different domestic QR rail* (Zero Pay/GME in Korea, Pix in Brazil, etc.), so the pattern is "integrate one local QR network at a time." South Korea is notable as a developed, non-friendly-aligned market where Russian cards are otherwise unusable.

## [3] Why it matters / strategic read
- For MTS this is a **retention + payments-monetization play on the Moy MTS super-app**: it keeps subscribers inside the MTS ecosystem for overseas spend and generates FX/payment flow MTS controls, rather than ceding it to banks or card networks.
- For Russian consumers it is a workaround to the post-2022 loss of international card acceptance — a recurring theme in Russian fintech: domestic players stitch together QR-based cross-border rails (MTS here; others via UnionPay, crypto, or local-QR bridges).
- South Korea adds a *developed-market* notch to a program that had skewed toward CIS, Asia and friendly-aligned destinations.

## [4] Open questions / watch items
- Who bears FX spread if the operation is "commission-free"? Revenue likely sits in the ruble→won conversion margin.
- Durability: GME/Zero Pay or Korean authorities could restrict a Russian-funded flow; sanctions-compliance risk for the Korean intermediary.
- Scale is unproven — single-market tourist payments, no volume disclosed; importance is strategic-signal, not financial.

## Related notes
- [[MTS enables local QR payments in Colombia and Argentina]]
- [[MTS Pay adds separate charitable-donation transactions]]
- [[MTS Bank app adds rail and air ticket purchases]]
- [[MTS Bank enables money transfers inside Max chats]]

## Sources / URLs
- RBC (note source): https://www.rbc.ru/rbcfreenews/6adb77165ea18da5a7ad8fb9
- CNews: https://www.cnews.ru/news/line/2026-10-26_mts_zapustila_oplatu_tovarov
- Expert.ru: https://expert.ru/news/mts-zapustil-oplatu-po-qr-kodu-v-yuzhnoy-koree
- Frank Media: https://frankmedia.ru/312072
- 1prime (ПРАЙМ): https://1prime.ru/20261026/mts-874599244.html
- Vesti: https://www.vesti.ru/ns/mts-realizovala-oplatu-po-qr-kodam-v-yuzhnoj-koree
- MForum: https://www.mforum.ru/news/article/130752.htm
- MTS service page (QR abroad): https://nsk.mts.ru/personal/servisy/oplata-zagranicej-po-qr-kodu
- Telecompaper (Brazil/Pix precedent): https://www.telecompaper.com/news/mts-expands-qr-payments-to-brazil--1580883
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
# Challenge / red-team

1. Is "first Russian company to enable QR payments in South Korea" an MTS marketing claim or independently verified? All sources trace to the MTS press release — treat as vendor claim.
2. "Commission-free" — is it truly free, or is the cost hidden in the ruble→won FX conversion spread? No disclosed FX rate or markup; likely the real revenue line.
3. What is the actual single-transaction / daily limit? Press cites ~400k RUB for Korea, but earlier program materials cited 800k RUB — which applies here, and are there aggregate caps?
4. Who is the counterparty of record — is MTS Bank, MTS the telco, or a payment-ops subsidiary the settlement entity? The note tags company/mts (telecom), not mts-bank; confirm which balance sheet carries the flow.
5. GME is a Korea-based foreigner-facing fintech — does routing Russian-funded payments through it create sanctions-exposure for GME/Zero Pay, and could it be shut off quickly?
6. Does this depend on a correspondent/settlement bank willing to handle RUB↔KRW under sanctions? If that link breaks, the service breaks.
7. Is the funding source genuinely "any Russian bank card," or only specific issuers/MTS Bank cards? Prior QR-abroad launches implied broad card support but acceptance varies.
8. Is acceptance really "most retail points," or only Zero Pay merchants (a government scheme with limited penetration vs. card terminals)? Zero Pay coverage in Korea is not universal.
9. iOS vs Android — early program notes said QR-pay launched on Android first; is South Korea live on both platforms now?
10. Transaction volume / user uptake: zero numbers disclosed. Is this a material payments business or a PR/retention gesture?
11. Is this genuinely new vs. the Colombia/Argentina launch a week earlier — i.e., same plumbing, new flag? It is a distinct domestic rail (Zero Pay/GME vs. LATAM rails), so fresh, but strategically incremental.
12. FX/consumer-protection: what happens on refunds, chargebacks, or disputes on a QR payment routed through a foreign intermediary? Likely weak recourse.
13. Regulatory durability in Korea: could Korean FSC/sanctions enforcement treat a Russian-telco-funded payment rail as a compliance problem?
14. Could the "mobile account balance" funding route hit AML/limits scrutiny (effectively using telecom prepaid as a payment instrument abroad)?
15. Is there any MTS financial upside large enough to move the parent's numbers, or is this purely ecosystem stickiness for the Moy MTS super-app?

Importance: 2/5 — Strategically interesting as another node in MTS's sanctions-era cross-border QR rollout and the first into a developed, non-aligned market (South Korea, via GME/Zero Pay), but it is an incremental geographic extension of an existing product with no disclosed volumes, no financial materiality, and vendor-sourced claims. Higher than a routine product tweak because of the sanctions-workaround and super-app-monetization angle; capped at 2 because it is one more flag on an established program.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**What launched.** MTS added in-store QR payments in South Korea inside its consumer super-app "Moy MTS" ("Мой МТС"), letting users scan local QR codes to pay for goods and services. Per Russian trade press (CNews, Frank Media, Prime, 26 Oct 2026), the rail is Korea's national **Zero Pay** QR scheme, intermediated by **GME**, a Korean fintech built for foreign residents/tourists. Users can fund payments from their MTS mobile-account balance or from Russian bank cards; transactions clear in rubles with on-the-fly conversion to KRW, stated as commission-free, with a per-operation cap of ~RUB 400k. MTS claims to be the first Russian company to offer this in Korea. Sources: [CNews](https://www.cnews.ru/news/line/2026-10-26_mts_zapustila_oplatu_tovarov), [Frank Media](https://frankmedia.ru/312072), [Prime](https://1prime.ru/20261026/mts-874599244.html).

**Why it exists (sector context).** Since 2022, Visa/Mastercard do not work for Russian-issued cards abroad, and UnionPay distanced itself from sanctioned Russian banks over secondary-sanctions fear ([Payments Dive](https://www.paymentsdive.com/news/russia-pivots-to-unionpay-for-payments-alternative/620254/)). Russian travellers abroad are therefore served by a patchwork of app-based QR workarounds that plug a domestic wallet/card into a foreign national QR rail via a local intermediary. This is now a competitive land-grab among the largest Russian banks:
- **Sber** is the pace-setter: foreign-QR volume in Q1 2026 ran ~5x the full-year 2025 total; it operates across Turkey, Vietnam, China, Kyrgyzstan, Tajikistan, Belarus, Uzbekistan, Armenia, Azerbaijan, Thailand, Indonesia, Philippines (~13 countries), with VTB and T-Bank following in mid-2026 ([Interfax](https://interfax.com/newsroom/top-stories/102052/), [Izvestia](https://iz.ru/en/node/2016688)).
- Notably, Sber's cross-border QR is reportedly open to clients of four banks incl. **MTS Bank** — so MTS's own-app route in Korea is both a complement and a hedge against dependence on a competitor's rail.

**In-base comparables (news DB).**
- `[[News/2026-10/MTS enables local QR payments in Colombia and Argentina]]` (2026-10-19) and MTS's Brazil launch — same "Moy MTS" + local-QR + mobile-balance/Russian-card model, confirming Korea is one node in a deliberate multi-country rollout, not a one-off.
- `[[News/2026-06/Alipay launches cross-border QR payments in Kyrgyzstan]]`, `[[News/2026-04/WeChat Pay expands cross-border QR across five countries]]`, `[[News/2025-12/China and Vietnam launch cross-border QR payment pilot]]`, `[[News/2026-03/ShopeePay integrates Alipay+ for cross-border QR payments]]` — the global template (Alipay+/WeChat/UnionPay interoperable QR) that the Russian players are reproducing in a sanctions-walled-off variant.

**IR grounding (primary evidence).** MTS Group Q1 2026 results (press release 2026-05-20; [filing PDF](https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf), latest in `ir_latest.json` — note this lags the current quarter): consolidated revenue RUB 201.3bn (+14.7% y/y), OIBDA RUB 74.7bn (+18%), Group net profit RUB 7.2bn (+46.4%). **FinTech vertical revenue +18.4% y/y**; **MTS Bank net profit RUB 2.5bn (x2.6 y/y)**, retail loan book RUB 325.7bn ([Group Q1 2026 figures](https://www.content-review.com/articles/74372/), [BFM on MTS Bank](https://www.bfm.ru/news/607202)). Context from the 2024 annual report fintech section: fintech operating income RUB 74.7bn in 2024 (+15.5% y/y), with explicit strategy language on "development of payment infrastructure" and the MTS Money/ecosystem push — i.e., the Korea QR feature sits inside an already-material, growing fintech segment rather than being a marketing stunt. Material-reality check: a commission-free travel-payments feature is a customer-retention / ecosystem-engagement play (drives "Moy MTS" DAU and keeps balances on-platform); it is not disclosed as a standalone revenue line and should not be read as near-term fintech P&L uplift.

**Risk flags (skeptical).**
1. **Single-source, vendor-PR origin.** The claim rests on MTS's own announcement relayed by Russian outlets (RBC/CNews/Prime); no independent confirmation of coverage breadth, uptime, or that "first Russian company in Korea" is literally true. Treat "commission-free" and the RUB 400k limit as issuer-stated, likely subject to change.
2. **Intermediary & rail dependency.** Function depends on GME and the Zero Pay network; acceptance is limited to merchants displaying Zero Pay, which is far from universal in Korea (Zero Pay skews to small merchants/public programs, not major retail/transit). Real-world usability may be narrow.
3. **Sanctions / counterparty continuity.** Any Korean intermediary touching Russian-bank funds faces secondary-sanctions and compliance exposure; the service could be curtailed at short notice, as happened with UnionPay. FX conversion economics (who sets the RUB/KRW rate, hidden spread) are unverified despite the "no commission" headline.
4. **Competitive commoditization.** Sber/VTB/T-Bank are expanding the same capability faster and across more countries; MTS's differentiation is thin and the feature is easily matched, limiting any durable moat or pricing power.
5. **Not financially quantified.** No disclosed KPIs (users, volume, incremental revenue) for the cross-border QR product; impact on the +18.4% fintech growth is unmeasurable and presumed immaterial for now.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Financial context for MTS's fintech push (latest reported: Q2 2026, released 25-26 Aug 2026).** The Moy MTS South Korea QR-payment launch is a product/ecosystem move, not an earnings event; the backdrop below frames the financial standing of MTS's fintech arm.

**Group results (Q2 2026, IFRS):**
- Group revenue: RUB 213.5bn, +9.2% YoY — driven by telecom/B2B rather than fintech. Telecom segment RUB 136.8bn (+12.2%); AdTech RUB 19.3bn (+16%); MWS (cloud/IT) RUB 15bn (+7%).
- Group OIBDA: RUB 84.6bn, +16.3% YoY (from RUB 72.7bn) — margin expansion on cost optimisation.
- Net profit: RUB 66.9bn vs RUB 2.8bn a year earlier (~24x), but largely a one-off: boosted by the sale of a stake in the tower-infrastructure subsidiary plus lower interest expense. Core operating momentum is better read off OIBDA.
- H1 2026: revenue RUB 414.7bn (vs RUB 370.9bn H1 2025); OIBDA RUB 159.4bn (+17.1%).

**Fintech segment / MTS Bank — the relevant line for this story:**
- Fintech segment revenue: RUB 40.5bn, **down 6.1% YoY** — the only major segment to contract, attributed by MTS to falling interest rates compressing net interest income.
- MTS Bank net profit, by contrast, **+89.7% YoY to RUB 4.7bn** in Q2 — profitability improved sharply even as top-line revenue fell, signalling a pivot toward margin/quality over balance-sheet growth.
- Retail loan portfolio: RUB 306.8bn at quarter-end.

**Beat / miss / in-line:** Group = beat (revenue +9.2%, OIBDA +16.3%, net profit flattered by a one-off asset sale). Fintech segment = miss on revenue (-6.1%), but MTS Bank bottom line a clear beat (+89.7%). Net read for the fintech thesis: in-line-to-mixed.

**Thesis flags for the fintech expansion:**
- Rate sensitivity is the key risk: fintech revenue is shrinking purely on lower rates, so MTS is leaning on fee/transaction and ecosystem revenue (cross-border QR payments, super-app engagement via Moy MTS) to diversify away from spread-dependent income. The South Korea QR launch fits this fee/engagement-led diversification.
- Rising bank profitability (+89.7%) with a controlled loan book suggests capacity to fund ecosystem/product initiatives from within the fintech vertical rather than relying on group subsidy.
- Net-profit optics are inflated by the tower-stake disposal; recurring fintech economics should be judged on segment revenue trend and MTS Bank net profit, not the headline group figure.

Figures from MTS Q2 2026 reporting (released 25-26 Aug 2026). Latest filing indexed in ir_latest.json is Q1 2026 (press release 2026-05-20, https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf); Q2 2026 figures cross-checked via MTS IR (https://ir.mts.ru/news_and_events/corporate_releases/details/742437), Telecompaper, Kommersant and CNews.
<!-- /enrichment:earnings_review -->
