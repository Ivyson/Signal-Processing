# Signal-Processing

The objective of this Repository is to store and develop tools for my signal processing course. This includes, but is not limited to, transforming signals and manipulating them in various ways. The functionality of this code will evolve as new concepts are introduced in class. This README file will provide guidance on how to use the code effectively. Stick around, the science is about to begin 😎😎!

## Usage

I primarily use <del> `scipy` </del> `sympy` , `matplotlib`, and `numpy` in this project. However, the scope may expand as the problems become more complex. To ensure that the necessary libraries are installed and up-to-date, please refer to the `requirements.txt` file, which will contain the updated list of required libraries.
The code does not yet accept user inputted signals, i shall do that research and see how can i fiddle with that!

### Fourier Series Approximation

The first scripts in this repository demonstrates how to compute and visualize the Fourier Series approximation of a given function. In this example, the Fourier Series is used to approximate a simple sine function, but it can be hanged to approximate other periodic functions(The power is in your hands!).

#### Code Explanation

- **Function Definitions**:
  - `square_wave(x)`: A helper function (currently not in use) that defines a square wave. It returns `1` if the input `x` is in the first half of the wave's period and `-1` otherwise.
  - `Signal(p)`: Defines the signal function. In this case, it's a simple sine wave (You can change it to any preffered function).
  
- **Fourier Coefficient Calculation**:
  - `fourier_coefficient(n, f, L)`: This function calculates the Fourier coefficients \(a_0\), \(a_n\), and \(b_n\) using numerical integration (via `scipy.integrate.quad`). These coefficients are important for constructing the Fourier Series formula.

- **Fourier Series Construction**:
  - `fourier_series(x, coeffs)`: This function reconstructs the signal using the calculated Fourier coefficients.

#### How to Use

1. **Run the Script**: The script will calculate and display both the original signal and its Fourier approximation over a range of values. 

2. **Customization**: 
    - Modify the `Signal(p)` function to your desired periodic signal.
    - Adjust `N` (the number of terms in the Fourier Series) to improve the accuracy of the approximation.
  
3. **Visualization**: The output includes a plot comparing the original signal with its Fourier Series approximation.

### Convolution of Two Functions

The second script demonstrates how to convolve two functions: an impulse response and a linear function.

#### Code Explanation

- **Function Definitions**:
  - `impulse_response(t)`: Defines a simple impulse response function, which alternates between 1 and -1 over a given period.
  - `linear_function(t)`: Defines a linear function \(y = t\), which represents a simple increasing trend over time.

- **Convolution**:
  - The convolution of the impulse response and linear function is computed using `np.convolve` with `mode='same'`, ensuring the output has the same length as the input.

#### How to Use

1. **Run the Script**: The script will plot the impulse response, the linear function, and their convolution.

2. **Customization**:
    - Modify the `impulse_response(t)` and `linear_function(t)` functions to represent different signals.
    - Adjust the `t` range if you need to analyze signals over different time intervals.
  
3. **Visualization**: The script generates three subplots showing the individual functions and their convolution.

### Future Enhancements

- **Dynamic Function Input**: Currently, the code does not accept user-defined functions as input. I'm working on allowing dynamic function input so that you can easily apply Fourier transforms and convolutions to any arbitrary function without modifying the code.

### Requirements

Please ensure that you have the necessary Python libraries installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```
