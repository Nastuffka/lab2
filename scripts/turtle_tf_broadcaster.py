#!/usr/bin/env python3
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

rospy.init_node('turtle_tf_broadcaster.py')
turtlename = rospy.get_param('~turtle_tf_name')

def handle_turtle_pose(msg):

	br = tf.TransformBroadcaster()
	
	br.sendTransform((msg.x, msg.y, 0), 
			quaternion_from_euler(0, 0, msg.theta), 
			rospy.Time.now(), 
			turtlename, 
			"world")
			
			
rospy.Subscriber('input_pose', 
		Pose,
		handle_turtle_pose)

rospy.spin()
