import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document
import math

def fun(string,c, naming):
    file_bubble = open(string, "r")
    x_bubble = []
    for i in range(1, 4001):
        x_bubble.append(i)
    y_bubble = []
    tt = 0
    for line in file_bubble:
        tt += 1
        if(int(line) == 0 or math.log(tt) == 0):
            y_bubble.append(0)
        else:
            y_bubble.append(int(line)/(tt * math.log(tt)))
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

fun("sort_laba/nlogn/data_heap.txt",'r',"heap")
fun("sort_laba/nlogn/data_quick.txt",'b',"quick")
fun("sort_laba/nlogn/data_merging.txt",'g',"merge")

plt.legend()
plt.show()