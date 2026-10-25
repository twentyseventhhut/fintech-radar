---
title: "How Monzo uses multi-cloud infrastructure to improve resilience"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - company/monzo
  - industry/neobank
  - industry/infrastructure
  - region/uk
  - type/commentary
sources:
  - https://cloud.google.com/customers/monzo-bank
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s7d37bd15
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# How Monzo uses multi-cloud infrastructure to improve resilience

> [!info] 2026-10-22 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] How Monzo uses multi-cloud infrastructure to improve resilience.

## Первоисточники

### cloud.google.com
<https://cloud.google.com/customers/monzo-bank>
*1099 слов · direct*

Monzo: Rethinking banking using data-driven insights
 Looker helps Monzo access, analyze, and act on the most up-to-date multiple terabyte data sets in minutes 
 Uses BigQuery and VertexAI to train ML models to help protect customer payments from fraudsters 
 Has created an online 24/7 disaster recovery capability that is continuously running using Google Cloud 
As Monzo continues its rapid growth, it leverages data insights to build a customer centric product and provide a financial control center. Using BigQuery and Looker, Monzo can access valuable insights around business performance and customer behavior to empower Monzo on its mission to make money work for everyone.
Digital banks, or challenger banks, are becoming an ever more prominent feature of the financial landscape, particularly in the UK. Strictly digital, they use apps and online platforms to support their customers. Digital banks have an advantage in that they don’t rely on legacy systems. This allows them to be nimble, innovate at speed, and more proactive than many traditional banks. Monzo is now one of the most popular digital banks in the UK, with over 9 million customers, making it the seventh largest bank in the UK by customer numbers. The bank has been working with Google Cloud to create and shape a data analytics hub that can help it grow with its customers and create better customer experiences.
“We generate a lot of data on our backend and also on our frontend, from our systems, services, and our customers using the app,” says Suhail Patel, Senior Staff Engineer at Monzo. “We use that in a multitude of ways, for example, to provide better customer support by sharing insights with customers about how they're spending their money.”
Building a high-performance data analysis hub
Monzo has been working with Google Cloud since the bank was founded in 2015, and was one of the first banks in the UK to be 100% cloud-based. The bank is multi-cloud, and Google Cloud has been integral in building its data analysis hub, helping to provide the bank with data that can empower all of its teams to get the insights that can drive better business decisions. BigQuery , for example, is a serverless and cost-effective enterprise data warehouse that is helping Monzo store, access, and utilize data.
“We empower all of our engineers and all of our technical staff with BigQuery data across the organization,” says Patel. “We leverage BigQuery’s scale and capabilities to run complex pipelines and data modeling to surface detailed customer and business insights.”
The company also uses Looker on top of BigQuery to access, analyze, and act on the most up-to-date multiple terabyte data sets in minutes, and it’s helping the bank get access to a wide range of business insights. Whether it’s helping track key goals for the bank’s diversity and inclusion program or tracking profitability, all of this data is being served on top of BigQuery. This aggregated data is then made accessible across the bank. 
The bank has nearly 19 petabytes of data in BigQuery and more than 2,000 data models across its BigQuery estate. The internal and external insights Monzo gets from BigQuery also allow the bank to develop its customer-facing features, such as how it provides lending facilities to customers.
“With BigQuery we can have all the data we need to effectively make business-critical decisions, and analyze the impact of complex incidents when something goes wrong. For us, this is like having a superpower,” says Patel.
Utilizing the power of AI to create better customer experiences
With all this data, Monzo is able to build powerful machine learning (ML) models to improve its services in a variety of ways, such as helping to protect customers from fraudsters. Monzo also uses ML models across different borrowing products and contexts, which are the key drivers of their lending decisions, from accepting credit applications to setting credit limits and interest rates. 
As Monzo continues to grow, the bank is using ML to develop its new experimental customer demand forecasting system. Monzo has already completed early experiments for predicting outcomes related to customer experience and auto-complete search queries.
To train its ML models, the bank analyzes data sets like its support help articles on BigQuery using Vertex AI . This way, Monzo can test, build, and monitor ML models as it continues to refine and iterate on them. 
Supporting the safeguarding of customer data
Monzo worked very closely with Google Cloud and the banking regulators to effectively build a disaster recovery program where its data is being continuously synced between another cloud platform and Google Cloud. This allows Monzo to flip a switch and provide all of its important business services within a matter of seconds.
This backup platform, run on Google Cloud, means that customers can continue using all the important business services within Monzo if its primary platform were ever to go down. This is an online 24/7 disaster recovery capability that is continuously running, ready to take over in the event of failure of its other cloud provider. The bank also uses the disaster recovery program as a testbed for Google Kubernetes Engine , exploring what new features and capabilities it can build. 
The work with Google Cloud team also supports Monzo’s ongoing efforts when it comes to navigating the complicated and ever-changing world of banking regulations, both in the UK and abroad. This expertise helps Monzo build customer confidence. “As Google Cloud team operates both within the UK and across other markets, their geographical reach is a key strategic advantage, which aligns with our global ambition,” says Patel. 
Redefining banking for the 21st century
Monzo continues its impressive growth and should secure another £500 million in funding from investors, which could push its valuation to £4.1 billion. And it will continue to work with Google Cloud as it cements its place in the global banking landscape. “We have grown with Google Cloud and we can integrate our data with its other solutions,” says Patel. “By being on top of Google Cloud, we’re prepared to bring more products and continue growing in the UK and beyond.”
 Monzo was founded in 2015 and now serves more than 9 million customers, making it the largest digital bank in the UK. With a mission to make money work for everyone, Monzo is known for pioneering industry-first features like the Gambling Block and Call Status and co-creating with its customers to deliver data driven products powered by BigQuery and tools that put them in control of their finances.
 Industries: Financial Services
 Location: UK
 Products: Google Cloud , BigQuery , Google Kubernetes Engine , Looker , Vertex AI

