---
layout: post
title: "Approximate Reasoning: Computational Rationality in Humans and LLMs"
subtitle: "Why 'Flaws' in Thinking Might Be Optimal Strategies for Incomplete Models"
permalink: approximate-reasoning
categories:
  - "play"
---

This post argues that many so-called human cognitive 'flaws' are not errors but computationally rational adaptations to a world of incomplete information and limited processing power. We will explore ten such strategies, demonstrating their computational benefits and drawing striking parallels to the behaviors of Large Language Models (LLMs). When we reason, we make mistakes. We use stereotypes, fall for logical fallacies, remember events that never happened, and maintain contradictory beliefs. Traditionally, these errors have been viewed as flaws in human cognition—imperfections to be corrected through better education or more careful thinking.

But what if many of these "flaws" actually represent optimal strategies for reasoning with incomplete information and limited cognitive resources? This perspective, often termed "computational rationality," suggests that these cognitive shortcuts are not bugs, but features honed by the need to make timely and effective decisions in a complex world.[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)][[3](https://www.erichorvitz.com/computational_rationality.pdf)][[4](http://www.keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich.Sternberg2003.pdf)]

This post explores how the apparent irrationality of human reasoning might be computationally rational when viewed through the lens of approximate reasoning under constraints. We will also examine how similar patterns of approximate reasoning are emerging in Large Language Models (LLMs), suggesting that these advanced AI systems, when faced with similar computational pressures, might be converging on analogous solutions.

## Defining Our Setting: Reasoning Under Constraints

To properly analyze reasoning strategies, we need to define what constitutes "limited resources" and "incomplete information" in computational terms.

### Limited Resources

Reasoning systems (human or artificial) operate under several resource constraints:

1.  **Memory limitations**: Bounded capacity to store facts, rules, and intermediate results.
2.  **Processing bandwidth**: Limited number of operations per unit time.
3.  **Energy constraints**: Computational operations require energy (particularly relevant for biological systems and large-scale AI models).
4.  **Time pressure**: Decisions often need to be made before exhaustive analysis is possible.

### Incomplete Information

Reasoning systems rarely have complete information about their domain:

1.  **Partial observability**: Many relevant variables cannot be directly observed.
2.  **Noisy observations**: Available data contains errors and ambiguities.
3.  **Sparse sampling**: Only a tiny fraction of possible scenarios have been encountered.
4.  **Concept drift**: The underlying reality changes over time, invalidating past knowledge.
5.  **Hidden variables**: Unknown factors influence observed relationships.

### Formal Framework

Let's formalize our reasoning model:

-   Let $K$ be a knowledge base represented as a graph $G(V, E)$ where nodes $V$ represent concepts and edges $E$ represent relationships.
-   The "ground truth" would be a complete and accurate $G^\ast(V^\ast, E^\ast)$.
-   Due to incomplete information, we only have access to a partial graph $G_p(V_p, E_p)$ where $V_p \subset V^\ast$ and $E_p \subset E^\ast$.
-   Due to resource constraints, we can only actively utilize a subgraph $G_a(V_a, E_a)$ where $\mid V_a \mid \ll \mid V_p \mid$ and operations on $G_a$ are limited.

Under these constraints, optimal reasoning strategies must balance:
-   Accuracy of conclusions
-   Resource utilization
-   Speed of inference

Now let's examine specific strategies that achieve this balance.

## Strategy 1: Chunking Complex Paths (High-level Linkages)

### The Psychological Phenomenon

**Chunking** is a cognitive process where individual pieces of information are bound together into a meaningful whole[^1]. In reasoning, this manifests as compressing multi-step logical chains into direct associations, often appearing as heuristics or rules of thumb.

[^1]: Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97. This seminal paper established that human working memory is limited to approximately seven items, driving the need for chunking strategies.

### Real-World Examples

1.  **Medical diagnosis**: An experienced doctor might directly associate a constellation of symptoms with a disease without consciously working through the underlying physiological mechanisms.
2.  **Chess expertise**: Grandmasters recognize board patterns and make moves without calculating every possible sequence, while novices must analyze each step methodically[^2].
3.  **Social stereotyping**: We develop shortcut associations between social groups and attributes that bypass detailed individual assessment (e.g., "engineers are good at math").

[^2]: Chase, W. G., & Simon, H. A. (1973). Perception in chess. Cognitive Psychology, 4(1), 55–81. This research demonstrated that chess experts chunk board positions into meaningful patterns, allowing rapid recognition rather than piece-by-piece analysis.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function findConnection(conceptA, conceptB):
    Create empty queue Q
    Add conceptA to Q
    While Q is not empty:
        current = Q.dequeue()
        If current == conceptB:
            Return the full path from conceptA to conceptB
        For each neighbor of current:
            Add neighbor to Q if not already visited
            Record the path taken
    Return "No connection found"
```

This breadth-first search algorithm guarantees finding the shortest path between concepts if one exists, but requires storing and processing potentially many intermediate states.

#### The Chunked Algorithm:

```python
function findChunkedConnection(conceptA, conceptB):
    If directConnectionExists(conceptA, conceptB): # Checks a lookup table of pre-computed paths
        Return direct connection
    Else:
        Fall back to standard search algorithm # Or a more limited search
```

The `directConnectionExists` function checks a lookup table of pre-computed paths, effectively "chunking" commonly used multi-step inferences into single-step connections.

### LLM Analogues and Behaviors

Large Language Models exhibit behaviors analogous to chunking:
*   **Learned Phrases & N-grams:** LLMs inherently learn common sequences of tokens (words or sub-words) that frequently appear together. These function like pre-compiled "chunks" that can be generated rapidly.
*   **Attention Mechanisms:** Transformer attention mechanisms can dynamically create "high-level linkages" by directly connecting distant but relevant parts of an input sequence to generate an output, effectively bypassing intermediate reasoning steps. Some research explicitly analyzes attention patterns as reflecting a chunking mechanism for input context.[[5](https://arxiv.org/abs/2412.04757)][[6](https://dev.to/foxgem/overview-infiniretri-enhancing-llms-for-infinite-length-context-via-attention-based-retrieval-21ib)]
*   **Function Calling/Tool Use:** When LLMs are augmented with the ability to call external functions or tools, they are using a highly optimized, "chunked" pathway to perform a specific task (e.g., a calculation, a database lookup) rather than attempting to reason it out from first principles. This is akin to an expert relying on a well-honed skill.
*   **Efficient Attention on KV Cache:** Techniques like ChunkAttention optimize LLM inference by sharing and batching computations for common prompt prefixes, essentially treating these shared prefixes as pre-processed chunks.[[7](https://openreview.net/forum?id=9k27IITeAZ)] Approaches like Dual Chunk Attention (DCA) further optimize attention by processing data in chunks, managing computational resources efficiently for long contexts.[[8](https://adasci.org/long-context-comprehension-with-dual-chunk-attention-dca-in-llms/)]

### Computational Rationality

The chunking strategy is computationally rational under constraints because:

1.  **Memory efficiency**: Storing compressed chunks (or learned weights that represent them) requires significantly less memory than all possible detailed pathways.
2.  **Time efficiency**: Chunk-based reasoning approaches much faster inference for common pathways compared to exhaustive search-based reasoning.
3.  **Error profile**: Errors typically occur when exceptions to the chunked rule exist, an acceptable trade-off if these exceptions are rare or the cost of the error is low compared to the efficiency gain.

This creates a power-law efficiency: Frequently used reasoning patterns become extremely efficient at the cost of potentially missing edge cases—exactly the pattern we see in human expertise development and increasingly in optimized LLM behaviors.

## Strategy 2: Generative Models of Relationships (Factoring Links)

### The Psychological Phenomenon

**Schema-based reasoning** involves using abstract knowledge structures to generate expectations and inferences about new situations without storing every possible relationship[^3]. This manifests psychologically as our ability to make reasonable guesses about novel situations based on their similarity to familiar categories.

[^3]: Bartlett, F.C. (1932). Remembering: A Study in Experimental and Social Psychology. Cambridge University Press. This classic work introduced the concept of schemas as dynamic knowledge structures that guide perception and memory.

### Real-World Examples

1.  **Restaurant scripts**: When entering a new restaurant, we automatically know to wait to be seated, expect a menu, and pay after eating—without having to memorize the procedure for each specific establishment[^4].
2.  **Technological interfaces**: We can navigate new smartphone apps using general interface schemas without reading instructions for each one.
3.  **Social relationships**: We apply relationship models (friend, colleague, authority figure) to new acquaintances that generate appropriate behavioral expectations.

[^4]: Schank, R. C., & Abelson, R. P. (1977). Scripts, plans, goals, and understanding: An inquiry into human knowledge structures. Lawrence Erlbaum. This work formalized how people use schematic knowledge structures ("scripts") to navigate common social situations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function determineRelationship(conceptA, conceptB):
    Look up in complete relationship matrix M[conceptA, conceptB]
    Return stored relationship type and strength
```

This approach requires storing an explicit relationship between every pair of concepts—an $O(n^2)$ space requirement where $n$ is the number of concepts.

#### The Generative Algorithm:

```python
function generateRelationship(conceptA, conceptB):
    features_A = extractFeatures(conceptA)
    features_B = extractFeatures(conceptB)
    relationship = relationshipModel(features_A, features_B) # A learned model
    Return relationship
```

This approach uses a parameterized model that generates likely relationships based on concept features rather than storing each relationship explicitly.

### LLM Analogues and Behaviors

LLMs are inherently generative models that learn statistical relationships:
*   **Core Functionality:** LLMs learn the statistical patterns of how tokens relate to each other from vast datasets. They don't store every explicit fact but generate responses based on these learned "schemas" of language and conceptual relationships. Their ability to predict the next token is a form of generating relationships.[[9](https://www.i-jmr.org/2025/1/e59823)][[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)]
*   **Analogy and Metaphor Generation:** LLMs can create novel analogies and explain concepts in various ways, suggesting they've captured underlying relational structures rather than just memorizing instances.
*   **Emergent "World Models":** There's ongoing research into whether LLMs develop implicit "world models"—internal representations of how entities and concepts relate in the world—which guide their generation of coherent and contextually appropriate text.[[11](https://www.assemblyai.com/blog/emergent-abilities-of-large-language-models)][[12](https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/)]

### Computational Rationality

The generative model strategy is computationally rational under constraints because:

1.  **Memory efficiency**: Storing a parametric model with $k$ parameters where $k \ll n^2$ drastically reduces memory requirements.
2.  **Generalization**: The model can generate reasonable relationship hypotheses for entirely new concepts.
3.  **Update efficiency**: New information can update the general model rather than requiring updates to many individual relationships.
4.  **Graceful degradation**: When exact relationships aren't known, the system still produces plausible approximations.

The trade-off is reduced precision for specific cases that deviate from general patterns, which is optimal when most relationships follow regular patterns and resources are insufficient to memorize all exceptions.

## Strategy 3: Prototype-Based Representation (Sketched Nodes)

### The Psychological Phenomenon

**Prototype theory** proposes that humans categorize objects by comparing them to abstract prototypes that represent the central tendency of the category, rather than through strict definitional boundaries[^5]. This allows efficient representation of complex categories using only a few exemplars.

[^5]: Rosch, E. (1975). Cognitive representations of semantic categories. Journal of Experimental Psychology: General, 104(3), 192–233. This research demonstrated that people judge category membership by similarity to prototypes rather than by necessary and sufficient conditions.

### Real-World Examples

1.  **Bird recognition**: We recognize birds by their similarity to prototypical birds (like robins) rather than checking a list of necessary and sufficient conditions, which explains why penguins and ostriches are psychologically "less bird-like"[^6].
2.  **Facial recognition**: We identify faces by comparing them to abstracted prototypes rather than memorizing every possible face.
3.  **Concept learning**: Children learn concepts like "chair" by exposure to examples and abstraction of common features, not by memorizing definitions.

[^6]: Lakoff, G. (1987). Women, Fire, and Dangerous Things: What Categories Reveal about the Mind. University of Chicago Press. This work explored how prototypes and radial categories structure human conceptual systems.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function representConcepts(domain):
    concepts = []
    For each distinct entity in domain:
        Store complete feature vector
        Add to concepts
    Return concepts
```

This approach stores every concept as a separate entity with its full feature representation, requiring $O(nf)$ space where $n$ is the number of concepts and $f$ is the number of features.

#### The Prototype Algorithm:

```python
function representWithPrototypes(domain):
    clusters = findClusters(domain)
    prototypes = []
    For each cluster:
        prototype = computeCentralTendency(cluster)
        Add prototype to prototypes
    function recognizeConcept(entity):
        Return nearestPrototype(entity, prototypes) + transformVector # Transform accounts for deviation
    Return prototypes, recognizeConcept
```

This approach stores only cluster prototypes plus transformation rules, reducing storage requirements significantly.

### LLM Analogues and Behaviors

LLMs utilize representations that share characteristics with prototype theory:
*   **Embeddings:** Word and sentence embeddings in LLMs represent concepts as vectors in a high-dimensional space. Concepts with similar meanings are clustered together, with the "center" of such a cluster acting like a prototype. The model can then reason about new words or phrases based on their proximity to these learned prototypes.
*   **Few-Shot Learning / In-Context Learning:** When an LLM learns a new task from a few examples provided in the prompt (few-shot or in-context learning), it's essentially abstracting a "prototype" of the task or concept from those examples.[[13](https://aclanthology.org/2024.acl-long.279/)] It then applies this abstracted prototype to new, unseen instances.

### Computational Rationality

The prototype strategy is computationally rational under constraints because:

1.  **Memory efficiency**: Storing $k$ prototypes (or the parameters that define the embedding space) where $k \ll n$ reduces memory requirements.
2.  **Generalization capacity**: Novel entities can be understood or represented as transformations of or combinations of existing prototypes (vectors).
3.  **Retrieval efficiency**: Similarity-based retrieval in embedding space allows for fast approximate matching.
4.  **Graceful degradation**: Even with limited information, the system can approximate concepts by their nearest prototype.

The trade-off is category boundary fuzziness and typicality effects, which are acceptable when exact boundaries are rarely needed and resources are insufficient to store every instance.

## Strategy 4: Context-Dependent Inconsistency Tolerance

### The Psychological Phenomenon

**Belief compartmentalization** refers to the human tendency to hold contradictory beliefs simultaneously by segregating them into different contexts or domains[^7]. Rather than maintaining global consistency, we allow local inconsistencies when they serve practical purposes.

[^7]: Festinger, L. (1957). A Theory of Cognitive Dissonance. Stanford University Press. This influential work explored how people manage contradictory beliefs, often through compartmentalization to reduce cognitive dissonance.

### Real-World Examples

1.  **Religious and scientific beliefs**: Many scientists maintain religious beliefs that would appear to contradict their scientific understanding, activating different belief systems in different contexts[^8].
2.  **Health behaviors**: People often maintain inconsistent beliefs about health risks, such as knowing smoking causes cancer while believing "it won't happen to me."
3.  **Professional vs. personal ethics**: People may apply different ethical standards in business contexts than in personal relationships.

[^8]: Legare, C. H., & Visala, A. (2011). Between religion and science: Integrating psychological and philosophical accounts of explanatory coexistence. Human Development, 54(3), 169-184. This research examines how people integrate seemingly incompatible religious and scientific explanations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function maintainConsistency(knowledgeBase, newFact):
    If contradicts(newFact, knowledgeBase):
        Resolve contradiction by:
            - Rejecting newFact
            - Removing contradicting facts
            - Creating complex exception rules
            - Restructuring knowledge hierarchy
    Add newFact to knowledgeBase
    Return knowledgeBase
```

This approach ensures global consistency but requires expensive contradiction detection and resolution operations that scale with knowledge base size.

#### The Compartmentalization Algorithm:

```python
function contextualKnowledge(newFact, context):
    contextualKB = knowledgeBase.getContext(context) # Activates a relevant subset
    Add newFact to contextualKB
    function retrieveFact(query, context):
        Return knowledgeBase.getContext(context).lookup(query)
    Return retrieveFact
```

This approach stores knowledge in context-specific compartments, only checking for consistency within relevant contexts.

### LLM Analogues and Behaviors

LLMs exhibit behaviors that mirror context-dependent inconsistency:
*   **Context Window Limitations:** LLMs operate with a finite "context window"—they only consider a certain amount of recent text when generating a response.[[14](https://nebius.com/blog/posts/context-window-in-ai)][[15](https://bdtechtalks.com/2025/02/05/the-context-window-problem-or-why-llm-forgets-the-middle-of-a-long-file/)][[16](https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot)][[17](https://nlpnest.com/unlocking-the-context-window-in-llms/)] Information outside this window is effectively "forgotten," which can lead to inconsistencies if a long conversation refers back to points that are no longer in the active context. This is analogous to human compartmentalization, where only the current "active context" is fully coherent.[[16](https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot)]
*   **Prompt Sensitivity:** The same LLM can provide different or even contradictory answers to semantically similar questions if they are phrased differently or if the preceding context in the prompt changes.[[18](https://arxiv.org/html/2501.11709v3)] This suggests that their "knowledge" is not globally consistent but is activated and shaped by the immediate input context.
*   **"Context Degradation Syndrome":** In very long interactions, LLM responses can become repetitive or lose focus, indicating a breakdown in coherence as the initial context gets pushed out of the window.[[16](https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot)]

### Computational Rationality

The compartmentalization strategy is computationally rational under constraints because:

1.  **Computational efficiency**: Consistency checking is limited to relevant subsets of knowledge rather than the entire knowledge base.
2.  **Practical accuracy**: Domain-specific approximations can be more accurate within their domains than general rules that must account for all cases.
3.  **Learning efficiency**: New information can be incorporated without expensive global restructuring.
4.  **Adaptability**: Different contexts can maintain specialized knowledge representations optimized for their domain.

The trade-off is potential contradictions when contexts overlap or when information from outside the immediate context is crucial. This is acceptable when most reasoning occurs within specific contexts and the computational cost of maintaining global consistency is prohibitive.[[14](https://nebius.com/blog/posts/context-window-in-ai)]

## Strategy 5: Recency and Availability Heuristics

### The Psychological Phenomenon

The **availability heuristic** causes people to judge the likelihood of events based on how easily examples come to mind[^9]. Related to this, the **recency effect** gives disproportionate weight to recently encountered information. Together, these cognitive shortcuts prioritize information that is likely to be relevant in the current temporal and spatial context.

[^9]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology, 5(2), 207–232. This paper introduced the availability heuristic as a mental shortcut that relies on immediate examples that come to mind.

### Real-World Examples

1.  **Risk assessment**: People overestimate the likelihood of plane crashes after media coverage of an accident, while underestimating more common but less publicized risks like heart disease.
2.  **Stock market decisions**: Investors give more weight to recent market performance than long-term trends.
3.  **Consumer choices**: Purchase decisions are heavily influenced by recently viewed advertisements or recommendations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function assessProbability(event):
    Count all historical occurrences of event
    Count all possible scenarios
    Return occurrences / possible scenarios
```

This approach requires maintaining complete historical statistics and computing true frequencies, which is memory and computation intensive.

#### The Availability Algorithm:

```python
function estimateProbability(event):
    examples = retrieveExamples(event) # Based on ease of retrieval
    recencyWeight = function(example):
        Return 1 / (current_time - example.time)
    availability = sum(recencyWeight(e) for e in examples) # Simplified proxy for probability
    Return availability
```

This approach estimates probabilities based on the ease of retrieving examples, with a strong recency bias.

### LLM Analogues and Behaviors

LLMs demonstrate behaviors consistent with recency and availability:
*   **Recency Bias in Prompts:** Information presented later in an LLM's prompt often has a disproportionately strong influence on its output.[[19](https://arxiv.org/html/2402.01769v1)] This is a well-documented phenomenon where the "most available" recent input tokens heavily guide generation.
*   **Influence of Training Data Frequency (Availability):** Concepts, facts, styles, and even biases that are more frequent in the LLM's training data are more "available" to the model and thus more likely to be reproduced in its outputs, irrespective of their objective truth or nuanced importance.[[19](https://arxiv.org/html/2402.01769v1)][[20](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)][[21](https://www.comet.com/site/blog/llm-hallucination/)]
*   **Outputting Common/Fluent Phrases:** LLMs tend to generate common and fluent phrases (high availability from their training data) because these represent high-probability sequences. This can sometimes come at the expense of more precise or less common, but more appropriate, phrasing.

### Computational Rationality

The availability/recency strategy is computationally rational under constraints because:

1.  **Memory efficiency**: It relies on readily accessible information (e.g., recent items in a context window, high-frequency patterns in training data) rather than requiring exhaustive search or storage of complete historical statistics.
2.  **Temporal relevance**: Recent events or information are often more predictive of current conditions due to environmental autocorrelation.
3.  **Computational simplicity**: It uses retrieval fluency or pattern frequency as a proxy for probability, avoiding complex calculations.
4.  **Attentional allocation**: Resources are directed to information that is likely to be immediately relevant.

The trade-off is systematic bias when retrieval ease (e.g., due to media exposure, emotional salience, or training data imbalances) distorts true frequencies or importance.[[19](https://arxiv.org/html/2402.01769v1)][[20](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)] This is acceptable when the environment is relatively stable and recent/frequent information is generally more relevant.

## Strategy 6: Confirmation Bias and Hypothesis Maintenance

### The Psychological Phenomenon

**Confirmation bias** is the tendency to search for, interpret, and recall information in a way that confirms existing beliefs[^10]. While often framed as a cognitive flaw, it can be viewed as a resource-efficient strategy for maintaining stable beliefs in noisy information environments.[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)]

[^10]: Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. Review of General Psychology, 2(2), 175–220. This comprehensive review documents confirmation bias across many domains and explains its cognitive foundations.

### Real-World Examples

1.  **Political beliefs**: People selectively consume news that aligns with their political views and interpret ambiguous events as supporting their position.
2.  **Scientific research**: Scientists may design experiments to confirm rather than challenge their hypotheses and be more critical of methodologies in studies with contrary findings.
3.  **Relationship judgments**: People tend to notice behaviors that confirm initial impressions of others while overlooking contradictory evidence.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function evaluateHypothesis(hypothesis, data):
    For each possible alternative hypothesis:
        Calculate P(data|hypothesis) for all data points
        Calculate prior probability P(hypothesis)
        Apply Bayes' rule to compute P(hypothesis|data)
    Return hypothesis with highest posterior probability
```

This approach requires maintaining and evaluating all possible alternative hypotheses, which is computationally expensive.

#### The Confirmation-Biased Algorithm:

```python
function maintainHypothesis(currentHypothesis, newData):
    If supports(newData, currentHypothesis):
        Increase confidence in currentHypothesis
    Else if weaklyContradicts(newData, currentHypothesis):
        Discount or reinterpret newData # Or assign lower weight
    Else if stronglyContradicts(newData, currentHypothesis):
        Consider revising hypothesis # Higher threshold for revision
    Return updated currentHypothesis and confidence
```

This approach maintains the current hypothesis unless strongly contradicted, focusing computational resources on interpretation rather than complete re-evaluation.

### LLM Analogues and Behaviors

LLMs can exhibit behaviors that resemble confirmation bias:
*   **Generating Consistent (but Potentially Flawed) Narratives:** Once an LLM begins generating text along a particular "hypothesis" or narrative thread (often seeded by the initial prompt), it tends to continue in that direction, reinforcing its initial output. This can lead to plausible-sounding but factually incorrect "hallucinations" if the initial direction was flawed.[[9](https://www.i-jmr.org/2025/1/e59823)][[19](https://arxiv.org/html/2402.01769v1)]
*   **Influence of User Input and Prompts:** If a user's prompt suggests a certain belief or frames a question in a biased way, the LLM may be more likely to generate a response that "confirms" that implicit bias, rather than challenging it or offering neutral information.[[19](https://arxiv.org/html/2402.01769v1)][[22](https://arxiv.org/abs/2412.04629)]
*   **Reinforcement Learning from Human Feedback (RLHF):** While RLHF aims to align LLMs with human preferences, if human raters exhibit confirmation biases when evaluating responses, the LLM can inadvertently be trained to perpetuate those biases.[[19](https://arxiv.org/html/2402.01769v1)] Some research explores how LLM-generated debates with multiple personas can help reduce user confirmation bias.[[22](https://arxiv.org/abs/2412.04629)]

### Computational Rationality

The confirmation bias strategy is computationally rational under constraints because:

1.  **Computational efficiency**: Evaluating a single (or few) prevailing hypothesis against new data is less costly than constantly re-evaluating all possible hypotheses.
2.  **Learning stability**: It prevents rapid belief oscillation in noisy environments where contradictory evidence might be spurious or misleading.
3.  **Resource allocation**: It focuses cognitive resources on refining and elaborating the current best model of the world rather than constantly searching for entirely new models.
4.  **Search efficiency**: It directs information seeking toward data that is most likely to be relevant to the current hypothesis.

The trade-off is resistance to belief updating, especially when the environment changes significantly or the initial hypothesis is deeply flawed. This is acceptable when the environment is relatively stable, the cost of erroneously changing a correct belief is high, or resources are insufficient to constantly entertain multiple complex hypotheses.

## Strategy 7: Satisficing Decision Making

### The Psychological Phenomenon

**Satisficing** is a decision-making strategy where people accept "good enough" solutions rather than optimizing for the best possible outcome[^11]. Rather than exhaustively evaluating all options, people stop searching once they find an acceptable alternative.

[^11]: Simon, H. A. (1956). Rational choice and the structure of the environment. Psychological Review, 63(2), 129–138. Herbert Simon introduced the concept of satisficing as a bounded rationality strategy that seeks adequacy rather than optimality.

### Real-World Examples

1.  **Consumer purchases**: Instead of reviewing all possible products, shoppers often buy the first item that meets their basic requirements.
2.  **Hiring decisions**: Recruiters may hire the first candidate who exceeds a threshold of qualifications rather than interviewing all applicants.
3.  **Everyday problem solving**: When facing a computer issue, people typically try solutions until one works, rather than analyzing the optimal approach.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function optimizeDecision(options, valuationFunction):
    bestOption = null
    bestValue = -infinity
    For each option in options:
        value = valuationFunction(option)
        If value > bestValue:
            bestValue = value
            bestOption = option
    Return bestOption
```

This approach evaluates every option to find the global optimum, requiring $O(n)$ evaluations where $n$ is the number of options.

#### The Satisficing Algorithm:

```python
function satisfice(options, acceptabilityThreshold, valuationFunction):
    For each option in options:
        If valuationFunction(option) >= acceptabilityThreshold:
            Return option # First "good enough" option
    // Fallback if no option meets threshold (optional)
    Return optimizeDecision(options, valuationFunction)
```

This approach returns the first acceptable option encountered, requiring only $O(k)$ evaluations in the best case, where $k$ is the position of the first acceptable option.

### LLM Analogues and Behaviors

LLM generation processes often involve satisficing:
*   **Decoding Strategies (Top-k, Nucleus Sampling):** LLMs rarely use greedy decoding (always picking the single most probable next token) as it often leads to repetitive or dull text. Instead, they employ sampling strategies like:
    *   **Top-k sampling:** Consider only the 'k' most probable next tokens and sample from this reduced set.
    *   **Nucleus (Top-p) sampling:** Consider the smallest set of most probable tokens whose cumulative probability exceeds a threshold 'p', and sample from this set.
    These are forms of satisficing: selecting a "good enough" token from a limited, high-probability set rather than exhaustively searching for or committing to the single "best" (most probable) token, which balances coherence and diversity.
*   **Stopping Criteria:** LLMs cease generating text based on various criteria (e.g., maximum length, generation of a stop token), not necessarily when an "optimal" or "complete" answer (if such a thing could be defined) is reached.

### Computational Rationality

The satisficing strategy is computationally rational under constraints because:

1.  **Search termination**: Early stopping dramatically reduces the average-case computational complexity.
2.  **Diminishing returns**: The marginal gain in utility from finding the absolute optimal solution over a "good enough" one is often small compared to the additional search cost.
3.  **Time sensitivity**: Many decisions lose value if delayed, making a quick "good enough" decision preferable to a slow optimal one.
4.  **Resource reallocation**: Computational resources saved through satisficing can be allocated to other tasks or problems.

The trade-off is settling for suboptimal solutions. This is acceptable when the distribution of option values is such that many "good enough" options exist, search costs are high relative to the benefits of full optimization, or time pressure demands rapid responses.

## Strategy 8: False Memory and Pattern Completion

### The Psychological Phenomenon

**False memory** refers to the phenomenon where people remember events that never occurred or remember them differently from how they occurred[^12]. This can be viewed as an adaptive pattern completion mechanism rather than simply a memory failure. The brain often fills in gaps with plausible information consistent with existing schemas.

[^12]: Loftus, E. F. (2005). Planting misinformation in the human mind: A 30-year investigation of the malleability of memory. Learning & Memory, 12(4), 361–366. This paper reviews research showing how memory reconstructs rather than reproduces past events.

### Real-World Examples

1.  **Eyewitness testimony**: Witnesses often "remember" details that align with their expectations or schemas rather than what they actually observed.
2.  **Childhood memories**: People incorporate family stories and photographs into their "memories," believing they remember events they only heard about.
3.  **Educational contexts**: Students often misremember information in ways that make it more coherent with their existing knowledge.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function recall(event):
    Retrieve complete storage record of event
    If record exists:
        Return record
    Else:
        Return "No memory found"
```

This approach requires perfect, verbatim storage and retrieval of all experienced events, which is extremely memory intensive and inflexible.

#### The Pattern Completion Algorithm:

```python
function reconstructiveRecall(eventPartial):
    knownFragments = retrieve(eventPartial) # Retrieve stored fragments related to the cue
    context = getCurrentContext()
    schemaExpectations = activateSchema(context) # Activate relevant general knowledge
    reconstructed = combine(knownFragments, schemaExpectations) # Fill gaps plausibly
    Return reconstructed
```

This approach reconstructs memories by combining stored fragments with schematic expectations and general knowledge.

### LLM Analogues and Behaviors

LLMs exhibit a striking parallel to false memory through "hallucinations" or "confabulations":
*   **Hallucinations/Confabulations:** LLMs frequently generate plausible-sounding information that is not factually correct or not present in their training data.[[9](https://www.i-jmr.org/2025/1/e59823)][[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)][[19](https://arxiv.org/html/2402.01769v1)][[21](https://www.comet.com/site/blog/llm-hallucination/)] They "fill in the gaps" to provide a coherent-seeming response, much like human reconstructive memory. Some researchers argue "confabulation" is a more accurate term than "hallucination" for LLMs, as it describes producing false memories without intent to deceive, often to complete a narrative.[[23](https://pmc.ncbi.nlm.nih.gov/articles/PMC10619792/)][[24](https://community.openai.com/t/hallucination-vs-confabulation/172639)][[25](https://www.integrative-psych.org/resources/confabulation-not-hallucination-ai-errors)][[26](https://www.researchgate.net/publication/375206401_Hallucination_or_Confabulation_Neuroanatomy_as_metaphor_in_Large_Language_Models)]
*   **Over-generalization and Factual Invention:** The model might combine disparate pieces of information from its training data in a novel but incorrect way, creating a "false memory" of a connection or fact that doesn't exist.[[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)][[21](https://www.comet.com/site/blog/llm-hallucination/)] This is driven by their training to produce statistically probable sequences, even if those sequences don't align with ground truth.

### Computational Rationality

The pattern completion/reconstructive memory strategy is computationally rational under constraints because:

1.  **Storage efficiency**: Storing the "gist" or key elements and relying on generative processes to fill in details requires much less memory than storing complete episodic records.
2.  **Retrieval robustness**: Pattern completion allows recall and generation from partial cues, making the system more fault-tolerant and flexible.
3.  **Generalization capacity**: Reconstructed "memories" or generated text often emphasize schema-consistent aspects that are more likely to be useful or understandable in future, similar situations.
4.  **Prediction utility**: Filled-in details often represent statistically likely truths based on the learned patterns in the data, even if not specifically factual for a given instance.

The trade-off is reduced accuracy for specific details and the generation of entirely false information.[[9](https://www.i-jmr.org/2025/1/e59823)][[21](https://www.comet.com/site/blog/llm-hallucination/)] This is acceptable when the gist is more important than perfect detail, storage capacity is limited, and the environment (or training data) contains strong statistical regularities that make "educated guesses" often plausible.

## Strategy 9: Question Substitution (Attribute Substitution)

### The Psychological Phenomenon

Attribute substitution occurs when people respond to a difficult question by unconsciously substituting it with an easier one[^13]. Rather than engaging in computationally expensive reasoning about a complex attribute, the mind quickly assesses a related but simpler attribute.

[^13]: Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In T. Gilovich, D. Griffin, & D. Kahneman (Eds.), Heuristics and biases: The psychology of intuitive judgment (pp. 49–81). Cambridge University Press. This paper introduced the concept of attribute substitution as a general mechanism underlying many cognitive biases.

### Real-World Examples

1.  **Risk assessment:** When asked "How dangerous is this activity?" people often answer the easier question "How afraid does this make me feel?" which explains why shark attacks seem more dangerous than diabetes despite vastly different mortality rates.
2.  **Person evaluation:** When asked "Will this candidate be successful?" interviewers often substitute "Did I feel good during the interview?" leading to confidence in judgments with poor predictive validity.
3.  **Economic forecasting:** When asked "How will the market perform next year?" experts often answer the easier question "How has the market performed recently?" leading to trend extrapolation.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function evaluateAttribute(target, complexAttribute):
    relevantFactors = identifyAllFactors(complexAttribute)
    data = collectDataForAllFactors(target, relevantFactors)
    weights = determineFactorWeights(complexAttribute)
    # Complex modeling and calculation follows
    Return weightedCalculation(data, weights)
```

This approach requires extensive data collection, causal analysis, and computational resources to properly evaluate complex attributes.

#### The Substitution Algorithm:

```python
function substituteAttribute(target, complexAttribute):
    accessibleAttributes = identifyAccessibleAttributes(target) # Find easily computable attributes
    # Select a substitute that is correlated (even if imperfectly) and much easier to evaluate
    substituteAttribute = selectCorrelatedEasierAttribute(accessibleAttributes, complexAttribute)
    return evaluateSimpleAttribute(target, substituteAttribute)
```

This approach replaces the difficult evaluation with a simpler one based on an accessible attribute that is somewhat correlated with the target attribute.

### LLM Analogues and Behaviors

LLMs can exhibit behaviors analogous to attribute substitution:
*   **Answering a Simpler Version of the Question:** If a prompt is very complex, ambiguous, or requires deep reasoning beyond the LLM's current capabilities or readily available patterns, it might generate a response that addresses a related but simpler aspect of the question.[[28](https://arxiv.org/html/2503.16515v1)]
*   **Focusing on Keywords over Nuance:** LLMs might latch onto salient keywords in a prompt and generate text primarily related to those keywords, potentially missing the more nuanced intent of the overall question. This is like substituting "what is this keyword associated with?" for "what is the complex meaning of this entire query?"
*   **Generating Generic or Superficial Answers:** When asked for highly specific, deep, or novel analysis (a complex attribute to compute), an LLM might provide a more generic, superficial, or common answer (a simpler, more "accessible" attribute from its training data). Studies show LLMs struggle with nuanced, domain-specific tasks without careful prompting or fine-tuning.[[28](https://arxiv.org/html/2503.16515v1)]

### Computational Rationality

The question substitution strategy is computationally rational under constraints because:

1.  **Computational efficiency:** Evaluating a simple attribute (e.g., keyword association, generating a common pattern) is often orders of magnitude less computationally intensive than a complex, multi-step reasoning process.
2.  **Data requirements:** Simple attributes typically rely on more readily available patterns in the training data.
3.  **Response speed:** Substitution allows for rapid responses, which is crucial when interaction speed is valued.
4.  **Heuristic value:** The substitute attribute often correlates sufficiently with the complex target attribute to provide an answer that is better than random chance, or at least plausible.

The trade-off is systematic bias when the substitute attribute significantly diverges from the target attribute.[[30](https://www.flyrank.com/id/blogs/berita-ai/study-reveals-chatgpt-s-cognitive-shortcuts-and-biases-questioning-ai-s-trustworthiness-in-critical-decisions)] This is acceptable when the correlation is reasonably high in common scenarios, the cost of delay for a more precise answer outweighs the cost of imprecision, or the computational investment for a precise analysis is not justified or feasible.

## Strategy 10: Logical Fallacies as Computational Shortcuts

### The Psychological Phenomenon

Logical fallacies are patterns of reasoning that appear valid but contain logical flaws[^14]. While traditionally viewed as errors, many common fallacies can be understood as computationally efficient cognitive shortcuts that often work well in typical social or everyday environments despite being logically invalid in a formal sense.[[4](http://www.keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich.Sternberg2003.pdf)]

[^14]: Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131. While not focused specifically on logical fallacies, this paper established how seemingly irrational cognitive shortcuts serve pragmatic functions.

### Real-World Examples

1.  **Appeal to authority:** When facing complex topics like climate science or medicine, deferring to expert opinion is computationally cheaper than personally evaluating all evidence, even though it's technically a logical fallacy if the authority is not a relevant expert or if their claims are unscrutinized.
2.  **Ad hominem reasoning (circumstantial):** Discounting arguments from sources with clear conflicts of interest can be an efficient filtering mechanism, though logically the source's characteristics don't determine the truth value of the argument itself.
3.  **Post hoc ergo propter hoc (correlation-causation confusion):** Assuming that if B follows A, then A caused B, provides a simple causal model that's often a useful first guess in everyday experience (e.g., "I ate the berries, then I got sick, so the berries made me sick"), despite being logically invalid without further evidence.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function evaluateArgument(claim, evidence, source, context):
    formalizeLogic(claim, evidence)
    verifyPremises(evidence) # Check truthfulness of each piece of evidence
    checkValidityOfInference(claim, evidence) # Check logical structure
    assessSourceReliability(source, context) # Evaluate expertise, bias
    checkForAlternativeExplanations(claim, evidence)
    assessPriorProbability(claim)
    Return validityScore, probabilityScore
```

This approach requires formal logical analysis, verification of all premises, evaluation of source credibility, and consideration of alternative explanations—a highly resource-intensive process.

#### The Fallacy-Based Heuristic Algorithm:

```python
function quickArgumentEvaluation(claim, source, context, evidenceStructure):
    if isAuthoritativeSource(source, relevantDomain=context.domain) && !requiresHighPrecision(context):
        Return acceptClaim(claim) with moderateConfidence
    if evidenceStructure.pattern == "B_follows_A" && !requiresHighPrecision(context):
        Return tentativelyAcceptCausation(A_causes_B)
    if hasStrongConflictOfInterest(source, claim):
        Return lowerConfidenceInClaim(claim) or seekCorroboration
    // More fallacy-based shortcuts...
    // Fall back to more careful analysis if context requires or shortcut yields low confidence
```

This approach uses source characteristics, simple structural patterns, and contextual relevance as proxies for thorough logical analysis.

### LLM Analogues and Behaviors

LLMs, trained on vast amounts of human text, can reproduce and sometimes appear to "use" patterns analogous to logical fallacies:
*   **Reproducing Fallacies from Training Data:** Human language is replete with logical fallacies. LLMs learn these patterns and can generate text that includes them. For instance, an LLM might generate an argument that sounds authoritative (appeal to authority) because that pattern is common, even if the substance is weak or the "authority" cited is misattributed or irrelevant.[[31](https://zilliz.com/blog/how-to-detect-and-correct-logical-fallacies-from-genai-models)][[32](https://aclanthology.org/2025.naacl-long.374.pdf)] Studies show LLMs can generate arguments containing various fallacies.[[32](https://aclanthology.org/2025.naacl-long.374.pdf)]
*   **Correlation as Causation:** LLMs are excellent at identifying statistical correlations in their training data. They might present these correlations as causal relationships because such inferences are common in human discourse, even if not logically sound without further evidence.[[33](https://arxiv.org/abs/2410.05229)][[34](https://www.mobihealthnews.com/news/apple-study-highlights-limitations-llms)][[35](https://www.computing.co.uk/news/2024/ai/researchers-find-flaws-llm-reasoning)][[36](https://learnprompting.org/docs/basics/pitfalls)][[37](https://kili-technology.com/large-language-models-llms/llm-reasoning-guide)]
*   **Superficial Pattern Matching for Plausibility:** An LLM might assess or generate an argument based on superficial linguistic features (e.g., presence of "sciency" words, confident tone, common argumentative structures) rather than deep logical structure, similar to how humans can be persuaded by arguments that "sound right." Their core mechanism is predicting plausible next tokens, not verifying logical validity.[[9](https://www.i-jmr.org/2025/1/e59823)][[31](https://zilliz.com/blog/how-to-detect-and-correct-logical-fallacies-from-genai-models)]
*   **Sensitivity to Phrasing over Logic:** LLMs can be swayed by how a problem is phrased, even if the underlying logical structure remains the same, indicating their reasoning is not always robustly logical.[[33](https://arxiv.org/abs/2410.05229)][[34](https://www.mobihealthnews.com/news/apple-study-highlights-limitations-llms)][[35](https://www.computing.co.uk/news/2024/ai/researchers-find-flaws-llm-reasoning)] Some research aims to improve LLM logical reasoning by fine-tuning them on datasets designed to counteract cognitive biases and fallacies.[[38](https://openreview.net/forum?id=mfTM4UdYnC)][[39](https://openreview.net/pdf/810efa50e83dbf741cb856f5b356071b769afb49.pdf)][[40](https://aclanthology.org/2024.emnlp-main.794.pdf)]

### Computational Rationality

Using these "fallacy-like" heuristics can be computationally rational under constraints because:

1.  **Computational simplicity:** Evaluating source trustworthiness (even superficially) or temporal sequence is much simpler and faster than formal logical deconstruction.
2.  **Social & Environmental Efficiency:** Many fallacies encode heuristics that are often "good enough" in everyday social interactions or stable environments. For example, generally trusting recognized experts (a form of appeal to authority) is often an adaptive shortcut.
3.  **Speed advantage:** Heuristic-based evaluation provides immediate assessments when formal analysis would be prohibitively time-consuming or impossible given available information.
4.  **Cognitive accessibility:** Patterns like authority appeals or simple causal inferences (A then B, so A caused B) are easily applied across many domains without requiring deep, domain-specific logical expertise.

These shortcuts become problematic primarily when applied in contexts requiring high rigor (e.g., scientific reasoning, legal judgments, critical safety decisions) where their underlying assumptions don't hold, or when exploited by bad actors.

## The Double-Edged Sword: Nuancing Computational Rationality

While framing these cognitive and algorithmic strategies as "computationally rational" offers valuable insights, it's crucial to nuance this perspective. The "optimality" of these approximate reasoning methods is highly context-dependent and comes with significant trade-offs.

1.  **Context is Key:** A strategy that is efficient and effective in one environment (e.g., making quick social judgments) can be detrimental in another (e.g., conducting rigorous scientific research or ensuring fairness in AI decision-making).[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)] The statistical properties of the environment and the specific goals of the reasoning agent determine whether a heuristic is truly adaptive.
2.  **The "Dark Side" of Heuristics:** While these shortcuts save cognitive resources, they are also the root of many well-documented biases that can lead to poor decisions, prejudice, and errors in critical situations.[[20](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)][[30](https://www.flyrank.com/id/blogs/berita-ai/study-reveals-chatgpt-s-cognitive-shortcuts-and-biases-questioning-ai-s-trustworthiness-in-critical-decisions)][[41](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)]
    *   **Stereotyping (Chunking/Prototypes):** Can lead to prejudice and discrimination.
    *   **Confirmation Bias:** Can entrench false beliefs and hinder learning.[[19](https://arxiv.org/html/2402.01769v1)][[22](https://arxiv.org/abs/2412.04629)]
    *   **Availability Heuristic:** Can lead to misjudgment of risks and poor decision-making (e.g., overestimating rare but vivid events).[[19](https://arxiv.org/html/2402.01769v1)][[20](https://shs.cairn.info/journal-of-innovation-economics-2024-2-page-223?lang=en)][[42](https://www.itschiara.me/ai-human-collaboration)]
    *   **False Memories/Hallucinations:** Can have serious consequences if acted upon as truth, especially in domains like medicine or law.[[9](https://www.i-jmr.org/2025/1/e59823)][[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)][[19](https://arxiv.org/html/2402.01769v1)][[21](https://www.comet.com/site/blog/llm-hallucination/)]

Therefore, while these strategies are computationally rational *given certain constraints and for certain goals*, they are not universally optimal or without peril. Recognizing their dual nature—as both efficient adaptations and potential sources of systematic error—is vital for understanding both human fallibility and the challenges in developing truly intelligent and reliable AI.

## Conclusion: The Convergent Evolution of Approximate Reasoning

The exploration of these ten approximate reasoning strategies reveals a compelling pattern: both human cognition and, increasingly, advanced AI like Large Language Models, seem to converge on similar solutions when faced with the fundamental challenges of operating with incomplete information and finite computational resources. These strategies—chunking, generative modeling, prototyping, context-dependence, availability, confirmation, satisficing, pattern completion, attribute substitution, and even heuristic shortcuts resembling logical fallacies—all prioritize computational efficiency, generalization, and resource optimization, often at the cost of perfect, case-specific accuracy.

This perspective offers several critical implications:

1.  **Reframing "Biases" and "Errors":** Many cognitive biases and LLM "hallucinations" or errors can be understood not merely as flaws, but as byproducts of adaptive, computationally rational strategies.[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)][[3](https://www.erichorvitz.com/computational_rationality.pdf)][[4](http://www.keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich.Sternberg2003.pdf)][[9](https://www.i-jmr.org/2025/1/e59823)][[19](https://arxiv.org/html/2402.01769v1)] This doesn't excuse harmful outcomes but provides a deeper understanding of their origins.
2.  **Context-Dependent Rationality:** A reasoning strategy that appears irrational or flawed in a decontextualized laboratory setting or benchmark might be highly effective and rational in the complex, noisy, real-world environments for which it evolved or was trained.
3.  **Guidance for Artificial Intelligence Design:** Instead of solely pursuing perfect logical reasoning (which is often intractable), AI systems designed for real-world interaction might benefit from explicitly incorporating or learning these kinds of resource-bounded, approximate reasoning mechanisms. Understanding their trade-offs is key to building more robust and adaptable AI. Some "emergent abilities" in LLMs might indeed be the result of the models implicitly learning such computationally efficient strategies.[[11](https://www.assemblyai.com/blog/emergent-abilities-of-large-language-models)][[12](https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/)][[13](https://aclanthology.org/2024.acl-long.279/)][[43](https://openreview.net/pdf?id=yzkSU5zdwD)]
4.  **Human-AI Interaction and Cognitive Offloading:** As we increasingly rely on AI systems that exhibit these approximate reasoning patterns, understanding their inherent cognitive shortcuts becomes crucial for effective collaboration and for mitigating risks associated with over-reliance or misinterpretation of AI outputs.[[42](https://www.itschiara.me/ai-human-collaboration)][[44](https://artificialityinstitute.org/how-ai-affects-critical-thinking-and-cognitive-offloading/)]
5.  **Educational and Mitigation Strategies:** Rather than attempting to eliminate these cognitive shortcuts entirely (which may be impossible or even counterproductive), efforts could focus on metacognitive awareness: teaching humans (and perhaps instilling in AI) when specific approximate strategies are appropriate, when they are likely to lead to harmful errors, and when more rigorous, effortful processing is required.

In a universe of bounded resources and pervasive uncertainty, perfect, exhaustive reasoning is a computationally expensive luxury, often an impossibility. The true art of intelligence, whether biological or artificial, lies in the sophisticated ability to make the *right* approximations—to know which corners to cut, which details to abstract, and which heuristics to trust, given the specific task, context, and available resources.

## References


### LLM References

*   Papers on LLM attention mechanisms, chunking, and context windows (e.g.,[[14](https://nebius.com/blog/posts/context-window-in-ai)],[[15](https://bdtechtalks.com/2025/02/05/the-context-window-problem-or-why-llm-forgets-the-middle-of-a-long-file/)],[[16](https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot)],[[5](https://arxiv.org/abs/2412.04757)],[[6](https://dev.to/foxgem/overview-infiniretri-enhancing-llms-for-infinite-length-context-via-attention-based-retrieval-21ib)],[[17](https://nlpnest.com/unlocking-the-context-window-in-llms/)],[[8](https://adasci.org/long-context-comprehension-with-dual-chunk-attention-dca-in-llms/)],[[45](https://www.promptlayer.com/research-papers/unlocking-faster-ai-star-attention-for-llms)],[[46](https://datasciencedojo.com/blog/the-llm-context-window-paradox/)],[[7](https://openreview.net/forum?id=9k27IITeAZ)])
*   Research on LLMs as generative models, world models, and their training data influence (e.g.,[[9](https://www.i-jmr.org/2025/1/e59823)],[[11](https://www.assemblyai.com/blog/emergent-abilities-of-large-language-models)],[[12](https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/)],[[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)],[[21](https://www.comet.com/site/blog/llm-hallucination/)])
*   Studies on word embeddings, few-shot learning, and in-context learning in LLMs (e.g.,[[13](https://aclanthology.org/2024.acl-long.279/)])
*   Analyses of LLM hallucinations, confabulation, and factuality (e.g.,[[19](https://arxiv.org/html/2402.01769v1)],[[23](https://pmc.ncbi.nlm.nih.gov/articles/PMC10619792/)],[[24](https://community.openai.com/t/hallucination-vs-confabulation/172639)],[[36](https://learnprompting.org/docs/basics/pitfalls)],[[9](https://www.i-jmr.org/2025/1/e59823)],[[25](https://www.integrative-psych.org/resources/confabulation-not-hallucination-ai-errors)],[[28](https://arxiv.org/html/2503.16515v1)],[[26](https://www.researchgate.net/publication/375206401_Hallucination_or_Confabulation_Neuroanatomy_as_metaphor_in_Large_Language_Models)],[[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)],[[21](https://www.comet.com/site/blog/llm-hallucination/)])
*   Work on LLM biases (confirmation, availability, etc.) and their reflection of training data (e.g.,[[19](https://arxiv.org/html/2402.01769v1)],[[20](https://shs.cairn.info/journal-of-innovation-economics-2024-2-page-223?lang=en)],[[36](https://learnprompting.org/docs/basics/pitfalls)],[[41](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)],[[30](https://www.flyrank.com/id/blogs/berita-ai/study-reveals-chatgpt-s-cognitive-shortcuts-and-biases-questioning-ai-s-trustworthiness-in-critical-decisions)],[[22](https://arxiv.org/abs/2412.04629)],[[21](https://www.comet.com/site/blog/llm-hallucination/)])
*   Discussions on LLM decoding strategies (top-k, nucleus sampling)
*   Research into LLM reasoning capabilities and limitations, including logical fallacies (e.g.,[[33](https://arxiv.org/abs/2410.05229)],[[34](https://www.mobihealthnews.com/news/apple-study-highlights-limitations-llms)],[[35](https://www.computing.co.uk/news/2024/ai/researchers-find-flaws-llm-reasoning)],[[31](https://zilliz.com/blog/how-to-detect-and-correct-logical-fallacies-from-genai-models)],[[36](https://learnprompting.org/docs/basics/pitfalls)],[[37](https://kili-technology.com/large-language-models-llms/llm-reasoning-guide)],[[28](https://arxiv.org/html/2503.16515v1)],[[38](https://openreview.net/forum?id=mfTM4UdYnC)],[[47](http://www.bistrochat.com/foodforthought/en/posts/seo-optimization-for-llm-restaurants.html)],[[18](https://arxiv.org/html/2501.11709v3)],[[32](https://aclanthology.org/2025.naacl-long.374.pdf)],[[39](https://openreview.net/pdf/810efa50e83dbf741cb856f5b356071b769afb49.pdf)],[[40](https://aclanthology.org/2024.emnlp-main.794.pdf)])
*   Papers on computational rationality and cognitive biases (e.g.,[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)],[[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)],[[20](https://shs.cairn.info/journal-of-innovation-economics-2024-2-page-223?lang=en)],[[44](https://artificialityinstitute.org/how-ai-affects-critical-thinking-and-cognitive-offloading/)],[[42](https://www.itschiara.me/ai-human-collaboration)],[[41](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)],[[30](https://www.flyrank.com/id/blogs/berita-ai/study-reveals-chatgpt-s-cognitive-shortcuts-and-biases-questioning-ai-s-trustworthiness-in-critical-decisions)],[[3](https://www.erichorvitz.com/computational_rationality.pdf)],[[4](http://www.keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich.Sternberg2003.pdf)],[[48](https://agentmodels.org/chapters/5-biases-intro.html)])
*   Research on emergent abilities in LLMs (e.g.,[[43](https://openreview.net/pdf?id=yzkSU5zdwD)],[[49](https://proceedings.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf)],[[11](https://www.assemblyai.com/blog/emergent-abilities-of-large-language-models)],[[12](https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/)],[[13](https://aclanthology.org/2024.acl-long.279/)])


### Psychology references

[^1]: Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97.
[^2]: Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology, 4*(1), 55–81.
[^3]: Bartlett, F.C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press.
[^4]: Schank, R. C., & Abelson, R. P. (1977). *Scripts, plans, goals, and understanding: An inquiry into human knowledge structures*. Lawrence Erlbaum.
[^5]: Rosch, E. (1975). Cognitive representations of semantic categories. *Journal of Experimental Psychology: General, 104*(3), 192–233.
[^6]: Lakoff, G. (1987). *Women, Fire, and Dangerous Things: What Categories Reveal about the Mind*. University of Chicago Press.
[^7]: Festinger, L. (1957). *A Theory of Cognitive Dissonance*. Stanford University Press.
[^8]: Legare, C. H., & Visala, A. (2011). Between religion and science: Integrating psychological and philosophical accounts of explanatory coexistence. *Human Development, 54*(3), 169-184.
[^9]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology, 5*(2), 207–232.
[^10]: Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology, 2*(2), 175–220.
[^11]: Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review, 63*(2), 129–138.
[^12]: Loftus, E. F. (2005). Planting misinformation in the human mind: A 30-year investigation of the malleability of memory. *Learning & Memory, 12*(4), 361–366.
[^13]: Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In T. Gilovich, D. Griffin, & D. Kahneman (Eds.), *Heuristics and biases: The psychology of intuitive judgment* (pp. 49–81). Cambridge University Press.
[^14]: Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124–1131.
