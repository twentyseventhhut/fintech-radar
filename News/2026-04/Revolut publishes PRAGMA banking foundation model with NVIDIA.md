---
title: "Revolut publishes PRAGMA banking foundation model with NVIDIA"
date: 2026-04-14
tags:
  - company/revolut
  - company/nvidia
  - industry/ai
  - industry/banking
  - region/uk
  - type/research-report
sources:
  - https://letsdatascience.com/news/revolut-deploys-pragma-foundation-model-for-finance-50d47f78
  - https://arxiv.org/html/2604.08649v1
  - https://www.businesspost.ie/companies/revolut-users-set-to-miss-out-on-harriss-new-investment-accounts
status: tagged
n_mentions: 5
channels:
  - "Connecting the Dots in Fintech"
  - "Fintech Brainfood"
story_id: sda2e3ad8
month: 2026-04
enriched: false
---

# Revolut publishes PRAGMA banking foundation model with NVIDIA

> [!info] 2026-04-14 · 5 упоминаний · 2 источника(ов) с текстом
> Каналы: Connecting the Dots in Fintech, Fintech Brainfood

## Агрегированный текст (из дайджестов)

[Connecting the Dots in Fintech] 🇬🇧 Revolut deploys PRAGMA foundation model for finance. The model is pre-trained with a masked modelling, self-supervised objective designed for the discrete, variable-length nature of transaction and event logs, and is reported to be trained on a large corpus of roughly 40 billion behavioral events. Revolut users set to miss out on Harris’s new investment accounts. Revolut said it would need to set up an Irish branch to offer the accounts if platforms were required to administer the tax.

[Fintech Brainfood] Revolut published PRAGMA — a foundation model trained on 24 billion banking events across 111 countries. Credit scoring up 130%. Fraud recall up 65%.

[Fintech Brainfood] The most important signal in Revolut’s PRAGMA work with NVIDIA is the significant improvement (uplift) their model delivered vs their existing custom ML models, across multiple use cases.

[Fintech Brainfood] The paper is the first time I've seen published evidence on the effectiveness of a foundation model for banking’s most important competitive levers. Revolut published the uplift this model produced vs their existing ML models:

[Fintech Brainfood] 2. Revolut built a foundation model for customer event data.

## Первоисточники

### letsdatascience.com
<https://letsdatascience.com/news/revolut-deploys-pragma-foundation-model-for-finance-50d47f78>
*677 слов · direct*

Revolut introduces PRAGMA , a family of Transformer-based foundation models trained on a large, heterogeneous corpus of banking event sequences. PRAGMA uses a masked modelling, self-supervised objective adapted to discrete, variable-length financial records and produces embeddings that power credit scoring, fraud detection, lifetime value prediction, and other downstream tasks. The architecture is optimized so a simple linear probe on top of extracted embeddings already delivers strong performance, with further gains from lightweight fine-tuning. Revolut reports training on a corpus of roughly 40 billion behavioral events and running inference and orchestration at scale using an on-prem/cloud stack with hundreds of H100 GPUs, making PRAGMA both a technical and strategic asset for fintech use cases.
 What happened
Revolut published PRAGMA , a family of Transformer-based foundation models tailored to multi-source banking event sequences, and an arXiv preprint describes the approach, training objective, and downstream evaluation. The model is pre-trained with a masked modelling, self-supervised objective designed for the discrete, variable-length nature of transaction and event logs, and is reported to be trained on a large corpus of roughly 40 billion behavioral events. The paper shows PRAGMA yields strong embeddings that enable good downstream results via linear probes and improve further with lightweight fine-tuning.
 Technical details
The pre-training uses a Transformer backbone adapted to sequence heterogeneity and sparse, event-driven timestamps. The self-supervised objective is a masked modelling variant tuned for variable-length, categorical-rich records rather than continuous text tokens. Key practitioner takeaways:
 • Models are trained on multi-source banking event sequences to capture cross-product signals (payments, authorization events, support interactions). 
 • Embeddings produced by PRAGMA support downstream tasks including credit scoring, fraud detection, and lifetime value prediction with minimal additional training. 
 • Simple linear models on top of frozen embeddings already achieve strong baselines; lightweight fine-tuning yields consistent uplift. 
 Evaluation and infra
The preprint reports broad evaluation across multiple financial domains and shows superior performance compared to task-specific baselines. Revolut also describes a production inference stack capable of high-throughput, low-latency use: industry reporting indicates inference and orchestration run on an AI cloud with more than 200 NVIDIA H100 GPUs , plus tooling for monitoring and FinCrime agents that leverage shared embeddings.
 Context and significance
