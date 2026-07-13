---
title: "Alibaba reportedly bans employees from using Claude Code"
date: 2026-07-05
retrieved: 2026-07-05
tags:
  - company/alibaba
  - company/anthropic
  - industry/ai
  - region/asia
  - type/product
sources:
  - https://link.techcrunch.com/click/46421576.46192/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA3LzA0L2FsaWJhYmEtcmVwb3J0ZWRseS1iYW5zLWVtcGxveWVlcy1mcm9tLXVzaW5nLWNsYXVkZS1jb2RlP3V0bV9jYW1wYWlnbj1kYWlseV93ZWVrZW5k/6a347703be04c47cab07526aBbf379ffe
status: published
n_mentions: 1
channels:
  - "TechCrunch"
story_id: s7bfcb534
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Alibaba reportedly bans employees from using Claude Code

> [!info] 2026-07-05 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: TechCrunch

## Агрегированный текст (из дайджестов)

[TechCrunch] Alibaba reportedly bans employees from using Claude Code: Alibaba has reportedly classified Claude Code as high-risk software. Read More

## Первоисточники

### link.techcrunch.com
<https://link.techcrunch.com/click/46421576.46192/aHR0cHM6Ly90ZWNoY3J1bmNoLmNvbS8yMDI2LzA3LzA0L2FsaWJhYmEtcmVwb3J0ZWRseS1iYW5zLWVtcGxveWVlcy1mcm9tLXVzaW5nLWNsYXVkZS1jb2RlP3V0bV9jYW1wYWlnbj1kYWlseV93ZWVrZW5k/6a347703be04c47cab07526aBbf379ffe>
*326 слов · direct*

Posted:

 
 
 Anthony Ha 
Alibaba reportedly bans employees from using Claude Code
China’s Alibaba will ban employees from using Anthropic’s programming tool Claude Code, starting on July 10, according to multiple reports . 
Anthropic already prohibits Chinese companies, as well as foreign entities owned by those companies, from using its models. The company has reportedly been working to close loopholes that allow Chinese users to access Claude.
According to a recent Reddit post , some of that loophole-closing involved a version of Claude Code that could secretly identify Chinese users. Anthropic’s Thariq Shihipar said in a post on X that this was “an experiment we launched in March that was meant to prevent account abuse from unauthorized resellers and protect against distillation.” ( Distillation is a practice where AI models are trained on the outputs of other models.)
“The team has landed stronger mitigations since then and we’ve actually been meaning to take this down for a while,” Shihipar said.
Nonetheless, Alibaba has reportedly classified Claude Code as high-risk software and is instructing employees to use the company’s own Qoder tool instead.
Topics
 Last chance to save up to $190 on TechCrunch Founder Summit. Join 1,000+ founders and VCs at all stages for real-world scaling insights and connections that move the needle. Savings end June 26, 11:59 p.m. PT .
Newsletters
Subscribe for the industry’s biggest tech news
Related

 

 
 

 
 
 

 
 
 
 
 Media & Entertainment 
 
 
 

 
 New Google commercial imagines a Declaration of Independence written with help from AI 
 
 
 
 
 
 Anthony Ha 

 

 
 

 
 
 

 
 
 
 
 AI 
 
 
 

 
 Midjourney wants Hollywood studios to reveal the details of their AI usage 
 
 
 
 
 
 Anthony Ha 

 

 
 

 
 
 

 
 
 
 
 AI 
 
 
 

 
 The only AI glossary you’ll need this year 
 
 
 
 
 
 Natasha Lomas 
 Romain Dillet 
 Kyle Wiggers 
 Lucas Ropek 
Latest in AI

 

 
 

 
 
 

 
 
 
 
 Media & Entertainment 
 
 
 

 
 New Google commercial imagines a Declaration of Independence written with help from AI 
 
 
 
 
 
 Anthony Ha 

 

 
 

 
 
 

 
 
 
 
 AI 
 
 
 

 
 Midjourney wants Hollywood studios to reveal the details of their AI usage 
 
 
 
 
 
 Anthony Ha 

 

 
 

 
 
 

 
 
 
 
 In Brief 
 
 
 

 
 
 
 Alibaba reportedly bans employees from using Claude Code 
 
 
 
 
 
 Anthony Ha

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Alibaba reportedly bans employees from using Claude Code
_Analytical notes (not a post). Importance: 3/5._

