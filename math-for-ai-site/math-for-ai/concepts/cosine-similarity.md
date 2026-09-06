---
title: Cosine similarity
summary: The dot product of two unit vectors; the metric behind embedding search and retrieval.
tags:
  - inner-product
  - vectors
  - linear-algebra
weeks:
  - 1
  - 4
source: Linear Algebra, Ch 1 (1.4 dot product) and Ch 7 (7.4 Cauchy–Schwarz)
---

## Definition

For non-zero vectors $a, b \in \mathbb{R}^n$,

$$\cos\theta = \frac{a \cdot b}{\lVert a \rVert\,\lVert b \rVert} = \frac{\sum_i a_i b_i}{\sqrt{\sum_i a_i^2}\,\sqrt{\sum_i b_i^2}}$$

where $\theta$ is the angle between them. It depends only on direction, not on magnitude.

## Essential result

The Cauchy–Schwarz inequality $|a \cdot b| \le \lVert a \rVert \lVert b \rVert$ guarantees $-1 \le \cos\theta \le 1$, with equality exactly when one vector is a scalar multiple of the other. If both vectors are normalised to unit length in advance, cosine similarity reduces to a plain dot product, and the search over a matrix of $N$ stored vectors $E$ is one matrix–vector product $E q$.

## Where it lives in AI

- **Retrieval-augmented generation.** A vector database stores normalised passage embeddings and ranks them against a query embedding by cosine similarity; the top-$k$ passages go into the prompt.
- **Contrastive learning.** CLIP and sentence-embedding models are trained so that matching pairs have high cosine similarity and mismatched pairs low, using a softmax over similarities scaled by a temperature.
- **Attention scores.** Scaled dot-product attention $QK^\top / \sqrt{d}$ is an unnormalised cousin: the same dot product, without dividing by the norms, with the $\sqrt{d}$ factor controlling variance instead.
- **Deduplication and clustering** of documents, embeddings, or model outputs.

## Related

- [Softmax and the log-sum-exp trick](softmax-and-log-sum-exp.md)
- Weeks 1 and 4 of the [schedule](../schedule.md)
