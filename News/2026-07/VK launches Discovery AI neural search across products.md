---
title: "VK launches Discovery AI neural search across products"
date: 2026-07-01
retrieved: 2026-07-01
tags:
  - company/vk
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://www.forbes.ru/tekhnologii/564003-kanal-discovery-vk-zapuskaet-sobstvennyj-nejropoisk
status: published
n_mentions: 1
channels:
  - "42 секунды"
story_id: sb10142c1
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# VK launches Discovery AI neural search across products

> [!info] 2026-07-01 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Forbes: VK запускает собственный нейропоиск – VK внедряет в свои продукты новую технологию нейропоиска Discovery AI – Технологию внедрят в «VK Видео», «Дзен» и «Медиапроекты Mail» – Discovery AI поможет подбирать контент и получать ИИ-ответы на вопросы – Новая технология работает на базе собственной модели от компании – В основе лежат веса open-source LLM, которые дообучили инженеры AI VK – Нейропоиск учитывает интересы пользователей во всех сервисах VK – Технологию Discovery AI можно адаптировать под самые разные сценарии – В новостных сервисах можно найти общий контекст вокруг события – Контентные сервисы помогут подобрать плейлист или фильм на вечер – В дейтинге можно составить запрос фразой, а не по параметрам – Также технология Discovery AI может работать в режиме Deep Research – Discovery AI может уточнять детали запроса, проводить анализ и др. – Источники оценивают инвестиции в разработку Discovery AI до 500 млн руб. – Нейропоиск стал одним из самых популярных корп

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.forbes.ru/tekhnologii/564003-kanal-discovery-vk-zapuskaet-sobstvennyj-nejropoisk>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: VK launches Discovery AI neural search across products
_Analytical notes (not a post). Importance: 3/5._

**Freshness verdict: FRESH.** No prior note on VK exists in the corpus (internal `sem search` and grep returned only cross-lingual false positives from Klarna/PhonePe/FIS AI-search items and "VK" substring hits inside Revolut notes — none about VK Company). Externally, VK launched a unified **Discovery** *recommendation* platform back in 2025 (Forbes RU, "VK внедрила технологии рекомендаций на базе ИИ", forbes.ru/…/549931). The 2026-07-01 news is the **generative neural-search / RAG layer ("Discovery AI") built on top** of that platform — a new capability, not a reprint of the 2025 platform launch. Not stale.

