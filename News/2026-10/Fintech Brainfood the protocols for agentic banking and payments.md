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
status: tagged
n_mentions: 7
channels:
  - "Fintech Brainfood"
story_id: sdf5b26fb
month: 2026-10
enriched: false
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
_(пусто — заполняется при обогащении)_
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
_(пусто)_
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
_(пусто)_
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
