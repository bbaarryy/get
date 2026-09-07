import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})

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

    sigma_b = 1/((len(x))**0.5) * ( (y_2_av - y_av**2) / (x_2_av - x_av ** 2) - b**2  ) ** 0.5
    sigma_a = sigma_b * (x_2_av - x_av**2)**0.5

    hi = 0
    for i in range(len(arrx)):
        hi += (arry[i] - (a*arrx[i]+b))**2 / (0.03)**2
    if(ch):
        print("Hi: ", hi**0.5, len(arrx))
        print("K: ", a)
        print(sigma_a)

    return(a,b,hi**0.5)
    
dP1 = [4, 3.5, 3, 2.5, 2, 1.5]
dU1 = [0.160, 0.135,0.113,0.090,0.067,0.05]
for i in range(0,len(dU1)):
    dU1[i] = dU1[i]/0.0407

dP2 = [4, 3.5, 3, 2.5, 2, 1.5]
dU2 = [0.146, 0.122,0.100,0.080,0.061,0.042]
for i in range(0,len(dU2)):
    dU2[i] = dU2[i]/0.0416

dP3 = [4, 3.6, 3, 2.5, 2, 1.5]
dU3 = [0.088, 0.078,0.060,0.043,0.030,0.019]
for i in range(0,len(dU3)):
    dU3[i] = dU3[i]/0.0433

plt.errorbar(dP3,dU3,xerr=[0.1,0.1,0.1,0.1,0.1,0.1], capsize=3,fmt="o", ecolor = "black")
a,b,hi = fun(dP1,dU1,1)
a,b,hi = fun(dP2,dU2,1)
a,b,hi = fun(dP3,dU3,1)

plt.plot([1,4],[a+b,4*a+b],c = 'r')

plt.xlabel(r"Разница давлений, Па",fontsize=20)
plt.ylabel("Разница температур, К",fontsize=20)
plt.grid()
plt.show()