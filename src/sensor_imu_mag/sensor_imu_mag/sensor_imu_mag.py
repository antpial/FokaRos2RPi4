import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, MagneticField
from sensor_imu_mag.sensor_imu_mag_driver import SensorIMUDriver
from system_launcher.log_helper import setup_logger


class SensorIMUMagNode(Node):
    def __init__(self):
        super().__init__('sensor_imu_mag')

        # Parametry
        self.declare_parameter('publish_frequency', 10.0)    # Hz
        self.declare_parameter('imu_topic_name', 'imu/data_raw')
        self.declare_parameter('mag_topic_name', 'imu/mag')

        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value
        imu_topic_name = self.get_parameter('imu_topic_name').get_parameter_value().string_value
        mag_topic_name = self.get_parameter('mag_topic_name').get_parameter_value().string_value

        # Logger
        self.log = setup_logger(self)

        # Sterownik IMU+Mag
        try:
            self.driver = SensorIMUDriver()
        except Exception as e:
            self.log(f"sensor_imu_mag, error w czasie inicjalizacji sterownika: {e}")
            self.get_logger().error(f'Error initializing sensor_imu_mag driver: {e}')

        # Publishery
        self.imu_pub = self.create_publisher(Imu, imu_topic_name, 10)
        self.mag_pub = self.create_publisher(MagneticField, mag_topic_name, 10)

        # Timer
        self.timer = self.create_timer(1.0 / frequency, self.publish_imu_mag)
        self.get_logger().info(f'IMU Mag node started, publishing every {1.0 / frequency:.2f} seconds.')

    def publish_imu_mag(self):
        try:
            # imu_msg, mag_msg = self.driver.read_data_example()
            imu_msg, mag_msg = self.driver.read_data()
        except Exception as e:
            self.log(f"sensor_imu_mag, error w czasie odczytu danych ze sterownika: {e}")
            self.get_logger().error(f'Error reading data from sensor_imu_mag driver: {e}')
            return

        # Publikacja
        self.imu_pub.publish(imu_msg)
        self.mag_pub.publish(mag_msg)
        self.get_logger().debug('Published IMU and MagneticField data')


def main(args=None):
    rclpy.init(args=args)
    node = SensorIMUMagNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
