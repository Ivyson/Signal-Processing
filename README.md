# Signal-Processing

The objective of this Repository is to store and develop tools for my signal processing course. This includes, but is not limited to, transforming signals and manipulating them in various ways. The functionality of this code will evolve as new concepts are introduced in class. This README file will provide guidance on how to use the code effectively. Stick around, the science is about to begin 😎😎!
## Notes
- This whole repository is an experimental lab whereby i test python libraries on the theory we learn in Signal - Processing, As of Today, the repo will be used to prepare for test 1 of Signal-Processing. The goal is to separate the functionalities from Discrete and Continous to ensure that the implementation of this is easy in the test venue
  - Continous Functions Functionalities:
    - Finding Even and Odd Components Of any given signal
    - Finding convolution 
    - Finding the Fourier Series of a function,
    Now for this, There are a few key things to remember: For tests purposes, the representation of a fourier series should always be in a complex number form and not the Trigonometric form. Draw the original function first, this is to confirm that the fourier series will be correct! then draw the approximation on top of the original, if the original can not be distinguished from the fourier series approximation, then this means that the approximation is roughly correct.
    To represent the Fourier Series in a complex manner use  ` fourierdata.truncate[Number of terms].rewrite(sympy.exp) `, print the results on the console 
    - Finding integrals of Continous functions/Signals
  - Discrete Time Signals and Systems
    - Finding even and odd components of a signal
    - The primary library for this is ` numpy ` for arrays, and ` matplot ` for plotting the discrete functions: Discrete functions use ` plt.stem ` instead of ` plt.plot `
    - Finding Convolution of the two signals
    - Finding summation of the signal, this normally is mixed with the even and odd functions
