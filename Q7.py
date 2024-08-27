import matplotlib.pyplot as plt
import numpy as np
import sympy as sm

# # Define the time values
# t_values = np.arange(-4, 6)  # from -4 to 5

# # Define the signal values
# x_values = [0, -1, -1, 0, 1, 2, 3, 2, 1, 0]  # corresponding to t_values

# # Define the actual symbol/ Variable
# t = sm.Symbol('t')

# # Create a piecewise function using SymPy
# equation = sm.Piecewise(
#     (0, t < -4),
#     (-1, (t >= -4) & (t < -3)),
#     (-1, (t >= -3) & (t < -2)),
#     (0, (t >= -2) & (t < -1)),
#     (1, (t >= -1) & (t < 0)),
#     (2, (t >= 0) & (t < 1)),
#     (3, (t >= 1) & (t < 2)),
#     (2, (t >= 2) & (t < 3)),
#     (1, (t >= 3) & (t < 4)),
#     (0, t >= 4)
# )

# # Define the Flipped Function
# flipped_equation = equation.subs(t, -t)

# # Finding the Even Component
# xeven = (equation + flipped_equation) / 2

# # Integrate the even component over the range [-4, 5]
# integral_result = sm.integrate(xeven, (t, -4, 5))

# print("Integral result:", integral_result)

# # Convert sympy expression to numpy function for plotting
# x_t_func = sm.lambdify(t, equation, 'numpy')
# flipped_x_t_func = sm.lambdify(t, flipped_equation, 'numpy')

# # Generate values for t
# t_values_plot = np.linspace(-10, 10, 400)

# # Calculate y values for x(t) and flipped x(t)
# x_t_values = x_t_func(t_values_plot)
# flipped_x_t_values = flipped_x_t_func(t_values_plot)

# # Plot the Original and Flipped Functions
# plt.figure(figsize=(10, 6))
# plt.plot(t_values_plot, x_t_values, label='Original Function')
# plt.plot(t_values_plot, flipped_x_t_values, label='Flipped Function', linestyle='--')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('Original and Flipped Functions')
# plt.legend()
# plt.grid(True)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt


n_values = np.arange(-14, 14)

# Define the index values
index = [0, -1, -1, 0, 1, 2, 3, 2, 1, 0]


xn = np.zeros_like(n_values, dtype=float) ## Make the whole array output zeroo only and will change some of the values

for i in range(len(index)):
    xn[10 + i] = index[i]  

yn = (np.roll(xn, 3) + xn) / 2# Roll shifts the function 3 units to the right, yn = (xn(n-3)+xn) 


n = 10   # Define n as the midpoint of n_values for filtering

selected_terms = yn[(n_values >= -3) & (n_values <= 3)] # For the sum, I only need  to consider the terms from n = -3 to n = 3

print("Sum of selected terms:", np.sum(selected_terms))

# Plot the results
plt.stem(n_values, yn, label="Spider")
plt.title("Discrete Function yn")
plt.xlabel("n")
plt.ylabel("yn")
plt.legend()
plt.grid(True)
plt.show()
