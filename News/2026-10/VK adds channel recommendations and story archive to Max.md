---
title: "VK adds channel recommendations and story archive to Max"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/vk
  - industry/infrastructure
  - region/ru
  - type/product
sources:
  - https://www.cnews.ru/news/line/2026-10-15_v_max_poyavilis_novye_funktsii
status: enriched
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: sf98fc5de
month: 2026-10
enriched: true
importance: 2
freshness: fresh
---

# VK adds channel recommendations and story archive to Max

> [!info] 2026-10-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Добавил в Max рекомендации каналов на основе интересов пользователей, архив историй, автоматическое сохранение медиафайлов в галерею и настройку размера текста

## Первоисточники

### cnews.ru
<https://www.cnews.ru/news/line/2026-10-15_v_max_poyavilis_novye_funktsii>
*151 слов · direct*

Дмитрий Степанов

 В Max появились новые функции
 
 
Пользователи получили возможность регулировать размер текста в настройках мессенджера Max, сохранять истории в архив и подключить автосохранение медиа в галерею, а авторы могут попасть в подборку рекомендованных каналов в ленте. Об этом CNews сообщил представитель Max.
В числе новых возможностей: рекомендации каналов. После подписки на новый канал на экране пользователя отобразится блок с подборкой. Система рекомендаций предлагает каналы на основе интересов подписчиков, схожих тематик, качества контента и частоты взаимодействия с ним. Таким образом пользователи могут найти новых авторов и подписаться на новые каналы; архив историй. Получить доступ к архиву историй можно в разделе « Чаты », удерживая нажатием иконку профиля или в настройках приложения в разделе «Мои истории»; автосохранение медиа. Подключить или отключить автоматическое сохранение медиа из чата в галерею телефона можно в настройках приложения в разделе «Хранение и загрузка медиа», настроить комфортный размер текста – в разделе «Оформление». 
 III ежегодная конференция Ampire 360°

## Контекст

<!-- enrichment:context -->
# Context-enrichment: VK adds channel recommendations and story archive to Max
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
On 2026-10-15 VK shipped a bundle of four client-side UX features to Max (the state-backed Russian "national messenger"), confirmed to CNews by a Max spokesperson and re-reported broadly (RBC, Vedomosti, RIA, Rossiyskaya Gazeta, PRIME, m24):
1. **Channel recommendations** — after a user subscribes to a channel, a recommendation block appears suggesting other channels, ranked by "subscriber interests, similar topics, content quality and interaction frequency."
2. **Story archive** — users can access an archive of their stories under Chats (long-press the profile icon) or Settings → "My stories."
3. **Media auto-save** — optional auto-save of chat photos/video to the phone gallery (Settings → "Storage and media downloads").
4. **Text-size setting** — adjustable message text size (Settings → "Appearance").

**Why framed this way / what it reveals:** Three of the four are pure quality-of-life parity features (story archive, media auto-save, font size) that Telegram/WhatsApp have had for years — table-stakes shipped to close the UX gap that a *mandated* app can otherwise ignore. The only item with product/business weight is the **channel-recommendation algorithm**: it is a discovery/distribution mechanism, not a settings toggle. It directly thickens the channel surface VK and Yandex have just begun to monetize with ads (see [1]/[2]). The PR frames all four as equal "new functions," which flattens the one feature that actually matters (algorithmic channel distribution → more subscriptions → more ad inventory) into a list of cosmetic toggles. That flattening is the tell: VK is building a Telegram-style discovery/monetization funnel while presenting it as routine housekeeping.

## [1] Competitors / peers
- **Telegram** — the direct template. Telegram has algorithmic "similar channels" recommendations and a stories/archive feature; Max is cloning the discovery funnel feature-for-feature. Telegram remains the most-used messenger in Russia (~100M users early 2026) despite being throttled since Feb 2026 (voice/video blocked, media download speeds degraded) — so Max's recommendation engine is explicitly aimed at capturing the channel audience migrating off a degraded Telegram.
- **WhatsApp** — fully blocked in Russia (DNS scrubbed, ~Feb 12 2026); ~90M Russian users pre-block. No channel-discovery parity; pure DM competitor being displaced.
- **VK's own ecosystem** — VK the social network and Dzen already run interest-based feed recommendations (VK's Discovery recommendation/ad platform underlies VK Реклама); Max is importing that recommender stack into the messenger.

