from scipy.optimize import newton
from math import floor

n = int(input())
f = lambda x: x * (x + 1) / 2 - (n + 1)
g = lambda x: 2 * x + 1

v = newton(f, floor(n ** 0.5) + 1, fprime=g, maxiter=100)
print(n - floor(v) + 1)
