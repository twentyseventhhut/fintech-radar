---
title: "EU regulators question Google over London cloud outage"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - company/google
  - industry/infrastructure
  - industry/regtech
  - region/europe
  - type/regulation
sources:
  - https://www.reuters.com/business/finance/europes-financial-regulators-query-google-over-cloud-outage-that-hit-banks-2026-10-21
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s8caabcaf
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# EU regulators question Google over London cloud outage

> [!info] 2026-10-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] European regulators question Google over the cloud outage.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.reuters.com/business/finance/europes-financial-regulators-query-google-over-cloud-outage-that-hit-banks-2026-10-21>

## Контекст

<!-- enrichment:context -->
**What happened (dated).** On **Tue 20 Oct 2026** (~06:08 UTC / 07:08 UK) a "power event" in Google Cloud's **europe-west2-b** zone (London) knocked out services for hours. Multiple financial entities were hit: **Revolut** (card payments, top-ups, ATM withdrawals, FX, transfers, stock/crypto trading, sign-ins), **Lloyds/Halifax**, **HSBC**, plus open-banking rail **Tink** (full connectivity loss to Revolut UK). Outage reported across UK, Ireland, Italy, Netherlands, Romania and beyond. By **21 Oct** Reuters reported European financial regulators were formally questioning Google.

**The EU/EBA angle (this note).** The **European Banking Authority (EBA)** said it had **been in contact with Google Cloud** to obtain information on the incident, understand its implications and **assess potential impact on financial entities in the EU**. Key EBA framing: designation as a **Critical Third-Party Provider (CTPP)** establishes an EU-level oversight framework but **does NOT transfer responsibility for incident management from the provider, nor relieve financial entities of their own regulatory obligations**. This is the first real-world stress test of the EU oversight regime built on **DORA** (in force since 17 Jan 2025), under which the EU had designated 19 CTPPs including **Google Cloud EMEA Limited**.

**Regulatory backdrop (concentration risk).** The event crystallises the "concentration risk" DORA was designed to surface: a single physical fault at one hyperscaler simultaneously degraded many regulated firms. In the UK, parallel to the EU/EBA action, the **Treasury Committee** (chair Meg Hillier MP) wrote within hours to the **Bank of England** and **FCA** — nine questions, initial reply due **4 Nov 2026**, full detail by **20 Jan 2027**. The UK's own **Critical Third Parties** regime designated **Google, AWS, Microsoft, Oracle** effective **13 Jul 2026** (SI 2026/777), with joint BoE/PRA/FCA oversight. So the London outage landed ~3 months after the hyperscalers came under direct UK financial oversight.

