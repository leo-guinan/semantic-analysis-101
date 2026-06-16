# Case: close-margin / high-correlation

![Close-margin graph](../assets/close-margin.svg)

## What to notice

- Both raw cosine scores are high.
- The two pole scores move together.
- The margins are small.
- Alpha alone can make the lean look more decisive than it is.
- This may be an axis-construction problem, not a finding.

## Safe interpretation

> These poles are not clean opposites. They appear correlated, so the measurement may be capturing that the topic is much discussed and consistently semantically close to both poles. The small divergence is likely noise from word choice; not even a caveat makes a directional claim meaningful.

## Unsafe interpretation

> AI is clearly doom-coded.

Why unsafe:

- both poles score high
- the pole scores are correlated rather than opposed
- the difference is tiny
- normalized alpha hides how close the raw scores are
- wording artifacts like negation, “not,” or “no” can distort which pole a bucket appears closer to

## Teaching use

Use this after the low-volume and null examples. It teaches that some axes should be rejected, not merely interpreted cautiously. The market already has enough caveats stapled to weak claims.
