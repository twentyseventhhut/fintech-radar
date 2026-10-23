---
title: "Treasury Committee questions regulators over cloud outage oversight"
date: 2026-10-22
retrieved: 2026-10-22
tags:
  - industry/infrastructure
  - industry/regtech
  - region/uk
  - type/regulation
sources:
  - https://committees.parliament.uk/committee/158/treasury-committee/news/218364/google-cloud-outage-bank-of-england-and-fca-letter-published
status: enriched
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: scdd4c405
month: 2026-10
enriched: true
importance: 3
freshness: fresh
---

# Treasury Committee questions regulators over cloud outage oversight

> [!info] 2026-10-22 · 1 упоминаний · 0 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Treasury Committee questions regulators about the outage and their oversight powers.

## Первоисточники

_(нет загруженного полного текста первоисточника)_

### Прочие ссылки (без извлечённого текста)

- <https://committees.parliament.uk/committee/158/treasury-committee/news/218364/google-cloud-outage-bank-of-england-and-fca-letter-published>

## Контекст

<!-- enrichment:context -->
**[0] What happened (dated).** On **Tue 20 Oct 2026**, a power-related fault in **Google Cloud's London infrastructure** (europe-west2-b zone, ~06:08 UTC) knocked out banking apps, card payments, transfers and some public services across the UK and Europe for hours. Named casualties included **Revolut, Lloyds/Halifax, HSBC** and open-banking rail Tink. Within hours, **Treasury Committee chair Dame Meg Hillier MP** wrote to **Andrew Bailey** (Governor, Bank of England) and **Nikhil Rathi** (CEO, FCA). The letter was published by Parliament around **21 Oct 2026** ([UK Parliament / Treasury Committee](https://committees.parliament.uk/committee/158/treasury-committee/news/218364/google-cloud-outage-bank-of-england-and-fca-letter-published/)). It poses **nine questions** seeking to establish how the Bank and FCA will use their powers in response — including when regulators were first alerted and by whom, the cause of the outage, how many finance firms were impacted, how many of their customers were affected, and the scale of any financial harm. Hillier demanded an **initial response by 4 Nov 2026** and **full detail by 20 Jan 2027** ([Computer Weekly](https://www.computerweekly.com/news/366652388/MPs-ask-finance-regulators-how-they-will-deal-with-Google-Cloud-after-outage)).

**[1] Why it matters / the oversight hook.** This is the first real stress test of the UK's new **Critical Third Parties (CTP)** regime, which went live **13 Jul 2026** when HM Treasury designated **AWS, Google Cloud, Microsoft and Oracle** as the first CTPs, bringing them under joint **BoE/PRA/FCA** oversight ([[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]]; [FCA statement](https://www.fca.org.uk/news/statements/uk-financial-regulators-overseeing-critical-third-parties-announced-treasury)). The CTP regime gives regulators powers of information-gathering, oversight and (ultimately) enforcement over non-financial firms whose failure could hit many regulated firms at once — the textbook "concentration risk" the London outage just demonstrated live. The Committee's letter is Parliament pressing the regulators to show the regime has teeth ~3 months after it came into force.

**[2] The self-referential angle (the genuinely notable bit).** The Treasury Committee is effectively **following up on its own recommendation**. On **20 Jan 2026** the Committee's report *"Artificial intelligence in financial services"* recommended that **by end-2026 HM Treasury must designate the major AI and cloud providers as CTPs**, and criticised the Treasury for being slow to use the new powers ([UK Parliament report](https://publications.parliament.uk/pa/cm5901/cmselect/cmtreasy/684/report.html); [regulationtomorrow.com](https://www.regulationtomorrow.com/2026/01/house-of-commons-treasury-committee-report-on-ai-in-financial-services/)). The Jul 2026 designations answered that; the Oct outage now lets the Committee test whether designation translates into operational response. So this is less a cold-start inquiry and more a chair who warned about exactly this risk now demanding accountability.

