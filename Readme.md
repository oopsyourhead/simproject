# 	This file is a very simple 1-Dimensional python simulation of a radar system scanning across a swath of azimuth and detecting and displaying targets
##  	it will output a text file (output.txt) that will contain the outputs, as well as a console output
##		multiple scans has been implemented as of 3/25/2020

#### 	maybe next implement speed/mtr filter (changed filter to account for target headings, implemented 3/27/2020)
####	implement a logging function to record when target characteristics change (finished 3/30/2020)
####	implement heading differences between aircraft and target, begin implementing different mode searches (started 3/31/2020)
####	implement ability to change aircraft characteristics with function calls in Aircraft Class (started and finished 4/1/2020)

###		next i want to implement a way to automatically track how many target objects you create, so the program can scale automatically (started and finished 04/02/2020)
###		improve automatic scaling to use function call to create target list?? protect trig function inputs to be between -360 and 360 degrees (-2xPi to 2xPi)? (completed 	
###   	4/3/2020)
###		implement -180 to 180 degrees heading protection (started 04/06/2020)
###		next, make another output file that only outputs the display format (started 4/16/2020 finished 4/17/2020)
###		implement multiple bar scans/2 dimensions (started 4/17/2020)
			<p> another thing to implement is the ability to change map centers easier and more intuitively</p>

####	in the future implement 2 dimensions for targets, beam structure, target range, target elevation, target xyz, add in elevation angles, bars, different modes
