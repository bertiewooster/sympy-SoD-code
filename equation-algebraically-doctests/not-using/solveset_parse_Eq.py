from sympy import parse_expr, solveset
from sympy.abc import x

expr = "Eq(x**2, y)"
parsed = parse_expr(expr)
print(parsed)
solutions = solveset(parsed, x)
print(solutions)
