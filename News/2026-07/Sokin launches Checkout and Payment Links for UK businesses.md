---
title: "Sokin launches Checkout and Payment Links for UK businesses"
date: 2026-07-17
retrieved: 2026-07-17
tags:
  - company/sokin
  - industry/payments
  - industry/b2b-payments
  - region/uk
  - type/product
sources:
  - https://www.connectingthedotsinfin.tech/r/c158914a
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s95071604
month: 2026-07
enriched: true
importance: 2
freshness: stale
duplicate_of: [[Sokin and Adyen partner on US payments and treasury]]
---

# Sokin launches Checkout and Payment Links for UK businesses

> [!info] 2026-07-17 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 Sokin is launching Sokin Checkout and Payment Links for UK businesses. The two products give businesses and finance teams a single place to collect customer payments by card and other methods, with funds settling directly into the company’s Sokin account with no separate integration to build or maintain.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/c158914a>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Sokin launches Checkout and Payment Links for UK businesses
_Analytical notes (not a post). Importance: 2/5._

## [0] What exactly happened (de-PR'd)
- **16 Jul 2026**: Sokin turned on **Sokin Checkout** (hosted/embedded card page) and **Payment Links** (share-by-link/QR request + auto reminders + live status) for **UK businesses**. Funds settle directly into the merchant's existing Sokin account, marketed as "no separate integration to build or maintain."
- **De-PR'd:** this is a **region go-live**, not a new product. The exact same "checkout and payment links functionality" was already announced for **US businesses via the Adyen partnership on 29 Apr 2026** (see [[Sokin and Adyen partner on US payments and treasury]]), which explicitly listed "accept payments through Sokin's checkout and payment links functionality." The Adyen deal named the UK as a slated market. So July = the UK leg of an already-shipped acceptance layer.
- **The acceptance rails are not Sokin's own** — they run on **Adyen** (analysis, consistent with the April deal). Sokin is the orchestration + settlement-into-account + FX/treasury wrapper, not the acquirer.
- **UK-launch currencies reportedly only USD/GBP/EUR/CAD** — far narrower than Sokin's "70+ currencies" treasury pitch (analysis; from launch coverage). Acceptance breadth ≠ FX story breadth.
- **Not disclosed:** pricing/fees, launch merchants, volumes. "No integration" is marketing gloss — hosted page/links are low-code by design, but embedded checkout still needs storefront work.
- **Why framed this way:** Sokin's core is treasury/AP + FX; receivables/acquiring was the gap. Bolting acceptance onto the same dashboard lets money land where it's already held → less reconciliation + FX conversion friction. The UK "launch" headline recycles the Adyen capability to keep a cadence of milestones.

