#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range
def callback(msg):
    rospy.loginfo(msg)
def ultra_left():
    rospy.init_node("ultrasonic_left",anonymous=True)
    rospy.Subscriber("/ultrasonic_left/sonar",Range,callback)
    rospy.spin()
if __name__ =="__main__": 
    try :
       ultra_left ()
    except rospy.ROSInterruptException:
        pass