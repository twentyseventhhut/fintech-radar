---
title: "Sber QR-code payments via QRIS launch in Indonesia"
date: 2026-07-13
retrieved: 2026-07-13
tags:
  - company/sber
  - industry/payments
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-07-06_mws_ai_vylozhila_universalnyj
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s91f72d44
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Sber QR-code payments via QRIS launch in Indonesia

> [!info] 2026-07-13 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Выложил в открытый доступ фильтр AVI, позволяющий настраивать ограничения безопасности для LLM с помощью естественного языка без их переобучения

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-07-06_mws_ai_vylozhila_universalnyj>
*454 слов · direct*

Эльяс Касми
MWS AI выложила «универсальный фильтр» для больших языковых моделей в открытый доступ
Центр искусственного интеллекта МТС MWS AI (входит в МТС Web Services ) совместно с исследователями Корейского университета технологий и образования в Чхонане (Koreatech) разработали AVI (Agreement Validation Interface) – фильтр для нейросетей, который позволяет быстрее обучить и настроить модель ( LLM ) с учетом правил безопасности, законодательства и отраслевых регламентов с помощью естественного языка. Программа-посредник экономит до 10 дней на переобучении модели и доступна в репозитории GitHub. Об этом CNews сообщили представители MWS AI .
Большая языковая модель, на которой не настроены ограничения, может ответить на потенциально опасные вопросы, например, на попытку узнать чужие персональные данные . Для банка, страховой или медцентра это неприемлемо: у каждой отрасли свой список запретных тем, и он постоянно меняется вслед за законодательством. 
Созданный MWS AI совместно с корейскими исследователями универсальный фильтр работает как посредник между человеком и моделью: программа блокирует утечки персональных данных, токсичные ответы и обращения к запрещенным источникам информации, чем экономит временные и финансовые ресурсы пользователей. Доработка фильтра не требует навыков программирования , что делает ее доступной специалистам компании из разных отделов – юридического , финансового, комплаенс – и др.
Достичь такого результата удалось за счет изменения логики – фильтр работает «снаружи», на этапах формулирования вопросов и выдачи ответов, и не внедряется в саму LLM. На входе система уже блокирует запросы с провокациями, запрещенными темами или попытками раскрыть чужие персональные данные. На выходе – не пропускает ответы с оскорблениями, дезинформацией и устраняет риск утечки корпоративных сведений. 
Еще одна особенность решения – возможность задать правила фильтрации словами, а не строками кода. Это позволяет подключить к процессу настройки модели экспертов, которые разбираются в юридических ограничениях и корпоративных регламентах, но не владеют специальными навыками ML-инженеров . 
В ходе тестов фильтр распознал 98,5% опасных обращений в выборке из более чем 2 тыс. примеров на русском языке, в том числе провокации на экстремизм , разжигание ненависти, попытки получить персональные данные, призывы к суициду и незаконным действиям. На запрещенных запросах система прерывала ответ модели сразу при обнаружении нарушения. За счет этого ИИ-помощник реагировал почти в четыре раза быстрее, чем без него. На повторный вопрос система реагировала за доли секунды.
«Управление корпоративным ИИ сегодня — про то, как быстро компания подстроит модель под новое требование или риск, не переобучая ее с нуля. Именно в эту сторону сейчас движутся исследования по всему миру», – отметила профессор Korea University of Technology and Education (Южная Корея), руководитель Global Academia and Research Hub и Digital Professor в НИУ ВШЭ Ольга Швецова . 
Архитектура AVI совместима с любыми большими языковыми моделями. Исходный код фильтра доступен на GitHub . В репозитории находится образец использования фильтра на Python и FastAPI, конфигурации для векторной базы данных Qdrant.
 Лучший российский софт для видеосвязи: ищем замену Teams и Zoom

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sber QR-code payments via QRIS launch in Indonesia
_Analytical notes (not a post). Importance: 3/5._

> **NOTE DATA-QUALITY FLAG:** the aggregated body text of this note is mis-attached — it is about **MWS AI (MTS) releasing an "AVI" LLM safety filter**, which has nothing to do with Sber QR/QRIS. The enrichment below follows the note **title/story** (Sber enabling QRIS payments in Indonesia), corroborated by external Russian wires dated 10 July 2026. The primary-source cnews.ru link in frontmatter is the wrong article.

