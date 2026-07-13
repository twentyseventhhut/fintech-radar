---
title: "DeepSeek to double headcount as it races AGI labs"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/deepseek
  - industry/ai
  - region/asia
  - type/commentary
sources:
  - https://substack.com/redirect/5095e8ce-8dea-4ad4-88ec-6fbb542c00a7
status: published
n_mentions: 1
channels:
  - "MTS"
story_id: sef82643b
month: 2026-06
enriched: true
importance: 3
freshness: fresh
---

# DeepSeek to double headcount as it races AGI labs

> [!info] 2026-06-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: MTS

## Агрегированный текст (из дайджестов)

[MTS] DeepSeek plans to double its headcount in order to better compete with AGI labs in China and globally. DeepSeek recently released their V4 model series and is raising at a $50 billion valuation, but Z.ai now has a better frontier model (GLM-5.2) and a higher valuation.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/5095e8ce-8dea-4ad4-88ec-6fbb542c00a7>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: DeepSeek to double headcount as it races AGI labs
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On ~2026-06-25 DeepSeek told staff it intends to **"at least double the size of every department"** and opened a hiring spree: ~33 listed roles across seven categories (full-stack/algorithms, AI core-system R&D, deep-learning research, model/data strategy, product, ops), mostly Beijing and Hangzhou, courting campus interns + full-timers framed as people who "tackle core AGI problems themselves" rather than star hires. The hiring is paired with — and funded by — DeepSeek's **first-ever external raise**: ~50bn yuan (~$7.4B) at a **>$50B valuation** (reported $52–59B post-money), closed late June 2026.
- **Why structured this way / what it reveals:** The headcount story is the *soft* half of a *hard* capital + governance story. The raise is highly unusual: outside commercial investors get **no direct equity, no voting rights, a 5-year lock-up**; capital flowed into an LP controlled by CEO Liang Wenfeng (he himself put in ~20bn yuan / ~$3B; Tencent ~10bn / ~$1.4B; CATL ~5bn). Only **China's state-backed AI fund** received direct equity + voting rights. So "doubling headcount" is the publishable, morale-facing wrapper around a state-tilted, founder-controlled war-chest. From a tiny base (~150–170 people today) "doubling" is operationally trivial; the real signal is the capital + governance structure, not the body count.
- **Note error flagged:** the source note claims "Z.ai now has … a higher valuation." That is **false** — Z.ai (Zhipu) IPO'd Jan 2026 at ~$6.55B; DeepSeek is ~$50B. The *model* claim (GLM-5.2 > DeepSeek V4) is defensible (see [1]); the *valuation* claim is not.

## [1] Competitors / peers
Chinese open-weights frontier cohort, mid-2026: **DeepSeek (V4)**, **Z.ai / Zhipu (GLM-5.2)**, **Alibaba Qwen**, plus MiniMax-M3, Kimi K2.6, Ant's Ling-1T. On Artificial Analysis Intelligence Index v4.1: **GLM-5.2 = 51**, ahead of MiniMax-M3 (44), **DeepSeek V4 Pro (44)**, Kimi K2.6 (43). Western frontier: GPT-5.5, Claude Opus 4.7 — DeepSeek V4 Pro is ~95% of frontier on agentic/coding (parity-to-ahead on SWE-bench/LiveCodeBench/Terminal-Bench, behind on pure knowledge/math/HLE), at **~65% lower cost**; V4 Flash ~85–90% of GPT-5.5 at ~1/20th cost.
- **Why the lay of the land / second-order:** DeepSeek's 2025 mystique was "frontier on a shoestring." By mid-2026 it has been **caught and arguably passed on the model itself by Zhipu's GLM-5.2** while being out-valued by it ~7x. So DeepSeek's moat is no longer "best Chinese model" but **brand + state backing + price**. The hiring spree is the structural answer to losing the benchmark crown: throw bodies + state capital at AGI to re-take leadership. Whether that converts is open — the China open-weights race is now a multi-horse field, not a DeepSeek monopoly.

