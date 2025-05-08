---
layout: post
title: Approximate reasoning 
subtitle: with incomplete models
---

## Introduction

When we reason, we make mistakes. We use stereotypes, fall for logical fallacies, remember events that never happened, and maintain contradictory beliefs. Traditionally, these errors have been viewed as flaws in human cognition—imperfections to be corrected through better education or more careful thinking.

But what if many of these "flaws" actually represent optimal strategies for reasoning with incomplete information and limited cognitive resources?

This post explores how the apparent irrationality of human reasoning might be computationally rational when viewed through the lens of approximate reasoning under constraints.

## Defining Our Setting: Reasoning Under Constraints

To properly analyze reasoning strategies, we need to define what constitutes "limited resources" and "incomplete information" in computational terms.

### Limited Resources

Reasoning systems (human or artificial) operate under several resource constraints:

1. **Memory limitations**: Bounded capacity to store facts, rules, and intermediate results
2. **Processing bandwidth**: Limited number of operations per unit time
3. **Energy constraints**: Computational operations require energy (particularly relevant for biological systems)
4. **Time pressure**: Decisions often need to be made before exhaustive analysis is possible

### Incomplete Information

Reasoning systems rarely have complete information about their domain:

1. **Partial observability**: Many relevant variables cannot be directly observed
2. **Noisy observations**: Available data contains errors and ambiguities
3. **Sparse sampling**: Only a tiny fraction of possible scenarios have been encountered
4. **Concept drift**: The underlying reality changes over time, invalidating past knowledge
5. **Hidden variables**: Unknown factors influence observed relationships

### Formal Framework

Let's formalize our reasoning model:

- Let $K$ be a knowledge base represented as a graph $G(V, E)$ where nodes $V$ represent concepts and edges $E$ represent relationships
- The "ground truth" would be a complete and accurate $G^*(V^*, E^*)$
- Due to incomplete information, we only have access to a partial graph $G_p(V_p, E_p)$ where $V_p \subset V^*$ and $E_p \subset E^*$
- Due to resource constraints, we can only actively utilize a subgraph $G_a(V_a, E_a)$ where $|V_a| \ll |V_p|$ and operations on $G_a$ are limited

Under these constraints, optimal reasoning strategies must balance:
- Accuracy of conclusions
- Resource utilization
- Speed of inference

Now let's examine specific strategies that achieve this balance.

## Strategy 1: Chunking Complex Paths (High-level Linkages)

### The Psychological Phenomenon

**Chunking** is a cognitive process where individual pieces of information are bound together into a meaningful whole[^1]. In reasoning, this manifests as compressing multi-step logical chains into direct associations, often appearing as heuristics or rules of thumb.

[^1]: Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97. This seminal paper established that human working memory is limited to approximately seven items, driving the need for chunking strategies.

### Real-World Examples

1. **Medical diagnosis**: An experienced doctor might directly associate a constellation of symptoms with a disease without consciously working through the underlying physiological mechanisms
   
2. **Chess expertise**: Grandmasters recognize board patterns and make moves without calculating every possible sequence, while novices must analyze each step methodically[^2]
   
3. **Social stereotyping**: We develop shortcut associations between social groups and attributes that bypass detailed individual assessment (e.g., "engineers are good at math")

[^2]: Chase, W. G., & Simon, H. A. (1973). Perception in chess. Cognitive Psychology, 4(1), 55–81. This research demonstrated that chess experts chunk board positions into meaningful patterns, allowing rapid recognition rather than piece-by-piece analysis.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:


```
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

```
function findChunkedConnection(conceptA, conceptB):
    If directConnectionExists(conceptA, conceptB):
        Return direct connection
    Else:
        Fall back to standard search algorithm
