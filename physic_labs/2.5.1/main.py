import matplotlib.pyplot as plt
import math

ps = [144,142,141,140,139,138,136,133]
ts = [22.5, 27.3,32.3,37.3,42.3,47.2,52.0,57.0]
ros =[0.9953, 0,9888, ]

for i in range(len(ps)):
    ps[i] = 0.2 * 9.8067 * ps[i] *  

r = 0.0007
P = []
for i in range(len(ps)):
    P.append(ps[i] * r /2)