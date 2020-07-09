#! /usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group1 = moveit_commander.MoveGroupCommander("digging_arm")
group2 = moveit_commander.MoveGroupCommander("seeding_arm")
group3 = moveit_commander.MoveGroupCommander("clamp")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

group1_variable_values = group1.get_current_joint_values()
group2_variable_values = group2.get_current_joint_values()
group3_variable_values = group3.get_current_joint_values()

group1_variable_values[0] = 0.8478
group1_variable_values[1] = 0.1567
group1_variable_values[2] = 0.0000
group1.set_joint_value_target(group1_variable_values)

plan2 = group1.plan()
group1.go(wait=True)

group2_variable_values[0] = (-3.1416)
group2_variable_values[1] = 0.0420
group2_variable_values[2] = 0
group2.set_joint_value_target(group2_variable_values)

plan2 = group2.plan()
group2.go(wait=True)

group3_variable_values[0] = (-0.6)
group3_variable_values[1] = (-0.6)
group3.set_joint_value_target(group3_variable_values)

plan2 = group3.plan()
group3.go(wait=True)

group2_variable_values[0] = (-3.1416)
group2_variable_values[1] = 0.0420
group2_variable_values[2] = 0.180
group2.set_joint_value_target(group2_variable_values)

plan2 = group2.plan()
group2.go(wait=True)

group3_variable_values[0] = 0.2
group3_variable_values[1] = 0.2
group3.set_joint_value_target(group3_variable_values)

plan2 = group3.plan()
group3.go(wait=True)

group1_variable_values[0] = 0.8478
group1_variable_values[1] = 0.1567
group1_variable_values[2] = 0.2000
group1.set_joint_value_target(group1_variable_values)

plan2 = group1.plan()
group1.go(wait=True)
group1.go(wait=True)
group1.go(wait=True)
group1.go(wait=True)
group1.go(wait=True)
group1.go(wait=True)
group1.go(wait=True)

group2_variable_values[0] = (-3.1416)
group2_variable_values[1] = 0.0420
group2_variable_values[2] = 0.000
group2.set_joint_value_target(group2_variable_values)

plan2 = group2.plan()
group2.go(wait=True)

group1_variable_values[0] = 0.8478
group1_variable_values[1] = 0.1567
group1_variable_values[2] = 0.0000
group1.set_joint_value_target(group1_variable_values)

plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[0] = 0.0000
group1_variable_values[1] = 0.0000
group1_variable_values[2] = 0.0000
group1.set_joint_value_target(group1_variable_values)

plan2 = group1.plan()
group1.go(wait=True)

group2_variable_values[0] = (-0.8478)
group2_variable_values[1] = 0.1567
group2_variable_values[2] = 0.000
group2.set_joint_value_target(group2_variable_values)

plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[0] = (-0.8478)
group2_variable_values[1] = 0.1567
group2_variable_values[2] = 0.2100
group2.set_joint_value_target(group2_variable_values)

plan2 = group2.plan()
group2.go(wait=True)

group3_variable_values[0] = (-0.6000)
group3_variable_values[1] = (-0.6000)
group3.set_joint_value_target(group3_variable_values)

plan2 = group3.plan()
group3.go(wait=True)

group2_variable_values[0] = 0.0000
group2_variable_values[1] = 0.0000
group2_variable_values[2] = 0.0000
group2.set_joint_value_target(group2_variable_values)

plan2 = group2.plan()
group2.go(wait=True)

group3_variable_values[0] = 0
group3_variable_values[1] = 0
group3.set_joint_value_target(group3_variable_values)

plan2 = group3.plan()
group3.go(wait=True)

moveit_commander.roscpp_shutdown()
