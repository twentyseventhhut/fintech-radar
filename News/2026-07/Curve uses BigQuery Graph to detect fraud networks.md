---
title: "Curve uses BigQuery Graph to detect fraud networks"
date: 2026-07-01
retrieved: 2026-07-01
tags:
  - company/curve
  - industry/fraud-risk
  - region/uk
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/db0d74e1
  - https://www.connectingthedotsinpayments.com/r/600a155e
status: enriched
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s3eb7834e
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# Curve uses BigQuery Graph to detect fraud networks

> [!info] 2026-07-01 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 Curve uses BigQuery Graph to tackle fraud networks. The UK FinTech uses graph analytics to uncover linked fraud networks by identifying shared devices, payment cards, and contact details across accounts, improving its ability to detect organized fraud at scale.

[Connecting the Dots in Payments] 🇬🇧 Curve uses BigQuery Graph to tackle fraud networks. The UK FinTech uses graph analytics to uncover linked fraud networks by identifying shared devices, payment cards, and contact details across accounts, improving its ability to detect organized fraud at scale.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/db0d74e1>
- <https://www.connectingthedotsinpayments.com/r/600a155e>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Curve uses BigQuery Graph to detect fraud networks
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Curve (UK card-aggregation wallet, acquired by Lloyds for ~£120M, closing H1 2026 — see [[Lloyds Banking Group to acquire digital wallet Curve]]) disclosed that it uses **Google BigQuery Graph** to detect organized fraud. The mechanism: model accounts/devices/cards/contact details as a graph and run **entity-resolution / shared-attribute linking** — one device fingerprint or card tied to many "unrelated" accounts is the classic fraud-ring signature. This surfaces linked clusters that flat SQL joins miss at scale.

- **De-PR'd reality:** this is **not a Curve product announcement and not a new capability launch**. It is a **customer testimonial embedded in a Google Cloud product-marketing post** ("Introducing BigQuery Graph" / "Spanner Graph + BigQuery Graph" blog), re-surfaced by two curated newsletters (Connecting the Dots in Fintech / in Payments) as a one-line item. The primary framing is Google selling BigQuery Graph GA (GoogleSQL graph queries went GA in 2025), with Curve as the reference logo. Attribution reported to **Francis Darby, VP Data & ML at Curve** (per web summary — not verified against a primary quote).
- **The one hard number** floating in coverage — **"~£9.1M in savings"** — appears in AI-summarized search results, **NOT** in the newsletter text loaded in this note, and I could not confirm it against a primary Google/Curve page. **Treat as unverified/marketing** until sourced. No timeframe, baseline, or methodology accompanies it.
- **Why framed this way:** graph entity-resolution for fraud rings is a **decades-old, commoditized technique** (Palantir, Neo4j, Feature­space, Quantexa all built businesses on it). Google needs marquee fintech logos to sell BigQuery Graph GA; Curve, mid-integration into Lloyds, gains a "we do sophisticated fraud ML" signal. The item is **vendor co-marketing**, not a Curve milestone. → central question shifts from "is Curve's fraud tech novel?" (no) to "why is a sub-scale, being-acquired wallet the reference customer, and does the £9.1M claim survive scrutiny?" (open).

