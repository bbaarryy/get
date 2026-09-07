from time import time as t

n = range(10**5)

l=[]

t1=t()

for i in n:
    l.append(i)

print(t()-t1)

t1=t()

for i in n:
    -1 in l
print(t()-t1)

