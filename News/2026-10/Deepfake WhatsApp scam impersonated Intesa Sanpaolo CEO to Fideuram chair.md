---
title: "Deepfake WhatsApp scam impersonated Intesa Sanpaolo CEO to Fideuram chair"
date: 2026-10-27
retrieved: 2026-10-28
tags:
  - company/intesa-sanpaolo
  - industry/fraud-risk
  - industry/banking
  - region/europe
  - type/commentary
sources:
  - https://www.reuters.com/legal/government/ai-messaging-scam-costs-italys-top-bank-intesa-millions-sources-say-2026-09-25
  - https://cybernews.com/news/ai-voice-scam-hits-italian-bank-for-95-million
status: published
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s1931f10e
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Deepfake WhatsApp scam impersonated Intesa Sanpaolo CEO to Fideuram chair

> [!info] 2026-10-27 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] In February, Paolo Molesini, then chair of Fideuram, Intesa Sanpaolo's private banking arm, got a WhatsApp message that appeared to come from Intesa CEO Carlo Messina. It asked for urgent help with an overseas transaction. A follow-up call used an AI-cloned voice of Paolo Nastasi, managing partner of A&O Shearman Italy, who had nothing to do with it. Molesini had finance send roughly €95 million ($108 million) to accounts mainly in China and Hong Kong, Reuters reported. Cooperation between authorities in China, Portugal and Italy clawed back more than half. About €36 million is still missing, some of it already converted to crypto (AKA - it’s gone).

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.reuters.com/legal/government/ai-messaging-scam-costs-italys-top-bank-intesa-millions-sources-say-2026-09-25>
- <https://cybernews.com/news/ai-voice-scam-hits-italian-bank-for-95-million>

## Контекст

