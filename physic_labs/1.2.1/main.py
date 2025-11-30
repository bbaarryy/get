import matplotlib.pyplot as plt

ms = [0.506,0.512,0.504,0.511,0.513,0.500,0.510,0.509,0.510,0.500]
M = 2905

L = 2.17

xs = [8.125, 8.25, 8, 8.31, 8.3, 0.047, 0.048, 0.0475,0.047,0.0465]

vs = []
coords = []
av_1 = 0
for i in range(5):
    curr_u = M / ms[i] * (9.8/2.17)**0.5 * xs[i]*2 / 1000
    print(curr_u)
    vs.append(curr_u)
    av_1 += curr_u
    coords.append(i+1)



# T_out = 5.07
# T_1 = 6.7

# sKI = (4 * 3.141592 * 0.7306 * (0.617)**2 * 6.7)/(6.5**2 - 5.07**2)
# print(sKI)

# for i in range(5):
#     curr_u = xs[i+5] * sKI / (ms[i+5]/1000 * 2*0.2 * 1.652)
#     print(curr_u)
#     vs.append(curr_u)
#     av_1 += curr_u
#     coords.append(i+1+5)

av_1 /= 5
avm = [av_1] * 5

plt.plot(coords,avm,c = 'r',label = 'Среднее значение')
plt.plot(coords,vs, label = 'скорость в эксперименте')
plt.grid()
plt.title('График скорости пули')
plt.xlabel("Номер эскперимента")
plt.ylabel("Скорость, м\с")
plt.legend()
plt.show()

