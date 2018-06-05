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

ledpin="P9_41"
wirepin="P8_7"

print("initialising GPIOS")
GPIO.setup(wirepin,GPIO.IN)
GPIO.setup(ledpin,GPIO.OUT)
GPIO.output(ledpin,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(ledpin,GPIO.LOW)
time.sleep(0.5)
GPIO.output(ledpin,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(ledpin,GPIO.LOW)
time.sleep(0.5)
GPIO.output(ledpin,GPIO.HIGH)
#GPIO.setup("P8_11",GPIO.OUT)
#GPIO.output("P8_11",GPIO.LOW)
#GPIO.setup("P8_9",GPIO.OUT)
#GPIO.output("P8_9",GPIO.LOW)


try:
    mp = mpu9250.SL_MPU9250(0x68,2)
except:
	print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")

sampleTime=70
ctr=1
ctrFilenames = 56
waitforRestart=0

while True:
    if GPIO.input(wirepin)==1:
        if waitforRestart==0:
            timeout = time.time() + sampleTime
            while time.time()<timeout:
                if ctr==1:
                    ctrFilenames=ctrFilenames+1
                    print("started for " +str(sampleTime)+ "seconds to file: "+str(ctrFilenames))
                    ctr=2
                GPIO.output(ledpin,GPIO.HIGH)
                ax, ay, az = mp.getAccel()
                gx, gy, gz = mp.getGyro()
                data = open(str(ctrFilenames)+ '.txt', 'a+')
                data.write(str(time.time())+','+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz)+'\n')
                GPIO.output(ledpin,GPIO.LOW)
        #print("done writing")
        waitforRestart = 1
        ctr=1
    
    else:
        GPIO.output(ledpin,GPIO.LOW)
        waitforRestart=0

