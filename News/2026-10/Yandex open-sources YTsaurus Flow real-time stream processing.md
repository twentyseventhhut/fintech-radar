---
title: "Yandex open-sources YTsaurus Flow real-time stream processing"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/yandex
  - industry/infrastructure
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-10-06_yandeks_podelilsya_tehnologiej
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sab912eb8
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Yandex open-sources YTsaurus Flow real-time stream processing

> [!info] 2026-10-12 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Открыл исходный код YTsaurus Flow — технологии обработки потоков данных в реальном времени для рекомендательных и рекламных систем

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-10-06_yandeks_podelilsya_tehnologiej>
*433 слов · direct*

Эльяс Касми

 «Яндекс» поделился технологией непрерывной обработки данных: она помогает быстрее учитывать смену интересов пользователей
 
 
«Яндекс» выложил в опенсорс YTsaurus Flow — технологию для непрерывной обработки больших потоков данных. Она обрабатывает клики, лайки и другие события в интернете сразу же — по мере их появления. Благодаря этому алгоритмы быстрее замечают, как изменились интересы пользователей и что происходит в сети. Это позволяет мгновенно распознавать действия мошенников , точнее рекомендовать товары, книги, фильмы и так далее и подбирать рекламу, которая действительно полезна. Об этом CNews сообщили представители «Яндекса».
Интересы и потребности пользователей все время меняются. Человек может искать билет на самолет, а потом переключиться на новый фильм или товары для дома . Чтобы алгоритмы уловили эту смену интересов, им нужны свежие данные о действиях пользователя — что он покупал, какую музыку слушал, о чем спрашивал. Однако эти данные обычно обрабатывают не сразу, а сначала накапливают — примерно как посылки для отправки поездом. Из-за этого информация поступает в систему с задержкой, которая может составлять часы. YTsaurus Flow сводит эту задержку практически к нулю, поскольку обрабатывает данные в реальном времени — по мере поступления.
Технология будет полезна в самых разных проектах, где важна свежесть информации, — не только в рекламных и рекомендательных сервисах. Например, с ее помощью можно готовить данные для обучения ML-моделей , обновлять информацию для сайтов и приложений, считать просмотры, клики и заказы. Технология рассчитана на высокую нагрузку и обрабатывает каждое событие ровно один раз, не теряя и не дублируя данные. Она продолжает работать даже в случае сбоев, перераспределяя нагрузку между доступными серверами .
YTsaurus Flow уже применяется во многих сервисах « Яндекса ». Например, «Маркету» она помогает быстрее собирать статистику, чтобы продавцы могли оперативно реагировать на изменение спроса, антифрод -системам — обнаруживать действия злоумышленников , а «Рекламе» — подбирать интересные людям предложения. Например, раньше на подготовку данных для дообучения некоторых моделей, отвечающих за подбор рекламы, уходило больше 10 часов. С помощью YTsaurus Flow эту задержку удалось почти полностью устранить. Каждую секунду YTsaurus Flow обрабатывает в «Яндекс Рекламе» более 100 ГБ данных и миллионы событий в интернете: кликов, показов, лайков, заказов и так далее. 
Технология работает в рамках YTsaurus — это открытая платформа «Яндекса» для хранения и обработки больших объемов данных , предназначенная для крупного бизнеса. Благодаря YTsaurus Flow компании смогут обрабатывать данные не только партиями, но и по мере поступления. Кроме того, у них будет возможность учитывать накопленную и свежую информацию в одной системе. 
YTsaurus Flow — это совместная разработка команд Yandex Infrastructure и « Яндекс Рекламы ». Технология доступна под лицензией Apache 2.0, что позволяет использовать ее в том числе в коммерческих проектах. 
 Что лучше — ГЛОНАСС или GPS: главные различия систем навигации

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 2/5 — a genuine, Apache-2.0 open-source release of a real production component (100+ GB/s in Yandex Ads), but low fintech relevance, niche audience, and an incremental add-on to the already-open YTsaurus platform (2023)._

