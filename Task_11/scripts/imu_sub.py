#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
def callback(msg):
    rospy.loginfo(msg)
def imu_subscriber():
    rospy.init_node("imu_sensor",anonymous=True)
    rospy.Subscriber("/mpu6050",Imu, callback)
    rospy.spin()

if __name__ =="__main__": 
    try :
       imu_subscriber ()
    except rospy.ROSInterruptException:
        pass

