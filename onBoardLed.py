import os
import time

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
