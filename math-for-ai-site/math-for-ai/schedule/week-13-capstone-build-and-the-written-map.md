---
title: "Week 13: Capstone build and the written map"
week: 13
dates: "30 Nov – 6 Dec 2026"
phase: "4 — Consolidation"
books:
  - Calculus
  - Linear Algebra
  - Statistics
tags:
  - schedule
  - phase-4
  - calc
  - la
  - stat
---

## Read

| Book | Chapters | Priority |
|---|---|---|
| Linear Algebra | Re-work missed supplementary problems from Weeks 4, 8 and 10 | Core |
| Statistics | Same | Core |
| Calculus | Same | Core |

## Where it lives in AI

Mon–Tue: redo the problems you got wrong or skipped in the three checkpoint weeks. Wed–Fri: the capstone. Sat: write a two-page document in your own words giving, for each chapter studied, one line on where it appears in a modern AI stack. Sun: pick the next gap to fill.

## Build (Friday)

A single-head self-attention block in NumPy only: token embeddings plus sinusoidal positions (Wk 1, 11), Q/K/V projections (Wk 3), scaled dot-product scores (Wk 1, 4), softmax with log-sum-exp (Wk 3), a residual connection and LayerNorm (Wk 4), cross-entropy loss with hand-derived gradients for the output layer (Wk 7, 8), trained with SGD plus momentum (Wk 6, 9) on a toy next-token task. Then reduce the attention weight matrices with SVD (Wk 10) and measure how much rank you can remove before loss degrades.

---
[← Week 12](week-12-differential-equations-and-the-dynamics-of-generative-models.md) · [All weeks](../schedule.md)
