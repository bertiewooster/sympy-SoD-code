from sympy import Eq, solveset
from sympy.abc import x, y

eqn = Eq(x**2, y)
solutions = solveset(eqn, x)
print(solutions)

for solution in solutions:
    print(solution)
