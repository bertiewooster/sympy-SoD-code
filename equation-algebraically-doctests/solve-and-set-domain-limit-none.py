from sympy import Symbol, solve, solveset

x = Symbol('x'); x

solution = solve(x ** 4 - 256, x, dict=True)
print(solution)

solution_set = solveset(x ** 4 - 256, x)
print(solution_set)
