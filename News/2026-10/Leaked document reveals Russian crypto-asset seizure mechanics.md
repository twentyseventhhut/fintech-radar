---
title: "Leaked document reveals Russian crypto-asset seizure mechanics"
date: 2026-10-13
retrieved: 2026-10-13
tags:
  - company/bybit
  - industry/crypto
  - industry/regtech
  - region/ru
  - type/regulation
sources:
  - https://www.bybit.com/en/help-center/article/Service-Restricted-Countries/trade/spot
status: published
n_mentions: 1
channels:
  - "Финтехно"
story_id: sb7d11fd5
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Leaked document reveals Russian crypto-asset seizure mechanics

> [!info] 2026-10-13 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] То есть либо официальный адрес для хранения арестованной криптовалюты создан внутри иностранной биржи, либо это просто промежуточный адрес. Сама Bybit пишет, что не обслуживает пользователей в ряде запрещённых юрисдикций и соблюдает санкционные ограничения.

## Первоисточники

### bybit.com
<https://www.bybit.com/en/help-center/article/Service-Restricted-Countries/trade/spot>
*362 слов · direct*

Service Restricted Countries
 As stated in Section 11.3 of the Bybit Platform Terms & Conditions and Section 3.4 of the BVAPO Platform Terms & Conditions (as applicable), Bybit does not offer services or products to Users in a few excluded jurisdictions including the United States, the Chinese Mainland, Hong Kong, Singapore, Canada, North Korea, Cuba, Iran, Uzbekistan, Russian-controlled regions of Ukraine ( the Crimea region of Ukraine (including Sevastopol) and the non-government controlled areas of the Donetsk, Luhansk, Kherson and Zaporizhzhia regions of Ukraine), Sudan, Syria, and in the case of Bybit Virtual Asset Platform Operator LLC only Dubai, or any other jurisdictions in which we maydetermine from time to time to terminate the services at our sole discretion (the “ Excluded Jurisdictions ”). You should inform us immediately if you become a resident in any of the Excluded Jurisdictions or are aware of any Users based in any of the Excluded Jurisdictions or if you are a Prohibited Party. You understand and acknowledge that if it is determined that you have given false representations of your location or place of residence or your status as a Prohibited Party, the Company reserves the right to take any appropriate actions in compliance with this restriction or in compliance with the law of a relevant jurisdiction, including termination of any Account immediately and liquidating any open positions. We also do not offer servicesto persons or entities in the U.S. Treasury Department’s List of Specially Designated Nationals or Blocked Persons, the EU’s Consolidated Financial Sanctions List or the UK Sanctions List, or any entity that is owned or controlled (50 percent or greater) by a person or entity on such lists or persons in Seychelles (excluding an international business company incorporated in accordance with The International Business Companies Act 2016 of Seychelles)(hereinafter “ Prohibited Parties ” with each such person or entity a “Prohibited Pary Party”), or offer services that involve or otherwise benefit Prohibited Parties. You understand that the Company reserves the right to take any appropriate actions in compliance with this restriction or in compliance with the law of a relevant jurisdiction, including termination of any Account immediately and liquidating any open positions.

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Leaked document reveals Russian crypto-asset seizure mechanics
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
A seizure **protocol** (следственный документ, not a leaked policy paper) dated **10 Oct 2026** surfaced in Russian crypto media (HashTelegraph, smart-lab). It documents what is described as one of the first practical applications of Russia's new crypto-seizure regime: an investigator in Kazan seized **≈$6,328 in USDT** from a defendant whose balance (~$6,641.84) sat on a **RoboForex** trading account, moving it via the **Difinex** payment service over the **TRON** network. The action was carried out "with the participation of the accused, her lawyer, and a specialist" — matching the statutory requirement.

The Финтехно fragment poses the item's real question: is the "official storage address for seized crypto" **created inside a foreign exchange** (the implication being Bybit), **or is it just an intermediary address?** The evidence answers it: Russia uses **"адреса-идентификаторы" (address-identifiers)** — intermediary/custody addresses provided by a state bank-agent together with an **authorized organization** (coordinated with **FSB and Rosfinmonitoring**), serving the MVD, FSB, Investigative Committee and Prosecutor's Office. These are **intermediary addresses, NOT accounts inside Bybit or any specific foreign exchange.** Bybit does not appear in the seizure protocol at all.

