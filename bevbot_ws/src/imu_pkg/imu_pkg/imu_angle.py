__author__ = 'Ferdinand Thomas' #ferdinand.mec@gmail.com based on work of 'Majid Alekasir'

import rclpy
from rclpy.node import Node
from mpu6050 import MPU6050
from datetime import datetime
from std_msgs.msg import String


class IMUPublisher(Node):


    def __init__(self):
        self.i2c_bus = 0
        self.device_address = 0x68
        self.freq_divider = 0x20

        # Make an MPU6050
        self.mpu = MPU6050(self.i2c_bus, self.device_address, self.freq_divider)

        # Initiate your DMP
        self.mpu.dmp_initialize()
        self.mpu.set_DMP_enabled(True)

        self.packet_size = self.mpu.DMP_get_FIFO_packet_size()
        self.FIFO_buffer = [0]*64
        
        super().__init__('imu_publisher')
        self.publisher_ = self.create_publisher(String, 'imu_angle', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        if self.mpu.isreadyFIFO(self.packet_size): # Check if FIFO data are ready to use...
        
            self.FIFO_buffer = self.mpu.get_FIFO_bytes(self.packet_size) # get all the DMP data here
        
            q = self.mpu.DMP_get_quaternion_int16(self.FIFO_buffer)
            grav = self.mpu.DMP_get_gravity(q)
            roll_pitch_yaw = self.mpu.DMP_get_euler_roll_pitch_yaw(q)
        
            msg = String()
            now = datetime.now()
            msg.data = now.strftime("Timestamp: %m/%d/%Y, %H:%M:%S.%f")
            msg.data += '\nAngles: %f, %f, %f' % (roll_pitch_yaw.x, roll_pitch_yaw.y, roll_pitch_yaw.z)
            self.publisher_.publish(msg)
            #self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    imu_publisher = IMUPublisher()

    rclpy.spin(imu_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    imu_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


