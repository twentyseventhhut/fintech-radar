---
title: "Bank antifraud signals to be shared with digital platforms"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - industry/fraud-risk
  - industry/regtech
  - region/ru
  - type/regulation
sources:
  - https://max.ru/fintexno
status: enriched
n_mentions: 1
channels:
  - "Финтехно"
story_id: s9172c08c
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Bank antifraud signals to be shared with digital platforms

> [!info] 2026-10-08 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Финтехно

## Агрегированный текст (из дайджестов)

[Финтехно] Банковские антифрод-сигналы начинают работать за пределами банков — сведения о мошенниках и жертвах мошенничества будут получать цифровые платформы, и на их основе ограничивать связанные с риском учётные записи. До сих пор банк в основном управлял риском внутри своей транзакции или клиентского профиля. Минцифры говорит, что обмен уже запускается и для этого не нужны дополнительные изменения законодательства, а следующим сценарием будет передача сведений об умерших. В документах, может быть, и не потребуется апдейтов — но превратить формальный обмен в полезный продукт ещё предстоит. Кросс-индустриальный подход расширяет антифрод с отдельных операций до цепочки цифровых аккаунтов — но как конкретно платформа должна реагировать на сигналы, кто несёт ответственность за ошибки и каким будет реальный жизненный цикл такой информации (от присвоения статуса до снятия или оспаривания) — пока вопрос. Ответственность платформ, которые получили сигнал о мошенничестве, но не приняли меры, тоже ещё

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://max.ru/fintexno>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Bank antifraud signals to be shared with digital platforms
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On **7 Oct 2026**, at the "Digital Solutions" (Цифровые решения) forum at the National Centre "Russia", **Tatyana Skvortsova, director of Mintsifry's department for digital-identification technologies**, stated that banks and telecom operators will begin feeding **digital platforms** three categories of signal: **(1) fraudsters, (2) fraud victims, and (3) — next scenario — deceased persons**, so platforms can restrict/block the associated accounts. Her load-bearing claims: the fraudster/victim exchange **"is already launching"** and **"requires no additional legislative changes"**; deceased-person data is the next step.

De-PR'd: this is a **ministry official's verbal statement of intent at a forum**, not a decree, signed law, or a documented live production system. The newsworthy, checkable core — "already launching / no new law needed" — is exactly where sourcing is thinnest: no official text, no scope spec, no data-verification/dispute procedure. One trade outlet (Anti-Malware, 2026-10-08) explicitly flags the absence of an implementation timeline, verification procedures, and account-handling protocols.
- **Why framed this way:** "no new law needed" is a deliberate signal that the exchange rides on the **already-existing GIS "Antifrod" rails (FZ 41-FZ)**, whose GIS provisions went live 1 Mar 2026 — so Mintsifry can present a sub-legislative expansion as a done deal, not a bill subject to a comment period. → why it matters: it lets the ministry move fast and avoids Duma friction, but it also means there is **no fresh statutory basis defining platform duties, liability, or a dispute mechanism** — the governance is asserted, not legislated.
- **Named platforms:** Yandex reportedly already connected; Avito and RVB (Wildberries–Russ JV) pending. Ozon not named. Note a naming-collision to avoid: this is distinct from Mintsifry's separate **"Antifrod 3.0" third legislative package** (draft out for comment ~30 Sep–15 Oct 2026, covering SIM/eSIM, 3-yr data retention, unified consents on Gosuslugi).

## [1] Competitors / peers (regulatory analogues)
- **UK — CIFAS National Fraud Database** + mandatory APP-scam reimbursement (PSR, Oct 2024): the closest analogue (cross-sector fraud markers + refund regime) — but it has a **formal dispute/evidence framework** Russia's version lacks.
- **Singapore — Shared Responsibility Framework + ScamShield**: bank/telecom shared liability.
- **EU — GDPR**: cross-sector sharing of fraud/victim data into *commercial platforms* is far more constrained — a useful contrast for RF's thin data-protection basis.
- **Why the lay of the land:** mature regimes paired data-sharing with (a) a defined liability allocation and (b) a correction/appeal path. RF is building the data pipe first and leaving liability "under discussion" → second-order: the system can scale faster but accumulates false-positive and due-process debt that will surface later.

