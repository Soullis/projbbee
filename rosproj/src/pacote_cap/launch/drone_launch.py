from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        Node(
            package='pacote_cap',
            executable='obstacle_detector',
            name='my_detector'
        ),

        Node(
            package='pacote_cap',
            executable='obstacle_navigator',
            name='my_navigator',
        ),

        Node(
            package='pacote_cap',
            executable='drone_controller',
            name='drone_controller'
        ),
   ])
