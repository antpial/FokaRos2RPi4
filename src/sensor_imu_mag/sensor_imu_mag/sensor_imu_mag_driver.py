import time
import board
import busio
import adafruit_lsm9ds1
from sensor_msgs.msg import Imu, MagneticField
import random
import math

class SensorIMUDriver:
    def __init__(self):
        # Utworzenie magistrali I2C
        i2c = busio.I2C(board.SCL, board.SDA)
        
        # Inicjalizacja IMU LSM9DS1
        self.imu = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
        
        # Wiadomości ROS
        self.imu_msg = Imu()
        self.mag_msg = MagneticField()
    
    def read_data_example(self):
        """
        Symulacja odczytu danych (jak GPS example)
        """
        # Przyspieszenie w m/s^2
        self.imu_msg.linear_acceleration.x = random.uniform(-2, 2)
        self.imu_msg.linear_acceleration.y = random.uniform(-2, 2)
        self.imu_msg.linear_acceleration.z = random.uniform(-2, 2)
        
        # Żyroskop w rad/s
        self.imu_msg.angular_velocity.x = random.uniform(-250, 250)
        self.imu_msg.angular_velocity.y = random.uniform(-250, 250)
        self.imu_msg.angular_velocity.z = random.uniform(-250, 250)
        
        # Magnetometr w Tesla
        self.mag_msg.magnetic_field.x = random.uniform(-50e-6, 50e-6)
        self.mag_msg.magnetic_field.y = random.uniform(-50e-6, 50e-6)
        self.mag_msg.magnetic_field.z = random.uniform(-50e-6, 50e-6)
        
        return self.imu_msg, self.mag_msg
    
    def read_data(self):
        """
        Odczyt rzeczywistych danych z IMU LSM9DS1
        """
        # Przyspieszenie w m/s^2
        ax, ay, az = self.imu.acceleration
        self.imu_msg.linear_acceleration.x = ax
        self.imu_msg.linear_acceleration.y = ay
        self.imu_msg.linear_acceleration.z = az
        
        # Żyroskop w rad/s
        gx, gy, gz = self.imu.gyro
        # Konwersja z deg/s na rad/s
        self.imu_msg.angular_velocity.x = math.radians(gx)
        self.imu_msg.angular_velocity.y = math.radians(gy)
        self.imu_msg.angular_velocity.z = math.radians(gz)
        
        # Magnetometr w Tesla (LSM9DS1 daje w gaussach)
        mx, my, mz = self.imu.magnetic
        self.mag_msg.magnetic_field.x = mx * 1e-4
        self.mag_msg.magnetic_field.y = my * 1e-4
        self.mag_msg.magnetic_field.z = mz * 1e-4
        
        return self.imu_msg, self.mag_msg
