import matplotlib.pyplot as plt
import math

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

    sigma_a = 1/(len(arrx)**(0.5))*( (y_2_av - y_av ** 2)/(x_2_av - x_av**2) - a*2 ) ** 0.5
    sigma_b = sigma_a * (x_2_av - x_av**2)**0.5
    
    k = xy_av / x_2_av
    sigma_k = 1/(7**0.5)*(y_2_av / x_2_av - k ** 2)**0.5
    print(k,sigma_k)
    return(a,b,sigma_a,sigma_b)

Is = [1.49, 1.25, 1.15, 1.00, 0.8, 0.5, 0.25]
B = [6, 5.4, 5.1, 4.5, 3.7, 2.35, 1.3]

a,b,sa,sb = fun(Is, B)
xerrs = [0.05]*7
yerrs = [0.1]*7

plt.errorbar(Is,B, color='red',xerr=0.05,yerr=0.1,fmt='o',label='Полученные данные')
plt.plot([0,1.5],[0,1.5*4.3238],label="y = 4.3238x")
#plt.errorbar(xerrs,yerrs)

print(sa,sb)

plt.xlabel(r"Сила тока через германий, А",fontsize=20)
plt.ylabel(r"Индукция магнитного поля катушки, мВб",fontsize=20)
#plt.plot(ts,sigmas,color = 'r', label = "Полученные данные")
#plt.plot(t_correct,sigma_correct,color = 'g', label = "Табличные данные")



plt.legend(fontsize=20)
plt.grid()
plt.show()