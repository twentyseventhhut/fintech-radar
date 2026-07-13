---
title: "MWS Cloud launches fastest S3 storage for ML workloads"
date: 2026-07-02
retrieved: 2026-07-02
tags:
  - company/mws-cloud
  - industry/infrastructure
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://spark.ru/startup/mts-tb/blog/340020/mws-cloud-zapustila-samoe-bistroe-s3-hranilische-na-rinke-dlya-ml-zadach
status: published
n_mentions: 1
channels:
  - "42 секунды"
story_id: sf12e0cb8
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# MWS Cloud launches fastest S3 storage for ML workloads

> [!info] 2026-07-02 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Spark: MWS Cloud запустила самое быстрое S3-хранилище на рынке для ML-задач

## Первоисточники

### spark.ru
<https://spark.ru/startup/mts-tb/blog/340020/mws-cloud-zapustila-samoe-bistroe-s3-hranilische-na-rinke-dlya-ml-zadach>
*382 слов · jina*

MWS Cloud, входит в МТС Web Services, расширила возможности сервиса Object Storage, представив новый «тёплый» класс хранения. Он предназначен для сценариев, где критически важны высокая скорость доступа к данным, минимальные задержки и стабильная производительность при работе с большими объёмами информации.

**Мнение автора может не совпадать с мнением редакции**

**Новый класс ориентирован на высоконагруженные веб-приложения, проекты в области искусственного интеллекта и машинного обучения, аналитические платформы и системы потоковой обработки данных. По результатам внутреннего тестирования новый класс является самым быстрым решением среди крупнейших российских провайдеров на данный момент. С методологией и результатами исследования можно ознакомиться на****сайте MWS****.**

Рост бизнеса требует инфраструктуры, способной не только надёжно хранить большие объёмы данных, но и обеспечивать быстрый доступ к ним. Это особенно важно для проектов в области искусственного интеллекта, аналитики больших данных, медиасервисов и других ресурсоёмких приложений, где скорость чтения и записи напрямую влияет на производительность. Для таких сценариев MWS Cloud разработала новый «тёплый» класс хранения на базе высокопроизводительных NVMe-накопителей, который обеспечивает минимальные задержки и высокую скорость работы с данными.

По результатам внутренних тестов новый класс хранения демонстрирует скорость передачи данных до 1,8 ГиБ/с при загрузке объектов объёмом 64 МБ и время до получения первого байта (TTFB) около 20 мс. Такие показатели позволяют использовать сервис для задач, требующих быстрого доступа к большим объёмам данных и высокой интенсивности операций чтения и записи.

Решение подходит для обучения и эксплуатации моделей машинного обучения, обработки больших массивов данных, работы с медиаконтентом, высоконагруженных веб-сервисов и корпоративных приложений, в которых данные постоянно используются в рабочих процессах и должны быть доступны практически мгновенно.

Новый класс хранения совместим с AWS S3 API и поддерживает масштабирование без ограничений по объёму данных и количеству объектов. Пользователям доступны шифрование данных, версионирование объектов и управление их жизненным циклом, а также гибкая настройка прав доступа с помощью IAM-ролей и Bucket Policy. Для повышения отказоустойчивости данные реплицируются между двумя дата-центрами. Оплата сервиса осуществляется по модели pay-as-you-go— только за фактически использованные ресурсы.

> Сегодня скорость работы сданными становится одним изключевых факторов эффективности цифровых сервисов. Особенно это актуально для проектов, связанных сискусственным интеллектом, аналитикой иобработкой больших объёмов информации, где каждая миллисекунда задержки влияет напроизводительность истоимость вычислений. Новый «тёплый» класс хранения позволяет получить производительность, сопоставимую снаиболее быстрыми сетевыми дисками, сохранив при этом преимущества работы собъектным хранилищем— бесшовное масштабирование, удобство автоматизации иинтеграции саналитическими системами вроде Lakehouse,
> —отметил Даниил Пивоваров, CPO MWS Cloud.

0

В избр.Сохранено

## Контекст

