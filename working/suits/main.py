import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time
import os

pinfootLeft         = "P8_7"
pinfootRight        = "P8_8"
pintibiaLeft        = "P8_9"
pintibiaRight       = "P8_10"
pinthighLeft   	 = "P8_11"
pinthighRight 	   	 = "P8_12"
pinhandLeft         = "P8_14"
pinhandRight        = "P8_15"
pinforearmLeft      = "P8_16"
pinforearmRight     = "P8_17"
pinbicepsLeft       = "P8_18"
pinbicepsRight      = "P8_26"

pinbackLeft         = "P9_12"
pinbackRight        = "P9_15"
pinbackPelvis       = "P9_23"
pinfrontSternum     = "P9_25"
pinfrontBellybutton = "P9_27"
pinfrontPelvis      = "P9_30"
pinhead             = "P9_41"


filer1  = open('st/1.txt', 'r') 
filer2  = open('st/2.txt', 'r') 
filer3  = open('st/3.txt', 'r') 
filer4  = open('st/4.txt', 'r') 
filer5  = open('st/5.txt', 'r') 
filer6  = open('st/6.txt', 'r') 
filer7  = open('st/7.txt', 'r') 
filer8  = open('st/8.txt', 'r') 
filer9  = open('st/9.txt', 'r') 
filer10  = open('st/10.txt', 'r') 
filer11  = open('st/11.txt', 'r') 
filer12  = open('st/12.txt', 'r') 
filer13  = open('st/13.txt', 'r') 
filer14  = open('st/14.txt', 'r') 
filer15  = open('st/15.txt', 'r') 
filer16  = open('st/16.txt', 'r') 
filer17  = open('st/17.txt', 'r') 
filer18  = open('st/18.txt', 'r') 
filer19  = open('st/19.txt', 'r') 


lefthand = filer17.readline()

leftforearm = filer13.readline()
leftforearm = filer13.readline()

leftbiceps = filer14.readline()
leftbiceps = filer14.readline()
leftbiceps = filer14.readline()

righthand = filer18.readline()
righthand = filer18.readline()
righthand = filer18.readline()
righthand = filer18.readline()

rightforearm = filer15.readline()
rightforearm = filer15.readline()
rightforearm = filer15.readline()
rightforearm = filer15.readline()
rightforearm = filer15.readline()

rightbiceps = filer16.readline()
rightbiceps = filer16.readline()
rightbiceps = filer16.readline()
rightbiceps = filer16.readline()
rightbiceps = filer16.readline()
rightbiceps = filer16.readline()

leftshoulder = filer7.readline()
leftshoulder = filer7.readline()
leftshoulder = filer7.readline()
leftshoulder = filer7.readline()
leftshoulder = filer7.readline()
leftshoulder = filer7.readline()
leftshoulder = filer7.readline()

rightshoulder = filer8.readline()
rightshoulder = filer8.readline()
rightshoulder = filer8.readline()
rightshoulder = filer8.readline()
rightshoulder = filer8.readline()
rightshoulder = filer8.readline()
rightshoulder = filer8.readline()
rightshoulder = filer8.readline()

pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()
pelvisback = filer9.readline()

pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()
pelvisfront = filer10.readline()

bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()
bellybutton = filer11.readline()

sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()
sternum = filer12.readline()

head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()
head = filer19.readline()

leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()
leftthigh = filer4.readline()

lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()
lefttibia = filer3.readline()

leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()
leftfoot = filer1.readline()

rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()
rightthigh = filer6.readline()

righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()
righttibia = filer5.readline()

rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()
rightfoot = filer2.readline()





def writeToFile():
	filew.write("Left hand;"+lefthand)
	filew.write("Left forearm;"+leftforearm)
	filew.write("Left biceps;"+leftbiceps)
	filew.write("Right hand;"+righthand)
	filew.write("Right forearm;"+rightforearm)
	filew.write("Right biceps;"+rightbiceps)
	filew.write("Left shoulder;"+leftshoulder)
	filew.write("Right shoulder;"+rightshoulder)
	filew.write("Back pelvis;"+pelvisback)
	filew.write("Front pelvis;"+pelvisfront)
	filew.write("Belly button;"+bellybutton)
	filew.write("Sternum;"+sternum)
	filew.write("Head;"+head)
	filew.write("Left thigh;"+leftthigh)
	filew.write("Left tibia;"+lefttibia)
	filew.write("Left foot;"+leftfoot)
	filew.write("Right thigh;"+rightthigh)
	filew.write("Right tibia;"+righttibia)
	filew.write("Right foot;"+rightfoot)


#*****LED blinking to show you can start walking after leds stopped blinking*****#
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 255 > brightness")
time.sleep(1)
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")
time.sleep(0.2)
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 255 > brightness")
time.sleep(1)
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")
time.sleep(0.2)
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 255 > brightness")
time.sleep(1)
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")
time.sleep(0.2)
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 255 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 255 > brightness")


filename = "output.txt"
filew = open(filename,'w')
filew.write("Sensor,Timestamp,Acceleration x,Acceleration y,Acceleration z,Gyroscope x,Gyroscope y,Gyroscope z" + '\n')

#leds blinking


sampletime = 10
starttime = time.time()
timeout = starttime+sampletime
numberofIMUs = 19

writeToFile()

while True:
	if leftfoot !='':
		temp = leftfoot.split(',')
		tijd=temp[0]
	if float(tijd)<sampletime:
		for i in range(numberofIMUs):
			leftfoot = filer1.readline()
			rightfoot = filer2.readline()
			lefttibia = filer3.readline()
			leftthigh = filer4.readline()
			righttibia = filer5.readline()
			rightthigh = filer6.readline()
			leftshoulder = filer7.readline()
			rightshoulder = filer8.readline()
			pelvisback = filer9.readline()
			pelvisfront = filer10.readline()
			bellybutton = filer11.readline()
			sternum = filer12.readline()
			leftforearm = filer13.readline()
			leftbiceps = filer14.readline()
			rightforearm = filer15.readline()
			rightbiceps = filer16.readline()
			lefthand = filer17.readline()
			righthand = filer18.readline()
			head = filer19.readline()


		writeToFile()

	if time.time()>timeout:
		filew.close()



		#fileHandle = open (filename,"r" )
		#lineList = fileHandle.readlines()
		#fileHandle.close()
		##lines = lineList[:-1]
		#os.system("rm " + filename)
		#filew2= open(filename,'w')
		#filew2.writelines([item for item in lineList[:-1]])
		#filew2.close()

		break

os.system("cp "+ filename+ " /var/www/html/datafiles")




#*****LEDs turn off to show you can stop walking*****#
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")

