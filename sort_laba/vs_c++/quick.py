import random
import time

def quick_sort(arr,l_b,r_b):
    if(r_b-l_b <= 1 or l_b >= r_b):
        return
    
    l=l_b
    r=r_b
    m = arr[(l+r)//2]

    while(l<r):
        while(arr[l] < m):
            l+=1
        while(arr[r] > m):
            r-=1
        if(l<=r):
            arr[l], arr[r] = arr[r],arr[l]
    quick_sort(arr,l,r_b)
    quick_sort(arr,l_b,r)

file = open("sort_laba/vs_c++/python_time","w")

file_data = open("sort_laba/vs_c++/arrs","r")
in_data = []
for line in file_data:
    in_data.append(int(line))
ind = 0

for count in range(1,5001):
    arr = []
    for i in range(count):
        arr.append(in_data[ind])
        ind +=1
    start_time = time.time_ns()
    arr.sort()
    end_time = time.time_ns()
    arr.clear()
    #print(end_time - start_time)
    file.write(str(end_time - start_time) + '\n')
file.close()
