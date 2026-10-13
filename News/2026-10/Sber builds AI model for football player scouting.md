---
title: "Sber builds AI model for football player scouting"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/sber
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.sberbank.ru/ru/sberpress/all/article
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s9e87441d
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Sber builds AI model for football player scouting

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Разработал AI-модель для футбольного скаутинга, которая оценивает игроков с учетом их действий, партнеров по команде и соперников в конкретном матче

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.sberbank.ru/ru/sberpress/all/article>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sber builds AI model for football player scouting
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Sber's research teams (the "AI4Sport" / Sber AI group) published an **AI research result**, not a shipped product: a model that evaluates a footballer **contextually** — scoring a player's performance in a *specific* match while accounting for *who he played with and against* ("с кем и против кого он выходит на поле"), rather than from static aggregate ratings. It was trained on open player ratings so it can distinguish strong vs weak individual outings, and is pitched as an *additional data source for scouts* and for candidate-similarity / formation-fit, explicitly aimed "начиная с детско-юношеского футбола" (starting with youth football).
- **De-PR'd reality:** this is a **science/PR output**, not a bank product with users. Coverage is a single Sber press release mirrored verbatim across RU regional outlets (mskagency, primamedia, prokazan, togliatti24, astrakhan.su, 2026-10). No partner club, no league deal, no accuracy number, no pricing, no deployment — framed as "may become an additional source" (conditional). The note's single source URL is a generic `sberbank.ru/.../sberpress/all/article` stub.
- **Sibling, more concrete result (same AI-in-sport program):** on 2026-07-15 Sber + **PFK CSKA** published a *separate* model that tracks a footballer across a whole match from **a single camera**, identifying the correct player in **78%** of cases and flagging the other 22% as "undefined" to avoid false stats. Features used = jersey number + kit colour + physique/gait. It framed a new research task "Long-Term Player Identification (LTPI)" with a "Cost-Sensitive Identification Score (CSIS)" metric, trained on one 101-min match, led by **Konstantin Mitin** (head of AI-in-sport at Sber), and was a **CVPR 2026 (Denver) Best-Paper-Award nominee**. A third AI4Sport model, **PC-SSAS** (Player-Centric State-Space Action Spotting), took **2nd place at SoccerNet 2026**. Together these are the "invisible scouting" research line: cheap single-camera analytics for academies/regional clubs.
- **Why framed this way:** the press release leads with "scouting" because it is the commercially evocative word, but the substance is an *academic contextual-rating model*. The "youth football / regional clubs" angle is the honest tell — this is about lowering the cost of analytics (one camera, no multi-cam rig), i.e. a soft-power/ecosystem science story, not a bank revenue line.

## [1] Competitors / peers
Contextual player valuation and video-to-data football analytics are a **crowded, mature field** — Sber is a late academic entrant, not a pioneer:
- **SkillCorner, Stats Perform (Opta), Hudl/Wyscout, SciSport, Zone7, PFF FC, Sportlogiq** — commercial single-/broadcast-camera tracking and player-valuation products with paying clubs.
- **AiScout** (Wikipedia-notable; used by pro academies incl. Chelsea trials) — the direct "democratise scouting via phone video" analogue, already live with federations.
- **Possession-value / contextual metrics** (EPV, VAEP, "expected threat") are established since ~2019 academic work (KU Leuven, etc.) — Sber's "evaluate with teammates/opponents context" is this known lineage, not new.
- **Position: behind on traction, parity on research.** The CVPR Best-Paper *nomination* and SoccerNet 2nd place are legitimate academic signals (parity/credible), but there are **zero commercial clients** vs incumbents with league-wide deployments. **Why this matters (analysis):** in sports analytics the moat is proprietary tracking-data rights + club contracts, not a model paper; Sber has the paper and one friendly club (CSKA), not the data-rights flywheel.

