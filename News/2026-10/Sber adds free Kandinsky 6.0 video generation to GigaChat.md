---
title: "Sber adds free Kandinsky 6.0 video generation to GigaChat"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/sber
  - company/gigachat
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.sberbank.ru/ru/sberpress/all/article
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sf3a21062
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# Sber adds free Kandinsky 6.0 video generation to GigaChat

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Добавил в ГигаЧат бесплатную генерацию видео длительностью до пяти секунд со звуком и разрешением до Full HD с помощью новой модели Kandinsky 6.0 Video

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.sberbank.ru/ru/sberpress/all/article>

## Контекст

<!-- enrichment:context -->
_Analytical notes (not a post). Importance: 2/5 — real, live, open-sourced capability, but a consumer media feature and 2024–25-era catch-up tech; fintech angle is indirect (Sber AI-platform/import-substitution + sanctions-compute story)._

## [0] What exactly happened (de-PR'd)
Sber wired **free text-to-video generation into GigaChat**, powered by a new **Kandinsky 6.0 Video** model: clips **up to 5 seconds**, with **synchronized audio** (speech/music/ambient, lip-synced, 44 kHz), up to **Full HD (1920×1080)**, **24 fps**. Announced ~**Oct 6, 2026** (arXiv:2610.05608, submitted Oct 4); model **open-weighted under MIT** on GitHub/HuggingFace/ComfyUI (Lite 3B / Pro 29B, dual-stream "CrossDiT"). The GigaChat feature is **live, not just announced** (SD/HD/Full HD selector in the input box).
- **De-PR flags:** "Full HD" is achieved by a **separate super-resolution upscaler**, not native generation. "Free, no limits" is a vendor headline — **no published daily cap, queue policy, or quality throttle**; a 29B model served free at scale is almost certainly rate-limited/queued in practice (unconfirmed). The genuine first-ever here is **synchronized audio** for a Russian model — the video itself is an upgrade over Kandinsky 5.0.
- **Why structured this way:** MIT open-weights + free consumer tier is a **funnel + national-standard play**, not charity. The tell is the license — Sber wants Kandinsky embedded in third-party Russian products (agencies, martech, SberCloud API); consumer "free" drives engagement/lock-in, while **GigaChat Pro/MAX and B2B SberCloud** are the implied paid layers.

## [1] Competitors / peers
- **Global frontier:** OpenAI **Sora 2** (~25s, audio), Google **Veo 3.1** (8–15s, 4K/60fps, native audio), Kuaishou **Kling 3.0** (extendable to minutes), Runway, MiniMax Hailuo/H3, ByteDance Seedance. Native synced audio is **2025-era table stakes** for these — so Kandinsky's "video with sound" is **parity, not novelty, globally**; it's novel only *for a Russian model*.
- **Position:** On length/fps/resolution (5s / 24fps / 1080p-upscaled) Kandinsky **lags all frontier rivals**. Sber's benchmark claims are **cherry-picked**: beats its own 5.0, beats open LTX 2.5, "trails only MiniMax H3" among open models, and one RU outlet claims it exceeds **Veo 3.1 Fast** on image-animation specifically — no clean win vs full Sora 2 / Veo 3.1 / Kling 3.0. arXiv abstract itself only claims "competitive… particularly in speech quality."
- **Why the lay of the land matters (second order):** ChatGPT/Sora are **geoblocked/banned in Russia**; Veo gated. So the relevant comparison for RU users is not "as good as Sora" but "**best accessible option**." That makes 2024/25-parity **commercially sufficient domestically** — the real competitive lever is **price (Full HD + sound for free)**, where Sora 2 free is 480p, Veo has no real free tier, Kling ~66 free credits/day. Internally compare the Western frontier that this substitutes for: [[Google launches Nano Banana 2 Lite and Gemini Omni Flash]], [[Google Vids adds personalized AI avatars for users]], [[AI startup Runway plans major London expansion]].