Vertical, domain-specialized foundation models are an accelerating trend. PRAGMA is a clear example of a financial vertical model where proprietary behavioral signals produce a material performance moat. By focusing on raw event sequences and representation learning, Revolut moves evaluation emphasis from retrieval augmentation and large general LLMs toward robust, reusable embeddings that scale across supervised tasks. This aligns with industry shifts where orchestration, observability, and domain data quality matter more in production than marginal improvements in open-domain generative quality. The result is a strategic asset: shared embeddings reduce duplicated effort across risk, product, and support teams and convert raw event scale into an operational advantage.
 Risks and governance
Specialized models trained on transactional data raise model-risk, privacy, and regulatory scrutiny. Data lineage, explainability, drift detection, and auditability will be essential before PRAGMA -powered decisions drive credit or denials at scale. Practitioners will need to integrate model risk frameworks, differential privacy or synthetic data strategies, and rigorous evaluation across demographic slices.
 What to watch
Whether Revolut releases code, model checkpoints, or evaluation suites; how competitors respond with their own event-sequence models; and how regulators treat productionized, proprietary financial foundation models. Also monitor reproducibility and benchmark comparisons on public or synthetic banking datasets.
"careful data fetching and context engineering often matter more in production than heavy RAG patterns," said Pavel Nesterov, Executive Director of AI at Revolut, summarizing the trade-offs teams face when moving from experimentation to production.
Scoring Rationale
PRAGMA is a meaningful industry contribution: a specialized foundation model for finance that turns high-cardinality event data into reusable embeddings. Its practical significance for fintech engineering and product teams is notable, but the paper is narrowly domain-focused and lacks frontier-model disruption, and the arXiv submission is several days old, triggering a small freshness penalty.
Practice interview problems based on real data
1,500+ SQL & Python problems across 15 industry datasets — the exact type of data you work with.

### arxiv.org
<https://arxiv.org/html/2604.08649v1>
*2030 слов · direct*

PRAGMA: Revolut Foundation Model
 Modern financial systems generate vast quantities of transactional and event-level data that encode rich economic signals.
This paper presents PRAGMA, a family of foundation models for multi-source banking event sequences.
Our approach pre-trains a Transformer-based architecture with masked modelling on a large-scale, heterogeneous banking event corpus using a self-supervised objective tailored to the discrete, variable-length nature of financial records.
The resulting model supports a wide range of downstream tasks such as credit scoring, fraud detection, and lifetime value prediction: strong performance can be achieved by training a simple linear model on top of the extracted embeddings and can be further improved with lightweight fine-tuning.
Through extensive evaluation on downstream tasks, we demonstrate that PRAGMA achieves superior performance across multiple domains directly from raw event sequences, providing a general-purpose representation layer for financial applications.
 
 Disclaimer : We report only relative improvements, as absolute metrics are commercially sensitive.
 All examples are synthetic and not from real production data. 

 1 Introduction
 Foundation models are general-purpose models trained at scale on broad data distributions and subsequently adapted to a wide variety of downstream tasks  ( Bommasani et al. , 2021 ) .
While such models have transformed natural language processing  ( Devlin et al. , 2019 ; Brown et al. , 2020 ) and computer vision  ( Kirillov et al. , 2023 ; Caron et al. , 2021 ) , their application to multi-source banking user histories remains comparatively underexplored.
Modern banks and fintechs accumulate large volumes of data: event streams spanning card and transfer transactions, product usage, in-app navigation, and customer communications, alongside static generalised profile state such as account tenure and plan.
These event streams encode signals relevant to risk management, product analytics, and operations, but they are difficult to model efficiently with off-the-shelf language-model tokenisation and architectures.
While serialising structured records as text and feeding them to a standard Transformer is a viable baseline, it inflates sequence lengths considerably because every field name and delimiter becomes several subword tokens.
Moreover, numerical values are split into digit fragments that discard magnitude and ordering, both of which are critical for financial reasoning.
Together, these limitations make naive text serialisation impractical for the long, heterogeneous user histories common in banking. 
 Multi-source banking user histories differ from text in three ways.
First, each event is a variable-length record with mixed categorical, numerical, and free-text fields.
Second, histories are long-tailed in length and irregular in time, with strong daily and weekly cycles.
Third, practical deployments must operate under strict privacy and regulatory constraints, which limit what can be reported and which features can be used for certain decisions.
Because no single off-the-shelf architecture handles all three challenges simultaneously, practitioners default to building task-specific pipelines with extensive feature engineering, making it hard to share statistical strength across domains and products. 
 Prior work addresses isolated slices of this problem.