## [2] Company history / fit
Fits Sber's "AI in every vertical on a domestic stack" strategy, but this is a **non-core diversification / science-PR** limb, not banking. Same-ecosystem siblings: flagship model [[Sber unveils flagship GigaChat 3.5 Ultra model]] (Jul 2026), finance agent [[Sber teaches AIFA financial analyst to self-plan analysis]] (2027 launch), wealth tool [[SberInvestments launches GigaChat tool explaining portfolio moves]], consumer AI [[Sber adds free Kandinsky 6.0 video generation to GigaChat]], and non-banking service bolt-ons like [[Sber adds car-wash booking and payment to SberBank Online]]. Note: this football model is **not** confirmed to run on GigaChat (it's computer-vision/ML, distinct from the LLM line) — do not assume a GigaChat tie-in.
- **Why Sber acts this way (analysis):** as a dominant bank with a large in-house AI research org (AIRI / Sber AI) and a brand-building need, publishing eye-catching, citable sports-AI papers is cheap PR + talent branding + a route to later sell analytics into the (sanctions-walled) RU/Global-South sports market where Western vendors are absent. It is the same "sovereign/accessible AI" logic as the Global-South GigaChat pitch — applied to sport.

## [3] Novelty / value-add / traction
- **What's genuinely new:** narrow and academic — formalising **LTPI as its own task + CSIS metric** and the single-camera 78%-or-abstain design (the CSKA paper) is a real, peer-reviewed contribution; the "abstain rather than mislabel" design is a sensible, honest engineering choice. The *scouting* model's "contextual rating" is **not novel** (EPV/VAEP lineage).
- **What's NOT proven:** **traction = zero.** No club using it in production, no scouting decisions made, no accuracy figure for the *scouting* model itself (the 78% belongs to the separate tracking model). "May become an additional source for scouts" is explicitly conditional.
- **Where the value/margin sits (analysis):** even if productised, player-valuation models are a **commodity feature** sold to a tiny TAM (pro clubs + academies); the margin in football data sits with whoever owns **tracking-data rights and league distribution** (Stats Perform/Opta, Hudl), not a model author. Sber captures reputational/ecosystem value and optionality, not a business. Single-camera cost reduction is the one real value lever (democratises academy analytics) — but that also commoditises the output and compresses any price.

## [4] What's next / market sentiment
- **Next:** more papers and competition entries (SoccerNet, CVPR cadence), possibly a pilot with CSKA or RFU youth academies; watch for a *named club deployment* or an accuracy number for the scouting model — absent those, it stays research.
- **Sentiment:** enthusiastic, undifferentiated RU regional-press reprinting of a Sber release; no independent evaluation, no international pickup of the *scouting* claim (the CVPR/SoccerNet results are the parts with genuine external validation).
- **Why the market goes this way (analysis):** AI football analytics is genuinely growing, but it is a **low-margin niche** dominated by data-rights holders. Sber's play is to build a cheap, sovereign, academy-grade stack inside a market Western vendors can't serve — a plausible regional monopoly-by-default, like its other AI lines, but one whose commercial ceiling is small. **Second-order:** the real asset being built is a **talent/brand magnet and a tracking-data corpus**, not a scouting product — the paper is the marketing, the data is the moat if one ever forms.

## Sources
- Sber AI football-scouting model (press-release reprints, 2026-10): https://www.mskagency.ru/materials/3568981 · https://primamedia.ru/news/2644377/ · https://prokazan.ru/tehnologii/view/sber-sozdal-ii-dla-avtomaticeskogo-razbora-futbolnyh-matcej · https://prospect.com.ru/news/7078911/
- Sber + PFK CSKA single-camera tracking, 78%, LTPI/CSIS, CVPR 2026 Best-Paper nominee, K. Mitin (2026-07-15): https://corp.cnews.ru/news/line/2026-07-15_issledovateli_sberbanka · https://www.championat.com/football/news-6545538.html
- Field context (prior art): https://en.wikipedia.org/wiki/AiScout · SkillCorner / Stats Perform (Opta) / Hudl-Wyscout (commercial incumbents)
- Internal: [[Sber unveils flagship GigaChat 3.5 Ultra model]], [[Sber teaches AIFA financial analyst to self-plan analysis]], [[SberInvestments launches GigaChat tool explaining portfolio moves]], [[Sber adds free Kandinsky 6.0 video generation to GigaChat]], [[Sber adds car-wash booking and payment to SberBank Online]]
- Primary (note stub): https://www.sberbank.ru/ru/sberpress/all/article
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions (second-order)

