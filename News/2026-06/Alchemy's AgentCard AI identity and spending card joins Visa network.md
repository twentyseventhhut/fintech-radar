---
title: "Alchemy's AgentCard AI identity and spending card joins Visa network"
date: 2026-06-19
tags:
  - company/alchemy
  - company/visa
  - industry/agentic-commerce
  - industry/payments
  - region/us
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/8661d485
  - https://www.connectingthedotsinpayments.com/r/087484c1
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Connecting the Dots in Payments"
story_id: s01c38cc7
month: 2026-06
enriched: true
importance: 3
---

# Alchemy's AgentCard AI identity and spending card joins Visa network

> [!info] 2026-06-19 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Connecting the Dots in Payments

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Alchemy's AI-driven identity and payment service gains access to the Visa network. The integration allows AgentCard, a virtual ID and spending card for AI agents, to access Visa Intelligent Commerce to book a vacation, order groceries, or renew a subscription, without the consumer ever touching a checkout screen.

[Connecting the Dots in Payments] 🇺🇸 Alchemy's AI-driven identity and payment service gains access to the Visa network. The integration allows AgentCard, a virtual ID and spending card for AI agents, to access Visa Intelligent Commerce to book a vacation, order groceries, or renew a subscription, without the consumer ever touching a checkout screen.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/8661d485>
- <https://www.connectingthedotsinpayments.com/r/087484c1>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Alchemy AgentCard получает доступ к сети Visa
_Аналитические заметки (не пост). Важность: 3/5._

## [0] Что конкретно произошло (без PR)
18 июня 2026 Alchemy (инфраструктурная блокчейн-компания, основана 2017, $10.2 млрд оценка по Series C 2022, продаёт «AWS для блокчейна» — RPC/ноды/девтулы) представила **AgentCard** — «виртуальную личность + платёжную карту» для ИИ-агентов, построенную поверх **Visa Intelligent Commerce**. По единому API за «менее минуты» агент получает: токен Visa, выделенный email (`@agentcard.email`), номер телефона и криптокошелёк. Заявленный сценарий — агент бронирует отпуск, заказывает продукты, продлевает подписку «без того, чтобы потребитель касался экрана checkout».

**Де-PR'нутая суть:** это НЕ новая платёжная сеть и НЕ новая возможность Visa. Это **обёртка-онбординг** поверх уже существующего рельса Visa Intelligent Commerce (запущен Visa ~апрель 2025, [[Visa launches Intelligent Commerce Connect for agentic commerce]]). Реальная дельта Alchemy — упаковка четырёх примитивов (платёжный токен + email + телефон + кошелёк) в один вызов API, чтобы агенту дать «человекоподобную» цифровую идентичность для прохождения checkout/верификаций. Транзакции идут на токенах Visa, сохраняя кэшбэк/кредитную линию/льготы карты — то есть карта потребителя не пересоздаётся, агенту делегируется токенизированный доступ.

**Live vs анонс — расхождение источников:** CoinDesk формулирует «agents *now have access*» (живо) и подчёркивает мульти-рельсовость («лучший доступный механизм оплаты», фолбэк на single-use токены). PYMNTS подаёт как пресс-релиз без названных мерчантов/агентов-партнёров и **без единой цифры** (нет объёмов, числа агентов, GMV). Трактую как **продукт объявлен/в раннем доступе, без публичного трекшна** — классический «launched but not proven».

**Почему так структурировано (аналитика):** email+телефон+кошелёк рядом с платёжным токеном — потому что узкое место агентной коммерции не «как списать деньги» (это решают Visa/Mastercard токенами), а «как агенту пройти KYC-подобные барьеры мерчанта»: подтверждение почты, OTP на телефон, аккаунт. Alchemy продаёт «паспорт агента», а платёж — лишь один из его реквизитов.

