---
title: "Fintech Brainfood: the protocols for agentic banking and payments"
date: 2026-10-15
retrieved: 2026-10-15
tags:
  - company/mastercard
  - industry/agentic-commerce
  - industry/ai
  - region/global
  - type/commentary
sources:
  - https://personalagentprotocol.org/docs/introduction
  - https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/basic/authorization.mdx
  - https://www.mastercard.com/gb/en/news-and-trends/stories/2026/verifiable-intent.html
  - https://www.proof.com/blog/identity-infrastructure-agentic-internet-x401
  - https://ncua.gov/regulation-supervision/regulatory-compliance-resources/bank-secrecy-act-resources/frequently-asked-questions-regarding-treatment-verifiable-digital-credentials
  - https://x401.proof.com/spec/latest
  - https://pages.nist.gov/800-63-4/sp800-63a/ial
  - https://www.consumerfinance.gov/rules-policy/regulations/1005/6
  - https://www.consumerfinance.gov/rules-policy/regulations/1005/11
  - https://www.consumerfinance.gov/rules-policy/regulations/1005/2
status: enriched
n_mentions: 7
channels:
  - "Fintech Brainfood"
story_id: sdf5b26fb
month: 2026-10
enriched: true
importance: 4
freshness: fresh
---

# Fintech Brainfood: the protocols for agentic banking and payments

> [!info] 2026-10-15 · 7 упоминаний · 5 источника(ов) с текстом
> Каналы: Fintech Brainfood

## Агрегированный текст (из дайджестов)

[Fintech Brainfood] Personal Agent Protocol (PAP): Recognise the agent and sign the customer in. Access is limited to what the customer and company agree, and can be revoked.

[Fintech Brainfood] x401: Bring proof about the human. The bank can ask for verified identity or eligibility. The agent presents the proof; the bank checks it.

[Fintech Brainfood] MCP: Give the agent things it can do. It lets an agent discover and use the tools a service offers. Read these transactions. Request this action. The provider decides what’s allowed.

[Fintech Brainfood] Verifiable Intent: Prove what the user authorised. Mastercard’s approach links the authorisation to the purchase, leaving a tamper-resistant record.

[Fintech Brainfood] The important new piece here is x401. Proof, an identity provider, checks identity to NIST’s Identity Assurance Level 2 (IAL2). The promise is reusable proof, without uploading your documents to every service. No selfies or annoying head turning required before your agent can do a thing. And because FinCEN’s recent guidance allows digital credentials within banks’ customer identification programs, this is a lot more bank-ready than a basic handshake protocol alone.

[Fintech Brainfood] In the US, Regulation E protects consumers in covered electronic fund transfers, including rules for unauthorized transfers and resolving errors. That won’t go away, and gives at minimum a lot to think about for anyone who moves money.

[Fintech Brainfood] However, Reg E’s offi

## Первоисточники

### personalagentprotocol.org
<https://personalagentprotocol.org/docs/introduction>
*558 слов · direct*

Introduction
What is Personal Agent Protocol?
Personal Agent Protocol (Poppy for short ) is an open protocol for how personal agents and companies work together. A company uses it to declare how personal agents can interact with it. A personal agent uses it to sign in safely and get access to a person's account, limited to what that person and the company agree to.
The goal is for the protocol to cover everything a company and a personal agent can do together, so each side implements it once and works with every other side that supports it.
Why does it exist?
Personal agents are already here, and people like using them. They hand off everyday tasks, and many of those tasks end at a company. Companies are already seeing this traffic. Some block it, and others are deciding whether to.
Today it is all or nothing. Either the agent passes as the user, signing in with their password and clicking through pages built for people, or the company blocks it and it can't do anything. Neither works well. The user can't limit what the agent does once it's in, and the company can't tell an agent from a person or offer it a better path.
There need to be more points between those two extremes, so that companies and users can choose how agents work with them. An airline might let any agent search flights, let signed-in agents see the user's trips, and require the user's approval before buying a ticket. A user might let an agent see their trips but not change them.
As agents take on more of what people do online, the cost of all or nothing grows: companies spend more effort detecting agents, and agents spend more effort evading detection. Personal Agent Protocol gives both sides a way to work together, with more choice and control.
Principles
 Built on existing standards. Personal Agent Protocol uses OAuth, JWTs, HTTPS, OpenAPI, and MCP wherever they fit, so teams can implement it with libraries and tools that already exist. It defines something new only where no standard covers the need.
 Controls, not policy. The protocol offers a range of options, and each side chooses what fits. A company decides whether agents can work anonymously or must sign the user in, which personal agents to allow, which channels to offer, and how much access to grant. A user decides how to sign in and whether the agent can view their account, make changes, or both.
 Secure and private. We think Personal Agent Protocol can become part of the foundation of the internet, so it has to be trustworthy. A personal agent always identifies itself, but until the person signs in, the company knows them only by an ID that contains no personal information. The ID stays the same over time, so the company can recognize a returning user, but it is different at every company. Companies can choose which sign-in options meet their security needs, and access is limited to what was granted and can be revoked.
 Progressive adoption. A company can start with only a website, only APIs, or only an agent, and add more over time, without rebuilding its existing systems.
 Extensible. Discovery, identity, APIs, and conversations are building blocks that companies and industries can extend, for example to add payments, push notifications, or interactive elements.

### github.com
<https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/basic/authorization.mdx>
*2041 слов · direct*

Introduction
Purpose and Scope
The Model Context Protocol provides authorization capabilities at the transport level,
enabling MCP clients to make requests to restricted MCP servers on behalf of resource
owners. This specification defines the authorization flow for HTTP-based transports.
Protocol Requirements
Authorization is OPTIONAL for MCP implementations. When supported:
Implementations using an HTTP-based transport SHOULD conform to this specification.
Implementations using an STDIO transport SHOULD NOT follow this specification, and
instead retrieve credentials from the environment.
Implementations using alternative transports MUST follow established security best
practices for their protocol.
Standards Compliance
This authorization mechanism is based on established specifications listed below, but
implements a selected subset of their features to ensure security and interoperability
while maintaining simplicity:
OAuth 2.1 IETF DRAFT ( draft-ietf-oauth-v2-1-13 )
OAuth 2.0 Authorization Server Metadata
( RFC8414 )
OAuth 2.0 Dynamic Client Registration Protocol
( RFC7591 )
OAuth 2.0 Protected Resource Metadata ( RFC9728 )
Authorization Flow
Roles
A protected MCP server acts as an OAuth 2.1 resource server ,
capable of accepting and responding to protected resource requests using access tokens.
An MCP client acts as an OAuth 2.1 client ,
making protected resource requests on behalf of a resource owner.
The authorization server is responsible for interacting with the user (if necessary) and issuing access tokens for use at the MCP server.
The implementation details of the authorization server are beyond the scope of this specification. It may be hosted with the
resource server or a separate entity. The Authorization Server Discovery section 
specifies how an MCP server indicates the location of its corresponding authorization server to a client.
Overview

 Authorization servers MUST implement OAuth 2.1 with appropriate security
measures for both confidential and public clients. 


 Authorization servers and MCP clients SHOULD support the OAuth 2.0 Dynamic Client Registration
Protocol ( RFC7591 ). 


 MCP servers MUST implement OAuth 2.0 Protected Resource Metadata ( RFC9728 ).
MCP clients MUST use OAuth 2.0 Protected Resource Metadata for authorization server discovery. 


 Authorization servers MUST provide OAuth 2.0 Authorization
Server Metadata ( RFC8414 ).
MCP clients MUST use the OAuth 2.0 Authorization Server Metadata. 

Authorization Server Discovery
This section describes the mechanisms by which MCP servers advertise their associated
authorization servers to MCP clients, as well as the discovery process through which MCP
clients can determine authorization server endpoints and supported capabilities.
Authorization Server Location
MCP servers MUST implement the OAuth 2.0 Protected Resource Metadata ( RFC9728 )
specification to indicate the locations of authorization servers. The Protected Resource Metadata document returned by the MCP server MUST include
the authorization_servers field containing at least one authorization server.
The specific use of authorization_servers is beyond the scope of this specification; implementers should consult
OAuth 2.0 Protected Resource Metadata ( RFC9728 ) for
guidance on implementation details.
Implementors should note that Protected Resource Metadata documents can define multiple authorization servers. The responsibility for selecting which authorization server to use lies with the MCP client, following the guidelines specified in
 RFC9728 Section 7.6 "Authorization Servers" .
