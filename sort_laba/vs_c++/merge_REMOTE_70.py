import random
import time

def merging(arr_l,arr_r):
    arr= []
    l = 0
    r = 0
    while(l < len(arr_l) and r < len(arr_r)):
        if(arr_l[l] < arr_r[r]):
            arr.append(arr_l[l])
            l+=1
        else:
            arr.append(arr_r[r])
            r+=1
    while(l < len(arr_l)):
        arr.append(arr_l[l])
        l+=1
    while(r < len(arr_r)):
        arr.append(arr_r[r])
        r+=1
    return arr  

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    l_arr=[]
    r_arr = []
    for i in range(0, len(arr)//2):
        l_arr.append(arr[i])
    for i in range(len(arr)//2,len(arr)):
        r_arr.append(arr[i])
    l_arr = merge_sort(l_arr)
    r_arr = merge_sort(r_arr)
    arr = merging(l_arr,r_arr)
    return arr

file = open("sort_laba/vs_c++/python_mergetime.txt","w")

for count in range(1,5001):
    arr = []
    for i in range(count):
        arr.append(random.randint(-1000,1000))
    start_time = time.time_ns()
    arr = merge_sort(arr)
    #print(arr)
    end_time = time.time_ns()
    arr.clear()
    #print(end_time - start_time)
    file.write(str(end_time - start_time) + '\n')
file.close()