**+ Why structured this way / what it reveals:** The Bybit linkage in this note is weak and largely an artifact of the source mix. The only Bybit "source" is a generic help-center page listing excluded jurisdictions and sanctions compliance (standard boilerplate, Russia not even on the excluded list — only Crimea/occupied-Ukraine regions are). That page says nothing about custodying seized Russian state crypto. So the "Bybit address angle" is a hypothesis raised by the Финтехно commentator, not a documented fact — and the documented mechanics point the other way (state-controlled intermediary addresses). The genuinely informative core is the **legal/operational infrastructure**: Art. 164.2 of the Criminal Procedure Code (effective 3 Mar 2026), a government decree on storage/transfer/accounting of digital currency (reported variously as RF Government Resolution No. 808 of 30 Jun 2026 / in force ~3 Jul 2026), and the Putin-signed property-recognition law that lets courts seize crypto in criminal cases.

## [1] Competitors / peers (comparable regimes)
- **US DOJ / US Treasury:** mature crypto-seizure practice — DOJ Scam Center Strike Force seized >$578M in crypto ([[DOJ Scam Center Strike Force seizes over $578 million in crypto]]); US seized $61M USDT in a pig-butchering case ([[US seizes $61M in USDT linked to pig butchering crypto fraud scheme]]). US custodies seized crypto in government-controlled wallets and increasingly routes via qualified custodians.
- **Thailand** seized $420M tied to Cambodia scam ops ([[Thai authorities seize $420 million tied to Cambodia scam operations]]); **Kenya** froze crypto accounts in an anti-fraud probe ([[Kenya freezes crypto accounts in anti-fraud investigation]]).
- **Tether as a chokepoint:** the recurring enabler. Tether has frozen $4.2B over crime links ([[Tether says it has frozen $4.2 billion over crime links]]); as the USDT issuer it can block any address on a court/investigator order — which is why the Kazan case worked on USDT.
- **Position:** Russia is **catching up, codifying practice that already existed informally.** Deputy Justice Minister Ardabyeva explicitly framed the law as consolidating existing investigative practice. **+ Why:** Western seizures are AML/anti-fraud-oriented and transparent; Russia's build-out doubles as sanctions-evasion-adjacent infrastructure — the same state apparatus that custodies seized crypto also sits atop the A7/Garantex sanctions-circumvention nexus Elliptic has documented.

## [2] Company/state-actor history / fit
Russia moved from a near-ban posture to rapid codification in 2026: crypto recognized as property, Art. 164.2 live (Mar 2026), storage decree (mid-2026), and the broader crypto-market law effective **1 Sep 2026** licensing five participant categories (exchanges, brokers, management cos, depositories, exchangers) under a ~RUB cap on retail trading (~$3,700/yr equivalent). Central-bank supporting regulations were expected to be finalized ~**Oct 2026**. **+ Why the state acts this way:** sanctions have pushed Russia to treat crypto as both a controllable asset class (tax, seizure, confiscation) and a cross-border rail. Seizure mechanics are the enforcement leg of a regime being stood up at speed — "legalize so we can control, tax and confiscate," not "legalize for market freedom."

## [3] Novelty / value-add / traction
**Real novelty:** the publication of an actual applied protocol (amount, broker, rail, participants) — moving the story from "law passed" to "law used," which is the traction that matters. **What is NOT novel / overstated:** the Bybit framing. There is no evidence a seized-crypto custody address lives inside Bybit; the documented design uses state intermediary address-identifiers. Traction is still **tiny in scale** (a ~$6.3k single case) — this is a proof-of-mechanism, not mass enforcement. **+ Who captures control in the stack:** the leverage sits with (a) stablecoin issuers (Tether can freeze), and (b) the state bank-agent + FSB/Rosfinmonitoring-approved custodian holding the address-identifiers. Foreign exchanges like Bybit are peripheral and, if anything, de-risk by blocking Russian users (Moscow P2P-trader detentions, repeated account blocks) rather than acting as state custodians.

## [4] What's next / sentiment / risks
Expect more published protocols as courts and investigators standardize on Art. 164.2 and the storage decree; the CBR's final regulations (~Oct 2026) will formalize custodian roles. **Risks / open issues:** (1) authenticity — the smart-lab source flags the protocol could not be independently confirmed; (2) the real custody question (who technically holds keys to address-identifiers, and whether seized crypto can be liquidated/diverted) is unresolved; (3) second-order — the same infrastructure usable for legitimate seizure is usable for politically motivated confiscation (cf. the 2025–26 wave of elite property seizures, RUB 951bn in 2025). **+ Counterintuitive second-order:** codifying seizure makes Russian-held crypto *less* safe from the state, which pushes users toward self-custody and foreign/offshore venues — undercutting the state's own licensed-exchange buildout.

