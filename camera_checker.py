#!/usr/bin/env python3

import rospy
import rostopic
from rosgraph_msgs.msg import Log
from std_msgs.msg import Bool

def log_callback(data):
    pub = rospy.Publisher('is_camera_connected', Bool, queue_size=10)
    if data.level == Log.WARN:
        if "No RealSense devices were found!" in data.msg:
            pub.publish(False)
        else:
            rospy.logwarn("Unexpected warning: {}".format(data.msg))

def main():
    
    rospy.init_node('camera_status_checker', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.Subscriber('/rosout', Log, log_callback)
        rospy.sleep(5)
        
        
    rospy.spin()

if __name__ == '__main__':
    main()
