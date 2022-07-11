from sympy import S, solveset, symbols

x, y = symbols('x, y')
solution_set = solveset(x**2 - y, x, domain=S.Reals)
print(solution_set)
#Intersection({-sqrt(y), sqrt(y)}, Reals)
solution_set_args = solution_set.args
print(solution_set.args)
#(Reals, {-sqrt(y), sqrt(y)})
list(solution_set_args[1])
#[sqrt(y), -sqrt(y)]
