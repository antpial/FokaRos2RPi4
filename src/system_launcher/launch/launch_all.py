from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='aggregator',
            executable='aggregator', 
            name='aggregator'
        ),
        Node(
            package='saver',
            executable='saver',
            name='saver'
        ),
        Node(
            package='sensor_ph',
            executable='sensor_ph',
            name='sensor_ph'
        ),
        Node(
            package='sensor_thermometer',
            executable='sensor_thermometer',
            name='sensor_thermometer'
        ),
        Node(
            package='telemetry',
            executable='telemetry',
            name='telemetry'
        ),
        # msg_interfaces nie zawiera node'ów – tylko wiadomości
    ])

if __name__ == '__main__':
    main()

def main():
    generate_launch_description()
    print("Launched all")
