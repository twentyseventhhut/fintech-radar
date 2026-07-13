# Canonical tag vocabulary (Obsidian news archive)

Each note gets **3–5 tags**, namespaced with `/` (Obsidian nested tags). Aim:
**1–2 company + 1–2 industry + exactly 1 region + exactly 1 type.**

## company/<name>  (open set)
Normalized: lowercase, hyphenated, no legal suffix. The 1–2 PRIMARY entities in the story.
Examples: `company/nubank`, `company/revolut`, `company/brex`, `company/stripe`,
`company/jpmorgan`, `company/visa`, `company/mastercard`, `company/payoneer`,
`company/nuvei`, `company/klarna`, `company/coinbase`, `company/circle`, `company/ramp`.
(Skip if no clear company — e.g. macro/regulatory pieces.)

## industry/<area>  (closed seed — extend only if clearly missing)
payments, cards, b2b-payments, remittances, fx, stablecoins, crypto, defi,
neobank, banking, baas, embedded-finance, open-banking, lending, bnpl, credit,
wealth, trading, capital-markets, insurtech, regtech, fraud-risk, infrastructure,
spend-management, payroll, real-estate-fintech, agentic-commerce, ai

## region/<geo>  (closed — pick the single most relevant)
us, canada, uk, europe, ru, latam, asia, india, africa, mea, global
(`ru` = Russia (РФ) market news — Russian banks/fintechs/regulators/companies; NEVER tag these europe/asia/global.
A purely CIS story with no clear Russia angle (Uzbekistan, Kazakhstan, …) keeps its own geo, e.g. `asia` — not `ru`.
`global` = multi-region or no clear single geography.)

## type/<kind>  (closed — pick the single best)
funding, m-and-a, earnings, product, partnership, regulation, expansion,
leadership, layoffs, ipo, outage-security, research-report, commentary