MCP servers MUST use the HTTP header WWW-Authenticate when returning a 401 Unauthorized to indicate the location of the resource server metadata URL
as described in RFC9728 Section 5.1 "WWW-Authenticate Response" .
MCP clients MUST be able to parse WWW-Authenticate headers and respond appropriately to HTTP 401 Unauthorized responses from the MCP server.
Server Metadata Discovery
MCP clients MUST follow the OAuth 2.0 Authorization Server Metadata RFC8414 
specification to obtain the information required to interact with the authorization server.
Sequence Diagram
The following diagram outlines an example flow:
Dynamic Client Registration
MCP clients and authorization servers SHOULD support the
OAuth 2.0 Dynamic Client Registration Protocol RFC7591 
to allow MCP clients to obtain OAuth client IDs without user interaction. This provides a
standardized way for clients to automatically register with new authorization servers, which is crucial
for MCP because:
Clients may not know all possible MCP servers and their authorization servers in advance.
Manual registration would create friction for users.
It enables seamless connection to new MCP servers and their authorization servers.
Authorization servers can implement their own registration policies.
Any authorization servers that do not support Dynamic Client Registration need to provide
alternative ways to obtain a client ID (and, if applicable, client credentials). For one of
these authorization servers, MCP clients will have to either:
Hardcode a client ID (and, if applicable, client credentials) specifically for the MCP client to use when
interacting with that authorization server, or
Present a UI to users that allows them to enter these details, after registering an
OAuth client themselves (e.g., through a configuration interface hosted by the
server).
Authorization Flow Steps
The complete Authorization flow proceeds as follows:
Resource Parameter Implementation
MCP clients MUST implement Resource Indicators for OAuth 2.0 as defined in RFC 8707 
to explicitly specify the target resource for which the token is being requested. The resource parameter:
 MUST be included in both authorization requests and token requests.
 MUST identify the MCP server that the client intends to use the token with.
 MUST use the canonical URI of the MCP server as defined in RFC 8707 Section 2 .
For the purposes of this specification, the canonical URI of an MCP server is defined as the resource identifier as specified in
 RFC 8707 Section 2 and aligns with the resource parameter in
 RFC 9728 .
MCP clients SHOULD provide the most specific URI that they can for the MCP server they intend to access, following the guidance in RFC 8707 . While the canonical form uses lowercase scheme and host components, implementations SHOULD accept uppercase scheme and host components for robustness and interoperability.
Examples of valid canonical URIs:
 https://mcp.example.com/mcp 
 https://mcp.example.com 
 https://mcp.example.com:8443 
 https://mcp.example.com/server/mcp (when path component is necessary to identify individual MCP server)
Examples of invalid canonical URIs:
 mcp.example.com (missing scheme)
 https://mcp.example.com#fragment (contains fragment)

 Note: While both https://mcp.example.com/ (with trailing slash) and https://mcp.example.com (without trailing slash) are technically valid absolute URIs according to RFC 3986 , implementations SHOULD consistently use the form without the trailing slash for better interoperability unless the trailing slash is semantically significant for the specific resource. 

For example, if accessing an MCP server at https://mcp.example.com , the authorization request would include:
MCP clients MUST send this parameter regardless of whether authorization servers support it.
Access Token Usage
Token Requirements
Access token handling when making requests to MCP servers MUST conform to the requirements defined in
 OAuth 2.1 Section 5 "Resource Requests" .
Specifically:
MCP client MUST use the Authorization request header field defined in
 OAuth 2.1 Section 5.1.1 :
Note that authorization MUST be included in every HTTP request from client to server,
even if they are part of the same logical session.
Access tokens MUST NOT be included in the URI query string
Example request:
Token Handling
MCP servers, acting in their role as an OAuth 2.1 resource server, MUST validate access tokens as described in
 OAuth 2.1 Section 5.2 .
MCP servers MUST validate that access tokens were issued specifically for them as the intended audience,
according to RFC 8707 Section 2 .
If validation fails, servers MUST respond according to
 OAuth 2.1 Section 5.3 
error handling requirements. Invalid or expired tokens MUST receive a HTTP 401
response.
MCP clients MUST NOT send tokens to the MCP server other than ones issued by the MCP server's authorization server.
Authorization servers MUST only accept tokens that are valid for use with their
own resources.
MCP servers MUST NOT accept or transit any other tokens.
Error Handling
Servers MUST return appropriate HTTP status codes for authorization errors:
Security Considerations
Implementations MUST follow OAuth 2.1 security best practices as laid out in OAuth 2.1 Section 7. "Security Considerations" .
Token Audience Binding and Validation
 RFC 8707 Resource Indicators provide critical security benefits by binding tokens to their intended
audiences when the Authorization Server supports the capability . To enable current and future adoption:
MCP clients MUST include the resource parameter in authorization and token requests as specified in the Resource Parameter Implementation section
MCP servers MUST validate that tokens presented to them were specifically issued for their use
The Security Best Practices document 
outlines why token audience validation is crucial and why token passthrough is explicitly forbidden.
Token Theft
Attackers who obtain tokens stored by the client, or tokens cached or logged on the server can access protected resources with
requests that appear legitimate to resource servers.
Clients and servers MUST implement secure token storage and follow OAuth best practices,
as outlined in OAuth 2.1, Section 7.1 .
Authorization servers SHOULD issue short-lived access tokens to reduce the impact of leaked tokens.
For public clients, authorization servers MUST rotate refresh tokens as described in OAuth 2.1 Section 4.3.1 "Token Endpoint Extension" .
Communication Security
Implementations MUST follow OAuth 2.1 Section 1.5 "Communication Security" .
Specifically:
All authorization server endpoints MUST be served over HTTPS.
All redirect URIs MUST be either localhost or use HTTPS.
Authorization Code Protection
An attacker who has gained access to an authorization code contained in an authorization response can try to redeem the authorization code for an access token or otherwise make use of the authorization code.
(Further described in OAuth 2.1 Section 7.5 )
To mitigate this, MCP clients MUST implement PKCE according to OAuth 2.1 Section 7.5.2 .
PKCE helps prevent authorization code interception and injection attacks by requiring clients to create a secret verifier-challenge pair, ensuring that only the original requestor can exchange an authorization code for tokens.
Open Redirection
An attacker may craft malicious redirect URIs to direct users to phishing sites.
MCP clients MUST have redirect URIs registered with the authorization server.
Authorization servers MUST validate exact redirect URIs against pre-registered values to prevent redirection attacks.
MCP clients SHOULD use and verify state parameters in the authorization code flow
and discard any results that do not include or have a mismatch with the original state.
Authorization servers MUST take precautions to prevent redirecting user agents to untrusted URI's, following suggestions laid out in OAuth 2.1 Section 7.12.2 
Authorization servers SHOULD only automatically redirect the user agent if it trusts the redirection URI. If the URI is not trusted, the authorization server MAY inform the user and rely on the user to make the correct decision.
Confused Deputy Problem
Attackers can exploit MCP servers acting as intermediaries to third-party APIs, leading to confused deputy vulnerabilities .
By using stolen authorization codes, they can obtain access tokens without user consent.
MCP proxy servers using static client IDs MUST obtain user consent for each dynamically
registered client before forwarding to third-party authorization servers (which may require additional consent).
Access Token Privilege Restriction
An attacker can gain unauthorized access or otherwise compromise an MCP server if the server accepts tokens issued for other resources.
This vulnerability has two critical dimensions:
 Audience validation failures. When an MCP server doesn't verify that tokens were specifically intended for it (for example, via the audience claim, as mentioned in RFC9068 ), it may accept tokens originally issued for other services. This breaks a fundamental OAuth security boundary, allowing attackers to reuse legitimate tokens across different services than intended.
 Token passthrough. If the MCP server not only accepts tokens with incorrect audiences but also forwards these unmodified tokens to downstream services, it can potentially cause the "confused deputy" problem , where the downstream API may incorrectly trust the token as if it came from the MCP server or assume the token was validated by the upstream API. See the Token Passthrough section of the Security Best Practices guide for additional details.
MCP servers MUST validate access tokens before processing the request, ensuring the access token is issued specifically for the MCP server, and take all necessary steps to ensure no data is returned to unauthorized parties.
A MCP server MUST follow the guidelines in OAuth 2.1 - Section 5.2 to validate inbound tokens.
MCP servers MUST only accept tokens specifically intended for themselves and MUST reject tokens that do not include them in the audience claim or otherwise verify that they are the intended recipient of the token. See the Security Best Practices Token Passthrough section for details.
If the MCP server makes requests to upstream APIs, it may act as an OAuth client to them. The access token used at the upstream API is a separate token, issued by the upstream authorizat

### mastercard.com
<https://www.mastercard.com/gb/en/news-and-trends/stories/2026/verifiable-intent.html>
*1777 слов · direct*

