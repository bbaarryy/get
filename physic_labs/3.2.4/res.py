import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter1d

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

    sigma_k = 1/(len(x)**0.5)*(y_2_av / x_2_av - k ** 2)**0.5

    return(a,b,k,sigma_k)
U_0 = 12.6
Vs_0 = 5960

Us = [4.96, 5.68, 6.8, 8.44, 10, 12.6, 10.8, 8, 6.12, 4.76]
Vs = [6740, 6584,6428,6272,6116,5960, 5804,5648,5492, 5336]

U_02 = 6.68
Vs_02 = 5960

Us2 = [5.1, 5.6, 6, 6.08, 6.56, 6.68, 6.32, 5.6, 4.6, 3.92]
Vs2 = [6740, 6584,6428,6272,6116,5960, 5804,5648,5492, 5336]


(Vs2.reverse())
(Us2.reverse())

xs = []
ys = []

xs2 = []
ys2 = []
for i in range(len(Us)):
    xs.append(Vs[i] / Vs_0)
    ys.append(Us[i] / U_0)

    xs2.append(Vs2[i] / Vs_02)
    ys2.append(Us2[i] / U_02)

plt.scatter(xs,ys)
plt.scatter(xs2,ys2)
plt.legend(fontsize=20)

plt.plot(xs2,ys2,label = "R = 600 Om")
plt.plot(xs,ys,label = "R = 290 Om",linestyle = "-.")

# 1 / sqrt(2)
plt.plot([0.9,1.2],[1/(2)**0.5, 1/(2)**0.5], linewidth = 3, linestyle = "--")
plt.xlabel("Отношение частоты к резонансной",fontsize = 20)
plt.ylabel("Отношение амплитуд",fontsize = 20)
plt.legend(fontsize = 20)
plt.grid()
plt.show()
