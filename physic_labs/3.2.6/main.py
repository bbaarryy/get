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

I = []
x = [24.8, 22.5,20.9,18.5,16.7,15.2,12.3,11,9.9,8.3,6.3,4.8]

magasine = [1400,1600,1800,2100,2400,2700,3500,4000,4500,5500,8500,10000]
for i in range(len(magasine)):
    I.append( 1/2000 * 1.2  / (magasine[i] + 610))


# plt.errorbar(Is,ks,fmt='o')
# a,b,k,sigma_k = fun(Is,ks)

# plt.plot([0,1],[0,k],label = 'Прямая зависимость Y=(' + str(k)[0:6] + "+-" + "0.0004"  + ')x')

plt.plot(x, I)

plt.xlabel(r"Отклонение по шкале, см",fontsize=20)
plt.ylabel(r"Ток через гальванометр, А",fontsize=20)

a,b,k,sigma_k = fun(x, I)

plt.plot([5,25],[5 * a + b, 25 * a + b])

print(a,b)

plt.legend(fontsize=20)
plt.grid()
plt.show()