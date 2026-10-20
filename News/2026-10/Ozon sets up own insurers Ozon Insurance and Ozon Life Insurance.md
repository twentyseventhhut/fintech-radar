---
title: "Ozon sets up own insurers Ozon Insurance and Ozon Life Insurance"
date: 2026-10-19
retrieved: 2026-10-19
tags:
  - company/ozon
  - industry/insurtech
  - region/ru
  - type/product
sources:
  - https://www.retail.ru/news/marketpleys-ozon-uchredil-dve-strakhovye-kompanii-15-oktyabrya-2026-283360
status: published
n_mentions: 1
channels:
  - "News & Trends by Sber"
story_id: s6d7096a7
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Ozon sets up own insurers Ozon Insurance and Ozon Life Insurance

> [!info] 2026-10-19 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] Учредил две собственные страховые компании — «Озон Страхование» и «Озон Страхование жизни», чтобы самостоятельно разрабатывать страховые продукты для физлиц и бизнеса

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.retail.ru/news/marketpleys-ozon-uchredil-dve-strakhovye-kompanii-15-oktyabrya-2026-283360>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ozon sets up own insurers Ozon Insurance and Ozon Life Insurance
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **15 Oct 2026**, two new legal entities appeared in Russia's company register (EGRUL): **LLC "Insurance Company Ozon Insurance"** (Озон Страхование) and **LLC "Insurance Company Ozon Life Insurance"** (Озон Страхование жизни). Owner of both: **LLC "Ozon Capital"** (the fintech holding, same vehicle behind Ozon Asset Management and the DFA operator); director of both: **Denis Gavrilov**, head of the insurance line inside Ozon fintech. Stated aim: to design and launch insurance products in-house (for individuals and SMB, incl. life) instead of only re-selling partner policies.
- **De-PR'd reality — this is a shell registration, NOT a live insurer.** What exists is two LLCs in the registry. To actually underwrite — especially **life** — a Russian insurer must obtain a **Bank of Russia license** and hold **minimum charter capital of RUB 450m** (life). Neither a CBR license nor paid-in capital is confirmed; so "Ozon sets up own insurers" = **incorporation of license applicants**, months away from writing a single policy. "Announced/incorporated," not "launched." The marketplace itself says it **keeps the partner model** and continues with Renaissance Insurance, VSK, Sogaz and Ingosstrakh.
- **Why structured this way / what it reveals (the key red-team finding):** the timing is not incidental. Days earlier, on **13 Oct 2026**, Ozon and **Ingosstrakh ended** the only program that insured sellers' goods in warehouses against **mass damage / drone (UAV) attacks** (policies dead after 23:59 MSK 12 Oct), citing that "conditions for covering certain risks have significantly changed" — i.e. partner carriers refused to keep underwriting war-adjacent risk, and Ozon offered sellers **no alternative** beyond logistics workarounds (ship via PVZ, discounts for storing in Siberia/Kazakhstan). The new captive insurers are the **structural response to partner-carrier flight**: owning the licenses lets Ozon design and keep products that third-party insurers won't (or will only on bad terms), and capture the premium/float itself. That reframes the story from "marketplace adds insurance line" to **"marketplace internalizes underwriting because partners are pulling back from the riskiest covers."** (analysis)

## [1] Competitors / peers
Russian marketplace/ecosystem insurance splits sharply by **how deep each player goes down the regulatory stack**:
- **Sber — the full-stack benchmark:** owns two fully **CBR-licensed** carriers, **SberStrakhovanie** (P&C) and **SberStrakhovanie Zhizni** (life), 100% Sber-owned; pushing cyber-monitoring + cyber-insurance bundles in 2026. This is the end-state Ozon is now *starting* to copy — and Sber is years and licenses ahead.
- **Yandex — the agent model (deliberately shallow):** Yandex **considered buying a licensed insurer but chose to stay an agent**, earning commission; Yandex Go sells OSAGO/KASKO/apartment cover by subscription, Yandex Market insures purchased goods — all on **partners' licenses**. Yandex explicitly decided *not* to carry the balance sheet.
- **Wildberries / Ozon (to date):** both ran **subscription/embedded insurance as agents** before Yandex copied them. So on the *agent* game Ozon was early; owning carriers is the next rung.
- **Position:** On embedded-insurance distribution, Ozon is **at parity/ahead** (early mover on subscription cover). On *owning licensed capacity*, Ozon is **a late, pre-license entrant** — behind Sber's two licensed carriers, and only now crossing the line Yandex deliberately chose not to cross.
- **Why the landscape is this way / 2nd order:** the fork is **balance sheet vs. commission.** Agents (Yandex) keep it capital-light and avoid CBR capital/solvency rules; carriers (Sber, now Ozon) take underwriting risk for the premium + float + product control. Ozon moving to the carrier side is rational **only** because partner carriers are retreating from marketplace-specific risks (drone/warehouse) — otherwise the agent model is strictly cheaper. The decision is defensive supply-security, not an opportunistic margin grab. (analysis)

