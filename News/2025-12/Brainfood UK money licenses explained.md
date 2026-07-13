---
title: "Brainfood: UK money licenses explained"
date: 2025-12-24
tags:
  - industry/regtech
  - industry/banking
  - region/uk
  - type/research-report
sources:
  - https://open.substack.com/pub/samboboev/p/deep-dive-uk-money-licenses-payment
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s5a5b0f9b
month: 2025-12
enriched: false
---

# Brainfood: UK money licenses explained

> [!info] 2025-12-24 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] UK Money Licenses - Payment, E-Money, Banking, MSB, and AR Models

## Первоисточники

### open.substack.com
<https://open.substack.com/pub/samboboev/p/deep-dive-uk-money-licenses-payment>
*795 слов · direct*

Deep Dive: UK Money Licenses - Payment, E-Money, Banking, MSB, and AR Models
The UK fintech and payments ecosystem runs on a mosaic of license types. Each comes with specific permissions and limits. As a founder or product strategist, I needed a clear map of these options. Therefore, I have decided to break down the key UK money licenses: Payment Institution, Electronic Money Institution, Bank (Credit Institution), Money Service Business, Cryptoasset Registration, and the Appointed Representative/agent model, explaining what each allows, what it doesn’t, who regulates it, and when to choose one over the other. The focus is on first-principles clarity and how things work in practice, not legal trivia.
Fintech Wrap Up is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Payment Institution (PI) - Facilitating Payments, Not Holding Value 
A Payment Institution (PI) license lets me offer payment services, e.g., money remittance, payment processing, or card acquiring but without creating stored-value accounts. A PI acts as a conveyor of funds, not a bank or wallet provider. In essence, PIs can move money between parties or initiate payments on customers’ behalf, but they cannot issue e-money or hold customer balances beyond the immediate need to execute a payment. This is the critical line: a PI handles payments in transit rather than providing an ongoing account for customers’ money.
From a regulatory standpoint, PIs in the UK are authorized by the Financial Conduct Authority (FCA) under the Payment Services Regulations 2017 (PSRs), which implement PSD2. There are two tiers: small PIs (with monthly transaction volumes under ~€3m), which have lighter requirements, and authorized PIs for larger operations. Both types must meet AML (anti-money-laundering) standards and safeguard client funds during transit, but the capital and compliance burdens are lower than for e-money or banking institutions.
In practice, I’ve seen companies choose a PI license when they need to enable payments but don’t plan to hold customer funds long-term. For example, early Wise (TransferWise) started as an authorized PI to handle remittances. This allowed them to move money across borders efficiently. However, when Wise later wanted to offer multi-currency accounts and debit cards (storing customer money), they found the PI license too limiting and upgraded to an EMI. This highlights the trade-off: a PI license is simpler and cheaper upfront, but it cannot support products like prepaid wallets or stored balances.
 Key Points Payment Institution (PI): 
 Permitted services: Domestic and international payment transactions, money remittance, payment initiation, merchant acquiring, direct debits, etc. PIs serve as intermediaries moving funds from payer to payee. They may also provide account info services (AIS) under open banking, since that involves data not holding money. 
 Not allowed: Issuing e-money or stored value accounts (no wallets where users park funds). PIs cannot hold customer money beyond facilitating a specific payment or transfer. They also cannot pay interest on balances or lend out customer funds; those activities are for banks only. 
 Regulator & framework: FCA under the PSRs 2017 (UK law mirroring PSD2). Prudential rules apply (e.g., safeguarding funds in transit, capital floor of €20k–125k depending on services), but oversight is lighter than for banks. No PRA involvement since PIs don’t take deposits. 
 Examples: Remittance firms and payment processors use PI licenses. For instance, many payment fintechs that don’t offer wallets or cards operate as PIs. Early-stage Wise operated as a PI purely for money transfer. Payment gateways handling merchant payments often are authorized PIs if they hold funds only briefly for settlement. 
 When to choose PI: If your business is about moving money (payments) but not storing it for customers. A PI is faster and cheaper to obtain than an EMI or bank license ideal for a focused payments product or MVP. It’s a good starting point for fintechs doing remittances, payment processing or open banking services, as long as you don’t need customers to hold spending balances with you. 
Electronic Money Institution (EMI) - Issuing E-Money and Wallets 
An Electronic Money Institution (EMI) license goes a step further by allowing issuance of electronic money, essentially stored value that customers can hold in an account or wallet. With an EMI license, you can create multi-currency wallets, prepaid card accounts, or digital payment accounts where users keep a balance for future use. EMIs can do everything a PI can in terms of payment services, plus maintain customer balances over time and issue e-money against funds received. In plain terms, a licensed EMI can operate almost like a bank account provider, except it must not call the funds “deposits” and cannot lend them out for profit.
Keep reading with a 7-day free trial
Subscribe to Fintech Wrap Up to keep reading this post and get 7 days of free access to the full post archives.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
