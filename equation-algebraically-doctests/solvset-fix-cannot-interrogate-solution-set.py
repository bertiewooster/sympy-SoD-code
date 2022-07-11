from sympy import S, Symbol, solveset

x = Symbol('x')
y = Symbol('y', real=True, positive=True)

solution_set = solveset(x**2 - y, x, domain=S.Reals)
print(solution_set)

#Intersection({-sqrt(y), sqrt(y)}, Reals)
solution_list = list(solution_set)
print(solution_list)
#Traceback (most recent call last):
#    ...
#TypeError: The computation had not completed because of the undecidable set membership is found in every candidates.