## [0] What exactly happened (de-PR'd)
On 2026-10-06 Yandex released the source code of **YTsaurus Flow** — a stateful stream-processing framework with **exactly-once** guarantees by default — under **Apache 2.0** (commercial use permitted). It is NOT a new standalone product: it is a streaming layer **inside YTsaurus**, Yandex's big-data storage/compute platform that was itself open-sourced on **2023-03-20** (also Apache 2.0). So this is the "real-time" tier bolted onto a 2.5-year-old open platform, co-built by the Yandex Infrastructure and Yandex Ads teams.
- **Live, not vaporware.** Already in production: Yandex Ads processes **>100 GB/s and millions of events/sec** (clicks, impressions, likes, orders) through it; Market uses it for seller demand stats; antifraud for malicious-activity detection. Concrete latency win cited: ad-model retraining data prep dropped from **>10 hours** to near-zero (external sources say ~2h). These are vendor-supplied numbers, unaudited, but specific and plausible.
- **Mechanism delta:** instead of a self-contained engine, Flow **reuses the YTsaurus storage layer, queues and transactions** for state and failure recovery — unifying batch + streaming ("lambda-free") in one system. **→ Why structured this way:** this is the actual pitch — not "another Flink", but "streaming that shares state/transactions with your existing YTsaurus lake", so you don't run a separate state backend (RocksDB/checkpoints as in Flink). **→ Why it matters:** the moat and the lock-in are the same thing — Flow is only compelling if you already run YTsaurus.
- **PR vagueness flags:** the CNews framing ("spots fraudsters instantly", "recommends better") is recommendation/ad-tech marketing; the only de-PR'd substance is: Apache-2.0 release + exactly-once + the 100 GB/s / 10h→~0 internal figures. No external adoption, no contributor/community numbers, no roadmap.

## [1] Competitors / peers
Direct prior art in open-source streaming (all battle-tested, large communities): **Apache Flink** (stateful, exactly-once, RocksDB state backend — the closest analog), **Kafka Streams** (library model), **Apache Spark Structured Streaming** (micro-batch), **Apache Storm/Samza** (older). Flink already offers exactly-once across many sources/sinks, so Flow's headline feature is **parity, not novelty**. **+ Why the lay of the land:** Flow's only differentiation is tight coupling to YTsaurus (shared transactions/queues, batch+stream in one store) — attractive *only* to existing YTsaurus users, a tiny set outside Yandex. Against Flink's ecosystem (connectors, SQL, PyFlink, managed offerings on every cloud), a fresh open-source engine with ~zero external community starts far behind. On the storage-platform axis YTsaurus competes with ClickHouse, YDB, Spark/Hadoop stacks.

## [2] Company history / fit
Yandex has run its own big-data stack since **2010**; open-sourced the core **YTsaurus** in 2023 and has published periodic "two years on" progress posts. Flow is the logical next unbundling step — ship the real-time piece now that the platform base is public. It fits the broader 2026 Yandex-infrastructure posture visible in the corpus: [[Yandex Cloud helps clients migrate to rival providers after outages]] (data-center incidents, importance 4) and [[Yandex builds precise geopositioning network for autonomous transport]] — Yandex positioning its infra as credible/open amid reliability questions. **+ Why the company acts this way:** post-2022 isolation, open-sourcing under Apache 2.0 is both a talent/credibility play and a hedge — a permissive license lets Russian enterprises adopt without vendor/sanctions dependence, and lets Yandex claim a standards-setter role domestically.

## [3] Novelty / value-add / traction
**Not new as a capability** (exactly-once streaming exists in Flink since years). The real, confirmable value-add is narrow: (a) a **production-proven** engine at genuinely high throughput (100+ GB/s) is now public, and (b) **batch+stream unification on shared YTsaurus transactions** removes a class of plumbing *for YTsaurus users*. Traction *inside Yandex* is strong and quantified; **external traction is zero/unknown** — no third-party users, no community metrics. **+ Who captures the value:** the beneficiary is Yandex itself (ecosystem gravity around YTsaurus, hiring, domestic-platform narrative), not downstream adopters unless they already committed to YTsaurus. Value breaks the moment a prospective user asks "why not just run Flink with its huge connector/SQL ecosystem?".

## [4] What's next / market sentiment
Expect the usual OSS-release trajectory: docs, SDKs, a managed Yandex Cloud offering, gradual external pilots — mostly **Russian/CIS enterprises** seeking sanctions-resilient, self-hostable infra. Sentiment: neutral-positive engineering interest, but **adoption outside the YTsaurus base is the open question** and likely slow. Risk: a single-vendor OSS project with a tiny external community can stagnate; coupling to YTsaurus caps the addressable audience. **+ Second-order:** the release is more a *credibility/geopolitical* signal (Russia can ship world-class data infra; permissive licensing for domestic substitution) than a shift in the global streaming market, where Flink/Kafka dominance is unthreatened.

