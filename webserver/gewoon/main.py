# -*- coding: utf-8 -*-
# https://github.com/pallets/flask/tree/0.12.4/examples/jqueryexample
from flask import Flask, jsonify, render_template, request
import mpu9250
import os
app = Flask(__name__)

a = 4
try:
        mp1 = mpu9250.SL_MPU9250(0x68,2)
except:
        print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")

from subprocess import check_output
ips = check_output(['hostname', '--all-ip-addresses'])
print(ips)

@app.route('/_showValues')
def showValues():
    #global a
    #a = a+1#x#request.args.get('a', 0, type=int)
    ax, ay, az = mp1.getAccel()
    gx, gy, gz = mp1.getGyro()
    return jsonify(result=str(ax)+"!"+str(ay)+"!"+str(az)+"!"+str(gx)+"!"+str(gy)+"!"+str(gz))

@app.route('/_showFiles')
def showFiles():
    datafiles = os.listdir("/var/www/html/datafiles")
    allfiles = ""
    for i in range(0,len(datafiles)):
        allfiles=allfiles + ","+datafiles[i]
    return jsonify(result2=allfiles)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.0.124')