## [2] Company history / fit
Ozon fintech is the group's profit engine and has been systematically **collecting regulated licenses** one vertical at a time: cards/deposits → consumer credit → **own DFA issuance platform** (CBR register, Jun 2026, [[Ozon Bank registers digital financial assets platform with CBR]]) → **asset management** (Ozon Asset Management, 2025; CBR fund license Dec 2025) → **brokerage** (Ozon Investments, announced for autumn 2026, [[Ozon to launch brokerage arm Ozon Investments in autumn 2026]]) → **insurance carriers** now. Scale backdrop: ~39–42m active fintech clients (end-2025), deposits >RUB 438–505bn, fintech 9M-2025 pre-tax profit RUB 41.8bn (+156% YoY); Ozon Bank now a top-5 bank by brand awareness and #2 on customer satisfaction ([[Финтехно Ozon Bank tops banks on customer experience]]).
- **Why the company acts this way:** every step is the same logic — a commodity marketplace take-rate needs a **higher-multiple, recurring financial-services layer** bolted onto the captive 60m+ buyer / ~40m fintech-client funnel at near-zero CAC. Insurance adds (a) a new fee/float line and (b) **control of covers partners won't write**, protecting GMV (sellers who can't insure stock may leave the platform). The insurer build is both monetization *and* supply-chain defense. (analysis)

## [3] Novelty / value-add / traction
- **Novelty: low on the capability, real on the control.** Marketplace-embedded insurance already exists (Ozon/WB/Yandex all sell it). Owning a licensed carrier is not novel in Russia — **Sber already runs two.** What is genuinely new *for Ozon* is vertical integration into underwriting, triggered by partner withdrawal.
- **Traction: essentially zero.** Two registry entries, no CBR license, no paid-in capital confirmed, no product, no premiums written. This is the earliest possible stage. Prior Ozon insurance (agent) traction numbers are not disclosed.
- **Who captures the margin / what's real (2nd order):** as an *agent*, Ozon captured only commission; as a *carrier*, it can capture the **underwriting result + investment float** on premiums — a bigger, higher-multiple pool, **but only if it can actually price and absorb the risk partners just fled.** That is the catch: the covers Ozon most needs to own (drone/warehouse catastrophe) are precisely the ones professional reinsurers/carriers are repricing or exiting. Internalizing that risk concentrates a **tail, correlated, war-adjacent exposure** on Ozon's own balance sheet — value-add that could invert into a loss sink if a single large strike hits insured warehouses. The margin is real only if the book is diversified into mass retail/life/SMB lines fast enough to subsidize the catastrophe tail. (analysis / hypothesis)

## [4] What's next / market sentiment
Watch for the **concrete gates**, not the registry PR: (a) **CBR license grants** (P&C and, harder, life — RUB 450m capital); (b) paid-in charter capital; (c) first in-house product + whether it re-covers the dropped drone/warehouse risk sellers just lost; (d) whether partner carriers (Renaissance/VSK/Sogaz/Ingosstrakh) stay or exit as Ozon in-sources. Backdrop: Russian insurers are **repricing/withdrawing from UAV and warehouse-catastrophe risk** across marketplaces (specialist PVZ/warehouse insurance only emerged recently), so Ozon is entering underwriting exactly when the risk it most needs is hardest to price.
- **Why the market goes this way / counterintuitive 2nd order:** ecosystems keep marching toward the full super-app stack (bank + broker + funds + insurer), so an owned carrier is the predictable next tile. **But the counterintuitive effect:** taking insurance *in-house* at the moment specialist insurers are *fleeing* the key risk means Ozon is absorbing the exact exposure the market just priced as too hot — supply security bought at the cost of a concentrated catastrophe liability. If a licensed Ozon carrier later has to cover the drone/warehouse risk Ingosstrakh dropped, Ozon becomes the insurer of last resort for its own sellers — strategically sticky, but balance-sheet fragile. (analysis)

