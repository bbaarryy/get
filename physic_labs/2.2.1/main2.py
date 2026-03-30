import matplotlib.pyplot as plt
import math

plt.rcParams.update({'font.size': 15})

DS = [20.8, 10.7,7.5, 5.3]
PS = [1/40.9, 1/78, 1/121.9, 1/159.7]

yerr = []
for i in range(4):
    yerr.append(DS[i] * 0.023)


def fun(arrx,arry,yerr):
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

    b = (xy_av - x_av * y_av)/(x_2_av - x_av ** 2)
    a = y_av - b * x_av
   
    sigma_b = 1/(len(x))**0.5 * ( (y_2_av - y_av**2) / (x_2_av - x_av ** 2) - b**2) ** 0.5
    sigma_a = sigma_b * (x_2_av - x_av**2)**0.5

    k = (xy_av)/(x_2_av)
    print("KKK:", k)

    print("sigma_a: ", sigma_a)
    
    hi = 0
    for i in range(len(arrx)):
        hi += (arry[i] - (b*arrx[i]+a))**2 / (yerr[i])**2
    
    print((hi**0.5, len(arrx)))
    return(b,a)

a,b = fun(PS,DS,yerr)
#print(a * (1/760) + b)


#plt.plot([0.00,0.025],[a*0.00+b,a*0.025 + b],label = "Аппроксимация МНК")

plt.plot([0.00,0.025],[a*0.00,852.4*0.025],label = "Аппроксимация МНК")
print(1/760 * 852.4)
plt.scatter([1/760],[0.85],c='green', label = "Табличные значения")
plt.scatter(PS,DS, color = 'red')
plt.errorbar(PS,DS, yerr=yerr, ecolor='red',label = "Наши данные")
plt.ylabel(r"D, см^2/c",fontsize=20)
plt.xlabel("1/P, 1/торр",fontsize=20)
plt.legend()
plt.grid()
plt.show()