## Sources
See /tmp primary texts and inline URLs. Bybit help-center page (in note) is generic sanctions boilerplate and does NOT substantiate the custody-address claim.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is the "leaked document" actually a leaked policy paper, or just a routine seizure protocol?** → It is a **seizure protocol** (следственный документ) from a Kazan case, surfaced via crypto media (HashTelegraph/smart-lab), not a leaked MVD/FSB policy memo. The note's "leaked document" framing overstates it.
2. **Is the official storage address inside a foreign exchange (Bybit) or an intermediary?** → **Intermediary.** Russia uses state "address-identifiers" provided by a bank-agent + FSB/Rosfinmonitoring-approved custodian. No Bybit internal address is documented.
3. **Does Bybit actually appear in the seizure mechanics?** → **No.** Bybit's only presence is a generic help-center sanctions/excluded-jurisdictions page. The Bybit tag/source looks like a cross-wiring/ingest artifact. (Open: whether the Финтехно post discussed Bybit for a different reason.)
4. **Is Russia even on Bybit's excluded list?** → No — only Crimea and occupied-Ukraine regions are excluded; Russia proper is not. So the Bybit page doesn't even support a "Russia blocked" read directly.
5. **Is this really new, or codification of existing practice?** → Deputy Justice Minister stated the law **consolidates existing practice** of seizing from cold/hot wallets. Novelty = first *published applied* protocol, not a new power.
6. **What is the legal basis and its dates?** → Art. 164.2 CPC (eff. 3 Mar 2026); storage/transfer/accounting decree (reported as Gov't Resolution No. 808 of 30 Jun 2026, in force ~3 Jul 2026); crypto-market law eff. 1 Sep 2026; CBR final regs ~Oct 2026. (Open: exact decree number/date needs a primary-text confirm.)
7. **How large was the seizure?** → Tiny: ≈$6,328 USDT from a ~$6,641.84 RoboForex balance, via Difinex on TRON. Proof-of-mechanism, not scale.
8. **Who technically controls the seized crypto after transfer?** → State bank-agent + authorized custodian (FSB/Rosfinmonitoring-coordinated). Key-holding specifics and liquidation rights: **open.**
9. **What enabled the USDT seizure technically?** → Tether's freeze capability as issuer + broker/payment-rail cooperation (RoboForex/Difinex), not direct on-chain state seizure of private keys.
10. **Is the protocol authentic?** → smart-lab notes authenticity **could not be independently confirmed** — a material caveat.
11. **Freshness vs prior corpus?** → No prior note on Russian crypto seizure mechanics. Adjacent-only: [[Tether says it has frozen $4.2 billion over crime links]], [[DOJ Scam Center Strike Force seizes over $578 million in crypto]], [[US seizes $61M in USDT linked to pig butchering crypto fraud scheme]]. **FRESH** — new event, not a reprint.
12. **Who captures leverage in this stack?** → Stablecoin issuers (freeze) + state custodian of address-identifiers. Foreign exchanges are peripheral.
13. **Second-order risk?** → Same infrastructure enables politically motivated confiscation (cf. elite property-seizure wave, RUB 951bn in 2025); and it pushes users to self-custody/offshore, undercutting Russia's licensed-exchange buildout.
14. **What is NOT answered?** → Whether any seized crypto has actually been *confiscated/liquidated* (vs merely frozen), and the custodian's identity. **Open.**
15. **Why does this matter beyond Russia?** → Signals maturation of state crypto-seizure capability in a sanctioned jurisdiction, overlapping the A7/Garantex sanctions-evasion nexus Elliptic tracks.

Importance: 3/5 — Genuinely informative: first *applied* protocol under a fast-built Russian seizure regime, with a clear answer to the custody question (intermediary address-identifiers, not a Bybit internal address). Weighed down by: trivial amount ($6.3k), unconfirmed authenticity, and a misleading Bybit framing that the evidence does not support. Regionally/structurally relevant, but not a market-moving or precedent-setting event on its own.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-15]] (2026-10-15).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian state custody of seized digital assets is a brand-new sub-vertical spun out of the 2026 crypto-legalization wave. Per KuCoin/Cryptopolitan (as of 2026-07-07), Govt Resolution No. 808 set rules for storing/transferring/accounting seized crypto in criminal cases: a single state "Agent" bank (100% Russian-Federation-owned, custody free of charge) issues each authorized body (MVD, FSB, FTS, Prosecutor General, Investigative Committee, etc.) its own dedicated address-identifiers. Underlying law reclassifies digital currency as intangible property, letting investigators either seize hardware/wallets or move coins to "safe addresses" (per Bitget, 2026). In parallel, the Bank of Russia published its first register of regulated crypto operators (2026-10-06): 5 custodians (Sberbank, VTB, Atomyze, Voltari, Cloud Infrastructure) + 4 exchange operators (VTB, T-Invest Lab, Zefir, Sistema-Crypto); Sberbank targets Dec-1 for BTC/ETH/USDT products (per CoinDesk/Tokenpost, 2026-10). **Why now:** sanctions + the Sept-1-2026 Law on Digital Currencies forced Russia to build domestic state-controlled crypto rails (custody, exchange, forfeiture) nearly simultaneously. Market size: no data (no public AUC figure for seized-asset custody).

