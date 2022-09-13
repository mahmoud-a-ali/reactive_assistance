  #!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import os
import numpy as np
from time import time
from datetime import datetime



alg    = rospy.get_param("/alg")
print("alg: ", alg)
timestr = datetime.now() 
dir = "/home/hjardali/Repos/NAV_ws/src/data/" + alg 

itr_folder = dir  + "/trial"+ str(timestr)
if not os.path.exists(itr_folder):
    os.mkdir(itr_folder)
odom_file  = itr_folder +"/odom.txt"
scan_file = itr_folder +"/scan.txt"


def scan_callback(data):

    file = open(scan_file, "a")
    np.savetxt( file, np.array( [data.header.stamp.to_sec(), min(data.ranges) ], dtype='float64').reshape(-1,2) , delimiter=" ", fmt='%1.4f')
    file.close()
    


def odom_callback(data):

    file = open(odom_file, "a")
    np.savetxt( file, np.array( [data.header.stamp.to_sec(), data.twist.twist.linear.x, data.twist.twist.angular.z ], dtype='float64').reshape(-1,3) , delimiter=" ", fmt='%1.4f')
    file.close()
    
    
def main():


    rospy.init_node('save_data', anonymous=True)
    

    
    

    rospy.Subscriber("ground_truth/state", Odometry, odom_callback)
    rospy.Subscriber("/scan", LaserScan, scan_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()
    