#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
def callback(msg):
    valid_distances = [r for r in msg.ranges if r > 0.0 and r < float('inf')]
    if valid_distances:
        closest_object = min (valid_distances)
        rospy.loginfo(f"distance to the closest object: {closest_object:.2f} m")
    else:
        rospy.loginfo("there is no objects")

def Laser_scan ():
    rospy.init_node("LaserScane",anonymous=True)
    rospy.Subscriber("/lidar_sensor_2D",LaserScan,callback)
    rospy.loginfo("Node has been started.")
    rospy.spin()

if __name__ =="__main__": 
    try :
        Laser_scan()
    except rospy.ROSInterruptException:
        pass    