For you 
 

 For business 
 

 For the world 
 

 For innovators 
 

 News and trends 
 

 
 Find a card
 

 

 

 

 
 Ways to pay
 

 

 

 

 
 Protecting you
 

 

 

 

 
 Get support
 

 

 

 

 
 Experience Mastercard
 

 

 

 

 Explore all cards 


 

 

 

 Mastercard Credit Cards 


 

 

 

 Mastercard Debit Cards 


 

 

 

 Mastercard Prepaid Cards 


 

 

 

 Cards for your passions 


 

 

 

 Card benefits 


 

 

 

 Pay your way 


 

 

 

 Contactless 


 

 

 

 Click to Pay 


 

 

 

 Payment passkeys 


 

 

 

 Safety and security benefits 


 

 

 

 Mastercard ID Theft Protection 


 

 

 

 Support and contacts 


 

 

 

 Find the nearest ATM 


 

 

 

 Use our currency converter 


 

 

 

 Enjoy Priceless Experiences 


 

 

 

 Our multisensory brand 


 

 

 

 
 Explore solutions
 

 

 

 

 
 Explore by industry segment
 

 

 

 

 
 Partner programmes
 

 

 

 

 
 Support
 

 

 

 

 Consumer payments 


 

 

 

 Commercial payments 


 

 

 

 Money movement 


 

 

 

 Open finance 


 

 

 

 Advisors & transformation 


 

 

 

 Cybersecurity and fraud prevention 


 

 

 

 Consumer Acquisition & Engagement 


 

 

 

 Insights and intelligence 


 

 

 

 AI 


 

 

 

 Financial institutions 


 

 

 

 Small and medium enterprises 


 

 

 

 Large corporations 


 

 

 

 Public sector 


 

 

 

 Fintech 


 

 

 

 Acquirers and PSPs 


 

 

 

 Healthcare 


 

 

 

 Partner Advantage Programme 


 

 

 

 Network Enablement Partners (NEP) 


 

 

 

 Mastercard Move 


 

 

 

 Find a payment facilitator. 


 

 

 

 Network Enablement Partners 


 

 

 

 Mastercard rules and compliance programmes 


 

 

 

 BIN account range table 


 

 

 

 Mastercard interchange fees 


 

 

 

 
 Making an impact
 

 

 

 

 
 Empowering people
 

 

 

 

 
 Pathways to prosperity
 

 

 

 

 
 Preserving the planet
 

 

 

 

 
 About Mastercard
 

 

 

 

 Corporate impact 


 

 

 

 Empowering people 


 

 

 

 Pathways to prosperity 


 

 

 

 Preserving the planet 


 

 

 

 Community and belonging 


 

 

 

 Careers at Mastercard 


 

 

 

 Community impact 


 

 

 

 Girls4Tech 


 

 

 

 Mastercard Center for Inclusive Growth 


 

 

 

 Financial Inclusion products and solutions 


 

 

 

 Mastercard Community Pass 


 

 

 

 

 

 

 Reducing our GHG emissions 


 

 

 

 Environmentally conscious choices 


 

 

 

 Priceless Planet Coalition 


 

 

 

 Carbon Calculator 


 

 

 

 Digital First card programme 


 

 

 

 About us 


 

 

 

 Privacy and data responsibility 


 

 

 

 Reports, policies and statements 


 

 

 

 Mastercard in Europe 


 

 

 

 Regulatory overview 


 

 

 

 
 Build with us
 

 

 

 

 
 Partner with us
 

 

 

 

 
 Explore with us
 

 

 

 

 
 Engage with us
 

 

 

 

 Developers 


 

 

 

 Digital labs 


 

 

 

 Start Path 


 

 

 

 Mastercard Engage 


 

 

 

 Product Express 


 

 

 

 Research and insights 


 

 

 

 Research and development 


 

 

 

 Experience Centres 


 

 

 

 
 Newsroom
 

 

 

 

 
 Featured topics
 

 

 

 

 
 Insights and reports
 

 

 

 

 
 Press resources
 

 

 

 

 
 Investor relations
 

 

 

 

 Global newsroom 


 

 

 

 European newsroom 


 

 

 

 Eastern Europe, Middle East Africa newsroom 


 

 

 

 AI 


 

 

 

 Cybersecurity 


 

 

 

 Open finance 


 

 

 

 Small business 


 

 

 

 Digital assets 


 

 

 

 Consumer Acquisition & Engagement 


 

 

 

 Insights & Intelligence 


 

 

 

 Mastercard Economics Institute 


 

 

 

 Spendingpulse 


 

 

 

 Mastercard Business Intelligence 


 

 

 

 Press releases 


 

 

 

 Executive bios 


 

 

 

 Media contacts 


 

 

 

 Access our latest financial reports 


 

 

 

 Mastercard unveils tools to enable more intelligent agentic commerce
 
Mastercard is helping to shape the future of AI-powered payments and laying the foundation for trusted agentic transaction standards.

 What is agentic commerce? Your guide to AI-assisted retail
 
Understand how AI-powered agents are changing online shopping by streamlining choices and automating purchases.
AI
March 5, 2026
 
When AI starts buying for you, trust becomes the product
Mastercard introduces Verifiable Intent – a new, standards-based trust paradigm for agentic commerce, co-developed with Google.
Pablo Fourez
Chief Digital Officer, Mastercard
As AI agents begin to buy on our behalf, commerce is entering a new era. 
Search, shopping and purchasing are converging as AI systems move from assisting consumers to acting for them — planning purchases, making decisions and executing transactions autonomously. As this shift accelerates, a critical question comes into focus: How do we know an agent is doing exactly what we asked — and nothing more? 
This is a new payments paradigm. And in this paradigm, trust becomes the product.
When AI agents act with real money, consumers aren’t just looking for speed or convenience. They expect clarity about what was authorized, confidence that instructions were followed, and protection if something goes wrong. As autonomy increases, trust cannot be implied. It must be proven.
For decades, commerce relied on a simple, visible sign of intent. You tapped your card or clicked “buy,” and every party understood what you chose to purchase. That shared understanding is what makes digital commerce work today.
 Agentic commerce changes that equation . Instead of acting directly, consumers delegate. They might ask an agent to reorder their groceries, book travel within a budget, or buy a specific item in the right size. The agent interprets those instructions, monitors conditions, and may act independently to make the purchase. As a result, intent becomes less visible at the moment of transaction, even as it becomes more important to verify. 
Consumers need confidence and verifiable evidence that agents will follow instructions while maintaining privacy. Merchants need assurance that an agent is authorized to transact. Issuers must distinguish legitimate activity from fraud. And if something goes wrong, everyone needs facts — not guesswork.
Meeting these needs requires a new model of trust, designed specifically for agentic commerce, and built with privacy at the center.
To meet this moment, we’re collaborating with Google to introduce  Verifiable Intent , a new open, standards-based trust layer for agentic commerce. 
Aligned with Google’s Agent Payments Protocol (AP2) and Universal Commerce Protocol (UCP) and designed to be protocol agnostic, Verifiable Intent creates a tamper-resistant record of what a user authorized when an AI agent acts on their behalf, establishing a shared source of truth across the ecosystem. It provides cryptographic proof of authorization that consumers, merchants, and issuers can rely on.
In the coming months, Verifiable Intent will be integrated directly into Mastercard Agent Pay’s intent APIs to drive real-world adoption with partners and support responsible, scalable agent deployments across platforms. In parallel, Mastercard will continue working with industry bodies to define complementary standards for conversational AI in commerce.
This is not simply about enabling new payment experiences. It is about ensuring that as commerce becomes more autonomous, consumer protection keeps pace.
 
How do we rethink trust in an AI-driven world of autonomous agents? 
In an agentic world where actions are delegated, intent must be explicit and verifiable. Mastercard’s role in this new payments paradigm is to ensure that trust travels with every transaction, regardless of how it is initiated. 
At its core, Verifiable Intent links identity, intent, and action into a single, privacy-preserving record. It confirms the cardholder authorizing the AI agent, captures the consumer’s specific instructions and records the interaction between the agent and merchant resulting in a purchase. If a dispute occurs, all parties can rely on a clear audit trail to resolve it quickly and fairly.
For merchants, this clarity brings confidence to this new horizon of agentic transactions. For consumers, it provides peace of mind that delegation does not mean loss of control.
In agent-assisted, human-in-the-loop purchases, Verifiable Intent confirms the consumer was present, approved the shopping cart, and authorized the transaction. Merchants can fulfill these orders confidently without adding friction. In more autonomous scenarios, Verifiable Intent provides transparency and agency that allows merchants to assess whether additional confirmation is needed before completing an agentic transaction. 
These challenges extend well beyond traditional consumer transactions. In machine-to-machine commerce and programmable money implementations, a consumer or business is always delegating spending authority to a system. Whether an AI agent is paying for critical resources or managing procurement and executing a cross-border payment on behalf of an organization, the stakes are the same. These systems must make decisions at speed and scale while remaining faithful to the intent of the user.
 
How does Verifiable Intent preserve privacy and data control? 
Trust and privacy are not tradeoffs. Verifiable Intent uses  Selective Disclosure, a privacy control technique , to ensure that only the minimum necessary information about the transaction is required to be shared across parties, and only when needed. Transaction details can be verified for fraud mitigation or dispute resolution without exposing sensitive information beyond that process. 
This approach aligns with Mastercard’s data and technology principles, preserving control for consumers and merchants alike. 
 