**Why the lay of the land is this way (analysis):** Max's channel growth is **policy-manufactured** (pre-install mandate since Sep 2025, WhatsApp blocked, Telegram throttled), so supply is being pushed onto the platform administratively (schools, housing associations, gov agencies — ~70% of channels per Agentstvo/Meduza). A recommendation algorithm is the demand-side complement: having forced supply onto the platform, VK now needs a discovery mechanism so users actually *subscribe* to channels, converting a coerced channel count into live subscriptions that ads can monetize. The second-order dynamic: the recommender is where Max shifts from "mandated reach" toward "engineered engagement" — the metric that actually underwrites ad eCPM.

## [2] Company history / fit
Max launched ~2025; registrations grew to 107M (Mar 2026), 140M installs with >90M DAU by Oct 2026 (per CEO Khusnoyarov / ixbt). VK itself turned EBITDA-positive in FY2025 (RUB 22.6bn) but posted a 6th straight annual net loss; Q2 2026 produced a first small quarterly net profit (RUB 328M). This bundle fits VK's structural logic: a loss-making ad/social business handed a mandated distribution monopoly needs to convert that reach into ad/payment revenue, which requires (a) UX parity so the mandated app is tolerable, and (b) a discovery funnel to monetize channels. This note is one brick in a dense Oct-2026 Max channel-feature + monetization sprint already in-corpus: [[Max adds multi-choice polls with revoting in channels]] (polls, ~Oct 6), [[VK opens Max channel ads to accounts over 1K subscribers]] (ad cabinet, Oct 12), [[VK grows Max public channels to 530K in Q3 2026]] (Q3 channel KPIs). Channel recommendations is the discovery layer that feeds all three.

## [3] Novelty / value-add / traction
**Novelty: low-to-moderate.** Three features are pure parity (archive/auto-save/font). The channel-recommendation algorithm is genuinely new *for Max* but is itself a copy of Telegram's long-standing "similar channels" mechanic — novel only in a coerced-distribution market, not in absolute terms. **Traction: none disclosed.** No adoption numbers, no lift in subscriptions/engagement attributed to the recommender — it is an announced capability, not a measured result. **Who captures the margin (analysis):** For value to be real, recommendations must raise channel subscriptions → feed ad inventory (VK Реклама cabinet) and Yandex Direct targeting → realized ad revenue. But VK still shares payment economics with banks (VTB/Alfa rails) and, on the ad side, demand flows partly through Yandex Direct — so Max risks owning the commoditized *inventory/surface* while the ad network above it captures the performance-ad margin. A recommendation engine improves the top of the funnel; it does not by itself decide who books the high-margin economics.

## [4] What's next / market sentiment
Expect continued feature-velocity (CEO flagged stories, multi-pin, comment threads for Q1 2027) and monetization rollout atop the discovery funnel — more channel ads, the Partner Platform (commerce/payments, ~Oct 23), and eventual Max Pay. The regulatory backdrop is the whole story: WhatsApp blocked, Telegram throttled, Apple pulled Max from the App Store (Jun 2026) — hostile Western distribution, guaranteed domestic distribution. **Counterintuitive second-order (analysis):** An algorithmic recommender optimized over a largely *administratively-created* channel base (schools, ЖК, gov) can surface low-engagement institutional channels, inflating subscription counts without proving the ad-receptive attention monetization needs. The surveillance/no-E2E-encryption reputation (InterSecLab/Meduza; data shared with security services) caps voluntary stickiness and foreign reach, so recommendations improve domestic funnel mechanics but cannot fix the trust ceiling that bounds ad effectiveness and payments uptake.

## Top challenge/extra questions
See challenge column.

## Sources
- cnews.ru (primary, in note): https://www.cnews.ru/news/line/2026-10-15_v_max_poyavilis_novye_funktsii
- RBC: https://rb.ru/news/max-obnovil-prilozhenie-v-messendzhere-poyavilis-rekomendacii-kanalov-i-arhiv-istorij/
- Vedomosti: https://www.vedomosti.ru/technology/news/2026/10/15/1237295-max-dobavil-funktsii
- RIA: https://ria.ru/20261015/maks-2124660199.html
- Rossiyskaya Gazeta: https://rg.ru/2026/10/15/v-max-poiavilis-rekomendacii-kanalov.html
- Max (app) — Wikipedia: https://en.wikipedia.org/wiki/Max_(app)
- Telegram/WhatsApp throttling timeline: https://www.csmonitor.com/World/Europe/2026/0325/russia-max-telegram-whatsapp-internet-disruption
- Max dominated by state channels (Meduza): https://meduza.io/en/feature/2026/02/19/russia-s-national-messenger-was-billed-as-a-platform-for-the-people-it-s-dominated-by-state-run-channels
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge questions**

