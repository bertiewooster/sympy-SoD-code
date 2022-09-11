from sympy import roots
from sympy.abc import x

fifth_order = x ** 5 - x + 1

roots(fifth_order, x, strict=True)