## [2] Company history / fit
DeepSeek spun out of quant hedge fund **High-Flyer** (Liang Wenfeng), self-funded through R1 (the Jan-2025 "$6M / two months" cost-shock model that rattled US AI valuations). Trajectory: refused outside money for years → V4 launched **2026-04-24** (V4-Pro 1.6T total/49B active; V4-Flash 284B/13B; 1M context; open-weight) → April 2026 Tencent/Alibaba reportedly in talks at >$20B ([[Tencent and Alibaba in talks to invest in DeepSeek above $20B]]) → June 2026 closes ~$7.4B at >$50B.
- **Why it acts this way:** A quant-DNA, founder-controlled lab that historically prized small elite teams and self-funding has now reversed twice at once — taking outside capital AND mass-hiring. The structural pressure: compute + talent costs of the AGI race outran even High-Flyer's balance sheet, while rivals (Zhipu IPO'd, Qwen inside Alibaba) gained capital-market access. The voting-rights-to-state structure lets Liang raise without ceding control — keeping the founder-led ethos intact while plugging into state industrial policy.

## [3] Novelty / value-add / traction
Genuinely new here: (a) DeepSeek's **first external capital** after years of refusing it; (b) a **state-equity-only governance structure** that is itself a template/precedent for Chinese frontier-AI fundraising. The headcount line is the *least* novel element — doubling a ~150-person team is noise. Real traction is downstream of the **fintech cost angle**: DeepSeek-R1 already saw early adoption by Chinese banks (ICBC, Postal Savings Bank, Bank of Beijing/Jiangsu/Nanjing/Chongqing and mid-tier lenders) for risk control, contract verification, customer insight — Goldman/Morgan Stanley framed its cost curve as "supercharging AI adoption" for smaller institutions that couldn't afford OpenAI/Anthropic licensing.
- **Why value-add is real (1–2 levels deeper):** Open-weights + ~order-of-magnitude-cheaper inference (V4-Pro ~$0.45/M input) lets banks/insurers **self-host and control** the model — the decisive feature in finance (data residency, auditability, regulation). That's a structurally different value proposition from US labs that license closed APIs. **Margin capture:** because the weights are open, DeepSeek captures little direct rent per deployment — value leaks to integrators/cloud and to the banks themselves. So the multiple rests on *ecosystem dominance + state mandate*, not per-token economics. The risk: GLM-5.2/Qwen offer the same open-weights deal and are now benchmark-ahead — DeepSeek's cost-leadership moat is commoditizing within China.

## [4] What's next / market sentiment
Plan: hire aggressively toward AGI, ship next model gen to reclaim the benchmark lead, lean on state capital. Sentiment is bifurcated: bullish on China's open-weights momentum and DeepSeek's brand/cost; skeptical that mass-hiring from a tiny base + state-tilted governance translates to a frontier leap when Zhipu already out-benchmarks it. Regulatory backdrop: US CAISI/NIST evaluated V4 Pro (export-control + security scrutiny on Chinese models); state voting rights raise governance/geopolitical flags for any Western use.
- **Why the market goes this way / counterintuitive second-order:** Heavy state backing reads as strength but is **a fragility** — it deepens the geopolitical wall (export controls, Western enterprise avoidance, app-store/policy bans), capping DeepSeek's TAM to China + Global South even as the model is technically world-class. And concentrating governance in founder+state reduces the investor discipline that might force commercial focus → risk of a well-funded lab optimizing for "AGI prestige" over deployable, revenue-generating product. The central question is not "can DeepSeek hire fast enough" but **"can a state-anchored, open-weights lab capture durable value when its own price/openness strategy commoditizes the category and its geography caps its market."**

## Sources
- Bloomberg / SCMP / TechRadar — "double every department," ~33 roles, ~150–170 staff (2026-06-25).
- TechFundingNews / The Information / Trending Topics — $7.4B raise, >$50B valuation, state-only voting rights, 5-yr lock-up, Liang/Tencent/CATL contributions.
- TechCrunch / DataCamp / NIST CAISI / Artificial Analysis — V4 launch 2026-04-24, specs, benchmarks vs GPT-5.5 / Claude Opus 4.7; GLM-5.2 index = 51 vs V4 Pro 44.
- CFO Dive (Goldman) / Yicai / Capco / Global Finance / Risk.net — fintech cost angle, Chinese bank adoption of DeepSeek.
- Internal: [[Tencent and Alibaba in talks to invest in DeepSeek above $20B]]; [[Ant Group releases Ling-1T AI model]]; [[Chinese tech giants including Alibaba, ByteDance, and Tencent, are upgrading their agentic]].