## [2] Company / regulator history / fit
Lead actor is **Mintsifry** (with Roskomnadzor), not the Bank of Russia — CBR is a data contributor, not announcer. RF has built antifraud infrastructure in layers:
- FinCERT/ФинЦЕРТ (CBR, since ~2015) — inter-bank fraud info exchange.
- CBR "database of transfers without client consent" + **369-FZ (25 Jul 2024)**: 2-day pause on suspicious transfers + mandatory refund; drop-recipient blacklist.
- **Dropper database** (база дропперов, 2024–25).
- **Self-ban on loans** via Gosuslugi (1 Mar 2025).
- **FZ 41-FZ** (signed 1 Apr 2025; GIS "Antifrod" live 1 Mar 2026) — the vehicle obliging operators, banks and platforms to feed fraud data.
- **Why Mintsifry acts now:** having built the GIS pipe and obliged platforms to *contribute*, the logical next move is to let platforms *consume* signals — turning a one-way reporting duty into a two-way exchange. The structural pressure is that fraud has migrated from the bank transaction to the whole digital-account chain (cf. the QR/dropper scheme below), so a bank-only antifraud perimeter is no longer sufficient.

## [3] Novelty / value-add / traction
Genuinely new: **cross-industry extension** of antifraud from a single bank's transaction/profile to the chain of digital accounts across marketplaces/classifieds. That is a real conceptual step beyond prior RF schemes (which kept fraud data inside the banking/telecom + state loop).
- **But traction is thin:** only one platform ("Yandex connected") is claimed, with no independent confirmation; Avito/RVB are "expected". "Already launching" ≠ live, measured production. No volumes, no account-action counts, no false-positive data.
- **Where value breaks (analysis):** the value-add depends entirely on the **error lifecycle** — how a "fraudster" flag is assigned, disputed, and removed. Without that, the signal is noise that platforms either over-enforce (mass wrongful restrictions, esp. for mis-tagged mules/victims) or ignore (no liability for inaction). → the central question shifts from "is cross-industry sharing useful?" to **"who owns the false-positive cost and the dispute, and who is liable when a received signal is ignored?"** — both currently undefined.

## [4] What's next / sentiment / risks
Next scenario: **deceased-person data** (operators/banks → platforms) to block dormant accounts — but sourcing notes it doesn't address inheritance/heir access or content retention (block ≠ delete). Watch whether this folds into or stays separate from "Antifrod 3.0" (comment period to 15 Oct 2026).
- **Risks:** 152-FZ (personal-data) basis for piping *victims'* identities to commercial marketplaces is claimed, not shown; no sanction/standard for platform inaction; no appeal for mis-flagged users; false-death flags are an account-takeover/harassment vector. **Scope-creep (analysis):** a "risk-signal" pipe into platforms with no statutory cap can expand to adjacent categories.
- **Sentiment:** trade press is cautiously skeptical — direction is real and overdue, execution governance is missing.

