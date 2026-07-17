---
title: "Sunday Robotics unveils ACT-2 model for home robot Memo"
date: 2026-07-16
retrieved: 2026-07-17
tags:
  - company/sunday-robotics
  - industry/ai
  - region/us
  - type/product
sources:
  - https://substack.com/redirect/555872ab-72de-497a-a81d-9d8cb6856f25
  - https://substack.com/redirect/5f9962fc-98b4-494f-b271-778f012f3a57
  - https://substack.com/redirect/6b57fd98-a2f5-433a-8037-c439e6916a46
  - https://substack.com/redirect/2301046d-6672-4834-aaaa-a58db7cc4955
status: enriched
n_mentions: 4
channels:
  - "Not Boring"
story_id: s28005333
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Sunday Robotics unveils ACT-2 model for home robot Memo

> [!info] 2026-07-16 · 4 упоминаний · 0 источника(ов) с текстом
> Каналы: Not Boring

## Агрегированный текст (из дайджестов)

[Not Boring] (3) Don’t Forget About the Humanoids: Walden and Sunday

[Not Boring] The robots are built as a full stack: hardware, software, models, and an application layer for deploying them into real workflows, a la Standard Bots. They learn tasks through demonstrations, then improve through practice, starting with the annoying jobs in manufacturing and logistics that have remained hard to automate because they change too often or require a little too much judgment for traditional fixed automation.

[Not Boring] Yesterday, Sunday Robotics introduced ACT-2 Preview, its new robotics model for Memo, the company’s home robot. Sunday says ACT-2 can learn a new behavior from a single fine-tuning example, generalize it zero-shot to real homes it has never seen, and perform with a 99% success rate.

[Not Boring] It’s still a preview, but they got ahead of the slick demo criticism by introducing something called Solves. “Progress in robotics is difficult to measure because demos vary by setup. Demo ≠ Solved,” CEO Tony Zhao tweeted. “A Solve declares two boundaries: scope and adaptation cost. Without both, 99% has no context.”

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://substack.com/redirect/555872ab-72de-497a-a81d-9d8cb6856f25>
- <https://substack.com/redirect/5f9962fc-98b4-494f-b271-778f012f3a57>
- <https://substack.com/redirect/6b57fd98-a2f5-433a-8037-c439e6916a46>
- <https://substack.com/redirect/2301046d-6672-4834-aaaa-a58db7cc4955>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sunday Robotics unveils ACT-2 model for home robot Memo
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 2026-07-15/16 Sunday Robotics (Mountain View; ex-Stanford ALOHA / diffusion-policy team, founders Tony Zhao & Cheng Chi) released **ACT-2 Preview**, the next iteration of the foundation model that drives **Memo**, its wheeled at-home manipulation robot. Headline claims: learn a new behavior from **a single fine-tuning example**, generalize it **zero-shot** to unseen real homes, at a **99% success rate**.
- The one hard number behind "99%" is narrow and specific: the **"Laundry Solve" = 99.1% zero-shot success on laundry folding, 785 autonomous attempts across 31 unseen environments** (per sunday.ai/blog/act-2-preview). It is one task family, not general household competence.
- **Why framed this way — the "Solve" construct is the real story, not the number.** CEO Zhao pre-empted the "slick demo" critique by defining a **Solve = a declared (scope, adaptation-cost) pair**: "Demo ≠ Solved… without both boundaries, 99% has no context." This is a deliberate move to set an evaluation standard the field lacks — and, second-order, to make Sunday the one who defines the benchmark (a competitive/PR lever as much as a scientific one).
- **Still a Preview**, not a shipped capability on customer units. Memo itself is not yet in homes at scale (company targeted first autonomous units ~Thanksgiving 2026 in its March raise). So this is **announced capability on a declared task**, not deployed household autonomy.

