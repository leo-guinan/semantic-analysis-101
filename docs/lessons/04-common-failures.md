# 04 — Common interpretation failures

Semantic trend graphs fail in predictable ways.

The failures are not random. They are mostly the usual human crimes with nicer typography.

## 1. Low-N overclaiming

Pattern:

> A dramatic spike happened, therefore discourse changed.

Correction:

> A dramatic spike happened in a low-document bucket. Treat it as weak until corroborated.

Minimum response:

- name the document count
- compare it to neighboring buckets
- avoid quoting the spike alone

## 2. Screenshot laundering

Pattern:

A chart gets shared without:

- corpus source
- date range
- bucket size
- document counts
- caveats

Correction:

The chart image itself should carry those fields. If not, the screenshot is not self-contained evidence.

## 3. Alpha absolutism

Pattern:

> Alpha went up, so the concept became more doom-like.

Correction:

Alpha is normalized between two selected poles. You still need raw cosine scores and margin size.

## 4. Close-margin overconfidence

Pattern:

> Pole B is higher, therefore B wins.

Correction:

If both poles are high and the difference is tiny, the honest claim is weak.

Say:

> B is slightly higher, but both poles are strongly activated and the margin is small.

## 5. Corpus substitution

Pattern:

> This chart shows what people think.

Correction:

It shows what this corpus says under this measurement setup.

A corpus of tweets, headlines, papers, or comments cannot silently stand in for “people.”

## 6. Causal storytelling

Pattern:

> The line moved after event X, so X caused the movement.

Correction:

The chart can suggest an event worth inspecting. It does not establish causality.

## 7. Pole smuggling

Pattern:

The analyst chooses loaded pole terms, then acts surprised by the result.

Correction:

Publish the pole terms. Better: test alternative pole sets.

## 8. No-result embarrassment

Pattern:

The data shows no meaningful trend, but the analyst forces a story because “nothing happened” feels like failure.

Correction:

A chart that can say “nothing meaningful here” is more trustworthy than one that always produces a story.

Boring null results are where credibility goes to take a nap. Let it sleep.
