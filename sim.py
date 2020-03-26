############################################################################################################################################################################
#   Developer           Date            Version             Comment
#   Sean Tatarka        03/23/2020      0001                Initial commit, 1 dimension scan, map center, scan speed, power threshold implemented
#   Sean Tatarka        03/25/2020      0002                Added the ability to scan multiple "bars", only 1 dimension so it's just left-right and right-left each time
#
#
#
#
#
#
#############################################################################################################################################################################

#SETUP
from targets import Target


f = open('output.txt', 'w')


###########################CC INPUTS################################
#########################Interface########################
##########################Modes######################
NORMAL_SCAN = 0
HIGH_PRF_AIR_TO_AIR_SEARCH = 1
MED_PRF_AIR_TO_AIR_SEARCH = 2
INTLV_AIR_TO_AIR_SEARCH = 3
STT = 4
TWS = 5


######################Mapping Controls#########################
mapcenter = 11
scanwidth = 10
scanspeed = 1
scan_direction = 1         #1 = left to right, 2 = right to left
number_of_scans = 3
elevation_angle = 0


######################Radar execution controls#####################
radar_mode = NORMAL_SCAN
mtr_setting = 20
detection_threshold = 50

##############################CC OUTPUTS##################################
current_scan_number = 1




#######################helper functions and classes###############################

            

######################Scenario###############################################
target_1 = Target(1, 0, 100)
target_2 = Target(5, 50, 100)
target_3 = Target(9, 0, 100)

target_list = [target_1, target_2, target_3]

target_locations = [o.location for o in target_list]
target_powers = [o.power for o in target_list]
target_speeds = [o.speed for o in target_list]

#target_locations = []
#target_locations.append(target_1.location)
#target_locations.append(target_2.location)
#target_locations.append(target_3.location)

beam_width = 5.0
half_power_beam_width = beam_width / 2


##################SCAN EXECUTION#############################
while current_scan_number <= number_of_scans :
    print("the current bar # is: ",current_scan_number)
    print("the current bar # is: ",current_scan_number, file = f)

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


    if scan_direction != 1:
        scan_swath.reverse()

    print('scan_boundry_left: ', scan_boundry_left)
    print('scan_boundry_left: ', scan_boundry_left, file = f)
    print('scan_boundry_right: ', scan_boundry_right)
    print('scan_boundry_right: ', scan_boundry_right, file = f)
    print('')

    i = 0

    while ((i < len(scan_swath)) & (i >= 0)):
        print(scan_swath[i], "\t", end ="", flush=True)
        print(scan_swath[i], "\t", end ="", flush=True, file = f)
        i += scanspeed

    print("")
    print("", file = f)

    a = 0

    while ((current_scan_location <= scan_boundry_right) and (current_scan_location >= scan_boundry_left)):
        if (current_scan_location in target_locations):
            while (a < len(target_powers)): 
                if target_locations[a] == current_scan_location and target_powers[a] >= detection_threshold and target_speeds[a] >= mtr_setting:
                    print('#',"\t", end="", flush=True)
                    print('#',"\t", end="", flush=True, file = f)
                    a += 1
                    break
                elif target_locations[a] == current_scan_location and target_powers[a] >= detection_threshold and target_speeds[a] < mtr_setting:
                    print('=', "\t", end="", flush=True)
                    print('=', "\t", end="", flush=True, file = f)
                    a += 1
                    break                     
                elif target_locations[a] == current_scan_location and (target_powers[a] < detection_threshold or target_speeds[a] < mtr_setting):
                    print('=', "\t", end="", flush=True)
                    print('=', "\t", end="", flush=True, file = f)
                    a += 1
                    break 
                else:
                    a += 1
        else:
            print('=', "\t", end="", flush=True)
            print('=', "\t", end="", flush=True, file = f)

                    
        if scan_direction == 1:
            current_scan_location += scanspeed
            a = 0
        else:
            current_scan_location -= scanspeed
            a = 0


    if scan_direction == 1:
        scan_direction = 2
    else:
        scan_direction = 1

##################OUTPUTS#########################################

    target_location_output = target_locations 
    target_powers_output = target_powers
    target_speeds_output = target_speeds
    current_scan_location_output = current_scan_location
    scanspeed_output = scanspeed
    current_scan_number_output = current_scan_number
    radar_mode_output = radar_mode

################PRINTING##################################################

    print("")
    print("", file = f)
    #print("len(range)-1", len(range)-1)
    #print("i = ", i)
    #print("i-scanspeed=",i-scanspeed)
    #print("(i-scanspeed)%scanspeed = ", (i-scanspeed)%scanspeed)
    print("The current Radar Mode is: ", radar_mode_output)
    print("The current Radar Mode is: ", radar_mode_output, file = f)
    print("Target Locations Are: ", target_location_output)
    print("Target Locations Are: ", target_location_output, file = f)
    print("Target Powers Are: ", target_powers_output)
    print("Target Powers Are: ", target_powers_output, file = f)
    print("Target Speeds are: ", target_speeds_output)
    print("Target Speeds are: ", target_speeds_output, file = f)
    print("The scan speed was: ", scanspeed_output)
    print("The scan speed was: ", scanspeed_output, file = f)
    print("", file = f)
    print("")


#################UPDATE TARGETS FOR NEXT SCAN################################

    target_powers = target_1.change_power(10, target_list)
    target_powers = target_2.change_power(50, target_list)
    target_locations = target_2.change_location(7, target_list)
    target_speeds = target_2.change_speed(75, target_list)

    current_scan_number += 1
#print(target_powers[0])
#print(target_powers[1])
#print(target_powers[2])

f.close()

#power check implemented and working
#next  maybe make scenario control it's own file then import
#maybe next implement speed/mtr filter (started 3/27/20202)
#add log that records when target characteristics are changed

#in the future implement beam structure, target range, target elevation, target xyz, add in elevation angles, bars, different modes
