import matplotlib.pyplot as plt

# ---------------
#  TOP-CAPACITY
# ---------------

# file = open("./STL_Laba/0.capacity-top.txt")
# i=0
# xs = []
# tops=[]
# capacities=[]
# for line in file:
#     top, capacity = map(int,line.split(' '))
#     xs.append(i)
#     i+=1
#     tops.append(top)
#     capacities.append(capacity)
# plt.plot(xs,tops,c = 'g',label = 'top')
# plt.plot(xs,capacities,c = 'b',label='capacity')
# plt.legend()
# plt.show()

# --------------

# ----------------------
#  STL-MY VECTOR INSERT
# ----------------------

# file = open("./STL_Laba/1.insert.txt")
# xs = []
# my_vector = []
# stl_vector= []

# ind= 0
# for line in file:
#     my, stl = map(float, line.split(' '))
#     my_vector.append(my)
#     stl_vector.append(stl)
#     xs.append(ind)
#     ind+=1

# plt.scatter(xs,my_vector,c = 'r',label = 'my')
# plt.scatter(xs,stl_vector,c = 'g',label='stl')
# plt.legend()
# plt.show()
# --------------

# ---------------------
#  STL-MY VECTOR ERASE
# ---------------------
# file = open("./STL_Laba/2.erase.txt")
# xs = []
# my_vector = []
# stl_vector= []

# ind= 0
# for line in file:
#     my, stl = map(float, line.split(' '))
#     my_vector.append(my)
#     stl_vector.append(stl)
#     xs.append(ind)
#     ind+=1

# plt.scatter(xs,my_vector,c = 'r',label = 'my')
# plt.scatter(xs,stl_vector,c = 'g',label='stl')
# plt.legend()
# plt.show()

# --------------

# ---------------------
#  STL_LIST PUSHFRONT
# ---------------------

# file = open("./STL_Laba/3.push_list.txt")
# xs = []
# us_list = []
# f_us_list = []

# ind= 0
# for line in file:
#     us, f_us = map(float, line.split(' '))
#     us_list.append(us)
#     if(f_us < 10**(-6)/3):
#         f_us_list.append(f_us)
#     else:
#         f_us_list.append(10**(-6))
#     xs.append(ind)
#     ind+=1

# #plt.scatter(xs,us_list,c = 'r',label = 'usual')
# plt.scatter(xs,f_us_list,c = 'g',label='forward')
# plt.legend()
# plt.show()


file = open("./STL_Laba/4.map-set.txt")
xs = []
us_list = []
f_us_list = []

ind= 0
for line in file:
    us, f_us = map(float, line.split(' '))
    us_list.append(us)
    if(f_us < 10**(-6)/3):
        f_us_list.append(f_us)
    else:
        f_us_list.append(10**(-6))
    xs.append(ind)
    ind+=1

plt.scatter(xs,us_list,c = 'r',label = 'usual')
plt.scatter(xs,f_us_list,c = 'g',label='forward')
plt.legend()
plt.show()
