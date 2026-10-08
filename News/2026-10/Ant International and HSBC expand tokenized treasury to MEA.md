---
title: "Ant International and HSBC expand tokenized treasury to MEA"
date: 2026-10-07
retrieved: 2026-10-08
tags:
  - company/ant-international
  - company/hsbc
  - industry/blockchain
  - industry/b2b-payments
  - region/mea
  - type/expansion
sources:
  - https://www.businesswire.com/news/home/20261005783186/en/Ant-International-and-HSBC-Expand-Real-Time-Treasury-Management-Services-to-the-Middle-East
status: enriched
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sc05640b3
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Ant International and HSBC expand tokenized treasury to MEA

> [!info] 2026-10-07 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🌍 Ant International and HSBC expand real-time treasury management services to the Middle East. Ant International becomes HSBC’s first regional client to use its Tokenised Deposit Service, completing real-time AED transactions in the UAE and cross-border USD transfers between the UAE and markets including Hong Kong and Singapore.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://www.businesswire.com/news/home/20261005783186/en/Ant-International-and-HSBC-Expand-Real-Time-Treasury-Management-Services-to-the-Middle-East>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Ant International and HSBC expand tokenized treasury to MEA
_Analytical notes (not a post). Importance: 3/5._

## [0] What exactly happened (de-PR'd)
On 6 Oct 2026, Ant International said it extended its existing tie-up with HSBC to bring HSBC's **Tokenised Deposit Service (TDS)** to the Middle East, with Ant becoming HSBC's **first TDS client in the region**. Two corridors were exercised: (a) real-time **intra-UAE AED** tokenised-deposit transfers; (b) **USD** tokenised transfers initiated from the UAE to HK and Singapore. Transactions were initiated on **WhaleRTP** (Ant's proprietary blockchain treasury-settlement platform) and executed through HSBC's TDS, with the two jointly designing the workflow.

**De-PR'ing the frame.** The press wording ("expand real-time treasury management services") implies a bigger product event than it is. This is a **geographic rollout of an already-live service to one more market (UAE) for one already-onboarded client (Ant itself)** — not a new product, not a new external customer, not a public-network launch. Several outlets describe the UAE transactions as **"pilot" / "test"** transactions (thepaypers, bamboodt), which matters: "completed pilot transactions" is not the same as "live at scale for third parties." The economically honest read: Ant is both the technology partner (WhaleRTP) and the first/only named user, so this is close to a **co-development milestone between two long-standing partners** rather than independent third-party adoption. → Why framed this way: both sides benefit from a "regional first" headline in a hot narrative (banks racing to put deposits on-chain ahead of stablecoins), and the UAE is a strategically marketed hub.

**What is genuinely concrete:** AED is now a supported TDS currency and the UAE is now a live TDS market. HSBC TDS is live in **six markets** (HK, Singapore, Luxembourg, UK, US, UAE) across **seven currencies** (CNH, HKD, SGD, EUR, GBP, USD, AED). That currency/market list is the real, checkable delta.

## [1] Competitors / peers
Direct bank-led tokenised-deposit / on-chain treasury rails:
- **JPMorgan Kinexys** (ex-Onyx): the clear scale leader — **$4T+ processed to date**, ~**$7B/day** settling (reported Mar 2026), and a **deep MENA footprint**: mandates/live clients incl. Qatar National Bank, First Abu Dhabi Bank, Saudi National Bank, Emirates NBD, Commercial Bank of Dubai, Bank ABC. JPMD deposit token going to Canton Network. See [[JPMorgan tokenizes private-equity fund on its blockchain]].
- **Citi Token Services**: billions processed since 2024 launch, live US/UK/SG/HK, integrated with 24/7 USD clearing (250+ banks, 40+ markets). See [[Citi Token Services integrates with 24 7 USD clearing]].
- **BNY** weighing tokenised deposits for its ~$2.5T/day network ([[BNY explores tokenized deposits for payments network]]); **SWIFT/Standard Chartered-HSBC** live tokenised-deposit tx on SWIFT's blockchain ledger ([[SWIFT to integrate blockchain-based ledger for cross-border payments]]); broad "most custody banks now tokenize" trend ([[Most custody banks now offer tokenization services]], [[UK banks prep live pilot of tokenized sterling deposits]]).

**Position: catching up, not ahead.** On MENA specifically, **JPM is materially ahead** — multiple live regional bank clients vs HSBC's single corporate (Ant). HSBC's differentiator is its own global branch network + a captive, blockchain-native anchor client (Ant) that actually routes real cross-border volume. → Second-order: the race is less about tech novelty (tokenised deposits are now table-stakes among global transaction banks) and more about **which network wins the corridor density and the regulated-currency coverage**; AED coverage is a genuine, if narrow, HSBC gain in a corridor (Gulf↔Asia) where HSBC and Ant both have real flows.

## [2] Company history / fit
Clear, logical trajectory, not opportunistic:
- **May/Jun 2025**: HSBC launches TDS in Hong Kong; **Ant International is the first client**, doing instant intragroup HKD/USD transfers by tokenising deposits on HSBC's DLT — built off a pilot of Ant's internal **Whale** platform.
- **Dec 2025** (Forbes): Whale/WhaleRTP processed ~a third of Ant's global transactions on-chain in 2024 (~$1T volume); WhaleRTP handled **45% of cross-border volume in 2025**, cutting working-capital needs ~60% and lifting interest income ~23%.
- **Apr 2026**: HSBC extends TDS to the **US**.
- **Sep 2026**: Ant launches full-stack AI-native stack (Alipay+, Antom, WorldFirst, Bettr) ([[Ant International launches AI SHIELD risk toolkit]] context).
- **Oct 2026**: UAE/MEA (this item).

→ Why Ant acts this way: Ant runs a sprawling cross-border group needing 24/7 intragroup liquidity; it is **structurally the ideal reference client** because it supplies both the demand (real FX/treasury flows) and the tech (WhaleRTP). Riding HSBC's regulated rails lets Ant stay bank-grade and compliant while owning the orchestration layer. The UAE step fits Gulf↔Asia corridor logic and Ant's Middle East merchant/acquiring push ([[Capital A taps Ant International to cut FX hedging costs]] shows the same treasury-optimisation playbook).

## [3] Novelty / value-add / traction
**Novelty is incremental.** Tokenised deposits for intragroup/cross-border treasury are already live for Ant (since mid-2025) and across JPM/Citi. The new bits: (1) **AED** as a tokenised-deposit currency; (2) UAE as a TDS market; (3) the specific **UAE→HK/SG USD** corridor. These are real but narrow.

**Traction caveat (the anti-PR gate):** the UAE leg is described as **pilot/test** transactions and the only named user is Ant itself. There is **no disclosed third-party corporate on TDS in the UAE**, no volume figure for the UAE corridor, and no AED ticket size. → Why the value-add is real-but-limited: the durable value accrues to whoever captures the **regulated settlement + corridor liquidity**, i.e. HSBC (balance sheet, currency licences) and to Ant as orchestrator. Tokenisation itself is **commoditising** fast across transaction banks, so the moat is network coverage + the captive flow, not the "tokenised deposit" per se. For Ant, the genuine payoff is the WhaleRTP-reported working-capital/interest-income gains — but those are 2025 group-wide metrics, not attributable to this UAE step.

## [4] What's next / market sentiment
Expect further **TDS market/currency additions** and, the key test, **named third-party corporates** beyond Ant in the UAE. Sentiment is strongly pro-"deposit tokens over stablecoins" among global banks (the bitbase framing: "banks race to put deposits on-chain ahead of stablecoins"), reinforced by Gulf regulators courting digital-asset infrastructure. Risks: (1) **concentration** — HSBC's MENA tokenised-treasury story currently rests on one client; (2) **interoperability** — competing permissioned networks (Kinexys/Canton, Citi, SWIFT ledger) risk fragmentation; (3) execution gap between "pilot completed" and "live at scale." → Counterintuitive second-order: being first-mover with a single captive anchor client can look like leadership but is **fragile** — JPM's multi-bank MENA roster is a more defensible position than HSBC's single-client headline.

## Sources
- Business Wire (primary release, 5–6 Oct 2026): https://www.businesswire.com/news/home/20261005783186/en/Ant-International-and-HSBC-Expand-Real-Time-Treasury-Management-Services-to-the-Middle-East
- ffnews: https://ffnews.com/news/ant-international-and-hsbc-expand-real-time-treasury-management-services-to-the--c1246639
- thepaypers (pilot framing): https://thepaypers.com/fintech/news/ant-international-pilots-hsbc-tokenised-deposits-in-the-middle-east
- bitbase (banks-vs-stablecoins framing): https://www.bitbase.com/news/327526
- HSBC HK launch (Jun 2025): https://www.about.hsbc.com.hk/news-and-media/hsbc-launches-tokenised-deposit-service-for-corporate-cash-management-in-hong-kong
- Crowdfund Insider / PYMNTS (Ant first client, 2025): https://www.pymnts.com/news/banking/2025/ant-international-helps-hsbc-hong-kong-offer-tokenized-deposits/
- HSBC US expansion (Apr 2026): https://www.businesswire.com/news/home/20260413715909/en/HSBC-Expands-Tokenized-Deposit-Service-to-the-United-States
- Forbes on Whale/WhaleRTP metrics (Dec 2025): https://www.forbes.com/sites/zennonkapron/2025/12/13/inside-ant-internationals-treasury-platform-how-whale-bettr-and-ai-are-rewiring-global-liquidity/
- JPM Kinexys MENA: https://www.jpmorgan.com/payments/newsroom/kinexys-blockchain-mena-region
- CoinDesk Kinexys scale (Jun 2026): https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
### Red-team / challenge questions

1. **Is this a new product or a geographic rollout?** A rollout. HSBC TDS already live since mid-2025; this adds UAE as the 6th market and AED as a currency. (answered)
2. **Pilot or live?** Multiple outlets (thepaypers, bamboodt) call the UAE transactions "pilot"/"test." Not confirmed live-at-scale for third parties. (answered — caveat)
3. **Any third-party corporate using UAE TDS, or only Ant?** Only Ant is named. Ant is simultaneously tech partner (WhaleRTP) and the client — weakens "adoption" claim. (answered)
4. **What is genuinely first here?** First TDS client in MEA (Ant), AED tokenised deposits, UAE→HK/SG USD corridor. All narrow but real. (answered)
5. **Duplicate of the Jun 2025 HK "first client" story?** No — different region (MEA), new currency (AED), new corridor. Fresh development, not a reprint. (answered — FRESH)
6. **Who is ahead in MENA?** JPM Kinexys, decisively — 6+ live MENA bank clients (QNB, FAB, SNB, Emirates NBD, CBD, Bank ABC) vs HSBC's single corporate. (answered)
7. **Any disclosed volume/ticket size for the UAE corridor?** None. No AED amount, no transaction count. (open — silence is telling)
8. **Does WhaleRTP's 45%/60%/23% metrics apply to this UAE step?** No — those are 2025 group-wide figures (Forbes), not attributable to UAE. Don't let PR borrow them. (answered)
9. **What is the real moat — tokenisation or the network?** The network (regulated settlement + corridor coverage + captive flow). Tokenised deposits are commoditising across JPM/Citi/BNY/SWIFT. (analysis)
10. **Who captures the margin?** HSBC (balance sheet, FX, licences) + Ant as orchestrator; the "token" layer is thin. (analysis)
11. **Interoperability risk?** High — Kinexys/Canton, Citi, SWIFT ledger are competing permissioned silos; cross-network settlement unsolved. (open)
12. **Is "first in region" a strength or fragility?** Fragile — single anchor client is less defensible than JPM's multi-bank roster. (hypothesis)
13. **Regulatory backdrop in UAE?** Gulf regulators actively courting digital-asset infra; supportive, but no specific UAE licence detail in the release. (partly open)
14. **Why announce now?** Rides the "deposit tokens vs stablecoins" bank narrative and UAE-hub marketing; also sequences after Apr 2026 US expansion. (analysis)
15. **Does this change Ant's or HSBC's economics materially?** Not yet — incremental corridor, no new external revenue disclosed. (answered — limited)

Importance: 3/5 — A real, checkable regional expansion of a live service (new market UAE, new currency AED, new Gulf↔Asia corridor) from two credible, deeply committed players, and part of a structurally important shift of corporate treasury on-chain. Capped at 3 because it is incremental (rollout, not new product), the UAE leg is pilot-stage with a single captive client (Ant itself) and no disclosed volumes, and HSBC trails JPM Kinexys badly on actual MENA third-party adoption.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Tokenised bank deposits — on-chain claims on commercial-bank money, kept inside the regulated banking perimeter (vs. stablecoins) — are the fastest-moving wholesale-payments subvertical of 2025–26. No clean, free TAM exists for "tokenised deposits" specifically → no data on market size; the best available proxy is throughput at the leading rail: JPMorgan's Kinexys (formerly Onyx) processes >$7bn/day and >$7tn cumulative in wholesale tokenised-deposit transfers (per Kinexys/press, via Banking Exchange, as of 2026). Structure: still forming and bank-controlled, not fragmented-startup — the value chain is incumbent transaction banks (HSBC TDS, Citi Token Services, JPMorgan Kinexys) owning the ledger + liquidity, with platform layers (Ant's WhaleRTP) orchestrating across banks. Entry barriers are high: banking licences, deposit-taking, correspondent networks, multi-regulator approval. Drivers / "why now": (1) regulatory tailwind for *deposit tokens over stablecoins* in wholesale cross-border (per JPMorgan, foreign regulators prefer tokenised deposits — [[JPMorgan Foreign regulators prefer tokenized deposits over stablecoins]]); (2) a defensive network race — US majors (JPMorgan/Citi/BofA/Wells) plan a shared tokenised-deposit network via The Clearing House targeting 2027 ([[US banks build collaborative tokenized deposit network]]) explicitly to counter stablecoins. Second-order effect: banks are racing to keep treasury flows on *their* balance-sheet rails before stablecoin issuers disintermediate the deposit base.