## Top challenge/extra questions
1. New capability or Flink parity? → **Parity** on exactly-once; the only delta is YTsaurus coupling. (answered)
2. First release of this, or re-run? → **Fresh**: YTsaurus core was 2023; *Flow* is a new 2026-10-06 release. No prior corpus note. (answered)
3. Live or announced? → **Live** in Yandex Ads/Market/antifraud at 100+ GB/s. (answered)
4. Are the 100 GB/s and 10h→~0 figures independently verified? → **No**, vendor-supplied. (open)
5. Any external adopters or community/contributor counts? → **None disclosed**. (open)
6. Does Flow work without the full YTsaurus platform, or is it hard-coupled? → Appears hard-coupled (uses YTsaurus storage/queues/transactions). (analysis)
7. Why Apache 2.0 vs a restrictive license? → Maximize domestic/commercial adoption + credibility; sanctions-resilient substitution play. (analysis)
8. Does this change the global streaming market? → No; Flink/Kafka ecosystems far ahead. (analysis)
9. Fintech relevance? → Indirect only (antifraud/real-time risk could use it); no fintech adopter named. (open)
10. Why now, 2.5 years after YTsaurus core? → Base platform matured; unbundle the real-time tier; reinforce open-infra narrative amid 2026 reliability incidents. (analysis)

## Sources
- cnews.ru (primary, in note): https://www.cnews.ru/news/line/2026-10-06_yandeks_podelilsya_tehnologiej
- Yandex IR press release 2026-10-06: https://ir.yandex/press-releases?year=2026&id=2026-10-06
- Medium (Yandex): "Open-Sourcing YTsaurus Flow: Real-Time Data Stream Processing at 100+ GB/s": https://medium.com/yandex/open-sourcing-ytsaurus-flow-real-time-data-stream-processing-at-100-gb-s-d90957e5cfb2
- YTsaurus core open-sourced 2023-03-20: https://yandex.com/company/press_center/press_releases/2023/20-03-2023
- GitHub ytsaurus/ytsaurus: https://github.com/ytsaurus/ytsaurus
- Flink/Kafka/Spark streaming comparison: https://www.onehouse.ai/blog/apache-spark-structured-streaming-vs-apache-flink-vs-apache-kafka-streams-comparing-stream-processing-engines
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 2/5 — rationale.** A real, Apache-2.0 open-source release of a production-grade component (exactly-once streaming at 100+ GB/s inside Yandex Ads) — so it is not vaporware. But it scores low because: (a) **capability novelty is ~nil** vs Apache Flink/Kafka Streams/Spark, which already provide exactly-once streaming with vastly larger ecosystems; (b) it is an **incremental add-on** to YTsaurus, already open-sourced in 2023, not a new platform; (c) **external traction is zero/undisclosed** — all cited adoption is internal to Yandex; (d) **fintech relevance is indirect** (antifraud/real-time risk at best), with no fintech adopter named. It matters mainly as a Russia-infra credibility / domestic-substitution signal, not a market mover.

**Red-team flags:**
- **Parity dressed as breakthrough.** The PR headline ("real-time processing", "exactly-once") is standard in Flink since years. The only genuine delta is coupling to YTsaurus (shared transactions/queues → batch+stream in one store) — which is also the lock-in. Treat "revolutionary" framing skeptically.
- **Vendor numbers unaudited.** 100+ GB/s, millions of events/sec, "10h → near-zero" retraining latency are Yandex-supplied and plausible but unverified.
- **Moat = lock-in.** Value materializes only for existing YTsaurus users; everyone else rationally compares to Flink's connector/SQL/managed ecosystem and the new engine's near-empty external community.
- **No external adoption or contributor metrics** disclosed — classic single-vendor OSS risk (stagnation).
- **Marketing creep** in the source ("instantly spot fraudsters", "recommend better") is ad/rec-tech framing, not de-PR'd substance.

