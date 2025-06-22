import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class TelemetryNode(Node):
    def __init__(self):
        super().__init__('telemetry')

        # Parametr: co ile sekund wysyłać dane
        self.declare_parameter('send_interval', 2.0)
        self.send_interval = self.get_parameter('send_interval').value

        self.latest_data = None

        # Subskrypcja z agregatora
        self.subscription = self.create_subscription(
            String,
            '/aggregated/data',
            self.aggregated_callback,
            10
        )

        # Timer do wysyłania
        self.create_timer(self.send_interval, self.send_data)

        self.get_logger().info(f"Telemetry node started. Will 'send' data every {self.send_interval} seconds.")

    def aggregated_callback(self, msg):
        try:
            self.latest_data = json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().error("Received invalid JSON from aggregator.")

    def send_data(self):
        if self.latest_data is None:
            self.get_logger().warn("No data available yet.")
            return

        # Na razie: wysyłanie na terminal w prostym protokole tekstowym
        # Przykład: TEMP=24.3;PH=6.9;TURB=0.55;TIME=1717509001
        message = f"TEMP={self.latest_data.get('temperature')};" \
                  f"PH={self.latest_data.get('ph')};" \
                  f"TURB={self.latest_data.get('turbidity')};" \
                  f"TIME={self.latest_data.get('timestamp')}"
        print(f"[TELEMETRY OUT] {message}")

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