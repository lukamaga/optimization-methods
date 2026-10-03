import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from optimization_algorithms import (
    gradient_descent,
    gradient_descent_optimal,
    simplexMethod,
    Vector,
    gamma
)

# Global variables for counting
gradientCount = 0
functionCalls = 0

# Objective Function
def f(X):
    global functionCalls
    functionCalls += 1
    x, y = X.x, X.y
    return 0.125 * (x ** 2 * y + x * y ** 2 - x * y)

# Gradient of the Objective Function
def grad_f(X):
    global gradientCount
    gradientCount += 1
    x, y = X.x, X.y
    df_dx = 0.125 * (2 * x * y + y ** 2 - y)
    df_dy = 0.125 * (x ** 2 + 2 * x * y - x)
    return Vector(df_dx, df_dy)

# Starting Point
X0 = (0, 0.4)
X0_vector = Vector(*X0)

print("\nFunction and gradient at X0:")
print("X0 =", X0_vector)
print("f(X0) =", f(X0_vector))
print("grad_f(X0) =", grad_f(X0_vector))

epsilon = 1e-4

results = {}

# Gradient Descent
gradientCount = 0
functionCalls = 0

X_gd, f_gd, steps_gd, traj_gd, table_gd = gradient_descent(
    f, grad_f, X0, gamma, epsilon, max_iter=10000, return_table=True
)
func_calls_gd = functionCalls
grad_calls_gd = gradientCount
print(
    f"\nGradient Descent (Fixed Step Size): X = {X_gd}, f(X) = {f_gd}, steps = {steps_gd}, "
    f"function calls = {func_calls_gd}, gradient evaluations = {grad_calls_gd}"
)

# Store results
results["Gradient Descent"] = {
    "X": X_gd,
    "f(X)": f_gd,
    "steps": steps_gd,
    "function_calls": func_calls_gd,
    "gradient_calls": grad_calls_gd,
    "trajectory": traj_gd,
    "table": table_gd,
}

# Gradient Descent with Optimal Step Size
gradientCount = 0
functionCalls = 0
X_sd, f_sd, steps_sd, traj_sd, table_sd = gradient_descent_optimal(
    f, grad_f, X0, epsilon, max_iter=10000, return_table=True
)
func_calls_sd = functionCalls
grad_calls_sd = gradientCount
print(
    f"\nGradient Descent with Optimal Step Size: X = {X_sd}, f(X) = {f_sd}, steps = {steps_sd}, "
    f"function calls = {func_calls_sd}, gradient evaluations = {grad_calls_sd}"
)

# Store results
results["Gradient Descent with Optimal Step Size"] = {
    "X": X_sd,
    "f(X)": f_sd,
    "steps": steps_sd,
    "function_calls": func_calls_sd,
    "gradient_calls": grad_calls_sd,
    "trajectory": traj_sd,
    "table": table_sd,
}

# Simplex Method
functionCalls = 0
X0_vector = Vector(*X0)
reflection = 0.8
expansion = 2.01
contraction = 0.25
tau = 0.151

best_point, iterations, table_ds, constructedSimplexes = simplexMethod(
    f,
    X0_vector,
    reflectionRate=reflection,
    expansionRate=expansion,
    contractionRate=contraction,
    tau=tau,
    epsilon=epsilon,
    maxIterations=250,
    return_table=True,
)

func_calls_ds = functionCalls
print(
    f"\nSimplex Method: X = {best_point}, f(X) = {f(best_point)}, steps = {iterations}, function calls = {func_calls_ds}"
)

# Store results
results["Simplex Method"] = {
    "X": best_point,
    "f(X)": f(best_point),
    "steps": iterations,
    "function_calls": func_calls_ds,
    "gradient_calls": "N/A",
    "trajectory": constructedSimplexes,
    "table": table_ds,
}