## [1] Competitors / peers
Home/general manipulation foundation models, 2026:
- **Physical Intelligence (π0 → π0.7, Apr 2026)** — pure "robot brain," cross-embodiment, flow-matching action generation for contact-rich tasks like folding. Sunday's closest intellectual rival; PI is model-only, Sunday is **full-stack (hardware + model + glove data pipeline)**.
- **Figure Helix** — VLA for **humanoids**, whole-body control, industrial (BMW) — different form factor and market (factory, not home).
- **Google DeepMind Gemini Robotics-ER 1.6 (Apr 2026)** — spatial-reasoning "brain" licensed to partners (Boston Dynamics), not a consumer product.
- In-corpus adjacencies (all industrial/humanoid, not home manipulation): [[UK robotics startup Humanoid raises $150M Series A tranche]], [[Japan launches AI consortium Noetra for physical AI]], [[Forterra deploys 100+ autonomous ground vehicles in Ukraine]]; closest technical cousin is dexterous-hand work in [[Proception settles Tesla trade-secret suit, raises $11M]].
- **Position:** parity-to-ahead on the *specific* generalization-with-reliability claim, and unusually rigorous on measurement (the Solve). **Why the landscape splits this way:** PI/Gemini bet the brain generalizes across any body; Sunday bets that **owning the data (human-glove teleop, 500+ homes) + the body** is what buys reliability in the messy home — a data-moat thesis vs a model-scale thesis.

## [2] Company history / fit
Founded 2024; emerged from stealth Nov 2025 with **Memo + ACT-1** ("zero robot data" — trained on human motion via the ~$200 **Skill Capture Glove** across 500+ homes). Funding path: $35M (Benchmark, Conviction/Sarah Guo) → **$165M raise (Mar 2026, ~$1.15B valuation)**, ~$200M total, ~70+ engineers (Tesla/DeepMind/Waymo/Meta/OpenAI/Apple alumni). Backers also incl. Bain Capital Ventures. **Why this cadence:** ACT-1 was the "we can learn from humans" proof; ACT-2 is the **"it generalizes reliably" proof needed to justify shipping** — the structural pressure is that a $1.15B home-robot valuation demands evidence of reliability, not just viral clips, before a Thanksgiving ship date.