## Freshness / duplicate verdict
**FRESH.** Internal retrieval (grep over `company/ozon` + insurance terms) shows no prior corpus note on Ozon insurance carriers: the closest notes are a *different* license step (DFA, [[Ozon Bank registers digital financial assets platform with CBR]]), a *different* vertical (brokerage, [[Ozon to launch brokerage arm Ozon Investments in autumn 2026]]), and a CX survey ([[Финтехно Ozon Bank tops banks on customer experience]]). This is a distinct 15-Oct-2026 incorporation event, not a reprint or re-framing of any existing note. Fresh — though pre-license and low-traction (hence importance 3/5, lifted above 2 only by the strong, under-reported drone-insurance-withdrawal backstory that gives it strategic weight).

## Sources
- retail.ru — Ozon founded two insurance companies (15 Oct 2026): https://www.retail.ru/news/marketpleys-ozon-uchredil-dve-strakhovye-kompanii-15-oktyabrya-2026-283360/
- vc.ru — Ozon set up insurers amid end of partner drone-attack insurance program: https://vc.ru/marketplace/3197000-ozon-uchredil-strahovye-kompanii-dlya-podderzhki
- Interfax — Ozon plans own insurer: https://www.interfax.ru/business/1122624
- bosfera.ru — Ozon founded two new insurance companies (owner Ozon Capital, director Gavrilov): https://bosfera.ru/press-release/ozon-uchredil-dve-novye-strahovye-kompanii
- new-retail.ru — license + RUB 450m charter-capital requirement for life: https://new-retail.ru/novosti/retail/ozon_uchredil_sobstvennye_strakhovye_kompanii/
- The Bell — Ozon stops insuring sellers' goods against drone attacks (10/13 Oct 2026): https://thebell.io/ozon-prekrashchaet-strakhovat-tovary-sellerov-ot-atak-bespilotnikov
- The Insider — Ozon seller drone-damage cover ends 13 Oct: https://theins.ru/news/298142
- RG.ru — marketplace sellers no longer insured against UAVs: https://rg.ru/2026/10/13/ozonovye-dyry.html
- Kommersant — Yandex launched subscription insurance (agent model): https://www.kommersant.ru/doc/8710314 ; Yandex considered buying an insurer: https://www.kommersant.ru/doc/7198584
- Kommersant — insurers launch PVZ/warehouse cover for marketplaces: https://www.kommersant.ru/doc/7606706
- Bank of Russia — SberStrakhovanie (licensed carrier, Sber-owned): https://www.cbr.ru/finorg/foinfo/?ogrn=1147746683479
- insur-info.ru — SberStrakhovanie + SberStrakhovanie Zhizni: https://www.insur-info.ru/pressr/92347/
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Launched or just incorporated?** Incorporated only. Two LLCs appeared in EGRUL on 15 Oct 2026 — no CBR license, no confirmed paid-in capital, no product, no premiums. "Sets up" = registered license applicants, not a live insurer. (answered — central red flag)
2. **Can they legally underwrite today?** No. A Russian insurer needs a Bank of Russia license; for the LIFE entity, minimum charter capital RUB 450m. Neither confirmed. Months of regulatory runway remain. (answered)
3. **Why NOW — what's the real trigger?** Days earlier (effective 13 Oct), Ozon + Ingosstrakh ended the only program insuring sellers' goods against mass-damage/drone (UAV) attacks; Ozon offered no replacement. Owning carriers is the structural answer to partner-carrier retreat from war-adjacent risk. (answered — reframes the story)
4. **Is this genuinely new vs. Ozon's past?** New step (carrier ownership) but continuous with a serial license-collection pattern (DFA, asset mgmt, brokerage). Fresh, incremental. (answered)
5. **New vs. the market?** Not novel in Russia — Sber already owns two licensed carriers (P&C + life). Ozon is a late, pre-license entrant crossing a line Yandex deliberately chose not to cross. (answered)
6. **Does Ozon drop the partner model?** No — it explicitly keeps Renaissance, VSK, Sogaz, Ingosstrakh. So this is incremental in-sourcing, not a clean break. (answered)
7. **Who captures the margin — agent vs. carrier?** As agent: commission only. As carrier: underwriting result + investment float on premiums — a bigger, higher-multiple pool, but only if Ozon can price and absorb the risk. (answered)
8. **What's the catch in owning the risk?** The covers Ozon most needs (drone/warehouse catastrophe) are exactly what professional insurers are repricing/exiting. Internalizing concentrates a correlated, tail, war-adjacent exposure on Ozon's own balance sheet. (answered — key 2nd-order risk)
9. **Could Ozon become insurer-of-last-resort for its own sellers?** Plausibly. If a licensed Ozon carrier re-covers the dropped drone risk, Ozon absorbs the exact exposure the market just fled — strategically sticky, balance-sheet fragile. (answered — hypothesis)
10. **Two entities — why split life and non-life?** Russian law separates life from general insurance into distinct licensed legal entities (life carries the higher RUB 450m capital bar). Standard structuring, not two product launches. (answered)
11. **Is there any disclosed traction/numbers?** None. Prior agent-model insurance volumes undisclosed; new entities have zero book. All the hard financial traction lives in Ozon fintech earnings, not here. (answered)
12. **Who's silent about what?** Ozon is silent on license timing, charter capital, and whether/when it re-covers the dropped drone risk — the very questions that decide if this matters. (flagged)
13. **How does it compare to Yandex's choice?** Yandex weighed buying a licensed insurer and chose the agent model to stay capital-light; Ozon going carrier implies it values product/supply control over capital-lightness — a defensive, not opportunistic, calculus. (answered)
14. **What's the real central question?** Not "did Ozon add an insurance line" but "can a marketplace safely in-source the catastrophe risk its partner insurers just abandoned, and get CBR-licensed to do it?" (answered — reframes weight)
15. **What would prove this worked?** A CBR license grant (esp. life), paid-in RUB 450m capital, a first in-house product that re-covers the dropped seller risk, and partners staying rather than exiting — none present as of 19 Oct 2026. (open)

