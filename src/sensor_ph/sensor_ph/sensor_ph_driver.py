import random
from std_msgs.msg import Float32

class sensor_ph_driver:
    def __init__(self):
        self.data = Float32()

    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.data = random.uniform(5.0, 9.0)  # Example data
        return self.data

    def read_data_Float32(self):
        # I'll add a method to read data from the sensor
        return self.data
