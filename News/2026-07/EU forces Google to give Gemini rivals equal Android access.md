---
title: "EU forces Google to give Gemini rivals equal Android access"
date: 2026-07-16
retrieved: 2026-07-16
tags:
  - company/google
  - industry/ai
  - region/europe
  - type/regulation
sources:
  - https://www.bloomberg.com/news/articles/2026-07-16/google-must-give-gemini-rivals-equal-access-to-android-system-eu-says
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: sbf2b2d2a
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# EU forces Google to give Gemini rivals equal Android access

> [!info] 2026-07-16 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] Bloomberg: ЕС обязал Google предоставить конкурентам Gemini равный доступ к системе Android

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.bloomberg.com/news/articles/2026-07-16/google-must-give-gemini-rivals-equal-access-to-android-system-eu-says>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: EU forces Google to give Gemini rivals equal Android access
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
On **2026-07-16** the European Commission adopted a **final, legally binding DMA "specification decision" under Article 6(7)** (interoperability obligation), case **DMA.100220**, requiring Google to give rival AI assistants "free and effective interoperability" with the same Android hardware/software features Gemini uses. A parallel decision (**DMA.100209**, Article 6(11) FRAND search-data access) forces Google to share search-ranking/click data with rival search & AI-search providers.

De-PR the Bloomberg "forces" frame — three caveats matter:
- This is a **specification of an existing gatekeeper obligation, NOT a fine or a non-compliance ruling.** No money changes hands here. "Specification proceedings are not non-compliance investigations" (EC).
- **Effects are delayed to 2027:** search-data sharing starts **1 Jan 2027**; Android interoperability lands with the next Android release around **July 2027**.
- It is a binding administrative act but still **subject to judicial review** at the EU General Court. The consultation phase is already closed (measures sent 27 Apr 2026; consultation ended 13 May 2026), so "still open to consultation" would be wrong.

**Why structured this way (analysis):** the Commission chose the Article 6(7) *specification* route rather than a fresh antitrust case or a fine because Android is already a designated Core Platform Service and Alphabet a designated gatekeeper — so the obligation already exists; the Commission is only *writing the rulebook* for how it applies to the AI-assistant layer. This is faster and harder to litigate than a de-novo abuse case, and it pre-positions any future breach for the DMA fine regime (up to 10% of global turnover, ~$35bn on Alphabet; 20% repeat).

Concretely, "equal access" spans ~**11 Android features** in four layers: (1) **invocation** — custom wake words at parity with "Hey Google" + system entry points (long-press home) so a rival can BE the assistant; (2) **context** — on-screen content and on-device context Gemini reads, proactive suggestions; (3) **agentic action** — control installed apps and OS settings, execute cross-app tasks (book a taxi/restaurant, suggest replies); (4) **resource access** — hardware/model parity so rivals are as responsive as Gemini. Google may vet services for safety/security.

## [1] Competitors / peers
Named beneficiaries: **OpenAI (ChatGPT), Anthropic (Claude), Perplexity, Mistral (Le Chat)**, plus rival search/AI-search engines on the data leg. No single complainant is identifiable — this appears **Commission-initiated**, not complaint-driven (unverified who, if anyone, lodged it).

