---
title: "Финтехно: QIWI Bank collapse rooted in laundering-channel risk"
date: 2026-06-26
retrieved: 2026-06-26
tags:
  - company/qiwi
  - industry/payments
  - industry/regtech
  - region/europe
  - type/commentary
sources:
  - https://max.ru/fintexno
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: s1f28bd62
month: 2026-06
enriched: true
importance: 4
---

# Финтехно: QIWI Bank collapse rooted in laundering-channel risk

> [!info] 2026-06-26 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Проблема QIWI-Банка была не просто в формальных нарушениях ПОД/ФТ, а в риске превращения электронных кошельков, терминалов и платёжных агентов в инфраструктуру большого теневого денежного оборота. Что известно по итогам расследования МВД: ⚪️ В 2022–2023 годах с использованием похищенных персональных данных и дропов было создано более 24 тыс. кошельков, через которые вывели за рубеж более 30 млрд рублей, а также проходили расчёты для нелегального гемблинга, букмекерских сервисов, криптообмена и других теневых операций. ⚪️ В Москве арестованы трое фигурантов, предполагаемые организаторы находятся за границей. Руководители и владельцы группы компаний «Интерком» Григорий Кисильгоф и Денис Ли, а также Александр Михальчук, которого «Ъ» называет бенефициаром терминального бизнеса и дилеров сотовых операторов. Как работала схема Дроперы якобы лично приходили в офисы фигурантов и верифицировали электронные кошельки. Один кошелёк быстро привлёк бы внимание: большие обороты, странные операци

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: QIWI Bank collapse rooted in laundering-channel risk
_Analytical notes (not a post). Importance: 4/5._

This note is not "fresh news" — it is a **June 2026 criminal post-mortem** of a bank the Bank of Russia already killed on **21 Feb 2024**. The real value is the causal chain it closes: the CBR's 2024 abstract reason ("settlements between individuals and shadow businesses") is now backed by named suspects, a concrete dropper scheme and hard numbers. The story's weight is as a **case study of how a terminal+low-KYC-wallet model turns into shadow-money infrastructure**, not as a market-moving event (the entity is already liquidated).

## [0] What exactly happened (de-PR'd)
- The 2026-06-26 item reports **MVD (ГУЭБиПК) investigation findings**, surfaced via Kommersant/RIA: in **2022–2023**, **24,000+ QIWI wallets** were opened on **stolen personal data + droppers**; through them **30+ billion rubles** were moved abroad, plus settlements for illegal gambling, bookmakers, crypto exchange, drug trafficking. **Three suspects arrested in Moscow** (custody ordered 25 Jun 2026 by Meshchansky Court); alleged organizers abroad. Named: **Grigory Kisilgof** and **Denis Li** (owners of the "Intercom" group), and **Alexander Mikhalchuk** (named by Kommersant as beneficiary of the terminal business / cellular-dealer network). Criminal case opened **11 Feb 2026** under CC Art. 187 ch.2 + Art. 193.1 ch.3. All names, the 24k figure and 30bn figure are **confirmed** across MVD + multiple outlets.
- **Why this framing matters (→):** the channel headline ("not just formal AML breaches, but the risk of wallets/terminals/agents becoming big shadow-turnover infrastructure") is the correct read. → The structural fact is that QIWI ran **cash-in kiosks** (cash→digital, run via agent/dealer networks) **plus low-KYC e-wallets**. → Cash entry obscures origin; "simplified-ID" and anonymous wallets break traceability (ASV later found **9.3M wallets**, of which **7.15M simplified-ID** and **1.3M fully anonymous**); the dealer layer dilutes accountability. → So the 24k-wallet dropper scheme is not an aberration — it is the **designed-in failure mode** of the model, which is exactly what the CBR cited in 2024.
- **De-PR caveat:** one sensational add-on — that an anonymous QIWI wallet financed the **May 2023 assassination attempt on writer Zakhar Prilepin** — is attributed to the **Investigative Committee via Kommersant/Fontanka, NOT to the MVD statement**. Least corroborated element; keep hedged, do not lead with it.

