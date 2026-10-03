# Unconstrained optimization

This lab compares fixed-step gradient descent, gradient descent with a bounded line search, and a two-dimensional deformable simplex method. Each method keeps its trajectory and iteration data for the contour plots and printed comparison.

## Mathematical model

The objective is

$$
f(x,y)=\frac{x^2y+xy^2-xy}{8}.
$$

It comes from the box-volume formulation in the coursework report. If $x$, $y$ and $z$ represent the areas of three pairs of opposite faces, unit total surface area gives $z=1-x-y$. Then $-f(x,y)=xy(1-x-y)/8$ is the squared box volume in the physical region $x\ge0$, $y\ge0$, $x+y\le1$.

The optimization routines themselves impose no constraints. They use the analytical gradient

$$
\nabla f(x,y)=\frac18
\begin{bmatrix}
2xy+y^2-y\\
x^2+2xy-x
\end{bmatrix}.
$$

The point $(1/3,1/3)$ is a local minimum with value $-1/216$. The cubic objective is unbounded below on the whole plane, so this is a local optimization experiment, not a global minimization guarantee.

## Run

After installing the repository requirements and activating the environment from the [main README](../../README.md):

```bash
cd labs/unconstrained
python main.py
```

The script prints a comparison and complete iteration tables, then opens three Matplotlib figures: the two gradient trajectories and the successive simplex triangles. Close each window to continue. Parameters are constants in the source; there are no command-line options or automatic plot exports.

## Parameters in the supplied experiment

| Setting | Value |
| --- | --- |
| Starting point | `(0, 0.4)` |
| Common experiment tolerance | `1e-4` |
| Fixed gradient step | `0.03` |
| Gradient iteration limit | `10000` |
| Line-search interval | `[0, 1]` |
| Line-search ratio | `0.618` |
| Simplex reflection coefficient | `0.8` |
| Simplex expansion coefficient | `2.01` |
| Simplex contraction coefficient | `0.25` |
| Simplex initialization scale `tau` | `0.151` |
| Additional simplex initialization offset `step` | `0.025` |
| Simplex iteration limit | `250` |

The common tolerance and starting point are set in `main.py`. The fixed step is imported as `gamma` from `optimization_algorithms.py`. Function defaults can differ from the values passed by this experiment; in particular, `main.py` explicitly supplies `epsilon=1e-4` to the line-search and simplex calls.

## Implementation

- `Vector` supplies the two-dimensional arithmetic used by all three methods.
- `gradient_descent` takes steps of the form $X_{k+1}=X_k-\gamma\nabla f(X_k)$.
- `gradient_descent_optimal` uses a golden-section-style search to choose a step in `[0, 1]` along the negative gradient. The name is retained from the source; the search is restricted to that interval.
- `simplexMethod` keeps three vertices and orders them by objective value. Reflection, expansion and contraction use the midpoint of the best and second-best vertices. Shrinking moves the other two vertices toward the best point. It is a coursework deformable-simplex implementation in the Nelder-Mead family.

Gradient methods stop when the gradient norm is below the tolerance or the iteration limit is reached. The simplex routine uses the maximum pairwise distance between its vertices as its size criterion, with the separate iteration limit.

The gradient functions return the final point, objective value, iteration count and trajectory; `return_table=True` also returns a pandas table. The simplex returns the best vertex selected at the start of its final iteration, the iteration count and simplex history, with an optional iteration table. It does not reselect the best vertex after that iteration's final update.

## Reading the output

Function and gradient counters belong to the objective wrappers in `main.py`. Function evaluations for the line search and iteration logging contribute to those counters; they are useful for understanding the experiment's workload but do not represent wall-clock benchmarks. The detailed tables can be long for the small fixed gradient step.

The supplied problem, start and coefficients determine the displayed paths. Different starting points can approach other stationary points or leave the physical box-volume region because no feasibility projection is applied.

Source: the original `be_apribojimu/main.py` and `be_apribojimu/optimization_algorithms.py`, associated with the October 2024 report. See [attribution](../../ATTRIBUTION.md).