<!-- enrichment:context -->
# Context-enrichment: MWS Cloud launches "fastest" S3 storage class for ML workloads
_Analytical notes (not a post). Importance: 2/5._

**Freshness: FRESH** — no prior MWS / mws-cloud note exists in the corpus (internal sem search returned zero relevant hits; the only mws-cloud-tagged note is this one). First coverage of MWS Cloud and of this specific "warm" NVMe storage-class launch. Not a duplicate. Corpus has no Russian-cloud object-storage prior art at all — this is a new company thread for the vault.

## [0] What exactly happened (de-PR'd)
On **2026-07-02** MWS Cloud (the cloud arm of MTS Web Services / МТС) added a new **"warm" (тёплый) storage class** to its S3-compatible Object Storage, built on **NVMe** drives. Vendor-stated specs, from **MWS's own internal tests**: up to **1.8 GiB/s throughput on 64 MB object uploads**, **TTFB ~20 ms**. Features: AWS S3 API compatibility, encryption, versioning, lifecycle, IAM roles, Bucket Policy, replication across **two data centers**, pay-as-you-go. CPO **Daniil Pivovarov** quoted (his framing: performance "comparable to the fastest network disks" while keeping object-storage benefits like Lakehouse integration).

**The load-bearing claim — "the fastest S3 storage on the Russian market for ML" — is MWS's own headline, not an independent finding.** It rests entirely on undisclosed internal testing (no concurrency, region, client, or sample-size methodology published; a link to "MWS's site" is asserted but the methodology was not verifiable). A trade-press pickup (IT-World, same day) **dropped the "fastest" superlative** and described the class factually — a tell that the leadership claim is marketing, not editorial. → Why framed this way: MWS is a **mid/low-tier** RU S3 player (bottom third of the first CNews S3 rating, Feb 2026; ~6% of the RU cloud market) filling a gap in a **young** product line (Object Storage standard class only launched spring 2025). A superlative is the cheapest way for a challenger to earn a headline. (analysis)

