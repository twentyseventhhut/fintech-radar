---
title: "Google DeepMind delays Gemini 3.5 Pro again"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - company/google
  - industry/ai
  - region/us
  - type/product
sources:
  - https://substack.com/redirect/b3de9037-7897-4937-ae91-b55b7a4d8313
status: enriched
n_mentions: 1
channels:
  - "MTS"
story_id: s306a0172
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# Google DeepMind delays Gemini 3.5 Pro again

> [!info] 2026-07-17 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: MTS

## Агрегированный текст (из дайджестов)

[MTS] Gemini 3.5 Pro is delayed, again. Google DeepMind’s latest frontier model is nowhere to be found nearly two months after the release of Gemini 3.5 Flash and five months after 3.1 Pro. GDM’s public models are now behind Anthropic, OpenAI, Meta, xAI, Z.ai, and Moonshot, and possibly ByteDance, DeepSeek, and MiniMax. Multiple top researchers have left the org in recent weeks, including Gemini’s co-lead, Noam Shazeer, now at OpenAI.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/b3de9037-7897-4937-ae91-b55b7a4d8313>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Google DeepMind delays Gemini 3.5 Pro again
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
Google DeepMind's flagship **Gemini 3.5 Pro** is still unreleased ~2 months after **Gemini 3.5 Flash** (shipped 2026-05-19) and ~5 months after **3.1 Pro** — so the tentpole model is missing while the cheaper Flash tier ships on time. The hard catalyst is Bloomberg's **2026-07-16** report ("Gemini launch delayed as tech falls short of internal goals"), sourced to ~10 current/former employees: the original target was **June 2026** (Pichai at I/O, ~May 2026) and the model is now "months behind," with a late-June retraining-data pass that "fell short of expectations." Stated bottleneck = **coding capability below the internal bar**, not an officially cited safety/compute reason.
- **De-PR caveat:** Google **disputes the framing** on-record — a spokesperson only said it is "currently testing 3.5 Pro, an upgraded Flash, and other models with partners" and "shipping quickly… cost-effective." That is neither a confirmation nor a denial of a delay. → The corpus text's flat list of rivals "ahead" (Anthropic, OpenAI, Meta, xAI, Z.ai, Moonshot, and possibly ByteDance/DeepSeek/MiniMax) is a **directional community read, not a benchmarked ranking** — treat as sentiment, not scoreboard.
- **Why this framing lands hard now:** the slip is being read alongside a **DeepMind talent exodus** — Gemini co-lead **Noam Shazeer → OpenAI**, plus Nobel laureate John Jumper and researchers Jonas Adler / Alexander Pritzel → Anthropic (see corpus). "Model slips + org bleeds talent" is a compounding narrative, which is why a known slip became a market event. **(analysis)**

## [1] Competitors / peers
A **"Christmas in July" frontier cluster** landed the same week Google slipped — maximally bad optics:
- **xAI / SpaceXAI Grok 4.5** — released 2026-07-08/09, pitched as an "Opus-class" cheaper/more-efficient model [[SpaceXAI releases Grok 4.5, an 'Opus-class model']].
- **Anthropic Claude Fable 5 / Mythos** — topped the hardest coding benchmarks; deployment traction visible in corpus [[Linas Newsletter deployment playbook for Claude Fable 5]], [[Elon Musk praises Mythos and Fable, vows not to cut off Anthropic]].
- **OpenAI GPT-5.6** family — GA ~2026-07-09 (reported); strong coding; also poached Gemini's co-lead Shazeer.
- **Low-cost Chinese frontier** (DeepSeek, GLM, Qwen, MiniMax, Moonshot) eating the cost-efficiency angle Google usually owns [[New low-cost Chinese AI model rivals Anthropic and OpenAI]], [[DeepSeek annualized revenue nears $500 million]].
- **Position: catching up / behind on the flagship tier.** Why the lay of the land is this way: Google's structural edge is **cost-efficient Flash-tier + distribution (Android/Search)**, not necessarily the frontier reasoning/coding crown — and precisely on coding is where 3.5 Pro is stuck. Second-order: rivals shipping first on coding means Google defends on **distribution**, but the EU just weakened even that moat [[EU forces Google to give Gemini rivals equal Android access]]. **(analysis)**

