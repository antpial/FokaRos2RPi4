import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from msg_interfaces.msg import SensorData  # Importing the custom message type

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(SensorData, '/sensor_data', 10)
        timer_period = 1.0  # sekunda
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = SensorData()
        msg.temperature = 20.0 + self.i  # Example temperature valu
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg}"')
        self.i += 1
        if self.i >10:
            self.i = 0

def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
