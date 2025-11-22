import matplotlib.pyplot as plt
import numpy as np

file_calib = open("./Lab_air/new_calib1_data.txt")
zero_level = 0

q = 0
for line in file_calib:
    zero_level += int(line[0:6])
    q+=1

zero_level /= q

def fun_plot(file00,s):
    arr00=[]
    coords = []

    for line in file00:
        curr = line
        num = ""
        x = ""
        for i in range(len(curr)):
            if curr[i] == ' ':
                num = line[0:i]
                if(int(num) > 1e6):
                    num = str(int(zero_level))
                x = line[i+1:-1]
        arr00.append(int(num) - zero_level)
        
        coords.append(int(x))
    plt.xticks(np.arange(min(coords), max(coords)+50, 50.0),fontsize = 15)
    
    plt.plot(coords,arr00,color = s)

colors = ['r','g','b','y','b','pink','v','brown']

for i in range(0,6,1):
    url = "./Lab_air/" + str(i) + "0data.txt"
    file00 = open(url)
    fun_plot(file00,colors[i])
    
plt.yticks(np.arange(-1800, 1e4, 600.0))
plt.grid()
plt.title("Зависимость давления(в условных единицах), от смещения",fontsize = 25)

ax = plt.gca()
ax.set_xlabel("Смещение(у.е.)", fontsize=25)    # +
ax.set_ylabel("Давление(у.е.)", fontsize=25)

plt.show()
#print(arr00[0:10])



