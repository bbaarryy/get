k = int(input())

dic = {}

for i in range(k):
    s, n = map(str,input.split(" "))
    n = int(n)
    if s in dic:
        dic[s].append(n)
    else:
