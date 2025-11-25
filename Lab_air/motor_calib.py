import matplotlib.pyplot as plt
import numpy as np

colors = ['r','g','b','y','black','pink','v','brown']

dot_atm_pressure = [0,1400]
dot_atm_sensor = [0,7.7]

plt.title("Калибровка моторного двигателя",fontsize = 50)
plt.scatter(dot_atm_pressure,dot_atm_sensor,color = 'purple',s=20,marker = 'D',label = "Измерения")
plt.plot(dot_atm_pressure,dot_atm_sensor,label ="график прямой y = 0,0055x")

ax = plt.gca()
ax.set_xlabel("Количество шагов", fontsize=40)    # +
ax.set_ylabel("Перемещение, см", fontsize=40)

print(7.7 / 1400)

plt.legend(fontsize = 40)
plt.minorticks_on()
plt.grid(which='major', color = '#444', linewidth = 1)
plt.grid(which='minor', color='#aaa', ls=':')
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.show()




