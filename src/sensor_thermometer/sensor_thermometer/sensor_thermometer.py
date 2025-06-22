import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_thermometer.sensor_thermometer_driver import sensor_thermometer_driver
class ThermometerNode(Node):
    def __init__(self):
        super().__init__('sensor_thermometer')

        # Inicjalizacja sterownika termometru
        self.driver_thermometer = sensor_thermometer_driver()
        # Parametr: częstotliwość publikacji
        self.declare_parameter('publish_frequency', 1.0)
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value

        self.publisher = self.create_publisher(Float32, 'sensor_thermometer', 10)
        self.timer = self.create_timer(1.0 / frequency, self.publish_temperature)

        self.get_logger().info(f'Thermometer node started, publishing every {1.0 / frequency:.2f} seconds.')

    def publish_temperature(self):
        msg = Float32()
        # Symulowana temperatura: wartość losowa z przedziału 20–30°C
        msg = self.driver_thermometer.read_data_example_Float32()
        self.publisher.publish(msg)
        self.get_logger().info(f'Published temperature: {msg.data:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = ThermometerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
