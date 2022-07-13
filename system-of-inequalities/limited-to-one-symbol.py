from sympy import solve, symbols

x, y = symbols("x y")
from sympy.abc import x, y

solve([x ** 2 < y, x > 0], x)
# Traceback (most recent call last):
#     ...
# NotImplementedError: inequality has more than one symbol of interest.
