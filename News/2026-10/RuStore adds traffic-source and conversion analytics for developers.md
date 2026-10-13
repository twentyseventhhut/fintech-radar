---
title: "RuStore adds traffic-source and conversion analytics for developers"
date: 2026-10-12
retrieved: 2026-10-12
tags:
  - company/rustore
  - industry/infrastructure
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-10-07_razrabotchiki_v_rustore_smogut
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sf9306634
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# RuStore adds traffic-source and conversion analytics for developers

> [!info] 2026-10-12 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Добавил в RuStore аналитику источников трафика, установок и конверсии для разработчиков приложений

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-10-07_razrabotchiki_v_rustore_smogut>
*162 слов · direct*

Эльяс Касми

 Разработчики в RuStore смогут отслеживать источники установок приложений
 
 
Магазин приложений RuStore добавил в статистику консоли анализ источников трафика. Разработчики теперь могут видеть, откуда приходят пользователи, и оценивать эффективность разных каналов продвижения приложений. Об этом CNews сообщили представители RuStore .
В статистике доступно распределение просмотров, установок, обновлений и конверсии по источникам трафика — как внутри RuStore, так и за его пределами. Это позволяет сравнивать разные каналы и понимать, какие из них приводят больше пользователей.
Также разработчики могут посмотреть эти показатели по странам. Данные помогут оценить географию аудитории приложения и учитывать ее при выборе стратегии продвижения. Более подробную информацию разработчики могут получить с помощью SDK Install Referer, который отслеживает количество установок по рекламным ссылкам. 
«Для разработчиков важно понимать не только сколько пользователей пришло в приложение, но и откуда именно. Анализ источников трафика поможет увидеть, какие каналы реально приводят установки и где находится аудитория приложения, чтобы точнее распределять усилия на продвижение», — сказал директор по продукту RuStore Олег Афанасьев . 
 EvaConf Enterprise 2026

## Контекст

<!-- enrichment:context -->
**[0] TL;DR.** RuStore — Russia's state-backed Android/HarmonyOS/Aurora app store — added traffic-source analytics to its developer Console. Developers can now see where installs come from (channels inside and outside RuStore) and break down views, installs, updates and conversion by source and by country. Announced via CNews on 2026-10-07. This is an incremental developer-console feature, not a strategic or financial event: a catch-up with the standard attribution tooling (UTM/referrer) long available on Google Play and the App Store. Importance is low from a fintech/markets lens.

**[1] What's actually new (vs. prior state).** The RuStore Console already exposed basic statistics (page views, installs, version updates, install-conversion rate). The new piece is *attribution by traffic source*: splitting those same metrics by where the user came from, with geographic breakdown and comparison of internal vs. external channels. RuStore pairs this with an existing SDK ("Install Referer") that counts installs from ad links. Named spokesperson: Oleg Afanasyev, RuStore product director. Mirrors Google Play's acquisition/UTM reports and App Store Connect source-type analytics — so this is feature parity, not innovation.

**[2] Who/landscape.** RuStore launched in 2022 as a domestic alternative after Apple/Google restricted Russian access. Scale (web, mixed dates — treat as approximate): ~65,000–110,000+ apps; ~54–68 million monthly/active users by 2025–2026; ~15,000 registered developers; cited as #2 app store in Russia (~13% share early-2025) behind Google Play (~85%), but growing fastest. Regulatory tailwind: from 2025-09-01 Russian law mandates RuStore be made available/pre-installed on devices sold in Russia, including Apple iPhones/iPads, even over OS-owner objection — a captive-distribution advantage no Western store enjoys.

**[3] CAUTION — ownership change not reflected in the note.** The note frames RuStore as VK's property, but **VK agreed (2026-07-16) to sell 100% of RuStore to Dmitry Pankrushev, CEO of developer "Mnogo Prilozheniy," days after the EU sanctioned VK (2026-07-13) over the Kremlin Max messenger.** So by the time of this 2026-10 feature launch, RuStore was being/had been divested from VK. Any framing should NOT call RuStore "VK's app store" without caveat. Sale price undisclosed. (Sources: Moscow Times, Interfax, Meduza, 2026-07-16.) Separately, the same-day-adjacent note [[VK sells 40% stake in ticketing service Intickets]] is part of VK's broader post-sanctions asset shedding — thematically linked but a different asset.

**[4] Why it matters / fintech angle (thin).** Direct fintech relevance is marginal: better install attribution lowers user-acquisition cost measurement for app developers, including fintech/banking apps that must distribute via RuStore to reach sanctioned-market Russian Android/iOS users. The more material backdrop is structural — sanctions-driven divestment of RuStore from VK and the mandated-distribution regime — not this analytics add-on itself. Related internal notes: [[VK sells 40% stake in ticketing service Intickets]], [[News & Trends Foldable smartphones split the global market]] (RuStore mentioned in device/app-ecosystem context).

