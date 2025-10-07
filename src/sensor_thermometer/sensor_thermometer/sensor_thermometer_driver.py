import random
import os
import glob
import time
from std_msgs.msg import Float32

class sensor_thermometer_driver:
    def __init__(self):
        self.data = Float32()
        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folder = glob.glob(self.base_dir + '28*')[0]  # bierzemy pierwszy DS18B20
        self.device_file = self.device_folder + '/w1_slave'

    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.data = random.uniform(20.0, 30.0)  # Example data
        return self.data

    def read_data_Float32(self):
        lines = self.read_temp_raw()
        # sprawdzamy czy pomiar jest OK
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # szukamy temperatury
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            self.data.data = float(temp_string) / 1000.0
            return self.data
    
    def read_temp_raw(self):
        with open(self.device_file, 'r') as f:
            return f.readlines()