What does a future-proof trust layer for agentic systems look like? 
Verifiable Intent is built on widely adopted specifications from the FIDO Alliance, EMVCo, the Internet Engineering Task Force, and the World Wide Web Consortium. It is designed to work across agentic protocols, devices, wallets, platforms, and even other payments networks today and as the ecosystem evolves.
Over time, it will be strengthened through integration with  Verifiable Credentials , making consumer authorization and delegation even more explicit, portable and cryptographically verifiable.
Today, Mastercard is open-sourcing the Verifiable Intent specification and an initial reference implementation on  GitHub  and at  verifiableintent.dev . Agent platforms, payment and checkout enablers, merchants, and developers are invited to review, contribute, and build. API specifications and developer tools for using Verifiable Intent with Mastercard Agent Pay will be available soon on  Mastercard Developers .
As AI agents take on more responsibility, payments become a reflection of trust. In this new payments paradigm, consumers want more than efficiency. They want confidence, accountability, and reassurance that someone has their back when AI acts on their behalf. 
Verifiable Intent is built to deliver on that promise. When integrated into Mastercard Agent Pay, it serves as the heart of a system providing clear proof of authorization, accountability, and recourse. As commerce becomes more autonomous, trust won’t take a backseat. It will matter even more.
 
What they're saying
“As AI agents begin to act more independently, it’s essential that user intent remains clear, provable, and protected,” said Stavan Parikh, vice president and general manager, Payments, at Google. “Strong, interoperable trust infrastructure like Verifiable Intent that is compatible with Agent Payments Protocol is a natural accelerator for scaling agentic commerce, and we’re proud to have collaborated with Mastercard on this initiative.”
“Merchants have built their businesses on the trust of their customers,” said Tom Adams, chief technology officer at Adyen. “As consumers increasingly transact through AI agents, having a verifiable, privacy-preserving way to confirm customer intent becomes foundational. Approaches like Verifiable Intent can help merchants anchor agent-initiated transactions in explicit authorization, while retaining control over identity, data, and the customer experience.”
“Over the last couple of months we’ve seen adoption of AI agents skyrocket,” said James Armstead, chief technology officer at Basis Theory. “As these agents start participating directly in commerce — making purchases and completing transactions on behalf of consumers and businesses — the most important question becomes trust. How do you know the intent behind a transaction is real? Mastercard’s Verifiable Intent API is an important step toward solving that. By combining Mastercard’s network with Basis Theory’s tokenization and secure data infrastructure, we can help enable a new model of commerce where agents can initiate and complete payments safely and transparently.”
“As Al agents begin making purchases on behalf of consumers, trust and clear proof of intent will be essential. Mastercard's Verifiable Intent is an important step toward making sure those transactions are authorised and secure,” said Meron Colbeci, chief product officer at Checkout.com. “Checkout.com supports open standards that help enterprise merchants adopt agentic commerce with confidence across schemes, platforms and protocols.”
“As merchants increasingly navigating new forms of digital delegation, our role at Getnet is to ensure we’re delivering the consistency to move forward with confidence,” said Juan Franco, CEO at Getnet. “Initiatives such as Verifiable Intent contribute to that alignment, supporting responsible innovation while reinforcing the safeguards merchants and consumers rely on every day.”
“Verifiable Intent marks a meaningful step forward in how intent, authentication, and accountability are established in agentic commerce,” said Sanjay Saraf, chief product officer, Merchant Solutions

### proof.com
<https://www.proof.com/blog/identity-infrastructure-agentic-internet-x401>
*1856 слов · direct*

AI agents can now buy, sign, build, publish and move money. What they can't carry is proof of who authorized the agent.
 Every company is racing to open its products to AI . The hard part isn't getting agents to act; it's trusting that a real person authorized them . Without that, a service has no safe way to let an agent through.
Today, Proof, the identity authorization company , launched x401, an open, issuer-neutral protocol that lets any website or API ask for and verify the identity behind agents.
With x401, a service can ask for the proof it requires: verified identity, age, membership, organizational affiliation, signing authority, proof of humanness, orf another trusted claim. The agent presents a compatible credential and authorization. The service verifies the issuer, claim, scope and action before proceeding. 
Identity establishes who or what an agent represents. Authorization establishes what it is permitted to do. x401 binds the two into proof and unlocks agents' ability to act on people’s behalf.
 “AI is making actions and content effortless to generate. Trust will come from knowing who stands behind them,” said Pat Kinsel, founder and CEO of Proof. “x401 gives every service a common way to ask for proof. Proof Digital ID gives people and organizations a high-assurance way to answer—with a signed record of who authorized what.” 
 Open by design 
x401 is an open protocol allowing any conforming issuer to deliver x401-compatible credentials. Any agent can present them. Every service determines which claims, issuers and levels of assurance it will accept.
That separation allows one protocol to support many forms of authority without forcing the internet to adopt a single identity provider or credential model.
x401 was developed by Proof with technical contributors from leading payments, identity and AI organizations. The public specification, implementation materials, and complete contributor list are available at x401.id .
Proof will submit x401 to the FIDO Alliance’s agentic authentication standards workgroup.
 Built to complete the agent stack 
x401 is designed to work with the protocols already emerging around agentic activity. In payments, x402 enables machines to make payments. AP2 and Verifiable Intent capture instructions and approvals in commerce. x401 now completes the missing link, when used together with these other protocols, agents can now pay, prove a person’s identity, and authorize specific actions.
 “x402 is the open standard that lets agents pay for web resources over HTTP with pay-per-request settled in stablecoins, with no accounts or API keys. Through Circle Agent Stack and USDC, which settles nearly all x402 volumes, Circle has been one of its core contributors. x401, built with Proof, pairs that with identity: x402 answers how an agent pays, x401 answers who it is. Those are the first two questions any agentic transaction has to clear, and now each has an open standard. Circle is proud to be an early adopter and co-endorser of x401." — Gagan Mac, VP Product, Circle 
 Proof’s digital identity: A high-assurance identity that can sign 
Proof is launching the first live implementation that can satisfy an x401 challenge. Built on Verifiable Credentials, Proof’s digital identity is the world’s first inline implementation of OID4VC Issuance and Presentation, allowing people to verify their identity to an IAL2 standard and enroll just-in-time or instantly reauthenticate with a biometric. Developers simply request identity and Proof manages the complexity of who is enrolled vs not.
Using selective disclosure and zero-knowledge proofs, someone can prove that they are verified, their nationality, over a required age or authorized to represent an organization without exposing their complete identity record.
In addition to credential presentation, Proof’s platform is the first to support transaction signing, which produces verifiable records. The API supports signing authorizations like AP2 with Verifiable Intent and cryptographically binds a verified identity to any payment, transaction, or payload. Verifiable records prove who you are and what you’ve authorized, creating the evidence that every industry requires in the agentic era. U.S. law has recognized agreements made by electronic agents for decades. Proof provides what's been missing: trustworthy proof of the person behind the transaction.
Proof’s digital identity is backed by Proof's Kantara-certified NIST IAL2 identity service and WebTrust-audited certificate-authority infrastructure. As a Certificate Authority that pairs a publicly trusted, audited certificate hierarchy with IAL2-grade identity proofing, Proof’s digital identity is the only legal credential that can secure everything a person signs, does in person, does online, or delegates to an agent.
 x401 works end-to-end today 
