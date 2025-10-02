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

fun("sort_laba/n^2/data_insertion.txt",'r',"insertion")
fun("sort_laba/n^2/data_bubble.txt",'b',"bubble")
fun("sort_laba/n^2/data_shaker.txt",'g',"shaker")


plt.legend()
plt.show()