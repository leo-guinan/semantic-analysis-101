# Glossary

## Alpha / α

A normalized measure of where a concept sits between two semantic poles.

In these teaching examples:

- lower α: closer to optimism
- higher α: closer to doom
- α near 0.5: roughly balanced

Alpha is not confidence. It is position.

## Cosine similarity

A measure of closeness between two embedding vectors.

Higher cosine means more semantic similarity under the embedding model.

## Pole

One side of a semantic contrast.

Example:

- pole A: optimism, hope, progress
- pole B: doom, risk, danger

The pole terms matter. Change them and the measurement can change.

## Concept

The thing being measured against the poles.

Example:

- AI
- artificial intelligence

## Corpus

The text collection being measured.

Examples:

- tweets
- papers
- news headlines
- comments
- synthetic fixtures

A corpus is not automatically a population.

## Bucket

A time window used to group documents.

Examples:

- month
- quarter
- year

## Document count

The number of documents in a bucket.

Document count is evidence volume, not truth. Low counts make measurements easier to overinterpret.

## Margin

The difference between similarity to one pole and similarity to the other.

A tiny margin should produce a weak claim.

## Null control

A dataset or setup where no meaningful signal should appear.

If your chart finds a dramatic story in the null control, the chart may be manufacturing drama.