The documentation for x401 is live today. The public specification, technical documentation, sample apps, and contributor list are available at x401.id . 
Proof Digital ID documentation is available at dev.proof.com .
Developers can connect Proof’s live x401 MCP server to Claude and ChatGPT to use x401 in real agent workflows.
Participating organizations will announce their implementations as they become available.
Subscribe to our newsletter
Related Articles
Title lorem ipsum
Title lorem ipsum
Title lorem ipsum
Proof Launches x401, Giving AI Agents A Way to Prove Who They Represent - and What They're Authorized To Do
The Fraud Files: When Fraud Went Corporate | October 2026
Anatomy of a Fraud Attempt: The Password Reset That Was the Attack
How Businesses Reduce Help Desk Social Engineering Attacks
Candidate Fraud and the Continuity Gap in Remote Hiring
Proof Appoints Jeremiah Glodoveza as Chief Marketing Officer
An AI Just Passed the Video Turing Test. Who's on Your Next Call?
What Makes ID Checks Fail
Anatomy of a Fraud Attempt: the Photograph of a Building Nobody Owned
Can AI Deepfakes Bypass Identity Verification?
How Companies Prevent Account Takeover Fraud
How to Verify the Identity of an AI Agent
Face Rental: The Candidate Fraud That Passes Every Document Check
The Seller Who Isn't in the Room: What Remote Closings Actually Fix in Title and Escrow
The Exception Desk: Wire Callbacks | September 2026
Why Fake Candidates Stopped Standing Out in Your Pipeline
Proof and Superfluid: A Verified Human Behind Every Agent Transaction
The Fraud Files: When the Verification Layer Became the Target | September 2026
The Last Mile That…Wasn't: Notarization Challenges in Lending and Equipment Finance
Why The Right Fraud Tools Can Help Stop Seller Impersonation
Remote Online Notarization: The Last Analog Step in Digital Transformation
Proof Launches Portable Digital Identity for Banks as Federal Regulators Recognize Verifiable Credentials Under CIP Rules
What is a Fraud Signal?
What Is MISMO Certification, and Why Do Mortgage Lenders Care Which RON Platform Has It?
The Sellers Never Showed Up. The Houses Sold Anyway.
Mobile Notary, Online Notary, or Traditional Notary: When Should You Use Which?
What Businesses Need to Know About ID Scans and Retention Risk
Six Money-Out Moments Worth Auditing in Your Firm
What Deepfake Detection Actually Analyzes in a Candidate Video
See Your Fraud Data, Keep Your Transaction History, and Close with Confidence. What’s new in August.
How Equipment Finance Companies Close Loans Remotely
Authentication Verifies What You Have, Not Who You Are
Sanctions screening is live. Your KYB record isn't.
What Actually Happens During a Video Identity Verification Session with Proof
How to Catch Candidate Fraud Without Changing Your Greenhouse Workflow
72 Fake Sites, One Phone Call: Vishing Hits Private Equity
The Messy Identity Verification Stack Behind Most Online Gaming Platforms
Why Identity-Verified Signing Matters, and How to Evaluate It
The Three Identity Checks in an Auto Deal, and Why the Last One Breaks
The Fraud Files: When Trust Became the Attack Surface | August 2026
Electronic Signatures and Digital Signatures: The Difference and Why It Matters
1,000 Companies in 3 Months: North Korea's Hiring Infiltration
How to Evaluate eClosing Platforms
Inside the Fake-ID Detection Stack
How to Evaluate an Online Notary
The Attack That Breaks the Identity Check You Just Deployed
The 3 Checks That Catch Most Fake IDs Online
Which Digital Signature Standard Is Actually Secure?
The One E-Signature Feature That Actually Verifies Identity
Is There a Best eClosing Platform? Here's the Short Answer
What Makes a Good Online Notary? 3 Things That Actually Matter
More Ways to Verify, Authorize, and Protect. July Is Here.
Fake IDs, Fake Deeds, and $1.5M in Stolen Land
Who's Really Behind That Business? Why KYB Alone Can't Stop Invoice Fraud
Your Account Recovery Process Is Your Biggest Security Gap
The Authorization Gap: Why Agentic Commerce Can't Scale Without an Identity Layer
What Identity Verification Actually Looks Like for Your Real Candidates
The Real Cost of a Manual POA Process at Your Credit Union
A Historic Step Toward the American Dream
This Is What Candidate Fraud Looks Like From the Inside
The Fraud Files: Agents, Impersonation, and the Identity Layer Nobody Built | July 2026
What Is Digital Identity? A Complete Guide
The Return to In-Person Interviews Is an Admission, Not a Strategy
Why Auto Lenders Can't Afford to Keep Mailing POAs
When You Find One Fraudulent Hire, You Usually Find More
The Identity Infrastructure for the Internet
The Five Levels of Verified Identity For the Agent Economy
Introducing x401: Bringing Proof of Identity to the Web
Proof Launches x401, the Open Protocol for Verifying the Authority Behind AI Agents
Why You Can’t Get Pokémon Center Drops (Hint: It’s Not Just Site Issues)
The Fraud Files: Stolen Credentials, Fake Biometrics, and the Synthetic Identity Wave | June 2026
Sherpas Healthcare Solutions Wins More Clients with Remote Online Notarization
Cleaner Data, Tighter Security, and More Admin Control This June
Electronic Signatures vs. Digital Signatures: What's the Difference?
How Generative AI Turned Candidate Fraud Into an Industry
Why Equipment Finance Teams Can't Afford a Manual POA Process
How to Implement Digital Identity Verification
Is Remote Online Notarization Legal and Available in All States? 
Why Only 31% of CHROs Are Confident They Can Stop Hiring Fraud
Real Estate Fraud Hit $275M in 2025. The Fix Isn't Better Agent Training.
Proof Puts Itself To The Test For Account Recovery
Your Interviewers Can't Catch Deepfakes. That's Not Their Fault.
The Top States for eClosings in 2026
What is Remote Online Notarization?
How to Catch Candidate Fraud Without Changing Your Lever Workflow
Proof and Enigma Partner to Launch a Verified Business Identity and Authorization Layer for U.S. Businesses
Salesforce Under Attack: What the ShinyHunters Breach Reveals About CRM Identity Risk
A Better Way to Notarize, for Cohen & Fitch LLP and Every Client They Serve
Verified Identities, New Closing Types, and Faster Document Prep. Here's What's New in May.
The Fraud Files: Bank Insiders, BEC Billions, and the AI Threat to ACH Payments | May 2026
The Interview Isn't Where Candidate Fraud Gets Caught
The Insider Threat Your Hiring Pipeline Was Never Built to Catch
The New Generation of Scattered Spider Is Turning Account Recovery Into a Seven-Figure Business
Real Names, Fake IDs, and a Bank Insider: The Massachusetts Fraud Ring That Beat Two Lines of Defense
Agentic AI Needs Verifiable Records to Be Trusted
Proof Joins FIDO Alliance to Link AI Agent Actions to Verified Human Identity
The Fraud Files: Fraud Rings, AI Scams, and the Signals to Watch | April 2026
Wigs, Fake IDs, and $19.8 Million in Loans: What the NFL Impersonation Scam Means for Lenders
Built for How You Work | What's New at Proof in April
The VINsanity Indictment and the Urgent Need for Banks to Adopt Real Identity Verification

### ncua.gov
<https://ncua.gov/regulation-supervision/regulatory-compliance-resources/bank-secrecy-act-resources/frequently-asked-questions-regarding-treatment-verifiable-digital-credentials>
*768 слов · direct*

Search
Jump to...
 September 8, 2026 
The U.S. Department of Treasury’s Financial Crimes Enforcement Network (FinCEN), jointly with the staffs of the Board of Governors of the Federal Reserve System, the Federal Deposit Insurance Corporation, the National Credit Union Administration, and the Office of the Comptroller of the Currency (the “Agencies”), are issuing two new frequently asked questions (FAQs) that address the use of state-issued mobile driver’s licenses (mDLs) and other government-issued verifiable digital credentials, which may be used to verify identities of natural person customers under the Customer Identification Program (CIP) Rule. 1 These FAQs explain how the CIP Rule may apply to such verifiable digital credentials (VDCs). Additionally, FinCEN and the Agencies are amending a previously issued FAQ to reflect updated terminology being used to describe VDCs. 2 The answers to these FAQs neither alter existing BSA legal or regulatory requirements nor establish new supervisory expectations. 
31 C.F.R. § 1020.220(a)(2)(ii) - Customer Verification
What is a verifiable digital credential?
A verifiable digital credential, or VDC, is a data structure that contains information about an individual, is digitally signed by the issuing source of the information, is cryptographically bound to a device, and is protected by an activation factor. An activation factor is something the user knows (e.g., a PIN or password) or a unique attribute they possess (e.g., a physical biometric, like a face or finger-print).
Can a bank or credit union use a government-issued verifiable digital credential (VDC), such as a state-issued mDL, to verify the identity of a customer who opens an account, either in-person, remotely over the Internet, or through some other digital or virtual channel?
Yes, a mobile driver’s license, or mDL, is a VDC format for a driver’s license or identity card that is issued by a state government and contains all of the same information as a physical driver’s license. As such, a bank or credit union may consider accepting such a credential provided that the bank or credit union can meet the requirements of the CIP Rule. The CIP Rule neither requires nor prohibits reliance on such government-issued VDCs as a means of verifying a customer’s identity. For the purposes of 31 C.F.R. § 1020.220(a)(2)(ii)(A)(1), an unexpired, government-issued VDC, such as an mDL, would qualify as a “government-issued identification,” though it must also “evidence nationality or residence and bear a photograph or similar safeguard.” Accordingly, if the bank or credit union maintains the appropriate technology or systems to extract the relevant information from a government-issued VDC and it is allowable under the bank’s or credit union’s CIP, it may consider unexpired state-issued mDLs or other unexpired government-issued VDCs that “evidenc[e] nationality or residence and bear a photograph or similar safeguard” as one of the documentary methods it uses to verify a customer’s identity.
As with other forms of government-issued identification, a bank or credit union generally may rely on a government-issued VDC as verification of a customer’s identity; however, if a government-issued VDC shows indications of fraud, the bank or credit union must consider that factor in determining whether it can form a reasonable belief that it knows the customer’s true identity.
Update to previously published Final CIP Rule FAQ: 31 C.F.R. § 103.121(b)(2)(ii) - Customer verification
Can a bank or credit union use an electronic credential, such as a digital certificate or a verifiable digital credential, as a non-documentary means to verify the identity of a customer who opens an account either in-person, remotely over the Internet, or through some other digital or virtual channel?
A bank or credit union may obtain an electronic credential, such as a digital certificate or a verifiable digital credential, as one of the methods it uses to verify a customer’s identity, to the extent permitted by the bank’s or credit union’s CIP. However, the CIP Rule requires the bank or credit union to have a reasonable belief that it knows the true identity of the customer. Therefore, for example, for electronic credentials and verifiable digital credentials issued and maintained by a non-government third party, the bank or credit union is responsible for ensuring that the third party uses the same level of authentication as the bank or credit union itself would use. See also FFIEC guidance titled “Authentication in an Electronic Banking Environment” (Updated: September 2026)
Footnotes
 1 31 C.F.R. § 1020.220.
 2 See Board of Governors of the Federal Reserve System, Federal Deposit Insurance Corporation, FinCEN, National Credit Union Administration, Office of the Comptroller of the Currency, Office of Thrift Supervision, and Treasury, FAQs: Final CIP Rule , 31 C.F.R. § 103.121(b)(2)(ii) -- Customer verification, FAQ #3, available at https://www.fincen.gov/system/files/guidance/finalciprule.pdf .

