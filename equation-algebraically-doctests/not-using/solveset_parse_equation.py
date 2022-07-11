from sympy import parse_expr, solveset
from sympy.abc import x

expr = "x ** 2 = y"
parsed = parse_expr(expr, transformations="all")
print(parsed)
solutions = solveset(parsed, x)
print(solutions)