1. **Is this fresh or a duplicate?** Fresh — these specific features (channel-recommendation algorithm, story archive, media auto-save, text size, announced 2026-10-15) are distinct from the sibling Max notes: polls ([[Max adds multi-choice polls with revoting in channels]], ~Oct 6), ad cabinet ([[VK opens Max channel ads to accounts over 1K subscribers]], Oct 12), Q3 channel KPIs ([[VK grows Max public channels to 530K in Q3 2026]]). Same platform/sprint, different capabilities — not a reprint.
2. **Is it a meaningful event or trivial parity?** Mostly trivial: archive, media auto-save and font size are table-stakes Telegram/WhatsApp have had for years. Only the channel-recommendation algorithm has product/business weight.
3. **Announced or live?** Spokesperson statement to CNews; features described as available, but no independent usage verification and no adoption metrics — "live" per PR, effect unmeasured.
4. **Does the recommender touch fintech/payments at all?** Only indirectly: recommendations → subscriptions → channel ad inventory. Payments leg still gated (CBR called Max financial-ops confirmation "premature," Mar 2026). No direct fintech content.
5. **Is channel growth being recommended on an organic base?** No — ~70% of Max channels are government/institutional (Agentstvo/Meduza). A recommender over a coerced supply base can inflate subscriptions with low-engagement channels.
6. **Who captures the margin?** Recommendations feed the top of the funnel; ad demand partly flows through Yandex Direct and payments through VTB/Alfa rails — Max risks supplying commoditized inventory while others book the high-margin economics. Open.
7. **Is the recommendation algorithm novel?** No in absolute terms — a copy of Telegram's "similar channels." Novel only for Max / in a coerced-distribution market.
8. **How much is discovery vs surveillance signal?** Interest/interaction-based recommendations imply behavioral profiling on a no-E2E-encryption platform reported to share data with security services — a privacy overhang, not disclosed. Open.
9. **Does any of this move a monetizable metric?** Not disclosed — no subscription lift, no ad-fill or ARPU read. Pure engagement scaffolding at this stage.
10. **Why bundle a discovery algorithm with cosmetic toggles in one PR?** Likely to normalize the recommender as routine housekeeping; flattening obscures the one strategically significant feature. (analysis)
11. **Single-vendor sourcing?** Primary is a Max spokesperson statement re-reported identically across RBC/Vedomosti/RIA/RG — one vendor announcement, multiple relays; no independent corroboration of behavior.
12. **Does it change VK's financials?** No — Max is still a pre-monetization cost/distribution bet; not a disclosed revenue line. Strategic, not financial.
13. **Competitive moat created?** None on merit — the moat is regulatory (pre-install + rival blocking); a recommender is UX catch-up, not a defensible edge.
14. **International relevance?** Minimal — App Store removal (Jun 2026), surveillance reputation cap foreign/voluntary adoption. Domestic-only.
15. **What would make this 4-5/5?** Disclosed subscription/engagement lift from recommendations tied to ad revenue, or a payments-leg unlock. None present.

