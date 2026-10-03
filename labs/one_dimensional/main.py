import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from algorithms import f, f_prime, f_double_prime, interval_halving_method, golden_section_search, newton_method

pd.options.display.float_format = '{:.13f}'.format


interval = (0, 10)
epsilon = 1e-4
x0 = 5

# Interval Halving Method
x_min_halving, steps_halving, evals_halving, iteration_data_halving, interval_table_halving = interval_halving_method(f, *interval, epsilon)
f_min_halving = f(x_min_halving)

# Golden Section Search
x_min_golden, steps_golden, evals_golden, iteration_data_golden, interval_table_golden = golden_section_search(f, *interval, epsilon)
f_min_golden = f(x_min_golden)

# Newton's Method
x_min_newton, steps_newton, iteration_data_newton = newton_method(f_prime, f_double_prime, x0, epsilon)
f_min_newton = f(x_min_newton)

results = {
    "Name": ["Intervalo pusiau dalijimas", "Auksinis pjūvis", "Niutono metodas"],
    "Found solution": [True, True, True],
    "Solution": [x_min_halving, x_min_golden, x_min_newton],
    "Value": [f_min_halving, f_min_golden, f_min_newton],
    "Steps (N)": [steps_halving, steps_golden, steps_newton],
    "f calls": [evals_halving, evals_golden, 0],
    "df calls": [0, 0, steps_newton],  # Only for Newton method
    "ddf calls": [0, 0, steps_newton]  # Only for Newton method
}

x_vals = np.linspace(0, 10, 400)
y_vals = f(x_vals)

y_min, y_max = -2, 6
x_min, x_max = -0.5, 4

# Plot for Interval Halving Method
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = (x^4)/4 - 1', color='blue')

for data in iteration_data_halving:
    x1 = data['x1']
    x2 = data['x2']
    xm = data['xm']

    plt.scatter([x1, x2], [f(x1), f(x2)], color='green', s=10, zorder=3, label='x1 ir x2' if data['Iteration'] == 1 else "")  # Green for x1 and x2
    plt.scatter(xm, f(xm), color='red', s=10, zorder=4, label='x_m' if data['Iteration'] == 1 else "")  # Red for xm

plt.scatter(x_min_halving, f_min_halving, color='red', marker='o', zorder=5, label='Minimum')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Intervalo pusiau dalijimas')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
iterations = [i['Iteracija'] for i in interval_table_halving]
l_values = [i['l'] for i in interval_table_halving]
r_values = [i['r'] for i in interval_table_halving]

plt.plot(iterations, l_values, label='l (kairysis intervalas)', color='blue', marker='o')
plt.plot(iterations, r_values, label='r (dešinysis intervalas)', color='red', marker='o')

plt.xlabel('Iteracija')
plt.ylabel('Intervalo reikšmė')
plt.title('Intervalo kaita (Intervalo pusiau dalijimas)')
plt.legend()
plt.grid(True)
plt.show()

# Plot for Golden Section Search
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = (x^4)/4 - 1', color='blue')

for data in iteration_data_golden:
    x1 = data['x1']
    x2 = data['x2']
    xm = data['xm']
    plt.scatter([x1, x2], [f(x1), f(x2)], color='green', s=10, label='x1 ir x2' if data['Iteration'] == 1 else "")  # Green for x1 and x2
    plt.scatter(xm, f(xm), color='red', s=10, label='x_m' if data['Iteration'] == 1 else "")  # Red for xm

plt.scatter(x_min_golden, f_min_golden, color='red', marker='o', zorder=5, label='Minimum')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Auksinio pjūvio metodas')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#golden
plt.figure(figsize=(10, 6))
iterations_golden = [i['Iteracija'] for i in interval_table_golden]
l_values_golden = [i['l'] for i in interval_table_golden]
r_values_golden = [i['r'] for i in interval_table_golden]

plt.plot(iterations_golden, l_values_golden, label='l (kairysis intervalas)', color='blue', marker='o')
plt.plot(iterations_golden, r_values_golden, label='r (dešinysis intervalas)', color='red', marker='o')

plt.xlabel('Iteracija')
plt.ylabel('Intervalo reikšmė')
plt.title('Intervalo kaita (Auksinio pjūvio metodas)')
plt.legend()
plt.grid(True)
plt.show()

#dalijimas lines
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = (x^4)/4 - 1', color='blue')

for data in interval_table_halving:
    l = data['l']
    r = data['r']
    plt.axvline(x=l, color='green', linestyle='-', linewidth=1.5, alpha=0.7)
    plt.axvline(x=r, color='red', linestyle='-', linewidth=1.5, alpha=0.7)

plt.scatter(x_min_halving, f_min_halving, color='red', marker='o', zorder=5, label='Minimum')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Intervalo pusiau dalijimas su intervalais')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# golden lines
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = (x^4)/4 - 1', color='blue')

for data in interval_table_golden:
    l = data['l']
    r = data['r']
    plt.axvline(x=l, color='green', linestyle='-', linewidth=1.5, alpha=0.7)
    plt.axvline(x=r, color='red', linestyle='-', linewidth=1.5, alpha=0.7)

plt.scatter(x_min_golden, f_min_golden, color='red', marker='o', zorder=5, label='Minimum')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Auksinio pjūvio metodas su intervalais')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# Plot for Newton's Method
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = (x^4)/4 - 1', color='blue')

x_iterations = [data['x'] for data in iteration_data_newton]
f_iterations = [f(x) for x in x_iterations]
plt.scatter(x_iterations, f_iterations, color='purple', s=10)

plt.scatter(x_min_newton, f_min_newton, color='red', marker='o', zorder=5, label='Minimum')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Niutono metodas')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


plt.figure(figsize=(10, 6))

steps_halving_list = [data['Iteration'] for data in iteration_data_halving]
x_halving = [data['xm'] for data in iteration_data_halving]
plt.plot(steps_halving_list, x_halving, label='Intervalo pusiau dalijimas', marker='o', color='blue')
steps_golden_list = [data['Iteration'] for data in iteration_data_golden]
x_golden = [data['xm'] for data in iteration_data_golden]
plt.plot(steps_golden_list, x_golden, label='Auksinis pjūvis', marker='s', color='green')
steps_newton_list = [data['Iteration'] for data in iteration_data_newton]
x_newton = [data['x'] for data in iteration_data_newton]
plt.plot(steps_newton_list, x_newton, label='Niutono metodas', marker='^', color='red')
plt.xlabel('Iteracijų skaičius')
plt.ylabel('x reikšmės (minimui artėjanti taško vertė)')
plt.title('Optimizavimo metodų palyginimas')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Summary of results
results_df = pd.DataFrame(results)
print("Summary Results:")
print(results_df.to_string(index=False))

print("\nInterval Halving Method Iterations:")
df_halving = pd.DataFrame(iteration_data_halving)
print(df_halving.to_string(index=False))

print("\nInterval Halving Method - Interval Data:")
df_interval_halving = pd.DataFrame(interval_table_halving)
print(df_interval_halving.to_string(index=False))

print("\nGolden Section Search Iterations:")
df_golden = pd.DataFrame(iteration_data_golden)
print(df_golden.to_string(index=False))

print("\nGolden Section Search - Interval Data:")
df_interval_golden = pd.DataFrame(interval_table_golden)
print(df_interval_golden.to_string(index=False))

print("\nNewton's Method Iterations:")
df_newton = pd.DataFrame(iteration_data_newton)
print(df_newton.to_string(index=False))
