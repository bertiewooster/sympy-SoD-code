from sympy import solve
from sympy.abc import x

solutions = solve(x**5 - x - 1, x, dict=True)
print(solutions)
#[{x: CRootOf(x**5 - x - 1, 0)}, {x: CRootOf(x**5 - x - 1, 1)}, {x: CRootOf(x**5 - x - 1, 2)}, {x: CRootOf(x**5 - x - 1, 3)}, {x: CRootOf(x**5 - x - 1, 4)}]
[s[x].n(3) for s in solutions]
#[1.17, -0.765 - 0.352*I, -0.765 + 0.352*I, 0.181 - 1.08*I, 0.181 + 1.08*I]
