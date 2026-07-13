---
title: "Figure data breach exposes nearly 1 million accounts"
date: 2026-02-13
tags:
  - company/figure
  - industry/lending
  - industry/fraud-risk
  - region/us
  - type/outage-security
sources:
  - https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft
  - https://securityaffairs.com/187988/data-breach/fintech-firm-figure-disclosed-data-breach-after-employee-phishing-attack.html
  - https://databreach.com/breach/figure-technology-solutions-2026
  - https://techcrunch.com/2026/02/13/fintech-lending-giant-figure-confirms-data-breach
  - https://www.finextra.com/newsarticle/47327/figure-technology-data-breach-hits-nearly-1-million-accounts
status: tagged
n_mentions: 7
channels:
  - "Connecting the Dots in Fintech"
  - "TechCrunch — Fintech"
  - "This Week in Fintech"
story_id: s2506954d
month: 2026-02
enriched: false
---

# Figure data breach exposes nearly 1 million accounts

> [!info] 2026-02-13 · 7 упоминаний · 3 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, TechCrunch — Fintech, This Week in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 FinTech lending giant Figure confirms data breach. The company said it is notifying affected partners and individuals and offering free credit monitoring. The hacking group ShinyHunters claimed responsibility and has reportedly published 2.5GB of stolen data after Figure refused to pay a ransom.

[TechCrunch — Fintech] A member of ShinyHunters told TechCrunch that Figure was among the victims of a hacking campaign that targeted customers who rely on the single sign-on provider Okta. Other victims of the campaign include Harvard University and the University of Pennsylvania (UPenn).

[This Week in Fintech] Figure Technology suffered a major data breach that compromised the personal information of nearly 1 million user accounts.

[This Week in Fintech] On February 13th,Figure confirmed a data breach after an employee fell victim to a voice phishing (vishing) attack. The attacker impersonated IT support, tricked the employee into surrendering their Okta single sign-on credentials, and used a real-time Adversary-in-the-Middle (AiTM) phishing kit to bypass multi-factor authentication entirely. ShinyHunters, one of the most prolific ransomware groups operating today, published roughly 2.5 gigabytes of stolen data after Figure refused to pay the ransom demand.

[This Week in Fintech] The damage:nearly one million records exposed, enough PII to fuel identity theft, phishing campaigns, and synthetic identity fraud for years.

[This Week in Fintech]

## Первоисточники

### cloud.google.com
<https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft>
*1675 слов · direct*

Vishing for Access: Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft 
 
 
 
 

Visibility and context on the threats that matter most.
 Introduction   
 Mandiant has identified an expansion in threat activity that uses tactics, techniques, and procedures (TTPs) consistent with prior ShinyHunters-branded extortion operations. These operations primarily leverage sophisticated voice phishing (vishing) and victim-branded credential harvesting sites to gain initial access to corporate environments by obtaining single sign-on (SSO) credentials and multi-factor authentication (MFA) codes. Once inside, the threat actors target cloud-based software-as-a-service (SaaS) applications to exfiltrate sensitive data and internal communications for use in subsequent extortion demands. 
 Google Threat Intelligence Group (GTIG) is currently tracking this activity under multiple threat clusters (UNC6661, UNC6671, and UNC6240 ) to enable a more granular understanding of evolving partnerships and account for potential impersonation activity. While this methodology of targeting identity providers and SaaS platforms is consistent with our prior observations of threat activity preceding ShinyHunters-branded extortion, the breadth of targeted cloud platforms continues to expand as these threat actors seek more sensitive data for extortion. Further, they appear to be escalating their extortion tactics with recent incidents including harassment of victim personnel, among other tactics . 
 This activity is not the result of a security vulnerability in vendors' products or infrastructure. Instead, it continues to highlight the effectiveness of social engineering and underscores the importance of organizations moving towards phishing-resistant MFA where possible. Methods such as FIDO2 security keys or passkeys are resistant to social engineering in ways that push-based or SMS authentication are not. 
 Mandiant has also published a comprehensive guide with proactive hardening and detection recommendations , and Google published a detailed walkthrough for operationalizing these findings within Google Security Operations. 
