import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt
from scipy.integrate import quad
from numpy.fft import fft, ifft

from numpy import sqrt, sin, cos, pi

pi = 3.1415926535

correct_ys = [pi, 0, pi]
correct_xs = [-pi,0,pi]

#plt.plot(correct_xs, correct_ys, color = 'g')

N = 6

def fun(x):
    return x**2

def fsin(x,n):
    return x**2 * sin(n*x)

def fcos(x,n):
    return x**2 * cos(n*x)

def draw_app_fun():
    delta = 0.01

    xs = []
    ys = []
    x= -pi

    waves_as = []
    waves_fs = []
    while x <= pi:
        xs.append(x)

        a0 = integrate.quad(fun, -pi, pi)[0]
        a0 *= (1/pi)

        fx = a0/2

        for n in range(1,N+1):
            an = (1/pi) * quad(fcos, -pi,pi, args = (n))[0]
            bn = (1/pi) * quad(fsin, -pi,pi, args = (n))[0]

            fx += an * cos(n*x) + bn * sin(n*x)
            waves_as.append(an)
            waves_fs.append(bn)

        ys.append(fx)
        x+=delta
    
    
    plt.plot(xs,ys)

draw_app_fun()
plt.grid()
plt.show()


