# 01 — What is a semantic trend?

A semantic trend is a time series built from text.

Instead of counting exact words, it asks how close a concept is to two chosen semantic poles in each time bucket.

Example setup:

- concept: `AI`, `artificial intelligence`
- pole A: `optimism`, `hope`, `progress`
- pole B: `doom`, `risk`, `danger`
- corpus: a set of documents, posts, headlines, comments, or transcripts
- bucket size: monthly, quarterly, yearly

The output is not “what people believe.”

It is closer to:

> In this corpus, during this time window, the language around this concept was closer to these pole terms than those pole terms.

That sentence has several load-bearing clauses. Remove one and the chart becomes a fortune cookie with a y-axis.

## What semantic trends are good for

Semantic trends can help with:

- tracking shifts in discourse over time
- comparing different corpora
- finding moments worth investigating
- generating hypotheses
- making latent language movement visible

## What semantic trends are not good for

They do not automatically prove:

- public opinion changed
- a causal event happened
- a community believes something
- the future will follow the line
- a tiny difference is meaningful

A semantic graph is a measurement artifact. Treat it like a lab instrument, not a horoscope.

## The minimum context required

Before interpreting a trend, you need:

1. corpus source
2. date range
3. bucket size
4. document counts per bucket
5. concept terms
6. pole terms
7. raw similarity scores or enough information to judge margin size
8. known caveats

If the chart cannot carry those basics, it is not ready to travel as a screenshot.
