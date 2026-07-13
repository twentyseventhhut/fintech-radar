---
title: "Connecting the Dots: Noah on stablecoins versus SWIFT"
date: 2026-02-11
tags:
  - company/noah
  - industry/stablecoins
  - region/global
  - type/commentary
sources:
  - https://noah.com/en
  - https://noah.com/blog/stablecoin-vs-swift
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sd3a3c101
month: 2026-02
enriched: false
---

# Connecting the Dots: Noah on stablecoins versus SWIFT

> [!info] 2026-02-11 · 1 упоминаний · 2 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] ➡️ Stablecoins vs SWIFT: Routing Value by Logic, Not Legacy by Noah. Stablecoins bridge traditional finance and programmable payments, enabling faster, cheaper transfers than legacy rails. Bank cross-border payments still rely on BIC/SWIFT codes for secure messaging, but SWIFT only sends instructions; it does not move money. Read the full article hereHow SWIFT Transfers Work

## Первоисточники

### noah.com
<https://noah.com/en>
*296 слов · direct*

Powering the New Era of Payments
Trusted by Innovators
Our Solutions
Payin
 Issue named virtual bank accounts across major currencies , supporting both local bank transfer payments and SWIFT. Collect fiat and convert instantly to stablecoins.
Orchestrate
 Trigger automatic payments based on rules you define - like thresholds, timing, recipient type, or currency. Set it once and automate high-volume flows with full compliance and reliability.
Regulated Payments Infrastructure, Engineered for Modern Money
Architected for High-Volume Money Movement
 Precision at scale . Whether you are running mass payroll or high-frequency remittances, our modular infrastructure delivers the flexibility and reliability your platform demands.
Total Visibility, Complete Operational Control.
Developer-First, by Design
This endpoint sets up a workflow which automatically converts fiat currency from bank deposits into cryptocurrency and sends the acquired crypto to the specified wallet address on the specified network.
Backed by the Brightest. Built by Industry Experts
Backed by Felix Capital, FJ Labs, and LocalGlobe, plus a network of strategic investors and operators who believe stablecoins will power the next generation of payments.
Shah Ramezani
Shah Ramezani is the Founder and Board Member of Noah. Shah previously led the Asia division at The Hut Group and has significant experience working in the financial sector at Kingsway Capital, Lazard and UBS.
Thijn Lamers
Thijn Lamers is a founding team member of Adyen and the former Executive Vice President of Global Sales. Adyen grew into the world’s leading global payments platform, with clients including Uber, Facebook & Ebay.
Enterprise Grade Compliance & Security
Risk scoring, anomaly detection, ongoing review.
Pre-existing onboarding data can be shared via API for real-time approval.
Document checks, liveness verification, ID validation. White label or hosted, you decide.
Sanctions, PEP, AML, adverse media checks, travel rule compliance.
Start Building on the Enterprise
Stablecoin Stack.

### noah.com
<https://noah.com/blog/stablecoin-vs-swift>
*1601 слов · direct*

Stablecoins represent the blending between traditional finance and banking, with novel, programmable financial infrastructure. Stablecoins can overcome the limitations of conventional banking rails by moving faster, with lower costs, and providing additional security.
 B ank I dentifier C odes (BICs) are 8-11 characters long and often referred to as S ociety for W orldwide I nterbank F inancial T elecommunication (SWIFT) codes. These codes uniquely represent banks and financial institutions worldwide. These codes facilitate secure and efficient communication across borders. The SWIFT system does not directly transmit or interact with money.
SWIFT’s Role in Money Movement
SWIFT is a secure financial-messaging network; it doesn’t move funds.
After a payment instruction is sent—historically via SWIFT “MT” messages and now migrating to ISO 20022 “MX” under SWIFT’s Cross-Border Payments and Reporting+ (CBPR+) program—settlement occurs on correspondent-bank (nostro/vostro) ledgers and regional high-value systems, many of which are either Real-Time Gross Settlement (RTGS) or net-based, with batch settlements:
 in USD, Fedwire (RTGS) or CHIPS (a private netting system with intraday finality) 
 in GBP, CHAPS (RTGS) 
 in EUR, T2 (RTGS) 
 Note: The MT/MX coexistence period ends 22 November 2025. After this date, all SWIFT messages must use MX format. 
