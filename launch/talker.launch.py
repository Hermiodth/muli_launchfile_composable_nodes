from launch import LaunchDescription
from launch_ros.actions import LoadComposableNodes, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition

def generate_launch_description():
        container_id_arg = DeclareLaunchArgument(name='container_id', default_value='')
        standalone_arg = DeclareLaunchArgument(name='standalone', default_value='true')
        
        node = ComposableNode(
            package='composable_example',
            plugin='composable_example::TalkerComponent',
            name='talker',
            parameters=[{'use_sim_time': False}],
            extra_arguments=[{'use_intra_process_comms': True}],
        )
        
        # Load talker component into the container (if standalone == false)
        load_comp_nodes = LoadComposableNodes(
            condition=UnlessCondition(LaunchConfiguration('standalone')),
            composable_node_descriptions=[node],
            target_container=LaunchConfiguration('container_id'),
        )
    
        # Create new component container and add the node to it (if standalone == true)
        standalone_container = ComposableNodeContainer(
            condition=IfCondition(LaunchConfiguration('standalone')),
            name='talker_standalone_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[node],  # Start empty
            output='screen',
        )
    
        return LaunchDescription([
            container_id_arg,
            standalone_arg,
            load_comp_nodes,
            standalone_container
        ])