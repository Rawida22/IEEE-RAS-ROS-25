#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range
def callback(msg):
    rospy.loginfo(msg)
def ultra_right():
    rospy.init_node("ultrasonic_right",anonymous=True)
    rospy.Subscriber("/ultrasonic_right/sonar",Range,callback)
    rospy.spin()
if __name__ =="__main__": 
    try :
       ultra_right ()
    except rospy.ROSInterruptException:
        pass