**[3] Related notes in vault.**
- [[EU regulators question Google over London cloud outage]] — the **EU/EBA twin** of this item: same outage, different regulator (EBA, DORA/CTPP), different jurisdiction, different source (Reuters). **Not a duplicate** — this note is the UK Parliament/BoE/FCA action.
- [[Revolut outage linked to Google Cloud infrastructure problems]] — the operational incident itself (trigger event).
- [[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]] — the Jul 2026 CTP designation that created the oversight powers Hillier is invoking.
- [[Bank of England runs sector-wide cloud outage drill with 38 firms]] — SIMEX26 (8 Oct 2026), the sector cloud-outage drill run **12 days before** the real thing.
- [[How Monzo uses multi-cloud infrastructure to improve resilience]] — the "good-practice" cross-cloud failover counter-example.
- [[AWS outage disrupts UK banks' online services]] (2025-10) — near-identical precedent one year earlier (AWS, UK banks).
- [[Worldpay outage leaves UK pubs and shops cash-only during England match]] (2026-06) — prior UK payments-concentration outage.

**[4] Net read.** A **genuinely significant governance/regtech signal**: the first parliamentary test of the UK CTP regime, with named deadlines (4 Nov, 20 Jan 2027) and a chair who pre-called the risk. But as a *news item in isolation* it is an early-stage **fact-finding letter**, not a finding, sanction or new power — the hard consequences (regulators' answers, any skilled-person review or scenario-testing order) are still to come. Much of the heavy substance (the outage, the EU twin, the CTP designation) lives in sibling notes. Structurally important; procedurally still early.
<!-- /enrichment:context -->

## Челлендж / ред-тим

<!-- enrichment:challenge -->
**Red-team questions**

1. Is this a formal *investigation* with teeth, or a letter asking nine questions? It is the latter — a scrutiny letter from a select committee demanding answers from the Bank and FCA, not an enforcement action by anyone against Google.
2. Who is the subject — Google, or the regulators? The letter targets the **regulators'** response/powers (BoE, FCA), not Google directly. That distinguishes it from the EU/EBA item, which questions Google.
3. Is this a duplicate of [[EU regulators question Google over London cloud outage]]? No — same outage, but different actor (UK Parliament vs EBA), jurisdiction (UK vs EU), target (regulators vs Google) and source (Parliament/Computer Weekly vs Reuters). Fresh, sibling not dupe.
4. Does a committee letter actually change anything, or is it theatre? Select committees have no direct power over CTPs; their leverage is public accountability + the hard deadlines (4 Nov, 20 Jan 2027). Consequence depends on the regulators' answers, not the letter.
5. Are the "nine questions" and deadlines independently confirmed? Yes — Computer Weekly and multiple wires cite nine questions, initial reply 4 Nov 2026, full detail 20 Jan 2027, consistent with the Parliament news page.
6. Is the CTP regime even applicable yet in an enforceable way? Designation was 13 Jul 2026; this is the first live test ~3 months in. Whether powers translate into incident-reporting demands, scenario testing or skilled-person reviews is **unproven**.
7. Is there a conflict/self-interest angle? The Committee recommended designating cloud/AI providers as CTPs in its Jan 2026 report; this letter lets it claim vindication. Framing risk: is the Committee grandstanding on its own prior recommendation?
8. How much financial harm actually occurred? Unquantified — one of the nine questions explicitly asks how many firms/customers were hit and the scale of harm. No hard loss figure exists yet.
9. Was Google at fault in a CTP-relevant way, or a routine single-zone power failure with normal RTO? Root-cause/liability split between Google and its single-region bank customers is unresolved.
10. Could the banks' own single-region/single-cloud design be the real failure, not Google? Plausible — a localised europe-west2-b fault cascaded because affected firms lacked failover (cf. Monzo's cross-cloud DR as counter-example).
11. Timeline/novelty risk: outage 20 Oct, letter ~21 Oct, note dated 22 Oct — is this just echoing a one-day-old wire with no development? Partly; the development to watch is the 4 Nov reply.
12. Does anything bind Google here? No penalty or enforcement mechanism is cited; CTP oversight is resilience-focused, "not the same as authorisation."
13. Is "Treasury Committee" being conflated with "the Treasury"? They are distinct — the Committee is a Commons scrutiny body; HM Treasury (executive) made the designations. The letter is Committee→regulators.
14. Does this meaningfully affect Google's UK cloud-finance business commercially? Likely negligible near-term; reputational/oversight pressure only.
15. Counterfactual: did SIMEX26 (the 8 Oct BoE drill, 12 days earlier) surface these exact gaps, and will the regulators' answers show the drill's lessons were applied — or ignored?

**Importance: 3/5** — The highest-signal of the three same-day sibling items on the governance axis: it is the first parliamentary test of the UK Critical Third Parties regime, with named officials, nine specific questions and hard deadlines (4 Nov 2026, 20 Jan 2027), driven by a chair who pre-recommended exactly this designation in Jan 2026. That gives it real structural and narrative weight. But as a standalone it is an early-stage scrutiny *letter* — no finding, sanction or new power yet — and much of the substance (the outage, the EU twin, the CTP designation, the Monzo counter-example) lives in sibling notes. Significant for the resilience/regtech theme; light on immediate hard consequence.
<!-- /enrichment:challenge -->

## Связь с постом

<!-- enrichment:post -->
_(пусто)_
<!-- /enrichment:post -->

## Market Research

<!-- enrichment:market_research -->
**Sector & drivers.** This is a regulatory/operational-resilience story, not a company deal — no valuation/round attaches. Subvertical: critical-third-party (CTP) / cloud-concentration oversight for UK financial services. Market structure of the underlying cloud layer is highly consolidated: the big three hyperscalers hold ~63–67% of global cloud infrastructure spend — AWS ~28%, Microsoft Azure ~20%, Google Cloud ~15% (per Synergy/industry trackers, via sobalabs/holori, as of Q2 2026). That oligopoly IS the policy problem: a single provider's regional failure cascades across many regulated firms at once. Why now: a 20 Oct 2026 Google Cloud London-region outage disrupted multiple banks and fintechs — Revolut (80m+ customers) saw payments/card declines, and open-banking rail Tink reported a full connectivity failure to Revolut UK (via Reuters). This landed three months after the Treasury designated Google Cloud EMEA, AWS EMEA, Microsoft Ireland and Oracle UK as Critical Third Parties (Jul 2026), activating the UK CTP regime — so the outage is the first live stress test of brand-new BoE/FCA oversight powers over non-financial providers. Treasury Committee chair Meg Hillier MP wrote to the BoE Governor and FCA CEO with nine questions, initial response due 4 Nov 2026, full detail by 20 Jan 2027 (per UK Parliament committee site; Computer Weekly). Entry barriers for would-be regulators: they can supervise CTPs but cannot cap concentration or force firms off a given cloud — the regime is oversight, not antitrust.

**Competitive landscape.** This isn't a company-vs-company market; the relevant "players" are the regime's three poles. (1) Regulators (BoE/PRA + FCA) wielding CTP investigation/enforcement powers — the question Hillier poses is whether they will actually use them. (2) The four designated CTPs (Google, AWS, Microsoft, Oracle) — the supervised parties. (3) Regulated firms carrying the concentration exposure. The FSB's standing prescription is a "multi-vendor"/multi-cloud approach so critical services replicate across providers and avoid lock-in (FSB, cloud third-party dependencies work). Recent moves with dates: BoE ran a sector-wide cloud-outage drill with 38 firms (15 Oct 2026) — five days before the real outage, a sharp de-PR'd signal the regulator already saw this coming; EU financial regulators separately queried Google over the same outage (21 Oct 2026, Reuters). Protagonist positioning — the UK CTP regime is ahead of most peers in codifying hyperscaler oversight (live since Jul 2026) but behind in enforcement track record (zero precedents; this is incident #1). Moat for the hyperscalers is deep switching costs + scale (why firms concentrate in the first place); the regulator's "moat" is statutory authority but with no proven teeth yet `(analysis)`.

**Comps & multiples.** No valuation event — trading multiples are N/A ("no data"). Comps here are precedent events in-base, which cluster tightly around this exact theme:
- [[UK designates Google, AWS, Microsoft, Oracle as Critical Third Parties]] (2026-10) — the designation this letter invokes.
- [[UK to oversee critical third-party cloud service providers]] (2026-07) — the regime's rollout.
- [[Bank of England runs sector-wide cloud outage drill with 38 firms]] (2026-10-15) — the pre-outage stress test.
- [[Revolut outage linked to Google Cloud infrastructure problems]] (2026-10-20) — the triggering incident.
- [[EU regulators question Google over London cloud outage]] (2026-10-21) — parallel EU probe.
- [[How Monzo uses multi-cloud infrastructure to improve resilience]] (2026-10) — a firm-side mitigation (the FSB-recommended multi-vendor answer).
Adjacent prior precedent: [[ECB payment system T2 suffers second outage in a week]] (2026-07) — concentration/resilience failure in core infra, regulator-side. No multiple to flag rich/cheap; qualitative only.

**Risk flags.**
1. **Concentration / single-point-of-failure (systemic).** One hyperscaler region failing took down multiple regulated firms simultaneously (Revolut, Tink) — the oligopolistic cloud market means idiosyncratic provider risk becomes system-wide; the CTP regime acknowledges but does not reduce the dependency.
2. **Regulatory enforcement untested / expectations risk.** Powers exist but have never been used on a CTP; if BoE/FCA respond softly (information requests, no sanction), the second-order effect is that designation becomes a paper exercise and firms under-invest in resilience — exactly the gap Hillier is probing with a hard 4 Nov / 20 Jan deadline.
3. **Jurisdictional limits of oversight.** Designated entities are EMEA/UK subsidiaries of US parents (Google Cloud EMEA, AWS EMEA, Microsoft Ireland); a UK regulator's reach over a global outage rooted in another region/parent is structurally weak — remediation levers may sit outside UK jurisdiction.

**What this changes (idea-lens).** This is the first real-world test of the UK CTP regime; the 4 Nov 2026 response and 20 Jan 2027 full report are the catalysts to watch. Falsifiable thesis `(analysis)`: expect the outcome to tilt toward mandated multi-cloud/exit-planning obligations and resilience-testing requirements on regulated firms (demand-side), rather than any direct enforcement action against a hyperscaler (supply-side) — because regulators can't force provider behaviour without antitrust tools. Thesis is wrong if BoE/FCA open a formal CTP enforcement action against Google, which would re-rate the regime from "monitoring" to "teeth" and raise compliance cost expectations across all four CTPs.

Sources: https://committees.parliament.uk/committee/158/treasury-committee/news/218364/google-cloud-outage-bank-of-england-and-fca-letter-published/ · https://www.computerweekly.com/news/366652388/MPs-ask-finance-regulators-how-they-will-deal-with-Google-Cloud-after-outage · https://finance.yahoo.com/technology/articles/europes-financial-regulators-query-google-154104572.html · https://sobalabs.ai/blog/who-are-the-big-five-hyperscalers/ · https://www.fsb.org/2019/12/third-party-dependencies-in-cloud-services-considerations-on-financial-stability-implications/
<!-- /enrichment:market_research -->

## Earnings Review

<!-- enrichment:earnings_review -->
_(пусто)_
<!-- /enrichment:earnings_review -->
