from sympy import S, solveset
from sympy.abc import x

solution = solveset(x**2 + 1, x, domain=S.Reals)
print(solution)
