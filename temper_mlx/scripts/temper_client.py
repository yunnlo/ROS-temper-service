#! /usr/bin/env python3

import sys
import rospy
from beginner_tutorials.srv import *

def temper_client():
    rospy.wait_for_service('temper')
    try:
        temper = rospy.ServiceProxy('temper',Temper)
        resp1 = temper()
        return resp1.temp
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

if __name__ == "__main__":

       print (temper_client())

