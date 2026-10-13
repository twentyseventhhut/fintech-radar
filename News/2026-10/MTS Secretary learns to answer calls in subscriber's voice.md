---
title: "MTS Secretary learns to answer calls in subscriber's voice"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/mts
  - industry/ai
  - region/ru
  - type/product
sources:
  - https://rb.ru/news/mts-nauchila-avtootvetchik-govorit-golosom-abonenta-funkciya-uzhe-dostupna-chasti-polzovatelej
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sdea3af3f
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# MTS Secretary learns to answer calls in subscriber's voice

> [!info] 2026-10-12 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Научил МТС Секретаря отвечать на звонки голосом абонента — функция пока тестируется на ограниченной группе пользователей

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://rb.ru/news/mts-nauchila-avtootvetchik-govorit-golosom-abonenta-funkciya-uzhe-dostupna-chasti-polzovatelej>

## Контекст

<!-- enrichment:context -->
**[0] What happened (one line).** On 8 Oct 2026, MTS announced "Свой голос" ("Own Voice"), a feature that clones a subscriber's own voice and speech style so the existing "MTS Secretary" virtual assistant answers missed/declined calls in a voice indistinguishable from the user's; it is in limited test and MTS calls it the first such feature on the Russian telecom market. (The aggregated digest line is dated 2026-10-12, but the underlying press announcement is 8 Oct 2026.)

**[1] How it works / the specifics.**
- The user records a short voice sample in the "Мой МТС" (My MTS) app; an AI model extracts individual speech patterns and intonation, then synthesizes replies in that voice when MTS Secretary handles an incoming call the user did not pick up.
- After the call, Secretary already sends the subscriber a transcript + audio recording (via SMS/Telegram) and flags whether the caller was spam or potentially useful (delivery, colleague, relative, appointment reminder, etc.). "Own Voice" only changes the voice layer, not the call-handling logic.
- MTS says the voice recording is stored in a "особо защищённый контур" (specially protected enclave) accessible only to the owner. No third-party access is claimed.
- MTS cites internal analytics that ~30% of Russians would like the autoresponder to speak in their own voice — this is a vendor-supplied demand stat, not independent research.

**[2] Why it matters (business/market framing).**
- MTS Secretary is a scaled, monetizable AI product, not a lab demo: in Q2 2026 MTS reported AI-Secretary-processed calls roughly doubled and 550 million AI-enhanced voice minutes. Voice-cloning is a differentiation/retention and upsell lever on top of that base.
- Call-screening AI is now a standard Russian-operator battleground. MTS joins a crowded field: Tinkoff/T-Bank's "Oleg" (free cross-operator spam defender, trained on 100M+ calls since ~2019-2021), Beeline's AI family assistants (routed ~19.1M suspected scam calls in 2026, personas like grandmother/teen/parent; "736M calls" anti-fraud claim), and Yandex's Alice (the #1 general AI assistant in Russia by Mediascope, ~14.3% usage). MTS's twist — the assistant speaking in *your* voice rather than a generic/persona voice — is the genuinely novel angle here.
- Fits MTS's broader 2026 AI push visible in adjacent same-month items: [[MWS AI opens RESON speech-recognition model evaluation tool]] (ASR benchmarking), [[MTS Link adds Chinese speech recognition and 19-language subtitles]] (speech tech productization), and [[MTS bundles enterprise solutions under MTS CorpTech brand]] (packaging AI for enterprise). The missed-call economics that justify this category are quantified in [[Forbes Russian SMBs lose over 2bn rubles yearly on missed calls]].

**[3] Open questions / what's unverified.**
- No disclosed subscriber count for Secretary itself, and no count for the "Own Voice" test cohort ("limited base").
- No pricing: unclear whether Own Voice stays bundled or becomes a paid add-on (MTS says it "will become an additional feature for all users" later).
- No independent verification of the "30% of Russians" demand figure or of the "first on the Russian market" claim.
- Security model ("specially protected enclave") is asserted, not audited; no detail on consent for the *callers* being recorded, nor on anti-abuse controls preventing cloning of someone else's voice.

