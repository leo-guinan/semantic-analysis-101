# Checklist before quoting a semantic trend

Use this before turning a graph into a sentence.

## 1. Name the corpus

Can you say exactly what text was measured?

Bad:

> AI discourse became more pessimistic.

Better:

> In this synthetic fixture / tweet archive / comment corpus, AI language moved toward the doom pole.

## 2. Name the time range and bucket size

Ask:

- What dates are included?
- Are buckets monthly, quarterly, or yearly?
- Would the claim change with a different bucket size?

## 3. Check document volume

Ask:

- How many documents are in the bucket I am quoting?
- Is that count similar to neighboring buckets?
- Is the most dramatic bucket also the lowest-volume bucket?

If yes, lower confidence.

## 4. Compare raw cosine scores

Ask:

- Is one pole clearly higher?
- Are both poles high?
- Is the margin large or tiny?

If both poles are high and close, do not make a strong directional claim.

## 5. Separate signal from interpretation

Signal:

> Alpha increased from 0.50 to 0.78.

Interpretation:

> The corpus became more doom-like.

Public claim:

> In this corpus, the low-volume April bucket shifted toward the doom pole, but the bucket has only 18 documents, so it should be treated as weak evidence.

The third sentence costs more. That is why it is useful.

## 6. Check screenshot safety

If the graph is shared alone, does it still show:

- corpus
- date range
- bucket size
- document counts
- pole terms
- model / method caveat

If not, the graph is not ready to travel.

## 7. State what would falsify the claim

Examples:

- the spike disappears with more documents
- alternative pole terms remove the effect
- adjacent buckets do not support the claimed trend
- raw cosine margins are too small
- a null/shuffled control produces similar movement

If nothing could change your interpretation, congratulations: you have left analysis and entered décor.
