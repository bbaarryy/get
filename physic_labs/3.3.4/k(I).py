import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy

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

ks = [0.0046, 0.0062,0.0078, 0.0092, 0.0109 , 0.0154]
Is = [0.3,0.4,0.5,0.6,0.7,1]

plt.errorbar(Is,ks,fmt='o')
a,b,k,sigma_k = fun(Is,ks)

plt.plot([0,1],[0,k],label = 'Прямая зависимость Y=(' + str(k)[0:6] + "+-" + "0.0004"  + ')x')

plt.xlabel(r"Ток на германии, A",fontsize=20)
plt.ylabel(r"Коэффициент k = dU/dB",fontsize=20)

plt.legend(fontsize=20)
plt.grid()
plt.show()