**FRESHNESS / DUPLICATE VERDICT: FRESH.** Internal grep over `company/yandex` and over `open-source|ytsaurus|stream processing|flink|kafka` in News/2026-* found **no prior note covering YTsaurus, YTsaurus Flow, or this open-source release**. The nearest company notes ([[Yandex Cloud helps clients migrate to rival providers after outages]], [[Yandex builds precise geopositioning network for autonomous transport]]) are unrelated events. The 2023 YTsaurus-core open-sourcing is a *different, earlier* release, not this one. Not a reprint/re-framing → **fresh**, no `duplicate_of`.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: real-time stream-processing / data infrastructure (open-source engines underneath ads, recommendations, antifraud, ML-feature pipelines). Market size: the event-stream-processing market was ~$1.78bn in 2026, growing at ~10.6% CAGR to ~$2.96bn by 2031 (per Mordor Intelligence, via mordorintelligence.com, as of 2026) — one secondary source; a second cites a ~10.5% CAGR to a larger 2031 figure, so treat the absolute TAM as indicative, not precise. Structure: consolidating around the Kafka/Flink stack — Apache Kafka is the de-facto log standard (>150k orgs) and Flink the emerging stateful-compute standard; IBM closed its ~$11bn acquisition of Confluent in March 2026 and retired its own Kafka products, while Databricks' "Real-Time Mode" reached GA in 2026 (per kai-waehner.de, as of 2026-09). Entry barriers are high: exactly-once semantics at 100+ GB/s, fault-tolerance and operational maturity are hard to build. "Why now": (1) the AI/ML cycle makes data *freshness* a first-order input — Yandex cites cutting ad-model feature-prep latency from >10h to ~zero; (2) the open-core playbook (release the engine, monetize managed/cloud) is now the dominant go-to-market for data infra, and in RU specifically, import-substitution raises the value of a domestic, Apache-2.0-licensed platform.

**Competitive landscape.** Sector KPIs: throughput (GB/s, events/s), latency (end-to-end), processing guarantee (at-least-once vs exactly-once), fault-tolerance/recovery. Key players and basis of competition: Confluent/IBM (Kafka+Flink, managed cloud), Databricks (Spark Structured Streaming + Real-Time Mode, bundled with lakehouse+AI), plus the Apache Flink/Kafka OSS projects and hyperscaler services (AWS, Azure, GCP). Competition is on throughput/latency-at-scale, exactly-once correctness, and ecosystem/bundling — not price. Recent moves: IBM–Confluent close (2026-03); Databricks Real-Time Mode GA (2026); Yandex open-sourced the base YTsaurus platform back in 2023-03-20 and now extends it with Flow (2026-10-06). Protagonist position: niche globally, but credible — YTsaurus Flow is battle-tested internally (>100 GB/s, millions of events/s in Yandex Ads; used in Market, antifraud, Ads) and Apache-2.0, so commercially reusable. Moat is intangibles + switching costs *within* the YTsaurus ecosystem (unified batch+streaming on one storage platform), not a standalone network effect `(analysis)`.

**Comps & multiples.** No deal/round/valuation attaches to *this* event — it is a code release, not a financing — so there is no YTsaurus Flow multiple to compute ("no data" by design). Sector reference multiples for the engine layer: Confluent — IBM paid ~$11bn EV on ~$1.1bn revenue → EV/Revenue = $11bn / $1.1bn ≈ 10.0x (per gfmag.com / multiples.vc, as of 2026-03; mature ~growth name). Databricks — ~$190bn implied valuation on ~$7bn revenue run-rate → ~$190bn / $7bn ≈ 27.1x (per Yahoo Finance/multiples.vc, round valuation, not market cap, as of 2026-08; richer, justified by >80% YoY growth — the growth-multiple spread between the two is the signal, not an over-valuation flag). Internal comp: [[Addepar launches ADX data exchange built on Databricks]] — an adjacent "re-architect data infra, then expose it as a product" move (built on Databricks), the closest base precedent. Distribution not computed (only 2 external multiples, different model/stage) — qualitative comparison only. Yandex group financials sit in IR (latest filed result Q1 2026 press release, 2026-04-28, https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf), but YTsaurus Flow is an internal cost/infra and ecosystem play — it does not map to a disclosed revenue line, so no top-down revenue attribution `[UNSOURCED]`.

