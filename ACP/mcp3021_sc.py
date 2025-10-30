import time
import mcp3021_driver as m3021
import abc_plot as abcp

voltage_values = []
time_values = []
duration = 3.0

my_plate = m3021.MCP3021(5.19)

curr_time = 0

try:
    update=0
    start = time.time()
    while(curr_time < duration):
        while curr_time < duration:
            ans = my_plate.get_voltage()
            
            voltage_values.append(ans)
            print(curr_time,end = '\r')
            last_ans = ans
            time.sleep(0.001)
            curr_time = time.time() - start
            time_values.append(curr_time)
    print(123)
finally:
    print(len(time_values), len(voltage_values))
    abcp.plot_voltage_vs_time(time_values,voltage_values)
    #abcp.plot_sampling_period_hist(time_values)
        
        
            

