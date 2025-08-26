cmake_minimum_required(VERSION 3.8)
project(composable_example)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(std_msgs REQUIRED)

# Include directories
include_directories(include)

# Create library for talker component
add_library(talker_component SHARED
  src/talker_component.cpp)
target_compile_definitions(talker_component
  PRIVATE "COMPOSITION_BUILDING_DLL")
ament_target_dependencies(talker_component
  rclcpp
  rclcpp_components
  std_msgs)
rclcpp_components_register_nodes(talker_component 
  "composable_example::TalkerComponent")

# Create library for listener component
add_library(listener_component SHARED
  src/listener_component.cpp)
target_compile_definitions(listener_component
  PRIVATE "COMPOSITION_BUILDING_DLL")
ament_target_dependencies(listener_component
  rclcpp
  rclcpp_components
  std_msgs)
rclcpp_components_register_nodes(listener_component 
  "composable_example::ListenerComponent")

# Install libraries
install(TARGETS
  talker_component
  listener_component
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)

# Install headers
install(DIRECTORY include/
  DESTINATION include)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()