Figure 1: Attack path diagram
 UNC6661 Vishing and Credential Theft Activity 
 In incidents spanning early to mid-January 2026, UNC6661 pretended to be IT staff and called employees at targeted victim organizations claiming that the company was updating MFA settings. The threat actor directed the employees to victim-branded credential harvesting sites to capture their SSO credentials and MFA codes, and then registered their own device for MFA. The credential harvesting domains attributed to UNC6661 commonly, but not exclusively, use the format <companyname>sso.com or <companyname>internal.com and have often been registered with NICENIC. 
 In at least some cases, the threat actor gained access to accounts belonging to Okta customers. Okta published a report about phishing kits targeting identity providers and cryptocurrency platforms, as well as follow-on vishing attacks. While they associate this activity with multiple threat clusters, at least some of the activity appears to overlap with the ShinyHunters-branded operations tracked by GTIG. 
 After gaining initial access, UNC6661 moved laterally through victim customer environments to exfiltrate data from various SaaS platforms (log examples in Figures 2 through 5). While the targeting of specific organizations and user identities is deliberate, analysis suggests that the subsequent access to these platforms is likely opportunistic, determined by the specific permissions and applications accessible via the individual compromised SSO session. These compromises did not result from security vulnerabilities in the vendors' products or infrastructure. 
 In some cases, they have appeared to target specific types of information. For example, the threat actors have conducted searches in cloud applications for documents containing specific text including "poc," "confidential," "internal," "proposal," "salesforce," and "vpn" or targeted personally identifiable information (PII) stored in Salesforce. Additionally, UNC6661 may have targeted Slack data at some victims' environments, based on a claim made in a ShinyHunters-branded data leak site (DLS) entry. 
 Figure 2: SharePoint/M365 log example 
 Figure 3: Salesforce log example 
 Figure 4: Docusign log example 
 In at least one incident where the threat actor gained access to an Okta customer account, UNC6661 enabled the ToogleBox Recall add-on for the victim's Google Workspace account, a tool designed to search for and permanently delete emails. They then deleted a "Security method enrolled" email from Okta, almost certainly to prevent the employee from identifying that their account was associated with a new MFA device. 
 Figure 5: ToogleBox Recall auth log entry example 
 In at least one case, after conducting the initial data theft, UNC6661 used their newly obtained access to compromised email accounts to send additional phishing emails to contacts at cryptocurrency-focused companies. The threat actor then deleted the outbound emails, likely in an attempt to obfuscate their malicious activity. 
 GTIG attributes the subsequent extortion activity following UNC6661 intrusions to UNC6240 , based on several overlaps, including the use of a common Tox account for negotiations, ShinyHunters-branded extortion emails, and Limewire to host samples of stolen data. In mid-January 2026 extortion emails, UNC6240 outlined what data they allegedly stole, specifying a payment amount and destination BTC address, and threatening consequences if the ransom was not paid within 72 hours, which is consistent with prior extortion emails (Figure 6). They also provided proof of data theft via samples hosted on Limewire. GTIG also observed extortion text messages sent to employees and received reports of victim websites being targeted with distributed denial-of-service (DDoS) attacks. 
 Notably, in late January 2026 a new ShinyHunters-branded DLS named "SHINYHUNTERS" emerged listing several alleged victims who may have been compromised in these most recent extortion operations. The DLS also lists contact information (shinycorp@tutanota[.]com, shinygroup@onionmail[.]com) that have previously been associated with UNC6240. 
