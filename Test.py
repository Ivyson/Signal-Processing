import sympy as sp

def get_function_input(prompt):
    """Prompt the user to input a function and return it as a sympy expression."""
    expr = input(prompt)
    return sp.sympify(expr)

def convolution(f, g, x):
    """Compute the convolution of two functions f and g with respect to x."""
    t = sp.symbols('t')
    return sp.integrate(f.subs(x, x - t) * g, (t, -sp.oo, sp.oo))

def fourier_transform(f, x, omega):
    """Compute the Fourier transform of function f with respect to variable x."""
    return sp.fourier_transform(f, x, omega)

def fourier_series(f, x, n, T):
    """Compute the Fourier series of function f with respect to variable x, up to n terms, with period T."""
    # Compute the Fourier series coefficients
    a0 = (2 / T) * sp.integrate(f, (x, -T/2, T/2))
    an = lambda k: (2 / T) * sp.integrate(f * sp.cos(2 * sp.pi * k * x / T), (x, -T/2, T/2))
    bn = lambda k: (2 / T) * sp.integrate(f * sp.sin(2 * sp.pi * k * x / T), (x, -T/2, T/2))

    # Construct the Fourier series
    series = a0 / 2
    for k in range(1, n + 1):
        series += an(k) * sp.cos(2 * sp.pi * k * x / T) + bn(k) * sp.sin(2 * sp.pi * k * x / T)
    
    return series

def series_expansion(f, x, n):
    """Compute the series expansion of function f around x = 0 up to order n."""
    return sp.series(f, x, 0, n)

def main():
    # Define symbols
    x, omega = sp.symbols('x omega')

    # Get function from user
    f = get_function_input("Enter the function f(x): ")
    
    # Perform Fourier Transform
    fourier_transform_result = fourier_transform(f, x, omega)
    print(f"Fourier Transform result: {fourier_transform_result}")

    # Perform Fourier Series
    n_terms = int(input("Enter the number of terms for the Fourier series: "))
    period = sp.Symbol('T')  # Period of the function
    fourier_series_result = fourier_series(f, x, n_terms, period)
    print(f"Fourier series (up to {n_terms} terms): {fourier_series_result}")

    # Perform Series Expansion
    n_terms_expansion = int(input("Enter the number of terms for series expansion: "))
    series_result = series_expansion(f, x, n_terms_expansion)
    print(f"Series expansion result: {series_result}")

if __name__ == "__main__":
    main()
