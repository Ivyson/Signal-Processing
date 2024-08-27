import sympy as sm

u = sm.Heaviside
t = sm.Symbol('t')
x = 2*sm.Heaviside(t)
y = 0.7*x.subs(t, t-1) + x
print(y)