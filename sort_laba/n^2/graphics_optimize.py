import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document

def fun(string,c, naming):
    file_bubble = open("n^2/" + string, "r")
    x_bubble = []
    for i in range(1, 4001):
        x_bubble.append(i)
    y_bubble = []
    for line in file_bubble:
        y_bubble.append(int(line))
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

fun("o1.txt",'r',"o1")
fun("o2.txt",'b',"o2")
fun("o3.txt",'g',"o3")
fun("ofast.txt",'y',"ofast")

plt.legend()
plt.show()