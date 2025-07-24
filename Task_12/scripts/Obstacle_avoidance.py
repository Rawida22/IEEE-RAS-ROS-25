#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist
# Global variables to store distance readings
fused_front = None
left_distance = None
right_distance = None
move = Twist()
pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)             
def fused_callback(msg):
    global fused_front, left_distance, right_distance
    fused_front = msg.x
    left_distance = msg.y
    right_distance = msg.z
    if fused_front is not None and left_distance is not None and right_distance is not None :
        if fused_front >= 0.5 :
            move.linear.x = 0.8 
            move.angular.z = 0.0
            rospy.loginfo("Moving Forward")
        else:
            move.linear.x = 0.0
            if right_distance > left_distance:
                move.linear.x = 0.0 
                move.angular.z = -0.5
                rospy.loginfo("Turning Right")
            else:
                move.linear.x = 0.0 
                move.angular.z = 0.5
                rospy.loginfo("Turning Left")
    pub.publish(move)
def Sub():        
    rospy.init_node("obstacle_avoidance", anonymous=True)
    #subscriber to the fused distances
    rospy.Subscriber("/fused_distances", Vector3, fused_callback)
    rospy.spin()
if __name__ =="__main__": 
    try :
        Sub()
    except rospy.ROSInterruptException:
        pass    

