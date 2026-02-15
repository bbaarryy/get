import matplotlib.pyplot as plt

micros = [15,20,30,40,50,60,45]
qs = [1.955, 2.619, 3.787, 4.961, 6.080, 7.072, 5.466]
plt.rcParams.update({'font.size': 15})

micros_t = [101,130,150,209,260,312,273]
qs_t = [9.024, 10.084, 10.860, 13.090, 14.755, 16.188, 15.133]

# micros_t += micros
# qs_t += qs

# micros.sort()
# qs.sort()
# micros_t.sort()
# qs_t.sort()
# plt.rcParams.update({'font.size': 15})

# #plt.plot(micros_t, qs_t,c = 'r')
# #plt.scatter(micros_t,qs_t,c='g')
# plt.plot(micros, qs,c = 'r')
# plt.scatter(micros,qs,c='g')

# plt.grid()
#plt.show()


table = [[0, 21, 39, 62, 87],
         [21, 0,  5,  29, 55],
         [39,  5, 0,  14,  40],
         [62,29, 14,  0,  20],
         [206,131,99,  56,  0]]

arr_table = [10.5,40.5,80.5,130.5]
anss = []

curr_summ = 0
for j in range(0,2):
    for i in range(1,5):
        curr_summ   = table[j][i]
        anss.append(curr_summ)
    plt.plot(arr_table,anss,c='r')
    plt.scatter(arr_table,anss,c='r')
    anss.clear()    

# table = [[0, 46, 88, 140, 206],
#          [46, 0,  9,  63, 131],
#          [88,  9, 0,  30,  99],
#          [140,63, 30,  0,  56],
#          [206,131,99,  56,  0]]

# arr_table = [11,41,51,61]
# anss = []

# curr_summ = 0
# for i in range(1,5):
#     curr_summ += table[0][i]
#     anss.append(curr_summ)

# plt.plot(anss,arr_table)

# micros += micros_t
# qs += qs_t
# micros.sort()
# qs.sort()

# #plt.plot(micros, qs,c = 'r')
# #plt.scatter(micros,qs,c='g')
plt.grid()

plt.xlabel(r"Расстояние от 0, см",fontsize=20)
plt.ylabel("Давление, мм в ст",fontsize=20)
# # plt.legend()
plt.show()