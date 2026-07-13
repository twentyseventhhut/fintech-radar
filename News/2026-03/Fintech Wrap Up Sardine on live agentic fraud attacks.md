---
title: "Fintech Wrap Up: Sardine on live agentic fraud attacks"
date: 2026-03-22
tags:
  - company/sardine
  - industry/fraud-risk
  - industry/ai
  - region/global
  - type/research-report
sources:
  - https://www.sardine.ai/blog/agentic-attacks
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: s22ef9733
month: 2026-03
enriched: false
---

# Fintech Wrap Up: Sardine on live agentic fraud attacks

> [!info] 2026-03-22 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] AI-driven fraud vectors: 7 agentic attacks now live in 2026 - Sardine, accessed March 15, 2026, https://www.sardine.ai/blog/agentic-attacks

## Первоисточники

### sardine.ai
<https://www.sardine.ai/blog/agentic-attacks>
*1695 слов · direct*

For more than a decade, fraud followed a relatively stable trajectory. Attackers scaled through automation, but strategy, judgment, and adaptation remained human-driven. Scripts sent phishing emails. Operators laundered funds. Analysts investigated after losses occurred.
That model is now obsolete.
This is what’s now hitting fraud ops, security, and risk teams first.
Over the last 12-18 months, we’ve observed a decisive shift from “fraud-at-scale” to “fraud-with-agency”. Modern fraud systems no longer just execute predefined instructions; they observe environments, learn behavioral patterns, make decisions, and act independently inside live financial ecosystems.
This matters because the majority of fraud stacks deployed today were designed for a very different threat model: one where attacks were noisy, patterns repeated, and execution speed was limited by human latency. In an agentic world, those assumptions collapse. Call it what it is: AI fraud in banking and fintech has crossed into autonomous execution.
We have identified seven AI-driven attack vectors that have moved from research concepts to operational threats. These are currently producing losses across our partner network in banking, fintech, and crypto. This report examines the mechanics of these attacks and the specific reasons legacy controls fail to stop them.
The 7 agentic fraud vectors at a glance
 Vector 
 Core capability 
 Why legacy controls fail 
 Required defensive shift 