## [0] What exactly happened (de-PR'd)
- 2026-07-01, VK announced **Discovery AI**, a neural-search + generative-answer ("нейропоиск") technology being rolled into **VK Видео, Дзен (Zen), and Медиапроекты Mail (Mail media)**. Primary source: Forbes RU (forbes.ru/…/564003), retold by the "42 секунды" channel; corroborated by CNews, AdIndex, and a VK engineering blog on Habr (habr.com/ru/companies/vk/articles/1054358).
- Function: content discovery (find a video/playlist/film), AI answers to questions, "общий контекст вокруг события" for news, natural-language querying in dating ("составить запрос фразой, а не по параметрам"), and a **Deep Research mode** (multi-step query refinement + analysis).
- Mechanism (from VK's own Habr post — vendor claim, not independently verified): built on **weights of an open-source LLM fine-tuned by AI VK engineers**, plus BERT-like transformers, "billions of synthetic annotations", claimed **first-token latency <500 ms**. It reuses the cross-product signal graph from the 2025 Discovery recommendation platform ("учитывает интересы пользователей во всех сервисах VK").
- **Investment: "up to ~500 million rubles" (~$5.8m)** per Forbes sources — a notably SMALL figure that is the de-PR'd headline. It signals VK did NOT train a foundation model; it fine-tuned open weights and wrapped them in retrieval over its existing content graph.
- **Why framed this way:** VK leads with breadth ("across products") and the Deep Research buzzword, and lets the ~500m ruble number leak as evidence of capital discipline. That framing is deliberate: VK is a serially loss-making company (see [2]) that cannot credibly sell a "we built a frontier LLM" story, so it sells "cheap, pragmatic AI layered on our unique content moat". The real claim is distribution + data, not model prowess.

## [1] Competitors / peers
- **Yandex** — the clear leader. Yandex "Neuro" neural search and **Alice AI** serve ~88m Alisa users; the Alice AI LLM family (rebranded Feb 2026) is regarded as the strongest Russian-made model. Yandex owns both the general-web search box AND the assistant — VK does not have a general search engine, so VK's neural search only lives *inside its own content silos*.
- **Sber / GigaChat** — enterprise/B2B leader; GigaChat adopted by ~15,000 Russian companies in year one, tied to the Sber ecosystem; Sber has publicly pushed a reasoning LLM. GigaChat competes on B2B and assistant, less on in-app content discovery.
- **Position: catching up / niche.** VK is neither the model leader (Yandex/Sber) nor a general-search player. Its edge is **owning the largest Russian consumer content corpus** (VK Video, Clips, Zen, Mail) — that is the one axis where it beats Yandex/Sber. (analysis) The bet is that discovery inside that corpus is a distribution game VK can win locally even with a fine-tuned open model.
- **Why the landscape is this way (2nd order):** Russian AI is a 3-horse sovereign race (Yandex, Sber, VK) walled off from OpenAI/Google by sanctions. VK is structurally the weakest financially, so it competes on the one asset the other two lack — a captive social/video audience — rather than on model quality. Whether "cheapest fine-tuned model + best content graph" beats "best model + your own search box" is the open question.

## [2] Company history / fit
- VK Company (ex-Mail.ru Group) is state-adjacent, runs VKontakte, VK Video/Clips, Mail, Zen, and the state-mandated national messenger **MAX**.
- **Financials (weak, the key backdrop):** VK logged its **6th straight annual loss** (FY2025, Moscow Times, 2026-03-19). Net debt cut >half to **RUB 82bn (~$951m)**, but 2025 interest expense **RUB 23.25bn** roughly equalled adjusted **EBITDA of RUB 22.6bn** — i.e. debt service eats essentially all operating cash flow. Net debt/EBITDA ~3.6x (target 2–3x); guides EBITDA >RUB 20bn for 2026.
- Product strategy 2025: improve recommendations, ad efficiency, prioritize MAX, social commerce, and **VK Video leadership** (VK Clips daily views +92% YoY to 3.25bn in Q1'25). The 2025 unified Discovery *recommendation* platform (multimodal LLM, cross-format content model, face recognition) is the direct predecessor of this 2026 search layer.
- **Fit: logical and cheap by necessity.** With interest expense ≈ EBITDA, VK cannot fund a frontier-model program. A **~500m ruble fine-tune-and-retrieve project** that lifts engagement (time-spent → ad inventory) across already-owned surfaces is exactly the move a cash-constrained, ad-dependent, loss-making company makes. **Structural driver:** ad revenue needs engagement; engagement needs better discovery; VK can't afford to buy discovery from anyone → it must build the cheapest in-house version on its own data.

## [3] Novelty / value-add / traction
- **What's new:** the *generative/agentic search* layer (AI answers, Deep Research, NL querying incl. dating) on top of the pre-existing 2025 recommendation platform. The recommendation platform and cross-product personalization are NOT new.
- **What's not new / is PR:** "own model" — it's fine-tuned open weights, standard 2025-26 practice; the <500ms latency and "billions of synthetic annotations" are unverified vendor stats from VK's own blog.
- **Traction: essentially none disclosed.** This is an **announcement, not adoption** — no live user counts, query volumes, engagement lift, or A/B results for Discovery AI search. The aggregated text's tail ("стал одним из самых популярных корп…") is truncated and unsubstantiated. Contrast Yandex's cited 88m Alisa users and GigaChat's 15,000 companies — VK gave no comparable number.
- **Who captures the margin (2nd order):** VK monetizes via ads, so value accrues only if better discovery → more time-spent → more ad inventory/CPM. The margin sits with VK's ad business, not the AI feature itself; the feature is a cost center justified by engagement. **What breaks it:** if users treat in-app AI search as a novelty and still go to Yandex/Alice for real answers, VK burns opex without an engagement payoff. (analysis)

## [4] What's next / market sentiment
- Expect VK to (a) extend Discovery AI into MAX and social commerce (its stated priorities), (b) later publish engagement/adoption stats if favorable, (c) position it in the sovereign-AI narrative for regulatory goodwill.
- **Sentiment:** analysts remain skeptical of VK — weak ad momentum, high borrowing costs, unproven monetization of MAX and new products; the AI push is credibility-positive but immaterial to the P&L at ~500m rubles.
- **Regulatory backdrop:** Russian tech-sovereignty policy favors domestic LLMs; being visibly "AI-native" helps VK with the state, which matters given its state-adjacent role and the MAX mandate.
- **Counterintuitive 2nd-order:** the *smallness* of the investment is the real signal. It reframes the central question from "how good is VK's AI?" to **"can a financially stretched incumbent turn a cheap AI layer on a captive content graph into measurable engagement/ad lift before Yandex's superior assistant makes in-silo search feel second-rate?"** If yes, capital-efficient; if no, it's a defensive feature that changes nothing about VK's loss trajectory.

## Top challenge/extra questions
See challenge column / chl_vk-discovery.md.

## Sources
- Forbes RU 2026-07-01 (primary): https://www.forbes.ru/tekhnologii/564003-kanal-discovery-vk-zapuskaet-sobstvennyj-nejropoisk
- VK Habr engineering post: https://habr.com/ru/companies/vk/articles/1054358/
- CNews 2026-07-01: https://www.cnews.ru/news/line/2026-07-01_vk_vnedryaet_ii-poisk_v_produkty
- AdIndex 2026-07-01: https://adindex.ru/news/digital/2026/07/1/346799.phtml
- Forbes RU 2025 (predecessor Discovery recommendation platform): https://www.forbes.ru/tekhnologii/549931-vk-vnedrila-tehnologii-rekomendacij-na-baze-ii
- VK FY2025 press release: https://vk.company/en/press/releases/12255/
- Moscow Times 2026-03-19 (6th straight loss): https://www.themoscowtimes.com/2026/03/19/vk-logs-6th-straight-annual-loss-despite-revenue-growth-a92270
- Yandex Alice AI: https://yandex.com/company/news/2025-10-28-01 ; https://en.wikipedia.org/wiki/Alice_AI
- GigaChat / Sber: https://cryptorank.io/news/feed/fefe1-russia-sberbank-to-unveil-reasoning-llm
- No internal corpus prior notes on VK (verified via sem search + grep).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Announced vs live?** Is Discovery AI search actually live in VK Видео/Дзен/Mail for all users on 2026-07-01, or a phased/beta rollout? — **OPEN.** Press says "внедряет/внедрят" (present/future); no user counts or rollout % given. Treat as announcement.

2. **What is the "own model", really?** VK's own Habr post says it fine-tuned **open-source LLM weights** — so "собственная модель" is a fine-tune, not a from-scratch foundation model. Which base (Llama/Qwen/etc.)? — **OPEN** (not disclosed). Undercuts the "proprietary model" framing.

3. **Is the ~500m ruble figure the whole cost?** Forbes attributes it to third-party sources ("up to 500m rubles"), corroborated by one external engineer — NOT VK-confirmed. Does it exclude the 2025 Discovery platform sunk cost and inference/GPU opex? — **OPEN, likely excludes.** The real all-in cost is higher.

4. **Any adoption/traction number at all?** Query volume, engagement lift, time-spent delta, A/B conversion? — **NONE disclosed.** This is the decisive gap vs Yandex (88m Alisa users) and GigaChat (15k companies). Weight is capped low without it.

5. **Does it beat Yandex/Alice inside VK's own apps?** Users can already ask Alice anything; will they use VK's in-silo search or default to Yandex? — **OPEN (analysis: skeptical).** VK's only edge is proprietary VK Video/Zen content Yandex can't index as deeply.

6. **Is the moat the model or the content graph?** Answer: the **content graph** (largest RU consumer video/media corpus). The model is commodity fine-tune. So the item's value = distribution+data, not AI quality. Confirms importance is about VK's engagement funnel, not AI leadership.

7. **How does this touch the P&L?** Value only via ads: better discovery → time-spent → inventory/CPM. At ~500m rubles it is immaterial to a company with RUB 23bn interest expense. — **Analysis: credibility play, not a financial needle-mover.**

8. **Why now?** VK just posted a 6th straight loss (Mar 2026) and needs an AI-native narrative for the state (sovereign-AI policy, MAX mandate). Is timing PR/regulatory rather than product-driven? — **Plausible; analysis.**

9. **Latency claim <500ms to first token — verified?** From VK's own blog only; no third-party benchmark. — **OPEN / vendor claim.**

10. **Deep Research mode — genuine agent or rebranded multi-step retrieval?** "Уточняет детали, проводит анализ" is the standard agentic-RAG pattern of 2025-26, not novel. — **Analysis: not differentiated.**

11. **Duplicate of the 2025 Discovery platform?** No — 2025 was the *recommendation* platform; 2026 adds the *generative search* layer. Genuinely incremental new capability. — **FRESH.**

12. **Any prior corpus note?** Internal sem search + grep found none on VK Company. — **No duplicate in DB.**

13. **Dating natural-language querying — does VK have a dating product at scale?** Which service (VK Знакомства)? Is this a real surface or a demo scenario? — **OPEN.**

14. **Data/privacy angle:** "учитывает интересы во всех сервисах VK" = cross-service profiling across VK/Mail/Zen/dating. Any regulatory or user-trust risk in RU context? — **OPEN, not addressed by VK.**

15. **What breaks the bet?** If in-app AI search is a novelty users abandon for Yandex/Alice, VK adds opex with no engagement payoff — a defensive feature that doesn't change the loss trajectory. — **Key downside trigger.**

**Importance: 3/5.** Rationale: a real, sensibly-scoped product move by a top-3 Russian tech platform on its genuinely unique content moat (raises it above 1–2), BUT it is an announcement with zero disclosed traction, a commodity fine-tuned model, and a tiny (~500m ruble) financially immaterial investment, and VK trails Yandex/Sber on model quality (caps it below 4). Fresh, not a duplicate.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-02]] (2026-07-02).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian generative-AI search / "answer engine" layer, adjacent to VK's core ad-supported content ecosystem. Market structure is a **duopoly-plus**: Yandex leads with ~69.3% of Russian search share and its "Neuro/Alisa" answer engine reaching a ~19mn weekly audience; Alice AI investment alone was ~RUB 55bn in 2025 (per Yandex FY2025, via akm.ru/onlinemarketplaces, as of 2025). Sber's GigaChat is the second pole (GigaChat 3 Ultra Preview, open MoE model, Nov 2025). A Q1-2026 consumer AI-assistant tracker put Yandex's Alisa at ~67% share vs DeepSeek ~29% / ChatGPT ~7% domestically (per geoscout.pro, Q1 2026 — third-party estimate, treat as indicative). Driver / "why now": foreign models are throttled/unavailable in RU (import-substitution + regulation), so the contest is between domestic ecosystems; each incumbent is bolting generative answers onto an owned distribution surface (Yandex→search, Sber→super-app/bank, VK→content) to defend engagement and ad inventory. Barriers: proprietary content corpus + recsys + compute + distribution, not the LLM weights themselves (VK openly fine-tunes open-source weights — see note text).

