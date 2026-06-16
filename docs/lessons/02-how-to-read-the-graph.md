# 02 — How to read the graph

A Semantic Axis graph usually has four pieces:

1. alpha line
2. raw cosine similarities
3. time buckets
4. document-count bars

## Alpha

Alpha is the normalized position between two poles.

In the teaching examples:

- lower alpha means closer to optimism
- higher alpha means closer to doom
- alpha near 0.5 means roughly balanced between the poles

Alpha is useful because it gives one readable line.

Alpha is dangerous because a normalized line can make tiny differences look dramatic.

## Raw cosine scores

Cosine scores show how semantically close the concept is to each pole.

If both cosine scores are high, that means both poles are semantically active.

Example:

- cos optimism: 0.82
- cos doom: 0.84

A careless reading says:

> Doom wins.

A better reading says:

> Both optimism and doom are close. Doom is slightly higher, but the margin is small.

This is less satisfying. Excellent.

## Buckets

Buckets are time windows.

Monthly buckets answer a different question than quarterly buckets. A monthly spike can disappear when aggregated quarterly. A quarterly average can hide a short event.

Always ask:

- What is the bucket size?
- Is the bucket size appropriate for the phenomenon?
- Are we comparing buckets with similar document volume?

## Document-count bars

Document counts are evidence volume.

They do not prove truth. They tell you how much text the bucket measurement is based on.

A dramatic movement based on 18 documents should receive less trust than a stable movement based on 1,200 documents.

Document counts should be visible in the chart itself because screenshots escape their containers. If the warning lives below the fold, it is already gone.

## Reading order

Use this order:

1. Read title, corpus, date range, bucket size.
2. Check document counts.
3. Look for low-volume buckets.
4. Compare alpha movement.
5. Compare raw cosine scores.
6. Ask whether the margin is large enough to quote.
7. State the caveat before the claim.

The caveat is not an apology. It is the thing that makes the claim minimally honest.
