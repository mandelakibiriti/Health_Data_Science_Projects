---
title: Rank and low-rank adaptation (LoRA)
summary: Why a weight update can be factored into two thin matrices, and what that saves.
tags:
  - rank
  - vector-spaces
  - linear-algebra
weeks:
  - 2
  - 10
source: Linear Algebra, Ch 4 (4.9 rank of a matrix) and Ch 13 (spectral theorem, from which SVD follows)
---

## Definition

The rank of a matrix $A \in \mathbb{R}^{m \times n}$ is the dimension of its column space, equivalently the number of linearly independent rows or columns. A matrix of rank $r$ can always be written as a product

$$A = B\,C, \qquad B \in \mathbb{R}^{m \times r},\; C \in \mathbb{R}^{r \times n}$$

which stores $r(m + n)$ numbers instead of $mn$.

## Essential result

The singular value decomposition $A = U \Sigma V^\top$ orders the "directions" of $A$ by importance. Keeping the top $r$ singular values gives the best rank-$r$ approximation of $A$ in both the Frobenius and spectral norms (Eckart–Young). Empirically, the change a fine-tuning run makes to a large weight matrix has low intrinsic rank — most of the update lives in a few directions.

## Where it lives in AI

- **LoRA.** Instead of updating a $d \times d$ weight $W$, freeze it and learn $\Delta W = BA$ with $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times d}$, $r \ll d$. For $d = 4096$ and $r = 8$ that is $65{,}536$ trainable parameters instead of $16.8$ million — a $256\times$ reduction per matrix, and the adapter can be merged back with one addition at inference.
- **Model compression** by truncated SVD of weight matrices.
- **Feature engineering.** Rank-deficient design matrices mean collinear features; the normal equations of least squares become ill-conditioned.
- **Interpretability.** SVD of an attention head's $W_Q W_K^\top$ reveals which directions of the residual stream the head compares.

## Related

- [Cosine similarity](cosine-similarity.md)
- Weeks 2 and 10 of the [schedule](../schedule.md)