**Competitive landscape.** Sector KPIs: MAU/WAU of the answer engine, query share, session depth, and (for VK specifically) ad load / eCPM on the surfaces where search is embedded (VK Video, Dzen, Mail media). Key players & basis of competition: **Yandex** (query share + data recency, RUB 551.2bn Search-Services-&-AI revenue in 2025, +10% YoY — via akm.ru); **Sber/GigaChat** (bank + super-app distribution, own foundation model); **VK** (largest RU content base + cross-service intent — video/Dzen/Mail/dating). Basis of competition is **distribution + proprietary content**, not raw model quality. Recent moves: VK's Discovery AI launch 2026-07-01 into VK Video, Dzen and Mail media, with a "Deep Research" mode and cross-service personalization; reported dev spend "up to RUB 500mn" (per Forbes, note source — small vs Yandex's RUB 55bn Alice budget, i.e. ~2 orders of magnitude less). VK's position: **catching up / follower** — it launches an answer engine ~2 years after Yandex Neuro (Apr 2024) and defends its own turf rather than contesting general web search. Moat `(analysis)`: intangible content corpus + cross-service intent graph (switching costs are low for a user, so the moat is engagement/distribution, not lock-in).

**Comps & multiples.** No round/valuation attaches to this product launch, so this is a positioning read, not a transaction comp. Peer scale (public, sourced):
- **VK (MOEX: VKCO):** FY2025 revenue RUB 160bn (+8% YoY); EBITDA RUB 22.6bn (margin 14%, from negative in 2024); video-ad revenue RUB 6.5bn (+68%); SME online ad RUB 37.7bn (+12%); VK Tech RUB 18.8bn (+38%). Net debt/EBITDA 3.6x, target 2–3x. Mkt cap ≈ RUB 15bn area / price ~RUB 240 (as of May-2026, via mlq.ai/smart-lab — cross-source, sanity only). **EV/Revenue on face ≈ tiny on equity but EV is dominated by debt** given 3.6x leverage → equity multiple not meaningful; flagged, not computed cleanly [UNSOURCED clean EV].
- **Yandex (MOEX: YDEX):** FY2025 revenue RUB 1.44tn (+32%); Search-Services-&-AI RUB 551.2bn; net profit RUB 79.6bn (via akm.ru/onlinemarketplaces/TheMoscowTimes). ~9x VK's total revenue — different weight class.
Cross-market **[UNSOURCED]**: no free, verifiable EV/EBITDA or EV/Revenue pair for VK vs Yandex captured here → "distribution not computed, qualitative comparison." Internal comps (base, AI-search/assistant launches as `[[wikilink]]`): [[PhonePe launches AI natural-language search with Microsoft]], [[Revolut launches AIR AI assistant in app]], [[Perplexity launches AI shopping assistant with PayPal Instant Buy]], [[Bank of America rolls out AI payments assistant]] — the cross-industry pattern is incumbents embedding an answer/agent layer into an owned surface, matching VK's play.

