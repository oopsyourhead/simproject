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

	def change_ownship_location(self, new_location, name):
		daytime = datetime.datetime.now()
		file_name = 'log.txt'

		if self.location != new_location:
		    self.location = new_location

		    if os.path.getsize(file_name) == 0:
		        f2 = open('log.txt', 'w')
		        print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Location Changed To", new_location, file = f2)
		    else:
		        f2 = open('log.txt', 'a')
		        print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Location Changed To", new_location, file = f2)

		    f2.close()

	def change_aircraft_speed(self, new_speed, name):
		daytime = datetime.datetime.now()
		file_name = 'log.txt'

		if self.speed != new_speed:
			self.speed = new_speed

			if os.path.getsize(file_name) == 0:
				f2 = open('log.txt', 'w')
				print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Speed Changed To", new_speed, file = f2)
			else:
				f2 = open('log.txt', 'a')
				print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Speed Changed To", new_speed, file = f2) 

			f2.close()

	def change_aircraft_heading(self, new_heading, name):
		daytime = datetime.datetime.now()
		file_name = 'log.txt'

		if self.heading != new_heading:
			self.heading = new_heading

			if os.path.getsize(file_name) == 0:
				f2 = open('log.txt', 'w')
				print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Heading Changed To", new_heading, file = f2)
			else:
				f2 = open('log.txt', 'a')
				print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Heading Changed To", new_heading, file = f2) 

			f2.close()

	def change_aircraft_altitude(self, new_altitude, name):
		daytime = datetime.datetime.now()
		file_name = 'log.txt'

		if self.altitude != new_altitude:
			self.altitude = new_altitude

			if os.path.getsize(file_name) == 0:
				f2 = open('log.txt', 'w')
				print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Altitude Changed To", new_altitude, file = f2)
			else:
				f2 = open('log.txt', 'a')
				print(daytime.strftime("%H:%M:%S.%f:"), name, "Aircraft Altitude Changed To", new_altitude, file = f2) 

			f2.close()