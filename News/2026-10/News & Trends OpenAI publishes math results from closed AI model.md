---
title: "News & Trends: OpenAI publishes math results from closed AI model"
date: 2026-10-08
retrieved: 2026-10-08
tags:
  - company/openai
  - industry/ai
  - region/us
  - type/research-report
sources:
  - https://www.theverge.com/ai-artificial-intelligence/1005004/openai-math-release-github
  - https://github.com/openai/math
  - https://www.theguardian.com/technology/2026/oct/07/openai-mathematical-findings-concerns
  - https://www.ahmath.org/statements
  - https://scottaaronson.blog
  - https://www.wsj.com/tech/ai/openai-ai-math-problems-millennium-prize-23d14511
  - https://www.scientificamerican.com/article/openai-unleashes-hundreds-more-math-results-upon-a-field-already-in-shock
  - https://openai.com/ru-RU/index/sharing-ai-progress-in-mathematics
status: tagged
n_mentions: 6
channels:
  - "News & Trends by Sber"
story_id: s7ce6b37d
month: 2026-10
enriched: false
---

# News & Trends: OpenAI publishes math results from closed AI model

> [!info] 2026-10-08 · 6 упоминаний · 4 источника(ов) с текстом
> Каналы: News & Trends by Sber

## Агрегированный текст (из дайджестов)

[News & Trends by Sber] OpenAI опубликовал сотни математических результатов, полученных с помощью закрытой AI-модели. Среди них — доказательства известных гипотез, новые алгоритмы и продвижение к «задачам тысячелетия». Одни ученые говорят об историческом прорыве, другие опасаются, что корпорации превращают фундаментальную науку в гонку закрытых моделей

[News & Trends by Sber] Кроме того, компания заявила о доказательстве гипотезы уникальных игр (Unique Games Conjecture) из теоретической информатики. Она позволяет установить, насколько близко алгоритмы способны подойти к оптимальному решению чрезвычайно сложных задач. Подтверждение доказательства уточнило бы фундаментальные пределы эффективности вычислений. Другие работы затрагивают квантовые вычисления и математическую физику. По оценке исследователя Скотта Ааронсона, отдельные результаты могли бы стать открытиями года в своих областях

[News & Trends by Sber] В сентябре доказательство для задачи Навье-Стокса потребовало работы около 10 тыс. AI-агентов и миллионов долларов на вычисления. Новую серию работ OpenAI получил главным образом с помощью одной внутренней AI-модели. В компании утверждают, что почти все результаты были получены одним агентом по одному запросу на задачу, хотя иногда требовалось несколько попыток. По оценке OpenAI, средний результат требовал вычислений, эквивалентных трем часам размышлений ChatGPT Pro. Модель протестировали примерно на 4 тыс. задач, отобрав для публикации наиболее значимые результаты

