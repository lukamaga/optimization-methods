import math

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: float):
        return self.__mul__(other)

    def __truediv__(self, other: float):
        ratio = 1.0 / other
        return self * ratio

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

def simplexMethod(f, X0, reflectionRate: float = 1.0, expansionRate: float = 2.0, contractionRate: float = 0.5, tau: float = 1, epsilon: float = 0.0001, maxIterations: int = 250):
    def contract():
        nonlocal worst, fWorst, good1, fGood1, good2, fGood2, mid

        contractedPoint = mid + contractionRate * (worst - mid)
        fContr = f(contractedPoint)

        if fContr < fWorst:
            worst, fWorst = contractedPoint, fContr
        else:
            good1 = (good1 + best) / 2
            fGood1 = f(good1)

            good2 = (good2 + best) / 2
            fGood2 = f(good2)

            worst = (worst + best) / 2
            fWorst = f(worst)

    delta1 = (2 * math.sqrt(2) / 3.0) * tau
    delta2 = (math.sqrt(2) / 6) * tau

    X1 = Vector(X0.x + delta2, X0.y + delta1, X0.z + delta1)
    X2 = Vector(X0.x + delta1, X0.y + delta2, X0.z + delta1)
    X3 = Vector(X0.x + delta1, X0.y + delta1, X0.z + delta2)
    #print(f"x1: {X1}, x2: {X2}, x3: {X3}")
    simplex = [ (X0, f(X0)), (X1, f(X1)), (X2, f(X2)), (X3, f(X3)) ]
    iterations = 0

    while iterations < maxIterations:
        iterations += 1
        #print(iterations)

        points = sorted(simplex, key=lambda x: x[1])

        best, fBest = points[0][0], points[0][1]
        good1, fGood1 = points[1][0], points[1][1]
        good2, fGood2 = points[2][0], points[2][1]
        worst, fWorst = points[3][0], points[3][1]

        #print(best, good1, good2, worst)

        mid = (best + good1 + good2) / 3.0
        refl = mid + reflectionRate * (mid - worst)
        fRefl = f(refl)
        if fRefl < fBest:
            exp = mid + expansionRate * (refl - mid)
            fExp = f(exp)
            if fExp < fRefl:
                worst, fWorst = exp, fExp
            else:
                worst, fWorst = refl, fRefl
        elif fRefl < fGood2 and fRefl > fBest:
            worst , fWorst = refl, fRefl
        elif fRefl < fWorst and fRefl >= fGood2:
            tmp = (worst, fWorst)
            worst, fWorst = refl, fRefl
            refl, fRefl = tmp
            contract()
        else:
            contract()

        perimeter = (worst - best).length() + (good2 - best).length() + (good1 - worst).length() + (good1 - good2).length() + (good2 - worst).length() + (best - good1).length()
        if perimeter < epsilon:
            break

        simplex = [ (worst, fWorst), (good2, fGood2), (good1, fGood1), (best, fBest) ]

    return best

penaltyFunctionCalls = 0

def V(x, y, z):
    return -x * y * z

def Penalty(X):
    global r
    x, y, z = X.x, X.y, X.z
    return 1.0 / r * (max(0, -x)**2 + max(0, -y)**2 + max(0, -z)**2 + (2*x*y + 2*x*z + 2*y*z - 1)**2)

def VPenalty(X):
    global penaltyFunctionCalls
    penaltyFunctionCalls += 1

    x, y, z = X.x, X.y, X.z

    return V(x, y, z) + Penalty(X)

def RunPenaltyAlgorithm(X):
    return simplexMethod(VPenalty, X)

if __name__ == '__main__':
    x0 = Vector(0.1, 0, 0.4)
    #x0 = Vector(1, 1, 1)
    #x0 = Vector(0, 0, 0)
    r = 10 #baudos kooficentas
    iterations = 0
    epsilon = 1e-6
    #prev_x0 = Vector(2, 2, 2)
    prevPenalty = Penalty(x0) + 0.001
    currentPenalty = Penalty(x0)


    while prevPenalty - currentPenalty > 0 or x0.x < 0 or x0.y < 0 or x0.z < 0:
    #while abs(prevPenalty - currentPenalty) > epsilon:
    #while abs(x0.x - prev_x0.x) > epsilon or abs(x0.y - prev_x0.y) > epsilon or abs(x0.z - prev_x0.z) > epsilon:
        B_value = VPenalty(x0)
        #print(f"r: {r}, (x, y, z): {x0}, Penalty: {currentPenalty}, V(X) = {V(x0.x, x0.y, x0.z)}")
        print( f"r: {r}, (x, y, z): ({x0.x:.8f}, {x0.y:.8f}, {x0.z:.8f}), Penalty: {currentPenalty}, B(X, r) = {B_value:.6f}, V(X) = {V(x0.x, x0.y, x0.z):.6f}")

    #prev_x0 = x0

        x0 = RunPenaltyAlgorithm(x0)

        prevPenalty = currentPenalty
        currentPenalty = Penalty(x0)

        r/= 2
        iterations += 1

    print(f"""
          X = {x0}
          V(X) = {V(x0.x, x0.y, x0.z)}
          iterations = {iterations}
          penalty function calls = {penaltyFunctionCalls}
          """)