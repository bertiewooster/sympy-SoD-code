from sympy import solve
from sympy.abc import x, y

solution = solve(x ** 2 - y, x, dict=True)
print(solution)