## [2] Company history / fit
Trajectory: **Gemini 3.5 Flash** shipped 2026-05-19 with full benchmarks; **3.5 Pro** appeared at I/O with **no benchmark, price, or model card** — a tell it wasn't ready. Google keeps cadence with **Flash/Lite/image** releases (Nano Banana 2 Lite, Gemini Omni Flash) [[Google launches Nano Banana 2 Lite and Gemini Omni Flash]] while Pro slips. **Why the company acts this way:** DeepMind is under simultaneous pressure — a **talent drain to Anthropic/OpenAI** [[Nobel laureate John Jumper leaves DeepMind for Anthropic]], [[More DeepMind talent joins Anthropic from Google]], [[AI researchers continue to leave Google for Anthropic]] — and internal compute/priority competition. Shipping Flash on time preserves the "we ship" story and protects the cost-leadership position while the frontier model is de-risked. **(analysis)**

## [3] Novelty / value-add / traction
**What's genuinely new (2026-07-16):** first mainstream-financial confirmation the slip is now "months" (not weeks), employee-sourced, plus a **real market reaction** (~4–4.4% Alphabet drop, ~$200B market cap). **What is NOT new / unconfirmed:** the delay itself (known since June), the rumored "July 17" relaunch, "2M-token context," a "full architectural rebuild / scrapped base model," a "third missed deadline," and leaked benchmarks (two leaks contradict — one says it beats Fable 5 on frontend/SVG, another says it trails Fable 5 and GPT-5.6 on reasoning/coding). **Traction, not announcements:** the only hard, verifiable datapoint is the stock move; everything about the model's capability is leak/speculation until an official model card + benchmarks ship. **Who captures the margin:** if Pro keeps slipping, enterprise coding/agentic spend flows to Anthropic/OpenAI rails now, and switching cost rises — a slip is not neutral, it's share leakage. **(analysis)**

## [4] What's next / market sentiment
- **Alphabet −4–4.4% on 2026-07-16** (~$200B erased); AI-leadership is core to the valuation thesis, so a flagship slip + rising capex draws execution-credibility scrutiny.
- **Base case:** further slip into **late-July/August**; near-term **Flash-tier stopgaps** (rumored 3.6 Flash / 3.5 Flash Lite) to keep cadence.
- **Confirmation trigger:** an official Google launch post with **model card + published benchmarks + pricing** — until then discount all capability claims.
- **Counterintuitive second-order:** a rushed ship to answer the narrative would risk shipping the very reliability/coding weaknesses that caused the delay — worse than slipping again. The real question shifts from "when does Pro ship" to **"can DeepMind still out-execute on the frontier while bleeding its top researchers, or does its edge narrow to cost-efficient Flash + distribution (now under EU attack)?"** **(analysis / hypothesis)**

