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
        self.writer = csv.DictWriter(self.file, fieldnames=[
            'timestamp', 
            'latitude', 
            'longitude', 
            'satelites', 
            'velocity', 
            'acceleration', 
            'temperature', 
            'ph', 
            'turbidity', 
            'tds', 
            'voltage'])
        self.writer.writeheader()

    def listener_callback(self, msg):
        try:
            data = json.loads(msg.data)
            gps = data.get('gps') or {}

            self.writer.writerow({
                'timestamp': data.get('timestamp'),
                'latitude': gps.get('latitude'),
                'longitude': gps.get('longitude'),
                'satelites': gps.get('satelites'),
                'velocity': gps.get('velocity'),
                'acceleration': gps.get('acceleration'),
                'temperature': data.get('temperature'),
                'ph': data.get('ph'),
                'turbidity': data.get('turbidity'),
                'tds': data.get('tds'),
                'voltage': data.get('voltage')
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