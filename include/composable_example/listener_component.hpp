#ifndef COMPOSABLE_EXAMPLE__LISTENER_COMPONENT_HPP_
#define COMPOSABLE_EXAMPLE__LISTENER_COMPONENT_HPP_

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

namespace composable_example
{

class ListenerComponent : public rclcpp::Node
{
public:
  explicit ListenerComponent(const rclcpp::NodeOptions & options);

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg);
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

}  // namespace composable_example

#endif  // COMPOSABLE_EXAMPLE__LISTENER_COMPONENT_HPP_