## [0] What exactly happened (de-PR'd)
On **10 July 2026** Sber (Sberbank) announced — with a live test transaction reported from Bali — that Russian retail customers can now **scan QRIS merchant codes inside the SberBank Online app** to pay at Indonesian merchants, with automatic RUB conversion (amount shown in both IDR and RUB; requires recent app versions). Sber calls Indonesia its **13th country** for in-app cross-border QR, and cites cross-border QR turnover **>2x in Q2** and **>190,000 monthly users** across all its QR-enabled countries (ria.ru, vedomosti.ru, bosfera.ru — all one press release).
- **De-PR'd reality:** this is a **unilateral, Russian-side consumer app feature, NOT an official Bank Indonesia (BI)/ASPI cross-border QRIS corridor.** The confirmed S. Korea and China QRIS links are central-bank-to-central-bank; Russia is **not** on BI's cross-border partner roadmap and there is **no BI/ASPI acknowledgment, no bilateral agreement**. QRIS is merchant-presented (MPM) and interoperable, so *any* app that can push a compliant transaction to a QRIS acquirer can scan the codes — which is exactly the seam Sber is exploiting from the buyer side.
- **Why framed this way / what it reveals:** the press anchors to a flattering, verifiable-looking detail (a Bali restaurant paid, "13th country," 2x turnover) while **omitting every mechanic that matters** — the Indonesian acquirer/partner is **unnamed**, the **settlement rail is undisclosed**, and there is **zero sanctions context**. That omission is the story: a SWIFT/Visa/Mastercard-cut, OFAC/EU/UK-sanctioned bank cannot use the normal national-switch QRIS interconnect, so the routing almost certainly runs through an **unnamed intermediary/local acquirer** with RUB↔IDR conversion handled internally by Sber (analysis). "Live app feature" is confirmed; "sanction-clean, BI-blessed corridor" is not.

