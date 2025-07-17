import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from msg_interfaces.msg import GpsData
import json

class AggregatorNode(Node):
    def __init__(self):
        super().__init__('aggregator')

        # Bufor na dane (może być None, jeśli nie przyszły)
        self.latest_data = {
            'gps': None,
            'temperature': None,
            'ph': None,
            'turbidity': None,
            'tds': None,
            'voltage': None,
        }

        # Deklaracja parametrow (wraz z domyslnymi gdyby nie podano w pliku konfiguracyjnym)
        self.declare_parameter('publish_frequency', 1.0)

        # Pobranie wartosci parametrow z pliku configuracyjnego
        self.publish_frequency = self.get_parameter('publish_frequency').get_parameter_value().double_value

        # Subskrypcje z czujników
        self.create_subscription(GpsData, '/sensor_gps', self.gps_callback, 10)
        self.create_subscription(Float32, '/sensor_thermometer', self.temp_callback, 10)
        self.create_subscription(Float32, '/sensor_ph', self.ph_callback, 10)
        self.create_subscription(Float32, '/sensor_turbidity', self.turb_callback, 10)
        self.create_subscription(Float32, '/sensor_tds', self.tds_callback, 10)
        self.create_subscription(Float32, '/sensor_voltage', self.voltage_callback, 10)

        # Jeden wspólny publisher
        self.publisher = self.create_publisher(String, '/aggregated/data', 10)

        # Timer do publikowania
        self.create_timer(1.0 / self.publish_frequency, self.publish_aggregated_data)

    # Metoda do czyszczenia ostatnich danych z czujnika
    def clear_data(self):
        for sensor in self.latest_data:
            self.latest_data[sensor] = None

    def gps_callback(self, msg):
        self.latest_data['gps'] = msg

    def temp_callback(self, msg):
        self.latest_data['temperature'] = msg.data

    def ph_callback(self, msg):
        self.latest_data['ph'] = msg.data

    def turb_callback(self, msg):
        self.latest_data['turbidity'] = msg.data

    def tds_callback(self, msg):
        self.latest_data['tds'] = msg.data

    def voltage_callback(self, msg):
        self.latest_data['voltage'] = msg.data

    def publish_aggregated_data(self):
        # Tworzymy pakiet danych z aktualnymi wartościami (None jeśli brak)
        gps_msg = self.latest_data['gps']
        if gps_msg is not None:
            gps_data = {
                'latitude': gps_msg.latitude,
                'longitude': gps_msg.longitude,
                'velocity': gps_msg.velocity,
                'satelites': gps_msg.satelites,
                'hdop': gps_msg.hdop
            }
        else:
            gps_data = None

        data = {
            'gps': gps_data,
            'temperature': self.latest_data['temperature'],
            'ph': self.latest_data['ph'],
            'turbidity': self.latest_data['turbidity'],
            'tds': self.latest_data['tds'],
            'voltage': self.latest_data['voltage'],
            'timestamp': self.get_clock().now().to_msg().sec

        }
        self.clear_data()  # Czyścimy dane po publikacji

        msg = String()
        msg.data = json.dumps(data)
        self.publisher.publish(msg)
        self.get_logger().info(f'Published aggregated: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = AggregatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()