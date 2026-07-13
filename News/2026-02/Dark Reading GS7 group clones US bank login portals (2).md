---
title: "Dark Reading: GS7 group clones US bank login portals"
date: 2026-02-19
tags:
  - industry/fraud-risk
  - industry/banking
  - region/us
  - type/outage-security
sources:
  - https://www.darkreading.com/cyberattacks-data-breaches/operation-doppelbrand-weaponizing-fortune-500-brands
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sc6eeaa05
month: 2026-02
enriched: false
---

# Dark Reading: GS7 group clones US bank login portals

> [!info] 2026-02-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Dark Reading reported this week onOperation DoppelBrand, a campaign by the GS7 cyberthreat group deploying near-perfect imitations of U.S. financial institution login portals. These aren't phishing emails with typos. These are pixel-perfect clones of major bank portals hosted on lookalike domains, designed to steal credentials and establish remote access.

## Первоисточники

### darkreading.com
<https://www.darkreading.com/cyberattacks-data-breaches/operation-doppelbrand-weaponizing-fortune-500-brands>
*796 слов · jina*

3 Min Read

_Thomas_Bethge_Alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Thomas Bethge via Alamy Stock Photo

An elusive, financially motivated threat actor dubbed GS7 has been targeting Fortune 500 companies in a broad phishing campaign that turns the company's own brands against them with impersonated websites aimed at harvesting credentials.

The campaign — dubbed Operation DoppelBrand — is ongoing, first observed between December and January. The group itself, however, has a history stretching back to 2022, according to a white paper by SOCRadar published today.

The campaign targets top financial institutions — including Wells Fargo, USAA, Navy Federal Credit Union, Fidelity Investments, and Citibank — as well as technology, healthcare, and telecommunications firms worldwide.

The secret to the success of Operation DoppelBrand is a sophisticated phishing infrastructure consistently rotated by GS7 and constructed to mimic legitimate login portals, replicating official branding with unprecedented accuracy. This makes it difficult for victims to spot the scam, according to SOCRadar.

Related:Chinese, N. Korean Threat Groups Build on Asia-Pacific Success

The scam requires significant work on the front end, to choose targets and construct convincing pages, as well as preparing the infrastructure to mount the attacks, according to the researchers. In fact, the threat actor registered more than 150 malicious domains in recent months alone, using registrars such as NameCheap and OwnRegistrar, and routing traffic through Cloudflare to obscure back-end servers.

## Evolving Initial Access Broker Activity?

Once collected, login credentials — including usernames and passwords, IP addresses and geolocation data, device and browser fingerprints, and timestamps — are immediately exfiltrated to attacker-controlled Telegram bots. The researchers identified a Telegram group titled "NfResultz by GS" that they believe is operated by the group.

GS7's end game includes not only harvesting credentials, but also downloading remote management and monitoring (RMM) tools on victim systems to enable remote access or the deployment of malware. In fact, SOCRadar believes the group may even act as an initial access broker (IAB), selling access to infrastructure to ransomware groups or other affiliates.

## Targeting English Speakers for Credential Theft

GS7 primarily has focused on English-speaking markets in recent months, with the US being the largest target, by far. Meanwhile, the group also is expanding and maintaining DoppelBrand activity in Europe and other regions.

The threat actor in general targets Fortune 500 and other "high-value entities" with a broad geographic reach. "In recent attacks, assets, domains, and records associated with different companies operating in very diverse sectors and locations have been identified," according to the white paper.

Related:Silent Ransom Group Hits US Law Firms in Escalating Extortion Attacks

Someone claiming to be a member of GS7 told SOCRadar researchers that the group has operated for nearly a decade, and provided screenshots of phishing panels signed with the group's handle as proof of its long-time activity, according to the white paper. The individual also gave a phishing demonstration with a portal mimicking Fidelity, which resulted in the download of RMM tools once the log-in form was completed.

The researchers did not say where the group is based, though they did uncover links between GS7 and Brazilian cybercrime forums where stolen credentials and financial data were traded. "These venues represent key locations for selling harvested information or acquiring data to fuel further campaigns," according to the white paper.

## Phishing Continues to Evolve

Given that GS7 has remained active for years and amassed a significant infrastructure for its phishing operation without security researchers noticing until now is a testament to the continued sophistication of organized phishing operations.

GS7's particularly convincing brand impersonation makes its phishing pages difficult to spot, but people should be careful to take steps to ensure that it's the authentic site when they log into their financial institution's homepage. They can do this by setting up multifactor authentication (MFA) and practicing safe online behavior in general.

Related:Iran Signed a Ceasefire — Its Hackers Didn't

To help defenders track Operation DoppelBrand and GS7's activities, SOCRadar provided an extensive list of tactics, techniques, and procedures (TTPs) and indicators of compromise (IoCs) for both the campaign and the group in its white paper.

## About the Author

[](https://www.darkreading.com/author/elizabeth-montalbano)

Contributing Writer

Elizabeth Montalbano is freelance writer, editor, and journalist with 30 years of professional experience and a master's degree from Arizona State University. Her areas of expertise include enterprise technology, cybersecurity, business, and culture. During her long career, Elizabeth has lived and worked as a full-time journalist in Phoenix, San Francisco, and New York City. She specializes in news coverage and analysis, using her years of experience to look at the current state of cybersecurity with a critical gaze. She currently resides in a village on the southwest coast of Portugal, where in her free time she enjoys surfing, hiking with her dogs, growing plants, and playing and performing as a singer and musician.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
