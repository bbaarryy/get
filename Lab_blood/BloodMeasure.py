import time
import BloodFunctions as m3021
import abc_plot as abcp

values = []
time_values = []
pressure_values = []
duration = 15.0

my_plate = m3021.MCP3021(5.19)

curr_time = 0

start = time.time()

file = open("./Lab_blood/data_4.txt",'w')

while curr_time < duration:
    ans = my_plate.get_number()
    time.sleep(0.001)
    curr_time = time.time() - start
    time_values.append(curr_time)
    values.append(ans)
    file.write(str(ans) + ' ' + str(curr_time) + '\n')
    print(curr_time)

abcp.plot_pressure_vs_time(time_values, values)
        
        
            

