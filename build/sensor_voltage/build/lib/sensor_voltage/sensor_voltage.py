import rclpy    # Standard ROS 2 library for Python
from rclpy.node import Node # Base class for ROS 2 nodes
from std_msgs.msg import Float32 # Sensor Ph bedzie podawal dane w formacie Float32
from sensor_voltage.sensor_voltage_driver import sensor_voltage_driver # Importuje moj wlasny sterownik (plik obok)
from system_launcher.log_helper import setup_logger # Samemu stworzony logger, taki sam w kazdym module


class sensor_voltage_node(Node):
    def __init__(self):
        super().__init__('sensor_voltage')

        # Deklaracja parametrow (wraz z domyslnymi gdyby nie podano w pliku konfiguracyjnym)
        self.declare_parameter('publish_frequency', 1.0)    #in Hz
        self.declare_parameter('topic_name', 'sensor_voltage')
        self.declare_parameter('adc_channel', -1)   # -1 oznacza, ze nie podano w pliku konfiguracyjnym, wtedy wyskoczy blad
        
        # Pobranie wartosci parametrow z pliku configuracyjnego
        frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value
        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        adc_channel = self.get_parameter('adc_channel').get_parameter_value().integer_value

        # Inicjalizacja sterownika senosra pH i loggera 
        self.log = setup_logger(self)
        try:
            self.driver_voltage = sensor_voltage_driver(adc_channel=adc_channel)
        except Exception as e:
            self.log("sensor_voltage, error w czasie inicjalizacji sterownika: " + str(e))
            self.get_logger().error(f'Error initializing sensor_voltage driver: {e}')

        # Utworzenie publishera na dane z czujnika napięcia
        self.publisher = self.create_publisher(Float32, topic_name, 10)
        self.timer = self.create_timer(1.0 / frequency, self.publish_voltage)
        self.get_logger().info(f'Sensor Voltage node started, publishing every {1.0 / frequency:.2f} seconds.')

    # Publikowanie topicu z danymi napięcia na baterii dla aggregatora
    def publish_voltage(self):
        msg = Float32()
        try:
            # msg = self.driver_voltage.read_data_example_Float32()
            msg = self.driver_voltage.read_data_Float32()
        except Exception as e:
            self.log("sensor_voltage, error w czasie odczytu danych ze sterownika: " + str(e))
            self.get_logger().error(f'Error reading data from sensor_voltage driver: {e}')
            return
        self.publisher.publish(msg)
        self.get_logger().info(f'Published voltage: {msg.data:.2f} V')

def main(args=None):
    rclpy.init(args=args)
    node = sensor_voltage_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
