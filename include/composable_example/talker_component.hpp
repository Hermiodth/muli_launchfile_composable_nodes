#ifndef COMPOSABLE_EXAMPLE__TALKER_COMPONENT_HPP_
#define COMPOSABLE_EXAMPLE__TALKER_COMPONENT_HPP_

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

namespace composable_example
{

class TalkerComponent : public rclcpp::Node
{
public:
  explicit TalkerComponent(const rclcpp::NodeOptions & options);

private:
  void timer_callback();
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

}  // namespace composable_example

#endif  // COMPOSABLE_EXAMPLE__TALKER_COMPONENT_HPP_