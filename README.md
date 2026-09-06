# Math for AI

A 13-week study path through four Schaum's Outlines — *Linear Algebra*, *Calculus*, *Statistics*, and *Advanced Mathematics for Engineers and Scientists* — organised around one question: which mathematics do you need to understand, and to build, AI systems from classical machine learning through transformers and diffusion models?

This folder is laid out like [Algebrica](https://github.com/antoniolupetti/algebrica): Markdown entries with front matter, one per topic, so the content is readable on GitHub and also buildable as a GitHub Pages site.

## Layout

| Path | What it holds |
|---|---|
| `README.md` | This page: the full schedule |
| `schedule/` | One entry per week — chapters, AI relevance, build exercise |
| `concepts/` | Algebrica-style entries, one per mathematical idea, each ending with where it appears in AI |
| `notebooks/` | The Friday build exercises as Jupyter notebooks (NumPy only) |
| `assets/` | A standalone HTML version of the schedule with per-week checkboxes |
| `_config.yml`, `index.md`, `*.md` | Jekyll site scaffolding for GitHub Pages |

## How to use the four books

Schaum's Outlines are not meant to be read cover to cover. Each chapter opens with a compressed theory summary, then earns its keep through solved problems. Read the summary once, work three to five solved problems with the solution covered, then attempt five to eight supplementary problems. Roughly 40% of the total page count is scheduled here; the rest is prerequisite refresher or engineering material with little bearing on AI.

| Book | Role | Scheduled |
|---|---|---|
| Linear Algebra (4th ed., Lipschutz & Lipson) | The most important of the four | 9 of 13 chapters |
| Calculus (5th ed., Ayres & Mendelson) | Short chapters, used selectively | ~25 of 59 chapters |
| Statistics (Spiegel & Stephens) | Descriptive statistics through least squares | Ch 1–15 of 18 |
| Advanced Mathematics for Engineers & Scientists (Spiegel) | Vector analysis, Fourier, ODEs, special functions, calculus of variations | 8 of 16 chapters |

Priority labels: **Core** = do the solved problems · **Skim** = read the theory summary only · **Optional** = if time allows.

## Weekly rhythm (about 10 hours)

| Day | Block | What |
|---|---|---|
| Mon–Thu | 75–90 min each | Theory summary of the assigned chapter, then solved problems. Keep a notebook of definitions in your own words. |
| Fri | 90 min | The Build exercise in Python/NumPy, so the mathematics becomes code you have typed. |
| Sat | 2 h | Supplementary problems from the week's chapters — aim for 10–15 across all books. |
| Sun | 30 min | Review the notebook, tick the week off, note what still feels shaky. Rest. |

## The schedule


### Phase 1 · The substrate (Weeks 1–4)

#### Week 1 — 7–13 Sep: [Vectors, dot products, and the algebra of matrices](schedule/week-01-vectors-dot-products-and-the-algebra-of-matrices.md)

| Book | Chapters | Priority |
|---|---|---|
| LinAlg | Ch 1 Vectors in Rⁿ (1.1–1.6) | Core |
| LinAlg | 1.7–1.8 complex vectors | Skim |
| LinAlg | Ch 2 Algebra of Matrices (2.1–2.10, 2.12 block matrices) | Core |
| Calc | Ch 6 Functions, Ch 7 Limits, Ch 8 Continuity | Skim |
| Calc | Ch 9 The Derivative, Ch 10 Differentiation Rules | Core (refresher) |

**Where it lives in AI.** A tensor is a stack of matrices; every dense layer, attention score and embedding lookup is matrix multiplication. The dot product is similarity, which is what a vector database computes when it ranks retrieved passages for a RAG system. Block matrices are how multi-head attention concatenates heads and how weight matrices are sharded across GPUs. Summation notation (2.4) is the notation of every paper you will read.

**Build.** Implement matrix multiplication with explicit loops, then with `np.einsum`, and confirm they agree. Write `cosine_similarity(a, b)` and rank a handful of hand-made "embedding" vectors against a query.

#### Week 2 — 14–20 Sep: [Solving systems, and the idea of a vector space](schedule/week-02-solving-systems-and-the-idea-of-a-vector-space.md)

| Book | Chapters | Priority |
|---|---|---|
| LinAlg | Ch 3 Systems of Linear Equations (3.1–3.11 Gaussian elimination, echelon form; 3.13 LU decomposition) | Core |
| LinAlg | Ch 4 Vector Spaces (4.2–4.9 span, subspaces, independence, basis, dimension, rank) | Core |
| LinAlg | 4.10–4.11 | Skim |
| Calc | Ch 11 Implicit Differentiation, Ch 13 Mean Value Theorem, Ch 14 Maxima and Minima | Core |

**Where it lives in AI.** Rank is the single most useful idea this week. LoRA fine-tunes a large model by learning a low-rank update $W + BA$ instead of a full matrix, and that only makes sense once rank and dimension are intuitive. Linear independence explains why collinear features break linear regression and why embedding dimensions can be "wasted". Basis and coordinates are what a tokenizer plus embedding table actually produce: a coordinate vector in a learned basis.

**Build.** Solve a small linear system by hand with row reduction, then check with `np.linalg.solve`. Build a random 512×512 matrix as `B @ A` with rank 8, confirm it with `np.linalg.matrix_rank`, and count the parameters saved versus the full matrix.

#### Week 3 — 21–27 Sep: [Linear maps, change of basis, and exp/log](schedule/week-03-linear-maps-change-of-basis-and-exp-log.md)

| Book | Chapters | Priority |
|---|---|---|
| LinAlg | Ch 5 Linear Mappings (5.2–5.6 kernel, image, isomorphisms) | Core |
| LinAlg | Ch 6 Linear Mappings and Matrices (6.2–6.4 matrix representation, change of basis, similarity) | Core |
| Calc | Ch 25 Natural Logarithm, Ch 26 Exponential and Logarithmic Functions | Core |
| Calc | Ch 27 L'Hôpital's Rule, Ch 28 Exponential Growth and Decay | Skim |

**Where it lives in AI.** A neural network layer is a linear map followed by a pointwise non-linearity; the kernel of that map is the information the layer discards. Change of basis is what a projection head does, what PCA does, and what "rotating" an embedding space means in interpretability work. Exponential and logarithm underpin softmax, log-likelihood, cross-entropy and the log-sum-exp trick that keeps training numerically stable. Exponential decay is your learning-rate schedule.

**Build.** Apply a 2×2 matrix to a grid of points and plot before/after to see a linear map as a geometric deformation. Implement `softmax` naively, watch it overflow on large logits, then fix it with the log-sum-exp shift.

#### Week 4 — 28 Sep – 4 Oct: [Inner products, norms, orthogonality, determinants, integrals](schedule/week-04-inner-products-norms-orthogonality-determinants-integrals.md)

| Book | Chapters | Priority |
|---|---|---|
| LinAlg | Ch 7 Inner Product Spaces (7.2–7.8 Cauchy–Schwarz, orthogonal bases, Gram–Schmidt, positive definite matrices; 7.10 normed spaces) | Core |
| LinAlg | Ch 8 Determinants (8.1–8.10; 8.13 determinants and volume) | Core |
| LinAlg | Ch 8 remaining sections | Optional |
| Calc | Ch 22 Antiderivatives, Ch 23 Definite Integral, Ch 24 Fundamental Theorem | Core |

**Where it lives in AI.** Norms are everywhere: L2 weight decay, L1 sparsity, gradient clipping, LayerNorm and RMSNorm, and the unit-normalised embeddings that make cosine similarity a plain dot product. Cauchy–Schwarz is why cosine similarity lies in $[-1, 1]$. Orthogonal matrices preserve norms, which is why orthogonal initialisation helps deep networks train. The determinant as a volume factor is the key to normalising flows. Integrals are expectations, and expectations are what every loss function really is.

**Build.** Implement Gram–Schmidt and verify $Q^\top Q = I$. Implement LayerNorm from the formula. Compute the determinant of a random 2×2 matrix and measure how it scales the area of a unit square.

> **Phase 1 checkpoint.** You should be able to explain without notes: what rank means for LoRA, why softmax needs the log-sum-exp shift, and what LayerNorm computes and why.


### Phase 2 · Learning from data (Weeks 5–8)

#### Week 5 — 5–11 Oct: [Describing data, and probability from first principles](schedule/week-05-describing-data-and-probability-from-first-principles.md)

| Book | Chapters | Priority |
|---|---|---|
| Stats | Ch 1 Variables and Graphs, Ch 2 Frequency Distributions | Skim |
| Stats | Ch 3 Mean, Median, Mode; Ch 4 Standard Deviation and Dispersion | Core |
| Stats | Ch 5 Moments, Skewness, Kurtosis | Core |
| Stats | Ch 6 Elementary Probability Theory (conditional probability, independence, Bayes, random variables, expectation, combinatorics) | Core — heaviest week in this book |

**Where it lives in AI.** Standardisation (subtract the mean, divide by the standard deviation) is the first thing done to features and is exactly what BatchNorm computes on activations. Moments are the language of distribution shift; skew and kurtosis tell you when a Gaussian assumption is lying. Bayes' theorem is naive Bayes, Bayesian hyperparameter optimisation, the posterior in a VAE, and the right way to read a model's predicted probability against a base rate. Expectation is the operator inside every loss: training minimises expected loss over the data distribution.

**Build.** Take any tabular dataset, compute mean, std, skew and kurtosis per column, and standardise it. Implement Bayes' rule for a diagnostic-test problem (prior, sensitivity, specificity) and plot posterior against prior.

#### Week 6 — 12–18 Oct: [Distributions, sampling, and the central limit theorem](schedule/week-06-distributions-sampling-and-the-central-limit-theorem.md)

| Book | Chapters | Priority |
|---|---|---|
| Stats | Ch 7 Binomial, Normal, and Poisson Distributions | Core |
| Stats | Ch 8 Elementary Sampling Theory (sampling distributions, standard error, CLT) | Core |
| Calc | Ch 35 Improper Integrals | Core — needed for the normal density |
| Calc | Ch 42 Sequences, Ch 43 Infinite Series | Skim |

**Where it lives in AI.** The Bernoulli/binomial is a sigmoid output and binary cross-entropy. The Gaussian is weight initialisation, the noise added at each step of a diffusion model, the latent prior of a VAE, and the assumption behind mean-squared-error loss. Poisson models counts. The central limit theorem is why a minibatch gradient is approximately the true gradient plus Gaussian noise — the justification for SGD and the reason batch size trades off against noise.

**Build.** Draw samples from a skewed distribution, average them in batches of 1, 8, 64 and 512, and watch the histogram of batch means turn Gaussian with standard error shrinking as $1/\sqrt{n}$. Overlay the normal density you integrated by hand.

#### Week 7 — 19–25 Oct: [Estimation, decisions, and testing whether a model is better](schedule/week-07-estimation-decisions-and-testing-whether-a-model-is-better.md)

| Book | Chapters | Priority |
|---|---|---|
| Stats | Ch 9 Statistical Estimation Theory (unbiased and efficient estimators, confidence intervals) | Core |
| Stats | Ch 10 Statistical Decision Theory (hypotheses, Type I/II errors, power, p-values) | Core |
| Stats | Ch 11 Small Sampling Theory (t and chi-square distributions) | Core |
| Stats | Ch 12 The Chi-Square Test | Skim |

**Where it lives in AI.** Maximum likelihood estimation is model training: minimising negative log-likelihood is fitting parameters, and cross-entropy loss is MLE for a categorical output. Confidence intervals are what an honest evaluation reports; a 0.4-point gain on a 500-example eval is usually noise. Type I and II errors map to false positives and negatives and to the threshold you set on a classifier. Chi-square tests check whether a feature and a label are independent, or whether an LLM's output categories differ between two prompts.

**Build.** Bootstrap a 95% confidence interval for the accuracy of a classifier on a held-out set. Simulate two models with true accuracies 0.80 and 0.82 on 500 examples and count how often a paired test can tell them apart.

#### Week 8 — 26 Oct – 1 Nov: [Least squares, correlation, and the multivariable chain rule](schedule/week-08-least-squares-correlation-and-the-multivariable-chain-rule.md)

| Book | Chapters | Priority |
|---|---|---|
| Stats | Ch 13 Curve Fitting and Least Squares | Core |
| Stats | Ch 14 Correlation Theory | Core |
| Stats | Ch 15 Multiple and Partial Correlation | Skim |
| Calc | Ch 48 Partial Derivatives | Core |
| Calc | Ch 49 Total Differential, Differentiability, Chain Rules | Core — read twice |
| Calc | Ch 47 Taylor and Maclaurin Series | Core |

**Where it lives in AI.** Least-squares linear regression is the first machine-learning model, and the normal equations tie it back to Week 2. Correlation versus causation is the discipline behind feature selection and behind reading any evaluation. The multivariable chain rule *is* backpropagation: automatic differentiation is a machine that applies Ch 49 across a computation graph. The total differential is a first-order Taylor expansion, which is what gradient descent assumes about the loss near the current weights.

**Build.** Fit linear regression three ways: the normal equations, gradient descent with hand-derived partial derivatives, and `np.polyfit`. Then differentiate a small two-layer network by hand with the chain rule and check against finite differences.

> **Phase 2 checkpoint.** You should be able to derive cross-entropy loss from maximum likelihood, explain why SGD works from the CLT, and compute the gradients of a two-layer network by hand.


### Phase 3 · Structure and dynamics (Weeks 9–12)

#### Week 9 — 2–8 Nov: [Gradients, curvature, and constrained optimisation](schedule/week-09-gradients-curvature-and-constrained-optimisation.md)

| Book | Chapters | Priority |
|---|---|---|
| Calc | Ch 50 Space Vectors; Ch 52 Directional Derivatives and Extrema (gradient, Hessian test, Lagrange multipliers) | Core |
| Calc | Ch 21 Differentials and Newton's Method | Core |
| AdvMath | Ch 16 Calculus of Variations (Euler's equation, constraints, Lagrange multipliers) | Skim theory; problems optional |

**Where it lives in AI.** The negative gradient is the descent direction; the directional derivative says how much a step in any direction changes the loss. The Hessian describes curvature: sharp versus flat minima, why Adam rescales per parameter, why second-order methods are expensive. Newton's method is the ancestor of every quasi-Newton optimiser. Lagrange multipliers turn constrained problems into unconstrained ones — how SVMs are derived, and how a KL penalty in PPO or RLHF keeps a fine-tuned policy close to its base model.

**Build.** Write gradient descent with numerical gradients on the Rosenbrock function and plot the path; add momentum and compare. Solve "maximise $xy$ subject to $x + y = 10$" with a Lagrange multiplier and by substitution.

#### Week 10 — 9–15 Nov: [Eigenvalues, the spectral theorem, and singular values](schedule/week-10-eigenvalues-the-spectral-theorem-and-singular-values.md)

| Book | Chapters | Priority |
|---|---|---|
| LinAlg | Ch 9 Diagonalization: Eigenvalues and Eigenvectors (9.1–9.6) | Core — the most important chapter in the four books |
| LinAlg | Ch 12 Bilinear, Quadratic, Hermitian Forms (12.5–12.6 quadratic forms, law of inertia) | Core |
| LinAlg | Ch 13 Linear Operators on Inner Product Spaces (13.4–13.10 self-adjoint, orthogonal/unitary, positive definite, spectral theorem) | Core |
| AdvMath | Ch 15 Matrices (eigenvalue theorems) | Skim — a second angle |
| LinAlg | Ch 10 Canonical Forms, Ch 11 Dual Space | Optional |

**Where it lives in AI.** PCA is the eigendecomposition of a covariance matrix. Applying the spectral theorem to $A^\top A$ gives the singular value decomposition, which none of the four books names but which you can now derive; SVD is low-rank approximation, model compression, the initialisation of some LoRA variants, and the way to read what an attention head does. Eigenvalues of the Hessian are last week's curvature. The spectral norm bounds how much a layer can stretch an input (Lipschitz control). Eigenvectors of a transition matrix give PageRank and stationary distributions; eigenvectors of a graph Laplacian are what graph neural networks operate on.

**Build.** Implement PCA via `np.linalg.eigh` on the covariance matrix and via SVD of the centred data; confirm they match. Compress a grayscale image by keeping the top-$k$ singular values and plot error against $k$. Implement power iteration and recover the dominant eigenvector.

#### Week 11 — 16–22 Nov: [Multiple integrals, vector calculus, and Fourier](schedule/week-11-multiple-integrals-vector-calculus-and-fourier.md)

| Book | Chapters | Priority |
|---|---|---|
| Calc | Ch 54 Double and Iterated Integrals, Ch 57 Triple Integrals | Core theory, light on problems |
| AdvMath | Ch 5 Vector Analysis (gradient, divergence, Jacobian, change of variables) | Core |
| AdvMath | Ch 6 Multiple, Line and Surface Integrals | Skim |
| AdvMath | Ch 7 Fourier Series | Core |
| AdvMath | Ch 8 Fourier Integrals | Skim |

**Where it lives in AI.** Multiple integrals are marginalisation: $p(x) = \int p(x, z)\,dz$ is the intractable quantity that VAEs bound with the ELBO and that diffusion models sidestep. The Jacobian and the change-of-variables formula are the whole mechanism of normalising flows. Fourier series explain sinusoidal positional encodings and RoPE in transformers, why a convolution is a multiplication in frequency space, why networks learn low frequencies first, and what a spectrogram is before an audio model sees it.

**Build.** Generate the sinusoidal positional-encoding matrix from the transformer paper's formula and plot it as a heatmap; check that nearby positions have higher dot products. Verify the convolution theorem with `np.fft` on a 1-D signal. Monte-Carlo estimate a double integral and compare with the iterated integral.

#### Week 12 — 23–29 Nov: [Differential equations and the dynamics of generative models](schedule/week-12-differential-equations-and-the-dynamics-of-generative-models.md)

| Book | Chapters | Priority |
|---|---|---|
| AdvMath | Ch 2 Ordinary Differential Equations (first-order, separable, linear) | Core |
| AdvMath | Ch 3 Linear Differential Equations | Skim |
| Calc | Ch 59 Differential Equations of First and Second Order | Core — the gentler version |
| AdvMath | Ch 9 Gamma, Beta and Other Special Functions | Core theory |
| AdvMath | Ch 4 Laplace Transforms, Ch 12 Partial Differential Equations | Optional |

**Where it lives in AI.** Gradient descent with a small step is Euler's method on the ODE $dw/dt = -\nabla L$, and learning-rate schedules are its time-stepping; neural ODEs make that literal. Diffusion models add Gaussian noise through a first-order linear stochastic differential equation and generate by integrating it backwards — the sampler you choose (DDIM, Euler, Heun) is an ODE solver from this chapter. Exponential moving averages of weights and Adam's moment estimates are discretised first-order linear ODEs. The gamma and beta functions define the Beta and Dirichlet distributions used as Bayesian priors.

**Build.** Simulate the forward diffusion process on 1-D data with the closed-form noising formula and watch the distribution become standard normal. Implement Euler and Heun steps on a simple ODE and compare error. Plot the Beta distribution for several parameter pairs using the beta function.


### Phase 4 · Consolidation (Week 13)

#### Week 13 — 30 Nov – 6 Dec: [Capstone build and the written map](schedule/week-13-capstone-build-and-the-written-map.md)

| Book | Chapters | Priority |
|---|---|---|
| LinAlg | Re-work missed supplementary problems from Weeks 4, 8 and 10 | Core |
| Stats | Same | Core |
| Calc | Same | Core |

**Where it lives in AI.** Mon–Tue: redo the problems you got wrong or skipped in the three checkpoint weeks. Wed–Fri: the capstone. Sat: write a two-page document in your own words giving, for each chapter studied, one line on where it appears in a modern AI stack. Sun: pick the next gap to fill.

**Build.** A single-head self-attention block in NumPy only: token embeddings plus sinusoidal positions (Wk 1, 11), Q/K/V projections (Wk 3), scaled dot-product scores (Wk 1, 4), softmax with log-sum-exp (Wk 3), a residual connection and LayerNorm (Wk 4), cross-entropy loss with hand-derived gradients for the output layer (Wk 7, 8), trained with SGD plus momentum (Wk 6, 9) on a toy next-token task. Then reduce the attention weight matrices with SVD (Wk 10) and measure how much rank you can remove before loss degrades.

## What these four books do not cover

The Schaum's set is strong on the classical core and silent on several things a modern AI engineer needs. Fill these after Week 13 — the free textbook *Mathematics for Machine Learning* (Deisenroth, Faisal & Ong) covers most of them, as do the Stanford CS229 lecture notes.

| Gap | Why it matters |
|---|---|
| Information theory | Entropy, cross-entropy, KL divergence, mutual information — the language of LM losses and RLHF objectives |
| Singular value decomposition, named | Derivable from Week 10 but never stated as its own topic |
| Multivariate Gaussian | Covariance, Mahalanobis distance, conditioning and marginalising — Gaussian processes, Kalman filters, diffusion |
| Markov chains and MDPs | Stationary distributions, Bellman equations, policy gradients — RL, RLHF, agents |
| Matrix calculus notation | Jacobians of matrix-valued functions and the layout conventions used in papers and autodiff |
| Convex optimisation | Convex sets and functions, duality, KKT — when a training problem has a unique answer |
| Numerical stability | Floating point, conditioning, mixed precision — why fp16 diverges and bf16 does not |
| Measure-theoretic probability | Optional; for reading SDE and score-matching theory rigorously |

## Chapter-to-AI map

| Mathematics | Classical ML | Deep learning | Generative AI and LLMs |
|---|---|---|---|
| Matrix algebra, rank | Linear/logistic regression, feature matrices | Dense layers, batching, GPU kernels | Attention scores, LoRA, quantisation |
| Inner products, norms | k-NN, SVM kernels, regularisation | LayerNorm, gradient clipping, weight decay | Embedding retrieval, RAG, contrastive learning |
| Eigen/SVD, quadratic forms | PCA, spectral clustering, ridge regression | Hessian curvature, spectral norm, initialisation | Low-rank adapters, compression, head analysis |
| Derivatives, chain rule, Taylor | Gradient descent, Newton's method | Backpropagation, autodiff, Adam | Training stability, LR schedules |
| Lagrange multipliers | SVM dual, constrained least squares | Constrained fine-tuning | KL penalties in PPO / RLHF / DPO |
| Probability, Bayes, expectation | Naive Bayes, Bayesian inference, expected risk | Dropout as noise, calibration | Sampling temperature, top-p, posterior over latents |
| Distributions, CLT | MLE, generalised linear models | Init schemes, SGD noise, BatchNorm | Gaussian noise in diffusion, VAE prior |
| Estimation and testing | Cross-validation, confidence intervals | Error bars on results | LLM evals, A/B tests, win-rate significance |
| Multiple integrals, Jacobians | Marginal likelihood | Normalising flows | ELBO, VAEs, change of variables in samplers |
| Fourier analysis | Signal features, kernels | Convolutions, spectral bias | Positional encodings, RoPE, audio/vision tokens |
| Differential equations | Dynamical-systems view of GD | Neural ODEs, EMA of weights | Diffusion SDE/ODE, samplers (DDIM, Euler, Heun) |

## Publishing as a GitHub Pages site

1. Copy this folder and `.github/workflows/pages.yml` into the repo.
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push to `main`. The workflow builds `math-for-ai/` with Jekyll and deploys it to `https://mandelakibiriti.github.io/Health_Data_Science_Projects/`.

To preview locally: `cd math-for-ai && bundle install && bundle exec jekyll serve`.

## Adding content

- **A new week or revision:** edit the file in `schedule/`; the schedule index page picks it up automatically.
- **A concept entry:** copy `concepts/_template.md`, fill in the front matter (`title`, `summary`, `tags`, `weeks`), and write. Equations use `$...$` and `$$...$$` (MathJax).
- **A notebook:** save it as `notebooks/week-NN-description.ipynb` and add a line to `notebooks.md`.

Built 6 September 2026. Chapter numbers refer to the editions listed above.