1. **Live product or research paper?** Research/PR output. No users, no club deployment, no pricing — "may become an additional source for scouts" is conditional. → announced, not adopted.
2. **Is the "scouting" capability novel?** No. Contextual player valuation (EPV/VAEP/expected-threat, since ~2019) and commercial platforms (SkillCorner, Stats Perform/Opta, Hudl/Wyscout, AiScout) long predate it. → not novel.
3. **Then what IS genuinely new?** Only the *sibling* CSKA paper's narrow academic contributions: formalising "Long-Term Player Identification (LTPI)" as a task + "Cost-Sensitive Identification Score (CSIS)" metric + single-camera 78%-or-abstain design. The scouting model itself is lineage work. → thin, academic novelty.
4. **Any accuracy/traction number for the scouting model?** None. The only hard number (78% correct, 22% "undefined") belongs to the *separate* single-camera tracking model, not the scouting rater. → open / absent.
5. **Does it run on GigaChat?** Not stated and unlikely — this is computer-vision/ML, distinct from the LLM line. Do not assume a GigaChat tie-in. → no evidence of GigaChat.
6. **Is coverage independent?** No — one Sber press release mirrored verbatim across RU regional outlets (mskagency/primamedia/prokazan/etc.). The CVPR-2026 Best-Paper *nomination* and SoccerNet-2026 2nd place ARE genuine external validation — but of the tracking/action-spotting work, not the scouting claim. → PR-sourced for the headline.
7. **Who captures the margin in football data?** Tracking-data-rights + league-distribution holders (Stats Perform/Opta, Hudl), not a model author. Sber gets reputation/optionality, not revenue. → value accrues elsewhere.
8. **How big is the TAM?** Tiny — pro clubs + academies. Single-camera "democratisation" lowers cost but also commoditises the output and compresses price. → low-margin niche.
9. **Why would Sber, a bank, do this?** Cheap PR + AI-talent branding + a sovereign/accessible-AI play into a sanctions-walled RU/Global-South sports market Western vendors can't serve. Mirrors the Global-South GigaChat pitch. → brand/ecosystem, not P&L.
10. **Is there a real partner/league?** Only PFK CSKA as a research collaborator (on the tracking paper). No RPL/league commercial deal; youth-football is the stated target. → research collaboration, not a league contract.
11. **What's the binding constraint to productisation?** Data-rights + club contracts + proven in-match accuracy for the *rating* model — none demonstrated. → commercialisation gap.
12. **What is Sber silent about?** Scouting-model accuracy, any pilot club, whether a human scout actually used it, licensing/pricing, and how the "contextual" rating is validated against outcomes. → key silences.
13. **Freshness — duplicate of a prior note?** No prior note covers the football/sports-AI line (siblings are GigaChat/AIFA/wealth, different subjects). The Oct-2026 scouting release is also a distinct event from the Jul-2026 CSKA tracking paper. → fresh, not a reprint.
14. **Does it move Sber's P&L or thesis?** No — immaterial to a ~RUB 1.7tn-net-profit bank; a science-PR limb of the AI ecosystem. → strategically colourful, financially negligible.
15. **What would raise its importance?** A named club/federation deployment, a published scouting-accuracy benchmark, or a commercial analytics product — none present today. → stays low until traction appears.

