#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
def move():
     rospy.init_node("move_forward",anonymous=True)
     rospy.sleep(1)
     rospy.loginfo("Node has been started.")
     pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
     msg = Twist()
     #forward
     #velocity = 0.1 m/s
     msg.linear.x=0.1 
     msg.angular.z=0.0
     distance = 0.3 #per m
     time = distance / msg.linear.x #(3 sec )
     #Save the current time(in ROS system) in seconds  as a starting point
     start_time = rospy.Time.now().to_sec()
     #message every second
     rate = rospy.Rate(1)

     while not rospy.is_shutdown() and rospy.Time.now().to_sec() - start_time < time :
        pub.publish(msg)
        rospy.loginfo("moving")
        #time = distance / velocity (0.3 / 0.1)
        rate.sleep()
     #stop    
     msg.linear.x = 0.0
     pub.publish(msg)
     rospy.loginfo("stopped")


if __name__ =="__main__": 
    try :
        move()
    except rospy.ROSInterruptException:
        pass

