from sympy import solve
from sympy.abc import x, y

expr = x**2 - (y**5 - 3*y**3 + y**2 - 3)

solution_simplify_true = solve(expr, x, dict=True)  # 0 is excluded
print(solution_simplify_true)
#[{x: -sqrt(y**5 - 3*y**3 + y**2 - 3)}, {x: sqrt(y**5 - 3*y**3 + y**2 - 3)}]

solution_simplify_false = solve(expr, x, dict=True, simplify=False)  # 0 is excluded
print(solution_simplify_false)
#[{x: -sqrt((y + 1)*(y**2 - 3)*(y**2 - y + 1))}, {x: sqrt((y + 1)*(y**2 - 3)*(y**2 - y + 1))}]
