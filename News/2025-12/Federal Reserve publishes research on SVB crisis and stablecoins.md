---
title: "Federal Reserve publishes research on SVB crisis and stablecoins"
date: 2025-12-19
tags:
  - company/federal-reserve
  - industry/stablecoins
  - industry/banking
  - region/us
  - type/research-report
sources:
  - https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sca3799b8
month: 2025-12
enriched: false
---

# Federal Reserve publishes research on SVB crisis and stablecoins

> [!info] 2025-12-19 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] The Federal Reserve also published some really interesting research this week on the Silicon Valley Bank crisis and its impact on stablecoins.

## Первоисточники

### federalreserve.gov
<https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html>
*2149 слов · direct*

An official website of the United States Government
 Official websites use .gov A .gov website belongs to an official government organization in the United States.
 Secure .gov websites use HTTPS A lock ( Lock Locked padlock icon ) or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.

 Stay Connected 
 
 
 
 
 Federal Reserve Facebook Page 
 

 
 
 Federal Reserve Instagram Page 
 

 
 
 Federal Reserve YouTube Page 
 

 
 
 Federal Reserve Flickr Page 
 

 
 
 Federal Reserve LinkedIn Page 
 

 
 
 Federal Reserve Threads Page 
 

 
 
 Federal Reserve X Page 
 

 
 
 Federal Reserve Bluesky Page 
 

 
 
 Subscribe to RSS 
 

 
 
 Subscribe to Email 
 

 Recent Postings 
 

 Calendar 
 

 Publications 
 

 Site Map 
 

 A-Z index 
 

 Careers 
 

 FAQs 
 

 Videos 
 

 Contact 
 
 Home 
 Economic Research 
 FEDS Notes 
 2025 
FEDS Notes

 
 
 
 
 

 
 
 
 
 

 
 
 
 
 

 
 
 
 
 
December 17, 2025
In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins
 Chuan Du , Ria Sonawane , and Cy Watsky 
