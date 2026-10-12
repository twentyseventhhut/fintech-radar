---
title: "WSJ: Amazon in talks to buy AI startup Decart for about $7B"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/amazon
  - company/decart
  - industry/ai
  - region/us
  - type/m-and-a
sources:
  - https://www.wsj.com/business/deals/amazon-in-talks-to-buy-ai-startup-decart-for-around-7-billion-9433abad
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: s2bd2859f
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# WSJ: Amazon in talks to buy AI startup Decart for about $7B

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] WSJ: Amazon обсуждает покупку ИИ-стартапа Decart примерно за $7 млрд

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.wsj.com/business/deals/amazon-in-talks-to-buy-ai-startup-decart-for-around-7-billion-9433abad>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: WSJ Amazon in talks to buy AI startup Decart for about $7B
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
WSJ reported (Sun 11 Oct 2026, wires picked it up 11–12 Oct) that Amazon is **"in talks"** to buy Israel-rooted AI startup **Decart** for **~$7B**. That is the whole fact. De-PR'd:
- **Rumor, not a deal.** "In talks," single primary source (WSJ). **Neither Amazon nor Decart confirmed or denied** (Amazon "declined to comment"; Decart silent). WSJ itself hedged a deal could happen "if talks do not fall apart or another suitor emerges." No signed agreement, no 8-K.
- **Structure undisclosed** — cash vs stock not reported (open). Price is "around $7B," not a fixed figure.
- **→ Why framed this way:** This is a leak-stage story, so the headline price does the work. The analytically important detail is buried: WSJ also reported **Anthropic explored buying Decart (~$6B, Aug 2026) and walked away after due diligence**. So Decart was already shopped and vetted — which both supports "a deal is in motion" AND is a red flag (why did the most sophisticated possible buyer pass post-diligence?). The $7B is a step-up from a ~$6B Anthropic look and from Decart's ~$4B Series C (May 2026, PitchBook) — ~1.75x in 5 months.