**[4] Risk / skeptic's read.** A telecom normalizing consumer-grade voice cloning sits uneasily beside the deepfake-fraud wave MTS itself warns about (МТС has published deepfake-awareness campaigns). Legitimizing "my phone answers in my cloned voice" lowers the public's guard against synthetic-voice scams, and a stored voiceprint is a high-value target even inside a "protected enclave." Compare the privacy backlash around always-listening assistants — e.g. [[Apple begins distributing Siri privacy settlement payments]]. Net: incrementally novel product feature, modest standalone importance, main interest is as a market-positioning signal and a voice-biometrics/privacy bellwether.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. The note title/date says 2026-10-12 but the press announcement is 8 Oct 2026 — is this a late digest pickup of an already-public story (freshness risk)?
2. How many subscribers actually use MTS Secretary, and how large is the "Own Voice" test cohort? ("Limited base" is unquantified.)
3. Is "first on the Russian telecom market" to clone the subscriber's own voice actually true, or just first *among the big three operators*? Beeline already uses AI personas (grandmother/teen) — but those are generic, not the user's voice.
4. Is the "~30% of Russians want their own voice" figure independent, or MTS-commissioned marketing research?
5. Will Own Voice be free/bundled or a paid add-on? Revenue impact is unstated.
6. What exactly is a "специально защищённый контур"? Is the voiceprint encrypted at rest, who holds keys, and is it audited?
7. Do callers consent to being recorded and to talking to a cloned-voice bot? What are the legal implications under Russian personal-data law (152-ФЗ)?
8. What prevents a user from enrolling *someone else's* voice (e.g., uploading a sample of a public figure or family member)? Liveness/anti-spoof controls?
9. Does normalizing consumer voice cloning increase societal vulnerability to deepfake voice fraud — the very threat MTS campaigns against?
10. Is the underlying synthesis MTS's own (Audiogram/MWS AI stack) or licensed? Quality/latency in real-time call conditions is unverified.
11. How does this compare on scale to Tinkoff Oleg (100M+ calls trained, cross-operator, free) — is MTS structurally behind in reach?
12. Any regulator (Roskomnadzor / CBR / FAS) stance on biometric voice data or synthetic-voice disclosure requirements?
13. Is the 550M AI voice minutes / "doubled calls" Q2 2026 stat for Secretary specifically or MTS AI voice overall?
14. Could a stored voiceprint leak enable account takeover elsewhere (voice-biometric banking auth)?
15. Does this story add anything beyond the existing MTS Secretary product, or is it a feature-press-release with limited strategic weight?

**Importance: 2/5** — A genuinely novel but incremental feature (voice-cloning layer on an already-shipping, scaled call-screening product) from a single Russian operator, in test mode, with no disclosed pricing, adoption numbers, or financial impact. Interesting mainly as (a) a competitive-positioning signal in Russia's crowded AI call-assistant market and (b) a voice-biometrics/deepfake-normalization bellwether — not a market-moving or sector-defining event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian call-screening / voice-assistant AI (robo-secretaries, caller-ID + anti-spam) sits atop two secular drivers. (1) Fraud/spam-call surge: Russia has no standalone legal protection of a person's voice (draft Art. 152.3 Civil Code introduced to the State Duma in 2024, not yet passed as of Oct 2026), while globally voice-clone fraud is exploding — deepfake fraud losses reached ~$3.7bn by mid-2026, ~89% of it in the prior 18 months (per StationX compilation; attribute with care — secondary aggregate). (2) Call-economics pressure in RU: the outsourced contact-center market is stalling — +0.2% in 2025 to ₽31bn with voice traffic down 12.1% y/y and operator seats −10%, as traffic shifts to text (+37.5%) (per iKS-Consulting, via Forbes.ru, 2026-07-14) — i.e. voice handling is being automated, not expanded. SMBs separately lose >₽2bn/yr on missed calls (Forbes.ru, 2026-06). Why now: cheap few-shot voice cloning (3 sec of audio ≈ 85% match, per StationX) makes "answer in the subscriber's own voice" technically trivial — MTS is productizing the same tech attackers use, defensively. Structure: consolidated around 3–4 telco/bigtech ecosystems that own the SIM/number layer; barrier = distribution (subscriber base + network-level call interception), not model IP.

**Competitive landscape.** Sector KPIs: active users of the assistant, calls handled/day, spam-classification accuracy, attach/penetration into the subscriber base. Players & basis of competition (ecosystem distribution, not price):
- **MTS "Секретарь"** — virtual secretary: auto-answers missed/declined calls, classifies caller into 20+ categories (spammer / courier / colleague …). New "Свой голос" feature (Oct 2026) makes it reply in the subscriber's cloned voice — MTS claims a first on the RU telco market; test-mode, limited base (per ixbt/CNews/rb.ru, 2026-10-08). Voice sample stored on a "protected contour" as personal data.
- **Yandex "Определитель номера"** (in "Яндекс с Алисой") — AI caller-ID, claims +40% fraud-detection accuracy and 7x faster scoring (10min→1.5min) via 300+ behavioral features; added block-all-unknown-numbers (per Habr/comss, Jan 2026). Caller-ID/blocking, not a voice robot.
- **T-Bank "Олег"** — the incumbent robo-secretary (launched 2021): trained on 110m+ calls, 100+ dialog scenarios, ~100k calls/day; "Фабрика роботов" trolls scammers to waste their time, test-mode to ~500k users (per vc.ru/Forbes).
- **Kaspersky Who Calls, МТС Защитник, bank caller-IDs** — anti-spam caller-ID layer.
MTS position: catching up on the robo-secretary dialog depth vs T-Bank's Олег (5-yr head start, 110m-call corpus), but ahead/first on voice personalization. Moat = distribution/switching cost via the SIM + MWS AI stack (cf. [[MWS AI opens RESON speech-recognition model evaluation tool]] = in-house ASR tooling; [[MTS bundles enterprise solutions under MTS CorpTech brand]] = B2B AI packaging). Not a model moat — a bundling/distribution moat (analysis).