Importance: 3/5 — Rationale: Fresh, strategically coherent, and about Russia's #2 marketplace's fast-growing, profitable fintech arm, with a strong, under-reported backstory (it directly follows partner carriers fleeing drone/warehouse risk — the new entities are a supply-security move, not mere product expansion). That backstory, plus a credible balance-sheet-level second-order risk (Ozon internalizing a correlated catastrophe exposure), lifts it above a routine registry filing. Held to 3 (not higher) because it is pre-license, zero-traction incorporation with no CBR approval, no capital confirmed, no product, and the capability (an owned carrier) is already standard at Sber — low novelty, high execution/regulatory runway.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-20]] (2026-10-20).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Ozon is bolting licensed carriers onto an e-commerce/fintech ecosystem — the subvertical is embedded insurance / marketplace insurtech, not standalone insurtech. Russian market size: total written premiums reached ~RUB 4tn at end-2025, +6.9% YoY, with life at ~RUB 2.3tn (+10.8%, ~57% share) and non-life ~RUB 1.7tn (+2.1%); ACRA forecasts ~15% nominal growth in 2026, led by non-credit life (~16%) and motor (~15–16%) (per ACRA, via acra-ratings.ru, as of 2025-12-29). Structure: concentrated at the top (bank-affiliated carriers like Sberstrakhovanie dominate distribution via embedded/mortgage/savings channels) but with a long tail of monoline players; the value shifts to whoever owns the distribution funnel, not the balance sheet. Why now: (i) Ozon had run goods-insurance since 2024 on a partner/white-label model (third-party licenses) and is now internalizing underwriting economics by founding its own carriers (per Interfax/retail.ru, Oct 2026); (ii) wartime risk (drone strikes on warehouses) has made seller goods-insurance a live, repriced product across marketplaces in 2026 — a demand catalyst Ozon can now underwrite directly rather than cede the premium.

