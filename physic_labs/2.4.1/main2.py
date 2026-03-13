import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
import matplotlib.ticker as ticker
plt.rcParams.update({'font.size': 15})

from numpy import sqrt, sin, cos, pi

ts = [22.00,23.00,24.00,25.00,26.00,27.00,28.00,29.00,30.00,31.00,32.00,33.00,34.00,35.00,36.00,37.00,38.00,39.00,40.00]
ps = [16.35,16.84,17.26,18.49,20.47,22.03,23.64,25.23,27.04,28.95,31.03,32.88,35.02,37.06,39.48,41.93,44.65,47.22,49.92]


# ts = [40.00,38.00,36.00,34.00,32.00,30.00,28.00,26.00,24.00,22.00,20.00]
# ps = [49.92,46.21,41.75,36.99,32.72,29.35,25.78,22.74,19.80,16.55,15.44]
n = len(ts)

def show_line(k,b):
    xs = ts
    ys = []

    for i in range(n):
        ys.append(xs[i] * k + b)
    plt.plot(xs,ys)

xx = 6
abs_ans = 0
qs = 0
# for i in range(2,n-1):
#     qs+=1
#     curr_k1 = (ps[i+1] - ps[i])/(ts[i+1] - ts[i])
#     curr_k2 = (ps[i] - ps[i-1])/(ts[i] - ts[i-1])
#     curr_k = (curr_k1 + curr_k2)/2
#     if(i == xx):
#         show_line(curr_k,-(ts[i] * curr_k - ps[i]))
#     #break
#     curr_L = 8.31 * (ts[i] + 273.15)**2 / (ps[i] ) * curr_k 
#     print(curr_L)
#     abs_ans += curr_L

for i in range(n):
    ps[i] = math.log(ps[i]*133.3)
    ts[i] = 1 / (ts[i] + 273.15)

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

    b = (xy_av - x_av * y_av)/(x_2_av - x_av ** 2)
    a = y_av - b * x_av

    hi = 0
    for i in range(len(arrx)):
        hi += (arry[i] - (b*arrx[i]+a))**2 / (0.01)**2
    if(ch):
        print((hi**0.5, len(arrx)))
    return(a,b,hi**0.5)



a,b,hi = fun(ts,ps,1)
show_line(b,a)

for i in range(1,n-1):
    
    qs+=1
    curr_k1 = (ps[i+1] - ps[i]) /(ts[i+1] - ts[i])
    curr_k2 = (ps[i] - ps[i-1]) /(ts[i] - ts[i-1])
    curr_k = (curr_k1 + curr_k2)/2
    
    if(i == xx):
        show_line(curr_k,ts[i] * curr_k - ps[i])
    curr_L = -8.31 * curr_k
    abs_ans += curr_L
    print(curr_L)



print()
print(abs_ans / qs)

plt.grid()
plt.scatter(ts,ps,c='r')
ax = plt.gca() 
formatter = ticker.FormatStrFormatter('%.3f')
ax.xaxis.set_major_formatter(formatter)
plt.ylabel(r"$Давление, мм.рт.ст$",fontsize=20)
plt.xlabel(r"$Температура, С$",fontsize=20)
plt.show()