## [1] Competitors / peers (the AML-revocation cohort)
The relevant peer set is not "payment innovators" but **regulators pulling licences over AML/shadow flows**, and the corpus has a clean cohort:
- [[Central Bank of Kenya strips PayU Kenya's payment license]] / [[Central Bank of Kenya revokes PayU Kenya license]] — revocation → **liquidation** (Aug 2025), same arc as QIWI (revoke → forced liquidation Apr 2024 → wind-down Nov–Dec 2025).
- [[Dutch central bank fines bunq for AML control failures]] — DNB fined bunq (May 2025) for "serious shortcomings" in AML controls — the **fine-not-revoke** end of the spectrum; QIWI is what happens when fines (Dec 2020: RUB 11M + foreign/prepaid restrictions) **fail to change behavior** across five supervisory measures in 12 months.
- [[MAS revokes Bsquared Technology's major payment institution license]] (May 2026) — another payments-licence revocation, showing this is a **global supervisory pattern**, not Russia-specific.
- [[Russia's A7 cross-border payments firm plans global expansion]] — the **counter-current**: as the CBR kills a shadow-channel bank, sanctioned cross-border vehicles (A7, "gold bank") are being built to move money out of Russia. → The demand for grey cross-border rails doesn't vanish with QIWI; it **migrates**.
- **Why the cohort looks this way (→):** the common denominator is **low-friction money-in + weak identity binding** (e-wallets, terminals, EMIs). Regulators that catch it early fine (bunq); those that catch it late revoke and liquidate (QIWI, PayU, Bsquared). QIWI sits at the **terminal** end of the spectrum: the longest leash (Dec 2020 → Feb 2024), the largest blast radius (9.3M wallets, Contact = ~500 points in 180 countries).

## [2] Company history / fit
- **Trajectory:** OSMP/OE merger 2007 → cash-in terminals + QIWI Wallet → NASDAQ IPO 2013 (MOEX dual-listed). **Dec 2020:** first major CBR sanction (RUB 11M fine + curbs on foreign payments and prepaid-card transfers). **Feb 2022:** NASDAQ suspends trading post-invasion. **2023:** corporate split — Russian assets into JSC Qiwi; international parent stays Qiwi plc (Cyprus). **Jan 2024:** Russian assets sold to a management group led by CEO **Andrey Protopopov** for **23.75 billion rubles** (via Fusion Factor Fintech, HK), closed 29 Jan 2024. **21 Feb 2024:** CBR revokes JSC QIWI Bank's licence (Order OD-266); MOEX receipts ~-50% to record low. **Apr 2024:** forced liquidation. Parent renamed **NanduQ plc** (effective Feb 2025), moved to Astana (AIX). NASDAQ delisting effective **16 Sep 2024**. Liquidation completed **Nov–Dec 2025** (creditor claims reportedly satisfied 100%).
- **Why the company acted this way (→):** the **23.75bn sale closed 29 Jan 2024, three weeks before the revocation of 21 Feb 2024**. → The management buyout offloaded the toxic Russian entity from the listed parent **just ahead of the kill** — whether prescient or informed, it ring-fenced the international shell (now NanduQ) from the bank's collapse. → So the "QIWI collapse" is two separate events: the **regulatory death of the Russian bank** and the **survival of an international husk** that quietly relisted in Kazakhstan. The PR-flattering frame ("orderly restructuring") hides that the substance — the licence, the wallets, the AML liability — all stayed in the entity that was about to die.

## [3] Novelty / value-add / traction
- **What is genuinely new here (June 2026):** the **named mechanism and beneficiaries** behind the CBR's 2024 abstraction. Until now the public record had "high-risk transactions for shadow businesses"; now it has 24,000 dropper wallets, 30bn rubles, and three named men tied to the **terminal/dealer** business — i.e., the laundering ran through the **physical agent network**, not just the wallets. → That is the load-bearing finding: it locates the failure in the **dealer/terminal layer**, the part hardest to KYC.
- **Traction = the body count, not adoption:** ASV found **9.3M wallets / RUB 4.4bn**; insured liability ~RUB 4.6bn; payouts RUB 880M (day 2) → RUB 3.26bn (by 15 Mar 2024, ~75% of depositors); final ~RUB 37.2bn disbursed to 79,000+ creditors (single-source RIA/Vedomosti). Network at death: ~16.6M wallets/virtual cards, ~106,000 terminals.
- **Why the value-add is real (→):** this isn't a press release — it is **enforcement converting a supervisory assertion into a prosecutable scheme**. → For a fintech-regulation reader the durable lesson is unit-economic: the same features that made QIWI cheap and ubiquitous (anonymous cash-in, simplified-ID wallets, broad dealer reach) are exactly what made it a **negative-externality machine** that the regulator eventually had to write off entirely. The "margin" of the shadow model was captured by the dropper operators; the losses by depositors and the DIA.

## [4] What's next / market sentiment
- **No live market impact:** the bank is liquidated, the parent (NanduQ) delisted from NASDAQ (Sep 2024) and MOEX (Nov 2025), trading thinly on AIX. This is a **legal/historical** story, not a tradable one.
- **What's next:** the criminal cases proceed against the three arrested; organizers are abroad (extradition unlikely → likely in-absentia). Expect the **Prilepin-financing thread** to drive Russian-media coverage — handle as СК-attributed and unproven.
- **Why the market/regulatory direction matters (→):** the second-order effect is **migration, not elimination**. → As Russia closes domestic low-KYC rails (QIWI killed; anonymous top-ups progressively banned under 115-FZ), grey cross-border demand shifts to **sanctioned/state-adjacent vehicles** ([[Russia's A7 cross-border payments firm plans global expansion]]) and to crypto. → Counterintuitively, the QIWI takedown may **concentrate** shadow flows into fewer, more politically-protected channels that are harder, not easier, for any single regulator to unwind. The lesson for non-Russian regulators (Kenya/PayU, Singapore/Bsquared, NL/bunq): catch the EMI/terminal model **before** it scales to 9M wallets.

## Sources
- Bank of Russia, Order OD-266, licence revocation (verbatim reasons): https://www.cbr.ru/eng/press/pr/?id=39708
- MVD/Kommersant June 2026 scheme (24k wallets, 30bn rub): https://www.kommersant.ru/doc/8765193 · https://ria.ru/20260626/moshennichestvo-2101179333.html
- Custody order, suspects: https://www.fontanka.ru/2026/06/25/76499480/ · https://iz.ru/2122163/2026-06-25/
- ASV 9.3M wallets / RUB 4.4bn breakdown: https://www.vedomosti.ru/finance/articles/2024/02/26/1022198-asv-obnaruzhil-v-kivi-banke-93-mln-koshelkov
- DIA payouts: https://www.rbc.ru/rbcfreenews/65e1f7279a7947468052b891 · https://www.rbc.ru/rbcfreenews/65f3fa729a79473472e1a740
- 23.75bn sale to Protopopov / close: https://interfax.com/newsroom/top-stories/98625/ · https://interfax.com/newsroom/top-stories/98921/
- Dec 2020 CBR fine: https://www.rbc.ru/finances/10/12/2020/5fd1c2a39a79479a4074495b
- Network at revocation, Contact: https://tass.com/economy/1749559 · https://www.rbc.ru/finances/21/02/2024/65d5a51b9a794792398eeb08
- Final liquidation (single-source): https://ria.ru/20251117/banu-2055523427.html
- Internal: [[Central Bank of Kenya strips PayU Kenya's payment license]] · [[Dutch central bank fines bunq for AML control failures]] · [[MAS revokes Bsquared Technology's major payment institution license]] · [[Russia's A7 cross-border payments firm plans global expansion]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions (second-order)

1. **Is this actually new, or a re-run of the Feb 2024 revocation?** — Partly new. The CBR's revocation (21 Feb 2024) already cited shadow-business settlements; June 2026 adds the **named mechanism** (24k dropper wallets, 30bn rub) and **named beneficiaries** (Kisilgof, Li, Mikhalchuk / "Intercom"). The novelty is enforcement, not the diagnosis. **Answered.**

2. **Are the headline numbers (24,000 wallets, 30bn rubles) verified or single-source?** — Confirmed: stated by MVD (ГУЭБиПК) and carried by RIA, Izvestia, Fontanka, Kommersant and others. **Answered.**

3. **Does the 30bn-rub-abroad figure overlap with the RUB 4.4bn ASV found in wallets, or are they different scopes?** — Different scopes. The 30bn is **cumulative flow moved abroad over 2022–2023**; the 4.4bn is the **static balance** sitting in 9.3M wallets at the moment of revocation. Do not conflate flow with stock. **Answered.**

4. **Why did it take the CBR from Dec 2020 (first fine) to Feb 2024 to revoke?** — Open / analysis. Five supervisory measures in the final 12 months suggest escalating-but-tolerated breaches; the political/economic value of QIWI's ubiquity likely lengthened the leash. CBR never disclosed the specific tolerated transactions. **Partly open.**

5. **Did the Jan 2024 sale to Protopopov insulate the listed parent from liability — coincidence or foreknowledge?** — The 23.75bn sale **closed 29 Jan 2024, 23 days before** the 21 Feb revocation. Sequencing strongly suggests ring-fencing of the international shell (now NanduQ) ahead of the kill. Foreknowledge is **unproven (hypothesis)**; the timing is fact. **Partly open.**

6. **Who actually bore the losses?** — Depositors covered to RUB 1.4M each by DIA; DIA/ASV (state) absorbed insured liability (~4.6bn) and ran liquidation; final ~37.2bn disbursed to 79,000+ creditors with reported 100% satisfaction (single-source RIA/Vedomosti). Shadow operators captured the upside. **Answered (final totals single-source).**

7. **Is the Prilepin-assassination-financing claim safe to publish?** — No, not as fact. Attributed to the **Investigative Committee via Kommersant/Fontanka, not the MVD**; least corroborated. Hedge or omit. **Answered.**

8. **Did the shadow flows stop when QIWI died, or migrate?** — Analysis: demand for grey cross-border rails persists; corpus shows sanctioned vehicles ([[Russia's A7 cross-border payments firm plans global expansion]]) and crypto absorbing it. Net effect is migration/concentration, not elimination. **Answered (analysis).**

9. **Was the laundering primarily a wallet problem or a terminal/dealer problem?** — June 2026 locates beneficiaries in the **terminal/dealer/cellular-operator** business (Mikhalchuk), and droppers physically verified wallets in offices — pointing to the **agent layer** as the weak point, the part hardest to KYC. **Answered.**

10. **How does QIWI compare to the corpus's other licence-loss cases?** — Same arc as [[Central Bank of Kenya strips PayU Kenya's payment license]] (revoke→liquidate) and [[MAS revokes Bsquared Technology's major payment institution license]]; contrast with [[Dutch central bank fines bunq for AML control failures]] (fine, not revoke). QIWI is the largest blast radius (9.3M wallets). **Answered.**

11. **Is there any live, tradable market angle?** — No. Parent NanduQ delisted from NASDAQ (Sep 2024) and MOEX (Nov 2025); thin AIX listing. Historical/legal story only. **Answered.**

12. **Could the "100% creditor satisfaction" claim be PR?** — Possibly. Rests mainly on RIA/Vedomosti (17 Nov 2025); not independently audited in the sources gathered. Treat as reported, not verified. **Open.**

13. **What is the durable lesson vs the transactional headline?** — Durable: low-KYC cash-in (terminals) + simplified-ID wallets + broad dealer networks = a structural shadow-money machine that fines won't fix once scaled; regulators must intervene pre-scale. Transactional: the arrests themselves. **Answered.**

14. **Does this change Russia's payments landscape going forward?** — Marginally. The bank is gone; the structural demand it served shifts to state-adjacent rails and crypto. Bigger signal is CBR's willingness to liquidate a systemically-embedded payments name over AML. **Answered (analysis).**

15. **Any date/attribution artifacts to avoid repeating?** — Yes: a stray "24 March 2026" MVD date appeared only in a search snippet and conflicts with the 11 Feb (case opened) / 25 Jun (arrests) timeline — treat as artifact. Verify 115-FZ article numbers if made load-bearing. **Answered.**

Importance: 4/5 — A well-documented, primary-source-verified case study that closes the causal loop on a major payments-bank collapse and crystallizes a structural AML lesson (terminal + low-KYC wallet = shadow infrastructure), with strong corpus parallels. Capped below 5 because it is a backward-looking post-mortem with no live market impact, the most striking sub-claim (Prilepin financing) is unverified, and final liquidation totals are single-source.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-06-27]] (2026-06-27).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russia's retail-payments stack split into two opposing tracks, and QIWI's model sat on the losing side of both. (1) **Structural decline of the cash-in-terminal + e-wallet niche**: QIWI's own active-wallet base was already shrinking pre-collapse — **14.1M active wallets (2021) → 13.8M (2022)** (per Statista/company data, via marketscreener), and its kiosk network fell to **~93,244 terminals at end-2021** from a >100k peak (Statista, via web), only nominally back at ~106k at the 2024 death. The August 2020 ban on anonymous wallet top-ups had already cut the user base of QIWI/VK Pay/WebMoney. → The terminal/anonymous-wallet model was a **declining, regulation-squeezed niche before the AML case ever surfaced** — the collapse accelerated an existing structural sunset, it did not interrupt a growth story. (2) **Displacement by state rails**: the CBR's **SBP (Faster Payments System)**, free 24/7 P2P + QR settlement in central-bank money, and **MIR** card scheme are the secular winners; SberPay/YooMoney (Sber-owned, **15M+ users**, ~180k merchants on YuKassa as of May 2023, per yoomoney) absorb the legitimate cash-out demand QIWI used to serve. **Why now:** regulation is the driver, not technology — **522-FZ (28 Dec 2024)** set a **RUB 100,000 ceiling on simplified-identification transfers** (full ID required above; web sources), structurally closing the low-KYC gap QIWI monetized. The entry barrier in this sub-sector flipped from "cheap, ubiquitous cash-in" to "regulatory compliance + state-rail integration" — a barrier QIWI's model could not clear.

**Competitive landscape.** Sector KPIs: active wallets, terminal count, TPV, take rate on cash-in, simplified-ID share. QIWI at death — ~16.6M wallets/virtual cards, ~106k terminals, **9.3M wallets of which 7.15M simplified-ID + 1.3M fully anonymous** (already in [0], not re-derived here). The legitimate successor set is **state-adjacent**: SBP/MIR (CBR-controlled), **YooMoney/SberPay** (Sber), Tinkoff Wallet — i.e. the demand migrated to **bank-backed, fully-KYC'd ecosystems**, the opposite of QIWI's anonymous-cash-in basis of competition. QIWI's only durable asset was distribution (terminal ubiquity), which SBP-QR made obsolete by pushing acceptance onto any smartphone at ~0% acquiring. Position: **terminal cash-in = niche in terminal decline**, no moat — its "network" (106k kiosks) was a depreciating physical footprint, not switching-cost lock-in; users left for free state rails the moment the bank died.

**Comps & multiples.** No live valuation: parent NanduQ is delisted (NASDAQ Sep 2024, MOEX Nov 2025), thin AIX; the Russian bank is liquidated. The only public transaction price is the **Jan 2024 management buyout of Russian assets at RUB 23.75bn** (~$265M at ~RUB 90/$ as of close, [UNSOURCED] exact FX) — a **distressed/ring-fencing price three weeks before revocation**, not a clean market comp; per-wallet that is **RUB 23.75bn / 16.6M wallets ≈ RUB 1,430/wallet (~$16)**, a fire-sale level reflecting embedded AML liability, not franchise value. Internal comps (AML-revocation cohort, same revoke→liquidate arc) already wikilinked in [1]: [[Central Bank of Kenya revokes PayU Kenya license]] · [[MAS revokes Bsquared Technology's major payment institution license]] (revoke→liquidate); [[Dutch central bank fines bunq for AML control failures]] (fine, not revoke — the earlier-intervention end); migration counter-current [[Russia's A7 cross-border payments firm plans global expansion]]. Trading-multiple comparison: **distribution not computed** — no comparable disclosed revenue/EBITDA for the dead entity; qualitative only. Outlier flag: the RUB 23.75bn sale is **cheap vs any going-concern payments multiple**, correctly so — the discount IS the AML-liability mark.

**Risk flags.**
1. **Shadow-flow migration confirmed by the regulator, not eliminated** — Rosfinmonitoring deputy head **German Neglyad** publicly stated high-risk clients "have indeed moved to other lending institutions" after QIWI's death (Interfax, 2024). Why it matters: the takedown displaced the risk into other banks and (per [4]) sanctioned cross-border vehicles/crypto — second-order effect is **concentration into harder-to-unwind channels**, so the sector's AML exposure is relocated, not retired.
2. **Successor-rail concentration into state hands** — the legitimate demand migrated to CBR-owned SBP/MIR and Sber's YooMoney/SberPay. Why it matters: replacing a private low-KYC operator with state-controlled rails raises **surveillance/single-point-of-control** concentration; competitively it leaves little room for an independent private wallet to re-enter the niche.
3. **Regulatory model-risk for any low-KYC/terminal/EMI operator globally** — QIWI is the worked example that fines (Dec 2020: RUB 11M) do not change behavior once the model is scaled to 9M+ wallets; the only fix was liquidation. Why it matters: prices in a **binary tail risk** (revoke→liquidate) for the EMI/terminal sub-sector that the cohort comps (PayU, Bsquared) confirm is a global, not Russia-specific, supervisory pattern.

**What this changes (idea-lens).** Consolidation/elimination of the independent anonymous-wallet+terminal niche in Russia, not a re-rating — the value migrates to state rails (SBP/MIR/Sber) and, for grey flows, to sanctioned cross-border vehicles and crypto (analysis). Falsifiable thesis: if a new private low-KYC cash-in operator gains share post-QIWI, the "state-rail capture" read is wrong; **trigger to watch** — any CBR enforcement action against a *successor* bank named by Rosfinmonitoring as having absorbed QIWI's high-risk clients would confirm the migration-not-elimination thesis. (analysis)

Sources: https://www.marketscreener.com/quote/stock/QIWI-PLC-13125210/news/Russia-s-CBR-shuts-down-major-e-payment-player-Qiwi-46006096/ · https://www.statista.com/statistics/1123430/qiwi-value-of-total-payments-by-category/ · https://yoomoney.ru/ · https://valen-tax.com/blog/new-rules-for-money-transfers-in-russia-as-of-may-30-2025-what-has-changed-for-individuals-and-businesses/ · https://interfax.com/newsroom/top-stories/104980/ · https://www.cbr.ru/eng/press/pr/?id=39708
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
