import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def square_wave(x):# Define the square wave function
    return 1 if (x % (2 * np.pi)) < np.pi else -1


def Signal(p):
    return np.sin(p)

# Calculate the nth coefficient of the Fourier series, for this case, calculate 11 terms
def fourier_coefficient(n, f, L):
    a0 = quad(lambda x: f(x), -L, L)[0] / (2 * L)
    an = quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)[0] / L
    bn = quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)[0] / L
    return a0, an, bn


N = 10 # Number of terms in the Fourier series
L = np.pi  # Period of the sine function


coefficients = [fourier_coefficient(n, Signal, L) for n in range(N)] ## Retrieve the coeffiecients form 0 to 10

# This calculates the whole fourier series
def fourier_series(x, coeffs):
    a0 = coeffs[0][0]
    series = a0 / 2
    for n in range(1, len(coeffs)):
        an, bn = coeffs[n][1], coeffs[n][2]
        series += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    return series


x_vals = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
original = np.vectorize(Signal)(x_vals)
approximation = fourier_series(x_vals, coefficients)
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(x_vals, original, label="Original Graph",color="Pink")
plt.title("Original graph")
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)
# hold
# plt.figure(2)
plt.subplot(2,1,2)
plt.plot(x_vals, approximation, label="Fourier Approximation",color="red")
plt.title("Fourier Series")
plt.ylabel("Y")
plt.xlabel("X")
plt.tight_layout()
plt.grid(True)
plt.show()
