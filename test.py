import matplotlib.pyplot as plt
import numpy as np

# Данные для графика
x = [0, 0.13, 0.213, 0.24, 0.278, 0.31, 0.346, 0.371, 0.4, 0.421, 0.445, 0.469, 0.491, 0.513, 0.533, 0.551, 0.569, 0.588, 0.606 ]
y = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180 ]

def deriv(x,y):
    xd = []
    yd = []
    for i in range(len(x)-1):
        xd.append(x[i])
        yd.append((y[i+1]-y[i]) / (x[i+1]-x[i]))
    return xd,yd
xd ,yd = deriv(x,y)
xdd,ydd = deriv(xd,yd)

# Создание графика
plt.figure(figsize=(10, 6))

# Экспериментальные точки
plt.plot(x, y, marker='o', linestyle='', color='blue', markersize=8, label='Экспериментальные точки')
plt.plot(xd, yd, marker='o', linestyle='', color='red', markersize=8, label='Экспериментальные точки')
plt.plot(xdd, ydd, marker='o', linestyle='', color='green', markersize=8, label='Экспериментальные точки')

# Настройки графика
plt.xlabel('t, c ', fontsize=12)
plt.ylabel('S, м', fontsize=12)

# Плотная сетка
plt.grid(True, alpha=0.8, which='both')
plt.minorticks_on()
plt.grid(True, alpha=0.4, which='minor')

# Легенда
plt.legend(fontsize=11, loc='upper left')

# Настройка осей
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Текстовое поле с информацией о наклоне

plt.tight_layout()
plt.show()

# Дополнительная информация
print(f"\nДополнительная информация:")
#print(f"Коэффициент детерминации R²: {model.score(x_array, y_array):.4f}")