Figure 6: Ransom note extract
 Similar Activity Conducted by UNC6671 
 Also beginning in early January 2026, UNC6671 conducted vishing operations masquerading as IT staff and directing victims to enter their credentials and MFA authentication codes on a victim-branded credential harvesting site. The credential harvesting domains used the same structure as UNC6661, but were more often registered using Tucows. In at least some cases, the threat actors have gained access to Okta customer accounts. Mandiant has also observed evidence that UNC6671 leveraged PowerShell to download sensitive data from SharePoint and OneDrive. While many of these TTPs are consistent with UNC6661, an extortion email stemming from UNC6671 activity was unbranded and used a different Tox ID for further contact. The threat actors employed aggressive extortion tactics following UNC6671 intrusions, including harassment of victim personnel. The extortion tactics and difference in domain registrars suggests that separate individuals may be involved with these sets of activity . 
 Remediation and Hardening 
 Mandiant has published a comprehensive guide with proactive hardening and detection recommendations . 
 Outlook and Implications 
 This recent activity is similar to prior operations associated with UNC6240, which have frequently used vishing for initial access and have targeted Salesforce data . It does, however, represent an expansion in the number and type of targeted cloud platforms, suggesting that the associated threat actors are modifying their operations to gather more sensitive data for extortion operations. Further, the use of a compromised account to send phishing emails to cryptocurrency-related entities suggests that associated threat actors may be building relationships with potential victims to expand their access or engage in other follow-on operations. Notably, this portion of the activity appears operationally distinct, given that it appears to target individuals instead of organizations. 
 Indicators of Compromise (IOCs) 
 To assist the wider community in hunting and identifying activity outlined in this blog post, we have included indicators of compromise (IOCs) in a free GTI Collection for registered users. 
 Phishing Domain Lure Patterns  
 Threat actors associated with these clusters frequently register domains designed to impersonate legitimate corporate portals. At time of publication all identified phishing domains have been added to Chrome Safe Browsing . These domains typically follow specific naming conventions using a variation of the organization name: 
 Pattern 
 Examples (Defanged) 
 Corporate SSO 
 <companyname>sso[.]com, my<companyname>sso[.]com, my-<companyname>sso[.]com 
 Internal Portals 
 <companyname>internal[.]com, www.<companyname>internal[.]com, my<companyname>internal[.]com 
 Support/Helpdesk 
 <companyname>support[.]com, ticket-<companyname>[.]support, support-<companyname>[.]com 
 Identity Providers 
 <companyname>okta[.]com, <companyname>azure[.]com, on<companyname>zendesk[.]com 
 Access Portal 
 <companyname>access[.]com, www.<companyname>access[.]com, my<companyname>acess[.]com 
 Network Indicators 
 Many of the network indicators identified in this campaign are associated with commercial VPN services or residential proxy networks, including Mullvad, Oxylabs, NetNut, 9Proxy, Infatica, and nsocks. Mandiant recommends that organizations exercise caution when using these indicators for broad blocking and prioritize them for hunting and correlation within their environments. 
 IOC 
 ASN 
 Association 
 24.242.93[.]122 
 11427 
 UNC6661 
 23.234.100[.]107 
 11878 
 UNC6661 
 23.234.100[.]235 
 11878 
 UNC6661 
 73.135.228[.]98 
 33657 
 UNC6661 
 157.131.172[.]74 
 46375 
 UNC6661 
 149.50.97[.]144 
 201814 
 UNC6661 
 67.21.178[.]234 
 400595 
 UNC6661 
 142.127.171[.]133 
 577 
 UNC6671 
 76.64.54[.]159 
 577 
 UNC6671 
 76.70.74[.]63 
 577 
 UNC6671 
 206.170.208[.]23 
 7018 
 UNC6671 
 68.73.213[.]196 
 7018 
 UNC6671 
 37.15.73[.]132 
 12479 
 UNC6671 
 104.32.172[.]247 
 20001 
 UNC6671 
 85.238.66[.]242 
 20845 
 UNC6671 
 199.127.61[.]200 
 23470 
 UNC6671 
 209.222.98[.]200 
 23470 
 UNC6671 
 38.190.138[.]239 
 27924 
 UNC6671 
 198.52.166[.]197 
 395965 
 UNC6671 
 Google Security Operations 
 Google Security Operations customers have access to these broad category rules and more under the Okta, Cloud Hacktool, and O365 rule packs. A walkthrough for operationalizing these findings within the Google Security Operations is available in Part Three of this series. The activity discussed in the blog post is detected in Google Security Operations under the rule names: 

 Okta Admin Console Access Failure 


 Okta Super or Organization Admin Access Granted 


 Okta Suspicious Actions from Anonymized IP 


 Okta User Assigned Administrator Role 


 O365 SharePoint Bulk File Access or Download via PowerShell 


 O365 SharePoint High Volume File Access Events 


 O365 SharePoint High Volume File Download Events 


 O365 Sharepoint Query for Proprietary or Privileged Information 


 O365 Deletion of MFA Modification Notification Email 


 Workspace ToogleBox Recall OAuth Application Authorized 

 Figure 7: Hunting query for suspicious Okta actions conducted from anonymized IPs 
 Figure 8: Hunting query for Google Workspace authorization events for ToogleBox Recall 
 Figure 9: Hunting query for suspicious VPN / proxy services observed in this campaign 
 Figure 10: Hunting query for suspicious user-agent string observed in this campaign 
 Figure 11: Hunting query for programmatic file access or downloads from SharePoint where the User-Agent identifies as PowerShell 
 Figure 12: Hunting query for high volume document file access from SharePoint 
 Figure 13: Hunting query for high volume document file downloads from SharePoint 
 Figure 14: Hunting query for SharePoint queries for strings of interest 
 Figure 15: Hunting query for O365 Exchange deletion of MFA modification notification email 
 Threat Intelligence 
ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit
By Mandiant • 12-minute read
Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms
By Mandiant • 19-minute read
Exploitation of KnowledgeDeliver via ViewState Deserialization Vulnerability
By Mandiant • 7-minute read
2 PhaaS 2 Furious: The Evolution of Chinese-Language Phishing Services
By Google Threat Intelligence Group • 7-minute read