[N

## Первоисточники

### theverge.com
<https://www.theverge.com/ai-artificial-intelligence/1005004/openai-math-release-github>
*558 слов · direct*

AI 
 OpenAI 
OpenAI drops another batch of mathematical breakthroughs
Solutions to ‘hundreds’ of open questions are said to be included in a batch of manuscripts released by OpenAI.
Solutions to ‘hundreds’ of open questions are said to be included in a batch of manuscripts released by OpenAI.
 Link 
 Share 
 Gift 
OpenAI has revealed solutions to a number of long-standing mathematics problems produced by an unreleased frontier model in a batch of 722 manuscripts, covering 372 result families that group related papers. It extends a run of breakthroughs that have both impressed and unsettled parts of the mathematical community while raising questions about research ethics and academic conduct. According to AGMAI, the newly formed independent advisory group of elite mathematicians put together to work on communicating the results responsibly, the release includes solutions to “hundreds” of open questions.
The results have been expected for weeks, although until now OpenAI had not provided details about which problems the model had solved or exactly when they would be published. In September, the company said its model had “resolved more than 100 long-standing open problems across most areas of mathematics.” The released papers and other details also include some summaries of the model’s reasoning, estimates of the compute used, and stats about the number of problems attempted. OpenAI claims the “average result” used the equivalent of three hours of ChatGPT Pro thinking.
AGMAI, or the Advisory Group on Mathematics and Artificial Intelligence, published its first recommendations in late September, urging AI labs to release mathematical results promptly and through established academic channels where possible, while disclosing details such as the name of the model used, prompts, and compute costs. The group also implored AI companies to “refrain from treating the release of mathematical results as marketing vehicles to promote their models,” a practice they said inflicts significant harm on the mathematical community.
Here’s how OpenAI described its process for this release:
 For this release, we’re publishing the results in a GitHub repository, with protocols for paper revisions and citations. We’re continuing to explore other community-hosted alternatives for this release which meet the committee’s guidelines. For future releases, we are committed to further improving the quality of the papers via the citations, mathematical exposition, and presentation of the results for better understanding 
The full impact of the results will likely take some time to be felt as mathematicians assess and digest them. They add to a rapidly growing body of mathematical results from OpenAI and rival labs like Anthropic that the field is still processing, including results concerning a Millennium Prize problem, among the most famous open questions in the field. The speed at which AI labs have barreled into the discipline this year — particularly their handling of announcements — has provoked fierce debate over research practices , ethics, and how companies credit the human mathematicians whose work their systems build upon and potentially use to produce results.
 Robert Hart 
 AI 
 OpenAI 
More in: All the drama around AI’s takeover of mathematics 
Most Popular
 Google invests millions in Mark Zuckerberg’s efforts to create a ‘virtual cell’ 
 New leaks provide our first look at Apple and LG’s smart home devices 
 How Microsoft built its MacBook Pro competitor 
 Xbox has secured GTA 6 streaming rights 
 Surface RTX Spark Dev Box is available for preorder for $5,999 
This is the title for the native ad

### github.com
<https://github.com/openai/math>
*392 слов · direct*

Readme
This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model.
As part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated. Some outputs build upon earlier results produced by the models.
This collection includes results at different stages of verification. Not all have accompanying Lean formalizations. We will continue to update this repository with Lean formalizations as we obtain them.
Some of the unformalized results could have issues. We will endeavor to fix any such issues quickly.
We are also exploring community-hosted repositories for these materials.
Navigating the collection
The current catalogue contains 719 manuscripts organized into 372 families. A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs. Each family is classified by mathematical discipline.
Start with the overview for descriptions of the families.
Use the manuscript map to find individual papers and their supporting materials.
The preprints/ directory contains PDFs, source files, and manuscript-specific citation and build instructions.
The Lean library and formalization catalogue describe the available formal proofs, their associated papers, and verification configurations. See the Comparator instructions for additional checking instructions. The repository has ~42% top-line results formalized.
Updates to the repo are described in the history .
Reasoning summaries
We are also releasing abridged summaries of the model's reasoning, covering the following results:
How the results were produced
The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model. On average, each result used three hours of ChatGPT Pro thinking compute with that model. Over the course of the evaluation, the model was posed approximately 4,000 problems. Aggregating the output into result families and manuscripts and requiring an appropriate level of significance led to the catalog outlined above.
Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties. Additionally, the writeup for the Re(s) > 11/12 zero-free region for the Riemann zeta function was human edited for readability.
Versions and citations
We will preserve the public release history of this collection. Corrections and revisions will be recorded as new versions, with previously released versions remaining accessible.
To cite the individual manuscript, use the BibTeX block in its directory.

### theguardian.com
<https://www.theguardian.com/technology/2026/oct/07/openai-mathematical-findings-concerns>
*436 слов · direct*

OpenAI’s release of mathematical findings draws concerns from experts
Leaders worry OpenAI is not doing due diligence to vet results and that AI models aren’t accessible to broader field of mathematicians 
OpenAI has astounded mathematicians after releasing hundreds of new mathematical findings on Tuesday.
The company published over 370 mathematical results across a variety of topics such as algebra, theoretical computer science and mathematical logic, showcasing what some of its most advanced artificial intelligence models are capable of.
Last month, the company solved the Navier-Stokes equation , one of the world’s toughest mathematical problems with a $1m reward for anyone who cracked it.
The achievement prompted concerns from leaders in the field who say that frontier labs should not be testing the most advanced mathematical problems on proprietary AI models that are not accessible to the broader field of mathematicians. The Institute for Advanced Study in Princeton, New Jersey, an independent group of mathematical experts, said that it does not endorse the practice.
“It is now the case that AI can output mathematical arguments in situations without the human who prompted it being able to understand the arguments, verify them, or take responsibility for them,” a statement from the organization read. “We believe that human understanding of mathematics remains of paramount importance. How, in this new era, can we work towards a new paradigm that includes human understanding of mathematics as part of responsible scholarly output?”
To address concerns from the mathematics community, OpenAI announced it would work with the Institute for Advanced Study in order to give “mathematicians a voice in how we move forward” .
The company did not indicate, however, that it would stop testing its AI models with these advanced problems. Experts in the field say they worry OpenAI is not doing the due diligence required to vet these results.
In an interview with the New York Times , Tristan Buckmaster, a New York University mathematician who was working on the Navier-Strokes problem, said mathematicians who were prompting AI models to solve equations could be providing information that helped the model get to the result.
“There’s likely to be a bunch of results where they take someone’s work and then take it to completion,” Buckmaster said.
The advisory board has also asked that AI labs grant “equitable access” to their AI models to the global mathematics community.
“The use of proprietary internal models by AI labs to do mathematical research risks creating a two-tier system where labs outrun the rest of the field, effectively alienating the mathematical community from its own discipline,” the group wrote.
 OpenAI 
 AI (artificial intelligence) 
 Mathematics 
 Computing 
 news

### ahmath.org
<https://www.ahmath.org/statements>
*222 слов · direct*

Statements
AHM Statement on OpenAI’s October 6 Release of Mathematical Documents
Yesterday, on October 6th, 2026, OpenAI – which is currently defending lawsuits against accusations of illegal plagiarism, copyright infringement, and trademark dilution – released a repository of manuscripts purporting to contain solutions to a number of high-profile problems in mathematics.
Mathematicians did not ask for this work to be done. The Advisory Group on Mathematics and Artificial Intelligence, from whom OpenAI has claimed to derive its legitimacy, opened their initial advisory statement by saying that frontier AI corporations should not test advanced mathematical problems on internal models. In ignoring the central premise of the Advisory Group’s position, OpenAI has indicated total disregard for the norms of scientific research — norms that guarantee that mathematics remains trustworthy, ethically researched, and in the public interest.
Mathematicians have a particular vision of progress that is informed by history and field-specific considerations. We reject OpenAI's assertion that this release advances our subject, and we urge mathematicians and the public to view the value of this publication model with due skepticism. 
Releasing over 700 files at once is not a demonstration of scholarship, but a demonstration of power. We urge mathematicians to discontinue their work with OpenAI and to return to a vision of science that centers human understanding. 
 Association for Human Mathematics Communications Working Group

### Прочие ссылки (без извлечённого текста)

- <https://scottaaronson.blog>
- <https://www.wsj.com/tech/ai/openai-ai-math-problems-millennium-prize-23d14511>
- <https://www.scientificamerican.com/article/openai-unleashes-hundreds-more-math-results-upon-a-field-already-in-shock>
- <https://openai.com/ru-RU/index/sharing-ai-progress-in-mathematics>

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
