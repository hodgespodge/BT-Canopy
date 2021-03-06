import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
# from ament_index_python import get_package_share_directory

def generate_launch_description():

    coverage_node = Node(
        package='bt_canopy_bringup',
        executable='coverage_monitor',
        name='coverage_monitor_node',
        output='screen',
        emulate_tty=True,
    )

    return LaunchDescription([
        coverage_node

    ])