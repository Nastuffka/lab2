#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32

def callback(msg_in):

	pub = rospy.Publisher('result', Int32, queue_size=10, latch=True)
	msg_out = Int32()
	msg_out.data = sum(list(msg_in.data))
	rospy.loginfo(msg_out.data)
	pub.publish(msg_out)
	

rospy.init_node('Summing')

rospy.Subscriber('poly', Int32MultiArray, callback, queue_size=10)

rospy.spin()


