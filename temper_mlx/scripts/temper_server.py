#!/usr/bin/env python

from __future__ import print_function

import serial
import threading
import time
import random
import rospy
from std_msgs.msg import Float32MultiArray
from temper_mlx.srv import *

class MLXTemper:
    def __init__(self):
        self.MLX_port = '/dev/ttyUSB0'       
        self.arduino = serial.Serial(self.MLX_port, 9600, timeout=1)
        if not self.arduino.is_open:
            self.arduino.open()

        self.MLX_t = threading.Thread(target=self.get_data)
        self.MLX_t.start()
        time.sleep(0.5)
    
    def get_data(self):
        # while True:
        while self.arduino.is_open:

            try:
                raw_data = self.arduino.readline()
                temp = [float(val) for val in raw_data.split()]
            except Exception:
                print('oops')            
            return temp       
        
def handle_temper(req):
    print("asking temper")
    t=MLXTemper()
    tem = t.get_data()
    a=tem[0]
    print (a)
    return TemperResponse(a)


def temper_server():
    rospy.init_node('temper_server')
    s = rospy.Service('temper', Temper, handle_temper)
    print("Ready to output temper.")
    rospy.spin()

if __name__ == "__main__":
    temper_server()
