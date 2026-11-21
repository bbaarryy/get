import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np

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

    sigma_k = 1/(6**0.5)*(y_2_av / x_2_av - k ** 2)**0.5

    return(a,b,k,sigma_k)

Rs = np.array([50,40,30,10,5,2.5])
Xs = [15.5, 15.1, 14.4, 11, 8.3, 4.7]

Rs = Rs*1000 + 610



plt.plot(Rs, Xs)
plt.scatter(Rs, Xs)

plt.hlines(18.8 / math.e,xmin = 0,xmax = 50000,linestyles='--')

plt.xlabel(r"Сопротивление R + R_0, Ком",fontsize=20)
plt.ylabel("Отклонение, мм",fontsize=20)

plt.grid()
plt.show()
###
# plt.legend(fontsize=20)
# plt.grid()
# plt.show()