```

The `directConnectionExists` function checks a lookup table of pre-computed paths, effectively "chunking" commonly used multi-step inferences into single-step connections.

### Computational Optimality

The chunking strategy is optimal under our constraints because:

1. **Memory efficiency**: Storing compressed chunks requires significantly less memory than all possible detailed pathways ($O(n)$ vs $O(n^2)$ in the worst case)

2. **Time efficiency**: Chunk-based reasoning approaches $O(1)$ time complexity for common pathways versus $O(b^d)$ for search-based reasoning (where $b$ is the branching factor and $d$ is the path depth)

3. **Error profile**: Errors typically occur only when exceptions to the chunked rule exist, which is an acceptable trade-off when these exceptions are rare in the environment

This creates a power-law efficiency: Frequently used reasoning patterns become extremely efficient at the cost of potentially missing edge cases—exactly the pattern we see in human expertise development.

## Strategy 2: Generative Models of Relationships (Factoring Links)

### The Psychological Phenomenon

**Schema-based reasoning** involves using abstract knowledge structures to generate expectations and inferences about new situations without storing every possible relationship[^3]. This manifests psychologically as our ability to make reasonable guesses about novel situations based on their similarity to familiar categories.

[^3]: Bartlett, F.C. (1932). Remembering: A Study in Experimental and Social Psychology. Cambridge University Press. This classic work introduced the concept of schemas as dynamic knowledge structures that guide perception and memory.

### Real-World Examples

1. **Restaurant scripts**: When entering a new restaurant, we automatically know to wait to be seated, expect a menu, and pay after eating—without having to memorize the procedure for each specific establishment[^4]

2. **Technological interfaces**: We can navigate new smartphone apps using general interface schemas without reading instructions for each one

3. **Social relationships**: We apply relationship models (friend, colleague, authority figure) to new acquaintances that generate appropriate behavioral expectations

[^4]: Schank, R. C., & Abelson, R. P. (1977). Scripts, plans, goals, and understanding: An inquiry into human knowledge structures. Lawrence Erlbaum. This work formalized how people use schematic knowledge structures ("scripts") to navigate common social situations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function determineRelationship(conceptA, conceptB):
    Look up in complete relationship matrix M[conceptA, conceptB]
    Return stored relationship type and strength
```

This approach requires storing an explicit relationship between every pair of concepts—an $O(n^2)$ space requirement where $n$ is the number of concepts.

#### The Generative Algorithm:

```
function generateRelationship(conceptA, conceptB):
    features_A = extractFeatures(conceptA)
    features_B = extractFeatures(conceptB)
    relationship = relationshipModel(features_A, features_B)
    Return relationship
```

This approach uses a parameterized model that generates likely relationships based on concept features rather than storing each relationship explicitly.

### Computational Optimality

The generative model strategy is optimal under constraints because:

1. **Memory efficiency**: Storing a parametric model with $k$ parameters where $k \ll n^2$ drastically reduces memory requirements from $O(n^2)$ to $O(k + n)$

2. **Generalization**: The model can generate reasonable relationship hypotheses for entirely new concepts never seen before

3. **Update efficiency**: New information can update the general model rather than requiring updates to many individual relationships

4. **Graceful degradation**: When exact relationships aren't known, the system still produces plausible approximations

The trade-off is reduced precision for specific cases that deviate from general patterns, which is optimal when most relationships follow regular patterns and resources are insufficient to memorize all exceptions.

## Strategy 3: Prototype-Based Representation (Sketched Nodes)

### The Psychological Phenomenon

**Prototype theory** proposes that humans categorize objects by comparing them to abstract prototypes that represent the central tendency of the category, rather than through strict definitional boundaries[^5]. This allows efficient representation of complex categories using only a few exemplars.

[^5]: Rosch, E. (1975). Cognitive representations of semantic categories. Journal of Experimental Psychology: General, 104(3), 192–233. This research demonstrated that people judge category membership by similarity to prototypes rather than by necessary and sufficient conditions.

### Real-World Examples

1. **Bird recognition**: We recognize birds by their similarity to prototypical birds (like robins) rather than checking a list of necessary and sufficient conditions, which explains why penguins and ostriches are psychologically "less bird-like"[^6]

2. **Facial recognition**: We identify faces by comparing them to abstracted prototypes rather than memorizing every possible face

