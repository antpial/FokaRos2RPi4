import random
from std_msgs.msg import Float32
import time
import board
import busio
import RPi.GPIO as GPIO


class sensor_depth_driver:
    def __init__(self):
        self.data = Float32()
        # Piny GPIO
        self.TRIG = 23
        self.ECHO = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)


    def read_data_example_Float32(self):
        # Simulate reading data from the sensor
        self.data.data = random.uniform(20.0, 400.0)  # Example data
        return self.data

    def read_data_Float32(self):
        # Krótki impuls na TRIG
        self.data.data = -10.0
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)   # 10 µs
        GPIO.output(self.TRIG, False)

        # --- czekaj na start impulsu ECHO ---
        start_wait = time.time()
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()
            if pulse_start - start_wait > 1.0:  # timeout 1s
                print("Błąd: brak startu impulsu ECHO")
                raise Exception("Timeout start")

        # --- czekaj na koniec impulsu ECHO ---
        start_wait = time.time()
        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
            if pulse_end - start_wait > 1.0:  # timeout 1s
                print("Błąd: brak końca impulsu ECHO")
                raise Exception("Timeout end")

        # Czas trwania impulsu
        pulse_duration = pulse_end - pulse_start

        # Przelicz na cm (prędkość dźwięku 34300 cm/s)
        self.data.data = pulse_duration * 34300 / 2
        return self.data
        
    # # Funkcja do przeliczenia napięcia na ppm (0V = 0ppm, 2.3V = 1000ppm)
    # @staticmethod
    # # Funkcja przeliczająca napięcie na pH (szybki start, bez kalibracji)
    # def _voltage_to_ph(voltage):
    #     return 7 + ((2.5 - voltage) / 0.17)
