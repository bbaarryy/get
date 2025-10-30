import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage):
    plt.figure(figsize = (10,6))
    plt.plot(time,voltage)
    plt.grid()
    plt.show()

def plot_sampling_period_hist(time):
    affect_time = []
    for i in range(len(time)-1):
        affect_time.append(time[i+1]-time[i])
    print(affect_time)
    plt.figure(figsize = (10,6))
    plt.hist(affect_time)
    #plt.xlim(0, 0.06)
    plt.grid()
    plt.show()

