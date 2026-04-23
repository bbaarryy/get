import matplotlib.pyplot as plt
import math


def fun(arrx,arry,ch):
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

    hi = 0
    for i in range(len(arrx)):
        hi += (arry[i] - (a*arrx[i]+b))**2 / (0.03 * arry[i])**2
    if(ch):
        print(("Hi: ", hi**0.5, len(arrx)))
    return(a,b,hi**0.5)

xs = [0.01, 0.02, 0.03, 0.04, 0.05]
ys = [5.71, 8, 16.39, 20, 26.3]

ys2 = [7.75,13.89,25,32.26,43.48]


a,b,hi = fun(xs,ys,0)
k1 = a
print(a/1000)

plt.plot([0,0.05],[b,a*0.05+b],c = 'b')

plt.scatter(xs,ys2,c = 'g')
plt.grid()
plt.show()