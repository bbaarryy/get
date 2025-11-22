import matplotlib.pyplot as plt
import numpy as np

colors = ['r','g','b','y','black','pink','v','brown']

dot_atm_pressure = [0,1400]
dot_atm_sensor = [0,7.7]


plt.xticks(np.arange(0, 1500, 100))
plt.yticks(np.arange(0, 8, 0.5))
plt.title("Калибровка моторного двигателя",fontsize = 25)

plt.scatter(dot_atm_pressure,dot_atm_sensor,color = 'purple',s=20,marker = 'D',label = "Измерения")
plt.plot(dot_atm_pressure,dot_atm_sensor,label ="график прямой y = 0,0055x")

ax = plt.gca()
ax.set_xlabel("Количество шагов", fontsize=25)    # +
ax.set_ylabel("Перемещение, см", fontsize=25)

plt.legend(fontsize = 25)
plt.grid()
plt.show()
#print(arr00[0:10])



