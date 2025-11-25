import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d

colors = ['r','g','b','y','black','pink','v','brown','violet','grey']

arr = [2.3734359112988224,
2.922128643862065,
3.402900882137556,
4.0951388345319994,
4.3414030435904785,
4.9288436302511425,
6.656674408109578,
7.819901398869738]
coord = [0,10,20,30,40,50,70,90]

plt.plot(coord,arr,label='Измерения',color='r')

# Метод 'cubic' для более плавного сплайна
f_cubic = interp1d(coord, arr, kind='cubic')
x_new = []
for i in range(0,91):
    x_new.append(i)

y_cubic = f_cubic(x_new)
print(x_new)
#plt.plot(x_new, y_cubic, label='Кубическая интерполяция',color = 'g')
#plt.plot()

plt.grid()
plt.title("Зависимость расхода от расстояния до трубки Пито",fontsize = 50)

ax = plt.gca()
ax.set_xlabel("Расстояние(мм)", fontsize=40)    # +
ax.set_ylabel("Расход(г\с)", fontsize=40)

plt.legend(fontsize = 40)
plt.minorticks_on()
plt.grid(which='major', color = '#444', linewidth = 1)
plt.grid(which='minor', color='#aaa', ls=':')
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)

plt.show()