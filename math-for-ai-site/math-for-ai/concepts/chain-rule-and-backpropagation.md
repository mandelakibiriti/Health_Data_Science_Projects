---
title: Chain rule and backpropagation
summary: The multivariable chain rule is the algorithm that trains every neural network.
tags:
  - partial-derivatives
  - chain-rule
  - calculus
  - optimisation
weeks:
  - 8
  - 9
source: Calculus, Ch 48 (partial derivatives) and Ch 49 (total differential, chain rules)
---

## Definition

If $y = f(u_1, \dots, u_m)$ and each $u_j = g_j(x_1, \dots, x_n)$, then

$$\frac{\partial y}{\partial x_i} = \sum_{j=1}^{m} \frac{\partial y}{\partial u_j}\,\frac{\partial u_j}{\partial x_i}$$

In matrix form, with Jacobians, the derivative of a composition is the product of the Jacobians of its parts, taken in order.

## Essential result

A neural network is a composition $L = \ell \circ f_K \circ \cdots \circ f_1$. Applying the chain rule from the loss backwards, each layer receives $\partial L / \partial(\text{its output})$, multiplies by its own local Jacobian, and passes $\partial L / \partial(\text{its input})$ to the layer before. Because the loss is a scalar, this vector–Jacobian product never materialises a full Jacobian, so the backward pass costs about the same as the forward pass regardless of the number of parameters.

## Where it lives in AI

- **Backpropagation** is this procedure; **automatic differentiation** (PyTorch autograd, JAX) applies it mechanically over a recorded computation graph.
- **Vanishing and exploding gradients** are the product of many Jacobians shrinking or growing; residual connections add an identity term to each Jacobian so the product stays near $1$.
- **Gradient checkpointing** trades recomputation of forward activations for memory, because the backward pass needs them.
- **The total differential** $dL \approx \nabla L \cdot dw$ is the first-order model of the loss that gradient descent relies on when it takes a step.

## Related

- [Softmax and the log-sum-exp trick](softmax-and-log-sum-exp.md)
- Weeks 8 and 9 of the [schedule](../schedule.md)
