import matplotlib.pyplot as plt

G = 6.67430*(10**(-11))/(10**9) #
M=1.98847*(10**30) #кг

xs = [147098291]
ys = [0]

vx = [0]
vy = [20] #

for t in range(0,365*40):
    dt = 1*60*60 #seconds

    current_ax = -(G * M) / ((xs[-1] ** 2 + ys[-1]**2) ** (1.5)) * xs[-1]
    vx.append(vx[-1] + current_ax*dt)
    xs.append(xs[-1] + vx[-1]*dt)

    current_ay = -(G * M) / ((xs[-1] ** 2 + ys[-1]**2) ** (1.5)) * ys[-1]
    vy.append(vy[-1] + current_ay*dt)
    ys.append(ys[-1] + vy[-1]*dt)

plt.scatter(xs,ys)
plt.scatter(0,0,c='y')
plt.grid()
plt.show()
    

