import matplotlib.pyplot as plt
import numpy as np

# Данные для калибровки
pressure_mmHg = np.array([40, 80, 120, 160])  # мм рт ст
units = np.array([129.75489457831324, 232.16537369914855, 322.22598440175005, 419.0453154875717])  # у е

# Линейная аппроксимация (y = k*x + b), где x - условные единицы, y - давление
coefficients = np.polyfit(units, pressure_mmHg, 1)
k = coefficients[0]
b = coefficients[1]

print(f"Калибровочная формула: P = {k:.6f} * x + {b:.6f}")
print(f"где x - условные единицы, P - давление (мм рт ст)")

# Создаем линию аппроксимации
units_line = np.linspace(100, 450, 100)
pressure_line = k * units_line + b

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(units, pressure_mmHg, 'o', color='red', markersize=10, label='Калибровочные точки')
plt.plot(units_line, pressure_line, '-', color='blue', linewidth=2, label=f'P = {k:.3f}x + {b:.3f}')
plt.xlabel('Условные единицы', fontsize=12)
plt.ylabel('Давление (мм рт ст)', fontsize=12)
plt.title('Калибровочный график', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()

# Коэффициент корреляции
correlation = np.corrcoef(units, pressure_mmHg)[0, 1]
print(f"\nКоэффициент корреляции: {correlation:.6f}")
