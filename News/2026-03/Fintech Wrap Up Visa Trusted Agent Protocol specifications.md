---
title: "Fintech Wrap Up: Visa Trusted Agent Protocol specifications"
date: 2026-03-29
tags:
  - company/visa
  - industry/agentic-commerce
  - industry/infrastructure
  - region/global
  - type/research-report
sources:
  - https://developer.visa.com/capabilities/trusted-agent-protocol/trusted-agent-protocol-specifications
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s6052521b
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Visa Trusted Agent Protocol specifications

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] Specifications - Trusted Agent Protocol - Visa Developer, accessed March 22, 2026, https://developer.visa.com/capabilities/trusted-agent-protocol/trusted-agent-protocol-specifications

## Первоисточники

### developer.visa.com
<https://developer.visa.com/capabilities/trusted-agent-protocol/trusted-agent-protocol-specifications>
*2171 слов · direct*

Trusted Agent Protocol
 
 ⬅️ Back to Getting Started 
 
 
 Product Terms 
 
 
 Merchant Specifications 
 
 
Merchant Specifications
 By accessing, downloading, or using this specification, you agree to the terms and conditions outlined in the   Visa Trusted Agent Protocol Product Terms .
Introduction
This material outlines the next phase of Agentic Commerce – focusing on how Merchants can recognize when an "approved Agent with commerce intent" is interacting with their website or server and how Merchants can make requests to the Agent (e.g. for payment or additional information).
While it is possible that Agents could have bi-lateral agreements with Merchants and interact through authenticated, secure interfaces, this protocol is applicable to the scenario when the Agent is initially unknown to the Merchant. That is, this protocol is intended for those scenarios [where the Agent is initially unknown] and includes an Agent interacting with a Merchant website or message protocols exposed by a Merchant - and an agent is directed by the user with an intent for commerce.
As agentic commerce becomes more prevalent, we believe this recognition will become necessary, as Merchants (or their Site Protection Providers) will/could confuse these Agent interactions with bots (web crawlers, etc.) or nefarious actors that could be attempting to degrade the Merchant services, be a product reseller of limited-edition releases, or be trying to actively attack the Merchant property. Additionally, it is envisaged that Merchants should have a mechanism to request payment for access to certain information (e.g. customer product reviews) or request additional information from an Agent (e.g. a consumer email address for an unrecognized consumer).
While there are a number of ways that Merchants could identify Agents, such as through user agent headers, allow/white-listing of IP addresses, registries of approved Agents, or shared keys, a more efficient mechanism is to provide linked, verifiable, purpose-identifying, and time-based signed credentials in the headers and/or in the request body of messages when interacting with a Merchant especially when it is originating with a verified intent for commerce. Each of these signatures can be ignored by Merchants that do not adopt, or have not yet adopted, this mechanism.
While there are a number of upstream processes that may occur for an Agent to determine whether a product or service is sold by a Merchant, this protocol is intended during two specific interactions with the Merchant. That is, (1) a browsing interaction, when the Agent has been initiated by a verified consumer with commerce intent and needs to determine further information about a product and whether inventory is available (e.g. in a specific size, color, etc. and shippable to an address) and to determine the final cost of a product after taxes and shipping, and (2) a payment interaction, when the Agent is providing all the information necessary to purchase a product from the Merchant or gain paid access to a Merchant resource.
For Merchants that adopt this mechanism, the purpose of this material is to describe (i) the steps that can be taken to verify each of the signatures, (ii) how the data provided by each signature can be used to identify whether the interaction originated from a trusted Agent, and (iii) how that data can be used to control, limit or complement the interaction.
The protocol is designed to enable agentic commerce at scale with a framework where an Agent can:
Facilitate verifiable trust over existing web infrastructure (HTTP), with minimal changes required to existing merchant systems
Securely carry various forms of payment credentials
Communicate over a variety of channels (e.g., web, API) and protocols (e.g., MCP, ACP)
Audience
This material is intended for Merchants and Site Protection Providers to inform them how to recognize approved Agents and verify that the data agents are including in messages comply with the defined requirements.  The document defines the framework for a generic protocol and references Visa’s implementation specifications. Where examples are provided, we label them explicitly as part of the Visa implementation to distinguish them from the broader Trusted Agent Protocol.
Participants
 Agent Providers (Agent) are certified AI platforms that have been onboarded as an "Agent" to Payment Schemes and are approved and trusted by the respective Payment Schemes to make payments on behalf of thei account holders.
 Checkout Enablers may be used by agents to interact with Merchant websites. While the role of these Checkout Enablers is recognized, the only expectation in regard to this proposal is that these entities will pass through [to the Merchant] any message signatures and query parameters provided by the Agents.
 Consumers are account holders of respective Payment Schemes that have a profile created at an Agent and have at least one payment credential linked to their profile [for the purpose of being used by the Agent to make purchases on the consumer's behalf].
 Site Protection Providers are defined as systems that are typically a layer sitting in front of a Merchant's website. These systems also provide a level of protection to their customers by identifying traffic that could degrade services or be malicious. These are typically CDNs (Content Delivery Networks), trust management systems, or other such proxies.
 Identity Provider is an entity that has verified the credentials used to identify a Consumer and can provide a value [containing the verified credential] that can be authenticated by the relying entity [in this case the Merchant or its Site Protection Provider].
 Merchants are online entities selling goods or services and that, through their acquirer relationship, accept credentials from Payment Schemes as a payment method for these goods and services. Merchants are not required to use this proposal and do not necessarily have to be registered with the Payment Schemes to accept these payment credentials. Merchants can expose their goods or services directly to Agents through APIs or similar message protocols or through a web protocol. Merchants that expose web sites and can recognize when Agents are visiting their web properties may choose to present an agent-specific experience to the Agent - for example, present simpler html pages and/or scale down the number of checkout pages with less navigation.
 Payment Schemes refer to systems that facilitate electronic payments between consumers, merchants, and financial institutions. These schemes set the rules, standards, and infrastructure for Agent initiated transactions, ensuring interoperability, security, and efficiency across various payment channels and third-party payment providers. 
 Key Store will be the location on the web where Merchants or Site Protection Providers can retrieve the public keys needed to verify the signatures.
Trust Model
The trust model described hereunder is comprised of three distinct signatures.
An agent recognition signature provided in the message header (HTTP header, REST API header or similar message header). This signature is intended to ensure that the Agent is a trusted agent interacting with the Merchant in order to retrieve additional information about a specific product/service sold by the Merchant or in order to make an actual purchase. This signature is provided both during the browsing and payment interactions.
A linked and signed consumer/device identity provided in the message request body. This signature is intended to allow the Merchant to determine whether the consumer that the Agent is shopping on behalf of is known to the Merchant. That is, whether the consumer (through a consumer or device identity) has previously shopped at the Merchant or whether the consumer (through a consumer identity, loyalty number, etc.) has an account at the Merchant. This signature is provided during the browsing interaction and may be provided during the payment interaction.
A linked and signed payment container provided in the message request body. This signature is intended to provide information related to the payment credentials and information necessary to complete or complement a purchase. The content provided in the signature is dependent upon the mechanism being used to interact with the Merchant and may contain a range of information. For example, if browser automation is being used to complete a web-based guest checkout, key entry experience, this signature may contain a hash of the payment credential data that will be key entered, while if the protocol allows the complete payment payload , this signature may contain all the data necessary to complete the payment. This signature can be provided during the payment interaction or at any point the Merchant is requesting a payment.
Agent Recognition Signature
The Agent recognition signature is based on the HTTP Message Signatures defined by RCF 9421 [and aligned with web-bot-auth] and offers a secure, standardized, and verifiable way to ensure the legitimacy of clients (bots, agents, or any automated traffic) and the integrity of their requests. Here's why it's beneficial:
 Strong Identity Verification Agents can sign requests using a private key. Servers verify the signature using the corresponding public key [retrieved from a trusted Key Store]. This proves the Agent's participation in the Payment Scheme specific program. In the case that the public key is associated with Visa, this would imply the Agent's participation in (and compliance with) Visa Intelligent Commerce program requirements. 

 Tamper-Proof Requests The signature covers critical parts of the message (e.g., method, path, headers). Any modification to the request (e.g., changing a header or path) invalidates the signature. 

 Replay Attack Protection Agents include timestamps (created, expires) and nonces in the signature. Servers are able to reject reused or expired signatures, thereby preventing replay attacks. 

 No Reliance on IP addresses or overloading of header fields 
 Traditional bot detection often relies on IP addresses or adding content to other HTTP header fields. HTTP message signatures are specifically intended to provide cryptographic assurance of origin.
As per RFC9421, HTTP Message Signatures comprise the following 2 fields being present in the HTTP header or message header:
The following is a browsing example of the above fields as provided in a HTTP header as defined in this material:
Processes
The following section describes the processes used to validate the agent recognition signature and describes the steps that can be taken to verify the signed content. These validation processes can be performed independently by the Merchant or by a Site Protection Provider on behalf of the Merchant.
In the context of Visa Intelligent Commerce, Agents are expected to interact with a Merchant site at two points.
The first point is when the Agent is navigating to a product detail page in order to retrieve more details about a specific product (for example, determine what materials were used in the production process) or, to determine whether the product is currently available is a specific size or color, etc.
The second point is when the Agent is navigating to a checkout page to complete the purchase
Both of the above interactions can contain a slightly different message signature and as such this section details the steps for either interaction.
Example Agent Verification for Payments
Signature Verification
The following description is for any agent-to-merchant interaction and defines how a Merchant should verify the Message Signature.
The Message Signature will follow the RFC9421 standard ( https://datatracker.ietf.org/doc/html/rfc9421#section-2.3-3 ) and contain the below minimum set of parameters that are required to be present for a trusted Agent.
 Sample Browsing Request with Message Signature 
 Sample Checkout Request with Message Signature 
 Required Message Signature Fields 
Below is the minimum list of fields required to be a trusted Agent. An Agent or a Payment Scheme may optionally define additional fields that could be part of the signature.
 Verification Steps 
The Merchant should perform the following steps to verify that the message being received has not been manipulated in any way, is not being replayed or relayed, and has been signed using a key maintained by a trusted agent.
If the header does not contain a message signature with a Signature-Input field containing a tag of either agent-browser-auth or agent-payer-auth , the message has not been signed by a trusted agent. The Merchant may decide to block the message or use some other mechanism to determine whether the interaction can continue. The following steps only apply if the Signature-Input field contains a tag of either agent-browser-auth or agent-payer-auth .
 Minimum fields 
 If any of the fields listed in the table above are missing, the message should be blocked.
 Timestamps 
 The timestamps ( created and expired ) should fall within the current GMT time and should not be more than 8 minutes apart. That is, if the interval between the created and expired timestamps is greater than 8 minutes, or if the created timestamp is not in the past, or the expired timestamp is not in the future, the message should be blocked.
 Nonce 
 If maintaining a record of all nonces received in the last 8 minutes, if the nonce received matches a recorded nonce, the message should be blocked.
 Locate the public key 
 If the public key for the keyid in the Signature-Input field has not been previously retrieved and cached, refer to the Public Keys Retrieval Service section for details of how to retrieve the public key. If the public key cannot be retrieved or the public key has expired, the message should be blocked.
 Validate the signature 
 Create the signature base string. The signature base string is a canonical representation of cri

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
