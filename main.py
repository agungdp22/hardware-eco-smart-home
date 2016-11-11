#!/usr/bin/env python
import time
from time import strftime
import smbus
from fuzzy.fuzzy import fuzzy
from API.getAPI import getAPI
from API.postAPI import postAPI

bus = smbus.SMBus(1)

# alamat i2c, disamain dgn yg di arduino->0x2a
address = 0x2a
header = 'iotpln2016'

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

def hitungFuzzy(valLDR, valBat):
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
	print getFuzzyCahaya
	return getFuzzyCahaya

var = 1
postdata = postAPI(header)
getdata = getAPI(header)

while True:
	pil = int(input("Pilih pilihan: "))
	if pil==1:
		writeNumber(var)
		print "RPI: Kirim ke arduino-> ", var
		time.sleep(1)

		value = bacaSensor()
		print "Arduino: terima dari RPI-> ", value

		datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
		postdata.sensor(datetimeWrite,var,value)
		print "Mengirim data sensor ke server..."
		time.sleep(1)

		varFuzzy = hitungFuzzy(value,var)
		postdata.fuzzy(datetimeWrite,varFuzzy)
		time.sleep(1)
		print "Mengirim informasi fuzzy ke server..."

		# var = var+1
		# if var==4:
		# 	var = 1
		time.sleep(30) # delay 30 detik
	elif pil==2:
		print getdata.sensor()
