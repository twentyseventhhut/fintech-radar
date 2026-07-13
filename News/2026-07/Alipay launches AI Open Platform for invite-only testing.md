---
title: "Alipay launches AI Open Platform for invite-only testing"
date: 2026-07-08
retrieved: 2026-07-08
tags:
  - company/alipay
  - industry/ai
  - industry/payments
  - region/asia
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/fc1fae8a
status: published
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s8d47421e
month: 2026-07
enriched: true
importance: 3
freshness: fresh
---

# Alipay launches AI Open Platform for invite-only testing

> [!info] 2026-07-08 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇨🇳 Alipay launches AI Open Platform for invite testing, signaling FinTech’s pivot from blockchain to AI. The invite-only beta gives enterprise developers, merchants, and third-party software vendors the ability to turn their existing mini-programs into AI-callable tools.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/fc1fae8a>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Alipay launches AI Open Platform for invite-only testing
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
Alipay opened an **invite-only beta of its "AI Open Platform"** — the *supply-side / developer* layer of its broader AI overhaul. It lets **enterprise developers, merchants and third-party software vendors (ISVs) convert existing mini-programs, APIs and service interfaces into "AI-callable tools"** without rebuilding them, so those services can be invoked by Alipay's conversational agent **Abao (阿宝 / "Ah Bao")**. Access is gated to invited partners; the consumer-facing Abao app entered its own limited test ~June 16, 2026, and Abao ("Aobao") opened *public* (no invite code) testing on **July 2, 2026** on iOS/Android. Reported scale: **>10,000 services already adapted** (government, transport, daily life), on a base of ~1bn Alipay MAU.
- **Why structured this way (and what it reveals):** This is the **B2B ecosystem-enablement piece**, deliberately separated from the consumer front-end. Ant is not asking merchants to rebuild for AI — it is wrapping the **existing mini-program estate** (the moat WeChat and Alipay spent a decade building) into agent-callable tools. The framing "signaling FinTech's pivot from blockchain to AI" is source editorializing (Connecting the Dots), not Ant's claim — discount it. The real move: turn the mini-program directory into the **tool/skill catalog for an agent**, so Abao has supply on day one rather than an empty marketplace.
- **De-PR caveat:** "invite-only testing" = **announced + piloting, not live at scale**. No disclosed monetization terms, no partner tool counts beyond the aggregate "10,000 services," no take-rate for AI-routed transactions. "AI-callable" is a capability, not adoption.

## [1] Competitors / peers
Direct, near-simultaneous move by **WeChat/Tencent**: on ~June 2 WeChat internally tested an AI agent that invokes mini-programs; **June 8 it published technical specs** for connecting mini-programs to AI, with **JD.com, Meituan, Didi** announcing integration immediately, plus a developer plan (1bn token credits, free cloud dev, reduced fees). Both super-apps are explicitly **counter-attacking ByteDance's Doubao** (~300m MAU but <RMB 1m/day revenue; testing paid tiers ~68/200/500 yuan). Externally, this mirrors Western agentic-commerce rails — **OpenAI's Agentic Commerce Protocol, PayPal+Perplexity/ChatGPT, Mastercard Agent Pay, Visa Intelligent Commerce, Worldpay/Checkout.com MCP servers** ([[OpenAI publishes Agentic Commerce Protocol documentation]], [[PayPal integrates Mastercard Agent Pay and comes to ChatGPT]]).
- **Why the lay of the land is this way (2nd order):** The battle is over **who owns the AI traffic entry point**. Doubao has the users but **must build monetization and a merchant graph from scratch**; Alipay/WeChat already own the payment rail + mini-program supply, so their agent monetizes the *first* time a user transacts. The winner is whoever converts an existing distribution moat into agent supply fastest — hence both racing to wrap mini-programs within days of each other. Alipay's structural edge over WeChat here: it already runs the **payment + AI Pay/Token Pay rail** ([[Alipay launches full-stack AI Pay payments platform]]), so the loop from "agent surfaces service" → "agent pays" is closed inside one house.

