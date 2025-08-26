from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import ComposableNodeContainer
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():        
    container_id_arg = DeclareLaunchArgument(name='container_id', default_value='ce_container')
        
    # First create the container
    container = ComposableNodeContainer(
        name=LaunchConfiguration('container_id'),
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[],  # Start empty
        output='screen',
    )
    
    talker = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('composable_example'),
                'launch',
                'talker.launch.py'
            ])
        ]),
        launch_arguments={
            #'custom_config': LaunchConfiguration('custom_config')
            'container_id': LaunchConfiguration('container_id'),
            'standalone': 'false'
        }.items(),
    )
    
    listener = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('composable_example'),
                'launch',
                'listener.launch.py'
            ])
        ]),
        launch_arguments={
            #'custom_config': LaunchConfiguration('custom_config')
            'container_id': LaunchConfiguration('container_id'),
            'standalone': 'false'
        }.items(),
    )
    
    return LaunchDescription([
        container_id_arg,
        container,
        talker,
        listener
    ])