---
title: "Stripe publishes analysis on first-party fraud across its network"
date: 2026-03-17
tags:
  - company/stripe
  - industry/fraud-risk
  - industry/ai
  - region/us
  - type/research-report
sources:
  - https://stripe.com/blog/analyzing-first-party-fraud-trends-account-free-trial-and-refund-abuse
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: se1de5f71
month: 2026-03
enriched: false
---

# Stripe publishes analysis on first-party fraud across its network

> [!info] 2026-03-17 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Stripe published new analysis this week on first-party fraud across its network. 7.4% of sign-ups at AI companies involve suspected multi-account abuse, with bad actors spinning up accounts to harvest free tiers and compute resources. AI startups with direct API access see 10x more attempted abuse than enterprise AI solutions. On the refund side, Stripe estimates global refund abuse losses at approximately $100 billion annually — with "wardrobing" running at 49% among Gen Z returners, and bad actors routinely using 100+ email variations across multiple payment cards to exploit no-questions-asked refund policies.

## Первоисточники

### stripe.com
<https://stripe.com/blog/analyzing-first-party-fraud-trends-account-free-trial-and-refund-abuse>
*1153 слов · direct*

From November 2025 to February 2026, we detected a significant increase in abusive free trials across Stripe’s network. 
This is part of a broader shift toward first-party fraud, where legitimate users abuse policies by setting up multiple accounts, cycling through free trials, or exploiting refunds. In fact, 62% of merchants have experienced an increase in disputes due to first-party fraud over the past year. Managing it costs businesses $35 for every $100 in disputes. 
Businesses facing these losses ask us the same questions: is first-party fraud increasing industry-wide as much as it is for my business? What can we do about it?
We analyzed hundreds of millions of transactions across the Stripe network to find answers. We identified three of the fastest growing types of first-party fraud, each occurring at a distinct point in the customer lifecycle: account abuse at sign-up, free trial abuse during product evaluation, and refund fraud after a customer has already received goods or services.
Here’s what we found about the prevalence of each and how Stripe Radar , our AI-powered fraud product, can help protect your business.  
Account abuse is especially costly for AI companies, where expensive compute costs are tied directly to usage
One in five consumers admit to using different email addresses or contact information to access promotions and discounts multiple times—rising to 29% of Gen Z and 27% of millennials, according to 451 Research’s Voice of the Connected User Landscape: Connected Customer, Trust and Privacy 2025 . This behavior, known as account abuse or multi-account abuse, occurs when a single person creates several accounts to repeatedly abuse free trials, use promotional coupons over and over again, or use their multiple accounts to spread stolen card use and avoid detection for longer. 
The fraud pattern forms a giant web with a single payment method identifier getting attached to dozens, if not hundreds, of emails, IP addresses, and names. 
Any business that offers something valuable—a free trial or a free perk with a new account—can be a target. But AI companies are particularly impacted.
Based on a Stripe analysis, 7.4% of customer sign-ups at AI companies are implicated in suspected multi-account abuse. AI tools run on compute resources, which makes multi-account abuse especially costly. Users might breach a business’s terms to create multiple accounts to get repeated access to free tiers or perks that come with new account sign-ups, such as free tokens. When a bad actor spins up five accounts instead of one, they consume five times the compute resources. 
In response, we are rolling out a new Radar feature to help you evaluate potential abuse during customer account registration and login events. You can see which new sign-ups are real customers, who might be likely to convert to a paid subscription, rather than fraudulent actors looking to repeatedly exploit new account perks. Sign up for early access. 
Free trial abuse is accelerating, driven by AI companies and the legitimate use of virtual cards
Free trials are necessary for customer evaluation, but they can be abused by users who violate common trial terms, such as cycling through multiple trials to get prolonged free access to a product or service. 
We found that this type of abuse is accelerating for two reasons: AI companies’ free trial acquisition strategies and the breakdown of traditional prevention methods that businesses have previously relied on.
 AI companies face acute exposure. Free trial abuse isn’t new, but AI companies are driving much of the increase we’re seeing today. These businesses run on expensive compute resources and rely on free trials to acquire customers, making them especially vulnerable to abuse. In fact, AI startups that offer free trials with self-serve sign-ups and direct API access see 10x more attempted abuse than enterprise AI solutions. 
 Traditional prevention methods no longer work. In an effort to reduce free trial abuse, businesses used to block high-risk payment methods such as virtual cards at sign-up. However, today, many virtual cards are legitimately used by customers for privacy and security. Blanket blocking them means rejecting legitimate sign-ups and hurting conversion rates. This leaves AI companies in a bind: they need free trials for customer acquisition, but those trials create financial exposure that traditional fraud tools weren’t designed to address.
Radar launched a new solution that predicts common free trial terms abuse with 90% accuracy. We also introduced a new analytics page that shows all high-risk payments that are blocked. For businesses that have not yet enabled the control, we show which payments would have been blocked if you had turned it on. Email us at trial-abuse-prevention@stripe.com for early access. 
Refund abuse costs businesses worldwide $100 billion each year 
Many retailers offer generous refund policies to stay competitive and improve the customer experience. However, lenient policies can be abused, with customers falsely claiming items never arrived or are defective in order to receive a refund—and keep the product. It’s an expensive problem: we estimate that global losses from refund abuse reach approximately $100 billion each year. 
Customers might buy expensive clothing, wear it for a short time, and then return it—behavior known as “wardrobing.” According to the National Retail Federation’s 2025 Retail Returns Landscape report , 27% of shoppers that returned at least 1 online purchase in a 12-month period admitted to wardrobing, and that increased to 49% for Gen Z shoppers. 
Retailers tell us that social media has amplified this behavior: influencers might purchase large shopping hauls for content and then return the clothes once the video is created. Retailers absorb the cost on both ends—two-way shipping, processing fees, and markdowns on items they may no longer be able to sell as new.
There are also more sophisticated operations. We’ve seen bad actors use more than 100 email variations and multiple payment cards to systematically exploit refund policies, such as “no questions asked” refund policies. When retailers implement refund limits, like charging a fee for frequent returns, these bad actors simply create new accounts with different cards to bypass the restrictions.
In both cases, there are real customers with valid payment credentials making genuine purchases. This makes it very difficult to detect refund abuse at the point of transaction; the fraud only becomes apparent later, once the refund is processed.
We are actively building solutions to help businesses identify and prevent refund abuse. Please contact us at refund-abuse-prevention@stripe.com to be part of the preview for this feature. 
What we’re building to help
Our goal is to equip businesses on Stripe with tools to identify, reduce, and monitor first-party fraud and abuse. We process billions of transactions across millions of businesses, which gives us visibility into comprehensive fraud patterns, such as repeat abusers, networks of fake accounts, and emerging tactics. We plan to continue using our existing AI infrastructure and Radar’s capabilities to extend fraud protection to first-party fraud. 
To hear more about how Radar is adapting to additional fraud and abuse vectors, join us at Stripe Sessions .

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