### Прочие ссылки (без извлечённого текста)

- <https://x401.proof.com/spec/latest>
- <https://pages.nist.gov/800-63-4/sp800-63a/ial>
- <https://www.consumerfinance.gov/rules-policy/regulations/1005/6>
- <https://www.consumerfinance.gov/rules-policy/regulations/1005/11>
- <https://www.consumerfinance.gov/rules-policy/regulations/1005/2>

## Контекст

<!-- enrichment:context -->
# Context-enrichment: Fintech Brainfood — the protocols for agentic banking and payments
_Analytical notes (not a post). Importance: 4/5._

## [0] What exactly happened (de-PR'd)
Simon Taylor's Fintech Brainfood essay is a **map-making, not a news event**: it tries to impose order on the now-crowded agentic-commerce protocol stack by sorting the pieces into **four jobs** rather than treating them as rival "winners":
- **Personal Agent Protocol (PAP / "Poppy")** — recognise the agent and sign the customer in; scoped, revocable access. (Meta + Sierra; draft 0.1 published **9 Oct 2026**, 35+ design partners incl. OpenAI, Visa, Mastercard, PayPal, Plaid, BofA, Wells Fargo, Chime.) The "who do I let in and with what rights" layer. See [[Meta and Sierra introduce Personal Agent Protocol standard]].
- **x401** (Proof, launched **15 Oct 2026**; v0.1.0 had shipped Jun 2026) — "bring proof about the human": a service asks for verified identity/age/eligibility to **NIST IAL2**, the agent presents a credential, the service verifies issuer/claim/scope. The identity-and-authorization layer.
- **MCP** (Model Context Protocol) — "give the agent things it can do": OAuth 2.1-based tool discovery/invocation; the provider decides what's allowed.
- **Verifiable Intent** (Mastercard + Google, **Mar 2026**) — "prove what the user authorised": a tamper-resistant, privacy-preserving record binding identity → intent → action, integrated into Mastercard Agent Pay's intent APIs. See [[Mastercard launches Verifiable Intent trust layer with Google]].

**Why framed this way, and what it reveals:** Taylor's real argument is that these are **complementary layers, not competitors** — identity (x401), permission/capability (MCP, PAP), and proof-of-authorisation (Verifiable Intent / AP2) sit on top of payment rails (x402, ACP, Agent Pay). The de-PR'd punchline: the "protocol wars" headline is mostly **stack-layering**, and the genuinely new, under-covered brick is **x401** — because it plugs the identity hole, and because **FinCEN's Sep 2026 CIP guidance** (banks may use verifiable digital credentials under the Customer Identification Program) makes reusable, IAL2-grade proof **bank-ready**, not just a consumer handshake. The essay also flags the **regulatory gap nobody's protocol solves**: US **Reg E** (unauthorized-transfer liability, error resolution) still governs anyone moving money, and none of these specs by themselves answer "who eats the loss when an agent buys the wrong thing."

## [1] Competitors / peers
The field is now a **layered stack with multiple contenders per layer** — the essay's whole point:
- **Payment / checkout layer:** OpenAI+Stripe **ACP** (announced 29 Sep 2025; Shared Payment Token; merchant stays merchant-of-record; Instant Checkout in ChatGPT launched Feb 2026 then **scaled back Mar 2026** — see [[OpenAI scales back ChatGPT shopping plans]]); Google **AP2** (16 Sep 2025, 60→100+ partners, Mandate VCs, rail-agnostic; **donated to FIDO Alliance**, v0.2.0 added "Human Not Present" autonomous pay Apr 2026); Coinbase **x402** (HTTP-402 stablecoin pay-per-request, now under **Linux Foundation**, 40+ members incl. Visa/MC/Stripe/Google/AWS/Circle; V2 Dec 2025); **Mastercard Agent Pay** and **Visa Intelligent Commerce / Trusted Agent Protocol (TAP)** (Visa+Cloudflare PKI "digital passport"; see [[Visa launches Trusted Agent Protocol for AI commerce]]).
- **Identity layer:** **x401** (Proof) is essentially alone as a *live, IAL2* implementation; competes conceptually with Visa TAP's lighter agent-attestation and AP2's mandate model.
- **Authorisation-record layer:** Verifiable Intent vs AP2 Mandates — now **converging inside FIDO's Agentic Authentication WG** (formed Apr 2026; Google donated AP2, Mastercard donated Verifiable Intent). See [[Google and Mastercard back FIDO Alliance on agentic commerce standards]].

**Why the landscape is this way / second-order:** the networks (Visa/Mastercard) and the AI platforms (OpenAI, Google, Meta) are each trying to **own the trust/authorisation layer** because that is where durable rent lives — the rails are commoditising (stablecoins via x402 settle "with no accounts or API keys"). So the fight isn't "which protocol pays" but **"whose record of intent/identity merchants and issuers rely on"**. Consolidation into FIDO/Linux Foundation is the tell: when everyone donates their spec to a neutral body, it means **no single sponsor could win it alone**, and the value migrates from the protocol to whoever controls distribution (the issuer relationship, the agent platform, the identity wallet).

## [2] Company history / fit
Brainfood/11:FS (Taylor) is a **synthesiser/standard-explainer**, not a vendor — its "product" is sense-making for banks, so a four-box taxonomy that de-hypes the protocol wars is exactly on-brand. The underlying actors fit their structural incentives: **Mastercard/Visa** keep adding trust layers (Verifiable Intent, TAP, Agent Pay) because their take-rate is defensible only if they remain the **dispute/liability arbiter** as checkout de-materialises; **Proof** (identity-authorization co., prior bank/Visa tie-ups — [[Proof partners with Visa to secure high-risk transactions]]) is pushing x401 to become the **reusable KYC credential**, leveraging the FinCEN CIP opening to sell into banks; **Meta/Sierra/OpenAI** push PAP because the agent platform that owns the *sign-in handshake* owns the customer. Each is extending from its moat toward the one scarce asset: **a trusted record of who authorised what.**

## [3] Novelty / value-add / traction
**Genuinely new (vs the Mar 2026 Verifiable Intent note and the 2025 protocol announcements):** (a) **x401 going live (15 Oct 2026)** as the first IAL2 identity answer with a working MCP server usable from Claude/ChatGPT — identity was the missing brick everyone hand-waved; (b) the **FinCEN CIP / verifiable-digital-credential bridge** that makes agent identity *regulatorily usable inside banks* (see the NCUA/FinCEN FAQ, Sep 2026) — this is the real "bank-ready" unlock, not the protocol handshake; (c) the **PAP/Poppy** sign-in layer (Oct 2026) formalising scoped, revocable agent access.

**Traction reality check (anti-PR):** most of this is **specs + reference implementations + design partners**, not GMV. Verifiable Intent is still "being integrated into Agent Pay in coming months"; PAP is **draft 0.1**; x401 is live docs + sample apps + "participating orgs will announce as available." ACP's flagship (ChatGPT Instant Checkout) was **pulled back** in Mar 2026. So: **announced/piloted, not yet adopted at scale.** The only hard live-transaction evidence in the corpus is network pilots (Mastercard/Visa first-agent-payments in Portugal, Netherlands, France, Mexico, Brazil — single transactions, not volume).

**Who captures the margin (1 level deeper):** if settlement commoditises to stablecoins (x402) and checkout tokens (ACP), the margin moves **up to identity + authorisation-record + dispute**. Whoever owns the IAL2 credential (Proof?) or the issuer-side intent record (Visa/MC via FIDO) captures rent; the AI platforms capture it only if they own the sign-in (PAP). The risk for banks: they become the **balance-sheet-of-last-resort for Reg E liability** while the record-of-intent — and the fee — sits with a network or an identity provider.

## [4] What's next / market sentiment
Direction: **standards consolidation, then a liability fight.** FIDO's Agentic Authentication WG (AP2 + Verifiable Intent) and the Linux Foundation's x402 are collapsing the "wars" into a shared stack through 2026–27; Secure Technology Alliance meets Nov 2026. McKinsey-cited sizing: **$3–5T agentic transaction volume by 2030** (vendor-quoted, treat as directional). The counterintuitive second-order effect: **more/better protocols do not resolve the hard question** — Reg E error-resolution and unauthorized-transfer liability are **unsolved by any spec**, so the binding constraint shifts from "can the agent pay" to **"who is liable when the agent is wrong, and whose record proves intent in a dispute."** Risks: fragmentation (too many overlapping specs → merchants adopt none), prompt-injection / "whisper" attacks on mandate-signing (noted in arXiv security analyses of AP2/x402), and **regulatory lag** — banks will move only once CIP/Reg E treatment is unambiguous.

