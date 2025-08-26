#include "composable_example/talker_component.hpp"
#include "rclcpp_components/register_node_macro.hpp"

#include <chrono>
#include <memory>

namespace composable_example
{

TalkerComponent::TalkerComponent(const rclcpp::NodeOptions & options)
: Node("talker", options), count_(0)
{
  // Create publisher
  publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
  
  // Create timer
  timer_ = this->create_wall_timer(
    std::chrono::milliseconds(500),
    std::bind(&TalkerComponent::timer_callback, this));
  
  RCLCPP_INFO(this->get_logger(), "Talker component initialized");
}

void TalkerComponent::timer_callback()
{
  auto message = std_msgs::msg::String();
  message.data = "Hello World: " + std::to_string(count_++);
  RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
  publisher_->publish(message);
}

}  // namespace composable_example

// Register the component with class_loader
RCLCPP_COMPONENTS_REGISTER_NODE(composable_example::TalkerComponent)