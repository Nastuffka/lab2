#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('t_even_numbers')
pub = rospy.Publisher('chat_topic_en', String, queue_size=10)
pub2 = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)


def start_talker():
	i = 0;
	msg = String()
	msg2 = String()
	while not rospy.is_shutdown():
	
		en = 0
		while en < 101:
		
			msg.data = "%s" % en
			rospy.loginfo("talker %s", msg.data)
			pub.publish(msg)
			en = en + 2
			rate.sleep()
			
		i = i + 1
		msg2.data = "%s" % i
		pub2.publish(msg2)

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
