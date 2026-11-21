import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import CubicSpline

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


Ts_0 = 12.6
Vs_0 = 5960

Ts = [6.4, 9.2, 12.4, 16.4, 24.4, 39.2, 53.6, 65.2, 73.2, 78.2]
Vs = [6740, 6584,6428,6272,6116,5960, 5804,5648,5492, 5336]

Ts_02 = 6.68
Vs_02 = 5960

Ts2 = [11.2, 14, 16.4, 21.6, 28.8, 36.4, 46.4, 58.2, 62.4, 68.4]
Vs2 = [6740, 6584,6428,6272,6116,5960, 5804,5648,5492, 5336]

xs = []
ys = []
xs2 = []
ys2 = []
for i in range(len(Ts2)):
    dPhi = 2 * 3.1415 * Vs[i] * Ts[i] / (10 ** 6)
    dPhi2 = 2*3.1415 * Vs2[i] * Ts2[i] / (10 ** 6)

    xs.append(dPhi)
    xs2.append(dPhi2)

    W = Vs[i] / Vs_0
    W2 = Vs2[i] / Vs_02
    ys.append(W)
    ys2.append(W2)


cs = CubicSpline(np.array(xs), np.array(ys))

# Генерируем много точек для плавной кривой
x_smooth = np.linspace(np.array(xs).min(), np.array(xs).max(), 100)
y_smooth = cs(x_smooth)


cs2 = CubicSpline(np.array(xs2), np.array(ys2))
# Генерируем много точек для плавной кривой
x_smooth2 = np.linspace(np.array(xs2).min(), np.array(xs2).max(), 100)
y_smooth2 = cs2(x_smooth2)

plt.scatter(ys,xs,label = "290 Om")
plt.plot(y_smooth,x_smooth)
plt.scatter(ys2,xs2, label = "600 Om")
plt.plot(ys2,xs2)

plt.plot([0.8,1.2],[3.1415/4, 3.1415/4])
plt.plot([0.8,1.2], [3/4 * 3.1415, 3/4 * 3.1415])

plt.xlabel("Отношение частоты к резонансной",fontsize = 20)
plt.ylabel("Разность фаз, пи",fontsize = 20)
plt.legend(fontsize = 20)
plt.grid()
plt.show()
