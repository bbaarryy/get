import matplotlib.pyplot as plt
import numpy as np

file_calib = open("./Lab_air/new_calib0_data.txt")
file_plus = open("./Lab_air/new_calib1_data.txt")

def average(file_calib):
    zero_level = 0
    q =0
    for line in file_calib:
        zero_level += int(line[0:6])
        q+=1
    zero_level /= q
    return zero_level

zero_level = average(file_calib)
plus_level = average(file_plus)

colors = ['r','g','b','y','black','pink','v','brown']

dot_atm_pressure = [0,91]
dot_atm_sensor = [zero_level, plus_level]

arr_yt = []
for i in range (215000-200, 217000+600, 200):
    arr_yt.append(str(i))

plt.yticks(arr_yt,fontsize = 25)
plt.xticks(np.arange(-10, 100, 5),fontsize = 25,rotation=45)
plt.title("Калибровка датчика давления",fontsize = 25)

plt.scatter(dot_atm_pressure,dot_atm_sensor,color = 'purple',s=20,marker = 'D',label = "Измерения")
plt.plot(dot_atm_pressure,dot_atm_sensor,label ="график прямой y = 23.6x + 214876")

ax = plt.gca()
ax.set_xlabel("Давление(Па)", fontsize=25)    # +
ax.set_ylabel("АЦП(у.е.)", fontsize=25)

plt.legend(fontsize = 25)
plt.grid()
plt.show()
#print(arr00[0:10])



