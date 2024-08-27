import sympy as sm
from scipy.integrate import quad
import numpy as np
t = sm.Symbol('t')
u = sm.Heaviside
equation = 5*u(t+4)+2*u(t+1)-3*u(t-3)-4*u(t-5)
fixequation = sm.lambdify(t, equation, 'numpy')
result, error = quad(fixequation, -2, 3)
print("The intergral results: ", result) ### Answer is supposed to be 33
sm.plot(equation, (t, -10, 10))
