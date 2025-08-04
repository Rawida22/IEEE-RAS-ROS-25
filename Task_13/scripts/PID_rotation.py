#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
import math
# PID Parameters 
kp = 1.2
ki = 0.0
kd = 0.3

# Variables
current_yaw = None
# current yaw ±90 
target_yaw = None
yaw_error = 0.0
yaw_integral = 0.0
yaw_prev_error = 0.0

yaw_tolerance = math.radians(1)  # ±1 degree
cmd_pub = None
# Normalize angle to [-pi, pi] 
def normalize_angle(angle):
    if angle > math.pi:
        angle -= 2 * math.pi
    elif angle < - math.pi:
        angle += 2 * math.pi
    return angle
    
# IMU callback 
def imu_callback(msg):
    global current_yaw
    orientation_q = msg.orientation
    quaternion = [msg.orientation.x , msg.orientation.y ,msg.orientation.z ,msg.orientation.w]
    ( _, _, current_yaw) = euler_from_quaternion(quaternion)
def odom_callback(msg):
    pass

# Control loop 
def control_loop(event):
    global yaw_error, yaw_integral, yaw_prev_error
    if current_yaw is None or target_yaw is None:
        return

    yaw_error = normalize_angle(target_yaw - current_yaw)

    if abs(yaw_error) < yaw_tolerance:
        stop_robot()
        rospy.loginfo("Rotation complete!")
        rospy.signal_shutdown("Finished precise turn")
        return

    yaw_integral += yaw_error
    yaw_derivative = yaw_error - yaw_prev_error 
    yaw_prev_error = yaw_error
    angular_z = kp * yaw_error + ki * yaw_integral + kd * yaw_derivative
    # Limit angular speed
    angular_z = max(min(angular_z, 0.5), -0.5)

    # Publish command
    twist = Twist()
    twist.angular.z = angular_z
    cmd_pub.publish(twist)

# ---- Stop robot ----
def stop_robot():
    twist = Twist()
    cmd_pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node("precise_90_rotation")
    cmd_pub =rospy.Publisher("/cmd_vel",Twist,queue_size=10)
    rospy.Subscriber("/mpu6050", Imu, imu_callback)
    rospy.Subscriber("/odom",Odometry,odom_callback)
    rospy.sleep(1)  

    if current_yaw is not None :
        target_yaw = normalize_angle(current_yaw + math.radians(90))
        rospy.loginfo(f"Target Yaw: {math.degrees(target_yaw):.2f}°")
    rospy.Timer(rospy.Duration(0.05), control_loop)
    rospy.spin()