**FRESHNESS VERDICT: FRESH.** No prior note covers RuStore developer analytics or this 2026-10-07 announcement; it is not a duplicate. However it is LOW-IMPORTANCE / incremental and arguably "stale-signal" (parity feature, not news-moving) — kept as fresh because not previously covered.

_Sources: cnews.ru 2026-10-07 (primary); tadviser.com; rustore.ru dev docs; en.wikipedia.org/wiki/RuStore; themoscowtimes.com / interfax.com / meduza.io 2026-07-16 (VK sale); telecompaper.com / tass.com / akm.ru (2025 pre-install mandate). Web stats are approximate and date-mixed._
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Is traffic-source attribution genuinely new, or was a limited version already in the Console? The note says the Console already had install/conversion stats — how much of this is repackaging?
2. Does "sources inside and outside RuStore" mean true cross-domain attribution, or only tagged ad-links via the Install Referer SDK (i.e., developers must instrument links themselves)?
3. How accurate is external attribution without IDFA/GAID-style identifiers under Russian privacy constraints — is conversion measurement deduplicated or last-click only?
4. The note calls RuStore VK's store; but VK agreed to sell 100% to Pankrushev on 2026-07-16 after EU sanctions. Who actually owns/operates RuStore at the 2026-10 launch date?
5. Did the VK divestment complete, and does the new owner ("Mnogo Prilozheniy"/Pankrushev) change the product roadmap or data-governance of these analytics?
6. Are the audience/app/developer counts (54–68M users, 65k–110k apps, 15k devs) from RuStore's own PR or independently verified? Dates are mixed across sources.
7. Only one source (CNews) and one channel (News & Trends by Sber). Is this effectively a vendor press release with no independent corroboration?
8. Does this feature move any market, revenue, or fintech metric, or is it purely developer-tooling with no financial signal?
9. Is there a fintech-specific angle at all, or is relevance only via the generic "fintech apps also distribute on RuStore" argument?
10. Is the "by country" breakdown meaningful given RuStore is overwhelmingly Russia-only distribution? What non-RU install volume realistically exists?
11. Does this close a competitive gap vs. Google Play/App Store, or does it still lag (e.g., cohort/LTV/funnel analytics those platforms offer)?
12. Could the timing (post-sanctions, mandated pre-installation on Apple devices from 2025-09) mean this is positioning for a captive-but-growing developer base rather than a competitive feature?
13. Any risk the analytics data feeds state-surveillance concerns given RuStore's state-backed status and the sanctioned-VK lineage?
14. Does the Sber channel's framing add spin (Sber competes/partners in Russian app ecosystem)? Any conflict of interest in sourcing?
15. Is anything time-sensitive here, or can this note be safely deprioritized in the digest?

**Importance: 2/5** — Incremental developer-console attribution feature (parity with Google Play/App Store), single-source (CNews) vendor announcement, no revenue/market impact and only marginal fintech relevance. Bumped slightly above minimum because of the material, under-reported backdrop the note itself misses: RuStore's July-2026 sanctions-driven divestment from VK and Russia's mandated-distribution regime, which are the genuinely consequential stories around this asset.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** RuStore operates in the Russian Android app-distribution market, a politically-driven carve-out of the global duopoly. Market structure is concentrated: as of early 2025 Google Play held ~85% and RuStore ~13% share of Russian app stores (per TAdviser/Wikipedia, as of early 2025) — so RuStore is the #2 distribution rail by share but with fast traction: 110,000 apps/games listed by July 2026 and a monthly audience >68m users by late 2025, which per reporting had passed Google Play in *active users* inside Russia (per Wikipedia/TAdviser, as of late 2025/mid-2026). Why now: Russia's app-store "sovereignty" push — RuStore is mandated pre-installed on all Android devices and, from Sep 2025, legally required on new iPhones/iPads, with device makers obliged to give it non-discriminatory screen placement even over OS-owner objections (per Telecompaper/TASS, 2025). State backing (originally VK + Ministry of Digital Development) + Google Play's partial withdrawal (removed apps, no new paid listings for RU devs) is the structural driver converting RuStore from fallback to default rail. Entry barriers here are regulatory/political, not capital — the moat is the mandate, not the product.

