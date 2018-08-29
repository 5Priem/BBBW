import time
import os

filer1  = open('1.txt', 'r') 
filer2  = open('2.txt', 'r') 
filer3  = open('3.txt', 'r') 


filename = "difficultoutput.txt"
filew = open(filename,'w')
filew.write("Sensor,Timestamp,Acceleration x,Acceleration y,Acceleration z,Gyroscope x,Gyroscope y,Gyroscope z" + '\n')

#leds blinking


sampletime = 4
starttime = time.time()
timeout = starttime+sampletime


lefthand = filer1.readline()
righthand = filer2.readline()
righthand = filer2.readline()
leftbiceps = filer3.readline()
leftbiceps = filer3.readline()
leftbiceps = filer3.readline()
filew.write("Left hand,"+lefthand)
filew.write("Right hand,"+righthand)
#filew.write("Left biceps,"+leftbiceps)




while True:
	if lefthand !='':
		temp = lefthand.split(',')
		tijd=temp[0]
	if float(tijd)<sampletime:
		for i in range(2):
			lefthand = filer1.readline()
			righthand = filer2.readline()
			leftbiceps = filer3.readline()
		filew.write("Left hand,"+lefthand)
		filew.write("Right hand,"+righthand)
		#filew.write("Left biceps,"+leftbiceps)

	#righthand = filer2.readline()
	#filew.write("Right hand,"+righthand)

	#leftbiceps = filer3.readline()
	#filew.write("Left biceps,"+leftbiceps)
	
	if time.time()>timeout:
		filew.close()

		fileHandle = open (filename,"r" )
		lineList = fileHandle.readlines()
		fileHandle.close()
		#lines = lineList[:-1]
		os.system("rm " + filename)
		filew2= open(filename,'w')
		filew2.writelines([item for item in lineList[:-1]])
		filew2.close()

		break










