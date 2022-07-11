from sympy import sin, solve
from sympy.abc import x

solve(x**2 - sin(x), x)
