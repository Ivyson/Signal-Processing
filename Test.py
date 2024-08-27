<<<<<<< HEAD
import sympy as sym
t = sym.Symbol('t')
# equation = sym.Piecewise((1,(t > 0) & (t < 10)), (0, True))
equation = sym.exp(t)
fourier = sym.fourier_series(equation,(t, 0, 2*sym.pi))
truncated = fourier.truncate(4)
print(f"The dc component of the fourier series is: {fourier.a0}")
print(f"The Cosine Coefficient of the fourier series is: {fourier.an}")
print(f"The Sine Coefficient of the fourier series is: {fourier.bn}")
p1 = sym.plot(equation, (t, 0, 2*sym.pi), show=False, line_color = "red",legend = True)
p2 = sym.plot(truncated, (t, 0, 2*sym.pi), show=False, line_color = "blue",legend=True)
p1.extend(p2)
p1.show()
# def UserFunction():
#     # period = input("What is the period of the function: ")
#     variable = input("What is the indepedant variable in your equation: ")
#     t = sym.Symbol(variable)
#     number_equations = input("How many different equations does your graph have: ")
#     start, end = float(input("Where does your function start: "), input("Where does your function end"))
#     #From the start and end, i can get the period by having an equation : end - start, and this applies only if end > start, start - end if end < start, then start - end
#     equation1 = input("Enter your equation: -.e.g:- sym.sin(your_variable here) or sym.cos(your_variable here!): ")
#     if(end > start):
#         period = end - start
#     else:
#         period = start - end
#     return t,period, sym.sympify(equation1),
=======
>>>>>>> fab2a7be8a0b4125364e8dd66ae3f5df44724b09
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
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> fab2a7be8a0b4125364e8dd66ae3f5df44724b09