Off-chain payments can be settled more expediently in EUR due to the standardized acceptance of T2, SEPA Credit Transfer (SCT), and SEPA Instant for Euro-based transactions. US-based payments can be routed through either Fedwire (for comparable finality) or CHIPS for liquidity preservation.
 llustrative time ranges by corridor and counterparty; not SLAs. 
Advantages of SWIFT Transfers
SWIFT made cross-border payments dramatically more efficient than the legacy rails it replaced, like Telex, which powered traveler’s checks, and DNS systems that predated modern RTGS infrastructure such as T2, CHAPS, and Fedwire.
 Global Reach With a Single Connection: 
SWIFT is the common language banks use to move money information. With a single connection to your bank, you can pay almost any institution worldwide without new integrations or bespoke corridors. It runs on payment rails your counterparties already trust, which keeps onboarding simple.
 Structured Data Means Fewer Repairs: 
SWIFT’s newer message standard (ISO 20022/MX) sends payments with clear, labeled fields, and many banks pre-check key details via API before a payment goes out. Pre-verification catches typos and missing data up front, reducing “repairs,” investigations, and back-and-forth. Fewer exceptions mean faster credits and less time lost in operations.
 Traceability You Can Audit: 
Modern SWIFT payments carry a unique tracking ID (UETR) and show real-time status in the gpi tracker. You can see when a payment is sent, where it is in the chain, when it’s credited or held, and what fees were taken. Finance and compliance teams get a clean, verifiable trail that accelerates reconciliation and can close their books with confidence.
Limitations of SWIFT Transfers
While SWIFT has proven massively more efficient than telex, it still has substantial limitations and associated costs. Local posting windows serve as a substantial barrier to same-day and instant payment posting. There are three key limitations for SWIFT, despite its global footprint and improved speed.
 Not Built for 24/7 
SWIFT can send a message instantly, but that doesn’t mean the funds settle right away. Banks batch and post payments in their own windows. Some hold for screening. Others delay until the next local business day. For payments crossing borders and time zones, that variability slows everything.
 Fees Stack Up 
Domestic wires in the U.S. can cost $25–35, and international transfers up to $35–50, plus FX spread, plus any intermediary fees. And those deductions often don’t show up until the money lands. Reconciling expected vs received amounts creates additional operations overhead.
 Banking Infrastructure Gaps Remain 
In some markets within sub‑Saharan Africa, remote Pacific islands (e.g., Tuvalu before its ATM rollout), or countries facing correspondent banking restrictions, electronic transfers and SWIFT connectivity remain patchy or unavailable.
These gaps make traditional rails impractical for many real-world use cases. According to the World Bank (Global Findex), over 1.4 billion people remain unbanked , and in many regions, SWIFT is not reliably accessible or practical for many recipients.
How Stablecoin Payments Work
Stablecoin transfers collapse instruction and settlement onto one rail. A provider runs KYC/sanctions checks, submits the transfer to the chosen chain, and after the required confirmations (seconds to a few minutes, chain-dependent), the recipient controls the funds.
If bank money is needed, an off-ramp converts tokens to a local bank credit. Many business flows today are on Ethereum L2s, Ethereum, Solana, or Polygon.
Since stablecoin-based payments are directly settled on a blockchain (e.g., Ethereum, Polygon, Solana, etc.), availability of funds depends on the confirmations of the underlying blockchain rather than local bank clearing and settlement.
With the advent of the GENIUS Act, payment stablecoins like Circle’s USDC and PayPal’s PYUSD have gained substantial credibility in the payments world as a payment option. Unless the beneficiary of a stablecoin transfer wants to offramp, they have near-instant access to their cash.
Regulatory Landscape Overview
Regulations are evolving at various paces around the world, but we’ve selected a few of the major updates from Europe, APAC, and MENA regions to highlight alongside the recently passed GENIUS Act.
 US: GENIUS Act 
The GENIUS Act defines payment stablecoins in U.S. law and sets reserve, disclosure, and supervisory expectations for issuers, reducing policy uncertainty for corporates evaluating stablecoins for treasury workflows.
 EU: MiCA 
