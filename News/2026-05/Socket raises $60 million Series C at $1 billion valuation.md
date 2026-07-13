---
title: "Socket raises $60 million Series C at $1 billion valuation"
date: 2026-05-27
tags:
  - company/socket
  - industry/infrastructure
  - industry/ai
  - region/us
  - type/funding
sources:
  - https://socket.dev/blog/series-c
  - https://techstartups.com/2026/05/21/ai-security-startup-socket-hits-1b-valuation-after-60m-raise-to-stop-software-supply-chain-attacks
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: sf37062d9
month: 2026-05
enriched: false
---

# Socket raises $60 million Series C at $1 billion valuation

> [!info] 2026-05-27 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Socket hasraised$60m Series C at a $1bn valuation, led by Thrive Capital, as AI-assisted software development increases enterprise exposure to open-source supply chain risk.

## Первоисточники

### socket.dev
<https://socket.dev/blog/series-c>
*1890 слов · jina*

#### Secure your dependencies with us

Socket proactively blocks malicious open source packages in your code.

Install

Today we're announcing Socket's $60 million Series C at a $1 billion valuation, led by Thrive Capital, with participation from Andreessen Horowitz, Abstract Ventures, and Capital One Ventures. The round brings our total funding to $125 million and sets up the next phase of what we're building to protect the software supply chain.

This is the moment we've been working toward since we started Socket. AI has changed how every engineering team writes and ships code, increasing the volume of open source entering production. At the same time, attackers have spent the past several years exploiting a trust gap in open source that the industry was slow to defend.

## The original bet#

When we first announced Socket four years ago, modern applications were already pulling in more open source code than any team could realistically review. The dominant approach to securing dependencies was to scan for known vulnerabilities after public disclosure, which left a long gap between the moment a malicious package hit a public registry and the moment defenders had any chance to act on it. We believed that gap was where the next generation of attacks would happen, and that the right response was to analyze the actual behavior of dependencies in real time.

That conviction has only sharpened. AI now writes more than 90% of code at top engineering organizations and a substantial share everywhere else. A lot of what AI produces reaches for open source dependencies developers have never read. The volume of third-party code entering production keeps going up, the time anyone spends reviewing it keeps going down, and security tools from the previous era can't keep up.

## Open source is under sustained attack#

Supply chain attacks in the past year have been relentless. The Shai-Hulud worm has hit npm in repeated waves since September 2025, most recently as Mini Shai-Hulud across npm, PyPI, and Packagist earlier this month. Attackers compromised Aqua Security's Trivy scanner in March and used the stolen credentials for a chain of follow-on attacks. DPRK-aligned attackers ran a social engineering campaign against Node.js maintainers, including several Socket engineers, and the same playbook compromised Axios.

Package hijackings and maintainer compromises that were once a handful of incidents a year now happen weekly. They're the new normal. Attackers caught on to a trust gap that has existed for decades, and the industry was slow to build defenses for behavioral risk in open source because we all assumed Linus' Law would hold. The disclosure process most defenders rely on can't catch what the security community hasn't catalogued.

## Socket since Series B#

Since we closed our Series B in October 2024, Socket has grown from 7,500 organizations to more than 27,000. We protect 1.5 million repositories and secure over 11.6 million commits every month. Our platform blocks more than 10,000 supply chain attacks every week. The team has grown to more than 100 people.

The companies building the most ambitious AI products run Socket. Anthropic, xAI, Replit, Cursor, Vercel, Figma, Gusto, Mercado Libre, and Cribl are customers, alongside Fortune 100 companies in financial services and global media. These teams are shipping faster than ever, and they need security that moves at the same speed.

We've shipped a lot of product since the last round. Socket Firewall blocks malicious packages at install time, stopping compromised dependencies before they ever reach a developer's laptop or a CI pipeline. With our acquisition of Coana, we brought reachability analysis into the platform for precision CVE triage, which eliminates 50 to 80 percent of irrelevant vulnerability alerts by focusing only on the vulnerabilities that are actually exploitable. Socket Certified Patches let teams remediate exploitable CVEs in seconds without waiting on upstream maintainers.

When the Axios compromise hit, our detection systems flagged the malicious dependency within six minutes. Within 24 hours, more than 2,000 organizations had onboarded to Socket to block the package from reaching their environments. That speed of response is the entire point of what we've built.

Thrive Capital led the round because they see the same shift. Philip Clark, Partner at Thrive Capital, on why the legacy approach no longer works: "Legacy tools were designed to react to known vulnerabilities and assumed there was sufficient time to prevent a breach. Today, AI models can identify vulnerabilities so well and so quickly that this is no longer an option."

## What this funding is for#

With this round, we're focused on five areas.

**Investing in Socket Firewall.** Firewall already blocks malicious packages before they reach a developer's environment or CI pipeline. Socket Firewall is free for everyone, part of how we help defend the open source ecosystem. We're going to make it faster and sharper across more ecosystems, with new detections, better policy controls, and deeper integration into the places developers and agents install code.

**Massively expanding Socket Certified Patches.** Certified Patches are surgical fixes that let teams remediate exploitable CVEs without breaking production. We validate each patch against hundreds of AI-created test cases, giving teams an instant way to protect applications while they define a safe upgrade path. We're scaling the catalog to help defenders respond faster to the growing volume of disclosures as AI accelerates vulnerability discovery.