Regulatory prior art (dated): **2018 Google Android** case, €4.34bn fine (cut to €4.1bn in 2022), whose **final appeal was dismissed by the CJEU ~2-3 July 2026** — days before this decision, removing Google's last defense and producing today's browser/search choice screens. **Google Shopping (2017, €2.42bn)** established the self-preferencing theory. A separate **DMA Search self-preferencing + Google Play non-compliance case** (preliminary findings 19 Mar 2025) is reportedly nearing a record DMA fine (high triple-digit-million €, exceeding Apple's €200m April 2025 App Store penalty) — that is the *fine-bearing* case, distinct from today's specification.

**Why this matters (analysis):** the beneficiaries are the exact set fighting Google for the **consumer-AI default** — the single most valuable distribution real estate in AI. Being invocable by wake word and set as system assistant on Android (~70%+ global mobile share) is worth more than any model benchmark. The EU is manufacturing a distribution on-ramp OpenAI/Anthropic/Perplexity cannot buy at any price in the US.

## [2] Company / context fit
This is the AI-era extension of a decade-long EU theory: *Google leverages Android to entrench its own service* — now Gemini instead of Search/Chrome. It fits the DMA's structural logic (pre-emptive, obligation-based, no need to prove harm case-by-case). Google's public pushback leans on privacy/security ("exposing Europeans' private searches to unfamiliar companies") — the same guardrail argument Apple used against DMA sideloading/interoperability, and a preview of the compliance-friction Google will use to slow real 2027 access.

## [3] Novelty / value-add / traction
Genuinely **new**: first DMA Article 6(7) interoperability specification applied to the **AI-assistant layer** of a dominant mobile OS. But **traction is zero today** — nothing is live; obligations bite in 2027, and history (2018 choice screens took years and delivered muted share shifts to Google's rivals) says implementation friction will blunt the win. Announced ≠ adopted.

**Who captures the margin (analysis):** even if a rival becomes the default Android assistant, the **agentic-payments rails sit with Visa/Mastercard/PayPal**, and the merchant/catalog integrations sit with the likes of PayPal-Perplexity (see [[PayPal and Perplexity launch instant buy for Black Friday]]) and are actively contested by incumbents (see [[Amazon sues Perplexity over agentic shopping tool]]). So EU-mandated Android access decides *who talks to the user*, not *who captures the transaction economics* when the assistant "books a taxi and pays". The central question shifts from "can rivals reach the phone" to "who monetizes the agentic action once they're there".

## [4] What's next / market sentiment
Timeline: data-sharing 1 Jan 2027, Android interoperability ~July 2027; judicial review possible but not confirmed as of 2026-07-16. Sentiment: framed as a major precedent and a template the EU can reuse against Apple's assistant/OS layer. Fintech angle: this is upstream plumbing for **agentic commerce** — whoever wins the assistant slot becomes the front door for on-device "book & pay" flows, making the payments-rail and merchant-catalog control (Visa/MA/PayPal/Amazon) the real second-order battleground.

**Counterintuitive second-order (hypothesis):** forcing open the assistant layer may *commoditize* the assistant and push the durable margin down into the agentic-payment and merchant-integration layer — meaning the EU decision helps model labs reach users but hands pricing power to the rails, not the models.

## Sources
See challenge file + column-two dump. Primary: EC DMA.100220 / DMA.100209; Bloomberg (headline), CNBC, Fortune, EC press corner IP_26_202.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Top challenge / red-team questions

1. **Fine or no fine?** — Answered: **no fine.** This is an Article 6(7) *specification decision* (DMA.100220), not a non-compliance ruling. Bloomberg's "forces" is technically correct but no penalty attaches. Future breach → up to 10% (20% repeat) of global turnover, ~$35bn on Alphabet — contingent, not applied.
2. **Binding or preliminary?** — Answered: **final and binding** as an administrative act (adopted 16 Jul 2026, ahead of 27 Jul statutory deadline). Consultation closed 13 May 2026. Subject to judicial review at the General Court.
3. **When does anything actually change?** — Answered: **2027.** Search-data sharing 1 Jan 2027; Android interoperability ~July 2027 (next Android release). Nothing is live now.
4. **What does "equal access" concretely include?** — Answered: ~11 features in 4 layers — invocation (wake word/entry points), context (on-screen/on-device data), agentic action (app + OS control), resource/model parity. Enumerated 11-feature primary list not fully verified.
5. **Who benefits?** — Answered: OpenAI, Anthropic, Perplexity, Mistral + rival search engines (data leg). No named complainant; appears Commission-initiated (open).
6. **Is this a new case or repackaging the 2018 Android case?** — Answered: **new instrument** (DMA, not 2018 antitrust). But same theory of harm (Android leverage), and CJEU dismissed the 2018 appeal ~2-3 Jul 2026, clearing the runway.
7. **Will it move share, or be another muted choice-screen?** — Open/skeptical: 2018-mandated browser/search choice screens delivered limited rival share gains; implementation friction (Google's "safety vetting") likely blunts impact. (analysis)
8. **Does Android access = capturing value?** — Answered (analysis): **No.** Agentic-payment rails (Visa/MA/PayPal) and merchant catalogs sit outside; access decides who talks to the user, not who monetizes the transaction.
9. **Will Google appeal?** — Open: public criticism confirmed (privacy/security); no formal appeal announced as of 2026-07-16.
10. **Why the specification route vs a fine?** — Answered (analysis): Android already a designated CPS; specification is faster, litigation-resistant, and pre-loads the fine regime for future breach.
11. **Does the fintech angle survive?** — Answered: yes via agentic commerce — the assistant is the front door for on-device "book & pay"; connects to [[Amazon sues Perplexity over agentic shopping tool]] and [[PayPal and Perplexity launch instant buy for Black Friday]].
12. **Is the search-data leg (DMA.100209) bigger than the assistant leg?** — Open: FRAND search-data access could matter more for AI-search quality (Perplexity, OpenAI) than assistant slots; under-covered in the headline.
13. **Freshness/duplicate?** — No prior corpus note covers this event; the closest notes are agentic-commerce (different companies/topic). **Fresh, standalone.**
14. **Precedent for Apple?** — Answered (analysis): reusable DMA template against Apple's Siri/OS assistant layer; strategic, not just Google-specific.
15. **Second-order risk to the beneficiaries?** — Hypothesis: forced-open assistant layer may commoditize the assistant and push durable margin to the payment rails, helping model labs reach users but not capture economics.

**FRESHNESS / DUPLICATE VERDICT:** **FRESH.** First corpus coverage of the EU DMA.100220/100209 decision; no duplicate. Related but distinct: [[Amazon sues Perplexity over agentic shopping tool]], [[PayPal and Perplexity launch instant buy for Black Friday]].

**Importance: 4/5** — Major regulatory precedent: first DMA interoperability specification applied to the AI-assistant layer of the dominant mobile OS, directly benefiting OpenAI/Anthropic/Perplexity/Mistral and reshaping the consumer-AI distribution + agentic-commerce battleground relevant to fintech payments. Not 5 because no fine attaches, real effects are delayed to 2027, and judicial review remains open.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits at the intersection of EU platform regulation (DMA) and AI-assistant distribution on mobile. The action is a July 2026 binding DMA specification decision (case DMA.100220) forcing Google to open ~11 Android system-level integration points (voice activation, agentic cross-app actions, hardware access) to rival AI assistants, and to share Search query data with rival engines from January 2027; Android changes reach users progressively from July 2027 (per CNBC / Bloomberg / eweek, 2026-07-16). Drivers / "why now": (1) mobile is the primary AI-assistant distribution channel and system-level integration (the "Hey Google" default) is the key barrier to entry — regulators are treating the OS assistant layer as a bottleneck the way browser defaults were treated in the 2010s; (2) DMA moves from fining to prescriptive behavioral remedies (interoperability mandates), following the 2026 Search self-preferencing case. Barriers here are regulatory + platform gatekeeping, not capital — the whole point of the remedy is to lower a distribution barrier that money alone could not clear.

**Competitive landscape.** KPIs that matter here: assistant default/attach rate on the ~mobile install base, voice-invocation share, and data access parity for search. Who gains distribution: OpenAI (ChatGPT), Anthropic (Claude), Perplexity, Mistral (Le Chat) — all named as beneficiaries that could integrate "as deeply as only Gemini can today" (per TheNextWeb, ICLE, 2026-07). Basis of competition shifts from pure model quality toward distribution + data access. Recent DMA cadence: Search self-preferencing fine (high-triple-digit-€m, expected pre-August recess 2026); an EU court ruling (2026-07-09) reportedly gave Google ~18 days and blocked a last legal defense, forcing the July 27 specification. Protagonist's position: Google/Gemini remains the default incumbent on Android with an installed-base moat — the remedy is designed to erode exactly that moat, but only in the EU and only from mid-2027, so near-term Gemini distribution is largely intact (analysis).

**Comps & multiples.** This is a regulatory action, not a deal — no transaction multiple. IR grounding (Alphabet, IR-covered, GOOGL): latest reported quarter Q1 2026 total revenue $109.9bn (+22% YoY); Google advertising $77.25bn of which Search & other $60.4bn; Google Cloud $20.03bn (+63% YoY) (per 9to5Google / Yahoo, 2026-04-29). The EU-Search-data-sharing remedy touches the ~$60bn/quarter Search franchise, but only EU-scoped and gradually — no quantified revenue-at-risk is disclosed, so impact = "no data". DMA fine ceiling for reference: 4–20% of global annual turnover (per CSIS). Internal comps (base): [[EU orders Meta to make Instagram, Facebook less addictive]] (same-week DMA/EU behavioral remedy on a US platform), [[EU to exclude Big Tech from financial data-sharing system]], [[Trump threatens 100% tariffs over foreign digital services taxes]] (US–EU regulatory friction). External precedent penalties: Apple €500m (App Store anti-steering), Meta €200m ("pay or consent") — behavioral, not structural (per cybersecuritynews, 2026).

**Risk flags.** (1) *Enforcement/appeal uncertainty* — a July 27 specification can still be litigated; the 2026-07-09 court ruling narrowed but did not end Google's legal options, and behavioral DMA remedies have historically produced slow, contested compliance (why: mandated timeline slips to July 2027, real-world assistant switching may lag years). (2) *Limited behavioral impact* — like browser choice screens, opening the integration layer does not guarantee users switch defaults; Gemini keeps the "Hey Google" muscle memory and pre-install, so rivals gain the right to compete but not demand (why: distribution parity ≠ share shift). (3) *US–EU friction / geographic containment* — remedy is EU-only against a US gatekeeper amid active digital-services-tax / tariff tensions ([[Trump threatens 100% tariffs over foreign digital services taxes]]); Google may minimize spillover, and retaliation risk could dilute or delay enforcement (why: the "Brussels effect" template is a hypothesis, not a guarantee).

**What this changes (idea-lens).** For AI assistants, the OS layer becomes contestable in the EU — a re-rating of distribution risk for challengers (OpenAI/Anthropic/Perplexity) who have models but lacked system-level reach (analysis). Falsifiable thesis: if the July 27 spec holds and Android exposes voice + agentic hooks in 2027, watch for rival assistants shipping as system defaults on EU Android and Gemini's EU voice-invocation share declining. What breaks the thesis: a successful appeal, a watered-down specification, or (as with browser choice) users simply keeping the default — in which case the remedy is symbolic and Gemini's mobile moat survives.

Sources: https://www.bloomberg.com/news/articles/2026-07-16/google-must-give-gemini-rivals-equal-access-to-android-system-eu-says · https://www.cnbc.com/2026/07/16/google-required-to-open-up-to-ai-search-engine-rivals-under-eu-mandated-changes.html · https://thenextweb.com/news/google-eu-android-gemini-rivals-dma · https://laweconcenter.org/resources/integrating-ai-assistants-and-agents-competition-policy-in-dynamic-markets/ · https://cybersecuritynews.com/record-dma-fine-against-google/ · https://9to5google.com/2026/04/29/alphabet-q1-2026-earnings/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
