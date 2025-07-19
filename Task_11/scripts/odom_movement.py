#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
initial_x = None
initial_y = None
stopped = False
move = Twist()
def odom_callback(msg):
    # modify the variables defined outside the function
    global initial_x, initial_y, move, stopped
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    # save initial position
    if initial_x is None and initial_y is None:
        initial_x = x 
        initial_y = y
        rospy.loginfo("initial position saved")
        return
    # calculate the distance from the starting point 
    distance = math.sqrt((x - initial_x)**2 +(y - initial_y)**2)
    rospy.loginfo("Distance = %.2f",distance)
    #to move or stop
    if distance < 0.3 :
        move.linear.x = 0.1
        pub.publish(move)
    else:
        move.linear.x = 0.0 
        pub.publish(move)
        stopped = True
        return
rospy.init_node("move_forward",anonymous=True)
rospy.loginfo("Node has been started.")
pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)    
rospy.Subscriber("/odom",Odometry,odom_callback)
rospy.spin()