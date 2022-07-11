from sympy import pprint, sin, solveset
from sympy.abc import x

solution = solveset(sin(x), x)
pprint(solution)
