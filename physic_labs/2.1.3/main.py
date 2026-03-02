import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})

def fun(arr,freq,ch):
    x = []
    y = arr
    st = y[0]
    for i in range(len(arr)):
        x.append(i)
        y[i] = y[i] - st
    plt.plot(x,y)

    xy_av = 0
    x_2_av = 0
    y_2_av = 0
    for i in range(len(arr)):
        xy_av += x[i] * y[i]
        x_2_av += x[i] * x[i]
        y_2_av += y[i] * y[i]
    
    xy_av /= len(x)
    x_2_av /= len(x)
    y_2_av /= len(x)

    k = xy_av / x_2_av
    hi = 0
    for i in range(len(arr)):
        hi += (arr[i] - k*i)**2 / (1)**2
    if(ch):
        print((hi**0.5, len(arr)))
    return(k*freq*2,hi)
    

air = [[83,199],
       [55,142,227],
       [32,91,148,203],
       [44,97,151,207],
       [41,110,180],
       [42,103,167],
       [58,138,212],
       [25,72,122,170]]
freq_air = [1.5,2,3,3.2,2.5,2.75,2.25,3.5]

co2 = [[31,100,165,230],
       [65,122,170],
       [52,116,159,212],
       [23,71,121,168,216],
       [20,53,114,156,187,232],
       [8,50,92,131,178,216]]

freq_co2 = [2,2.25,2.5,2.75,3,3.2]

cs = []
ks = []
ans=0

q_a = 0

for i in range(len(co2)):
    cs.append(i)
    k = fun(co2[i],freq_co2[i],0)[0]
    q = fun(co2[i],freq_co2[i],1)[1]
    q_a += q
    ks.append(k)
    ans += ks[i]

q_a/=len(co2)
print(q_a)
plt.plot(cs,ks)
print(ans/len(co2))

plt.ylabel(r"Скорость звука",fontsize=20)
plt.xlabel("Номер опыта",fontsize=20)
plt.grid()
plt.show()

