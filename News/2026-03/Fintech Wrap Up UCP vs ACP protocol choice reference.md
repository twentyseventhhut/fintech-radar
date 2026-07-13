---
title: "Fintech Wrap Up: UCP vs ACP protocol choice reference"
date: 2026-03-29
tags:
  - industry/agentic-commerce
  - industry/infrastructure
  - region/global
  - type/research-report
sources:
  - https://www.paz.ai/blog/ucp-vs-acp-which-agentic-commerce-protocol-should-retailers-choose
status: tagged
n_mentions: 1
channels:
  - "Fintech Wrap Up"
story_id: sa6f16ab4
month: 2026-03
enriched: false
---

# Fintech Wrap Up: UCP vs ACP protocol choice reference

> [!info] 2026-03-29 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: Fintech Wrap Up

## Агрегированный текст (из дайджестов)

[Fintech Wrap Up] UCP vs ACP: Which Agentic Commerce Protocol Should Retailers Choose? - Paz.ai, accessed March 22, 2026, https://www.paz.ai/blog/ucp-vs-acp-which-agentic-commerce-protocol-should-retailers-choose

## Первоисточники

### paz.ai
<https://www.paz.ai/blog/ucp-vs-acp-which-agentic-commerce-protocol-should-retailers-choose>
*2010 слов · direct*

UCP vs ACP: Which Agentic Commerce Protocol Should Retailers Choose?
ACP (Agentic Commerce Protocol), UCP (Universal Commerce Protocol), and MCP (Model Context Protocol) are the three open standards competing to power AI-agent commerce in 2026. ACP, built by Stripe and OpenAI, handles checkout flows inside ChatGPT and went live in production in late 2025 with PayPal and Worldpay as payment partners. UCP, launched by Google with Shopify and Walmart at NRF 2026, covers the full commerce journey from discovery through post-purchase. MCP, created by Anthropic and now governed by the Linux Foundation, provides a general-purpose protocol for connecting AI models to external tools and data sources, including commerce APIs.
Most retailers will need to support at least two of these three protocols, since each connects to different AI shopping surfaces. ChatGPT uses ACP for transactions. Google AI Mode and Gemini use UCP. And enterprise AI tools from Salesforce, Adobe, and others increasingly rely on MCP for catalog integration. Choosing just one protocol means losing access to significant portions of the AI shopping market.
Today, Google CEO Sundar Pichai took the stage at NRF 2026 to announce the Universal Commerce Protocol (UCP) , an open standard developed with Shopify, Walmart, Target, and over 20 industry partners. This launch puts Google in direct competition with the Agentic Commerce Protocol (ACP) , created by Stripe and OpenAI to power ChatGPT Instant Checkout.
For retailers already navigating the complexity of AI shopping agents, this raises an urgent question: Which protocol should you prioritize?
The short answer: You will likely need both. But understanding when, why, and how changes everything about your implementation strategy.
What Is UCP and Why Did Google Launch It Now?
The Universal Commerce Protocol is Google's bid to standardize the entire agentic shopping journey, from product discovery through post-purchase support. Unlike protocols that focus on a single transaction layer, UCP establishes what Google calls a "common language" for AI agents to communicate with retailers across every stage of commerce.
UCP's timing is strategic. Google watched OpenAI and Stripe capture early agentic commerce momentum with ACP, which powers ChatGPT's shopping features used by 45% of U.S. consumers in the past month. Rather than compete on identical terrain, Google built UCP to address the entire commerce lifecycle while integrating its earlier Agent Payments Protocol (AP2) as the underlying payment layer.
 UCP's co-developers and endorsers include: 
 Retailers : Walmart, Target, Shopify, Etsy, Wayfair, Best Buy, The Home Depot, Macy's, Zalando
 Payment providers : Visa, Mastercard, American Express, Stripe, Adyen, PayPal (coming)
This partner list reveals Google's strategy: build the protocol with retailers rather than imposing a standard on them. Walmart's presence is particularly notable given their existing ChatGPT integration , signaling that major retailers see value in supporting multiple protocols.
How UCP Differs from ACP: A Technical Comparison
The fundamental difference between UCP and ACP lies in scope. ACP standardizes the checkout conversation between AI agents and merchants. UCP standardizes the entire shopping journey.
 "UCP is used to orchestrate the broader purchase lifecycle, while AP2 can be used as a specialized payment layer within UCP." — Google Developers Blog 
What UCP Does That ACP Doesn't
 1. Product Discovery Standardization 
UCP defines how AI agents should query product catalogs, interpret search intent, and present options to consumers. This matters because as of September 2025, 87% of AI agent requests target product pages, according to HUMAN Security , yet most retailers haven't optimized their catalog data for agent comprehension.
 2. Post-Purchase Orchestration 
