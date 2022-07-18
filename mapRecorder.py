import rospy
import sys
from nav_msgs.msg import Odometry

class ScriptToMap(object):

    def __init__(self, fileName="data"):
        self.x = self.y = 0
        self.distance = 0.01 #Update the map every 20 mm
        self.fileName = fileName + ".txt"
        self.sub = rospy.Subscriber("/odom_reframer/odom_chassis", Odometry, self.handle_pose)

    def handle_pose(self,msg):
        with open(self.fileName,'a') as f:
            x = msg.pose.pose.position.x
            y = msg.pose.pose.position.y
            dist = ((x-self.x)**2+(y-self.y)**2)**0.5
            if dist >= self.distance:
                self.x = x
                self.y = y
                newLine = str(x)+", "+str(y)+'\n'
                f.write(newLine)
            print("Current position: "+str(x)+", "+ str(y))
            


def usage():
    print("USAGE: python mapRecorder.py <mapOutputFile>")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    else:
        rospy.init_node("mapRecorder", anonymous = True)
        f = open(sys.argv[1]+".txt",'w')
        f.close()
        mapper = ScriptToMap(sys.argv[1])
        rospy.spin()
