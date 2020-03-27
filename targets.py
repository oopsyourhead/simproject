############################################################################################################################################################################
#   Developer           Date            Version             Comment
#   Sean Tatarka        03/23/2020      0001                Initial commit, create target object, change target aspects using functions
#   Sean Tatarka        03/27/2020      0002                Started logging stuff, will log when targets are created, added target name and target heading characteristics
#   
#
#
#
#
#############################################################################################################################################################################

import os, datetime

class Target:
    def __init__(self, name, location, speed, heading, power):
        daytime = datetime.datetime.now()

        file_name = 'log.txt'
        if os.path.getsize(file_name) == 0:
            f2 = open('log.txt', 'w')
            print(name, "has been created at ", daytime.strftime("%I:%M:%S"), ".", daytime.microsecond, " ", daytime.strftime("%p"), file = f2)
        else:
            f2 = open('log.txt', 'a')
            print(name, "has been created at ", daytime.strftime("%I:%M:%S"), ".", daytime.microsecond, " ", daytime.strftime("%p"), file = f2)

        f2.close()
        self.location = location
        self.speed = speed
        self.heading = heading
        self.power = power
        self.name = name

    def change_location(self, new_location, target_list):
        self.location = new_location
        target_locations = [o.location for o in target_list]
        return target_locations

    def change_power(self, new_power, target_list):
        self.power = new_power
        target_powers = [o.power for o in target_list]
        return target_powers

    def change_speed(self, new_speed, target_list):
        self.speed = new_speed
        target_speeds = [o.speed for o in target_list]
        return target_speeds

    def change_heading(self, new_heading, target_list):
        self.heading = new_heading
        target_headings = [o.heading for o in target_list]
        return target_headings

