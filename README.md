
# Signal Processing

Welcome to the Signal Processing repository! This repository is dedicated to developing and storing tools for my signal processing course. It includes functionalities for transforming and manipulating signals in various ways. This README will guide you on how to use the code effectively. Let’s dive into the continuous signal processing functionalities! 😎

## Notes

### Overview

This repository serves as an experimental lab for testing Python libraries based on the theory learned in the Signal Processing course. The repository is currently focused on preparing for Test 1 of the course, with a goal to organize functionalities for both discrete and continuous signals for easier implementation during the test.

### Continuous Functions Functionalities

1. **Finding Even and Odd Components of a Signal**
   - **Code Example (`file3.py`)**: This script defines a piecewise function, calculates its even and odd components, and integrates them. The even and odd components are obtained by flipping the function and averaging.
   - **Integration**: 
     ```python
     import sympy as sm
     from scipy.integrate import quad
     
     # Define the function and its flipped version
     x = sm.Piecewise(...)
     flipped_equation = x.subs(t, -t)
     
     # Calculate even and odd components
     xeven = (x + flipped_equation) / 2
     xodd = (x - flipped_equation) / 2
     
     # Convert to lambda functions for integration
     xeven_func = sm.lambdify(t, xeven, 'numpy')
     xodd_func = sm.lambdify(t, xodd, 'numpy')
     
     # Perform integration
     result, error = quad(xeven_func, -3, 3)
     inter, miss = quad(xodd_func, -3, 3)
     ```

2. **Finding Convolution**
   - **Convolution of continuous functions** can be done using numerical methods, often with the help of libraries such as `scipy`. This functionality is not directly covered in the provided files but is typically implemented using the convolution theorem and numerical integration.

3. **Finding the Fourier Series of a Function**
   - **Code Example (`file1.py`)**: This script computes the Fourier series of a function and plots it alongside the original function.
   - **Fourier Series Calculation**:
     ```python
     import sympy as sp
     
     # Define the function and Fourier series
     t = sp.Symbol('t')
     equation = sp.sin(t)
     T = 10
     fourier = sp.fourier_series(equation, (t, 0, T))
     truncated_series = fourier.truncate(40)
     
     # Print and plot the Fourier series
     sp.pprint(truncated_series.rewrite(sp.exp))
     ```
   - **Plotting**: Use `sympy.plot` to compare the Fourier series with the original function.

4. **Finding Integrals of Continuous Functions/Signals**
   - **Code Example (`file2.py`)**: This script demonstrates integration of a continuous function from 0 to \( t \).
   - **Integration**:
     ```python
     import sympy as sp
     
     # Define the function and integrate
     t = sp.Symbol('t')
     x = sp.sin(t)
     inter = sp.integrate(x, (t, 0, t))
     
     # Print the result
     sp.pprint(inter)
     ```

### Important Notes

- **Time Shifting Diagrams**: Calculating time shifts using Python is not recommended, and therefore, Question 2 in this repository is considered incorrect.
- **Convolution Mode**: For the purpose of this course, use convolution in "same" mode.
- **Signal Shifting**: `np.roll` performs a circular shift and is not a direct substitute for non-circular time shifting in signal processing. Handle time shifts carefully by adjusting indices rather than using `np.roll`.
Certainly! Here’s an updated README with a focus on the discrete part, incorporating the modifications for `file1.py` and `file2.py`:

### Discrete Time Signals and Systems

1. **Finding Even and Odd Components of a Signal**
   - **Code Example**: Not explicitly provided in the current files but can be implemented similarly to continuous signals.

2. **Finding Convolution**
   - **Code Example (`file1.py`)**: This script demonstrates how to perform convolution on two discrete sequences and plot the results.
   - **Steps**:
     ```python
     import numpy as np
     import matplotlib.pyplot as plt

     # Define two discrete sequences
     n = np.arange(-6, 7)
     x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0])
     h = np.array([0, 0, 0, -1, -1, 0, 1, 2, 3, 2, 1, 0, 0])

     # Perform convolution
     y = np.convolve(x, h, mode='same')

     plt.figure(figsize=(12, 6))
     plt.subplot(3, 1, 1)
     plt.stem(n, x, basefmt=" ")  # Plots the x[n] function 
     plt.title('Sequence x[n]')
     plt.xlabel('n')
     plt.ylabel('x[n]')

     plt.subplot(3, 1, 2)
     plt.stem(n, h, basefmt=" ")  # Plots the h[n] function 
     plt.title('Sequence h[n]')
     plt.xlabel('n')
     plt.ylabel('h[n]')

     plt.subplot(3, 1, 3)
     plt.stem(n, y, basefmt=" ")  # Plots the convolution result
     plt.title('Convolution y[n]')
     plt.xlabel('n')
     plt.ylabel('y[n]')

     plt.tight_layout()
     plt.show()
     ```

3. **Finding the Sum of Specific Terms in a Signal**
   - **Code Example (`file2.py`)**: This script calculates the sum of the terms of a discrete function within a specified range and plots the function.
   - **Steps**:
     ```python
     import numpy as np
     import matplotlib.pyplot as plt

     # Define the range of the independent variable
     n = np.arange(-10, 10)  # Array of integers from -10 to 9
     output = np.array([0, 0, 0, 1, 1, 2, 2, 3, 5, 3, 3, 2, 1, 0, 1, 1, 1, 1, 1, 1])

     # Find indices where n is between -3 and 0
     indices = np.where((n >= -3) & (n <= 0))
     selected_terms = output[indices]

     # Print the sum of the selected terms
     print(f"The sum of the terms of the function from -3 to 0 is: {np.sum(selected_terms)}")

     # Plot the discrete function
     plt.stem(n, output, label="Discrete Function")
     plt.legend()
     plt.show()
     ```

4. **Using Libraries**
   - **NumPy**: Utilized for array operations and convolution.
   - **Matplotlib**: Used for plotting discrete functions. Use `plt.stem` for plotting discrete signals.

### Important Notes

- **Time Shifting Diagrams**: Calculating time shifts using Python is not recommended, and therefore, Question 2 in this repository is considered incorrect.
- **Convolution Mode**: For the purpose of this course, use convolution in "same" mode.
- **Signal Shifting**: `np.roll` performs a circular shift and is not a direct substitute for non-circular time shifting in signal processing. Handle time shifts carefully by adjusting indices rather than using `np.roll`.
