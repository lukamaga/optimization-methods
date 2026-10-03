# One-dimensional optimization

Three methods minimize the same scalar objective: interval halving, golden-section search and Newton's method applied to its derivative. The lab records the search points, retained intervals and derivative values so their convergence can be compared.

## Mathematical model

$$
f(x)=\frac{x^4}{4}-1,\qquad x\in[0,10].
$$

The derivatives used by Newton's method are

$$
f'(x)=x^3,\qquad f''(x)=3x^2.
$$

The analytical minimum on the interval is at $x=0$, with $f(0)=-1$. Newton's update is $x_{k+1}=x_k-f'(x_k)/f''(x_k)$; for a nonzero iterate of this particular objective, it simplifies to $x_{k+1}=2x_k/3$.

## Run

Install the repository requirements and activate the Python environment described in the [main README](../../README.md), then run from the repository root:

```bash
cd labs/one_dimensional
python main.py
```

This is a desktop Matplotlib script. It opens eight figures in sequence, including search points, interval bounds and the comparison of all three trajectories. Close each figure window to continue. After the plotting section, the script prints the summary and detailed iteration tables. It does not automatically export images or accept command-line parameters.

## Parameters in the supplied experiment

| Setting | Value | Where it is used |
| --- | --- | --- |
| Search interval | `[0, 10]` | Interval halving and golden-section search |
| Tolerance | `1e-4` | Interval width and Newton stopping conditions |
| Newton starting point | `5` | Initial Newton iterate |
| Golden-section ratio | `(sqrt(5) - 1) / 2` | Reuse of an interior point |

Change `interval`, `epsilon` and `x0` near the beginning of `main.py` to choose another experiment. The objective and its derivatives are defined in `algorithms.py`.

## Implementation

| Function | Behavior | Returned information |
| --- | --- | --- |
| `interval_halving_method` | Compares the midpoint and two quarter points, then retains the promising half-interval | Midpoint estimate, iterations, evaluation count, point history and interval history |
| `golden_section_search` | Reuses one interior point while shrinking the interval | Midpoint estimate, iterations, evaluation count, point history and interval history |
| `newton_method` | Uses first and second derivatives until both the derivative magnitude and iterate displacement meet the tolerance | Final iterate, iterations and derivative history |

Interval methods stop when the retained interval is no wider than `epsilon`. Newton requires both `abs(f_prime(x)) <= epsilon` and the most recent step length to be at most `epsilon`.

## Reading the output

The histories distinguish the current estimate from the interval boundaries. The displayed function-call counts reflect this implementation's bookkeeping: golden-section search also evaluates the midpoint for its history, while the Newton summary uses its step count for derivative counts. These columns are not a uniform measure of all computation performed by the script.

The methods retain their coursework scope. The interval routines assume an appropriate search interval and positive tolerance. Newton's routine has no separate iteration limit or zero-curvature guard; its supplied start avoids the zero second derivative at `x=0`. Its history also refers to the module's `f`, so changing derivatives alone is not enough to change the objective consistently.

Source: the original `vienmatis/algorithms.py` and `vienmatis/main.py`, associated with the September 2024 one-dimensional optimization report. See [attribution](../../ATTRIBUTION.md).