Stablecoin provisions for asset-referenced tokens (ARTs) and e-money tokens (EMTs) have applied since June 2024; broader CASP provisions apply from December 2024 with optional national transitional periods until July 2026. In practice, issuers face reserve, redemption, disclosure, and supervision standards.
 UK: Proposed regime 
The FCA published a stablecoin consultation in June 2025, with final rules targeted for 2026; the Bank of England will oversee systemic payment chains. Until finalized, firms operate under existing e-money/payment rules and case-by-case supervision.
 Singapore: MAS framework 
Finalized August 2023 for single-currency stablecoins pegged to SGD or G10 currencies, with requirements for 1:1 high-quality reserves, segregation, monthly attestations, annual audits, and timely redemption.
 Hong Kong: FRS issuer regime 
The HKMA/FSTB issued consultation conclusions in July 2024 and followed with 2025 consultations on licensing, supervision, and AML/CFT rules for fiat-referenced stablecoin issuers.
 Japan: Payment Services Act 
Since June 2023, only licensed banks, trust companies, or registered money transfer agents may issue yen stablecoins; tokens are treated as electronic payment instruments with strict redemption and custody controls.
 UAE: VARA/SCA alignment 
Dubai VARA updated rulebooks in May 2025; a September 2024 SCA–VARA agreement coordinates licensing and supervision for virtual asset service providers (VASPs) operating across the UAE.
 Global baseline: FATF 
The Travel Rule and risk-based supervision apply to VASPs worldwide, with 2025 updates urging faster, consistent implementation.
Net effect: clearer rules in the EU, Singapore, Japan, and Hong Kong reduce policy risk for corporates and banks piloting stablecoin workflows, while the UK and UAE are converging on supervision models that should lower legal uncertainty as rules finalize.
 Secure Transfer 
Stablecoin payments don’t rely on banks or other intermediaries to clear and settle behind the scenes. Good providers layer in operational controls like payment approvals, whitelisted wallets, and KYC/KYB.
 Fast and Efficient Processing 
Stablecoin payments are fast because they don’t have to wait in the same lines. There are no cut-off times, no overnight holds, no business days. Stablecoins move and settle 24/7/365. The moment a transaction is confirmed, the funds are usable, whether it’s 3 pm in New York or midnight in Jakarta.
This speed reduces friction and changes how finance teams operate. There’s no guessing when money will arrive or chasing status updates. You can approve a payment, see that it landed, and move on.
 Low Transaction Fees 
While traditional cross-border payments stack up costs at every hop, stablecoins don’t. Most intermediary deductions disappear. You pay a small network fee and, if applicable, a provider fee. FX only applies when off-ramping to a different currency.
On fast, efficient blockchains, those costs are often just a few cents. Even when converting back to bank money, the total cost is predictable. There are no surprise deductions, no intermediary “lift” fees, and no need to reconcile what was sent versus what was received. What you send is what they receive.
When to Use Stablecoins Over Traditional Systems
Stablecoins aren’t a replacement for all payments, but they solve real problems in the right places. If you’re paying across borders, moving funds outside of bank hours, or handling high-frequency, low-margin transfers, stablecoins can unlock speed and savings that legacy systems struggle to match.
What Comes Next: Stablecoins as the Default Settlement Layer
According to McKinsey & Co., stablecoin circulation has more than doubled in the last 18 months and stablecoins now account for over $30 billion of daily transaction volume. Visa, for example, processes roughly $43 billion per day, placing the current daily volume of stablecoins in line with that of major payment networks.
The same report projects that daily stablecoin volume will grow from $30 billion to $250 billion per day within the next 36 months. At that scale, stablecoins should be considered a default settlement layer for many cross-border workflows. Regulatory clarity (e.g. GENIUS, MiCA, etc.) should translate to continually growing acceptance and integration alongside pre-existing financial infrastructure.
Issuer and chain competition will remain intense, while off-ramp infrastructure and legacy settlement infrastructure should continue to accelerate to meet the modern demand for 24/7 always-on markets. Stablecoins are well-suited to cross-border payments, supplier disbursements, payroll, marketplace settlements, and intraday treasury sweeps.
That said, traditional rails still make sense for domestic payments, legacy invoicing flows, or high-risk jurisdictions where off-ramps are limited or compliance expectations are shifting. But for global, programmable, real-time value movement, stablecoins are already proving to be a better default in many workflows.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
