import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt
from scipy.integrate import quad

from numpy import sqrt, sin, cos, pi

pi = 3.1415926535

N = 10

def fun(x):
    return abs(x)

def fsin(x,n):
    return abs(x) * sin(n*x)

def fcos(x,n):
    return abs(x) * cos(n*x)

ns = []
a_ns= []

def draw_app_fun():
    delta = 0.01

    xs = []
    ys = []
    x= -pi
    while x <= pi:
        xs.append(x)

        a0 = integrate.quad(fun, -pi, pi)[0]
        a0 *= (1/pi)

        fx = a0/2

        for n in range(1,N+1):
            an = (1/pi) * quad(fcos, -pi,pi, args = (n))[0]
            bn = (1/pi) * quad(fsin, -pi,pi, args = (n))[0]

            ns.append(n)
            a_ns.append(an)

            fx += an * cos(n*x) + bn * sin(n*x)
        
        ys.append(fx)
        x+=delta

    plt.plot(xs,ys)


draw_app_fun()
plt.grid()
plt.show()