## FRESHNESS / DUPLICATE VERDICT
**FRESH.** The internal corpus has the *April* >$20B talks ([[Tencent and Alibaba in talks to invest in DeepSeek above $20B]]) but no note covering the **closed June raise (~$7.4B / >$50B), the state-only-voting governance, or the headcount-doubling plan**. This is a genuine "talks → signed deal" follow-up plus a new operational announcement, not a reprint. Not stale.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Is the headcount story material at all?** Doubling a ~150–170-person team adds ~150 people — trivial vs the $7.4B raise. The real event is the **first external capital + state-voting governance**; the headline buries the lede. (answered: yes, hiring is the soft wrapper)
2. **Is the note's "Z.ai higher valuation" claim true?** **No — false.** DeepSeek ~$50B vs Z.ai ~$6.55B IPO (Jan 2026). The *model* superiority claim (GLM-5.2 > V4) is defensible; the valuation claim should be corrected, not repeated.
3. **Talks vs closed?** April 2026 it was *talks* at >$20B; June 2026 the raise is **closed** at >$50B. Confirm it's signed/closed (Bloomberg/The Information report closed). Open: exact final number ($52–59B post-money range cited).
4. **Who actually controls the company now?** Only China's state-backed AI fund got direct equity + voting rights; commercial money (Tencent, CATL) sits in a founder-controlled LP with no votes, 5-yr lock-up. Governance is founder + state — what does that mean for Western enterprise trust?
5. **Has DeepSeek already lost the benchmark crown?** GLM-5.2 (index 51) > DeepSeek V4 Pro (44). If so, "racing AGI labs" is partly a *catch-up* narrative, not leadership. (answered: yes, within China)
6. **What is the durable moat now — model, brand, or price?** Model lead is gone; price is commoditizing (Qwen/GLM also open + cheap). Likely brand + state mandate. Open whether that's defensible.
7. **Fintech angle — adoption real or announced?** Real for R1: ICBC, Postal Savings Bank, several mid-tier Chinese banks live for risk control/contract verification. Open: V4 adoption depth, and any non-China financial adoption (likely blocked by geopolitics).
8. **Who captures the margin?** Open weights → DeepSeek captures little per-deployment rent; value leaks to integrators, clouds, and the banks self-hosting. Multiple rests on ecosystem + state, not unit economics.
9. **Geopolitical TAM cap?** US CAISI/NIST scrutiny, export controls, state voting rights → Western enterprise/govt avoidance. Is DeepSeek's market structurally capped to China + Global South despite world-class models?
10. **Is "AGI" framing substance or recruiting PR?** "Humanity stands on the eve of AGI" + interns "solving core AGI problems" is morale/recruiting language. No dated capability milestone attached. Mark as PR framing.
11. **Why take outside money now after years of refusing?** Compute + talent costs of the race outran High-Flyer's balance sheet; rivals gained capital-market access (Zhipu IPO, Qwen inside Alibaba). Structural pressure, not opportunism.
12. **Does state backing read as strength or fragility?** Counterintuitive: it deepens the geopolitical wall and reduces investor discipline → risk of prestige-over-product. Argued as net fragility for global ambitions.
13. **Burn vs runway?** $7.4B is large but the AGI compute race is expensive; how many model generations does it fund? Open — no disclosed burn rate.
14. **Cross-source corroboration?** Headcount: Bloomberg + SCMP + TechRadar concur. Raise: TechFundingNews + The Information + Trending Topics concur on $7.4B/>$50B/state-voting. High confidence on core facts.
15. **What changes the central question?** From "can DeepSeek hire fast enough" → **"can a state-anchored open-weights lab capture durable value when its own price/openness strategy commoditizes the category and geography caps its market."**

