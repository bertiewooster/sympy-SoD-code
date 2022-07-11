from sympy import diff, solve
from sympy.abc import x

f = x**3 + x**2 - x
derivative = diff(f, x)
critical_points = solve(derivative, x, dict=True)
print(critical_points)
point1, point2 = critical_points
print(f.subs(point1))
print(f.subs(point2))
curvature = diff(f, x, 2)
print(curvature.subs(point1))
print(curvature.subs(point2))
