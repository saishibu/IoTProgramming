import serial,pynmea2,time,datetime
# import subprocess,os
from time import mktime

port = serial.Serial("/dev/ttyUSB0", baudrate=9600)

t = datetime.datetime.now()
# unix_secs = mktime(t.timetuple())

a=1
while a:
	rcv = port.readline()
#	print rcv[0:6]
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		#print msg
		lat=msg.lat
		lat=pynmea2.dm_to_sd(lat)
		#print type (lat)
		lon=msg.lon
		lon=pynmea2.dm_to_sd(lon)
		#print lon
	if rcv[0:6] == '$GPRMC':
		msg=pynmea2.parse(rcv)
		#print msg
		speed=msg.spd_over_grnd
		#print speed
		a=0
data={'time':t,'lat':lat,'lon':lon,'speed':speed}
print(data)

print("GPS Updated")