## [1] Competitors / peers
- **[[Klarna and Google Cloud enter strategic AI partnership]]** (Oct 2025) — the direct peer: Klarna also uses Google Cloud to train **graph neural networks** for fraud/AML, analyzing user–transaction–device relationships. Klarna's is GNN (learned embeddings); Curve's disclosed use is graph **querying/entity-resolution** (GQL patterns), a shallower, rules-adjacent technique. Klarna is far larger (114M users) → Curve is the smaller, later, less-sophisticated logo on the same Google stack.
- **[[Marqeta delivers AI-driven risk decisioning for fraud prevention]]** (Apr 2026) — real-time authorization risk score, 300+ attributes, per-transaction. Different axis (real-time point-of-auth ML vs. Curve's batch graph forensics).
- Also in corpus: [[Thredd launches fraud solution with Featurespace]], [[Fintech Wrap Up Sardine on real-time financial crime AI]], Mastercard (two decades of network AI). All show fraud ML/graph is **table stakes**, not differentiation.
- **Position: catching-up / parity at best.** Quantexa (UK, ~$2B+ valuation) is built entirely on graph entity-resolution for fraud/AML and is a UK-native leader; Curve running graph queries in BigQuery is a **buyer of commodity infra**, not a builder of edge.

## [2] Company history / fit
Curve's trajectory (see [[Lloyds Banking Group to acquire digital wallet Curve]], [[Curve shareholder IDC Ventures files challenge to block Lloyds deal]]): raised ~£250M, growth slowed, layoffs, governance dispute (IDC Ventures ~12% opposed the deal), sold to Lloyds for ~£120M (below capital raised). Fit: a card-aggregation wallet sits on top of *other* issuers' cards → it sees a cross-card behavioral graph, so graph fraud detection is **logical**. But structurally Curve is being absorbed; publishing a Google testimonial now reads as **narrative-burnishing during integration**, or simply Google's timing. → Why: a distressed asset mid-acquisition has strong incentive to signal technical competence; a hyperscaler has incentive to name any recognizable fintech.

## [3] Novelty / value-add / traction
- **Novelty: low.** Shared-device/card/contact graph linking to bust fraud rings is textbook (fan-out, shared-attribute rings, short-paths-to-risky-nodes). BigQuery Graph GA (2025) is the only genuinely-new element, and that is **Google's** innovation, not Curve's.
- **Traction: unverified.** The £9.1M figure is the only quantification and it is **not primary-sourced here** — no baseline, period, or definition (fraud avoided? ops cost saved?). No disclosure of false-positive impact, coverage, or live-vs-pilot. Treat as **announced/marketed, not demonstrated**.
- **Who captures the margin:** Google (recurring BigQuery compute/storage spend). Curve gets a fraud-loss reduction *if* the number is real, but as an acquired entity the value accrues to **Lloyds'** eventual integrated risk stack, not to Curve as an independent franchise. The durable asset is the **cross-card graph data**, which Lloyds now owns.

## [4] What's next / market sentiment
- Curve's independent future is limited — it folds into Lloyds (H1 2026). This fraud-graph capability is most relevant as **something Lloyds inherits**, plausibly feeding Lloyds' broader fraud/AML analytics program (Lloyds separately ran a 2026 quantum money-mule graph trial with IBM — analysis, adjacent not same).
- Market backdrop: payment fraud projected to rise sharply (Marqeta cited +153% 2025–2030); every issuer/wallet is bolting on graph + ML. Regulatory pressure (UK APP-fraud reimbursement rules) raises the ROI of catching mule/ring networks.
- **Second-order (analysis):** the item's real signal is **Google Cloud's push to win fintech fraud/AML workloads with BigQuery Graph GA** — Curve is a data point in that campaign, not the story. For Curve specifically the weight is low: commodity tech, unverified numbers, a company losing independence.

## Top challenge/extra questions
See challenge file.

## Sources
- Note aggregated text: Connecting the Dots in Fintech / in Payments (2026-07-01), one-line item each.
  - https://www.connectingthedotsinfin.tech/r/db0d74e1
  - https://www.connectingthedotsinpayments.com/r/600a155e
- External (web, 2026-07-04): Google Cloud "Introducing BigQuery Graph" / "Spanner Graph + BigQuery Graph" blog (Curve as reference customer; Francis Darby VP Data & ML quote — reported); "£9.1M savings" figure appears only in AI-summarized results, **unverified**.
  - https://cloud.google.com/blog/products/data-analytics/introducing-bigquery-graph
  - https://cloud.google.com/blog/products/data-analytics/the-unified-graph-solution-with-spanner-graph-and-bigquery-graph
- Peer/prior notes: [[Klarna and Google Cloud enter strategic AI partnership]], [[Marqeta delivers AI-driven risk decisioning for fraud prevention]], [[Lloyds Banking Group to acquire digital wallet Curve]], [[Thredd launches fraud solution with Featurespace]].
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is the "£9.1M savings" real?** It appears only in AI-summarized web results, not in the newsletter text or a confirmed primary page. What is the baseline, timeframe, and definition (fraud avoided vs. ops cost)? — **OPEN / likely marketing.**
2. **Whose announcement is this actually?** The framing is a **Google Cloud** product post promoting BigQuery Graph GA with Curve as a reference logo — not a Curve product launch. Does that downgrade its weight as "Curve news"? — **Yes.**
3. **Is graph fraud detection new for Curve or for the industry?** Shared-attribute entity resolution is decades-old (Quantexa, Neo4j, Palantir, Featurespace). What is Curve's *delta*? — **None evident.**
4. **Query graph vs. GNN:** Curve's disclosed use is graph *querying* (GQL patterns), not learned graph neural networks like [[Klarna and Google Cloud enter strategic AI partnership]]. Is this materially less sophisticated? — **Likely yes.**
5. **Live or pilot?** Is this in production catching real fraud, or a showcased implementation? No adoption metrics (rings caught, precision, false-positive delta) disclosed. — **OPEN.**
6. **Attribution:** Is the "Francis Darby, VP Data & ML" quote real and primary-sourced? Currently only in web summary. — **Unverified.**
7. **Why now?** Curve is mid-acquisition by Lloyds (governance dispute, below-cost sale). Is this technical-competence signaling during integration, or just Google's timing? — **Ambiguous.**
8. **Who owns the value?** As Curve folds into Lloyds, does this capability/data accrue to Lloyds' fraud stack rather than to Curve? — **Yes; the cross-card graph is the durable asset.**
9. **Data edge:** Curve's card-aggregation model gives a cross-issuer behavioral graph competitors lack. Is *that* (not BigQuery) the only genuinely interesting angle? — **Plausibly, but unquantified.**
10. **Duplicate check:** Does any prior corpus note cover this exact Curve/graph-fraud event? — **No** (closest is Klarna+Google GNNs, different company). → **fresh, not a duplicate.**
11. **Vendor lock-in:** What recurring BigQuery compute cost does this imply, and does Google capture the margin? — **Google is the clear economic winner.**
12. **Regulatory tailwind:** Does UK APP-fraud reimbursement liability make ring/mule detection higher-ROI, and is that the real driver? — **Likely a background driver.**
13. **Comparability:** How does this differ from Lloyds' own 2026 IBM quantum money-mule graph trial? Overlap or separate programs? — **Separate/adjacent (analysis).**
14. **Second-order:** Is the true story "Google Cloud winning fintech fraud/AML workloads," with Curve as one data point? — **Yes.**
15. **Net weight:** Commodity technique + unverified numbers + vendor-authored framing + company losing independence → does anything here move the market? — **Little.**

Importance: 2/5 — Commodity graph-analytics fraud technique, disclosed as a Google Cloud customer testimonial rather than a Curve milestone; the only hard figure (£9.1M) is unverified marketing; Curve is mid-absorption into Lloyds. Fresh (no prior corpus coverage of this event) but low weight. Marginal value only as evidence of Google Cloud's push into fintech fraud/AML workloads.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Curve — UK card-aggregation "wallet-over-wallets" — sits in the fraud/risk-analytics + graph-database subvertical, not fraud-tech per se: it's a *consumer* of a graph tool (Google BigQuery Graph), not a vendor. Sector size: the fraud-detection & prevention (FDP) market is ~$70.2bn in 2026 → ~$171.8bn by 2031 (CAGR ~19.6%; per MarketsandMarkets via researchandmarkets.com / mordorintelligence.com, as of 2026); the narrower *graph-databases-for-fraud* niche was ~$2.34bn in 2024 growing ~22.1% CAGR toward ~$16.9bn by 2033 (per Dataintelo, as of 2026 — single-vendor secondary source, treat as directional). Structure: highly fragmented — pure-play fraud platforms (Feedzai, Unit21, Alloy, Socure), graph-DB engines (Neo4j, TigerGraph, AWS Neptune, hyperscaler-native BigQuery/Spanner Graph), plus in-house builds like Curve's. Why now: (1) organized fraud has shifted from lone actors to *rings* sharing devices/cards/contact details across many synthetic accounts — a topology relational SQL detects poorly and graph traversal detects natively (fact → why: linked-account patterns are edges, not rows → why it matters: multi-hop link analysis surfaces collusion invisible to per-transaction rules → second-order: liability/chargeback losses compress); (2) hyperscalers (Google's GQL/SQL-PGQ BigQuery Graph, GA-era 2026) collapsed the build-cost of graph fraud analytics, letting a mid-size fintech run it without standing up a dedicated Neo4j/TigerGraph cluster.

