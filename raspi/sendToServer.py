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
import numpy as np

bus = smbus.SMBus(1)

# alamat i2c, disamain dgn yg di arduino
address = 0x2a
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
	# value = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	# data = chr(bus.read_byte(address))
	data = []
	summ = 0
	for i in range(0, 4):
		val = bus.read_byte(address)
		summ+=val
		# data.append(bus.read_byte(address))
		data.append(val)
	data.append(summ)
	# hasil = 0
	# for i in range(np.size(data)):
	# 	hasil += data[i] * (2**(9-i))
	# 	# hasil+=val
	# data = 0
	# for i in range(0, 4):
	# 	data += int(bus.read_byte(address));
	return data

var = 1
while True:
	writeNumber(var)
	print "RPI: Kirim ke arduino-> ", var
	time.sleep(0.5)

	value = bacaSensor()
	print "Arduino: terima dari RPI-> ", value
	time.sleep(1)
	# datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
	# post_data(datetimeWrite,var,value)
	# # sql = ("""INSERT INTO data_sensor (datetime,id_sensor,nilai_sensor) VALUES (%s,%s,%s)""",(datetimeWrite,var,value))
	# # try:
	# # 	my_sql_operation(sql)
	# # except OperationalError as e:
	# # 	db.reconnect()
	# # 	print e
	# # except:
	# #     # Rollback in case there is any error
	# #     db.rollback()
	# #     print "Failed writing to database"
	# # cur.close()
	# # db.close()
	# var = var+1
	# if var==4:
	# 	var = 1
	# time.sleep(30) # delay 30 detik