Tabular Transformers such as TabTransformer and FT-Transformer  ( Huang et al. , 2020 ; Gorishniy et al. , 2021 ) model fixed-schema rows, while sequential recommender models such as SASRec and BERT4Rec  ( Kang and McAuley , 2018 ; Sun et al. , 2019 ) operate on item-like interaction histories.
Financial foundation models have largely focused on text or generic time-series tokenisation  ( Yang et al. , 2020 ; Wu et al. , 2023 ; Yang et al. , 2023 ; Jin et al. , 2024 ; Ansari et al. , 2024 ) , while newer transaction-ledger models such as nuFormer and TransactionGPT  ( Braithwaite et al. , 2025 ; Dou et al. , 2025 ) move closer to our setting.
However, these models typically ingest a single event source, omit static profile state, and are evaluated on a narrow set of tasks: nuFormer targets product recommendation, while TransactionGPT focuses on anomaly detection and trajectory generation.
The literature still lacks a multi-source encoder backbone with explicit profile state that transfers across a broad range of discriminative banking tasks. 
 In this paper, we present PRAGMA, a family of encoder-style foundation models for multi-source banking user histories.
PRAGMA is pre-trained with masked modelling on a large-scale corpus of user histories that combines multi-source events with static profile state (§ 2.1 ).
To handle heterogeneity, we apply a key–value–time tokenisation scheme with type-specific value encoding for numerical, categorical, and textual fields (§ 2.2 ).
The resulting backbone uses two encoder branches for profile state and events whose outputs are fused by a history encoder (§ 2.3 ). 
 We choose an encoder-only, bidirectional design because our primary goal is transferable representations for discriminative financial tasks, rather than open-ended generation.
Masked modelling enables each token to attend to both past and future context  ( Devlin et al. , 2019 ) , which is particularly useful when reconstructing partially observed event records and learning record-level representations from complete histories.
After pre-training, PRAGMA can be adapted efficiently in two complementary ways (§ 3.1 ).
In the embedding probe setting, we freeze the backbone and train a lightweight head on top of the extracted embeddings.
In the LoRA fine-tuning setting, we apply Low-Rank Adaptation (LoRA)  ( Hu et al. , 2022 ) to update only a small fraction of parameters, enabling fast specialisation while keeping most of the backbone shared across tasks. 
 We evaluate PRAGMA on a suite of internal downstream benchmarks spanning credit scoring, fraud detection, communication engagement, recurrent transaction detection, lifetime value prediction, and more (§ 3.2 ).
Across evaluated domains, PRAGMA consistently outperforms strong task-specific baselines while reducing the need for hand-crafted features (Figure  1 ).
We further describe the engineering choices required to train PRAGMA efficiently on long and highly variable user histories, including sequence packing and dynamic batching (§ 2.4 ). 
 Our contributions are as follows: 

 • 
 
 We introduce PRAGMA, a family of encoder-style foundation models for multi-source banking user histories, scaling from 10 M to 1 B parameters, to our knowledge, the largest published encoder backbone for consumer banking event sequences. The architecture combines a key–value–time tokenisation scheme with a two-branch design in which profile-state and event encoders feed a history encoder for heterogeneous financial records. 
 


 • 
 
 We describe an efficient pre-training recipe for long and irregular banking user histories based on masked modelling, sequence packing, and dynamic batching, and show that LoRA fine-tuning of a pre-trained backbone consistently matches or outperforms full training from scratch. 
 


 • 
 
 We evaluate a single pre-trained backbone across six diverse downstream tasks (credit scoring, fraud detection, lifetime value, communication engagement, recurrent transaction detection, and product recommendation), a substantially broader task scope than prior transaction-ledger models, which typically target one or two tasks. PRAGMA consistently outperforms strong task-specific baselines while reducing the need for hand-crafted features. 
 


 2 Pre-training

 2.1 Dataset
 Our goal is to build a foundation model that encodes diverse event-level signals and transfers across a wide range of downstream tasks.
Our dataset is structured at the record level, where each observation represents a pseudonymised event history associated with an evaluation point.
As shown in Figure  2 , we consider an event history alongside contextual attributes.
This approach enables the model to account for both sequential patterns and time-invariant features like account currency. 
 All data used in this work is fully anonymised and contains no personally identifiable information.
We construct our pre-training dataset from 26 M user records spanning 111 countries, accumulating 24 B events that total 207 B tokens. 

 2.1.1 Event History
 Standard platform usage generates event streams across various services, e.g., account funding, payments, in-app navigation, or service communications.
