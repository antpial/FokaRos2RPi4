import random
from std_msgs.msg import Float32
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO


class sensor_voltage_driver:
    def __init__(self,*, adc_channel):
        self.data = Float32()
        # Inicjalizacja magistrali I2C
        i2c = busio.I2C(board.SCL, board.SDA)
        # Inicjalizacja ADS1015
        ads = ADS.ADS1015(i2c)
        # Ustawienie kanału ADC
        if adc_channel < 0 or adc_channel > 3:
            raise ValueError("sensor_voltage: adc_channel must be between 0 and 3 ")
        # Assign the channel based on adc_channel parameter
        channels = [ADS.P0, ADS.P1, ADS.P2, ADS.P3]
        self.chan = AnalogIn(ads, channels[adc_channel])


    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.data = random.uniform(20.0, 25.0)  # Example data
        return self.data

    def read_data_Float32(self):
        # I'll add a method to read data from the sensor
        voltage = self.chan.voltage
        v = self._scale_voltage(voltage)
        print(f"Napięcie: {voltage:.3f} V, Bateria: {v:.1f} V")
        return Float32(data=v)
    
    # Skalowanie napięcia z ADC (0–5V) na rzeczywiste (0–25V)
    @staticmethod
    def _scale_voltage(voltage_adc, scale_factor=5):
        return voltage_adc * scale_factor