**Related notes in vault:**
- [[Revolut outage linked to Google Cloud infrastructure problems]] — the operational incident itself (the trigger event).
- [[Treasury Committee questions regulators over cloud outage oversight]] — the UK Parliament/BoE/FCA twin (distinct regulator/action from this EU/EBA item).
- [[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]] — the Jul 2026 UK CTP designation that set up oversight powers.
- [[Bank of England runs sector-wide cloud outage drill with 38 firms]] — prior sector resilience exercise.
- [[How Monzo uses multi-cloud infrastructure to improve resilience]] — multi-cloud mitigation playbook.
- [[AWS outage disrupts UK banks' online services]] (2025-10) — near-identical precedent one year earlier (AWS, UK banks).

**Why it matters.** The questioning signals regulators are moving from framework-building to enforcement posture on cloud concentration. But note the limited scope: "being in contact / seeking information" is an early-stage inquiry, not a sanction or formal investigation. Real teeth would be CTPP incident-reporting demands, scenario-testing orders, or (UK) skilled-person reviews.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Is "EU regulators question Google" an actual investigation, or merely the EBA saying it is "in contact" seeking information? (Sources suggest the latter — an early inquiry, not enforcement.)
2. Which body is acting — EBA alone, or also ESMA/EIOPA and national competent authorities? The headline says "EU regulators" (plural) but only the EBA is clearly cited.
3. Is this the EU/EBA angle specifically, distinct from the UK Treasury Committee/BoE/FCA action? Yes — different regulator, different jurisdiction, different source (Reuters vs Parliament). Not a duplicate.
4. Was Google Cloud actually at fault in a way that triggers CTPP obligations, or was this a routine power failure with normal RTO? The EBA explicitly notes designation does not transfer incident-management responsibility to the provider.
5. How many EU-regulated entities were materially affected vs merely inconvenienced? Revolut is the headline casualty; quantified downtime/financial harm for other EU banks is unconfirmed.
6. Is there any formal DORA incident report filed, or just media reporting? No confirmation of a filed major-incident classification.
7. Could this prompt a binding CTPP oversight action (scenario testing, remediation orders), or will it fizzle as a fact-finding exercise? Unproven.
8. Does the outage expose a gap between designation (done Jan 2025 EU / Jul 2026 UK) and operational enforcement (untested until now)?
9. Is "London outage" even in EBA's jurisdiction post-Brexit? The physical zone (europe-west2) is UK, but it served EU customers — jurisdictional overlap is itself a story.
10. What is the counterfactual resilience expectation — were affected banks supposed to fail over to another region/provider (multi-cloud), and did any succeed (cf. Monzo)?
11. Does Google face any financial penalty, or is reputational/oversight pressure the only consequence? No penalty mechanism cited.
12. Is the "concentration risk" narrative overstated — one zone (-west2-b) failed, not all of Google Cloud; how much was single-AZ dependency by the banks themselves?
13. Timeline risk: Reuters dated 21 Oct, outage 20 Oct, note dated 22 Oct — is the note just echoing a one-day-old wire with no new development?
14. Does this materially change Google's EU cloud-finance business, or CaixaBank-style multi-year deals (cf. [[CaixaBank extends Google Cloud alliance to 2033]])? Likely negligible commercially.

**Importance: 3/5** — A genuinely notable first live test of the EU DORA / UK CTP cloud-concentration oversight regimes, with named casualties (Revolut, HSBC, Lloyds). But as a standalone item it is an early-stage "EBA seeking information" story that largely restates one Reuters wire; the heavier substance (the outage itself, the UK Treasury Committee's nine formal questions with deadlines) lives in sibling notes. Structurally significant for the resilience/regtech theme, low on immediate hard consequence.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-25]] (2026-10-25).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Market Research — cloud concentration risk & operational resilience** _(as of 2026-10-22; skeptical read)_

### What happened (the trigger)
On Tue 2026-10-20/21 a "power event" in a London-based Google Cloud network serving European customers knocked out core banking services for several hours. Revolut, Lloyds and HSBC were among the banks affected. The EBA says it contacted Google Cloud to understand the incident and assess impact on EU financial entities; the UK FCA said it was engaging with Google. ([Reuters via Global Banking & Finance](https://www.globalbankingandfinance.com/europes-financial-regulators-query-google-over-cloud-outage/))

### Sector context — cloud concentration in financial services
- **The Big Three dominate.** In Q2 2026 AWS held ~28% of global cloud-infrastructure spend, Microsoft ~20%, Google ~15% — roughly 67% combined, a share stable for ~2 years. ([tech-insider.org](https://tech-insider.org/au/google-cloud-15-percent-share-aws-falls-2026/)) This is the core "concentration risk" regulators cite: a single provider's failure can simultaneously degrade many regulated firms — exactly what the London event demonstrated across multiple banks.
- **Regulators have formalised the concern.** The UK CMA's 2026 concurrency work found Amazon and Microsoft to have significant market power in cloud and flagged barriers limiting customer choice (lock-in, egress fees, interoperability). The Bank of England FPC (July 2026 Financial Stability Report) warned that dependence on common third-party tech — and AI-related services concentration — can magnify system-wide operational risk. ([Global Banking & Finance](https://www.globalbankingandfinance.com/the-hidden-concentration-risk-in-banking-s-dependence-on-microsoft-amazon-and-google/))

### Regulatory regime — DORA / CTPP oversight
- **This is the first live test of DORA's oversight arm.** On 2025-11-19 the ESAs (EBA, ESMA, EIOPA) designated **19 critical ICT third-party providers (CTPPs)** under DORA Art. 32(1) — the first time such firms fall under direct, Union-level financial oversight. The list includes **Google Cloud EMEA Limited, Amazon Web Services EMEA Sarl and Microsoft Ireland Operations Limited**, alongside IBM, Oracle, SAP, FIS, LSEG, Equinix, Accenture, Capgemini, TCS, NTT Data, Kyndryl and telco/colo players. ([FMA Austria](https://www.fma.gv.at/en/european-supervisory-authorities-publish-list-of-critical-ict-service-providers/), [PwC Legal](https://legal.pwc.de/en/news/articles/esas-publish-first-list-of-critical-ict-third-party-providers-under-dora))
- **Oversight mechanics.** CTPPs face direct ESA oversight via Joint Examination Teams (JETs): annual risk analyses, reporting obligations and on-site inspections. Selection used a two-step test on systemic relevance, substitutability and concentration risk. ([PwC Legal](https://legal.pwc.de/en/news/articles/esas-publish-first-list-of-critical-ict-third-party-providers-under-dora))
- **UK parallel.** In July 2026 UK authorities (BoE/PRA/FCA) designated AWS EMEA, Google Cloud EMEA and Microsoft Ireland as **Critical Third Parties** under the UK CTP regime — explicitly on systemic grounds. ([Global Banking & Finance](https://www.globalbankingandfinance.com/the-hidden-concentration-risk-in-banking-s-dependence-on-microsoft-amazon-and-google/)) So the same outage sits inside two parallel oversight regimes at once.

### In-base comps
Thin. The news DB (grep fallback — semsearch down, OpenRouter 402) has no prior DORA / cloud-concentration / hyperscaler-outage items; closest adjacencies are generic cloud-partnership notes (e.g. Instapay–Alibaba Cloud hardening its e-wallet stack, 2026-01; BoE £180m digital-transformation contracts, 2026-01), which are migration/spend stories, not resilience/oversight stories. Treat this item as the first resilience-regulation data point in the base rather than one of a cluster.

### Risk flags
1. **Systemic concentration, by design.** Google Cloud is one of only 19 EU CTPPs; the Big Three run ~67% of cloud. A single power event hit Revolut, Lloyds and HSBC at once — the textbook correlated-failure scenario DORA was written for.
2. **Enforcement is unproven.** CTPP designation is <12 months old and this is its first real-world stress test. EBA/FCA "engagement" is information-gathering, not sanction; whether oversight translates into penalties, binding resilience requirements or exit-plan mandates is still untested — do not assume teeth yet.
3. **Single-region / single-provider dependency.** A localised "power event" in one London datacentre cascaded Europe-wide, exposing weak multi-region/multi-cloud failover at affected banks. The liability/root-cause split between Google and its bank customers is unresolved.
4. **Reputational & lock-in risk for Google.** Being singled out by regulators days after the outage is adverse for Google Cloud's financial-services push; conversely, CMA-flagged lock-in (egress fees, interoperability) means affected banks cannot easily diversify away — the concentration that caused the risk also sustains it.

_Sources: Reuters (via Global Banking & Finance, The Star, Yahoo Finance) 2026-10-21; FMA Austria / PwC Legal on the 2025-11-19 CTPP list; tech-insider.org cloud market-share Q2 2026; Global Banking & Finance on UK CTP designation & BoE FPC July 2026 FSR. WebSearch inline; semsearch unavailable (OpenRouter 402, grep fallback used)._
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
