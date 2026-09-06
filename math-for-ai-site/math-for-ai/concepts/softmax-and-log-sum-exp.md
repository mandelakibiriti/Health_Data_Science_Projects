---
title: Softmax and the log-sum-exp trick
summary: Turning a vector of scores into a probability distribution without numerical overflow.
tags:
  - exponential
  - logarithm
  - probability
  - calculus
weeks:
  - 3
source: Calculus, Ch 25–26 (natural logarithm, exponential functions); Statistics, Ch 6 (probability distributions)
---

## Definition

For a vector of scores (logits) $z \in \mathbb{R}^K$,

$$\operatorname{softmax}(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

Each output lies in $(0, 1)$ and they sum to $1$, so the result is a probability distribution over $K$ classes. Softmax is invariant to adding the same constant to every $z_i$.

## Essential result

Because $e^{z}$ overflows double precision near $z \approx 710$ (and half precision near $z \approx 11$), the naive formula fails on large logits. Using the shift invariance with $m = \max_j z_j$,

$$\log \sum_j e^{z_j} = m + \log \sum_j e^{z_j - m}$$

Every exponent is now $\le 0$, so nothing overflows, and at least one term equals $e^0 = 1$, so the sum cannot underflow to zero. The log of softmax is then $z_i - \operatorname{logsumexp}(z)$, which is what cross-entropy loss actually computes.

## Where it lives in AI

- **The output layer of every classifier and language model.** Next-token prediction is a softmax over the vocabulary.
- **Attention weights.** Row-wise softmax of $QK^\top/\sqrt{d}$ turns similarity scores into a weighted average of value vectors.
- **Cross-entropy loss** is $-\log \operatorname{softmax}(z)_y$; frameworks fuse the two into one numerically stable operation for exactly the reason above.
- **Sampling temperature.** Dividing logits by $T$ before softmax sharpens ($T < 1$) or flattens ($T > 1$) the distribution.
- **Log-domain computation** more generally: probabilities of sequences are summed as log-probabilities to avoid underflow.

## Related

- [Cosine similarity](cosine-similarity.md)
- [Chain rule and backpropagation](chain-rule-and-backpropagation.md)
- Week 3 of the [schedule](../schedule.md)