**Competitive landscape.** Sector KPIs: for a bank TDS — settlement throughput ($/day), number of live markets/currencies, banks connected; for the orchestration layer (WhaleRTP) — banks integrated, currencies, corridors live. Key players + basis of competition (network reach + regulatory coverage, not price): HSBC TDS now live in **6 markets** — Hong Kong, Singapore, Luxembourg, UK, US, UAE (per HSBC/Ant PR, 2026-10-06); Citi Token Services (live NY–London–HK, expanding to Japan + UAE, [[Citi expands Citi Token Services into Japan and UAE]]); JPMorgan Kinexys (>$7bn/day). Ant's WhaleRTP is integrated with >20 global banks and supports 17 currencies (per PR). Recent dated moves show how fast this is compounding for the Ant↔HSBC pair: 2025-09 TDS launch with Ant ([[HSBC launches tokenized deposit service with Ant International]]); 2025-11 US+UAE markets added ([[HSBC expands tokenized deposit service to US and UAE]]); 2025-12 Ant/HSBC/Swift pilot completed ([[Ant International, HSBC and Swift complete tokenized deposits pilot]]); 2026-04 Canton Network pilot ([[HSBC completes tokenised deposit pilot on Canton Network]]); 2026-10 MEA expansion (this note). Ant is multi-homing — it also runs tokenised deposits with Standard Chartered on Whale ([[Standard Chartered rolls out tokenized deposits on Ant's Whale]]), UBS Digital Cash ([[UBS partners Ant International on Digital Cash blockchain platform]]) and JPMorgan Kinexys FX settlement ([[Ant International completes blockchain FX settlement via JPMorgan's Kinexys]]). Protagonist position: HSBC is **ahead of peers on live-market breadth** (6 markets) but behind JPMorgan on disclosed scale; Ant is the orchestration **hub** connecting rival banks — a genuine network-effects moat (each bank added makes WhaleRTP more valuable to corporates) `(analysis)`. Moat for HSBC = scale + regulated multi-jurisdiction footprint; for Ant = switching costs once corporate treasury is wired into WhaleRTP.

**Comps & multiples.** Ant International is private → no market-cap/revenue multiple; last disclosed data point is a sought $1bn raise at a **~$10bn valuation** ([[Ant International seeks $1B raise at $10B valuation]], 2026-06) — a round valuation, not market cap, and against undisclosed revenue, so EV/Revenue = no data. HSBC is public (LSE/HKEX; US ADR, not in SEC coverage set here) but TDS is a feature inside Wholesale Transaction Banking, not separately valued → a clean TDS multiple is `[UNSOURCED]`. **IR grounding (HSBC H1 2026, interim results 2026-08-04):** Wholesale Transaction Banking fee & other income **$6.1bn** in H1 2026 vs **$5.8bn** H1 2025 = **+5.2%** ($6.1bn/$5.8bn − 1); +7% y/y in Q2 across all product areas; group revenue $38.2bn (+6%), PBT $20.4bn (+6%) (per HSBC Interim Results 2026 media release / investor presentation). This frames the stakes: tokenised deposits defend a transaction-banking fee pool growing only mid-single-digit — the prize is protecting ~$12bn/yr of wholesale TxB income, not new revenue. Peer internal comps (no public multiples, qualitative): [[JPMorgan, BofA, Citi plan shared tokenized deposit network by 2027]], [[Citi expands Citi Token Services into Japan and UAE]], [[Standard Chartered rolls out tokenized deposits on Ant's Whale]]. Distribution not computed — no ≥3 comparable public figures; qualitative comparison only.

**Risk flags.**
- **Rail dependence / disintermediation of the orchestrator.** Ant's WhaleRTP sits *on top of* banks' TDS ledgers; it owns the corporate relationship but not the settlement rail. If banks' own token networks (the 2027 Clearing House network, Citi Token Services) interconnect directly, the orchestration layer's value — and its take — can be squeezed. Why it matters: the party that owns the ledger + liquidity ultimately captures the economics.
- **Economics undisclosed — "announced vs. monetised."** Neither party disclosed fees, pricing or transaction volumes for the MEA flows (PR is strategic-milestone language only). Flag "who's silent about what": no ticket size, no revenue, no cost-saving figure → adoption is real (pilot→live) but the P&L contribution is unproven.
- **Concentration + geopolitical/regulatory exposure.** This is a single-corridor, single-anchor-client expansion (Ant as HSBC's *first* MEA TDS client) in a new jurisdiction (UAE); Ant is a China-linked group pushing cross-border USD rails amid tightening scrutiny of Chinese fintech abroad and multi-regulator tokenised-money rules still being written. Why: concentration in one client/market and cross-border USD politics make the flow fragile to a single regulatory or counterparty shift.

**What this changes (idea-lens).** `(analysis)` This is incremental network-extension, not a re-rating: it widens HSBC's live-market lead (6 markets) and cements Ant/WhaleRTP as the multi-bank treasury hub in a market incumbents are racing to wall off before stablecoins arrive. Falsifiable thesis: tokenised deposits become the default wholesale cross-border rail for large corporates *if* interbank interoperability lands (Swift ledger / Project Agorá / the 2027 US network) — watch for the first disclosed throughput or fee figure from WhaleRTP/HSBC TDS and whether rival banks' tokens become directly interoperable. What breaks it: if the US 2027 shared network or a Swift ledger standard commoditises connectivity, orchestration layers lose pricing power and the moat shifts entirely back to balance-sheet-owning banks.

Sources: https://www.businesswire.com/news/home/20261005783186/en/Ant-International-and-HSBC-Expand-Real-Time-Treasury-Management-Services-to-the-Middle-East · https://ffnews.com/news/ant-international-and-hsbc-expand-real-time-treasury-management-services-to-the--c1246639 · https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2026/interim/pdfs/hsbc-holdings-plc/260804-hsbc-holdings-plc-interim-results-2026-media-release.pdf · https://www.bankingexchange.com/news-feed/item/10700-tokenized-deposit-networks-a-practical-guide-for-the-banking-c-suite-in-2026 · https://www.pymnts.com/news/banking/2026/tokenized-deposits-set-up-banking-next-network-race/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
