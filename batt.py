import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

file = open('battery_stat.txt','r')

ch = 1
arr=[]
dates=[]
d = 0
for line in file:
    if(ch):
        dates.append(d)
        d+=1
    else:
        arr.append(int(line)/1000/71000)
    ch = ch+1
    ch = ch%2

print(len(arr))
plt.plot(dates, arr)
plt.show()