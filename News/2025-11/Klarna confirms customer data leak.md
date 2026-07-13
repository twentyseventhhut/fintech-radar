---
title: "Klarna confirms customer data leak"
date: 2025-11-06
tags:
  - company/klarna
  - industry/fraud-risk
  - industry/neobank
  - region/us
  - type/outage-security
sources:
  - https://www.businessinsider.com/klarna-data-leak-exposed-customer-logins-2025-11
  - https://www.forbes.com/sites/christerholloman/2025/11/05/klarna-confirms-potential-customer-data-leak-but-wont-reveal-extent
status: tagged
n_mentions: 2
channels:
  - "Connecting the Dots in Fintech"
story_id: s8ed923c9
month: 2025-11
enriched: false
---

# Klarna confirms customer data leak

> [!info] 2025-11-06 · 2 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Internal messages reveal how Klarna scrambled to fix a glitch that exposed customer data. Internal Slack messages, seen by Business Insider, show the Sweden-based company dealt with a problem caused by the absence of login protections for recycled phone numbers, when mobile carriers reassign a number after a previous owner gives it up.

[Connecting the Dots in Fintech] 🇺🇸 Klarna confirms potential customer data leak but won’t reveal extent. An error in its credit application form exposes what appears to be sensitive personal information belonging to other customers. The issue came to light when a customer noticed that several pages of their application form had been pre-filled with details apparently belonging to another user.

## Первоисточники

### businessinsider.com
<https://www.businessinsider.com/klarna-data-leak-exposed-customer-logins-2025-11>
*1322 слов · jina*

Klarna CEO Sebastian Siemiatkowski.Getty Images; Jenny Chang-Rodriguez/BI

A product director at buy-now, pay-later company Klarna estimated that as many as 288,000 customers' login details could be exposed in a data glitch, potentially costing the company up to $41.8 million, according to internal messages.

It turned out the impact wasn't as bad as initially estimated. A Klarna spokesperson told Business Insider that "the actual number of impacted accounts is estimated at more than ~99% lower than the initial theoretical scope" of 288,000.

Internal Slack messages, seen by Business Insider, show the Sweden-based company dealt with a problem caused by the absence of login protections for recycled phone numbers — when mobile carriers reassign a number after a previous owner gives it up.

When a new customer received one of these reused numbers and logged into Klarna's system, they could, in some cases, see a former account owner's details, a Klarna spokesperson explained.

"Klarna uses advanced systems and algorithms, including device fingerprinting, behavioral analysis, geolocation, and dynamic risk assessment, to detect recycled phone numbers," the spokesperson said. "These measures ensure that even in rare edge cases, we identify the vast majority of recycled phone numbers."

The glitch, which Business Insider learned has happened before, underscores the risk companies can face when holding confidential customer data. The internal communications reveal how Klarna has grappled with how to deal with the security issue.

The company said that as of Wednesday, the issue had been entirely resolved, with all verification methods now fully rolled out—including a one-time passcode (OTP) login, whereby a customer receives a unique code via email when they log in.

Where Big Tech secrets go public — unfiltered in your inbox weekly.

By clicking "Sign up", you agree to receive emails from Business Insider. In addition, you accept Insider’s Terms of Service and Privacy Policy.

"We have identified that information about this issue remained at working team levels longer than appropriate," a Klarna spokesperson said about the two-day gap between when the snafu happened and when it was rectified.

The customer data leak was first reported on Wednesday by Forbes, which spoke with a customer who began filling in a Klarna credit application form and found it already contained details that appeared to belong to another customer. Forbes said it verified the authenticity of the form and that it contained another person's full name, birth date, and address. A Klarna spokesperson told the outlet the issue was a "rare scenario" and that it is "not the result of a system-wide issue or a customer data breach."

Internal Slack messages told a different story.

On Monday, a Klarna product director wrote a Slack post containing an estimation of the financial impact of "not having proper Phone Recycle Protection." In the post, the director wrote that 288,000 customer logins could be exposed to unauthorized access.

In an email to Business Insider, Klarna said that the number was only "a starting point" for its investigation and "not a number of impacted individuals." It did not provide an exact number of customers affected.