## Sources
- Bloomberg, "Google Gemini launch delayed…" (2026-07-16)
- CNBC / Benzinga / ts2.tech (Alphabet −4%, ~$200B) (2026-07-16)
- 9to5Google, Android Authority (Google response) (2026-07-16)
- Corpus: DeepMind talent exodus, Grok 4.5, Fable 5, EU Android ruling, Nano Banana 2 Lite (see wikilinks)
- Tech-blog leak layer (July 17 date, rebuild, benchmarks) — flagged unverified
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
1. **Is "again" a genuinely new delay or a re-report?** → Re-report/amplification. The delay was known since the missed June target; the 2026-07-16 catalyst is Bloomberg's confirmation + market reaction, not a fresh slip event. Still FRESH here because no prior vault note covers it.
2. **Did Google officially announce a delay?** → No — Google disputes the framing on-record; the slip is inferred from a missed June target + the Bloomberg leak. Open on exact official date.
3. **How many slips are actually confirmed?** → One well-sourced (June → July+). "Second"/"third missed deadline" are blog-reported only. Open.
4. **Was "July 17" ever an official relaunch date?** → No — unnamed sources / tech blogs only.
5. **Official stated reason — safety, compute, or benchmarks?** → Coding capability below internal bar + a late-June retraining pass that fell short. Safety/compute/alignment are unstated or speculative for the Pro delay.
6. **Is "months behind" independently verified?** → Sourced to Bloomberg (~10 employees), not independently confirmed; plausible given the June→mid-July gap. Partly open.
7. **Are the leaked benchmarks trustworthy?** → No — two leaks directly contradict each other; no reproducible data; no Google/Anthropic comment.
8. **Did the stock really drop on THIS?** → ~4–4.4% on 2026-07-16, but same-week rival launches (GPT-5.6, Grok 4.5, Fable 5) + capex fears + the EU Android ruling are confounders. Attribution isn't clean.
9. **$200B vs $225B market-cap loss?** → Use ~$200B (CNBC/ts2); $225B is a lower-tier blog figure. Open.
10. **Is the "full architectural rebuild / scrapped base model" real?** → Open — only tech blogs. Bloomberg said retraining data was updated, not the model scrapped.
11. **Is the DeepMind talent exodus causally linked to the delay?** → Open. Corpus confirms Shazeer→OpenAI and Jumper/Adler/Pritzel→Anthropic, but causation to the slip is asserted, not established.
12. **Are competitors actually ahead on coding?** → Directionally supported (Fable 5 topped coding benchmarks; GPT-5.6 shipped; Grok 4.5 released), but "ahead" is benchmark/task-dependent and partly vendor-framed.
13. **Could the "third deadline miss" be blog inflation of one event?** → Likely yes — rapid same-day re-reporting around the Bloomberg drop suggests amplification, not three independently-verified misses.
14. **How much does this matter for fintech specifically?** → Indirectly: Google's agentic-commerce/payments push (AP2, Wallet, agentic shopping) depends on a credible frontier model; a slipping flagship weakens that pitch vs Anthropic/OpenAI-powered rivals. Open on magnitude.
15. **What would confirm resolution?** → An official Google launch post with a model card + published benchmarks + pricing. None exists as of 2026-07-17 — base case is a further slip into late-July/August.

Importance: 4/5 — A major Google flagship slipping while the DeepMind org bleeds top researchers (Shazeer/Jumper/Adler/Pritzel) and rivals ship a frontier cluster the same week is a genuine strategic signal, with a real ~$200B market reaction. Docked from 5 because the "delay" itself is a re-report of a June-known slip, the reason is coding-not-catastrophe, Google disputes the framing, and most sensational specifics (rebuild, July 17, benchmarks, third miss) are unverified.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Frontier-model race — closed general-purpose LLMs sold via API + first-party apps + cloud/enterprise. Not a disclosed-TAM market here, so "no data" on size; the sizing that matters is capex intensity: Alphabet raised FY26 capex guidance to **$180–190bn** (from $175–185bn), roughly double 2025's $91.4bn, with Q1'26 spend of **$35.7bn (+107% YoY)** and a signal that FY27 goes "meaningfully" higher (per Alphabet Q1'26 release/call). Structure is a consolidating oligopoly at the frontier (OpenAI, Anthropic, Google, xAI, Meta, plus Chinese labs Z.ai/DeepSeek/Moonshot/ByteDance) — barriers are capital (multi-$10bn compute), scarce researcher talent, and data/distribution, not IP. Drivers/why-now: (1) release cadence has become the competitive metric itself — Google shipped 3.5 Flash but its Pro tier stalled ~5 months after 3.1 Pro; (2) talent is the binding constraint — Gemini co-lead Noam Shazeer and other senior researchers left GDM for OpenAI/Anthropic, a second-order tax on velocity. Google's own monetization is *not* stalling: Google Cloud grew **+63% YoY to $20.0bn** in Q1'26 with backlog ~$460bn, and Search advertising grew **+19% to $60.4bn** even under AI Overviews — so the delay is a leadership/competitive-optics problem, not (yet) a revenue problem (per Alphabet Q1'26 disclosures).

