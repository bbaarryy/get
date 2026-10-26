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

    sigma_k = 1/(len(x)**0.5)*(y_2_av / x_2_av - k ** 2)**0.5

    return(a,b,k,sigma_k)

ch=1
if(ch==1):
    ### Теперь декремент затухания
    Qs = [290,600,900,1200,1400]
    a=[[656,500,368,280,204],
    [544,316,180],
    [448,200,92],
    [376,132,44],
    [344,108,36]]

    xSpiral = [[3.8,2.9,2.2],
               [3.6,2.1,1.2],
               [3.4,1.6,0.7],
               [3.2,1.1,0.4],
               [3.1,1,0.3]]


    
    ys = []
    xs = []
    yerr= []

    xSs = []
    ySs = []

    for i in range(len(Qs)):
        D1 = math.log(a[i][0] / a[i][1])
        D2 = math.log(a[i][1] / a[i][2])
        D3 = 0.5 * math.log(a[i][0] / a[i][2])

        DS1 = math.log(xSpiral[i][0] / xSpiral[i][1])
        DS2 = math.log(xSpiral[i][1] / xSpiral[i][2])
        DS3 = 0.5 * math.log(xSpiral[i][0] / xSpiral[i][2])

        print("Q - ", 3.1415926535 / ( (DS1 + DS2 + DS3)/3 ) )
        print("Q_th - ", 4.1 / Qs[i] * 1000)
        yerr.append((1/(D1) - 1/((D1+D2+D3)/3)) ** 2)
        #print(D1, D2, D3)
        ys.append( 1 / ((D1 + D2 + D3)/3)**2 )
        xs.append(1/ (Qs[i]) ** 2)

        


    a,b,k,sigma_k = fun(xs,ys)
    #plt.plot([0,1.2 * 10**-5], [b,a*1.2 * 10**-5 + b])
    #print(a,b)

    #print(sigma_k)

    #print((ys[1] - ys[0]) / (xs[1] - xs[0]))

    # plt.scatter(xs,ys)
    # #plt.errorbar(xs,ys,xerr = 0.000001,yerr = yerr)
    # plt.xlabel("1/R^2",fontsize = 20)
    # plt.ylabel("Обратный декремент",fontsize=20)
    # plt.legend(fontsize=20)
    # plt.grid()
    # plt.show()

    ###
