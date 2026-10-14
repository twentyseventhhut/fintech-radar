---
title: "SlowMist and Mandiant trace how Bitget $387.5M hack happened"
date: 2026-10-14
retrieved: 2026-10-14
tags:
  - company/bitget
  - company/mandiant
  - industry/crypto
  - industry/fraud-risk
  - region/global
  - type/outage-security
sources:
  - https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sb763ac05
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# SlowMist and Mandiant trace how Bitget $387.5M hack happened

> [!info] 2026-10-14 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Last edition covered how Bitget lost $387.5 million to spoofed transfers without a single private key being stolen. Now we know how the attackers got in. Investigations by SlowMist and Google's Mandiant found the attackers compromised two third-party security appliances using zero-day exploits, planted a web shell on one, moved laterally to the production wallet job server, and deployed a custom withdrawal tool. SlowMist traced the earliest malicious activity to Aug. 31, when a hidden script read a database password from an environment variable. The theft itself took about three hours on Sept. 25.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: SlowMist and Mandiant trace how Bitget $387.5M hack happened
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
This is the **post-mortem / attacker-entry investigation** into Bitget's ~$387.5M loss of 24–25 Sept 2026 (the year's largest crypto hack to date, and among the ten largest ever). The prior event — the loss itself — was never captured as a standalone note in the corpus, so this is the first Bitget-breach entry here. The new material detail is the **attack vector**, from independent probes by SlowMist and Google's Mandiant.

De-PR'd chain of events (dated):
- **Aug 31, 2026** — earliest malicious activity. A hidden script running under a service process on a third-party security appliance ("Product A" node) read a **database password from an environment variable** and connected to the DB. The attackers were inside for ~**3.5 weeks before stealing anything** (dwell time).
- Attackers compromised **two third-party security appliances via zero-day exploits**, planted a **web shell** on one, then **moved laterally to the production wallet-job server**.
- Similar activity re-observed **Sept 23 and Sept 25**.
- **Sept 24, 18:31 UTC** — Bitget's systems detected unauthorized transfers leaving hot wallets. Detection took ~6 min from the first large transfer; the **signing-service stop took a further 2h39m** — in that window ~$238M of the ~$387M left.
- **Sept 25, ~01:49** — a **custom withdrawal tool** forged the risk-control fields and let **Bitget's own signing service sign** fraudulent transfers. Theft spanned ~3 hours, across **11 blockchains**.
- **No private key was stolen and cold wallets were untouched** — the attackers abused the legitimate backend signing flow (spoofed/forged withdrawal requests), not key extraction.
- Loss revised to ~$387.5M after stolen assets surfaced on **Zcash and TRON** (initial figure was ~$351.6M).
- **Attribution:** SlowMist + Mandiant note TTPs consistent with **North Korea's Lazarus Group**; CEO Gracy Chen also flagged North Korea on an X livestream. Attribution is probabilistic, not proven in court.

**Why it's structured this way / what it reveals:** the headline "hacked" obscures that **the exchange's cryptography was never broken** — the weak link was a **third-party security product** (ironic: a security appliance was the breach vector) plus a **plaintext DB password in an env var** and a signing service that trusted forged risk-control fields. The real lesson is **third-party/vendor supply-chain risk + insufficient withdrawal-request integrity checks**, not key custody.