## [1] Competitors / peers
- Hosted checkout + payment links are **table-stakes**: Stripe, Checkout.com, Adyen (Sokin's own back-end), SumUp, Square, **Revolut Business**, Tide; GoCardless for collections. Cash App shipped consumer payment links Feb 2026 ([[Cash App adds payment links to get paid]]); Revolut Business moved into recurring billing Jan 2026 ([[Revolut Business launches recurring billing tool]]).
- **Closest analogue = Revolut Business**, which already fuses multi-currency accounts + FX + acquiring — exactly Sokin's pitch. Sokin's only real differentiator is **treasury/FX depth + stablecoin rails** on one dashboard for cross-border-heavy SMB/mid-market, not any novel acceptance capability.
- **Position: catching up / parity**, not ahead. Second-order: since acceptance is Adyen-powered, Sokin competes on *bundling and FX economics*, not on the payment rail itself — so margin on the acquiring leg is shared with Adyen, and the durable moat has to come from the treasury/account relationship.

## [2] Company history / fit
- London fintech (founded 2019, CEO **Vroon Modgill**). Trajectory: **$50M Series B at ~$300M valuation, Dec 2025** ([[Sokin raises $50M Series B for global payments]]); **$100M Oxford Finance debt facility, Jan 2026** ([[Sokin secures $100m debt facility from Oxford Finance]]); **stablecoin launch, Mar 2026** ([[Sokin launches stablecoin capabilities for hybrid finance platform]]); **Adyen acceptance partnership, Apr 2026**.
- **Regulatory structure (key):** Sokin is largely a **distributor of Modulr FS (FCA EMI) in the UK**, not the licence-holder; US/Canada/India via Plata Capital entities. Merchant funds/safeguarding sit with Modulr. So it's an **orchestration layer** stacked on third-party licences + Adyen rails.
- **Why it acts this way:** commodity cross-border take-rate → needs a stickier, multi-product account relationship to defend a software-like multiple → hence the march into acquiring, stablecoins, treasury. The UK Checkout go-live is one more brick in "one dashboard for fiat + stablecoin + acceptance + treasury."

## [3] Novelty / value-add / traction
- **Novelty: low.** Not new capability, not new to Sokin (US had it in April), not new to the market. The only genuinely new thing is **UK availability + GBP like-for-like settlement**.
- **Traction: unproven.** No merchants, volumes, or pricing disclosed. Self-reported ~$4.5bn annual volume / 100% YoY growth / profitability are **PR-sourced, unaudited** (hypothesis-grade).
- **Who captures the margin:** on the acquiring leg, **Adyen takes acceptance economics + Modulr the EMI economics**; Sokin captures FX spread + account/subscription. Value-add is real *only if* the bundle lowers a cross-border SMB's total cost/reconciliation vs running Stripe + a separate FX account — plausible but not evidenced here.

## [4] What's next / market sentiment
- Expect further regional go-lives of the Adyen acceptance layer (Canada, Europe, UAE, Singapore, Australia were slated) plus the stablecoin merchant-acceptance phase. Watch for the first **disclosed pricing** and **named merchants** — that's when this becomes a real product story rather than a milestone drip.
- **Marketing signal (why it matters):** Sokin is **sports-sponsorship-heavy** — Manchester United ([[Manchester United names Sokin official B2B payments partner]]), British & Irish Lions, Professional Triathletes Organisation / T100 ([[Professional Triathletes Organisation names Sokin official payments partner]]), plus European clubs; Rio Ferdinand as an angle. Counterintuitive second-order: a challenger spending heavily on brand while running on other firms' rails (Adyen/Modulr) is buying **CFO trust** to win mandates it couldn't win on product novelty alone — durable only if the bundle economics actually hold.

## Sources
See challenge file and note frontmatter. Prior corpus: [[Sokin and Adyen partner on US payments and treasury]], [[Sokin launches stablecoin capabilities for hybrid finance platform]], [[Sokin raises $50M Series B for global payments]], [[Sokin secures $100m debt facility from Oxford Finance]], [[Manchester United names Sokin official B2B payments partner]], [[Professional Triathletes Organisation names Sokin official payments partner]], [[Revolut Business launches recurring billing tool]], [[Cash App adds payment links to get paid]].
External: Financial IT / Finextra (16 Jul 2026 UK launch); PR Newswire (Adyen 29 Apr 2026; stablecoin 17 Mar 2026); BusinessWire (Series B, Oxford Finance debt); Marketing Week (sports-sponsorship "credibility" framing).
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team (Sokin UK Checkout + Payment Links)

1. **Is this actually new, or the UK leg of the April Adyen launch?** — The latter. The 29 Apr 2026 Adyen deal already shipped "checkout and payment links functionality" for US businesses and named the UK as slated. This is a **region go-live re-frame**, not a new capability. (near-duplicate of [[Sokin and Adyen partner on US payments and treasury]])
2. **Whose acquiring rails?** — **Adyen's**, not Sokin's. Sokin is orchestration + settlement-into-account + FX. Margin on acceptance is shared.
3. **Who holds the UK regulatory permission?** — **Modulr FS (FCA EMI)**; Sokin is a distributor, not the licence-holder. Merchant safeguarding sits with Modulr.
4. **What are the fees?** — Open. No pricing disclosed. Can't verify cost-competitiveness vs Stripe/SumUp/Revolut Business.
5. **Live or soft-launched?** — Framed as live for UK businesses (16 Jul 2026), but no launch merchants/volumes → real availability/scale open.
6. **Genuinely differentiated vs Revolut Business?** — No. Revolut Business already bundles multi-currency accounts + FX + acquiring. Sokin's edge is treasury/stablecoin depth, not acceptance.
7. **Currency gap:** UK Checkout reportedly supports only USD/GBP/EUR/CAD vs the "70+ currencies" treasury pitch — acceptance far narrower than the FX story.
8. **Are the growth numbers ($4.5bn volume, 100% YoY, profitable) verified?** — No, PR-sourced/unaudited.
9. **"No separate integration" — true no-code?** — Overstated. Hosted page/links are low-code; embedded checkout still needs storefront work.
10. **Concentration risk:** heavy dependence on Adyen (rails) + Modulr (UK EMI) + Plata entities abroad — Sokin is an orchestration layer; a dependency and margin-share risk.
11. **Where's the durable margin?** — On the account/FX relationship, not the commodity acquiring leg. Bundle must lower total cost/reconciliation for cross-border SMBs to justify the multiple.
12. **Why the sports-sponsorship spend (Man Utd, Lions, PTO/T100)?** — Buying CFO trust for mandates it can't win on product novelty; ROI unquantified, acknowledged as a "big outlay."
13. **What would move this from milestone to story?** — First disclosed pricing + named merchants + independent volume.

**Importance: 2/5 — rationale:** Commodity capability (hosted checkout + payment links), running on Adyen's rails under Modulr's licence, that Sokin already launched in the US in April 2026. The only new element is UK availability + GBP settlement. No disclosed pricing, merchants, or volumes. Real but minor incremental region go-live; not a novel product and not evidenced traction.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** UK online-checkout / payment-links for SMBs — a commoditized, feature-level layer within a growing acquiring market. UK payment-gateway market ~$3.02bn in 2026 → ~$5.88bn by 2031 at ~14.3% CAGR, hosted checkout pages ~67.5% share (per Mordor/secondary gateway-market citations, via generatesepa.com, 2026) `[UNSOURCED — single secondary source, treat as directional]`. Structure: highly fragmented at the SMB acquiring/checkout end and rapidly commoditizing — payment links + hosted checkout are now a default, table-stakes feature across Stripe, Square, SumUp, Revolut Business and GoCardless (businessexpert.co.uk / smallbusiness.co.uk, 2026). Barriers to the *link/checkout feature itself* are low (no card scheme licence needed when riding a processor); real barriers sit upstream in acquiring licences, scheme relationships and settlement/FX rails. Why now: Sokin already shipped Checkout in the US in April 2026 on Adyen's platform (`[[Sokin and Adyen partner on US payments and treasury]]`); this is a UK rollout of the same stack, bundling acceptance into its existing multi-currency/treasury account to lift take-rate and stickiness — same play as `[[Ecommpay launches self-serve payments platform for UK small businesses]]` one day earlier (2026-07-16).

**Competitive landscape.** Sector KPIs: TPV/GPV, blended take rate, attach rate (share of account-holders also using acceptance), settlement currencies. Key players & basis of competition: incumbents Stripe/Adyen (product depth, developer distribution), SumUp/Square/Dojo/Viva ("tap pack" — price, hardware, self-serve onboarding), Revolut Business (bundled account + acquiring, live in 19 countries, volumes ~3x in 2025 per revolut.com) and GoCardless (bank-to-bank). Competition here is on price and distribution, not novelty — the feature is undifferentiated. Recent moves: Ecommpay UK SMB self-serve (2026-07-16); Sage + GoCardless Pay-by-Bank for SMBs (2026-07); Revolut Business merchant expansion (2025). Sokin's position: **niche / catching up** — differentiator is not the checkout (which is generic) but funnelling acceptance into its cross-border multi-currency + treasury account (USD/GBP/EUR/CAD like-for-like settlement at launch; Visa/Mastercard/Amex/Apple/Google Pay/Alipay/WeChat). Moat `(analysis)`: modest switching costs from being the customer's treasury account-of-record + its 26-currency hold / 70-currency send rails; not the payments acceptance per se, where it depends on a partner processor.

**Comps & multiples.** Sokin: last round $300m post-money (Series B, Dec 2025; €42.9m/~$50m raised, led by Prysm Capital), 100% YoY revenue growth / ~8x since 2022; also $100m Oxford Finance debt facility (`[[Sokin raises $50M Series B for global payments]]`, `[[Sokin secures $100m debt facility from Oxford Finance]]`). Revenue undisclosed → EV/Revenue = `$300m / no data = no data`; all valuation multiples "no data" (private, no denominator). Internal comps (private-round valuations, not market caps): `[[Sokin raises $50M Series B for global payments]]` ($300m post-money); `[[Sokin launches stablecoin capabilities for hybrid finance platform]]`; `[[Sokin and Adyen partner on US payments and treasury]]`. Public acceptance peers (Adyen, Stripe) trade/are valued far above SMB-acquiring pure-plays — not comparable on scale/geo; distribution not computed → qualitative only. Flag: in-line for a growth-stage private paytech; nothing here re-rates the $300m mark — it's a product line-extension, not a metrics event.

**Risk flags.**
1. **Commoditization / no differentiation** — Checkout + Payment Links are table-stakes at Stripe/Square/SumUp/Revolut/GoCardless; Sokin competes on price and bundling, not product. Second-order: margin compression and reliance on cross-selling the account to justify acquiring, since the acceptance layer alone won't win merchants.
2. **Rails dependence / disintermediation** — acceptance runs on a partner processor (Adyen for the US launch); Sokin captures the treasury/FX layer but the interchange+scheme economics sit with the acquirer. Second-order: thin, partner-dependent take rate on the payments leg; margin can be squeezed by the processor.
3. **"Announced vs adopted" + silent economics** — the PR discloses no pricing, no target merchant count and no TPV; it's a UK availability announcement, not evidence of traction. Second-order: unclear whether it moves the P&L vs merely broadening the account's utility.

**What this changes (idea-lens).** `(analysis)` Not a re-rating and not a new category — it's Sokin extending a bundled cross-border-account + acceptance stack down-market in the UK, the same convergence Revolut Business and Ecommpay are riding: acquiring as a feature attached to a business account, not a standalone product. Falsifiable thesis: if Sokin's edge is real, watch for disclosed TPV/attach-rate (share of account-holders using Checkout) or a follow-on round marking above $300m; absent that within ~2–3 quarters, this reads as feature-parity catch-up. What breaks the thesis: a large incumbent (Stripe/Revolut) further bundling multi-currency treasury into SMB acceptance, erasing Sokin's cross-border differentiator.

Sources: https://financialit.net/news/payments/sokin-now-lets-uk-businesses-take-card-payments-online · https://www.finextra.com/pressarticle/110431/sokin-now-lets-businesses-take-card-payments-online · https://fintechmagazine.com/news/us-300m-valued-sokin-raises-us-50m-to-fuel-global-expansion · https://www.eu-startups.com/2025/12/british-fintech-firm-sokin-raises-e42-9-million-to-expand-global-payments-and-treasury-infrastructure/ · https://www.generatesepa.com/blog/payment-gateways-uk · https://www.businessexpert.co.uk/payment-processing/payment-links-and-qr-codes/ · https://www.revolut.com/business/accept-payments/payment-solutions-sme/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
