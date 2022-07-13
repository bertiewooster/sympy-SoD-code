from sympy import symbols, solve
from sympy.core.relational import Relational

x = symbols("x")
eq = solve([x >= 0.5, x <= 0.7])
[(i.rhs, i.rel_op, i.lhs) for i in [i.canonical for i in eq.atoms(Relational)]]
