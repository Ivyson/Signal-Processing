import numpy as np
import matplotlib.pyplot as plt

# Define the discrete signals
x = np.array([2, 3, 2])  # Example signal x[n]
h = np.array([ -1, -1, 0, 1, 2, 3, 2, 1])    # Example signal h[n]

# Perform convolution
y = np.convolve(x, h, mode='same')  # Convolution of x and h

# Define the range for plotting
n_x = np.arange(len(x))  # Indices for x
n_h = np.arange(len(h))  # Indices for h
n_y = np.arange(len(y))  # Indices for y
print(y)
# Determine the index for n = 1 in the result of convolution
n = 1
index_y = np.where(n_y == n)[0]  # Find index in y where n_y == n

# Check if the index exists
if index_y.size > 0:
    value_at_n = y[index_y[0]]
    print(f"Convolution value at n = {n}: {value_at_n}")
else:
    print(f"No convolution result for n = {n}")

# Plot the signals and their convolution
plt.figure(figsize=(12, 8))

# Plot signal x
plt.subplot(3, 1, 1)
plt.stem(n_x-10, x)
plt.title('Signal x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

# Plot signal h
plt.subplot(3, 1, 2)
plt.stem(n_h-10, h)
plt.title('Signal h[n]')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)

# Plot the convolution result y
plt.subplot(3, 1, 3)
plt.stem(n_y, y)
plt.title('Convolution y[n]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