## [1] Competitors / peers
Russian S3 / object-storage field (AWS/Azure/GCP effectively exited RU post-2022, so this is a domestic contest):
- **Selectel** — the direct rebuttal to "novel" and "fastest": already runs **NVMe-backed hot tiers** with a documented hot/standard/cold/ice taxonomy; publishes **aggregate** ~100–200k RPS and 150–200 Gbit/s per installation (cluster numbers, not per-object, so not apples-to-apples with MWS's 1.8 GiB/s single-object figure). Ranked **#1** in the first CNews RU S3 rating (Feb 2026).
- **Yandex Object Storage** — standard + cold, 3-replica across AZs (stronger durability than MWS's dual-DC), S3-compatible; no public per-object TTFB/throughput numbers.
- **Cloud.ru (ex-SberCloud) "Evolution Object Storage"** — S3-compatible with documented classes; ~32.5% RU cloud share (segment leader). **VK Cloud, Т1, Timeweb, Croc** also in the field.
→ Why the lay of the land matters: MWS competes on a **speed** axis that the market's own rating (CNews) does NOT score — the rating weights fault tolerance, security, functionality, support, where MWS sits at ~300 pts (near bottom). So "fastest" targets a dimension where MWS can self-declare a win while it lags on the dimensions buyers actually rate. The superlative is **sectoral positioning, not verified leadership**. (analysis)

## [2] Company history / fit
MTS Web Services ("MWS") is MTS's consolidated IT/cloud subsidiary (MWS Cloud + cybersecurity + AI/MWS GPT). Company-stated 2025 revenue **63.8 bn ₽** (+9.6% YoY; external revenue +53%); MWS Cloud revenue +40%, OIBDA >2×. CEO Pavel Voronin targets **>200 bn ₽ capitalization by end-2028**. MWS Cloud Platform public cloud launched **2025** (public-cloud announcement ~Oct 2025); Object Storage standard class spring 2025; cold class planned 2026; this warm/NVMe class now July 2026. → Why: a telecom monetizing spare data-center + AI-compute capacity into a domestic cloud, riding import substitution; rapid class-by-class buildout is the natural cadence of a **young** object store racing to feature parity. IPO-in-2026 is **not confirmed** — only the 2028 cap target is on record (open).

## [3] Novelty / value-add / traction
**Novelty: low-to-moderate.** A "warm NVMe object-storage class" is **standard industry practice**, not a first: AWS shipped **S3 Express One Zone** (single-digit-ms, up to ~10× faster than S3 Standard) in **2023**, and Selectel already runs NVMe hot tiers domestically. MWS's real contribution is **feature parity in its own line**, not category invention. **Traction: none cited** — no customers, GMV, or third-party benchmark at launch; this is a **capability announcement**, not a proof point. → Where the value-add is / isn't real: the genuine value-add is **domestic, ruble-priced, 152-ФЗ-compliant, S3-API-compatible** storage that lets RU firms lift-and-shift AWS-targeted ML pipelines — that's real and demand-driven. But "fastest for ML" is unproven: MWS's ~20 ms TTFB is **good-for-RU yet ~2–4× slower than AWS S3 Express One Zone (≈5–10 ms)**, and the release claims **no compute co-location** (the actual source of AWS's ML latency edge), so the ML-training benefit is asserted, not demonstrated. (analysis)

## [4] What's next / market sentiment
RU cloud infra ~**416.5 bn ₽ in 2025**, forecast **>1.2 tr ₽ by 2030** (~24% CAGR); PaaS fastest-growing. Import substitution keeps S3-API compatibility the core sell. Watch: MWS cold class (2026), whether MWS ever publishes a real benchmark methodology, and whether it climbs the CNews S3 rating. → Second-order: in a market where all domestic providers converge on "S3-compatible + ruble + compliant," **differentiation collapses to price, durability SLA, and ecosystem (compute/Lakehouse) — not a single throughput number.** A challenger leading with an unaudited speed superlative signals it lacks a durable moat, which is why the real question is not "is it the fastest" but "can MWS bundle storage with MTS's compute/AI to win the ML platform, not just a disk." (analysis/hypothesis)

## Sources
- Primary (note): spark.ru — https://spark.ru/startup/mts-tb/blog/340020/mws-cloud-zapustila-samoe-bistroe-s3-hranilische-na-rinke-dlya-ml-zadach
- MWS newsroom (launch): https://mws.ru/news/ ; IT-World pickup (2026-07-02): https://www.it-world.ru/news-company/mfh0ulo74o0kos8804w408gko04gs8k.html
- MWS Object Storage: https://mws.ru/cloud-platform/object-storage/ ; MWS profile: https://www.tadviser.ru/index.php/Компания:MTS_Web_Services,_MWS
- Selectel S3/NVMe: https://selectel.ru/services/cloud/storage/ ; https://selectel.ru/blog/how-we-build-s3/
- CNews first RU S3 rating (Feb 2026): https://www.cnews.ru/reviews/servisy_v_obektnyh_hranilishchah_s3/articles/cnewsmarket_opublikoval_pervyj_rejting_1
- RU cloud market size: https://www.comnews.ru/content/242275/2025-11-12/2025-w46/1008/obem-rossiyskogo-oblachnogo-rynka-k-2030-g-pereydet-za-1-trln-rub
- AWS S3 Express One Zone (baseline): https://aws.amazon.com/s3/storage-classes/express-one-zone/ ; Yandex: https://yandex.cloud/en/services/storage ; Cloud.ru: https://cloud.ru/products/evolution-object-storage
- Internal corpus: no prior MWS / mws-cloud / RU-object-storage note found (sem search empty; this is the first).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. Is the launch independently confirmed? Partly — event dated 2026-07-02 is real, but only via MWS's own release + a same-day trade re-post (IT-World). No independent verification of specs. (confirmed event / unverified performance)
2. Where does "fastest S3 on the RU market" come from? MWS's own headline; IT-World's pickup dropped the superlative. Marketing claim, not verified.
3. Is 1.8 GiB/s internal or independent? MWS "internal tests" (внутренние тесты). No third party. Methodology link asserted but not verified.
4. Was any test methodology published? Not verifiable — no concurrency, region, client, or sample-size disclosure. Open.
5. Is 1.8 GiB/s single-stream or aggregate? Stated "on 64 MB object uploads" reads as single-object; unclear vs concurrent workloads. Open.
6. How does ~20 ms TTFB compare globally? Faster than commodity S3 (~50–150 ms) but ~2–4× slower than AWS S3 Express One Zone (≈5–10 ms). Good-for-RU, not a global record.
7. Is a warm NVMe object-storage class novel? No — AWS S3 Express One Zone (2023) and Selectel's NVMe hot tiers predate it. This is feature parity, not invention.
8. Do RU competitors publish comparable numbers? Selectel publishes higher aggregate RPS/throughput (cluster, not per-object); few RU providers publish per-object TTFB at all. Partly open.
9. Is the CPO (Pivovarov) quote/title verifiable? Quote appears in the primary source; independent confirmation of title not established. Treat as company statement.
10. Where does MWS actually rank in RU S3? Bottom third of the first CNews S3 rating (Feb 2026, ~300 pts) and ~6% of the RU cloud market — contradicts a "leader/fastest" tone.
11. How mature is MWS Object Storage? Young — standard class launched spring 2025; warm class is an early add-on. Low maturity.
12. Is dual-DC replication strong durability? It is 2-datacenter, weaker than Yandex's stated 3-replica-across-AZs. Adequate, not best-in-class.
13. Does "fastest for ML" hold without compute co-location? The release claims no GPU/compute co-location — the actual source of AWS's ML latency edge — so the ML-training benefit is asserted, not demonstrated. Open.
14. Any adoption/traction at launch? None cited — no customers, GMV, or benchmark. Capability announcement only.
15. Is there a 2026 IPO? Unverified — only a >200 bn ₽ end-2028 capitalization target is on record. Open.
16. Are the 63.8 bn ₽ revenue / +40% cloud figures audited? Company/press-stated, not independently audited. Treat as company figures.

**Importance: 2/5** — Real, dated product launch, but a standard NVMe "warm" storage class from a mid/low-tier RU provider, with the sole differentiator ("fastest on the market") being an unaudited self-claim from internal tests, no traction, and no compute-co-location proof that the ML benefit is real. Genuine but incremental import-substitution parity move, not a category or competitive shift.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-03]] (2026-07-03).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian public cloud services consumption reached RUB 392bn in 2024 and is projected to roughly double to ~RUB 801bn by 2029 (per Izvestia, via en.iz.ru, as of 2025-06-26); the narrower public-cloud-services segment was RUB 91bn (+20% YoY), of which ~99% domestic solutions (per TAdviser). IaaS is the fastest-growing layer — CAGR ~29% over 2022–2024 (per TAdviser/secondary citations). Structure is consolidating around national champions: in IaaS 2025 Cloud.ru led with 29.7% share, RTK-DPC 15.7%, Selectel 8.4% (per TAdviser, as of 2025); a handful of players (Cloud.ru/SberCloud, Yandex Cloud, VK Cloud, Rostelecom) reportedly control >85% of infrastructure. **Why now:** (1) data-localization mandate (Federal Law 242-FZ/152-FZ) forces workload repatriation to domestic providers — a regulatory tailwind, not a market-chosen migration; (2) AI/ML demand — Russian AI-GPU-accelerator market was RUB 62.7bn in 2025 (+~20%, per T1 study, via TAdviser), yet sanctions cut off NVIDIA supply (~10k AI cards in-country), so the scarce compute must be fed by fast local storage. Object storage sitting under starved GPUs is the second-order beneficiary of that bottleneck (analysis).

**Competitive landscape.** Sector KPIs: IaaS/storage runs on utilization/GPV-equivalent (consumption RUB), throughput (GiB/s) and TTFB latency (ms), and price-per-TB. Key players in S3-compatible object storage: Yandex Cloud (standard + cold, 100+ services), VK Cloud, Selectel (bare-metal/high-load heritage), Cloud.ru — basis of competition is price (VK Cloud reportedly undercuts rivals 15–20% on smaller workloads) and performance tiers. Protagonist position: MWS Cloud (МТС Web Services) is a **catching-up challenger**, not the volume leader (MTS is absent from the IaaS top-3 above). Its "warm" NVMe class — up to 1.8 GiB/s on 64 MB objects, ~20 ms TTFB, dual-DC replication, AWS S3 API, pay-as-you-go — is a product-differentiation bid on the AI/analytics/Lakehouse niche. The "fastest S3 on the market" claim rests solely on **MTS's own internal testing** — no independent benchmark, and the methodology page is the vendor's; treat as marketing, not verified (de-PR). Moat is thin: NVMe tiers and S3-API compatibility are commoditizing across peers; any edge is scale/data-center capex, not switching costs (analysis).

**Comps & multiples.** Parent MTS is IR-covered (`mts`, telecom, Russia; 33 filings). MWS (the digital/cloud unit) revenue RUB 63.8bn in 2025, +40% YoY, external revenue +53%, cloud-product sales +40%, OIBDA >2x (per Telecompaper/AKM). MWS Cloud is allocating ~RUB 6.5bn to data-center build-out (Avantage, GreenBushDC + a new Moscow-region DC, ~1,200 racks) — capex-heavy scaling (per AKM). No public valuation/round for the MWS unit → EV/Revenue, EV/EBITDA **not computed** — no data (unit not separately listed; parent MTS trades on MOEX but a clean segment multiple is `[UNSOURCED]`). Peer object-storage pricing/latency for a like-for-like multiple → no independent data. Internal comps from the base are only tangential (foreign cloud+banking partnerships, not Russian object-storage deals): [[Rakuten Cloud enters Brazilian market for financial sector]], [[SAP unveils sovereign cloud infrastructure in India]], [[AWS in talks to sell Trainium AI chip racks to outside companies]]. Distribution not computed; qualitative comparison only.

**Risk flags.**
1. **Unverified "fastest" claim / execution risk.** The market-leadership headline is 100% self-tested by MTS with no third-party benchmark — if a peer (Yandex/Selectel) publishes contradicting numbers, the sole marketing differentiator evaporates and the launch reverts to table-stakes parity.
2. **Regulatory-dependent demand.** Much of the domestic-cloud tailwind is manufactured by 242-FZ localization, not organic competitiveness — a policy-driven moat that shields margins from foreign rivals but leaves the whole sector exposed to a single regulatory regime and to being out-scaled by the >85%-share incumbents (Cloud.ru/Yandex/VK).
3. **GPU-supply / import-substitution bottleneck.** The AI-storage thesis presumes GPUs to feed; sanctions cap NVIDIA access (~10k cards nationally). Fast storage is worth less if compute stays scarce — MWS's warm tier is a complement to a supply-constrained input, so TAM is gated by someone else's hardware access.

**What this changes (idea-lens).** For the sector this is a niche performance-tier land-grab in a consolidating, regulation-fenced IaaS market, not a re-rating — MWS is buying differentiation on latency while the volume leaders (Cloud.ru 29.7%, Selectel) hold share on price/scale (analysis). Falsifiable thesis: if MWS Cloud's cloud-product growth stays ~40%+ AND it wins named AI/ML anchor customers off this tier, it credibly moves up the IaaS ranking; trigger to watch — an *independent* throughput/TTFB benchmark vs Yandex/Selectel, or MTS disclosing MWS Cloud object-storage volume. What breaks it: peers matching 1.8 GiB/s NVMe tiers at 15–20% lower price, collapsing the edge to a pricing war (analysis).

Sources: https://en.iz.ru/en/1910988/2025-06-26/volume-russian-public-cloud-services-market-will-double-2029 · https://tadviser.com/index.php/Article:Cloud_services_(Russian_market) · https://www.telecompaper.com/news/mws-revenues-up-40-in-2025--1564570 · https://www.akm.ru/eng/news/mws-cloud-will-allocate-6-5-billion-rubles-to-data-center-development/ · https://tadviser.com/index.php/Article:Video_cards_(Russian_market) · https://www.cloud4y.ru/en/blog/top-iaas-provider-2026/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
