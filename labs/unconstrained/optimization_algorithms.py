import math
import numpy as np
import statistics
import pandas as pd

# Vector class as per your implementation
class Vector(object):
    def __init__(self, x, y):  # konstruktrius
        self.x = x  # x saugomas kaip vektoriaus koordinate
        self.y = y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)  # pitagoro teorema

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)  # atvirkstine

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: float):
        return self.__mul__(other)

    def __truediv__(self, other: float):
        ratio = 1.0 / other
        return self * ratio

    def __rtruediv__(self, other: float):
        return self.__truediv__(other)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

# Global variables for counting
gradientCount = 0
functionCalls = 0

gamma = 0.03 #kaip toli judesim

# Gradient Descent
def gradient_descent(f, grad_f, X0, step_size=gamma, epsilon=0.0001, max_iter=10000, return_table=False):
    global gradientCount
    gradientCount = 0
    X = Vector(*X0)  # pradinė vektoriaus reikšmė
    grad = grad_f(X)
    iterations = 0
    trajectory = [X]
    table_data = []
    # step_size = gamma  # Dabar step_size yra perduodamas iš išorės

    while grad.length() >= epsilon and iterations < max_iter:
        f_X = f(X)
        table_data.append({
            'Iteration': iterations,
            'X1': X.x,
            'X2': X.y,
            'f(X)': f_X,
            'Gradient Norm': grad.length()
        })
        X = X - step_size * grad  # gradiento nusileidimo žingsnis, atnaujiname taska judedami pries gradiento krypti
        grad = grad_f(X)
        iterations += 1
        trajectory.append(X)

    f_X = f(X)  # f-jos reikšmė paskutiniame taške
    table_data.append({
        'Iteration': iterations,
        'X1': X.x,
        'X2': X.y,
        'f(X)': f_X,
        'Gradient Norm': grad.length()
    })

    if return_table:
        table = pd.DataFrame(table_data)
        return X, f_X, iterations, trajectory, table
    else:
        return X, f_X, iterations, trajectory

# Gradient Descent with Optimal Step Size
def gradient_descent_optimal(f, grad_f, X0, epsilon=0.000001, max_iter=10000, return_table=False):
    global gradientCount, functionCalls
    gradientCount = 0
    functionCalls = 0
    X = Vector(*X0)
    grad = grad_f(X)
    iterations = 0
    trajectory = [X]
    table_data = []

    tau = 0.618

    def golden_ratio_search(f_line, l, r, epsilon):
        L = r - l
        x1 = r - tau * L
        x2 = l + tau * L

        fx1 = f_line(x1)
        fx2 = f_line(x2)

        while L >= epsilon:
            if fx2 < fx1:
                l = x1
                L = r - l
                x1 = x2
                x2 = l + tau * L

                fx1 = fx2
                fx2 = f_line(x2)
            else:
                r = x2
                L = r - l
                x2 = x1
                x1 = r - tau * L

                fx2 = fx1
                fx1 = f_line(x1)

        return (l + r) / 2.0 #optimalus zingsnis

    while grad.length() >= epsilon and iterations < max_iter:
        f_X = f(X)
        table_data.append({
            'Iteration': iterations,
            'X1': X.x,
            'X2': X.y,
            'f(X)': f_X,
            'Gradient Norm': grad.length()
        })

        def f_line(step):#tam kad rasti optimalu zingsni, ir tai minimizuojama funkcija
            new_X = X - step * grad  #new_X  yra pasislinkes nuo dabartinio tasko X gradiento kryptimi per atstuma step
            return f(new_X)

        step_size = golden_ratio_search(f_line, 0, 1 , epsilon)
        #print(step_size)
        X = X - step_size * grad  # judame prieš gradientą
        grad = grad_f(X) #naujas gradiendas taske x
        iterations += 1
        trajectory.append(X)

    f_X = f(X)
    table_data.append({
        'Iteration': iterations,
        'X1': X.x,
        'X2': X.y,
        'f(X)': f_X,
        'Gradient Norm': grad.length()
    })

    if return_table:
        table = pd.DataFrame(table_data)
        return X, f_X, iterations, trajectory, table
    else:
        return X, f_X, iterations, trajectory

# Simplex method
def simplexMethod(f, X0, reflectionRate: float = 1, expansionRate: float = 2.0, contractionRate: float = 0.5,
                  tau: float = 1.0, epsilon: float = 1e-8, maxIterations: int = 250, return_table=False):
    constructedSimplexes = []
    table_data = []
    step = 0.025
    #reflectionRate - alfa, refleksijos kooficentas
    #expansionRate - gamma, ispletimo kooficentas
    #contractionRate - beta, kontrakcijos kooficentas, suspausdimas
    def contract():
        nonlocal worst, fWorst, good, fGood, mid

        contractedPoint = (1 - contractionRate) * mid + contractionRate * worst #perkelti blogiausia taska link centroido, taip sumazinant simplekso dydi
        fContr = f(contractedPoint)

        if fContr < fWorst:
            worst, fWorst = contractedPoint, fContr
        else: #shrink aplink best taska
            good = (good + best) / 2
            fGood = f(good)

            worst = (worst + best) / 2
            fWorst = f(worst)

    # Koeficientai, kad simpleksas būtų lygiašonis trikampis
    b1 = ((math.sqrt(2) + 1) / (2 * math.sqrt(2))) * tau
    b2 = ((math.sqrt(2) - 1) / (2 * math.sqrt(2))) * tau

    X1 = Vector(X0.x + step + b2, X0.y + b1)  # nauji vektoriai
    X2 = Vector(X0.x + step / 2 + b1, X0.y + step * 0.866 + b2)

    simplex = {X0: f(X0), X1: f(X1), X2: f(X2)} #zodynas raktas:reiksme
    iterations = 0

    # max atstumas
    def simplex_size(simplex_points):
        max_distance = 0
        for i in range(len(simplex_points)):
            for j in range(i + 1, len(simplex_points)):
                distance = (simplex_points[i] - simplex_points[j]).length()
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    while iterations < maxIterations:
        iterations += 1

        points = sorted(simplex.items(), key=lambda x: x[1])

        best, fBest = points[0][0], points[0][1]
        good, fGood = points[1][0], points[1][1]
        worst, fWorst = points[2][0], points[2][1]

        constructedSimplexes.append([best, good, worst])

        # Collect iteration data
        table_data.append({
            'Iteration': iterations,
            'Best X1': best.x,
            'Best X2': best.y,
            'f(Best)': fBest,
            'Worst X1': worst.x,
            'Worst X2': worst.y,
            'f(Worst)': fWorst
        })

        mid = (best + good) / 2.0 #centroido skaiciavimas
        refl = mid + reflectionRate * (mid - worst) #refleksija
        fRefl = f(refl)

        if fRefl < fBest:
            exp = mid + expansionRate * (refl - mid)
            fExp = f(exp)
            if fExp < fRefl:
                worst, fWorst = exp, fExp
            else:
                worst, fWorst = refl, fRefl
        elif fRefl < fGood:
            worst, fWorst = refl, fRefl
        else:
            contract() #refleksija nesuteikia geresnio tasko fRefl >= fGood, todel darom suspausdima

        if simplex_size([best, good, worst]) < epsilon:
            break

        simplex = {worst: fWorst, good: fGood, best: fBest}

    if return_table:
        table = pd.DataFrame(table_data)
        return best, iterations, table, constructedSimplexes
    else:
        return best, iterations, constructedSimplexes
