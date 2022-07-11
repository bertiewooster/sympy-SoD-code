from sympy import solveset
from sympy.abc import x, y

solution_set = solveset(x**2 - y, x)
print(solution_set)

solution_list = list(solution_set)
print(solution_list)