## Контекст

<!-- enrichment:context -->
**What this is.** A Google Cloud customer-story / vendor commentary ("How Monzo uses multi-cloud infrastructure to improve resilience") re-surfaced via *This Week in Fintech* on 2026-10-22. It is evergreen marketing-adjacent material, not a fresh news event — but it lands squarely in the middle of a live UK cloud-resilience news cycle (see cluster below).

**The actual architecture (web-verified, and it inverts the vendor framing).** Monzo's *primary* core-banking platform runs on **AWS** — ~400+ Go microservices on EC2/EKS/S3/Keyspaces, orchestrated with Kubernetes and Cassandra, wired via Kafka. Its disaster-recovery system, **"Monzo Stand-in,"** runs independently on **Google Cloud (GCP)** with deliberately different software/data so no single code or infra fault can take out both. The GCP case study (the cited source, cloud.google.com/customers/monzo-bank) soft-pedals this by calling GCP the platform "continuously synced" and ready to "take over in the event of failure of its other cloud provider" — i.e. GCP is the *backup*, AWS is the *primary*. Stand-in covers only essential functions: card payments, ATM withdrawals, freeze/unfreeze cards, transfers, balance/transaction checks — not the full feature set.

**Stand-in has been battle-tested, repeatedly, in 2026.** It was activated during a multi-hour outage in **Jan 2026** ([[Monzo hit by major outage disrupting payments]]) and again publicly on **19 Aug 2026**, when Stand-in rolled out to customers during an app/payments incident (3,000+ DownDetector reports). Independent monitors noted Stand-in largely held but some customers still had a degraded experience. So the "flip a switch in seconds, 24/7 DR" claim is real but not frictionless.

**Scale / standing.** Monzo founded 2015; one of the first 100%-cloud UK banks. The cited (older) case study says "9 million customers / 7th largest"; newer data (FY to Mar 2026) has it past **15 million customers**, deposits up 55% to ~£25.7bn, and eyeing a potential IPO at a reported £6–7bn ($8–9bn) valuation. The "£500m raise / £4.1bn valuation" line in the source is stale vendor copy.

**Why it's timely — the live cloud-resilience cluster.** The story surfaces days after the **20 Oct 2026 Google Cloud London outage** (power event in europe-west2-b, ~06:08 UTC) that locked customers of Lloyds, Halifax, HSBC and Revolut out of banking apps, cards and transfers. That triggered regulatory heat now dominating the same digest: [[EU regulators question Google over London cloud outage]], [[Treasury Committee questions regulators over cloud outage oversight]], and the UK's new **Critical Third Parties** regime — [[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]] — the first real-world test of hyperscaler oversight brought in ~3 months earlier (FCA engaging Google and affected firms). Monzo's multi-cloud DR is implicitly the "do it right" counter-example to the single-cloud banks that went dark.

