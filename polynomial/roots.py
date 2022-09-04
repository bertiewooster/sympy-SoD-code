from sympy import nroots, real_roots, roots, solve
from sympy.abc import a, b, x

r = roots((x + a) ** 2 * (x - b), x)
print(r)
print(f"{a=}")
print(f"{b=}")
