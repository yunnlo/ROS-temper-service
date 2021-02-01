#! /usr/bin/env python

from __future__ import print_function

import sys
import rospy
import math
from temper_mlx.srv import *

def temper_client():
    rospy.wait_for_service('temper')
    try:
        temper = rospy.ServiceProxy('temper',Temper)
        resp1 = temper()
        return resp1.temp
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

if __name__ == "__main__":
       a=math.floor(10*temper_client())/10
       print (a)

