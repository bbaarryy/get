strings = list(map(str, input().split(" ")))

mapic = {}

for i in range(len(strings)):
    mapic[strings[i]] = 0

for i in range(len(strings)):
    mapic[strings[i]] += 1

new_ans = []
max_len = -1

for i in range(len(strings)):
    if(mapic[strings[i]] >= 1):
        new_ans.append(strings[i])
        mapic[strings[i]]=0
        max_len = max(max_len, len(strings[i]))

for i in range(len(new_ans)):
    new_ans[i] = "{"*(max_len - len(new_ans[i])) + new_ans[i]

new_ans.sort()

for i in range(len(new_ans)):
    for j in range(max_len):
        if(new_ans[i][j]!="{"):
            print(new_ans[i][j], end = '')
    print('\n', end = '')


