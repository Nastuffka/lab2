#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

def callback(msg_in):
	pub = rospy.Publisher('poly', Int32MultiArray, queue_size=10, latch=True)
	msg_out = Int32MultiArray()
	num_list = list(msg_in.data)
	i = len(num_list)
	j = 0
	
	for x in num_list:
		num_list[j] = x**(i-j)
		j += 1
		
	msg_out.data = num_list
	rospy.loginfo(num_list)
	pub.publish(msg_out)

rospy.init_node('Polynominal')
rospy.Subscriber('numbers', Int32MultiArray, callback, queue_size=10)
rospy.spin()


