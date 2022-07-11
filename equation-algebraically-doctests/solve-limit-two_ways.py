from sympy import Or, Symbol, solve

x = Symbol('x', real=True)

expr = (x-4)*(x-3)*(x-2)*(x-1)

solution = solve(expr, x)
print(solution)

solution_outside_2_3 = [v for v in solution if (v.is_real and Or(v<2,v>3))]
print(solution_outside_2_3)

solution_2_3 = solve((expr,x>=2,x<=3), x)
print(solution_2_3)
