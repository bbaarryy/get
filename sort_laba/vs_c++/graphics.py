import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document

def fun(string,c, naming):
    file_bubble = open(string, "r")
    x_bubble = []
    for i in range(1, 5001):
        x_bubble.append(i)
    y_bubble = []
    for line in file_bubble:
        y_bubble.append(int(line))
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

fun("sort_laba/vs_c++/python_time",'r','python fast')
fun("sort_laba/vs_c++/data_cfast.txt",'g',"c++")

plt.legend()
plt.show()