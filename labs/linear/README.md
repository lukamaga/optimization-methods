# Linear programming with a simplex tableau

This lab implements tableau construction, entering-variable selection, the minimum-ratio test and pivot row operations for a small linear program. The console output exposes the intermediate tableaux rather than hiding them behind a solver library.

## Mathematical model

The active example minimizes

$$
-2x_1-3x_2-5x_4
$$

subject to

$$
\begin{aligned}
3x_1+x_2-x_3-x_4 &\le 8,\\
-2x_1+4x_2 &\le 10,\\
x_3+x_4 &\le 3,\\
x_1,x_2,x_3,x_4 &\ge0.
\end{aligned}
$$

In matrix form, the example uses

```text
A = [[ 3, 1, -1, -1],
     [-2, 4,  0,  0],
     [ 0, 0,  1,  1]]
b = [8, 10, 3]
c = [-2, -3, 0, -5]
```

The analytical reference solution is $(17/7,26/7,0,3)$ with objective value $-31$. All three inequality constraints are active at this point.

The source also assigns an earlier coefficient set near the start of `main()`. The second assignments to `A`, `b` and `c` replace it before the model is constructed; only the matrix above is solved by the supplied entry point.

## Run

After installing NumPy, either directly or through the repository requirements:

```bash
cd labs/linear
python main.py
```

The script prints the input matrices, starting tableau, pivot details, intermediate tableaux and final solution. There are no plots, exported files or command-line parameters.

## Implementation

| Method | Purpose |
| --- | --- |
| `addA`, `addB`, `addC` | Assign the coefficient matrix, right-hand side and objective vector |
| `setObj` | Select the source's `MIN` or `MAX` objective mode |
| `getTableau` | Build the starting tableau, adding identity slack columns when needed |
| `simplexOptimization` | Choose a negative reduced-cost column, apply the ratio test and pivot |
| `printTableau` | Display the tableau with rounded entries |
| `printSoln` | Display the stored solution vector and objective value |

The example starts from the slack-variable basis for $Ax\le b$, $x\ge0$. The most negative objective-row coefficient determines the entering variable. Positive pivot-column entries participate in the minimum-ratio test. Row operations then replace one basis variable.

## Reading the output and scope

`model.x` contains the decision variables followed by the slack variables, so the four-variable example stores seven values. The displayed `Base` list is formed from nonzero entries of that stored vector; it is not a full representation of a potentially degenerate basis.

The implementation is a coursework solver for examples with a feasible initial slack basis. It does not implement a Phase I procedure, robust infeasibility or unboundedness detection, or a general solver status interface. Its loop allows at most 49 pivot iterations; the counter starts at one and can reach and print 50 when the limit is exhausted. Reaching that bound is not separately reported as a failed convergence condition.

The objective vector is transformed in place during tableau setup. Use a fresh model and coefficient arrays for a new problem. `setPrintIter(False)` suppresses tableau printing, but the pivot messages are unconditional in the original implementation.

Source: the original `ties/tiesinis/main.py`. See [attribution](../../ATTRIBUTION.md).
