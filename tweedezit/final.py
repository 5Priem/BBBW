import mpu9250
import Adafruit_BBIO.GPIO as GPIO
import time
import os
from decimal import Decimal
import smbus2

wirePin = "P8_8"
ledPin = "P9_41"

GPIO.setup(wirePin, GPIO.IN)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.output(ledPin,GPIO.HIGH)

try:
	mp1 = mpu9250.SL_MPU9250(0x68,2)
	#mp2 = mpu9250.SL_MPU9250(0x69,2)
except:
	print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")

fileCounter = open("counter.txt","r")
counter = int(fileCounter.read())
counter = counter + 1
fileCounter.close()
fileName = str(counter)

def setLedsHIGH():
	os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 255 > brightness")
	os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 255 > brightness")
	os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 255 > brightness")
	os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 255 > brightness")


def setLedsLOW():
	os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
	os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
	os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
	os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")

def blinkLeds():

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



	#GPIO.output(ledPin, GPIO.LOW)
	#time.sleep(2)
	#GPIO.output(ledPin, GPIO.HIGH)
	#time.sleep(1)
	#GPIO.output(ledPin, GPIO.LOW)
	#time.sleep(1)
	#GPIO.output(ledPin, GPIO.HIGH)
	#time.sleep(1)
	#GPIO.output(ledPin, GPIO.LOW)
	#time.sleep(1)
	#GPIO.output(ledPin, GPIO.HIGH)
	#time.sleep(1)
	#GPIO.output(ledPin, GPIO.LOW)
	#time.sleep(1)



data = open(fileName+ '.txt', 'a+')
#data.write("CSV format: Accelerometer x value, acclerometer y value, accelerometer z value, gyroscope x value, gyroscope y value, gyroscope z value"+'\n')

sampleTime = 2
bus=smbus2.SMBus(2)
boolPin = GPIO.input(wirePin)
blinkLeds()
setLedsLOW()

timeout = time.time() + sampleTime
while True:
	try:
		#ax, ay, az = mp1.getAccel()
		#gx, gy, gz = mp1.getGyro()
		ax="1"
		ay="1"
		az="1"
		gx="1"
		gy="1"
		gz="1"
		
		data.write(str(Decimal(time.time()))+', '+str(ax) +str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz)+'\n')
	
		if time.time()>timeout:
			data.close()
			setLedsHIGH()
			while GPIO.input(wirePin) == boolPin:
				pass
			boolPin = not boolPin	
			counter = counter + 1
			dataWriteCtr=open("counter"+".txt","w+")
			dataWriteCtr.write(str(counter))
			
			fileName=str(counter)
			data = open(fileName+ '.txt', 'a+')
			
			blinkLeds()

			setLedsLOW()
			timeout = time.time()+ sampleTime
			#break

	except:
		print("Data is not being read anymore.")
		break