# Comparison Table
comparison_data = []
for algo_name, res in results.items():
    comparison_data.append(
        {
            "Algorithm": algo_name,
            "Obtained Solution": f"({round(res['X'].x, 5)}, {round(res['X'].y, 5)})",
            "Estimated Minimum": round(res["f(X)"], 5),
            "Number of Steps": res["steps"],
            "Function Evaluations": res["function_calls"],
            "Gradient Evaluations": res.get("gradient_calls", "N/A"),
        }
    )
comparison_table = pd.DataFrame(comparison_data)

print("\nComparison of Results:")
print(comparison_table.to_string(index=False))

# Print Iteration Tables
print(f"\nIteration details starting from X0:")
for algo_name, res in results.items():
    if "table" in res:
        table = res["table"]
        print(f"\nAlgorithm: {algo_name}")
        print(table.to_string(index=False))  # Print the table without the index

# Visualization Functions
def plot_algorithm_with_contour(algo_name, traj, x0, step_size=None):
    # Pagal pateiktą pavyzdį
    x = np.linspace(-1, 2, 200)
    y = np.linspace(-1, 2, 200)
    X, Y = np.meshgrid(x, y)
    Z = 0.125 * (X ** 2 * Y + X * Y ** 2 - X * Y)
    levels = np.linspace(-5, 5, 75)

    plt.figure(figsize=(10, 8))
    plt.contour(X, Y, Z, levels=levels)

    allX = [point.x for point in traj]
    allY = [point.y for point in traj]

    plt.plot(allX, allY, '-bx', label='Trajektorija', markersize=3)

    # Pradinis ir minimumo taškai
    plt.plot(x0.x, x0.y, 'ro', label='Pradinis taškas')
    min_point = traj[-1]
    plt.plot(min_point.x, min_point.y, 'go', label='Minimumo taškas')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("V(x, y) = x^2*y + x*y^2 - x*y contour. X0 = {0}, γ = {1}".format(x0, step_size))
    #plt.title("V(x, y) = x^2*y + x*y^2 - x*y contour. X0 = {0},  Intervalas: [5,10]".format(x0))
    plt.legend()
    plt.show()

def plot_simplex_with_contour(constructedSimplexes, x0, reflection, expansion, contraction, tau):
    # Pagal pateiktą pavyzdį
    x = np.linspace(-1, 2, 200)
    y = np.linspace(-1, 2, 200)
    X, Y = np.meshgrid(x, y)
    Z = 0.125 * (X ** 2 * Y + X * Y ** 2 - X * Y)
    levels = np.linspace(-5, 5, 75)

    plt.figure(figsize=(10, 8))
    plt.contour(X, Y, Z, levels=levels)

    for simplex in constructedSimplexes:
        simplexX = [vertex.x for vertex in simplex] + [simplex[0].x]
        simplexY = [vertex.y for vertex in simplex] + [simplex[0].y]
        plt.plot(simplexX, simplexY, '-b')

    plt.plot(x0.x, x0.y, 'ro', label='Pradinis taškas')
    final_simplex = constructedSimplexes[-1]
    best_vertex = final_simplex[0]
    plt.plot(best_vertex.x, best_vertex.y, 'go', label='Minimumo taškas')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Simplex Method: X0 = {0}, α = {1}, γ = {2}, β = {3}, τ = {4}".format(
        x0, reflection, expansion, contraction, tau
    ))
    plt.legend()
    plt.show()

# Vizualizacija
plot_algorithm_with_contour(
    "Gradient Descent",
    results["Gradient Descent"]["trajectory"],
    X0_vector,
    gamma
)

plot_algorithm_with_contour(
    "Gradient Descent with Optimal Step Size",
    results["Gradient Descent with Optimal Step Size"]["trajectory"],
    X0_vector
)

plot_simplex_with_contour(
    results["Simplex Method"]["trajectory"],
    X0_vector,
    reflection,
    expansion,
    contraction,
    tau
)