**Risk flags.**
1. **Scale-of-investment gap.** ~RUB 500mn reported dev spend vs Yandex's RUB 55bn/yr on Alice (110x). Why: answer-engine quality is compute- and data-hungry; a follower on a fraction of the budget risks a persistently inferior product and being out-iterated.
2. **Balance-sheet constraint on the AI arms race.** Net debt/EBITDA at 3.6x (target 2–3x) limits how aggressively VK can fund an AI capex race while deleveraging. Why: forces trade-offs between AI spend and debt paydown just as peers escalate.
3. **"Announced ≠ adopted" + no disclosed economics.** VK gives no MAU/query-share/engagement or monetization uplift for Discovery AI, and generative answers can *cannibalize* ad-bearing feed impressions. Why: an answer engine that summarizes content can reduce the click/scroll surface that carries VK's ad load — the monetization mechanism is silent.

**What this changes (idea-lens).** `(analysis)` Not a re-rating catalyst — it's a **defensive parity move**: VK closing an obvious feature gap vs Yandex/Sber to protect engagement on its content assets, not a bid for general search. Falsifiable thesis: if VK later discloses Discovery-AI-attributable WAU or an ad eCPM/engagement uplift on VK Video/Dzen, it becomes a monetization story; absent that within ~2–3 quarters, treat it as table-stakes with no P&L signal. Trigger to watch: next VK results (post-9M/FY 2026) for any Discovery AI engagement or ad-yield metric; what breaks the thesis = a monetized VK Tech / B2B licensing angle for the model rather than pure consumer defense.

