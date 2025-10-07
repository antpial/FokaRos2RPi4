#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import pigpio
import time


class ThrusterDriver(Node):
    def __init__(self):
        super().__init__('thruster_driver')

        # Konfiguracja pinów PWM
        self.LEFT_PIN = 13   # lewy thruster
        self.RIGHT_PIN = 12  # prawy thruster
        self.PWM_FREQUENCY = 50  # Hz
        self.PWM_RANGE = 20000   # odpowiada 20 ms okresowi (50 Hz)

        # Inicjalizacja pigpio
        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("Nie udało się połączyć z demonem pigpiod! Uruchom: sudo pigpiod")
            exit(1)

        # Ustaw tryb pinów
        self.pi.set_mode(self.LEFT_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.RIGHT_PIN, pigpio.OUTPUT)

        # Odblokowanie ESC – ustawienie sygnału neutralnego (1.5 ms)
        self.idle_us = 1500
        self.min_us = 1000
        self.max_us = 2000

        self.get_logger().info("Odblokowuję ESC – ustawiam neutralne PWM (1.5ms) na 10 sekund...")
        self.pi.set_servo_pulsewidth(self.LEFT_PIN, self.idle_us)
        self.pi.set_servo_pulsewidth(self.RIGHT_PIN, self.idle_us)
        time.sleep(10)
        self.get_logger().info("ESC odblokowane. Oczekuję komend thrust...")

        # Subskrypcje ROS
        self.create_subscription(Float32, 'left_thrust', self.left_callback, 10)
        self.create_subscription(Float32, 'right_thrust', self.right_callback, 10)

    def thrust_to_us(self, thrust):
        """
        Konwersja wartości z zakresu [-1, 1] na impuls w mikrosekundach [1000, 2000]
        """
        thrust = max(-1.0, min(1.0, thrust))  # ograniczenie zakresu
        return int(self.idle_us + thrust * 500)  # 0 → 1500, ±1 → 1000/2000

    def left_callback(self, msg):
        pwm_us = self.thrust_to_us(msg.data)
        self.pi.set_servo_pulsewidth(self.LEFT_PIN, pwm_us)
        self.get_logger().debug(f"LEFT thrust={msg.data:.2f} → {pwm_us} µs")

    def right_callback(self, msg):
        pwm_us = self.thrust_to_us(msg.data)
        self.pi.set_servo_pulsewidth(self.RIGHT_PIN, pwm_us)
        self.get_logger().debug(f"RIGHT thrust={msg.data:.2f} → {pwm_us} µs")

    def destroy_node(self):
        # Zatrzymanie silników i czyszczenie pinów
        self.get_logger().info("Zatrzymuję thrusters i czyszczę piny GPIO...")
        self.pi.set_servo_pulsewidth(self.LEFT_PIN, 0)
        self.pi.set_servo_pulsewidth(self.RIGHT_PIN, 0)
        self.pi.set_mode(self.LEFT_PIN, pigpio.INPUT)
        self.pi.set_mode(self.RIGHT_PIN, pigpio.INPUT)
        self.pi.stop()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ThrusterDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
