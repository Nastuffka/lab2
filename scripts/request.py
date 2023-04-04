#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32

def numbers():
	
	pub = rospy.Publisher('numbers', Int32MultiArray, queue_size=10, latch=True)
	msg = Int32MultiArray()
	num = input("Введите через пробел числа ").split()
	num_list = list(map(int, num))
	msg.data = num_list
	pub.publish(msg)
	

def callback(result):
	rospy.loginfo(result.data)
	
f = True
rospy.init_node('Request')
numbers()
rate = rospy.Rate(0.4)
rospy.Subscriber('result', Int32, callback, queue_size=10)
rate.sleep()










