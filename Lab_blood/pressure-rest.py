import matplotlib.pyplot as plt
import numpy as np


def Pressure(x):
    P = 0.417329 * x - 15.098481
    return P


input_file = 'data_1.txt'  # Имя входного файла


# Считываем данные из файла
data = np.loadtxt(input_file, delimiter=' ')


# Разделяем данные на два массива: значения и время
acp = data[:, 0]
values = []


for i in acp:
    values.append(Pressure(i))


time = data[:, 1]

# Вычисляем и выводим среднее значение первого столбца
average_acp = np.mean(acp)
print(f"Среднее значение первого столбца: {average_acp}")


# Строим график
plt.figure(figsize=(10, 6))
plt.plot(time, values, linestyle='-', color='b')
plt.plot(7.576132535934448, Pressure(343), 'o', color = 'black')
plt.plot(53.914387464523315, Pressure(193), 'o', color = 'black')
plt.annotate('Систола',
             xy=(7.576132535934448, Pressure(343)),
             xytext=(30, 30),
             textcoords='offset points', 
             arrowprops=dict(facecolor='black', 
                           shrink=0.05, 
                           width=2,
                           headwidth=8),
             fontsize=16,
             color='black',
)

plt.annotate('Диастола',
             xy=(53.914387464523315, Pressure(193)),
             xytext=(30, 30),
             textcoords='offset points', 
             arrowprops=dict(facecolor='black', 
                           shrink=0.05, 
                           width=2,
                           headwidth=8),
             fontsize=16,
             color='black',
)
plt.title('Артериальное давление до нагрузки', fontsize = 45)
plt.xlabel('Время (секунды)', fontsize = 25)
plt.ylabel('мм рт. ст.', fontsize = 25)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.grid(True)
plt.show()
