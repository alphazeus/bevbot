# BEVBot
BEVBot codebase is for the complete control of the robot with its embedded hardware including
- [ ] Lidar (Livox MID360)
- [ ] Camera (OAK-D Lite)
- [X] IMU (MPU 6050)

Whole code is based on the Nvidia Jetson TX2 and ROS2 humble platform. The ROS2 workspace is created in such a way that you can remove any folder from src and run each hardware independently if needed.

##Running the project:
It will be quite hard to get everything running first time. The breakdown of testing each component is mentioned below and at the end about running everything together.

### ROS2 Nodes
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

Navigate to <bevbot_folder> and run
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
mpu6050 : (https://github.com/OmidAlekasir/mpu6050)