3. **Concept learning**: Children learn concepts like "chair" by exposure to examples and abstraction of common features, not by memorizing definitions

[^6]: Lakoff, G. (1987). Women, Fire, and Dangerous Things: What Categories Reveal about the Mind. University of Chicago Press. This work explored how prototypes and radial categories structure human conceptual systems.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function representConcepts(domain):
    concepts = []
    For each distinct entity in domain:
        Store complete feature vector
        Add to concepts
    Return concepts
```

This approach stores every concept as a separate entity with its full feature representation, requiring $O(nf)$ space where $n$ is the number of concepts and $f$ is the number of features.

#### The Prototype Algorithm:

```
function representWithPrototypes(domain):
    clusters = findClusters(domain)
    prototypes = []
    For each cluster:
        prototype = computeCentralTendency(cluster)
        Add prototype to prototypes
    function recognizeConcept(entity):
        Return nearestPrototype(entity, prototypes) + transformVector
    Return prototypes, recognizeConcept
```

This approach stores only cluster prototypes plus transformation rules, reducing storage requirements significantly.

### Computational Optimality

The prototype strategy is optimal under constraints because:

1. **Memory efficiency**: Storing $k$ prototypes where $k \ll n$ reduces memory requirements from $O(nf)$ to $O(kf)$

2. **Generalization capacity**: Novel entities can be represented as transformations of existing prototypes

3. **Retrieval efficiency**: Similarity-based retrieval allows fast approximate matching

4. **Graceful degradation**: Even with limited information, the system can approximate concepts by their nearest prototype

The trade-off is category boundary fuzziness and typicality effects, which are acceptable when exact boundaries are rarely needed and resources are insufficient to store every instance.

## Strategy 4: Context-Dependent Inconsistency Tolerance

### The Psychological Phenomenon

**Belief compartmentalization** refers to the human tendency to hold contradictory beliefs simultaneously by segregating them into different contexts or domains[^7]. Rather than maintaining global consistency, we allow local inconsistencies when they serve practical purposes.

[^7]: Festinger, L. (1957). A Theory of Cognitive Dissonance. Stanford University Press. This influential work explored how people manage contradictory beliefs, often through compartmentalization to reduce cognitive dissonance.

### Real-World Examples

1. **Religious and scientific beliefs**: Many scientists maintain religious beliefs that would appear to contradict their scientific understanding, activating different belief systems in different contexts[^8]

2. **Health behaviors**: People often maintain inconsistent beliefs about health risks, such as knowing smoking causes cancer while believing "it won't happen to me"

3. **Professional vs. personal ethics**: People may apply different ethical standards in business contexts than in personal relationships

[^8]: Legare, C. H., & Visala, A. (2011). Between religion and science: Integrating psychological and philosophical accounts of explanatory coexistence. Human Development, 54(3), 169-184. This research examines how people integrate seemingly incompatible religious and scientific explanations.

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
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

```
function contextualKnowledge(newFact, context):
    contextualKB = knowledgeBase.getContext(context)
    Add newFact to contextualKB
    function retrieveFact(query, context):
        Return knowledgeBase.getContext(context).lookup(query)
    Return retrieveFact
