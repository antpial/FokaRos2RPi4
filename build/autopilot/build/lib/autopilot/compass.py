import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, MagneticField
from std_msgs.msg import Float32
import math

class AzimuthCalculatorNode(Node):
    def __init__(self):
        super().__init__('azimuth_calculator')

        # Parametry
        self.declare_parameter('mag_topic', '/imu/mag')
        self.declare_parameter('publish_topic', '/current_azimuth')
        self.declare_parameter('publish_frequency', 1.0)  # Hz
        self.declare_parameter('imu_rotation', 90.0)
        self.declare_parameter('magnetic_declination', -4.0)  # degrees (4E lotnisko wroclaws)
        self.declare_parameter('magnetic_deviation', 0.0)  # degrees (4E lotnisko wroclaws)


        mag_topic = self.get_parameter('mag_topic').get_parameter_value().string_value
        self.publish_topic = self.get_parameter('publish_topic').get_parameter_value().string_value
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value

        # Subskrypcja magnetometru
        self.mag_vector = None
        self.mag_sub = self.create_subscription(MagneticField, mag_topic, self.mag_callback, 10)

        # Publisher azymutu
        self.publisher = self.create_publisher(Float32, self.publish_topic, 10)

        # Timer publikacji azymutu
        self.timer = self.create_timer(1.0 / frequency, self.publish_azimuth)

        self.get_logger().info(f'Azimuth Calculator Node started. Reading {mag_topic} and publishing {self.publish_topic} at {frequency} Hz.')


    def mag_callback(self, msg: MagneticField):
        # Zapisujemy najnowszy wektor pola magnetycznego
        self.mag_vector = msg.magnetic_field
        if self.mag_vector == None:
            self.get_logger().warning('Received empty magnetometer data.')


    def calculate_current_azimuth(self):
        # obliczam kat sredniego wektora pola magnetycznego
        theta_rad = math.atan2(self.mag_vector.y, self.mag_vector.x)

        # Konwertuje z rad na stopnie
        theta_deg = math.degrees(theta_rad)     

        # atan2 oblicza kat od osi x, a polnoc jest na osi y (+90), wiec trzeba obrocic
        azimuth = theta_deg + 90.0
        # Dodaje korekty
        azimuth += self.get_parameter('imu_rotation').get_parameter_value().double_value
        azimuth += self.get_parameter('magnetic_declination').get_parameter_value().double_value    
        azimuth += self.get_parameter('magnetic_deviation').get_parameter_value().double_value

        # atan 2 daje wartosc w przedziale (-pi,pi), a nie (0,2pi), a wiec dla
        # azymutu z przedzialu (180,360) musimy przekalkulowac
        if(azimuth < 0):
            azimuth += 360.0

        return azimuth
   

    def publish_azimuth(self):
        azimuth = self.calculate_current_azimuth()
        if azimuth is None:
            self.get_logger().warning('No magnetometer data received yet.')
            return

        msg = Float32()
        msg.data = float(azimuth)
        self.publisher.publish(msg)
        self.get_logger().info(f'Published current azimuth: {azimuth:.2f} deg')

def main(args=None):
    rclpy.init(args=args)
    node = AzimuthCalculatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
