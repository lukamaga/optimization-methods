# Recorded coursework results

These selected results come from the 2024 reports. The CSV files retain the reported parameters, rounded values and counting conventions; report filenames and page numbers identify each source. The [figure gallery](gallery.md) preserves the original illustrations.

## One-dimensional optimization

For `f(x) = x^4 / 4 - 1` on `[0, 10]`, the analytical minimum is `x = 0`, with `f(x) = -1`. The reported tolerance is `0.0001`; Newton starts at `x = 5`.

The concluding table on page 10 records:

| Method | Reported minimum point | Iterations excluding the initial state | Objective evaluations | First/second derivative evaluations |
| --- | ---: | ---: | ---: | --- |
| Interval halving | 0.0000762939453 | 17 | 54 | 0 / 0 |
| Golden-section search | 0.0000482243784 | 24 | 51 | 0 / 0 |
| Newton | 0.0001980106402 | 25 | 0 | 25 / 25 |

[CSV transcription](one-dimensional-summary.csv)

The report body gives 51 objective evaluations for interval halving, while the final summary gives 54. This table follows the final summary. The golden-section discussion includes 25 displayed states, whereas the summary lists 24 updates. These counting conventions should not be mixed, and derivative evaluations need not have the same cost as objective evaluations.

## Unconstrained methods

The reduced box model uses paired face areas `x = 2ac`, `y = 2bc`, `z = 2ab`, with `x + y + z = 1`. Its minimization objective is `f(x, y) = (x^2*y + x*y^2 - x*y) / 8 = -V^2`. The physical solution is `x = y = z = 1/3`, giving `f = -1/216`. The polynomial is not globally bounded below over the entire plane.

Selected fixed-step gradient results, from report pages 3 to 5:

| Start | Step | Reported final point | Iterations | Gradient evaluations | Outcome |
| --- | ---: | --- | ---: | ---: | --- |
| (1, 1) | 0.03 | (0.3339, 0.3339) | 1590 | 1591 | Convergence |
| (1, 1) | 2.666 | (0.33325, 0.33325) | 1 | 2 | Near the solution after one update for this starting point |
| (0, 0.4) | 10.523 | (0.33193, 0.3348) | 7 | 8 | Convergence |
| (0, 0.4) | 16.124 | (0.35268, 0.35268) | 10000 | 10001 | Iteration limit, not a converged minimum |

The last case alternates approximately between `(0.352682, 0.352682)` and `(0.311421, 0.311421)`. Starting exactly at `(0, 0)` shows another limitation of a gradient-norm stopping rule: the gradient is zero there, although it is not the desired box solution.

From `(0, 0.4)`, line search over `[0, 5]` took 19 iterations, 495 objective evaluations and 20 gradient evaluations. The interval `[5, 10]` gave 8 iterations, 209 objective evaluations and 9 gradient evaluations. Source: pages 8 to 9.

With simplex parameters reflection 0.8, expansion 2.01, contraction 0.25, initial size 0.151 and tolerance 0.0001, the report records 23, 26 and 21 iterations from `(1, 1)`, `(0, 0)` and `(0, 0.4)` respectively. All three reported final points are close to `(1/3, 1/3)`. Source: pages 11 to 13.

[Selected unconstrained results as CSV](unconstrained-selected-results.csv)

The original contour titles omit the objective's factor of `1/8`; the report and code use the scaled function. The report also contains isolated transcription slips, including the objective value attached to the near-origin point for step 3.999. That row is not used as a result here. The explicit objective formula should guide interpretation of such entries.

## Constrained box problem

Here `x, y, z` are box dimensions. The model minimizes `-xyz`, subject to `2xy + 2xz + 2yz = 1` and nonnegative dimensions. The squared penalty is weighted by `1/r`, starting at `r = 10` and reducing it by a divisor `q` at each outer step.

The analytical box solution is a cube with side `1/sqrt(6)` and volume `1/(6*sqrt(6))`.

From `(0, 0, 0)`, the summary tables on pages 3 to 4 record:

| Divisor q | Reported outer iterations | Reported objective | Penalty-function evaluations |
| --- | ---: | ---: | ---: |
| 2 | 31 | -0.068041381 | 4367 |
| 5 | 13 | -0.068041381 | 1906 |
| 20 | 8 | -0.0680413813 | 1374 |

[CSV with final coordinates](constrained-penalty-summary.csv)

Some table headers label the divisor as `r`; the experiment descriptions identify it as `q`. The CSV uses `q` to distinguish the divisor from the changing penalty parameter. The method section and appendix use a deformable simplex, despite an introductory reference to steepest descent. The initial-value list also prints `V(1,1,1) = 1`, whereas the minimization definition and later tables use `f = -xyz` and therefore `f(1,1,1) = -1`.

## Linear programming and source record

The archive contains linear-programming source files, but no separate own report or saved chart was found. No numerical result is added here without a historical source.

The [published reports](../reports/README.md) redact the student identifier only. [provenance.json](provenance.json) records original relative filenames, image origins, selected report versions and file hashes.
