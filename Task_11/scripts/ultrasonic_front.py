#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range
def callback(msg):
    rospy.loginfo(msg)
def ultra_front():
    rospy.init_node("ultrasonic_front",anonymous=True)
    rospy.Subscriber("/ultrasonic_front/sonar",Range,callback)
    rospy.spin()
if __name__ =="__main__": 
    try :
       ultra_front ()
    except rospy.ROSInterruptException:
        pass