## [2] Company history / fit
Consistent, dated trajectory, not opportunism:
- 2024 Inclusion Conf (Shanghai): **Zhixiaobao** AI life assistant unveiled, built on Ant's **Bailing** foundation model (finance/health/life focus); later spun into a standalone assistant app.
- Apr 2026: **AI payment processing product** for businesses/OPCs ([[Alipay expands AI Pay to support autonomous agents]]).
- Feb 2026: AI Pay first AI-native payment product past **100m users**, **120m tx in one week** ([[Alipay AI Pay exceeds 120 million transactions in week]]).
- May 26–27, 2026: full-stack AI Pay + **AI Wallet + Token Pay**, 300m cumulative tx; PR already flagged "developing a new AI-driven open platform by integrating AI agents" ([[Alipay launches full-stack AI Pay payments platform]]).
- Jun 15–17, 2026: Abao consumer app testing / "AI agent interface" ([[Ant Group tests AI agent interface inside Alipay]], [[Alipay unveils AI agent upgrade Ah Bao]]).
- Jul 2, 2026: Abao public test. Jul 7–8: **AI Open Platform** developer beta (this note).
- **Why Ant acts this way:** Post-2020 IPO halt / regulatory reset, Ant is reframed as an **AI + tech company, not a fintech that lends**. Rebuilding Alipay around an agent is both a growth narrative and a **regulatory-safe** one (services/AI, not consumer credit). The Open Platform monetizes the moat it already has (mini-programs + rail) rather than betting on model supremacy.

## [3] Novelty / value-add / traction
- **What's genuinely new:** the **developer-facing tool-wrapping platform** — not the consumer Abao app (covered in June), not AI Pay (covered May). This is the piece that populates the agent with third-party supply. It is the Chinese analog of an **MCP-server / agent-tooling standard**, but bundled with the payment rail and 1bn-user distribution.
- **Traction reality:** the only hard number is **"10,000 services adapted"** — but many are Alipay's own first-party services; **no disclosed count of external ISV tools live, no agent-routed GMV, no monetization terms.** Consumer Abao is in *public test* (real signal) but not GA. So: **capability + early supply, adoption unproven.**
- **Who captures the margin (2nd order):** Whoever **owns the agent + the rail** captures it. Unlike the Ramp case (where Visa/MA own the rail so the AI layer risks being a "dashboard"), **Ant owns both the agent and AI Pay/Token Pay** — so it is positioned to be *"the one who pays,"* not just a router. The risk that breaks the multiple: if merchants integrate their tools into *multiple* agents (Alipay + WeChat + Doubao), the tool layer commoditizes and value shifts back to whoever owns **consumer default + payment**, which favors the incumbent rail — again Alipay.

## [4] What's next / market sentiment
- Path: invite-only dev beta → broader ISV onboarding → Abao GA; monetization likely via **pay-per-use / AI payment processing** ([[Alipay launches full-stack AI Pay payments platform]] terms) and eventual take-rate on agent-routed transactions.
- Sentiment: framed as **Alipay's "biggest transformation in two decades"** (SCMP/Pandaily). Market skeptical on agentic monetization broadly — WeChat's agent launch was met with "the market isn't buying it," and Doubao's revenue is thin — so **execution/adoption, not announcements, is the gate.**
- Risks: (1) menu-driven super-app habits are sticky — conversational UX may underperform; (2) regulatory scrutiny of dominant payment platforms in China ([[China broadens oversight of dominant payment platforms]]) could constrain data/AI leverage; (3) three-way traffic war (Alipay/WeChat/Doubao) compresses any near-term monetization.
- **Counterintuitive 2nd order:** the more Alipay opens the platform to ISVs, the more it **commoditizes its own mini-program lock-in** (tools become portable across agents) — so the durable moat is not the tool catalog but the **payment rail + consumer default**, which is exactly what Ant is quietly protecting under the AI narrative.

## Verdict
**FRESH.** Related to but NOT a duplicate of the June consumer-app notes ([[Ant Group tests AI agent interface inside Alipay]] / [[Alipay unveils AI agent upgrade Ah Bao]]) — those cover the *consumer* Abao front-end; this is the distinct *developer/ISV supply-side* Open Platform (mini-programs → AI-callable tools). Importance 3/5: strategically significant piece of a major program and a direct WeChat/Doubao competitive event, but announced-not-live, no monetization/adoption numbers, and downstream of the already-covered May AI Pay and June Abao milestones.

