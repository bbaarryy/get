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

Cs = [0,0.002,0.004,0.006,0.008,0.009]
Ts_exp = [0.088,0.112,0.142,0.172,0.190,0.202]

C_0 = 1.96 * 10**(-9)

Ts_the = []
for i in range(len(Cs)):
    Ts_the.append(2 * 3.1415926535 * ( (C_0 + Cs[i] * 10**(-6) ) * (100 * 10**(-3) ))**0.5)

xs = []
yerr = []
for i in range(len(Cs)):
    xs.append(i+1)
    Ts_exp[i] *= 10**(-3)
    yerr.append(3.5 / 100 * Ts_exp[i])


### Теперь декремент затухания
Rs = [18,24,27,30,33,36,42,48,54,60]

xs=[[22.9, 3.2, 0.6],
    [23,   5.1, 1.2],
    [20.5, 5.2, 1.4],
    [18.5, 5.4, 1.7],
    [25.2, 8.1, 2.6],
    [23.1, 8.1, 2.9],
    [19.9, 7.9, 3.2],
    [17.5, 7.6, 3.4],
    [22.1, 10.3,4.9],
    [19.9, 9.8, 5.1]
    ]


xss=[]
yss=[]
Rcrs= []

error = 0

for i in range(len(Rs)):
    t1 = math.log(xs[i][0]/xs[i][1])
    t2 = math.log(xs[i][1]/xs[i][2])
    print("R:", Rs[i] * 1000 , "Om,", " t:", str((t1 + t2) / 2)[0:4])

    error += abs(t1-t2)

    t = (t1+t2)/2

    Rcr = (Rs[i]*1000 + 610) / (( ( (2 * 3.1415) / t ) ** 2 + 1 )**0.5) - 610
    print(Rcr)
    Rcrs.append(Rcr)
    xss.append(Rs[i])
    yss.append((t1+t2)/2)

error /= len(Rs)
print("error" , error)

print(np.array(Rcrs).sum() / len(Rcrs), "bebe")
plt.scatter(xss,yss)
#plt.plot(xss,Rcrs)

plt.xlabel("Сопротивление R, Ком",fontsize=20)
plt.ylabel("Декремент затухания",fontsize=20)



plt.grid()

plt.grid(True, alpha=0.8, which='both')
plt.minorticks_on()
plt.grid(True, alpha=0.4, which='minor')
plt.show()
###

# plt.legend(fontsize=20)
# plt.grid()
# plt.show()