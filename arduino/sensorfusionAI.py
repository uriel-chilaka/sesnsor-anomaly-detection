from engi1020.arduino.api import *
import time
import os

filename = "sensor_log.csv"
file_exists = os.path.exists(filename)

f = open(filename, "a")

if not file_exists:
    f.write("timestamp,light,sound,temperature\n")
    f.flush()
    
while True:
    light = analog_read(6)
    sound = analog_read(0)
    temperature = pressure_get_temp()

    #timestamp to get current time
    ts = time.time()
    line = f"{ts},{light},{sound},{temperature}\n"
    print(line.strip())
    f.write(line)
    f.flush()
    
    oled_print(f"L:{light} S:{sound} T:{round(temperature, 1)}")
    time.sleep(0.5)
    oled_clear()