############################################################################################################################################################################
#   Developer           Date            Version             Comment
#   Sean Tatarka        03/31/2020      0001                Create aircraft object with different aspects
#
#
#
#
#
#############################################################################################################################################################################

import os, datetime

class Aircraft:
	def __init__(self, name, heading, speed, altitude, ownship_location):
		daytime = datetime.datetime.now()
		file_name = 'log.txt'

		if os.path.getsize(file_name) == 0:
			f2 = open('log.txt', 'w')
			print(daytime.strftime("%H:%M:%S.%f:"), name, "has been created", file = f2)
		else:
			f2 = open('log.txt', 'a')
			print(daytime.strftime("%H:%M:%S.%f:"), name, "has been created", file = f2)

		f2.close()

		self.location = ownship_location
		self.speed = speed
		self.heading = heading
		self.name = name
		self.altitude = altitude