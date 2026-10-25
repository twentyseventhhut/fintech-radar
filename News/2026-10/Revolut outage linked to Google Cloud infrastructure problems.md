---
title: "Revolut outage linked to Google Cloud infrastructure problems"
date: 2026-10-20
retrieved: 2026-10-20
tags:
  - company/revolut
  - company/google
  - industry/neobank
  - industry/infrastructure
  - region/uk
  - type/outage-security
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: se25671c0
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Revolut outage linked to Google Cloud infrastructure problems

> [!info] 2026-10-20 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] У Revolut проблемы из-за Google Cloud. Reuters со ссылкой на источник, знакомый с ситуацией, пишет, что нарушения в работе необанка связаны с проблемами облачной инфраструктуры Google в Лондоне. Проблемы затронули сразу несколько облачных сервисов. Revolut, обслуживающий более 80 млн клиентов по всему миру, столкнулся с нарушениями работы, причём сообщения поступают из Великобритании, Ирландии, Италии, Нидерландов, Румынии и других стран. ⬛️ Клиенты видят сообщения об ошибке и не могут получить доступ к счетам. ⬛️ Часть пользователей сообщает об отклонении карточных операций в магазинах. ⬛️ Есть жалобы на переводы и обмен валют. Revolut подтвердил инцидент и заявил, что деньги и данные клиентов находятся в безопасности. Это важно на фоне последних новостей о взломах и утечках. Последствия шире клиентской базы Revolut: инцидент затронул внешние финансовые сервисы: ▶️ Tink, поставщик инфраструктуры открытого банкинга, сообщил о полном отказе подключения к Revolut в Великобритании.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
### [0] What happened

On the morning of **20 October 2026**, UK-headquartered neobank **Revolut** (80M+ customers globally, ~68.3M retail at end-2025) suffered a broad service outage. Reuters, citing a person familiar with the matter, linked the disruption to a **Google Cloud infrastructure failure in Google's London region (europe-west2)**. Google confirmed services in the region were "experiencing issues" and later attributed the root cause to a **power event in the europe-west2-b availability zone**, beginning ~06:08 UTC (07:08 BST). Multiple Google Cloud services were affected simultaneously.

Impacted Revolut functions (status page listed ~28–31 services partially unavailable): account sign-in, card payments at merchants (declines), top-ups, ATM withdrawals, transfers, currency exchange, stock trading and live-chat support. Reports came from the **UK, Ireland, Italy, Netherlands, Romania and other markets**. Revolut confirmed the incident and stressed **customer money and data remained safe**. Reported duration: roughly ~2 to ~4 hours (reports vary; ~1h48m in one tracker update, resolved later in the day).

### [1] Why it matters

- The incident is a textbook **single-cloud concentration-risk** event: Revolut runs core operations on Google Cloud under a strategic partnership, so a regional power fault cascaded straight into customer-facing banking. See [[Bank of England runs sector-wide cloud outage drill with 38 firms]] — UK regulators had just rehearsed exactly this scenario.
- **Blast radius beyond Revolut**: the same London region event hit banks (Lloyds, Halifax, HSBC, ING Germany per reports) and non-finance services (NHS England, Royal Mail, DPD). **Tink** (open-banking infrastructure) logged "Revolut | Open Banking" as a 100% outage for AIS and PIS — showing downstream dependency chains.
- Reputationally sensitive given Revolut's IPO push and record valuation ([[Revolut hits $121.2B valuation as IPO talk intensifies]]) and its recent security troubles ([[Revolut to cover costs for 680 customers hit by data hack]]).

### [2] Key numbers

