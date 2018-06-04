#Library from:
#https://github.com/boyaki-machine/MPU-9250/blob/master/mpu9250.py

#Connections:
#SDA - SDA
#SCL - SCL
#3.3V - VDD
#GND - GND
#Pull up resistor to VDD for each IMU (I used 10k)

#try:
import mpu9250
#except:
#    print("import mpu9250 mislukt")
import Adafruit_BBIO.GPIO as GPIO
import time
import os

print("initialising GPIOS")
GPIO.setup("P9_12",GPIO.OUT)
GPIO.output("P9_12",GPIO.HIGH)
#GPIO.setup("P8_15",GPIO.OUT)
#GPIO.output("P8_15",GPIO.LOW)
#GPIO.setup("P8_11",GPIO.OUT)
#GPIO.output("P8_11",GPIO.LOW)
#GPIO.setup("P8_9",GPIO.OUT)
#GPIO.output("P8_9",GPIO.LOW)


try:
    mp1 = mpu9250.SL_MPU9250(0x69,2)
	#mp2 = mpu9250.SL_MPU9250(0x69,2)
except:
	print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")

filename = "sampleData"
data = open(filename+ '.txt', 'a+')
sampleTime=5
timeout = time.time() + sampleTime
print("started")
while True:
	try:
		ax1, ay1, az1 = mp1.getAccel()
		gx1, gy1, gz1 = mp1.getGyro()
        	#print(ax1)
                data.write(str(time.time())+str(ax1)+','+str(ay1)+','+str(az1)+','+str(gx1)+','+str(gy1)+','+str(gz1)+'\n')
                if time.time()>timeout:
                    data.close()
                    print("5 seconden om")
                    break


	except:
		print("Finito1")