**Risk flags.** (1) *Monetization gap / open-core risk* — releasing under Apache 2.0 gives away the engine with no disclosed managed-cloud SKU or pricing; value accrues only if Yandex Cloud converts adoption into paid services, otherwise this is pure developer-relations spend, not a revenue line. (2) *Geopolitical/ecosystem isolation* — a RU-origin, sanctions-exposed project will struggle for Western enterprise and cloud-marketplace adoption, capping the addressable developer/customer base versus Confluent/Databricks; adoption may be largely RU/CIS. (3) *Disintermediation by the standard stack* — Kafka+Flink is the consolidating de-facto standard (IBM/Confluent, hyperscalers); a parallel engine risks staying niche unless it offers clear, sustained throughput/latency advantages and real community traction (stars, external committers, production users outside Yandex are all undisclosed → `[UNSOURCED]`).

**What this changes (idea-lens).** `(analysis)` This is an ecosystem/talent-and-lock-in play, not a re-rating event: open-sourcing Flow deepens the YTsaurus moat and is a feeder for Yandex Cloud's managed-data business and for RU import-substitution, rather than a direct financial catalyst. Falsifiable thesis: if within ~12 months there is a priced Yandex Cloud managed-Flow offering and documented external production adopters, the open-core-to-cloud flywheel is working; if adoption stays Yandex-internal with no external committers/customers, it remains cost/PR with no P&L impact — that absence would break the thesis.

Sources: https://ir.yandex/press-releases?year=2026&id=2026-10-06 · https://www.mordorintelligence.com/industry-reports/event-stream-processing-market · https://www.kai-waehner.de/blog/2026/09/07/data-streaming-landscape-q3-2026-who-controls-your-streams/ · https://gfmag.com/capital-raising-corporate-finance/ibm-targets-confluent-with-11-billion-buyout/ · https://multiples.vc/private-comps/databricks · https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news.** This is a product/open-source release — Yandex open-sourced YTsaurus Flow (real-time stream processing, part of the YTsaurus data platform) under Apache 2.0; no financials are reported in the item. Brief grounding of the latest reported results follows, framed to the relevant B2B-infra segment.

**Latest reported results (ground — not from this news).** Yandex Q1 2026 (reported 2026-04-28, latest IR filing): revenue RUB 372.7bn (+22% YoY), adjusted EBITDA RUB 73.3bn (+50% YoY). FY2026 guidance: revenue growth ~20%, adj. EBITDA ~RUB 350bn. Primary source: Yandex Q1 2026 Press Release (RUS) — https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf (IR). Figures corroborated by public press (rb.ru, Reuters via TradingView).

**B2B-infra flag (relevant to this story).** YTsaurus / YTsaurus Flow sits in the B2B Tech segment (Yandex Cloud). Q1 2026 B2B Tech revenue RUB 13.6bn (+36% YoY), EBITDA +49% YoY; Yandex Cloud clients ~60k. H1 2026 (reported 2026-08-12, post-dates latest ir_latest entry): B2B Tech revenue RUB 28.9bn (+32% YoY), adj. EBITDA RUB 6.4bn (+45% YoY), cloud-services revenue RUB 16.7bn (+30% YoY), ~64k clients (+36% YoY). So the segment this open-source tech serves is Yandex's fastest-growing infra line, though still small (~4% of group revenue). Open-sourcing core infra (Apache 2.0) is an ecosystem/adoption play, not a near-term monetization lever — no revenue is attached to the release itself; impact on the above figures is nil.

Sources: Yandex Q1 2026 Press Release (RUS, IR primary) — https://yastatic.net/s3/ir-docs/docs/2026/847f189a3b090d07d2c9125d942f2de2/1Q26_Press%20Release_RUS_189a.pdf · Q1 figures corroboration — https://rb.ru/news/yandeks-opublikoval-finansovye-itogi-za-i-kvartal-2026-goda-vyruchka-vyrosla-na-22-do-3727-mlrd/ · H1 2026 B2B Tech — https://www.comnews.ru/content/246852/2026-08-12/2026-w33/1010/yandex-b2b-tech-obyavil-finansovye-rezultaty-za-pervoe-polugodie-2026-g · Reuters (Q1 buyback/+22%) — https://www.tradingview.com/news/reuters.com,2026:newsml_S8N40B0AJ:0-yandex-reports-22-rise-in-q1-revenue-says-board-to-consider-share-buyback/ · news item (product) — https://www.cnews.ru/news/line/2026-10-06_yandeks_podelilsya_tehnologiej
<!-- /enrichment:earnings_review -->
