from sympy import solve, solveset
from sympy.abc import x, y

solve(x ** 2 - y, x, dict=True)
#[{x: -sqrt(y)}, {x: sqrt(y)}]

solveset(x**2 - y, x)
#{-sqrt(y), sqrt(y)}
