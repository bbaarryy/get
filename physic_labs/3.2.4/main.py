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


plt.errorbar(Ts_exp, Ts_the, yerr = yerr, xerr = 0.005 * 10 ** -3, color = 'g')
plt.plot([0.00008,0.0002],[0.00008,0.0002])
# plt.errorbar(xs,Ts_the,yerr=0.002 * 10**(-3),color='red')
# plt.plot(xs, Ts_exp, color = 'red', label = 'Экспериментально')
# plt.errorbar(xs,Ts_exp,yerr=0.002 * 10**(-3),color='red')
# plt.errorbar(Is,ks,fmt='o')
# a,b,k,sigma_k = fun(Is,ks)

# plt.plot([0,1],[0,k],label = 'Прямая зависимость Y=(' + str(k)[0:6] + "+-" + "0.0004"  + ')x')



plt.xlabel(r"Эксперимент, c",fontsize=20)
plt.ylabel(r"Теория, c",fontsize=20)

#a,b,k,sigma_k = fun(x, I)

#plt.plot([5,25],[5 * a + b, 25 * a + b])

#print(a,b)


### Теперь декремент затухания
Qs = [290,600,900,1200,1400]
a=[[656,500,368,280,204],
   [544,316,180],
   [448,200,92],
   [376,132,44],
   [344,108,36]]

for i in range(len(Qs)):
    D1 = math.log(a[i][0] / a[i][1])
    D2 = math.log(a[i][0] / a[i][2])
    D3 = 0.5 * math.log(a[i][0] / a[i][2])

    print(D1, D2, D3)
###

plt.legend(fontsize=20)
plt.grid()
plt.show()