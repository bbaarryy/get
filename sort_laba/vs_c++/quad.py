import random
import time

def bubble_sort(arr):
    while True:
        ch=1
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                ch=0
        if(ch):
            return arr
            

file = open("sort_laba/vs_c++/python_bubbletime.txt","w")

for count in range(1,5001):
    arr = []
    for i in range(count):
        arr.append(random.randint(-1000,1000))
    start_time = time.time_ns()
    arr = bubble_sort(arr)
    #print(arr)
    end_time = time.time_ns()
    arr.clear()
    #print(end_time - start_time)
    file.write(str(end_time - start_time) + '\n')
file.close()
