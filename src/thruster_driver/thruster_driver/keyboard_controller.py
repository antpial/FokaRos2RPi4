#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import sys, termios, tty

class KeyboardThrust(Node):
    def __init__(self):
        super().__init__('keyboard_thrust')
        self.left_pub = self.create_publisher(Float32, 'left_thrust', 10)
        self.right_pub = self.create_publisher(Float32, 'right_thrust', 10)

        self.left = 0.0
        self.right = 0.0

        self.get_logger().info("Sterowanie klawiaturą: [W/S] przód/tył, [A/D] skręt, [Q] wyjście")
        self.loop()

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def loop(self):
        while rclpy.ok():
            key = self.get_key()
            if key.lower() == 'w':
                self.left += 0.1
                self.right += 0.1
            elif key.lower() == 's':
                self.left -= 0.1
                self.right -= 0.1
            elif key.lower() == 'a':
                self.left -= 0.1
                self.right += 0.0
            elif key.lower() == 'd':
                self.left += 0.0
                self.right -= 0.1
            elif key.lower() == 'r':
                self.left = 0.0
                self.right = 0.0
            elif key.lower() == 'q':
                break

            # ogranicz wartości do [-1, 1]
            self.left = max(-1.0, min(1.0, self.left))
            self.right = max(-1.0, min(1.0, self.right))

            self.left_pub.publish(Float32(data=self.left))
            self.right_pub.publish(Float32(data=self.right))

            print(f"\rLEFT: {self.left:.2f}  RIGHT: {self.right:.2f}", end="")

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardThrust()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