**Importance: 2/5 — rationale.** A mostly cosmetic UX-parity bundle (story archive, media auto-save, text size) whose only strategically relevant element is a Telegram-cloned channel-recommendation algorithm — a discovery-funnel brick in the broader Max super-app/monetization build-out, where the ad-cabinet and Q3-KPI notes already carry the 2-3/5 substance. Fresh and dated, but low-materiality on its own, single-vendor-sourced, non-fintech (payments gated), with no disclosed traction and a moat that is regulatory, not product. A line for the Russian digital-infra beat, not a standalone fintech event.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is the Russian "national messenger"/super-app race: VK's Max vs incumbent Telegram and WhatsApp. The news (channel recommendations, story archive, media auto-save, text sizing) is a feature-parity push, not a monetization event — the engagement layer that precedes the ad/payments monetization VK switched on days earlier ([[VK opens Max channel ads to accounts over 1K subscribers]], 2026-10-12). Structure: state-driven, not market-driven. Max is pre-installed by law on all smartphones sold in Russia since Sept 2025, carriers waive its data fees (The Moscow Times, 2026-07-31), and Roskomnadzor restricts rivals — WhatsApp/Telegram traffic has fallen materially (iz.ru; csmonitor, 2026-03-25). Scale: Max passed 100mn registered users by Mar 2026 (107mn per www1.ru, 2026-03-29); but registered ≠ active — Q4 2025 average monthly audience was only ~20.2mn globally / ~18.9mn in Russia (VK press release, via search). Drivers/"why now": (1) regulatory moat — forced distribution + rival throttling; (2) Max is explicitly a WeChat clone (messaging + Gosuslugi/ESIA digital ID + planned banking/payments), so each engagement feature compounds the super-app funnel (france24, 2026-03-23; biometricupdate, 2026-09).

**Competitive landscape.** Sector KPIs: MAU/DAU, messages/day, channel count, subscriptions, and (downstream) ad ARPU / payments attach. Players & basis of competition: Telegram (product/network effects, ~96mn RU users Jan 2026, most-popular in Russia — caliber.az/meduza) and WhatsApp (~89mn RU, declining) compete on product and incumbency; Max competes almost entirely on distribution/regulation, not product. The channel-recommendation feature is a direct lift of Telegram's discovery/creator playbook (same 1K-subscriber ad-eligibility floor Telegram uses), and VK is growing Max channels fast: 530K public channels in Q3 2026, +58% QoQ, 355mn subscriptions +39% QoQ ([[VK grows Max public channels to 530K in Q3 2026]]). Protagonist position: catching up on product, ahead on forced distribution (analysis). Moat = regulatory/distribution, not switching costs or network effects — brittle because it depends on policy, not user preference (analysis).

**Comps & multiples.** No deal/valuation in this product news → no transaction multiple to compute. Parent VK FY2025 (IR-grounded): revenue RUB 160bn (+8% YoY); adjusted EBITDA RUB 22.6bn vs −RUB 4.9bn in 2024; EBITDA margin ~14% (Interfax; VK Q4/FY2025 press release, 2026-03-19; corp.vkcdn.ru PDF). Segments: Social Platforms & Media Content RUB 109.8bn (+5%), EBITDA RUB 21.1bn; VK Tech RUB 18.8bn (+38%), EBITDA RUB 4.8bn; EdTech RUB 7.4bn (+19%). Max sits in Social Platforms. Net debt more than halved in 2025, but VK still logged a 6th straight annual net loss (The Moscow Times, 2026-03-19) — EBITDA-positive, bottom-line negative. Internal comps (same super-app/messenger cluster): [[VK opens Max channel ads to accounts over 1K subscribers]], [[VK grows Max public channels to 530K in Q3 2026]], [[Max adds multi-choice polls with revoting in channels]], [[Yandex Direct adds personalized ad targeting under Max posts]]. Trading multiples (EV/Rev, EV/EBITDA): no clean free source for VK current EV/market cap → [UNSOURCED]; distribution not computed.

**Risk flags.** (1) Regulatory-dependence / reversibility — Max's entire advantage is mandated distribution + rival throttling; a policy shift or even user passive resistance (registered-but-inactive gap: 100mn+ registered vs ~19mn RU MAU) erodes the thesis faster than any competitor could. (2) Engagement vs scale mismatch — shipping Telegram-like discovery features does not close the ~20mn MAU vs ~96mn Telegram gap; feature parity without organic pull risks a "ghost network" where channels exist but attention doesn't. (3) Monetization/thin P&L — VK is EBITDA-positive but still loss-making after 6 years; Max monetization (ads just launched, payments/banking only planned) is early and unproven, so this feature sits far upstream of revenue.

**What this changes (idea-lens).** For the sector: incremental, not a re-rating — it's engagement plumbing feeding the already-launched ad cabinet and the planned super-app payments stack (analysis). Watch the MAU/DAU trajectory and ad ARPU in the next VK quarterly, not channel counts: the falsifiable thesis is "forced distribution converts to durable active usage." Trigger that would confirm it — RU MAU closing on Telegram's ~90mn; what would break it — registered base keeps climbing while MAU/engagement stalls, confirming compliance-not-preference adoption (analysis).

