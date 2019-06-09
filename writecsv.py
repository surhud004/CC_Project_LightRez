import serial
import time
import datetime
import csv

ser = serial.Serial('COM4', 9600)

print("connected to: " + ser.portstr)
filename = "data" + str(datetime.datetime.fromtimestamp(time.time()).strftime('%d%m%Y')) + ".csv"
print(filename)

with open(filename, 'a', newline='') as csvFile:
	while True:
		try:
			line = str(ser.readline().decode('utf-8'))
			line = line.rstrip()
			#timestamp = str(time.time())
			now = time.strftime('%d-%m-%Y %H:%M:%S')
			print(now+" -> "+line)
			each = line.split(":")
		
			writer = csv.writer(csvFile, delimiter=",")
			writer.writerow([now, each[0], each[1]])
		except:
			csvFile.close()
			print("Keyboard Interrupt")
			break
ser.close()