Polymorphic phishing
Context-aware thread insertion
No malicious URLs or domains
Conversational anomaly detection
Invoice-timed malware
Predictive payment impersonation
Matches routine and vendor timing
Transactional expectation modeling
Deepfake-as-a-Service
Real-time synthetic identity manipulation
Device class + liveness assumed trustworthy
Stream integrity and session consistency checks
Synthetic identity farms
Long-horizon identity maturation
Point-in-time KYC passes
Network-level behavioral memory
Ghost Touch attacks
Biometric session hijacking
Login does not equal intent validation
Continuous session monitoring
CVE weaponization agents
Auto-generated exploit deployment
Patch windows too slow
Assume-breach behavioral detection
Automated chain-hopping
Fragmenting stolen funds into thousands of micro-transactions
Rule-based monitoring misses the pattern when funds are fragmented
Velocity and cross-chain correlation
1. Polymorphic phishing agents that operate in context
Traditional phishing relies on probability. Send enough messages and a small percentage of recipients will eventually click, reply, or comply. Polymorphic phishing agents reverse that logic entirely.
Instead of sending messages at scale, these agents embed themselves inside compromised inboxes and quietly observe. They read historical threads, analyze language patterns, learn internal slang, identify approval hierarchies, and model how real people communicate with one another over time.
Once trained, the agent does not initiate suspicious conversations. It inserts itself into existing, high-trust threads, often weeks after initial compromise. The responses it generates are not generic. They are tailored to the exact conversational context, written in the precise tone, cadence, and formatting the recipient expects.
Many variants avoid external command-and-control infrastructure to help conceal themselves. They "live off the land" by mirroring the victim’s working hours and typing rhythms. By matching reply latency and activity windows, the agent blends into the standard background noise of a workday.
The impact is profound. Email security systems that depend on indicators like URLs, attachments, or sender reputation see nothing unusual. Human reviewers see nothing suspicious. The strongest communication signals become the attack surface: trust, timing, and familiarity.
For fraud teams, detecting these incursions requires monitoring for deviations in conversational dynamics. The threat resides within the trusted identity, making message content a secondary signal.
2. Invoice-timed malware and predictive payment fraud
One of the most effective evolutions we see actually targets routine itself.
Malware families such as Predator and Thief v6 no longer prioritize immediate exfiltration. Instead, they focus on persistent observation. Once inside an environment, they map the connective tissue of the business: vendor relationships, invoice schedules, and payment approval flows.
Once that model is established, the malware waits patiently. If a legitimate vendor invoice historically arrives on the 15th of the month, the malware sends a counterfeit version on the 14th. The message mirrors prior invoices in formatting, language, and context, but quietly substitutes attacker-controlled banking details.
The success of this technique lies in operational psychology. Payment teams are optimized for throughput and accuracy under time pressure. Familiar senders and expected timing reduce scrutiny. When the real invoice arrives later, it is often dismissed as a duplicate.
This technique represents an evolution into predictive financial impersonation. The malware achieves high success rates by aligning with established operational routines. Because these messages contain no broken domains, malicious links, or unusual file types, they rarely trigger perimeter alerts before funds move.
Detecting predictive financial impersonation requires transactional expectation modeling. Because these messages contain no malicious links or suspicious domains, security relies on evaluating the payment behavior against a historical and contextual baseline. If the transaction details deviate from the established pattern for that entity, the system flags the anomaly regardless of how "clean" the email appears.
3. Deepfake-as-a-Service and hardware-assisted kyc bypass
Underground marketplaces now provide Deepfake-as-a-Service (DFaaS) platforms as standard infrastructure. These services offer APIs for real-time video manipulation, voice cloning, and face swapping, specifically engineered to plug directly into financial crime workflows.
Early KYC bypass attempts relied on replayed videos or static image substitution. Those techniques are now widely detectable. In response, attackers have introduced hybrid attacks that combine advanced software with physical hardware.
In these scenarios, high-fidelity deepfake models run on laptops or desktops capable of supporting heavy compute workloads. The output is then routed through a physical hardware device that presents itself as a mobile phone camera. From the perspective of the KYC system, the session appears to originate from a legitimate mobile device, complete with live video and natural motion.
This hardware-level manipulation renders device class an unreliable trust signal. Because these sessions appear as legitimate mobile devices with live video, liveness checks alone are insufficient. Effective detection requires analyzing session-wide consistency, including frame-rate stability, sensor data discrepancies, and behavioral patterns that deviate from standard mobile usage. Verification must focus on the integrity of the data stream rather than the assumed security of the hardware.
4. Synthetic identity farms and long-horizon fraud
Modern identity farms use AI agents to manage synthetic profiles through maturation cycles. During this phase, agents programmatically build credit history by cycling micro-loans and automating monthly repayments. By maintaining positive balances for six to 18 months, these profiles generate high-trust signals that often result in credit scores exceeding 800.
These identities remain dormant until a coordinated activation event. Attackers trigger them in waves to max out credit lines and drain balances across multiple institutions simultaneously. 
Regional adaptations amplify the damage. In Europe, attackers exploit uneven KYC enforcement and IBAN discrimination to move funds across borders with minimal friction. In North America, synthetic identities are increasingly paired with MFA token theft and internal IT impersonation to unlock higher-value accounts.
In isolation, each identity appears legitimate. Risk only surfaces at the network level through long-term behavioral memory and cross-entity linkage. Point-in-time verification fails to catch the slow accumulation of these synthetic clusters.
5. Ghost Touch attacks and biometric session hijacking
One of the most unsettling developments we have observed is the emergence of ghost touch attacks on mobile devices.
These attacks combine mobile Remote Access Trojans with electromagnetic interference hardware embedded in compromised charging stations located in public spaces such as airports, cafes, and office buildings.
When a device is plugged in, EMI emitters inject invisible touch inputs into the screen, allowing attackers to install malware without physical interaction. The malware then waits passively until the user authenticates into a high-value application.
Once the user successfully passes a biometric check, the malware takes control of the live session. It often simulates a system crash or darkens the screen to mask its activity. While the user believes the device is locked or rebooting, the malware executes transfers using the fully authenticated state.
By all appearances, the session is legitimate.
This attack vector exposes a critical blind spot: biometric authentication secures access, but not intent. Defending against it requires continuous session monitoring, anomaly detection during authenticated states, and device integrity assessment that extends beyond login events.
6. Turning defensive transparency into offensive automation
Public vulnerability disclosure serves as a cornerstone of cybersecurity, yet attackers now systematically weaponize this transparency. AI agents continuously ingest CVE and CISA disclosures to extract technical context, affected technologies, and mitigation guidance. By converting this data into structured prompts for code-generation models, attackers produce functional exploit code at machine speed.
Custom attack agents then deploy these exploits against exposed systems. The window between a vulnerability disclosure and its active exploitation is shrinking toward zero. Organizations that cannot patch immediately face increasing exposure even when they follow established security protocols.
This shift requires an "assume-exploit" posture for fraud and risk teams. Controls must detect the abnormal behavior resulting from a breach because relying solely on vulnerability management timelines is no longer a viable defense.
7. Automated chain-hopping and dust laundering
AI agents have turned money laundering into a high-speed optimization problem. Rather than relying on manual layering, these systems orchestrate cross-chain laundering strategies that move assets through blockchains, privacy protocols, and bridges in seconds.
The agents fragment stolen funds into tens of thousands of low-value transactions, often under $10 each. These "dust trails" are designed to make the economic cost of an investigation exceed the value of the recovered assets. The objective is not perfect anonymity, but rather economic exhaustion. At this scale, manual tracing is no longer a viable countermeasure.
Mitigating this risk requires cross-rail visibility and velocity-aware monitoring. Economic modeling must identify the underlying laundering patterns, even when the individual micro-transactions appear benign.
What this evolution means for fraud defense
Current defenses designed to flag the unusual fail when AI agents mimic established conversational tones and business timelines. These agents camouflage their activity within the mundane aspects of daily operations to bypass traditional security friction.
Countering this requires analyzing the intersection of identity, device integrity, and monetary velocity as a single event. Identification must focus on subtle deviations within a session before a transaction is finalized.
At Sardine, we provide the infrastructure to perform this correlation. By unifying these signals into a single data layer, the platform identifies patterns that point-in-time checks miss. Defensive strategy requires moving from reactive human review to an agentic oversight framework that matches the scale and speed of the current threat landscape.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