**Competitive landscape.** Sector KPIs: gross written premium (GWP), loss ratio / combined ratio, attach rate (policies per order/GMV), and — for embedded — the distribution take vs. underwriting margin split. Key players and their 2026 moves: Sberstrakhovanie (Sber) — ecosystem incumbent, already covers marketplace goods in storage; Wildberries — launched seller goods-insurance Feb 2025 (test rate 1.4%), added drone/sabotage cover Aug 2026, and raised rates to ~1.96–5.6% of item value by category (per Meduza, 2026-08-07); Yandex Market — has instead limited its own liability for drone attacks, pushing risk onto merchants (per Moscow Times, 2026-10-15); Alfa and other bancassurers compete on the retail-individual side. Ozon's position: catching up as a carrier (Sber/Alfa have scaled licensed books; Wildberries already runs the embedded-goods product live), but ahead on captive distribution — ~RUB 2.6bn-per-day-scale marketplace plus a fast-growing fintech arm give it a built-in funnel most monoline insurtechs lack. Moat is distribution/network-effect (own GMV + Ozon Bank/Ozon Capital customer base), not underwriting skill — which it has yet to demonstrate `(analysis)`.

**Comps & multiples.** No deal/valuation attaches to this news (two newly-founded legal entities, no round, no disclosed capital), so trading multiples are not computable — "no data" on any EV/Rev or P/E for the insurers themselves. Primary-evidence scale for the parent: per Ozon's own latest filing (Q3/9M 2025 earnings release, 2025-11-10, [cdn1.ozone.ru](https://cdn1.ozone.ru/s3/sigma-static-e93b3ad2-6f0b-4ad0-a53e-192ad6466704/Ozon_%D0%A4%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B5%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B%20%D0%B7%D0%B0%203%20%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B0%D0%BB%20%D0%B8%209%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2%202025%20%D0%B3%D0%BE%D0%B4%D0%B0.pdf)) Ozon reported Q3 2025 revenue ~RUB 258.9bn and a first net profit of ~RUB 2.9bn; fintech revenue trajectory from prior quarters was +164% YoY to RUB 46.2bn in Q2 2025 and +2.5x to RUB 39.0bn in Q1 2025, with FY2025 fintech guidance >+80% YoY (per Ozon IR releases via ir.ozon.com). That fintech cash flow is what funds captive insurers. Internal comps (grep, same ecosystem/geo): [[Ozon Bank registers digital financial assets platform with CBR]], [[Ozon to launch brokerage arm Ozon Investments in autumn 2026]], [[VTB takes large Ozon share stake as collateral]] — a clear 2026 pattern of Ozon stacking regulated financial licenses (bank, DFA, brokerage, now insurance). External embedded-insurance comps as directional, not valuation: [[Wrisk acquires Atto for embedded insurance offering]], [[Igloo expands embedded insurance in Philippines with 40-plus platforms]], [[Uala launches life and accident insurance with Allianz]] — note Uala/Igloo partner with a licensed carrier (asset-light), whereas Ozon is going balance-sheet-heavy by founding its own. Multiples distribution not computed (no comparable disclosed figures).

**Risk flags.**
1. Capital/underwriting execution — founding a carrier means holding insurance risk on balance sheet (reserves, solvency capital, CBR licensing/supervision); a marketplace has no underwriting track record, so early mispricing of the new drone/goods-damage peril (fat-tail, correlated wartime losses) could produce a combined ratio well over 100% — the opposite of the capital-light partner model it just left.
2. Correlated-catastrophe concentration — the demand driver (drone/sabotage cover for warehoused goods) is exactly the risk most prone to simultaneous large losses across one geography; without reinsurance this concentrates tail risk precisely where Ozon's own logistics assets also sit (double exposure).
3. Self-dealing / conflict optics — insuring goods sold on your own marketplace, underwritten by your own carrier, financed by your own bank raises claims-handling and fairness questions for sellers (cf. Wildberries' 1.96–5.6% rate hikes and Yandex's liability-dodging drawing seller pushback in 2026) and potential regulatory attention to captive economics.