**Competitive landscape.** The relevant KPIs for an app store are MAU, listed-app count, install volume, and (for the monetization stack) payment conversion / take rate; for the *analytics layer* announced here the KPIs are attribution coverage (share of installs sourced) and funnel conversion. Players: (a) distribution — Google Play (incumbent, ~85% share but managed decline), RuStore (#2), plus Huawei AppGallery, Xiaomi GetApps and Samsung/NashStore in the long tail; (b) the adjacent **attribution/analytics (MMP) layer** RuStore is now stepping into — globally AppsFlyer (~65% self-claimed share, ~$28bn ad spend measured), Adjust, Branch, Kochava, with AppsFlyer+Adjust ~45% and top-3 >60% of global MMP revenue in 2024 (per Business of Apps / Intel Market Research, 2024-25). In Russia the closest comp is **AppMetrica (Yandex)**, a free MMP already on the top-5 MMP lists and which added RuStore install-referrer support in May/Jul 2026. Recent moves: RuStore added install-referrer to the AppMetrica SDK (May/Jul 2026), an Offers funnel report in the Monetization section (Sep 2026), and now (Oct 2026) traffic-source/install/conversion analytics by channel and country directly in Console Statistics, plus its own SDK Install Referer (per cnews/rustore.ru, Oct 2026). Protagonist's position: RuStore is *catching up* on the analytics layer to what AppsFlyer/Adjust/AppMetrica already offer, but it is bundling attribution natively into the store console — a first-party data advantage no third-party MMP has, since RuStore owns the install event. `(analysis)` Moat = control of the mandated distribution rail + first-party install data; weak on product maturity vs specialist MMPs.

**Comps & multiples.** No valuation disclosed for this product news; RuStore itself has no public standalone valuation. Critically, VK **sold 100% of RuStore to management** (CEO Dmitry Pankrushev / Mnogo Prilozheniy) in Jul 2026, days after EU sanctions hit VK — deal terms and valuation undisclosed (per Meduza/Kommersant/VK, Jul 2026), so no transaction multiple is computable. Internal comps: no comparable app-store/MMP deal found in the corpus (semsearch down — OpenRouter 402; grep fallback surfaced no app-store/attribution comps — distribution not computed). External multiples for listed MMPs are not publicly derivable (AppsFlyer, Adjust, Branch all private; no verifiable revenue) → **EV/Revenue and all multiples = no data / [UNSOURCED]**. Qualitative only: RuStore is a sub-scale #2 store monetizing via a payment SDK + now an analytics layer, not a standalone traded asset.

**Risk flags.** (1) **Ownership/independence shift** — RuStore left the VK ecosystem in Jul 2026 (management buyout post-EU-sanctions); the sovereignty mandate and Sber/VK distribution tailwinds that made it default may not transfer cleanly to an independent, sanctions-adjacent owner, and sanctions on the former parent raise SDK/payments counterparty risk for foreign developers. (2) **Mandate dependency** — RuStore's share is a creature of regulation (forced pre-install, iOS mandate), not product preference; any softening of enforcement or Apple non-compliance caps the upside, and growth is non-replicable outside RU. (3) **Attribution credibility / conflict of interest** — a store grading the effectiveness of ad channels that it also sells into is both marker and referee; without third-party MMP corroboration (AppsFlyer/Adjust absent from RU), self-reported source/conversion data is hard for developers to audit — fraud/over-attribution risk unflagged.

**What this changes (idea-lens).** `(analysis)` RuStore is moving up the stack from pure distribution into the adtech/attribution layer, using its ownership of the install event to bundle MMP-style analytics for free — a classic store-as-platform play (what Apple/Google did with SKAdNetwork/Play Install Referrer). Thesis: in a sanctions-walled market where AppsFlyer/Adjust are effectively absent, RuStore + Yandex AppMetrica consolidate the RU mobile-attribution stack between them. Trigger to watch: whether the new independent owner keeps the state mandate and whether RuStore starts charging for or gating the analytics (signal it's building a real monetization layer vs a retention feature). Falsifier: if Google Play reverses its RU withdrawal, the mandate-driven share advantage erodes fast.

Sources: https://www.cnews.ru/news/line/2026-10-07_razrabotchiki_v_rustore_smogut · https://en.wikipedia.org/wiki/RuStore · https://tadviser.com/index.php/Product:RuStore · https://www.telecompaper.com/news/russia-to-make-rustore-mandatory-on-iphones-ipads--1513337 · https://tass.com/economy/1666931 · https://meduza.io/en/news/2026/07/16/days-after-eu-sanctions-russian-social-network-vk-agrees-to-sell-its-rustore-app-store-to-the-head-of-the-company-that-developed-it · https://www.rustore.ru/developer/en/blog/monetization-and-promotion-in-rustore-what-is-important-for-a-developer-to-know · https://www.businessofapps.com/marketplace/app-analytics/mobile-measurement-partners/ · https://splitmetrics.com/blog/best-mobile-measurement-partners-mmps/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
