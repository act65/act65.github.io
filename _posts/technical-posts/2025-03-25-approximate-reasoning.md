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

**Chunking** is a cognitive process where individual pieces of information are bound together into a meaningful whole[^1]. In reasoning, this manifests as compressing multi-step logical chains (paths in $G_a$) into direct associations or treating frequently co-occurring subgraphs as single conceptual units.

[^1]: Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97. This seminal paper established that human working memory is limited to approximately seven items, driving the need for chunking strategies.

### Real-World Examples

1.  **Chess expertise**: Grandmasters recognize board patterns (subgraphs of piece configurations) and make moves without calculating every possible sequence, while novices must analyze each step methodically[^2].
2.  **Remembering a phone number**: Instead of memorising the 10 digit sequence; 0,2,3,4,5,2,2,2,9,7,5 we might chunk it into 0, 2345, 22, 975. Requiring us to remember only 4 items (nodes).
3.  **Medical diagnosis**: An experienced doctor might recognize a *syndrome* (a "chunk" of co-occurring symptoms and signs, e.g., fever, cough, fatigue as "flu-like illness") which directly suggests a diagnostic path or treatment, rather than analyzing the causal pathway of each symptom from first principles every time.

[^2]: Chase, W. G., & Simon, H. A. (1973). Perception in chess. Cognitive Psychology, 4(1), 55–81. This research demonstrated that chess experts chunk board positions into meaningful patterns, allowing rapid recognition rather than piece-by-piece analysis.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function findDetailedConnection(start_node V_s, end_node V_e, graph G_a):
    # Performs a breadth-first search (or similar) on G_a
    queue = [(V_s, [V_s])] # (current_node, path_so_far)
    visited = {V_s}
    while queue:
        current_node, path = queue.pop(0)
        if current_node == V_e:
            return path # Returns the full, detailed path
        for neighbor_node, relationship_edge in G_a.get_neighbors(current_node):
            if neighbor_node not in visited:
                visited.add(neighbor_node)
                queue.append((neighbor_node, path + [neighbor_node]))
    return "No connection found"
```
This algorithm guarantees finding the shortest path in $G_a$ if one exists, but requires storing and processing potentially many intermediate states (nodes and paths).

#### The Chunked Algorithm:

```python
# Assumes G_a has been pre-processed or dynamically recognizes "chunks"
# A chunk G_c is a frequently co-occurring subgraph, or a pre-defined multi-step path.
# These chunks can be represented as "super-nodes" or "super-edges" in a compressed graph G_compressed.

function findChunkedConnection(start_node V_s, end_node V_e, graph G_a, compressed_graph_view G_compressed):
    # Attempt to find a path using high-level chunks in G_compressed
    chunk_path = findPathInCompressedGraph(V_s, V_e, G_compressed)
    if chunk_path:
        # The chunk_path is a sequence of chunks; can be expanded if details are needed
        return chunk_path # Returns a path of "super-edges" or chunk identifiers
    else:
        # Fall back to a more detailed, but possibly depth-limited, search in G_a
        return findDetailedConnection(V_s, V_e, G_a, depth_limit=SMALL_DEPTH)
```
The `findPathInCompressedGraph` operates on a smaller graph where common multi-step paths in $G_a$ are represented as single edges, making pathfinding much faster for common queries.

### LLM Analogues and Behaviors

Large Language Models exhibit behaviors analogous to chunking:
*   **Learned Phrases & N-grams:** LLMs inherently learn common sequences of tokens (words or sub-words) that frequently appear together. These function like pre-compiled "chunks" (multi-token units) that can be generated rapidly.
*   **Attention Mechanisms:** Transformer attention can dynamically create "high-level linkages" by directly connecting distant but relevant tokens in an input sequence to generate an output, effectively bypassing intermediate reasoning steps. Some research explicitly analyzes attention patterns as reflecting a chunking mechanism for input context.[[5](https://arxiv.org/abs/2412.04757)][[6](https://dev.to/foxgem/overview-infiniretri-enhancing-llms-for-infinite-length-context-via-attention-based-retrieval-21ib)]
*   **Efficient Attention on KV Cache:** Techniques like ChunkAttention optimize LLM inference by sharing and batching computations for common prompt prefixes, essentially treating these shared prefixes as pre-processed chunks.[[7](https://openreview.net/forum?id=9k27IITeAZ)] Approaches like Dual Chunk Attention (DCA) further optimize attention by processing data in chunks, managing computational resources efficiently for long contexts.[[8](https://adasci.org/long-context-comprehension-with-dual-chunk-attention-dca-in-llms/)]

### Computational Rationality

The chunking strategy is computationally rational under constraints because:

1.  **Memory efficiency**: Storing compressed chunks (or learned weights that represent them as super-edges in $G_{compressed}$) requires significantly less memory than all possible detailed pathways in $G_a$.
2.  **Time efficiency**: Chunk-based reasoning approaches much faster inference for common pathways compared to exhaustive search-based reasoning in $G_a$.
3.  **Error profile**: Errors typically occur when exceptions to the chunked rule exist, an acceptable trade-off if these exceptions are rare or the cost of the error is low compared to the efficiency gain.

This creates a power-law efficiency: Frequently used reasoning patterns become extremely efficient at the cost of potentially missing edge cases—exactly the pattern we see in human expertise development and increasingly in optimized LLM behaviors.

## Strategy 2: Generative Models of Relationships (Factoring Links)

### The Psychological Phenomenon

**Schema-based reasoning** involves using abstract knowledge structures (schemas, which can be thought of as templates for subgraphs in $G_a$) to generate expectations and inferences about new situations without storing every possible relationship[^3]. This manifests psychologically as our ability to make reasonable guesses about novel situations based on their similarity to familiar categories.

[^3]: Bartlett, F.C. (1932). Remembering: A Study in Experimental and Social Psychology. Cambridge University Press. This classic work introduced the concept of schemas as dynamic knowledge structures that guide perception and memory.

### Real-World Examples

1.  **Restaurant scripts**: When entering a new restaurant (a new node $V_{new\_restaurant}$), we automatically know to wait to be seated, expect a menu, etc.—without having to memorize the procedure (a sequence of edges and nodes) for each specific establishment[^4]. We apply a "restaurant schema" $G_{schema\_restaurant}$.
2.  **Technological interfaces**: We can navigate new smartphone apps using general interface schemas without reading instructions for each one.
3.  **Social relationships**: We apply relationship models (friend, colleague, authority figure – types of edges $E_{relationship}$) to new acquaintances that generate appropriate behavioral expectations.

[^4]: Schank, R. C., & Abelson, R. P. (1977). Scripts, plans, goals, and understanding: An inquiry into human knowledge structures. Lawrence Erlbaum. This work formalized how people use schematic knowledge structures ("scripts") to navigate common social situations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function determineRelationship(node_A V_A, node_B V_B, complete_graph G_p):
    # Assumes G_p contains all true relationships
    relationship_edge = G_p.get_edge_between(V_A, V_B)
    if relationship_edge:
        return relationship_edge.type, relationship_edge.strength
    else:
        return "No direct relationship stored"
```
This approach requires storing an explicit relationship (an edge $E$) between every pair of concepts (nodes $V$) in $G_p$ for which a relationship exists—potentially $O(|V_p|^2)$ space in the worst case.

#### The Generative Algorithm:

```python
# relationshipModel is a learned function, e.g., a neural network
function generateRelationship(node_A V_A, node_B V_B, relationshipModel, active_graph G_a):
    features_A = G_a.get_node_features(V_A)
    features_B = G_a.get_node_features(V_B)
    # The model predicts the likely relationship (type, strength) based on node features
    predicted_relationship_type, predicted_strength = relationshipModel(features_A, features_B)
    return predicted_relationship_type, predicted_strength
```
This approach uses a parameterized model that generates likely relationships based on concept features (properties of nodes in $G_a$) rather than storing each relationship explicitly.