**Freshness: FRESH.** No prior note covers this ban. It is, however, the direct retaliation-leg of the feud already logged in [[Anthropic accuses Alibaba of stealing Claude]] (2026-06-22) — treat those two as one escalating storyline, not duplicates.

## [0] What exactly happened (de-PR'd)
- Alibaba issued an internal directive classifying Anthropic's **Claude Code** (and, per some reports, all Anthropic products incl. Sonnet/Opus/Fable) as **"high-risk software,"** ordering employees to uninstall it and switch to Alibaba's own **Qoder** by **July 10, 2026**. Reported ~July 3 by **The Information** + **Reuters**, then TechCrunch July 4.
- **Sourcing reality:** every outlet traces to ONE leaked internal notice. There is **no public Alibaba statement**. So the ban, the July-10 date, the "high-risk" label and the Qoder-switch order are all "reported, single-source-origin" — widely reprinted, not independently multi-sourced. (analysis) The story is real but its precision is borrowed from one document.
- **Why framed this way / what it reveals:** the trigger is a Reddit-surfaced finding that a Claude Code build could **covertly identify Chinese users** (timezone `Asia/Shanghai`/`Asia/Urumqi` checks, keyword scan for Alibaba/ByteDance/Baidu, allegedly via steganographic system-prompt payload in ~v2.1.91). Anthropic's Thariq Shihipar confirmed **an experiment existed** (launched March 2026, to stop reseller abuse + **distillation**), said stronger mitigations shipped and it was slated for removal in the July 1 release. So: Anthropic frames it as **anti-abuse hygiene**; Alibaba frames it as a **backdoor**. The exact technical specifics (version, steganography) are reverse-engineering claims from secondary press — PLAUSIBLE, not Anthropic-confirmed.
- **The real spine (de-PR'd):** this is not a neutral "security review." It is a **tit-for-tat** in the distillation feud — Anthropic's June 10 Senate letter accused Alibaba's Qwen lab of running the "largest known distillation attack" (~25,000 fake accounts, >28.8M Claude exchanges, Apr 22–Jun 5, 2026) → the ban lands ~3–4 weeks later. → why it matters: the "high-risk" label is doing double duty as **retaliation + a forcing function to migrate staff onto Qoder**.

## [1] Competitors / peers
- **Replacement — Qoder (Alibaba):** agentic coding platform, global preview **Aug 21 2025**, Qoder 1.0 ~May 15 2026; **>5M users** claimed by mid-2026. Backed by **Qwen-Coder-Qoder** (Feb 3 2026), a model trained end-to-end inside the live product; Alibaba's own benchmark: **60.51%** task-resolution vs **Claude Opus 4.5 at 64.86%** (vendor claim — Alibaba trails its own comparison, notable that they still publish it).
- **Homegrown-tool wave:** Z.ai's **ZCode** (self-hostable, MIT weights) explicitly pitches "no regulatory kill-switch risk" vs Cursor/Claude Code/Copilot. Same playbook as Qoder.
- **Prior art on banning FOREIGN coding tools is thin:** no confirmed report of a major Chinese firm formally banning Cursor/Copilot/Windsurf on security grounds — access friction exists (geo/licensing) but a documented *corporate security ban* is new here. (analysis) So Alibaba is somewhat setting precedent, not following one.
- **Position:** on the model, Qoder is at parity-minus vs Claude; on **control/sovereignty** it wins by definition. → why: for a firm on the Pentagon's Chinese-military list ([[Pentagon adds Alibaba and Baidu to Chinese military companies list]]) and already blocked by Anthropic's own policy, the coding tool that "won't phone a US server" beats the marginally-better one.

## [2] Company history / fit
- Alibaba has been on a **full-stack Qwen self-sufficiency** march: Qwen >1B cumulative HF downloads by Mar 2026, >50% of global open-source model downloads (SCMP), plus product pushes like [[Alibaba launches Accio Work agentic AI tool for SMEs]]. The ban fits perfectly: it converts an external security scare into **internal Qoder adoption**.
- Structural pressure driving it: Anthropic's **Sept 4 2025 ownership ban** (>50% China-owned entities prohibited) already fenced Alibaba out of legitimate Claude access → any continued use is via loopholes Anthropic is now closing (ID + selfie verification, per FT). → so Alibaba had a **latent dependency on a tool it can't legally buy**; the "backdoor" story gave it the pretext to sever cleanly and dogfood Qoder.

## [3] Novelty / value-add / traction
- **What's genuinely new:** a named Chinese tech giant issuing a **formal internal ban** of a specific US AI coding agent, tied to an alleged covert user-detection mechanism. That combination (covert detection story + retaliation-in-a-distillation-feud + forced migration) is the fresh element vs the already-logged accusation note.
- **Traction that's real:** Qoder's >5M users and the internal-mandate migration are concrete; the ban gives Qoder a captive install base of ~124k–131k employees. → who captures the margin: Alibaba internalizes the coding-agent spend (no US vendor rent) AND gets **RL signal from real internal repos** feeding Qwen-Coder — a compounding data moat. → what breaks it: if Qoder materially lags on capability, forced migration = a productivity tax; the 60.51 vs 64.86 gap is the risk.
- **For Anthropic:** near-zero *direct* revenue hit (China enterprise already closed by its own policy). The real cost is **reputational** — the "covert detection" narrative drove a global developer backlash on Reddit/X, not just in China. (analysis) The margin question for Anthropic isn't China revenue (there is ~none) but **trust among its Western dev base**.

## [4] What's next / market sentiment
- **Escalation trajectory:** US side — Anthropic tightening loophole enforcement (FT), plus a reported **Hagerty (R-TN)/Kim (D-NJ)** defense-bill amendment to sanction distillation-running entities (pending). China side — ban + Qoder promotion. Analysts read it as **bifurcation of AI infra along geopolitical lines**, mirroring [[US drops export restrictions on Anthropic's Mythos and Fable]] (loosening one way, decoupling another).
- **Counterintuitive second-order (analysis):** the ban *helps* Alibaba more than it hurts Anthropic — it hands Alibaba a clean sovereignty narrative and a migration forcing-function, while Anthropic loses a market it had already exited. The louder second-order risk for Anthropic is that the covert-detection story **normalizes "US AI tools spy on you"** globally, aiding self-hostable rivals (ZCode, Qwen) everywhere, not just China.
- **Risks/unknowns:** no Alibaba confirmation; July-10 date single-sourced; technical backdoor specifics unverified by Anthropic.

## Sources
- TechCrunch (2026-07-04): https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/
- The Information: https://www.theinformation.com/briefings/alibaba-bans-employees-using-claude
- Reuters via Yahoo: https://finance.yahoo.com/technology/ai/articles/alibaba-ban-claude-code-workplace-065029852.html
- SCMP: https://www.scmp.com/tech/big-tech/article/3359375/
- Tom's Hardware: https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens
- The Decoder: https://the-decoder.com/claude-codes-complicated-china-problem-involves-bans-on-both-sides-of-the-pacific/
- Anthropic policy (2025-09-04): https://www.anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions
- MLQ (detection removal): https://mlq.ai/news/anthropic-removes-hidden-code-from-claude-code-that-covertly-flagged-chinese-users/
- Reddit r/ClaudeAI: https://www.reddit.com/r/ClaudeAI/comments/1ujila1/
- Shihipar (X): https://x.com/trq212/status/2072079729331777817
- Qoder / Qwen-Coder-Qoder: https://finance.yahoo.com/news/alibaba-launches-qoder-agentic-coding-133000732.html ; https://www.accessnewswire.com/newsroom/en/business-and-professional-services/alibaba-launches-a-large-model-trained-inside-a-coding-platform-1132940
- Distillation letter: https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm
- ZCode: https://venturebeat.com/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding
- Related internal notes: [[Anthropic accuses Alibaba of stealing Claude]], [[Pentagon adds Alibaba and Baidu to Chinese military companies list]], [[Alibaba launches Accio Work agentic AI tool for SMEs]], [[US drops export restrictions on Anthropic's Mythos and Fable]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / second-order questions

1. **Is this a new event or a re-report of the June distillation accusation?** New. The June 22 note [[Anthropic accuses Alibaba of stealing Claude]] is Anthropic→Alibaba (theft claim); THIS is Alibaba→Anthropic (retaliatory ban + tool migration). Same feud, distinct move → FRESH.

2. **Did Alibaba actually confirm the ban?** No. Every source traces to one leaked internal directive; no Alibaba public statement. Confidence in the *event* is high (many outlets), in the *details* (July 10, exact wording) medium.

3. **Is the July 10 enforcement date multi-sourced?** Reported consistently but all trace to the same leaked notice — treat as "reported/consistent," not independently verified. Open on independent confirmation.

4. **Did Anthropic really put a covert China-detection mechanism in Claude Code?** Anthropic (Shihipar) CONFIRMED *an experiment* existed (March 2026, anti-abuse/anti-distillation) and was being removed. The specific mechanics (v2.1.91, timezone strings, steganographic payload) are reverse-engineering claims from secondary press — PLAUSIBLE, not Anthropic-validated. Open on exact mechanism.

5. **How much revenue does Anthropic actually lose from this ban?** Near zero directly — Chinese enterprises were already prohibited by Anthropic's own Sept 2025 ownership policy. The cost is reputational/trust, not China ARR. Answered.

6. **Is Qoder good enough to replace Claude Code, or is this a productivity tax on staff?** Alibaba's OWN benchmark puts Qoder at 60.51% vs Claude Opus 4.5's 64.86% — trailing. So for capability-sensitive work the mandate imposes a real (if modest) tax. Open on independent benchmarks.

7. **Who benefits more — does the ban hurt Anthropic or help Alibaba?** Asymmetric: helps Alibaba more (clean sovereignty narrative + forced Qoder adoption + RL data from internal repos) than it hurts Anthropic (a market it had already exited). Answered (analysis).

8. **What's the real second-order risk for Anthropic?** Normalizing "US AI tools covertly track you" globally — aiding self-hostable rivals (ZCode, Qwen-based tools) in ALL regions, not just China. This shifts the central question from "China revenue" to "Western developer trust." Answered (analysis).

9. **Is there prior art of Chinese firms banning foreign coding tools?** No confirmed formal security ban of Cursor/Copilot/Windsurf surfaced — access friction is geo/licensing, not documented corporate bans. So Alibaba is closer to setting precedent. Open (absence of evidence).

10. **Is the distillation accusation itself proven?** No — it's Anthropic's claim in a Senate letter (~25k accounts, >28.8M exchanges, Apr 22–Jun 5). Numbers are Anthropic's, unadjudicated. Open.

11. **Does the ban cover all Anthropic products or just Claude Code?** Reports vary: some say Claude Code specifically, others "all Anthropic products incl. Sonnet/Opus/Fable." Open — matters for the "high-risk" framing scope.

12. **Could this be internal Alibaba security-team caution rather than top-down geopolitics?** Plausible both — a genuine security review CAN reach "high-risk" independently of the feud, but the timing (weeks after the Senate letter) makes retaliation the dominant read. Open on internal motive.

13. **What's the regulatory next step?** Reported Hagerty(R-TN)/Kim(D-NJ) defense-bill amendment to sanction distillation-runners — pending, not passed. Open.

14. **Does this accelerate China AI-coding self-sufficiency measurably?** Directionally yes (forced ~124k–131k-employee Qoder base + RL signal into Qwen-Coder), but no post-ban adoption metric yet. Open.

15. **Fresh or stale for the digest?** FRESH — a distinct escalation move with its own facts (ban, July 10, Qoder mandate, covert-detection trigger) not previously logged.

**Importance: 3/5** — A real, well-corroborated escalation in the marquee US–China AI-decoupling story with concrete stakes (forced migration of a giant's dev org, sovereignty precedent, Anthropic reputational hit). Capped below 4 because: single-leak sourcing with no Alibaba confirmation, minimal direct financial impact (Anthropic already exited China), and it is one leg of an already-covered feud rather than a standalone market-moving event. Above 2 because of geopolitical weight and the covert-detection angle's broad reputational spillover.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-06]] (2026-07-06).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits at the crossroads of the AI coding-tool market and China AI sovereignty. Market size: the AI code-assistant market is put at ~$10.3bn in 2026 (up from ~$8.5bn 2025), with the enterprise coding-agent slice estimated at ~$9.8–11.0bn annualized as of Apr 2026 (per Grand View / Gartner-cited figures, via ideaplan.io & getpanto.ai — third-party analyst estimates, ranges vary widely, treat as directional, not audited). Growth is fast (~65% YoY 2025–26 cited; 85% of developers reported using AI coding tools). Structure: consolidating around a few Western stacks — GitHub Copilot (~4.7m paid subs Jan 2026), Cursor, and Claude Code (46% "most-loved," JetBrains Apr 2026 survey) — but bifurcating along a geopolitical seam. Entry barriers: frontier-model access + distribution; for China the *binding* barrier is now regulatory/access, not capability. Why now: Anthropic's Sept 2025 ownership ban already fenced >50%-China-owned firms out of legitimate Claude access, and the June 2026 distillation feud ([[Anthropic accuses Alibaba of stealing Claude]]) converted a latent dependency into a forced-migration trigger. → second-order: the market is splitting into a US-vendor track and a China-sovereign track, each with its own tools.

**Competitive landscape.** Sector KPIs: seats/paid subscribers, task-resolution rate (SWE-bench-style), and annualized revenue run-rate. Key players & basis of competition — Western: Copilot (distribution/scale), Cursor (product/UX), Claude Code (model capability); China-sovereign: Alibaba's **Qoder** (>5m users claimed mid-2026), Z.ai's ZCode (self-hostable, MIT weights). Basis of competition splits: capability in the West, control/sovereignty in China. Recent moves: Qwen-Coder-Qoder released Feb 3 2026 (trained end-to-end inside the product); Qwen-based coding models >20m downloads; Tongyi Lingma >3bn lines of code since Jun 2024 (Alibaba Cloud / Yahoo Finance, various 2026). Protagonist position: on capability Qoder is **catching up** (Alibaba's own benchmark 60.51% vs Claude Opus 4.5 64.86% — trailing by its own yardstick); on sovereignty it wins by definition. Moat (analysis): a data/scale moat — forcing ~124k–131k employees onto Qoder yields RL signal from real internal repos feeding Qwen-Coder, compounding over time. That moat is control- and data-based, not capability-based today.

**Comps & multiples.** No market-cap multiple applies to the ban itself (no deal/round). Peer economics for scale context: **Anthropic** — annualized revenue ~$47bn (May 2026, up from $9bn end-2025); confidential IPO filing Jun 1 2026 at ~$965bn valuation → P/S ≈ `$965bn / $47bn = 20.5x` (VentureBeat/Simon Willison/Sacra — run-rate not GAAP, so this is a rich, growth-justified multiple, not a clean trailing P/S; mark `[UNSOURCED]` on any margin/EBITDA). **Claude Code** specifically: ~$2.5bn annualized (Feb 2026), >half enterprise — the product Alibaba is banning is a fast-doubling line for Anthropic, but its China exposure is ~nil (already policy-excluded). Alibaba IR grounding (real reported figures, FY ends Mar 31): Cloud Intelligence Group revenue **RMB41,626m (US$6,035m) in the Mar-2026 quarter, +38% YoY**, external-customer revenue **+40%**; **AI-related product revenue RMB8,971m, 11th consecutive quarter of triple-digit YoY growth**; **FY2026 Cloud revenue RMB158,132m (US$22,924m), +34%** (Alibaba Mar-quarter FY2026 earnings release & 20-F, 2026-05-13/20). Internal comps: [[Anthropic accuses Alibaba of stealing Claude]] (the theft-claim leg of the same feud); [[Ant Group releases Ling-1T AI model]] (China code-capable model wave); [[Coinbase CEO pressures staff to adopt AI tools]] (enterprise coding-tool mandate precedent, opposite direction). Distribution not computed — no ≥3 comparable public multiples; qualitative comparison only.

**Risk flags.**
1. **Single-source event risk.** Ban, July-10 date, "high-risk" label and Qoder mandate all trace to ONE leaked internal notice — no Alibaba statement. → if the directive is narrower/softer than reported, the "forced-migration moat" thesis is overstated.
2. **Capability/productivity tax.** Qoder trails Claude on Alibaba's *own* benchmark (60.51% vs 64.86%). → mandating a weaker tool on ~124k+ engineers risks a real (if modest) productivity drag until Qoder closes the gap.
3. **Reputational spillover for Anthropic (not revenue).** China ARR is already ~zero; the actual risk is the "US AI tools covertly track you" narrative normalizing globally, aiding self-hostable rivals (ZCode, Qwen) in *all* regions → erosion of Western developer trust, the metric that actually matters for Anthropic.

**What this changes (idea-lens).** (analysis) This accelerates a two-track AI-coding market: a US-vendor stack and a China-sovereign stack, each self-reinforcing. Falsifiable thesis: forced Qoder adoption + internal-repo RL signal narrows the Qoder–Claude capability gap within ~2–3 quarters. Trigger/watch: an *independent* (non-vendor) benchmark showing Qoder ≥ Claude on SWE-style tasks, and any post-ban Qoder adoption/retention metric. What breaks the thesis: Alibaba engineers routing around the ban, or Qoder churn back to Western tools once the sovereignty headline fades — would show the moat is narrative, not capability.

Sources: https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/baba-20260331.htm · https://drive.google.com/file/d/1L9dTLyVtKelIdtox_Cu1nErF_U61KBy_/view · https://drive.google.com/file/d/14VG-ISy4IUmqyA23TIX0RtLq5xlNTL87/view · https://www.ideaplan.io/blog/ai-coding-assistant-market-share-2026 · https://www.getpanto.ai/blog/anthropic-ai-statistics · https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth · https://simonwillison.net/2026/May/29/anthropic/ · https://finance.yahoo.com/news/alibaba-launches-large-model-trained-120000343.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings review — earnings-reviewer layer on top of [0]–[4], not a recap. Primary source: Alibaba's OWN filings (March Quarter 2026 & FY2026 results, released 2026-05-13, period ended 2026-03-31). This note's event is a July 2026 corporate-security story with NO financials of its own; the review below anchors the Alibaba investment context to the most recent reported quarter (FY ends Mar 31). Figures are the company's reported numbers, not consensus.

**Verdict (headline read).** MIXED — revenue MISS, margins MISS, but the segment that matters here (AI + Cloud) BEAT. Group revenue RMB243,380m (US$35,283m), +3% YoY (+11% like-for-like ex-disposals of Sun Art/Intime) — below the ~US$35.5bn Street looked for. Non-GAAP net income collapsed to RMB86m (US$12m), -100% YoY, and the group swung to a **loss from operations of RMB848m** vs +RMB28,465m a year ago, as heavy AI/cloud capex + instant-commerce spend crushed profitability. Offsetting this: **Cloud Intelligence Group revenue RMB41,626m (US$6,035m), +38% YoY (external customers +40%)** with AI-related product revenue up triple-digits for the 11th straight quarter. Guidance: not a formal number, but management reaffirmed aggressive AI+Cloud investment. Relevance to THIS note: the Claude Code ban is a forcing-function to migrate staff onto Qoder — and the quarter shows Alibaba both accelerating its cloud/AI top line and eating a large near-term margin hit to do it.

**Key figures (with growth).**
- **Group revenue:** RMB243,380m (US$35,283m), +3% YoY vs RMB236,454m in Q Mar-2025; +11% on a like-for-like basis excluding disposed Sun Art & Intime.
- **Cloud Intelligence Group revenue:** RMB41,626m (US$6,035m), **+38% YoY** vs RMB30,127m in Q Mar-2025; external-customer revenue **+40% YoY** (accelerating from prior quarters — see trajectory below).
- **AI-related product revenue:** RMB8,971m in the quarter, **11th consecutive quarter of triple-digit YoY growth**; ~30% of external cloud revenue.
- **FY2026 (full year) Cloud Intelligence Group revenue:** RMB158,132m (US$22,924m), **+34% YoY** vs RMB118,028m in FY2025.
- **Operating result:** **Loss from operations RMB848m (US$123m)** vs income from operations RMB28,465m (12% margin) a year ago — a swing driven by the decrease in adjusted EBITA (AI-infrastructure + instant-commerce investment).
- **Non-GAAP net income:** RMB86m (US$12m), **-100% YoY** vs RMB29,847m in Q Mar-2025.
- **GAAP net income attributable to ordinary shareholders (basic):** RMB25,476m (US$3,693m) in Q Mar-2026 vs RMB12,382m a year ago — an *increase*, but driven by mark-to-market gains on equity investments, NOT operations (de-PR flag below).

**By segment / driver.** The quarter is a story of two engines pulling opposite ways. Cloud (+38%, external +40%) and AI (RMB8,971m, triple-digit for the 11th quarter) are the accelerating, thesis-relevant line — CEO Eddie Wu framed full-stack AI as moving "from incubation to commercialization at scale." The drag: "All others" segment revenue RMB65,459m, **-21% YoY**, mechanically from the Sun Art/Intime disposals; and a group-wide margin collapse as adjusted EBITA fell on AI-infrastructure buildout + a "Taobao Instant Commerce" push. So the top line disappointed on the mature/e-commerce side while the AI+Cloud side beat — exactly the mix that matters for the Qoder/Claude-Code storyline in this note.

**vs expectations / prior period.** Vs public consensus (as of ~2026-05-13, StockAnalysis/Yahoo/TipRanks aggregators): revenue ~US$34.57bn reported **missed** the ~US$35.5bn expected; non-GAAP diluted EPS ~US$2.06 **missed** the ~US$2.17 consensus. Yet BABA shares reportedly rallied (~+13% cited) on the cloud/AI re-rating — the market rewarded the +40% external-cloud acceleration and looked through the investment-driven margin hit. Prior-quarter Cloud trajectory (own filings): Q Mar-2025 +18% → Q Jun-2025 +26% → Q Sep-2025 +34% → Q Dec-2025 +36% → **Q Mar-2026 +38%** — clean sequential acceleration for five quarters. See related [[Anthropic accuses Alibaba of stealing Claude]] (same feud, June 2026).

**Guidance / forward.** No formal revenue/EPS guidance number given. Management (Eddie Wu, CEO; Toby Xu, CFO) reaffirmed intent to "continue to invest in AI + Cloud to strengthen our competitive advantages" — i.e., margins stay pressured near-term by choice. Tone: confident on cloud/AI commercialization, explicitly transparent that profitability was sacrificed for infrastructure + instant-commerce investment. What they emphasized: cloud acceleration, AI-product monetization, Qwen integration into consumer apps. What's underplayed: the depth of the operating-loss swing and that headline GAAP net income rose only because of investment mark-to-market gains, not the core business.

**Thesis-flags.**
1. **Cloud/AI acceleration is real and self-funded (bull).** External cloud +40% and AI revenue triple-digit for 11 quarters → why it matters: gives Alibaba the balance-sheet and demand case to force ~124k+ engineers off Claude Code onto Qoder (this note's event) without a capability cliff being commercially fatal. Second-order: internal Qoder adoption feeds RL signal into Qwen-Coder, compounding the same cloud/AI line that just accelerated.
2. **Profitability sacrificed by design (watch).** Loss from operations RMB848m vs +RMB28,465m; non-GAAP net income RMB86m (-100%) → why it matters: the AI-sovereignty push (of which the Claude Code ban is one leg) is expensive; if cloud growth decelerates before margins recover, the "invest-through-it" thesis breaks. Watch adjusted EBITA trajectory next quarter.
3. **Headline GAAP net income is flattered by investment gains, not operations (de-PR).** GAAP net income to shareholders rose to RMB25,476m largely on mark-to-market equity gains → don't read the higher GAAP number as operational strength; the operating loss + non-GAAP wipeout are the true read.
4. **The ban has ~zero financial footprint in these numbers.** Claude Code was already policy-excluded from Alibaba (Anthropic's Sept-2025 ownership ban); the July-2026 ban changes Alibaba internal tooling, not its reported revenue or Anthropic's China ARR (~nil). The material line for this note is Cloud/Qoder capacity, which the quarter shows is accelerating.

Sources (primary = Alibaba's own filings): March Quarter 2026 investor presentation https://drive.google.com/file/d/14VG-ISy4IUmqyA23TIX0RtLq5xlNTL87/view · earnings release https://drive.google.com/file/d/1L9dTLyVtKelIdtox_Cu1nErF_U61KBy_/view · 6-K financials https://drive.google.com/file/d/1RyvZWSGOGKgDqU8eD_Ar5Nu-2dxvpy0K/view · EDGAR 20-F (FY2026, period 2026-03-31) https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/baba-20260331.htm · consensus/reaction (as of 2026-05-13): Nasdaq/Businesswire release https://www.nasdaq.com/press-release/alibaba-group-announces-march-quarter-2026-and-fiscal-year-2026-results ; 24/7 Wall St https://247wallst.com/companies/baba/earnings/2026/Q1 ; medium/tech-acc (stock +13% on miss) https://medium.com/techacc/alibabas-earnings-report-missed-so-why-did-the-stock-soar-13-df4300ae045d
<!-- /enrichment:earnings_review -->
