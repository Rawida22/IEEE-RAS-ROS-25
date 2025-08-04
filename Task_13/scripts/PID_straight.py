#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
# to turn IMU data into angles
from tf.transformations import euler_from_quaternion
import math
# PID variables 
kp = 1.3
ki = 0.01
kd =0.5

yaw_error = 0.0 
yaw_integral = 0.0
yaw_previous_error = 0.0 
# yaw (straight line) 
desired_yaw = None
pub =rospy.Publisher("/cmd_vel",Twist,queue_size=10)
def IMU_callback(msg):
    global yaw_error,yaw_integral,yaw_previous_error,desired_yaw
      # Get current yaw from IMU 
    orientation_q = msg.orientation
    quaternion = [orientation_q.x ,orientation_q.y ,orientation_q.z ,orientation_q.w]
    (_, _, current_yaw) = euler_from_quaternion(quaternion)
    current_yaw = math.atan2(math.sin(current_yaw),math.cos(current_yaw))
    if desired_yaw is None:
        desired_yaw = current_yaw
        return
    # calculate yaw_error 
    yaw_error =  desired_yaw -  current_yaw 
  
    if yaw_error > math.pi:
        yaw_error -= 2 * math.pi
    elif yaw_error < -math.pi:
        yaw_error += 2 * math.pi
    # PID calculations
    yaw_integral += yaw_error
    yaw_derivative = yaw_error - yaw_previous_error
    control_signal = kp * yaw_error +ki * yaw_integral + kd * yaw_derivative
    yaw_previous_error = yaw_error
    cmd = Twist()
    # Move forward
    cmd.linear.x = 0.2 
    # Apply correction    
    cmd.angular.z = control_signal  
    pub.publish(cmd)
    print(f"Yaw: {current_yaw:.3f}, Error: {yaw_error:.3f}, Control: {control_signal:.3f}")


def main():
    rospy.init_node("pid_straight_node")
    rospy.Subscriber("/mpu6050", Imu, IMU_callback)
    rospy.spin()

if __name__ == "__main__":
    try :
       main()
    except rospy.ROSInterruptException:
        pass