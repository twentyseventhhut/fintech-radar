---
title: "Incognia launches Verified IP Location for fraud teams"
date: 2026-04-01
tags:
  - company/incognia
  - industry/fraud-risk
  - region/us
  - type/product
sources:
  - https://www.incognia.com/blog/verified-ip-location-know-where-your-web-traffic-is-actually-coming-from
  - https://www.incognia.com
status: tagged
n_mentions: 1
channels:
  - "Connecting the Dots in Fintech"
story_id: s440f13f2
month: 2026-04
enriched: false
---

# Incognia launches Verified IP Location for fraud teams

> [!info] 2026-04-01 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇺🇸 Verified IP Location: Know Where Your Web Traffic is Actually Coming From by Incognia. Incognia introduced Verified IP Location, a solution that provides fraud teams with accurate, real-time location intelligence for web traffic by using observed device data rather than unreliable IP assignment records. Rafael Gouveia explains that the innovation helps detect threats like VPN masking and account takeovers without adding friction for legitimate users.Incognia Introduced Verified IP Location

## Первоисточники

### incognia.com
<https://www.incognia.com/blog/verified-ip-location-know-where-your-web-traffic-is-actually-coming-from>
*1010 слов · direct*

Verified IP Location: Know Where Your Web Traffic is Actually Coming From 
The web has always been a difficult environment for location intelligence. IP addresses rotate, get reassigned, and can be masked, leaving fraud teams without a signal they can reliably act on. Incognia's Verified IP Location solves this by inferring IP location dynamically from real-world device observations rather than ISP assignment records, giving risk teams a live location layer for every web session. The result is visibility into attacks that were previously undetectable—account takeovers from unexpected regions, VPN masking, and geographic compliance violations—without adding any friction for legitimate users.
Subscribe to Incognia’s content

 For fraud teams, mobile has been the gold standard for years—GPS coordinates, sensor fusion, permission-based signals that together build a rich, layered picture of where a device actually is. 
 For the web? You get an IP address. This gap has defined what is and is not detectable on the web for the last decade. 
 Incognia's Verified IP Location changes that. Now, fraud teams have a location signal for the web built from real-world observed signals, not inferred from administrative assignment records. 
 Why the web has always been a hard environment for location 
 Mobile fraud detection runs on a combination of signals: GPS coordinates, sensor data, Wi-Fi triangulation, permission flows that let platforms verify where a device is operating. None of that exists on the web. 
 Browser-based location permission technically exists. But it's not a viable foundation. Adoption is more than 10x lower than on mobile. Implementation varies significantly across browsers. Desktop devices usually lack GPS entirely. And browser sandboxing blocks access to the supplementary signals that make mobile location meaningful—you can't combine signals the way mobile allows. 
 What fraud teams are realistically left with is an IP address. 
 That IP rotates between carriers. It gets reassigned. It's masked by VPNs. And through NAT rerouting, a single IP can represent thousands of distinct users. 
 The static databases the industry has relied on were built for a more predictable internet—they map assignment, not usage, and they can't keep pace with how the internet actually behaves today. 
 What IP alone can’t tell you 
 The core question every location-based risk check is trying to answer: is this session coming from where it claims to be? 
 The honest answer with IP alone: often, you can't tell. 
 A login from an unexpected region looks identical to a normal one. A fraudster routing through a VPN or cloud infrastructure leaves no trace. A user operating outside a permitted geographic zone is unverifiable. And platforms trying to compensate end up in an impossible position: accept the imprecision and miss attacks, or tighten the signal and create friction that punishes legitimate users. 
 A network built from the real world 
 Think about how weather forecasting works. Meteorologists can't measure temperature at every point on the planet. But thousands of weather stations reporting real conditions in real time let them accurately infer conditions anywhere, including places where no station exists. The more stations, the more precise the forecast. 
 That's the same principle behind Incognia's Verified IP Location. 
 Incognia's global network of devices enables continuous signal improvement across the platform. When a device sends a relevant signal alongside its IP, that observation contributes to continuously updating the inferred location associated with that IP. The result is a location signal for the web built from real observed signals, not from administrative assignment records. 
 The more devices that interact with the network, the richer the location intelligence becomes. Every new device contributes to improving signal quality across the network. That network effect compounds over time: more coverage, sharper signals, less room to hide. 
 How it’s built and what makes it reliable 
 Incognia builds Verified IP Location using signal intelligence generated in the normal course of providing its services across its global network of devices, not ISP allocation records. 
 VPN and proxy detection is layered in alongside ISP origin signals, so masked origins are flagged as fraud signals rather than passing through undetected. NAT rerouting—which can hide thousands of distinct users behind a single IP—is accounted for in the inference model. 
 IP is then combined with device, network, and account relationship data to compose layered risk signals. A known device on an unknown network. A known account accessing from an unexpected region. These combinations create a risk context that triggers the right response. 
 Coverage is now approaching 90%+ of IPs observed across the platform, with a clear path to 99%. At that level, nearly every IP a platform sees has a live, verified location behind it. 
 Benchmarked against prior third-party providers, Verified IP Location shows higher stability and lower noise, meaning fewer missed fraud events and fewer false positives. 
 What fraud teams can detect now that they couldn't before 
 With a reliable location signal at the IP level, fraud teams can detect patterns that were previously invisible. 
 Account takeovers originating from unexpected regions are now detectable. A login that looks normal by every other signal can be checked against a location that either fits or doesn't. VPN masking as an attack vector is visible—fraudsters routing through cloud infrastructure can be identified by the concentration of origins in specific providers. 
 Platforms with geographic compliance requirements—regulated financial institutions, marketplaces, gig economy platforms—can verify that users and workers are actually where they claim to be. 
 The IP is always present, but what's changed is how intelligently it's being used. 
 The goal for web location is a signal reliable enough to support decisions that protect revenue without adding friction for good users , and that's what Verified IP Location delivers. 
 The foundation changes what you can build 
 Verified IP Location is the layer that makes a new class of capabilities possible. 
 Trust Location for Web—which verifies whether a device is operating in a permitted geographic region without relying on user-granted location permissions—is launching soon on top of this infrastructure. 
 Cross-platform correlation, layered login risk assessment, and geographic compliance enforcement at scale all follow from the same foundation. 
 The location layer was the missing piece. This is what you build on top of it. 
 
Rafael Gouveia

### Прочие ссылки (без извлечённого текста)

- <https://www.incognia.com>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
