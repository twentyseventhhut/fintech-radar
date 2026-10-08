---
title: "Alfa-Bank starts selling its cybersecurity system externally"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - company/alfa-bank
  - industry/regtech
  - industry/banking
  - region/ru
  - type/product
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s10ef82da
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Alfa-Bank starts selling its cybersecurity system externally

> [!info] 2026-10-08 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Альфа-Банк начал продавать собственную систему кибербезопасности внешним клиентам — и это довольно необычно для российского рынка. Похожие технологии есть у других: Т-Банк использует ИИ-систему, которая имитирует действия злоумышленника, ищет слабые места и проверяет возможность реальной эксплуатации, но пока не продаёт её внешним клиентам; Сбер бесплатно предоставляет базу зарегистрированных уязвимостей. То есть технологическая компетенция внутри банков уже сформировалась, а Альфа первой пытается сделать из неё отдельный внешний бизнес. ⚪️ Система на базе ИИ проверяет сайты, приложения, сетевые сервисы и внешний периметр, ранжирует найденные уязвимости и формирует рекомендации. Ранее продукт использовался внутри банка. ⚪️ Начальная цена — около 500 тыс. рублей за контракт продолжительностью от шести месяцев. Стоимость альтернативных решений на рынке оценивается от 1 млн до 100 млн рублей в год. По сути, банк превращает собственные расходы на безопасность во внешний источник выручки

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Alfa-Bank starts selling its cybersecurity system externally
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-10-08 Alfa-Bank commercialized an internally-built security tool as **"Alfa-Scanner"** — a **cloud (SaaS) external-perimeter vulnerability scanner** combining automated tooling + AI classification + the bank's own analyst expertise (Lenta, Gazeta, Kommersant, bfm, 2026-10-08). It scans a company's internet-facing assets (websites, apps, network services, external perimeter), ranks findings by criticality, and produces remediation recommendations. No hardware/software install required (cloud-delivered). Entry price ~500k RUB for a contract of 6+ months; the bank frames rival solutions at 1M–100M RUB/year.
- **De-PR'd:** This is NOT a SOC, SIEM, EDR, or antifraud platform. It is a narrow **external attack-surface / VM (vulnerability management) scanner** — the easiest security capability to productize because it needs no access to the client's internal network, so sales friction and liability are low. The "unique first among banks" claim is about *commercialization*, not technology; scanning is a commodity capability (Positive Technologies MaxPatrol, BI.ZONE CPT, etc. all do it).
- **Why structured this way:** cloud + external-only + low entry price = a lead-gen / land-and-expand motion, not a serious enterprise VM play. The 500k anchor vs "up to 100M" is a classic favorable-base PR framing (comparing a stripped external scan to full enterprise platforms). (analysis)
- **Why it matters (2nd order):** the real story is a Russian bank monetizing an internal cost center as a B2B revenue line — the "bank-as-IT-vendor" pattern, driven by import-substitution demand after Western security vendors exited. (analysis)

## [1] Competitors / peers
- **Positive Technologies** — market leader; MaxPatrol VM, Standoff Bug Bounty (7,870 reports in 2025, +34% y/y). Deep, enterprise, publicly listed. Alfa is far below this.
- **BI.ZONE (Sber group)** — CPT/vuln-assessment + Bug Bounty platform (Alfa itself ran a program on BI.ZONE Bug Bounty, 2025, payouts up to 1M RUB). Moving into EDR/ESP vs Kaspersky by 2027.
- **Kaspersky** — endpoint/platform incumbent.
- **Sber** — provides a registered-vulnerability database for free (per the item) — a different, non-commercial posture.
- **T-Bank** — has an AI red-team/pentest tool but does NOT sell externally (per the item) — confirms Alfa is first to *externalize*.
- **Position:** Alfa is a **niche late entrant in capability, first-mover in packaging** among banks. Real cyber vendors dwarf it; the differentiation is distribution (existing corporate client base) + price, not tech. (analysis)