## [1] Competitors / peers
The real comparison is "who moves tourist cross-border QR into Indonesia," where the incumbents dwarf Sber:
- **BI's own QRIS cross-border** — live to Thailand (Aug 2022), Malaysia (May 2023), Singapore (Nov 2023), Japan (Aug 2025), **South Korea (1 Apr 2026)**, **China (30 Apr 2026)**; India UPI↔QRIS targeted late 2026. See [[Bank Indonesia expands QRIS to Saudi Arabia and India]], [[Indonesia and South Korea launch cross-border QRIS payments]], [[Indonesia and China launch cross-border QR payments via Alipay+]].
- **Alipay+ / UnionPay** — the de-facto regional alt-rail: Chinese travelers pay at 40M+ QRIS merchants; Indonesian apps scan 80M+ Alipay/UnionPay codes in China.
- **Russia-side alternative:** the **Manna/LinkAja tourist corridor** ([[Russia-Indonesia tourist payment corridor planned via Manna Group]], 2026-07-06) — a *different, non-bank* attempt at the same RUB→IDR tourist problem, still **not launched**. Sber's move is the **bank-side, already-live** answer to the same demand.
- **Why the landscape is this way (2nd order):** the winning corridors are **national-switch to national-switch under both central banks**; Russia is structurally excluded because NSPK/Mir/SBP are sanctioned ([[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]]). So Sber cannot get a *symmetric* link — it can only ride QRIS **one-directionally from the buyer side** via an intermediary. Position: **ahead of other Russian actors (live vs Manna's announcement), but a fringe/gray participant** relative to the BI-sanctioned corridors.

## [2] Company history / fit
Sber has spent 2025-26 pushing in-app cross-border QR across "friendly" markets (Thailand, Vietnam, Philippines named; Indonesia = 13th) as its **substitute for the Visa/Mastercard acceptance it lost in 2022**. It fits Sber's broader post-sanctions playbook of building parallel rails (cf. its crypto/custody and domestic-QR pushes: [[Sberbank plans crypto wallet and custody service by December]], [[Sberbank plans India branch expansion and bond investment]]).
- **Why it acts this way:** with Mir/SBP unable to interconnect abroad, Sber's only route to serve outbound Russian tourists is a **software-side scanner + internal FX** that touches foreign rails through a non-sanctioned intermediary — hence a *consumer-app* feature rather than a bank-to-scheme deal. VTB (~1.3bn RUB foreign-QR volume by June 2026) and MTS Bank do the same; this is a **Russian-banking-sector pattern**, not a Sber first.

## [3] Novelty / value-add / traction
- **Novelty:** moderate. In-app cross-border QR is not new (Alipay+/QRIS do it at scale); the specific novelty is **Sber routing Russian retail payments into QRIS despite sanctions**, which is operationally hard and therefore notable.
- **Traction:** partly real, unlike the Manna announcement — a **live test transaction** and **>190k monthly users** (all-country, not Indonesia-specific) are claimed; but **no Indonesia-specific volume, no named partner, no BI recognition**. So "live for Russian tourists" = plausible; "durable corridor" = unproven.
- **Who captures the margin (analysis):** value sits in the **RUB↔IDR FX spread** on tourist spend. The fragile link is the **unnamed Indonesian acquirer**, which carries **secondary-sanctions exposure** (US Treasury has threatened foreign banks servicing NSPK/Mir). If that counterparty gets cold feet or is named/sanctioned, the corridor breaks overnight — the value-add rests on an intermediary Sber won't disclose.

## [4] What's next / market sentiment
Watch for: (a) any BI/ASPI statement (silence to date suggests this is *not* a sanctioned corridor); (b) the named Indonesian acquirer; (c) whether it survives OFAC scrutiny. Backdrop: Russia–Indonesia local-currency (RUB/IDR) settlement talks are ongoing post-BRICS but with **no deadline**.
- **Why the market goes this way / 2nd order:** the binding constraint is **sanctions/correspondent risk, not tech**. Counterintuitively, the *more visible* Sber makes this, the *more* compliance scrutiny falls on its unnamed Indonesian partner — so publicity can itself endanger the rail. Expect a **quiet, intermediary-fronted, gray-zone** setup rather than a formal corridor; durability is the open question, not existence.

## Freshness / duplicate verdict
**FRESH.** grep over `News/` finds the adjacent [[Russia-Indonesia tourist payment corridor planned via Manna Group]] (2026-07-06), but that is a **different mechanism** (non-bank Manna Group + LinkAja e-wallet, explicitly *not launched, seeking a payment partner*). This Sber item is a **distinct, bank-side, reported-live app feature dated 10 July 2026** — not a reprint or re-framing of the Manna note, and no prior note covers a Sber QRIS/Indonesia launch. Genuinely new.

## Sources
- Sber launch (10 Jul 2026): https://ria.ru/20260710/sber-2104022107.html · https://www.vedomosti.ru/finance/news/2026/07/10/1212754-sber-podklyuchil-oplatu · https://bosfera.ru/press-release/sberbank-zapustil-oplatu-po-qr-kodu-v-indonezii · https://finance.mail.ru/article/sberbank-zapustil-oplatu-po-qr-kodu-v-indonezii-69217210/ · https://investfuture.ru/articles/sberbank-rasshiryaet-oplatu-po-qr-kodu-v-indonezii-cherez-sistemu-qris-1182891050
- QRIS overview/scale: https://en.wikipedia.org/wiki/QRIS · https://www.bi.go.id/en/fungsi-utama/sistem-pembayaran/ritel/kanal-layanan/qris/default.aspx · https://databoks.katadata.co.id/en/finance/statistics/6a3dcaf6cba47/number-of-qris-merchants-in-indonesia-increased-in-q1-2026
- QRIS cross-border: https://www.bi.go.id/en/fungsi-utama/sistem-pembayaran/ritel/kanal-layanan/qris/qris-antarnegara/default.aspx · https://en.tempo.co/read/2101260/indonesia-launches-qris-cross-border-payment-service-with-china · https://fintechnews.id/110259/payments/indonesia-india-qris-upi-payment-linkage/
- Sanctions/rails: https://en.wikipedia.org/wiki/Mir_(payment_system) · https://www.cbr.ru/eng/psystem/sfp/ · https://interfax.com/newsroom/top-stories/101004/ · https://home.treasury.gov/news/press-releases/jy2725
- Competitors / UPI intl: https://fintechnews.id/109836/payments/indonesia-china-qris-cross-border-payment/ · https://vajiramandravi.com/current-affairs/countries-accepting-upi-payment/
- Internal: [[Russia-Indonesia tourist payment corridor planned via Manna Group]] · [[Bank Indonesia expands QRIS to Saudi Arabia and India]] · [[Indonesia and South Korea launch cross-border QRIS payments]] · [[Indonesia and China launch cross-border QR payments via Alipay+]] · [[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 3/5** — Unlike the sibling Manna/LinkAja *announcement* [[Russia-Indonesia tourist payment corridor planned via Manna Group]], this is a **reported-live, dated (10 Jul 2026) bank-side feature** with a claimed test transaction and cross-country usage numbers — genuinely new and materially more real. But it is weighed down: it is a **unilateral Sber-side app scanner, NOT a Bank Indonesia-blessed corridor**; the Indonesian acquirer, the settlement rail, and the sanctions-compliance path are all **undisclosed**, and there is no BI acknowledgment. Notable as a concrete data point on how a sanctioned Russian bank routes tourist payments into ASEAN QR rails; not a structural shift. (Also flagged: this note's aggregated body is mis-attached — it is MWS AI LLM-filter text, not the Sber QRIS story.)

## Red-team / challenge questions
1. **Is this a BI/ASPI cross-border QRIS corridor or a Sber-only app feature?** A Sber-side feature — no BI/ASPI announcement, Russia not on BI's roadmap. **Confirmed (feature, not corridor).**
2. **Who is the Indonesian acquirer/local partner routing Sber into QRIS?** Unnamed in all coverage. **Open — the key gap.**
3. **What is the actual settlement rail (NSPK/SBP + intermediary? correspondent bank?)** Undisclosed; likely intermediary-fronted with internal RUB↔IDR FX. **Open (hypothesis).**
4. **How does a SWIFT/Visa/MC-cut, OFAC-SDN bank clear into QRIS at all?** Only via a non-sanctioned intermediary/local acquirer; the normal national-switch link is closed. **Analysis.**
5. **Is it actually live or just announced?** Reported live with a Bali test transaction; but no Indonesia-specific volume. **Partly confirmed / partly open.**
6. **Fresh vs the Manna note?** Fresh — different mechanism (bank + QRIS, live) vs Manna (non-bank + LinkAja, unlaunched). **Confirmed fresh.**
7. **Are the "13th country / >190k users / 2x Q2" figures Indonesia-specific?** No — they are all-country aggregates from Sber's PR. **Confirmed (aggregate, not Indonesia).**
8. **Does the counterparty face secondary-sanctions risk?** Yes — US Treasury has threatened foreign banks servicing NSPK/Mir; this is why the partner is likely unnamed. **Hypothesis / material risk.**
9. **Is there any Bank Indonesia stance on Russian/sanctioned participants?** No public statement found; BI allows foreign operators "if they don't disrupt payment sovereignty." **Open.**
10. **Who captures the margin?** The RUB↔IDR FX spread on tourist spend; the fragile dependency is the unnamed acquirer. **Analysis.**
11. **Is this a Sber-first or a Russian-sector pattern?** Sector pattern — VTB (~1.3bn RUB foreign-QR by Jun 2026) and MTS Bank do the same. **Confirmed.**
12. **What breaks the corridor?** The intermediary being named/sanctioned, or BI objecting; publicity itself raises that risk. **Hypothesis.**
13. **Does it remove the crypto/USDT workaround Russians use in Bali?** For Sber cardholders scanning QRIS, plausibly yes for merchant payments — but not confirmed for cash-out/remittance. **Partly.**
14. **What would raise importance to 4/5?** A named acquirer surviving OFAC scrutiny + real Indonesia volume, or a formal CBR–BI local-currency settlement deal. **Watch item.**
15. **Does the mis-attached note body undermine the item?** No — the title/story is corroborated by independent 10 Jul 2026 Russian wires; but the note's frontmatter source (cnews.ru MWS AI) is wrong and should be corrected. **Data-quality flag.**
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
> _Note QC flag: this note's aggregated body text is mismatched — it describes MWS AI's (MTS) "AVI" LLM-safety filter, NOT Sber's QRIS launch. Research below follows the note TITLE (Sber QRIS in Indonesia), grounded on primary Sber/RIA coverage of 10 Jul 2026._

**Sector & drivers.** Cross-border interoperable QR is the fast-growing layer sitting on top of domestic instant-payment rails; the "why now" is that acquiring a foreign-tourist wallet no longer requires card-scheme rails (Visa/Mastercard) — it rides the merchant's existing domestic QR. Indonesia's QRIS is the anchor: Bank Indonesia recorded 6.05bn QRIS transactions worth ~IDR 579tn (~$37bn) in H1 2025 (+139% y/y), across ~39–40m merchants and ~57m users (per Bank Indonesia, via ASEAN Briefing / Jakarta Globe, mid-2025). Cross-border QRIS is the hyper-growth sub-segment: cross-border QRIS value surged +225% y/y to ~IDR 1.66tn (~$105m) across Malaysia/Singapore/Thailand by mid-2025 (per Jakarta Globe). BI frames the linkage push explicitly as dedollarisation/local-currency settlement, and has signed or launched links with Thailand, Malaysia, Singapore, Japan (17 Aug 2025), South Korea (Apr 2026), plus UAE/India in the pipeline. Sber's move plugs a Russian issuer into this existing rail rather than building new acceptance.

**Competitive landscape.** Sector KPIs: cross-border TPV, merchant reach (acceptance points), FX spread captured on conversion, and active-user attach. Basis of competition = distribution (which issuer's app the traveller already holds) + FX economics, not merchant-side acceptance (that is BI's QRIS network, shared by all). Recent dated moves: Alipay+ ↔ HUMO (Uzbekistan) cross-border QR, 50+ markets (2025) [[Alipay+ partners HUMO for cross-border QR payments in Uzbekistan]]; Bank of Thailand ↔ China QR linkage (2025) [[Bank of Thailand launches cross-border QR linkage with China]]; Cambodia ↔ Singapore QR (2025) [[Cambodia and Singapore launch cross-border QR payments]]; NPCI/UPI ↔ Bahrain BENEFIT (2025) [[NPCI International and BENEFIT link UPI for India-Bahrain payments]]; BI QRIS → Saudi Arabia + India, cross-border +38% in Q3 2025 [[Bank Indonesia expands QRIS to Saudi Arabia and India]]. Sber's positioning: NICHE / late-follower on a shared rail — it is the traveller-app distributor for outbound Russian tourists, not an interoperability operator. Per Sber, Indonesia is its 13th QR-payment country (after Thailand, Vietnam, Philippines etc.), amount auto-converted to rubles inside SberBank Online, ~40m+ merchant locations reachable (per RIA/Vedomosti, 10 Jul 2026). Moat = Sber's domestic distribution (84.7m SberBank Online MAU, H1 2026) and its RUB-conversion FX engine (analysis); the acceptance side is a commodity it does not own.

**Comps & multiples.** No valuation/round/deal in this news — it is a product connection, not a financing event; trading multiples not applicable → "no data". Comparison is qualitative vs the cross-border-QR peer set above. Franchise scale for context (Sber, RPBU): H1 2026 net profit ₽995bn, +20.4% y/y; SberBank Online MAU 84.7m [[Sberbank H1 2026 net profit rises 20.4% to RUB 995bn]]; latest IFRS 9M/Q3 2025 results 28 Oct 2025 (per IR). Sber is a state-controlled, deeply profitable domestic monopoly monetising outbound-tourist FX at the margin — this launch is immaterial to earnings, strategic optionality only.

**Risk flags.**
1. **Sanctions / correspondent-banking (primary).** Sber is on major Western sanctions lists; EU (from 25 Jan 2026) bars EU entities from connecting to Russian financial-messaging systems (Mir/SBP), and from 14 May 2026 targets non-bank settlement operators used to bypass sanctions (per Matheson / Pravda EN). QRIS rides on Indonesian PSP settlement — the second-order risk is that Indonesian settlement banks with USD correspondent exposure de-risk away from Sber flows, quietly capping or killing the corridor regardless of the tech working.
2. **Settlement-currency opacity.** The app shows rubles to the user, but Sber is silent on the actual RUB↔IDR settlement path (direct, via yuan, or via a payment-agent chain). Payment-agent chains are exactly what the May 2026 EU package targets — corridor durability and FX cost are unverifiable ([UNSOURCED] on the settlement leg).
3. **Adoption / concentration.** Value is capped by outbound Russian tourist volume to Indonesia (thin, seasonal, Bali-weighted) and by whether Indonesian tourism recovers Russian arrivals; it is a marginal-revenue feature, not a franchise driver — execution/scale risk is low-stakes but so is upside.

**What this changes (idea-lens).** Signals Russia's continued pivot to non-Western retail rails via ASEAN QR interoperability, using tourist/remittance flows as the low-friction entry wedge (analysis). Falsifiable thesis: if the corridor is genuine local-currency (RUB/IDR) settlement it survives; if it secretly routes through USD-touching agents it is one sanctions-enforcement action from being switched off. Watch/trigger: Sber (or NSPK, universal-QR operator from 1 Sep 2026) disclosing the settlement mechanism, or any Indonesian PSP publicly withdrawing — either resolves the thesis.

Sources: https://ria.ru/20260710/sber-2104022107.html · https://www.vedomosti.ru/finance/news/2026/07/10/1212754-sber-podklyuchil-oplatu · https://www.aseanbriefing.com/news/indonesias-qris-expansion-across-apec-and-what-it-means-for-businesses/ · https://jakartaglobe.id/business/bi-expands-qris-links-to-seven-countries-to-reduce-dollar-reliance · https://www.matheson.com/insights/the-european-unions-19th-sanctions-package-against-russia-key-takeaways/ · https://www.sberbank.com/investor-relations/groupresults/ifrs_results_for_the_3rd_quarter9oct
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
