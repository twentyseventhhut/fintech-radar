---
title: "Belvo and dLocal bring direct debit payments to Mexican businesses"
date: 2026-10-26
retrieved: 2026-10-26
tags:
  - company/belvo
  - company/dlocal
  - industry/payments
  - region/latam
  - type/partnership
sources:
  - https://www.dlocal.com
  - https://www.dlocal.com/press-releases/recurring-payments-with-less-friction-and-operational-burden-the-belvodlocal-partnership
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: se23f9914
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Belvo and dLocal bring direct debit payments to Mexican businesses

> [!info] 2026-10-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇲🇽 Belvo and dLocal bring direct debit payments to more Mexican businesses. The partnership aims to help businesses with recurring payments, subscriptions and memberships collect payments more reliably, reducing failed transactions and operational friction. The companies are expanding bank debit as a payment option for recurring collections in Mexico

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.dlocal.com>
- <https://www.dlocal.com/press-releases/recurring-payments-with-less-friction-and-operational-burden-the-belvodlocal-partnership>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** On 2026-10-22 Belvo (open-finance infrastructure) and dLocal (cross-border payments for emerging markets) announced a Mexico partnership that embeds Belvo's bank **direct debit** ("domiciliación bancaria") into dLocal's payment stack, giving dLocal's merchants an additional rail to automate recurring collections directly from customers' Mexican bank accounts. Target verticals: subscriptions, memberships, insurance, utilities, lending and automotive. Goal: diversify collection routes beyond cards and cut failed renewals (expired cards, single-method dependence) and operational burden. Source: [dLocal press release](https://www.dlocal.com/press-releases/recurring-payments-with-less-friction-and-operational-burden-the-belvodlocal-partnership), [latamfintech](https://www.latamfintech.co/articles/belvo-y-dlocal-se-alian-en-mexico-para-llevar-la-domiciliacion-bancaria-a-mas-empresas-y-facilitar-los-pagos-recurrentes).