**Comps & multiples.** This is a free consumer feature inside a telco, not a standalone monetized asset — no deal/round/valuation attached, so transaction multiples = no data. Protagonist (parent) valuation anchors, from IR: MTS Group Q1 2026 revenue ₽201.3bn (+14.7% y/y), OIBDA ₽74.7bn (+18.0% y/y), net income ₽7.2bn (+46.4% y/y), net debt ₽451.5bn, net debt/LTM OIBDA 1.6x (MTS Q1 2026 press release, 2026-05-20; drive_url https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf; figures corroborated via ir.mts.ru / smart-lab). OIBDA margin ≈ 74.7/201.3 = 37.1% (analysis). The Секретарь feature is immaterial to these numbers — treat as retention/ARPU-defense, not a revenue line. Internal comps (no valuation, qualitative): [[Forbes Russian SMBs lose over 2bn rubles yearly on missed calls]] (demand-side TAM proxy), [[Forbes Russian outsourced contact-center market stalled in 2025]] (₽31bn CC market being automated away), [[MWS AI opens RESON speech-recognition model evaluation tool]] (ASR capability). EV/Revenue, EV/EBITDA, P/E not computed — equity price/shares-out not sourced here → [UNSOURCED]; leverage at 1.6x is in-line, not stretched.

**Risk flags.**
1. **Voice-cloning / deepfake-fraud dual-use (primary).** Normalizing "reply in your own cloned voice" lowers the social barrier to voice cloning and expands the attack surface — a leaked/replayed voice model is exactly the vector behind the ~$3.7bn global deepfake-fraud loss pool; second-order: regulatory/reputational blowback if a cloned MTS voice is used to defraud the same subscriber. Mitigant claimed (protected-contour storage) is unverified.
2. **Legal/regulatory gap.** No settled RU law on voice as a protected attribute (Art. 152.3 still pending); voice may qualify as biometric personal data — consent/storage rules could tighten and force rework, and liability for a misused clone is undefined.
3. **Competitive catch-up vs disintermediation.** T-Bank's Олег has a 5-yr, 110m-call data lead; Yandex owns the caller-ID funnel inside Алиса. If classification/anti-spam becomes OS- or super-app-native (Yandex/Max), the telco's network-level screening gets disintermediated and Секретарь becomes a commodity retention tool, not a moat.