## Sources
- Connecting the Dots in Fintech (primary digest item) — https://www.connectingthedotsinfin.tech/r/fc1fae8a
- cryptonomist.ch (enterprise beta) — https://en.cryptonomist.ch/2026/07/07/alipay-ai-platform-beta/
- Pandaily — WeChat/Alipay mini-programs into AI skills vs Doubao — https://pandaily.com/wechat-alipay-mini-program-ai-skills-jun2026
- SCMP — "Ni hao, Ah Bao": Alipay AI-agent overhaul vs Tencent/ByteDance — https://www.scmp.com/tech/big-tech/article/3357307/
- aibase — Abao public testing July 2 — https://news.aibase.com/news/29330
- Alipay full-stack AI Pay / AI Wallet / Token Pay (Business Wire) — https://www.businesswire.com/news/home/20260526337824/en/
- aibase — Zhixiaobao / Maxicaicai / AI Health Manager — https://www.aibase.com/news/11563
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Live or announced?** It is invite-only beta — how many *external ISV* tools are actually live, versus Alipay's own 10,000 first-party services counted to pad the number? (open — only aggregate disclosed)
2. **Monetization:** what is the take-rate / fee model for agent-routed transactions? Pay-per-use is mentioned for AI Pay processing, but no terms for the Open Platform itself. (open)
3. **Duplicate check:** is this the same event as June's Abao app testing? No — June = consumer front-end; July = developer/ISV supply-side platform. Distinct facet, same program. (fresh)
4. **Who captures the margin?** Ant owns both agent + AI Pay/Token Pay rail — does it become "the one who pays" or just a router? Structurally it owns the rail, unlike Ramp/Visa-MA dynamics. (analysis: favorable to Ant)
5. **Portability risk:** if merchants wrap the same mini-program tools for WeChat and Doubao too, the tool catalog commoditizes — what then is the durable moat? (rail + consumer default, not tools)
6. **Timing vs WeChat:** WeChat published mini-program-to-AI specs June 8 with JD/Meituan/Didi; is Alipay ahead or catching up on the developer platform? (roughly parity / weeks apart; Alipay's edge is the integrated payment rail)
7. **Consumer adoption:** Abao went public-test July 2 — any DAU/retention signal, or is conversational UX losing to sticky menu habits? (open; "market isn't buying it" sentiment on WeChat's agent)
8. **Regulatory overhang:** does China's oversight of dominant payment platforms constrain how Ant leverages AI + data across the platform? (open risk)
9. **Foundation model dependency:** platform rides on Ant's Bailing model (Zhixiaobao lineage) — is model quality a differentiator or does supply/distribution dominate? (distribution dominates)
10. **First-party bias:** will Alipay's own services get preferential surfacing in Abao over third-party ISV tools, undermining the "open" claim? (open — self-preferencing risk)
11. **GMV/tx attribution:** the 300m AI Pay tx and 120m/week figures predate this platform — none are attributable to the Open Platform yet. (no traction number for this launch specifically)
12. **"Pivot from blockchain to AI" framing:** is that Ant's claim or source editorializing? (source editorializing — Connecting the Dots, not Ant)
13. **Downside trigger:** what breaks the thesis? Slow ISV onboarding + no monetization terms + three-way traffic war compressing economics.
14. **Fraud/liability:** who bears liability for an agent-executed erroneous transaction across a third-party tool? (open — Agentic Commerce Trust Protocol exists but liability unstated)

**Importance: 3/5 — rationale:** Strategically meaningful, distinct supply-side component of a flagship AI overhaul and a direct competitive event vs WeChat/ByteDance in the world's largest agentic-commerce market. Capped at 3 because it is invite-only/announced-not-live, discloses no monetization or external-adoption numbers, and sits downstream of the already-covered May AI Pay platform and June Abao app milestones.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-09]] (2026-07-09).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce in China's super-apps: the value shift is from the payment "last step" to the AI-agent orchestration layer that plans and executes tasks (search → order → pay) inside a single chat window. Size/growth: no clean TAM figure is publicly sourced for "agentic payments"; Alipay's own traction is the best proxy — AI Pay passed 100M users by Feb 2026 (**IR: primary**, "Alipay AI Pay and AI Health App AQ Each Surpass 100 Million Users", Ant Group, 2026-02-23, antgroup.com/en/news-media/press-releases/1771812000000) and 300M cumulative transactions by late May 2026 (businesswire, 2026-05-26). Structure: highly consolidated at the top (three-to-four-way race — Alipay/Ant, Tencent/WeChat, ByteDance/Doubao, Alibaba/Qwen); barriers are distribution (1B+ MAU installed base), a captive payment rail, and a mini-program supply base — not model quality. Drivers + "why now": (1) the agentic-commerce inflection — rivals racing to make AI agents the primary UI (Qwen linked to Taobao 2026-05-11; Doubao agents on Douyin; WeChat testing an OpenClaw/ClawBot agent since 2026-03-22); (2) a China-specific regulatory headwind — the Interim Measures on Anthropomorphic AI Interaction Services take effect **2026-07-15**, forcing ByteDance's Doubao and Alibaba's Qwen to disable personalized/humanlike AI agents (SCMP/TechNode, 2026-07). The AI Open Platform's invite-only, enterprise-developer framing lands squarely in this tightening window.

**Competitive landscape.** Sector KPIs: MAU / installed base, agent-attach (share of users on the AI surface), transactions per agent, and merchant/tool supply (mini-programs converted to AI-callable tools). Distribution — not model MAU — is Alipay's edge: Alipay has ~1B MAU vs standalone-assistant MAU of Doubao ~345M, Qwen ~166M, Tencent Yuanbao ~57M (QuestMobile, Q1 2026). Recent moves: Alipay full-stack AI Pay + AI Wallet + Token Pay (2026-05-26); "Ah Bao"/Abao agent upgrade with 10,000+ services (2026-06-17); consumer AI-app limited testing (~2026-06-16); **AI Open Platform invite-only beta (2026-07-07)** turning merchants' existing mini-programs/APIs into AI-callable tools without a rebuild. Basis of competition: distribution + payment-rail control + tool supply, not raw model performance. Protagonist's position: **ahead on distribution and on the payment layer, catching up on the model/agent layer** (analysis) — Doubao/Qwen have larger AI-assistant MAU, but Alipay owns the rail and, post-2026-07-15, faces less anthropomorphic-agent regulatory drag than the consumer chatbots. Moat: network effects (1B users ↔ 80M merchants) + switching costs on the rail (analysis).

**Comps & multiples.** Ant Group is private; use it as a valuation anchor via disclosed figures. Ant net profit ~$5.3bn on ~$25bn revenue (2024; Fintech Inside/Statista, cited via secondary — treat as approximate), profit +10% YoY in the year to 2025-11 (Bloomberg, 2025-11-25); private valuation ~$103bn (2025, stockanalysis.com secondary). Implied P/E on secondary figures = `$103bn / $5.3bn ≈ 19.4x` (analysis; both numbers are secondary/estimated, not audited filings → treat as indicative, not a hard multiple). Alibaba owns ~32.65% of Ant (Ant IPO prospectus) and books ~$381m of Ant profit-share into Alibaba (retaildive), so Ant/Alipay is partly reflected via BABA. No listed pure-play agentic-payments comp with a clean multiple → EV/Revenue and EV/EBITDA = no data. Internal comps (base): [[Alipay launches full-stack AI Pay payments platform]] (2026-05; 300M tx, AI Wallet/Token Pay), [[Alipay unveils AI agent upgrade Ah Bao]] (2026-06), [[Ant Group tests AI agent interface inside Alipay]] (2026-06, Bloomberg), [[Alipay AI Pay exceeds 120 million transactions in week]] (2026-02), [[Alipay extends AI Pay agent shopping to Taobao]] (2026-05), [[This Week in Fintech Conversational AI drives China's agentic payments]] (2026-03). Flag: valuation is indicative only — all figures secondary, so "distribution not computed, qualitative comparison."

**Risk flags.**
1. **Regulation (concentration + timing).** China's anthropomorphic-AI rules (2026-07-15) already force rivals to disable personalized agents; the same regime can constrain how "conversational" Ah Bao/Abao may be. Invite-only enterprise framing looks partly defensive → execution and feature scope hostage to a moving regulatory line.
2. **Adoption ≠ announcement (de-PR).** "AI-callable tools" and 300M cumulative transactions are supply/announcement metrics; Alipay is silent on agent-driven revenue, take-rate on agent transactions, and fraud/liability allocation when an agent transacts wrongly → the monetization and risk economics are unproven.
3. **Disintermediation of the payment layer.** If model owners (Doubao/Qwen) or a protocol (Google AP2, Visa/Mastercard agentic tokens, ACP) become the default agent surface abroad, Alipay's rail advantage is China-bounded; outside China the agentic-payment standard is being set by Visa Trusted Agent Protocol, Mastercard Agent Pay and PayPal-on-ACP, not Alipay.

**What this changes (idea-lens).** This is a platform land-grab, not a re-rating: whoever converts the most mini-programs into AI-callable tools fastest controls China's agent-commerce OS (analysis). Falsifiable thesis — Alipay's distribution + rail control lets it out-scale model-first rivals (Doubao/Qwen) on agent transactions within 12 months. Trigger to watch: disclosed agent-driven transaction/GMV or tool-count figures at the next Ant conference; what would break it — regulators forcing the AI surface back behind a menu, or a model-owner default-agent lock-in that bypasses Alipay's rail.

Sources: https://en.cryptonomist.ch/2026/07/07/alipay-ai-platform-beta/ · https://www.scmp.com/tech/big-tech/article/3357307/ni-hao-ah-bao-chinas-alipay-gets-ai-agent-overhaul-challenge-big-tech-rivals · https://www.businesswire.com/news/home/20260526337824 · https://www.antgroup.com/en/news-media/press-releases/1771812000000 · https://technode.com/2026/07/06/bytedances-doubao-and-alibabas-qwen-to-shut-down-ai-agent-features-on-july-15/ · https://www.scmp.com/tech/big-tech/article/3355651/tencent-shares-jump-expectations-ai-agent-within-wechat-super-app · https://www.bloomberg.com/news/articles/2025-11-25/jack-ma-backed-ant-s-profit-grew-10-after-ai-global-expansion · https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings context — Ant Group is PRIVATE (no filed standalone results). Read via Alibaba's equity-method income (Alibaba holds ~33% of Ant Group), Alibaba FY2026 20-F/6-K (year ended 2026-03-31), plus Ant Group's own operating disclosures. The news itself (AI Open Platform beta) is `type/product`, NOT an earnings release — figures below are the closest disclosed financial read on the entity behind the product.

**Verdict (headline read).** No standalone Ant Group print (private) — but the proxy read is a MISS/deterioration on profitability: Alibaba's share of results of equity-method investees (dominated by Ant Group) was a **loss of RMB685mn (US$99mn) in the March quarter FY2026, vs a +RMB354mn profit a year earlier** (a swing to loss), and **RMB2,785mn (US$404mn) for full FY2026, −53% YoY** (vs RMB5,966mn FY2025). Alibaba explicitly attributes the drop in its share of Ant's profit to Ant's own **"increase in investments in new growth initiatives, including user growth, and technologies"** — i.e. the AI build-out (AI Pay, AQ, the AI Open Platform / Abao) is being funded through the P&L. Ant is buying AI share at the cost of near-term profit.

**Key figures (with growth).**
- Alibaba share of equity-method investees (Ant-driven): **US$404mn FY2026, −53% YoY** (RMB2,785mn vs RMB5,966mn); Mar-Q FY2026 **loss RMB685mn / US$99mn vs +RMB354mn PY** — swing to loss.
- No standalone Ant Group revenue / net-income / TPV disclosed for the period (private; no filed results) — **"no data"** on a full P&L.
- Ant operating traction (Ant/Alipay press disclosures, not audited financials): **AI Pay >100mn users by Feb-2026** and **>120mn transactions in a single week (Feb-2026)**; **AQ (AI health app) >100mn users** at CNY-2026; Alipay **"Tap!" NFC users >100mn** (2025). These are user-growth metrics, not revenue.

**By segment / driver.** The single driver of the equity-method deterioration named by Alibaba is Ant's step-up in investment (user growth + AI/technology). No margin/segment split is public for Ant. The AI Open Platform (this note) sits inside that spend: it converts merchants' existing mini-programs / APIs into AI-callable tools plugged into Abao (Alipay's conversational agent), shifting the model from "service as app" to "service as conversation." Monetization signals disclosed: **Token Pay** (subscriptions, token top-ups, micro-transactions via agent frameworks) and a developer program with **token incentives + zero payment-processing fees** — i.e. subsidized adoption first, monetization deferred.

**vs expectations / prior period.** No public consensus exists for a private issuer → assess vs prior year only. Directionally clear: equity-method contribution **swung profit→loss QoQ-basis (Mar-Q)** and **−53% for the year**. Prior-year FY2025 share was RMB5,966mn. Ant's earlier profit had already been depressed (a widely-reported ~92% quarterly profit drop in the 2023–24 regulatory-overhang period). So this is deceleration on an already-reset base — [UNSOURCED] for any exact Ant net-income figure.

**Guidance / forward.** None — Ant is private, gives no guidance. Independent read (analysis): the equity-method loss is a *deliberate* investment cycle, not demand collapse; Alibaba frames it as Ant funding user/tech growth. Expect continued suppressed near-term equity-method contribution while the AI Open Platform + AI Pay + Abao land-grab runs; monetization (Token Pay take-rate, agentic-commerce GMV) is the swing factor for a profit recovery, and it is not yet quantified.

**Thesis-flags.**
1. **Profit is being consumed to fund AI (fact→why).** Alibaba names Ant's "user growth and technologies" investment as the cause of the −53% equity-method drop → the AI Open Platform / Abao / AI Pay push is a cost center today, not yet a profit center → second-order: near-term drag on Alibaba's reported net income too (Ant is a non-controlling equity stake), and Ant's next IPO/valuation narrative hinges on turning this spend into agentic-commerce monetization.
2. **Adoption is real but pre-monetization (de-PR: announced vs live).** AI Pay >100mn users / >120mn weekly transactions is genuine live traction — but the AI Open Platform is **invite-only beta** and the developer economics are **zero-fee + token subsidies**, so the "monetization" is deferred by design. Watch for a disclosed take-rate on Token Pay before crediting revenue.
3. **Competitive forcing function (why it matters).** The pivot "service as app → service as conversation" is an explicit counter to WeChat and to AI-native assistants (Doubao) → Ant is defending the mini-program moat by making it AI-callable → if it works, it re-entrenches Alipay's distribution; if it doesn't, the investment that cut this year's profit yields little.
4. **Data quality flag.** All financials here are a *proxy* (Alibaba's ~33% equity-method line), not Ant's own audited results. Any single-quarter Ant net-income number in the press is [UNSOURCED] / not directly filed.

Sources: Alibaba FY2026 6-K / earnings release (year ended 2026-03-31), <https://www.sec.gov/Archives/edgar/data/0001577552/000110465926060224/tm2614494d1_ex99-1.htm> · Alibaba 20-F FY2026 (filed 2026-05-20), <https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/baba-20260331.htm> · Alibaba "March Quarter 2026 and Fiscal Year 2026 Results" (BusinessWire), <https://www.businesswire.com/news/home/20260512841182/en/Alibaba-Group-Announces-March-Quarter-2026-and-Fiscal-Year-2026-Results> · Ant/Alipay AI Payment >120mn tx (BusinessWire), <https://www.businesswire.com/news/home/20260213770962/en/> · Alipay AI Wallet / Token Pay (BusinessWire/SCMP), <https://www.businesswire.com/news/home/20260526337824/en/> · Ant Group press (AI Pay & AQ >100mn users), <https://www.antgroup.com/en/news-media/press-releases/1771812000000> · Ant standalone net income for the period: **no data** (private, no filed results).
<!-- /enrichment:earnings_review -->
