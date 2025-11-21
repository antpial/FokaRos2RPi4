from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction
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
        # Uruchomienie GPS
        Node(
            package='sensor_gps',
            executable='sensor_gps',
            name='sensor_gps',
            parameters=[config_path]
        ),
        # Uruchomienie IMU/Mag po 5 sekundach
        Node(
                package='sensor_imu_mag',
                executable='sensor_imu_mag',
                name='sensor_imu_mag',
                parameters=[config_path]
        ),
        # Uruchomienie compass po kolejnych 5 sekundach
        TimerAction(
            period=5.0,  # 5s + 5s = 10s od startu launch
            actions=[
                Node(
                    package='autopilot',
                    executable='compass',
                    name='compass',
                    parameters=[config_path]
                )
            ]
        ),

        # Uruchomienie checkpoints po kolejnych 5 sekundach
        TimerAction(
            period=10.0,  # 5s + 5s + 5s = 15s od startu launch
            actions=[
                Node(
                    package='autopilot',
                    executable='checkpoints',
                    name='checkpoints',
                    parameters=[config_path]
                )
            ]
        )
    ])

def main():
    generate_launch_description()
    print("Launched all for autopilot")

if __name__ == '__main__':
    main()