Summary
Stablecoins are crypto-assets designed to maintain a stable value against a reference asset, typically the U.S. Dollar. The peg to the dollar is supported by the assets that back the stablecoin. Stablecoins perform dollar-like functions in decentralized finance ("DeFi") and represent a run-able liability for their issuers. As with money market funds and bank deposits, stablecoins are susceptible to crises of confidence, contagion, and self-reinforcing runs.
In this note we utilize a granular dataset to document the market stress experienced by USDC, the second largest stablecoin by market cap, during the Silicon Valley Bank ("SVB") crisis of March 2023. SVB was a traditional bank that failed due to inadequate risk management practices. 1 The bank experienced a rapid run of deposits and was taken into receivership by the Federal Deposit Insurance Corporation ("FDIC").
Shortly after, Circle, the issuer of USDC, publicly announced that it was unable to access a portion of its dollar reserves held as (uninsured) deposits at SVB. This announcement precipitated a surge in redemption requests by holders of USDC, causing the stablecoin to lose its peg against the dollar on secondary markets when Circle shut down primary market operations over the weekend.
We identify a key channel of contagion in the DeFi sector, illustrative of the potential for code-based financial products to amplify stress. At the same time during the resolution of SVB, a crypto-collateralized stablecoin, Dai, was operating one-to-one exchange facilities — called Peg Stability Modules ("PSMs") — against USDC and other stablecoins. 2 Over the weekend, these PSMs were rapidly drained of liquidity. Dai, and other stablecoins with otherwise no exposure to SVB, also lost their peg to the dollar. Both the SVB run and the stablecoins depegs were ameliorated when the FDIC, the Treasury Department, and the Federal Reserve Board jointly announced that all depositors in SVB would be fully protected.
We highlight three aspects of this USDC depeg episode.
First, there is a potential for two-way feedback between the traditional and the DeFi sectors. In this event, the run on SVB was the trigger for the USDC depeg, which then sparked a broader sell-off in other stablecoins. Intervention designed to backstop SVB stemmed the selling pressure on the affected stablecoins while the USDC primary market was closed. But had the run unfolded differently, the pressure for USDC redemptions might have forced Circle to liquidate backing assets (for example, U.S.Treasury securities), with potential knock-on effects on traditional financial markets.
Second, while stablecoins with high quality backing assets can maintain their pegs during normal times, they may still be fragile during periods of significant stress. When stablecoins lose their peg against the dollar, the effect can reverberate through the sector.
Third, smart contracts, such as the one-to-one exchange facilities backing Dai, can create interlinkages between DeFi participants. Such facilities can be created at the discretion of any individual participant and operate autonomously. Without appropriate consideration of the risks posed to the wider ecosystem, these interlinkages can channel and amplify contagion.
This paper provides a detailed account of how SVB's failure affected USDC and other stablecoins during March 2023. Our account is backed by granular data on both the primary and secondary market activities of the affected stablecoins.
Policy discussions relating to the design of stablecoin regulations are outside of the scope of our study.
Future research should explore relevant counterfactuals and other instances of pressure in stablecoin markets to better understand how the traditional and DeFi markets interact during periods of significant stress. Further studies are particularly important as stablecoins continue to expand their role in the economy.
1. The Run on SVB and its implications for USDC
On the morning of Friday, March 10, 2023, Silicon Valley Bank ("SVB") entered bank resolution after experiencing over $40 billion in withdrawals from depositors in a single day. 3 At 10 p.m. on Friday evening, Circle announced that it was unable to withdraw $3.3 billion of USDC reserves from SVB (around 8% of total reserves at the time), sparking a wave of redemption requests for the stablecoin. 4 
Solvency concerns around Circle are likely to have played a part. As a private company at the time, Circle was not subject to public disclosure requirements; however, subsequent filing with the Securities and Exchange Commission on April 1, 2025, stated that Circle's total stockholders' equity as of December 31, 2023, was $0.34 billion, representing just over a tenth of the $3.3 billion reserves held at SVB. 5 * Without a public guarantee on the uninsured deposits at SVB, Circle faced the possibility of a significant shortfall.
Solvency concerns can morph and extend into liquidity concerns. Redemption requests in the primary market for USDC rose sharply after the announcement that SVB was taken into receivership, ahead of Circle's public acknowledgment that it was unable to access deposits at SVB. Suspension of primary market redemptions over the ensuing weekend contributed to selling pressure on USDC in the secondary markets, triggering a depeg against the U.S. dollar in the secondary market. Public reassurances from Circle that it would "stand behind USDC and cover any shortfall using corporate resources, involving external capital if necessary," may have helped to shore up the price of USDC during the weekend, but were not sufficient to restore the peg. 6 
 1.1 Primary Market Shutdown 
Our granular dataset allows us to analyze the market dynamics during the SVB episode in great detail. 7 Figure 1 tracks the hourly net issuance of USDC on its primary market (bars), overlaid on top of the secondary market price of USDC (line), from Thursday, March 9 to Tuesday, March 14, 2023. Event lines indicate the timing of major public announcements related to the episode.
The bars indicate significant USDC redemptions after SVB was taken into receivership at 11:37 a.m. ET on Friday, March 10, even before Circle's public announcement around 10 p.m. that same day. Redemptions peaked shortly before this announcement, then dropped to minimal levels over the weekend, as Circle announced that issuance and redemptions were "constrained by working hours of the U.S. banking systems." 8 
The selloffs translated into a dramatic depeg when Circle publicly tweeted about its exposure to SVB and the primary market largely ceased operations (as shown by the line). At its trough, USDC traded at 86 cents to the dollar. 9 Public commitment from Circle, to stand behind USDC using "external capital," on Saturday, March 11 provided price support but did not restore the peg.
The "resolution weekend" for SVB culminated in a joint press release by the Department of the Treasury, the Federal Reserve Board, and the FDIC at 6:15 p.m. ET, Sunday, March 12, 2023. The press release announced that the Federal Reserve "will make available additional funding to eligible depository institutions to help assure banks have the ability to meet the needs of all their (insured and uninsured) depositors." USDC's price on the secondary market recovered sharply after the backstop announcement on Sunday and fully recovered once Circle began processing redemptions on Monday, March 13.
On Wednesday, March 15 Circle announced: "we have cleared substantially all of the backlog of minting and redemption requests for USDC" and "continue making progress toward full USDC liquidity operations [...] Since Monday morning, Circle has redeemed $3.8 billion in USDC and minted $0.8 billion USDC." 10 
The timing of both primary market redemptions and secondary market price dislocation confirm predictable but insightful facts about stablecoin markets. 11 First, traders responded rapidly to news about SVB, and redemptions increased quickly following this information. Second, primary market activity clearly mattered for USDC's price on secondary markets. It wasn't until primary markets shut down that USDC's hit its low point, and it wasn't until Circle began processing redemptions again that USDC returned to its peg. Third, information asymmetry may have played a role. Some (possibly more informed) traders ran ahead of Circle's own announcement on Friday, while others followed afterwards.
 1.2 Secondary Market Activity 
