import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})

def fun(arr):
    x = []
    y = arr
    st = y[0]
    for i in range(len(arr)):
        x.append(i)
        y[i] = y[i] - st
    #plt.plot(x,y)

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
    sigma_k = 0
    sigma_k = 1/((len(x))**0.5) * (y_2_av / x_2_av - k**2)**0.5

    #print((sigma_k/k))
    return(k*800*2,sigma_k/k)
    

freqs = [[1.314,1.530,1.745,1.961,2.178],
       [1.326, 1.542, 1.760, 1.976, 2.194],
       [1.333,1.555,1.777,1.992,2.211],
       [1.361,1.578,1.800,2.023,2.246],
       [1.150,1.379,1.603,1.828,2.054]]

freq_air = [25.2,30.2,35,45,54.9]

ks=[]
gammas = []
ans = 0
for i in range(len(freqs)):

    k = fun(freqs[i])[0]
    q = fun(freqs[i])[1]
    ks.append(k)
    gammas.append((29 / 1000 * (1/(8.31 * (freq_air[i] + 273.15)))) * k * k)
    print(gammas[i])
    ans += gammas[i]

ans /= 5
print(ans)
#plt.plot(freq_air,ks)
plt.plot([0,1,2,3,4],gammas)

plt.ylabel(r"Показатель адиабаты",fontsize=20)
plt.xlabel("Номер",fontsize=20)
plt.grid()
plt.show()

