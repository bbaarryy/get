import matplotlib.pyplot as plt


k1 = 0.6
k2 = 0.3
fig, (axs1, axs2, axs3) = plt.subplots(3, 1, figsize = (6, 4))

def fun(k1,k2,k3,axs1):
    ts = []
    vs = []
    xs = []
    ass =[]

    dx0 = 20
    dv0 = 20
    da0 = 20

    last_dxdt = 0
    last_dvdt = 0
    last_dadt = 0

    for t in range(0,100):
        dx0 += last_dxdt
        dv0 += last_dvdt
        da0 += last_dadt

        curr_dxdt = (1-k1) * dv0 + t * da0
        curr_dvdt = -k2 * dv0 + da0
        curr_dadt = -k3 * dv0

        last_dvdt = curr_dvdt
        last_dxdt = curr_dxdt
        last_dadt = curr_dadt

        # print(dx0,dv0)
        vs.append(dv0)
        xs.append(dx0)
        ass.append(da0)
        ts.append(t)

    axs1.plot(ts,vs,color='r')
    axs1.plot(ts,xs,color='g')
    axs1.plot(ts,ass,color='b')
    axs1.grid()

fun(0.4,0.3,0.6,axs1)
fun(1.1,0.3,1.1,axs2)
fun(1.1,0.2,0.3,axs3)

plt.show()