**Freshness verdict: FRESH.** This is original analysis/synthesis by Simon Taylor; no prior Brainfood essay note covers this taxonomy. It *references* events already in the corpus (Verifiable Intent [[Mastercard launches Verifiable Intent trust layer with Google]], PAP [[Meta and Sierra introduce Personal Agent Protocol standard]], TAP [[Visa launches Trusted Agent Protocol for AI commerce]]) but is not a re-report of any single one — it is the connective tissue. Keep.

## Sources
- personalagentprotocol.org/docs/introduction; sierra.ai/blog/poppy (PAP/Poppy draft 0.1, 9 Oct 2026)
- proof.com/blog/identity-infrastructure-agentic-internet-x401; x401.id (x401 launch 15 Oct 2026, IAL2)
- mastercard.com .../verifiable-intent.html (Verifiable Intent, Mar 2026, co-dev w/ Google)
- ncua.gov / FinCEN CIP FAQ on verifiable digital credentials (8 Sep 2026)
- MCP authorization spec (OAuth 2.1); consumerfinance.gov Reg E (1005)
- fidoalliance.org — Google donates AP2 to FIDO; Agentic Authentication WG (Apr 2026)
- crossmint.com / openfort.io / openhermit.com — ACP vs AP2 vs x402 vs MPP comparisons (2026)
- Internal: [[Fintech Wrap Up ACP vs AP2 vs TAP protocol wars reference]], [[Mastercard launches Verifiable Intent trust layer with Google]], [[Meta and Sierra introduce Personal Agent Protocol standard]], [[Google and Mastercard back FIDO Alliance on agentic commerce standards]], [[Visa launches Trusted Agent Protocol for AI commerce]], [[OpenAI scales back ChatGPT shopping plans]], [[Proof partners with Visa to secure high-risk transactions]]
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
## Red-team / challenge questions

1. **Is this actually one stack or competing stacks?** Taylor says complementary layers; but ACP (merchant-of-record + card token) and x402 (accountless stablecoin) and AP2 (mandate VCs) overlap on "how does the agent pay." Answer: *mostly* layered, but the payment layer itself has 3+ rivals → fragmentation risk is real, not resolved. (partially open)

2. **What is genuinely NEW here vs March 2026?** Only x401 going live (15 Oct) + FinCEN CIP bridge + PAP draft are new; Verifiable Intent, AP2, ACP, TAP all pre-date. The novelty is the *identity brick + bank-readiness*, not payments. (answered)

3. **Announced vs live?** PAP = draft 0.1; Verifiable Intent = "coming months" into Agent Pay; x401 = live docs/sample apps, no named production merchants; ACP = Instant Checkout *pulled back* Mar 2026. Verdict: specs + pilots, near-zero GMV disclosed. (answered)

4. **Who eats Reg E liability when an agent buys wrong?** No protocol answers this. Reg E error-resolution/unauthorized-transfer rules still bind. This is the unsolved core, and the essay flags it. (open — structural)

5. **Does FinCEN's CIP guidance really make agent identity "bank-ready"?** The FAQ *permits* verifiable digital credentials but neither requires them nor sets new expectations; banks remain responsible for third-party assurance. So "bank-ready" is permission, not mandate. (answered — overstated by PR)

6. **Why donate everything to FIDO/Linux Foundation?** Because no single sponsor could win the standard alone; value migrates from spec to distribution (issuer relationship, identity wallet, agent sign-in). (analysis)

7. **Who captures the margin if rails commoditise?** Identity (Proof/x401), authorisation-record (Visa/MC via FIDO), or sign-in owner (Meta/OpenAI via PAP). Banks risk becoming liability balance-sheet while fee sits elsewhere. (analysis)

8. **Is x401 really alone at IAL2, or marketing?** Proof claims first live IAL2 + transaction-signing, Kantara-certified. Plausible but unverified at merchant scale; "participating orgs announce as available." (partly open)

9. **Could MCP's OAuth 2.1 auth layer make a dedicated identity protocol redundant?** MCP handles tool authz, not human IAL2 identity — different job. So no, but boundaries blur (confused-deputy risks noted in MCP spec). (answered)

10. **What's the attack surface?** arXiv work documents prompt-injection/"whisper" attacks on AP2 mandate-signing and free-riding/PII attacks on x402. Signing the transaction ≠ signing the decision. Security is unsettled. (open)

11. **Is the $3–5T-by-2030 TAM credible?** McKinsey/vendor-quoted; directional only, no adoption base to extrapolate from. Treat skeptically. (open)

12. **Does ChatGPT Instant Checkout's pullback undercut the thesis?** Yes — the most-hyped live deployment retrenched to app-model in Mar 2026, evidence that UX/liability isn't solved. (answered)

13. **Who needs whom more — networks or AI platforms?** Networks need agent distribution; AI platforms need trusted settlement + dispute. Symbiotic now, but whoever owns identity+intent record has leverage. (analysis)

14. **Downside trigger?** A high-profile agent-mis-purchase dispute with unclear Reg E recourse, or regulators demanding issuer liability, would freeze bank adoption regardless of protocol maturity. (open)

15. **Is this note stale (dup of prior)?** No — it's Taylor's original taxonomy/synthesis, not a re-report of any single prior note. Fresh. (answered)

Importance: 4/5 — a clear, well-sourced synthesis of THE defining fintech-infra fight (who owns agentic trust/identity/authorisation), surfacing the genuinely new bricks (x401 live, FinCEN CIP bridge, PAP) and the unsolved liability core (Reg E), with named protocols, dates and partners. Not 5/5 because it's commentary on mostly-announced/piloted specs with little disclosed adoption, and it re-packages events already in the corpus rather than breaking news.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** Agentic commerce = AI agents searching, deciding and paying on a user's behalf. This essay sits at the *protocol/trust* layer below the money movement. Market sizing is wide and vendor-driven, so treat as directional: McKinsey projects up to ~$5tn global agentic commerce volume by 2030 (per McKinsey, via digitalcommerce360, 2025-10-20); Morgan Stanley sees US agentic e-commerce spend of ~$190–385bn by 2030 (per Morgan Stanley Research); Juniper pegs global agentic transaction value at ~$8bn in 2026 rising to ~$3.5tn by 2031 (per Juniper Research). The spread itself is the signal — nobody can size live volume yet; current adoption is pilots, not scale. **Structure:** fragmented at the protocol layer and consolidating fast around a few sponsors. Six-plus overlapping standards now exist — ACP (OpenAI/Stripe, Sep 2025), AP2 (Google, donated to FIDO Alliance Apr 2026), UCP (Google/Shopify), MCP (Anthropic), A2A (Google), x402/x401 (Circle/Proof), plus the networks' own Mastercard Agent Pay and Visa Trusted Agent Protocol/Intelligent Commerce (per digitalapplied, honeyb.ai, reactify, 2026). The note's own framing (PAP/Poppy for sign-in, x401 for human-identity, MCP for capabilities, Verifiable Intent for authorization) correctly reads these as *complementary layers*, not one winner — but that is also the generous reading. **Why now:** three forces converge — (1) agents are already generating site traffic that companies either block or let masquerade as the user (the PAP "all-or-nothing" problem); (2) FinCEN/Agencies' Sep 2026 FAQ lets banks use verifiable digital credentials inside CIP, making IAL2 proofs (x401/Proof) genuinely bank-ready; (3) the card networks are racing to avoid being disintermediated by stablecoin-native rails (x402 settles in USDC with no accounts/API keys — a direct bypass of card economics).

**Competitive landscape.** Sector KPIs at this layer: adoption breadth (issuers/processors live), interoperability (does an agent built to one spec clear across networks), and assurance level (IAL2 vs handshake). **Key players & basis of competition** — not price but *standard-setting and trust capture*: Mastercard (Agent Pay + Verifiable Intent, co-developed with Google, open-sourced on GitHub/verifiableintent.dev), Visa (Trusted Agent Protocol, launched 2025-10-14 — see [[Visa launches Trusted Agent Protocol for AI commerce]], [[Nuvei supports Visa Trusted Agent Protocol]]), Google (AP2, now FIDO-governed), OpenAI/Stripe (ACP), Circle/Proof (x402/x401 stablecoin + identity stack). **Recent moves:** both networks joined Google's AP2 in Sep 2025, and Mastercard maps AP2 mandates to its Agentic Tokens so an AP2 agent clears across both (per digitalapplied, 2026) — convergence, not a pure war. Mastercard completed *live* agentic transactions across LatAm with 17 issuers/processors (incl. Bancolombia, Santander, Itaú, Banamex, Pomelo) (per Mastercard newsroom/thepaypers, Mar 2026); Verifiable Intent has commitments from Google, Fiserv, IBM, Checkout.com, Adyen, Worldpay, Basis Theory, Getnet (per Mastercard story, finextra/pymnts, 2026). Internal precedent: [[PayPal integrates Mastercard Agent Pay into wallet]], [[Google and Mastercard back FIDO Alliance on agentic commerce standards]], [[PhotonPay completes first live agentic payment with Mastercard]], [[Mastercard and Rabobank complete Netherlands' first AI agent payment]]. **Mastercard's position:** *ahead on distribution, not on the stack* — its moat is the network (acceptance, issuer relationships, switching scale) and tokenization, not the protocol itself, which is deliberately open and protocol-agnostic. That is the honest read of Verifiable Intent: Mastercard isn't trying to own the standard, it's trying to keep the *authorization/dispute record* (and therefore the transaction) on its rails regardless of which agent protocol wins. De-PR: the Mastercard release is heavy on "trust is the product" and silent on economics — who pays the take rate on an agent-initiated purchase, and whether agent volume carries the same interchange.