**Reading.** This is a vendor case study doing double duty as a resilience talking point at exactly the moment UK regulators and the press are asking why so many banks sit on one hyperscaler. The genuinely interesting fact is the cross-cloud primary/backup split (AWS primary, GCP standby) and that it has fired in production in 2026 — not the BigQuery/Looker/Vertex AI data-hub marketing that fills most of the source text.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. The cited source (Google Cloud case study) frames GCP as the platform Monzo relies on — but the real architecture is AWS *primary*, GCP *Stand-in backup*. Does the headline/aggregated text mislead readers into thinking GCP is the resilience engine?
2. "Multi-cloud" here is not active-active across two clouds — it's a primary + a deliberately-different standby for essential functions only. Is calling it "multi-cloud" overselling what is really cross-cloud disaster recovery?
3. Stand-in covers only a reduced function set (payments, ATM, transfers, balances). What breaks for customers when it's active — lending, in-app features, support flows? Is "all important business services" accurate?
4. Stand-in was invoked in Jan 2026 AND Aug 2026. Doesn't the frequency of invocation undercut the "resilience" story — i.e. the primary keeps failing enough to need it?
5. Monitors reported some customers still had a bad day during the Aug 2026 Stand-in activation. How close is the "flip a switch, seconds, seamless" claim to reality?
6. The source is a vendor marketing asset. How much is independently verified vs. Monzo/Google PR? Which specific claims (19 PB in BigQuery, "seconds" failover) are unaudited?
7. Data-sync between AWS and GCP has a cost and a consistency/lag problem. What's the RPO/RTO actually? Could customers lose recent transactions on failover?
8. Timing: this story rode the 20 Oct 2026 Google Cloud London outage. Is This Week in Fintech using an old case study opportunistically, risking a "Monzo-is-immune" impression that the outages don't actually support?
9. Ironic exposure: Monzo's *backup* is GCP, which is exactly the cloud that just failed on 20 Oct. If an incident coincided with a GCP-region fault, would Stand-in be available?
10. The stale figures (9M customers, £4.1bn valuation, £500m raise) are long superseded (15M+, IPO talk at £6–7bn). Does keeping the dated vendor copy damage credibility?
11. Under the new UK Critical Third Parties regime, does running both primary and backup on two designated CTPs (AWS + Google) actually reduce concentration risk, or just spread it across two single points the regulator now watches?
12. Cross-cloud DR is capital- and engineering-intensive (duplicate Kubernetes estate, separate services). Is this replicable by smaller challengers, or a moat only a 15M-customer bank can afford — and is that framed honestly?
13. Is there any independent regulator confirmation (PRA/FCA/BoE cloud drill) that Monzo's DR meets operational-resilience impact-tolerance rules, or only Monzo's own testing?

**Importance: 4/5** — As a standalone vendor case study it would be a 2–3 (evergreen, marketing-heavy, stale figures). But it lands in the single most important UK fintech-infrastructure story of the moment: the 20 Oct 2026 Google Cloud London outage, the new Critical Third Parties regime, and Treasury/EU scrutiny of cloud concentration. Monzo's cross-cloud primary/backup split — demonstrably exercised in production twice in 2026 — is the concrete "good-practice" reference point the whole regulatory debate is circling, which makes it a 4 in context.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-25]] (2026-10-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a UK neobank *resilience-engineering* story landing in the middle of a live regulatory inflection. Monzo runs 100% cloud (on Google Cloud since 2015) with a continuously-synced, online 24/7 disaster-recovery replica on a second cloud — true multi-cloud active/standby rather than a cold backup (per source, cloud.google.com/customers/monzo-bank). The "why now" is acute: on 20 Oct 2026 a power event at a Google europe-west2 facility took out services at Lloyds, HSBC and Revolut, making cloud *concentration risk* the UK's clearest recent case study (per Reuters/Techerati, via web, 21 Oct 2026). Backdrop: from 13 Jul 2026 HM Treasury designated Google Cloud, AWS, Microsoft and Oracle as the first Critical Third Parties (CTPs) to the UK financial system, under joint BoE/PRA/FCA oversight; DORA (EU) keeps resilience accountability *inside* the regulated firm even when infrastructure is outsourced (per Gresham/Copla, via web, 2026). So Monzo's "flip-a-switch" cross-cloud failover is exactly the capability regulators are now pressing the sector to prove — this reads as a de-PR'd vendor case study timed to a resilience news cycle, not new financials.

