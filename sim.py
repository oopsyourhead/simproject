#######################################################################################################################################################################################
#   Developer           Date            Version             Comment
#   Sean Tatarka        03/23/2020      0001                Initial commit, 1 dimension scan, map center, scan speed, power threshold implemented
#   Sean Tatarka        03/25/2020      0002                Added the ability to scan multiple "bars", only 1 dimension so it's just left-right and right-left each time
#   Sean Tatarka        03/27/2020      0003                Added MTR filtering based on target velocity, which takes heading into account. Added initial logging capability
#   Sean Tatarka        03/30/2020      0004                Updated class function calls to include object names to support logging functions
#   Sean Tatarka        03/31/2020      0005                Added Aircraft class objects, incorporated aircraft heading and mode into target detection
#   Sean Tatarka        04/02/2020      0006                Changed function calls to use loops based on number of Target objects created, fixed trig calculations, updated functions
#   Sean Tatarka        04/03/2020      0007                Updated calls to test trig limitations, and implement new list from targets class
#   Sean Tatarka        04/06/2020      0008                Updated target and aircraft class objects to test new trig protection for -180 to 180
#   Sean Tatarka        04/17/2020      0009                Added display.txt output, implemented multibar scans, added arrow indicator for scan direction on display.txt
#
#
#
#
#
#
#
#
#
#######################################################################################################################################################################################

#SETUP
from targets import Target
from aircraft import Aircraft
from math import cos, fabs, radians
import os, datetime

f = open('output.txt', 'w')
f2 = open('log.txt', 'w')
f3 = open('display.txt', 'w')
f2.write("")
f2.close()
f3.write("")
f3.close()
f3 = open('display.txt', 'w')

display_count = 1


###########################CC INPUTS################################
#########################Interface########################
##########################Modes######################
NORMAL_SCAN = 0                     #normal scan is a placeholder mode, doesn't use any of the mode drawbacks, just raw inputs and outputs
HIGH_PRF_AIR_TO_AIR_SEARCH = 1      #High PRF Search cannot detect trailing targets (those tha have the same headed as the aircraft)
MED_PRF_AIR_TO_AIR_SEARCH = 2       #Med PRF search can detect all targets, leading or trailing, but has a lower detection threshold
INTLV_AIR_TO_AIR_SEARCH = 3         #Interleave search mixes Med and High PRF's, so the advantages and drawbacks match up with each scan
STT = 4
TWS = 5


######################Mapping Controls#########################
mapcenter = 11
scanwidth = 10
scanspeed = 1
scan_direction = 1         #1 = left to right, 2 = right to left
number_of_scans = 2
number_of_bars = 4
elevation_angle = 0
azimuth_angle = 0


######################Radar execution controls#####################
radar_mode = HIGH_PRF_AIR_TO_AIR_SEARCH
mtr_setting = 20
detection_threshold = 50

##############################CC OUTPUTS##################################
current_bar_number = 1
current_scan_number = 1




#######################helper functions and classes###############################

def calc_velocities(target_speeds, heading_differences, number_of_targets):  #calculates velocity based on target speed and the heading difference
    n = 0
    target_velocities = []

    while n < number_of_targets:
        target_velocities.append((target_1.speed * cos(radians(heading_differences[n]))))
        n += 1

    return target_velocities

def calc_heading_difference(target_headings, aircraft_heading, number_of_targets):         #calculates heading difference between targets and aircraft
    m = 0
    heading_differences = []

    while m < number_of_targets:
        heading_differences.append((target_headings[m] - aircraft_heading))
        m += 1

    return heading_differences

            

######################Scenario###############################################
target_1 = Target("target_1", 1, 100, 370, 100)                     #(name, location, speed, heading, power)
target_2 = Target("target_2", 5, 100, 900, 100)
target_3 = Target("target_3", 9, 100, 90, 100)
target_4 = Target("target_4", 4, 100, 270, 100)

print("number of targets is: ", Target.number_of_targets)
print("number of targets is: ", Target.number_of_targets, file = f)

aircraft_1 = Aircraft("aircraft_1", 365, 100, 10000, 0)           #(name, heading, speed, altitude, ownship_location)

target_list = Target.target_list
#target_list = [target_1, target_2, target_3, target_4]

#print(target_list, file = f)

target_names = [o.name for o in target_list]
target_locations = [o.location for o in target_list]
target_powers = [o.power for o in target_list]
target_speeds = [o.speed for o in target_list]
target_headings = [o.heading for o in target_list]


beam_width = 5.0
half_power_beam_width = beam_width / 2