**Comps & multiples.** This is an essay, not a Mastercard print, so comps are the two network duopolists as a sanity check on who can afford to set the standard. As of 2026-10-12 (per macrotrends/companiesmarketcap/simplywall.st):
- **Mastercard (MA):** market cap ≈ $523.3bn, P/E ≈ 32.8x, revenue TTM ≈ $35.1bn → P/S = $523.3bn / $35.1bn = **14.9x**.
- **Visa (V):** market cap ≈ $730.2bn, P/E ≈ 33.2x.
Both sit at the top of the P/E sanity range (~10–50x) — rich, but *in-line with each other* and justified by Mastercard's Q2 2026 growth (below). No standalone "agentic commerce" comps are publicly valuable: x402/Circle, Proof and the AI-agent settlement names are private or early (internal: [[Basis Theory raises $33 million for agentic commerce]] — $33m round, agentic-commerce infra; [[AEON raises $8 million to build settlement layer for AI agents]] — $8m), so distribution not computed, qualitative comparison only. EV/EBITDA / clean EV not computed — no free source → `[UNSOURCED]`.

**IR grounding (Mastercard Q2 2026, per 8-K EX-99.1 / earnings release, filed ~2026-07-30):** net revenue **$9.3bn, +12% currency-neutral**; GDV **$2.9tn, +8%** local-currency; switched transactions **+9%**; cross-border volume **+12%**; adjusted net income **$4.5bn (+16% c-n)**; adjusted diluted EPS **$5.04 (+19% c-n)**; **value-added services & solutions net revenue +20% (+18% c-n)** — the fastest-growing segment, and the bucket where agentic-commerce/trust products (Agent Pay, Verifiable Intent, tokenization, identity) actually monetize. The thesis link: Mastercard can fund an open, "give-it-away" trust layer precisely because the payoff is keeping a $2.9tn-GDV / 14%-revenue-growth franchise relevant as volume shifts to agents — the standard is a defensive moat spend, not a new revenue line yet. Source: SEC 8-K FY2026 earnings release.

**Risk flags.**
1. **Fraud/liability gap in agent-initiated payments (regulatory).** Reg E and EFTA were written for human-initiated transfers; as of late 2026 there's no federal framework clarifying whether delegating to an agent satisfies "authorization," and no reason code separating "agent error" from a genuine cardholder purchase (per chargeflow, worldpay, fenwick, 2026). PYMNTS (Sep 2026) found 93% of merchants think the AI/agent provider should eat the loss — today the merchant does. Verifiable Intent is explicitly aimed at this (tamper-resistant authorization record), but it mitigates *evidence*, not the unsettled legal allocation of loss. Second-order: until liability is settled, scaled autonomous (human-not-present) spend stays capped at pilots.
2. **Standards fragmentation / integration tax.** Six-plus overlapping protocols mean merchants and PSPs face an interop matrix, not one rail. Convergence via AP2/FIDO reduces this but isn't settled; a wrong bet on the losing spec is sunk cost. Second-order: fragmentation delays the volume the whole thesis depends on and favors whoever already has distribution (the networks) over pure-protocol startups.
3. **Disintermediation by stablecoin-native rails.** x402 (Circle/USDC) lets agents pay per-request with no card account or interchange. If agent commerce standardizes on that where it can, the card networks' take rate is bypassed at exactly the new-volume layer — the reason Mastercard is spending to stay in the authorization path. Second-order: Mastercard's defensive moat works only if issuers/merchants keep settlement on cards rather than stablecoins.

**What this changes (idea-lens).** `(analysis)` The agentic-payments fight is not "which protocol wins" but "who owns the authorization-and-dispute record," because that is what anchors the transaction to a rail and a liability chain. Falsifiable thesis: the card networks hold the money layer *if* liability law resolves in a card-friendly way and agent volume clears through tokenized card credentials rather than stablecoins. **Trigger/catalyst to watch:** (a) a CFPB/FinCEN rule or EFTA interpretation that explicitly covers agent-delegated authorization; (b) Verifiable Intent moving from "commitments" to disclosed *live cleared volume* in Agent Pay intent APIs; (c) first material agent dispute/chargeback that tests who pays. **What breaks the thesis:** stablecoin x402-style rails capturing a visible share of agent transaction value (watch Circle's x402 USDC volume), which would show the networks' trust layer didn't keep the money on cards.

Sources: https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000081/ma06302026-exx991xearnings.htm · https://www.mastercard.com/gb/en/news-and-trends/stories/2026/verifiable-intent.html · https://www.mastercard.com/news/latin-america/en/newsroom/press-releases/pr-en/2026/march/mastercard-advances-agentic-payments-in-latin-america-and-the-caribbean-with-live-transactions-completed-across-the-region/ · https://www.digitalapplied.com/blog/agentic-commerce-standards-ucp-acp-ap2-2026-merchant-guide · https://www.chargeflow.io/blog/agentic-commerce-regulation-what-merchants-need-to-know · https://www.worldpay.com/en/insights/articles/agentic-commerce-liability-is-still-being-written · https://www.digitalcommerce360.com/2025/10/20/mckinsey-forecast-5-trillion-agentic-commerce-sales-2030/ · https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook · https://www.macrotrends.net/stocks/charts/MA/mastercard/pe-ratio · https://simplywall.st/stocks/us/diversified-financials/nyse-ma/mastercard · https://www.proof.com/blog/identity-infrastructure-agentic-internet-x401
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
This is a commentary/essay on agentic-payment protocols, not an earnings event — **no full earnings report in the news**. But Mastercard is IR-covered and its own latest print materially grounds the thesis (the note cites Mastercard's Verifiable Intent as one of the four protocol building blocks), so a brief grounding:

**Latest print: Q2 2026 (quarter ended 2026-06-30, released ~2026-07).** Net revenue $9.3bn, +14% (+12% currency-neutral); GAAP diluted EPS $4.97 (+22% YoY), adjusted diluted EPS $5.04 (+21%); net income $4.4bn. Gross dollar volume +8%, cross-border volume +12%, switched transactions +9% (local-currency); Value-Added Services & Solutions revenue +20% (+18% cn). Management raised the FY outlook to the high end of the low-double-digit range. Verdict: BEAT / accelerating — but this only matters here as context, not as an event.

**Why it informs the agentic thesis.** On the Q2 call, CEO Michael Miebach framed agentic commerce as "shaping what's next in commerce" and flagged a "market-first Agentic Payment capability." Management's thesis: cards "prevail in both consumer and commercial use cases due to the security, transparency, and control offered by the card ecosystem." For the machine-to-machine (low-ticket, high-velocity) class, Mastercard launched **Agent Pay for Machines**, described as "the only network protocol facilitating this," with "over 30 industry leaders at launch." On settlement, management said stablecoins "are not the only option" — Mastercard wants to "enable choice" (spend stablecoin balances, settle on its network, move money). (earnings-call commentary)

**Thesis-flag (de-PR).** The Brainfood note slots Mastercard's **Verifiable Intent** (the "prove what the user authorised" layer, co-developed with Google, aligned to AP2) alongside PAP, x401 and MCP. Fact → the Q2 numbers show agentic has no measurable P&L contribution yet (growth is the familiar cross-border + VAS engine, not agents); why it matters → Verifiable Intent / Agent Pay are still "announced, not live/adopted at scale" — "over 30 industry leaders" is an intent-to-participate count, not volume; second-order → the real test is whether a card-network trust layer out-adopts the open, issuer-neutral stack (x401 + MCP + PAP) the note argues could become "part of the foundation of the internet." Mastercard is positioning to be the trust/record layer on top of those open protocols rather than compete with them — consistent with the note's "Verifiable Intent links authorisation to the purchase" framing.

Sources: https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000081/ma06302026-exx991xearnings.htm (Q2 2026 8-K earnings release) · Q2 2026 earnings-call highlights · note's own Mastercard source https://www.mastercard.com/gb/en/news-and-trends/stories/2026/verifiable-intent.html · public consensus: not pulled (not an earnings event).
<!-- /enrichment:earnings_review -->