## FRESHNESS / DUPLICATE VERDICT
**FRESH.** This is a distinct, newly-dated event (7 Oct 2026 forum statement on bank/telecom → platform signal sharing + deceased-person scenario). Adjacent priors exist but cover different events: [[Russia's Mincifry drafts scam-victim compensation rules]] (compensation procedure, Jul 2026), [[Russian central bank proposes Gosuslugi fraud-victim support service]] (victim navigation service, Jun 2026), [[T-Bank and CBR flag new crypto-based bank antifraud scheme]] (QR/dropper scheme, Jul 2026). None is the same announcement — no duplicate.

## Sources
- RIA Novosti 07.10.2026 — https://ria.ru/20261007/smert-2123051888.html
- PRIME 07.10.2026 — https://1prime.ru/20261007/operatory-874051259.html
- Anti-Malware 08.10.2026 (gaps) — https://www.anti-malware.ru/news/2026-10-08-1447/51669
- Infox (41-FZ framing) — https://www.infox.ru/news/299/381840
- FZ 41-FZ / GIS Antifrod — https://base.garant.ru/411783215/
- FinCERT (CBR) — https://www.cbr.ru/analytics/ib/fincert/
- 369-FZ refunds 24.07.2024 — https://rg.ru/2024/07/24/zaplatiat-iz-svoego-karmana.html
- Internal priors: [[Russia's Mincifry drafts scam-victim compensation rules]], [[Russian central bank proposes Gosuslugi fraud-victim support service]], [[T-Bank and CBR flag new crypto-based bank antifraud scheme]], [[Russian central bank measures payment-service satisfaction metric]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team challenge questions

1. Is there any **published legal act / GIS "Antifrod" regulation** authorising platform *receipt* of bank/telecom fraud-victim-death data, or is "no new law needed" an unsupported ministerial reading of FZ 41-FZ? — **Open; no official text cited. This is the pivotal weakness.**
2. What does **"already launching" actually mean** — is Yandex in measured production, or merely technically onboarded to the GIS? Any confirmation from Yandex/Avito/RVB themselves? — Open; no platform-side confirmation found.
3. **152-FZ (personal data) basis:** on what legal ground do banks hand *victims'* identities to commercial marketplaces, and with what purpose limitation? — Open; basis asserted, not shown.
4. What is the **definition and evidentiary threshold** for the "fraudster" label — self-report, MVD data, bank suspicion, drop-DB inclusion? False-positive rate? — Open.
5. **Dispute / correction:** can a flagged person see, contest, or remove the flag at platform level, and in what timeframe? Who bears the cost of wrongful restriction? — Open; no mechanism specified.
6. **Platform liability:** sanction if a platform ignores a signal and harm follows — and conversely, liability for *over-blocking* a legitimate user? — Explicitly "under discussion"; undefined.
7. On **deceased persons:** what verifies death (ZAGS registry vs a bank's own flag), and how are **false death flags** (a takeover/harassment vector) detected and reversed? — Open.
8. Does the deceased flow **conflict with inheritance law** (heir access to accounts/funds/digital assets) and content-retention duties? — Not addressed; block vs delete vs inherit conflated.
9. Why share **victims' identities with marketplaces at all** — what legitimate platform action requires knowing the victim rather than just the fraudster? — Unexplained.
10. Is this a **confirmed cross-industry live exchange or a forum statement of intent** that may not survive inter-agency review / the "Antifrod 3.0" comment period? — Statement of intent; direction real, execution unproven.
11. **CBR's role:** the announcer is Mintsifry; has the Bank of Russia confirmed it will route FinCERT/drop-DB data to commercial platforms, and under what mandate? — Open.
12. **Scope-creep cap:** once a "risk-signal" pipe into platforms exists with no statutory limit, what prevents expansion to tax/political/other categories? — No cap stated.
13. How does this interact with the **mandatory scam refund (369-FZ)** and the Mincifry compensation procedure ([[Russia's Mincifry drafts scam-victim compensation rules]]) — does a platform-received signal shift liability? — Open; no linkage specified.

Importance: 3/5 — A genuinely new cross-industry concept (antifraud extended from the single bank transaction to the digital-account chain across marketplaces), driven by a real regulator (Mintsifry) on existing GIS "Antifrod"/41-FZ rails, in a high-salience RF fraud-policy stream. Capped at 3 because it is a **forum statement of intent, not a decree or confirmed live system**: traction is one unconfirmed platform ("Yandex connected"), and the whole value-add hinges on an error/dispute/liability framework that is explicitly undefined. Upgrade to 4 if an official regulation or confirmed multi-platform production rollout appears.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Russian cross-industry antifraud / fraud-data-sharing. The protagonist is not a company but a state-coordinated data-sharing scheme (Mincifry / Ministry of Digital Development) that pushes bank-held fraud signals (fraudsters + victims) out to digital platforms so they can restrict risk-linked accounts. Market size: Russian fraud losses are large and rising — fraudsters stole ₽27bn from Russians in 2024, with non-consensual transactions up +74% YoY (per CBR, via en.iz.ru, Feb 2025). Sber estimated >₽80bn stolen YTD by mid-2025 and projected ₽330–340bn full-year 2025 if the trend held (per Sber, via TASS, 2025). CBR reports banks prevented ₽3.5tn of theft attempts in 2025 Q3 (per CBR, Oct 2025), and suspicious transactions fell -12% in 2025 H1 (per CBR) — so prevention is scaling even as gross attempts grow. Structure: heavily state-orchestrated, not a competitive private market — value sits with whoever runs the central registry (CBR / Gosuslugi / Mincifry), while banks and platforms are mandated participants. Entry barrier = regulatory mandate, not product. Why now: part of the "Antifraud" legislative package (2025), with "Antifraud 3.0" slated for State Duma in autumn 2026 (per Interior Ministry, via en.iz.ru, Sep 2026) and a Gosuslugi "red button" due by year-end 2026 (per www1.ru, Oct 2026). Mincifry's claim that the exchange needs no new legislation (analysis) signals it is bolting onto existing infrastructure (FinCERT, the KYC Platform) rather than building greenfield.

**Competitive landscape.** Sector KPIs: fraud-loss ₽ volume, share of losses reimbursed, number of blocked/restricted accounts, suspicious-transaction decline %. Existing Russian rails this builds on: CBR's **FinCERT** (>1,700 institutions, incl. all Russian banks, exchanging incident data with police, telecoms, AV vendors — per CBR); the CBR **"Know Your Customer" Platform** (live since 1 Jul 2022; restricted transactions for >178,000 high-risk entities over three years — per CBR); the CBR **dropper database** (banks suspend remote access for registered mule accounts — per CBR); and a planned biometric voice-of-scammers database (Minfin + MVD + Roskomnadzor + CBR, due before 1 Apr 2026 — per en.iz.ru). Recent moves: Moscow Times (21 Oct 2025) reported a cross-agency cybercriminal-tracking database (police + CBR + Rosfinmonitoring). The genuinely new element here is cross-industry propagation of bank signals to non-bank digital platforms (marketplaces, services) — extending antifraud from the transaction/customer-profile layer to the chain of digital accounts. Position: this is a scope-extension of an already-mature bank-side system, not a new entrant; the moat is the state mandate + incumbency of FinCERT/KYC-Platform data (analysis).

**Comps & multiples.** No valuation/round/metrics in the item — it is a regulatory scheme, not a deal; trading multiples N/A ("no data"). Qualitative in-base comps (same fraud-data-sharing / registry theme):
- [[Plaid-Javelin report $38B lost to identity fraud in 2025]] — frames the loss pool antifraud sharing targets (US scale as reference, not comparable geo).
- [[Incognia launches AI Agent Detection for financial institutions]] — account/device-level fraud signals, the private-vendor analogue to platform-side account restriction.
- [[Pix adds dispute button against fraud in Brazil]] — a parallel state-rail antifraud mechanism (Brazil's Pix) showing the global pattern of payment/platform operators internalising fraud controls.
Distribution not computed (non-financial item); qualitative comparison only.

**Risk flags.**
1. **Unassigned liability / due-process gap.** The item itself flags that liability for platforms that receive a fraud signal but fail to act is undefined, and there is no stated lifecycle for a flag (assignment → contest → removal). Second-order: false positives can freeze legitimate users/sellers with no appeal, inviting FAS/consumer-rights backlash — note FAS is already scrutinising Wildberries/Ozon seller conditions (per www1.ru, Apr 2026).
2. **"Announced vs live" execution risk.** Mincifry says the exchange "is already launching" and needs no new law, but turning a formal data feed into a usable product (how a platform must react, status lifecycle) is explicitly unsettled. Second-order: a formal-but-inert exchange produces compliance theatre without loss reduction.
3. **Concentration / state-single-point dependence.** The scheme centralises on state-run rails (CBR, Gosuslugi, Mincifry); platforms depend on signal quality they cannot audit. Second-order: errors or scope-creep (e.g. the "next scenario" — data on the deceased) propagate instantly across all connected platforms, and the same channel could be repurposed beyond antifraud.

**What this changes (idea-lens).** This shifts the Russian fraud perimeter from the bank transaction to the cross-platform account graph — if it works, marketplaces and digital services effectively inherit bank-grade KYC/risk signals for free, raising the cost of account-farming for fraudsters (analysis). Falsifiable thesis: a working exchange should show a measurable drop in platform-account-based fraud within ~2–4 quarters of go-live. Watch for: (a) a published flag lifecycle + platform-liability rule, (b) the deceased-persons data extension actually shipping, (c) "Antifraud 3.0" passage in the Duma this autumn. What breaks the thesis: it stays a formal feed with no platform-action mandate or liability, i.e. data flows but nothing is restricted.

Sources: https://en.iz.ru/en/1841157/2025-02-18/fraudsters-stole-27-billion-rubles-russians-2024 · https://tass.com/economy/1974997 · https://www.cbr.ru/eng/press/event/?id=28094 · https://www.cbr.ru/eng/press/event/?id=27992 · https://www.cbr.ru/eng/information_security/fincert/ · https://www.cbr.ru/eng/counteraction_m_ter/ · https://en.iz.ru/en/2173935/2026-09-26/interior-ministry-announced-its-intention-introduce-draft-law-anti-fraud-30-state-duma-fall · https://www1.ru/en/news/2026/10/01/krasnaia-knopka-dlia-zashhity-ot-mosennikov-poiavitsia-na-gosuslugax-do-konca-goda.html · https://en.iz.ru/en/1913710/maria-frolova/find-out-voice-database-biometric-data-scammers-will-appear-russia · https://www.themoscowtimes.com/2025/10/21/russia-creates-database-to-track-and-block-cybercriminals-a90883
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