##################SCAN EXECUTION#############################
while current_scan_number <= number_of_scans:
    current_bar_number = 1
    print("current scan number: ", current_scan_number, file = f)
    print("current bar number: ", current_bar_number, file = f)
    while current_bar_number <= number_of_bars:
        daytime = datetime.datetime.now()

        print("the current scan # is: ",current_scan_number)
        print("the current scan # is: ",current_scan_number, file = f)

        print("the current bar # is: ",current_bar_number)
        print("the current bar # is: ",current_bar_number, file = f)

        f2 = open('log.txt', 'a')
        print(daytime.strftime("%H:%M:%S.%f:"), "the current bar # is: ", current_scan_number, file = f2)
        f2.close()
        
        heading_differences = calc_heading_difference(target_headings, aircraft_1.heading, Target.number_of_targets)
        target_velocities = calc_velocities(target_speeds, heading_differences, Target.number_of_targets)
        targets_detected = []

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
        
        if display_count == 1:
            print("\t", end ="", flush=True, file = f3)

        while ((i < len(scan_swath)) and (i >= 0)):
            print(scan_swath[i], "\t", end ="", flush=True)
            print(scan_swath[i], "\t", end ="", flush=True, file = f)
            if display_count == 1:
                print(scan_swath[i], "\t", end ="", flush=True, file = f3)
            i += scanspeed
            

        print("")
        print("", file = f)
        print("", file = f3)

        if scan_direction == 1:
            print('->',"\t", end="", flush=True, file = f3)
        else:
            print('<-',"\t", end="", flush=True, file = f3)

        a = 0

    #This section needs to be double checked, it seems to be working, but need to make sure all cases are accounted for
        while ((current_scan_location <= scan_boundry_right) and (current_scan_location >= scan_boundry_left)):
            if (current_scan_location in target_locations):
                while (a < len(target_powers)): 
                    if (target_locations[a] == current_scan_location and target_powers[a] >= detection_threshold and fabs(target_velocities[a]) >= mtr_setting     #speed filtering
                        and ((fabs(heading_differences[a]) >= 15 and (radar_mode == HIGH_PRF_AIR_TO_AIR_SEARCH)                                                    #heading check in high PRF
                        or radar_mode == MED_PRF_AIR_TO_AIR_SEARCH or radar_mode == NORMAL_SCAN))):                                                                     #modes
                        print('#',"\t", end="", flush=True)
                        print('#',"\t", end="", flush=True, file = f)
                        print('#',"\t", end="", flush=True, file = f3)
                        targets_detected.append(current_scan_location)
                        a += 1
                        break                   
                    elif target_locations[a] == current_scan_location and (target_powers[a] < detection_threshold or target_velocities[a] < mtr_setting
                        or heading_differences[a] < 15):
                        print('=', "\t", end="", flush=True)
                        print('=', "\t", end="", flush=True, file = f)
                        print('=', "\t", end="", flush=True, file = f3)
                        a += 1
                        break 
                    else:
                        a += 1
            else:
                print('=', "\t", end="", flush=True)
                print('=', "\t", end="", flush=True, file = f)
                print('=', "\t", end="", flush=True, file = f3)

                        
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
        target_headings_output = target_headings
        heading_differences_output = heading_differences
        target_velocities_output = target_velocities
        current_scan_location_output = current_scan_location
        scanspeed_output = scanspeed
        current_scan_number_output = current_scan_number
        radar_mode_output = radar_mode
        targets_detected.sort()
        targets_detected_output = targets_detected
        mtr_setting_output = mtr_setting

    ################PRINTING##################################################

        print("")
        print("", file = f)
        print("", file = f3)
        #print("", file = f3)
        print("The current Radar Mode is: ", radar_mode_output)
        print("The current Radar Mode is: ", radar_mode_output, file = f)
        print("Target Locations Are: ", target_location_output)
        print("Target Locations Are: ", target_location_output, file = f)
        print("Target Powers Are: ", target_powers_output)
        print("Target Powers Are: ", target_powers_output, file = f)
        print("Target Speeds are: ", target_speeds_output)
        print("Target Speeds are: ", target_speeds_output, file = f)
        print("Current Aircraft Heading is: ", aircraft_1.heading)
        print("Current Aircraft Heading is: ", aircraft_1.heading, file = f)
        print("Target Headings are: ", target_headings_output)
        print("Target Headings are: ", target_headings_output, file = f)
        print("Target Heading Differences are: ", heading_differences_output)
        print("Target Heading Differences are: ", heading_differences_output, file = f)
        print("MTR Setting is: ", mtr_setting_output)
        print("MTR Setting is: ", mtr_setting_output, file = f)
        print("Target Velocities are: ", target_velocities_output)
        print("Target Velocities are: ", target_velocities_output, file = f)
        print("Targets were detected in these locations: ", targets_detected_output)
        print("Targets were detected in these locations: ", targets_detected_output, file = f)
        #print("The scan speed was: ", scanspeed_output)
        #print("The scan speed was: ", scanspeed_output, file = f)
        print("", file = f)
        print("")


    #################UPDATE TARGETS FOR NEXT SCAN################################

        target_powers = target_1.change_power(90, target_list, target_1.name)
        target_powers = target_2.change_power(50, target_list, target_2.name)
        target_locations = target_2.change_location(7, target_list, target_2.name)
        target_speeds = target_2.change_speed(40, target_list, target_2.name)
        target_speeds = target_1.change_speed(65, target_list, target_1.name)
        target_headings = target_1.change_heading(375, target_list, target_1.name)
        target_headings = target_3.change_heading(120, target_list, target_3.name)
        aircraft_1.change_aircraft_heading(450, aircraft_1.name)

        current_bar_number += 1
        display_count += 1
    current_scan_number += 1
    display_count = 1



#print(target_powers[1])
#print(target_powers[2])

f.close()
f3.close()

#power check implemented and working
#next  maybe make scenario control it's own file then import
#maybe next implement speed/mtr filter (finished 3/27/2020)
#add log that records when target characteristics are changed

#in the future implement beam structure, target range, target elevation, target xyz, add in elevation angles, bars, different modes