## [2] Company history / fit
- **Kandinsky video lineage:** first dedicated T2V late 2023 → Kandinsky 3.1 (Apr 2024) → **Kandinsky 4.0 Video (Dec 2024, first DiT, ~12s HD, silent)** → **Kandinsky 5.0 (Nov 2025, open-source, Lite 2B/Pro 19B, ~10s HD, no audio)** → **6.0 (Oct 2026, + synced audio)**. Note the **odd regression**: 5.0 did ~10s silent, 6.0 drops to 5s but adds sound — audio-sync is the expensive new trick, not longer/better video.
- **Fit:** This slots cleanly into Sber's stack ([[Sber unveils flagship GigaChat 3.5 Ultra model]] lists "Kandinsky (image/video)" as a pillar alongside GigaChat LLMs, GigaCode, AIRI). GigaChat is the ChatGPT substitute; adding free video **deepens the everything-app ecosystem** and the import-substitution narrative. See also same-day Sber/GigaChat consumer pushes: [[SberInvestments launches GigaChat tool explaining portfolio moves]].
- **Why the company acts this way:** Sber is **compute-constrained under sanctions** — Gref (May 2026) said GigaChat hopes to run on Chinese **Huawei Ascend** chips, behind ByteDance/Alibaba in queue. Shipping a *free* 29B video model while compute-strained implies either real efficiency (the Lite 3B) or heavily capped free throughput — reinforcing the "free is funnel, not product" read.

