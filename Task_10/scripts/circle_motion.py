#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
def Circle_motion():
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rospy.init_node("Circle_motion")
    rospy.loginfo("Node has been started.")
    status_pub = rospy.Publisher("/turtle_motion_status", String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        pub.publish(msg)
        status_pub.publish("rotating")
        rate.sleep()

if __name__ =="__main__": 
    try :
        Circle_motion()
    except rospy.ROSInterruptException:
        pass