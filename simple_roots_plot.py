# simple_roots_plot

# this program is designed to plot a simply function on an y-x grid and determine its roots

import numpy as np
import matplotlib.pyplot as plt
from math import *

def bisection(f, a, b, epsilon):
    a_n = a
    b_n = b
    while abs(a_n - b_n) > epsilon: # until interval is small enough
        mid = (a_n + b_n) / 2 # find midpoint
        f_mid = f(mid)
        if f(a_n) * f_mid < 0: # check if f(x) sign changes in left interval
            a_n = a_n
            b_n = mid
        elif f(b_n) * f_mid < 0: # check if f(x) sign changes in right interval
            a_n = mid
            b_n = b_n
        elif abs(f_mid) < epsilon: # f(midpoint) was close enough to 0
            # return the midpoint
            return mid
        else: # no sign change, so root is not in interval
            return None
    return (a_n + b_n) / 2 # return final midpoint


def function(x):
    y = (cosh(x) * cos(x) - 150)
    return y
 
x_values = np.arange(-10, 11, 0.1)
y_values = [(cosh(x) * cos(x) - 150) for x in x_values]
plt.plot(x_values, y_values, color="black", label = "cosh(x) * cos(x) - 150")

x_axis = np.full(len(range(-500, 501)), 0)
plt.plot(x_axis, range(-500, 501), '--', color="grey")

y_axis = np.full(len(range(-10, 11)), 0)
plt.plot(range(-10, 11), y_axis, '--', color="grey")

roots = []
roots.append(bisection(function, -8, -7, 0.1))
roots.append(bisection(function, -7, -5, 0.1))
roots.append(bisection(function, 5, 7, 0.1))
roots.append(bisection(function, 7, 8, 0.1))
plt.scatter(roots, np.zeros(len(roots)), color="red", label="Roots") 

plt.ylim([-500, 500]) # constrain plot dimensions
plt.xlim([-10, 10])
plt.legend()
plt.show() # show plot to screen