## [3] Novelty / value-add / traction
- **Real novelty:** synchronized video+audio with lip-sync in an **open-weight (MIT)** model is non-trivial engineering and a **first for a Russian model**. That is the genuine delta.
- **Not novel:** globally this is catch-up to 2024–25 Western capability; length/resolution/fps lag the frontier; Full HD is upscaled.
- **Traction:** none yet beyond launch — **no usage/adoption numbers**, no disclosed free-tier limits. "Live in GigaChat" is confirmed; sustained free-at-scale economics are **unproven**.
- **Who captures the margin (why value-add is/ isn't real):** consumer video gen is a **loss-leader**; margin sits in (a) ecosystem lock-in/engagement for the Sber super-app and (b) **SberCloud B2B API + GigaChat Pro/MAX**. MIT open-weights deliberately **commoditizes the model** to make Sber the default Russian standard — betting value accrues to the **distribution + cloud layer**, not the model itself.

## [4] What's next / market sentiment
- **Plans:** Sber signals it will **extend clip length** beyond 5s later; open-weights invite ComfyUI/third-party integration; implied monetization via SberCloud/GigaChat paid tiers (pricing **unconfirmed**).
- **Risks (silent in PR):** no apples-to-apples frontier benchmark; "free" cost hidden (expect throttling); **training-data provenance undisclosed** — material given it generates human speech + lip-sync (deepfake/likeness + copyright exposure), and the watermark is reportedly **strippable with simple filters** (single-source, unconfirmed); dependence on scarce/Chinese compute.
- **Why the market goes this way (second order):** in a geoblocked market, **"accessible + free + good enough" beats "frontier-but-banned."** Sber doesn't need to beat Sora; it needs to own the default RU AI surface before Yandex/VK/T-Tech do — which makes catch-up tech strategically rational. The genuinely fintech-adjacent signal is the **sanctions-compute dependency** (Huawei Ascend) exposed by shipping a heavy model for free.

## Top challenge / extra questions
1. Is the free tier truly uncapped, or rate-limited/queued? → **open** (no published caps).
2. Is Full HD native or upscaled? → **upscaled** (separate SR model).
3. First-ever video or upgrade? → **upgrade**; first-ever is *synced audio*, video dates to 2023 / 4.0 Dec 2024.
4. Does it beat Sora 2 / Veo 3.1 / Kling 3.0? → **no clean claim**; only vs own 5.0, open LTX 2.5, and "Veo 3.1 Fast" on one task.
5. Why does 6.0 regress to 5s from 5.0's ~10s? → audio-sync is the expensive new capability (analysis).
6. Who captures margin from a free consumer model? → SberCloud B2B + GigaChat Pro/MAX + ecosystem lock-in (analysis).
7. Does geoblocking of Sora/Veo change the competitive bar? → yes; "best accessible" > "best."
8. Training-data provenance / copyright? → **silent / open** — key given lip-synced human speech.
9. Is the watermark robust? → reportedly strippable (single-source, **unconfirmed**).
10. Can Sber afford free 29B at scale under sanctions-compute? → **open**; implies throttling or Lite-3B default.
11. Is there a hosted API free tier, or only GigaChat UI + self-host weights? → **unconfirmed**.
12. Fintech materiality? → **low-direct** (consumer media), meaningful only as AI-sovereignty / SberCloud monetization data point.

## Sources
See challenge column. Primary: arXiv:2610.05608; kandinskylab.ai; github.com/kandinskylab/kandinsky-6; Sber press (sberbank.ru). Secondary RU: 3dnews.ru/1149527, hi-tech.mail.ru/news/157142, 4pda.to/2026/10/06/461916, vc.ru/ai/3041620. Lineage: github.com/ai-forever/Kandinsky-4, arXiv:2511.14993. Compute context: tomshardware (Sber/Huawei Ascend, May 2026).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / freshness verdict.**

**FRESHNESS: FRESH.** Internal grep (`kandinsky`, `gigachat`, video-gen terms across `News/`) surfaces **no prior note on Kandinsky 6.0 or any Kandinsky video release**. The only prior mention is a one-line stack reference ("Kandinsky (image/video)") inside [[Sber unveils flagship GigaChat 3.5 Ultra model]] (Jul 2026) — not a coverage of this release. No duplicate_of. This is a genuine new event (Oct 6, 2026 launch: Kandinsky 6.0 Video + free generation live in GigaChat).

**What it really is (anti-PR):**
- **Catch-up, not a leap.** 5s / 24fps / 1080p (upscaled) with synced audio = **2024–25 Western capability band**. Frontier (Sora 2 ~25s; Veo 3.1 8–15s/4K/60fps/native audio; Kling 3.0 minutes) is well ahead on length, fps, resolution. Synced audio is a genuine **first for a Russian model** but global table stakes.
- **"Free, no limits" is unverified.** No published daily cap / queue / throttle; a free 29B model under sanctions-compute almost certainly throttles (unconfirmed).
- **"Full HD" is upscaled**, not native generation.
- **Benchmarks cherry-picked:** only vs own 5.0, open LTX 2.5, and "Veo 3.1 Fast" on image-animation (one RU source, narrow task). arXiv claims only "competitive… particularly in speech quality." No clean win vs full frontier.
- **Odd regression:** 6.0 drops to 5s from 5.0's ~10s — audio-sync is the costly new trick.
- **Silent on:** training-data provenance/copyright (material given lip-synced human speech), watermark robustness (reportedly strippable, single-source), real free-tier economics under Huawei-Ascend compute constraints.
- **Why it still matters:** geoblocking of Sora/Veo in Russia makes "accessible + free + good enough" > "frontier-but-banned"; strategic for Sber's super-app lock-in and import-substitution. Fintech-adjacent signal = **sanctions-compute dependency** (Gref/Huawei Ascend, May 2026) and SberCloud/GigaChat Pro monetization funnel.

**Importance: 2/5 — rationale.** Technically credible and strategically meaningful for the RU import-substitution / Sber-ecosystem story, but it is a **consumer media feature**, not a banking/payments development, and globally it is catch-up tech with no verified traction. Bump to 3 only if tracking Russian AI-sovereignty / SberCloud monetization as a theme.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Generative text-to-video ("gen-video") moved from frontier demo to commodity consumer feature through 2025–2026. The sector's defining shift this year is the collapse of the paid-only model: OpenAI shut its standalone Sora app (26 Apr 2026) and killed the Sora API (24 Sep 2026), per Wikipedia/Artnet, while Google Veo pushed native-audio 4K clips (Veo 3/3.1). Kandinsky 6.0 Video (Sber/Kandinsky Lab, open-sourced 6 Oct 2026) sits squarely in the new "free + synchronized audio" wave: 5-sec clips with speech/lip-sync, SFX, music and ambience from one prompt, up to Full HD, shipped under an MIT license, with ~10 free generations/day inside GigaChat after sign-in (per 3dnews/iphones.ru/technetbooks, Oct 2026). No credible, verifiable TAM for Russian gen-video specifically — "no data"; treat global figures as inapplicable given sanctions-walled compute/model access. "Why now": (1) foundation-model cost curves make 5-sec HD generation cheap enough to give away as a funnel feature; (2) for Russia, Western tools (Sora/Veo) are largely inaccessible, so domestic incumbents (Sber, Yandex) race to own the default.

**Competitive landscape.** This is not a standalone revenue line — it is a distribution/engagement feature bundled into a super-app AI assistant; the KPIs that matter are MAU, queries/engagement and downstream monetization of the parent AI stack, not a per-video take rate (none disclosed — `[UNSOURCED]`). Key players in Russia: Sber (GigaChat + Kandinsky), Yandex (Shedevrum / YandexART, ~5B-param image/video model per SourceForge/PowerUsers). Basis of competition = distribution (who owns the default assistant/super-app) + Russian-language quality + price (now effectively zero). Recent moves: GigaChat 3.5 Ultra flagship LLM (6 Jul 2026, [[Sber unveils flagship GigaChat 3.5 Ultra model]]); GigaChat embedded into SberInvestments portfolio explainer and SberDevices AI deals, same-day cluster ([[SberInvestments launches GigaChat tool explaining portfolio moves]], [[Sber teaches AIFA financial analyst to self-plan analysis]]). Sber's position: **ahead on distribution inside Russia** (GigaChat 20M+ MAU, 800M+ queries in 2025, per Sber FY2025/Investor Day via TASS) and now also ahead on openness (MIT license vs Yandex's closed Shedevrum). Moat = distribution/scale via the Sber super-app + bundling into financial services, not a model-quality moat (Sber itself benchmarks Kandinsky 6.0 Pro only as "competitive with leading audio-video models," not best — i.e. parity, not lead) `(analysis)`.

