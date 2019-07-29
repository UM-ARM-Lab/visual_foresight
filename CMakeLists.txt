cmake_minimum_required(VERSION 2.8.3)
project(foresight_rospkg)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

catkin_package()

catkin_python_setup()
