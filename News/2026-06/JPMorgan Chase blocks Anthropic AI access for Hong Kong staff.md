---
title: "JPMorgan Chase blocks Anthropic AI access for Hong Kong staff"
date: 2026-06-19
tags:
  - company/jpmorgan
  - company/anthropic
  - industry/banking
  - region/asia
  - type/regulation
sources:
  - https://www.connectingthedotsinfin.tech/r/3f1ac9f7
  - https://www.futureofbanking.info/r/946af70c
status: published
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
  - "Future of Banking"
story_id: sf50cc2f9
month: 2026-06
enriched: true
importance: 3
---

# JPMorgan Chase blocks Anthropic AI access for Hong Kong staff

> [!info] 2026-06-19 · 2 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Future of Banking

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇭🇰 JPMorgan Chase cuts off Anthropic access for its Hong Kong staff. The decision is linked to licensing and usage restrictions for Greater China, highlighting the growing regulatory and compliance challenges surrounding AI adoption in global financial institutions.

[Future of Banking] 🇭🇰 JPMorgan Chase cuts off Anthropic access for its Hong Kong staff. The decision is linked to licensing and usage restrictions for Greater China, highlighting the growing regulatory and compliance challenges surrounding AI adoption in global financial institutions.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/3f1ac9f7>
- <https://www.futureofbanking.info/r/946af70c>

## Контекст

<!-- enrichment:context -->
## [0] Суть события

JPMorgan Chase убрал модели Claude (Anthropic) из внутреннего выпадающего меню одобренных ИИ-инструментов для сотрудников в Гонконге. Поводом стала строгая интерпретация банком пользовательского соглашения Anthropic: в нём явно запрещено использование сервисов в «Большом Китае» (Greater China), включая Гонконг и Макао. Это не регуляторное предписание SFC или HKMA — банк действовал по собственному compliance-решению, читая контракт буквально.

Событие вписывается в более широкую волну: ещё в апреле 2026 Goldman Sachs заблокировал Claude для своих гонконгских банкиров, сохранив доступ к ChatGPT и Gemini. Goldman также проконсультировался с Anthropic и пришёл к тому же выводу. Ни одна из двух компаний не получала прямого предписания от регулятора — речь идёт о самостоятельных compliance-решениях на основании контрактных терминов.