## [2] Company history / fit
- Alfa has been building security muscle visibly: bug-bounty on BI.ZONE (2025, raised payouts to 1M RUB), Security Vision SOAR/SGRC deployment, AI for transaction-safety confirmation, and a CIPR-2026 memorandum with "Kod Bezopasnosti" on joint banking/IT solutions.
- Fits the broader Alfa pattern of turning internal infrastructure into external products: crypto international settlements for corporates ([[Alfa-Bank launches crypto international settlements for corporates]], 2026-07, imp 4), crypto depositary plans ([[Alfa-Bank plans own crypto depositary after peers]], 2026-07), and Multibank for corporates ([[VTB and Alfa-Bank roll out Multibank service for corporates]], 2026-06). Also note the big-bank-as-platform ambition in [[Russia's central bank rejects Sber, Alfa, T-Bank payment system project]].
- **Why:** Russian banks are among the best-capitalized IT shops in the country; with foreign vendors gone, selling in-house capability to their SME/corporate clients is a natural B2B cross-sell. (analysis)

## [3] Novelty / value-add / traction
- **New:** first Russian bank to *sell* a vulnerability-scanning service externally as a product (commercialization novelty). Technologically it is not new — external VM scanning is mature and crowded.
- **Traction:** NONE disclosed — no client count, no revenue, launched the same day as the news (announcement, not adoption). Treat as **launch, not proven business**.
- **Value-add reality:** modest. The scanner competes in the most commoditized security segment; margin/moat is thin. The durable asset is Alfa's **corporate client distribution**, not the AI. Who captures margin: likely the bank keeps it only if it bundles scanning into broader corporate relationships; standalone, it is squeezed by PT/BI.ZONE on depth and by price pressure. (analysis)

## [4] What's next / market sentiment
- **Market:** Russia cybersecurity ~USD 7.75B in 2026, CAGR ~8.3% to ~USD 11.56B by 2031 (Mordor Intelligence); structurally boosted by the Dec-2024 import-substitution decree blocking foreign products. Tailwind is real.
- **Likely path:** Alfa expands from external scanning toward managed VM / pentest-as-a-service and bundles with corporate banking. Watch for client numbers in 6–12 months to validate.
- **Risks:** (1) commoditization — PT/BI.ZONE out-feature it; (2) trust/conflict — some firms wary of letting a *bank* scan their perimeter; (3) it may stay a marketing/lead-gen feature rather than a real revenue line. Counterintuitive 2nd-order: the low 500k price signals Alfa is buying client logos, not margin. (analysis)

## FRESHNESS / DUPLICATE VERDICT
**FRESH.** This is a genuine new event: product launch of "Alfa-Scanner" on 2026-10-08, confirmed independently by Lenta, Gazeta, Kommersant and bfm on that date. Prior Alfa cyber items in the corpus are different (bug-bounty program in 2025, crypto/payments products) — none covers this commercialization. No duplicate in the News/ corpus.

## Sources
- Lenta (2026-10-08): https://lenta.ru/news/2026/10/08/alfa-bank-zapustil-ii-servis-dlya-zaschity-biznesa/
- Gazeta (2026-10-08): https://www.gazeta.press/business/news/2026/10/08/29483767.shtml
- Kommersant: https://www.kommersant.ru/doc/9008607 ; https://www.kommersant.ru/doc/9008615
- bfm: https://www.bfm.ru/news/620294
- Mordor Intelligence, Russia Cybersecurity Market: https://www.mordorintelligence.com/industry-reports/russia-cybersecurity-market
- anti-malware (BI.ZONE vs PT/Kaspersky ESP): https://www.anti-malware.ru/news/2026-04-23-111332/49806
- computerra (Alfa on BI.ZONE Bug Bounty, 2025): https://www.computerra.ru/318269/alfa-bank-zapuskaet-programmu-poiska-uyazvimostej-na-bi-zone-bug-bounty/
- cisoclub (Alfa + Kod Bezopasnosti, CIPR-2026): https://cisoclub.ru/alfa-bank-i-kod-bezopasnosti-podpisali-memorandum
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team challenge questions

1. **Is this actually a new product or a re-announcement of the 2025 bug-bounty program?** New — "Alfa-Scanner" is a separate SaaS scanner launched 2026-10-08; the 2025 item was a bug-bounty program on BI.ZONE. Distinct. (resolved)
2. **SOC/SIEM/antifraud or just a scanner?** Just an external-perimeter vulnerability scanner — the narrowest, most commoditized security capability. Not a platform. (resolved)
3. **Is "first bank to sell this" a tech claim or a packaging claim?** Packaging only; the scanning tech is mature and widely sold by PT/BI.ZONE. (resolved)
4. **Is the 500k RUB vs "up to 100M" comparison honest?** No — it compares a stripped external scan to full enterprise platforms; favorable-base framing. (analysis)
5. **Any traction — clients, revenue, pilots?** None disclosed. Launch-day announcement. (open — watch 6–12 months)
6. **Why external-only and cloud?** Lowest sales friction and liability (no internal network access), enabling a land-and-expand motion. (analysis)
7. **Where is the real moat — AI or distribution?** Distribution (Alfa's corporate client base); the AI is table-stakes. (analysis)
8. **Will corporates trust a bank to scan their perimeter?** Possible conflict/trust friction; unquantified. (open)
9. **Who captures the margin standalone vs bundled?** Likely thin standalone; value only if bundled into corporate banking relationships. (analysis)
10. **How big/real is the import-substitution tailwind?** Real — ~USD 7.75B market 2026, +8.3% CAGR, Dec-2024 decree blocks foreign vendors. (resolved)
11. **Can Alfa out-compete PT/BI.ZONE on depth?** No — those are dedicated, deeper, and (PT) listed. Alfa competes on price/access only. (analysis)
12. **Is this a revenue line or a marketing/lead-gen feature?** Low price signals lead-gen / logo acquisition more than margin. (hypothesis)
13. **Any regulatory/CB angle?** None specific; general IB import-substitution policy backdrop. (resolved)
14. **Fits Alfa's strategy?** Yes — matches its pattern of externalizing internal infra (crypto settlements, depositary, Multibank). (resolved)
15. **Duplicate in corpus?** No — unique event, fresh. (resolved)

Importance: 3/5 — Real, independently confirmed launch and a genuinely novel *commercialization* move (bank-as-cybersecurity-vendor) riding a strong import-substitution tailwind. But capped by: commodity capability, zero disclosed traction, a late/niche position behind Positive Technologies and BI.ZONE, and a low price point suggesting lead-gen over a material revenue line. Notable pattern, not yet a material business.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russia cybersecurity (ИБ) market ~337bn rubles in 2024, expected +20–25% to exceed 400bn rubles in 2025 (per TAdviser, via search, as of 2025–26); a Dec-2024 import-substitution decree structurally shields domestic vendors by blocking many foreign products, so demand is captive and growing (regulation-driven, not purely cyclical). Structure: consolidating around a few scaled domestic vendors (Kaspersky, Positive Technologies, BI.ZONE, Solar, Group-IB/F.A.C.C.T.) after Western exits; value sits in the software/SOC/managed-services layer. Why now: sanctions-forced import substitution + rising attack volume on Russian targets makes external-perimeter scanning / EASM a growth subvertical, and banks — already heavy ИБ spenders — are trying to turn internal cost centres into revenue (bank-tech commercialization). De-PR: Alfa's product is the "Альфа-сканер" cloud service for AI-assisted vulnerability discovery on the external perimeter (sites, apps, network services), confirmed by Kommersant — this is a narrow EASM/vuln-scan tool, NOT a full ИБ platform.

**Competitive landscape.** Subvertical KPIs: contract count / ARR, external-perimeter assets under scan, number of validated vulnerabilities, price-per-contract. Players & basis of competition: Positive Technologies (public, result-driven security, products + SOC), BI.ZONE (platform of 40+ products incl. EASM / BI.ZONE CPT), Kaspersky, Solar, Group-IB — competing on product breadth, platform lock-in and distribution; Alfa enters at the low-price, single-product end. Recent moves: BI.ZONE completed transition to a unified platform model in 2025; Positive Group lifted delivery volumes to ~35bn rubles in 2025. Among banks, T-Bank runs an internal AI attacker-simulation tool and Sber gives away a vulnerability database — but neither sells externally (per the note); Alfa is first to commercialize. Position: niche new entrant / first-mover among banks on commercialization, but a late, sub-scale entrant versus dedicated ИБ vendors. Moat: weak — the only differentiators are a low price (from ~500k rubles for a 6-month contract vs 1m–100m rubles/yr cited for alternatives) and in-house credibility as a large bank; no network effects or switching costs yet (analysis). CAC/LTV, contract pipeline, external revenue target → `[UNSOURCED]`.

**Comps & multiples.** External, public:
- Positive Technologies / Positive Group — FY2025 revenue 30.9bn rubles (+26% IFRS, per TAdviser), market cap >200bn rubles in 2024 (per search). P/S ≈ 200bn / 30.9bn = ~6.5x (mixing a 2024 cap with 2025 revenue — directional only, treat as `[UNSOURCED]` for a clean multiple).
- BI.ZONE — 2025 revenue 24.9bn rubles (+16.7% YoY from 21.36bn; note one source cites a decline to 21.3bn — figures conflict, flag). Private, no public cap → EV/Revenue = no data.
Internal comps: no comparable Russian cybersecurity-vendor deals/valuations found in the base via grep (sem down, OpenRouter 402); corpus cyber hits are global fraud/Trojan items, not comparable. Distribution not computed (<3 comparable figures) → qualitative only. Read: Alfa's offering is orders of magnitude smaller than either peer's revenue base; the ~500k-ruble entry price undercuts the market but implies tiny per-contract economics — rich/cheap framing N/A (no Alfa financials disclosed).

**Risk flags.**
1. Sub-scale, single-product entrant vs platform incumbents (BI.ZONE 40+ products, Positive ~31bn-ruble revenue) — an AI vuln-scanner is easily matched/bundled by vendors, so first-mover status among banks ≠ durable moat; price-led entry invites margin compression (disintermediation by the vendor stack).
2. Conflict-of-interest / trust: a competitor bank buying critical-security tooling from Alfa, and clients exposing external-perimeter data to a rival bank, caps the addressable market (second-order: Alfa may end up selling mainly to non-bank SMEs, limiting scale).
3. No disclosed economics — revenue target, pipeline, margin all silent; "turning cost into revenue" is PR framing until live-adoption numbers appear (execution risk). The note gives no customer count or contracts signed.

**What this changes (idea-lens).** Signals a bank-tech commercialization trend: Russian banks, flush with internal ИБ/AI competence and shielded by import substitution, probing whether in-house security can become a B2B line (analysis). Falsifiable thesis: if Alfa discloses >50 external contracts or a stated revenue target within ~12 months, bank-as-ИБ-vendor becomes a real category and Sber/T-Bank follow; trigger = a published client/revenue number. What breaks it: no adoption disclosed, trust/conflict friction confines it to a marketing halo rather than a standalone business.

Sources: https://www.kommersant.ru/doc/9008615 · https://www.kommersant.ru/doc/9008607 · https://tadviser.com/index.php/Article:Information_security_(Russian_market) · https://tadviser.com/index.php/Article:Positive_Technologies_financials · https://interfax.com/newsroom/top-stories/116028/ · https://tadviser.com/index.php/Company:BI.Zone_(Secure_Information_Zone,_Bison) · https://www.mordorintelligence.com/industry-reports/russia-cybersecurity-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
