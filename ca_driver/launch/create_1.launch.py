from launch import LaunchDescription
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    config = launch.substitutions.LaunchConfiguration('config', default=[launch.substitutions.ThisLaunchFileDir(), '/../config/default.yaml'])
    desc = launch.substitutions.LaunchConfiguration('desc', default=['true'])
    return LaunchDescription([
        launch_ros.actions.Node(
            node_name='ca_driver', package='ca_driver', node_executable='ca_driver', output='screen', parameters=[config, {'robot_model':'CREATE_1'}]
        )
    ])