**Competitive landscape.** Sector KPIs for neobanks: customers/MAU, deposits, ARPU, pre-tax profit, and — newly salient — *operational resilience* (RTO/RPO, cloud diversification). Monzo cites scale metrics that are real: >15.2M customers and ~19 PB in BigQuery (FY2026 report / source). Positioning on the *resilience* axis: ahead of single-cloud peers. In-base evidence that the whole UK neobank set is racing on this same vector, Oct 2026: [[Revolut outage linked to Google Cloud infrastructure problems]] (the negative counter-example — single-region exposure), [[Starling Bank builds AI model on UK sovereign cloud]] and [[Starling Bank unveils AI agent for 17-second financial crime probes]] (Starling diversifying onto sovereign cloud), [[Bank of England runs sector-wide cloud outage drill with 38 firms]], [[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]], [[Treasury Committee questions regulators over cloud outage oversight]]. Moat (analysis): switching costs + a decade of multi-cloud DR muscle memory is a genuine operational intangible — but the "multi-cloud" claim is softer than it sounds (see risks).

**Comps & multiples.** No deal/valuation in this news item, so multiples are contextual, not transactional. Monzo last completed round ≈£4.5bn (TechFundingNews, via web); autumn 2026 talks with Nubank were reported up to ~£10bn before collapsing — see [[Monzo explores PE options after Nubank deal falls through]]. FY2026 hard figures (source: Monzo Annual Report FY2026, MBHG consolidated, 2026-05-19, per web/IR): revenue £1.7bn (+39% YoY), gross profit crossing £1.0bn, statutory pre-tax profit £87.3m (+~44%), deposits £25.7bn (+55%), ~15.2M customers. On a £10bn mooted valuation vs £87.3m statutory PTP that is ~115x pre-tax profit (`£10bn / £0.087bn = 115x`), i.e. a growth/scale multiple, not an earnings one (Forbes framing, via web) — rich, justified only by the +39% revenue growth and deposit momentum. Peer anchor: [[Revolut hits $121.2B valuation as IPO talk intensifies]] — a different scale class entirely; Starling's founder exited a residual stake at a ~£1.7bn mark ([[Starling founder Anne Boden sells remaining stake at 1.7bn valuation]]). EV/Revenue, EV/EBITDA for Monzo = no data (private, no public EV). Distribution not computed — qualitative comparison only.

**Risk flags.**
1. **"Multi-cloud" is really Google-primary + a DR replica, not load-balanced dual-active.** The source says a second cloud runs a *continuously-synced standby* ready to "take over in the event of failure of its *other* cloud provider." That is resilience against a single-provider outage, but the day-to-day control plane, data estate (19 PB BigQuery), ML (Vertex AI) and GKE all sit on Google — a deep Google-Cloud *dependency* that the CTP regime exists to police. Second-order: failover tooling that is itself exercised only on Google (the DR program doubles as a GKE testbed) couples test and prod to the same vendor.
2. **Concentration / CTP regulatory overhang.** With Google Cloud now a designated CTP, Monzo's architecture is under direct supervisory scrutiny; a mandated exit/stressing requirement or a repeat of the 20 Oct europe-west2 failure mode would hit Monzo's primary, not just the standby. Monzo has its own outage history ([[Monzo hit by major outage disrupting payments]], Jan 2026), so "flip a switch in seconds" is a claim regulators will want demonstrated, not asserted.
3. **De-PR gap: no stated RTO/RPO, no named second provider, no cost.** A vendor case study is silent on recovery-time objective, data-loss window, and what the standby cloud actually is — the economics and the hard resilience numbers are exactly what's omitted.

