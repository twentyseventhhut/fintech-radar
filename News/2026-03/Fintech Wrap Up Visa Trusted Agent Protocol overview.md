---
title: "Fintech Wrap Up: Visa Trusted Agent Protocol overview"
date: 2026-03-29
tags:
  - company/visa
  - industry/agentic-commerce
  - industry/infrastructure
  - region/global
  - type/research-report
sources:
  - https://developer.visa.com/capabilities/trusted-agent-protocol
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s097ccd4f
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Visa Trusted Agent Protocol overview

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Trusted Agent Protocol - Visa Developer, accessed March 22, 2026, https://developer.visa.com/capabilities/trusted-agent-protocol

## Первоисточники

### developer.visa.com
<https://developer.visa.com/capabilities/trusted-agent-protocol>
*662 слов · direct*

Trusted Agent Protocol
Enhancing Visa Intelligent Commerce to improve merchant visibility.

available for use by
Merchants
Independent Developers
Regional Availability
N. America 
Asia-Pacific 
Europe 
CEMEA 
LAC 
Visa is introducing enhancements to Visa Intelligent Commerce to improve transparency, safety, and merchant visibility in agentic commerce transactions.
 As AI agents help customers browse merchant sites, discover products, compare prices, and make selections, the commerce journey begins long before checkout. Agents play a key role in shaping the shopping experience from the very first interaction. Historically, merchants and their proxies (CDNs and bot mitigation services, etc.) have classified automated web traffic as bots and have typically blocked such traffic. As agent usage grows, merchants will need tools and controls to distinguish trusted, commerce-focused agents from malicious bots. Recognizing trusted agents allows merchants to engage with the same customers coming through a different medium to streamline and enhance these agent interactions. 
New specifications include details related to signatures that are specific to the merchant and purpose, and are time bound, cannot be replayed or relayed.
 
 This product is in the process of development and deployment.  Depictions are representations of potential features and sequences.  May not be available in all markets. 
     
Verifiable Information
Agent Intent
An indication that the agent is a Visa trusted agent with an intent to retrieve additional details about, or purchase, a specific product or service from the merchant.
Consumer Recognition
Agents can pass multiple consumer related data elements to provide merchants greater insight into the underlying consumer. For example:
 Customer with Merchant Account  - Through a verifiable token ID or loyalty account, merchants will be able to connect the browsing or payment action to a customer's existing merchant account
 Prior Interactions  - If the consumer does not have an existing merchant account, merchants can use provided device identifiers to determine whether this consumer has previously made purchases from their site
 Location Parameters  - To help merchants determine if there are any limitations or restrictions on products or services on products or services that they can sell based on customer location, agents can share country and postal code information
Payment Information
Merchants may support different payment methods for agentic commerce. The protocol lets agents tailor the payment details they provide to align with each merchant’s preferred processing method:
 Key Entry  - Pass a hashed Visa Intelligent Commerce payment credential, allowing merchants to validate the authenticity of credentials entered during checkout. Agents can pass card metadata that merchants can use to enhance their communication with the consumer - for example, display accurate card art and card product descriptions.
 API or Protocol based  - For merchants using APIs or protocols to process payments, pass all required payment information, such as token, shipping address, billing address, needed to complete the transaction.
 IOUs  - Information needed to manage balances and settlements between agents and merchants, bringing merchants supplemental content revenue beyond traditional models like ads and upsells.
Details on how agents generate these signatures are available in the Visa Intelligent Commerce  Client Implementation Guide  for onboarded agents. Visa's  Trusted Agent Protocol  outlines merchant processes like key retrieval, signature verification, and best practices for merchants handling agent messages containing these signatures and acting on their contents.
 By accessing these materials, you are agreeing to the terms and conditions outlined in the  Product Terms . 
Trusted Agent Protocol
Materials detailing Visa's Trusted Agent Protocol. Merchants may read this material for more details on how to implement the Trusted Agent Protocol in adherence with Visa's policies. By accessing, downloading, or using this material, you agree to the terms and conditions outlined in the Trusted Agent Protocol Product Terms.
 Learn More 
Sample Code Implementation of Trusted Agent Protocol
A sample implementation of Visa's Trusted Agent Protocol to give both merchants and agents guidance on how to conduct signature-based authentication in agentic commerce. By using, downloading, viewing, or installing this code from the GitHub repository, you agree to the terms and conditions outlined in the Trusted Agent Protocol Product Terms.
 GitHub Repository

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