Sources: https://www.forbes.ru/tekhnologii/564003-kanal-discovery-vk-zapuskaet-sobstvennyj-nejropoisk · https://www.telecompaper.com/news/vk-revenues-up-8-in-2025-on-video-advertising-growth--1565830 · https://vk.company/en/press/releases/12255/ · IR FY2025 press release (drive: https://drive.google.com/file/d/1b7nHaZDN_nNcmL1M9t1FyyRjA9p8slb8/view) · https://www.akm.ru/eng/news/revenue-of-yandex-b2b-tech-according-to-ifrs-in-2025-in-two-key-areas-increased-by-48/ · https://www.onlinemarketplaces.com/articles/yandex-q4-revenue-up-28-as-real-estate-sits-within-ai-engine/ · https://geoscout.pro/en/blog/ai-visibility-rating-q1-2026 · https://mlq.ai/stocks/VKCO.ME/market-cap/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** IN-LINE / modestly ahead on profitability — this is a product launch (Discovery AI neuro-search), not a print, so the "earnings" read is VK's own latest audited numbers (FY2025, released 2026-03-19). Revenue RUB 160.0 bn (+8% YoY vs RUB 147.6 bn) · adj. EBITDA RUB 22.6 bn (roughly doubled, ▲RUB 12.4 bn YoY), EBITDA margin 14% (+~7 p.p.) · net debt cut >2x to RUB 82 bn. FY2025 adj. EBITDA cleared VK's own raised ">RUB 20 bn" guidance (originally ">RUB 10 bn"): a **beat vs own guidance**. No public sell-side consensus in the corpus → variance vs a Street number is [UNSOURCED]; verdict is vs prior year and vs management guidance.

