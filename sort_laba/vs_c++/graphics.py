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
        if(len(y_bubble) < 4000):
            y_bubble.append(int(line))
        else:
            break
    plt.scatter(x_bubble,y_bubble,color = c, s = 5, label = naming)

# fun("sort_laba/vs_c++/python_time",'r','python biuld-in')
# fun("sort_laba/vs_c++/data_cfast.txt",'g',"c++ build-in")
fun("sort_laba/vs_c++/data_bubble.txt",'y','c++ slow')
fun("sort_laba/vs_c++/python_bubbletime.txt",'b',"python slow")

plt.legend(fontsize = "30")
plt.show()