---
title: "Amazon cloud capacity sold out through end of 2027"
date: 2026-10-27
retrieved: 2026-10-27
tags:
  - company/amazon
  - industry/infrastructure
  - industry/ai
  - region/us
  - type/commentary
sources:
  - https://www.reuters.com/business/retail-consumer/amazon-cloud-capacity-sold-out-through-2027-ceo-jassy-says-2026-10-23
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: s8c5a58c6
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Amazon cloud capacity sold out through end of 2027

> [!info] 2026-10-27 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Reuters: Облачные мощности Amazon распроданы до конца 2027

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.reuters.com/business/retail-consumer/amazon-cloud-capacity-sold-out-through-2027-ceo-jassy-says-2026-10-23>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 23 Oct 2026, in a podcast with Andreessen Horowitz (a16z), Amazon CEO Andy Jassy said AWS cloud-computing capacity is largely/nearly sold out through the end of 2027, with a meaningful chunk of 2028 already pre-committed. Jassy framed demand from AI labs and enterprises as effectively insatiable and said Amazon "could invest a lot more and it wouldn't be a bad use of capital," signaling the bottleneck is supply (power, chips, data-center buildout), not demand. AWS still reserves some capacity for on-demand use, Bedrock inference and EC2. (Reuters, 2026-10-23, per the note's source link.)

**[1] Scale / numbers.** Amazon raised 2026 cash capex guidance to ~$220B (up from ~$200B), citing higher memory costs. AWS backlog stood at ~$496B, growing triple digits. AWS revenue reportedly reaccelerated to ~36.7% YoY (~$42.2B/quarter), its fastest growth in ~18 quarters, up from ~20% a year earlier. Amazon is scheduled to report Q3 2026 earnings on 29 Oct 2026 (two days after this note's date), which is the hard test of these claims.

**[2] Why it matters for fintech.** AWS is the default cloud for a large share of banks, payment processors and fintechs (e.g., in-DB notes: Danske Bank, Nationwide, UOB, Prosus, 2C2P, FIS on AWS; Stripe/Coinbase on AgentCore Payments). A sold-out window through 2027 means financial institutions racing to deploy GenAI may face capacity rationing, reservation-price premiums and multi-year forward commitments rather than elastic on-demand scaling — a shift from cloud's original "pay-as-you-go" promise. It also concentrates systemic dependence: the UK already designated AWS/Microsoft/Google/Oracle as Critical Third Parties, and recent AWS outages (Coinbase trading halt; UAE data-residency waiver) show fintech exposure to a single constrained provider.

**[3] Prior art / trajectory (internal).** This is the latest beat in a consistent AWS supply-squeeze story, not a one-off:
- [[Amazon raises AWS GPU reservation prices about 20% amid chip shortage]] — pricing power from scarcity (2026-06).
- [[AWS in talks to sell Trainium AI chip racks to outside companies]] — Amazon monetizing/expanding silicon supply (2026-06).
- [[Amazon ups India bet with $13B AI infrastructure investment]] — capacity buildout response (2026-06).
- [[Prosus signs three-year AWS deal to accelerate AI adoption]] — the multi-year forward-commitment pattern this note predicts (2026-10).
- [[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]] — regulatory concentration angle.

**[4] Competitive read (AWS vs Azure vs GCP).** Capacity constraint is industry-wide, which blunts "AWS is uniquely strained" readings: Microsoft said Azure demand exceeds supply at least through end-2026, with ~$80B of Azure orders unfulfillable on power constraints and Microsoft Cloud backlog ~$678B (+84% YoY). Google Cloud backlog ~$514B (+46% YoY). So all three hyperscalers report multi-hundred-billion backlogs and supply-bound growth; AWS's "sold out through 2027" is a sharper verbal framing of the same GPU/power/data-center bottleneck. Reads bullish for AWS near-term revenue visibility but raises execution risk on the $220B capex (memory-cost inflation, power availability).

Sources: https://www.reuters.com/business/retail-consumer/amazon-cloud-capacity-sold-out-through-2027-ceo-jassy-says-2026-10-23 · https://finance.yahoo.com/technology/articles/amazon-cloud-capacity-sold-2027-230625002.html · https://www.datacenterknowledge.com/infrastructure/amazon-lifts-ai-infrastructure-spending-to-220b-as-demand-outpaces-capacity · https://futurumgroup.com/insights/microsoft-q4-fy-2026-ai-demand-accelerates-azure-and-enterprise-growth/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge**

1. **Is "sold out" literal?** No. Jassy's own framing is "largely"/"nearly" sold out; AWS explicitly reserves capacity for on-demand, Bedrock and EC2. The headline overstates a nuanced capacity-planning comment. (answered)
2. **Was this a formal disclosure or a podcast remark?** A podcast (a16z), not an SEC filing or earnings call. Lower evidentiary weight; the real number test is the 29 Oct 2026 Q3 print. (answered)
3. **Is "sold out" bullish or bearish?** Ambiguous. Bullish for revenue visibility (backlog ~$496B) but it caps near-term upside — you can't sell capacity you don't have. The constraint is supply, so growth is gated by buildout, not demand. (answered)
4. **Does the $496B backlog = guaranteed revenue?** No. Backlog includes long-dated, potentially cancellable or re-priceable commitments; triple-digit growth may partly reflect mega-deals (Anthropic/OpenAI-type) with concentration risk. (answered)
5. **Is AWS uniquely constrained vs peers?** No — Azure (demand>supply through end-2026, ~$80B unfulfillable orders) and Google Cloud (~$514B backlog) report the same bottleneck. "Sold out" is framing, not a moat. (answered)
6. **What's the actual binding constraint?** Reporting points to power, data-center shell availability, and memory-cost inflation (cited reason for the $220B capex bump) more than raw GPU supply alone. (answered)
7. **Does the fintech angle hold?** Partially. Direct fintech impact is second-order: capacity rationing and reservation-price premiums (see GPU price-hike note), plus forward-commitment deals. Few fintechs are at the frontier-training scale that actually saturates capacity. (answered)
8. **Could this be AWS talking its book ahead of earnings?** Plausible — a bullish demand narrative two days before Q3 results frames expectations. Treat as management messaging, verify against actuals. (open — resolved by 29 Oct print)
9. **Is the ~37% AWS growth figure confirmed?** Sourced to analyst previews/aggregators, not yet to the official Q3 release at note date. Treat as estimate. (open)
10. **Capex $220B — credible to deploy?** Execution risk is high: power interconnect queues, chip delivery, and memory inflation could slip the buildout, meaning "sold out through 2027" partly reflects inability to build fast enough, not pure demand strength. (answered)
11. **Does this change cloud's pricing model for banks?** Directionally yes — scarcity pushes customers toward multi-year reserved commitments over elastic on-demand; but on-demand remains for non-AI workloads. Overstating a regime change would be wrong. (answered)
12. **Systemic-risk read?** Valid concern — UK CTP designation + recent AWS outages (Coinbase halt, UAE waiver) show concentration risk; a sold-out AWS discourages multi-cloud redundancy for cost reasons. (answered)
13. **Any chance capacity frees up (demand air-pocket)?** Possible if an AI capex correction hits in 2027; long forward commitments could then become overhang rather than strength. Non-trivial tail risk. (open)
14. **Duplicate of a prior in-DB note?** No. Related beats (GPU price hike, Trainium racks, $13B India) are distinct events; this specific 23 Oct Jassy sold-out-through-2027 claim is new. (answered — fresh)
15. **Is the Reuters source text actually loaded?** No — the note has only the headline/link, no extracted body; enrichment rests on web verification of the same Reuters story + corroborating outlets. (answered)

**Importance: 3/5** — A high-visibility, widely-corroborated macro-infrastructure signal confirming AWS supply-bound AI growth and a $220B capex regime, with real second-order fintech implications (capacity rationing, concentration/CTP risk, shift to reserved commitments). Capped below 4 because it's a podcast remark (not hard data), peers show the same constraint (no AWS-specific edge), the fintech link is indirect, and the authoritative numbers land on the 29 Oct Q3 call.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector context.** This is a demand-side signal for the AI cloud buildout, not a company earnings event (it comes from a pre-earnings interview; Amazon reports Q3 2026 on Oct 29, 2026). Jassy's claim — 2026 capacity sold out, 2027 "largely sold out," and "a good chunk" of 2028 already committed, leaving reserves only for on-demand EC2 and Bedrock inference — is consistent with an industry-wide pattern of supply-constrained, not demand-constrained, cloud. All three hyperscalers report the same: Google Cloud carries a ~$460B backlog and Microsoft reportedly sits on ~$80B of unfulfilled Azure orders it cannot power. Combined 2026 hyperscaler capex is tracking ~$660–730B, with Amazon ~$220B, Alphabet ~$195–205B, Microsoft ~$175B, Meta ~$130–145B. The binding constraint is increasingly power and (per Amazon) memory cost, not chips or capital.

**In-base comps (news DB).** The vault already tracks the supply/demand mechanics behind this: [[AWS in talks to sell Trainium AI chip racks to outside companies]] (2026-06) shows Amazon monetizing its own silicon as a lever against GPU scarcity, and enterprise AWS AI adoption notes (OCC genAI, Experian migration) corroborate the enterprise-demand leg. No in-base note yet directly quantifies the "sold out" backlog, so this is a net-new data point rather than a duplicate.

**IR grounding (EDGAR / Amazon IR — real figures).**
- AWS growth is re-accelerating off a very large base, which is what makes "sold out" credible rather than hype. Q1 2026 8-K (Apr 29, 2026): Jassy — "AWS is growing 28% (our fastest growth in 15 quarters) on a very large base, our chips business topped a $20 billion run rate." ([8-K ex-99.1](https://drive.google.com/file/d/1oROIVAsOv7xyriJDmaCaQ4IiDgCxQ8IY/view) / [SEC](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000012/amzn-20260331xex991.htm)). Street expects AWS +30–41% YoY in Q3 2026 (Q2 2026 was +37% to $42.2B, fastest in 18 quarters).
- Scale context: 2025 total revenue $717B, +12% YoY ($638B→$717B); North America $426B (+10%), International $162B (+13%), with AWS the margin engine. 2025 Shareholder Letter / ARS (Apr 2026): [drive_url](https://drive.google.com/file/d/1ZRXSDzNtDIrzI1RlzboZllpH-b78iP6N/view) / [SEC](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041036/tm263815d4_ars.pdf). Prior year for trend: 2024 AWS revenue $91B, +19% YoY ([2024 ARS/letter](https://drive.google.com/file/d/1-fTCNgsw4K0kinR7ZQHSPV-SvSVLWYPb/view)).
- Capex guide: Amazon guided ~$220B cash capex for 2026 (up from a prior ~$200B, raised chiefly on higher memory cost), with most directed at AWS AI infrastructure. This is the spend behind the "sold out" capacity. (Q3 2026 guide/Jassy interview, Oct 2026.)
- Note: ir_latest.json `latest_result` is a 2026-06-12 procedural 8-K; the financially load-bearing figures above come from the Q1 2026 earnings 8-K and the 2025 ARS, which are the correct grounding docs.

**Risk flags (skeptical).**
1. **Pre-earnings framing / unquantified.** "Sold out" is a CEO interview characterization, not a reported backlog figure. Amazon does not disclose a committed-backlog number the way Google/Microsoft do (RPO), so the claim is hard to independently verify until Q3 (Oct 29) data lands.
2. **Circular-demand quality.** A large share of committed capacity is tied to AI labs whose ability to pay depends on future funding — e.g. OpenAI's ~$38B / reported multi-year AWS commitment and Anthropic's ~$100B+ decade commitment, both paired with Amazon investments (compute-credit structures). "Sold out" to not-yet-profitable counterparties is lower-quality than enterprise bookings.
3. **Capex / depreciation drag.** ~$220B capex front-loads cost while revenue and margin from new capacity arrive later; a demand air-pocket or slower ramp would compress AWS operating margin and ROIC even if top-line "sold out" holds.
4. **Power & memory as the real ceiling.** The constraint has shifted to electricity and memory pricing (Amazon itself cited memory for the capex hike). "Sold out" may partly reflect inability to build fast enough rather than pure pull — a supply failure dressed as demand strength.
5. **Industry-wide signal, not an Amazon moat.** Azure (~$80B unfulfilled) and Google Cloud (~$460B backlog) report the same scarcity; the "sold out" headline is table stakes across hyperscalers and does not by itself imply AWS share gains.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Earnings context for the "AWS sold out through 2027" story.** The capacity remark (Jassy, a16z podcast, ~Oct 23, 2026) lands between prints: the most recent *reported* quarter is **Q2 2026** (reported Jul 30, 2026; period ended Jun 30, 2026). Q3 2026 reports Oct 29, 2026 — two days *after* this news — so Q3 figures below are company guidance / Street expectation, not results. Note: Amazon is IR-covered but the pipeline IR db lags (latest cached quarterly release = Q1 2026); Q2/Q3 figures are grounded in Amazon's own release and SEC filing via web.

**Verdict (headline read).** Q2 2026 = BEAT · net sales $200.6bn (+20% YoY; vs ~$196.2bn public consensus, ≈ +$4.4bn / +2.2%) · GAAP diluted EPS $5.75, but that includes a **$53.4bn non-operating, non-cash pre-tax mark-to-market gain "primarily from our investments in Anthropic"**; **ex-gain EPS ≈ $1.97 vs ~$1.86 consensus (≈ +6%)** · driver = AWS re-acceleration to +37% · guidance: Q3 net sales $197.0–202.0bn (+9–12%), operating income $22.5–26.5bn. This is the read directly relevant to the "sold out" claim: demand, not reported revenue, is the binding constraint.

**Key figures (Q2 2026, reported).**
- Net sales **$200.6bn, +20% YoY** (vs $167.7bn Q2 2025).
- Operating income **$27.5bn, +43% YoY** (vs $19.2bn); operating-income guidance for Q2 had topped out at the low-$20s, so a clean operating beat.
- Net income **$62.6bn** / diluted EPS **$5.75** (vs $18.2bn / $1.68) — inflated by the **$53.4bn pre-tax Anthropic mark** (non-cash, set by a private funding round, non-recurring). Strip it and operating profit ($27.5bn) is roughly *half* reported net income; the headline EPS is a paper number, not cash.

**By segment / driver (the AWS line is the thesis).**
- **AWS: net sales $42.2bn, +37% YoY — fastest growth in 18 quarters**, fifth straight quarter of acceleration (Q2'25 +17% → +20% → +24% → +28% → **+37%**). AWS operating income **$16.6bn vs $10.2bn** YoY (≈39% segment margin); AWS is the dominant profit engine.
- **AWS backlog (RPO) $496bn**, up from $364bn in Q1 (ex-Anthropic), growing triple digits YoY — a ~3.3x forward book on ~$148bn TTM AWS revenue. This backlog is the quantitative backbone of the "sold out through 2027" claim: contracted demand is running far ahead of deliverable capacity.
- North America $116.2bn (+16%); International $42.2bn (+15%). Amazon's AI business crossed a **~$25bn annualized** run-rate; custom-silicon (Trainium) and Bedrock cited as capacity draws.
- Prior quarter Q1 2026 for trend: net sales $181.5bn (+17%), **AWS $37.6bn (+28%)**, AWS operating income $14.2bn (~37.7% margin), total op income $23.9bn. So AWS accelerated +28% → +37% sequentially — consistent with "demand outrunning supply."

**vs expectations / prior period.** Revenue beat public consensus (~$196.2bn) by ≈$4.4bn/+2.2%; AWS ($42.2bn) beat the ~$40.5bn Street number. Ex-Anthropic EPS ~$1.97 beat ~$1.86 (≈+6%). AWS +37% beat the ~31–33% the Street modeled pre-print. YoY momentum strongly positive and *accelerating* on the one line that matters for a capacity story. (Public consensus per aggregators as of the Jul 30, 2026 print; no paid feed.)

**Guidance / forward.** Q3 2026 guided net sales **$197.0–202.0bn (+9–12%)** and operating income **$22.5–26.5bn** (the +9–12% headline decelerates vs +20% partly on FX/retail base effects, not AWS). Capex: management **raised 2026 capital expenditure to ~$220bn** (from ~$200bn prior), explicitly AWS/AI-weighted — the direct funding side of "sold out." Jassy's framing ("could invest a lot more and it wouldn't be a bad use of capital") signals the ceiling is build-out speed, not demand. Management tone on AWS: confident/supply-constrained. What they stay quieter on: free cash flow is under pressure from the capex ramp, and the ~$220bn spend front-loads depreciation that will weigh on the AWS margin that currently looks pristine. Q3 2026 actuals land Oct 29, 2026 (not yet reported here).

**Thesis-flags.**
1. **Capacity, not demand, is the binding constraint (fact→why→matters).** $496bn backlog + "sold out through 2027 / good chunk of 2028 spoken for" → revenue is now gated by how fast Amazon can energize data centers, chips and power, not by selling. Second-order: revenue visibility is unusually high, but so is execution risk on the build-out — any slip (power, memory, Trainium yield) converts straight into deferred revenue.
2. **$220bn capex is the double-edged flag.** It validates the demand story but compresses near-term FCF and seeds a depreciation wall; the +39% AWS segment margin is unlikely to hold as newly-built capacity depreciates. Watch whether AWS *dollar* operating income keeps rising faster than D&A.
3. **Headline EPS is distorted by the $53.4bn Anthropic mark** — non-cash, round-based, reversible. Don't anchor on $5.75; the operating story (+43% op income, +37% AWS) is the real signal. De-PR: the number that moves the thesis is backlog + AWS growth, not GAAP EPS.
4. **Deceleration risk in the guide.** Q3 +9–12% total optically decelerates; confirm it's retail/FX base, not AWS cooling, when Q3 prints Oct 29.

Sources: Amazon Q2 2026 release (aboutamazon.com / ir.aboutamazon.com; period ended Jun 30, 2026; reported Jul 30, 2026) · SEC 8-K/10-Q amzn-20260630 (sec.gov) · Q1 2026 release AMZN-Q1-2026-Earnings-Release.pdf (s2.q4cdn.com, drive-cached) · public consensus via StockAnalysis/Yahoo/TradingKey aggregators (as of Jul 30, 2026 print) · Jassy capacity remarks via Reuters/Yahoo/TipRanks (Oct 23, 2026). Q3 2026 figures = guidance/expectation only (actuals report Oct 29, 2026 — after this news date).
<!-- /enrichment:earnings_review -->