Importance: 2/5 — A legitimate but narrow AI research result (with real academic credibility on the *sibling* CVPR/SoccerNet tracking work) from Russia's dominant bank, in a non-core sports vertical. Discounts: the scouting "capability" is well-established prior art, it is a conditional research/PR output with zero commercial traction or disclosed accuracy, coverage is a single reprinted press release, it is likely not even GigaChat-based, and it is immaterial to Sber's economics — a regional brand/ecosystem signal, not a fintech or frontier-AI event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Sber's football-scouting model sits in AI-for-sports / sports-analytics, a niche far outside banking. Global sports-analytics market ~$5.8bn in 2025, projected ~$7.0bn in 2026, CAGR ~20% to ~$31bn by 2034 (per Fortune Business Insights / Straits / Grand View, via secondary citations, as of 2025–26); the broader "AI in sports" market ~$10.8bn in 2025 → ~$13.1bn in 2026 (per Precedence Research, via article). Predictive analytics is the dominant application (~41% share, 2025) and football is the largest segment — consistent with Sber's player-evaluation use case. Structure: fragmented, dominated by Western specialists (Opta/Stats Perform, Hudl/Wyscout, SkillCorner); value sits in proprietary tracking data + model accuracy; entry barrier is data access (event/tracking feeds) more than compute. Why now: this is a de-PR'd showcase, not a monetized business line — it demonstrates GigaChat/compute capability in a visible domain, aligned with Sber's "open AI ecosystem" push (GigaChat Ultra, Mar 2026; ~14m MAU across AI assistants per Sber) rather than a sports-data P&L.

**Competitive landscape.** Sector KPIs: model predictive accuracy, proprietary data coverage (matches/leagues tracked), club/federation contracts. Key players and basis of competition: Stats Perform/Opta and Hudl/Wyscout compete on data depth + installed base with pro clubs; Sber competes here only on a model/demo basis with no disclosed club adoption. Recent peer moves: Western scouting-data vendors already embed ML for player valuation and injury-risk; Sber's differentiator is contextual evaluation (player actions vs teammates/opponents in a given match) — credible as a research artifact. Sber's position: niche / peripheral entrant in sports specifically; the real moat is elsewhere — Sber's AI stack, compute (SberCloud, now on Chinese accelerators post-sanctions) and distribution across its ecosystem `(analysis)`. Internal comps (same Sber AI showcase/monetization pattern): [[Sber adds free Kandinsky 6.0 video generation to GigaChat]], [[Sber teaches AIFA financial analyst to self-plan analysis]], [[SberInvestments launches GigaChat tool explaining portfolio moves]], [[Sber unveils flagship GigaChat 3.5 Ultra model]] — all are AI-capability demos layered onto the ecosystem, the same de-PR'd template.

**Comps & multiples.** No deal, round, valuation or revenue attached to this scouting model → trading multiples not computable, "no data". IR grounding (scale check): Sber FY2025 IFRS net profit RUB 1.705tn (+7.9% y/y), ROE 22.7%, EPS RUB 77.8 (Sber Summary Consolidated IFRS 12M 2025, 2026-02-26, via TASS/Investing.com). AI contribution is bank-wide, not sports: Sber claims AI drove >RUB 350bn additional profit in 2024 (per secondary citation) — i.e. ~20% of annual profit scale. Against that, a football-scouting model is immaterial to the P&L: revenue/users/contracts for this product = `[UNSOURCED]`. External peer valuations (Stats Perform, Hudl) are private, no verifiable post-money → "no data". Distribution not computed; qualitative only.

**Risk flags.** (1) Non-core execution / diversification track record — Sber's past digital-ecosystem build-out ran heavy losses (ecosystem lost ~RUB 19.2bn in H1 2021, ~RUB 14.3bn negative EBITDA, per bne IntelliNews) and ended in divestitures (SberDevices/SalutDevices sold Jan 2023; Okko, Zvuk, Evotor, STC exited); a sports-AI foray risks the same non-core drift unless it stays a cheap showcase. (2) Monetization opacity — no disclosed customer, pricing or club contract; classic "announced vs adopted" gap, so it reads as marketing for GigaChat rather than a revenue line (who's silent: economics). (3) Competitive/data moat — incumbent scouting-data vendors own the proprietary tracking feeds and club relationships; Sber has no stated data-rights advantage, and geopolitical isolation limits access to Western leagues' data and hardware (Chinese accelerators substituting Nvidia), capping international reach.

