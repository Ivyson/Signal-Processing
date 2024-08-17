import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Function to evaluate user input as a function
def get_user_defined_signal():
    signal_str = input("Enter a signal function of p (e.g., 'np.sin(p)', 'p**2', 'np.exp(-p) * np.sin(p)'): ")
    return lambda p: eval(signal_str)

# Function to calculate the nth coefficient of the Fourier series
def fourier_coefficient(n, f, L):
    a0 = quad(lambda x: f(x), -L, L)[0] / (2 * L)
    an = quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)[0] / L
    bn = quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)[0] / L
    return a0, an, bn

# Number of terms in the Fourier series
N = eval(input("How Many terms do you want to approximate: "))
L = eval(input("What is your period: "))

# Get user-defined signal
Signal = get_user_defined_signal()

# Retrieve coefficients from 0 to N
coefficients = [fourier_coefficient(n, Signal, L) for n in range(N)]

# Calculate the Fourier series
def fourier_series(x, coeffs):
    a0 = coeffs[0][0]
    series = a0 / 2 
    for n in range(1, len(coeffs)):
        an, bn = coeffs[n][1], coeffs[n][2]
        series += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    return series

# Plot the original and approximated signals
x_vals = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
original = np.vectorize(Signal)(x_vals)
approximation = fourier_series(x_vals, coefficients)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(x_vals, original, label="Original Graph", color="Pink")
plt.title("Original graph")
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_vals, approximation, label="Fourier Approximation", color="red")
plt.title("Fourier Series")
plt.ylabel("Y")
plt.xlabel("X")
plt.tight_layout()
plt.grid(True)
plt.show()