```

This approach stores knowledge in context-specific compartments, only checking for consistency within relevant contexts.

### Computational Optimality

The compartmentalization strategy is optimal under constraints because:

1. **Computational efficiency**: Consistency checking is limited to relevant subsets of knowledge rather than the entire knowledge base, reducing complexity from $O(n)$ to $O(c)$ where $c$ is the size of the active context

2. **Practical accuracy**: Domain-specific approximations can be more accurate within their domains than general rules that must account for all cases

3. **Learning efficiency**: New information can be incorporated without expensive global restructuring

4. **Adaptability**: Different contexts can maintain specialized knowledge representations optimized for their domain

The trade-off is potential contradictions when contexts overlap, which is acceptable when most reasoning occurs within specific contexts and cross-context consistency is rarely needed.

## Strategy 5: Recency and Availability Heuristics

### The Psychological Phenomenon

The **availability heuristic** causes people to judge the likelihood of events based on how easily examples come to mind[^9]. Related to this, the **recency effect** gives disproportionate weight to recently encountered information. Together, these biases prioritize information that is likely to be relevant in the current temporal and spatial context.

[^9]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology, 5(2), 207–232. This paper introduced the availability heuristic as a mental shortcut that relies on immediate examples that come to mind.

### Real-World Examples

1. **Risk assessment**: People overestimate the likelihood of plane crashes after media coverage of an accident, while underestimating more common but less publicized risks like heart disease

2. **Stock market decisions**: Investors give more weight to recent market performance than long-term trends

3. **Consumer choices**: Purchase decisions are heavily influenced by recently viewed advertisements or recommendations

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function assessProbability(event):
    Count all historical occurrences of event
    Count all possible scenarios
    Return occurrences / possible scenarios
```

This approach requires maintaining complete historical statistics and computing true frequencies, which is memory and computation intensive.

#### The Availability Algorithm:

```
function estimateProbability(event):
    examples = retrieveExamples(event)
    recencyWeight = function(example):
        Return 1 / (current_time - example.time)
    availability = sum(recencyWeight(e) for e in examples)
    Return availability
```

This approach estimates probabilities based on the ease of retrieving examples, with a strong recency bias.

### Computational Optimality

The availability strategy is optimal under constraints because:

1. **Memory efficiency**: Only requires storing a sample of events rather than complete statistics

2. **Temporal relevance**: Recent events are often more predictive of current conditions due to environmental autocorrelation

3. **Computation simplicity**: Avoids complex probability calculations by using retrieval fluency as a proxy

4. **Attentional allocation**: Resources are directed to information that is likely to be immediately relevant

The trade-off is systematic bias when media exposure or emotional salience distorts true frequencies, which is acceptable when the environment is relatively stable and recent information is generally more relevant than distant history.

## Strategy 6: Confirmation Bias and Hypothesis Maintenance

### The Psychological Phenomenon

**Confirmation bias** is the tendency to search for, interpret, and recall information in a way that confirms existing beliefs[^10]. While often framed as a cognitive flaw, it can be viewed as a resource-efficient strategy for maintaining stable beliefs in noisy information environments.

[^10]: Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. Review of General Psychology, 2(2), 175–220. This comprehensive review documents confirmation bias across many domains and explains its cognitive foundations.

### Real-World Examples

1. **Political beliefs**: People selectively consume news that aligns with their political views and interpret ambiguous events as supporting their position

2. **Scientific research**: Scientists may design experiments to confirm rather than challenge their hypotheses and be more critical of methodologies in studies with contrary findings

3. **Relationship judgments**: People tend to notice behaviors that confirm initial impressions of others while overlooking contradictory evidence

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function evaluateHypothesis(hypothesis, data):
    For each possible alternative hypothesis:
        Calculate P(data|hypothesis) for all data points
        Calculate prior probability P(hypothesis)
        Apply Bayes' rule to compute P(hypothesis|data)
    Return hypothesis with highest posterior probability
```

This approach requires maintaining and evaluating all possible alternative hypotheses, which is computationally expensive.

#### The Confirmation-Biased Algorithm:

```
function maintainHypothesis(currentHypothesis, newData):
    If supports(newData, currentHypothesis):
        Increase confidence in currentHypothesis
    Else if weaklyContradicts(newData, currentHypothesis):
        Discount or reinterpret newData
    Else if stronglyContradicts(newData, currentHypothesis):
        Consider revising hypothesis
    Return updated currentHypothesis and confidence
