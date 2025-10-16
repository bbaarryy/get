import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document

def fun(string,c, naming):
    file_bubble = open(string, "r")
    x_bubble = []
    for i in range(1, 4001):
        x_bubble.append(i)
    y_bubble = []
    for line in file_bubble:
        y_bubble.append(int(line))
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

fun("sort_laba/n^2/olog0.txt",'r',"o0")
fun("sort_laba/n^2/olog1.txt",'b',"o1")
fun("sort_laba/n^2/olog2.txt",'g',"o2")
fun("sort_laba/n^2/olog3.txt",'y',"o3")

plt.legend(fontsize = "30")
plt.show()