import matplotlib.pyplot as plt

def plot_pressure_vs_time(time, pressure):
    plt.figure(figsize = (10,6))
    plt.plot(time,pressure)
    plt.grid()
    plt.show()