Klarna projected an average legal and remediation cost of $1,000 per severe case, with the potential financial impact of $41.8 million, a Slack post written by Klarna's product director said.

The same Slack post also said of the affected accounts, "Out of them we estimate that roughly 10% of them are severe cases where new phone owners gain access to sensitive information such as Klarna Balance." Klarna Balance is a digital wallet that allows customers to store funds from their bank accounts and earn cash back.

In another Slack post this week summarizing the incident, Klarna detailed the cause of the issue.

"The incident involves a recycled phone number issue where a consumer who recently acquired a new phone number was automatically logged into a Klarna account belonging to the previous owner of that phone number. This allowed the consumer to view personal details of the previous account owner," the post said.

On Wednesday, Klarna greenlit employees to execute a full patch. A product director said in a Slack post that Klarna's chief product officer, David Fock, authorized a full rollout of the login policy change to add email OTP.

The messages also say Klarna was putting together a summary of what merchants can do about the issue, and they planned to share it with Fock and Klarna's chief operating officer, Camilla Giesecke.

"When our senior leadership team became aware of potential vulnerabilities related to phone number recycling, we took immediate action," the Klarna spokesperson told Business Insider.

## **Klarna grapples with the fallout**

Other internal messages, as seen by Business Insider, show that Klarna has been contending with how to roll out a fix for the recycled phone data leak issue and was concerned it would impact its sales.

Klarna's product team discussed adding email OTP login, rather than only a text message OTP login via phone, internal Slack messages from August showed.

Staffers said at the time in Slack messages that adding the additional verification measure would have a negative impact on the conversion ratio for merchants — meaning the number of visitors to a retail outlet who complete a sales transaction — because email OTP would be more time-consuming for customers than text message OTP.

In a November Slack message about the potential impact on the conversion rate, a data analytics manager said Klarna could see a drop amounting to a reduction in gross merchandise value of $28.5 million a month. The manager said that the amount "will not go unnoticed and will raise questions."

The manager also wrote that "we don't know the real number of recycled phone number cases" and questioned whether the company was confident the issue was serious enough to justify risking a potential drop in conversion rates in one of its key markets, the US.

He added that he is "not suggesting not to improve things" and would rather invest time and resources in improved login flows, rather than rolling out a change with such a high financial impact.

The manager said Klarna "concluded that we can't roll out the changes needed" because "the impact on these strategic partner[s] would just be too high."

Klarna said that it is continuing to investigate the issue thoroughly and "will report to the relevant regulatory authorities if required, which also includes notifying any potentially impacted consumers."

## **Klarna had similar data incidents in the past**

It's not the first time the issue has occurred.Support tickets from three years ago, which were seen by Business Insider, show similar incidents dating back to at least 2022.

In 2021, Klarna disclosed a data breach incident caused by a "faulty" change to its app, which exposed customers' information to other customers for a period of 31 minutes. In a separate incident, the company was fined about $733,000 in 2024 by a Swedish court for not giving users enough information about how it would store their personal data.

Klarna's share price has dropped by over 20% from its IPO opening price in September, when it went public on the New York Stock Exchange and raised about $1.37 billion.

Klarna says it has 111 million active consumers, with the vast majority of its business coming from zero-percent interest loans to customers that let them split payments for products and services from over 790,000 merchants, including Walmart, Nike, and Microsoft.

_Update: November 7, 2025 — This story has been updated to reflect that Klarna says it has 111 million active consumers and to clarify that the initial estimate of how many consumers might be affected was made by a product director in a Slack message._

_Have a tip? Contact this reporter via email at__jmann@businessinsider.com__or Signal at jyotimann.11. Use a personal email address and a nonwork device;_here's our guide to sharing information securely_._

## Read next

[](https://www.businessinsider.com/author/jyoti-mann)
Jyoti Mann

You're currently following this author! Want to unfollow? Unsubscribe via the link in your email.

*   Exclusive
*   Cybersecurity

### Прочие ссылки (без извлечённого текста)

- <https://www.forbes.com/sites/christerholloman/2025/11/05/klarna-confirms-potential-customer-data-leak-but-wont-reveal-extent>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
