#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
def Square_motion():
    rospy.init_node("Square_motion")
    rospy.loginfo("Node has been started.")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    status_pub = rospy.Publisher("/turtle_motion_status", String, queue_size=10)
    msg = Twist()

    def Forward():
        msg.linear.x = 1.0
        msg.angular.z = 0.0
        pub.publish(msg)
        status_pub.publish("Forward")
        rospy.sleep(2)

    def Rotating():
        msg.linear.x = 0.0
        msg.angular.z = 1.57
        pub.publish(msg)
        status_pub.publish("Rotating")
        rospy.sleep(2)

    def Stop():
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        pub.publish(msg)
        status_pub.publish("Stop")

    for _ in range(4):
        Forward()
        Rotating()
        Stop()

if __name__== "__main__":
    try:
        Square_motion()
    except rospy.ROSInterruptException:
        pass