**What this changes (idea-lens).** This is vertical integration, not a new market: Ozon converts a partner-fee line into a captive underwriting-plus-distribution stack, mirroring Sber's ecosystem-insurer playbook — the read-across is that every large Russian marketplace/bank ecosystem ends up owning a licensed carrier, squeezing independent insurtech partners out of the distribution they used to rent `(analysis)`. Falsifiable thesis: if Ozon discloses insurance GWP or a standalone solvency/combined ratio within ~4 quarters and it scales inside the fintech segment, the captive move is working; trigger to watch — first disclosed premium/loss figures in a 2026–27 Ozon filing, or conversely a CBR licensing delay / reinsurance gap that forces it back to the partner model, which would falsify the thesis.

Sources: https://www.interfax.ru/business/1122624 · https://www.retail.ru/news/marketpleys-ozon-uchredil-dve-strakhovye-kompanii-15-oktyabrya-2026-283360 · https://www.acra-ratings.ru/upload/iblock/780/mexawws2gub2lkkbc7y3w3mifxl2edf5/20251229_RFIABe.pdf · https://meduza.io/en/news/2026/08/07/russian-e-commerce-giant-wildberries-introduces-drone-attack-insurance · https://www.themoscowtimes.com/2026/10/15/from-wildberries-to-yandex-ukraine-is-turning-russian-business-giants-dominance-into-a-liability-a93976 · https://ir.ozon.com/en/sth/ozon-reports-second-quarter-2025-financial-results-and-raises-full-year-outlook-c397b9ca · https://worldef.com/2025/11/10/ozon-reports-q3-2025-net-profit-of-2-9-billion-roubles/ · https://cdn1.ozone.ru/s3/sigma-static-e93b3ad2-6f0b-4ad0-a53e-192ad6466704/Ozon_Databook_Q3_25.xlsx
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> Note: this story is a structural/product move (Ozon incorporating two insurers), not an earnings release. The review below grounds Ozon's scale and fintech trajectory in its latest FILED results — Q3 & 9M 2025 (filed 2025-11-10) — to frame the insurance expansion.

**Verdict (headline read).** BEAT / inflection confirmed · Group Q3 2025 revenue RUB 258.9bn (+69% YoY) · adj. EBITDA RUB 41.5bn (+215% YoY) · net profit RUB 2.9bn (vs −0.7bn loss in Q3 2024) · Fintech revenue RUB 53.9bn (+131% YoY). Ozon has flipped from land-grab to profitable growth, and Fintech is the principal margin engine — the backdrop that makes building captive insurers a logical next adjacency rather than a stretch. Guidance RAISED (GMV +41-43%, group adj. EBITDA ~RUB 140bn FY2025; Fintech revenue growth lifted to ~110% for 2025). No public consensus for a Russian-domiciled, recently-redomiciled name — beat/miss is framed vs prior year and prior quarters, numbers taken straight from the filing.

**Key figures (with growth).**
- GMV incl. services: Q3 2025 RUB 1,102.2bn (+53% YoY); 9M 2025 ~RUB 2.9trn. E-commerce orders Q3 667.8mln (+80%); active buyers 63.0mln (+18%).
- Group revenue: Q3 RUB 258.9bn (+69% YoY); 9M RUB 688.6bn (+73%). Gross profit Q3 RUB 60.1bn (+122%).
- Group adj. EBITDA: Q3 RUB 41.5bn (+215% YoY), margin 3.8% of GMV (vs ~1.8% a year ago); 9M RUB 164.8bn (+157%). Net profit Q3 RUB 2.9bn — second straight profitable quarter (first was Q2 2025).
- Operating cash flow Q3 RUB 133.6bn (+78%); cash & equivalents RUB 565.7bn (+145%).

