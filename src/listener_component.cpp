#include "composable_example/listener_component.hpp"
#include "rclcpp_components/register_node_macro.hpp"

#include <memory>

namespace composable_example
{

ListenerComponent::ListenerComponent(const rclcpp::NodeOptions & options)
: Node("listener", options)
{
  // Create subscription
  subscription_ = this->create_subscription<std_msgs::msg::String>(
    "chatter", 10,
    std::bind(&ListenerComponent::topic_callback, this, std::placeholders::_1));
  
  RCLCPP_INFO(this->get_logger(), "Listener component initialized");
}

void ListenerComponent::topic_callback(const std_msgs::msg::String::SharedPtr msg)
{
  RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
}

}  // namespace composable_example

// Register the component with class_loader
RCLCPP_COMPONENTS_REGISTER_NODE(composable_example::ListenerComponent)