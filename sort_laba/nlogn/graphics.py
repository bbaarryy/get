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

def print(pref,color):
    fun("sort_laba/nlogn/data_merging" + pref + ".txt",color,"merge" + pref)
    fun("sort_laba/nlogn/data_heap" + pref + ".txt",color,"heap"+pref)
    fun("sort_laba/nlogn/data_quick" + pref + ".txt",color,"quick"+pref)

print("_b","green")
print("_w", "red")
print("", "y")

plt.legend()
plt.show()