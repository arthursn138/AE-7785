#! /usr/bin/env python3

# Arthur Scaquetti do Nascimento and Smit Sparsh
# AE/ECE 7785 - Spring 2022
# Lab 5

import math
import rospy
import numpy as np
import sys
from geometry_msgs.msg import Twist, Point
# from nav_msgs.msg import Odometry

'''Testing WP reading'''
with open('global_waypoints.txt') as waypoints:
    for lines in waypoints:
        wp = lines.split(', ')
        print(wp[0])
        print(wp[1])
        print(wp[2])
        print(wp[3])
        print(wp[4])
        print(wp[5])
        print(wp[6])

# TODO: Set each collumn with their corresponding pose.position.x = wp[0], ... pose.orientation.w = wp[6]
# publish pose
# wait til it gets there: compare with odom???
# when treshold met, display, do a 360 or smt, wait for 2s
# read next line and go to that wp


'''Structure to run in ROS'''
# class Position:
#     """X direction is longitudinal,
#        Y is lateral and
#        Z is Perpendicular"""

#     def __init__(self, x=0.0, y=0.0, z=0.0):
#         self.x = x
#         self.y = y
#         self.z = z


# def main(args):
#     """Initializes and cleanup ros node"""
#     print("Initializing the go_to_object Node")
#     rospy.init_node('go_to_object', anonymous=True)
#     ic = Controller()
#     try:
#         rospy.spin()
#     except KeyboardInterrupt:
#         pass


# if __name__ == '__main__':
#     main(sys.argv)