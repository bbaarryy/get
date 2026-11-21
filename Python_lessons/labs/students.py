import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np

file = open("./Python_lessons/labs/students.csv")

plt.figure()
plt.subplot(2, 1, 1)   

preps = []
groups = []
marks = []

dicts = []
for i in range(7):
    dicts.append({2:0,
                  3:0,
                  4:0,
                  5:0,
                  6:0,
                  7:0,
                  8:0,
                  9:0,
                  10:0})
for line in file:
    prep, group, mark = map(str, line.split(";"))
    dicts[int(prep[-1])-1][int(mark)]+=1
    groups.append(int(group))
    marks.append(int(mark))

# print(preps)
# print(groups)
# print(marks)
colors = ['black', 'black', 'brown', 'red','orange','yellow','green','blue', 'pink']
layers = ['2','3','4','5','6','7','8','9','10']
left = 0
labels = [3,4,5,6,7,8,9,10]
for prep in range(7):
    bottom = 0
    left += 1
    for v, c in zip(dicts[prep], colors):
        #print(v)
        plt.bar(left, dicts[prep][v], bottom=bottom, color=c)
        bottom += dicts[prep][v]

names = []
for i in range(7):
    names.append("Prep " + str(i+1))

from matplotlib.patches import Patch

handles = [Patch(color=c, label=l) for c, l in zip(colors[1::], layers[1::])]
plt.legend(handles=handles, title='Слои',loc='upper right')

plt.xticks(range(1,8), names) 
plt.title("Marks per prep")
plt.grid()





plt.subplot(2, 1, 2)   

dicts = []
for i in range(6):
    dicts.append({2:0,
                  3:0,
                  4:0,
                  5:0,
                  6:0,
                  7:0,
                  8:0,
                  9:0,
                  10:0})

file = open("./Python_lessons/labs/students.csv")
for line in file:
    prep, group, mark = map(str, line.split(";"))
    dicts[int(group[-1])-1][int(mark)]+=1
    groups.append(int(group))
    marks.append(int(mark))

print(dicts)

# print(preps)
# print(groups)
# print(marks)
colors = ['black', 'black', 'brown', 'red','orange','yellow','green','blue', 'pink']
layers = ['2','3','4','5','6','7','8','9','10']
left = 0
labels = [3,4,5,6,7,8,9,10]
for group in range(6):
    bottom = 0
    left += 1
    for v, c in zip(dicts[group], colors):
        #print(v)
        plt.bar(left, dicts[group][v], bottom=bottom, color=c)
        bottom += dicts[group][v]

names = []
for i in range(6):
    names.append("group 75" + str(i+1))

from matplotlib.patches import Patch

handles = [Patch(color=c, label=l) for c, l in zip(colors[1::], layers[1::])]
plt.legend(handles=handles, title='Слои',loc='upper right')

plt.xticks(range(1,7), names) 
plt.title("Marks per group")
plt.grid()


plt.tight_layout()
plt.show()