**What this changes (idea-lens).** For the sector: the frontier is shifting from *screening* (who's calling) to *impersonation-grade response* (answering as you) — personalization, not just classification, becomes the battleground, and every anti-spam vendor now also ships the cloning tech it's meant to defend against (analysis). Falsifiable thesis: this is ARPU/retention defense, not a new revenue stream — watch for MTS disclosing Секретарь MAU/paid-tier or calls-handled/day (as T-Bank does for Олег); absent monetization disclosure within ~2–4 quarters, treat it as a churn-reduction feature. Thesis breaks if MTS packages voice-secretary into a paid B2B anti-fraud SKU under МТС КорпТех (trigger: a priced CorpTech line item). Catalyst to watch: passage of Art. 152.3 (voice-protection law) — would raise compliance cost for everyone and could favor the ecosystem with the cleanest consent/storage story.

Sources: https://rb.ru/news/mts-nauchila-avtootvetchik-govorit-golosom-abonenta-funkciya-uzhe-dostupna-chasti-polzovatelej · https://www.ixbt.com/news/2026/10/08/otdat-svoi-golos-ii-mts-naucil-virtualnogo-sekretaria-otvecat-golosom-abonenta.html · https://www.cnews.ru/news/line/2026-10-08_mts_nauchila_virtualnogo · https://habr.com/ru/news/1018326/ · https://www.comss.ru/page.php?id=16809 · https://vc.ru/services/844430-tinkoff-zapustil-golosovyh-robotov-kotorye-otvlekayut-moshennikov-uderzhivaya-ih-na-linii-kak-mozhno-dolshe · https://www.forbes.ru/tekhnologii/564710-otlozit-trubku-pocemu-kontakt-centry-pocti-ne-rastut · https://app.stationx.net/articles/deepfake-statistics · https://kadr-ai.ru/en/blog/ai-voice-cloning · https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Verdict (headline read).** BEAT · Q1 2026 (reported 2026-05-20): Group revenue RUB 201.3bn (+14.7% YoY) · OIBDA RUB 74.7bn (+18.0% YoY, margin ~37.1%) · net profit RUB 7.2bn (+46.4% YoY) · fintech (MTS Bank) net profit RUB 2.5bn (x2.6 YoY) · no explicit FY2026 revenue/OIBDA guidance given — only a dividend recommendation of RUB 35/share. (The MTS Secretary voice-cloning news is a product release with no financials of its own; this review pulls MTS's own latest filing as earnings context.)

**Key figures (with growth).**
- Group revenue: RUB 201.3bn, +14.7% YoY — driven by mobile and fixed-line, inter-operator business and B2B.
- OIBDA: RUB 74.7bn, +18.0% YoY; margin ~37.1% (analysis: 74.7/201.3), i.e. OIBDA grew faster than revenue → positive operating leverage.
- Net profit: RUB 7.2bn, +46.4% YoY.
- Net debt: RUB 451.5bn; Net debt/LTM OIBDA 1.6x, down 0.2x vs 1Q 2025 — deleveraging despite the high-rate environment.
- Capex: not disclosed in the press release [no data].

**By segment / driver.**
- Fintech (MTS Bank, IFRS): net profit RUB 2.5bn, x2.6 (+~160%) YoY. Net interest income before provisions RUB 14.3bn (+65% YoY); after provisions RUB 6.9bn, x3.7 YoY. Net fee and other non-interest income RUB 4.2bn, +37.9% YoY. Credit-card portfolio RUB 90.3bn, +4.8% YoY. NIM (YTD) 8.1%, +2.3pp YoY. Read: profit surge is driven far more by margin expansion / falling relative provisioning than by loan-book growth (cards +4.8% is modest) — de-PR flag that the x2.6 headline leans on NII mix and reserve dynamics, not volume.
- AdTech vertical: revenue RUB 15.3bn vs RUB 15.0bn a year earlier (~+2% YoY); OIBDA +33% YoY on a mix shift toward higher-margin inventory. Sub-drivers: MTS Ads Premium Video +28%, MarTech +11% (MTS Marketolog AI agent), Getblogger +25%.

**vs expectations / prior period.** No public consensus estimate was retrievable [UNSOURCED]; assessed qualitatively vs prior year. Group growth is broad-based and all three top lines (revenue/OIBDA/net profit) accelerated YoY, with net profit the standout (+46.4%). On the bank, T-Investments analysts rated the Q1 print "moderately negative" despite the x2.6 profit, flagging rising provisioning risk — a signal that the profit quality is debated even as the headline beats. No same-company prior-quarter earnings note exists in the corpus to wikilink.

**Guidance / forward.** No FY2026 revenue or OIBDA guidance issued in the release. Only forward item: management's recommendation of RUB 35/share dividend. Management tone (as framed in the release): confident on diversification (telecom + fintech + AdTech ecosystem). What's left out: no capex outlook, no explicit margin guide, and the bank's provisioning trajectory is not reassured against — the key open question for the fintech thesis.

**Thesis-flags.**
1. Fintech profit quality (MTS Bank net profit x2.6, but loan growth only +4.8% and analysts flag provisioning) → the beat is NII/margin-led, not volume-led → if reserve releases normalize, the x2.6 pace is not repeatable → watch provisioning in subsequent quarters.
2. Operating leverage intact (OIBDA +18.0% > revenue +14.7%) → margin ~37.1% expanding → supports the ecosystem-monetization thesis (voice-AI / AdTech as margin-accretive add-ons, consistent with the MTS Secretary voice-cloning product push).
3. Deleveraging (Net debt/LTM OIBDA 1.6x, −0.2x YoY) in a high-rate regime → reduces balance-sheet risk and protects the RUB 35/share dividend capacity.
4. No FY2026 guidance → forward visibility is low; the market must lean on the dividend signal rather than a revenue/OIBDA frame.

Sources: MTS IR Q1 2026 press release (primary) https://storage.ir.mts.ru/mts-ir/images/documents/results/MTS_1Q_2026_Press_release_RUS.pdf · MTS IR release page https://ir.mts.ru/en/news_and_events/corporate_releases/details/742412 · MTS Bank Q1 2026 (fintech) https://www.mtsbank.ru/o-banke/novosti/detail/1151373/ · AdTech Q1 2026 https://www.content-review.com/articles/74395/ · public consensus [UNSOURCED]; capex [no data].
<!-- /enrichment:earnings_review -->
