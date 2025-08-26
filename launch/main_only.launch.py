from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    """Alternative main launch that demonstrates loading components separately."""
    
    pkg_dir = get_package_share_directory('composable_example')
    
    # First create the container
    container = ComposableNodeContainer(
        name='my_component_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[],  # Start empty
        output='screen',
    )
    
    return LaunchDescription([
        container
    ])