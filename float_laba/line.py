import matplotlib.pyplot as plt

x_arr = []
for i in range(1000):
    x_arr.append(i/1000)
y_arr = []
for i in range(len(x_arr)):
    y_arr.append(x_arr[i]**2)
plt.scatter(x_arr,y_arr,color = 'b', s = 5, label = 'x^2')

y_arr.clear()
for i in range(len(x_arr)):
    y_arr.append(2*x_arr[i])
plt.scatter(x_arr,y_arr,color = 'g', s = 5, label = '2x')

y_arr.clear()
for i in range(len(x_arr)):
    y_arr.append(x_arr[i]**3/3)
plt.scatter(x_arr,y_arr,color = 'r', s = 5, label = 'x**3/3')

plt.legend()
plt.show()