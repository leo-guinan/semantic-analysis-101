# 03 — Four teaching datasets

The examples in this repo use synthetic data with answer keys. That matters.

With real data, you can argue forever about what the signal means. With synthetic data, we can first test whether someone reads the graph correctly when the intended answer is known.

## Dataset 1: clean-room phase shift

![Clean-room graph](../assets/clean-room.svg)

What it contains:

- 9 monthly buckets
- optimism phase
- neutral phase
- doom phase
- enough documents in every bucket

Correct reading:

> The synthetic corpus moves from optimism to neutral to doom.

Watch out for:

- treating the synthetic result as real-world evidence
- ignoring that the poles were chosen by the analyst

## Dataset 2: misleading low-volume spike

![Misleading-volume graph](../assets/misleading-volume.svg)

What it contains:

- mostly high-volume neutral buckets
- one dramatic low-volume spike
- the spike bucket has only 18 documents

Correct reading:

> The spike is visually dramatic but evidentially weak.

Watch out for:

- quoting the spike without the 18-doc caveat
- cropping away volume bars
- confusing visual drama with evidentiary strength

## Dataset 3: null / shuffled

![Null shuffled graph](../assets/null-shuffled.svg)

What it contains:

- 12 monthly buckets
- stable document counts
- alpha wiggles around neutral
- no planted semantic drift

Correct reading:

> There is no meaningful semantic trend.

Watch out for:

- inventing seasonal stories
- over-reading small wiggles
- using a chart because a paragraph saying “nothing happened” feels disappointing

## Dataset 4: close-margin / high-correlation

![Close-margin graph](../assets/close-margin.svg)

What it contains:

- both poles have high cosine scores
- differences are tiny
- alpha mildly favors doom but not enough for a strong claim

Correct reading:

> Both poles are semantically close; the margin is small.

Watch out for:

- treating normalized alpha as strength
- ignoring raw cosine scores
- claiming direction without magnitude

## Suggested teaching sequence

1. Start with clean-room so people learn the grammar.
2. Show misleading-volume to teach evidence volume.
3. Show null/shuffled to teach restraint.
4. Show close-margin to teach margin and uncertainty.

This order moves from easy reading to honest reading. The latter is rarer.