**[1] How Mexican direct debit works here.** Belvo built a Mexico direct-debit product that lets a customer connect their bank account once and authorize recurring/variable charges without leaving the merchant app; Belvo abstracts per-bank integrations into one API. This is distinct from card rails and from SPEI push transfers — it is a *pull* authorization on the bank account (domiciliación), closer to A2A account-to-account collection. dLocal already supports SPEI, OXXO and wallets in Mexico; direct debit adds a recurring-pull rail dLocal did not natively own. ([Belvo Direct Debit](https://belvo.com/products/direct-debit/), [Belvo developer docs](https://developers.belvo.com/products/payments_mexico/direct-debit-overview)).

**[2] Who the players are.** Belvo is the leading LatAm open-finance/aggregation API, with a deep Mexico franchise — see [[Belvo and Banco Plata launch open finance credit in Mexico]], [[Belvo launches AI-powered Intelligent Ecosystem in Mexico]], [[Belvo and Uala partner on employment-based credit access in Mexico]]. dLocal is a Nasdaq-listed (DLO) emerging-markets payments processor that handled ~US$41B TPV in 2025 (+60% YoY), revenue past US$1B; it monetizes local payment methods for global merchants. This is a supply-side plug-in for dLocal (adds a method) and a distribution deal for Belvo (reaches dLocal's merchant base).

**[3] Prior art / pattern.** dLocal repeatedly adds local recurring rails: [[dLocal introduces recurring Pix payments]] (Brazil), [[dLocal enables instant transfers via Colombia's Bre-B]], and [[Kueski partners with dLocal to expand BNPL across Mexico]]. Belvo has been productizing direct debit with other partners (e.g. Bitso integrating Belvo domiciliación for bank-account funding of a wallet; a Mexican gym chain using Belvo). So neither the technology nor the strategy is new — the novelty is the Belvo↔dLocal channel pairing in Mexico specifically.

**[4] Why it matters / open angle.** Recurring-revenue businesses in Mexico lean heavily on cards (39% debit / 33% credit of volume) with high involuntary churn from expired/declined cards; a bank-account direct-debit rail promises higher success rates and lower cost. The deal is a distribution multiplier — Belvo gets volume via dLocal's merchant portfolio instead of one-by-one sales. No pricing, exclusivity, volume targets or live-merchant count disclosed, so commercial impact is unquantified as of the announcement.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. *Is this a real, dated announcement?* Yes — 2026-10-22, dLocal press release + latamfintech/fintechexpert coverage. Confirmed.
2. *Is it a new partnership or a re-announcement?* New Belvo↔dLocal pairing; no prior note covers it. Fresh.
3. *Is direct debit new to either party?* No — Belvo already sells a Mexico direct-debit product (Bitso, gym chain); dLocal already added recurring rails elsewhere (Pix, Bre-B). The *channel* is the only novelty.
4. *What exactly is the integration — API, resale, white-label?* Not disclosed; framed as dLocal offering Belvo direct debit to its merchants. Open.
5. *Any economics — pricing, rev-share, volume targets, exclusivity?* None disclosed. Open.
6. *How many merchants are live or in pipeline?* Not stated; only target verticals named. Open.
7. *Is "direct debit" here domiciliación (pull) vs SPEI (push) vs CoDi?* It is domiciliación bancaria — an authorized recurring pull on the bank account, not a SPEI push. Confirmed via Belvo docs.
8. *Does it rely on Mexico's open-finance regulation?* Belvo operates in Mexico's Fintech Law / open-finance context, but direct debit mandates predate formal open banking; regulatory dependency unclear. Open.
9. *Who bears mandate/authorization and dispute risk?* Unspecified; direct-debit chargeback/refund rules in Mexico differ from cards. Open.
10. *Is this exclusive, or can dLocal use other aggregators?* No exclusivity stated. Open.
11. *Competitors?* Other MX open-finance/A2A players (Prometeo, Minu-adjacent, bank-native domiciliación, Clip/Kushki rails); card networks for recurring. Belvo is market leader but not sole provider.
12. *Material to dLocal financials?* Mexico is one of dLocal's larger markets but one method among six; no volume guidance, so immaterial-to-TBD near term.
13. *Could it cannibalize card volume dLocal already monetizes?* dLocal's own data says added local methods create net-new volume rather than cannibalize — mildly supportive.
14. *Any customer/success-rate data?* None quantified in the announcement. Open.
15. *Source quality?* Primary (dLocal PR) plus regional trade press; no independent financial verification. Adequate but promotional.

Importance: 3/5 — Credible, dated, strategically logical distribution deal that strengthens A2A/recurring rails in a key LatAm market, but it is incremental (direct debit already exists for both firms), carries no disclosed economics or volumes, and the near-term financial impact is unquantified.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Deal in one line.** Belvo (open-finance infra, MX/BR) and dLocal (NASDAQ: DLO, cross-border payments orchestrator for emerging markets) are expanding **bank direct debit** as a recurring-collections rail for Mexican businesses — subscriptions, memberships, utilities, lending, insurance. The pitch is reliability: fewer failed charges and less operational friction vs. card-on-file recurring. No deal value, no volume commitment, no exclusivity disclosed (per the dLocal press release and the Connecting-the-Dots mention). Treat as a product/distribution tie-up, not a material financial event.

### Sector context — why direct debit in Mexico is a real gap

- **Card recurring is lossy in MX.** Mexican card recurring collections suffer high involuntary churn (expired/declined cards, issuer decline rates well above developed markets). Bank direct debit ("domiciliación") authorizes pulls straight from the bank account, cutting the decline/expiry failure modes. That is the concrete value prop here.
- **The legacy rail is weak.** Mexico's direct-debit clearing house **CECOBAN** is bank-only, dated, and — unlike US ACH or UK Bacs — has **no standardized consumer dispute/mandate framework**; disputes fall to individual banks' discretion. So "direct debit in MX" is less a plug-into-rails play and more an orchestration/connectivity problem — exactly Belvo's open-finance lane. ([Mexico Business News](https://mexicobusiness.news/finance/news/trend-shaping-future-payments-mexico-2026))
- **A2A/instant rails exist but don't cover recurring.** SPEI (~5.4B txns in 2024, ~6x GDP in value) is the instant backbone; CoDi (~21M validated accounts by 2025) and DiMo ride on SPEI but adoption is thin and **CoDi does not support recurring pull payments**. That leaves a structural hole for subscription/membership billing that bank debit + open-finance mandate management targets. ([FacePhi observatory](https://facephi.com/observatory/en/financial-inclusion-mexico-fintech-digital-payments/), [Mexico Business News](https://mexicobusiness.news/finance/news/trend-shaping-future-payments-mexico-2026))
- **Role split.** Belvo supplies the open-finance connectivity/mandate layer; dLocal supplies merchant distribution, settlement and its cross-border/global-merchant book. Complementary, low overlap.

### In-base comps (news vault)

- [[News/2026-05/Belvo and Banco Plata launch open finance credit in Mexico]] — Belvo's open-finance-for-credit play in MX; same connectivity primitive, different use case.
- [[News/2026-02/Belvo launches AI-powered Intelligent Ecosystem in Mexico]] — Belvo's MX product push incl. collections/recovery; direct-debit recurring extends this collections angle.
- [[News/2025-10/dLocal enables instant transfers via Colombia's Bre-B]] and [[News/2025-09/dLocal integrates Capitec Pay for A2A payments in South Africa]] — dLocal's pattern of bolting local A2A/instant rails onto its network market-by-market; the Belvo MX debit tie-up is the same playbook in Mexico.
- [[News/2025-10/Kueski and dLocal collaborate on BNPL services in Mexico]] — dLocal already building MX merchant distribution via local-method partnerships.

Pattern read: both companies are serially partnering to stitch local MX payment methods; this is incremental method-coverage expansion, not a new strategic lane for either.

### dLocal — IR-grounded financials (skeptical read)

ir_latest.json tops out at **1Q26 (6-K filed 2026-05-14)** and irdb is even staler (chunks to 4Q24, 2025-02-27) — both **lag the latest print**. Cross-checking via web: dLocal has since reported **2Q26** (reported 2026-08; 6-K index 000184683226000031 on EDGAR).

Reported **2Q26** figures (web, cross-checked; verify against the EDGAR 6-K before quoting externally):
- **TPV $17.7B, +92% YoY** — 7th straight quarter of 50%+ TPV growth. ([Market Chameleon](https://marketchameleon.com/articles/b/2026/8/14/dlocal-q2-2026-results-tpv-growth-cash-generation), [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/20/dlocal-dlo-q2-2026-earnings-call-transcript/))
- **Revenue $399.7M, +56% YoY**; **Gross profit ~$127M, +29% YoY**; net income ~$55M, +28% YoY; diluted EPS $0.18 (missed ~$0.19 consensus). ([Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-dlocal-tops-revenue-in-q2-2026-but-eps-misses-93CH-4859491))
- **Net take rate (GP/TPV) 0.72%, down from 1.07% YoY and 0.84% QoQ** — the key tension: volume is compounding fast but margin-on-volume is compressing hard (mix shift to large merchants / lower-margin geographies). Gross profit growing far slower than TPV is the structural story.
- **FY26 guidance raised**: TPV +60–70% YoY, gross profit +25–30% YoY; operating profit +27.5–32.5% YoY.

The Belvo MX debit expansion is **immaterial** to these numbers — it's a method add in one country, not a volume driver you'd see in the TPV line. Don't attribute financial upside to it.

### Belvo — context (private, no IR)

- Raised **$15M in Apr 2025** (Quona Capital new; Kaszek, Kibo, Future Positive, Citi Ventures, Y Combinator existing); ~**$74M total raised** over 7 rounds. Operates MX + BR, 150+ clients (BBVA, Banamex, Bradesco, Santander, Mercado Libre, Creditas), ~**2M A2A txns/month, ~$500M annualized TPV**. ([Finextra](https://www.finextra.com/newsarticle/45848/latin-american-open-finance-platform-belvo-raises-15m), [Belvo blog](https://belvo.com/blog/belvo-secures-15-million-in-new-round-of-funding-open-finance-latin-america/)) These are small, early-stage volumes — this is a growth bet, not a scaled rail.

### Risk flags

1. **Rail/dispute risk.** Mexican direct debit (CECOBAN) has no standardized mandate or chargeback/dispute framework; mandate authorization and disputed-pull handling are left to banks. Execution and consumer-protection/regulatory risk is non-trivial.
2. **Take-rate compression at dLocal.** Net take rate fell to 0.72% (from 1.07% YoY). Low-margin local methods like bank debit can further dilute take rate even as they add TPV — the Belvo tie-up leans into the exact mix trend pressuring dLocal's gross-profit-to-volume ratio.
3. **Competitive overlap / channel conflict.** Belvo already runs an analogous MX recurring/direct-debit partnership with **J.P. Morgan Payments** (announced ~Jan 2025). Non-exclusive, partially overlapping distribution raises the question of how much incremental volume the dLocal deal actually captures. ([The Paypers](https://thepaypers.com/payments/news/belvo-and-jp-morgan-payments-support-recurring-payments-in-mexico))
4. **Adoption uncertainty for A2A recurring in MX.** CoDi/DiMo adoption has been slow; bank-debit-for-subscriptions is unproven at scale in Mexico. Demand-side uptake, not tech, is the gating factor.
5. **Materiality / disclosure gap.** No deal value, volume commitment, revenue-share, or exclusivity disclosed. Early product announcement — easy to over-read.
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
**Earnings-grounding context (dLocal, Nasdaq: DLO).** This story is a product/partnership launch (Belvo + dLocal direct debit for recurring collections in Mexico), not an earnings print — no results in the news. Below is a grounding read of dLocal's most recent *reported* quarter (Q2 2026, reported Aug 14, 2026) for context; Mexico is one of dLocal's key markets, so the direct-debit expansion feeds the same Mexican flow discussed in the print. Q3 2026 is not yet reported (expected ~Nov 11, 2026).

**Verdict (headline read, Q2 2026).** MIXED (revenue beat, EPS slight miss) · Revenue $399.7M (+56% YoY; vs expected ~$365M → beat ~+9.6%, ~+$35M) · Diluted EPS $0.18 (+29% YoY; vs expected $0.19 → miss ~$0.01) · driven by record TPV +92% YoY; FY2026 guidance *raised* on TPV and gross profit.

**Key figures (with growth).**
- TPV: $17.7B, +92% YoY / +26% QoQ (80% YoY FX-neutral) — 7th straight quarter of 50%+ growth, with the last three at/above 70%.
- Revenue: $399.7M, +56% YoY / +19% QoQ (50% YoY FX-neutral).
- Gross profit: $127.2M (record), +29% YoY / +7% QoQ (23% FX-neutral). Gross margin 32%, -700 bps YoY; gross-profit/TPV take rate 0.72%, -35 bps YoY / -12 bps QoQ — i.e. revenue and TPV out-growing gross profit (take-rate compression).
- Operating profit: $64.2M, +15% YoY / +22% QoQ; op-profit/gross-profit ratio 50% (+6 p.p. QoQ, -600 bps YoY).
- Net income: $54.8M, +28% YoY / +31% QoQ.
- Diluted EPS: $0.18, +29% YoY.
- Adjusted free cash flow: $68.5M, +41% YoY. Corporate cash $369.1M at Jun 30 (down QoQ on dividends + $86.1M buyback). New $150M senior unsecured facility signed Aug 12, 2026.
- NRR / adjusted EBITDA: not separately disclosed in the release ("no data").

**By segment / driver.** Brazil record gross profit ~$40M (ride-hailing, travel, e-commerce); Argentina record ~$20M (e-commerce, ride-hailing, on-demand delivery, lower advancement costs). **Mexico (key market):** underlying growth remained ~64% YoY but was flagged as a *margin headwind* — "large Tier 0 merchants hitting higher volume pricing tier along with cost pressure." Africa/Asia margin pressure from lower-FX-spread markets (Mozambique, Vietnam) and a one-off Nigeria cost increase. Net: volume and revenue screaming, but mix (large-merchant tiering + lower-spread geographies) is the gross-margin drag.

**vs expectations / prior period.** Revenue beat public consensus ~$365M by ~+9.6% (+~$35M; Wall St Engine est. $369M, Investing.com est. $364.65M, as of the Aug 14, 2026 print). EPS missed the ~$0.19 consensus by ~$0.01 (Investing.com: "tops revenue but EPS misses"). Operating profit $64.2M landed essentially in line (est. ~$64.3M). YoY momentum is clearly *accelerating* — TPV +92% is the fastest YoY rate in four years and the prior quarter (Q2 2025) was TPV $9.2B / >50% YoY, so volume roughly doubled year-on-year. No past dLocal report currently exists as an enriched note in the base to wikilink.

**Guidance / forward.** FY2026 guidance *raised*: TPV growth to 60–70% YoY and gross-profit growth to 25–30% YoY; operating-profit growth *maintained* at 27.5–32.5% YoY. CEO Pedro Arnt flagged that "the pace and scale of this growth will naturally create more demanding comparisons as we move through the second half of the year and into 2027" — confident tone, but an explicit sandbag/deceleration warning on H2 comps. The maintained (not raised) operating-profit guide alongside a raised TPV/gross-profit guide signals management expects opex/investment to absorb the upside — consistent with the margin story.

**Thesis-flags.**
1. Take-rate compression (gross margin -700 bps YoY, GP/TPV 0.72% -35 bps) → fact: TPV +92% but gross profit only +29% → why: large Tier-0 merchant volume prices at lower tiers (Mexico explicitly cited) + lower-FX-spread geographies → why it matters: dLocal monetizes spread/take-rate, so hyper-growth in low-margin volume dilutes unit economics → second-order: the Belvo/dLocal Mexican direct-debit push adds recurring-payment rails that could lift reliability/retention but also sits in exactly the Mexico market flagged as a pricing-tier headwind.
2. Mexico is dual-signal: ~64% underlying growth (strong demand, supports the partnership thesis) yet named as a margin drag — watch whether local-payment-method expansion (bank debit) improves economics or just adds low-take volume.
3. Guidance asymmetry: TPV/gross-profit raised but operating-profit only maintained → management is choosing growth/investment over near-term margin; EPS miss (vs beat on revenue) is the first visible crack if operating leverage doesn't arrive in H2 as promised.
4. Balance-sheet action: $86.1M buyback + new $150M facility → capital-return plus leverage optionality, modestly share-count supportive for EPS.

Sources: dLocal Q2 2026 6-K/EX-99.1 earnings release <https://www.sec.gov/Archives/edgar/data/0001846832/000184683226000031/ex_991-dlocalxearningsxres.htm> · Investing.com (revenue beat / EPS miss + consensus) <https://www.investing.com/news/transcripts/earnings-call-transcript-dlocal-tops-revenue-in-q2-2026-but-eps-misses-93CH-4859491> · Investing.com Q2 slides / guidance <https://www.investing.com/news/company-news/dlocal-q2-2026-slides-tpv-surges-92-guidance-raised-on-broad-growth-93CH-4859512> · MarketBeat Q3 2026 date + consensus <https://www.marketbeat.com/earnings/reports/2026-11-11-dlocal-limited-class-a-common-shares-stock/> · IR ir_latest.json[dlocal] · NRR / adj. EBITDA: no data.
<!-- /enrichment:earnings_review -->
