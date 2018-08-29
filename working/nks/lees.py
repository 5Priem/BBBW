import time
import os


filer  = open('sto.csv', 'r') 
filer.readline()

filename = "output.txt"
filew = open (filename,'w')
filew.write("Sensor,Timestamp,Acceleration x,Acceleration y,Acceleration z,Gyroscope x,Gyroscope y,Gyroscope z" + '\n')



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


sampletime = 9
starttime = time.time()
timeout = starttime+sampletime

while True:
	value = filer.readline()
	if value != '':
		temp = value.split(',')
		tijd = temp[1]
	if float(tijd)<sampletime:
		filew.write(str(value))
	

	if time.time()>timeout:
		#print("gedaan")
		filew.close()
		while True:
			fileHandle = open (filename,"r" )
			lineList = fileHandle.readlines()
			fileHandle.close()
			if lineList[len(lineList)-1].split(',')[0] != 'Right foot':
				lines = lineList[:-1]
				os.system("rm " + filename)
				filew2= open(filename,'w')
				filew2.writelines([item for item in lines[:-1]])
				filew2.close()
			else:
				break
			
		break



os.system("cp "+ filename+ " /var/www/html/datafiles")

#*****LEDs turn off to show you can stop walking*****#
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")