### LLM Analogues and Behaviors

LLMs are inherently generative models that learn statistical relationships:
*   **Core Functionality:** LLMs learn the statistical patterns of how tokens (representing concepts or parts of concepts, i.e., nodes $V$) relate to each other from vast datasets. They don't store every explicit fact (edge $E$) but generate responses based on these learned "schemas" of language and conceptual relationships. Their ability to predict the next token is a form of generating relationships.[[9](https://www.i-jmr.org/2025/1/e59823)][[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)]
*   **Analogy and Metaphor Generation:** LLMs can create novel analogies (identifying similar relational structures between different sets of nodes) and explain concepts in various ways, suggesting they've captured underlying relational structures rather than just memorizing instances.
*   **Emergent "World Models":** There's ongoing research into whether LLMs develop implicit "world models"—internal representations of how entities (nodes $V$) and concepts relate in the world—which guide their generation of coherent and contextually appropriate text (sequences of related nodes).[[11](https://www.assemblyai.com/blog/emergent-abilities-of-large-language-models)][[12](https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/)]

### Computational Rationality

The generative model strategy is computationally rational under constraints because:

1.  **Memory efficiency**: Storing a parametric model with $k$ parameters where $k \ll |V_p|^2$ drastically reduces memory requirements compared to storing all edges in $G_p$.
2.  **Generalization**: The model can generate reasonable relationship hypotheses for entirely new concepts (nodes $V_{new}$) or pairs of concepts not explicitly seen.
3.  **Update efficiency**: New information can update the general model rather than requiring updates to many individual relationships (edges $E$).
4.  **Graceful degradation**: When exact relationships aren't known, the system still produces plausible approximations.

The trade-off is reduced precision for specific cases that deviate from general patterns, which is optimal when most relationships follow regular patterns and resources are insufficient to memorize all exceptions.

## Strategy 3: Prototype-Based Representation (Sketched Nodes)

### The Psychological Phenomenon

**Prototype theory** proposes that humans categorize objects by comparing them to abstract prototypes (representative nodes $V_{prototype}$ in $G_a$) that represent the central tendency of the category, rather than through strict definitional boundaries[^5]. This allows efficient representation of complex categories using only a few exemplars.

[^5]: Rosch, E. (1975). Cognitive representations of semantic categories. Journal of Experimental Psychology: General, 104(3), 192–233. This research demonstrated that people judge category membership by similarity to prototypes rather than by necessary and sufficient conditions.

### Real-World Examples

1.  **Bird recognition**: We recognize birds by their similarity to prototypical birds (like robins, $V_{robin\_prototype}$) rather than checking a list of necessary and sufficient conditions (a complex set of features for each $V_{bird}$), which explains why penguins and ostriches are psychologically "less bird-like"[^6].
2.  **Facial recognition**: We identify faces by comparing them to abstracted prototypes rather than memorizing every possible face.
3.  **Concept learning**: Children learn concepts like "chair" by exposure to examples and abstraction of common features (forming a $V_{chair\_prototype}$), not by memorizing definitions for every $V_{chair\_instance}$.

[^6]: Lakoff, G. (1987). Women, Fire, and Dangerous Things: What Categories Reveal about the Mind. University of Chicago Press. This work explored how prototypes and radial categories structure human conceptual systems.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function representAllConceptsExhaustively(domain_data_stream, full_knowledge_graph G_p):
    # For each distinct entity encountered in the domain
    for entity_data in domain_data_stream:
        V_entity = create_node_from_data(entity_data) # Node with complete feature vector
        G_p.add_node(V_entity)
    # To recognize a concept, one would search G_p for an exact match or apply complex rules.
```
This approach stores every concept (node $V$) as a separate entity with its full feature representation in $G_p$, requiring $O(|V_p| \times f)$ space where $f$ is the average number of features per concept.

#### The Prototype Algorithm:

```python
# Assumes G_a stores prototypes and transformation rules/functions.
function representWithPrototypes(training_data_nodes V_training, active_graph G_a):
    clusters = findClusters(V_training) # Cluster nodes based on feature similarity
    G_a.prototypes = {}
    for cluster_id, nodes_in_cluster in clusters.items():
        V_prototype = computeCentralTendencyNode(nodes_in_cluster) # e.g., average feature vector
        G_a.prototypes[cluster_id] = V_prototype
    # Recognition involves finding the nearest prototype and applying a transformation
    # function recognizeConcept(entity_node V_entity, active_graph G_a):
    #     nearest_proto_id, similarity = findNearestPrototype(V_entity, G_a.prototypes)
    #     V_recognized_as_prototype = G_a.prototypes[nearest_proto_id]
    #     transformation = learnTransformation(V_entity, V_recognized_as_prototype)
    #     return V_recognized_as_prototype, transformation
```
This approach stores only cluster prototypes (a smaller set of nodes $V_{prototype}$ in $G_a$) plus transformation rules, reducing storage requirements significantly.

### LLM Analogues and Behaviors

LLMs utilize representations that share characteristics with prototype theory:
*   **Embeddings:** Word and sentence embeddings in LLMs represent concepts as vectors (features of nodes $V$) in a high-dimensional space. Concepts with similar meanings are clustered together, with the "center" of such a cluster in $G_a$'s embedding space acting like a prototype. The model can then reason about new words or phrases based on their proximity to these learned prototypes.
*   **Few-Shot Learning / In-Context Learning:** When an LLM learns a new task from a few examples provided in the prompt (few-shot or in-context learning), it's essentially abstracting a "prototype" of the task or concept (a temporary $V_{task\_prototype}$ in its active context $G_a$) from those examples.[[13](https://aclanthology.org/2024.acl-long.279/)] It then applies this abstracted prototype to new, unseen instances.

### Computational Rationality

The prototype strategy is computationally rational under constraints because:

1.  **Memory efficiency**: Storing $k$ prototypes (or the parameters that define the embedding space for $G_a$) where $k \ll |V_p|$ reduces memory requirements.
2.  **Generalization capacity**: Novel entities (new nodes $V_{new}$) can be understood or represented as transformations of or combinations of existing prototypes (vectors in $G_a$).
3.  **Retrieval efficiency**: Similarity-based retrieval in embedding space allows for fast approximate matching of nodes in $G_a$.
4.  **Graceful degradation**: Even with limited information, the system can approximate concepts by their nearest prototype in $G_a$.

The trade-off is category boundary fuzziness and typicality effects, which are acceptable when exact boundaries are rarely needed and resources are insufficient to store every instance.

## Strategy 4: Context-Dependent Inconsistency Tolerance

### The Psychological Phenomenon

**Belief compartmentalization** refers to the human tendency to hold contradictory beliefs simultaneously by segregating them into different contexts or domains[^7]. Rather than maintaining global consistency across the entire knowledge base $G_p$, we allow local inconsistencies within specific active subgraphs $G_a$ (or $G_{context} \subset G_a$) when they serve practical purposes.

[^7]: Festinger, L. (1957). A Theory of Cognitive Dissonance. Stanford University Press. This influential work explored how people manage contradictory beliefs, often through compartmentalization to reduce cognitive dissonance.

### Real-World Examples

1.  **Religious and scientific beliefs**: Many scientists maintain religious beliefs that would appear to contradict their scientific understanding (e.g., $V_{creation}$ vs $V_{evolution}$), activating different belief subgraphs $G_{religious\_context}$ vs $G_{scientific\_context}$ in different situations[^8].
2.  **Health behaviors**: People often maintain inconsistent beliefs about health risks, such as knowing smoking causes cancer (edge: $V_{smoking} \rightarrow V_{cancer}$) while believing "it won't happen to me" (a conflicting property on $V_{self}$).
3.  **Professional vs. personal ethics**: People may apply different ethical standards (different sets of rule-nodes or edge-weights in $G_a$) in business contexts than in personal relationships.

[^8]: Legare, C. H., & Visala, A. (2011). Between religion and science: Integrating psychological and philosophical accounts of explanatory coexistence. Human Development, 54(3), 169-184. This research examines how people integrate seemingly incompatible religious and scientific explanations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function maintainGlobalConsistency(graph G_p, new_fact_node_or_edge F_new):
    # Check if F_new (e.g., an edge (V1, 'is', V2) or (V1, 'is_not', V2))
    # creates a logical contradiction with any existing information in G_p.
    # A contradiction could be:
    # 1. Direct: G_p contains (X, 'is', Y) and F_new is (X, 'is_not', Y).
    # 2. Indirect: G_p implies P, and G_p + F_new implies NOT P.
    if creates_contradiction(F_new, G_p):
        # Resolution is complex:
        # - Reject F_new
        # - Remove contradicting facts/edges from G_p
        # - Create complex exception rules (new nodes/edges modifying existing ones)
        # - Restructure knowledge hierarchy in G_p
        resolve_contradiction_globally(F_new, G_p) # Computationally very expensive
    else:
        G_p.add(F_new)
    return G_p
```
This approach ensures global consistency across $G_p$ but requires expensive contradiction detection and resolution operations that scale with the size of $G_p$.

