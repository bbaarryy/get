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

ps =    [144,142,141,140,139,138,136,133]
ts =    [22.5, 27.3,32.3,37.3,42.3,47.2,52.0,57.0]

t_correct = [20,25,30,35,40,45,50,55]
sigma_correct = [72.75,71.99,71.20,70.41,69.60,68.78,67.94, 67.1]

for i in range(len(ps)):
    ps[i] = 0.2 * 9.8067 * (ps[i]-38) * 0.9975 
    sigma_correct[i] /= 1000

ps[-1] = 0.2 * 9.8067 * 134 * 0.9975 - (985.7 * 9.8 * 7.78 / 1000)

r = 0.0007
sigmas = []
for i in range(len(ps)):
    sigmas.append(ps[i] * r / 2)

a,b,hi = fun(ts, sigmas,1)

print(sigmas[0])

plt.plot([20,60],[20*a + b,a*60+b],color = 'b', label = "Ожидаемые данные")
print( (20*a + b - (a*60+b)) / (60-20))
plt.ylabel(r"$Коэффициент_ пов. натяжения , Н/м$",fontsize=20)
plt.xlabel(r"$Температура, С$",fontsize=20)
plt.plot(ts,sigmas,color = 'r', label = "Полученные данные")
plt.plot(t_correct,sigma_correct,color = 'g', label = "Табличные данные")
plt.legend()
plt.grid()
plt.show()