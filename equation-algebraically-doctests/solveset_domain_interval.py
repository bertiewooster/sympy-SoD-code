from sympy import Interval, pi, sin, solveset
from sympy.abc import x

solution = solveset(sin(x), x, Interval(-pi, pi))
print(solution)
