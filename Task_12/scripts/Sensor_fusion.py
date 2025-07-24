#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan
#To publish fused distances as a single message[3 numbers (x, y, z)]
from geometry_msgs.msg import Vector3
# Global variables to store distance readings
front_distance = None
left_distance = None
right_distance = None
lidar_front_distance = None
dis_msg = Vector3()
#publisher to send fused distances
pub = rospy.Publisher("/fused_distances", Vector3, queue_size=10)
def lidar_callback(msg):
    global lidar_front_distance
    front_ranges = msg.ranges[0:10] + msg.ranges[-10:]
    valid_distances = [r for r in front_ranges if r > 0.0 and r < float('inf')]
    if valid_distances:
        lidar_front_distance = min(valid_distances)
def front_callback(msg):
    global front_distance
    if msg.range > 0.0 and msg.range < float('inf') :
        front_distance = msg.range
def left_callback(msg):
    global left_distance
    if msg.range > 0.0 and msg.range < float('inf') :
        left_distance = msg.range 
def right_callback(msg):
    global right_distance
    if msg.range > 0.0 and msg.range < float('inf') :
        right_distance = msg.range             
def Print_distance(event):
    if front_distance is not None and left_distance is not None and right_distance is not None and lidar_front_distance is not None:
        #Fuse front Lidar and ultrasonic 
        fused_front = min(front_distance, lidar_front_distance)
        rospy.loginfo(f"Front:{fused_front:.2f}m | Left:{left_distance:.2f}m | Right:{right_distance:.2f}m")
        dis_msg.x = fused_front
        dis_msg.y = left_distance
        dis_msg.z = right_distance
        pub.publish(dis_msg)

def Fuse():        
    rospy.init_node("Sensor_fusion", anonymous=True)
    rospy.Subscriber("/ultrasonic_front/sonar",Range,front_callback) 
    rospy.Subscriber("/ultrasonic_left/sonar",Range,left_callback)    
    rospy.Subscriber("/ultrasonic_right/sonar",Range,right_callback)    
    rospy.Subscriber("/lidar_sensor_2D",LaserScan,lidar_callback) 
    #Set a timer to print distances every 0.5 seconds
    rospy.Timer(rospy.Duration(0.5),Print_distance)
    rospy.spin()
if __name__ =="__main__": 
    try :
        Fuse()
    except rospy.ROSInterruptException:
        pass    

