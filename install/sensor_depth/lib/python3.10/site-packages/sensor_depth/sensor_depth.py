import rclpy    # Standard ROS 2 library for Python
from rclpy.node import Node # Base class for ROS 2 nodes
from std_msgs.msg import Float32 # Sensor Ph bedzie podawal dane w formacie Float32
from sensor_depth.sensor_depth_driver import sensor_depth_driver # Importuje moj wlasny sterownik (plik obok)
from system_launcher.log_helper import setup_logger # Samemu stworzony logger, taki sam w kazdym module


class sensor_depth_node(Node):
    def __init__(self):
        super().__init__('sensor_depth')

        # Deklaracja parametrow (wraz z domyslnymi gdyby nie podano w pliku konfiguracyjnym)
        self.declare_parameter('publish_frequency', 1.0)    #in Hz
        self.declare_parameter('topic_name', 'sensor_depth')

        # Pobranie wartosci parametrow z pliku configuracyjnego
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value
        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value

        # Inicjalizacja sterownika senosra depth i loggera 
        self.log = setup_logger(self)
        try:
            self.driver_depth = sensor_depth_driver()
        except Exception as e:
            self.log("sensor_depth, error w czasie inicjalizacji sterownika: " + str(e))
            self.get_logger().error(f'Error initializing sensor_depth driver: {e}')

        # Utworzenie publishera na dane z czujnika pH
        self.publisher = self.create_publisher(Float32, topic_name, 10)
        self.timer = self.create_timer(1.0 / frequency, self.publish_depth)
        self.get_logger().info(f'Depth node started, publishing every {1.0 / frequency:.2f} seconds.')

    # Publikowanie topicu z danymi pH dla aggregatora
    def publish_depth(self):
        msg = Float32()
        try:
            # msg = self.driver_depth.read_data_example_Float32()
            msg = self.driver_depth.read_data_Float32()
        except Exception as e:
            self.log("sensor_depth, error w czasie odczytu danych ze sterownika: " + str(e))
            self.get_logger().error(f'Error reading data from sensor_depth driver: {e}')
            return
        self.publisher.publish(msg)
        self.get_logger().info(f'Published depth: {msg.data:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = sensor_depth_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
