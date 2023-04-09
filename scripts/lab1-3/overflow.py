#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg2):
    rospy.loginfo("Прошло циклов: %s", msg2.data)

rospy.init_node('overflow')
rospy.Subscriber('overflow_topic', String, callback, queue_size=10)
rospy.spin()