```

This approach maintains the current hypothesis unless strongly contradicted, focusing computational resources on interpretation rather than complete re-evaluation.

### Computational Optimality

The confirmation bias strategy is optimal under constraints because:

1. **Computational efficiency**: Evaluating a single hypothesis against data is $O(n)$ compared to $O(hn)$ for evaluating $h$ hypotheses

2. **Learning stability**: Prevents belief oscillation in noisy environments where contradictory evidence may be spurious

3. **Resource allocation**: Focuses cognitive resources on refining the current best hypothesis rather than constantly exploring alternatives

4. **Search efficiency**: Directs information seeking toward relevant data that can refine the current model

The trade-off is resistance to belief updating when the environment changes, which is acceptable when:
- The environment is relatively stable
- The cost of false belief change exceeds the cost of delayed adaptation
- Computational resources are insufficient to maintain multiple complex hypotheses

## Strategy 7: Satisficing Decision Making

### The Psychological Phenomenon

**Satisficing** is a decision-making strategy where people accept "good enough" solutions rather than optimizing for the best possible outcome[^11]. Rather than exhaustively evaluating all options, people stop searching once they find an acceptable alternative.

[^11]: Simon, H. A. (1956). Rational choice and the structure of the environment. Psychological Review, 63(2), 129–138. Herbert Simon introduced the concept of satisficing as a bounded rationality strategy that seeks adequacy rather than optimality.

### Real-World Examples

1. **Consumer purchases**: Instead of reviewing all possible products, shoppers often buy the first item that meets their basic requirements

2. **Hiring decisions**: Recruiters may hire the first candidate who exceeds a threshold of qualifications rather than interviewing all applicants

3. **Everyday problem solving**: When facing a computer issue, people typically try solutions until one works, rather than analyzing the optimal approach

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
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

```
function satisfice(options, acceptabilityThreshold):
    For each option in options:
        If value(option) >= acceptabilityThreshold:
            Return option
    // If no option meets threshold, fall back to optimization
    Return optimizeDecision(options, valuationFunction)
```

This approach returns the first acceptable option encountered, requiring only $O(k)$ evaluations where $k$ is the position of the first acceptable option.

### Computational Optimality

The satisficing strategy is optimal under constraints because:

1. **Search termination**: Early stopping dramatically reduces the average case computational complexity from $O(n)$ to $O(k)$ where $k \ll n$ in many real-world scenarios

2. **Diminishing returns**: The difference between an acceptable solution and the optimal solution is often small compared to the cost of finding the optimum

3. **Time sensitivity**: Many decisions lose value if delayed too long, making a quick "good enough" decision better than a slow optimal one

4. **Exploration-exploitation balance**: Resources saved through satisficing can be allocated to other tasks or problems

The trade-off is settling for suboptimal solutions, which is acceptable when:
- The distribution of options has a small variance in quality above the acceptability threshold
- Search costs are high relative to the benefits of optimization
- Time pressure requires rapid decisions

## Strategy 8: False Memory and Pattern Completion

### The Psychological Phenomenon

**False memory** refers to the phenomenon where people remember events that never occurred or remember them differently from how they occurred[^12]. This can be viewed as an adaptive pattern completion mechanism rather than simply a memory failure.

[^12]: Loftus, E. F. (2005). Planting misinformation in the human mind: A 30-year investigation of the malleability of memory. Learning & Memory, 12(4), 361–366. This paper reviews research showing how memory reconstructs rather than reproduces past events.

### Real-World Examples

1. **Eyewitness testimony**: Witnesses often "remember" details that align with their expectations rather than what they actually observed

2. **Childhood memories**: People incorporate family stories and photographs into their "memories," believing they remember events they only heard about

3. **Educational contexts**: Students often misremember information in ways that make it more coherent with their existing knowledge

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function recall(event):
    Retrieve complete storage record of event
    If record exists:
        Return record
    Else:
        Return "No memory found"
```

This approach requires perfect storage and retrieval of all experienced events, which is memory intensive.

#### The Pattern Completion Algorithm:

```
function reconstructiveRecall(eventPartial):
    knownFragments = retrieve(eventPartial)
    context = getCurrentContext()
    schemaExpectations = activateSchema(context)
    reconstructed = combine(knownFragments, schemaExpectations)
    Return reconstructed
```

This approach reconstructs memories by combining stored fragments with schematic expectations.

### Computational Optimality

