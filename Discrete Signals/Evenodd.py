import numpy as np 
import matplotlib.pyplot as plt

# Define the range of the independant variable , normally its n in discrete
n = np.arange(-10, 10) # Created an array of integers from - 10 to 9
output = np.array([0, 0, 0, 1, 1, 2, 2, 3, 5, 3,3, 2, 1, 0,1,1,1,1,1,1]) # Places the corresponding output to the n input
indices = np.where((n >= -3) & (n <= 0)) # This line takes in the indices whereby n is between this range
selected_terms = output[indices]
print(f"The sum of the terms of the function from -3 to 0 is : {np.sum(selected_terms)}")
plt.stem(n, output, label="Discrete Function")
plt.legend()
plt.show()