## [1] Competitors / peers
- **AMD → World Labs, ~$8.2B all-stock, announced 28 Sep 2026** ([[FT AMD acquires Fei-Fei Li's World Labs for $8.2bn]]) — a chipmaker buying a world-model lab to co-design silicon. Same logic, two weeks earlier, and it **sets the ~$7–8B price band** Amazon's rumored number sits just under. This is the single most load-bearing comp: it reframes Decart from "AI video toy" to "the silicon-adoption trade."
- **Google DeepMind Genie 3** (playable world model, ~24fps/720p) and **Runway Gen-4.5 "General World Model"** are the technical peers; **OpenAI pulled back from consumer video** (Sora app killed Apr 2026, Sora 2 API Sep 2026) — so the category is contested and churning, not settled.
- **→ Why the lay of the land is this way:** The valuable layer is not the flashy playable-Minecraft demo (Oasis, Oct 2024) but **model-to-silicon porting** (Decart's DOS stack). AMD paid up for exactly that capability binding. The multiple is being set by **chipmakers/hyperscalers needing CUDA-escape velocity**, not by content economics.

## [2] Company history / fit
- **Decart:** founded Sep 2023 by Dean Leitersdorf (CEO) + Moshe Shalev, both IDF Unit 8200; HQ Tel Aviv, offices SF/NY. Raised >$450M: Seed $21M → Series A $32M (~$500M, Dec 2024, Benchmark) → Series B $100M (~$3.1B, Aug 2025) → Series C $300M (~$4B, May 2026; Nvidia, Adobe, Toyota, Radical, Sequoia). Angels include Karpathy. **No disclosed revenue/ARR/users** — this is a research-lab/model shop, not a revenue business.
- **Amazon fit:** Amazon is **winding down its own Nova models** (several EOL Sep 2026) and leaning on Anthropic (minority stake, up to 5GW Trainium committed) + third-party models on Bedrock. Posture = **"own the infra, rent the models."** Decart's **DOS automates porting models off Nvidia/CUDA onto AWS Trainium** — and **Lucy2 already runs on Trainium3** (Annapurna cited >80% MFU). So there's a pre-existing relationship.
- **→ Why Amazon acts this way:** Amazon's Trainium bottleneck isn't silicon performance — it's **developer gravity toward CUDA**. Buying DOS removes "the primary barrier to Trainium enterprise adoption" and monetizes a multi-billion custom-silicon bet. The world-model/video layer is the secondary, more speculative thread.

## [3] Novelty / value-add / traction
- **Real novelty:** the credible value-add is the **chip-portability layer (DOS)**, not world models. World models are a crowded demo race (Genie/Runway/ex-Sora); Decart's durable edge is CUDA→Trainium automation — a scarce capability a hyperscaler can't easily build in-house fast.
- **Traction is unproven:** no revenue/ARR/user figures in any source. Valuation rests on **strategic scarcity + talent**, not unit economics. The playable-Minecraft/Oasis fame is marketing-grade, not adoption-grade.
- **→ Who captures the margin:** If Amazon owns the porting layer, it captures the switching cost that today anchors customers to Nvidia — the whole point. But if DOS value is mostly a thin optimization wrapper (and Anthropic's post-diligence pass hints the moat may be thinner than the $6–7B suggests), Amazon overpays for a feature, not a franchise. **Central question shifts from "is Decart a good AI company" to "is CUDA-escape worth $7B to AWS, and does Decart actually deliver it?"**

## [4] What's next / market sentiment
- **Watch:** official announcement + deal structure (cash/stock) + any FTC/EU signal. Until then, treat as unconfirmed.
- **Antitrust:** a $7B **full acquisition** (WSJ's framing, not an acqui-hire) faces real HSR/merger review. Precedents cut both ways: **Amazon–iRobot ($1.4B) abandoned Jan 2024** after EU/FTC pressure (cautionary); **Amazon–Adept (2024) acqui-hire still drew FTC scrutiny**; peer dodges Microsoft–Inflection, Google–Character.AI. **Mitigants:** Decart isn't a horizontal Amazon competitor (vertical silicon-adoption rationale defends more easily), but the **Israel HQ** adds a cross-border/foreign-investment wrinkle.
- **→ Counterintuitive second-order:** the AMD/World Labs comp makes this look "normal," but it also signals a **2026 scramble by chip/cloud players to buy world-model/porting labs** to defend custom silicon against Nvidia — capital is concentrating into a narrow, unproven-traction category, which makes any single ~$7B bet fragile, not safe.

## Top challenge/extra questions
1. Is there a signed deal or only a leak? — **Open; currently only "in talks" (WSJ).**
2. Why did Anthropic walk after diligence (~$6B, Aug 2026)? — **Open; unexplained. Material red flag.**
3. Cash or stock? — **Open; undisclosed.**
4. Does Amazon want DOS (silicon porting) or the world models? — **Analysis: primarily DOS/Trainium adoption; world models secondary.**
5. What is Decart's actual revenue/ARR? — **None disclosed; valuation = strategic, not financial.**
6. Is the ~$7B justified vs ~$4B (May 2026)? — **~1.75x in 5m; in-band vs AMD/World Labs ~$8.2B, but on zero disclosed revenue.**
7. Does DOS have a real moat or is it a thin wrapper? — **Open; Anthropic's pass is a negative signal.**
8. Antitrust exposure for a $7B full buy? — **Analysis: real HSR/EU review likely; vertical rationale + Israel HQ shape it.**
9. How unique is CUDA→Trainium porting? — **Analysis: scarce enough that a hyperscaler buys rather than builds — the core thesis.**
10. Is the world-model category settling or churning? — **Churning: OpenAI retreated, Google/Runway/AMD advancing.**
11. Could another suitor outbid? — **WSJ explicitly flags this risk; Nvidia/Adobe/Toyota are already investors.**
12. Does this move AWS numbers near-term? — **No; even if closed, impact is strategic/long-dated.**

## Sources
- WSJ (orig., paywalled): amazon-in-talks-to-buy-ai-startup-decart (11 Oct 2026); Reuters/Investing.com, Seeking Alpha, Tech Times pickups.
- Comp: AMD/World Labs — [[FT AMD acquires Fei-Fei Li's World Labs for $8.2bn]] (28 Sep 2026).
- Internal: [[Amazon sues Perplexity over agentic shopping tool]], [[AWS in talks to sell Trainium AI chip racks to outside companies]], [[Amazon ups India bet with $13B AI infrastructure investment]].
- Decart funding/profile: Contrary Research, SiliconANGLE (2024, 2026), The Next Web.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team verdict

**FRESHNESS: FRESH.** This is a distinct, new event — WSJ's 11 Oct 2026 report of Amazon/Decart talks. No prior corpus note covers this deal or these parties together; the only near-neighbor, [[FT AMD acquires Fei-Fei Li's World Labs for $8.2bn]], is a different acquirer and target (AMD/World Labs) and serves as a comp, not a duplicate. Not a reprint. (Caveat: fresh as a *report* — the underlying event is still only "in talks," unconfirmed.)

**Biggest red flags (anti-PR):**
- **It's a rumor, not a deal.** "In talks," single source (WSJ), no confirmation from either party, structure undisclosed, WSJ hedges talks could collapse. The headline risks overstating certainty.
- **Anthropic walked after due diligence** (explored ~$6B, Aug 2026, declined). The most capable AI buyer passed post-diligence — the loudest signal in the whole story, and it's buried. Suggests the moat may be thinner than the price implies.
- **Zero disclosed traction.** No revenue/ARR/users. ~$7B rests entirely on strategic scarcity (CUDA→Trainium porting) + talent, not economics. ~1.75x step-up from ~$4B in 5 months on nothing financial.
- **PR frame vs real substance:** the "AI world model / playable-Minecraft" angle is the marketing hook; the value-add, if real, is the DOS silicon-porting stack for Trainium adoption. Don't lead from the demo.
- **"MirageLSD" / exact product naming** could not be verified; current stack is DOS/Oasis/Lucy. Deal structure, close probability, and antitrust path all open.

**Importance: 3/5** — A $7B acquisition by Amazon of a buzzy AI lab is inherently newsworthy and strategically coherent (Trainium/CUDA-escape, mirroring AMD/World Labs). But it is unconfirmed, single-sourced, "in talks," with no disclosed traction and a negative post-diligence signal (Anthropic's pass). High potential weight discounted heavily for rumor status and unproven fundamentals. Would be a 4 if signed; 2 if it were pure acqui-hire noise.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Big-tech AI M&A is in a distinct regime where the Big Five are spending record capex on compute while doing historically few outright acquisitions: combined AI infra spend by Google/Microsoft/Apple/Amazon/Meta is projected near $600bn in 2026, yet outright Big-Five acquisitions hit a decade low (7 in 2024, ~14 in 2025, ~12 by May 2026) — per Futurum/analyst compilation, via fastaijobs acqui-hire map, Oct 2026. The dominant structure has been the "reverse acqui-hire" (license + hire founders, no company purchased) to dodge antitrust: Microsoft–Inflection (~$650m, 2024), Google–Character.AI (~$3bn license, 2024), Google–Windsurf (~$2.4bn license, 2025), Meta–Scale AI ($14.8bn for 49%, 2025) — same sources. Why now: Decart's economics sit at two scarce chokepoints — (a) inference-cost / chip-efficiency software (its Optimization Stack / "DOS", reported to help chips run more cheaply), and (b) real-time "world models" / generative-video (products Lucy and Oasis), a frontier sub-vertical for gaming/robotics/physical-AI synthetic data. A full acquisition (not a license) signals Amazon wants the asset inside AWS, not just the team.

**Competitive landscape.** Sector runs on compute-cost-per-token / inference efficiency, model latency (real-time generation), and talent. Key players circling Decart form a telling sequence: Nvidia (investor via the May round) entered exclusive talks → Decart's founders reportedly preferred Anthropic → Anthropic walked away after diligence on a ~$6bn mostly-stock deal → Amazon stepped in at ~$7bn (per Calcalist, SiliconANGLE, Yahoo/Bloomberg, Oct 2026). Basis of competition here is strategic control of the inference stack, not price. Amazon's position: it is simultaneously Anthropic's largest backer AND a strategic customer of Decart, so buying Decart directly after its own portfolio company passed is an unusual, aggressive vertical move — tightening the AWS/Trainium cost stack rather than relying on partners. Decart founded 2023 (Dean & Orian Leitersdorf, Moshe Shalev), Israeli; backers include Sequoia, Benchmark, Radical Ventures, Nvidia, plus angels Karpathy and Eisner. Amazon's own AI-infra moves in-base: [[AWS in talks to sell Trainium AI chip racks to outside companies]], [[Amazon raises AWS GPU reservation prices about 20% amid chip shortage]], [[Amazon ups India bet with $13B AI infrastructure investment]] — all point to compute-cost pressure that a chip-efficiency asset directly addresses.

**Comps & multiples.** Private asset, no revenue disclosed → EV/Revenue not computable ("no data" on fundamentals; revenue `[UNSOURCED]`). What IS sourced is the valuation step-up on the SAME asset over months: ~$3.1bn ($100m round) → ~$4bn (May 2026, $300m round led by Radical, Nvidia participating) → ~$6bn (Anthropic's lapsed offer) → ~$7bn (Amazon talks) — step-up arithmetic $7bn / $4bn = 1.75x in roughly five months (per Calcalist/Ynet, Oct 2026). Deal-size anchor: $7bn would exceed Amazon's $6.5bn MGM purchase (2022), its largest to date (per Ynet/Wikipedia M&A list). No comparable public world-model pure-play to mark against → distribution not computed, qualitative only. In-base acquisition comps for scale, not sector: [[Capital One to acquire Brex for $5.15 billion]], [[Stripe completes acquisition of Metronome]] (both fintech, included only as deal-size reference, not valuation comps).
IR grounding (PRIMARY): Amazon's latest filed financials — Q1 2026 earnings release 2026-04-29 (https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q1/earnings-result/AMZN-Q1-2026-Earnings-Release.pdf) and 10-Q filed 2026-04-30 (https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm); FY2025 10-K filed 2026-02-06 (https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm) — confirm Amazon has the balance-sheet capacity for a ~$7bn cash/stock deal; a transaction of this size, if signed, would surface in a future 8-K/10-Q (none filed as of the latest 8-K, 2026-06-12).

**Risk flags.**
1. Valuation step-up risk: 1.75x in ~5 months with no disclosed revenue — if Amazon pays ~$7bn and the world-model products (Lucy/Oasis) stay pre-revenue, this is a talent/strategic-option bet, not a cash-flow asset; write-down risk if the inference-efficiency IP doesn't translate onto Trainium/AWS economics.
2. Two prior suitors walked (Nvidia talks collapsed; Anthropic exited AFTER diligence) — diligence-signal risk: whatever Anthropic saw could equally stall or reprice Amazon's deal; "in talks" is not "signed."
3. Antitrust / optics: Amazon is Anthropic's largest investor buying an asset Anthropic just dropped and that it is itself a customer of — vertical-integration scrutiny, plus a cross-Atlantic (Israel) deal, could draw regulatory review that the acqui-hire structure was invented to avoid.

**What this changes (idea-lens).** If signed, this marks a shift from license/acqui-hire back to outright buying — hyperscalers absorbing the inference-cost layer directly to defend margin as the ~$600bn capex cycle bites (analysis). Falsifiable thesis: Amazon is buying chip-efficiency IP to lower AWS/Trainium cost-per-token more than it is buying generative-video; watch whether any signed 8-K/press framing leads with inference-stack/Trainium integration vs. consumer world-model products. Thesis breaks if the deal is restructured as a license/partial stake (acqui-hire relapse) or collapses in diligence like the prior two (analysis).

Sources: https://www.wsj.com/business/deals/amazon-in-talks-to-buy-ai-startup-decart-for-around-7-billion-9433abad · https://www.calcalistech.com/ctechnews/article/hjhzrluuml · https://www.calcalistech.com/ctechnews/article/sjt9ncukgl · https://siliconangle.com/2026/10/11/report-amazon-in-talks-with-ai-startup-decart-over-possible-7b-acquisition/ · https://www.ynetnews.com/business/article/hkiluhfszg · https://finance.yahoo.com/technology/ai/articles/anthropic-said-walk-away-6-012511516.html · https://www.fastaijobs.com/career-hacks/ai-acquihire-map-2026 · https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q1/earnings-result/AMZN-Q1-2026-Earnings-Release.pdf · https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] This is an M&A-talks story (reported ~$7bn bid for Decart), not an earnings release. The following grounds Amazon's latest reported results as context for its ability to fund AI-infra M&A; it is not a reaction to a print.

**Verdict (latest print, grounds the thesis).** Amazon's most recent report is **Q2 2026** (quarter ended 2026-06-30, released 2026-07-30; note: IR DB's newest cached filing is Q1 2026, so Q2 figures below are WebSearch-sourced, not from `ir_latest.json`). Read: **BEAT** · revenue $200.6bn (+20% YoY) · operating income $27.5bn (+43% YoY, from $19.2bn) · AWS $42.2bn (+36.7% YoY), the fastest AWS growth in ~18 quarters and a fifth straight quarter of acceleration. The engine funding a $7bn Decart bid — AWS — is accelerating, not decelerating. GAAP EPS of $5.75 is heavily flattered by a one-off (see thesis-flags).

**Key figures (Q2 2026, with growth).**
- Revenue **$200.6bn, +20% YoY**.
- Operating income **$27.5bn, +43% YoY** (vs $19.2bn Q2 2025) — operating leverage, not just top-line.
- Net income **$62.6bn**; GAAP diluted **EPS $5.75** — but this includes **$53.4bn non-operating pre-tax other income, primarily from the Anthropic stake revaluation**; stripped out, the number is far lower. Treat $5.75 as non-comparable.
- **AWS $42.2bn, +36.7% YoY**; AWS operating margin **~39%, +650bps YoY**; AWS sequential add ~$4.6bn (~80% above its prior largest-ever increase); ~$169bn annualized run-rate; backlog ~$496bn growing triple digits.
- **Capex: cash capex $53.1bn in Q2; FY2026 guidance raised to ~$220bn** (from ~$200bn prior), citing AI/data-center demand and inflated component prices (memory, HDD, SSD).

**AWS trajectory (why the acceleration matters for the deal).** AWS YoY: Q1 2026 **+28%** (then a 15-quarter high, ~$37.6bn) → Q2 2026 **+36.7%** (~$42.2bn). Overall revenue accelerated from +11.5% (Q3 2025) / +12.4% (Q4 2025) to +17% (Q1 2026) to +20% (Q2 2026). The reported ~$15bn+ AI run-rate and triple-digit Bedrock token growth are the strategic frame into which a Decart buy fits.

**Deal grounding (reported, M&A-talks).** WSJ (2026-10-11/12) reports Amazon in talks to buy AI startup Decart for **~$7bn** — a sharp step-up from Decart's ~$4bn valuation in May 2026. Decart (founded 2023) builds software to switch workloads seamlessly across AI chips; Amazon already gave it early access to its Trainium3 custom silicon in 2025. Talks follow prior Nvidia/Anthropic discussions that fell apart, so completion is not assured. Fit: chip-portability software directly supports Amazon's Trainium push to cut Nvidia dependence — consistent with the capex-and-AI thesis the Q2 print confirms.

**Thesis-flags.**
1. **Headline EPS is a mirage.** The $62.6bn net income / $5.75 EPS is ~$53.4bn inflated by the Anthropic mark-to-market gain (non-cash, non-operating). Second-order: the same AI boom props both the P&L (via the Anthropic revaluation) and the spend side (capex) — a reflexive loop; a reversal would hit reported profit even if operations are fine.
2. **Capex is outrunning its own guide** ($200bn → $220bn FY2026, with $53.1bn in a single quarter). Why it matters: a ~$7bn Decart deal is small vs the capex envelope and easily affordable, but every incremental AI commitment widens the ROIC-proof gap the Street is watching; component-cost inflation flagged by management pressures that return.
3. **AWS acceleration is the load-bearing pillar** (+36.7% YoY, 39% margin). If a Decart-type bolt-on improves chip flexibility and AWS AI capacity, it reinforces the pillar; the risk is integration/retention of a 2023-vintage startup at a 75%+ markup in ~5 months.
4. **Deal is talks-only** — may collapse like the prior Nvidia/Anthropic–Decart discussions; do not price it in.

Sources: WSJ via [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-11/amazon-is-in-talks-to-buy-ai-startup-decart-wsj-reports) · [Calcalist](https://www.calcalistech.com/ctechnews/article/ec25jzet0) · Q2 2026 results [Amazon IR](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/) and [release PDF](https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q2/earnings-result/AMZN-Q2-2026-Earnings-Release.pdf) · [TradingView 10-Q summary](https://www.tradingview.com/news/tradingview:15b8f73c13724:0-amazon-com-inc-q2-2026-revenue-200-6b-net-income-62-65b-eps-5-75-10-q-summary/) · AWS detail [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/amazon-q2-2026-earnings-aws-204411872.html) · Q1 2026 AWS +28% [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/amazon-q1-2026-earnings-beat-203149838.html) · IR cached latest = Q1 2026 release [drive/url](https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q1/earnings-result/AMZN-Q1-2026-Earnings-Release.pdf). Q3 2026 guidance specifics not located — no data.
<!-- /enrichment:earnings_review -->