**Comps & multiples.** No deal/round/valuation attaches to this news — it is a free product feature, so trading multiples are **not applicable / "no data"**; distribution not computed. Internal comps (feature/launch precedents, not valuation): [[Sber unveils flagship GigaChat 3.5 Ultra model]] (Jul 2026 flagship LLM), [[SberInvestments launches GigaChat tool explaining portfolio moves]], [[Sber teaches AIFA financial analyst to self-plan analysis]] (both 12 Oct / 5 Oct 2026, GigaChat productization), [[VK launches Discovery AI neural search across products]] (Jul 2026, VK gen-AI peer, reported dev spend up to RUB 500mn). For scale/parent anchor (IR, PRIMARY): Sber Group FY2025 IFRS net profit **RUB 1,705.9bn (+7.9% YoY), ROE 22.7%** (Sber FY2025 IFRS statements, 26 Feb 2026, data/sber/ir/annual_report/reporting_q4_8a5ewlbo_2025_en.pdf · https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf). AI economic effect FY2025 **RUB ~450bn** total, of which **RUB ~50bn from generative AI**; Gref guided total AI effect to **RUB 550bn in 2026** (Investor Day, 10 Dec 2025, via TASS). Arithmetic for context: GenAI effect RUB 50bn / FY2025 net profit RUB 1,705.9bn = **~2.9% of group profit** — i.e. GenAI (incl. GigaChat/Kandinsky) is still a strategic/engagement bet, not yet a material P&L driver `(analysis)`.

**Risk flags.**
1. **No direct monetization / cost-side drag.** Free Full-HD video with audio at ~10/day/user is a pure cost and engagement play; GenAI is still ~2.9% of group profit (arithmetic above). Giving away compute-heavy inference raises COGS with no stated payback path — second-order: pressure to paywall or throttle once adoption scales, undercutting the "free" positioning.
2. **Parity, not leadership — commoditization.** Sber's own evaluation frames Kandinsky 6.0 Pro as "competitive," and the MIT open-sourcing lets anyone (incl. rivals/agencies) run it on their own hardware. Open weights erode any model moat and let competitors catch up instantly — the only durable edge is distribution, not the model.
3. **Regulatory / content-liability exposure.** Lip-synced speech + photoreal 5-sec video is prime deepfake material; Russian AI-content/labelling rules are tightening — second-order: compliance cost, forced watermarking, or feature restrictions that blunt the consumer hook.

**What this changes (idea-lens).** `(analysis)` This confirms the Russian gen-video market is being commoditized toward free-by-default, with the battle collapsing to *distribution* between Sber (GigaChat) and Yandex (Shedevrum) rather than model quality. Falsifiable thesis: GigaChat MAU and queries re-accelerate in FY2026 disclosures as gen-video drives engagement, feeding Sber's RUB 550bn 2026 AI-effect guidance. Trigger/what breaks it: watch the next Sber results (Q1/1H 2026 IFRS) for GigaChat MAU and GenAI effect — if GenAI's share of profit stays flat near ~3% while free video scales, the feature is a cost sink, not a flywheel.

