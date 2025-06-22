import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_ph.sensor_ph_driver import sensor_ph_driver

class sensor_ph_node(Node):
    def __init__(self):
        super().__init__('sensor_ph')

        # Inicjalizacja sterownika pH
        self.driver_ph = sensor_ph_driver()

        # Parametr: częstotliwość publikacji
        self.declare_parameter('publish_frequency', 1.0)
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value

        self.publisher = self.create_publisher(Float32, 'sensor_ph', 10)
        self.timer = self.create_timer(1.0 / frequency, self.publish_ph)

        self.get_logger().info(f'Ph node started, publishing every {1.0 / frequency:.2f} seconds.')

    def publish_ph(self):
        msg = Float32()
        # Symulowane ph
        msg = self.driver_ph.read_data_example_Float32()
        self.publisher.publish(msg)
        self.get_logger().info(f'Published ph: {msg.data:.2f} ph')

def main(args=None):
    rclpy.init(args=args)
    node = sensor_ph_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
