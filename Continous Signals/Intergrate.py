import sympy as sp
# Define symbolic variables
t = sp.Symbol('t')
tau = sp.Symbol('tau')
x = sp.sin(t)
# Perform intergration
inter = sp.integrate(x, (t, 0, t)) #t is the main variable, intergrating from 0 to t
# Display the result
sp.pprint(inter)