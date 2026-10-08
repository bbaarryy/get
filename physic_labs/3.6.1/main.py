import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np

xs1 = [20,30,40,50,60,80,100,120,140,160,180,200]
for i in range(len(xs1)):
    xs1[i] = 1 / xs1[i] * 10**3

ls1 = [37,27,21,17,15,12,10,8,7,6,5.5,5]

xs2 = [5,4,3.5,3,2.5,1,0.5,0.2]

# for i in range(len(xs2)):
#     xs2[i] = 1 / xs1[i] / 10**3

ls2 = [5,4,3.5,3,2.5,1,0.5,0.2]

#AMMMM

ms = [20,30,40,50,60,70,80,90,100]
vs = [54.88,81.75,110.1,138,161.7,190,220,244.8,270]

big = 535.7

for i in range(len(vs)):
    vs[i] = vs[i] / (big / 2)


plt.plot(vs,ms)


#plt.plot(xs2,ls2)


def fun(arrx,arry):
    x = arrx
    y = arry

    xy_av = 0
    x_2_av = 0
    y_2_av = 0
    x_av=0
    y_av = 0
    for i in range(len(arrx)):
        x_av += x[i]
        y_av += y[i]
        xy_av += x[i] * y[i]
        x_2_av += x[i] * x[i]
        y_2_av += y[i] * y[i]
    
    x_av /= len(x)
    y_av /= len(y)
    xy_av /= len(x)
    x_2_av /= len(x)
    y_2_av /= len(x)

    a = (xy_av - x_av * y_av)/(x_2_av - x_av ** 2)
    b = y_av - a * x_av
    k = xy_av / x_2_av

    sigma_a = 1/(7**(0.5))*(abs( (y_2_av - y_av ** 2)/(x_2_av - x_av**2) - a*2 )) ** 0.5
    sigma_b = sigma_a * (x_2_av - x_av**2)**0.5

    return(a,b,k,sigma_a,sigma_b)

a,b,k,sigma_a,sigma_b = fun(xs2,ls2)
print(a,b)
y = 5
#plt.plot([0,y],[b,a*y+b],label="Наилучшая прямая: y = 0.72x + 2.19")
#plt.plot([0,y],[0,k*y])

#plt.plot(x_smooth, y_smooth)

plt.xlabel(r"Отношение амплитуд * 2",fontsize=20)
plt.ylabel(r"Глубина модуляции, %",fontsize=20)
plt.legend(fontsize = 20)
plt.grid()
plt.show()