## [1] Конкуренты / пиры
Поле плотное и в основном **инфраструктура поверх тех же двух сетей**:
- **Сами сети:** Visa Intelligent Commerce (рельс, на котором стоит AgentCard) и **Mastercard Agent Pay / Agent Pay for Machines** — последний запущен **10 июня 2026 с 30+ партнёрами**, и среди «initial participants» **числится сама Alchemy** ([[Mastercard launches Agent Pay for Machines for machine-speed payments]]). То есть Alchemy одновременно строит на Visa (AgentCard) и участвует в экосистеме Mastercard — она агностик к сети, а не «Visa-команда».
- **Прямые аналоги обёртки-идентичности:** Skyfire (KYA «Know Your Agent» / KYAPay), PayOS (вышел из стелса апр-2025, network-issued Agent Tokens на Visa и Mastercard), Crossmint, Nevermined (с которым Visa+Coinbase делали делегирование Visa-карт агентам ещё в апреле — [[Visa and Coinbase team with Nevermined on AI agent commerce]]), Catena, Skyfire.
- **Сама Alchemy 2 месяца назад:** [[Alchemy launches AgentPay AI payments tools]] (апр-2026) — «трансляционный слой» между протоколами (Coinbase x402, Stripe, Visa, Mastercard, Circle), не держащий средства. AgentCard — следующий шаг вверх по стеку: от «роутера протоколов» к «идентичности агента».

**Позиция:** паритет/догоняет. Возможность (агент платит токеном Visa с лимитами) уже была у Nevermined+Visa в апреле и системно — у Mastercard Agent Pay. Новизна AgentCard — UX-упаковка (минута на онбординг) и связка идентичности, а не сам платёж.

**Второпорядковая динамика (аналитика):** маржу платёжного рельса захватывают Visa/Mastercard (interchange + токен-вольты). Обёрточные игроки (Alchemy, Skyfire, PayOS) конкурируют за тонкий слой «идентичность/онбординг агента», который легко коммодитизируется — сети могут поглотить его сами (у Visa уже есть Intelligent Commerce Connect как «on-ramp»). Риск Alchemy — остаться «дев-удобством», а не точкой захвата стоимости.

## [2] История компании / встраиваемость
Alchemy — инфра-провайдер блокчейна ($545M+ всего привлечено, $10.2 млрд оценка 2022, основатели Nikil Viswanathan / Joe Lau). Траектория 2026: апрель — [[Alchemy launches AgentPay AI payments tools]] (роутер протоколов); инвестор через Alchemy Ventures в [[AEON raises $8 million to build settlement layer for AI agents]] (май, settlement-слой для агентов); ранее — серия playbook'ов по стейблкоинам/депозит-токенам для банков ([[Alchemy publishes bank playbook on stablecoins versus deposit tokens]]).

**Почему компания так действует (аналитика):** базовый бизнес Alchemy — коммодити-инфраструктура (RPC/ноды), где take-rate под давлением. Логичный ход — двигаться вверх по стеку в более маржинальные «приложения»: агентные платежи и идентичность как новая высоко-нарративная категория. AgentCard — продолжение этого дрейфа от «нод» к «экономическому актору» (цитата CEO: «AI-агенты — следующий новый экономический актор»). Встраиваемость высокая: у Alchemy уже есть кошельки/девтулы, добавить email+телефон+токен — органично.

## [3] Новизна / value-add / traction
**Что реально ново:** не платёж и не делегирование (это уже было), а **сшивка «полная идентичность агента в один API за минуту»**: токен Visa + email + телефон + кошелёк. Это снимает реальную боль — агенту нужны не только деньги, но и почта/телефон для OTP, аккаунтов, верификаций мерчанта.

**Трекшн:** не подтверждён. Нет названных мерчантов/агентов в проде, нет объёмов, нет числа выпущенных AgentCard, нет данных по конверсии/фроду. PYMNTS прямо без цифр. → По стандарту скилла: «piloted/framed ≠ live».

