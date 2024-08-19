import sympy as sp
t = sp.Symbol('t')

# Define the piecewise function with a default condition (covering entire range)
# equation = sp.Piecewise((t, (t > 1) & (t < 4)), (1, (t > 4) & (t < 10)), (0, True))
equation = sp.sin(t)
T = 10  
forier = sp.fourier_series(equation, (t, 0, T))

truncated_series = forier.truncate(40)

sp.pprint(truncated_series)

p1 = sp.plot(truncated_series, (t, 0, T), show=False, line_color='blue', label='Fourier Series')
p2 = sp.plot(equation, (t, 0, T), show=False, line_color='red', label='Original Function')

p1.extend(p2)
p1.show()