cmake_minimum_required(VERSION 3.8)
project(pacote_cap)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SendCommand.srv"
)

ament_python_install_package()