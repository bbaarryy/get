import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np

file = open("./Python_lessons/labs/frames.txt")

all_x = []
all_y = []

q = 1
for line in file:
    if(q):
        q=0
        curr_xs = list(map(float, line.split(" ")))
        all_x.append(np.array(curr_xs))
    else:
        q=1
        curr_ys = list(map(float, line.split(" ")))
        all_y.append(np.array(curr_ys))


# xmin = min(a.min() for a in all_x); xmax = max(a.max() for a in all_x)
# ymin = min(a.min() for a in all_y); ymax = max(a.max() for a in all_y)
# s  = max(xmax - xmin, ymax - ymin)
# cx = (xmin + xmax) / 2
# cy = (ymin + ymax) / 2
xlim = (-1,17)
ylim = (-8.5, 11.5)

fig, axes = plt.subplots(2, 3, figsize=(12, 8), sharex=True, sharey=True)

ind = 1
for ax, x, y in zip(axes.flat, all_x, all_y):
    ax.plot(x, y)
    ax.set_title("Frame " + str(ind))
    ind+=1
    ax.set_aspect('equal')      
    ax.grid(True)
    ax.tick_params(labelbottom=True, labelleft=True)

axes[0, 0].set_xlim(xlim)
axes[0, 0].set_ylim(ylim)

from matplotlib.ticker import MultipleLocator

ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.yaxis.set_major_locator(MultipleLocator(2.0))

ax.grid(True, which='major', linewidth=0.7, alpha=0.8)

plt.tight_layout()
plt.show()

