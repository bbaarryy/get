import matplotlib.pyplot as plt
import numpy as np

file_calib = open("./Lab_air/new_calib0_data.txt")
zero_level = 0

calib_arr = []

for line in file_calib:
    calib_arr.append(line[0:6])

#автоцентрирование
delta = 0

file_00 = open("./Lab_air/00data.txt",'r')
start = -1
end=-1
last = 216227
for line in file_00:
    curr = int(line[0:6])
    if(curr > 5000):
        if(start == -1):
            start = last
        elif end == -1:
            end = int(line[6::])
    last=curr

print(start,end)
delta = 0.5
print(delta)

def fun_plot(file00,s,qq,start_int,end_int):
    arr00=[]
    coords = []
    index = 0
    curr_calib = -1
    for line in file00:
        curr = line
        num = ""
        x = ""
        v = 0
        next_v= -2
        for i in range(len(curr)):
            if curr[i] == ' ':
                num = line[0:i]
                if(curr_calib == -1):
                    curr_calib = int(num)
                if(int(num) > 1e6):
                    num = str(int(curr_calib))
                v = (((max(0,2*(int(num) - int(curr_calib))/23.6) / 1.2))**0.5)
                if(v < 1):
                    next_v+=1
                if(next_v == 0):
                    v=0
                x = line[i+1:-1]
                if(abs(int(x)) > 270):
                    v = 0
        if(start_int < int(x) * 0.0055 * 10 < end_int):
            arr00.append(v)
        else:
            arr00.append(0)
        coords.append(int(x) * 0.0055 * 10)
        index+=1
    curr_Q = 0
    for i in range(len(coords)):
            coords[i] += delta
    for i in range(1,len(arr00)):
        if(start_int < coords[i] < end_int):
            curr_Q += abs(0.5*(abs(coords[i]) * arr00[i] + abs(coords[i-1]) * arr00[i-1]) * (coords[i] - coords[i-1]))  
    print(str((curr_Q * 2 * 3.1415/1000)) + ',')
    plt.plot(coords,arr00,color = s,label = 'Расстояние - ' + qq + "cm",lw = 2)

colors = ['r','g','b','y','black','pink','v','brown','violet','grey']

start_int_arr = [-6, -6,-10,-9, -10, -11,0, -14, 0,-16]
end_int_arr =   [ 6, 8 ,10, 8, 10 , 11 ,0, 14 , 0, 16]
for i in range(0,10,1):
    if(i!=6 and i!= 8):
        url = "./Lab_air/" + str(i) + "0data.txt"
        file00 = open(url)
        fun_plot(file00,colors[i],str(i*10),start_int_arr[i],end_int_arr[i])

plt.grid()
plt.title("Зависимость скорости струи от смещения" + '\n',fontsize = 50)

ax = plt.gca()
ax.set_xlabel("Смещение(mm)", fontsize=40)    # +
ax.set_ylabel("Скорость(м\с)", fontsize=40)

plt.legend(fontsize = 40)
plt.minorticks_on()
plt.grid(which='major', color = '#444', linewidth = 1)
plt.grid(which='minor', color='#aaa', ls=':')
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)

plt.show()
#print(arr00[0:10])



