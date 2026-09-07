import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

m1, m2, k = 1.0, 6.0, 1.0
x1, x2, v1, v2 = sp.symbols('x1 x2 v1 v2')
k1, k2, k3, k4 = sp.symbols('k1 k2 k3 k4', real=True)

#Решение системы S' = A S
A = sp.Matrix([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [-k/m1,  k/m1, 0, 0], #
    [ k/m2, -k/m2, 0, 0]
])

C = sp.Matrix([[1, 0, 0, 0]])
K_vec = sp.Matrix([k1, k2, k3, k4])
# Произведение K*C (4x4)
KC = K_vec * C
# Ошибка(матрица) F = A - K*C
F = A - KC


#характеристический полином det(sI - F)
I = sp.eye(4)
s = sp.symbols('s')
char_poly = (s*I - F).det()

# Приводим к полиному с символьными коэффициентами
char_poly_simplified = sp.collect(sp.expand(char_poly), s)

print("\nПолином det(sI - F):")
sp.pprint(char_poly_simplified)

# Извлечение коэффициентов: a1*s**3 + a2*s**2 + a3*s + a4 + s**4
coeffs = sp.Poly(char_poly_simplified, s).all_coeffs()
# coeffs имеет вид [1, a1, a2, a3, a4]
a1, a2, a3, a4 = coeffs[1], coeffs[2], coeffs[3], coeffs[4]

print("\nКоэффициенты характеристического полинома:")
print(f"  a1 = {sp.simplify(a1)}")
print(f"  a2 = {sp.simplify(a2)}")
print(f"  a3 = {sp.simplify(a3)}")
print(f"  a4 = {sp.simplify(a4)}")

# Условия Гурвица в символьной форме

# Для полинома 4-й степени:
# (1) ai > 0
# (5) Delta2 = a1*a2 - a3 > 0
# (6) Delta3 = a1*a2*a3 - a1**2*a4 - a3**2 > 0
Delta2 = a1*a2 - a3
Delta3 = a1*a2*a3 - a1**2*a4 - a3**2

print("\nУсловия Гурвица (символьные):")
print(f"  (1) a1 = {sp.simplify(a1)} > 0")
print(f"  (2) a2 = {sp.simplify(a2)} > 0")
print(f"  (3) a3 = {sp.simplify(a3)} > 0")
print(f"  (4) a4 = {sp.simplify(a4)} > 0")
print(f"  (5) Delta2 = {sp.simplify(Delta2)} > 0")
print(f"  (6) Delta3 = {sp.simplify(Delta3)} > 0")

#Подстановка численных параметров m1, m2, k

# Заменяем символьные параметры числами
subs_dict = {m1: 1.0, m2: 6.0, k: 1.0}
a1_num = sp.simplify(a1.subs(subs_dict))
a2_num = sp.simplify(a2.subs(subs_dict))
a3_num = sp.simplify(a3.subs(subs_dict))
a4_num = sp.simplify(a4.subs(subs_dict))
Delta2_num = sp.simplify(Delta2.subs(subs_dict))
Delta3_num = sp.simplify(Delta3.subs(subs_dict))

print("\nПосле подстановки:")
print(f"  a1 = {a1_num}")
print(f"  a2 = {a2_num} = k3 + 2")
print(f"  a3 = {a3_num} = k1 + k2")
print(f"  a4 = {a4_num} = k3 + k4")
print(f"  Delta2 = {Delta2_num}")
print(f"  Delta3 = {Delta3_num}")

#6 Проверка устойчивости для заданных K

def is_okay(k1_val, k2_val, k3_val, k4_val, m1=1.0, m2=1.0, k_spring=1.0):
    #проверка гурвица для заданных значений наших переменных масс и жёсткостей
    a1 = k1_val
    a4 = k_spring*(k3_val/m2 + k4_val/m1)
    a2 = k3_val + k_spring/m1 + k_spring/m2
    a3 = k1_val*k_spring/m2 + k2_val*k_spring/m1
    
    Delta3 = a1*a2*a3 - a1**2*a4 - a3**2
    Delta2 = a1*a2 - a3
    
    checks = {
        'a1>0': a1 > 0,
        'a2>0': a2 > 0,
        'a3>0': a3 > 0,
        'a4>0': a4 > 0,
        'Δ2>0': Delta2 > 0,
        'Δ3>0': Delta3 > 0
    }
    
    return checks, (a1,a2,a3,a4,Delta2,Delta3)


#Построение 3D-поверхностей границы устойчивости elta3 = 0 при фиксированных k4


