#TRATANDO DE IMPLEMENTAR UN WHILE
import rospy
import time
from std_msgs.msg import *
from geometry_msgs.msg import Twist
import random
import datetime

testing = 0

def controlTotal (comando):
	instruction = str(comando.data)
	if(instruction == "0"):
		nav_auto_pub.publish("0")
	elif(instruction == "1"):
		nav_auto_pub.publish("1")

def test (comando2):
	global testing
	instruction2 = str(comando2.data)
	if(instruction2 == "1"):
		testing = "1"
		while(testing == "1"):
			for y in range(20):
				string_test = ""
				for x in range(9):
					random.seed(datetime.datetime.now())
					string_rand = random.uniform(6.1, 8)
					string_test = string_test + str(string_rand) + "|"
				nav_auto_pub_test.publish(string_test)
				time.sleep(0.5)
			for y in range(20):
				string_test = ""
				for x in range(9):
					random.seed(datetime.datetime.now())
					string_rand = random.uniform(4, 7)
					string_test = string_test + str(string_rand) + "|"
				nav_auto_pub_test.publish(string_test)
				time.sleep(0.5)
	elif(instruction2 == "0"):
		testing = "0"

nav_auto_pub = rospy.Publisher('/flag/nav_auto',String,queue_size = 10)
nav_auto_pub_test = rospy.Publisher('/nav/depths',String,queue_size = 10)
def main():
	rospy.init_node("decision_auto")
	sub = rospy.Subscriber('/total_control/nav_auto',String, controlTotal)
	sub_test = rospy.Subscriber('/total_control/test',String, test)
	rate = rospy.Rate(5)
	rospy.spin()