The pattern completion strategy is optimal under constraints because:

1. **Storage efficiency**: Storing gist and distinctive elements requires much less memory than storing complete episodic records

2. **Retrieval robustness**: Pattern completion allows recall from partial cues, making memory more fault-tolerant

3. **Generalization capacity**: Reconstructed memories emphasize schema-consistent aspects that are more likely to be useful in future situations

4. **Prediction utility**: Filled-in details often represent likely truths based on world knowledge

The trade-off is reduced accuracy for specific details, which is acceptable when:
- The gist of memories is more important than perfect detail
- Memory storage capacity is limited
- The environment contains strong statistical regularities that make educated guesses usually correct

## Strategy 9: Question Substitution (Attribute Substitution)

### The Psychological Phenomenon

Attribute substitution occurs when people respond to a difficult question by unconsciously substituting it with an easier one[^13]. Rather than engaging in computationally expensive reasoning about a complex attribute, the mind quickly assesses a related but simpler attribute.

[^13]: Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In T. Gilovich, D. Griffin, & D. Kahneman (Eds.), Heuristics and biases: The psychology of intuitive judgment (pp. 49–81). Cambridge University Press. This paper introduced the concept of attribute substitution as a general mechanism underlying many cognitive biases.

### Real-World Examples

1. **Risk assessment:** When asked "How dangerous is this activity?" people often answer the easier question "How afraid does this make me feel?" which explains why shark attacks seem more dangerous than diabetes despite vastly different mortality rates

2. **Person evaluation:** When asked "Will this candidate be successful?" interviewers often substitute "Did I feel good during the interview?" leading to confidence in judgments with poor predictive validity

3. **Economic forecasting:** When asked "How will the market perform next year?" experts often answer the easier question "How has the market performed recently?" leading to trend extrapolation

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function evaluateAttribute(target, complexAttribute):
    relevantFactors = identifyAllFactors(complexAttribute)
    data = collectDataForAllFactors(target, relevantFactors)
    weights = determineFactorWeights(complexAttribute)
    For each factor in relevantFactors:
        Analyze historical correlation between factor and attribute
        Assess causal mechanisms
        Model interactions between factors
    Return weightedCalculation(data, weights)
```

This approach requires extensive data collection, causal analysis, and computational resources to properly evaluate complex attributes.

#### The Substitution Algorithm:

```
function substituteAttribute(target, complexAttribute):
    accessibleAttributes = identifyAccessibleAttributes(target)
    substituteAttribute = selectCorrelatedAttribute(accessibleAttributes, 
                                                   complexAttribute)
    return evaluateSimpleAttribute(target, substituteAttribute)
```

This approach replaces the difficult evaluation with a simpler one based on an accessible attribute that is somewhat correlated with the target attribute.

### Computational Optimality

The question substitution strategy is optimal under constraints because:

1. **Computational efficiency:** Evaluating a simple attribute often requires orders of magnitude less computation than a complex one (e.g., $O(1)$ vs $O(n^2)$)

2. **Data requirements:** Simple attributes typically require much less data to assess than complex ones

3. **Response speed:** Substitution allows for rapid responses when decisions under time pressure are required

4. **Heuristic value:** The substitute attribute often correlates sufficiently with the complex attribute to provide above-chance accuracy

The trade-off is systematic bias when the substitute attribute diverges from the target attribute, which is acceptable when:

- The correlation between attributes is reasonably high in common environments
- The cost of delay exceeds the cost of imprecision
- Complete information for the complex attribute is unavailable
- The decision doesn't justify the computational investment required for precise analysis

## Strategy 10: Logical Fallacies as Computational Shortcuts

### The Psychological Phenomenon

Logical fallacies are patterns of reasoning that appear valid but contain logical flaws[^14]. While traditionally viewed as errors, many common fallacies can be understood as computationally efficient heuristics that work well in typical social environments despite being logically invalid.

[^14]: Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131. While not focused specifically on logical fallacies, this paper established how seemingly irrational cognitive shortcuts serve pragmatic functions.

### Real-World Examples

1. **Appeal to authority:** When facing complex topics like climate science or medicine, deferring to expert opinion is computationally cheaper than personally evaluating all evidence, even though it's technically a logical fallacy

2. **Ad hominem reasoning:** Discounting arguments from sources with conflicts of interest or previous false claims serves as an efficient filtering mechanism, though logically the source doesn't determine truth value

3. **Post hoc reasoning (correlation-causation confusion):** Assuming that if B follows A, then A caused B provides a simple causal model that's often correct in everyday experience despite being logically invalid

### The Computational Strategy

#### The Expensive "Correct" Algorithm:

```
function evaluateArgument(claim, evidence):
    formalizeLogic(claim, evidence)
    verifyPremises(evidence)
    checkValidityOfInference(claim, evidence)
    checkForAlternativeExplanations(claim)
    assessPriorProbability(claim)
    Return validityScore, probabilityScore