**Key figures (with growth, FY2025 audited IFRS, RUB).**
- Revenue **RUB 160.0 bn, +8% YoY** (2024: 147.6). Growth decelerated hard from +23% in FY2024 — the top line is the weak spot.
- Adj. EBITDA **RUB 22.6 bn** vs ~RUB 10.2 bn in 2024 (smart-lab deck: ▲RUB 12.4 bn YoY → ≈+120%); **margin 14%**, up ~7 p.p. The FY2025 story is margin, not growth.
- Net loss: bottom-line profit/loss for FY2025 **[UNSOURCED]** in the filings retrieved (VK has historically run a net loss on heavy finance costs; not confirmed here → no data).
- VK Tech: revenue **RUB 18.8 bn, +38% YoY**; EBITDA **RUB 4.8 bn, +22%**; margin 26% (−3 p.p. YoY) — scaling but margin diluted by investment.
- Video advertising on VK platforms **RUB 6.5 bn, +68% YoY**; children's edtech **RUB 7.4 bn, +19% YoY**.
- Engagement: Q4 2025 time-spent **5.7 bn minutes/day, +20% YoY**; on average one user uses two VK products per day — the audience base the AI-search feature plugs into.

**By segment / driver.** Growth is carried by VK Tech (+38%) and video/in-stream advertising (+68%), i.e. the higher-margin, strategically-favoured lines; the legacy social/advertising core is the drag pulling group revenue to +8%. Profitability inflection (EBITDA doubling, +7 p.p. margin) is the real 2025 result — VK explicitly pivoted from top-line growth to "improve profitability." Discovery AI neuro-search (built on fine-tuned open-source LLM weights; press reports investment "up to RUB 500 mn") is embedded into VK Video, Dzen and Mail media — engagement/ad-monetisation plays on that same audience.

**vs expectations / prior period.** No public consensus in corpus → beat/miss is qualitative + [UNSOURCED] for any Street number. vs prior year: revenue growth decelerated (+23% FY2024 → +8% FY2025); EBITDA and margin sharply improved. Trajectory across the year: Q1 rev +16%, H1 +13%, 9M +10%, FY +8% — a clear **deceleration through 2025**, while adj. EBITDA margin held steady at 14% each quarter. Related in base: [[VK launches Discovery AI neural search across products]].

