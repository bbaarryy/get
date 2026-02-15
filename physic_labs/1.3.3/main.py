import matplotlib.pyplot as plt

micros_t = [5,10,15,20,30,40,50,60]
qs_t = [0.541, 1.013, 1.518, 1.989, 2.920, 3.840, 4.729, 5.549]
plt.rcParams.update({'font.size': 15})

micros = [130,161,200,260, 297, 327, 100,231]
qs = [7.757, 8.603, 9.654, 11.192, 11.923, 12.704, 6.859, 10.465]

table = [[0, 46, 88, 140, 206],
         [46, 0,  9,  63, 131],
         [88,  9, 0,  30,  99],
         [140,63, 30,  0,  56],
         [206,131,99,  56,  0]]

arr_table = [11,41,81,131]
anss = []

curr_summ = 0
for j in range(0,2):
    for i in range(1,5):
        curr_summ   = table[j][i]
        anss.append(curr_summ)
    plt.plot(arr_table,anss,c='r')
    plt.scatter(arr_table,anss,c='r')
    anss.clear()    


# micros.sort()
# qs.sort()

# plt.plot(micros, qs,c = 'r')
# plt.scatter(micros,qs,c='g')

# plt.plot(micros_t, qs_t,c='r')
# plt.scatter(micros_t,qs_t,c='g')

plt.grid()

plt.xlabel(r"Расстояние от 0, см",fontsize=20)
plt.ylabel("Давление, мм в ст",fontsize=20)
# # plt.legend()
plt.show()