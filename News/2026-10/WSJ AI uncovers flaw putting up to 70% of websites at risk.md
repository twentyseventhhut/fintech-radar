---
title: "WSJ: AI uncovers flaw putting up to 70% of websites at risk"
date: 2026-10-21
retrieved: 2026-10-21
tags:
  - industry/fraud-risk
  - industry/ai
  - region/global
  - type/outage-security
sources:
  - https://www.wsj.com/tech/cybersecurity/ai-just-found-a-bug-that-puts-up-to-70-of-the-worlds-websites-at-risk-fd0902ea
status: enriched
n_mentions: 1
channels:
  - "42 секунды"
story_id: sff7aa98a
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# WSJ: AI uncovers flaw putting up to 70% of websites at risk

> [!info] 2026-10-21 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: 42 секунды

## Агрегированный текст (из дайджестов)

[42 секунды] WSJ: ИИ обнаружил ошибку, которая подвергает риску до 70% всех веб-сайтов

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.wsj.com/tech/cybersecurity/ai-just-found-a-bug-that-puts-up-to-70-of-the-worlds-websites-at-risk-fd0902ea>

## Контекст

<!-- enrichment:context -->
## [0] What happened
On 2026-10-21 the WSJ (exclusively) and most major outlets reported that AI tools helped uncover **PHP2Shell** — a pair of critical, unauthenticated remote-code-execution (RCE) vulnerabilities in the PHP engine itself (**CVE-2026-109618** and **CVE-2026-109619**). PHP is the server-side language running roughly **70% of the world's websites/web apps** (the basis for the "70% of websites at risk" headline — it is a measure of PHP's web footprint, not that 70% are confirmed-exploitable). PHP shipped emergency patches the same day (8.5.12, 8.4.27, 8.3.36, 8.2.35); PHP 5/7 remain unpatched. The bug class had reportedly been latent in PHP for ~14 years (back to 5.4).

## [1] The technical substance (skeptical read)
- Both CVEs are **memory-safety / uninitialized-pointer flaws (CWE-824)** tied to PHP aborting request processing via `longjmp()` after out-of-memory or fatal errors, leaving request/global state in an unsafe condition (areas cited: session handling, OPcache class caching, fatal-error backtrace generation).
- Trigger is reportedly in **multipart/form-data parsing / session upload-progress**, i.e. **before application code runs** — so WAFs, auth layers, CMS maintenance modes and clean app code do **not** protect you until PHP itself is patched. This is what makes it broad.
- Severity: PHP devs rate CVSS v4.0 **9.2 (Critical)**; watchTowr rates it **10.0**. Outcome = unauthenticated RCE + memory disclosure (passwords/secrets) — this is the credible, verifiable part. The "could take down 70% of the internet" framing is headline amplification, not a disclosed impact assessment.

## [2] Who/what found it — the "AI discovered it" claim
Three parties independently/collaboratively: a firm reported as **Calif** (first issue, 2026-08-01, using OpenAI **GPT-5.6 "Sol"**), **OpenAI** (found a fuller version in Sept using its own models), and Google-owned **Wiz** (independently found both, using Google **Gemini 4 "Argon"**, Wiz Atlas and GPT-5.6 Sol). Wiz and Imperva/Sansec/Cloudflare published technical write-ups. Caveat: AI accelerated discovery (hours vs. manual weeks), but humans validated/triaged — "AI found it" is partly vendor/AI-lab marketing. Note our news DB has NO Anthropic/Claude involvement reported here; attribution is to OpenAI + Google models.

## [3] Fintech / payments relevance (why this is in Radar)
PHP underpins a large share of **e-commerce and payment-adjacent stacks**: Magento 2 / Adobe Commerce, WooCommerce, Shopware, WordPress, and countless merchant checkout, billing and KYC portals. Because the flaw is in the engine, these stores are exposed **even with clean plugin code**. Researchers confirmed unauthenticated RCE against Magento 2.4.9 and ~10 other PHP apps. For payments the exposure is card-data/PII theft, credential harvesting and checkout-page tampering (Magecart-style skimming) on unpatched hosts — a PCI-DSS and merchant-fraud risk, not a card-network protocol flaw.

## [4] Status / exploitation
Active exploitation attempts began **at scale ~11:35 UTC on 2026-10-21**, before/around public patch release (Cloudflare reported pre-disclosure probing and pushed temporary WAF rules; watchTowr and Hadrian report ongoing exploitation, largely via the session upload-progress path). The dynamic: patched PHP exists, but mass-patching millions of hosts (plus unpatched PHP 5/7) is a race against AI-assisted attackers. Comparisons to Log4Shell are being drawn by outlets.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team questions
1. **Does "70% of websites" = "70% at risk"?** No. 70% is PHP's share of the web (W3Techs-style footprint). Risk requires: PHP 5.4–8.x on the server, reachable multipart/session path, and no patch/WAF. Headline conflates footprint with exposure.
2. **Did "AI" really find it, or is this vendor/AI-lab PR?** Attribution is to OpenAI (GPT-5.6 "Sol") + Google (Gemini 4 "Argon")/Wiz — the same firms that benefit from "AI finds critical bugs" narratives. AI accelerated fuzzing/triage; humans still validated. Treat the "AI discovered" claim as substantially true but marketing-amplified.
3. **Is the fintech angle direct?** Indirect. This is NOT a payments-network/protocol flaw. It matters to fintech only via PHP-based merchant/e-commerce/portal stacks (Magento, WooCommerce) — a server-hardening + PCI issue, not a Visa/Mastercard/rails event.
4. **CVE/disclosure solid?** Yes — CVE-2026-109618 / 109619, CVSS 9.2 (watchTowr 10.0), patched 2026-10-21 (8.5.12/8.4.27/8.3.36/8.2.35). This is the hard, verifiable core.
5. **Novel vs. hype?** The AI-discovery framing and "most severe PHP flaw in a decade / Log4Shell comparison" are outlet narratives; the RCE itself is real and serious. Active exploitation is confirmed by multiple vendors.
6. **Any confirmed fintech breach from it yet?** No specific payments/fintech breach reported as of 2026-10-21 — exposure is potential, not realized in our sources.

### Importance: 3/5
Legitimately significant internet-wide RCE with confirmed active exploitation and a clean CVE/patch record, directly touching PHP-based payment/e-commerce stacks (PCI, Magecart risk). Capped at 3 for Fintech Radar because the fintech link is indirect (web-infra, not rails) and the "AI found it / 70% at risk" framing is partly hype — no confirmed fintech breach yet.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This sits in the AI-driven vulnerability discovery / application-security (AppSec) subsector of cybersecurity. Market sizing (secondary analyst reports, treat as indicative, not audited): the AI vulnerability-scanning segment is put at ~$3.6bn in 2026 growing ~17% CAGR (per TheBusinessResearchCompany, via GII Research, as of 2026); the broader AI-in-cybersecurity market at ~$25–44bn in 2026 depending on definition (MarketsandMarkets / Fortune Business Insights, 2026). The flaw itself — "PHP2Shell", two unauthenticated-RCE bugs CVE-2026-109618 / CVE-2026-109619, CVSS v4.0 9.2, present in PHP since v5.4 and disclosed/patched 21 Oct 2026 (PHP 8.5.12/8.4.27/8.3.36/8.2.35) — matters because PHP powers ~70% of websites, so the blast radius is horizontal, not vendor-specific. **Why now:** the discovery itself is the story — an AI security system surfaced a 14-year-old engine-level bug that researchers (Wiz) say humans likely would not have found, validating AI as a first-class vuln-discovery tool. The same capability is dual-use: the public fix hands attackers a template to reverse-engineer, triggering a "race to exploit."

