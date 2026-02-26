from skyfield.api import load, wgs84
from skyfield.sgp4lib import EarthSatellite
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 15})


line1 = '1 33591U 09005A   26055.21485026  .00000032  00000-0  40752-4 0  9998'
line2 = '2 33591  98.9636 125.9615 0013475 354.3600   5.7419 14.13453966878522'

ts = load.timescale()
satellite = EarthSatellite(line1, line2, 'noaa19', ts)
location = wgs84.latlon(55.930172, 37.518217)

t_start = ts.utc(2026, 1, 1)
t_end = ts.utc(2026, 3, 1)

times, events = satellite.find_events(location, t_start, t_end, altitude_degrees=0.0)

vis_table = open("vis.txt",'w')
for t, event in zip(times, events):
    if(event == 0):
        vis_table.write(f"{t.utc_strftime('%Y-%m-%d %H:%M:%S')}" + " - ")
        #print(f"{t.utc_strftime('%Y-%m-%d %H:%M:%S')}" , "Восход")
    elif(event == 2):
        vis_table.write(f"{t.utc_strftime('%Y-%m-%d %H:%M:%S')}" + '\n')
        #print(f"{t.utc_strftime('%Y-%m-%d %H:%M:%S')}" , "Заход")

### graphic

t_0 = ts.utc(2026, 1, 1)
t_1 = ts.utc(2026, 1, 3)
gaps = ts.linspace(t_0,t_1,1000)

azimut = []
altitud = []

for t in gaps:
    alt, az, distance = (satellite - location).at(t).altaz()
    if alt.degrees > 0:
        azimut.append(az.degrees)
        altitud.append(alt.degrees)

fig, axes = plt.subplots(subplot_kw={'projection': 'polar'})
axes.set_theta_zero_location('N')
axes.set_ylim(90, 0)
axes.plot(np.radians(azimut), altitud, linewidth=1)
plt.show()

vis_table.close()