### securityaffairs.com
<https://securityaffairs.com/187988/data-breach/fintech-firm-figure-disclosed-data-breach-after-employee-phishing-attack.html>
*371 слов · direct*

Home 
 Breaking News 
 Cyber Crime 
 Data Breach 
 Hacking 
Fintech firm Figure disclosed data breach after employee phishing attack
Fintech firm Figure disclosed data breach after employee phishing attack
Fintech firm Figure confirmed a data breach after hackers used social engineering to trick an employee and steal a limited number of files.
Blockchain-based lending firm Figure confirmed a data breach after an employee fell victim to a social engineering attack. According to a company spokesperson, the incident allowed hackers to access and steal a limited number of files. The company disclosed the breach following inquiries and is assessing the impact.
Figure Technology Solutions, Inc. is a US financial technology company. Established in 2018, it develops and operates blockchain-based platforms used in lending, capital markets, and asset management.
The company offers consumer and institutional lending products such as HELOCs, cash-out refinancing, DSCR loans, crypto-backed loans, and operates the Figure Connect credit marketplace.
On Friday, Figure spokesperson Alethea Jadick told TechCrunch that the security breach occurred after an employee was tricked in a social engineering attack, allowing hackers to steal “a limited number of files.” She said the company is communicating “with partners and those impacted” and offering free credit monitoring “to all individuals who receive a notice.” 
Figure has started notifying affected individuals and is offering free credit monitoring to those who receive a breach notice. The company has not shared the number of impacted users or when the breach was discovered. 
The cybercrime group ShinyHunters claimed responsibility for the breach on its dark web site, saying Figure refused to pay a ransom and releasing about 2.5GB of stolen data. 
TechCrunch reviewed samples showing names, addresses, birth dates, and phone numbers, raising risks of identity fraud and phishing.
 “A member of ShinyHunters told TechCrunch that Figure was among the victims of  a hacking campaign  that targeted customers who rely on the single sign-on provider Okta.” reported TechCruch. 
 Follow me on Twitter:  @securityaffairs  and  Facebook  and  Mastodon 
 Pierluigi Paganini 
 ( SecurityAffairs  – hacking, data breach) 
you might also like
leave a comment
newsletter

recent articles
 Breaking News / June 14, 2026
 Security / June 14, 2026
 Uncategorized / June 14, 2026
 Artificial Intelligence / June 13, 2026
 Security / June 13, 2026
Privacy Overview

### databreach.com
<https://databreach.com/breach/figure-technology-solutions-2026>
*250 слов · jina*

In February 2026, Figure Technology Solutions, a leading fintech firm known for its blockchain-based Home Equity Lines of Credit (HELOCs), confirmed it fell victim to a targeted social engineering attack.

The incident occurred after a single employee was manipulated into providing access to their credentials, allowing a threat actor to bypass internal security perimeters. The breach has been linked to a wider campaign by the notorious hacking group ShinyHunters, which specifically targeted organizations utilizing Okta for single sign-on services.

According to data parsed from the subsequent leak, the breach exposed nearly 1 million records of sensitive personally identifiable information (PII). The exfiltrated dataset includes 1,004,503 dates of birth, 991,777 email addresses, and 941,184 physical street addresses. Additionally, over 925,588 phone numbers and 807,644 full names were compromised. While Figure has stated that customer funds and passwords remained secure, the sheer volume of contact and identity data published on the dark web after the company refused ransom demands poses a significant risk for secondary phishing and identity theft.

In response to the disclosure, Figure blocked the compromised account and engaged a third-party forensic firm to conduct a comprehensive audit of the accessed files.

The company is currently in the process of notifying affected partners and customers, offering complimentary credit monitoring services to those whose data was part of the 2.5 GB leak. Despite the security lapse, Figure’s leadership maintained that its core blockchain infrastructure remained intact, framing the event as a failure of human-centric security rather than a systemic technical flaw.

### Прочие ссылки (без извлечённого текста)

- <https://techcrunch.com/2026/02/13/fintech-lending-giant-figure-confirms-data-breach>
- <https://www.finextra.com/newsarticle/47327/figure-technology-data-breach-hits-nearly-1-million-accounts>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
