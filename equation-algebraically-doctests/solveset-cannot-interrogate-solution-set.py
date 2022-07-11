from sympy import S, solveset, symbols

x, y = symbols('x, y')

solution_set = solveset(x**2 - y, x, domain=S.Reals)
print(solution_set)

#Intersection({-sqrt(y), sqrt(y)}, Reals)
list(solution_set)
#Traceback (most recent call last):
#    ...
#TypeError: The computation had not completed because of the undecidable set membership is found in every candidates.

