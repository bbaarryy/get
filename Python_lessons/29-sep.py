# file = open("./Python_lessons/BTC_data.csv", "r")

# q = 3
# for line in file:
#     print(line)
#     if(q==0):
#         break
#     q-=1

import pandas as pd
df = pd.read_csv("./Python_lessons/BTC_data.csv")
print(df[0:5])

k = 5
for i in range(k,len(df)):
    average = 0
    for j in range(i-k,i):
        average += df[i][j]

    average /= k

    average_m = 0
    for j in range(i-k,i):
        average_m += (j-(i-k)+1) * df[i][j]
    average_m/= (k+1)*k/2