**Кто захватывает маржу (аналитика):** платёж идёт по рельсу Visa (interchange + токен), значит экономика транзакции у Visa/эмитента. Alchemy монетизирует, вероятно, API/подписку/комиссию за провижининг идентичности — слой, который сети и сами строят (Intelligent Commerce Connect, Mastercard Agent Pay). Мультипликатор value-add держится только если Alchemy станет дефолтным «реестром идентичности агентов» с сетевым эффектом; иначе — тонкая, дизинтермедиируемая прослойка.

**Молчат о:** ответственности за фрод (кто платит, если агент-«паспорт» скомпрометирован — открыто), экономике (take-rate Alchemy), эксклюзивности с Visa (её нет — мульти-рельс), реальном объёме.

## [4] Что дальше / настроения рынка
Сектор агентных платежей — горячий нарратив 2026: все три сети (Visa Intelligent Commerce, Mastercard Agent Pay, Amex Agentic Commerce) + десятки стартапов. McKinsey: до $5 трлн коммерции в орбите ИИ-агентов к 2030 (из [[Alchemy launches AgentPay AI payments tools]]). Visa Intelligent Commerce Connect ожидался к GA ~июнь 2026.

**Почему рынок пойдёт так (аналитика):** в ближайший год — гонка стандартов идентичности агента (KYA), а не платежа; платёж уже решён сетями. Контринтуитивный эффект 2-го порядка: чем больше «обёрток» (AgentCard, Skyfire, PayOS) строится поверх Visa/Mastercard, тем сильнее **сети, а не обёртки** — последние взаимозаменяемы и давят маржу друг друга вниз. Реальный вопрос смещается с «есть ли у Alchemy AI-история» на «успеет ли Alchemy закрепить идентичность агента как сетевой стандарт до того, как Visa/Mastercard поглотят этот слой».

**Риски:** коммодитизация слоя идентичности; фрод/ответственность при делегировании; регуляторика делегированных платежей и KYC агента; отсутствие доказанного спроса (нет цифр).

## Источники
- CoinDesk, 18.06.2026 — https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network
- PYMNTS — https://www.pymnts.com/partnerships/2026/alchemy-teams-with-visa-ai-agent-payment-stack/
- SalesTechStar (пресс-релиз) — https://salestechstar.com/predictive-ai-artificial-intelligence/alchemy-introduces-agentcard-a-payments-and-identity-platform-for-ai-agents-built-on-visa-intelligent-commerce/
- Mastercard Agent Pay for Machines (Alchemy в участниках), 10.06.2026 — https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- Genfinity (30+ партнёров Mastercard) — https://genfinity.io/2026/06/10/mastercard-agent-pay-for-machines-launch/
- Visa Intelligent Commerce / Connect — https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-intelligent-commerce-connect-ai-shopping-for-businesses.html
- Crossmint, сравнение agent card payments — https://www.crossmint.com/learn/agent-card-payments-compared
- Alchemy оценка $10.2 млрд — https://techcrunch.com/2022/02/08/alchemy-which-aims-to-be-the-de-facto-platform-for-developers-to-build-on-web3-raises-another-200m-and-is-now-valued-at-10-2b/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Топ челлендж/ред-тим вопросы (2-го порядка)

1. **Это правда новое или активация существующего рельса?** Возможность «агент платит токеном Visa с лимитами» уже была у Nevermined+Visa (апр-2026) и системно у Mastercard Agent Pay. → Новое — только UX-обёртка идентичности (токен+email+телефон+кошелёк за минуту), а не платёжная способность. **Ответ: новизна инкрементальная, на уровне онбординга, не механизма.**

2. **Live или анонс?** CoinDesk: «now have access» (живо); PYMNTS: пресс-релиз без партнёров и без цифр. → **Ответ: объявлено/ранний доступ, публичного трекшна нет. Считать «не доказано».**

3. **Эксклюзив с Visa?** Нет: CoinDesk говорит о мульти-рельсе («лучший доступный механизм»), а Alchemy числится участником Mastercard Agent Pay for Machines (10.06). → **Ответ: AgentCard на Visa, но Alchemy сетево-агностична; «joins Visa network» — частная правда.**