Importance: 3/5 — A genuine, well-corroporated NEW event (first external raise closed, unusual state-voting governance, headcount plan) with a real fintech hook (cost-efficient open-weights models driving bank adoption). Capped below 4 because: the headline ("double headcount") is the least material part; DeepSeek has lost the China benchmark lead to GLM-5.2; open weights mean weak direct margin capture; and the source note carries a factual error (valuation claim). Important as a structural signal of the China open-weights + state-AI-capital dynamic, not as a standalone breakthrough.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-29]] (2026-06-29).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Subvertical: frontier AI labs / cost-efficient open-weights foundation models, with the fintech hook being self-hostable LLMs for banks. Sizing the *application* layer (not lab valuations): per Credence Research (via web), China AI-in-finance ~$3.66bn (2023) → ~$40.4bn (2032E) at ~30.6% CAGR; Grand View pegs China generative-AI-in-financial-services at only ~$1.67bn by 2033 at ~29.9% CAGR — the two figures differ ~24x, so treat as directional, not a hard TAM ("no data" on a clean number). Demand driver / "why now": Chinese open-weights models reportedly went from ~1% to ~15% of global model usage in a year (TrendForce, Nov-2025), and DeepSeek-R1 + Qwen reached rough parity with Western frontier — making self-hosted, auditable, cheap inference newly viable for regulated banks (data residency + supervisory compliance is the decisive feature, not raw quality). Second-order: the value migrates from the model layer (commoditizing, open) to integration/compliance and to the banks themselves — labs capture little per-deployment rent.