Sources: https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf · https://tass.com/economy/2092243 · https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · https://3dnews.ru/1149527/ · https://www.iphones.ru/iNotes/v-gigachate-poyavilas-besplatnaya-generaciya-video-so-zvukom-v-full-hd · https://www.technetbooks.com/2026/10/sber-releases-kandinsky-60-video-with.html · https://en.wikipedia.org/wiki/Sora_(text-to-video_model) · https://news.artnet.com/art-world/openai-shutters-sora-2758298
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Product story, not an earnings release. Sber's own financials are grounded below as context; no results data is reported in this GigaChat/Kandinsky item itself.

**Verdict (headline read).** N/A to this item — a free-feature product launch (Kandinsky 6.0 Video in GigaChat), no financials. For grounding: Sber's latest print is IN-LINE/solid — H1 2026 IFRS net profit RUB 1,019bn (+18.6% YoY), ROE 24.2%, carrying the FY2025 base (net profit RUB 1,705.9bn, +7.9% YoY, ROE 22.7%).

**Key figures (latest reported, for context).**
- **H1 2026 IFRS (most recent print):** net profit >RUB 1,019bn, +18.6% YoY; ROE 24.2%; net interest income >RUB 2.05tn, +22.5% YoY; NIM 6.7% in Q2. Quarterly: Q1 2026 net income RUB 507.9bn (+16.5% YoY), Q2 2026 RUB 511.2bn (NII +26.7% in the quarter).
- **FY2025 IFRS (annual baseline, latest full-year filing, 2026-02-26):** net profit RUB 1,705.9bn (~$22bn), +7.9% YoY; ROE 22.7%; net interest income RUB 3,556bn, +18.5% YoY; NIM expanded 6.0% (Q4 2024) → 6.5% (Q4 2025); cost-to-income 30.3%.

**AI-investment / monetization flags (the only earnings-relevant angle for an AI product story).**
- Sber frames AI as a P&L lever, not just R&D: management has guided ~RUB 60bn over three years into AI/GenAI and cites ~$1bn/year AI spend, targeting ~RUB 550bn of cumulative AI-driven value by 2026 (revenue uplift + risk reduction + cost optimization) (hypothesis — press-cited management targets, not an audited line item).
- GigaChat monetization is still small vs the RUB 1.7tn group profit: Sber projected ~RUB 10bn of GigaChat revenue for 2024 via licensing/integration (analysis — immaterial at group scale; the strategic value is operating leverage, i.e. the 30.3% cost-to-income, not direct SaaS revenue).
- De-PR: a **free** video-gen feature is customer-acquisition/engagement spend, not a revenue event — it monetizes indirectly (ecosystem lock-in, GigaChat API upsell). Watch whether free multimodal features pressure the AI unit's own economics; Sber discloses no standalone GigaChat P&L, so direct monetization is [UNSOURCED].

**Guidance / forward.** FY2025 management trimmed the net fee & commission income growth target to 3%–5% (loyalty-program expansion / commission waivers) — a mild negative on fee momentum; NII and ROE remain the profit engine (ROE held ~24% into H1 2026). No AI-specific revenue guidance is broken out.

**Thesis-flags.**
1. ROE durable at ~24% (H1 2026) despite a Russian macro slowdown → the AI/efficiency program is showing up in cost discipline (cost-to-income 30.3%), the second-order payoff Sber wants from GigaChat, not in direct AI revenue.
2. Fee-income guidance cut to 3%–5% is the soft spot; free AI features add engagement but not near-term fees — monetization remains a "later" story.

Sources: Sber Summary Consolidated IFRS Financial Statements 12M 2025 (FY2025) — https://www.sberbank.com/common/img/uploaded/files/info/reporting_q4_8a5ewlbo_2025_en.pdf (url fallback; no drive_url) · FY2025 figures: https://tass.com/economy/2092243 · https://www.investing.com/news/company-news/sber-2025-slides-227-roe-achieved-amid-russian-economic-slowdown-93CH-4527511 · H1 2026: https://www.investing.com/news/transcripts/earnings-call-transcript-sber-posts-strong-h1-2026-profit-as-macro-risks-rise-93CH-4819283 · Q1 2026: https://tass.com/economy/2123961 · AI-investment targets: https://quartr.com/events/sberbank-of-russia-sber-investor-day-2025_F6WnUnpc · GigaChat monetization [UNSOURCED standalone P&L].
<!-- /enrichment:earnings_review -->