**Competitive landscape.** KPIs the subvertical runs on: fraud-loss basis points on TPV, false-positive / precision rate, alert-to-investigation handle time, multi-hop query latency. This is not a market Curve *competes* in — it's a buyer. Named tooling: Google BigQuery Graph (the pick's subject) vs. Neo4j (dominant property-graph, Cypher) and TigerGraph (parallel, multi-hop analytics — claims 40–337x faster than Neo4j at 5+ hops, per tigergraph.com — vendor marketing, `[UNSOURCED]` as independent fact). Basis of competition among engines: query latency at depth, ISO-GQL standardization, and native integration with the customer's existing data stack — the last is exactly why Curve, already on BigQuery, chose BigQuery Graph over a standalone graph DB (switching-cost/data-gravity moat for the hyperscaler, not for Curve). Curve's own position: a card-aggregation consumer fintech, acquired by Lloyds Banking Group (announced 2025-11-18, per IR); the fraud-graph story is an internal ops win, not a product it sells. Recent peer move: Feedzai launched "RiskFM" financial-crime foundation model (2026-03-25, [[Feedzai unveils RiskFM AI financial crime model]]).

**Comps & multiples.** No deal/valuation in the news — this is an ops/product item, so trading multiples are **not applicable**. Curve is private and now inside Lloyds; no standalone market cap. Total raised >$250m (per Samsung Next release, 2024-06-24, IR); last independent round £37m led by Hanaco (2025-03-14, IR) — a funding round valuation, not a market cap, and post-money not disclosed → "no data". Internal comps (fraud/risk-analytics adjacencies, as directional peers not valuation comps): [[Feedzai unveils RiskFM AI financial crime model]] · [[Alloy AI-driven fraud and identity risk platform sponsorship]] · [[Fintech Wrap Up Unit21 named to 2026 RegTech100 list]] · [[Themis acquires fraud platform Pasabi, expands social monitoring]]. Multiple arithmetic: **not computed** — no publicly verifiable revenue/EV pair for Curve or the private peers. Distribution not computed; qualitative comparison only.

