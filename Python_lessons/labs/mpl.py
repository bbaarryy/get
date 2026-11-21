import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np

file = open("./Python_lessons/labs/dead_moroz/002.dat")

q = 1
start =100
data = []

xs = []
ys = []

for line in file:
    if(q):
        start = int(line)
        q=0
    elif start != 0:
        start-=1
        curr = list(map(float, line.split(" ")))
        data.append(curr)
        xs.append(curr[0])
        ys.append(curr[1])
    else:
        break

#print(data)


plt.scatter(xs,ys)

plt.title("Number of points:" + str(len(xs)))

plt.gca().set_aspect('equal', adjustable='datalim')
plt.show()

