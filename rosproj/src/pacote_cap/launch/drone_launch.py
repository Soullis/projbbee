from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        Node(
            package='pacote_cap',
            executable='objc_detector_pub',
            name='detection_talker'
        ),

        Node(
            package='pacote_cap',
            executable='objc_detector_sub',
            name='detection_listener',
            output='screen'
        )
    ])