Returns, exchanges, customer service inquiries: UCP standardizes how agents handle the entire post-purchase experience. Retailers using AI agents for customer service saw a 70% surge in automated agent actions for tasks like address updates and returns during Cyber Week 2025.
 3. Multi-Surface Distribution 
With UCP, a single integration enables commerce across Google Search AI Mode, Gemini, and potentially future Google surfaces. This "build once, distribute everywhere" approach reduces the N-to-N integration problem that plagues multi-platform retailers.
What ACP Does That UCP Doesn't
 1. Existing ChatGPT Integration 
ACP already powers ChatGPT Instant Checkout . ChatGPT processes 50 million shopping queries daily, with Instant Checkout available to complete purchases directly in the conversation. If your customers are on ChatGPT (and statistically, many are), ACP is your gateway.
 2. Stripe Native Payment Rails 
For retailers already on Stripe, ACP integration leverages existing payment infrastructure. The Agentic Commerce Suite provides a low-code solution that brands like Anthropologie, Coach, and Revolve are already onboarding.
 3. First-Mover Ecosystem 
ACP has a three-month head start. Salesforce announced Agentforce Commerce integration in October 2025. E-commerce platforms including Wix, WooCommerce, BigCommerce, and Squarespace are rolling out ACP support.
The Multi-Protocol Reality: Why "Either/Or" Is the Wrong Question
Here's what the protocol debate misses: retailers won't choose between UCP and ACP. They'll use both.
The consumer doesn't care which protocol powers their AI shopping experience. They care whether their preferred AI assistant can find, purchase, and track products seamlessly. A customer using ChatGPT expects Instant Checkout. A customer using Gemini expects Google's native experience. Retailers who support only one protocol lose the other's traffic.
This multi-protocol reality is already emerging:
 Walmart integrated with ChatGPT (ACP ecosystem) AND announced Google Gemini partnership at NRF 2026 (UCP ecosystem)
 Shopify co-developed UCP with Google while also supporting 1M+ merchants on ChatGPT Instant Checkout via ACP
 Stripe endorsed UCP despite creating ACP, recognizing that payment protocols and commerce protocols serve different functions
The winners in agentic commerce won't be protocol purists. They'll be retailers who reach consumers wherever AI agents operate.
Which Protocol Should You Prioritize First?
While most retailers will eventually need both protocols, resource constraints demand prioritization. Here's a decision framework based on your current situation:
Prioritize ACP First If:
 Your customers skew younger : 65% of ages 16-24 used ChatGPT in the past month vs. 32% for Gemini, according to Morgan Stanley 
 You're already on Stripe : The Agentic Commerce Suite offers the fastest path to ChatGPT visibility
 You sell impulse-friendly products : ChatGPT's conversational interface drives 36% purchase rates among platform users 
 You need results this quarter : ACP is live now; UCP is still ramping
Prioritize UCP First If:
 You have complex catalogs : UCP's full-journey approach handles discovery better for large inventories
 Post-purchase is a competitive advantage : UCP standardizes returns, exchanges, and support
 You're targeting Google Search traffic : UCP powers AI Mode in Search, where most product queries still start
 You already participate in Google Shopping : Existing Merchant Center data accelerates UCP integration
The "Build for Both" Path
Infrastructure platforms that support multiple protocols eliminate this trade-off entirely. Rather than building separate integrations for ACP, UCP, and the emerging MCP ecosystem, protocol abstraction layers provide unified access.
Case Studies: How Major Retailers Are Handling Protocol Strategy
Walmart: The Multi-Protocol Pioneer
Walmart exemplifies the "yes, and" approach to protocol strategy. Their October 2025 OpenAI partnership brought ChatGPT Instant Checkout to their catalog. At NRF 2026, they announced Gemini integration through UCP. The result: 20% of Walmart's referral traffic now comes from ChatGPT, up 15% from July, according to Digiday .
Meanwhile, Walmart's internal AI deployment cut customer service resolution times by 40%. They're not just enabling agentic commerce; they're running agents throughout their operations.
Amazon: The Anti-Pattern
Amazon chose to block AI crawlers, removing 600 million product listings from AI results. The consequence: ChatGPT referral traffic to Amazon fell 18% month-over-month to under 3% .
This isn't about protocols. Amazon's "Buy for Me" controversy, where merchants report unauthorized product listings via Amazon's agentic purchasing, shows a fundamentally different philosophy: control the agent rather than enable external ones.
Shopify Merchants: Protocol-Agnostic by Default
Shopify's Winter 2025 Edition made every store "agent-ready by default." Their Agentic Storefronts feature enables selling across ChatGPT, Perplexity, and Microsoft Copilot through a single setup. With 7x growth in AI traffic and 11x growth in AI-driven orders since January 2025, according to TechCrunch , Shopify merchants don't need to pick protocols: their platform handles it.
The Full Protocol Landscape: Beyond UCP and ACP
UCP and ACP don't exist in isolation. The complete agentic commerce stack includes:
UCP explicitly designed for compatibility with AP2, A2A, and MCP . This interoperability matters because agentic commerce isn't one protocol solving everything. It's a stack of protocols, each handling a specific layer.
The practical implication: retailers evaluating protocol strategy should ask not just "UCP or ACP?" but "How do we participate in the full agentic commerce stack without building five separate integrations?"
What Happens Next: The 2026 Protocol Timeline
The protocol landscape will evolve rapidly. Here's what to expect:
 Q1 2026: 