Источники: [American Banker](https://www.americanbanker.com/news/jpmorganchase-blocks-hong-kong-staff-from-using-claude), [Bloomberg / Goldman](https://www.bloomberg.com/news/articles/2026-04-29/goldman-staff-in-hong-kong-lose-access-to-anthropic-s-claude), [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/jpmorgan-blocks-anthropic-ai-models-111631812.html)

## [1] Почему Anthropic не поддерживает Гонконг

Anthropic официально не перечисляет Гонконг, Макао и материковый Китай в списке поддерживаемых регионов (ни для Claude.ai, ни для коммерческого API). Политика компании сформировалась под влиянием нескольких факторов:

1. **Экспортные соображения США.** Китай — юрисдикция, ограниченная по соображениям национальной безопасности. Гонконг после 2020 года де-факто перешёл под контроль КНР, поэтому попал под те же ограничения.
2. **Обновлённая политика продаж.** В 2025–2026 гг. Anthropic ужесточил условия: теперь запрещено использование моделей не только напрямую из ограниченных регионов, но и через дочерние структуры компаний, более чем на 50% подконтрольных юрисдикциям из стоп-листа. [Официальное обновление Anthropic](https://anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions).
3. **Экспортный контроль июня 2026 г.** 12–13 июня 2026 г. правительство США выпустило директиву об экспортном контроле, обязав Anthropic заблокировать доступ к Fable 5 и Mythos 5 для всех иностранных граждан — даже для сотрудников самой Anthropic с иностранным гражданством (например, Андрей Карпати). Это дополнительно усилило тревогу банков. [Al Jazeera](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals), [Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/)

Важно: блокировка JPMorgan касается прежде всего стандартных рабочих моделей Claude (LLM Suite), а не только Fable/Mythos — то есть это отдельная история от экспортного контроля на топ-модели.

## [2] Что JPMorgan использует вместо Claude

JPMorgan располагает собственной платформой **LLM Suite** — model-agnostic порталом для 230 000+ сотрудников, который агрегирует модели OpenAI и Anthropic. После удаления Claude из гонконгского меню сотрудники в Гонконге продолжают пользоваться инструментами на базе **OpenAI** (GPT-серия) через тот же LLM Suite. По данным американских медиа, именно OpenAI остаётся основным поставщиком моделей в LLM Suite. Кроме того, JPMorgan разрабатывает собственные специализированные агенты через платформу Kinexys (блокчейн/платежи) — см. [[Why JPMorgan built Kinexys for institutional blockchain settlements]]. Банк тратит $19,8 млрд в год на технологии и AI — стратегия ставит на диверсификацию поставщиков, а не на зависимость от одного вендора. [CNBC](https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html)

Параллельно другие банки в Гонконге выбрали иной путь: **Citibank HK** запустил Citi AI (доступен ~150 000 сотрудников в 11 странах) на базе собственных инструментов; **HSBC** активно участвует в HKMA GenAI sandbox вместе с Baidu и Alibaba Cloud. [Finviz/Citi](https://finviz.com/news/64264/citigroup-introduces-ai-tools-enhances-banking-operations-in-hong-kong)

## [3] Регуляторный контекст: Гонконг и AI

Блокировка не является прямым следствием предписаний гонконгских регуляторов. Однако SFC и HKMA сформировали рамочный контекст:

- **SFC Circular (ноябрь 2024):** четыре принципа использования GenAI в лицензируемых видах деятельности — надзор старшего менеджмента, валидация моделей, кибербезопасность, риски третьих сторон. Инвестиционные рекомендации через AI признаны «высоким риском».
- **HKMA GenAI Sandbox (апрель 2025):** банки (BOC HK, Citi HK, Hang Seng, HSBC HK, Standard Chartered) тестируют GenAI совместно с Baidu и Alibaba Cloud — то есть доступны китайские альтернативы.
- **Patchwork-регулирование:** единого AI-закона нет, банки вынуждены интерпретировать руководство нескольких регуляторов одновременно.

Источники: [Beaumont Capital](https://beaumont-capitalmarkets.co.uk/featured_item/ai-financial-services-hong-kong-2025-regulations/), [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/hong-kong-financial-regulators-issue-rules-on-the-use-of-ai-102jrmt), [HKMA sandbox](https://www.itiger.com/news/2493473573)

## [4] Смежные истории и развитие темы

- **Broadridge + Project Glasswing:** в тот же день, 19 июня 2026, стало известно, что Broadridge присоединился к инициативе Anthropic Project Glasswing, используя нерелизный Claude Mythos Preview для киберзащиты критической инфраструктуры. Это парадокс: Anthropic расширяет партнёрства в финансовом секторе США, одновременно теряя доступ в азиатских офисах тех же финансовых институтов. [[Broadridge joins Anthropic Project Glasswing for frontier AI deployment]]
- **Trump vs. Anthropic / Fable 5:** Администрация Трампа требует от Anthropic доказать, что Claude Fable 5 не поддаётся джейлбрейку, прежде чем разрешить повторный выпуск. NSA подтвердило наличие уязвимостей. Это усиливает неопределённость вокруг доступности топ-моделей Anthropic для банков. [[Trump administration demands Anthropic prove Claude Fable 5 cannot be bypassed]]
- **OpenAI выигрывает от блокировки:** OpenAI предложил 9 крупным британским банкам доступ к GPT-5.5 Cyber — именно тем банкам, которым Anthropic заблокировал Mythos. Паттерн повторяется: банки в Гонконге переходят с Claude на OpenAI. [[OpenAI offers nine UK banks access to GPT-5.5 Cyber model]]
- **Kalshi строит агентов на Claude:** [[Kalshi builds Claude-based AI agent to stress-test prediction bets]] — пример того, что Claude остаётся востребованным в финтехе за пределами ограниченных регионов.
- **Гонконг как регуляторный узел:** [[ZA Bank launches Hong Kong's first digital-bank Southbound wealth service]] показывает, что Гонконг продолжает развивать цифровые финансы, но в условиях растущего разрыва между западными AI-сервисами и местным рынком.

Ключевой вывод: речь идёт не о технической несовместимости и не о прямом запрете регулятора, а о том, что банки самостоятельно, через compliance-интерпретацию условий вендора, создают AI-сегрегацию по географическому принципу. Гонконг оказывается в «серой зоне» между западными AI-экосистемами и китайскими альтернативами.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Ред-тим вопросы

1. **Контрактная vs. регуляторная причина.** Банк убрал Claude потому, что так требует контракт с Anthropic, — или потому, что боялся будущего регуляторного риска? Если причина чисто контрактная, то это новость о вендорных условиях, а не о «регуляторном давлении».

2. **Почему именно сейчас?** Goldman убрал Claude в апреле, JPMorgan — в июне. Anthropic не обновлял условия по Гонконгу недавно (ограничения существуют с момента запуска). Что изменилось: ужесточение внутренней compliance-проверки после Goldman? Реакция на новости об экспортном контроле Fable/Mythos? Или просто запаздывающая стандартизация?

3. **Масштаб блокировки: только Claude или всё?** Источники говорят об удалении Claude из выпадающего меню LLM Suite. Но могут ли гонконгские сотрудники всё равно использовать Claude через собственные аккаунты / VPN? Реальная ли это блокировка или символическое compliance-действие?

4. **Что именно было заблокировано?** Claude.ai (веб-интерфейс), API-интеграции в LLM Suite, или ещё и мобильное приложение? Данные из первоисточников на этот вопрос не отвечают однозначно.

5. **OpenAI и Google остались доступны: почему?** Если проблема в «Greater China restriction», то почему GPT и Gemini остаются разрешёнными? Microsoft (Azure OpenAI) и Google тоже имеют ограничения на использование в Китае, но банки их не блокируют. Это значит, что интерпретация условий избирательна?

6. **Конкурентный эффект на Anthropic.** Гонконг — крупнейший финансовый хаб Азии. Если американские банки убирают Claude, а местные банки (HSBC HK, Hang Seng) используют Baidu/Alibaba Cloud в HKMA sandbox — Anthropic рискует выбыть из азиатского enterprise-рынка структурно. Насколько это критично для Anthropic на фоне готовящегося IPO?

7. **Данные и суверенитет.** Основной риск — что данные гонконгских сотрудников попадают на серверы вне Китая? Или это риск того, что гонконгские власти могут потребовать доступ к переписке через AI? Ни один источник не раскрывает реальную мотивацию банков — только «лицензионные ограничения».

8. **Двойной стандарт по моделям.** Экспортные ограничения США (директива июня 2026) касаются Fable 5 и Mythos 5 — самых мощных моделей. LLM Suite JPMorgan использовал стандартные Claude (Claude 3.x или Claude Sonnet). Это разные ограничения по разным основаниям — журналисты их смешивают?

9. **Антропик как переговорная сторона.** Goldman «проконсультировался с Anthropic» перед блокировкой. Могла ли Anthropic выдать банку специальный enterprise-контракт с явным разрешением для Гонконга? Почему этого не произошло — нежелание Anthropic, или банки не стали добиваться исключения?

10. **Сигнал для других банков и регионов.** Блокировка в Гонконге — прецедент для Сингапура, Токио, Дубая? У Anthropic есть схожие (хотя и менее жёсткие) ограничения для ряда других юрисдикций. Можно ли ожидать эффекта домино в других азиатских офисах западных банков?

11. **Стратегический проигрыш Anthropic?** Broadridge присоединяется к Project Glasswing в тот же день, когда JPMorgan блокирует Claude. Это говорит о том, что Anthropic укрепляет позиции в США, одновременно системно теряя enterprise-позиции в Азии. Является ли это осознанной стратегией или непреднамеренным следствием политики экспортного контроля?

12. **Что будет с LLM Suite в Гонконге?** JPMorgan активно развивает агентный AI (450+ use cases в продакшене). Если у гонконгских сотрудников ограниченный набор одобренных моделей — это дифференцирует их возможности vs. коллег в США/Европе? Каков HR- и операционный риск?

13. **Верификация цифр.** «230 000 сотрудников» в LLM Suite — это глобально. Сколько из них в Гонконге? Новость не называет число затронутых сотрудников, что затрудняет оценку реального масштаба.

---

**Важность: 3/5** — Обоснование: история значимая как сигнал о растущей AI-сегрегации по географическому признаку в глобальном банкинге и косвенный удар по позициям Anthropic перед IPO в азиатском enterprise-рынке. Однако непосредственный операционный эффект ограничен: JPMorgan не теряет AI-возможности в Гонконге — сотрудники переходят на OpenAI в том же LLM Suite. Блокировка не вызвана прямым регуляторным предписанием и не является отраслевым кризисом. Масштаб затронутых пользователей неизвестен. Потенциально важная долгосрочная тенденция, но конкретное событие — compliance-решение одного банка по читке контракта вендора.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Включено в дайджест [[Posts/2026-06-19]] — 2026-06-19.
<!-- /enrichment:post -->
