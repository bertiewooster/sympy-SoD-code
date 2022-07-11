from sympy import Symbol, solve

x = Symbol('x', real=True)

solution_range = solve(((x-4)*(x-3)*(x-2)*(x-1)), x, dict=True)
print(solution_range)
