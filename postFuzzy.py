#!/usr/bin/env python
import os
import time
import datetime
from time import strftime
import smbus
import urllib2
from fuzzy.fuzzy import fuzzy

bus = smbus.SMBus(1)

# alamat i2c, disamain dgn yg di arduino->0x2a
address = 0x2a
header = 'iotpln2016'

def post_data_sensor(datetime,idSensor,nilai):
	data = '{"datetime":"'+str(datetime)+'","id_sensor": "'+str(idSensor)+'","nilai_sensor":"'+str(nilai)+'","header":"'+str(header)+'"}'
	url = 'http://agungdp.agri.web.id:3456/api/sensor'
	req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	for x in f:
	    print(x)
	f.close()

def post_data_fuzzy(varFuzzy,datetime):
	data = '{"datetime":"'+str(datetime)+'","fuzzy_rendah": "'+str(varFuzzy[0])+'","fuzzy_sedang":"'+str(varFuzzy[1])+'","fuzzy_tinggi":"'+str(varFuzzy[2])+'","header":"'+str(header)+'"}'
	url = 'http://agungdp.agri.web.id:3456/api/fuzzy'
	req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	for x in f:
	    print(x)
	f.close()

def writeNumber(value):
	bus.write_byte(address, value)
	return -1

def bacaSensor():
	data = []
	jumlah = 0
	for i in range(0, 4):
		val = bus.read_byte(address)
		jumlah+=val
		data.append(val)
	data.append(jumlah)
	return jumlah

def hitungFuzzy(valLDR, valBat, datetime):
	# membership function variabel cahaya
	cahayarendah = [0,450,550] # trapezoid
	cahayasedang = [500,600,800] # segitiga
	cahayatinggi = [650,950] # trapezoid

	# membership function variabel baterai
	bateraisedikit = [0,1,3]
	bateraisedang = [2,4,6]
	bateraibanyak = [5,7]
	initFuzzy = fuzzy(valLDR,valBat,1)
	initFuzzy.membershipCahaya(cahayarendah,cahayasedang,cahayatinggi)
	initFuzzy.membershipBaterai(bateraisedikit,bateraisedang,bateraibanyak)

	getFuzzyCahaya = initFuzzy.fuzzifikasiCahaya()
	post_data_fuzzy(getFuzzyCahaya,datetime)
	print getFuzzyCahaya

var = 1
while True:
	writeNumber(var)
	print "RPI: Kirim ke arduino-> ", var
	time.sleep(1)

	value = bacaSensor()
	print "Arduino: terima dari RPI-> ", value

	datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
	post_data_sensor(datetimeWrite,var,value)
	print "Mengirim data sensor ke server..."
	time.sleep(1)

	hitungFuzzy(value,var,datetimeWrite)
	time.sleep(1)
	print "Mengirim informasi fuzzy ke server..."

	# var = var+1
	# if var==4:
	# 	var = 1
	time.sleep(30) # delay 30 detik
