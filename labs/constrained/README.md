# Nonlinear constrained optimization

The lab maximizes the volume of a rectangular box with unit surface area. It combines a quadratic penalty with a three-dimensional deformable simplex search, repeatedly strengthening the penalty by decreasing its parameter.

## Mathematical model

For side lengths $X=(x,y,z)$, the minimization objective is the negative volume:

$$
f(X)=-xyz.
$$

The constraints are

$$
2xy+2xz+2yz-1=0,\qquad x\ge0,\ y\ge0,\ z\ge0.
$$

The source calls the objective `V`, so its printed `V(X)` is **negative** physical volume. Its augmented objective is

$$
B(X,r)=-xyz+\frac{1}{r}\left[
\max(0,-x)^2+\max(0,-y)^2+\max(0,-z)^2+
(2xy+2xz+2yz-1)^2\right].
$$

Halving $r$ increases the coefficient $1/r$ and penalizes constraint violations more strongly. The analytical symmetric solution is a cube with side length $1/\sqrt6$ and positive volume $1/(6\sqrt6)$; this is a mathematical reference, not a claim about the accuracy of every run.

## Run

This particular lab uses only Python's standard-library `math` module:

```bash
cd labs/constrained
python main.py
```

The program prints each outer iteration's parameter, point and objective information, followed by the final coordinates, negative volume, iteration count and penalty-function-call count. It has no graphical interface or command-line arguments.

## Parameters in the supplied experiment

| Setting | Value |
| --- | --- |
| Starting point | `(0.1, 0, 0.4)` |
| Initial penalty parameter `r` | `10` |
| Penalty schedule | `r /= 2` after each inner solve |
| Simplex reflection coefficient | `1.0` |
| Simplex expansion coefficient | `2.0` |
| Simplex contraction coefficient | `0.5` |
| Simplex initialization scale `tau` | `1` |
| Inner simplex tolerance | `0.0001` |
| Inner simplex iteration limit | `250` |

The initial point and penalty schedule are in the `if __name__ == '__main__'` block. Commented starts `(1,1,1)` and `(0,0,0)` remain in the original file. Inner simplex settings are the defaults of `simplexMethod`.

## Implementation

`Vector` represents a three-dimensional point. `simplexMethod` constructs four vertices and performs reflection, expansion, contraction or shrinking. Its size criterion is the sum of the tetrahedron's six edge lengths.

`Penalty` computes the constraint term using the global `r`; `VPenalty` adds `V` and increments the objective-call counter. `RunPenaltyAlgorithm` solves one augmented problem from the current point. The outer loop reuses that result as the next starting point.

## Stopping behavior

The active outer loop continues while the stored penalty decreases or any coordinate is negative. This is a historical heuristic, not a direct feasibility or optimality tolerance. The `epsilon=1e-6` assignment beside the outer loop is only referenced by commented alternative stopping conditions; it does not control the active loop. There is no separate outer iteration limit.

The printed penalty-call counter includes calls made for reporting as well as optimization. The global penalty parameter is initialized by the script entry point, so direct use of the functions requires setting `r` explicitly.

From the second outer iteration onward, the printed `Penalty` value was stored using the preceding value of `r`, while `B(X,r)` is recalculated using the newly halved `r`. Those two columns therefore refer to different penalty weights on the same printed row.

Source: the original `neties_test/main.py`. Despite its archive directory name, this is a complete coursework program matching the box-volume model in the author's November 2024 report. The unrelated quadratic-objective experiment from the archive's `netiesinis` directory is not part of this lab. See [attribution](../../ATTRIBUTION.md).
