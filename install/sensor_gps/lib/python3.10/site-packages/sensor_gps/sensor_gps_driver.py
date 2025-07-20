import random
from std_msgs.msg import Float32
from msg_interfaces.msg import GpsData
from sensor_gps import L76X
import time
import math
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO


class sensor_gps_driver:
    def __init__(self,*, adc_channel):
        self.data = GpsData()
        self.x = L76X.L76X()
        self.x.L76X_Set_Baudrate(115200)
        #x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
        #time.sleep(2)
        #x.L76X_Set_Baudrate(115200)

        self.x.L76X_Send_Command(self.x.SET_POS_FIX_400MS);

        #Set output message
        self.x.L76X_Send_Command(self.x.SET_NMEA_OUTPUT);

        self.x.L76X_Exit_BackupMode();

    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.latitude = random.uniform(51.0, 52.0)
        self.data.longitude = random.uniform(17.0, 18.0)
        self.data.velocity = round(random.uniform(0.0, 2.0), 3)
        self.data.hdop = round(random.uniform(0.0, 1.0), 3)
        self.data.satelites = float(random.randint(0, 12))
        return self.data

    def read_data_Float32(self):
        self.x.L76X_Gat_GNRMC()
        if(self.x.Status == 1):
            print('Already positioned')
        else:
            print('No positioning')
            raise Exception("GPS not positioned")
        self.data.latitude = self.x.Lat
        self.data.longitude = self.x.Lon
        self.data.velocity = round(self.x.SpeedMh, 3) # m/s
        self.data.hdop = round(self.x.HDOP,3)  
        self.data.satelites = round(float(self.x.Satellites), 3)  # Round to 3 decimal places  
        return self.data
    