**What this changes (idea-lens).** `(analysis)` Nothing material for the sector or for Sber's valuation — this is an AI-capability flex that reinforces the GigaChat ecosystem narrative, not a move into sports-tech. Falsifiable thesis: if within ~12 months there is no paying club/federation contract or disclosed revenue, treat it as pure marketing; the thesis flips only on a signed adoption deal (RPL club, RFU, or export to a non-sanctioned league) — that would be the catalyst worth watching.

Sources: https://tass.com/economy/2092243 · https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · https://www.fortunebusinessinsights.com/sports-analytics-market-102217 · https://www.precedenceresearch.com/ai-in-sports-market · https://www.klover.ai/sberbank-ai-strategy-analysis-of-dominance-in-banking-ai/ · https://www.intellinews.com/sber-considers-listing-digital-subsidiaries-in-a-few-years-220819/ · https://tadviser.com/index.php/Company:SberDevices_(SalutDevices,_formerly_SberDevices)
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No earnings event in this story.** This item is an AI-venture/product announcement (Sber's football-scouting model) — not a results release. The following folds in Sber's OWN latest reported financials as IR context only.

**Verdict (headline read, context only).** Record FY2025 — net profit RUB 1.705tn (+7.9% YoY), ROE 22.7%, driven by net interest income (+18.5%) offsetting flat fee income and rising costs; 50% payout maintained (dividend ~RUB 850bn recommended). 2026 trend is re-accelerating: 9M 2026 RAS net profit +18.2% YoY. The scouting-AI story has no financial figures of its own.

**Key figures — FY2025 IFRS (reported 2026-02-26).**
- Net profit: RUB 1.705tn, +7.9% YoY (vs RUB 1.580tn FY2024) — a record.
- ROE: 22.7% (FY2025).
- Net interest income: RUB 3.55tn, +18.5% YoY — main growth engine.
- Net fee & commission income: RUB 833.7bn, −1.1% YoY — flat/soft, the weak line.
- Cost-to-income ratio: 30.3%; operating expenses RUB 1,237bn, +16.5% YoY (personnel + tech investment).
- Capital adequacy ratio ~13.7%; total equity RUB 8.3tn (+16.4% YTD).

**Latest 2026 figures (RAS, to augment — standalone bank, not Group IFRS).**
- 9M 2026 RAS net profit: ~RUB 1.5tn, +18.2% YoY; ROE 23.0%.
- September 2026: net profit RUB 168.5bn, +12.1% YoY; ROE 23.4%.
- 9M 2026 net interest income +24.1% YoY to ~RUB 2.8tn; net fee & commission income RUB 534.6bn, −0.8% YoY (fee softness persists into 2026).

**Guidance / dividend.** Dividend policy = 50% of IFRS net profit; for FY2025 the supervisory board recommended a 50% payout (~RUB 850bn). Investor Day 2025 (2025-12-10) reaffirmed ROE target above ~22%; FY2026 RAS run-rate (ROE ~23%) is tracking above that.

**Thesis-flags (context for the AI venture, not an earnings read).**
1. NII is carrying the P&L (+18.5% FY2025, +24.1% 9M 2026 RAS) while fee income is flat-to-down (−1.1% FY2025, −0.8% 9M 2026) → earnings quality leans on rate margin; the AI/non-financial ecosystem push (of which scouting-AI is a small signal) is management's answer to the stalled fee engine — second-order: watch whether AI/ecosystem monetization ever shows up in the fee line.
2. Record profit + 23% ROE in a slowing Russian economy with cost growth (+16.5% opex) still contained to a 30.3% CIR → operating leverage intact; AI/tech spend is inside that opex, so the scouting model is funded from a healthy base, not a stretched one.
3. No results event in this story — do not treat the scouting-AI announcement as financially material; it is a reputational/R&D data point, not a reported metric.

Sources: Sber FY2025 Summary Consolidated IFRS Financial Statements 12M 2025, 2026-02-26 (primary) https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf · https://tass.com/economy/2092243 · https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · https://www.akm.ru/eng/news/sberbank-s-ras-net-profit-for-the-first-nine-months-of-2026-increased-by-18-2-/ · FY2025 dividend/payout: https://tass.com/economy/2074501 · FY2025 dividend per-share: no data.
<!-- /enrichment:earnings_review -->
