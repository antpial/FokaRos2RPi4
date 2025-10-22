from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory 

def generate_launch_description():

    config_path = os.path.join(
        get_package_share_directory('system_launcher'),
        'config',
        'system_config.yaml'
    )

    telemetry_cwd = os.path.join(
        get_package_share_directory('telemetry')
    )

    return LaunchDescription([
        Node(
            package='aggregator',
            executable='aggregator', 
            name='aggregator',
            parameters=[config_path]
        ),
        Node(
            package='saver',
            executable='saver',
            name='saver'
        ),
        # Node(
        #     package='sensor_ph',
        #     executable='sensor_ph',
        #     name='sensor_ph',
        #     parameters=[config_path]
        # ),
        Node(
            package='sensor_thermometer',
            executable='sensor_thermometer',
            name='sensor_thermometer',
            parameters=[config_path]
        ),                  
        # Node(
        #     package='sensor_tds',
        #     executable='sensor_tds',
        #     name='sensor_tds',
        #     parameters=[config_path]
        # ),
        # Node(
        #     package='sensor_voltage',
        #     executable='sensor_voltage',
        #     name='sensor_voltage',
        #     parameters=[config_path]
        # ),
        Node(
            package='sensor_gps',
            executable='sensor_gps',
            name='sensor_gps',
            parameters=[config_path]
        ),
        # Node(
        #     package='sensor_turbidity',
        #     executable='sensor_turbidity',
        #     name='sensor_turbidity',
        #     parameters=[config_path]
        # ),
        Node(
            package='sensor_depth',
            executable='sensor_depth',
            name='sensor_depth',
            parameters=[config_path]
        ),
        # Node(
        #     package='telemetry',
        #     executable='telemetry',
        #     name='telemetry',
        #     parameters=[config_path],
        #     output='screen',
        #     cwd=telemetry_cwd,
        # ),
    ])

def main():
    generate_launch_description()
    print("Launched all")

if __name__ == '__main__':
    main()