<!-- enrichment:context -->
**[0] What happened.** In February 2026, Paolo Molesini — then chairman of Fideuram, the private-banking arm of Intesa Sanpaolo (Italy's largest bank) — received a WhatsApp message spoofing Intesa CEO Carlo Messina, asking for urgent help with a confidential overseas transaction. A follow-up phone call used an AI-cloned voice of Paolo Nastasi, managing partner of A&O Shearman Italy, who had nothing to do with the matter, to "confirm" the request. Molesini had Fideuram's finance function wire roughly €95 million ($108M) in a series of transfers to accounts mainly in China and Hong Kong. Fideuram detected the irregularity quickly and alerted authorities; cross-border cooperation among Italy, China and Portugal clawed back ~€53M, but ~€36M remains missing, some already converted to crypto. Milan prosecutors are investigating a foreign national living outside the EU for computer fraud. The story surfaced publicly via Reuters on 2026-09-25 and was picked up by This Week in Fintech. (Sources: [Reuters via Euronext](https://live.euronext.com/en/financial-news/ai-messaging-scam-costs-italys-top-bank-intesa-millions-sources-say), [Cybernews](https://cybernews.com/news/ai-voice-scam-hits-italian-bank-for-95-million/), [AML Intelligence](https://www.amlintelligence.com/2026/09/news-ai-messaging-scam-costs-italys-top-bank-intesa-millions-sources-say/))

**[1] Why it matters.** This is one of the largest confirmed deepfake-enabled business-email-compromise (BEC) losses at a European bank to date — and the victim was itself a Tier-1 financial institution, not a corporate treasury. It combines three attack primitives: (a) a spoofed-messenger "CEO fraud" lure over WhatsApp, (b) AI voice cloning of a named outside counsel to add a trusted third-party "confirmation," and (c) rapid laundering through China/Hong Kong corridors and crypto off-ramps. It validates the thesis that voice/video deepfakes have moved from novelty to an operational fraud tool causing nine-figure losses, and it lands squarely in the fraud-risk / payment-authorization-controls debate that vendors like Sardine, Persona, LexisNexis/IDVerse and FinCEN alerts have been flagging. See [[Sam Altman warns of impending AI-driven bank fraud crisis]] and [[Brainfood Regula's 2025 identity fraud by the numbers]].

**[2] Precedent / pattern — this is not isolated.** Italy specifically has become a repeated deepfake-voice target:
- **2024 Ferrari (attempt, foiled).** An unnamed Ferrari executive received WhatsApp messages and a deepfaked voice call impersonating CEO Benedetto Vigna pushing a confidential acquisition. The exec defeated it by asking a question only the real Vigna could answer (the title of a book Vigna had recently recommended); the caller hung up. No money lost. ([Bloomberg](https://www.bloomberg.com/news/articles/2024-07-26/ferrari-narrowly-dodges-deepfake-scam-simulating-deal-hungry-ceo))
- **Feb 2025 fake-Defence-Minister scam.** Fraudsters cloned the voice of Italian Defence Minister Guido Crosetto and "his staff" to ask tycoons (Armani, Prada's Bertelli, Pirelli's Tronchetti Provera, Massimo Moratti) to wire ransom money for "kidnapped journalists." Only Moratti is confirmed to have paid — ~€1M to accounts in the Netherlands and Hong Kong — before realising the fraud. ([Bloomberg](https://www.bloomberg.com/news/articles/2025-02-09/italian-elite-targeted-by-scammers-using-ai-voice-impersonation), [Identity Week](https://identityweek.net/audio-deepfakes-imitate-italian-defence-minister-guido-crosetto-2/))

The Intesa case is the pattern's escalation: same playbook (urgent confidential wire, spoofed authority figure, overseas accounts incl. Hong Kong), but ~100x the loss of the Moratti case and executed against a bank's own private-banking arm.

**[3] Mechanism / controls angle.** The loss did not stem from a technical breach of Intesa's systems — it was authorization-process failure: a single senior principal (the chairman) authorized out-of-band wires on the strength of a messaging app and a voice call, apparently bypassing standard multi-party / call-back verification for large cross-border transfers. The relevant defenses are behavioral and procedural: payment-anomaly detection against historical baselines (the kind Sardine describes for link-less, domain-less social-engineering fraud — [[Fintech Wrap Up Sardine on live agentic fraud attacks]]), mandatory independent call-back on a known number for high-value wires, and dual authorization that cannot be collapsed by a single executive. FinCEN's 2026 alert on deepfake-media fraud targeting financial institutions is directly on point ([[The article also notes that ID cards are abused more frequently than]]).

**[4] Open threads / what to watch.**
- Whether the remaining ~€36M (crypto-converted) is recoverable — treat as likely gone.
- Attribution: Milan prosecutors naming/charging the non-EU suspect; whether an organized group vs. a single actor.
- Governance fallout: Molesini resigned in March 2026 ("personal reasons" at the time); reporting says neither he nor other Fideuram execs are under investigation — watch for any regulatory (Bank of Italy / ECB) review of Intesa's payment controls.
- Sector response: expect renewed vendor positioning (deepfake-detection, payment-verification) and possibly supervisory guidance on voice-cloning risk in high-value wire authorization.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team / challenge**

1. **Is the €95M figure confirmed or "sources say"?** Partially open. Reporting originates from Reuters citing unnamed sources (2026-09-25); Intesa/Fideuram have not published an official loss figure. €95M (~$108M) is consistently repeated across Reuters, Cybernews, Bloomberg-adjacent outlets — treat as credible but unaudited.

2. **Was there really a loss, or was it fully recovered?** Loss confirmed. ~€53M clawed back via Italy/China/Portugal cooperation; ~€36M still missing, partly crypto-converted. Net realized loss is material even after recovery.

3. **Is this the same incident as any prior note in the DB?** No. Internal semantic search surfaced only thematic neighbors (Sardine agentic fraud, Sam Altman AI-fraud warning, Regula/Persona/LexisNexis fraud content, FinCEN deepfake alert, deepidv). None describe the Intesa/Fideuram February-2026 incident. Verdict: FRESH.

4. **Is it the same as the Ferrari (2024) or Crosetto (2025) cases?** No — distinct incidents, different victims, different years. They are precedent/pattern, not duplicates. Ferrari was a foiled attempt (no loss); Crosetto netted ~€1M from one victim (Moratti).

5. **Did the attackers breach Intesa's IT systems?** No evidence of a systems breach. This was social engineering / authorization-process failure, not a technical intrusion. (Distinguishes it from, e.g., the bank's separate Google Cloud migration news — unrelated.)

6. **Why would a bank chairman personally authorize €95M on a WhatsApp message?** Open/behavioral. Reporting implies the confidential "overseas transaction" framing plus a cloned voice of a known outside lawyer defeated skepticism; it exposes that call-back / dual-auth controls were either absent or overridden at the top. This is the core governance question.

7. **Is the voice-clone of A&O Shearman's Paolo Nastasi corroborated?** Reported consistently (Reuters-sourced); Nastasi is described as uninvolved and his voice cloned. Not independently verifiable from public filings — accept as reported.

8. **Could the "deepfake" framing be overstated (i.e. just spoofing + impersonation)?** Partially. The WhatsApp side is spoofing/impersonation; the AI element is specifically the cloned voice on the confirmation call. "Deepfake" here = audio voice clone, not video. The note should not imply video deepfakes.

9. **How much is this an Intesa-specific failure vs. an industry-wide exposure?** Industry-wide. The pattern (Ferrari, Crosetto, FinCEN alert, Sardine/Persona commentary) shows voice-cloning BEC is a sector risk; Intesa is the largest confirmed loss, not an outlier in method.

10. **Is there a fintech/vendor angle worth the DB's attention?** Yes — payment-anomaly detection, deepfake-voice detection, and wire-verification controls. Directly relevant to Sardine, LexisNexis/IDVerse, Persona, deepidv, Regula coverage already in the DB.

11. **Timeline consistency?** Consistent: incident Feb 2026 → Molesini resigns Mar 2026 → public reporting Sep 2026 → TWIF pickup Oct 2026. The ~7-month gap between incident and disclosure is itself notable (quiet handling).

12. **Regulatory/supervisory consequence?** Open. No confirmed Bank of Italy / ECB action yet; reporting says execs not under investigation. Watch for supervisory review of large-wire controls.

13. **Recovery credibility — is €53M really back?** Reported via cross-border law-enforcement cooperation; plausible given rapid detection and fast freezing in China/HK/Portugal corridors. The crypto-converted ~€36M is realistically unrecoverable.

14. **Attribution risk.** One non-EU suspect under investigation by Milan prosecutors for computer fraud; no charge/conviction confirmed. Do not assert a named perpetrator.

15. **Does the note's headline accurately match the body?** Yes — "Deepfake WhatsApp scam impersonated Intesa Sanpaolo CEO to Fideuram chair" correctly: CEO (Messina) impersonated on WhatsApp to Fideuram chair (Molesini), with voice-clone confirmation. No entity cross-wiring detected.

**Importance: 4/5** — Largest confirmed deepfake-enabled nine-figure loss at a European Tier-1 bank; strong signal for the AI-fraud / payment-controls thesis and well-connected to existing fraud-risk coverage. Not a 5 because it's an isolated incident with no business-model or market-structure shift, and core figures remain "sources say" rather than officially confirmed.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
Опубликовано в дайджесте [[digest/2026-10-28]] (2026-10-28).
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits in deepfake / social-engineering fraud — an exec-impersonation (CEO-fraud / BEC-successor) loss event, not a product or deal. Sector sizing is for the *defensive* layer: the deepfake-detection market is ~$990m in 2026 on one estimate, with software-only estimates nearer ~$543m, projected to ~$3.28bn by 2033 (~29% CAGR) (per Meticulous Research / openPR syndicated reports, as of 2026 — vendor-commissioned, treat as directional). On the *loss* side, cumulative reported deepfake-fraud losses reached ~$3.7bn through mid-2026, ~89% of it in the prior 18 months, with the US alone ~$712m and ~43% of US losses hitting the corporate sector via executive-impersonation transfer requests (per brside.com / netarx.com citing industry trackers, as of 2026 — only publicly-reported incidents counted, so a floor). Why now: 3 seconds of public audio yields an ~85% voice match with free tools (per cybelangel.com, 2026) — every earnings call / conference clip is attack material. The €95m ($108m) Fideuram loss is likely one of the largest known single deepfake cases globally (per trendingtopics.eu / Reuters, 2026-09).

**Competitive landscape.** The sector KPIs that matter here are detection-side: liveness/anti-spoof pass rate, synthetic-voice detection accuracy, and — on the bank-process side — call-back / dual-authorisation adherence and IBAN-name-match coverage. Vendor landscape splits into (1) voice/audio specialists (Pindrop — incumbent in call-centre fraud scoring for banking/insurance), (2) multimodal detection (Reality Defender — named a Gartner "Market Shaper" June 2026; Hive; Sensity), and (3) identity/liveness (Jumio, Sumsub, Persona). Basis of competition: detection accuracy + integration into existing KYC/payment flows, not price. Recent in-base moves: [[Jumio rolls out Advanced Liveness Detection against deepfakes]] (2025-06), [[deepidv closes $1 million seed, launches AI fraud suite]] (2026-03, deepfake + synthetic-media detection), [[Falkin raises funding for AI scam prevention]] (2025-11, targeting the emotional-manipulation gap before money moves), [[Fintech Wrap Up Sardine on live agentic fraud attacks]] (2026-03, argues link-less impersonation needs transactional-expectation modelling, not URL/domain signals). Intesa's position here is the *victim*, not a player: a €95m loss despite being Italy's largest bank is the tell that process controls (not just tooling) failed — the request bypassed call-back and dual-auth via a cloned-voice "confirmation" from a fake external lawyer (analysis).

**Comps & multiples.** No deal/valuation/round attaches to the protagonist — Intesa is a listed incumbent and this is a loss event, so EV/Revenue, P/E etc. are **not applicable** here. Loss-magnitude comps instead: Arup (~$25m deepfake video-call transfer, 2024) and a Fortune-500 early-2026 case (~$28m) (per securitytoday.de / brside.com, 2026); average single deepfake-fraud incident ~$500k, financial-services firms >$600k (per 2026 industry surveys via brside.com). Against those, Fideuram's €95m is a ~3–4x step-change over the prior largest-known cases — an outlier that resets the "max single loss" range for the category. Internal loss/recovery arithmetic from the note: €95m sent → ~€53m clawed back (China/Portugal/Italy cooperation) → ~€36m still missing, part already converted to crypto (per Reuters / cybernews, 2026). Recovery rate ≈ €53m / €95m ≈ 56%. Detection-market multiples: no clean public EV/Revenue for the named private vendors → [UNSOURCED].

**Risk flags.**
- **Fraud-liability re-pricing (regulatory).** PSD3/PSR will make PSPs liable for reimbursement in *bank-impersonation* APP scams, with directly-applicable PSR fraud-liability rules landing ~H2 2027 and mandatory IBAN-name matching (per Norton Rose / MoFo, 2026). Second-order: losses like this shift from "operational write-off" to balance-sheet liability for banks that under-invest in detection — raising the ROI on Pindrop/Reality-Defender-class tooling.
- **Process > tooling single point of failure.** The loss ran through a *person* (chairman) authorising outside normal controls, not a system breach — so detection vendors can't fully remediate it. Concentration risk: one senior approver able to override call-back/dual-auth is the real exposure (analysis).
- **Crypto off-ramp = terminal loss.** ~€36m converted to crypto is effectively unrecoverable ("it's gone"); the ~56% clawback depended on cross-border (China/HK) cooperation that won't generalise, so expected recovery on future cases is lower (analysis).

**What this changes (idea-lens).** A €95m single loss at Europe's largest bank is a re-rating catalyst for the deepfake-detection sector: it converts exec-impersonation from a tail-risk talking point into a board-level capex line, especially ahead of PSD3 liability. Falsifiable thesis: detection/anti-spoof vendors (voice-biometric and multimodal) should see accelerating bank-procurement cycles into 2027; what would break it — if post-mortems conclude the fix is *procedural* (hard call-back + payee verification) rather than *technological*, spend flows to process/consulting, not detection SaaS (analysis).

Sources: https://www.reuters.com/legal/government/ai-messaging-scam-costs-italys-top-bank-intesa-millions-sources-say-2026-09-25 · https://www.trendingtopics.eu/intesa-sanpaolo-deepfake-95-million/ · https://www.brside.com/blog/deepfake-fraud-losses-2026 · https://www.netarx.com/blog/deepfake-statistics-2026 · https://cybelangel.com/blog/deepfake-ceo-fraud-how-voice-cloning-targets-us-executives/ · https://www.meticulousresearch.com/product/deepfake-detection-market-6944 · https://www.openpr.com/news/4637375/deepfake-detection-software-market-to-reach-us-3-28-billion · https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
