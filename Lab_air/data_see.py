import matplotlib.pyplot as plt
import numpy as np

file_calib = open("./Lab_air/new_calib0_data.txt")
zero_level = 0

calib_arr = []

for line in file_calib:
    calib_arr.append(line[0:6])

def fun_plot(file00,s,qq):
    arr00=[]
    coords = []

    index = 0
    for line in file00:
        curr = line
        num = ""
        x = ""
        for i in range(len(curr)):
            if curr[i] == ' ':
                num = line[0:i]
                if(int(num) > 1e6):
                    num = str(int(calib_arr[index]))
                x = line[i+1:-1]
        arr00.append((int(num) - int(calib_arr[index]))/23.6)
        coords.append(int(x) * 0.0055 + 0.05)
        index+=1
    
    
    
    plt.plot(coords,arr00,color = s,label = 'Расстояние - ' + qq + "cm",lw = 2)

colors = ['r','g','b','y','b','pink','v','brown','violet','grey']

for i in range(0,10,1):
    if(i!=6 and i!= 8):
        url = "./Lab_air/" + str(i) + "0data.txt"
        file00 = open(url)
        fun_plot(file00,colors[i],str(i*10))

plt.grid()
plt.title("Зависимость давления(в условных единицах), от смещения",fontsize = 50)

ax = plt.gca()
ax.set_xlabel("Смещение(см)", fontsize=40)    # +
ax.set_ylabel("Увеличение давления(Па)", fontsize=40)

plt.minorticks_on()
plt.grid(which='major', color = '#444', linewidth = 1)
plt.grid(which='minor', color='#aaa', ls=':')
plt.legend(fontsize = 40)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.show()
#print(arr00[0:10])



