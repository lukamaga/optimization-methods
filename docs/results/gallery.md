# Original figure gallery

These figures come from the saved 2024 coursework plots and reports. Lithuanian labels are retained; English captions identify the methods and parameters. PNG exports are copied without changes. The comparison figure is extracted from page 10 of the one-dimensional report.

The two-dimensional contour titles show the polynomial without its factor of 1/8. The report and code use the scaled objective $f(x,y)=(x^2y+xy^2-xy)/8$. This distinction does not change the geometric level sets, but the scale matters when interpreting a fixed gradient step.

## One-dimensional methods

<details open>
<summary>Eight figures: comparison, sample points and interval histories</summary>

### Method comparison

![Interval halving, golden-section search and Newton iterates compared on the same quartic objective. Original report figure 8.](../assets/one-dimensional-method-comparison.png)

### Interval halving: sample points

![Interval halving: sample points on the quartic objective.](../assets/interval-halving-samples.png)

### Interval halving: search intervals

![Interval halving: successive search intervals.](../assets/interval-halving-intervals.png)

### Interval halving: endpoint history

![Interval halving: left and right endpoint history.](../assets/interval-halving-bounds.png)

### Golden section: sample points

![Golden-section search: sample points on the quartic objective.](../assets/golden-section-samples.png)

### Golden section: search intervals

![Golden-section search: successive search intervals.](../assets/golden-section-intervals.png)

### Golden section: endpoint history

![Golden-section search: left and right endpoint history.](../assets/golden-section-bounds.png)

### Newton iterates

![Newton method: iterates on the quartic objective.](../assets/newton-trajectory.png)

</details>

## Unconstrained methods

<details>
<summary>Eight fixed-step gradient experiments</summary>

### Step 0.03, start (0, 0.4)

![Fixed-step gradient descent: start (0, 0.4), step 0.03.](../assets/unconstrained-gradient-start-0-0.4-step-0.03.png)

### Step 0.03, start (1, 1)

![Fixed-step gradient descent: start (1, 1), step 0.03.](../assets/unconstrained-gradient-start-1-1-step-0.03.png)

### Step 0.3, start (1, 1)

![Fixed-step gradient descent: start (1, 1), step 0.3.](../assets/unconstrained-gradient-start-1-1-step-0.3.png)

### Step 10.523, start (0, 0.4)

![Fixed-step gradient descent: start (0, 0.4), step 10.523.](../assets/unconstrained-gradient-start-0-0.4-step-10.523.png)

### Step 15.4523, start (0, 0.4)

![Fixed-step gradient descent: start (0, 0.4), step 15.4523.](../assets/unconstrained-gradient-start-0-0.4-step-15.4523.png)

### Step 16.124, start (0, 0.4)

![Fixed-step gradient descent: start (0, 0.4), step 16.124; the report records an iteration-limit case.](../assets/unconstrained-gradient-start-0-0.4-step-16.124.png)

### Step 2.666, start (1, 1)

![Fixed-step gradient descent: start (1, 1), step 2.666.](../assets/unconstrained-gradient-start-1-1-step-2.666.png)

### Step 3.233, start (1, 1)

![Fixed-step gradient descent: start (1, 1), step 3.233.](../assets/unconstrained-gradient-start-1-1-step-3.233.png)

</details>

<details>
<summary>Four line-search experiments</summary>

### Search [0, 1], start (1, 1)

![Steepest descent with line search: start (1, 1), step-search interval [0, 1].](../assets/unconstrained-optimal-step-start-1-1-range-0-1.png)

### Search [0, 5], start (0, 0.4)

![Steepest descent with line search: start (0, 0.4), step-search interval [0, 5].](../assets/unconstrained-optimal-step-start-0-0.4-range-0-5.png)

### Search [0, 5], start (1, 1)

![Steepest descent with line search: start (1, 1), step-search interval [0, 5].](../assets/unconstrained-optimal-step-start-1-1-range-0-5.png)

### Search [5, 10], start (0, 0.4)

![Steepest descent with line search: start (0, 0.4), step-search interval [5, 10].](../assets/unconstrained-optimal-step-start-0-0.4-range-5-10.png)

</details>

<details>
<summary>Three deformable-simplex trajectories</summary>

### Simplex, start (0, 0.4)

![Deformable simplex trajectory: start (0, 0.4). Parameters: reflection 0.8, expansion 2.01, contraction 0.25, initial size 0.151.](../assets/unconstrained-simplex-start-0-0.4.png)

### Simplex, start (0, 0)

![Deformable simplex trajectory: start (0, 0). Parameters: reflection 0.8, expansion 2.01, contraction 0.25, initial size 0.151.](../assets/unconstrained-simplex-start-0-0.png)

### Simplex, start (1, 1)

![Deformable simplex trajectory: start (1, 1). Parameters: reflection 0.8, expansion 2.01, contraction 0.25, initial size 0.151.](../assets/unconstrained-simplex-start-1-1.png)

</details>

## Reports and provenance

The constrained box problem is documented through tables in its report. No original chart was found for that lab or for linear programming; no replacement chart is presented here.

See [recorded results](recorded-results.md), [report selection](../reports/README.md), and the [source manifest](provenance.json).
