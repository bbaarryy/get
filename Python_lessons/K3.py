n , m = map(int,input().split(' '))

mapic = ['']*m

for i in range(m):
    curr_s = input()
    mapic[i] = curr_s

x,y,see = map(int,input().split(' '))

lc_x = max(0, x-see)
lc_y = max(0, y-see)

rd_x = min(x+see, n-1)
rd_y = min(y+see, m-1)

for i in range(lc_x , rd_x+1):
    for j in range(lc_y, rd_y+1):
        print(mapic[i][j], end = '')
    print()
