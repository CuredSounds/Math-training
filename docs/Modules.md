# Learning Modules Curriculum

This document defines the core modules for the "Lab in a Box" training system. Each module is a self-contained learning unit with a specific focus, set of tools, and target outcomes.

## 1. Math Foundations for ML & Data Science
**Goal:** Build the mathematical intuition required for understanding machine learning algorithms.
- **Topics:**
  - **Calculus:** Derivatives, Gradients, Chain Rule, Optimization (Gradient Descent).
  - **Linear Algebra:** Vectors, Matrices, Dot Products, Eigenvalues/Eigenvectors.
  - **Probability:** Distributions, Bayes Theorem, Expectation, Variance.
  - **Statistics:** Hypothesis Testing, Confidence Intervals, p-values.
- **Tools:** `numpy`, `sympy`, `scipy.stats`.
- **Output:** A functional knowledge of how models "learn" (optimization).

## 2. Physics Module
**Goal:** Apply mathematical concepts to model the physical world (Applied Math).
- **Topics:**
  - **Kinematics:** Vectors in motion (Velocity, Acceleration).
  - **Forces:** Newton's Laws (Differential Equations).
  - **Energy:** Work, Potential/Kinetic Energy (Integrals).
  - **Simulation:** Modeling projectile motion, pendulum swings.
- **Tools:** `matplotlib` (animation), `scipy.integrate` (ODE solvers).
- **Output:** A physics engine or simulation playground.

## 3. Engineering Applied Mathematics
**Goal:** Solve real-world engineering problems using numerical methods.
- **Topics:**
  - **Signal Processing:** Fourier Transforms (FFT), Filtering.
  - **Control Systems:** PID Controllers, Feedback loops.
  - **Optimization:** Linear Programming (resource allocation).
- **Tools:** `scipy.signal`, `cvxpy`.
- **Output:** A system that analyzes signals or optimizes a process.

## 4. Machine Learning Module
**Goal:** Build and understand ML models from scratch (not just calling `.fit()`).
- **Topics:**
  - **Regression:** Linear/Logistic Regression from first principles.
  - **Classification:** k-NN, Decision Trees.
  - **Neural Networks:** Forward/Backpropagation implementation.
  - **Evaluation:** Precision/Recall, ROC curves, Overfitting/Underfitting.
- **Tools:** `sklearn` (for comparison), `pytorch` (intro to tensors).
- **Output:** A custom-built neural network trained on a dataset.

## 5. Pure Math Training
**Goal:** Develop rigorous logical thinking and proof-based understanding.
- **Topics:**
  - **Set Theory:** Logic, Sets, Functions.
  - **Number Theory:** Primes, Modulo arithmetic (Cryptography basics).
  - **Graph Theory:** Nodes, Edges, Shortest Paths.
- **Tools:** Python for discrete math simulations.
- **Output:** Solvers for cryptographic puzzles or graph problems.

## 6. Financial Module
**Goal:** quantitative finance and modeling.
- **Topics:**
  - **Time Value of Money:** PV, FV, Annuities.
  - **Portfolio Theory:** Risk/Return, Efficient Frontier.
  - **Options Pricing:** Black-Scholes model.
- **Tools:** `pandas`, `numpy`.
- **Output:** A portfolio optimizer or options pricer.
