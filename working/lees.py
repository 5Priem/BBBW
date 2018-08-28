import time


filer  = open('lgo.csv', 'r') 
filer.readline()

filew = open ('output.csv','w')


sampletime = 5
starttime = time.time()
timeout = starttime+sampletime

while True:
	value = filer.readline()
	if value != '':
		temp = value.split(',')
		tijd = temp[1]
	if float(tijd)<5:
		filew.write(str(value)+'\n')
	

	if time.time()>timeout:
		#print("gedaan")
		break