**Risk flags.**
1. **Unverified savings claim.** The circulating "~£9.1m saved" figure (Google Cloud case-study origin) is a *vendor-attributed* number with no audited basis and no baseline disclosed — PR data, not a KPI; treat as marketing. Why: case-study ROI numbers are self-selected and rarely net of the tool's own cost.
2. **Not a moat / commoditizing capability.** Graph fraud analytics on a hyperscaler is now a buy-not-build commodity — every BigQuery-resident fintech can flip it on. Why: no durable edge accrues to Curve; the value (data gravity, lock-in) accrues to Google, and de-PR'd this is "we adopted a standard tool," not a differentiator.
3. **Signal timing / stale-owner risk.** Curve is being absorbed into Lloyds; a mid-2026 fraud-tooling announcement reads partly as integration-era hygiene. Why: post-acquisition, the graph-fraud stack may be folded into Lloyds' own risk infrastructure, so Curve's independent narrative here has a short shelf life.

**What this changes (idea-lens).** (analysis) The signal is sector-wide, not Curve-specific: hyperscaler-native graph (BigQuery/Spanner Graph, Neptune) is beginning to disintermediate standalone graph-DB vendors (Neo4j/TigerGraph) *inside* mid-market fintech fraud stacks — the incumbents keep the deep-analytics / very-large-graph high end, hyperscalers take the "already-on-our-warehouse" long tail. Falsifiable thesis: if BigQuery/Spanner Graph adoption for fraud keeps surfacing in fintech case studies through 2026–27, expect Neo4j/TigerGraph to re-position toward GraphRAG/agentic and away from commodity fraud link-analysis. What would break it: a wave of fintechs publicly standardizing on Neo4j/TigerGraph specifically for real-time (OLTP) fraud, where hyperscaler batch-graph is weaker. Trigger to watch: whether Lloyds keeps Curve's BigQuery Graph stack or migrates it post-integration.

