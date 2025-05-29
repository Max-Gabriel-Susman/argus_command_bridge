# Argus Command Bridge 

Argus Command Bridge is a lightweight ROS 2 package that provides a secure gateway for tele-operating Argus Bot from anywhere.

## Local Setup 


Prior to the rest of these steps you'll need to be in an Ubuntu 20 environment with ROS 2 Foxy installed.

Create a workspace directory: 
```
mkdir dev_ws
```

Source the setup script(location may be different on your machine):
```
source /opt/ros/foxy/setup.bash
```

Create a `src` sub directory to store packages in: 
```
mkdir dev_ws/src
```

Navigate into the `src` directory and clone this repository: 
```
git clone https://github.com/Max-Gabriel-Susman/argus_command_bridge
```

Navigate back to the workspace root(`dev_ws`) and build it with `colcon` using the `symlink-install` setting: 
```
colcon build --symlink-install
```

Ensure `xacro` and `joint_state_publisher_gui` are installed:
```
sudo apt install ros-foxy-xacro ros-foxy-joint-state-publisher-gui
```

Source the workspace: 
```
source install/setup.bash
```

If you're launching without Gazebo(this method defaults to unix time): 
```
ros2 launch argus_command_bridge rsp.launch.py
```
