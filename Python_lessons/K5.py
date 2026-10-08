name = input()

try:
    curr_file = open(name, 'r')
except:
    print(0)
    exit(0)

max_size = -1
ans = 0

for line in curr_file:
    arr = list(map(int,line.split(' ')))
    if(max_size < len(arr)):
        ans = sum(arr)
    elif(max_size == len(arr)):
        ans = max(ans,sum(arr))

    max_size = max(max_size, len(arr))
    
print(ans)