## [1] Competitors / peers (comparable exchange breaches)
- **Bybit, Feb 2025 — ~$1.5B** (largest crypto breach ever; also Lazarus). Mechanism differed: Lazarus compromised **Safe{Wallet} developer infra** and injected malicious JS to swap the cold-wallet transaction at the **signing-interface** layer. Bybit later **sued North Korea/Lazarus and secured an asset freeze** (Aug 2026). [[Bybit secures full UAE virtual asset license]] context shows Bybit's parallel regulatory push.
- **Ledger $86M thefts linked to CryptoBilis** (same month, Oct 2026) — see [[Ledger investigates $86M crypto thefts linked to CryptoBilis]]; a different, user-side/front-end vector but reinforces the 2026 crypto-theft wave.
- **Industry defensive moves in corpus:** [[Ripple partners with Coinbase to counter North Korean hackers]], [[Chainalysis flags North Korea's multi-chain illicit fund movement]], and OFAC/DoJ actions ([[OFAC sanctions individuals over North Korea IT worker fraud]], [[Oleksandr Didenko sentenced to five years for North Korea IT scheme]]) — the sector was already primed for Lazarus-style multi-chain laundering.

**Why the landscape is this way (2nd order):** the two biggest CEX losses (Bybit, Bitget) both route through **trusted off-platform code** (a wallet SDK provider; a security-appliance vendor) rather than core exchange crypto. The attack surface has **shifted from "steal the keys" to "subvert the signing/authorization pipeline"** — meaning cold-storage marketing is no longer the relevant defense; **withdrawal-request provenance and vendor supply chain are**.

## [2] Company history / fit
Bitget is the world's ~6th-largest spot exchange by volume, aggressively expanding in payments and regulated hubs: [[Bitget taps ex-Bitpanda Legal Chief Oliver Stauber to build Vienna MiCA hub]], [[Bitget completes Mexico regulatory registrations with SAT and UIF]], plus the Bitget Wallet LatAm/Mastercard card push ([[Bitget Wallet and Mastercard launch crypto card in Latin America]]). The hack lands mid-expansion, when **trust capital matters most** for its MiCA/LatAm regulatory ambitions.

**Why the disclosure logic:** Bitget restarted withdrawals in phases from Sept 28, pledged to cover user losses, and commissioned **two independent firms** (SlowMist + Mandiant) — a reputation-repair playbook that mirrors Bybit's. Publishing a detailed root-cause (env-var password, vendor zero-day) is a credibility signal that the core custody wasn't broken — useful while courting MiCA regulators.

## [3] Novelty / value-add / traction
What's genuinely **new in THIS item** vs the Sept loss reports: the **confirmed entry vector** (zero-days in two third-party security appliances), the **~3.5-week dwell time from Aug 31**, the **web shell + lateral move to the wallet-job server**, the **custom withdrawal tool forging risk-control fields**, and the **env-var DB password**. Earlier coverage said "backend compromised, no keys stolen"; this is the forensic "how."

**Why the value-add is real:** for a defender, this converts a vague "backend breach" into actionable controls — **vendor zero-day exposure, secrets-in-env-vars hygiene, and signing-service integrity validation**. The counterintuitive finding: a **security product was the ingress**, i.e. the defensive tooling expanded (not reduced) attack surface.

## [4] What's next / market sentiment
- Expect **Lazarus laundering across the 11 chains + Zcash/TRON**; Zcash (shielded) complicates tracing — a growing North-Korea pattern ([[Chainalysis flags North Korea's multi-chain illicit fund movement]]).
- Likely follow-ons: Bitget legal action / asset-freeze attempts (Bybit precedent), insurer/ fund reimbursement questions, and **regulatory scrutiny** of exchange vendor risk management (MiCA, and South Korea, which is actively policing crypto — [[South Korea blocks 27 unregistered crypto exchange websites]]).
- **2nd-order:** the repeated pattern (Bybit, Bitget) that the **biggest losses come via trusted third-party code** will push CEXes toward in-house signing hardening, stricter vendor zero-day SLAs, and withdrawal-request cryptographic attestation — a structural cost increase for the sector. (analysis)

## Sources
- BleepingComputer: Bitget hacked via zero-day in third-party security products — https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products
- The Hacker News: Bitget Confirms Third-Party Zero-Day Behind $387.5M Theft — https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html
- Crypto Times: SlowMist & Mandiant say zero-day began weeks before theft — https://www.cryptotimes.io/2026/09/30/bitget-387-5m-hack-slowmist-and-mandiant-say-zero-day-attack-began-weeks-before-theft/
- Halborn technical analysis — https://www.halborn.com/blog/post/bitget-hack-technical-analysis-september-2026
- Decrypt: losses climb to $387M, North Korea suspect — https://decrypt.co/379350/bitget-hack-387m-what-happened-why-north-korea-suspect
- CoinDesk: Bybit sues North Korea/Lazarus, secures asset freeze — https://www.coindesk.com/policy/2026/08/07/bybit-sues-north-korea-and-lazarus-group-over-usd1-5-billion-hack-secures-asset-freeze
- Rekt News: Bitget — https://rekt.news/bitget-rekt
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Importance: 4/5** — rationale: the year's largest crypto hack ($387.5M), now with a confirmed, dated forensic entry vector (third-party zero-days, env-var DB password, forged signing) from two credible firms (SlowMist + Mandiant), probable Lazarus attribution, and clear vendor-supply-chain lessons that generalize across CEXes. Not a 5 because it's a post-mortem of an already-known loss rather than a new event, and attribution remains probabilistic.

1. **Is the loss figure settled?** Answered — revised from ~$351.6M to ~$387.5M after Zcash/TRON assets surfaced; current consensus ~$387.5M (biggest 2026 hack).
2. **Were private keys or cold wallets compromised?** Answered — No. Attackers abused the legitimate backend signing flow via forged/spoofed withdrawal requests; keys and cold storage untouched.
3. **What was the actual entry point?** Answered — zero-day exploits in two third-party security appliances; web shell planted on one; lateral move to the production wallet-job server.
4. **How long was the dwell time?** Answered — earliest malicious activity Aug 31, 2026; theft Sept 24–25 → ~3.5 weeks undetected.
5. **How did credentials leak?** Answered — a hidden script read a database password from an environment variable (plaintext secret in env) — a basic secrets-hygiene failure.
6. **How long did the theft take and how fast was detection?** Answered — detection ~6 min after first large transfer; signing stop took a further 2h39m; ~$238M of ~$387M left in that window; total theft ~3 hours.
7. **How many chains affected?** Answered — 11 blockchains; later tracing found assets on Zcash and TRON.
8. **Is the Lazarus/North Korea attribution proven?** Open/partial — SlowMist + Mandiant cite TTPs "consistent with" Lazarus; CEO flagged North Korea; no court-proven attribution yet. Treat as probable, not confirmed.
9. **Which specific vendor products were the zero-days in?** Open — reports say "two third-party security products/appliances" (Product A/B) but do not publicly name the vendors.
10. **Were the zero-days patched / disclosed to vendors (CVE)?** Open — no public CVE or vendor patch confirmation found in sourcing.
11. **How does this compare to Bybit (Feb 2025, ~$1.5B)?** Answered — both Lazarus, both via trusted off-platform code, but Bybit was a Safe{Wallet} dev-infra JS injection at the signing interface; Bitget forged risk-control fields to abuse the automated signing service. Bitget ~1/4 the size.
12. **Will Bitget pursue legal/asset-freeze action like Bybit?** Open — Bybit precedent (sued NK/Lazarus, secured freeze Aug 2026) suggests likely, but not yet reported for Bitget.
13. **Are users made whole?** Partial — Bitget pledged to cover user losses and restarted withdrawals in phases from Sept 28; full reimbursement mechanics/insurer involvement not detailed.
14. **Does this change the central risk question for CEXes?** Answered (analysis) — Yes: the two biggest losses prove the frontier has moved from "protect the keys" to "protect the signing/authorization pipeline and vet third-party/vendor code." Security tooling itself was the ingress.
15. **Regulatory fallout?** Open — plausible MiCA/South-Korea scrutiny of exchange vendor-risk management given Bitget's active EU/LatAm expansion; no specific action reported yet.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Crypto-exchange security / custody-ops. Scale of the problem: crypto theft hit $3.4bn in 2025, of which 44% ($1.5bn) was the single Bybit hack (per Chainalysis, via gate.com/forklog, as of Dec 2025); North Korea-linked actors took ~$2.02bn (76% of service compromises) that year, and in 2026 have already crossed $1bn — including this Bitget theft, which investigators (SlowMist/Mandiant) link to operational patterns consistent with Lazarus, the same unit tied to Bybit (per cryptotimes.io / startupfortune, as of Sep-Oct 2026). Structure: exchange security spend is consolidating value into a thin stack of third-party appliance vendors — the attack came in via zero-days in two external "security products," not Bitget's own keys (bleepingcomputer, Oct 2026). "Why now": 2025-26 attack pattern has shifted from stealing private keys to compromising the operational pipeline (spoofed/unauthorized transfers, withdrawal-job servers) and to supply-chain/vendor zero-days (e.g. the parallel Trezor/ShipMonk Metabase zero-day, Aug-Sep 2026) — the human/vendor layer is now the soft target, not cryptography.

**Competitive landscape.** Sector KPIs (security-ops, not financials): dwell time (Bitget: ~25 days — first malicious activity Aug 31, theft Sep 25); theft-execution window (~3 hours across multiple chains); loss vs insurance-fund coverage ratio; hot/warm-wallet exposure. Key players as benchmarks: Bybit ($1.5bn, Feb 2025), Upbit (~$36m hot-wallet, 2026), WazirX (2024). Basis of "competition" here = who reimburses credibly and who publishes proof-of-reserves. Binance's SAFU (~$1bn, on-chain visible) is the reference backstop; Bitget also markets a SAFU fund. Protagonist's position: Bitget is mid-to-upper-tier by volume (surpassed 1M users / $1.2bn AI-agent volume per earlier note, May 2026) but the breach lands it in the "large-loss, vendor-blamed" bucket alongside Bybit. Moat/response (analysis): fast, detailed third-party forensics (SlowMist + Google's Mandiant) plus a loss size ($387.5m) small enough to plausibly absorb vs a $1.5bn Bybit — reputational, not solvency, risk.

**Comps & multiples.** No valuation/round/revenue multiple in this story — it is a security incident, so trading comps = "no data". Loss-scale comparison instead: Bitget $387.5m (2026, largest reported YTD at the time) vs Bybit $1.5bn (2025, ~3.9x larger: $1,500m / $387.5m) vs Upbit ~$36m (2026) vs CertiK's $370.3m total crypto-scam losses for all of Jan 2026 — i.e. this single hack ≈ an entire peak scam-month. Internal comps: [[TRM Labs North Korea hackers took 76% of 2026 crypto hack value]], [[CertiK reports $370 million in crypto scam losses in January 2026]], [[Ripple partners with Coinbase to counter North Korean hackers]], [[Ledger investigates $86M crypto thefts linked to CryptoBilis]], [[Coinbase and Microsoft disrupt Tycoon 2FA phishing platform]].

**Risk flags.**
1. **Third-party / supply-chain dependence.** The breach entered through two external security appliances' zero-days — exchanges now inherit their vendors' attack surface; a vendor zero-day = direct path to the withdrawal pipeline. Second-order: due-diligence and liability shift to opaque security-tool supply chains that customers can't audit.
2. **Operational (not cryptographic) failure.** No private key was stolen; attackers used lateral movement to a wallet-job server + a custom withdrawal tool. Cold-storage/key-ceremony marketing is beside the point when the production transfer path is owned — undermines the industry's "keys safe = funds safe" assurance narrative.
3. **Insurance-fund / reimbursement opacity.** SAFU-type funds have no external insurer, no audited reserve ratio, no deposit-insurance backstop (per cryptoslate/cryptodaily, 2026); a $387.5m draw is survivable but repeated large losses or a bigger hit could exceed the fund — users bear residual risk. Watch whether Bitget's SAFU/PoR is actually sized and verified post-hack.

**What this changes (idea-lens).** (analysis) Reinforces a sector re-rating toward vendor-risk and operational security over cryptography marketing — and strengthens the regulatory case: ESMA opened a MiCA custody review (8 Jul 2026) explicitly covering firms' dependence on third-party tech providers, under which a CASP is liable for client-asset loss from operational failure. Falsifiable thesis: tighter MiCA/CASP custody rules will push liability and audit onto exchanges and their security vendors within 12 months; trigger to watch = ESMA findings / any mandated vendor-risk or PoR-insurance standard. Thesis wrong if losses keep being quietly reimbursed from SAFU with no rule change.

Sources: https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/ · https://www.cryptotimes.io/2026/09/30/bitget-387-5m-hack-slowmist-and-mandiant-say-zero-day-attack-began-weeks-before-theft/ · https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/ · https://forklog.com/en/losses-from-crypto-hacks-reached-3-4bn-in-2025/ · https://cryptoslate.com/36-million-upbit-hack-revives-the-quiet-truth-about-hot-wallet-insurance/ · https://coinpaprika.com/news/eu-regulator-crypto-custody-mica-transition/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
