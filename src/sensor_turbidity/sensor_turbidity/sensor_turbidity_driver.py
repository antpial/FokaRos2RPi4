import random
from std_msgs.msg import Float32
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO


class sensor_turbidity_driver:
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
        self.data.data = random.uniform(2.5, 4.0)  # Example data
        return self.data

    def read_data_Float32(self):
        # I'll add a method to read data from the sensor
        voltage = self.chan.voltage
        tss = self._v2tss(voltage)
        print(f"Napięcie: {voltage:.3f} V, Tss: {tss:.1f} tss")
        return Float32(data=tss)
    
    # Funkcja do przeliczenia napięcia na tss ze wzoru z dokumntacji
    @staticmethod
    def _v2tss(v):
        tss = -1120.4 * v**2 + 5742.3 * v - 4352.9
        return tss
