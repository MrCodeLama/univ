import math

epsilon = 0.0001
rangeMin = 0
rangeMax = 1
iterationDihotomy = 1

def f(x):
    return x**4 + 4 * x - 2

def derivativeF(x):
    return 4*(x**3) + 4

def signum(x):
    if x < 0: return -1
    else: return 1

# Dihotomy method
def numberOfIterationsDihotomy():
    return math.floor(math.log2((rangeMax - rangeMin) / epsilon))

def dihotomy(a,b):
    global iterationDihotomy
    print(f"{iterationDihotomy}) {a} {b} {(a+b)/2}")
    if iterationDihotomy < numberOfIterationsDihotomy():
        iterationDihotomy += 1
        a0 = a
        b0 = b
        x0 = (a0 + b0) / 2
        if f(x0) == 0:
            return x0
        else:
            if (signum(f(x0)) == signum(f(a0))):
                a0 = x0
            if (signum(f(x0)) == signum(f(b0))):
                b0 = x0
            return dihotomy(a0, b0)
    else:
        return (a + b) / 2


m1 = derivativeF(rangeMin)
M1 = derivativeF(rangeMax)
q=(M1-m1)/(M1+m1)
tau = 2/(m1+M1)
z0 = (rangeMax - rangeMin)/2
x0 = (rangeMax + rangeMin)/2
iterationRelaxation = 0

def numberOfIterationsRelaxation():
    return math.floor(math.log(abs(z0)/epsilon)/math.log(1/q)) + 1

def relaxation(a,b, xPrev):

    global iterationRelaxation
    print(f"{iterationRelaxation}) {xPrev} {(q/(1-q))*math.fabs(xPrev - tau*(f(xPrev)) - xPrev)}")
    if iterationRelaxation < numberOfIterationsRelaxation():
        iterationRelaxation += 1
        return relaxation(a, b, xPrev - tau*(f(xPrev)))
    else:
        return xPrev


dihotomy_result = dihotomy(rangeMin, rangeMax)
relaxation_result = relaxation(rangeMin, rangeMax, x0)
print(f"Result of dihotomy:   {dihotomy_result}  \nnumber of steps: {numberOfIterationsDihotomy()}")
print(f"Result of relaxation: {relaxation_result}  \nnumber of steps: {numberOfIterationsRelaxation()}")
print(f"{m1} {M1} {q} {tau} {z0} {x0}")