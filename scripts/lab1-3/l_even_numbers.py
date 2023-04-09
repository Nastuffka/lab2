#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("listener %s", msg.data)

rospy.init_node('l_eveb_numbers')
rospy.Subscriber('chat_topic_en', String, callback, queue_size=10)
rospy.spin()
