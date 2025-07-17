from std_msgs.msg import String

def setup_logger(node):
    """Rejestruje publisher logów i zwraca funkcję logującą."""
    log_pub = node.create_publisher(String, '/system_logs', 10)

    def log(text):
        msg = String()
        msg.data = text
        log_pub.publish(msg)

    return log