```

This approach requires formal logical analysis, verification of all premises, and consideration of alternative explanations.

#### The Fallacy-Based Algorithm:

```
function quickArgumentEvaluation(claim, source, context):
    if isAuthoritativeSource(source) && !requiresPrecision(context):
        Return acceptClaim(claim)
    if followsTemporally(evidence, claim) && !requiresPrecision(context):
        Return acceptClaim(claim)
    if hasConflictOfInterest(source):
        Return rejectClaim(claim)
    // More fallacy-based shortcuts
    // Fall back to more careful analysis if context requires
```

This approach uses source characteristics and simple pattern matching rather than formal logical analysis.

### Computational Optimality

The fallacy-based reasoning strategy is optimal under constraints because:

1. **Computational simplicity:** Evaluating source trustworthiness or temporal sequence is much simpler than formal logical analysis

2. **Social efficiency:** Many fallacies encode social heuristics that work well in practice (e.g., generally trusting experts is adaptive)

3. **Speed advantage:** Fallacious reasoning provides immediate answers when formal analysis would be prohibitively time-consuming

4. **Cognitive accessibility:** Patterns like authority appeals are easily applied across domains without domain-specific knowledge

The trade-off is vulnerability to systematic errors when the shortcut doesn't align with logical validity, which is acceptable when:

- The environmental structure makes the fallacy usually correct (e.g., effects typically do follow causes)
- The precision requirements of the decision don't justify exhaustive analysis
- The decision is in a domain where expertise strongly correlates with accuracy
- Social coordination benefits outweigh individual accuracy costs

These fallacies become problematic primarily when applied in contexts where their underlying assumptions don't hold—such as scientific reasoning, where correlation-causation distinctions are crucial, or in evaluating fringe claims where authority appeals may mislead.

## Conclusion: The Computational Rationality of Cognitive Biases

The strategies examined above share a common pattern: they sacrifice perfect accuracy in specific cases to achieve greater computational efficiency (average case), better generalization, and more effective resource allocation. Importantly, these trade-offs are often optimal given the constraints under which human cognition operates.

This perspective suggests several important implications:

1. **Reframing biases**: Many cognitive biases should be understood not as design flaws but as adaptive solutions to computational constraints

2. **Context-dependent rationality**: A reasoning strategy that appears irrational in a laboratory setting may be optimal in real-world environments with specific statistical properties

3. **Artificial intelligence design**: Systems that aim for human-like intelligence might benefit from implementing some of these approximate reasoning strategies rather than aiming for perfect but computationally intractable reasoning

4. **Educational approaches**: Rather than trying to eliminate cognitive biases entirely, education might focus on understanding when particular approximate strategies are appropriate and when they lead to harmful errors

In a world of bounded resources and incomplete information, perfect reasoning is not only impossible but suboptimal. The art of intelligence—whether human or artificial—lies in knowing which corners to cut and which approximations to make given the task at hand.

As we develop increasingly sophisticated AI systems, we should remember that the seemingly irrational quirks of human cognition might contain hidden wisdom about how to reason effectively in complex, uncertain environments with limited computational resources.

## References