**By segment / driver.** Two verticals: Marketplace (E-commerce) and Fintech.
- E-commerce: Q3 adj. EBITDA RUB 23.0bn (+407% YoY off a low base), driven by higher-margin services (commissions, advertising) and logistics operating leverage.
- Fintech (Ozon Bank): Q3 revenue RUB 53.9bn (+131% YoY); Q3 pre-tax profit RUB 17.7bn (+138% YoY). 9M Fintech revenue RUB 137.0bn (+150% YoY); 9M pre-tax profit RUB 41.8bn (+156%). Interest-earning assets RUB 592.3bn (+86% since year-start); customer funds RUB 438.1bn (+128% since year-start, +26% QoQ from RUB 348.6bn at 30 Jun). Active Fintech clients 39mln (from 11mln in 2022). 9M revenue mix 63% interest / 37% fee — i.e. Fintech is already a diversified bank, not just BNPL on the marketplace. Fintech operating cash flow +RUB 169.6bn YoY over 9M, the main source of group cash generation.
- Caveat (de-PR / who's quiet on what): NIM compressed — Q3 NIM 11.2% vs 14.6% a year ago (−3.4pp), risk-adjusted NIM 8.8% vs 12.1% (−3.3pp), and cost of risk worsened to −10.6% from −7.1% (−3.5pp). So Fintech growth is volume-led (asset and deposit book scaling fast) while per-unit spreads thin and credit costs rise — the standard trade-off of a lending book growing into new, less-captive customer segments.

**vs expectations / prior period.** No public sell-side consensus to anchor against (recently redomiciled MKPAO "Ozon"; MOEX trading of new shares began 2026-11-11). Qualitatively a clear BEAT vs prior year on every line (revenue +69%, adj. EBITDA +215%, swung to net profit) and acceleration vs prior quarters — this is the second profitable quarter after a long loss history and management calls out crossing into profit from Q2 2025. [No consensus figure available — UNSOURCED for any "vs Street".]

**Guidance / forward.** RAISED on the strength of 9M. FY2025: GMV incl. services +41-43% YoY (up from ~"40%" prior); group adj. EBITDA ~RUB 140bn; Fintech revenue growth lifted to ~110% for 2025 (from >80% at Q2). Medium-term Fintech targets: ~30% ROE and off-marketplace ("external") Ozon Card volume exceeding on-marketplace volume by end-2025. Management tone confident; emphasis on "balance between confident GMV growth, margin improvement and shareholder distributions" — alongside the first-ever dividend (RUB 143.55/share) and a RUB 25bn buyback through end-2026.

**Thesis-flags (framing the insurance move).**
1. Fintech is now Ozon's profit engine, not an accessory — Q3 pre-tax RUB 17.7bn and a diversified 63/37 interest/fee mix. Standing up Ozon Insurance / Ozon Life Insurance is a vertical-integration play to recapture insurance margin (embedded cover on orders, cards, loans) rather than passing it to third-party insurers → second-order: a new fee/float line that further diversifies away from NIM-sensitive lending just as NIM compresses.
2. Deposit base RUB 438bn (+26% QoQ) + 39mln active clients + 63mln buyers = a captive distribution channel insurers would pay to access; Ozon builds it in-house instead. Why it matters: life insurance in particular monetizes that deposit/float relationship and lengthens customer tenure.
3. NIM compression and rising cost of risk (−3.4pp / +3.5pp cost of risk YoY) are the quiet line — fee/insurance income is the hedge. The insurer licenses extend the "financial supermarket" from banking into protection, reducing reliance on spread income.
4. Execution/regulatory risk: new insurance carriers need CBR licensing, reserving and actuarial capability — a different risk profile from retail lending; traction is "announced," not yet earning. (analysis)

Sources: Ozon Q3 & 9M 2025 results (earnings_release, filed 2025-11-10), primary — https://cdn1.ozone.ru/s3/sigma-static-e93b3ad2-6f0b-4ad0-a53e-192ad6466704/Ozon_%D0%A4%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B5%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B%20%D0%B7%D0%B0%203%20%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B0%D0%BB%20%D0%B8%209%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2%202025%20%D0%B3%D0%BE%D0%B4%D0%B0.pdf (figures cross-checked against the identical deck mirrored at moex.com/media/finansovye-rezultaty-ozon-3-kv-2025.pdf) · public consensus: none available [UNSOURCED].
<!-- /enrichment:earnings_review -->
