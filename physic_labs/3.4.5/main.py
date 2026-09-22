import matplotlib.pyplot as plt
import math
from copy import copy, deepcopy
import numpy as np

data1 = [115, 100, 80, 50, 20, 40, 130, 65]
#approx=[[3,2],[1.8,1.8],[1.2,2.4],[1.2,1], [1,1], [1,0.8], [3.4,2]]

coords1 = [[3,1.8], [2.7,1.7],[2.2,1.5], [1.2,1], [0.8,0.36], [1, 0.8], [3.4,2], [1.6, 1.2]]


data2 = [210,190,150,130,110,95,85,70,50]

coords2 = [[1,2], [0.7,1],[0.5,1.8],[0.4,1.5],[0.4,1.1],[0.3,0.7],[0.3,0.5],[0.26,0.22],[0.22,0.06]]


data3 = [450, 440, 430, 400, 370, 340, 310, 270, 240, 200, 156, 120, 50]

coords3 = [[4.4,2.8],[4.2,2.7],[4,2.6],[3.6,2.5],[3.4,2.4],[3,2.3],[2.6,2.1],[2.2,2],[1.8,1.8],[1.4,1.4],[1,1.1],[0.8,0.8],[0.44,0.28]]

lim1 = 145
coord_lim1 = [[3.4, 2]]
Ch1 = 20


maxx =-1
xs = [0]
ys = [0]
for i in range(len(coords2)):
    xs.append(coords2[i][0])
    ys.append(coords2[i][1])
    
    # xs.append(-coords1[i][0])
    # ys.append(-coords1[i][1])



xs = sorted(xs)
ys = sorted(ys)

for i in range(1,len(xs)):
    if xs[i] - xs[i-1] !=0 :
        maxx=max(maxx, abs( (ys[i] - ys[i-1]) / (xs[i] - xs[i-1])))

print(maxx)
plt.scatter(xs,ys)

coeffs = np.polyfit(xs, ys, 4)          # [a, b, c, d]
poly = np.poly1d(coeffs)              # удобная функция

# гладкая кривая для отрисовки
x_smooth = np.linspace(min(xs), max(xs), 200)
y_smooth = poly(x_smooth)

#plt.plot(x_smooth, y_smooth)

plt.ylabel(r"Магнитная индукция, Тл",fontsize=20)
plt.xlabel(r"Напряженность, Н/Кл",fontsize=20)
plt.grid()
plt.show()