**Moving protection closer to the point of install.** Following our acquisition of Secure Annex, Socket is extending coverage from package managers to browser extensions, code editor extensions, MCP servers, and AI tools. Attackers are moving across packages, extensions, containers, CI/CD, and AI-adjacent tooling in rapid succession, and Socket needs to defend that whole surface.

**Imminent product launches.** New products coming soon push Socket into a category we haven't entered before. It's the natural next step for what we've been building.

**Growing the team.** Socket has gotten this far with a small, technically deep team. We're going to keep that bar high as we grow.

Alongside this round, we're rolling out a refreshed Socket brand, starting with a redesigned homepage and a refinement of our logo. The rest of the site will follow over the coming days. It's a sharper evolution of the same Socket.

## We're hiring#

This is a historic moment for software. AI is reshaping the industry faster than any technology in a generation, and the work of securing it has never mattered more. We're hiring across engineering, sales, customer success, and threat intel. If you want to work on the hardest problems in this space with a team that ships fast and takes the open source community seriously, take a look at our open roles at socket.dev/careers.

To every maintainer and developer working in open source: we see what you're up against, we're with you, and we're going to keep working to defend it. To our customers, our investors, and the team that has shipped all of this: thank you. There's a lot more to build.

## Investor Quotes#

*   **Miles Grimshaw, Partner at Thrive Capital:**"We first discovered Socket because Cursor, OpenAI, and Anthropic all independently told us it was the most important security tool they'd adopted in response to AI-driven development. When three of the most sophisticated AI companies in the world converge on the same vendor unprompted, you pay attention."
*   **Philip Clark, Partner at Thrive Capital:** "The developer laptop is the new perimeter. AI-driven development means millions of lines of third-party code flow onto developer machines every day, and legacy tools only flag problems after exploitation. Socket flips that model: it blocks malicious code before it ever reaches a developer's environment. Feross is exactly the right founder for this problem -- a legendary open source developer who built a tool that stops attacks in real time, not a dashboard that reports on them after the fact."
*   **Nick Marwell, Long Horizons team at Anthropic:** "As AI agents become more autonomous, they're making software decisions at speeds that require new paradigms for review. Socket is the only company I've seen that can match the pace we need. When the Axios attack hit, Socket caught it in minutes. That's the kind of infrastructure the industry needs."
*   **Ramtin Naimi, Founder and Managing Partner of Abstract Ventures:** "Security is a winner-take-all market. The company that sees the most attacks builds the best detection, which attracts the most customers, which surfaces more attacks. Socket has that flywheel running at scale now. We backed Socket before the market understood how big this category would become, and the speed at which enterprises have consolidated around Socket over the past year has exceeded every benchmark we track."
*   **Zane Lackey, Partner at Andreessen Horowitz**: "When we first invested in Socket at Series A, we said this team had all the signs of building an iconic security company. Three years later, they've proven it. Socket is now the standard for supply chain security at the companies building the most consequential AI products in the world. That doesn't happen without exceptional product and an exceptional team."

## Customer Quotes#

*   **Jason Clinton, CISO at Anthropic:** “Attackers are evolving their supply chain attacks and legacy tools aren’t catching them. Socket’s real-time threat detection helps strengthen our security posture, even from zero-day supply chain attacks.”
*   **Christina Cacioppo, CEO at Vanta:** "Every company selling into the enterprise is asked how they manage open source supply chain risk and stop supply chain attacks. The answers, until recently, were messy, manual, and prone to error. Socket's changed that when it became the standard way to block malicious packages before they reach code."
*   **Amjad Masad, CEO at Replit:** "AI is writing more code than ever, and a growing share of that code reaches for open source packages no human has reviewed. Replit serves millions of developers, and Socket is how we ensure the packages in their projects are safe."
*   **Aaron Brown, Former Head of Security, Vercel**: "Socket has helped us in reducing overlapping dependencies, reducing cognitive load, and improving dependency hygiene. It enables our teams to build fast and ship fast, with automation that supports our fast pace of experimentation."
*   **Kenneth Kaye, Lead Security Engineer, JupiterOne**: "We tried a variety of different solutions, but Socket turned out to be the most cost-effective and efficient, replacing all the others."
*   **Frédéric Charpentier, Head of Product Security, Doctolib**: "Although we explored some competitors that claimed to have supply chain protection, Socket was the only solution we found that truly explained the malicious patterns we were looking for in libraries. Its transparency and dedicated focus on supply chain security made it the perfect fit for our needs."
*   **Justin England, VP of Platform and Security, Chia**: "Our number of open security alerts in GitHub from across all tools is down 70 percent, due to fewer false positives and faster identification of actual threats, which gives us the ability to focus on alerts that matter."
*   More love from our supporters and customers.

## Series C Investors#

### Lead investor:

*   **Thrive Capital**

### With participation from existing investors:

*   **Andreessen Horowitz** (a16z)
*   **Abstract Ventures**
*   **Elad Gil**, Color Genomics founder, prolific investor & advisor
*   **Michael Ovitz**, CAA Co-founder, Hollywood super-agent

### Joined by new investors:

*   **CapitalOne Ventures**, strategic venture investment arm
*   **Sven Wollschlaeger**, cybersecurity investor at Brightmind
*   **Nick Marwell**, Anthropic Long Horizons team
*   **Michael Lai**, Anthropic state & local government AI lead

### Прочие ссылки (без извлечённого текста)

- <https://techstartups.com/2026/05/21/ai-security-startup-socket-hits-1b-valuation-after-60m-raise-to-stop-software-supply-chain-attacks>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