## [3] Novelty / value-add / traction
- **Genuinely new (as a claim):** unifying *broad generalization* with *high reliability* on a contact-rich task, plus a **published, falsifiable eval protocol (the Solve)** — the latter is arguably the more durable contribution than the 99.1% itself.
- **Traction is thin/announced, not adopted:** 785 lab-style attempts across 31 envs ≠ paying households; no live-customer, no GMV-equivalent. "Preview" + "zero-shot on laundry" is real but **narrow**. (analysis) The single-example fine-tuning claim is impressive but unverified beyond Sunday's own demos.
- **Where the margin/moat sits (analysis):** if the thesis holds, value accrues to whoever owns the **home-scale demonstration data** (Sunday's glove pipeline) — the model is commoditizing (PI/Gemini give away brains), so the defensible layer is proprietary real-home data + the integrated hardware. What breaks it: brain-only players proving embodiment-agnostic transfer removes Sunday's full-stack premium.

## [4] What's next / market sentiment
Roadmap: preview → broader task Solves → first autonomous Memo units to homes (targeted late-2026). Sentiment is hot (home robotics is a 2026 theme; $1.15B valuation pre-ship). **Risks / second-order:** (1) laundry-Solve is cherry-pickable — the field will demand Solves on messier, less structured chores; (2) safety/liability in occupied homes is unaddressed publicly; (3) **counterintuitive:** the more Sunday standardizes evaluation with "Solves," the more it invites competitors to beat it on *its own* scoreboard — a benchmark you publish is a benchmark others can top. (hypothesis) The central question is not "is 99% real" but "does full-stack + proprietary home data out-durable brain-only generalists once both ship."

## Sources
- sunday.ai/blog/act-2-preview ; sunday.ai/journal/no-robot-data (ACT-1)
- Not Boring digest (aggregated in note) — Zhao "Solve" tweet
- theaiinsider.tech / siliconangle (Nov 2025 stealth, $35M) ; globenewswire / robohorizon (Mar 2026 $165M, $1.15B) ; baincapitalventures.com ; founded.com ; sacra.com/c/sunday
- Competitors: blackscarab.ai (π0.7) ; mikekalil.com + Gemini Robotics-ER 1.6 ; marktechpost top-10 physical AI 2026 (Figure Helix)
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **"99%" scope.** The number is 99.1% on *laundry folding only* (785 attempts / 31 envs). Does any other chore have a published Solve, or is one task standing in for "household competence"? — **open / narrow.**
2. **Solve independence.** The 31 "unseen" environments and 785 attempts are Sunday-run and Sunday-scored. Is there any third-party or adversarial evaluation? — **open (self-reported).**
3. **Single-example fine-tuning.** How robust is "learn from one example" — one example per task, per object, per home? What is the failure distribution outside the demoed behaviors? — **open, unverified beyond Sunday demos.**
4. **Preview vs shipped.** ACT-2 runs on lab/pilot Memo units, not units in paying homes. How many (if any) Memos are autonomously operating in real households today? — **~zero live; ship target late-2026.**
5. **Adaptation cost.** A Solve declares an "adaptation cost." What is ACT-2's actual per-home/per-task setup cost in time, teleop, or compute? — **not disclosed in the summary.**
6. **Data moat durability.** The thesis is proprietary human-glove data (500+ homes). Can PI/Gemini-style brain-only models close the reliability gap without that data, commoditizing Sunday's edge? — **open; core bear case.**
7. **Full-stack vs brain-only economics.** Sunday builds hardware + model + glove pipeline; PI ships only the brain. Which layer captures margin if home robots scale — the body, the brain, or the data? — **analysis; likely data+integration.**
8. **Safety/liability.** A wheeled manipulator operating unsupervised around people/pets/property — what is the safety record and who bears liability for damage or injury? — **not addressed publicly.**
9. **Benchmark boomerang.** By publishing the "Solve" standard, does Sunday hand competitors a scoreboard to beat it on? Is the standard defensible or a gift? — **counterintuitive risk (analysis).**
10. **Valuation vs traction.** $1.15B valuation pre-shipment on one Solved task — what real revenue/orders exist, or is this pure narrative pricing on a hot theme? — **narrative-priced; no revenue.**
11. **Generalization stress test.** Laundry is relatively structured/repetitive. Does ACT-2 hold on unstructured, high-judgment chores (dishes with clutter, spills, novel objects)? — **open; not demonstrated.**
12. **Competitive timeline.** π0.7 (Apr 2026), Gemini Robotics-ER 1.6 (Apr 2026), Figure Helix all advancing fast. Is ACT-2 ahead, at parity, or catching up on *home* manipulation specifically? — **parity-to-ahead on the specific reliability claim only.**
13. **Prior art on "zero robot data."** Learning from human video/teleop is not unique to Sunday. What exactly is novel in ACT-1/ACT-2 vs existing human-demo VLA work? — **the reliability+eval framing, not the data source.**
14. **Duplicate check.** Any prior vault note covering Sunday Robotics, Memo, or ACT-1/ACT-2? — **none; this is the first coverage (fresh).**
15. **Fintech relevance.** Why does a home-robot model matter to a fintech corpus — capital-markets/venture angle, or thematic "physical AI capex" only? — **venture/theme signal, not direct fintech.**

Importance: 3/5 — A technically credible, well-measured advance (the "Solve" eval discipline is the genuinely notable part) from a well-funded, pedigreed team, but the substance is a Preview on a single task family with zero live-in-home traction and a self-reported benchmark; adjacent-to-fintech (physical-AI venture theme) rather than core. Fresh, no prior coverage in the vault.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Home/consumer robotics sits inside the humanoid-robot market that most forecasters size at ~$2.9bn in 2025 rising to ~$15bn by 2030 (~39% CAGR, per MarketsandMarkets/Grand View via secondary citation, as of 2026); Morgan Stanley separately puts *China* humanoid shipments at 50k units / ~$2bn in 2026 → ~$15bn by 2030 (per MS note via CNBC, 2026-06-24) — see [[Morgan Stanley raises forecast for China humanoid robot market]]. These are top-down analyst TAMs, not bookings; near-term revenue is a rounding error (~$1.8bn in 2026 per secondary est.) and the home sub-segment barely exists in units. Structure: capital- and talent-intensive, still fragmented and pre-consolidation, splitting into a **software/foundation-model layer** (license the "brain" onto any body) vs a **full-stack hardware+model+deployment layer** — Sunday explicitly builds the full stack (hardware, software, model, application). Why now: the manipulation-model breakthrough (learn a task from demonstrations, generalize zero-shot) plus a wave of cheap capital (2025 robotics funding >$10bn per secondary est.) and a policy/industrial push (Japan's $2.4bn Noetra consortium, [[Japan launches AI consortium Noetra for physical AI]]).

**Competitive landscape.** Sector runs on (KPIs): task success rate / autonomy vs teleop share, generalization (zero-shot to unseen homes), unit cost/price, and deployment count — not revenue yet. Layers & players: (a) **foundation-model / "brain"** — Physical Intelligence (~$5.6bn val, reportedly raising at ~$11bn), Skild AI ($14bn val after a $1.4bn round, Jan 2026); (b) **full-stack humanoid** — Figure AI (~$39bn val), 1X (Neo home robot, $20k or $499/mo, US 2026), Tesla Optimus, plus [[UK robotics startup Humanoid raises $150M Series A tranche]] (~$1.2bn pre-money) and Boston Dynamics ([[Hyundai to buy SoftBank's remaining Boston Dynamics stake for $325M]]). Recent moves: Sunday raised a $165M Series B at **$1.15bn** post led by Coatue (2026-03-12, total ~$200M incl. $35M Nov 2025 from Benchmark/Conviction); Skild $1.4bn/$14bn (Jan 2026); Physical Intelligence reportedly raising ~$1bn (2026). Sunday's position: **niche/early full-stack home player**, well below the model-layer and Figure valuations; its differentiation is the **home** target (laundry, table-clearing) and the ACT-2 "Solve" framing (scope + adaptation cost) explicitly designed to rebut demo-inflation. Moat `(analysis)`: proprietary demonstration data + home deployment loop *if* Memo ships — thin today, since the model layer (PI/Skild) could commoditize the "brain" and 1X/Tesla out-scale the hardware.

**Comps & multiples.** Private, pre-revenue → valuations are round post-money, NOT market cap; revenue/EBITDA multiples = **no data** (no disclosed revenue). Comparison is qualitative on last-round valuation:
- Sunday: ~$1.15bn post (Series B, 2026-03) — *smallest / earliest* of the peer set.
- 1X: reportedly raising ~$10bn (home-robot direct comp).
- Figure AI: ~$39bn (full-stack, industrial-first).
- Physical Intelligence ~$5.6bn (→~$11bn reportedly); Skild ~$14bn (model-only).
- Internal round comps: [[UK robotics startup Humanoid raises $150M Series A tranche]] (~$1.2bn pre — closest by size/stage), [[TerraFirma raises $100M Series A led by Kleiner Perkins]] (construction robots, adjacent), [[Kindred Ventures raises $355 million for AI and robotics bets]].
Distribution not computed (valuations span $1.2bn–$39bn on non-comparable stage/model; no revenue to normalize). Flag: on a **funding-vs-progress** basis Sunday looks *cheap relative to hype peers* but that reflects earlier stage and no shipped product — cheapness here is stage risk, not a bargain.

**Risk flags.**
1. **Demo ≠ deployment.** ACT-2 is a *Preview*; the headline "99% success, single-example, zero-shot to unseen homes" is a company claim, unverified in independent field use. Sunday itself flags this ("Demo ≠ Solved") — credit for candor, but the burden of proof is a Beta shipping to real homes (targeted Thanksgiving 2026); slippage would re-rate the $1.15bn mark.
2. **Autonomy/safety in unstructured homes.** Homes have pets, children, fragile/private objects and changing layouts; first-gen home robots (incl. 1X Neo) lean on human teleop ("Expert Mode"). If Memo needs remote operators, the unit economics and privacy story break, and "autonomous" becomes marketing.
3. **Squeezed between layers + cost.** Model-layer peers (PI, Skild) can license a "brain" onto cheaper bodies, while 1X/Tesla push hardware toward $20k. A full-stack sub-scale player risks being out-modeled above and out-priced below; consumer price for Memo is undisclosed [UNSOURCED].

**What this changes (idea-lens).** `(analysis)` The ACT-2 "Solve" metric is an attempt to move the sector's scorecard from demo virality to falsifiable scope+adaptation-cost benchmarks — if it sticks, it's a modest re-rating for whoever can *prove* generalization, and a discount for demo-only names. Watch/trigger: the actual Thanksgiving-2026 Beta deliveries and any *independent* success-rate replication in real homes; the thesis is wrong if Memo ships broadly autonomous at the claimed 99% — or dead if the Beta slips or ships teleop-dependent.

Sources: https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/ · https://siliconangle.com/2026/03/12/sunday-raises-165m-1-15b-valuation-launch-memo-household-robot/ · https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation/ · https://app.dealroom.co/news/note/robot-ai-startup-physical-intelligence-seeks-1b-at-11b-valuation · https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html · https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html · https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
