import matplotlib.pyplot as plt

def fun(string,c, naming):
    file_bubble = open(string, "r")
    
    y_bubble = []
    for line in file_bubble:
        y_bubble.append(float(line))

    x_bubble = []
    for i in range(len(y_bubble)):
        x_bubble.append(i)
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

fun("./float_laba/norm.txt",'r',"norm")
fun("./float_laba/denorm.txt",'g',"denorm")

plt.legend()
plt.show()