These aggregated event histories capture population-level patterns that support a range of analytical and predictive tasks.
An event is defined by a created timestamp and a set of key–value pairs, e.g., Direction: out .
We fetch events from broad source types that can be loosely grouped into transactions, app, trading, and communication, which were selected for their high expected impact on downstream tasks.
Event schemas are specific to their source type and incorporate distinct sets of keys, e.g., Symbol key is unique to trading events.
Beyond anonymisation, de-identification, and standard eligibility criteria, no additional statistical filtering or pre-processing, such as outlier removal or vocabulary pruning, is applied to the event streams, to ensure that the model captures the full heterogeneity found in production. 

 2.1.2 Profile State
 In addition to the event history, we incorporate general contextual attributes such as balance quantile, plan, insurance state, and service region.
These attributes provide useful context that is otherwise missing from the event history alone.
Profile state is a set of descriptive key–value pairs in an event-like format, e.g., Plan: metal , timestamped at the designated evaluation point (or the cut-off date during pre-training). 
 High-activity users often generate tens of thousands of interactions, exceeding computational bounds; we address this via truncation to a fixed context window (§ 2.3.5 ).
However, truncation risks discarding early historical milestones that carry useful signal, such as account age.
We therefore augment profile state with life-long events , key–value pairs that, unlike regular profile attributes, each carry an individual timestamp recording a first occurrence, e.g., Lifelong: first_topup at 20-11-02 12:09:04 .
This timestamp is then used to compute the temporal distance to the evaluation point, enabling the model to encode the timing of historical milestones. 

 2.1.3 Pre-training Time Range
 Developing a robust and generalisable model requires a delicate balance between maximising historical coverage and maintaining data relevance.
Accordingly, determining the optimal temporal range for pre-training involves navigating several trade-offs between event diversity, distribution shift, and computational efficiency. 
 First, simply including every event from the full available dataset is often impractical and sub-optimal.
Older events may reflect historical patterns, product features, or system dynamics that are no longer relevant at inference time.
Such discrepancies create a distribution mismatch that can degrade performance, as the model may struggle to generalise from obsolete historical examples to the evolving behaviours present in deployment.
Additionally, the inclusion of highly heterogeneous events from long time spans can make the pre-training task harder and slow down model convergence.
Second, downstream applications may require making predictions on events that took place within temporal ranges either much earlier or much later than those used for pre-training.
If the model is not exposed to sufficient diversity in both recent and less-common historical patterns, the performance on these out-of-distribution inputs may suffer.
Finally, Transformer architectures have a limited effective context span, determined both by model design and hardware constraints. 
 With these considerations in mind, we select a temporal range of 25 months from 2023 to 2025 for pre-training, balancing comprehensive event coverage, recency, distribution consistency, and tractable sequence modelling. 

 2.2 Tokenisation
 Unlike standard LLMs that treat everything as text, a financial foundation model needs to preserve the structural nature and heterogeneity of tabular data.
We address this challenge by implementing a disentangled embedding space of input tokens. 
 As shown in Figure  3 , we represent each data point by three components: a semantic type (key), a value, and a temporal coordinate, following a common standard in tabular event data  ( Braithwaite et al. , 2025 ) .
For instance, Channel: email at 24-04-07 19:20:18 maps to a key, a value, and a temporal coordinate, respectively.
This ensures that the model distinguishes between the meaning of a field and its value, while also encoding event chronology.
Next, we present how the three are tokenised. 
 The semantic type embedding enables the model to learn the meaning of a field and to contextualise the value it holds.
We tokenise all semantic types (keys) as single tokens, and both event and profile state semantic types are encoded in a similar way.
This results in a vocabulary of ∼ \sim 60 tokens. 
 We cover the diversity of values with three value types: numerical , categorical , and textual .
Numerical values are mapped to percentile buckets, where bin boundaries are learned from training data with an extra bucket for zero, allocating one token per bucket.
The distinction between categorical and textual is determined by cardinality thresholding: string fields whose number of unique values falls below a predefined threshold are treated as categorical, while higher-cardinality fields are treated as textual.
Categorical values are manually selected from all text fields to prevent splitting common values, such as merchant category codes (MCC), into multiple tokens, and are re

### Прочие ссылки (без извлечённого текста)

- <https://www.businesspost.ie/companies/revolut-users-set-to-miss-out-on-harriss-new-investment-accounts>

## Контекст
<!-- enrichment:context -->
_(пусто — заполняется при обогащении)_

## Челлендж / ред-тим
<!-- enrichment:challenge -->
_(пусто)_

## Связь с постом
<!-- enrichment:post -->
_(пусто)_
