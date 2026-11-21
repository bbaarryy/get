import matplotlib.pyplot as plt
import math

pi=3.1415926535
x_bubble = [0.0108, 0.0328, 0.0209, 0.0108, 0.0073, 0.0327, 0.0209, 0.0073]
y_bubble = [0.112,0.335,0.215,0.112,0.076,0.335,0.215,0.076]

for i in range(len(x_bubble)):
    x_bubble[i] *= 2 * pi

z_bubble = []
aver = 0 
for i in range(len(x_bubble)):
    curr = ((y_bubble[i] * 9.8 * 0.121)/(0.00079 * x_bubble[i]))
    z_bubble.append(curr)
    aver += curr
aver /= 8
print(aver)
def get_ab(i20,u20):
    x_a,y_a,xy_a,x2_a =0,0,0,0
    y2_a = 0
    r_a = 0
    for i in range(len(i20)):
        x_a += i20[i]
        y_a += u20[i]
        xy_a += i20[i] * u20[i]
        x2_a += i20[i] ** 2
        y2_a += u20[i] **2
        r_a += 5000*u20[i]/(i20[i]*5000 - u20[i])
    xy_a /= 10
    x_a /=10
    y_a /=10
    x2_a /=10
    y2_a /=10

    print(xy_a/x2_a)
    #print(y2_a,x2_a)
  

plt.scatter(x_bubble,y_bubble,color = 'r', label = "omega(m)")
#plt.scatter(x_bubble,z_bubble,color = 'g', label = "omega(m)")

get_ab(x_bubble,y_bubble)

plt.grid()
plt.legend()
plt.show()