**What this changes (idea-lens).** (analysis) The Oct 2026 Google outage + CTP designation turn "which cloud are you on, and can you fail over?" from a back-office detail into a competitive and supervisory differentiator for UK neobanks — Monzo is pre-positioned, Revolut got caught single-region, Starling is hedging onto sovereign cloud. Falsifiable thesis: resilience architecture becomes a published, examinable metric (BoE's 38-firm drill is the leading indicator). Trigger to watch: a BoE/PRA resilience testing mandate for CTP users, or a *second* hyperscaler outage — either would force the sector to prove multi-cloud failover rather than narrate it, and would expose any neobank whose "multi-cloud" is really a dormant replica. What breaks the thesis: regulators settle for provider-level CTP oversight and don't push failover testing onto firms.

Sources: https://cloud.google.com/customers/monzo-bank · https://monzo.com/annual-report/2026/Monzo-Annual-Report-2026.pdf · https://www.reuters.com/business/finance/europes-financial-regulators-query-google-over-cloud-outage-that-hit-banks-2026-10-21 · https://www.techerati.com/news-hub/google-cloud-outage-exposes-shared-infrastructure-risks-for-uk-banks/ · https://www.greshamtech.com/blog/dora-in-2026-why-cloud-resilience-will-define-financial-services-compliance · https://techfundingnews.com/monzo-hits-record-high-4-5b-valuation-everything-you-need-to-know-the-3rd-most-valuable-neobank-in-europe/ · https://www.forbes.com/sites/zennonkapron/2026/09/27/nubank-wants-to-pay-up-to-10-billion-for-monzo-that-is-twice-monzos-last-valuation-and-115-times-its-pre-tax-profit/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news.** This is an infrastructure/engineering case study (Monzo's multi-cloud / Google Cloud disaster-recovery setup), not a results release — no fresh period figures in [0]. Below is Monzo's OWN latest reported scale/trajectory from the FY2026 Annual Report (year ended 31 March 2026, published 2026-05-19) as context; no new print to beat/miss against.

**Latest reported figures (FY2026, MBHG consolidated; vs FY2025).**
- Revenue £1.7bn, +39% YoY (FY2025 £1.2bn).
- Gross profit £1.0bn, +35% YoY (FY2025 £748m) — first time crossing £1bn.
- Statutory pre-tax profit £87.3m, +~44% YoY; adjusted pre-tax profit £172.6m, +20% YoY. Third consecutive profitable year.
- Customers 15.2m, +3.0m in the year (+25%); monthly active users 10.4m, +26%; ~49% use Monzo as primary bank; 1.6m+ on paid subscriptions.
- Customer deposits £25.7bn, +55% YoY (FY2025 £16.6bn).
- Card spend £73.0bn, +32% YoY (FY2025 £55.3bn); ARPAC £183, +11% YoY.

Note: the news body cites "over 9 million customers" / "seventh largest bank" — that is a stale figure from Monzo's Google Cloud case-study page, not current; Monzo itself reports 15.2m customers as of FY2026. Flag the 9m as outdated marketing copy, not a live metric.

**Trajectory / thesis context (no beat/miss — no new release).**
- Deposit growth (+55%) running well ahead of customer growth (+25%), i.e. deeper engagement / primary-bank adoption, not just account land-grab — this is the funding base that lets Monzo lend. Four income streams each >£300m (current-account balances, borrowing, payments, wealth), so revenue is diversifying off pure interest-income reliance.
- The multi-cloud/DR story is a cost and operational-resilience lever on a now-£1.7bn-revenue, £25.7bn-deposit book; relevant given the same-batch London cloud-outage item ([[EU regulators question Google over London cloud outage]]) — resilience is a regulatory and continuity concern at this scale, not a nice-to-have. Second-order: a credible continuous-DR posture de-risks the UK banking-licence/operational-resilience angle ahead of a potential IPO.
- Guidance: Monzo is private, UK-unlisted; no formal forward guidance or consensus exists. Press frames FY2026 as the setup for a possible London IPO (reported valuation discussions ~£4.1bn+ / prior CapitalG round at ~$5bn). No earnings guidance to assess — [UNSOURCED] on any forward figure.

Sources: https://monzo.com/annual-report (FY2026 Annual Report, published 2026-05-19) · https://monzo.com/annual-report/2026/Monzo-Annual-Report-2026.pdf · https://www.techmeme.com/260519/p6 (Bloomberg/Gani summary) · https://cloud.google.com/customers/monzo-bank (news source; "9m customers" figure is stale case-study copy)
<!-- /enrichment:earnings_review -->
