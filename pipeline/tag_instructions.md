# Tagging instructions (fintech news → Obsidian tags)

You assign precise semantic tags to fintech news stories. PRECISION over recall —
only tags that genuinely apply. Read each story's `agg_text` + `title_auto`.

For EACH story in your assigned slice where `is_news == true` (skip is_news==false),
output 3–6 namespaced tags. Target mix:
**1–2 company/ + 1–2 industry/ + EXACTLY 1 region/ + EXACTLY 1 type/.**

- **company/<name>** — ALWAYS include the 1–2 PRIMARY named entities (acquirer/target,
  the funded startup, the company shipping the product). Normalize: lowercase, hyphenated,
  no legal suffix. e.g. company/jpmorgan, company/stripe, company/nubank, company/revolut.
  Don't invent companies not named in the text. (A few macro/regulatory pieces may have none.)
- **industry/<area>** — closed seed (extend ONLY if clearly missing). Do NOT add `payments`
  unless it is truly a payments story:
  payments, cards, b2b-payments, remittances, fx, stablecoins, crypto, defi, blockchain,
  neobank, banking, baas, embedded-finance, open-banking, lending, bnpl, credit, mortgage,
  wealth, trading, capital-markets, insurtech, regtech, fraud-risk, infrastructure,
  spend-management, payroll, real-estate-fintech, agentic-commerce, ai
- **region/<geo>** — EXACTLY ONE, correct geography:
  us, canada, uk, europe, ru, latam, asia, india, africa, mea, global  (global = multi-region/none)
  Use **ru** for Russia (РФ) market news — Russian banks/fintechs/regulators/companies
  (ЦБ РФ, СБП, Сбер, Т-Банк, Альфа, ВТБ, Тинькофф, Wildberries/Ozon fintech, Яндекс, цифровой рубль, etc.)
  and Russia-focused items from the Russian-language source channels. RU news must NOT be tagged europe/asia/global.
  A purely CIS story with no clear Russia angle (Uzbekistan, Kazakhstan, …) keeps its own geo (e.g. asia), NOT ru.
- **type/<kind>** — EXACTLY ONE:
  funding, m-and-a, earnings, product, partnership, regulation, expansion, leadership,
  layoffs, ipo, outage-security, research-report, commentary

Output: STRICT JSON object `{"sID": ["company/..","industry/..","region/..","type/.."], ...}`
with an entry for EVERY is_news story in your slice. Validate it parses before writing.
