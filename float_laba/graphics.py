import matplotlib.pyplot as plt

def fun(string,c, naming):
    file_bubble = open(string, "r")
    
    y_bubble = []
    for line in file_bubble:
        if(float(line) > 0.34):
            y_bubble.append(0.333)
        else:
            y_bubble.append(float(line))

    x_bubble = []
    for i in range(len(y_bubble)):
        x_bubble.append(i*10)
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

fun("./float_laba/integrate_double.txt",'g',"int_float")
plt.legend()
plt.show()