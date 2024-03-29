####################################################################################################################################################################################
#   Developer           Date            Version             Comment
#   Sean Tatarka        03/23/2020      0001                Initial commit, create target object, change target aspects using functions
#   Sean Tatarka        03/27/2020      0002                Started logging stuff, will log when targets are created, added target name and target heading characteristics
#   Sean Tatarka        03/30/2020      0003                Finished logging events when creating targets, and changing target characteristics, includes timetags will only change
#                                                           attribute and log it if the new value is different than the old value
#   Sean Tatarka        04/02/2020      0004                Added counter that tracks number of target objects created, this is to facilitate looping in sim.py
#   Sean Tatarka        04/03/2020      0005                Changed target_list to be created from object from targets.py, sim.py assigns the list of targets after they're created
#                                                           Added a limit for target headings to be between -360 and 360 degrees, may change this to -180 to 180 soon
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
#####################################################################################################################################################################################

import os, datetime

class Target:
    number_of_targets = 0
    target_list = []

    def __init__(self, name, location, speed, heading, power):
        old_heading = heading
        daytime = datetime.datetime.now()
        f2 = open('log.txt', 'a')
        print(daytime.strftime("%H:%M:%S.%f:"), name, "has been created", file = f2)
        #file_name = 'log.txt'
        Target.number_of_targets += 1

        while heading > 180 or heading < -180:
            if heading > 180:
                heading -= 360
            elif heading < -180:
                heading += 360

        if old_heading != heading:
            print(daytime.strftime("%H:%M:%S.%f:"), name, "heading was", old_heading, "and has been changed to: ", heading, file = f2)

        self.location = location                            #right now location is 1 dimension
        self.speed = speed
        self.heading = heading                              #heading is in degrees
        self.power = power
        self.name = name
                                                                                                                                        #if os.path.getsize(file_name) == 0:
                                                                                                                                        #    f2 = open('log.txt', 'w')                                                                                                
                                                                                                                                        #    print(daytime.strftime("%H:%M:%S.%f:"), name, "has been created", file = f2)
        f2.close()                                                                                                                      #else:
        Target.target_list.append(self)                                                                                                 #    f2 = open('log.txt', 'a')
                                                                                                                                        #    print(daytime.strftime("%H:%M:%S.%f:"), name, "has been created", file = f2)
                                                                                                                                        #    print("target else case being run here:")

    def change_location(self, new_location, target_list, name):
        daytime = datetime.datetime.now()
        file_name = 'log.txt'

        if self.location != new_location:
            self.location = new_location
            target_locations = [o.location for o in target_list]

            if os.path.getsize(file_name) == 0:
                f2 = open('log.txt', 'w')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Location Changed To", new_location, file = f2)
            else:
                f2 = open('log.txt', 'a')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Location Changed To", new_location, file = f2)

            f2.close()        
        else:
            target_locations = [o.location for o in target_list]

        return target_locations

    def change_power(self, new_power, target_list, name):
        daytime = datetime.datetime.now()
        file_name = 'log.txt'

        if self.power != new_power:
            self.power = new_power
            target_powers = [o.power for o in target_list]

            if os.path.getsize(file_name) == 0:
                f2 = open('log.txt', 'w')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Power Changed To", new_power, file = f2)
            else:
                f2 = open('log.txt', 'a')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Power Changed To", new_power, file = f2)    

            f2.close()   
        else:
            target_powers = [o.power for o in target_list]      

        return target_powers

    def change_speed(self, new_speed, target_list, name):
        daytime = datetime.datetime.now()
        file_name = 'log.txt'

        if self.speed != new_speed:
            self.speed = new_speed
            target_speeds = [o.speed for o in target_list]

            if os.path.getsize(file_name) == 0:
                f2 = open('log.txt', 'w')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Speed Changed To", new_speed, file = f2)
            else:
                f2 = open('log.txt', 'a')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Speed Changed To", new_speed, file = f2) 

            f2.close()
        else:
            target_speeds = [o.speed for o in target_list]

        return target_speeds

    def change_heading(self, new_heading, target_list, name):
        daytime = datetime.datetime.now()
        file_name = 'log.txt'
        print_heading = new_heading

        while new_heading > 180 or new_heading < -180:
            if new_heading > 180:
                new_heading -= 360
            elif new_heading < -180:
                new_heading += 360

        f2 = open('log.txt', 'a')
        print(daytime.strftime("%H:%M:%S.%f:"), name, "heading was", print_heading, "and has been changed to: ", new_heading, file = f2)
        f2.close()

        if self.heading != new_heading:
            self.heading = new_heading
            target_headings = [o.heading for o in target_list]

            if os.path.getsize(file_name) == 0:
                f2 = open('log.txt', 'w')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Heading Changed To", new_heading, file = f2)
            else:
                f2 = open('log.txt', 'a')
                print(daytime.strftime("%H:%M:%S.%f:"), name, "Heading Changed To", new_heading, file = f2) 

            f2.close()
        else:
            target_headings = [o.heading for o in target_list]

        return target_headings

