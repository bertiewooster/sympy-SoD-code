from sympy import parse_expr, solve, solveset
from sympy.abc import x

expr = "x^2 = y"
parsed = parse_expr(expr, transformations="all")
print(parsed)
solutions = solve(parsed, x, dict=True)
print(solutions)
for solution in solutions:
    for key, val in solution.items():
        print(val)

solutions_set = solveset(parsed, x)
print(solutions_set)