4. **Кто несёт ответственность за фрод?** Если «паспорт агента» (email/телефон/токен) скомпрометирован и агент тратит лишнее — кто платит: потребитель, эмитент, Visa, Alchemy? Источники молчат. → **открыто.**

5. **Какая юнит-экономика у Alchemy на этом?** Платёж идёт по interchange Visa; Alchemy зарабатывает на API/провижининге идентичности. Какова комиссия/подписка? Не раскрыто. → **открыто.**

6. **Кто захватывает маржу в стеке?** Транзакционная экономика — у Visa/эмитента; Alchemy держит тонкий слой идентичности. → **Ответ: маржу транзакции захватывает сеть; Alchemy — за коммодитизируемый онбординг-слой.**

7. **Сколько AgentCard реально выпущено / какой объём?** Ни одного числа (агентов, мерчантов, GMV, конверсии). → **открыто (красный флаг отсутствия трекшна).**

8. **Чем AgentCard отличается от Skyfire KYA и PayOS Agent Tokens?** Все трое — обёртки идентичности поверх Visa/Mastercard. Дифференциатор Alchemy — «минута на онбординг» + криптокошелёк рядом. → **Ответ: дифференциация слабая, поле переполнено; защитимость под вопросом.**

9. **Почему именно email+телефон, а не только платёж?** Узкое место — не списание денег, а прохождение KYC/OTP/аккаунтов мерчанта. → **Ответ: настоящий value — «человекоподобная идентичность» агента, платёж вторичен.**

10. **Поглотят ли сети этот слой?** У Visa есть Intelligent Commerce Connect как «on-ramp»; у Mastercard — Verifiable Intent/Agentic Tokens. → **Ответ (гипотеза): высокий риск дизинтермедиации — сети могут встроить идентичность сами.**

11. **Меняет ли это центральный вопрос оценки?** Да: с «есть ли у Alchemy AI-история» на «успеет ли Alchemy сделать идентичность агента сетевым стандартом до поглощения сетями». → **Ответ: вес новости — в гонке за стандарт идентичности, а не в «доступе к Visa».**

12. **Нет ли конфликта: Alchemy и на Visa, и в Mastercard?** Нет конфликта, но «joins Visa network» как заголовок преувеличивает аффилиацию. → **Ответ: это позиционирование, не эксклюзив.**

13. **Что с регуляторикой делегированных платежей и KYC агента?** Кто верифицирует, что за агентом стоит реальный потребитель и согласие (consent)? Visa требует spend controls/auth, но юр-рамка делегирования открыта. → **открыто.**

14. **Криптокошелёк — для чего реально?** Вероятно для стейблкоин-расчётов/x402-микроплатежей (логика прошлого AgentPay). В пресс-релизе про крипто-использование не сказано. → **открыто (гипотеза: мост к стейблкоин-рельсам).**

15. **Триггер даунсайда?** Если за 6-12 мес нет названных мерчантов/объёмов, а сети выкатят встроенную идентичность — AgentCard станет «фичей», а не продуктом. → **Ответ: главный риск — отсутствие доказанного спроса + коммодитизация.**

**Важность: 3/5 — обоснование.** Тема стратегически значимая (агентные платежи — ключевой нарратив 2026, $5 трлн к 2030 по McKinsey), и сшивка полной идентичности агента в один API решает реальную боль. Но: (1) платёжная способность не нова — рельс Visa существует с 2025, делегирование показывали Nevermined и Mastercard ранее; (2) нулевой публичный трекшн (ни мерчантов, ни объёмов, ни цифр); (3) поле переполнено взаимозаменяемыми обёртками (Skyfire, PayOS, Crossmint), а маржу держат сети, не обёртки. Не 4/5 — нет доказанного value-add и трекшна; не 2/5 — игрок ($10.2 млрд) и категория значимы, а продукт встроен в горячую гонку стандартов идентичности агентов.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Включено в дайджест [[Posts/2026-06-21]] — 2026-06-21.
<!-- /enrichment:post -->
