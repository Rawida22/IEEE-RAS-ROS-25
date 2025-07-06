#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
def callback_Twist(msg):
    rospy.loginfo("received status %s",msg.data)
def callback_Helllo(data):
    rospy.loginfo("I heard %s",data.data)
def multi_sub():
    rospy.init_node("multi_subscriber",anonymous=True)
    rospy.Subscriber("/turtle_motion_status",String,callback_Twist)
    rospy.Subscriber("chatter",String,callback_Helllo)
    rospy.spin()


if __name__ =="__main__": 
    try :
        multi_sub ()
    except rospy.ROSInterruptException:
        pass
