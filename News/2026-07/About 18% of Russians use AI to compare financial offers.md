---
title: "About 18% of Russians use AI to compare financial offers"
date: 2026-07-11
retrieved: 2026-07-11
tags:
  - industry/ai
  - industry/banking
  - region/ru
  - type/research-report
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: s6e615da9
month: 2026-07
enriched: true
importance: 2
freshness: fresh
---

# About 18% of Russians use AI to compare financial offers

> [!info] 2026-07-11 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] ИИ становится новым входом клиента в финансовый выбор: около 18% россиян в 2026 году используют нейросети как источник информации о предложениях банков, МФО, брокеров и других финансовых организаций, по данным Servicepipe. Другие полезные сигналы ▶️ В июне 2026 года ИИ-агенты, краулеры и скраперы сгенерировали 6 млн запросов к сайтам четырёх крупных брокеров. Частные инвесторы за тот же период совершили 922 млн обращений к сайтам тех же брокеров. ▶️ Речь не только о ChatGPT-подобных ассистентах, но и о поисковиках, которые перешли на ИИ-технологии. Доля ИИ-запросов к сайтам брокеров выросла на 20% с начала года. ▶️ Внутри ИИ-трафика есть разные типы. На ИИ-ассистентов пришлось чуть больше 2 млн обращений за месяц, или 33% всего ИИ-трафика. Чаще всего для поиска финансовой информации через нейросети пользователи используют ChatGPT, Alisa․AI и Perplexity. ▶️ Краулеры и скраперы, которые собирают данные для индексации, обучения или точечного извлечения информации, дали ещё 7% обращен

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: About 18% of Russians use AI to compare financial offers (Servicepipe)
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
Servicepipe — a **Russian DDoS/anti-bot traffic-filtering vendor** (in market since 2015; clients include banks, telecoms, e-com, payment systems) — published a study (circulated via Финтехно; primary pickup 1prime.ru, 08 Jul 2026) headlined "~**18% of Russians in 2026 use neural networks as a source of information** about offers from banks, MFOs, brokers and other financial firms." The rest of the item is **traffic analytics**, which is Servicepipe's actual product domain:
- In **June 2026**, AI agents + crawlers + scrapers generated **~6M requests** to the sites of **four large brokers**; private investors made **~922M requests** to the same sites in the same period → AI traffic ≈ **~0.7%** of total (the note's own figures).
- Share of AI requests to broker sites **+20% since start of year**.
- Within AI traffic: **AI assistants ~2M requests (33%)**; **crawlers/scrapers ~7%** (leader: Applebot, ~1.2M). Most-used assistants for financial search: **ChatGPT, Alisa.AI, Perplexity**.
- Activity peaked **16–21 June**, ahead of the CBR key-rate decision.

**+ Why framed this way / the core red-team point (analysis):** the "18% of Russians" headline is **not from an opinion poll** — Servicepipe measures *machine-readable traffic* (bots, crawlers, AI-assistant fingerprints) on its clients' sites and *infers* human behaviour. A bot-protection vendor's incentive is to make "AI/bot traffic to financial sites" look large and threatening (it sells AI-traffic classification/gating — cf. Servicepipe reporting a "3x rise in requests to configure AI-agent handling"). So the number is a **marketing artefact of a security vendor**, methodology undisclosed (how "18% of Russians" is derived from site traffic is never shown), and should be read as **directional, not survey-grade**. The internally consistent, verifiable part is the **broker-site traffic split (~0.7% AI, +20% YTD)** — that is Servicepipe's real data; the "18% of Russians" is the soft extrapolation.

## [1] Competitors / peers (other RU AI-in-finance surveys — the freshness pivot)
Mid-2026 saw a **cluster of overlapping "Russians + AI + money" studies from different authors with different numbers** — so cross-checking is essential and none is a straight duplicate of this one:
- **SberStrakhovanie Zhizni "ИИнвестиции"** (26 Jun 2026, Vedomosti/PRIME/1prime): **19.5%** already use AI for financial questions; **11,000 respondents, 37 cities >500k pop.** — a proper opinion survey. 40% still prefer discussing money with a human; 38% fear wrong recommendations. This is the **methodologically stronger** comparable, and its ~19.5% roughly brackets Servicepipe's 18%.
- **"Russians disappointed in AI financial advice"** (finance.mail.ru / prospect.com.ru): nearly half dissatisfied with neural-net financial advice — the skeptical counter-signal.
- **Banki.ru**: which banks neural nets recommend to Russians (AI-as-recommendation-engine angle).
- **CNews/plusworld (28 May 2026)**: "how Russians build a dialogue with neural nets on finance."
**Position:** Servicepipe's item is **ahead only on the traffic-measurement angle** (it uniquely quantifies AI-bot vs human traffic to broker sites); on the "% of Russians using AI for finance" headline it is **parity/behind** the larger SberStrakhovanie poll. **+ Why (analysis):** every vendor here has a book to talk — Sber sells AI, Servicepipe sells bot-filtering — so each survey is a lead-gen asset; the *convergence* around ~18–20% is the only robust takeaway.

## [2] Company history / fit
Servicepipe (est. 2015) = high-precision DDoS + advanced-bot filtering; sub-ms blocking, <0.01% false positives, per-request (not IP) filtering. Recently shipped **Digital Fraud Protection** (deep traffic analytics) and reports a **3x rise in client requests to configure AI-agent handling**. **+ Why it acts this way (analysis):** this "study" is **content marketing for exactly that product** — the pitch is "AI/crawler/scraper traffic to your financial site is real, rising 20% YTD, and you need to classify/gate it (allow good assistants, block scrapers)." The financial-market framing targets the buyer segment (brokers, banks) it wants to sell into. Fits the vendor's commercial logic precisely.

## [3] Novelty / value-add / traction
**What's genuinely useful:** the **broker-site AI-traffic dataset** — ~6M AI requests vs ~922M human (~0.7%), +20% YTD, 33% assistants / 7% crawlers, Applebot leading, peak around the CBR-rate window. That is a **rare, concrete, source-side measurement** of how AI/agents actually touch Russian financial sites — more novel than the "18%" headline. **What's soft:** the "18% of Russians" claim (opaque methodology, vendor incentive, single self-published source). **+ Who captures the value (analysis):** the second-order story is **GEO/AEO and traffic economics** — if a growing share of financial discovery routes through ChatGPT/Alisa/Perplexity, brokers and banks lose the direct-site funnel (and its analytics/retargeting) to the assistant layer, exactly the "AI becomes the client's new front door to financial choice" thesis in [[Финтехно T-Bank sees standalone banking apps losing relevance]]. But at **~0.7% of broker traffic**, this is still an **early signal, not a channel shift** — the note's own numbers undercut the headline's urgency.

## [4] What's next / market sentiment
Expect this "AI-as-financial-discovery-channel" theme to keep recurring (multiple vendors are seeding it). Structural backdrop: Russia's assistant layer is domesticating (Alisa.AI/Yandex, Sber's [[Sber unveils flagship GigaChat 3.5 Ultra model]], VK's [[VK launches Discovery AI neural search across products]]) and the CBR is tightening financial-product disclosure/advertising ([[Russian Duma backs bill on clearer financial product ads]], [[Финтехно Russian banks need memorandum on honest deposit disclosure]]) — which will eventually collide with "what an AI assistant tells you about a deposit/loan." Risk: unregulated AI financial recommendations + the "half are dissatisfied" counter-survey → a mis-selling / accuracy problem regulators will notice. **+ Second-order (analysis):** for a bot-protection vendor the *real* market is not "% of Russians" but brokers/banks paying to **classify and gate** AI traffic (allow assistants that drive leads, block scrapers that lift pricing) — that is where Servicepipe monetises, and why it publishes numbers like these.

## FRESHNESS / DUPLICATE VERDICT
**FRESH.** No prior vault note covers the Servicepipe study or its broker-traffic figures. It is **distinct** from the SberStrakhovanie "ИИнвестиции" survey (different author, method, and the ~0.7% traffic dataset is unique to Servicepipe), so it is **not a duplicate** — but it is one of several near-simultaneous RU "AI + finance" surveys, and its "18%" headline is the least rigorous of them. Weight is low.

## Sources
- Финтехно (max.ru/fintexno) — aggregated primary text (2026-07-11). Full text not cached.
- 1prime.ru, "Исследование показало, как россияне используют ИИ на финансовом рынке" (08 Jul 2026): https://1prime.ru/20260708/issledovanie-871366408.html
- Servicepipe (company / products, est. 2015, bank & payment-system clients): https://servicepipe.ru/ ; Digital Fraud Protection: https://www.itsec.ru/news/servicepipe-vipuskayet-digital-fraud-protection-sistemu-glubokoy-analitiki-trafika-dlia-vuyavleniya-moshennichestva ; "3x rise in AI-agent-handling requests": https://www.itsec.ru/news/servicepipe-fixiruyet-triohkratniy-rost-zaprosov-na-nastroyku-raboti-s-ii-agentami
- Comparable survey — SberStrakhovanie Zhizni "ИИнвестиции" (19.5%, 11,000 resp., 37 cities, 26 Jun 2026): https://www.vedomosti.ru/press_releases/2026/06/26/iinvestitsii-kazhdii-pyatii-rossiyanin-uzhe-ispolzuet-iskusstvennii-intellekt-v-finansovih-voprosah ; https://1prime.ru/20260626/sberstrakhovanie-871068170.html
- Counter-signal ("half disappointed in AI financial advice"): https://finance.mail.ru/article/rossiyane-zabrakovali-finansovye-sovety-nejrosetej-69215688/ ; https://prospect.com.ru/news/6831480/
- Which banks neural nets recommend (banki.ru): https://www.banki.ru/news/lenta/?id=11024208
- Prior corpus notes: [[Финтехно T-Bank sees standalone banking apps losing relevance]], [[Sber unveils flagship GigaChat 3.5 Ultra model]], [[VK launches Discovery AI neural search across products]], [[Russian Duma backs bill on clearer financial product ads]], [[Финтехно Russian banks need memorandum on honest deposit disclosure]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **How is "18% of Russians" actually derived?** Servicepipe measures *site traffic* (bot/crawler/assistant fingerprints), not a sampled population. The path from "AI traffic on client sites" to "18% of Russians" is **never disclosed** → treat as vendor extrapolation, not survey-grade. **Open / methodology opaque.**
2. **Whose incentive shapes the number?** Servicepipe sells AI/bot-traffic classification and gating; a bigger "AI traffic to financial sites" number sells more product. **Confirmed vendor bias.**
3. **Is it a duplicate of the SberStrakhovanie "ИИнвестиции" survey (19.5%, 26 Jun 2026)?** No — different author, different method (11,000-respondent poll vs traffic analytics), and the ~0.7% broker-traffic dataset is unique to Servicepipe. **Fresh, not a duplicate.** But numbers converge (~18–20%), which is the only robust takeaway.
4. **What is the hard, verifiable part?** The **broker-site traffic split**: ~6M AI vs ~922M human requests (~0.7% AI), +20% YTD, 33% assistants / 7% crawlers, Applebot ~1.2M. That is Servicepipe's real data. **Answered.**
5. **Does ~0.7% AI traffic support the "AI is the new front door" framing?** Not yet — 0.7% is a **weak early signal**, not a channel shift. The headline overstates the underlying data. **Confirmed — note's own numbers undercut it.**
6. **Is "18%" a stable trend or a one-off spike?** Activity peaked 16–21 June around the CBR key-rate decision — i.e. **event-driven**, so June may over-represent AI traffic. **Open.**
7. **Sample scope?** "Four large brokers" only. Generalising broker-site behaviour to "all Russians / banks / MFOs" is a leap. **Open / narrow base.**
8. **Assistant list credibility (ChatGPT, Alisa.AI, Perplexity)?** Plausible but note ChatGPT is officially unavailable in Russia — so this measures VPN/relay use; classification of assistant traffic can be noisy. **Open.**
9. **Human vs bot attribution error?** Servicepipe's whole business is distinguishing them, but "AI-assistant on behalf of a human" vs "autonomous scraper" is a hard line; the 33%/7% split rests on their classifier. **Open — single-vendor method.**
10. **Counter-evidence?** A parallel finance.mail.ru/banki.ru survey found ~half of Russians *dissatisfied* with AI financial advice — adoption ≠ satisfaction/reliance. Weakens the "AI drives real financial choice" read. **Confirmed counter-signal.**
11. **Sourcing strength.** Single self-published vendor study via a Telegram digest (Финтехно), no primary methodology doc, no independent replication. **Weak sourcing.**
12. **Regulatory hook?** If AI assistants increasingly "advise" on deposits/loans, does that collide with CBR disclosure/ad rules ([[Russian Duma backs bill on clearer financial product ads]])? Real but downstream. **Open / directional.**
13. **What is silent?** No absolute base for "18%" (of adults? of internet users? of visitors?), no y/y comparison, no confidence interval, no definition of "use as a source of information." **Multiple undisclosed denominators.**
14. **Does it move anything for the market?** Marginally — useful as a *trend marker* for the "assistant-layer disintermediation" thesis, but at 0.7% traffic it changes no one's numbers today. **Low read-across.**

**Importance: 2/5 — rationale:** A vendor content-marketing study whose headline ("18% of Russians") has **opaque, non-survey methodology and a clear commercial incentive**, published via a single Telegram digest with no primary methodology doc. It is *fresh* (no prior note; distinct from the stronger SberStrakhovanie 11,000-respondent survey that brackets it at ~19.5%) and contains one genuinely useful, verifiable nugget — the broker-site AI-vs-human traffic split (~0.7% AI, +20% YTD, 33% assistants) — which is a real early signal for the "AI as the new front door to financial choice" thesis ([[Финтехно T-Bank sees standalone banking apps losing relevance]]). But the load-bearing headline is soft, the base is narrow (four brokers, an event-driven June peak), a parallel survey shows ~half are dissatisfied with AI financial advice, and 0.7% traffic doesn't yet move anything. Directionally interesting, evidentiarily thin → 2/5.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-07-12]] (2026-07-12).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a survey datapoint on the Russian retail-finance *discovery* layer — where customers first form intent about banks/MFOs/brokers — not a company event. Sourced facts: per Servicepipe (cybersecurity lab), ~18% of Russians in 2026 use neural nets as a source of info on financial offers; AI requests to broker sites are up ~20% YTD; in June 2026 AI agents/crawlers/scrapers generated ~6M requests to four large brokers vs ~922M human private-investor visits (i.e. AI ≈ 0.7% of visits, though skewed by player); of AI traffic, ~2M/month (~33%) came from AI assistants — most-used: ChatGPT, Alisa.AI, Perplexity — and crawlers/scrapers added ~7% (per Servicepipe, via 1prime.ru / itsec.ru, 08.07.2026). Cross-check: a separate June-2026 survey put AI usage in financial questions at "every fifth" Russian (~20%), so ~18–20% is a consistent read (Vedomosti, 26.06.2026). Structure: the discovery market is a fragmented, contestable choke-point sitting *above* product providers — historically owned by search engines (Yandex) and comparison marketplaces (Sravni.ru, Banki.ru, Vyberu.ru); AI assistants are a new, thin but fast-growing layer that intermediates the same intent. **Why now:** search engines themselves went generative (AI answers displace blue links), so the entry point migrates from "search box → provider site" to "assistant answer → provider," compressing the funnel and moving discovery off providers' own properties.

**Competitive landscape.** KPIs this layer runs on: share of AI-sourced traffic/intent, assistant-answer inclusion (being cited/recommended), and downstream conversion of AI referrals. Players: (a) foreign/dual assistants — ChatGPT, Perplexity; (b) domestic AI — Yandex Alisa.AI, Sber GigaChat (Ultra 3.5 refresh, 2026-07), VK Discovery AI neural-search (2026-07); (c) legacy discovery — comparison marketplaces + classic search. Basis of competition: answer quality/recency, distribution (default in a browser/OS/superapp), and trust. Recent moves: T-Bank publicly argued standalone banking apps will lose relevance as finance moves into contextual/platform scenarios (2026-07); Sber shipped GigaChat 3.5 Ultra with agentic scenarios (2026-07); VK launched Discovery AI incl. Deep Research (2026-07). Protagonist here is the *sector*, not a firm: banks/MFOs/brokers are on the losing side of position — they don't own the new entry point; the moat migrates to whoever owns the default assistant (network effects + distribution), which in RU points to Yandex/Sber/VK, not the product manufacturers `(analysis)`.

**Comps & multiples.** No valuation/round/metric in the item → trading multiples not applicable ("no data"). Internal thematic comps (the "AI/assistant displaces the app as customer entry point" thread):
- [[Финтехно T-Bank sees standalone banking apps losing relevance]] (2026-07) — closest RU comp; same thesis from the provider side.
- [[VK launches Discovery AI neural search across products]] (2026-07) and [[Sber unveils flagship GigaChat 3.5 Ultra model]] (2026-07) — the domestic assistants capturing the entry point.
- [[Ozon to launch brokerage arm Ozon Investments in autumn 2026]] (2026-07) — a marketplace pushing into brokerage, i.e. discovery→product integration.
- [[CaixaBank deploys AI agent for in-app purchases]] (2026-03), [[Starling launches UK's first agentic AI assistant]] (2026-03), [[Mercado Pago launches AI financial assistant]] (2026-01) — global precedents for finance-in-assistant. Distribution not computed — no comparable figures; qualitative only.

**Risk flags.**
1. **Reliability / mis-selling gap (near-term, largest).** A parallel Vyberu.ru/Еврокредит survey found ~46% of Russians who asked AI for financial advice were disappointed — complaints: too-generic answers (37%), stale product/rate data (26%), calculation errors (21%); average loss ~₽21,700 among those who followed bad advice (finance.mail.ru / prospect.com.ru, 2026-06/07). Second-order: assistants confidently recommending suboptimal deposits/loans invite consumer-protection and CBR attention, and providers bear reputational fallout for answers they don't control.
2. **Disintermediation of the customer relationship.** If ~18%+ of intent forms inside a third-party assistant, banks/MFOs/brokers lose the top-of-funnel and become interchangeable SKUs ranked by an opaque model — margin/attention captured by the assistant-and-browser layer, not the balance-sheet holder.
3. **Bot/traffic-quality & data-extraction risk.** The same trend means crawlers/scrapers hammering provider sites (Servicepipe's core pitch is filtering this) — cost, scraping of proprietary rate data, and inability to distinguish "good" AI referrals from abusive bots. Note bias: Servicepipe sells anti-bot tooling, so it is an interested source — treat the 18% as directional, not audited.

**What this changes (idea-lens).** The customer *entry point* in RU retail finance is starting to shift from search + comparison marketplaces to AI assistants — a re-rating risk for discovery incumbents (Sravni/Banki.ru/Yandex search) and a distribution risk for product providers `(analysis)`. Falsifiable thesis: over 2026 the share of AI-sourced financial intent keeps climbing (Servicepipe reported +20% YTD to broker sites); trigger/what to watch — CBR guidance on AI financial advice, banks paying/optimizing for assistant "answer inclusion," and whether the ~46% disappointment rate falls (which would legitimize the channel) or holds (which caps adoption at experimentation).

Sources: https://1prime.ru/20260708/issledovanie-871366408.html · https://www.itsec.ru/news/servicepipe-fixiruyet-triohkratniy-rost-zaprosov-na-nastroyku-raboti-s-ii-agentami · https://www.vedomosti.ru/press_releases/2026/06/26/iinvestitsii-kazhdii-pyatii-rossiyanin-uzhe-ispolzuet-iskusstvennii-intellekt-v-finansovih-voprosah · https://finance.mail.ru/article/rossiyane-zabrakovali-finansovye-sovety-nejrosetej-69215688/ · https://prospect.com.ru/news/6831480/rossiyane-razocharovalis-v-finansovyh-sovetah-nejrosetej-pochti-polovina-nedovolna-rezultatami.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
