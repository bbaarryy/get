import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d

colors = ['r','g','b','y','black','pink','v','brown','violet','grey']

arr = [2.401754851645565,
2.939913873438772,
3.3773697870040533,
4.2018791688895405,
4.364931838908569,
4.942873877575612,
6.688218076425404,
7.787827726200365]
coord = [0,10,20,30,40,50,70,90]

plt.scatter(coord,arr,label='Измерения',color='r')

# Метод 'cubic' для более плавного сплайна
f_cubic = interp1d(coord, arr, kind='cubic')
x_new = []
for i in range(0,91):
    x_new.append(i)

y_cubic = f_cubic(x_new)
print(x_new)
plt.plot(x_new, y_cubic, label='Кубическая интерполяция',color = 'g')

plt.grid()
plt.title("Зависимость расхода от расстояния до трубки Пито",fontsize = 25)

ax = plt.gca()
ax.set_xlabel("Расстояние(мм)", fontsize=25)    # +
ax.set_ylabel("Расход(г\с)", fontsize=25)

plt.legend(fontsize = 25)
plt.minorticks_on()
plt.grid(which='major', color = '#444', linewidth = 1)
plt.grid(which='minor', color='#aaa', ls=':')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

plt.show()