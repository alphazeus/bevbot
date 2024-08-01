# BEVBot
BEVBot codebase is for the complete control of the robot with its embedded hardware including
- [X] Lidar (Livox MID360)
- [ ] Camera (OAK-D Lite)
- [X] IMU (MPU 6050)

Whole code is based on the Nvidia Jetson TX2 and ROS2 humble platform. The ROS2 workspace is created in such a way that you can remove any folder from src and run each hardware independently if needed.

##Running the project:
It will be quite hard to get everything running first time. The breakdown of testing each component is mentioned below and at the end about running everything together.

### ROS2 Nodes
#### Lidar
The code for lidar is based on the Livox MID 360. As an initial setup, follow the instructions mentioned in the [Livox github](https://github.com/Livox-SDK/livox_ros_driver2).
Navigate to the `<BEVBot folder>/bevbot_ws` Test your code by running the following launch file:
```
ros2 launch launch/lidar_plc2_launch.py
```
To test the code, on a new terminal, run
```
ros2 topic list
```
You should be able to see two topics `/livox/imu` and  `/livox/lidar`

#### IMU
IMU node is based on the MPU6050 hardware.
Dependencies:
- Python: > 3.9
- mpu6050

Make sure to update the repositories before every step.
```
sudo apt-get update
```

Running the node :
Make sure to install the dependecies:
```
pip install mpu6050
```
If you have a specific version of python running, like python3.10, use
```
python3.10 -m pip install mpu6050
```

Navigate to `<bevbot_folder>/bevbot_ws` and run
```
colcon build
```
Then source the setup file for ros2
```
source install/setup.sh
```
Finally run the node
```
ros2 run imu_pkg imu_angle
```
This should start the ros2 topic publishing the IMU data on `/imu_angle`

## References
[MPU6050 DMP Library](https://github.com/OmidAlekasir/mpu6050)
[Livox ROS2 Driver](https://github.com/Livox-SDK/livox_ros_driver2)
