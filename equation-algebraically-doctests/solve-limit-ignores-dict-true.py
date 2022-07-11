from sympy import Symbol, solve

x = Symbol('x', real=True)

expr = (x-4)*(x-3)*(x-2)*(x-1)

solution = solve(expr, x, dict=True)
print(solution)

solution_2_3 = solve((expr,x>=2,x<=3), x, dict=True)
print(solution_2_3)
