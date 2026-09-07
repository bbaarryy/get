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

    sigma_a = 1/(7**(0.5))*(abs( (y_2_av - y_av ** 2)/(x_2_av - x_av**2) - a*2 )) ** 0.5
    sigma_b = sigma_a * (x_2_av - x_av**2)**0.5

    return(a,b,k,sigma_a,sigma_b)

Germ1 = 0.3
U01 = 0.097
I1 = [0.25, 0.5, 0.75, 0.8, 1.00, 1.15, 1.25, 1.5]
U1 = [0.9, 1.770, 2.5, 2.730, 3.15, 3.6, 3.8, 4.19]

Germ2 = 0.4
U02 = 0.125
I2 = [0.25,0.5,0.75,1,1.25,1.5]
U2 = [1.3,2.365,3.420,4.330,5.145,5.79]

Germ3 = 0.5
U03 = 0.155
I3 = [0.25,0.5,0.75,1,1.25,1.5]
U3 = [1.53, 2.99, 4.255, 5.5, 6.42, 7.13]

Germ4 = 0.6
U04 = 0.190
I4 = [0.25,0.5,0.75,1,1.25,1.5]
U4 = [1.87, 3.57, 5.09, 6.47, 7.67, 8.5]

Germ5 = 0.7
U05 = 0.220
I5 = [0.25,0.5,0.75,1,1.25,1.5]
U5 = [2.17, 4.14, 5.9, 7.53, 8.94, 10]

Germ6 = 1
U06 = 0.310
I6 = [0.25,0.5,0.75,1,1.25,1.5]
U6 = [3.13, 5.9, 8.52, 10.8, 12.82, 14.13]

total_I = [I1, I2, I3, I4, I5, I6]
total_U = [U1, U2, U3, U4, U5, U6]

Germs = [Germ1, Germ2, Germ3, Germ4, Germ5, Germ6]
U0s = [U01, U02, U03, U04, U05, U06]

total_B = deepcopy(total_I)


errors_B = deepcopy(total_I)

for i in range(len(total_B)):
    for j in range(len(total_B[i])):
        errors_B[i][j] = errors_B[i][j]*0.1
        #total_B[i][j] = total_B[i][j]*3.9133121468926535 + 0.44975282485875834
        total_B[i][j] = total_B[i][j]*4.3238
        total_U[i][j] -= U0s[i]
    
colors = ['r','g','b','purple','black','brown','yellow']
print(errors_B[0])
for i in range(6):
    a,b,k,sigma_a,sigma_b = fun(total_B[i],total_U[i])
    #sigma_a = format(sigma_a, '.8f')
    plt.errorbar(total_B[i], total_U[i], yerr = 0.1, xerr = errors_B[i], fmt='o',label = str(Germs[i]) + 'A; k = ' + str(a)[0:5] + '+-' + str(sigma_a)[0:5],color = colors[i] )   #U(B)
    plt.plot([0,7],[b,a*7+b],color = colors[i]) 
    #plt.plot(total_B[i], total_U[i],label = str(Germs[i]) + 'A' )   #U(B)

#plt.errorbar(Is,B, color='red',xerr=0.05,yerr=0.1,fmt='o',label='')

#plt.plot([0,1.5],[b,a*1.5 + b],label="3.9x + 0.45")
#plt.errorbar(xerrs,yerrs)
#print(a,b)

plt.ylabel(r"ЭДС Холла, mV",fontsize=20)
plt.xlabel(r"Индукция магнитного поля катушки, мВб",fontsize=20)

plt.legend(fontsize=20)
plt.grid()
plt.show()