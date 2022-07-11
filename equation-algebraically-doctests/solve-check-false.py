from sympy import Symbol, sin, solve

x = Symbol("x")

solution_check_true = solve(sin(x)/x)  # 0 is excluded
print(solution_check_true)
# [pi]

solution_check_false = solve(sin(x)/x, check=False)  # 0 is excluded
print(solution_check_false)
# [0, pi]