UCP merchant onboarding accelerates (waitlist now open at Google )
ACP expands beyond ChatGPT to additional AI surfaces
Microsoft Copilot Shopping adds new commerce partners
 Q2-Q3 2026: 
Protocol consolidation begins as winners emerge
PayPal activates UCP integration
Enterprise retailers report first protocol performance comparisons
 Q4 2026: 
Holiday shopping becomes the first true multi-protocol stress test
Market share data reveals which protocols drive actual revenue
The window for early-mover advantage is now. Retailers establishing protocol presence in H1 2026 will capture traffic before the holiday rush forces mass adoption.
Frequently Asked Questions
What is the Universal Commerce Protocol (UCP)?
The Universal Commerce Protocol is an open standard developed by Google in collaboration with Shopify, Walmart, Target, and 20+ industry partners. UCP establishes a common language for AI agents to handle the entire shopping journey, from product discovery through checkout and post-purchase support. It launched at NRF 2026 and powers Google AI Mode and Gemini app commerce experiences.
How is UCP different from Google's earlier AP2 protocol?
AP2 (Agent Payments Protocol) focuses specifically on payment authorization and trust, defining how agents, users, and payment providers communicate consent for transactions. UCP is broader: it orchestrates the full commerce journey while using AP2 as its underlying payment layer. Think of AP2 as the payment component within the larger UCP framework.
Can retailers use both UCP and ACP?
Yes, and most large retailers will need both. Walmart already supports ChatGPT (ACP ecosystem) and Gemini (UCP ecosystem). Shopify merchants automatically gain access to both through platform-level integrations. The protocols serve different AI surfaces, so supporting both maximizes consumer reach.
Which protocol is better for small retailers?
For small retailers on Shopify, platform-level integration handles protocol complexity automatically. For others, ACP via Stripe offers faster time-to-market if you're already using Stripe for payments. UCP requires Google Merchant Center participation but offers access to Google Search's massive query volume.
Do I need to rebuild my e-commerce stack for these protocols?
No. Both UCP and ACP are designed to work with existing commerce infrastructure. The merchant remains the merchant of record, and transactions flow through established payment processors. The protocols standardize how AI agents interact with your existing systems, not replace those systems.
What about MCP (Model Context Protocol)?
MCP, created by Anthropic, handles AI-to-tool connectivity and is complementary to both UCP and ACP. UCP explicitly supports MCP interoperability. For retailers, MCP becomes relevant when deploying internal AI agents that need to access commerce data, inventory systems, or customer service tools.
The Bottom Line: Protocol Strategy Is Now Business Strategy
The launch of UCP makes one thing clear: agentic commerce protocols are no longer experimental. They're infrastructure. McKinsey projects agentic commerce will reach $3-5 trillion globally by 2030. Morgan Stanley estimates $190-385 billion in the U.S. alone.
Retailers who treat protocol selection as a technical detail will fall behind. Those who recognize it as strategic positioning will capture the traffic that's already flowing through AI shopping agents.
The question isn't "UCP vs ACP." The question is: How quickly can you become visible everywhere AI agents shop?
Your customers' AI agents are making purchase decisions right now. Are they finding you?
 Ready to support every agentic commerce protocol without building multiple integrations? Paz.ai's protocol unification layer gives retailers single-integration access to UCP, ACP, MCP, and emerging standards. Learn how unified infrastructure simplifies your protocol strategy .
Related: UCP technical implementation guide 
 Sources: 
 Google Developers Blog: Universal Commerce Protocol 
 OpenAI: Buy it in ChatGPT 
 Stripe: Agentic Commerce Suite 
 Morgan Stanley: Agentic Commerce Market Impact Outlook 
 Salesforce: Cyber Week AI Agents Dat

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
