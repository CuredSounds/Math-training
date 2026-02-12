# Math Foundations for ML & Data Science — Training System

<aside>
🎯

**Goal:** Build strong, practical intuition and problem-solving skill in **statistics, probability, calculus, and linear algebra** for machine learning and data science.

**How to use:** Follow the weekly cycles, track progress in the dashboard, and ship small projects.

</aside>

### The system (how you will learn)

**Weekly cycle (repeat every week):**

- **Day 1 (Learn):** Read/watch + make concise notes (definitions, key formulas, “when to use”).
- **Day 2 (Do):** 15–30 targeted practice problems.
- **Day 3 (Apply):** 1 small notebook lab (simulate, visualize, or implement).
- **Day 4 (Explain):** Write a 5–10 sentence explanation as if teaching.
- **Day 5 (Assess):** Quiz yourself: 10 questions, no notes. Log weak spots.
- **Day 6 (Review):** Fix mistakes, re-do missed problems, create flashcards.
- **Day 7 (Rest / light recap).**

**Rules of thumb:**

- Prefer *doing* over consuming content.
- Every topic ends with an **ML link** (why this matters for models).
- Keep a “mistake log”: concept, error type, corrected approach.

---

### Dashboard

[Learning Dashboard](Math%20Foundations%20for%20ML%20&%20Data%20Science%20%E2%80%94%20Training%20/Learning%20Dashboard%20547aa6b5414b43ce834ccdbf72acf745.csv)

---

### Curriculum map (what to learn)

### Module 0 — Setup and baseline (1 week)

- Skills: algebra refresh, logs/exponents, sums, basic functions.
- Tools: Python + Jupyter, NumPy, Matplotlib/Seaborn.
- Output: one notebook that generates and visualizes synthetic datasets.

### Module 1 — Data types, distributions, and visualization (2 weeks)

- **Qualitative vs quantitative data** (nominal, ordinal, interval, ratio).
- Describing distributions: center, spread, skew, outliers.
- Visuals: histograms, KDE, box plots, scatter plots, QQ plots.
- ML link: why distribution shape matters for scaling, loss functions, and model assumptions.
- Output lab: EDA notebook on a public dataset (with clear plots and written interpretation).

### Module 2 — Probability foundations (3 weeks)

- Events, sample spaces, conditional probability.
- Bayes’ rule and base rates.
- Random variables; expectation and variance.
- Common distributions: Bernoulli, Binomial, Geometric, Poisson, Uniform, Normal, Exponential.
- Law of large numbers; central limit theorem.
- ML link: Naive Bayes, calibration, uncertainty, noise modeling.
- Output lab: simulate the CLT and visualize convergence.

### Module 3 — Statistics and inference (4 weeks)

- Sampling, estimators, bias/variance intuition.
- Confidence intervals and bootstrapping.
- Hypothesis testing: null/alternative, test statistics.
- p-values, Type I/II errors, power, multiple testing.
- Checking assumptions: normality (visual + tests), independence, equal variance.
- ML link: evaluation, A/B tests, offline metrics, overfitting vs generalization.
- Output lab: bootstrap CI + hypothesis test on a dataset; interpret results.

### Module 4 — Research questions and study design (1–2 weeks)

- Crafting questions with **PICOT/PECOT**.
- Outcomes, exposures/interventions, confounders.
- Translating questions into testable hypotheses and analysis plans.
- ML link: defining target variable, leakage checks, causal vs predictive framing.
- Output: 3 research questions + analysis plans for 1 dataset.

### Module 5 — Calculus for optimization (4 weeks)

- Functions, limits (as needed), derivatives.
- Chain rule, partial derivatives, gradients.
- Taylor approximation (intuition).
- Optimization: critical points, convexity basics.
- Gradient descent and learning rates.
- ML link: training neural nets, logistic regression, regularization.
- Output lab: implement gradient descent for linear and logistic regression from scratch.

### Module 6 — Linear algebra for ML (4 weeks)

- Vectors, matrices, norms, dot products.
- Linear transformations; projections.
- Eigenvalues/eigenvectors; SVD intuition.
- Least squares and normal equations.
- ML link: PCA, embeddings, regularization, matrix factorization.
- Output lab: PCA from scratch + compare to sklearn.

### Module 7 — Putting it together (2–3 weeks)

- From question → data → assumptions → model → evaluation.
- Error analysis: data issues vs model issues.
- Communicating results: visual + written story.
- Output: one end-to-end project with a clear report.

---

### Statistical procedure checklist (use for any analysis)

- [ ]  Define the question and target metric.
- [ ]  Identify variable types and units.
- [ ]  Inspect distributions and missingness.
- [ ]  Choose an approach (estimation, test, model) and justify assumptions.
- [ ]  Check assumptions (normality, independence, variance, etc.).
- [ ]  Set hypotheses and significance level (if testing).
- [ ]  Compute estimate / test statistic and p-value (or CI).
- [ ]  Interpret practical significance (effect size), not only p-value.
- [ ]  Run sensitivity checks (alternative tests, bootstrap, robust metrics).
- [ ]  Document decisions and limitations.

---

### Common errors to actively avoid

- Overreliance on p-values without effect sizes or CIs.
- Ignoring multiple comparisons.
- Confusing correlation with causation.
- Data leakage (using future info or target proxies).
- Overfitting via repeated peeking and tuning.
- Misreading charts (axes, binning artifacts, small samples).

---

### Tools and apps (practical stack)

- **Python**: Jupyter, NumPy, pandas, SciPy, statsmodels, scikit-learn.
- **R (optional)**: RStudio + tidyverse for stats-heavy workflows.
- **Visualization**: Matplotlib/Seaborn or ggplot2.
- **Math practice**: a problem set source + a spaced repetition tool.

<aside>
✅

If you tell me your current level (e.g., “comfortable with algebra, rusty on calculus”), and how many hours per week you can commit, I can map this into a specific 8–16 week schedule.

</aside>