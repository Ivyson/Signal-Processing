import numpy as np
import matplotlib.pyplot as plt

# Define the impulse response function (eg## a simple impulse)
def impulse_response(t):
    return np.where((t % (2 * np.pi)) < np.pi, 1, -1)

# Define a continous function y= t.....
def linear_function(t):
    return t

t = np.linspace(-5, 5, 1000) ## have a function starting at -5 to 5, plotting 1000 points 

impulse = impulse_response(t)
linear = linear_function(t)

convolution = np.convolve(impulse, linear, mode='same')

# Plot the original functions and their convolution
fig, ax = plt.subplots(3, 1, figsize=(10, 8))

# Plot the impulse response function
ax[0].plot(t, impulse, label='Impulse Response')
ax[0].set_title('Impulse Response Function')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].legend()

# Plotsecond function(Linear function here)
ax[1].plot(t, linear, label='Linear Function (y = x)', color='orange')
ax[1].set_title('Linear Function')
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Amplitude')
ax[1].legend()

# Plot the convolution
convolution_t = np.linspace(-10, 10, len(convolution))  #This needs to be adjusted for when the limit of the convolution is outside this limit
ax[2].plot(convolution_t, convolution, label='Convolution', color='green')
ax[2].set_title('Convolution of Impulse Response and Linear Function')
ax[2].set_xlabel('Time')
ax[2].set_ylabel('Amplitude')
ax[2].legend()

plt.tight_layout() ## This ensures that the graphs do not overlap
plt.show()