**Competitive landscape.** KPIs the frontier runs on: benchmark standing (LMArena Elo, coding/reasoning suites), release cadence/recency, API price-per-token, and API/enterprise adoption. Basis of competition = capability-per-dollar + distribution, not price alone. Recent moves: Gemini 3.5 Pro missed successive targets (June → mid-July), reportedly after GDM scrapped a near-ready model for a ground-up rebuild on a native Gemini-3 foundation, with hallucination/tool-calling issues still open and prediction markets pricing a slip into late-July/August (per TechTimes/BigGo, Jul 2026 — third-party reporting, treat as directional). Google's position: a fast-follower slipping to laggard *in the public Pro tier specifically* — the note's own claim is GDM's public models now sit behind Anthropic, OpenAI, Meta, xAI, Z.ai and Moonshot. Caveat (analysis): benchmark leadership rotates by category and Google still fields competitive lower tiers (Flash, Nano Banana, Omni Flash) and owns unmatched distribution (Search, Android, Cloud) — the moat is distribution + custom TPU compute, not a single model's ranking.

**Comps & multiples.** No trading multiple computed: Alphabet is a diversified ad/cloud conglomerate, not a pure-play frontier-lab, so an EV/Revenue on the AI unit isn't derivable — the private labs (OpenAI, Anthropic, xAI) trade on last-round post-money, not market cap, and those aren't in the note; comparison stays qualitative. Internal comps from the base (frontier-model cadence / Google-AI competitive pressure): [[EU forces Google to give Gemini rivals equal Android access]] (distribution moat under regulatory pressure), [[Google launches Nano Banana 2 Lite and Gemini Omni Flash]] (Google's lower-tier cadence still shipping), [[Linas Newsletter GLM-5.2 ships 1M-token context amid Claude export ban]] and [[OpenAI announces GPT-Red model for automated red-teaming]] (rivals' shipping velocity), [[Barret Zoph rejoins OpenAI as VP after Thinking Machines exit]] (the talent-flow dynamic cutting the other way). Distribution/qualitative flag: in-line — the delay is a relative-position slip, not a valuation event.

**Risk flags.**
1. **Talent exodus → compounding velocity loss.** Losing a Gemini co-lead and senior researchers to direct rivals isn't a one-off; frontier progress is researcher-bound, so departures both slow Google and speed OpenAI/Anthropic — a two-sided second-order hit that a $180bn+ capex budget can't buy back quickly.
2. **Cadence/perception risk into a capex ramp.** Google is spending toward ~$185bn/yr partly justified by frontier leadership; a Pro tier that slips repeatedly widens the gap between spend and shipped capability, pressuring the AI-monetization narrative even while Cloud/Search numbers stay strong.
3. **Distribution moat is under regulatory attack.** Google's fallback advantage — bundling Gemini through Android/Search — is exactly what the EU is forcing open ([[EU forces Google to give Gemini rivals equal Android access]]); if the model isn't best-in-class *and* the distribution edge is diluted, the two legs of the thesis weaken together.

**What this changes (idea-lens).** (analysis) This is a competitive-slippage story, not a re-rating — Cloud +63% and Search +19% mean the market can forgive a late model as long as enterprise demand and ad monetization hold. Falsifiable thesis: if Gemini 3.5 Pro ships by end-Aug'26 and lands top-tier on independent benchmarks, the "Google is behind" narrative resets and the capex looks vindicated; if it slips into Q4 or launches mid-pack, expect scrutiny on capex ROI and further talent attrition. Trigger to watch: the actual launch date + first independent LMArena/coding-benchmark placement, and whether more GDM researchers depart.

Sources: https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/ · https://www.cnbc.com/2026/04/29/alphabet-googl-q1-2026-earnings.html · https://ppc.land/alphabet-q1-2026-google-network-ad-revenue-falls-4-as-ai-reshapes-the-web/ · https://www.techtimes.com/articles/320736/20260716/rebuilt-gemini-35-pro-misses-third-deadline-google-eyes-stopgap-release.htm · https://finance.biggo.com/news/6f0c6bb2-795f-4c57-9d09-6db691d7638a · https://startupfortune.com/google-delays-gemini-35-pro-to-july-as-talent-exodus-deepens-the-pressure-on-its-ai-ambitions/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
