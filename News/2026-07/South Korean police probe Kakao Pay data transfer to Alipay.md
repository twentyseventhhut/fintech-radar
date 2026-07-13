---
title: "South Korean police probe Kakao Pay data transfer to Alipay"
date: 2026-07-13
retrieved: 2026-07-13
tags:
  - company/kakao-pay
  - company/alipay
  - industry/payments
  - region/asia
  - type/regulation
sources:
  - https://www.connectingthedotsinfin.tech/r/ae835357
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s5a914b22
month: 2026-07
enriched: true
importance: 4
freshness: fresh
---

# South Korean police probe Kakao Pay data transfer to Alipay

> [!info] 2026-07-13 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇰🇷 South Korean police launches a probe into Kakao Pay Corp.'s transfer of 40 million of its users’ information to Chinese payment app Alipay, in what has become one of the country's most closely watched FinTech controversies. Continue reading

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.connectingthedotsinfin.tech/r/ae835357>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: South Korean police probe Kakao Pay data transfer to Alipay
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
The **Gyeonggi Nambu Provincial Police Agency** has opened a **full criminal investigation** into Kakao Pay, having received a **referral from the Financial Supervisory Service (FSS)**. Kakao Pay has been **"booked" (formally named a suspect) as a corporation on suspicion of violating the Credit Information Act** (KED Global, 2026-07-09; MLex; Seoul Economic Daily). This is the point people miss: the story is NOT another regulator fine — it is the **escalation from administrative penalty to a police/criminal track** (Credit Information Act Art. 32 requires per-instance individual consent before providing personal credit info to a third party).

The underlying conduct: between **27 April 2018 and 21 May 2024**, Kakao Pay transmitted **54.2 billion records** of personal credit information covering a cumulative **40.45 million people** to **Alipay (Singapore)** — daily, without user consent. Data included (encrypted) mobile numbers, email addresses, charged balances and electronic financial transaction data. Officially framed as feeding Apple's **"NSF score"** (Non-Sufficient-Funds, 0–100 default-risk score) that Apple requires from any App Store payment provider for fraud/insufficient-funds control.

**Why structured this way / what it reveals:** Kakao Pay's defense — "encrypted data, lawful procedure, fraud prevention for Apple Pay on the App Store" — is a *purpose-laundering* argument: even if the stated purpose (fraud control) is legitimate, the LAW keys on **consent per transfer**, not on purpose or encryption. That is why the criminal exposure survives Kakao Pay's technical defense. The second-order tell: the data went to **Alipay Singapore, Kakao Pay's ~2nd-largest shareholder (Ant/Alipay affiliate, ~32% stake)** — so a "vendor fraud-scoring" story doubles as a **related-party cross-border data flow to a Chinese-linked shareholder**, which is what makes this politically radioactive in Korea.

## [1] Competitors / peers (regulatory-exposure comparison)
- **Apple** — co-respondent. PIPC (Jan 2026) fined Apple ~KRW 2.45bn + ~KRW 2.2bn (non-disclosure), ordered to destroy the NSF model. Apple was the *commissioner* of the score; Kakao Pay the *transferor*. Both criminal-adjacent, but Kakao Pay is the one police-booked.
- **Alipay/Ant** — the recipient and interested shareholder; PIPC action named Alipay too (Digital Policy Alert). Ant's global posture (see [[Ant Group adds stock trading to AlipayHK]], [[2C2P to invest $60 million after Ant Group acquisition]]) makes Korea a reputational pressure point on cross-border data.
- Contrast with Alipay's *other* Korea footprint, which is clean/commercial: [[Alipay+ and Mastercard bring NFC payments to Kakao Pay]] (Sept 2025) and [[PayPay launches payments in South Korea via Alipay+]] — legitimate rails partnerships. So the "Alipay in Korea" story bifurcates: sanctioned data-sharing vs. sanctioned commercial rails.

**Why the landscape is this way:** Korea's regulators (PIPC + FSS + now police) are demonstrably willing to run **parallel, escalating tracks** on the SAME facts. This is a jurisdiction that stacks penalties rather than settling once.

