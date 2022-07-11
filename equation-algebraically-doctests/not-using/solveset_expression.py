from sympy import solveset
from sympy.abc import x, y

solution = solveset(x**2 - y, x)
print(solution)