- **80M+** global customers (Revolut's own figure); ~68.3M retail at end-2025.
- Google region: **europe-west2 / zone europe-west2-b**; incident start **~06:08 UTC**.
- ~**28–31** Revolut services listed partially unavailable.
- Tink: **100%** of AIS + PIS users affected on the Revolut connection.
- Markets reporting disruption: UK, Ireland, Italy, Netherlands, Romania + others.

### [3] Players

- **Revolut** — affected neobank; confirmed incident, said funds/data safe.
- **Google Cloud** — infrastructure provider; power event in London region is the attributed cause.
- **Tink** — open-banking aggregator reporting full connectivity failure to Revolut UK (downstream victim).
- **Other hit entities** — Lloyds, Halifax, HSBC, ING Germany, NHS England, Royal Mail, DPD (shared-cloud contagion).
- **Reuters** — original source linking Revolut's outage to Google Cloud.

### [4] Context & precedents

- Fits a run of high-profile cloud-infrastructure failures stress-testing fintech resilience; UK's own [[Bank of England runs sector-wide cloud outage drill with 38 firms]] pre-empted this concentration concern. Multi-cloud/exit strategy debate echoes [[Yandex Cloud helps clients migrate to rival providers after outages]] and long-term single-provider bets like [[CaixaBank extends Google Cloud alliance to 2033]].
- Revolut has a recurring reliability tail (status trackers cite ~1,800+ historical outage reports over ~6 years; a multi-hour outage in May 2024).

Sources: Reuters (via report); Bloomberg https://www.bloomberg.com/news/articles/2026-10-20/google-cloud-outage-takes-down-revolut-and-other-banks-in-uk ; CNN https://www.cnn.com/2026/10/20/europe/google-cloud-outage-london-revolut-intl ; Irish Times https://www.irishtimes.com/business/2026/10/20/revolut-services-hit-by-outage-including-in-ireland/ ; Techzine https://www.techzine.eu/news/infrastructure/145123/google-cloud-outage-in-london-causes-global-revolut-disruption/ ; The Journal https://www.thejournal.ie/revolut-outage-customers-card-payments-app-7198815-Oct2026/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions

1. Is the Google Cloud link confirmed or still "person familiar with the matter"? Reuters sourced it anonymously; Google confirmed a London-region power event but has Google/Revolut officially attributed Revolut's outage to it on record?
2. What was the *actual* duration? Trackers disagree (~1h48m update vs ~2–4h); the digest gives no number — avoid asserting a precise figure.
3. How many customers were *actually* unable to transact vs "80M+ could be affected"? The 80M is total base, not impact count — don't conflate.
4. Which exact services failed, and were any (e.g. deposits, FSCS-type protections) never at risk? Status lists "partially unavailable" — degradation, not full blackout.
5. Was this truly single-cloud dependency, or does Revolut have failover that simply didn't trigger for a regional power fault? Resilience design matters for the "concentration risk" framing.
6. Did customers lose money (failed-but-charged card txns, stuck transfers)? Revolut says funds safe — verify no settlement/duplicate-charge fallout.
7. Is the Tink "100% outage" figure Tink's own status wording or independently verified? One-source.
8. Are the other named victims (Lloyds, HSBC, ING, NHS, Royal Mail) confirmed as the *same* root cause, or coincidental same-morning issues?
9. Does "europe-west2-b power event" fully explain a multi-service, multi-country Revolut outage, or were there dependencies outside that single zone?
10. Any regulatory response (FCA/BoE/Central Bank of Ireland) triggered, given the sector-wide cloud drill context? Not yet evidenced.
11. Is this distinct from the same-day [[Revolut hits $121.2B valuation as IPO talk intensifies]] note? Yes — different event; not a duplicate.
12. Historical-outage counts from status-tracker sites (1,800+ reports) are crowd-sourced and noisy — don't present as authoritative reliability metric.
13. Could the outage be partly Revolut-side (deploy/config) with Google as convenient scapegoat? Attribution is early.
14. What's Revolut's remediation/post-mortem commitment? Unknown at publish time.

Importance: 3/5 — major, widely reported outage at a flagship neobank with real transactional and reputational impact, amplified by IPO timing and concentration-risk narrative; but it was a relatively short (hours), no-data-loss infrastructure incident with recovery same day, so lasting significance is moderate rather than structural.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-25]] (2026-10-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Cloud-concentration risk in EU/UK financial services is the live structural theme. In Nov 2025 the ESAs (EBA/EIOPA/ESMA) published the first DORA list of 19 Critical ICT Third-Party Providers — AWS, Microsoft Azure and Google Cloud among them (per openmetal.io / theindustryspread.com, Nov 2025). DORA (Regulation (EU) 2022/2554) has been fully enforceable since 17 Jan 2025 and explicitly requires financial entities to quantify ICT concentration risk and evidence mitigations, with firms retaining continuity responsibility "regardless of where the failure originates." Structure: the cloud layer under fintech is highly consolidated (hyperscaler oligopoly — 3 providers), while the neobank layer above is fragmented; value and resilience bottleneck sits at the infra layer the fintech does not control. "Why now": a London `europe-west2` Google Cloud fault on 20 Oct 2026 (reportedly an electrical event) took down Revolut app access, card auth, transfers and FX for users across UK/IE/IT/NL/RO (per CNN, qz.com, globalbankingandfinance.com, 20 Oct 2026). This lands exactly one year after the 20 Oct 2025 AWS us-east-1 DNS failure that hit Lloyds/Halifax/BoS and ~25% of UK consumers (per Finextra / Retail Banker Int'l) — two hyperscaler-origin financial outages on the same calendar date, a year apart.

**Competitive landscape.** Resilience KPIs for a daily-banking neobank: service uptime / RTO-RPO, number-of-nines, single-vs-multi-cloud posture, and critical-dependency count. Revolut: 68.3m retail customers (+30%) and $6.0bn group revenue (+46%), PBT $2.3bn at a 38% margin for FY2025 (per Revolut IR / CNBC 24 Mar 2026; note the digest's "80m" figure is above the audited 68.3m retail base — treat 80m as an unverified/global-including-business claim). The outage's blast radius exceeded Revolut's own base: Tink (Visa's open-banking aggregator) logged "Revolut | Open Banking" as a 100%-of-users major outage from 07:05 BST for both AIS and PIS, error "Token endpoint unavailable" (per cybersecuritynews.com, datastudios.org) — i.e. a single bank's cloud fault propagated into third-party open-banking rails. Position: Revolut is a scale leader among EU neobanks but, like peers, is a price-taker on hyperscaler reliability; the moat is product breadth/scale (11 product lines each >~$135m revenue), not infra independence (analysis).

**Comps & multiples.** This is an operational-resilience event, not a valuation/round event — EV/Revenue, EV/EBITDA, P/E = not applicable (no listed equity; private, no fresh round here). Distribution not computed; qualitative comparison only. Internal precedent comps (same cloud-outage-hits-fintech pattern):
- [[AWS outage disrupts UK banks' online services]] — Oct 2025, AWS us-east-1, Lloyds/Halifax/BoS.
- [[Coinbase suffers multi-hour trading outage after AWS failure]] — May 2026, AWS dependency on an exchange.
- [[Afterpay hit by major outage across Australia and US]] — Oct 2025, BNPL checkout downtime.
- [[Revolut suspends inbound PayTo top-ups in Australia after security incident]] — May 2026, Revolut's own prior resilience/security incident.
Pattern read: these are recurring, correlated single-provider failures, not idiosyncratic — a GUIDE to systemic concentration, not a per-name valuation signal.

**Risk flags.**
1. Single-cloud concentration / disintermediated reliability — Revolut's availability is hostage to one hyperscaler region (europe-west2); a provider-side electrical/DNS event cascades straight to card auth and account access, which no amount of app-side engineering mitigates. Second-order: DORA requires evidencing concentration mitigation (multi-cloud/hybrid), so this is now a regulatory-exposure event, not just an uptime blip.
2. Contagion into shared rails — the fault propagated to Tink's open-banking AIS/PIS (100% of users), meaning one bank's cloud outage degrades the wider open-banking ecosystem that depends on reachable token endpoints; systemic, not contained.
3. Trust/timing — Revolut framed it as "money and data are safe," but the incident lands amid a run of breach/leak headlines and ahead of its US banking push and 100m-customer-by-2027 target; repeated outages erode the reliability perception a deposit-taking bank needs (analysis).

**What this changes (idea-lens).** Watch for DORA to bite at the provider tier: Google Cloud is already a designated CTPP, so a high-profile financial outage in its London region is exactly the trigger for ESA oversight scrutiny and for banks to be asked to evidence multi-cloud/exit plans. Falsifiable thesis: EU/UK financial entities will visibly accelerate multi-cloud / active-active and critical-dependency disclosure in 2026-27; it's wrong if regulators and firms treat this as another one-off and status-quo single-cloud reliance persists (analysis). Catalyst to watch: any ESA/PRA statement referencing concentration risk, or Revolut disclosing a multi-cloud/failover posture.

Sources: https://www.cnn.com/2026/10/20/europe/google-cloud-outage-london-revolut-intl · https://cybersecuritynews.com/revolut-outage/ · https://www.datastudios.org/post/google-cloud-outage-revolut-uk-banking-payments-october-2026 · https://openmetal.io/resources/blog/what-doras-ict-concentration-risk-requirements-mean-for-eu-financial-infrastructure/ · https://theindustryspread.com/dora-cloud-oversight-splits-eu-uk-us-2026/ · https://www.finextra.com/newsarticle/46782/banks-come-back-online-after-aws-outage · https://www.cnbc.com/2026/03/24/revolut-2025-earnings-record-profit.html · https://assets.revolut.com/pdf/annualreport2025.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
