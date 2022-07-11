from sympy import pprint, sin, solve, solveset
from sympy.abc import x
from sympy.calculus.util import periodicity

f = sin(x)
solution = solve(f, x)
print(solution)
print(periodicity(f, x))

solution_set = solveset(f, x)
pprint(solution_set)