Unlike bank deposits, stablecoins are actively traded on exchanges in the secondary markets. This means that the suspension of redemption on the primary market cannot arrest a run, as temporarily closing a bank would. USDC trading activity on its secondary market during the resolution weekend offers an additional window into the potential dynamics of a stablecoin run. 12 
Trading volumes on the secondary markets for USDC were highly elevated throughout the episode – especially during the suspension of the primary market. Pent up redemption pressure was reflected in a surge of trading on centralized and decentralized exchanges. Hourly trading volume shot up to nearly $2 billion on March 11, triggering the sharp price dislocation of USDC against the dollar.
Figure 2 plots the trading volume of USDC on the secondary markets, decomposed into activity on decentralized exchanges (“DEXs”) and centralized exchanges (“CEXs”). Though centralized exchanges tend to handle a higher volume of crypto-asset trading activity than decentralized exchanges during normal times; during the crisis, trading on DEXs rose dramatically and accounted for most of the activity. 13 
As we see in Figure 2, trading volumes on secondary markets also increased in the run up to Circle's Friday announcement, mirroring the primary market trend. This suggests some traders were sensitive towards potential issues with respect to USDC and began exiting USDC positions in advance of the public announcement.
2. The contagion to Dai: A DeFi transmission channel
Like bank runs, stress originating in one stablecoin can spillover to other industry participants. Such contagion can be direct, for example, through explicit interlinkages, or indirect, for example, through a crisis of confidence. Most episodes exhibit elements of both.
We highlight the direct contagion from USDC to a crypto-backed “stablecoin", Dai. 14 The issuer of Dai, MakerDAO, operates a set of smart-contract-based collateralized lending facilities issuing Dai tokens in return for crypto collateral. 15 One such facility, named the Dai-USDC Peg Stability Module ("USDC-PSM"), allowed users to exchange between Dai and USDC on a one-to-one basis, and was designed to stabilize Dai's price at one dollar by explicitly pegging Dai to USDC. While this mechanism worked in normal times, during the SVB crisis the PSM became an escape valve for USDC holders and triggered simultaneous selling pressures on both stablecoins.
 2.1 Escaping through the USDC-PSM 
As Circle halted its primary market transactions over the resolution weekend, and exchanges stopped accepting USDC at par, the USDC-PSM became an attractive way for traders to exit their USDC positions. 16 The PSM's hard-coded smart contracts continued to accept USDC on a one-for-one basis against Dai. The only safeguard was a 950 million USDC daily cap built into the facility.
As the bottom panel of Figure 3 illustrates, the volume of minting activity in the PSM shot up on Friday, March 10, and the 950 million daily cap was swiftly reached. Activity in the PSM strongly correlated with the increase in USDC trading volumes on exchanges in the run-up to Circle's announcement, reflecting the fact that the PSM was well integrated into secondary markets. Many centralized and decentralized exchanges used automated processes to search for the most favorable price for those seeking to exit USDC positions.
Trading through the PSM resumed on Saturday, March 11, but quickly shut down again once the daily cap was reached.
Figure 4 plots PSM activity against secondary prices of USDC and Dai. Positive bars represent USDC being deposited in the PSM (traders selling USDC for newly minted Dai), and negative bars represent USDC being withdrawn from the PSM (traders burning Dai for USDC).
As expected, the price of both USDC and Dai fell in tandem in the window when the PSM was operational. Once the PSM daily cap was reached, however, a price differential opened up on March 11, with USDC falling further as selling continued through other channels. Prices converged once again upon the resumption of the PSM and remained broadly in lockstep thereafter.
The presence of the PSM helped to relieve some of the selling pressure on USDC. The PSM provided a hard-coded, zero-haircut facility offering Dai "at par" against USDC. The fact that the PSM was us

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
