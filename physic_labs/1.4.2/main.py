import matplotlib.pyplot as plt

qs = [60,    60,   40,   40,   20,20,   30,   30,   90,    90]
ts = [84.08, 83.47,55.63,56.16,28,27.81,41.95,41.70,125.12,126.61 ]

qs = [20,20,30,30,40,40,90,90]
ts = [28,27.81,41.95,41.70,55.63,56.16,125.12,126.61]

l1 = 36.92/100
l2 = 10.66/100

xs = [1,2,3,4]
gs = []
gsu = []
gsd = []
for i in range(0,8,2):
    g = 4 * ((3.1415926535)**2) * (l1**2 - l2**2) / (l1 * (ts[i]/qs[i])**2 - l2*(ts[i+1]/qs[i+1])**2)
    p = g * ((0.01/47.58)**2 + ( ( (l1**2+l2**2)**0.5 / (l1-l2) * (0.01/ts[i]) ) / ((l1 * ts[i]**2 - l2 * ts[i+1]**2)/ (l1-l2)))**0.5)
    gs.append(g)
    gsu.append(g+p)
    gsd.append(g-p)
    print(qs[i] , g, p)

plt.plot(xs,gs,c = 'b')
plt.plot(xs,gsu,c='r')
plt.plot(xs,gsd,c='r')

plt.grid()
plt.show()