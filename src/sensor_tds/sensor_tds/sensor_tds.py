import rclpy    # Standard ROS 2 library for Python
from rclpy.node import Node # Base class for ROS 2 nodes
from std_msgs.msg import Float32 # Sensor Ph bedzie podawal dane w formacie Float32
from sensor_tds.sensor_tds_driver import sensor_tds_driver # Importuje moj wlasny sterownik (plik obok)
from system_launcher.log_helper import setup_logger # Samemu stworzony logger, taki sam w kazdym module


class sensor_tds_node(Node):
    def __init__(self):
        super().__init__('sensor_tds')

        # Deklaracja parametrow (wraz z domyslnymi gdyby nie podano w pliku konfiguracyjnym)
        self.declare_parameter('publish_frequency', 1.0)    #in Hz
        self.declare_parameter('topic_name', 'sensor_tds')
        self.declare_parameter('adc_channel', -1)   # -1 oznacza, ze nie podano w pliku konfiguracyjnym, wtedy wyskoczy blad
        
        # Pobranie wartosci parametrow z pliku configuracyjnego
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value
        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        adc_channel = self.get_parameter('adc_channel').get_parameter_value().integer_value

        # Inicjalizacja sterownika senosra pH i loggera 
        self.log = setup_logger(self)
        try:
            self.driver_tds = sensor_tds_driver(adc_channel=adc_channel)
        except Exception as e:
            self.log("sensor_tds, error w czasie inicjalizacji sterownika: " + str(e))
            self.get_logger().error(f'Error initializing sensor_tds driver: {e}')

        # Utworzenie publishera na dane z czujnika pH
        self.publisher = self.create_publisher(Float32, topic_name, 10)
        self.timer = self.create_timer(1.0 / frequency, self.publish_tds)
        self.get_logger().info(f'Tds node started, publishing every {1.0 / frequency:.2f} seconds.')

    # Publikowanie topicu z danymi pH dla aggregatora
    def publish_tds(self):
        msg = Float32()
        try:
            # msg = self.driver_tds.read_data_example_Float32()
            msg = self.driver_tds.read_data_Float32()
        except Exception as e:
            self.log("sensor_tds, error w czasie odczytu danych ze sterownika: " + str(e))
            self.get_logger().error(f'Error reading data from sensor_tds driver: {e}')
            return
        self.publisher.publish(msg)
        self.get_logger().info(f'Published tds: {msg.data:.2f} ppm')

def main(args=None):
    rclpy.init(args=args)
    node = sensor_tds_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