# Решаем относительно k3:
def k3_from_delta3(k1, k2, k4, m1=1.0, m2=6.0, k_spring=1.0):
    # Возвращает значение k3, при котором delta3 = 0 (граница)
    # В общем случае решаем уравнение ddelta3=0 относительно k3
    # Delta3 = a1*a2*a3 - a1**2*a4 - a3**2 = 0
    # где a1=k1, a2=k3 + k/m1 + k/m2, a3=k1*k/m2 + k2*k/m1, a4=k*(k3/m2 + k4/m1)
    # Подставляем и решаем
    a = k_spring/m1 + k_spring/m2
    b1 = k_spring/m2
    b2 = k_spring/m1
    # Delta3 = k1*(k3+a)*(k1*b1 + k2*b2) - k1**2*(k*(k3/m2 + k4/m1)) - (k1*b1 + k2*b2)**2 = 0
    # Раскрываем и решаем относительно k3
    # k1*(k3+a)*(k1*b1 + k2*b2) = k1*(k1*b1 + k2*b2)*k3 + k1*a*(k1*b1 + k2*b2)
    # k1**2*k*(k3/m2 + k4/m1) = k1**2*k*k3/m2 + k1**2*k*k4/m1
    # Подставляем:
    # k1*(k1*b1 + k2*b2)*k3 + A - (k1**2*k/m2)*k3 - B - (k1*b1 + k2*b2)**2 = 0
    # где A = k1*a*(k1*b1 + k2*b2), B = k1**2*k*k4/m1
    # k3*[k1*(k1*b1 + k2*b2) - k1**2*k/m2] + A - B - (k1*b1 + k2*b2)**2 = 0
    coeff_k3 = k1*(k1*b1 + k2*b2) - k1**2*k_spring/m2
    const_term = k1*a*(k1*b1 + k2*b2) - k1**2*k_spring*k4/m1 - (k1*b1 + k2*b2)**2

    return -const_term / coeff_k3

# Набор фиксированных k4 для построения графиков
k4_values = [-1.0, 0.0, 1.0]
# Диапазон k1, k2
k1_vals = np.linspace(0.5, 3.0, 60)
k2_vals = np.linspace(0.5, 3.0, 60)
K1, K2 = np.meshgrid(k1_vals, k2_vals)

# Цветовая карта для разных k4
colors = ['red', 'blue', 'white']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for k4_val, color in zip(k4_values, colors):
    # Вычисляем k3 для границы
    K3_boundary = np.zeros_like(K1)
    for i in range(K1.shape[0]):
        for j in range(K1.shape[1]):
            K3_boundary[i,j] = k3_from_delta3(K1[i,j], K2[i,j], k4_val, m1, m2, k)
    # Ограничим для наглядности диапазоном [-10, 10]
    K3_boundary = np.clip(K3_boundary, -10, 10)
    ax.plot_surface(K1, K2, K3_boundary, alpha=0.6, color=color, label=f'k4={k4_val}')

ax.set_xlabel('k1')
ax.set_ylabel('k2')
ax.set_zlabel('k3')
ax.set_title('Граница устойчивости при разных k_4')

legend_elements = [Patch(facecolor=color, alpha=0.6, label=f'k_4={k4}') for k4,color in zip(k4_values,colors)]
ax.legend(handles=legend_elements)
plt.show()

# Моделирование переходного процесса e(t) для устойчивых коэффициентов

# Выберем конкретный устойчивый набор внутри области (например, k4=0, k1=2, k2=1, k3=1)
k1_ex = 2.0
k2_ex = 1.0
k3_ex = 1.0
k4_ex = 0.0
checks, extra = is_okay(k1_ex, k2_ex, k3_ex, k4_ex, m1, m2, k)

print("\nПроверка устойчивости для выбранных коэффициентов:")
print(f"  k1={k1_ex}, k2={k2_ex}, k3={k3_ex}, k4={k4_ex}")
for cond, val in checks.items():
    print(f"    {cond}: {val}")

# Строим матрицу F численно
F_num = np.array([
    [-k1_ex, 0, 1, 0],
    [-k2_ex, 0, 0, 1],
    [-k/m1 - k3_ex, k/m1, 0, 0],
    [k/m2 - k4_ex, -k/m2, 0, 0]
])

# Решаем e' = F e с начальными условиями e0 = (10,10,10,10)
e0 = np.array([10.0, 10.0, 10.0, 10.0])
t_span = np.linspace(0, 20, 1000)

def ode_system(e, t):
    return F_num @ e

sol = odeint(ode_system, e0, t_span)

# Построение графика
plt.figure(figsize=(10,6))
plt.plot(t_span, sol[:,0], label='e1 (ошибка по x1)', linewidth=2)
plt.plot(t_span, sol[:,1], label='e2 (ошибка по x2)', linewidth=2)
plt.plot(t_span, sol[:,2], label='e3 (ошибка по v1)', linewidth=2)
plt.plot(t_span, sol[:,3], label='e4 (ошибка по v2)', linewidth=2)
plt.xlabel('Время t (с)', fontsize=12)
plt.ylabel('Ошибка e', fontsize=12)
plt.title('Переходный процесс ошибки наблюдателя (e0 = (10,10,10,10))', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.show()





