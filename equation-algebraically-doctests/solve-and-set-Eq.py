from sympy import Eq, solve, solveset
from sympy.abc import x, y

eqn = Eq(x**2, y)
# print(eqn)
# solutions = solve(eqn, x, dict=True)
# print(solutions)
solve(eqn, x, dict=True)
# solutions_set = solveset(eqn, x)
# print(solutions_set)
# for solution_set in solutions_set:
#     print(solution_set)
