import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math; 

from numpy import sqrt, sin, cos, pi

pi = 3.1415926535

x_by_ws = []
ws = []

n = 5

def fun(x):
    return x**2

curr_w = 0.00
while(curr_w < 10):
    curr_w+=0.01
    curr_x=0
    curr_i = 0
    while(curr_i < n):
        curr_i += 0.1
        curr_x += fun(curr_i) * math.e ** (-1j * curr_w * curr_i)
    ws.append(curr_w)
    x_by_ws.append(abs(curr_x))

plt.plot(ws,x_by_ws)
plt.show()





