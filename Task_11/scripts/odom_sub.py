#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
def callback(msg):
 rospy.loginfo(msg)
def odom_subcriber():
 rospy.init_node("odom_subscriber",anonymous=True)
 rospy.Subscriber("/odom",Odometry,callback)
 rospy.spin()
if __name__ =="__main__": 
    try :
       odom_subcriber ()
    except rospy.ROSInterruptException:
        pass


