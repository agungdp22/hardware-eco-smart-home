#!/usr/bin/env python

import os
import time
import datetime
# import glob
# import MySQLdb
from time import strftime
# from MySQLdb import OperationalError
import smbus
import urllib2

bus = smbus.SMBus(1)

# alamat i2c, disamain dgn yg di arduino
address = 0x04
header = 'iotpln2016'
 
# db = MySQLdb.connect(host="agungdp.agri.web.id", user="agungdp_iotpln",passwd="iotpln2016", db="agungdp_iotpln")
# cur = db.cursor()

# def my_sql_operation(sql):
# 	print "Writing to database..."
# 	cur.execute(*sql)
# 	db.commit()
# 	print "Write Complete"

def post_data(datetime,idSensor,nilai):
	data = '{"datetime":"'+str(datetime)+'","id_sensor": "'+str(idSensor)+'","nilai_sensor":"'+str(nilai)+'","header":"'+str(header)+'"}'
	url = 'http://agungdp.agri.web.id:3456/api/sensor'
	req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	for x in f:
	    print(x)
	f.close()

def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def bacaSensor():
	value = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	return value

var = 1
while True:
	writeNumber(var)
	print "RPI: Kirim ke arduino-> ", var
	time.sleep(1)

	value = bacaSensor()
	print "Arduino: terima dari RPI-> ", value

	datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
	post_data(datetimeWrite,var,value)
	# sql = ("""INSERT INTO data_sensor (datetime,id_sensor,nilai_sensor) VALUES (%s,%s,%s)""",(datetimeWrite,var,value))
	# try:
	# 	my_sql_operation(sql)
	# except OperationalError as e:
	# 	db.reconnect()
	# 	print e
	# except:
	#     # Rollback in case there is any error
	#     db.rollback()
	#     print "Failed writing to database"
	# cur.close()
	# db.close()
	var = var+1
	if var==4:
		var = 1
	time.sleep(30) # delay 30 detik
