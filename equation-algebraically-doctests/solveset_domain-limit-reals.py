from sympy import S, solveset
from sympy.abc import x

solution = solveset(x**4 - 256, x, domain=S.Reals)
print(solution)
