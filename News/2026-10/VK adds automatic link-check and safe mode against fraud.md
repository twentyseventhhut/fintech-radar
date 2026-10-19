---
title: "VK adds automatic link-check and safe mode against fraud"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/vk
  - industry/fraud-risk
  - region/ru
  - type/product
sources:
  - https://vk.company/ru/press/releases/12436
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sc178b6bd
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# VK adds automatic link-check and safe mode against fraud

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Внедрил автоматическую проверку ссылок при переходе по ним и включение безопасного режима для пользователей, столкнувшихся с потенциальными мошенническими угрозами

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://vk.company/ru/press/releases/12436>

## Контекст

<!-- enrichment:context -->
## [0] What exactly happened (de-PR'd)

VK's Max messenger (press service, 13 Oct 2026) switched on two in-app safety features: (a) an **automatic link check** — on tap, an automated system scans the URL for threats and pops a warning before the user leaves the app; (b) an auto-triggered **"Safe mode"** — a 24-hour lockdown where only address-book contacts can call the user or add them to chats, toggleable in Settings → Security and self-disabling after 24h. De-PR'd: this is a **client-side nudge/UX layer**, not a new fraud-detection engine. Max already runs number verification via Kaspersky and anti-fraud tech via Sber plus a 24/7 Security Center; link-check and safe-mode are the user-facing surface on top of that stack. No numbers disclosed: no block rate, no false-positive rate, no catalog/source of the "dangerous link" verdict, no adoption figures.

**Why structured this way:** Max is the state-blessed "national messenger" (VK-built; by law from Sep 2026 banks and large platforms must use domestic messengers, and officials were pushed onto Max). Its credibility problem is precisely that it is seen as a surveillance/spyware vector, not a trust tool. Shipping visible anti-fraud UX is a **trust-and-legitimacy play** against Russia's record cyber-fraud wave — i.e. positioning Max as the "safe" alternative to Telegram/WhatsApp as regulators squeeze foreign apps. The feature is cheap to build and high-signal to cite in policy terms, which is why it leads the PR.

## [1] Competitors / peers

