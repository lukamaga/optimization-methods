def f(x):
    return (x ** 4) / 4 - 1


def f_prime(x):
    return x ** 3


def f_double_prime(x):
    return 3 * x ** 2


# Interval Halving Method
def interval_halving_method(f, l, r, epsilon):
    steps = 0
    function_evals = 0
    iteration_data = []
    interval_table = []

    L = r - l

    interval_table.append({
        'Iteracija': steps,
        'l': l,
        'r': r,
        'L': L,
        'Atmetamas intervalas': None
    })

    xm = (l + r) / 2
    x1 = l + L / 4
    x2 = r - L / 4

    f_xm = f(xm)
    f_x1 = f(x1)
    f_x2 = f(x2)
    function_evals += 3

    iteration_data.append({
        'Iteration': steps,
        'x1': x1,
        'f(x1)': f_x1,
        'x2': x2,
        'f(x2)': f_x2,
        'xm': xm,
        'f(xm)': f_xm
    })

    while (r - l) > epsilon:
        steps += 1

        if f_x1 < f_xm:
            discarded_interval = 'R'
            r = xm
        elif f_x2 < f_xm:
            discarded_interval = 'L'
            l = xm
        else:
            discarded_interval = 'Both'
            l = x1
            r = x2

        L = r - l
        xm = (l + r) / 2
        x1 = l + L / 4
        x2 = r - L / 4

        f_xm = f(xm)
        f_x1 = f(x1)
        f_x2 = f(x2)
        function_evals += 3

        interval_table.append({
            'Iteracija': steps,
            'l': l,
            'r': r,
            'L': L,
            'Atmetamas intervalas': discarded_interval
        })

        iteration_data.append({
            'Iteration': steps,
            'x1': x1,
            'f(x1)': f_x1,
            'x2': x2,
            'f(x2)': f_x2,
            'xm': xm,
            'f(xm)': f_xm
        })

    return (l + r) / 2, steps, function_evals, iteration_data, interval_table


# Golden Section Search Method
def golden_section_search(f, l, r, epsilon):
    tau = (5 ** 0.5 - 1) / 2
    steps = 0
    function_evals = 0
    L = r - l
    x1 = r - tau * L
    x2 = l + tau * L
    f_x1 = f(x1)
    f_x2 = f(x2)
    function_evals += 2

    iteration_data = []
    interval_table = []

    # Pradinės reikšmės užfiksavimas
    interval_table.append({
        'Iteracija': steps,
        'l': l,
        'r': r,
        'L': L,
        'Atmetamas intervalas': None
    })

    iteration_data.append({
        'Iteration': steps,
        'x1': x1,
        'f(x1)': f_x1,
        'x2': x2,
        'f(x2)': f_x2,
        'xm': (l + r) / 2,
        'f(xm)': f((l + r) / 2)
    })
    function_evals += 1

    while L > epsilon:
        steps += 1

        if f_x2 < f_x1:
            discarded_interval = 'L'
            l = x1
            x1 = x2
            f_x1 = f_x2
            L = r - l
            x2 = l + tau * L
            f_x2 = f(x2)
            function_evals += 1
        else:
            discarded_interval = 'R'
            r = x2
            x2 = x1
            f_x2 = f_x1
            L = r - l
            x1 = r - tau * L
            f_x1 = f(x1)
            function_evals += 1

        interval_table.append({
            'Iteracija': steps,
            'l': l,
            'r': r,
            'L': L,
            'Atmetamas intervalas': discarded_interval
        })

        iteration_data.append({
            'Iteration': steps,
            'x1': x1,
            'f(x1)': f_x1,
            'x2': x2,
            'f(x2)': f_x2,
            'xm': (l + r) / 2,
            'f(xm)': f((l + r) / 2)
        })
        function_evals += 1

    return (l + r) / 2, steps, function_evals, iteration_data, interval_table

# Newton's Method
def newton_method(f_prime, f_double_prime, x0, epsilon):
    steps = 0
    x = x0
    iteration_data = []

    f_x = f_prime(x)
    fpp_x = f_double_prime(x)
    L = 10
    iteration_data.append({
        'Iteration': steps,
        'x': x,
        'f(x)': f(x),
        'f\'(x)': f_x,
        'f\'\'(x)': fpp_x,
        'L': L
    })

    while True:
        if abs(f_x) <= epsilon and L <= epsilon:
            break

        x_new = x - f_x / fpp_x
        L = abs(x_new - x)
        x = x_new
        steps += 1

        f_x = f_prime(x)
        fpp_x = f_double_prime(x)

        iteration_data.append({
            'Iteration': steps,
            'x': x,
            'f(x)': f(x),
            'f\'(x)': f_x,
            'f\'\'(x)': fpp_x,
            'L': L
        })

    return x, steps, iteration_data