**Competitive landscape.** Sector KPIs that actually matter here: (1) benchmark rank (Artificial Analysis Intelligence Index / Code Arena), (2) inference price per 1M tokens, (3) external valuation / capital access. Players: DeepSeek (V4), Zhipu/Z.ai (GLM-5.2), Alibaba Qwen, MiniMax, Moonshot Kimi, Ant Ling — a multi-horse Chinese open-weights field, no longer a DeepSeek monopoly. Basis of competition has shifted from "best Chinese model" to **brand + capital access + price**, because the model lead is gone: GLM-5.2 sits at index 51 vs DeepSeek V4 Pro 44 (per note's [1], Artificial Analysis), and GLM-5.2 ranked #2 globally on Code Arena front-end (behind Claude Fable 5; SCMP/Caixin, Jun-2026). Recent peer move (dated): Zhipu listed Jan-2026, and on **2026-06-22** its market cap topped **HK$1 trillion (~$128bn)** after a 42% intraday surge on the GLM-5.2 launch (SCMP / Caixin / Nation Press). DeepSeek's position: **catching up, not leading** — its 2025 "frontier-on-a-shoestring" mystique is intact on *price* but it trails Zhipu on both benchmark and (now) valuation. Moat = brand + state backing + cost leadership `(analysis)`; all three are contestable (Qwen/GLM offer the same open + cheap deal).

**Comps & multiples.** Conventional EV/Revenue, EV/EBITDA, P/E are **not computable** — DeepSeek is private with no disclosed revenue/EBITDA (`[UNSOURCED]`). What can be shown is *relative valuation* of the two named China frontier labs and the price gap that anchors the fintech thesis:
- **DeepSeek:** ~$7.4bn raised (~50bn yuan) at **>$50bn** post-money (reported $52–59bn), closed late-Jun 2026 — first-ever external capital, state-only voting rights, 5-yr lock-up (TechFundingNews / Trending Topics / Tech Times).
- **Zhipu / Z.ai (GLM-5.2):** **~$128bn** public market cap as of 2026-06-22 (SCMP / Caixin). JPMorgan forecasts Zhipu revenue 4.6bn yuan (2026) → 30.9bn yuan (2028E, first profit). On that JPM 2026 figure, implied **P/S ≈ HK$1,000bn / ~5.0bn yuan ≈ very rich** (mixing HK$ market cap with yuan revenue — order-of-magnitude only, treat as "richly priced," not a clean multiple).
- **Valuation reversal (corrects the note):** the enrichment [0]/[2] flagged the source's "Z.ai higher valuation" as *false* using Zhipu's **Jan-2026 IPO price (~$6.55bn)**. On **current market cap** the original note is actually right — Zhipu (~$128bn) now out-values DeepSeek (~$50bn) by **~2.5x**, a reversal *vs* the note's "DeepSeek out-values Z.ai ~7x." The model-superiority claim (GLM-5.2 > V4) holds either way.
- **Inference-price comp (the real fintech multiple):** DeepSeek V4-Pro ~$0.435/M input, $0.87/M output; V4-Flash $0.14/$0.28 — vs GPT-5.5 $5/$30 and Claude Opus 4.7 $5/$25 (PricePerToken / DeepSeek docs). Worked example: 100M output tokens/mo ≈ $348 (V4-Pro) vs ~$2,500 (Opus 4.7) vs ~$3,000 (GPT-5.5) = **~7–9x cheaper**. This is the lever for smaller banks priced out of Western APIs.
- Internal comps: [[Tencent and Alibaba in talks to invest in DeepSeek above $20B]] (Apr-2026 talks → this June close); [[Ant Group releases Ling-1T AI model]] (peer open-weights). Distribution not computed — 2 labs, non-comparable basis (private round vs public mkt cap); qualitative comparison only.

**Risk flags.**
1. **Benchmark + valuation crown already lost to Zhipu** — GLM-5.2 (51 vs 44) and ~$128bn vs ~$50bn. "Racing AGI labs" is a *catch-up* narrative; the hiring spree is the structural answer to losing the lead, with no dated capability milestone attached (AGI framing = recruiting PR).
2. **Geopolitical TAM cap + governance toxicity for Western finance.** State-fund-only voting rights, US CAISI/NIST scrutiny, and moves like JPMorgan blocking Anthropic in HK over Greater-China licensing ([[JPMorgan Chase blocks Anthropic AI access for Hong Kong staff]], 2026-06-19) cut both ways — Western enterprise/govt will avoid a state-governed Chinese lab, structurally capping DeepSeek to China + Global South.
3. **Weak margin capture — open weights commoditize the layer.** Banks self-host (ICBC: localized DeepSeek deploy, 200+ AI use-cases, ~1bn calls/yr; Postal Savings, Bank of Jiangsu/Nanjing/Beijing also live — Global Times/Global Finance). Value leaks to integrators, clouds and the banks; per-token rent ≈ near-zero, and Qwen/GLM offer the identical deal. The >$50bn rests on ecosystem + state mandate, not unit economics — a thin support if the model lead doesn't return.

**What this changes (idea-lens).** `(analysis)` The signal is the **template, not the body count**: a state-equity-only, founder-controlled raise becomes a precedent for how China funds frontier AI without ceding control — and a structural divergence from the equity-and-votes Western model. Falsifiable thesis: if DeepSeek's next model gen does NOT retake the China benchmark lead from GLM-5.2 within ~2 quarters, the "racing AGI labs" framing is hiring/morale PR and the durable moat is brand + state distribution, not technology. Trigger to watch: DeepSeek V5 benchmark vs GLM-5.x, and whether *any* non-China financial institution adopts V4 in production (geopolitics likely blocks it).

Sources: https://techfundingnews.com/deepseek-raises-7-4b-at-50b-valuation-in-first-ever-external-funding-round/ · https://www.trendingtopics.eu/deepseek-raises-7-4-billion-only-the-chinese-state-gets-voting-rights/ · https://www.scmp.com/tech/article/3357858/zhipu-ai-market-cap-tops-hk1-trillion-shares-glm-52-developer-soar · https://www.caixinglobal.com/2026-06-23/new-model-propels-zhipu-ais-market-value-to-record-hk1-trillion-102456760.html · https://pricepertoken.com/compare/provider/anthropic-vs-deepseek · https://www.trendforce.com/news/2026/01/26/news-chinese-ai-models-reportedly-hit-15-global-share-in-nov-2025-fueled-by-deepseek-open-source-push/ · https://gfmag.com/technology/deepseek-ai-takes-root-in-chinas-banks/ · https://www.credenceresearch.com/report/china-ai-in-finance-market
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
