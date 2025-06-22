import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import csv
import os
from datetime import datetime

class SaverNode(Node):
    def __init__(self):
        super().__init__('saver')

        # Subskrypcja danych z agregatora
        self.subscription = self.create_subscription(
            String,
            '/aggregated/data',
            self.listener_callback,
            10
        )

        # Tworzenie pliku do zapisu
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.filename = f'data/data_log_{timestamp}.csv'
        self.get_logger().info(f'Saving data to: {self.filename}')

        self.file = open(self.filename, mode='w', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=['timestamp', 'temperature', 'ph', 'turbidity'])
        self.writer.writeheader()

    def listener_callback(self, msg):
        try:
            data = json.loads(msg.data)
            self.writer.writerow({
                'timestamp': data.get('timestamp'),
                'temperature': data.get('temperature'),
                'ph': data.get('ph'),
                'turbidity': data.get('turbidity')
            })
        except Exception as e:
            self.get_logger().error(f"Failed to parse or write data: {e}")

    def destroy_node(self):
        self.get_logger().info('Shutting down. Closing file.')
        self.file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = SaverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()