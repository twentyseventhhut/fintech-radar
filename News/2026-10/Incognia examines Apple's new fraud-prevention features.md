---
title: "Incognia examines Apple's new fraud-prevention features"
date: 2026-10-23
retrieved: 2026-10-23
tags:
  - company/incognia
  - company/apple
  - industry/fraud-risk
  - region/us
  - type/commentary
sources:
  - https://www.incognia.com/blog/apples-new-trust-signals-and-their-role-in-fraud-prevention
  - https://www.incognia.com
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: sdef88942
month: 2026-10
enriched: false
---

# Incognia examines Apple's new fraud-prevention features

> [!info] 2026-10-23 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Incognia examines Apple’s new fraud-prevention features.Incognia’s Gabriel Falcone, Co-Founder and Head of Software Engineering, explains how Apple’s new trust signals can help flag scams but cannot confirm whether a transaction or identity is legitimate. He highlights why combining them with device, location and transaction data remains important for fraud prevention.

## Первоисточники

### incognia.com
<https://www.incognia.com/blog/apples-new-trust-signals-and-their-role-in-fraud-prevention>
*723 слов · direct*

Apple’s New Trust Signals and Their Role in Fraud Prevention 
Subscribe to Incognia’s content

 Apple’s new security capabilities can help detect when a customer is being manipulated by a scammer or verify what an iPhone camera originally captured. 
 However, neither capability can independently determine whether a payment is legitimate, an identity document belongs to the person submitting it, or a device has been compromised. 
 iOS already provides several layers of security, including application sandboxing and restrictions on access to sensitive capabilities. 
 Apple's new fraud-prevention and image-authenticity features build on these protections, giving applications additional information to assess risk. 
 Understanding what these capabilities can establish, and where their limitations lie, is important when incorporating them into a broader fraud-prevention strategy. 
What Apple is adding
 Impersonation Risk Detection helps applications assess whether a user may be involved in an active social-engineering scam. 
 Starting with iOS and iPadOS 27, an application can request an assessment and receive an Unknown, Medium, or High risk level, provided the user has enabled sharing. 
 This addresses a scenario in which a legitimate customer successfully authenticates while being manipulated into authorizing a payment. The application can use the assessment to introduce a delay, display a warning, or request additional verification. 
 Apple also makes an important distinction: Unknown means that no evidence of suspicious activity was detected, not that the action was confirmed as safe. 
 Apple Reference Image provides a way to verify what an iPhone camera originally captured and identify subsequent modifications to a photograph. 
 On iPhone 18 Pro models, taking a photo in Reference mode captures signed sensor data that is used to create an unalterable reference image. Users can compare that reference with the main image to identify changes. 
 For identity verification, this helps establish the authenticity of an image but does not establish the identity of the person submitting it. 
 An authentic photograph of a genuine identity document, for example, could still be submitted by someone other than its owner. Image authenticity therefore complements identity verification, liveness detection, and an assessment of the device and session involved. 
Experience with existing protections
 Mobile platforms have long provided native security mechanisms designed to protect devices, applications, and sensitive information. 
 When attackers need capabilities restricted by the operating system, they often need to bypass native security protections. We have observed this pattern across different types of device manipulation. 
 Jailbreaks are a good example. 
 iOS restricts applications and users from accessing capabilities beyond those permitted by the operating system. Jailbreak techniques typically exploit vulnerabilities or weaknesses to bypass these restrictions. As platforms introduce stronger protections, attackers can adapt their techniques to circumvent them. 
 Apple itself notes that App Attest cannot definitively identify a device with a compromised operating system. A successful application integrity check therefore does not necessarily establish the integrity of the device or the legitimacy of the activity taking place on it. 
 This is where Incognia complements the native security model, using additional device and environment signals to identify situations in which platform protections may have been bypassed. 
What the new signals leave unresolved
 The practical question is which fraud scenarios Apple's new signals can address, and where complementary detections remain necessary. 
 Their actual contribution will need to be measured in real-world deployments, considering both their effectiveness and coverage. 
 Incognia already incorporates evidence from native platform protections into its fraud decisions and monitors fraud attempts that succeed despite those mechanisms. 
 While this experience does not establish how Apple's newer capabilities will perform, it demonstrates why platform protections should be considered alongside other sources of evidence. 
 Device and location intelligence, session information, account history, transaction context, and connections to previous abuse can provide additional context around what the platform reports. 
 Together, these signals help fraud teams identify risks that fall outside the scope or visibility of individual platform protections. 
Combining platform and application-level defenses
 Responding quickly to emerging attacks is also essential to fraud prevention. 
 Operating-system protections evolve according to platform-wide priorities and release schedules, while a new fraud technique can begin affecting a specific business immediately. 
 In practice, application-level detections often need to be updated before a platform-level mitigation is available. 
 Incognia can adapt its detections as new bypasses and attack patterns emerge, while continuing to incorporate the platform's protections. 
 Apple's new capabilities become additional inputs in this process, complementing the signals Incognia already uses to detect fraud. 
Gabriel Falcone

### Прочие ссылки (без извлечённого текста)

- <https://www.incognia.com>

## Контекст

<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_(пусто)_
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
_(пусто)_
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
