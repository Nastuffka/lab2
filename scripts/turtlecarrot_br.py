#!/usr/bin/env python3
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

rospy.init_node('turtlecarrot_br.py')
turtlename = rospy.get_param('~turtle_tf_name')

def handle_turtlecarrot_pose(msg):

	global i
	br = tf.TransformBroadcaster()
	# Второй объект публикатора информации TF
	br2 = tf.TransformBroadcaster()
	
	br.sendTransform((msg.x, msg.y, 0), 
			quaternion_from_euler(0, 0, msg.theta), 
			rospy.Time.now(), 
			turtlename, 
			"world")
			
	# Публикация информации TF, координаты морковки постоянно изменяются, причем учитывается поворот черепашки		
	br2.sendTransform((math.cos(i-msg.theta), math.sin(i-msg.theta), 0), 
			quaternion_from_euler(0, 0, 0), 
			rospy.Time.now(), 
			"carrot1", 
			turtlename)
	
	# Чтобы i не переполнилась, обнуляем переменную каждые 360 градусов		
	if i > 2*math.pi: i = 0
	i = i + 0.01

# Создаю глобальную переменную i			
i = 0	
rospy.Subscriber('input_pose', 
		Pose,
		handle_turtlecarrot_pose)

rospy.spin()
