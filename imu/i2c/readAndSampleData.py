#Library from:
#https://github.com/boyaki-machine/MPU-9250/blob/master/mpu9250.py

#Connections:
#SDA - SDA
#SCL - SCL
#3.3V - VDD
#GND - GND
#Pull up resistor to VDD for each IMU (I used 10k)

import mpu9250
import Adafruit_BBIO.GPIO as GPIO
import time
import os
from decimal import Decimal
import smbus2

#GPIO.setup("P8_8",GPIO.OUT)
#GPIO.output("P8_8",GPIO.LOW)
#GPIO.setup("P8_7",GPIO.OUT)
#GPIO.output("P8_7",GPIO.HIGH)
#GPIO.setup("P8_9",GPIO.OUT)
#GPIO.output("P8_9",GPIO.HIGH)

#try:
	#mp1 = mpu9250.SL_MPU9250(0x68,2)
	#mp2 = mpu9250.SL_MPU9250(0x69,2)
#except:
	#print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")
fileName = "sampleData400tryH"
sampleFreq = 100
sampleTime = 5

data = open(fileName+ '.txt', 'a+')
#data.write("CSV format: Accelerometer x value, acclerometer y value, accelerometer z value, gyroscope x value, gyroscope y value, gyroscope z value"+'\n')
#data.write("Sample frequency: " + str(sampleFreq)+"Hz"+'\n')
#data.write("Sample time: " + str(sampleTime)+"sec"+'\n')
ctr = 1
timeout = time.time() + sampleTime
variabele = ""
#mp1.resetRegister()
#mp1.powerWakeUp()
#mp1.setAccelRange(8,True)
#mp1.setGyroRange(1000,True)
#mp1.setMagRegister('100Hz','16bit')

bus=smbus2.SMBus(2)
ctr =0
while True:
	#try:
	#gx1 = "1"
	#gy1 = "1"
	#gz1 = "1"

	#ax1, ay1, az1 = mp1.getAccel()
	#gx1, gy1, gz1 = mp1.getGyro()
	dataAccel = bus.read_i2c_block_data(0x68, 0x3B ,1)
	#print(str(data))
	#print(Decimal(time.time()))
	#data.write(str(Decimal(time.time()))+", "+str(dataAccel) +'\n')
	#data.write(str(dataAccel) +'\n')
	ctr=ctr+1

	#print "Eerste IMU values:"
	#voortijd = time.time()
	#print(time.time())
	#natijd = time.time()
	#data.write("voortijd: "+str(voortijd)+"natijd: "+str(natijd)+ '\n')
	#print "Ax1: ",ax1
	#print "Ay1: ",ay1
	#print "Az1: ",az1

	#print "Gx1: ",gx1
	#print "Gy1: ",gy1
	#print "Gz1: ",gz1
	#data.write(str(time.time())+str(ax1)+','+str(ay1)+','+str(az1)+','+str(gx1)+','+str(gy1)+','+str(gz1)+'\n')
	#data.write(str(time.time())+str(ax1)+','+str(ay1)+','+str(az1)+'\n')
	#time.sleep(float(1)/sampleFreq)

	if time.time()>timeout:
		data.write("counter: "+str(ctr))
		data.close()
		break

	#except:
		#print("Finito1")
