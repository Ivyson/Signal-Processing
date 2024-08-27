import sympy as sm
from scipy.integrate import quad
import numpy as np

# Define the actual symbol/ Variable
t = sm.Symbol('t')

# Define the Original Function
equation = sm.Piecewise((t + 6, (t > -6) & (t < -3)), 
                        (3, (t > -3) & (t < -1)), 
                        (-t + 2, (t > -1) & (t < 0)), 
                        (2, (t > 0) & (t < 4)), 
                        (0, True))

# Define the Flipped Function
flipped_equation = equation.subs(t, -t)

# Finding the Even Component
xeven = (equation + flipped_equation) / 2
xodd = (equation-flipped_equation) / 2
xeven_func = sm.lambdify(t, xeven, 'numpy') # Convert the even component to a lambda function for integration
xodd_func = sm.lambdify(t, xodd, 'numpy')
inter, miss = quad(xodd_func, -3, 3)
result, error = quad(xeven_func, -3, 3)
print("Integration even result:", result)
print("Integration odd result:", inter)
# print("Integration error:", error)
# sm.plot(equation, flipped_equation, (t, -8, 8), show=True, legend=True, labels=['Original Function', 'Flipped Function'])