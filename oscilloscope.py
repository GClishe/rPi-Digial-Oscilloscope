import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

channel = AnalogIn(ads,ADS.P1)

plt.ion() #interactive plot
fig, ax = plt.subplots()
times=[]
voltages=[]
line, = ax.plot(times,voltages)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_ylim(0,3.3) #we are currently using the 3.3 V pin

start_time=time.time()

try:
    while True:
        current_time = time.time() - start_time
        voltage = channel.voltage
        
        times.append(current_time)
        voltages.append(voltage)
        
        line.set_xdata(times)
        line.set_ydata(voltages)
        ax.relim()
        ax.autoscale_view()
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("stopped")
                   
                   