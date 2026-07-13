---
title: "OpenAI publishes Agentic Commerce Protocol documentation"
date: 2025-11-25
tags:
  - company/openai
  - industry/agentic-commerce
  - industry/ai
  - region/global
  - type/commentary
sources:
  - https://developers.openai.com/commerce/guides/get-started
status: tagged
n_mentions: 1
channels:
  - "This Week in Fintech"
story_id: s58f07449
month: 2025-11
enriched: false
---

# OpenAI publishes Agentic Commerce Protocol documentation

> [!info] 2025-11-25 · 1 упоминаний · 1 источника(ов) с текстом
> Каналы: This Week in Fintech

## Агрегированный текст (из дайджестов)

[This Week in Fintech] Source: OpenAI Agentic Commerce Protocol Documentation

## Первоисточники

### developers.openai.com
<https://developers.openai.com/commerce/guides/get-started>
*368 слов · direct*

Onboarding product feeds in ChatGPT is currently available to approved
partners. To apply for access, fill out this form 
here
 Overview 
Start your ACP integration by sharing a structured product feed with OpenAI. Product feeds give ChatGPT the catalog data it needs to index your products, understand core attributes, and present accurate product information in shopping experiences.
Start with product feeds when you want to:
Make your catalog understandable to ChatGPT.
Share up-to-date product data, including titles, descriptions, images, price, and availability.
Establish a clear integration path based on a documented schema and delivery model.
You can learn more about the Agentic Commerce Protocol at agenticcommerce.dev and on GitHub .
 Integration path 
Use this sequence to stand up your integration with ACP:
 Decide which integration method to use: file upload or API .
 
 It is generally recommended to provide the entire feed once a day via file upload, and then send updates throughout the day via the API.
If your feed is small, you can provide both the entire feed and regular updates via the API.
Promotions data can only be provided via the API.
 Review the specs for the chosen integration method, and confirm the required fields, canonical field names, and validation rules.
 Validate required fields for every record.
 Upload feed data through the chosen integration method.
 Keep the feed current based on the integration method:
 
 For file upload, overwrite the same file or shard set with your latest snapshot on a regular cadence.
For the API, upsert products through the API.
 Prohibited products policy 
To keep ChatGPT a safe place for everyone, we only allow products and services that are legal, safe, and appropriate for a general audience. Prohibited products include, but are not limited to, those that involve adult content, age-restricted products (for example, alcohol, nicotine, gambling), harmful or dangerous materials, weapons, prescription-only medications, unlicensed financial products, legally restricted goods, illegal activities, or deceptive practices.
Merchants are responsible for ensuring their products and content do not violate these restrictions or any applicable law. OpenAI may take corrective actions such as removing a product or banning a seller from being surfaced in ChatGPT if these policies are violated.
 Best practices 
Review integration best practices for guidance.

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