- **WhatsApp** (2026): on-device ML "Scam Alert" banner for non-contact senders; device-linking scam checks with location flags — comparable *proactive* warning UX, shipped globally.
- **Telegram**: report-a-message, in-app reporting; weaker *automatic* link scanning; Mini-Apps remain a phishing surface. Max's auto-link-check is arguably ahead of Telegram here.
- **Domestic adjacent**: [[MTS Secretary learns to answer calls in subscriber's voice]] (call-screening AI) and the regulatory [[Bank antifraud signals to be shared with digital platforms]] attack the same fraud problem from telco/bank angles.

Position: **parity-to-catching-up on UX** with WhatsApp; the differentiator is not the feature but that Max is mandated/pushed by the state, so distribution — not product edge — is the moat.

## [2] Company history / fit

Fits VK's 2026 Max push: public channels to 530K (+58% q/q), 355M subscriptions — see [[VK grows Max public channels to 530K in Q3 2026]], plus ads to 1K-sub channels and polls/recommendations. VK is racing to make Max a full platform (chat + channels + ads + gov services + hotel check-in). **Why act now:** as Telegram/WhatsApp face blocking and Max inherits sensitive flows (banking alerts, gov services), the single biggest adoption blocker is trust; anti-fraud UX is the logical next brick after the content/ads build-out, timed to the "Antifraud 2.0" regulatory wave (effective Sep 2026).

## [3] Novelty / value-add / traction

Not novel globally (WhatsApp/others ship similar). Novelty is **local + distribution**: first-party auto-link-check + auto safe-mode inside Russia's mandated messenger. **Value-add is real only if** the link-threat verdict is backed by a credible, broad threat feed (Kaspersky/Sber signals) and the false-positive rate is low — neither disclosed. Traction = **zero evidence**: announcement only, no block counts, no user-adoption, no independent efficacy test. The "safe mode" is behaviorally sound (cuts the cold-call/add-to-chat vector that drives Russian social-engineering fraud) but opt-outable and time-boxed, so impact depends on default triggering logic that isn't specified.

## [4] What's next / market sentiment

Expect Max to fold in bank/telco anti-fraud signal-sharing (cf. [[Bank antifraud signals to be shared with digital platforms]]) and tie into the Gosuslugi "red button" and single IMEI/anti-fraud databases under Antifraud 2.0. **Why the market goes this way:** Russia's fraud losses are a political issue, foreign apps are being squeezed, so the state wants its own messenger to be demonstrably "safe" — safety features are as much compliance/legitimacy theater as protection. **Counterintuitive second-order:** concentrating communications into one state-controlled app may *raise* systemic risk (single honeypot, single point of failure/abuse) even as per-message link-safety improves. Risk: skeptics frame Max itself as the threat vector, so anti-fraud UX may not move the trust needle.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Top challenge / red-team questions

1. **What powers the "dangerous link" verdict** — Kaspersky/Sber threat feed, a URL blocklist, or heuristics? Breadth and freshness decide efficacy. **Open** (not disclosed).
2. **False-positive rate?** Over-blocking legitimate links (banks, gov) erodes trust fast. **Open.**
3. **Is safe mode auto-triggered or user-initiated?** PR says "auto-enabling for users facing threats" but the trigger logic is unspecified — this is the whole value. **Open / partially open.**
4. **Any block/efficacy numbers?** None disclosed — announcement only, no traction. **Open.**
5. **Is this genuinely new vs already-live Max security (Kaspersky number check, Sber anti-fraud, Security Center)?** It is a new *UX surface* over an existing stack, not a new engine. **Answered.**
6. **Does it beat WhatsApp/Telegram on mechanism?** Roughly parity with WhatsApp's Scam Alert; ahead of Telegram on auto-link-scan. Moat is distribution/mandate, not product. **Answered.**
7. **Who is silent on liability?** If a scanned link is passed as "safe" and defrauds a user, who is liable? Not addressed. **Open.**
8. **Does safe mode (contacts-only 24h) actually block the dominant fraud vector?** It cuts cold calls/add-to-chat — a real Russian social-engineering path — but is opt-outable and time-boxed. **Partially answered.**
9. **Privacy cost of link scanning** — does URL analysis send browsing data to VK/state? Given Max's surveillance reputation, this could deter adoption. **Open (analysis).**
10. **Was it live on announcement day or rolling out?** No rollout timeline given; "launched" is a PR claim, not verified adoption. **Open.**
11. **How does it tie to Antifraud 2.0 / bank signal-sharing?** Likely future integration (red button, IMEI DB) but not announced here. **Open / hypothesis.**
12. **Is this freshness real or a re-report?** No prior VK/Max note covers link-check or safe mode; nearest VK notes are channels/ads/polls — distinct features. **Fresh.**
13. **Does the state mandate make adoption meaningful?** Forced distribution inflates usage; "safety feature in a mandated app" is weaker signal than voluntary adoption. **Answered (analysis).**
14. **Second-order systemic risk?** Centralizing comms into one state messenger raises honeypot/single-point-of-abuse risk even if per-link safety rises. **Analysis.**
15. **Does anti-fraud UX move Max's trust needle at all**, given it is widely framed as spyware? Core doubt on the whole play. **Open (analysis).**

**Importance: 2/5 — rationale:** A genuine but incremental, globally-common product feature (parity with WhatsApp) on a single regional messenger, shipped with zero disclosed efficacy/adoption numbers and no new fraud-detection engine. Weight comes almost entirely from Max's state-mandated distribution and the Russian anti-fraud regulatory context, not from product novelty. Fresh, but low-substance for a fintech lens.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Anti-fraud / scam-protection inside messaging apps, Russia. The feature (automatic link-checking on tap + a 24h "safe mode" for targeted users) sits in VK's Max messenger, announced 2026-10-13 (per iz.ru). Russia's scam problem is large and phone/messenger-led: of ~RUB 300 bn (~$3.85 bn) swindled from Russians in 2024, 45.6% of contact was via calls/SMS and 15.7% via messaging apps (per NBC/Moscow Times citing Russian data); cases reportedly declined in 2025 but messengers remain a primary vector. "Why now": (1) Max is now the state-backed "national messenger," mandatory pre-install on phones sold in Russia since Sep 2025 and granted social-network status 2026-03-18 — scale makes it a high-value target and raises the political cost of visible fraud on-platform; (2) link-based phishing is the dominant attack — Max + F6 jointly flagged 2,550+ phishing/fraud/malicious sites/pages in Jul–Aug 2026 alone (per www1.ru / iz.ru). Structure: consolidated, state-steered — Max is the designated platform, so the "market" here is a compliance/trust moat, not a contestable commercial segment.

**Competitive landscape.** Platform KPIs that matter here: DAU/MAU (exposure surface), share of blocked malicious links, time-to-block. Max scale: 107 mn registered users (Mar 2026), ~70–77 mn DAU, ~1 bn messages/day (per www1.ru / vk.company). Security is vendor-layered rather than built fully in-house: F6 (Digital Risk Protection, AI fake-site detection) supplies the external-URL/phishing feed; Kaspersky does automatic number verification; Sber provides anti-fraud detection tech. Basis of competition vs global peers is distribution + mandate, not product: Meta Messenger shipped comparable scam-warning features in 2026, Starling Bank launched an AI scam-spotting tool (see internal comps), so link-checking/safe-mode is table-stakes catch-up, not differentiation. VK/Max position: catching up on product (Meta had similar), but ahead on reach by state fiat. Moat = distribution mandate + regulatory alignment (analysis), not proprietary anti-fraud tech (that is licensed from F6/Kaspersky/Sber).

**Comps & multiples.** No deal/round/valuation in this news — it is a product release, so no transaction multiple to compute. Parent VK (MOEX: VKCO) FY2025 IFRS (per Interfax / Moscow Times / vk.company 12M 2025 release): revenue RUB 160 bn (+8% YoY), adjusted EBITDA RUB 22.6 bn (14% margin, +17 p.p., vs negative 2024), net loss RUB 25.4 bn (6th straight annual loss, narrowed from RUB 95.5 bn). Max sits in the "Social platforms and media content" segment (RUB 109.8 bn, +5%) and is not separately monetised — anti-fraud is cost/retention, not revenue. EV/Revenue, EV/EBITDA not computed: EV (net debt, market cap on the date) not sourced from a free feed → [UNSOURCED]; a RU-listed, sanctioned, loss-making name is also not comparable to the Western fraud-vendor peers below. Internal comps (fraud/scam-protection precedents, qualitative — not valuation-comparable to a state messenger): [[Starling Bank launches AI tool for customers to spot purchase scams]], [[Ant International launches AI SHIELD risk toolkit]], [[Resistant AI raises $25M Series B against financial crime]], [[Plaid launches Ti2 next-generation Trust Index]]. Distribution not computed — qualitative comparison only.

**Risk flags.**
1. Vendor dependence / disintermediation of the moat: the actual detection (F6 phishing feed, Kaspersky number-check, Sber anti-fraud) is licensed, not owned — VK captures the user relationship but a third-party stack owns the fraud-signal layer; feed quality/cost and vendor continuity are outside VK's control.
2. Announced vs live/efficacy gap: "automatic link-check + 24h safe mode" is a detection/warning layer, not blocking of social-engineering (code/PIN/linked-device theft), which Russian-nexus actors use against WhatsApp/Signal (per FBI/CISA 2026). De-PR: no disclosed block rate, false-positive rate, or coverage — unverifiable efficacy.
3. State/trust concentration: Max's growth is mandate-driven (forced pre-install, "national messenger"); independent analysis (interseclab.org) frames it as a state-mandated app — security features double as a trust-restoration play, so adoption and the "anti-fraud" framing are politically, not commercially, load-bearing.

**What this changes (idea-lens).** For the sector: in-messenger link-scanning is converging to table-stakes (Meta, Max within one 2026 cycle) — differentiation shifts to block-rate transparency and covering social-engineering flows that warnings don't stop (analysis). Falsifiable thesis: if Max/F6 publish a measurable drop in on-platform fraud contact (the 15.7%-of-attacks messenger share) over the next 2–3 quarters, the mandate-trust bet is working; trigger to watch — a published efficacy/block-rate metric or a 9M/FY2026 VK release quantifying Max fraud outcomes. What breaks it: continued reliance on warnings while account-takeover/linked-device phishing keeps growing.

IR grounding: VK FY2025 IFRS — revenue RUB 160 bn, adj. EBITDA RUB 22.6 bn, net loss RUB 25.4 bn (vk.company 12M 2025 release; corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf). Latest IR doc in base: Smart-Lab Conf 2026 SPb investor presentation (2026-06-01, corp.vkcdn.ru/media/files/vk_ir_smart-lab_2026_spb.pdf). irdb/semsearch 402 (OpenRouter credits) — web-sourced.

Sources: https://en.iz.ru/en/2183453/2026-10-13/max-started-warning-users-when-they-click-suspicious-links · https://www1.ru/en/news/2026/09/10/vygliadit-kak-nastoiashhii-sait-maks-i-f6-nasli-tysiaci-mosenniceskix-kopii.html · https://interseclab.org/research/max/ · https://www.themoscowtimes.com/2026/03/19/vk-logs-6th-straight-annual-loss-despite-revenue-growth-a92270 · https://interfax.com/newsroom/top-stories/116698/ · https://vk.company/en/press/releases/12255/ · https://vk.company/en/press/releases/12199/ · https://www1.ru/en/news/2026/03/29/za-odin-god-v-messendzere-max-zaregistrirovalis-107-millionov-polzovatelei-sredi-nix-est-inostrancy.html · https://www.nbcnews.com/tech/security/signal-whatsapp-users-face-russian-phishing-push-dutch-warn-rcna262533
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**No full earnings report in the news** — this is a product/trust-&-safety announcement (automatic link-check + safe mode against fraud), not a financial result. VK is IR-covered, so the latest reported figures are attached as financial context only (CONTEXT-ONLY, not a print tied to this item).

**Financial context (VK's own filings / press).** Most recent print: **Q2 2026** (reported 2026-08-14) — revenue **RUB 43.5bn (+17% YoY)**, of which online advertising **RUB 26.7bn (+14% YoY)**; EBITDA **RUB 7.6bn (+41% YoY)**; net profit **RUB 0.328bn** — VK's first profitable quarter since end-2022. **H1 2026:** revenue **RUB 81.04bn (+11.7% YoY, from RUB 72.567bn)**; EBITDA **RUB 14.0bn (+34% YoY)**; net loss **RUB 3.846bn**, narrowed from RUB 12.67bn in H1 2025. **FY 2025** (audited IFRS, filed 2026-03-19): revenue **RUB 160bn (+8% YoY)**; adjusted EBITDA **RUB 22.6bn**, swinging from **negative RUB 4.9bn in 2024** — both ahead of Interfax consensus (RUB 158.9bn revenue / RUB 21.6bn EBITDA). 9M 2025 reference: revenue RUB 111.3bn, adj EBITDA RUB 15.5bn, of which Social Platforms & Media Content RUB 77.0bn; VK Tech RUB 10.7bn (+39% YoY); education RUB 5.4bn (+20% YoY); ecosystem & other RUB 20.4bn (+21% YoY).

**Read vs the item.** The anti-fraud link-check and safe mode sit inside the core Social Platforms & Media Content segment (the ad-monetized surfaces + Max messenger) that drives ~70% of revenue and essentially all of group profitability. Trust-and-safety spend is a cost/retention item, not a revenue line — it is not visible in any disclosed figure above and management has not quantified it. The strategic read: with VK having just turned its first quarterly profit in 3+ years on accelerating ad revenue (+14% YoY) and surging EBITDA (+41% YoY in Q2), protecting the user base from fraud churn on Max/VK surfaces defends the exact engagement base that monetization depends on — but it carries no standalone P&L impact in the reported numbers.

**Thesis-flags (context, not driven by this news).** (1) EBITDA inflection is the live thesis — +34% H1 / +41% Q2 with margin expansion suggests the 2022–2024 loss cycle may be ending; watch whether 9M 2026 (due ~Nov 2026, not yet released as of 2026-10-19) sustains the net-profit turn or reverts to loss. (2) Ad revenue deceleration risk — +14% Q2 advertising vs +17% total means non-ad (VK Tech, education) is now the faster grower; a fraud/trust failure on ad surfaces would hit the slower but far larger pool. No FY2026 guidance disclosed in the public press; 9M/Q3 2026 print and any Max monetization update are the next catalysts — [UNSOURCED] on segment detail for 2026.

Sources: VK FY2025 press release 2026-03-19 (drive_url https://corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf) · VK Q3/9M 2025 press release (drive_url https://corp.vkcdn.ru/media/files/ENG_Press_Release_9M_2025.pdf) · Interfax FY2025 (interfax.com/newsroom/top-stories/116698) · akm.ru Q2 2026 · Meduza 2026-08-14 (first quarterly profit). Q3/9M 2026: no data (not yet reported). Trust-&-safety cost impact: not disclosed [UNSOURCED].
<!-- /enrichment:earnings_review -->