Sources: https://cloud.google.com/blog/products/data-analytics/introducing-bigquery-graph · https://www.mordorintelligence.com/industry-reports/global-fraud-detection-and-prevention-fdp-market-industry · https://dataintelo.com/report/graph-databases-for-fraud-detection-market · https://www.puppygraph.com/blog/tigergraph-alternatives · https://www.investegate.co.uk/announcement/rns/lloyds-banking-group--lloy/curve-acquisition/9242567 · https://www.prnewswire.com/il/news-releases/curve-secures-37m-investment-led-by-hanaco-ventures-as-the-company-approaches-profitability-and-prepares-to-launch-curve-pay-in-2025-302401910.html (IR drive: https://drive.google.com/file/d/1nOLJ8uHPhIy_6URCWKT2tRhqWlW1oe7K/view)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** NO-DATA on the news itself (this is a fraud-tooling / product item, not a results release) — but the latest audited accounts are a MISS on profitability. Backdrop: FY2024 (Curve OS Group Ltd, since renamed *Kerem Naboth Limited*, reg. 13619624) — turnover £27.6m (+3.3% YoY) but gross profit collapsed to £2.2m (-55.5% YoY), operating loss widened to £(33.0)m and loss for the year to £(35.0)m (vs £(31.1)m restated); net liabilities deepened to £(58.1)m. No guidance (private co.). This is context only; the story carries no financials.

**Key figures (FY2024 consolidated, year ended 31 Dec 2024; 2023 = restated per note 27).**
- Turnover: £27.613m vs £26.733m — +3.3% YoY.
- Cost of sales: £(25.399)m vs £(21.760)m — +16.7% YoY (grew ~5x faster than revenue).
- Gross profit: £2.214m vs £4.973m — **-55.5% YoY**; gross margin 8.0% vs 18.6% (-10.6pp).
- Administrative expenses: £(35.223)m vs £(35.000)m — +0.6% YoY (broadly flat).
- Operating loss: £(33.009)m vs £(30.027)m — loss widened 9.9% YoY.
- Interest payable: £(1.332)m vs £(0.983)m — +35.5% YoY (rising debt cost); plus a £(0.976)m fair-value remeasurement (new, 2023: nil).
- Loss before tax: £(35.169)m vs £(30.893)m — loss widened 13.8% YoY.
- Loss for the financial year: £(35.046)m vs £(31.112)m — **loss widened 12.6% YoY** (KPI-rounded "£(35.0)m vs £(31.1)m").
- Cash & equivalents: £36.124m vs £15.258m — +136.8% YoY (narrative cites £34.4m vs £13.3m — funding-driven, not operating).
- Net liabilities / total equity: £(58.131)m vs £(26.708)m — **deteriorated £31.4m**; P&L reserve deficit £(264.8)m.
- Operating KPIs: Annual GTV £3.2bn vs £3.4bn — **-5.9% YoY** (volume shrank); avg staff 196 vs 208 (vs 228 in prior text) — headcount cut.

