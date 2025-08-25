import random
from std_msgs.msg import Float32
import time
import board
import busio
import RPi.GPIO as GPIO


class sensor_depth_driver:
    def __init__(self):
        self.data = Float32()


    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.data = random.uniform(20.0, 400.0)  # Example data
        return self.data

    def read_data_Float32(self):
        pass
    
    # # Funkcja do przeliczenia napięcia na ppm (0V = 0ppm, 2.3V = 1000ppm)
    # @staticmethod
    # # Funkcja przeliczająca napięcie na pH (szybki start, bez kalibracji)
    # def _voltage_to_ph(voltage):
    #     return 7 + ((2.5 - voltage) / 0.17)