**Competitive landscape.** AppSec KPIs the sector runs on: ARR, net revenue retention, and increasingly "vulns found / mean-time-to-remediate." Key players span cloud/code security (Wiz, Snyk, Checkmarx, Veracode, Socket) and the frontier-lab/AI-firm entrants now doing autonomous vuln research (OpenAI reportedly coordinated the disclosure coalition; the discovering AI security firm is reported variously as Calif (per WSJ/Fortune) or Wiz (per Wikipedia/Datadog) — attribution not yet settled, so treat as "an AI security firm," not confirmed). Basis of competition is shifting from signature/rule coverage toward AI depth-of-discovery and speed-to-patch orchestration. Recent moves: Google closed its ~$32bn ($29.5bn SEC-adjusted) acquisition of Wiz in Mar 2026; Cloudflare shipped WAF protections against PHP2Shell on disclosure day (21 Oct 2026). Positioning note for fintech: this is not about one protagonist company — the "loser" is any fintech/e-commerce stack on unpatched PHP (Magento 2.4.9 and 10+ PHP apps confirmed exploitable), and app-level auth does NOT help because PHP parses the malicious request before application code runs `(analysis)`.

**Comps & multiples.** No deal/valuation attaches to this news item itself, so this is a qualitative read on the surrounding AppSec names rather than a multiple on the protagonist (there is none).
- Wiz — Google acquisition ~$32bn headline / $29.5bn SEC-adjusted on >$1bn ARR ⇒ EV/ARR ≈ `$32bn / $1bn = 32x` (M&A multiple, not a trading comp; trophy cloud-security premium).
- Snyk — ~$7.4bn last private valuation (press, 2026); ARR not publicly verified ⇒ EV/Rev [UNSOURCED].
- Veracode — ~$2.5bn (TA Associates, 2022); private, stale ⇒ no current multiple.
- Internal comps: [[Socket raises $60 million Series C at $1 billion valuation]] (AI software-supply-chain security, $1bn, May 2026) and [[MagicCube raises $10 million to expand into biometrics and IDV]] (payment-security/AI-trust). Both are early-stage private rounds, not comparable in scale — distribution not computed, qualitative comparison only. Takeaway: AI-security assets command rich strategic multiples (Wiz 32x ARR) when they prove frontier capability, which is exactly what an AI-discovered engine-level bug advertises.

**Risk flags.**
1. **Horizontal attack-surface exposure for fintech.** PHP sits under Magento/WooCommerce/Shopware storefronts and many legacy banking/payment web apps; unauthenticated RCE below the app layer means PCI-DSS and app-level auth give no protection — second-order: card-data and payment-credential theft at checkout, plus incident-response/breach-notification cost.
2. **Race-to-exploit / patch-lag concentration.** The public fix is a reverse-engineering template; AI lowers attacker cost, so the window between disclosure (21 Oct) and mass exploitation is compressing — fintechs with slow patch cadence or unsupported PHP versions carry outsized tail risk.
3. **Attribution / hype uncertainty.** Discoverer credited inconsistently (Calif vs Wiz) and "70% of websites" is engine-prevalence, not confirmed-exploitable share — risk of overstatement; the investable signal (AI as vuln-discovery engine) is real, the single-event severity framing is partly PR `(analysis)`.

**What this changes (idea-lens).** `(analysis)` This is a capability-proof moment, not a single-company re-rating: AI-native vuln discovery just demonstrated it can find what humans miss at engine scale, which should pull spend toward AI-AppSec and raise strategic bids for frontier-capable security assets (Wiz-style premiums). Falsifiable thesis: if the next 2–3 high-severity CVEs are also AI-surfaced, expect accelerated M&A/funding in AI-security and a budget shift from signature-based scanners to AI discovery; trigger to watch — exploitation-in-the-wild volume for PHP2Shell and whether frontier labs formalize paid vuln-research offerings. What breaks the thesis: if PHP2Shell proves hard to weaponize at scale, the "AI changes security economics" narrative cools.

Sources: https://www.wsj.com/tech/cybersecurity/ai-just-found-a-bug-that-puts-up-to-70-of-the-worlds-websites-at-risk-fd0902ea · https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/ · https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/ · https://www.helpnetsecurity.com/2026/10/21/php2shell-php-vulnerabilities-patched-cve-2026-109618-cve-2026-109619/ · https://blog.cloudflare.com/php-vulnerabilities-waf-protection · https://techcrunch.com/2026/03/11/google-completes-32b-acquisition-of-wiz/ · https://www.giiresearch.com/report/tbrc1978396-artificial-intelligence-ai-vulnerability-scanning.html
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