Sources: https://vk.company/en/press/releases/12255/ · https://corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf · https://interfax.com/newsroom/top-stories/116698/ · https://www.themoscowtimes.com/2026/03/19/vk-logs-6th-straight-annual-loss-despite-revenue-growth-a92270 · https://www.themoscowtimes.com/2026/07/31/russian-mobile-carriers-waive-data-fees-for-state-backed-max-messenger-a93386 · https://www.france24.com/en/live-news/20260323-russia-s-max-the-unencrypted-super-app-being-forced-on-citizens · https://www.csmonitor.com/World/Europe/2026/0325/russia-max-telegram-whatsapp-internet-disruption · https://caliber.az/en/post/telegram-becomes-russia-s-most-popular-messenger
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Context-only — no earnings in this news.** The item is a Max product update (channel recommendations, story archive, media auto-save, text-size settings), not a financial report. VK is IR-covered, so the relevant financial backdrop from VK's own IFRS filings:

**Latest print — H1 2026 (reported ~Aug 2026).** Revenue RUB 81.04 bn, +11.7% YoY (vs RUB 72.6 bn in H1 2025). EBITDA RUB 14 bn, +34% YoY. Net loss narrowed sharply to RUB 3.846 bn, vs a RUB 12.67 bn loss in H1 2025 — a ~70% improvement, the clearest sign the 2025 cost-discipline/margin turn is holding. Q2 2026 alone: revenue RUB 43.5 bn (+17% YoY), EBITDA RUB 7.6 bn (+41% YoY), online advertising RUB 26.7 bn (+14%). Online advertising for H1 2026 reached RUB 48.6 bn (+8%), with large-business advertising RUB 29.1 bn (+12%). (web — akm.ru / telecompaper, period-confirmed as Russian VK, IFRS/RUB.)

**Last audited full year — FY2025 (filing in irdb, released 2026-03-19).** Revenue RUB 160 bn, +8% YoY. Adjusted EBITDA RUB 22.6 bn, swinging from −RUB 4.9 bn in 2024; EBITDA margin ~14%. Net loss RUB 24.9–25.4 bn — VK's sixth straight annual loss, though narrowed from a RUB 94.9 bn loss in 2024. VK Tech segment revenue RUB 18.8 bn, +38% YoY (H1 2025 VK Tech +48% to RUB 6.7 bn). (filing: ENG Press Release 12M 2025 · drive_url https://corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf · web: interfax / Moscow Times.)

**Why the Max features matter to the thesis.** Max (the state-backed "national messenger") passed 100 mn registered users and ~70 mn DAU by March 2026. Channel recommendations + story archive are engagement/retention plumbing: the recommendation feed is the discovery rail that turns a messaging base into an addressable ad/content surface, i.e. the pipe from DAU toward the advertising line that still drives ~60% of group revenue. (hypothesis — the release gives no Max monetization figures; no Max revenue or ARPU is broken out in VK's segments to date.) De-PR: VK touts the user milestone and feature cadence but discloses no Max-level revenue, no advertising-load, and no cost of the Max build — and the group is still 6 years loss-making, so Max remains a cost/strategic bet, not yet a reported earnings driver.

**Guidance.** VK does not issue specific numeric revenue/EBITDA guidance; management framing is continued double-digit revenue growth with EBITDA margin expansion. H1 2026's +34% EBITDA on +11.7% revenue confirms operating leverage is the live story. No Max-specific targets given — [UNSOURCED].

Sources: https://www.akm.ru/eng/news/vk-s-net-loss-under-ifrs-for-the-first-half-of-the-year-amounted-to-3-846-billion-rubles/ · https://www.akm.ru/eng/news/vk-s-revenue-for-the-second-quarter-according-to-ifrs-increased-by-17/ · https://corp.vkcdn.ru/media/files/ENG_Press_Release_12M_2025.pdf · https://interfax.com/newsroom/top-stories/116698/ · https://www.themoscowtimes.com/2026/03/19/vk-logs-6th-straight-annual-loss-despite-revenue-growth-a92270 · https://vk.company/en/press/releases/12248/ (Max 100 mn users). Note: ticker "VK" also belongs to Vallourec SA — those figures were excluded.
<!-- /enrichment:earnings_review -->
