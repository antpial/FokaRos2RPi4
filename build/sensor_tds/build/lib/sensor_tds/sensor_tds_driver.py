import random
from std_msgs.msg import Float32
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO


class sensor_tds_driver:
    def __init__(self,*, adc_channel):
        self.data = Float32()
        # Inicjalizacja magistrali I2C
        i2c = busio.I2C(board.SCL, board.SDA)
        # Inicjalizacja ADS1015
        ads = ADS.ADS1015(i2c)
        # Ustawienie kanału ADC
        if adc_channel < 0 or adc_channel > 3:
            raise ValueError("adc_channel must be between 0 and 3 ")
        # Assign the channel based on adc_channel parameter
        channels = [ADS.P0, ADS.P1, ADS.P2, ADS.P3]
        self.chan = AnalogIn(ads, channels[adc_channel])


    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.data = random.uniform(100.0, 250.0)  # Example data
        return self.data

    def read_data_Float32(self):
        # I'll add a method to read data from the sensor
        voltage = self.chan.voltage
        ppm = self._voltage_to_ppm(voltage)
        print(f"Napięcie: {voltage:.3f} V, Stężenie: {ppm:.1f} ppm")
        self.data.data=ppm
        return self.data
    
    # Funkcja do przeliczenia napięcia na ppm (0V = 0ppm, 2.3V = 1000ppm)
    @staticmethod
    def _voltage_to_ppm(voltage, v_max=2.3, ppm_max=1000.0):
        # Zabezpieczenie przed przekroczeniem zakresu
        if voltage < 0.0:
            return 0.0
        elif voltage > v_max:
            return ppm_max
        return ((voltage / v_max) * ppm_max)
