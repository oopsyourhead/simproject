#SETUP
NORMAL_SCAN = 0
HIGH_PRF_AIR_TO_AIR_SEARCH = 1
MED_PRF_AIR_TO_AIR_SEARCH = 2
INTLV_AIR_TO_AIR_SEARCH = 3
STT = 4
TWS = 5
DETECTION_THRESHOLD = 50



#helper functions and classes
class Target:
    def __init__(self, location, speed, power):
        self.location = location
        self.speed = speed
        self.power = power

    def change_location(self, new_location):
        self.location = new_location
        target_locations = [o.location for o in target_list]

    def change_power(self, new_power):
        self.power = new_power
        target_power = [o.power for o in target_list]
        return target_power

    def change_speed(self, new_speed):
        self.speed = new_speed
        target_speeds = [o.speed for o in target_list]
        return target_speeds

#def check_power(target_power, power_threshold):
#    x = 0 
#    while x < (len(target_power)-1):
#        if power_threshold >= target_power[x]:
#            return False
#       else:
#           return True
#   x += 1
            

#Scenario
target_1 = Target(1, 0, 100)
target_2 = Target(-3, 0, 100)
target_3 = Target(9, 0, 100)

target_list = [target_1, target_2, target_3]

#target_1.change_location(-1)
#target_2.change_power(75)

target_locations = [o.location for o in target_list]
target_power = [o.power for o in target_list]
target_speeds = [o.speed for o in target_list]

#target_locations = []
#target_locations.append(target_1.location)
#target_locations.append(target_2.location)
#target_locations.append(target_3.location)

beam_width = 5.0
half_power_beam_width = beam_width / 2


#Interface
############################################################################
#INPUTS

mapcenter = 11
scanwidth = 16
scanspeed = 2
scan_direction = 2         #1 = left to right, 2 = right to left
number_of_scans = 10
elevation_angle = 0
radar_mode = 0
mtr_setting = 0


if (scan_direction == 1):
    starting_scan_location = mapcenter - scanwidth
    current_scan_location = starting_scan_location
    scan_boundry_left = mapcenter - scanwidth
    scan_boundry_right = mapcenter + scanwidth

else:
    starting_scan_location = mapcenter + scanwidth
    current_scan_location = starting_scan_location
    scan_boundry_left = mapcenter - scanwidth
    scan_boundry_right = mapcenter + scanwidth
    
scan_swath = list(range(scan_boundry_left, scan_boundry_right + 1))
target_power = target_2.change_power(10)
target_power = target_3.change_power(50)

if scan_direction != 1:
    scan_swath.reverse()

print('scan_boundry_left: ', scan_boundry_left)
print('scan_boundry_right: ', scan_boundry_right)
print('')

i = 0

while ((i < len(scan_swath)) & (i >= 0)):
        print(scan_swath[i], "\t", end ="", flush=True)
        i += scanspeed

print("")

a = 0

while ((current_scan_location <= scan_boundry_right) and (current_scan_location >= scan_boundry_left)):
    if (current_scan_location in target_locations):
        while (a < len(target_power)): 
            if target_locations[a] == current_scan_location and target_power[a] >= DETECTION_THRESHOLD:
                print('#',"\t", end="", flush=True)
                a += 1
                break
            elif target_locations[a] == current_scan_location and target_power[a] < DETECTION_THRESHOLD:
                print('=', "\t", end="", flush=True)
                a += 1
                break
            else:
                a += 1
    else:
        print('=', "\t", end="", flush=True)

                
    if scan_direction == 1:
        current_scan_location += scanspeed
        a = 0
    else:
        current_scan_location -= scanspeed
        a = 0

###############OUTPUTS#########################################

target_location_output = target_locations 
target_power_output = target_power
current_scan_location_output = current_scan_location
scanspeed_output = scanspeed

###############################################################

print("")
#print("len(range)-1", len(range)-1)
#print("i = ", i)
#print("i-scanspeed=",i-scanspeed)
#print("(i-scanspeed)%scanspeed = ", (i-scanspeed)%scanspeed)
print("Target Location Is: ", target_location_output)
print("Target Powers Are: ", target_power_output)
print("The scan speed was: ", scanspeed_output)
#print(target_power[0])
#print(target_power[1])
#print(target_power[2])

#power check implemented and working
#maybe next implement speed/mtr filter, scan multiple times in a row

#in the future implement beam structure, target range, target elevation, target xyz, add in elevation angles, bars, different modes