**By segment / driver.** The topline barely grew (+3.3%) while cost of sales rose +16.7%, gutting gross profit. Management attributes the -55.5% gross-profit drop to "non-recurring prior-year gross profit items" in FY2023 (one-off scheme incentives / recognitions), and claims *underlying* unit economics improved via premium pricing, a revised pricing framework and lower acquiring costs. Admin expenses held flat (£35.2m) despite headcount cut to 196 (from 228) — restructuring/automation savings offset relaunched paid advertising. GTV fell to £3.2bn, so revenue growth came from monetisation/take-rate, not volume. June 2024: Curve became a Principal Member of Visa.

**vs expectations / prior period.** No public consensus for a private UK fintech — beat/miss is assessed vs prior year. MISS on every profit line: gross profit -55.5%, operating loss -9.9% wider, net loss -12.6% wider, net liabilities -£31.4m deeper. The only positives are cash (+137%, but debt/SAFE-funded, not earned) and management's *claimed* underlying-margin improvement (which the reported 8.0% gross margin does not yet show). [Exact consensus figures: no data — private company.]

**Guidance / forward.** No guidance issued (private company; no forward numbers disclosed). Forward frame is dominated by the post-year-end event: Curve OS Holding Ltd + subsidiaries agreed to be **acquired by Lloyds Banking Group** (announced 2025-11-18), subject to conditions — so the standalone earnings trajectory is being subsumed into Lloyds. Going-concern support is investor funding (Hanaco Ventures round + SAFEs / convertible loan notes; Lord Stanley Fink joined as Chairman). Absent the Lloyds deal, the £(58.1)m net-liability position and £(35.0)m annual loss imply continued external-funding dependence.

**Thesis-flags.**
1. **Gross profit -55.5% while revenue is roughly flat** → the "approaching profitability" narrative (from the Mar-2025 Hanaco round PR) is not visible in the FY2024 GAAP numbers; the loss *widened*. Why it matters: monetisation quality is thin (8.0% gross margin) and depends on premium/pricing changes management calls "underlying" — second-order: the fraud-network graph tooling (this story) is a cost-side loss-reduction lever, sensible when acquiring/fraud costs are eating an already-thin gross margin.
2. **Net liabilities deepened to £(58.1)m; cash is funding-driven, not operating** → the +137% cash build is debt/SAFE-financed; operating cash generation is not demonstrated. Second-order: solvency rests on continued shareholder support and, decisively, on the Lloyds acquisition closing.
3. **GTV -5.9% (£3.2bn) with headcount cut to 196** → the platform is shrinking volume while cutting costs; growth is being traded for margin/survival. Second-order: a fraud-detection efficiency play (BigQuery Graph) fits a cost-discipline, not a land-grab, posture.
4. **Rising financing cost + new £1.0m fair-value remeasurement** → interest payable +35.5% and a fresh SAFE-linked FV charge signal capital-structure strain feeding into the loss.

Sources: Curve OS Group Ltd / Kerem Naboth Ltd FY2024 consolidated accounts, year ended 31 Dec 2024 (Companies House, reg. 13619624, filed 2026-05-18; approved 8 May 2026) — [Companies House filing](https://find-and-update.company-information.service.gov.uk/company/13619624/filing-history/MzUyMTY3MTE2MWFkaXF6a2N4/document?format=pdf&download=0) · Lloyds acquisition RNS 2025-11-18 [drive_url](https://drive.google.com/file/d/1RLved83g6XEDCI9NtArCJBaTV-i05hAm/view) · Hanaco £37M round PR 2025-03-14 [drive_url](https://drive.google.com/file/d/1nOLJ8uHPhIy_6URCWKT2tRhqWlW1oe7K/view) · public consensus/whisper: no data (private company). No earnings in this news item; figures are latest-accounts backdrop only.
<!-- /enrichment:earnings_review -->