The leaked-document angle: the note's primary source is only Bybit's own Restricted-Countries T&C. The channel's claim is that an official seized-crypto storage address was created *inside a foreign exchange (Bybit)* — either as formal custody or a mere intermediate hop. This is unverified by any confirming source and sits in direct tension with Resolution 808's design, which routes custody through a 100%-state-owned Agent bank, not a foreign venue. Treat as **(hypothesis / leaked, unconfirmed)**.

**Competitive landscape.** KPIs for this niche: assets-under-custody of seized coins, number of authorized-body address-identifiers, recovery/conversion rate to rubles. Players are not commercial competitors but a state-mandated stack: the forfeiture Agent bank (Resolution 808) on one side; the newly-registered commercial custodians/exchangers (Sberbank, VTB) on the other. Foreign exchanges (Bybit, and historically others) are *rails of last resort* where Russian users actually hold coins — relevant because seizure of a wallet whose keys sit on an offshore exchange requires that exchange's cooperation (Cryptopolitan: "Russia to seek assistance from foreign exchanges when seizing crypto"). Bybit's position: its published T&C excludes Russian-controlled Ukrainian regions and OFAC/EU/UK-listed parties but does NOT list the Russian Federation itself as an excluded jurisdiction — leaving a live compliance grey zone. Protagonist (the Russian state) position: ahead on legal machinery, dependent on foreign venues for enforcement reach.

**Comps & multiples.** No valuation/round/deal in this story → trading multiples **not applicable / no data**. Internal comparables (base):
- [[Russia to legalize crypto for cross-border trade payments]] — the policy root enabling this whole stack (2025-10).
- [[Russia names first crypto-market depositaries and exchangers]] and [[Russia registers first crypto exchange operators and custodians]] — the BoR custody/exchange register (2026-10), the legal counterpoint to a foreign-exchange custody address.
- [[Финтехно banks race to control Russian crypto infrastructure]] — Sberbank/VTB land-grab over domestic crypto rails (2026-10).
- [[DOJ seizes $15B bitcoin from Cambodia pig-butchering scam]] and [[Vietnam police seize $34 million from NextTech founder]] — external precedents for state crypto seizure mechanics (2025-10).
- [[Reuters investigates Iran's largest crypto exchange Nobitex]] — sanctioned-state / exchange-as-rail analogue (2026-05).

**Risk flags.**
1. **Regulatory / legal-contradiction risk** — the leaked claim (seizure address inside Bybit) contradicts Resolution 808's 100%-state-Agent design; if real, it implies an off-book workaround outside the stated custody regime, with chain-of-custody and asset-safety exposure for seized coins. Single-source, so also *reporting risk*.
2. **Counterparty / exchange-exposure risk** — a foreign exchange holding (or routing) Russian state-seized assets can freeze, liquidate (its T&C reserves exactly this on "appropriate actions in compliance with law"), or lose access for Russian-linked flows; enforcement reach depends entirely on a venue outside Russian jurisdiction. Second-order: Russian users' own coins on Bybit are equally exposed to unilateral T&C action.
3. **Sanctions risk** — Bybit's own terms bar OFAC/EU/UK-listed parties and Russian-controlled Ukrainian regions; any state-body interaction with the platform risks tripping sanctions screens and secondary-sanctions exposure for the exchange, incentivizing it to sever rather than cooperate (undercutting Russia's "seek assistance from foreign exchanges" enforcement plan).

**What this changes (idea-lens).** (analysis) Russia is assembling the full sovereign crypto stack — legalize → register custodians → codify forfeiture — but enforcement still leaks offshore where coins actually live, making foreign exchanges the chokepoint. Falsifiable thesis: as the state Agent-bank custody goes live, seized-asset routing should migrate *off* foreign venues onto domestic state rails. Trigger to watch: an official confirmation (or denial) of a state storage address on any foreign exchange, and whether BoR-registered custodians (Sberbank, Dec-1) become the mandated destination for forfeited coins. What breaks the thesis: continued reliance on offshore addresses would signal the domestic stack can't yet reach assets held abroad.

Sources: https://www.kucoin.com/blog/rules-for-storing-seized-cryptocurrency-in-russia-what-resolution-808-established · https://www.cryptopolitan.com/russia-to-seek-assistance-seizing-crypto/ · https://www.bitget.com/news/detail/12560605191912 · https://www.coindesk.com/business/2026/10/13/russia-s-largest-bank-sberbank-secures-approval-to-trade-crypto · https://www.tokenpost.com/news/regulation/27394 · https://www.bybit.com/en/help-center/article/Service-Restricted-Countries/trade/spot
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
