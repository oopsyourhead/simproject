############################################################################################################################################################################
#   Developer           Date            Version             Comment
#   Sean Tatarka        03/31/2020      0001                Create aircraft object with different aspects
#	Sean Tatarka		04/03/2020		0002				Protect heading on init and change_heading to -359 to 359 degrees.
#   Sean Tatarka        04/06/2020      0006                Change trig protection to use -180 to 180 for headings
#
#
#
#
#
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

		while heading > 180 or heading < -180:
			if heading > 180:
				heading -= 360
			elif heading < -180:
				heading += 360

			f2 = open('log.txt', 'w')
			print(daytime.strftime("%H:%M:%S.%f:"), name, "heading was bigger than 360 and has been changed to: ", heading, file = f2)
			f2.close()

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

		while new_heading > 180 or new_heading < -180:
			if new_heading > 180:
				new_heading -= 360
			elif new_heading < -180:
				new_heading += 360

			f2 = open('log.txt', 'a')
			print(daytime.strftime("%H:%M:%S.%f:"), name, "heading was bigger than 360 and has been changed to: ", new_heading, file = f2)
			f2.close()

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