## [2] Company history / fit
Kakao Pay trajectory: KOSPI-listed digital wallet arm of Kakao Corp. Recent moves show a company under strain — it **abandoned the SSG Pay / Smile Pay acquisition** (~KRW 400bn) at the last minute on parent Kakao's order ([[Kakao Pay abandons acquisition of Shinsegae's SSG Pay, Smile Pay]]), yet is still pushing growth: [[Kakao Pay targets 10 million offline payment users by 2027]], [[Kakao Pay links Japan's PayPay to offline payments in Korea]], [[Paywatch raises $20M Series A with Kakao Pay]]. **Why it acts this way:** Kakao Pay needs the Ant/Alipay relationship (global rails, NFC reach, shareholder capital) — which is exactly the relationship now generating its worst regulatory/criminal liability. The strategic dependency IS the legal risk.

## [3] Novelty / value-add / traction (freshness)
**This is a genuinely NEW event, not a reprint of the fine.** Prior coverage was the *administrative* strand: PIPC KRW 5.968bn fine + corrective order (Jan 2026); FSS ~KRW 15bn / "$10–11M" fine + institutional warning (Apr 2025 → confirmed ~KRW 12.976bn Feb 2026); appellate appeal by KakaoPay. The July 2026 item is the **criminal-investigation strand**: police booking Kakao Pay as a corporate suspect under the **Credit Information Act** following an **FSS criminal referral**. New actor (police), new legal basis (criminal, not administrative), new procedural stage. Traction = real state action, not an announcement.

## [4] What's next / market sentiment
Path: police investigation → possible referral to prosecutors → potential indictment of Kakao Pay (corporate) and possibly executives. Parallel civil/administrative appeal is already at the **appellate court** (KakaoPay contesting fines). Risks: (1) a criminal finding would be far more damaging to Kakao Pay's standing than fines already absorbed; (2) renewed political pressure to force unwinding/curbing the Ant/Alipay shareholding and cross-border data flows; (3) chilling effect on the Alipay+ commercial rails partnership. **Counterintuitive second-order:** the more Kakao Pay leans on Alipay for global reach, the more each new Korea-China data headline compounds — the growth engine and the liability are the same relationship. Stock-impact specifics were not confirmed in sources (open).

## Sources
- KED Global, "Korean police launch probe into Kakao Pay's customer data transfer to Alipay" (2026-07-09)
- Seoul Economic Daily, "Police Launch Probe Into KakaoPay Over 54.2bn Data Leak to China" (2026-05-13)
- MLex, "KakaoPay faces police probe over alleged unauthorized data transfer to Alipay"
- AJU Press, "KakaoPay Under Investigation for Allegedly Sharing 404.5 Million User Data" (2026-05-14)
- Digital Policy Alert / dataguidance — PIPC fines Kakao Pay, Apple, Alipay (Jan 2026)
- The Korea Times (2024-08-13; 2025-04-09) — FSS findings / fine
- The Register (2024-08-15) — 40M-user data sharing
- MLex — KakaoPay appellate appeal; fresh KRW penalty
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Challenge / red-team

**Importance: 4/5** — This is the criminal-escalation of Korea's most-watched fintech data scandal: a formal police booking of a KOSPI-listed payments firm as a corporate suspect under the Credit Information Act, following an FSS referral, touching a Chinese-linked (Ant/Alipay ~32%) shareholder. Materially above a routine regulator fine because criminal liability + related-party China-data politics raise structural questions about Kakao Pay's ownership and rails strategy. Not a 5 because it's an *investigation opening*, not yet an indictment or verdict, and the underlying facts were already public.

1. Is this actually NEW vs. the earlier fines? **Answered — yes.** The July 2026 item is the **police criminal probe (Credit Information Act, FSS referral)**, a distinct track from the PIPC (Jan 2026, KRW 5.968bn) and FSS (2025–26, ~KRW 13bn) *administrative* penalties. New actor, new legal basis, new stage.
2. When did the police actually open it? Seoul Economic Daily reports the Gyeonggi Nambu agency began "last month" (~May 2026); the July digest item is the wider surfacing/confirmation of the same probe. Distinguish "opened" (~May) vs. "reported in this feed" (Jul). (open — exact booking date)
3. Who is charged and with what? Kakao Pay booked **as a corporation** on suspicion of violating the **Credit Information Act (Art. 32)** — per-transfer consent requirement. Individual executives named? (open)
4. Does Kakao Pay's "encrypted + lawful + fraud-prevention" defense neutralize criminal exposure? Analysis: no — the statute keys on **consent per transfer**, not encryption or purpose. That's why the criminal track persists.
5. What exactly was transferred? 54.2bn records / 40.45M people, Apr 2018–May 2024, to Alipay Singapore; incl. encrypted phone/email, balances, e-financial transaction data.
6. Why Alipay Singapore specifically? It is Kakao Pay's **~2nd-largest shareholder (~32%, Ant/Alipay affiliate)** — a **related-party cross-border flow**, which is the political core, not just a vendor relationship.
7. Was the NSF-score/Apple purpose real or a fig leaf? Purpose appears real (Apple requires NSF scores from App Store payment providers) but legally irrelevant to the consent violation.
8. Could this force a change in the Ant/Alipay shareholding? Political pressure exists; no divestiture ordered in sources. (open — live second-order risk)
9. Stock-price / market-cap impact? **Open** — not confirmed in sources.
10. Is there prosecutorial referral / indictment risk? Path runs police → prosecutors → possible indictment; not yet reached. (open)
11. Does the parallel appellate appeal weaken or strengthen the criminal case? KakaoPay is appealing the administrative fines at the appellate court; the tracks are independent — an appeal win on fines would not extinguish criminal liability.
12. Is Apple exposed on the same criminal track? Apple was PIPC-fined and ordered to destroy the NSF model, but the *police booking* named is Kakao Pay; Apple's criminal status (open).
13. Any duplicate risk in the corpus? No prior note covers the **police/criminal** angle — closest are commercial ([[Alipay+ and Mastercard bring NFC payments to Kakao Pay]]) and the abandoned M&A ([[Kakao Pay abandons acquisition of Shinsegae's SSG Pay, Smile Pay]]). Not a duplicate.
14. Second-order thesis check: is the growth engine also the liability? Analysis: yes — Alipay dependency delivers global rails/NFC/capital AND the exact China-data exposure now under criminal review. The two cannot be cleanly separated.
15. What would move this from 4 to 5? An actual indictment, executive charges, a court verdict, or a regulator-forced unwind of the Alipay stake.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Korean digital payments/fintech is a consolidated oligopoly around three super-apps — Kakao Pay, Naver Pay (Naver Financial) and Toss (Viva Republica) — layered on top of the online-only banks (KakaoBank, Toss Bank), which together near 60mn customers ([[Korea's online-only banks near 60 million customers]]). All three payment platforms turned profitable and began expanding abroad in 2025 ([[Naver, KakaoPay and Toss turn profitable, expand globally]]). Kakao Pay itself: FY2025 TPV KRW 185.6tn (+11% YoY), revenue KRW 958.4bn (+25% YoY), first annual operating profit KRW 50.4bn; Q1 2026 accelerated — TPV KRW 50.9tn (first >KRW 50tn quarter, +15% YoY), revenue KRW 300.3bn (+42% YoY), with financial-services revenue +82% now ~49% of the mix (per Kakao Pay Q1 2026 IR, via TradingView/AlphaSpread). "Why now": the driver here is *regulatory*, not demand — cross-border data governance (Credit Information Act, Personal Information Protection Act) has become the binding constraint on Korea-China fintech data flows, and enforcement is escalating from administrative fines to criminal probe.

**Competitive landscape.** Sector KPIs: TPV, DAU/MAU, ARPU, take-rate, financial-services attach. Players & basis of competition: Kakao Pay (KakaoTalk messaging distribution), Naver Pay (commerce/search distribution), Toss (product velocity, biometric FacePay — >5mn users, [[South Korea's Toss FacePay surpasses 5 million users]]); competition is on distribution + super-app breadth, not price. Recent moves: Kakao Pay targeting 10mn offline-payment users by 2027 ([[Kakao Pay targets 10 million offline payment users by 2027]]) and linked Japan's PayPay for inbound offline pay (2025-09, [[Kakao Pay links Japan's PayPay to offline payments in Korea]]); Toss planning a Q2 2026 US IPO at $10bn+ (per KED Global/ID Tech). Kakao Pay's position: co-leader by TPV, DAU 6.69mn (+8% YoY Q1 2026), but this probe is a moat *liability* — its Alipay linkage (Ant is #2 shareholder, >32%, per KED Global) is now the source of legal/reputational risk rather than an expansion asset. Related-party angle: the same entity (Ant/Alipay) that received the 40mn users' data is also Kakao Pay's largest strategic shareholder — a governance red flag `(analysis)`.

**Comps & multiples.** Kakao Pay market cap ~KRW 8.3tn (share ~KRW 61,200, Mar 2026), ~$6.28bn; TTM revenue ~$643mn → P/S ≈ $6.28bn / $643mn ≈ **9.8x** (Feb 2026, per Multiples.vc/stockanalysis). On FY2025 revenue KRW 958.4bn (~$690mn) → P/S ≈ KRW 8.3tn / 0.958tn ≈ **8.7x**. Peers: Adyen EV/Revenue ~6.0x, P/E ~22x, EV/EBITDA ~11.2x (Jun 2026, Multiples.vc); PayPal P/E ~16.9x. Internal comp for Ant-in-Korea precedent: Kakao's Dunamu divestitures ([[Kakao sells $670 million Dunamu stake to Hana Bank]]). Read: Kakao Pay's ~9x sales is **rich vs Adyen's 6x** but is arguably supported by +42% Q1 revenue growth and financial-services mix shift (growth-multiple correlation) — not flagged as over-valuation on growth alone; the regulatory overhang is the un-priced tail. EV/EBITDA and clean forward multiples → `[UNSOURCED]` (no free consensus).

**Risk flags.**
1. **Regulatory/criminal escalation.** Case has moved beyond the Feb 2026 FSS fine (~KRW 12.98bn) and PIPC fine (~KRW 5.97bn) to a police raid (Bundang HQ, Jul 2026) and corporate booking under the Credit Information Act — criminal liability, not just administrative. The data set is large: cumulatively ~40.45mn people / 54.2bn credit records transferred 2018–2024, allegedly without consent (per KED Global/Aju Press). Why: caps offline-expansion ambitions and invites tighter cross-border data rules on the whole sector.
2. **Related-party / shareholder concentration.** Ant/Alipay is simultaneously the data recipient AND >32% #2 shareholder. Why: conflicts governance scrutiny, and any forced unwind of the Alipay linkage (or Ant stake reduction, precedent 2022) removes an overseas-payments partner and pressures the stock.
3. **Fine/reputation vs. valuation.** At ~9x sales the stock prices in continued financial-services acceleration; a criminal outcome, larger penalty, or user churn on privacy distrust is not in the ~KRW 8.3tn cap. Why: asymmetric downside given the rich multiple.

**What this changes (idea-lens).** `(analysis)` This is a sector-wide precedent, not just a single-name event: Korea is criminalizing cross-border consumer-data transfers, which raises the compliance cost of Korea↔China fintech rails and could force super-apps to on-shore data/scoring. Falsifiable thesis: if the probe results in criminal indictment or a forced Ant divestment, expect a Kakao Pay de-rating toward peer (~6x) sales and a chilling effect on Alipay/Ant's remaining Korean stakes (incl. Toss Payments). Trigger to watch: prosecutorial referral/indictment decision and any Ant stake action. What breaks the thesis: settlement into a fine-only outcome with no indictment, leaving the growth story intact.

Sources: https://www.kedglobal.com/fintech/newsView/ked202607090008 · https://www.ajupress.com/view/20260709134048744 · https://www.aa.com.tr/en/asia-pacific/south-korea-to-fine-kakao-pay-11m-for-sharing-user-data-with-chinese-platform-alipay/3532358 · https://www.tradingview.com/news/urn:summary_document_slides:quartr.com:2762418:0 · https://multiples.vc/public-comps/kakao-pay-valuation-multiples · https://stockanalysis.com/quote/krx/377300/ · https://idtechwire.com/toss-plans-q2-2026-us-ipo-at-10b-valuation-as-facepay-biometric-payments-reach-1-million-users/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
> [!note] Earnings context for the regulatory probe — grounded in Kakao Pay's (377300.KS) OWN latest reported results (Q1 2026, reported 2026-05-07). NB: this is a legal/regulatory item, not an earnings event; the figures below are supplied to size the regulatory downside. Kakao Pay is a separate KOSPI listing from Kakao Corp (035720), which is covered in IR.

**Verdict (headline read).** Not an earnings print — a police probe. But the financials it lands on are strongly positive: Q1 2026 (ended 2026-03-31) revenue KRW 300.3bn (+41.7% YoY) with operating profit KRW 32.2bn (+630.9% YoY) — the first double-digit operating margin (10.7%) in Kakao Pay's history, driven by digital-finance (securities/insurance) operating leverage. The regulatory risk sits on top of an accelerating, newly-profitable business, and crucially involves its second-largest shareholder (Alipay/Ant, ~34.7% stake).

**Key figures (Q1 2026, YoY).**
- Revenue: KRW 300.3bn (+41.7% YoY).
- Operating profit: KRW 32.2bn (+630.9% YoY); operating margin 10.7% (first double-digit op margin, up from ~1-2% a year ago).
- Net income: KRW 34.7bn (+141.5% YoY); net margin 11.6%.
- Total Payment Volume (TPV): KRW 50.9tn (+15% YoY).
- DAU 6.69mn (+8% YoY); transactions/user +35% YoY. Core base ~24mn MAU (per prior disclosure) [UNSOURCED for Q1'26 exact MAU].

**By segment / driver.**
- Digital finance: KRW 145.9bn (+82.0% YoY), 49% of revenue — the growth engine. Within it: Kakao Pay Securities revenue KRW 100.1bn, AUM +208% to KRW 13.0tn; Kakao Pay Insurance KRW 24.3bn (+85% YoY).
- Digital payment: KRW 138.4bn (+13.3% YoY); online non-captive +24%.
- Platform services: KRW 16.0bn (+67.4% YoY).
- Read: growth is shifting away from core payments toward higher-margin finance (securities/insurance) — this is what flipped the P&L to double-digit margin. The payment franchise (the piece touched by the data/probe) grows in mid-teens.

**vs expectations / prior period.** No public sell-side consensus captured [UNSOURCED]. YoY momentum is unambiguous acceleration: revenue +41.7% and op profit +631% mark a clear inflection to profitability vs prior quarters. Internal trend in corpus: [[Kakao Pay targets 10 million offline payment users by 2027]] (May 2026, ~6mn offline MAU, QR/AI push) and [[Kakao Pay links Japan's PayPay to offline payments in Korea]] — consistent offline/user-growth trajectory.

**Guidance / forward.** No formal quantitative guidance in the release [UNSOURCED]. Management framing is AI/product-led: proprietary "Pay i" system, integration with Kakao's AI-agent ecosystem, sole Korean founding member of the x402 Foundation (autonomous AI-agent payments). Offline-payment target: 10mn users by 2027 (from ~6mn).

**Thesis-flags (regulatory-downside sizing).**
1. Alipay is both counterparty of the probe AND the No.2 shareholder (~34.7%). Fact: the probe concerns transfer of ~40mn users' data to Alipay Singapore. Why it matters: this is not an arms-length breach — it goes to the governance of the largest strategic relationship on the cap table; second-order, any forced unwind/restriction of the Alipay tie hits both the shareholder register and the Alipay+ cross-border payment/credit-scoring cooperation.
2. This is a re-escalation, not a new event. The FSS already fined Kakao Pay KRW 15bn (April 2025) for the same ~40mn-user data transfer (2024 FX inspection). A police (criminal) probe raises the ceiling from administrative fine to potential criminal liability for executives — a step-change in tail risk vs the KRW 15bn already booked.
3. Downside is modest against the P&L but real on multiple/trust. KRW 15bn prior fine is ~0.5 quarters of current op profit (KRW 32.2bn/qtr) — financially absorbable. The genuine risk is (a) re-rating on governance/China-data-exposure overhang just as the stock's story turns to first-time profitability, and (b) constraints on the Alipay+ rails that feed cross-border payments.
4. Timing asymmetry (de-PR). Management is loudly touting the AI/x402/margin-inflection story; the probe reintroduces the data-governance question they would rather leave behind. Watch whether any prospective restriction touches the digital-finance engine (securities/insurance, 49% of revenue and the margin driver) vs the payment leg — the probe is on payment/FX data, so the high-growth finance segment is likely insulated.

Sources: [Kakao Pay Q1 2026 (thepickool)](https://www.thepickool.com/kakao-pay-q1-2026-earnings-profit-surges-631-to-krw-32-2b/) · [Asia Business Outlook — Q1 profit +141%](https://www.asiabusinessoutlook.com/news/kakao-pay-q1-profit-jumps-141-on-fintech-growth-surge-nwid-11868.html) · [Digital Today — Kakao finance units record Q1, DAU 6.69mn](https://www.digitaltoday.co.kr/en/view/53177/) · [Alipay ~34.7% stake / $200m Ant investment (World Finance)](https://www.worldfinance.com/inward-investment/alibabas-ant-financial-invests-200m-in-kakao-pay) · [FSS KRW 15bn fine / 40mn-user data transfer (Kaamel)](https://www.kaamel.com/blog/article/a48b233c-56cd-4164-af6f-c4ed1cdca221) · consensus: no public consensus captured [UNSOURCED]; Q1'26 MAU exact [UNSOURCED]. Kakao Pay IR not on disk / irdb 'notes' table unbuilt — figures via WebSearch, not local IR PDFs.
<!-- /enrichment:earnings_review -->
