import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time
import os

#*********SETUP*********#
try:
	mp=mpu9250.SL_MPU9250(0x69, 2)
except:
	print("First IMU (in Setup) not found")
footLeft         = "P8_7"
footRight        = "P8_8"
tibiaLeft        = "P8_9"
tibiaRight       = "P8_10"
thighLeft   	 = "P8_11"
thighRight 	   	 = "P8_12"
handLeft         = "P8_14"
handRight        = "P8_15"
forearmLeft      = "P8_16"
forearmRight     = "P8_17"
bicepsLeft       = "P8_18"
bicepsRight      = "P8_26"

backLeft         = "P9_12"
backRight        = "P9_15"
backPelvis       = "P9_23"
frontSternum     = "P9_25"
frontBellybutton = "P9_27"
frontPelvis      = "P9_30"
head             = "P9_41"

print("Initialising GPIO's...")
GPIO.setup(footLeft, GPIO.OUT)
GPIO.setup(footRight, GPIO.OUT)
GPIO.setup(tibiaLeft, GPIO.OUT)
GPIO.setup(tibiaRight, GPIO.OUT)
GPIO.setup(thighLeft, GPIO.OUT)
GPIO.setup(thighRight, GPIO.OUT)
GPIO.setup(handLeft, GPIO.OUT)
GPIO.setup(handRight, GPIO.OUT)
GPIO.setup(forearmLeft, GPIO.OUT)
GPIO.setup(forearmRight, GPIO.OUT)
GPIO.setup(bicepsLeft, GPIO.OUT)
GPIO.setup(bicepsRight, GPIO.OUT)

GPIO.setup(backLeft, GPIO.OUT)
GPIO.setup(backRight, GPIO.OUT)
GPIO.setup(backPelvis, GPIO.OUT)
GPIO.setup(frontSternum, GPIO.OUT)
GPIO.setup(frontBellybutton, GPIO.OUT)
GPIO.setup(frontPelvis, GPIO.OUT)
GPIO.setup(head, GPIO.OUT)


GPIO.output(footLeft, GPIO.LOW)
GPIO.output(footRight, GPIO.LOW)
GPIO.output(tibiaLeft, GPIO.LOW)
GPIO.output(tibiaRight, GPIO.LOW)
GPIO.output(thighLeft, GPIO.LOW)
GPIO.output(thighRight, GPIO.LOW)
GPIO.output(handLeft, GPIO.LOW)
GPIO.output(handRight, GPIO.LOW)
GPIO.output(forearmLeft, GPIO.LOW)
GPIO.output(forearmRight, GPIO.LOW)
GPIO.output(bicepsLeft, GPIO.LOW)
GPIO.output(bicepsRight, GPIO.LOW)

GPIO.output(backLeft, GPIO.LOW)
GPIO.output(backRight, GPIO.LOW)
GPIO.output(backPelvis, GPIO.LOW)
GPIO.output(frontSternum, GPIO.LOW)
GPIO.output(frontBellybutton, GPIO.LOW)
GPIO.output(frontPelvis, GPIO.LOW)
GPIO.output(head, GPIO.LOW)

fileName = "dataIMUSuit"

print("Initialisation finished, gonna write to " + fileName + " and start reading now")
data.write("Sensor,Timestamp,Acceleration x,Acceleration y,Acceleration z,Gyroscope x,Gyroscope y,Gyroscope z" + '\n')


data = open(fileName + '.txt', 'a+')

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



sampleTime = 60 # 1 minute
startTime = time.time()
timeout = startTime + sampleTime
#*********LOOP*********#
while True:
    #*****Left hand*****#
    try:
        GPIO.output(footRight, GPIO.LOW)
        GPIO.output(handLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left hand,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left hand failed to connect")

    #*****Left forearm*****#
    try:
        GPIO.output(handLeft, GPIO.LOW)
        GPIO.output(forearmLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left forearm,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left forearm failed to connect")

    #*****Left biceps*****#
    try:
        GPIO.output(forearmLeft, GPIO.LOW)
        GPIO.output(bicepsLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left biceps,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left biceps failed to connect")

    #****Right hand*****#
    try:
        GPIO.output(bicepsLeft, GPIO.LOW)
        GPIO.output(handRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right hand,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Right hand failed to connect")

    #*****Right forearm*****#
    try:
        GPIO.output(handRight, GPIO.LOW)
        GPIO.output(forearmRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right forearm,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Right forearm failed to connect")

    #*****Right biceps*****#
    try:
        GPIO.output(forearmRight, GPIO.LOW)
        GPIO.output(bicepsRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right biceps,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Right biceps failed to connect")

    #*****Left shoulder*****#
    try:
        GPIO.output(bicepsRight, GPIO.LOW)
        GPIO.output(backLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left shoulder,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left shoulder failed to connect")

    #*****Right shoulder*****#
    try:
        GPIO.output(backLeft, GPIO.LOW)
        GPIO.output(backRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right shoulder,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Right shoulder failed to connect")

    #*****Back pelvis*****#
    try:
        GPIO.output(backRight, GPIO.LOW)
        GPIO.output(backPelvis, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Back pelvis,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Back pelvis failed to connect")

    #*****Front pelvis*****#
    try:
        GPIO.output(backPelvis, GPIO.LOW)
        GPIO.output(frontPelvis, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Front pelvis,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Front pelvis failed to connect")

    #*****Belly button*****#
    try:
        GPIO.output(frontPelvis, GPIO.LOW)
        GPIO.output(frontBellybutton, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Belly button,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Belly button failed to connect")

    #*****Sternum*****#
    try:
        GPIO.output(frontBellybutton, GPIO.LOW)
        GPIO.output(frontSternum, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Sternum,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Sternum failed to connect")

    #*****Head*****#
    try:
        GPIO.output(frontSternum, GPIO.LOW)
        GPIO.output(head, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Head,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Head failed to connect")

    #*****Left thigh*****#
    try:
        GPIO.output(head, GPIO.LOW)
        GPIO.output(thighLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left thigh,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left thigh failed to connect")

    #*****Left tibia*****#
    try:
        GPIO.output(thighLeft, GPIO.LOW)
        GPIO.output(tibiaLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left tibia,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left tibia failed to connect")

    #*****Left foot*****#
    try:
        GPIO.output(tibiaLeft, GPIO.LOW)
        GPIO.output(footLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left foot,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Left foot failed to connect")

    #*****Right thigh*****#
    try:
        GPIO.output(footLeft, GPIO.LOW)
        GPIO.output(thighRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right thigh,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Right thigh failed to connect")

    #*****Right tibia*****#
    try:
        GPIO.output(thighRight, GPIO.LOW)
        GPIO.output(tibiaRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right tibia,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    except:
        print("Right tibia failed to connect")

    #*****Right foot*****#
    try:
        GPIO.output(tibiaRight, GPIO.LOW)
        GPIO.output(footRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right foot,"+str(time.time()-startTime)+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    	data.close()
    except:
        print("Right foot to connect")
		
	if time.time()>timeout:
		data.close()
		break

data.close()
GPIO.cleanup()

#*****LEDs turn off to show you can stop walking*****#
os.system("cd /sys/class/leds/beaglebone:green:usr0 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr1 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr2 && echo 0 > brightness")
os.system("cd /sys/class/leds/beaglebone:green:usr3 && echo 0 > brightness")