#### The Compartmentalization Algorithm:

```python
# G_a is the active knowledge graph, G_contexts is a collection of subgraphs for different contexts.
function contextualUpdate(new_fact F_new, context_label C_label, graph G_a, dict_of_contexts G_contexts):
    if C_label not in G_contexts:
        G_contexts[C_label] = create_empty_subgraph_of(G_a) # Or initialize from a template
    
    current_context_graph G_c = G_contexts[C_label]
    
    # Consistency check is limited to the current context G_c
    if creates_contradiction_locally(F_new, G_c):
        resolve_contradiction_locally(F_new, G_c) # Simpler, localized resolution
    else:
        G_c.add(F_new)
        # Optionally, propagate some information to G_a if needed, carefully.
    
    # Retrieval is also context-dependent
    # function retrieveFact(query Q, context_label C_label, G_contexts):
    #     if C_label in G_contexts:
    #         return G_contexts[C_label].execute_query(Q)
    #     return G_a.execute_query(Q) # Fallback to general active graph
```
This approach stores/activates knowledge in context-specific subgraphs $G_c \subset G_a$, only checking for consistency within $G_c$.

### LLM Analogues and Behaviors

LLMs exhibit behaviors that mirror context-dependent inconsistency:
*   **Context Window Limitations:** LLMs operate with a finite "context window"—their $G_a$ is limited to a certain amount of recent text.[[14](https://nebius.com/blog/posts/context-window-in-ai)][[15](https://bdtechtalks.com/2025/02/05/the-context-window-problem-or-why-llm-forgets-the-middle-of-a-long-file/)] Information (nodes/edges) outside this window is effectively "forgotten" or inaccessible, which can lead to inconsistencies if a long conversation refers back to points that are no longer in the active $G_a$. This is analogous to human compartmentalization, where only the current "active context" $G_a$ is fully coherent.[[16](https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot)]
*   **Prompt Sensitivity:** The same LLM can provide different or even contradictory answers (generate conflicting subgraphs) to semantically similar questions if they are phrased differently or if the preceding context in the prompt (the initial state of $G_a$) changes.[[18](https://arxiv.org/html/2501.11709v3)] This suggests that their "knowledge" is not globally consistent but is activated and shaped by the immediate input context $G_a$.

### Computational Rationality

The compartmentalization strategy is computationally rational under constraints because:

1.  **Computational efficiency**: Consistency checking is limited to relevant subgraphs $G_c$ of $G_a$ rather than the entire (potentially vast) $G_p$.
2.  **Practical accuracy**: Domain-specific approximations within a $G_c$ can be more accurate within their domains than general rules that must account for all cases in $G_p$.
3.  **Learning efficiency**: New information (nodes/edges) can be incorporated into a $G_c$ without expensive global restructuring of $G_p$.
4.  **Adaptability**: Different contexts $G_c$ can maintain specialized knowledge representations optimized for their domain.

The trade-off is potential contradictions when contexts overlap or when information from outside the immediate $G_a$ (or active $G_c$) is crucial. This is acceptable when most reasoning occurs within specific contexts and the computational cost of maintaining global consistency is prohibitive.[[14](https://nebius.com/blog/posts/context-window-in-ai)]

## Strategy 5: Recency and Availability Heuristics

### The Psychological Phenomenon

The **availability heuristic** causes people to judge the likelihood of events based on how easily examples (nodes $V$ or subgraphs $G_{event}$ in $G_a$) come to mind[^9]. Related to this, the **recency effect** gives disproportionate weight to recently encountered information (nodes/edges recently added to or activated in $G_a$). Together, these cognitive shortcuts prioritize information that is likely to be relevant in the current temporal and spatial context.

[^9]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology, 5(2), 207–232. This paper introduced the availability heuristic as a mental shortcut that relies on immediate examples that come to mind.

### Real-World Examples

1.  **Risk assessment**: People overestimate the likelihood of plane crashes (node $V_{plane\_crash}$) after media coverage of an accident (increasing its salience/activation in $G_a$), while underestimating more common but less publicized risks like heart disease.
2.  **Stock market decisions**: Investors give more weight to recent market performance (recently activated nodes/edges in $G_a$ related to market trends) than long-term trends (less active parts of $G_p$).
3.  **Consumer choices**: Purchase decisions are heavily influenced by recently viewed advertisements or recommendations (priming specific nodes in $G_a$).

### The Computational Strategy

#### The Expensive "Correct" Algorithm (Ideal Frequency Assessment):

```python
function assessTrueFrequency(event_type_descriptor ETD, complete_historical_graph G_historical_star):
    # G_historical_star is an idealized, complete log of all past events and contexts.
    # ETD describes the properties of nodes/subgraphs that constitute the event.
    
    count_occurrences = 0
    count_total_opportunities = 0 # The truly intractable part
    
    for potential_event_subgraph G_sub in G_historical_star: # Iterate all relevant parts
        if G_sub.matches_descriptor(ETD):
            count_occurrences += 1
        if G_sub.represents_opportunity_for(ETD): # e.g. for "plane crash", an opportunity is "a flight"
            count_total_opportunities += 1
            
    if count_total_opportunities == 0: return 0
    return count_occurrences / count_total_opportunities
```
This approach requires maintaining complete historical statistics ($G_{historical\_star}$) and computing true frequencies, which is memory and computation intensive. *Note: Defining and counting all "total possible scenarios" or "opportunities" is often intractable or ill-defined in complex real-world environments.*

#### The Availability/Recency Algorithm:

```python
function estimateProbabilityByAvailability(event_type_descriptor ETD, active_graph G_a, current_time T_now):
    # Estimates probability based on ease of retrieving/activating instances in G_a.
    # Nodes in G_a have properties like 'timestamp_added', 'activation_level'.
    
    availability_score = 0
    for node V_instance in G_a.get_nodes_matching_type(ETD.type):
        # Factors contributing to salience/availability:
        recency = 1.0 / (T_now - V_instance.properties.get('timestamp_activated', T_now - LARGE_INTERVAL) + 1.0)
        current_activation = V_instance.properties.get('activation_level', 0.0) # e.g., from priming
        vividness_strength = V_instance.properties.get('vividness', 1.0) # e.g., emotional tag
        
        # Combine factors to get a salience score for this instance
        instance_salience = recency * current_activation * vividness_strength
        availability_score += instance_salience
        
    # Normalize or scale if needed, but this score is a proxy, not a true probability.
    return availability_score 
```
This approach estimates likelihood based on the weighted sum of salience of matching instances currently active or easily retrievable in $G_a$.

### LLM Analogues and Behaviors

LLMs demonstrate behaviors consistent with recency and availability:
*   **Recency Bias in Prompts:** Information (nodes/edges) presented later in an LLM's prompt (current $G_a$) often has a disproportionately strong influence on its output.[[19](https://arxiv.org/html/2402.01769v1)] This is a well-documented phenomenon where the "most available" recent input tokens heavily guide generation.
*   **Influence of Training Data Frequency (Availability):** Concepts, facts, styles, and even biases that are more frequent in the LLM's training data ($G_p$ from which $G_a$ is sampled/weighted) are more "available" to the model and thus more likely to be reproduced in its outputs, irrespective of their objective truth or nuanced importance.[[19](https://arxiv.org/html/2402.01769v1)][[20](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)][[21](https://www.comet.com/site/blog/llm-hallucination/)]
*   **Outputting Common/Fluent Phrases:** LLMs tend to generate common and fluent phrases (high availability from their training data, i.e., high-probability paths in $G_p$) because these represent high-probability sequences. This can sometimes come at the expense of more precise or less common, but more appropriate, phrasing.

### Computational Rationality

The availability/recency strategy is computationally rational under constraints because:

1.  **Memory efficiency**: It relies on readily accessible information (e.g., recent items in $G_a$, high-frequency patterns from $G_p$ reflected in $G_a$'s weights) rather than requiring exhaustive search or storage of complete historical statistics ($G_{historical\_star}$).
2.  **Temporal relevance**: Recent events or information in $G_a$ are often more predictive of current conditions due to environmental autocorrelation.
3.  **Computational simplicity**: It uses retrieval fluency or pattern frequency (activation levels in $G_a$) as a proxy for probability, avoiding complex calculations over $G_p$.
4.  **Attentional allocation**: Resources are directed to information in $G_a$ that is likely to be immediately relevant.

The trade-off is systematic bias when retrieval ease (e.g., due to media exposure, emotional salience, or training data imbalances reflected in $G_a$) distorts true frequencies or importance.[[19](https://arxiv.org/html/2402.01769v1)][[20](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)]

## Strategy 6: Confirmation Bias and Hypothesis Maintenance

### The Psychological Phenomenon

**Confirmation bias** is the tendency to search for, interpret, and recall information in a way that confirms existing beliefs or hypotheses (a favored subgraph $G_{hypothesis}$ within $G_a$)[^10]. While often framed as a cognitive flaw, it can be viewed as a resource-efficient strategy for maintaining stable beliefs in noisy information environments.[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)]

[^10]: Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. Review of General Psychology, 2(2), 175–220. This comprehensive review documents confirmation bias across many domains and explains its cognitive foundations.

### Real-World Examples

1.  **Political beliefs**: People selectively consume news that aligns with their political views (reinforcing a $G_{political\_hypothesis}$) and interpret ambiguous events (new nodes/edges) as supporting their position.
2.  **Scientific research**: Scientists may design experiments to confirm rather than challenge their hypotheses ($G_{scientific\_hypothesis}$) and be more critical of methodologies in studies with contrary findings.
3.  **Relationship judgments**: People tend to notice behaviors (new edges related to a person-node $V_{person}$) that confirm initial impressions ($G_{impression\_hypothesis}$) of others while overlooking contradictory evidence.

### The Computational Strategy

#### The Expensive "Correct" Algorithm (Bayesian Hypothesis Evaluation):

```python
function evaluateAllHypotheses(set_of_hypotheses H_set, new_data_evidence D_new, prior_graph G_p):
    # Each hypothesis H_i in H_set is a potential model or subgraph.
    # G_p contains prior probabilities P(H_i) and likelihoods P(D|H_i).
    
    posterior_probabilities = {}
    for H_i in H_set:
        likelihood_P_D_given_Hi = G_p.calculate_likelihood(D_new, H_i)
        prior_P_Hi = G_p.get_prior_prob(H_i)
        evidence_P_D = sum(G_p.calculate_likelihood(D_new, H_j) * G_p.get_prior_prob(H_j) for H_j in H_set) # Normalization
        
        if evidence_P_D == 0: posterior_probabilities[H_i] = 0
        else: posterior_probabilities[H_i] = (likelihood_P_D_given_Hi * prior_P_Hi) / evidence_P_D
            
    return H_i_with_max_posterior_prob(posterior_probabilities)
```
This approach requires maintaining and evaluating all possible alternative hypotheses (potentially many complex subgraphs) against $G_p$, which is computationally expensive.

#### The Confirmation-Biased Algorithm:

```python
function maintainHypothesis(current_hypothesis_graph G_hyp, new_data_node_or_edge D_new, active_graph G_a):
    # G_hyp is the currently favored subgraph/model within G_a.
    # Confidence in G_hyp is an attribute of G_hyp itself.
    
    if is_consistent_with_and_supports(D_new, G_hyp, G_a):
        G_hyp.increase_confidence_score()
        G_hyp.integrate_data(D_new) # Strengthens G_hyp
    elif weakly_contradicts(D_new, G_hyp, G_a):
        # Discount D_new, reinterpret it to fit G_hyp, or slightly lower G_hyp confidence
        G_hyp.assign_lower_weight_to_contradiction(D_new)
    elif strongly_contradicts(D_new, G_hyp, G_a) and G_hyp.confidence_score < THRESHOLD_FOR_REVISION:
        # Only consider revising G_hyp if contradiction is strong and confidence isn't too high
        # This might trigger a search for alternative hypotheses, but with a high bar.
        consider_alternative_hypotheses(D_new, G_a) 
    return G_hyp # G_hyp is largely maintained
```
This approach maintains the current hypothesis $G_{hyp}$ in $G_a$ unless strongly contradicted, focusing computational resources on interpretation consistent with $G_{hyp}$ rather than complete re-evaluation.

### LLM Analogues and Behaviors

LLMs can exhibit behaviors that resemble confirmation bias:
*   **Reinforcement of Initial Output Stream:** Once an LLM begins generating text along a particular "hypothesis" or narrative thread (often seeded by the initial prompt, forming an initial $G_a$), it tends to produce subsequent tokens that are consistent with that path. This can lead to plausible-sounding but factually incorrect "hallucinations" if the initial direction (initial $G_a$) was flawed, as the model "confirms" its own ongoing generation.[[9](https://www.i-jmr.org/2025/1/e59823)][[19](https://arxiv.org/html/2402.01769v1)]
*   **Influence of Prompt Framing:** If a user's prompt suggests a certain belief or frames a question in a biased way (pre-populating $G_a$ with a biased hypothesis), the LLM may be more likely to generate a response that "confirms" that implicit bias, rather than challenging it or offering neutral information.[[19](https://arxiv.org/html/2402.01769v1)][[22](https://arxiv.org/abs/2412.04629)]
*   **Reinforcement Learning from Human Feedback (RLHF):** While RLHF aims to align LLMs with human preferences, if human raters exhibit confirmation biases when evaluating responses (e.g., preferring answers that align with their own $G_{hypothesis}$), the LLM can inadvertently be trained to perpetuate those biases in its $G_p$ (weights).[[19](https://arxiv.org/html/2402.01769v1)]
*   **Agentic Confirmation (Speculative):** Future LLM-powered agents that learn from interaction might preferentially seek or upweight information sources that confirm their existing world model (their current $G_a$ or learned $G_p$ components) to maintain stability, especially if exploration is costly.

### Computational Rationality

The confirmation bias strategy is computationally rational under constraints because:

1.  **Computational efficiency**: Evaluating a single (or few) prevailing hypothesis $G_{hyp}$ in $G_a$ against new data is less costly than constantly re-evaluating all possible hypotheses from $G_p$.
2.  **Learning stability**: It prevents rapid belief oscillation in noisy environments where contradictory evidence might be spurious or misleading, keeping $G_a$ relatively stable.
3.  **Resource allocation**: It focuses cognitive resources on refining and elaborating the current best model $G_{hyp}$ of the world rather than constantly searching for entirely new models.
4.  **Search efficiency**: It directs information seeking toward data that is most likely to be relevant to the current $G_{hyp}$.

The trade-off is resistance to belief updating, especially when the environment changes significantly or the initial $G_{hyp}$ is deeply flawed. This is acceptable when the environment is relatively stable, the cost of erroneously changing a correct belief is high, or resources are insufficient to constantly entertain multiple complex hypotheses.

## Strategy 7: False Memory and Pattern Completion

### The Psychological Phenomenon

**False memory** refers to the phenomenon where people remember events that never occurred or remember them differently from how they occurred[^12]. This can be viewed as an adaptive pattern completion mechanism rather than simply a memory failure. The brain often fills in gaps in a recalled subgraph $G_{recalled\_event}$ with plausible information (nodes/edges) consistent with existing schemas ($G_{schema}$) stored in $G_a$.

[^12]: Loftus, E. F. (2005). Planting misinformation in the human mind: A 30-year investigation of the malleability of memory. Learning & Memory, 12(4), 361–366. This paper reviews research showing how memory reconstructs rather than reproduces past events.

### Real-World Examples

1.  **Eyewitness testimony**: Witnesses often "remember" details (add nodes/edges to their $G_{recalled\_event}$) that align with their expectations ($G_{schema}$) rather than what they actually observed.
2.  **Childhood memories**: People incorporate family stories and photographs into their "memories," believing they remember events they only heard about (constructing a $G_{reconstructed\_event}$ from fragments and external inputs).
3.  **Educational contexts**: Students often misremember information in ways that make it more coherent with their existing knowledge (modifying a $G_{learned\_concept}$ to fit better with their $G_a$).

### The Computational Strategy

#### The Expensive "Correct" Algorithm (Verbatim Recall):

```python
function verbatimRecall(event_cue C_event, perfect_event_log_graph G_log_star):
    # G_log_star is an idealized, complete, and accurate graph of all past experiences.
    # Each event is a distinct, perfectly stored subgraph G_event_i.
    
    # Search G_log_star for a subgraph that perfectly matches the cue C_event
    # and represents the full, original event.
    G_exact_event = G_log_star.find_exact_event_subgraph(C_event)
    
    if G_exact_event:
        return G_exact_event # Returns the perfectly preserved subgraph
    else:
        return "No exact memory found" 
```
This approach requires perfect, verbatim storage and retrieval of all experienced events (all subgraphs in $G_{log\_star}$), which is extremely memory intensive and inflexible.

#### The Pattern Completion / Reconstructive Algorithm:

```python
function reconstructiveRecall(event_cue C_event, active_graph G_a, schema_library S_lib):
    # G_a contains fragmented memories (partial subgraphs) and general knowledge.
    # S_lib contains prototypical event schemas (template subgraphs G_schema).
    
    # 1. Retrieve known fragments related to the cue from G_a
    retrieved_fragments_subgraph G_fragments = G_a.retrieve_relevant_fragments(C_event)
    
    # 2. Activate relevant schemas from S_lib based on cue and fragments
    activated_schema_subgraph G_schema_instance = S_lib.get_best_matching_schema(C_event, G_fragments)
    
    # 3. Combine fragments and schema, filling gaps plausibly using a generative model
    # This model might add nodes/edges to G_fragments based on G_schema_instance
    # and general consistency rules within G_a.
    G_reconstructed_event = generative_completion_model(G_fragments, G_schema_instance, G_a)
    
    return G_reconstructed_event # The reconstructed, possibly partially false, memory subgraph
```
This approach reconstructs memories by combining stored fragments from $G_a$ with schematic expectations from $S_{lib}$ and general knowledge, using a generative process to fill gaps.

### LLM Analogues and Behaviors

LLMs exhibit a striking parallel to false memory through "hallucinations" or "confabulations":
*   **Hallucinations/Confabulations:** LLMs frequently generate plausible-sounding information (new nodes/edges in their output sequence) that is not factually correct or not present in their training data ($G_p$).[[9](https://www.i-jmr.org/2025/1/e59823)][[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)][[19](https://arxiv.org/html/2402.01769v1)][[21](https://www.comet.com/site/blog/llm-hallucination/)] They "fill in the gaps" to provide a coherent-seeming response (a plausible output subgraph), much like human reconstructive memory. Some researchers argue "confabulation" is a more accurate term than "hallucination" for LLMs, as it describes producing false memories without intent to deceive, often to complete a narrative.[[23](https://pmc.ncbi.nlm.nih.gov/articles/PMC10619792/)][[24](https://community.openai.com/t/hallucination-vs-confabulation/172639)][[25](https://www.integrative-psych.org/resources/confabulation-not-hallucination-ai-errors)][[26](https://www.researchgate.net/publication/375206401_Hallucination_or_Confabulation_Neuroanatomy_as_metaphor_in_Large_Language_Models)]
*   **Over-generalization and Factual Invention:** The model might combine disparate pieces of information (nodes/edges from different parts of $G_p$) in a novel but incorrect way, creating a "false memory" of a connection or fact that doesn't exist. This is driven by their training to produce statistically probable sequences of tokens (paths in a conceptual graph), even if those sequences don't align with ground truth $G^\ast$.[[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)][[21](https://www.comet.com/site/blog/llm-hallucination/)]

### Computational Rationality

The pattern completion/reconstructive memory strategy is computationally rational under constraints because:

1.  **Storage efficiency**: Storing the "gist" or key elements (sparse subgraphs in $G_a$) and relying on generative processes to fill in details requires much less memory than storing complete episodic records ($G_{log\_star}$).
2.  **Retrieval robustness**: Pattern completion allows recall and generation from partial cues (incomplete $G_{fragments}$), making the system more fault-tolerant and flexible.
3.  **Generalization capacity**: Reconstructed "memories" or generated text often emphasize schema-consistent aspects ($G_{schema\_instance}$) that are more likely to be useful or understandable in future, similar situations.
4.  **Prediction utility**: Filled-in details often represent statistically likely truths based on the learned patterns in $G_p$ (and reflected in $G_a$'s generative capabilities), even if not specifically factual for a given instance.

The trade-off is reduced accuracy for specific details and the generation of entirely false information (incorrect nodes/edges in $G_{reconstructed\_event}$).[[9](https://www.i-jmr.org/2025/1/e59823)][[21](https://www.comet.com/site/blog/llm-hallucination/)] This is acceptable when the gist is more important than perfect detail, storage capacity is limited, and the environment (or training data $G_p$) contains strong statistical regularities that make "educated guesses" often plausible.

## Strategy 8: Question Substitution (Attribute Substitution)

### The Psychological Phenomenon

Attribute substitution occurs when people respond to a difficult question (requiring complex inference over $G_p$) by unconsciously substituting it with an easier one (answerable with simple queries on $G_a$)[^13]. Rather than engaging in computationally expensive reasoning about a complex attribute, the mind quickly assesses a related but simpler attribute.

[^13]: Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In T. Gilovich, D. Griffin, & D. Kahneman (Eds.), Heuristics and biases: The psychology of intuitive judgment (pp. 49–81). Cambridge University Press. This paper introduced the concept of attribute substitution as a general mechanism underlying many cognitive biases.

### Real-World Examples

1.  **Risk assessment:** When asked "How dangerous is this activity?" (a complex query on $V_{activity}$ involving its properties and relations in $G_p$), people often answer the easier question "How salient are negative outcomes associated with $V_{activity}$ in my current $G_a$?"
2.  **Person evaluation:** When asked "Will candidate $V_{candidate}$ be successful?" (complex query on $G_p$), interviewers often substitute "How fluent and confident was $V_{candidate}$ during the interview?" (simple query on properties of $V_{candidate}$ observed in $G_a$).
3.  **Economic forecasting:** When asked "How will $V_{market}$ perform next year?" (complex query on $G_p$), experts often answer "How has $V_{market}$ performed recently?" (query on recent trends in $G_a$).

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```python
function evaluateComplexAttribute(target_node V_target, complex_query CQ, comprehensive_graph G_p):
    # CQ defines a complex property requiring extensive inference over G_p.
    # e.g., CQ = "long-term_viability_of(V_target)"
    # This involves:
    # 1. Identifying all relevant factors (nodes, edges, subgraphs in G_p) related to V_target and CQ.
    # 2. Collecting/accessing data for these factors from G_p.
    # 3. Determining weights and causal relationships (complex edges in G_p).
    # 4. Executing a complex inference model (e.g., Bayesian network, simulation) over the relevant subgraph of G_p.
    
    relevant_subgraph_from_Gp = G_p.extract_subgraph_for_query(V_target, CQ.dependencies)
    result = execute_complex_inference_model(relevant_subgraph_from_Gp, CQ.logic_and_parameters)
    return result
```
This approach requires extensive data access from $G_p$, causal analysis, and computational resources to properly evaluate complex attributes.

#### The Substitution Algorithm:

```python
function substituteAndEvaluate(target_node V_target, complex_query CQ, active_graph G_a):
    # 1. Identify accessible attributes (properties of V_target or its immediate neighbors in G_a)
    #    that are heuristically correlated with the complex_query CQ.
    #    e.g., if CQ is "Is V_target trustworthy?", HQ might be "Does V_target have 'positive_sentiment' edges in G_a?"
    heuristic_query HQ = find_simpler_correlated_heuristic_query(CQ, V_target, G_a.available_properties_and_local_edges)
    
    # 2. Evaluate this simpler heuristic_query HQ using only readily available info in G_a.
    value_of_HQ = G_a.evaluate_simple_query(V_target, HQ)
    
    # 3. Return the result of HQ as a proxy for the result of CQ.
    return value_of_HQ 
```
This approach replaces the difficult evaluation over $G_p$ with a simpler one based on an accessible attribute or pattern in $G_a$ that is somewhat correlated with the target attribute.

### LLM Analogues and Behaviors

LLMs can exhibit behaviors analogous to attribute substitution:
*   **Answering a Simpler Version of the Question:** If a prompt is very complex, ambiguous, or requires deep reasoning beyond the LLM's current capabilities (i.e., cannot be easily resolved by traversing its weighted $G_a$), it might generate a response that addresses a related but simpler aspect of the question—one for which it has readily available high-probability paths in its $G_a$.[[28](https://arxiv.org/html/2503.16515v1)]
*   **Focusing on Keywords over Nuance:** LLMs might latch onto salient keywords (highly activated nodes $V_{keyword}$ in the prompt part of $G_a$) and generate text primarily related to those keywords, potentially missing the more nuanced intent of the overall query. This is like substituting "what is $V_{keyword}$ associated with in $G_a$?" for "what is the complex meaning of this entire query graph?"
*   **Generating Generic or Superficial Answers:** When asked for highly specific, deep, or novel analysis (a complex attribute to compute, requiring novel pathfinding in $G_p$), an LLM might provide a more generic, superficial, or common answer (a simpler, more "accessible" attribute represented by a well-trodden path in its $G_a$ derived from $G_p$). Studies show LLMs struggle with nuanced, domain-specific tasks without careful prompting or fine-tuning.[[28](https://arxiv.org/html/2503.16515v1)]

### Computational Rationality

The question substitution strategy is computationally rational under constraints because:

1.  **Computational efficiency:** Evaluating a simple attribute (e.g., keyword association in $G_a$, generating a common pattern from $G_a$) is often orders of magnitude less computationally intensive than a complex, multi-step reasoning process over $G_p$.
2.  **Data requirements:** Simple attributes typically rely on more readily available patterns in the active graph $G_a$.
3.  **Response speed:** Substitution allows for rapid responses, which is crucial when interaction speed is valued.
4.  **Heuristic value:** The substitute attribute (simple query on $G_a$) often correlates sufficiently with the complex target attribute (complex query on $G_p$) to provide an answer that is better than random chance, or at least plausible.

The trade-off is systematic bias when the substitute attribute significantly diverges from the target attribute.[[30](https://www.flyrank.com/id/blogs/berita-ai/study-reveals-chatgpt-s-cognitive-shortcuts-and-biases-questioning-ai-s-trustworthiness-in-critical-decisions)] This is acceptable when the correlation is reasonably high in common scenarios, the cost of delay for a more precise answer outweighs the cost of imprecision, or the computational investment for a precise analysis is not justified or feasible.

## Strategy 9: Logical Fallacies as Computational Shortcuts

### The Psychological Phenomenon

Logical fallacies are patterns of reasoning that appear valid but contain logical flaws[^14]. While traditionally viewed as errors, many common fallacies can be understood as computationally efficient cognitive shortcuts that often work well in typical social or everyday environments (relying on simple patterns in $G_a$) despite being logically invalid in a formal sense (when rigorously checked against $G_p$ or formal logic).[[4](http://www.keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich.Sternberg2003.pdf)]

[^14]: Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131. While not focused specifically on logical fallacies, this paper established how seemingly irrational cognitive shortcuts serve pragmatic functions.

### Real-World Examples

1.  **Appeal to authority:** When facing complex topics, deferring to an expert opinion (checking if source node $V_{source}$ has an 'is_expert_in' edge to $V_{domain}$ in $G_a$) is computationally cheaper than personally evaluating all evidence in $G_p$.
2.  **Ad hominem reasoning (circumstantial):** Discounting arguments from sources with clear conflicts of interest (e.g., $V_{source}$ has an edge 'has_conflict_with' $V_{claim}$ in $G_a$) can be an efficient filtering mechanism.
3.  **Post hoc ergo propter hoc:** Assuming that if $V_B$ follows $V_A$ (an edge $(V_A, \text{precedes}, V_B)$ in $G_a$), then $V_A$ caused $V_B$ (inferring an edge $(V_A, \text{causes}, V_B)$), provides a simple causal model.

### The Computational Strategy

#### The Expensive "Correct" Algorithm (Formal Logical Evaluation):

```python
function evaluateArgumentFormally(claim_proposition P_claim, evidence_propositions E_set, source_node V_source, context_graph G_context, knowledge_graph G_p):
    # 1. Verify truthfulness of all premises in E_set against G_p (or a trusted G_a).
    for premise P_i in E_set:
        if not G_p.verify_truth(P_i): return "Invalid Argument: False Premise"
            
    # 2. Check logical validity of the inference from E_set to P_claim.
    #    This might involve converting propositions to a formal language and using a theorem prover.
    #    e.g., does (E1 AND E2 AND ... En) LOGICALLY_IMPLY P_claim?
    if not check_logical_validity(E_set, P_claim, G_p.logical_rules):
        return "Invalid Argument: Flawed Inference"
        
    # 3. Assess source reliability/expertise of V_source for P_claim in G_context from G_p.
    source_credibility = G_p.assess_source_properties(V_source, P_claim.domain)
    
    # 4. Consider alternative explanations for P_claim or E_set from G_p.
    # ... and so on for a full, rigorous evaluation.
    return "Argument Appears Sound (pending further checks)", source_credibility
```
This approach requires formal logical analysis, verification of all premises against $G_p$, evaluation of source credibility from $G_p$, and consideration of alternative explanations—a highly resource-intensive process.

#### The Fallacy-Based Heuristic Algorithm:

```python
function quickArgumentEvaluation(claim_node V_claim, source_node V_source, evidence_structure E_struct, active_graph G_a):
    # E_struct might be a simple pattern like "V_A precedes V_B" or "V_source asserts V_claim".
    
    # Appeal to Authority Heuristic:
    if G_a.has_edge(V_source, 'is_recognized_expert_in', V_claim.domain) and G_a.get_property(V_claim, 'requires_high_precision') == False:
        return "Accept Claim (Moderate Confidence)"
        
    # Post Hoc Heuristic:
    if E_struct.type == "temporal_sequence_A_then_B" and V_claim.asserts_causation("A_causes_B") and G_a.get_property(V_claim, 'requires_high_precision') == False:
        return "Tentatively Accept Causation (Low/Moderate Confidence)"
        
    # Ad Hominem (Conflict of Interest) Heuristic:
    if G_a.has_edge(V_source, 'has_strong_conflict_of_interest_regarding', V_claim):
        return "Lower Confidence in Claim / Seek Corroboration"
        
    # ... other fallacy-like shortcuts ...
    # If no simple heuristic applies or confidence is too low, may escalate to more careful analysis.
    return "Evaluation Inconclusive via Heuristics"
```
This approach uses source characteristics (properties of $V_{source}$ in $G_a$), simple structural patterns in $G_a$, and contextual relevance as proxies for thorough logical analysis over $G_p$.

### LLM Analogues and Behaviors

LLMs, trained on vast amounts of human text ($G_p$), can reproduce and sometimes appear to "use" patterns analogous to logical fallacies:
*   **Reproducing Fallacies from Training Data:** Human language is replete with logical fallacies. LLMs learn these patterns (common subgraphs in $G_p$) and can generate text that includes them. For instance, an LLM might generate an argument that sounds authoritative (mimicking an "appeal to authority" structure from $G_p$) because that pattern is common, even if the substance is weak or the "authority" cited is misattributed or irrelevant.[[31](https://zilliz.com/blog/how-to-detect-and-correct-logical-fallacies-from-genai-models)][[32](https://aclanthology.org/2025.naacl-long.374.pdf)]
*   **Correlation as Causation:** LLMs are excellent at identifying statistical correlations in their training data ($G_p$). They might present these correlations (e.g., node $V_A$ often co-occurs with node $V_B$) as causal relationships (inferring an edge $(V_A, \text{causes}, V_B)$) because such inferences are common in human discourse, even if not logically sound without further evidence from $G_p$.[[33](https://arxiv.org/abs/2410.05229)][[34](https://www.mobihealthnews.com/news/apple-study-highlights-limitations-llms)]
*   **Superficial Pattern Matching for Plausibility:** An LLM might assess or generate an argument based on superficial linguistic features (e.g., presence of "sciency" words, confident tone, common argumentative structures – all patterns in $G_p$) rather than deep logical structure. Their core mechanism is predicting plausible next tokens (extending paths in $G_a$ based on $G_p$'s statistics), not verifying logical validity.[[9](https://www.i-jmr.org/2025/1/e59823)][[31](https://zilliz.com/blog/how-to-detect-and-correct-logical-fallacies-from-genai-models)]
*   **Sensitivity to Phrasing over Logic:** LLMs can be swayed by how a problem is phrased (different initial $G_a$ structure), even if the underlying logical structure remains the same, indicating their reasoning is not always robustly logical.[[33](https://arxiv.org/abs/2410.05229)][[35](https://www.computing.co.uk/news/2024/ai/researchers-find-flaws-llm-reasoning)]

### Computational Rationality

Using these "fallacy-like" heuristics can be computationally rational under constraints because:

1.  **Computational simplicity:** Evaluating source trustworthiness (checking an edge in $G_a$) or temporal sequence is much simpler and faster than formal logical deconstruction over $G_p$.
2.  **Social & Environmental Efficiency:** Many fallacies encode heuristics that are often "good enough" in everyday social interactions or stable environments. Generally trusting recognized experts (a pattern in $G_a$) is often an adaptive shortcut.
3.  **Speed advantage:** Heuristic-based evaluation provides immediate assessments when formal analysis would be prohibitively time-consuming or impossible given available information in $G_a$.
4.  **Cognitive accessibility:** Patterns like authority appeals or simple causal inferences are easily applied across many domains without requiring deep, domain-specific logical expertise (complex subgraphs in $G_p$).

These shortcuts become problematic primarily when applied in contexts requiring high rigor where their underlying assumptions don't hold, or when exploited.

## Strategy 10: Satisficing (Good Enough is Best)

### The Psychological Phenomenon

**Satisficing**, a term coined by Herbert Simon, describes the strategy of choosing the first option that meets a minimum acceptability threshold or "aspiration level," rather than exhaustively searching for the absolute best (optimal) option[^11]. It's about finding a "good enough" solution quickly.

[^11]: Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review, 63*(2), 129–138. This paper introduced the concept of satisficing as a core element of bounded rationality.

### Real-World Examples

1.  **Choosing a restaurant:** Instead of researching every restaurant in the city for the "best" meal (optimizing over a large $G_p$), you pick the first one you find that looks decent and is within your budget (meets aspiration level using readily available info in $G_a$).
2.  **Job search:** Applying for jobs until one offer meets your minimum salary and work-life balance criteria, rather than waiting to evaluate all possible job offers in the market.
3.  **Product purchase:** Buying a product that fulfills the basic requirements without spending excessive time comparing every single alternative.

### The Computational Strategy

#### The Expensive "Correct" (Optimizing) Algorithm:

```python
function findOptimalSolution(problem_P, solution_space S, evaluation_func eval_f, knowledge_graph G_p):
    # S could be a vast space of potential solution subgraphs derived from G_p.
    best_solution_found = null
    max_score_found = -infinity
    
    for potential_solution Sol_i in S: # Exhaustively iterate through all possible solutions
        current_score = eval_f(Sol_i, G_p) # Evaluation might be complex, using G_p
        if current_score > max_score_found:
            max_score_found = current_score
            best_solution_found = Sol_i
            
    return best_solution_found
```
This approach requires generating or identifying all possible solutions in $S$ (often derived from $G_p$) and evaluating each one, which can be combinatorially explosive.

#### The Satisficing Algorithm:

```python
function findSatisficingSolution(problem_P, solution_generator_func gen_sol, evaluation_func eval_f, aspiration_level A_L, resource_limit R_L, active_graph G_a):
    # gen_sol generates potential solutions iteratively, possibly using heuristics based on G_a.
    # eval_f evaluates a solution, perhaps using simpler criteria based on G_a.
    
    solutions_considered = 0
    for potential_solution Sol_i in gen_sol(problem_P, G_a, R_L - solutions_considered):
        solutions_considered += 1
        if eval_f(Sol_i, G_a) >= A_L:
            return Sol_i # Found a "good enough" solution
        if solutions_considered >= R_L: # Check resource limit (e.g., time, computation)
            break
            
    return "No solution met aspiration level within resource limits" # Or return best found so far
```
This approach stops as soon as a solution meeting the `aspiration_level` is found using information primarily from $G_a$, or when resources run out.

### LLM Analogues and Behaviors

LLMs exhibit behaviors consistent with satisficing principles:
*   **Decoding Strategies (Top-k, Nucleus Sampling):** When generating text, LLMs don't just pick the single token with the absolute highest probability (which can lead to deterministic, repetitive output). Instead, strategies like top-k sampling or nucleus (top-p) sampling consider a *set* of sufficiently probable next tokens (those meeting an "aspiration level" of likelihood within $G_a$'s current state) and sample from this set. This is a form of satisficing for fluency and diversity, saving computation over exploring all exponentially many continuations.
*   **Stopping Criteria for Generation:** LLMs typically stop generating text when the output is deemed "sufficiently complete" (e.g., an end-of-sequence token is generated with high probability, or a length limit is reached), not necessarily when a theoretically "perfect" or "exhaustive" answer has been constructed. This is satisficing for response length and coherence.
*   **Iterative Refinement in Complex Tasks:** In multi-step reasoning (e.g., Chain-of-Thought prompting), an LLM might generate an initial thought or sub-solution, implicitly or explicitly check if it's "good enough" to proceed or if it meets an intermediate goal, and then continue. The overall goal is often a satisfactory final output within the implicit constraints of the interaction, not necessarily a globally optimal one derived from its entire $G_p$.

### Computational Rationality

The satisficing strategy is computationally rational under constraints because:

1.  **Drastic reduction in search costs:** It avoids the need to explore the entire solution space (all of $G_p$ or its derivatives), saving enormous computational resources.
2.  **Timeliness:** It provides solutions much more quickly, which is critical in time-pressured situations.
3.  **Tractability:** It makes decision-making possible in complex problems where finding the true optimum is computationally intractable or impossible with available information in $G_a$.
4.  **Resource management:** It allows for allocation of cognitive/computational effort proportional to the importance of the problem or the quality of solution needed.

The trade-off is that the chosen solution may not be the best possible one. However, in many real-world scenarios, the cost of finding the optimal solution (extensive search in $G_p$) outweighs the marginal benefit of the optimal solution over a "good enough" one found quickly using $G_a$.

## The Double-Edged Sword: Nuancing Computational Rationality

While framing these cognitive and algorithmic strategies as "computationally rational" offers valuable insights, it's crucial to nuance this perspective. The "optimality" of these approximate reasoning methods is highly context-dependent and comes with significant trade-offs.

1.  **Context is Key:** A strategy that is efficient and effective in one environment (e.g., making quick social judgments using $G_a$) can be detrimental in another (e.g., conducting rigorous scientific research requiring deep dives into $G_p$).[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)] The statistical properties of the environment and the specific goals of the reasoning agent determine whether a heuristic is truly adaptive.
2.  **The "Dark Side" of Heuristics:** While these shortcuts save cognitive resources, they are also the root of many well-documented biases that can lead to poor decisions, prejudice, and errors in critical situations.[[20](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)][[30](https://www.flyrank.com/id/blogs/berita-ai/study-reveals-chatgpt-s-cognitive-shortcuts-and-biases-questioning-ai-s-trustworthiness-in-critical-decisions)][[41](https://espace.library.uq.edu.au/data/UQ_fd10d8a/UQfd10d8a_OA.pdf)]
    *   **Stereotyping (Chunking/Prototypes):** Can lead to prejudice and discrimination when $G_a$'s chunks/prototypes are overgeneralized or biased.
    *   **Confirmation Bias:** Can entrench false beliefs (incorrect $G_{hypothesis}$ in $G_a$) and hinder learning.[[19](https://arxiv.org/html/2402.01769v1)][[22](https://arxiv.org/abs/2412.04629)]
    *   **Availability Heuristic:** Can lead to misjudgment of risks and poor decision-making when $G_a$'s salience doesn't match $G_p$'s true frequencies.[[19](https://arxiv.org/html/2402.01769v1)][[20](https://shs.cairn.info/journal-of-innovation-economics-2024-2-page-223?lang=en)][[42](https://www.itschiara.me/ai-human-collaboration)]
    *   **False Memories/Hallucinations:** Can have serious consequences if acted upon as truth, especially when $G_{reconstructed\_event}$ deviates significantly from reality.[[9](https://www.i-jmr.org/2025/1/e59823)][[10](https://www.getzep.com/ai-agents/reducing-llm-hallucinations)][[19](https://arxiv.org/html/2402.01769v1)][[21](https://www.comet.com/site/blog/llm-hallucination/)]

Therefore, while these strategies are computationally rational *given certain constraints on $G_a$ and for certain goals*, they are not universally optimal or without peril. Recognizing their dual nature—as both efficient adaptations and potential sources of systematic error—is vital for understanding both human fallibility and the challenges in developing truly intelligent and reliable AI.

## Conclusion: The Convergent Evolution of Approximate Reasoning

The exploration of these ten approximate reasoning strategies reveals a compelling pattern: both human cognition and, increasingly, advanced AI like Large Language Models, seem to converge on similar solutions when faced with the fundamental challenges of operating with incomplete information ($G_p$ instead of $G^\ast$) and finite computational resources (forcing reliance on a smaller $G_a$). These strategies—chunking, generative modeling, prototyping, context-dependence, availability/recency, confirmation bias, false memory/pattern completion, attribute substitution, logical fallacies as heuristics, and satisficing—all prioritize computational efficiency, generalization, and resource optimization, often at the cost of perfect, case-specific accuracy that would require full access to and processing of $G_p$ or $G^\ast$.

This perspective offers several critical implications:

1.  **Reframing "Biases" and "Errors":** Many cognitive biases and LLM "hallucinations" or errors can be understood not merely as flaws, but as byproducts of adaptive, computationally rational strategies operating on $G_a$ under constraints.[[1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1189704/full)][[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10187636/)][[3](https://www.erichorvitz.com/computational_rationality.pdf)][[4](http://www.keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich.Sternberg2003.pdf)][[9](https://www.i-jmr.org/2025/1/e59823)][[19](https://arxiv.org/html/2402.01769v1)] This doesn't excuse harmful outcomes but provides a deeper understanding of their origins.
2.  **Context-Dependent Rationality:** A reasoning strategy that appears irrational or flawed in a decontextualized laboratory setting or benchmark might be highly effective and rational in the complex, noisy, real-world environments for which its $G_a$-based operations evolved or were trained.
3.  **Guidance for Artificial Intelligence Design:** Instead of solely pursuing perfect logical reasoning (which is often intractable over $G_p$), AI systems designed for real-world interaction might benefit from explicitly incorporating or learning these kinds of resource-bounded, approximate reasoning mechanisms. Understanding their trade-offs is key to building more robust and adaptable AI. Some "emergent abilities" in LLMs might indeed be the result of the models implicitly learning such computationally efficient strategies for manipulating their internal $G_a$.[[11](https://www.assemblyai.com/blog/emergent-abilities-of-large-language-models)][[12](https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/)][[13](https://aclanthology.org/2024.acl-long.279/)][[43](https://openreview.net/pdf?id=yzkSU5zdwD)]
4.  **Human-AI Interaction and Cognitive Offloading:** As we increasingly rely on AI systems that exhibit these approximate reasoning patterns (operating on their own $G_a$), understanding their inherent cognitive shortcuts becomes crucial for effective collaboration and for mitigating risks associated with over-reliance or misinterpretation of AI outputs.[[42](https://www.itschiara.me/ai-human-collaboration)][[44](https://artificialityinstitute.org/how-ai-affects-critical-thinking-and-cognitive-offloading/)]
5.  **Educational and Mitigation Strategies:** Rather than attempting to eliminate these cognitive shortcuts entirely (which may be impossible or even counterproductive for efficient use of $G_a$), efforts could focus on metacognitive awareness: teaching humans (and perhaps instilling in AI) when specific approximate strategies are appropriate, when they are likely to lead to harmful errors, and when more rigorous, effortful processing (attempting to access or reconstruct parts of $G_p$) is required.

In a universe of bounded resources and pervasive uncertainty, perfect, exhaustive reasoning over a complete $G^\ast$ is a computationally expensive luxury, often an impossibility. The true art of intelligence, whether biological or artificial, lies in the sophisticated ability to make the *right* approximations—to know which corners to cut in $G_a$, which details to abstract from $G_p$, and which heuristics to trust, given the specific task, context, and available resources.

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