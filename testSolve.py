import sympy as sp
from sympy.solvers import solve


# 94A + 22B = 8400
# 34A + 67B = 5400

eq1= sp.Eq(94*x+22*y-8400) 
eq2 = sp.Eq(34*x+67*y-5400)
output = solve([eq1,eq2],dict=True)
print(ouptput)