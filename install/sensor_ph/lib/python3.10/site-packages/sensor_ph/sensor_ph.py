import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_ph.sensor_ph_driver import sensor_ph_driver
from system_launcher.log_helper import setup_logger


class sensor_ph_node(Node):
    def __init__(self):
        super().__init__('sensor_ph')

        # Inicjalizacja sterownika senosra pH i loggera 
        self.driver_ph = sensor_ph_driver()
        self.log = setup_logger(self)
        self.log("Sensor pH node initialized.")

        # Deklaracja parametrow (wraz z domyslnymi gdyby nie podano w pliku konfiguracyjnym)
        self.declare_parameter('publish_frequency', 1.0)    #in Hz
        self.declare_parameter('topic_name', 'sensor_ph')

        # Pobranie wartosci parametrow z pliku configuracyjnego
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value
        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value

        # Utworzenie publishera na dane z czujnika pH
        self.publisher = self.create_publisher(Float32, topic_name, 10)
        self.timer = self.create_timer(1.0 / frequency, self.publish_ph)
        self.get_logger().info(f'Ph node started, publishing every {1.0 / frequency:.2f} seconds.')

    # Publikowanie topicu z danymi pH dla aggregatora
    def publish_ph(self):
        msg = Float32()
        msg = self.driver_ph.read_data_example_Float32()
        self.publisher.publish(msg)
        self.get_logger().info(f'Published ph: {msg.data:.2f} w skali ph')

def main(args=None):
    rclpy.init(args=args)
    node = sensor_ph_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
