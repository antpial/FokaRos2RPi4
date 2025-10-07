import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from telemetry.loraSX1278_driver import loraSX1278_driver  # Importing the LoRa driver
import json

class TelemetryNode(Node):
    def __init__(self):
        super().__init__('telemetry')

        # Parametr: co ile sekund wysyłać dane
        self.declare_parameter('send_interval', 0.5)
        self.send_interval = self.get_parameter('send_interval').value

        # Inicjalizacja LoRa driver
        self.lora_driver = loraSX1278_driver(self.get_logger())

        self.latest_data = None

        # Subskrypcja z agregatora
        self.subscription = self.create_subscription(
            String,
            '/aggregated/data',
            self.aggregated_callback,
            10
        )

        # Timer do wysyłania
        self.create_timer(1.0 / self.send_interval, self.send_data)

        self.get_logger().info(f"Telemetry node started. Will 'send' data every {self.send_interval} seconds.")

    def aggregated_callback(self, msg):
        try:
            self.latest_data = json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().error("Received invalid JSON from aggregator.")

    def send_data(self):
        # if self.latest_data is None:
        #     self.get_logger().warn("No data available yet.")
        #     return
        # Konweruje json do stringa
        json_str = json.dumps(self.latest_data)
        try:
            self.lora_driver.send_data(json_str)
            # self.lora_driver.send_data_example(json_str)  # Sending data via LoRa
        except Exception as e:
            self.get_logger().error(f"Failed to send data via LoRa: {e}")
        self.get_logger().info(f"Sent data: {json_str}")
        self.latest_data = None

def main(args=None):
    rclpy.init(args=args)
    node = TelemetryNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()