**Guidance / forward.** FY2025 adj. EBITDA guidance was raised during the year from ">RUB 10 bn" (set at FY2024 release) to ">RUB 20 bn" (at 9M 2025); actual RUB 22.6 bn **cleared the raised bar** — a beat with a credit-positive read. **FY2026 guidance: not found** in the retrieved filings ([UNSOURCED]; not given in corpus). Independent read (analysis): with the deleveraging done and margin discipline in place, 2026 is likely framed as continued profitability + selective AI/Tech investment rather than a growth re-acceleration.

**Thesis-flags — can VK fund an AI-search build given its debt/EBITDA?**
1. **Balance sheet de-risked, so yes — it can fund it.** Net debt cut **>2x to RUB 82 bn** (end-2025) via a **RUB 112 bn private SPO in H1 2025, 100% directed to debt reduction**; cash RUB 32.8 bn; net-debt/EBITDA **2.6x → 2.3x** with a further ~25% reduction targeted (Analyst Day 2026). ACRA upgraded VK to **AA(RU)/Stable**. Why it matters: a year ago the FY2024 accounts carried a **going-concern material-uncertainty flag** (debt/equity 6.44); that overhang is now largely cleared, so a modest AI-search build (~RUB 500 mn reported, i.e. immaterial vs RUB 22.6 bn EBITDA) is easily self-fundable from operating cash flow. Second-order: lower finance costs should feed the bottom line even without faster revenue.
2. **Growth deceleration is the standing risk (+8% and slowing).** AI neuro-search is an engagement/ad-monetisation lever precisely because the core top line is soft; if it lifts ad load and time-spent, it defends the +8% base — but it's a defensive, not a re-acceleration, bet. Why it matters: the equity story now leans on margin + deleveraging, not growth, so any EBITDA-margin slip would remove the sole positive driver.
3. **VK Tech margin dilution (26%, −3 p.p.).** The fastest grower is investing through margin; watch whether the group's +7 p.p. margin gain is durable or partly one-off/mix-driven. De-PR: management leads with EBITDA doubling and stays quiet on the FY2025 net result and any FY2026 numeric guidance — both absent from the retrieved filings.

Sources (primary = VK's own filings): FY2025 press release (audited IFRS, 2026-03-19) https://drive.google.com/file/d/1b7nHaZDN_nNcmL1M9t1FyyRjA9p8slb8/view · FY2025 results presentation https://drive.google.com/file/d/1-R2PjcT3YvpJKgHrDgoeQyIRTs0Sf6EE/view · Единый годовой отчёт 2025 (net debt RUB 82 bn, RUB 112 bn SPO) https://drive.google.com/file/d/1FB7eUJLNSAAVp-kbwSDXfUQGG9YQq4MG/view · Smart-Lab 2026 deck (EBITDA 22.6bn ▲12.4bn, net debt 82.3bn, 2.3x, cash 32.8bn, AA) https://drive.google.com/file/d/1_17YdGyWpHMJQ1eGH_Qopuzk2JbjZKlo/view · Analyst Day 2026 (net-debt/EBITDA 2.6x→2.3x, ▼25% target) https://drive.google.com/file/d/1rOToo_kQnLlxGEEO8G6JyOZD55KRUEJZ/view · prior/guidance: 9M 2025 (">20bn" forecast) https://drive.google.com/file/d/1LawNrtQ_o5yi8cI_BBFZZZpPD0861M1m/view · FY2024 release (">10bn" forecast, debt/equity 6.44) https://drive.google.com/file/d/1mAkQ10hOB8e1N1nX0zFPbDV8H09hLJVo/view · product/investment (up to RUB 500 mn): Forbes https://www.forbes.ru/tekhnologii/564003-kanal-discovery-vk-zapuskaet-sobstvennyj-nejropoisk · FY2025 net result & FY2026 numeric guidance: no data / [UNSOURCED] · public consensus: [UNSOURCED] (none in corpus).
<!-- /enrichment:earnings_review -->
